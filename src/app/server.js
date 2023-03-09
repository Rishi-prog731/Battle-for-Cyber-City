const path = require("path");

const express = require("express");
const app = express();
const ws = require("express-ws")(app);

// public
app.use(express.static(path.join(__dirname, "public")));

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

const bodyParser = require("body-parser");
app.use(bodyParser.json()); // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

// database
const db = require("./db");
db.setupDb();

// Routes
const api = require("./routes/api");
app.use("/api", api);

const main = require("./routes/main");
app.use("/", main);

// WebSockets
app.ws("/", (ws, req) => {
  console.log("Websocket connected");

  ws.on("message", (msg) => {
    console.log("Websocket message: ", msg);
  });

  ws.on("close", () => {
    console.log("Websocket closed");
  });

  ws.send(
    JSON.stringify({
      mode: "alert",
      message: "Hello from the server!",
    })
  );
});

module.exports = app;
