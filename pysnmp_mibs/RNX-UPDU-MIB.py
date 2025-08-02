_u='upduMibGroupRev1'
_t='upduRcmSensorQuality'
_s='upduRcmCurrentDc'
_r='upduRcmCurrentRms'
_q='upduRcmName'
_p='upduSensorHumidity'
_o='upduSensorTemperatureCelsius'
_n='upduSensorType'
_m='upduSensorPortName'
_l='upduRelayCondition'
_k='upduRelayOperStatus'
_j='upduRelayAdminStatus'
_i='upduRelayMeterNames'
_h='upduMeterDescription'
_g='upduMeterCustomName'
_f='upduMeterSystemName'
_e='upduMeterIrms'
_d='upduMeterUrms'
_c='upduMeterPowerS'
_b='upduMeterPowerQ'
_a='upduMeterPowerP'
_Z='upduMeterEnergyR4'
_Y='upduMeterEnergyR1'
_X='upduMeterEnergyP'
_W='upduMeterType'
_V='upduMeterName'
_U='upduModuleLotNumber'
_T='upduModuleSerialNumber'
_S='upduModulePartNumber'
_R='upduModuleType'
_Q='upduInfoLotNumber'
_P='upduInfoSerialNumber'
_O='upduInfoPartNumber'
_N='upduRelayIndex'
_M='upduRcmIndex'
_L='upduSensorPort'
_K='upduMeterIndex'
_J='read-write'
_I='unknown'
_H='not-accessible'
_G='upduModuleIndex'
_F='OctetString'
_E='d'
_D='Integer32'
_C='read-only'
_B='RNX-UPDU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rnx=ModuleIdentity((1,3,6,1,4,1,55108))
if mibBuilder.loadTexts:rnx.setRevisions(('2022-07-06 00:00','2022-06-22 00:00','2020-12-16 00:00','2020-06-18 00:00'))
class Watts(TextualConvention,Integer32):status=_A;displayHint=_E
class VoltAmpereReactives(TextualConvention,Integer32):status=_A;displayHint=_E
class VoltAmperes(TextualConvention,Integer32):status=_A;displayHint=_E
class WattHours(TextualConvention,Counter64):status=_A;displayHint=_E
class VoltAmpereReactiveHours(TextualConvention,Counter64):status=_A;displayHint=_E
class MilliAmperes(TextualConvention,Integer32):status=_A;displayHint=_E
class TenthMilliAmperes(TextualConvention,Integer32):status=_A;displayHint=_E
class MilliVolts(TextualConvention,Integer32):status=_A;displayHint=_E
class TenthDegreesCelsius(TextualConvention,Integer32):status=_A;displayHint=_E
class Permil(TextualConvention,Integer32):status=_A;displayHint=_E
_UpduMib_ObjectIdentity=ObjectIdentity
upduMib=_UpduMib_ObjectIdentity((1,3,6,1,4,1,55108,1))
_UpduInfo_ObjectIdentity=ObjectIdentity
upduInfo=_UpduInfo_ObjectIdentity((1,3,6,1,4,1,55108,1,1))
_UpduInfoPartNumber_Type=OctetString
_UpduInfoPartNumber_Object=MibScalar
upduInfoPartNumber=_UpduInfoPartNumber_Object((1,3,6,1,4,1,55108,1,1,1),_UpduInfoPartNumber_Type())
upduInfoPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduInfoPartNumber.setStatus(_A)
_UpduInfoSerialNumber_Type=Integer32
_UpduInfoSerialNumber_Object=MibScalar
upduInfoSerialNumber=_UpduInfoSerialNumber_Object((1,3,6,1,4,1,55108,1,1,2),_UpduInfoSerialNumber_Type())
upduInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduInfoSerialNumber.setStatus(_A)
_UpduInfoLotNumber_Type=OctetString
_UpduInfoLotNumber_Object=MibScalar
upduInfoLotNumber=_UpduInfoLotNumber_Object((1,3,6,1,4,1,55108,1,1,3),_UpduInfoLotNumber_Type())
upduInfoLotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduInfoLotNumber.setStatus(_A)
_UpduInventory_ObjectIdentity=ObjectIdentity
upduInventory=_UpduInventory_ObjectIdentity((1,3,6,1,4,1,55108,1,2))
_UpduModuleTable_Object=MibTable
upduModuleTable=_UpduModuleTable_Object((1,3,6,1,4,1,55108,1,2,1))
if mibBuilder.loadTexts:upduModuleTable.setStatus(_A)
_UpduModuleEntry_Object=MibTableRow
upduModuleEntry=_UpduModuleEntry_Object((1,3,6,1,4,1,55108,1,2,1,1))
upduModuleEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:upduModuleEntry.setStatus(_A)
class _UpduModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_UpduModuleIndex_Type.__name__=_D
_UpduModuleIndex_Object=MibTableColumn
upduModuleIndex=_UpduModuleIndex_Object((1,3,6,1,4,1,55108,1,2,1,1,1),_UpduModuleIndex_Type())
upduModuleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:upduModuleIndex.setStatus(_A)
class _UpduModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('icm',1),('meterModule',2)))
_UpduModuleType_Type.__name__=_D
_UpduModuleType_Object=MibTableColumn
upduModuleType=_UpduModuleType_Object((1,3,6,1,4,1,55108,1,2,1,1,2),_UpduModuleType_Type())
upduModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:upduModuleType.setStatus(_A)
_UpduModulePartNumber_Type=OctetString
_UpduModulePartNumber_Object=MibTableColumn
upduModulePartNumber=_UpduModulePartNumber_Object((1,3,6,1,4,1,55108,1,2,1,1,3),_UpduModulePartNumber_Type())
upduModulePartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduModulePartNumber.setStatus(_A)
_UpduModuleSerialNumber_Type=Integer32
_UpduModuleSerialNumber_Object=MibTableColumn
upduModuleSerialNumber=_UpduModuleSerialNumber_Object((1,3,6,1,4,1,55108,1,2,1,1,4),_UpduModuleSerialNumber_Type())
upduModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduModuleSerialNumber.setStatus(_A)
_UpduModuleLotNumber_Type=OctetString
_UpduModuleLotNumber_Object=MibTableColumn
upduModuleLotNumber=_UpduModuleLotNumber_Object((1,3,6,1,4,1,55108,1,2,1,1,5),_UpduModuleLotNumber_Type())
upduModuleLotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:upduModuleLotNumber.setStatus(_A)
_UpduMeasurements_ObjectIdentity=ObjectIdentity
upduMeasurements=_UpduMeasurements_ObjectIdentity((1,3,6,1,4,1,55108,1,3))
_UpduMeterTable_Object=MibTable
upduMeterTable=_UpduMeterTable_Object((1,3,6,1,4,1,55108,1,3,1))
if mibBuilder.loadTexts:upduMeterTable.setStatus(_A)
_UpduMeterEntry_Object=MibTableRow
upduMeterEntry=_UpduMeterEntry_Object((1,3,6,1,4,1,55108,1,3,1,1))
upduMeterEntry.setIndexNames((0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:upduMeterEntry.setStatus(_A)
class _UpduMeterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_UpduMeterIndex_Type.__name__=_D
_UpduMeterIndex_Object=MibTableColumn
upduMeterIndex=_UpduMeterIndex_Object((1,3,6,1,4,1,55108,1,3,1,1,1),_UpduMeterIndex_Type())
upduMeterIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:upduMeterIndex.setStatus(_A)
class _UpduMeterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpduMeterName_Type.__name__=_F
_UpduMeterName_Object=MibTableColumn
upduMeterName=_UpduMeterName_Object((1,3,6,1,4,1,55108,1,3,1,1,2),_UpduMeterName_Type())
upduMeterName.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterName.setStatus(_A)
class _UpduMeterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('pduTotal',0),('pduTotalCalc',1),('phaseTotal',2),('phaseTotalCalc',3),('moduleTotal',4),('moduleTotalCalc',5),('outlet',6),('outletGroup',7)))
_UpduMeterType_Type.__name__=_D
_UpduMeterType_Object=MibTableColumn
upduMeterType=_UpduMeterType_Object((1,3,6,1,4,1,55108,1,3,1,1,3),_UpduMeterType_Type())
upduMeterType.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterType.setStatus(_A)
_UpduMeterEnergyP_Type=WattHours
_UpduMeterEnergyP_Object=MibTableColumn
upduMeterEnergyP=_UpduMeterEnergyP_Object((1,3,6,1,4,1,55108,1,3,1,1,4),_UpduMeterEnergyP_Type())
upduMeterEnergyP.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterEnergyP.setStatus(_A)
if mibBuilder.loadTexts:upduMeterEnergyP.setUnits('Wh')
_UpduMeterEnergyR1_Type=VoltAmpereReactiveHours
_UpduMeterEnergyR1_Object=MibTableColumn
upduMeterEnergyR1=_UpduMeterEnergyR1_Object((1,3,6,1,4,1,55108,1,3,1,1,5),_UpduMeterEnergyR1_Type())
upduMeterEnergyR1.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterEnergyR1.setStatus(_A)
if mibBuilder.loadTexts:upduMeterEnergyR1.setUnits('varh')
_UpduMeterEnergyR4_Type=VoltAmpereReactiveHours
_UpduMeterEnergyR4_Object=MibTableColumn
upduMeterEnergyR4=_UpduMeterEnergyR4_Object((1,3,6,1,4,1,55108,1,3,1,1,6),_UpduMeterEnergyR4_Type())
upduMeterEnergyR4.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterEnergyR4.setStatus(_A)
if mibBuilder.loadTexts:upduMeterEnergyR4.setUnits('varh')
_UpduMeterPowerP_Type=Watts
_UpduMeterPowerP_Object=MibTableColumn
upduMeterPowerP=_UpduMeterPowerP_Object((1,3,6,1,4,1,55108,1,3,1,1,7),_UpduMeterPowerP_Type())
upduMeterPowerP.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterPowerP.setStatus(_A)
if mibBuilder.loadTexts:upduMeterPowerP.setUnits('W')
_UpduMeterPowerQ_Type=VoltAmpereReactives
_UpduMeterPowerQ_Object=MibTableColumn
upduMeterPowerQ=_UpduMeterPowerQ_Object((1,3,6,1,4,1,55108,1,3,1,1,8),_UpduMeterPowerQ_Type())
upduMeterPowerQ.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterPowerQ.setStatus(_A)
if mibBuilder.loadTexts:upduMeterPowerQ.setUnits('var')
_UpduMeterPowerS_Type=VoltAmperes
_UpduMeterPowerS_Object=MibTableColumn
upduMeterPowerS=_UpduMeterPowerS_Object((1,3,6,1,4,1,55108,1,3,1,1,9),_UpduMeterPowerS_Type())
upduMeterPowerS.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterPowerS.setStatus(_A)
if mibBuilder.loadTexts:upduMeterPowerS.setUnits('VA')
_UpduMeterUrms_Type=MilliVolts
_UpduMeterUrms_Object=MibTableColumn
upduMeterUrms=_UpduMeterUrms_Object((1,3,6,1,4,1,55108,1,3,1,1,10),_UpduMeterUrms_Type())
upduMeterUrms.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterUrms.setStatus(_A)
if mibBuilder.loadTexts:upduMeterUrms.setUnits('mV')
_UpduMeterIrms_Type=MilliAmperes
_UpduMeterIrms_Object=MibTableColumn
upduMeterIrms=_UpduMeterIrms_Object((1,3,6,1,4,1,55108,1,3,1,1,11),_UpduMeterIrms_Type())
upduMeterIrms.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterIrms.setStatus(_A)
if mibBuilder.loadTexts:upduMeterIrms.setUnits('mA')
_UpduMeterSystemName_Type=OctetString
_UpduMeterSystemName_Object=MibTableColumn
upduMeterSystemName=_UpduMeterSystemName_Object((1,3,6,1,4,1,55108,1,3,1,1,12),_UpduMeterSystemName_Type())
upduMeterSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:upduMeterSystemName.setStatus(_A)
class _UpduMeterCustomName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,23))
_UpduMeterCustomName_Type.__name__=_F
_UpduMeterCustomName_Object=MibTableColumn
upduMeterCustomName=_UpduMeterCustomName_Object((1,3,6,1,4,1,55108,1,3,1,1,13),_UpduMeterCustomName_Type())
upduMeterCustomName.setMaxAccess(_J)
if mibBuilder.loadTexts:upduMeterCustomName.setStatus(_A)
class _UpduMeterDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_UpduMeterDescription_Type.__name__=_F
_UpduMeterDescription_Object=MibTableColumn
upduMeterDescription=_UpduMeterDescription_Object((1,3,6,1,4,1,55108,1,3,1,1,14),_UpduMeterDescription_Type())
upduMeterDescription.setMaxAccess(_J)
if mibBuilder.loadTexts:upduMeterDescription.setStatus(_A)
_UpduSensorTable_Object=MibTable
upduSensorTable=_UpduSensorTable_Object((1,3,6,1,4,1,55108,1,3,2))
if mibBuilder.loadTexts:upduSensorTable.setStatus(_A)
_UpduSensorEntry_Object=MibTableRow
upduSensorEntry=_UpduSensorEntry_Object((1,3,6,1,4,1,55108,1,3,2,1))
upduSensorEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:upduSensorEntry.setStatus(_A)
class _UpduSensorPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_UpduSensorPort_Type.__name__=_D
_UpduSensorPort_Object=MibTableColumn
upduSensorPort=_UpduSensorPort_Object((1,3,6,1,4,1,55108,1,3,2,1,1),_UpduSensorPort_Type())
upduSensorPort.setMaxAccess(_H)
if mibBuilder.loadTexts:upduSensorPort.setStatus(_A)
_UpduSensorPortName_Type=OctetString
_UpduSensorPortName_Object=MibTableColumn
upduSensorPortName=_UpduSensorPortName_Object((1,3,6,1,4,1,55108,1,3,2,1,2),_UpduSensorPortName_Type())
upduSensorPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:upduSensorPortName.setStatus(_A)
class _UpduSensorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('temp',1),('tempHumidity',2)))
_UpduSensorType_Type.__name__=_D
_UpduSensorType_Object=MibTableColumn
upduSensorType=_UpduSensorType_Object((1,3,6,1,4,1,55108,1,3,2,1,3),_UpduSensorType_Type())
upduSensorType.setMaxAccess(_C)
if mibBuilder.loadTexts:upduSensorType.setStatus(_A)
_UpduSensorTemperatureCelsius_Type=TenthDegreesCelsius
_UpduSensorTemperatureCelsius_Object=MibTableColumn
upduSensorTemperatureCelsius=_UpduSensorTemperatureCelsius_Object((1,3,6,1,4,1,55108,1,3,2,1,4),_UpduSensorTemperatureCelsius_Type())
upduSensorTemperatureCelsius.setMaxAccess(_C)
if mibBuilder.loadTexts:upduSensorTemperatureCelsius.setStatus(_A)
if mibBuilder.loadTexts:upduSensorTemperatureCelsius.setUnits('deg-C/10')
_UpduSensorHumidity_Type=Permil
_UpduSensorHumidity_Object=MibTableColumn
upduSensorHumidity=_UpduSensorHumidity_Object((1,3,6,1,4,1,55108,1,3,2,1,5),_UpduSensorHumidity_Type())
upduSensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:upduSensorHumidity.setStatus(_A)
if mibBuilder.loadTexts:upduSensorHumidity.setUnits('/1000')
_UpduRcmTable_Object=MibTable
upduRcmTable=_UpduRcmTable_Object((1,3,6,1,4,1,55108,1,3,3))
if mibBuilder.loadTexts:upduRcmTable.setStatus(_A)
_UpduRcmEntry_Object=MibTableRow
upduRcmEntry=_UpduRcmEntry_Object((1,3,6,1,4,1,55108,1,3,3,1))
upduRcmEntry.setIndexNames((0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:upduRcmEntry.setStatus(_A)
class _UpduRcmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_UpduRcmIndex_Type.__name__=_D
_UpduRcmIndex_Object=MibTableColumn
upduRcmIndex=_UpduRcmIndex_Object((1,3,6,1,4,1,55108,1,3,3,1,1),_UpduRcmIndex_Type())
upduRcmIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:upduRcmIndex.setStatus(_A)
class _UpduRcmName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_UpduRcmName_Type.__name__=_F
_UpduRcmName_Object=MibTableColumn
upduRcmName=_UpduRcmName_Object((1,3,6,1,4,1,55108,1,3,3,1,2),_UpduRcmName_Type())
upduRcmName.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRcmName.setStatus(_A)
_UpduRcmCurrentRms_Type=TenthMilliAmperes
_UpduRcmCurrentRms_Object=MibTableColumn
upduRcmCurrentRms=_UpduRcmCurrentRms_Object((1,3,6,1,4,1,55108,1,3,3,1,3),_UpduRcmCurrentRms_Type())
upduRcmCurrentRms.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRcmCurrentRms.setStatus(_A)
if mibBuilder.loadTexts:upduRcmCurrentRms.setUnits('mA/10')
_UpduRcmCurrentDc_Type=TenthMilliAmperes
_UpduRcmCurrentDc_Object=MibTableColumn
upduRcmCurrentDc=_UpduRcmCurrentDc_Object((1,3,6,1,4,1,55108,1,3,3,1,4),_UpduRcmCurrentDc_Type())
upduRcmCurrentDc.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRcmCurrentDc.setStatus(_A)
if mibBuilder.loadTexts:upduRcmCurrentDc.setUnits('mA/10')
class _UpduRcmSensorQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ok',0),('nodata',1),('timeout',2),('internalerror',3),('selftestfailed',4)))
_UpduRcmSensorQuality_Type.__name__=_D
_UpduRcmSensorQuality_Object=MibTableColumn
upduRcmSensorQuality=_UpduRcmSensorQuality_Object((1,3,6,1,4,1,55108,1,3,3,1,5),_UpduRcmSensorQuality_Type())
upduRcmSensorQuality.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRcmSensorQuality.setStatus(_A)
_UpduControl_ObjectIdentity=ObjectIdentity
upduControl=_UpduControl_ObjectIdentity((1,3,6,1,4,1,55108,1,4))
_UpduRelayTable_Object=MibTable
upduRelayTable=_UpduRelayTable_Object((1,3,6,1,4,1,55108,1,4,1))
if mibBuilder.loadTexts:upduRelayTable.setStatus(_A)
_UpduRelayEntry_Object=MibTableRow
upduRelayEntry=_UpduRelayEntry_Object((1,3,6,1,4,1,55108,1,4,1,1))
upduRelayEntry.setIndexNames((0,_B,_G),(0,_B,_N))
if mibBuilder.loadTexts:upduRelayEntry.setStatus(_A)
class _UpduRelayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_UpduRelayIndex_Type.__name__=_D
_UpduRelayIndex_Object=MibTableColumn
upduRelayIndex=_UpduRelayIndex_Object((1,3,6,1,4,1,55108,1,4,1,1,1),_UpduRelayIndex_Type())
upduRelayIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:upduRelayIndex.setStatus(_A)
class _UpduRelayMeterNames_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UpduRelayMeterNames_Type.__name__=_F
_UpduRelayMeterNames_Object=MibTableColumn
upduRelayMeterNames=_UpduRelayMeterNames_Object((1,3,6,1,4,1,55108,1,4,1,1,2),_UpduRelayMeterNames_Type())
upduRelayMeterNames.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRelayMeterNames.setStatus(_A)
class _UpduRelayAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),(_I,2)))
_UpduRelayAdminStatus_Type.__name__=_D
_UpduRelayAdminStatus_Object=MibTableColumn
upduRelayAdminStatus=_UpduRelayAdminStatus_Object((1,3,6,1,4,1,55108,1,4,1,1,3),_UpduRelayAdminStatus_Type())
upduRelayAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:upduRelayAdminStatus.setStatus(_A)
class _UpduRelayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('off',0),('on',1),(_I,2)))
_UpduRelayOperStatus_Type.__name__=_D
_UpduRelayOperStatus_Object=MibTableColumn
upduRelayOperStatus=_UpduRelayOperStatus_Object((1,3,6,1,4,1,55108,1,4,1,1,4),_UpduRelayOperStatus_Type())
upduRelayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRelayOperStatus.setStatus(_A)
class _UpduRelayCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ok',0),('failed',1),(_I,2)))
_UpduRelayCondition_Type.__name__=_D
_UpduRelayCondition_Object=MibTableColumn
upduRelayCondition=_UpduRelayCondition_Object((1,3,6,1,4,1,55108,1,4,1,1,5),_UpduRelayCondition_Type())
upduRelayCondition.setMaxAccess(_C)
if mibBuilder.loadTexts:upduRelayCondition.setStatus(_A)
_UpduConformance_ObjectIdentity=ObjectIdentity
upduConformance=_UpduConformance_ObjectIdentity((1,3,6,1,4,1,55108,1,5))
_UpduMibCompliances_ObjectIdentity=ObjectIdentity
upduMibCompliances=_UpduMibCompliances_ObjectIdentity((1,3,6,1,4,1,55108,1,5,1))
_UpduMibGroups_ObjectIdentity=ObjectIdentity
upduMibGroups=_UpduMibGroups_ObjectIdentity((1,3,6,1,4,1,55108,1,5,2))
upduMibGroupRev1=ObjectGroup((1,3,6,1,4,1,55108,1,5,2,1))
upduMibGroupRev1.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:upduMibGroupRev1.setStatus(_A)
upduMibCompliance=ModuleCompliance((1,3,6,1,4,1,55108,1,5,1,1))
upduMibCompliance.setObjects((_B,_u))
if mibBuilder.loadTexts:upduMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Watts':Watts,'VoltAmpereReactives':VoltAmpereReactives,'VoltAmperes':VoltAmperes,'WattHours':WattHours,'VoltAmpereReactiveHours':VoltAmpereReactiveHours,'MilliAmperes':MilliAmperes,'TenthMilliAmperes':TenthMilliAmperes,'MilliVolts':MilliVolts,'TenthDegreesCelsius':TenthDegreesCelsius,'Permil':Permil,'rnx':rnx,'upduMib':upduMib,'upduInfo':upduInfo,_O:upduInfoPartNumber,_P:upduInfoSerialNumber,_Q:upduInfoLotNumber,'upduInventory':upduInventory,'upduModuleTable':upduModuleTable,'upduModuleEntry':upduModuleEntry,_G:upduModuleIndex,_R:upduModuleType,_S:upduModulePartNumber,_T:upduModuleSerialNumber,_U:upduModuleLotNumber,'upduMeasurements':upduMeasurements,'upduMeterTable':upduMeterTable,'upduMeterEntry':upduMeterEntry,_K:upduMeterIndex,_V:upduMeterName,_W:upduMeterType,_X:upduMeterEnergyP,_Y:upduMeterEnergyR1,_Z:upduMeterEnergyR4,_a:upduMeterPowerP,_b:upduMeterPowerQ,_c:upduMeterPowerS,_d:upduMeterUrms,_e:upduMeterIrms,_f:upduMeterSystemName,_g:upduMeterCustomName,_h:upduMeterDescription,'upduSensorTable':upduSensorTable,'upduSensorEntry':upduSensorEntry,_L:upduSensorPort,_m:upduSensorPortName,_n:upduSensorType,_o:upduSensorTemperatureCelsius,_p:upduSensorHumidity,'upduRcmTable':upduRcmTable,'upduRcmEntry':upduRcmEntry,_M:upduRcmIndex,_q:upduRcmName,_r:upduRcmCurrentRms,_s:upduRcmCurrentDc,_t:upduRcmSensorQuality,'upduControl':upduControl,'upduRelayTable':upduRelayTable,'upduRelayEntry':upduRelayEntry,_N:upduRelayIndex,_i:upduRelayMeterNames,_j:upduRelayAdminStatus,_k:upduRelayOperStatus,_l:upduRelayCondition,'upduConformance':upduConformance,'upduMibCompliances':upduMibCompliances,'upduMibCompliance':upduMibCompliance,'upduMibGroups':upduMibGroups,_u:upduMibGroupRev1})