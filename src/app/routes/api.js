const express = require("express");
var bodyParser = require("body-parser");
const router = express.Router();

const db = require("../db");

router.get("/", (req, res) => {
  res.send("Hello World!");
});

router.post("/", (req, res) => {
  res.send("Hello World!");
});

router.post("/login", (req, res) => {
  console.log(req.body);
  res.send(req.body);
  //res.redirect("/game");
});

module.exports = router;
