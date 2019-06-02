import React, { Component } from 'react';

/*
This Is written By Nkrumah Samson Kwaku
This show the Login Modal Backdrop which responds to 
a Double click event to close the modal

WE WILL WORK ON HOW TO MAKE THE MODAL FIXED TO PREVENT SCROLLING
WHEN THE LOGIN MODAL IS ACTIVATED
*/


function LoginBackDrop(props) {

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

export default LoginBackDrop;