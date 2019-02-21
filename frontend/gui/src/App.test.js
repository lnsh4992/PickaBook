const axios  = require('axios');
/*
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { mount } from 'enzyme';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

*/
test('Fake Test', () => {
    expect(true).toBeTruthy();
})

test('Fetch Book by name', () => {
  expect.assertions(1);
  return axios.get('http://127.0.0.1:8000/library/view/Tailspin')
  .then(res => {
      expect(res.data.title).toEqual('Tailspin');
//      console.log(res.data);
  })
  .catch(err => console.log(err));
});

test('Fetch Author by name', () => {
  expect.assertions(1);
  return axios.get('http://127.0.0.1:8000/authors/view/Jordan')
  .then(res => {
      expect(res.data.name).toEqual('Jordan');
//      console.log(res.data);
  })
  .catch(err => console.log(err));
});

test('Books By Author', () => {
  expect.assertions(1);

  return axios.get(`http://127.0.0.1:8000/library/authorbooks/Jordan`)
      .then(res2 => {
//        console.log(res2.data[0]);
        expect('Test book 1').toBe(res2.data[0].title);
      })
      .catch(error => console.log(error));
});

test('Profile From User', () => {
  expect.assertions(1);
  return axios.get(`http://127.0.0.1:8000/profile/8`).then(res => {
            expect(res.data.first_name).toBe('CS491');
        });
});

test('Reviews of book', () => {
  expect.assertions(2);
  return axios.get(`http://127.0.0.1:8000/bookreview/1`).then(res => {
          expect(res.data.length).toBeGreaterThan(0);
          expect(res.data[0].title).toBe("Good stuff");
  })
})

test('Questions of Book', () => {
  expect.assertions(1);
  return axios.get(`http://127.0.0.1:8000/qanswer/question/1`).then(res => {
          expect(res.data.length).toBeGreaterThan(0);
  });
});



/*
describe('Indicator', () => {
  describe('when loading is false', () => {
    it('should render children', () =>{
      const wrapper = mount(
        <App isLoading={false}>
        <div>Indicator Test</div>
        </App>
      );
      expect(wrapper.html()).toEqual('<div>Indicator Test</div>');
      wrapper.unmount();
    });
  });

});
*/
