import React from 'react';
import { useState, useEffect } from 'react';
import './css/DisplayData.css'


function DisplayData({url}) {

    const [data, setData] = useState(null);
    const [titles, setTitles] = useState(null);
    const [sectionTitle, setSectionTitle] = useState(null);

    const handleFetch = (flag) => {
        let fetchURL = "";
        if (flag == 1)      fetchURL = url + "/aadhar/get_all_data";
        else                fetchURL = url + "/pan/get_all_data";

        fetch(fetchURL, {
            method: "GET",
        }).then((res) => res.json()).then((data) => {
            setData(data);
            if (flag == 1) {
                setTitles(['id', 'aadhar_no', 'name', 'gender', 'dob']);
                setSectionTitle('Aadhar Data');
            } else if (flag == 2) {
                setTitles(['id', 'pan_no', 'name', 'father_name', 'dob']);
                setSectionTitle('Pan Data');
            }
        }).catch((error) => {
            console.error("Error fetching data:", error);
            alert("Error Fetching Data ")
        });
    }

    return (
        <div className="container d-flex flex-column align-items-center">
            <input type="button" value="Fetch Aadhar Data" onClick={() => handleFetch(1)} />
            <input type="button" value="Fetch Pan Data" onClick={() => handleFetch(2)} />

            <div className="mt-4 ">
                <h1>{sectionTitle}</h1>
            </div>

            {data &&
                <div className="tableDiv">
                    <table>
                        <thead>
                            <tr>
                                {titles.map((title) => (
                                    <td>{title.toUpperCase()}</td>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {data.map((item) => (
                                <tr>
                                    {titles.map((title) => (
                                        <td>{item[title]}</td>
                                    ))}
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





// {data.map((item) => (
//     <tr key={item.id}>
//         {titles.map((title) => (
//             <td>{item.title}</td>
//         ))}
//     </tr>
// ))}