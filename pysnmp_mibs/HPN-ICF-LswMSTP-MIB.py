_R='hpnicfdot1sMstVID'
_Q='legacy'
_P='disabled'
_O='hpnicfdot1sMstiDesignedRoot'
_N='hpnicfdot1sMstiDesignatedBridge'
_M='dot1dStpPort'
_L='BRIDGE-MIB'
_K='unused'
_J='enable'
_I='hpnicfdot1sMstiPortIndex'
_H='hpnicfdot1sInstanceID'
_G='EnabledStatus'
_F='OctetString'
_E='HPN-ICF-LswMSTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols(_L,_M,'dot1dStpPortEntry')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfdot1sMstp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,14))
if mibBuilder.loadTexts:hpnicfdot1sMstp.setRevisions(('2001-06-29 00:00',))
class BridgeId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
class Hpnicfdot1sFormatStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('dot1s',2),('auto',3)))
_HpnicfMstpEventsV2_ObjectIdentity=ObjectIdentity
hpnicfMstpEventsV2=_HpnicfMstpEventsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0))
if mibBuilder.loadTexts:hpnicfMstpEventsV2.setStatus(_A)
class _Hpnicfdot1sStpStatus_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sStpStatus_Type.__name__=_G
_Hpnicfdot1sStpStatus_Object=MibScalar
hpnicfdot1sStpStatus=_Hpnicfdot1sStpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,1),_Hpnicfdot1sStpStatus_Type())
hpnicfdot1sStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sStpStatus.setStatus(_A)
class _Hpnicfdot1sStpForceVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stp',0),('rstp',2),('mstp',3)))
_Hpnicfdot1sStpForceVersion_Type.__name__=_C
_Hpnicfdot1sStpForceVersion_Object=MibScalar
hpnicfdot1sStpForceVersion=_Hpnicfdot1sStpForceVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,2),_Hpnicfdot1sStpForceVersion_Type())
hpnicfdot1sStpForceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sStpForceVersion.setStatus(_A)
class _Hpnicfdot1sStpDiameter_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_Hpnicfdot1sStpDiameter_Type.__name__=_C
_Hpnicfdot1sStpDiameter_Object=MibScalar
hpnicfdot1sStpDiameter=_Hpnicfdot1sStpDiameter_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,3),_Hpnicfdot1sStpDiameter_Type())
hpnicfdot1sStpDiameter.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sStpDiameter.setStatus(_A)
class _Hpnicfdot1sMstBridgeMaxHops_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_Hpnicfdot1sMstBridgeMaxHops_Type.__name__=_C
_Hpnicfdot1sMstBridgeMaxHops_Object=MibScalar
hpnicfdot1sMstBridgeMaxHops=_Hpnicfdot1sMstBridgeMaxHops_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,4),_Hpnicfdot1sMstBridgeMaxHops_Type())
hpnicfdot1sMstBridgeMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstBridgeMaxHops.setStatus(_A)
_Hpnicfdot1sMstMasterBridgeID_Type=BridgeId
_Hpnicfdot1sMstMasterBridgeID_Object=MibScalar
hpnicfdot1sMstMasterBridgeID=_Hpnicfdot1sMstMasterBridgeID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,5),_Hpnicfdot1sMstMasterBridgeID_Type())
hpnicfdot1sMstMasterBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstMasterBridgeID.setStatus(_A)
class _Hpnicfdot1sMstMasterPathCost_Type(Integer32):defaultValue=0
_Hpnicfdot1sMstMasterPathCost_Type.__name__=_C
_Hpnicfdot1sMstMasterPathCost_Object=MibScalar
hpnicfdot1sMstMasterPathCost=_Hpnicfdot1sMstMasterPathCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,6),_Hpnicfdot1sMstMasterPathCost_Type())
hpnicfdot1sMstMasterPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstMasterPathCost.setStatus(_A)
class _Hpnicfdot1sMstBpduGuard_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstBpduGuard_Type.__name__=_G
_Hpnicfdot1sMstBpduGuard_Object=MibScalar
hpnicfdot1sMstBpduGuard=_Hpnicfdot1sMstBpduGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,7),_Hpnicfdot1sMstBpduGuard_Type())
hpnicfdot1sMstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstBpduGuard.setStatus(_A)
class _Hpnicfdot1sMstAdminFormatSelector_Type(Integer32):defaultValue=0
_Hpnicfdot1sMstAdminFormatSelector_Type.__name__=_C
_Hpnicfdot1sMstAdminFormatSelector_Object=MibScalar
hpnicfdot1sMstAdminFormatSelector=_Hpnicfdot1sMstAdminFormatSelector_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,8),_Hpnicfdot1sMstAdminFormatSelector_Type())
hpnicfdot1sMstAdminFormatSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstAdminFormatSelector.setStatus(_A)
class _Hpnicfdot1sMstAdminRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hpnicfdot1sMstAdminRegionName_Type.__name__=_F
_Hpnicfdot1sMstAdminRegionName_Object=MibScalar
hpnicfdot1sMstAdminRegionName=_Hpnicfdot1sMstAdminRegionName_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,9),_Hpnicfdot1sMstAdminRegionName_Type())
hpnicfdot1sMstAdminRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstAdminRegionName.setStatus(_A)
class _Hpnicfdot1sMstAdminRevisionLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hpnicfdot1sMstAdminRevisionLevel_Type.__name__=_C
_Hpnicfdot1sMstAdminRevisionLevel_Object=MibScalar
hpnicfdot1sMstAdminRevisionLevel=_Hpnicfdot1sMstAdminRevisionLevel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,10),_Hpnicfdot1sMstAdminRevisionLevel_Type())
hpnicfdot1sMstAdminRevisionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstAdminRevisionLevel.setStatus(_A)
class _Hpnicfdot1sMstOperFormatSelector_Type(Integer32):defaultValue=0
_Hpnicfdot1sMstOperFormatSelector_Type.__name__=_C
_Hpnicfdot1sMstOperFormatSelector_Object=MibScalar
hpnicfdot1sMstOperFormatSelector=_Hpnicfdot1sMstOperFormatSelector_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,11),_Hpnicfdot1sMstOperFormatSelector_Type())
hpnicfdot1sMstOperFormatSelector.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstOperFormatSelector.setStatus(_A)
class _Hpnicfdot1sMstOperRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Hpnicfdot1sMstOperRegionName_Type.__name__=_F
_Hpnicfdot1sMstOperRegionName_Object=MibScalar
hpnicfdot1sMstOperRegionName=_Hpnicfdot1sMstOperRegionName_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,12),_Hpnicfdot1sMstOperRegionName_Type())
hpnicfdot1sMstOperRegionName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstOperRegionName.setStatus(_A)
class _Hpnicfdot1sMstOperRevisionLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hpnicfdot1sMstOperRevisionLevel_Type.__name__=_C
_Hpnicfdot1sMstOperRevisionLevel_Object=MibScalar
hpnicfdot1sMstOperRevisionLevel=_Hpnicfdot1sMstOperRevisionLevel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,13),_Hpnicfdot1sMstOperRevisionLevel_Type())
hpnicfdot1sMstOperRevisionLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstOperRevisionLevel.setStatus(_A)
class _Hpnicfdot1sMstOperConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Hpnicfdot1sMstOperConfigDigest_Type.__name__=_F
_Hpnicfdot1sMstOperConfigDigest_Object=MibScalar
hpnicfdot1sMstOperConfigDigest=_Hpnicfdot1sMstOperConfigDigest_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,14),_Hpnicfdot1sMstOperConfigDigest_Type())
hpnicfdot1sMstOperConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstOperConfigDigest.setStatus(_A)
class _Hpnicfdot1sMstRegionConfActive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('disable',2)))
_Hpnicfdot1sMstRegionConfActive_Type.__name__=_C
_Hpnicfdot1sMstRegionConfActive_Object=MibScalar
hpnicfdot1sMstRegionConfActive=_Hpnicfdot1sMstRegionConfActive_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,15),_Hpnicfdot1sMstRegionConfActive_Type())
hpnicfdot1sMstRegionConfActive.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstRegionConfActive.setStatus(_A)
class _Hpnicfdot1sMstDefaultVlanAllo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hpnicfdot1sMstDefaultVlanAllo_Type.__name__=_C
_Hpnicfdot1sMstDefaultVlanAllo_Object=MibScalar
hpnicfdot1sMstDefaultVlanAllo=_Hpnicfdot1sMstDefaultVlanAllo_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,16),_Hpnicfdot1sMstDefaultVlanAllo_Type())
hpnicfdot1sMstDefaultVlanAllo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstDefaultVlanAllo.setStatus(_A)
class _Hpnicfdot1sMstDefaultRegionName_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hpnicfdot1sMstDefaultRegionName_Type.__name__=_C
_Hpnicfdot1sMstDefaultRegionName_Object=MibScalar
hpnicfdot1sMstDefaultRegionName=_Hpnicfdot1sMstDefaultRegionName_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,17),_Hpnicfdot1sMstDefaultRegionName_Type())
hpnicfdot1sMstDefaultRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstDefaultRegionName.setStatus(_A)
_Hpnicfdot1sVIDAllocationTable_Object=MibTable
hpnicfdot1sVIDAllocationTable=_Hpnicfdot1sVIDAllocationTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,18))
if mibBuilder.loadTexts:hpnicfdot1sVIDAllocationTable.setStatus(_A)
_Hpnicfdot1sVIDAllocationEntry_Object=MibTableRow
hpnicfdot1sVIDAllocationEntry=_Hpnicfdot1sVIDAllocationEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,18,1))
hpnicfdot1sVIDAllocationEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hpnicfdot1sVIDAllocationEntry.setStatus(_A)
class _Hpnicfdot1sMstVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Hpnicfdot1sMstVID_Type.__name__=_C
_Hpnicfdot1sMstVID_Object=MibTableColumn
hpnicfdot1sMstVID=_Hpnicfdot1sMstVID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,18,1,1),_Hpnicfdot1sMstVID_Type())
hpnicfdot1sMstVID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstVID.setStatus(_A)
class _Hpnicfdot1sAdminMstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hpnicfdot1sAdminMstID_Type.__name__=_C
_Hpnicfdot1sAdminMstID_Object=MibTableColumn
hpnicfdot1sAdminMstID=_Hpnicfdot1sAdminMstID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,18,1,2),_Hpnicfdot1sAdminMstID_Type())
hpnicfdot1sAdminMstID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sAdminMstID.setStatus(_A)
class _Hpnicfdot1sOperMstID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hpnicfdot1sOperMstID_Type.__name__=_C
_Hpnicfdot1sOperMstID_Object=MibTableColumn
hpnicfdot1sOperMstID=_Hpnicfdot1sOperMstID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,18,1,3),_Hpnicfdot1sOperMstID_Type())
hpnicfdot1sOperMstID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sOperMstID.setStatus(_A)
_Hpnicfdot1sInstanceTable_Object=MibTable
hpnicfdot1sInstanceTable=_Hpnicfdot1sInstanceTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19))
if mibBuilder.loadTexts:hpnicfdot1sInstanceTable.setStatus(_A)
_Hpnicfdot1sInstanceEntry_Object=MibTableRow
hpnicfdot1sInstanceEntry=_Hpnicfdot1sInstanceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1))
hpnicfdot1sInstanceEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnicfdot1sInstanceEntry.setStatus(_A)
class _Hpnicfdot1sInstanceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_Hpnicfdot1sInstanceID_Type.__name__=_C
_Hpnicfdot1sInstanceID_Object=MibTableColumn
hpnicfdot1sInstanceID=_Hpnicfdot1sInstanceID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,1),_Hpnicfdot1sInstanceID_Type())
hpnicfdot1sInstanceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sInstanceID.setStatus(_A)
_Hpnicfdot1sMstiBridgeID_Type=BridgeId
_Hpnicfdot1sMstiBridgeID_Object=MibTableColumn
hpnicfdot1sMstiBridgeID=_Hpnicfdot1sMstiBridgeID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,2),_Hpnicfdot1sMstiBridgeID_Type())
hpnicfdot1sMstiBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiBridgeID.setStatus(_A)
class _Hpnicfdot1sMstiBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Hpnicfdot1sMstiBridgePriority_Type.__name__=_C
_Hpnicfdot1sMstiBridgePriority_Object=MibTableColumn
hpnicfdot1sMstiBridgePriority=_Hpnicfdot1sMstiBridgePriority_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,3),_Hpnicfdot1sMstiBridgePriority_Type())
hpnicfdot1sMstiBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiBridgePriority.setStatus(_A)
_Hpnicfdot1sMstiDesignedRoot_Type=BridgeId
_Hpnicfdot1sMstiDesignedRoot_Object=MibTableColumn
hpnicfdot1sMstiDesignedRoot=_Hpnicfdot1sMstiDesignedRoot_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,4),_Hpnicfdot1sMstiDesignedRoot_Type())
hpnicfdot1sMstiDesignedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiDesignedRoot.setStatus(_A)
_Hpnicfdot1sMstiRootPathCost_Type=Integer32
_Hpnicfdot1sMstiRootPathCost_Object=MibTableColumn
hpnicfdot1sMstiRootPathCost=_Hpnicfdot1sMstiRootPathCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,5),_Hpnicfdot1sMstiRootPathCost_Type())
hpnicfdot1sMstiRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiRootPathCost.setStatus(_A)
_Hpnicfdot1sMstiRootPort_Type=Integer32
_Hpnicfdot1sMstiRootPort_Object=MibTableColumn
hpnicfdot1sMstiRootPort=_Hpnicfdot1sMstiRootPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,6),_Hpnicfdot1sMstiRootPort_Type())
hpnicfdot1sMstiRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiRootPort.setStatus(_A)
class _Hpnicfdot1sMstiRootType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('secondary',1),('primary',2)))
_Hpnicfdot1sMstiRootType_Type.__name__=_C
_Hpnicfdot1sMstiRootType_Object=MibTableColumn
hpnicfdot1sMstiRootType=_Hpnicfdot1sMstiRootType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,7),_Hpnicfdot1sMstiRootType_Type())
hpnicfdot1sMstiRootType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiRootType.setStatus(_A)
_Hpnicfdot1sMstiRemainingHops_Type=Integer32
_Hpnicfdot1sMstiRemainingHops_Object=MibTableColumn
hpnicfdot1sMstiRemainingHops=_Hpnicfdot1sMstiRemainingHops_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,8),_Hpnicfdot1sMstiRemainingHops_Type())
hpnicfdot1sMstiRemainingHops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiRemainingHops.setStatus(_A)
class _Hpnicfdot1sMstiAdminMappedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hpnicfdot1sMstiAdminMappedVlanListLow_Type.__name__=_F
_Hpnicfdot1sMstiAdminMappedVlanListLow_Object=MibTableColumn
hpnicfdot1sMstiAdminMappedVlanListLow=_Hpnicfdot1sMstiAdminMappedVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,9),_Hpnicfdot1sMstiAdminMappedVlanListLow_Type())
hpnicfdot1sMstiAdminMappedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiAdminMappedVlanListLow.setStatus(_A)
class _Hpnicfdot1sMstiAdminMappedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hpnicfdot1sMstiAdminMappedVlanListHigh_Type.__name__=_F
_Hpnicfdot1sMstiAdminMappedVlanListHigh_Object=MibTableColumn
hpnicfdot1sMstiAdminMappedVlanListHigh=_Hpnicfdot1sMstiAdminMappedVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,10),_Hpnicfdot1sMstiAdminMappedVlanListHigh_Type())
hpnicfdot1sMstiAdminMappedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiAdminMappedVlanListHigh.setStatus(_A)
class _Hpnicfdot1sMstiOperMappedVlanListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hpnicfdot1sMstiOperMappedVlanListLow_Type.__name__=_F
_Hpnicfdot1sMstiOperMappedVlanListLow_Object=MibTableColumn
hpnicfdot1sMstiOperMappedVlanListLow=_Hpnicfdot1sMstiOperMappedVlanListLow_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,11),_Hpnicfdot1sMstiOperMappedVlanListLow_Type())
hpnicfdot1sMstiOperMappedVlanListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiOperMappedVlanListLow.setStatus(_A)
class _Hpnicfdot1sMstiOperMappedVlanListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_Hpnicfdot1sMstiOperMappedVlanListHigh_Type.__name__=_F
_Hpnicfdot1sMstiOperMappedVlanListHigh_Object=MibTableColumn
hpnicfdot1sMstiOperMappedVlanListHigh=_Hpnicfdot1sMstiOperMappedVlanListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,19,1,12),_Hpnicfdot1sMstiOperMappedVlanListHigh_Type())
hpnicfdot1sMstiOperMappedVlanListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiOperMappedVlanListHigh.setStatus(_A)
_Hpnicfdot1sPortTable_Object=MibTable
hpnicfdot1sPortTable=_Hpnicfdot1sPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20))
if mibBuilder.loadTexts:hpnicfdot1sPortTable.setStatus(_A)
_Hpnicfdot1sPortEntry_Object=MibTableRow
hpnicfdot1sPortEntry=_Hpnicfdot1sPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1))
hpnicfdot1sPortEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfdot1sPortEntry.setStatus(_A)
class _Hpnicfdot1sMstiPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hpnicfdot1sMstiPortIndex_Type.__name__=_C
_Hpnicfdot1sMstiPortIndex_Object=MibTableColumn
hpnicfdot1sMstiPortIndex=_Hpnicfdot1sMstiPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,1),_Hpnicfdot1sMstiPortIndex_Type())
hpnicfdot1sMstiPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiPortIndex.setStatus(_A)
class _Hpnicfdot1sMstiState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_P,1),('discarding',2),('learning',4),('forwarding',5)))
_Hpnicfdot1sMstiState_Type.__name__=_C
_Hpnicfdot1sMstiState_Object=MibTableColumn
hpnicfdot1sMstiState=_Hpnicfdot1sMstiState_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,2),_Hpnicfdot1sMstiState_Type())
hpnicfdot1sMstiState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiState.setStatus(_A)
class _Hpnicfdot1sMstiPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Hpnicfdot1sMstiPortPriority_Type.__name__=_C
_Hpnicfdot1sMstiPortPriority_Object=MibTableColumn
hpnicfdot1sMstiPortPriority=_Hpnicfdot1sMstiPortPriority_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,3),_Hpnicfdot1sMstiPortPriority_Type())
hpnicfdot1sMstiPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiPortPriority.setStatus(_A)
class _Hpnicfdot1sMstiPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Hpnicfdot1sMstiPathCost_Type.__name__=_C
_Hpnicfdot1sMstiPathCost_Object=MibTableColumn
hpnicfdot1sMstiPathCost=_Hpnicfdot1sMstiPathCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,4),_Hpnicfdot1sMstiPathCost_Type())
hpnicfdot1sMstiPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiPathCost.setStatus(_A)
_Hpnicfdot1sMstiDesignatedRoot_Type=BridgeId
_Hpnicfdot1sMstiDesignatedRoot_Object=MibTableColumn
hpnicfdot1sMstiDesignatedRoot=_Hpnicfdot1sMstiDesignatedRoot_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,5),_Hpnicfdot1sMstiDesignatedRoot_Type())
hpnicfdot1sMstiDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiDesignatedRoot.setStatus(_A)
_Hpnicfdot1sMstiDesignatedCost_Type=Integer32
_Hpnicfdot1sMstiDesignatedCost_Object=MibTableColumn
hpnicfdot1sMstiDesignatedCost=_Hpnicfdot1sMstiDesignatedCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,6),_Hpnicfdot1sMstiDesignatedCost_Type())
hpnicfdot1sMstiDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiDesignatedCost.setStatus(_A)
_Hpnicfdot1sMstiDesignatedBridge_Type=BridgeId
_Hpnicfdot1sMstiDesignatedBridge_Object=MibTableColumn
hpnicfdot1sMstiDesignatedBridge=_Hpnicfdot1sMstiDesignatedBridge_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,7),_Hpnicfdot1sMstiDesignatedBridge_Type())
hpnicfdot1sMstiDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiDesignatedBridge.setStatus(_A)
class _Hpnicfdot1sMstiDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_Hpnicfdot1sMstiDesignatedPort_Type.__name__=_F
_Hpnicfdot1sMstiDesignatedPort_Object=MibTableColumn
hpnicfdot1sMstiDesignatedPort=_Hpnicfdot1sMstiDesignatedPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,8),_Hpnicfdot1sMstiDesignatedPort_Type())
hpnicfdot1sMstiDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiDesignatedPort.setStatus(_A)
_Hpnicfdot1sMstiMasterBridgeID_Type=BridgeId
_Hpnicfdot1sMstiMasterBridgeID_Object=MibTableColumn
hpnicfdot1sMstiMasterBridgeID=_Hpnicfdot1sMstiMasterBridgeID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,9),_Hpnicfdot1sMstiMasterBridgeID_Type())
hpnicfdot1sMstiMasterBridgeID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiMasterBridgeID.setStatus(_A)
_Hpnicfdot1sMstiMasterPortCost_Type=Integer32
_Hpnicfdot1sMstiMasterPortCost_Object=MibTableColumn
hpnicfdot1sMstiMasterPortCost=_Hpnicfdot1sMstiMasterPortCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,10),_Hpnicfdot1sMstiMasterPortCost_Type())
hpnicfdot1sMstiMasterPortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiMasterPortCost.setStatus(_A)
class _Hpnicfdot1sMstiStpPortEdgeport_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstiStpPortEdgeport_Type.__name__=_G
_Hpnicfdot1sMstiStpPortEdgeport_Object=MibTableColumn
hpnicfdot1sMstiStpPortEdgeport=_Hpnicfdot1sMstiStpPortEdgeport_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,11),_Hpnicfdot1sMstiStpPortEdgeport_Type())
hpnicfdot1sMstiStpPortEdgeport.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortEdgeport.setStatus(_A)
class _Hpnicfdot1sMstiStpPortPointToPoint_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_Hpnicfdot1sMstiStpPortPointToPoint_Type.__name__=_C
_Hpnicfdot1sMstiStpPortPointToPoint_Object=MibTableColumn
hpnicfdot1sMstiStpPortPointToPoint=_Hpnicfdot1sMstiStpPortPointToPoint_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,12),_Hpnicfdot1sMstiStpPortPointToPoint_Type())
hpnicfdot1sMstiStpPortPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortPointToPoint.setStatus(_A)
class _Hpnicfdot1sMstiStpMcheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hpnicfdot1sMstiStpMcheck_Type.__name__=_C
_Hpnicfdot1sMstiStpMcheck_Object=MibTableColumn
hpnicfdot1sMstiStpMcheck=_Hpnicfdot1sMstiStpMcheck_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,13),_Hpnicfdot1sMstiStpMcheck_Type())
hpnicfdot1sMstiStpMcheck.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpMcheck.setStatus(_A)
class _Hpnicfdot1sMstiStpTransLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hpnicfdot1sMstiStpTransLimit_Type.__name__=_C
_Hpnicfdot1sMstiStpTransLimit_Object=MibTableColumn
hpnicfdot1sMstiStpTransLimit=_Hpnicfdot1sMstiStpTransLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,14),_Hpnicfdot1sMstiStpTransLimit_Type())
hpnicfdot1sMstiStpTransLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpTransLimit.setStatus(_A)
_Hpnicfdot1sMstiStpRXStpBPDU_Type=Counter32
_Hpnicfdot1sMstiStpRXStpBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpRXStpBPDU=_Hpnicfdot1sMstiStpRXStpBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,15),_Hpnicfdot1sMstiStpRXStpBPDU_Type())
hpnicfdot1sMstiStpRXStpBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpRXStpBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpTXStpBPDU_Type=Counter32
_Hpnicfdot1sMstiStpTXStpBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpTXStpBPDU=_Hpnicfdot1sMstiStpTXStpBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,16),_Hpnicfdot1sMstiStpTXStpBPDU_Type())
hpnicfdot1sMstiStpTXStpBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpTXStpBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpRXTCNBPDU_Type=Counter32
_Hpnicfdot1sMstiStpRXTCNBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpRXTCNBPDU=_Hpnicfdot1sMstiStpRXTCNBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,17),_Hpnicfdot1sMstiStpRXTCNBPDU_Type())
hpnicfdot1sMstiStpRXTCNBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpRXTCNBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpTXTCNBPDU_Type=Counter32
_Hpnicfdot1sMstiStpTXTCNBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpTXTCNBPDU=_Hpnicfdot1sMstiStpTXTCNBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,18),_Hpnicfdot1sMstiStpTXTCNBPDU_Type())
hpnicfdot1sMstiStpTXTCNBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpTXTCNBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpRXRSTPBPDU_Type=Counter32
_Hpnicfdot1sMstiStpRXRSTPBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpRXRSTPBPDU=_Hpnicfdot1sMstiStpRXRSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,19),_Hpnicfdot1sMstiStpRXRSTPBPDU_Type())
hpnicfdot1sMstiStpRXRSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpRXRSTPBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpTXRSTPBPDU_Type=Counter32
_Hpnicfdot1sMstiStpTXRSTPBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpTXRSTPBPDU=_Hpnicfdot1sMstiStpTXRSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,20),_Hpnicfdot1sMstiStpTXRSTPBPDU_Type())
hpnicfdot1sMstiStpTXRSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpTXRSTPBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpRXMSTPBPDU_Type=Counter32
_Hpnicfdot1sMstiStpRXMSTPBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpRXMSTPBPDU=_Hpnicfdot1sMstiStpRXMSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,21),_Hpnicfdot1sMstiStpRXMSTPBPDU_Type())
hpnicfdot1sMstiStpRXMSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpRXMSTPBPDU.setStatus(_A)
_Hpnicfdot1sMstiStpTXMSTPBPDU_Type=Counter32
_Hpnicfdot1sMstiStpTXMSTPBPDU_Object=MibTableColumn
hpnicfdot1sMstiStpTXMSTPBPDU=_Hpnicfdot1sMstiStpTXMSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,22),_Hpnicfdot1sMstiStpTXMSTPBPDU_Type())
hpnicfdot1sMstiStpTXMSTPBPDU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpTXMSTPBPDU.setStatus(_A)
class _Hpnicfdot1sMstiStpClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*(('clear',1),(_K,65535)))
_Hpnicfdot1sMstiStpClearStatistics_Type.__name__=_C
_Hpnicfdot1sMstiStpClearStatistics_Object=MibTableColumn
hpnicfdot1sMstiStpClearStatistics=_Hpnicfdot1sMstiStpClearStatistics_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,23),_Hpnicfdot1sMstiStpClearStatistics_Type())
hpnicfdot1sMstiStpClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpClearStatistics.setStatus(_A)
class _Hpnicfdot1sMstiStpDefaultPortCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,65535)));namedValues=NamedValues(*((_J,1),(_K,65535)))
_Hpnicfdot1sMstiStpDefaultPortCost_Type.__name__=_C
_Hpnicfdot1sMstiStpDefaultPortCost_Object=MibTableColumn
hpnicfdot1sMstiStpDefaultPortCost=_Hpnicfdot1sMstiStpDefaultPortCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,24),_Hpnicfdot1sMstiStpDefaultPortCost_Type())
hpnicfdot1sMstiStpDefaultPortCost.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpDefaultPortCost.setStatus(_A)
class _Hpnicfdot1sMstiStpStatus_Type(EnabledStatus):defaultValue=1
_Hpnicfdot1sMstiStpStatus_Type.__name__=_G
_Hpnicfdot1sMstiStpStatus_Object=MibTableColumn
hpnicfdot1sMstiStpStatus=_Hpnicfdot1sMstiStpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,25),_Hpnicfdot1sMstiStpStatus_Type())
hpnicfdot1sMstiStpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpStatus.setStatus(_A)
class _Hpnicfdot1sMstiPortRootGuard_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstiPortRootGuard_Type.__name__=_G
_Hpnicfdot1sMstiPortRootGuard_Object=MibTableColumn
hpnicfdot1sMstiPortRootGuard=_Hpnicfdot1sMstiPortRootGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,26),_Hpnicfdot1sMstiPortRootGuard_Type())
hpnicfdot1sMstiPortRootGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiPortRootGuard.setStatus(_A)
class _Hpnicfdot1sMstiPortLoopGuard_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstiPortLoopGuard_Type.__name__=_G
_Hpnicfdot1sMstiPortLoopGuard_Object=MibTableColumn
hpnicfdot1sMstiPortLoopGuard=_Hpnicfdot1sMstiPortLoopGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,27),_Hpnicfdot1sMstiPortLoopGuard_Type())
hpnicfdot1sMstiPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiPortLoopGuard.setStatus(_A)
class _Hpnicfdot1sMstiStpPortSendingBPDUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_Hpnicfdot1sMstiStpPortSendingBPDUType_Type.__name__=_C
_Hpnicfdot1sMstiStpPortSendingBPDUType_Object=MibTableColumn
hpnicfdot1sMstiStpPortSendingBPDUType=_Hpnicfdot1sMstiStpPortSendingBPDUType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,28),_Hpnicfdot1sMstiStpPortSendingBPDUType_Type())
hpnicfdot1sMstiStpPortSendingBPDUType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortSendingBPDUType.setStatus(_A)
class _Hpnicfdot1sMstiStpOperPortPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hpnicfdot1sMstiStpOperPortPointToPoint_Type.__name__=_C
_Hpnicfdot1sMstiStpOperPortPointToPoint_Object=MibTableColumn
hpnicfdot1sMstiStpOperPortPointToPoint=_Hpnicfdot1sMstiStpOperPortPointToPoint_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,29),_Hpnicfdot1sMstiStpOperPortPointToPoint_Type())
hpnicfdot1sMstiStpOperPortPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpOperPortPointToPoint.setStatus(_A)
_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Type=Hpnicfdot1sFormatStatus
_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Object=MibTableColumn
hpnicfdot1sMstiStpPortAdminBPDUFmt=_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,30),_Hpnicfdot1sMstiStpPortAdminBPDUFmt_Type())
hpnicfdot1sMstiStpPortAdminBPDUFmt.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortAdminBPDUFmt.setStatus(_A)
_Hpnicfdot1sMstiStpPortOperBPDUFmt_Type=Hpnicfdot1sFormatStatus
_Hpnicfdot1sMstiStpPortOperBPDUFmt_Object=MibTableColumn
hpnicfdot1sMstiStpPortOperBPDUFmt=_Hpnicfdot1sMstiStpPortOperBPDUFmt_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,31),_Hpnicfdot1sMstiStpPortOperBPDUFmt_Type())
hpnicfdot1sMstiStpPortOperBPDUFmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortOperBPDUFmt.setStatus(_A)
class _Hpnicfdot1sMstiStpPortRoleRestriction_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstiStpPortRoleRestriction_Type.__name__=_G
_Hpnicfdot1sMstiStpPortRoleRestriction_Object=MibTableColumn
hpnicfdot1sMstiStpPortRoleRestriction=_Hpnicfdot1sMstiStpPortRoleRestriction_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,32),_Hpnicfdot1sMstiStpPortRoleRestriction_Type())
hpnicfdot1sMstiStpPortRoleRestriction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortRoleRestriction.setStatus(_A)
class _Hpnicfdot1sMstiStpPortTcRestriction_Type(EnabledStatus):defaultValue=2
_Hpnicfdot1sMstiStpPortTcRestriction_Type.__name__=_G
_Hpnicfdot1sMstiStpPortTcRestriction_Object=MibTableColumn
hpnicfdot1sMstiStpPortTcRestriction=_Hpnicfdot1sMstiStpPortTcRestriction_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,33),_Hpnicfdot1sMstiStpPortTcRestriction_Type())
hpnicfdot1sMstiStpPortTcRestriction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortTcRestriction.setStatus(_A)
_Hpnicfdot1sMstiStpPortDisputed_Type=TruthValue
_Hpnicfdot1sMstiStpPortDisputed_Object=MibTableColumn
hpnicfdot1sMstiStpPortDisputed=_Hpnicfdot1sMstiStpPortDisputed_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,20,1,34),_Hpnicfdot1sMstiStpPortDisputed_Type())
hpnicfdot1sMstiStpPortDisputed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1sMstiStpPortDisputed.setStatus(_A)
class _Hpnicfdot1sStpPathCostStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('dot1d-1998',1),('dot1t',2)))
_Hpnicfdot1sStpPathCostStandard_Type.__name__=_C
_Hpnicfdot1sStpPathCostStandard_Object=MibScalar
hpnicfdot1sStpPathCostStandard=_Hpnicfdot1sStpPathCostStandard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,14,21),_Hpnicfdot1sStpPathCostStandard_Type())
hpnicfdot1sStpPathCostStandard.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1sStpPathCostStandard.setStatus(_A)
hpnicfPortMstiStateForwarding=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,1))
hpnicfPortMstiStateForwarding.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hpnicfPortMstiStateForwarding.setStatus(_A)
hpnicfPortMstiStateDiscarding=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,2))
hpnicfPortMstiStateDiscarding.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hpnicfPortMstiStateDiscarding.setStatus(_A)
hpnicfBridgeLostRootPrimary=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,3))
hpnicfBridgeLostRootPrimary.setObjects((_E,_H))
if mibBuilder.loadTexts:hpnicfBridgeLostRootPrimary.setStatus(_A)
hpnicfPortMstiRootGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,4))
hpnicfPortMstiRootGuarded.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hpnicfPortMstiRootGuarded.setStatus(_A)
hpnicfPortMstiBpduGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,5))
hpnicfPortMstiBpduGuarded.setObjects(*((_L,_M),(_E,_N)))
if mibBuilder.loadTexts:hpnicfPortMstiBpduGuarded.setStatus(_A)
hpnicfPortMstiLoopGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,6))
hpnicfPortMstiLoopGuarded.setObjects(*((_E,_H),(_E,_I)))
if mibBuilder.loadTexts:hpnicfPortMstiLoopGuarded.setStatus(_A)
hpnicfMstiNewRoot=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,7))
hpnicfMstiNewRoot.setObjects(*((_E,_H),(_E,_O),(_E,_O)))
if mibBuilder.loadTexts:hpnicfMstiNewRoot.setStatus(_A)
hpnicfPortPvstBpduProtection=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,14,0,8))
hpnicfPortPvstBpduProtection.setObjects(*((_L,_M),(_E,_N)))
if mibBuilder.loadTexts:hpnicfPortPvstBpduProtection.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_G:EnabledStatus,'BridgeId':BridgeId,'Hpnicfdot1sFormatStatus':Hpnicfdot1sFormatStatus,'hpnicfdot1sMstp':hpnicfdot1sMstp,'hpnicfMstpEventsV2':hpnicfMstpEventsV2,'hpnicfPortMstiStateForwarding':hpnicfPortMstiStateForwarding,'hpnicfPortMstiStateDiscarding':hpnicfPortMstiStateDiscarding,'hpnicfBridgeLostRootPrimary':hpnicfBridgeLostRootPrimary,'hpnicfPortMstiRootGuarded':hpnicfPortMstiRootGuarded,'hpnicfPortMstiBpduGuarded':hpnicfPortMstiBpduGuarded,'hpnicfPortMstiLoopGuarded':hpnicfPortMstiLoopGuarded,'hpnicfMstiNewRoot':hpnicfMstiNewRoot,'hpnicfPortPvstBpduProtection':hpnicfPortPvstBpduProtection,'hpnicfdot1sStpStatus':hpnicfdot1sStpStatus,'hpnicfdot1sStpForceVersion':hpnicfdot1sStpForceVersion,'hpnicfdot1sStpDiameter':hpnicfdot1sStpDiameter,'hpnicfdot1sMstBridgeMaxHops':hpnicfdot1sMstBridgeMaxHops,'hpnicfdot1sMstMasterBridgeID':hpnicfdot1sMstMasterBridgeID,'hpnicfdot1sMstMasterPathCost':hpnicfdot1sMstMasterPathCost,'hpnicfdot1sMstBpduGuard':hpnicfdot1sMstBpduGuard,'hpnicfdot1sMstAdminFormatSelector':hpnicfdot1sMstAdminFormatSelector,'hpnicfdot1sMstAdminRegionName':hpnicfdot1sMstAdminRegionName,'hpnicfdot1sMstAdminRevisionLevel':hpnicfdot1sMstAdminRevisionLevel,'hpnicfdot1sMstOperFormatSelector':hpnicfdot1sMstOperFormatSelector,'hpnicfdot1sMstOperRegionName':hpnicfdot1sMstOperRegionName,'hpnicfdot1sMstOperRevisionLevel':hpnicfdot1sMstOperRevisionLevel,'hpnicfdot1sMstOperConfigDigest':hpnicfdot1sMstOperConfigDigest,'hpnicfdot1sMstRegionConfActive':hpnicfdot1sMstRegionConfActive,'hpnicfdot1sMstDefaultVlanAllo':hpnicfdot1sMstDefaultVlanAllo,'hpnicfdot1sMstDefaultRegionName':hpnicfdot1sMstDefaultRegionName,'hpnicfdot1sVIDAllocationTable':hpnicfdot1sVIDAllocationTable,'hpnicfdot1sVIDAllocationEntry':hpnicfdot1sVIDAllocationEntry,_R:hpnicfdot1sMstVID,'hpnicfdot1sAdminMstID':hpnicfdot1sAdminMstID,'hpnicfdot1sOperMstID':hpnicfdot1sOperMstID,'hpnicfdot1sInstanceTable':hpnicfdot1sInstanceTable,'hpnicfdot1sInstanceEntry':hpnicfdot1sInstanceEntry,_H:hpnicfdot1sInstanceID,'hpnicfdot1sMstiBridgeID':hpnicfdot1sMstiBridgeID,'hpnicfdot1sMstiBridgePriority':hpnicfdot1sMstiBridgePriority,_O:hpnicfdot1sMstiDesignedRoot,'hpnicfdot1sMstiRootPathCost':hpnicfdot1sMstiRootPathCost,'hpnicfdot1sMstiRootPort':hpnicfdot1sMstiRootPort,'hpnicfdot1sMstiRootType':hpnicfdot1sMstiRootType,'hpnicfdot1sMstiRemainingHops':hpnicfdot1sMstiRemainingHops,'hpnicfdot1sMstiAdminMappedVlanListLow':hpnicfdot1sMstiAdminMappedVlanListLow,'hpnicfdot1sMstiAdminMappedVlanListHigh':hpnicfdot1sMstiAdminMappedVlanListHigh,'hpnicfdot1sMstiOperMappedVlanListLow':hpnicfdot1sMstiOperMappedVlanListLow,'hpnicfdot1sMstiOperMappedVlanListHigh':hpnicfdot1sMstiOperMappedVlanListHigh,'hpnicfdot1sPortTable':hpnicfdot1sPortTable,'hpnicfdot1sPortEntry':hpnicfdot1sPortEntry,_I:hpnicfdot1sMstiPortIndex,'hpnicfdot1sMstiState':hpnicfdot1sMstiState,'hpnicfdot1sMstiPortPriority':hpnicfdot1sMstiPortPriority,'hpnicfdot1sMstiPathCost':hpnicfdot1sMstiPathCost,'hpnicfdot1sMstiDesignatedRoot':hpnicfdot1sMstiDesignatedRoot,'hpnicfdot1sMstiDesignatedCost':hpnicfdot1sMstiDesignatedCost,_N:hpnicfdot1sMstiDesignatedBridge,'hpnicfdot1sMstiDesignatedPort':hpnicfdot1sMstiDesignatedPort,'hpnicfdot1sMstiMasterBridgeID':hpnicfdot1sMstiMasterBridgeID,'hpnicfdot1sMstiMasterPortCost':hpnicfdot1sMstiMasterPortCost,'hpnicfdot1sMstiStpPortEdgeport':hpnicfdot1sMstiStpPortEdgeport,'hpnicfdot1sMstiStpPortPointToPoint':hpnicfdot1sMstiStpPortPointToPoint,'hpnicfdot1sMstiStpMcheck':hpnicfdot1sMstiStpMcheck,'hpnicfdot1sMstiStpTransLimit':hpnicfdot1sMstiStpTransLimit,'hpnicfdot1sMstiStpRXStpBPDU':hpnicfdot1sMstiStpRXStpBPDU,'hpnicfdot1sMstiStpTXStpBPDU':hpnicfdot1sMstiStpTXStpBPDU,'hpnicfdot1sMstiStpRXTCNBPDU':hpnicfdot1sMstiStpRXTCNBPDU,'hpnicfdot1sMstiStpTXTCNBPDU':hpnicfdot1sMstiStpTXTCNBPDU,'hpnicfdot1sMstiStpRXRSTPBPDU':hpnicfdot1sMstiStpRXRSTPBPDU,'hpnicfdot1sMstiStpTXRSTPBPDU':hpnicfdot1sMstiStpTXRSTPBPDU,'hpnicfdot1sMstiStpRXMSTPBPDU':hpnicfdot1sMstiStpRXMSTPBPDU,'hpnicfdot1sMstiStpTXMSTPBPDU':hpnicfdot1sMstiStpTXMSTPBPDU,'hpnicfdot1sMstiStpClearStatistics':hpnicfdot1sMstiStpClearStatistics,'hpnicfdot1sMstiStpDefaultPortCost':hpnicfdot1sMstiStpDefaultPortCost,'hpnicfdot1sMstiStpStatus':hpnicfdot1sMstiStpStatus,'hpnicfdot1sMstiPortRootGuard':hpnicfdot1sMstiPortRootGuard,'hpnicfdot1sMstiPortLoopGuard':hpnicfdot1sMstiPortLoopGuard,'hpnicfdot1sMstiStpPortSendingBPDUType':hpnicfdot1sMstiStpPortSendingBPDUType,'hpnicfdot1sMstiStpOperPortPointToPoint':hpnicfdot1sMstiStpOperPortPointToPoint,'hpnicfdot1sMstiStpPortAdminBPDUFmt':hpnicfdot1sMstiStpPortAdminBPDUFmt,'hpnicfdot1sMstiStpPortOperBPDUFmt':hpnicfdot1sMstiStpPortOperBPDUFmt,'hpnicfdot1sMstiStpPortRoleRestriction':hpnicfdot1sMstiStpPortRoleRestriction,'hpnicfdot1sMstiStpPortTcRestriction':hpnicfdot1sMstiStpPortTcRestriction,'hpnicfdot1sMstiStpPortDisputed':hpnicfdot1sMstiStpPortDisputed,'hpnicfdot1sStpPathCostStandard':hpnicfdot1sStpPathCostStandard})