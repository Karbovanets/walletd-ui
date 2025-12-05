import http from "http";
import fetch from "node-fetch";

http.createServer(async (req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    return res.end();
  }

  let body = "";
  req.on("data", d => body += d);
  req.on("end", async () => {
    const r = await fetch("http://127.0.0.1:16000/json_rpc", {
      method: "POST",
      body,
      headers: { "Content-Type": "application/json" }
    });
    const t = await r.text();
    res.end(t);
  });
}).listen(16001);

