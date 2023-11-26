import warnings
from ml_pipeline.wrapper.u2net_pretrained import U2NETPretrained
from ml_pipeline.wrapper.u2net_custom import U2NETCustom
from ml_pipeline.interface_creation.interface_main import InterfaceMain
from collections import defaultdict


class SegInterface(InterfaceMain):

    def __init__(self,data):

        data = defaultdict(lambda:None, data)
        # Define all possible attributes and initialize them
        self.model_type=data.get("segmentationModel")
        self.seg_mask_size = data.get("seg_mask_size")
        self.device = data.get("device")

        # print('updating model',data.get('update_model'))

        if self.model_type == "pretrained":
            self.u2net = U2NETPretrained(
                device=self.device,
                input_image_size=self.seg_mask_size
            )

        elif self.model_type == "custom":

            self.u2net = U2NETCustom(
                device=self.device,
                input_image_size=self.seg_mask_size)
            
        else:
            warnings.warn(
                f"Unknown object type: {self.model_type}. Using default object type: object"
            )
            self.u2net = U2NETPretrained(
                _device=self.device,
                input_image_size=self.seg_mask_size
            )


        super(SegInterface, self).__init__(
            seg_model=self.u2net,
            device=self.device,
        )
    
