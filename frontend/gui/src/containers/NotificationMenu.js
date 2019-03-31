import React from 'react';
import axios from 'axios';
import { Dropdown, Icon, Button, Badge, List } from "antd";
import { connect } from "react-redux";

const gridStyle = {
    textAlign: 'center',
  };

const data = [
    'One',
    'Two',
    'Three'
]
const lists = (
    <div>
        <List
            size="small"
            dataSource={data}
            renderItem={item => (<List.Item>{item}</List.Item>)}
        />
    </div>
)

class NotificationMenu extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            notifications: []
        };
    }  

    componentDidMount() {
        const profID = localStorage.getItem("profID");
        axios.get(`http://127.0.0.1:8000/notification/${profID}`).then(res => {
            this.setState({
                notifications: res.data,
                length: res.data.length
            });
            
        })
        .catch(err => console.log(err));
    }

    render() {
        return (
        <div>
            <Dropdown overlay={
                <div>
                    <List 
                        size="small"
                        bordered
                        style={{backgroundColor: '#555'}}
                        dataSource = {this.state.notifications}
                        renderItem = {item => ( <a href={'/booklist/'+item.book} ><List.Item>{item.text}</List.Item></a>)}
                    />
                </div>
            } trigger={['click']}>
                <Badge count={this.state.length}>
                    <div>
                        <Button ghost>
                            <Icon type="bell" />
                        </Button>
                    </div>
                </Badge>
            </Dropdown>
        </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        userid: state.userId
    };
};

export default NotificationMenu;