const path = require("path");
const file = path.join(__dirname, "/09.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n")[0];
let sum = 0;
let id = 0;
let lastid = Math.floor(data.length / 2);
let i = 0;
let j = data.length - 1;
let x = 0;
let lastelements = data.slice(j, j + 1);
while (j > i) {
	if (i % 2 == 0) {
		for (let k = 0; k < data[i]; k++) {
			sum += x * id;
			x++;
		}
		id++;
	} else {
		for (let k = 0; k < data[i]; k++) {
			if (lastelements == 0 && i > j) {
				j -= 2;
				break;
			}
			if (lastelements == 0) {
				j -= 2;
				lastid--;
				lastelements = data.slice(j, j + 1);
			}
			lastelements--;
			sum += x * lastid;
			x++;
		}
	}
	i++;
}
while (lastelements != 0) {
	lastelements--;
	sum += x * lastid;
	x++;
}

// 6334655948042 too low
console.log(sum);
