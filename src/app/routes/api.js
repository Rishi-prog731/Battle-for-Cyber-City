const express = require("express");
const router = express.Router();

const db = require("../db");

router.get("/", (req, res) => {
  res.send("Hello World!");
});

router.post("/", (req, res) => {
  res.send("Hello World!");
});

module.exports = router;
