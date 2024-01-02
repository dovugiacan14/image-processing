import os 
import logging
import requests
from requests.exceptions import HTTPError
from PIL import Image 
from pathlib import Path
from helpers import pil_to_base64, convert_file_name_to_txt

class CaptionImage:
    def __init__(self, url, model, dir_in, dir_out, prefix):
        self.url = url 
        self.model = model
        self.dir_in = dir_in 
        if not os.path.exists(dir_out):
            os.makedirs(dir_out)
        self.dir_out = dir_out 
        self.prefix = prefix
    def interrogate(self):
        """Captions images using the Interrogate API.

        Args:
            url: The URL of the Interrogate API.
            model: The model to use for captioning.
            dir_in: The directory containing the input images.
            dir_out: The directory to save the output captions.
            prefix: The prefix to add to each caption.
        """
        try: 
            logging.info("Start captioning image")
            image_name = [f for f in os.listdir(self.dir_in) if os.path.isfile(os.path.join(self.dir_in, f))]
            logging.info(f"Captioning {len(image_name)} images.....")

            image_list = []
            for i in image_name:   
                image_list.append({"data": pil_to_base64(Image.open(self.dir_in + i)), "name": i})

            for i in range(len(image_list)):
                # parameter of Interrogate API
                payload = {
                    "image": image_list[i].get("data"),
                    "model": self.model
                }

                response = requests.post(url= self.url, json= payload) 
                if response.status_code >= 200 and response.status_code < 300:
                    response_json = response.json()
                    logging.info("Interrogate {} xuccesfuly.!".format(image_list[i].get("name")))
                else:
                    logging.error(f"Error: {response.status_code}, {response.text}")
                    return None

                if "caption" not in response_json:
                    logging.error("Error: Caption not found")
                    return None
                original_desc = response_json.get("caption")

                # save captioning 
                output_filename = convert_file_name_to_txt(image_list[i].get("name"))
                file_path = os.path.join(self.dir_out, output_filename)

                with open(file_path, "w") as f:
                    f.write(self.prefix)
                    f.write(original_desc)
                    f.write("\n")
            logging.info("Captioning successfully.!")

        except HTTPError as e:
            logging.error(f"Error: {e}")
            return None
        
        except Exception as e:
            logging.error(f"Error in captioning image: {e}")
            return None
    