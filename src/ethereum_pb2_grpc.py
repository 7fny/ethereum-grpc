# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ethereum_pb2 as ethereum__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ProtoEthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalance = channel.unary_unary(
                '/protoeth.ProtoEthService/GetBalance',
                request_serializer=ethereum__pb2.GetBalanceReq.SerializeToString,
                response_deserializer=ethereum__pb2.GetBalanceResp.FromString,
                )
        self.EstimateGas = channel.unary_unary(
                '/protoeth.ProtoEthService/EstimateGas',
                request_serializer=ethereum__pb2.EstimateGasReq.SerializeToString,
                response_deserializer=ethereum__pb2.EstimateGasResp.FromString,
                )
        self.GetGanacheAccounts = channel.unary_unary(
                '/protoeth.ProtoEthService/GetGanacheAccounts',
                request_serializer=ethereum__pb2.GanacheAccReq.SerializeToString,
                response_deserializer=ethereum__pb2.GanacheAccRsp.FromString,
                )
        self.BuildRawTransaction = channel.unary_unary(
                '/protoeth.ProtoEthService/BuildRawTransaction',
                request_serializer=ethereum__pb2.BuildTxRequest.SerializeToString,
                response_deserializer=ethereum__pb2.RawTransaction.FromString,
                )
        self.SendRawTransactions = channel.unary_unary(
                '/protoeth.ProtoEthService/SendRawTransactions',
                request_serializer=ethereum__pb2.SendTxRequest.SerializeToString,
                response_deserializer=ethereum__pb2.TxHash.FromString,
                )
        self.Transact = channel.unary_unary(
                '/protoeth.ProtoEthService/Transact',
                request_serializer=ethereum__pb2.BuildTxRequest.SerializeToString,
                response_deserializer=ethereum__pb2.TxHash.FromString,
                )
        self.GetTransaction = channel.unary_unary(
                '/protoeth.ProtoEthService/GetTransaction',
                request_serializer=ethereum__pb2.GetTxReq.SerializeToString,
                response_deserializer=ethereum__pb2.TransactionInfo.FromString,
                )
        self.GetTransactionReceipt = channel.unary_unary(
                '/protoeth.ProtoEthService/GetTransactionReceipt',
                request_serializer=ethereum__pb2.TxHash.SerializeToString,
                response_deserializer=ethereum__pb2.TxReceipt.FromString,
                )
        self.ContractCall = channel.unary_unary(
                '/protoeth.ProtoEthService/ContractCall',
                request_serializer=ethereum__pb2.CallRequest.SerializeToString,
                response_deserializer=ethereum__pb2.CallResponse.FromString,
                )
        self.GetHashrate = channel.unary_unary(
                '/protoeth.ProtoEthService/GetHashrate',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ethereum__pb2.NumResult.FromString,
                )
        self.GetGasPrice = channel.unary_unary(
                '/protoeth.ProtoEthService/GetGasPrice',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ethereum__pb2.NumResult.FromString,
                )
        self.GetBlockNumber = channel.unary_unary(
                '/protoeth.ProtoEthService/GetBlockNumber',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=ethereum__pb2.BlockNumber.FromString,
                )
        self.GetBlockTransactionCount = channel.unary_unary(
                '/protoeth.ProtoEthService/GetBlockTransactionCount',
                request_serializer=ethereum__pb2.HashStringOrNumber.SerializeToString,
                response_deserializer=ethereum__pb2.CountResp.FromString,
                )
        self.GetBlock = channel.unary_unary(
                '/protoeth.ProtoEthService/GetBlock',
                request_serializer=ethereum__pb2.HashStringOrNumber.SerializeToString,
                response_deserializer=ethereum__pb2.ObjResp.FromString,
                )
        self.GetTransactionFromBlock = channel.unary_unary(
                '/protoeth.ProtoEthService/GetTransactionFromBlock',
                request_serializer=ethereum__pb2.InfoWithIndex.SerializeToString,
                response_deserializer=ethereum__pb2.ObjResp.FromString,
                )


class ProtoEthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBalance(self, request, context):
        """Done
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstimateGas(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGanacheAccounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuildRawTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRawTransactions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransaction(self, request, context):
        """TODO
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionReceipt(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ContractCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHashrate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGasPrice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockTransactionCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTransactionFromBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProtoEthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalance,
                    request_deserializer=ethereum__pb2.GetBalanceReq.FromString,
                    response_serializer=ethereum__pb2.GetBalanceResp.SerializeToString,
            ),
            'EstimateGas': grpc.unary_unary_rpc_method_handler(
                    servicer.EstimateGas,
                    request_deserializer=ethereum__pb2.EstimateGasReq.FromString,
                    response_serializer=ethereum__pb2.EstimateGasResp.SerializeToString,
            ),
            'GetGanacheAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGanacheAccounts,
                    request_deserializer=ethereum__pb2.GanacheAccReq.FromString,
                    response_serializer=ethereum__pb2.GanacheAccRsp.SerializeToString,
            ),
            'BuildRawTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.BuildRawTransaction,
                    request_deserializer=ethereum__pb2.BuildTxRequest.FromString,
                    response_serializer=ethereum__pb2.RawTransaction.SerializeToString,
            ),
            'SendRawTransactions': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRawTransactions,
                    request_deserializer=ethereum__pb2.SendTxRequest.FromString,
                    response_serializer=ethereum__pb2.TxHash.SerializeToString,
            ),
            'Transact': grpc.unary_unary_rpc_method_handler(
                    servicer.Transact,
                    request_deserializer=ethereum__pb2.BuildTxRequest.FromString,
                    response_serializer=ethereum__pb2.TxHash.SerializeToString,
            ),
            'GetTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransaction,
                    request_deserializer=ethereum__pb2.GetTxReq.FromString,
                    response_serializer=ethereum__pb2.TransactionInfo.SerializeToString,
            ),
            'GetTransactionReceipt': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransactionReceipt,
                    request_deserializer=ethereum__pb2.TxHash.FromString,
                    response_serializer=ethereum__pb2.TxReceipt.SerializeToString,
            ),
            'ContractCall': grpc.unary_unary_rpc_method_handler(
                    servicer.ContractCall,
                    request_deserializer=ethereum__pb2.CallRequest.FromString,
                    response_serializer=ethereum__pb2.CallResponse.SerializeToString,
            ),
            'GetHashrate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHashrate,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ethereum__pb2.NumResult.SerializeToString,
            ),
            'GetGasPrice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGasPrice,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ethereum__pb2.NumResult.SerializeToString,
            ),
            'GetBlockNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockNumber,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=ethereum__pb2.BlockNumber.SerializeToString,
            ),
            'GetBlockTransactionCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockTransactionCount,
                    request_deserializer=ethereum__pb2.HashStringOrNumber.FromString,
                    response_serializer=ethereum__pb2.CountResp.SerializeToString,
            ),
            'GetBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlock,
                    request_deserializer=ethereum__pb2.HashStringOrNumber.FromString,
                    response_serializer=ethereum__pb2.ObjResp.SerializeToString,
            ),
            'GetTransactionFromBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransactionFromBlock,
                    request_deserializer=ethereum__pb2.InfoWithIndex.FromString,
                    response_serializer=ethereum__pb2.ObjResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protoeth.ProtoEthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProtoEthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetBalance',
            ethereum__pb2.GetBalanceReq.SerializeToString,
            ethereum__pb2.GetBalanceResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstimateGas(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/EstimateGas',
            ethereum__pb2.EstimateGasReq.SerializeToString,
            ethereum__pb2.EstimateGasResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGanacheAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetGanacheAccounts',
            ethereum__pb2.GanacheAccReq.SerializeToString,
            ethereum__pb2.GanacheAccRsp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuildRawTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/BuildRawTransaction',
            ethereum__pb2.BuildTxRequest.SerializeToString,
            ethereum__pb2.RawTransaction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRawTransactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/SendRawTransactions',
            ethereum__pb2.SendTxRequest.SerializeToString,
            ethereum__pb2.TxHash.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Transact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/Transact',
            ethereum__pb2.BuildTxRequest.SerializeToString,
            ethereum__pb2.TxHash.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetTransaction',
            ethereum__pb2.GetTxReq.SerializeToString,
            ethereum__pb2.TransactionInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionReceipt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetTransactionReceipt',
            ethereum__pb2.TxHash.SerializeToString,
            ethereum__pb2.TxReceipt.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ContractCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/ContractCall',
            ethereum__pb2.CallRequest.SerializeToString,
            ethereum__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHashrate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetHashrate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ethereum__pb2.NumResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGasPrice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetGasPrice',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ethereum__pb2.NumResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetBlockNumber',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ethereum__pb2.BlockNumber.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockTransactionCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetBlockTransactionCount',
            ethereum__pb2.HashStringOrNumber.SerializeToString,
            ethereum__pb2.CountResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetBlock',
            ethereum__pb2.HashStringOrNumber.SerializeToString,
            ethereum__pb2.ObjResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTransactionFromBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protoeth.ProtoEthService/GetTransactionFromBlock',
            ethereum__pb2.InfoWithIndex.SerializeToString,
            ethereum__pb2.ObjResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
