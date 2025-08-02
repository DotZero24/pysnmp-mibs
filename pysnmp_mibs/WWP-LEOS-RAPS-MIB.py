_W='wwpLeosRapsVirtualRingAlarm'
_V='wwpLeosRapsVirtualRingName'
_U='wwpLeosRapsVirtualRingMemberVsId'
_T='wwpLeosRapsVirtualRingMemberVlanId'
_S='remoteSignalFailure'
_R='remoteForceSwitch'
_Q='ccmFailure'
_P='blocked'
_O='forwarding'
_N='seconds'
_M='minutes'
_L='not-accessible'
_K='wwpLeosRapsLogicalRingIndex'
_J='localForceSwitch'
_I='off'
_H='milliseconds'
_G='disabled'
_F='wwpLeosRapsVirtualRingIndex'
_E='OctetString'
_D='WWP-LEOS-RAPS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosRapsMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,47))
if mibBuilder.loadTexts:wwpLeosRapsMIB.setRevisions(('2010-09-16 17:00',))
_WwpLeosRapsMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBObjects=_WwpLeosRapsMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1))
_WwpLeosRapsGlobal_ObjectIdentity=ObjectIdentity
wwpLeosRapsGlobal=_WwpLeosRapsGlobal_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1,1))
_WwpLeosRapsGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosRapsGlobalAttrs=_WwpLeosRapsGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1,1,1))
class _WwpLeosRapsState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('enabled',2)))
_WwpLeosRapsState_Type.__name__=_C
_WwpLeosRapsState_Object=MibScalar
wwpLeosRapsState=_WwpLeosRapsState_Object((1,3,6,1,4,1,6141,2,60,47,1,1,1,1),_WwpLeosRapsState_Type())
wwpLeosRapsState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsState.setStatus(_A)
_WwpLeosRapsNodeId_Type=MacAddress
_WwpLeosRapsNodeId_Object=MibScalar
wwpLeosRapsNodeId=_WwpLeosRapsNodeId_Object((1,3,6,1,4,1,6141,2,60,47,1,1,1,2),_WwpLeosRapsNodeId_Type())
wwpLeosRapsNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsNodeId.setStatus(_A)
class _WwpLeosRapsEtherType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_WwpLeosRapsEtherType_Type.__name__=_E
_WwpLeosRapsEtherType_Object=MibScalar
wwpLeosRapsEtherType=_WwpLeosRapsEtherType_Object((1,3,6,1,4,1,6141,2,60,47,1,1,1,3),_WwpLeosRapsEtherType_Type())
wwpLeosRapsEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsEtherType.setStatus(_A)
class _WwpLeosRapsNumberOfRings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRapsNumberOfRings_Type.__name__=_C
_WwpLeosRapsNumberOfRings_Object=MibScalar
wwpLeosRapsNumberOfRings=_WwpLeosRapsNumberOfRings_Object((1,3,6,1,4,1,6141,2,60,47,1,1,1,4),_WwpLeosRapsNumberOfRings_Type())
wwpLeosRapsNumberOfRings.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsNumberOfRings.setStatus(_A)
_WwpLeosRapsLogicalRing_ObjectIdentity=ObjectIdentity
wwpLeosRapsLogicalRing=_WwpLeosRapsLogicalRing_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1,2))
_WwpLeosRapsLogicalRingTable_Object=MibTable
wwpLeosRapsLogicalRingTable=_WwpLeosRapsLogicalRingTable_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1))
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingTable.setStatus(_A)
_WwpLeosRapsLogicalRingEntry_Object=MibTableRow
wwpLeosRapsLogicalRingEntry=_WwpLeosRapsLogicalRingEntry_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1))
wwpLeosRapsLogicalRingEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEntry.setStatus(_A)
class _WwpLeosRapsLogicalRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_WwpLeosRapsLogicalRingIndex_Type.__name__=_C
_WwpLeosRapsLogicalRingIndex_Object=MibTableColumn
wwpLeosRapsLogicalRingIndex=_WwpLeosRapsLogicalRingIndex_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,1),_WwpLeosRapsLogicalRingIndex_Type())
wwpLeosRapsLogicalRingIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingIndex.setStatus(_A)
class _WwpLeosRapsLogicalRingName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosRapsLogicalRingName_Type.__name__=_E
_WwpLeosRapsLogicalRingName_Object=MibTableColumn
wwpLeosRapsLogicalRingName=_WwpLeosRapsLogicalRingName_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,2),_WwpLeosRapsLogicalRingName_Type())
wwpLeosRapsLogicalRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingName.setStatus(_A)
class _WwpLeosRapsLogicalRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpLeosRapsLogicalRingId_Type.__name__=_C
_WwpLeosRapsLogicalRingId_Object=MibTableColumn
wwpLeosRapsLogicalRingId=_WwpLeosRapsLogicalRingId_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,3),_WwpLeosRapsLogicalRingId_Type())
wwpLeosRapsLogicalRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingId.setStatus(_A)
class _WwpLeosRapsLogicalRingGuardTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_WwpLeosRapsLogicalRingGuardTime_Type.__name__=_C
_WwpLeosRapsLogicalRingGuardTime_Object=MibTableColumn
wwpLeosRapsLogicalRingGuardTime=_WwpLeosRapsLogicalRingGuardTime_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,4),_WwpLeosRapsLogicalRingGuardTime_Type())
wwpLeosRapsLogicalRingGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingGuardTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingGuardTime.setUnits(_H)
class _WwpLeosRapsLogicalRingWtr_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_WwpLeosRapsLogicalRingWtr_Type.__name__=_C
_WwpLeosRapsLogicalRingWtr_Object=MibTableColumn
wwpLeosRapsLogicalRingWtr=_WwpLeosRapsLogicalRingWtr_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,5),_WwpLeosRapsLogicalRingWtr_Type())
wwpLeosRapsLogicalRingWtr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWtr.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWtr.setUnits(_M)
_WwpLeosRapsLogicalRingWtb_Type=Integer32
_WwpLeosRapsLogicalRingWtb_Object=MibTableColumn
wwpLeosRapsLogicalRingWtb=_WwpLeosRapsLogicalRingWtb_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,6),_WwpLeosRapsLogicalRingWtb_Type())
wwpLeosRapsLogicalRingWtb.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWtb.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWtb.setUnits(_M)
class _WwpLeosRapsLogicalRingWestPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRapsLogicalRingWestPortId_Type.__name__=_C
_WwpLeosRapsLogicalRingWestPortId_Object=MibTableColumn
wwpLeosRapsLogicalRingWestPortId=_WwpLeosRapsLogicalRingWestPortId_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,7),_WwpLeosRapsLogicalRingWestPortId_Type())
wwpLeosRapsLogicalRingWestPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWestPortId.setStatus(_A)
class _WwpLeosRapsLogicalRingWestHoldOffTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WwpLeosRapsLogicalRingWestHoldOffTime_Type.__name__=_C
_WwpLeosRapsLogicalRingWestHoldOffTime_Object=MibTableColumn
wwpLeosRapsLogicalRingWestHoldOffTime=_WwpLeosRapsLogicalRingWestHoldOffTime_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,8),_WwpLeosRapsLogicalRingWestHoldOffTime_Type())
wwpLeosRapsLogicalRingWestHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWestHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWestHoldOffTime.setUnits(_H)
class _WwpLeosRapsLogicalRingWestForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('on',2)))
_WwpLeosRapsLogicalRingWestForce_Type.__name__=_C
_WwpLeosRapsLogicalRingWestForce_Object=MibTableColumn
wwpLeosRapsLogicalRingWestForce=_WwpLeosRapsLogicalRingWestForce_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,9),_WwpLeosRapsLogicalRingWestForce_Type())
wwpLeosRapsLogicalRingWestForce.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWestForce.setStatus(_A)
class _WwpLeosRapsLogicalRingWestCfmService_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosRapsLogicalRingWestCfmService_Type.__name__=_E
_WwpLeosRapsLogicalRingWestCfmService_Object=MibTableColumn
wwpLeosRapsLogicalRingWestCfmService=_WwpLeosRapsLogicalRingWestCfmService_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,10),_WwpLeosRapsLogicalRingWestCfmService_Type())
wwpLeosRapsLogicalRingWestCfmService.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingWestCfmService.setStatus(_A)
class _WwpLeosRapsLogicalRingEastPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosRapsLogicalRingEastPortId_Type.__name__=_C
_WwpLeosRapsLogicalRingEastPortId_Object=MibTableColumn
wwpLeosRapsLogicalRingEastPortId=_WwpLeosRapsLogicalRingEastPortId_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,11),_WwpLeosRapsLogicalRingEastPortId_Type())
wwpLeosRapsLogicalRingEastPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEastPortId.setStatus(_A)
class _WwpLeosRapsLogicalRingEastHoldOffTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_WwpLeosRapsLogicalRingEastHoldOffTime_Type.__name__=_C
_WwpLeosRapsLogicalRingEastHoldOffTime_Object=MibTableColumn
wwpLeosRapsLogicalRingEastHoldOffTime=_WwpLeosRapsLogicalRingEastHoldOffTime_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,12),_WwpLeosRapsLogicalRingEastHoldOffTime_Type())
wwpLeosRapsLogicalRingEastHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEastHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEastHoldOffTime.setUnits(_H)
class _WwpLeosRapsLogicalRingEastForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('on',2)))
_WwpLeosRapsLogicalRingEastForce_Type.__name__=_C
_WwpLeosRapsLogicalRingEastForce_Object=MibTableColumn
wwpLeosRapsLogicalRingEastForce=_WwpLeosRapsLogicalRingEastForce_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,13),_WwpLeosRapsLogicalRingEastForce_Type())
wwpLeosRapsLogicalRingEastForce.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEastForce.setStatus(_A)
class _WwpLeosRapsLogicalRingEastCfmService_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosRapsLogicalRingEastCfmService_Type.__name__=_E
_WwpLeosRapsLogicalRingEastCfmService_Object=MibTableColumn
wwpLeosRapsLogicalRingEastCfmService=_WwpLeosRapsLogicalRingEastCfmService_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,14),_WwpLeosRapsLogicalRingEastCfmService_Type())
wwpLeosRapsLogicalRingEastCfmService.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingEastCfmService.setStatus(_A)
class _WwpLeosRapsLogicalRingNumberOfVirtualRings_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRapsLogicalRingNumberOfVirtualRings_Type.__name__=_C
_WwpLeosRapsLogicalRingNumberOfVirtualRings_Object=MibTableColumn
wwpLeosRapsLogicalRingNumberOfVirtualRings=_WwpLeosRapsLogicalRingNumberOfVirtualRings_Object((1,3,6,1,4,1,6141,2,60,47,1,2,1,1,15),_WwpLeosRapsLogicalRingNumberOfVirtualRings_Type())
wwpLeosRapsLogicalRingNumberOfVirtualRings.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsLogicalRingNumberOfVirtualRings.setStatus(_A)
_WwpLeosRapsVirtualRing_ObjectIdentity=ObjectIdentity
wwpLeosRapsVirtualRing=_WwpLeosRapsVirtualRing_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1,3))
_WwpLeosRapsVirtualRingTable_Object=MibTable
wwpLeosRapsVirtualRingTable=_WwpLeosRapsVirtualRingTable_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingTable.setStatus(_A)
_WwpLeosRapsVirtualRingEntry_Object=MibTableRow
wwpLeosRapsVirtualRingEntry=_WwpLeosRapsVirtualRingEntry_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1))
wwpLeosRapsVirtualRingEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEntry.setStatus(_A)
class _WwpLeosRapsVirtualRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_WwpLeosRapsVirtualRingIndex_Type.__name__=_C
_WwpLeosRapsVirtualRingIndex_Object=MibTableColumn
wwpLeosRapsVirtualRingIndex=_WwpLeosRapsVirtualRingIndex_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,1),_WwpLeosRapsVirtualRingIndex_Type())
wwpLeosRapsVirtualRingIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingIndex.setStatus(_A)
class _WwpLeosRapsVirtualRingName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosRapsVirtualRingName_Type.__name__=_E
_WwpLeosRapsVirtualRingName_Object=MibTableColumn
wwpLeosRapsVirtualRingName=_WwpLeosRapsVirtualRingName_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,2),_WwpLeosRapsVirtualRingName_Type())
wwpLeosRapsVirtualRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingName.setStatus(_A)
class _WwpLeosRapsVirtualRingVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosRapsVirtualRingVid_Type.__name__=_C
_WwpLeosRapsVirtualRingVid_Object=MibTableColumn
wwpLeosRapsVirtualRingVid=_WwpLeosRapsVirtualRingVid_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,3),_WwpLeosRapsVirtualRingVid_Type())
wwpLeosRapsVirtualRingVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingVid.setStatus(_A)
class _WwpLeosRapsVirtualRingLogicalRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_WwpLeosRapsVirtualRingLogicalRingId_Type.__name__=_C
_WwpLeosRapsVirtualRingLogicalRingId_Object=MibTableColumn
wwpLeosRapsVirtualRingLogicalRingId=_WwpLeosRapsVirtualRingLogicalRingId_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,4),_WwpLeosRapsVirtualRingLogicalRingId_Type())
wwpLeosRapsVirtualRingLogicalRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingLogicalRingId.setStatus(_A)
class _WwpLeosRapsVirtualRingMel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosRapsVirtualRingMel_Type.__name__=_C
_WwpLeosRapsVirtualRingMel_Object=MibTableColumn
wwpLeosRapsVirtualRingMel=_WwpLeosRapsVirtualRingMel_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,5),_WwpLeosRapsVirtualRingMel_Type())
wwpLeosRapsVirtualRingMel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMel.setStatus(_A)
class _WwpLeosRapsVirtualRingRevertive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('on',2)))
_WwpLeosRapsVirtualRingRevertive_Type.__name__=_C
_WwpLeosRapsVirtualRingRevertive_Object=MibTableColumn
wwpLeosRapsVirtualRingRevertive=_WwpLeosRapsVirtualRingRevertive_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,6),_WwpLeosRapsVirtualRingRevertive_Type())
wwpLeosRapsVirtualRingRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingRevertive.setStatus(_A)
class _WwpLeosRapsVirtualRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('adminDisabled',1),('ok',2),('protecting',3),('recovering',4)))
_WwpLeosRapsVirtualRingState_Type.__name__=_C
_WwpLeosRapsVirtualRingState_Object=MibTableColumn
wwpLeosRapsVirtualRingState=_WwpLeosRapsVirtualRingState_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,7),_WwpLeosRapsVirtualRingState_Type())
wwpLeosRapsVirtualRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingState.setStatus(_A)
class _WwpLeosRapsVirtualRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('clear',1),('localSignalFail',2),(_J,3),('remoteOrOtherPortSignalFail',4),('remoteOrOtherPortForceSwitch',5),('provisioningMismatch',6)))
_WwpLeosRapsVirtualRingStatus_Type.__name__=_C
_WwpLeosRapsVirtualRingStatus_Object=MibTableColumn
wwpLeosRapsVirtualRingStatus=_WwpLeosRapsVirtualRingStatus_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,8),_WwpLeosRapsVirtualRingStatus_Type())
wwpLeosRapsVirtualRingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingStatus.setStatus(_A)
class _WwpLeosRapsVirtualRingAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clear',1),('protectionSwitching',2),('provisionMismatch',3)))
_WwpLeosRapsVirtualRingAlarm_Type.__name__=_C
_WwpLeosRapsVirtualRingAlarm_Object=MibTableColumn
wwpLeosRapsVirtualRingAlarm=_WwpLeosRapsVirtualRingAlarm_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,9),_WwpLeosRapsVirtualRingAlarm_Type())
wwpLeosRapsVirtualRingAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingAlarm.setStatus(_A)
class _WwpLeosRapsVirtualRingNumOfSwitchOvers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosRapsVirtualRingNumOfSwitchOvers_Type.__name__=_C
_WwpLeosRapsVirtualRingNumOfSwitchOvers_Object=MibTableColumn
wwpLeosRapsVirtualRingNumOfSwitchOvers=_WwpLeosRapsVirtualRingNumOfSwitchOvers_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,10),_WwpLeosRapsVirtualRingNumOfSwitchOvers_Type())
wwpLeosRapsVirtualRingNumOfSwitchOvers.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingNumOfSwitchOvers.setStatus(_A)
_WwpLeosRapsVirtualRingUptimeFromLastFailure_Type=Counter32
_WwpLeosRapsVirtualRingUptimeFromLastFailure_Object=MibTableColumn
wwpLeosRapsVirtualRingUptimeFromLastFailure=_WwpLeosRapsVirtualRingUptimeFromLastFailure_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,11),_WwpLeosRapsVirtualRingUptimeFromLastFailure_Type())
wwpLeosRapsVirtualRingUptimeFromLastFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingUptimeFromLastFailure.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingUptimeFromLastFailure.setUnits(_N)
_WwpLeosRapsVirtualRingTotalDownTime_Type=Counter32
_WwpLeosRapsVirtualRingTotalDownTime_Object=MibTableColumn
wwpLeosRapsVirtualRingTotalDownTime=_WwpLeosRapsVirtualRingTotalDownTime_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,12),_WwpLeosRapsVirtualRingTotalDownTime_Type())
wwpLeosRapsVirtualRingTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingTotalDownTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingTotalDownTime.setUnits(_N)
class _WwpLeosRapsVirtualRingWestPortRpl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('owner',2)))
_WwpLeosRapsVirtualRingWestPortRpl_Type.__name__=_C
_WwpLeosRapsVirtualRingWestPortRpl_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortRpl=_WwpLeosRapsVirtualRingWestPortRpl_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,13),_WwpLeosRapsVirtualRingWestPortRpl_Type())
wwpLeosRapsVirtualRingWestPortRpl.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortRpl.setStatus(_A)
class _WwpLeosRapsVirtualRingWestPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_O,2),(_P,3)))
_WwpLeosRapsVirtualRingWestPortState_Type.__name__=_C
_WwpLeosRapsVirtualRingWestPortState_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortState=_WwpLeosRapsVirtualRingWestPortState_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,14),_WwpLeosRapsVirtualRingWestPortState_Type())
wwpLeosRapsVirtualRingWestPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortState.setStatus(_A)
class _WwpLeosRapsVirtualRingWestPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('oK',1),('down',2),(_Q,3),(_J,4),(_R,5),(_S,6)))
_WwpLeosRapsVirtualRingWestPortStatus_Type.__name__=_C
_WwpLeosRapsVirtualRingWestPortStatus_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortStatus=_WwpLeosRapsVirtualRingWestPortStatus_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,15),_WwpLeosRapsVirtualRingWestPortStatus_Type())
wwpLeosRapsVirtualRingWestPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortStatus.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortNrRxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortNrRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRxd=_WwpLeosRapsVirtualRingWestPortNrRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,16),_WwpLeosRapsVirtualRingWestPortNrRxd_Type())
wwpLeosRapsVirtualRingWestPortNrRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortNrRxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortNrTxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortNrTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortNrTxd=_WwpLeosRapsVirtualRingWestPortNrTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,17),_WwpLeosRapsVirtualRingWestPortNrTxd_Type())
wwpLeosRapsVirtualRingWestPortNrTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortNrTxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortSfRxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortSfRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortSfRxd=_WwpLeosRapsVirtualRingWestPortSfRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,18),_WwpLeosRapsVirtualRingWestPortSfRxd_Type())
wwpLeosRapsVirtualRingWestPortSfRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortSfRxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortSfTxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortSfTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortSfTxd=_WwpLeosRapsVirtualRingWestPortSfTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,19),_WwpLeosRapsVirtualRingWestPortSfTxd_Type())
wwpLeosRapsVirtualRingWestPortSfTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortSfTxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortFsRxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortFsRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortFsRxd=_WwpLeosRapsVirtualRingWestPortFsRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,20),_WwpLeosRapsVirtualRingWestPortFsRxd_Type())
wwpLeosRapsVirtualRingWestPortFsRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortFsRxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortFsTxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortFsTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortFsTxd=_WwpLeosRapsVirtualRingWestPortFsTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,21),_WwpLeosRapsVirtualRingWestPortFsTxd_Type())
wwpLeosRapsVirtualRingWestPortFsTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortFsTxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortNrRbRxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortNrRbRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRbRxd=_WwpLeosRapsVirtualRingWestPortNrRbRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,22),_WwpLeosRapsVirtualRingWestPortNrRbRxd_Type())
wwpLeosRapsVirtualRingWestPortNrRbRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortNrRbRxd.setStatus(_A)
_WwpLeosRapsVirtualRingWestPortNrRbTxd_Type=Counter32
_WwpLeosRapsVirtualRingWestPortNrRbTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRbTxd=_WwpLeosRapsVirtualRingWestPortNrRbTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,23),_WwpLeosRapsVirtualRingWestPortNrRbTxd_Type())
wwpLeosRapsVirtualRingWestPortNrRbTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingWestPortNrRbTxd.setStatus(_A)
class _WwpLeosRapsVirtualRingEastPortRpl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('owner',2)))
_WwpLeosRapsVirtualRingEastPortRpl_Type.__name__=_C
_WwpLeosRapsVirtualRingEastPortRpl_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortRpl=_WwpLeosRapsVirtualRingEastPortRpl_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,24),_WwpLeosRapsVirtualRingEastPortRpl_Type())
wwpLeosRapsVirtualRingEastPortRpl.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortRpl.setStatus(_A)
class _WwpLeosRapsVirtualRingEastPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_O,2),(_P,3)))
_WwpLeosRapsVirtualRingEastPortState_Type.__name__=_C
_WwpLeosRapsVirtualRingEastPortState_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortState=_WwpLeosRapsVirtualRingEastPortState_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,25),_WwpLeosRapsVirtualRingEastPortState_Type())
wwpLeosRapsVirtualRingEastPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortState.setStatus(_A)
class _WwpLeosRapsVirtualRingEastPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('down',2),(_Q,3),(_J,4),(_R,5),(_S,6)))
_WwpLeosRapsVirtualRingEastPortStatus_Type.__name__=_C
_WwpLeosRapsVirtualRingEastPortStatus_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortStatus=_WwpLeosRapsVirtualRingEastPortStatus_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,26),_WwpLeosRapsVirtualRingEastPortStatus_Type())
wwpLeosRapsVirtualRingEastPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortStatus.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortNrRxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortNrRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRxd=_WwpLeosRapsVirtualRingEastPortNrRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,27),_WwpLeosRapsVirtualRingEastPortNrRxd_Type())
wwpLeosRapsVirtualRingEastPortNrRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortNrRxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortNrTxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortNrTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortNrTxd=_WwpLeosRapsVirtualRingEastPortNrTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,28),_WwpLeosRapsVirtualRingEastPortNrTxd_Type())
wwpLeosRapsVirtualRingEastPortNrTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortNrTxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortSfRxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortSfRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortSfRxd=_WwpLeosRapsVirtualRingEastPortSfRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,29),_WwpLeosRapsVirtualRingEastPortSfRxd_Type())
wwpLeosRapsVirtualRingEastPortSfRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortSfRxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortSfTxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortSfTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortSfTxd=_WwpLeosRapsVirtualRingEastPortSfTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,30),_WwpLeosRapsVirtualRingEastPortSfTxd_Type())
wwpLeosRapsVirtualRingEastPortSfTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortSfTxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortFsRxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortFsRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortFsRxd=_WwpLeosRapsVirtualRingEastPortFsRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,31),_WwpLeosRapsVirtualRingEastPortFsRxd_Type())
wwpLeosRapsVirtualRingEastPortFsRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortFsRxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortFsTxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortFsTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortFsTxd=_WwpLeosRapsVirtualRingEastPortFsTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,32),_WwpLeosRapsVirtualRingEastPortFsTxd_Type())
wwpLeosRapsVirtualRingEastPortFsTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortFsTxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortNrRbRxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortNrRbRxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRbRxd=_WwpLeosRapsVirtualRingEastPortNrRbRxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,33),_WwpLeosRapsVirtualRingEastPortNrRbRxd_Type())
wwpLeosRapsVirtualRingEastPortNrRbRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortNrRbRxd.setStatus(_A)
_WwpLeosRapsVirtualRingEastPortNrRbTxd_Type=Counter32
_WwpLeosRapsVirtualRingEastPortNrRbTxd_Object=MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRbTxd=_WwpLeosRapsVirtualRingEastPortNrRbTxd_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,34),_WwpLeosRapsVirtualRingEastPortNrRbTxd_Type())
wwpLeosRapsVirtualRingEastPortNrRbTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingEastPortNrRbTxd.setStatus(_A)
class _WwpLeosRapsVirtualRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('majorRing',1),('subRing',2)))
_WwpLeosRapsVirtualRingType_Type.__name__=_C
_WwpLeosRapsVirtualRingType_Object=MibTableColumn
wwpLeosRapsVirtualRingType=_WwpLeosRapsVirtualRingType_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,35),_WwpLeosRapsVirtualRingType_Type())
wwpLeosRapsVirtualRingType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingType.setStatus(_A)
class _WwpLeosRapsVirtualRingSubRingPortTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTerminate',1),('westPortTerminate',2),('eastPortTerminate',3)))
_WwpLeosRapsVirtualRingSubRingPortTerm_Type.__name__=_C
_WwpLeosRapsVirtualRingSubRingPortTerm_Object=MibTableColumn
wwpLeosRapsVirtualRingSubRingPortTerm=_WwpLeosRapsVirtualRingSubRingPortTerm_Object((1,3,6,1,4,1,6141,2,60,47,1,3,1,1,36),_WwpLeosRapsVirtualRingSubRingPortTerm_Type())
wwpLeosRapsVirtualRingSubRingPortTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingSubRingPortTerm.setStatus(_A)
_WwpLeosRapsVirtualRingMember_ObjectIdentity=ObjectIdentity
wwpLeosRapsVirtualRingMember=_WwpLeosRapsVirtualRingMember_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,1,4))
_WwpLeosRapsVirtualRingMemberTable_Object=MibTable
wwpLeosRapsVirtualRingMemberTable=_WwpLeosRapsVirtualRingMemberTable_Object((1,3,6,1,4,1,6141,2,60,47,1,4,1))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberTable.setStatus(_A)
_WwpLeosRapsVirtualRingMemberEntry_Object=MibTableRow
wwpLeosRapsVirtualRingMemberEntry=_WwpLeosRapsVirtualRingMemberEntry_Object((1,3,6,1,4,1,6141,2,60,47,1,4,1,1))
wwpLeosRapsVirtualRingMemberEntry.setIndexNames((0,_D,_F),(0,_D,_T))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberEntry.setStatus(_A)
class _WwpLeosRapsVirtualRingMemberVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_WwpLeosRapsVirtualRingMemberVlanId_Type.__name__=_C
_WwpLeosRapsVirtualRingMemberVlanId_Object=MibTableColumn
wwpLeosRapsVirtualRingMemberVlanId=_WwpLeosRapsVirtualRingMemberVlanId_Object((1,3,6,1,4,1,6141,2,60,47,1,4,1,1,2),_WwpLeosRapsVirtualRingMemberVlanId_Type())
wwpLeosRapsVirtualRingMemberVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberVlanId.setStatus(_A)
_WwpLeosRapsVirtualRingMemberVsTable_Object=MibTable
wwpLeosRapsVirtualRingMemberVsTable=_WwpLeosRapsVirtualRingMemberVsTable_Object((1,3,6,1,4,1,6141,2,60,47,1,4,2))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberVsTable.setStatus(_A)
_WwpLeosRapsVirtualRingMemberVsEntry_Object=MibTableRow
wwpLeosRapsVirtualRingMemberVsEntry=_WwpLeosRapsVirtualRingMemberVsEntry_Object((1,3,6,1,4,1,6141,2,60,47,1,4,2,1))
wwpLeosRapsVirtualRingMemberVsEntry.setIndexNames((0,_D,_F),(0,_D,_U))
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberVsEntry.setStatus(_A)
class _WwpLeosRapsVirtualRingMemberVsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_WwpLeosRapsVirtualRingMemberVsId_Type.__name__=_C
_WwpLeosRapsVirtualRingMemberVsId_Object=MibTableColumn
wwpLeosRapsVirtualRingMemberVsId=_WwpLeosRapsVirtualRingMemberVsId_Object((1,3,6,1,4,1,6141,2,60,47,1,4,2,1,1),_WwpLeosRapsVirtualRingMemberVsId_Type())
wwpLeosRapsVirtualRingMemberVsId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosRapsVirtualRingMemberVsId.setStatus(_A)
_WwpLeosRapsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBNotificationPrefix=_WwpLeosRapsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,2))
_WwpLeosRapsMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBNotifications=_WwpLeosRapsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,2,0))
_WwpLeosRapsMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBConformance=_WwpLeosRapsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,3))
_WwpLeosRapsMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBCompliances=_WwpLeosRapsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,3,1))
_WwpLeosRapsMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosRapsMIBGroups=_WwpLeosRapsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,47,3,2))
wwpLeosRapsAlarm=NotificationType((1,3,6,1,4,1,6141,2,60,47,2,0,1))
wwpLeosRapsAlarm.setObjects(*((_D,_V),(_D,_W)))
if mibBuilder.loadTexts:wwpLeosRapsAlarm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpLeosRapsMIB':wwpLeosRapsMIB,'wwpLeosRapsMIBObjects':wwpLeosRapsMIBObjects,'wwpLeosRapsGlobal':wwpLeosRapsGlobal,'wwpLeosRapsGlobalAttrs':wwpLeosRapsGlobalAttrs,'wwpLeosRapsState':wwpLeosRapsState,'wwpLeosRapsNodeId':wwpLeosRapsNodeId,'wwpLeosRapsEtherType':wwpLeosRapsEtherType,'wwpLeosRapsNumberOfRings':wwpLeosRapsNumberOfRings,'wwpLeosRapsLogicalRing':wwpLeosRapsLogicalRing,'wwpLeosRapsLogicalRingTable':wwpLeosRapsLogicalRingTable,'wwpLeosRapsLogicalRingEntry':wwpLeosRapsLogicalRingEntry,_K:wwpLeosRapsLogicalRingIndex,'wwpLeosRapsLogicalRingName':wwpLeosRapsLogicalRingName,'wwpLeosRapsLogicalRingId':wwpLeosRapsLogicalRingId,'wwpLeosRapsLogicalRingGuardTime':wwpLeosRapsLogicalRingGuardTime,'wwpLeosRapsLogicalRingWtr':wwpLeosRapsLogicalRingWtr,'wwpLeosRapsLogicalRingWtb':wwpLeosRapsLogicalRingWtb,'wwpLeosRapsLogicalRingWestPortId':wwpLeosRapsLogicalRingWestPortId,'wwpLeosRapsLogicalRingWestHoldOffTime':wwpLeosRapsLogicalRingWestHoldOffTime,'wwpLeosRapsLogicalRingWestForce':wwpLeosRapsLogicalRingWestForce,'wwpLeosRapsLogicalRingWestCfmService':wwpLeosRapsLogicalRingWestCfmService,'wwpLeosRapsLogicalRingEastPortId':wwpLeosRapsLogicalRingEastPortId,'wwpLeosRapsLogicalRingEastHoldOffTime':wwpLeosRapsLogicalRingEastHoldOffTime,'wwpLeosRapsLogicalRingEastForce':wwpLeosRapsLogicalRingEastForce,'wwpLeosRapsLogicalRingEastCfmService':wwpLeosRapsLogicalRingEastCfmService,'wwpLeosRapsLogicalRingNumberOfVirtualRings':wwpLeosRapsLogicalRingNumberOfVirtualRings,'wwpLeosRapsVirtualRing':wwpLeosRapsVirtualRing,'wwpLeosRapsVirtualRingTable':wwpLeosRapsVirtualRingTable,'wwpLeosRapsVirtualRingEntry':wwpLeosRapsVirtualRingEntry,_F:wwpLeosRapsVirtualRingIndex,_V:wwpLeosRapsVirtualRingName,'wwpLeosRapsVirtualRingVid':wwpLeosRapsVirtualRingVid,'wwpLeosRapsVirtualRingLogicalRingId':wwpLeosRapsVirtualRingLogicalRingId,'wwpLeosRapsVirtualRingMel':wwpLeosRapsVirtualRingMel,'wwpLeosRapsVirtualRingRevertive':wwpLeosRapsVirtualRingRevertive,'wwpLeosRapsVirtualRingState':wwpLeosRapsVirtualRingState,'wwpLeosRapsVirtualRingStatus':wwpLeosRapsVirtualRingStatus,_W:wwpLeosRapsVirtualRingAlarm,'wwpLeosRapsVirtualRingNumOfSwitchOvers':wwpLeosRapsVirtualRingNumOfSwitchOvers,'wwpLeosRapsVirtualRingUptimeFromLastFailure':wwpLeosRapsVirtualRingUptimeFromLastFailure,'wwpLeosRapsVirtualRingTotalDownTime':wwpLeosRapsVirtualRingTotalDownTime,'wwpLeosRapsVirtualRingWestPortRpl':wwpLeosRapsVirtualRingWestPortRpl,'wwpLeosRapsVirtualRingWestPortState':wwpLeosRapsVirtualRingWestPortState,'wwpLeosRapsVirtualRingWestPortStatus':wwpLeosRapsVirtualRingWestPortStatus,'wwpLeosRapsVirtualRingWestPortNrRxd':wwpLeosRapsVirtualRingWestPortNrRxd,'wwpLeosRapsVirtualRingWestPortNrTxd':wwpLeosRapsVirtualRingWestPortNrTxd,'wwpLeosRapsVirtualRingWestPortSfRxd':wwpLeosRapsVirtualRingWestPortSfRxd,'wwpLeosRapsVirtualRingWestPortSfTxd':wwpLeosRapsVirtualRingWestPortSfTxd,'wwpLeosRapsVirtualRingWestPortFsRxd':wwpLeosRapsVirtualRingWestPortFsRxd,'wwpLeosRapsVirtualRingWestPortFsTxd':wwpLeosRapsVirtualRingWestPortFsTxd,'wwpLeosRapsVirtualRingWestPortNrRbRxd':wwpLeosRapsVirtualRingWestPortNrRbRxd,'wwpLeosRapsVirtualRingWestPortNrRbTxd':wwpLeosRapsVirtualRingWestPortNrRbTxd,'wwpLeosRapsVirtualRingEastPortRpl':wwpLeosRapsVirtualRingEastPortRpl,'wwpLeosRapsVirtualRingEastPortState':wwpLeosRapsVirtualRingEastPortState,'wwpLeosRapsVirtualRingEastPortStatus':wwpLeosRapsVirtualRingEastPortStatus,'wwpLeosRapsVirtualRingEastPortNrRxd':wwpLeosRapsVirtualRingEastPortNrRxd,'wwpLeosRapsVirtualRingEastPortNrTxd':wwpLeosRapsVirtualRingEastPortNrTxd,'wwpLeosRapsVirtualRingEastPortSfRxd':wwpLeosRapsVirtualRingEastPortSfRxd,'wwpLeosRapsVirtualRingEastPortSfTxd':wwpLeosRapsVirtualRingEastPortSfTxd,'wwpLeosRapsVirtualRingEastPortFsRxd':wwpLeosRapsVirtualRingEastPortFsRxd,'wwpLeosRapsVirtualRingEastPortFsTxd':wwpLeosRapsVirtualRingEastPortFsTxd,'wwpLeosRapsVirtualRingEastPortNrRbRxd':wwpLeosRapsVirtualRingEastPortNrRbRxd,'wwpLeosRapsVirtualRingEastPortNrRbTxd':wwpLeosRapsVirtualRingEastPortNrRbTxd,'wwpLeosRapsVirtualRingType':wwpLeosRapsVirtualRingType,'wwpLeosRapsVirtualRingSubRingPortTerm':wwpLeosRapsVirtualRingSubRingPortTerm,'wwpLeosRapsVirtualRingMember':wwpLeosRapsVirtualRingMember,'wwpLeosRapsVirtualRingMemberTable':wwpLeosRapsVirtualRingMemberTable,'wwpLeosRapsVirtualRingMemberEntry':wwpLeosRapsVirtualRingMemberEntry,_T:wwpLeosRapsVirtualRingMemberVlanId,'wwpLeosRapsVirtualRingMemberVsTable':wwpLeosRapsVirtualRingMemberVsTable,'wwpLeosRapsVirtualRingMemberVsEntry':wwpLeosRapsVirtualRingMemberVsEntry,_U:wwpLeosRapsVirtualRingMemberVsId,'wwpLeosRapsMIBNotificationPrefix':wwpLeosRapsMIBNotificationPrefix,'wwpLeosRapsMIBNotifications':wwpLeosRapsMIBNotifications,'wwpLeosRapsAlarm':wwpLeosRapsAlarm,'wwpLeosRapsMIBConformance':wwpLeosRapsMIBConformance,'wwpLeosRapsMIBCompliances':wwpLeosRapsMIBCompliances,'wwpLeosRapsMIBGroups':wwpLeosRapsMIBGroups})