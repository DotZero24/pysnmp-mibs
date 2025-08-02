_T='mstpXstPortState'
_S='disabled'
_R='mstpXstPortXstId'
_Q='mstpMapVlanRangeIndex'
_P='mstpMapMSTiID'
_O='mstpPortIndex'
_N='nonStp'
_M='DisplayString'
_L='OctetString'
_K='read-create'
_J='not-accessible'
_I='mstpXstPortIndex'
_H='unknown'
_G='mstpXstId'
_F='Timeout'
_E='FORCE10-MSTP-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dBridge=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_F,'dot1dBridge')
f10Experiment,=mibBuilder.importSymbols('FORCE10-SMI','f10Experiment')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TruthValue')
f10Mstp=ModuleIdentity((1,3,6,1,4,1,6027,20,2))
class PortIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class PortIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class MstiInstanceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
class BpduCounter(TextualConvention,Counter32):status=_A;displayHint='d'
class MstiOrCistInstanceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
class PortId(TextualConvention,OctetString):status=_A;displayHint='d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MstpTraps_ObjectIdentity=ObjectIdentity
mstpTraps=_MstpTraps_ObjectIdentity((1,3,6,1,4,1,6027,20,2,0))
_MstpGen_ObjectIdentity=ObjectIdentity
mstpGen=_MstpGen_ObjectIdentity((1,3,6,1,4,1,6027,20,2,10))
class _MstpGenBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_MstpGenBridgeMaxAge_Type.__name__=_F
_MstpGenBridgeMaxAge_Object=MibScalar
mstpGenBridgeMaxAge=_MstpGenBridgeMaxAge_Object((1,3,6,1,4,1,6027,20,2,10,2),_MstpGenBridgeMaxAge_Type())
mstpGenBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenBridgeMaxAge.setStatus(_A)
class _MstpGenBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_MstpGenBridgeHelloTime_Type.__name__=_F
_MstpGenBridgeHelloTime_Object=MibScalar
mstpGenBridgeHelloTime=_MstpGenBridgeHelloTime_Object((1,3,6,1,4,1,6027,20,2,10,3),_MstpGenBridgeHelloTime_Type())
mstpGenBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenBridgeHelloTime.setStatus(_A)
class _MstpGenBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_MstpGenBridgeForwardDelay_Type.__name__=_F
_MstpGenBridgeForwardDelay_Object=MibScalar
mstpGenBridgeForwardDelay=_MstpGenBridgeForwardDelay_Object((1,3,6,1,4,1,6027,20,2,10,4),_MstpGenBridgeForwardDelay_Type())
mstpGenBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenBridgeForwardDelay.setStatus(_A)
class _MstpGenMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_MstpGenMaxAge_Type.__name__=_F
_MstpGenMaxAge_Object=MibScalar
mstpGenMaxAge=_MstpGenMaxAge_Object((1,3,6,1,4,1,6027,20,2,10,8),_MstpGenMaxAge_Type())
mstpGenMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenMaxAge.setStatus(_A)
class _MstpGenHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_MstpGenHelloTime_Type.__name__=_F
_MstpGenHelloTime_Object=MibScalar
mstpGenHelloTime=_MstpGenHelloTime_Object((1,3,6,1,4,1,6027,20,2,10,9),_MstpGenHelloTime_Type())
mstpGenHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenHelloTime.setStatus(_A)
class _MstpGenForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_MstpGenForwardDelay_Type.__name__=_F
_MstpGenForwardDelay_Object=MibScalar
mstpGenForwardDelay=_MstpGenForwardDelay_Object((1,3,6,1,4,1,6027,20,2,10,10),_MstpGenForwardDelay_Type())
mstpGenForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenForwardDelay.setStatus(_A)
class _MstpGenMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_MstpGenMaxHops_Type.__name__=_D
_MstpGenMaxHops_Object=MibScalar
mstpGenMaxHops=_MstpGenMaxHops_Object((1,3,6,1,4,1,6027,20,2,10,14),_MstpGenMaxHops_Type())
mstpGenMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenMaxHops.setStatus(_A)
class _MstpGenHoldTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_MstpGenHoldTime_Type.__name__=_F
_MstpGenHoldTime_Object=MibScalar
mstpGenHoldTime=_MstpGenHoldTime_Object((1,3,6,1,4,1,6027,20,2,10,15),_MstpGenHoldTime_Type())
mstpGenHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenHoldTime.setStatus(_A)
class _MstpGenMigrateTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_MstpGenMigrateTime_Type.__name__=_F
_MstpGenMigrateTime_Object=MibScalar
mstpGenMigrateTime=_MstpGenMigrateTime_Object((1,3,6,1,4,1,6027,20,2,10,16),_MstpGenMigrateTime_Type())
mstpGenMigrateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenMigrateTime.setStatus(_A)
class _MstpGenPathCostDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pathCostDefault8021d1998',1),('pathCostDefault8021t2001',2)))
_MstpGenPathCostDefault_Type.__name__=_D
_MstpGenPathCostDefault_Object=MibScalar
mstpGenPathCostDefault=_MstpGenPathCostDefault_Object((1,3,6,1,4,1,6027,20,2,10,18),_MstpGenPathCostDefault_Type())
mstpGenPathCostDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenPathCostDefault.setStatus(_A)
class _MstpGenCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_N,0),('dot1d1998',1),('dot1w',2),('dot1d2004',3),('dot1s',4),('dot1q',5),(_H,6)))
_MstpGenCapable_Type.__name__=_D
_MstpGenCapable_Object=MibScalar
mstpGenCapable=_MstpGenCapable_Object((1,3,6,1,4,1,6027,20,2,10,19),_MstpGenCapable_Type())
mstpGenCapable.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenCapable.setStatus(_A)
class _MstpGenForceVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('forceNonStp',0),('forceLegacyDot1d',1),('forceDot1w',2),('autoDot1s',3),(_H,4)))
_MstpGenForceVersion_Type.__name__=_D
_MstpGenForceVersion_Object=MibScalar
mstpGenForceVersion=_MstpGenForceVersion_Object((1,3,6,1,4,1,6027,20,2,10,20),_MstpGenForceVersion_Type())
mstpGenForceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenForceVersion.setStatus(_A)
_MstpGenCfgIdFmtSel_Type=Integer32
_MstpGenCfgIdFmtSel_Object=MibScalar
mstpGenCfgIdFmtSel=_MstpGenCfgIdFmtSel_Object((1,3,6,1,4,1,6027,20,2,10,30),_MstpGenCfgIdFmtSel_Type())
mstpGenCfgIdFmtSel.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenCfgIdFmtSel.setStatus(_A)
class _MstpGenCfgIdName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_MstpGenCfgIdName_Type.__name__=_M
_MstpGenCfgIdName_Object=MibScalar
mstpGenCfgIdName=_MstpGenCfgIdName_Object((1,3,6,1,4,1,6027,20,2,10,31),_MstpGenCfgIdName_Type())
mstpGenCfgIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenCfgIdName.setStatus(_A)
_MstpGenCfgIdRevLevel_Type=Integer32
_MstpGenCfgIdRevLevel_Object=MibScalar
mstpGenCfgIdRevLevel=_MstpGenCfgIdRevLevel_Object((1,3,6,1,4,1,6027,20,2,10,32),_MstpGenCfgIdRevLevel_Type())
mstpGenCfgIdRevLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpGenCfgIdRevLevel.setStatus(_A)
class _MstpGenCfgIdDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MstpGenCfgIdDigest_Type.__name__=_L
_MstpGenCfgIdDigest_Object=MibScalar
mstpGenCfgIdDigest=_MstpGenCfgIdDigest_Object((1,3,6,1,4,1,6027,20,2,10,33),_MstpGenCfgIdDigest_Type())
mstpGenCfgIdDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenCfgIdDigest.setStatus(_A)
_MstpGenReginalRoot_Type=BridgeId
_MstpGenReginalRoot_Object=MibScalar
mstpGenReginalRoot=_MstpGenReginalRoot_Object((1,3,6,1,4,1,6027,20,2,10,34),_MstpGenReginalRoot_Type())
mstpGenReginalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenReginalRoot.setStatus(_A)
_MstpGenExternalRootCost_Type=Integer32
_MstpGenExternalRootCost_Object=MibScalar
mstpGenExternalRootCost=_MstpGenExternalRootCost_Object((1,3,6,1,4,1,6027,20,2,10,35),_MstpGenExternalRootCost_Type())
mstpGenExternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpGenExternalRootCost.setStatus(_A)
_MstpPortTable_Object=MibTable
mstpPortTable=_MstpPortTable_Object((1,3,6,1,4,1,6027,20,2,11))
if mibBuilder.loadTexts:mstpPortTable.setStatus(_A)
_MstpPortEntry_Object=MibTableRow
mstpPortEntry=_MstpPortEntry_Object((1,3,6,1,4,1,6027,20,2,11,1))
mstpPortEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:mstpPortEntry.setStatus(_A)
_MstpPortIndex_Type=PortIndex
_MstpPortIndex_Object=MibTableColumn
mstpPortIndex=_MstpPortIndex_Object((1,3,6,1,4,1,6027,20,2,11,1,1),_MstpPortIndex_Type())
mstpPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortIndex.setStatus(_A)
_MstpPortAdminMACEnable_Type=TruthValue
_MstpPortAdminMACEnable_Object=MibTableColumn
mstpPortAdminMACEnable=_MstpPortAdminMACEnable_Object((1,3,6,1,4,1,6027,20,2,11,1,2),_MstpPortAdminMACEnable_Type())
mstpPortAdminMACEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAdminMACEnable.setStatus(_A)
_MstpPortOperMACEnable_Type=TruthValue
_MstpPortOperMACEnable_Object=MibTableColumn
mstpPortOperMACEnable=_MstpPortOperMACEnable_Object((1,3,6,1,4,1,6027,20,2,11,1,3),_MstpPortOperMACEnable_Type())
mstpPortOperMACEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortOperMACEnable.setStatus(_A)
_MstpPortUpTime_Type=TimeTicks
_MstpPortUpTime_Object=MibTableColumn
mstpPortUpTime=_MstpPortUpTime_Object((1,3,6,1,4,1,6027,20,2,11,1,4),_MstpPortUpTime_Type())
mstpPortUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortUpTime.setStatus(_A)
class _MstpPortAdminExternalPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_MstpPortAdminExternalPathCost_Type.__name__=_D
_MstpPortAdminExternalPathCost_Object=MibTableColumn
mstpPortAdminExternalPathCost=_MstpPortAdminExternalPathCost_Object((1,3,6,1,4,1,6027,20,2,11,1,5),_MstpPortAdminExternalPathCost_Type())
mstpPortAdminExternalPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAdminExternalPathCost.setStatus(_A)
_MstpPortOperExternalPathCost_Type=Integer32
_MstpPortOperExternalPathCost_Object=MibTableColumn
mstpPortOperExternalPathCost=_MstpPortOperExternalPathCost_Object((1,3,6,1,4,1,6027,20,2,11,1,6),_MstpPortOperExternalPathCost_Type())
mstpPortOperExternalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortOperExternalPathCost.setStatus(_A)
_MstpPortAdminEdge_Type=TruthValue
_MstpPortAdminEdge_Object=MibTableColumn
mstpPortAdminEdge=_MstpPortAdminEdge_Object((1,3,6,1,4,1,6027,20,2,11,1,7),_MstpPortAdminEdge_Type())
mstpPortAdminEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAdminEdge.setStatus(_A)
_MstpPortOperEdge_Type=TruthValue
_MstpPortOperEdge_Object=MibTableColumn
mstpPortOperEdge=_MstpPortOperEdge_Object((1,3,6,1,4,1,6027,20,2,11,1,8),_MstpPortOperEdge_Type())
mstpPortOperEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortOperEdge.setStatus(_A)
_MstpPortAutoEdge_Type=TruthValue
_MstpPortAutoEdge_Object=MibTableColumn
mstpPortAutoEdge=_MstpPortAutoEdge_Object((1,3,6,1,4,1,6027,20,2,11,1,9),_MstpPortAutoEdge_Type())
mstpPortAutoEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAutoEdge.setStatus(_A)
class _MstpPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_MstpPortAdminPointToPoint_Type.__name__=_D
_MstpPortAdminPointToPoint_Object=MibTableColumn
mstpPortAdminPointToPoint=_MstpPortAdminPointToPoint_Object((1,3,6,1,4,1,6027,20,2,11,1,10),_MstpPortAdminPointToPoint_Type())
mstpPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAdminPointToPoint.setStatus(_A)
_MstpPortOperPointToPoint_Type=TruthValue
_MstpPortOperPointToPoint_Object=MibTableColumn
mstpPortOperPointToPoint=_MstpPortOperPointToPoint_Object((1,3,6,1,4,1,6027,20,2,11,1,11),_MstpPortOperPointToPoint_Type())
mstpPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortOperPointToPoint.setStatus(_A)
class _MstpPortHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_MstpPortHelloTime_Type.__name__=_F
_MstpPortHelloTime_Object=MibTableColumn
mstpPortHelloTime=_MstpPortHelloTime_Object((1,3,6,1,4,1,6027,20,2,11,1,12),_MstpPortHelloTime_Type())
mstpPortHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortHelloTime.setStatus(_A)
_MstpPortAdminNonStp_Type=TruthValue
_MstpPortAdminNonStp_Object=MibTableColumn
mstpPortAdminNonStp=_MstpPortAdminNonStp_Object((1,3,6,1,4,1,6027,20,2,11,1,13),_MstpPortAdminNonStp_Type())
mstpPortAdminNonStp.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortAdminNonStp.setStatus(_A)
_MstpPortProtocolMigration_Type=TruthValue
_MstpPortProtocolMigration_Object=MibTableColumn
mstpPortProtocolMigration=_MstpPortProtocolMigration_Object((1,3,6,1,4,1,6027,20,2,11,1,14),_MstpPortProtocolMigration_Type())
mstpPortProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpPortProtocolMigration.setStatus(_A)
_MstpPortRxTcnBpduCounter_Type=BpduCounter
_MstpPortRxTcnBpduCounter_Object=MibTableColumn
mstpPortRxTcnBpduCounter=_MstpPortRxTcnBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,15),_MstpPortRxTcnBpduCounter_Type())
mstpPortRxTcnBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortRxTcnBpduCounter.setStatus(_A)
_MstpPortRxCfgBpduCounter_Type=BpduCounter
_MstpPortRxCfgBpduCounter_Object=MibTableColumn
mstpPortRxCfgBpduCounter=_MstpPortRxCfgBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,16),_MstpPortRxCfgBpduCounter_Type())
mstpPortRxCfgBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortRxCfgBpduCounter.setStatus(_A)
_MstpPortRxRstBpduCounter_Type=BpduCounter
_MstpPortRxRstBpduCounter_Object=MibTableColumn
mstpPortRxRstBpduCounter=_MstpPortRxRstBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,17),_MstpPortRxRstBpduCounter_Type())
mstpPortRxRstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortRxRstBpduCounter.setStatus(_A)
_MstpPortRxMstBpduCounter_Type=BpduCounter
_MstpPortRxMstBpduCounter_Object=MibTableColumn
mstpPortRxMstBpduCounter=_MstpPortRxMstBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,18),_MstpPortRxMstBpduCounter_Type())
mstpPortRxMstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortRxMstBpduCounter.setStatus(_A)
_MstpPortTxTcnBpduCounter_Type=BpduCounter
_MstpPortTxTcnBpduCounter_Object=MibTableColumn
mstpPortTxTcnBpduCounter=_MstpPortTxTcnBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,19),_MstpPortTxTcnBpduCounter_Type())
mstpPortTxTcnBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortTxTcnBpduCounter.setStatus(_A)
_MstpPortTxCfgBpduCounter_Type=BpduCounter
_MstpPortTxCfgBpduCounter_Object=MibTableColumn
mstpPortTxCfgBpduCounter=_MstpPortTxCfgBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,20),_MstpPortTxCfgBpduCounter_Type())
mstpPortTxCfgBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortTxCfgBpduCounter.setStatus(_A)
_MstpPortTxRstBpduCounter_Type=BpduCounter
_MstpPortTxRstBpduCounter_Object=MibTableColumn
mstpPortTxRstBpduCounter=_MstpPortTxRstBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,21),_MstpPortTxRstBpduCounter_Type())
mstpPortTxRstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortTxRstBpduCounter.setStatus(_A)
_MstpPortTxMstBpduCounter_Type=BpduCounter
_MstpPortTxMstBpduCounter_Object=MibTableColumn
mstpPortTxMstBpduCounter=_MstpPortTxMstBpduCounter_Object((1,3,6,1,4,1,6027,20,2,11,1,22),_MstpPortTxMstBpduCounter_Type())
mstpPortTxMstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpPortTxMstBpduCounter.setStatus(_A)
_MstpMapTable_Object=MibTable
mstpMapTable=_MstpMapTable_Object((1,3,6,1,4,1,6027,20,2,12))
if mibBuilder.loadTexts:mstpMapTable.setStatus(_A)
_MstpMapEntry_Object=MibTableRow
mstpMapEntry=_MstpMapEntry_Object((1,3,6,1,4,1,6027,20,2,12,1))
mstpMapEntry.setIndexNames((0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:mstpMapEntry.setStatus(_A)
_MstpMapMSTiID_Type=MstiInstanceIndex
_MstpMapMSTiID_Object=MibTableColumn
mstpMapMSTiID=_MstpMapMSTiID_Object((1,3,6,1,4,1,6027,20,2,12,1,1),_MstpMapMSTiID_Type())
mstpMapMSTiID.setMaxAccess(_J)
if mibBuilder.loadTexts:mstpMapMSTiID.setStatus(_A)
class _MstpMapVlanRangeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MstpMapVlanRangeIndex_Type.__name__=_D
_MstpMapVlanRangeIndex_Object=MibTableColumn
mstpMapVlanRangeIndex=_MstpMapVlanRangeIndex_Object((1,3,6,1,4,1,6027,20,2,12,1,2),_MstpMapVlanRangeIndex_Type())
mstpMapVlanRangeIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:mstpMapVlanRangeIndex.setStatus(_A)
_MstpMapVlanMin_Type=VlanId
_MstpMapVlanMin_Object=MibTableColumn
mstpMapVlanMin=_MstpMapVlanMin_Object((1,3,6,1,4,1,6027,20,2,12,1,3),_MstpMapVlanMin_Type())
mstpMapVlanMin.setMaxAccess(_K)
if mibBuilder.loadTexts:mstpMapVlanMin.setStatus(_A)
_MstpMapVlanMax_Type=VlanId
_MstpMapVlanMax_Object=MibTableColumn
mstpMapVlanMax=_MstpMapVlanMax_Object((1,3,6,1,4,1,6027,20,2,12,1,4),_MstpMapVlanMax_Type())
mstpMapVlanMax.setMaxAccess(_K)
if mibBuilder.loadTexts:mstpMapVlanMax.setStatus(_A)
_MstpMapRowStatus_Type=RowStatus
_MstpMapRowStatus_Object=MibTableColumn
mstpMapRowStatus=_MstpMapRowStatus_Object((1,3,6,1,4,1,6027,20,2,12,1,9),_MstpMapRowStatus_Type())
mstpMapRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:mstpMapRowStatus.setStatus(_A)
_MstpXstTable_Object=MibTable
mstpXstTable=_MstpXstTable_Object((1,3,6,1,4,1,6027,20,2,13))
if mibBuilder.loadTexts:mstpXstTable.setStatus(_A)
_MstpXstEntry_Object=MibTableRow
mstpXstEntry=_MstpXstEntry_Object((1,3,6,1,4,1,6027,20,2,13,1))
mstpXstEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:mstpXstEntry.setStatus(_A)
_MstpXstId_Type=MstiOrCistInstanceIndex
_MstpXstId_Object=MibTableColumn
mstpXstId=_MstpXstId_Object((1,3,6,1,4,1,6027,20,2,13,1,1),_MstpXstId_Type())
mstpXstId.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstId.setStatus(_A)
class _MstpXstBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_MstpXstBridgePriority_Type.__name__=_D
_MstpXstBridgePriority_Object=MibTableColumn
mstpXstBridgePriority=_MstpXstBridgePriority_Object((1,3,6,1,4,1,6027,20,2,13,1,2),_MstpXstBridgePriority_Type())
mstpXstBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpXstBridgePriority.setStatus(_A)
_MstpXstBridgeId_Type=BridgeId
_MstpXstBridgeId_Object=MibTableColumn
mstpXstBridgeId=_MstpXstBridgeId_Object((1,3,6,1,4,1,6027,20,2,13,1,3),_MstpXstBridgeId_Type())
mstpXstBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstBridgeId.setStatus(_A)
_MstpXstDesignatedRoot_Type=BridgeId
_MstpXstDesignatedRoot_Object=MibTableColumn
mstpXstDesignatedRoot=_MstpXstDesignatedRoot_Object((1,3,6,1,4,1,6027,20,2,13,1,4),_MstpXstDesignatedRoot_Type())
mstpXstDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstDesignatedRoot.setStatus(_A)
_MstpXstDesignatedBridge_Type=BridgeId
_MstpXstDesignatedBridge_Object=MibTableColumn
mstpXstDesignatedBridge=_MstpXstDesignatedBridge_Object((1,3,6,1,4,1,6027,20,2,13,1,5),_MstpXstDesignatedBridge_Type())
mstpXstDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstDesignatedBridge.setStatus(_A)
_MstpXstInternalRootCost_Type=Integer32
_MstpXstInternalRootCost_Object=MibTableColumn
mstpXstInternalRootCost=_MstpXstInternalRootCost_Object((1,3,6,1,4,1,6027,20,2,13,1,6),_MstpXstInternalRootCost_Type())
mstpXstInternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstInternalRootCost.setStatus(_A)
_MstpXstRootPort_Type=PortIndexOrZero
_MstpXstRootPort_Object=MibTableColumn
mstpXstRootPort=_MstpXstRootPort_Object((1,3,6,1,4,1,6027,20,2,13,1,7),_MstpXstRootPort_Type())
mstpXstRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstRootPort.setStatus(_A)
_MstpXstMasterPort_Type=PortIndexOrZero
_MstpXstMasterPort_Object=MibTableColumn
mstpXstMasterPort=_MstpXstMasterPort_Object((1,3,6,1,4,1,6027,20,2,13,1,8),_MstpXstMasterPort_Type())
mstpXstMasterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstMasterPort.setStatus(_A)
_MstpXstTimeSinceTopologyChange_Type=TimeTicks
_MstpXstTimeSinceTopologyChange_Object=MibTableColumn
mstpXstTimeSinceTopologyChange=_MstpXstTimeSinceTopologyChange_Object((1,3,6,1,4,1,6027,20,2,13,1,11),_MstpXstTimeSinceTopologyChange_Type())
mstpXstTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstTimeSinceTopologyChange.setStatus(_A)
_MstpXstTopologyChangesCount_Type=Counter32
_MstpXstTopologyChangesCount_Object=MibTableColumn
mstpXstTopologyChangesCount=_MstpXstTopologyChangesCount_Object((1,3,6,1,4,1,6027,20,2,13,1,12),_MstpXstTopologyChangesCount_Type())
mstpXstTopologyChangesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstTopologyChangesCount.setStatus(_A)
_MstpXstTopologyChangeFlag_Type=TruthValue
_MstpXstTopologyChangeFlag_Object=MibTableColumn
mstpXstTopologyChangeFlag=_MstpXstTopologyChangeFlag_Object((1,3,6,1,4,1,6027,20,2,13,1,13),_MstpXstTopologyChangeFlag_Type())
mstpXstTopologyChangeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstTopologyChangeFlag.setStatus(_A)
_MstpXstPortTable_Object=MibTable
mstpXstPortTable=_MstpXstPortTable_Object((1,3,6,1,4,1,6027,20,2,14))
if mibBuilder.loadTexts:mstpXstPortTable.setStatus(_A)
_MstpXstPortEntry_Object=MibTableRow
mstpXstPortEntry=_MstpXstPortEntry_Object((1,3,6,1,4,1,6027,20,2,14,1))
mstpXstPortEntry.setIndexNames((0,_E,_R),(0,_E,_I))
if mibBuilder.loadTexts:mstpXstPortEntry.setStatus(_A)
_MstpXstPortXstId_Type=MstiOrCistInstanceIndex
_MstpXstPortXstId_Object=MibTableColumn
mstpXstPortXstId=_MstpXstPortXstId_Object((1,3,6,1,4,1,6027,20,2,14,1,1),_MstpXstPortXstId_Type())
mstpXstPortXstId.setMaxAccess(_J)
if mibBuilder.loadTexts:mstpXstPortXstId.setStatus(_A)
_MstpXstPortIndex_Type=PortIndex
_MstpXstPortIndex_Object=MibTableColumn
mstpXstPortIndex=_MstpXstPortIndex_Object((1,3,6,1,4,1,6027,20,2,14,1,2),_MstpXstPortIndex_Type())
mstpXstPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortIndex.setStatus(_A)
class _MstpXstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('discarding',2),('learning',3),('forwarding',4),(_H,5)))
_MstpXstPortState_Type.__name__=_D
_MstpXstPortState_Object=MibTableColumn
mstpXstPortState=_MstpXstPortState_Object((1,3,6,1,4,1,6027,20,2,14,1,3),_MstpXstPortState_Type())
mstpXstPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortState.setStatus(_A)
class _MstpXstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,1),('alternate',2),('backup',3),('root',4),('designated',5),('master',6),(_N,7),(_H,8)))
_MstpXstPortRole_Type.__name__=_D
_MstpXstPortRole_Object=MibTableColumn
mstpXstPortRole=_MstpXstPortRole_Object((1,3,6,1,4,1,6027,20,2,14,1,4),_MstpXstPortRole_Type())
mstpXstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortRole.setStatus(_A)
_MstpXstPortDesignatedRoot_Type=BridgeId
_MstpXstPortDesignatedRoot_Object=MibTableColumn
mstpXstPortDesignatedRoot=_MstpXstPortDesignatedRoot_Object((1,3,6,1,4,1,6027,20,2,14,1,6),_MstpXstPortDesignatedRoot_Type())
mstpXstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortDesignatedRoot.setStatus(_A)
_MstpXstPortExternalRootCost_Type=Integer32
_MstpXstPortExternalRootCost_Object=MibTableColumn
mstpXstPortExternalRootCost=_MstpXstPortExternalRootCost_Object((1,3,6,1,4,1,6027,20,2,14,1,7),_MstpXstPortExternalRootCost_Type())
mstpXstPortExternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortExternalRootCost.setStatus(_A)
_MstpXstPortRegionalBridge_Type=BridgeId
_MstpXstPortRegionalBridge_Object=MibTableColumn
mstpXstPortRegionalBridge=_MstpXstPortRegionalBridge_Object((1,3,6,1,4,1,6027,20,2,14,1,8),_MstpXstPortRegionalBridge_Type())
mstpXstPortRegionalBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortRegionalBridge.setStatus(_A)
_MstpXstPortInternalRootCost_Type=Integer32
_MstpXstPortInternalRootCost_Object=MibTableColumn
mstpXstPortInternalRootCost=_MstpXstPortInternalRootCost_Object((1,3,6,1,4,1,6027,20,2,14,1,9),_MstpXstPortInternalRootCost_Type())
mstpXstPortInternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortInternalRootCost.setStatus(_A)
_MstpXstPortDesignatedBridge_Type=BridgeId
_MstpXstPortDesignatedBridge_Object=MibTableColumn
mstpXstPortDesignatedBridge=_MstpXstPortDesignatedBridge_Object((1,3,6,1,4,1,6027,20,2,14,1,10),_MstpXstPortDesignatedBridge_Type())
mstpXstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortDesignatedBridge.setStatus(_A)
_MstpXstPortDesignatedPort_Type=PortId
_MstpXstPortDesignatedPort_Object=MibTableColumn
mstpXstPortDesignatedPort=_MstpXstPortDesignatedPort_Object((1,3,6,1,4,1,6027,20,2,14,1,14),_MstpXstPortDesignatedPort_Type())
mstpXstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortDesignatedPort.setStatus(_A)
class _MstpXstPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MstpXstPortPriority_Type.__name__=_D
_MstpXstPortPriority_Object=MibTableColumn
mstpXstPortPriority=_MstpXstPortPriority_Object((1,3,6,1,4,1,6027,20,2,14,1,15),_MstpXstPortPriority_Type())
mstpXstPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpXstPortPriority.setStatus(_A)
class _MstpXstPortAdminInternalPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_MstpXstPortAdminInternalPathCost_Type.__name__=_D
_MstpXstPortAdminInternalPathCost_Object=MibTableColumn
mstpXstPortAdminInternalPathCost=_MstpXstPortAdminInternalPathCost_Object((1,3,6,1,4,1,6027,20,2,14,1,16),_MstpXstPortAdminInternalPathCost_Type())
mstpXstPortAdminInternalPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpXstPortAdminInternalPathCost.setStatus(_A)
_MstpXstPortOperInternalPathCost_Type=Integer32
_MstpXstPortOperInternalPathCost_Object=MibTableColumn
mstpXstPortOperInternalPathCost=_MstpXstPortOperInternalPathCost_Object((1,3,6,1,4,1,6027,20,2,14,1,17),_MstpXstPortOperInternalPathCost_Type())
mstpXstPortOperInternalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:mstpXstPortOperInternalPathCost.setStatus(_A)
mstpNewRootBridge=NotificationType((1,3,6,1,4,1,6027,20,2,0,1))
mstpNewRootBridge.setObjects((_E,_G))
if mibBuilder.loadTexts:mstpNewRootBridge.setStatus(_A)
mstpNewRootPort=NotificationType((1,3,6,1,4,1,6027,20,2,0,2))
mstpNewRootPort.setObjects(*((_E,_G),(_E,_I)))
if mibBuilder.loadTexts:mstpNewRootPort.setStatus(_A)
mstpTopologyChange=NotificationType((1,3,6,1,4,1,6027,20,2,0,3))
mstpTopologyChange.setObjects(*((_E,_G),(_E,_I),(_E,_T)))
if mibBuilder.loadTexts:mstpTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PortIndex':PortIndex,'PortIndexOrZero':PortIndexOrZero,'MstiInstanceIndex':MstiInstanceIndex,'BpduCounter':BpduCounter,'MstiOrCistInstanceIndex':MstiOrCistInstanceIndex,'PortId':PortId,'f10Mstp':f10Mstp,'mstpTraps':mstpTraps,'mstpNewRootBridge':mstpNewRootBridge,'mstpNewRootPort':mstpNewRootPort,'mstpTopologyChange':mstpTopologyChange,'mstpGen':mstpGen,'mstpGenBridgeMaxAge':mstpGenBridgeMaxAge,'mstpGenBridgeHelloTime':mstpGenBridgeHelloTime,'mstpGenBridgeForwardDelay':mstpGenBridgeForwardDelay,'mstpGenMaxAge':mstpGenMaxAge,'mstpGenHelloTime':mstpGenHelloTime,'mstpGenForwardDelay':mstpGenForwardDelay,'mstpGenMaxHops':mstpGenMaxHops,'mstpGenHoldTime':mstpGenHoldTime,'mstpGenMigrateTime':mstpGenMigrateTime,'mstpGenPathCostDefault':mstpGenPathCostDefault,'mstpGenCapable':mstpGenCapable,'mstpGenForceVersion':mstpGenForceVersion,'mstpGenCfgIdFmtSel':mstpGenCfgIdFmtSel,'mstpGenCfgIdName':mstpGenCfgIdName,'mstpGenCfgIdRevLevel':mstpGenCfgIdRevLevel,'mstpGenCfgIdDigest':mstpGenCfgIdDigest,'mstpGenReginalRoot':mstpGenReginalRoot,'mstpGenExternalRootCost':mstpGenExternalRootCost,'mstpPortTable':mstpPortTable,'mstpPortEntry':mstpPortEntry,_O:mstpPortIndex,'mstpPortAdminMACEnable':mstpPortAdminMACEnable,'mstpPortOperMACEnable':mstpPortOperMACEnable,'mstpPortUpTime':mstpPortUpTime,'mstpPortAdminExternalPathCost':mstpPortAdminExternalPathCost,'mstpPortOperExternalPathCost':mstpPortOperExternalPathCost,'mstpPortAdminEdge':mstpPortAdminEdge,'mstpPortOperEdge':mstpPortOperEdge,'mstpPortAutoEdge':mstpPortAutoEdge,'mstpPortAdminPointToPoint':mstpPortAdminPointToPoint,'mstpPortOperPointToPoint':mstpPortOperPointToPoint,'mstpPortHelloTime':mstpPortHelloTime,'mstpPortAdminNonStp':mstpPortAdminNonStp,'mstpPortProtocolMigration':mstpPortProtocolMigration,'mstpPortRxTcnBpduCounter':mstpPortRxTcnBpduCounter,'mstpPortRxCfgBpduCounter':mstpPortRxCfgBpduCounter,'mstpPortRxRstBpduCounter':mstpPortRxRstBpduCounter,'mstpPortRxMstBpduCounter':mstpPortRxMstBpduCounter,'mstpPortTxTcnBpduCounter':mstpPortTxTcnBpduCounter,'mstpPortTxCfgBpduCounter':mstpPortTxCfgBpduCounter,'mstpPortTxRstBpduCounter':mstpPortTxRstBpduCounter,'mstpPortTxMstBpduCounter':mstpPortTxMstBpduCounter,'mstpMapTable':mstpMapTable,'mstpMapEntry':mstpMapEntry,_P:mstpMapMSTiID,_Q:mstpMapVlanRangeIndex,'mstpMapVlanMin':mstpMapVlanMin,'mstpMapVlanMax':mstpMapVlanMax,'mstpMapRowStatus':mstpMapRowStatus,'mstpXstTable':mstpXstTable,'mstpXstEntry':mstpXstEntry,_G:mstpXstId,'mstpXstBridgePriority':mstpXstBridgePriority,'mstpXstBridgeId':mstpXstBridgeId,'mstpXstDesignatedRoot':mstpXstDesignatedRoot,'mstpXstDesignatedBridge':mstpXstDesignatedBridge,'mstpXstInternalRootCost':mstpXstInternalRootCost,'mstpXstRootPort':mstpXstRootPort,'mstpXstMasterPort':mstpXstMasterPort,'mstpXstTimeSinceTopologyChange':mstpXstTimeSinceTopologyChange,'mstpXstTopologyChangesCount':mstpXstTopologyChangesCount,'mstpXstTopologyChangeFlag':mstpXstTopologyChangeFlag,'mstpXstPortTable':mstpXstPortTable,'mstpXstPortEntry':mstpXstPortEntry,_R:mstpXstPortXstId,_I:mstpXstPortIndex,_T:mstpXstPortState,'mstpXstPortRole':mstpXstPortRole,'mstpXstPortDesignatedRoot':mstpXstPortDesignatedRoot,'mstpXstPortExternalRootCost':mstpXstPortExternalRootCost,'mstpXstPortRegionalBridge':mstpXstPortRegionalBridge,'mstpXstPortInternalRootCost':mstpXstPortInternalRootCost,'mstpXstPortDesignatedBridge':mstpXstPortDesignatedBridge,'mstpXstPortDesignatedPort':mstpXstPortDesignatedPort,'mstpXstPortPriority':mstpXstPortPriority,'mstpXstPortAdminInternalPathCost':mstpXstPortAdminInternalPathCost,'mstpXstPortOperInternalPathCost':mstpXstPortOperInternalPathCost})