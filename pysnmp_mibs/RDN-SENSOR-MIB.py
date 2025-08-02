_L='rdnSensorStatus'
_K='rdnSensorThresholdLow'
_J='rdnSensorThresholdHigh'
_I='rdnSensorValue'
_H='rdnSensorObjectID'
_G='rdnSensorDescr'
_F='read-write'
_E='rdnSensorIndex'
_D='Integer32'
_C='read-only'
_B='RDN-SENSOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
riverdelta,=mibBuilder.importSymbols('RDN-MIB','riverdelta')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnSensor=ModuleIdentity((1,3,6,1,4,1,4981,5))
if mibBuilder.loadTexts:rdnSensor.setRevisions(('2008-08-08 00:00','2003-11-05 00:00','2003-04-29 00:00','2001-08-07 00:00'))
_RdnSensorTable_Object=MibTable
rdnSensorTable=_RdnSensorTable_Object((1,3,6,1,4,1,4981,5,1))
if mibBuilder.loadTexts:rdnSensorTable.setStatus(_A)
_RdnSensorEntry_Object=MibTableRow
rdnSensorEntry=_RdnSensorEntry_Object((1,3,6,1,4,1,4981,5,1,1))
rdnSensorEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:rdnSensorEntry.setStatus(_A)
_RdnSensorIndex_Type=Integer32
_RdnSensorIndex_Object=MibTableColumn
rdnSensorIndex=_RdnSensorIndex_Object((1,3,6,1,4,1,4981,5,1,1,1),_RdnSensorIndex_Type())
rdnSensorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSensorIndex.setStatus(_A)
_RdnSensorDescr_Type=DisplayString
_RdnSensorDescr_Object=MibTableColumn
rdnSensorDescr=_RdnSensorDescr_Object((1,3,6,1,4,1,4981,5,1,1,2),_RdnSensorDescr_Type())
rdnSensorDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSensorDescr.setStatus(_A)
_RdnSensorObjectID_Type=ObjectIdentifier
_RdnSensorObjectID_Object=MibTableColumn
rdnSensorObjectID=_RdnSensorObjectID_Object((1,3,6,1,4,1,4981,5,1,1,3),_RdnSensorObjectID_Type())
rdnSensorObjectID.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSensorObjectID.setStatus(_A)
_RdnSensorValue_Type=Integer32
_RdnSensorValue_Object=MibTableColumn
rdnSensorValue=_RdnSensorValue_Object((1,3,6,1,4,1,4981,5,1,1,4),_RdnSensorValue_Type())
rdnSensorValue.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSensorValue.setStatus(_A)
_RdnSensorThresholdHigh_Type=Integer32
_RdnSensorThresholdHigh_Object=MibTableColumn
rdnSensorThresholdHigh=_RdnSensorThresholdHigh_Object((1,3,6,1,4,1,4981,5,1,1,5),_RdnSensorThresholdHigh_Type())
rdnSensorThresholdHigh.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnSensorThresholdHigh.setStatus(_A)
_RdnSensorThresholdLow_Type=Integer32
_RdnSensorThresholdLow_Object=MibTableColumn
rdnSensorThresholdLow=_RdnSensorThresholdLow_Object((1,3,6,1,4,1,4981,5,1,1,6),_RdnSensorThresholdLow_Type())
rdnSensorThresholdLow.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnSensorThresholdLow.setStatus(_A)
class _RdnSensorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('ok',2),('belowMin',3),('aboveMax',4),('defective',5),('notPresent',6)))
_RdnSensorStatus_Type.__name__=_D
_RdnSensorStatus_Object=MibTableColumn
rdnSensorStatus=_RdnSensorStatus_Object((1,3,6,1,4,1,4981,5,1,1,7),_RdnSensorStatus_Type())
rdnSensorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rdnSensorStatus.setStatus(_A)
class _RdnSensorNotificationEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_RdnSensorNotificationEnable_Type.__name__=_D
_RdnSensorNotificationEnable_Object=MibTableColumn
rdnSensorNotificationEnable=_RdnSensorNotificationEnable_Object((1,3,6,1,4,1,4981,5,1,1,8),_RdnSensorNotificationEnable_Type())
rdnSensorNotificationEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rdnSensorNotificationEnable.setStatus(_A)
_RdnSensorNotifications_ObjectIdentity=ObjectIdentity
rdnSensorNotifications=_RdnSensorNotifications_ObjectIdentity((1,3,6,1,4,1,4981,5,2))
_RdnSensorNotificationsPrefix_ObjectIdentity=ObjectIdentity
rdnSensorNotificationsPrefix=_RdnSensorNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,4981,5,2,0))
rdnSensorThresholdExceeded=NotificationType((1,3,6,1,4,1,4981,5,2,0,1))
rdnSensorThresholdExceeded.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rdnSensorThresholdExceeded.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rdnSensor':rdnSensor,'rdnSensorTable':rdnSensorTable,'rdnSensorEntry':rdnSensorEntry,_E:rdnSensorIndex,_G:rdnSensorDescr,_H:rdnSensorObjectID,_I:rdnSensorValue,_J:rdnSensorThresholdHigh,_K:rdnSensorThresholdLow,_L:rdnSensorStatus,'rdnSensorNotificationEnable':rdnSensorNotificationEnable,'rdnSensorNotifications':rdnSensorNotifications,'rdnSensorNotificationsPrefix':rdnSensorNotificationsPrefix,'rdnSensorThresholdExceeded':rdnSensorThresholdExceeded})