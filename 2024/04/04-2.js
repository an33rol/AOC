const path = require("path");
const file = path.join(__dirname, "/04.txt");
const fs = require("node:fs");

const data = fs.readFileSync(file, "utf8").split("\n");
let found = 0;

data.forEach((line, index) => {
	for (let j = 0; j < data[0].length; j++) {
		if (data[index][j] == "A") {
			let mas = 0;

			for (dir of [
				[1, 1],
				[1, -1],
				[-1, 1],
				[-1, -1],
			]) {
				try {
					if (
						data[index + dir[0]][j + dir[1]] == "S" &&
						data[index + dir[0] * -1][j + dir[1] * -1] == "M"
					) {
						mas++;
					}
				} catch (e) {}
			}
			if (mas == 2) {
				found++;
			}
		}
	}
});

console.log(found);
