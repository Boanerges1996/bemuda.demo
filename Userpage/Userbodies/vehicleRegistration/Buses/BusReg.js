import React from 'react';
import ImageUpload from '../ImageUpload/imageUploads';
import './BusReg.css';
import { Button } from 'semantic-ui-react';


export default class BusReg extends React.Component{
    state ={
        Car_number:"",
        Capacity:""
    }

    storeCarNumber=(e)=>{
        let value=e.target.value
        this.setState({
            Car_number:value
        })
    }
    storeCapacity=(e)=>{
        let value = e.target.value
        this.setState({
            Capacity:value
        })
    }
    render(){
        return(
            <div className="VehReg">
                <Info Name="Car number" Holder="Car number" Change={this.storeCarNumber}/>
                <Info Name="Capacity" Holder="Capacity" Change={this.storeCapacity}/>
                <ImageUpload />
                <Button className="btnStyle">
                    Send
                </Button>
            </div>
        )
    }
}

export function Info(props){

    return (
        <div className="Infostyle">
            <div className="InfostyleA">
                {props.Name}
            </div>
            <div className="InfostyleB">
                <input type={props.Type} placeholder={props.Holder} className="styleInput" onChange={props.Change}/>
            </div>
        </div>
    )
}