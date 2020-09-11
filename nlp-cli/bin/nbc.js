#!/usr/bin/env node

const yargs = require("yargs");
const axios = require("axios");

// Définitions des paramètres de la commande
const options = yargs
 .usage("Usage: -t <name>")
 .option("t", { alias: "text", describe: "Input text", type: "string", demandOption: true })
 .argv;

// Constructition des données de la requête
const data = {'text': options.text};

// Définition de l'url cible.
const url = 'http://127.0.0.1:5000/nb-characters/';

// Envoie de la requête et affichage du résultat.
axios.post(url, data)
  .then(res => console.log(res.data['output']));