import React from 'react';
import axios from 'axios';
import { Card, Row, Col } from "antd";
import { connect } from "react-redux";

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
                avatar: res.data.avatar
            });
            localStorage.setItem("profID", res.data.pk);
            console.log(localStorage.getItem("profID"));

        })
    }

    render() {
        return (
                <div>
                    <Row gutter={20} type="flex" justify="center">
                        <Col span={6}>
                            <Card bodyStyle={{
                                padding: 0
                            }}>
                                <img src={this.state.avatar} style={{    
                                }}
                                width="100%" height="100%" >
                                </img>
                            </Card>
                        </Col>
                        
                        <Col span={16}>
                            <Card title={this.state.first_name + this.state.last_name} headStyle={{
                                fontSize: 20,
                                fontStyle: 'italic',
                                fontFamily: 'Georgia'
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

                    <Row gutter={20} type="flex" justify="center">
                        <Col span={22}>
                            <Card style={gridStyle} title="About Me">
                                <p>
                                    {this.state.bio}
                                </p>
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