_L='ogconnNotificationsGroup'
_K='ogConnectMibGroup'
_J='ogconnEventOccurred'
_I='ogconnEventIndex'
_H='Integer32'
_G='ogconnEventPortLabel'
_F='ogconnEventPortNumber'
_E='ogconnEventType'
_D='ogconnEventUsername'
_C='read-only'
_B='current'
_A='OG-CONNECT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogConnectMib=ModuleIdentity((1,3,6,1,4,1,25049,10,10))
if mibBuilder.loadTexts:ogConnectMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgConnectMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogConnectMibNotificationPrefix=_OgConnectMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,10,2))
_OgconnMibNotifications_ObjectIdentity=ObjectIdentity
ogconnMibNotifications=_OgconnMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,10,2,0))
_OgConnectMibConformance_ObjectIdentity=ObjectIdentity
ogConnectMibConformance=_OgConnectMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,10,3))
_OgConnectMibCompliances_ObjectIdentity=ObjectIdentity
ogConnectMibCompliances=_OgConnectMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,10,3,1))
_OgConnectMibGroups_ObjectIdentity=ObjectIdentity
ogConnectMibGroups=_OgConnectMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,10,3,2))
_OgConnectMibObjects_ObjectIdentity=ObjectIdentity
ogConnectMibObjects=_OgConnectMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,10,10))
_OgconnEvent_ObjectIdentity=ObjectIdentity
ogconnEvent=_OgconnEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,10,10,1))
_OgconnEventTable_Object=MibTable
ogconnEventTable=_OgconnEventTable_Object((1,3,6,1,4,1,25049,10,10,10,1,1))
if mibBuilder.loadTexts:ogconnEventTable.setStatus(_B)
_OgconnEventEntry_Object=MibTableRow
ogconnEventEntry=_OgconnEventEntry_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1))
ogconnEventEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ogconnEventEntry.setStatus(_B)
class _OgconnEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgconnEventIndex_Type.__name__=_H
_OgconnEventIndex_Object=MibTableColumn
ogconnEventIndex=_OgconnEventIndex_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1,1),_OgconnEventIndex_Type())
ogconnEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogconnEventIndex.setStatus(_B)
_OgconnEventUsername_Type=DisplayString
_OgconnEventUsername_Object=MibTableColumn
ogconnEventUsername=_OgconnEventUsername_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1,10),_OgconnEventUsername_Type())
ogconnEventUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:ogconnEventUsername.setStatus(_B)
_OgconnEventType_Type=DisplayString
_OgconnEventType_Object=MibTableColumn
ogconnEventType=_OgconnEventType_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1,11),_OgconnEventType_Type())
ogconnEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:ogconnEventType.setStatus(_B)
_OgconnEventPortNumber_Type=Integer32
_OgconnEventPortNumber_Object=MibTableColumn
ogconnEventPortNumber=_OgconnEventPortNumber_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1,12),_OgconnEventPortNumber_Type())
ogconnEventPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ogconnEventPortNumber.setStatus(_B)
_OgconnEventPortLabel_Type=DisplayString
_OgconnEventPortLabel_Object=MibTableColumn
ogconnEventPortLabel=_OgconnEventPortLabel_Object((1,3,6,1,4,1,25049,10,10,10,1,1,1,13),_OgconnEventPortLabel_Type())
ogconnEventPortLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:ogconnEventPortLabel.setStatus(_B)
ogConnectMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,10,3,2,1))
ogConnectMibGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogConnectMibGroup.setStatus(_B)
ogconnEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,10,2,0,200))
ogconnEventOccurred.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogconnEventOccurred.setStatus(_B)
ogconnNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,10,3,2,2))
ogconnNotificationsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ogconnNotificationsGroup.setStatus(_B)
ogConnectMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,10,3,1,1))
ogConnectMibCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogConnectMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogConnectMib':ogConnectMib,'ogConnectMibNotificationPrefix':ogConnectMibNotificationPrefix,'ogconnMibNotifications':ogconnMibNotifications,_J:ogconnEventOccurred,'ogConnectMibConformance':ogConnectMibConformance,'ogConnectMibCompliances':ogConnectMibCompliances,'ogConnectMibCompliance':ogConnectMibCompliance,'ogConnectMibGroups':ogConnectMibGroups,_K:ogConnectMibGroup,_L:ogconnNotificationsGroup,'ogConnectMibObjects':ogConnectMibObjects,'ogconnEvent':ogconnEvent,'ogconnEventTable':ogconnEventTable,'ogconnEventEntry':ogconnEventEntry,_I:ogconnEventIndex,_D:ogconnEventUsername,_E:ogconnEventType,_F:ogconnEventPortNumber,_G:ogconnEventPortLabel})