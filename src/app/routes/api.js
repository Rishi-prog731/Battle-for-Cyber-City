const express = require("express");
const router = express.Router();

const db = require("../db");
db.init();

router.post("/login", (req, res) => {
  console.log(req.body);
  db.userDatabase_add(req.body.username, req.body.email, req.body.game_token);
  res.send(req.body);
  //res.redirect("/game");
});

module.exports = router;
