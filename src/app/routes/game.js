const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("game", { title: "Cyber City - game" });
});

module.exports = router;
