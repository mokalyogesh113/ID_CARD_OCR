import React from 'react';
import { useState } from 'react';
import './css/DisplayData.css'


function DisplayData() {

    const [data, setData] = useState(null);


    const handleFetch = () => {
        fetch("/get_pan_data_db", {
            method: "GET",
        }).then((res) => res.json()).then((data) => {
            setData(data);
            console.log(data);
        }).catch((error) => {
            console.error("Error fetching data:", error);
            alert("Error Fetching Data ")
        });
    }


    return (
        <div className="container d-flex flex-column align-items-center">
            <input type="button" value="Fetch Data" onClick={handleFetch} />

            {data &&

                <div className="tableDiv">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Pan NO</th>
                                <th>Name</th>
                                <th>Father's Name</th>
                                <th>DOB</th>
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((item) => (
                                <tr key={item.id}>
                                    <td>{item.id}</td>
                                    <td>{item.pan_no}</td>
                                    <td>{item.name}</td>
                                    <td>{item.father_name}</td>
                                    <td>{item.dob}</td>
                                </tr>
                            ))}

                        </tbody>

                    </table>

                </div>


            }


        </div>
    )
}

export default DisplayData;


/*
<tbody>
    {data.map((item) => (
        <tr key={item.id}>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.pan_no}</td>
            <td>{item.dob}</td>
            <td>{item.father_name}</td>
        </tr>
    ))}

    */