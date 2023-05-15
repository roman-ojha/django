import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setdata] = useState();
  useEffect(async () => {
    const res = await fetch("http://localhost/apiPage", {
      method: "GET",
    });
    const resData = await res.text();
    setdata(resData);
  }, []);

  return (
    <div className="App">
      <div
        className="Container"
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          width: "100%",
          height: "100vh",
          backgroundColor: "pink",
          flexDirection: "column",
        }}
      >
        <h1>Hello world</h1>
        <br />
        <h1>{data}</h1>
      </div>
    </div>
  );
}

export default App;
