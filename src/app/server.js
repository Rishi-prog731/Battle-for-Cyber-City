const bodyParser = require("body-parser");
const path = require("path");

const express = require("express");
const app = express();

// parse application/json
app.use(bodyParser.json());

// Routes
const main = require("./routes/main");
app.use("/", main);

module.exports = app;
