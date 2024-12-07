const path = require("path");
const file = path.join(__dirname, "/07.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let sum = 0;
data.forEach((line) => {
	let res = parseInt(line.split(":")[0]);
	let nums = line
		.split(": ")[1]
		.split(" ")
		.map((e) => parseInt(e));
	let possible = [nums[0]];
	for (let i = 1; i < nums.length; i++) {
		tmp = [];
		for (elem of possible) {
			tmp.push(elem * nums[i]);
			tmp.push(elem + nums[i]);
			tmp.push(parseInt(elem.toString().concat(nums[i])));
		}
		possible = tmp.filter((e) => e <= res);
	}
	if (possible.includes(res)) sum += res;
});

console.log(sum);
