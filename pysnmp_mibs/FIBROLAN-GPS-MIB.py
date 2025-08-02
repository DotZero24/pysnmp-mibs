_K='flGpsAntennaState'
_J='flGpsState'
_I='flGpsSatelliteId'
_H='flGpsId'
_G='not-accessible'
_F='FIBROLAN-GPS-MIB'
_E='DisplayString'
_D='other'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FlGeoCoordinateAxis,fibrolanGeneric=mibBuilder.importSymbols('FIBROLAN-COMMON-MIB','FlGeoCoordinateAxis','fibrolanGeneric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention')
flGps=ModuleIdentity((1,3,6,1,4,1,4467,1000,210))
if mibBuilder.loadTexts:flGps.setRevisions(('2015-09-15 00:00','2015-08-10 00:00'))
_FlGpsNotifications_ObjectIdentity=ObjectIdentity
flGpsNotifications=_FlGpsNotifications_ObjectIdentity((1,3,6,1,4,1,4467,1000,210,0))
_FlGpsMIBObjects_ObjectIdentity=ObjectIdentity
flGpsMIBObjects=_FlGpsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4467,1000,210,1))
_FlGpsTable_Object=MibTable
flGpsTable=_FlGpsTable_Object((1,3,6,1,4,1,4467,1000,210,1,10))
if mibBuilder.loadTexts:flGpsTable.setStatus(_A)
_FlGpsEntry_Object=MibTableRow
flGpsEntry=_FlGpsEntry_Object((1,3,6,1,4,1,4467,1000,210,1,10,1))
flGpsEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:flGpsEntry.setStatus(_A)
class _FlGpsId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_FlGpsId_Type.__name__=_C
_FlGpsId_Object=MibTableColumn
flGpsId=_FlGpsId_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,1),_FlGpsId_Type())
flGpsId.setMaxAccess(_G)
if mibBuilder.loadTexts:flGpsId.setStatus(_A)
class _FlGpsModulePartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlGpsModulePartNumber_Type.__name__=_E
_FlGpsModulePartNumber_Object=MibTableColumn
flGpsModulePartNumber=_FlGpsModulePartNumber_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,2),_FlGpsModulePartNumber_Type())
flGpsModulePartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsModulePartNumber.setStatus(_A)
class _FlGpsModuleSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlGpsModuleSerialNumber_Type.__name__=_E
_FlGpsModuleSerialNumber_Object=MibTableColumn
flGpsModuleSerialNumber=_FlGpsModuleSerialNumber_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,3),_FlGpsModuleSerialNumber_Type())
flGpsModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsModuleSerialNumber.setStatus(_A)
class _FlGpsHardwareId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlGpsHardwareId_Type.__name__=_E
_FlGpsHardwareId_Object=MibTableColumn
flGpsHardwareId=_FlGpsHardwareId_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,4),_FlGpsHardwareId_Type())
flGpsHardwareId.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsHardwareId.setStatus(_A)
class _FlGpsFirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlGpsFirmwareVersion_Type.__name__=_E
_FlGpsFirmwareVersion_Object=MibTableColumn
flGpsFirmwareVersion=_FlGpsFirmwareVersion_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,5),_FlGpsFirmwareVersion_Type())
flGpsFirmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsFirmwareVersion.setStatus(_A)
class _FlGpsFirmwareDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FlGpsFirmwareDate_Type.__name__=_E
_FlGpsFirmwareDate_Object=MibTableColumn
flGpsFirmwareDate=_FlGpsFirmwareDate_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,6),_FlGpsFirmwareDate_Type())
flGpsFirmwareDate.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsFirmwareDate.setStatus(_A)
class _FlGpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('noSignal',1),('searching',2),('acquiring',3),('locked',4),('fail',5),(_D,99)))
_FlGpsState_Type.__name__=_C
_FlGpsState_Object=MibTableColumn
flGpsState=_FlGpsState_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,7),_FlGpsState_Type())
flGpsState.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsState.setStatus(_A)
_FlGpsStateLastChange_Type=TimeTicks
_FlGpsStateLastChange_Object=MibTableColumn
flGpsStateLastChange=_FlGpsStateLastChange_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,8),_FlGpsStateLastChange_Type())
flGpsStateLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsStateLastChange.setStatus(_A)
_FlGpsDateAndTime_Type=DateAndTime
_FlGpsDateAndTime_Object=MibTableColumn
flGpsDateAndTime=_FlGpsDateAndTime_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,9),_FlGpsDateAndTime_Type())
flGpsDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsDateAndTime.setStatus(_A)
_FlGpsLatitude_Type=FlGeoCoordinateAxis
_FlGpsLatitude_Object=MibTableColumn
flGpsLatitude=_FlGpsLatitude_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,10),_FlGpsLatitude_Type())
flGpsLatitude.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsLatitude.setStatus(_A)
_FlGpsLongitude_Type=FlGeoCoordinateAxis
_FlGpsLongitude_Object=MibTableColumn
flGpsLongitude=_FlGpsLongitude_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,11),_FlGpsLongitude_Type())
flGpsLongitude.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsLongitude.setStatus(_A)
class _FlGpsAltitude_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-500,10000))
_FlGpsAltitude_Type.__name__=_C
_FlGpsAltitude_Object=MibTableColumn
flGpsAltitude=_FlGpsAltitude_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,12),_FlGpsAltitude_Type())
flGpsAltitude.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsAltitude.setStatus(_A)
class _FlGpsCableDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FlGpsCableDelay_Type.__name__=_C
_FlGpsCableDelay_Object=MibTableColumn
flGpsCableDelay=_FlGpsCableDelay_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,13),_FlGpsCableDelay_Type())
flGpsCableDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsCableDelay.setStatus(_A)
class _FlGpsAntennaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('ok',1),('open',2),('shorted',3),(_D,99)))
_FlGpsAntennaState_Type.__name__=_C
_FlGpsAntennaState_Object=MibTableColumn
flGpsAntennaState=_FlGpsAntennaState_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,14),_FlGpsAntennaState_Type())
flGpsAntennaState.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsAntennaState.setStatus(_A)
class _FlGps1PpsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('ok',1),('notGenerated',2),(_D,99)))
_FlGps1PpsState_Type.__name__=_C
_FlGps1PpsState_Object=MibTableColumn
flGps1PpsState=_FlGps1PpsState_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,15),_FlGps1PpsState_Type())
flGps1PpsState.setMaxAccess(_B)
if mibBuilder.loadTexts:flGps1PpsState.setStatus(_A)
class _FlGpsTrackedSatelliteCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_FlGpsTrackedSatelliteCount_Type.__name__=_C
_FlGpsTrackedSatelliteCount_Object=MibTableColumn
flGpsTrackedSatelliteCount=_FlGpsTrackedSatelliteCount_Object((1,3,6,1,4,1,4467,1000,210,1,10,1,16),_FlGpsTrackedSatelliteCount_Type())
flGpsTrackedSatelliteCount.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsTrackedSatelliteCount.setStatus(_A)
_FlGpsSatelliteTable_Object=MibTable
flGpsSatelliteTable=_FlGpsSatelliteTable_Object((1,3,6,1,4,1,4467,1000,210,1,30))
if mibBuilder.loadTexts:flGpsSatelliteTable.setStatus(_A)
_FlGpsSatelliteEntry_Object=MibTableRow
flGpsSatelliteEntry=_FlGpsSatelliteEntry_Object((1,3,6,1,4,1,4467,1000,210,1,30,1))
flGpsSatelliteEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:flGpsSatelliteEntry.setStatus(_A)
class _FlGpsSatelliteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FlGpsSatelliteId_Type.__name__=_C
_FlGpsSatelliteId_Object=MibTableColumn
flGpsSatelliteId=_FlGpsSatelliteId_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,2),_FlGpsSatelliteId_Type())
flGpsSatelliteId.setMaxAccess(_G)
if mibBuilder.loadTexts:flGpsSatelliteId.setStatus(_A)
class _FlGpsSatellitePrn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FlGpsSatellitePrn_Type.__name__=_C
_FlGpsSatellitePrn_Object=MibTableColumn
flGpsSatellitePrn=_FlGpsSatellitePrn_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,3),_FlGpsSatellitePrn_Type())
flGpsSatellitePrn.setMaxAccess(_G)
if mibBuilder.loadTexts:flGpsSatellitePrn.setStatus(_A)
class _FlGpsSatelliteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,99)));namedValues=NamedValues(*(('gps',1),('glonass',2),('galileo',3),('beidou',4),('qzss',5),(_D,99)))
_FlGpsSatelliteType_Type.__name__=_C
_FlGpsSatelliteType_Object=MibTableColumn
flGpsSatelliteType=_FlGpsSatelliteType_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,4),_FlGpsSatelliteType_Type())
flGpsSatelliteType.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteType.setStatus(_A)
class _FlGpsSatelliteChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FlGpsSatelliteChannel_Type.__name__=_C
_FlGpsSatelliteChannel_Object=MibTableColumn
flGpsSatelliteChannel=_FlGpsSatelliteChannel_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,5),_FlGpsSatelliteChannel_Type())
flGpsSatelliteChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteChannel.setStatus(_A)
class _FlGpsSatelliteAcquisitionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,99)));namedValues=NamedValues(*(('acquired',1),('neverAcquired',2),('reopenSearch',3),(_D,99)))
_FlGpsSatelliteAcquisitionState_Type.__name__=_C
_FlGpsSatelliteAcquisitionState_Object=MibTableColumn
flGpsSatelliteAcquisitionState=_FlGpsSatelliteAcquisitionState_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,6),_FlGpsSatelliteAcquisitionState_Type())
flGpsSatelliteAcquisitionState.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteAcquisitionState.setStatus(_A)
class _FlGpsSatelliteSignalLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FlGpsSatelliteSignalLevel_Type.__name__=_C
_FlGpsSatelliteSignalLevel_Object=MibTableColumn
flGpsSatelliteSignalLevel=_FlGpsSatelliteSignalLevel_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,7),_FlGpsSatelliteSignalLevel_Type())
flGpsSatelliteSignalLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteSignalLevel.setStatus(_A)
class _FlGpsSatelliteElevationAngle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_FlGpsSatelliteElevationAngle_Type.__name__=_C
_FlGpsSatelliteElevationAngle_Object=MibTableColumn
flGpsSatelliteElevationAngle=_FlGpsSatelliteElevationAngle_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,8),_FlGpsSatelliteElevationAngle_Type())
flGpsSatelliteElevationAngle.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteElevationAngle.setStatus(_A)
class _FlGpsSatelliteAzimuthAngle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,180))
_FlGpsSatelliteAzimuthAngle_Type.__name__=_C
_FlGpsSatelliteAzimuthAngle_Object=MibTableColumn
flGpsSatelliteAzimuthAngle=_FlGpsSatelliteAzimuthAngle_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,9),_FlGpsSatelliteAzimuthAngle_Type())
flGpsSatelliteAzimuthAngle.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteAzimuthAngle.setStatus(_A)
class _FlGpsSatelliteUsedForTiming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('yes',1),('no',2),(_D,99)))
_FlGpsSatelliteUsedForTiming_Type.__name__=_C
_FlGpsSatelliteUsedForTiming_Object=MibTableColumn
flGpsSatelliteUsedForTiming=_FlGpsSatelliteUsedForTiming_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,10),_FlGpsSatelliteUsedForTiming_Type())
flGpsSatelliteUsedForTiming.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteUsedForTiming.setStatus(_A)
class _FlGpsSatelliteUsedForPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,99)));namedValues=NamedValues(*(('yes',1),('no',2),(_D,99)))
_FlGpsSatelliteUsedForPosition_Type.__name__=_C
_FlGpsSatelliteUsedForPosition_Object=MibTableColumn
flGpsSatelliteUsedForPosition=_FlGpsSatelliteUsedForPosition_Object((1,3,6,1,4,1,4467,1000,210,1,30,1,11),_FlGpsSatelliteUsedForPosition_Type())
flGpsSatelliteUsedForPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:flGpsSatelliteUsedForPosition.setStatus(_A)
flGpsStateChanged=NotificationType((1,3,6,1,4,1,4467,1000,210,0,10))
flGpsStateChanged.setObjects((_F,_J))
if mibBuilder.loadTexts:flGpsStateChanged.setStatus(_A)
flGpsAntennaStateChanged=NotificationType((1,3,6,1,4,1,4467,1000,210,0,20))
flGpsAntennaStateChanged.setObjects((_F,_K))
if mibBuilder.loadTexts:flGpsAntennaStateChanged.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'flGps':flGps,'flGpsNotifications':flGpsNotifications,'flGpsStateChanged':flGpsStateChanged,'flGpsAntennaStateChanged':flGpsAntennaStateChanged,'flGpsMIBObjects':flGpsMIBObjects,'flGpsTable':flGpsTable,'flGpsEntry':flGpsEntry,_H:flGpsId,'flGpsModulePartNumber':flGpsModulePartNumber,'flGpsModuleSerialNumber':flGpsModuleSerialNumber,'flGpsHardwareId':flGpsHardwareId,'flGpsFirmwareVersion':flGpsFirmwareVersion,'flGpsFirmwareDate':flGpsFirmwareDate,_J:flGpsState,'flGpsStateLastChange':flGpsStateLastChange,'flGpsDateAndTime':flGpsDateAndTime,'flGpsLatitude':flGpsLatitude,'flGpsLongitude':flGpsLongitude,'flGpsAltitude':flGpsAltitude,'flGpsCableDelay':flGpsCableDelay,_K:flGpsAntennaState,'flGps1PpsState':flGps1PpsState,'flGpsTrackedSatelliteCount':flGpsTrackedSatelliteCount,'flGpsSatelliteTable':flGpsSatelliteTable,'flGpsSatelliteEntry':flGpsSatelliteEntry,_I:flGpsSatelliteId,'flGpsSatellitePrn':flGpsSatellitePrn,'flGpsSatelliteType':flGpsSatelliteType,'flGpsSatelliteChannel':flGpsSatelliteChannel,'flGpsSatelliteAcquisitionState':flGpsSatelliteAcquisitionState,'flGpsSatelliteSignalLevel':flGpsSatelliteSignalLevel,'flGpsSatelliteElevationAngle':flGpsSatelliteElevationAngle,'flGpsSatelliteAzimuthAngle':flGpsSatelliteAzimuthAngle,'flGpsSatelliteUsedForTiming':flGpsSatelliteUsedForTiming,'flGpsSatelliteUsedForPosition':flGpsSatelliteUsedForPosition})