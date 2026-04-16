from flask import Flask

app = Flask(__name__)

@app.route('/api/fetch_api')
def get_string():
    return '''import React, { useState, useEffect } from "react";

function App() {

  const [query, setQuery] = useState("");
  const [users, setUsers] = useState([]);

  useEffect(() => {

    if (query === "") return; // avoid empty search

    fetch(`https://api.github.com/search/users?q=${query}`)
      .then(res => res.json())
      .then(data => setUsers(data.items || []));

  }, [query]); // runs whenever query changes

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

export default App;'''

if __name__ == '__main__':
    app.run(debug=True)