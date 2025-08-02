_R='hwdot1sMstVID'
_Q='legacy'
_P='disabled'
_O='hwdot1sMstiDesignedRoot'
_N='hwdot1sMstiDesignatedBridge'
_M='dot1dStpPort'
_L='BRIDGE-MIB'
_K='unused'
_J='enable'
_I='hwdot1sMstiPortIndex'
_H='hwdot1sInstanceID'
_G='EnabledStatus'
_F='OctetString'
_E='HUAWEI-LswMSTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols(_L,_M,'dot1dStpPortEntry')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hwdot1sMstp=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,14))
if mibBuilder.loadTexts:hwdot1sMstp.setRevisions(('2001-06-29 00:00',))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
class Hwdot1sFormatStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('dot1s',2),('auto',3)))
_HwMstpEventsV2_ObjectIdentity=ObjectIdentity
hwMstpEventsV2=_HwMstpEventsV2_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,14,0))
if mibBuilder.loadTexts:hwMstpEventsV2.setStatus(_A)
class _Hwdot1sStpStatus_Type(EnabledStatus):defaultValue=2
_Hwdot1sStpStatus_Type.__name__=_G
_Hwdot1sStpStatus_Object=MibScalar
hwdot1sStpStatus=_Hwdot1sStpStatus_Object((1,3,6,1,4,1,2011,2,23,1,14,1),_Hwdot1sStpStatus_Type())
hwdot1sStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sStpStatus.setStatus(_A)
class _Hwdot1sStpForceVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stp',0),('rstp',2),('mstp',3)))
_Hwdot1sStpForceVersion_Type.__name__=_C
_Hwdot1sStpForceVersion_Object=MibScalar
hwdot1sStpForceVersion=_Hwdot1sStpForceVersion_Object((1,3,6,1,4,1,2011,2,23,1,14,2),_Hwdot1sStpForceVersion_Type())
hwdot1sStpForceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sStpForceVersion.setStatus(_A)
class _Hwdot1sStpDiameter_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_Hwdot1sStpDiameter_Type.__name__=_C
_Hwdot1sStpDiameter_Object=MibScalar
hwdot1sStpDiameter=_Hwdot1sStpDiameter_Object((1,3,6,1,4,1,2011,2,23,1,14,3),_Hwdot1sStpDiameter_Type())
hwdot1sStpDiameter.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sStpDiameter.setStatus(_A)
class _Hwdot1sMstBridgeMaxHops_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_Hwdot1sMstBridgeMaxHops_Type.__name__=_C
_Hwdot1sMstBridgeMaxHops_Object=MibScalar
hwdot1sMstBridgeMaxHops=_Hwdot1sMstBridgeMaxHops_Object((1,3,6,1,4,1,2011,2,23,1,14,4),_Hwdot1sMstBridgeMaxHops_Type())
hwdot1sMstBridgeMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstBridgeMaxHops.setStatus(_A)
_Hwdot1sMstMasterBridgeID_Type=BridgeId
_Hwdot1sMstMasterBridgeID_Object=MibScalar
hwdot1sMstMasterBridgeID=_Hwdot1sMstMasterBridgeID_Object((1,3,6,1,4,1,2011,2,23,1,14,5),_Hwdot1sMstMasterBridgeID_Type())
hwdot1sMstMasterBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstMasterBridgeID.setStatus(_A)
class _Hwdot1sMstMasterPathCost_Type(Integer32):defaultValue=0
_Hwdot1sMstMasterPathCost_Type.__name__=_C
_Hwdot1sMstMasterPathCost_Object=MibScalar
hwdot1sMstMasterPathCost=_Hwdot1sMstMasterPathCost_Object((1,3,6,1,4,1,2011,2,23,1,14,6),_Hwdot1sMstMasterPathCost_Type())
hwdot1sMstMasterPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstMasterPathCost.setStatus(_A)
class _Hwdot1sMstBpduGuard_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstBpduGuard_Type.__name__=_G
_Hwdot1sMstBpduGuard_Object=MibScalar
hwdot1sMstBpduGuard=_Hwdot1sMstBpduGuard_Object((1,3,6,1,4,1,2011,2,23,1,14,7),_Hwdot1sMstBpduGuard_Type())
hwdot1sMstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstBpduGuard.setStatus(_A)
class _Hwdot1sMstAdminFormatSelector_Type(Integer32):defaultValue=0
_Hwdot1sMstAdminFormatSelector_Type.__name__=_C
_Hwdot1sMstAdminFormatSelector_Object=MibScalar
hwdot1sMstAdminFormatSelector=_Hwdot1sMstAdminFormatSelector_Object((1,3,6,1,4,1,2011,2,23,1,14,8),_Hwdot1sMstAdminFormatSelector_Type())
hwdot1sMstAdminFormatSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstAdminFormatSelector.setStatus(_A)
class _Hwdot1sMstAdminRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hwdot1sMstAdminRegionName_Type.__name__=_F
_Hwdot1sMstAdminRegionName_Object=MibScalar
hwdot1sMstAdminRegionName=_Hwdot1sMstAdminRegionName_Object((1,3,6,1,4,1,2011,2,23,1,14,9),_Hwdot1sMstAdminRegionName_Type())
hwdot1sMstAdminRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstAdminRegionName.setStatus(_A)
class _Hwdot1sMstAdminRevisionLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hwdot1sMstAdminRevisionLevel_Type.__name__=_C
_Hwdot1sMstAdminRevisionLevel_Object=MibScalar
hwdot1sMstAdminRevisionLevel=_Hwdot1sMstAdminRevisionLevel_Object((1,3,6,1,4,1,2011,2,23,1,14,10),_Hwdot1sMstAdminRevisionLevel_Type())
hwdot1sMstAdminRevisionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstAdminRevisionLevel.setStatus(_A)
class _Hwdot1sMstOperFormatSelector_Type(Integer32):defaultValue=0
_Hwdot1sMstOperFormatSelector_Type.__name__=_C
_Hwdot1sMstOperFormatSelector_Object=MibScalar
hwdot1sMstOperFormatSelector=_Hwdot1sMstOperFormatSelector_Object((1,3,6,1,4,1,2011,2,23,1,14,11),_Hwdot1sMstOperFormatSelector_Type())
hwdot1sMstOperFormatSelector.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstOperFormatSelector.setStatus(_A)
class _Hwdot1sMstOperRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hwdot1sMstOperRegionName_Type.__name__=_F
_Hwdot1sMstOperRegionName_Object=MibScalar
hwdot1sMstOperRegionName=_Hwdot1sMstOperRegionName_Object((1,3,6,1,4,1,2011,2,23,1,14,12),_Hwdot1sMstOperRegionName_Type())
hwdot1sMstOperRegionName.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstOperRegionName.setStatus(_A)
class _Hwdot1sMstOperRevisionLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hwdot1sMstOperRevisionLevel_Type.__name__=_C
_Hwdot1sMstOperRevisionLevel_Object=MibScalar
hwdot1sMstOperRevisionLevel=_Hwdot1sMstOperRevisionLevel_Object((1,3,6,1,4,1,2011,2,23,1,14,13),_Hwdot1sMstOperRevisionLevel_Type())
hwdot1sMstOperRevisionLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstOperRevisionLevel.setStatus(_A)
class _Hwdot1sMstOperConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hwdot1sMstOperConfigDigest_Type.__name__=_F
_Hwdot1sMstOperConfigDigest_Object=MibScalar
hwdot1sMstOperConfigDigest=_Hwdot1sMstOperConfigDigest_Object((1,3,6,1,4,1,2011,2,23,1,14,14),_Hwdot1sMstOperConfigDigest_Type())
hwdot1sMstOperConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstOperConfigDigest.setStatus(_A)
class _Hwdot1sMstRegionConfActive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('disable',2)))
_Hwdot1sMstRegionConfActive_Type.__name__=_C
_Hwdot1sMstRegionConfActive_Object=MibScalar
hwdot1sMstRegionConfActive=_Hwdot1sMstRegionConfActive_Object((1,3,6,1,4,1,2011,2,23,1,14,15),_Hwdot1sMstRegionConfActive_Type())
hwdot1sMstRegionConfActive.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstRegionConfActive.setStatus(_A)
class _Hwdot1sMstDefaultVlanAllo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hwdot1sMstDefaultVlanAllo_Type.__name__=_C
_Hwdot1sMstDefaultVlanAllo_Object=MibScalar
hwdot1sMstDefaultVlanAllo=_Hwdot1sMstDefaultVlanAllo_Object((1,3,6,1,4,1,2011,2,23,1,14,16),_Hwdot1sMstDefaultVlanAllo_Type())
hwdot1sMstDefaultVlanAllo.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstDefaultVlanAllo.setStatus(_A)
class _Hwdot1sMstDefaultRegionName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hwdot1sMstDefaultRegionName_Type.__name__=_C
_Hwdot1sMstDefaultRegionName_Object=MibScalar
hwdot1sMstDefaultRegionName=_Hwdot1sMstDefaultRegionName_Object((1,3,6,1,4,1,2011,2,23,1,14,17),_Hwdot1sMstDefaultRegionName_Type())
hwdot1sMstDefaultRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstDefaultRegionName.setStatus(_A)
_Hwdot1sVIDAllocationTable_Object=MibTable
hwdot1sVIDAllocationTable=_Hwdot1sVIDAllocationTable_Object((1,3,6,1,4,1,2011,2,23,1,14,18))
if mibBuilder.loadTexts:hwdot1sVIDAllocationTable.setStatus(_A)
_Hwdot1sVIDAllocationEntry_Object=MibTableRow
hwdot1sVIDAllocationEntry=_Hwdot1sVIDAllocationEntry_Object((1,3,6,1,4,1,2011,2,23,1,14,18,1))
hwdot1sVIDAllocationEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hwdot1sVIDAllocationEntry.setStatus(_A)
class _Hwdot1sMstVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Hwdot1sMstVID_Type.__name__=_C
_Hwdot1sMstVID_Object=MibTableColumn
hwdot1sMstVID=_Hwdot1sMstVID_Object((1,3,6,1,4,1,2011,2,23,1,14,18,1,1),_Hwdot1sMstVID_Type())
hwdot1sMstVID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstVID.setStatus(_A)
class _Hwdot1sAdminMstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hwdot1sAdminMstID_Type.__name__=_C
_Hwdot1sAdminMstID_Object=MibTableColumn
hwdot1sAdminMstID=_Hwdot1sAdminMstID_Object((1,3,6,1,4,1,2011,2,23,1,14,18,1,2),_Hwdot1sAdminMstID_Type())
hwdot1sAdminMstID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sAdminMstID.setStatus(_A)
class _Hwdot1sOperMstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hwdot1sOperMstID_Type.__name__=_C
_Hwdot1sOperMstID_Object=MibTableColumn
hwdot1sOperMstID=_Hwdot1sOperMstID_Object((1,3,6,1,4,1,2011,2,23,1,14,18,1,3),_Hwdot1sOperMstID_Type())
hwdot1sOperMstID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sOperMstID.setStatus(_A)
_Hwdot1sInstanceTable_Object=MibTable
hwdot1sInstanceTable=_Hwdot1sInstanceTable_Object((1,3,6,1,4,1,2011,2,23,1,14,19))
if mibBuilder.loadTexts:hwdot1sInstanceTable.setStatus(_A)
_Hwdot1sInstanceEntry_Object=MibTableRow
hwdot1sInstanceEntry=_Hwdot1sInstanceEntry_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1))
hwdot1sInstanceEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hwdot1sInstanceEntry.setStatus(_A)
class _Hwdot1sInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hwdot1sInstanceID_Type.__name__=_C
_Hwdot1sInstanceID_Object=MibTableColumn
hwdot1sInstanceID=_Hwdot1sInstanceID_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,1),_Hwdot1sInstanceID_Type())
hwdot1sInstanceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sInstanceID.setStatus(_A)
_Hwdot1sMstiBridgeID_Type=BridgeId
_Hwdot1sMstiBridgeID_Object=MibTableColumn
hwdot1sMstiBridgeID=_Hwdot1sMstiBridgeID_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,2),_Hwdot1sMstiBridgeID_Type())
hwdot1sMstiBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiBridgeID.setStatus(_A)
class _Hwdot1sMstiBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Hwdot1sMstiBridgePriority_Type.__name__=_C
_Hwdot1sMstiBridgePriority_Object=MibTableColumn
hwdot1sMstiBridgePriority=_Hwdot1sMstiBridgePriority_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,3),_Hwdot1sMstiBridgePriority_Type())
hwdot1sMstiBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiBridgePriority.setStatus(_A)
_Hwdot1sMstiDesignedRoot_Type=BridgeId
_Hwdot1sMstiDesignedRoot_Object=MibTableColumn
hwdot1sMstiDesignedRoot=_Hwdot1sMstiDesignedRoot_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,4),_Hwdot1sMstiDesignedRoot_Type())
hwdot1sMstiDesignedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiDesignedRoot.setStatus(_A)
_Hwdot1sMstiRootPathCost_Type=Integer32
_Hwdot1sMstiRootPathCost_Object=MibTableColumn
hwdot1sMstiRootPathCost=_Hwdot1sMstiRootPathCost_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,5),_Hwdot1sMstiRootPathCost_Type())
hwdot1sMstiRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiRootPathCost.setStatus(_A)
_Hwdot1sMstiRootPort_Type=Integer32
_Hwdot1sMstiRootPort_Object=MibTableColumn
hwdot1sMstiRootPort=_Hwdot1sMstiRootPort_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,6),_Hwdot1sMstiRootPort_Type())
hwdot1sMstiRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiRootPort.setStatus(_A)
class _Hwdot1sMstiRootType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('secondary',1),('primary',2)))
_Hwdot1sMstiRootType_Type.__name__=_C
_Hwdot1sMstiRootType_Object=MibTableColumn
hwdot1sMstiRootType=_Hwdot1sMstiRootType_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,7),_Hwdot1sMstiRootType_Type())
hwdot1sMstiRootType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiRootType.setStatus(_A)
_Hwdot1sMstiRemainingHops_Type=Integer32
_Hwdot1sMstiRemainingHops_Object=MibTableColumn
hwdot1sMstiRemainingHops=_Hwdot1sMstiRemainingHops_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,8),_Hwdot1sMstiRemainingHops_Type())
hwdot1sMstiRemainingHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiRemainingHops.setStatus(_A)
class _Hwdot1sMstiAdminMappedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hwdot1sMstiAdminMappedVlanListLow_Type.__name__=_F
_Hwdot1sMstiAdminMappedVlanListLow_Object=MibTableColumn
hwdot1sMstiAdminMappedVlanListLow=_Hwdot1sMstiAdminMappedVlanListLow_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,9),_Hwdot1sMstiAdminMappedVlanListLow_Type())
hwdot1sMstiAdminMappedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiAdminMappedVlanListLow.setStatus(_A)
class _Hwdot1sMstiAdminMappedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hwdot1sMstiAdminMappedVlanListHigh_Type.__name__=_F
_Hwdot1sMstiAdminMappedVlanListHigh_Object=MibTableColumn
hwdot1sMstiAdminMappedVlanListHigh=_Hwdot1sMstiAdminMappedVlanListHigh_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,10),_Hwdot1sMstiAdminMappedVlanListHigh_Type())
hwdot1sMstiAdminMappedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiAdminMappedVlanListHigh.setStatus(_A)
class _Hwdot1sMstiOperMappedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hwdot1sMstiOperMappedVlanListLow_Type.__name__=_F
_Hwdot1sMstiOperMappedVlanListLow_Object=MibTableColumn
hwdot1sMstiOperMappedVlanListLow=_Hwdot1sMstiOperMappedVlanListLow_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,11),_Hwdot1sMstiOperMappedVlanListLow_Type())
hwdot1sMstiOperMappedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiOperMappedVlanListLow.setStatus(_A)
class _Hwdot1sMstiOperMappedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hwdot1sMstiOperMappedVlanListHigh_Type.__name__=_F
_Hwdot1sMstiOperMappedVlanListHigh_Object=MibTableColumn
hwdot1sMstiOperMappedVlanListHigh=_Hwdot1sMstiOperMappedVlanListHigh_Object((1,3,6,1,4,1,2011,2,23,1,14,19,1,12),_Hwdot1sMstiOperMappedVlanListHigh_Type())
hwdot1sMstiOperMappedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiOperMappedVlanListHigh.setStatus(_A)
_Hwdot1sPortTable_Object=MibTable
hwdot1sPortTable=_Hwdot1sPortTable_Object((1,3,6,1,4,1,2011,2,23,1,14,20))
if mibBuilder.loadTexts:hwdot1sPortTable.setStatus(_A)
_Hwdot1sPortEntry_Object=MibTableRow
hwdot1sPortEntry=_Hwdot1sPortEntry_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1))
hwdot1sPortEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:hwdot1sPortEntry.setStatus(_A)
class _Hwdot1sMstiPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hwdot1sMstiPortIndex_Type.__name__=_C
_Hwdot1sMstiPortIndex_Object=MibTableColumn
hwdot1sMstiPortIndex=_Hwdot1sMstiPortIndex_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,1),_Hwdot1sMstiPortIndex_Type())
hwdot1sMstiPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiPortIndex.setStatus(_A)
class _Hwdot1sMstiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_P,1),('discarding',2),('learning',4),('forwarding',5)))
_Hwdot1sMstiState_Type.__name__=_C
_Hwdot1sMstiState_Object=MibTableColumn
hwdot1sMstiState=_Hwdot1sMstiState_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,2),_Hwdot1sMstiState_Type())
hwdot1sMstiState.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiState.setStatus(_A)
class _Hwdot1sMstiPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Hwdot1sMstiPortPriority_Type.__name__=_C
_Hwdot1sMstiPortPriority_Object=MibTableColumn
hwdot1sMstiPortPriority=_Hwdot1sMstiPortPriority_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,3),_Hwdot1sMstiPortPriority_Type())
hwdot1sMstiPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiPortPriority.setStatus(_A)
class _Hwdot1sMstiPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Hwdot1sMstiPathCost_Type.__name__=_C
_Hwdot1sMstiPathCost_Object=MibTableColumn
hwdot1sMstiPathCost=_Hwdot1sMstiPathCost_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,4),_Hwdot1sMstiPathCost_Type())
hwdot1sMstiPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiPathCost.setStatus(_A)
_Hwdot1sMstiDesignatedRoot_Type=BridgeId
_Hwdot1sMstiDesignatedRoot_Object=MibTableColumn
hwdot1sMstiDesignatedRoot=_Hwdot1sMstiDesignatedRoot_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,5),_Hwdot1sMstiDesignatedRoot_Type())
hwdot1sMstiDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiDesignatedRoot.setStatus(_A)
_Hwdot1sMstiDesignatedCost_Type=Integer32
_Hwdot1sMstiDesignatedCost_Object=MibTableColumn
hwdot1sMstiDesignatedCost=_Hwdot1sMstiDesignatedCost_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,6),_Hwdot1sMstiDesignatedCost_Type())
hwdot1sMstiDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiDesignatedCost.setStatus(_A)
_Hwdot1sMstiDesignatedBridge_Type=BridgeId
_Hwdot1sMstiDesignatedBridge_Object=MibTableColumn
hwdot1sMstiDesignatedBridge=_Hwdot1sMstiDesignatedBridge_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,7),_Hwdot1sMstiDesignatedBridge_Type())
hwdot1sMstiDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiDesignatedBridge.setStatus(_A)
class _Hwdot1sMstiDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Hwdot1sMstiDesignatedPort_Type.__name__=_F
_Hwdot1sMstiDesignatedPort_Object=MibTableColumn
hwdot1sMstiDesignatedPort=_Hwdot1sMstiDesignatedPort_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,8),_Hwdot1sMstiDesignatedPort_Type())
hwdot1sMstiDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiDesignatedPort.setStatus(_A)
_Hwdot1sMstiMasterBridgeID_Type=BridgeId
_Hwdot1sMstiMasterBridgeID_Object=MibTableColumn
hwdot1sMstiMasterBridgeID=_Hwdot1sMstiMasterBridgeID_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,9),_Hwdot1sMstiMasterBridgeID_Type())
hwdot1sMstiMasterBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiMasterBridgeID.setStatus(_A)
_Hwdot1sMstiMasterPortCost_Type=Integer32
_Hwdot1sMstiMasterPortCost_Object=MibTableColumn
hwdot1sMstiMasterPortCost=_Hwdot1sMstiMasterPortCost_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,10),_Hwdot1sMstiMasterPortCost_Type())
hwdot1sMstiMasterPortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiMasterPortCost.setStatus(_A)
class _Hwdot1sMstiStpPortEdgeport_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstiStpPortEdgeport_Type.__name__=_G
_Hwdot1sMstiStpPortEdgeport_Object=MibTableColumn
hwdot1sMstiStpPortEdgeport=_Hwdot1sMstiStpPortEdgeport_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,11),_Hwdot1sMstiStpPortEdgeport_Type())
hwdot1sMstiStpPortEdgeport.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpPortEdgeport.setStatus(_A)
class _Hwdot1sMstiStpPortPointToPoint_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_Hwdot1sMstiStpPortPointToPoint_Type.__name__=_C
_Hwdot1sMstiStpPortPointToPoint_Object=MibTableColumn
hwdot1sMstiStpPortPointToPoint=_Hwdot1sMstiStpPortPointToPoint_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,12),_Hwdot1sMstiStpPortPointToPoint_Type())
hwdot1sMstiStpPortPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpPortPointToPoint.setStatus(_A)
class _Hwdot1sMstiStpMcheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hwdot1sMstiStpMcheck_Type.__name__=_C
_Hwdot1sMstiStpMcheck_Object=MibTableColumn
hwdot1sMstiStpMcheck=_Hwdot1sMstiStpMcheck_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,13),_Hwdot1sMstiStpMcheck_Type())
hwdot1sMstiStpMcheck.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpMcheck.setStatus(_A)
class _Hwdot1sMstiStpTransLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hwdot1sMstiStpTransLimit_Type.__name__=_C
_Hwdot1sMstiStpTransLimit_Object=MibTableColumn
hwdot1sMstiStpTransLimit=_Hwdot1sMstiStpTransLimit_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,14),_Hwdot1sMstiStpTransLimit_Type())
hwdot1sMstiStpTransLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpTransLimit.setStatus(_A)
_Hwdot1sMstiStpRXStpBPDU_Type=Counter32
_Hwdot1sMstiStpRXStpBPDU_Object=MibTableColumn
hwdot1sMstiStpRXStpBPDU=_Hwdot1sMstiStpRXStpBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,15),_Hwdot1sMstiStpRXStpBPDU_Type())
hwdot1sMstiStpRXStpBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpRXStpBPDU.setStatus(_A)
_Hwdot1sMstiStpTXStpBPDU_Type=Counter32
_Hwdot1sMstiStpTXStpBPDU_Object=MibTableColumn
hwdot1sMstiStpTXStpBPDU=_Hwdot1sMstiStpTXStpBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,16),_Hwdot1sMstiStpTXStpBPDU_Type())
hwdot1sMstiStpTXStpBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpTXStpBPDU.setStatus(_A)
_Hwdot1sMstiStpRXTCNBPDU_Type=Counter32
_Hwdot1sMstiStpRXTCNBPDU_Object=MibTableColumn
hwdot1sMstiStpRXTCNBPDU=_Hwdot1sMstiStpRXTCNBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,17),_Hwdot1sMstiStpRXTCNBPDU_Type())
hwdot1sMstiStpRXTCNBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpRXTCNBPDU.setStatus(_A)
_Hwdot1sMstiStpTXTCNBPDU_Type=Counter32
_Hwdot1sMstiStpTXTCNBPDU_Object=MibTableColumn
hwdot1sMstiStpTXTCNBPDU=_Hwdot1sMstiStpTXTCNBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,18),_Hwdot1sMstiStpTXTCNBPDU_Type())
hwdot1sMstiStpTXTCNBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpTXTCNBPDU.setStatus(_A)
_Hwdot1sMstiStpRXRSTPBPDU_Type=Counter32
_Hwdot1sMstiStpRXRSTPBPDU_Object=MibTableColumn
hwdot1sMstiStpRXRSTPBPDU=_Hwdot1sMstiStpRXRSTPBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,19),_Hwdot1sMstiStpRXRSTPBPDU_Type())
hwdot1sMstiStpRXRSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpRXRSTPBPDU.setStatus(_A)
_Hwdot1sMstiStpTXRSTPBPDU_Type=Counter32
_Hwdot1sMstiStpTXRSTPBPDU_Object=MibTableColumn
hwdot1sMstiStpTXRSTPBPDU=_Hwdot1sMstiStpTXRSTPBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,20),_Hwdot1sMstiStpTXRSTPBPDU_Type())
hwdot1sMstiStpTXRSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpTXRSTPBPDU.setStatus(_A)
_Hwdot1sMstiStpRXMSTPBPDU_Type=Counter32
_Hwdot1sMstiStpRXMSTPBPDU_Object=MibTableColumn
hwdot1sMstiStpRXMSTPBPDU=_Hwdot1sMstiStpRXMSTPBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,21),_Hwdot1sMstiStpRXMSTPBPDU_Type())
hwdot1sMstiStpRXMSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpRXMSTPBPDU.setStatus(_A)
_Hwdot1sMstiStpTXMSTPBPDU_Type=Counter32
_Hwdot1sMstiStpTXMSTPBPDU_Object=MibTableColumn
hwdot1sMstiStpTXMSTPBPDU=_Hwdot1sMstiStpTXMSTPBPDU_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,22),_Hwdot1sMstiStpTXMSTPBPDU_Type())
hwdot1sMstiStpTXMSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpTXMSTPBPDU.setStatus(_A)
class _Hwdot1sMstiStpClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*(('clear',1),(_K,65535)))
_Hwdot1sMstiStpClearStatistics_Type.__name__=_C
_Hwdot1sMstiStpClearStatistics_Object=MibTableColumn
hwdot1sMstiStpClearStatistics=_Hwdot1sMstiStpClearStatistics_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,23),_Hwdot1sMstiStpClearStatistics_Type())
hwdot1sMstiStpClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpClearStatistics.setStatus(_A)
class _Hwdot1sMstiStpDefaultPortCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hwdot1sMstiStpDefaultPortCost_Type.__name__=_C
_Hwdot1sMstiStpDefaultPortCost_Object=MibTableColumn
hwdot1sMstiStpDefaultPortCost=_Hwdot1sMstiStpDefaultPortCost_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,24),_Hwdot1sMstiStpDefaultPortCost_Type())
hwdot1sMstiStpDefaultPortCost.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpDefaultPortCost.setStatus(_A)
class _Hwdot1sMstiStpStatus_Type(EnabledStatus):defaultValue=1
_Hwdot1sMstiStpStatus_Type.__name__=_G
_Hwdot1sMstiStpStatus_Object=MibTableColumn
hwdot1sMstiStpStatus=_Hwdot1sMstiStpStatus_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,25),_Hwdot1sMstiStpStatus_Type())
hwdot1sMstiStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpStatus.setStatus(_A)
class _Hwdot1sMstiPortRootGuard_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstiPortRootGuard_Type.__name__=_G
_Hwdot1sMstiPortRootGuard_Object=MibTableColumn
hwdot1sMstiPortRootGuard=_Hwdot1sMstiPortRootGuard_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,26),_Hwdot1sMstiPortRootGuard_Type())
hwdot1sMstiPortRootGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiPortRootGuard.setStatus(_A)
class _Hwdot1sMstiPortLoopGuard_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstiPortLoopGuard_Type.__name__=_G
_Hwdot1sMstiPortLoopGuard_Object=MibTableColumn
hwdot1sMstiPortLoopGuard=_Hwdot1sMstiPortLoopGuard_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,27),_Hwdot1sMstiPortLoopGuard_Type())
hwdot1sMstiPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiPortLoopGuard.setStatus(_A)
class _Hwdot1sMstiStpPortSendingBPDUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_Hwdot1sMstiStpPortSendingBPDUType_Type.__name__=_C
_Hwdot1sMstiStpPortSendingBPDUType_Object=MibTableColumn
hwdot1sMstiStpPortSendingBPDUType=_Hwdot1sMstiStpPortSendingBPDUType_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,28),_Hwdot1sMstiStpPortSendingBPDUType_Type())
hwdot1sMstiStpPortSendingBPDUType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpPortSendingBPDUType.setStatus(_A)
class _Hwdot1sMstiStpOperPortPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hwdot1sMstiStpOperPortPointToPoint_Type.__name__=_C
_Hwdot1sMstiStpOperPortPointToPoint_Object=MibTableColumn
hwdot1sMstiStpOperPortPointToPoint=_Hwdot1sMstiStpOperPortPointToPoint_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,29),_Hwdot1sMstiStpOperPortPointToPoint_Type())
hwdot1sMstiStpOperPortPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpOperPortPointToPoint.setStatus(_A)
_Hwdot1sMstiStpPortAdminBPDUFmt_Type=Hwdot1sFormatStatus
_Hwdot1sMstiStpPortAdminBPDUFmt_Object=MibTableColumn
hwdot1sMstiStpPortAdminBPDUFmt=_Hwdot1sMstiStpPortAdminBPDUFmt_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,30),_Hwdot1sMstiStpPortAdminBPDUFmt_Type())
hwdot1sMstiStpPortAdminBPDUFmt.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpPortAdminBPDUFmt.setStatus(_A)
_Hwdot1sMstiStpPortOperBPDUFmt_Type=Hwdot1sFormatStatus
_Hwdot1sMstiStpPortOperBPDUFmt_Object=MibTableColumn
hwdot1sMstiStpPortOperBPDUFmt=_Hwdot1sMstiStpPortOperBPDUFmt_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,31),_Hwdot1sMstiStpPortOperBPDUFmt_Type())
hwdot1sMstiStpPortOperBPDUFmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpPortOperBPDUFmt.setStatus(_A)
class _Hwdot1sMstiStpPortRoleRestriction_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstiStpPortRoleRestriction_Type.__name__=_G
_Hwdot1sMstiStpPortRoleRestriction_Object=MibTableColumn
hwdot1sMstiStpPortRoleRestriction=_Hwdot1sMstiStpPortRoleRestriction_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,32),_Hwdot1sMstiStpPortRoleRestriction_Type())
hwdot1sMstiStpPortRoleRestriction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpPortRoleRestriction.setStatus(_A)
class _Hwdot1sMstiStpPortTcRestriction_Type(EnabledStatus):defaultValue=2
_Hwdot1sMstiStpPortTcRestriction_Type.__name__=_G
_Hwdot1sMstiStpPortTcRestriction_Object=MibTableColumn
hwdot1sMstiStpPortTcRestriction=_Hwdot1sMstiStpPortTcRestriction_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,33),_Hwdot1sMstiStpPortTcRestriction_Type())
hwdot1sMstiStpPortTcRestriction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sMstiStpPortTcRestriction.setStatus(_A)
_Hwdot1sMstiStpPortDisputed_Type=TruthValue
_Hwdot1sMstiStpPortDisputed_Object=MibTableColumn
hwdot1sMstiStpPortDisputed=_Hwdot1sMstiStpPortDisputed_Object((1,3,6,1,4,1,2011,2,23,1,14,20,1,34),_Hwdot1sMstiStpPortDisputed_Type())
hwdot1sMstiStpPortDisputed.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1sMstiStpPortDisputed.setStatus(_A)
class _Hwdot1sStpPathCostStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('dot1d-1998',1),('dot1t',2)))
_Hwdot1sStpPathCostStandard_Type.__name__=_C
_Hwdot1sStpPathCostStandard_Object=MibScalar
hwdot1sStpPathCostStandard=_Hwdot1sStpPathCostStandard_Object((1,3,6,1,4,1,2011,2,23,1,14,21),_Hwdot1sStpPathCostStandard_Type())
hwdot1sStpPathCostStandard.setMaxAccess(_D)
if mibBuilder.loadTexts:hwdot1sStpPathCostStandard.setStatus(_A)
hwPortMstiStateForwarding=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,1))
hwPortMstiStateForwarding.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hwPortMstiStateForwarding.setStatus(_A)
hwPortMstiStateDiscarding=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,2))
hwPortMstiStateDiscarding.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hwPortMstiStateDiscarding.setStatus(_A)
hwBridgeLostRootPrimary=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,3))
hwBridgeLostRootPrimary.setObjects((_E,_H))
if mibBuilder.loadTexts:hwBridgeLostRootPrimary.setStatus(_A)
hwPortMstiRootGuarded=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,4))
hwPortMstiRootGuarded.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hwPortMstiRootGuarded.setStatus(_A)
hwPortMstiBpduGuarded=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,5))
hwPortMstiBpduGuarded.setObjects(*((_L,_M),(_E,_N)))
if mibBuilder.loadTexts:hwPortMstiBpduGuarded.setStatus(_A)
hwPortMstiLoopGuarded=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,6))
hwPortMstiLoopGuarded.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hwPortMstiLoopGuarded.setStatus(_A)
hwMstiNewRoot=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,7))
hwMstiNewRoot.setObjects(*((_E,_H),(_E,_O),(_E,_O)))
if mibBuilder.loadTexts:hwMstiNewRoot.setStatus(_A)
hwPortPvstBpduProtection=NotificationType((1,3,6,1,4,1,2011,2,23,1,14,0,8))
hwPortPvstBpduProtection.setObjects(*((_L,_M),(_E,_N)))
if mibBuilder.loadTexts:hwPortPvstBpduProtection.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:EnabledStatus,'BridgeId':BridgeId,'Hwdot1sFormatStatus':Hwdot1sFormatStatus,'hwdot1sMstp':hwdot1sMstp,'hwMstpEventsV2':hwMstpEventsV2,'hwPortMstiStateForwarding':hwPortMstiStateForwarding,'hwPortMstiStateDiscarding':hwPortMstiStateDiscarding,'hwBridgeLostRootPrimary':hwBridgeLostRootPrimary,'hwPortMstiRootGuarded':hwPortMstiRootGuarded,'hwPortMstiBpduGuarded':hwPortMstiBpduGuarded,'hwPortMstiLoopGuarded':hwPortMstiLoopGuarded,'hwMstiNewRoot':hwMstiNewRoot,'hwPortPvstBpduProtection':hwPortPvstBpduProtection,'hwdot1sStpStatus':hwdot1sStpStatus,'hwdot1sStpForceVersion':hwdot1sStpForceVersion,'hwdot1sStpDiameter':hwdot1sStpDiameter,'hwdot1sMstBridgeMaxHops':hwdot1sMstBridgeMaxHops,'hwdot1sMstMasterBridgeID':hwdot1sMstMasterBridgeID,'hwdot1sMstMasterPathCost':hwdot1sMstMasterPathCost,'hwdot1sMstBpduGuard':hwdot1sMstBpduGuard,'hwdot1sMstAdminFormatSelector':hwdot1sMstAdminFormatSelector,'hwdot1sMstAdminRegionName':hwdot1sMstAdminRegionName,'hwdot1sMstAdminRevisionLevel':hwdot1sMstAdminRevisionLevel,'hwdot1sMstOperFormatSelector':hwdot1sMstOperFormatSelector,'hwdot1sMstOperRegionName':hwdot1sMstOperRegionName,'hwdot1sMstOperRevisionLevel':hwdot1sMstOperRevisionLevel,'hwdot1sMstOperConfigDigest':hwdot1sMstOperConfigDigest,'hwdot1sMstRegionConfActive':hwdot1sMstRegionConfActive,'hwdot1sMstDefaultVlanAllo':hwdot1sMstDefaultVlanAllo,'hwdot1sMstDefaultRegionName':hwdot1sMstDefaultRegionName,'hwdot1sVIDAllocationTable':hwdot1sVIDAllocationTable,'hwdot1sVIDAllocationEntry':hwdot1sVIDAllocationEntry,_R:hwdot1sMstVID,'hwdot1sAdminMstID':hwdot1sAdminMstID,'hwdot1sOperMstID':hwdot1sOperMstID,'hwdot1sInstanceTable':hwdot1sInstanceTable,'hwdot1sInstanceEntry':hwdot1sInstanceEntry,_H:hwdot1sInstanceID,'hwdot1sMstiBridgeID':hwdot1sMstiBridgeID,'hwdot1sMstiBridgePriority':hwdot1sMstiBridgePriority,_O:hwdot1sMstiDesignedRoot,'hwdot1sMstiRootPathCost':hwdot1sMstiRootPathCost,'hwdot1sMstiRootPort':hwdot1sMstiRootPort,'hwdot1sMstiRootType':hwdot1sMstiRootType,'hwdot1sMstiRemainingHops':hwdot1sMstiRemainingHops,'hwdot1sMstiAdminMappedVlanListLow':hwdot1sMstiAdminMappedVlanListLow,'hwdot1sMstiAdminMappedVlanListHigh':hwdot1sMstiAdminMappedVlanListHigh,'hwdot1sMstiOperMappedVlanListLow':hwdot1sMstiOperMappedVlanListLow,'hwdot1sMstiOperMappedVlanListHigh':hwdot1sMstiOperMappedVlanListHigh,'hwdot1sPortTable':hwdot1sPortTable,'hwdot1sPortEntry':hwdot1sPortEntry,_I:hwdot1sMstiPortIndex,'hwdot1sMstiState':hwdot1sMstiState,'hwdot1sMstiPortPriority':hwdot1sMstiPortPriority,'hwdot1sMstiPathCost':hwdot1sMstiPathCost,'hwdot1sMstiDesignatedRoot':hwdot1sMstiDesignatedRoot,'hwdot1sMstiDesignatedCost':hwdot1sMstiDesignatedCost,_N:hwdot1sMstiDesignatedBridge,'hwdot1sMstiDesignatedPort':hwdot1sMstiDesignatedPort,'hwdot1sMstiMasterBridgeID':hwdot1sMstiMasterBridgeID,'hwdot1sMstiMasterPortCost':hwdot1sMstiMasterPortCost,'hwdot1sMstiStpPortEdgeport':hwdot1sMstiStpPortEdgeport,'hwdot1sMstiStpPortPointToPoint':hwdot1sMstiStpPortPointToPoint,'hwdot1sMstiStpMcheck':hwdot1sMstiStpMcheck,'hwdot1sMstiStpTransLimit':hwdot1sMstiStpTransLimit,'hwdot1sMstiStpRXStpBPDU':hwdot1sMstiStpRXStpBPDU,'hwdot1sMstiStpTXStpBPDU':hwdot1sMstiStpTXStpBPDU,'hwdot1sMstiStpRXTCNBPDU':hwdot1sMstiStpRXTCNBPDU,'hwdot1sMstiStpTXTCNBPDU':hwdot1sMstiStpTXTCNBPDU,'hwdot1sMstiStpRXRSTPBPDU':hwdot1sMstiStpRXRSTPBPDU,'hwdot1sMstiStpTXRSTPBPDU':hwdot1sMstiStpTXRSTPBPDU,'hwdot1sMstiStpRXMSTPBPDU':hwdot1sMstiStpRXMSTPBPDU,'hwdot1sMstiStpTXMSTPBPDU':hwdot1sMstiStpTXMSTPBPDU,'hwdot1sMstiStpClearStatistics':hwdot1sMstiStpClearStatistics,'hwdot1sMstiStpDefaultPortCost':hwdot1sMstiStpDefaultPortCost,'hwdot1sMstiStpStatus':hwdot1sMstiStpStatus,'hwdot1sMstiPortRootGuard':hwdot1sMstiPortRootGuard,'hwdot1sMstiPortLoopGuard':hwdot1sMstiPortLoopGuard,'hwdot1sMstiStpPortSendingBPDUType':hwdot1sMstiStpPortSendingBPDUType,'hwdot1sMstiStpOperPortPointToPoint':hwdot1sMstiStpOperPortPointToPoint,'hwdot1sMstiStpPortAdminBPDUFmt':hwdot1sMstiStpPortAdminBPDUFmt,'hwdot1sMstiStpPortOperBPDUFmt':hwdot1sMstiStpPortOperBPDUFmt,'hwdot1sMstiStpPortRoleRestriction':hwdot1sMstiStpPortRoleRestriction,'hwdot1sMstiStpPortTcRestriction':hwdot1sMstiStpPortTcRestriction,'hwdot1sMstiStpPortDisputed':hwdot1sMstiStpPortDisputed,'hwdot1sStpPathCostStandard':hwdot1sStpPathCostStandard})