import React from 'react';
import { List, Icon, Comment, Avatar, Tooltip } from 'antd';
import axios from 'axios';

class QAnswer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            questions: [],
            likes: 0,
            dislikes: 0,
            action: null,
            img: null
        };
    }  


    componentDidMount = () => {
        const bookID = this.props.bookID; //match.params.bookID;
        axios.get(`http://127.0.0.1:8000/qanswer/question/${bookID}`).then(res => {
            this.setState({
                questions: res.data,
            });
        })
        .catch(error => console.log(error));
    }

    like = () => {
        this.setState({
          likes: 1,
          dislikes: 0,
          action: 'liked',
        });
      }
    
      dislike = () => {
        this.setState({
          likes: 0,
          dislikes: 1,
          action: 'disliked',
        });
      }

    render() {

        const { likes, dislikes, action } = this.state;
        const actions = [
            <span>
              <Tooltip title="Like">
                <Icon
                  type="like"
                  theme={action === 'liked' ? 'filled' : 'outlined'}
                  onClick={this.like}
                />
              </Tooltip>
              <span style={{ paddingLeft: 8, cursor: 'auto' }}>
                {likes}
              </span>
            </span>,
            <span>
              <Tooltip title="Dislike">
                <Icon
                  type="dislike"
                  theme={action === 'disliked' ? 'filled' : 'outlined'}
                  onClick={this.dislike}
                />
              </Tooltip>
              <span style={{ paddingLeft: 8, cursor: 'auto' }}>
                {dislikes}
              </span>
            </span>,
            <span>Reply to</span>,
        ];

        return (
            <div>
                <List
                    className="comment-list"
                    itemLayout="horizontal"
                    dataSource={this.state.questions}
                    renderItem={item => (
                        <Comment
                            actions={actions}
                            author={item.profile}
                            avatar={<Avatar src={item.profile.avatar}/>}
                            content={item.question}
                            datetime={item.creation_date}
                        >
                            {
                                item.answers.length > 0 ?
                                
                                <List
                                className="comment-list"
                                itemLayout="horizontal"
                                dataSource={item.answers}
                                renderItem={answer => (
                                    <Comment
                                        author={answer.profile}
                                        avatar={<Avatar src={answer.profile.avatar}/>}
                                        content={answer.answer}
                                        datetime={answer.creation_date}
                                    />
                                )}
                                />
                                :
                                <b syle={{marginLeft: 200}}>No replies</b>
                            }
                            </Comment>
                        
                    )}
                />
            </div>
        )
    }
}

export default QAnswer;