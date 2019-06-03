import React from 'react';


function Base(props){
    return(
        <div className="Base">
          <h1>Im the Base</h1>
          <button onClick={props.bclick}>OK</button>
        </div>
    )
}


export default Base;