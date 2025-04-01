import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check if an access token exists
    const token = localStorage.getItem("access_token");
    setIsLoggedIn(!!token);
  }, []);

  const handleLogout = () => {
    // Clear tokens from localStorage
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    
    setIsLoggedIn(false);
    navigate("/login"); // Redirect to login page
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <a className="navbar-brand" href="/">MyApp</a>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ml-auto">
            {isLoggedIn ? (
              <li className="nav-item">
                <button className="btn btn-danger" onClick={handleLogout}>Logout</button>
              </li>
            ) : (
              <li className="nav-item">
                <button className="btn btn-primary" onClick={() => navigate("/login")}>Login</button>
              </li>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
