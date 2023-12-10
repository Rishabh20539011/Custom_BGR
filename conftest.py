from pathlib import Path
import pytest
import numpy as np
import cv2
from custom_bgr.project.ml_pipeline.wrapper.u2net_pretrained import U2NETPretrained
from custom_bgr.project.ml_pipeline.wrapper.u2net_custom import U2NETCustom
from typing import Callable, Tuple, List, Union, Optional, Any
from custom_bgr.project.ml_pipeline.models.file_location import download_all

download_all()

@pytest.fixture()
def image_path() -> Path:
    return Path(__file__).parent.joinpath("tests").joinpath("data", "1.png")


@pytest.fixture()
def loaded_image(image_path: Path) -> np.ndarray:

    image_path_str = str(image_path) if isinstance(image_path, Path) else image_path

    image = cv2.imread(image_path_str)

    num_channels = image.shape[2] if len(image.shape) == 3 else 1

    # If the image has only one channel, convert it to 3 channels
    if num_channels == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if image is None:
        raise FileNotFoundError(f"No image found at {image_path_str}")
    
    return image

@pytest.fixture()
def pretrained_interface()->Callable[[bool], U2NETPretrained]:
    return lambda: U2NETPretrained(device="cpu",input_image_size=512)

@pytest.fixture()
def custom_interface()->Callable[[bool], U2NETCustom]:
    return lambda: U2NETCustom(device="cpu",input_image_size=512)
