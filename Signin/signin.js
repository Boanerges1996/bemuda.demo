import React from 'react';
import './signin.css';
import axios from 'axios';



class Signin extends React.Component{
    state = {
        firstname:'',
        lastname:'',
        username:'',
        phonenumber:'',
        email:'',
        password:'',
        confirmpass:'',
        emailError:'',
        showError:false,
    }
    
    /*
    Handling submit functions and events
     */
    submitForm = e =>{
        e.preventDefault();
        /* This is for the client-side validation */
        if(!this.state.email.includes('@')){
            this.setState({
                showError:true,
                emailError:'invalid email'
            })
        }
        else{
            this.setState({
                showError:false,
                emailError:''
            })
        }
        console.log(this.state)
    }
    /* This code is sent to the backend API */
    handleSubmit(event){
        event.preventDefault();
        let userInfo = new FormData(event.target);
        let data = {}
        userInfo.forEach((value,key)=>{
            data[key]=value
        });
        data['othernames']=''
        data['user_avatar']=`https://firebasestorage.googleapis.com/v0/b/vehicle-rental-a0b39.appspot.
        com/o/Images%2FdefaultAvatar%2FdefaultUserAvatar.png?alt=media&token=b044f2f2-f3c7-492d-8955-7aa44e43dd32`
        console.log(data)
        axios.post('http://127.0.0.1:5000/user/sign_up',data)
    }
    
    render(){

        /* This is to show the emailError message */
        let errorMessage = null;

        const errorStyle = {
            color:'red',
            fontSize:'12px'
        }
        const style = {
            fontSize:'20px'
        }
        const formErrors ={
            color:'red',
            fontSize:'12px'
        }
        /* This sets a value for the email error message when the showError is true */
        if(this.state.showError){
            errorMessage = (
                <div style={errorStyle}>
                    {this.state.emailError}
                </div>
            )
        }


        return(
            <div className='Signin'>
                <div className='SigninActual'>
                    <div className='SigninActualComment'>
                        <h1>Bemuda Rentals</h1>
                        <p style={style}>
                            Login to enjoy our wondeful services
                            <p>Welcome to Bermuda Rentals</p>
                            <p>Sign up to create an account</p>
                        </p>
                    </div>
                    <form className='myForm' onSubmit={this.handleSubmit}>
                        {/* Firstname */}
                        <input type="text" name="firstname" value={this.state.firstname} 
                        className="SigninInputBox" placeholder="&#xf007; Firstname"
                        onChange={e=>{
                            this.setState({firstname:e.target.value})
                        }} />
                        <br/>

                        {/* Lastname */}
                        <input type='text' name='lastname' placeholder='&#xf007; Lastname' className="SigninInputBox"
                        value={this.state.lastname}
                        onChange={e=>{
                            this.setState({
                                lastname:e.target.value
                            })
                        }}/>
                        <br/>
                        
                        {/* othernames */}
                        <input type='text' name='username' placeholder='&#xf007; Username' className="SigninInputBox"
                        value={this.state.othernames}
                        onChange={e=>{
                            this.setState({
                                username:e.target.value
                            })
                        }}/>
                        <br/>

                        {/* phonenumber */}
                        <input type='text' name='telephone_number' placeholder='&#xf095; Phone' className="SigninInputBox"
                        value={this.state.phonenumber}
                        onChange={e=>{
                            this.setState({
                                phonenumber:e.target.value
                            })
                        }}/>
                        <br/>
                        
                        {/* Email */}
                        <input type='email' name='email' placeholder='&#xf199; Email' className="SigninInputBox"
                        value={this.state.email}
                        onChange={e=>{
                            this.setState({
                                email:e.target.value
                            })
                        }}/>
                        <br/>
                        {errorMessage}
                        
                        {/* Password */}
                        <input type='password' name='user_password' placeholder='&#xf084; Password' className="SigninInputBox"
                        value={this.state.password}
                        onChange={e=>{
                            this.setState({
                                password:e.target.value
                            })
                        }}/>
                        <br/>
                        
                        
                        <input type='password' name='confirmpass' placeholder='&#xf084; Confirm Password' className="SigninInputBox"
                        value={this.state.confirmpass}
                        onChange={e=>{
                            this.setState({
                                confirmpass:e.target.value
                            })
                        }}/><br/>
                        
                        <input type="submit" name="submit" className="SigninSubmitStyle" value='Signin'/>
                        
                    </form>

                </div>
                <div className='SigninOther'>
                     <div className='SigninOtherCovering'>

                     </div>
                </div>
            </div>
        )
    }
}
export default Signin;