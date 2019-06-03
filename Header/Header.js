import React, {Component}from 'react';
import './Header.css';
import Login from '../Login/Login';
import LoginBackDrop from '../Login/LoginBackdrop';
import Signin from '../Signin/signin';
import  SigninBackdrop from '../Signin/signinBackdrop';


/*
wriiten by Azungah Hillary

This Contains the Header component with the Logo, and other
Links such as sign-in,sign-up,about-us,service
 */

class Header extends Component{
    state = {
        LoginStatus:false,
        SigninStatus:false
    }
    /* Login Part */
    loginToggle = ()=>{
        this.setState({
            LoginStatus:true
        })
    }
    closeLoginModal = ()=>{
        this.setState({
            LoginStatus:false
        })
    }
    /* Sign in part */
    signinToggle = ()=>{
        this.setState({
            SigninStatus:true
        })
    }
    closeSigninBack = ()=>{
        this.setState({
            SigninStatus:false
        })
    }

    
    render(){
        let Log = null;
        let loginBackdrop = null;
        let signin = null
        if (this.state.LoginStatus){
            Log = <Login />
        }
        if (this.state.SigninStatus){
            signin = <Signin />
        }
        return (
            <div className='Header' on>
                <div className='HeaderLogo'>
                </div>
                <div className='Header2' >
                    <div className='Header21' /*The Login and SignUp will be done by a Modal */>
                        <a className='HeaderTopLink' onClick={this.signinToggle}>SIGNUP</a>
                        <a className='HeaderTopLink' onClick={this.loginToggle}>LOGIN</a>
                    </div>
                    <div className='Header22' /*It will navigate to the bottom of the page */>
                        <a className='HeaderBotomLink' href='#'>
                        <a className="HeaderBotom" href='#section3'>
                        CONTACTS
                        </a>
                        
                        </a>
                        <a className='HeaderBotomLink' href='#'>
                        <a className="HeaderBotom" href='#section2'>  
                        SERVICES
                        </a>
                        
                        </a>
                        <a className='HeaderBotomLink' href='#'>
                        <a className="HeaderBotom" href='#section1'>   
                        ABOUT US
                          </a> 
                        
                        </a>
                        <a className='HeaderBotomLink' href='#'>HOME</a>
                    </div>
                </div>
                {Log}
                {signin}
                {this.state.LoginStatus ? <LoginBackDrop click={this.closeLoginModal}/>:null}
                {this.state.SigninStatus ? <SigninBackdrop click={this.closeSigninBack} />:null}
            </div>
        );
    }
    

}

export default Header;