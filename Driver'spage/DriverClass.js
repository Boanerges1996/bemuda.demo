import React from "react";
// written by Lawrence Ofoli Mensah
function DriverClass(props) {
  return (
    <div className="DriverClass">
      <img src={props.ImgUrl} alt="ANNNNIK" />
      <h1>{props.name}</h1>
      <h1>Age:{props.Age}</h1>
      <h1>{props.Gender}</h1>
      <button onClick={props.click}>MORE DETAILS</button>
    </div>
  );
}
export default DriverClass;
