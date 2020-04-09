echo "begin"
protoc -I . game.proto --go_out=plugins=grpc:svc-main/protos/ \
&& \
echo "go main server proto compiled"