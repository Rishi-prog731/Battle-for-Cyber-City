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

  await hackerAbility.createTable();
  await hackerEvent.createTable();
  await defenderAbility.createTable();
  await defenderEvent.createTable();
  await matchup.createTable();
  await district.createTable();
};

// District Table
const district = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS district (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        health INTEGER NOT NULL,
        active_hacker_abilities INTEGER,
        active_defender_abilities INTEGER,
        FOREIGN KEY (active_hacker_abilities) REFERENCES hacker_ability(id),
        FOREIGN KEY (active_defender_abilities) REFERENCES defender_ability(id)
      );`);
  },
};

// Match_Up Table
const matchup = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS matchup (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hacker_id INTEGER NOT NULL,
        defender_id INTEGER NOT NULL,
        FOREIGN KEY (hacker_id) REFERENCES hacker(id),
        FOREIGN KEY (defender_id) REFERENCES defender(id)
      );`);
  },
};

// Hacker - Ability Table
const hackerAbility = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS hacker_ability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        value INTEGER NOT NULL
      );`);
  },
};

// Hacker - Event Table
const hackerEvent = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS hacker_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        extra_ability_count INTEGER NOT NULL
      );`);
  },
};

// Defender - Ability Table
const defenderAbility = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS defender_ability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        value INTEGER NOT NULL
      );`);
  },
};

// Defender - Event Table
const defenderEvent = {
  createTable: async () => {
    database.run(`
      CREATE TABLE IF NOT EXISTS defender_event (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        extra_ability_count INTEGER NOT NULL
      );`);
  },
};

module.exports = {
  database,
  setupDb,

  matchup,
  district,
  hackerAbility,
  hackerEvent,
  defenderAbility,
  defenderEvent,
};
