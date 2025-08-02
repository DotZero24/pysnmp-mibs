_Q='adTa5kStandbyNotReadyReasonIndex'
_P='ADTRAN-TA5K-REDUNDANCY-MIB'
_O='standby'
_N='active'
_M='ifIndex'
_L='IF-MIB'
_K='read-only'
_J='TruthValue'
_I='Integer32'
_H='read-write'
_G='sysName'
_F='SNMPv2-MIB'
_E='adTrapInformSeqNum'
_D='ADTRAN-GENTRAPINFORM-MIB'
_C='adGenSlotInfoIndex'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_B,_C)
adGenTa5kRedundancy,adGenTa5kRedundancyID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kRedundancy','adGenTa5kRedundancyID')
adTrapInformSeqNum,=mibBuilder.importSymbols(_D,_E)
adIdentity,adIdentityShared,adMgmt,adProducts=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity','adIdentityShared','adMgmt','adProducts')
ifIndex,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_F,_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
adTa5kRedundancyModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,1,1))
if mibBuilder.loadTexts:adTa5kRedundancyModuleIdentity.setRevisions(('2011-10-12 14:00',))
_AdTa5kEquipmentRedundancy_ObjectIdentity=ObjectIdentity
adTa5kEquipmentRedundancy=_AdTa5kEquipmentRedundancy_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,1,1))
_AdTa5kEquipmentRedundancyTable_Object=MibTable
adTa5kEquipmentRedundancyTable=_AdTa5kEquipmentRedundancyTable_Object((1,3,6,1,4,1,664,5,67,1,1,1,1))
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyTable.setStatus(_A)
_AdTa5kEquipmentRedundancyEntry_Object=MibTableRow
adTa5kEquipmentRedundancyEntry=_AdTa5kEquipmentRedundancyEntry_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1))
adTa5kEquipmentRedundancyEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyEntry.setStatus(_A)
class _AdTa5kEquipmentRedundancySupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('true',1),('peerNotResponding',2),('peerIncompatible',3),('peerNotPresent',4),('peerNotReady',5)))
_AdTa5kEquipmentRedundancySupported_Type.__name__=_I
_AdTa5kEquipmentRedundancySupported_Object=MibTableColumn
adTa5kEquipmentRedundancySupported=_AdTa5kEquipmentRedundancySupported_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,1),_AdTa5kEquipmentRedundancySupported_Type())
adTa5kEquipmentRedundancySupported.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancySupported.setStatus(_A)
class _AdTa5kEquipmentRedundancyRevertive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AdTa5kEquipmentRedundancyRevertive_Type.__name__=_I
_AdTa5kEquipmentRedundancyRevertive_Object=MibTableColumn
adTa5kEquipmentRedundancyRevertive=_AdTa5kEquipmentRedundancyRevertive_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,2),_AdTa5kEquipmentRedundancyRevertive_Type())
adTa5kEquipmentRedundancyRevertive.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyRevertive.setStatus(_A)
_AdTa5kEquipmentRedundancyRevertiveTimeout_Type=Integer32
_AdTa5kEquipmentRedundancyRevertiveTimeout_Object=MibTableColumn
adTa5kEquipmentRedundancyRevertiveTimeout=_AdTa5kEquipmentRedundancyRevertiveTimeout_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,3),_AdTa5kEquipmentRedundancyRevertiveTimeout_Type())
adTa5kEquipmentRedundancyRevertiveTimeout.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyRevertiveTimeout.setStatus(_A)
class _AdTa5kEquipmentRedundancyForceFailover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('failover',1),('notapplicable',2)))
_AdTa5kEquipmentRedundancyForceFailover_Type.__name__=_I
_AdTa5kEquipmentRedundancyForceFailover_Object=MibTableColumn
adTa5kEquipmentRedundancyForceFailover=_AdTa5kEquipmentRedundancyForceFailover_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,4),_AdTa5kEquipmentRedundancyForceFailover_Type())
adTa5kEquipmentRedundancyForceFailover.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyForceFailover.setStatus(_A)
class _AdTa5kEquipmentRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),('standbyNotReady',3),('notApplicable',4)))
_AdTa5kEquipmentRedundancyState_Type.__name__=_I
_AdTa5kEquipmentRedundancyState_Object=MibTableColumn
adTa5kEquipmentRedundancyState=_AdTa5kEquipmentRedundancyState_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,5),_AdTa5kEquipmentRedundancyState_Type())
adTa5kEquipmentRedundancyState.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyState.setStatus(_A)
_AdTa5kEquipmentRedundancyPeerSlot_Type=Integer32
_AdTa5kEquipmentRedundancyPeerSlot_Object=MibTableColumn
adTa5kEquipmentRedundancyPeerSlot=_AdTa5kEquipmentRedundancyPeerSlot_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,6),_AdTa5kEquipmentRedundancyPeerSlot_Type())
adTa5kEquipmentRedundancyPeerSlot.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyPeerSlot.setStatus(_A)
class _AdTa5kEquipmentRedundancyFeatureEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_AdTa5kEquipmentRedundancyFeatureEnabled_Type.__name__=_I
_AdTa5kEquipmentRedundancyFeatureEnabled_Object=MibTableColumn
adTa5kEquipmentRedundancyFeatureEnabled=_AdTa5kEquipmentRedundancyFeatureEnabled_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,7),_AdTa5kEquipmentRedundancyFeatureEnabled_Type())
adTa5kEquipmentRedundancyFeatureEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyFeatureEnabled.setStatus(_A)
class _AdTa5kEquipmentRedundancyFacilityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sharedFacilities',0),('dualFacilities',1),('separateFacilities',2)))
_AdTa5kEquipmentRedundancyFacilityType_Type.__name__=_I
_AdTa5kEquipmentRedundancyFacilityType_Object=MibTableColumn
adTa5kEquipmentRedundancyFacilityType=_AdTa5kEquipmentRedundancyFacilityType_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,8),_AdTa5kEquipmentRedundancyFacilityType_Type())
adTa5kEquipmentRedundancyFacilityType.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyFacilityType.setStatus(_A)
_AdTa5kEquipmentRedundancyStandbyReasonsCount_Type=Integer32
_AdTa5kEquipmentRedundancyStandbyReasonsCount_Object=MibTableColumn
adTa5kEquipmentRedundancyStandbyReasonsCount=_AdTa5kEquipmentRedundancyStandbyReasonsCount_Object((1,3,6,1,4,1,664,5,67,1,1,1,1,1,9),_AdTa5kEquipmentRedundancyStandbyReasonsCount_Type())
adTa5kEquipmentRedundancyStandbyReasonsCount.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kEquipmentRedundancyStandbyReasonsCount.setStatus(_A)
_AdTa5kStandbyNotReadyReasonsTable_Object=MibTable
adTa5kStandbyNotReadyReasonsTable=_AdTa5kStandbyNotReadyReasonsTable_Object((1,3,6,1,4,1,664,5,67,1,1,1,3))
if mibBuilder.loadTexts:adTa5kStandbyNotReadyReasonsTable.setStatus(_A)
_AdTa5kStandbyNotReadyReasonEntry_Object=MibTableRow
adTa5kStandbyNotReadyReasonEntry=_AdTa5kStandbyNotReadyReasonEntry_Object((1,3,6,1,4,1,664,5,67,1,1,1,3,1))
adTa5kStandbyNotReadyReasonEntry.setIndexNames((0,_B,_C),(0,_P,_Q))
if mibBuilder.loadTexts:adTa5kStandbyNotReadyReasonEntry.setStatus(_A)
_AdTa5kStandbyNotReadyReasonIndex_Type=Integer32
_AdTa5kStandbyNotReadyReasonIndex_Object=MibTableColumn
adTa5kStandbyNotReadyReasonIndex=_AdTa5kStandbyNotReadyReasonIndex_Object((1,3,6,1,4,1,664,5,67,1,1,1,3,1,1),_AdTa5kStandbyNotReadyReasonIndex_Type())
adTa5kStandbyNotReadyReasonIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adTa5kStandbyNotReadyReasonIndex.setStatus(_A)
_AdTa5kStandbyNotReadyReason_Type=DisplayString
_AdTa5kStandbyNotReadyReason_Object=MibTableColumn
adTa5kStandbyNotReadyReason=_AdTa5kStandbyNotReadyReason_Object((1,3,6,1,4,1,664,5,67,1,1,1,3,1,2),_AdTa5kStandbyNotReadyReason_Type())
adTa5kStandbyNotReadyReason.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kStandbyNotReadyReason.setStatus(_A)
_AdTa5kFacilityRedundancy_ObjectIdentity=ObjectIdentity
adTa5kFacilityRedundancy=_AdTa5kFacilityRedundancy_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,1,2))
_AdTa5kFacilityRedundancyTable_Object=MibTable
adTa5kFacilityRedundancyTable=_AdTa5kFacilityRedundancyTable_Object((1,3,6,1,4,1,664,5,67,1,1,2,1))
if mibBuilder.loadTexts:adTa5kFacilityRedundancyTable.setStatus(_A)
_AdTa5kFacilityRedundancyEntry_Object=MibTableRow
adTa5kFacilityRedundancyEntry=_AdTa5kFacilityRedundancyEntry_Object((1,3,6,1,4,1,664,5,67,1,1,2,1,1))
adTa5kFacilityRedundancyEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:adTa5kFacilityRedundancyEntry.setStatus(_A)
class _AdTa5kFacilityRedundancySupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('protected',1),('redundantFacilityNotPresent',2),('redundantFacilityNotCompatible',3),('redundantFacilityAdminDown',4),('redundantFacilityLinkDown',5),('redundantFacilityInUse',6),('redundantEquipmentAdminDown',7)))
_AdTa5kFacilityRedundancySupported_Type.__name__=_I
_AdTa5kFacilityRedundancySupported_Object=MibTableColumn
adTa5kFacilityRedundancySupported=_AdTa5kFacilityRedundancySupported_Object((1,3,6,1,4,1,664,5,67,1,1,2,1,1,1),_AdTa5kFacilityRedundancySupported_Type())
adTa5kFacilityRedundancySupported.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kFacilityRedundancySupported.setStatus(_A)
class _AdTa5kFacilityRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_AdTa5kFacilityRedundancyState_Type.__name__=_I
_AdTa5kFacilityRedundancyState_Object=MibTableColumn
adTa5kFacilityRedundancyState=_AdTa5kFacilityRedundancyState_Object((1,3,6,1,4,1,664,5,67,1,1,2,1,1,2),_AdTa5kFacilityRedundancyState_Type())
adTa5kFacilityRedundancyState.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kFacilityRedundancyState.setStatus(_A)
_AdTa5kFacilityRedundancyForceProtect_Type=Integer32
_AdTa5kFacilityRedundancyForceProtect_Object=MibTableColumn
adTa5kFacilityRedundancyForceProtect=_AdTa5kFacilityRedundancyForceProtect_Object((1,3,6,1,4,1,664,5,67,1,1,2,1,1,3),_AdTa5kFacilityRedundancyForceProtect_Type())
adTa5kFacilityRedundancyForceProtect.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kFacilityRedundancyForceProtect.setStatus(_A)
_AdTa5kFacilityRedundancyProtectedByIfIndex_Type=Integer32
_AdTa5kFacilityRedundancyProtectedByIfIndex_Object=MibTableColumn
adTa5kFacilityRedundancyProtectedByIfIndex=_AdTa5kFacilityRedundancyProtectedByIfIndex_Object((1,3,6,1,4,1,664,5,67,1,1,2,1,1,4),_AdTa5kFacilityRedundancyProtectedByIfIndex_Type())
adTa5kFacilityRedundancyProtectedByIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:adTa5kFacilityRedundancyProtectedByIfIndex.setStatus(_A)
_AdTa5kRedundancyAlarmPrefix_ObjectIdentity=ObjectIdentity
adTa5kRedundancyAlarmPrefix=_AdTa5kRedundancyAlarmPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,1,3))
_AdTa5kRedundancyAlarms_ObjectIdentity=ObjectIdentity
adTa5kRedundancyAlarms=_AdTa5kRedundancyAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,1,3,0))
_AdTa5kRedundancyAlarmProv_ObjectIdentity=ObjectIdentity
adTa5kRedundancyAlarmProv=_AdTa5kRedundancyAlarmProv_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,1,4))
_AdTa5kRedundancyAlarmProvTable_Object=MibTable
adTa5kRedundancyAlarmProvTable=_AdTa5kRedundancyAlarmProvTable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1))
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvTable.setStatus(_A)
_AdTa5kRedundancyAlarmProvEntry_Object=MibTableRow
adTa5kRedundancyAlarmProvEntry=_AdTa5kRedundancyAlarmProvEntry_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1))
adTa5kRedundancyAlarmProvEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvEntry.setStatus(_A)
class _AdTa5kRedundancyAlarmProvCardActiveEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvCardActiveEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvCardActiveEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvCardActiveEnable=_AdTa5kRedundancyAlarmProvCardActiveEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,1),_AdTa5kRedundancyAlarmProvCardActiveEnable_Type())
adTa5kRedundancyAlarmProvCardActiveEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvCardActiveEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvProtectionUnavailableEnable=_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,2),_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type())
adTa5kRedundancyAlarmProvProtectionUnavailableEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvProtectionUnavailableEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable=_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,3),_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type())
adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable=_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,4),_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type())
adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable=_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,5),_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type())
adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvManualSwitchEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvManualSwitchEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvManualSwitchEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvManualSwitchEnable=_AdTa5kRedundancyAlarmProvManualSwitchEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,6),_AdTa5kRedundancyAlarmProvManualSwitchEnable_Type())
adTa5kRedundancyAlarmProvManualSwitchEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvManualSwitchEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvSwitchToProtectEnable=_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,7),_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type())
adTa5kRedundancyAlarmProvSwitchToProtectEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvSwitchToProtectEnable.setStatus(_A)
class _AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type(TruthValue):defaultValue=1
_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type.__name__=_J
_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Object=MibTableColumn
adTa5kRedundancyAlarmProvAutomaticSwitchEnable=_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Object((1,3,6,1,4,1,664,5,67,1,1,4,1,1,8),_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type())
adTa5kRedundancyAlarmProvAutomaticSwitchEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:adTa5kRedundancyAlarmProvAutomaticSwitchEnable.setStatus(_A)
adTa5kRedundancyCardActive=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,1))
adTa5kRedundancyCardActive.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyCardActive.setStatus(_A)
adTa5kRedundancyProtectionAvailable=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,2))
adTa5kRedundancyProtectionAvailable.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyProtectionAvailable.setStatus(_A)
adTa5kRedundancyProtectionUnavailable=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,3))
adTa5kRedundancyProtectionUnavailable.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyProtectionUnavailable.setStatus(_A)
adTa5kRedundancyPeerCodeVersionMismatchClear=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,4))
adTa5kRedundancyPeerCodeVersionMismatchClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerCodeVersionMismatchClear.setStatus(_A)
adTa5kRedundancyPeerCodeVersionMismatch=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,5))
adTa5kRedundancyPeerCodeVersionMismatch.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerCodeVersionMismatch.setStatus(_A)
adTa5kRedundancyPeerDatabaseMirroringInSync=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,6))
adTa5kRedundancyPeerDatabaseMirroringInSync.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerDatabaseMirroringInSync.setStatus(_A)
adTa5kRedundancyPeerDbMirroringSyncInProgress=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,7))
adTa5kRedundancyPeerDbMirroringSyncInProgress.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerDbMirroringSyncInProgress.setStatus(_A)
adTa5kRedundancyPeerRemoteDatabaseSyncInProgress=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,8))
adTa5kRedundancyPeerRemoteDatabaseSyncInProgress.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerRemoteDatabaseSyncInProgress.setStatus(_A)
adTa5kRedundancyPeerRemoteDatabaseInSync=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,9))
adTa5kRedundancyPeerRemoteDatabaseInSync.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyPeerRemoteDatabaseInSync.setStatus(_A)
adTa5kRedundancyManualSwitch=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,10))
adTa5kRedundancyManualSwitch.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyManualSwitch.setStatus(_A)
adTa5kEquipmentRedundancySwitchToProtectClear=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,12))
adTa5kEquipmentRedundancySwitchToProtectClear.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kEquipmentRedundancySwitchToProtectClear.setStatus(_A)
adTa5kEquipmentRedundancySwitchToProtect=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,13))
adTa5kEquipmentRedundancySwitchToProtect.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kEquipmentRedundancySwitchToProtect.setStatus(_A)
adTa5kRedundancyAutomaticSwitch=NotificationType((1,3,6,1,4,1,664,5,67,1,1,3,0,14))
adTa5kRedundancyAutomaticSwitch.setObjects(*((_D,_E),(_F,_G),(_B,_C)))
if mibBuilder.loadTexts:adTa5kRedundancyAutomaticSwitch.setStatus(_A)
mibBuilder.exportSymbols(_P,**{'adTa5kEquipmentRedundancy':adTa5kEquipmentRedundancy,'adTa5kEquipmentRedundancyTable':adTa5kEquipmentRedundancyTable,'adTa5kEquipmentRedundancyEntry':adTa5kEquipmentRedundancyEntry,'adTa5kEquipmentRedundancySupported':adTa5kEquipmentRedundancySupported,'adTa5kEquipmentRedundancyRevertive':adTa5kEquipmentRedundancyRevertive,'adTa5kEquipmentRedundancyRevertiveTimeout':adTa5kEquipmentRedundancyRevertiveTimeout,'adTa5kEquipmentRedundancyForceFailover':adTa5kEquipmentRedundancyForceFailover,'adTa5kEquipmentRedundancyState':adTa5kEquipmentRedundancyState,'adTa5kEquipmentRedundancyPeerSlot':adTa5kEquipmentRedundancyPeerSlot,'adTa5kEquipmentRedundancyFeatureEnabled':adTa5kEquipmentRedundancyFeatureEnabled,'adTa5kEquipmentRedundancyFacilityType':adTa5kEquipmentRedundancyFacilityType,'adTa5kEquipmentRedundancyStandbyReasonsCount':adTa5kEquipmentRedundancyStandbyReasonsCount,'adTa5kStandbyNotReadyReasonsTable':adTa5kStandbyNotReadyReasonsTable,'adTa5kStandbyNotReadyReasonEntry':adTa5kStandbyNotReadyReasonEntry,_Q:adTa5kStandbyNotReadyReasonIndex,'adTa5kStandbyNotReadyReason':adTa5kStandbyNotReadyReason,'adTa5kFacilityRedundancy':adTa5kFacilityRedundancy,'adTa5kFacilityRedundancyTable':adTa5kFacilityRedundancyTable,'adTa5kFacilityRedundancyEntry':adTa5kFacilityRedundancyEntry,'adTa5kFacilityRedundancySupported':adTa5kFacilityRedundancySupported,'adTa5kFacilityRedundancyState':adTa5kFacilityRedundancyState,'adTa5kFacilityRedundancyForceProtect':adTa5kFacilityRedundancyForceProtect,'adTa5kFacilityRedundancyProtectedByIfIndex':adTa5kFacilityRedundancyProtectedByIfIndex,'adTa5kRedundancyAlarmPrefix':adTa5kRedundancyAlarmPrefix,'adTa5kRedundancyAlarms':adTa5kRedundancyAlarms,'adTa5kRedundancyCardActive':adTa5kRedundancyCardActive,'adTa5kRedundancyProtectionAvailable':adTa5kRedundancyProtectionAvailable,'adTa5kRedundancyProtectionUnavailable':adTa5kRedundancyProtectionUnavailable,'adTa5kRedundancyPeerCodeVersionMismatchClear':adTa5kRedundancyPeerCodeVersionMismatchClear,'adTa5kRedundancyPeerCodeVersionMismatch':adTa5kRedundancyPeerCodeVersionMismatch,'adTa5kRedundancyPeerDatabaseMirroringInSync':adTa5kRedundancyPeerDatabaseMirroringInSync,'adTa5kRedundancyPeerDbMirroringSyncInProgress':adTa5kRedundancyPeerDbMirroringSyncInProgress,'adTa5kRedundancyPeerRemoteDatabaseSyncInProgress':adTa5kRedundancyPeerRemoteDatabaseSyncInProgress,'adTa5kRedundancyPeerRemoteDatabaseInSync':adTa5kRedundancyPeerRemoteDatabaseInSync,'adTa5kRedundancyManualSwitch':adTa5kRedundancyManualSwitch,'adTa5kEquipmentRedundancySwitchToProtectClear':adTa5kEquipmentRedundancySwitchToProtectClear,'adTa5kEquipmentRedundancySwitchToProtect':adTa5kEquipmentRedundancySwitchToProtect,'adTa5kRedundancyAutomaticSwitch':adTa5kRedundancyAutomaticSwitch,'adTa5kRedundancyAlarmProv':adTa5kRedundancyAlarmProv,'adTa5kRedundancyAlarmProvTable':adTa5kRedundancyAlarmProvTable,'adTa5kRedundancyAlarmProvEntry':adTa5kRedundancyAlarmProvEntry,'adTa5kRedundancyAlarmProvCardActiveEnable':adTa5kRedundancyAlarmProvCardActiveEnable,'adTa5kRedundancyAlarmProvProtectionUnavailableEnable':adTa5kRedundancyAlarmProvProtectionUnavailableEnable,'adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable':adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable,'adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable':adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable,'adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable':adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable,'adTa5kRedundancyAlarmProvManualSwitchEnable':adTa5kRedundancyAlarmProvManualSwitchEnable,'adTa5kRedundancyAlarmProvSwitchToProtectEnable':adTa5kRedundancyAlarmProvSwitchToProtectEnable,'adTa5kRedundancyAlarmProvAutomaticSwitchEnable':adTa5kRedundancyAlarmProvAutomaticSwitchEnable,'adTa5kRedundancyModuleIdentity':adTa5kRedundancyModuleIdentity})