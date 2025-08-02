_T='fsofcMeterIndex'
_S='fsofcGroupIndex'
_R='fsofcFlowIndex'
_Q='fsofcTableIndex'
_P='fsofcIfIndex'
_O='fsofcControllerConnAuxId'
_N='fsofcControllerIpAddress'
_M='fsofcControllerIpAddrType'
_L='d32'
_K='Unsigned32'
_J='disabled'
_I='enabled'
_H='DisplayString'
_G='fsofcContextId'
_F='not-accessible'
_E='read-write'
_D='SUPERMICRO-OFC-CFG-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
fsofc=ModuleIdentity((1,3,6,1,4,1,10876,101,2,81))
if mibBuilder.loadTexts:fsofc.setRevisions(('2013-01-11 00:00',))
class PortList(TextualConvention,OctetString):status=_A
class INTEGER64(TextualConvention,Counter64):status=_A;displayHint='d64'
class ActionString(TextualConvention,OctetString):status=_A;displayHint='255as';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class ContextId(TextualConvention,Unsigned32):status=_A;displayHint=_L;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class TableIndex(TextualConvention,Unsigned32):status=_A;displayHint=_L;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class FlowIndex(TextualConvention,Unsigned32):status=_A;displayHint=_L;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsofcCfgGroup_ObjectIdentity=ObjectIdentity
fsofcCfgGroup=_FsofcCfgGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,1))
_FsofcCfgTable_Object=MibTable
fsofcCfgTable=_FsofcCfgTable_Object((1,3,6,1,4,1,10876,101,2,81,1,1))
if mibBuilder.loadTexts:fsofcCfgTable.setStatus(_A)
_FsofcCfgEntry_Object=MibTableRow
fsofcCfgEntry=_FsofcCfgEntry_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1))
fsofcCfgEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsofcCfgEntry.setStatus(_A)
_FsofcContextId_Type=ContextId
_FsofcContextId_Object=MibTableColumn
fsofcContextId=_FsofcContextId_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,1),_FsofcContextId_Type())
fsofcContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcContextId.setStatus(_A)
class _FsofcModuleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsofcModuleStatus_Type.__name__=_C
_FsofcModuleStatus_Object=MibTableColumn
fsofcModuleStatus=_FsofcModuleStatus_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,2),_FsofcModuleStatus_Type())
fsofcModuleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcModuleStatus.setStatus(_A)
class _FsofcSupportedVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('v100',1),('v131',2)))
_FsofcSupportedVersion_Type.__name__=_C
_FsofcSupportedVersion_Object=MibTableColumn
fsofcSupportedVersion=_FsofcSupportedVersion_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,3),_FsofcSupportedVersion_Type())
fsofcSupportedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcSupportedVersion.setStatus(_A)
class _FsofcDefaultFlowMissBehaviour_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('sendToController',2)))
_FsofcDefaultFlowMissBehaviour_Type.__name__=_C
_FsofcDefaultFlowMissBehaviour_Object=MibTableColumn
fsofcDefaultFlowMissBehaviour=_FsofcDefaultFlowMissBehaviour_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,4),_FsofcDefaultFlowMissBehaviour_Type())
fsofcDefaultFlowMissBehaviour.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcDefaultFlowMissBehaviour.setStatus(_A)
class _FsofcControlPktBuffering_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsofcControlPktBuffering_Type.__name__=_C
_FsofcControlPktBuffering_Object=MibTableColumn
fsofcControlPktBuffering=_FsofcControlPktBuffering_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,5),_FsofcControlPktBuffering_Type())
fsofcControlPktBuffering.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcControlPktBuffering.setStatus(_A)
class _FsofcIpReassembleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsofcIpReassembleStatus_Type.__name__=_C
_FsofcIpReassembleStatus_Object=MibTableColumn
fsofcIpReassembleStatus=_FsofcIpReassembleStatus_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,6),_FsofcIpReassembleStatus_Type())
fsofcIpReassembleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcIpReassembleStatus.setStatus(_A)
class _FsofcPortStpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FsofcPortStpStatus_Type.__name__=_C
_FsofcPortStpStatus_Object=MibTableColumn
fsofcPortStpStatus=_FsofcPortStpStatus_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,7),_FsofcPortStpStatus_Type())
fsofcPortStpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcPortStpStatus.setStatus(_A)
_FsofcTraceEnable_Type=Unsigned32
_FsofcTraceEnable_Object=MibTableColumn
fsofcTraceEnable=_FsofcTraceEnable_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,8),_FsofcTraceEnable_Type())
fsofcTraceEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcTraceEnable.setStatus(_A)
class _FsofcSwitchModeOnConnFailure_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('failSecure',1),('failStandAlone',2)))
_FsofcSwitchModeOnConnFailure_Type.__name__=_C
_FsofcSwitchModeOnConnFailure_Object=MibTableColumn
fsofcSwitchModeOnConnFailure=_FsofcSwitchModeOnConnFailure_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,9),_FsofcSwitchModeOnConnFailure_Type())
fsofcSwitchModeOnConnFailure.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcSwitchModeOnConnFailure.setStatus(_A)
_FsofcSwitchEntryStatus_Type=RowStatus
_FsofcSwitchEntryStatus_Object=MibTableColumn
fsofcSwitchEntryStatus=_FsofcSwitchEntryStatus_Object((1,3,6,1,4,1,10876,101,2,81,1,1,1,10),_FsofcSwitchEntryStatus_Type())
fsofcSwitchEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcSwitchEntryStatus.setStatus(_A)
_FsofcControllerCfgGroup_ObjectIdentity=ObjectIdentity
fsofcControllerCfgGroup=_FsofcControllerCfgGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,2))
_FsofcControllerConnTable_Object=MibTable
fsofcControllerConnTable=_FsofcControllerConnTable_Object((1,3,6,1,4,1,10876,101,2,81,2,1))
if mibBuilder.loadTexts:fsofcControllerConnTable.setStatus(_A)
_FsofcControllerConnEntry_Object=MibTableRow
fsofcControllerConnEntry=_FsofcControllerConnEntry_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1))
fsofcControllerConnEntry.setIndexNames((0,_D,_G),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:fsofcControllerConnEntry.setStatus(_A)
_FsofcControllerIpAddrType_Type=InetAddressType
_FsofcControllerIpAddrType_Object=MibTableColumn
fsofcControllerIpAddrType=_FsofcControllerIpAddrType_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,1),_FsofcControllerIpAddrType_Type())
fsofcControllerIpAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcControllerIpAddrType.setStatus(_A)
_FsofcControllerIpAddress_Type=InetAddress
_FsofcControllerIpAddress_Object=MibTableColumn
fsofcControllerIpAddress=_FsofcControllerIpAddress_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,2),_FsofcControllerIpAddress_Type())
fsofcControllerIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcControllerIpAddress.setStatus(_A)
class _FsofcControllerConnAuxId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_FsofcControllerConnAuxId_Type.__name__=_C
_FsofcControllerConnAuxId_Object=MibTableColumn
fsofcControllerConnAuxId=_FsofcControllerConnAuxId_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,3),_FsofcControllerConnAuxId_Type())
fsofcControllerConnAuxId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcControllerConnAuxId.setStatus(_A)
class _FsofcControllerConnPort_Type(Integer32):defaultValue=6633;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsofcControllerConnPort_Type.__name__=_C
_FsofcControllerConnPort_Object=MibTableColumn
fsofcControllerConnPort=_FsofcControllerConnPort_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,4),_FsofcControllerConnPort_Type())
fsofcControllerConnPort.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcControllerConnPort.setStatus(_A)
class _FsofcControllerConnProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tcp',1),('ssl',2)))
_FsofcControllerConnProtocol_Type.__name__=_C
_FsofcControllerConnProtocol_Object=MibTableColumn
fsofcControllerConnProtocol=_FsofcControllerConnProtocol_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,5),_FsofcControllerConnProtocol_Type())
fsofcControllerConnProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcControllerConnProtocol.setStatus(_A)
class _FsofcControllerRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('equal',1),('master',2),('slave',3)))
_FsofcControllerRole_Type.__name__=_C
_FsofcControllerRole_Object=MibTableColumn
fsofcControllerRole=_FsofcControllerRole_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,6),_FsofcControllerRole_Type())
fsofcControllerRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcControllerRole.setStatus(_A)
class _FsofcControllerConnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connected',1),('notConnected',2),('connInProgress',3)))
_FsofcControllerConnState_Type.__name__=_C
_FsofcControllerConnState_Object=MibTableColumn
fsofcControllerConnState=_FsofcControllerConnState_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,7),_FsofcControllerConnState_Type())
fsofcControllerConnState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcControllerConnState.setStatus(_A)
class _FsofcControllerConnEchoReqCount_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsofcControllerConnEchoReqCount_Type.__name__=_C
_FsofcControllerConnEchoReqCount_Object=MibTableColumn
fsofcControllerConnEchoReqCount=_FsofcControllerConnEchoReqCount_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,8),_FsofcControllerConnEchoReqCount_Type())
fsofcControllerConnEchoReqCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcControllerConnEchoReqCount.setStatus(_A)
class _FsofcControllerConnEchoReplyCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_FsofcControllerConnEchoReplyCount_Type.__name__=_C
_FsofcControllerConnEchoReplyCount_Object=MibTableColumn
fsofcControllerConnEchoReplyCount=_FsofcControllerConnEchoReplyCount_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,9),_FsofcControllerConnEchoReplyCount_Type())
fsofcControllerConnEchoReplyCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcControllerConnEchoReplyCount.setStatus(_A)
_FsofcControllerConnEntryStatus_Type=RowStatus
_FsofcControllerConnEntryStatus_Object=MibTableColumn
fsofcControllerConnEntryStatus=_FsofcControllerConnEntryStatus_Object((1,3,6,1,4,1,10876,101,2,81,2,1,1,10),_FsofcControllerConnEntryStatus_Type())
fsofcControllerConnEntryStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcControllerConnEntryStatus.setStatus(_A)
_FsofcInterfaceGroup_ObjectIdentity=ObjectIdentity
fsofcInterfaceGroup=_FsofcInterfaceGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,3))
_FsofcIfTable_Object=MibTable
fsofcIfTable=_FsofcIfTable_Object((1,3,6,1,4,1,10876,101,2,81,3,1))
if mibBuilder.loadTexts:fsofcIfTable.setStatus(_A)
_FsofcIfEntry_Object=MibTableRow
fsofcIfEntry=_FsofcIfEntry_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1))
fsofcIfEntry.setIndexNames((0,_D,_G),(0,_D,_P))
if mibBuilder.loadTexts:fsofcIfEntry.setStatus(_A)
_FsofcIfIndex_Type=InterfaceIndex
_FsofcIfIndex_Object=MibTableColumn
fsofcIfIndex=_FsofcIfIndex_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,1),_FsofcIfIndex_Type())
fsofcIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcIfIndex.setStatus(_A)
class _FsofcIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('physical',1),('logical',2),('reserved',3)))
_FsofcIfType_Type.__name__=_C
_FsofcIfType_Object=MibTableColumn
fsofcIfType=_FsofcIfType_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,2),_FsofcIfType_Type())
fsofcIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcIfType.setStatus(_A)
class _FsofcIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsofcIfAlias_Type.__name__=_H
_FsofcIfAlias_Object=MibTableColumn
fsofcIfAlias=_FsofcIfAlias_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,3),_FsofcIfAlias_Type())
fsofcIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcIfAlias.setStatus(_A)
class _FsofcIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('others',3)))
_FsofcIfOperStatus_Type.__name__=_C
_FsofcIfOperStatus_Object=MibTableColumn
fsofcIfOperStatus=_FsofcIfOperStatus_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,4),_FsofcIfOperStatus_Type())
fsofcIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcIfOperStatus.setStatus(_A)
_FsofcVlanEgressPorts_Type=PortList
_FsofcVlanEgressPorts_Object=MibTableColumn
fsofcVlanEgressPorts=_FsofcVlanEgressPorts_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,5),_FsofcVlanEgressPorts_Type())
fsofcVlanEgressPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcVlanEgressPorts.setStatus(_A)
_FsofcVlanUntaggedPorts_Type=PortList
_FsofcVlanUntaggedPorts_Object=MibTableColumn
fsofcVlanUntaggedPorts=_FsofcVlanUntaggedPorts_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,6),_FsofcVlanUntaggedPorts_Type())
fsofcVlanUntaggedPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:fsofcVlanUntaggedPorts.setStatus(_A)
_FsofcVlanInFrames_Type=Counter32
_FsofcVlanInFrames_Object=MibTableColumn
fsofcVlanInFrames=_FsofcVlanInFrames_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,7),_FsofcVlanInFrames_Type())
fsofcVlanInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcVlanInFrames.setStatus(_A)
_FsofcVlanOutFrames_Type=Counter32
_FsofcVlanOutFrames_Object=MibTableColumn
fsofcVlanOutFrames=_FsofcVlanOutFrames_Object((1,3,6,1,4,1,10876,101,2,81,3,1,1,8),_FsofcVlanOutFrames_Type())
fsofcVlanOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcVlanOutFrames.setStatus(_A)
_FsofcFlowGroup_ObjectIdentity=ObjectIdentity
fsofcFlowGroup=_FsofcFlowGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,4))
_FsofcFlowTable_Object=MibTable
fsofcFlowTable=_FsofcFlowTable_Object((1,3,6,1,4,1,10876,101,2,81,4,1))
if mibBuilder.loadTexts:fsofcFlowTable.setStatus(_A)
_FsofcFlowEntry_Object=MibTableRow
fsofcFlowEntry=_FsofcFlowEntry_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1))
fsofcFlowEntry.setIndexNames((0,_D,_G),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:fsofcFlowEntry.setStatus(_A)
_FsofcTableIndex_Type=TableIndex
_FsofcTableIndex_Object=MibTableColumn
fsofcTableIndex=_FsofcTableIndex_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,1),_FsofcTableIndex_Type())
fsofcTableIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcTableIndex.setStatus(_A)
_FsofcFlowIndex_Type=FlowIndex
_FsofcFlowIndex_Object=MibTableColumn
fsofcFlowIndex=_FsofcFlowIndex_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,2),_FsofcFlowIndex_Type())
fsofcFlowIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcFlowIndex.setStatus(_A)
class _FsofcFlowMatchField_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_FsofcFlowMatchField_Type.__name__=_H
_FsofcFlowMatchField_Object=MibTableColumn
fsofcFlowMatchField=_FsofcFlowMatchField_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,3),_FsofcFlowMatchField_Type())
fsofcFlowMatchField.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowMatchField.setStatus(_A)
class _FsofcFlowOutputAction_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_FsofcFlowOutputAction_Type.__name__=_H
_FsofcFlowOutputAction_Object=MibTableColumn
fsofcFlowOutputAction=_FsofcFlowOutputAction_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,4),_FsofcFlowOutputAction_Type())
fsofcFlowOutputAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowOutputAction.setStatus(_A)
_FsofcFlowIdleTimeout_Type=Unsigned32
_FsofcFlowIdleTimeout_Object=MibTableColumn
fsofcFlowIdleTimeout=_FsofcFlowIdleTimeout_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,5),_FsofcFlowIdleTimeout_Type())
fsofcFlowIdleTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowIdleTimeout.setStatus(_A)
_FsofcFlowHardTimeout_Type=Unsigned32
_FsofcFlowHardTimeout_Object=MibTableColumn
fsofcFlowHardTimeout=_FsofcFlowHardTimeout_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,6),_FsofcFlowHardTimeout_Type())
fsofcFlowHardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowHardTimeout.setStatus(_A)
_FsofcFlowPacketCount_Type=INTEGER64
_FsofcFlowPacketCount_Object=MibTableColumn
fsofcFlowPacketCount=_FsofcFlowPacketCount_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,7),_FsofcFlowPacketCount_Type())
fsofcFlowPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowPacketCount.setStatus(_A)
_FsofcFlowByteCount_Type=INTEGER64
_FsofcFlowByteCount_Object=MibTableColumn
fsofcFlowByteCount=_FsofcFlowByteCount_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,8),_FsofcFlowByteCount_Type())
fsofcFlowByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowByteCount.setStatus(_A)
_FsofcFlowDurationSec_Type=Unsigned32
_FsofcFlowDurationSec_Object=MibTableColumn
fsofcFlowDurationSec=_FsofcFlowDurationSec_Object((1,3,6,1,4,1,10876,101,2,81,4,1,1,9),_FsofcFlowDurationSec_Type())
fsofcFlowDurationSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcFlowDurationSec.setStatus(_A)
_FsofcGrpGroup_ObjectIdentity=ObjectIdentity
fsofcGrpGroup=_FsofcGrpGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,5))
_FsofcGroupTable_Object=MibTable
fsofcGroupTable=_FsofcGroupTable_Object((1,3,6,1,4,1,10876,101,2,81,5,1))
if mibBuilder.loadTexts:fsofcGroupTable.setStatus(_A)
_FsofcGroupEntry_Object=MibTableRow
fsofcGroupEntry=_FsofcGroupEntry_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1))
fsofcGroupEntry.setIndexNames((0,_D,_G),(0,_D,_S))
if mibBuilder.loadTexts:fsofcGroupEntry.setStatus(_A)
class _FsofcGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsofcGroupIndex_Type.__name__=_K
_FsofcGroupIndex_Object=MibTableColumn
fsofcGroupIndex=_FsofcGroupIndex_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,1),_FsofcGroupIndex_Type())
fsofcGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcGroupIndex.setStatus(_A)
class _FsofcGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('select',1),('indirect',2),('fastfailover',3)))
_FsofcGroupType_Type.__name__=_C
_FsofcGroupType_Object=MibTableColumn
fsofcGroupType=_FsofcGroupType_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,2),_FsofcGroupType_Type())
fsofcGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcGroupType.setStatus(_A)
_FsofcGroupActionBuckets_Type=ActionString
_FsofcGroupActionBuckets_Object=MibTableColumn
fsofcGroupActionBuckets=_FsofcGroupActionBuckets_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,3),_FsofcGroupActionBuckets_Type())
fsofcGroupActionBuckets.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcGroupActionBuckets.setStatus(_A)
_FsofcGroupPacketCount_Type=INTEGER64
_FsofcGroupPacketCount_Object=MibTableColumn
fsofcGroupPacketCount=_FsofcGroupPacketCount_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,5),_FsofcGroupPacketCount_Type())
fsofcGroupPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcGroupPacketCount.setStatus(_A)
_FsofcGroupByteCount_Type=INTEGER64
_FsofcGroupByteCount_Object=MibTableColumn
fsofcGroupByteCount=_FsofcGroupByteCount_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,6),_FsofcGroupByteCount_Type())
fsofcGroupByteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcGroupByteCount.setStatus(_A)
_FsofcGroupDurationSec_Type=Unsigned32
_FsofcGroupDurationSec_Object=MibTableColumn
fsofcGroupDurationSec=_FsofcGroupDurationSec_Object((1,3,6,1,4,1,10876,101,2,81,5,1,1,7),_FsofcGroupDurationSec_Type())
fsofcGroupDurationSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcGroupDurationSec.setStatus(_A)
_FsofcMeterGroup_ObjectIdentity=ObjectIdentity
fsofcMeterGroup=_FsofcMeterGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,2,81,6))
_FsofcMeterTable_Object=MibTable
fsofcMeterTable=_FsofcMeterTable_Object((1,3,6,1,4,1,10876,101,2,81,6,1))
if mibBuilder.loadTexts:fsofcMeterTable.setStatus(_A)
_FsofcMeterEntry_Object=MibTableRow
fsofcMeterEntry=_FsofcMeterEntry_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1))
fsofcMeterEntry.setIndexNames((0,_D,_G),(0,_D,_T))
if mibBuilder.loadTexts:fsofcMeterEntry.setStatus(_A)
class _FsofcMeterIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsofcMeterIndex_Type.__name__=_K
_FsofcMeterIndex_Object=MibTableColumn
fsofcMeterIndex=_FsofcMeterIndex_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,1),_FsofcMeterIndex_Type())
fsofcMeterIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsofcMeterIndex.setStatus(_A)
class _FsofcMeterBandInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsofcMeterBandInfo_Type.__name__=_H
_FsofcMeterBandInfo_Object=MibTableColumn
fsofcMeterBandInfo=_FsofcMeterBandInfo_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,2),_FsofcMeterBandInfo_Type())
fsofcMeterBandInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcMeterBandInfo.setStatus(_A)
_FsofcMeterFlowCount_Type=Counter32
_FsofcMeterFlowCount_Object=MibTableColumn
fsofcMeterFlowCount=_FsofcMeterFlowCount_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,3),_FsofcMeterFlowCount_Type())
fsofcMeterFlowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcMeterFlowCount.setStatus(_A)
_FsofcMeterPacketInCount_Type=INTEGER64
_FsofcMeterPacketInCount_Object=MibTableColumn
fsofcMeterPacketInCount=_FsofcMeterPacketInCount_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,4),_FsofcMeterPacketInCount_Type())
fsofcMeterPacketInCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcMeterPacketInCount.setStatus(_A)
_FsofcMeterByteInCount_Type=INTEGER64
_FsofcMeterByteInCount_Object=MibTableColumn
fsofcMeterByteInCount=_FsofcMeterByteInCount_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,5),_FsofcMeterByteInCount_Type())
fsofcMeterByteInCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcMeterByteInCount.setStatus(_A)
_FsofcMeterDurationSec_Type=Unsigned32
_FsofcMeterDurationSec_Object=MibTableColumn
fsofcMeterDurationSec=_FsofcMeterDurationSec_Object((1,3,6,1,4,1,10876,101,2,81,6,1,1,6),_FsofcMeterDurationSec_Type())
fsofcMeterDurationSec.setMaxAccess(_B)
if mibBuilder.loadTexts:fsofcMeterDurationSec.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'INTEGER64':INTEGER64,'ActionString':ActionString,'ContextId':ContextId,'TableIndex':TableIndex,'FlowIndex':FlowIndex,'fsofc':fsofc,'fsofcCfgGroup':fsofcCfgGroup,'fsofcCfgTable':fsofcCfgTable,'fsofcCfgEntry':fsofcCfgEntry,_G:fsofcContextId,'fsofcModuleStatus':fsofcModuleStatus,'fsofcSupportedVersion':fsofcSupportedVersion,'fsofcDefaultFlowMissBehaviour':fsofcDefaultFlowMissBehaviour,'fsofcControlPktBuffering':fsofcControlPktBuffering,'fsofcIpReassembleStatus':fsofcIpReassembleStatus,'fsofcPortStpStatus':fsofcPortStpStatus,'fsofcTraceEnable':fsofcTraceEnable,'fsofcSwitchModeOnConnFailure':fsofcSwitchModeOnConnFailure,'fsofcSwitchEntryStatus':fsofcSwitchEntryStatus,'fsofcControllerCfgGroup':fsofcControllerCfgGroup,'fsofcControllerConnTable':fsofcControllerConnTable,'fsofcControllerConnEntry':fsofcControllerConnEntry,_M:fsofcControllerIpAddrType,_N:fsofcControllerIpAddress,_O:fsofcControllerConnAuxId,'fsofcControllerConnPort':fsofcControllerConnPort,'fsofcControllerConnProtocol':fsofcControllerConnProtocol,'fsofcControllerRole':fsofcControllerRole,'fsofcControllerConnState':fsofcControllerConnState,'fsofcControllerConnEchoReqCount':fsofcControllerConnEchoReqCount,'fsofcControllerConnEchoReplyCount':fsofcControllerConnEchoReplyCount,'fsofcControllerConnEntryStatus':fsofcControllerConnEntryStatus,'fsofcInterfaceGroup':fsofcInterfaceGroup,'fsofcIfTable':fsofcIfTable,'fsofcIfEntry':fsofcIfEntry,_P:fsofcIfIndex,'fsofcIfType':fsofcIfType,'fsofcIfAlias':fsofcIfAlias,'fsofcIfOperStatus':fsofcIfOperStatus,'fsofcVlanEgressPorts':fsofcVlanEgressPorts,'fsofcVlanUntaggedPorts':fsofcVlanUntaggedPorts,'fsofcVlanInFrames':fsofcVlanInFrames,'fsofcVlanOutFrames':fsofcVlanOutFrames,'fsofcFlowGroup':fsofcFlowGroup,'fsofcFlowTable':fsofcFlowTable,'fsofcFlowEntry':fsofcFlowEntry,_Q:fsofcTableIndex,_R:fsofcFlowIndex,'fsofcFlowMatchField':fsofcFlowMatchField,'fsofcFlowOutputAction':fsofcFlowOutputAction,'fsofcFlowIdleTimeout':fsofcFlowIdleTimeout,'fsofcFlowHardTimeout':fsofcFlowHardTimeout,'fsofcFlowPacketCount':fsofcFlowPacketCount,'fsofcFlowByteCount':fsofcFlowByteCount,'fsofcFlowDurationSec':fsofcFlowDurationSec,'fsofcGrpGroup':fsofcGrpGroup,'fsofcGroupTable':fsofcGroupTable,'fsofcGroupEntry':fsofcGroupEntry,_S:fsofcGroupIndex,'fsofcGroupType':fsofcGroupType,'fsofcGroupActionBuckets':fsofcGroupActionBuckets,'fsofcGroupPacketCount':fsofcGroupPacketCount,'fsofcGroupByteCount':fsofcGroupByteCount,'fsofcGroupDurationSec':fsofcGroupDurationSec,'fsofcMeterGroup':fsofcMeterGroup,'fsofcMeterTable':fsofcMeterTable,'fsofcMeterEntry':fsofcMeterEntry,_T:fsofcMeterIndex,'fsofcMeterBandInfo':fsofcMeterBandInfo,'fsofcMeterFlowCount':fsofcMeterFlowCount,'fsofcMeterPacketInCount':fsofcMeterPacketInCount,'fsofcMeterByteInCount':fsofcMeterByteInCount,'fsofcMeterDurationSec':fsofcMeterDurationSec})