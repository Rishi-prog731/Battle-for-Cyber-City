const express = require("express");
const api = express.Router();

const db = require("../db");

const hacker = express.Router();
const defender = express.Router();

hacker.get("/ability/", async (req, res) => {
  const abilities = await db.hackerAbility.getAll();
  res.json(abilities);
});

hacker.get("/ability/:id", async (req, res) => {
  const ability = await db.hackerAbility.get(req.params.id);
  res.json(ability);
});

hacker.post("/ability", async (req, res) => {
  const { name, description, value } = req.body;
  await db.hackerAbility.insertAbility(name, description, value);
  res.json({ success: true });
});

hacker.delete("/ability", async (req, res) => {
  await db.hackerAbility.clear();
  res.json({ success: true });
});

hacker.delete("/ability/:id", async (req, res) => {
  await db.hackerAbility.remove(req.params.id);
  res.json({ success: true });
});

api.use("/hacker", hacker);
api.use("/defender", defender);

module.exports = api;
