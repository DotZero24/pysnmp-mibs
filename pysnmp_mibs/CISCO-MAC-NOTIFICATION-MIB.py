_w='cmnMACThresholdNotifGroup'
_v='cmnMACMoveNotifGroup'
_u='cmnMACThresholdGroup'
_t='cmnMACMoveGroup'
_s='cmnMacThresholdExceedNotif'
_r='cmnMacMoveNotification'
_q='cmnMacChangedNotification'
_p='cmnUtilizationEntries'
_o='cmnMACThresholdNotifEnabled'
_n='cmnMACThresholdInterval'
_m='cmnMACThresholdFeatureEnabled'
_l='cmnMACMoveNotificationsEnabled'
_k='cmnMACMoveFeatureEnabled'
_j='cmnMacAddrRemovedEnable'
_i='cmnMacAddrLearntEnable'
_h='cmnNotificationsSent'
_g='cmnHistTableMaxLength'
_f='cmnNotificationsEnabled'
_e='cmnMacAddressesRemoved'
_d='cmnMacAddressesLearnt'
_c='cmnNotificationInterval'
_b='cmnGlobalFeatureEnabled'
_a='cmnHistIndex'
_Z='seconds'
_Y='ifIndex'
_X='IF-MIB'
_W='entPhysicalIndex'
_V='ENTITY-MIB'
_U='OctetString'
_T='cmnNotificationGroup'
_S='cmnInterfaceGroup'
_R='cmnGlobalGroup'
_Q='cmnUtilizationTimeStamp'
_P='cmnUtilizationUtilization'
_O='cmnMACThresholdLimit'
_N='cmnMACMoveTime'
_M='cmnMACMoveToPortId'
_L='cmnMACMoveFromPortId'
_K='cmnMACMoveVlanNumber'
_J='cmnMACMoveAddress'
_I='cmnHistTimestamp'
_H='cmnHistMacChangedMsg'
_G='Integer32'
_F='TruthValue'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-MAC-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_U,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percent,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','Percent')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
entPhysicalIndex,=mibBuilder.importSymbols(_V,_W)
ifIndex,=mibBuilder.importSymbols(_X,_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp',_F)
ciscoMacNotificationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,215))
if mibBuilder.loadTexts:ciscoMacNotificationMIB.setRevisions(('2007-06-11 00:00','2003-03-21 00:00','2001-10-22 00:00'))
_CiscoMacNotificationMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMacNotificationMIBObjects=_CiscoMacNotificationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,215,1))
_CmnGlobalObjects_ObjectIdentity=ObjectIdentity
cmnGlobalObjects=_CmnGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,215,1,1))
_CmnGlobalFeatureEnabled_Type=TruthValue
_CmnGlobalFeatureEnabled_Object=MibScalar
cmnGlobalFeatureEnabled=_CmnGlobalFeatureEnabled_Object((1,3,6,1,4,1,9,9,215,1,1,1),_CmnGlobalFeatureEnabled_Type())
cmnGlobalFeatureEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnGlobalFeatureEnabled.setStatus(_B)
class _CmnNotificationInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CmnNotificationInterval_Type.__name__=_E
_CmnNotificationInterval_Object=MibScalar
cmnNotificationInterval=_CmnNotificationInterval_Object((1,3,6,1,4,1,9,9,215,1,1,2),_CmnNotificationInterval_Type())
cmnNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnNotificationInterval.setStatus(_B)
if mibBuilder.loadTexts:cmnNotificationInterval.setUnits(_Z)
_CmnMacAddressesLearnt_Type=Counter32
_CmnMacAddressesLearnt_Object=MibScalar
cmnMacAddressesLearnt=_CmnMacAddressesLearnt_Object((1,3,6,1,4,1,9,9,215,1,1,3),_CmnMacAddressesLearnt_Type())
cmnMacAddressesLearnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMacAddressesLearnt.setStatus(_B)
_CmnMacAddressesRemoved_Type=Counter32
_CmnMacAddressesRemoved_Object=MibScalar
cmnMacAddressesRemoved=_CmnMacAddressesRemoved_Object((1,3,6,1,4,1,9,9,215,1,1,4),_CmnMacAddressesRemoved_Type())
cmnMacAddressesRemoved.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMacAddressesRemoved.setStatus(_B)
class _CmnNotificationsEnabled_Type(TruthValue):defaultValue=2
_CmnNotificationsEnabled_Type.__name__=_F
_CmnNotificationsEnabled_Object=MibScalar
cmnNotificationsEnabled=_CmnNotificationsEnabled_Object((1,3,6,1,4,1,9,9,215,1,1,5),_CmnNotificationsEnabled_Type())
cmnNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnNotificationsEnabled.setStatus(_B)
_CmnNotificationsSent_Type=Counter32
_CmnNotificationsSent_Object=MibScalar
cmnNotificationsSent=_CmnNotificationsSent_Object((1,3,6,1,4,1,9,9,215,1,1,6),_CmnNotificationsSent_Type())
cmnNotificationsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnNotificationsSent.setStatus(_B)
class _CmnHistTableMaxLength_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CmnHistTableMaxLength_Type.__name__=_E
_CmnHistTableMaxLength_Object=MibScalar
cmnHistTableMaxLength=_CmnHistTableMaxLength_Object((1,3,6,1,4,1,9,9,215,1,1,7),_CmnHistTableMaxLength_Type())
cmnHistTableMaxLength.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnHistTableMaxLength.setStatus(_B)
if mibBuilder.loadTexts:cmnHistTableMaxLength.setUnits('entries')
_CmnHistoryTable_Object=MibTable
cmnHistoryTable=_CmnHistoryTable_Object((1,3,6,1,4,1,9,9,215,1,1,8))
if mibBuilder.loadTexts:cmnHistoryTable.setStatus(_B)
_CmnHistoryEntry_Object=MibTableRow
cmnHistoryEntry=_CmnHistoryEntry_Object((1,3,6,1,4,1,9,9,215,1,1,8,1))
cmnHistoryEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:cmnHistoryEntry.setStatus(_B)
class _CmnHistIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CmnHistIndex_Type.__name__=_E
_CmnHistIndex_Object=MibTableColumn
cmnHistIndex=_CmnHistIndex_Object((1,3,6,1,4,1,9,9,215,1,1,8,1,1),_CmnHistIndex_Type())
cmnHistIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cmnHistIndex.setStatus(_B)
class _CmnHistMacChangedMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_CmnHistMacChangedMsg_Type.__name__=_U
_CmnHistMacChangedMsg_Object=MibTableColumn
cmnHistMacChangedMsg=_CmnHistMacChangedMsg_Object((1,3,6,1,4,1,9,9,215,1,1,8,1,2),_CmnHistMacChangedMsg_Type())
cmnHistMacChangedMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnHistMacChangedMsg.setStatus(_B)
_CmnHistTimestamp_Type=TimeStamp
_CmnHistTimestamp_Object=MibTableColumn
cmnHistTimestamp=_CmnHistTimestamp_Object((1,3,6,1,4,1,9,9,215,1,1,8,1,3),_CmnHistTimestamp_Type())
cmnHistTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnHistTimestamp.setStatus(_B)
_CmnInterfaceObjects_ObjectIdentity=ObjectIdentity
cmnInterfaceObjects=_CmnInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,215,1,2))
_CmnIfConfigTable_Object=MibTable
cmnIfConfigTable=_CmnIfConfigTable_Object((1,3,6,1,4,1,9,9,215,1,2,1))
if mibBuilder.loadTexts:cmnIfConfigTable.setStatus(_B)
_CmnIfConfigEntry_Object=MibTableRow
cmnIfConfigEntry=_CmnIfConfigEntry_Object((1,3,6,1,4,1,9,9,215,1,2,1,1))
cmnIfConfigEntry.setIndexNames((0,_X,_Y))
if mibBuilder.loadTexts:cmnIfConfigEntry.setStatus(_B)
class _CmnMacAddrLearntEnable_Type(TruthValue):defaultValue=2
_CmnMacAddrLearntEnable_Type.__name__=_F
_CmnMacAddrLearntEnable_Object=MibTableColumn
cmnMacAddrLearntEnable=_CmnMacAddrLearntEnable_Object((1,3,6,1,4,1,9,9,215,1,2,1,1,1),_CmnMacAddrLearntEnable_Type())
cmnMacAddrLearntEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMacAddrLearntEnable.setStatus(_B)
class _CmnMacAddrRemovedEnable_Type(TruthValue):defaultValue=2
_CmnMacAddrRemovedEnable_Type.__name__=_F
_CmnMacAddrRemovedEnable_Object=MibTableColumn
cmnMacAddrRemovedEnable=_CmnMacAddrRemovedEnable_Object((1,3,6,1,4,1,9,9,215,1,2,1,1,2),_CmnMacAddrRemovedEnable_Type())
cmnMacAddrRemovedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMacAddrRemovedEnable.setStatus(_B)
_CmnMACMoveObjects_ObjectIdentity=ObjectIdentity
cmnMACMoveObjects=_CmnMACMoveObjects_ObjectIdentity((1,3,6,1,4,1,9,9,215,1,3))
_CmnMACMoveFeatureEnabled_Type=TruthValue
_CmnMACMoveFeatureEnabled_Object=MibScalar
cmnMACMoveFeatureEnabled=_CmnMACMoveFeatureEnabled_Object((1,3,6,1,4,1,9,9,215,1,3,1),_CmnMACMoveFeatureEnabled_Type())
cmnMACMoveFeatureEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACMoveFeatureEnabled.setStatus(_B)
_CmnMACMoveNotificationsEnabled_Type=TruthValue
_CmnMACMoveNotificationsEnabled_Object=MibScalar
cmnMACMoveNotificationsEnabled=_CmnMACMoveNotificationsEnabled_Object((1,3,6,1,4,1,9,9,215,1,3,2),_CmnMACMoveNotificationsEnabled_Type())
cmnMACMoveNotificationsEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACMoveNotificationsEnabled.setStatus(_B)
_CmnMACMoveAddress_Type=MacAddress
_CmnMACMoveAddress_Object=MibScalar
cmnMACMoveAddress=_CmnMACMoveAddress_Object((1,3,6,1,4,1,9,9,215,1,3,3),_CmnMACMoveAddress_Type())
cmnMACMoveAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMACMoveAddress.setStatus(_B)
_CmnMACMoveVlanNumber_Type=VlanIndex
_CmnMACMoveVlanNumber_Object=MibScalar
cmnMACMoveVlanNumber=_CmnMACMoveVlanNumber_Object((1,3,6,1,4,1,9,9,215,1,3,4),_CmnMACMoveVlanNumber_Type())
cmnMACMoveVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMACMoveVlanNumber.setStatus(_B)
class _CmnMACMoveFromPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmnMACMoveFromPortId_Type.__name__=_G
_CmnMACMoveFromPortId_Object=MibScalar
cmnMACMoveFromPortId=_CmnMACMoveFromPortId_Object((1,3,6,1,4,1,9,9,215,1,3,5),_CmnMACMoveFromPortId_Type())
cmnMACMoveFromPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMACMoveFromPortId.setStatus(_B)
class _CmnMACMoveToPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CmnMACMoveToPortId_Type.__name__=_G
_CmnMACMoveToPortId_Object=MibScalar
cmnMACMoveToPortId=_CmnMACMoveToPortId_Object((1,3,6,1,4,1,9,9,215,1,3,6),_CmnMACMoveToPortId_Type())
cmnMACMoveToPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMACMoveToPortId.setStatus(_B)
_CmnMACMoveTime_Type=TimeStamp
_CmnMACMoveTime_Object=MibScalar
cmnMACMoveTime=_CmnMACMoveTime_Object((1,3,6,1,4,1,9,9,215,1,3,7),_CmnMACMoveTime_Type())
cmnMACMoveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnMACMoveTime.setStatus(_B)
_CmnMACThresholdObjects_ObjectIdentity=ObjectIdentity
cmnMACThresholdObjects=_CmnMACThresholdObjects_ObjectIdentity((1,3,6,1,4,1,9,9,215,1,4))
_CmnMACThresholdFeatureEnabled_Type=TruthValue
_CmnMACThresholdFeatureEnabled_Object=MibScalar
cmnMACThresholdFeatureEnabled=_CmnMACThresholdFeatureEnabled_Object((1,3,6,1,4,1,9,9,215,1,4,1),_CmnMACThresholdFeatureEnabled_Type())
cmnMACThresholdFeatureEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACThresholdFeatureEnabled.setStatus(_B)
_CmnMACThresholdLimit_Type=Percent
_CmnMACThresholdLimit_Object=MibScalar
cmnMACThresholdLimit=_CmnMACThresholdLimit_Object((1,3,6,1,4,1,9,9,215,1,4,2),_CmnMACThresholdLimit_Type())
cmnMACThresholdLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACThresholdLimit.setStatus(_B)
_CmnMACThresholdInterval_Type=Unsigned32
_CmnMACThresholdInterval_Object=MibScalar
cmnMACThresholdInterval=_CmnMACThresholdInterval_Object((1,3,6,1,4,1,9,9,215,1,4,3),_CmnMACThresholdInterval_Type())
cmnMACThresholdInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACThresholdInterval.setStatus(_B)
if mibBuilder.loadTexts:cmnMACThresholdInterval.setUnits(_Z)
_CmnMACThresholdNotifEnabled_Type=TruthValue
_CmnMACThresholdNotifEnabled_Object=MibScalar
cmnMACThresholdNotifEnabled=_CmnMACThresholdNotifEnabled_Object((1,3,6,1,4,1,9,9,215,1,4,4),_CmnMACThresholdNotifEnabled_Type())
cmnMACThresholdNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cmnMACThresholdNotifEnabled.setStatus(_B)
_CmnUtilizationTable_Object=MibTable
cmnUtilizationTable=_CmnUtilizationTable_Object((1,3,6,1,4,1,9,9,215,1,4,5))
if mibBuilder.loadTexts:cmnUtilizationTable.setStatus(_B)
_CmnUtilizationEntry_Object=MibTableRow
cmnUtilizationEntry=_CmnUtilizationEntry_Object((1,3,6,1,4,1,9,9,215,1,4,5,1))
cmnUtilizationEntry.setIndexNames((0,_V,_W))
if mibBuilder.loadTexts:cmnUtilizationEntry.setStatus(_B)
_CmnUtilizationEntries_Type=Unsigned32
_CmnUtilizationEntries_Object=MibTableColumn
cmnUtilizationEntries=_CmnUtilizationEntries_Object((1,3,6,1,4,1,9,9,215,1,4,5,1,1),_CmnUtilizationEntries_Type())
cmnUtilizationEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnUtilizationEntries.setStatus(_B)
_CmnUtilizationUtilization_Type=Percent
_CmnUtilizationUtilization_Object=MibTableColumn
cmnUtilizationUtilization=_CmnUtilizationUtilization_Object((1,3,6,1,4,1,9,9,215,1,4,5,1,2),_CmnUtilizationUtilization_Type())
cmnUtilizationUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnUtilizationUtilization.setStatus(_B)
_CmnUtilizationTimeStamp_Type=TimeStamp
_CmnUtilizationTimeStamp_Object=MibTableColumn
cmnUtilizationTimeStamp=_CmnUtilizationTimeStamp_Object((1,3,6,1,4,1,9,9,215,1,4,5,1,3),_CmnUtilizationTimeStamp_Type())
cmnUtilizationTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cmnUtilizationTimeStamp.setStatus(_B)
_CmnMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cmnMIBNotificationPrefix=_CmnMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,215,2))
_CmnMIBNotifications_ObjectIdentity=ObjectIdentity
cmnMIBNotifications=_CmnMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,215,2,0))
_CmnMIBConformance_ObjectIdentity=ObjectIdentity
cmnMIBConformance=_CmnMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,215,3))
_CmnMIBCompliances_ObjectIdentity=ObjectIdentity
cmnMIBCompliances=_CmnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,215,3,1))
_CmnMIBGroups_ObjectIdentity=ObjectIdentity
cmnMIBGroups=_CmnMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,215,3,2))
cmnGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,215,3,2,1))
cmnGlobalGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_H),(_A,_I),(_A,_h)))
if mibBuilder.loadTexts:cmnGlobalGroup.setStatus(_B)
cmnInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,215,3,2,2))
cmnInterfaceGroup.setObjects(*((_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cmnInterfaceGroup.setStatus(_B)
cmnMACMoveGroup=ObjectGroup((1,3,6,1,4,1,9,9,215,3,2,5))
cmnMACMoveGroup.setObjects(*((_A,_k),(_A,_l),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cmnMACMoveGroup.setStatus(_B)
cmnMACThresholdGroup=ObjectGroup((1,3,6,1,4,1,9,9,215,3,2,6))
cmnMACThresholdGroup.setObjects(*((_A,_m),(_A,_O),(_A,_n),(_A,_o),(_A,_p),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:cmnMACThresholdGroup.setStatus(_B)
cmnMacChangedNotification=NotificationType((1,3,6,1,4,1,9,9,215,2,0,1))
cmnMacChangedNotification.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:cmnMacChangedNotification.setStatus(_B)
cmnMacMoveNotification=NotificationType((1,3,6,1,4,1,9,9,215,2,0,2))
cmnMacMoveNotification.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cmnMacMoveNotification.setStatus(_B)
cmnMacThresholdExceedNotif=NotificationType((1,3,6,1,4,1,9,9,215,2,0,3))
cmnMacThresholdExceedNotif.setObjects(*((_A,_P),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:cmnMacThresholdExceedNotif.setStatus(_B)
cmnNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,215,3,2,3))
cmnNotificationGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:cmnNotificationGroup.setStatus(_B)
cmnMACMoveNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,215,3,2,7))
cmnMACMoveNotifGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:cmnMACMoveNotifGroup.setStatus(_B)
cmnMACThresholdNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,215,3,2,8))
cmnMACThresholdNotifGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:cmnMACThresholdNotifGroup.setStatus(_B)
cmnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,215,3,1,1))
cmnMIBCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cmnMIBCompliance.setStatus('deprecated')
cmnMIBComplianceVer1=ModuleCompliance((1,3,6,1,4,1,9,9,215,3,1,2))
cmnMIBComplianceVer1.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cmnMIBComplianceVer1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoMacNotificationMIB':ciscoMacNotificationMIB,'ciscoMacNotificationMIBObjects':ciscoMacNotificationMIBObjects,'cmnGlobalObjects':cmnGlobalObjects,_b:cmnGlobalFeatureEnabled,_c:cmnNotificationInterval,_d:cmnMacAddressesLearnt,_e:cmnMacAddressesRemoved,_f:cmnNotificationsEnabled,_h:cmnNotificationsSent,_g:cmnHistTableMaxLength,'cmnHistoryTable':cmnHistoryTable,'cmnHistoryEntry':cmnHistoryEntry,_a:cmnHistIndex,_H:cmnHistMacChangedMsg,_I:cmnHistTimestamp,'cmnInterfaceObjects':cmnInterfaceObjects,'cmnIfConfigTable':cmnIfConfigTable,'cmnIfConfigEntry':cmnIfConfigEntry,_i:cmnMacAddrLearntEnable,_j:cmnMacAddrRemovedEnable,'cmnMACMoveObjects':cmnMACMoveObjects,_k:cmnMACMoveFeatureEnabled,_l:cmnMACMoveNotificationsEnabled,_J:cmnMACMoveAddress,_K:cmnMACMoveVlanNumber,_L:cmnMACMoveFromPortId,_M:cmnMACMoveToPortId,_N:cmnMACMoveTime,'cmnMACThresholdObjects':cmnMACThresholdObjects,_m:cmnMACThresholdFeatureEnabled,_O:cmnMACThresholdLimit,_n:cmnMACThresholdInterval,_o:cmnMACThresholdNotifEnabled,'cmnUtilizationTable':cmnUtilizationTable,'cmnUtilizationEntry':cmnUtilizationEntry,_p:cmnUtilizationEntries,_P:cmnUtilizationUtilization,_Q:cmnUtilizationTimeStamp,'cmnMIBNotificationPrefix':cmnMIBNotificationPrefix,'cmnMIBNotifications':cmnMIBNotifications,_q:cmnMacChangedNotification,_r:cmnMacMoveNotification,_s:cmnMacThresholdExceedNotif,'cmnMIBConformance':cmnMIBConformance,'cmnMIBCompliances':cmnMIBCompliances,'cmnMIBCompliance':cmnMIBCompliance,'cmnMIBComplianceVer1':cmnMIBComplianceVer1,'cmnMIBGroups':cmnMIBGroups,_R:cmnGlobalGroup,_S:cmnInterfaceGroup,_T:cmnNotificationGroup,_t:cmnMACMoveGroup,_u:cmnMACThresholdGroup,_v:cmnMACMoveNotifGroup,_w:cmnMACThresholdNotifGroup})