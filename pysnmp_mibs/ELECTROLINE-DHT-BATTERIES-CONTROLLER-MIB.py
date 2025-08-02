_b='battManBattLogBatteryID'
_a='battManBattLogStringID'
_Z='battManBattLogDatasetID'
_Y='battManBattLogDeviceAddress'
_X='battManManualMeasDeviceAddress'
_W='battManEnvStatusDeviceAddress'
_V='battManStatusDeviceAddress'
_U='battManControlDeviceAddress'
_T='battManBatteryDiagModuleID'
_S='battManBatteryDiagDeviceAddress'
_R='battManBattery'
_Q='battManBatteryStringID'
_P='battManBatteryDeviceAddress'
_O='battManString'
_N='battManStringDeviceAddress'
_M='battManDeviceAddress'
_L='DisplayString'
_K='false'
_J='true'
_I='current'
_H='OctetString'
_G='read-write'
_F='supported'
_E='none'
_D='Integer32'
_C='ELECTROLINE-DHT-BATTERIES-CONTROLLER-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtExtensionsMibObjects,=mibBuilder.importSymbols('ELECTROLINE-DHT-EXTENSIONS-MIB','dhtExtensionsMibObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_L,'PhysAddress','TextualConvention','TruthValue')
battManIdentMIB=ModuleIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,16))
if mibBuilder.loadTexts:battManIdentMIB.setRevisions(('2015-03-19 00:00','2015-04-20 00:00','2015-08-20 00:00'))
class HundredthmOhm(TextualConvention,Integer32):status=_I;displayHint='d-2'
class HundredthkS(TextualConvention,Integer32):status=_I;displayHint='d-2'
_BattManIdentObjects_ObjectIdentity=ObjectIdentity
battManIdentObjects=_BattManIdentObjects_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1))
_BattManMonitored_Type=Integer32
_BattManMonitored_Object=MibScalar
battManMonitored=_BattManMonitored_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,1),_BattManMonitored_Type())
battManMonitored.setMaxAccess(_B)
if mibBuilder.loadTexts:battManMonitored.setStatus(_A)
_BattManDeviceTable_Object=MibTable
battManDeviceTable=_BattManDeviceTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2))
if mibBuilder.loadTexts:battManDeviceTable.setStatus(_A)
_BattManDeviceEntry_Object=MibTableRow
battManDeviceEntry=_BattManDeviceEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1))
battManDeviceEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:battManDeviceEntry.setStatus(_A)
class _BattManDeviceAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(17,127))
_BattManDeviceAddress_Type.__name__=_D
_BattManDeviceAddress_Object=MibTableColumn
battManDeviceAddress=_BattManDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,1),_BattManDeviceAddress_Type())
battManDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManDeviceAddress.setStatus(_A)
class _BattManProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_BattManProtocolVersion_Type.__name__=_D
_BattManProtocolVersion_Object=MibTableColumn
battManProtocolVersion=_BattManProtocolVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,2),_BattManProtocolVersion_Type())
battManProtocolVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:battManProtocolVersion.setStatus(_A)
class _BattManSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_BattManSoftwareVersion_Type.__name__=_H
_BattManSoftwareVersion_Object=MibTableColumn
battManSoftwareVersion=_BattManSoftwareVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,3),_BattManSoftwareVersion_Type())
battManSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:battManSoftwareVersion.setStatus(_A)
class _BattManDeviceId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_BattManDeviceId_Type.__name__=_H
_BattManDeviceId_Object=MibTableColumn
battManDeviceId=_BattManDeviceId_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,4),_BattManDeviceId_Type())
battManDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:battManDeviceId.setStatus(_A)
class _BattManVendorIdentity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_BattManVendorIdentity_Type.__name__=_L
_BattManVendorIdentity_Object=MibTableColumn
battManVendorIdentity=_BattManVendorIdentity_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,5),_BattManVendorIdentity_Type())
battManVendorIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:battManVendorIdentity.setStatus(_A)
_BattManStringVoltage_Type=Integer32
_BattManStringVoltage_Object=MibTableColumn
battManStringVoltage=_BattManStringVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,6),_BattManStringVoltage_Type())
battManStringVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStringVoltage.setStatus(_A)
_BattManBatteries_Type=Integer32
_BattManBatteries_Object=MibTableColumn
battManBatteries=_BattManBatteries_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,7),_BattManBatteries_Type())
battManBatteries.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteries.setStatus(_A)
_BattManBatteryStrings_Type=Integer32
_BattManBatteryStrings_Object=MibTableColumn
battManBatteryStrings=_BattManBatteryStrings_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,8),_BattManBatteryStrings_Type())
battManBatteryStrings.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryStrings.setStatus(_A)
_BattManBatteriesPerStrings_Type=Integer32
_BattManBatteriesPerStrings_Object=MibTableColumn
battManBatteriesPerStrings=_BattManBatteriesPerStrings_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,9),_BattManBatteriesPerStrings_Type())
battManBatteriesPerStrings.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteriesPerStrings.setStatus(_A)
class _BattManVoltageSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManVoltageSupport_Type.__name__=_D
_BattManVoltageSupport_Object=MibTableColumn
battManVoltageSupport=_BattManVoltageSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,10),_BattManVoltageSupport_Type())
battManVoltageSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManVoltageSupport.setStatus(_A)
class _BattManTemperatureSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManTemperatureSupport_Type.__name__=_D
_BattManTemperatureSupport_Object=MibTableColumn
battManTemperatureSupport=_BattManTemperatureSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,11),_BattManTemperatureSupport_Type())
battManTemperatureSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManTemperatureSupport.setStatus(_A)
class _BattManImpedanceSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManImpedanceSupport_Type.__name__=_D
_BattManImpedanceSupport_Object=MibTableColumn
battManImpedanceSupport=_BattManImpedanceSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,12),_BattManImpedanceSupport_Type())
battManImpedanceSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManImpedanceSupport.setStatus(_A)
class _BattManEqualPercentSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManEqualPercentSupport_Type.__name__=_D
_BattManEqualPercentSupport_Object=MibTableColumn
battManEqualPercentSupport=_BattManEqualPercentSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,13),_BattManEqualPercentSupport_Type())
battManEqualPercentSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEqualPercentSupport.setStatus(_A)
class _BattManBatteryStatusSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManBatteryStatusSupport_Type.__name__=_D
_BattManBatteryStatusSupport_Object=MibTableColumn
battManBatteryStatusSupport=_BattManBatteryStatusSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,14),_BattManBatteryStatusSupport_Type())
battManBatteryStatusSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryStatusSupport.setStatus(_A)
class _BattManDiagSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManDiagSupport_Type.__name__=_D
_BattManDiagSupport_Object=MibTableColumn
battManDiagSupport=_BattManDiagSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,15),_BattManDiagSupport_Type())
battManDiagSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManDiagSupport.setStatus(_A)
class _BattManEnvDataSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManEnvDataSupport_Type.__name__=_D
_BattManEnvDataSupport_Object=MibTableColumn
battManEnvDataSupport=_BattManEnvDataSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,16),_BattManEnvDataSupport_Type())
battManEnvDataSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEnvDataSupport.setStatus(_A)
class _BattManManualMeasurementSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_BattManManualMeasurementSupport_Type.__name__=_D
_BattManManualMeasurementSupport_Object=MibTableColumn
battManManualMeasurementSupport=_BattManManualMeasurementSupport_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,2,1,17),_BattManManualMeasurementSupport_Type())
battManManualMeasurementSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasurementSupport.setStatus(_A)
_BattManStringTable_Object=MibTable
battManStringTable=_BattManStringTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3))
if mibBuilder.loadTexts:battManStringTable.setStatus(_A)
_BattManStringEntry_Object=MibTableRow
battManStringEntry=_BattManStringEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3,1))
battManStringEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:battManStringEntry.setStatus(_A)
_BattManStringDeviceAddress_Type=Integer32
_BattManStringDeviceAddress_Object=MibTableColumn
battManStringDeviceAddress=_BattManStringDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3,1,1),_BattManStringDeviceAddress_Type())
battManStringDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStringDeviceAddress.setStatus(_A)
_BattManString_Type=Integer32
_BattManString_Object=MibTableColumn
battManString=_BattManString_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3,1,2),_BattManString_Type())
battManString.setMaxAccess(_B)
if mibBuilder.loadTexts:battManString.setStatus(_A)
_BattManStringBatteries_Type=Integer32
_BattManStringBatteries_Object=MibTableColumn
battManStringBatteries=_BattManStringBatteries_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3,1,3),_BattManStringBatteries_Type())
battManStringBatteries.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStringBatteries.setStatus(_A)
_BattManStringTotalVoltage_Type=Integer32
_BattManStringTotalVoltage_Object=MibTableColumn
battManStringTotalVoltage=_BattManStringTotalVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,3,1,4),_BattManStringTotalVoltage_Type())
battManStringTotalVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStringTotalVoltage.setStatus(_A)
_BattManBatteryTable_Object=MibTable
battManBatteryTable=_BattManBatteryTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4))
if mibBuilder.loadTexts:battManBatteryTable.setStatus(_A)
_BattManBatteryEntry_Object=MibTableRow
battManBatteryEntry=_BattManBatteryEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1))
battManBatteryEntry.setIndexNames((0,_C,_P),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:battManBatteryEntry.setStatus(_A)
_BattManBatteryDeviceAddress_Type=Integer32
_BattManBatteryDeviceAddress_Object=MibTableColumn
battManBatteryDeviceAddress=_BattManBatteryDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,1),_BattManBatteryDeviceAddress_Type())
battManBatteryDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryDeviceAddress.setStatus(_A)
_BattManBattery_Type=Integer32
_BattManBattery_Object=MibTableColumn
battManBattery=_BattManBattery_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,2),_BattManBattery_Type())
battManBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattery.setStatus(_A)
_BattManBatteryStringID_Type=Integer32
_BattManBatteryStringID_Object=MibTableColumn
battManBatteryStringID=_BattManBatteryStringID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,3),_BattManBatteryStringID_Type())
battManBatteryStringID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryStringID.setStatus(_A)
_BattManBatteryVersion_Type=Integer32
_BattManBatteryVersion_Object=MibTableColumn
battManBatteryVersion=_BattManBatteryVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,4),_BattManBatteryVersion_Type())
battManBatteryVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryVersion.setStatus(_A)
_BattManBatteryHwVersion_Type=OctetString
_BattManBatteryHwVersion_Object=MibTableColumn
battManBatteryHwVersion=_BattManBatteryHwVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,5),_BattManBatteryHwVersion_Type())
battManBatteryHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryHwVersion.setStatus(_A)
_BattManBatterySwVersion_Type=OctetString
_BattManBatterySwVersion_Object=MibTableColumn
battManBatterySwVersion=_BattManBatterySwVersion_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,6),_BattManBatterySwVersion_Type())
battManBatterySwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatterySwVersion.setStatus(_A)
_BattManBatteryVoltage_Type=Integer32
_BattManBatteryVoltage_Object=MibTableColumn
battManBatteryVoltage=_BattManBatteryVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,7),_BattManBatteryVoltage_Type())
battManBatteryVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryVoltage.setStatus(_A)
_BattManBatteryTemperature_Type=Integer32
_BattManBatteryTemperature_Object=MibTableColumn
battManBatteryTemperature=_BattManBatteryTemperature_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,8),_BattManBatteryTemperature_Type())
battManBatteryTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryTemperature.setStatus(_A)
_BattManBatteryImpedance_Type=Integer32
_BattManBatteryImpedance_Object=MibTableColumn
battManBatteryImpedance=_BattManBatteryImpedance_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,9),_BattManBatteryImpedance_Type())
battManBatteryImpedance.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryImpedance.setStatus(_A)
_BattManBatteryEqualizationPercent_Type=Integer32
_BattManBatteryEqualizationPercent_Object=MibTableColumn
battManBatteryEqualizationPercent=_BattManBatteryEqualizationPercent_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,10),_BattManBatteryEqualizationPercent_Type())
battManBatteryEqualizationPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryEqualizationPercent.setStatus(_A)
class _BattManBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('alarm',2)))
_BattManBatteryStatus_Type.__name__=_D
_BattManBatteryStatus_Object=MibTableColumn
battManBatteryStatus=_BattManBatteryStatus_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,11),_BattManBatteryStatus_Type())
battManBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryStatus.setStatus(_A)
_BattManBatteryDatasetID_Type=Unsigned32
_BattManBatteryDatasetID_Object=MibTableColumn
battManBatteryDatasetID=_BattManBatteryDatasetID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,4,1,12),_BattManBatteryDatasetID_Type())
battManBatteryDatasetID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryDatasetID.setStatus(_A)
_BattManBatteryDiagTable_Object=MibTable
battManBatteryDiagTable=_BattManBatteryDiagTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5))
if mibBuilder.loadTexts:battManBatteryDiagTable.setStatus(_A)
_BattManBatteryDiagEntry_Object=MibTableRow
battManBatteryDiagEntry=_BattManBatteryDiagEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5,1))
battManBatteryDiagEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:battManBatteryDiagEntry.setStatus(_A)
_BattManBatteryDiagDeviceAddress_Type=Integer32
_BattManBatteryDiagDeviceAddress_Object=MibTableColumn
battManBatteryDiagDeviceAddress=_BattManBatteryDiagDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5,1,1),_BattManBatteryDiagDeviceAddress_Type())
battManBatteryDiagDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryDiagDeviceAddress.setStatus(_A)
_BattManBatteryDiagModuleID_Type=Integer32
_BattManBatteryDiagModuleID_Object=MibTableColumn
battManBatteryDiagModuleID=_BattManBatteryDiagModuleID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5,1,2),_BattManBatteryDiagModuleID_Type())
battManBatteryDiagModuleID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryDiagModuleID.setStatus(_A)
_BattManBatteryDiagPageNumber_Type=Integer32
_BattManBatteryDiagPageNumber_Object=MibTableColumn
battManBatteryDiagPageNumber=_BattManBatteryDiagPageNumber_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5,1,3),_BattManBatteryDiagPageNumber_Type())
battManBatteryDiagPageNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:battManBatteryDiagPageNumber.setStatus(_A)
class _BattManBatteryDiagPageData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_BattManBatteryDiagPageData_Type.__name__=_H
_BattManBatteryDiagPageData_Object=MibTableColumn
battManBatteryDiagPageData=_BattManBatteryDiagPageData_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,5,1,4),_BattManBatteryDiagPageData_Type())
battManBatteryDiagPageData.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBatteryDiagPageData.setStatus(_A)
_BattManControlTable_Object=MibTable
battManControlTable=_BattManControlTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6))
if mibBuilder.loadTexts:battManControlTable.setStatus(_A)
_BattManControlEntry_Object=MibTableRow
battManControlEntry=_BattManControlEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6,1))
battManControlEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:battManControlEntry.setStatus(_A)
_BattManControlDeviceAddress_Type=Integer32
_BattManControlDeviceAddress_Object=MibTableColumn
battManControlDeviceAddress=_BattManControlDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6,1,1),_BattManControlDeviceAddress_Type())
battManControlDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManControlDeviceAddress.setStatus(_A)
class _BattManControlEqualizationSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activated',1),('deactivated',2)))
_BattManControlEqualizationSetting_Type.__name__=_D
_BattManControlEqualizationSetting_Object=MibTableColumn
battManControlEqualizationSetting=_BattManControlEqualizationSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6,1,2),_BattManControlEqualizationSetting_Type())
battManControlEqualizationSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:battManControlEqualizationSetting.setStatus(_A)
_BattManControlAutoInterval_Type=Integer32
_BattManControlAutoInterval_Object=MibTableColumn
battManControlAutoInterval=_BattManControlAutoInterval_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6,1,3),_BattManControlAutoInterval_Type())
battManControlAutoInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:battManControlAutoInterval.setStatus(_A)
class _BattManControlSensorsRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BattManControlSensorsRestart_Type.__name__=_D
_BattManControlSensorsRestart_Object=MibTableColumn
battManControlSensorsRestart=_BattManControlSensorsRestart_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,6,1,4),_BattManControlSensorsRestart_Type())
battManControlSensorsRestart.setMaxAccess(_G)
if mibBuilder.loadTexts:battManControlSensorsRestart.setStatus(_I)
_BattManStatusTable_Object=MibTable
battManStatusTable=_BattManStatusTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,7))
if mibBuilder.loadTexts:battManStatusTable.setStatus(_A)
_BattManStatusEntry_Object=MibTableRow
battManStatusEntry=_BattManStatusEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,7,1))
battManStatusEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:battManStatusEntry.setStatus(_A)
_BattManStatusDeviceAddress_Type=Integer32
_BattManStatusDeviceAddress_Object=MibTableColumn
battManStatusDeviceAddress=_BattManStatusDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,7,1,1),_BattManStatusDeviceAddress_Type())
battManStatusDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStatusDeviceAddress.setStatus(_A)
_BattManStatusTimeToMeasurement_Type=Unsigned32
_BattManStatusTimeToMeasurement_Object=MibTableColumn
battManStatusTimeToMeasurement=_BattManStatusTimeToMeasurement_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,7,1,2),_BattManStatusTimeToMeasurement_Type())
battManStatusTimeToMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:battManStatusTimeToMeasurement.setStatus(_A)
_BattManEnvStatusTable_Object=MibTable
battManEnvStatusTable=_BattManEnvStatusTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8))
if mibBuilder.loadTexts:battManEnvStatusTable.setStatus(_A)
_BattManEnvStatusEntry_Object=MibTableRow
battManEnvStatusEntry=_BattManEnvStatusEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8,1))
battManEnvStatusEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:battManEnvStatusEntry.setStatus(_A)
_BattManEnvStatusDeviceAddress_Type=Integer32
_BattManEnvStatusDeviceAddress_Object=MibTableColumn
battManEnvStatusDeviceAddress=_BattManEnvStatusDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8,1,1),_BattManEnvStatusDeviceAddress_Type())
battManEnvStatusDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEnvStatusDeviceAddress.setStatus(_A)
_BattManEnvStatusTemperature_Type=Integer32
_BattManEnvStatusTemperature_Object=MibTableColumn
battManEnvStatusTemperature=_BattManEnvStatusTemperature_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8,1,2),_BattManEnvStatusTemperature_Type())
battManEnvStatusTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEnvStatusTemperature.setStatus(_A)
_BattManEnvStatusHumidity_Type=Integer32
_BattManEnvStatusHumidity_Object=MibTableColumn
battManEnvStatusHumidity=_BattManEnvStatusHumidity_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8,1,3),_BattManEnvStatusHumidity_Type())
battManEnvStatusHumidity.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEnvStatusHumidity.setStatus(_A)
_BattManEnvStatusDryContact_Type=Integer32
_BattManEnvStatusDryContact_Object=MibTableColumn
battManEnvStatusDryContact=_BattManEnvStatusDryContact_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,8,1,4),_BattManEnvStatusDryContact_Type())
battManEnvStatusDryContact.setMaxAccess(_B)
if mibBuilder.loadTexts:battManEnvStatusDryContact.setStatus(_A)
_BattManManualMeasTable_Object=MibTable
battManManualMeasTable=_BattManManualMeasTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9))
if mibBuilder.loadTexts:battManManualMeasTable.setStatus(_A)
_BattManManualMeasEntry_Object=MibTableRow
battManManualMeasEntry=_BattManManualMeasEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1))
battManManualMeasEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:battManManualMeasEntry.setStatus(_A)
_BattManManualMeasDeviceAddress_Type=Integer32
_BattManManualMeasDeviceAddress_Object=MibTableColumn
battManManualMeasDeviceAddress=_BattManManualMeasDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,1),_BattManManualMeasDeviceAddress_Type())
battManManualMeasDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasDeviceAddress.setStatus(_A)
class _BattManManualMeasStatusText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_BattManManualMeasStatusText_Type.__name__=_H
_BattManManualMeasStatusText_Object=MibTableColumn
battManManualMeasStatusText=_BattManManualMeasStatusText_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,2),_BattManManualMeasStatusText_Type())
battManManualMeasStatusText.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasStatusText.setStatus(_A)
_BattManManualMeasStatusCode_Type=Unsigned32
_BattManManualMeasStatusCode_Object=MibTableColumn
battManManualMeasStatusCode=_BattManManualMeasStatusCode_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,3),_BattManManualMeasStatusCode_Type())
battManManualMeasStatusCode.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasStatusCode.setStatus(_A)
_BattManManualMeasDatasetID_Type=Unsigned32
_BattManManualMeasDatasetID_Object=MibTableColumn
battManManualMeasDatasetID=_BattManManualMeasDatasetID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,4),_BattManManualMeasDatasetID_Type())
battManManualMeasDatasetID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasDatasetID.setStatus(_A)
_BattManManualMeasTimeToMeasurement_Type=Unsigned32
_BattManManualMeasTimeToMeasurement_Object=MibTableColumn
battManManualMeasTimeToMeasurement=_BattManManualMeasTimeToMeasurement_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,5),_BattManManualMeasTimeToMeasurement_Type())
battManManualMeasTimeToMeasurement.setMaxAccess(_B)
if mibBuilder.loadTexts:battManManualMeasTimeToMeasurement.setStatus(_A)
class _BattManManualMeasurementTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BattManManualMeasurementTrigger_Type.__name__=_D
_BattManManualMeasurementTrigger_Object=MibTableColumn
battManManualMeasurementTrigger=_BattManManualMeasurementTrigger_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,9,1,6),_BattManManualMeasurementTrigger_Type())
battManManualMeasurementTrigger.setMaxAccess(_G)
if mibBuilder.loadTexts:battManManualMeasurementTrigger.setStatus(_I)
_BattManDeviceSettings_ObjectIdentity=ObjectIdentity
battManDeviceSettings=_BattManDeviceSettings_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,10))
_BattManDevStringVoltsSetting_Type=Integer32
_BattManDevStringVoltsSetting_Object=MibScalar
battManDevStringVoltsSetting=_BattManDevStringVoltsSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,10,1),_BattManDevStringVoltsSetting_Type())
battManDevStringVoltsSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:battManDevStringVoltsSetting.setStatus(_A)
_BattManDevStringCountSetting_Type=Integer32
_BattManDevStringCountSetting_Object=MibScalar
battManDevStringCountSetting=_BattManDevStringCountSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,10,2),_BattManDevStringCountSetting_Type())
battManDevStringCountSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:battManDevStringCountSetting.setStatus(_A)
class _BattManDevDiagnoscticsSetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BattManDevDiagnoscticsSetting_Type.__name__=_D
_BattManDevDiagnoscticsSetting_Object=MibScalar
battManDevDiagnoscticsSetting=_BattManDevDiagnoscticsSetting_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,10,3),_BattManDevDiagnoscticsSetting_Type())
battManDevDiagnoscticsSetting.setMaxAccess(_G)
if mibBuilder.loadTexts:battManDevDiagnoscticsSetting.setStatus(_I)
_BattManBatteryLogTable_Object=MibTable
battManBatteryLogTable=_BattManBatteryLogTable_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11))
if mibBuilder.loadTexts:battManBatteryLogTable.setStatus(_A)
_BattManBatteryLogEntry_Object=MibTableRow
battManBatteryLogEntry=_BattManBatteryLogEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1))
battManBatteryLogEntry.setIndexNames((0,_C,_Y),(0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:battManBatteryLogEntry.setStatus(_A)
_BattManBattLogDeviceAddress_Type=Integer32
_BattManBattLogDeviceAddress_Object=MibTableColumn
battManBattLogDeviceAddress=_BattManBattLogDeviceAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,1),_BattManBattLogDeviceAddress_Type())
battManBattLogDeviceAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogDeviceAddress.setStatus(_A)
_BattManBattLogDatasetID_Type=Unsigned32
_BattManBattLogDatasetID_Object=MibTableColumn
battManBattLogDatasetID=_BattManBattLogDatasetID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,2),_BattManBattLogDatasetID_Type())
battManBattLogDatasetID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogDatasetID.setStatus(_A)
_BattManBattLogBatteryID_Type=Integer32
_BattManBattLogBatteryID_Object=MibTableColumn
battManBattLogBatteryID=_BattManBattLogBatteryID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,3),_BattManBattLogBatteryID_Type())
battManBattLogBatteryID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogBatteryID.setStatus(_A)
_BattManBattLogStringID_Type=Integer32
_BattManBattLogStringID_Object=MibTableColumn
battManBattLogStringID=_BattManBattLogStringID_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,4),_BattManBattLogStringID_Type())
battManBattLogStringID.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogStringID.setStatus(_A)
_BattManBattLogVoltage_Type=Integer32
_BattManBattLogVoltage_Object=MibTableColumn
battManBattLogVoltage=_BattManBattLogVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,5),_BattManBattLogVoltage_Type())
battManBattLogVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogVoltage.setStatus(_A)
_BattManBattLogTemperature_Type=Integer32
_BattManBattLogTemperature_Object=MibTableColumn
battManBattLogTemperature=_BattManBattLogTemperature_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,6),_BattManBattLogTemperature_Type())
battManBattLogTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogTemperature.setStatus(_A)
_BattManBattLogImpedance_Type=HundredthmOhm
_BattManBattLogImpedance_Object=MibTableColumn
battManBattLogImpedance=_BattManBattLogImpedance_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,7),_BattManBattLogImpedance_Type())
battManBattLogImpedance.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogImpedance.setStatus(_A)
_BattManBattLogConductance_Type=HundredthkS
_BattManBattLogConductance_Object=MibTableColumn
battManBattLogConductance=_BattManBattLogConductance_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,8),_BattManBattLogConductance_Type())
battManBattLogConductance.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogConductance.setStatus(_A)
_BattManBattLogTimestamp_Type=DateAndTime
_BattManBattLogTimestamp_Object=MibTableColumn
battManBattLogTimestamp=_BattManBattLogTimestamp_Object((1,3,6,1,4,1,5802,1,3,1,2,5,1,16,1,11,1,9),_BattManBattLogTimestamp_Type())
battManBattLogTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:battManBattLogTimestamp.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HundredthmOhm':HundredthmOhm,'HundredthkS':HundredthkS,'battManIdentMIB':battManIdentMIB,'battManIdentObjects':battManIdentObjects,'battManMonitored':battManMonitored,'battManDeviceTable':battManDeviceTable,'battManDeviceEntry':battManDeviceEntry,_M:battManDeviceAddress,'battManProtocolVersion':battManProtocolVersion,'battManSoftwareVersion':battManSoftwareVersion,'battManDeviceId':battManDeviceId,'battManVendorIdentity':battManVendorIdentity,'battManStringVoltage':battManStringVoltage,'battManBatteries':battManBatteries,'battManBatteryStrings':battManBatteryStrings,'battManBatteriesPerStrings':battManBatteriesPerStrings,'battManVoltageSupport':battManVoltageSupport,'battManTemperatureSupport':battManTemperatureSupport,'battManImpedanceSupport':battManImpedanceSupport,'battManEqualPercentSupport':battManEqualPercentSupport,'battManBatteryStatusSupport':battManBatteryStatusSupport,'battManDiagSupport':battManDiagSupport,'battManEnvDataSupport':battManEnvDataSupport,'battManManualMeasurementSupport':battManManualMeasurementSupport,'battManStringTable':battManStringTable,'battManStringEntry':battManStringEntry,_N:battManStringDeviceAddress,_O:battManString,'battManStringBatteries':battManStringBatteries,'battManStringTotalVoltage':battManStringTotalVoltage,'battManBatteryTable':battManBatteryTable,'battManBatteryEntry':battManBatteryEntry,_P:battManBatteryDeviceAddress,_R:battManBattery,_Q:battManBatteryStringID,'battManBatteryVersion':battManBatteryVersion,'battManBatteryHwVersion':battManBatteryHwVersion,'battManBatterySwVersion':battManBatterySwVersion,'battManBatteryVoltage':battManBatteryVoltage,'battManBatteryTemperature':battManBatteryTemperature,'battManBatteryImpedance':battManBatteryImpedance,'battManBatteryEqualizationPercent':battManBatteryEqualizationPercent,'battManBatteryStatus':battManBatteryStatus,'battManBatteryDatasetID':battManBatteryDatasetID,'battManBatteryDiagTable':battManBatteryDiagTable,'battManBatteryDiagEntry':battManBatteryDiagEntry,_S:battManBatteryDiagDeviceAddress,_T:battManBatteryDiagModuleID,'battManBatteryDiagPageNumber':battManBatteryDiagPageNumber,'battManBatteryDiagPageData':battManBatteryDiagPageData,'battManControlTable':battManControlTable,'battManControlEntry':battManControlEntry,_U:battManControlDeviceAddress,'battManControlEqualizationSetting':battManControlEqualizationSetting,'battManControlAutoInterval':battManControlAutoInterval,'battManControlSensorsRestart':battManControlSensorsRestart,'battManStatusTable':battManStatusTable,'battManStatusEntry':battManStatusEntry,_V:battManStatusDeviceAddress,'battManStatusTimeToMeasurement':battManStatusTimeToMeasurement,'battManEnvStatusTable':battManEnvStatusTable,'battManEnvStatusEntry':battManEnvStatusEntry,_W:battManEnvStatusDeviceAddress,'battManEnvStatusTemperature':battManEnvStatusTemperature,'battManEnvStatusHumidity':battManEnvStatusHumidity,'battManEnvStatusDryContact':battManEnvStatusDryContact,'battManManualMeasTable':battManManualMeasTable,'battManManualMeasEntry':battManManualMeasEntry,_X:battManManualMeasDeviceAddress,'battManManualMeasStatusText':battManManualMeasStatusText,'battManManualMeasStatusCode':battManManualMeasStatusCode,'battManManualMeasDatasetID':battManManualMeasDatasetID,'battManManualMeasTimeToMeasurement':battManManualMeasTimeToMeasurement,'battManManualMeasurementTrigger':battManManualMeasurementTrigger,'battManDeviceSettings':battManDeviceSettings,'battManDevStringVoltsSetting':battManDevStringVoltsSetting,'battManDevStringCountSetting':battManDevStringCountSetting,'battManDevDiagnoscticsSetting':battManDevDiagnoscticsSetting,'battManBatteryLogTable':battManBatteryLogTable,'battManBatteryLogEntry':battManBatteryLogEntry,_Y:battManBattLogDeviceAddress,_Z:battManBattLogDatasetID,_b:battManBattLogBatteryID,_a:battManBattLogStringID,'battManBattLogVoltage':battManBattLogVoltage,'battManBattLogTemperature':battManBattLogTemperature,'battManBattLogImpedance':battManBattLogImpedance,'battManBattLogConductance':battManBattLogConductance,'battManBattLogTimestamp':battManBattLogTimestamp})