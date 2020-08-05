const charLength = require('../src/01.js');

const text = "Sonasa Rinusantoro";
test(`Panjang Karakter dari Teks: ${text}`, () => {
  expect(charLength(text)).toBe(text.length);
});