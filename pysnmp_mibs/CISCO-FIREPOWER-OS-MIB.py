_J='cfprOsInstanceInstanceId'
_I='cfprOsControllerFsmTaskInstanceId'
_H='cfprOsControllerFsmStageInstanceId'
_G='cfprOsControllerFsmInstanceId'
_F='cfprOsControllerInstanceId'
_E='cfprOsAgentInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-OS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionRemoteInvRslt,CfprFsmCompletion,CfprFsmFsmStageStatus,CfprHostagAction,CfprHostagAgentType,CfprHostagEvent,CfprOsBootingUpType,CfprOsControllerBootMode,CfprOsControllerFormatDisk,CfprOsControllerFsmCurrentFsm,CfprOsControllerFsmStageName,CfprOsControllerFsmTaskFlags,CfprOsControllerFsmTaskItem,CfprOsDeployState,CfprOsInitState,CfprOsInstallLicenseState,CfprOsOsMode,CfprOsOsType,CfprOsUpgradeReturnCode,CfprOsUpgradeState=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionRemoteInvRslt','CfprFsmCompletion','CfprFsmFsmStageStatus','CfprHostagAction','CfprHostagAgentType','CfprHostagEvent','CfprOsBootingUpType','CfprOsControllerBootMode','CfprOsControllerFormatDisk','CfprOsControllerFsmCurrentFsm','CfprOsControllerFsmStageName','CfprOsControllerFsmTaskFlags','CfprOsControllerFsmTaskItem','CfprOsDeployState','CfprOsInitState','CfprOsInstallLicenseState','CfprOsOsMode','CfprOsOsType','CfprOsUpgradeReturnCode','CfprOsUpgradeState')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprOsObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,59))
_CfprOsAgentTable_Object=MibTable
cfprOsAgentTable=_CfprOsAgentTable_Object((1,3,6,1,4,1,9,9,826,1,59,1))
if mibBuilder.loadTexts:cfprOsAgentTable.setStatus(_A)
_CfprOsAgentEntry_Object=MibTableRow
cfprOsAgentEntry=_CfprOsAgentEntry_Object((1,3,6,1,4,1,9,9,826,1,59,1,1))
cfprOsAgentEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprOsAgentEntry.setStatus(_A)
_CfprOsAgentInstanceId_Type=CfprManagedObjectId
_CfprOsAgentInstanceId_Object=MibTableColumn
cfprOsAgentInstanceId=_CfprOsAgentInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,1),_CfprOsAgentInstanceId_Type())
cfprOsAgentInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsAgentInstanceId.setStatus(_A)
_CfprOsAgentDn_Type=CfprManagedObjectDn
_CfprOsAgentDn_Object=MibTableColumn
cfprOsAgentDn=_CfprOsAgentDn_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,2),_CfprOsAgentDn_Type())
cfprOsAgentDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentDn.setStatus(_A)
_CfprOsAgentRn_Type=SnmpAdminString
_CfprOsAgentRn_Object=MibTableColumn
cfprOsAgentRn=_CfprOsAgentRn_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,3),_CfprOsAgentRn_Type())
cfprOsAgentRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentRn.setStatus(_A)
_CfprOsAgentLastCmd_Type=CfprHostagAction
_CfprOsAgentLastCmd_Object=MibTableColumn
cfprOsAgentLastCmd=_CfprOsAgentLastCmd_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,4),_CfprOsAgentLastCmd_Type())
cfprOsAgentLastCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentLastCmd.setStatus(_A)
_CfprOsAgentLastEvt_Type=CfprHostagEvent
_CfprOsAgentLastEvt_Object=MibTableColumn
cfprOsAgentLastEvt=_CfprOsAgentLastEvt_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,5),_CfprOsAgentLastEvt_Type())
cfprOsAgentLastEvt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentLastEvt.setStatus(_A)
_CfprOsAgentLastEvtTs_Type=DateAndTime
_CfprOsAgentLastEvtTs_Object=MibTableColumn
cfprOsAgentLastEvtTs=_CfprOsAgentLastEvtTs_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,6),_CfprOsAgentLastEvtTs_Type())
cfprOsAgentLastEvtTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentLastEvtTs.setStatus(_A)
_CfprOsAgentPrevCmd_Type=CfprHostagAction
_CfprOsAgentPrevCmd_Object=MibTableColumn
cfprOsAgentPrevCmd=_CfprOsAgentPrevCmd_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,7),_CfprOsAgentPrevCmd_Type())
cfprOsAgentPrevCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentPrevCmd.setStatus(_A)
_CfprOsAgentPrevEvt_Type=CfprHostagEvent
_CfprOsAgentPrevEvt_Object=MibTableColumn
cfprOsAgentPrevEvt=_CfprOsAgentPrevEvt_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,8),_CfprOsAgentPrevEvt_Type())
cfprOsAgentPrevEvt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentPrevEvt.setStatus(_A)
_CfprOsAgentType_Type=CfprHostagAgentType
_CfprOsAgentType_Object=MibTableColumn
cfprOsAgentType=_CfprOsAgentType_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,9),_CfprOsAgentType_Type())
cfprOsAgentType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentType.setStatus(_A)
_CfprOsAgentVendor_Type=SnmpAdminString
_CfprOsAgentVendor_Object=MibTableColumn
cfprOsAgentVendor=_CfprOsAgentVendor_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,10),_CfprOsAgentVendor_Type())
cfprOsAgentVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentVendor.setStatus(_A)
_CfprOsAgentVersion_Type=SnmpAdminString
_CfprOsAgentVersion_Object=MibTableColumn
cfprOsAgentVersion=_CfprOsAgentVersion_Object((1,3,6,1,4,1,9,9,826,1,59,1,1,11),_CfprOsAgentVersion_Type())
cfprOsAgentVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsAgentVersion.setStatus(_A)
_CfprOsControllerTable_Object=MibTable
cfprOsControllerTable=_CfprOsControllerTable_Object((1,3,6,1,4,1,9,9,826,1,59,2))
if mibBuilder.loadTexts:cfprOsControllerTable.setStatus(_A)
_CfprOsControllerEntry_Object=MibTableRow
cfprOsControllerEntry=_CfprOsControllerEntry_Object((1,3,6,1,4,1,9,9,826,1,59,2,1))
cfprOsControllerEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprOsControllerEntry.setStatus(_A)
_CfprOsControllerInstanceId_Type=CfprManagedObjectId
_CfprOsControllerInstanceId_Object=MibTableColumn
cfprOsControllerInstanceId=_CfprOsControllerInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,1),_CfprOsControllerInstanceId_Type())
cfprOsControllerInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsControllerInstanceId.setStatus(_A)
_CfprOsControllerDn_Type=CfprManagedObjectDn
_CfprOsControllerDn_Object=MibTableColumn
cfprOsControllerDn=_CfprOsControllerDn_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,2),_CfprOsControllerDn_Type())
cfprOsControllerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerDn.setStatus(_A)
_CfprOsControllerRn_Type=SnmpAdminString
_CfprOsControllerRn_Object=MibTableColumn
cfprOsControllerRn=_CfprOsControllerRn_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,3),_CfprOsControllerRn_Type())
cfprOsControllerRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerRn.setStatus(_A)
_CfprOsControllerBootMode_Type=CfprOsControllerBootMode
_CfprOsControllerBootMode_Object=MibTableColumn
cfprOsControllerBootMode=_CfprOsControllerBootMode_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,4),_CfprOsControllerBootMode_Type())
cfprOsControllerBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerBootMode.setStatus(_A)
_CfprOsControllerChassisId_Type=Gauge32
_CfprOsControllerChassisId_Object=MibTableColumn
cfprOsControllerChassisId=_CfprOsControllerChassisId_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,5),_CfprOsControllerChassisId_Type())
cfprOsControllerChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerChassisId.setStatus(_A)
_CfprOsControllerDeployState_Type=CfprOsDeployState
_CfprOsControllerDeployState_Object=MibTableColumn
cfprOsControllerDeployState=_CfprOsControllerDeployState_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,6),_CfprOsControllerDeployState_Type())
cfprOsControllerDeployState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerDeployState.setStatus(_A)
_CfprOsControllerEnableDeployOS_Type=TruthValue
_CfprOsControllerEnableDeployOS_Object=MibTableColumn
cfprOsControllerEnableDeployOS=_CfprOsControllerEnableDeployOS_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,7),_CfprOsControllerEnableDeployOS_Type())
cfprOsControllerEnableDeployOS.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerEnableDeployOS.setStatus(_A)
_CfprOsControllerFormatDisk_Type=CfprOsControllerFormatDisk
_CfprOsControllerFormatDisk_Object=MibTableColumn
cfprOsControllerFormatDisk=_CfprOsControllerFormatDisk_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,8),_CfprOsControllerFormatDisk_Type())
cfprOsControllerFormatDisk.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFormatDisk.setStatus(_A)
_CfprOsControllerFsmDescr_Type=SnmpAdminString
_CfprOsControllerFsmDescr_Object=MibTableColumn
cfprOsControllerFsmDescr=_CfprOsControllerFsmDescr_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,9),_CfprOsControllerFsmDescr_Type())
cfprOsControllerFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmDescr.setStatus(_A)
_CfprOsControllerFsmFlags_Type=SnmpAdminString
_CfprOsControllerFsmFlags_Object=MibTableColumn
cfprOsControllerFsmFlags=_CfprOsControllerFsmFlags_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,10),_CfprOsControllerFsmFlags_Type())
cfprOsControllerFsmFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmFlags.setStatus(_A)
_CfprOsControllerFsmPrev_Type=SnmpAdminString
_CfprOsControllerFsmPrev_Object=MibTableColumn
cfprOsControllerFsmPrev=_CfprOsControllerFsmPrev_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,11),_CfprOsControllerFsmPrev_Type())
cfprOsControllerFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmPrev.setStatus(_A)
_CfprOsControllerFsmProgr_Type=Gauge32
_CfprOsControllerFsmProgr_Object=MibTableColumn
cfprOsControllerFsmProgr=_CfprOsControllerFsmProgr_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,12),_CfprOsControllerFsmProgr_Type())
cfprOsControllerFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmProgr.setStatus(_A)
_CfprOsControllerFsmRmtInvErrCode_Type=Gauge32
_CfprOsControllerFsmRmtInvErrCode_Object=MibTableColumn
cfprOsControllerFsmRmtInvErrCode=_CfprOsControllerFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,13),_CfprOsControllerFsmRmtInvErrCode_Type())
cfprOsControllerFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtInvErrCode.setStatus(_A)
_CfprOsControllerFsmRmtInvErrDescr_Type=SnmpAdminString
_CfprOsControllerFsmRmtInvErrDescr_Object=MibTableColumn
cfprOsControllerFsmRmtInvErrDescr=_CfprOsControllerFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,14),_CfprOsControllerFsmRmtInvErrDescr_Type())
cfprOsControllerFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtInvErrDescr.setStatus(_A)
_CfprOsControllerFsmRmtInvRslt_Type=CfprConditionRemoteInvRslt
_CfprOsControllerFsmRmtInvRslt_Object=MibTableColumn
cfprOsControllerFsmRmtInvRslt=_CfprOsControllerFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,15),_CfprOsControllerFsmRmtInvRslt_Type())
cfprOsControllerFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtInvRslt.setStatus(_A)
_CfprOsControllerFsmStageDescr_Type=SnmpAdminString
_CfprOsControllerFsmStageDescr_Object=MibTableColumn
cfprOsControllerFsmStageDescr=_CfprOsControllerFsmStageDescr_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,16),_CfprOsControllerFsmStageDescr_Type())
cfprOsControllerFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageDescr.setStatus(_A)
_CfprOsControllerFsmStamp_Type=DateAndTime
_CfprOsControllerFsmStamp_Object=MibTableColumn
cfprOsControllerFsmStamp=_CfprOsControllerFsmStamp_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,17),_CfprOsControllerFsmStamp_Type())
cfprOsControllerFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStamp.setStatus(_A)
_CfprOsControllerFsmStatus_Type=SnmpAdminString
_CfprOsControllerFsmStatus_Object=MibTableColumn
cfprOsControllerFsmStatus=_CfprOsControllerFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,18),_CfprOsControllerFsmStatus_Type())
cfprOsControllerFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStatus.setStatus(_A)
_CfprOsControllerFsmTry_Type=Gauge32
_CfprOsControllerFsmTry_Object=MibTableColumn
cfprOsControllerFsmTry=_CfprOsControllerFsmTry_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,19),_CfprOsControllerFsmTry_Type())
cfprOsControllerFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTry.setStatus(_A)
_CfprOsControllerHostname_Type=SnmpAdminString
_CfprOsControllerHostname_Object=MibTableColumn
cfprOsControllerHostname=_CfprOsControllerHostname_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,20),_CfprOsControllerHostname_Type())
cfprOsControllerHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerHostname.setStatus(_A)
_CfprOsControllerImageName_Type=SnmpAdminString
_CfprOsControllerImageName_Object=MibTableColumn
cfprOsControllerImageName=_CfprOsControllerImageName_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,21),_CfprOsControllerImageName_Type())
cfprOsControllerImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerImageName.setStatus(_A)
_CfprOsControllerImageSize_Type=Gauge32
_CfprOsControllerImageSize_Object=MibTableColumn
cfprOsControllerImageSize=_CfprOsControllerImageSize_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,22),_CfprOsControllerImageSize_Type())
cfprOsControllerImageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerImageSize.setStatus(_A)
_CfprOsControllerInitState_Type=CfprOsInitState
_CfprOsControllerInitState_Object=MibTableColumn
cfprOsControllerInitState=_CfprOsControllerInitState_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,23),_CfprOsControllerInitState_Type())
cfprOsControllerInitState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerInitState.setStatus(_A)
_CfprOsControllerMaxNumDeployFailureRecovery_Type=Gauge32
_CfprOsControllerMaxNumDeployFailureRecovery_Object=MibTableColumn
cfprOsControllerMaxNumDeployFailureRecovery=_CfprOsControllerMaxNumDeployFailureRecovery_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,24),_CfprOsControllerMaxNumDeployFailureRecovery_Type())
cfprOsControllerMaxNumDeployFailureRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerMaxNumDeployFailureRecovery.setStatus(_A)
_CfprOsControllerMaxNumberVersionMismatched_Type=Gauge32
_CfprOsControllerMaxNumberVersionMismatched_Object=MibTableColumn
cfprOsControllerMaxNumberVersionMismatched=_CfprOsControllerMaxNumberVersionMismatched_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,25),_CfprOsControllerMaxNumberVersionMismatched_Type())
cfprOsControllerMaxNumberVersionMismatched.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerMaxNumberVersionMismatched.setStatus(_A)
_CfprOsControllerModel_Type=SnmpAdminString
_CfprOsControllerModel_Object=MibTableColumn
cfprOsControllerModel=_CfprOsControllerModel_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,26),_CfprOsControllerModel_Type())
cfprOsControllerModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerModel.setStatus(_A)
_CfprOsControllerName_Type=SnmpAdminString
_CfprOsControllerName_Object=MibTableColumn
cfprOsControllerName=_CfprOsControllerName_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,27),_CfprOsControllerName_Type())
cfprOsControllerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerName.setStatus(_A)
_CfprOsControllerNumDeployFailureRecovery_Type=Gauge32
_CfprOsControllerNumDeployFailureRecovery_Object=MibTableColumn
cfprOsControllerNumDeployFailureRecovery=_CfprOsControllerNumDeployFailureRecovery_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,28),_CfprOsControllerNumDeployFailureRecovery_Type())
cfprOsControllerNumDeployFailureRecovery.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerNumDeployFailureRecovery.setStatus(_A)
_CfprOsControllerNumberVersionMismatched_Type=Gauge32
_CfprOsControllerNumberVersionMismatched_Object=MibTableColumn
cfprOsControllerNumberVersionMismatched=_CfprOsControllerNumberVersionMismatched_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,29),_CfprOsControllerNumberVersionMismatched_Type())
cfprOsControllerNumberVersionMismatched.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerNumberVersionMismatched.setStatus(_A)
_CfprOsControllerPnDn_Type=SnmpAdminString
_CfprOsControllerPnDn_Object=MibTableColumn
cfprOsControllerPnDn=_CfprOsControllerPnDn_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,30),_CfprOsControllerPnDn_Type())
cfprOsControllerPnDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerPnDn.setStatus(_A)
_CfprOsControllerRevision_Type=SnmpAdminString
_CfprOsControllerRevision_Object=MibTableColumn
cfprOsControllerRevision=_CfprOsControllerRevision_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,31),_CfprOsControllerRevision_Type())
cfprOsControllerRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerRevision.setStatus(_A)
_CfprOsControllerRommonBuildDate_Type=SnmpAdminString
_CfprOsControllerRommonBuildDate_Object=MibTableColumn
cfprOsControllerRommonBuildDate=_CfprOsControllerRommonBuildDate_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,32),_CfprOsControllerRommonBuildDate_Type())
cfprOsControllerRommonBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerRommonBuildDate.setStatus(_A)
_CfprOsControllerRommonVersion_Type=SnmpAdminString
_CfprOsControllerRommonVersion_Object=MibTableColumn
cfprOsControllerRommonVersion=_CfprOsControllerRommonVersion_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,33),_CfprOsControllerRommonVersion_Type())
cfprOsControllerRommonVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerRommonVersion.setStatus(_A)
_CfprOsControllerSerial_Type=SnmpAdminString
_CfprOsControllerSerial_Object=MibTableColumn
cfprOsControllerSerial=_CfprOsControllerSerial_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,34),_CfprOsControllerSerial_Type())
cfprOsControllerSerial.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerSerial.setStatus(_A)
_CfprOsControllerServiceStatus_Type=CfprOsBootingUpType
_CfprOsControllerServiceStatus_Object=MibTableColumn
cfprOsControllerServiceStatus=_CfprOsControllerServiceStatus_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,35),_CfprOsControllerServiceStatus_Type())
cfprOsControllerServiceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerServiceStatus.setStatus(_A)
_CfprOsControllerSlotId_Type=Gauge32
_CfprOsControllerSlotId_Object=MibTableColumn
cfprOsControllerSlotId=_CfprOsControllerSlotId_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,36),_CfprOsControllerSlotId_Type())
cfprOsControllerSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerSlotId.setStatus(_A)
_CfprOsControllerSsposMode_Type=CfprOsOsMode
_CfprOsControllerSsposMode_Object=MibTableColumn
cfprOsControllerSsposMode=_CfprOsControllerSsposMode_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,37),_CfprOsControllerSsposMode_Type())
cfprOsControllerSsposMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerSsposMode.setStatus(_A)
_CfprOsControllerSupportTftpboot_Type=TruthValue
_CfprOsControllerSupportTftpboot_Object=MibTableColumn
cfprOsControllerSupportTftpboot=_CfprOsControllerSupportTftpboot_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,38),_CfprOsControllerSupportTftpboot_Type())
cfprOsControllerSupportTftpboot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerSupportTftpboot.setStatus(_A)
_CfprOsControllerType_Type=CfprOsOsType
_CfprOsControllerType_Object=MibTableColumn
cfprOsControllerType=_CfprOsControllerType_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,39),_CfprOsControllerType_Type())
cfprOsControllerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerType.setStatus(_A)
_CfprOsControllerUpgradeState_Type=CfprOsUpgradeState
_CfprOsControllerUpgradeState_Object=MibTableColumn
cfprOsControllerUpgradeState=_CfprOsControllerUpgradeState_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,40),_CfprOsControllerUpgradeState_Type())
cfprOsControllerUpgradeState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerUpgradeState.setStatus(_A)
_CfprOsControllerVendor_Type=SnmpAdminString
_CfprOsControllerVendor_Object=MibTableColumn
cfprOsControllerVendor=_CfprOsControllerVendor_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,41),_CfprOsControllerVendor_Type())
cfprOsControllerVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerVendor.setStatus(_A)
_CfprOsControllerVersion_Type=SnmpAdminString
_CfprOsControllerVersion_Object=MibTableColumn
cfprOsControllerVersion=_CfprOsControllerVersion_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,42),_CfprOsControllerVersion_Type())
cfprOsControllerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerVersion.setStatus(_A)
_CfprOsControllerDmaSize_Type=SnmpAdminString
_CfprOsControllerDmaSize_Object=MibTableColumn
cfprOsControllerDmaSize=_CfprOsControllerDmaSize_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,43),_CfprOsControllerDmaSize_Type())
cfprOsControllerDmaSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerDmaSize.setStatus(_A)
_CfprOsControllerHeapSize_Type=SnmpAdminString
_CfprOsControllerHeapSize_Object=MibTableColumn
cfprOsControllerHeapSize=_CfprOsControllerHeapSize_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,44),_CfprOsControllerHeapSize_Type())
cfprOsControllerHeapSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerHeapSize.setStatus(_A)
_CfprOsControllerHugePageSize_Type=SnmpAdminString
_CfprOsControllerHugePageSize_Object=MibTableColumn
cfprOsControllerHugePageSize=_CfprOsControllerHugePageSize_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,45),_CfprOsControllerHugePageSize_Type())
cfprOsControllerHugePageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerHugePageSize.setStatus(_A)
_CfprOsControllerInstallLicenseState_Type=CfprOsInstallLicenseState
_CfprOsControllerInstallLicenseState_Object=MibTableColumn
cfprOsControllerInstallLicenseState=_CfprOsControllerInstallLicenseState_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,46),_CfprOsControllerInstallLicenseState_Type())
cfprOsControllerInstallLicenseState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerInstallLicenseState.setStatus(_A)
_CfprOsControllerNumHugePages_Type=SnmpAdminString
_CfprOsControllerNumHugePages_Object=MibTableColumn
cfprOsControllerNumHugePages=_CfprOsControllerNumHugePages_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,47),_CfprOsControllerNumHugePages_Type())
cfprOsControllerNumHugePages.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerNumHugePages.setStatus(_A)
_CfprOsControllerPti_Type=SnmpAdminString
_CfprOsControllerPti_Object=MibTableColumn
cfprOsControllerPti=_CfprOsControllerPti_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,48),_CfprOsControllerPti_Type())
cfprOsControllerPti.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerPti.setStatus(_A)
_CfprOsControllerSecSmack_Type=TruthValue
_CfprOsControllerSecSmack_Object=MibTableColumn
cfprOsControllerSecSmack=_CfprOsControllerSecSmack_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,49),_CfprOsControllerSecSmack_Type())
cfprOsControllerSecSmack.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerSecSmack.setStatus(_A)
_CfprOsControllerTurboMode_Type=TruthValue
_CfprOsControllerTurboMode_Object=MibTableColumn
cfprOsControllerTurboMode=_CfprOsControllerTurboMode_Object((1,3,6,1,4,1,9,9,826,1,59,2,1,50),_CfprOsControllerTurboMode_Type())
cfprOsControllerTurboMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerTurboMode.setStatus(_A)
_CfprOsControllerFsmTable_Object=MibTable
cfprOsControllerFsmTable=_CfprOsControllerFsmTable_Object((1,3,6,1,4,1,9,9,826,1,59,3))
if mibBuilder.loadTexts:cfprOsControllerFsmTable.setStatus(_A)
_CfprOsControllerFsmEntry_Object=MibTableRow
cfprOsControllerFsmEntry=_CfprOsControllerFsmEntry_Object((1,3,6,1,4,1,9,9,826,1,59,3,1))
cfprOsControllerFsmEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprOsControllerFsmEntry.setStatus(_A)
_CfprOsControllerFsmInstanceId_Type=CfprManagedObjectId
_CfprOsControllerFsmInstanceId_Object=MibTableColumn
cfprOsControllerFsmInstanceId=_CfprOsControllerFsmInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,1),_CfprOsControllerFsmInstanceId_Type())
cfprOsControllerFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsControllerFsmInstanceId.setStatus(_A)
_CfprOsControllerFsmDn_Type=CfprManagedObjectDn
_CfprOsControllerFsmDn_Object=MibTableColumn
cfprOsControllerFsmDn=_CfprOsControllerFsmDn_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,2),_CfprOsControllerFsmDn_Type())
cfprOsControllerFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmDn.setStatus(_A)
_CfprOsControllerFsmRn_Type=SnmpAdminString
_CfprOsControllerFsmRn_Object=MibTableColumn
cfprOsControllerFsmRn=_CfprOsControllerFsmRn_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,3),_CfprOsControllerFsmRn_Type())
cfprOsControllerFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRn.setStatus(_A)
_CfprOsControllerFsmCompletionTime_Type=DateAndTime
_CfprOsControllerFsmCompletionTime_Object=MibTableColumn
cfprOsControllerFsmCompletionTime=_CfprOsControllerFsmCompletionTime_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,4),_CfprOsControllerFsmCompletionTime_Type())
cfprOsControllerFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmCompletionTime.setStatus(_A)
_CfprOsControllerFsmCurrentFsm_Type=CfprOsControllerFsmCurrentFsm
_CfprOsControllerFsmCurrentFsm_Object=MibTableColumn
cfprOsControllerFsmCurrentFsm=_CfprOsControllerFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,5),_CfprOsControllerFsmCurrentFsm_Type())
cfprOsControllerFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmCurrentFsm.setStatus(_A)
_CfprOsControllerFsmDescrData_Type=SnmpAdminString
_CfprOsControllerFsmDescrData_Object=MibTableColumn
cfprOsControllerFsmDescrData=_CfprOsControllerFsmDescrData_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,6),_CfprOsControllerFsmDescrData_Type())
cfprOsControllerFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmDescrData.setStatus(_A)
_CfprOsControllerFsmFsmStatus_Type=CfprFsmFsmStageStatus
_CfprOsControllerFsmFsmStatus_Object=MibTableColumn
cfprOsControllerFsmFsmStatus=_CfprOsControllerFsmFsmStatus_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,7),_CfprOsControllerFsmFsmStatus_Type())
cfprOsControllerFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmFsmStatus.setStatus(_A)
_CfprOsControllerFsmProgress_Type=Gauge32
_CfprOsControllerFsmProgress_Object=MibTableColumn
cfprOsControllerFsmProgress=_CfprOsControllerFsmProgress_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,8),_CfprOsControllerFsmProgress_Type())
cfprOsControllerFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmProgress.setStatus(_A)
_CfprOsControllerFsmRmtErrCode_Type=Gauge32
_CfprOsControllerFsmRmtErrCode_Object=MibTableColumn
cfprOsControllerFsmRmtErrCode=_CfprOsControllerFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,9),_CfprOsControllerFsmRmtErrCode_Type())
cfprOsControllerFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtErrCode.setStatus(_A)
_CfprOsControllerFsmRmtErrDescr_Type=SnmpAdminString
_CfprOsControllerFsmRmtErrDescr_Object=MibTableColumn
cfprOsControllerFsmRmtErrDescr=_CfprOsControllerFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,10),_CfprOsControllerFsmRmtErrDescr_Type())
cfprOsControllerFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtErrDescr.setStatus(_A)
_CfprOsControllerFsmRmtRslt_Type=CfprConditionRemoteInvRslt
_CfprOsControllerFsmRmtRslt_Object=MibTableColumn
cfprOsControllerFsmRmtRslt=_CfprOsControllerFsmRmtRslt_Object((1,3,6,1,4,1,9,9,826,1,59,3,1,11),_CfprOsControllerFsmRmtRslt_Type())
cfprOsControllerFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmRmtRslt.setStatus(_A)
_CfprOsControllerFsmStageTable_Object=MibTable
cfprOsControllerFsmStageTable=_CfprOsControllerFsmStageTable_Object((1,3,6,1,4,1,9,9,826,1,59,4))
if mibBuilder.loadTexts:cfprOsControllerFsmStageTable.setStatus(_A)
_CfprOsControllerFsmStageEntry_Object=MibTableRow
cfprOsControllerFsmStageEntry=_CfprOsControllerFsmStageEntry_Object((1,3,6,1,4,1,9,9,826,1,59,4,1))
cfprOsControllerFsmStageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprOsControllerFsmStageEntry.setStatus(_A)
_CfprOsControllerFsmStageInstanceId_Type=CfprManagedObjectId
_CfprOsControllerFsmStageInstanceId_Object=MibTableColumn
cfprOsControllerFsmStageInstanceId=_CfprOsControllerFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,1),_CfprOsControllerFsmStageInstanceId_Type())
cfprOsControllerFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsControllerFsmStageInstanceId.setStatus(_A)
_CfprOsControllerFsmStageDn_Type=CfprManagedObjectDn
_CfprOsControllerFsmStageDn_Object=MibTableColumn
cfprOsControllerFsmStageDn=_CfprOsControllerFsmStageDn_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,2),_CfprOsControllerFsmStageDn_Type())
cfprOsControllerFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageDn.setStatus(_A)
_CfprOsControllerFsmStageRn_Type=SnmpAdminString
_CfprOsControllerFsmStageRn_Object=MibTableColumn
cfprOsControllerFsmStageRn=_CfprOsControllerFsmStageRn_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,3),_CfprOsControllerFsmStageRn_Type())
cfprOsControllerFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageRn.setStatus(_A)
_CfprOsControllerFsmStageDescrData_Type=SnmpAdminString
_CfprOsControllerFsmStageDescrData_Object=MibTableColumn
cfprOsControllerFsmStageDescrData=_CfprOsControllerFsmStageDescrData_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,4),_CfprOsControllerFsmStageDescrData_Type())
cfprOsControllerFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageDescrData.setStatus(_A)
_CfprOsControllerFsmStageLastUpdateTime_Type=DateAndTime
_CfprOsControllerFsmStageLastUpdateTime_Object=MibTableColumn
cfprOsControllerFsmStageLastUpdateTime=_CfprOsControllerFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,5),_CfprOsControllerFsmStageLastUpdateTime_Type())
cfprOsControllerFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageLastUpdateTime.setStatus(_A)
_CfprOsControllerFsmStageName_Type=CfprOsControllerFsmStageName
_CfprOsControllerFsmStageName_Object=MibTableColumn
cfprOsControllerFsmStageName=_CfprOsControllerFsmStageName_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,6),_CfprOsControllerFsmStageName_Type())
cfprOsControllerFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageName.setStatus(_A)
_CfprOsControllerFsmStageOrder_Type=Gauge32
_CfprOsControllerFsmStageOrder_Object=MibTableColumn
cfprOsControllerFsmStageOrder=_CfprOsControllerFsmStageOrder_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,7),_CfprOsControllerFsmStageOrder_Type())
cfprOsControllerFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageOrder.setStatus(_A)
_CfprOsControllerFsmStageRetry_Type=Gauge32
_CfprOsControllerFsmStageRetry_Object=MibTableColumn
cfprOsControllerFsmStageRetry=_CfprOsControllerFsmStageRetry_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,8),_CfprOsControllerFsmStageRetry_Type())
cfprOsControllerFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageRetry.setStatus(_A)
_CfprOsControllerFsmStageStageStatus_Type=CfprFsmFsmStageStatus
_CfprOsControllerFsmStageStageStatus_Object=MibTableColumn
cfprOsControllerFsmStageStageStatus=_CfprOsControllerFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,826,1,59,4,1,9),_CfprOsControllerFsmStageStageStatus_Type())
cfprOsControllerFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmStageStageStatus.setStatus(_A)
_CfprOsControllerFsmTaskTable_Object=MibTable
cfprOsControllerFsmTaskTable=_CfprOsControllerFsmTaskTable_Object((1,3,6,1,4,1,9,9,826,1,59,5))
if mibBuilder.loadTexts:cfprOsControllerFsmTaskTable.setStatus(_A)
_CfprOsControllerFsmTaskEntry_Object=MibTableRow
cfprOsControllerFsmTaskEntry=_CfprOsControllerFsmTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,59,5,1))
cfprOsControllerFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprOsControllerFsmTaskEntry.setStatus(_A)
_CfprOsControllerFsmTaskInstanceId_Type=CfprManagedObjectId
_CfprOsControllerFsmTaskInstanceId_Object=MibTableColumn
cfprOsControllerFsmTaskInstanceId=_CfprOsControllerFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,1),_CfprOsControllerFsmTaskInstanceId_Type())
cfprOsControllerFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskInstanceId.setStatus(_A)
_CfprOsControllerFsmTaskDn_Type=CfprManagedObjectDn
_CfprOsControllerFsmTaskDn_Object=MibTableColumn
cfprOsControllerFsmTaskDn=_CfprOsControllerFsmTaskDn_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,2),_CfprOsControllerFsmTaskDn_Type())
cfprOsControllerFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskDn.setStatus(_A)
_CfprOsControllerFsmTaskRn_Type=SnmpAdminString
_CfprOsControllerFsmTaskRn_Object=MibTableColumn
cfprOsControllerFsmTaskRn=_CfprOsControllerFsmTaskRn_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,3),_CfprOsControllerFsmTaskRn_Type())
cfprOsControllerFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskRn.setStatus(_A)
_CfprOsControllerFsmTaskCompletion_Type=CfprFsmCompletion
_CfprOsControllerFsmTaskCompletion_Object=MibTableColumn
cfprOsControllerFsmTaskCompletion=_CfprOsControllerFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,4),_CfprOsControllerFsmTaskCompletion_Type())
cfprOsControllerFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskCompletion.setStatus(_A)
_CfprOsControllerFsmTaskFlags_Type=CfprOsControllerFsmTaskFlags
_CfprOsControllerFsmTaskFlags_Object=MibTableColumn
cfprOsControllerFsmTaskFlags=_CfprOsControllerFsmTaskFlags_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,5),_CfprOsControllerFsmTaskFlags_Type())
cfprOsControllerFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskFlags.setStatus(_A)
_CfprOsControllerFsmTaskItem_Type=CfprOsControllerFsmTaskItem
_CfprOsControllerFsmTaskItem_Object=MibTableColumn
cfprOsControllerFsmTaskItem=_CfprOsControllerFsmTaskItem_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,6),_CfprOsControllerFsmTaskItem_Type())
cfprOsControllerFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskItem.setStatus(_A)
_CfprOsControllerFsmTaskSeqId_Type=Gauge32
_CfprOsControllerFsmTaskSeqId_Object=MibTableColumn
cfprOsControllerFsmTaskSeqId=_CfprOsControllerFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,826,1,59,5,1,7),_CfprOsControllerFsmTaskSeqId_Type())
cfprOsControllerFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsControllerFsmTaskSeqId.setStatus(_A)
_CfprOsInstanceTable_Object=MibTable
cfprOsInstanceTable=_CfprOsInstanceTable_Object((1,3,6,1,4,1,9,9,826,1,59,6))
if mibBuilder.loadTexts:cfprOsInstanceTable.setStatus(_A)
_CfprOsInstanceEntry_Object=MibTableRow
cfprOsInstanceEntry=_CfprOsInstanceEntry_Object((1,3,6,1,4,1,9,9,826,1,59,6,1))
cfprOsInstanceEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprOsInstanceEntry.setStatus(_A)
_CfprOsInstanceInstanceId_Type=CfprManagedObjectId
_CfprOsInstanceInstanceId_Object=MibTableColumn
cfprOsInstanceInstanceId=_CfprOsInstanceInstanceId_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,1),_CfprOsInstanceInstanceId_Type())
cfprOsInstanceInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprOsInstanceInstanceId.setStatus(_A)
_CfprOsInstanceDn_Type=CfprManagedObjectDn
_CfprOsInstanceDn_Object=MibTableColumn
cfprOsInstanceDn=_CfprOsInstanceDn_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,2),_CfprOsInstanceDn_Type())
cfprOsInstanceDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceDn.setStatus(_A)
_CfprOsInstanceRn_Type=SnmpAdminString
_CfprOsInstanceRn_Object=MibTableColumn
cfprOsInstanceRn=_CfprOsInstanceRn_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,3),_CfprOsInstanceRn_Type())
cfprOsInstanceRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceRn.setStatus(_A)
_CfprOsInstanceHostname_Type=SnmpAdminString
_CfprOsInstanceHostname_Object=MibTableColumn
cfprOsInstanceHostname=_CfprOsInstanceHostname_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,4),_CfprOsInstanceHostname_Type())
cfprOsInstanceHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceHostname.setStatus(_A)
_CfprOsInstanceKernelName_Type=SnmpAdminString
_CfprOsInstanceKernelName_Object=MibTableColumn
cfprOsInstanceKernelName=_CfprOsInstanceKernelName_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,5),_CfprOsInstanceKernelName_Type())
cfprOsInstanceKernelName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceKernelName.setStatus(_A)
_CfprOsInstanceKernelRelease_Type=SnmpAdminString
_CfprOsInstanceKernelRelease_Object=MibTableColumn
cfprOsInstanceKernelRelease=_CfprOsInstanceKernelRelease_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,6),_CfprOsInstanceKernelRelease_Type())
cfprOsInstanceKernelRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceKernelRelease.setStatus(_A)
_CfprOsInstanceKernelVersion_Type=SnmpAdminString
_CfprOsInstanceKernelVersion_Object=MibTableColumn
cfprOsInstanceKernelVersion=_CfprOsInstanceKernelVersion_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,7),_CfprOsInstanceKernelVersion_Type())
cfprOsInstanceKernelVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceKernelVersion.setStatus(_A)
_CfprOsInstanceName_Type=SnmpAdminString
_CfprOsInstanceName_Object=MibTableColumn
cfprOsInstanceName=_CfprOsInstanceName_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,8),_CfprOsInstanceName_Type())
cfprOsInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceName.setStatus(_A)
_CfprOsInstanceType_Type=CfprOsOsType
_CfprOsInstanceType_Object=MibTableColumn
cfprOsInstanceType=_CfprOsInstanceType_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,9),_CfprOsInstanceType_Type())
cfprOsInstanceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceType.setStatus(_A)
_CfprOsInstanceUpgradeProgress_Type=Gauge32
_CfprOsInstanceUpgradeProgress_Object=MibTableColumn
cfprOsInstanceUpgradeProgress=_CfprOsInstanceUpgradeProgress_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,10),_CfprOsInstanceUpgradeProgress_Type())
cfprOsInstanceUpgradeProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceUpgradeProgress.setStatus(_A)
_CfprOsInstanceUpgradeReturnCode_Type=CfprOsUpgradeReturnCode
_CfprOsInstanceUpgradeReturnCode_Object=MibTableColumn
cfprOsInstanceUpgradeReturnCode=_CfprOsInstanceUpgradeReturnCode_Object((1,3,6,1,4,1,9,9,826,1,59,6,1,11),_CfprOsInstanceUpgradeReturnCode_Type())
cfprOsInstanceUpgradeReturnCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprOsInstanceUpgradeReturnCode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprOsObjects':cfprOsObjects,'cfprOsAgentTable':cfprOsAgentTable,'cfprOsAgentEntry':cfprOsAgentEntry,_E:cfprOsAgentInstanceId,'cfprOsAgentDn':cfprOsAgentDn,'cfprOsAgentRn':cfprOsAgentRn,'cfprOsAgentLastCmd':cfprOsAgentLastCmd,'cfprOsAgentLastEvt':cfprOsAgentLastEvt,'cfprOsAgentLastEvtTs':cfprOsAgentLastEvtTs,'cfprOsAgentPrevCmd':cfprOsAgentPrevCmd,'cfprOsAgentPrevEvt':cfprOsAgentPrevEvt,'cfprOsAgentType':cfprOsAgentType,'cfprOsAgentVendor':cfprOsAgentVendor,'cfprOsAgentVersion':cfprOsAgentVersion,'cfprOsControllerTable':cfprOsControllerTable,'cfprOsControllerEntry':cfprOsControllerEntry,_F:cfprOsControllerInstanceId,'cfprOsControllerDn':cfprOsControllerDn,'cfprOsControllerRn':cfprOsControllerRn,'cfprOsControllerBootMode':cfprOsControllerBootMode,'cfprOsControllerChassisId':cfprOsControllerChassisId,'cfprOsControllerDeployState':cfprOsControllerDeployState,'cfprOsControllerEnableDeployOS':cfprOsControllerEnableDeployOS,'cfprOsControllerFormatDisk':cfprOsControllerFormatDisk,'cfprOsControllerFsmDescr':cfprOsControllerFsmDescr,'cfprOsControllerFsmFlags':cfprOsControllerFsmFlags,'cfprOsControllerFsmPrev':cfprOsControllerFsmPrev,'cfprOsControllerFsmProgr':cfprOsControllerFsmProgr,'cfprOsControllerFsmRmtInvErrCode':cfprOsControllerFsmRmtInvErrCode,'cfprOsControllerFsmRmtInvErrDescr':cfprOsControllerFsmRmtInvErrDescr,'cfprOsControllerFsmRmtInvRslt':cfprOsControllerFsmRmtInvRslt,'cfprOsControllerFsmStageDescr':cfprOsControllerFsmStageDescr,'cfprOsControllerFsmStamp':cfprOsControllerFsmStamp,'cfprOsControllerFsmStatus':cfprOsControllerFsmStatus,'cfprOsControllerFsmTry':cfprOsControllerFsmTry,'cfprOsControllerHostname':cfprOsControllerHostname,'cfprOsControllerImageName':cfprOsControllerImageName,'cfprOsControllerImageSize':cfprOsControllerImageSize,'cfprOsControllerInitState':cfprOsControllerInitState,'cfprOsControllerMaxNumDeployFailureRecovery':cfprOsControllerMaxNumDeployFailureRecovery,'cfprOsControllerMaxNumberVersionMismatched':cfprOsControllerMaxNumberVersionMismatched,'cfprOsControllerModel':cfprOsControllerModel,'cfprOsControllerName':cfprOsControllerName,'cfprOsControllerNumDeployFailureRecovery':cfprOsControllerNumDeployFailureRecovery,'cfprOsControllerNumberVersionMismatched':cfprOsControllerNumberVersionMismatched,'cfprOsControllerPnDn':cfprOsControllerPnDn,'cfprOsControllerRevision':cfprOsControllerRevision,'cfprOsControllerRommonBuildDate':cfprOsControllerRommonBuildDate,'cfprOsControllerRommonVersion':cfprOsControllerRommonVersion,'cfprOsControllerSerial':cfprOsControllerSerial,'cfprOsControllerServiceStatus':cfprOsControllerServiceStatus,'cfprOsControllerSlotId':cfprOsControllerSlotId,'cfprOsControllerSsposMode':cfprOsControllerSsposMode,'cfprOsControllerSupportTftpboot':cfprOsControllerSupportTftpboot,'cfprOsControllerType':cfprOsControllerType,'cfprOsControllerUpgradeState':cfprOsControllerUpgradeState,'cfprOsControllerVendor':cfprOsControllerVendor,'cfprOsControllerVersion':cfprOsControllerVersion,'cfprOsControllerDmaSize':cfprOsControllerDmaSize,'cfprOsControllerHeapSize':cfprOsControllerHeapSize,'cfprOsControllerHugePageSize':cfprOsControllerHugePageSize,'cfprOsControllerInstallLicenseState':cfprOsControllerInstallLicenseState,'cfprOsControllerNumHugePages':cfprOsControllerNumHugePages,'cfprOsControllerPti':cfprOsControllerPti,'cfprOsControllerSecSmack':cfprOsControllerSecSmack,'cfprOsControllerTurboMode':cfprOsControllerTurboMode,'cfprOsControllerFsmTable':cfprOsControllerFsmTable,'cfprOsControllerFsmEntry':cfprOsControllerFsmEntry,_G:cfprOsControllerFsmInstanceId,'cfprOsControllerFsmDn':cfprOsControllerFsmDn,'cfprOsControllerFsmRn':cfprOsControllerFsmRn,'cfprOsControllerFsmCompletionTime':cfprOsControllerFsmCompletionTime,'cfprOsControllerFsmCurrentFsm':cfprOsControllerFsmCurrentFsm,'cfprOsControllerFsmDescrData':cfprOsControllerFsmDescrData,'cfprOsControllerFsmFsmStatus':cfprOsControllerFsmFsmStatus,'cfprOsControllerFsmProgress':cfprOsControllerFsmProgress,'cfprOsControllerFsmRmtErrCode':cfprOsControllerFsmRmtErrCode,'cfprOsControllerFsmRmtErrDescr':cfprOsControllerFsmRmtErrDescr,'cfprOsControllerFsmRmtRslt':cfprOsControllerFsmRmtRslt,'cfprOsControllerFsmStageTable':cfprOsControllerFsmStageTable,'cfprOsControllerFsmStageEntry':cfprOsControllerFsmStageEntry,_H:cfprOsControllerFsmStageInstanceId,'cfprOsControllerFsmStageDn':cfprOsControllerFsmStageDn,'cfprOsControllerFsmStageRn':cfprOsControllerFsmStageRn,'cfprOsControllerFsmStageDescrData':cfprOsControllerFsmStageDescrData,'cfprOsControllerFsmStageLastUpdateTime':cfprOsControllerFsmStageLastUpdateTime,'cfprOsControllerFsmStageName':cfprOsControllerFsmStageName,'cfprOsControllerFsmStageOrder':cfprOsControllerFsmStageOrder,'cfprOsControllerFsmStageRetry':cfprOsControllerFsmStageRetry,'cfprOsControllerFsmStageStageStatus':cfprOsControllerFsmStageStageStatus,'cfprOsControllerFsmTaskTable':cfprOsControllerFsmTaskTable,'cfprOsControllerFsmTaskEntry':cfprOsControllerFsmTaskEntry,_I:cfprOsControllerFsmTaskInstanceId,'cfprOsControllerFsmTaskDn':cfprOsControllerFsmTaskDn,'cfprOsControllerFsmTaskRn':cfprOsControllerFsmTaskRn,'cfprOsControllerFsmTaskCompletion':cfprOsControllerFsmTaskCompletion,'cfprOsControllerFsmTaskFlags':cfprOsControllerFsmTaskFlags,'cfprOsControllerFsmTaskItem':cfprOsControllerFsmTaskItem,'cfprOsControllerFsmTaskSeqId':cfprOsControllerFsmTaskSeqId,'cfprOsInstanceTable':cfprOsInstanceTable,'cfprOsInstanceEntry':cfprOsInstanceEntry,_J:cfprOsInstanceInstanceId,'cfprOsInstanceDn':cfprOsInstanceDn,'cfprOsInstanceRn':cfprOsInstanceRn,'cfprOsInstanceHostname':cfprOsInstanceHostname,'cfprOsInstanceKernelName':cfprOsInstanceKernelName,'cfprOsInstanceKernelRelease':cfprOsInstanceKernelRelease,'cfprOsInstanceKernelVersion':cfprOsInstanceKernelVersion,'cfprOsInstanceName':cfprOsInstanceName,'cfprOsInstanceType':cfprOsInstanceType,'cfprOsInstanceUpgradeProgress':cfprOsInstanceUpgradeProgress,'cfprOsInstanceUpgradeReturnCode':cfprOsInstanceUpgradeReturnCode})