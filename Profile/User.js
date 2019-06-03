import React from 'react';
// written by Lawrence Ofoli Mensah

function User(props){
    return(
        <div className="User">
             <h1>{props.title}</h1>
             <p>First Name {props.fname}</p>
             <p>Last Name {props.lname}</p>
             <p>Other Name {props.oname}</p>
             <p>Phone {props.phone}</p>
             <p>Email {props.email}</p>
             <button onClick={props.Uclick}>EDIT {props.title} PROFILE</button>
             
        </div>
    )
}
export default User;