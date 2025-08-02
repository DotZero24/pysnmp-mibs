_t='cfprStorageVsanRefInstanceId'
_s='cfprStorageVirtualDriveInstanceId'
_r='cfprStorageTransportableFlashModuleInstanceId'
_q='cfprStorageSystemFsmTaskInstanceId'
_p='cfprStorageSystemFsmStageInstanceId'
_o='cfprStorageSystemFsmInstanceId'
_n='cfprStorageSystemInstanceId'
_m='cfprStorageRaidBatteryInstanceId'
_l='cfprStorageQualInstanceId'
_k='cfprStorageOperationInstanceId'
_j='cfprStorageNodeEpInstanceId'
_i='cfprStorageMezzFlashLifeInstanceId'
_h='cfprStorageLunDiskInstanceId'
_g='cfprStorageLocalLunInstanceId'
_f='cfprStorageLocalDiskSlotEpInstanceId'
_e='cfprStorageLocalDiskPartitionInstanceId'
_d='cfprStorageLocalDiskConfigPolicyInstanceId'
_c='cfprStorageLocalDiskConfigDefInstanceId'
_b='cfprStorageLocalDiskInstanceId'
_a='cfprStorageItemInstanceId'
_Z='cfprStorageInitiatorInstanceId'
_Y='cfprStorageIniGroupInstanceId'
_X='cfprStorageIScsiTargetIfInstanceId'
_W='cfprStorageFlexFlashVirtualDriveInstanceId'
_V='cfprStorageFlexFlashDriveInstanceId'
_U='cfprStorageFlexFlashControllerFsmTaskInstanceId'
_T='cfprStorageFlexFlashControllerFsmStageInstanceId'
_S='cfprStorageFlexFlashControllerFsmInstanceId'
_R='cfprStorageFlexFlashControllerInstanceId'
_Q='cfprStorageFlexFlashCardInstanceId'
_P='cfprStorageFcTargetIfInstanceId'
_O='cfprStorageFcTargetEpInstanceId'
_N='cfprStorageFcIfInstanceId'
_M='cfprStorageEtherIfInstanceId'
_L='cfprStorageEpUserInstanceId'
_K='cfprStorageEnclosureInstanceId'
_J='cfprStorageDriveInstanceId'
_I='cfprStorageDomainEpInstanceId'
_H='cfprStorageControllerInstanceId'
_G='cfprStorageConnectionPolicyInstanceId'
_F='cfprStorageConnectionDefInstanceId'
_E='cfprStorageAuthKeyInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-STORAGE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAaaConfigState,CfprConditionRemoteInvRslt,CfprEquipmentOperability,CfprEquipmentPowerState,CfprEquipmentPresence,CfprEquipmentSensorThresholdStatus,CfprFabricZoningState,CfprFsmCompletion,CfprFsmFlags,CfprFsmFsmStageStatus,CfprFsmLifecycle,CfprPolicyPolicyOwner,CfprStorageAccessType,CfprStorageActualWriteType,CfprStorageBatteryType,CfprStorageBbuStatus,CfprStorageBootableType,CfprStorageCacheType,CfprStorageConfiguration,CfprStorageConfiguredWriteType,CfprStorageConnectionProtocol,CfprStorageControllerFaultMonitoring,CfprStorageControllerId,CfprStorageControllerStatus,CfprStorageControllerType,CfprStorageDisklessAction,CfprStorageEpAccess,CfprStorageEtherIfVlanType,CfprStorageFFCardHealth,CfprStorageFFCardMode,CfprStorageFFCardSizeMismatch,CfprStorageFFCardState,CfprStorageFFCardSync,CfprStorageFFCardWriteEnable,CfprStorageFFControllerHealth,CfprStorageFFControllerState,CfprStorageFFDriveRemovable,CfprStorageFFDriveState,CfprStorageFFDriveType,CfprStorageFFDriveVisible,CfprStorageFFFormatRunning,CfprStorageFFHasError,CfprStorageFFRAIDHealth,CfprStorageFFRAIDState,CfprStorageFFRWType,CfprStorageFFRaidSyncSupport,CfprStorageFFSlotENUM,CfprStorageFFType,CfprStorageFcZoningType,CfprStorageFileSystemStatus,CfprStorageFlexFlashControllerFsmCurrentFsm,CfprStorageFlexFlashControllerFsmStageName,CfprStorageFlexFlashControllerFsmTaskItem,CfprStorageFlexFlashControllerId,CfprStorageIOType,CfprStorageIniGroupOperProtocol,CfprStorageIniGroupOwner,CfprStorageIniGroupProtocol,CfprStorageKeyType,CfprStorageLearnCycleRequested,CfprStorageLearnMode,CfprStorageLinkSpeed,CfprStorageLocalDiskConfigFlexFlashRAIDReportingState,CfprStorageLocalDiskConfigFlexFlashState,CfprStorageLocalDiskMode,CfprStorageLocalDiskPartitionType,CfprStorageLunType,CfprStorageOperState,CfprStorageOperatingModeType,CfprStorageOperationRequestType,CfprStorageOperationState,CfprStorageOperationStateType,CfprStorageOperationType,CfprStoragePDriveStatus,CfprStoragePowerState,CfprStorageProtocol,CfprStorageRaidBatteryOperabilityQualifier,CfprStorageReadType,CfprStorageSystemFsmCurrentFsm,CfprStorageSystemFsmStageName,CfprStorageSystemFsmTaskItem,CfprStorageTargetPath,CfprStorageTechnology,CfprStorageVDriveState,CfprStorageVsanRefSwitchId,CfprVnicConfigIssues=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAaaConfigState','CfprConditionRemoteInvRslt','CfprEquipmentOperability','CfprEquipmentPowerState','CfprEquipmentPresence','CfprEquipmentSensorThresholdStatus','CfprFabricZoningState','CfprFsmCompletion','CfprFsmFlags','CfprFsmFsmStageStatus','CfprFsmLifecycle','CfprPolicyPolicyOwner','CfprStorageAccessType','CfprStorageActualWriteType','CfprStorageBatteryType','CfprStorageBbuStatus','CfprStorageBootableType','CfprStorageCacheType','CfprStorageConfiguration','CfprStorageConfiguredWriteType','CfprStorageConnectionProtocol','CfprStorageControllerFaultMonitoring','CfprStorageControllerId','CfprStorageControllerStatus','CfprStorageControllerType','CfprStorageDisklessAction','CfprStorageEpAccess','CfprStorageEtherIfVlanType','CfprStorageFFCardHealth','CfprStorageFFCardMode','CfprStorageFFCardSizeMismatch','CfprStorageFFCardState','CfprStorageFFCardSync','CfprStorageFFCardWriteEnable','CfprStorageFFControllerHealth','CfprStorageFFControllerState','CfprStorageFFDriveRemovable','CfprStorageFFDriveState','CfprStorageFFDriveType','CfprStorageFFDriveVisible','CfprStorageFFFormatRunning','CfprStorageFFHasError','CfprStorageFFRAIDHealth','CfprStorageFFRAIDState','CfprStorageFFRWType','CfprStorageFFRaidSyncSupport','CfprStorageFFSlotENUM','CfprStorageFFType','CfprStorageFcZoningType','CfprStorageFileSystemStatus','CfprStorageFlexFlashControllerFsmCurrentFsm','CfprStorageFlexFlashControllerFsmStageName','CfprStorageFlexFlashControllerFsmTaskItem','CfprStorageFlexFlashControllerId','CfprStorageIOType','CfprStorageIniGroupOperProtocol','CfprStorageIniGroupOwner','CfprStorageIniGroupProtocol','CfprStorageKeyType','CfprStorageLearnCycleRequested','CfprStorageLearnMode','CfprStorageLinkSpeed','CfprStorageLocalDiskConfigFlexFlashRAIDReportingState','CfprStorageLocalDiskConfigFlexFlashState','CfprStorageLocalDiskMode','CfprStorageLocalDiskPartitionType','CfprStorageLunType','CfprStorageOperState','CfprStorageOperatingModeType','CfprStorageOperationRequestType','CfprStorageOperationState','CfprStorageOperationStateType','CfprStorageOperationType','CfprStoragePDriveStatus','CfprStoragePowerState','CfprStorageProtocol','CfprStorageRaidBatteryOperabilityQualifier','CfprStorageReadType','CfprStorageSystemFsmCurrentFsm','CfprStorageSystemFsmStageName','CfprStorageSystemFsmTaskItem','CfprStorageTargetPath','CfprStorageTechnology','CfprStorageVDriveState','CfprStorageVsanRefSwitchId','CfprVnicConfigIssues')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprStorageObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,74))
_CfprStorageAuthKeyTable_Object=MibTable
cfprStorageAuthKeyTable=_CfprStorageAuthKeyTable_Object((1,3,6,1,4,1,9,9,826,1,74,1))
if mibBuilder.loadTexts:cfprStorageAuthKeyTable.setStatus(_A)
_CfprStorageAuthKeyEntry_Object=MibTableRow
cfprStorageAuthKeyEntry=_CfprStorageAuthKeyEntry_Object((1,3,6,1,4,1,9,9,826,1,74,1,1))
cfprStorageAuthKeyEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprStorageAuthKeyEntry.setStatus(_A)
_CfprStorageAuthKeyInstanceId_Type=CfprManagedObjectId
_CfprStorageAuthKeyInstanceId_Object=MibTableColumn
cfprStorageAuthKeyInstanceId=_CfprStorageAuthKeyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,1),_CfprStorageAuthKeyInstanceId_Type())
cfprStorageAuthKeyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageAuthKeyInstanceId.setStatus(_A)
_CfprStorageAuthKeyDn_Type=CfprManagedObjectDn
_CfprStorageAuthKeyDn_Object=MibTableColumn
cfprStorageAuthKeyDn=_CfprStorageAuthKeyDn_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,2),_CfprStorageAuthKeyDn_Type())
cfprStorageAuthKeyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyDn.setStatus(_A)
_CfprStorageAuthKeyRn_Type=SnmpAdminString
_CfprStorageAuthKeyRn_Object=MibTableColumn
cfprStorageAuthKeyRn=_CfprStorageAuthKeyRn_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,3),_CfprStorageAuthKeyRn_Type())
cfprStorageAuthKeyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyRn.setStatus(_A)
_CfprStorageAuthKeyDescr_Type=SnmpAdminString
_CfprStorageAuthKeyDescr_Object=MibTableColumn
cfprStorageAuthKeyDescr=_CfprStorageAuthKeyDescr_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,4),_CfprStorageAuthKeyDescr_Type())
cfprStorageAuthKeyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyDescr.setStatus(_A)
_CfprStorageAuthKeyIntId_Type=SnmpAdminString
_CfprStorageAuthKeyIntId_Object=MibTableColumn
cfprStorageAuthKeyIntId=_CfprStorageAuthKeyIntId_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,5),_CfprStorageAuthKeyIntId_Type())
cfprStorageAuthKeyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyIntId.setStatus(_A)
_CfprStorageAuthKeyName_Type=SnmpAdminString
_CfprStorageAuthKeyName_Object=MibTableColumn
cfprStorageAuthKeyName=_CfprStorageAuthKeyName_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,6),_CfprStorageAuthKeyName_Type())
cfprStorageAuthKeyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyName.setStatus(_A)
_CfprStorageAuthKeyPassword_Type=SnmpAdminString
_CfprStorageAuthKeyPassword_Object=MibTableColumn
cfprStorageAuthKeyPassword=_CfprStorageAuthKeyPassword_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,7),_CfprStorageAuthKeyPassword_Type())
cfprStorageAuthKeyPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyPassword.setStatus(_A)
_CfprStorageAuthKeyPolicyLevel_Type=Gauge32
_CfprStorageAuthKeyPolicyLevel_Object=MibTableColumn
cfprStorageAuthKeyPolicyLevel=_CfprStorageAuthKeyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,8),_CfprStorageAuthKeyPolicyLevel_Type())
cfprStorageAuthKeyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyPolicyLevel.setStatus(_A)
_CfprStorageAuthKeyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageAuthKeyPolicyOwner_Object=MibTableColumn
cfprStorageAuthKeyPolicyOwner=_CfprStorageAuthKeyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,9),_CfprStorageAuthKeyPolicyOwner_Type())
cfprStorageAuthKeyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyPolicyOwner.setStatus(_A)
_CfprStorageAuthKeyType_Type=CfprStorageKeyType
_CfprStorageAuthKeyType_Object=MibTableColumn
cfprStorageAuthKeyType=_CfprStorageAuthKeyType_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,10),_CfprStorageAuthKeyType_Type())
cfprStorageAuthKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyType.setStatus(_A)
_CfprStorageAuthKeyUserId_Type=SnmpAdminString
_CfprStorageAuthKeyUserId_Object=MibTableColumn
cfprStorageAuthKeyUserId=_CfprStorageAuthKeyUserId_Object((1,3,6,1,4,1,9,9,826,1,74,1,1,11),_CfprStorageAuthKeyUserId_Type())
cfprStorageAuthKeyUserId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageAuthKeyUserId.setStatus(_A)
_CfprStorageConnectionDefTable_Object=MibTable
cfprStorageConnectionDefTable=_CfprStorageConnectionDefTable_Object((1,3,6,1,4,1,9,9,826,1,74,2))
if mibBuilder.loadTexts:cfprStorageConnectionDefTable.setStatus(_A)
_CfprStorageConnectionDefEntry_Object=MibTableRow
cfprStorageConnectionDefEntry=_CfprStorageConnectionDefEntry_Object((1,3,6,1,4,1,9,9,826,1,74,2,1))
cfprStorageConnectionDefEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprStorageConnectionDefEntry.setStatus(_A)
_CfprStorageConnectionDefInstanceId_Type=CfprManagedObjectId
_CfprStorageConnectionDefInstanceId_Object=MibTableColumn
cfprStorageConnectionDefInstanceId=_CfprStorageConnectionDefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,1),_CfprStorageConnectionDefInstanceId_Type())
cfprStorageConnectionDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageConnectionDefInstanceId.setStatus(_A)
_CfprStorageConnectionDefDn_Type=CfprManagedObjectDn
_CfprStorageConnectionDefDn_Object=MibTableColumn
cfprStorageConnectionDefDn=_CfprStorageConnectionDefDn_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,2),_CfprStorageConnectionDefDn_Type())
cfprStorageConnectionDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefDn.setStatus(_A)
_CfprStorageConnectionDefRn_Type=SnmpAdminString
_CfprStorageConnectionDefRn_Object=MibTableColumn
cfprStorageConnectionDefRn=_CfprStorageConnectionDefRn_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,3),_CfprStorageConnectionDefRn_Type())
cfprStorageConnectionDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefRn.setStatus(_A)
_CfprStorageConnectionDefDescr_Type=SnmpAdminString
_CfprStorageConnectionDefDescr_Object=MibTableColumn
cfprStorageConnectionDefDescr=_CfprStorageConnectionDefDescr_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,4),_CfprStorageConnectionDefDescr_Type())
cfprStorageConnectionDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefDescr.setStatus(_A)
_CfprStorageConnectionDefIntId_Type=SnmpAdminString
_CfprStorageConnectionDefIntId_Object=MibTableColumn
cfprStorageConnectionDefIntId=_CfprStorageConnectionDefIntId_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,5),_CfprStorageConnectionDefIntId_Type())
cfprStorageConnectionDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefIntId.setStatus(_A)
_CfprStorageConnectionDefName_Type=SnmpAdminString
_CfprStorageConnectionDefName_Object=MibTableColumn
cfprStorageConnectionDefName=_CfprStorageConnectionDefName_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,6),_CfprStorageConnectionDefName_Type())
cfprStorageConnectionDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefName.setStatus(_A)
_CfprStorageConnectionDefOperState_Type=CfprStorageOperState
_CfprStorageConnectionDefOperState_Object=MibTableColumn
cfprStorageConnectionDefOperState=_CfprStorageConnectionDefOperState_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,7),_CfprStorageConnectionDefOperState_Type())
cfprStorageConnectionDefOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefOperState.setStatus(_A)
_CfprStorageConnectionDefPolicyLevel_Type=Gauge32
_CfprStorageConnectionDefPolicyLevel_Object=MibTableColumn
cfprStorageConnectionDefPolicyLevel=_CfprStorageConnectionDefPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,8),_CfprStorageConnectionDefPolicyLevel_Type())
cfprStorageConnectionDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefPolicyLevel.setStatus(_A)
_CfprStorageConnectionDefPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageConnectionDefPolicyOwner_Object=MibTableColumn
cfprStorageConnectionDefPolicyOwner=_CfprStorageConnectionDefPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,9),_CfprStorageConnectionDefPolicyOwner_Type())
cfprStorageConnectionDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefPolicyOwner.setStatus(_A)
_CfprStorageConnectionDefZoningType_Type=CfprStorageFcZoningType
_CfprStorageConnectionDefZoningType_Object=MibTableColumn
cfprStorageConnectionDefZoningType=_CfprStorageConnectionDefZoningType_Object((1,3,6,1,4,1,9,9,826,1,74,2,1,10),_CfprStorageConnectionDefZoningType_Type())
cfprStorageConnectionDefZoningType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionDefZoningType.setStatus(_A)
_CfprStorageConnectionPolicyTable_Object=MibTable
cfprStorageConnectionPolicyTable=_CfprStorageConnectionPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,74,3))
if mibBuilder.loadTexts:cfprStorageConnectionPolicyTable.setStatus(_A)
_CfprStorageConnectionPolicyEntry_Object=MibTableRow
cfprStorageConnectionPolicyEntry=_CfprStorageConnectionPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,74,3,1))
cfprStorageConnectionPolicyEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprStorageConnectionPolicyEntry.setStatus(_A)
_CfprStorageConnectionPolicyInstanceId_Type=CfprManagedObjectId
_CfprStorageConnectionPolicyInstanceId_Object=MibTableColumn
cfprStorageConnectionPolicyInstanceId=_CfprStorageConnectionPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,1),_CfprStorageConnectionPolicyInstanceId_Type())
cfprStorageConnectionPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyInstanceId.setStatus(_A)
_CfprStorageConnectionPolicyDn_Type=CfprManagedObjectDn
_CfprStorageConnectionPolicyDn_Object=MibTableColumn
cfprStorageConnectionPolicyDn=_CfprStorageConnectionPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,2),_CfprStorageConnectionPolicyDn_Type())
cfprStorageConnectionPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyDn.setStatus(_A)
_CfprStorageConnectionPolicyRn_Type=SnmpAdminString
_CfprStorageConnectionPolicyRn_Object=MibTableColumn
cfprStorageConnectionPolicyRn=_CfprStorageConnectionPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,3),_CfprStorageConnectionPolicyRn_Type())
cfprStorageConnectionPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyRn.setStatus(_A)
_CfprStorageConnectionPolicyDescr_Type=SnmpAdminString
_CfprStorageConnectionPolicyDescr_Object=MibTableColumn
cfprStorageConnectionPolicyDescr=_CfprStorageConnectionPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,4),_CfprStorageConnectionPolicyDescr_Type())
cfprStorageConnectionPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyDescr.setStatus(_A)
_CfprStorageConnectionPolicyIntId_Type=SnmpAdminString
_CfprStorageConnectionPolicyIntId_Object=MibTableColumn
cfprStorageConnectionPolicyIntId=_CfprStorageConnectionPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,5),_CfprStorageConnectionPolicyIntId_Type())
cfprStorageConnectionPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyIntId.setStatus(_A)
_CfprStorageConnectionPolicyName_Type=SnmpAdminString
_CfprStorageConnectionPolicyName_Object=MibTableColumn
cfprStorageConnectionPolicyName=_CfprStorageConnectionPolicyName_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,6),_CfprStorageConnectionPolicyName_Type())
cfprStorageConnectionPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyName.setStatus(_A)
_CfprStorageConnectionPolicyOperState_Type=CfprStorageOperState
_CfprStorageConnectionPolicyOperState_Object=MibTableColumn
cfprStorageConnectionPolicyOperState=_CfprStorageConnectionPolicyOperState_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,7),_CfprStorageConnectionPolicyOperState_Type())
cfprStorageConnectionPolicyOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyOperState.setStatus(_A)
_CfprStorageConnectionPolicyPolicyLevel_Type=Gauge32
_CfprStorageConnectionPolicyPolicyLevel_Object=MibTableColumn
cfprStorageConnectionPolicyPolicyLevel=_CfprStorageConnectionPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,8),_CfprStorageConnectionPolicyPolicyLevel_Type())
cfprStorageConnectionPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyPolicyLevel.setStatus(_A)
_CfprStorageConnectionPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageConnectionPolicyPolicyOwner_Object=MibTableColumn
cfprStorageConnectionPolicyPolicyOwner=_CfprStorageConnectionPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,9),_CfprStorageConnectionPolicyPolicyOwner_Type())
cfprStorageConnectionPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyPolicyOwner.setStatus(_A)
_CfprStorageConnectionPolicyZoningType_Type=CfprStorageFcZoningType
_CfprStorageConnectionPolicyZoningType_Object=MibTableColumn
cfprStorageConnectionPolicyZoningType=_CfprStorageConnectionPolicyZoningType_Object((1,3,6,1,4,1,9,9,826,1,74,3,1,10),_CfprStorageConnectionPolicyZoningType_Type())
cfprStorageConnectionPolicyZoningType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageConnectionPolicyZoningType.setStatus(_A)
_CfprStorageControllerTable_Object=MibTable
cfprStorageControllerTable=_CfprStorageControllerTable_Object((1,3,6,1,4,1,9,9,826,1,74,4))
if mibBuilder.loadTexts:cfprStorageControllerTable.setStatus(_A)
_CfprStorageControllerEntry_Object=MibTableRow
cfprStorageControllerEntry=_CfprStorageControllerEntry_Object((1,3,6,1,4,1,9,9,826,1,74,4,1))
cfprStorageControllerEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprStorageControllerEntry.setStatus(_A)
_CfprStorageControllerInstanceId_Type=CfprManagedObjectId
_CfprStorageControllerInstanceId_Object=MibTableColumn
cfprStorageControllerInstanceId=_CfprStorageControllerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,1),_CfprStorageControllerInstanceId_Type())
cfprStorageControllerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageControllerInstanceId.setStatus(_A)
_CfprStorageControllerDn_Type=CfprManagedObjectDn
_CfprStorageControllerDn_Object=MibTableColumn
cfprStorageControllerDn=_CfprStorageControllerDn_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,2),_CfprStorageControllerDn_Type())
cfprStorageControllerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerDn.setStatus(_A)
_CfprStorageControllerRn_Type=SnmpAdminString
_CfprStorageControllerRn_Object=MibTableColumn
cfprStorageControllerRn=_CfprStorageControllerRn_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,3),_CfprStorageControllerRn_Type())
cfprStorageControllerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerRn.setStatus(_A)
_CfprStorageControllerControllerStatus_Type=CfprStorageControllerStatus
_CfprStorageControllerControllerStatus_Object=MibTableColumn
cfprStorageControllerControllerStatus=_CfprStorageControllerControllerStatus_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,4),_CfprStorageControllerControllerStatus_Type())
cfprStorageControllerControllerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerControllerStatus.setStatus(_A)
_CfprStorageControllerDeviceRaidSupport_Type=SnmpAdminString
_CfprStorageControllerDeviceRaidSupport_Object=MibTableColumn
cfprStorageControllerDeviceRaidSupport=_CfprStorageControllerDeviceRaidSupport_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,5),_CfprStorageControllerDeviceRaidSupport_Type())
cfprStorageControllerDeviceRaidSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerDeviceRaidSupport.setStatus(_A)
_CfprStorageControllerFaultMonitoring_Type=CfprStorageControllerFaultMonitoring
_CfprStorageControllerFaultMonitoring_Object=MibTableColumn
cfprStorageControllerFaultMonitoring=_CfprStorageControllerFaultMonitoring_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,6),_CfprStorageControllerFaultMonitoring_Type())
cfprStorageControllerFaultMonitoring.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerFaultMonitoring.setStatus(_A)
_CfprStorageControllerHwRevision_Type=SnmpAdminString
_CfprStorageControllerHwRevision_Object=MibTableColumn
cfprStorageControllerHwRevision=_CfprStorageControllerHwRevision_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,7),_CfprStorageControllerHwRevision_Type())
cfprStorageControllerHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerHwRevision.setStatus(_A)
_CfprStorageControllerId_Type=CfprStorageControllerId
_CfprStorageControllerId_Object=MibTableColumn
cfprStorageControllerId=_CfprStorageControllerId_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,8),_CfprStorageControllerId_Type())
cfprStorageControllerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerId.setStatus(_A)
_CfprStorageControllerLc_Type=CfprFsmLifecycle
_CfprStorageControllerLc_Object=MibTableColumn
cfprStorageControllerLc=_CfprStorageControllerLc_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,9),_CfprStorageControllerLc_Type())
cfprStorageControllerLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerLc.setStatus(_A)
_CfprStorageControllerLocationDn_Type=SnmpAdminString
_CfprStorageControllerLocationDn_Object=MibTableColumn
cfprStorageControllerLocationDn=_CfprStorageControllerLocationDn_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,10),_CfprStorageControllerLocationDn_Type())
cfprStorageControllerLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerLocationDn.setStatus(_A)
_CfprStorageControllerModel_Type=SnmpAdminString
_CfprStorageControllerModel_Object=MibTableColumn
cfprStorageControllerModel=_CfprStorageControllerModel_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,11),_CfprStorageControllerModel_Type())
cfprStorageControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerModel.setStatus(_A)
_CfprStorageControllerOobControllerId_Type=Gauge32
_CfprStorageControllerOobControllerId_Object=MibTableColumn
cfprStorageControllerOobControllerId=_CfprStorageControllerOobControllerId_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,12),_CfprStorageControllerOobControllerId_Type())
cfprStorageControllerOobControllerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerOobControllerId.setStatus(_A)
_CfprStorageControllerOobInterfaceSupported_Type=TruthValue
_CfprStorageControllerOobInterfaceSupported_Object=MibTableColumn
cfprStorageControllerOobInterfaceSupported=_CfprStorageControllerOobInterfaceSupported_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,13),_CfprStorageControllerOobInterfaceSupported_Type())
cfprStorageControllerOobInterfaceSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerOobInterfaceSupported.setStatus(_A)
_CfprStorageControllerOperQualifierReason_Type=SnmpAdminString
_CfprStorageControllerOperQualifierReason_Object=MibTableColumn
cfprStorageControllerOperQualifierReason=_CfprStorageControllerOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,14),_CfprStorageControllerOperQualifierReason_Type())
cfprStorageControllerOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerOperQualifierReason.setStatus(_A)
_CfprStorageControllerOperState_Type=CfprEquipmentOperability
_CfprStorageControllerOperState_Object=MibTableColumn
cfprStorageControllerOperState=_CfprStorageControllerOperState_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,15),_CfprStorageControllerOperState_Type())
cfprStorageControllerOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerOperState.setStatus(_A)
_CfprStorageControllerOperability_Type=CfprEquipmentOperability
_CfprStorageControllerOperability_Object=MibTableColumn
cfprStorageControllerOperability=_CfprStorageControllerOperability_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,16),_CfprStorageControllerOperability_Type())
cfprStorageControllerOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerOperability.setStatus(_A)
_CfprStorageControllerPartNumber_Type=SnmpAdminString
_CfprStorageControllerPartNumber_Object=MibTableColumn
cfprStorageControllerPartNumber=_CfprStorageControllerPartNumber_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,17),_CfprStorageControllerPartNumber_Type())
cfprStorageControllerPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPartNumber.setStatus(_A)
_CfprStorageControllerPciAddr_Type=SnmpAdminString
_CfprStorageControllerPciAddr_Object=MibTableColumn
cfprStorageControllerPciAddr=_CfprStorageControllerPciAddr_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,18),_CfprStorageControllerPciAddr_Type())
cfprStorageControllerPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPciAddr.setStatus(_A)
_CfprStorageControllerPciSlot_Type=SnmpAdminString
_CfprStorageControllerPciSlot_Object=MibTableColumn
cfprStorageControllerPciSlot=_CfprStorageControllerPciSlot_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,19),_CfprStorageControllerPciSlot_Type())
cfprStorageControllerPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPciSlot.setStatus(_A)
_CfprStorageControllerPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageControllerPerf_Object=MibTableColumn
cfprStorageControllerPerf=_CfprStorageControllerPerf_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,20),_CfprStorageControllerPerf_Type())
cfprStorageControllerPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPerf.setStatus(_A)
_CfprStorageControllerPower_Type=CfprEquipmentPowerState
_CfprStorageControllerPower_Object=MibTableColumn
cfprStorageControllerPower=_CfprStorageControllerPower_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,21),_CfprStorageControllerPower_Type())
cfprStorageControllerPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPower.setStatus(_A)
_CfprStorageControllerPresence_Type=CfprEquipmentPresence
_CfprStorageControllerPresence_Object=MibTableColumn
cfprStorageControllerPresence=_CfprStorageControllerPresence_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,22),_CfprStorageControllerPresence_Type())
cfprStorageControllerPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerPresence.setStatus(_A)
_CfprStorageControllerRaidSupport_Type=SnmpAdminString
_CfprStorageControllerRaidSupport_Object=MibTableColumn
cfprStorageControllerRaidSupport=_CfprStorageControllerRaidSupport_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,23),_CfprStorageControllerRaidSupport_Type())
cfprStorageControllerRaidSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerRaidSupport.setStatus(_A)
_CfprStorageControllerRebuildRate_Type=Gauge32
_CfprStorageControllerRebuildRate_Object=MibTableColumn
cfprStorageControllerRebuildRate=_CfprStorageControllerRebuildRate_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,24),_CfprStorageControllerRebuildRate_Type())
cfprStorageControllerRebuildRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerRebuildRate.setStatus(_A)
_CfprStorageControllerRevision_Type=SnmpAdminString
_CfprStorageControllerRevision_Object=MibTableColumn
cfprStorageControllerRevision=_CfprStorageControllerRevision_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,25),_CfprStorageControllerRevision_Type())
cfprStorageControllerRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerRevision.setStatus(_A)
_CfprStorageControllerSerial_Type=SnmpAdminString
_CfprStorageControllerSerial_Object=MibTableColumn
cfprStorageControllerSerial=_CfprStorageControllerSerial_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,26),_CfprStorageControllerSerial_Type())
cfprStorageControllerSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerSerial.setStatus(_A)
_CfprStorageControllerThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageControllerThermal_Object=MibTableColumn
cfprStorageControllerThermal=_CfprStorageControllerThermal_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,27),_CfprStorageControllerThermal_Type())
cfprStorageControllerThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerThermal.setStatus(_A)
_CfprStorageControllerType_Type=CfprStorageControllerType
_CfprStorageControllerType_Object=MibTableColumn
cfprStorageControllerType=_CfprStorageControllerType_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,28),_CfprStorageControllerType_Type())
cfprStorageControllerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerType.setStatus(_A)
_CfprStorageControllerVendor_Type=SnmpAdminString
_CfprStorageControllerVendor_Object=MibTableColumn
cfprStorageControllerVendor=_CfprStorageControllerVendor_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,29),_CfprStorageControllerVendor_Type())
cfprStorageControllerVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerVendor.setStatus(_A)
_CfprStorageControllerVid_Type=SnmpAdminString
_CfprStorageControllerVid_Object=MibTableColumn
cfprStorageControllerVid=_CfprStorageControllerVid_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,30),_CfprStorageControllerVid_Type())
cfprStorageControllerVid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerVid.setStatus(_A)
_CfprStorageControllerVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageControllerVoltage_Object=MibTableColumn
cfprStorageControllerVoltage=_CfprStorageControllerVoltage_Object((1,3,6,1,4,1,9,9,826,1,74,4,1,31),_CfprStorageControllerVoltage_Type())
cfprStorageControllerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageControllerVoltage.setStatus(_A)
_CfprStorageDomainEpTable_Object=MibTable
cfprStorageDomainEpTable=_CfprStorageDomainEpTable_Object((1,3,6,1,4,1,9,9,826,1,74,5))
if mibBuilder.loadTexts:cfprStorageDomainEpTable.setStatus(_A)
_CfprStorageDomainEpEntry_Object=MibTableRow
cfprStorageDomainEpEntry=_CfprStorageDomainEpEntry_Object((1,3,6,1,4,1,9,9,826,1,74,5,1))
cfprStorageDomainEpEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprStorageDomainEpEntry.setStatus(_A)
_CfprStorageDomainEpInstanceId_Type=CfprManagedObjectId
_CfprStorageDomainEpInstanceId_Object=MibTableColumn
cfprStorageDomainEpInstanceId=_CfprStorageDomainEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,5,1,1),_CfprStorageDomainEpInstanceId_Type())
cfprStorageDomainEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageDomainEpInstanceId.setStatus(_A)
_CfprStorageDomainEpDn_Type=CfprManagedObjectDn
_CfprStorageDomainEpDn_Object=MibTableColumn
cfprStorageDomainEpDn=_CfprStorageDomainEpDn_Object((1,3,6,1,4,1,9,9,826,1,74,5,1,2),_CfprStorageDomainEpDn_Type())
cfprStorageDomainEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDomainEpDn.setStatus(_A)
_CfprStorageDomainEpRn_Type=SnmpAdminString
_CfprStorageDomainEpRn_Object=MibTableColumn
cfprStorageDomainEpRn=_CfprStorageDomainEpRn_Object((1,3,6,1,4,1,9,9,826,1,74,5,1,3),_CfprStorageDomainEpRn_Type())
cfprStorageDomainEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDomainEpRn.setStatus(_A)
_CfprStorageDriveTable_Object=MibTable
cfprStorageDriveTable=_CfprStorageDriveTable_Object((1,3,6,1,4,1,9,9,826,1,74,6))
if mibBuilder.loadTexts:cfprStorageDriveTable.setStatus(_A)
_CfprStorageDriveEntry_Object=MibTableRow
cfprStorageDriveEntry=_CfprStorageDriveEntry_Object((1,3,6,1,4,1,9,9,826,1,74,6,1))
cfprStorageDriveEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprStorageDriveEntry.setStatus(_A)
_CfprStorageDriveInstanceId_Type=CfprManagedObjectId
_CfprStorageDriveInstanceId_Object=MibTableColumn
cfprStorageDriveInstanceId=_CfprStorageDriveInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,1),_CfprStorageDriveInstanceId_Type())
cfprStorageDriveInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageDriveInstanceId.setStatus(_A)
_CfprStorageDriveDn_Type=CfprManagedObjectDn
_CfprStorageDriveDn_Object=MibTableColumn
cfprStorageDriveDn=_CfprStorageDriveDn_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,2),_CfprStorageDriveDn_Type())
cfprStorageDriveDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveDn.setStatus(_A)
_CfprStorageDriveRn_Type=SnmpAdminString
_CfprStorageDriveRn_Object=MibTableColumn
cfprStorageDriveRn=_CfprStorageDriveRn_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,3),_CfprStorageDriveRn_Type())
cfprStorageDriveRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveRn.setStatus(_A)
_CfprStorageDriveId_Type=Gauge32
_CfprStorageDriveId_Object=MibTableColumn
cfprStorageDriveId=_CfprStorageDriveId_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,4),_CfprStorageDriveId_Type())
cfprStorageDriveId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveId.setStatus(_A)
_CfprStorageDriveModel_Type=SnmpAdminString
_CfprStorageDriveModel_Object=MibTableColumn
cfprStorageDriveModel=_CfprStorageDriveModel_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,5),_CfprStorageDriveModel_Type())
cfprStorageDriveModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveModel.setStatus(_A)
_CfprStorageDrivePciAddr_Type=SnmpAdminString
_CfprStorageDrivePciAddr_Object=MibTableColumn
cfprStorageDrivePciAddr=_CfprStorageDrivePciAddr_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,6),_CfprStorageDrivePciAddr_Type())
cfprStorageDrivePciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDrivePciAddr.setStatus(_A)
_CfprStorageDriveRevision_Type=SnmpAdminString
_CfprStorageDriveRevision_Object=MibTableColumn
cfprStorageDriveRevision=_CfprStorageDriveRevision_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,7),_CfprStorageDriveRevision_Type())
cfprStorageDriveRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveRevision.setStatus(_A)
_CfprStorageDriveSerial_Type=SnmpAdminString
_CfprStorageDriveSerial_Object=MibTableColumn
cfprStorageDriveSerial=_CfprStorageDriveSerial_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,8),_CfprStorageDriveSerial_Type())
cfprStorageDriveSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveSerial.setStatus(_A)
_CfprStorageDriveVendor_Type=SnmpAdminString
_CfprStorageDriveVendor_Object=MibTableColumn
cfprStorageDriveVendor=_CfprStorageDriveVendor_Object((1,3,6,1,4,1,9,9,826,1,74,6,1,9),_CfprStorageDriveVendor_Type())
cfprStorageDriveVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageDriveVendor.setStatus(_A)
_CfprStorageEnclosureTable_Object=MibTable
cfprStorageEnclosureTable=_CfprStorageEnclosureTable_Object((1,3,6,1,4,1,9,9,826,1,74,7))
if mibBuilder.loadTexts:cfprStorageEnclosureTable.setStatus(_A)
_CfprStorageEnclosureEntry_Object=MibTableRow
cfprStorageEnclosureEntry=_CfprStorageEnclosureEntry_Object((1,3,6,1,4,1,9,9,826,1,74,7,1))
cfprStorageEnclosureEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprStorageEnclosureEntry.setStatus(_A)
_CfprStorageEnclosureInstanceId_Type=CfprManagedObjectId
_CfprStorageEnclosureInstanceId_Object=MibTableColumn
cfprStorageEnclosureInstanceId=_CfprStorageEnclosureInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,1),_CfprStorageEnclosureInstanceId_Type())
cfprStorageEnclosureInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageEnclosureInstanceId.setStatus(_A)
_CfprStorageEnclosureDn_Type=CfprManagedObjectDn
_CfprStorageEnclosureDn_Object=MibTableColumn
cfprStorageEnclosureDn=_CfprStorageEnclosureDn_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,2),_CfprStorageEnclosureDn_Type())
cfprStorageEnclosureDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureDn.setStatus(_A)
_CfprStorageEnclosureRn_Type=SnmpAdminString
_CfprStorageEnclosureRn_Object=MibTableColumn
cfprStorageEnclosureRn=_CfprStorageEnclosureRn_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,3),_CfprStorageEnclosureRn_Type())
cfprStorageEnclosureRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureRn.setStatus(_A)
_CfprStorageEnclosureId_Type=Gauge32
_CfprStorageEnclosureId_Object=MibTableColumn
cfprStorageEnclosureId=_CfprStorageEnclosureId_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,4),_CfprStorageEnclosureId_Type())
cfprStorageEnclosureId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureId.setStatus(_A)
_CfprStorageEnclosureLc_Type=CfprFsmLifecycle
_CfprStorageEnclosureLc_Object=MibTableColumn
cfprStorageEnclosureLc=_CfprStorageEnclosureLc_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,5),_CfprStorageEnclosureLc_Type())
cfprStorageEnclosureLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureLc.setStatus(_A)
_CfprStorageEnclosureModel_Type=SnmpAdminString
_CfprStorageEnclosureModel_Object=MibTableColumn
cfprStorageEnclosureModel=_CfprStorageEnclosureModel_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,6),_CfprStorageEnclosureModel_Type())
cfprStorageEnclosureModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureModel.setStatus(_A)
_CfprStorageEnclosureNumSlots_Type=Gauge32
_CfprStorageEnclosureNumSlots_Object=MibTableColumn
cfprStorageEnclosureNumSlots=_CfprStorageEnclosureNumSlots_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,7),_CfprStorageEnclosureNumSlots_Type())
cfprStorageEnclosureNumSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureNumSlots.setStatus(_A)
_CfprStorageEnclosureRevision_Type=SnmpAdminString
_CfprStorageEnclosureRevision_Object=MibTableColumn
cfprStorageEnclosureRevision=_CfprStorageEnclosureRevision_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,8),_CfprStorageEnclosureRevision_Type())
cfprStorageEnclosureRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureRevision.setStatus(_A)
_CfprStorageEnclosureSerial_Type=SnmpAdminString
_CfprStorageEnclosureSerial_Object=MibTableColumn
cfprStorageEnclosureSerial=_CfprStorageEnclosureSerial_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,9),_CfprStorageEnclosureSerial_Type())
cfprStorageEnclosureSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureSerial.setStatus(_A)
_CfprStorageEnclosureVendor_Type=SnmpAdminString
_CfprStorageEnclosureVendor_Object=MibTableColumn
cfprStorageEnclosureVendor=_CfprStorageEnclosureVendor_Object((1,3,6,1,4,1,9,9,826,1,74,7,1,10),_CfprStorageEnclosureVendor_Type())
cfprStorageEnclosureVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEnclosureVendor.setStatus(_A)
_CfprStorageEpUserTable_Object=MibTable
cfprStorageEpUserTable=_CfprStorageEpUserTable_Object((1,3,6,1,4,1,9,9,826,1,74,8))
if mibBuilder.loadTexts:cfprStorageEpUserTable.setStatus(_A)
_CfprStorageEpUserEntry_Object=MibTableRow
cfprStorageEpUserEntry=_CfprStorageEpUserEntry_Object((1,3,6,1,4,1,9,9,826,1,74,8,1))
cfprStorageEpUserEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprStorageEpUserEntry.setStatus(_A)
_CfprStorageEpUserInstanceId_Type=CfprManagedObjectId
_CfprStorageEpUserInstanceId_Object=MibTableColumn
cfprStorageEpUserInstanceId=_CfprStorageEpUserInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,1),_CfprStorageEpUserInstanceId_Type())
cfprStorageEpUserInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageEpUserInstanceId.setStatus(_A)
_CfprStorageEpUserDn_Type=CfprManagedObjectDn
_CfprStorageEpUserDn_Object=MibTableColumn
cfprStorageEpUserDn=_CfprStorageEpUserDn_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,2),_CfprStorageEpUserDn_Type())
cfprStorageEpUserDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserDn.setStatus(_A)
_CfprStorageEpUserRn_Type=SnmpAdminString
_CfprStorageEpUserRn_Object=MibTableColumn
cfprStorageEpUserRn=_CfprStorageEpUserRn_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,3),_CfprStorageEpUserRn_Type())
cfprStorageEpUserRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserRn.setStatus(_A)
_CfprStorageEpUserConfigState_Type=CfprAaaConfigState
_CfprStorageEpUserConfigState_Object=MibTableColumn
cfprStorageEpUserConfigState=_CfprStorageEpUserConfigState_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,4),_CfprStorageEpUserConfigState_Type())
cfprStorageEpUserConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserConfigState.setStatus(_A)
_CfprStorageEpUserConfigStatusMessage_Type=SnmpAdminString
_CfprStorageEpUserConfigStatusMessage_Object=MibTableColumn
cfprStorageEpUserConfigStatusMessage=_CfprStorageEpUserConfigStatusMessage_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,5),_CfprStorageEpUserConfigStatusMessage_Type())
cfprStorageEpUserConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserConfigStatusMessage.setStatus(_A)
_CfprStorageEpUserDescr_Type=SnmpAdminString
_CfprStorageEpUserDescr_Object=MibTableColumn
cfprStorageEpUserDescr=_CfprStorageEpUserDescr_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,6),_CfprStorageEpUserDescr_Type())
cfprStorageEpUserDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserDescr.setStatus(_A)
_CfprStorageEpUserDomain_Type=SnmpAdminString
_CfprStorageEpUserDomain_Object=MibTableColumn
cfprStorageEpUserDomain=_CfprStorageEpUserDomain_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,7),_CfprStorageEpUserDomain_Type())
cfprStorageEpUserDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserDomain.setStatus(_A)
_CfprStorageEpUserName_Type=SnmpAdminString
_CfprStorageEpUserName_Object=MibTableColumn
cfprStorageEpUserName=_CfprStorageEpUserName_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,8),_CfprStorageEpUserName_Type())
cfprStorageEpUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserName.setStatus(_A)
_CfprStorageEpUserPriv_Type=CfprStorageEpAccess
_CfprStorageEpUserPriv_Object=MibTableColumn
cfprStorageEpUserPriv=_CfprStorageEpUserPriv_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,9),_CfprStorageEpUserPriv_Type())
cfprStorageEpUserPriv.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserPriv.setStatus(_A)
_CfprStorageEpUserPwd_Type=SnmpAdminString
_CfprStorageEpUserPwd_Object=MibTableColumn
cfprStorageEpUserPwd=_CfprStorageEpUserPwd_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,10),_CfprStorageEpUserPwd_Type())
cfprStorageEpUserPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserPwd.setStatus(_A)
_CfprStorageEpUserPwdSet_Type=TruthValue
_CfprStorageEpUserPwdSet_Object=MibTableColumn
cfprStorageEpUserPwdSet=_CfprStorageEpUserPwdSet_Object((1,3,6,1,4,1,9,9,826,1,74,8,1,11),_CfprStorageEpUserPwdSet_Type())
cfprStorageEpUserPwdSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEpUserPwdSet.setStatus(_A)
_CfprStorageEtherIfTable_Object=MibTable
cfprStorageEtherIfTable=_CfprStorageEtherIfTable_Object((1,3,6,1,4,1,9,9,826,1,74,9))
if mibBuilder.loadTexts:cfprStorageEtherIfTable.setStatus(_A)
_CfprStorageEtherIfEntry_Object=MibTableRow
cfprStorageEtherIfEntry=_CfprStorageEtherIfEntry_Object((1,3,6,1,4,1,9,9,826,1,74,9,1))
cfprStorageEtherIfEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprStorageEtherIfEntry.setStatus(_A)
_CfprStorageEtherIfInstanceId_Type=CfprManagedObjectId
_CfprStorageEtherIfInstanceId_Object=MibTableColumn
cfprStorageEtherIfInstanceId=_CfprStorageEtherIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,9,1,1),_CfprStorageEtherIfInstanceId_Type())
cfprStorageEtherIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageEtherIfInstanceId.setStatus(_A)
_CfprStorageEtherIfDn_Type=CfprManagedObjectDn
_CfprStorageEtherIfDn_Object=MibTableColumn
cfprStorageEtherIfDn=_CfprStorageEtherIfDn_Object((1,3,6,1,4,1,9,9,826,1,74,9,1,2),_CfprStorageEtherIfDn_Type())
cfprStorageEtherIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEtherIfDn.setStatus(_A)
_CfprStorageEtherIfRn_Type=SnmpAdminString
_CfprStorageEtherIfRn_Object=MibTableColumn
cfprStorageEtherIfRn=_CfprStorageEtherIfRn_Object((1,3,6,1,4,1,9,9,826,1,74,9,1,3),_CfprStorageEtherIfRn_Type())
cfprStorageEtherIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEtherIfRn.setStatus(_A)
_CfprStorageEtherIfName_Type=SnmpAdminString
_CfprStorageEtherIfName_Object=MibTableColumn
cfprStorageEtherIfName=_CfprStorageEtherIfName_Object((1,3,6,1,4,1,9,9,826,1,74,9,1,4),_CfprStorageEtherIfName_Type())
cfprStorageEtherIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEtherIfName.setStatus(_A)
_CfprStorageEtherIfVlanType_Type=CfprStorageEtherIfVlanType
_CfprStorageEtherIfVlanType_Object=MibTableColumn
cfprStorageEtherIfVlanType=_CfprStorageEtherIfVlanType_Object((1,3,6,1,4,1,9,9,826,1,74,9,1,5),_CfprStorageEtherIfVlanType_Type())
cfprStorageEtherIfVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageEtherIfVlanType.setStatus(_A)
_CfprStorageFcIfTable_Object=MibTable
cfprStorageFcIfTable=_CfprStorageFcIfTable_Object((1,3,6,1,4,1,9,9,826,1,74,10))
if mibBuilder.loadTexts:cfprStorageFcIfTable.setStatus(_A)
_CfprStorageFcIfEntry_Object=MibTableRow
cfprStorageFcIfEntry=_CfprStorageFcIfEntry_Object((1,3,6,1,4,1,9,9,826,1,74,10,1))
cfprStorageFcIfEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprStorageFcIfEntry.setStatus(_A)
_CfprStorageFcIfInstanceId_Type=CfprManagedObjectId
_CfprStorageFcIfInstanceId_Object=MibTableColumn
cfprStorageFcIfInstanceId=_CfprStorageFcIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,10,1,1),_CfprStorageFcIfInstanceId_Type())
cfprStorageFcIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFcIfInstanceId.setStatus(_A)
_CfprStorageFcIfDn_Type=CfprManagedObjectDn
_CfprStorageFcIfDn_Object=MibTableColumn
cfprStorageFcIfDn=_CfprStorageFcIfDn_Object((1,3,6,1,4,1,9,9,826,1,74,10,1,2),_CfprStorageFcIfDn_Type())
cfprStorageFcIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcIfDn.setStatus(_A)
_CfprStorageFcIfRn_Type=SnmpAdminString
_CfprStorageFcIfRn_Object=MibTableColumn
cfprStorageFcIfRn=_CfprStorageFcIfRn_Object((1,3,6,1,4,1,9,9,826,1,74,10,1,3),_CfprStorageFcIfRn_Type())
cfprStorageFcIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcIfRn.setStatus(_A)
_CfprStorageFcIfName_Type=SnmpAdminString
_CfprStorageFcIfName_Object=MibTableColumn
cfprStorageFcIfName=_CfprStorageFcIfName_Object((1,3,6,1,4,1,9,9,826,1,74,10,1,4),_CfprStorageFcIfName_Type())
cfprStorageFcIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcIfName.setStatus(_A)
_CfprStorageFcTargetEpTable_Object=MibTable
cfprStorageFcTargetEpTable=_CfprStorageFcTargetEpTable_Object((1,3,6,1,4,1,9,9,826,1,74,11))
if mibBuilder.loadTexts:cfprStorageFcTargetEpTable.setStatus(_A)
_CfprStorageFcTargetEpEntry_Object=MibTableRow
cfprStorageFcTargetEpEntry=_CfprStorageFcTargetEpEntry_Object((1,3,6,1,4,1,9,9,826,1,74,11,1))
cfprStorageFcTargetEpEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprStorageFcTargetEpEntry.setStatus(_A)
_CfprStorageFcTargetEpInstanceId_Type=CfprManagedObjectId
_CfprStorageFcTargetEpInstanceId_Object=MibTableColumn
cfprStorageFcTargetEpInstanceId=_CfprStorageFcTargetEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,1),_CfprStorageFcTargetEpInstanceId_Type())
cfprStorageFcTargetEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFcTargetEpInstanceId.setStatus(_A)
_CfprStorageFcTargetEpDn_Type=CfprManagedObjectDn
_CfprStorageFcTargetEpDn_Object=MibTableColumn
cfprStorageFcTargetEpDn=_CfprStorageFcTargetEpDn_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,2),_CfprStorageFcTargetEpDn_Type())
cfprStorageFcTargetEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetEpDn.setStatus(_A)
_CfprStorageFcTargetEpRn_Type=SnmpAdminString
_CfprStorageFcTargetEpRn_Object=MibTableColumn
cfprStorageFcTargetEpRn=_CfprStorageFcTargetEpRn_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,3),_CfprStorageFcTargetEpRn_Type())
cfprStorageFcTargetEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetEpRn.setStatus(_A)
_CfprStorageFcTargetEpDescr_Type=SnmpAdminString
_CfprStorageFcTargetEpDescr_Object=MibTableColumn
cfprStorageFcTargetEpDescr=_CfprStorageFcTargetEpDescr_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,4),_CfprStorageFcTargetEpDescr_Type())
cfprStorageFcTargetEpDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetEpDescr.setStatus(_A)
_CfprStorageFcTargetEpPath_Type=CfprStorageTargetPath
_CfprStorageFcTargetEpPath_Object=MibTableColumn
cfprStorageFcTargetEpPath=_CfprStorageFcTargetEpPath_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,5),_CfprStorageFcTargetEpPath_Type())
cfprStorageFcTargetEpPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetEpPath.setStatus(_A)
_CfprStorageFcTargetEpTargetwwpn_Type=SnmpAdminString
_CfprStorageFcTargetEpTargetwwpn_Object=MibTableColumn
cfprStorageFcTargetEpTargetwwpn=_CfprStorageFcTargetEpTargetwwpn_Object((1,3,6,1,4,1,9,9,826,1,74,11,1,6),_CfprStorageFcTargetEpTargetwwpn_Type())
cfprStorageFcTargetEpTargetwwpn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetEpTargetwwpn.setStatus(_A)
_CfprStorageFcTargetIfTable_Object=MibTable
cfprStorageFcTargetIfTable=_CfprStorageFcTargetIfTable_Object((1,3,6,1,4,1,9,9,826,1,74,12))
if mibBuilder.loadTexts:cfprStorageFcTargetIfTable.setStatus(_A)
_CfprStorageFcTargetIfEntry_Object=MibTableRow
cfprStorageFcTargetIfEntry=_CfprStorageFcTargetIfEntry_Object((1,3,6,1,4,1,9,9,826,1,74,12,1))
cfprStorageFcTargetIfEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprStorageFcTargetIfEntry.setStatus(_A)
_CfprStorageFcTargetIfInstanceId_Type=CfprManagedObjectId
_CfprStorageFcTargetIfInstanceId_Object=MibTableColumn
cfprStorageFcTargetIfInstanceId=_CfprStorageFcTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,12,1,1),_CfprStorageFcTargetIfInstanceId_Type())
cfprStorageFcTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFcTargetIfInstanceId.setStatus(_A)
_CfprStorageFcTargetIfDn_Type=CfprManagedObjectDn
_CfprStorageFcTargetIfDn_Object=MibTableColumn
cfprStorageFcTargetIfDn=_CfprStorageFcTargetIfDn_Object((1,3,6,1,4,1,9,9,826,1,74,12,1,2),_CfprStorageFcTargetIfDn_Type())
cfprStorageFcTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetIfDn.setStatus(_A)
_CfprStorageFcTargetIfRn_Type=SnmpAdminString
_CfprStorageFcTargetIfRn_Object=MibTableColumn
cfprStorageFcTargetIfRn=_CfprStorageFcTargetIfRn_Object((1,3,6,1,4,1,9,9,826,1,74,12,1,3),_CfprStorageFcTargetIfRn_Type())
cfprStorageFcTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetIfRn.setStatus(_A)
_CfprStorageFcTargetIfId_Type=Unsigned64
_CfprStorageFcTargetIfId_Object=MibTableColumn
cfprStorageFcTargetIfId=_CfprStorageFcTargetIfId_Object((1,3,6,1,4,1,9,9,826,1,74,12,1,4),_CfprStorageFcTargetIfId_Type())
cfprStorageFcTargetIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetIfId.setStatus(_A)
_CfprStorageFcTargetIfProt_Type=CfprStorageProtocol
_CfprStorageFcTargetIfProt_Object=MibTableColumn
cfprStorageFcTargetIfProt=_CfprStorageFcTargetIfProt_Object((1,3,6,1,4,1,9,9,826,1,74,12,1,5),_CfprStorageFcTargetIfProt_Type())
cfprStorageFcTargetIfProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFcTargetIfProt.setStatus(_A)
_CfprStorageFlexFlashCardTable_Object=MibTable
cfprStorageFlexFlashCardTable=_CfprStorageFlexFlashCardTable_Object((1,3,6,1,4,1,9,9,826,1,74,13))
if mibBuilder.loadTexts:cfprStorageFlexFlashCardTable.setStatus(_A)
_CfprStorageFlexFlashCardEntry_Object=MibTableRow
cfprStorageFlexFlashCardEntry=_CfprStorageFlexFlashCardEntry_Object((1,3,6,1,4,1,9,9,826,1,74,13,1))
cfprStorageFlexFlashCardEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprStorageFlexFlashCardEntry.setStatus(_A)
_CfprStorageFlexFlashCardInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashCardInstanceId_Object=MibTableColumn
cfprStorageFlexFlashCardInstanceId=_CfprStorageFlexFlashCardInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,1),_CfprStorageFlexFlashCardInstanceId_Type())
cfprStorageFlexFlashCardInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardInstanceId.setStatus(_A)
_CfprStorageFlexFlashCardDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashCardDn_Object=MibTableColumn
cfprStorageFlexFlashCardDn=_CfprStorageFlexFlashCardDn_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,2),_CfprStorageFlexFlashCardDn_Type())
cfprStorageFlexFlashCardDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardDn.setStatus(_A)
_CfprStorageFlexFlashCardRn_Type=SnmpAdminString
_CfprStorageFlexFlashCardRn_Object=MibTableColumn
cfprStorageFlexFlashCardRn=_CfprStorageFlexFlashCardRn_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,3),_CfprStorageFlexFlashCardRn_Type())
cfprStorageFlexFlashCardRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardRn.setStatus(_A)
_CfprStorageFlexFlashCardBlockSize_Type=Gauge32
_CfprStorageFlexFlashCardBlockSize_Object=MibTableColumn
cfprStorageFlexFlashCardBlockSize=_CfprStorageFlexFlashCardBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,4),_CfprStorageFlexFlashCardBlockSize_Type())
cfprStorageFlexFlashCardBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardBlockSize.setStatus(_A)
_CfprStorageFlexFlashCardCardHealth_Type=CfprStorageFFCardHealth
_CfprStorageFlexFlashCardCardHealth_Object=MibTableColumn
cfprStorageFlexFlashCardCardHealth=_CfprStorageFlexFlashCardCardHealth_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,5),_CfprStorageFlexFlashCardCardHealth_Type())
cfprStorageFlexFlashCardCardHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardCardHealth.setStatus(_A)
_CfprStorageFlexFlashCardCardMode_Type=CfprStorageFFCardMode
_CfprStorageFlexFlashCardCardMode_Object=MibTableColumn
cfprStorageFlexFlashCardCardMode=_CfprStorageFlexFlashCardCardMode_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,6),_CfprStorageFlexFlashCardCardMode_Type())
cfprStorageFlexFlashCardCardMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardCardMode.setStatus(_A)
_CfprStorageFlexFlashCardCardState_Type=CfprStorageFFCardState
_CfprStorageFlexFlashCardCardState_Object=MibTableColumn
cfprStorageFlexFlashCardCardState=_CfprStorageFlexFlashCardCardState_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,7),_CfprStorageFlexFlashCardCardState_Type())
cfprStorageFlexFlashCardCardState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardCardState.setStatus(_A)
_CfprStorageFlexFlashCardCardSync_Type=CfprStorageFFCardSync
_CfprStorageFlexFlashCardCardSync_Object=MibTableColumn
cfprStorageFlexFlashCardCardSync=_CfprStorageFlexFlashCardCardSync_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,8),_CfprStorageFlexFlashCardCardSync_Type())
cfprStorageFlexFlashCardCardSync.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardCardSync.setStatus(_A)
_CfprStorageFlexFlashCardCardType_Type=SnmpAdminString
_CfprStorageFlexFlashCardCardType_Object=MibTableColumn
cfprStorageFlexFlashCardCardType=_CfprStorageFlexFlashCardCardType_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,9),_CfprStorageFlexFlashCardCardType_Type())
cfprStorageFlexFlashCardCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardCardType.setStatus(_A)
_CfprStorageFlexFlashCardConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageFlexFlashCardConnectionProtocol_Object=MibTableColumn
cfprStorageFlexFlashCardConnectionProtocol=_CfprStorageFlexFlashCardConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,10),_CfprStorageFlexFlashCardConnectionProtocol_Type())
cfprStorageFlexFlashCardConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardConnectionProtocol.setStatus(_A)
_CfprStorageFlexFlashCardControllerIndex_Type=Gauge32
_CfprStorageFlexFlashCardControllerIndex_Object=MibTableColumn
cfprStorageFlexFlashCardControllerIndex=_CfprStorageFlexFlashCardControllerIndex_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,11),_CfprStorageFlexFlashCardControllerIndex_Type())
cfprStorageFlexFlashCardControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardControllerIndex.setStatus(_A)
_CfprStorageFlexFlashCardDrivesEnabled_Type=SnmpAdminString
_CfprStorageFlexFlashCardDrivesEnabled_Object=MibTableColumn
cfprStorageFlexFlashCardDrivesEnabled=_CfprStorageFlexFlashCardDrivesEnabled_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,12),_CfprStorageFlexFlashCardDrivesEnabled_Type())
cfprStorageFlexFlashCardDrivesEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardDrivesEnabled.setStatus(_A)
_CfprStorageFlexFlashCardId_Type=Gauge32
_CfprStorageFlexFlashCardId_Object=MibTableColumn
cfprStorageFlexFlashCardId=_CfprStorageFlexFlashCardId_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,13),_CfprStorageFlexFlashCardId_Type())
cfprStorageFlexFlashCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardId.setStatus(_A)
_CfprStorageFlexFlashCardMfgDate_Type=SnmpAdminString
_CfprStorageFlexFlashCardMfgDate_Object=MibTableColumn
cfprStorageFlexFlashCardMfgDate=_CfprStorageFlexFlashCardMfgDate_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,14),_CfprStorageFlexFlashCardMfgDate_Type())
cfprStorageFlexFlashCardMfgDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardMfgDate.setStatus(_A)
_CfprStorageFlexFlashCardMfgId_Type=SnmpAdminString
_CfprStorageFlexFlashCardMfgId_Object=MibTableColumn
cfprStorageFlexFlashCardMfgId=_CfprStorageFlexFlashCardMfgId_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,15),_CfprStorageFlexFlashCardMfgId_Type())
cfprStorageFlexFlashCardMfgId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardMfgId.setStatus(_A)
_CfprStorageFlexFlashCardModel_Type=SnmpAdminString
_CfprStorageFlexFlashCardModel_Object=MibTableColumn
cfprStorageFlexFlashCardModel=_CfprStorageFlexFlashCardModel_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,16),_CfprStorageFlexFlashCardModel_Type())
cfprStorageFlexFlashCardModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardModel.setStatus(_A)
_CfprStorageFlexFlashCardNumberOfBlocks_Type=Unsigned64
_CfprStorageFlexFlashCardNumberOfBlocks_Object=MibTableColumn
cfprStorageFlexFlashCardNumberOfBlocks=_CfprStorageFlexFlashCardNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,17),_CfprStorageFlexFlashCardNumberOfBlocks_Type())
cfprStorageFlexFlashCardNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardNumberOfBlocks.setStatus(_A)
_CfprStorageFlexFlashCardOemId_Type=SnmpAdminString
_CfprStorageFlexFlashCardOemId_Object=MibTableColumn
cfprStorageFlexFlashCardOemId=_CfprStorageFlexFlashCardOemId_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,18),_CfprStorageFlexFlashCardOemId_Type())
cfprStorageFlexFlashCardOemId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardOemId.setStatus(_A)
_CfprStorageFlexFlashCardOperQualifierReason_Type=SnmpAdminString
_CfprStorageFlexFlashCardOperQualifierReason_Object=MibTableColumn
cfprStorageFlexFlashCardOperQualifierReason=_CfprStorageFlexFlashCardOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,19),_CfprStorageFlexFlashCardOperQualifierReason_Type())
cfprStorageFlexFlashCardOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardOperQualifierReason.setStatus(_A)
_CfprStorageFlexFlashCardOperability_Type=CfprEquipmentOperability
_CfprStorageFlexFlashCardOperability_Object=MibTableColumn
cfprStorageFlexFlashCardOperability=_CfprStorageFlexFlashCardOperability_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,20),_CfprStorageFlexFlashCardOperability_Type())
cfprStorageFlexFlashCardOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardOperability.setStatus(_A)
_CfprStorageFlexFlashCardPartitionCount_Type=Gauge32
_CfprStorageFlexFlashCardPartitionCount_Object=MibTableColumn
cfprStorageFlexFlashCardPartitionCount=_CfprStorageFlexFlashCardPartitionCount_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,21),_CfprStorageFlexFlashCardPartitionCount_Type())
cfprStorageFlexFlashCardPartitionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardPartitionCount.setStatus(_A)
_CfprStorageFlexFlashCardPresence_Type=CfprEquipmentPresence
_CfprStorageFlexFlashCardPresence_Object=MibTableColumn
cfprStorageFlexFlashCardPresence=_CfprStorageFlexFlashCardPresence_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,22),_CfprStorageFlexFlashCardPresence_Type())
cfprStorageFlexFlashCardPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardPresence.setStatus(_A)
_CfprStorageFlexFlashCardReadErrorThreshold_Type=Gauge32
_CfprStorageFlexFlashCardReadErrorThreshold_Object=MibTableColumn
cfprStorageFlexFlashCardReadErrorThreshold=_CfprStorageFlexFlashCardReadErrorThreshold_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,23),_CfprStorageFlexFlashCardReadErrorThreshold_Type())
cfprStorageFlexFlashCardReadErrorThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardReadErrorThreshold.setStatus(_A)
_CfprStorageFlexFlashCardReadIOErrorCount_Type=Gauge32
_CfprStorageFlexFlashCardReadIOErrorCount_Object=MibTableColumn
cfprStorageFlexFlashCardReadIOErrorCount=_CfprStorageFlexFlashCardReadIOErrorCount_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,24),_CfprStorageFlexFlashCardReadIOErrorCount_Type())
cfprStorageFlexFlashCardReadIOErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardReadIOErrorCount.setStatus(_A)
_CfprStorageFlexFlashCardRevision_Type=SnmpAdminString
_CfprStorageFlexFlashCardRevision_Object=MibTableColumn
cfprStorageFlexFlashCardRevision=_CfprStorageFlexFlashCardRevision_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,25),_CfprStorageFlexFlashCardRevision_Type())
cfprStorageFlexFlashCardRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardRevision.setStatus(_A)
_CfprStorageFlexFlashCardSerial_Type=SnmpAdminString
_CfprStorageFlexFlashCardSerial_Object=MibTableColumn
cfprStorageFlexFlashCardSerial=_CfprStorageFlexFlashCardSerial_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,26),_CfprStorageFlexFlashCardSerial_Type())
cfprStorageFlexFlashCardSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardSerial.setStatus(_A)
_CfprStorageFlexFlashCardSignature_Type=SnmpAdminString
_CfprStorageFlexFlashCardSignature_Object=MibTableColumn
cfprStorageFlexFlashCardSignature=_CfprStorageFlexFlashCardSignature_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,27),_CfprStorageFlexFlashCardSignature_Type())
cfprStorageFlexFlashCardSignature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardSignature.setStatus(_A)
_CfprStorageFlexFlashCardSize_Type=Unsigned64
_CfprStorageFlexFlashCardSize_Object=MibTableColumn
cfprStorageFlexFlashCardSize=_CfprStorageFlexFlashCardSize_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,28),_CfprStorageFlexFlashCardSize_Type())
cfprStorageFlexFlashCardSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardSize.setStatus(_A)
_CfprStorageFlexFlashCardSlotNumber_Type=Gauge32
_CfprStorageFlexFlashCardSlotNumber_Object=MibTableColumn
cfprStorageFlexFlashCardSlotNumber=_CfprStorageFlexFlashCardSlotNumber_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,29),_CfprStorageFlexFlashCardSlotNumber_Type())
cfprStorageFlexFlashCardSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardSlotNumber.setStatus(_A)
_CfprStorageFlexFlashCardVendor_Type=SnmpAdminString
_CfprStorageFlexFlashCardVendor_Object=MibTableColumn
cfprStorageFlexFlashCardVendor=_CfprStorageFlexFlashCardVendor_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,30),_CfprStorageFlexFlashCardVendor_Type())
cfprStorageFlexFlashCardVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardVendor.setStatus(_A)
_CfprStorageFlexFlashCardWriteEnable_Type=CfprStorageFFCardWriteEnable
_CfprStorageFlexFlashCardWriteEnable_Object=MibTableColumn
cfprStorageFlexFlashCardWriteEnable=_CfprStorageFlexFlashCardWriteEnable_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,31),_CfprStorageFlexFlashCardWriteEnable_Type())
cfprStorageFlexFlashCardWriteEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardWriteEnable.setStatus(_A)
_CfprStorageFlexFlashCardWriteErrorThreshold_Type=Gauge32
_CfprStorageFlexFlashCardWriteErrorThreshold_Object=MibTableColumn
cfprStorageFlexFlashCardWriteErrorThreshold=_CfprStorageFlexFlashCardWriteErrorThreshold_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,32),_CfprStorageFlexFlashCardWriteErrorThreshold_Type())
cfprStorageFlexFlashCardWriteErrorThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardWriteErrorThreshold.setStatus(_A)
_CfprStorageFlexFlashCardWriteIOErrorCount_Type=Gauge32
_CfprStorageFlexFlashCardWriteIOErrorCount_Object=MibTableColumn
cfprStorageFlexFlashCardWriteIOErrorCount=_CfprStorageFlexFlashCardWriteIOErrorCount_Object((1,3,6,1,4,1,9,9,826,1,74,13,1,33),_CfprStorageFlexFlashCardWriteIOErrorCount_Type())
cfprStorageFlexFlashCardWriteIOErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashCardWriteIOErrorCount.setStatus(_A)
_CfprStorageFlexFlashControllerTable_Object=MibTable
cfprStorageFlexFlashControllerTable=_CfprStorageFlexFlashControllerTable_Object((1,3,6,1,4,1,9,9,826,1,74,14))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerTable.setStatus(_A)
_CfprStorageFlexFlashControllerEntry_Object=MibTableRow
cfprStorageFlexFlashControllerEntry=_CfprStorageFlexFlashControllerEntry_Object((1,3,6,1,4,1,9,9,826,1,74,14,1))
cfprStorageFlexFlashControllerEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerEntry.setStatus(_A)
_CfprStorageFlexFlashControllerInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashControllerInstanceId_Object=MibTableColumn
cfprStorageFlexFlashControllerInstanceId=_CfprStorageFlexFlashControllerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,1),_CfprStorageFlexFlashControllerInstanceId_Type())
cfprStorageFlexFlashControllerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerInstanceId.setStatus(_A)
_CfprStorageFlexFlashControllerDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashControllerDn_Object=MibTableColumn
cfprStorageFlexFlashControllerDn=_CfprStorageFlexFlashControllerDn_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,2),_CfprStorageFlexFlashControllerDn_Type())
cfprStorageFlexFlashControllerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerDn.setStatus(_A)
_CfprStorageFlexFlashControllerRn_Type=SnmpAdminString
_CfprStorageFlexFlashControllerRn_Object=MibTableColumn
cfprStorageFlexFlashControllerRn=_CfprStorageFlexFlashControllerRn_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,3),_CfprStorageFlexFlashControllerRn_Type())
cfprStorageFlexFlashControllerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerRn.setStatus(_A)
_CfprStorageFlexFlashControllerAdminSlotNumber_Type=CfprStorageFFSlotENUM
_CfprStorageFlexFlashControllerAdminSlotNumber_Object=MibTableColumn
cfprStorageFlexFlashControllerAdminSlotNumber=_CfprStorageFlexFlashControllerAdminSlotNumber_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,4),_CfprStorageFlexFlashControllerAdminSlotNumber_Type())
cfprStorageFlexFlashControllerAdminSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerAdminSlotNumber.setStatus(_A)
_CfprStorageFlexFlashControllerConfiguredMode_Type=CfprStorageOperatingModeType
_CfprStorageFlexFlashControllerConfiguredMode_Object=MibTableColumn
cfprStorageFlexFlashControllerConfiguredMode=_CfprStorageFlexFlashControllerConfiguredMode_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,5),_CfprStorageFlexFlashControllerConfiguredMode_Type())
cfprStorageFlexFlashControllerConfiguredMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerConfiguredMode.setStatus(_A)
_CfprStorageFlexFlashControllerControllerHealth_Type=CfprStorageFFControllerHealth
_CfprStorageFlexFlashControllerControllerHealth_Object=MibTableColumn
cfprStorageFlexFlashControllerControllerHealth=_CfprStorageFlexFlashControllerControllerHealth_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,6),_CfprStorageFlexFlashControllerControllerHealth_Type())
cfprStorageFlexFlashControllerControllerHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerControllerHealth.setStatus(_A)
_CfprStorageFlexFlashControllerControllerState_Type=CfprStorageFFControllerState
_CfprStorageFlexFlashControllerControllerState_Object=MibTableColumn
cfprStorageFlexFlashControllerControllerState=_CfprStorageFlexFlashControllerControllerState_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,7),_CfprStorageFlexFlashControllerControllerState_Type())
cfprStorageFlexFlashControllerControllerState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerControllerState.setStatus(_A)
_CfprStorageFlexFlashControllerFirmwareVersion_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFirmwareVersion_Object=MibTableColumn
cfprStorageFlexFlashControllerFirmwareVersion=_CfprStorageFlexFlashControllerFirmwareVersion_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,8),_CfprStorageFlexFlashControllerFirmwareVersion_Type())
cfprStorageFlexFlashControllerFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFirmwareVersion.setStatus(_A)
_CfprStorageFlexFlashControllerFlexFlashType_Type=CfprStorageFFType
_CfprStorageFlexFlashControllerFlexFlashType_Object=MibTableColumn
cfprStorageFlexFlashControllerFlexFlashType=_CfprStorageFlexFlashControllerFlexFlashType_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,9),_CfprStorageFlexFlashControllerFlexFlashType_Type())
cfprStorageFlexFlashControllerFlexFlashType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFlexFlashType.setStatus(_A)
_CfprStorageFlexFlashControllerFsmDescr_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmDescr_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmDescr=_CfprStorageFlexFlashControllerFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,10),_CfprStorageFlexFlashControllerFsmDescr_Type())
cfprStorageFlexFlashControllerFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmDescr.setStatus(_A)
_CfprStorageFlexFlashControllerFsmPrev_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmPrev_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmPrev=_CfprStorageFlexFlashControllerFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,11),_CfprStorageFlexFlashControllerFsmPrev_Type())
cfprStorageFlexFlashControllerFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmPrev.setStatus(_A)
_CfprStorageFlexFlashControllerFsmProgr_Type=Gauge32
_CfprStorageFlexFlashControllerFsmProgr_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmProgr=_CfprStorageFlexFlashControllerFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,12),_CfprStorageFlexFlashControllerFsmProgr_Type())
cfprStorageFlexFlashControllerFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmProgr.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Type=Gauge32
_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvErrCode=_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,13),_CfprStorageFlexFlashControllerFsmRmtInvErrCode_Type())
cfprStorageFlexFlashControllerFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtInvErrCode.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvErrDescr=_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,14),_CfprStorageFlexFlashControllerFsmRmtInvErrDescr_Type())
cfprStorageFlexFlashControllerFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtInvErrDescr.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprStorageFlexFlashControllerFsmRmtInvRslt_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtInvRslt=_CfprStorageFlexFlashControllerFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,15),_CfprStorageFlexFlashControllerFsmRmtInvRslt_Type())
cfprStorageFlexFlashControllerFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtInvRslt.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageDescr_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageDescr_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageDescr=_CfprStorageFlexFlashControllerFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,16),_CfprStorageFlexFlashControllerFsmStageDescr_Type())
cfprStorageFlexFlashControllerFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageDescr.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStamp_Type=DateAndTime
_CfprStorageFlexFlashControllerFsmStamp_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStamp=_CfprStorageFlexFlashControllerFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,17),_CfprStorageFlexFlashControllerFsmStamp_Type())
cfprStorageFlexFlashControllerFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStamp.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStatus_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmStatus_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStatus=_CfprStorageFlexFlashControllerFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,18),_CfprStorageFlexFlashControllerFsmStatus_Type())
cfprStorageFlexFlashControllerFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStatus.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTry_Type=Gauge32
_CfprStorageFlexFlashControllerFsmTry_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTry=_CfprStorageFlexFlashControllerFsmTry_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,19),_CfprStorageFlexFlashControllerFsmTry_Type())
cfprStorageFlexFlashControllerFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTry.setStatus(_A)
_CfprStorageFlexFlashControllerHasError_Type=CfprStorageFFHasError
_CfprStorageFlexFlashControllerHasError_Object=MibTableColumn
cfprStorageFlexFlashControllerHasError=_CfprStorageFlexFlashControllerHasError_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,20),_CfprStorageFlexFlashControllerHasError_Type())
cfprStorageFlexFlashControllerHasError.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerHasError.setStatus(_A)
_CfprStorageFlexFlashControllerId_Type=CfprStorageFlexFlashControllerId
_CfprStorageFlexFlashControllerId_Object=MibTableColumn
cfprStorageFlexFlashControllerId=_CfprStorageFlexFlashControllerId_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,21),_CfprStorageFlexFlashControllerId_Type())
cfprStorageFlexFlashControllerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerId.setStatus(_A)
_CfprStorageFlexFlashControllerIsCardMismatch_Type=CfprStorageFFCardSizeMismatch
_CfprStorageFlexFlashControllerIsCardMismatch_Object=MibTableColumn
cfprStorageFlexFlashControllerIsCardMismatch=_CfprStorageFlexFlashControllerIsCardMismatch_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,22),_CfprStorageFlexFlashControllerIsCardMismatch_Type())
cfprStorageFlexFlashControllerIsCardMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerIsCardMismatch.setStatus(_A)
_CfprStorageFlexFlashControllerIsFormatFSMRunning_Type=CfprStorageFFFormatRunning
_CfprStorageFlexFlashControllerIsFormatFSMRunning_Object=MibTableColumn
cfprStorageFlexFlashControllerIsFormatFSMRunning=_CfprStorageFlexFlashControllerIsFormatFSMRunning_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,23),_CfprStorageFlexFlashControllerIsFormatFSMRunning_Type())
cfprStorageFlexFlashControllerIsFormatFSMRunning.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerIsFormatFSMRunning.setStatus(_A)
_CfprStorageFlexFlashControllerLocationDn_Type=SnmpAdminString
_CfprStorageFlexFlashControllerLocationDn_Object=MibTableColumn
cfprStorageFlexFlashControllerLocationDn=_CfprStorageFlexFlashControllerLocationDn_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,24),_CfprStorageFlexFlashControllerLocationDn_Type())
cfprStorageFlexFlashControllerLocationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerLocationDn.setStatus(_A)
_CfprStorageFlexFlashControllerModel_Type=SnmpAdminString
_CfprStorageFlexFlashControllerModel_Object=MibTableColumn
cfprStorageFlexFlashControllerModel=_CfprStorageFlexFlashControllerModel_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,25),_CfprStorageFlexFlashControllerModel_Type())
cfprStorageFlexFlashControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerModel.setStatus(_A)
_CfprStorageFlexFlashControllerOperQualifierReason_Type=SnmpAdminString
_CfprStorageFlexFlashControllerOperQualifierReason_Object=MibTableColumn
cfprStorageFlexFlashControllerOperQualifierReason=_CfprStorageFlexFlashControllerOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,26),_CfprStorageFlexFlashControllerOperQualifierReason_Type())
cfprStorageFlexFlashControllerOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerOperQualifierReason.setStatus(_A)
_CfprStorageFlexFlashControllerOperState_Type=CfprEquipmentOperability
_CfprStorageFlexFlashControllerOperState_Object=MibTableColumn
cfprStorageFlexFlashControllerOperState=_CfprStorageFlexFlashControllerOperState_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,27),_CfprStorageFlexFlashControllerOperState_Type())
cfprStorageFlexFlashControllerOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerOperState.setStatus(_A)
_CfprStorageFlexFlashControllerOperability_Type=CfprEquipmentOperability
_CfprStorageFlexFlashControllerOperability_Object=MibTableColumn
cfprStorageFlexFlashControllerOperability=_CfprStorageFlexFlashControllerOperability_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,28),_CfprStorageFlexFlashControllerOperability_Type())
cfprStorageFlexFlashControllerOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerOperability.setStatus(_A)
_CfprStorageFlexFlashControllerOperatingMode_Type=CfprStorageOperatingModeType
_CfprStorageFlexFlashControllerOperatingMode_Object=MibTableColumn
cfprStorageFlexFlashControllerOperatingMode=_CfprStorageFlexFlashControllerOperatingMode_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,29),_CfprStorageFlexFlashControllerOperatingMode_Type())
cfprStorageFlexFlashControllerOperatingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerOperatingMode.setStatus(_A)
_CfprStorageFlexFlashControllerOperationRequest_Type=CfprStorageOperationRequestType
_CfprStorageFlexFlashControllerOperationRequest_Object=MibTableColumn
cfprStorageFlexFlashControllerOperationRequest=_CfprStorageFlexFlashControllerOperationRequest_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,30),_CfprStorageFlexFlashControllerOperationRequest_Type())
cfprStorageFlexFlashControllerOperationRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerOperationRequest.setStatus(_A)
_CfprStorageFlexFlashControllerPciAddr_Type=SnmpAdminString
_CfprStorageFlexFlashControllerPciAddr_Object=MibTableColumn
cfprStorageFlexFlashControllerPciAddr=_CfprStorageFlexFlashControllerPciAddr_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,31),_CfprStorageFlexFlashControllerPciAddr_Type())
cfprStorageFlexFlashControllerPciAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPciAddr.setStatus(_A)
_CfprStorageFlexFlashControllerPciSlot_Type=SnmpAdminString
_CfprStorageFlexFlashControllerPciSlot_Object=MibTableColumn
cfprStorageFlexFlashControllerPciSlot=_CfprStorageFlexFlashControllerPciSlot_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,32),_CfprStorageFlexFlashControllerPciSlot_Type())
cfprStorageFlexFlashControllerPciSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPciSlot.setStatus(_A)
_CfprStorageFlexFlashControllerPerf_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerPerf_Object=MibTableColumn
cfprStorageFlexFlashControllerPerf=_CfprStorageFlexFlashControllerPerf_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,33),_CfprStorageFlexFlashControllerPerf_Type())
cfprStorageFlexFlashControllerPerf.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPerf.setStatus(_A)
_CfprStorageFlexFlashControllerPhysicalDriveCount_Type=Gauge32
_CfprStorageFlexFlashControllerPhysicalDriveCount_Object=MibTableColumn
cfprStorageFlexFlashControllerPhysicalDriveCount=_CfprStorageFlexFlashControllerPhysicalDriveCount_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,34),_CfprStorageFlexFlashControllerPhysicalDriveCount_Type())
cfprStorageFlexFlashControllerPhysicalDriveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPhysicalDriveCount.setStatus(_A)
_CfprStorageFlexFlashControllerPower_Type=CfprEquipmentPowerState
_CfprStorageFlexFlashControllerPower_Object=MibTableColumn
cfprStorageFlexFlashControllerPower=_CfprStorageFlexFlashControllerPower_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,35),_CfprStorageFlexFlashControllerPower_Type())
cfprStorageFlexFlashControllerPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPower.setStatus(_A)
_CfprStorageFlexFlashControllerPresence_Type=CfprEquipmentPresence
_CfprStorageFlexFlashControllerPresence_Object=MibTableColumn
cfprStorageFlexFlashControllerPresence=_CfprStorageFlexFlashControllerPresence_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,36),_CfprStorageFlexFlashControllerPresence_Type())
cfprStorageFlexFlashControllerPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPresence.setStatus(_A)
_CfprStorageFlexFlashControllerPrimarySlotNumber_Type=Gauge32
_CfprStorageFlexFlashControllerPrimarySlotNumber_Object=MibTableColumn
cfprStorageFlexFlashControllerPrimarySlotNumber=_CfprStorageFlexFlashControllerPrimarySlotNumber_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,37),_CfprStorageFlexFlashControllerPrimarySlotNumber_Type())
cfprStorageFlexFlashControllerPrimarySlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerPrimarySlotNumber.setStatus(_A)
_CfprStorageFlexFlashControllerRaidSyncSupport_Type=CfprStorageFFRaidSyncSupport
_CfprStorageFlexFlashControllerRaidSyncSupport_Object=MibTableColumn
cfprStorageFlexFlashControllerRaidSyncSupport=_CfprStorageFlexFlashControllerRaidSyncSupport_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,38),_CfprStorageFlexFlashControllerRaidSyncSupport_Type())
cfprStorageFlexFlashControllerRaidSyncSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerRaidSyncSupport.setStatus(_A)
_CfprStorageFlexFlashControllerReadErrorThreshold_Type=Gauge32
_CfprStorageFlexFlashControllerReadErrorThreshold_Object=MibTableColumn
cfprStorageFlexFlashControllerReadErrorThreshold=_CfprStorageFlexFlashControllerReadErrorThreshold_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,39),_CfprStorageFlexFlashControllerReadErrorThreshold_Type())
cfprStorageFlexFlashControllerReadErrorThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerReadErrorThreshold.setStatus(_A)
_CfprStorageFlexFlashControllerRevision_Type=SnmpAdminString
_CfprStorageFlexFlashControllerRevision_Object=MibTableColumn
cfprStorageFlexFlashControllerRevision=_CfprStorageFlexFlashControllerRevision_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,40),_CfprStorageFlexFlashControllerRevision_Type())
cfprStorageFlexFlashControllerRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerRevision.setStatus(_A)
_CfprStorageFlexFlashControllerSerial_Type=SnmpAdminString
_CfprStorageFlexFlashControllerSerial_Object=MibTableColumn
cfprStorageFlexFlashControllerSerial=_CfprStorageFlexFlashControllerSerial_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,41),_CfprStorageFlexFlashControllerSerial_Type())
cfprStorageFlexFlashControllerSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerSerial.setStatus(_A)
_CfprStorageFlexFlashControllerThermal_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerThermal_Object=MibTableColumn
cfprStorageFlexFlashControllerThermal=_CfprStorageFlexFlashControllerThermal_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,42),_CfprStorageFlexFlashControllerThermal_Type())
cfprStorageFlexFlashControllerThermal.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerThermal.setStatus(_A)
_CfprStorageFlexFlashControllerType_Type=CfprStorageControllerType
_CfprStorageFlexFlashControllerType_Object=MibTableColumn
cfprStorageFlexFlashControllerType=_CfprStorageFlexFlashControllerType_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,43),_CfprStorageFlexFlashControllerType_Type())
cfprStorageFlexFlashControllerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerType.setStatus(_A)
_CfprStorageFlexFlashControllerVendor_Type=SnmpAdminString
_CfprStorageFlexFlashControllerVendor_Object=MibTableColumn
cfprStorageFlexFlashControllerVendor=_CfprStorageFlexFlashControllerVendor_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,44),_CfprStorageFlexFlashControllerVendor_Type())
cfprStorageFlexFlashControllerVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerVendor.setStatus(_A)
_CfprStorageFlexFlashControllerVirtualDriveCount_Type=Gauge32
_CfprStorageFlexFlashControllerVirtualDriveCount_Object=MibTableColumn
cfprStorageFlexFlashControllerVirtualDriveCount=_CfprStorageFlexFlashControllerVirtualDriveCount_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,45),_CfprStorageFlexFlashControllerVirtualDriveCount_Type())
cfprStorageFlexFlashControllerVirtualDriveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerVirtualDriveCount.setStatus(_A)
_CfprStorageFlexFlashControllerVoltage_Type=CfprEquipmentSensorThresholdStatus
_CfprStorageFlexFlashControllerVoltage_Object=MibTableColumn
cfprStorageFlexFlashControllerVoltage=_CfprStorageFlexFlashControllerVoltage_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,46),_CfprStorageFlexFlashControllerVoltage_Type())
cfprStorageFlexFlashControllerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerVoltage.setStatus(_A)
_CfprStorageFlexFlashControllerWriteErrorThreshold_Type=Gauge32
_CfprStorageFlexFlashControllerWriteErrorThreshold_Object=MibTableColumn
cfprStorageFlexFlashControllerWriteErrorThreshold=_CfprStorageFlexFlashControllerWriteErrorThreshold_Object((1,3,6,1,4,1,9,9,826,1,74,14,1,47),_CfprStorageFlexFlashControllerWriteErrorThreshold_Type())
cfprStorageFlexFlashControllerWriteErrorThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerWriteErrorThreshold.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTable_Object=MibTable
cfprStorageFlexFlashControllerFsmTable=_CfprStorageFlexFlashControllerFsmTable_Object((1,3,6,1,4,1,9,9,826,1,74,15))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTable.setStatus(_A)
_CfprStorageFlexFlashControllerFsmEntry_Object=MibTableRow
cfprStorageFlexFlashControllerFsmEntry=_CfprStorageFlexFlashControllerFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,74,15,1))
cfprStorageFlexFlashControllerFsmEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmEntry.setStatus(_A)
_CfprStorageFlexFlashControllerFsmInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmInstanceId_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmInstanceId=_CfprStorageFlexFlashControllerFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,1),_CfprStorageFlexFlashControllerFsmInstanceId_Type())
cfprStorageFlexFlashControllerFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmInstanceId.setStatus(_A)
_CfprStorageFlexFlashControllerFsmDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmDn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmDn=_CfprStorageFlexFlashControllerFsmDn_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,2),_CfprStorageFlexFlashControllerFsmDn_Type())
cfprStorageFlexFlashControllerFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmDn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRn_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmRn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRn=_CfprStorageFlexFlashControllerFsmRn_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,3),_CfprStorageFlexFlashControllerFsmRn_Type())
cfprStorageFlexFlashControllerFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmCompletionTime_Type=DateAndTime
_CfprStorageFlexFlashControllerFsmCompletionTime_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmCompletionTime=_CfprStorageFlexFlashControllerFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,4),_CfprStorageFlexFlashControllerFsmCompletionTime_Type())
cfprStorageFlexFlashControllerFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmCompletionTime.setStatus(_A)
_CfprStorageFlexFlashControllerFsmCurrentFsm_Type=CfprStorageFlexFlashControllerFsmCurrentFsm
_CfprStorageFlexFlashControllerFsmCurrentFsm_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmCurrentFsm=_CfprStorageFlexFlashControllerFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,5),_CfprStorageFlexFlashControllerFsmCurrentFsm_Type())
cfprStorageFlexFlashControllerFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmCurrentFsm.setStatus(_A)
_CfprStorageFlexFlashControllerFsmDescrData_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmDescrData_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmDescrData=_CfprStorageFlexFlashControllerFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,6),_CfprStorageFlexFlashControllerFsmDescrData_Type())
cfprStorageFlexFlashControllerFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmDescrData.setStatus(_A)
_CfprStorageFlexFlashControllerFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprStorageFlexFlashControllerFsmFsmStatus_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmFsmStatus=_CfprStorageFlexFlashControllerFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,7),_CfprStorageFlexFlashControllerFsmFsmStatus_Type())
cfprStorageFlexFlashControllerFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmFsmStatus.setStatus(_A)
_CfprStorageFlexFlashControllerFsmProgress_Type=Gauge32
_CfprStorageFlexFlashControllerFsmProgress_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmProgress=_CfprStorageFlexFlashControllerFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,8),_CfprStorageFlexFlashControllerFsmProgress_Type())
cfprStorageFlexFlashControllerFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmProgress.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtErrCode_Type=Gauge32
_CfprStorageFlexFlashControllerFsmRmtErrCode_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtErrCode=_CfprStorageFlexFlashControllerFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,9),_CfprStorageFlexFlashControllerFsmRmtErrCode_Type())
cfprStorageFlexFlashControllerFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtErrCode.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtErrDescr_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmRmtErrDescr_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtErrDescr=_CfprStorageFlexFlashControllerFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,10),_CfprStorageFlexFlashControllerFsmRmtErrDescr_Type())
cfprStorageFlexFlashControllerFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtErrDescr.setStatus(_A)
_CfprStorageFlexFlashControllerFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprStorageFlexFlashControllerFsmRmtRslt_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmRmtRslt=_CfprStorageFlexFlashControllerFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,74,15,1,11),_CfprStorageFlexFlashControllerFsmRmtRslt_Type())
cfprStorageFlexFlashControllerFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmRmtRslt.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageTable_Object=MibTable
cfprStorageFlexFlashControllerFsmStageTable=_CfprStorageFlexFlashControllerFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,74,16))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageTable.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageEntry_Object=MibTableRow
cfprStorageFlexFlashControllerFsmStageEntry=_CfprStorageFlexFlashControllerFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,74,16,1))
cfprStorageFlexFlashControllerFsmStageEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageEntry.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmStageInstanceId_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageInstanceId=_CfprStorageFlexFlashControllerFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,1),_CfprStorageFlexFlashControllerFsmStageInstanceId_Type())
cfprStorageFlexFlashControllerFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageInstanceId.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmStageDn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageDn=_CfprStorageFlexFlashControllerFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,2),_CfprStorageFlexFlashControllerFsmStageDn_Type())
cfprStorageFlexFlashControllerFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageDn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageRn_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageRn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageRn=_CfprStorageFlexFlashControllerFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,3),_CfprStorageFlexFlashControllerFsmStageRn_Type())
cfprStorageFlexFlashControllerFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageRn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageDescrData_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmStageDescrData_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageDescrData=_CfprStorageFlexFlashControllerFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,4),_CfprStorageFlexFlashControllerFsmStageDescrData_Type())
cfprStorageFlexFlashControllerFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageDescrData.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Type=DateAndTime
_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageLastUpdateTime=_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,5),_CfprStorageFlexFlashControllerFsmStageLastUpdateTime_Type())
cfprStorageFlexFlashControllerFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageLastUpdateTime.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageName_Type=CfprStorageFlexFlashControllerFsmStageName
_CfprStorageFlexFlashControllerFsmStageName_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageName=_CfprStorageFlexFlashControllerFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,6),_CfprStorageFlexFlashControllerFsmStageName_Type())
cfprStorageFlexFlashControllerFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageName.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageOrder_Type=Gauge32
_CfprStorageFlexFlashControllerFsmStageOrder_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageOrder=_CfprStorageFlexFlashControllerFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,7),_CfprStorageFlexFlashControllerFsmStageOrder_Type())
cfprStorageFlexFlashControllerFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageOrder.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageRetry_Type=Gauge32
_CfprStorageFlexFlashControllerFsmStageRetry_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageRetry=_CfprStorageFlexFlashControllerFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,8),_CfprStorageFlexFlashControllerFsmStageRetry_Type())
cfprStorageFlexFlashControllerFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageRetry.setStatus(_A)
_CfprStorageFlexFlashControllerFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprStorageFlexFlashControllerFsmStageStageStatus_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmStageStageStatus=_CfprStorageFlexFlashControllerFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,74,16,1,9),_CfprStorageFlexFlashControllerFsmStageStageStatus_Type())
cfprStorageFlexFlashControllerFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmStageStageStatus.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskTable_Object=MibTable
cfprStorageFlexFlashControllerFsmTaskTable=_CfprStorageFlexFlashControllerFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,74,17))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskTable.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskEntry_Object=MibTableRow
cfprStorageFlexFlashControllerFsmTaskEntry=_CfprStorageFlexFlashControllerFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,74,17,1))
cfprStorageFlexFlashControllerFsmTaskEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskEntry.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashControllerFsmTaskInstanceId_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskInstanceId=_CfprStorageFlexFlashControllerFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,1),_CfprStorageFlexFlashControllerFsmTaskInstanceId_Type())
cfprStorageFlexFlashControllerFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskInstanceId.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashControllerFsmTaskDn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskDn=_CfprStorageFlexFlashControllerFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,2),_CfprStorageFlexFlashControllerFsmTaskDn_Type())
cfprStorageFlexFlashControllerFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskDn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskRn_Type=SnmpAdminString
_CfprStorageFlexFlashControllerFsmTaskRn_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskRn=_CfprStorageFlexFlashControllerFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,3),_CfprStorageFlexFlashControllerFsmTaskRn_Type())
cfprStorageFlexFlashControllerFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskRn.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskCompletion_Type=CfprFsmCompletion
_CfprStorageFlexFlashControllerFsmTaskCompletion_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskCompletion=_CfprStorageFlexFlashControllerFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,4),_CfprStorageFlexFlashControllerFsmTaskCompletion_Type())
cfprStorageFlexFlashControllerFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskCompletion.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskFlags_Type=CfprFsmFlags
_CfprStorageFlexFlashControllerFsmTaskFlags_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskFlags=_CfprStorageFlexFlashControllerFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,5),_CfprStorageFlexFlashControllerFsmTaskFlags_Type())
cfprStorageFlexFlashControllerFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskFlags.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskItem_Type=CfprStorageFlexFlashControllerFsmTaskItem
_CfprStorageFlexFlashControllerFsmTaskItem_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskItem=_CfprStorageFlexFlashControllerFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,6),_CfprStorageFlexFlashControllerFsmTaskItem_Type())
cfprStorageFlexFlashControllerFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskItem.setStatus(_A)
_CfprStorageFlexFlashControllerFsmTaskSeqId_Type=Gauge32
_CfprStorageFlexFlashControllerFsmTaskSeqId_Object=MibTableColumn
cfprStorageFlexFlashControllerFsmTaskSeqId=_CfprStorageFlexFlashControllerFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,74,17,1,7),_CfprStorageFlexFlashControllerFsmTaskSeqId_Type())
cfprStorageFlexFlashControllerFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashControllerFsmTaskSeqId.setStatus(_A)
_CfprStorageFlexFlashDriveTable_Object=MibTable
cfprStorageFlexFlashDriveTable=_CfprStorageFlexFlashDriveTable_Object((1,3,6,1,4,1,9,9,826,1,74,18))
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveTable.setStatus(_A)
_CfprStorageFlexFlashDriveEntry_Object=MibTableRow
cfprStorageFlexFlashDriveEntry=_CfprStorageFlexFlashDriveEntry_Object((1,3,6,1,4,1,9,9,826,1,74,18,1))
cfprStorageFlexFlashDriveEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveEntry.setStatus(_A)
_CfprStorageFlexFlashDriveInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashDriveInstanceId_Object=MibTableColumn
cfprStorageFlexFlashDriveInstanceId=_CfprStorageFlexFlashDriveInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,1),_CfprStorageFlexFlashDriveInstanceId_Type())
cfprStorageFlexFlashDriveInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveInstanceId.setStatus(_A)
_CfprStorageFlexFlashDriveDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashDriveDn_Object=MibTableColumn
cfprStorageFlexFlashDriveDn=_CfprStorageFlexFlashDriveDn_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,2),_CfprStorageFlexFlashDriveDn_Type())
cfprStorageFlexFlashDriveDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveDn.setStatus(_A)
_CfprStorageFlexFlashDriveRn_Type=SnmpAdminString
_CfprStorageFlexFlashDriveRn_Object=MibTableColumn
cfprStorageFlexFlashDriveRn=_CfprStorageFlexFlashDriveRn_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,3),_CfprStorageFlexFlashDriveRn_Type())
cfprStorageFlexFlashDriveRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveRn.setStatus(_A)
_CfprStorageFlexFlashDriveRWType_Type=CfprStorageFFRWType
_CfprStorageFlexFlashDriveRWType_Object=MibTableColumn
cfprStorageFlexFlashDriveRWType=_CfprStorageFlexFlashDriveRWType_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,4),_CfprStorageFlexFlashDriveRWType_Type())
cfprStorageFlexFlashDriveRWType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveRWType.setStatus(_A)
_CfprStorageFlexFlashDriveBlockSize_Type=Gauge32
_CfprStorageFlexFlashDriveBlockSize_Object=MibTableColumn
cfprStorageFlexFlashDriveBlockSize=_CfprStorageFlexFlashDriveBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,5),_CfprStorageFlexFlashDriveBlockSize_Type())
cfprStorageFlexFlashDriveBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveBlockSize.setStatus(_A)
_CfprStorageFlexFlashDriveConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageFlexFlashDriveConnectionProtocol_Object=MibTableColumn
cfprStorageFlexFlashDriveConnectionProtocol=_CfprStorageFlexFlashDriveConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,6),_CfprStorageFlexFlashDriveConnectionProtocol_Type())
cfprStorageFlexFlashDriveConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveConnectionProtocol.setStatus(_A)
_CfprStorageFlexFlashDriveControllerIndex_Type=Gauge32
_CfprStorageFlexFlashDriveControllerIndex_Object=MibTableColumn
cfprStorageFlexFlashDriveControllerIndex=_CfprStorageFlexFlashDriveControllerIndex_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,7),_CfprStorageFlexFlashDriveControllerIndex_Type())
cfprStorageFlexFlashDriveControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveControllerIndex.setStatus(_A)
_CfprStorageFlexFlashDriveDriveState_Type=CfprStorageFFDriveState
_CfprStorageFlexFlashDriveDriveState_Object=MibTableColumn
cfprStorageFlexFlashDriveDriveState=_CfprStorageFlexFlashDriveDriveState_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,8),_CfprStorageFlexFlashDriveDriveState_Type())
cfprStorageFlexFlashDriveDriveState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveDriveState.setStatus(_A)
_CfprStorageFlexFlashDriveDriveType_Type=CfprStorageFFDriveType
_CfprStorageFlexFlashDriveDriveType_Object=MibTableColumn
cfprStorageFlexFlashDriveDriveType=_CfprStorageFlexFlashDriveDriveType_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,9),_CfprStorageFlexFlashDriveDriveType_Type())
cfprStorageFlexFlashDriveDriveType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveDriveType.setStatus(_A)
_CfprStorageFlexFlashDriveId_Type=Gauge32
_CfprStorageFlexFlashDriveId_Object=MibTableColumn
cfprStorageFlexFlashDriveId=_CfprStorageFlexFlashDriveId_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,10),_CfprStorageFlexFlashDriveId_Type())
cfprStorageFlexFlashDriveId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveId.setStatus(_A)
_CfprStorageFlexFlashDriveLastOperation_Type=CfprStorageOperationStateType
_CfprStorageFlexFlashDriveLastOperation_Object=MibTableColumn
cfprStorageFlexFlashDriveLastOperation=_CfprStorageFlexFlashDriveLastOperation_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,11),_CfprStorageFlexFlashDriveLastOperation_Type())
cfprStorageFlexFlashDriveLastOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveLastOperation.setStatus(_A)
_CfprStorageFlexFlashDriveModel_Type=SnmpAdminString
_CfprStorageFlexFlashDriveModel_Object=MibTableColumn
cfprStorageFlexFlashDriveModel=_CfprStorageFlexFlashDriveModel_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,12),_CfprStorageFlexFlashDriveModel_Type())
cfprStorageFlexFlashDriveModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveModel.setStatus(_A)
_CfprStorageFlexFlashDriveName_Type=SnmpAdminString
_CfprStorageFlexFlashDriveName_Object=MibTableColumn
cfprStorageFlexFlashDriveName=_CfprStorageFlexFlashDriveName_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,13),_CfprStorageFlexFlashDriveName_Type())
cfprStorageFlexFlashDriveName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveName.setStatus(_A)
_CfprStorageFlexFlashDriveNumberOfBlocks_Type=Unsigned64
_CfprStorageFlexFlashDriveNumberOfBlocks_Object=MibTableColumn
cfprStorageFlexFlashDriveNumberOfBlocks=_CfprStorageFlexFlashDriveNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,14),_CfprStorageFlexFlashDriveNumberOfBlocks_Type())
cfprStorageFlexFlashDriveNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveNumberOfBlocks.setStatus(_A)
_CfprStorageFlexFlashDriveOperQualifierReason_Type=SnmpAdminString
_CfprStorageFlexFlashDriveOperQualifierReason_Object=MibTableColumn
cfprStorageFlexFlashDriveOperQualifierReason=_CfprStorageFlexFlashDriveOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,15),_CfprStorageFlexFlashDriveOperQualifierReason_Type())
cfprStorageFlexFlashDriveOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveOperQualifierReason.setStatus(_A)
_CfprStorageFlexFlashDriveOperability_Type=CfprEquipmentOperability
_CfprStorageFlexFlashDriveOperability_Object=MibTableColumn
cfprStorageFlexFlashDriveOperability=_CfprStorageFlexFlashDriveOperability_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,16),_CfprStorageFlexFlashDriveOperability_Type())
cfprStorageFlexFlashDriveOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveOperability.setStatus(_A)
_CfprStorageFlexFlashDriveOperationState_Type=CfprStorageOperationStateType
_CfprStorageFlexFlashDriveOperationState_Object=MibTableColumn
cfprStorageFlexFlashDriveOperationState=_CfprStorageFlexFlashDriveOperationState_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,17),_CfprStorageFlexFlashDriveOperationState_Type())
cfprStorageFlexFlashDriveOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveOperationState.setStatus(_A)
_CfprStorageFlexFlashDrivePresence_Type=CfprEquipmentPresence
_CfprStorageFlexFlashDrivePresence_Object=MibTableColumn
cfprStorageFlexFlashDrivePresence=_CfprStorageFlexFlashDrivePresence_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,18),_CfprStorageFlexFlashDrivePresence_Type())
cfprStorageFlexFlashDrivePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDrivePresence.setStatus(_A)
_CfprStorageFlexFlashDriveRemovable_Type=CfprStorageFFDriveRemovable
_CfprStorageFlexFlashDriveRemovable_Object=MibTableColumn
cfprStorageFlexFlashDriveRemovable=_CfprStorageFlexFlashDriveRemovable_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,19),_CfprStorageFlexFlashDriveRemovable_Type())
cfprStorageFlexFlashDriveRemovable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveRemovable.setStatus(_A)
_CfprStorageFlexFlashDriveRevision_Type=SnmpAdminString
_CfprStorageFlexFlashDriveRevision_Object=MibTableColumn
cfprStorageFlexFlashDriveRevision=_CfprStorageFlexFlashDriveRevision_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,20),_CfprStorageFlexFlashDriveRevision_Type())
cfprStorageFlexFlashDriveRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveRevision.setStatus(_A)
_CfprStorageFlexFlashDriveSerial_Type=SnmpAdminString
_CfprStorageFlexFlashDriveSerial_Object=MibTableColumn
cfprStorageFlexFlashDriveSerial=_CfprStorageFlexFlashDriveSerial_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,21),_CfprStorageFlexFlashDriveSerial_Type())
cfprStorageFlexFlashDriveSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveSerial.setStatus(_A)
_CfprStorageFlexFlashDriveSize_Type=Unsigned64
_CfprStorageFlexFlashDriveSize_Object=MibTableColumn
cfprStorageFlexFlashDriveSize=_CfprStorageFlexFlashDriveSize_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,22),_CfprStorageFlexFlashDriveSize_Type())
cfprStorageFlexFlashDriveSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveSize.setStatus(_A)
_CfprStorageFlexFlashDriveSlotNumber_Type=Gauge32
_CfprStorageFlexFlashDriveSlotNumber_Object=MibTableColumn
cfprStorageFlexFlashDriveSlotNumber=_CfprStorageFlexFlashDriveSlotNumber_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,23),_CfprStorageFlexFlashDriveSlotNumber_Type())
cfprStorageFlexFlashDriveSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveSlotNumber.setStatus(_A)
_CfprStorageFlexFlashDriveVendor_Type=SnmpAdminString
_CfprStorageFlexFlashDriveVendor_Object=MibTableColumn
cfprStorageFlexFlashDriveVendor=_CfprStorageFlexFlashDriveVendor_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,24),_CfprStorageFlexFlashDriveVendor_Type())
cfprStorageFlexFlashDriveVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveVendor.setStatus(_A)
_CfprStorageFlexFlashDriveVisible_Type=CfprStorageFFDriveVisible
_CfprStorageFlexFlashDriveVisible_Object=MibTableColumn
cfprStorageFlexFlashDriveVisible=_CfprStorageFlexFlashDriveVisible_Object((1,3,6,1,4,1,9,9,826,1,74,18,1,25),_CfprStorageFlexFlashDriveVisible_Type())
cfprStorageFlexFlashDriveVisible.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashDriveVisible.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveTable_Object=MibTable
cfprStorageFlexFlashVirtualDriveTable=_CfprStorageFlexFlashVirtualDriveTable_Object((1,3,6,1,4,1,9,9,826,1,74,19))
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveTable.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveEntry_Object=MibTableRow
cfprStorageFlexFlashVirtualDriveEntry=_CfprStorageFlexFlashVirtualDriveEntry_Object((1,3,6,1,4,1,9,9,826,1,74,19,1))
cfprStorageFlexFlashVirtualDriveEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveEntry.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveInstanceId_Type=CfprManagedObjectId
_CfprStorageFlexFlashVirtualDriveInstanceId_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveInstanceId=_CfprStorageFlexFlashVirtualDriveInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,1),_CfprStorageFlexFlashVirtualDriveInstanceId_Type())
cfprStorageFlexFlashVirtualDriveInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveInstanceId.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveDn_Type=CfprManagedObjectDn
_CfprStorageFlexFlashVirtualDriveDn_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveDn=_CfprStorageFlexFlashVirtualDriveDn_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,2),_CfprStorageFlexFlashVirtualDriveDn_Type())
cfprStorageFlexFlashVirtualDriveDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveDn.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveRn_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveRn_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveRn=_CfprStorageFlexFlashVirtualDriveRn_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,3),_CfprStorageFlexFlashVirtualDriveRn_Type())
cfprStorageFlexFlashVirtualDriveRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveRn.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveBlockSize_Type=Gauge32
_CfprStorageFlexFlashVirtualDriveBlockSize_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveBlockSize=_CfprStorageFlexFlashVirtualDriveBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,4),_CfprStorageFlexFlashVirtualDriveBlockSize_Type())
cfprStorageFlexFlashVirtualDriveBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveBlockSize.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveConnectionProtocol=_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,5),_CfprStorageFlexFlashVirtualDriveConnectionProtocol_Type())
cfprStorageFlexFlashVirtualDriveConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveConnectionProtocol.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveId_Type=Gauge32
_CfprStorageFlexFlashVirtualDriveId_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveId=_CfprStorageFlexFlashVirtualDriveId_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,6),_CfprStorageFlexFlashVirtualDriveId_Type())
cfprStorageFlexFlashVirtualDriveId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveId.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveModel_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveModel_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveModel=_CfprStorageFlexFlashVirtualDriveModel_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,7),_CfprStorageFlexFlashVirtualDriveModel_Type())
cfprStorageFlexFlashVirtualDriveModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveModel.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Type=Unsigned64
_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveNumberOfBlocks=_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,8),_CfprStorageFlexFlashVirtualDriveNumberOfBlocks_Type())
cfprStorageFlexFlashVirtualDriveNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveNumberOfBlocks.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveOperQualifierReason=_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,9),_CfprStorageFlexFlashVirtualDriveOperQualifierReason_Type())
cfprStorageFlexFlashVirtualDriveOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveOperQualifierReason.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveOperability_Type=CfprEquipmentOperability
_CfprStorageFlexFlashVirtualDriveOperability_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveOperability=_CfprStorageFlexFlashVirtualDriveOperability_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,10),_CfprStorageFlexFlashVirtualDriveOperability_Type())
cfprStorageFlexFlashVirtualDriveOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveOperability.setStatus(_A)
_CfprStorageFlexFlashVirtualDrivePresence_Type=CfprEquipmentPresence
_CfprStorageFlexFlashVirtualDrivePresence_Object=MibTableColumn
cfprStorageFlexFlashVirtualDrivePresence=_CfprStorageFlexFlashVirtualDrivePresence_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,11),_CfprStorageFlexFlashVirtualDrivePresence_Type())
cfprStorageFlexFlashVirtualDrivePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDrivePresence.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveRaidHealth_Type=CfprStorageFFRAIDHealth
_CfprStorageFlexFlashVirtualDriveRaidHealth_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveRaidHealth=_CfprStorageFlexFlashVirtualDriveRaidHealth_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,12),_CfprStorageFlexFlashVirtualDriveRaidHealth_Type())
cfprStorageFlexFlashVirtualDriveRaidHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveRaidHealth.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveRaidState_Type=CfprStorageFFRAIDState
_CfprStorageFlexFlashVirtualDriveRaidState_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveRaidState=_CfprStorageFlexFlashVirtualDriveRaidState_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,13),_CfprStorageFlexFlashVirtualDriveRaidState_Type())
cfprStorageFlexFlashVirtualDriveRaidState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveRaidState.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveRevision_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveRevision_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveRevision=_CfprStorageFlexFlashVirtualDriveRevision_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,14),_CfprStorageFlexFlashVirtualDriveRevision_Type())
cfprStorageFlexFlashVirtualDriveRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveRevision.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveSerial_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveSerial_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveSerial=_CfprStorageFlexFlashVirtualDriveSerial_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,15),_CfprStorageFlexFlashVirtualDriveSerial_Type())
cfprStorageFlexFlashVirtualDriveSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveSerial.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveSize_Type=Unsigned64
_CfprStorageFlexFlashVirtualDriveSize_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveSize=_CfprStorageFlexFlashVirtualDriveSize_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,16),_CfprStorageFlexFlashVirtualDriveSize_Type())
cfprStorageFlexFlashVirtualDriveSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveSize.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveType_Type=CfprStorageLunType
_CfprStorageFlexFlashVirtualDriveType_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveType=_CfprStorageFlexFlashVirtualDriveType_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,17),_CfprStorageFlexFlashVirtualDriveType_Type())
cfprStorageFlexFlashVirtualDriveType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveType.setStatus(_A)
_CfprStorageFlexFlashVirtualDriveVendor_Type=SnmpAdminString
_CfprStorageFlexFlashVirtualDriveVendor_Object=MibTableColumn
cfprStorageFlexFlashVirtualDriveVendor=_CfprStorageFlexFlashVirtualDriveVendor_Object((1,3,6,1,4,1,9,9,826,1,74,19,1,18),_CfprStorageFlexFlashVirtualDriveVendor_Type())
cfprStorageFlexFlashVirtualDriveVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageFlexFlashVirtualDriveVendor.setStatus(_A)
_CfprStorageIScsiTargetIfTable_Object=MibTable
cfprStorageIScsiTargetIfTable=_CfprStorageIScsiTargetIfTable_Object((1,3,6,1,4,1,9,9,826,1,74,20))
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfTable.setStatus(_A)
_CfprStorageIScsiTargetIfEntry_Object=MibTableRow
cfprStorageIScsiTargetIfEntry=_CfprStorageIScsiTargetIfEntry_Object((1,3,6,1,4,1,9,9,826,1,74,20,1))
cfprStorageIScsiTargetIfEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfEntry.setStatus(_A)
_CfprStorageIScsiTargetIfInstanceId_Type=CfprManagedObjectId
_CfprStorageIScsiTargetIfInstanceId_Object=MibTableColumn
cfprStorageIScsiTargetIfInstanceId=_CfprStorageIScsiTargetIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,20,1,1),_CfprStorageIScsiTargetIfInstanceId_Type())
cfprStorageIScsiTargetIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfInstanceId.setStatus(_A)
_CfprStorageIScsiTargetIfDn_Type=CfprManagedObjectDn
_CfprStorageIScsiTargetIfDn_Object=MibTableColumn
cfprStorageIScsiTargetIfDn=_CfprStorageIScsiTargetIfDn_Object((1,3,6,1,4,1,9,9,826,1,74,20,1,2),_CfprStorageIScsiTargetIfDn_Type())
cfprStorageIScsiTargetIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfDn.setStatus(_A)
_CfprStorageIScsiTargetIfRn_Type=SnmpAdminString
_CfprStorageIScsiTargetIfRn_Object=MibTableColumn
cfprStorageIScsiTargetIfRn=_CfprStorageIScsiTargetIfRn_Object((1,3,6,1,4,1,9,9,826,1,74,20,1,3),_CfprStorageIScsiTargetIfRn_Type())
cfprStorageIScsiTargetIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfRn.setStatus(_A)
_CfprStorageIScsiTargetIfName_Type=SnmpAdminString
_CfprStorageIScsiTargetIfName_Object=MibTableColumn
cfprStorageIScsiTargetIfName=_CfprStorageIScsiTargetIfName_Object((1,3,6,1,4,1,9,9,826,1,74,20,1,4),_CfprStorageIScsiTargetIfName_Type())
cfprStorageIScsiTargetIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfName.setStatus(_A)
_CfprStorageIScsiTargetIfProt_Type=CfprStorageProtocol
_CfprStorageIScsiTargetIfProt_Object=MibTableColumn
cfprStorageIScsiTargetIfProt=_CfprStorageIScsiTargetIfProt_Object((1,3,6,1,4,1,9,9,826,1,74,20,1,5),_CfprStorageIScsiTargetIfProt_Type())
cfprStorageIScsiTargetIfProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIScsiTargetIfProt.setStatus(_A)
_CfprStorageIniGroupTable_Object=MibTable
cfprStorageIniGroupTable=_CfprStorageIniGroupTable_Object((1,3,6,1,4,1,9,9,826,1,74,21))
if mibBuilder.loadTexts:cfprStorageIniGroupTable.setStatus(_A)
_CfprStorageIniGroupEntry_Object=MibTableRow
cfprStorageIniGroupEntry=_CfprStorageIniGroupEntry_Object((1,3,6,1,4,1,9,9,826,1,74,21,1))
cfprStorageIniGroupEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cfprStorageIniGroupEntry.setStatus(_A)
_CfprStorageIniGroupInstanceId_Type=CfprManagedObjectId
_CfprStorageIniGroupInstanceId_Object=MibTableColumn
cfprStorageIniGroupInstanceId=_CfprStorageIniGroupInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,1),_CfprStorageIniGroupInstanceId_Type())
cfprStorageIniGroupInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageIniGroupInstanceId.setStatus(_A)
_CfprStorageIniGroupDn_Type=CfprManagedObjectDn
_CfprStorageIniGroupDn_Object=MibTableColumn
cfprStorageIniGroupDn=_CfprStorageIniGroupDn_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,2),_CfprStorageIniGroupDn_Type())
cfprStorageIniGroupDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupDn.setStatus(_A)
_CfprStorageIniGroupRn_Type=SnmpAdminString
_CfprStorageIniGroupRn_Object=MibTableColumn
cfprStorageIniGroupRn=_CfprStorageIniGroupRn_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,3),_CfprStorageIniGroupRn_Type())
cfprStorageIniGroupRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupRn.setStatus(_A)
_CfprStorageIniGroupDescr_Type=SnmpAdminString
_CfprStorageIniGroupDescr_Object=MibTableColumn
cfprStorageIniGroupDescr=_CfprStorageIniGroupDescr_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,4),_CfprStorageIniGroupDescr_Type())
cfprStorageIniGroupDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupDescr.setStatus(_A)
_CfprStorageIniGroupGroupPolicyName_Type=SnmpAdminString
_CfprStorageIniGroupGroupPolicyName_Object=MibTableColumn
cfprStorageIniGroupGroupPolicyName=_CfprStorageIniGroupGroupPolicyName_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,5),_CfprStorageIniGroupGroupPolicyName_Type())
cfprStorageIniGroupGroupPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupGroupPolicyName.setStatus(_A)
_CfprStorageIniGroupIntId_Type=SnmpAdminString
_CfprStorageIniGroupIntId_Object=MibTableColumn
cfprStorageIniGroupIntId=_CfprStorageIniGroupIntId_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,6),_CfprStorageIniGroupIntId_Type())
cfprStorageIniGroupIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupIntId.setStatus(_A)
_CfprStorageIniGroupName_Type=SnmpAdminString
_CfprStorageIniGroupName_Object=MibTableColumn
cfprStorageIniGroupName=_CfprStorageIniGroupName_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,7),_CfprStorageIniGroupName_Type())
cfprStorageIniGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupName.setStatus(_A)
_CfprStorageIniGroupOperProtocol_Type=CfprStorageIniGroupOperProtocol
_CfprStorageIniGroupOperProtocol_Object=MibTableColumn
cfprStorageIniGroupOperProtocol=_CfprStorageIniGroupOperProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,8),_CfprStorageIniGroupOperProtocol_Type())
cfprStorageIniGroupOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupOperProtocol.setStatus(_A)
_CfprStorageIniGroupOperState_Type=CfprStorageOperState
_CfprStorageIniGroupOperState_Object=MibTableColumn
cfprStorageIniGroupOperState=_CfprStorageIniGroupOperState_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,9),_CfprStorageIniGroupOperState_Type())
cfprStorageIniGroupOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupOperState.setStatus(_A)
_CfprStorageIniGroupOwner_Type=CfprStorageIniGroupOwner
_CfprStorageIniGroupOwner_Object=MibTableColumn
cfprStorageIniGroupOwner=_CfprStorageIniGroupOwner_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,10),_CfprStorageIniGroupOwner_Type())
cfprStorageIniGroupOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupOwner.setStatus(_A)
_CfprStorageIniGroupPolicyLevel_Type=Gauge32
_CfprStorageIniGroupPolicyLevel_Object=MibTableColumn
cfprStorageIniGroupPolicyLevel=_CfprStorageIniGroupPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,11),_CfprStorageIniGroupPolicyLevel_Type())
cfprStorageIniGroupPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupPolicyLevel.setStatus(_A)
_CfprStorageIniGroupPolicyName_Type=SnmpAdminString
_CfprStorageIniGroupPolicyName_Object=MibTableColumn
cfprStorageIniGroupPolicyName=_CfprStorageIniGroupPolicyName_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,12),_CfprStorageIniGroupPolicyName_Type())
cfprStorageIniGroupPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupPolicyName.setStatus(_A)
_CfprStorageIniGroupPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageIniGroupPolicyOwner_Object=MibTableColumn
cfprStorageIniGroupPolicyOwner=_CfprStorageIniGroupPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,13),_CfprStorageIniGroupPolicyOwner_Type())
cfprStorageIniGroupPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupPolicyOwner.setStatus(_A)
_CfprStorageIniGroupProtocol_Type=CfprStorageIniGroupProtocol
_CfprStorageIniGroupProtocol_Object=MibTableColumn
cfprStorageIniGroupProtocol=_CfprStorageIniGroupProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,14),_CfprStorageIniGroupProtocol_Type())
cfprStorageIniGroupProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupProtocol.setStatus(_A)
_CfprStorageIniGroupRmtDiskCfgName_Type=SnmpAdminString
_CfprStorageIniGroupRmtDiskCfgName_Object=MibTableColumn
cfprStorageIniGroupRmtDiskCfgName=_CfprStorageIniGroupRmtDiskCfgName_Object((1,3,6,1,4,1,9,9,826,1,74,21,1,15),_CfprStorageIniGroupRmtDiskCfgName_Type())
cfprStorageIniGroupRmtDiskCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageIniGroupRmtDiskCfgName.setStatus(_A)
_CfprStorageInitiatorTable_Object=MibTable
cfprStorageInitiatorTable=_CfprStorageInitiatorTable_Object((1,3,6,1,4,1,9,9,826,1,74,22))
if mibBuilder.loadTexts:cfprStorageInitiatorTable.setStatus(_A)
_CfprStorageInitiatorEntry_Object=MibTableRow
cfprStorageInitiatorEntry=_CfprStorageInitiatorEntry_Object((1,3,6,1,4,1,9,9,826,1,74,22,1))
cfprStorageInitiatorEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cfprStorageInitiatorEntry.setStatus(_A)
_CfprStorageInitiatorInstanceId_Type=CfprManagedObjectId
_CfprStorageInitiatorInstanceId_Object=MibTableColumn
cfprStorageInitiatorInstanceId=_CfprStorageInitiatorInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,1),_CfprStorageInitiatorInstanceId_Type())
cfprStorageInitiatorInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageInitiatorInstanceId.setStatus(_A)
_CfprStorageInitiatorDn_Type=CfprManagedObjectDn
_CfprStorageInitiatorDn_Object=MibTableColumn
cfprStorageInitiatorDn=_CfprStorageInitiatorDn_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,2),_CfprStorageInitiatorDn_Type())
cfprStorageInitiatorDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorDn.setStatus(_A)
_CfprStorageInitiatorRn_Type=SnmpAdminString
_CfprStorageInitiatorRn_Object=MibTableColumn
cfprStorageInitiatorRn=_CfprStorageInitiatorRn_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,3),_CfprStorageInitiatorRn_Type())
cfprStorageInitiatorRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorRn.setStatus(_A)
_CfprStorageInitiatorDescr_Type=SnmpAdminString
_CfprStorageInitiatorDescr_Object=MibTableColumn
cfprStorageInitiatorDescr=_CfprStorageInitiatorDescr_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,4),_CfprStorageInitiatorDescr_Type())
cfprStorageInitiatorDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorDescr.setStatus(_A)
_CfprStorageInitiatorDuplicateTarget_Type=SnmpAdminString
_CfprStorageInitiatorDuplicateTarget_Object=MibTableColumn
cfprStorageInitiatorDuplicateTarget=_CfprStorageInitiatorDuplicateTarget_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,5),_CfprStorageInitiatorDuplicateTarget_Type())
cfprStorageInitiatorDuplicateTarget.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorDuplicateTarget.setStatus(_A)
_CfprStorageInitiatorIntId_Type=SnmpAdminString
_CfprStorageInitiatorIntId_Object=MibTableColumn
cfprStorageInitiatorIntId=_CfprStorageInitiatorIntId_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,6),_CfprStorageInitiatorIntId_Type())
cfprStorageInitiatorIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorIntId.setStatus(_A)
_CfprStorageInitiatorName_Type=SnmpAdminString
_CfprStorageInitiatorName_Object=MibTableColumn
cfprStorageInitiatorName=_CfprStorageInitiatorName_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,7),_CfprStorageInitiatorName_Type())
cfprStorageInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorName.setStatus(_A)
_CfprStorageInitiatorOperState_Type=CfprStorageOperState
_CfprStorageInitiatorOperState_Object=MibTableColumn
cfprStorageInitiatorOperState=_CfprStorageInitiatorOperState_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,8),_CfprStorageInitiatorOperState_Type())
cfprStorageInitiatorOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorOperState.setStatus(_A)
_CfprStorageInitiatorPolicyLevel_Type=Gauge32
_CfprStorageInitiatorPolicyLevel_Object=MibTableColumn
cfprStorageInitiatorPolicyLevel=_CfprStorageInitiatorPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,9),_CfprStorageInitiatorPolicyLevel_Type())
cfprStorageInitiatorPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorPolicyLevel.setStatus(_A)
_CfprStorageInitiatorPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageInitiatorPolicyOwner_Object=MibTableColumn
cfprStorageInitiatorPolicyOwner=_CfprStorageInitiatorPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,22,1,10),_CfprStorageInitiatorPolicyOwner_Type())
cfprStorageInitiatorPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageInitiatorPolicyOwner.setStatus(_A)
_CfprStorageItemTable_Object=MibTable
cfprStorageItemTable=_CfprStorageItemTable_Object((1,3,6,1,4,1,9,9,826,1,74,23))
if mibBuilder.loadTexts:cfprStorageItemTable.setStatus(_A)
_CfprStorageItemEntry_Object=MibTableRow
cfprStorageItemEntry=_CfprStorageItemEntry_Object((1,3,6,1,4,1,9,9,826,1,74,23,1))
cfprStorageItemEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cfprStorageItemEntry.setStatus(_A)
_CfprStorageItemInstanceId_Type=CfprManagedObjectId
_CfprStorageItemInstanceId_Object=MibTableColumn
cfprStorageItemInstanceId=_CfprStorageItemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,1),_CfprStorageItemInstanceId_Type())
cfprStorageItemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageItemInstanceId.setStatus(_A)
_CfprStorageItemDn_Type=CfprManagedObjectDn
_CfprStorageItemDn_Object=MibTableColumn
cfprStorageItemDn=_CfprStorageItemDn_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,2),_CfprStorageItemDn_Type())
cfprStorageItemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemDn.setStatus(_A)
_CfprStorageItemRn_Type=SnmpAdminString
_CfprStorageItemRn_Object=MibTableColumn
cfprStorageItemRn=_CfprStorageItemRn_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,3),_CfprStorageItemRn_Type())
cfprStorageItemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemRn.setStatus(_A)
_CfprStorageItemName_Type=SnmpAdminString
_CfprStorageItemName_Object=MibTableColumn
cfprStorageItemName=_CfprStorageItemName_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,4),_CfprStorageItemName_Type())
cfprStorageItemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemName.setStatus(_A)
_CfprStorageItemOperState_Type=CfprStorageFileSystemStatus
_CfprStorageItemOperState_Object=MibTableColumn
cfprStorageItemOperState=_CfprStorageItemOperState_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,5),_CfprStorageItemOperState_Type())
cfprStorageItemOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemOperState.setStatus(_A)
_CfprStorageItemSize_Type=Unsigned64
_CfprStorageItemSize_Object=MibTableColumn
cfprStorageItemSize=_CfprStorageItemSize_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,6),_CfprStorageItemSize_Type())
cfprStorageItemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemSize.setStatus(_A)
_CfprStorageItemUsed_Type=Gauge32
_CfprStorageItemUsed_Object=MibTableColumn
cfprStorageItemUsed=_CfprStorageItemUsed_Object((1,3,6,1,4,1,9,9,826,1,74,23,1,7),_CfprStorageItemUsed_Type())
cfprStorageItemUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageItemUsed.setStatus(_A)
_CfprStorageLocalDiskTable_Object=MibTable
cfprStorageLocalDiskTable=_CfprStorageLocalDiskTable_Object((1,3,6,1,4,1,9,9,826,1,74,24))
if mibBuilder.loadTexts:cfprStorageLocalDiskTable.setStatus(_A)
_CfprStorageLocalDiskEntry_Object=MibTableRow
cfprStorageLocalDiskEntry=_CfprStorageLocalDiskEntry_Object((1,3,6,1,4,1,9,9,826,1,74,24,1))
cfprStorageLocalDiskEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cfprStorageLocalDiskEntry.setStatus(_A)
_CfprStorageLocalDiskInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalDiskInstanceId_Object=MibTableColumn
cfprStorageLocalDiskInstanceId=_CfprStorageLocalDiskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,1),_CfprStorageLocalDiskInstanceId_Type())
cfprStorageLocalDiskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalDiskInstanceId.setStatus(_A)
_CfprStorageLocalDiskDn_Type=CfprManagedObjectDn
_CfprStorageLocalDiskDn_Object=MibTableColumn
cfprStorageLocalDiskDn=_CfprStorageLocalDiskDn_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,2),_CfprStorageLocalDiskDn_Type())
cfprStorageLocalDiskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskDn.setStatus(_A)
_CfprStorageLocalDiskRn_Type=SnmpAdminString
_CfprStorageLocalDiskRn_Object=MibTableColumn
cfprStorageLocalDiskRn=_CfprStorageLocalDiskRn_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,3),_CfprStorageLocalDiskRn_Type())
cfprStorageLocalDiskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskRn.setStatus(_A)
_CfprStorageLocalDiskBlockSize_Type=Gauge32
_CfprStorageLocalDiskBlockSize_Object=MibTableColumn
cfprStorageLocalDiskBlockSize=_CfprStorageLocalDiskBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,4),_CfprStorageLocalDiskBlockSize_Type())
cfprStorageLocalDiskBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskBlockSize.setStatus(_A)
_CfprStorageLocalDiskConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageLocalDiskConnectionProtocol_Object=MibTableColumn
cfprStorageLocalDiskConnectionProtocol=_CfprStorageLocalDiskConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,5),_CfprStorageLocalDiskConnectionProtocol_Type())
cfprStorageLocalDiskConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConnectionProtocol.setStatus(_A)
_CfprStorageLocalDiskDeviceType_Type=CfprStorageTechnology
_CfprStorageLocalDiskDeviceType_Object=MibTableColumn
cfprStorageLocalDiskDeviceType=_CfprStorageLocalDiskDeviceType_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,6),_CfprStorageLocalDiskDeviceType_Type())
cfprStorageLocalDiskDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskDeviceType.setStatus(_A)
_CfprStorageLocalDiskDiskState_Type=CfprStoragePDriveStatus
_CfprStorageLocalDiskDiskState_Object=MibTableColumn
cfprStorageLocalDiskDiskState=_CfprStorageLocalDiskDiskState_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,7),_CfprStorageLocalDiskDiskState_Type())
cfprStorageLocalDiskDiskState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskDiskState.setStatus(_A)
_CfprStorageLocalDiskId_Type=Gauge32
_CfprStorageLocalDiskId_Object=MibTableColumn
cfprStorageLocalDiskId=_CfprStorageLocalDiskId_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,8),_CfprStorageLocalDiskId_Type())
cfprStorageLocalDiskId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskId.setStatus(_A)
_CfprStorageLocalDiskLc_Type=CfprFsmLifecycle
_CfprStorageLocalDiskLc_Object=MibTableColumn
cfprStorageLocalDiskLc=_CfprStorageLocalDiskLc_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,9),_CfprStorageLocalDiskLc_Type())
cfprStorageLocalDiskLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskLc.setStatus(_A)
_CfprStorageLocalDiskLinkSpeed_Type=CfprStorageLinkSpeed
_CfprStorageLocalDiskLinkSpeed_Object=MibTableColumn
cfprStorageLocalDiskLinkSpeed=_CfprStorageLocalDiskLinkSpeed_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,10),_CfprStorageLocalDiskLinkSpeed_Type())
cfprStorageLocalDiskLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskLinkSpeed.setStatus(_A)
_CfprStorageLocalDiskModel_Type=SnmpAdminString
_CfprStorageLocalDiskModel_Object=MibTableColumn
cfprStorageLocalDiskModel=_CfprStorageLocalDiskModel_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,11),_CfprStorageLocalDiskModel_Type())
cfprStorageLocalDiskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskModel.setStatus(_A)
_CfprStorageLocalDiskNumberOfBlocks_Type=Unsigned64
_CfprStorageLocalDiskNumberOfBlocks_Object=MibTableColumn
cfprStorageLocalDiskNumberOfBlocks=_CfprStorageLocalDiskNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,12),_CfprStorageLocalDiskNumberOfBlocks_Type())
cfprStorageLocalDiskNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskNumberOfBlocks.setStatus(_A)
_CfprStorageLocalDiskOperQualifierReason_Type=SnmpAdminString
_CfprStorageLocalDiskOperQualifierReason_Object=MibTableColumn
cfprStorageLocalDiskOperQualifierReason=_CfprStorageLocalDiskOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,13),_CfprStorageLocalDiskOperQualifierReason_Type())
cfprStorageLocalDiskOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskOperQualifierReason.setStatus(_A)
_CfprStorageLocalDiskOperability_Type=CfprEquipmentOperability
_CfprStorageLocalDiskOperability_Object=MibTableColumn
cfprStorageLocalDiskOperability=_CfprStorageLocalDiskOperability_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,14),_CfprStorageLocalDiskOperability_Type())
cfprStorageLocalDiskOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskOperability.setStatus(_A)
_CfprStorageLocalDiskPowerState_Type=CfprStoragePowerState
_CfprStorageLocalDiskPowerState_Object=MibTableColumn
cfprStorageLocalDiskPowerState=_CfprStorageLocalDiskPowerState_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,15),_CfprStorageLocalDiskPowerState_Type())
cfprStorageLocalDiskPowerState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPowerState.setStatus(_A)
_CfprStorageLocalDiskPresence_Type=CfprEquipmentPresence
_CfprStorageLocalDiskPresence_Object=MibTableColumn
cfprStorageLocalDiskPresence=_CfprStorageLocalDiskPresence_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,16),_CfprStorageLocalDiskPresence_Type())
cfprStorageLocalDiskPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPresence.setStatus(_A)
_CfprStorageLocalDiskRevision_Type=SnmpAdminString
_CfprStorageLocalDiskRevision_Object=MibTableColumn
cfprStorageLocalDiskRevision=_CfprStorageLocalDiskRevision_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,17),_CfprStorageLocalDiskRevision_Type())
cfprStorageLocalDiskRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskRevision.setStatus(_A)
_CfprStorageLocalDiskSerial_Type=SnmpAdminString
_CfprStorageLocalDiskSerial_Object=MibTableColumn
cfprStorageLocalDiskSerial=_CfprStorageLocalDiskSerial_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,18),_CfprStorageLocalDiskSerial_Type())
cfprStorageLocalDiskSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSerial.setStatus(_A)
_CfprStorageLocalDiskSize_Type=Unsigned64
_CfprStorageLocalDiskSize_Object=MibTableColumn
cfprStorageLocalDiskSize=_CfprStorageLocalDiskSize_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,19),_CfprStorageLocalDiskSize_Type())
cfprStorageLocalDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSize.setStatus(_A)
_CfprStorageLocalDiskVendor_Type=SnmpAdminString
_CfprStorageLocalDiskVendor_Object=MibTableColumn
cfprStorageLocalDiskVendor=_CfprStorageLocalDiskVendor_Object((1,3,6,1,4,1,9,9,826,1,74,24,1,20),_CfprStorageLocalDiskVendor_Type())
cfprStorageLocalDiskVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskVendor.setStatus(_A)
_CfprStorageLocalDiskConfigDefTable_Object=MibTable
cfprStorageLocalDiskConfigDefTable=_CfprStorageLocalDiskConfigDefTable_Object((1,3,6,1,4,1,9,9,826,1,74,25))
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefTable.setStatus(_A)
_CfprStorageLocalDiskConfigDefEntry_Object=MibTableRow
cfprStorageLocalDiskConfigDefEntry=_CfprStorageLocalDiskConfigDefEntry_Object((1,3,6,1,4,1,9,9,826,1,74,25,1))
cfprStorageLocalDiskConfigDefEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefEntry.setStatus(_A)
_CfprStorageLocalDiskConfigDefInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalDiskConfigDefInstanceId_Object=MibTableColumn
cfprStorageLocalDiskConfigDefInstanceId=_CfprStorageLocalDiskConfigDefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,1),_CfprStorageLocalDiskConfigDefInstanceId_Type())
cfprStorageLocalDiskConfigDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefInstanceId.setStatus(_A)
_CfprStorageLocalDiskConfigDefDn_Type=CfprManagedObjectDn
_CfprStorageLocalDiskConfigDefDn_Object=MibTableColumn
cfprStorageLocalDiskConfigDefDn=_CfprStorageLocalDiskConfigDefDn_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,2),_CfprStorageLocalDiskConfigDefDn_Type())
cfprStorageLocalDiskConfigDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefDn.setStatus(_A)
_CfprStorageLocalDiskConfigDefRn_Type=SnmpAdminString
_CfprStorageLocalDiskConfigDefRn_Object=MibTableColumn
cfprStorageLocalDiskConfigDefRn=_CfprStorageLocalDiskConfigDefRn_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,3),_CfprStorageLocalDiskConfigDefRn_Type())
cfprStorageLocalDiskConfigDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefRn.setStatus(_A)
_CfprStorageLocalDiskConfigDefDescr_Type=SnmpAdminString
_CfprStorageLocalDiskConfigDefDescr_Object=MibTableColumn
cfprStorageLocalDiskConfigDefDescr=_CfprStorageLocalDiskConfigDefDescr_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,4),_CfprStorageLocalDiskConfigDefDescr_Type())
cfprStorageLocalDiskConfigDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefDescr.setStatus(_A)
_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type=CfprStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object=MibTableColumn
cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState=_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,5),_CfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState_Type())
cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState.setStatus(_A)
_CfprStorageLocalDiskConfigDefFlexFlashState_Type=CfprStorageLocalDiskConfigFlexFlashState
_CfprStorageLocalDiskConfigDefFlexFlashState_Object=MibTableColumn
cfprStorageLocalDiskConfigDefFlexFlashState=_CfprStorageLocalDiskConfigDefFlexFlashState_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,6),_CfprStorageLocalDiskConfigDefFlexFlashState_Type())
cfprStorageLocalDiskConfigDefFlexFlashState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefFlexFlashState.setStatus(_A)
_CfprStorageLocalDiskConfigDefIntId_Type=SnmpAdminString
_CfprStorageLocalDiskConfigDefIntId_Object=MibTableColumn
cfprStorageLocalDiskConfigDefIntId=_CfprStorageLocalDiskConfigDefIntId_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,7),_CfprStorageLocalDiskConfigDefIntId_Type())
cfprStorageLocalDiskConfigDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefIntId.setStatus(_A)
_CfprStorageLocalDiskConfigDefMode_Type=CfprStorageLocalDiskMode
_CfprStorageLocalDiskConfigDefMode_Object=MibTableColumn
cfprStorageLocalDiskConfigDefMode=_CfprStorageLocalDiskConfigDefMode_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,8),_CfprStorageLocalDiskConfigDefMode_Type())
cfprStorageLocalDiskConfigDefMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefMode.setStatus(_A)
_CfprStorageLocalDiskConfigDefName_Type=SnmpAdminString
_CfprStorageLocalDiskConfigDefName_Object=MibTableColumn
cfprStorageLocalDiskConfigDefName=_CfprStorageLocalDiskConfigDefName_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,9),_CfprStorageLocalDiskConfigDefName_Type())
cfprStorageLocalDiskConfigDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefName.setStatus(_A)
_CfprStorageLocalDiskConfigDefPolicyLevel_Type=Gauge32
_CfprStorageLocalDiskConfigDefPolicyLevel_Object=MibTableColumn
cfprStorageLocalDiskConfigDefPolicyLevel=_CfprStorageLocalDiskConfigDefPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,10),_CfprStorageLocalDiskConfigDefPolicyLevel_Type())
cfprStorageLocalDiskConfigDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefPolicyLevel.setStatus(_A)
_CfprStorageLocalDiskConfigDefPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageLocalDiskConfigDefPolicyOwner_Object=MibTableColumn
cfprStorageLocalDiskConfigDefPolicyOwner=_CfprStorageLocalDiskConfigDefPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,11),_CfprStorageLocalDiskConfigDefPolicyOwner_Type())
cfprStorageLocalDiskConfigDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefPolicyOwner.setStatus(_A)
_CfprStorageLocalDiskConfigDefProtectConfig_Type=TruthValue
_CfprStorageLocalDiskConfigDefProtectConfig_Object=MibTableColumn
cfprStorageLocalDiskConfigDefProtectConfig=_CfprStorageLocalDiskConfigDefProtectConfig_Object((1,3,6,1,4,1,9,9,826,1,74,25,1,12),_CfprStorageLocalDiskConfigDefProtectConfig_Type())
cfprStorageLocalDiskConfigDefProtectConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigDefProtectConfig.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyTable_Object=MibTable
cfprStorageLocalDiskConfigPolicyTable=_CfprStorageLocalDiskConfigPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,74,26))
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyTable.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyEntry_Object=MibTableRow
cfprStorageLocalDiskConfigPolicyEntry=_CfprStorageLocalDiskConfigPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,74,26,1))
cfprStorageLocalDiskConfigPolicyEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyEntry.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalDiskConfigPolicyInstanceId_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyInstanceId=_CfprStorageLocalDiskConfigPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,1),_CfprStorageLocalDiskConfigPolicyInstanceId_Type())
cfprStorageLocalDiskConfigPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyInstanceId.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyDn_Type=CfprManagedObjectDn
_CfprStorageLocalDiskConfigPolicyDn_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyDn=_CfprStorageLocalDiskConfigPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,2),_CfprStorageLocalDiskConfigPolicyDn_Type())
cfprStorageLocalDiskConfigPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyDn.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyRn_Type=SnmpAdminString
_CfprStorageLocalDiskConfigPolicyRn_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyRn=_CfprStorageLocalDiskConfigPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,3),_CfprStorageLocalDiskConfigPolicyRn_Type())
cfprStorageLocalDiskConfigPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyRn.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyDescr_Type=SnmpAdminString
_CfprStorageLocalDiskConfigPolicyDescr_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyDescr=_CfprStorageLocalDiskConfigPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,4),_CfprStorageLocalDiskConfigPolicyDescr_Type())
cfprStorageLocalDiskConfigPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyDescr.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type=CfprStorageLocalDiskConfigFlexFlashRAIDReportingState
_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState=_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,5),_CfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState_Type())
cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyFlexFlashState_Type=CfprStorageLocalDiskConfigFlexFlashState
_CfprStorageLocalDiskConfigPolicyFlexFlashState_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyFlexFlashState=_CfprStorageLocalDiskConfigPolicyFlexFlashState_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,6),_CfprStorageLocalDiskConfigPolicyFlexFlashState_Type())
cfprStorageLocalDiskConfigPolicyFlexFlashState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyFlexFlashState.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyIntId_Type=SnmpAdminString
_CfprStorageLocalDiskConfigPolicyIntId_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyIntId=_CfprStorageLocalDiskConfigPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,7),_CfprStorageLocalDiskConfigPolicyIntId_Type())
cfprStorageLocalDiskConfigPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyIntId.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyMode_Type=CfprStorageLocalDiskMode
_CfprStorageLocalDiskConfigPolicyMode_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyMode=_CfprStorageLocalDiskConfigPolicyMode_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,8),_CfprStorageLocalDiskConfigPolicyMode_Type())
cfprStorageLocalDiskConfigPolicyMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyMode.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyName_Type=SnmpAdminString
_CfprStorageLocalDiskConfigPolicyName_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyName=_CfprStorageLocalDiskConfigPolicyName_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,9),_CfprStorageLocalDiskConfigPolicyName_Type())
cfprStorageLocalDiskConfigPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyName.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyPolicyLevel_Type=Gauge32
_CfprStorageLocalDiskConfigPolicyPolicyLevel_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyPolicyLevel=_CfprStorageLocalDiskConfigPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,10),_CfprStorageLocalDiskConfigPolicyPolicyLevel_Type())
cfprStorageLocalDiskConfigPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyPolicyLevel.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageLocalDiskConfigPolicyPolicyOwner_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyPolicyOwner=_CfprStorageLocalDiskConfigPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,11),_CfprStorageLocalDiskConfigPolicyPolicyOwner_Type())
cfprStorageLocalDiskConfigPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyPolicyOwner.setStatus(_A)
_CfprStorageLocalDiskConfigPolicyProtectConfig_Type=TruthValue
_CfprStorageLocalDiskConfigPolicyProtectConfig_Object=MibTableColumn
cfprStorageLocalDiskConfigPolicyProtectConfig=_CfprStorageLocalDiskConfigPolicyProtectConfig_Object((1,3,6,1,4,1,9,9,826,1,74,26,1,12),_CfprStorageLocalDiskConfigPolicyProtectConfig_Type())
cfprStorageLocalDiskConfigPolicyProtectConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskConfigPolicyProtectConfig.setStatus(_A)
_CfprStorageLocalDiskPartitionTable_Object=MibTable
cfprStorageLocalDiskPartitionTable=_CfprStorageLocalDiskPartitionTable_Object((1,3,6,1,4,1,9,9,826,1,74,27))
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionTable.setStatus(_A)
_CfprStorageLocalDiskPartitionEntry_Object=MibTableRow
cfprStorageLocalDiskPartitionEntry=_CfprStorageLocalDiskPartitionEntry_Object((1,3,6,1,4,1,9,9,826,1,74,27,1))
cfprStorageLocalDiskPartitionEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionEntry.setStatus(_A)
_CfprStorageLocalDiskPartitionInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalDiskPartitionInstanceId_Object=MibTableColumn
cfprStorageLocalDiskPartitionInstanceId=_CfprStorageLocalDiskPartitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,1),_CfprStorageLocalDiskPartitionInstanceId_Type())
cfprStorageLocalDiskPartitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionInstanceId.setStatus(_A)
_CfprStorageLocalDiskPartitionDn_Type=CfprManagedObjectDn
_CfprStorageLocalDiskPartitionDn_Object=MibTableColumn
cfprStorageLocalDiskPartitionDn=_CfprStorageLocalDiskPartitionDn_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,2),_CfprStorageLocalDiskPartitionDn_Type())
cfprStorageLocalDiskPartitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionDn.setStatus(_A)
_CfprStorageLocalDiskPartitionRn_Type=SnmpAdminString
_CfprStorageLocalDiskPartitionRn_Object=MibTableColumn
cfprStorageLocalDiskPartitionRn=_CfprStorageLocalDiskPartitionRn_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,3),_CfprStorageLocalDiskPartitionRn_Type())
cfprStorageLocalDiskPartitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionRn.setStatus(_A)
_CfprStorageLocalDiskPartitionDescr_Type=SnmpAdminString
_CfprStorageLocalDiskPartitionDescr_Object=MibTableColumn
cfprStorageLocalDiskPartitionDescr=_CfprStorageLocalDiskPartitionDescr_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,4),_CfprStorageLocalDiskPartitionDescr_Type())
cfprStorageLocalDiskPartitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionDescr.setStatus(_A)
_CfprStorageLocalDiskPartitionIntId_Type=SnmpAdminString
_CfprStorageLocalDiskPartitionIntId_Object=MibTableColumn
cfprStorageLocalDiskPartitionIntId=_CfprStorageLocalDiskPartitionIntId_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,5),_CfprStorageLocalDiskPartitionIntId_Type())
cfprStorageLocalDiskPartitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionIntId.setStatus(_A)
_CfprStorageLocalDiskPartitionName_Type=SnmpAdminString
_CfprStorageLocalDiskPartitionName_Object=MibTableColumn
cfprStorageLocalDiskPartitionName=_CfprStorageLocalDiskPartitionName_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,6),_CfprStorageLocalDiskPartitionName_Type())
cfprStorageLocalDiskPartitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionName.setStatus(_A)
_CfprStorageLocalDiskPartitionOrder_Type=Gauge32
_CfprStorageLocalDiskPartitionOrder_Object=MibTableColumn
cfprStorageLocalDiskPartitionOrder=_CfprStorageLocalDiskPartitionOrder_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,7),_CfprStorageLocalDiskPartitionOrder_Type())
cfprStorageLocalDiskPartitionOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionOrder.setStatus(_A)
_CfprStorageLocalDiskPartitionPolicyLevel_Type=Gauge32
_CfprStorageLocalDiskPartitionPolicyLevel_Object=MibTableColumn
cfprStorageLocalDiskPartitionPolicyLevel=_CfprStorageLocalDiskPartitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,8),_CfprStorageLocalDiskPartitionPolicyLevel_Type())
cfprStorageLocalDiskPartitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionPolicyLevel.setStatus(_A)
_CfprStorageLocalDiskPartitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprStorageLocalDiskPartitionPolicyOwner_Object=MibTableColumn
cfprStorageLocalDiskPartitionPolicyOwner=_CfprStorageLocalDiskPartitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,9),_CfprStorageLocalDiskPartitionPolicyOwner_Type())
cfprStorageLocalDiskPartitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionPolicyOwner.setStatus(_A)
_CfprStorageLocalDiskPartitionSize_Type=Unsigned64
_CfprStorageLocalDiskPartitionSize_Object=MibTableColumn
cfprStorageLocalDiskPartitionSize=_CfprStorageLocalDiskPartitionSize_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,10),_CfprStorageLocalDiskPartitionSize_Type())
cfprStorageLocalDiskPartitionSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionSize.setStatus(_A)
_CfprStorageLocalDiskPartitionType_Type=CfprStorageLocalDiskPartitionType
_CfprStorageLocalDiskPartitionType_Object=MibTableColumn
cfprStorageLocalDiskPartitionType=_CfprStorageLocalDiskPartitionType_Object((1,3,6,1,4,1,9,9,826,1,74,27,1,11),_CfprStorageLocalDiskPartitionType_Type())
cfprStorageLocalDiskPartitionType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskPartitionType.setStatus(_A)
_CfprStorageLocalDiskSlotEpTable_Object=MibTable
cfprStorageLocalDiskSlotEpTable=_CfprStorageLocalDiskSlotEpTable_Object((1,3,6,1,4,1,9,9,826,1,74,28))
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpTable.setStatus(_A)
_CfprStorageLocalDiskSlotEpEntry_Object=MibTableRow
cfprStorageLocalDiskSlotEpEntry=_CfprStorageLocalDiskSlotEpEntry_Object((1,3,6,1,4,1,9,9,826,1,74,28,1))
cfprStorageLocalDiskSlotEpEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpEntry.setStatus(_A)
_CfprStorageLocalDiskSlotEpInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalDiskSlotEpInstanceId_Object=MibTableColumn
cfprStorageLocalDiskSlotEpInstanceId=_CfprStorageLocalDiskSlotEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,1),_CfprStorageLocalDiskSlotEpInstanceId_Type())
cfprStorageLocalDiskSlotEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpInstanceId.setStatus(_A)
_CfprStorageLocalDiskSlotEpDn_Type=CfprManagedObjectDn
_CfprStorageLocalDiskSlotEpDn_Object=MibTableColumn
cfprStorageLocalDiskSlotEpDn=_CfprStorageLocalDiskSlotEpDn_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,2),_CfprStorageLocalDiskSlotEpDn_Type())
cfprStorageLocalDiskSlotEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpDn.setStatus(_A)
_CfprStorageLocalDiskSlotEpRn_Type=SnmpAdminString
_CfprStorageLocalDiskSlotEpRn_Object=MibTableColumn
cfprStorageLocalDiskSlotEpRn=_CfprStorageLocalDiskSlotEpRn_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,3),_CfprStorageLocalDiskSlotEpRn_Type())
cfprStorageLocalDiskSlotEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpRn.setStatus(_A)
_CfprStorageLocalDiskSlotEpConfiguration_Type=CfprStorageConfiguration
_CfprStorageLocalDiskSlotEpConfiguration_Object=MibTableColumn
cfprStorageLocalDiskSlotEpConfiguration=_CfprStorageLocalDiskSlotEpConfiguration_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,4),_CfprStorageLocalDiskSlotEpConfiguration_Type())
cfprStorageLocalDiskSlotEpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpConfiguration.setStatus(_A)
_CfprStorageLocalDiskSlotEpId_Type=Gauge32
_CfprStorageLocalDiskSlotEpId_Object=MibTableColumn
cfprStorageLocalDiskSlotEpId=_CfprStorageLocalDiskSlotEpId_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,5),_CfprStorageLocalDiskSlotEpId_Type())
cfprStorageLocalDiskSlotEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpId.setStatus(_A)
_CfprStorageLocalDiskSlotEpOperQualifierReason_Type=SnmpAdminString
_CfprStorageLocalDiskSlotEpOperQualifierReason_Object=MibTableColumn
cfprStorageLocalDiskSlotEpOperQualifierReason=_CfprStorageLocalDiskSlotEpOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,6),_CfprStorageLocalDiskSlotEpOperQualifierReason_Type())
cfprStorageLocalDiskSlotEpOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpOperQualifierReason.setStatus(_A)
_CfprStorageLocalDiskSlotEpOperability_Type=CfprEquipmentOperability
_CfprStorageLocalDiskSlotEpOperability_Object=MibTableColumn
cfprStorageLocalDiskSlotEpOperability=_CfprStorageLocalDiskSlotEpOperability_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,7),_CfprStorageLocalDiskSlotEpOperability_Type())
cfprStorageLocalDiskSlotEpOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpOperability.setStatus(_A)
_CfprStorageLocalDiskSlotEpPeerDn_Type=SnmpAdminString
_CfprStorageLocalDiskSlotEpPeerDn_Object=MibTableColumn
cfprStorageLocalDiskSlotEpPeerDn=_CfprStorageLocalDiskSlotEpPeerDn_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,8),_CfprStorageLocalDiskSlotEpPeerDn_Type())
cfprStorageLocalDiskSlotEpPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpPeerDn.setStatus(_A)
_CfprStorageLocalDiskSlotEpPresence_Type=CfprEquipmentPresence
_CfprStorageLocalDiskSlotEpPresence_Object=MibTableColumn
cfprStorageLocalDiskSlotEpPresence=_CfprStorageLocalDiskSlotEpPresence_Object((1,3,6,1,4,1,9,9,826,1,74,28,1,9),_CfprStorageLocalDiskSlotEpPresence_Type())
cfprStorageLocalDiskSlotEpPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalDiskSlotEpPresence.setStatus(_A)
_CfprStorageLocalLunTable_Object=MibTable
cfprStorageLocalLunTable=_CfprStorageLocalLunTable_Object((1,3,6,1,4,1,9,9,826,1,74,29))
if mibBuilder.loadTexts:cfprStorageLocalLunTable.setStatus(_A)
_CfprStorageLocalLunEntry_Object=MibTableRow
cfprStorageLocalLunEntry=_CfprStorageLocalLunEntry_Object((1,3,6,1,4,1,9,9,826,1,74,29,1))
cfprStorageLocalLunEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cfprStorageLocalLunEntry.setStatus(_A)
_CfprStorageLocalLunInstanceId_Type=CfprManagedObjectId
_CfprStorageLocalLunInstanceId_Object=MibTableColumn
cfprStorageLocalLunInstanceId=_CfprStorageLocalLunInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,1),_CfprStorageLocalLunInstanceId_Type())
cfprStorageLocalLunInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLocalLunInstanceId.setStatus(_A)
_CfprStorageLocalLunDn_Type=CfprManagedObjectDn
_CfprStorageLocalLunDn_Object=MibTableColumn
cfprStorageLocalLunDn=_CfprStorageLocalLunDn_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,2),_CfprStorageLocalLunDn_Type())
cfprStorageLocalLunDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunDn.setStatus(_A)
_CfprStorageLocalLunRn_Type=SnmpAdminString
_CfprStorageLocalLunRn_Object=MibTableColumn
cfprStorageLocalLunRn=_CfprStorageLocalLunRn_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,3),_CfprStorageLocalLunRn_Type())
cfprStorageLocalLunRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunRn.setStatus(_A)
_CfprStorageLocalLunBlockSize_Type=Gauge32
_CfprStorageLocalLunBlockSize_Object=MibTableColumn
cfprStorageLocalLunBlockSize=_CfprStorageLocalLunBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,4),_CfprStorageLocalLunBlockSize_Type())
cfprStorageLocalLunBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunBlockSize.setStatus(_A)
_CfprStorageLocalLunConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageLocalLunConnectionProtocol_Object=MibTableColumn
cfprStorageLocalLunConnectionProtocol=_CfprStorageLocalLunConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,5),_CfprStorageLocalLunConnectionProtocol_Type())
cfprStorageLocalLunConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunConnectionProtocol.setStatus(_A)
_CfprStorageLocalLunId_Type=Gauge32
_CfprStorageLocalLunId_Object=MibTableColumn
cfprStorageLocalLunId=_CfprStorageLocalLunId_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,6),_CfprStorageLocalLunId_Type())
cfprStorageLocalLunId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunId.setStatus(_A)
_CfprStorageLocalLunLc_Type=CfprFsmLifecycle
_CfprStorageLocalLunLc_Object=MibTableColumn
cfprStorageLocalLunLc=_CfprStorageLocalLunLc_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,7),_CfprStorageLocalLunLc_Type())
cfprStorageLocalLunLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunLc.setStatus(_A)
_CfprStorageLocalLunModel_Type=SnmpAdminString
_CfprStorageLocalLunModel_Object=MibTableColumn
cfprStorageLocalLunModel=_CfprStorageLocalLunModel_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,8),_CfprStorageLocalLunModel_Type())
cfprStorageLocalLunModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunModel.setStatus(_A)
_CfprStorageLocalLunNumberOfBlocks_Type=Unsigned64
_CfprStorageLocalLunNumberOfBlocks_Object=MibTableColumn
cfprStorageLocalLunNumberOfBlocks=_CfprStorageLocalLunNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,9),_CfprStorageLocalLunNumberOfBlocks_Type())
cfprStorageLocalLunNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunNumberOfBlocks.setStatus(_A)
_CfprStorageLocalLunOperQualifierReason_Type=SnmpAdminString
_CfprStorageLocalLunOperQualifierReason_Object=MibTableColumn
cfprStorageLocalLunOperQualifierReason=_CfprStorageLocalLunOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,10),_CfprStorageLocalLunOperQualifierReason_Type())
cfprStorageLocalLunOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunOperQualifierReason.setStatus(_A)
_CfprStorageLocalLunOperability_Type=CfprEquipmentOperability
_CfprStorageLocalLunOperability_Object=MibTableColumn
cfprStorageLocalLunOperability=_CfprStorageLocalLunOperability_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,11),_CfprStorageLocalLunOperability_Type())
cfprStorageLocalLunOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunOperability.setStatus(_A)
_CfprStorageLocalLunPresence_Type=CfprEquipmentPresence
_CfprStorageLocalLunPresence_Object=MibTableColumn
cfprStorageLocalLunPresence=_CfprStorageLocalLunPresence_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,12),_CfprStorageLocalLunPresence_Type())
cfprStorageLocalLunPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunPresence.setStatus(_A)
_CfprStorageLocalLunRevision_Type=SnmpAdminString
_CfprStorageLocalLunRevision_Object=MibTableColumn
cfprStorageLocalLunRevision=_CfprStorageLocalLunRevision_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,13),_CfprStorageLocalLunRevision_Type())
cfprStorageLocalLunRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunRevision.setStatus(_A)
_CfprStorageLocalLunSerial_Type=SnmpAdminString
_CfprStorageLocalLunSerial_Object=MibTableColumn
cfprStorageLocalLunSerial=_CfprStorageLocalLunSerial_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,14),_CfprStorageLocalLunSerial_Type())
cfprStorageLocalLunSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunSerial.setStatus(_A)
_CfprStorageLocalLunSize_Type=Unsigned64
_CfprStorageLocalLunSize_Object=MibTableColumn
cfprStorageLocalLunSize=_CfprStorageLocalLunSize_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,15),_CfprStorageLocalLunSize_Type())
cfprStorageLocalLunSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunSize.setStatus(_A)
_CfprStorageLocalLunType_Type=CfprStorageLunType
_CfprStorageLocalLunType_Object=MibTableColumn
cfprStorageLocalLunType=_CfprStorageLocalLunType_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,16),_CfprStorageLocalLunType_Type())
cfprStorageLocalLunType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunType.setStatus(_A)
_CfprStorageLocalLunVendor_Type=SnmpAdminString
_CfprStorageLocalLunVendor_Object=MibTableColumn
cfprStorageLocalLunVendor=_CfprStorageLocalLunVendor_Object((1,3,6,1,4,1,9,9,826,1,74,29,1,17),_CfprStorageLocalLunVendor_Type())
cfprStorageLocalLunVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLocalLunVendor.setStatus(_A)
_CfprStorageLunDiskTable_Object=MibTable
cfprStorageLunDiskTable=_CfprStorageLunDiskTable_Object((1,3,6,1,4,1,9,9,826,1,74,30))
if mibBuilder.loadTexts:cfprStorageLunDiskTable.setStatus(_A)
_CfprStorageLunDiskEntry_Object=MibTableRow
cfprStorageLunDiskEntry=_CfprStorageLunDiskEntry_Object((1,3,6,1,4,1,9,9,826,1,74,30,1))
cfprStorageLunDiskEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cfprStorageLunDiskEntry.setStatus(_A)
_CfprStorageLunDiskInstanceId_Type=CfprManagedObjectId
_CfprStorageLunDiskInstanceId_Object=MibTableColumn
cfprStorageLunDiskInstanceId=_CfprStorageLunDiskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,30,1,1),_CfprStorageLunDiskInstanceId_Type())
cfprStorageLunDiskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageLunDiskInstanceId.setStatus(_A)
_CfprStorageLunDiskDn_Type=CfprManagedObjectDn
_CfprStorageLunDiskDn_Object=MibTableColumn
cfprStorageLunDiskDn=_CfprStorageLunDiskDn_Object((1,3,6,1,4,1,9,9,826,1,74,30,1,2),_CfprStorageLunDiskDn_Type())
cfprStorageLunDiskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLunDiskDn.setStatus(_A)
_CfprStorageLunDiskRn_Type=SnmpAdminString
_CfprStorageLunDiskRn_Object=MibTableColumn
cfprStorageLunDiskRn=_CfprStorageLunDiskRn_Object((1,3,6,1,4,1,9,9,826,1,74,30,1,3),_CfprStorageLunDiskRn_Type())
cfprStorageLunDiskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLunDiskRn.setStatus(_A)
_CfprStorageLunDiskId_Type=Gauge32
_CfprStorageLunDiskId_Object=MibTableColumn
cfprStorageLunDiskId=_CfprStorageLunDiskId_Object((1,3,6,1,4,1,9,9,826,1,74,30,1,4),_CfprStorageLunDiskId_Type())
cfprStorageLunDiskId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageLunDiskId.setStatus(_A)
_CfprStorageMezzFlashLifeTable_Object=MibTable
cfprStorageMezzFlashLifeTable=_CfprStorageMezzFlashLifeTable_Object((1,3,6,1,4,1,9,9,826,1,74,31))
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeTable.setStatus(_A)
_CfprStorageMezzFlashLifeEntry_Object=MibTableRow
cfprStorageMezzFlashLifeEntry=_CfprStorageMezzFlashLifeEntry_Object((1,3,6,1,4,1,9,9,826,1,74,31,1))
cfprStorageMezzFlashLifeEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeEntry.setStatus(_A)
_CfprStorageMezzFlashLifeInstanceId_Type=CfprManagedObjectId
_CfprStorageMezzFlashLifeInstanceId_Object=MibTableColumn
cfprStorageMezzFlashLifeInstanceId=_CfprStorageMezzFlashLifeInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,1),_CfprStorageMezzFlashLifeInstanceId_Type())
cfprStorageMezzFlashLifeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeInstanceId.setStatus(_A)
_CfprStorageMezzFlashLifeDn_Type=CfprManagedObjectDn
_CfprStorageMezzFlashLifeDn_Object=MibTableColumn
cfprStorageMezzFlashLifeDn=_CfprStorageMezzFlashLifeDn_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,2),_CfprStorageMezzFlashLifeDn_Type())
cfprStorageMezzFlashLifeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeDn.setStatus(_A)
_CfprStorageMezzFlashLifeRn_Type=SnmpAdminString
_CfprStorageMezzFlashLifeRn_Object=MibTableColumn
cfprStorageMezzFlashLifeRn=_CfprStorageMezzFlashLifeRn_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,3),_CfprStorageMezzFlashLifeRn_Type())
cfprStorageMezzFlashLifeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeRn.setStatus(_A)
_CfprStorageMezzFlashLifeBlockSize_Type=Gauge32
_CfprStorageMezzFlashLifeBlockSize_Object=MibTableColumn
cfprStorageMezzFlashLifeBlockSize=_CfprStorageMezzFlashLifeBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,4),_CfprStorageMezzFlashLifeBlockSize_Type())
cfprStorageMezzFlashLifeBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeBlockSize.setStatus(_A)
_CfprStorageMezzFlashLifeConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageMezzFlashLifeConnectionProtocol_Object=MibTableColumn
cfprStorageMezzFlashLifeConnectionProtocol=_CfprStorageMezzFlashLifeConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,5),_CfprStorageMezzFlashLifeConnectionProtocol_Type())
cfprStorageMezzFlashLifeConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeConnectionProtocol.setStatus(_A)
_CfprStorageMezzFlashLifeFlashPercentage_Type=SnmpAdminString
_CfprStorageMezzFlashLifeFlashPercentage_Object=MibTableColumn
cfprStorageMezzFlashLifeFlashPercentage=_CfprStorageMezzFlashLifeFlashPercentage_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,6),_CfprStorageMezzFlashLifeFlashPercentage_Type())
cfprStorageMezzFlashLifeFlashPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeFlashPercentage.setStatus(_A)
_CfprStorageMezzFlashLifeFlashStatus_Type=SnmpAdminString
_CfprStorageMezzFlashLifeFlashStatus_Object=MibTableColumn
cfprStorageMezzFlashLifeFlashStatus=_CfprStorageMezzFlashLifeFlashStatus_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,7),_CfprStorageMezzFlashLifeFlashStatus_Type())
cfprStorageMezzFlashLifeFlashStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeFlashStatus.setStatus(_A)
_CfprStorageMezzFlashLifeId_Type=Gauge32
_CfprStorageMezzFlashLifeId_Object=MibTableColumn
cfprStorageMezzFlashLifeId=_CfprStorageMezzFlashLifeId_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,8),_CfprStorageMezzFlashLifeId_Type())
cfprStorageMezzFlashLifeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeId.setStatus(_A)
_CfprStorageMezzFlashLifeModel_Type=SnmpAdminString
_CfprStorageMezzFlashLifeModel_Object=MibTableColumn
cfprStorageMezzFlashLifeModel=_CfprStorageMezzFlashLifeModel_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,9),_CfprStorageMezzFlashLifeModel_Type())
cfprStorageMezzFlashLifeModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeModel.setStatus(_A)
_CfprStorageMezzFlashLifeNumberOfBlocks_Type=Unsigned64
_CfprStorageMezzFlashLifeNumberOfBlocks_Object=MibTableColumn
cfprStorageMezzFlashLifeNumberOfBlocks=_CfprStorageMezzFlashLifeNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,10),_CfprStorageMezzFlashLifeNumberOfBlocks_Type())
cfprStorageMezzFlashLifeNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeNumberOfBlocks.setStatus(_A)
_CfprStorageMezzFlashLifeOperQualifierReason_Type=SnmpAdminString
_CfprStorageMezzFlashLifeOperQualifierReason_Object=MibTableColumn
cfprStorageMezzFlashLifeOperQualifierReason=_CfprStorageMezzFlashLifeOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,11),_CfprStorageMezzFlashLifeOperQualifierReason_Type())
cfprStorageMezzFlashLifeOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeOperQualifierReason.setStatus(_A)
_CfprStorageMezzFlashLifeOperability_Type=CfprEquipmentOperability
_CfprStorageMezzFlashLifeOperability_Object=MibTableColumn
cfprStorageMezzFlashLifeOperability=_CfprStorageMezzFlashLifeOperability_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,12),_CfprStorageMezzFlashLifeOperability_Type())
cfprStorageMezzFlashLifeOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeOperability.setStatus(_A)
_CfprStorageMezzFlashLifePresence_Type=CfprEquipmentPresence
_CfprStorageMezzFlashLifePresence_Object=MibTableColumn
cfprStorageMezzFlashLifePresence=_CfprStorageMezzFlashLifePresence_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,13),_CfprStorageMezzFlashLifePresence_Type())
cfprStorageMezzFlashLifePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifePresence.setStatus(_A)
_CfprStorageMezzFlashLifeRevision_Type=SnmpAdminString
_CfprStorageMezzFlashLifeRevision_Object=MibTableColumn
cfprStorageMezzFlashLifeRevision=_CfprStorageMezzFlashLifeRevision_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,14),_CfprStorageMezzFlashLifeRevision_Type())
cfprStorageMezzFlashLifeRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeRevision.setStatus(_A)
_CfprStorageMezzFlashLifeSerial_Type=SnmpAdminString
_CfprStorageMezzFlashLifeSerial_Object=MibTableColumn
cfprStorageMezzFlashLifeSerial=_CfprStorageMezzFlashLifeSerial_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,15),_CfprStorageMezzFlashLifeSerial_Type())
cfprStorageMezzFlashLifeSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeSerial.setStatus(_A)
_CfprStorageMezzFlashLifeSize_Type=Unsigned64
_CfprStorageMezzFlashLifeSize_Object=MibTableColumn
cfprStorageMezzFlashLifeSize=_CfprStorageMezzFlashLifeSize_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,16),_CfprStorageMezzFlashLifeSize_Type())
cfprStorageMezzFlashLifeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeSize.setStatus(_A)
_CfprStorageMezzFlashLifeVendor_Type=SnmpAdminString
_CfprStorageMezzFlashLifeVendor_Object=MibTableColumn
cfprStorageMezzFlashLifeVendor=_CfprStorageMezzFlashLifeVendor_Object((1,3,6,1,4,1,9,9,826,1,74,31,1,17),_CfprStorageMezzFlashLifeVendor_Type())
cfprStorageMezzFlashLifeVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageMezzFlashLifeVendor.setStatus(_A)
_CfprStorageNodeEpTable_Object=MibTable
cfprStorageNodeEpTable=_CfprStorageNodeEpTable_Object((1,3,6,1,4,1,9,9,826,1,74,32))
if mibBuilder.loadTexts:cfprStorageNodeEpTable.setStatus(_A)
_CfprStorageNodeEpEntry_Object=MibTableRow
cfprStorageNodeEpEntry=_CfprStorageNodeEpEntry_Object((1,3,6,1,4,1,9,9,826,1,74,32,1))
cfprStorageNodeEpEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:cfprStorageNodeEpEntry.setStatus(_A)
_CfprStorageNodeEpInstanceId_Type=CfprManagedObjectId
_CfprStorageNodeEpInstanceId_Object=MibTableColumn
cfprStorageNodeEpInstanceId=_CfprStorageNodeEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,32,1,1),_CfprStorageNodeEpInstanceId_Type())
cfprStorageNodeEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageNodeEpInstanceId.setStatus(_A)
_CfprStorageNodeEpDn_Type=CfprManagedObjectDn
_CfprStorageNodeEpDn_Object=MibTableColumn
cfprStorageNodeEpDn=_CfprStorageNodeEpDn_Object((1,3,6,1,4,1,9,9,826,1,74,32,1,2),_CfprStorageNodeEpDn_Type())
cfprStorageNodeEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageNodeEpDn.setStatus(_A)
_CfprStorageNodeEpRn_Type=SnmpAdminString
_CfprStorageNodeEpRn_Object=MibTableColumn
cfprStorageNodeEpRn=_CfprStorageNodeEpRn_Object((1,3,6,1,4,1,9,9,826,1,74,32,1,3),_CfprStorageNodeEpRn_Type())
cfprStorageNodeEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageNodeEpRn.setStatus(_A)
_CfprStorageNodeEpEpDn_Type=SnmpAdminString
_CfprStorageNodeEpEpDn_Object=MibTableColumn
cfprStorageNodeEpEpDn=_CfprStorageNodeEpEpDn_Object((1,3,6,1,4,1,9,9,826,1,74,32,1,4),_CfprStorageNodeEpEpDn_Type())
cfprStorageNodeEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageNodeEpEpDn.setStatus(_A)
_CfprStorageNodeEpId_Type=Gauge32
_CfprStorageNodeEpId_Object=MibTableColumn
cfprStorageNodeEpId=_CfprStorageNodeEpId_Object((1,3,6,1,4,1,9,9,826,1,74,32,1,5),_CfprStorageNodeEpId_Type())
cfprStorageNodeEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageNodeEpId.setStatus(_A)
_CfprStorageOperationTable_Object=MibTable
cfprStorageOperationTable=_CfprStorageOperationTable_Object((1,3,6,1,4,1,9,9,826,1,74,33))
if mibBuilder.loadTexts:cfprStorageOperationTable.setStatus(_A)
_CfprStorageOperationEntry_Object=MibTableRow
cfprStorageOperationEntry=_CfprStorageOperationEntry_Object((1,3,6,1,4,1,9,9,826,1,74,33,1))
cfprStorageOperationEntry.setIndexNames((0,_C,_k))
if mibBuilder.loadTexts:cfprStorageOperationEntry.setStatus(_A)
_CfprStorageOperationInstanceId_Type=CfprManagedObjectId
_CfprStorageOperationInstanceId_Object=MibTableColumn
cfprStorageOperationInstanceId=_CfprStorageOperationInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,1),_CfprStorageOperationInstanceId_Type())
cfprStorageOperationInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageOperationInstanceId.setStatus(_A)
_CfprStorageOperationDn_Type=CfprManagedObjectDn
_CfprStorageOperationDn_Object=MibTableColumn
cfprStorageOperationDn=_CfprStorageOperationDn_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,2),_CfprStorageOperationDn_Type())
cfprStorageOperationDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationDn.setStatus(_A)
_CfprStorageOperationRn_Type=SnmpAdminString
_CfprStorageOperationRn_Object=MibTableColumn
cfprStorageOperationRn=_CfprStorageOperationRn_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,3),_CfprStorageOperationRn_Type())
cfprStorageOperationRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationRn.setStatus(_A)
_CfprStorageOperationEndTime_Type=DateAndTime
_CfprStorageOperationEndTime_Object=MibTableColumn
cfprStorageOperationEndTime=_CfprStorageOperationEndTime_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,4),_CfprStorageOperationEndTime_Type())
cfprStorageOperationEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationEndTime.setStatus(_A)
_CfprStorageOperationName_Type=CfprStorageOperationType
_CfprStorageOperationName_Object=MibTableColumn
cfprStorageOperationName=_CfprStorageOperationName_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,5),_CfprStorageOperationName_Type())
cfprStorageOperationName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationName.setStatus(_A)
_CfprStorageOperationOperState_Type=CfprStorageOperationState
_CfprStorageOperationOperState_Object=MibTableColumn
cfprStorageOperationOperState=_CfprStorageOperationOperState_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,6),_CfprStorageOperationOperState_Type())
cfprStorageOperationOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationOperState.setStatus(_A)
_CfprStorageOperationProgress_Type=Gauge32
_CfprStorageOperationProgress_Object=MibTableColumn
cfprStorageOperationProgress=_CfprStorageOperationProgress_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,7),_CfprStorageOperationProgress_Type())
cfprStorageOperationProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationProgress.setStatus(_A)
_CfprStorageOperationStartTime_Type=DateAndTime
_CfprStorageOperationStartTime_Object=MibTableColumn
cfprStorageOperationStartTime=_CfprStorageOperationStartTime_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,8),_CfprStorageOperationStartTime_Type())
cfprStorageOperationStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationStartTime.setStatus(_A)
_CfprStorageOperationStatusDescr_Type=SnmpAdminString
_CfprStorageOperationStatusDescr_Object=MibTableColumn
cfprStorageOperationStatusDescr=_CfprStorageOperationStatusDescr_Object((1,3,6,1,4,1,9,9,826,1,74,33,1,9),_CfprStorageOperationStatusDescr_Type())
cfprStorageOperationStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageOperationStatusDescr.setStatus(_A)
_CfprStorageQualTable_Object=MibTable
cfprStorageQualTable=_CfprStorageQualTable_Object((1,3,6,1,4,1,9,9,826,1,74,34))
if mibBuilder.loadTexts:cfprStorageQualTable.setStatus(_A)
_CfprStorageQualEntry_Object=MibTableRow
cfprStorageQualEntry=_CfprStorageQualEntry_Object((1,3,6,1,4,1,9,9,826,1,74,34,1))
cfprStorageQualEntry.setIndexNames((0,_C,_l))
if mibBuilder.loadTexts:cfprStorageQualEntry.setStatus(_A)
_CfprStorageQualInstanceId_Type=CfprManagedObjectId
_CfprStorageQualInstanceId_Object=MibTableColumn
cfprStorageQualInstanceId=_CfprStorageQualInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,1),_CfprStorageQualInstanceId_Type())
cfprStorageQualInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageQualInstanceId.setStatus(_A)
_CfprStorageQualDn_Type=CfprManagedObjectDn
_CfprStorageQualDn_Object=MibTableColumn
cfprStorageQualDn=_CfprStorageQualDn_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,2),_CfprStorageQualDn_Type())
cfprStorageQualDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualDn.setStatus(_A)
_CfprStorageQualRn_Type=SnmpAdminString
_CfprStorageQualRn_Object=MibTableColumn
cfprStorageQualRn=_CfprStorageQualRn_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,3),_CfprStorageQualRn_Type())
cfprStorageQualRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualRn.setStatus(_A)
_CfprStorageQualBlockSize_Type=Gauge32
_CfprStorageQualBlockSize_Object=MibTableColumn
cfprStorageQualBlockSize=_CfprStorageQualBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,4),_CfprStorageQualBlockSize_Type())
cfprStorageQualBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualBlockSize.setStatus(_A)
_CfprStorageQualDiskless_Type=CfprStorageDisklessAction
_CfprStorageQualDiskless_Object=MibTableColumn
cfprStorageQualDiskless=_CfprStorageQualDiskless_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,5),_CfprStorageQualDiskless_Type())
cfprStorageQualDiskless.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualDiskless.setStatus(_A)
_CfprStorageQualMaxCap_Type=Unsigned64
_CfprStorageQualMaxCap_Object=MibTableColumn
cfprStorageQualMaxCap=_CfprStorageQualMaxCap_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,6),_CfprStorageQualMaxCap_Type())
cfprStorageQualMaxCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualMaxCap.setStatus(_A)
_CfprStorageQualMinCap_Type=Unsigned64
_CfprStorageQualMinCap_Object=MibTableColumn
cfprStorageQualMinCap=_CfprStorageQualMinCap_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,7),_CfprStorageQualMinCap_Type())
cfprStorageQualMinCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualMinCap.setStatus(_A)
_CfprStorageQualNumberOfBlocks_Type=Unsigned64
_CfprStorageQualNumberOfBlocks_Object=MibTableColumn
cfprStorageQualNumberOfBlocks=_CfprStorageQualNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,8),_CfprStorageQualNumberOfBlocks_Type())
cfprStorageQualNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualNumberOfBlocks.setStatus(_A)
_CfprStorageQualNumberOfFlexFlashCards_Type=Integer32
_CfprStorageQualNumberOfFlexFlashCards_Object=MibTableColumn
cfprStorageQualNumberOfFlexFlashCards=_CfprStorageQualNumberOfFlexFlashCards_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,9),_CfprStorageQualNumberOfFlexFlashCards_Type())
cfprStorageQualNumberOfFlexFlashCards.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualNumberOfFlexFlashCards.setStatus(_A)
_CfprStorageQualPerDiskCap_Type=Unsigned64
_CfprStorageQualPerDiskCap_Object=MibTableColumn
cfprStorageQualPerDiskCap=_CfprStorageQualPerDiskCap_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,10),_CfprStorageQualPerDiskCap_Type())
cfprStorageQualPerDiskCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualPerDiskCap.setStatus(_A)
_CfprStorageQualUnits_Type=Gauge32
_CfprStorageQualUnits_Object=MibTableColumn
cfprStorageQualUnits=_CfprStorageQualUnits_Object((1,3,6,1,4,1,9,9,826,1,74,34,1,11),_CfprStorageQualUnits_Type())
cfprStorageQualUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageQualUnits.setStatus(_A)
_CfprStorageRaidBatteryTable_Object=MibTable
cfprStorageRaidBatteryTable=_CfprStorageRaidBatteryTable_Object((1,3,6,1,4,1,9,9,826,1,74,35))
if mibBuilder.loadTexts:cfprStorageRaidBatteryTable.setStatus(_A)
_CfprStorageRaidBatteryEntry_Object=MibTableRow
cfprStorageRaidBatteryEntry=_CfprStorageRaidBatteryEntry_Object((1,3,6,1,4,1,9,9,826,1,74,35,1))
cfprStorageRaidBatteryEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:cfprStorageRaidBatteryEntry.setStatus(_A)
_CfprStorageRaidBatteryInstanceId_Type=CfprManagedObjectId
_CfprStorageRaidBatteryInstanceId_Object=MibTableColumn
cfprStorageRaidBatteryInstanceId=_CfprStorageRaidBatteryInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,1),_CfprStorageRaidBatteryInstanceId_Type())
cfprStorageRaidBatteryInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageRaidBatteryInstanceId.setStatus(_A)
_CfprStorageRaidBatteryDn_Type=CfprManagedObjectDn
_CfprStorageRaidBatteryDn_Object=MibTableColumn
cfprStorageRaidBatteryDn=_CfprStorageRaidBatteryDn_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,2),_CfprStorageRaidBatteryDn_Type())
cfprStorageRaidBatteryDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryDn.setStatus(_A)
_CfprStorageRaidBatteryRn_Type=SnmpAdminString
_CfprStorageRaidBatteryRn_Object=MibTableColumn
cfprStorageRaidBatteryRn=_CfprStorageRaidBatteryRn_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,3),_CfprStorageRaidBatteryRn_Type())
cfprStorageRaidBatteryRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryRn.setStatus(_A)
_CfprStorageRaidBatteryBatteryType_Type=CfprStorageBatteryType
_CfprStorageRaidBatteryBatteryType_Object=MibTableColumn
cfprStorageRaidBatteryBatteryType=_CfprStorageRaidBatteryBatteryType_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,4),_CfprStorageRaidBatteryBatteryType_Type())
cfprStorageRaidBatteryBatteryType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryBatteryType.setStatus(_A)
_CfprStorageRaidBatteryBbuStatus_Type=CfprStorageBbuStatus
_CfprStorageRaidBatteryBbuStatus_Object=MibTableColumn
cfprStorageRaidBatteryBbuStatus=_CfprStorageRaidBatteryBbuStatus_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,5),_CfprStorageRaidBatteryBbuStatus_Type())
cfprStorageRaidBatteryBbuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryBbuStatus.setStatus(_A)
_CfprStorageRaidBatteryBlockSize_Type=Gauge32
_CfprStorageRaidBatteryBlockSize_Object=MibTableColumn
cfprStorageRaidBatteryBlockSize=_CfprStorageRaidBatteryBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,6),_CfprStorageRaidBatteryBlockSize_Type())
cfprStorageRaidBatteryBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryBlockSize.setStatus(_A)
_CfprStorageRaidBatteryCapacityPercentage_Type=Gauge32
_CfprStorageRaidBatteryCapacityPercentage_Object=MibTableColumn
cfprStorageRaidBatteryCapacityPercentage=_CfprStorageRaidBatteryCapacityPercentage_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,7),_CfprStorageRaidBatteryCapacityPercentage_Type())
cfprStorageRaidBatteryCapacityPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryCapacityPercentage.setStatus(_A)
_CfprStorageRaidBatteryConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageRaidBatteryConnectionProtocol_Object=MibTableColumn
cfprStorageRaidBatteryConnectionProtocol=_CfprStorageRaidBatteryConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,8),_CfprStorageRaidBatteryConnectionProtocol_Type())
cfprStorageRaidBatteryConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryConnectionProtocol.setStatus(_A)
_CfprStorageRaidBatteryId_Type=Gauge32
_CfprStorageRaidBatteryId_Object=MibTableColumn
cfprStorageRaidBatteryId=_CfprStorageRaidBatteryId_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,9),_CfprStorageRaidBatteryId_Type())
cfprStorageRaidBatteryId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryId.setStatus(_A)
_CfprStorageRaidBatteryLc_Type=CfprFsmLifecycle
_CfprStorageRaidBatteryLc_Object=MibTableColumn
cfprStorageRaidBatteryLc=_CfprStorageRaidBatteryLc_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,10),_CfprStorageRaidBatteryLc_Type())
cfprStorageRaidBatteryLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryLc.setStatus(_A)
_CfprStorageRaidBatteryLearnCycleRequested_Type=CfprStorageLearnCycleRequested
_CfprStorageRaidBatteryLearnCycleRequested_Object=MibTableColumn
cfprStorageRaidBatteryLearnCycleRequested=_CfprStorageRaidBatteryLearnCycleRequested_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,11),_CfprStorageRaidBatteryLearnCycleRequested_Type())
cfprStorageRaidBatteryLearnCycleRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryLearnCycleRequested.setStatus(_A)
_CfprStorageRaidBatteryLearnMode_Type=CfprStorageLearnMode
_CfprStorageRaidBatteryLearnMode_Object=MibTableColumn
cfprStorageRaidBatteryLearnMode=_CfprStorageRaidBatteryLearnMode_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,12),_CfprStorageRaidBatteryLearnMode_Type())
cfprStorageRaidBatteryLearnMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryLearnMode.setStatus(_A)
_CfprStorageRaidBatteryModel_Type=SnmpAdminString
_CfprStorageRaidBatteryModel_Object=MibTableColumn
cfprStorageRaidBatteryModel=_CfprStorageRaidBatteryModel_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,13),_CfprStorageRaidBatteryModel_Type())
cfprStorageRaidBatteryModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryModel.setStatus(_A)
_CfprStorageRaidBatteryNextLearnCycleTs_Type=DateAndTime
_CfprStorageRaidBatteryNextLearnCycleTs_Object=MibTableColumn
cfprStorageRaidBatteryNextLearnCycleTs=_CfprStorageRaidBatteryNextLearnCycleTs_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,14),_CfprStorageRaidBatteryNextLearnCycleTs_Type())
cfprStorageRaidBatteryNextLearnCycleTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryNextLearnCycleTs.setStatus(_A)
_CfprStorageRaidBatteryNumberOfBlocks_Type=Unsigned64
_CfprStorageRaidBatteryNumberOfBlocks_Object=MibTableColumn
cfprStorageRaidBatteryNumberOfBlocks=_CfprStorageRaidBatteryNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,15),_CfprStorageRaidBatteryNumberOfBlocks_Type())
cfprStorageRaidBatteryNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryNumberOfBlocks.setStatus(_A)
_CfprStorageRaidBatteryOperQualifierReason_Type=SnmpAdminString
_CfprStorageRaidBatteryOperQualifierReason_Object=MibTableColumn
cfprStorageRaidBatteryOperQualifierReason=_CfprStorageRaidBatteryOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,16),_CfprStorageRaidBatteryOperQualifierReason_Type())
cfprStorageRaidBatteryOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryOperQualifierReason.setStatus(_A)
_CfprStorageRaidBatteryOperability_Type=CfprEquipmentOperability
_CfprStorageRaidBatteryOperability_Object=MibTableColumn
cfprStorageRaidBatteryOperability=_CfprStorageRaidBatteryOperability_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,17),_CfprStorageRaidBatteryOperability_Type())
cfprStorageRaidBatteryOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryOperability.setStatus(_A)
_CfprStorageRaidBatteryOperabilityQualifier_Type=CfprStorageRaidBatteryOperabilityQualifier
_CfprStorageRaidBatteryOperabilityQualifier_Object=MibTableColumn
cfprStorageRaidBatteryOperabilityQualifier=_CfprStorageRaidBatteryOperabilityQualifier_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,18),_CfprStorageRaidBatteryOperabilityQualifier_Type())
cfprStorageRaidBatteryOperabilityQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryOperabilityQualifier.setStatus(_A)
_CfprStorageRaidBatteryOperabilityQualifierReason_Type=SnmpAdminString
_CfprStorageRaidBatteryOperabilityQualifierReason_Object=MibTableColumn
cfprStorageRaidBatteryOperabilityQualifierReason=_CfprStorageRaidBatteryOperabilityQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,19),_CfprStorageRaidBatteryOperabilityQualifierReason_Type())
cfprStorageRaidBatteryOperabilityQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryOperabilityQualifierReason.setStatus(_A)
_CfprStorageRaidBatteryPresence_Type=CfprEquipmentPresence
_CfprStorageRaidBatteryPresence_Object=MibTableColumn
cfprStorageRaidBatteryPresence=_CfprStorageRaidBatteryPresence_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,20),_CfprStorageRaidBatteryPresence_Type())
cfprStorageRaidBatteryPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryPresence.setStatus(_A)
_CfprStorageRaidBatteryRevision_Type=SnmpAdminString
_CfprStorageRaidBatteryRevision_Object=MibTableColumn
cfprStorageRaidBatteryRevision=_CfprStorageRaidBatteryRevision_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,21),_CfprStorageRaidBatteryRevision_Type())
cfprStorageRaidBatteryRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryRevision.setStatus(_A)
_CfprStorageRaidBatterySerial_Type=SnmpAdminString
_CfprStorageRaidBatterySerial_Object=MibTableColumn
cfprStorageRaidBatterySerial=_CfprStorageRaidBatterySerial_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,22),_CfprStorageRaidBatterySerial_Type())
cfprStorageRaidBatterySerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatterySerial.setStatus(_A)
_CfprStorageRaidBatterySize_Type=Unsigned64
_CfprStorageRaidBatterySize_Object=MibTableColumn
cfprStorageRaidBatterySize=_CfprStorageRaidBatterySize_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,23),_CfprStorageRaidBatterySize_Type())
cfprStorageRaidBatterySize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatterySize.setStatus(_A)
_CfprStorageRaidBatteryTemperature_Type=Integer32
_CfprStorageRaidBatteryTemperature_Object=MibTableColumn
cfprStorageRaidBatteryTemperature=_CfprStorageRaidBatteryTemperature_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,24),_CfprStorageRaidBatteryTemperature_Type())
cfprStorageRaidBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryTemperature.setStatus(_A)
_CfprStorageRaidBatteryVendor_Type=SnmpAdminString
_CfprStorageRaidBatteryVendor_Object=MibTableColumn
cfprStorageRaidBatteryVendor=_CfprStorageRaidBatteryVendor_Object((1,3,6,1,4,1,9,9,826,1,74,35,1,25),_CfprStorageRaidBatteryVendor_Type())
cfprStorageRaidBatteryVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageRaidBatteryVendor.setStatus(_A)
_CfprStorageSystemTable_Object=MibTable
cfprStorageSystemTable=_CfprStorageSystemTable_Object((1,3,6,1,4,1,9,9,826,1,74,36))
if mibBuilder.loadTexts:cfprStorageSystemTable.setStatus(_A)
_CfprStorageSystemEntry_Object=MibTableRow
cfprStorageSystemEntry=_CfprStorageSystemEntry_Object((1,3,6,1,4,1,9,9,826,1,74,36,1))
cfprStorageSystemEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:cfprStorageSystemEntry.setStatus(_A)
_CfprStorageSystemInstanceId_Type=CfprManagedObjectId
_CfprStorageSystemInstanceId_Object=MibTableColumn
cfprStorageSystemInstanceId=_CfprStorageSystemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,1),_CfprStorageSystemInstanceId_Type())
cfprStorageSystemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageSystemInstanceId.setStatus(_A)
_CfprStorageSystemDn_Type=CfprManagedObjectDn
_CfprStorageSystemDn_Object=MibTableColumn
cfprStorageSystemDn=_CfprStorageSystemDn_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,2),_CfprStorageSystemDn_Type())
cfprStorageSystemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemDn.setStatus(_A)
_CfprStorageSystemRn_Type=SnmpAdminString
_CfprStorageSystemRn_Object=MibTableColumn
cfprStorageSystemRn=_CfprStorageSystemRn_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,3),_CfprStorageSystemRn_Type())
cfprStorageSystemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemRn.setStatus(_A)
_CfprStorageSystemFsmDescr_Type=SnmpAdminString
_CfprStorageSystemFsmDescr_Object=MibTableColumn
cfprStorageSystemFsmDescr=_CfprStorageSystemFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,4),_CfprStorageSystemFsmDescr_Type())
cfprStorageSystemFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmDescr.setStatus(_A)
_CfprStorageSystemFsmPrev_Type=SnmpAdminString
_CfprStorageSystemFsmPrev_Object=MibTableColumn
cfprStorageSystemFsmPrev=_CfprStorageSystemFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,5),_CfprStorageSystemFsmPrev_Type())
cfprStorageSystemFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmPrev.setStatus(_A)
_CfprStorageSystemFsmProgr_Type=Gauge32
_CfprStorageSystemFsmProgr_Object=MibTableColumn
cfprStorageSystemFsmProgr=_CfprStorageSystemFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,6),_CfprStorageSystemFsmProgr_Type())
cfprStorageSystemFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmProgr.setStatus(_A)
_CfprStorageSystemFsmRmtInvErrCode_Type=Gauge32
_CfprStorageSystemFsmRmtInvErrCode_Object=MibTableColumn
cfprStorageSystemFsmRmtInvErrCode=_CfprStorageSystemFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,7),_CfprStorageSystemFsmRmtInvErrCode_Type())
cfprStorageSystemFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtInvErrCode.setStatus(_A)
_CfprStorageSystemFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprStorageSystemFsmRmtInvErrDescr_Object=MibTableColumn
cfprStorageSystemFsmRmtInvErrDescr=_CfprStorageSystemFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,8),_CfprStorageSystemFsmRmtInvErrDescr_Type())
cfprStorageSystemFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtInvErrDescr.setStatus(_A)
_CfprStorageSystemFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprStorageSystemFsmRmtInvRslt_Object=MibTableColumn
cfprStorageSystemFsmRmtInvRslt=_CfprStorageSystemFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,9),_CfprStorageSystemFsmRmtInvRslt_Type())
cfprStorageSystemFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtInvRslt.setStatus(_A)
_CfprStorageSystemFsmStageDescr_Type=SnmpAdminString
_CfprStorageSystemFsmStageDescr_Object=MibTableColumn
cfprStorageSystemFsmStageDescr=_CfprStorageSystemFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,10),_CfprStorageSystemFsmStageDescr_Type())
cfprStorageSystemFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageDescr.setStatus(_A)
_CfprStorageSystemFsmStamp_Type=DateAndTime
_CfprStorageSystemFsmStamp_Object=MibTableColumn
cfprStorageSystemFsmStamp=_CfprStorageSystemFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,11),_CfprStorageSystemFsmStamp_Type())
cfprStorageSystemFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStamp.setStatus(_A)
_CfprStorageSystemFsmStatus_Type=SnmpAdminString
_CfprStorageSystemFsmStatus_Object=MibTableColumn
cfprStorageSystemFsmStatus=_CfprStorageSystemFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,12),_CfprStorageSystemFsmStatus_Type())
cfprStorageSystemFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStatus.setStatus(_A)
_CfprStorageSystemFsmTry_Type=Gauge32
_CfprStorageSystemFsmTry_Object=MibTableColumn
cfprStorageSystemFsmTry=_CfprStorageSystemFsmTry_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,13),_CfprStorageSystemFsmTry_Type())
cfprStorageSystemFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTry.setStatus(_A)
_CfprStorageSystemId_Type=SnmpAdminString
_CfprStorageSystemId_Object=MibTableColumn
cfprStorageSystemId=_CfprStorageSystemId_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,14),_CfprStorageSystemId_Type())
cfprStorageSystemId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemId.setStatus(_A)
_CfprStorageSystemName_Type=SnmpAdminString
_CfprStorageSystemName_Object=MibTableColumn
cfprStorageSystemName=_CfprStorageSystemName_Object((1,3,6,1,4,1,9,9,826,1,74,36,1,15),_CfprStorageSystemName_Type())
cfprStorageSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemName.setStatus(_A)
_CfprStorageSystemFsmTable_Object=MibTable
cfprStorageSystemFsmTable=_CfprStorageSystemFsmTable_Object((1,3,6,1,4,1,9,9,826,1,74,37))
if mibBuilder.loadTexts:cfprStorageSystemFsmTable.setStatus(_A)
_CfprStorageSystemFsmEntry_Object=MibTableRow
cfprStorageSystemFsmEntry=_CfprStorageSystemFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,74,37,1))
cfprStorageSystemFsmEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:cfprStorageSystemFsmEntry.setStatus(_A)
_CfprStorageSystemFsmInstanceId_Type=CfprManagedObjectId
_CfprStorageSystemFsmInstanceId_Object=MibTableColumn
cfprStorageSystemFsmInstanceId=_CfprStorageSystemFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,1),_CfprStorageSystemFsmInstanceId_Type())
cfprStorageSystemFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageSystemFsmInstanceId.setStatus(_A)
_CfprStorageSystemFsmDn_Type=CfprManagedObjectDn
_CfprStorageSystemFsmDn_Object=MibTableColumn
cfprStorageSystemFsmDn=_CfprStorageSystemFsmDn_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,2),_CfprStorageSystemFsmDn_Type())
cfprStorageSystemFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmDn.setStatus(_A)
_CfprStorageSystemFsmRn_Type=SnmpAdminString
_CfprStorageSystemFsmRn_Object=MibTableColumn
cfprStorageSystemFsmRn=_CfprStorageSystemFsmRn_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,3),_CfprStorageSystemFsmRn_Type())
cfprStorageSystemFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRn.setStatus(_A)
_CfprStorageSystemFsmCompletionTime_Type=DateAndTime
_CfprStorageSystemFsmCompletionTime_Object=MibTableColumn
cfprStorageSystemFsmCompletionTime=_CfprStorageSystemFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,4),_CfprStorageSystemFsmCompletionTime_Type())
cfprStorageSystemFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmCompletionTime.setStatus(_A)
_CfprStorageSystemFsmCurrentFsm_Type=CfprStorageSystemFsmCurrentFsm
_CfprStorageSystemFsmCurrentFsm_Object=MibTableColumn
cfprStorageSystemFsmCurrentFsm=_CfprStorageSystemFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,5),_CfprStorageSystemFsmCurrentFsm_Type())
cfprStorageSystemFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmCurrentFsm.setStatus(_A)
_CfprStorageSystemFsmDescrData_Type=SnmpAdminString
_CfprStorageSystemFsmDescrData_Object=MibTableColumn
cfprStorageSystemFsmDescrData=_CfprStorageSystemFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,6),_CfprStorageSystemFsmDescrData_Type())
cfprStorageSystemFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmDescrData.setStatus(_A)
_CfprStorageSystemFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprStorageSystemFsmFsmStatus_Object=MibTableColumn
cfprStorageSystemFsmFsmStatus=_CfprStorageSystemFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,7),_CfprStorageSystemFsmFsmStatus_Type())
cfprStorageSystemFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmFsmStatus.setStatus(_A)
_CfprStorageSystemFsmProgress_Type=Gauge32
_CfprStorageSystemFsmProgress_Object=MibTableColumn
cfprStorageSystemFsmProgress=_CfprStorageSystemFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,8),_CfprStorageSystemFsmProgress_Type())
cfprStorageSystemFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmProgress.setStatus(_A)
_CfprStorageSystemFsmRmtErrCode_Type=Gauge32
_CfprStorageSystemFsmRmtErrCode_Object=MibTableColumn
cfprStorageSystemFsmRmtErrCode=_CfprStorageSystemFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,9),_CfprStorageSystemFsmRmtErrCode_Type())
cfprStorageSystemFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtErrCode.setStatus(_A)
_CfprStorageSystemFsmRmtErrDescr_Type=SnmpAdminString
_CfprStorageSystemFsmRmtErrDescr_Object=MibTableColumn
cfprStorageSystemFsmRmtErrDescr=_CfprStorageSystemFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,10),_CfprStorageSystemFsmRmtErrDescr_Type())
cfprStorageSystemFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtErrDescr.setStatus(_A)
_CfprStorageSystemFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprStorageSystemFsmRmtRslt_Object=MibTableColumn
cfprStorageSystemFsmRmtRslt=_CfprStorageSystemFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,74,37,1,11),_CfprStorageSystemFsmRmtRslt_Type())
cfprStorageSystemFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmRmtRslt.setStatus(_A)
_CfprStorageSystemFsmStageTable_Object=MibTable
cfprStorageSystemFsmStageTable=_CfprStorageSystemFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,74,38))
if mibBuilder.loadTexts:cfprStorageSystemFsmStageTable.setStatus(_A)
_CfprStorageSystemFsmStageEntry_Object=MibTableRow
cfprStorageSystemFsmStageEntry=_CfprStorageSystemFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,74,38,1))
cfprStorageSystemFsmStageEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:cfprStorageSystemFsmStageEntry.setStatus(_A)
_CfprStorageSystemFsmStageInstanceId_Type=CfprManagedObjectId
_CfprStorageSystemFsmStageInstanceId_Object=MibTableColumn
cfprStorageSystemFsmStageInstanceId=_CfprStorageSystemFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,1),_CfprStorageSystemFsmStageInstanceId_Type())
cfprStorageSystemFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageInstanceId.setStatus(_A)
_CfprStorageSystemFsmStageDn_Type=CfprManagedObjectDn
_CfprStorageSystemFsmStageDn_Object=MibTableColumn
cfprStorageSystemFsmStageDn=_CfprStorageSystemFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,2),_CfprStorageSystemFsmStageDn_Type())
cfprStorageSystemFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageDn.setStatus(_A)
_CfprStorageSystemFsmStageRn_Type=SnmpAdminString
_CfprStorageSystemFsmStageRn_Object=MibTableColumn
cfprStorageSystemFsmStageRn=_CfprStorageSystemFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,3),_CfprStorageSystemFsmStageRn_Type())
cfprStorageSystemFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageRn.setStatus(_A)
_CfprStorageSystemFsmStageDescrData_Type=SnmpAdminString
_CfprStorageSystemFsmStageDescrData_Object=MibTableColumn
cfprStorageSystemFsmStageDescrData=_CfprStorageSystemFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,4),_CfprStorageSystemFsmStageDescrData_Type())
cfprStorageSystemFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageDescrData.setStatus(_A)
_CfprStorageSystemFsmStageLastUpdateTime_Type=DateAndTime
_CfprStorageSystemFsmStageLastUpdateTime_Object=MibTableColumn
cfprStorageSystemFsmStageLastUpdateTime=_CfprStorageSystemFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,5),_CfprStorageSystemFsmStageLastUpdateTime_Type())
cfprStorageSystemFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageLastUpdateTime.setStatus(_A)
_CfprStorageSystemFsmStageName_Type=CfprStorageSystemFsmStageName
_CfprStorageSystemFsmStageName_Object=MibTableColumn
cfprStorageSystemFsmStageName=_CfprStorageSystemFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,6),_CfprStorageSystemFsmStageName_Type())
cfprStorageSystemFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageName.setStatus(_A)
_CfprStorageSystemFsmStageOrder_Type=Gauge32
_CfprStorageSystemFsmStageOrder_Object=MibTableColumn
cfprStorageSystemFsmStageOrder=_CfprStorageSystemFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,7),_CfprStorageSystemFsmStageOrder_Type())
cfprStorageSystemFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageOrder.setStatus(_A)
_CfprStorageSystemFsmStageRetry_Type=Gauge32
_CfprStorageSystemFsmStageRetry_Object=MibTableColumn
cfprStorageSystemFsmStageRetry=_CfprStorageSystemFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,8),_CfprStorageSystemFsmStageRetry_Type())
cfprStorageSystemFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageRetry.setStatus(_A)
_CfprStorageSystemFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprStorageSystemFsmStageStageStatus_Object=MibTableColumn
cfprStorageSystemFsmStageStageStatus=_CfprStorageSystemFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,74,38,1,9),_CfprStorageSystemFsmStageStageStatus_Type())
cfprStorageSystemFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmStageStageStatus.setStatus(_A)
_CfprStorageSystemFsmTaskTable_Object=MibTable
cfprStorageSystemFsmTaskTable=_CfprStorageSystemFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,74,39))
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskTable.setStatus(_A)
_CfprStorageSystemFsmTaskEntry_Object=MibTableRow
cfprStorageSystemFsmTaskEntry=_CfprStorageSystemFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,74,39,1))
cfprStorageSystemFsmTaskEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskEntry.setStatus(_A)
_CfprStorageSystemFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprStorageSystemFsmTaskInstanceId_Object=MibTableColumn
cfprStorageSystemFsmTaskInstanceId=_CfprStorageSystemFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,1),_CfprStorageSystemFsmTaskInstanceId_Type())
cfprStorageSystemFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskInstanceId.setStatus(_A)
_CfprStorageSystemFsmTaskDn_Type=CfprManagedObjectDn
_CfprStorageSystemFsmTaskDn_Object=MibTableColumn
cfprStorageSystemFsmTaskDn=_CfprStorageSystemFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,2),_CfprStorageSystemFsmTaskDn_Type())
cfprStorageSystemFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskDn.setStatus(_A)
_CfprStorageSystemFsmTaskRn_Type=SnmpAdminString
_CfprStorageSystemFsmTaskRn_Object=MibTableColumn
cfprStorageSystemFsmTaskRn=_CfprStorageSystemFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,3),_CfprStorageSystemFsmTaskRn_Type())
cfprStorageSystemFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskRn.setStatus(_A)
_CfprStorageSystemFsmTaskCompletion_Type=CfprFsmCompletion
_CfprStorageSystemFsmTaskCompletion_Object=MibTableColumn
cfprStorageSystemFsmTaskCompletion=_CfprStorageSystemFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,4),_CfprStorageSystemFsmTaskCompletion_Type())
cfprStorageSystemFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskCompletion.setStatus(_A)
_CfprStorageSystemFsmTaskFlags_Type=CfprFsmFlags
_CfprStorageSystemFsmTaskFlags_Object=MibTableColumn
cfprStorageSystemFsmTaskFlags=_CfprStorageSystemFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,5),_CfprStorageSystemFsmTaskFlags_Type())
cfprStorageSystemFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskFlags.setStatus(_A)
_CfprStorageSystemFsmTaskItem_Type=CfprStorageSystemFsmTaskItem
_CfprStorageSystemFsmTaskItem_Object=MibTableColumn
cfprStorageSystemFsmTaskItem=_CfprStorageSystemFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,6),_CfprStorageSystemFsmTaskItem_Type())
cfprStorageSystemFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskItem.setStatus(_A)
_CfprStorageSystemFsmTaskSeqId_Type=Gauge32
_CfprStorageSystemFsmTaskSeqId_Object=MibTableColumn
cfprStorageSystemFsmTaskSeqId=_CfprStorageSystemFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,74,39,1,7),_CfprStorageSystemFsmTaskSeqId_Type())
cfprStorageSystemFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageSystemFsmTaskSeqId.setStatus(_A)
_CfprStorageTransportableFlashModuleTable_Object=MibTable
cfprStorageTransportableFlashModuleTable=_CfprStorageTransportableFlashModuleTable_Object((1,3,6,1,4,1,9,9,826,1,74,40))
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleTable.setStatus(_A)
_CfprStorageTransportableFlashModuleEntry_Object=MibTableRow
cfprStorageTransportableFlashModuleEntry=_CfprStorageTransportableFlashModuleEntry_Object((1,3,6,1,4,1,9,9,826,1,74,40,1))
cfprStorageTransportableFlashModuleEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleEntry.setStatus(_A)
_CfprStorageTransportableFlashModuleInstanceId_Type=CfprManagedObjectId
_CfprStorageTransportableFlashModuleInstanceId_Object=MibTableColumn
cfprStorageTransportableFlashModuleInstanceId=_CfprStorageTransportableFlashModuleInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,1),_CfprStorageTransportableFlashModuleInstanceId_Type())
cfprStorageTransportableFlashModuleInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleInstanceId.setStatus(_A)
_CfprStorageTransportableFlashModuleDn_Type=CfprManagedObjectDn
_CfprStorageTransportableFlashModuleDn_Object=MibTableColumn
cfprStorageTransportableFlashModuleDn=_CfprStorageTransportableFlashModuleDn_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,2),_CfprStorageTransportableFlashModuleDn_Type())
cfprStorageTransportableFlashModuleDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleDn.setStatus(_A)
_CfprStorageTransportableFlashModuleRn_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleRn_Object=MibTableColumn
cfprStorageTransportableFlashModuleRn=_CfprStorageTransportableFlashModuleRn_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,3),_CfprStorageTransportableFlashModuleRn_Type())
cfprStorageTransportableFlashModuleRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleRn.setStatus(_A)
_CfprStorageTransportableFlashModuleBlockSize_Type=Gauge32
_CfprStorageTransportableFlashModuleBlockSize_Object=MibTableColumn
cfprStorageTransportableFlashModuleBlockSize=_CfprStorageTransportableFlashModuleBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,4),_CfprStorageTransportableFlashModuleBlockSize_Type())
cfprStorageTransportableFlashModuleBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleBlockSize.setStatus(_A)
_CfprStorageTransportableFlashModuleConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageTransportableFlashModuleConnectionProtocol_Object=MibTableColumn
cfprStorageTransportableFlashModuleConnectionProtocol=_CfprStorageTransportableFlashModuleConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,5),_CfprStorageTransportableFlashModuleConnectionProtocol_Type())
cfprStorageTransportableFlashModuleConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleConnectionProtocol.setStatus(_A)
_CfprStorageTransportableFlashModuleId_Type=Gauge32
_CfprStorageTransportableFlashModuleId_Object=MibTableColumn
cfprStorageTransportableFlashModuleId=_CfprStorageTransportableFlashModuleId_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,6),_CfprStorageTransportableFlashModuleId_Type())
cfprStorageTransportableFlashModuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleId.setStatus(_A)
_CfprStorageTransportableFlashModuleModel_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleModel_Object=MibTableColumn
cfprStorageTransportableFlashModuleModel=_CfprStorageTransportableFlashModuleModel_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,7),_CfprStorageTransportableFlashModuleModel_Type())
cfprStorageTransportableFlashModuleModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleModel.setStatus(_A)
_CfprStorageTransportableFlashModuleNumberOfBlocks_Type=Unsigned64
_CfprStorageTransportableFlashModuleNumberOfBlocks_Object=MibTableColumn
cfprStorageTransportableFlashModuleNumberOfBlocks=_CfprStorageTransportableFlashModuleNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,8),_CfprStorageTransportableFlashModuleNumberOfBlocks_Type())
cfprStorageTransportableFlashModuleNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleNumberOfBlocks.setStatus(_A)
_CfprStorageTransportableFlashModuleOperQualifierReason_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleOperQualifierReason_Object=MibTableColumn
cfprStorageTransportableFlashModuleOperQualifierReason=_CfprStorageTransportableFlashModuleOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,9),_CfprStorageTransportableFlashModuleOperQualifierReason_Type())
cfprStorageTransportableFlashModuleOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleOperQualifierReason.setStatus(_A)
_CfprStorageTransportableFlashModuleOperability_Type=CfprEquipmentOperability
_CfprStorageTransportableFlashModuleOperability_Object=MibTableColumn
cfprStorageTransportableFlashModuleOperability=_CfprStorageTransportableFlashModuleOperability_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,10),_CfprStorageTransportableFlashModuleOperability_Type())
cfprStorageTransportableFlashModuleOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleOperability.setStatus(_A)
_CfprStorageTransportableFlashModulePresence_Type=CfprEquipmentPresence
_CfprStorageTransportableFlashModulePresence_Object=MibTableColumn
cfprStorageTransportableFlashModulePresence=_CfprStorageTransportableFlashModulePresence_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,11),_CfprStorageTransportableFlashModulePresence_Type())
cfprStorageTransportableFlashModulePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModulePresence.setStatus(_A)
_CfprStorageTransportableFlashModuleRevision_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleRevision_Object=MibTableColumn
cfprStorageTransportableFlashModuleRevision=_CfprStorageTransportableFlashModuleRevision_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,12),_CfprStorageTransportableFlashModuleRevision_Type())
cfprStorageTransportableFlashModuleRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleRevision.setStatus(_A)
_CfprStorageTransportableFlashModuleSerial_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleSerial_Object=MibTableColumn
cfprStorageTransportableFlashModuleSerial=_CfprStorageTransportableFlashModuleSerial_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,13),_CfprStorageTransportableFlashModuleSerial_Type())
cfprStorageTransportableFlashModuleSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleSerial.setStatus(_A)
_CfprStorageTransportableFlashModuleSize_Type=Unsigned64
_CfprStorageTransportableFlashModuleSize_Object=MibTableColumn
cfprStorageTransportableFlashModuleSize=_CfprStorageTransportableFlashModuleSize_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,14),_CfprStorageTransportableFlashModuleSize_Type())
cfprStorageTransportableFlashModuleSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleSize.setStatus(_A)
_CfprStorageTransportableFlashModuleVendor_Type=SnmpAdminString
_CfprStorageTransportableFlashModuleVendor_Object=MibTableColumn
cfprStorageTransportableFlashModuleVendor=_CfprStorageTransportableFlashModuleVendor_Object((1,3,6,1,4,1,9,9,826,1,74,40,1,15),_CfprStorageTransportableFlashModuleVendor_Type())
cfprStorageTransportableFlashModuleVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageTransportableFlashModuleVendor.setStatus(_A)
_CfprStorageVirtualDriveTable_Object=MibTable
cfprStorageVirtualDriveTable=_CfprStorageVirtualDriveTable_Object((1,3,6,1,4,1,9,9,826,1,74,41))
if mibBuilder.loadTexts:cfprStorageVirtualDriveTable.setStatus(_A)
_CfprStorageVirtualDriveEntry_Object=MibTableRow
cfprStorageVirtualDriveEntry=_CfprStorageVirtualDriveEntry_Object((1,3,6,1,4,1,9,9,826,1,74,41,1))
cfprStorageVirtualDriveEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:cfprStorageVirtualDriveEntry.setStatus(_A)
_CfprStorageVirtualDriveInstanceId_Type=CfprManagedObjectId
_CfprStorageVirtualDriveInstanceId_Object=MibTableColumn
cfprStorageVirtualDriveInstanceId=_CfprStorageVirtualDriveInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,1),_CfprStorageVirtualDriveInstanceId_Type())
cfprStorageVirtualDriveInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageVirtualDriveInstanceId.setStatus(_A)
_CfprStorageVirtualDriveDn_Type=CfprManagedObjectDn
_CfprStorageVirtualDriveDn_Object=MibTableColumn
cfprStorageVirtualDriveDn=_CfprStorageVirtualDriveDn_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,2),_CfprStorageVirtualDriveDn_Type())
cfprStorageVirtualDriveDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveDn.setStatus(_A)
_CfprStorageVirtualDriveRn_Type=SnmpAdminString
_CfprStorageVirtualDriveRn_Object=MibTableColumn
cfprStorageVirtualDriveRn=_CfprStorageVirtualDriveRn_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,3),_CfprStorageVirtualDriveRn_Type())
cfprStorageVirtualDriveRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveRn.setStatus(_A)
_CfprStorageVirtualDriveAccessPolicy_Type=CfprStorageAccessType
_CfprStorageVirtualDriveAccessPolicy_Object=MibTableColumn
cfprStorageVirtualDriveAccessPolicy=_CfprStorageVirtualDriveAccessPolicy_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,4),_CfprStorageVirtualDriveAccessPolicy_Type())
cfprStorageVirtualDriveAccessPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveAccessPolicy.setStatus(_A)
_CfprStorageVirtualDriveActualWriteCachePolicy_Type=CfprStorageActualWriteType
_CfprStorageVirtualDriveActualWriteCachePolicy_Object=MibTableColumn
cfprStorageVirtualDriveActualWriteCachePolicy=_CfprStorageVirtualDriveActualWriteCachePolicy_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,5),_CfprStorageVirtualDriveActualWriteCachePolicy_Type())
cfprStorageVirtualDriveActualWriteCachePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveActualWriteCachePolicy.setStatus(_A)
_CfprStorageVirtualDriveBlockSize_Type=Gauge32
_CfprStorageVirtualDriveBlockSize_Object=MibTableColumn
cfprStorageVirtualDriveBlockSize=_CfprStorageVirtualDriveBlockSize_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,6),_CfprStorageVirtualDriveBlockSize_Type())
cfprStorageVirtualDriveBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveBlockSize.setStatus(_A)
_CfprStorageVirtualDriveBootable_Type=CfprStorageBootableType
_CfprStorageVirtualDriveBootable_Object=MibTableColumn
cfprStorageVirtualDriveBootable=_CfprStorageVirtualDriveBootable_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,7),_CfprStorageVirtualDriveBootable_Type())
cfprStorageVirtualDriveBootable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveBootable.setStatus(_A)
_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Type=CfprStorageConfiguredWriteType
_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Object=MibTableColumn
cfprStorageVirtualDriveConfiguredWriteCachePolicy=_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,8),_CfprStorageVirtualDriveConfiguredWriteCachePolicy_Type())
cfprStorageVirtualDriveConfiguredWriteCachePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveConfiguredWriteCachePolicy.setStatus(_A)
_CfprStorageVirtualDriveConnectionProtocol_Type=CfprStorageConnectionProtocol
_CfprStorageVirtualDriveConnectionProtocol_Object=MibTableColumn
cfprStorageVirtualDriveConnectionProtocol=_CfprStorageVirtualDriveConnectionProtocol_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,9),_CfprStorageVirtualDriveConnectionProtocol_Type())
cfprStorageVirtualDriveConnectionProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveConnectionProtocol.setStatus(_A)
_CfprStorageVirtualDriveDriveCache_Type=CfprStorageCacheType
_CfprStorageVirtualDriveDriveCache_Object=MibTableColumn
cfprStorageVirtualDriveDriveCache=_CfprStorageVirtualDriveDriveCache_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,10),_CfprStorageVirtualDriveDriveCache_Type())
cfprStorageVirtualDriveDriveCache.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveDriveCache.setStatus(_A)
_CfprStorageVirtualDriveDriveState_Type=CfprStorageVDriveState
_CfprStorageVirtualDriveDriveState_Object=MibTableColumn
cfprStorageVirtualDriveDriveState=_CfprStorageVirtualDriveDriveState_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,11),_CfprStorageVirtualDriveDriveState_Type())
cfprStorageVirtualDriveDriveState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveDriveState.setStatus(_A)
_CfprStorageVirtualDriveId_Type=Gauge32
_CfprStorageVirtualDriveId_Object=MibTableColumn
cfprStorageVirtualDriveId=_CfprStorageVirtualDriveId_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,12),_CfprStorageVirtualDriveId_Type())
cfprStorageVirtualDriveId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveId.setStatus(_A)
_CfprStorageVirtualDriveIoPolicy_Type=CfprStorageIOType
_CfprStorageVirtualDriveIoPolicy_Object=MibTableColumn
cfprStorageVirtualDriveIoPolicy=_CfprStorageVirtualDriveIoPolicy_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,13),_CfprStorageVirtualDriveIoPolicy_Type())
cfprStorageVirtualDriveIoPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveIoPolicy.setStatus(_A)
_CfprStorageVirtualDriveLc_Type=CfprFsmLifecycle
_CfprStorageVirtualDriveLc_Object=MibTableColumn
cfprStorageVirtualDriveLc=_CfprStorageVirtualDriveLc_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,14),_CfprStorageVirtualDriveLc_Type())
cfprStorageVirtualDriveLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveLc.setStatus(_A)
_CfprStorageVirtualDriveModel_Type=SnmpAdminString
_CfprStorageVirtualDriveModel_Object=MibTableColumn
cfprStorageVirtualDriveModel=_CfprStorageVirtualDriveModel_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,15),_CfprStorageVirtualDriveModel_Type())
cfprStorageVirtualDriveModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveModel.setStatus(_A)
_CfprStorageVirtualDriveNumberOfBlocks_Type=Unsigned64
_CfprStorageVirtualDriveNumberOfBlocks_Object=MibTableColumn
cfprStorageVirtualDriveNumberOfBlocks=_CfprStorageVirtualDriveNumberOfBlocks_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,16),_CfprStorageVirtualDriveNumberOfBlocks_Type())
cfprStorageVirtualDriveNumberOfBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveNumberOfBlocks.setStatus(_A)
_CfprStorageVirtualDriveOperQualifierReason_Type=SnmpAdminString
_CfprStorageVirtualDriveOperQualifierReason_Object=MibTableColumn
cfprStorageVirtualDriveOperQualifierReason=_CfprStorageVirtualDriveOperQualifierReason_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,17),_CfprStorageVirtualDriveOperQualifierReason_Type())
cfprStorageVirtualDriveOperQualifierReason.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveOperQualifierReason.setStatus(_A)
_CfprStorageVirtualDriveOperability_Type=CfprEquipmentOperability
_CfprStorageVirtualDriveOperability_Object=MibTableColumn
cfprStorageVirtualDriveOperability=_CfprStorageVirtualDriveOperability_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,18),_CfprStorageVirtualDriveOperability_Type())
cfprStorageVirtualDriveOperability.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveOperability.setStatus(_A)
_CfprStorageVirtualDrivePresence_Type=CfprEquipmentPresence
_CfprStorageVirtualDrivePresence_Object=MibTableColumn
cfprStorageVirtualDrivePresence=_CfprStorageVirtualDrivePresence_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,19),_CfprStorageVirtualDrivePresence_Type())
cfprStorageVirtualDrivePresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDrivePresence.setStatus(_A)
_CfprStorageVirtualDriveReadPolicy_Type=CfprStorageReadType
_CfprStorageVirtualDriveReadPolicy_Object=MibTableColumn
cfprStorageVirtualDriveReadPolicy=_CfprStorageVirtualDriveReadPolicy_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,20),_CfprStorageVirtualDriveReadPolicy_Type())
cfprStorageVirtualDriveReadPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveReadPolicy.setStatus(_A)
_CfprStorageVirtualDriveRevision_Type=SnmpAdminString
_CfprStorageVirtualDriveRevision_Object=MibTableColumn
cfprStorageVirtualDriveRevision=_CfprStorageVirtualDriveRevision_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,21),_CfprStorageVirtualDriveRevision_Type())
cfprStorageVirtualDriveRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveRevision.setStatus(_A)
_CfprStorageVirtualDriveSerial_Type=SnmpAdminString
_CfprStorageVirtualDriveSerial_Object=MibTableColumn
cfprStorageVirtualDriveSerial=_CfprStorageVirtualDriveSerial_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,22),_CfprStorageVirtualDriveSerial_Type())
cfprStorageVirtualDriveSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveSerial.setStatus(_A)
_CfprStorageVirtualDriveSize_Type=Unsigned64
_CfprStorageVirtualDriveSize_Object=MibTableColumn
cfprStorageVirtualDriveSize=_CfprStorageVirtualDriveSize_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,23),_CfprStorageVirtualDriveSize_Type())
cfprStorageVirtualDriveSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveSize.setStatus(_A)
_CfprStorageVirtualDriveStripSize_Type=Unsigned64
_CfprStorageVirtualDriveStripSize_Object=MibTableColumn
cfprStorageVirtualDriveStripSize=_CfprStorageVirtualDriveStripSize_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,24),_CfprStorageVirtualDriveStripSize_Type())
cfprStorageVirtualDriveStripSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveStripSize.setStatus(_A)
_CfprStorageVirtualDriveType_Type=CfprStorageLunType
_CfprStorageVirtualDriveType_Object=MibTableColumn
cfprStorageVirtualDriveType=_CfprStorageVirtualDriveType_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,25),_CfprStorageVirtualDriveType_Type())
cfprStorageVirtualDriveType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveType.setStatus(_A)
_CfprStorageVirtualDriveVendor_Type=SnmpAdminString
_CfprStorageVirtualDriveVendor_Object=MibTableColumn
cfprStorageVirtualDriveVendor=_CfprStorageVirtualDriveVendor_Object((1,3,6,1,4,1,9,9,826,1,74,41,1,26),_CfprStorageVirtualDriveVendor_Type())
cfprStorageVirtualDriveVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVirtualDriveVendor.setStatus(_A)
_CfprStorageVsanRefTable_Object=MibTable
cfprStorageVsanRefTable=_CfprStorageVsanRefTable_Object((1,3,6,1,4,1,9,9,826,1,74,42))
if mibBuilder.loadTexts:cfprStorageVsanRefTable.setStatus(_A)
_CfprStorageVsanRefEntry_Object=MibTableRow
cfprStorageVsanRefEntry=_CfprStorageVsanRefEntry_Object((1,3,6,1,4,1,9,9,826,1,74,42,1))
cfprStorageVsanRefEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:cfprStorageVsanRefEntry.setStatus(_A)
_CfprStorageVsanRefInstanceId_Type=CfprManagedObjectId
_CfprStorageVsanRefInstanceId_Object=MibTableColumn
cfprStorageVsanRefInstanceId=_CfprStorageVsanRefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,1),_CfprStorageVsanRefInstanceId_Type())
cfprStorageVsanRefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprStorageVsanRefInstanceId.setStatus(_A)
_CfprStorageVsanRefDn_Type=CfprManagedObjectDn
_CfprStorageVsanRefDn_Object=MibTableColumn
cfprStorageVsanRefDn=_CfprStorageVsanRefDn_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,2),_CfprStorageVsanRefDn_Type())
cfprStorageVsanRefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefDn.setStatus(_A)
_CfprStorageVsanRefRn_Type=SnmpAdminString
_CfprStorageVsanRefRn_Object=MibTableColumn
cfprStorageVsanRefRn=_CfprStorageVsanRefRn_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,3),_CfprStorageVsanRefRn_Type())
cfprStorageVsanRefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefRn.setStatus(_A)
_CfprStorageVsanRefConfigQualifier_Type=CfprVnicConfigIssues
_CfprStorageVsanRefConfigQualifier_Object=MibTableColumn
cfprStorageVsanRefConfigQualifier=_CfprStorageVsanRefConfigQualifier_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,4),_CfprStorageVsanRefConfigQualifier_Type())
cfprStorageVsanRefConfigQualifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefConfigQualifier.setStatus(_A)
_CfprStorageVsanRefName_Type=SnmpAdminString
_CfprStorageVsanRefName_Object=MibTableColumn
cfprStorageVsanRefName=_CfprStorageVsanRefName_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,5),_CfprStorageVsanRefName_Type())
cfprStorageVsanRefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefName.setStatus(_A)
_CfprStorageVsanRefOperVnetDn_Type=SnmpAdminString
_CfprStorageVsanRefOperVnetDn_Object=MibTableColumn
cfprStorageVsanRefOperVnetDn=_CfprStorageVsanRefOperVnetDn_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,6),_CfprStorageVsanRefOperVnetDn_Type())
cfprStorageVsanRefOperVnetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefOperVnetDn.setStatus(_A)
_CfprStorageVsanRefOperVnetName_Type=SnmpAdminString
_CfprStorageVsanRefOperVnetName_Object=MibTableColumn
cfprStorageVsanRefOperVnetName=_CfprStorageVsanRefOperVnetName_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,7),_CfprStorageVsanRefOperVnetName_Type())
cfprStorageVsanRefOperVnetName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefOperVnetName.setStatus(_A)
_CfprStorageVsanRefSwitchId_Type=CfprStorageVsanRefSwitchId
_CfprStorageVsanRefSwitchId_Object=MibTableColumn
cfprStorageVsanRefSwitchId=_CfprStorageVsanRefSwitchId_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,8),_CfprStorageVsanRefSwitchId_Type())
cfprStorageVsanRefSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefSwitchId.setStatus(_A)
_CfprStorageVsanRefVnet_Type=Gauge32
_CfprStorageVsanRefVnet_Object=MibTableColumn
cfprStorageVsanRefVnet=_CfprStorageVsanRefVnet_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,9),_CfprStorageVsanRefVnet_Type())
cfprStorageVsanRefVnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefVnet.setStatus(_A)
_CfprStorageVsanRefZoningState_Type=CfprFabricZoningState
_CfprStorageVsanRefZoningState_Object=MibTableColumn
cfprStorageVsanRefZoningState=_CfprStorageVsanRefZoningState_Object((1,3,6,1,4,1,9,9,826,1,74,42,1,10),_CfprStorageVsanRefZoningState_Type())
cfprStorageVsanRefZoningState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprStorageVsanRefZoningState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprStorageObjects':cfprStorageObjects,'cfprStorageAuthKeyTable':cfprStorageAuthKeyTable,'cfprStorageAuthKeyEntry':cfprStorageAuthKeyEntry,_E:cfprStorageAuthKeyInstanceId,'cfprStorageAuthKeyDn':cfprStorageAuthKeyDn,'cfprStorageAuthKeyRn':cfprStorageAuthKeyRn,'cfprStorageAuthKeyDescr':cfprStorageAuthKeyDescr,'cfprStorageAuthKeyIntId':cfprStorageAuthKeyIntId,'cfprStorageAuthKeyName':cfprStorageAuthKeyName,'cfprStorageAuthKeyPassword':cfprStorageAuthKeyPassword,'cfprStorageAuthKeyPolicyLevel':cfprStorageAuthKeyPolicyLevel,'cfprStorageAuthKeyPolicyOwner':cfprStorageAuthKeyPolicyOwner,'cfprStorageAuthKeyType':cfprStorageAuthKeyType,'cfprStorageAuthKeyUserId':cfprStorageAuthKeyUserId,'cfprStorageConnectionDefTable':cfprStorageConnectionDefTable,'cfprStorageConnectionDefEntry':cfprStorageConnectionDefEntry,_F:cfprStorageConnectionDefInstanceId,'cfprStorageConnectionDefDn':cfprStorageConnectionDefDn,'cfprStorageConnectionDefRn':cfprStorageConnectionDefRn,'cfprStorageConnectionDefDescr':cfprStorageConnectionDefDescr,'cfprStorageConnectionDefIntId':cfprStorageConnectionDefIntId,'cfprStorageConnectionDefName':cfprStorageConnectionDefName,'cfprStorageConnectionDefOperState':cfprStorageConnectionDefOperState,'cfprStorageConnectionDefPolicyLevel':cfprStorageConnectionDefPolicyLevel,'cfprStorageConnectionDefPolicyOwner':cfprStorageConnectionDefPolicyOwner,'cfprStorageConnectionDefZoningType':cfprStorageConnectionDefZoningType,'cfprStorageConnectionPolicyTable':cfprStorageConnectionPolicyTable,'cfprStorageConnectionPolicyEntry':cfprStorageConnectionPolicyEntry,_G:cfprStorageConnectionPolicyInstanceId,'cfprStorageConnectionPolicyDn':cfprStorageConnectionPolicyDn,'cfprStorageConnectionPolicyRn':cfprStorageConnectionPolicyRn,'cfprStorageConnectionPolicyDescr':cfprStorageConnectionPolicyDescr,'cfprStorageConnectionPolicyIntId':cfprStorageConnectionPolicyIntId,'cfprStorageConnectionPolicyName':cfprStorageConnectionPolicyName,'cfprStorageConnectionPolicyOperState':cfprStorageConnectionPolicyOperState,'cfprStorageConnectionPolicyPolicyLevel':cfprStorageConnectionPolicyPolicyLevel,'cfprStorageConnectionPolicyPolicyOwner':cfprStorageConnectionPolicyPolicyOwner,'cfprStorageConnectionPolicyZoningType':cfprStorageConnectionPolicyZoningType,'cfprStorageControllerTable':cfprStorageControllerTable,'cfprStorageControllerEntry':cfprStorageControllerEntry,_H:cfprStorageControllerInstanceId,'cfprStorageControllerDn':cfprStorageControllerDn,'cfprStorageControllerRn':cfprStorageControllerRn,'cfprStorageControllerControllerStatus':cfprStorageControllerControllerStatus,'cfprStorageControllerDeviceRaidSupport':cfprStorageControllerDeviceRaidSupport,'cfprStorageControllerFaultMonitoring':cfprStorageControllerFaultMonitoring,'cfprStorageControllerHwRevision':cfprStorageControllerHwRevision,'cfprStorageControllerId':cfprStorageControllerId,'cfprStorageControllerLc':cfprStorageControllerLc,'cfprStorageControllerLocationDn':cfprStorageControllerLocationDn,'cfprStorageControllerModel':cfprStorageControllerModel,'cfprStorageControllerOobControllerId':cfprStorageControllerOobControllerId,'cfprStorageControllerOobInterfaceSupported':cfprStorageControllerOobInterfaceSupported,'cfprStorageControllerOperQualifierReason':cfprStorageControllerOperQualifierReason,'cfprStorageControllerOperState':cfprStorageControllerOperState,'cfprStorageControllerOperability':cfprStorageControllerOperability,'cfprStorageControllerPartNumber':cfprStorageControllerPartNumber,'cfprStorageControllerPciAddr':cfprStorageControllerPciAddr,'cfprStorageControllerPciSlot':cfprStorageControllerPciSlot,'cfprStorageControllerPerf':cfprStorageControllerPerf,'cfprStorageControllerPower':cfprStorageControllerPower,'cfprStorageControllerPresence':cfprStorageControllerPresence,'cfprStorageControllerRaidSupport':cfprStorageControllerRaidSupport,'cfprStorageControllerRebuildRate':cfprStorageControllerRebuildRate,'cfprStorageControllerRevision':cfprStorageControllerRevision,'cfprStorageControllerSerial':cfprStorageControllerSerial,'cfprStorageControllerThermal':cfprStorageControllerThermal,'cfprStorageControllerType':cfprStorageControllerType,'cfprStorageControllerVendor':cfprStorageControllerVendor,'cfprStorageControllerVid':cfprStorageControllerVid,'cfprStorageControllerVoltage':cfprStorageControllerVoltage,'cfprStorageDomainEpTable':cfprStorageDomainEpTable,'cfprStorageDomainEpEntry':cfprStorageDomainEpEntry,_I:cfprStorageDomainEpInstanceId,'cfprStorageDomainEpDn':cfprStorageDomainEpDn,'cfprStorageDomainEpRn':cfprStorageDomainEpRn,'cfprStorageDriveTable':cfprStorageDriveTable,'cfprStorageDriveEntry':cfprStorageDriveEntry,_J:cfprStorageDriveInstanceId,'cfprStorageDriveDn':cfprStorageDriveDn,'cfprStorageDriveRn':cfprStorageDriveRn,'cfprStorageDriveId':cfprStorageDriveId,'cfprStorageDriveModel':cfprStorageDriveModel,'cfprStorageDrivePciAddr':cfprStorageDrivePciAddr,'cfprStorageDriveRevision':cfprStorageDriveRevision,'cfprStorageDriveSerial':cfprStorageDriveSerial,'cfprStorageDriveVendor':cfprStorageDriveVendor,'cfprStorageEnclosureTable':cfprStorageEnclosureTable,'cfprStorageEnclosureEntry':cfprStorageEnclosureEntry,_K:cfprStorageEnclosureInstanceId,'cfprStorageEnclosureDn':cfprStorageEnclosureDn,'cfprStorageEnclosureRn':cfprStorageEnclosureRn,'cfprStorageEnclosureId':cfprStorageEnclosureId,'cfprStorageEnclosureLc':cfprStorageEnclosureLc,'cfprStorageEnclosureModel':cfprStorageEnclosureModel,'cfprStorageEnclosureNumSlots':cfprStorageEnclosureNumSlots,'cfprStorageEnclosureRevision':cfprStorageEnclosureRevision,'cfprStorageEnclosureSerial':cfprStorageEnclosureSerial,'cfprStorageEnclosureVendor':cfprStorageEnclosureVendor,'cfprStorageEpUserTable':cfprStorageEpUserTable,'cfprStorageEpUserEntry':cfprStorageEpUserEntry,_L:cfprStorageEpUserInstanceId,'cfprStorageEpUserDn':cfprStorageEpUserDn,'cfprStorageEpUserRn':cfprStorageEpUserRn,'cfprStorageEpUserConfigState':cfprStorageEpUserConfigState,'cfprStorageEpUserConfigStatusMessage':cfprStorageEpUserConfigStatusMessage,'cfprStorageEpUserDescr':cfprStorageEpUserDescr,'cfprStorageEpUserDomain':cfprStorageEpUserDomain,'cfprStorageEpUserName':cfprStorageEpUserName,'cfprStorageEpUserPriv':cfprStorageEpUserPriv,'cfprStorageEpUserPwd':cfprStorageEpUserPwd,'cfprStorageEpUserPwdSet':cfprStorageEpUserPwdSet,'cfprStorageEtherIfTable':cfprStorageEtherIfTable,'cfprStorageEtherIfEntry':cfprStorageEtherIfEntry,_M:cfprStorageEtherIfInstanceId,'cfprStorageEtherIfDn':cfprStorageEtherIfDn,'cfprStorageEtherIfRn':cfprStorageEtherIfRn,'cfprStorageEtherIfName':cfprStorageEtherIfName,'cfprStorageEtherIfVlanType':cfprStorageEtherIfVlanType,'cfprStorageFcIfTable':cfprStorageFcIfTable,'cfprStorageFcIfEntry':cfprStorageFcIfEntry,_N:cfprStorageFcIfInstanceId,'cfprStorageFcIfDn':cfprStorageFcIfDn,'cfprStorageFcIfRn':cfprStorageFcIfRn,'cfprStorageFcIfName':cfprStorageFcIfName,'cfprStorageFcTargetEpTable':cfprStorageFcTargetEpTable,'cfprStorageFcTargetEpEntry':cfprStorageFcTargetEpEntry,_O:cfprStorageFcTargetEpInstanceId,'cfprStorageFcTargetEpDn':cfprStorageFcTargetEpDn,'cfprStorageFcTargetEpRn':cfprStorageFcTargetEpRn,'cfprStorageFcTargetEpDescr':cfprStorageFcTargetEpDescr,'cfprStorageFcTargetEpPath':cfprStorageFcTargetEpPath,'cfprStorageFcTargetEpTargetwwpn':cfprStorageFcTargetEpTargetwwpn,'cfprStorageFcTargetIfTable':cfprStorageFcTargetIfTable,'cfprStorageFcTargetIfEntry':cfprStorageFcTargetIfEntry,_P:cfprStorageFcTargetIfInstanceId,'cfprStorageFcTargetIfDn':cfprStorageFcTargetIfDn,'cfprStorageFcTargetIfRn':cfprStorageFcTargetIfRn,'cfprStorageFcTargetIfId':cfprStorageFcTargetIfId,'cfprStorageFcTargetIfProt':cfprStorageFcTargetIfProt,'cfprStorageFlexFlashCardTable':cfprStorageFlexFlashCardTable,'cfprStorageFlexFlashCardEntry':cfprStorageFlexFlashCardEntry,_Q:cfprStorageFlexFlashCardInstanceId,'cfprStorageFlexFlashCardDn':cfprStorageFlexFlashCardDn,'cfprStorageFlexFlashCardRn':cfprStorageFlexFlashCardRn,'cfprStorageFlexFlashCardBlockSize':cfprStorageFlexFlashCardBlockSize,'cfprStorageFlexFlashCardCardHealth':cfprStorageFlexFlashCardCardHealth,'cfprStorageFlexFlashCardCardMode':cfprStorageFlexFlashCardCardMode,'cfprStorageFlexFlashCardCardState':cfprStorageFlexFlashCardCardState,'cfprStorageFlexFlashCardCardSync':cfprStorageFlexFlashCardCardSync,'cfprStorageFlexFlashCardCardType':cfprStorageFlexFlashCardCardType,'cfprStorageFlexFlashCardConnectionProtocol':cfprStorageFlexFlashCardConnectionProtocol,'cfprStorageFlexFlashCardControllerIndex':cfprStorageFlexFlashCardControllerIndex,'cfprStorageFlexFlashCardDrivesEnabled':cfprStorageFlexFlashCardDrivesEnabled,'cfprStorageFlexFlashCardId':cfprStorageFlexFlashCardId,'cfprStorageFlexFlashCardMfgDate':cfprStorageFlexFlashCardMfgDate,'cfprStorageFlexFlashCardMfgId':cfprStorageFlexFlashCardMfgId,'cfprStorageFlexFlashCardModel':cfprStorageFlexFlashCardModel,'cfprStorageFlexFlashCardNumberOfBlocks':cfprStorageFlexFlashCardNumberOfBlocks,'cfprStorageFlexFlashCardOemId':cfprStorageFlexFlashCardOemId,'cfprStorageFlexFlashCardOperQualifierReason':cfprStorageFlexFlashCardOperQualifierReason,'cfprStorageFlexFlashCardOperability':cfprStorageFlexFlashCardOperability,'cfprStorageFlexFlashCardPartitionCount':cfprStorageFlexFlashCardPartitionCount,'cfprStorageFlexFlashCardPresence':cfprStorageFlexFlashCardPresence,'cfprStorageFlexFlashCardReadErrorThreshold':cfprStorageFlexFlashCardReadErrorThreshold,'cfprStorageFlexFlashCardReadIOErrorCount':cfprStorageFlexFlashCardReadIOErrorCount,'cfprStorageFlexFlashCardRevision':cfprStorageFlexFlashCardRevision,'cfprStorageFlexFlashCardSerial':cfprStorageFlexFlashCardSerial,'cfprStorageFlexFlashCardSignature':cfprStorageFlexFlashCardSignature,'cfprStorageFlexFlashCardSize':cfprStorageFlexFlashCardSize,'cfprStorageFlexFlashCardSlotNumber':cfprStorageFlexFlashCardSlotNumber,'cfprStorageFlexFlashCardVendor':cfprStorageFlexFlashCardVendor,'cfprStorageFlexFlashCardWriteEnable':cfprStorageFlexFlashCardWriteEnable,'cfprStorageFlexFlashCardWriteErrorThreshold':cfprStorageFlexFlashCardWriteErrorThreshold,'cfprStorageFlexFlashCardWriteIOErrorCount':cfprStorageFlexFlashCardWriteIOErrorCount,'cfprStorageFlexFlashControllerTable':cfprStorageFlexFlashControllerTable,'cfprStorageFlexFlashControllerEntry':cfprStorageFlexFlashControllerEntry,_R:cfprStorageFlexFlashControllerInstanceId,'cfprStorageFlexFlashControllerDn':cfprStorageFlexFlashControllerDn,'cfprStorageFlexFlashControllerRn':cfprStorageFlexFlashControllerRn,'cfprStorageFlexFlashControllerAdminSlotNumber':cfprStorageFlexFlashControllerAdminSlotNumber,'cfprStorageFlexFlashControllerConfiguredMode':cfprStorageFlexFlashControllerConfiguredMode,'cfprStorageFlexFlashControllerControllerHealth':cfprStorageFlexFlashControllerControllerHealth,'cfprStorageFlexFlashControllerControllerState':cfprStorageFlexFlashControllerControllerState,'cfprStorageFlexFlashControllerFirmwareVersion':cfprStorageFlexFlashControllerFirmwareVersion,'cfprStorageFlexFlashControllerFlexFlashType':cfprStorageFlexFlashControllerFlexFlashType,'cfprStorageFlexFlashControllerFsmDescr':cfprStorageFlexFlashControllerFsmDescr,'cfprStorageFlexFlashControllerFsmPrev':cfprStorageFlexFlashControllerFsmPrev,'cfprStorageFlexFlashControllerFsmProgr':cfprStorageFlexFlashControllerFsmProgr,'cfprStorageFlexFlashControllerFsmRmtInvErrCode':cfprStorageFlexFlashControllerFsmRmtInvErrCode,'cfprStorageFlexFlashControllerFsmRmtInvErrDescr':cfprStorageFlexFlashControllerFsmRmtInvErrDescr,'cfprStorageFlexFlashControllerFsmRmtInvRslt':cfprStorageFlexFlashControllerFsmRmtInvRslt,'cfprStorageFlexFlashControllerFsmStageDescr':cfprStorageFlexFlashControllerFsmStageDescr,'cfprStorageFlexFlashControllerFsmStamp':cfprStorageFlexFlashControllerFsmStamp,'cfprStorageFlexFlashControllerFsmStatus':cfprStorageFlexFlashControllerFsmStatus,'cfprStorageFlexFlashControllerFsmTry':cfprStorageFlexFlashControllerFsmTry,'cfprStorageFlexFlashControllerHasError':cfprStorageFlexFlashControllerHasError,'cfprStorageFlexFlashControllerId':cfprStorageFlexFlashControllerId,'cfprStorageFlexFlashControllerIsCardMismatch':cfprStorageFlexFlashControllerIsCardMismatch,'cfprStorageFlexFlashControllerIsFormatFSMRunning':cfprStorageFlexFlashControllerIsFormatFSMRunning,'cfprStorageFlexFlashControllerLocationDn':cfprStorageFlexFlashControllerLocationDn,'cfprStorageFlexFlashControllerModel':cfprStorageFlexFlashControllerModel,'cfprStorageFlexFlashControllerOperQualifierReason':cfprStorageFlexFlashControllerOperQualifierReason,'cfprStorageFlexFlashControllerOperState':cfprStorageFlexFlashControllerOperState,'cfprStorageFlexFlashControllerOperability':cfprStorageFlexFlashControllerOperability,'cfprStorageFlexFlashControllerOperatingMode':cfprStorageFlexFlashControllerOperatingMode,'cfprStorageFlexFlashControllerOperationRequest':cfprStorageFlexFlashControllerOperationRequest,'cfprStorageFlexFlashControllerPciAddr':cfprStorageFlexFlashControllerPciAddr,'cfprStorageFlexFlashControllerPciSlot':cfprStorageFlexFlashControllerPciSlot,'cfprStorageFlexFlashControllerPerf':cfprStorageFlexFlashControllerPerf,'cfprStorageFlexFlashControllerPhysicalDriveCount':cfprStorageFlexFlashControllerPhysicalDriveCount,'cfprStorageFlexFlashControllerPower':cfprStorageFlexFlashControllerPower,'cfprStorageFlexFlashControllerPresence':cfprStorageFlexFlashControllerPresence,'cfprStorageFlexFlashControllerPrimarySlotNumber':cfprStorageFlexFlashControllerPrimarySlotNumber,'cfprStorageFlexFlashControllerRaidSyncSupport':cfprStorageFlexFlashControllerRaidSyncSupport,'cfprStorageFlexFlashControllerReadErrorThreshold':cfprStorageFlexFlashControllerReadErrorThreshold,'cfprStorageFlexFlashControllerRevision':cfprStorageFlexFlashControllerRevision,'cfprStorageFlexFlashControllerSerial':cfprStorageFlexFlashControllerSerial,'cfprStorageFlexFlashControllerThermal':cfprStorageFlexFlashControllerThermal,'cfprStorageFlexFlashControllerType':cfprStorageFlexFlashControllerType,'cfprStorageFlexFlashControllerVendor':cfprStorageFlexFlashControllerVendor,'cfprStorageFlexFlashControllerVirtualDriveCount':cfprStorageFlexFlashControllerVirtualDriveCount,'cfprStorageFlexFlashControllerVoltage':cfprStorageFlexFlashControllerVoltage,'cfprStorageFlexFlashControllerWriteErrorThreshold':cfprStorageFlexFlashControllerWriteErrorThreshold,'cfprStorageFlexFlashControllerFsmTable':cfprStorageFlexFlashControllerFsmTable,'cfprStorageFlexFlashControllerFsmEntry':cfprStorageFlexFlashControllerFsmEntry,_S:cfprStorageFlexFlashControllerFsmInstanceId,'cfprStorageFlexFlashControllerFsmDn':cfprStorageFlexFlashControllerFsmDn,'cfprStorageFlexFlashControllerFsmRn':cfprStorageFlexFlashControllerFsmRn,'cfprStorageFlexFlashControllerFsmCompletionTime':cfprStorageFlexFlashControllerFsmCompletionTime,'cfprStorageFlexFlashControllerFsmCurrentFsm':cfprStorageFlexFlashControllerFsmCurrentFsm,'cfprStorageFlexFlashControllerFsmDescrData':cfprStorageFlexFlashControllerFsmDescrData,'cfprStorageFlexFlashControllerFsmFsmStatus':cfprStorageFlexFlashControllerFsmFsmStatus,'cfprStorageFlexFlashControllerFsmProgress':cfprStorageFlexFlashControllerFsmProgress,'cfprStorageFlexFlashControllerFsmRmtErrCode':cfprStorageFlexFlashControllerFsmRmtErrCode,'cfprStorageFlexFlashControllerFsmRmtErrDescr':cfprStorageFlexFlashControllerFsmRmtErrDescr,'cfprStorageFlexFlashControllerFsmRmtRslt':cfprStorageFlexFlashControllerFsmRmtRslt,'cfprStorageFlexFlashControllerFsmStageTable':cfprStorageFlexFlashControllerFsmStageTable,'cfprStorageFlexFlashControllerFsmStageEntry':cfprStorageFlexFlashControllerFsmStageEntry,_T:cfprStorageFlexFlashControllerFsmStageInstanceId,'cfprStorageFlexFlashControllerFsmStageDn':cfprStorageFlexFlashControllerFsmStageDn,'cfprStorageFlexFlashControllerFsmStageRn':cfprStorageFlexFlashControllerFsmStageRn,'cfprStorageFlexFlashControllerFsmStageDescrData':cfprStorageFlexFlashControllerFsmStageDescrData,'cfprStorageFlexFlashControllerFsmStageLastUpdateTime':cfprStorageFlexFlashControllerFsmStageLastUpdateTime,'cfprStorageFlexFlashControllerFsmStageName':cfprStorageFlexFlashControllerFsmStageName,'cfprStorageFlexFlashControllerFsmStageOrder':cfprStorageFlexFlashControllerFsmStageOrder,'cfprStorageFlexFlashControllerFsmStageRetry':cfprStorageFlexFlashControllerFsmStageRetry,'cfprStorageFlexFlashControllerFsmStageStageStatus':cfprStorageFlexFlashControllerFsmStageStageStatus,'cfprStorageFlexFlashControllerFsmTaskTable':cfprStorageFlexFlashControllerFsmTaskTable,'cfprStorageFlexFlashControllerFsmTaskEntry':cfprStorageFlexFlashControllerFsmTaskEntry,_U:cfprStorageFlexFlashControllerFsmTaskInstanceId,'cfprStorageFlexFlashControllerFsmTaskDn':cfprStorageFlexFlashControllerFsmTaskDn,'cfprStorageFlexFlashControllerFsmTaskRn':cfprStorageFlexFlashControllerFsmTaskRn,'cfprStorageFlexFlashControllerFsmTaskCompletion':cfprStorageFlexFlashControllerFsmTaskCompletion,'cfprStorageFlexFlashControllerFsmTaskFlags':cfprStorageFlexFlashControllerFsmTaskFlags,'cfprStorageFlexFlashControllerFsmTaskItem':cfprStorageFlexFlashControllerFsmTaskItem,'cfprStorageFlexFlashControllerFsmTaskSeqId':cfprStorageFlexFlashControllerFsmTaskSeqId,'cfprStorageFlexFlashDriveTable':cfprStorageFlexFlashDriveTable,'cfprStorageFlexFlashDriveEntry':cfprStorageFlexFlashDriveEntry,_V:cfprStorageFlexFlashDriveInstanceId,'cfprStorageFlexFlashDriveDn':cfprStorageFlexFlashDriveDn,'cfprStorageFlexFlashDriveRn':cfprStorageFlexFlashDriveRn,'cfprStorageFlexFlashDriveRWType':cfprStorageFlexFlashDriveRWType,'cfprStorageFlexFlashDriveBlockSize':cfprStorageFlexFlashDriveBlockSize,'cfprStorageFlexFlashDriveConnectionProtocol':cfprStorageFlexFlashDriveConnectionProtocol,'cfprStorageFlexFlashDriveControllerIndex':cfprStorageFlexFlashDriveControllerIndex,'cfprStorageFlexFlashDriveDriveState':cfprStorageFlexFlashDriveDriveState,'cfprStorageFlexFlashDriveDriveType':cfprStorageFlexFlashDriveDriveType,'cfprStorageFlexFlashDriveId':cfprStorageFlexFlashDriveId,'cfprStorageFlexFlashDriveLastOperation':cfprStorageFlexFlashDriveLastOperation,'cfprStorageFlexFlashDriveModel':cfprStorageFlexFlashDriveModel,'cfprStorageFlexFlashDriveName':cfprStorageFlexFlashDriveName,'cfprStorageFlexFlashDriveNumberOfBlocks':cfprStorageFlexFlashDriveNumberOfBlocks,'cfprStorageFlexFlashDriveOperQualifierReason':cfprStorageFlexFlashDriveOperQualifierReason,'cfprStorageFlexFlashDriveOperability':cfprStorageFlexFlashDriveOperability,'cfprStorageFlexFlashDriveOperationState':cfprStorageFlexFlashDriveOperationState,'cfprStorageFlexFlashDrivePresence':cfprStorageFlexFlashDrivePresence,'cfprStorageFlexFlashDriveRemovable':cfprStorageFlexFlashDriveRemovable,'cfprStorageFlexFlashDriveRevision':cfprStorageFlexFlashDriveRevision,'cfprStorageFlexFlashDriveSerial':cfprStorageFlexFlashDriveSerial,'cfprStorageFlexFlashDriveSize':cfprStorageFlexFlashDriveSize,'cfprStorageFlexFlashDriveSlotNumber':cfprStorageFlexFlashDriveSlotNumber,'cfprStorageFlexFlashDriveVendor':cfprStorageFlexFlashDriveVendor,'cfprStorageFlexFlashDriveVisible':cfprStorageFlexFlashDriveVisible,'cfprStorageFlexFlashVirtualDriveTable':cfprStorageFlexFlashVirtualDriveTable,'cfprStorageFlexFlashVirtualDriveEntry':cfprStorageFlexFlashVirtualDriveEntry,_W:cfprStorageFlexFlashVirtualDriveInstanceId,'cfprStorageFlexFlashVirtualDriveDn':cfprStorageFlexFlashVirtualDriveDn,'cfprStorageFlexFlashVirtualDriveRn':cfprStorageFlexFlashVirtualDriveRn,'cfprStorageFlexFlashVirtualDriveBlockSize':cfprStorageFlexFlashVirtualDriveBlockSize,'cfprStorageFlexFlashVirtualDriveConnectionProtocol':cfprStorageFlexFlashVirtualDriveConnectionProtocol,'cfprStorageFlexFlashVirtualDriveId':cfprStorageFlexFlashVirtualDriveId,'cfprStorageFlexFlashVirtualDriveModel':cfprStorageFlexFlashVirtualDriveModel,'cfprStorageFlexFlashVirtualDriveNumberOfBlocks':cfprStorageFlexFlashVirtualDriveNumberOfBlocks,'cfprStorageFlexFlashVirtualDriveOperQualifierReason':cfprStorageFlexFlashVirtualDriveOperQualifierReason,'cfprStorageFlexFlashVirtualDriveOperability':cfprStorageFlexFlashVirtualDriveOperability,'cfprStorageFlexFlashVirtualDrivePresence':cfprStorageFlexFlashVirtualDrivePresence,'cfprStorageFlexFlashVirtualDriveRaidHealth':cfprStorageFlexFlashVirtualDriveRaidHealth,'cfprStorageFlexFlashVirtualDriveRaidState':cfprStorageFlexFlashVirtualDriveRaidState,'cfprStorageFlexFlashVirtualDriveRevision':cfprStorageFlexFlashVirtualDriveRevision,'cfprStorageFlexFlashVirtualDriveSerial':cfprStorageFlexFlashVirtualDriveSerial,'cfprStorageFlexFlashVirtualDriveSize':cfprStorageFlexFlashVirtualDriveSize,'cfprStorageFlexFlashVirtualDriveType':cfprStorageFlexFlashVirtualDriveType,'cfprStorageFlexFlashVirtualDriveVendor':cfprStorageFlexFlashVirtualDriveVendor,'cfprStorageIScsiTargetIfTable':cfprStorageIScsiTargetIfTable,'cfprStorageIScsiTargetIfEntry':cfprStorageIScsiTargetIfEntry,_X:cfprStorageIScsiTargetIfInstanceId,'cfprStorageIScsiTargetIfDn':cfprStorageIScsiTargetIfDn,'cfprStorageIScsiTargetIfRn':cfprStorageIScsiTargetIfRn,'cfprStorageIScsiTargetIfName':cfprStorageIScsiTargetIfName,'cfprStorageIScsiTargetIfProt':cfprStorageIScsiTargetIfProt,'cfprStorageIniGroupTable':cfprStorageIniGroupTable,'cfprStorageIniGroupEntry':cfprStorageIniGroupEntry,_Y:cfprStorageIniGroupInstanceId,'cfprStorageIniGroupDn':cfprStorageIniGroupDn,'cfprStorageIniGroupRn':cfprStorageIniGroupRn,'cfprStorageIniGroupDescr':cfprStorageIniGroupDescr,'cfprStorageIniGroupGroupPolicyName':cfprStorageIniGroupGroupPolicyName,'cfprStorageIniGroupIntId':cfprStorageIniGroupIntId,'cfprStorageIniGroupName':cfprStorageIniGroupName,'cfprStorageIniGroupOperProtocol':cfprStorageIniGroupOperProtocol,'cfprStorageIniGroupOperState':cfprStorageIniGroupOperState,'cfprStorageIniGroupOwner':cfprStorageIniGroupOwner,'cfprStorageIniGroupPolicyLevel':cfprStorageIniGroupPolicyLevel,'cfprStorageIniGroupPolicyName':cfprStorageIniGroupPolicyName,'cfprStorageIniGroupPolicyOwner':cfprStorageIniGroupPolicyOwner,'cfprStorageIniGroupProtocol':cfprStorageIniGroupProtocol,'cfprStorageIniGroupRmtDiskCfgName':cfprStorageIniGroupRmtDiskCfgName,'cfprStorageInitiatorTable':cfprStorageInitiatorTable,'cfprStorageInitiatorEntry':cfprStorageInitiatorEntry,_Z:cfprStorageInitiatorInstanceId,'cfprStorageInitiatorDn':cfprStorageInitiatorDn,'cfprStorageInitiatorRn':cfprStorageInitiatorRn,'cfprStorageInitiatorDescr':cfprStorageInitiatorDescr,'cfprStorageInitiatorDuplicateTarget':cfprStorageInitiatorDuplicateTarget,'cfprStorageInitiatorIntId':cfprStorageInitiatorIntId,'cfprStorageInitiatorName':cfprStorageInitiatorName,'cfprStorageInitiatorOperState':cfprStorageInitiatorOperState,'cfprStorageInitiatorPolicyLevel':cfprStorageInitiatorPolicyLevel,'cfprStorageInitiatorPolicyOwner':cfprStorageInitiatorPolicyOwner,'cfprStorageItemTable':cfprStorageItemTable,'cfprStorageItemEntry':cfprStorageItemEntry,_a:cfprStorageItemInstanceId,'cfprStorageItemDn':cfprStorageItemDn,'cfprStorageItemRn':cfprStorageItemRn,'cfprStorageItemName':cfprStorageItemName,'cfprStorageItemOperState':cfprStorageItemOperState,'cfprStorageItemSize':cfprStorageItemSize,'cfprStorageItemUsed':cfprStorageItemUsed,'cfprStorageLocalDiskTable':cfprStorageLocalDiskTable,'cfprStorageLocalDiskEntry':cfprStorageLocalDiskEntry,_b:cfprStorageLocalDiskInstanceId,'cfprStorageLocalDiskDn':cfprStorageLocalDiskDn,'cfprStorageLocalDiskRn':cfprStorageLocalDiskRn,'cfprStorageLocalDiskBlockSize':cfprStorageLocalDiskBlockSize,'cfprStorageLocalDiskConnectionProtocol':cfprStorageLocalDiskConnectionProtocol,'cfprStorageLocalDiskDeviceType':cfprStorageLocalDiskDeviceType,'cfprStorageLocalDiskDiskState':cfprStorageLocalDiskDiskState,'cfprStorageLocalDiskId':cfprStorageLocalDiskId,'cfprStorageLocalDiskLc':cfprStorageLocalDiskLc,'cfprStorageLocalDiskLinkSpeed':cfprStorageLocalDiskLinkSpeed,'cfprStorageLocalDiskModel':cfprStorageLocalDiskModel,'cfprStorageLocalDiskNumberOfBlocks':cfprStorageLocalDiskNumberOfBlocks,'cfprStorageLocalDiskOperQualifierReason':cfprStorageLocalDiskOperQualifierReason,'cfprStorageLocalDiskOperability':cfprStorageLocalDiskOperability,'cfprStorageLocalDiskPowerState':cfprStorageLocalDiskPowerState,'cfprStorageLocalDiskPresence':cfprStorageLocalDiskPresence,'cfprStorageLocalDiskRevision':cfprStorageLocalDiskRevision,'cfprStorageLocalDiskSerial':cfprStorageLocalDiskSerial,'cfprStorageLocalDiskSize':cfprStorageLocalDiskSize,'cfprStorageLocalDiskVendor':cfprStorageLocalDiskVendor,'cfprStorageLocalDiskConfigDefTable':cfprStorageLocalDiskConfigDefTable,'cfprStorageLocalDiskConfigDefEntry':cfprStorageLocalDiskConfigDefEntry,_c:cfprStorageLocalDiskConfigDefInstanceId,'cfprStorageLocalDiskConfigDefDn':cfprStorageLocalDiskConfigDefDn,'cfprStorageLocalDiskConfigDefRn':cfprStorageLocalDiskConfigDefRn,'cfprStorageLocalDiskConfigDefDescr':cfprStorageLocalDiskConfigDefDescr,'cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState':cfprStorageLocalDiskConfigDefFlexFlashRAIDReportingState,'cfprStorageLocalDiskConfigDefFlexFlashState':cfprStorageLocalDiskConfigDefFlexFlashState,'cfprStorageLocalDiskConfigDefIntId':cfprStorageLocalDiskConfigDefIntId,'cfprStorageLocalDiskConfigDefMode':cfprStorageLocalDiskConfigDefMode,'cfprStorageLocalDiskConfigDefName':cfprStorageLocalDiskConfigDefName,'cfprStorageLocalDiskConfigDefPolicyLevel':cfprStorageLocalDiskConfigDefPolicyLevel,'cfprStorageLocalDiskConfigDefPolicyOwner':cfprStorageLocalDiskConfigDefPolicyOwner,'cfprStorageLocalDiskConfigDefProtectConfig':cfprStorageLocalDiskConfigDefProtectConfig,'cfprStorageLocalDiskConfigPolicyTable':cfprStorageLocalDiskConfigPolicyTable,'cfprStorageLocalDiskConfigPolicyEntry':cfprStorageLocalDiskConfigPolicyEntry,_d:cfprStorageLocalDiskConfigPolicyInstanceId,'cfprStorageLocalDiskConfigPolicyDn':cfprStorageLocalDiskConfigPolicyDn,'cfprStorageLocalDiskConfigPolicyRn':cfprStorageLocalDiskConfigPolicyRn,'cfprStorageLocalDiskConfigPolicyDescr':cfprStorageLocalDiskConfigPolicyDescr,'cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState':cfprStorageLocalDiskConfigPolicyFlexFlashRAIDReportingState,'cfprStorageLocalDiskConfigPolicyFlexFlashState':cfprStorageLocalDiskConfigPolicyFlexFlashState,'cfprStorageLocalDiskConfigPolicyIntId':cfprStorageLocalDiskConfigPolicyIntId,'cfprStorageLocalDiskConfigPolicyMode':cfprStorageLocalDiskConfigPolicyMode,'cfprStorageLocalDiskConfigPolicyName':cfprStorageLocalDiskConfigPolicyName,'cfprStorageLocalDiskConfigPolicyPolicyLevel':cfprStorageLocalDiskConfigPolicyPolicyLevel,'cfprStorageLocalDiskConfigPolicyPolicyOwner':cfprStorageLocalDiskConfigPolicyPolicyOwner,'cfprStorageLocalDiskConfigPolicyProtectConfig':cfprStorageLocalDiskConfigPolicyProtectConfig,'cfprStorageLocalDiskPartitionTable':cfprStorageLocalDiskPartitionTable,'cfprStorageLocalDiskPartitionEntry':cfprStorageLocalDiskPartitionEntry,_e:cfprStorageLocalDiskPartitionInstanceId,'cfprStorageLocalDiskPartitionDn':cfprStorageLocalDiskPartitionDn,'cfprStorageLocalDiskPartitionRn':cfprStorageLocalDiskPartitionRn,'cfprStorageLocalDiskPartitionDescr':cfprStorageLocalDiskPartitionDescr,'cfprStorageLocalDiskPartitionIntId':cfprStorageLocalDiskPartitionIntId,'cfprStorageLocalDiskPartitionName':cfprStorageLocalDiskPartitionName,'cfprStorageLocalDiskPartitionOrder':cfprStorageLocalDiskPartitionOrder,'cfprStorageLocalDiskPartitionPolicyLevel':cfprStorageLocalDiskPartitionPolicyLevel,'cfprStorageLocalDiskPartitionPolicyOwner':cfprStorageLocalDiskPartitionPolicyOwner,'cfprStorageLocalDiskPartitionSize':cfprStorageLocalDiskPartitionSize,'cfprStorageLocalDiskPartitionType':cfprStorageLocalDiskPartitionType,'cfprStorageLocalDiskSlotEpTable':cfprStorageLocalDiskSlotEpTable,'cfprStorageLocalDiskSlotEpEntry':cfprStorageLocalDiskSlotEpEntry,_f:cfprStorageLocalDiskSlotEpInstanceId,'cfprStorageLocalDiskSlotEpDn':cfprStorageLocalDiskSlotEpDn,'cfprStorageLocalDiskSlotEpRn':cfprStorageLocalDiskSlotEpRn,'cfprStorageLocalDiskSlotEpConfiguration':cfprStorageLocalDiskSlotEpConfiguration,'cfprStorageLocalDiskSlotEpId':cfprStorageLocalDiskSlotEpId,'cfprStorageLocalDiskSlotEpOperQualifierReason':cfprStorageLocalDiskSlotEpOperQualifierReason,'cfprStorageLocalDiskSlotEpOperability':cfprStorageLocalDiskSlotEpOperability,'cfprStorageLocalDiskSlotEpPeerDn':cfprStorageLocalDiskSlotEpPeerDn,'cfprStorageLocalDiskSlotEpPresence':cfprStorageLocalDiskSlotEpPresence,'cfprStorageLocalLunTable':cfprStorageLocalLunTable,'cfprStorageLocalLunEntry':cfprStorageLocalLunEntry,_g:cfprStorageLocalLunInstanceId,'cfprStorageLocalLunDn':cfprStorageLocalLunDn,'cfprStorageLocalLunRn':cfprStorageLocalLunRn,'cfprStorageLocalLunBlockSize':cfprStorageLocalLunBlockSize,'cfprStorageLocalLunConnectionProtocol':cfprStorageLocalLunConnectionProtocol,'cfprStorageLocalLunId':cfprStorageLocalLunId,'cfprStorageLocalLunLc':cfprStorageLocalLunLc,'cfprStorageLocalLunModel':cfprStorageLocalLunModel,'cfprStorageLocalLunNumberOfBlocks':cfprStorageLocalLunNumberOfBlocks,'cfprStorageLocalLunOperQualifierReason':cfprStorageLocalLunOperQualifierReason,'cfprStorageLocalLunOperability':cfprStorageLocalLunOperability,'cfprStorageLocalLunPresence':cfprStorageLocalLunPresence,'cfprStorageLocalLunRevision':cfprStorageLocalLunRevision,'cfprStorageLocalLunSerial':cfprStorageLocalLunSerial,'cfprStorageLocalLunSize':cfprStorageLocalLunSize,'cfprStorageLocalLunType':cfprStorageLocalLunType,'cfprStorageLocalLunVendor':cfprStorageLocalLunVendor,'cfprStorageLunDiskTable':cfprStorageLunDiskTable,'cfprStorageLunDiskEntry':cfprStorageLunDiskEntry,_h:cfprStorageLunDiskInstanceId,'cfprStorageLunDiskDn':cfprStorageLunDiskDn,'cfprStorageLunDiskRn':cfprStorageLunDiskRn,'cfprStorageLunDiskId':cfprStorageLunDiskId,'cfprStorageMezzFlashLifeTable':cfprStorageMezzFlashLifeTable,'cfprStorageMezzFlashLifeEntry':cfprStorageMezzFlashLifeEntry,_i:cfprStorageMezzFlashLifeInstanceId,'cfprStorageMezzFlashLifeDn':cfprStorageMezzFlashLifeDn,'cfprStorageMezzFlashLifeRn':cfprStorageMezzFlashLifeRn,'cfprStorageMezzFlashLifeBlockSize':cfprStorageMezzFlashLifeBlockSize,'cfprStorageMezzFlashLifeConnectionProtocol':cfprStorageMezzFlashLifeConnectionProtocol,'cfprStorageMezzFlashLifeFlashPercentage':cfprStorageMezzFlashLifeFlashPercentage,'cfprStorageMezzFlashLifeFlashStatus':cfprStorageMezzFlashLifeFlashStatus,'cfprStorageMezzFlashLifeId':cfprStorageMezzFlashLifeId,'cfprStorageMezzFlashLifeModel':cfprStorageMezzFlashLifeModel,'cfprStorageMezzFlashLifeNumberOfBlocks':cfprStorageMezzFlashLifeNumberOfBlocks,'cfprStorageMezzFlashLifeOperQualifierReason':cfprStorageMezzFlashLifeOperQualifierReason,'cfprStorageMezzFlashLifeOperability':cfprStorageMezzFlashLifeOperability,'cfprStorageMezzFlashLifePresence':cfprStorageMezzFlashLifePresence,'cfprStorageMezzFlashLifeRevision':cfprStorageMezzFlashLifeRevision,'cfprStorageMezzFlashLifeSerial':cfprStorageMezzFlashLifeSerial,'cfprStorageMezzFlashLifeSize':cfprStorageMezzFlashLifeSize,'cfprStorageMezzFlashLifeVendor':cfprStorageMezzFlashLifeVendor,'cfprStorageNodeEpTable':cfprStorageNodeEpTable,'cfprStorageNodeEpEntry':cfprStorageNodeEpEntry,_j:cfprStorageNodeEpInstanceId,'cfprStorageNodeEpDn':cfprStorageNodeEpDn,'cfprStorageNodeEpRn':cfprStorageNodeEpRn,'cfprStorageNodeEpEpDn':cfprStorageNodeEpEpDn,'cfprStorageNodeEpId':cfprStorageNodeEpId,'cfprStorageOperationTable':cfprStorageOperationTable,'cfprStorageOperationEntry':cfprStorageOperationEntry,_k:cfprStorageOperationInstanceId,'cfprStorageOperationDn':cfprStorageOperationDn,'cfprStorageOperationRn':cfprStorageOperationRn,'cfprStorageOperationEndTime':cfprStorageOperationEndTime,'cfprStorageOperationName':cfprStorageOperationName,'cfprStorageOperationOperState':cfprStorageOperationOperState,'cfprStorageOperationProgress':cfprStorageOperationProgress,'cfprStorageOperationStartTime':cfprStorageOperationStartTime,'cfprStorageOperationStatusDescr':cfprStorageOperationStatusDescr,'cfprStorageQualTable':cfprStorageQualTable,'cfprStorageQualEntry':cfprStorageQualEntry,_l:cfprStorageQualInstanceId,'cfprStorageQualDn':cfprStorageQualDn,'cfprStorageQualRn':cfprStorageQualRn,'cfprStorageQualBlockSize':cfprStorageQualBlockSize,'cfprStorageQualDiskless':cfprStorageQualDiskless,'cfprStorageQualMaxCap':cfprStorageQualMaxCap,'cfprStorageQualMinCap':cfprStorageQualMinCap,'cfprStorageQualNumberOfBlocks':cfprStorageQualNumberOfBlocks,'cfprStorageQualNumberOfFlexFlashCards':cfprStorageQualNumberOfFlexFlashCards,'cfprStorageQualPerDiskCap':cfprStorageQualPerDiskCap,'cfprStorageQualUnits':cfprStorageQualUnits,'cfprStorageRaidBatteryTable':cfprStorageRaidBatteryTable,'cfprStorageRaidBatteryEntry':cfprStorageRaidBatteryEntry,_m:cfprStorageRaidBatteryInstanceId,'cfprStorageRaidBatteryDn':cfprStorageRaidBatteryDn,'cfprStorageRaidBatteryRn':cfprStorageRaidBatteryRn,'cfprStorageRaidBatteryBatteryType':cfprStorageRaidBatteryBatteryType,'cfprStorageRaidBatteryBbuStatus':cfprStorageRaidBatteryBbuStatus,'cfprStorageRaidBatteryBlockSize':cfprStorageRaidBatteryBlockSize,'cfprStorageRaidBatteryCapacityPercentage':cfprStorageRaidBatteryCapacityPercentage,'cfprStorageRaidBatteryConnectionProtocol':cfprStorageRaidBatteryConnectionProtocol,'cfprStorageRaidBatteryId':cfprStorageRaidBatteryId,'cfprStorageRaidBatteryLc':cfprStorageRaidBatteryLc,'cfprStorageRaidBatteryLearnCycleRequested':cfprStorageRaidBatteryLearnCycleRequested,'cfprStorageRaidBatteryLearnMode':cfprStorageRaidBatteryLearnMode,'cfprStorageRaidBatteryModel':cfprStorageRaidBatteryModel,'cfprStorageRaidBatteryNextLearnCycleTs':cfprStorageRaidBatteryNextLearnCycleTs,'cfprStorageRaidBatteryNumberOfBlocks':cfprStorageRaidBatteryNumberOfBlocks,'cfprStorageRaidBatteryOperQualifierReason':cfprStorageRaidBatteryOperQualifierReason,'cfprStorageRaidBatteryOperability':cfprStorageRaidBatteryOperability,'cfprStorageRaidBatteryOperabilityQualifier':cfprStorageRaidBatteryOperabilityQualifier,'cfprStorageRaidBatteryOperabilityQualifierReason':cfprStorageRaidBatteryOperabilityQualifierReason,'cfprStorageRaidBatteryPresence':cfprStorageRaidBatteryPresence,'cfprStorageRaidBatteryRevision':cfprStorageRaidBatteryRevision,'cfprStorageRaidBatterySerial':cfprStorageRaidBatterySerial,'cfprStorageRaidBatterySize':cfprStorageRaidBatterySize,'cfprStorageRaidBatteryTemperature':cfprStorageRaidBatteryTemperature,'cfprStorageRaidBatteryVendor':cfprStorageRaidBatteryVendor,'cfprStorageSystemTable':cfprStorageSystemTable,'cfprStorageSystemEntry':cfprStorageSystemEntry,_n:cfprStorageSystemInstanceId,'cfprStorageSystemDn':cfprStorageSystemDn,'cfprStorageSystemRn':cfprStorageSystemRn,'cfprStorageSystemFsmDescr':cfprStorageSystemFsmDescr,'cfprStorageSystemFsmPrev':cfprStorageSystemFsmPrev,'cfprStorageSystemFsmProgr':cfprStorageSystemFsmProgr,'cfprStorageSystemFsmRmtInvErrCode':cfprStorageSystemFsmRmtInvErrCode,'cfprStorageSystemFsmRmtInvErrDescr':cfprStorageSystemFsmRmtInvErrDescr,'cfprStorageSystemFsmRmtInvRslt':cfprStorageSystemFsmRmtInvRslt,'cfprStorageSystemFsmStageDescr':cfprStorageSystemFsmStageDescr,'cfprStorageSystemFsmStamp':cfprStorageSystemFsmStamp,'cfprStorageSystemFsmStatus':cfprStorageSystemFsmStatus,'cfprStorageSystemFsmTry':cfprStorageSystemFsmTry,'cfprStorageSystemId':cfprStorageSystemId,'cfprStorageSystemName':cfprStorageSystemName,'cfprStorageSystemFsmTable':cfprStorageSystemFsmTable,'cfprStorageSystemFsmEntry':cfprStorageSystemFsmEntry,_o:cfprStorageSystemFsmInstanceId,'cfprStorageSystemFsmDn':cfprStorageSystemFsmDn,'cfprStorageSystemFsmRn':cfprStorageSystemFsmRn,'cfprStorageSystemFsmCompletionTime':cfprStorageSystemFsmCompletionTime,'cfprStorageSystemFsmCurrentFsm':cfprStorageSystemFsmCurrentFsm,'cfprStorageSystemFsmDescrData':cfprStorageSystemFsmDescrData,'cfprStorageSystemFsmFsmStatus':cfprStorageSystemFsmFsmStatus,'cfprStorageSystemFsmProgress':cfprStorageSystemFsmProgress,'cfprStorageSystemFsmRmtErrCode':cfprStorageSystemFsmRmtErrCode,'cfprStorageSystemFsmRmtErrDescr':cfprStorageSystemFsmRmtErrDescr,'cfprStorageSystemFsmRmtRslt':cfprStorageSystemFsmRmtRslt,'cfprStorageSystemFsmStageTable':cfprStorageSystemFsmStageTable,'cfprStorageSystemFsmStageEntry':cfprStorageSystemFsmStageEntry,_p:cfprStorageSystemFsmStageInstanceId,'cfprStorageSystemFsmStageDn':cfprStorageSystemFsmStageDn,'cfprStorageSystemFsmStageRn':cfprStorageSystemFsmStageRn,'cfprStorageSystemFsmStageDescrData':cfprStorageSystemFsmStageDescrData,'cfprStorageSystemFsmStageLastUpdateTime':cfprStorageSystemFsmStageLastUpdateTime,'cfprStorageSystemFsmStageName':cfprStorageSystemFsmStageName,'cfprStorageSystemFsmStageOrder':cfprStorageSystemFsmStageOrder,'cfprStorageSystemFsmStageRetry':cfprStorageSystemFsmStageRetry,'cfprStorageSystemFsmStageStageStatus':cfprStorageSystemFsmStageStageStatus,'cfprStorageSystemFsmTaskTable':cfprStorageSystemFsmTaskTable,'cfprStorageSystemFsmTaskEntry':cfprStorageSystemFsmTaskEntry,_q:cfprStorageSystemFsmTaskInstanceId,'cfprStorageSystemFsmTaskDn':cfprStorageSystemFsmTaskDn,'cfprStorageSystemFsmTaskRn':cfprStorageSystemFsmTaskRn,'cfprStorageSystemFsmTaskCompletion':cfprStorageSystemFsmTaskCompletion,'cfprStorageSystemFsmTaskFlags':cfprStorageSystemFsmTaskFlags,'cfprStorageSystemFsmTaskItem':cfprStorageSystemFsmTaskItem,'cfprStorageSystemFsmTaskSeqId':cfprStorageSystemFsmTaskSeqId,'cfprStorageTransportableFlashModuleTable':cfprStorageTransportableFlashModuleTable,'cfprStorageTransportableFlashModuleEntry':cfprStorageTransportableFlashModuleEntry,_r:cfprStorageTransportableFlashModuleInstanceId,'cfprStorageTransportableFlashModuleDn':cfprStorageTransportableFlashModuleDn,'cfprStorageTransportableFlashModuleRn':cfprStorageTransportableFlashModuleRn,'cfprStorageTransportableFlashModuleBlockSize':cfprStorageTransportableFlashModuleBlockSize,'cfprStorageTransportableFlashModuleConnectionProtocol':cfprStorageTransportableFlashModuleConnectionProtocol,'cfprStorageTransportableFlashModuleId':cfprStorageTransportableFlashModuleId,'cfprStorageTransportableFlashModuleModel':cfprStorageTransportableFlashModuleModel,'cfprStorageTransportableFlashModuleNumberOfBlocks':cfprStorageTransportableFlashModuleNumberOfBlocks,'cfprStorageTransportableFlashModuleOperQualifierReason':cfprStorageTransportableFlashModuleOperQualifierReason,'cfprStorageTransportableFlashModuleOperability':cfprStorageTransportableFlashModuleOperability,'cfprStorageTransportableFlashModulePresence':cfprStorageTransportableFlashModulePresence,'cfprStorageTransportableFlashModuleRevision':cfprStorageTransportableFlashModuleRevision,'cfprStorageTransportableFlashModuleSerial':cfprStorageTransportableFlashModuleSerial,'cfprStorageTransportableFlashModuleSize':cfprStorageTransportableFlashModuleSize,'cfprStorageTransportableFlashModuleVendor':cfprStorageTransportableFlashModuleVendor,'cfprStorageVirtualDriveTable':cfprStorageVirtualDriveTable,'cfprStorageVirtualDriveEntry':cfprStorageVirtualDriveEntry,_s:cfprStorageVirtualDriveInstanceId,'cfprStorageVirtualDriveDn':cfprStorageVirtualDriveDn,'cfprStorageVirtualDriveRn':cfprStorageVirtualDriveRn,'cfprStorageVirtualDriveAccessPolicy':cfprStorageVirtualDriveAccessPolicy,'cfprStorageVirtualDriveActualWriteCachePolicy':cfprStorageVirtualDriveActualWriteCachePolicy,'cfprStorageVirtualDriveBlockSize':cfprStorageVirtualDriveBlockSize,'cfprStorageVirtualDriveBootable':cfprStorageVirtualDriveBootable,'cfprStorageVirtualDriveConfiguredWriteCachePolicy':cfprStorageVirtualDriveConfiguredWriteCachePolicy,'cfprStorageVirtualDriveConnectionProtocol':cfprStorageVirtualDriveConnectionProtocol,'cfprStorageVirtualDriveDriveCache':cfprStorageVirtualDriveDriveCache,'cfprStorageVirtualDriveDriveState':cfprStorageVirtualDriveDriveState,'cfprStorageVirtualDriveId':cfprStorageVirtualDriveId,'cfprStorageVirtualDriveIoPolicy':cfprStorageVirtualDriveIoPolicy,'cfprStorageVirtualDriveLc':cfprStorageVirtualDriveLc,'cfprStorageVirtualDriveModel':cfprStorageVirtualDriveModel,'cfprStorageVirtualDriveNumberOfBlocks':cfprStorageVirtualDriveNumberOfBlocks,'cfprStorageVirtualDriveOperQualifierReason':cfprStorageVirtualDriveOperQualifierReason,'cfprStorageVirtualDriveOperability':cfprStorageVirtualDriveOperability,'cfprStorageVirtualDrivePresence':cfprStorageVirtualDrivePresence,'cfprStorageVirtualDriveReadPolicy':cfprStorageVirtualDriveReadPolicy,'cfprStorageVirtualDriveRevision':cfprStorageVirtualDriveRevision,'cfprStorageVirtualDriveSerial':cfprStorageVirtualDriveSerial,'cfprStorageVirtualDriveSize':cfprStorageVirtualDriveSize,'cfprStorageVirtualDriveStripSize':cfprStorageVirtualDriveStripSize,'cfprStorageVirtualDriveType':cfprStorageVirtualDriveType,'cfprStorageVirtualDriveVendor':cfprStorageVirtualDriveVendor,'cfprStorageVsanRefTable':cfprStorageVsanRefTable,'cfprStorageVsanRefEntry':cfprStorageVsanRefEntry,_t:cfprStorageVsanRefInstanceId,'cfprStorageVsanRefDn':cfprStorageVsanRefDn,'cfprStorageVsanRefRn':cfprStorageVsanRefRn,'cfprStorageVsanRefConfigQualifier':cfprStorageVsanRefConfigQualifier,'cfprStorageVsanRefName':cfprStorageVsanRefName,'cfprStorageVsanRefOperVnetDn':cfprStorageVsanRefOperVnetDn,'cfprStorageVsanRefOperVnetName':cfprStorageVsanRefOperVnetName,'cfprStorageVsanRefSwitchId':cfprStorageVsanRefSwitchId,'cfprStorageVsanRefVnet':cfprStorageVsanRefVnet,'cfprStorageVsanRefZoningState':cfprStorageVsanRefZoningState})