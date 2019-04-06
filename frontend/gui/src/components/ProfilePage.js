import React from 'react';
import axios from 'axios';
import { Card, Row, Col, List } from "antd";
import { connect } from "react-redux";
import NotificationMenu from '../containers/NotificationMenu';

const gridStyle = {
    textAlign: 'center',
  };

class ProfilePage extends React.Component {
    
    state = {
        profile: {}
    }

    constructor(props) {
        super(props);
        this.state = {
            FA: "Fantasy",
            NF: "Non Fiction",
            RO: "Romance",
            TR: "Thriller",
            MY: "Mystery",
            BI: "Biography",
            FI: "Fiction",
            SF: "Science Fiction",
            image_url: "https://www.flynz.co.nz/wp-content/uploads/profile-placeholder.png",
            avatar: this.state.image_url
        };
    }  


    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/profile/${this.props.userid}`).then(res => {
            this.setState({
                first_name: res.data.first_name,
                last_name: res.data.last_name,
                review_count: res.data.review_count,
                creation_date: res.data.creation_date,
                bio: res.data.bio,
                genre: res.data.genre,
                books: res.data.favorites,
                authors: res.data.following,
                avatar: res.data.avatar
            });
            localStorage.setItem("profID", res.data.pk);
            console.log(localStorage.getItem("profID"));

        })
    }

    render() {
        return (
                <div>
                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={4}>
                            <Card bodyStyle={{
                                padding: 0
                            }}>
                                <img src={this.state.avatar} 
                                style={{
                                    width: 194, height: 224
                                }}
                                width="100%" height="100%" >
                                </img>
                            </Card>
                        </Col>
                        
                        <Col span={18}>
                            <Card title={
                                <div style={{display:'flex', alignItems: 'stretch'}}>
                                    <Col span={22}>
                                        {this.state.first_name + " " + this.state.last_name}
                                    </Col>
                                    <NotificationMenu history={this.props.history}/>
                                </div>} 
                                headStyle={{
                                    fontSize: 20,
                                    fontStyle: 'italic',
                                    fontFamily: 'Georgia', 
                                    background: '#020037',
                                    color: 'white'
                                }}>
                                <p>
                                    <b><i>User Since: </i></b> 
                                    {this.state.creation_date}
                                </p>
                                
                                <p>
                                    <b><i>Review Count: </i></b> 
                                    {this.state.review_count}
                                </p>
                                
                                <p>
                                    <b><i>Favorite Genre: </i></b>
                                    {this.state[this.state.genre]}
                                </p>


                            </Card>
                        </Col>

                    </Row>

                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={22}>
                            <Card 
                                style={gridStyle} 
                                title="About Me" 
                                headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia', 
                                background: '#020037',
                                color: 'white'
                                }}
                            >
                                <p>
                                    {this.state.bio}
                                </p>
                            </Card>
                        </Col>
                    </Row>

                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={11}>
                        <Card 
                            title="Favorites"
                            headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia', 
                                background: '#020037',
                                color: 'white'
                            }}
                        >
                        <List
                            pagination={{
                                onChange: (page) => {
                                    console.log(page);
                                },
                                pageSize: 2,
                            }}
                            grid={{ gutter: 0, column: 2 }}
                            dataSource={this.state.books}
                            renderItem={item => (
                                <List.Item>
                                    <Card
                                        hoverable
                                        style={{ width: 180, background: '#F6C564'}}
                                        cover={<img alt={item.title} src={item.image_url} style={{width:178, height: 250}} />}
                                    >
                                        <Card.Meta
                                        title={<a href={'/booklist/'+item.pk}><b>{item.title}</b></a>}
                                        />
                                    </Card>
                                </List.Item>
                            )}
                        />
                        </Card>
                        </Col>

                        <Col span={11}>
                        <Card 
                            title="Following"
                            headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia', 
                                background: '#020037',
                                color: 'white'
                            }}
                        >
                        <List
                            pagination={{
                                onChange: (page) => {
                                    console.log(page);
                                },
                                pageSize: 2,
                            }}
                            grid={{ gutter: 0, column: 2 }}
                            dataSource={this.state.authors}
                            renderItem={item => (
                                <List.Item>
                                    <Card
                                        hoverable
                                        style={{ width: 180, background: '#F6C564', color: 'white'}}
                                        cover={<img alt={item.name} src={item.image_url} style={{width:178, height: 250}} />}
                                    >
                                        <Card.Meta
                                        title={<a href={'/authors/'+item.pk}><b>{item.name}</b></a>}
                                        />
                                    </Card>
                                </List.Item>
                            )}
                        />
                        </Card>
                        </Col>
                    </Row>
                </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        userid: state.userId
    };
};

export default connect(mapStateToProps)(ProfilePage);