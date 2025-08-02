_H='enabled'
_G='eventListIndex'
_F='G6-EVENT-MIB'
_E='disabled'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
management=ModuleIdentity((1,3,6,1,4,1,3181,10,6,3))
if mibBuilder.loadTexts:management.setRevisions(('2018-02-12 16:19',))
_Event_ObjectIdentity=ObjectIdentity
event=_Event_ObjectIdentity((1,3,6,1,4,1,3181,10,6,3,70))
_EventListTable_Object=MibTable
eventListTable=_EventListTable_Object((1,3,6,1,4,1,3181,10,6,3,70,1))
if mibBuilder.loadTexts:eventListTable.setStatus(_A)
_EventListEntry_Object=MibTableRow
eventListEntry=_EventListEntry_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1))
eventListEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:eventListEntry.setStatus(_A)
class _EventListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_EventListIndex_Type.__name__=_B
_EventListIndex_Object=MibTableColumn
eventListIndex=_EventListIndex_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,1),_EventListIndex_Type())
eventListIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eventListIndex.setStatus(_A)
_EventListName_Type=DisplayString
_EventListName_Object=MibTableColumn
eventListName=_EventListName_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,2),_EventListName_Type())
eventListName.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListName.setStatus(_A)
class _EventListGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)));namedValues=NamedValues(*(('internal',0),('debug',2),('test',3),('reset',4),('firmware',5),('system',6),('config',7),('login',8),('auth',9),('power',10),('temperature',11),('link',12),('sfp',13),('poe',14),('ring',15),('ntp',16),('signals',17),('script',18),('filter',19),('lacp',20),('app',21),('cable',22),('security',23),('msp1000',24),('backup',25),('fan',26),('messaging',27),('terminalServer',28),('smartOffice',29)))
_EventListGroup_Type.__name__=_B
_EventListGroup_Object=MibTableColumn
eventListGroup=_EventListGroup_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,3),_EventListGroup_Type())
eventListGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListGroup.setStatus(_A)
class _EventListRelevance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('pos',0),('neg',1),('info',2)))
_EventListRelevance_Type.__name__=_B
_EventListRelevance_Object=MibTableColumn
eventListRelevance=_EventListRelevance_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,4),_EventListRelevance_Type())
eventListRelevance.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListRelevance.setStatus(_A)
class _EventListInternal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_EventListInternal_Type.__name__=_B
_EventListInternal_Object=MibTableColumn
eventListInternal=_EventListInternal_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,5),_EventListInternal_Type())
eventListInternal.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListInternal.setStatus(_A)
class _EventListSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,0),('debug',1),('info',2),('notice',3),('warning',4),('error',5),('critical',6),('alert',7),('emergency',8)))
_EventListSeverity_Type.__name__=_B
_EventListSeverity_Object=MibTableColumn
eventListSeverity=_EventListSeverity_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,6),_EventListSeverity_Type())
eventListSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:eventListSeverity.setStatus(_A)
class _EventListSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unit',0),('port',1)))
_EventListSource_Type.__name__=_B
_EventListSource_Object=MibTableColumn
eventListSource=_EventListSource_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,7),_EventListSource_Type())
eventListSource.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListSource.setStatus(_A)
class _EventListTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_EventListTrap_Type.__name__=_B
_EventListTrap_Object=MibTableColumn
eventListTrap=_EventListTrap_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,8),_EventListTrap_Type())
eventListTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:eventListTrap.setStatus(_A)
_EventListSyslogMessage_Type=DisplayString
_EventListSyslogMessage_Object=MibTableColumn
eventListSyslogMessage=_EventListSyslogMessage_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,9),_EventListSyslogMessage_Type())
eventListSyslogMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListSyslogMessage.setStatus(_A)
_EventListCustomMessage_Type=DisplayString
_EventListCustomMessage_Object=MibTableColumn
eventListCustomMessage=_EventListCustomMessage_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,10),_EventListCustomMessage_Type())
eventListCustomMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:eventListCustomMessage.setStatus(_A)
_EventListIntegerElements_Type=DisplayString
_EventListIntegerElements_Object=MibTableColumn
eventListIntegerElements=_EventListIntegerElements_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,11),_EventListIntegerElements_Type())
eventListIntegerElements.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListIntegerElements.setStatus(_A)
_EventListStringElements_Type=DisplayString
_EventListStringElements_Object=MibTableColumn
eventListStringElements=_EventListStringElements_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,12),_EventListStringElements_Type())
eventListStringElements.setMaxAccess(_C)
if mibBuilder.loadTexts:eventListStringElements.setStatus(_A)
_EventListCliScript_Type=DisplayString
_EventListCliScript_Object=MibTableColumn
eventListCliScript=_EventListCliScript_Object((1,3,6,1,4,1,3181,10,6,3,70,1,1,13),_EventListCliScript_Type())
eventListCliScript.setMaxAccess(_D)
if mibBuilder.loadTexts:eventListCliScript.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'management':management,'event':event,'eventListTable':eventListTable,'eventListEntry':eventListEntry,_G:eventListIndex,'eventListName':eventListName,'eventListGroup':eventListGroup,'eventListRelevance':eventListRelevance,'eventListInternal':eventListInternal,'eventListSeverity':eventListSeverity,'eventListSource':eventListSource,'eventListTrap':eventListTrap,'eventListSyslogMessage':eventListSyslogMessage,'eventListCustomMessage':eventListCustomMessage,'eventListIntegerElements':eventListIntegerElements,'eventListStringElements':eventListStringElements,'eventListCliScript':eventListCliScript})