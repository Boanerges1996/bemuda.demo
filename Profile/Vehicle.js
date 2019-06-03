import React from "react";
// written by Lawrence Ofoli Mensah

function Vehicle(props) {
  return (
    <div className="Vehicle">
      <h1>{props.title}</h1>
      <p>Registered Cars{props.NoRegCars}</p>
      <button className="butt">VIEW CARS</button>
    </div>
  );
}
export default Vehicle;
