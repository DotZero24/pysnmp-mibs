_o='dcpAlarmActiveListGroupV2'
_n='dcpAlarmLogListGroupV1'
_m='dcpAlarmNotificationWarning'
_l='dcpAlarmNotificationMinor'
_k='dcpAlarmNotificationMajor'
_j='dcpAlarmNotificationCritical'
_i='dcpAlarmNotificationCleared'
_h='dcpAlarmActiveListInterfaceDescription'
_g='dcpAlarmGeneralLastTrapSeqNumber'
_f='dcpAlarmGeneralNumberLogList'
_e='dcpAlarmGeneralNumberActiveList'
_d='dcpAlarmGeneralActiveWarning'
_c='dcpAlarmGeneralActiveMinor'
_b='dcpAlarmGeneralActiveMajor'
_a='dcpAlarmGeneralActiveCritical'
_Z='dcpAlarmGeneralHighestSeverity'
_Y='dcpAlarmLogListGroupV2'
_X='dcpAlarmActiveListGroupV1'
_W='dcpAlarmActiveListSeqNumber'
_V='dcpAlarmActiveListStartTime'
_U='dcpAlarmActiveListSeverity'
_T='dcpAlarmActiveListText'
_S='dcpAlarmActiveListInterfaceName'
_R='dcpAlarmActiveListLocation'
_Q='DisplayString'
_P='dcpAlarmNotificationGroupV1'
_O='dcpAlarmGeneralGroupV1'
_N='dcpAlarmLogListEndTime'
_M='deprecated'
_L='dcpAlarmActiveListIndex'
_K='dcpAlarmLogListInterfaceDescription'
_J='dcpAlarmLogListSeqNumber'
_I='dcpAlarmLogListStartTime'
_H='dcpAlarmLogListSeverity'
_G='dcpAlarmLogListText'
_F='dcpAlarmLogListInterfaceName'
_E='dcpAlarmLogListLocation'
_D='dcpAlarmLogListIndex'
_C='read-only'
_B='current'
_A='DCP-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_Q,'PhysAddress','TextualConvention')
ItuPerceivedSeverity,=mibBuilder.importSymbols('SO-TC-MIB','ItuPerceivedSeverity')
dcpAlarm=ModuleIdentity((1,3,6,1,4,1,30826,2,2,2))
if mibBuilder.loadTexts:dcpAlarm.setRevisions(('2020-06-24 08:00','2018-10-08 14:44'))
class DcpAlarmIndex(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,29999))
_DcpAlarmGeneral_ObjectIdentity=ObjectIdentity
dcpAlarmGeneral=_DcpAlarmGeneral_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,1))
_DcpAlarmGeneralList_ObjectIdentity=ObjectIdentity
dcpAlarmGeneralList=_DcpAlarmGeneralList_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,1,1))
_DcpAlarmGeneralHighestSeverity_Type=ItuPerceivedSeverity
_DcpAlarmGeneralHighestSeverity_Object=MibScalar
dcpAlarmGeneralHighestSeverity=_DcpAlarmGeneralHighestSeverity_Object((1,3,6,1,4,1,30826,2,2,2,1,1,1),_DcpAlarmGeneralHighestSeverity_Type())
dcpAlarmGeneralHighestSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralHighestSeverity.setStatus(_B)
_DcpAlarmGeneralActiveCritical_Type=Unsigned32
_DcpAlarmGeneralActiveCritical_Object=MibScalar
dcpAlarmGeneralActiveCritical=_DcpAlarmGeneralActiveCritical_Object((1,3,6,1,4,1,30826,2,2,2,1,1,2),_DcpAlarmGeneralActiveCritical_Type())
dcpAlarmGeneralActiveCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralActiveCritical.setStatus(_B)
_DcpAlarmGeneralActiveMajor_Type=Unsigned32
_DcpAlarmGeneralActiveMajor_Object=MibScalar
dcpAlarmGeneralActiveMajor=_DcpAlarmGeneralActiveMajor_Object((1,3,6,1,4,1,30826,2,2,2,1,1,3),_DcpAlarmGeneralActiveMajor_Type())
dcpAlarmGeneralActiveMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralActiveMajor.setStatus(_B)
_DcpAlarmGeneralActiveMinor_Type=Unsigned32
_DcpAlarmGeneralActiveMinor_Object=MibScalar
dcpAlarmGeneralActiveMinor=_DcpAlarmGeneralActiveMinor_Object((1,3,6,1,4,1,30826,2,2,2,1,1,4),_DcpAlarmGeneralActiveMinor_Type())
dcpAlarmGeneralActiveMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralActiveMinor.setStatus(_B)
_DcpAlarmGeneralActiveWarning_Type=Unsigned32
_DcpAlarmGeneralActiveWarning_Object=MibScalar
dcpAlarmGeneralActiveWarning=_DcpAlarmGeneralActiveWarning_Object((1,3,6,1,4,1,30826,2,2,2,1,1,5),_DcpAlarmGeneralActiveWarning_Type())
dcpAlarmGeneralActiveWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralActiveWarning.setStatus(_B)
_DcpAlarmGeneralNumberActiveList_Type=Unsigned32
_DcpAlarmGeneralNumberActiveList_Object=MibScalar
dcpAlarmGeneralNumberActiveList=_DcpAlarmGeneralNumberActiveList_Object((1,3,6,1,4,1,30826,2,2,2,1,1,6),_DcpAlarmGeneralNumberActiveList_Type())
dcpAlarmGeneralNumberActiveList.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralNumberActiveList.setStatus(_B)
_DcpAlarmGeneralNumberLogList_Type=Unsigned32
_DcpAlarmGeneralNumberLogList_Object=MibScalar
dcpAlarmGeneralNumberLogList=_DcpAlarmGeneralNumberLogList_Object((1,3,6,1,4,1,30826,2,2,2,1,1,7),_DcpAlarmGeneralNumberLogList_Type())
dcpAlarmGeneralNumberLogList.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralNumberLogList.setStatus(_B)
_DcpAlarmGeneralLastTrapSeqNumber_Type=Unsigned32
_DcpAlarmGeneralLastTrapSeqNumber_Object=MibScalar
dcpAlarmGeneralLastTrapSeqNumber=_DcpAlarmGeneralLastTrapSeqNumber_Object((1,3,6,1,4,1,30826,2,2,2,1,1,8),_DcpAlarmGeneralLastTrapSeqNumber_Type())
dcpAlarmGeneralLastTrapSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmGeneralLastTrapSeqNumber.setStatus(_B)
_DcpAlarmObjects_ObjectIdentity=ObjectIdentity
dcpAlarmObjects=_DcpAlarmObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,2))
_DcpAlarmActiveListTable_Object=MibTable
dcpAlarmActiveListTable=_DcpAlarmActiveListTable_Object((1,3,6,1,4,1,30826,2,2,2,2,1))
if mibBuilder.loadTexts:dcpAlarmActiveListTable.setStatus(_B)
_DcpAlarmActiveListEntry_Object=MibTableRow
dcpAlarmActiveListEntry=_DcpAlarmActiveListEntry_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1))
dcpAlarmActiveListEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:dcpAlarmActiveListEntry.setStatus(_B)
_DcpAlarmActiveListIndex_Type=DcpAlarmIndex
_DcpAlarmActiveListIndex_Object=MibTableColumn
dcpAlarmActiveListIndex=_DcpAlarmActiveListIndex_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,1),_DcpAlarmActiveListIndex_Type())
dcpAlarmActiveListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListIndex.setStatus(_B)
_DcpAlarmActiveListLocation_Type=DisplayString
_DcpAlarmActiveListLocation_Object=MibTableColumn
dcpAlarmActiveListLocation=_DcpAlarmActiveListLocation_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,2),_DcpAlarmActiveListLocation_Type())
dcpAlarmActiveListLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListLocation.setStatus(_B)
_DcpAlarmActiveListInterfaceName_Type=DisplayString
_DcpAlarmActiveListInterfaceName_Object=MibTableColumn
dcpAlarmActiveListInterfaceName=_DcpAlarmActiveListInterfaceName_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,3),_DcpAlarmActiveListInterfaceName_Type())
dcpAlarmActiveListInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListInterfaceName.setStatus(_B)
_DcpAlarmActiveListText_Type=DisplayString
_DcpAlarmActiveListText_Object=MibTableColumn
dcpAlarmActiveListText=_DcpAlarmActiveListText_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,4),_DcpAlarmActiveListText_Type())
dcpAlarmActiveListText.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListText.setStatus(_B)
_DcpAlarmActiveListSeverity_Type=ItuPerceivedSeverity
_DcpAlarmActiveListSeverity_Object=MibTableColumn
dcpAlarmActiveListSeverity=_DcpAlarmActiveListSeverity_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,5),_DcpAlarmActiveListSeverity_Type())
dcpAlarmActiveListSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListSeverity.setStatus(_B)
_DcpAlarmActiveListStartTime_Type=DateAndTime
_DcpAlarmActiveListStartTime_Object=MibTableColumn
dcpAlarmActiveListStartTime=_DcpAlarmActiveListStartTime_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,6),_DcpAlarmActiveListStartTime_Type())
dcpAlarmActiveListStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListStartTime.setStatus(_B)
_DcpAlarmActiveListSeqNumber_Type=Unsigned32
_DcpAlarmActiveListSeqNumber_Object=MibTableColumn
dcpAlarmActiveListSeqNumber=_DcpAlarmActiveListSeqNumber_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,7),_DcpAlarmActiveListSeqNumber_Type())
dcpAlarmActiveListSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListSeqNumber.setStatus(_B)
class _DcpAlarmActiveListInterfaceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DcpAlarmActiveListInterfaceDescription_Type.__name__=_Q
_DcpAlarmActiveListInterfaceDescription_Object=MibTableColumn
dcpAlarmActiveListInterfaceDescription=_DcpAlarmActiveListInterfaceDescription_Object((1,3,6,1,4,1,30826,2,2,2,2,1,1,8),_DcpAlarmActiveListInterfaceDescription_Type())
dcpAlarmActiveListInterfaceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmActiveListInterfaceDescription.setStatus(_B)
_DcpAlarmLogTable_Object=MibTable
dcpAlarmLogTable=_DcpAlarmLogTable_Object((1,3,6,1,4,1,30826,2,2,2,2,2))
if mibBuilder.loadTexts:dcpAlarmLogTable.setStatus(_B)
_DcpAlarmLogEntry_Object=MibTableRow
dcpAlarmLogEntry=_DcpAlarmLogEntry_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1))
dcpAlarmLogEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:dcpAlarmLogEntry.setStatus(_B)
_DcpAlarmLogListIndex_Type=DcpAlarmIndex
_DcpAlarmLogListIndex_Object=MibTableColumn
dcpAlarmLogListIndex=_DcpAlarmLogListIndex_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,1),_DcpAlarmLogListIndex_Type())
dcpAlarmLogListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListIndex.setStatus(_B)
_DcpAlarmLogListLocation_Type=DisplayString
_DcpAlarmLogListLocation_Object=MibTableColumn
dcpAlarmLogListLocation=_DcpAlarmLogListLocation_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,2),_DcpAlarmLogListLocation_Type())
dcpAlarmLogListLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListLocation.setStatus(_B)
_DcpAlarmLogListInterfaceName_Type=DisplayString
_DcpAlarmLogListInterfaceName_Object=MibTableColumn
dcpAlarmLogListInterfaceName=_DcpAlarmLogListInterfaceName_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,3),_DcpAlarmLogListInterfaceName_Type())
dcpAlarmLogListInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListInterfaceName.setStatus(_B)
_DcpAlarmLogListText_Type=DisplayString
_DcpAlarmLogListText_Object=MibTableColumn
dcpAlarmLogListText=_DcpAlarmLogListText_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,4),_DcpAlarmLogListText_Type())
dcpAlarmLogListText.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListText.setStatus(_B)
_DcpAlarmLogListSeverity_Type=ItuPerceivedSeverity
_DcpAlarmLogListSeverity_Object=MibTableColumn
dcpAlarmLogListSeverity=_DcpAlarmLogListSeverity_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,5),_DcpAlarmLogListSeverity_Type())
dcpAlarmLogListSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListSeverity.setStatus(_B)
_DcpAlarmLogListStartTime_Type=DateAndTime
_DcpAlarmLogListStartTime_Object=MibTableColumn
dcpAlarmLogListStartTime=_DcpAlarmLogListStartTime_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,6),_DcpAlarmLogListStartTime_Type())
dcpAlarmLogListStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListStartTime.setStatus(_B)
_DcpAlarmLogListEndTime_Type=DateAndTime
_DcpAlarmLogListEndTime_Object=MibTableColumn
dcpAlarmLogListEndTime=_DcpAlarmLogListEndTime_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,7),_DcpAlarmLogListEndTime_Type())
dcpAlarmLogListEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListEndTime.setStatus(_B)
_DcpAlarmLogListSeqNumber_Type=Unsigned32
_DcpAlarmLogListSeqNumber_Object=MibTableColumn
dcpAlarmLogListSeqNumber=_DcpAlarmLogListSeqNumber_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,8),_DcpAlarmLogListSeqNumber_Type())
dcpAlarmLogListSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListSeqNumber.setStatus(_B)
class _DcpAlarmLogListInterfaceDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DcpAlarmLogListInterfaceDescription_Type.__name__=_Q
_DcpAlarmLogListInterfaceDescription_Object=MibTableColumn
dcpAlarmLogListInterfaceDescription=_DcpAlarmLogListInterfaceDescription_Object((1,3,6,1,4,1,30826,2,2,2,2,2,1,9),_DcpAlarmLogListInterfaceDescription_Type())
dcpAlarmLogListInterfaceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:dcpAlarmLogListInterfaceDescription.setStatus(_B)
_DcpAlarmMIBNotifications_ObjectIdentity=ObjectIdentity
dcpAlarmMIBNotifications=_DcpAlarmMIBNotifications_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,3))
_DcpAlarmNotification_ObjectIdentity=ObjectIdentity
dcpAlarmNotification=_DcpAlarmNotification_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,3,0))
_DcpAlarmMIBCompliance_ObjectIdentity=ObjectIdentity
dcpAlarmMIBCompliance=_DcpAlarmMIBCompliance_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,4))
_DcpAlarmMIBGroups_ObjectIdentity=ObjectIdentity
dcpAlarmMIBGroups=_DcpAlarmMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,4,1))
_DcpAlarmMIBCompliances_ObjectIdentity=ObjectIdentity
dcpAlarmMIBCompliances=_DcpAlarmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30826,2,2,2,4,2))
dcpAlarmGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,2,4,1,1))
dcpAlarmGeneralGroupV1.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:dcpAlarmGeneralGroupV1.setStatus(_B)
dcpAlarmActiveListGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,2,4,1,3))
dcpAlarmActiveListGroupV1.setObjects(*((_A,_L),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:dcpAlarmActiveListGroupV1.setStatus(_M)
dcpAlarmLogListGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,2,4,1,4))
dcpAlarmLogListGroupV1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_J)))
if mibBuilder.loadTexts:dcpAlarmLogListGroupV1.setStatus(_M)
dcpAlarmLogListGroupV2=ObjectGroup((1,3,6,1,4,1,30826,2,2,2,4,1,5))
dcpAlarmLogListGroupV2.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmLogListGroupV2.setStatus(_B)
dcpAlarmActiveListGroupV2=ObjectGroup((1,3,6,1,4,1,30826,2,2,2,4,1,6))
dcpAlarmActiveListGroupV2.setObjects(*((_A,_L),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_h)))
if mibBuilder.loadTexts:dcpAlarmActiveListGroupV2.setStatus(_B)
dcpAlarmNotificationCleared=NotificationType((1,3,6,1,4,1,30826,2,2,2,3,0,1))
dcpAlarmNotificationCleared.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmNotificationCleared.setStatus(_B)
dcpAlarmNotificationCritical=NotificationType((1,3,6,1,4,1,30826,2,2,2,3,0,2))
dcpAlarmNotificationCritical.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmNotificationCritical.setStatus(_B)
dcpAlarmNotificationMajor=NotificationType((1,3,6,1,4,1,30826,2,2,2,3,0,3))
dcpAlarmNotificationMajor.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmNotificationMajor.setStatus(_B)
dcpAlarmNotificationMinor=NotificationType((1,3,6,1,4,1,30826,2,2,2,3,0,4))
dcpAlarmNotificationMinor.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmNotificationMinor.setStatus(_B)
dcpAlarmNotificationWarning=NotificationType((1,3,6,1,4,1,30826,2,2,2,3,0,5))
dcpAlarmNotificationWarning.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:dcpAlarmNotificationWarning.setStatus(_B)
dcpAlarmNotificationGroupV1=NotificationGroup((1,3,6,1,4,1,30826,2,2,2,4,1,2))
dcpAlarmNotificationGroupV1.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:dcpAlarmNotificationGroupV1.setStatus(_B)
dcpAlarmBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,2,2,2,4,2,1))
dcpAlarmBasicComplV1.setObjects(*((_A,_O),(_A,_P),(_A,_X),(_A,_n)))
if mibBuilder.loadTexts:dcpAlarmBasicComplV1.setStatus(_M)
dcpAlarmBasicComplV2=ModuleCompliance((1,3,6,1,4,1,30826,2,2,2,4,2,2))
dcpAlarmBasicComplV2.setObjects(*((_A,_O),(_A,_P),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:dcpAlarmBasicComplV2.setStatus(_M)
dcpAlarmBasicComplV3=ModuleCompliance((1,3,6,1,4,1,30826,2,2,2,4,2,3))
dcpAlarmBasicComplV3.setObjects(*((_A,_O),(_A,_P),(_A,_o),(_A,_Y)))
if mibBuilder.loadTexts:dcpAlarmBasicComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DcpAlarmIndex':DcpAlarmIndex,'dcpAlarm':dcpAlarm,'dcpAlarmGeneral':dcpAlarmGeneral,'dcpAlarmGeneralList':dcpAlarmGeneralList,_Z:dcpAlarmGeneralHighestSeverity,_a:dcpAlarmGeneralActiveCritical,_b:dcpAlarmGeneralActiveMajor,_c:dcpAlarmGeneralActiveMinor,_d:dcpAlarmGeneralActiveWarning,_e:dcpAlarmGeneralNumberActiveList,_f:dcpAlarmGeneralNumberLogList,_g:dcpAlarmGeneralLastTrapSeqNumber,'dcpAlarmObjects':dcpAlarmObjects,'dcpAlarmActiveListTable':dcpAlarmActiveListTable,'dcpAlarmActiveListEntry':dcpAlarmActiveListEntry,_L:dcpAlarmActiveListIndex,_R:dcpAlarmActiveListLocation,_S:dcpAlarmActiveListInterfaceName,_T:dcpAlarmActiveListText,_U:dcpAlarmActiveListSeverity,_V:dcpAlarmActiveListStartTime,_W:dcpAlarmActiveListSeqNumber,_h:dcpAlarmActiveListInterfaceDescription,'dcpAlarmLogTable':dcpAlarmLogTable,'dcpAlarmLogEntry':dcpAlarmLogEntry,_D:dcpAlarmLogListIndex,_E:dcpAlarmLogListLocation,_F:dcpAlarmLogListInterfaceName,_G:dcpAlarmLogListText,_H:dcpAlarmLogListSeverity,_I:dcpAlarmLogListStartTime,_N:dcpAlarmLogListEndTime,_J:dcpAlarmLogListSeqNumber,_K:dcpAlarmLogListInterfaceDescription,'dcpAlarmMIBNotifications':dcpAlarmMIBNotifications,'dcpAlarmNotification':dcpAlarmNotification,_i:dcpAlarmNotificationCleared,_j:dcpAlarmNotificationCritical,_k:dcpAlarmNotificationMajor,_l:dcpAlarmNotificationMinor,_m:dcpAlarmNotificationWarning,'dcpAlarmMIBCompliance':dcpAlarmMIBCompliance,'dcpAlarmMIBGroups':dcpAlarmMIBGroups,_O:dcpAlarmGeneralGroupV1,_P:dcpAlarmNotificationGroupV1,_X:dcpAlarmActiveListGroupV1,_n:dcpAlarmLogListGroupV1,_Y:dcpAlarmLogListGroupV2,_o:dcpAlarmActiveListGroupV2,'dcpAlarmMIBCompliances':dcpAlarmMIBCompliances,'dcpAlarmBasicComplV1':dcpAlarmBasicComplV1,'dcpAlarmBasicComplV2':dcpAlarmBasicComplV2,'dcpAlarmBasicComplV3':dcpAlarmBasicComplV3})