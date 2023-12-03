from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
import cv2
import base64
import numpy as np
from io import BytesIO
from ml_pipeline.interface_creation.interface import SegInterface
from fastapi.middleware.cors import CORSMiddleware
# from socket_io_handler import sio, emit_image
# from fastapi.routing import Mount
# import socketio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


class InputData(BaseModel):
    data: dict = Field(..., example={
        "model_type": "pretrained",
        "seg_mask_size": 320,
        "device": "cuda",
        "update_model": False
    })
    image: str = Field(..., example="base64ImageString")

global_interface = None


def call_interface(input_data):
    
    interface=SegInterface(input_data)

    return interface

# Function to process the image and return the result
def process_image(image_data,interface):
    # Decode the base64 image
    image_data = image_data.split(",")[-1]

    image_bytes = base64.b64decode(image_data)

    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    print('initial shape-----',image.shape)

    # Check the number of channels in the image
    num_channels = image.shape[2] if len(image.shape) == 3 else 1

    # If the image has only one channel, convert it to 3 channels
    if num_channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    print('properties of image-----',image.shape)
    # Your processing logic here
    # For example, you can use SegInterface to process the image

    result_image=interface(image)

    print('properties of image-----',result_image.shape)

    # Encode the result image as base64
    _, buffer = cv2.imencode('.png', result_image)

    result_image_base64 = base64.b64encode(buffer).decode('utf-8')

    return result_image_base64

@app.post("/process")
async def analyze_image(input_data:InputData):
    global global_interface
    try:
        # print('input_data', input_data.data)
        print('data----coming=---------')
        global_interface = call_interface(input_data.data)
        print('interface ----- called----- =---------')
        result_image_base64 = process_image(input_data.image, global_interface)
        print('image generated----- =---------')
        # await emit_image('image',result_image_base64)

        return {"image": result_image_base64}

        # if input_data.data['update_model']:
        #     global_interface = call_interface(input_data.data)
        #     result_image_base64 = process_image(input_data.image, global_interface)
        #     return {"image": result_image_base64}

        # else:
        #     if global_interface is None:
        #         raise HTTPException(status_code=400, detail="No interface available")
        #     result_image_base64 = process_image(input_data.image, global_interface)
        #     return {"image": result_image_base64}

    except Exception as e:
        print('error-----',e)
        raise HTTPException(status_code=500, detail=str(e))

print('APP started')

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="192.168.1.45", port=8000)
