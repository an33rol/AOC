const path = require("path");
const file = path.join(__dirname, "/09.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n")[0];
let sum = 0;
// let id = 0;
// let lastid = Math.floor(data.length / 2);
// let i = 0;
// let j = data.length - 1;
// let x = 0;
// let lastelements = data.slice(j, j + 1);

console.log(data);
let empty = [];
let files = [];
for (let i = 0; i < data.length; i += 2) {
	files.push(parseInt(data.slice(i, i + 1)));
	console.log(data.slice(i + 1, i + 2));
	empty.push(parseInt(data.slice(i + 1, i + 2)));
}
empty.pop(-1);

console.log("files", files);
console.log("before", empty);

for (let i = files.length - 1; i >= 0; i--) {
	for (let j = 0; j < empty.length; j++) {
		if (parseInt(files[i]) < empty[j]) {
			// leftover space
			empty.splice(j + 1, 0, empty[j] - files[i]);
			// taken space
			empty[j] = [i, files[i]]; // id, len
			console.log(empty[j], files[i]);
			break;
		}
	}
}

console.log("after,", empty);

let id = 0;
let newarray = [];
for (let i = 0; i < data.length; i += 2) {
	newarray.push(id, data.slice(i, i + 1));
	id++;
}

// // translate
// let line = "";
// while (i < data.length) {
// 	line += id.toString().repeat(data.slice(i, i + 1));
// 	line += ".".repeat(data.slice(i + 1, i + 2));
// 	i += 2;
// 	id++;
// }
// // console.log(line);
// let end = line.length;
// for (let k = id - 1; k >= 0; k--) {
// 	let rgxp = new RegExp("(" + k.toString() + ")+", "g");
// 	let match = Array.from(line.substring(0, end).matchAll(rgxp)).slice(-1)[0];
// 	console.log(match, "for", k);

// 	let matchlen = match[0].length;
// 	// console.log(match, "for", k, "of len", matchlen);

// 	let ergxp = new RegExp("\\.{" + matchlen + "}");
// 	let empty = line.substring(0, end).match(ergxp);
// 	console.log(empty);
// 	if (empty && match.index > empty.index) {
// 		// console.log("EMPTY", empty);

// 		line = line.replace(rgxp, empty);
// 		line = line.replace(ergxp, match[0]);
// 		// console.log("new", line);
// 	}
// 	end = match.index;
// }
// // console.log(line);

// for (let i = 0; i < line.length; i++) {
// 	if (line.slice(i, i + 1) != ".") sum += parseInt(line.slice(i, i + 1)) * i;
// }

// console.log(sum);
