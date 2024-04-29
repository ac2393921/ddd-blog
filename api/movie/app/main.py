from app.infrastructures.gateway.grpc.server import GrpcServer


def main():
    server = GrpcServer()
    server.run()


if __name__ == "__main__":
    main()
