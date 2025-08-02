_t='ciscoEpmNotificationAlarmGroupRev1'
_s='ciscoEpmNotificationObjectsGroupRev1'
_r='ciscoEpmNotificationAlarmGroup'
_q='ciscoEpmNotificationObjectsGroup'
_p='ciscoEpmNotificationAlarmRev1'
_o='ciscoEpmNotificationAlarm'
_n='cenAlarmTableMaxLength'
_m='unknown'
_l='cenAlarmIndex'
_k='ciscoEpmAlarmConfigGroup'
_j='cenAlertID'
_i='cenCustomerRevision'
_h='cenCustomerIdentification'
_g='cenPartitionName'
_f='cenPartitionNumber'
_e='cenAlarmMode'
_d='OctetString'
_c='deprecated'
_b='Unsigned32'
_a='cenUserMessage3'
_Z='cenUserMessage2'
_Y='cenUserMessage1'
_X='cenEventIDList'
_W='cenAlarmTriageValue'
_V='cenAlarmSeverityDefinition'
_U='cenAlarmSeverity'
_T='cenAlarmDescription'
_S='cenAlarmManagedObjectAddress'
_R='cenAlarmManagedObjectAddressType'
_Q='cenAlarmManagedObjectClass'
_P='cenAlarmServerAddress'
_O='cenAlarmServerAddressType'
_N='cenAlarmCategoryDefinition'
_M='cenAlarmCategory'
_L='cenAlarmType'
_K='cenAlarmStatusDefinition'
_J='cenAlarmStatus'
_I='cenAlarmInstanceID'
_H='cenAlarmUpdatedTimestamp'
_G='cenAlarmTimestamp'
_F='cenAlarmVersion'
_E='Integer32'
_D='SnmpAdminString'
_C='read-only'
_B='current'
_A='CISCO-EPM-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_d,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoEpmNotificationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,311))
if mibBuilder.loadTexts:ciscoEpmNotificationMIB.setRevisions(('2004-06-07 00:00','2003-08-21 00:00','2002-07-28 14:20'))
_CiscoEpmNotificationMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoEpmNotificationMIBNotifs=_CiscoEpmNotificationMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,311,0))
_CiscoEpmNotificationMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEpmNotificationMIBObjects=_CiscoEpmNotificationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,311,1))
_CenAlarmData_ObjectIdentity=ObjectIdentity
cenAlarmData=_CenAlarmData_ObjectIdentity((1,3,6,1,4,1,9,9,311,1,1))
class _CenAlarmTableMaxLength_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CenAlarmTableMaxLength_Type.__name__=_b
_CenAlarmTableMaxLength_Object=MibScalar
cenAlarmTableMaxLength=_CenAlarmTableMaxLength_Object((1,3,6,1,4,1,9,9,311,1,1,1),_CenAlarmTableMaxLength_Type())
cenAlarmTableMaxLength.setMaxAccess('read-write')
if mibBuilder.loadTexts:cenAlarmTableMaxLength.setStatus(_B)
_CenAlarmTable_Object=MibTable
cenAlarmTable=_CenAlarmTable_Object((1,3,6,1,4,1,9,9,311,1,1,2))
if mibBuilder.loadTexts:cenAlarmTable.setStatus(_B)
_CenAlarmEntry_Object=MibTableRow
cenAlarmEntry=_CenAlarmEntry_Object((1,3,6,1,4,1,9,9,311,1,1,2,1))
cenAlarmEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:cenAlarmEntry.setStatus(_B)
class _CenAlarmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CenAlarmIndex_Type.__name__=_b
_CenAlarmIndex_Object=MibTableColumn
cenAlarmIndex=_CenAlarmIndex_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,1),_CenAlarmIndex_Type())
cenAlarmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cenAlarmIndex.setStatus(_B)
class _CenAlarmVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CenAlarmVersion_Type.__name__=_D
_CenAlarmVersion_Object=MibTableColumn
cenAlarmVersion=_CenAlarmVersion_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,2),_CenAlarmVersion_Type())
cenAlarmVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmVersion.setStatus(_B)
_CenAlarmTimestamp_Type=TimeStamp
_CenAlarmTimestamp_Object=MibTableColumn
cenAlarmTimestamp=_CenAlarmTimestamp_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,3),_CenAlarmTimestamp_Type())
cenAlarmTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmTimestamp.setStatus(_B)
_CenAlarmUpdatedTimestamp_Type=TimeStamp
_CenAlarmUpdatedTimestamp_Object=MibTableColumn
cenAlarmUpdatedTimestamp=_CenAlarmUpdatedTimestamp_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,4),_CenAlarmUpdatedTimestamp_Type())
cenAlarmUpdatedTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmUpdatedTimestamp.setStatus(_B)
class _CenAlarmInstanceID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CenAlarmInstanceID_Type.__name__=_D
_CenAlarmInstanceID_Object=MibTableColumn
cenAlarmInstanceID=_CenAlarmInstanceID_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,5),_CenAlarmInstanceID_Type())
cenAlarmInstanceID.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmInstanceID.setStatus(_B)
class _CenAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_CenAlarmStatus_Type.__name__=_E
_CenAlarmStatus_Object=MibTableColumn
cenAlarmStatus=_CenAlarmStatus_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,6),_CenAlarmStatus_Type())
cenAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmStatus.setStatus(_B)
class _CenAlarmStatusDefinition_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenAlarmStatusDefinition_Type.__name__=_D
_CenAlarmStatusDefinition_Object=MibTableColumn
cenAlarmStatusDefinition=_CenAlarmStatusDefinition_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,7),_CenAlarmStatusDefinition_Type())
cenAlarmStatusDefinition.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmStatusDefinition.setStatus(_B)
class _CenAlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_m,1),('direct',2),('indirect',3),('mixed',4)))
_CenAlarmType_Type.__name__=_E
_CenAlarmType_Object=MibTableColumn
cenAlarmType=_CenAlarmType_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,8),_CenAlarmType_Type())
cenAlarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmType.setStatus(_B)
class _CenAlarmCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,250))
_CenAlarmCategory_Type.__name__=_E
_CenAlarmCategory_Object=MibTableColumn
cenAlarmCategory=_CenAlarmCategory_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,9),_CenAlarmCategory_Type())
cenAlarmCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmCategory.setStatus(_B)
class _CenAlarmCategoryDefinition_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenAlarmCategoryDefinition_Type.__name__=_D
_CenAlarmCategoryDefinition_Object=MibTableColumn
cenAlarmCategoryDefinition=_CenAlarmCategoryDefinition_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,10),_CenAlarmCategoryDefinition_Type())
cenAlarmCategoryDefinition.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmCategoryDefinition.setStatus(_B)
_CenAlarmServerAddressType_Type=InetAddressType
_CenAlarmServerAddressType_Object=MibTableColumn
cenAlarmServerAddressType=_CenAlarmServerAddressType_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,11),_CenAlarmServerAddressType_Type())
cenAlarmServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmServerAddressType.setStatus(_B)
_CenAlarmServerAddress_Type=InetAddress
_CenAlarmServerAddress_Object=MibTableColumn
cenAlarmServerAddress=_CenAlarmServerAddress_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,12),_CenAlarmServerAddress_Type())
cenAlarmServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmServerAddress.setStatus(_B)
class _CenAlarmManagedObjectClass_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenAlarmManagedObjectClass_Type.__name__=_D
_CenAlarmManagedObjectClass_Object=MibTableColumn
cenAlarmManagedObjectClass=_CenAlarmManagedObjectClass_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,13),_CenAlarmManagedObjectClass_Type())
cenAlarmManagedObjectClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmManagedObjectClass.setStatus(_B)
_CenAlarmManagedObjectAddressType_Type=InetAddressType
_CenAlarmManagedObjectAddressType_Object=MibTableColumn
cenAlarmManagedObjectAddressType=_CenAlarmManagedObjectAddressType_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,14),_CenAlarmManagedObjectAddressType_Type())
cenAlarmManagedObjectAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmManagedObjectAddressType.setStatus(_B)
_CenAlarmManagedObjectAddress_Type=InetAddress
_CenAlarmManagedObjectAddress_Object=MibTableColumn
cenAlarmManagedObjectAddress=_CenAlarmManagedObjectAddress_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,15),_CenAlarmManagedObjectAddress_Type())
cenAlarmManagedObjectAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmManagedObjectAddress.setStatus(_B)
class _CenAlarmDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_CenAlarmDescription_Type.__name__=_d
_CenAlarmDescription_Object=MibTableColumn
cenAlarmDescription=_CenAlarmDescription_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,16),_CenAlarmDescription_Type())
cenAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmDescription.setStatus(_B)
class _CenAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CenAlarmSeverity_Type.__name__=_E
_CenAlarmSeverity_Object=MibTableColumn
cenAlarmSeverity=_CenAlarmSeverity_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,17),_CenAlarmSeverity_Type())
cenAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmSeverity.setStatus(_B)
class _CenAlarmSeverityDefinition_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenAlarmSeverityDefinition_Type.__name__=_D
_CenAlarmSeverityDefinition_Object=MibTableColumn
cenAlarmSeverityDefinition=_CenAlarmSeverityDefinition_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,18),_CenAlarmSeverityDefinition_Type())
cenAlarmSeverityDefinition.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmSeverityDefinition.setStatus(_B)
class _CenAlarmTriageValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CenAlarmTriageValue_Type.__name__=_E
_CenAlarmTriageValue_Object=MibTableColumn
cenAlarmTriageValue=_CenAlarmTriageValue_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,19),_CenAlarmTriageValue_Type())
cenAlarmTriageValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmTriageValue.setStatus(_B)
class _CenEventIDList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_CenEventIDList_Type.__name__=_d
_CenEventIDList_Object=MibTableColumn
cenEventIDList=_CenEventIDList_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,20),_CenEventIDList_Type())
cenEventIDList.setMaxAccess(_C)
if mibBuilder.loadTexts:cenEventIDList.setStatus(_B)
class _CenUserMessage1_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenUserMessage1_Type.__name__=_D
_CenUserMessage1_Object=MibTableColumn
cenUserMessage1=_CenUserMessage1_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,21),_CenUserMessage1_Type())
cenUserMessage1.setMaxAccess(_C)
if mibBuilder.loadTexts:cenUserMessage1.setStatus(_B)
class _CenUserMessage2_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenUserMessage2_Type.__name__=_D
_CenUserMessage2_Object=MibTableColumn
cenUserMessage2=_CenUserMessage2_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,22),_CenUserMessage2_Type())
cenUserMessage2.setMaxAccess(_C)
if mibBuilder.loadTexts:cenUserMessage2.setStatus(_B)
class _CenUserMessage3_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenUserMessage3_Type.__name__=_D
_CenUserMessage3_Object=MibTableColumn
cenUserMessage3=_CenUserMessage3_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,23),_CenUserMessage3_Type())
cenUserMessage3.setMaxAccess(_C)
if mibBuilder.loadTexts:cenUserMessage3.setStatus(_B)
class _CenAlarmMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),('alert',2),('event',3)))
_CenAlarmMode_Type.__name__=_E
_CenAlarmMode_Object=MibTableColumn
cenAlarmMode=_CenAlarmMode_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,24),_CenAlarmMode_Type())
cenAlarmMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlarmMode.setStatus(_B)
class _CenPartitionNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CenPartitionNumber_Type.__name__=_b
_CenPartitionNumber_Object=MibTableColumn
cenPartitionNumber=_CenPartitionNumber_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,25),_CenPartitionNumber_Type())
cenPartitionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cenPartitionNumber.setStatus(_B)
class _CenPartitionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenPartitionName_Type.__name__=_D
_CenPartitionName_Object=MibTableColumn
cenPartitionName=_CenPartitionName_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,26),_CenPartitionName_Type())
cenPartitionName.setMaxAccess(_C)
if mibBuilder.loadTexts:cenPartitionName.setStatus(_B)
class _CenCustomerIdentification_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenCustomerIdentification_Type.__name__=_D
_CenCustomerIdentification_Object=MibTableColumn
cenCustomerIdentification=_CenCustomerIdentification_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,27),_CenCustomerIdentification_Type())
cenCustomerIdentification.setMaxAccess(_C)
if mibBuilder.loadTexts:cenCustomerIdentification.setStatus(_B)
class _CenCustomerRevision_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CenCustomerRevision_Type.__name__=_D
_CenCustomerRevision_Object=MibTableColumn
cenCustomerRevision=_CenCustomerRevision_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,28),_CenCustomerRevision_Type())
cenCustomerRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cenCustomerRevision.setStatus(_B)
class _CenAlertID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CenAlertID_Type.__name__=_D
_CenAlertID_Object=MibTableColumn
cenAlertID=_CenAlertID_Object((1,3,6,1,4,1,9,9,311,1,1,2,1,29),_CenAlertID_Type())
cenAlertID.setMaxAccess(_C)
if mibBuilder.loadTexts:cenAlertID.setStatus(_B)
_CiscoEpmNotificationMIBConform_ObjectIdentity=ObjectIdentity
ciscoEpmNotificationMIBConform=_CiscoEpmNotificationMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,311,2))
_CiscoEpmNotificationMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEpmNotificationMIBCompliances=_CiscoEpmNotificationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,311,2,1))
_CiscoEpmNotificationMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEpmNotificationMIBGroups=_CiscoEpmNotificationMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,311,2,2))
ciscoEpmNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,311,2,2,2))
ciscoEpmNotificationObjectsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoEpmNotificationObjectsGroup.setStatus(_c)
ciscoEpmAlarmConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,311,2,2,3))
ciscoEpmAlarmConfigGroup.setObjects((_A,_n))
if mibBuilder.loadTexts:ciscoEpmAlarmConfigGroup.setStatus(_B)
ciscoEpmNotificationObjectsGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,311,2,2,5))
ciscoEpmNotificationObjectsGroupRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoEpmNotificationObjectsGroupRev1.setStatus(_B)
ciscoEpmNotificationAlarm=NotificationType((1,3,6,1,4,1,9,9,311,0,1))
ciscoEpmNotificationAlarm.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoEpmNotificationAlarm.setStatus(_c)
ciscoEpmNotificationAlarmRev1=NotificationType((1,3,6,1,4,1,9,9,311,0,2))
ciscoEpmNotificationAlarmRev1.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:ciscoEpmNotificationAlarmRev1.setStatus(_B)
ciscoEpmNotificationAlarmGroup=NotificationGroup((1,3,6,1,4,1,9,9,311,2,2,1))
ciscoEpmNotificationAlarmGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:ciscoEpmNotificationAlarmGroup.setStatus(_c)
ciscoEpmNotificationAlarmGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,311,2,2,4))
ciscoEpmNotificationAlarmGroupRev1.setObjects((_A,_p))
if mibBuilder.loadTexts:ciscoEpmNotificationAlarmGroupRev1.setStatus(_B)
ciscoEpmNotificationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,311,2,1,1))
ciscoEpmNotificationMIBCompliance.setObjects(*((_A,_q),(_A,_r),(_A,_k)))
if mibBuilder.loadTexts:ciscoEpmNotificationMIBCompliance.setStatus(_c)
ciscoEpmNotificationMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,311,2,1,1,2))
ciscoEpmNotificationMIBComplianceRev1.setObjects(*((_A,_s),(_A,_t),(_A,_k)))
if mibBuilder.loadTexts:ciscoEpmNotificationMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoEpmNotificationMIB':ciscoEpmNotificationMIB,'ciscoEpmNotificationMIBNotifs':ciscoEpmNotificationMIBNotifs,_o:ciscoEpmNotificationAlarm,_p:ciscoEpmNotificationAlarmRev1,'ciscoEpmNotificationMIBObjects':ciscoEpmNotificationMIBObjects,'cenAlarmData':cenAlarmData,_n:cenAlarmTableMaxLength,'cenAlarmTable':cenAlarmTable,'cenAlarmEntry':cenAlarmEntry,_l:cenAlarmIndex,_F:cenAlarmVersion,_G:cenAlarmTimestamp,_H:cenAlarmUpdatedTimestamp,_I:cenAlarmInstanceID,_J:cenAlarmStatus,_K:cenAlarmStatusDefinition,_L:cenAlarmType,_M:cenAlarmCategory,_N:cenAlarmCategoryDefinition,_O:cenAlarmServerAddressType,_P:cenAlarmServerAddress,_Q:cenAlarmManagedObjectClass,_R:cenAlarmManagedObjectAddressType,_S:cenAlarmManagedObjectAddress,_T:cenAlarmDescription,_U:cenAlarmSeverity,_V:cenAlarmSeverityDefinition,_W:cenAlarmTriageValue,_X:cenEventIDList,_Y:cenUserMessage1,_Z:cenUserMessage2,_a:cenUserMessage3,_e:cenAlarmMode,_f:cenPartitionNumber,_g:cenPartitionName,_h:cenCustomerIdentification,_i:cenCustomerRevision,_j:cenAlertID,'ciscoEpmNotificationMIBConform':ciscoEpmNotificationMIBConform,'ciscoEpmNotificationMIBCompliances':ciscoEpmNotificationMIBCompliances,'ciscoEpmNotificationMIBCompliance':ciscoEpmNotificationMIBCompliance,'ciscoEpmNotificationMIBComplianceRev1':ciscoEpmNotificationMIBComplianceRev1,'ciscoEpmNotificationMIBGroups':ciscoEpmNotificationMIBGroups,_r:ciscoEpmNotificationAlarmGroup,_q:ciscoEpmNotificationObjectsGroup,_k:ciscoEpmAlarmConfigGroup,_t:ciscoEpmNotificationAlarmGroupRev1,_s:ciscoEpmNotificationObjectsGroupRev1})