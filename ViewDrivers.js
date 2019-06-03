import React, { Component } from 'react';
import './ViewDrivers.css';
import VehiclesClass from './VehiclesClass';


class ViewDrivers extends Component {

   
   DeleteVehicleHandler=(VehicleIndex)=>{
       const Vehicle=[...this.state.Vehicles];
       Vehicle.splice(VehicleIndex,1);
       this.setState({Vehicles:Vehicle})
   }

    state = {
        Vehicles: [
            {
                ImgUrl: require('./pic.jpg'),
                name: "VIP",
                id: 1,
                capacity: 20,
                lincencePlate: "HW-O0W",
            },
            {
                ImgUrl: require('./pic.jpg'),
                name: "Troski",
                id: 2,
                capacity: 16,
                lincencePlate: "BA-123",
            },
            {
                ImgUrl: require('./pic.jpg'),
                name: "VVip",
                id: 3,
                capacity: 45,
                lincencePlate: "GT-123",
            }



        ]
    }

 
    


   
    

    render(){
        return (
                <div>
                     {
                    this.state.Vehicles.map((veh,index)=>{
                    return (<VehiclesClass
                        ImgUrl={veh.ImgUrl}
                        name={veh.name}                 
                        capacity={veh.capacity}
                        lincencePlate={veh.lincencePlate}
                        key={veh.id}
                        click={()=>this.DeleteVehicleHandler(index)}
                    /> )                
                       
                     })
                    }

                     <label className='AddCar'>Click to add a car</label>
                       <button className='AddCar'>ADD CAR</button>
                </div>)
                
                 
                 
    }
}
export default ViewDrivers;