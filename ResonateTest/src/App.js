import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from "react-router-dom";
 

import Header from "./components/header"
import Q1 from "./pages/basic"
import Q2 from "./pages/Q2";
import Q3 from "./pages/Q3";
function App() {
  return (
    
    <Router>
      <Header />
      <Route exact path="/" component={Q1} />
      <Route path="/q2" component={Q2} />
      <Route path="/q3" component={Q3} />
      {/* <Route path="/q4" component={Q4} /> */}
    </Router>
  );
}

export default App;
