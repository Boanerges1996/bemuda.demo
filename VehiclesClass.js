import React from  'react';

function VehiclesClass(props){
    return(<div>
         <div className="VehiclesClass">
             <img src={props.ImgUrl} alt="ANNNNIK" />
             <h1>{props.name}</h1>
             <h1>{props.capacity}</h1>
             <h1>{props.lincencePlate}</h1>
             <button onClick={props.click}>DELETE VEHICLE</button>
       </div>
      
    </div>
       
    )
       
    
}

export default VehiclesClass;