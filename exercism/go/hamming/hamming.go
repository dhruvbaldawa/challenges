package hamming

import "errors"

func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return -1, errors.New("length of strings is not equal")
	}

	counter := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			counter++
		}
	}

	return counter, nil
}
