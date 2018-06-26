# hybrid-image

It is a simple computer-vision appliction that synthesizes two images to yield a synthesis image. 
The basic idea of approaching this goal is to fedd two different images to a high-pass and a low-pass 
filter to extract high frequence information and blur the image, respectivly. Finally, a new image is created by 
doing pixel-wise summation given two filtered images.  <br />

# Usage

To run the programs, please use the following command: <br />

python3 main.py [one image path] [the other image path]
