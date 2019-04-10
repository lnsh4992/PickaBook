import React from 'react';
import { Form, Input, Button, Select } from 'antd';
import { connect } from "react-redux";

import axios from 'axios';

const FormItem = Form.Item;
const { TextArea } = Input;
const Option = Select.Option;


class ProfileRegistrationForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = { genre: "FA" };
      }

    handleFileSelect = event => {
        this.setState({
            selectedFile: event.target.files[0]
        })
    }

    handleFormSubmit = (event, userID) => {
        event.preventDefault();
        console.log(this.state)

        let img_data = new FormData()
        img_data.append('avatar', this.state.selectedFile)
        fetch(`http://127.0.0.1:8000/profile/updatepicprof/${this.state.profID}`, {
            method: 'PUT',
            headers: {
                Accept: 'application/json, text/plain, */*',
            },
            body: img_data
        }).then(res => res.json())
        .then((data) => {
            console.log(data);
        })
        .catch(err => console.log(err))

        axios.put(`http://127.0.0.1:8000/profile/update/${userID}`, {
            first_name: event.target.elements.firstname.value,
            last_name: event.target.elements.lastname.value,
            bio: event.target.elements.bio.value,
            genre: this.state.genre
        })
        .then(res => console.log(res))
        .catch(error => console.log(error));
        this.props.history.push('/profile');
    }

    handleGenreChange = (value) => {
        this.setState({genre: value});
    }

    handlePrivacyChange = (value) => {
      this.setState({privacy: value});
    }

    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/profile/${this.props.userid}`).then(res => {
            this.setState({
                profID: res.data.pk
            })

        })
    }

    render() {
        return (
            <div>
                <Form onSubmit={(event) => this.handleFormSubmit(
                    event,
                    this.props.userid
                )}>
                    <FormItem label="Privacy">
                      <Select name="privacy" defaultValue="False"
                      onChange={(value) => this.handlePrivacyChange(value)}>
                        <Option value="True">True</Option>
                        <Option value="False">False</Option>
                      </Select>
                    </FormItem>

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
