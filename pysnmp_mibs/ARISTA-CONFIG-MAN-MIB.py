_P='aristaConfigManMibNotificationsGroup'
_O='aristaConfigEventDetailGroup'
_N='aristaConfigManEvent'
_M='aristaCmdHistoryEventTime'
_L='aristaCmdHistoryRunningLastChanged'
_K='aristaCmdHistoryEventIndex'
_J='Integer32'
_I='aristaCmdHistoryEventConfigDestURLScheme'
_H='aristaCmdHistoryEventConfigSourceURLScheme'
_G='aristaCmdHistoryEventConfigDestination'
_F='aristaCmdHistoryEventConfigSource'
_E='aristaCmdHistoryEventCommandSource'
_D='OctetString'
_C='read-only'
_B='current'
_A='ARISTA-CONFIG-MAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaConfigManMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,9))
if mibBuilder.loadTexts:aristaConfigManMIB.setRevisions(('2014-08-15 00:00','2014-05-06 13:00','2012-08-23 13:00'))
class ConfigHistoryEventMedium(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('none',0),('erase',1),('commandSource',2),('running',3),('startup',4),('url',5),('session',6)))
_AristaConfigManMIBObjects_ObjectIdentity=ObjectIdentity
aristaConfigManMIBObjects=_AristaConfigManMIBObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,9,1))
_AristaCmdHistory_ObjectIdentity=ObjectIdentity
aristaCmdHistory=_AristaCmdHistory_ObjectIdentity((1,3,6,1,4,1,30065,3,9,1,1))
_AristaCmdHistoryRunningLastChanged_Type=TimeTicks
_AristaCmdHistoryRunningLastChanged_Object=MibScalar
aristaCmdHistoryRunningLastChanged=_AristaCmdHistoryRunningLastChanged_Object((1,3,6,1,4,1,30065,3,9,1,1,1),_AristaCmdHistoryRunningLastChanged_Type())
aristaCmdHistoryRunningLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryRunningLastChanged.setStatus(_B)
_AristaCmdHistoryEventTable_Object=MibTable
aristaCmdHistoryEventTable=_AristaCmdHistoryEventTable_Object((1,3,6,1,4,1,30065,3,9,1,1,2))
if mibBuilder.loadTexts:aristaCmdHistoryEventTable.setStatus(_B)
_AristaCmdHistoryEventEntry_Object=MibTableRow
aristaCmdHistoryEventEntry=_AristaCmdHistoryEventEntry_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1))
aristaCmdHistoryEventEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:aristaCmdHistoryEventEntry.setStatus(_B)
_AristaCmdHistoryEventIndex_Type=Unsigned32
_AristaCmdHistoryEventIndex_Object=MibTableColumn
aristaCmdHistoryEventIndex=_AristaCmdHistoryEventIndex_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,1),_AristaCmdHistoryEventIndex_Type())
aristaCmdHistoryEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aristaCmdHistoryEventIndex.setStatus(_B)
_AristaCmdHistoryEventTime_Type=TimeTicks
_AristaCmdHistoryEventTime_Object=MibTableColumn
aristaCmdHistoryEventTime=_AristaCmdHistoryEventTime_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,2),_AristaCmdHistoryEventTime_Type())
aristaCmdHistoryEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventTime.setStatus(_B)
class _AristaCmdHistoryEventCommandSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('commandLine',0),('snmp',1)))
_AristaCmdHistoryEventCommandSource_Type.__name__=_J
_AristaCmdHistoryEventCommandSource_Object=MibTableColumn
aristaCmdHistoryEventCommandSource=_AristaCmdHistoryEventCommandSource_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,3),_AristaCmdHistoryEventCommandSource_Type())
aristaCmdHistoryEventCommandSource.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventCommandSource.setStatus(_B)
_AristaCmdHistoryEventConfigSource_Type=ConfigHistoryEventMedium
_AristaCmdHistoryEventConfigSource_Object=MibTableColumn
aristaCmdHistoryEventConfigSource=_AristaCmdHistoryEventConfigSource_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,4),_AristaCmdHistoryEventConfigSource_Type())
aristaCmdHistoryEventConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventConfigSource.setStatus(_B)
_AristaCmdHistoryEventConfigDestination_Type=ConfigHistoryEventMedium
_AristaCmdHistoryEventConfigDestination_Object=MibTableColumn
aristaCmdHistoryEventConfigDestination=_AristaCmdHistoryEventConfigDestination_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,5),_AristaCmdHistoryEventConfigDestination_Type())
aristaCmdHistoryEventConfigDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventConfigDestination.setStatus(_B)
class _AristaCmdHistoryEventConfigSourceURLScheme_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaCmdHistoryEventConfigSourceURLScheme_Type.__name__=_D
_AristaCmdHistoryEventConfigSourceURLScheme_Object=MibTableColumn
aristaCmdHistoryEventConfigSourceURLScheme=_AristaCmdHistoryEventConfigSourceURLScheme_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,6),_AristaCmdHistoryEventConfigSourceURLScheme_Type())
aristaCmdHistoryEventConfigSourceURLScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventConfigSourceURLScheme.setStatus(_B)
class _AristaCmdHistoryEventConfigDestURLScheme_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaCmdHistoryEventConfigDestURLScheme_Type.__name__=_D
_AristaCmdHistoryEventConfigDestURLScheme_Object=MibTableColumn
aristaCmdHistoryEventConfigDestURLScheme=_AristaCmdHistoryEventConfigDestURLScheme_Object((1,3,6,1,4,1,30065,3,9,1,1,2,1,7),_AristaCmdHistoryEventConfigDestURLScheme_Type())
aristaCmdHistoryEventConfigDestURLScheme.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaCmdHistoryEventConfigDestURLScheme.setStatus(_B)
_AristaConfigManMibConformance_ObjectIdentity=ObjectIdentity
aristaConfigManMibConformance=_AristaConfigManMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,9,2))
_AristaConfigManMibCompliances_ObjectIdentity=ObjectIdentity
aristaConfigManMibCompliances=_AristaConfigManMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,9,2,1))
_AristaConfigManMibGroups_ObjectIdentity=ObjectIdentity
aristaConfigManMibGroups=_AristaConfigManMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,9,2,1,2))
_AristaConfigManMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
aristaConfigManMIBNotificationPrefix=_AristaConfigManMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,30065,3,9,3))
_AristaConfigManMIBNotifications_ObjectIdentity=ObjectIdentity
aristaConfigManMIBNotifications=_AristaConfigManMIBNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,9,3,0))
aristaConfigEventDetailGroup=ObjectGroup((1,3,6,1,4,1,30065,3,9,2,1,2,1))
aristaConfigEventDetailGroup.setObjects(*((_A,_L),(_A,_M),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaConfigEventDetailGroup.setStatus(_B)
aristaConfigManEvent=NotificationType((1,3,6,1,4,1,30065,3,9,3,0,1))
aristaConfigManEvent.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaConfigManEvent.setStatus(_B)
aristaConfigManMibNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,9,2,1,2,2))
aristaConfigManMibNotificationsGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:aristaConfigManMibNotificationsGroup.setStatus(_B)
aristaConfigManMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,9,2,1,1))
aristaConfigManMibCompliance.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:aristaConfigManMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ConfigHistoryEventMedium':ConfigHistoryEventMedium,'aristaConfigManMIB':aristaConfigManMIB,'aristaConfigManMIBObjects':aristaConfigManMIBObjects,'aristaCmdHistory':aristaCmdHistory,_L:aristaCmdHistoryRunningLastChanged,'aristaCmdHistoryEventTable':aristaCmdHistoryEventTable,'aristaCmdHistoryEventEntry':aristaCmdHistoryEventEntry,_K:aristaCmdHistoryEventIndex,_M:aristaCmdHistoryEventTime,_E:aristaCmdHistoryEventCommandSource,_F:aristaCmdHistoryEventConfigSource,_G:aristaCmdHistoryEventConfigDestination,_H:aristaCmdHistoryEventConfigSourceURLScheme,_I:aristaCmdHistoryEventConfigDestURLScheme,'aristaConfigManMibConformance':aristaConfigManMibConformance,'aristaConfigManMibCompliances':aristaConfigManMibCompliances,'aristaConfigManMibCompliance':aristaConfigManMibCompliance,'aristaConfigManMibGroups':aristaConfigManMibGroups,_O:aristaConfigEventDetailGroup,_P:aristaConfigManMibNotificationsGroup,'aristaConfigManMIBNotificationPrefix':aristaConfigManMIBNotificationPrefix,'aristaConfigManMIBNotifications':aristaConfigManMIBNotifications,_N:aristaConfigManEvent})