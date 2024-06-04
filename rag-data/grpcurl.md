# grpcurl
grpcurl is a command-line tool that lets you interact with gRPC servers. It's basically curl for gRPC servers.
Common ports for gRPC services include 50051

## Example commands:
### grpcurl -plaintext -vv <ip:port> list
	Use this for initial scan of the gRPC API.
	Outputs a list of available services at the given address:port.
	-plaintext flag says to not use TLS when connecting.

### grpcurl -plaintext -vv <ip:port> list <Service>
	Use this to gather information about a service provided by the gRPC API.
	Outputs a list of available methods for the given service.
	-plaintext flag says to not use TSL when connecting.

### grpcurl -plaintext -vv <ip:port> describe <Service>
	Outputs the available methods for the given service with each methods input parameters and expected output.
	-plaintext flag says to not use TSL when connecting.

### grpcurl -plaintext -vv -format text -d '<input string>' <ip:port> <Service.Method>
	Submits data to the given service.method endpoint.
	-plaintext flag says to not use TSL when connecting.
	-format text flag tells the given input data is in a text format.
	-d '<input string>' flag tells what data to submit.