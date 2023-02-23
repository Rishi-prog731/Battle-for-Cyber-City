const express = require("express");
const router = express.Router();

const db = require("../db");

router.get("/", (req, res) => {
  db.all("SELECT * FROM lorem", (err, rows) => {
    res.json(rows);
  });
});

router.post("/", (req, res) => {
  res.send("Hello World!");
});

module.exports = router;
