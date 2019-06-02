import React, { Component } from 'react';


function  Person(props) {
    let style = {
        '@media (min-width: 500px)':{
            width:'450px'
        }
    }
    return (<div className="myStyles" style={style}>
        <p onClick={props.click}>My name is {props.name}</p>
        <p>I am {props.age}</p>
    </div>
    );
    
};

export default Radium(Person);