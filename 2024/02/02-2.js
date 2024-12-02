let file = "02.txt";

const fs = require("node:fs");

function processLine(line, checkAgain) {
	let growing = Number(line[1]) - Number(line[0]) > 0;
	for (let i = 0; i < line.length - 1; i++) {
		let diff = Number(line[i + 1]) - Number(line[i]);
		if (
			Math.abs(diff) > 3 ||
			Math.abs(diff) < 1 ||
			(diff < 0 && growing) ||
			(diff > 0 && !growing)
		) {
			if (checkAgain) {
				// optimize ?
				for (let j = 0; j < line.length; j++) {
					let temp = Array.of(...line);
					temp.splice(j, 1);

					if (processLine(temp, false)) {
						return true;
					}
				}
			}
			return false;
		}
	}
	return true;
}

try {
	const data = fs.readFileSync(file, "utf8");
	let count = 0;
	data.split("\n").forEach((line) => {
		if (processLine(line.split(" "), true)) count++;
	});
	console.log(count);
} catch (err) {
	console.log(err);
}
