_J='agentDot1qMrpMmrpIntf'
_I='not-accessible'
_H='agentDot1qMmrpPort'
_G='Unsigned32'
_F='Integer32'
_E='read-write'
_D='NETGEAR-MMRP-MIB'
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
fastPathMMRP=ModuleIdentity((1,3,6,1,4,1,4526,10,60,2,1))
if mibBuilder.loadTexts:fastPathMMRP.setRevisions(('2011-04-29 00:00',))
_AgentDot1qMmrp_ObjectIdentity=ObjectIdentity
agentDot1qMmrp=_AgentDot1qMmrp_ObjectIdentity((1,3,6,1,4,1,4526,10,60,2,1,1))
_AgentDot1qPortMmrpTable_Object=MibTable
agentDot1qPortMmrpTable=_AgentDot1qPortMmrpTable_Object((1,3,6,1,4,1,4526,10,60,2,1,1,1))
if mibBuilder.loadTexts:agentDot1qPortMmrpTable.setStatus(_A)
_AgentDot1qPortMmrpEntry_Object=MibTableRow
agentDot1qPortMmrpEntry=_AgentDot1qPortMmrpEntry_Object((1,3,6,1,4,1,4526,10,60,2,1,1,1,1))
agentDot1qPortMmrpEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:agentDot1qPortMmrpEntry.setStatus(_A)
class _AgentDot1qMmrpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1qMmrpPort_Type.__name__=_G
_AgentDot1qMmrpPort_Object=MibTableColumn
agentDot1qMmrpPort=_AgentDot1qMmrpPort_Object((1,3,6,1,4,1,4526,10,60,2,1,1,1,1,1),_AgentDot1qMmrpPort_Type())
agentDot1qMmrpPort.setMaxAccess(_I)
if mibBuilder.loadTexts:agentDot1qMmrpPort.setStatus(_A)
class _AgentDot1qPortMmrpMode_Type(EnabledStatus):defaultValue=2
_AgentDot1qPortMmrpMode_Type.__name__=_C
_AgentDot1qPortMmrpMode_Object=MibTableColumn
agentDot1qPortMmrpMode=_AgentDot1qPortMmrpMode_Object((1,3,6,1,4,1,4526,10,60,2,1,1,1,1,2),_AgentDot1qPortMmrpMode_Type())
agentDot1qPortMmrpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qPortMmrpMode.setStatus(_A)
class _AgentDot1qBridgeMmrpMode_Type(EnabledStatus):defaultValue=2
_AgentDot1qBridgeMmrpMode_Type.__name__=_C
_AgentDot1qBridgeMmrpMode_Object=MibScalar
agentDot1qBridgeMmrpMode=_AgentDot1qBridgeMmrpMode_Object((1,3,6,1,4,1,4526,10,60,2,1,1,2),_AgentDot1qBridgeMmrpMode_Type())
agentDot1qBridgeMmrpMode.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qBridgeMmrpMode.setStatus(_A)
class _AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type(EnabledStatus):defaultValue=2
_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type.__name__=_C
_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object=MibScalar
agentDot1qBridgeMrpPeriodicStateMachineForMmrp=_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object((1,3,6,1,4,1,4526,10,60,2,1,1,3),_AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type())
agentDot1qBridgeMrpPeriodicStateMachineForMmrp.setMaxAccess(_E)
if mibBuilder.loadTexts:agentDot1qBridgeMrpPeriodicStateMachineForMmrp.setStatus(_A)
_AgentDot1qMrpMmrpStats_ObjectIdentity=ObjectIdentity
agentDot1qMrpMmrpStats=_AgentDot1qMrpMmrpStats_ObjectIdentity((1,3,6,1,4,1,4526,10,60,2,1,2))
_AgentDot1qMrpMmrpPktTx_Type=Counter32
_AgentDot1qMrpMmrpPktTx_Object=MibScalar
agentDot1qMrpMmrpPktTx=_AgentDot1qMrpMmrpPktTx_Object((1,3,6,1,4,1,4526,10,60,2,1,2,1),_AgentDot1qMrpMmrpPktTx_Type())
agentDot1qMrpMmrpPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPktTx.setStatus(_A)
_AgentDot1qMrpMmrpPktRx_Type=Counter32
_AgentDot1qMrpMmrpPktRx_Object=MibScalar
agentDot1qMrpMmrpPktRx=_AgentDot1qMrpMmrpPktRx_Object((1,3,6,1,4,1,4526,10,60,2,1,2,2),_AgentDot1qMrpMmrpPktRx_Type())
agentDot1qMrpMmrpPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPktRx.setStatus(_A)
_AgentDot1qMrpMmrpPktRxBadHeader_Type=Counter32
_AgentDot1qMrpMmrpPktRxBadHeader_Object=MibScalar
agentDot1qMrpMmrpPktRxBadHeader=_AgentDot1qMrpMmrpPktRxBadHeader_Object((1,3,6,1,4,1,4526,10,60,2,1,2,3),_AgentDot1qMrpMmrpPktRxBadHeader_Type())
agentDot1qMrpMmrpPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPktRxBadHeader.setStatus(_A)
_AgentDot1qMrpMmrpPktRxBadFormat_Type=Counter32
_AgentDot1qMrpMmrpPktRxBadFormat_Object=MibScalar
agentDot1qMrpMmrpPktRxBadFormat=_AgentDot1qMrpMmrpPktRxBadFormat_Object((1,3,6,1,4,1,4526,10,60,2,1,2,4),_AgentDot1qMrpMmrpPktRxBadFormat_Type())
agentDot1qMrpMmrpPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPktRxBadFormat.setStatus(_A)
_AgentDot1qMrpMmrpPktTxFailure_Type=Counter32
_AgentDot1qMrpMmrpPktTxFailure_Object=MibScalar
agentDot1qMrpMmrpPktTxFailure=_AgentDot1qMrpMmrpPktTxFailure_Object((1,3,6,1,4,1,4526,10,60,2,1,2,5),_AgentDot1qMrpMmrpPktTxFailure_Type())
agentDot1qMrpMmrpPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPktTxFailure.setStatus(_A)
_AgentDot1qMrpMmrpStatsTable_Object=MibTable
agentDot1qMrpMmrpStatsTable=_AgentDot1qMrpMmrpStatsTable_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6))
if mibBuilder.loadTexts:agentDot1qMrpMmrpStatsTable.setStatus(_A)
_AgentDot1qMrpMmrpStatisticsEntry_Object=MibTableRow
agentDot1qMrpMmrpStatisticsEntry=_AgentDot1qMrpMmrpStatisticsEntry_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1))
agentDot1qMrpMmrpStatisticsEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:agentDot1qMrpMmrpStatisticsEntry.setStatus(_A)
class _AgentDot1qMrpMmrpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1qMrpMmrpIntf_Type.__name__=_F
_AgentDot1qMrpMmrpIntf_Object=MibTableColumn
agentDot1qMrpMmrpIntf=_AgentDot1qMrpMmrpIntf_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,1),_AgentDot1qMrpMmrpIntf_Type())
agentDot1qMrpMmrpIntf.setMaxAccess(_I)
if mibBuilder.loadTexts:agentDot1qMrpMmrpIntf.setStatus(_A)
_AgentDot1qMrpMmrpPortPktTx_Type=Counter32
_AgentDot1qMrpMmrpPortPktTx_Object=MibTableColumn
agentDot1qMrpMmrpPortPktTx=_AgentDot1qMrpMmrpPortPktTx_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,2),_AgentDot1qMrpMmrpPortPktTx_Type())
agentDot1qMrpMmrpPortPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPortPktTx.setStatus(_A)
_AgentDot1qMrpMmrpPortPktRx_Type=Counter32
_AgentDot1qMrpMmrpPortPktRx_Object=MibTableColumn
agentDot1qMrpMmrpPortPktRx=_AgentDot1qMrpMmrpPortPktRx_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,3),_AgentDot1qMrpMmrpPortPktRx_Type())
agentDot1qMrpMmrpPortPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPortPktRx.setStatus(_A)
_AgentDot1qMrpMmrpPortPktRxBadHeader_Type=Counter32
_AgentDot1qMrpMmrpPortPktRxBadHeader_Object=MibTableColumn
agentDot1qMrpMmrpPortPktRxBadHeader=_AgentDot1qMrpMmrpPortPktRxBadHeader_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,4),_AgentDot1qMrpMmrpPortPktRxBadHeader_Type())
agentDot1qMrpMmrpPortPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPortPktRxBadHeader.setStatus(_A)
_AgentDot1qMrpMmrpPortPktRxBadFormat_Type=Counter32
_AgentDot1qMrpMmrpPortPktRxBadFormat_Object=MibTableColumn
agentDot1qMrpMmrpPortPktRxBadFormat=_AgentDot1qMrpMmrpPortPktRxBadFormat_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,5),_AgentDot1qMrpMmrpPortPktRxBadFormat_Type())
agentDot1qMrpMmrpPortPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPortPktRxBadFormat.setStatus(_A)
_AgentDot1qMrpMmrpPortPktTxFailure_Type=Counter32
_AgentDot1qMrpMmrpPortPktTxFailure_Object=MibTableColumn
agentDot1qMrpMmrpPortPktTxFailure=_AgentDot1qMrpMmrpPortPktTxFailure_Object((1,3,6,1,4,1,4526,10,60,2,1,2,6,1,6),_AgentDot1qMrpMmrpPortPktTxFailure_Type())
agentDot1qMrpMmrpPortPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDot1qMrpMmrpPortPktTxFailure.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fastPathMMRP':fastPathMMRP,'agentDot1qMmrp':agentDot1qMmrp,'agentDot1qPortMmrpTable':agentDot1qPortMmrpTable,'agentDot1qPortMmrpEntry':agentDot1qPortMmrpEntry,_H:agentDot1qMmrpPort,'agentDot1qPortMmrpMode':agentDot1qPortMmrpMode,'agentDot1qBridgeMmrpMode':agentDot1qBridgeMmrpMode,'agentDot1qBridgeMrpPeriodicStateMachineForMmrp':agentDot1qBridgeMrpPeriodicStateMachineForMmrp,'agentDot1qMrpMmrpStats':agentDot1qMrpMmrpStats,'agentDot1qMrpMmrpPktTx':agentDot1qMrpMmrpPktTx,'agentDot1qMrpMmrpPktRx':agentDot1qMrpMmrpPktRx,'agentDot1qMrpMmrpPktRxBadHeader':agentDot1qMrpMmrpPktRxBadHeader,'agentDot1qMrpMmrpPktRxBadFormat':agentDot1qMrpMmrpPktRxBadFormat,'agentDot1qMrpMmrpPktTxFailure':agentDot1qMrpMmrpPktTxFailure,'agentDot1qMrpMmrpStatsTable':agentDot1qMrpMmrpStatsTable,'agentDot1qMrpMmrpStatisticsEntry':agentDot1qMrpMmrpStatisticsEntry,_J:agentDot1qMrpMmrpIntf,'agentDot1qMrpMmrpPortPktTx':agentDot1qMrpMmrpPortPktTx,'agentDot1qMrpMmrpPortPktRx':agentDot1qMrpMmrpPortPktRx,'agentDot1qMrpMmrpPortPktRxBadHeader':agentDot1qMrpMmrpPortPktRxBadHeader,'agentDot1qMrpMmrpPortPktRxBadFormat':agentDot1qMrpMmrpPortPktRxBadFormat,'agentDot1qMrpMmrpPortPktTxFailure':agentDot1qMrpMmrpPortPktTxFailure})