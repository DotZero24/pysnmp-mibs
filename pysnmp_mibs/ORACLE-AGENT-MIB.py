_P='oraAgentEventResults'
_O='oraAgentEventArguments'
_N='oraAgentEventMessage'
_M='oraAgentEventAppID'
_L='oraAgentEventUser'
_K='oraAgentEventSeverity'
_J='oraAgentEventTime'
_I='oraAgentEventService'
_H='oraAgentEventID'
_G='oraAgentEventName'
_F='oraAgentEventIndex'
_E='NotificationType'
_D='Integer32'
_C='read-only'
_B='ORACLE-AGENT-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,11))
_Oracle_ObjectIdentity=ObjectIdentity
oracle=_Oracle_ObjectIdentity((1,3,6,1,4,1,111))
_OraAgent_ObjectIdentity=ObjectIdentity
oraAgent=_OraAgent_ObjectIdentity((1,3,6,1,4,1,111,12))
_OraAgentObjects_ObjectIdentity=ObjectIdentity
oraAgentObjects=_OraAgentObjects_ObjectIdentity((1,3,6,1,4,1,111,12,1))
_OraAgentEventTable_Object=MibTable
oraAgentEventTable=_OraAgentEventTable_Object((1,3,6,1,4,1,111,12,1,1))
if mibBuilder.loadTexts:oraAgentEventTable.setStatus(_A)
_OraAgentEventEntry_Object=MibTableRow
oraAgentEventEntry=_OraAgentEventEntry_Object((1,3,6,1,4,1,111,12,1,1,1))
oraAgentEventEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:oraAgentEventEntry.setStatus(_A)
_OraAgentEventIndex_Type=Integer32
_OraAgentEventIndex_Object=MibTableColumn
oraAgentEventIndex=_OraAgentEventIndex_Object((1,3,6,1,4,1,111,12,1,1,1,1),_OraAgentEventIndex_Type())
oraAgentEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventIndex.setStatus(_A)
_OraAgentEventName_Type=DisplayString
_OraAgentEventName_Object=MibTableColumn
oraAgentEventName=_OraAgentEventName_Object((1,3,6,1,4,1,111,12,1,1,1,2),_OraAgentEventName_Type())
oraAgentEventName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventName.setStatus(_A)
_OraAgentEventID_Type=Integer32
_OraAgentEventID_Object=MibTableColumn
oraAgentEventID=_OraAgentEventID_Object((1,3,6,1,4,1,111,12,1,1,1,3),_OraAgentEventID_Type())
oraAgentEventID.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventID.setStatus(_A)
_OraAgentEventService_Type=DisplayString
_OraAgentEventService_Object=MibTableColumn
oraAgentEventService=_OraAgentEventService_Object((1,3,6,1,4,1,111,12,1,1,1,4),_OraAgentEventService_Type())
oraAgentEventService.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventService.setStatus(_A)
_OraAgentEventTime_Type=DateAndTime
_OraAgentEventTime_Object=MibTableColumn
oraAgentEventTime=_OraAgentEventTime_Object((1,3,6,1,4,1,111,12,1,1,1,5),_OraAgentEventTime_Type())
oraAgentEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventTime.setStatus(_A)
class _OraAgentEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*(('clear',-1),('warning',1),('alert',2)))
_OraAgentEventSeverity_Type.__name__=_D
_OraAgentEventSeverity_Object=MibTableColumn
oraAgentEventSeverity=_OraAgentEventSeverity_Object((1,3,6,1,4,1,111,12,1,1,1,6),_OraAgentEventSeverity_Type())
oraAgentEventSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventSeverity.setStatus(_A)
_OraAgentEventUser_Type=DisplayString
_OraAgentEventUser_Object=MibTableColumn
oraAgentEventUser=_OraAgentEventUser_Object((1,3,6,1,4,1,111,12,1,1,1,7),_OraAgentEventUser_Type())
oraAgentEventUser.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventUser.setStatus(_A)
_OraAgentEventAppID_Type=Integer32
_OraAgentEventAppID_Object=MibTableColumn
oraAgentEventAppID=_OraAgentEventAppID_Object((1,3,6,1,4,1,111,12,1,1,1,8),_OraAgentEventAppID_Type())
oraAgentEventAppID.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventAppID.setStatus(_A)
_OraAgentEventMessage_Type=DisplayString
_OraAgentEventMessage_Object=MibTableColumn
oraAgentEventMessage=_OraAgentEventMessage_Object((1,3,6,1,4,1,111,12,1,1,1,9),_OraAgentEventMessage_Type())
oraAgentEventMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventMessage.setStatus(_A)
_OraAgentEventArguments_Type=DisplayString
_OraAgentEventArguments_Object=MibTableColumn
oraAgentEventArguments=_OraAgentEventArguments_Object((1,3,6,1,4,1,111,12,1,1,1,10),_OraAgentEventArguments_Type())
oraAgentEventArguments.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventArguments.setStatus(_A)
_OraAgentEventResults_Type=DisplayString
_OraAgentEventResults_Object=MibTableColumn
oraAgentEventResults=_OraAgentEventResults_Object((1,3,6,1,4,1,111,12,1,1,1,11),_OraAgentEventResults_Type())
oraAgentEventResults.setMaxAccess(_C)
if mibBuilder.loadTexts:oraAgentEventResults.setStatus(_A)
_OraAgentTraps_ObjectIdentity=ObjectIdentity
oraAgentTraps=_OraAgentTraps_ObjectIdentity((1,3,6,1,4,1,111,12,2))
oraAgentEventOcc=NotificationType((1,3,6,1,4,1,111,12,2,0,2))
oraAgentEventOcc.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:oraAgentEventOcc.setStatus('')
mibBuilder.exportSymbols(_B,**{'DateAndTime':DateAndTime,'oracle':oracle,'oraAgent':oraAgent,'oraAgentObjects':oraAgentObjects,'oraAgentEventTable':oraAgentEventTable,'oraAgentEventEntry':oraAgentEventEntry,_F:oraAgentEventIndex,_G:oraAgentEventName,_H:oraAgentEventID,_I:oraAgentEventService,_J:oraAgentEventTime,_K:oraAgentEventSeverity,_L:oraAgentEventUser,_M:oraAgentEventAppID,_N:oraAgentEventMessage,_O:oraAgentEventArguments,_P:oraAgentEventResults,'oraAgentTraps':oraAgentTraps,'oraAgentEventOcc':oraAgentEventOcc})