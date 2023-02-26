const path = require("path");

const express = require("express");
const app = express();

// public
app.use(express.static(path.join(__dirname, "public")));

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

const bodyParser = require("body-parser");
app.use(bodyParser.json()); // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({ extended: true }));

// Routes
const main = require("./routes/main");
app.use("/", main);

const game = require("./routes/game");
app.use("/game", game);

const api = require("./routes/api");
app.use("/api", api);

module.exports = app;
