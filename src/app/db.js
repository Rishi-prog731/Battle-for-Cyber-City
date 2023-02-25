const path = require("path");
const fs = require("fs");

const DATA_PATH = "./data.json";
const getData = async () => {
  return JSON.parse(fs.readFileSync(DATA_PATH, "utf8"));
};

const db = {
  getData,
};

module.exports = db;
