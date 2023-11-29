import { useState } from "react";
import styled from "@emotion/styled";
import { Input } from "@material-ui/core";
import { io } from "socket.io-client";
import axios from "axios";
import styles from "../styles/Root.module.css";

const socket = io.connect('http://localhost:8000');


socket.on("connect", function() {
  console.log("Connected to server");
});


socket.on("image", function(data) {
  // Code to display the image using the base64 string in data.image
  document.getElementById("imageElementId").src = "data:image/png;base64," + data.image;
});




socket.on('receive_image', (data) => {
  // const imageElement = document.getElementById('imageDisplay');
  // imageElement.src = `data:image/png;base64,${data.image}`;
  setResponseImage(data.image)
});

const Container = styled.div`
  align-items: center; /* Center items vertically */
  // flex-wrap: wrap; /* Wrap to the next line if there are more than 3 dropdowns */
`;

const DropdownContainer = styled.div`
  display: flex; /* Use flexbox to create a horizontal layout */
  justify-content: space-around; /* Space around items in the row */
  text-align: center;
  flex-wrap:wrap; 
  margin: 10px;
  padding: 10px;
  background-color: #f1f1f1;
  border-radius: 5px;
`;

const Header = styled.h1`
  background-color: #3498db;
  color: white;
  padding: 20px;
  margin: 0;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 10px;
`;

const CustomSelect = styled.select`
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  width: 200px;
`;

const SelectedOption = styled.p`
  margin-top: 10px;
  font-weight: bold;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* Two columns */
  gap: 300px; /* Gap between boxes */
  justify-content: center; /* Center the grid horizontally */
  margin: 20px 200px 0;
`;

const ImageBox = styled.div`
  width: 200px;
  height: 200px;
  background-color: #3498db;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 24px;
  margin: 10px; /* Equal margins around the square box */
  padding: 10px; /* Equal padding inside the square box */
`;

const Image = styled.img`
  max-width: 100%;
  max-height: 100%;
`;

const Button = styled.button`
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: #2577b5;
  }
`;

