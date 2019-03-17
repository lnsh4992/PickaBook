import React from 'react';
import Books from '../components/Book';
import axios from 'axios';
import {List, Card, Row, Rate, Layout, Menu} from 'antd';
import ReactCardFlip from 'react-card-flip';

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

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

    handleChange = (event) => {
        var obj = [...this.state.books];

        switch(event){
            case 'title': 
                obj.sort((a, b) => a.title.localeCompare(b.title));
                break;
            case 'rating':
                obj.sort((a, b) => b.rating - a.rating);
                break;
            case 'publication_date':
                obj.sort((a, b) => b.publication_date.localeCompare(a.publication_date));
                break;
        }

        this.setState({books: obj});
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
            <Layout style={{ padding: '0 0', background: '#fff'}}>
                <Sider width={200} >
                    <Menu
                        mode="inline"
                        theme="dark"
                        defaultSelectedKeys={[3]}
                        style={{ height: '100%' }}
                    >
                        <Menu.Item key="1" onClick={()=> this.handleChange('publication_date')}>Newest Collection</Menu.Item>
                        <Menu.Item key="2" onClick={() => this.handleChange('rating')}>Top Rated</Menu.Item>
                        <Menu.Item key="3" onClick={() => this.handleChange('title')}>Title</Menu.Item>
                        <SubMenu key="genre" title='Genre'>
                        <Menu.Item key="FA">Fantasy</Menu.Item>
                        <Menu.Item key="NF">Non Fiction</Menu.Item>
                        <Menu.Item key="RO">Romance</Menu.Item>
                        <Menu.Item key="TH">Thriller</Menu.Item>
                        <Menu.Item key="MY">Mystery</Menu.Item>
                        <Menu.Item key="BI">Biography</Menu.Item>
                        <Menu.Item key="FI">Fiction</Menu.Item>
                        <Menu.Item key="SF">Science Fiction</Menu.Item>
                        </SubMenu>
                    </Menu>
                </Sider>

                <Content>
                    
                <List
                grid={{
                    gutter: 16, column: 3
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
                            <p>Rating: <Rate disabled allowHalf value={item.rating} /></p>
                            <p>Reviews: {item.number_of_reviews}</p>
                        </Card>
                        </ReactCardFlip>
                    </List.Item>
                )}
            />

                </Content>
            </Layout>


        )
    }
}

export default Explore;