# Image Processing
*** 

## **OVERVIEW**

In this repository, we provide a number of image processing features, including: 

* **Image augmentation:**  This feature provide a way to increase the amount of data This is to enable you to generate more data even if you have little data. You can do this by leveraging the data you already have. 

* **Image captioning:** This feature generates a text description of an image, describing the content of the image and the scene that is depicted. For example, image captioning can be used to create descriptive content for images that are used in websites or applications, or to help people with visual impairments understand the content of images.
 
* **Image resizing:** This feature resizes images to a specified width and height. For example, image resizing can be used to create smaller versions of images for web or mobile devices, or to create larger versions of images for printing.

* **Image upscaling:** This feature improves the resolution of images, making them appear sharper and clearer. For example, image upscaling can be used to restore the original resolution of old photos, or to create high-quality images from low-resolution images.

## PRE-REQUISITS 
1. First, you need to prepare an image folder. 
2. If any of these packages are not installed on your computer, you can install them using the supplied `requirements.txt` file:
>        pip install -r requirements.txt 

## DEMO
### Image captioning 
**Condition:** you have start Stable Diffusion Web UI.

Unleash the power of image captioning with a simple command:
>       python launch.py --method 0 

To select pre-trained model for image captioning, including: 
* [CLIP](https://huggingface.co/sujitpal/clip-imageclef): A versatile model adept at diverse visual tasks.
* [Deepdanbooru](https://huggingface.co/spaces/hysts/DeepDanbooru): Specialized for anime and manga images. 

you can use argument `--model`. Example: `python launch.py --method 0 --model deepdanbooru`

In addition, you can add prefix for captioniig by add argument `--prefix`. 

### Image Augmentation
You can choose one of three types of augmentation by add argument `--type`, where 0, 1, 2 corresponse skew (default), flip, and rotate. 

Example, run: 
>       python launch.py --method 1 --type 1 

### Image Resizing 
Resize images in a flash with a single command: `python launch.py --method 2.` Take control of minimum size with --min_size for precision tailoring, we set default by 1024. 

Example: 
>       python launch.py --method 2 --min_size 512 

resizes images while ensuring a minimum size of 512 pixels. It's that easy!

### Image Upscale
Condition: you have start Stable Diffusion Web UI. 

Unleash the power of image upscale with a simple command: 
>       python launch.py --method 3 







