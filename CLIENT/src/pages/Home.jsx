import React from 'react';
import Nav from '../components/Nav';
import Upload from '../components/Upload';
import DisplayData from '../components/DisplayData'
import { useState } from 'react';

function HomePage() {
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
    <div className="container d-flex justify-content-center">
      <input type='button' value='Aadhar' onClick={() => setFlag(1)} className="btn btn-link m-2"/>
      <input type='button' value='Pan' onClick={() => setFlag(2)} className="btn btn-link m-2"/>
    </div>
    <Upload flag={flag}></Upload>
    <DisplayData flag={flag}></DisplayData>
    </>
  )
}

export default HomePage