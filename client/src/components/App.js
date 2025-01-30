import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navbar from "./Navbar";
import Home from "../pages/Home";
import ClubPage from "../pages/ClubPage";
import MyClubs from "../pages/MyClubs";
import LoginForm from "./Forms/LoginForm";
import RegistrationForm from "./Forms/RegistrationForm";

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" element={<Home />} />
        <Route path="/clubs/:id" element={<ClubPage />} />
        <Route path="/my-clubs" element={<MyClubs />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/register" element={<RegistrationForm />} />
      </Switch>
    </Router>
  );
}

export default App;