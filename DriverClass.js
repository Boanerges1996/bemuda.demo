import React,{Component} from 'react';
import Base from './Base';
//Written by Mensah Ofoli Lawrence
//Class component that renders the driver's page

class DriverClass extends Component{
        
    state={
        ViewDetail:false
          }

    ViewDetailHandler=()=>{
        this.setState({ViewDetail:true})
    }

    ViewedHandler=()=>{
        this.setState({ViewDetail:false})
    }
     

    render(){
        let BaseContent=null;

        return(
            <div className ="DriverClass">
                <img src={this.props.ImgUrl} alt="ANNNNIK"/>
                <h2>{this.props.name}</h2>
                <h2>{this.props.Age} years</h2>
                <h2>{this.props.Gender}</h2>
                <button onClick={this.ViewDetailHandler}>MORE DETAILS</button>


                {     
                this.state.ViewDetail?
                (BaseContent= <Base
                    bclick={this.ViewedHandler}
                    phone={this.props.phone}
                    email={this.props.email}
                />):null
            
                
            }
            {BaseContent}
            </div>
               
        )
    }
    
}
export default DriverClass;