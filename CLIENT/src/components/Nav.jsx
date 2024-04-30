import React from 'react'

function Nav({flag}) {
  return (
    <div>
      <h2 className='container d-flex justify-content-center'>{flag==2 && 'PAN'} {flag==1 && 'Aadhar'} - OCR Web App</h2>
    </div>
  )
}

export default Nav;