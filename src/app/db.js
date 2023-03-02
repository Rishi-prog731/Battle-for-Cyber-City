const path = require("path");
const fs = require("fs");

// Main databases
const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

let database;
const setupDb = async () => {
  sqlite.open({
    filename: path.join("database.db"),
    driver: sqlite3.Database,
  });
};

// District Table

// Match_Up Table

// Hacker - Ability Table

// Hacker - Event Table

// Defender - Ability Table

// Defender - Event Table

module.exports = {
  database,
  setupDb,
};
