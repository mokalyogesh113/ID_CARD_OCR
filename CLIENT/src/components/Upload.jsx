import React from "react";
import './css/Upload.css'
import folderIcon from "../images/img/folder-icon.png";
import { useState, useEffect } from "react";
import { ring } from 'ldrs'


ring.register()

// Default values shown


function Upload({flag}) {

  // STATES
  const [selectedImage, setSelectedImage] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [aadharFlag, setAadharFlag] = useState(false);
  const [data, setData] = useState({
    pan_no: "",
    father_name: "",
    name: "",
    dob: "06-04-2024",
  });


  // USE EFFECT 
  useEffect(() => {
    handleImageUpload();
  }, [selectedImage]);

  // HANDLERS

  const handleImageUpload = () =>{
    if (selectedImage) {
      const blob = dataURItoBlob(selectedImage);
      const formData = new FormData();
      formData.append("imageFile", blob, "image.jpg");

      setIsLoading(true);

      let url = ""
      if (flag == 1) {
        url = "http://localhost:5005/aadhar/extract_data";
      } else {
        url = "http://localhost:5005/pan/extract_data";
      }

      fetch(url, {
        method: "POST",
        body: formData,
      })
        .then((res) => res.json())
        .then((data) => {
          setData(data);
          console.log(data);
          setIsLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          alert("Error Fetching Data ")

          setIsLoading(false);
        });
    }
  }



  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setSelectedImage(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleChange = (event) => {
    setData({
      ...data,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = () => {
    if (data.pan_no && data.father_name && data.name && data.dob) {
      fetch("/pan/store_data", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      }).then((response) => {
        console.log(response);
        alert("Data Stored To databse");
      }).catch(error => console.error('Error:', error));
    } else {
      console.log("Not Allowed")
    }
  }

  return (
    <div className="hero container">
      <div className="m-5">
        {isLoading &&
          <div className="loading">
            <l-ring
              size="40"
              stroke="5"
              bg-opacity="0"
              speed="2"
              color="black"
              ></l-ring>
          </div>
        }

        <div className="row">
          <div className="col-12 col-lg-4">
            {!selectedImage && (
              <div className="d-flex flex-column justify-content-center align-items-center">
                <img src={folderIcon} alt="Logo" />
                <label htmlFor="file-upload" className="mt-2 btn btn-secondary">
                  Upload File{" "}
                </label>
                <input
                  id="file-upload"
                  type="file"
                  accept=".png, .jpg, .jpeg"
                  onChange={handleImageChange}
                  />
              </div>
            )}

            {selectedImage && (
              <div>
                <label htmlFor="file-upload" className="m-2 btn btn-secondary ">
                  Upload File{" "}
                </label>
                <input type="button" value="Fetch Data again" onClick={handleImageUpload} className="m-2 btn btn-secondary "/>
                <input
                  type="file"
                  id="file-upload"
                  accept=".png, .jpg, .jpeg"
                  onChange={handleImageChange}
                  />
                <img id="pan-img" src={selectedImage} alt="No File Found" />
              </div>
            )}


            
          </div>

          <div className="col">
            <form action="">

              {/*PAN Number*/}
              {flag == 2 &&
                (<div className="row m-2">
                  <div className="col-6 d-flex justify-content-end">
                    <label htmlFor="pan-id">Permanant Account Number:- </label>
                  </div>
                  <div className="col-6 d-flex justify-content-start">
                    <input
                      type="text"
                      name="pan_no"
                      placeholder="Permanant Account Number"
                      value={data.pan_no}
                      onChange={handleChange}
                      ></input>
                  </div>
                </div>)}

              {/*AADHAR Number*/}
              {flag == 1 &&
                (<div className="row m-2">
                  <div className="col-6 d-flex justify-content-end">
                    <label htmlFor="pan-id">UIDAI Number:- </label>
                  </div>
                  <div className="col-6 d-flex justify-content-start">
                    <input
                      type="text"
                      name="aadhar_no"
                      placeholder="UIDAI"
                      value={data.aadhar_no}
                      onChange={handleChange}
                      ></input>
                  </div>
                </div>)}

              {/*NAME*/}
              <div className="row m-2">
                <div className="col-6 d-flex justify-content-end">
                  <label htmlFor="pan-name">Name :- </label>
                </div>
                <div className="col-6 d-flex justify-content-start">
                  <input
                    type="text"
                    name="name"
                    placeholder="Full Name"
                    value={data.name}
                    onChange={handleChange}
                    ></input>
                </div>
              </div>

              {/*FATHER'S NAME*/}
              {flag == 2 &&
                (<div className="row m-2">
                  <div className="col-6 d-flex justify-content-end">
                    <label htmlFor="pan-f-name">Father's Name :- </label>
                  </div>
                  <div className="col-6 d-flex justify-content-start">
                    <input
                      type="text"
                      name="father_name"
                      placeholder="Father's Name"
                      value={data.father_name}
                      onChange={handleChange}
                      ></input>
                  </div>
                </div>)}

              {/*GENDER*/}
              {flag == 1 &&
                (<div className="row m-2">
                  <div className="col-6 d-flex justify-content-end">
                    <label htmlFor="pan-f-name">Gender :- </label>
                  </div>
                  <div className="col-6 d-flex justify-content-start">
                    <input
                      type="text"
                      name="gender"
                      placeholder="Male / Female "
                      value={data.gender}
                      onChange={handleChange}
                      ></input>
                  </div>
                </div>)}

              {/*DATE OF BIRTH*/}
              <div className="row m-2">
                <div className="col-6 d-flex justify-content-end">
                  <label htmlFor="pan-dob">Date of Birth :- </label>
                </div>
                <div className="col-6 d-flex justify-content-start">
                  <input
                    type="date"
                    name="dob"
                    value={convertDate(data.dob)}
                    onChange={handleChange}
                    ></input>
                </div>
              </div>

              <div className="row m-2">
                <div className="col-6 d-flex justify-content-end">
                  <input type="button" value="Store Data" onClick={handleSubmit} />
                </div>
                <div className="col-6 d-flex justify-content-start">
                  {/* TEMP */}
                </div>
              </div>


            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Upload;

function dataURItoBlob(dataURI) {
  const byteString = atob(dataURI.split(",")[1]);
  const mimeString = dataURI.split(",")[0].split(":")[1].split(";")[0];
  const ab = new ArrayBuffer(byteString.length);
  const ia = new Uint8Array(ab);
  for (let i = 0; i < byteString.length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  return new Blob([ab], { type: mimeString });
}

function convertDate(date) {
  if (!date) return date;

  // 01/01/2003
  var result =
    date.substr(6, 4) + "-" + date.substr(3, 2) + "-" + date.substr(0, 2);
  return result;
}
