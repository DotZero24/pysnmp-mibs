_L='cfprFaultSuppressTaskInstanceId'
_K='cfprFaultSuppressPolicyItemInstanceId'
_J='cfprFaultSuppressPolicyInstanceId'
_I='cfprFaultPolicyInstanceId'
_H='cfprFaultLocalTypedHolderInstanceId'
_G='cfprFaultHolderInstanceId'
_F='cfprFaultAffectedClassInstanceId'
_E='cfprFaultInstInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-FAULT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprConditionAckAction,CfprConditionCause,CfprConditionCode,CfprConditionLifecycle,CfprConditionRule,CfprConditionSeverity,CfprConditionTag,CfprConditionType,CfprFaultBasePolicyClearAction,CfprFaultBasePolicySoakingSeverity,CfprMoMoClassId,CfprPolicyPolicyOwner,CfprTrigAdminState,CfprTrigTrigOperState=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprConditionAckAction','CfprConditionCause','CfprConditionCode','CfprConditionLifecycle','CfprConditionRule','CfprConditionSeverity','CfprConditionTag','CfprConditionType','CfprFaultBasePolicyClearAction','CfprFaultBasePolicySoakingSeverity','CfprMoMoClassId','CfprPolicyPolicyOwner','CfprTrigAdminState','CfprTrigTrigOperState')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprFaultObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,1))
_CfprFaultInstTable_Object=MibTable
cfprFaultInstTable=_CfprFaultInstTable_Object((1,3,6,1,4,1,9,9,826,1,1,1))
if mibBuilder.loadTexts:cfprFaultInstTable.setStatus(_A)
_CfprFaultInstEntry_Object=MibTableRow
cfprFaultInstEntry=_CfprFaultInstEntry_Object((1,3,6,1,4,1,9,9,826,1,1,1,1))
cfprFaultInstEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprFaultInstEntry.setStatus(_A)
_CfprFaultInstInstanceId_Type=CfprManagedObjectId
_CfprFaultInstInstanceId_Object=MibTableColumn
cfprFaultInstInstanceId=_CfprFaultInstInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,1),_CfprFaultInstInstanceId_Type())
cfprFaultInstInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultInstInstanceId.setStatus(_A)
_CfprFaultInstDn_Type=CfprManagedObjectDn
_CfprFaultInstDn_Object=MibTableColumn
cfprFaultInstDn=_CfprFaultInstDn_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,2),_CfprFaultInstDn_Type())
cfprFaultInstDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstDn.setStatus(_A)
_CfprFaultInstRn_Type=SnmpAdminString
_CfprFaultInstRn_Object=MibTableColumn
cfprFaultInstRn=_CfprFaultInstRn_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,3),_CfprFaultInstRn_Type())
cfprFaultInstRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstRn.setStatus(_A)
_CfprFaultInstAffectedObjectId_Type=RowPointer
_CfprFaultInstAffectedObjectId_Object=MibTableColumn
cfprFaultInstAffectedObjectId=_CfprFaultInstAffectedObjectId_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,4),_CfprFaultInstAffectedObjectId_Type())
cfprFaultInstAffectedObjectId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstAffectedObjectId.setStatus(_A)
_CfprFaultInstAffectedObjectDn_Type=CfprManagedObjectDn
_CfprFaultInstAffectedObjectDn_Object=MibTableColumn
cfprFaultInstAffectedObjectDn=_CfprFaultInstAffectedObjectDn_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,5),_CfprFaultInstAffectedObjectDn_Type())
cfprFaultInstAffectedObjectDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstAffectedObjectDn.setStatus(_A)
_CfprFaultInstAck_Type=TruthValue
_CfprFaultInstAck_Object=MibTableColumn
cfprFaultInstAck=_CfprFaultInstAck_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,6),_CfprFaultInstAck_Type())
cfprFaultInstAck.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstAck.setStatus(_A)
_CfprFaultInstCause_Type=CfprConditionCause
_CfprFaultInstCause_Object=MibTableColumn
cfprFaultInstCause=_CfprFaultInstCause_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,7),_CfprFaultInstCause_Type())
cfprFaultInstCause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstCause.setStatus(_A)
_CfprFaultInstChangeSet_Type=SnmpAdminString
_CfprFaultInstChangeSet_Object=MibTableColumn
cfprFaultInstChangeSet=_CfprFaultInstChangeSet_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,8),_CfprFaultInstChangeSet_Type())
cfprFaultInstChangeSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstChangeSet.setStatus(_A)
_CfprFaultInstCode_Type=CfprConditionCode
_CfprFaultInstCode_Object=MibTableColumn
cfprFaultInstCode=_CfprFaultInstCode_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,9),_CfprFaultInstCode_Type())
cfprFaultInstCode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstCode.setStatus(_A)
_CfprFaultInstCreated_Type=DateAndTime
_CfprFaultInstCreated_Object=MibTableColumn
cfprFaultInstCreated=_CfprFaultInstCreated_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,10),_CfprFaultInstCreated_Type())
cfprFaultInstCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstCreated.setStatus(_A)
_CfprFaultInstDescr_Type=SnmpAdminString
_CfprFaultInstDescr_Object=MibTableColumn
cfprFaultInstDescr=_CfprFaultInstDescr_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,11),_CfprFaultInstDescr_Type())
cfprFaultInstDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstDescr.setStatus(_A)
_CfprFaultInstHighestSeverity_Type=CfprConditionSeverity
_CfprFaultInstHighestSeverity_Object=MibTableColumn
cfprFaultInstHighestSeverity=_CfprFaultInstHighestSeverity_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,12),_CfprFaultInstHighestSeverity_Type())
cfprFaultInstHighestSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstHighestSeverity.setStatus(_A)
_CfprFaultInstId_Type=Unsigned64
_CfprFaultInstId_Object=MibTableColumn
cfprFaultInstId=_CfprFaultInstId_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,13),_CfprFaultInstId_Type())
cfprFaultInstId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstId.setStatus(_A)
_CfprFaultInstLastTransition_Type=DateAndTime
_CfprFaultInstLastTransition_Object=MibTableColumn
cfprFaultInstLastTransition=_CfprFaultInstLastTransition_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,14),_CfprFaultInstLastTransition_Type())
cfprFaultInstLastTransition.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstLastTransition.setStatus(_A)
_CfprFaultInstLc_Type=CfprConditionLifecycle
_CfprFaultInstLc_Object=MibTableColumn
cfprFaultInstLc=_CfprFaultInstLc_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,15),_CfprFaultInstLc_Type())
cfprFaultInstLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstLc.setStatus(_A)
_CfprFaultInstOccur_Type=Gauge32
_CfprFaultInstOccur_Object=MibTableColumn
cfprFaultInstOccur=_CfprFaultInstOccur_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,16),_CfprFaultInstOccur_Type())
cfprFaultInstOccur.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstOccur.setStatus(_A)
_CfprFaultInstOrigSeverity_Type=CfprConditionSeverity
_CfprFaultInstOrigSeverity_Object=MibTableColumn
cfprFaultInstOrigSeverity=_CfprFaultInstOrigSeverity_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,17),_CfprFaultInstOrigSeverity_Type())
cfprFaultInstOrigSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstOrigSeverity.setStatus(_A)
_CfprFaultInstPrevSeverity_Type=CfprConditionSeverity
_CfprFaultInstPrevSeverity_Object=MibTableColumn
cfprFaultInstPrevSeverity=_CfprFaultInstPrevSeverity_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,18),_CfprFaultInstPrevSeverity_Type())
cfprFaultInstPrevSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstPrevSeverity.setStatus(_A)
_CfprFaultInstRule_Type=CfprConditionRule
_CfprFaultInstRule_Object=MibTableColumn
cfprFaultInstRule=_CfprFaultInstRule_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,19),_CfprFaultInstRule_Type())
cfprFaultInstRule.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstRule.setStatus(_A)
_CfprFaultInstSeverity_Type=CfprConditionSeverity
_CfprFaultInstSeverity_Object=MibTableColumn
cfprFaultInstSeverity=_CfprFaultInstSeverity_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,20),_CfprFaultInstSeverity_Type())
cfprFaultInstSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstSeverity.setStatus(_A)
_CfprFaultInstTags_Type=CfprConditionTag
_CfprFaultInstTags_Object=MibTableColumn
cfprFaultInstTags=_CfprFaultInstTags_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,21),_CfprFaultInstTags_Type())
cfprFaultInstTags.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstTags.setStatus(_A)
_CfprFaultInstType_Type=CfprConditionType
_CfprFaultInstType_Object=MibTableColumn
cfprFaultInstType=_CfprFaultInstType_Object((1,3,6,1,4,1,9,9,826,1,1,1,1,22),_CfprFaultInstType_Type())
cfprFaultInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultInstType.setStatus(_A)
_CfprFaultAffectedClassTable_Object=MibTable
cfprFaultAffectedClassTable=_CfprFaultAffectedClassTable_Object((1,3,6,1,4,1,9,9,826,1,1,2))
if mibBuilder.loadTexts:cfprFaultAffectedClassTable.setStatus(_A)
_CfprFaultAffectedClassEntry_Object=MibTableRow
cfprFaultAffectedClassEntry=_CfprFaultAffectedClassEntry_Object((1,3,6,1,4,1,9,9,826,1,1,2,1))
cfprFaultAffectedClassEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprFaultAffectedClassEntry.setStatus(_A)
_CfprFaultAffectedClassInstanceId_Type=CfprManagedObjectId
_CfprFaultAffectedClassInstanceId_Object=MibTableColumn
cfprFaultAffectedClassInstanceId=_CfprFaultAffectedClassInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,2,1,1),_CfprFaultAffectedClassInstanceId_Type())
cfprFaultAffectedClassInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultAffectedClassInstanceId.setStatus(_A)
_CfprFaultAffectedClassDn_Type=CfprManagedObjectDn
_CfprFaultAffectedClassDn_Object=MibTableColumn
cfprFaultAffectedClassDn=_CfprFaultAffectedClassDn_Object((1,3,6,1,4,1,9,9,826,1,1,2,1,2),_CfprFaultAffectedClassDn_Type())
cfprFaultAffectedClassDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultAffectedClassDn.setStatus(_A)
_CfprFaultAffectedClassRn_Type=SnmpAdminString
_CfprFaultAffectedClassRn_Object=MibTableColumn
cfprFaultAffectedClassRn=_CfprFaultAffectedClassRn_Object((1,3,6,1,4,1,9,9,826,1,1,2,1,3),_CfprFaultAffectedClassRn_Type())
cfprFaultAffectedClassRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultAffectedClassRn.setStatus(_A)
_CfprFaultAffectedClassMoClassId_Type=CfprMoMoClassId
_CfprFaultAffectedClassMoClassId_Object=MibTableColumn
cfprFaultAffectedClassMoClassId=_CfprFaultAffectedClassMoClassId_Object((1,3,6,1,4,1,9,9,826,1,1,2,1,4),_CfprFaultAffectedClassMoClassId_Type())
cfprFaultAffectedClassMoClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultAffectedClassMoClassId.setStatus(_A)
_CfprFaultHolderTable_Object=MibTable
cfprFaultHolderTable=_CfprFaultHolderTable_Object((1,3,6,1,4,1,9,9,826,1,1,3))
if mibBuilder.loadTexts:cfprFaultHolderTable.setStatus(_A)
_CfprFaultHolderEntry_Object=MibTableRow
cfprFaultHolderEntry=_CfprFaultHolderEntry_Object((1,3,6,1,4,1,9,9,826,1,1,3,1))
cfprFaultHolderEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprFaultHolderEntry.setStatus(_A)
_CfprFaultHolderInstanceId_Type=CfprManagedObjectId
_CfprFaultHolderInstanceId_Object=MibTableColumn
cfprFaultHolderInstanceId=_CfprFaultHolderInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,3,1,1),_CfprFaultHolderInstanceId_Type())
cfprFaultHolderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultHolderInstanceId.setStatus(_A)
_CfprFaultHolderDn_Type=CfprManagedObjectDn
_CfprFaultHolderDn_Object=MibTableColumn
cfprFaultHolderDn=_CfprFaultHolderDn_Object((1,3,6,1,4,1,9,9,826,1,1,3,1,2),_CfprFaultHolderDn_Type())
cfprFaultHolderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultHolderDn.setStatus(_A)
_CfprFaultHolderRn_Type=SnmpAdminString
_CfprFaultHolderRn_Object=MibTableColumn
cfprFaultHolderRn=_CfprFaultHolderRn_Object((1,3,6,1,4,1,9,9,826,1,1,3,1,3),_CfprFaultHolderRn_Type())
cfprFaultHolderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultHolderRn.setStatus(_A)
_CfprFaultHolderName_Type=SnmpAdminString
_CfprFaultHolderName_Object=MibTableColumn
cfprFaultHolderName=_CfprFaultHolderName_Object((1,3,6,1,4,1,9,9,826,1,1,3,1,4),_CfprFaultHolderName_Type())
cfprFaultHolderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultHolderName.setStatus(_A)
_CfprFaultHolderTotalFaults_Type=Unsigned64
_CfprFaultHolderTotalFaults_Object=MibTableColumn
cfprFaultHolderTotalFaults=_CfprFaultHolderTotalFaults_Object((1,3,6,1,4,1,9,9,826,1,1,3,1,5),_CfprFaultHolderTotalFaults_Type())
cfprFaultHolderTotalFaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultHolderTotalFaults.setStatus(_A)
_CfprFaultLocalTypedHolderTable_Object=MibTable
cfprFaultLocalTypedHolderTable=_CfprFaultLocalTypedHolderTable_Object((1,3,6,1,4,1,9,9,826,1,1,4))
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderTable.setStatus(_A)
_CfprFaultLocalTypedHolderEntry_Object=MibTableRow
cfprFaultLocalTypedHolderEntry=_CfprFaultLocalTypedHolderEntry_Object((1,3,6,1,4,1,9,9,826,1,1,4,1))
cfprFaultLocalTypedHolderEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderEntry.setStatus(_A)
_CfprFaultLocalTypedHolderInstanceId_Type=CfprManagedObjectId
_CfprFaultLocalTypedHolderInstanceId_Object=MibTableColumn
cfprFaultLocalTypedHolderInstanceId=_CfprFaultLocalTypedHolderInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,1),_CfprFaultLocalTypedHolderInstanceId_Type())
cfprFaultLocalTypedHolderInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderInstanceId.setStatus(_A)
_CfprFaultLocalTypedHolderDn_Type=CfprManagedObjectDn
_CfprFaultLocalTypedHolderDn_Object=MibTableColumn
cfprFaultLocalTypedHolderDn=_CfprFaultLocalTypedHolderDn_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,2),_CfprFaultLocalTypedHolderDn_Type())
cfprFaultLocalTypedHolderDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderDn.setStatus(_A)
_CfprFaultLocalTypedHolderRn_Type=SnmpAdminString
_CfprFaultLocalTypedHolderRn_Object=MibTableColumn
cfprFaultLocalTypedHolderRn=_CfprFaultLocalTypedHolderRn_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,3),_CfprFaultLocalTypedHolderRn_Type())
cfprFaultLocalTypedHolderRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderRn.setStatus(_A)
_CfprFaultLocalTypedHolderName_Type=SnmpAdminString
_CfprFaultLocalTypedHolderName_Object=MibTableColumn
cfprFaultLocalTypedHolderName=_CfprFaultLocalTypedHolderName_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,4),_CfprFaultLocalTypedHolderName_Type())
cfprFaultLocalTypedHolderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderName.setStatus(_A)
_CfprFaultLocalTypedHolderTotalFaults_Type=Unsigned64
_CfprFaultLocalTypedHolderTotalFaults_Object=MibTableColumn
cfprFaultLocalTypedHolderTotalFaults=_CfprFaultLocalTypedHolderTotalFaults_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,5),_CfprFaultLocalTypedHolderTotalFaults_Type())
cfprFaultLocalTypedHolderTotalFaults.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderTotalFaults.setStatus(_A)
_CfprFaultLocalTypedHolderType_Type=CfprConditionType
_CfprFaultLocalTypedHolderType_Object=MibTableColumn
cfprFaultLocalTypedHolderType=_CfprFaultLocalTypedHolderType_Object((1,3,6,1,4,1,9,9,826,1,1,4,1,6),_CfprFaultLocalTypedHolderType_Type())
cfprFaultLocalTypedHolderType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultLocalTypedHolderType.setStatus(_A)
_CfprFaultPolicyTable_Object=MibTable
cfprFaultPolicyTable=_CfprFaultPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,1,5))
if mibBuilder.loadTexts:cfprFaultPolicyTable.setStatus(_A)
_CfprFaultPolicyEntry_Object=MibTableRow
cfprFaultPolicyEntry=_CfprFaultPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,1,5,1))
cfprFaultPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprFaultPolicyEntry.setStatus(_A)
_CfprFaultPolicyInstanceId_Type=CfprManagedObjectId
_CfprFaultPolicyInstanceId_Object=MibTableColumn
cfprFaultPolicyInstanceId=_CfprFaultPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,1),_CfprFaultPolicyInstanceId_Type())
cfprFaultPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultPolicyInstanceId.setStatus(_A)
_CfprFaultPolicyDn_Type=CfprManagedObjectDn
_CfprFaultPolicyDn_Object=MibTableColumn
cfprFaultPolicyDn=_CfprFaultPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,2),_CfprFaultPolicyDn_Type())
cfprFaultPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyDn.setStatus(_A)
_CfprFaultPolicyRn_Type=SnmpAdminString
_CfprFaultPolicyRn_Object=MibTableColumn
cfprFaultPolicyRn=_CfprFaultPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,3),_CfprFaultPolicyRn_Type())
cfprFaultPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyRn.setStatus(_A)
_CfprFaultPolicyAckAction_Type=CfprConditionAckAction
_CfprFaultPolicyAckAction_Object=MibTableColumn
cfprFaultPolicyAckAction=_CfprFaultPolicyAckAction_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,4),_CfprFaultPolicyAckAction_Type())
cfprFaultPolicyAckAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyAckAction.setStatus(_A)
_CfprFaultPolicyClearAction_Type=CfprFaultBasePolicyClearAction
_CfprFaultPolicyClearAction_Object=MibTableColumn
cfprFaultPolicyClearAction=_CfprFaultPolicyClearAction_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,5),_CfprFaultPolicyClearAction_Type())
cfprFaultPolicyClearAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyClearAction.setStatus(_A)
_CfprFaultPolicyClearInterval_Type=TimeIntervalSec
_CfprFaultPolicyClearInterval_Object=MibTableColumn
cfprFaultPolicyClearInterval=_CfprFaultPolicyClearInterval_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,6),_CfprFaultPolicyClearInterval_Type())
cfprFaultPolicyClearInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyClearInterval.setStatus(_A)
_CfprFaultPolicyDescr_Type=SnmpAdminString
_CfprFaultPolicyDescr_Object=MibTableColumn
cfprFaultPolicyDescr=_CfprFaultPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,7),_CfprFaultPolicyDescr_Type())
cfprFaultPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyDescr.setStatus(_A)
_CfprFaultPolicyFlapInterval_Type=Unsigned64
_CfprFaultPolicyFlapInterval_Object=MibTableColumn
cfprFaultPolicyFlapInterval=_CfprFaultPolicyFlapInterval_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,8),_CfprFaultPolicyFlapInterval_Type())
cfprFaultPolicyFlapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyFlapInterval.setStatus(_A)
_CfprFaultPolicyIntId_Type=SnmpAdminString
_CfprFaultPolicyIntId_Object=MibTableColumn
cfprFaultPolicyIntId=_CfprFaultPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,9),_CfprFaultPolicyIntId_Type())
cfprFaultPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyIntId.setStatus(_A)
_CfprFaultPolicyName_Type=SnmpAdminString
_CfprFaultPolicyName_Object=MibTableColumn
cfprFaultPolicyName=_CfprFaultPolicyName_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,10),_CfprFaultPolicyName_Type())
cfprFaultPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyName.setStatus(_A)
_CfprFaultPolicyPolicyLevel_Type=Gauge32
_CfprFaultPolicyPolicyLevel_Object=MibTableColumn
cfprFaultPolicyPolicyLevel=_CfprFaultPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,11),_CfprFaultPolicyPolicyLevel_Type())
cfprFaultPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyPolicyLevel.setStatus(_A)
_CfprFaultPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprFaultPolicyPolicyOwner_Object=MibTableColumn
cfprFaultPolicyPolicyOwner=_CfprFaultPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,12),_CfprFaultPolicyPolicyOwner_Type())
cfprFaultPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyPolicyOwner.setStatus(_A)
_CfprFaultPolicyRetentionInterval_Type=TimeIntervalSec
_CfprFaultPolicyRetentionInterval_Object=MibTableColumn
cfprFaultPolicyRetentionInterval=_CfprFaultPolicyRetentionInterval_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,13),_CfprFaultPolicyRetentionInterval_Type())
cfprFaultPolicyRetentionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicyRetentionInterval.setStatus(_A)
_CfprFaultPolicySizeLimit_Type=Gauge32
_CfprFaultPolicySizeLimit_Object=MibTableColumn
cfprFaultPolicySizeLimit=_CfprFaultPolicySizeLimit_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,14),_CfprFaultPolicySizeLimit_Type())
cfprFaultPolicySizeLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicySizeLimit.setStatus(_A)
_CfprFaultPolicySoakInterval_Type=TimeIntervalSec
_CfprFaultPolicySoakInterval_Object=MibTableColumn
cfprFaultPolicySoakInterval=_CfprFaultPolicySoakInterval_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,15),_CfprFaultPolicySoakInterval_Type())
cfprFaultPolicySoakInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicySoakInterval.setStatus(_A)
_CfprFaultPolicySoakingSeverity_Type=CfprFaultBasePolicySoakingSeverity
_CfprFaultPolicySoakingSeverity_Object=MibTableColumn
cfprFaultPolicySoakingSeverity=_CfprFaultPolicySoakingSeverity_Object((1,3,6,1,4,1,9,9,826,1,1,5,1,16),_CfprFaultPolicySoakingSeverity_Type())
cfprFaultPolicySoakingSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultPolicySoakingSeverity.setStatus(_A)
_CfprFaultSuppressPolicyTable_Object=MibTable
cfprFaultSuppressPolicyTable=_CfprFaultSuppressPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,1,6))
if mibBuilder.loadTexts:cfprFaultSuppressPolicyTable.setStatus(_A)
_CfprFaultSuppressPolicyEntry_Object=MibTableRow
cfprFaultSuppressPolicyEntry=_CfprFaultSuppressPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,1,6,1))
cfprFaultSuppressPolicyEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprFaultSuppressPolicyEntry.setStatus(_A)
_CfprFaultSuppressPolicyInstanceId_Type=CfprManagedObjectId
_CfprFaultSuppressPolicyInstanceId_Object=MibTableColumn
cfprFaultSuppressPolicyInstanceId=_CfprFaultSuppressPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,1),_CfprFaultSuppressPolicyInstanceId_Type())
cfprFaultSuppressPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyInstanceId.setStatus(_A)
_CfprFaultSuppressPolicyDn_Type=CfprManagedObjectDn
_CfprFaultSuppressPolicyDn_Object=MibTableColumn
cfprFaultSuppressPolicyDn=_CfprFaultSuppressPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,2),_CfprFaultSuppressPolicyDn_Type())
cfprFaultSuppressPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyDn.setStatus(_A)
_CfprFaultSuppressPolicyRn_Type=SnmpAdminString
_CfprFaultSuppressPolicyRn_Object=MibTableColumn
cfprFaultSuppressPolicyRn=_CfprFaultSuppressPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,3),_CfprFaultSuppressPolicyRn_Type())
cfprFaultSuppressPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyRn.setStatus(_A)
_CfprFaultSuppressPolicyDescr_Type=SnmpAdminString
_CfprFaultSuppressPolicyDescr_Object=MibTableColumn
cfprFaultSuppressPolicyDescr=_CfprFaultSuppressPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,4),_CfprFaultSuppressPolicyDescr_Type())
cfprFaultSuppressPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyDescr.setStatus(_A)
_CfprFaultSuppressPolicyIntId_Type=SnmpAdminString
_CfprFaultSuppressPolicyIntId_Object=MibTableColumn
cfprFaultSuppressPolicyIntId=_CfprFaultSuppressPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,5),_CfprFaultSuppressPolicyIntId_Type())
cfprFaultSuppressPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyIntId.setStatus(_A)
_CfprFaultSuppressPolicyName_Type=SnmpAdminString
_CfprFaultSuppressPolicyName_Object=MibTableColumn
cfprFaultSuppressPolicyName=_CfprFaultSuppressPolicyName_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,6),_CfprFaultSuppressPolicyName_Type())
cfprFaultSuppressPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyName.setStatus(_A)
_CfprFaultSuppressPolicyPolicyLevel_Type=Gauge32
_CfprFaultSuppressPolicyPolicyLevel_Object=MibTableColumn
cfprFaultSuppressPolicyPolicyLevel=_CfprFaultSuppressPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,7),_CfprFaultSuppressPolicyPolicyLevel_Type())
cfprFaultSuppressPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyPolicyLevel.setStatus(_A)
_CfprFaultSuppressPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprFaultSuppressPolicyPolicyOwner_Object=MibTableColumn
cfprFaultSuppressPolicyPolicyOwner=_CfprFaultSuppressPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,1,6,1,8),_CfprFaultSuppressPolicyPolicyOwner_Type())
cfprFaultSuppressPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyPolicyOwner.setStatus(_A)
_CfprFaultSuppressPolicyItemTable_Object=MibTable
cfprFaultSuppressPolicyItemTable=_CfprFaultSuppressPolicyItemTable_Object((1,3,6,1,4,1,9,9,826,1,1,7))
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemTable.setStatus(_A)
_CfprFaultSuppressPolicyItemEntry_Object=MibTableRow
cfprFaultSuppressPolicyItemEntry=_CfprFaultSuppressPolicyItemEntry_Object((1,3,6,1,4,1,9,9,826,1,1,7,1))
cfprFaultSuppressPolicyItemEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemEntry.setStatus(_A)
_CfprFaultSuppressPolicyItemInstanceId_Type=CfprManagedObjectId
_CfprFaultSuppressPolicyItemInstanceId_Object=MibTableColumn
cfprFaultSuppressPolicyItemInstanceId=_CfprFaultSuppressPolicyItemInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,1),_CfprFaultSuppressPolicyItemInstanceId_Type())
cfprFaultSuppressPolicyItemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemInstanceId.setStatus(_A)
_CfprFaultSuppressPolicyItemDn_Type=CfprManagedObjectDn
_CfprFaultSuppressPolicyItemDn_Object=MibTableColumn
cfprFaultSuppressPolicyItemDn=_CfprFaultSuppressPolicyItemDn_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,2),_CfprFaultSuppressPolicyItemDn_Type())
cfprFaultSuppressPolicyItemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemDn.setStatus(_A)
_CfprFaultSuppressPolicyItemRn_Type=SnmpAdminString
_CfprFaultSuppressPolicyItemRn_Object=MibTableColumn
cfprFaultSuppressPolicyItemRn=_CfprFaultSuppressPolicyItemRn_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,3),_CfprFaultSuppressPolicyItemRn_Type())
cfprFaultSuppressPolicyItemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemRn.setStatus(_A)
_CfprFaultSuppressPolicyItemCause_Type=CfprConditionCause
_CfprFaultSuppressPolicyItemCause_Object=MibTableColumn
cfprFaultSuppressPolicyItemCause=_CfprFaultSuppressPolicyItemCause_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,4),_CfprFaultSuppressPolicyItemCause_Type())
cfprFaultSuppressPolicyItemCause.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemCause.setStatus(_A)
_CfprFaultSuppressPolicyItemDescr_Type=SnmpAdminString
_CfprFaultSuppressPolicyItemDescr_Object=MibTableColumn
cfprFaultSuppressPolicyItemDescr=_CfprFaultSuppressPolicyItemDescr_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,5),_CfprFaultSuppressPolicyItemDescr_Type())
cfprFaultSuppressPolicyItemDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemDescr.setStatus(_A)
_CfprFaultSuppressPolicyItemType_Type=CfprConditionType
_CfprFaultSuppressPolicyItemType_Object=MibTableColumn
cfprFaultSuppressPolicyItemType=_CfprFaultSuppressPolicyItemType_Object((1,3,6,1,4,1,9,9,826,1,1,7,1,6),_CfprFaultSuppressPolicyItemType_Type())
cfprFaultSuppressPolicyItemType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressPolicyItemType.setStatus(_A)
_CfprFaultSuppressTaskTable_Object=MibTable
cfprFaultSuppressTaskTable=_CfprFaultSuppressTaskTable_Object((1,3,6,1,4,1,9,9,826,1,1,8))
if mibBuilder.loadTexts:cfprFaultSuppressTaskTable.setStatus(_A)
_CfprFaultSuppressTaskEntry_Object=MibTableRow
cfprFaultSuppressTaskEntry=_CfprFaultSuppressTaskEntry_Object((1,3,6,1,4,1,9,9,826,1,1,8,1))
cfprFaultSuppressTaskEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprFaultSuppressTaskEntry.setStatus(_A)
_CfprFaultSuppressTaskInstanceId_Type=CfprManagedObjectId
_CfprFaultSuppressTaskInstanceId_Object=MibTableColumn
cfprFaultSuppressTaskInstanceId=_CfprFaultSuppressTaskInstanceId_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,1),_CfprFaultSuppressTaskInstanceId_Type())
cfprFaultSuppressTaskInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprFaultSuppressTaskInstanceId.setStatus(_A)
_CfprFaultSuppressTaskDn_Type=CfprManagedObjectDn
_CfprFaultSuppressTaskDn_Object=MibTableColumn
cfprFaultSuppressTaskDn=_CfprFaultSuppressTaskDn_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,2),_CfprFaultSuppressTaskDn_Type())
cfprFaultSuppressTaskDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskDn.setStatus(_A)
_CfprFaultSuppressTaskRn_Type=SnmpAdminString
_CfprFaultSuppressTaskRn_Object=MibTableColumn
cfprFaultSuppressTaskRn=_CfprFaultSuppressTaskRn_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,3),_CfprFaultSuppressTaskRn_Type())
cfprFaultSuppressTaskRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskRn.setStatus(_A)
_CfprFaultSuppressTaskAdminState_Type=CfprTrigAdminState
_CfprFaultSuppressTaskAdminState_Object=MibTableColumn
cfprFaultSuppressTaskAdminState=_CfprFaultSuppressTaskAdminState_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,4),_CfprFaultSuppressTaskAdminState_Type())
cfprFaultSuppressTaskAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskAdminState.setStatus(_A)
_CfprFaultSuppressTaskAutoDelete_Type=TruthValue
_CfprFaultSuppressTaskAutoDelete_Object=MibTableColumn
cfprFaultSuppressTaskAutoDelete=_CfprFaultSuppressTaskAutoDelete_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,5),_CfprFaultSuppressTaskAutoDelete_Type())
cfprFaultSuppressTaskAutoDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskAutoDelete.setStatus(_A)
_CfprFaultSuppressTaskDescr_Type=SnmpAdminString
_CfprFaultSuppressTaskDescr_Object=MibTableColumn
cfprFaultSuppressTaskDescr=_CfprFaultSuppressTaskDescr_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,6),_CfprFaultSuppressTaskDescr_Type())
cfprFaultSuppressTaskDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskDescr.setStatus(_A)
_CfprFaultSuppressTaskIgnoreCap_Type=TruthValue
_CfprFaultSuppressTaskIgnoreCap_Object=MibTableColumn
cfprFaultSuppressTaskIgnoreCap=_CfprFaultSuppressTaskIgnoreCap_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,7),_CfprFaultSuppressTaskIgnoreCap_Type())
cfprFaultSuppressTaskIgnoreCap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskIgnoreCap.setStatus(_A)
_CfprFaultSuppressTaskIntId_Type=SnmpAdminString
_CfprFaultSuppressTaskIntId_Object=MibTableColumn
cfprFaultSuppressTaskIntId=_CfprFaultSuppressTaskIntId_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,8),_CfprFaultSuppressTaskIntId_Type())
cfprFaultSuppressTaskIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskIntId.setStatus(_A)
_CfprFaultSuppressTaskName_Type=SnmpAdminString
_CfprFaultSuppressTaskName_Object=MibTableColumn
cfprFaultSuppressTaskName=_CfprFaultSuppressTaskName_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,9),_CfprFaultSuppressTaskName_Type())
cfprFaultSuppressTaskName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskName.setStatus(_A)
_CfprFaultSuppressTaskOperScheduler_Type=SnmpAdminString
_CfprFaultSuppressTaskOperScheduler_Object=MibTableColumn
cfprFaultSuppressTaskOperScheduler=_CfprFaultSuppressTaskOperScheduler_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,10),_CfprFaultSuppressTaskOperScheduler_Type())
cfprFaultSuppressTaskOperScheduler.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskOperScheduler.setStatus(_A)
_CfprFaultSuppressTaskOperState_Type=CfprTrigTrigOperState
_CfprFaultSuppressTaskOperState_Object=MibTableColumn
cfprFaultSuppressTaskOperState=_CfprFaultSuppressTaskOperState_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,11),_CfprFaultSuppressTaskOperState_Type())
cfprFaultSuppressTaskOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskOperState.setStatus(_A)
_CfprFaultSuppressTaskOperSuppressPolicyName_Type=SnmpAdminString
_CfprFaultSuppressTaskOperSuppressPolicyName_Object=MibTableColumn
cfprFaultSuppressTaskOperSuppressPolicyName=_CfprFaultSuppressTaskOperSuppressPolicyName_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,12),_CfprFaultSuppressTaskOperSuppressPolicyName_Type())
cfprFaultSuppressTaskOperSuppressPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskOperSuppressPolicyName.setStatus(_A)
_CfprFaultSuppressTaskPolicyLevel_Type=Gauge32
_CfprFaultSuppressTaskPolicyLevel_Object=MibTableColumn
cfprFaultSuppressTaskPolicyLevel=_CfprFaultSuppressTaskPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,13),_CfprFaultSuppressTaskPolicyLevel_Type())
cfprFaultSuppressTaskPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskPolicyLevel.setStatus(_A)
_CfprFaultSuppressTaskPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprFaultSuppressTaskPolicyOwner_Object=MibTableColumn
cfprFaultSuppressTaskPolicyOwner=_CfprFaultSuppressTaskPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,14),_CfprFaultSuppressTaskPolicyOwner_Type())
cfprFaultSuppressTaskPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskPolicyOwner.setStatus(_A)
_CfprFaultSuppressTaskScheduler_Type=SnmpAdminString
_CfprFaultSuppressTaskScheduler_Object=MibTableColumn
cfprFaultSuppressTaskScheduler=_CfprFaultSuppressTaskScheduler_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,15),_CfprFaultSuppressTaskScheduler_Type())
cfprFaultSuppressTaskScheduler.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskScheduler.setStatus(_A)
_CfprFaultSuppressTaskSuppressPolicyName_Type=SnmpAdminString
_CfprFaultSuppressTaskSuppressPolicyName_Object=MibTableColumn
cfprFaultSuppressTaskSuppressPolicyName=_CfprFaultSuppressTaskSuppressPolicyName_Object((1,3,6,1,4,1,9,9,826,1,1,8,1,16),_CfprFaultSuppressTaskSuppressPolicyName_Type())
cfprFaultSuppressTaskSuppressPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprFaultSuppressTaskSuppressPolicyName.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprFaultObjects':cfprFaultObjects,'cfprFaultInstTable':cfprFaultInstTable,'cfprFaultInstEntry':cfprFaultInstEntry,_E:cfprFaultInstInstanceId,'cfprFaultInstDn':cfprFaultInstDn,'cfprFaultInstRn':cfprFaultInstRn,'cfprFaultInstAffectedObjectId':cfprFaultInstAffectedObjectId,'cfprFaultInstAffectedObjectDn':cfprFaultInstAffectedObjectDn,'cfprFaultInstAck':cfprFaultInstAck,'cfprFaultInstCause':cfprFaultInstCause,'cfprFaultInstChangeSet':cfprFaultInstChangeSet,'cfprFaultInstCode':cfprFaultInstCode,'cfprFaultInstCreated':cfprFaultInstCreated,'cfprFaultInstDescr':cfprFaultInstDescr,'cfprFaultInstHighestSeverity':cfprFaultInstHighestSeverity,'cfprFaultInstId':cfprFaultInstId,'cfprFaultInstLastTransition':cfprFaultInstLastTransition,'cfprFaultInstLc':cfprFaultInstLc,'cfprFaultInstOccur':cfprFaultInstOccur,'cfprFaultInstOrigSeverity':cfprFaultInstOrigSeverity,'cfprFaultInstPrevSeverity':cfprFaultInstPrevSeverity,'cfprFaultInstRule':cfprFaultInstRule,'cfprFaultInstSeverity':cfprFaultInstSeverity,'cfprFaultInstTags':cfprFaultInstTags,'cfprFaultInstType':cfprFaultInstType,'cfprFaultAffectedClassTable':cfprFaultAffectedClassTable,'cfprFaultAffectedClassEntry':cfprFaultAffectedClassEntry,_F:cfprFaultAffectedClassInstanceId,'cfprFaultAffectedClassDn':cfprFaultAffectedClassDn,'cfprFaultAffectedClassRn':cfprFaultAffectedClassRn,'cfprFaultAffectedClassMoClassId':cfprFaultAffectedClassMoClassId,'cfprFaultHolderTable':cfprFaultHolderTable,'cfprFaultHolderEntry':cfprFaultHolderEntry,_G:cfprFaultHolderInstanceId,'cfprFaultHolderDn':cfprFaultHolderDn,'cfprFaultHolderRn':cfprFaultHolderRn,'cfprFaultHolderName':cfprFaultHolderName,'cfprFaultHolderTotalFaults':cfprFaultHolderTotalFaults,'cfprFaultLocalTypedHolderTable':cfprFaultLocalTypedHolderTable,'cfprFaultLocalTypedHolderEntry':cfprFaultLocalTypedHolderEntry,_H:cfprFaultLocalTypedHolderInstanceId,'cfprFaultLocalTypedHolderDn':cfprFaultLocalTypedHolderDn,'cfprFaultLocalTypedHolderRn':cfprFaultLocalTypedHolderRn,'cfprFaultLocalTypedHolderName':cfprFaultLocalTypedHolderName,'cfprFaultLocalTypedHolderTotalFaults':cfprFaultLocalTypedHolderTotalFaults,'cfprFaultLocalTypedHolderType':cfprFaultLocalTypedHolderType,'cfprFaultPolicyTable':cfprFaultPolicyTable,'cfprFaultPolicyEntry':cfprFaultPolicyEntry,_I:cfprFaultPolicyInstanceId,'cfprFaultPolicyDn':cfprFaultPolicyDn,'cfprFaultPolicyRn':cfprFaultPolicyRn,'cfprFaultPolicyAckAction':cfprFaultPolicyAckAction,'cfprFaultPolicyClearAction':cfprFaultPolicyClearAction,'cfprFaultPolicyClearInterval':cfprFaultPolicyClearInterval,'cfprFaultPolicyDescr':cfprFaultPolicyDescr,'cfprFaultPolicyFlapInterval':cfprFaultPolicyFlapInterval,'cfprFaultPolicyIntId':cfprFaultPolicyIntId,'cfprFaultPolicyName':cfprFaultPolicyName,'cfprFaultPolicyPolicyLevel':cfprFaultPolicyPolicyLevel,'cfprFaultPolicyPolicyOwner':cfprFaultPolicyPolicyOwner,'cfprFaultPolicyRetentionInterval':cfprFaultPolicyRetentionInterval,'cfprFaultPolicySizeLimit':cfprFaultPolicySizeLimit,'cfprFaultPolicySoakInterval':cfprFaultPolicySoakInterval,'cfprFaultPolicySoakingSeverity':cfprFaultPolicySoakingSeverity,'cfprFaultSuppressPolicyTable':cfprFaultSuppressPolicyTable,'cfprFaultSuppressPolicyEntry':cfprFaultSuppressPolicyEntry,_J:cfprFaultSuppressPolicyInstanceId,'cfprFaultSuppressPolicyDn':cfprFaultSuppressPolicyDn,'cfprFaultSuppressPolicyRn':cfprFaultSuppressPolicyRn,'cfprFaultSuppressPolicyDescr':cfprFaultSuppressPolicyDescr,'cfprFaultSuppressPolicyIntId':cfprFaultSuppressPolicyIntId,'cfprFaultSuppressPolicyName':cfprFaultSuppressPolicyName,'cfprFaultSuppressPolicyPolicyLevel':cfprFaultSuppressPolicyPolicyLevel,'cfprFaultSuppressPolicyPolicyOwner':cfprFaultSuppressPolicyPolicyOwner,'cfprFaultSuppressPolicyItemTable':cfprFaultSuppressPolicyItemTable,'cfprFaultSuppressPolicyItemEntry':cfprFaultSuppressPolicyItemEntry,_K:cfprFaultSuppressPolicyItemInstanceId,'cfprFaultSuppressPolicyItemDn':cfprFaultSuppressPolicyItemDn,'cfprFaultSuppressPolicyItemRn':cfprFaultSuppressPolicyItemRn,'cfprFaultSuppressPolicyItemCause':cfprFaultSuppressPolicyItemCause,'cfprFaultSuppressPolicyItemDescr':cfprFaultSuppressPolicyItemDescr,'cfprFaultSuppressPolicyItemType':cfprFaultSuppressPolicyItemType,'cfprFaultSuppressTaskTable':cfprFaultSuppressTaskTable,'cfprFaultSuppressTaskEntry':cfprFaultSuppressTaskEntry,_L:cfprFaultSuppressTaskInstanceId,'cfprFaultSuppressTaskDn':cfprFaultSuppressTaskDn,'cfprFaultSuppressTaskRn':cfprFaultSuppressTaskRn,'cfprFaultSuppressTaskAdminState':cfprFaultSuppressTaskAdminState,'cfprFaultSuppressTaskAutoDelete':cfprFaultSuppressTaskAutoDelete,'cfprFaultSuppressTaskDescr':cfprFaultSuppressTaskDescr,'cfprFaultSuppressTaskIgnoreCap':cfprFaultSuppressTaskIgnoreCap,'cfprFaultSuppressTaskIntId':cfprFaultSuppressTaskIntId,'cfprFaultSuppressTaskName':cfprFaultSuppressTaskName,'cfprFaultSuppressTaskOperScheduler':cfprFaultSuppressTaskOperScheduler,'cfprFaultSuppressTaskOperState':cfprFaultSuppressTaskOperState,'cfprFaultSuppressTaskOperSuppressPolicyName':cfprFaultSuppressTaskOperSuppressPolicyName,'cfprFaultSuppressTaskPolicyLevel':cfprFaultSuppressTaskPolicyLevel,'cfprFaultSuppressTaskPolicyOwner':cfprFaultSuppressTaskPolicyOwner,'cfprFaultSuppressTaskScheduler':cfprFaultSuppressTaskScheduler,'cfprFaultSuppressTaskSuppressPolicyName':cfprFaultSuppressTaskSuppressPolicyName})