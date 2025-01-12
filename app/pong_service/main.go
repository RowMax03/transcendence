package main

import (
	"fmt"
	"net/http"
	"server-side-pong/game"
)

const (
	port = ":4000"
)

func main() {
	game.StartSender()

	http.HandleFunc("/", game.HandleConnection)
	fmt.Println("WebSocket server is running on ws://localhost" + port)
	err := http.ListenAndServe(port, nil)
	if err != nil {
		panic(err)
	}
}
