const path = require("path");
const fs = require("fs");

// Main databases
const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

var database;
const setupDb = async () => {
  database = await sqlite.open({
    filename: path.join("database.db"),
    driver: sqlite3.Database,
  });
};

module.exports = {
  database,
  setupDb,
};
