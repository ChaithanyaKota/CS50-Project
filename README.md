# Sketched


## Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

#### Video Demo:  https://youtu.be/e2NuxjM6g9U


## Introduction
#### Description

The Sketched App is an exciting and artistic project that allows users to transform their images into captivating pencil sketches. Leveraging the power of Flask and the OpenCV-Python library, this web-based tool provides an intuitive interface for users to upload their favorite images. Upon processing, the application applies advanced image processing techniques, simulating the timeless charm of hand-drawn pencil sketches.

With a user-friendly interface and real-time preview, users can instantly witness the transformation of their images.

The App takes an image as user-input. 

The 'allowed_file' function makes sure the image is of one of the following types: .jpg .jpeg or .png. If the file is not one of these 3 types the image will not be processed.

After it is validated, the image is uploaded to the 'static/uploads' folder of the project.

The Image then goes into the 'make_sketch' function which transforms the image into sketch. 
    
The steps the image undergoes are: 
     1. Grayscale
     2. Inverting Color
     3. Gaussian Blur
     4. Dodging

The final result is an image that looks like a pencil sketch. 

Usage: 

1. (For Mac) Go to [app.py](app.py) and edit the 'path' variable to the project's virtual environemnt's site-packages directory

2. In [app.py](app.py) edit the 'UPLOAD_FOLDER' variable to your project directory

2. Start the flask server: 

    ```bash
    flask run
    ```

3. Open your web browser in your local host from the terminal

4. Upload an image of your choice and click on the "Make Sketch" button.

5. Wait for the processing to complete, and the pencil sketch version of your image will be displayed.


## Demo

VIDEO DEMO: https://youtu.be/e2NuxjM6g9U

## Installation

To run the Pencil Sketch Converter locally, follow these installation steps:

1. Clone the repository to your local machine:

    ```bash
    git clone 
    ```

2. Create a virtual environment (optional, but recommended):

    ```bash
    python3.11 -m venv venv
    ```

3. Activate virtual environment: 
    - On Windows: 
        ```bash
        venv/Scripts/activate
        ```

    - On Mac: 
        ```bash 
        source venv/bin/activate
        ```


4. Install the required dependencies
    ```bash
    pip install -r requirements.txt    
    ```


## Usage

1. (For Mac) Go to [app.py](app.py) and edit the 'path' variable to the project's virtual environemnt's site-packages directory

2. In [app.py](app.py) edit the 'UPLOAD_FOLDER' variable to your project directory

2. Start the flask server: 

    ```bash
    flask run
    ```

3. Open your web browser in your local host from the terminal

4. Upload an image of your choice and click on the "Make Sketch" button.

5. Wait for the processing to complete, and the pencil sketch version of your image will be displayed.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.



---

I hope you enjoy using the Sketched App! Feel free to reach out to us for any feedback or suggestions. Happy sketching!# CS50-Project
