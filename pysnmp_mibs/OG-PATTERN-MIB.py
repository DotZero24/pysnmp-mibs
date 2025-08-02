_L='ogpatnNotificationsGroup'
_K='ogPatternMibGroup'
_J='ogpatnEventOccurred'
_I='ogpatnEventIndex'
_H='Integer32'
_G='ogpatnEventPortLabel'
_F='ogpatnEventPortNumber'
_E='ogpatnEventText'
_D='ogpatnEventDescription'
_C='read-only'
_B='current'
_A='OG-PATTERN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogPatternMib=ModuleIdentity((1,3,6,1,4,1,25049,10,12))
if mibBuilder.loadTexts:ogPatternMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgPatternMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogPatternMibNotificationPrefix=_OgPatternMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,12,2))
_OgpatnMibNotifications_ObjectIdentity=ObjectIdentity
ogpatnMibNotifications=_OgpatnMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,12,2,0))
_OgPatternMibConformance_ObjectIdentity=ObjectIdentity
ogPatternMibConformance=_OgPatternMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,12,3))
_OgPatternMibCompliances_ObjectIdentity=ObjectIdentity
ogPatternMibCompliances=_OgPatternMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,12,3,1))
_OgPatternMibGroups_ObjectIdentity=ObjectIdentity
ogPatternMibGroups=_OgPatternMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,12,3,2))
_OgPatternMibObjects_ObjectIdentity=ObjectIdentity
ogPatternMibObjects=_OgPatternMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,12,10))
_OgpatnEvent_ObjectIdentity=ObjectIdentity
ogpatnEvent=_OgpatnEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,12,10,1))
_OgpatnEventTable_Object=MibTable
ogpatnEventTable=_OgpatnEventTable_Object((1,3,6,1,4,1,25049,10,12,10,1,1))
if mibBuilder.loadTexts:ogpatnEventTable.setStatus(_B)
_OgpatnEventEntry_Object=MibTableRow
ogpatnEventEntry=_OgpatnEventEntry_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1))
ogpatnEventEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ogpatnEventEntry.setStatus(_B)
class _OgpatnEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgpatnEventIndex_Type.__name__=_H
_OgpatnEventIndex_Object=MibTableColumn
ogpatnEventIndex=_OgpatnEventIndex_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1,1),_OgpatnEventIndex_Type())
ogpatnEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogpatnEventIndex.setStatus(_B)
_OgpatnEventDescription_Type=DisplayString
_OgpatnEventDescription_Object=MibTableColumn
ogpatnEventDescription=_OgpatnEventDescription_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1,10),_OgpatnEventDescription_Type())
ogpatnEventDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ogpatnEventDescription.setStatus(_B)
_OgpatnEventText_Type=DisplayString
_OgpatnEventText_Object=MibTableColumn
ogpatnEventText=_OgpatnEventText_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1,11),_OgpatnEventText_Type())
ogpatnEventText.setMaxAccess(_C)
if mibBuilder.loadTexts:ogpatnEventText.setStatus(_B)
_OgpatnEventPortNumber_Type=Integer32
_OgpatnEventPortNumber_Object=MibTableColumn
ogpatnEventPortNumber=_OgpatnEventPortNumber_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1,12),_OgpatnEventPortNumber_Type())
ogpatnEventPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ogpatnEventPortNumber.setStatus(_B)
_OgpatnEventPortLabel_Type=DisplayString
_OgpatnEventPortLabel_Object=MibTableColumn
ogpatnEventPortLabel=_OgpatnEventPortLabel_Object((1,3,6,1,4,1,25049,10,12,10,1,1,1,13),_OgpatnEventPortLabel_Type())
ogpatnEventPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogpatnEventPortLabel.setStatus(_B)
ogPatternMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,12,3,2,1))
ogPatternMibGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogPatternMibGroup.setStatus(_B)
ogpatnEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,12,2,0,200))
ogpatnEventOccurred.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogpatnEventOccurred.setStatus(_B)
ogpatnNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,12,3,2,2))
ogpatnNotificationsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ogpatnNotificationsGroup.setStatus(_B)
ogPatternMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,12,3,1,1))
ogPatternMibCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogPatternMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogPatternMib':ogPatternMib,'ogPatternMibNotificationPrefix':ogPatternMibNotificationPrefix,'ogpatnMibNotifications':ogpatnMibNotifications,_J:ogpatnEventOccurred,'ogPatternMibConformance':ogPatternMibConformance,'ogPatternMibCompliances':ogPatternMibCompliances,'ogPatternMibCompliance':ogPatternMibCompliance,'ogPatternMibGroups':ogPatternMibGroups,_K:ogPatternMibGroup,_L:ogpatnNotificationsGroup,'ogPatternMibObjects':ogPatternMibObjects,'ogpatnEvent':ogpatnEvent,'ogpatnEventTable':ogpatnEventTable,'ogpatnEventEntry':ogpatnEventEntry,_I:ogpatnEventIndex,_D:ogpatnEventDescription,_E:ogpatnEventText,_F:ogpatnEventPortNumber,_G:ogpatnEventPortLabel})