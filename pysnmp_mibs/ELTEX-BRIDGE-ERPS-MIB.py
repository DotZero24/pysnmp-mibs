_T='not-accessible'
_S='eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId'
_R='eltexErpsMgmtSubRingCtrlRAPSVlanId'
_Q='read-create'
_P='eltexErpsMgmtRAPSVlanId'
_O='pending'
_N='active'
_M='forced-switch'
_L='manual-switch'
_K='disabled'
_J='TruthValue'
_I='eltexErpsNodeId'
_H='EltexErpsMgmtRAPSPortId'
_G='read-only'
_F='OctetString'
_E='ELTEX-BRIDGE-ERPS-MIB'
_D='EltexErpsEnabledState'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexBridgeExtMIBObjects,=mibBuilder.importSymbols('ELTEX-BRIDGE-EXT-MIB','eltexBridgeExtMIBObjects')
VlanIdOrNone,=mibBuilder.importSymbols('RLLAN1-MIB','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
eltexErpsMIB=ModuleIdentity((1,3,6,1,4,1,35265,35,1,1))
class EltexErpsEnabledState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_K,2)))
class EltexErpsMgmtRAPSPortState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('fowarding',1),('blocking',2),('signal-fail',3),(_L,4),(_M,5)))
class EltexErpsMgmtRAPSPortId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('west',2),('east',3)))
_EltexErpsCtrl_ObjectIdentity=ObjectIdentity
eltexErpsCtrl=_EltexErpsCtrl_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,1))
class _EltexErpsAdminState_Type(EltexErpsEnabledState):defaultValue=2
_EltexErpsAdminState_Type.__name__=_D
_EltexErpsAdminState_Object=MibScalar
eltexErpsAdminState=_EltexErpsAdminState_Object((1,3,6,1,4,1,35265,35,1,1,1,1),_EltexErpsAdminState_Type())
eltexErpsAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsAdminState.setStatus(_A)
class _EltexErpsLogState_Type(EltexErpsEnabledState):defaultValue=1
_EltexErpsLogState_Type.__name__=_D
_EltexErpsLogState_Object=MibScalar
eltexErpsLogState=_EltexErpsLogState_Object((1,3,6,1,4,1,35265,35,1,1,1,2),_EltexErpsLogState_Type())
eltexErpsLogState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsLogState.setStatus(_A)
class _EltexErpsTrapState_Type(EltexErpsEnabledState):defaultValue=1
_EltexErpsTrapState_Type.__name__=_D
_EltexErpsTrapState_Object=MibScalar
eltexErpsTrapState=_EltexErpsTrapState_Object((1,3,6,1,4,1,35265,35,1,1,1,3),_EltexErpsTrapState_Type())
eltexErpsTrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsTrapState.setStatus(_A)
class _EltexErpsPendingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copyPendingActive',1),('copyActivePending',2)))
_EltexErpsPendingAction_Type.__name__=_C
_EltexErpsPendingAction_Object=MibScalar
eltexErpsPendingAction=_EltexErpsPendingAction_Object((1,3,6,1,4,1,35265,35,1,1,1,5),_EltexErpsPendingAction_Type())
eltexErpsPendingAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsPendingAction.setStatus(_A)
_EltexErpsPendingActionVlan_Type=Integer32
_EltexErpsPendingActionVlan_Object=MibScalar
eltexErpsPendingActionVlan=_EltexErpsPendingActionVlan_Object((1,3,6,1,4,1,35265,35,1,1,1,6),_EltexErpsPendingActionVlan_Type())
eltexErpsPendingActionVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsPendingActionVlan.setStatus(_A)
class _EltexErpsGetConfigId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_EltexErpsGetConfigId_Type.__name__=_C
_EltexErpsGetConfigId_Object=MibScalar
eltexErpsGetConfigId=_EltexErpsGetConfigId_Object((1,3,6,1,4,1,35265,35,1,1,1,7),_EltexErpsGetConfigId_Type())
eltexErpsGetConfigId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsGetConfigId.setStatus(_A)
_EltexErpsInfo_ObjectIdentity=ObjectIdentity
eltexErpsInfo=_EltexErpsInfo_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,2))
_EltexErpsMgmt_ObjectIdentity=ObjectIdentity
eltexErpsMgmt=_EltexErpsMgmt_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,3))
_EltexErpsMgmtRAPSVlanTable_Object=MibTable
eltexErpsMgmtRAPSVlanTable=_EltexErpsMgmtRAPSVlanTable_Object((1,3,6,1,4,1,35265,35,1,1,3,1))
if mibBuilder.loadTexts:eltexErpsMgmtRAPSVlanTable.setStatus(_A)
_EltexErpsMgmtRAPSVlanEntry_Object=MibTableRow
eltexErpsMgmtRAPSVlanEntry=_EltexErpsMgmtRAPSVlanEntry_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1))
eltexErpsMgmtRAPSVlanEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:eltexErpsMgmtRAPSVlanEntry.setStatus(_A)
_EltexErpsMgmtRAPSVlanId_Type=Integer32
_EltexErpsMgmtRAPSVlanId_Object=MibTableColumn
eltexErpsMgmtRAPSVlanId=_EltexErpsMgmtRAPSVlanId_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,1),_EltexErpsMgmtRAPSVlanId_Type())
eltexErpsMgmtRAPSVlanId.setMaxAccess(_G)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSVlanId.setStatus(_A)
class _EltexErpsMgmtRAPSWestPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EltexErpsMgmtRAPSWestPort_Type.__name__=_C
_EltexErpsMgmtRAPSWestPort_Object=MibTableColumn
eltexErpsMgmtRAPSWestPort=_EltexErpsMgmtRAPSWestPort_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,2),_EltexErpsMgmtRAPSWestPort_Type())
eltexErpsMgmtRAPSWestPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSWestPort.setStatus(_A)
_EltexErpsMgmtRAPSWestPortState_Type=EltexErpsMgmtRAPSPortState
_EltexErpsMgmtRAPSWestPortState_Object=MibTableColumn
eltexErpsMgmtRAPSWestPortState=_EltexErpsMgmtRAPSWestPortState_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,3),_EltexErpsMgmtRAPSWestPortState_Type())
eltexErpsMgmtRAPSWestPortState.setMaxAccess(_G)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSWestPortState.setStatus(_A)
class _EltexErpsMgmtRAPSEastPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_EltexErpsMgmtRAPSEastPort_Type.__name__=_C
_EltexErpsMgmtRAPSEastPort_Object=MibTableColumn
eltexErpsMgmtRAPSEastPort=_EltexErpsMgmtRAPSEastPort_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,4),_EltexErpsMgmtRAPSEastPort_Type())
eltexErpsMgmtRAPSEastPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSEastPort.setStatus(_A)
_EltexErpsMgmtRAPSEastPortState_Type=EltexErpsMgmtRAPSPortState
_EltexErpsMgmtRAPSEastPortState_Object=MibTableColumn
eltexErpsMgmtRAPSEastPortState=_EltexErpsMgmtRAPSEastPortState_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,5),_EltexErpsMgmtRAPSEastPortState_Type())
eltexErpsMgmtRAPSEastPortState.setMaxAccess(_G)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSEastPortState.setStatus(_A)
class _EltexErpsMgmtRAPSRPLPort_Type(EltexErpsMgmtRAPSPortId):defaultValue=1
_EltexErpsMgmtRAPSRPLPort_Type.__name__=_H
_EltexErpsMgmtRAPSRPLPort_Object=MibTableColumn
eltexErpsMgmtRAPSRPLPort=_EltexErpsMgmtRAPSRPLPort_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,6),_EltexErpsMgmtRAPSRPLPort_Type())
eltexErpsMgmtRAPSRPLPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRPLPort.setStatus(_A)
class _EltexErpsMgmtRAPSRPLOwnerAdminState_Type(EltexErpsEnabledState):defaultValue=2
_EltexErpsMgmtRAPSRPLOwnerAdminState_Type.__name__=_D
_EltexErpsMgmtRAPSRPLOwnerAdminState_Object=MibTableColumn
eltexErpsMgmtRAPSRPLOwnerAdminState=_EltexErpsMgmtRAPSRPLOwnerAdminState_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,7),_EltexErpsMgmtRAPSRPLOwnerAdminState_Type())
eltexErpsMgmtRAPSRPLOwnerAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRPLOwnerAdminState.setStatus(_A)
class _EltexErpsMgmtRAPSRingMEL_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EltexErpsMgmtRAPSRingMEL_Type.__name__=_C
_EltexErpsMgmtRAPSRingMEL_Object=MibTableColumn
eltexErpsMgmtRAPSRingMEL=_EltexErpsMgmtRAPSRingMEL_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,8),_EltexErpsMgmtRAPSRingMEL_Type())
eltexErpsMgmtRAPSRingMEL.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRingMEL.setStatus(_A)
class _EltexErpsMgmtRAPSHoldOffTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_EltexErpsMgmtRAPSHoldOffTime_Type.__name__=_C
_EltexErpsMgmtRAPSHoldOffTime_Object=MibTableColumn
eltexErpsMgmtRAPSHoldOffTime=_EltexErpsMgmtRAPSHoldOffTime_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,9),_EltexErpsMgmtRAPSHoldOffTime_Type())
eltexErpsMgmtRAPSHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSHoldOffTime.setStatus(_A)
class _EltexErpsMgmtRAPSGuardTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_EltexErpsMgmtRAPSGuardTime_Type.__name__=_C
_EltexErpsMgmtRAPSGuardTime_Object=MibTableColumn
eltexErpsMgmtRAPSGuardTime=_EltexErpsMgmtRAPSGuardTime_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,10),_EltexErpsMgmtRAPSGuardTime_Type())
eltexErpsMgmtRAPSGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSGuardTime.setStatus(_A)
class _EltexErpsMgmtRAPSWTRTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_EltexErpsMgmtRAPSWTRTime_Type.__name__=_C
_EltexErpsMgmtRAPSWTRTime_Object=MibTableColumn
eltexErpsMgmtRAPSWTRTime=_EltexErpsMgmtRAPSWTRTime_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,11),_EltexErpsMgmtRAPSWTRTime_Type())
eltexErpsMgmtRAPSWTRTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSWTRTime.setStatus(_A)
class _EltexErpsMgmtRAPSRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('init',1),('idle',2),('protection',3),(_L,4),(_M,5),(_O,6)))
_EltexErpsMgmtRAPSRingState_Type.__name__=_C
_EltexErpsMgmtRAPSRingState_Object=MibTableColumn
eltexErpsMgmtRAPSRingState=_EltexErpsMgmtRAPSRingState_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,12),_EltexErpsMgmtRAPSRingState_Type())
eltexErpsMgmtRAPSRingState.setMaxAccess(_G)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRingState.setStatus(_A)
class _EltexErpsMgmtRAPSRingAdminState_Type(EltexErpsEnabledState):defaultValue=2
_EltexErpsMgmtRAPSRingAdminState_Type.__name__=_D
_EltexErpsMgmtRAPSRingAdminState_Object=MibTableColumn
eltexErpsMgmtRAPSRingAdminState=_EltexErpsMgmtRAPSRingAdminState_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,13),_EltexErpsMgmtRAPSRingAdminState_Type())
eltexErpsMgmtRAPSRingAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRingAdminState.setStatus(_A)
class _EltexErpsMgmtRAPSRPLOwnerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('inactive',2),(_K,3)))
_EltexErpsMgmtRAPSRPLOwnerOperStatus_Type.__name__=_C
_EltexErpsMgmtRAPSRPLOwnerOperStatus_Object=MibTableColumn
eltexErpsMgmtRAPSRPLOwnerOperStatus=_EltexErpsMgmtRAPSRPLOwnerOperStatus_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,14),_EltexErpsMgmtRAPSRPLOwnerOperStatus_Type())
eltexErpsMgmtRAPSRPLOwnerOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRPLOwnerOperStatus.setStatus(_A)
class _EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type.__name__=_F
_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Object=MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList1to1024=_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,15),_EltexErpsMgmtRAPSProtectionVlanRangeList1to1024_Type())
eltexErpsMgmtRAPSProtectionVlanRangeList1to1024.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSProtectionVlanRangeList1to1024.setStatus(_A)
class _EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type.__name__=_F
_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object=MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048=_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,16),_EltexErpsMgmtRAPSProtectionVlanRangeList1025to2048_Type())
eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048.setStatus(_A)
class _EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type.__name__=_F
_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object=MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072=_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,17),_EltexErpsMgmtRAPSProtectionVlanRangeList2049to3072_Type())
eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072.setStatus(_A)
class _EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type.__name__=_F
_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object=MibTableColumn
eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094=_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,18),_EltexErpsMgmtRAPSProtectionVlanRangeList3073to4094_Type())
eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094.setStatus(_A)
class _EltexErpsMgmtRAPSRevertive_Type(TruthValue):defaultValue=1
_EltexErpsMgmtRAPSRevertive_Type.__name__=_J
_EltexErpsMgmtRAPSRevertive_Object=MibTableColumn
eltexErpsMgmtRAPSRevertive=_EltexErpsMgmtRAPSRevertive_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,19),_EltexErpsMgmtRAPSRevertive_Type())
eltexErpsMgmtRAPSRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRevertive.setStatus(_A)
class _EltexErpsMgmtRAPSProtocolVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_EltexErpsMgmtRAPSProtocolVersion_Type.__name__=_C
_EltexErpsMgmtRAPSProtocolVersion_Object=MibTableColumn
eltexErpsMgmtRAPSProtocolVersion=_EltexErpsMgmtRAPSProtocolVersion_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,20),_EltexErpsMgmtRAPSProtocolVersion_Type())
eltexErpsMgmtRAPSProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSProtocolVersion.setStatus(_A)
class _EltexErpsMgmtRAPSPortForcedSwitch_Type(EltexErpsMgmtRAPSPortId):defaultValue=1
_EltexErpsMgmtRAPSPortForcedSwitch_Type.__name__=_H
_EltexErpsMgmtRAPSPortForcedSwitch_Object=MibTableColumn
eltexErpsMgmtRAPSPortForcedSwitch=_EltexErpsMgmtRAPSPortForcedSwitch_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,21),_EltexErpsMgmtRAPSPortForcedSwitch_Type())
eltexErpsMgmtRAPSPortForcedSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSPortForcedSwitch.setStatus(_A)
class _EltexErpsMgmtRAPSPortManualSwitch_Type(EltexErpsMgmtRAPSPortId):defaultValue=1
_EltexErpsMgmtRAPSPortManualSwitch_Type.__name__=_H
_EltexErpsMgmtRAPSPortManualSwitch_Object=MibTableColumn
eltexErpsMgmtRAPSPortManualSwitch=_EltexErpsMgmtRAPSPortManualSwitch_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,22),_EltexErpsMgmtRAPSPortManualSwitch_Type())
eltexErpsMgmtRAPSPortManualSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSPortManualSwitch.setStatus(_A)
_EltexErpsMgmtRAPSRowStatus_Type=RowStatus
_EltexErpsMgmtRAPSRowStatus_Object=MibTableColumn
eltexErpsMgmtRAPSRowStatus=_EltexErpsMgmtRAPSRowStatus_Object((1,3,6,1,4,1,35265,35,1,1,3,1,1,23),_EltexErpsMgmtRAPSRowStatus_Type())
eltexErpsMgmtRAPSRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:eltexErpsMgmtRAPSRowStatus.setStatus(_A)
_EltexErpsMgmtSubRingCtrlTable_Object=MibTable
eltexErpsMgmtSubRingCtrlTable=_EltexErpsMgmtSubRingCtrlTable_Object((1,3,6,1,4,1,35265,35,1,1,3,2))
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlTable.setStatus(_A)
_EltexErpsMgmtSubRingCtrlEntry_Object=MibTableRow
eltexErpsMgmtSubRingCtrlEntry=_EltexErpsMgmtSubRingCtrlEntry_Object((1,3,6,1,4,1,35265,35,1,1,3,2,1))
eltexErpsMgmtSubRingCtrlEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlEntry.setStatus(_A)
_EltexErpsMgmtSubRingCtrlRAPSVlanId_Type=Integer32
_EltexErpsMgmtSubRingCtrlRAPSVlanId_Object=MibTableColumn
eltexErpsMgmtSubRingCtrlRAPSVlanId=_EltexErpsMgmtSubRingCtrlRAPSVlanId_Object((1,3,6,1,4,1,35265,35,1,1,3,2,1,1),_EltexErpsMgmtSubRingCtrlRAPSVlanId_Type())
eltexErpsMgmtSubRingCtrlRAPSVlanId.setMaxAccess(_T)
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlRAPSVlanId.setStatus(_A)
_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type=Integer32
_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object=MibTableColumn
eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId=_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Object((1,3,6,1,4,1,35265,35,1,1,3,2,1,2),_EltexErpsMgmtSubRingCtrlSubRingRAPSVlanId_Type())
eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId.setMaxAccess(_T)
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId.setStatus(_A)
class _EltexErpsMgmtSubRingCtrlTCPropagationState_Type(EltexErpsEnabledState):defaultValue=2
_EltexErpsMgmtSubRingCtrlTCPropagationState_Type.__name__=_D
_EltexErpsMgmtSubRingCtrlTCPropagationState_Object=MibTableColumn
eltexErpsMgmtSubRingCtrlTCPropagationState=_EltexErpsMgmtSubRingCtrlTCPropagationState_Object((1,3,6,1,4,1,35265,35,1,1,3,2,1,3),_EltexErpsMgmtSubRingCtrlTCPropagationState_Type())
eltexErpsMgmtSubRingCtrlTCPropagationState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlTCPropagationState.setStatus(_A)
_EltexErpsMgmtSubRingCtrlRowStatus_Type=RowStatus
_EltexErpsMgmtSubRingCtrlRowStatus_Object=MibTableColumn
eltexErpsMgmtSubRingCtrlRowStatus=_EltexErpsMgmtSubRingCtrlRowStatus_Object((1,3,6,1,4,1,35265,35,1,1,3,2,1,4),_EltexErpsMgmtSubRingCtrlRowStatus_Type())
eltexErpsMgmtSubRingCtrlRowStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:eltexErpsMgmtSubRingCtrlRowStatus.setStatus(_A)
_EltexErpsNotify_ObjectIdentity=ObjectIdentity
eltexErpsNotify=_EltexErpsNotify_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,4))
_EltexErpsNotifyPrefix_ObjectIdentity=ObjectIdentity
eltexErpsNotifyPrefix=_EltexErpsNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,4,0))
_EltexErpsNotificationBindings_ObjectIdentity=ObjectIdentity
eltexErpsNotificationBindings=_EltexErpsNotificationBindings_ObjectIdentity((1,3,6,1,4,1,35265,35,1,1,4,2))
_EltexErpsNodeId_Type=MacAddress
_EltexErpsNodeId_Object=MibScalar
eltexErpsNodeId=_EltexErpsNodeId_Object((1,3,6,1,4,1,35265,35,1,1,4,2,1),_EltexErpsNodeId_Type())
eltexErpsNodeId.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:eltexErpsNodeId.setStatus(_A)
eltexErpsSFDetectedTrap=NotificationType((1,3,6,1,4,1,35265,35,1,1,4,0,1))
eltexErpsSFDetectedTrap.setObjects((_E,_I))
if mibBuilder.loadTexts:eltexErpsSFDetectedTrap.setStatus(_A)
eltexErpsSFClearedTrap=NotificationType((1,3,6,1,4,1,35265,35,1,1,4,0,2))
eltexErpsSFClearedTrap.setObjects((_E,_I))
if mibBuilder.loadTexts:eltexErpsSFClearedTrap.setStatus(_A)
eltexErpsRPLOwnerConflictTrap=NotificationType((1,3,6,1,4,1,35265,35,1,1,4,0,3))
eltexErpsRPLOwnerConflictTrap.setObjects((_E,_I))
if mibBuilder.loadTexts:eltexErpsRPLOwnerConflictTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:EltexErpsEnabledState,'EltexErpsMgmtRAPSPortState':EltexErpsMgmtRAPSPortState,_H:EltexErpsMgmtRAPSPortId,'eltexErpsMIB':eltexErpsMIB,'eltexErpsCtrl':eltexErpsCtrl,'eltexErpsAdminState':eltexErpsAdminState,'eltexErpsLogState':eltexErpsLogState,'eltexErpsTrapState':eltexErpsTrapState,'eltexErpsPendingAction':eltexErpsPendingAction,'eltexErpsPendingActionVlan':eltexErpsPendingActionVlan,'eltexErpsGetConfigId':eltexErpsGetConfigId,'eltexErpsInfo':eltexErpsInfo,'eltexErpsMgmt':eltexErpsMgmt,'eltexErpsMgmtRAPSVlanTable':eltexErpsMgmtRAPSVlanTable,'eltexErpsMgmtRAPSVlanEntry':eltexErpsMgmtRAPSVlanEntry,_P:eltexErpsMgmtRAPSVlanId,'eltexErpsMgmtRAPSWestPort':eltexErpsMgmtRAPSWestPort,'eltexErpsMgmtRAPSWestPortState':eltexErpsMgmtRAPSWestPortState,'eltexErpsMgmtRAPSEastPort':eltexErpsMgmtRAPSEastPort,'eltexErpsMgmtRAPSEastPortState':eltexErpsMgmtRAPSEastPortState,'eltexErpsMgmtRAPSRPLPort':eltexErpsMgmtRAPSRPLPort,'eltexErpsMgmtRAPSRPLOwnerAdminState':eltexErpsMgmtRAPSRPLOwnerAdminState,'eltexErpsMgmtRAPSRingMEL':eltexErpsMgmtRAPSRingMEL,'eltexErpsMgmtRAPSHoldOffTime':eltexErpsMgmtRAPSHoldOffTime,'eltexErpsMgmtRAPSGuardTime':eltexErpsMgmtRAPSGuardTime,'eltexErpsMgmtRAPSWTRTime':eltexErpsMgmtRAPSWTRTime,'eltexErpsMgmtRAPSRingState':eltexErpsMgmtRAPSRingState,'eltexErpsMgmtRAPSRingAdminState':eltexErpsMgmtRAPSRingAdminState,'eltexErpsMgmtRAPSRPLOwnerOperStatus':eltexErpsMgmtRAPSRPLOwnerOperStatus,'eltexErpsMgmtRAPSProtectionVlanRangeList1to1024':eltexErpsMgmtRAPSProtectionVlanRangeList1to1024,'eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048':eltexErpsMgmtRAPSProtectionVlanRangeList1025to2048,'eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072':eltexErpsMgmtRAPSProtectionVlanRangeList2049to3072,'eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094':eltexErpsMgmtRAPSProtectionVlanRangeList3073to4094,'eltexErpsMgmtRAPSRevertive':eltexErpsMgmtRAPSRevertive,'eltexErpsMgmtRAPSProtocolVersion':eltexErpsMgmtRAPSProtocolVersion,'eltexErpsMgmtRAPSPortForcedSwitch':eltexErpsMgmtRAPSPortForcedSwitch,'eltexErpsMgmtRAPSPortManualSwitch':eltexErpsMgmtRAPSPortManualSwitch,'eltexErpsMgmtRAPSRowStatus':eltexErpsMgmtRAPSRowStatus,'eltexErpsMgmtSubRingCtrlTable':eltexErpsMgmtSubRingCtrlTable,'eltexErpsMgmtSubRingCtrlEntry':eltexErpsMgmtSubRingCtrlEntry,_R:eltexErpsMgmtSubRingCtrlRAPSVlanId,_S:eltexErpsMgmtSubRingCtrlSubRingRAPSVlanId,'eltexErpsMgmtSubRingCtrlTCPropagationState':eltexErpsMgmtSubRingCtrlTCPropagationState,'eltexErpsMgmtSubRingCtrlRowStatus':eltexErpsMgmtSubRingCtrlRowStatus,'eltexErpsNotify':eltexErpsNotify,'eltexErpsNotifyPrefix':eltexErpsNotifyPrefix,'eltexErpsSFDetectedTrap':eltexErpsSFDetectedTrap,'eltexErpsSFClearedTrap':eltexErpsSFClearedTrap,'eltexErpsRPLOwnerConflictTrap':eltexErpsRPLOwnerConflictTrap,'eltexErpsNotificationBindings':eltexErpsNotificationBindings,_I:eltexErpsNodeId})