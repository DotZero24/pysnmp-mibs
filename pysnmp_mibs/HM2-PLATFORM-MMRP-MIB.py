_I='hm2AgentDot1qMrpMmrpIntf'
_H='not-accessible'
_G='hm2AgentDot1qMmrpPort'
_F='read-write'
_E='HM2-PLATFORM-MMRP-MIB'
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
hm2PlatformMMRP=ModuleIdentity((1,3,6,1,4,1,248,12,60,2,1))
if mibBuilder.loadTexts:hm2PlatformMMRP.setRevisions(('2013-04-10 00:00',))
_Hm2AgentDot1qMmrp_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMmrp=_Hm2AgentDot1qMmrp_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,1,1))
_Hm2AgentDot1qPortMmrpTable_Object=MibTable
hm2AgentDot1qPortMmrpTable=_Hm2AgentDot1qPortMmrpTable_Object((1,3,6,1,4,1,248,12,60,2,1,1,1))
if mibBuilder.loadTexts:hm2AgentDot1qPortMmrpTable.setStatus(_A)
_Hm2AgentDot1qPortMmrpEntry_Object=MibTableRow
hm2AgentDot1qPortMmrpEntry=_Hm2AgentDot1qPortMmrpEntry_Object((1,3,6,1,4,1,248,12,60,2,1,1,1,1))
hm2AgentDot1qPortMmrpEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hm2AgentDot1qPortMmrpEntry.setStatus(_A)
class _Hm2AgentDot1qMmrpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMmrpPort_Type.__name__=_D
_Hm2AgentDot1qMmrpPort_Object=MibTableColumn
hm2AgentDot1qMmrpPort=_Hm2AgentDot1qMmrpPort_Object((1,3,6,1,4,1,248,12,60,2,1,1,1,1,1),_Hm2AgentDot1qMmrpPort_Type())
hm2AgentDot1qMmrpPort.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentDot1qMmrpPort.setStatus(_A)
class _Hm2AgentDot1qPortMmrpMode_Type(EnabledStatus):defaultValue=1
_Hm2AgentDot1qPortMmrpMode_Type.__name__=_C
_Hm2AgentDot1qPortMmrpMode_Object=MibTableColumn
hm2AgentDot1qPortMmrpMode=_Hm2AgentDot1qPortMmrpMode_Object((1,3,6,1,4,1,248,12,60,2,1,1,1,1,2),_Hm2AgentDot1qPortMmrpMode_Type())
hm2AgentDot1qPortMmrpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qPortMmrpMode.setStatus(_A)
class _Hm2AgentDot1qBridgeMmrpMode_Type(EnabledStatus):defaultValue=2
_Hm2AgentDot1qBridgeMmrpMode_Type.__name__=_C
_Hm2AgentDot1qBridgeMmrpMode_Object=MibScalar
hm2AgentDot1qBridgeMmrpMode=_Hm2AgentDot1qBridgeMmrpMode_Object((1,3,6,1,4,1,248,12,60,2,1,1,2),_Hm2AgentDot1qBridgeMmrpMode_Type())
hm2AgentDot1qBridgeMmrpMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMmrpMode.setStatus(_A)
class _Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type(EnabledStatus):defaultValue=2
_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type.__name__=_C
_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object=MibScalar
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp=_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Object((1,3,6,1,4,1,248,12,60,2,1,1,3),_Hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp_Type())
hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp.setStatus(_A)
_Hm2AgentDot1qMrpMmrpStats_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMrpMmrpStats=_Hm2AgentDot1qMrpMmrpStats_ObjectIdentity((1,3,6,1,4,1,248,12,60,2,1,2))
_Hm2AgentDot1qMrpMmrpPktTx_Type=Counter32
_Hm2AgentDot1qMrpMmrpPktTx_Object=MibScalar
hm2AgentDot1qMrpMmrpPktTx=_Hm2AgentDot1qMrpMmrpPktTx_Object((1,3,6,1,4,1,248,12,60,2,1,2,1),_Hm2AgentDot1qMrpMmrpPktTx_Type())
hm2AgentDot1qMrpMmrpPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPktRx_Type=Counter32
_Hm2AgentDot1qMrpMmrpPktRx_Object=MibScalar
hm2AgentDot1qMrpMmrpPktRx=_Hm2AgentDot1qMrpMmrpPktRx_Object((1,3,6,1,4,1,248,12,60,2,1,2,2),_Hm2AgentDot1qMrpMmrpPktRx_Type())
hm2AgentDot1qMrpMmrpPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Object=MibScalar
hm2AgentDot1qMrpMmrpPktRxBadHeader=_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,1,2,3),_Hm2AgentDot1qMrpMmrpPktRxBadHeader_Type())
hm2AgentDot1qMrpMmrpPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Object=MibScalar
hm2AgentDot1qMrpMmrpPktRxBadFormat=_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,1,2,4),_Hm2AgentDot1qMrpMmrpPktRxBadFormat_Type())
hm2AgentDot1qMrpMmrpPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMmrpPktTxFailure_Object=MibScalar
hm2AgentDot1qMrpMmrpPktTxFailure=_Hm2AgentDot1qMrpMmrpPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,1,2,5),_Hm2AgentDot1qMrpMmrpPktTxFailure_Type())
hm2AgentDot1qMrpMmrpPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMmrpStatsTable_Object=MibTable
hm2AgentDot1qMrpMmrpStatsTable=_Hm2AgentDot1qMrpMmrpStatsTable_Object((1,3,6,1,4,1,248,12,60,2,1,2,6))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpStatsTable.setStatus(_A)
_Hm2AgentDot1qMrpMmrpStatsEntry_Object=MibTableRow
hm2AgentDot1qMrpMmrpStatsEntry=_Hm2AgentDot1qMrpMmrpStatsEntry_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1))
hm2AgentDot1qMrpMmrpStatsEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpStatsEntry.setStatus(_A)
class _Hm2AgentDot1qMrpMmrpIntf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMrpMmrpIntf_Type.__name__=_D
_Hm2AgentDot1qMrpMmrpIntf_Object=MibTableColumn
hm2AgentDot1qMrpMmrpIntf=_Hm2AgentDot1qMrpMmrpIntf_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,1),_Hm2AgentDot1qMrpMmrpIntf_Type())
hm2AgentDot1qMrpMmrpIntf.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpIntf.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPortPktTx_Type=Counter32
_Hm2AgentDot1qMrpMmrpPortPktTx_Object=MibTableColumn
hm2AgentDot1qMrpMmrpPortPktTx=_Hm2AgentDot1qMrpMmrpPortPktTx_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,2),_Hm2AgentDot1qMrpMmrpPortPktTx_Type())
hm2AgentDot1qMrpMmrpPortPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPortPktTx.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPortPktRx_Type=Counter32
_Hm2AgentDot1qMrpMmrpPortPktRx_Object=MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRx=_Hm2AgentDot1qMrpMmrpPortPktRx_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,3),_Hm2AgentDot1qMrpMmrpPortPktRx_Type())
hm2AgentDot1qMrpMmrpPortPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPortPktRx.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Type=Counter32
_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Object=MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRxBadHeader=_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,4),_Hm2AgentDot1qMrpMmrpPortPktRxBadHeader_Type())
hm2AgentDot1qMrpMmrpPortPktRxBadHeader.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPortPktRxBadHeader.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Type=Counter32
_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Object=MibTableColumn
hm2AgentDot1qMrpMmrpPortPktRxBadFormat=_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,5),_Hm2AgentDot1qMrpMmrpPortPktRxBadFormat_Type())
hm2AgentDot1qMrpMmrpPortPktRxBadFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPortPktRxBadFormat.setStatus(_A)
_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Type=Counter32
_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Object=MibTableColumn
hm2AgentDot1qMrpMmrpPortPktTxFailure=_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Object((1,3,6,1,4,1,248,12,60,2,1,2,6,1,6),_Hm2AgentDot1qMrpMmrpPortPktTxFailure_Type())
hm2AgentDot1qMrpMmrpPortPktTxFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpPortPktTxFailure.setStatus(_A)
_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Type=Counter32
_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Object=MibScalar
hm2AgentDot1qMrpMmrpDynamicAddrCount=_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Object((1,3,6,1,4,1,248,12,60,2,1,2,248),_Hm2AgentDot1qMrpMmrpDynamicAddrCount_Type())
hm2AgentDot1qMrpMmrpDynamicAddrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2AgentDot1qMrpMmrpDynamicAddrCount.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hm2PlatformMMRP':hm2PlatformMMRP,'hm2AgentDot1qMmrp':hm2AgentDot1qMmrp,'hm2AgentDot1qPortMmrpTable':hm2AgentDot1qPortMmrpTable,'hm2AgentDot1qPortMmrpEntry':hm2AgentDot1qPortMmrpEntry,_G:hm2AgentDot1qMmrpPort,'hm2AgentDot1qPortMmrpMode':hm2AgentDot1qPortMmrpMode,'hm2AgentDot1qBridgeMmrpMode':hm2AgentDot1qBridgeMmrpMode,'hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp':hm2AgentDot1qBridgeMrpPeriodicStateMachineForMmrp,'hm2AgentDot1qMrpMmrpStats':hm2AgentDot1qMrpMmrpStats,'hm2AgentDot1qMrpMmrpPktTx':hm2AgentDot1qMrpMmrpPktTx,'hm2AgentDot1qMrpMmrpPktRx':hm2AgentDot1qMrpMmrpPktRx,'hm2AgentDot1qMrpMmrpPktRxBadHeader':hm2AgentDot1qMrpMmrpPktRxBadHeader,'hm2AgentDot1qMrpMmrpPktRxBadFormat':hm2AgentDot1qMrpMmrpPktRxBadFormat,'hm2AgentDot1qMrpMmrpPktTxFailure':hm2AgentDot1qMrpMmrpPktTxFailure,'hm2AgentDot1qMrpMmrpStatsTable':hm2AgentDot1qMrpMmrpStatsTable,'hm2AgentDot1qMrpMmrpStatsEntry':hm2AgentDot1qMrpMmrpStatsEntry,_I:hm2AgentDot1qMrpMmrpIntf,'hm2AgentDot1qMrpMmrpPortPktTx':hm2AgentDot1qMrpMmrpPortPktTx,'hm2AgentDot1qMrpMmrpPortPktRx':hm2AgentDot1qMrpMmrpPortPktRx,'hm2AgentDot1qMrpMmrpPortPktRxBadHeader':hm2AgentDot1qMrpMmrpPortPktRxBadHeader,'hm2AgentDot1qMrpMmrpPortPktRxBadFormat':hm2AgentDot1qMrpMmrpPortPktRxBadFormat,'hm2AgentDot1qMrpMmrpPortPktTxFailure':hm2AgentDot1qMrpMmrpPortPktTxFailure,'hm2AgentDot1qMrpMmrpDynamicAddrCount':hm2AgentDot1qMrpMmrpDynamicAddrCount})