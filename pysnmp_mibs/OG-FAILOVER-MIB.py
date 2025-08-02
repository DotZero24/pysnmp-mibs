_J='ogfovrNotificationsGroup'
_I='ogFailoverMibGroup'
_H='ogfovrEventOccurred'
_G='read-only'
_F='ogfovrEventIndex'
_E='Integer32'
_D='ogfovrEventSecondary'
_C='ogfovrEventPrimary'
_B='OG-FAILOVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogFailoverMib=ModuleIdentity((1,3,6,1,4,1,25049,10,15))
if mibBuilder.loadTexts:ogFailoverMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgFailoverMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogFailoverMibNotificationPrefix=_OgFailoverMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,15,2))
_OgfovrMibNotifications_ObjectIdentity=ObjectIdentity
ogfovrMibNotifications=_OgfovrMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,15,2,0))
_OgFailoverMibConformance_ObjectIdentity=ObjectIdentity
ogFailoverMibConformance=_OgFailoverMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,15,3))
_OgFailoverMibCompliances_ObjectIdentity=ObjectIdentity
ogFailoverMibCompliances=_OgFailoverMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,15,3,1))
_OgFailoverMibGroups_ObjectIdentity=ObjectIdentity
ogFailoverMibGroups=_OgFailoverMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,15,3,2))
_OgFailoverMibObjects_ObjectIdentity=ObjectIdentity
ogFailoverMibObjects=_OgFailoverMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,15,10))
_OgfovrEvent_ObjectIdentity=ObjectIdentity
ogfovrEvent=_OgfovrEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,15,10,1))
_OgfovrEventTable_Object=MibTable
ogfovrEventTable=_OgfovrEventTable_Object((1,3,6,1,4,1,25049,10,15,10,1,1))
if mibBuilder.loadTexts:ogfovrEventTable.setStatus(_A)
_OgfovrEventEntry_Object=MibTableRow
ogfovrEventEntry=_OgfovrEventEntry_Object((1,3,6,1,4,1,25049,10,15,10,1,1,1))
ogfovrEventEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ogfovrEventEntry.setStatus(_A)
class _OgfovrEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgfovrEventIndex_Type.__name__=_E
_OgfovrEventIndex_Object=MibTableColumn
ogfovrEventIndex=_OgfovrEventIndex_Object((1,3,6,1,4,1,25049,10,15,10,1,1,1,1),_OgfovrEventIndex_Type())
ogfovrEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogfovrEventIndex.setStatus(_A)
_OgfovrEventPrimary_Type=DisplayString
_OgfovrEventPrimary_Object=MibTableColumn
ogfovrEventPrimary=_OgfovrEventPrimary_Object((1,3,6,1,4,1,25049,10,15,10,1,1,1,10),_OgfovrEventPrimary_Type())
ogfovrEventPrimary.setMaxAccess(_G)
if mibBuilder.loadTexts:ogfovrEventPrimary.setStatus(_A)
_OgfovrEventSecondary_Type=DisplayString
_OgfovrEventSecondary_Object=MibTableColumn
ogfovrEventSecondary=_OgfovrEventSecondary_Object((1,3,6,1,4,1,25049,10,15,10,1,1,1,11),_OgfovrEventSecondary_Type())
ogfovrEventSecondary.setMaxAccess(_G)
if mibBuilder.loadTexts:ogfovrEventSecondary.setStatus(_A)
ogFailoverMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,15,3,2,1))
ogFailoverMibGroup.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:ogFailoverMibGroup.setStatus(_A)
ogfovrEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,15,2,0,200))
ogfovrEventOccurred.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:ogfovrEventOccurred.setStatus(_A)
ogfovrNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,15,3,2,2))
ogfovrNotificationsGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:ogfovrNotificationsGroup.setStatus(_A)
ogFailoverMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,15,3,1,1))
ogFailoverMibCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ogFailoverMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ogFailoverMib':ogFailoverMib,'ogFailoverMibNotificationPrefix':ogFailoverMibNotificationPrefix,'ogfovrMibNotifications':ogfovrMibNotifications,_H:ogfovrEventOccurred,'ogFailoverMibConformance':ogFailoverMibConformance,'ogFailoverMibCompliances':ogFailoverMibCompliances,'ogFailoverMibCompliance':ogFailoverMibCompliance,'ogFailoverMibGroups':ogFailoverMibGroups,_I:ogFailoverMibGroup,_J:ogfovrNotificationsGroup,'ogFailoverMibObjects':ogFailoverMibObjects,'ogfovrEvent':ogfovrEvent,'ogfovrEventTable':ogfovrEventTable,'ogfovrEventEntry':ogfovrEventEntry,_F:ogfovrEventIndex,_C:ogfovrEventPrimary,_D:ogfovrEventSecondary})