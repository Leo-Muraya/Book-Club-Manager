import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import MyClubs from "./pages/MyClubs";
import ClubPage from "./pages/ClubPage";

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/clubs" element={<MyClubs />} />
        <Route path="/clubs/:id" element={<ClubPage />} />
      </Routes>
    </Router>
  );
};

export default App;
