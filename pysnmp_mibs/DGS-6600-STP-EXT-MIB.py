_S='swMSTPPortRestrictedRole'
_R='swMSTPPortOperFilterBpdu'
_Q='swMSTPInstId'
_P='swMSTPMstPortInsID'
_O='swMSTPMstPort'
_N='auto'
_M='false'
_L='true'
_K='swMSTPPort'
_J='other'
_I='enabled'
_H='disabled'
_G='read-create'
_F='OctetString'
_E='DGS-6600-STP-EXT-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dgs6600_l2,=mibBuilder.importSymbols('DGS-6600-ID-MIB','dgs6600-l2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
dgs6600StpExtMIB=ModuleIdentity((1,3,6,1,4,1,171,10,120,100,2,2))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_SwMSTPGblMgmt_ObjectIdentity=ObjectIdentity
swMSTPGblMgmt=_SwMSTPGblMgmt_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,2,2,1))
class _SwMSTPStpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwMSTPStpAdminState_Type.__name__=_B
_SwMSTPStpAdminState_Object=MibScalar
swMSTPStpAdminState=_SwMSTPStpAdminState_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,1),_SwMSTPStpAdminState_Type())
swMSTPStpAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpAdminState.setStatus(_A)
class _SwMSTPStpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('stp',0),('rstp',1),('mstp',2)))
_SwMSTPStpVersion_Type.__name__=_B
_SwMSTPStpVersion_Object=MibScalar
swMSTPStpVersion=_SwMSTPStpVersion_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,2),_SwMSTPStpVersion_Type())
swMSTPStpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpVersion.setStatus(_A)
class _SwMSTPStpMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_SwMSTPStpMaxAge_Type.__name__=_B
_SwMSTPStpMaxAge_Object=MibScalar
swMSTPStpMaxAge=_SwMSTPStpMaxAge_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,3),_SwMSTPStpMaxAge_Type())
swMSTPStpMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpMaxAge.setStatus(_A)
class _SwMSTPStpHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_SwMSTPStpHelloTime_Type.__name__=_B
_SwMSTPStpHelloTime_Object=MibScalar
swMSTPStpHelloTime=_SwMSTPStpHelloTime_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,4),_SwMSTPStpHelloTime_Type())
swMSTPStpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpHelloTime.setStatus(_A)
class _SwMSTPStpForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_SwMSTPStpForwardDelay_Type.__name__=_B
_SwMSTPStpForwardDelay_Object=MibScalar
swMSTPStpForwardDelay=_SwMSTPStpForwardDelay_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,5),_SwMSTPStpForwardDelay_Type())
swMSTPStpForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpForwardDelay.setStatus(_A)
class _SwMSTPStpMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_SwMSTPStpMaxHops_Type.__name__=_B
_SwMSTPStpMaxHops_Object=MibScalar
swMSTPStpMaxHops=_SwMSTPStpMaxHops_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,6),_SwMSTPStpMaxHops_Type())
swMSTPStpMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpMaxHops.setStatus(_A)
class _SwMSTPStpTxHoldCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SwMSTPStpTxHoldCount_Type.__name__=_B
_SwMSTPStpTxHoldCount_Object=MibScalar
swMSTPStpTxHoldCount=_SwMSTPStpTxHoldCount_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,7),_SwMSTPStpTxHoldCount_Type())
swMSTPStpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpTxHoldCount.setStatus(_A)
class _SwMSTPStpForwardBPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwMSTPStpForwardBPDU_Type.__name__=_B
_SwMSTPStpForwardBPDU_Object=MibScalar
swMSTPStpForwardBPDU=_SwMSTPStpForwardBPDU_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,8),_SwMSTPStpForwardBPDU_Type())
swMSTPStpForwardBPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpForwardBPDU.setStatus(_A)
class _SwMSTPStpLBD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwMSTPStpLBD_Type.__name__=_B
_SwMSTPStpLBD_Object=MibScalar
swMSTPStpLBD=_SwMSTPStpLBD_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,9),_SwMSTPStpLBD_Type())
swMSTPStpLBD.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpLBD.setStatus(_A)
class _SwMSTPStpLBDRecoverTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SwMSTPStpLBDRecoverTime_Type.__name__=_B
_SwMSTPStpLBDRecoverTime_Object=MibScalar
swMSTPStpLBDRecoverTime=_SwMSTPStpLBDRecoverTime_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,10),_SwMSTPStpLBDRecoverTime_Type())
swMSTPStpLBDRecoverTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPStpLBDRecoverTime.setStatus(_A)
class _SwMSTPNniBPDUAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1d',1),('dot1ad',2)))
_SwMSTPNniBPDUAddress_Type.__name__=_B
_SwMSTPNniBPDUAddress_Object=MibScalar
swMSTPNniBPDUAddress=_SwMSTPNniBPDUAddress_Object((1,3,6,1,4,1,171,10,120,100,2,2,1,11),_SwMSTPNniBPDUAddress_Type())
swMSTPNniBPDUAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPNniBPDUAddress.setStatus(_A)
_SwMSTPCtrl_ObjectIdentity=ObjectIdentity
swMSTPCtrl=_SwMSTPCtrl_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,2,2,2))
class _SwMSTPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwMSTPName_Type.__name__=_F
_SwMSTPName_Object=MibScalar
swMSTPName=_SwMSTPName_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,1),_SwMSTPName_Type())
swMSTPName.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPName.setStatus(_A)
class _SwMSTPRevisionLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwMSTPRevisionLevel_Type.__name__=_B
_SwMSTPRevisionLevel_Object=MibScalar
swMSTPRevisionLevel=_SwMSTPRevisionLevel_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,2),_SwMSTPRevisionLevel_Type())
swMSTPRevisionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPRevisionLevel.setStatus(_A)
_SwMSTPInstanceCtrlTable_Object=MibTable
swMSTPInstanceCtrlTable=_SwMSTPInstanceCtrlTable_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3))
if mibBuilder.loadTexts:swMSTPInstanceCtrlTable.setStatus(_A)
_SwMSTPInstanceCtrlEntry_Object=MibTableRow
swMSTPInstanceCtrlEntry=_SwMSTPInstanceCtrlEntry_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1))
swMSTPInstanceCtrlEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:swMSTPInstanceCtrlEntry.setStatus(_A)
class _SwMSTPInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwMSTPInstId_Type.__name__=_B
_SwMSTPInstId_Object=MibTableColumn
swMSTPInstId=_SwMSTPInstId_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,1),_SwMSTPInstId_Type())
swMSTPInstId.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstId.setStatus(_A)
class _SwMSTPInstVlanRangeList1to64_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList1to64_Type.__name__=_F
_SwMSTPInstVlanRangeList1to64_Object=MibTableColumn
swMSTPInstVlanRangeList1to64=_SwMSTPInstVlanRangeList1to64_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,2),_SwMSTPInstVlanRangeList1to64_Type())
swMSTPInstVlanRangeList1to64.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList1to64.setStatus(_A)
class _SwMSTPInstVlanRangeList65to128_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList65to128_Type.__name__=_F
_SwMSTPInstVlanRangeList65to128_Object=MibTableColumn
swMSTPInstVlanRangeList65to128=_SwMSTPInstVlanRangeList65to128_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,3),_SwMSTPInstVlanRangeList65to128_Type())
swMSTPInstVlanRangeList65to128.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList65to128.setStatus(_A)
class _SwMSTPInstVlanRangeList129to192_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList129to192_Type.__name__=_F
_SwMSTPInstVlanRangeList129to192_Object=MibTableColumn
swMSTPInstVlanRangeList129to192=_SwMSTPInstVlanRangeList129to192_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,4),_SwMSTPInstVlanRangeList129to192_Type())
swMSTPInstVlanRangeList129to192.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList129to192.setStatus(_A)
class _SwMSTPInstVlanRangeList193to256_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList193to256_Type.__name__=_F
_SwMSTPInstVlanRangeList193to256_Object=MibTableColumn
swMSTPInstVlanRangeList193to256=_SwMSTPInstVlanRangeList193to256_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,5),_SwMSTPInstVlanRangeList193to256_Type())
swMSTPInstVlanRangeList193to256.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList193to256.setStatus(_A)
class _SwMSTPInstVlanRangeList257to320_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList257to320_Type.__name__=_F
_SwMSTPInstVlanRangeList257to320_Object=MibTableColumn
swMSTPInstVlanRangeList257to320=_SwMSTPInstVlanRangeList257to320_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,6),_SwMSTPInstVlanRangeList257to320_Type())
swMSTPInstVlanRangeList257to320.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList257to320.setStatus(_A)
class _SwMSTPInstVlanRangeList321to384_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList321to384_Type.__name__=_F
_SwMSTPInstVlanRangeList321to384_Object=MibTableColumn
swMSTPInstVlanRangeList321to384=_SwMSTPInstVlanRangeList321to384_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,7),_SwMSTPInstVlanRangeList321to384_Type())
swMSTPInstVlanRangeList321to384.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList321to384.setStatus(_A)
class _SwMSTPInstVlanRangeList385to448_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList385to448_Type.__name__=_F
_SwMSTPInstVlanRangeList385to448_Object=MibTableColumn
swMSTPInstVlanRangeList385to448=_SwMSTPInstVlanRangeList385to448_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,8),_SwMSTPInstVlanRangeList385to448_Type())
swMSTPInstVlanRangeList385to448.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList385to448.setStatus(_A)
class _SwMSTPInstVlanRangeList449to512_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SwMSTPInstVlanRangeList449to512_Type.__name__=_F
_SwMSTPInstVlanRangeList449to512_Object=MibTableColumn
swMSTPInstVlanRangeList449to512=_SwMSTPInstVlanRangeList449to512_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,9),_SwMSTPInstVlanRangeList449to512_Type())
swMSTPInstVlanRangeList449to512.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstVlanRangeList449to512.setStatus(_A)
class _SwMSTPInstType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cist',0),('msti',1)))
_SwMSTPInstType_Type.__name__=_B
_SwMSTPInstType_Object=MibTableColumn
swMSTPInstType=_SwMSTPInstType_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,10),_SwMSTPInstType_Type())
swMSTPInstType.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstType.setStatus(_A)
class _SwMSTPInstStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SwMSTPInstStatus_Type.__name__=_B
_SwMSTPInstStatus_Object=MibTableColumn
swMSTPInstStatus=_SwMSTPInstStatus_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,11),_SwMSTPInstStatus_Type())
swMSTPInstStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstStatus.setStatus(_A)
class _SwMSTPInstPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_SwMSTPInstPriority_Type.__name__=_B
_SwMSTPInstPriority_Object=MibTableColumn
swMSTPInstPriority=_SwMSTPInstPriority_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,12),_SwMSTPInstPriority_Type())
swMSTPInstPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstPriority.setStatus(_A)
_SwMSTPInstDesignatedRootBridge_Type=BridgeId
_SwMSTPInstDesignatedRootBridge_Object=MibTableColumn
swMSTPInstDesignatedRootBridge=_SwMSTPInstDesignatedRootBridge_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,13),_SwMSTPInstDesignatedRootBridge_Type())
swMSTPInstDesignatedRootBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstDesignatedRootBridge.setStatus(_A)
_SwMSTPInstExternalRootCost_Type=Integer32
_SwMSTPInstExternalRootCost_Object=MibTableColumn
swMSTPInstExternalRootCost=_SwMSTPInstExternalRootCost_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,14),_SwMSTPInstExternalRootCost_Type())
swMSTPInstExternalRootCost.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstExternalRootCost.setStatus(_A)
_SwMSTPInstRegionalRootBridge_Type=BridgeId
_SwMSTPInstRegionalRootBridge_Object=MibTableColumn
swMSTPInstRegionalRootBridge=_SwMSTPInstRegionalRootBridge_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,15),_SwMSTPInstRegionalRootBridge_Type())
swMSTPInstRegionalRootBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstRegionalRootBridge.setStatus(_A)
_SwMSTPInstInternalRootCost_Type=Integer32
_SwMSTPInstInternalRootCost_Object=MibTableColumn
swMSTPInstInternalRootCost=_SwMSTPInstInternalRootCost_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,16),_SwMSTPInstInternalRootCost_Type())
swMSTPInstInternalRootCost.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstInternalRootCost.setStatus(_A)
_SwMSTPInstDesignatedBridge_Type=BridgeId
_SwMSTPInstDesignatedBridge_Object=MibTableColumn
swMSTPInstDesignatedBridge=_SwMSTPInstDesignatedBridge_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,17),_SwMSTPInstDesignatedBridge_Type())
swMSTPInstDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstDesignatedBridge.setStatus(_A)
_SwMSTPInstRootPort_Type=Integer32
_SwMSTPInstRootPort_Object=MibTableColumn
swMSTPInstRootPort=_SwMSTPInstRootPort_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,18),_SwMSTPInstRootPort_Type())
swMSTPInstRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstRootPort.setStatus(_A)
_SwMSTPInstMaxAge_Type=Integer32
_SwMSTPInstMaxAge_Object=MibTableColumn
swMSTPInstMaxAge=_SwMSTPInstMaxAge_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,19),_SwMSTPInstMaxAge_Type())
swMSTPInstMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstMaxAge.setStatus(_A)
_SwMSTPInstForwardDelay_Type=Integer32
_SwMSTPInstForwardDelay_Object=MibTableColumn
swMSTPInstForwardDelay=_SwMSTPInstForwardDelay_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,20),_SwMSTPInstForwardDelay_Type())
swMSTPInstForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstForwardDelay.setStatus(_A)
_SwMSTPInstLastTopologyChange_Type=TimeTicks
_SwMSTPInstLastTopologyChange_Object=MibTableColumn
swMSTPInstLastTopologyChange=_SwMSTPInstLastTopologyChange_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,21),_SwMSTPInstLastTopologyChange_Type())
swMSTPInstLastTopologyChange.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstLastTopologyChange.setStatus(_A)
_SwMSTPInstTopChangesCount_Type=Counter32
_SwMSTPInstTopChangesCount_Object=MibTableColumn
swMSTPInstTopChangesCount=_SwMSTPInstTopChangesCount_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,22),_SwMSTPInstTopChangesCount_Type())
swMSTPInstTopChangesCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstTopChangesCount.setStatus(_A)
_SwMSTPInstRemainHops_Type=Integer32
_SwMSTPInstRemainHops_Object=MibTableColumn
swMSTPInstRemainHops=_SwMSTPInstRemainHops_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,23),_SwMSTPInstRemainHops_Type())
swMSTPInstRemainHops.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPInstRemainHops.setStatus(_A)
_SwMSTPInstRowStatus_Type=RowStatus
_SwMSTPInstRowStatus_Object=MibTableColumn
swMSTPInstRowStatus=_SwMSTPInstRowStatus_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,3,1,24),_SwMSTPInstRowStatus_Type())
swMSTPInstRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:swMSTPInstRowStatus.setStatus(_A)
_SwMSTPPortTable_Object=MibTable
swMSTPPortTable=_SwMSTPPortTable_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4))
if mibBuilder.loadTexts:swMSTPPortTable.setStatus(_A)
_SwMSTPPortEntry_Object=MibTableRow
swMSTPPortEntry=_SwMSTPPortEntry_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1))
swMSTPPortEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:swMSTPPortEntry.setStatus(_A)
class _SwMSTPPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwMSTPPort_Type.__name__=_B
_SwMSTPPort_Object=MibTableColumn
swMSTPPort=_SwMSTPPort_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,1),_SwMSTPPort_Type())
swMSTPPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPPort.setStatus(_A)
class _SwMSTPPortAdminHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_SwMSTPPortAdminHelloTime_Type.__name__=_B
_SwMSTPPortAdminHelloTime_Object=MibTableColumn
swMSTPPortAdminHelloTime=_SwMSTPPortAdminHelloTime_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,2),_SwMSTPPortAdminHelloTime_Type())
swMSTPPortAdminHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortAdminHelloTime.setStatus(_A)
class _SwMSTPPortOperHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_SwMSTPPortOperHelloTime_Type.__name__=_B
_SwMSTPPortOperHelloTime_Object=MibTableColumn
swMSTPPortOperHelloTime=_SwMSTPPortOperHelloTime_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,3),_SwMSTPPortOperHelloTime_Type())
swMSTPPortOperHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPPortOperHelloTime.setStatus(_A)
class _SwMSTPSTPPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_H,2)))
_SwMSTPSTPPortEnable_Type.__name__=_B
_SwMSTPSTPPortEnable_Object=MibTableColumn
swMSTPSTPPortEnable=_SwMSTPSTPPortEnable_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,4),_SwMSTPSTPPortEnable_Type())
swMSTPSTPPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPSTPPortEnable.setStatus(_A)
class _SwMSTPPortExternalPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_SwMSTPPortExternalPathCost_Type.__name__=_B
_SwMSTPPortExternalPathCost_Object=MibTableColumn
swMSTPPortExternalPathCost=_SwMSTPPortExternalPathCost_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,5),_SwMSTPPortExternalPathCost_Type())
swMSTPPortExternalPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortExternalPathCost.setStatus(_A)
_SwMSTPPortMigration_Type=TruthValue
_SwMSTPPortMigration_Object=MibTableColumn
swMSTPPortMigration=_SwMSTPPortMigration_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,6),_SwMSTPPortMigration_Type())
swMSTPPortMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortMigration.setStatus(_A)
class _SwMSTPPortAdminEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_SwMSTPPortAdminEdgePort_Type.__name__=_B
_SwMSTPPortAdminEdgePort_Object=MibTableColumn
swMSTPPortAdminEdgePort=_SwMSTPPortAdminEdgePort_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,7),_SwMSTPPortAdminEdgePort_Type())
swMSTPPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortAdminEdgePort.setStatus(_A)
class _SwMSTPPortOperEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3)))
_SwMSTPPortOperEdgePort_Type.__name__=_B
_SwMSTPPortOperEdgePort_Object=MibTableColumn
swMSTPPortOperEdgePort=_SwMSTPPortOperEdgePort_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,8),_SwMSTPPortOperEdgePort_Type())
swMSTPPortOperEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPPortOperEdgePort.setStatus(_A)
class _SwMSTPPortAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_SwMSTPPortAdminP2P_Type.__name__=_B
_SwMSTPPortAdminP2P_Object=MibTableColumn
swMSTPPortAdminP2P=_SwMSTPPortAdminP2P_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,9),_SwMSTPPortAdminP2P_Type())
swMSTPPortAdminP2P.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortAdminP2P.setStatus(_A)
class _SwMSTPPortOperP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_SwMSTPPortOperP2P_Type.__name__=_B
_SwMSTPPortOperP2P_Object=MibTableColumn
swMSTPPortOperP2P=_SwMSTPPortOperP2P_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,10),_SwMSTPPortOperP2P_Type())
swMSTPPortOperP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPPortOperP2P.setStatus(_A)
class _SwMSTPPortLBD_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwMSTPPortLBD_Type.__name__=_B
_SwMSTPPortLBD_Object=MibTableColumn
swMSTPPortLBD=_SwMSTPPortLBD_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,11),_SwMSTPPortLBD_Type())
swMSTPPortLBD.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortLBD.setStatus(_A)
class _SwMSTPPortBPDUFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_H,2),(_I,3)))
_SwMSTPPortBPDUFiltering_Type.__name__=_B
_SwMSTPPortBPDUFiltering_Object=MibTableColumn
swMSTPPortBPDUFiltering=_SwMSTPPortBPDUFiltering_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,12),_SwMSTPPortBPDUFiltering_Type())
swMSTPPortBPDUFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortBPDUFiltering.setStatus(_A)
_SwMSTPPortRestrictedRole_Type=TruthValue
_SwMSTPPortRestrictedRole_Object=MibTableColumn
swMSTPPortRestrictedRole=_SwMSTPPortRestrictedRole_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,13),_SwMSTPPortRestrictedRole_Type())
swMSTPPortRestrictedRole.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortRestrictedRole.setStatus(_A)
_SwMSTPPortRestrictedTCN_Type=TruthValue
_SwMSTPPortRestrictedTCN_Object=MibTableColumn
swMSTPPortRestrictedTCN=_SwMSTPPortRestrictedTCN_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,14),_SwMSTPPortRestrictedTCN_Type())
swMSTPPortRestrictedTCN.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortRestrictedTCN.setStatus(_A)
class _SwMSTPPortOperFilterBpdu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('receiving',1),('filtering',2)))
_SwMSTPPortOperFilterBpdu_Type.__name__=_B
_SwMSTPPortOperFilterBpdu_Object=MibTableColumn
swMSTPPortOperFilterBpdu=_SwMSTPPortOperFilterBpdu_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,15),_SwMSTPPortOperFilterBpdu_Type())
swMSTPPortOperFilterBpdu.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPPortOperFilterBpdu.setStatus(_A)
_SwMSTPPortRecoverFilterBpdu_Type=TruthValue
_SwMSTPPortRecoverFilterBpdu_Object=MibTableColumn
swMSTPPortRecoverFilterBpdu=_SwMSTPPortRecoverFilterBpdu_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,4,1,16),_SwMSTPPortRecoverFilterBpdu_Type())
swMSTPPortRecoverFilterBpdu.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPPortRecoverFilterBpdu.setStatus(_A)
_SwMSTPMstPortTable_Object=MibTable
swMSTPMstPortTable=_SwMSTPMstPortTable_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5))
if mibBuilder.loadTexts:swMSTPMstPortTable.setStatus(_A)
_SwMSTPMstPortEntry_Object=MibTableRow
swMSTPMstPortEntry=_SwMSTPMstPortEntry_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1))
swMSTPMstPortEntry.setIndexNames((0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:swMSTPMstPortEntry.setStatus(_A)
class _SwMSTPMstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwMSTPMstPort_Type.__name__=_B
_SwMSTPMstPort_Object=MibTableColumn
swMSTPMstPort=_SwMSTPMstPort_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,1),_SwMSTPMstPort_Type())
swMSTPMstPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPMstPort.setStatus(_A)
class _SwMSTPMstPortInsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwMSTPMstPortInsID_Type.__name__=_B
_SwMSTPMstPortInsID_Object=MibTableColumn
swMSTPMstPortInsID=_SwMSTPMstPortInsID_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,2),_SwMSTPMstPortInsID_Type())
swMSTPMstPortInsID.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPMstPortInsID.setStatus(_A)
_SwMSTPMstPortDesignatedBridge_Type=BridgeId
_SwMSTPMstPortDesignatedBridge_Object=MibTableColumn
swMSTPMstPortDesignatedBridge=_SwMSTPMstPortDesignatedBridge_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,3),_SwMSTPMstPortDesignatedBridge_Type())
swMSTPMstPortDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPMstPortDesignatedBridge.setStatus(_A)
class _SwMSTPMstPortInternalPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_SwMSTPMstPortInternalPathCost_Type.__name__=_B
_SwMSTPMstPortInternalPathCost_Object=MibTableColumn
swMSTPMstPortInternalPathCost=_SwMSTPMstPortInternalPathCost_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,4),_SwMSTPMstPortInternalPathCost_Type())
swMSTPMstPortInternalPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPMstPortInternalPathCost.setStatus(_A)
class _SwMSTPMstPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_SwMSTPMstPortPriority_Type.__name__=_B
_SwMSTPMstPortPriority_Object=MibTableColumn
swMSTPMstPortPriority=_SwMSTPMstPortPriority_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,5),_SwMSTPMstPortPriority_Type())
swMSTPMstPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swMSTPMstPortPriority.setStatus(_A)
class _SwMSTPMstPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_H,2),('discarding',3),('learning',4),('forwarding',5),('broken',6),('no-stp-enabled',7),('err-disabled',8)))
_SwMSTPMstPortStatus_Type.__name__=_B
_SwMSTPMstPortStatus_Object=MibTableColumn
swMSTPMstPortStatus=_SwMSTPMstPortStatus_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,6),_SwMSTPMstPortStatus_Type())
swMSTPMstPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPMstPortStatus.setStatus(_A)
class _SwMSTPMstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disable',0),('alternate',1),('backup',2),('root',3),('designated',4),('master',5),('nonstp',6),('loopback',7)))
_SwMSTPMstPortRole_Type.__name__=_B
_SwMSTPMstPortRole_Object=MibTableColumn
swMSTPMstPortRole=_SwMSTPMstPortRole_Object((1,3,6,1,4,1,171,10,120,100,2,2,2,5,1,7),_SwMSTPMstPortRole_Type())
swMSTPMstPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:swMSTPMstPortRole.setStatus(_A)
_SwMSTPTraps_ObjectIdentity=ObjectIdentity
swMSTPTraps=_SwMSTPTraps_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,2,2,11))
_SwMSTPNotify_ObjectIdentity=ObjectIdentity
swMSTPNotify=_SwMSTPNotify_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,2,2,11,1))
_SwMSTPNotifyPrefix_ObjectIdentity=ObjectIdentity
swMSTPNotifyPrefix=_SwMSTPNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0))
swMSTPPortLBDTrap=NotificationType((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0,1))
swMSTPPortLBDTrap.setObjects((_E,_K))
if mibBuilder.loadTexts:swMSTPPortLBDTrap.setStatus(_A)
swMSTPPortBackupTrap=NotificationType((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0,2))
swMSTPPortBackupTrap.setObjects(*((_E,_O),(_E,_P)))
if mibBuilder.loadTexts:swMSTPPortBackupTrap.setStatus(_A)
swMSTPPortAlternateTrap=NotificationType((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0,3))
swMSTPPortAlternateTrap.setObjects(*((_E,_O),(_E,_P)))
if mibBuilder.loadTexts:swMSTPPortAlternateTrap.setStatus(_A)
swMSTPHwFilterStatusChange=NotificationType((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0,4))
swMSTPHwFilterStatusChange.setObjects(*((_E,_K),(_E,_R)))
if mibBuilder.loadTexts:swMSTPHwFilterStatusChange.setStatus(_A)
swMSTPRootRestrictedChange=NotificationType((1,3,6,1,4,1,171,10,120,100,2,2,11,1,0,5))
swMSTPRootRestrictedChange.setObjects(*((_E,_K),(_E,_S)))
if mibBuilder.loadTexts:swMSTPRootRestrictedChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'BridgeId':BridgeId,'dgs6600StpExtMIB':dgs6600StpExtMIB,'swMSTPGblMgmt':swMSTPGblMgmt,'swMSTPStpAdminState':swMSTPStpAdminState,'swMSTPStpVersion':swMSTPStpVersion,'swMSTPStpMaxAge':swMSTPStpMaxAge,'swMSTPStpHelloTime':swMSTPStpHelloTime,'swMSTPStpForwardDelay':swMSTPStpForwardDelay,'swMSTPStpMaxHops':swMSTPStpMaxHops,'swMSTPStpTxHoldCount':swMSTPStpTxHoldCount,'swMSTPStpForwardBPDU':swMSTPStpForwardBPDU,'swMSTPStpLBD':swMSTPStpLBD,'swMSTPStpLBDRecoverTime':swMSTPStpLBDRecoverTime,'swMSTPNniBPDUAddress':swMSTPNniBPDUAddress,'swMSTPCtrl':swMSTPCtrl,'swMSTPName':swMSTPName,'swMSTPRevisionLevel':swMSTPRevisionLevel,'swMSTPInstanceCtrlTable':swMSTPInstanceCtrlTable,'swMSTPInstanceCtrlEntry':swMSTPInstanceCtrlEntry,_Q:swMSTPInstId,'swMSTPInstVlanRangeList1to64':swMSTPInstVlanRangeList1to64,'swMSTPInstVlanRangeList65to128':swMSTPInstVlanRangeList65to128,'swMSTPInstVlanRangeList129to192':swMSTPInstVlanRangeList129to192,'swMSTPInstVlanRangeList193to256':swMSTPInstVlanRangeList193to256,'swMSTPInstVlanRangeList257to320':swMSTPInstVlanRangeList257to320,'swMSTPInstVlanRangeList321to384':swMSTPInstVlanRangeList321to384,'swMSTPInstVlanRangeList385to448':swMSTPInstVlanRangeList385to448,'swMSTPInstVlanRangeList449to512':swMSTPInstVlanRangeList449to512,'swMSTPInstType':swMSTPInstType,'swMSTPInstStatus':swMSTPInstStatus,'swMSTPInstPriority':swMSTPInstPriority,'swMSTPInstDesignatedRootBridge':swMSTPInstDesignatedRootBridge,'swMSTPInstExternalRootCost':swMSTPInstExternalRootCost,'swMSTPInstRegionalRootBridge':swMSTPInstRegionalRootBridge,'swMSTPInstInternalRootCost':swMSTPInstInternalRootCost,'swMSTPInstDesignatedBridge':swMSTPInstDesignatedBridge,'swMSTPInstRootPort':swMSTPInstRootPort,'swMSTPInstMaxAge':swMSTPInstMaxAge,'swMSTPInstForwardDelay':swMSTPInstForwardDelay,'swMSTPInstLastTopologyChange':swMSTPInstLastTopologyChange,'swMSTPInstTopChangesCount':swMSTPInstTopChangesCount,'swMSTPInstRemainHops':swMSTPInstRemainHops,'swMSTPInstRowStatus':swMSTPInstRowStatus,'swMSTPPortTable':swMSTPPortTable,'swMSTPPortEntry':swMSTPPortEntry,_K:swMSTPPort,'swMSTPPortAdminHelloTime':swMSTPPortAdminHelloTime,'swMSTPPortOperHelloTime':swMSTPPortOperHelloTime,'swMSTPSTPPortEnable':swMSTPSTPPortEnable,'swMSTPPortExternalPathCost':swMSTPPortExternalPathCost,'swMSTPPortMigration':swMSTPPortMigration,'swMSTPPortAdminEdgePort':swMSTPPortAdminEdgePort,'swMSTPPortOperEdgePort':swMSTPPortOperEdgePort,'swMSTPPortAdminP2P':swMSTPPortAdminP2P,'swMSTPPortOperP2P':swMSTPPortOperP2P,'swMSTPPortLBD':swMSTPPortLBD,'swMSTPPortBPDUFiltering':swMSTPPortBPDUFiltering,_S:swMSTPPortRestrictedRole,'swMSTPPortRestrictedTCN':swMSTPPortRestrictedTCN,_R:swMSTPPortOperFilterBpdu,'swMSTPPortRecoverFilterBpdu':swMSTPPortRecoverFilterBpdu,'swMSTPMstPortTable':swMSTPMstPortTable,'swMSTPMstPortEntry':swMSTPMstPortEntry,_O:swMSTPMstPort,_P:swMSTPMstPortInsID,'swMSTPMstPortDesignatedBridge':swMSTPMstPortDesignatedBridge,'swMSTPMstPortInternalPathCost':swMSTPMstPortInternalPathCost,'swMSTPMstPortPriority':swMSTPMstPortPriority,'swMSTPMstPortStatus':swMSTPMstPortStatus,'swMSTPMstPortRole':swMSTPMstPortRole,'swMSTPTraps':swMSTPTraps,'swMSTPNotify':swMSTPNotify,'swMSTPNotifyPrefix':swMSTPNotifyPrefix,'swMSTPPortLBDTrap':swMSTPPortLBDTrap,'swMSTPPortBackupTrap':swMSTPPortBackupTrap,'swMSTPPortAlternateTrap':swMSTPPortAlternateTrap,'swMSTPHwFilterStatusChange':swMSTPHwFilterStatusChange,'swMSTPRootRestrictedChange':swMSTPRootRestrictedChange})