package services

import (
	pb "app/protos"
	"context"
	"log"
)

// Server is a protos.StatusServer instance.
type Server struct {
	pb.StatusServer
}

func (s *Server) Test(ctx context.Context, in *pb.StatusRequest) (*pb.StatusResponse, error) {
	log.Printf("Receive message: %s", in.Check)
	return &pb.StatusResponse{Status: "Ok."}, nil
}