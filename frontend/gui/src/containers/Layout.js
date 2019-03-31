import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';
import CustomHeader from './Header';

const { Header, Content, Footer } = Layout;

class CustomLayout extends React.Component {
  render() {
    console.log(this.props);
      return (
        <Layout className="layout">
        
        <CustomHeader history={this.props.history} isAuthenticated={this.props.isAuthenticated}/>
{/*
        <Header>
          <div className="logo" />
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={['2']}
            style={{ lineHeight: '64px' }}
          >

          {
              this.props.isAuthenticated ?

              <Menu.Item key="2" onClick={this.props.logout}>
                Logout
              </Menu.Item>

              :
            
              <Menu.Item key="2">
                <Link to="/login">Login</Link>
              </Menu.Item>
          }
            <Menu.Item key="1">
                <Link to="/">Home</Link>
            </Menu.Item>
          </Menu>
        </Header>
*/}
        
        <Content style={{ padding: '0 50px', background: '#378695'}}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>Home</Breadcrumb.Item>
            <Breadcrumb.Item>List</Breadcrumb.Item>
            <Breadcrumb.Item>App</Breadcrumb.Item>
          </Breadcrumb>
          
          <div style={{ background: '#DDA72F' , padding: 24, minHeight: 280 }}>
            {this.props.children}
          </div>

        </Content>
        
        <Footer style={{ textAlign: 'center', background: '#414141', color: 'white'}}>
          PickaBook: a CS 307 Project | Created by Myeongsu Kim, Logesh Roshan, Piyush Juneja, Shobhit Makhija
        </Footer>
      
      </Layout>
    );
  }
    
}

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(actions.logout())
  }
}

export default withRouter(connect(null, mapDispatchToProps)( CustomLayout));
