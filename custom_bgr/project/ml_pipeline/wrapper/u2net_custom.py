import numpy as np
import torch
import os
import cv2
import time
import random
from ml_pipeline.architecture.u2net_custom_arch import U2NETArch
from ml_pipeline.models.file_location import u2net_full_custom


class U2NETCustom(U2NETArch):
    
    def __init__(
    self,
    device="cpu",
    input_image_size:int = 512 ):


        super(U2NETCustom, self).__init__(arch= "UnetPlusPlus",encoder_name="timm-efficientnet-b5",in_channels=3,out_classes=1,decoder_attention_type='scse')


        self._device=device
        self.model_path=u2net_full_custom(download=False)
        self.input_image_size=input_image_size
        self.to(self._device)
        # Loading the saved model weights
        self.load_state_dict(torch.load(self.model_path,map_location=self.device))
        self.eval()


    # Function to preprocess the image(Normalsing happens in the model)

    def preprocess_img(self,image):
        # Resizing
        print('error here----1111111111-----------------',self.input_image_size)
        image = cv2.resize(image, (int(self.input_image_size), int(self.input_image_size)), cv2.INTER_AREA)
        print('error here----222222222222-----------------')
        # Transposing
        print('image shape----',image.shape)
        image = image.transpose(2,0,1)
        
        return image

    @staticmethod
    def postprocess_mask(mask, image):
        mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
        return mask
    

    def __call__(self,actual_image):
        
        print('image shape----initial ',actual_image.shape)

        image = self.preprocess_img(actual_image)
        # Adding one more dimesion in front
        print('error here----3333333333333-----------------')

        image = torch.unsqueeze(torch.tensor(image), 0).to(self._device)

        print('error here----444444444444444-----------------')

        result=super(U2NETCustom, self).forward(image)
        print('predict custom---',result.shape)

        sigmoid_res = np.array(result.sigmoid().detach().cpu())
        sigmoid_res[sigmoid_res>0.5] = 255
        sigmoid_res[sigmoid_res!=255] = 0
        final_mask = sigmoid_res.astype("uint8")[0][0]
        final_mask = self.postprocess_mask(mask=final_mask, image=actual_image)

        return final_mask


