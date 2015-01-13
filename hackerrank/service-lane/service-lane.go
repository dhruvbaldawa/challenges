package main;

import "fmt"

func main() {
    var N, T int
    fmt.Scanf("%d %d", &N, &T)
    width := make([]int, N)

    // Initialize the width of service lane
    for n := 0; n < N; n++ {
        fmt.Scanf("%d", &width[n])
    }

    // fmt.Println(N, T, width)
    for n := 0; n < T; n++ {
        var i, j, min int
        // read i and j for the problem
        fmt.Scanf("%d %d", &i, &j)

        // minimum width will be the least allowed vehicle
        min = width[i]
        for x := i; x <= j; x += 1 {
            if width[x] < min {
                min = width[x]
            }
        }
        fmt.Println(min)
    }
}
