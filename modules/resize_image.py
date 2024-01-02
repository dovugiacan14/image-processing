import os
import cv2 
import logging 
import traceback

class RESIZE: 
    def __init__(self, in_path, out_path, min_size):
        self.in_path = in_path

        if not os.path.exists(out_path):
            os.makedirs(out_path) 
            
        self.out_path = out_path 
        self.min_size = min_size

    def resize_image(self): 
        try:
            logging.info("Start resizing image")
            if not os.path.exists(self.out_path):
                os.makedirs(self.out_path)

            count = 1
            for filename in os.listdir(self.in_path):
                input_path = os.path.join(self.in_path, filename)

                # read image content 
                img = cv2.imread(input_path)

                # resize image 
                if img.shape[0] < img.shape[1]:
                    size = img.shape[0]
                    size_resize = self.min_size/size
                    resize_img = cv2.resize(img, (int(img.shape[1] * size_resize), self.min_size))
                else:
                    size = img.shape[1]
                    size_resize = self.min_size/size 
                    resize_img = cv2.resize(img, (self.min_size, int(img.shape[0] * size_resize)))    

                # save resized image 
                output_filename = "image" + str(count) + ".png"
                output_path = os.path.join(self.out_path, output_filename)
                cv2.imwrite(output_path, resize_img)

                count += 1 

            logging.info("Successfully.!") 

        except Exception as e:
            logging.error(f"Error when resizing image: {e}")
            traceback.format_exc()
            return None 