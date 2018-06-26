import numpy as np
import cv2

# Image Synthesis
class synthesis:
    def __init__(self, img_path_1, img_path_2):
        self.im_1_path = img_path_1
        self.im_2_path = img_path_2
    # ========================================
    def high_pass_function(self):
        # read one image
        img_1 = cv2.imread(self.im_1_path)

        # split the image to three channels
        b,g,r = cv2.split(img_1)
        
        # apply Gaussian filter to yield a blur image
        blur_img_b = cv2.GaussianBlur(b, (43, 43), 0)
        blur_img_g = cv2.GaussianBlur(g, (43, 43), 0)
        blur_img_r = cv2.GaussianBlur(r, (43, 43), 0)
        
        # get sharp image
        combined_img = cv2.merge((blur_img_b, blur_img_g, blur_img_r))
        sharp_img = img_1 - combined_img
        
        return sharp_img
        
    def low_pass_function(self):
        # read the other image
        img_2 = cv2.imread(self.im_2_path)

        # apply Gaussian filter to yield a blur image
        blur_img = cv2.GaussianBlur(img_2, (45, 45), 0)

        return blur_img

    def synthesize(self, in_img1, in_im2):
        result = in_img1 + in_im2
        
        # show the image
        cv2.namedWindow('Hybrid_Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Hybrid_Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
