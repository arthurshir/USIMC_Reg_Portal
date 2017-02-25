import React from 'react';
// import ReactDOM from 'react-dom';
// import { Provider } from 'react-redux';
// import { Router, Route, IndexRoute, browserHistory } from 'react-router';
// import HomePage from './components/pages/HomePage.js';


// const App = ({ }) => (
//   // <Router history={browserHistory}>
//     // <Route path="/" component={HomePage} />
//     // <Route onEnter={checkAuth}>
//     //   <Route path="/login" component={LoginPage} />
//     //   <Route path="/register" component={RegisterPage} />
//     //   <Route path="/dashboard" component={Dashboard} />
//     // </Route>
//     // <Route path="*" component={NotFound} />
//   // </Router>
//       <div>
//       <section className="text-section">
//         <h1>Hello welcome to Home Page</h1>
//       </section>
//     </div>
// )

class App extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// Todo.propTypes = {
//   onClick: PropTypes.func.isRequired,
//   completed: PropTypes.bool.isRequired,
//   text: PropTypes.string.isRequired
// }

export default App;
