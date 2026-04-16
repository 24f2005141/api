from flask import Flask, jsonify
import os

app = Flask(__name__)

# Root route (so you stop getting 404 and questioning your life)
@app.route('/')
def home():
    return "API is live"

# Your actual endpoint
@app.route('/api/fetch_api', methods=['GET'])
def get_string():
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

# Important part for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)