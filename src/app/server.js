const bodyParser = require("body-parser");
const path = require("path");

const express = require("express");
const app = express();

// public
app.use(express.static(path.join(__dirname, "public")));

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

// parse application/json
app.use(bodyParser.json());

// Routes
const main = require("./routes/main");
app.use("/", main);

const api = require("./routes/api");
app.use("/api", api);

module.exports = app;
