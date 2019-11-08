require('module-alias/register')
var PROTO_PATH = './services/remix-debug.proto'
import * as grpc from 'grpc'
import * as protoLoader from '@grpc/proto-loader'
import { DebugResponse } from "generated/services/remix-debug_pb"
// @ts-ignore
import { EthDebugger } from 'remix-debug'
import Web3 from 'web3'

// gRPC server
const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
})
var protoDescriptor = grpc.loadPackageDefinition(packageDefinition) as any;

var remix_debug_pb = protoDescriptor.remix_debug;

var rxDbgServer = new grpc.Server();
rxDbgServer.addService(remix_debug_pb.RemixDebugService.service, {
    RunDebug: debug,
});
rxDbgServer.bind('0.0.0.0:50052', grpc.ServerCredentials.createInsecure());
console.log('Server running at 0.0.0.0:50052');
rxDbgServer.start();

// remix-debug code
const web3 = new Web3('http://localhost:8545');
const ethdebugger = new EthDebugger({ web3 });
function debug(call: any) {
    let result = new DebugResponse();
    console.log(call.request);
    web3.eth.getTransaction("0x79d432611763d3efd6d2a7d309b7c0ef84102cef9d8113362b83d45458c723df", (error, tx) => {
        if (error)
            throw error;
        console.log(tx);
        ethdebugger.event.register('newTraceLoaded', (trace: any) => {
            console.log(trace);
            call.write({ result: trace });
        });
        ethdebugger.debug(tx);
    })
}