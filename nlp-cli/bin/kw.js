#!/usr/bin/env node

const yargs = require("yargs");
const axios = require("axios");

const options = yargs
 .usage("Usage: -t <name>")
 .option("t", { alias: "text", describe: "Input text", type: "string", demandOption: true })
 .option("n", { alias: "nb_keywords", describe: "Number of keywords", type: "integer", demandOption: true })
 .argv;

const data = {
    'text': options.text,
    'nb_keywords': options.nb_keywords,
};

const url = 'http://127.0.0.1:5000/extract-keywords/';

axios.post(url, data)
  .then(res => console.log(res.data['output']));