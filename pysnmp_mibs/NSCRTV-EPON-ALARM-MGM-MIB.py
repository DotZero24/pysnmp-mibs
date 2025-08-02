_T='eponTrapCorrelationId'
_S='eponTrapSeverity'
_R='eponManagementAddrName'
_Q='eventSeqNum'
_P='historyAlarmRaisingNumber'
_O='historyAlarmSeqNum'
_N='activeAlarmRaisingNumber'
_M='activeAlarmSeqNum'
_L='eponTrapAdditionalText'
_K='eponTrapInstance'
_J='eponTrapCode'
_I='eponTrapOccurTime'
_H='eponTrapSequenceNumber'
_G='read-create'
_F='not-accessible'
_E='accessible-for-notify'
_D='OctetString'
_C='NSCRTV-EPON-ALARM-MGM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,eponAlarmObjGroup,eponAlarmTree,eponManagementObjGroup,eponTrapObjectGroup=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','eponAlarmObjGroup','eponAlarmTree','eponManagementObjGroup','eponTrapObjectGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_EponNotifications_ObjectIdentity=ObjectIdentity
eponNotifications=_EponNotifications_ObjectIdentity((1,3,6,1,4,1,17409,2,2,11,1,1))
_EponTrapObjects_ObjectIdentity=ObjectIdentity
eponTrapObjects=_EponTrapObjects_ObjectIdentity((1,3,6,1,4,1,17409,2,2,11,1,2))
_EponTrapInstance_Type=EponAlarmInstance
_EponTrapInstance_Object=MibScalar
eponTrapInstance=_EponTrapInstance_Object((1,3,6,1,4,1,17409,2,2,11,1,2,1),_EponTrapInstance_Type())
eponTrapInstance.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapInstance.setStatus(_A)
_EponTrapCorrelationId_Type=Unsigned32
_EponTrapCorrelationId_Object=MibScalar
eponTrapCorrelationId=_EponTrapCorrelationId_Object((1,3,6,1,4,1,17409,2,2,11,1,2,2),_EponTrapCorrelationId_Type())
eponTrapCorrelationId.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapCorrelationId.setStatus(_A)
class _EponTrapAdditionalText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_EponTrapAdditionalText_Type.__name__=_D
_EponTrapAdditionalText_Object=MibScalar
eponTrapAdditionalText=_EponTrapAdditionalText_Object((1,3,6,1,4,1,17409,2,2,11,1,2,3),_EponTrapAdditionalText_Type())
eponTrapAdditionalText.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapAdditionalText.setStatus(_A)
_EponTrapCode_Type=EponAlarmCode
_EponTrapCode_Object=MibScalar
eponTrapCode=_EponTrapCode_Object((1,3,6,1,4,1,17409,2,2,11,1,2,4),_EponTrapCode_Type())
eponTrapCode.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapCode.setStatus(_A)
_EponTrapSeverity_Type=EponSeverityType
_EponTrapSeverity_Object=MibScalar
eponTrapSeverity=_EponTrapSeverity_Object((1,3,6,1,4,1,17409,2,2,11,1,2,5),_EponTrapSeverity_Type())
eponTrapSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapSeverity.setStatus(_A)
_EponTrapOccurTime_Type=DateAndTime
_EponTrapOccurTime_Object=MibScalar
eponTrapOccurTime=_EponTrapOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,1,2,6),_EponTrapOccurTime_Type())
eponTrapOccurTime.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapOccurTime.setStatus(_A)
_EponTrapSequenceNumber_Type=Unsigned32
_EponTrapSequenceNumber_Object=MibScalar
eponTrapSequenceNumber=_EponTrapSequenceNumber_Object((1,3,6,1,4,1,17409,2,2,11,1,2,7),_EponTrapSequenceNumber_Type())
eponTrapSequenceNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:eponTrapSequenceNumber.setStatus(_A)
_ActiveAlarmTable_Object=MibTable
activeAlarmTable=_ActiveAlarmTable_Object((1,3,6,1,4,1,17409,2,2,11,2,1))
if mibBuilder.loadTexts:activeAlarmTable.setStatus(_A)
_ActiveAlarmEntry_Object=MibTableRow
activeAlarmEntry=_ActiveAlarmEntry_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1))
activeAlarmEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:activeAlarmEntry.setStatus(_A)
_ActiveAlarmSeqNum_Type=Unsigned32
_ActiveAlarmSeqNum_Object=MibTableColumn
activeAlarmSeqNum=_ActiveAlarmSeqNum_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,1),_ActiveAlarmSeqNum_Type())
activeAlarmSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:activeAlarmSeqNum.setStatus(_A)
_ActiveAlarmCode_Type=EponAlarmCode
_ActiveAlarmCode_Object=MibTableColumn
activeAlarmCode=_ActiveAlarmCode_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,2),_ActiveAlarmCode_Type())
activeAlarmCode.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmCode.setStatus(_A)
_ActiveAlarmInstance_Type=EponAlarmInstance
_ActiveAlarmInstance_Object=MibTableColumn
activeAlarmInstance=_ActiveAlarmInstance_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,3),_ActiveAlarmInstance_Type())
activeAlarmInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmInstance.setStatus(_A)
_ActiveAlarmSeverity_Type=EponSeverityType
_ActiveAlarmSeverity_Object=MibTableColumn
activeAlarmSeverity=_ActiveAlarmSeverity_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,4),_ActiveAlarmSeverity_Type())
activeAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmSeverity.setStatus(_A)
_ActiveAlarmRaisingNumber_Type=Unsigned32
_ActiveAlarmRaisingNumber_Object=MibTableColumn
activeAlarmRaisingNumber=_ActiveAlarmRaisingNumber_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,5),_ActiveAlarmRaisingNumber_Type())
activeAlarmRaisingNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:activeAlarmRaisingNumber.setStatus(_A)
_ActiveAlarmFirstOccurTime_Type=DateAndTime
_ActiveAlarmFirstOccurTime_Object=MibTableColumn
activeAlarmFirstOccurTime=_ActiveAlarmFirstOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,6),_ActiveAlarmFirstOccurTime_Type())
activeAlarmFirstOccurTime.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmFirstOccurTime.setStatus(_A)
_ActiveAlarmLastOccurTime_Type=DateAndTime
_ActiveAlarmLastOccurTime_Object=MibTableColumn
activeAlarmLastOccurTime=_ActiveAlarmLastOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,7),_ActiveAlarmLastOccurTime_Type())
activeAlarmLastOccurTime.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmLastOccurTime.setStatus(_A)
_ActiveAlarmRepeats_Type=Counter32
_ActiveAlarmRepeats_Object=MibTableColumn
activeAlarmRepeats=_ActiveAlarmRepeats_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,8),_ActiveAlarmRepeats_Type())
activeAlarmRepeats.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmRepeats.setStatus(_A)
_ActiveAlarmConfirm_Type=TruthValue
_ActiveAlarmConfirm_Object=MibTableColumn
activeAlarmConfirm=_ActiveAlarmConfirm_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,9),_ActiveAlarmConfirm_Type())
activeAlarmConfirm.setMaxAccess('read-write')
if mibBuilder.loadTexts:activeAlarmConfirm.setStatus(_A)
class _ActiveAlarmAdditionalText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ActiveAlarmAdditionalText_Type.__name__=_D
_ActiveAlarmAdditionalText_Object=MibTableColumn
activeAlarmAdditionalText=_ActiveAlarmAdditionalText_Object((1,3,6,1,4,1,17409,2,2,11,2,1,1,10),_ActiveAlarmAdditionalText_Type())
activeAlarmAdditionalText.setMaxAccess(_B)
if mibBuilder.loadTexts:activeAlarmAdditionalText.setStatus(_A)
_HistoryAlarmTable_Object=MibTable
historyAlarmTable=_HistoryAlarmTable_Object((1,3,6,1,4,1,17409,2,2,11,2,2))
if mibBuilder.loadTexts:historyAlarmTable.setStatus(_A)
_HistoryAlarmEntry_Object=MibTableRow
historyAlarmEntry=_HistoryAlarmEntry_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1))
historyAlarmEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:historyAlarmEntry.setStatus(_A)
_HistoryAlarmSeqNum_Type=Unsigned32
_HistoryAlarmSeqNum_Object=MibTableColumn
historyAlarmSeqNum=_HistoryAlarmSeqNum_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,1),_HistoryAlarmSeqNum_Type())
historyAlarmSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:historyAlarmSeqNum.setStatus(_A)
_HistoryAlarmCode_Type=EponAlarmCode
_HistoryAlarmCode_Object=MibTableColumn
historyAlarmCode=_HistoryAlarmCode_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,2),_HistoryAlarmCode_Type())
historyAlarmCode.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmCode.setStatus(_A)
_HistoryAlarmInstance_Type=EponAlarmInstance
_HistoryAlarmInstance_Object=MibTableColumn
historyAlarmInstance=_HistoryAlarmInstance_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,3),_HistoryAlarmInstance_Type())
historyAlarmInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmInstance.setStatus(_A)
_HistoryAlarmSeverity_Type=EponSeverityType
_HistoryAlarmSeverity_Object=MibTableColumn
historyAlarmSeverity=_HistoryAlarmSeverity_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,4),_HistoryAlarmSeverity_Type())
historyAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmSeverity.setStatus(_A)
_HistoryAlarmRaisingNumber_Type=Unsigned32
_HistoryAlarmRaisingNumber_Object=MibTableColumn
historyAlarmRaisingNumber=_HistoryAlarmRaisingNumber_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,5),_HistoryAlarmRaisingNumber_Type())
historyAlarmRaisingNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:historyAlarmRaisingNumber.setStatus(_A)
_HistoryAlarmFirstOccurTime_Type=DateAndTime
_HistoryAlarmFirstOccurTime_Object=MibTableColumn
historyAlarmFirstOccurTime=_HistoryAlarmFirstOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,6),_HistoryAlarmFirstOccurTime_Type())
historyAlarmFirstOccurTime.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmFirstOccurTime.setStatus(_A)
_HistoryAlarmLastOccurTime_Type=DateAndTime
_HistoryAlarmLastOccurTime_Object=MibTableColumn
historyAlarmLastOccurTime=_HistoryAlarmLastOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,7),_HistoryAlarmLastOccurTime_Type())
historyAlarmLastOccurTime.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmLastOccurTime.setStatus(_A)
_HistoryAlarmRepeats_Type=Counter32
_HistoryAlarmRepeats_Object=MibTableColumn
historyAlarmRepeats=_HistoryAlarmRepeats_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,8),_HistoryAlarmRepeats_Type())
historyAlarmRepeats.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmRepeats.setStatus(_A)
_HistoryAlarmCorrelationId_Type=Unsigned32
_HistoryAlarmCorrelationId_Object=MibTableColumn
historyAlarmCorrelationId=_HistoryAlarmCorrelationId_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,9),_HistoryAlarmCorrelationId_Type())
historyAlarmCorrelationId.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmCorrelationId.setStatus(_A)
class _HistoryAlarmAdditionalText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HistoryAlarmAdditionalText_Type.__name__=_D
_HistoryAlarmAdditionalText_Object=MibTableColumn
historyAlarmAdditionalText=_HistoryAlarmAdditionalText_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,10),_HistoryAlarmAdditionalText_Type())
historyAlarmAdditionalText.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmAdditionalText.setStatus(_A)
_HistoryAlarmClearTime_Type=DateAndTime
_HistoryAlarmClearTime_Object=MibTableColumn
historyAlarmClearTime=_HistoryAlarmClearTime_Object((1,3,6,1,4,1,17409,2,2,11,2,2,1,11),_HistoryAlarmClearTime_Type())
historyAlarmClearTime.setMaxAccess(_B)
if mibBuilder.loadTexts:historyAlarmClearTime.setStatus(_A)
_EventLogTable_Object=MibTable
eventLogTable=_EventLogTable_Object((1,3,6,1,4,1,17409,2,2,11,2,3))
if mibBuilder.loadTexts:eventLogTable.setStatus(_A)
_EventLogEntry_Object=MibTableRow
eventLogEntry=_EventLogEntry_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1))
eventLogEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:eventLogEntry.setStatus(_A)
_EventSeqNum_Type=Unsigned32
_EventSeqNum_Object=MibTableColumn
eventSeqNum=_EventSeqNum_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1,1),_EventSeqNum_Type())
eventSeqNum.setMaxAccess(_F)
if mibBuilder.loadTexts:eventSeqNum.setStatus(_A)
_EventCode_Type=EponAlarmCode
_EventCode_Object=MibTableColumn
eventCode=_EventCode_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1,2),_EventCode_Type())
eventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:eventCode.setStatus(_A)
_EventInstance_Type=EponAlarmInstance
_EventInstance_Object=MibTableColumn
eventInstance=_EventInstance_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1,3),_EventInstance_Type())
eventInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:eventInstance.setStatus(_A)
_EventOccurTime_Type=DateAndTime
_EventOccurTime_Object=MibTableColumn
eventOccurTime=_EventOccurTime_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1,4),_EventOccurTime_Type())
eventOccurTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eventOccurTime.setStatus(_A)
class _EventAdditionalText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_EventAdditionalText_Type.__name__=_D
_EventAdditionalText_Object=MibTableColumn
eventAdditionalText=_EventAdditionalText_Object((1,3,6,1,4,1,17409,2,2,11,2,3,1,5),_EventAdditionalText_Type())
eventAdditionalText.setMaxAccess(_B)
if mibBuilder.loadTexts:eventAdditionalText.setStatus(_A)
_EponManagementAddrTable_Object=MibTable
eponManagementAddrTable=_EponManagementAddrTable_Object((1,3,6,1,4,1,17409,2,2,11,3,1))
if mibBuilder.loadTexts:eponManagementAddrTable.setStatus(_A)
_EponManagementAddrEntry_Object=MibTableRow
eponManagementAddrEntry=_EponManagementAddrEntry_Object((1,3,6,1,4,1,17409,2,2,11,3,1,1))
eponManagementAddrEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:eponManagementAddrEntry.setStatus(_A)
class _EponManagementAddrName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EponManagementAddrName_Type.__name__=_D
_EponManagementAddrName_Object=MibTableColumn
eponManagementAddrName=_EponManagementAddrName_Object((1,3,6,1,4,1,17409,2,2,11,3,1,1,1),_EponManagementAddrName_Type())
eponManagementAddrName.setMaxAccess(_F)
if mibBuilder.loadTexts:eponManagementAddrName.setStatus(_A)
_EponManagementAddrTAddress_Type=TAddress
_EponManagementAddrTAddress_Object=MibTableColumn
eponManagementAddrTAddress=_EponManagementAddrTAddress_Object((1,3,6,1,4,1,17409,2,2,11,3,1,1,2),_EponManagementAddrTAddress_Type())
eponManagementAddrTAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:eponManagementAddrTAddress.setStatus(_A)
class _EponManagementAddrCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EponManagementAddrCommunity_Type.__name__=_D
_EponManagementAddrCommunity_Object=MibTableColumn
eponManagementAddrCommunity=_EponManagementAddrCommunity_Object((1,3,6,1,4,1,17409,2,2,11,3,1,1,3),_EponManagementAddrCommunity_Type())
eponManagementAddrCommunity.setMaxAccess(_G)
if mibBuilder.loadTexts:eponManagementAddrCommunity.setStatus(_A)
_EponManagementAddrRowStatus_Type=RowStatus
_EponManagementAddrRowStatus_Object=MibTableColumn
eponManagementAddrRowStatus=_EponManagementAddrRowStatus_Object((1,3,6,1,4,1,17409,2,2,11,3,1,1,4),_EponManagementAddrRowStatus_Type())
eponManagementAddrRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:eponManagementAddrRowStatus.setStatus(_A)
eponAlarmNotification=NotificationType((1,3,6,1,4,1,17409,2,2,11,1,1,1))
eponAlarmNotification.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_S),(_C,_T),(_C,_L)))
if mibBuilder.loadTexts:eponAlarmNotification.setStatus(_A)
eponEventNotification=NotificationType((1,3,6,1,4,1,17409,2,2,11,1,1,2))
eponEventNotification.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:eponEventNotification.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'eponNotifications':eponNotifications,'eponAlarmNotification':eponAlarmNotification,'eponEventNotification':eponEventNotification,'eponTrapObjects':eponTrapObjects,_K:eponTrapInstance,_T:eponTrapCorrelationId,_L:eponTrapAdditionalText,_J:eponTrapCode,_S:eponTrapSeverity,_I:eponTrapOccurTime,_H:eponTrapSequenceNumber,'activeAlarmTable':activeAlarmTable,'activeAlarmEntry':activeAlarmEntry,_M:activeAlarmSeqNum,'activeAlarmCode':activeAlarmCode,'activeAlarmInstance':activeAlarmInstance,'activeAlarmSeverity':activeAlarmSeverity,_N:activeAlarmRaisingNumber,'activeAlarmFirstOccurTime':activeAlarmFirstOccurTime,'activeAlarmLastOccurTime':activeAlarmLastOccurTime,'activeAlarmRepeats':activeAlarmRepeats,'activeAlarmConfirm':activeAlarmConfirm,'activeAlarmAdditionalText':activeAlarmAdditionalText,'historyAlarmTable':historyAlarmTable,'historyAlarmEntry':historyAlarmEntry,_O:historyAlarmSeqNum,'historyAlarmCode':historyAlarmCode,'historyAlarmInstance':historyAlarmInstance,'historyAlarmSeverity':historyAlarmSeverity,_P:historyAlarmRaisingNumber,'historyAlarmFirstOccurTime':historyAlarmFirstOccurTime,'historyAlarmLastOccurTime':historyAlarmLastOccurTime,'historyAlarmRepeats':historyAlarmRepeats,'historyAlarmCorrelationId':historyAlarmCorrelationId,'historyAlarmAdditionalText':historyAlarmAdditionalText,'historyAlarmClearTime':historyAlarmClearTime,'eventLogTable':eventLogTable,'eventLogEntry':eventLogEntry,_Q:eventSeqNum,'eventCode':eventCode,'eventInstance':eventInstance,'eventOccurTime':eventOccurTime,'eventAdditionalText':eventAdditionalText,'eponManagementAddrTable':eponManagementAddrTable,'eponManagementAddrEntry':eponManagementAddrEntry,_R:eponManagementAddrName,'eponManagementAddrTAddress':eponManagementAddrTAddress,'eponManagementAddrCommunity':eponManagementAddrCommunity,'eponManagementAddrRowStatus':eponManagementAddrRowStatus})