import React from 'react';
import axios from 'axios';
import { Card, Row, Col, List, message, Avatar, Icon, Rate } from "antd";
import { connect } from "react-redux";
import NotificationMenu from '../containers/NotificationMenu';

const gridStyle = {
    textAlign: 'left',
  };

const LikeStyle = {
    marginRight : 8,
    color: '#378695'
};

const DislikeStyle = {
    marginRight : 8,
    color: '#900e01'
};

const IconText = ({ type, text, onClick, theme, style }) => (
    <span>
        <Icon type={type} style={style} onClick={onClick} theme={theme}/>
        {text}
    </span>
);

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
            avatar: this.state.image_url,
            reviews: []
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
                avatar: res.data.avatar,
                profID: res.data.pk
            });
            localStorage.setItem("profID", res.data.pk);

            this.fetchReviews();
        })
    }

    fetchReviews = () => {
        const pr_ID = this.state.profID;
        axios.get(`http://127.0.0.1:8000/bookreview/user/${pr_ID}`).then(res => {
            console.log(res);            
            this.setState({
                reviews: res.data,
                max_length: res.data.length,
                current_length: Math.min(3, res.data.length)
            })


        })
        .catch(error => console.log(error));
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
                                        {
                                            this.state.review_count > 10 &&
                                                <Icon style={{marginLeft: 10, color: '#DAA520'}} type="crown" theme="filled" />
                                        }
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
                                color: 'white',
                                textAlign: 'left'
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

                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={22}>
                            <Card 
                                style={gridStyle} 
                                title="My Reviews"
                                headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia', 
                                background: '#020037',
                                color: 'white',
                                textAlign: 'left'
                                }}
                            >

                                <Col span={12} style={{ marginBottom: 16 }} type="flex" justify="left">
                                    <Card 
                                    style={gridStyle} 
                                    title="Books"
                                    headStyle={{
                                    fontSize: 20,
                                    fontStyle: 'italic',
                                    fontFamily: 'Georgia', 
                                    background: '#020037',
                                    color: 'white',
                                    textAlign: 'left'
                                    }}
                                    >

                                        <List
                                            itemLayout="vertical"
                                            size="large"
                                            dataSource={this.state.reviews}
                                            renderItem={item => (
                                            <List.Item key={item.id}
                                                    actions={[<IconText type="like-o" 
                                                                        text={item.likes} 
                                                                        theme = {'outlined'}
                                                                        style = {LikeStyle}/>, 
                                                            <IconText type="dislike-o" 
                                                                        text={item.dislikes}
                                                                        theme = {'outlined'}
                                                                        style = {DislikeStyle} />]}
                                                    extra={<div><Rate disabled allowHalf defaultValue={item.rating} /> {item.creation_date} </div>}
                                            >
                                                <List.Item.Meta
                                                    avatar={<Avatar src={item.prof.avatar} />}
                                                    title={item.title}
                                                    description={<a href={'/profile/'+item.prof.pk}>{item.prof.first_name + " " + item.prof.last_name}</a>}
                                                    
                                                />
                                                <div>{item.content}</div>
                                            </List.Item>
                                            )}
                                        >

                                        </List>

                                    </Card>
                                </Col>

                                <Col span={12} style={{ marginBottom: 16 }} type="flex" justify="right">
                                    <Card 
                                    style={gridStyle} 
                                    title="Authors"
                                    headStyle={{
                                    fontSize: 20,
                                    fontStyle: 'italic',
                                    fontFamily: 'Georgia', 
                                    background: '#020037',
                                    color: 'white',
                                    textAlign: 'left'
                                    }}
                                    >

                                    </Card>
                                </Col>

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