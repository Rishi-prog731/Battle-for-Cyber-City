const express = require("express");
const router = express.Router();

router.get("/", (req, res) => {
  res.render("client", { title: "Cyber City - game" });
});

module.exports = router;
