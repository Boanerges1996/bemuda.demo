import React, { Component } from 'react';
import './Login.css';
import '../../../node_modules/font-awesome/css/font-awesome.min.css';

/*
This was written by Nkrumah Samson Kwaku

EDITING REQUIRED
1. The Submit button animation on hover.
2. Add an image to the front of the 
*/

class Login extends Component{
    state = {
        username:'',

    }

    render(){
        const style = {
            fontSize:'20px'
        }
        return (
            <div className='Login'>
                <div className='LoginActual'>
                    <div className='LoginActualComment'>
                        <h1>Bemuda Rentals</h1>
                        <p style={style}>
                            Login to enjoy our wondeful services
                            
                            <img src={require('./Logo.png')}/>
                        </p>
                    </div>
                    <form className='myForm'>
                        <input type="text" name="username" className="LoginInputBox" placeholder="&#xf007; Username" /><br/>
                        <input type='password' name='password' placeholder='&#xf09c; Password' className="LoginInputBox"/><br/>
                        <input type="submit" name="submit" className="LoginSubmitStyle" value='Login'/>
                        
                    </form>

                </div>
                <div className='LoginOther'>
                     <div className='LoginOtherCovering'>

                     </div>
                </div>
            </div>
        )
    }
}

export default Login;