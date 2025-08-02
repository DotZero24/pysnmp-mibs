_I='trapEventVarbindId'
_H='trapEventVarbindSeqId'
_G='activeTrapEventSeqId'
_F='historyTrapEventSeqId'
_E='not-accessible'
_D='FORCE10-TRAP-EVENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention')
f10TrapEventMib=ModuleIdentity((1,3,6,1,4,1,6027,3,6))
if mibBuilder.loadTexts:f10TrapEventMib.setRevisions(('2012-02-21 00:00','2005-10-05 00:00'))
_F10TrapEventObjects_ObjectIdentity=ObjectIdentity
f10TrapEventObjects=_F10TrapEventObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1))
_F10HistoryTrapEvent_ObjectIdentity=ObjectIdentity
f10HistoryTrapEvent=_F10HistoryTrapEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,1))
_F10ChassisBootupTime_Type=DateAndTime
_F10ChassisBootupTime_Object=MibScalar
f10ChassisBootupTime=_F10ChassisBootupTime_Object((1,3,6,1,4,1,6027,3,6,1,1,1),_F10ChassisBootupTime_Type())
f10ChassisBootupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:f10ChassisBootupTime.setStatus(_A)
class _F10LastTrapEventSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_F10LastTrapEventSeqId_Type.__name__=_C
_F10LastTrapEventSeqId_Object=MibScalar
f10LastTrapEventSeqId=_F10LastTrapEventSeqId_Object((1,3,6,1,4,1,6027,3,6,1,1,2),_F10LastTrapEventSeqId_Type())
f10LastTrapEventSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:f10LastTrapEventSeqId.setStatus(_A)
_F10MaxHistoryTableSize_Type=Integer32
_F10MaxHistoryTableSize_Object=MibScalar
f10MaxHistoryTableSize=_F10MaxHistoryTableSize_Object((1,3,6,1,4,1,6027,3,6,1,1,3),_F10MaxHistoryTableSize_Type())
f10MaxHistoryTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:f10MaxHistoryTableSize.setStatus(_A)
_F10HistoryTrapEventTable_Object=MibTable
f10HistoryTrapEventTable=_F10HistoryTrapEventTable_Object((1,3,6,1,4,1,6027,3,6,1,1,4))
if mibBuilder.loadTexts:f10HistoryTrapEventTable.setStatus(_A)
_F10HistoryTrapEventEntry_Object=MibTableRow
f10HistoryTrapEventEntry=_F10HistoryTrapEventEntry_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1))
f10HistoryTrapEventEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:f10HistoryTrapEventEntry.setStatus(_A)
class _HistoryTrapEventSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HistoryTrapEventSeqId_Type.__name__=_C
_HistoryTrapEventSeqId_Object=MibTableColumn
historyTrapEventSeqId=_HistoryTrapEventSeqId_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,1),_HistoryTrapEventSeqId_Type())
historyTrapEventSeqId.setMaxAccess(_E)
if mibBuilder.loadTexts:historyTrapEventSeqId.setStatus(_A)
_HistoryTrapEventSeverity_Type=Integer32
_HistoryTrapEventSeverity_Object=MibTableColumn
historyTrapEventSeverity=_HistoryTrapEventSeverity_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,2),_HistoryTrapEventSeverity_Type())
historyTrapEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventSeverity.setStatus(_A)
_HistoryTrapEventType_Type=Integer32
_HistoryTrapEventType_Object=MibTableColumn
historyTrapEventType=_HistoryTrapEventType_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,3),_HistoryTrapEventType_Type())
historyTrapEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventType.setStatus(_A)
_HistoryTrapEventMsg_Type=DisplayString
_HistoryTrapEventMsg_Object=MibTableColumn
historyTrapEventMsg=_HistoryTrapEventMsg_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,4),_HistoryTrapEventMsg_Type())
historyTrapEventMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventMsg.setStatus(_A)
_HistoryTrapEventOid_Type=RowPointer
_HistoryTrapEventOid_Object=MibTableColumn
historyTrapEventOid=_HistoryTrapEventOid_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,5),_HistoryTrapEventOid_Type())
historyTrapEventOid.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventOid.setStatus(_A)
_HistoryTrapEventSlot_Type=Integer32
_HistoryTrapEventSlot_Object=MibTableColumn
historyTrapEventSlot=_HistoryTrapEventSlot_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,6),_HistoryTrapEventSlot_Type())
historyTrapEventSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventSlot.setStatus(_A)
_HistoryTrapEventTimeStamp_Type=TimeTicks
_HistoryTrapEventTimeStamp_Object=MibTableColumn
historyTrapEventTimeStamp=_HistoryTrapEventTimeStamp_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,7),_HistoryTrapEventTimeStamp_Type())
historyTrapEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventTimeStamp.setStatus(_A)
_HistoryTrapEventPort_Type=Integer32
_HistoryTrapEventPort_Object=MibTableColumn
historyTrapEventPort=_HistoryTrapEventPort_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1,8),_HistoryTrapEventPort_Type())
historyTrapEventPort.setMaxAccess(_B)
if mibBuilder.loadTexts:historyTrapEventPort.setStatus(_A)
_F10ActiveTrapEvent_ObjectIdentity=ObjectIdentity
f10ActiveTrapEvent=_F10ActiveTrapEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,2))
_F10ActiveTrapEventTable_Object=MibTable
f10ActiveTrapEventTable=_F10ActiveTrapEventTable_Object((1,3,6,1,4,1,6027,3,6,1,2,1))
if mibBuilder.loadTexts:f10ActiveTrapEventTable.setStatus(_A)
_F10ActiveTrapEventEntry_Object=MibTableRow
f10ActiveTrapEventEntry=_F10ActiveTrapEventEntry_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1))
f10ActiveTrapEventEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:f10ActiveTrapEventEntry.setStatus(_A)
class _ActiveTrapEventSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ActiveTrapEventSeqId_Type.__name__=_C
_ActiveTrapEventSeqId_Object=MibTableColumn
activeTrapEventSeqId=_ActiveTrapEventSeqId_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,1),_ActiveTrapEventSeqId_Type())
activeTrapEventSeqId.setMaxAccess(_E)
if mibBuilder.loadTexts:activeTrapEventSeqId.setStatus(_A)
_ActiveTrapEventSeverity_Type=Integer32
_ActiveTrapEventSeverity_Object=MibTableColumn
activeTrapEventSeverity=_ActiveTrapEventSeverity_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,2),_ActiveTrapEventSeverity_Type())
activeTrapEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventSeverity.setStatus(_A)
_ActiveTrapEventType_Type=Integer32
_ActiveTrapEventType_Object=MibTableColumn
activeTrapEventType=_ActiveTrapEventType_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,3),_ActiveTrapEventType_Type())
activeTrapEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventType.setStatus(_A)
_ActiveTrapEventMsg_Type=DisplayString
_ActiveTrapEventMsg_Object=MibTableColumn
activeTrapEventMsg=_ActiveTrapEventMsg_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,4),_ActiveTrapEventMsg_Type())
activeTrapEventMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventMsg.setStatus(_A)
_ActiveTrapEventOid_Type=RowPointer
_ActiveTrapEventOid_Object=MibTableColumn
activeTrapEventOid=_ActiveTrapEventOid_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,5),_ActiveTrapEventOid_Type())
activeTrapEventOid.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventOid.setStatus(_A)
_ActiveTrapEventSlot_Type=Integer32
_ActiveTrapEventSlot_Object=MibTableColumn
activeTrapEventSlot=_ActiveTrapEventSlot_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,6),_ActiveTrapEventSlot_Type())
activeTrapEventSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventSlot.setStatus(_A)
_ActiveTrapEventTimeStamp_Type=TimeTicks
_ActiveTrapEventTimeStamp_Object=MibTableColumn
activeTrapEventTimeStamp=_ActiveTrapEventTimeStamp_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,7),_ActiveTrapEventTimeStamp_Type())
activeTrapEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventTimeStamp.setStatus(_A)
_ActiveTrapEventPort_Type=Integer32
_ActiveTrapEventPort_Object=MibTableColumn
activeTrapEventPort=_ActiveTrapEventPort_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1,8),_ActiveTrapEventPort_Type())
activeTrapEventPort.setMaxAccess(_B)
if mibBuilder.loadTexts:activeTrapEventPort.setStatus(_A)
_F10TrapVarbindEvent_ObjectIdentity=ObjectIdentity
f10TrapVarbindEvent=_F10TrapVarbindEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,3))
_F10TrapEventVarbindTable_Object=MibTable
f10TrapEventVarbindTable=_F10TrapEventVarbindTable_Object((1,3,6,1,4,1,6027,3,6,1,3,1))
if mibBuilder.loadTexts:f10TrapEventVarbindTable.setStatus(_A)
_F10TrapEventVarbindEntry_Object=MibTableRow
f10TrapEventVarbindEntry=_F10TrapEventVarbindEntry_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1))
f10TrapEventVarbindEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:f10TrapEventVarbindEntry.setStatus(_A)
class _TrapEventVarbindSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TrapEventVarbindSeqId_Type.__name__=_C
_TrapEventVarbindSeqId_Object=MibTableColumn
trapEventVarbindSeqId=_TrapEventVarbindSeqId_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1,1),_TrapEventVarbindSeqId_Type())
trapEventVarbindSeqId.setMaxAccess(_E)
if mibBuilder.loadTexts:trapEventVarbindSeqId.setStatus(_A)
class _TrapEventVarbindId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_TrapEventVarbindId_Type.__name__=_C
_TrapEventVarbindId_Object=MibTableColumn
trapEventVarbindId=_TrapEventVarbindId_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1,2),_TrapEventVarbindId_Type())
trapEventVarbindId.setMaxAccess(_E)
if mibBuilder.loadTexts:trapEventVarbindId.setStatus(_A)
_TrapEventVarbindOid_Type=ObjectIdentifier
_TrapEventVarbindOid_Object=MibTableColumn
trapEventVarbindOid=_TrapEventVarbindOid_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1,3),_TrapEventVarbindOid_Type())
trapEventVarbindOid.setMaxAccess(_B)
if mibBuilder.loadTexts:trapEventVarbindOid.setStatus(_A)
_TrapEventVarbindType_Type=Integer32
_TrapEventVarbindType_Object=MibTableColumn
trapEventVarbindType=_TrapEventVarbindType_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1,4),_TrapEventVarbindType_Type())
trapEventVarbindType.setMaxAccess(_B)
if mibBuilder.loadTexts:trapEventVarbindType.setStatus(_A)
_TrapEventVarbindValue_Type=DisplayString
_TrapEventVarbindValue_Object=MibTableColumn
trapEventVarbindValue=_TrapEventVarbindValue_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1,5),_TrapEventVarbindValue_Type())
trapEventVarbindValue.setMaxAccess(_B)
if mibBuilder.loadTexts:trapEventVarbindValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'f10TrapEventMib':f10TrapEventMib,'f10TrapEventObjects':f10TrapEventObjects,'f10HistoryTrapEvent':f10HistoryTrapEvent,'f10ChassisBootupTime':f10ChassisBootupTime,'f10LastTrapEventSeqId':f10LastTrapEventSeqId,'f10MaxHistoryTableSize':f10MaxHistoryTableSize,'f10HistoryTrapEventTable':f10HistoryTrapEventTable,'f10HistoryTrapEventEntry':f10HistoryTrapEventEntry,_F:historyTrapEventSeqId,'historyTrapEventSeverity':historyTrapEventSeverity,'historyTrapEventType':historyTrapEventType,'historyTrapEventMsg':historyTrapEventMsg,'historyTrapEventOid':historyTrapEventOid,'historyTrapEventSlot':historyTrapEventSlot,'historyTrapEventTimeStamp':historyTrapEventTimeStamp,'historyTrapEventPort':historyTrapEventPort,'f10ActiveTrapEvent':f10ActiveTrapEvent,'f10ActiveTrapEventTable':f10ActiveTrapEventTable,'f10ActiveTrapEventEntry':f10ActiveTrapEventEntry,_G:activeTrapEventSeqId,'activeTrapEventSeverity':activeTrapEventSeverity,'activeTrapEventType':activeTrapEventType,'activeTrapEventMsg':activeTrapEventMsg,'activeTrapEventOid':activeTrapEventOid,'activeTrapEventSlot':activeTrapEventSlot,'activeTrapEventTimeStamp':activeTrapEventTimeStamp,'activeTrapEventPort':activeTrapEventPort,'f10TrapVarbindEvent':f10TrapVarbindEvent,'f10TrapEventVarbindTable':f10TrapEventVarbindTable,'f10TrapEventVarbindEntry':f10TrapEventVarbindEntry,_H:trapEventVarbindSeqId,_I:trapEventVarbindId,'trapEventVarbindOid':trapEventVarbindOid,'trapEventVarbindType':trapEventVarbindType,'trapEventVarbindValue':trapEventVarbindValue})