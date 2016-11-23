import cv2
import os
import argparse

DEFAULT_OUTPUT_PATH = 'FaceCaptureImages/'
DEFAULT_CASCADE_INPUT_PATH = 'haarcascade_frontalface_alt.xml'
DEFAULT_IMAGES_PATH = '/Users/gotit/crawl_images/4/'


class DetectFace:
    """ Class for detecting faces """

    def __init__(self):
        self.argsObj = parse()
        self.face_cascade = cv2.CascadeClassifier(self.argsObj.input_path)
        self.count = 0

    def detect(self):
        """ Detect faces in images and save it """

        folder_path = os.path.join(self.argsObj.folder_path,'')
        output_path = os.path.join(self.argsObj.output_path,'')
        all_images = os.listdir(folder_path)
        for image_file in all_images:
            try:
                image = cv2.imread(os.path.join(folder_path, image_file))
                # set screen color to gray
                image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # customize the cascade
                faces = self.face_cascade.detectMultiScale(
                    image_gray,
                    scaleFactor=1.1,
                    minNeighbors=6,
                    minSize=(35, 35),
                    flags=cv2.CASCADE_SCALE_IMAGE
                )

                # number of faces detected
                if len(faces) == 0:
                    print "No face"
                elif len(faces) > 0:
                    print('Face Detected')

                    # draw the rectangle around faces
                    for (x, y, w, h) in faces:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.imwrite(output_path+image_file, image)
            except KeyboardInterrupt:
                break
            except:
                print "Ignore a file. It's ok."

            if not self.count%100:
                print 'number of images: ', self.count
            self.count += 1

    def clear_image_folder(self):
        """ Clear output path """

        if not (os.path.exists(self.argsObj.output_path)):
            os.makedirs(self.argsObj.output_path)

        else:
            for files in os.listdir(self.argsObj.output_path):
                file_path = os.path.join(self.argsObj.output_path, files)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                else:
                    continue


def parse():
    """ Get the command line arguments """

    parser = argparse.ArgumentParser(description='Cascade Path')
    parser.add_argument('-i', '--input_path', type=str,
                        default=DEFAULT_CASCADE_INPUT_PATH,
                        help='Cascade input path'
                        )
    parser.add_argument('-o', '--output_path', type=str,
                        default=DEFAULT_OUTPUT_PATH,
                        help='Output path'
                        )
    parser.add_argument('-f', '--folder_path', type=str,
                        default=DEFAULT_IMAGES_PATH,
                        help='Images folder path'
                        )
    args = parser.parse_args()
    return args


def main():
    face_detect_implementation = DetectFace()
    face_detect_implementation.clear_image_folder()
    face_detect_implementation.detect()


if __name__ == '__main__':
    main()
