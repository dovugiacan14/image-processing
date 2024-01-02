import argparse 
import logging 
import os 
import traceback
from config.api import * 
from modules.augmentation import Augmentor
from modules.captioning_image import CaptionImage
from modules.resize_image import RESIZE
from modules.upscale import UpscaleImage

def main(): 
    parser = argparse.ArgumentParser(description="Image augmentation")
    parser.add_argument("--method", type= int, default= 0, help= "Method to use")
    parser.add_argument("--port", type= int, default= 7860, help= "Port to use")
    parser.add_argument("--dir_in", type= str, default= "images/", help= "Directory containing the input images")
    parser.add_argument("--dir_out", type= str, default= "outputs/", help= "Directory to save the output images")
    parser.add_argument("--model", type= str, default= "clip", help= "Model to use for captioning")
    parser.add_argument("--prefix", type= str, default= "", help= "Prefix to add to each caption")
    parser.add_argument("--min_size", type= int, default= 1024, help= "Minimum size of the image")
    parser.add_argument("--type", type= int, default=0, help= "Type of augmentation")
    parser.add_argument("--magtitude", type= float, default= 0.3 , help= "Magtitude of skew method in augmentation")
    parser.add_argument("--ratio", type= float, default= 0.5, help= "The image's aspect ratio has been modified.")
    parser.add_argument("--max_left_rotation", type= float, default= 10, help= "The maximum angle to rotate the image to the left.")
    parser.add_argument("--max_right_rotation", type= float, default= 10, help= "The maximum angle to rotate the image to the right.")
    args = parser.parse_args()

    if args.method == 0:
        logging.info("Start captioning")

        url = DOMAIN + ":" + str(args.port) + INTERROGATE
        try:
            if args.model == "clip" or args.model == "deepdanbooru":
                caption = CaptionImage(url= url, model= args.model, dir_in= args.dir_in, dir_out= args.dir_out, prefix= args.prefix)
                caption.interrogate()
            else:  
                print("Model is invalid.! Try with clip or deepdanbooru.!")
                return None 
        except Exception as e:
            logging.error(f"Error in captioning: {e}")
            traceback.format_exc()
            return None
        
    elif args.method == 1:
        logging.info("Start augmentation")
        try:
            augmentor = Augmentor(args.dir_in)
            if args.type == 0:
                augmentor.skew_image(args.magtitude, args.ratio)
            elif args.type == 1:
                augmentor.flipping(args.ratio)
            elif args.type == 2:
                augmentor.rotate(args.ratio, args.max_left_rotation, args.max_right_rotation)
            else: 
                print("Type is invalid.! Try again.!")
                return None
        except Exception as e:
            logging.error(f"Error in augmentation: {e}")
            traceback.format_exc()
            return None
    
    elif args.method == 2:
        logging.info("Start resizing")
        try:
            resize = RESIZE(args.dir_in, args.dir_out, args.min_size)
            resize.resize_image()
        except Exception as e:
            logging.error(f"Error in resizing: {e}")
            traceback.format_exc()
            return None
    
    elif args.method == 3:
        logging.info("Start upscaling")
        url = DOMAIN + ":" + str(args.port) + UPSCALER
        payload_params = UPSCALE_PARAMS
        try:
            upscale = UpscaleImage(url= url, dir_in= args.dir_in, dir_out= args.dir_out, payload_params= payload_params)
            upscale.download_image()
        except Exception as e:
            logging.error(f"Error in upscaling: {e}")
            traceback.format_exc()
            return None
    
    else: 
        print("Method is invalid.! Try again.!")
        return None

if __name__ == "__main__":
    main()