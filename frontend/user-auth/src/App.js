import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Navbar from "./services/navbar";

function App() {
  return (
    <Router>
      <Navbar />

      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

      </Routes>
    </Router>
  );
}

export default App;
