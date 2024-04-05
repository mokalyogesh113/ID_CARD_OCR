import React from 'react';
import Nav from '../components/Nav';
import Upload from '../components/Upload';
import DisplayData from '../components/DisplayData'


function HomePage() {
  return (
    <>
      <Nav></Nav>
      <Upload></Upload>
      <DisplayData></DisplayData>
    </>
  )
}

export default HomePage