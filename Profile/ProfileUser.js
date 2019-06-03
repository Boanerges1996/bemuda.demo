import React, { Component } from "react";
// written by Lawrence Ofoli Mensah

class ProfileUser extends Component {
  state = {
    Users: [
      {
        title: "USER",
        fname: "30",
        lname: "male",
        others: "Kwaku",
        email: "lawrence",
        phone: "0244321299"
      }
    ]
  };

  render() {
    return (
      <div className="ProfileUser">
        <h1 className="head">{this.state.Users[0].title}</h1>
        <p> First Name{this.state.Users[0].fname}</p>
        <p> Last Name{this.state.Users[0].lname}</p>
        <p> other Name{this.state.Users[0].others}</p>
        <p> Email{this.state.Users[0].email}</p>
        <p> Phone{this.state.Users[0].phone}</p>
      </div>
    );
  }
}
export default ProfileUser;
