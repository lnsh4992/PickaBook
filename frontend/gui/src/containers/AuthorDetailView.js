import React from 'react';
import axios from 'axios';
import { Card, Row, Col, List, Icon, Avatar, Spin } from "antd";

const gridStyle = {
    textAlign: 'center',
  };

class AuthorDetail extends React.Component {

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
            books: [],
            following: false,
            iconType: "user-add"
        };

        this.style={marginLeft: 10, color: '#daa520'}
    }  

    componentDidMount = () => {
        const authID = this.props.match.params.authID;
        this._isMounted=true;
        axios.get(`http://127.0.0.1:8000/authors/${authID}`).then(res => {
          this.setState({
            // book: res.data
            title: res.data.name,
            birthdate: res.data.birthdate,
            numFollowers: res.data.numFollowers,
            image_url: res.data.image_url,
            genre: this.state[res.data.genre],
            rating: res.data.review,
            number_of_reviews: res.data.review_count,
            synopsis: res.data.bio
          });

          axios.get(`http://127.0.0.1:8000/library/authorbooks/${res.data.name}`).then(ares => {
              this.setState({
                  books: ares.data
              });
          })
          .catch(error => console.log(error));
        })
        .catch(error => console.log(error));
    }  

    componentWillUnmount(){
        this._isMounted = false;
        console.log("Unmounting");
    }

    handleFollow = () => {
        const profID = localStorage.getItem("profID");
        const authID = this.props.match.params.authID;
        axios.put(`http://127.0.0.1:8000/profile/addfollow/${profID}`, {
            following: [authID]
        })
        .then(res => {
            this.style = {
                marginLeft: 10,
                color: !this.state.following ? "#b22222": '#daa520'
            }
            this.setState({
                iconType: !this.state.following ? "user-delete" : "user-add" ,
                following: !this.state.following
            });
            

        })
        .catch(error => console.log(error));


    }

    render() {
        return (
                <div>
                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={6}>
                            <Card bodyStyle={{
                                padding: 0
                            }}>
                                <img src={this.state.image_url} 
                                style={{
                                    width: 302, height: 295
                                }}
                                width="100%" height="100%" >
                                </img>
                            </Card>
                        </Col>
                        
                        <Col span={16}>
                            <Card title={
                                    <div>
                                        {this.state.title} 
                                        <Icon style={this.style} type={this.state.iconType}
                                            onClick={this.handleFollow} />
                                    </div>
                                }
                                
                                headStyle={{
                                    fontSize: 20,
                                    fontStyle: 'italic',
                                    fontFamily: 'Georgia', 
                                    background: '#378695'
                                }}
                            >
                                <p>
                                    <b><i>Birthdate: </i></b> 
                                    {this.state.birthdate}
                                </p>
                                
                                <p>
                                    <b><i>Number of Followers: </i></b> 
                                    {this.state.numFollowers}
                                </p>
                                
                                <p>
                                    <b><i>Genre: </i></b>
                                    {this.state.genre}
                                </p>

                                <p>
                                    <b><i>Rating: </i></b>
                                    {this.state.rating}
                                </p>

                                <p>
                                    <b><i>Number of reviews: </i></b>
                                    {this.state.number_of_reviews}
                                </p>
                            </Card>
                        </Col>

                    </Row>

                    <Row gutter={20} style={{ marginBottom: 16 }} type="flex" justify="center">
                        <Col span={22}>
                            <Card style={gridStyle} title="Synopsis/blurb"
                            headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia', 
                                background: '#378695'
                            }}
                            >
                                <p>
                                    {this.state.synopsis}
                                </p>
                            </Card>
                        </Col>
                    </Row>

                    <List
                        grid={{ gutter: 16, column: 4 }}
                        style={{
                            paddingTop: 20, paddingLeft: 55  
                        }}
                        dataSource={this.state.books}
                        renderItem={item => (
                        <List.Item>


                            <Card
                                hoverable
                                style={{ width: 240 }}
                                cover={<img alt={item.title} 
                                            src={item.image_url} 
                                            style={{
                                                width: 238, height: 295
                                            }}
                                            width="100%" height="100%"
                                />}
                            >
                                <Card.Meta
                                title={<a href={'/booklist/'+item.pk}><b>{item.title}</b></a>}
                                
                                />
                            </Card>
                        </List.Item>
                        )}
                    />

                </div>
        )
    }
}

class Title extends React.Component {
    render() {
        return (
            <h2>
                Title
            </h2>
        );
    }
}

export default AuthorDetail;