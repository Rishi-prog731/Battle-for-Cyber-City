const express = require("express");
const router = express.Router();

const db = require("../db");
db.init();

router.post("/login", (req, res) => {
  db.table_users_insert(req.body.username, req.body.email);

  res.send(req.body);
});

module.exports = router;
