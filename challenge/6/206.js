let r = /1\d2\d3\d4\d5\d6\d7\d8\d9\d0/;

let a = `1_2_3_4_5_6_7_8_9_0`;
let a1 = Number.parseInt(a.replaceAll("_", "9"));
let a2 = Number.parseInt(a.replaceAll("_", "0"));
a1 = Math.floor(Math.sqrt(a1));
a2 = Math.ceil(Math.sqrt(a2));
console.log(a1, a2, a1 - a2);
console.log("testing");

for (let i = a2; i < a1; i++) {
  // print every 1 % of the way
  if (i % 1000000 === 0) {
    console.log(i);
  }
  if (r.test(`${i ** 2}`)) {
    console.log(i);
    break;
  }
}
// 1192213971
