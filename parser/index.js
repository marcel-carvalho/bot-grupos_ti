const fs = require('fs');
const path = require('path');
const {load} = require('cheerio');

const RAW_DATA = path.join(__dirname, 'raw/tg.html');
const OUTPUT = path.join(__dirname, 'output/entries.json');

function getEntries(html) {
  const $ = load(html);
  const entries = $('.im_message_text').map((i, el) => {
    return $(el).text();
  }).get()
  console.log(`${entries.length} grupos/canais encontrados`);
  return JSON.stringify(entries);
}

function parse(path) {
  fs.readFile(path, 'utf-8', (err, data) => {
    if (err) return console.log(err);
    fs.writeFile(OUTPUT, getEntries(data), (err) => {
      if (err) return console.log(err);
      console.log('Salvo em:', OUTPUT);
    });
  })
}

parse(RAW_DATA);
