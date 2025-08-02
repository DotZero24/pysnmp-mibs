_L='ogdataNotificationsGroup'
_K='ogDataMibGroup'
_J='ogdataEventOccurred'
_I='ogdataEventIndex'
_H='ogdataEventState'
_G='ogdataEventDevice'
_F='ogdataEventSeconds'
_E='ogdataEventBytes'
_D='Integer32'
_C='read-only'
_B='current'
_A='OG-DATA-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogDataMib=ModuleIdentity((1,3,6,1,4,1,25049,10,17))
if mibBuilder.loadTexts:ogDataMib.setRevisions(('2013-08-11 00:00','2011-01-30 21:10'))
_OgDataMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogDataMibNotificationPrefix=_OgDataMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,17,2))
_OgdataMibNotifications_ObjectIdentity=ObjectIdentity
ogdataMibNotifications=_OgdataMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,17,2,0))
_OgDataMibConformance_ObjectIdentity=ObjectIdentity
ogDataMibConformance=_OgDataMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,17,3))
_OgDataMibCompliances_ObjectIdentity=ObjectIdentity
ogDataMibCompliances=_OgDataMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,17,3,1))
_OgDataMibGroups_ObjectIdentity=ObjectIdentity
ogDataMibGroups=_OgDataMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,17,3,2))
_OgDataMibObjects_ObjectIdentity=ObjectIdentity
ogDataMibObjects=_OgDataMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,17,10))
_OgdataEvent_ObjectIdentity=ObjectIdentity
ogdataEvent=_OgdataEvent_ObjectIdentity((1,3,6,1,4,1,25049,10,17,10,1))
_OgdataEventTable_Object=MibTable
ogdataEventTable=_OgdataEventTable_Object((1,3,6,1,4,1,25049,10,17,10,1,1))
if mibBuilder.loadTexts:ogdataEventTable.setStatus(_B)
_OgdataEventEntry_Object=MibTableRow
ogdataEventEntry=_OgdataEventEntry_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1))
ogdataEventEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ogdataEventEntry.setStatus(_B)
class _OgdataEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgdataEventIndex_Type.__name__=_D
_OgdataEventIndex_Object=MibTableColumn
ogdataEventIndex=_OgdataEventIndex_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1,1),_OgdataEventIndex_Type())
ogdataEventIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogdataEventIndex.setStatus(_B)
_OgdataEventBytes_Type=Integer32
_OgdataEventBytes_Object=MibTableColumn
ogdataEventBytes=_OgdataEventBytes_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1,10),_OgdataEventBytes_Type())
ogdataEventBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ogdataEventBytes.setStatus(_B)
_OgdataEventSeconds_Type=Integer32
_OgdataEventSeconds_Object=MibTableColumn
ogdataEventSeconds=_OgdataEventSeconds_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1,11),_OgdataEventSeconds_Type())
ogdataEventSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:ogdataEventSeconds.setStatus(_B)
_OgdataEventDevice_Type=DisplayString
_OgdataEventDevice_Object=MibTableColumn
ogdataEventDevice=_OgdataEventDevice_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1,12),_OgdataEventDevice_Type())
ogdataEventDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:ogdataEventDevice.setStatus(_B)
class _OgdataEventState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_OgdataEventState_Type.__name__=_D
_OgdataEventState_Object=MibTableColumn
ogdataEventState=_OgdataEventState_Object((1,3,6,1,4,1,25049,10,17,10,1,1,1,13),_OgdataEventState_Type())
ogdataEventState.setMaxAccess(_C)
if mibBuilder.loadTexts:ogdataEventState.setStatus(_B)
ogDataMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,17,3,2,1))
ogDataMibGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ogDataMibGroup.setStatus(_B)
ogdataEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,17,2,0,200))
ogdataEventOccurred.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:ogdataEventOccurred.setStatus(_B)
ogdataNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,17,3,2,2))
ogdataNotificationsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ogdataNotificationsGroup.setStatus(_B)
ogDataMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,17,3,1,1))
ogDataMibCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogDataMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogDataMib':ogDataMib,'ogDataMibNotificationPrefix':ogDataMibNotificationPrefix,'ogdataMibNotifications':ogdataMibNotifications,_J:ogdataEventOccurred,'ogDataMibConformance':ogDataMibConformance,'ogDataMibCompliances':ogDataMibCompliances,'ogDataMibCompliance':ogDataMibCompliance,'ogDataMibGroups':ogDataMibGroups,_K:ogDataMibGroup,_L:ogdataNotificationsGroup,'ogDataMibObjects':ogDataMibObjects,'ogdataEvent':ogdataEvent,'ogdataEventTable':ogdataEventTable,'ogdataEventEntry':ogdataEventEntry,_I:ogdataEventIndex,_E:ogdataEventBytes,_F:ogdataEventSeconds,_G:ogdataEventDevice,_H:ogdataEventState})