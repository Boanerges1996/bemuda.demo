import React, {Component} from 'react';
import './ViewDrivers.css';
import DriverClass from './DriverClass';
import Drivers from'./Data.json';
// Written by Lawrene Ofoli
//component that renders cards of each driver
class ViewDrivers extends Component{
   
 render(){
        
        
        return(
            <div className="ViewDrivers">
                {Drivers.map((driver)=>{
                return(<DriverClass
                ImgUrl={driver.ImgUrl}
                name={driver.name}
                Age={driver.Age}
                Gender={driver.Gender}
                key={driver.id}
                click={this.ViewDetailHandler}
                phone={driver.phone}
                email={driver.email}
                


                />)
            })}
          
            </div>
            
        )
    }
}
export default ViewDrivers;