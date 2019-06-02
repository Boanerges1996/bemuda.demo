import React from 'react';
import './troskis.css';
import {Form,Button} from 'react-bootstrap';





export default class Troski extends React.Component{
    
    render(){

        return(
            <div className="troski">
                <Info Name="Location" Type="text"/>
                <div className="imgUpload"> 
                   <p></p> Click to upload profile image<br/>
                    <input type="file" accept="image/*" name="Upload" className="uploadImgStyle"/>
                </div>
                <br />
                <Button className="btnStyle">
                    Add vehicle
                </Button>
            </div>
        )
    }
}


function Info(props){

    return (
        <div className="Infostyle">
            <div className="InfostyleA">
                {props.Name}
            </div>
            <div className="InfostyleB">
                <input type={props.Type} placeholder={props.Holder} className="styleInput"/>
            </div>
        </div>
    )
}