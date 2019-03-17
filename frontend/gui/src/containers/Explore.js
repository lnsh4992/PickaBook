import React from 'react';
import Books from '../components/Book';
import axios from 'axios';
import {List, Card, Row, Rate} from 'antd';
import ReactCardFlip from 'react-card-flip';

class Explore extends React.Component {
    
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
            isFlipped: false
        };
    }

    handleClick = (item) => {
        item.isFlipped = !item.isFlipped;
        this.setState(prevState => ({ isFlipped: !prevState.isFlipped}));
    }

    componentDidMount = () => {
        axios.get("http://127.0.0.1:8000/library/booklist/").then(res => {
            this.setState({
                books: res.data
            });
            for(var i=0; i<this.state.books.length; ++i){
                this.state.books[i].isFlipped = false
            }
        })
        .catch(error => console.log(error));
    }
    
    render() {
        return (

                <List
                grid={{
                    gutter: 16, column: 4
                }}
                pagination={{
                onChange: (page) => {
                    console.log(page);
                },
                pageSize: 12,
                }}
                dataSource={this.state.books}
                
                renderItem={item => (
                    <List.Item style={{height: 450}}>
                        <ReactCardFlip isFlipped={item.isFlipped} flipDirection="horizontal">
                        <Card
                            hoverable
                            style={{ width: 240 }}
                            cover={<img alt={item.title} src={item.image_url} />}
                            onClick={() => this.handleClick(item)}
                            key="front"
                        >
                            <Card.Meta
                            title={<a href={'/booklist/'+item.pk}><b>{item.title }</b></a>}
                            />
                        </Card>

                        <Card
                            title={<a href={'/booklist/'+item.pk}><b>{item.title }</b></a>}
                            style={{width: 240}}
                            key="back"
                            onClick={() => this.handleClick(item)}
                        >
                            <p>Date: {item.publication_date}</p>
                            <p>Genre: {this.state[item.genre]}</p>
                            <p>Rating: <Rate disabled allowHalf defaultValue={item.rating} /></p>
                            <p>Reviews: {item.number_of_reviews}</p>
                        </Card>
                        </ReactCardFlip>
                    </List.Item>
                )}
            />

        )
    }
}

export default Explore;