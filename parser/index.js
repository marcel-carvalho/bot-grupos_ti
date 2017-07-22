const fs = require('fs');
const path = require('path');
const {load} = require('cheerio');

const RAW_DATA = path.join(__dirname, 'raw/tg.html');
const OUTPUT = path.join(__dirname, 'output/entries.json');

function getEntries(html) {
  const $ = load(html);
  const entries = $('.im_message_text, .im_message_photo_caption').map((i, el) => {
    let tags = $(el).find('[href^="tg://search_hashtag"]').text();
    let desc = $(el).clone().children('[href^="tg://search_hashtag"]').remove().end().find('br').replaceWith(' ').end().text().trim().replace(/^-\s/, '').replace(/\s\s+/g, ' ');
    let link = $(el).find('[href^="tg://join"],[href^="tg://resolve"],[href^="https://www.telegram.me/"]').text();
    return {tags, desc, link};
  }).get()
  const filtered = entries.filter(item => {
    return (item.tags.length && item.link.length && !item.tags.match(/Evento|Palestra/g))
  })
  console.log(`${filtered.length} grupos/canais encontrados`);
  return JSON.stringify(filtered, null, '  ');
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
