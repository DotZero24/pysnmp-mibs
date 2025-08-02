_J='cucsEventRecordInstanceId'
_I='cucsEventPolicyInstanceId'
_H='cucsEventLogInstanceId'
_G='cucsEventInstInstanceId'
_F='cucsEventHolderInstanceId'
_E='cucsEventEpCtrlInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-EVENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsConditionActionIndicator,CucsConditionCause,CucsConditionCode,CucsConditionRule,CucsConditionSeverity,CucsConditionTag,CucsConditionType,CucsEventEpCtrlLevel,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsConditionActionIndicator','CucsConditionCause','CucsConditionCode','CucsConditionRule','CucsConditionSeverity','CucsConditionTag','CucsConditionType','CucsEventEpCtrlLevel','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsEventObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,17))
_CucsEventEpCtrlTable_Object=MibTable
cucsEventEpCtrlTable=_CucsEventEpCtrlTable_Object((1,3,6,1,4,1,9,9,719,1,17,1))
if mibBuilder.loadTexts:cucsEventEpCtrlTable.setStatus(_A)
_CucsEventEpCtrlEntry_Object=MibTableRow
cucsEventEpCtrlEntry=_CucsEventEpCtrlEntry_Object((1,3,6,1,4,1,9,9,719,1,17,1,1))
cucsEventEpCtrlEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsEventEpCtrlEntry.setStatus(_A)
_CucsEventEpCtrlInstanceId_Type=CucsManagedObjectId
_CucsEventEpCtrlInstanceId_Object=MibTableColumn
cucsEventEpCtrlInstanceId=_CucsEventEpCtrlInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,1,1,1),_CucsEventEpCtrlInstanceId_Type())
cucsEventEpCtrlInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventEpCtrlInstanceId.setStatus(_A)
_CucsEventEpCtrlDn_Type=CucsManagedObjectDn
_CucsEventEpCtrlDn_Object=MibTableColumn
cucsEventEpCtrlDn=_CucsEventEpCtrlDn_Object((1,3,6,1,4,1,9,9,719,1,17,1,1,2),_CucsEventEpCtrlDn_Type())
cucsEventEpCtrlDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventEpCtrlDn.setStatus(_A)
_CucsEventEpCtrlRn_Type=SnmpAdminString
_CucsEventEpCtrlRn_Object=MibTableColumn
cucsEventEpCtrlRn=_CucsEventEpCtrlRn_Object((1,3,6,1,4,1,9,9,719,1,17,1,1,3),_CucsEventEpCtrlRn_Type())
cucsEventEpCtrlRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventEpCtrlRn.setStatus(_A)
_CucsEventEpCtrlLevel_Type=CucsEventEpCtrlLevel
_CucsEventEpCtrlLevel_Object=MibTableColumn
cucsEventEpCtrlLevel=_CucsEventEpCtrlLevel_Object((1,3,6,1,4,1,9,9,719,1,17,1,1,4),_CucsEventEpCtrlLevel_Type())
cucsEventEpCtrlLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventEpCtrlLevel.setStatus(_A)
_CucsEventEpCtrlRevertTimeout_Type=TimeIntervalSec
_CucsEventEpCtrlRevertTimeout_Object=MibTableColumn
cucsEventEpCtrlRevertTimeout=_CucsEventEpCtrlRevertTimeout_Object((1,3,6,1,4,1,9,9,719,1,17,1,1,5),_CucsEventEpCtrlRevertTimeout_Type())
cucsEventEpCtrlRevertTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventEpCtrlRevertTimeout.setStatus(_A)
_CucsEventHolderTable_Object=MibTable
cucsEventHolderTable=_CucsEventHolderTable_Object((1,3,6,1,4,1,9,9,719,1,17,2))
if mibBuilder.loadTexts:cucsEventHolderTable.setStatus(_A)
_CucsEventHolderEntry_Object=MibTableRow
cucsEventHolderEntry=_CucsEventHolderEntry_Object((1,3,6,1,4,1,9,9,719,1,17,2,1))
cucsEventHolderEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsEventHolderEntry.setStatus(_A)
_CucsEventHolderInstanceId_Type=CucsManagedObjectId
_CucsEventHolderInstanceId_Object=MibTableColumn
cucsEventHolderInstanceId=_CucsEventHolderInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,2,1,1),_CucsEventHolderInstanceId_Type())
cucsEventHolderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventHolderInstanceId.setStatus(_A)
_CucsEventHolderDn_Type=CucsManagedObjectDn
_CucsEventHolderDn_Object=MibTableColumn
cucsEventHolderDn=_CucsEventHolderDn_Object((1,3,6,1,4,1,9,9,719,1,17,2,1,2),_CucsEventHolderDn_Type())
cucsEventHolderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventHolderDn.setStatus(_A)
_CucsEventHolderRn_Type=SnmpAdminString
_CucsEventHolderRn_Object=MibTableColumn
cucsEventHolderRn=_CucsEventHolderRn_Object((1,3,6,1,4,1,9,9,719,1,17,2,1,3),_CucsEventHolderRn_Type())
cucsEventHolderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventHolderRn.setStatus(_A)
_CucsEventHolderName_Type=SnmpAdminString
_CucsEventHolderName_Object=MibTableColumn
cucsEventHolderName=_CucsEventHolderName_Object((1,3,6,1,4,1,9,9,719,1,17,2,1,4),_CucsEventHolderName_Type())
cucsEventHolderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventHolderName.setStatus(_A)
_CucsEventInstTable_Object=MibTable
cucsEventInstTable=_CucsEventInstTable_Object((1,3,6,1,4,1,9,9,719,1,17,3))
if mibBuilder.loadTexts:cucsEventInstTable.setStatus(_A)
_CucsEventInstEntry_Object=MibTableRow
cucsEventInstEntry=_CucsEventInstEntry_Object((1,3,6,1,4,1,9,9,719,1,17,3,1))
cucsEventInstEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsEventInstEntry.setStatus(_A)
_CucsEventInstInstanceId_Type=CucsManagedObjectId
_CucsEventInstInstanceId_Object=MibTableColumn
cucsEventInstInstanceId=_CucsEventInstInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,1),_CucsEventInstInstanceId_Type())
cucsEventInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventInstInstanceId.setStatus(_A)
_CucsEventInstDn_Type=CucsManagedObjectDn
_CucsEventInstDn_Object=MibTableColumn
cucsEventInstDn=_CucsEventInstDn_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,2),_CucsEventInstDn_Type())
cucsEventInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstDn.setStatus(_A)
_CucsEventInstRn_Type=SnmpAdminString
_CucsEventInstRn_Object=MibTableColumn
cucsEventInstRn=_CucsEventInstRn_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,3),_CucsEventInstRn_Type())
cucsEventInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstRn.setStatus(_A)
_CucsEventInstCause_Type=CucsConditionCause
_CucsEventInstCause_Object=MibTableColumn
cucsEventInstCause=_CucsEventInstCause_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,4),_CucsEventInstCause_Type())
cucsEventInstCause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstCause.setStatus(_A)
_CucsEventInstChangeSet_Type=SnmpAdminString
_CucsEventInstChangeSet_Object=MibTableColumn
cucsEventInstChangeSet=_CucsEventInstChangeSet_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,5),_CucsEventInstChangeSet_Type())
cucsEventInstChangeSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstChangeSet.setStatus(_A)
_CucsEventInstCode_Type=CucsConditionCode
_CucsEventInstCode_Object=MibTableColumn
cucsEventInstCode=_CucsEventInstCode_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,6),_CucsEventInstCode_Type())
cucsEventInstCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstCode.setStatus(_A)
_CucsEventInstCreated_Type=DateAndTime
_CucsEventInstCreated_Object=MibTableColumn
cucsEventInstCreated=_CucsEventInstCreated_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,7),_CucsEventInstCreated_Type())
cucsEventInstCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstCreated.setStatus(_A)
_CucsEventInstDescr_Type=SnmpAdminString
_CucsEventInstDescr_Object=MibTableColumn
cucsEventInstDescr=_CucsEventInstDescr_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,8),_CucsEventInstDescr_Type())
cucsEventInstDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstDescr.setStatus(_A)
_CucsEventInstId_Type=Unsigned64
_CucsEventInstId_Object=MibTableColumn
cucsEventInstId=_CucsEventInstId_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,9),_CucsEventInstId_Type())
cucsEventInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstId.setStatus(_A)
_CucsEventInstRule_Type=CucsConditionRule
_CucsEventInstRule_Object=MibTableColumn
cucsEventInstRule=_CucsEventInstRule_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,10),_CucsEventInstRule_Type())
cucsEventInstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstRule.setStatus(_A)
_CucsEventInstSeverity_Type=CucsConditionSeverity
_CucsEventInstSeverity_Object=MibTableColumn
cucsEventInstSeverity=_CucsEventInstSeverity_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,11),_CucsEventInstSeverity_Type())
cucsEventInstSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstSeverity.setStatus(_A)
_CucsEventInstTags_Type=CucsConditionTag
_CucsEventInstTags_Object=MibTableColumn
cucsEventInstTags=_CucsEventInstTags_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,12),_CucsEventInstTags_Type())
cucsEventInstTags.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstTags.setStatus(_A)
_CucsEventInstType_Type=CucsConditionType
_CucsEventInstType_Object=MibTableColumn
cucsEventInstType=_CucsEventInstType_Object((1,3,6,1,4,1,9,9,719,1,17,3,1,13),_CucsEventInstType_Type())
cucsEventInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventInstType.setStatus(_A)
_CucsEventLogTable_Object=MibTable
cucsEventLogTable=_CucsEventLogTable_Object((1,3,6,1,4,1,9,9,719,1,17,4))
if mibBuilder.loadTexts:cucsEventLogTable.setStatus(_A)
_CucsEventLogEntry_Object=MibTableRow
cucsEventLogEntry=_CucsEventLogEntry_Object((1,3,6,1,4,1,9,9,719,1,17,4,1))
cucsEventLogEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsEventLogEntry.setStatus(_A)
_CucsEventLogInstanceId_Type=CucsManagedObjectId
_CucsEventLogInstanceId_Object=MibTableColumn
cucsEventLogInstanceId=_CucsEventLogInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,1),_CucsEventLogInstanceId_Type())
cucsEventLogInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventLogInstanceId.setStatus(_A)
_CucsEventLogDn_Type=CucsManagedObjectDn
_CucsEventLogDn_Object=MibTableColumn
cucsEventLogDn=_CucsEventLogDn_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,2),_CucsEventLogDn_Type())
cucsEventLogDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventLogDn.setStatus(_A)
_CucsEventLogRn_Type=SnmpAdminString
_CucsEventLogRn_Object=MibTableColumn
cucsEventLogRn=_CucsEventLogRn_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,3),_CucsEventLogRn_Type())
cucsEventLogRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventLogRn.setStatus(_A)
_CucsEventLogMaxSize_Type=Gauge32
_CucsEventLogMaxSize_Object=MibTableColumn
cucsEventLogMaxSize=_CucsEventLogMaxSize_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,4),_CucsEventLogMaxSize_Type())
cucsEventLogMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventLogMaxSize.setStatus(_A)
_CucsEventLogPurgeWindow_Type=Gauge32
_CucsEventLogPurgeWindow_Object=MibTableColumn
cucsEventLogPurgeWindow=_CucsEventLogPurgeWindow_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,5),_CucsEventLogPurgeWindow_Type())
cucsEventLogPurgeWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventLogPurgeWindow.setStatus(_A)
_CucsEventLogSize_Type=Gauge32
_CucsEventLogSize_Object=MibTableColumn
cucsEventLogSize=_CucsEventLogSize_Object((1,3,6,1,4,1,9,9,719,1,17,4,1,6),_CucsEventLogSize_Type())
cucsEventLogSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventLogSize.setStatus(_A)
_CucsEventPolicyTable_Object=MibTable
cucsEventPolicyTable=_CucsEventPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,17,5))
if mibBuilder.loadTexts:cucsEventPolicyTable.setStatus(_A)
_CucsEventPolicyEntry_Object=MibTableRow
cucsEventPolicyEntry=_CucsEventPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,17,5,1))
cucsEventPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsEventPolicyEntry.setStatus(_A)
_CucsEventPolicyInstanceId_Type=CucsManagedObjectId
_CucsEventPolicyInstanceId_Object=MibTableColumn
cucsEventPolicyInstanceId=_CucsEventPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,1),_CucsEventPolicyInstanceId_Type())
cucsEventPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventPolicyInstanceId.setStatus(_A)
_CucsEventPolicyDn_Type=CucsManagedObjectDn
_CucsEventPolicyDn_Object=MibTableColumn
cucsEventPolicyDn=_CucsEventPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,2),_CucsEventPolicyDn_Type())
cucsEventPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyDn.setStatus(_A)
_CucsEventPolicyRn_Type=SnmpAdminString
_CucsEventPolicyRn_Object=MibTableColumn
cucsEventPolicyRn=_CucsEventPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,3),_CucsEventPolicyRn_Type())
cucsEventPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyRn.setStatus(_A)
_CucsEventPolicyDescr_Type=SnmpAdminString
_CucsEventPolicyDescr_Object=MibTableColumn
cucsEventPolicyDescr=_CucsEventPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,4),_CucsEventPolicyDescr_Type())
cucsEventPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyDescr.setStatus(_A)
_CucsEventPolicyIntId_Type=SnmpAdminString
_CucsEventPolicyIntId_Object=MibTableColumn
cucsEventPolicyIntId=_CucsEventPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,5),_CucsEventPolicyIntId_Type())
cucsEventPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyIntId.setStatus(_A)
_CucsEventPolicyName_Type=SnmpAdminString
_CucsEventPolicyName_Object=MibTableColumn
cucsEventPolicyName=_CucsEventPolicyName_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,6),_CucsEventPolicyName_Type())
cucsEventPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyName.setStatus(_A)
_CucsEventPolicyRetentionInterval_Type=TimeIntervalSec
_CucsEventPolicyRetentionInterval_Object=MibTableColumn
cucsEventPolicyRetentionInterval=_CucsEventPolicyRetentionInterval_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,7),_CucsEventPolicyRetentionInterval_Type())
cucsEventPolicyRetentionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyRetentionInterval.setStatus(_A)
_CucsEventPolicySizeLimit_Type=Gauge32
_CucsEventPolicySizeLimit_Object=MibTableColumn
cucsEventPolicySizeLimit=_CucsEventPolicySizeLimit_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,8),_CucsEventPolicySizeLimit_Type())
cucsEventPolicySizeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicySizeLimit.setStatus(_A)
_CucsEventPolicyPolicyLevel_Type=Gauge32
_CucsEventPolicyPolicyLevel_Object=MibTableColumn
cucsEventPolicyPolicyLevel=_CucsEventPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,9),_CucsEventPolicyPolicyLevel_Type())
cucsEventPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyPolicyLevel.setStatus(_A)
_CucsEventPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsEventPolicyPolicyOwner_Object=MibTableColumn
cucsEventPolicyPolicyOwner=_CucsEventPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,10),_CucsEventPolicyPolicyOwner_Type())
cucsEventPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyPolicyOwner.setStatus(_A)
_CucsEventPolicyPinningExpirationInterval_Type=TimeIntervalSec
_CucsEventPolicyPinningExpirationInterval_Object=MibTableColumn
cucsEventPolicyPinningExpirationInterval=_CucsEventPolicyPinningExpirationInterval_Object((1,3,6,1,4,1,9,9,719,1,17,5,1,11),_CucsEventPolicyPinningExpirationInterval_Type())
cucsEventPolicyPinningExpirationInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventPolicyPinningExpirationInterval.setStatus(_A)
_CucsEventRecordTable_Object=MibTable
cucsEventRecordTable=_CucsEventRecordTable_Object((1,3,6,1,4,1,9,9,719,1,17,6))
if mibBuilder.loadTexts:cucsEventRecordTable.setStatus(_A)
_CucsEventRecordEntry_Object=MibTableRow
cucsEventRecordEntry=_CucsEventRecordEntry_Object((1,3,6,1,4,1,9,9,719,1,17,6,1))
cucsEventRecordEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsEventRecordEntry.setStatus(_A)
_CucsEventRecordInstanceId_Type=CucsManagedObjectId
_CucsEventRecordInstanceId_Object=MibTableColumn
cucsEventRecordInstanceId=_CucsEventRecordInstanceId_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,1),_CucsEventRecordInstanceId_Type())
cucsEventRecordInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsEventRecordInstanceId.setStatus(_A)
_CucsEventRecordDn_Type=CucsManagedObjectDn
_CucsEventRecordDn_Object=MibTableColumn
cucsEventRecordDn=_CucsEventRecordDn_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,2),_CucsEventRecordDn_Type())
cucsEventRecordDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordDn.setStatus(_A)
_CucsEventRecordRn_Type=SnmpAdminString
_CucsEventRecordRn_Object=MibTableColumn
cucsEventRecordRn=_CucsEventRecordRn_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,3),_CucsEventRecordRn_Type())
cucsEventRecordRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordRn.setStatus(_A)
_CucsEventRecordAffected_Type=SnmpAdminString
_CucsEventRecordAffected_Object=MibTableColumn
cucsEventRecordAffected=_CucsEventRecordAffected_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,4),_CucsEventRecordAffected_Type())
cucsEventRecordAffected.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordAffected.setStatus(_A)
_CucsEventRecordCause_Type=CucsConditionCause
_CucsEventRecordCause_Object=MibTableColumn
cucsEventRecordCause=_CucsEventRecordCause_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,5),_CucsEventRecordCause_Type())
cucsEventRecordCause.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordCause.setStatus(_A)
_CucsEventRecordChangeSet_Type=SnmpAdminString
_CucsEventRecordChangeSet_Object=MibTableColumn
cucsEventRecordChangeSet=_CucsEventRecordChangeSet_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,6),_CucsEventRecordChangeSet_Type())
cucsEventRecordChangeSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordChangeSet.setStatus(_A)
_CucsEventRecordCode_Type=CucsConditionCode
_CucsEventRecordCode_Object=MibTableColumn
cucsEventRecordCode=_CucsEventRecordCode_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,7),_CucsEventRecordCode_Type())
cucsEventRecordCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordCode.setStatus(_A)
_CucsEventRecordCreated_Type=DateAndTime
_CucsEventRecordCreated_Object=MibTableColumn
cucsEventRecordCreated=_CucsEventRecordCreated_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,8),_CucsEventRecordCreated_Type())
cucsEventRecordCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordCreated.setStatus(_A)
_CucsEventRecordDescr_Type=SnmpAdminString
_CucsEventRecordDescr_Object=MibTableColumn
cucsEventRecordDescr=_CucsEventRecordDescr_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,9),_CucsEventRecordDescr_Type())
cucsEventRecordDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordDescr.setStatus(_A)
_CucsEventRecordId_Type=Unsigned64
_CucsEventRecordId_Object=MibTableColumn
cucsEventRecordId=_CucsEventRecordId_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,10),_CucsEventRecordId_Type())
cucsEventRecordId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordId.setStatus(_A)
_CucsEventRecordInd_Type=Gauge32
_CucsEventRecordInd_Object=MibTableColumn
cucsEventRecordInd=_CucsEventRecordInd_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,11),_CucsEventRecordInd_Type())
cucsEventRecordInd.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordInd.setStatus(_A)
_CucsEventRecordSeverity_Type=CucsConditionSeverity
_CucsEventRecordSeverity_Object=MibTableColumn
cucsEventRecordSeverity=_CucsEventRecordSeverity_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,12),_CucsEventRecordSeverity_Type())
cucsEventRecordSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordSeverity.setStatus(_A)
_CucsEventRecordTrig_Type=Gauge32
_CucsEventRecordTrig_Object=MibTableColumn
cucsEventRecordTrig=_CucsEventRecordTrig_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,13),_CucsEventRecordTrig_Type())
cucsEventRecordTrig.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordTrig.setStatus(_A)
_CucsEventRecordTxId_Type=Unsigned64
_CucsEventRecordTxId_Object=MibTableColumn
cucsEventRecordTxId=_CucsEventRecordTxId_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,14),_CucsEventRecordTxId_Type())
cucsEventRecordTxId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordTxId.setStatus(_A)
_CucsEventRecordUser_Type=SnmpAdminString
_CucsEventRecordUser_Object=MibTableColumn
cucsEventRecordUser=_CucsEventRecordUser_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,15),_CucsEventRecordUser_Type())
cucsEventRecordUser.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordUser.setStatus(_A)
_CucsEventRecordSessionId_Type=SnmpAdminString
_CucsEventRecordSessionId_Object=MibTableColumn
cucsEventRecordSessionId=_CucsEventRecordSessionId_Object((1,3,6,1,4,1,9,9,719,1,17,6,1,16),_CucsEventRecordSessionId_Type())
cucsEventRecordSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsEventRecordSessionId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsEventObjects':cucsEventObjects,'cucsEventEpCtrlTable':cucsEventEpCtrlTable,'cucsEventEpCtrlEntry':cucsEventEpCtrlEntry,_E:cucsEventEpCtrlInstanceId,'cucsEventEpCtrlDn':cucsEventEpCtrlDn,'cucsEventEpCtrlRn':cucsEventEpCtrlRn,'cucsEventEpCtrlLevel':cucsEventEpCtrlLevel,'cucsEventEpCtrlRevertTimeout':cucsEventEpCtrlRevertTimeout,'cucsEventHolderTable':cucsEventHolderTable,'cucsEventHolderEntry':cucsEventHolderEntry,_F:cucsEventHolderInstanceId,'cucsEventHolderDn':cucsEventHolderDn,'cucsEventHolderRn':cucsEventHolderRn,'cucsEventHolderName':cucsEventHolderName,'cucsEventInstTable':cucsEventInstTable,'cucsEventInstEntry':cucsEventInstEntry,_G:cucsEventInstInstanceId,'cucsEventInstDn':cucsEventInstDn,'cucsEventInstRn':cucsEventInstRn,'cucsEventInstCause':cucsEventInstCause,'cucsEventInstChangeSet':cucsEventInstChangeSet,'cucsEventInstCode':cucsEventInstCode,'cucsEventInstCreated':cucsEventInstCreated,'cucsEventInstDescr':cucsEventInstDescr,'cucsEventInstId':cucsEventInstId,'cucsEventInstRule':cucsEventInstRule,'cucsEventInstSeverity':cucsEventInstSeverity,'cucsEventInstTags':cucsEventInstTags,'cucsEventInstType':cucsEventInstType,'cucsEventLogTable':cucsEventLogTable,'cucsEventLogEntry':cucsEventLogEntry,_H:cucsEventLogInstanceId,'cucsEventLogDn':cucsEventLogDn,'cucsEventLogRn':cucsEventLogRn,'cucsEventLogMaxSize':cucsEventLogMaxSize,'cucsEventLogPurgeWindow':cucsEventLogPurgeWindow,'cucsEventLogSize':cucsEventLogSize,'cucsEventPolicyTable':cucsEventPolicyTable,'cucsEventPolicyEntry':cucsEventPolicyEntry,_I:cucsEventPolicyInstanceId,'cucsEventPolicyDn':cucsEventPolicyDn,'cucsEventPolicyRn':cucsEventPolicyRn,'cucsEventPolicyDescr':cucsEventPolicyDescr,'cucsEventPolicyIntId':cucsEventPolicyIntId,'cucsEventPolicyName':cucsEventPolicyName,'cucsEventPolicyRetentionInterval':cucsEventPolicyRetentionInterval,'cucsEventPolicySizeLimit':cucsEventPolicySizeLimit,'cucsEventPolicyPolicyLevel':cucsEventPolicyPolicyLevel,'cucsEventPolicyPolicyOwner':cucsEventPolicyPolicyOwner,'cucsEventPolicyPinningExpirationInterval':cucsEventPolicyPinningExpirationInterval,'cucsEventRecordTable':cucsEventRecordTable,'cucsEventRecordEntry':cucsEventRecordEntry,_J:cucsEventRecordInstanceId,'cucsEventRecordDn':cucsEventRecordDn,'cucsEventRecordRn':cucsEventRecordRn,'cucsEventRecordAffected':cucsEventRecordAffected,'cucsEventRecordCause':cucsEventRecordCause,'cucsEventRecordChangeSet':cucsEventRecordChangeSet,'cucsEventRecordCode':cucsEventRecordCode,'cucsEventRecordCreated':cucsEventRecordCreated,'cucsEventRecordDescr':cucsEventRecordDescr,'cucsEventRecordId':cucsEventRecordId,'cucsEventRecordInd':cucsEventRecordInd,'cucsEventRecordSeverity':cucsEventRecordSeverity,'cucsEventRecordTrig':cucsEventRecordTrig,'cucsEventRecordTxId':cucsEventRecordTxId,'cucsEventRecordUser':cucsEventRecordUser,'cucsEventRecordSessionId':cucsEventRecordSessionId})