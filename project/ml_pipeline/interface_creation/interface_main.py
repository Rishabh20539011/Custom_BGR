import numpy as np
import cv2

class InterfaceMain():

    def __init__(self,seg_model,device):

        self.seg_model=seg_model
        self.device=device

    def __call__(self,image):

        mask=self.seg_model(image)

        mask = mask.astype(np.uint8)

        print('mask-----',mask)

        mask = cv2.resize(mask, (image.shape[1], image.shape[0]))

        print('error---')
        # Create an empty alpha channel
        alpha = np.ones_like(mask, dtype=image.dtype) * 255

        # Set the alpha channel based on the mask
        alpha[mask == 0] = 0

        # Add the alpha channel to the image
        image_with_alpha = cv2.merge((image, alpha))

        print('analysis done')

        cv2.imwrite('result.png',image_with_alpha)
        
        return image_with_alpha