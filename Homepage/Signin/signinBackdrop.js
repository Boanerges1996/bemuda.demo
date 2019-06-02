import React, { Component } from 'react';

function SigninBackdrop(props) {

    const style = {
        backgroundColor:'rgba(0,0,0,0.7)',
        position:'fixed',
        top:'0',
        left:'0',
        width:'100%',
        height:'100%',
        zIndex:'2'
    }
    return(
        <div style={style} onDoubleClick={props.click}>

        </div>
    )
}

export default SigninBackdrop;