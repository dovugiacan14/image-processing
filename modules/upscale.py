import json 
import requests 
import io 
import base64 
import os 
import traceback 
import logging 
from PIL import Image, PngImagePlugin 
from helpers import pil_to_base64, is_base64

class UpscaleImage:
    def __init__(self, url, dir_in, dir_out, payload_params):
        self.url = url 
        self.dir_in = dir_in
        if not os.path.exists(dir_out):
            os.makedirs(dir_out)
        self.dir_out = dir_out 
        self.payload_params = payload_params 
    
    def download_image(self):
        logging.info("Start downloading image.....")
        base64_img_lst = self.upscale_image()
        if base64_img_lst is None:
            return None
        index = 0 

        try: 
            for i in base64_img_lst:
                if is_base64(i):
                    index += 1 
                    metadata = PngImagePlugin.PngInfo() 
                    img = Image.open(io.BytesIO(base64.b64decode(i)))
                    for key, value in img.info.items():
                        if isinstance(key, str) and isinstance(value, str):
                            metadata.add_text(key, value)   
                    
                    output_filename = f"image{index}.png"
                    output_path = os.path.join(self.dir_out, output_filename)
                    img.save(output_path, "PNG", pnginfo= metadata)
                    logging.info(f"Downloading {output_filename} successfully.!")
                else: 
                    logging.error("Not base64")
                    return None
                
        except Exception as e: 
            logging.error(f"Error in downloading image: {e}")
            traceback.format_exc()
            return None
        
    def upscale_image(self):
        logging.info("Start upscaling image") 
        try: 
            images_name = [f for f in os.listdir(self.dir_in) if os.path.isfile(os.path.join(self.dir_in, f))]
            logging.info(f"Upscaling {len(images_name)} images....") 

            image_list = [] 
            for i in images_name:
                image_list.append({"data": pil_to_base64(Image.open(self.dir_in + i)), "name": i})
            
            payload = self.parse_payload_params()
            if payload is None:
                return None
            payload["imageList"] = image_list 
            payloadJson = json.dumps(payload) 
            response = requests.post(url= self.url, data= payloadJson)

            if response.status_code >= 200 and response.status_code < 300:
                response_json = response.json()
                if "images" not in response_json:
                    logging.error("Error: Images not found")
                    return None
                logging.info("Upscaling {} successfully.!".format(image_list[i].get("name")))
                return response_json.get("images")
            else:
                logging.error(f"Error: {response.status_code}, {response.text}")
                return None    
            
        except Exception as e:
            logging.error(f"Error in upscaling image: {e}")
            traceback.format_exc()
            return None 

    def parse_payload_params(self):
        try:
            params = json.load(open(self.payload_params)) 
            if params is None: 
                return None 
            return params
        except Exception as e:
            logging.error(f"Error parsing payload params: {e}")
            return None
        



    