function Dropdown() {
  // const [segmentationModel, setSegmentationModel] = useState(null);
  const [reqBody,setReqBody]=useState({
    segmentationModel:"pretrained",
    mattingModel:"fba_mat",
    segmentationThreshold:0.5,
    // trimapThreshold:3,
    seg_mask_size: 320,
    update_model:true,
    device:"cuda"
  })
  // const [mattingModel, setMattingModel] = useState(null);
  // const [selectedFile, setSelectedFile] = useState(null);
  const [selectedImage, setSelectedImage] = useState(null);
  const [responseImage, setResponseImage] = useState(null);
  const [loader,setLoader]=useState(false);


  // const handleFileChange = (event) => {
  //   console.log(event.target.files, "---");
  //   setSelectedFile(event.target.files[0]);
  // };
  // const handleFileChange = (event) => {
  //   const file = event.target.files[0];
  //   if (file) {
  //     // Display the selected image
  //     const reader = new FileReader();
  //     reader.onload = (e) => {
  //       setSelectedImage(e.target.result);
  //     };
  //     reader.readAsDataURL(file);
  //   } else {
  //     setSelectedImage(null);
  //   }
  // };

  const getResult=async ()=>{
    setLoader(true);
    try{
      const res = await axios.post(process.env.NEXT_PUBLIC_URL, {
        data: reqBody,
        image: selectedImage,
      });
      setResponseImage(res.data.image);
    }catch(e){
      console.log("Process error:",e)
    }
    setLoader(false)
  }

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    try {
      if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(event.target.files[0])
        reader.onload = (e) => {
          // const imgElement = document.createElement("img");
          // imgElement.src = e.target.result;
          // imgElement.onload = () => {
          //   const canvas = document.createElement("canvas");
          //   const ctx = canvas.getContext("2d");
          //   const maxDimension = 200;

          //   if (imgElement.width > imgElement.height) {
          //     canvas.width = maxDimension;
          //     canvas.height =
          //       (maxDimension * imgElement.height) / imgElement.width;
          //   } else {
          //     canvas.width =
          //       (maxDimension * imgElement.width) / imgElement.height;
          //     canvas.height = maxDimension;
          //   }

          //   // Use "image-rendering" property for better quality
          //   ctx.imageSmoothingQuality = "high";
          //   ctx.drawImage(imgElement, 0, 0, canvas.width, canvas.height);
          //   reader.readAsDataURL(event.target.files[0])
          //   reader.onload(()=>{
          //     console.log(reader.result)
          //   })
          //   setSelectedImage();
          // };
          setSelectedImage(reader.result);
          // console.log(reader.result)
        };
        reader.readAsDataURL(file);
      } else {
        setSelectedImage(null);
      }

    // const res = await axios.post("http://localhost:8881/process", {
    //   data: reqBody,
    //   image: selectedImage,
    // });
  } catch (error) {
    if (error.response) {
      console.log('Data:', error.response.data);
      console.log('Status:', error.response.status);
      console.log('Headers:', error.response.headers);
    } else if (error.request) {
      console.log('Request:', error.request);
    } else {
      console.log('Error:', error.message);
    }
  }
};


  return (
    <Container>
      <Header style={{textAlign:"center",fontSize:"40px"}}>CUSTOM BGR TOOL</Header>
      <DropdownContainer className={styles.optionsParent}>
        <div>
          <Label htmlFor="dropdown">Select Segmentation Model:</Label>
          <CustomSelect
            id="dropdown"
            value={reqBody.segmentationModel}
            onChange={(e) => {setReqBody({...reqBody,segmentationModel:e.target.value})}}
          >
            <option value="custom">Custom</option>
            <option value="pretrained">Pretrained</option>
          </CustomSelect>
        </div>
        <div>
          <Label htmlFor="dropdown">Select Matting Model:</Label>
          <CustomSelect
            id="dropdown"
            value={reqBody.mattingModel}
            disabled={true}
            onChange={(e) => {setReqBody({...reqBody,mattingModel:e.target.value})}}
          >
            <option value="fba_mat">FBA_MAT</option>
            <option value="vit_mat">VIT_MAT</option>
          </CustomSelect>
        </div>
        <div>
          <Label htmlFor="dropdown">Select Device:</Label>
          <CustomSelect
            id="dropdown"
            value={reqBody.device}
            onChange={(e) => {setReqBody({...reqBody,device:e.target.value})}}
          >
            <option value="cuda">Cuda</option>
            <option value="cpu">CPU</option>
          </CustomSelect>
        </div>
        {/* <div>
          <Label htmlFor="dropdown">Select Trimap Threshold:</Label>
          <Input type="number" value={reqBody.trimapThreshold} onChange={(e)=>{
            setReqBody({...reqBody,trimapThreshold:e.target.value})
          }} step={1}  min={0} max={30}/>
        </div> */}
        <div>
          <Label htmlFor="dropdown">Select Segmentation Threshold:</Label>
          <Input type="number" value={reqBody.segmentationThreshold} onChange={(e)=>{
            setReqBody({...reqBody,segmentationThreshold:e.target.value})
          }} min={0} max={1} />
        </div>
        <div>
          <Label htmlFor="dropdown">Select Mask Size:</Label>
          <Input type="number" value={reqBody.seg_mask_size} onChange={(e)=>{
            setReqBody({...reqBody,seg_mask_size:e.target.value})
          }} min={256} max={1024} />
        </div>
        <div>
          <Label htmlFor="dropdown">Update Model:</Label>
          <Input type="checkbox" style={{width:"20px"}} checked={reqBody.update_model} onClick={(e)=>{
            setReqBody({...reqBody,update_model:!reqBody.update_model})
          }} />
        </div>
      </DropdownContainer>

      <GridContainer style={{justifyContent:"stretch"}}>
        {/* <ImageBox> */}
        <div className={styles.container}>
          {/* <Image
            src="image1.jpg"
            alt="Image 1"
            style={{ height: "200px", width: "200px"}}
          /> */}
          <div className={styles.placeholder}>{selectedImage ?<img src={selectedImage} alt="Selected" />:<p>Please choose image to start</p>}</div>
          
          {/* </ImageBox> */}
          {/* <Button>Upload image</Button> */}
          <Input
            // className={classes.input}
            type="file"
            onChange={handleFileChange}
            // placeholder="Select Image"
            // accept="image/*"
            inputProps={{ accept: "image/*" }}
            // style={{ width: "100px" }}
          />
        </div>
        <div className={styles.container}>
          <div className={styles.placeholder}>{loader && <Loader height={'4em'}/>}{responseImage ?<img src={`data:image/png;base64,${responseImage}`} alt="Selected" />:!loader?<p>Waiting for response</p>:<></>}</div>
          <Button onClick={()=>{
            getResult();
          }}>Get Result</Button>
        </div>
        {/* <ImageBox>
          <Image src="image2.jpg" alt="Image 2" />
        </ImageBox> */}
        {/* Add more ImageBox components as needed */}
      </GridContainer>
    </Container>
  );
}

export const Loader=({height})=>{
  return <div className={styles.loaderContainer}><div style={height && {height,width:height}} className={styles.loader}/></div>
}

export default Dropdown;
