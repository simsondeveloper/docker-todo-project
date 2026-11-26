const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
const PORT = 3000;

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

// EJS configuration
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Flask backend URL
const FLASK_API = process.env.FLASK_API || "http://localhost:5000";

// Home page
app.get("/", (req, res) => {
  res.render("index", { message: null, error: null });
});

// Submit To-Do item
app.post("/submittodoitem", async (req, res) => {
  try {
    const { itemName, itemDescription } = req.body;

    const response = await axios.post(`${FLASK_API}/submittodoitem`, {
      itemName,
      itemDescription,
    });

    res.render("index", {
      message: response.data.message,
      error: null,
    });
  } catch (error) {
    console.error("Backend error:", error.message);

    res.status(502).render("index", {
      message: null,
      error: "Unable to connect to Flask backend.",
    });
  }
});

// Start server
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Frontend running on port ${PORT}`);
});
