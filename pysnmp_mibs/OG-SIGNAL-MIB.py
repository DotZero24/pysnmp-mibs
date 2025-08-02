_L='ogsgnlNotificationsGroup'
_K='ogSignalMibGroup'
_J='ogsgnlEventOccurred'
_I='ogsgnlEventIndex'
_H='Integer32'
_G='ogsgnlEventPortLabel'
_F='ogsgnlEventPortNumber'
_E='ogsgnlEventState'
_D='ogsgnlEventType'
_C='read-only'
_B='current'
_A='OG-SIGNAL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogSignalMib=ModuleIdentity((1,3,6,1,4,1,25049,10,11))
if mibBuilder.loadTexts:ogSignalMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgSignalMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogSignalMibNotificationPrefix=_OgSignalMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,11,2))
_OgsgnlMibNotifications_ObjectIdentity=ObjectIdentity
ogsgnlMibNotifications=_OgsgnlMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,11,2,0))
_OgSignalMibConformance_ObjectIdentity=ObjectIdentity
ogSignalMibConformance=_OgSignalMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,11,3))
_OgSignalMibCompliances_ObjectIdentity=ObjectIdentity
ogSignalMibCompliances=_OgSignalMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,11,3,1))
_OgSignalMibGroups_ObjectIdentity=ObjectIdentity
ogSignalMibGroups=_OgSignalMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,11,3,2))
_OgSignalMibObjects_ObjectIdentity=ObjectIdentity
ogSignalMibObjects=_OgSignalMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,11,10))
_OgsgnlEvent_ObjectIdentity=ObjectIdentity
ogsgnlEvent=_OgsgnlEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,11,10,1))
_OgsgnlEventTable_Object=MibTable
ogsgnlEventTable=_OgsgnlEventTable_Object((1,3,6,1,4,1,25049,10,11,10,1,1))
if mibBuilder.loadTexts:ogsgnlEventTable.setStatus(_B)
_OgsgnlEventEntry_Object=MibTableRow
ogsgnlEventEntry=_OgsgnlEventEntry_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1))
ogsgnlEventEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ogsgnlEventEntry.setStatus(_B)
class _OgsgnlEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgsgnlEventIndex_Type.__name__=_H
_OgsgnlEventIndex_Object=MibTableColumn
ogsgnlEventIndex=_OgsgnlEventIndex_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1,1),_OgsgnlEventIndex_Type())
ogsgnlEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogsgnlEventIndex.setStatus(_B)
_OgsgnlEventType_Type=DisplayString
_OgsgnlEventType_Object=MibTableColumn
ogsgnlEventType=_OgsgnlEventType_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1,10),_OgsgnlEventType_Type())
ogsgnlEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsgnlEventType.setStatus(_B)
_OgsgnlEventState_Type=DisplayString
_OgsgnlEventState_Object=MibTableColumn
ogsgnlEventState=_OgsgnlEventState_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1,11),_OgsgnlEventState_Type())
ogsgnlEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsgnlEventState.setStatus(_B)
_OgsgnlEventPortNumber_Type=Integer32
_OgsgnlEventPortNumber_Object=MibTableColumn
ogsgnlEventPortNumber=_OgsgnlEventPortNumber_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1,12),_OgsgnlEventPortNumber_Type())
ogsgnlEventPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsgnlEventPortNumber.setStatus(_B)
_OgsgnlEventPortLabel_Type=DisplayString
_OgsgnlEventPortLabel_Object=MibTableColumn
ogsgnlEventPortLabel=_OgsgnlEventPortLabel_Object((1,3,6,1,4,1,25049,10,11,10,1,1,1,13),_OgsgnlEventPortLabel_Type())
ogsgnlEventPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsgnlEventPortLabel.setStatus(_B)
ogSignalMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,11,3,2,1))
ogSignalMibGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogSignalMibGroup.setStatus(_B)
ogsgnlEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,11,2,0,200))
ogsgnlEventOccurred.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogsgnlEventOccurred.setStatus(_B)
ogsgnlNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,11,3,2,2))
ogsgnlNotificationsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ogsgnlNotificationsGroup.setStatus(_B)
ogSignalMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,11,3,1,1))
ogSignalMibCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogSignalMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogSignalMib':ogSignalMib,'ogSignalMibNotificationPrefix':ogSignalMibNotificationPrefix,'ogsgnlMibNotifications':ogsgnlMibNotifications,_J:ogsgnlEventOccurred,'ogSignalMibConformance':ogSignalMibConformance,'ogSignalMibCompliances':ogSignalMibCompliances,'ogSignalMibCompliance':ogSignalMibCompliance,'ogSignalMibGroups':ogSignalMibGroups,_K:ogSignalMibGroup,_L:ogsgnlNotificationsGroup,'ogSignalMibObjects':ogSignalMibObjects,'ogsgnlEvent':ogsgnlEvent,'ogsgnlEventTable':ogsgnlEventTable,'ogsgnlEventEntry':ogsgnlEventEntry,_I:ogsgnlEventIndex,_D:ogsgnlEventType,_E:ogsgnlEventState,_F:ogsgnlEventPortNumber,_G:ogsgnlEventPortLabel})