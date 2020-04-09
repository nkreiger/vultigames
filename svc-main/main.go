package main

import (
	pb "app/protos"
	api "app/services"
	"context"
	"google.golang.org/grpc"
	"log"
	"net"
)

const (
	network = "tcp"
	port    = ":9901"
	url     = "localhost"
)


func main() {
	log.Println("Go Server starting up...")

	ctx := context.Background()

	listener, err := net.Listen(network, port)

	if err != nil {
		log.Printf("Listening error: %v", err)
	}

	defer func() {
		if err := listener.Close(); err != nil {
			log.Printf("Failed to close %s %s: %v", network, port, err)
		}
	}()

	server := grpc.NewServer()

	pb.RegisterStatusServer(server, &api.Server{})

	go func() {
		defer server.GracefulStop()
		<-ctx.Done()
	}()

	server.Serve(listener)
}
