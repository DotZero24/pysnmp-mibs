_L='ogsensNotificationsGroup'
_K='ogSensorMibGroup'
_J='ogsensEventOccurred'
_I='ogsensStatusIndex'
_H='Integer32'
_G='ogsensStatusValue'
_F='ogsensStatusType'
_E='ogsensStatusDevType'
_D='ogsensStatusName'
_C='read-only'
_B='current'
_A='OG-SENSOR-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ogMgmt,=mibBuilder.importSymbols('OG-SMI-MIB','ogMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ogSensorMib=ModuleIdentity((1,3,6,1,4,1,25049,10,13))
if mibBuilder.loadTexts:ogSensorMib.setRevisions(('2013-08-11 00:00','2010-03-22 11:27','2008-11-27 11:40'))
_OgSensorMibNotificationPrefix_ObjectIdentity=ObjectIdentity
ogSensorMibNotificationPrefix=_OgSensorMibNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,25049,10,13,2))
_OgsensMibNotifications_ObjectIdentity=ObjectIdentity
ogsensMibNotifications=_OgsensMibNotifications_ObjectIdentity((1,3,6,1,4,1,25049,10,13,2,0))
_OgSensorMibConformance_ObjectIdentity=ObjectIdentity
ogSensorMibConformance=_OgSensorMibConformance_ObjectIdentity((1,3,6,1,4,1,25049,10,13,3))
_OgSensorMibCompliances_ObjectIdentity=ObjectIdentity
ogSensorMibCompliances=_OgSensorMibCompliances_ObjectIdentity((1,3,6,1,4,1,25049,10,13,3,1))
_OgSensorMibGroups_ObjectIdentity=ObjectIdentity
ogSensorMibGroups=_OgSensorMibGroups_ObjectIdentity((1,3,6,1,4,1,25049,10,13,3,2))
_OgSensorMibObjects_ObjectIdentity=ObjectIdentity
ogSensorMibObjects=_OgSensorMibObjects_ObjectIdentity((1,3,6,1,4,1,25049,10,13,10))
_OgsensStatus_ObjectIdentity=ObjectIdentity
ogsensStatus=_OgsensStatus_ObjectIdentity((1,3,6,1,4,1,25049,10,13,10,1))
_OgsensStatusTable_Object=MibTable
ogsensStatusTable=_OgsensStatusTable_Object((1,3,6,1,4,1,25049,10,13,10,1,3))
if mibBuilder.loadTexts:ogsensStatusTable.setStatus(_B)
_OgsensStatusEntry_Object=MibTableRow
ogsensStatusEntry=_OgsensStatusEntry_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1))
ogsensStatusEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:ogsensStatusEntry.setStatus(_B)
class _OgsensStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OgsensStatusIndex_Type.__name__=_H
_OgsensStatusIndex_Object=MibTableColumn
ogsensStatusIndex=_OgsensStatusIndex_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1,1),_OgsensStatusIndex_Type())
ogsensStatusIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ogsensStatusIndex.setStatus(_B)
_OgsensStatusName_Type=DisplayString
_OgsensStatusName_Object=MibTableColumn
ogsensStatusName=_OgsensStatusName_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1,10),_OgsensStatusName_Type())
ogsensStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsensStatusName.setStatus(_B)
_OgsensStatusDevType_Type=DisplayString
_OgsensStatusDevType_Object=MibTableColumn
ogsensStatusDevType=_OgsensStatusDevType_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1,11),_OgsensStatusDevType_Type())
ogsensStatusDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsensStatusDevType.setStatus(_B)
_OgsensStatusType_Type=DisplayString
_OgsensStatusType_Object=MibTableColumn
ogsensStatusType=_OgsensStatusType_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1,12),_OgsensStatusType_Type())
ogsensStatusType.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsensStatusType.setStatus(_B)
_OgsensStatusValue_Type=Integer32
_OgsensStatusValue_Object=MibTableColumn
ogsensStatusValue=_OgsensStatusValue_Object((1,3,6,1,4,1,25049,10,13,10,1,3,1,13),_OgsensStatusValue_Type())
ogsensStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ogsensStatusValue.setStatus(_B)
ogSensorMibGroup=ObjectGroup((1,3,6,1,4,1,25049,10,13,3,2,1))
ogSensorMibGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogSensorMibGroup.setStatus(_B)
ogsensEventOccurred=NotificationType((1,3,6,1,4,1,25049,10,13,2,0,200))
ogsensEventOccurred.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ogsensEventOccurred.setStatus(_B)
ogsensNotificationsGroup=NotificationGroup((1,3,6,1,4,1,25049,10,13,3,2,2))
ogsensNotificationsGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:ogsensNotificationsGroup.setStatus(_B)
ogSensorMibCompliance=ModuleCompliance((1,3,6,1,4,1,25049,10,13,3,1,1))
ogSensorMibCompliance.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ogSensorMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ogSensorMib':ogSensorMib,'ogSensorMibNotificationPrefix':ogSensorMibNotificationPrefix,'ogsensMibNotifications':ogsensMibNotifications,_J:ogsensEventOccurred,'ogSensorMibConformance':ogSensorMibConformance,'ogSensorMibCompliances':ogSensorMibCompliances,'ogSensorMibCompliance':ogSensorMibCompliance,'ogSensorMibGroups':ogSensorMibGroups,_K:ogSensorMibGroup,_L:ogsensNotificationsGroup,'ogSensorMibObjects':ogSensorMibObjects,'ogsensStatus':ogsensStatus,'ogsensStatusTable':ogsensStatusTable,'ogsensStatusEntry':ogsensStatusEntry,_I:ogsensStatusIndex,_D:ogsensStatusName,_E:ogsensStatusDevType,_F:ogsensStatusType,_G:ogsensStatusValue})