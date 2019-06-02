import React from 'react';
import { Button } from 'semantic-ui-react';
import {storage} from '../../../../../index';
import './imageUploads.css';


export default class Imageupload extends React.Component{
    constructor(props){
        super(props)
        this.state={
            image:null,
            url:""
        }
        this.handleChange = this.handleChange.bind(this)
        this.uploadImage = this.uploadImage.bind(this)
    }
    handleChange=e=>{
        if(e.target.files[0]){
            let reader = new FileReader()
            const image = e.target.files[0]
            reader.onloadend=()=>{
                this.setState({
                    image:image,
                    url:reader.result
                })
            }
            reader.readAsDataURL(image)
        }
    }
    uploadImage=()=>{

    }
    render(){
        const myStyle={
            width:'50%',
            height:'110px',
            backgroundImage:'src('+this.state.url+')'
        }

        return(
            <div className="imageUpload">
                <input type="file" onChange={this.handleChange}/>
                
                <div>
                    {this.state.url?<img src={this.state.url} alt="Ur image"className="styleImage"/>:null}
                </div>
                
            </div>
            
        )
    }
}