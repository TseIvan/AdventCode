package main

import (
    "fmt"
    "io/ioutil"
    "strings"
)

func main() {
    file, err := ioutil.ReadFile("day16.txt")
    if err != nil {
        fmt.Print(err)
    }
    signal := string(file) // convert content to a 'string'
    signal = strings.TrimRight(signal, "\r\n")
    for _, char := range signal {
      fmt.Printf("character %c \n", char)
      // fmt.Printf("character %c starts at byte position %d\n", char, pos)
    }
    // fmt.Println(str) // print the content as a 'string'
}
