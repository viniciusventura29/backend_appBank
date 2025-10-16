const express = require("express");
const bodyParser = require("body-parser");
const { exec } = require("child_process");
const fs = require("fs");

const app = express();
app.use(bodyParser.json());

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  next();
});

app.post("/eval", (req, res) => {
  const code = req.body.code;
  try {
    const result = eval(code);
    res.send({ ok: true, result });
  } catch (e) {
    res.status(400).send({ ok: false, error: e.message });
  }
});

app.post("/user", (req, res) => {
  const username = req.body.username;
  // suponha que `db.query` executa a string diretamente
  const sql = "SELECT * FROM users WHERE username = '" + username + "'";
  fakeDbQuery(sql); // função fictícia só para exemplo
  res.send({ ok: true, sql });
});

// *4* - Execução de comando com input do usuário (command injection)
app.post("/run", (req, res) => {
  const cmd = req.body.cmd;
  exec(cmd, (err, stdout) => {
    if (err) return res.status(500).send(err.message);
    res.send({ out: stdout });
  });
});

// *5* - Grava arquivo usando nome fornecido pelo usuário (path traversal)
app.post("/save", (req, res) => {
  const filename = req.body.filename || "out.txt";
  const content = req.body.content || "";
  fs.writeFileSync("/tmp/" + filename, content); // permite "../" no filename
  res.send({ ok: true });
});

function fakeDbQuery(q) {
  console.log("[FAKE DB QUERY]", q);
}

app.listen(3000, () => console.log("Servidor vulnerável rodando na :3000"));
