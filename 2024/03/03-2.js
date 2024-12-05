const path = require("path");
const file = path.join(__dirname, "/03.txt");
const fs = require("node:fs");

try {
	const data = fs.readFileSync(file, "utf8");
	const mulls = data.match(/mul\(\d+,\d+\)|do\(\)|don't\(\)/g);

	let sum = 0;
	let doing = true;
	mulls.forEach((str) => {
		if (str.startsWith("don't")) {
			doing = false;
			return;
		} else if (str.startsWith("do")) {
			doing = true;
			return;
		}
		if (doing) {
			sum += str
				.substring(4, str.length - 1)
				.split(",")
				.reduce((a, b) => Number(a) * Number(b));
		}
	});

	console.log(sum);
} catch (err) {
	console.log(err);
}
