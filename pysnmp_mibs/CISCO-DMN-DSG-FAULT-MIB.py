_Q='awFaultHistorySequence'
_P='awFaultSettingPriority'
_O='information'
_N='awFaultStatusPriority'
_M='awFaultActiveListPriority'
_L='writeOnly'
_K='disabled'
_J='alarm'
_I='not-accessible'
_H='CISCO-DMN-DSG-FAULT-MIB'
_G='warning'
_F='read-write'
_E='yes'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ciscoDSGFault=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,17))
if mibBuilder.loadTexts:ciscoDSGFault.setRevisions(('2010-08-30 11:00','2010-03-22 05:00','2010-02-12 12:00','2010-01-08 12:00','2009-12-20 12:00','2009-12-07 12:00'))
_FaultSummary_ObjectIdentity=ObjectIdentity
faultSummary=_FaultSummary_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,17,1))
class _FaultSummaryNumActiveAlarms_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FaultSummaryNumActiveAlarms_Type.__name__=_C
_FaultSummaryNumActiveAlarms_Object=MibScalar
faultSummaryNumActiveAlarms=_FaultSummaryNumActiveAlarms_Object((1,3,6,1,4,1,1429,2,2,5,17,1,1),_FaultSummaryNumActiveAlarms_Type())
faultSummaryNumActiveAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:faultSummaryNumActiveAlarms.setStatus(_A)
class _FaultSummaryNumActiveWarnings_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FaultSummaryNumActiveWarnings_Type.__name__=_C
_FaultSummaryNumActiveWarnings_Object=MibScalar
faultSummaryNumActiveWarnings=_FaultSummaryNumActiveWarnings_Object((1,3,6,1,4,1,1429,2,2,5,17,1,2),_FaultSummaryNumActiveWarnings_Type())
faultSummaryNumActiveWarnings.setMaxAccess(_B)
if mibBuilder.loadTexts:faultSummaryNumActiveWarnings.setStatus(_A)
class _FaultSummaryClearAlarms_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('writeonly',1),(_E,2)))
_FaultSummaryClearAlarms_Type.__name__=_D
_FaultSummaryClearAlarms_Object=MibScalar
faultSummaryClearAlarms=_FaultSummaryClearAlarms_Object((1,3,6,1,4,1,1429,2,2,5,17,1,3),_FaultSummaryClearAlarms_Type())
faultSummaryClearAlarms.setMaxAccess(_F)
if mibBuilder.loadTexts:faultSummaryClearAlarms.setStatus(_A)
class _FaultSummaryClearWarnings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_E,2)))
_FaultSummaryClearWarnings_Type.__name__=_D
_FaultSummaryClearWarnings_Object=MibScalar
faultSummaryClearWarnings=_FaultSummaryClearWarnings_Object((1,3,6,1,4,1,1429,2,2,5,17,1,4),_FaultSummaryClearWarnings_Type())
faultSummaryClearWarnings.setMaxAccess(_F)
if mibBuilder.loadTexts:faultSummaryClearWarnings.setStatus(_A)
class _FaultSummaryClearHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_E,2)))
_FaultSummaryClearHistory_Type.__name__=_D
_FaultSummaryClearHistory_Object=MibScalar
faultSummaryClearHistory=_FaultSummaryClearHistory_Object((1,3,6,1,4,1,1429,2,2,5,17,1,5),_FaultSummaryClearHistory_Type())
faultSummaryClearHistory.setMaxAccess(_F)
if mibBuilder.loadTexts:faultSummaryClearHistory.setStatus(_A)
_FaultAWTable_ObjectIdentity=ObjectIdentity
faultAWTable=_FaultAWTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,17,2))
_AwFaultActiveListTable_Object=MibTable
awFaultActiveListTable=_AwFaultActiveListTable_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1))
if mibBuilder.loadTexts:awFaultActiveListTable.setStatus(_A)
_AwFaultActiveListEntry_Object=MibTableRow
awFaultActiveListEntry=_AwFaultActiveListEntry_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1))
awFaultActiveListEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:awFaultActiveListEntry.setStatus(_A)
class _AwFaultActiveListPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AwFaultActiveListPriority_Type.__name__=_D
_AwFaultActiveListPriority_Object=MibTableColumn
awFaultActiveListPriority=_AwFaultActiveListPriority_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,1),_AwFaultActiveListPriority_Type())
awFaultActiveListPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:awFaultActiveListPriority.setStatus(_A)
class _AwFaultActiveListTextID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultActiveListTextID_Type.__name__=_C
_AwFaultActiveListTextID_Object=MibTableColumn
awFaultActiveListTextID=_AwFaultActiveListTextID_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,2),_AwFaultActiveListTextID_Type())
awFaultActiveListTextID.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultActiveListTextID.setStatus(_A)
class _AwFaultActiveListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultActiveListName_Type.__name__=_C
_AwFaultActiveListName_Object=MibTableColumn
awFaultActiveListName=_AwFaultActiveListName_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,3),_AwFaultActiveListName_Type())
awFaultActiveListName.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultActiveListName.setStatus(_A)
class _AwFaultActiveListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_AwFaultActiveListType_Type.__name__=_D
_AwFaultActiveListType_Object=MibTableColumn
awFaultActiveListType=_AwFaultActiveListType_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,4),_AwFaultActiveListType_Type())
awFaultActiveListType.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultActiveListType.setStatus(_A)
class _AwFaultActiveListSetDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultActiveListSetDateTime_Type.__name__=_C
_AwFaultActiveListSetDateTime_Object=MibTableColumn
awFaultActiveListSetDateTime=_AwFaultActiveListSetDateTime_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,5),_AwFaultActiveListSetDateTime_Type())
awFaultActiveListSetDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultActiveListSetDateTime.setStatus(_A)
class _AwFaultActiveListDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AwFaultActiveListDetails_Type.__name__=_C
_AwFaultActiveListDetails_Object=MibTableColumn
awFaultActiveListDetails=_AwFaultActiveListDetails_Object((1,3,6,1,4,1,1429,2,2,5,17,2,1,1,6),_AwFaultActiveListDetails_Type())
awFaultActiveListDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultActiveListDetails.setStatus(_A)
_AwFaultStatusTable_Object=MibTable
awFaultStatusTable=_AwFaultStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2))
if mibBuilder.loadTexts:awFaultStatusTable.setStatus(_A)
_AwFaultStatusEntry_Object=MibTableRow
awFaultStatusEntry=_AwFaultStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1))
awFaultStatusEntry.setIndexNames((0,_H,_N))
if mibBuilder.loadTexts:awFaultStatusEntry.setStatus(_A)
class _AwFaultStatusPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AwFaultStatusPriority_Type.__name__=_D
_AwFaultStatusPriority_Object=MibTableColumn
awFaultStatusPriority=_AwFaultStatusPriority_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,1),_AwFaultStatusPriority_Type())
awFaultStatusPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:awFaultStatusPriority.setStatus(_A)
class _AwFaultStatusTextId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultStatusTextId_Type.__name__=_C
_AwFaultStatusTextId_Object=MibTableColumn
awFaultStatusTextId=_AwFaultStatusTextId_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,2),_AwFaultStatusTextId_Type())
awFaultStatusTextId.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusTextId.setStatus(_A)
class _AwFaultStatusFaultNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultStatusFaultNum_Type.__name__=_C
_AwFaultStatusFaultNum_Object=MibTableColumn
awFaultStatusFaultNum=_AwFaultStatusFaultNum_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,3),_AwFaultStatusFaultNum_Type())
awFaultStatusFaultNum.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusFaultNum.setStatus(_A)
class _AwFaultStatusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultStatusName_Type.__name__=_C
_AwFaultStatusName_Object=MibTableColumn
awFaultStatusName=_AwFaultStatusName_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,4),_AwFaultStatusName_Type())
awFaultStatusName.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusName.setStatus(_A)
class _AwFaultStatusType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_AwFaultStatusType_Type.__name__=_D
_AwFaultStatusType_Object=MibTableColumn
awFaultStatusType=_AwFaultStatusType_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,5),_AwFaultStatusType_Type())
awFaultStatusType.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusType.setStatus(_A)
class _AwFaultStatusSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('major',1),('minor',2),(_G,3),(_O,4)))
_AwFaultStatusSeverity_Type.__name__=_D
_AwFaultStatusSeverity_Object=MibTableColumn
awFaultStatusSeverity=_AwFaultStatusSeverity_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,6),_AwFaultStatusSeverity_Type())
awFaultStatusSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusSeverity.setStatus(_A)
class _AwFaultStatusLastDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultStatusLastDateTime_Type.__name__=_C
_AwFaultStatusLastDateTime_Object=MibTableColumn
awFaultStatusLastDateTime=_AwFaultStatusLastDateTime_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,7),_AwFaultStatusLastDateTime_Type())
awFaultStatusLastDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusLastDateTime.setStatus(_A)
class _AwFaultStatusTrapState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('set',2)))
_AwFaultStatusTrapState_Type.__name__=_D
_AwFaultStatusTrapState_Object=MibTableColumn
awFaultStatusTrapState=_AwFaultStatusTrapState_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,8),_AwFaultStatusTrapState_Type())
awFaultStatusTrapState.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusTrapState.setStatus(_A)
class _AwFaultStatusDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AwFaultStatusDetails_Type.__name__=_C
_AwFaultStatusDetails_Object=MibTableColumn
awFaultStatusDetails=_AwFaultStatusDetails_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,9),_AwFaultStatusDetails_Type())
awFaultStatusDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusDetails.setStatus(_A)
class _AwFaultStatusRelay_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultStatusRelay_Type.__name__=_C
_AwFaultStatusRelay_Object=MibTableColumn
awFaultStatusRelay=_AwFaultStatusRelay_Object((1,3,6,1,4,1,1429,2,2,5,17,2,2,1,10),_AwFaultStatusRelay_Type())
awFaultStatusRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultStatusRelay.setStatus(_A)
_AwFaultSettingTable_Object=MibTable
awFaultSettingTable=_AwFaultSettingTable_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3))
if mibBuilder.loadTexts:awFaultSettingTable.setStatus(_A)
_AwFaultSettingEntry_Object=MibTableRow
awFaultSettingEntry=_AwFaultSettingEntry_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1))
awFaultSettingEntry.setIndexNames((0,_H,_P))
if mibBuilder.loadTexts:awFaultSettingEntry.setStatus(_A)
class _AwFaultSettingPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AwFaultSettingPriority_Type.__name__=_D
_AwFaultSettingPriority_Object=MibTableColumn
awFaultSettingPriority=_AwFaultSettingPriority_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,1),_AwFaultSettingPriority_Type())
awFaultSettingPriority.setMaxAccess(_I)
if mibBuilder.loadTexts:awFaultSettingPriority.setStatus(_A)
class _AwFaultSettingTextId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultSettingTextId_Type.__name__=_C
_AwFaultSettingTextId_Object=MibTableColumn
awFaultSettingTextId=_AwFaultSettingTextId_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,2),_AwFaultSettingTextId_Type())
awFaultSettingTextId.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultSettingTextId.setStatus(_A)
class _AwFaultSettingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_AwFaultSettingType_Type.__name__=_D
_AwFaultSettingType_Object=MibTableColumn
awFaultSettingType=_AwFaultSettingType_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,3),_AwFaultSettingType_Type())
awFaultSettingType.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultSettingType.setStatus(_A)
class _AwFaultSettingSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('major',1),('minor',2),(_G,3),(_O,4)))
_AwFaultSettingSeverity_Type.__name__=_D
_AwFaultSettingSeverity_Object=MibTableColumn
awFaultSettingSeverity=_AwFaultSettingSeverity_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,4),_AwFaultSettingSeverity_Type())
awFaultSettingSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultSettingSeverity.setStatus(_A)
class _AwFaultSettingName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultSettingName_Type.__name__=_C
_AwFaultSettingName_Object=MibTableColumn
awFaultSettingName=_AwFaultSettingName_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,5),_AwFaultSettingName_Type())
awFaultSettingName.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultSettingName.setStatus(_A)
class _AwFaultSettingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),(_E,2),(_K,3)))
_AwFaultSettingEnable_Type.__name__=_D
_AwFaultSettingEnable_Object=MibTableColumn
awFaultSettingEnable=_AwFaultSettingEnable_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,6),_AwFaultSettingEnable_Type())
awFaultSettingEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:awFaultSettingEnable.setStatus(_A)
class _AwFaultSettingRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),(_E,2),(_K,3)))
_AwFaultSettingRelay_Type.__name__=_D
_AwFaultSettingRelay_Object=MibTableColumn
awFaultSettingRelay=_AwFaultSettingRelay_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,7),_AwFaultSettingRelay_Type())
awFaultSettingRelay.setMaxAccess(_F)
if mibBuilder.loadTexts:awFaultSettingRelay.setStatus(_A)
class _AwFaultSettingTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),(_E,2),(_K,3)))
_AwFaultSettingTrap_Type.__name__=_D
_AwFaultSettingTrap_Object=MibTableColumn
awFaultSettingTrap=_AwFaultSettingTrap_Object((1,3,6,1,4,1,1429,2,2,5,17,2,3,1,8),_AwFaultSettingTrap_Type())
awFaultSettingTrap.setMaxAccess(_F)
if mibBuilder.loadTexts:awFaultSettingTrap.setStatus(_A)
_AwFaultHistoryTable_Object=MibTable
awFaultHistoryTable=_AwFaultHistoryTable_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5))
if mibBuilder.loadTexts:awFaultHistoryTable.setStatus(_A)
_AwFaultHistoryEntry_Object=MibTableRow
awFaultHistoryEntry=_AwFaultHistoryEntry_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1))
awFaultHistoryEntry.setIndexNames((0,_H,_Q))
if mibBuilder.loadTexts:awFaultHistoryEntry.setStatus(_A)
_AwFaultHistorySequence_Type=Counter32
_AwFaultHistorySequence_Object=MibTableColumn
awFaultHistorySequence=_AwFaultHistorySequence_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,1),_AwFaultHistorySequence_Type())
awFaultHistorySequence.setMaxAccess(_I)
if mibBuilder.loadTexts:awFaultHistorySequence.setStatus(_A)
class _AwFaultHistoryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultHistoryName_Type.__name__=_C
_AwFaultHistoryName_Object=MibTableColumn
awFaultHistoryName=_AwFaultHistoryName_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,2),_AwFaultHistoryName_Type())
awFaultHistoryName.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistoryName.setStatus(_A)
class _AwFaultHistoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_AwFaultHistoryType_Type.__name__=_D
_AwFaultHistoryType_Object=MibTableColumn
awFaultHistoryType=_AwFaultHistoryType_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,3),_AwFaultHistoryType_Type())
awFaultHistoryType.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistoryType.setStatus(_A)
class _AwFaultHistorySetDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultHistorySetDateTime_Type.__name__=_C
_AwFaultHistorySetDateTime_Object=MibTableColumn
awFaultHistorySetDateTime=_AwFaultHistorySetDateTime_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,4),_AwFaultHistorySetDateTime_Type())
awFaultHistorySetDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistorySetDateTime.setStatus(_A)
class _AwFaultHistoryResetDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AwFaultHistoryResetDateTime_Type.__name__=_C
_AwFaultHistoryResetDateTime_Object=MibTableColumn
awFaultHistoryResetDateTime=_AwFaultHistoryResetDateTime_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,5),_AwFaultHistoryResetDateTime_Type())
awFaultHistoryResetDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistoryResetDateTime.setStatus(_A)
class _AwFaultHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clear',1),('set',2),('clearByReset',3)))
_AwFaultHistoryState_Type.__name__=_D
_AwFaultHistoryState_Object=MibTableColumn
awFaultHistoryState=_AwFaultHistoryState_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,6),_AwFaultHistoryState_Type())
awFaultHistoryState.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistoryState.setStatus(_A)
class _AwFaultHistoryDetails_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_AwFaultHistoryDetails_Type.__name__=_C
_AwFaultHistoryDetails_Object=MibTableColumn
awFaultHistoryDetails=_AwFaultHistoryDetails_Object((1,3,6,1,4,1,1429,2,2,5,17,2,5,1,7),_AwFaultHistoryDetails_Type())
awFaultHistoryDetails.setMaxAccess(_B)
if mibBuilder.loadTexts:awFaultHistoryDetails.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'ciscoDSGFault':ciscoDSGFault,'faultSummary':faultSummary,'faultSummaryNumActiveAlarms':faultSummaryNumActiveAlarms,'faultSummaryNumActiveWarnings':faultSummaryNumActiveWarnings,'faultSummaryClearAlarms':faultSummaryClearAlarms,'faultSummaryClearWarnings':faultSummaryClearWarnings,'faultSummaryClearHistory':faultSummaryClearHistory,'faultAWTable':faultAWTable,'awFaultActiveListTable':awFaultActiveListTable,'awFaultActiveListEntry':awFaultActiveListEntry,_M:awFaultActiveListPriority,'awFaultActiveListTextID':awFaultActiveListTextID,'awFaultActiveListName':awFaultActiveListName,'awFaultActiveListType':awFaultActiveListType,'awFaultActiveListSetDateTime':awFaultActiveListSetDateTime,'awFaultActiveListDetails':awFaultActiveListDetails,'awFaultStatusTable':awFaultStatusTable,'awFaultStatusEntry':awFaultStatusEntry,_N:awFaultStatusPriority,'awFaultStatusTextId':awFaultStatusTextId,'awFaultStatusFaultNum':awFaultStatusFaultNum,'awFaultStatusName':awFaultStatusName,'awFaultStatusType':awFaultStatusType,'awFaultStatusSeverity':awFaultStatusSeverity,'awFaultStatusLastDateTime':awFaultStatusLastDateTime,'awFaultStatusTrapState':awFaultStatusTrapState,'awFaultStatusDetails':awFaultStatusDetails,'awFaultStatusRelay':awFaultStatusRelay,'awFaultSettingTable':awFaultSettingTable,'awFaultSettingEntry':awFaultSettingEntry,_P:awFaultSettingPriority,'awFaultSettingTextId':awFaultSettingTextId,'awFaultSettingType':awFaultSettingType,'awFaultSettingSeverity':awFaultSettingSeverity,'awFaultSettingName':awFaultSettingName,'awFaultSettingEnable':awFaultSettingEnable,'awFaultSettingRelay':awFaultSettingRelay,'awFaultSettingTrap':awFaultSettingTrap,'awFaultHistoryTable':awFaultHistoryTable,'awFaultHistoryEntry':awFaultHistoryEntry,_Q:awFaultHistorySequence,'awFaultHistoryName':awFaultHistoryName,'awFaultHistoryType':awFaultHistoryType,'awFaultHistorySetDateTime':awFaultHistorySetDateTime,'awFaultHistoryResetDateTime':awFaultHistoryResetDateTime,'awFaultHistoryState':awFaultHistoryState,'awFaultHistoryDetails':awFaultHistoryDetails})