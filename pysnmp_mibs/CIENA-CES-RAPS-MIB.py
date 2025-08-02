_g='cienaCesRapsVirtualRingAlarmExtended'
_f='cienaCesRapsVirtualRingMemberVsId'
_e='remoteSignalFailure'
_d='remoteForceSwitch'
_c='ccmFailure'
_b='blocked'
_a='forwarding'
_Z='disabled'
_Y='seconds'
_X='noRplOwnerDetected'
_W='noRapsPduReceived'
_V='minutes'
_U='not-accessible'
_T='cienaCesRapsLogicalRingIndex'
_S='CienaGlobalState'
_R='localForceSwitch'
_Q='none'
_P='cienaCesRapsVirtualRingIndex'
_O='milliseconds'
_N='OctetString'
_M='cienaCesRapsVirtualRingAlarm'
_L='cienaCesRapsVirtualRingName'
_K='cienaCesRapsVirtualRingNotifIndex'
_J='on'
_I='off'
_H='DisplayString'
_G='cienaGlobalSeverity'
_F='cienaGlobalMacAddress'
_E='CIENA-GLOBAL-MIB'
_D='CIENA-CES-RAPS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_E,_F,_G)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC',_S)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','TextualConvention')
cienaCesRapsMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,20))
if mibBuilder.loadTexts:cienaCesRapsMIB.setRevisions(('2017-06-07 00:00','2017-01-23 00:00','2014-07-04 00:00','2011-04-16 17:00'))
_CienaCesRapsMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBObjects=_CienaCesRapsMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1))
_CienaCesRapsGlobal_ObjectIdentity=ObjectIdentity
cienaCesRapsGlobal=_CienaCesRapsGlobal_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1,1))
_CienaCesRapsGlobalAttrs_ObjectIdentity=ObjectIdentity
cienaCesRapsGlobalAttrs=_CienaCesRapsGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1,1,1))
class _CienaCesRapsState_Type(CienaGlobalState):defaultValue=1
_CienaCesRapsState_Type.__name__=_S
_CienaCesRapsState_Object=MibScalar
cienaCesRapsState=_CienaCesRapsState_Object((1,3,6,1,4,1,1271,2,1,20,1,1,1,1),_CienaCesRapsState_Type())
cienaCesRapsState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsState.setStatus(_A)
_CienaCesRapsNodeId_Type=MacAddress
_CienaCesRapsNodeId_Object=MibScalar
cienaCesRapsNodeId=_CienaCesRapsNodeId_Object((1,3,6,1,4,1,1271,2,1,20,1,1,1,2),_CienaCesRapsNodeId_Type())
cienaCesRapsNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsNodeId.setStatus(_A)
class _CienaCesRapsEtherType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,2))
_CienaCesRapsEtherType_Type.__name__=_N
_CienaCesRapsEtherType_Object=MibScalar
cienaCesRapsEtherType=_CienaCesRapsEtherType_Object((1,3,6,1,4,1,1271,2,1,20,1,1,1,3),_CienaCesRapsEtherType_Type())
cienaCesRapsEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsEtherType.setStatus(_A)
_CienaCesRapsNumberOfRings_Type=Integer32
_CienaCesRapsNumberOfRings_Object=MibScalar
cienaCesRapsNumberOfRings=_CienaCesRapsNumberOfRings_Object((1,3,6,1,4,1,1271,2,1,20,1,1,1,4),_CienaCesRapsNumberOfRings_Type())
cienaCesRapsNumberOfRings.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsNumberOfRings.setStatus(_A)
_CienaCesRapsLogicalRing_ObjectIdentity=ObjectIdentity
cienaCesRapsLogicalRing=_CienaCesRapsLogicalRing_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1,2))
_CienaCesRapsLogicalRingTable_Object=MibTable
cienaCesRapsLogicalRingTable=_CienaCesRapsLogicalRingTable_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1))
if mibBuilder.loadTexts:cienaCesRapsLogicalRingTable.setStatus(_A)
_CienaCesRapsLogicalRingEntry_Object=MibTableRow
cienaCesRapsLogicalRingEntry=_CienaCesRapsLogicalRingEntry_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1))
cienaCesRapsLogicalRingEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEntry.setStatus(_A)
class _CienaCesRapsLogicalRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CienaCesRapsLogicalRingIndex_Type.__name__=_C
_CienaCesRapsLogicalRingIndex_Object=MibTableColumn
cienaCesRapsLogicalRingIndex=_CienaCesRapsLogicalRingIndex_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,1),_CienaCesRapsLogicalRingIndex_Type())
cienaCesRapsLogicalRingIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingIndex.setStatus(_A)
class _CienaCesRapsLogicalRingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesRapsLogicalRingName_Type.__name__=_H
_CienaCesRapsLogicalRingName_Object=MibTableColumn
cienaCesRapsLogicalRingName=_CienaCesRapsLogicalRingName_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,2),_CienaCesRapsLogicalRingName_Type())
cienaCesRapsLogicalRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingName.setStatus(_A)
class _CienaCesRapsLogicalRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CienaCesRapsLogicalRingId_Type.__name__=_C
_CienaCesRapsLogicalRingId_Object=MibTableColumn
cienaCesRapsLogicalRingId=_CienaCesRapsLogicalRingId_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,3),_CienaCesRapsLogicalRingId_Type())
cienaCesRapsLogicalRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingId.setStatus(_A)
class _CienaCesRapsLogicalRingGuardTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,2000))
_CienaCesRapsLogicalRingGuardTime_Type.__name__=_C
_CienaCesRapsLogicalRingGuardTime_Object=MibTableColumn
cienaCesRapsLogicalRingGuardTime=_CienaCesRapsLogicalRingGuardTime_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,4),_CienaCesRapsLogicalRingGuardTime_Type())
cienaCesRapsLogicalRingGuardTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingGuardTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingGuardTime.setUnits(_O)
class _CienaCesRapsLogicalRingWtr_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_CienaCesRapsLogicalRingWtr_Type.__name__=_C
_CienaCesRapsLogicalRingWtr_Object=MibTableColumn
cienaCesRapsLogicalRingWtr=_CienaCesRapsLogicalRingWtr_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,5),_CienaCesRapsLogicalRingWtr_Type())
cienaCesRapsLogicalRingWtr.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWtr.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWtr.setUnits(_V)
_CienaCesRapsLogicalRingWtb_Type=Integer32
_CienaCesRapsLogicalRingWtb_Object=MibTableColumn
cienaCesRapsLogicalRingWtb=_CienaCesRapsLogicalRingWtb_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,6),_CienaCesRapsLogicalRingWtb_Type())
cienaCesRapsLogicalRingWtb.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWtb.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWtb.setUnits(_V)
_CienaCesRapsLogicalRingWestPortId_Type=Integer32
_CienaCesRapsLogicalRingWestPortId_Object=MibTableColumn
cienaCesRapsLogicalRingWestPortId=_CienaCesRapsLogicalRingWestPortId_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,7),_CienaCesRapsLogicalRingWestPortId_Type())
cienaCesRapsLogicalRingWestPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWestPortId.setStatus(_A)
class _CienaCesRapsLogicalRingWestHoldOffTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CienaCesRapsLogicalRingWestHoldOffTime_Type.__name__=_C
_CienaCesRapsLogicalRingWestHoldOffTime_Object=MibTableColumn
cienaCesRapsLogicalRingWestHoldOffTime=_CienaCesRapsLogicalRingWestHoldOffTime_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,8),_CienaCesRapsLogicalRingWestHoldOffTime_Type())
cienaCesRapsLogicalRingWestHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWestHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWestHoldOffTime.setUnits(_O)
class _CienaCesRapsLogicalRingWestForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsLogicalRingWestForce_Type.__name__=_C
_CienaCesRapsLogicalRingWestForce_Object=MibTableColumn
cienaCesRapsLogicalRingWestForce=_CienaCesRapsLogicalRingWestForce_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,9),_CienaCesRapsLogicalRingWestForce_Type())
cienaCesRapsLogicalRingWestForce.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWestForce.setStatus(_A)
class _CienaCesRapsLogicalRingWestCfmService_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesRapsLogicalRingWestCfmService_Type.__name__=_H
_CienaCesRapsLogicalRingWestCfmService_Object=MibTableColumn
cienaCesRapsLogicalRingWestCfmService=_CienaCesRapsLogicalRingWestCfmService_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,10),_CienaCesRapsLogicalRingWestCfmService_Type())
cienaCesRapsLogicalRingWestCfmService.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingWestCfmService.setStatus(_A)
_CienaCesRapsLogicalRingEastPortId_Type=Integer32
_CienaCesRapsLogicalRingEastPortId_Object=MibTableColumn
cienaCesRapsLogicalRingEastPortId=_CienaCesRapsLogicalRingEastPortId_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,11),_CienaCesRapsLogicalRingEastPortId_Type())
cienaCesRapsLogicalRingEastPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEastPortId.setStatus(_A)
class _CienaCesRapsLogicalRingEastHoldOffTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CienaCesRapsLogicalRingEastHoldOffTime_Type.__name__=_C
_CienaCesRapsLogicalRingEastHoldOffTime_Object=MibTableColumn
cienaCesRapsLogicalRingEastHoldOffTime=_CienaCesRapsLogicalRingEastHoldOffTime_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,12),_CienaCesRapsLogicalRingEastHoldOffTime_Type())
cienaCesRapsLogicalRingEastHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEastHoldOffTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEastHoldOffTime.setUnits(_O)
class _CienaCesRapsLogicalRingEastForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsLogicalRingEastForce_Type.__name__=_C
_CienaCesRapsLogicalRingEastForce_Object=MibTableColumn
cienaCesRapsLogicalRingEastForce=_CienaCesRapsLogicalRingEastForce_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,13),_CienaCesRapsLogicalRingEastForce_Type())
cienaCesRapsLogicalRingEastForce.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEastForce.setStatus(_A)
class _CienaCesRapsLogicalRingEastCfmService_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesRapsLogicalRingEastCfmService_Type.__name__=_H
_CienaCesRapsLogicalRingEastCfmService_Object=MibTableColumn
cienaCesRapsLogicalRingEastCfmService=_CienaCesRapsLogicalRingEastCfmService_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,14),_CienaCesRapsLogicalRingEastCfmService_Type())
cienaCesRapsLogicalRingEastCfmService.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingEastCfmService.setStatus(_A)
class _CienaCesRapsLogicalRingNumberOfVirtualRings_Type(Integer32):defaultValue=0
_CienaCesRapsLogicalRingNumberOfVirtualRings_Type.__name__=_C
_CienaCesRapsLogicalRingNumberOfVirtualRings_Object=MibTableColumn
cienaCesRapsLogicalRingNumberOfVirtualRings=_CienaCesRapsLogicalRingNumberOfVirtualRings_Object((1,3,6,1,4,1,1271,2,1,20,1,2,1,1,15),_CienaCesRapsLogicalRingNumberOfVirtualRings_Type())
cienaCesRapsLogicalRingNumberOfVirtualRings.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsLogicalRingNumberOfVirtualRings.setStatus(_A)
_CienaCesRapsVirtualRing_ObjectIdentity=ObjectIdentity
cienaCesRapsVirtualRing=_CienaCesRapsVirtualRing_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1,3))
_CienaCesRapsVirtualRingTable_Object=MibTable
cienaCesRapsVirtualRingTable=_CienaCesRapsVirtualRingTable_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1))
if mibBuilder.loadTexts:cienaCesRapsVirtualRingTable.setStatus(_A)
_CienaCesRapsVirtualRingEntry_Object=MibTableRow
cienaCesRapsVirtualRingEntry=_CienaCesRapsVirtualRingEntry_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1))
cienaCesRapsVirtualRingEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEntry.setStatus(_A)
class _CienaCesRapsVirtualRingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_CienaCesRapsVirtualRingIndex_Type.__name__=_C
_CienaCesRapsVirtualRingIndex_Object=MibTableColumn
cienaCesRapsVirtualRingIndex=_CienaCesRapsVirtualRingIndex_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,1),_CienaCesRapsVirtualRingIndex_Type())
cienaCesRapsVirtualRingIndex.setMaxAccess(_U)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingIndex.setStatus(_A)
class _CienaCesRapsVirtualRingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesRapsVirtualRingName_Type.__name__=_H
_CienaCesRapsVirtualRingName_Object=MibTableColumn
cienaCesRapsVirtualRingName=_CienaCesRapsVirtualRingName_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,2),_CienaCesRapsVirtualRingName_Type())
cienaCesRapsVirtualRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingName.setStatus(_A)
class _CienaCesRapsVirtualRingVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_CienaCesRapsVirtualRingVid_Type.__name__=_C
_CienaCesRapsVirtualRingVid_Object=MibTableColumn
cienaCesRapsVirtualRingVid=_CienaCesRapsVirtualRingVid_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,3),_CienaCesRapsVirtualRingVid_Type())
cienaCesRapsVirtualRingVid.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingVid.setStatus(_A)
class _CienaCesRapsVirtualRingLogicalRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CienaCesRapsVirtualRingLogicalRingId_Type.__name__=_C
_CienaCesRapsVirtualRingLogicalRingId_Object=MibTableColumn
cienaCesRapsVirtualRingLogicalRingId=_CienaCesRapsVirtualRingLogicalRingId_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,4),_CienaCesRapsVirtualRingLogicalRingId_Type())
cienaCesRapsVirtualRingLogicalRingId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingLogicalRingId.setStatus(_A)
class _CienaCesRapsVirtualRingMel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CienaCesRapsVirtualRingMel_Type.__name__=_C
_CienaCesRapsVirtualRingMel_Object=MibTableColumn
cienaCesRapsVirtualRingMel=_CienaCesRapsVirtualRingMel_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,5),_CienaCesRapsVirtualRingMel_Type())
cienaCesRapsVirtualRingMel.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingMel.setStatus(_A)
class _CienaCesRapsVirtualRingRevertive_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsVirtualRingRevertive_Type.__name__=_C
_CienaCesRapsVirtualRingRevertive_Object=MibTableColumn
cienaCesRapsVirtualRingRevertive=_CienaCesRapsVirtualRingRevertive_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,6),_CienaCesRapsVirtualRingRevertive_Type())
cienaCesRapsVirtualRingRevertive.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingRevertive.setStatus(_A)
class _CienaCesRapsVirtualRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('adminDisabled',1),('ok',2),('protecting',3),('recovering',4),('init',5),(_Q,6)))
_CienaCesRapsVirtualRingState_Type.__name__=_C
_CienaCesRapsVirtualRingState_Object=MibTableColumn
cienaCesRapsVirtualRingState=_CienaCesRapsVirtualRingState_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,7),_CienaCesRapsVirtualRingState_Type())
cienaCesRapsVirtualRingState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingState.setStatus(_A)
class _CienaCesRapsVirtualRingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('clear',1),('localSignalFail',2),(_R,3),('remoteOrOtherPortSignalFail',4),('remoteOrOtherPortForceSwitch',5),('provisioningMismatch',6),(_W,7),(_X,8)))
_CienaCesRapsVirtualRingStatus_Type.__name__=_C
_CienaCesRapsVirtualRingStatus_Object=MibTableColumn
cienaCesRapsVirtualRingStatus=_CienaCesRapsVirtualRingStatus_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,8),_CienaCesRapsVirtualRingStatus_Type())
cienaCesRapsVirtualRingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingStatus.setStatus(_A)
class _CienaCesRapsVirtualRingAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('clear',1),('protectionSwitching',2),('provisionMismatch',3),(_W,4),(_X,5)))
_CienaCesRapsVirtualRingAlarm_Type.__name__=_C
_CienaCesRapsVirtualRingAlarm_Object=MibTableColumn
cienaCesRapsVirtualRingAlarm=_CienaCesRapsVirtualRingAlarm_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,9),_CienaCesRapsVirtualRingAlarm_Type())
cienaCesRapsVirtualRingAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingAlarm.setStatus(_A)
_CienaCesRapsVirtualRingNumOfSwitchOvers_Type=Integer32
_CienaCesRapsVirtualRingNumOfSwitchOvers_Object=MibTableColumn
cienaCesRapsVirtualRingNumOfSwitchOvers=_CienaCesRapsVirtualRingNumOfSwitchOvers_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,10),_CienaCesRapsVirtualRingNumOfSwitchOvers_Type())
cienaCesRapsVirtualRingNumOfSwitchOvers.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingNumOfSwitchOvers.setStatus(_A)
_CienaCesRapsVirtualRingUptimeFromLastFailure_Type=Integer32
_CienaCesRapsVirtualRingUptimeFromLastFailure_Object=MibTableColumn
cienaCesRapsVirtualRingUptimeFromLastFailure=_CienaCesRapsVirtualRingUptimeFromLastFailure_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,11),_CienaCesRapsVirtualRingUptimeFromLastFailure_Type())
cienaCesRapsVirtualRingUptimeFromLastFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingUptimeFromLastFailure.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingUptimeFromLastFailure.setUnits(_Y)
_CienaCesRapsVirtualRingTotalDownTime_Type=Integer32
_CienaCesRapsVirtualRingTotalDownTime_Object=MibTableColumn
cienaCesRapsVirtualRingTotalDownTime=_CienaCesRapsVirtualRingTotalDownTime_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,12),_CienaCesRapsVirtualRingTotalDownTime_Type())
cienaCesRapsVirtualRingTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingTotalDownTime.setStatus(_A)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingTotalDownTime.setUnits(_Y)
class _CienaCesRapsVirtualRingWestPortRpl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('owner',2)))
_CienaCesRapsVirtualRingWestPortRpl_Type.__name__=_C
_CienaCesRapsVirtualRingWestPortRpl_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortRpl=_CienaCesRapsVirtualRingWestPortRpl_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,13),_CienaCesRapsVirtualRingWestPortRpl_Type())
cienaCesRapsVirtualRingWestPortRpl.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortRpl.setStatus(_A)
class _CienaCesRapsVirtualRingWestPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_CienaCesRapsVirtualRingWestPortState_Type.__name__=_C
_CienaCesRapsVirtualRingWestPortState_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortState=_CienaCesRapsVirtualRingWestPortState_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,14),_CienaCesRapsVirtualRingWestPortState_Type())
cienaCesRapsVirtualRingWestPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortState.setStatus(_A)
class _CienaCesRapsVirtualRingWestPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('oK',1),('down',2),(_c,3),(_R,4),(_d,5),(_e,6)))
_CienaCesRapsVirtualRingWestPortStatus_Type.__name__=_C
_CienaCesRapsVirtualRingWestPortStatus_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortStatus=_CienaCesRapsVirtualRingWestPortStatus_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,15),_CienaCesRapsVirtualRingWestPortStatus_Type())
cienaCesRapsVirtualRingWestPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortStatus.setStatus(_A)
_CienaCesRapsVirtualRingWestPortNrRxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortNrRxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortNrRxd=_CienaCesRapsVirtualRingWestPortNrRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,16),_CienaCesRapsVirtualRingWestPortNrRxd_Type())
cienaCesRapsVirtualRingWestPortNrRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortNrRxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortNrTxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortNrTxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortNrTxd=_CienaCesRapsVirtualRingWestPortNrTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,17),_CienaCesRapsVirtualRingWestPortNrTxd_Type())
cienaCesRapsVirtualRingWestPortNrTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortNrTxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortSfRxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortSfRxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortSfRxd=_CienaCesRapsVirtualRingWestPortSfRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,18),_CienaCesRapsVirtualRingWestPortSfRxd_Type())
cienaCesRapsVirtualRingWestPortSfRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortSfRxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortSfTxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortSfTxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortSfTxd=_CienaCesRapsVirtualRingWestPortSfTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,19),_CienaCesRapsVirtualRingWestPortSfTxd_Type())
cienaCesRapsVirtualRingWestPortSfTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortSfTxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortFsRxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortFsRxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortFsRxd=_CienaCesRapsVirtualRingWestPortFsRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,20),_CienaCesRapsVirtualRingWestPortFsRxd_Type())
cienaCesRapsVirtualRingWestPortFsRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortFsRxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortFsTxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortFsTxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortFsTxd=_CienaCesRapsVirtualRingWestPortFsTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,21),_CienaCesRapsVirtualRingWestPortFsTxd_Type())
cienaCesRapsVirtualRingWestPortFsTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortFsTxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortNrRbRxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortNrRbRxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortNrRbRxd=_CienaCesRapsVirtualRingWestPortNrRbRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,22),_CienaCesRapsVirtualRingWestPortNrRbRxd_Type())
cienaCesRapsVirtualRingWestPortNrRbRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortNrRbRxd.setStatus(_A)
_CienaCesRapsVirtualRingWestPortNrRbTxd_Type=Integer32
_CienaCesRapsVirtualRingWestPortNrRbTxd_Object=MibTableColumn
cienaCesRapsVirtualRingWestPortNrRbTxd=_CienaCesRapsVirtualRingWestPortNrRbTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,23),_CienaCesRapsVirtualRingWestPortNrRbTxd_Type())
cienaCesRapsVirtualRingWestPortNrRbTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestPortNrRbTxd.setStatus(_A)
class _CienaCesRapsVirtualRingEastPortRpl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('owner',2)))
_CienaCesRapsVirtualRingEastPortRpl_Type.__name__=_C
_CienaCesRapsVirtualRingEastPortRpl_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortRpl=_CienaCesRapsVirtualRingEastPortRpl_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,24),_CienaCesRapsVirtualRingEastPortRpl_Type())
cienaCesRapsVirtualRingEastPortRpl.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortRpl.setStatus(_A)
class _CienaCesRapsVirtualRingEastPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_CienaCesRapsVirtualRingEastPortState_Type.__name__=_C
_CienaCesRapsVirtualRingEastPortState_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortState=_CienaCesRapsVirtualRingEastPortState_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,25),_CienaCesRapsVirtualRingEastPortState_Type())
cienaCesRapsVirtualRingEastPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortState.setStatus(_A)
class _CienaCesRapsVirtualRingEastPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),('down',2),(_c,3),(_R,4),(_d,5),(_e,6)))
_CienaCesRapsVirtualRingEastPortStatus_Type.__name__=_C
_CienaCesRapsVirtualRingEastPortStatus_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortStatus=_CienaCesRapsVirtualRingEastPortStatus_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,26),_CienaCesRapsVirtualRingEastPortStatus_Type())
cienaCesRapsVirtualRingEastPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortStatus.setStatus(_A)
_CienaCesRapsVirtualRingEastPortNrRxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortNrRxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortNrRxd=_CienaCesRapsVirtualRingEastPortNrRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,27),_CienaCesRapsVirtualRingEastPortNrRxd_Type())
cienaCesRapsVirtualRingEastPortNrRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortNrRxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortNrTxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortNrTxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortNrTxd=_CienaCesRapsVirtualRingEastPortNrTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,28),_CienaCesRapsVirtualRingEastPortNrTxd_Type())
cienaCesRapsVirtualRingEastPortNrTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortNrTxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortSfRxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortSfRxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortSfRxd=_CienaCesRapsVirtualRingEastPortSfRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,29),_CienaCesRapsVirtualRingEastPortSfRxd_Type())
cienaCesRapsVirtualRingEastPortSfRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortSfRxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortSfTxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortSfTxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortSfTxd=_CienaCesRapsVirtualRingEastPortSfTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,30),_CienaCesRapsVirtualRingEastPortSfTxd_Type())
cienaCesRapsVirtualRingEastPortSfTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortSfTxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortFsRxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortFsRxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortFsRxd=_CienaCesRapsVirtualRingEastPortFsRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,31),_CienaCesRapsVirtualRingEastPortFsRxd_Type())
cienaCesRapsVirtualRingEastPortFsRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortFsRxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortFsTxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortFsTxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortFsTxd=_CienaCesRapsVirtualRingEastPortFsTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,32),_CienaCesRapsVirtualRingEastPortFsTxd_Type())
cienaCesRapsVirtualRingEastPortFsTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortFsTxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortNrRbRxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortNrRbRxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortNrRbRxd=_CienaCesRapsVirtualRingEastPortNrRbRxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,33),_CienaCesRapsVirtualRingEastPortNrRbRxd_Type())
cienaCesRapsVirtualRingEastPortNrRbRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortNrRbRxd.setStatus(_A)
_CienaCesRapsVirtualRingEastPortNrRbTxd_Type=Integer32
_CienaCesRapsVirtualRingEastPortNrRbTxd_Object=MibTableColumn
cienaCesRapsVirtualRingEastPortNrRbTxd=_CienaCesRapsVirtualRingEastPortNrRbTxd_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,34),_CienaCesRapsVirtualRingEastPortNrRbTxd_Type())
cienaCesRapsVirtualRingEastPortNrRbTxd.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastPortNrRbTxd.setStatus(_A)
class _CienaCesRapsVirtualRingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('majorRing',1),('subRing',2)))
_CienaCesRapsVirtualRingType_Type.__name__=_C
_CienaCesRapsVirtualRingType_Object=MibTableColumn
cienaCesRapsVirtualRingType=_CienaCesRapsVirtualRingType_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,35),_CienaCesRapsVirtualRingType_Type())
cienaCesRapsVirtualRingType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingType.setStatus(_A)
class _CienaCesRapsVirtualRingSubRingPortTerm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noTerminate',1),('westPortTerminate',2),('eastPortTerminate',3)))
_CienaCesRapsVirtualRingSubRingPortTerm_Type.__name__=_C
_CienaCesRapsVirtualRingSubRingPortTerm_Object=MibTableColumn
cienaCesRapsVirtualRingSubRingPortTerm=_CienaCesRapsVirtualRingSubRingPortTerm_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,36),_CienaCesRapsVirtualRingSubRingPortTerm_Type())
cienaCesRapsVirtualRingSubRingPortTerm.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingSubRingPortTerm.setStatus(_A)
class _CienaCesRapsVirtualRingNotifIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_CienaCesRapsVirtualRingNotifIndex_Type.__name__=_C
_CienaCesRapsVirtualRingNotifIndex_Object=MibTableColumn
cienaCesRapsVirtualRingNotifIndex=_CienaCesRapsVirtualRingNotifIndex_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,37),_CienaCesRapsVirtualRingNotifIndex_Type())
cienaCesRapsVirtualRingNotifIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cienaCesRapsVirtualRingNotifIndex.setStatus(_A)
class _CienaCesRapsVirtualRingAlarmExtended_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CienaCesRapsVirtualRingAlarmExtended_Type.__name__=_N
_CienaCesRapsVirtualRingAlarmExtended_Object=MibTableColumn
cienaCesRapsVirtualRingAlarmExtended=_CienaCesRapsVirtualRingAlarmExtended_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,38),_CienaCesRapsVirtualRingAlarmExtended_Type())
cienaCesRapsVirtualRingAlarmExtended.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingAlarmExtended.setStatus(_A)
class _CienaCesRapsVirtualRingWestForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsVirtualRingWestForce_Type.__name__=_C
_CienaCesRapsVirtualRingWestForce_Object=MibTableColumn
cienaCesRapsVirtualRingWestForce=_CienaCesRapsVirtualRingWestForce_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,39),_CienaCesRapsVirtualRingWestForce_Type())
cienaCesRapsVirtualRingWestForce.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingWestForce.setStatus(_A)
class _CienaCesRapsVirtualRingEastForce_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsVirtualRingEastForce_Type.__name__=_C
_CienaCesRapsVirtualRingEastForce_Object=MibTableColumn
cienaCesRapsVirtualRingEastForce=_CienaCesRapsVirtualRingEastForce_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,40),_CienaCesRapsVirtualRingEastForce_Type())
cienaCesRapsVirtualRingEastForce.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingEastForce.setStatus(_A)
class _CienaCesRapsVirtualRingFlushPropagate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CienaCesRapsVirtualRingFlushPropagate_Type.__name__=_C
_CienaCesRapsVirtualRingFlushPropagate_Object=MibTableColumn
cienaCesRapsVirtualRingFlushPropagate=_CienaCesRapsVirtualRingFlushPropagate_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,41),_CienaCesRapsVirtualRingFlushPropagate_Type())
cienaCesRapsVirtualRingFlushPropagate.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingFlushPropagate.setStatus(_A)
class _CienaCesRapsVirtualRingLogicalRingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesRapsVirtualRingLogicalRingName_Type.__name__=_H
_CienaCesRapsVirtualRingLogicalRingName_Object=MibTableColumn
cienaCesRapsVirtualRingLogicalRingName=_CienaCesRapsVirtualRingLogicalRingName_Object((1,3,6,1,4,1,1271,2,1,20,1,3,1,1,42),_CienaCesRapsVirtualRingLogicalRingName_Type())
cienaCesRapsVirtualRingLogicalRingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingLogicalRingName.setStatus(_A)
_CienaCesRapsVirtualRingMember_ObjectIdentity=ObjectIdentity
cienaCesRapsVirtualRingMember=_CienaCesRapsVirtualRingMember_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,1,4))
_CienaCesRapsVirtualRingMemberTable_Object=MibTable
cienaCesRapsVirtualRingMemberTable=_CienaCesRapsVirtualRingMemberTable_Object((1,3,6,1,4,1,1271,2,1,20,1,4,1))
if mibBuilder.loadTexts:cienaCesRapsVirtualRingMemberTable.setStatus(_A)
_CienaCesRapsVirtualRingMemberEntry_Object=MibTableRow
cienaCesRapsVirtualRingMemberEntry=_CienaCesRapsVirtualRingMemberEntry_Object((1,3,6,1,4,1,1271,2,1,20,1,4,1,1))
cienaCesRapsVirtualRingMemberEntry.setIndexNames((0,_D,_P),(0,_D,_f))
if mibBuilder.loadTexts:cienaCesRapsVirtualRingMemberEntry.setStatus(_A)
class _CienaCesRapsVirtualRingMemberVsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesRapsVirtualRingMemberVsId_Type.__name__=_C
_CienaCesRapsVirtualRingMemberVsId_Object=MibTableColumn
cienaCesRapsVirtualRingMemberVsId=_CienaCesRapsVirtualRingMemberVsId_Object((1,3,6,1,4,1,1271,2,1,20,1,4,1,1,2),_CienaCesRapsVirtualRingMemberVsId_Type())
cienaCesRapsVirtualRingMemberVsId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesRapsVirtualRingMemberVsId.setStatus(_A)
_CienaCesRapsMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBConformance=_CienaCesRapsMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,2))
_CienaCesRapsMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBCompliances=_CienaCesRapsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,2,1))
_CienaCesRapsMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBGroups=_CienaCesRapsMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,20,2,2))
_CienaCesRapsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBNotificationPrefix=_CienaCesRapsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,18))
_CienaCesRapsMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesRapsMIBNotifications=_CienaCesRapsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,18,0))
cienaCesRapsAlarmClearNotification=NotificationType((1,3,6,1,4,1,1271,2,2,18,0,1))
cienaCesRapsAlarmClearNotification.setObjects(*((_E,_G),(_E,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:cienaCesRapsAlarmClearNotification.setStatus(_A)
cienaCesRapsAlarmProtectionSwitchingNotification=NotificationType((1,3,6,1,4,1,1271,2,2,18,0,2))
cienaCesRapsAlarmProtectionSwitchingNotification.setObjects(*((_E,_G),(_E,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:cienaCesRapsAlarmProtectionSwitchingNotification.setStatus(_A)
cienaCesRapsAlarmProvisionMismatchNotification=NotificationType((1,3,6,1,4,1,1271,2,2,18,0,3))
cienaCesRapsAlarmProvisionMismatchNotification.setObjects(*((_E,_G),(_E,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:cienaCesRapsAlarmProvisionMismatchNotification.setStatus(_A)
cienaCesRapsAlarmNoRapsPduReceivedNotification=NotificationType((1,3,6,1,4,1,1271,2,2,18,0,4))
cienaCesRapsAlarmNoRapsPduReceivedNotification.setObjects(*((_E,_G),(_E,_F),(_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:cienaCesRapsAlarmNoRapsPduReceivedNotification.setStatus(_A)
cienaCesRapsAlarmNoRplOwnerDetectedNotification=NotificationType((1,3,6,1,4,1,1271,2,2,18,0,5))
cienaCesRapsAlarmNoRplOwnerDetectedNotification.setObjects(*((_E,_G),(_E,_F),(_D,_K),(_D,_L),(_D,_g)))
if mibBuilder.loadTexts:cienaCesRapsAlarmNoRplOwnerDetectedNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cienaCesRapsMIB':cienaCesRapsMIB,'cienaCesRapsMIBObjects':cienaCesRapsMIBObjects,'cienaCesRapsGlobal':cienaCesRapsGlobal,'cienaCesRapsGlobalAttrs':cienaCesRapsGlobalAttrs,'cienaCesRapsState':cienaCesRapsState,'cienaCesRapsNodeId':cienaCesRapsNodeId,'cienaCesRapsEtherType':cienaCesRapsEtherType,'cienaCesRapsNumberOfRings':cienaCesRapsNumberOfRings,'cienaCesRapsLogicalRing':cienaCesRapsLogicalRing,'cienaCesRapsLogicalRingTable':cienaCesRapsLogicalRingTable,'cienaCesRapsLogicalRingEntry':cienaCesRapsLogicalRingEntry,_T:cienaCesRapsLogicalRingIndex,'cienaCesRapsLogicalRingName':cienaCesRapsLogicalRingName,'cienaCesRapsLogicalRingId':cienaCesRapsLogicalRingId,'cienaCesRapsLogicalRingGuardTime':cienaCesRapsLogicalRingGuardTime,'cienaCesRapsLogicalRingWtr':cienaCesRapsLogicalRingWtr,'cienaCesRapsLogicalRingWtb':cienaCesRapsLogicalRingWtb,'cienaCesRapsLogicalRingWestPortId':cienaCesRapsLogicalRingWestPortId,'cienaCesRapsLogicalRingWestHoldOffTime':cienaCesRapsLogicalRingWestHoldOffTime,'cienaCesRapsLogicalRingWestForce':cienaCesRapsLogicalRingWestForce,'cienaCesRapsLogicalRingWestCfmService':cienaCesRapsLogicalRingWestCfmService,'cienaCesRapsLogicalRingEastPortId':cienaCesRapsLogicalRingEastPortId,'cienaCesRapsLogicalRingEastHoldOffTime':cienaCesRapsLogicalRingEastHoldOffTime,'cienaCesRapsLogicalRingEastForce':cienaCesRapsLogicalRingEastForce,'cienaCesRapsLogicalRingEastCfmService':cienaCesRapsLogicalRingEastCfmService,'cienaCesRapsLogicalRingNumberOfVirtualRings':cienaCesRapsLogicalRingNumberOfVirtualRings,'cienaCesRapsVirtualRing':cienaCesRapsVirtualRing,'cienaCesRapsVirtualRingTable':cienaCesRapsVirtualRingTable,'cienaCesRapsVirtualRingEntry':cienaCesRapsVirtualRingEntry,_P:cienaCesRapsVirtualRingIndex,_L:cienaCesRapsVirtualRingName,'cienaCesRapsVirtualRingVid':cienaCesRapsVirtualRingVid,'cienaCesRapsVirtualRingLogicalRingId':cienaCesRapsVirtualRingLogicalRingId,'cienaCesRapsVirtualRingMel':cienaCesRapsVirtualRingMel,'cienaCesRapsVirtualRingRevertive':cienaCesRapsVirtualRingRevertive,'cienaCesRapsVirtualRingState':cienaCesRapsVirtualRingState,'cienaCesRapsVirtualRingStatus':cienaCesRapsVirtualRingStatus,_M:cienaCesRapsVirtualRingAlarm,'cienaCesRapsVirtualRingNumOfSwitchOvers':cienaCesRapsVirtualRingNumOfSwitchOvers,'cienaCesRapsVirtualRingUptimeFromLastFailure':cienaCesRapsVirtualRingUptimeFromLastFailure,'cienaCesRapsVirtualRingTotalDownTime':cienaCesRapsVirtualRingTotalDownTime,'cienaCesRapsVirtualRingWestPortRpl':cienaCesRapsVirtualRingWestPortRpl,'cienaCesRapsVirtualRingWestPortState':cienaCesRapsVirtualRingWestPortState,'cienaCesRapsVirtualRingWestPortStatus':cienaCesRapsVirtualRingWestPortStatus,'cienaCesRapsVirtualRingWestPortNrRxd':cienaCesRapsVirtualRingWestPortNrRxd,'cienaCesRapsVirtualRingWestPortNrTxd':cienaCesRapsVirtualRingWestPortNrTxd,'cienaCesRapsVirtualRingWestPortSfRxd':cienaCesRapsVirtualRingWestPortSfRxd,'cienaCesRapsVirtualRingWestPortSfTxd':cienaCesRapsVirtualRingWestPortSfTxd,'cienaCesRapsVirtualRingWestPortFsRxd':cienaCesRapsVirtualRingWestPortFsRxd,'cienaCesRapsVirtualRingWestPortFsTxd':cienaCesRapsVirtualRingWestPortFsTxd,'cienaCesRapsVirtualRingWestPortNrRbRxd':cienaCesRapsVirtualRingWestPortNrRbRxd,'cienaCesRapsVirtualRingWestPortNrRbTxd':cienaCesRapsVirtualRingWestPortNrRbTxd,'cienaCesRapsVirtualRingEastPortRpl':cienaCesRapsVirtualRingEastPortRpl,'cienaCesRapsVirtualRingEastPortState':cienaCesRapsVirtualRingEastPortState,'cienaCesRapsVirtualRingEastPortStatus':cienaCesRapsVirtualRingEastPortStatus,'cienaCesRapsVirtualRingEastPortNrRxd':cienaCesRapsVirtualRingEastPortNrRxd,'cienaCesRapsVirtualRingEastPortNrTxd':cienaCesRapsVirtualRingEastPortNrTxd,'cienaCesRapsVirtualRingEastPortSfRxd':cienaCesRapsVirtualRingEastPortSfRxd,'cienaCesRapsVirtualRingEastPortSfTxd':cienaCesRapsVirtualRingEastPortSfTxd,'cienaCesRapsVirtualRingEastPortFsRxd':cienaCesRapsVirtualRingEastPortFsRxd,'cienaCesRapsVirtualRingEastPortFsTxd':cienaCesRapsVirtualRingEastPortFsTxd,'cienaCesRapsVirtualRingEastPortNrRbRxd':cienaCesRapsVirtualRingEastPortNrRbRxd,'cienaCesRapsVirtualRingEastPortNrRbTxd':cienaCesRapsVirtualRingEastPortNrRbTxd,'cienaCesRapsVirtualRingType':cienaCesRapsVirtualRingType,'cienaCesRapsVirtualRingSubRingPortTerm':cienaCesRapsVirtualRingSubRingPortTerm,_K:cienaCesRapsVirtualRingNotifIndex,_g:cienaCesRapsVirtualRingAlarmExtended,'cienaCesRapsVirtualRingWestForce':cienaCesRapsVirtualRingWestForce,'cienaCesRapsVirtualRingEastForce':cienaCesRapsVirtualRingEastForce,'cienaCesRapsVirtualRingFlushPropagate':cienaCesRapsVirtualRingFlushPropagate,'cienaCesRapsVirtualRingLogicalRingName':cienaCesRapsVirtualRingLogicalRingName,'cienaCesRapsVirtualRingMember':cienaCesRapsVirtualRingMember,'cienaCesRapsVirtualRingMemberTable':cienaCesRapsVirtualRingMemberTable,'cienaCesRapsVirtualRingMemberEntry':cienaCesRapsVirtualRingMemberEntry,_f:cienaCesRapsVirtualRingMemberVsId,'cienaCesRapsMIBConformance':cienaCesRapsMIBConformance,'cienaCesRapsMIBCompliances':cienaCesRapsMIBCompliances,'cienaCesRapsMIBGroups':cienaCesRapsMIBGroups,'cienaCesRapsMIBNotificationPrefix':cienaCesRapsMIBNotificationPrefix,'cienaCesRapsMIBNotifications':cienaCesRapsMIBNotifications,'cienaCesRapsAlarmClearNotification':cienaCesRapsAlarmClearNotification,'cienaCesRapsAlarmProtectionSwitchingNotification':cienaCesRapsAlarmProtectionSwitchingNotification,'cienaCesRapsAlarmProvisionMismatchNotification':cienaCesRapsAlarmProvisionMismatchNotification,'cienaCesRapsAlarmNoRapsPduReceivedNotification':cienaCesRapsAlarmNoRapsPduReceivedNotification,'cienaCesRapsAlarmNoRplOwnerDetectedNotification':cienaCesRapsAlarmNoRplOwnerDetectedNotification})