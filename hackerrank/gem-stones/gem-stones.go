package main

import (
    "fmt"
)

func main() {
    var N int
    fmt.Scanf("%d", &N)

    rocks := make([]string, N)
    element_map := make(map[rune]bool)

    for i := 0; i < N; i++{
        fmt.Scanf("%s", &rocks[i])
    }

    fmt.Println("Rocks: ", rocks)
    for _, rock := range rocks {
        // set all elements to false
        for k, v := range element_map {
            element_map[k] = false
        }

        for _, element := range rock {
            element_map[element] = true
        }

        // remove elements from element_map which are false
        for k, v := range element_map {
            if !v {
                fmt.Println(k, "->", v)
                delete(element_map, k)
            }
        }

        fmt.Println("element_map", element_map)

    }

    fmt.Println(len(element_map))
}
