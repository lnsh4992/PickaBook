import React from 'react';
import { Button, Input} from 'antd';
class Register extends React.Component {
  state = {
    username: '',
    email: '',
    password: '',
  }

  onChange = (e) => {
    if (e.target.name === 'isAdmin') {
      this.setState({
        [e.target.name]: e.target.checked,
      });
    } else {
      this.setState({
        [e.target.name]: e.target.value,
      });
    }
  }

  onSubmit = async () => {
    const response = await this.props.mutate({
      variables: this.state,
    });
    console.log(response);
  }

  render() {
    return (
      <div>
        <Input
          name='username'
          placeholder='Your Name'
          onChange={e => this.onChange(e)}
          value={this.state.username} />
        <br />
        <Button onClick={() => this.onSubmit()} type="primary">Register</Button>
      </div>
    );
  }
}
/*
const mutation = gql`
mutation($username: String!, $email: String!, $password: String!, $isAdmin: Boolean) {
	register(username: $username, email: $email, password: $password, isAdmin: $isAdmin) {
	  id
	}
}
`;
*/

export default graphql(mutation)(Register);
