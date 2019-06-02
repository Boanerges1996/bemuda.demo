import React from 'react';
import './privateCar.css';
import { Button, Input } from 'semantic-ui-react';


export default function PrivateCar(props){
    return(
        <div className="privateCars">
            <Info Name="location" Type="text"/><br/>
            <Button className="btnStyleA">
                    Add vehicle
            </Button>
        </div>
    )
}


export function Info(props){

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