import React, { Component } from "react";
// import Homepage from './Components/Homepage/Homepage';
import { BrowserRouter } from "react-router-dom";
import { Route, Link } from "react-router-dom";
import VehicleRegistration from "./Components/Userpage/Userbodies/vehicleRegistration/vehicleRegistration";

import Vehiclepage from "./Components/Userpage/Userbodies/Vehicles/Vehiclepage";
import Userpage from "./Components/Userpage/Userpage";
import "./App.css";
import Homepage from "./Homepage";
import Driverreg from "./Components/Driver Registration/Driverreg";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Route path="/" exact component={Homepage} />
          {/* // <Homepage /> */}
          {/*<Trysemantic />*/}
          {/* <Userpage /> */}
          {/* <Vehiclepage /> */}
          {/* <VehicleRegistration /> */}
          {/* <Route path='/user/vehicles' exact render={()=>{
            return(
              <div>
                <Userpage />
                <Vehiclepage />
              </div>
            )
           
          }} /> */}
          <Route path="/user/vehicles" exact component={Vehiclepage} />
          <Route
            path="/user/vehicle/registration"
            exact
            component={VehicleRegistration}
          />

          <Route path="/user/driver" exact component={Driverreg} />
          <Route path="/user/driver/registration" exact component={Driverreg} />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
