package main

import (
	"errors"
	"fmt"
	"strings"
)

func cleanString(in string) []int {
	in = strings.Replace(in, "-", "", -1)
	var isbn_int []int = make([]int, len(in))

	for i := 0; i < len(in); i++ {
		if in[i] == 'X' {
			isbn_int[i] = 10
		} else {
			isbn_int[i] = int(in[i] - '0')
		}
	}
	return isbn_int
}

func verifyISBN(isbn string) (bool, error) {
	var isbn_int = cleanString(isbn)
	if len(isbn_int) != 10 {
		return false, errors.New("The ISBN number should have 10")
	}

	var sum int = 0
	for counter := 10; counter > 0; counter-- {
		intgr := isbn_int[10-counter]
		sum += counter * int(intgr)
	}

	if sum%11 == 0 {
		return true, nil
	} else {
		return false, nil
	}

}

func TestVerifyISBN() {
	cases := []struct {
		isbn   string
		result bool
	}{
		{"0-7475-3269-9", true},
		{"0-7475-3269-X", false},
		{"156881111X", true},
	}

	for _, c := range cases {
		result, err := verifyISBN(c.isbn)
		if c.result != result {
			fmt.Printf("verifyISBN(%q) == %t, %t required\n", c.isbn, result, c.result)
		} else if err != nil {
			fmt.Printf("verifyISBN(%q) error: %q\n", c.isbn, err)
		} else {
			fmt.Printf("verifyISBN(%q) == %t, passed!\n", c.isbn, result)
		}
	}
}

func main() {
	// verifyISBN("0-7475-3269-X")
	// fmt.Println("Please run tests via `go test`.")
	TestVerifyISBN()
}
