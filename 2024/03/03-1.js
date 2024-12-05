const path = require("path");
const file = path.join(__dirname, "/03.txt");
const fs = require("node:fs");

try {
	const data = fs.readFileSync(file, "utf8");
	const mulls = data.match(/mul\(\d+,\d+\)/g);

	let sum = 0;
	mulls.forEach((str) => {
		sum += str
			.substring(4, str.length - 1)
			.split(",")
			.reduce((a, b) => Number(a) * Number(b));
	});
	console.log(sum);
} catch (err) {
	console.log(err);
}
