package main

import "fmt"


func main() {
    var T, N int
    fmt.Scanf("%d", &T)

    // 0 <= N <= 60
    height := make([]int, 61)
    height[0] = 1

    // Since 61 is a very small number, cache the heights for all 0 <= N <= 60
    // So, the calculation is only made once, and used for all the tests
    for i := 1; i < 61; i += 1 {
        if i % 2 == 0 {
            height[i] = height[i-1] + 1
        } else {
            height[i] = 2 * height[i-1]
        }
    }

    for i := 0; i < T; i++ {
        fmt.Scanf("%d", &N)
        fmt.Println(height[N])
    }
}
