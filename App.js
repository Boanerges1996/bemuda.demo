import React, { Component } from 'react';
import './App.css';



class App extends Component{
  state={
    dateOfBirth: null,
    gender: null,
    residence:null,
    lisence:null,

    formErrors: {
      dateOfBirth:'',
      gender: '',
      residence:'',
      lisence:''
    }
  }

  change=(e)=>{
   let  value = e.target.value
    this.setState({
        dateOfBirth: '',
        gender: '',
        residence:'',
        lisence:'',

    })
}
    onSubmit = e =>{
    e.preventDefault();
  
    }
       
   
    
render() {
  return(
  <div className='App'>
    
      <div className='App__Form'>
      

          <div className='FormTitle'>
            <h1 className='FormTitle__Link'>Sign Up as a driver</h1>
          
          </div>

     <div className='FormCenter'>
        <form className='FormFields'>
          <div className='FormField'></div>

         
         <div>
         <label htmlFor="start">Date Of Birth</label>
             <input type="date" id="start" name="trip-start"
                   min="1900-01-01" max="2050-12-31" required />
          <span className="validity"onChange={this.change} dateOfBirth={this.state.dateOfBirth}
          ></span>
           </div>

            <label htmlFor="Male">Male</label>
            <input type="radio" id="Male" name="gender" value="Male"
                  onChange={this.change} gender={this.state.gender} checked/>
            
            <label htmlFor="Female">Female</label>
            <input type="radio" id="Female" name="gender" value="Female"
            onChange={this.change} gender={this.state.gender}
                  />       

           <label className='FormField__Label' htmlFor="residential"></label>
           <input type='text'  className='FormField__Input' placeholder='Residential Address'
            name='residential' noValidate onChange={this.change}  residence={this.state.residence}
            formErrors = {this.state.formErrors} minlength='3' ></input>

             <label className='FormField__Label' htmlFor="lisence"></label>
           <input type='text'  className='FormField__Input' placeholder='Lisence Number'
           name='liscence' onChange={this.change} lisence={this.state.lisence} 
           formErrors = {this.state.formErrors} maxlength='16'/>
        
           
            <div className='FormField'>
              <button className='FormField__Button mr-20'>Sign Up</button>
            </div>
            </form>


 


            




     </div>
      
    </div>
    <div className='App__Aside'></div>
  </div>
 
  );
}
}

export default App;