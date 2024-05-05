import express from "express";
import router from "./routes/start.js";
import cors from "cors";
import bodyParser from "body-parser";
import ip from "ip";

let lastHouseVisited;
const app = express();
const port = 3000;

app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(router);

app.get("/", (req, res) => {
  res.json({ message: lastHouseVisited });
});

app.post("/", (req, res) => {
  lastHouseVisited = req.body.house;
  res.json({ message: lastHouseVisited });
});

app.listen(port, () => {
  console.log(
    `Example app listening on port ${port}, and with IP ${ip.address()}`
  );
});

// /users en GET = liste d'utilisateurS
// /users en POST = ajouter un utilisateur (body accessible) => .push
// /users/:id en GET = afficher un utilisateur // .find
// /users/:id en PUT = modifier un utilisateur (body accessible) // .find et =
// /users/:id en DELETE = supprimer un utilisateur // .find et .splice
