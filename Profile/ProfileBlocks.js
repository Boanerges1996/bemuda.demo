import React, { Component } from "react";
import User from "./User";
import Driver from "./Driver";
import Vehicle from "./Vehicle";
//import Updating from "./Updating";
import UpdateInfo from './UpdateInfo';
import UpdateDriverInfo from "./UpdateDriverInfo";


class ProfileBlocks extends Component {
  state = {
    ProfileData: [
      {
        id: 1,
        title: ["USER", "DRIVER", "VEHICLE"],
        fname: "kwesi",
        lname: "obou",
        oname: "frank",
        phone: 233244123980,
        email: "marie@gmail.com",
        age: 38,
        gender: "male",
        city: "Accra",
        lincence: "ABC1234777890123",
        residence: "Ho AK323",
        NoRegCars: 7,
        address: "HO 487"
      }

    ],
   
      firstname:'',
      lastname:'',
      othernames:'',
      email:'',
      phone:'',
      age:'',
      gender:'',
      city:'',
      lincence:'',
    
    EditUser:false,
    EditDriver:false
  }
    

  changeFirstName=e=>{
    let value=e.target.value
    this.setState({
      firstname:value
    })
  }
  changeLastName=e=>{
    let value=e.target.value
    this.setState({
      lastname:value
    })
  }
  changeOtherName=e=>{
    let value=e.target.value
    this.setState({
      othernames:value
    })
  }
  changePhoneNum=e=>{
    let value=e.target.value
    this.setState({
      phone:value
    })
  }
  changeEmail=e=>{
    let value=e.target.value
    this.setState({
      email:value
    })
  }
      
      changeDriver=(event)=>{
         this.setState({[event.target.name]:event.target.value});
      }


  UserEditHandler=()=>{
    this.setState({EditUser:true})
  }
  
  DriverEditHandler=()=>{
    this.setState({EditDriver:true})
  }
  
  DriverEditCancelHandler=()=>{
    this.setState({EditDriver:false})
  }
 
  UserEditCancelHandler=()=>{
    this.setState({EditUser:false})
  }
  
    UpdateHandler=(event)=>{
      this.setState({
        ProfileData: [
          {
            id: 1,
            title: ["USER", "DRIVER", "VEHICLE"],
            fname: this.state.firstname,
            lname: this.state.lastname,
            oname: this.state.othernames,
            phone: this.state.phone,
            email: this.state.email,
            age: 38,
            gender: "male",
            city: "Accra",
            lincence: "ABC1234777890123",
            residence: "Ho AK323",
            NoRegCars: 7,
            address: "HO 487"
          }
        ],
      })
    } 
    
    DriverUpdateHandler=(event)=>{
      this.setState({
        ProfileData: [
          {
            id: 1,
            title: ["USER", "DRIVER", "VEHICLE"],
            fname: "kwesi",
            lname: "obou",
            oname: "frank",
            phone: 233244123980,
            email: "marie@gmail.com",
            age: this.state.age,
            gender: this.state.gender,
            city:this.state.city ,
            lincence: this.state.lincence,
            residence: this.state.residence,
            NoRegCars: 7,
            address: "HO 487"
          }
    
        ],
      })

    }

  render() {
    let UActivator=null;
    let DActivator=null;
    return (
      <div className="Wrapper">
        <div className="ProfileBlocks">
          {this.state.ProfileData.map(Data => {
            return (
              <User
                title={Data.title[0]}
                fname={Data.fname}
                lname={Data.lname}
                oname={Data.oname}
                phone={Data.phone}
                email={Data.email}
                key={Data.id}
                Uclick={this.UserEditHandler}
               
              />
            );
          })}
         
          
        </div>
        <div className="ProfileBlocks">
          {this.state.ProfileData.map(Data => {
            return (
              <Driver
                title={Data.title[1]}
                gender={Data.gender}
                age={Data.age}
                lincence={Data.lincence}
                city={Data.city}
                residence={Data.residence}
                key={Data.id}
                Dclick={this.DriverEditHandler}
              />
            );
          })}
        </div>
        <div className="ProfileBlock">
          {this.state.ProfileData.map(Data => {
            return (
              <Vehicle
                title={Data.title[2]}
                NoRegCars={Data.NoRegCars}
                key={Data.id}
                
              />
            );
          })}
        </div>
        {
             this.state.EditUser?(UActivator=(<UpdateInfo
              UCancelEdit={this.UserEditCancelHandler}
              Update={this.UpdateHandler}
              changeFname={this.changeFirstName}
              changeLname={this.changeLastName}
              changeOname={this.changeOtherName}
              changeEmail={this.changeEmail}
              changePhone={this.changePhoneNum}
              />
            
          
             
             )):null}
          
          {UActivator}
      
       
       {
            this.state.EditDriver?(DActivator=(<UpdateDriverInfo
             DCancelEdit={this.DriverEditCancelHandler}
             DriverUpdate={this.DriverUpdateHandler}
             changeAge={this.changeDriver}
             changeGender={this.changeDriver}
             changeCity={this.changeDriver}
             changeLincence={this.changeDriver}
             changeResidence={this.changeDriver}
             />
           
         
            
            )):null}
         
         {DActivator}
     </div>
    );
  }
}

export default ProfileBlocks;
