_d='ciscoWirelessNotificationEnableGroup'
_c='ciscoWirelessNotificationConfigGroup'
_b='ciscoWirelessNotificationsGroup'
_a='ciscoWirelessNotificationObjectsGroup'
_Z='ciscoWirelessMOStatusNotification'
_Y='cwNotificationMOStatusEnable'
_X='cWNotificationType'
_W='cwNotificationHistoryTableMaxLength'
_V='cWNotificationIndex'
_U='read-write'
_T='unknown'
_S='TruthValue'
_R='SnmpAdminString'
_Q='cWNotificationVirtualDomains'
_P='cWNotificationSpecialAttributes'
_O='cWNotificationSeverity'
_N='cWNotificationDescription'
_M='cWNotificationSourceDisplayName'
_L='cWNotificationManagedObjectAddress'
_K='cWNotificationManagedObjectAddressType'
_J='cWNotificationSubCategory'
_I='cWNotificationCategory'
_H='cWNotificationKey'
_G='cWNotificationUpdatedTimestamp'
_F='cWNotificationTimestamp'
_E='Unsigned32'
_D='OctetString'
_C='read-only'
_B='current'
_A='CISCO-WIRELESS-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_S)
ciscoWirelessNotificationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,712))
if mibBuilder.loadTexts:ciscoWirelessNotificationMIB.setRevisions(('2011-06-06 00:00','2010-09-15 00:00','2009-10-28 00:00'))
class CWirelessNotificationType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('alert',2),('event',3)))
class CWirelessNotificationCategory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_T,1),('accessPoints',2),('adhocRogue',3),('clients',4),('controllers',5),('coverageHole',6),('interference',7),('contextAwareNotifications',8),('meshLinks',9),('mobilityService',10),('performance',11),('rogueAP',12),('rrm',13),('security',14),('wcs',15),('switch',16),('ncs',17)))
_CiscoWirelessNotificationMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoWirelessNotificationMIBNotifs=_CiscoWirelessNotificationMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,712,0))
_CiscoWirelessNotificationMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWirelessNotificationMIBObjects=_CiscoWirelessNotificationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,712,1))
_CWNotificationData_ObjectIdentity=ObjectIdentity
cWNotificationData=_CWNotificationData_ObjectIdentity((1,3,6,1,4,1,9,9,712,1,1))
class _CwNotificationHistoryTableMaxLength_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CwNotificationHistoryTableMaxLength_Type.__name__=_E
_CwNotificationHistoryTableMaxLength_Object=MibScalar
cwNotificationHistoryTableMaxLength=_CwNotificationHistoryTableMaxLength_Object((1,3,6,1,4,1,9,9,712,1,1,1),_CwNotificationHistoryTableMaxLength_Type())
cwNotificationHistoryTableMaxLength.setMaxAccess(_U)
if mibBuilder.loadTexts:cwNotificationHistoryTableMaxLength.setStatus(_B)
_CwNotificationHistoryTable_Object=MibTable
cwNotificationHistoryTable=_CwNotificationHistoryTable_Object((1,3,6,1,4,1,9,9,712,1,1,2))
if mibBuilder.loadTexts:cwNotificationHistoryTable.setStatus(_B)
_CwNotificationHistoryEntry_Object=MibTableRow
cwNotificationHistoryEntry=_CwNotificationHistoryEntry_Object((1,3,6,1,4,1,9,9,712,1,1,2,1))
cwNotificationHistoryEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:cwNotificationHistoryEntry.setStatus(_B)
class _CWNotificationIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CWNotificationIndex_Type.__name__=_E
_CWNotificationIndex_Object=MibTableColumn
cWNotificationIndex=_CWNotificationIndex_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,1),_CWNotificationIndex_Type())
cWNotificationIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cWNotificationIndex.setStatus(_B)
_CWNotificationTimestamp_Type=DateAndTime
_CWNotificationTimestamp_Object=MibTableColumn
cWNotificationTimestamp=_CWNotificationTimestamp_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,2),_CWNotificationTimestamp_Type())
cWNotificationTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationTimestamp.setStatus(_B)
_CWNotificationUpdatedTimestamp_Type=DateAndTime
_CWNotificationUpdatedTimestamp_Object=MibTableColumn
cWNotificationUpdatedTimestamp=_CWNotificationUpdatedTimestamp_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,3),_CWNotificationUpdatedTimestamp_Type())
cWNotificationUpdatedTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationUpdatedTimestamp.setStatus(_B)
class _CWNotificationKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CWNotificationKey_Type.__name__=_R
_CWNotificationKey_Object=MibTableColumn
cWNotificationKey=_CWNotificationKey_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,4),_CWNotificationKey_Type())
cWNotificationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationKey.setStatus(_B)
_CWNotificationCategory_Type=CWirelessNotificationCategory
_CWNotificationCategory_Object=MibTableColumn
cWNotificationCategory=_CWNotificationCategory_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,5),_CWNotificationCategory_Type())
cWNotificationCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationCategory.setStatus(_B)
class _CWNotificationSubCategory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_CWNotificationSubCategory_Type.__name__=_D
_CWNotificationSubCategory_Object=MibTableColumn
cWNotificationSubCategory=_CWNotificationSubCategory_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,6),_CWNotificationSubCategory_Type())
cWNotificationSubCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationSubCategory.setStatus(_B)
_CWNotificationManagedObjectAddressType_Type=InetAddressType
_CWNotificationManagedObjectAddressType_Object=MibTableColumn
cWNotificationManagedObjectAddressType=_CWNotificationManagedObjectAddressType_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,7),_CWNotificationManagedObjectAddressType_Type())
cWNotificationManagedObjectAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationManagedObjectAddressType.setStatus(_B)
_CWNotificationManagedObjectAddress_Type=InetAddress
_CWNotificationManagedObjectAddress_Object=MibTableColumn
cWNotificationManagedObjectAddress=_CWNotificationManagedObjectAddress_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,8),_CWNotificationManagedObjectAddress_Type())
cWNotificationManagedObjectAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationManagedObjectAddress.setStatus(_B)
class _CWNotificationSourceDisplayName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_CWNotificationSourceDisplayName_Type.__name__=_D
_CWNotificationSourceDisplayName_Object=MibTableColumn
cWNotificationSourceDisplayName=_CWNotificationSourceDisplayName_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,9),_CWNotificationSourceDisplayName_Type())
cWNotificationSourceDisplayName.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationSourceDisplayName.setStatus(_B)
class _CWNotificationDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_CWNotificationDescription_Type.__name__=_D
_CWNotificationDescription_Object=MibTableColumn
cWNotificationDescription=_CWNotificationDescription_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,10),_CWNotificationDescription_Type())
cWNotificationDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationDescription.setStatus(_B)
_CWNotificationSeverity_Type=CiscoAlarmSeverity
_CWNotificationSeverity_Object=MibTableColumn
cWNotificationSeverity=_CWNotificationSeverity_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,11),_CWNotificationSeverity_Type())
cWNotificationSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationSeverity.setStatus(_B)
class _CWNotificationSpecialAttributes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_CWNotificationSpecialAttributes_Type.__name__=_D
_CWNotificationSpecialAttributes_Object=MibTableColumn
cWNotificationSpecialAttributes=_CWNotificationSpecialAttributes_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,12),_CWNotificationSpecialAttributes_Type())
cWNotificationSpecialAttributes.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationSpecialAttributes.setStatus(_B)
_CWNotificationType_Type=CWirelessNotificationType
_CWNotificationType_Object=MibTableColumn
cWNotificationType=_CWNotificationType_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,13),_CWNotificationType_Type())
cWNotificationType.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationType.setStatus(_B)
class _CWNotificationVirtualDomains_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_CWNotificationVirtualDomains_Type.__name__=_D
_CWNotificationVirtualDomains_Object=MibTableColumn
cWNotificationVirtualDomains=_CWNotificationVirtualDomains_Object((1,3,6,1,4,1,9,9,712,1,1,2,1,14),_CWNotificationVirtualDomains_Type())
cWNotificationVirtualDomains.setMaxAccess(_C)
if mibBuilder.loadTexts:cWNotificationVirtualDomains.setStatus(_B)
class _CwNotificationMOStatusEnable_Type(TruthValue):defaultValue=1
_CwNotificationMOStatusEnable_Type.__name__=_S
_CwNotificationMOStatusEnable_Object=MibScalar
cwNotificationMOStatusEnable=_CwNotificationMOStatusEnable_Object((1,3,6,1,4,1,9,9,712,1,1,3),_CwNotificationMOStatusEnable_Type())
cwNotificationMOStatusEnable.setMaxAccess(_U)
if mibBuilder.loadTexts:cwNotificationMOStatusEnable.setStatus(_B)
_CiscoWirelessNotificationMIBConform_ObjectIdentity=ObjectIdentity
ciscoWirelessNotificationMIBConform=_CiscoWirelessNotificationMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,712,2))
_CiscoWirelessNotificationMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWirelessNotificationMIBCompliances=_CiscoWirelessNotificationMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,712,2,1))
_CiscoWirelessNotificationMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWirelessNotificationMIBGroups=_CiscoWirelessNotificationMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,712,2,2))
ciscoWirelessNotificationConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,712,2,2,1))
ciscoWirelessNotificationConfigGroup.setObjects((_A,_W))
if mibBuilder.loadTexts:ciscoWirelessNotificationConfigGroup.setStatus(_B)
ciscoWirelessNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,712,2,2,3))
ciscoWirelessNotificationObjectsGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_X),(_A,_Q)))
if mibBuilder.loadTexts:ciscoWirelessNotificationObjectsGroup.setStatus(_B)
ciscoWirelessNotificationEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,712,2,2,4))
ciscoWirelessNotificationEnableGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:ciscoWirelessNotificationEnableGroup.setStatus(_B)
ciscoWirelessMOStatusNotification=NotificationType((1,3,6,1,4,1,9,9,712,0,1))
ciscoWirelessMOStatusNotification.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciscoWirelessMOStatusNotification.setStatus(_B)
ciscoWirelessNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,712,2,2,2))
ciscoWirelessNotificationsGroup.setObjects((_A,_Z))
if mibBuilder.loadTexts:ciscoWirelessNotificationsGroup.setStatus(_B)
ciscoWirelessNotificationMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,712,2,1,1))
ciscoWirelessNotificationMIBCompliance.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoWirelessNotificationMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CWirelessNotificationType':CWirelessNotificationType,'CWirelessNotificationCategory':CWirelessNotificationCategory,'ciscoWirelessNotificationMIB':ciscoWirelessNotificationMIB,'ciscoWirelessNotificationMIBNotifs':ciscoWirelessNotificationMIBNotifs,_Z:ciscoWirelessMOStatusNotification,'ciscoWirelessNotificationMIBObjects':ciscoWirelessNotificationMIBObjects,'cWNotificationData':cWNotificationData,_W:cwNotificationHistoryTableMaxLength,'cwNotificationHistoryTable':cwNotificationHistoryTable,'cwNotificationHistoryEntry':cwNotificationHistoryEntry,_V:cWNotificationIndex,_F:cWNotificationTimestamp,_G:cWNotificationUpdatedTimestamp,_H:cWNotificationKey,_I:cWNotificationCategory,_J:cWNotificationSubCategory,_K:cWNotificationManagedObjectAddressType,_L:cWNotificationManagedObjectAddress,_M:cWNotificationSourceDisplayName,_N:cWNotificationDescription,_O:cWNotificationSeverity,_P:cWNotificationSpecialAttributes,_X:cWNotificationType,_Q:cWNotificationVirtualDomains,_Y:cwNotificationMOStatusEnable,'ciscoWirelessNotificationMIBConform':ciscoWirelessNotificationMIBConform,'ciscoWirelessNotificationMIBCompliances':ciscoWirelessNotificationMIBCompliances,'ciscoWirelessNotificationMIBCompliance':ciscoWirelessNotificationMIBCompliance,'ciscoWirelessNotificationMIBGroups':ciscoWirelessNotificationMIBGroups,_c:ciscoWirelessNotificationConfigGroup,_b:ciscoWirelessNotificationsGroup,_a:ciscoWirelessNotificationObjectsGroup,_d:ciscoWirelessNotificationEnableGroup})