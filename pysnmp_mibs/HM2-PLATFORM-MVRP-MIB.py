_I='hm2AgentDot1qMrpMvrpIntf'
_H='not-accessible'
_G='hm2AgentDot1qMvrpPort'
_F='read-write'
_E='HM2-PLATFORM-MVRP-MIB'
_D='Integer32'
_C='EnabledStatus'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2AgentDot1qMrpMxrp,=mibBuilder.importSymbols('HM2-PLATFORM-MRP-MIB','hm2AgentDot1qMrpMxrp')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2PlatformMVRP=ModuleIdentity((1,3,6,1,4,1,248,12,60,2,2))
if mibBuilder.loadTexts:hm2PlatformMVRP.setRevisions(('2013-04-10 00:00',))
_Hm2AgentDot1qMvrp_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMvrp=_Hm2AgentDot1qMvrp_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,2,1))
_Hm2AgentDot1qPortMvrpTable_Object=MibTable
hm2AgentDot1qPortMvrpTable=_Hm2AgentDot1qPortMvrpTable_Object((1,3,6,1,4,1,248,12,60,2,2,1,1))
if mibBuilder.loadTexts:hm2AgentDot1qPortMvrpTable.setStatus(_A)
_Hm2AgentDot1qPortMvrpEntry_Object=MibTableRow
hm2AgentDot1qPortMvrpEntry=_Hm2AgentDot1qPortMvrpEntry_Object((1,3,6,1,4,1,248,12,60,2,2,1,1,1))
hm2AgentDot1qPortMvrpEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hm2AgentDot1qPortMvrpEntry.setStatus(_A)
class _Hm2AgentDot1qMvrpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMvrpPort_Type.__name__=_D
_Hm2AgentDot1qMvrpPort_Object=MibTableColumn
hm2AgentDot1qMvrpPort=_Hm2AgentDot1qMvrpPort_Object((1,3,6,1,4,1,248,12,60,2,2,1,1,1,1),_Hm2AgentDot1qMvrpPort_Type())
hm2AgentDot1qMvrpPort.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentDot1qMvrpPort.setStatus(_A)
class _Hm2AgentDot1qPortMvrpMode_Type(EnabledStatus):defaultValue=1
_Hm2AgentDot1qPortMvrpMode_Type.__name__=_C
_Hm2AgentDot1qPortMvrpMode_Object=MibTableColumn
hm2AgentDot1qPortMvrpMode=_Hm2AgentDot1qPortMvrpMode_Object((1,3,6,1,4,1,248,12,60,2,2,1,1,1,10),_Hm2AgentDot1qPortMvrpMode_Type())
hm2AgentDot1qPortMvrpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qPortMvrpMode.setStatus(_A)
class _Hm2AgentDot1qBridgeMvrpMode_Type(EnabledStatus):defaultValue=2
_Hm2AgentDot1qBridgeMvrpMode_Type.__name__=_C
_Hm2AgentDot1qBridgeMvrpMode_Object=MibScalar
hm2AgentDot1qBridgeMvrpMode=_Hm2AgentDot1qBridgeMvrpMode_Object((1,3,6,1,4,1,248,12,60,2,2,1,2),_Hm2AgentDot1qBridgeMvrpMode_Type())
hm2AgentDot1qBridgeMvrpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMvrpMode.setStatus(_A)
class _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type(EnabledStatus):defaultValue=2
_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type.__name__=_C
_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object=MibScalar
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp=_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Object((1,3,6,1,4,1,248,12,60,2,2,1,3),_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp_Type())
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp.setStatus(_A)
_Hm2AgentDot1qMrpMvrpStats_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMrpMvrpStats=_Hm2AgentDot1qMrpMvrpStats_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,2,2))
_Hm2AgentDot1qMrpMvrpPktTx_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktTx_Object=MibScalar
hm2AgentDot1qMrpMvrpPktTx=_Hm2AgentDot1qMrpMvrpPktTx_Object((1,3,6,1,4,1,248,12,60,2,2,2,1),_Hm2AgentDot1qMrpMvrpPktTx_Type())
hm2AgentDot1qMrpMvrpPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPktRx_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktRx_Object=MibScalar
hm2AgentDot1qMrpMvrpPktRx=_Hm2AgentDot1qMrpMvrpPktRx_Object((1,3,6,1,4,1,248,12,60,2,2,2,2),_Hm2AgentDot1qMrpMvrpPktRx_Type())
hm2AgentDot1qMrpMvrpPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Object=MibScalar
hm2AgentDot1qMrpMvrpPktRxBadHeader=_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,2,2,3),_Hm2AgentDot1qMrpMvrpPktRxBadHeader_Type())
hm2AgentDot1qMrpMvrpPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Object=MibScalar
hm2AgentDot1qMrpMvrpPktRxBadFormat=_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,2,2,4),_Hm2AgentDot1qMrpMvrpPktRxBadFormat_Type())
hm2AgentDot1qMrpMvrpPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktTxFailure_Object=MibScalar
hm2AgentDot1qMrpMvrpPktTxFailure=_Hm2AgentDot1qMrpMvrpPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,2,2,5),_Hm2AgentDot1qMrpMvrpPktTxFailure_Type())
hm2AgentDot1qMrpMvrpPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMvrpStatsTable_Object=MibTable
hm2AgentDot1qMrpMvrpStatsTable=_Hm2AgentDot1qMrpMvrpStatsTable_Object((1,3,6,1,4,1,248,12,60,2,2,2,6))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpStatsTable.setStatus(_A)
_Hm2AgentDot1qMrpMvrpStatsEntry_Object=MibTableRow
hm2AgentDot1qMrpMvrpStatsEntry=_Hm2AgentDot1qMrpMvrpStatsEntry_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1))
hm2AgentDot1qMrpMvrpStatsEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpStatsEntry.setStatus(_A)
class _Hm2AgentDot1qMrpMvrpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMrpMvrpIntf_Type.__name__=_D
_Hm2AgentDot1qMrpMvrpIntf_Object=MibTableColumn
hm2AgentDot1qMrpMvrpIntf=_Hm2AgentDot1qMrpMvrpIntf_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,1),_Hm2AgentDot1qMrpMvrpIntf_Type())
hm2AgentDot1qMrpMvrpIntf.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpIntf.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktTx_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktTx_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktTx=_Hm2AgentDot1qMrpMvrpPortPktTx_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,2),_Hm2AgentDot1qMrpMvrpPortPktTx_Type())
hm2AgentDot1qMrpMvrpPortPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktRx_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktRx_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRx=_Hm2AgentDot1qMrpMvrpPortPktRx_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,3),_Hm2AgentDot1qMrpMvrpPortPktRx_Type())
hm2AgentDot1qMrpMvrpPortPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRxBadHeader=_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,4),_Hm2AgentDot1qMrpMvrpPortPktRxBadHeader_Type())
hm2AgentDot1qMrpMvrpPortPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRxBadFormat=_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,5),_Hm2AgentDot1qMrpMvrpPortPktRxBadFormat_Type())
hm2AgentDot1qMrpMvrpPortPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktTxFailure=_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,6),_Hm2AgentDot1qMrpMvrpPortPktTxFailure_Type())
hm2AgentDot1qMrpMvrpPortPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Type=Counter32
_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Object=MibTableColumn
hm2AgentDot1qMrpMvrpPortPktRegFailure=_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Object((1,3,6,1,4,1,248,12,60,2,2,2,6,1,7),_Hm2AgentDot1qMrpMvrpPortPktRegFailure_Type())
hm2AgentDot1qMrpMvrpPortPktRegFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPortPktRegFailure.setStatus(_A)
_Hm2AgentDot1qMrpMvrpPktMessageFailure_Type=Counter32
_Hm2AgentDot1qMrpMvrpPktMessageFailure_Object=MibScalar
hm2AgentDot1qMrpMvrpPktMessageFailure=_Hm2AgentDot1qMrpMvrpPktMessageFailure_Object((1,3,6,1,4,1,248,12,60,2,2,2,7),_Hm2AgentDot1qMrpMvrpPktMessageFailure_Type())
hm2AgentDot1qMrpMvrpPktMessageFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMvrpPktMessageFailure.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hm2PlatformMVRP':hm2PlatformMVRP,'hm2AgentDot1qMvrp':hm2AgentDot1qMvrp,'hm2AgentDot1qPortMvrpTable':hm2AgentDot1qPortMvrpTable,'hm2AgentDot1qPortMvrpEntry':hm2AgentDot1qPortMvrpEntry,_G:hm2AgentDot1qMvrpPort,'hm2AgentDot1qPortMvrpMode':hm2AgentDot1qPortMvrpMode,'hm2AgentDot1qBridgeMvrpMode':hm2AgentDot1qBridgeMvrpMode,'hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp':hm2AgentDot1qBridgeMrpPeriodicStateMachineForMvrp,'hm2AgentDot1qMrpMvrpStats':hm2AgentDot1qMrpMvrpStats,'hm2AgentDot1qMrpMvrpPktTx':hm2AgentDot1qMrpMvrpPktTx,'hm2AgentDot1qMrpMvrpPktRx':hm2AgentDot1qMrpMvrpPktRx,'hm2AgentDot1qMrpMvrpPktRxBadHeader':hm2AgentDot1qMrpMvrpPktRxBadHeader,'hm2AgentDot1qMrpMvrpPktRxBadFormat':hm2AgentDot1qMrpMvrpPktRxBadFormat,'hm2AgentDot1qMrpMvrpPktTxFailure':hm2AgentDot1qMrpMvrpPktTxFailure,'hm2AgentDot1qMrpMvrpStatsTable':hm2AgentDot1qMrpMvrpStatsTable,'hm2AgentDot1qMrpMvrpStatsEntry':hm2AgentDot1qMrpMvrpStatsEntry,_I:hm2AgentDot1qMrpMvrpIntf,'hm2AgentDot1qMrpMvrpPortPktTx':hm2AgentDot1qMrpMvrpPortPktTx,'hm2AgentDot1qMrpMvrpPortPktRx':hm2AgentDot1qMrpMvrpPortPktRx,'hm2AgentDot1qMrpMvrpPortPktRxBadHeader':hm2AgentDot1qMrpMvrpPortPktRxBadHeader,'hm2AgentDot1qMrpMvrpPortPktRxBadFormat':hm2AgentDot1qMrpMvrpPortPktRxBadFormat,'hm2AgentDot1qMrpMvrpPortPktTxFailure':hm2AgentDot1qMrpMvrpPortPktTxFailure,'hm2AgentDot1qMrpMvrpPortPktRegFailure':hm2AgentDot1qMrpMvrpPortPktRegFailure,'hm2AgentDot1qMrpMvrpPktMessageFailure':hm2AgentDot1qMrpMvrpPktMessageFailure})