#!/usr/bin/env Node
require("dotenv").config();
const http = require("http");

const game = require("./app/game").test();

const hostname = process.env.hostname,
  port = process.env.port;

const app = require("./app/server");
app.set("port", port);

const server = http.createServer(app);

server.on("connection", (socket) => {});

server.listen(port, hostname, () => {
  console.log(`server running at http://${hostname}:${port}/`);
});

const WebSocketServer = require("ws").Server;
const wss = new WebSocketServer({ server: server });

wss.on("connection", (ws) => {
  console.log("Client connected");
  ws.on("close", () => console.log("Client disconnected"));
  ws.on("message", (message) => {
    console.log("received: %s", message);
    ws.send(message);
  });
});
