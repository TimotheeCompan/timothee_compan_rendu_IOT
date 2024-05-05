import express from "express";
import UsersController from "../controllers/UsersController.js";
import authentificationController from "../controllers/authentificationController.js";
import authentificationMiddleware from "../middlewares/authentificationMiddleware.js";

const router = express.Router();

router.get("/users", UsersController.index);
router.post("/users", UsersController.store);
router.get("/users/:id", UsersController.show);
router.put("/users/:id", UsersController.update);
router.delete("/users/:id", UsersController.destroy);
router.get("/getMyProfile",authentificationMiddleware.authentification,UsersController.getMyProfile);
router.post("/login", authentificationController.login);

export default router;
