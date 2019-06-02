import React from 'react'


function Subbox1(){

   return(
    <div className="Subbox1">

        <div className="pageheader">
                        <p>Welcome to</p>
                        <h1>Bermuda Rentals</h1>
                        <p>Sign up to create an account</p>
        </div>

      <form>
          <div className="formlist">
               <input type="text" id="fname" placeholder="First Name"/>
          </div>
          <div className="formlist">
               <input type="text" id="fname" placeholder="Other names(s)"/>
          </div>
          <div className="formlist">
               <input type="tel" id="fname" placeholder="Phone"/>
          </div>
          <div className="formlist">
               <input type="email" id="fname" placeholder="Email"/>
          </div>
          <div className="formlist">
               <input type="password" id="fname" placeholder="password"/>
          </div>
          <div className="formlist">
               <input type="password" id="fname" placeholder="Confirm password"/>
          </div>
          <div className="btn">
          <input type= "submit" value="Sign Up" name="submit_form" id="submit_button" />
          </div>
      </form>
           
    </div>

   )
}

export default Subbox1;