const db = require("./db");

const playerType = {
  hacker: 0,
  city: 1,
};

class Event {
  constructor(name, description, playerType, modifier) {
    this.name = name;
    this.description = description;
    this.playerType = playerType;
    this.modifier = modifier;
  }
}

class District {
  constructor(name) {
    this.name = name;
  }
}

class Ability {
  constructor(name, description) {
    this.name = name;
    this.description = description;
  }
}

class HackerAbility extends Ability {}

class CityAbility extends Ability {}

function test() {
  
}

module.exports = {
  District,
  Ability,
  HackerAbility,
  CityAbility,
  test,
};
