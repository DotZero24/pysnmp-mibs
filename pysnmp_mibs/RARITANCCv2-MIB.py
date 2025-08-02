_z='ccLicenseTerminatedReason'
_y='ccLicensedFeature'
_x='ccTransferOperation'
_w='ccFileType'
_v='ccClusterOperationStatus'
_u='ccClusterOperation'
_t='ccDominionPXFirmwareVersion'
_s='ccSystemMonitorNotificationMessage'
_r='ccSystemMonitorNotificationLevel'
_q='ccNewNumberOfOutlets'
_p='ccOldNumberOfOutlets'
_o='ccMOTDChanges'
_n='ccBannerChanges'
_m='ccScheduledTaskFailureReason'
_l='ccScheduledTaskDescription'
_k='ccDeviceName'
_j='ccHardDisk'
_i='ccLanCard'
_h='ccUserNameTerminated'
_g='ccUserNameInitiated'
_f='modified'
_e='disabled'
_d='enabled'
_c='backup'
_b='failure'
_a='success'
_Z='ccDiagnosticConsoleMAX-ACCESSLevel'
_Y='ccLeafNodeFirmwareVersion'
_X='ccUserWhoDeleted'
_W='ccUserWhoAdded'
_V='ccImageVersionStatus'
_U='ccImageVersion'
_T='ccImageType'
_S='primary'
_R='ccLicenseServer'
_Q='ccClusterPeer'
_P='ccUserGroupName'
_O='ccPortName'
_N='ccNodeName'
_M='ccUserSessionId'
_L='ccSessionType'
_K='ccLeafNodeName'
_J='ccClusterState'
_I='ccUserWhoModified'
_H='ccLeafNodeIPAddress'
_G='Integer32'
_F='ccUserName'
_E='read-write'
_D='ccObjectInstance'
_C='ccObjectName'
_B='current'
_A='RARITANCCv2-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,internet,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','internet','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
raritan=ModuleIdentity((1,3,6,1,4,1,13742))
if mibBuilder.loadTexts:raritan.setRevisions(('2011-04-11 11:08',))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,13742,1))
_EnterpriseManagement_ObjectIdentity=ObjectIdentity
enterpriseManagement=_EnterpriseManagement_ObjectIdentity((1,3,6,1,4,1,13742,1,1))
_CommandCenter_ObjectIdentity=ObjectIdentity
commandCenter=_CommandCenter_ObjectIdentity((1,3,6,1,4,1,13742,1,1,1))
_CcObject_ObjectIdentity=ObjectIdentity
ccObject=_CcObject_ObjectIdentity((1,3,6,1,4,1,13742,1,1,1,0))
_CcObjectName_Type=DisplayString
_CcObjectName_Object=MibScalar
ccObjectName=_CcObjectName_Object((1,3,6,1,4,1,13742,1,1,1,0,1),_CcObjectName_Type())
ccObjectName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccObjectName.setStatus(_B)
_CcObjectInstance_Type=DisplayString
_CcObjectInstance_Object=MibScalar
ccObjectInstance=_CcObjectInstance_Object((1,3,6,1,4,1,13742,1,1,1,0,2),_CcObjectInstance_Type())
ccObjectInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:ccObjectInstance.setStatus(_B)
_CcUserName_Type=DisplayString
_CcUserName_Object=MibScalar
ccUserName=_CcUserName_Object((1,3,6,1,4,1,13742,1,1,1,0,3),_CcUserName_Type())
ccUserName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserName.setStatus(_B)
_CcUserSessionId_Type=DisplayString
_CcUserSessionId_Object=MibScalar
ccUserSessionId=_CcUserSessionId_Object((1,3,6,1,4,1,13742,1,1,1,0,4),_CcUserSessionId_Type())
ccUserSessionId.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserSessionId.setStatus(_B)
_CcUserNameInitiated_Type=DisplayString
_CcUserNameInitiated_Object=MibScalar
ccUserNameInitiated=_CcUserNameInitiated_Object((1,3,6,1,4,1,13742,1,1,1,0,5),_CcUserNameInitiated_Type())
ccUserNameInitiated.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserNameInitiated.setStatus(_B)
_CcUserNameTerminated_Type=DisplayString
_CcUserNameTerminated_Object=MibScalar
ccUserNameTerminated=_CcUserNameTerminated_Object((1,3,6,1,4,1,13742,1,1,1,0,6),_CcUserNameTerminated_Type())
ccUserNameTerminated.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserNameTerminated.setStatus(_B)
_CcImageType_Type=DisplayString
_CcImageType_Object=MibScalar
ccImageType=_CcImageType_Object((1,3,6,1,4,1,13742,1,1,1,0,7),_CcImageType_Type())
ccImageType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccImageType.setStatus(_B)
_CcImageVersion_Type=DisplayString
_CcImageVersion_Object=MibScalar
ccImageVersion=_CcImageVersion_Object((1,3,6,1,4,1,13742,1,1,1,0,8),_CcImageVersion_Type())
ccImageVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ccImageVersion.setStatus(_B)
class _CcImageVersionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_CcImageVersionStatus_Type.__name__=_G
_CcImageVersionStatus_Object=MibScalar
ccImageVersionStatus=_CcImageVersionStatus_Object((1,3,6,1,4,1,13742,1,1,1,0,9),_CcImageVersionStatus_Type())
ccImageVersionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ccImageVersionStatus.setStatus(_B)
_CcUserWhoAdded_Type=DisplayString
_CcUserWhoAdded_Object=MibScalar
ccUserWhoAdded=_CcUserWhoAdded_Object((1,3,6,1,4,1,13742,1,1,1,0,10),_CcUserWhoAdded_Type())
ccUserWhoAdded.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserWhoAdded.setStatus(_B)
_CcUserWhoDeleted_Type=DisplayString
_CcUserWhoDeleted_Object=MibScalar
ccUserWhoDeleted=_CcUserWhoDeleted_Object((1,3,6,1,4,1,13742,1,1,1,0,11),_CcUserWhoDeleted_Type())
ccUserWhoDeleted.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserWhoDeleted.setStatus(_B)
_CcUserWhoModified_Type=DisplayString
_CcUserWhoModified_Object=MibScalar
ccUserWhoModified=_CcUserWhoModified_Object((1,3,6,1,4,1,13742,1,1,1,0,12),_CcUserWhoModified_Type())
ccUserWhoModified.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserWhoModified.setStatus(_B)
_CcNodeName_Type=DisplayString
_CcNodeName_Object=MibScalar
ccNodeName=_CcNodeName_Object((1,3,6,1,4,1,13742,1,1,1,0,13),_CcNodeName_Type())
ccNodeName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccNodeName.setStatus(_B)
class _CcLanCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_c,2)))
_CcLanCard_Type.__name__=_G
_CcLanCard_Object=MibScalar
ccLanCard=_CcLanCard_Object((1,3,6,1,4,1,13742,1,1,1,0,14),_CcLanCard_Type())
ccLanCard.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLanCard.setStatus(_B)
class _CcHardDisk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_c,2)))
_CcHardDisk_Type.__name__=_G
_CcHardDisk_Object=MibScalar
ccHardDisk=_CcHardDisk_Object((1,3,6,1,4,1,13742,1,1,1,0,15),_CcHardDisk_Type())
ccHardDisk.setMaxAccess(_E)
if mibBuilder.loadTexts:ccHardDisk.setStatus(_B)
class _CcSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('serial',1),('kvm',2),('powerOutlet',3),('admin',4),('diagnostics',5)))
_CcSessionType_Type.__name__=_G
_CcSessionType_Object=MibScalar
ccSessionType=_CcSessionType_Object((1,3,6,1,4,1,13742,1,1,1,0,16),_CcSessionType_Type())
ccSessionType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccSessionType.setStatus(_B)
class _CcClusterState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('secondary',2),('standAlone',3)))
_CcClusterState_Type.__name__=_G
_CcClusterState_Object=MibScalar
ccClusterState=_CcClusterState_Object((1,3,6,1,4,1,13742,1,1,1,0,17),_CcClusterState_Type())
ccClusterState.setMaxAccess(_E)
if mibBuilder.loadTexts:ccClusterState.setStatus(_B)
_CcLeafNodeName_Type=DisplayString
_CcLeafNodeName_Object=MibScalar
ccLeafNodeName=_CcLeafNodeName_Object((1,3,6,1,4,1,13742,1,1,1,0,18),_CcLeafNodeName_Type())
ccLeafNodeName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLeafNodeName.setStatus(_B)
_CcLeafNodeIPAddress_Type=DisplayString
_CcLeafNodeIPAddress_Object=MibScalar
ccLeafNodeIPAddress=_CcLeafNodeIPAddress_Object((1,3,6,1,4,1,13742,1,1,1,0,19),_CcLeafNodeIPAddress_Type())
ccLeafNodeIPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLeafNodeIPAddress.setStatus(_B)
_CcLeafNodeFirmwareVersion_Type=DisplayString
_CcLeafNodeFirmwareVersion_Object=MibScalar
ccLeafNodeFirmwareVersion=_CcLeafNodeFirmwareVersion_Object((1,3,6,1,4,1,13742,1,1,1,0,20),_CcLeafNodeFirmwareVersion_Type())
ccLeafNodeFirmwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLeafNodeFirmwareVersion.setStatus(_B)
_CcScheduledTaskDescription_Type=DisplayString
_CcScheduledTaskDescription_Object=MibScalar
ccScheduledTaskDescription=_CcScheduledTaskDescription_Object((1,3,6,1,4,1,13742,1,1,1,0,21),_CcScheduledTaskDescription_Type())
ccScheduledTaskDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:ccScheduledTaskDescription.setStatus(_B)
_CcScheduledTaskFailureReason_Type=DisplayString
_CcScheduledTaskFailureReason_Object=MibScalar
ccScheduledTaskFailureReason=_CcScheduledTaskFailureReason_Object((1,3,6,1,4,1,13742,1,1,1,0,22),_CcScheduledTaskFailureReason_Type())
ccScheduledTaskFailureReason.setMaxAccess(_E)
if mibBuilder.loadTexts:ccScheduledTaskFailureReason.setStatus(_B)
_CcDiagnosticConsoleMAX_ACCESSLevel_Type=DisplayString
_CcDiagnosticConsoleMAX_ACCESSLevel_Object=MibScalar
ccDiagnosticConsoleMAX_ACCESSLevel=_CcDiagnosticConsoleMAX_ACCESSLevel_Object((1,3,6,1,4,1,13742,1,1,1,0,23),_CcDiagnosticConsoleMAX_ACCESSLevel_Type())
ccDiagnosticConsoleMAX_ACCESSLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:ccDiagnosticConsoleMAX_ACCESSLevel.setStatus(_B)
_CcDeviceName_Type=DisplayString
_CcDeviceName_Object=MibScalar
ccDeviceName=_CcDeviceName_Object((1,3,6,1,4,1,13742,1,1,1,0,24),_CcDeviceName_Type())
ccDeviceName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccDeviceName.setStatus(_B)
_CcUserGroupName_Type=DisplayString
_CcUserGroupName_Object=MibScalar
ccUserGroupName=_CcUserGroupName_Object((1,3,6,1,4,1,13742,1,1,1,0,25),_CcUserGroupName_Type())
ccUserGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccUserGroupName.setStatus(_B)
class _CcBannerChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3)))
_CcBannerChanges_Type.__name__=_G
_CcBannerChanges_Object=MibScalar
ccBannerChanges=_CcBannerChanges_Object((1,3,6,1,4,1,13742,1,1,1,0,26),_CcBannerChanges_Type())
ccBannerChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:ccBannerChanges.setStatus(_B)
class _CcMOTDChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3)))
_CcMOTDChanges_Type.__name__=_G
_CcMOTDChanges_Object=MibScalar
ccMOTDChanges=_CcMOTDChanges_Object((1,3,6,1,4,1,13742,1,1,1,0,27),_CcMOTDChanges_Type())
ccMOTDChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:ccMOTDChanges.setStatus(_B)
_CcOldNumberOfOutlets_Type=DisplayString
_CcOldNumberOfOutlets_Object=MibScalar
ccOldNumberOfOutlets=_CcOldNumberOfOutlets_Object((1,3,6,1,4,1,13742,1,1,1,0,28),_CcOldNumberOfOutlets_Type())
ccOldNumberOfOutlets.setMaxAccess(_E)
if mibBuilder.loadTexts:ccOldNumberOfOutlets.setStatus(_B)
_CcNewNumberOfOutlets_Type=DisplayString
_CcNewNumberOfOutlets_Object=MibScalar
ccNewNumberOfOutlets=_CcNewNumberOfOutlets_Object((1,3,6,1,4,1,13742,1,1,1,0,29),_CcNewNumberOfOutlets_Type())
ccNewNumberOfOutlets.setMaxAccess(_E)
if mibBuilder.loadTexts:ccNewNumberOfOutlets.setStatus(_B)
_CcSystemMonitorNotificationLevel_Type=DisplayString
_CcSystemMonitorNotificationLevel_Object=MibScalar
ccSystemMonitorNotificationLevel=_CcSystemMonitorNotificationLevel_Object((1,3,6,1,4,1,13742,1,1,1,0,30),_CcSystemMonitorNotificationLevel_Type())
ccSystemMonitorNotificationLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:ccSystemMonitorNotificationLevel.setStatus(_B)
_CcSystemMonitorNotificationMessage_Type=DisplayString
_CcSystemMonitorNotificationMessage_Object=MibScalar
ccSystemMonitorNotificationMessage=_CcSystemMonitorNotificationMessage_Object((1,3,6,1,4,1,13742,1,1,1,0,31),_CcSystemMonitorNotificationMessage_Type())
ccSystemMonitorNotificationMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:ccSystemMonitorNotificationMessage.setStatus(_B)
_CcDominionPXFirmwareVersion_Type=DisplayString
_CcDominionPXFirmwareVersion_Object=MibScalar
ccDominionPXFirmwareVersion=_CcDominionPXFirmwareVersion_Object((1,3,6,1,4,1,13742,1,1,1,0,32),_CcDominionPXFirmwareVersion_Type())
ccDominionPXFirmwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:ccDominionPXFirmwareVersion.setStatus(_B)
_CcClusterPeer_Type=DisplayString
_CcClusterPeer_Object=MibScalar
ccClusterPeer=_CcClusterPeer_Object((1,3,6,1,4,1,13742,1,1,1,0,33),_CcClusterPeer_Type())
ccClusterPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:ccClusterPeer.setStatus(_B)
_CcClusterOperation_Type=DisplayString
_CcClusterOperation_Object=MibScalar
ccClusterOperation=_CcClusterOperation_Object((1,3,6,1,4,1,13742,1,1,1,0,34),_CcClusterOperation_Type())
ccClusterOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:ccClusterOperation.setStatus(_B)
class _CcClusterOperationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_CcClusterOperationStatus_Type.__name__=_G
_CcClusterOperationStatus_Object=MibScalar
ccClusterOperationStatus=_CcClusterOperationStatus_Object((1,3,6,1,4,1,13742,1,1,1,0,35),_CcClusterOperationStatus_Type())
ccClusterOperationStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ccClusterOperationStatus.setStatus(_B)
class _CcTransferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('export',1),('import',2)))
_CcTransferOperation_Type.__name__=_G
_CcTransferOperation_Object=MibScalar
ccTransferOperation=_CcTransferOperation_Object((1,3,6,1,4,1,13742,1,1,1,0,36),_CcTransferOperation_Type())
ccTransferOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:ccTransferOperation.setStatus(_B)
_CcFileType_Type=DisplayString
_CcFileType_Object=MibScalar
ccFileType=_CcFileType_Object((1,3,6,1,4,1,13742,1,1,1,0,37),_CcFileType_Type())
ccFileType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccFileType.setStatus(_B)
_CcLicensedFeature_Type=DisplayString
_CcLicensedFeature_Object=MibScalar
ccLicensedFeature=_CcLicensedFeature_Object((1,3,6,1,4,1,13742,1,1,1,0,38),_CcLicensedFeature_Type())
ccLicensedFeature.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLicensedFeature.setStatus(_B)
_CcLicenseServer_Type=DisplayString
_CcLicenseServer_Object=MibScalar
ccLicenseServer=_CcLicenseServer_Object((1,3,6,1,4,1,13742,1,1,1,0,39),_CcLicenseServer_Type())
ccLicenseServer.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLicenseServer.setStatus(_B)
_CcLicenseTerminatedReason_Type=DisplayString
_CcLicenseTerminatedReason_Object=MibScalar
ccLicenseTerminatedReason=_CcLicenseTerminatedReason_Object((1,3,6,1,4,1,13742,1,1,1,0,40),_CcLicenseTerminatedReason_Type())
ccLicenseTerminatedReason.setMaxAccess(_E)
if mibBuilder.loadTexts:ccLicenseTerminatedReason.setStatus(_B)
_CcPortName_Type=DisplayString
_CcPortName_Object=MibScalar
ccPortName=_CcPortName_Object((1,3,6,1,4,1,13742,1,1,1,0,41),_CcPortName_Type())
ccPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccPortName.setStatus(_B)
_CcNotify_ObjectIdentity=ObjectIdentity
ccNotify=_CcNotify_ObjectIdentity((1,3,6,1,4,1,13742,1,1,1,1))
ccUnavailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,1))
ccUnavailable.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:ccUnavailable.setStatus(_B)
ccAvailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,2))
ccAvailable.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:ccAvailable.setStatus(_B)
ccUserLogin=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,3))
ccUserLogin.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccUserLogin.setStatus(_B)
ccUserLogout=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,4))
ccUserLogout.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccUserLogout.setStatus(_B)
ccSPortConnectionStarted=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,5))
ccSPortConnectionStarted.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ccSPortConnectionStarted.setStatus(_B)
ccPortConnectionStopped=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,6))
ccPortConnectionStopped.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ccPortConnectionStopped.setStatus(_B)
ccPortConnectionTerminated=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,7))
ccPortConnectionTerminated.setObjects(*((_A,_C),(_A,_D),(_A,_g),(_A,_h),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ccPortConnectionTerminated.setStatus(_B)
ccImageUpgradeStarted=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,8))
ccImageUpgradeStarted.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:ccImageUpgradeStarted.setStatus(_B)
ccImageUpgradeResults=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,9))
ccImageUpgradeResults.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ccImageUpgradeResults.setStatus(_B)
ccUserAdded=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,10))
ccUserAdded.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_W)))
if mibBuilder.loadTexts:ccUserAdded.setStatus(_B)
ccUserDeleted=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,11))
ccUserDeleted.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_X)))
if mibBuilder.loadTexts:ccUserDeleted.setStatus(_B)
ccUserModified=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,12))
ccUserModified.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_I)))
if mibBuilder.loadTexts:ccUserModified.setStatus(_B)
ccUserAuthenticationFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,13))
ccUserAuthenticationFailure.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccUserAuthenticationFailure.setStatus(_B)
ccRootPasswordChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,14))
ccRootPasswordChanged.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:ccRootPasswordChanged.setStatus(_B)
ccLanCardFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,15))
ccLanCardFailure.setObjects(*((_A,_C),(_A,_D),(_A,_i),(_A,_J)))
if mibBuilder.loadTexts:ccLanCardFailure.setStatus(_B)
ccHardDiskFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,16))
ccHardDiskFailure.setObjects(*((_A,_C),(_A,_D),(_A,_j),(_A,_J)))
if mibBuilder.loadTexts:ccHardDiskFailure.setStatus(_B)
ccLeafNodeUnavailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,17))
ccLeafNodeUnavailable.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:ccLeafNodeUnavailable.setStatus(_B)
ccLeafNodeAvailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,18))
ccLeafNodeAvailable.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:ccLeafNodeAvailable.setStatus(_B)
ccIncompatibleDeviceFirmware=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,19))
ccIncompatibleDeviceFirmware.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_H),(_A,_Y)))
if mibBuilder.loadTexts:ccIncompatibleDeviceFirmware.setStatus(_B)
ccDeviceUpgrade=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,20))
ccDeviceUpgrade.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_H),(_A,_Y),(_A,_V)))
if mibBuilder.loadTexts:ccDeviceUpgrade.setStatus(_B)
ccEnterMaintenanceMode=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,21))
ccEnterMaintenanceMode.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccEnterMaintenanceMode.setStatus(_B)
ccExitMaintenanceMode=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,22))
ccExitMaintenanceMode.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccExitMaintenanceMode.setStatus(_B)
ccUserLockedOut=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,23))
ccUserLockedOut.setObjects(*((_A,_C),(_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ccUserLockedOut.setStatus(_B)
ccDeviceAddedAfterCCNOCNotification=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,24))
ccDeviceAddedAfterCCNOCNotification.setObjects(*((_A,_C),(_A,_D),(_A,_k),(_A,_H)))
if mibBuilder.loadTexts:ccDeviceAddedAfterCCNOCNotification.setStatus(_B)
ccScheduledTaskExecutionFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,25))
ccScheduledTaskExecutionFailure.setObjects(*((_A,_C),(_A,_D),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ccScheduledTaskExecutionFailure.setStatus(_B)
ccDiagnosticConsoleLogin=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,26))
ccDiagnosticConsoleLogin.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:ccDiagnosticConsoleLogin.setStatus(_B)
ccDiagnosticConsoleLogout=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,27))
ccDiagnosticConsoleLogout.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_Z)))
if mibBuilder.loadTexts:ccDiagnosticConsoleLogout.setStatus(_B)
ccNOCAvailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,28))
ccNOCAvailable.setObjects(*((_A,_C),(_A,_D),(_A,_H)))
if mibBuilder.loadTexts:ccNOCAvailable.setStatus(_B)
ccNOCUnavailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,29))
ccNOCUnavailable.setObjects(*((_A,_C),(_A,_D),(_A,_H)))
if mibBuilder.loadTexts:ccNOCUnavailable.setStatus(_B)
ccUserGroupAdded=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,30))
ccUserGroupAdded.setObjects(*((_A,_C),(_A,_D),(_A,_P),(_A,_W)))
if mibBuilder.loadTexts:ccUserGroupAdded.setStatus(_B)
ccUserGroupDeleted=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,31))
ccUserGroupDeleted.setObjects(*((_A,_C),(_A,_D),(_A,_P),(_A,_X)))
if mibBuilder.loadTexts:ccUserGroupDeleted.setStatus(_B)
ccUserGroupModified=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,32))
ccUserGroupModified.setObjects(*((_A,_C),(_A,_D),(_A,_P),(_A,_I)))
if mibBuilder.loadTexts:ccUserGroupModified.setStatus(_B)
ccSuperuserNameChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,33))
ccSuperuserNameChanged.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:ccSuperuserNameChanged.setStatus(_B)
ccSuperuserPasswordChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,34))
ccSuperuserPasswordChanged.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:ccSuperuserPasswordChanged.setStatus(_B)
ccLoginBannerChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,35))
ccLoginBannerChanged.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_n)))
if mibBuilder.loadTexts:ccLoginBannerChanged.setStatus(_B)
ccMOTDChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,36))
ccMOTDChanged.setObjects(*((_A,_C),(_A,_D),(_A,_I),(_A,_o)))
if mibBuilder.loadTexts:ccMOTDChanged.setStatus(_B)
ccDominionPXReplaced=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,37))
ccDominionPXReplaced.setObjects(*((_A,_C),(_A,_D),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:ccDominionPXReplaced.setStatus(_B)
ccSystemMonitorNotification=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,38))
ccSystemMonitorNotification.setObjects(*((_A,_C),(_A,_D),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:ccSystemMonitorNotification.setStatus(_B)
ccNeighborhoodActivated=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,39))
ccNeighborhoodActivated.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ccNeighborhoodActivated.setStatus(_B)
ccNeighborhoodUpdated=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,40))
ccNeighborhoodUpdated.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ccNeighborhoodUpdated.setStatus(_B)
ccDominionPXFirmwareChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,41))
ccDominionPXFirmwareChanged.setObjects(*((_A,_C),(_A,_D),(_A,_t)))
if mibBuilder.loadTexts:ccDominionPXFirmwareChanged.setStatus(_B)
ccClusterFailover=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,42))
ccClusterFailover.setObjects(*((_A,_C),(_A,_D),(_A,_Q)))
if mibBuilder.loadTexts:ccClusterFailover.setStatus(_B)
ccClusterBackupFailed=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,43))
ccClusterBackupFailed.setObjects(*((_A,_C),(_A,_D),(_A,_Q)))
if mibBuilder.loadTexts:ccClusterBackupFailed.setStatus(_B)
ccClusterWaitingPeerDetected=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,44))
ccClusterWaitingPeerDetected.setObjects(*((_A,_C),(_A,_D),(_A,_Q)))
if mibBuilder.loadTexts:ccClusterWaitingPeerDetected.setStatus(_B)
ccClusterAction=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,45))
ccClusterAction.setObjects(*((_A,_C),(_A,_D),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ccClusterAction.setStatus(_B)
ccCSVFileTransferred=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,46))
ccCSVFileTransferred.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:ccCSVFileTransferred.setStatus(_B)
ccPIQUnavailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,47))
ccPIQUnavailable.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:ccPIQUnavailable.setStatus(_B)
ccPIQAvailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,48))
ccPIQAvailable.setObjects(*((_A,_C),(_A,_D),(_A,_K),(_A,_H)))
if mibBuilder.loadTexts:ccPIQAvailable.setStatus(_B)
ccLicenseServerUnavailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,49))
ccLicenseServerUnavailable.setObjects(*((_A,_C),(_A,_D),(_A,_R)))
if mibBuilder.loadTexts:ccLicenseServerUnavailable.setStatus(_B)
ccLicenseServerFailover=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,50))
ccLicenseServerFailover.setObjects(*((_A,_C),(_A,_D),(_A,_R)))
if mibBuilder.loadTexts:ccLicenseServerFailover.setStatus(_B)
ccLicenseServerAvailable=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,51))
ccLicenseServerAvailable.setObjects(*((_A,_C),(_A,_D),(_A,_R)))
if mibBuilder.loadTexts:ccLicenseServerAvailable.setStatus(_B)
ccLicenseTerminated=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,52))
ccLicenseTerminated.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ccLicenseTerminated.setStatus(_B)
ccAddLicenseFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,53))
ccAddLicenseFailure.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ccAddLicenseFailure.setStatus(_B)
ccAddFeatureFailure=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,54))
ccAddFeatureFailure.setObjects(*((_A,_C),(_A,_D),(_A,_y)))
if mibBuilder.loadTexts:ccAddFeatureFailure.setStatus(_B)
ccLicenseTerminatedWithReason=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,55))
ccLicenseTerminatedWithReason.setObjects(*((_A,_C),(_A,_D),(_A,_z)))
if mibBuilder.loadTexts:ccLicenseTerminatedWithReason.setStatus(_B)
ccUserPasswordChanged=NotificationType((1,3,6,1,4,1,13742,1,1,1,1,56))
ccUserPasswordChanged.setObjects(*((_A,_C),(_A,_D),(_A,_F),(_A,_I)))
if mibBuilder.loadTexts:ccUserPasswordChanged.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'raritan':raritan,'products':products,'enterpriseManagement':enterpriseManagement,'commandCenter':commandCenter,'ccObject':ccObject,_C:ccObjectName,_D:ccObjectInstance,_F:ccUserName,_M:ccUserSessionId,_g:ccUserNameInitiated,_h:ccUserNameTerminated,_T:ccImageType,_U:ccImageVersion,_V:ccImageVersionStatus,_W:ccUserWhoAdded,_X:ccUserWhoDeleted,_I:ccUserWhoModified,_N:ccNodeName,_i:ccLanCard,_j:ccHardDisk,_L:ccSessionType,_J:ccClusterState,_K:ccLeafNodeName,_H:ccLeafNodeIPAddress,_Y:ccLeafNodeFirmwareVersion,_l:ccScheduledTaskDescription,_m:ccScheduledTaskFailureReason,_Z:ccDiagnosticConsoleMAX_ACCESSLevel,_k:ccDeviceName,_P:ccUserGroupName,_n:ccBannerChanges,_o:ccMOTDChanges,_p:ccOldNumberOfOutlets,_q:ccNewNumberOfOutlets,_r:ccSystemMonitorNotificationLevel,_s:ccSystemMonitorNotificationMessage,_t:ccDominionPXFirmwareVersion,_Q:ccClusterPeer,_u:ccClusterOperation,_v:ccClusterOperationStatus,_x:ccTransferOperation,_w:ccFileType,_y:ccLicensedFeature,_R:ccLicenseServer,_z:ccLicenseTerminatedReason,_O:ccPortName,'ccNotify':ccNotify,'ccUnavailable':ccUnavailable,'ccAvailable':ccAvailable,'ccUserLogin':ccUserLogin,'ccUserLogout':ccUserLogout,'ccSPortConnectionStarted':ccSPortConnectionStarted,'ccPortConnectionStopped':ccPortConnectionStopped,'ccPortConnectionTerminated':ccPortConnectionTerminated,'ccImageUpgradeStarted':ccImageUpgradeStarted,'ccImageUpgradeResults':ccImageUpgradeResults,'ccUserAdded':ccUserAdded,'ccUserDeleted':ccUserDeleted,'ccUserModified':ccUserModified,'ccUserAuthenticationFailure':ccUserAuthenticationFailure,'ccRootPasswordChanged':ccRootPasswordChanged,'ccLanCardFailure':ccLanCardFailure,'ccHardDiskFailure':ccHardDiskFailure,'ccLeafNodeUnavailable':ccLeafNodeUnavailable,'ccLeafNodeAvailable':ccLeafNodeAvailable,'ccIncompatibleDeviceFirmware':ccIncompatibleDeviceFirmware,'ccDeviceUpgrade':ccDeviceUpgrade,'ccEnterMaintenanceMode':ccEnterMaintenanceMode,'ccExitMaintenanceMode':ccExitMaintenanceMode,'ccUserLockedOut':ccUserLockedOut,'ccDeviceAddedAfterCCNOCNotification':ccDeviceAddedAfterCCNOCNotification,'ccScheduledTaskExecutionFailure':ccScheduledTaskExecutionFailure,'ccDiagnosticConsoleLogin':ccDiagnosticConsoleLogin,'ccDiagnosticConsoleLogout':ccDiagnosticConsoleLogout,'ccNOCAvailable':ccNOCAvailable,'ccNOCUnavailable':ccNOCUnavailable,'ccUserGroupAdded':ccUserGroupAdded,'ccUserGroupDeleted':ccUserGroupDeleted,'ccUserGroupModified':ccUserGroupModified,'ccSuperuserNameChanged':ccSuperuserNameChanged,'ccSuperuserPasswordChanged':ccSuperuserPasswordChanged,'ccLoginBannerChanged':ccLoginBannerChanged,'ccMOTDChanged':ccMOTDChanged,'ccDominionPXReplaced':ccDominionPXReplaced,'ccSystemMonitorNotification':ccSystemMonitorNotification,'ccNeighborhoodActivated':ccNeighborhoodActivated,'ccNeighborhoodUpdated':ccNeighborhoodUpdated,'ccDominionPXFirmwareChanged':ccDominionPXFirmwareChanged,'ccClusterFailover':ccClusterFailover,'ccClusterBackupFailed':ccClusterBackupFailed,'ccClusterWaitingPeerDetected':ccClusterWaitingPeerDetected,'ccClusterAction':ccClusterAction,'ccCSVFileTransferred':ccCSVFileTransferred,'ccPIQUnavailable':ccPIQUnavailable,'ccPIQAvailable':ccPIQAvailable,'ccLicenseServerUnavailable':ccLicenseServerUnavailable,'ccLicenseServerFailover':ccLicenseServerFailover,'ccLicenseServerAvailable':ccLicenseServerAvailable,'ccLicenseTerminated':ccLicenseTerminated,'ccAddLicenseFailure':ccAddLicenseFailure,'ccAddFeatureFailure':ccAddFeatureFailure,'ccLicenseTerminatedWithReason':ccLicenseTerminatedWithReason,'ccUserPasswordChanged':ccUserPasswordChanged})