const path = require("path");
const supertest = require("supertest");
const server = require("../server");

const requestWithSupertest = supertest(server);

beforeAll(() => {});

describe("Test Suite", () => {
  it("GET /", async () => {
    const response = await requestWithSupertest.get("/");
    expect(response.status).toBe(200);
  });
});

afterAll(() => {});
