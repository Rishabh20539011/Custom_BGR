# <p align="center"> Custom_BGR 🖥️ </p> 

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
|**Process manager**| Supervisord                |
|            |                 |
| **Testing**    | Pytest          |
|            |                 |
| **CI/CD**      | Docker          |
|            | Kubernetes (minikube for local testing)|
|            | Github Actions  |
|            |                 |
| **Deployment** |  Google Kubernets Engine (GKE)|
|            |   (on Google cloud Platform)    |

>Here is the YouTube link featuring the demonstration of the Background Removal app. Click below to watch 👇. (Please note that the live instance of the project on Google cloud platform is currently inactive due to its billing cycle, so direct access through a link is unavailable.)

[![Custom_BGR_APP](https://img.youtube.com/vi/uAksgBFnGWY/0.jpg)](https://www.youtube.com/watch?v=uAksgBFnGWY) 

## Using Custom_BGR locally

1. Clone the repository and checkout to the final_branch (due to a slight variance in the configuration of Kubernetes pods between the local environment and the cloud)

```shell script
git clone https://github.com/Rishabh20539011/Custom_BGR.git
git checkout final_branch
```
2. Install [**Docker**](https://docs.docker.com/engine/install/) and [**Kubernetes**](https://minikube.sigs.k8s.io/docs/start/), if not available in your system
   Note-- I have used minikube to configure kubernetes in my system , you can install either directly from docker or through other setup.

3. Start minkube to setup kubectl, so that we can acess inside pods

```
minikube start
```

4. Create deployments through our configuration files which will fetch the required docker images from Dockerhub (rishabh20539011/custom_bgr) , and these images encompass all the dependencies and setup requirements.

```
kubectl apply -f /home/rishabh/Desktop/custom_bgr_main/Custom_BGR_APP/backend_deployment.yaml

kubectl apply -f /home/rishabh/Desktop/custom_bgr_main/Custom_BGR_APP/frontend_deployment.yaml

```





 
