import logging
import io 
import os
import base64
import traceback
from PIL import Image

def is_base64(str):
    try:
        base64.b64decode(str)
        return True
    except Exception as e:
        logging.debug(f"Check not base64: {e}")
        return False


def pil_to_base64(img):
    try: 
        im = Image.open(img)
        img_bytes = io.BytesIO()
        im.save(img_bytes, format='PNG')
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        return img_base64
    except Exception as e:
        logging.error(f"Error converting PIL image to base64: {e}")
        return None


def count_image_in_folder(folder_path):    
    try: 
        logging.info("Start counting image")
        file_tail = [".jpg", ".png", ".jpeg"]
        result = 0 
        for filename in os.listdir(folder_path):
            if filename.endswith(str(file_tail[0])):
                result += 1
        logging.info("Counting image successfully.!")
        return result
    
    except Exception as e:
        logging.error(f"Error in counting image: {e}")
        return None


def convert_file_name_to_txt(file_name):
    file_tail = [".jpg", ".png", ".jpeg"]
    try: 
        for i in file_tail: 
            if file_name.endswith(i):
                file_name_convert = file_name.replace(i, ".txt")
        return file_name_convert 
    except Exception as e:
        logging.error(f"Error converting file name: {e}")
        return None 


def rename_image_files(folder_path):
    try: 
        count = 1 
        for filename in os.listdir(folder_path):
            if filename.endswith(('.jpg', 'jpeg', '.png', '.gif')):
                new_file = f'image{count}.png'
                src = os.path.join(folder_path, filename)
                des = os.path.join(folder_path, new_file)
                os.rename(src, des)
                count += 1
        print("Succesfully.!")
                
    except Exception as e:
        print("Error Occur: ",str(e))
        traceback.print_exc()
    


