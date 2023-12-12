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

| Application| Languages       |
|------------|-----------------|
| **Frontend**   | HTML            |
|            | CSS             |
|            | React           |
|            | (On Next Framework) |
|            |                 |
| **Backend**    | Python          |
|            | Pytorch         |
|            | Fast api        |
|            | Opencv          |
|            |                 |
| **Testing**    | Pytest          |
|            |                 |
| **CI/CD**      | Docker          |
|            | Kubernetes (minikube for local testing)|
|            | Github Actions  |
|            |                 |
| **Deployment** |  Google Kubernets Engine (GKE)|
|            |   (on Google cloud Platform)    |


> Here is the Demo of my Background removal app from my youtube channel, click to see 👇

[![Custom_BGR_APP](https://img.youtube.com/vi/uAksgBFnGWY/0.jpg)](https://www.youtube.com/watch?v=uAksgBFnGWY) 
