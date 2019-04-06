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

    handleClick = (bookID, notifID) => {
        axios.delete(`http://127.0.0.1:8000/notification/destroy/${notifID}`);
        this.props.history.push('/booklist/'+bookID);
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
                        renderItem = {item => ( 
                            <List.Item onClick={()=>this.handleClick(item.book, item.pk)}><a href="#">{item.text}</a></List.Item>
                            )}
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