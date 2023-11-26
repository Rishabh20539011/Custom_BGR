import os
import json
import pathlib
from dotenv import load_dotenv

load_dotenv()

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# # Initialize GoogleDrive with your authentication
# gauth = GoogleAuth()
# gauth.LoadClientConfigFile("/home/frinksserver/rishabh/bgr/project/client_secrets.json")

# gauth.LocalWebserverAuth()  # This creates a local webserver and automatically handles authentication.
# drive = GoogleDrive(gauth)

# # Define the cache directory
# model_dir = "/home/frinksserver/.cache/custom_bgr_models"


model_dir=str(os.getenv('model_dir'))

def u2net_full_pretrained() -> pathlib.Path:
    """Returns u2net pretrained model location

    Returns:
        pathlib.Path to model location
    """
    selected_model = "u2net_pretrained.pth"

    # Check if the cache directory exists; if not, create it
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model_path = os.path.join(model_dir, selected_model)

    # # Check if the model is already in the cache
    # if not os.path.exists(model_path):
    #     # Model not found in the cache, download it from Google Drive
    #     model_id = '1av3d50YCerMPlW6G2vVnhTgCBKdPBnVC'  # Replace with the actual ID for the u2net model

    #     # Download the model
    #     file = drive.CreateFile({'id': model_id})
    #     file.GetContentFile(model_path)
    #     print('model loaded')
    # print('model already there')
    return pathlib.Path(model_path)



def u2net_full_custom() -> pathlib.Path:

    """Returns another custom model location

    Returns:
        pathlib.Path to model location
    """
    selected_model = "u2net_custom.pt"

    # Check if the cache directory exists; if not, create it
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model_path = os.path.join(model_dir, selected_model)

    # # Check if the model is already in the cache
    # if not os.path.exists(model_path):
    #     # Model not found in the cache, download it from Google Drive
    #     model_id = '1YjJ50hhxvOrSd2ZdrjHShEijHHjW8JpN'  # Replace with the actual ID for the other model

    #     # Download the model
    #     file = drive.CreateFile({'id': model_id})
    #     file.GetContentFile(model_path)
    #     print('model loaded')
    # print('model already there')
    return pathlib.Path(model_path)


# https://drive.google.com/file/d/1YjJ50hhxvOrSd2ZdrjHShEijHHjW8JpN/view?usp=sharing
# https://drive.google.com/file/d/1av3d50YCerMPlW6G2vVnhTgCBKdPBnVC/view?usp=sharing