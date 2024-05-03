import React from 'react';
import Nav from '../components/Nav';
import Upload from '../components/Upload';
import DisplayData from '../components/DisplayData'
import { useState } from 'react';

function HomePage({url}) {
  const [flag, setFlag] = useState(1);

  const updateDisplay = (n) => {
    setFlag(n);
    console.log(n);
  }

  // {flag == 1 && <h1>This is Aadhar</h1>}
  //     {flag == 2 && <h1>This is Pan</h1>}

  return (
    <>
    <Nav flag={flag}></Nav>
    

    <div className="form-group d-flex justify-content-center">
    <div className="form-check form-check-inline">
        <input className="form-check-input" type="radio" name="id_type" id="aadhar" value="AADHAR" defaultChecked  onChange={() => setFlag(1)}/>
        <label className="form-check-label" htmlFor="aadhar">AADHAR</label>
      </div>
      <div className="form-check form-check-inline">
        <input className="form-check-input" type="radio" name="id_type" id="pan" value="PAN" onChange={() => setFlag(2)}/>
        <label className="form-check-label" htmlFor="pan">PAN</label>
      </div>
    </div>

    <Upload flag={flag} url={url}></Upload>
    <DisplayData flag={flag} url={url}></DisplayData>
    </>
  )
}

export default HomePage