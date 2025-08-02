_J='ognupsNotificationsGroup'
_I='ogNetUpsMibGroup'
_H='ognupsEventOccurred'
_G='read-only'
_F='ognupsEventIndex'
_E='Integer32'
_D='ognupsEventType'
_C='ognupsEventName'
_B='OG-UPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogNetUpsMib=ModuleIdentity((1,3,6,1,4,1,25049,10,16))
if mibBuilder.loadTexts:ogNetUpsMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-06-13 11:00'))
_OgNetUpsMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogNetUpsMibNotificationPrefix=_OgNetUpsMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,16,2))
_OgnupsMibNotifications_ObjectIdentity=ObjectIdentity
ognupsMibNotifications=_OgnupsMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,16,2,0))
_OgNetUpsMibConformance_ObjectIdentity=ObjectIdentity
ogNetUpsMibConformance=_OgNetUpsMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,16,3))
_OgNetUpsMibCompliances_ObjectIdentity=ObjectIdentity
ogNetUpsMibCompliances=_OgNetUpsMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,16,3,1))
_OgNetUpsMibGroups_ObjectIdentity=ObjectIdentity
ogNetUpsMibGroups=_OgNetUpsMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,16,3,2))
_OgNetUpsMibObjects_ObjectIdentity=ObjectIdentity
ogNetUpsMibObjects=_OgNetUpsMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,16,10))
_OgnupsEvent_ObjectIdentity=ObjectIdentity
ognupsEvent=_OgnupsEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,16,10,1))
_OgnupsEventTable_Object=MibTable
ognupsEventTable=_OgnupsEventTable_Object((1,3,6,1,4,1,25049,10,16,10,1,1))
if mibBuilder.loadTexts:ognupsEventTable.setStatus(_A)
_OgnupsEventEntry_Object=MibTableRow
ognupsEventEntry=_OgnupsEventEntry_Object((1,3,6,1,4,1,25049,10,16,10,1,1,1))
ognupsEventEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ognupsEventEntry.setStatus(_A)
class _OgnupsEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgnupsEventIndex_Type.__name__=_E
_OgnupsEventIndex_Object=MibTableColumn
ognupsEventIndex=_OgnupsEventIndex_Object((1,3,6,1,4,1,25049,10,16,10,1,1,1,1),_OgnupsEventIndex_Type())
ognupsEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ognupsEventIndex.setStatus(_A)
_OgnupsEventName_Type=DisplayString
_OgnupsEventName_Object=MibTableColumn
ognupsEventName=_OgnupsEventName_Object((1,3,6,1,4,1,25049,10,16,10,1,1,1,10),_OgnupsEventName_Type())
ognupsEventName.setMaxAccess(_G)
if mibBuilder.loadTexts:ognupsEventName.setStatus(_A)
_OgnupsEventType_Type=DisplayString
_OgnupsEventType_Object=MibTableColumn
ognupsEventType=_OgnupsEventType_Object((1,3,6,1,4,1,25049,10,16,10,1,1,1,11),_OgnupsEventType_Type())
ognupsEventType.setMaxAccess(_G)
if mibBuilder.loadTexts:ognupsEventType.setStatus(_A)
ogNetUpsMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,16,3,2,1))
ogNetUpsMibGroup.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:ogNetUpsMibGroup.setStatus(_A)
ognupsEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,16,2,0,200))
ognupsEventOccurred.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:ognupsEventOccurred.setStatus(_A)
ognupsNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,16,3,2,2))
ognupsNotificationsGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:ognupsNotificationsGroup.setStatus(_A)
ogNetUpsMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,16,3,1,1))
ogNetUpsMibCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ogNetUpsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ogNetUpsMib':ogNetUpsMib,'ogNetUpsMibNotificationPrefix':ogNetUpsMibNotificationPrefix,'ognupsMibNotifications':ognupsMibNotifications,_H:ognupsEventOccurred,'ogNetUpsMibConformance':ogNetUpsMibConformance,'ogNetUpsMibCompliances':ogNetUpsMibCompliances,'ogNetUpsMibCompliance':ogNetUpsMibCompliance,'ogNetUpsMibGroups':ogNetUpsMibGroups,_I:ogNetUpsMibGroup,_J:ognupsNotificationsGroup,'ogNetUpsMibObjects':ogNetUpsMibObjects,'ognupsEvent':ognupsEvent,'ognupsEventTable':ognupsEventTable,'ognupsEventEntry':ognupsEventEntry,_F:ognupsEventIndex,_C:ognupsEventName,_D:ognupsEventType})