const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("style_test", { title: "Style Test" });
});

router.get("/hacker", (req, res) => {
  res.render("hacker", { title: "Hacker" });
});

router.get("/defender", (req, res) => {
  res.render("defender", { title: "Defender" });
});

module.exports = router;
