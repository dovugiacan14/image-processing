import Augmentor
import logging 

class Augmentor:
    def __init__(self, image_folder):
        self.image_folder = image_folder

    def skew_image(self, magtitude, ratio):
        try: 
            logging.info("Start skewing image")
            p = Augmentor.Pipeline(self.image_folder)
            p.skew(magtitude, ratio)
            p.sample(1)
        except Exception as e:
            logging.error(f"Error in skewing image: {e}")
        return None 
    
    def flipping(self, ratio):
        try:
            logging.info("Start flipping image")
            p = Augmentor.Pipeline(self.image_folder)
            p.flip_left_right(ratio)
            p.sample(1)
        except Exception as e:
            logging.error(f"Error in flipping image: {e}")
        return None
    
    def rotate(self, ratio, max_left_rotation, max_right_rotation):
        try:
            logging.info("Start rotating image")
            p = Augmentor.Pipeline(self.image_folder)
            p.rotate(ratio, max_left_rotation, max_right_rotation)
            p.sample(1)
        except Exception as e:
            logging.error(f"Error in rotating image: {e}")
        return None
    


   
