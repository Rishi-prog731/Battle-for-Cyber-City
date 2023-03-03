const path = require("path");
const supertest = require("supertest");
const server = require("../server");

const requestWithSupertest = supertest(server);

beforeAll(() => {});

describe("Test Suite", () => {
  it.todo("Tests ⚒️");
});

afterAll(() => {});
