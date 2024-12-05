const path = require("path");
const file = path.join(__dirname, "/04.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let found = 0;

data.forEach((line, index) => {
	for (let j = 0; j < data[0].length; j++) {
		if (data[index][j] == "X") {
			for (dir of [
				[0, 1],
				[1, 0],
				[0, -1],
				[-1, 0],
				[1, 1],
				[1, -1],
				[-1, 1],
				[-1, -1],
			]) {
				let good = true;
				for (step of [
					[1, "M"],
					[2, "A"],
					[3, "S"],
				]) {
					try {
						if (
							data[index + step[0] * dir[0]][j + step[0] * dir[1]] !=
							step[1]
						) {
							good = false;
							break;
						}
					} catch (e) {
						good = false;
					}
				}
				if (good) {
					found++;
				}
			}
		}
	}
});

console.log(found);
