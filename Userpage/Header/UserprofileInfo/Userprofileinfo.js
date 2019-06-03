import React from "react";
import "./Userprofileinfo.css";
import { Route, Link } from "react-router-dom";
{
  /*import '../../../../../node_modules/font-awesome/css/font-awesome.min.css';*/
}

class UserprofileModal extends React.Component {
  render() {
    return (
      <div className="UserprofileModal">
        <div className="UserprofileInfoHead">
          <div className="UserProfileAvatar">
            <img
              src={require("../boanerges.jpg")}
              className="profileImageStyle"
            />
          </div>
          <div className="UserProfileName">
            WELCOME <br />
            <div className="UsernameDiv"> Kwaku</div>
            <div className="SpecialLinkDiv">BERMUDA</div>
          </div>
        </div>

        <div className="UserprofileInfoContent">
          <div className="UserprofileList">
            &#xf007; <Link to="/user/vehicle/viewProfile">View Profile</Link>
          </div>
          <div className="UserprofileList">&#xf1de; Settings</div>
          <div className="UserprofileList">
            <i class="fa fa-sign-out" />
            Logout
          </div>
        </div>
      </div>
    );
  }
}

export default UserprofileModal;
