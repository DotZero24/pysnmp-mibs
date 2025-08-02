_V='cucsCapabilityUpdaterFsmStageInstanceId'
_U='cucsCapabilityUpdaterFsmInstanceId'
_T='cucsCapabilitySystemLimitsInstanceId'
_S='cucsCapabilityStorageLimitsInstanceId'
_R='cucsCapabilityNetworkLimitsInstanceId'
_Q='cucsCapabilityMgmtExtensionFsmStageInstanceId'
_P='cucsCapabilityMgmtExtensionFsmInstanceId'
_O='cucsCapabilityFeatureLimitsInstanceId'
_N='cucsCapabilityCatalogueFsmStageInstanceId'
_M='cucsCapabilityCatalogueFsmInstanceId'
_L='cucsCapabilityUpdaterFsmTaskInstanceId'
_K='cucsCapabilityUpdaterInstanceId'
_J='cucsCapabilityUpdateInstanceId'
_I='cucsCapabilityMgmtExtensionFsmTaskInstanceId'
_H='cucsCapabilityMgmtExtensionInstanceId'
_G='cucsCapabilityEpInstanceId'
_F='cucsCapabilityCatalogueFsmTaskInstanceId'
_E='cucsCapabilityCatalogueInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-CAPABILITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsCapabilityAdminState,CucsCapabilityCatalogueFsmCurrentFsm,CucsCapabilityCatalogueFsmStageName,CucsCapabilityCatalogueFsmTaskItem,CucsCapabilityFeatureStatus,CucsCapabilityMgmtExtensionFsmCurrentFsm,CucsCapabilityMgmtExtensionFsmStageName,CucsCapabilityMgmtExtensionFsmTaskItem,CucsCapabilityOperStatus,CucsCapabilityPlatform,CucsCapabilityUpdaterFsmCurrentFsm,CucsCapabilityUpdaterFsmStageName,CucsCapabilityUpdaterFsmTaskItem,CucsConditionRemoteInvRslt,CucsFirmwareTransport,CucsFsmCompletion,CucsFsmFlags,CucsFsmFsmStageStatus=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsCapabilityAdminState','CucsCapabilityCatalogueFsmCurrentFsm','CucsCapabilityCatalogueFsmStageName','CucsCapabilityCatalogueFsmTaskItem','CucsCapabilityFeatureStatus','CucsCapabilityMgmtExtensionFsmCurrentFsm','CucsCapabilityMgmtExtensionFsmStageName','CucsCapabilityMgmtExtensionFsmTaskItem','CucsCapabilityOperStatus','CucsCapabilityPlatform','CucsCapabilityUpdaterFsmCurrentFsm','CucsCapabilityUpdaterFsmStageName','CucsCapabilityUpdaterFsmTaskItem','CucsConditionRemoteInvRslt','CucsFirmwareTransport','CucsFsmCompletion','CucsFsmFlags','CucsFsmFsmStageStatus')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsCapabilityObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,7))
_CucsCapabilityCatalogueTable_Object=MibTable
cucsCapabilityCatalogueTable=_CucsCapabilityCatalogueTable_Object((1,3,6,1,4,1,9,9,719,1,7,1))
if mibBuilder.loadTexts:cucsCapabilityCatalogueTable.setStatus(_A)
_CucsCapabilityCatalogueEntry_Object=MibTableRow
cucsCapabilityCatalogueEntry=_CucsCapabilityCatalogueEntry_Object((1,3,6,1,4,1,9,9,719,1,7,1,1))
cucsCapabilityCatalogueEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsCapabilityCatalogueEntry.setStatus(_A)
_CucsCapabilityCatalogueInstanceId_Type=CucsManagedObjectId
_CucsCapabilityCatalogueInstanceId_Object=MibTableColumn
cucsCapabilityCatalogueInstanceId=_CucsCapabilityCatalogueInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,1),_CucsCapabilityCatalogueInstanceId_Type())
cucsCapabilityCatalogueInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityCatalogueInstanceId.setStatus(_A)
_CucsCapabilityCatalogueDn_Type=CucsManagedObjectDn
_CucsCapabilityCatalogueDn_Object=MibTableColumn
cucsCapabilityCatalogueDn=_CucsCapabilityCatalogueDn_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,2),_CucsCapabilityCatalogueDn_Type())
cucsCapabilityCatalogueDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueDn.setStatus(_A)
_CucsCapabilityCatalogueRn_Type=SnmpAdminString
_CucsCapabilityCatalogueRn_Object=MibTableColumn
cucsCapabilityCatalogueRn=_CucsCapabilityCatalogueRn_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,3),_CucsCapabilityCatalogueRn_Type())
cucsCapabilityCatalogueRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueRn.setStatus(_A)
_CucsCapabilityCatalogueFsmDescr_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmDescr_Object=MibTableColumn
cucsCapabilityCatalogueFsmDescr=_CucsCapabilityCatalogueFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,4),_CucsCapabilityCatalogueFsmDescr_Type())
cucsCapabilityCatalogueFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmDescr.setStatus(_A)
_CucsCapabilityCatalogueFsmPrev_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmPrev_Object=MibTableColumn
cucsCapabilityCatalogueFsmPrev=_CucsCapabilityCatalogueFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,5),_CucsCapabilityCatalogueFsmPrev_Type())
cucsCapabilityCatalogueFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmPrev.setStatus(_A)
_CucsCapabilityCatalogueFsmProgr_Type=Gauge32
_CucsCapabilityCatalogueFsmProgr_Object=MibTableColumn
cucsCapabilityCatalogueFsmProgr=_CucsCapabilityCatalogueFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,6),_CucsCapabilityCatalogueFsmProgr_Type())
cucsCapabilityCatalogueFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmProgr.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtInvErrCode_Type=Gauge32
_CucsCapabilityCatalogueFsmRmtInvErrCode_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtInvErrCode=_CucsCapabilityCatalogueFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,7),_CucsCapabilityCatalogueFsmRmtInvErrCode_Type())
cucsCapabilityCatalogueFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtInvErrCode.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmRmtInvErrDescr_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtInvErrDescr=_CucsCapabilityCatalogueFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,8),_CucsCapabilityCatalogueFsmRmtInvErrDescr_Type())
cucsCapabilityCatalogueFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtInvErrDescr.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityCatalogueFsmRmtInvRslt_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtInvRslt=_CucsCapabilityCatalogueFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,9),_CucsCapabilityCatalogueFsmRmtInvRslt_Type())
cucsCapabilityCatalogueFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtInvRslt.setStatus(_A)
_CucsCapabilityCatalogueFsmStageDescr_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmStageDescr_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageDescr=_CucsCapabilityCatalogueFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,10),_CucsCapabilityCatalogueFsmStageDescr_Type())
cucsCapabilityCatalogueFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageDescr.setStatus(_A)
_CucsCapabilityCatalogueFsmStamp_Type=DateAndTime
_CucsCapabilityCatalogueFsmStamp_Object=MibTableColumn
cucsCapabilityCatalogueFsmStamp=_CucsCapabilityCatalogueFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,11),_CucsCapabilityCatalogueFsmStamp_Type())
cucsCapabilityCatalogueFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStamp.setStatus(_A)
_CucsCapabilityCatalogueFsmStatus_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmStatus_Object=MibTableColumn
cucsCapabilityCatalogueFsmStatus=_CucsCapabilityCatalogueFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,12),_CucsCapabilityCatalogueFsmStatus_Type())
cucsCapabilityCatalogueFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStatus.setStatus(_A)
_CucsCapabilityCatalogueFsmTry_Type=Gauge32
_CucsCapabilityCatalogueFsmTry_Object=MibTableColumn
cucsCapabilityCatalogueFsmTry=_CucsCapabilityCatalogueFsmTry_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,13),_CucsCapabilityCatalogueFsmTry_Type())
cucsCapabilityCatalogueFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTry.setStatus(_A)
_CucsCapabilityCatalogueVersion_Type=SnmpAdminString
_CucsCapabilityCatalogueVersion_Object=MibTableColumn
cucsCapabilityCatalogueVersion=_CucsCapabilityCatalogueVersion_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,14),_CucsCapabilityCatalogueVersion_Type())
cucsCapabilityCatalogueVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueVersion.setStatus(_A)
_CucsCapabilityCatalogueFileParseFailures_Type=Gauge32
_CucsCapabilityCatalogueFileParseFailures_Object=MibTableColumn
cucsCapabilityCatalogueFileParseFailures=_CucsCapabilityCatalogueFileParseFailures_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,15),_CucsCapabilityCatalogueFileParseFailures_Type())
cucsCapabilityCatalogueFileParseFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFileParseFailures.setStatus(_A)
_CucsCapabilityCatalogueFilesParsed_Type=Gauge32
_CucsCapabilityCatalogueFilesParsed_Object=MibTableColumn
cucsCapabilityCatalogueFilesParsed=_CucsCapabilityCatalogueFilesParsed_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,16),_CucsCapabilityCatalogueFilesParsed_Type())
cucsCapabilityCatalogueFilesParsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFilesParsed.setStatus(_A)
_CucsCapabilityCatalogueLoadErrors_Type=Gauge32
_CucsCapabilityCatalogueLoadErrors_Object=MibTableColumn
cucsCapabilityCatalogueLoadErrors=_CucsCapabilityCatalogueLoadErrors_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,17),_CucsCapabilityCatalogueLoadErrors_Type())
cucsCapabilityCatalogueLoadErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueLoadErrors.setStatus(_A)
_CucsCapabilityCatalogueLoadWarnings_Type=Gauge32
_CucsCapabilityCatalogueLoadWarnings_Object=MibTableColumn
cucsCapabilityCatalogueLoadWarnings=_CucsCapabilityCatalogueLoadWarnings_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,18),_CucsCapabilityCatalogueLoadWarnings_Type())
cucsCapabilityCatalogueLoadWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueLoadWarnings.setStatus(_A)
_CucsCapabilityCatalogueProviderLoadFailures_Type=Gauge32
_CucsCapabilityCatalogueProviderLoadFailures_Object=MibTableColumn
cucsCapabilityCatalogueProviderLoadFailures=_CucsCapabilityCatalogueProviderLoadFailures_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,19),_CucsCapabilityCatalogueProviderLoadFailures_Type())
cucsCapabilityCatalogueProviderLoadFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueProviderLoadFailures.setStatus(_A)
_CucsCapabilityCatalogueProvidersLoaded_Type=Gauge32
_CucsCapabilityCatalogueProvidersLoaded_Object=MibTableColumn
cucsCapabilityCatalogueProvidersLoaded=_CucsCapabilityCatalogueProvidersLoaded_Object((1,3,6,1,4,1,9,9,719,1,7,1,1,20),_CucsCapabilityCatalogueProvidersLoaded_Type())
cucsCapabilityCatalogueProvidersLoaded.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueProvidersLoaded.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskTable_Object=MibTable
cucsCapabilityCatalogueFsmTaskTable=_CucsCapabilityCatalogueFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,7,2))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskTable.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskEntry_Object=MibTableRow
cucsCapabilityCatalogueFsmTaskEntry=_CucsCapabilityCatalogueFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,7,2,1))
cucsCapabilityCatalogueFsmTaskEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskEntry.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsCapabilityCatalogueFsmTaskInstanceId_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskInstanceId=_CucsCapabilityCatalogueFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,1),_CucsCapabilityCatalogueFsmTaskInstanceId_Type())
cucsCapabilityCatalogueFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskInstanceId.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskDn_Type=CucsManagedObjectDn
_CucsCapabilityCatalogueFsmTaskDn_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskDn=_CucsCapabilityCatalogueFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,2),_CucsCapabilityCatalogueFsmTaskDn_Type())
cucsCapabilityCatalogueFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskDn.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskRn_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmTaskRn_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskRn=_CucsCapabilityCatalogueFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,3),_CucsCapabilityCatalogueFsmTaskRn_Type())
cucsCapabilityCatalogueFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskRn.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskCompletion_Type=CucsFsmCompletion
_CucsCapabilityCatalogueFsmTaskCompletion_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskCompletion=_CucsCapabilityCatalogueFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,4),_CucsCapabilityCatalogueFsmTaskCompletion_Type())
cucsCapabilityCatalogueFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskCompletion.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskFlags_Type=CucsFsmFlags
_CucsCapabilityCatalogueFsmTaskFlags_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskFlags=_CucsCapabilityCatalogueFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,5),_CucsCapabilityCatalogueFsmTaskFlags_Type())
cucsCapabilityCatalogueFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskFlags.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskItem_Type=CucsCapabilityCatalogueFsmTaskItem
_CucsCapabilityCatalogueFsmTaskItem_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskItem=_CucsCapabilityCatalogueFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,6),_CucsCapabilityCatalogueFsmTaskItem_Type())
cucsCapabilityCatalogueFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskItem.setStatus(_A)
_CucsCapabilityCatalogueFsmTaskSeqId_Type=Gauge32
_CucsCapabilityCatalogueFsmTaskSeqId_Object=MibTableColumn
cucsCapabilityCatalogueFsmTaskSeqId=_CucsCapabilityCatalogueFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,7,2,1,7),_CucsCapabilityCatalogueFsmTaskSeqId_Type())
cucsCapabilityCatalogueFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTaskSeqId.setStatus(_A)
_CucsCapabilityEpTable_Object=MibTable
cucsCapabilityEpTable=_CucsCapabilityEpTable_Object((1,3,6,1,4,1,9,9,719,1,7,3))
if mibBuilder.loadTexts:cucsCapabilityEpTable.setStatus(_A)
_CucsCapabilityEpEntry_Object=MibTableRow
cucsCapabilityEpEntry=_CucsCapabilityEpEntry_Object((1,3,6,1,4,1,9,9,719,1,7,3,1))
cucsCapabilityEpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsCapabilityEpEntry.setStatus(_A)
_CucsCapabilityEpInstanceId_Type=CucsManagedObjectId
_CucsCapabilityEpInstanceId_Object=MibTableColumn
cucsCapabilityEpInstanceId=_CucsCapabilityEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,3,1,1),_CucsCapabilityEpInstanceId_Type())
cucsCapabilityEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityEpInstanceId.setStatus(_A)
_CucsCapabilityEpDn_Type=CucsManagedObjectDn
_CucsCapabilityEpDn_Object=MibTableColumn
cucsCapabilityEpDn=_CucsCapabilityEpDn_Object((1,3,6,1,4,1,9,9,719,1,7,3,1,2),_CucsCapabilityEpDn_Type())
cucsCapabilityEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityEpDn.setStatus(_A)
_CucsCapabilityEpRn_Type=SnmpAdminString
_CucsCapabilityEpRn_Object=MibTableColumn
cucsCapabilityEpRn=_CucsCapabilityEpRn_Object((1,3,6,1,4,1,9,9,719,1,7,3,1,3),_CucsCapabilityEpRn_Type())
cucsCapabilityEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityEpRn.setStatus(_A)
_CucsCapabilityMgmtExtensionTable_Object=MibTable
cucsCapabilityMgmtExtensionTable=_CucsCapabilityMgmtExtensionTable_Object((1,3,6,1,4,1,9,9,719,1,7,4))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionTable.setStatus(_A)
_CucsCapabilityMgmtExtensionEntry_Object=MibTableRow
cucsCapabilityMgmtExtensionEntry=_CucsCapabilityMgmtExtensionEntry_Object((1,3,6,1,4,1,9,9,719,1,7,4,1))
cucsCapabilityMgmtExtensionEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionEntry.setStatus(_A)
_CucsCapabilityMgmtExtensionInstanceId_Type=CucsManagedObjectId
_CucsCapabilityMgmtExtensionInstanceId_Object=MibTableColumn
cucsCapabilityMgmtExtensionInstanceId=_CucsCapabilityMgmtExtensionInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,1),_CucsCapabilityMgmtExtensionInstanceId_Type())
cucsCapabilityMgmtExtensionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionInstanceId.setStatus(_A)
_CucsCapabilityMgmtExtensionDn_Type=CucsManagedObjectDn
_CucsCapabilityMgmtExtensionDn_Object=MibTableColumn
cucsCapabilityMgmtExtensionDn=_CucsCapabilityMgmtExtensionDn_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,2),_CucsCapabilityMgmtExtensionDn_Type())
cucsCapabilityMgmtExtensionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionDn.setStatus(_A)
_CucsCapabilityMgmtExtensionRn_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionRn_Object=MibTableColumn
cucsCapabilityMgmtExtensionRn=_CucsCapabilityMgmtExtensionRn_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,3),_CucsCapabilityMgmtExtensionRn_Type())
cucsCapabilityMgmtExtensionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionRn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmDescr_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmDescr_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmDescr=_CucsCapabilityMgmtExtensionFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,4),_CucsCapabilityMgmtExtensionFsmDescr_Type())
cucsCapabilityMgmtExtensionFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmDescr.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmPrev_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmPrev_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmPrev=_CucsCapabilityMgmtExtensionFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,5),_CucsCapabilityMgmtExtensionFsmPrev_Type())
cucsCapabilityMgmtExtensionFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmPrev.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmProgr_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmProgr_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmProgr=_CucsCapabilityMgmtExtensionFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,6),_CucsCapabilityMgmtExtensionFsmProgr_Type())
cucsCapabilityMgmtExtensionFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmProgr.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvErrCode=_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,7),_CucsCapabilityMgmtExtensionFsmRmtInvErrCode_Type())
cucsCapabilityMgmtExtensionFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtInvErrCode.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvErrDescr=_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,8),_CucsCapabilityMgmtExtensionFsmRmtInvErrDescr_Type())
cucsCapabilityMgmtExtensionFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtInvErrDescr.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtInvRslt=_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,9),_CucsCapabilityMgmtExtensionFsmRmtInvRslt_Type())
cucsCapabilityMgmtExtensionFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtInvRslt.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageDescr_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageDescr_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDescr=_CucsCapabilityMgmtExtensionFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,10),_CucsCapabilityMgmtExtensionFsmStageDescr_Type())
cucsCapabilityMgmtExtensionFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageDescr.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStamp_Type=DateAndTime
_CucsCapabilityMgmtExtensionFsmStamp_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStamp=_CucsCapabilityMgmtExtensionFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,11),_CucsCapabilityMgmtExtensionFsmStamp_Type())
cucsCapabilityMgmtExtensionFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStamp.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStatus_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStatus_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStatus=_CucsCapabilityMgmtExtensionFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,12),_CucsCapabilityMgmtExtensionFsmStatus_Type())
cucsCapabilityMgmtExtensionFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStatus.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTry_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmTry_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTry=_CucsCapabilityMgmtExtensionFsmTry_Object((1,3,6,1,4,1,9,9,719,1,7,4,1,13),_CucsCapabilityMgmtExtensionFsmTry_Type())
cucsCapabilityMgmtExtensionFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTry.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskTable_Object=MibTable
cucsCapabilityMgmtExtensionFsmTaskTable=_CucsCapabilityMgmtExtensionFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,7,5))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskTable.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskEntry_Object=MibTableRow
cucsCapabilityMgmtExtensionFsmTaskEntry=_CucsCapabilityMgmtExtensionFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,7,5,1))
cucsCapabilityMgmtExtensionFsmTaskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskEntry.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskInstanceId=_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,1),_CucsCapabilityMgmtExtensionFsmTaskInstanceId_Type())
cucsCapabilityMgmtExtensionFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskInstanceId.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskDn_Type=CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmTaskDn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskDn=_CucsCapabilityMgmtExtensionFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,2),_CucsCapabilityMgmtExtensionFsmTaskDn_Type())
cucsCapabilityMgmtExtensionFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskDn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskRn_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmTaskRn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskRn=_CucsCapabilityMgmtExtensionFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,3),_CucsCapabilityMgmtExtensionFsmTaskRn_Type())
cucsCapabilityMgmtExtensionFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskRn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskCompletion_Type=CucsFsmCompletion
_CucsCapabilityMgmtExtensionFsmTaskCompletion_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskCompletion=_CucsCapabilityMgmtExtensionFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,4),_CucsCapabilityMgmtExtensionFsmTaskCompletion_Type())
cucsCapabilityMgmtExtensionFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskCompletion.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskFlags_Type=CucsFsmFlags
_CucsCapabilityMgmtExtensionFsmTaskFlags_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskFlags=_CucsCapabilityMgmtExtensionFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,5),_CucsCapabilityMgmtExtensionFsmTaskFlags_Type())
cucsCapabilityMgmtExtensionFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskFlags.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskItem_Type=CucsCapabilityMgmtExtensionFsmTaskItem
_CucsCapabilityMgmtExtensionFsmTaskItem_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskItem=_CucsCapabilityMgmtExtensionFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,6),_CucsCapabilityMgmtExtensionFsmTaskItem_Type())
cucsCapabilityMgmtExtensionFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskItem.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTaskSeqId_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmTaskSeqId_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmTaskSeqId=_CucsCapabilityMgmtExtensionFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,7,5,1,7),_CucsCapabilityMgmtExtensionFsmTaskSeqId_Type())
cucsCapabilityMgmtExtensionFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTaskSeqId.setStatus(_A)
_CucsCapabilityUpdateTable_Object=MibTable
cucsCapabilityUpdateTable=_CucsCapabilityUpdateTable_Object((1,3,6,1,4,1,9,9,719,1,7,6))
if mibBuilder.loadTexts:cucsCapabilityUpdateTable.setStatus(_A)
_CucsCapabilityUpdateEntry_Object=MibTableRow
cucsCapabilityUpdateEntry=_CucsCapabilityUpdateEntry_Object((1,3,6,1,4,1,9,9,719,1,7,6,1))
cucsCapabilityUpdateEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsCapabilityUpdateEntry.setStatus(_A)
_CucsCapabilityUpdateInstanceId_Type=CucsManagedObjectId
_CucsCapabilityUpdateInstanceId_Object=MibTableColumn
cucsCapabilityUpdateInstanceId=_CucsCapabilityUpdateInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,1),_CucsCapabilityUpdateInstanceId_Type())
cucsCapabilityUpdateInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityUpdateInstanceId.setStatus(_A)
_CucsCapabilityUpdateDn_Type=CucsManagedObjectDn
_CucsCapabilityUpdateDn_Object=MibTableColumn
cucsCapabilityUpdateDn=_CucsCapabilityUpdateDn_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,2),_CucsCapabilityUpdateDn_Type())
cucsCapabilityUpdateDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdateDn.setStatus(_A)
_CucsCapabilityUpdateRn_Type=SnmpAdminString
_CucsCapabilityUpdateRn_Object=MibTableColumn
cucsCapabilityUpdateRn=_CucsCapabilityUpdateRn_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,3),_CucsCapabilityUpdateRn_Type())
cucsCapabilityUpdateRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdateRn.setStatus(_A)
_CucsCapabilityUpdateImageName_Type=SnmpAdminString
_CucsCapabilityUpdateImageName_Object=MibTableColumn
cucsCapabilityUpdateImageName=_CucsCapabilityUpdateImageName_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,4),_CucsCapabilityUpdateImageName_Type())
cucsCapabilityUpdateImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdateImageName.setStatus(_A)
_CucsCapabilityUpdateUpdateTs_Type=DateAndTime
_CucsCapabilityUpdateUpdateTs_Object=MibTableColumn
cucsCapabilityUpdateUpdateTs=_CucsCapabilityUpdateUpdateTs_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,5),_CucsCapabilityUpdateUpdateTs_Type())
cucsCapabilityUpdateUpdateTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdateUpdateTs.setStatus(_A)
_CucsCapabilityUpdateVersion_Type=SnmpAdminString
_CucsCapabilityUpdateVersion_Object=MibTableColumn
cucsCapabilityUpdateVersion=_CucsCapabilityUpdateVersion_Object((1,3,6,1,4,1,9,9,719,1,7,6,1,6),_CucsCapabilityUpdateVersion_Type())
cucsCapabilityUpdateVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdateVersion.setStatus(_A)
_CucsCapabilityUpdaterTable_Object=MibTable
cucsCapabilityUpdaterTable=_CucsCapabilityUpdaterTable_Object((1,3,6,1,4,1,9,9,719,1,7,7))
if mibBuilder.loadTexts:cucsCapabilityUpdaterTable.setStatus(_A)
_CucsCapabilityUpdaterEntry_Object=MibTableRow
cucsCapabilityUpdaterEntry=_CucsCapabilityUpdaterEntry_Object((1,3,6,1,4,1,9,9,719,1,7,7,1))
cucsCapabilityUpdaterEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsCapabilityUpdaterEntry.setStatus(_A)
_CucsCapabilityUpdaterInstanceId_Type=CucsManagedObjectId
_CucsCapabilityUpdaterInstanceId_Object=MibTableColumn
cucsCapabilityUpdaterInstanceId=_CucsCapabilityUpdaterInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,1),_CucsCapabilityUpdaterInstanceId_Type())
cucsCapabilityUpdaterInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityUpdaterInstanceId.setStatus(_A)
_CucsCapabilityUpdaterDn_Type=CucsManagedObjectDn
_CucsCapabilityUpdaterDn_Object=MibTableColumn
cucsCapabilityUpdaterDn=_CucsCapabilityUpdaterDn_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,2),_CucsCapabilityUpdaterDn_Type())
cucsCapabilityUpdaterDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterDn.setStatus(_A)
_CucsCapabilityUpdaterRn_Type=SnmpAdminString
_CucsCapabilityUpdaterRn_Object=MibTableColumn
cucsCapabilityUpdaterRn=_CucsCapabilityUpdaterRn_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,3),_CucsCapabilityUpdaterRn_Type())
cucsCapabilityUpdaterRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterRn.setStatus(_A)
_CucsCapabilityUpdaterAdminState_Type=CucsCapabilityAdminState
_CucsCapabilityUpdaterAdminState_Object=MibTableColumn
cucsCapabilityUpdaterAdminState=_CucsCapabilityUpdaterAdminState_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,4),_CucsCapabilityUpdaterAdminState_Type())
cucsCapabilityUpdaterAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterAdminState.setStatus(_A)
_CucsCapabilityUpdaterFileName_Type=SnmpAdminString
_CucsCapabilityUpdaterFileName_Object=MibTableColumn
cucsCapabilityUpdaterFileName=_CucsCapabilityUpdaterFileName_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,5),_CucsCapabilityUpdaterFileName_Type())
cucsCapabilityUpdaterFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFileName.setStatus(_A)
_CucsCapabilityUpdaterFsmDescr_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmDescr_Object=MibTableColumn
cucsCapabilityUpdaterFsmDescr=_CucsCapabilityUpdaterFsmDescr_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,6),_CucsCapabilityUpdaterFsmDescr_Type())
cucsCapabilityUpdaterFsmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmDescr.setStatus(_A)
_CucsCapabilityUpdaterFsmPrev_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmPrev_Object=MibTableColumn
cucsCapabilityUpdaterFsmPrev=_CucsCapabilityUpdaterFsmPrev_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,7),_CucsCapabilityUpdaterFsmPrev_Type())
cucsCapabilityUpdaterFsmPrev.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmPrev.setStatus(_A)
_CucsCapabilityUpdaterFsmProgr_Type=Gauge32
_CucsCapabilityUpdaterFsmProgr_Object=MibTableColumn
cucsCapabilityUpdaterFsmProgr=_CucsCapabilityUpdaterFsmProgr_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,8),_CucsCapabilityUpdaterFsmProgr_Type())
cucsCapabilityUpdaterFsmProgr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmProgr.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtInvErrCode_Type=Gauge32
_CucsCapabilityUpdaterFsmRmtInvErrCode_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtInvErrCode=_CucsCapabilityUpdaterFsmRmtInvErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,9),_CucsCapabilityUpdaterFsmRmtInvErrCode_Type())
cucsCapabilityUpdaterFsmRmtInvErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtInvErrCode.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtInvErrDescr_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmRmtInvErrDescr_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtInvErrDescr=_CucsCapabilityUpdaterFsmRmtInvErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,10),_CucsCapabilityUpdaterFsmRmtInvErrDescr_Type())
cucsCapabilityUpdaterFsmRmtInvErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtInvErrDescr.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtInvRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityUpdaterFsmRmtInvRslt_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtInvRslt=_CucsCapabilityUpdaterFsmRmtInvRslt_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,11),_CucsCapabilityUpdaterFsmRmtInvRslt_Type())
cucsCapabilityUpdaterFsmRmtInvRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtInvRslt.setStatus(_A)
_CucsCapabilityUpdaterFsmStageDescr_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmStageDescr_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageDescr=_CucsCapabilityUpdaterFsmStageDescr_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,12),_CucsCapabilityUpdaterFsmStageDescr_Type())
cucsCapabilityUpdaterFsmStageDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageDescr.setStatus(_A)
_CucsCapabilityUpdaterFsmStamp_Type=DateAndTime
_CucsCapabilityUpdaterFsmStamp_Object=MibTableColumn
cucsCapabilityUpdaterFsmStamp=_CucsCapabilityUpdaterFsmStamp_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,13),_CucsCapabilityUpdaterFsmStamp_Type())
cucsCapabilityUpdaterFsmStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStamp.setStatus(_A)
_CucsCapabilityUpdaterFsmStatus_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmStatus_Object=MibTableColumn
cucsCapabilityUpdaterFsmStatus=_CucsCapabilityUpdaterFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,14),_CucsCapabilityUpdaterFsmStatus_Type())
cucsCapabilityUpdaterFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStatus.setStatus(_A)
_CucsCapabilityUpdaterFsmTry_Type=Gauge32
_CucsCapabilityUpdaterFsmTry_Object=MibTableColumn
cucsCapabilityUpdaterFsmTry=_CucsCapabilityUpdaterFsmTry_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,15),_CucsCapabilityUpdaterFsmTry_Type())
cucsCapabilityUpdaterFsmTry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTry.setStatus(_A)
_CucsCapabilityUpdaterImageName_Type=SnmpAdminString
_CucsCapabilityUpdaterImageName_Object=MibTableColumn
cucsCapabilityUpdaterImageName=_CucsCapabilityUpdaterImageName_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,16),_CucsCapabilityUpdaterImageName_Type())
cucsCapabilityUpdaterImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterImageName.setStatus(_A)
_CucsCapabilityUpdaterOperState_Type=CucsCapabilityOperStatus
_CucsCapabilityUpdaterOperState_Object=MibTableColumn
cucsCapabilityUpdaterOperState=_CucsCapabilityUpdaterOperState_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,17),_CucsCapabilityUpdaterOperState_Type())
cucsCapabilityUpdaterOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterOperState.setStatus(_A)
_CucsCapabilityUpdaterProtocol_Type=CucsFirmwareTransport
_CucsCapabilityUpdaterProtocol_Object=MibTableColumn
cucsCapabilityUpdaterProtocol=_CucsCapabilityUpdaterProtocol_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,18),_CucsCapabilityUpdaterProtocol_Type())
cucsCapabilityUpdaterProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterProtocol.setStatus(_A)
_CucsCapabilityUpdaterPwd_Type=SnmpAdminString
_CucsCapabilityUpdaterPwd_Object=MibTableColumn
cucsCapabilityUpdaterPwd=_CucsCapabilityUpdaterPwd_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,19),_CucsCapabilityUpdaterPwd_Type())
cucsCapabilityUpdaterPwd.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterPwd.setStatus(_A)
_CucsCapabilityUpdaterRemotePath_Type=SnmpAdminString
_CucsCapabilityUpdaterRemotePath_Object=MibTableColumn
cucsCapabilityUpdaterRemotePath=_CucsCapabilityUpdaterRemotePath_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,20),_CucsCapabilityUpdaterRemotePath_Type())
cucsCapabilityUpdaterRemotePath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterRemotePath.setStatus(_A)
_CucsCapabilityUpdaterServer_Type=SnmpAdminString
_CucsCapabilityUpdaterServer_Object=MibTableColumn
cucsCapabilityUpdaterServer=_CucsCapabilityUpdaterServer_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,21),_CucsCapabilityUpdaterServer_Type())
cucsCapabilityUpdaterServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterServer.setStatus(_A)
_CucsCapabilityUpdaterUser_Type=SnmpAdminString
_CucsCapabilityUpdaterUser_Object=MibTableColumn
cucsCapabilityUpdaterUser=_CucsCapabilityUpdaterUser_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,22),_CucsCapabilityUpdaterUser_Type())
cucsCapabilityUpdaterUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterUser.setStatus(_A)
_CucsCapabilityUpdaterVersion_Type=SnmpAdminString
_CucsCapabilityUpdaterVersion_Object=MibTableColumn
cucsCapabilityUpdaterVersion=_CucsCapabilityUpdaterVersion_Object((1,3,6,1,4,1,9,9,719,1,7,7,1,23),_CucsCapabilityUpdaterVersion_Type())
cucsCapabilityUpdaterVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterVersion.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskTable_Object=MibTable
cucsCapabilityUpdaterFsmTaskTable=_CucsCapabilityUpdaterFsmTaskTable_Object((1,3,6,1,4,1,9,9,719,1,7,8))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskTable.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskEntry_Object=MibTableRow
cucsCapabilityUpdaterFsmTaskEntry=_CucsCapabilityUpdaterFsmTaskEntry_Object((1,3,6,1,4,1,9,9,719,1,7,8,1))
cucsCapabilityUpdaterFsmTaskEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskEntry.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskInstanceId_Type=CucsManagedObjectId
_CucsCapabilityUpdaterFsmTaskInstanceId_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskInstanceId=_CucsCapabilityUpdaterFsmTaskInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,1),_CucsCapabilityUpdaterFsmTaskInstanceId_Type())
cucsCapabilityUpdaterFsmTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskInstanceId.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskDn_Type=CucsManagedObjectDn
_CucsCapabilityUpdaterFsmTaskDn_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskDn=_CucsCapabilityUpdaterFsmTaskDn_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,2),_CucsCapabilityUpdaterFsmTaskDn_Type())
cucsCapabilityUpdaterFsmTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskDn.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskRn_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmTaskRn_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskRn=_CucsCapabilityUpdaterFsmTaskRn_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,3),_CucsCapabilityUpdaterFsmTaskRn_Type())
cucsCapabilityUpdaterFsmTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskRn.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskCompletion_Type=CucsFsmCompletion
_CucsCapabilityUpdaterFsmTaskCompletion_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskCompletion=_CucsCapabilityUpdaterFsmTaskCompletion_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,4),_CucsCapabilityUpdaterFsmTaskCompletion_Type())
cucsCapabilityUpdaterFsmTaskCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskCompletion.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskFlags_Type=CucsFsmFlags
_CucsCapabilityUpdaterFsmTaskFlags_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskFlags=_CucsCapabilityUpdaterFsmTaskFlags_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,5),_CucsCapabilityUpdaterFsmTaskFlags_Type())
cucsCapabilityUpdaterFsmTaskFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskFlags.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskItem_Type=CucsCapabilityUpdaterFsmTaskItem
_CucsCapabilityUpdaterFsmTaskItem_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskItem=_CucsCapabilityUpdaterFsmTaskItem_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,6),_CucsCapabilityUpdaterFsmTaskItem_Type())
cucsCapabilityUpdaterFsmTaskItem.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskItem.setStatus(_A)
_CucsCapabilityUpdaterFsmTaskSeqId_Type=Gauge32
_CucsCapabilityUpdaterFsmTaskSeqId_Object=MibTableColumn
cucsCapabilityUpdaterFsmTaskSeqId=_CucsCapabilityUpdaterFsmTaskSeqId_Object((1,3,6,1,4,1,9,9,719,1,7,8,1,7),_CucsCapabilityUpdaterFsmTaskSeqId_Type())
cucsCapabilityUpdaterFsmTaskSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTaskSeqId.setStatus(_A)
_CucsCapabilityCatalogueFsmTable_Object=MibTable
cucsCapabilityCatalogueFsmTable=_CucsCapabilityCatalogueFsmTable_Object((1,3,6,1,4,1,9,9,719,1,7,9))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmTable.setStatus(_A)
_CucsCapabilityCatalogueFsmEntry_Object=MibTableRow
cucsCapabilityCatalogueFsmEntry=_CucsCapabilityCatalogueFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,7,9,1))
cucsCapabilityCatalogueFsmEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmEntry.setStatus(_A)
_CucsCapabilityCatalogueFsmInstanceId_Type=CucsManagedObjectId
_CucsCapabilityCatalogueFsmInstanceId_Object=MibTableColumn
cucsCapabilityCatalogueFsmInstanceId=_CucsCapabilityCatalogueFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,1),_CucsCapabilityCatalogueFsmInstanceId_Type())
cucsCapabilityCatalogueFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmInstanceId.setStatus(_A)
_CucsCapabilityCatalogueFsmDn_Type=CucsManagedObjectDn
_CucsCapabilityCatalogueFsmDn_Object=MibTableColumn
cucsCapabilityCatalogueFsmDn=_CucsCapabilityCatalogueFsmDn_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,2),_CucsCapabilityCatalogueFsmDn_Type())
cucsCapabilityCatalogueFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmDn.setStatus(_A)
_CucsCapabilityCatalogueFsmRn_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmRn_Object=MibTableColumn
cucsCapabilityCatalogueFsmRn=_CucsCapabilityCatalogueFsmRn_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,3),_CucsCapabilityCatalogueFsmRn_Type())
cucsCapabilityCatalogueFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRn.setStatus(_A)
_CucsCapabilityCatalogueFsmCompletionTime_Type=DateAndTime
_CucsCapabilityCatalogueFsmCompletionTime_Object=MibTableColumn
cucsCapabilityCatalogueFsmCompletionTime=_CucsCapabilityCatalogueFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,4),_CucsCapabilityCatalogueFsmCompletionTime_Type())
cucsCapabilityCatalogueFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmCompletionTime.setStatus(_A)
_CucsCapabilityCatalogueFsmCurrentFsm_Type=CucsCapabilityCatalogueFsmCurrentFsm
_CucsCapabilityCatalogueFsmCurrentFsm_Object=MibTableColumn
cucsCapabilityCatalogueFsmCurrentFsm=_CucsCapabilityCatalogueFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,5),_CucsCapabilityCatalogueFsmCurrentFsm_Type())
cucsCapabilityCatalogueFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmCurrentFsm.setStatus(_A)
_CucsCapabilityCatalogueFsmDescrData_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmDescrData_Object=MibTableColumn
cucsCapabilityCatalogueFsmDescrData=_CucsCapabilityCatalogueFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,6),_CucsCapabilityCatalogueFsmDescrData_Type())
cucsCapabilityCatalogueFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmDescrData.setStatus(_A)
_CucsCapabilityCatalogueFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityCatalogueFsmFsmStatus_Object=MibTableColumn
cucsCapabilityCatalogueFsmFsmStatus=_CucsCapabilityCatalogueFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,7),_CucsCapabilityCatalogueFsmFsmStatus_Type())
cucsCapabilityCatalogueFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmFsmStatus.setStatus(_A)
_CucsCapabilityCatalogueFsmProgress_Type=Gauge32
_CucsCapabilityCatalogueFsmProgress_Object=MibTableColumn
cucsCapabilityCatalogueFsmProgress=_CucsCapabilityCatalogueFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,8),_CucsCapabilityCatalogueFsmProgress_Type())
cucsCapabilityCatalogueFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmProgress.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtErrCode_Type=Gauge32
_CucsCapabilityCatalogueFsmRmtErrCode_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtErrCode=_CucsCapabilityCatalogueFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,9),_CucsCapabilityCatalogueFsmRmtErrCode_Type())
cucsCapabilityCatalogueFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtErrCode.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtErrDescr_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmRmtErrDescr_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtErrDescr=_CucsCapabilityCatalogueFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,10),_CucsCapabilityCatalogueFsmRmtErrDescr_Type())
cucsCapabilityCatalogueFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtErrDescr.setStatus(_A)
_CucsCapabilityCatalogueFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityCatalogueFsmRmtRslt_Object=MibTableColumn
cucsCapabilityCatalogueFsmRmtRslt=_CucsCapabilityCatalogueFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,7,9,1,11),_CucsCapabilityCatalogueFsmRmtRslt_Type())
cucsCapabilityCatalogueFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmRmtRslt.setStatus(_A)
_CucsCapabilityCatalogueFsmStageTable_Object=MibTable
cucsCapabilityCatalogueFsmStageTable=_CucsCapabilityCatalogueFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,7,10))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageTable.setStatus(_A)
_CucsCapabilityCatalogueFsmStageEntry_Object=MibTableRow
cucsCapabilityCatalogueFsmStageEntry=_CucsCapabilityCatalogueFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,7,10,1))
cucsCapabilityCatalogueFsmStageEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageEntry.setStatus(_A)
_CucsCapabilityCatalogueFsmStageInstanceId_Type=CucsManagedObjectId
_CucsCapabilityCatalogueFsmStageInstanceId_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageInstanceId=_CucsCapabilityCatalogueFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,1),_CucsCapabilityCatalogueFsmStageInstanceId_Type())
cucsCapabilityCatalogueFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageInstanceId.setStatus(_A)
_CucsCapabilityCatalogueFsmStageDn_Type=CucsManagedObjectDn
_CucsCapabilityCatalogueFsmStageDn_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageDn=_CucsCapabilityCatalogueFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,2),_CucsCapabilityCatalogueFsmStageDn_Type())
cucsCapabilityCatalogueFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageDn.setStatus(_A)
_CucsCapabilityCatalogueFsmStageRn_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmStageRn_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageRn=_CucsCapabilityCatalogueFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,3),_CucsCapabilityCatalogueFsmStageRn_Type())
cucsCapabilityCatalogueFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageRn.setStatus(_A)
_CucsCapabilityCatalogueFsmStageDescrData_Type=SnmpAdminString
_CucsCapabilityCatalogueFsmStageDescrData_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageDescrData=_CucsCapabilityCatalogueFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,4),_CucsCapabilityCatalogueFsmStageDescrData_Type())
cucsCapabilityCatalogueFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageDescrData.setStatus(_A)
_CucsCapabilityCatalogueFsmStageLastUpdateTime_Type=DateAndTime
_CucsCapabilityCatalogueFsmStageLastUpdateTime_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageLastUpdateTime=_CucsCapabilityCatalogueFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,5),_CucsCapabilityCatalogueFsmStageLastUpdateTime_Type())
cucsCapabilityCatalogueFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageLastUpdateTime.setStatus(_A)
_CucsCapabilityCatalogueFsmStageName_Type=CucsCapabilityCatalogueFsmStageName
_CucsCapabilityCatalogueFsmStageName_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageName=_CucsCapabilityCatalogueFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,6),_CucsCapabilityCatalogueFsmStageName_Type())
cucsCapabilityCatalogueFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageName.setStatus(_A)
_CucsCapabilityCatalogueFsmStageOrder_Type=Gauge32
_CucsCapabilityCatalogueFsmStageOrder_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageOrder=_CucsCapabilityCatalogueFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,7),_CucsCapabilityCatalogueFsmStageOrder_Type())
cucsCapabilityCatalogueFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageOrder.setStatus(_A)
_CucsCapabilityCatalogueFsmStageRetry_Type=Gauge32
_CucsCapabilityCatalogueFsmStageRetry_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageRetry=_CucsCapabilityCatalogueFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,8),_CucsCapabilityCatalogueFsmStageRetry_Type())
cucsCapabilityCatalogueFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageRetry.setStatus(_A)
_CucsCapabilityCatalogueFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityCatalogueFsmStageStageStatus_Object=MibTableColumn
cucsCapabilityCatalogueFsmStageStageStatus=_CucsCapabilityCatalogueFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,7,10,1,9),_CucsCapabilityCatalogueFsmStageStageStatus_Type())
cucsCapabilityCatalogueFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityCatalogueFsmStageStageStatus.setStatus(_A)
_CucsCapabilityFeatureLimitsTable_Object=MibTable
cucsCapabilityFeatureLimitsTable=_CucsCapabilityFeatureLimitsTable_Object((1,3,6,1,4,1,9,9,719,1,7,11))
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsTable.setStatus(_A)
_CucsCapabilityFeatureLimitsEntry_Object=MibTableRow
cucsCapabilityFeatureLimitsEntry=_CucsCapabilityFeatureLimitsEntry_Object((1,3,6,1,4,1,9,9,719,1,7,11,1))
cucsCapabilityFeatureLimitsEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsEntry.setStatus(_A)
_CucsCapabilityFeatureLimitsInstanceId_Type=CucsManagedObjectId
_CucsCapabilityFeatureLimitsInstanceId_Object=MibTableColumn
cucsCapabilityFeatureLimitsInstanceId=_CucsCapabilityFeatureLimitsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,1),_CucsCapabilityFeatureLimitsInstanceId_Type())
cucsCapabilityFeatureLimitsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsInstanceId.setStatus(_A)
_CucsCapabilityFeatureLimitsDn_Type=CucsManagedObjectDn
_CucsCapabilityFeatureLimitsDn_Object=MibTableColumn
cucsCapabilityFeatureLimitsDn=_CucsCapabilityFeatureLimitsDn_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,2),_CucsCapabilityFeatureLimitsDn_Type())
cucsCapabilityFeatureLimitsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsDn.setStatus(_A)
_CucsCapabilityFeatureLimitsRn_Type=SnmpAdminString
_CucsCapabilityFeatureLimitsRn_Object=MibTableColumn
cucsCapabilityFeatureLimitsRn=_CucsCapabilityFeatureLimitsRn_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,3),_CucsCapabilityFeatureLimitsRn_Type())
cucsCapabilityFeatureLimitsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsRn.setStatus(_A)
_CucsCapabilityFeatureLimitsDescr_Type=SnmpAdminString
_CucsCapabilityFeatureLimitsDescr_Object=MibTableColumn
cucsCapabilityFeatureLimitsDescr=_CucsCapabilityFeatureLimitsDescr_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,4),_CucsCapabilityFeatureLimitsDescr_Type())
cucsCapabilityFeatureLimitsDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsDescr.setStatus(_A)
_CucsCapabilityFeatureLimitsFeatureStatus_Type=CucsCapabilityFeatureStatus
_CucsCapabilityFeatureLimitsFeatureStatus_Object=MibTableColumn
cucsCapabilityFeatureLimitsFeatureStatus=_CucsCapabilityFeatureLimitsFeatureStatus_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,5),_CucsCapabilityFeatureLimitsFeatureStatus_Type())
cucsCapabilityFeatureLimitsFeatureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsFeatureStatus.setStatus(_A)
_CucsCapabilityFeatureLimitsLimit_Type=Gauge32
_CucsCapabilityFeatureLimitsLimit_Object=MibTableColumn
cucsCapabilityFeatureLimitsLimit=_CucsCapabilityFeatureLimitsLimit_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,6),_CucsCapabilityFeatureLimitsLimit_Type())
cucsCapabilityFeatureLimitsLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsLimit.setStatus(_A)
_CucsCapabilityFeatureLimitsName_Type=SnmpAdminString
_CucsCapabilityFeatureLimitsName_Object=MibTableColumn
cucsCapabilityFeatureLimitsName=_CucsCapabilityFeatureLimitsName_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,7),_CucsCapabilityFeatureLimitsName_Type())
cucsCapabilityFeatureLimitsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsName.setStatus(_A)
_CucsCapabilityFeatureLimitsPlatform_Type=CucsCapabilityPlatform
_CucsCapabilityFeatureLimitsPlatform_Object=MibTableColumn
cucsCapabilityFeatureLimitsPlatform=_CucsCapabilityFeatureLimitsPlatform_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,8),_CucsCapabilityFeatureLimitsPlatform_Type())
cucsCapabilityFeatureLimitsPlatform.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsPlatform.setStatus(_A)
_CucsCapabilityFeatureLimitsMinUCSMVersion_Type=SnmpAdminString
_CucsCapabilityFeatureLimitsMinUCSMVersion_Object=MibTableColumn
cucsCapabilityFeatureLimitsMinUCSMVersion=_CucsCapabilityFeatureLimitsMinUCSMVersion_Object((1,3,6,1,4,1,9,9,719,1,7,11,1,9),_CucsCapabilityFeatureLimitsMinUCSMVersion_Type())
cucsCapabilityFeatureLimitsMinUCSMVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityFeatureLimitsMinUCSMVersion.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmTable_Object=MibTable
cucsCapabilityMgmtExtensionFsmTable=_CucsCapabilityMgmtExtensionFsmTable_Object((1,3,6,1,4,1,9,9,719,1,7,12))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmTable.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmEntry_Object=MibTableRow
cucsCapabilityMgmtExtensionFsmEntry=_CucsCapabilityMgmtExtensionFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,7,12,1))
cucsCapabilityMgmtExtensionFsmEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmEntry.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmInstanceId_Type=CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmInstanceId_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmInstanceId=_CucsCapabilityMgmtExtensionFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,1),_CucsCapabilityMgmtExtensionFsmInstanceId_Type())
cucsCapabilityMgmtExtensionFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmInstanceId.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmDn_Type=CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmDn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmDn=_CucsCapabilityMgmtExtensionFsmDn_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,2),_CucsCapabilityMgmtExtensionFsmDn_Type())
cucsCapabilityMgmtExtensionFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmDn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRn_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRn=_CucsCapabilityMgmtExtensionFsmRn_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,3),_CucsCapabilityMgmtExtensionFsmRn_Type())
cucsCapabilityMgmtExtensionFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmCompletionTime_Type=DateAndTime
_CucsCapabilityMgmtExtensionFsmCompletionTime_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmCompletionTime=_CucsCapabilityMgmtExtensionFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,4),_CucsCapabilityMgmtExtensionFsmCompletionTime_Type())
cucsCapabilityMgmtExtensionFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmCompletionTime.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmCurrentFsm_Type=CucsCapabilityMgmtExtensionFsmCurrentFsm
_CucsCapabilityMgmtExtensionFsmCurrentFsm_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmCurrentFsm=_CucsCapabilityMgmtExtensionFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,5),_CucsCapabilityMgmtExtensionFsmCurrentFsm_Type())
cucsCapabilityMgmtExtensionFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmCurrentFsm.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmDescrData_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmDescrData_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmDescrData=_CucsCapabilityMgmtExtensionFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,6),_CucsCapabilityMgmtExtensionFsmDescrData_Type())
cucsCapabilityMgmtExtensionFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmDescrData.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityMgmtExtensionFsmFsmStatus_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmFsmStatus=_CucsCapabilityMgmtExtensionFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,7),_CucsCapabilityMgmtExtensionFsmFsmStatus_Type())
cucsCapabilityMgmtExtensionFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmFsmStatus.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmProgress_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmProgress_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmProgress=_CucsCapabilityMgmtExtensionFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,8),_CucsCapabilityMgmtExtensionFsmProgress_Type())
cucsCapabilityMgmtExtensionFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmProgress.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtErrCode_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmRmtErrCode_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtErrCode=_CucsCapabilityMgmtExtensionFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,9),_CucsCapabilityMgmtExtensionFsmRmtErrCode_Type())
cucsCapabilityMgmtExtensionFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtErrCode.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtErrDescr=_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,10),_CucsCapabilityMgmtExtensionFsmRmtErrDescr_Type())
cucsCapabilityMgmtExtensionFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtErrDescr.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityMgmtExtensionFsmRmtRslt_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmRmtRslt=_CucsCapabilityMgmtExtensionFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,7,12,1,11),_CucsCapabilityMgmtExtensionFsmRmtRslt_Type())
cucsCapabilityMgmtExtensionFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmRmtRslt.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageTable_Object=MibTable
cucsCapabilityMgmtExtensionFsmStageTable=_CucsCapabilityMgmtExtensionFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,7,13))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageTable.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageEntry_Object=MibTableRow
cucsCapabilityMgmtExtensionFsmStageEntry=_CucsCapabilityMgmtExtensionFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,7,13,1))
cucsCapabilityMgmtExtensionFsmStageEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageEntry.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageInstanceId_Type=CucsManagedObjectId
_CucsCapabilityMgmtExtensionFsmStageInstanceId_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageInstanceId=_CucsCapabilityMgmtExtensionFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,1),_CucsCapabilityMgmtExtensionFsmStageInstanceId_Type())
cucsCapabilityMgmtExtensionFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageInstanceId.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageDn_Type=CucsManagedObjectDn
_CucsCapabilityMgmtExtensionFsmStageDn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDn=_CucsCapabilityMgmtExtensionFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,2),_CucsCapabilityMgmtExtensionFsmStageDn_Type())
cucsCapabilityMgmtExtensionFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageDn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageRn_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageRn_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageRn=_CucsCapabilityMgmtExtensionFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,3),_CucsCapabilityMgmtExtensionFsmStageRn_Type())
cucsCapabilityMgmtExtensionFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageRn.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageDescrData_Type=SnmpAdminString
_CucsCapabilityMgmtExtensionFsmStageDescrData_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageDescrData=_CucsCapabilityMgmtExtensionFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,4),_CucsCapabilityMgmtExtensionFsmStageDescrData_Type())
cucsCapabilityMgmtExtensionFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageDescrData.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Type=DateAndTime
_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageLastUpdateTime=_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,5),_CucsCapabilityMgmtExtensionFsmStageLastUpdateTime_Type())
cucsCapabilityMgmtExtensionFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageLastUpdateTime.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageName_Type=CucsCapabilityMgmtExtensionFsmStageName
_CucsCapabilityMgmtExtensionFsmStageName_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageName=_CucsCapabilityMgmtExtensionFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,6),_CucsCapabilityMgmtExtensionFsmStageName_Type())
cucsCapabilityMgmtExtensionFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageName.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageOrder_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmStageOrder_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageOrder=_CucsCapabilityMgmtExtensionFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,7),_CucsCapabilityMgmtExtensionFsmStageOrder_Type())
cucsCapabilityMgmtExtensionFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageOrder.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageRetry_Type=Gauge32
_CucsCapabilityMgmtExtensionFsmStageRetry_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageRetry=_CucsCapabilityMgmtExtensionFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,8),_CucsCapabilityMgmtExtensionFsmStageRetry_Type())
cucsCapabilityMgmtExtensionFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageRetry.setStatus(_A)
_CucsCapabilityMgmtExtensionFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityMgmtExtensionFsmStageStageStatus_Object=MibTableColumn
cucsCapabilityMgmtExtensionFsmStageStageStatus=_CucsCapabilityMgmtExtensionFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,7,13,1,9),_CucsCapabilityMgmtExtensionFsmStageStageStatus_Type())
cucsCapabilityMgmtExtensionFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityMgmtExtensionFsmStageStageStatus.setStatus(_A)
_CucsCapabilityNetworkLimitsTable_Object=MibTable
cucsCapabilityNetworkLimitsTable=_CucsCapabilityNetworkLimitsTable_Object((1,3,6,1,4,1,9,9,719,1,7,14))
if mibBuilder.loadTexts:cucsCapabilityNetworkLimitsTable.setStatus(_A)
_CucsCapabilityNetworkLimitsEntry_Object=MibTableRow
cucsCapabilityNetworkLimitsEntry=_CucsCapabilityNetworkLimitsEntry_Object((1,3,6,1,4,1,9,9,719,1,7,14,1))
cucsCapabilityNetworkLimitsEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsCapabilityNetworkLimitsEntry.setStatus(_A)
_CucsCapabilityNetworkLimitsInstanceId_Type=CucsManagedObjectId
_CucsCapabilityNetworkLimitsInstanceId_Object=MibTableColumn
cucsCapabilityNetworkLimitsInstanceId=_CucsCapabilityNetworkLimitsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,14,1,1),_CucsCapabilityNetworkLimitsInstanceId_Type())
cucsCapabilityNetworkLimitsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityNetworkLimitsInstanceId.setStatus(_A)
_CucsCapabilityNetworkLimitsDn_Type=CucsManagedObjectDn
_CucsCapabilityNetworkLimitsDn_Object=MibTableColumn
cucsCapabilityNetworkLimitsDn=_CucsCapabilityNetworkLimitsDn_Object((1,3,6,1,4,1,9,9,719,1,7,14,1,2),_CucsCapabilityNetworkLimitsDn_Type())
cucsCapabilityNetworkLimitsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityNetworkLimitsDn.setStatus(_A)
_CucsCapabilityNetworkLimitsRn_Type=SnmpAdminString
_CucsCapabilityNetworkLimitsRn_Object=MibTableColumn
cucsCapabilityNetworkLimitsRn=_CucsCapabilityNetworkLimitsRn_Object((1,3,6,1,4,1,9,9,719,1,7,14,1,3),_CucsCapabilityNetworkLimitsRn_Type())
cucsCapabilityNetworkLimitsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityNetworkLimitsRn.setStatus(_A)
_CucsCapabilityStorageLimitsTable_Object=MibTable
cucsCapabilityStorageLimitsTable=_CucsCapabilityStorageLimitsTable_Object((1,3,6,1,4,1,9,9,719,1,7,15))
if mibBuilder.loadTexts:cucsCapabilityStorageLimitsTable.setStatus(_A)
_CucsCapabilityStorageLimitsEntry_Object=MibTableRow
cucsCapabilityStorageLimitsEntry=_CucsCapabilityStorageLimitsEntry_Object((1,3,6,1,4,1,9,9,719,1,7,15,1))
cucsCapabilityStorageLimitsEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsCapabilityStorageLimitsEntry.setStatus(_A)
_CucsCapabilityStorageLimitsInstanceId_Type=CucsManagedObjectId
_CucsCapabilityStorageLimitsInstanceId_Object=MibTableColumn
cucsCapabilityStorageLimitsInstanceId=_CucsCapabilityStorageLimitsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,15,1,1),_CucsCapabilityStorageLimitsInstanceId_Type())
cucsCapabilityStorageLimitsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityStorageLimitsInstanceId.setStatus(_A)
_CucsCapabilityStorageLimitsDn_Type=CucsManagedObjectDn
_CucsCapabilityStorageLimitsDn_Object=MibTableColumn
cucsCapabilityStorageLimitsDn=_CucsCapabilityStorageLimitsDn_Object((1,3,6,1,4,1,9,9,719,1,7,15,1,2),_CucsCapabilityStorageLimitsDn_Type())
cucsCapabilityStorageLimitsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityStorageLimitsDn.setStatus(_A)
_CucsCapabilityStorageLimitsRn_Type=SnmpAdminString
_CucsCapabilityStorageLimitsRn_Object=MibTableColumn
cucsCapabilityStorageLimitsRn=_CucsCapabilityStorageLimitsRn_Object((1,3,6,1,4,1,9,9,719,1,7,15,1,3),_CucsCapabilityStorageLimitsRn_Type())
cucsCapabilityStorageLimitsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityStorageLimitsRn.setStatus(_A)
_CucsCapabilitySystemLimitsTable_Object=MibTable
cucsCapabilitySystemLimitsTable=_CucsCapabilitySystemLimitsTable_Object((1,3,6,1,4,1,9,9,719,1,7,16))
if mibBuilder.loadTexts:cucsCapabilitySystemLimitsTable.setStatus(_A)
_CucsCapabilitySystemLimitsEntry_Object=MibTableRow
cucsCapabilitySystemLimitsEntry=_CucsCapabilitySystemLimitsEntry_Object((1,3,6,1,4,1,9,9,719,1,7,16,1))
cucsCapabilitySystemLimitsEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsCapabilitySystemLimitsEntry.setStatus(_A)
_CucsCapabilitySystemLimitsInstanceId_Type=CucsManagedObjectId
_CucsCapabilitySystemLimitsInstanceId_Object=MibTableColumn
cucsCapabilitySystemLimitsInstanceId=_CucsCapabilitySystemLimitsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,16,1,1),_CucsCapabilitySystemLimitsInstanceId_Type())
cucsCapabilitySystemLimitsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilitySystemLimitsInstanceId.setStatus(_A)
_CucsCapabilitySystemLimitsDn_Type=CucsManagedObjectDn
_CucsCapabilitySystemLimitsDn_Object=MibTableColumn
cucsCapabilitySystemLimitsDn=_CucsCapabilitySystemLimitsDn_Object((1,3,6,1,4,1,9,9,719,1,7,16,1,2),_CucsCapabilitySystemLimitsDn_Type())
cucsCapabilitySystemLimitsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilitySystemLimitsDn.setStatus(_A)
_CucsCapabilitySystemLimitsRn_Type=SnmpAdminString
_CucsCapabilitySystemLimitsRn_Object=MibTableColumn
cucsCapabilitySystemLimitsRn=_CucsCapabilitySystemLimitsRn_Object((1,3,6,1,4,1,9,9,719,1,7,16,1,3),_CucsCapabilitySystemLimitsRn_Type())
cucsCapabilitySystemLimitsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilitySystemLimitsRn.setStatus(_A)
_CucsCapabilityUpdaterFsmTable_Object=MibTable
cucsCapabilityUpdaterFsmTable=_CucsCapabilityUpdaterFsmTable_Object((1,3,6,1,4,1,9,9,719,1,7,17))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmTable.setStatus(_A)
_CucsCapabilityUpdaterFsmEntry_Object=MibTableRow
cucsCapabilityUpdaterFsmEntry=_CucsCapabilityUpdaterFsmEntry_Object((1,3,6,1,4,1,9,9,719,1,7,17,1))
cucsCapabilityUpdaterFsmEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmEntry.setStatus(_A)
_CucsCapabilityUpdaterFsmInstanceId_Type=CucsManagedObjectId
_CucsCapabilityUpdaterFsmInstanceId_Object=MibTableColumn
cucsCapabilityUpdaterFsmInstanceId=_CucsCapabilityUpdaterFsmInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,1),_CucsCapabilityUpdaterFsmInstanceId_Type())
cucsCapabilityUpdaterFsmInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmInstanceId.setStatus(_A)
_CucsCapabilityUpdaterFsmDn_Type=CucsManagedObjectDn
_CucsCapabilityUpdaterFsmDn_Object=MibTableColumn
cucsCapabilityUpdaterFsmDn=_CucsCapabilityUpdaterFsmDn_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,2),_CucsCapabilityUpdaterFsmDn_Type())
cucsCapabilityUpdaterFsmDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmDn.setStatus(_A)
_CucsCapabilityUpdaterFsmRn_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmRn_Object=MibTableColumn
cucsCapabilityUpdaterFsmRn=_CucsCapabilityUpdaterFsmRn_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,3),_CucsCapabilityUpdaterFsmRn_Type())
cucsCapabilityUpdaterFsmRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRn.setStatus(_A)
_CucsCapabilityUpdaterFsmCompletionTime_Type=DateAndTime
_CucsCapabilityUpdaterFsmCompletionTime_Object=MibTableColumn
cucsCapabilityUpdaterFsmCompletionTime=_CucsCapabilityUpdaterFsmCompletionTime_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,4),_CucsCapabilityUpdaterFsmCompletionTime_Type())
cucsCapabilityUpdaterFsmCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmCompletionTime.setStatus(_A)
_CucsCapabilityUpdaterFsmCurrentFsm_Type=CucsCapabilityUpdaterFsmCurrentFsm
_CucsCapabilityUpdaterFsmCurrentFsm_Object=MibTableColumn
cucsCapabilityUpdaterFsmCurrentFsm=_CucsCapabilityUpdaterFsmCurrentFsm_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,5),_CucsCapabilityUpdaterFsmCurrentFsm_Type())
cucsCapabilityUpdaterFsmCurrentFsm.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmCurrentFsm.setStatus(_A)
_CucsCapabilityUpdaterFsmDescrData_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmDescrData_Object=MibTableColumn
cucsCapabilityUpdaterFsmDescrData=_CucsCapabilityUpdaterFsmDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,6),_CucsCapabilityUpdaterFsmDescrData_Type())
cucsCapabilityUpdaterFsmDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmDescrData.setStatus(_A)
_CucsCapabilityUpdaterFsmFsmStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityUpdaterFsmFsmStatus_Object=MibTableColumn
cucsCapabilityUpdaterFsmFsmStatus=_CucsCapabilityUpdaterFsmFsmStatus_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,7),_CucsCapabilityUpdaterFsmFsmStatus_Type())
cucsCapabilityUpdaterFsmFsmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmFsmStatus.setStatus(_A)
_CucsCapabilityUpdaterFsmProgress_Type=Gauge32
_CucsCapabilityUpdaterFsmProgress_Object=MibTableColumn
cucsCapabilityUpdaterFsmProgress=_CucsCapabilityUpdaterFsmProgress_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,8),_CucsCapabilityUpdaterFsmProgress_Type())
cucsCapabilityUpdaterFsmProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmProgress.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtErrCode_Type=Gauge32
_CucsCapabilityUpdaterFsmRmtErrCode_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtErrCode=_CucsCapabilityUpdaterFsmRmtErrCode_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,9),_CucsCapabilityUpdaterFsmRmtErrCode_Type())
cucsCapabilityUpdaterFsmRmtErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtErrCode.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtErrDescr_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmRmtErrDescr_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtErrDescr=_CucsCapabilityUpdaterFsmRmtErrDescr_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,10),_CucsCapabilityUpdaterFsmRmtErrDescr_Type())
cucsCapabilityUpdaterFsmRmtErrDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtErrDescr.setStatus(_A)
_CucsCapabilityUpdaterFsmRmtRslt_Type=CucsConditionRemoteInvRslt
_CucsCapabilityUpdaterFsmRmtRslt_Object=MibTableColumn
cucsCapabilityUpdaterFsmRmtRslt=_CucsCapabilityUpdaterFsmRmtRslt_Object((1,3,6,1,4,1,9,9,719,1,7,17,1,11),_CucsCapabilityUpdaterFsmRmtRslt_Type())
cucsCapabilityUpdaterFsmRmtRslt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmRmtRslt.setStatus(_A)
_CucsCapabilityUpdaterFsmStageTable_Object=MibTable
cucsCapabilityUpdaterFsmStageTable=_CucsCapabilityUpdaterFsmStageTable_Object((1,3,6,1,4,1,9,9,719,1,7,18))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageTable.setStatus(_A)
_CucsCapabilityUpdaterFsmStageEntry_Object=MibTableRow
cucsCapabilityUpdaterFsmStageEntry=_CucsCapabilityUpdaterFsmStageEntry_Object((1,3,6,1,4,1,9,9,719,1,7,18,1))
cucsCapabilityUpdaterFsmStageEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageEntry.setStatus(_A)
_CucsCapabilityUpdaterFsmStageInstanceId_Type=CucsManagedObjectId
_CucsCapabilityUpdaterFsmStageInstanceId_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageInstanceId=_CucsCapabilityUpdaterFsmStageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,1),_CucsCapabilityUpdaterFsmStageInstanceId_Type())
cucsCapabilityUpdaterFsmStageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageInstanceId.setStatus(_A)
_CucsCapabilityUpdaterFsmStageDn_Type=CucsManagedObjectDn
_CucsCapabilityUpdaterFsmStageDn_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageDn=_CucsCapabilityUpdaterFsmStageDn_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,2),_CucsCapabilityUpdaterFsmStageDn_Type())
cucsCapabilityUpdaterFsmStageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageDn.setStatus(_A)
_CucsCapabilityUpdaterFsmStageRn_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmStageRn_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageRn=_CucsCapabilityUpdaterFsmStageRn_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,3),_CucsCapabilityUpdaterFsmStageRn_Type())
cucsCapabilityUpdaterFsmStageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageRn.setStatus(_A)
_CucsCapabilityUpdaterFsmStageDescrData_Type=SnmpAdminString
_CucsCapabilityUpdaterFsmStageDescrData_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageDescrData=_CucsCapabilityUpdaterFsmStageDescrData_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,4),_CucsCapabilityUpdaterFsmStageDescrData_Type())
cucsCapabilityUpdaterFsmStageDescrData.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageDescrData.setStatus(_A)
_CucsCapabilityUpdaterFsmStageLastUpdateTime_Type=DateAndTime
_CucsCapabilityUpdaterFsmStageLastUpdateTime_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageLastUpdateTime=_CucsCapabilityUpdaterFsmStageLastUpdateTime_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,5),_CucsCapabilityUpdaterFsmStageLastUpdateTime_Type())
cucsCapabilityUpdaterFsmStageLastUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageLastUpdateTime.setStatus(_A)
_CucsCapabilityUpdaterFsmStageName_Type=CucsCapabilityUpdaterFsmStageName
_CucsCapabilityUpdaterFsmStageName_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageName=_CucsCapabilityUpdaterFsmStageName_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,6),_CucsCapabilityUpdaterFsmStageName_Type())
cucsCapabilityUpdaterFsmStageName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageName.setStatus(_A)
_CucsCapabilityUpdaterFsmStageOrder_Type=Gauge32
_CucsCapabilityUpdaterFsmStageOrder_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageOrder=_CucsCapabilityUpdaterFsmStageOrder_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,7),_CucsCapabilityUpdaterFsmStageOrder_Type())
cucsCapabilityUpdaterFsmStageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageOrder.setStatus(_A)
_CucsCapabilityUpdaterFsmStageRetry_Type=Gauge32
_CucsCapabilityUpdaterFsmStageRetry_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageRetry=_CucsCapabilityUpdaterFsmStageRetry_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,8),_CucsCapabilityUpdaterFsmStageRetry_Type())
cucsCapabilityUpdaterFsmStageRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageRetry.setStatus(_A)
_CucsCapabilityUpdaterFsmStageStageStatus_Type=CucsFsmFsmStageStatus
_CucsCapabilityUpdaterFsmStageStageStatus_Object=MibTableColumn
cucsCapabilityUpdaterFsmStageStageStatus=_CucsCapabilityUpdaterFsmStageStageStatus_Object((1,3,6,1,4,1,9,9,719,1,7,18,1,9),_CucsCapabilityUpdaterFsmStageStageStatus_Type())
cucsCapabilityUpdaterFsmStageStageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsCapabilityUpdaterFsmStageStageStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsCapabilityObjects':cucsCapabilityObjects,'cucsCapabilityCatalogueTable':cucsCapabilityCatalogueTable,'cucsCapabilityCatalogueEntry':cucsCapabilityCatalogueEntry,_E:cucsCapabilityCatalogueInstanceId,'cucsCapabilityCatalogueDn':cucsCapabilityCatalogueDn,'cucsCapabilityCatalogueRn':cucsCapabilityCatalogueRn,'cucsCapabilityCatalogueFsmDescr':cucsCapabilityCatalogueFsmDescr,'cucsCapabilityCatalogueFsmPrev':cucsCapabilityCatalogueFsmPrev,'cucsCapabilityCatalogueFsmProgr':cucsCapabilityCatalogueFsmProgr,'cucsCapabilityCatalogueFsmRmtInvErrCode':cucsCapabilityCatalogueFsmRmtInvErrCode,'cucsCapabilityCatalogueFsmRmtInvErrDescr':cucsCapabilityCatalogueFsmRmtInvErrDescr,'cucsCapabilityCatalogueFsmRmtInvRslt':cucsCapabilityCatalogueFsmRmtInvRslt,'cucsCapabilityCatalogueFsmStageDescr':cucsCapabilityCatalogueFsmStageDescr,'cucsCapabilityCatalogueFsmStamp':cucsCapabilityCatalogueFsmStamp,'cucsCapabilityCatalogueFsmStatus':cucsCapabilityCatalogueFsmStatus,'cucsCapabilityCatalogueFsmTry':cucsCapabilityCatalogueFsmTry,'cucsCapabilityCatalogueVersion':cucsCapabilityCatalogueVersion,'cucsCapabilityCatalogueFileParseFailures':cucsCapabilityCatalogueFileParseFailures,'cucsCapabilityCatalogueFilesParsed':cucsCapabilityCatalogueFilesParsed,'cucsCapabilityCatalogueLoadErrors':cucsCapabilityCatalogueLoadErrors,'cucsCapabilityCatalogueLoadWarnings':cucsCapabilityCatalogueLoadWarnings,'cucsCapabilityCatalogueProviderLoadFailures':cucsCapabilityCatalogueProviderLoadFailures,'cucsCapabilityCatalogueProvidersLoaded':cucsCapabilityCatalogueProvidersLoaded,'cucsCapabilityCatalogueFsmTaskTable':cucsCapabilityCatalogueFsmTaskTable,'cucsCapabilityCatalogueFsmTaskEntry':cucsCapabilityCatalogueFsmTaskEntry,_F:cucsCapabilityCatalogueFsmTaskInstanceId,'cucsCapabilityCatalogueFsmTaskDn':cucsCapabilityCatalogueFsmTaskDn,'cucsCapabilityCatalogueFsmTaskRn':cucsCapabilityCatalogueFsmTaskRn,'cucsCapabilityCatalogueFsmTaskCompletion':cucsCapabilityCatalogueFsmTaskCompletion,'cucsCapabilityCatalogueFsmTaskFlags':cucsCapabilityCatalogueFsmTaskFlags,'cucsCapabilityCatalogueFsmTaskItem':cucsCapabilityCatalogueFsmTaskItem,'cucsCapabilityCatalogueFsmTaskSeqId':cucsCapabilityCatalogueFsmTaskSeqId,'cucsCapabilityEpTable':cucsCapabilityEpTable,'cucsCapabilityEpEntry':cucsCapabilityEpEntry,_G:cucsCapabilityEpInstanceId,'cucsCapabilityEpDn':cucsCapabilityEpDn,'cucsCapabilityEpRn':cucsCapabilityEpRn,'cucsCapabilityMgmtExtensionTable':cucsCapabilityMgmtExtensionTable,'cucsCapabilityMgmtExtensionEntry':cucsCapabilityMgmtExtensionEntry,_H:cucsCapabilityMgmtExtensionInstanceId,'cucsCapabilityMgmtExtensionDn':cucsCapabilityMgmtExtensionDn,'cucsCapabilityMgmtExtensionRn':cucsCapabilityMgmtExtensionRn,'cucsCapabilityMgmtExtensionFsmDescr':cucsCapabilityMgmtExtensionFsmDescr,'cucsCapabilityMgmtExtensionFsmPrev':cucsCapabilityMgmtExtensionFsmPrev,'cucsCapabilityMgmtExtensionFsmProgr':cucsCapabilityMgmtExtensionFsmProgr,'cucsCapabilityMgmtExtensionFsmRmtInvErrCode':cucsCapabilityMgmtExtensionFsmRmtInvErrCode,'cucsCapabilityMgmtExtensionFsmRmtInvErrDescr':cucsCapabilityMgmtExtensionFsmRmtInvErrDescr,'cucsCapabilityMgmtExtensionFsmRmtInvRslt':cucsCapabilityMgmtExtensionFsmRmtInvRslt,'cucsCapabilityMgmtExtensionFsmStageDescr':cucsCapabilityMgmtExtensionFsmStageDescr,'cucsCapabilityMgmtExtensionFsmStamp':cucsCapabilityMgmtExtensionFsmStamp,'cucsCapabilityMgmtExtensionFsmStatus':cucsCapabilityMgmtExtensionFsmStatus,'cucsCapabilityMgmtExtensionFsmTry':cucsCapabilityMgmtExtensionFsmTry,'cucsCapabilityMgmtExtensionFsmTaskTable':cucsCapabilityMgmtExtensionFsmTaskTable,'cucsCapabilityMgmtExtensionFsmTaskEntry':cucsCapabilityMgmtExtensionFsmTaskEntry,_I:cucsCapabilityMgmtExtensionFsmTaskInstanceId,'cucsCapabilityMgmtExtensionFsmTaskDn':cucsCapabilityMgmtExtensionFsmTaskDn,'cucsCapabilityMgmtExtensionFsmTaskRn':cucsCapabilityMgmtExtensionFsmTaskRn,'cucsCapabilityMgmtExtensionFsmTaskCompletion':cucsCapabilityMgmtExtensionFsmTaskCompletion,'cucsCapabilityMgmtExtensionFsmTaskFlags':cucsCapabilityMgmtExtensionFsmTaskFlags,'cucsCapabilityMgmtExtensionFsmTaskItem':cucsCapabilityMgmtExtensionFsmTaskItem,'cucsCapabilityMgmtExtensionFsmTaskSeqId':cucsCapabilityMgmtExtensionFsmTaskSeqId,'cucsCapabilityUpdateTable':cucsCapabilityUpdateTable,'cucsCapabilityUpdateEntry':cucsCapabilityUpdateEntry,_J:cucsCapabilityUpdateInstanceId,'cucsCapabilityUpdateDn':cucsCapabilityUpdateDn,'cucsCapabilityUpdateRn':cucsCapabilityUpdateRn,'cucsCapabilityUpdateImageName':cucsCapabilityUpdateImageName,'cucsCapabilityUpdateUpdateTs':cucsCapabilityUpdateUpdateTs,'cucsCapabilityUpdateVersion':cucsCapabilityUpdateVersion,'cucsCapabilityUpdaterTable':cucsCapabilityUpdaterTable,'cucsCapabilityUpdaterEntry':cucsCapabilityUpdaterEntry,_K:cucsCapabilityUpdaterInstanceId,'cucsCapabilityUpdaterDn':cucsCapabilityUpdaterDn,'cucsCapabilityUpdaterRn':cucsCapabilityUpdaterRn,'cucsCapabilityUpdaterAdminState':cucsCapabilityUpdaterAdminState,'cucsCapabilityUpdaterFileName':cucsCapabilityUpdaterFileName,'cucsCapabilityUpdaterFsmDescr':cucsCapabilityUpdaterFsmDescr,'cucsCapabilityUpdaterFsmPrev':cucsCapabilityUpdaterFsmPrev,'cucsCapabilityUpdaterFsmProgr':cucsCapabilityUpdaterFsmProgr,'cucsCapabilityUpdaterFsmRmtInvErrCode':cucsCapabilityUpdaterFsmRmtInvErrCode,'cucsCapabilityUpdaterFsmRmtInvErrDescr':cucsCapabilityUpdaterFsmRmtInvErrDescr,'cucsCapabilityUpdaterFsmRmtInvRslt':cucsCapabilityUpdaterFsmRmtInvRslt,'cucsCapabilityUpdaterFsmStageDescr':cucsCapabilityUpdaterFsmStageDescr,'cucsCapabilityUpdaterFsmStamp':cucsCapabilityUpdaterFsmStamp,'cucsCapabilityUpdaterFsmStatus':cucsCapabilityUpdaterFsmStatus,'cucsCapabilityUpdaterFsmTry':cucsCapabilityUpdaterFsmTry,'cucsCapabilityUpdaterImageName':cucsCapabilityUpdaterImageName,'cucsCapabilityUpdaterOperState':cucsCapabilityUpdaterOperState,'cucsCapabilityUpdaterProtocol':cucsCapabilityUpdaterProtocol,'cucsCapabilityUpdaterPwd':cucsCapabilityUpdaterPwd,'cucsCapabilityUpdaterRemotePath':cucsCapabilityUpdaterRemotePath,'cucsCapabilityUpdaterServer':cucsCapabilityUpdaterServer,'cucsCapabilityUpdaterUser':cucsCapabilityUpdaterUser,'cucsCapabilityUpdaterVersion':cucsCapabilityUpdaterVersion,'cucsCapabilityUpdaterFsmTaskTable':cucsCapabilityUpdaterFsmTaskTable,'cucsCapabilityUpdaterFsmTaskEntry':cucsCapabilityUpdaterFsmTaskEntry,_L:cucsCapabilityUpdaterFsmTaskInstanceId,'cucsCapabilityUpdaterFsmTaskDn':cucsCapabilityUpdaterFsmTaskDn,'cucsCapabilityUpdaterFsmTaskRn':cucsCapabilityUpdaterFsmTaskRn,'cucsCapabilityUpdaterFsmTaskCompletion':cucsCapabilityUpdaterFsmTaskCompletion,'cucsCapabilityUpdaterFsmTaskFlags':cucsCapabilityUpdaterFsmTaskFlags,'cucsCapabilityUpdaterFsmTaskItem':cucsCapabilityUpdaterFsmTaskItem,'cucsCapabilityUpdaterFsmTaskSeqId':cucsCapabilityUpdaterFsmTaskSeqId,'cucsCapabilityCatalogueFsmTable':cucsCapabilityCatalogueFsmTable,'cucsCapabilityCatalogueFsmEntry':cucsCapabilityCatalogueFsmEntry,_M:cucsCapabilityCatalogueFsmInstanceId,'cucsCapabilityCatalogueFsmDn':cucsCapabilityCatalogueFsmDn,'cucsCapabilityCatalogueFsmRn':cucsCapabilityCatalogueFsmRn,'cucsCapabilityCatalogueFsmCompletionTime':cucsCapabilityCatalogueFsmCompletionTime,'cucsCapabilityCatalogueFsmCurrentFsm':cucsCapabilityCatalogueFsmCurrentFsm,'cucsCapabilityCatalogueFsmDescrData':cucsCapabilityCatalogueFsmDescrData,'cucsCapabilityCatalogueFsmFsmStatus':cucsCapabilityCatalogueFsmFsmStatus,'cucsCapabilityCatalogueFsmProgress':cucsCapabilityCatalogueFsmProgress,'cucsCapabilityCatalogueFsmRmtErrCode':cucsCapabilityCatalogueFsmRmtErrCode,'cucsCapabilityCatalogueFsmRmtErrDescr':cucsCapabilityCatalogueFsmRmtErrDescr,'cucsCapabilityCatalogueFsmRmtRslt':cucsCapabilityCatalogueFsmRmtRslt,'cucsCapabilityCatalogueFsmStageTable':cucsCapabilityCatalogueFsmStageTable,'cucsCapabilityCatalogueFsmStageEntry':cucsCapabilityCatalogueFsmStageEntry,_N:cucsCapabilityCatalogueFsmStageInstanceId,'cucsCapabilityCatalogueFsmStageDn':cucsCapabilityCatalogueFsmStageDn,'cucsCapabilityCatalogueFsmStageRn':cucsCapabilityCatalogueFsmStageRn,'cucsCapabilityCatalogueFsmStageDescrData':cucsCapabilityCatalogueFsmStageDescrData,'cucsCapabilityCatalogueFsmStageLastUpdateTime':cucsCapabilityCatalogueFsmStageLastUpdateTime,'cucsCapabilityCatalogueFsmStageName':cucsCapabilityCatalogueFsmStageName,'cucsCapabilityCatalogueFsmStageOrder':cucsCapabilityCatalogueFsmStageOrder,'cucsCapabilityCatalogueFsmStageRetry':cucsCapabilityCatalogueFsmStageRetry,'cucsCapabilityCatalogueFsmStageStageStatus':cucsCapabilityCatalogueFsmStageStageStatus,'cucsCapabilityFeatureLimitsTable':cucsCapabilityFeatureLimitsTable,'cucsCapabilityFeatureLimitsEntry':cucsCapabilityFeatureLimitsEntry,_O:cucsCapabilityFeatureLimitsInstanceId,'cucsCapabilityFeatureLimitsDn':cucsCapabilityFeatureLimitsDn,'cucsCapabilityFeatureLimitsRn':cucsCapabilityFeatureLimitsRn,'cucsCapabilityFeatureLimitsDescr':cucsCapabilityFeatureLimitsDescr,'cucsCapabilityFeatureLimitsFeatureStatus':cucsCapabilityFeatureLimitsFeatureStatus,'cucsCapabilityFeatureLimitsLimit':cucsCapabilityFeatureLimitsLimit,'cucsCapabilityFeatureLimitsName':cucsCapabilityFeatureLimitsName,'cucsCapabilityFeatureLimitsPlatform':cucsCapabilityFeatureLimitsPlatform,'cucsCapabilityFeatureLimitsMinUCSMVersion':cucsCapabilityFeatureLimitsMinUCSMVersion,'cucsCapabilityMgmtExtensionFsmTable':cucsCapabilityMgmtExtensionFsmTable,'cucsCapabilityMgmtExtensionFsmEntry':cucsCapabilityMgmtExtensionFsmEntry,_P:cucsCapabilityMgmtExtensionFsmInstanceId,'cucsCapabilityMgmtExtensionFsmDn':cucsCapabilityMgmtExtensionFsmDn,'cucsCapabilityMgmtExtensionFsmRn':cucsCapabilityMgmtExtensionFsmRn,'cucsCapabilityMgmtExtensionFsmCompletionTime':cucsCapabilityMgmtExtensionFsmCompletionTime,'cucsCapabilityMgmtExtensionFsmCurrentFsm':cucsCapabilityMgmtExtensionFsmCurrentFsm,'cucsCapabilityMgmtExtensionFsmDescrData':cucsCapabilityMgmtExtensionFsmDescrData,'cucsCapabilityMgmtExtensionFsmFsmStatus':cucsCapabilityMgmtExtensionFsmFsmStatus,'cucsCapabilityMgmtExtensionFsmProgress':cucsCapabilityMgmtExtensionFsmProgress,'cucsCapabilityMgmtExtensionFsmRmtErrCode':cucsCapabilityMgmtExtensionFsmRmtErrCode,'cucsCapabilityMgmtExtensionFsmRmtErrDescr':cucsCapabilityMgmtExtensionFsmRmtErrDescr,'cucsCapabilityMgmtExtensionFsmRmtRslt':cucsCapabilityMgmtExtensionFsmRmtRslt,'cucsCapabilityMgmtExtensionFsmStageTable':cucsCapabilityMgmtExtensionFsmStageTable,'cucsCapabilityMgmtExtensionFsmStageEntry':cucsCapabilityMgmtExtensionFsmStageEntry,_Q:cucsCapabilityMgmtExtensionFsmStageInstanceId,'cucsCapabilityMgmtExtensionFsmStageDn':cucsCapabilityMgmtExtensionFsmStageDn,'cucsCapabilityMgmtExtensionFsmStageRn':cucsCapabilityMgmtExtensionFsmStageRn,'cucsCapabilityMgmtExtensionFsmStageDescrData':cucsCapabilityMgmtExtensionFsmStageDescrData,'cucsCapabilityMgmtExtensionFsmStageLastUpdateTime':cucsCapabilityMgmtExtensionFsmStageLastUpdateTime,'cucsCapabilityMgmtExtensionFsmStageName':cucsCapabilityMgmtExtensionFsmStageName,'cucsCapabilityMgmtExtensionFsmStageOrder':cucsCapabilityMgmtExtensionFsmStageOrder,'cucsCapabilityMgmtExtensionFsmStageRetry':cucsCapabilityMgmtExtensionFsmStageRetry,'cucsCapabilityMgmtExtensionFsmStageStageStatus':cucsCapabilityMgmtExtensionFsmStageStageStatus,'cucsCapabilityNetworkLimitsTable':cucsCapabilityNetworkLimitsTable,'cucsCapabilityNetworkLimitsEntry':cucsCapabilityNetworkLimitsEntry,_R:cucsCapabilityNetworkLimitsInstanceId,'cucsCapabilityNetworkLimitsDn':cucsCapabilityNetworkLimitsDn,'cucsCapabilityNetworkLimitsRn':cucsCapabilityNetworkLimitsRn,'cucsCapabilityStorageLimitsTable':cucsCapabilityStorageLimitsTable,'cucsCapabilityStorageLimitsEntry':cucsCapabilityStorageLimitsEntry,_S:cucsCapabilityStorageLimitsInstanceId,'cucsCapabilityStorageLimitsDn':cucsCapabilityStorageLimitsDn,'cucsCapabilityStorageLimitsRn':cucsCapabilityStorageLimitsRn,'cucsCapabilitySystemLimitsTable':cucsCapabilitySystemLimitsTable,'cucsCapabilitySystemLimitsEntry':cucsCapabilitySystemLimitsEntry,_T:cucsCapabilitySystemLimitsInstanceId,'cucsCapabilitySystemLimitsDn':cucsCapabilitySystemLimitsDn,'cucsCapabilitySystemLimitsRn':cucsCapabilitySystemLimitsRn,'cucsCapabilityUpdaterFsmTable':cucsCapabilityUpdaterFsmTable,'cucsCapabilityUpdaterFsmEntry':cucsCapabilityUpdaterFsmEntry,_U:cucsCapabilityUpdaterFsmInstanceId,'cucsCapabilityUpdaterFsmDn':cucsCapabilityUpdaterFsmDn,'cucsCapabilityUpdaterFsmRn':cucsCapabilityUpdaterFsmRn,'cucsCapabilityUpdaterFsmCompletionTime':cucsCapabilityUpdaterFsmCompletionTime,'cucsCapabilityUpdaterFsmCurrentFsm':cucsCapabilityUpdaterFsmCurrentFsm,'cucsCapabilityUpdaterFsmDescrData':cucsCapabilityUpdaterFsmDescrData,'cucsCapabilityUpdaterFsmFsmStatus':cucsCapabilityUpdaterFsmFsmStatus,'cucsCapabilityUpdaterFsmProgress':cucsCapabilityUpdaterFsmProgress,'cucsCapabilityUpdaterFsmRmtErrCode':cucsCapabilityUpdaterFsmRmtErrCode,'cucsCapabilityUpdaterFsmRmtErrDescr':cucsCapabilityUpdaterFsmRmtErrDescr,'cucsCapabilityUpdaterFsmRmtRslt':cucsCapabilityUpdaterFsmRmtRslt,'cucsCapabilityUpdaterFsmStageTable':cucsCapabilityUpdaterFsmStageTable,'cucsCapabilityUpdaterFsmStageEntry':cucsCapabilityUpdaterFsmStageEntry,_V:cucsCapabilityUpdaterFsmStageInstanceId,'cucsCapabilityUpdaterFsmStageDn':cucsCapabilityUpdaterFsmStageDn,'cucsCapabilityUpdaterFsmStageRn':cucsCapabilityUpdaterFsmStageRn,'cucsCapabilityUpdaterFsmStageDescrData':cucsCapabilityUpdaterFsmStageDescrData,'cucsCapabilityUpdaterFsmStageLastUpdateTime':cucsCapabilityUpdaterFsmStageLastUpdateTime,'cucsCapabilityUpdaterFsmStageName':cucsCapabilityUpdaterFsmStageName,'cucsCapabilityUpdaterFsmStageOrder':cucsCapabilityUpdaterFsmStageOrder,'cucsCapabilityUpdaterFsmStageRetry':cucsCapabilityUpdaterFsmStageRetry,'cucsCapabilityUpdaterFsmStageStageStatus':cucsCapabilityUpdaterFsmStageStageStatus})