_J='agentDot1qMrpMvrpIntf'
_I='not-accessible'
_H='agentDot1qMvrpPort'
_G='Unsigned32'
_F='Integer32'
_E='read-write'
_D='NETGEAR-MVRP-MIB'
_C='EnabledStatus'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
agentDot1qMrpMxrp,=mibBuilder.importSymbols('NETGEAR-MRP-MIB','agentDot1qMrpMxrp')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TruthValue')
fastPathMVRP=ModuleIdentity((1,3,6,1,4,1,4526,10,60,2,2))
if mibBuilder.loadTexts:fastPathMVRP.setRevisions(('2011-04-29 00:00',))
_AgentDot1qMvrp_ObjectIdentity=ObjectIdentity
agentDot1qMvrp=_AgentDot1qMvrp_ObjectIdentity((1,3,6,1,4,1,4526,10,60,2,2,1))
_AgentDot1qPortMvrpTable_Object=MibTable
agentDot1qPortMvrpTable=_AgentDot1qPortMvrpTable_Object((1,3,6,1,4,1,4526,10,60,2,2,1,1))
if mibBuilder.loadTexts:agentDot1qPortMvrpTable.setStatus(_A)
_AgentDot1qPortMvrpEntry_Object=MibTableRow
agentDot1qPortMvrpEntry=_AgentDot1qPortMvrpEntry_Object((1,3,6,1,4,1,4526,10,60,2,2,1,1,1))
agentDot1qPortMvrpEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:agentDot1qPortMvrpEntry.setStatus(_A)
class _AgentDot1qMvrpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1qMvrpPort_Type.__name__=_G
_AgentDot1qMvrpPort_Object=MibTableColumn
agentDot1qMvrpPort=_AgentDot1qMvrpPort_Object((1,3,6,1,4,1,4526,10,60,2,2,1,1,1,1),_AgentDot1qMvrpPort_Type())
agentDot1qMvrpPort.setMaxAccess(_I)
if mibBuilder.loadTexts:agentDot1qMvrpPort.setStatus(_A)
class _AgentDot1qPortMvrpMode_Type(EnabledStatus):defaultValue=2
_AgentDot1qPortMvrpMode_Type.__name__=_C
_AgentDot1qPortMvrpMode_Object=MibTableColumn
agentDot1qPortMvrpMode=_AgentDot1qPortMvrpMode_Object((1,3,6,1,4,1,4526,10,60,2,2,1,1,1,10),_AgentDot1qPortMvrpMode_Type())
agentDot1qPortMvrpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qPortMvrpMode.setStatus(_A)
class _AgentDot1qBridgeMvrpMode_Type(EnabledStatus):defaultValue=2
_AgentDot1qBridgeMvrpMode_Type.__name__=_C
_AgentDot1qBridgeMvrpMode_Object=MibScalar
agentDot1qBridgeMvrpMode=_AgentDot1qBridgeMvrpMode_Object((1,3,6,1,4,1,4526,10,60,2,2,1,2),_AgentDot1qBridgeMvrpMode_Type())
agentDot1qBridgeMvrpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qBridgeMvrpMode.setStatus(_A)
class _AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type(EnabledStatus):defaultValue=2
_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type.__name__=_C
_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object=MibScalar
agentDot1qBridgeMrpPeriodicStateMachineForMvrp=_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object((1,3,6,1,4,1,4526,10,60,2,2,1,3),_AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type())
agentDot1qBridgeMrpPeriodicStateMachineForMvrp.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qBridgeMrpPeriodicStateMachineForMvrp.setStatus(_A)
_AgentDot1qMrpMvrpStats_ObjectIdentity=ObjectIdentity
agentDot1qMrpMvrpStats=_AgentDot1qMrpMvrpStats_ObjectIdentity((1,3,6,1,4,1,4526,10,60,2,2,2))
_AgentDot1qMrpMvrpPktTx_Type=Counter32
_AgentDot1qMrpMvrpPktTx_Object=MibScalar
agentDot1qMrpMvrpPktTx=_AgentDot1qMrpMvrpPktTx_Object((1,3,6,1,4,1,4526,10,60,2,2,2,1),_AgentDot1qMrpMvrpPktTx_Type())
agentDot1qMrpMvrpPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktTx.setStatus(_A)
_AgentDot1qMrpMvrpPktRx_Type=Counter32
_AgentDot1qMrpMvrpPktRx_Object=MibScalar
agentDot1qMrpMvrpPktRx=_AgentDot1qMrpMvrpPktRx_Object((1,3,6,1,4,1,4526,10,60,2,2,2,2),_AgentDot1qMrpMvrpPktRx_Type())
agentDot1qMrpMvrpPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktRx.setStatus(_A)
_AgentDot1qMrpMvrpPktRxBadHeader_Type=Counter32
_AgentDot1qMrpMvrpPktRxBadHeader_Object=MibScalar
agentDot1qMrpMvrpPktRxBadHeader=_AgentDot1qMrpMvrpPktRxBadHeader_Object((1,3,6,1,4,1,4526,10,60,2,2,2,3),_AgentDot1qMrpMvrpPktRxBadHeader_Type())
agentDot1qMrpMvrpPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktRxBadHeader.setStatus(_A)
_AgentDot1qMrpMvrpPktRxBadFormat_Type=Counter32
_AgentDot1qMrpMvrpPktRxBadFormat_Object=MibScalar
agentDot1qMrpMvrpPktRxBadFormat=_AgentDot1qMrpMvrpPktRxBadFormat_Object((1,3,6,1,4,1,4526,10,60,2,2,2,4),_AgentDot1qMrpMvrpPktRxBadFormat_Type())
agentDot1qMrpMvrpPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktRxBadFormat.setStatus(_A)
_AgentDot1qMrpMvrpPktTxFailure_Type=Counter32
_AgentDot1qMrpMvrpPktTxFailure_Object=MibScalar
agentDot1qMrpMvrpPktTxFailure=_AgentDot1qMrpMvrpPktTxFailure_Object((1,3,6,1,4,1,4526,10,60,2,2,2,5),_AgentDot1qMrpMvrpPktTxFailure_Type())
agentDot1qMrpMvrpPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktTxFailure.setStatus(_A)
_AgentDot1qMrpMvrpStatsTable_Object=MibTable
agentDot1qMrpMvrpStatsTable=_AgentDot1qMrpMvrpStatsTable_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6))
if mibBuilder.loadTexts:agentDot1qMrpMvrpStatsTable.setStatus(_A)
_AgentDot1qMrpMvrpStatisticsEntry_Object=MibTableRow
agentDot1qMrpMvrpStatisticsEntry=_AgentDot1qMrpMvrpStatisticsEntry_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1))
agentDot1qMrpMvrpStatisticsEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:agentDot1qMrpMvrpStatisticsEntry.setStatus(_A)
class _AgentDot1qMrpMvrpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1qMrpMvrpIntf_Type.__name__=_F
_AgentDot1qMrpMvrpIntf_Object=MibTableColumn
agentDot1qMrpMvrpIntf=_AgentDot1qMrpMvrpIntf_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,1),_AgentDot1qMrpMvrpIntf_Type())
agentDot1qMrpMvrpIntf.setMaxAccess(_I)
if mibBuilder.loadTexts:agentDot1qMrpMvrpIntf.setStatus(_A)
_AgentDot1qMrpMvrpPortPktTx_Type=Counter32
_AgentDot1qMrpMvrpPortPktTx_Object=MibTableColumn
agentDot1qMrpMvrpPortPktTx=_AgentDot1qMrpMvrpPortPktTx_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,2),_AgentDot1qMrpMvrpPortPktTx_Type())
agentDot1qMrpMvrpPortPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktTx.setStatus(_A)
_AgentDot1qMrpMvrpPortPktRx_Type=Counter32
_AgentDot1qMrpMvrpPortPktRx_Object=MibTableColumn
agentDot1qMrpMvrpPortPktRx=_AgentDot1qMrpMvrpPortPktRx_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,3),_AgentDot1qMrpMvrpPortPktRx_Type())
agentDot1qMrpMvrpPortPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktRx.setStatus(_A)
_AgentDot1qMrpMvrpPortPktRxBadHeader_Type=Counter32
_AgentDot1qMrpMvrpPortPktRxBadHeader_Object=MibTableColumn
agentDot1qMrpMvrpPortPktRxBadHeader=_AgentDot1qMrpMvrpPortPktRxBadHeader_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,4),_AgentDot1qMrpMvrpPortPktRxBadHeader_Type())
agentDot1qMrpMvrpPortPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktRxBadHeader.setStatus(_A)
_AgentDot1qMrpMvrpPortPktRxBadFormat_Type=Counter32
_AgentDot1qMrpMvrpPortPktRxBadFormat_Object=MibTableColumn
agentDot1qMrpMvrpPortPktRxBadFormat=_AgentDot1qMrpMvrpPortPktRxBadFormat_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,5),_AgentDot1qMrpMvrpPortPktRxBadFormat_Type())
agentDot1qMrpMvrpPortPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktRxBadFormat.setStatus(_A)
_AgentDot1qMrpMvrpPortPktTxFailure_Type=Counter32
_AgentDot1qMrpMvrpPortPktTxFailure_Object=MibTableColumn
agentDot1qMrpMvrpPortPktTxFailure=_AgentDot1qMrpMvrpPortPktTxFailure_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,6),_AgentDot1qMrpMvrpPortPktTxFailure_Type())
agentDot1qMrpMvrpPortPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktTxFailure.setStatus(_A)
_AgentDot1qMrpMvrpPortPktRegFailure_Type=Counter32
_AgentDot1qMrpMvrpPortPktRegFailure_Object=MibTableColumn
agentDot1qMrpMvrpPortPktRegFailure=_AgentDot1qMrpMvrpPortPktRegFailure_Object((1,3,6,1,4,1,4526,10,60,2,2,2,6,1,7),_AgentDot1qMrpMvrpPortPktRegFailure_Type())
agentDot1qMrpMvrpPortPktRegFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPortPktRegFailure.setStatus(_A)
_AgentDot1qMrpMvrpPktMessageFailure_Type=Counter32
_AgentDot1qMrpMvrpPktMessageFailure_Object=MibScalar
agentDot1qMrpMvrpPktMessageFailure=_AgentDot1qMrpMvrpPktMessageFailure_Object((1,3,6,1,4,1,4526,10,60,2,2,2,7),_AgentDot1qMrpMvrpPktMessageFailure_Type())
agentDot1qMrpMvrpPktMessageFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMvrpPktMessageFailure.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathMVRP':fastPathMVRP,'agentDot1qMvrp':agentDot1qMvrp,'agentDot1qPortMvrpTable':agentDot1qPortMvrpTable,'agentDot1qPortMvrpEntry':agentDot1qPortMvrpEntry,_H:agentDot1qMvrpPort,'agentDot1qPortMvrpMode':agentDot1qPortMvrpMode,'agentDot1qBridgeMvrpMode':agentDot1qBridgeMvrpMode,'agentDot1qBridgeMrpPeriodicStateMachineForMvrp':agentDot1qBridgeMrpPeriodicStateMachineForMvrp,'agentDot1qMrpMvrpStats':agentDot1qMrpMvrpStats,'agentDot1qMrpMvrpPktTx':agentDot1qMrpMvrpPktTx,'agentDot1qMrpMvrpPktRx':agentDot1qMrpMvrpPktRx,'agentDot1qMrpMvrpPktRxBadHeader':agentDot1qMrpMvrpPktRxBadHeader,'agentDot1qMrpMvrpPktRxBadFormat':agentDot1qMrpMvrpPktRxBadFormat,'agentDot1qMrpMvrpPktTxFailure':agentDot1qMrpMvrpPktTxFailure,'agentDot1qMrpMvrpStatsTable':agentDot1qMrpMvrpStatsTable,'agentDot1qMrpMvrpStatisticsEntry':agentDot1qMrpMvrpStatisticsEntry,_J:agentDot1qMrpMvrpIntf,'agentDot1qMrpMvrpPortPktTx':agentDot1qMrpMvrpPortPktTx,'agentDot1qMrpMvrpPortPktRx':agentDot1qMrpMvrpPortPktRx,'agentDot1qMrpMvrpPortPktRxBadHeader':agentDot1qMrpMvrpPortPktRxBadHeader,'agentDot1qMrpMvrpPortPktRxBadFormat':agentDot1qMrpMvrpPortPktRxBadFormat,'agentDot1qMrpMvrpPortPktTxFailure':agentDot1qMrpMvrpPortPktTxFailure,'agentDot1qMrpMvrpPortPktRegFailure':agentDot1qMrpMvrpPortPktRegFailure,'agentDot1qMrpMvrpPktMessageFailure':agentDot1qMrpMvrpPktMessageFailure})