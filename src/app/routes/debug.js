const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("debug", { title: "Cyber City - debug" });
});

module.exports = router;
