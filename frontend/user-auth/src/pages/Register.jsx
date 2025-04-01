import React, { useState } from "react";

const Register = () => {
  const [formData, setFormData] = useState({
    email: "",
    name: "",
    password: "",
    password2: "",
    tc: true,  // Terms & Conditions checkbox
  });

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const API_BASE_URL = "http://127.0.0.1:8000/"; // Change this if needed

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const response = await fetch(`${API_BASE_URL}/register/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      console.log("Response:", data);  // Debugging

      if (response.ok) {
        setSuccess("Registration successful!");
      } else {
        setError(data.errors ? JSON.stringify(data.errors) : "Registration failed.");
      }
    } catch (error) {
      console.error("Error:", error);
      setError("Something went wrong. Try again.");
    }
  };

  return (
    <div>
      <h2>Register</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {success && <p style={{ color: "green" }}>{success}</p>}

      <form onSubmit={handleSubmit}>
        <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
        <input type="text" name="name" placeholder="Name" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <input type="password" name="password2" placeholder="Confirm Password" onChange={handleChange} required />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
