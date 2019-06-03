import React from 'react';

function Driver(props){
    return(
        <div className="Driver">
            <h1>{props.title}</h1>    
            <p>Gender {props.gender}</p> 
            <p>Age {props.age}</p>
            <p>Lincence {props.lincence}</p>
            <p>City {props.city}</p>
            <p>Residence {props.residence}</p>
            <button onClick={props.Dclick}>EDIT {props.title} PROFILE</button>
         
        </div>
    )
}
export default Driver