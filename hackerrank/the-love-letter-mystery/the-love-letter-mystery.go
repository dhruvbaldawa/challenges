package main

import (
    "fmt"
    "math"
)

func main() {
    var T int
    fmt.Scanf("%d", &T)

    for {
        var s string
        _, err := fmt.Scanf("%s", &s)
        if err != nil {
            break
        }

        var sum float64
        sum = 0

        for i := 0; i < len(s)/2; i++ {
            sum += math.Abs(float64(s[i]) - float64(s[len(s)-1-i]))
        }

        fmt.Println(sum)
    }
}
