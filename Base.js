import React from 'react';
//Written by Mensah Ofoli Lawrence
//Component that returns the contact detail
//of each driver.

function Base(props){
    return(
        <div className="Base">
          <label>Contact Details</label>
          <p>Phone {props.phone}</p>
          <p>email {props.email}</p>
          <button onClick={props.bclick}>OK</button>
        </div>
    )
}


export default Base;