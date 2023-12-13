# <p align="center"> Custom_BGR 🖥️ </p> 

## 📄 Description:  
🛠️ This is a Custom designed Background removal APP to demonstrate the entire CI/CD flow and the deployment process of Deep Learning models on the Google Cloud Platform.🛠️

## 📋 Features:  
- This app incorporates two deep learning models. One is a pre-trained model sourced from Torchvision, and the other is trained on our custom dataset. Both adhere to the **Unet architecture**, with 
 a slightly different design. It's possible to update these models within our app.
- The models can process on both **NVIDIA Cuda and CPU** but for now, the model is deployed on CPU instance so the configuration files are prepared according to that.   
- You have the flexibility to **adjust the image size** according to your preferences; simply choose the size that suits your download needs.
- **Matting Model**, which enhances hairline accuracy in our models, is currently been disabled due to increased computation time and the necessity for a larger cloud instance.
- The backend server is running on **FastAPI** which is faster and easier to integrate with Python.
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
| **Deployment** |  Google Kubernetes Engine (GKE)|
|            |   (on Google Cloud Platform)    |

>Here is the YouTube link featuring the demonstration of the Background Removal app. Click below to watch 👇. (Please note that the live instance of the project on the Google cloud platform is currently inactive due to its billing cycle, so direct access through a link is unavailable.)

[![Custom_BGR_APP](https://img.youtube.com/vi/uAksgBFnGWY/0.jpg)](https://www.youtube.com/watch?v=uAksgBFnGWY) 

## Using Custom_BGR locally

1. Clone the repository and checkout to the final_branch (due to a slight variance in the configuration of Kubernetes pods between the local environment and the cloud)

```shell script
git clone https://github.com/Rishabh20539011/Custom_BGR.git
git checkout final_branch
```
2. Install [**Docker**](https://docs.docker.com/engine/install/) and [**Kubernetes**](https://minikube.sigs.k8s.io/docs/start/), if not available in your system
   Note-- I have used Minikube to configure Kubernetes in my system, you can install it either directly from docker or through other setups.

3. Start Minkube to setup Kubectl, so that we can access inside pods

```
minikube start
```

4. Create deployments through our configuration files which will fetch the required docker images from Dockerhub (rishabh20539011/custom_bgr), and these images encompass all the dependencies and setup requirements.

```
kubectl apply -f /path/to/your/backend_deployment.yaml

kubectl apply -f /path/to/your/frontend_deployment.yaml

```

5. Create services through our configuration files which will create a separate network, excess necessary ports, and setup communication between the frontend and backend

```
kubectl apply -f /home/rishabh/Desktop/custom_bgr_main/Custom_BGR_APP/frontend_services.yaml

kubectl apply -f /home/rishabh/Desktop/custom_bgr_main/Custom_BGR_APP/backend_services.yaml

```

6. Start the application by getting a direct link through the frontend pod

```
minikube service frontend-service

```
 
 **Note**--------- If you want to run this app directly through docker without setting up Kubernetes than you can access docker-compose file:
 
 ```
 cd path/to/your/docker-compose-yaml
 docker-compose up -d --build
 ```
 Then access the application on --- http://localhost:3000

## 🗒 Note:

The target to improve this app in future versions are:- 

* Incorporating training scripts into our UI for the automated training of a custom model through CI/CD.
* Integrating Matting models to enhance the clarity of boundaries in our segmented images.
* Introducing additional variables to provide more control over our results.
* Implementing multi-factor authentication in our app.
* ADD Monitoring tool like Prometheus or Grafana to my deployment
* Developing a dynamic user interface.






 
