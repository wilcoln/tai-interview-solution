#!/usr/bin/env node

const yargs = require("yargs");
const axios = require("axios");

const options = yargs
 .usage("Usage: -t <name>")
 .option("t", { alias: "text", describe: "Input text", type: "string", demandOption: true })
 .argv;

const data = {'text': options.text};

const url = 'http://127.0.0.1:5000/nb-words/';

axios.post(url, data)
  .then(res => console.log(res.data['output']));