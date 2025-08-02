_T='temperatureStatusGroup'
_S='powerStatusGroup'
_R='pingStatusGroup'
_Q='eventStatusGroup'
_P='temperatureLow'
_O='temperatureHigh'
_N='powerSupplyLow'
_M='powerSupplyHigh'
_L='pingNotificationWarning'
_K='pingNotificationOK'
_J='Integer32'
_I='entPhySensorScale'
_H='entPhySensorPrecision'
_G='eventStatusTriggerId'
_F='entPhySensorValue'
_E='entPhysicalName'
_D='ENTITY-MIB'
_C='ENTITY-SENSOR-MIB'
_B='current'
_A='WESTERMO-EVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalName,=mibBuilder.importSymbols(_D,_E)
entPhySensorPrecision,entPhySensorScale,entPhySensorType,entPhySensorValue=mibBuilder.importSymbols(_C,_H,_I,'entPhySensorType',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
common,=mibBuilder.importSymbols('WESTERMO-OID-MIB','common')
event=ModuleIdentity((1,3,6,1,4,1,16177,2,3))
if mibBuilder.loadTexts:event.setRevisions(('2019-09-03 00:00',))
_EventStatus_ObjectIdentity=ObjectIdentity
eventStatus=_EventStatus_ObjectIdentity((1,3,6,1,4,1,16177,2,3,1))
_EventStatusTable_Object=MibTable
eventStatusTable=_EventStatusTable_Object((1,3,6,1,4,1,16177,2,3,1,1))
if mibBuilder.loadTexts:eventStatusTable.setStatus(_B)
_EventStatusEntry_Object=MibTableRow
eventStatusEntry=_EventStatusEntry_Object((1,3,6,1,4,1,16177,2,3,1,1,1))
eventStatusEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:eventStatusEntry.setStatus(_B)
class _EventStatusTriggerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EventStatusTriggerId_Type.__name__=_J
_EventStatusTriggerId_Object=MibTableColumn
eventStatusTriggerId=_EventStatusTriggerId_Object((1,3,6,1,4,1,16177,2,3,1,1,1,1),_EventStatusTriggerId_Type())
eventStatusTriggerId.setMaxAccess('read-only')
if mibBuilder.loadTexts:eventStatusTriggerId.setStatus(_B)
_EventConfig_ObjectIdentity=ObjectIdentity
eventConfig=_EventConfig_ObjectIdentity((1,3,6,1,4,1,16177,2,3,2))
_EventNotifications_ObjectIdentity=ObjectIdentity
eventNotifications=_EventNotifications_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3))
_PingNotifications_ObjectIdentity=ObjectIdentity
pingNotifications=_PingNotifications_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,2))
_PingNotificationPrefix_ObjectIdentity=ObjectIdentity
pingNotificationPrefix=_PingNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,2,0))
_PowerNotifications_ObjectIdentity=ObjectIdentity
powerNotifications=_PowerNotifications_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,3))
_PowerNotificationPrefix_ObjectIdentity=ObjectIdentity
powerNotificationPrefix=_PowerNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,3,0))
_TemperatureNotifications_ObjectIdentity=ObjectIdentity
temperatureNotifications=_TemperatureNotifications_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,4))
_TemperatureNotificationPrefix_ObjectIdentity=ObjectIdentity
temperatureNotificationPrefix=_TemperatureNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,16177,2,3,3,4,0))
_EventConformance_ObjectIdentity=ObjectIdentity
eventConformance=_EventConformance_ObjectIdentity((1,3,6,1,4,1,16177,2,3,4))
_EventGroups_ObjectIdentity=ObjectIdentity
eventGroups=_EventGroups_ObjectIdentity((1,3,6,1,4,1,16177,2,3,4,1))
_EventCompliances_ObjectIdentity=ObjectIdentity
eventCompliances=_EventCompliances_ObjectIdentity((1,3,6,1,4,1,16177,2,3,4,2))
eventStatusGroup=ObjectGroup((1,3,6,1,4,1,16177,2,3,4,1,1))
eventStatusGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:eventStatusGroup.setStatus(_B)
pingNotificationOK=NotificationType((1,3,6,1,4,1,16177,2,3,3,2,0,1))
pingNotificationOK.setObjects((_A,_G))
if mibBuilder.loadTexts:pingNotificationOK.setStatus(_B)
pingNotificationWarning=NotificationType((1,3,6,1,4,1,16177,2,3,3,2,0,2))
pingNotificationWarning.setObjects((_A,_G))
if mibBuilder.loadTexts:pingNotificationWarning.setStatus(_B)
powerSupplyHigh=NotificationType((1,3,6,1,4,1,16177,2,3,3,3,0,1))
powerSupplyHigh.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:powerSupplyHigh.setStatus(_B)
powerSupplyLow=NotificationType((1,3,6,1,4,1,16177,2,3,3,3,0,2))
powerSupplyLow.setObjects(*((_D,_E),(_C,_F)))
if mibBuilder.loadTexts:powerSupplyLow.setStatus(_B)
temperatureHigh=NotificationType((1,3,6,1,4,1,16177,2,3,3,4,0,1))
temperatureHigh.setObjects(*((_D,_E),(_C,_F),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:temperatureHigh.setStatus(_B)
temperatureLow=NotificationType((1,3,6,1,4,1,16177,2,3,3,4,0,2))
temperatureLow.setObjects(*((_D,_E),(_C,_F),(_C,_I),(_C,_H)))
if mibBuilder.loadTexts:temperatureLow.setStatus(_B)
pingStatusGroup=NotificationGroup((1,3,6,1,4,1,16177,2,3,4,1,2))
pingStatusGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:pingStatusGroup.setStatus(_B)
powerStatusGroup=NotificationGroup((1,3,6,1,4,1,16177,2,3,4,1,3))
powerStatusGroup.setObjects(*((_A,_M),(_A,_N)))
if mibBuilder.loadTexts:powerStatusGroup.setStatus(_B)
temperatureStatusGroup=NotificationGroup((1,3,6,1,4,1,16177,2,3,4,1,4))
temperatureStatusGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:temperatureStatusGroup.setStatus(_B)
eventCompliance=ModuleCompliance((1,3,6,1,4,1,16177,2,3,4,2,1))
eventCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:eventCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'event':event,'eventStatus':eventStatus,'eventStatusTable':eventStatusTable,'eventStatusEntry':eventStatusEntry,_G:eventStatusTriggerId,'eventConfig':eventConfig,'eventNotifications':eventNotifications,'pingNotifications':pingNotifications,'pingNotificationPrefix':pingNotificationPrefix,_K:pingNotificationOK,_L:pingNotificationWarning,'powerNotifications':powerNotifications,'powerNotificationPrefix':powerNotificationPrefix,_M:powerSupplyHigh,_N:powerSupplyLow,'temperatureNotifications':temperatureNotifications,'temperatureNotificationPrefix':temperatureNotificationPrefix,_O:temperatureHigh,_P:temperatureLow,'eventConformance':eventConformance,'eventGroups':eventGroups,_Q:eventStatusGroup,_R:pingStatusGroup,_S:powerStatusGroup,_T:temperatureStatusGroup,'eventCompliances':eventCompliances,'eventCompliance':eventCompliance})