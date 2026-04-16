from flask import Flask, jsonify
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Root route (so you stop getting 404 and questioning your life)
@app.route('/')
def home():
    return "API is live"

# Your actual endpoint
@app.route('/api/fetch_api', methods=['GET'])
def get_fetch_api_code():
    return jsonify({
        "code": """import React, { useState, useEffect } from "react";

function App() {

  const [query, setQuery] = useState("");
  const [users, setUsers] = useState([]);

  useEffect(() => {

    if (query === "") return;

    fetch(`https://api.github.com/search/users?q=${query}`)
      .then(res => res.json())
      .then(data => setUsers(data.items || []));

  }, [query]);

  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <h1>GitHub User Search</h1>

      <input
        type="text"
        placeholder="Search GitHub users..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: "10px", width: "250px" }}
      />

      <div style={{ marginTop: "20px" }}>
        {users.map(user => (
          <div key={user.id}>
            <img src={user.avatar_url} width="50" alt="" />
            <p>{user.login}</p>
          </div>
        ))}
      </div>

    </div>
  );
}

export default App;"""
    })

@app.route('/api/form', methods=['GET'])
def get_form_string():
    return jsonify({
        "code": """import React, { useState } from "react";

function App() {

  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const validate = () => {
    let newErrors = {};

    // Email validation
    if (!form.email.includes("@")) {
      newErrors.email = "Invalid email";
    }

    // Password validation
    if (form.password.length < 6) {
      newErrors.password = "Password must be at least 6 characters";
    }

    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const validationErrors = validate();
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length === 0) {
      alert("Login Successful");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Login Form</h1>

      <form onSubmit={handleSubmit}>

        <div>
          <input
            type="text"
            name="email"
            placeholder="Enter Email"
            value={form.email}
            onChange={handleChange}
          />
          <p style={{ color: "red" }}>{errors.email}</p>
        </div>

        <div>
          <input
            type="password"
            name="password"
            placeholder="Enter Password"
            value={form.password}
            onChange={handleChange}
          />
          <p style={{ color: "red" }}>{errors.password}</p>
        </div>

        <button type="submit">Login</button>

      </form>
    </div>
  );
}

export default App;"""
    })


def get_for_route():
    return jsonify({
        "code": """import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}

function Contact() {
  return <h1>Contact Page</h1>;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;"""
    })
