#!/usr/bin/env node

const yargs = require("yargs");
const axios = require("axios");

// Définitions des paramètres de la commande
const options = yargs
 .usage("Usage: -t <name>")
 .option("t", { alias: "text", describe: "Input text", type: "string", demandOption: true })
 .option("n", { alias: "nb_keywords", describe: "Number of keywords", type: "integer", demandOption: true })
 .argv;

// Constructition des données de la requête
const data = {
    'text': options.text,
    'nb_keywords': options.nb_keywords,
};

// Définition de l'url cible.
const url = 'http://127.0.0.1:5000/extract-keywords/';

// Envoie de la requête et affichage du résultat.
axios.post(url, data)
  .then(res => console.log(res.data['output']));