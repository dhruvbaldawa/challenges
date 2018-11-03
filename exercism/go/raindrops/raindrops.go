package raindrops

import "strconv"

func Convert(number int) (output string) {
	if number%3 == 0 || number%5 == 0 || number%7 == 0 {

		if number%3 == 0 {
			output = output + "Pling"
		}

		if number%5 == 0 {
			output = output + "Plang"
		}

		if number%7 == 0 {
			output = output + "Plong"
		}
	} else {
		output = strconv.Itoa(number)
	}

	return
}
