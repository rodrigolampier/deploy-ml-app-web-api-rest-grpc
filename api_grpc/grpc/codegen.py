# Instale os pacotes:
# pip install grpcio
# pip install grpcio.tools

from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=.',
        '--grpc_python_out=.',
        './iris.proto',
    )
)