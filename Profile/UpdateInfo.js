import React from 'react';
// written by Lawrence Ofoli Mensah

function UpdateInfo (props){
    return( <div className="UpdateInfo">
        <h1>Updating Form</h1>
        <input placeholder='First Name' type='text' name='fname' onChange={props.changeFname}/><br />
        <input placeholder='Last Name' type='text' name='lname' onChange={props.changeLname}/><br />
        <input placeholder='Other Names' type='text' name='oname' onChange={props.changeOname} /><br />
        <input placeholder='Phone' type='tel' name='number' onChange={props.changePhone}/><br />
        <input placeholder='Email' type='email' name='email' onChange={props.changeEmail}/><br />
        <button onClick={props.UCancelEdit}>CANCEL</button>
        <button  onClick={props.Update}>UPDATE</button>
        
    </div>
       
    )
}
export default UpdateInfo;