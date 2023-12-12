# <p align="center"> Custom_BGR_APP 🖥️ </p> 

## 📄 Description:  
🛠️ This is a Custom designed Background removal APP with a Complete CI/CD flow and deployed on Google Kubernetes Engine (GKE).🛠️

## 📋 Features:  
- This app incorporates two deep learning models. One is a pretrained model sourced from torchvision, and the other is trained on our custom dataset. Both adhere to the **Unet architecture**, with 
 a slightly different designs. It's possible to update these models within our app.
- The models can process on both**NVIDIA Cuda and CPU** but for now the model is deployed on CPU instance so the configuration files are prepared according to that.   
- You have the flexibility to **adjust the image size** according to your preferences; simply choose the size that suits your download needs.
- **Matting Model**, which enhances hairline accuracy in our models, is currently been disabled due to increased computation time and the necessity for a larger cloud instance.
- Backend server is running on **FastAPI** which faster and easier to integrate with python.
- Frontend is created on **NextJS** framework with using **React, HTML and CSS Components**.

## 🔧Tools

| Parts      | Languages       |
|------------|-----------------|
| Frontend   | HTML            |
|            | CSS             |
|            | React           |
|            |                 |
| Backend    | Python          |
|            | Pytorch         |
|            | Fast api        |
|------------|-----------------|
| Devops     | Docker          |
|            | Github actions  |



|        PARTS            |                   Languages                 | 
|:-----------------------:|:-------------------------------------------:|
| **Frontend**            |  HTML,CSS,React Components                  |
|                         |     on Next Framework                       | 
|:-----------------------:|:-------------------------------------------:|
|         BASNet          |        **General** (people, objects)        | 
|        DeepLabV3        |         People, Animals, Cars, etc          |  




|        Networks         |                   Target                    |             Accuracy             |
|:-----------------------:|:-------------------------------------------:|:--------------------------------:|
| **Tracer-B7** (default) |     **General** (objects, animals, etc)     | **90%** (mean F1-Score, DUTS-TE) |
|                         | **Hairs** (hairs, people, animals, objects) |  80.4% (mean F1-Score, DUTS-TE)  |
|:-----------------------:|:-------------------------------------------:|:--------------------------------:|
|         BASNet          |        **General** (people, objects)        |  80.3% (mean F1-Score, DUTS-TE)  |
|        DeepLabV3        |         People, Animals, Cars, etc          |  67.4% (mean IoU, COCO val2017)  |


> Here is the Demo of my Background removal app from my youtube channel, click to see 👇

[![Custom_BGR_APP](https://img.youtube.com/vi/uAksgBFnGWY/0.jpg)](https://www.youtube.com/watch?v=uAksgBFnGWY) 
