import React from 'react';
import {BrowserRouter as Router, Route, Link} from "react-router-dom";
import Home from './pages/Home/Home';
import Related from './pages/Related/Related';

function App() {
  return (
    <div className="app__screen">
      <Router>
      <div className="navbar">
        <h1>Finsocial</h1>
        <div>
          <Link to="/">Home</Link>
          <Link to="/related">Related Financial Posts</Link>
        </div>
      </div>
          <Route exact path="/" component={Home} />
          <Route exact path="/related" component={Related} />
      </Router>
    </div>
  );
}

export default App;
