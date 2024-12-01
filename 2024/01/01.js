let file = "2024/01/01.txt";

const fs = require("node:fs");

try {
	const data = fs.readFileSync(file, "utf8");
	let a = [];
	let b = [];

	data.split("\n").forEach((line) => {
		let ab = line.split(/[ ]+/);
		a.push(ab[0]);
		b.push(ab[1]);
	});

	console.log(
		a
			.sort()
			.map(function (item, index) {
				return Math.abs(item - b.sort()[index]);
			})
			.reduce(function (a, b) {
				return a + b;
			})
	);
} catch (err) {
	console.error(err);
}
