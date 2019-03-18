import React from 'react';
import { Form, Input, Button, Select, Avatar } from 'antd';
import { connect } from "react-redux";

import axios from 'axios';

const FormItem = Form.Item;
const { TextArea } = Input;
const Option = Select.Option;


class ProfileRegistrationForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = { 
            genre: "FA",
            selectedFile: null
        };
      }

    handleFileSelect = event => {
        this.setState({
            selectedFile: event.target.files[0]
        })
    }

    // handleFileUpload = () => {
    //     const data = new FormData()
    //     data.append('file', this.state.selectedFile, this.state.selectedFile.name)

    //     axios.post('http://localhost:8000/media/user_avatar/', data, {
    //         onUploadProgress: ProgressEvent => {
    //             this.setState({
    //                 loaded: (ProgressEvent.loaded / ProgressEvent.total*100),
    //             })
    //         },
    //     })
    //     .then(res => {
    //         console.log(res.statusText)
    //     })

    // }

    handleFormSubmit = (event, userID) => {
        event.preventDefault();

        const img_data = new FormData()
        img_data.append('file', this.state.selectedFile, this.state.selectedFile.name)

        axios.put(`http://127.0.0.1:8000/profile/update/${userID}`, {
            first_name: event.target.elements.firstname.value,
            last_name: event.target.elements.lastname.value,
            bio: event.target.elements.bio.value,
            genre: this.state.genre,
            avatar: this.state.img_data     // <---- for user story #6
        })
        .then(res => console.log(res))
        .catch(error => console.log(error));
        this.props.history.push('/profile');
    }

    handleGenreChange = (value) => {
        this.setState({genre: value});
    }

    render() {
        return (
            <div>
                <Form onSubmit={(event) => this.handleFormSubmit(
                    event,
                    this.props.userid
                )}>
                    <FormItem label="First Name" >
                        <Input name="firstname" placeholder="First name" />
                    </FormItem>

                    <FormItem label="Last Name" >
                        <Input name="lastname" placeholder="Last name" />
                    </FormItem>
                    
                    <FormItem label = "Bio" >
                        <TextArea name="bio" placeholder="About Me!" autosize={{minRows: 2}} />
                    </FormItem>

                    <FormItem label = "Genre" >
                        <Select name="genre" defaultValue="FA" 
                        onChange={(value) => this.handleGenreChange(value)}>
                            <Option value="FA">Fantasy</Option>
                            <Option value="RO">Romance</Option>
                            <Option value="TR">Thriller</Option>
                            <Option value="MY">Mystery</Option>
                            <Option value="BI">Biography</Option>
                            <Option value="FI">Fiction</Option>
                            <Option value="NF">Non Fiction</Option>
                            <Option value="SF">Science Fiction</Option>
                        </Select>    
                    </FormItem>
                    
                    <FormItem label = "Avatar">
                        <input 
                         type="file" 
                         name="" 
                         id="" 
                         onChange={this.handleFileSelect} />
                    </FormItem>

                    <FormItem>
                        <Button type="primary" htmlType="submit">
                            Submit!
                        </Button>
                    </FormItem>

                </Form>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        userid: state.userId
    };
};

export default connect(mapStateToProps)(ProfileRegistrationForm);