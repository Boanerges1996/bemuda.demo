import React from "react";
// written by Lawrence Ofoli Mensah

function UpdateDriverInfo(props) {
  return (
    <div className="UpdateDriverInfo">
      <input
        placeholder="age"
        type="text"
        name="age"
        onChange={props.changeAge}
      />
      <br />
      <input
        placeholder="gender"
        type="text"
        name="gender"
        onChange={props.changeGender}
      />
      <br />
      <input
        placeholder="city"
        type="text"
        name="city"
        onChange={props.changeCity}
      />
      <br />
      <input
        placeholder="lincence"
        type="text"
        name="lincence"
        onChange={props.changeLincence}
      />
      <br />
      <input
        placeholder="residence"
        type="text"
        name="residence"
        onChange={props.changeResidence}
      />
      <br />
      <button onClick={props.DCancelEdit}>CANCEL</button>
      <button onClick={props.DriverUpdate}>UPDATE</button>
    </div>
  );
}
export default UpdateDriverInfo;
