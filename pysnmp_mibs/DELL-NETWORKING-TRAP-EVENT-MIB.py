_I='trapEventVarbindId'
_H='trapEventVarbindSeqId'
_G='activeTrapEventSeqId'
_F='historyTrapEventSeqId'
_E='not-accessible'
_D='DELL-NETWORKING-TRAP-EVENT-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowPointer','TextualConvention')
dellNetTrapEventMib=ModuleIdentity((1,3,6,1,4,1,6027,3,6))
if mibBuilder.loadTexts:dellNetTrapEventMib.setRevisions(('2012-02-21 00:00','2005-10-05 00:00'))
_DellNetTrapEventObjects_ObjectIdentity=ObjectIdentity
dellNetTrapEventObjects=_DellNetTrapEventObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1))
_DellNetHistoryTrapEvent_ObjectIdentity=ObjectIdentity
dellNetHistoryTrapEvent=_DellNetHistoryTrapEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,1))
_DellNetChassisBootupTime_Type=DateAndTime
_DellNetChassisBootupTime_Object=MibScalar
dellNetChassisBootupTime=_DellNetChassisBootupTime_Object((1,3,6,1,4,1,6027,3,6,1,1,1),_DellNetChassisBootupTime_Type())
dellNetChassisBootupTime.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetChassisBootupTime.setStatus(_A)
class _DellNetLastTrapEventSeqId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DellNetLastTrapEventSeqId_Type.__name__=_C
_DellNetLastTrapEventSeqId_Object=MibScalar
dellNetLastTrapEventSeqId=_DellNetLastTrapEventSeqId_Object((1,3,6,1,4,1,6027,3,6,1,1,2),_DellNetLastTrapEventSeqId_Type())
dellNetLastTrapEventSeqId.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetLastTrapEventSeqId.setStatus(_A)
_DellNetMaxHistoryTableSize_Type=Integer32
_DellNetMaxHistoryTableSize_Object=MibScalar
dellNetMaxHistoryTableSize=_DellNetMaxHistoryTableSize_Object((1,3,6,1,4,1,6027,3,6,1,1,3),_DellNetMaxHistoryTableSize_Type())
dellNetMaxHistoryTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetMaxHistoryTableSize.setStatus(_A)
_DellNetHistoryTrapEventTable_Object=MibTable
dellNetHistoryTrapEventTable=_DellNetHistoryTrapEventTable_Object((1,3,6,1,4,1,6027,3,6,1,1,4))
if mibBuilder.loadTexts:dellNetHistoryTrapEventTable.setStatus(_A)
_DellNetHistoryTrapEventEntry_Object=MibTableRow
dellNetHistoryTrapEventEntry=_DellNetHistoryTrapEventEntry_Object((1,3,6,1,4,1,6027,3,6,1,1,4,1))
dellNetHistoryTrapEventEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:dellNetHistoryTrapEventEntry.setStatus(_A)
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
_DellNetActiveTrapEvent_ObjectIdentity=ObjectIdentity
dellNetActiveTrapEvent=_DellNetActiveTrapEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,2))
_DellNetActiveTrapEventTable_Object=MibTable
dellNetActiveTrapEventTable=_DellNetActiveTrapEventTable_Object((1,3,6,1,4,1,6027,3,6,1,2,1))
if mibBuilder.loadTexts:dellNetActiveTrapEventTable.setStatus(_A)
_DellNetActiveTrapEventEntry_Object=MibTableRow
dellNetActiveTrapEventEntry=_DellNetActiveTrapEventEntry_Object((1,3,6,1,4,1,6027,3,6,1,2,1,1))
dellNetActiveTrapEventEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:dellNetActiveTrapEventEntry.setStatus(_A)
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
_DellNetTrapVarbindEvent_ObjectIdentity=ObjectIdentity
dellNetTrapVarbindEvent=_DellNetTrapVarbindEvent_ObjectIdentity((1,3,6,1,4,1,6027,3,6,1,3))
_DellNetTrapEventVarbindTable_Object=MibTable
dellNetTrapEventVarbindTable=_DellNetTrapEventVarbindTable_Object((1,3,6,1,4,1,6027,3,6,1,3,1))
if mibBuilder.loadTexts:dellNetTrapEventVarbindTable.setStatus(_A)
_DellNetTrapEventVarbindEntry_Object=MibTableRow
dellNetTrapEventVarbindEntry=_DellNetTrapEventVarbindEntry_Object((1,3,6,1,4,1,6027,3,6,1,3,1,1))
dellNetTrapEventVarbindEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:dellNetTrapEventVarbindEntry.setStatus(_A)
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
mibBuilder.exportSymbols(_D,**{'dellNetTrapEventMib':dellNetTrapEventMib,'dellNetTrapEventObjects':dellNetTrapEventObjects,'dellNetHistoryTrapEvent':dellNetHistoryTrapEvent,'dellNetChassisBootupTime':dellNetChassisBootupTime,'dellNetLastTrapEventSeqId':dellNetLastTrapEventSeqId,'dellNetMaxHistoryTableSize':dellNetMaxHistoryTableSize,'dellNetHistoryTrapEventTable':dellNetHistoryTrapEventTable,'dellNetHistoryTrapEventEntry':dellNetHistoryTrapEventEntry,_F:historyTrapEventSeqId,'historyTrapEventSeverity':historyTrapEventSeverity,'historyTrapEventType':historyTrapEventType,'historyTrapEventMsg':historyTrapEventMsg,'historyTrapEventOid':historyTrapEventOid,'historyTrapEventSlot':historyTrapEventSlot,'historyTrapEventTimeStamp':historyTrapEventTimeStamp,'historyTrapEventPort':historyTrapEventPort,'dellNetActiveTrapEvent':dellNetActiveTrapEvent,'dellNetActiveTrapEventTable':dellNetActiveTrapEventTable,'dellNetActiveTrapEventEntry':dellNetActiveTrapEventEntry,_G:activeTrapEventSeqId,'activeTrapEventSeverity':activeTrapEventSeverity,'activeTrapEventType':activeTrapEventType,'activeTrapEventMsg':activeTrapEventMsg,'activeTrapEventOid':activeTrapEventOid,'activeTrapEventSlot':activeTrapEventSlot,'activeTrapEventTimeStamp':activeTrapEventTimeStamp,'activeTrapEventPort':activeTrapEventPort,'dellNetTrapVarbindEvent':dellNetTrapVarbindEvent,'dellNetTrapEventVarbindTable':dellNetTrapEventVarbindTable,'dellNetTrapEventVarbindEntry':dellNetTrapEventVarbindEntry,_H:trapEventVarbindSeqId,_I:trapEventVarbindId,'trapEventVarbindOid':trapEventVarbindOid,'trapEventVarbindType':trapEventVarbindType,'trapEventVarbindValue':trapEventVarbindValue})