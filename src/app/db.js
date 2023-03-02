const path = require("path");
const fs = require("fs");

const sqlite3 = require("sqlite3").verbose();
const sqlite = require("sqlite");

let database;
const setupDb = async () => {
  sqlite.open({
    filename: path.join("database.db"),
    driver: sqlite3.Database,
  });
};

module.exports = {
  database,
  setupDb,
};
