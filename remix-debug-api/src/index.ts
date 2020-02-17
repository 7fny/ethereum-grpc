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
function debug(call: any) {
    let result = new DebugResponse();
    const txHash: string = call.request.debugInterface.payload;
    const testnetId: string = call.request.debugInterface.testnetId;
    var url: string = "http://172.26.84.11:";
    var port: string = "754"
    switch (testnetId) {
        case "5":
            url += port + "5";
            break;
        case "3":
            url += port + "6";
            break;
        case "4":
            url += port + "7";
            break;
        case "ganache":
            url = "http://ganache:8545";
            break;
        default:
            url = "http://ganache:8545";
    }
    const web3 = new Web3(url);
    const ethdebugger = new EthDebugger({ web3 });
    web3.eth.getTransaction(txHash).then((tx: any) => {
        ethdebugger.event.register('newTraceLoaded', (trace: any) => {
            call.write({ result: JSON.stringify(trace) });
        });
        ethdebugger.debug(tx);

    }).catch((error: any) => {
        throw error;
    });
}