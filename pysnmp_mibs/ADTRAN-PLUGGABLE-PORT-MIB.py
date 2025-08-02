_o='adGenPluggablePortIntervalStatsInterval'
_n='adGenPluggablePortIntervalStatsIndex'
_m='adGenPluggablePortDayStatsIndex'
_l='adGenPluggablePortCurrentStatsIndex'
_k='adGenPluggablePortTotalStatsIndex'
_j='adGenPluggablePortChannelXcvrIndex'
_i='milliAmps'
_h='highTemp'
_g='speedMismatch'
_f='unsupported'
_e='missing'
_d='txFault'
_c='Unsigned32'
_b='critical'
_a='major'
_Z='minor'
_Y='alert'
_X='info'
_W='adGenPluggablePortIndex'
_V='read-write'
_U='Bits'
_T='deprecated'
_S='not-accessible'
_R='OctetString'
_Q='ADTRAN-PLUGGABLE-PORT-MIB'
_P='Integer32'
_O='sysName'
_N='SNMPv2-MIB'
_M='ifDescr'
_L='adTAeSCUTrapAlarmLevel'
_K='ADTRAN-TAeSCUEXT1-MIB'
_J='adTrapInformSeqNum'
_I='ADTRAN-GENTRAPINFORM-MIB'
_H='adGenPortTrapIdentifier'
_G='ADTRAN-GENPORT-MIB'
_F='ifIndex'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols(_G,_H)
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
adTrapInformSeqNum,=mibBuilder.importSymbols(_I,_J)
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
adGenPluggablePort,adGenPluggablePortID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenPluggablePort','adGenPluggablePortID')
adTAeSCUTrapAlarmLevel,=mibBuilder.importSymbols(_K,_L)
InterfaceIndex,ifDescr,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndex',_M,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_U,'Counter32','Counter64','Gauge32',_P,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_c,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenPluggablePortMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,4,1))
if mibBuilder.loadTexts:adGenPluggablePortMIB.setRevisions(('2020-03-19 00:00','2019-08-14 00:00','2019-05-31 00:00','2016-04-15 00:00','2013-06-13 00:00','2012-01-23 00:00','2011-03-22 00:00'))
class PluggablePortPowerUnits(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dBm',1),('tenthsDBm',2),('microWatts',3),('tenthsMicroWatts',4)))
_AdGenPluggablePortObjects_ObjectIdentity=ObjectIdentity
adGenPluggablePortObjects=_AdGenPluggablePortObjects_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,1))
_AdGenPluggablePortTable_Object=MibTable
adGenPluggablePortTable=_AdGenPluggablePortTable_Object((1,3,6,1,4,1,664,5,70,4,1,1))
if mibBuilder.loadTexts:adGenPluggablePortTable.setStatus(_A)
_AdGenPluggablePortEntry_Object=MibTableRow
adGenPluggablePortEntry=_AdGenPluggablePortEntry_Object((1,3,6,1,4,1,664,5,70,4,1,1,1))
adGenPluggablePortEntry.setIndexNames((0,_Q,_W))
if mibBuilder.loadTexts:adGenPluggablePortEntry.setStatus(_A)
_AdGenPluggablePortIndex_Type=InterfaceIndex
_AdGenPluggablePortIndex_Object=MibTableColumn
adGenPluggablePortIndex=_AdGenPluggablePortIndex_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,1),_AdGenPluggablePortIndex_Type())
adGenPluggablePortIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortIndex.setStatus(_A)
class _AdGenPluggablePortPluggableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('sfp',2),('xfp',3),('unknown',4),('qsfp',5)))
_AdGenPluggablePortPluggableType_Type.__name__=_P
_AdGenPluggablePortPluggableType_Object=MibTableColumn
adGenPluggablePortPluggableType=_AdGenPluggablePortPluggableType_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,2),_AdGenPluggablePortPluggableType_Type())
adGenPluggablePortPluggableType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortPluggableType.setStatus(_A)
class _AdGenPluggablePortConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('other',1),('fiberLC',2),('fiberSC',3),('mtrj',4),('hssdc',5),('copperRJ45',6),('none',7),('copperPigtail',8),('opticalPigtail',9),('mpo',10),('noSeparable',11)))
_AdGenPluggablePortConnectorType_Type.__name__=_P
_AdGenPluggablePortConnectorType_Object=MibTableColumn
adGenPluggablePortConnectorType=_AdGenPluggablePortConnectorType_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,3),_AdGenPluggablePortConnectorType_Type())
adGenPluggablePortConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortConnectorType.setStatus(_A)
class _AdGenPluggablePortCapabilities_Type(Bits):namedValues=NamedValues(*(('pluggable',0),('berReadable',1),('voltageReadable',2),('wavelengthReadable',3),('diagnosticsAvailable',4),('wavelengthProvisionable',5)))
_AdGenPluggablePortCapabilities_Type.__name__=_U
_AdGenPluggablePortCapabilities_Object=MibTableColumn
adGenPluggablePortCapabilities=_AdGenPluggablePortCapabilities_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,4),_AdGenPluggablePortCapabilities_Type())
adGenPluggablePortCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCapabilities.setStatus(_A)
class _AdGenPluggablePortState_Type(Bits):namedValues=NamedValues(*(('portUnsupported',0),('portUp',1),('portDown',2),('portLos',3),('portLol',4),('portSignalDegrade',5),('portSignalFail',6),('portMissing',7),('cardMissing',8)))
_AdGenPluggablePortState_Type.__name__=_U
_AdGenPluggablePortState_Object=MibTableColumn
adGenPluggablePortState=_AdGenPluggablePortState_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,5),_AdGenPluggablePortState_Type())
adGenPluggablePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortState.setStatus(_A)
class _AdGenPluggablePortStatusBits_Type(Bits):namedValues=NamedValues(*(('isPresent',0),('isValid',1),('isSupported',2),('isMismatched',3),('isTxEnabled',4),('isTxFault',5),('isWavelengthMismatch',6)))
_AdGenPluggablePortStatusBits_Type.__name__=_U
_AdGenPluggablePortStatusBits_Object=MibTableColumn
adGenPluggablePortStatusBits=_AdGenPluggablePortStatusBits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,6),_AdGenPluggablePortStatusBits_Type())
adGenPluggablePortStatusBits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortStatusBits.setStatus(_A)
class _AdGenPluggablePortAlarmBits_Type(Bits):namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3),(_h,4),('wavelengthMismatch',5)))
_AdGenPluggablePortAlarmBits_Type.__name__=_U
_AdGenPluggablePortAlarmBits_Object=MibTableColumn
adGenPluggablePortAlarmBits=_AdGenPluggablePortAlarmBits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,7),_AdGenPluggablePortAlarmBits_Type())
adGenPluggablePortAlarmBits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortAlarmBits.setStatus(_A)
class _AdGenPluggablePortAlarmsSuppressed_Type(Bits):namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3),(_h,4),('wavelengthMismacth',5)))
_AdGenPluggablePortAlarmsSuppressed_Type.__name__=_U
_AdGenPluggablePortAlarmsSuppressed_Object=MibTableColumn
adGenPluggablePortAlarmsSuppressed=_AdGenPluggablePortAlarmsSuppressed_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,8),_AdGenPluggablePortAlarmsSuppressed_Type())
adGenPluggablePortAlarmsSuppressed.setMaxAccess(_V)
if mibBuilder.loadTexts:adGenPluggablePortAlarmsSuppressed.setStatus(_A)
_AdGenPluggablePortBer_Type=Unsigned32
_AdGenPluggablePortBer_Object=MibTableColumn
adGenPluggablePortBer=_AdGenPluggablePortBer_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,9),_AdGenPluggablePortBer_Type())
adGenPluggablePortBer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortBer.setStatus(_A)
class _AdGenPluggablePortVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortVendorName_Type.__name__=_R
_AdGenPluggablePortVendorName_Object=MibTableColumn
adGenPluggablePortVendorName=_AdGenPluggablePortVendorName_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,10),_AdGenPluggablePortVendorName_Type())
adGenPluggablePortVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortVendorName.setStatus(_A)
class _AdGenPluggablePortVendorPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortVendorPartNumber_Type.__name__=_R
_AdGenPluggablePortVendorPartNumber_Object=MibTableColumn
adGenPluggablePortVendorPartNumber=_AdGenPluggablePortVendorPartNumber_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,11),_AdGenPluggablePortVendorPartNumber_Type())
adGenPluggablePortVendorPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortVendorPartNumber.setStatus(_A)
class _AdGenPluggablePortVendorSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortVendorSerialNumber_Type.__name__=_R
_AdGenPluggablePortVendorSerialNumber_Object=MibTableColumn
adGenPluggablePortVendorSerialNumber=_AdGenPluggablePortVendorSerialNumber_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,12),_AdGenPluggablePortVendorSerialNumber_Type())
adGenPluggablePortVendorSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortVendorSerialNumber.setStatus(_A)
class _AdGenPluggablePortAdtranName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortAdtranName_Type.__name__=_R
_AdGenPluggablePortAdtranName_Object=MibTableColumn
adGenPluggablePortAdtranName=_AdGenPluggablePortAdtranName_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,13),_AdGenPluggablePortAdtranName_Type())
adGenPluggablePortAdtranName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortAdtranName.setStatus(_A)
class _AdGenPluggablePortAdtranPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortAdtranPartNumber_Type.__name__=_R
_AdGenPluggablePortAdtranPartNumber_Object=MibTableColumn
adGenPluggablePortAdtranPartNumber=_AdGenPluggablePortAdtranPartNumber_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,14),_AdGenPluggablePortAdtranPartNumber_Type())
adGenPluggablePortAdtranPartNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortAdtranPartNumber.setStatus(_A)
class _AdGenPluggablePortAdtranClei_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdGenPluggablePortAdtranClei_Type.__name__=_R
_AdGenPluggablePortAdtranClei_Object=MibTableColumn
adGenPluggablePortAdtranClei=_AdGenPluggablePortAdtranClei_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,15),_AdGenPluggablePortAdtranClei_Type())
adGenPluggablePortAdtranClei.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortAdtranClei.setStatus(_A)
_AdGenPluggablePortWavelength_Type=Unsigned32
_AdGenPluggablePortWavelength_Object=MibTableColumn
adGenPluggablePortWavelength=_AdGenPluggablePortWavelength_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,16),_AdGenPluggablePortWavelength_Type())
adGenPluggablePortWavelength.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortWavelength.setStatus(_A)
_AdGenPluggablePortMinBitRate_Type=Unsigned32
_AdGenPluggablePortMinBitRate_Object=MibTableColumn
adGenPluggablePortMinBitRate=_AdGenPluggablePortMinBitRate_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,17),_AdGenPluggablePortMinBitRate_Type())
adGenPluggablePortMinBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortMinBitRate.setStatus(_A)
_AdGenPluggablePortMaxBitRate_Type=Unsigned32
_AdGenPluggablePortMaxBitRate_Object=MibTableColumn
adGenPluggablePortMaxBitRate=_AdGenPluggablePortMaxBitRate_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,18),_AdGenPluggablePortMaxBitRate_Type())
adGenPluggablePortMaxBitRate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortMaxBitRate.setStatus(_A)
_AdGenPluggablePortReachLength_Type=Unsigned32
_AdGenPluggablePortReachLength_Object=MibTableColumn
adGenPluggablePortReachLength=_AdGenPluggablePortReachLength_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,19),_AdGenPluggablePortReachLength_Type())
adGenPluggablePortReachLength.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortReachLength.setStatus(_A)
class _AdGenPluggablePortReachUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('reachUnit1Kmfor09um',1),('reachUnit100mfor09um',2),('reachUnit10mfor50um',3),('reachUnit10mfor62um',4),('reachUnit1mforCu',5),('reachUnit1KmforSmf',6),('reachUnit2mforEBW',7),('reachUnit1mfor50um',8),('reachUnit1mfor62um',9)))
_AdGenPluggablePortReachUnits_Type.__name__=_P
_AdGenPluggablePortReachUnits_Object=MibTableColumn
adGenPluggablePortReachUnits=_AdGenPluggablePortReachUnits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,20),_AdGenPluggablePortReachUnits_Type())
adGenPluggablePortReachUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortReachUnits.setStatus(_A)
_AdGenPluggablePortRxPower_Type=Integer32
_AdGenPluggablePortRxPower_Object=MibTableColumn
adGenPluggablePortRxPower=_AdGenPluggablePortRxPower_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,21),_AdGenPluggablePortRxPower_Type())
adGenPluggablePortRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortRxPower.setStatus(_T)
_AdGenPluggablePortRxPowerUnits_Type=PluggablePortPowerUnits
_AdGenPluggablePortRxPowerUnits_Object=MibTableColumn
adGenPluggablePortRxPowerUnits=_AdGenPluggablePortRxPowerUnits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,22),_AdGenPluggablePortRxPowerUnits_Type())
adGenPluggablePortRxPowerUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortRxPowerUnits.setStatus(_T)
_AdGenPluggablePortTxPower_Type=Integer32
_AdGenPluggablePortTxPower_Object=MibTableColumn
adGenPluggablePortTxPower=_AdGenPluggablePortTxPower_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,23),_AdGenPluggablePortTxPower_Type())
adGenPluggablePortTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTxPower.setStatus(_T)
_AdGenPluggablePortTxPowerUnits_Type=PluggablePortPowerUnits
_AdGenPluggablePortTxPowerUnits_Object=MibTableColumn
adGenPluggablePortTxPowerUnits=_AdGenPluggablePortTxPowerUnits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,24),_AdGenPluggablePortTxPowerUnits_Type())
adGenPluggablePortTxPowerUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTxPowerUnits.setStatus(_T)
_AdGenPluggablePortTxBias_Type=Integer32
_AdGenPluggablePortTxBias_Object=MibTableColumn
adGenPluggablePortTxBias=_AdGenPluggablePortTxBias_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,25),_AdGenPluggablePortTxBias_Type())
adGenPluggablePortTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTxBias.setStatus(_T)
class _AdGenPluggablePortTxBiasUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_i,1))
_AdGenPluggablePortTxBiasUnits_Type.__name__=_P
_AdGenPluggablePortTxBiasUnits_Object=MibTableColumn
adGenPluggablePortTxBiasUnits=_AdGenPluggablePortTxBiasUnits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,26),_AdGenPluggablePortTxBiasUnits_Type())
adGenPluggablePortTxBiasUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTxBiasUnits.setStatus(_T)
_AdGenPluggablePortTemperature_Type=Integer32
_AdGenPluggablePortTemperature_Object=MibTableColumn
adGenPluggablePortTemperature=_AdGenPluggablePortTemperature_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,27),_AdGenPluggablePortTemperature_Type())
adGenPluggablePortTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTemperature.setStatus(_A)
class _AdGenPluggablePortTemperatureUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('celsius',1),('tenthsCelsius',2),('fahrenheit',3),('tenthsFahrenheit',4)))
_AdGenPluggablePortTemperatureUnits_Type.__name__=_P
_AdGenPluggablePortTemperatureUnits_Object=MibTableColumn
adGenPluggablePortTemperatureUnits=_AdGenPluggablePortTemperatureUnits_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,28),_AdGenPluggablePortTemperatureUnits_Type())
adGenPluggablePortTemperatureUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTemperatureUnits.setStatus(_A)
_AdGenPluggablePortVoltage_Type=Integer32
_AdGenPluggablePortVoltage_Object=MibTableColumn
adGenPluggablePortVoltage=_AdGenPluggablePortVoltage_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,29),_AdGenPluggablePortVoltage_Type())
adGenPluggablePortVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortVoltage.setStatus(_A)
class _AdGenPluggablePortVendorRevision_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_AdGenPluggablePortVendorRevision_Type.__name__=_R
_AdGenPluggablePortVendorRevision_Object=MibTableColumn
adGenPluggablePortVendorRevision=_AdGenPluggablePortVendorRevision_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,30),_AdGenPluggablePortVendorRevision_Type())
adGenPluggablePortVendorRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortVendorRevision.setStatus(_A)
_AdGenPluggablePortWavelengthPicoMeter_Type=Unsigned32
_AdGenPluggablePortWavelengthPicoMeter_Object=MibTableColumn
adGenPluggablePortWavelengthPicoMeter=_AdGenPluggablePortWavelengthPicoMeter_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,31),_AdGenPluggablePortWavelengthPicoMeter_Type())
adGenPluggablePortWavelengthPicoMeter.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortWavelengthPicoMeter.setStatus(_A)
_AdGenPluggableNumberOfXcvrChannels_Type=Integer32
_AdGenPluggableNumberOfXcvrChannels_Object=MibTableColumn
adGenPluggableNumberOfXcvrChannels=_AdGenPluggableNumberOfXcvrChannels_Object((1,3,6,1,4,1,664,5,70,4,1,1,1,32),_AdGenPluggableNumberOfXcvrChannels_Type())
adGenPluggableNumberOfXcvrChannels.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggableNumberOfXcvrChannels.setStatus(_A)
_AdGenPluggablePortChannelTable_Object=MibTable
adGenPluggablePortChannelTable=_AdGenPluggablePortChannelTable_Object((1,3,6,1,4,1,664,5,70,4,1,2))
if mibBuilder.loadTexts:adGenPluggablePortChannelTable.setStatus(_A)
_AdGenPluggablePortChannelEntry_Object=MibTableRow
adGenPluggablePortChannelEntry=_AdGenPluggablePortChannelEntry_Object((1,3,6,1,4,1,664,5,70,4,1,2,1))
adGenPluggablePortChannelEntry.setIndexNames((0,_Q,_W),(0,_Q,_j))
if mibBuilder.loadTexts:adGenPluggablePortChannelEntry.setStatus(_A)
_AdGenPluggablePortChannelModuleIndex_Type=InterfaceIndex
_AdGenPluggablePortChannelModuleIndex_Object=MibTableColumn
adGenPluggablePortChannelModuleIndex=_AdGenPluggablePortChannelModuleIndex_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,1),_AdGenPluggablePortChannelModuleIndex_Type())
adGenPluggablePortChannelModuleIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortChannelModuleIndex.setStatus(_A)
_AdGenPluggablePortChannelXcvrIndex_Type=Unsigned32
_AdGenPluggablePortChannelXcvrIndex_Object=MibTableColumn
adGenPluggablePortChannelXcvrIndex=_AdGenPluggablePortChannelXcvrIndex_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,2),_AdGenPluggablePortChannelXcvrIndex_Type())
adGenPluggablePortChannelXcvrIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortChannelXcvrIndex.setStatus(_A)
_AdGenPluggablePortChannelRxPower_Type=Integer32
_AdGenPluggablePortChannelRxPower_Object=MibTableColumn
adGenPluggablePortChannelRxPower=_AdGenPluggablePortChannelRxPower_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,3),_AdGenPluggablePortChannelRxPower_Type())
adGenPluggablePortChannelRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelRxPower.setStatus(_A)
_AdGenPluggablePortChannelRxPowerUnits_Type=PluggablePortPowerUnits
_AdGenPluggablePortChannelRxPowerUnits_Object=MibTableColumn
adGenPluggablePortChannelRxPowerUnits=_AdGenPluggablePortChannelRxPowerUnits_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,4),_AdGenPluggablePortChannelRxPowerUnits_Type())
adGenPluggablePortChannelRxPowerUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelRxPowerUnits.setStatus(_A)
_AdGenPluggablePortChannelTxPower_Type=Integer32
_AdGenPluggablePortChannelTxPower_Object=MibTableColumn
adGenPluggablePortChannelTxPower=_AdGenPluggablePortChannelTxPower_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,5),_AdGenPluggablePortChannelTxPower_Type())
adGenPluggablePortChannelTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelTxPower.setStatus(_A)
_AdGenPluggablePortChannelTxPowerUnits_Type=PluggablePortPowerUnits
_AdGenPluggablePortChannelTxPowerUnits_Object=MibTableColumn
adGenPluggablePortChannelTxPowerUnits=_AdGenPluggablePortChannelTxPowerUnits_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,6),_AdGenPluggablePortChannelTxPowerUnits_Type())
adGenPluggablePortChannelTxPowerUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelTxPowerUnits.setStatus(_A)
_AdGenPluggablePortChannelTxBias_Type=Integer32
_AdGenPluggablePortChannelTxBias_Object=MibTableColumn
adGenPluggablePortChannelTxBias=_AdGenPluggablePortChannelTxBias_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,7),_AdGenPluggablePortChannelTxBias_Type())
adGenPluggablePortChannelTxBias.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelTxBias.setStatus(_A)
class _AdGenPluggablePortChannelTxBiasUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_i,1))
_AdGenPluggablePortChannelTxBiasUnits_Type.__name__=_P
_AdGenPluggablePortChannelTxBiasUnits_Object=MibTableColumn
adGenPluggablePortChannelTxBiasUnits=_AdGenPluggablePortChannelTxBiasUnits_Object((1,3,6,1,4,1,664,5,70,4,1,2,1,8),_AdGenPluggablePortChannelTxBiasUnits_Type())
adGenPluggablePortChannelTxBiasUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortChannelTxBiasUnits.setStatus(_A)
_AdGenPluggablePortStats_ObjectIdentity=ObjectIdentity
adGenPluggablePortStats=_AdGenPluggablePortStats_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,2))
_AdGenPluggablePortTotalStatsTable_Object=MibTable
adGenPluggablePortTotalStatsTable=_AdGenPluggablePortTotalStatsTable_Object((1,3,6,1,4,1,664,5,70,4,2,1))
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsTable.setStatus(_A)
_AdGenPluggablePortTotalStatsEntry_Object=MibTableRow
adGenPluggablePortTotalStatsEntry=_AdGenPluggablePortTotalStatsEntry_Object((1,3,6,1,4,1,664,5,70,4,2,1,1))
adGenPluggablePortTotalStatsEntry.setIndexNames((0,_Q,_k))
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsEntry.setStatus(_A)
_AdGenPluggablePortTotalStatsIndex_Type=InterfaceIndex
_AdGenPluggablePortTotalStatsIndex_Object=MibTableColumn
adGenPluggablePortTotalStatsIndex=_AdGenPluggablePortTotalStatsIndex_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,1),_AdGenPluggablePortTotalStatsIndex_Type())
adGenPluggablePortTotalStatsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsIndex.setStatus(_A)
_AdGenPluggablePortTotalStatsMaxRxPower_Type=Integer32
_AdGenPluggablePortTotalStatsMaxRxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsMaxRxPower=_AdGenPluggablePortTotalStatsMaxRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,2),_AdGenPluggablePortTotalStatsMaxRxPower_Type())
adGenPluggablePortTotalStatsMaxRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsMaxRxPower.setStatus(_A)
_AdGenPluggablePortTotalStatsMinRxPower_Type=Integer32
_AdGenPluggablePortTotalStatsMinRxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsMinRxPower=_AdGenPluggablePortTotalStatsMinRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,3),_AdGenPluggablePortTotalStatsMinRxPower_Type())
adGenPluggablePortTotalStatsMinRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsMinRxPower.setStatus(_A)
_AdGenPluggablePortTotalStatsAvgRxPower_Type=Integer32
_AdGenPluggablePortTotalStatsAvgRxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsAvgRxPower=_AdGenPluggablePortTotalStatsAvgRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,4),_AdGenPluggablePortTotalStatsAvgRxPower_Type())
adGenPluggablePortTotalStatsAvgRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsAvgRxPower.setStatus(_A)
_AdGenPluggablePortTotalStatsMaxTxPower_Type=Integer32
_AdGenPluggablePortTotalStatsMaxTxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsMaxTxPower=_AdGenPluggablePortTotalStatsMaxTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,5),_AdGenPluggablePortTotalStatsMaxTxPower_Type())
adGenPluggablePortTotalStatsMaxTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsMaxTxPower.setStatus(_A)
_AdGenPluggablePortTotalStatsMinTxPower_Type=Integer32
_AdGenPluggablePortTotalStatsMinTxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsMinTxPower=_AdGenPluggablePortTotalStatsMinTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,6),_AdGenPluggablePortTotalStatsMinTxPower_Type())
adGenPluggablePortTotalStatsMinTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsMinTxPower.setStatus(_A)
_AdGenPluggablePortTotalStatsAvgTxPower_Type=Integer32
_AdGenPluggablePortTotalStatsAvgTxPower_Object=MibTableColumn
adGenPluggablePortTotalStatsAvgTxPower=_AdGenPluggablePortTotalStatsAvgTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,1,1,7),_AdGenPluggablePortTotalStatsAvgTxPower_Type())
adGenPluggablePortTotalStatsAvgTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortTotalStatsAvgTxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsTable_Object=MibTable
adGenPluggablePortCurrentStatsTable=_AdGenPluggablePortCurrentStatsTable_Object((1,3,6,1,4,1,664,5,70,4,2,2))
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsTable.setStatus(_A)
_AdGenPluggablePortCurrentStatsEntry_Object=MibTableRow
adGenPluggablePortCurrentStatsEntry=_AdGenPluggablePortCurrentStatsEntry_Object((1,3,6,1,4,1,664,5,70,4,2,2,1))
adGenPluggablePortCurrentStatsEntry.setIndexNames((0,_Q,_l))
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsEntry.setStatus(_A)
_AdGenPluggablePortCurrentStatsIndex_Type=InterfaceIndex
_AdGenPluggablePortCurrentStatsIndex_Object=MibTableColumn
adGenPluggablePortCurrentStatsIndex=_AdGenPluggablePortCurrentStatsIndex_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,1),_AdGenPluggablePortCurrentStatsIndex_Type())
adGenPluggablePortCurrentStatsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsIndex.setStatus(_A)
_AdGenPluggablePortCurrentStatsMaxRxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsMaxRxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsMaxRxPower=_AdGenPluggablePortCurrentStatsMaxRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,2),_AdGenPluggablePortCurrentStatsMaxRxPower_Type())
adGenPluggablePortCurrentStatsMaxRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsMaxRxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsMinRxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsMinRxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsMinRxPower=_AdGenPluggablePortCurrentStatsMinRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,3),_AdGenPluggablePortCurrentStatsMinRxPower_Type())
adGenPluggablePortCurrentStatsMinRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsMinRxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsAvgRxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsAvgRxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsAvgRxPower=_AdGenPluggablePortCurrentStatsAvgRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,4),_AdGenPluggablePortCurrentStatsAvgRxPower_Type())
adGenPluggablePortCurrentStatsAvgRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsAvgRxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsMaxTxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsMaxTxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsMaxTxPower=_AdGenPluggablePortCurrentStatsMaxTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,5),_AdGenPluggablePortCurrentStatsMaxTxPower_Type())
adGenPluggablePortCurrentStatsMaxTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsMaxTxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsMinTxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsMinTxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsMinTxPower=_AdGenPluggablePortCurrentStatsMinTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,6),_AdGenPluggablePortCurrentStatsMinTxPower_Type())
adGenPluggablePortCurrentStatsMinTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsMinTxPower.setStatus(_A)
_AdGenPluggablePortCurrentStatsAvgTxPower_Type=Integer32
_AdGenPluggablePortCurrentStatsAvgTxPower_Object=MibTableColumn
adGenPluggablePortCurrentStatsAvgTxPower=_AdGenPluggablePortCurrentStatsAvgTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,2,1,7),_AdGenPluggablePortCurrentStatsAvgTxPower_Type())
adGenPluggablePortCurrentStatsAvgTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortCurrentStatsAvgTxPower.setStatus(_A)
_AdGenPluggablePortDayStatsTable_Object=MibTable
adGenPluggablePortDayStatsTable=_AdGenPluggablePortDayStatsTable_Object((1,3,6,1,4,1,664,5,70,4,2,3))
if mibBuilder.loadTexts:adGenPluggablePortDayStatsTable.setStatus(_A)
_AdGenPluggablePortDayStatsEntry_Object=MibTableRow
adGenPluggablePortDayStatsEntry=_AdGenPluggablePortDayStatsEntry_Object((1,3,6,1,4,1,664,5,70,4,2,3,1))
adGenPluggablePortDayStatsEntry.setIndexNames((0,_Q,_m))
if mibBuilder.loadTexts:adGenPluggablePortDayStatsEntry.setStatus(_A)
_AdGenPluggablePortDayStatsIndex_Type=InterfaceIndex
_AdGenPluggablePortDayStatsIndex_Object=MibTableColumn
adGenPluggablePortDayStatsIndex=_AdGenPluggablePortDayStatsIndex_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,1),_AdGenPluggablePortDayStatsIndex_Type())
adGenPluggablePortDayStatsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsIndex.setStatus(_A)
_AdGenPluggablePortDayStatsMaxRxPower_Type=Integer32
_AdGenPluggablePortDayStatsMaxRxPower_Object=MibTableColumn
adGenPluggablePortDayStatsMaxRxPower=_AdGenPluggablePortDayStatsMaxRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,2),_AdGenPluggablePortDayStatsMaxRxPower_Type())
adGenPluggablePortDayStatsMaxRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsMaxRxPower.setStatus(_A)
_AdGenPluggablePortDayStatsMinRxPower_Type=Integer32
_AdGenPluggablePortDayStatsMinRxPower_Object=MibTableColumn
adGenPluggablePortDayStatsMinRxPower=_AdGenPluggablePortDayStatsMinRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,3),_AdGenPluggablePortDayStatsMinRxPower_Type())
adGenPluggablePortDayStatsMinRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsMinRxPower.setStatus(_A)
_AdGenPluggablePortDayStatsAvgRxPower_Type=Integer32
_AdGenPluggablePortDayStatsAvgRxPower_Object=MibTableColumn
adGenPluggablePortDayStatsAvgRxPower=_AdGenPluggablePortDayStatsAvgRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,4),_AdGenPluggablePortDayStatsAvgRxPower_Type())
adGenPluggablePortDayStatsAvgRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsAvgRxPower.setStatus(_A)
_AdGenPluggablePortDayStatsMaxTxPower_Type=Integer32
_AdGenPluggablePortDayStatsMaxTxPower_Object=MibTableColumn
adGenPluggablePortDayStatsMaxTxPower=_AdGenPluggablePortDayStatsMaxTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,5),_AdGenPluggablePortDayStatsMaxTxPower_Type())
adGenPluggablePortDayStatsMaxTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsMaxTxPower.setStatus(_A)
_AdGenPluggablePortDayStatsMinTxPower_Type=Integer32
_AdGenPluggablePortDayStatsMinTxPower_Object=MibTableColumn
adGenPluggablePortDayStatsMinTxPower=_AdGenPluggablePortDayStatsMinTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,6),_AdGenPluggablePortDayStatsMinTxPower_Type())
adGenPluggablePortDayStatsMinTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsMinTxPower.setStatus(_A)
_AdGenPluggablePortDayStatsAvgTxPower_Type=Integer32
_AdGenPluggablePortDayStatsAvgTxPower_Object=MibTableColumn
adGenPluggablePortDayStatsAvgTxPower=_AdGenPluggablePortDayStatsAvgTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,3,1,7),_AdGenPluggablePortDayStatsAvgTxPower_Type())
adGenPluggablePortDayStatsAvgTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortDayStatsAvgTxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsTable_Object=MibTable
adGenPluggablePortIntervalStatsTable=_AdGenPluggablePortIntervalStatsTable_Object((1,3,6,1,4,1,664,5,70,4,2,4))
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsTable.setStatus(_A)
_AdGenPluggablePortIntervalStatsEntry_Object=MibTableRow
adGenPluggablePortIntervalStatsEntry=_AdGenPluggablePortIntervalStatsEntry_Object((1,3,6,1,4,1,664,5,70,4,2,4,1))
adGenPluggablePortIntervalStatsEntry.setIndexNames((0,_Q,_n),(0,_Q,_o))
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsEntry.setStatus(_A)
_AdGenPluggablePortIntervalStatsIndex_Type=InterfaceIndex
_AdGenPluggablePortIntervalStatsIndex_Object=MibTableColumn
adGenPluggablePortIntervalStatsIndex=_AdGenPluggablePortIntervalStatsIndex_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,1),_AdGenPluggablePortIntervalStatsIndex_Type())
adGenPluggablePortIntervalStatsIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsIndex.setStatus(_A)
class _AdGenPluggablePortIntervalStatsInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenPluggablePortIntervalStatsInterval_Type.__name__=_c
_AdGenPluggablePortIntervalStatsInterval_Object=MibTableColumn
adGenPluggablePortIntervalStatsInterval=_AdGenPluggablePortIntervalStatsInterval_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,2),_AdGenPluggablePortIntervalStatsInterval_Type())
adGenPluggablePortIntervalStatsInterval.setMaxAccess(_S)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsInterval.setStatus(_A)
_AdGenPluggablePortIntervalStatsMaxRxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsMaxRxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsMaxRxPower=_AdGenPluggablePortIntervalStatsMaxRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,3),_AdGenPluggablePortIntervalStatsMaxRxPower_Type())
adGenPluggablePortIntervalStatsMaxRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsMaxRxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsMinRxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsMinRxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsMinRxPower=_AdGenPluggablePortIntervalStatsMinRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,4),_AdGenPluggablePortIntervalStatsMinRxPower_Type())
adGenPluggablePortIntervalStatsMinRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsMinRxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsAvgRxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsAvgRxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsAvgRxPower=_AdGenPluggablePortIntervalStatsAvgRxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,5),_AdGenPluggablePortIntervalStatsAvgRxPower_Type())
adGenPluggablePortIntervalStatsAvgRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsAvgRxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsMaxTxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsMaxTxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsMaxTxPower=_AdGenPluggablePortIntervalStatsMaxTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,6),_AdGenPluggablePortIntervalStatsMaxTxPower_Type())
adGenPluggablePortIntervalStatsMaxTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsMaxTxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsMinTxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsMinTxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsMinTxPower=_AdGenPluggablePortIntervalStatsMinTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,7),_AdGenPluggablePortIntervalStatsMinTxPower_Type())
adGenPluggablePortIntervalStatsMinTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsMinTxPower.setStatus(_A)
_AdGenPluggablePortIntervalStatsAvgTxPower_Type=Integer32
_AdGenPluggablePortIntervalStatsAvgTxPower_Object=MibTableColumn
adGenPluggablePortIntervalStatsAvgTxPower=_AdGenPluggablePortIntervalStatsAvgTxPower_Object((1,3,6,1,4,1,664,5,70,4,2,4,1,8),_AdGenPluggablePortIntervalStatsAvgTxPower_Type())
adGenPluggablePortIntervalStatsAvgTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortIntervalStatsAvgTxPower.setStatus(_A)
_AdGenPluggablePortScalars_ObjectIdentity=ObjectIdentity
adGenPluggablePortScalars=_AdGenPluggablePortScalars_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,3))
class _AdGenPluggablePortAlarmLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_AdGenPluggablePortAlarmLevel_Type.__name__=_P
_AdGenPluggablePortAlarmLevel_Object=MibScalar
adGenPluggablePortAlarmLevel=_AdGenPluggablePortAlarmLevel_Object((1,3,6,1,4,1,664,5,70,4,3,1),_AdGenPluggablePortAlarmLevel_Type())
adGenPluggablePortAlarmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPluggablePortAlarmLevel.setStatus(_T)
_AdGenPluggablePortTraps_ObjectIdentity=ObjectIdentity
adGenPluggablePortTraps=_AdGenPluggablePortTraps_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,4))
_AdGenPluggablePortAlarms_ObjectIdentity=ObjectIdentity
adGenPluggablePortAlarms=_AdGenPluggablePortAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,4,0))
_AdGenPluggablePortProv_ObjectIdentity=ObjectIdentity
adGenPluggablePortProv=_AdGenPluggablePortProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,4,5))
_AdGenPluggablePortProvTable_Object=MibTable
adGenPluggablePortProvTable=_AdGenPluggablePortProvTable_Object((1,3,6,1,4,1,664,5,70,4,5,1))
if mibBuilder.loadTexts:adGenPluggablePortProvTable.setStatus(_A)
_AdGenPluggablePortProvEntry_Object=MibTableRow
adGenPluggablePortProvEntry=_AdGenPluggablePortProvEntry_Object((1,3,6,1,4,1,664,5,70,4,5,1,1))
adGenPluggablePortProvEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:adGenPluggablePortProvEntry.setStatus(_A)
_AdGenPluggablePortProvWaveLength_Type=Integer32
_AdGenPluggablePortProvWaveLength_Object=MibTableColumn
adGenPluggablePortProvWaveLength=_AdGenPluggablePortProvWaveLength_Object((1,3,6,1,4,1,664,5,70,4,5,1,1,1),_AdGenPluggablePortProvWaveLength_Type())
adGenPluggablePortProvWaveLength.setMaxAccess(_V)
if mibBuilder.loadTexts:adGenPluggablePortProvWaveLength.setStatus(_A)
_AdGenPluggablePortProvChannelNumber_Type=Integer32
_AdGenPluggablePortProvChannelNumber_Object=MibTableColumn
adGenPluggablePortProvChannelNumber=_AdGenPluggablePortProvChannelNumber_Object((1,3,6,1,4,1,664,5,70,4,5,1,1,2),_AdGenPluggablePortProvChannelNumber_Type())
adGenPluggablePortProvChannelNumber.setMaxAccess(_V)
if mibBuilder.loadTexts:adGenPluggablePortProvChannelNumber.setStatus(_A)
_AdGenPluggableAlarmSlotProvTable_Object=MibTable
adGenPluggableAlarmSlotProvTable=_AdGenPluggableAlarmSlotProvTable_Object((1,3,6,1,4,1,664,5,70,4,5,2))
if mibBuilder.loadTexts:adGenPluggableAlarmSlotProvTable.setStatus(_A)
_AdGenPluggableAlarmSlotProvEntry_Object=MibTableRow
adGenPluggableAlarmSlotProvEntry=_AdGenPluggableAlarmSlotProvEntry_Object((1,3,6,1,4,1,664,5,70,4,5,2,1))
adGenPluggableAlarmSlotProvEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenPluggableAlarmSlotProvEntry.setStatus(_A)
class _AdGenPluggableAlarmSlotTxFaultLevel_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_AdGenPluggableAlarmSlotTxFaultLevel_Type.__name__=_P
_AdGenPluggableAlarmSlotTxFaultLevel_Object=MibTableColumn
adGenPluggableAlarmSlotTxFaultLevel=_AdGenPluggableAlarmSlotTxFaultLevel_Object((1,3,6,1,4,1,664,5,70,4,5,2,1,1),_AdGenPluggableAlarmSlotTxFaultLevel_Type())
adGenPluggableAlarmSlotTxFaultLevel.setMaxAccess(_V)
if mibBuilder.loadTexts:adGenPluggableAlarmSlotTxFaultLevel.setStatus(_A)
class _AdGenPluggableAlarmSlotMissingLevel_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6)));namedValues=NamedValues(*((_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_AdGenPluggableAlarmSlotMissingLevel_Type.__name__=_P
_AdGenPluggableAlarmSlotMissingLevel_Object=MibTableColumn
adGenPluggableAlarmSlotMissingLevel=_AdGenPluggableAlarmSlotMissingLevel_Object((1,3,6,1,4,1,664,5,70,4,5,2,1,2),_AdGenPluggableAlarmSlotMissingLevel_Type())
adGenPluggableAlarmSlotMissingLevel.setMaxAccess(_V)
if mibBuilder.loadTexts:adGenPluggableAlarmSlotMissingLevel.setStatus(_A)
adGenPluggablePortTxFaultClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,2))
adGenPluggablePortTxFaultClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortTxFaultClear.setStatus(_A)
adGenPluggablePortTxFaultSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,3))
adGenPluggablePortTxFaultSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortTxFaultSet.setStatus(_A)
adGenPluggablePortMissingClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,4))
adGenPluggablePortMissingClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortMissingClear.setStatus(_A)
adGenPluggablePortMissingSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,5))
adGenPluggablePortMissingSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortMissingSet.setStatus(_A)
adGenPluggablePortUnsupportedClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,6))
adGenPluggablePortUnsupportedClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortUnsupportedClear.setStatus(_A)
adGenPluggablePortUnsupportedSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,7))
adGenPluggablePortUnsupportedSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortUnsupportedSet.setStatus(_A)
adGenPluggablePortMismatchClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,8))
adGenPluggablePortMismatchClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortMismatchClear.setStatus(_A)
adGenPluggablePortMismatchSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,9))
adGenPluggablePortMismatchSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortMismatchSet.setStatus(_A)
adGenPluggablePortTempClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,10))
adGenPluggablePortTempClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortTempClear.setStatus(_A)
adGenPluggablePortTempSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,11))
adGenPluggablePortTempSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortTempSet.setStatus(_A)
adGenPluggablePortProvWavelengthMismatchClear=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,12))
adGenPluggablePortProvWavelengthMismatchClear.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortProvWavelengthMismatchClear.setStatus(_A)
adGenPluggablePortProvWavelengthMismatchSet=NotificationType((1,3,6,1,4,1,664,5,70,4,4,0,13))
adGenPluggablePortProvWavelengthMismatchSet.setObjects(*((_I,_J),(_N,_O),(_D,_E),(_G,_H),(_C,_F),(_K,_L),(_C,_M)))
if mibBuilder.loadTexts:adGenPluggablePortProvWavelengthMismatchSet.setStatus(_A)
mibBuilder.exportSymbols(_Q,**{'PluggablePortPowerUnits':PluggablePortPowerUnits,'adGenPluggablePortObjects':adGenPluggablePortObjects,'adGenPluggablePortTable':adGenPluggablePortTable,'adGenPluggablePortEntry':adGenPluggablePortEntry,_W:adGenPluggablePortIndex,'adGenPluggablePortPluggableType':adGenPluggablePortPluggableType,'adGenPluggablePortConnectorType':adGenPluggablePortConnectorType,'adGenPluggablePortCapabilities':adGenPluggablePortCapabilities,'adGenPluggablePortState':adGenPluggablePortState,'adGenPluggablePortStatusBits':adGenPluggablePortStatusBits,'adGenPluggablePortAlarmBits':adGenPluggablePortAlarmBits,'adGenPluggablePortAlarmsSuppressed':adGenPluggablePortAlarmsSuppressed,'adGenPluggablePortBer':adGenPluggablePortBer,'adGenPluggablePortVendorName':adGenPluggablePortVendorName,'adGenPluggablePortVendorPartNumber':adGenPluggablePortVendorPartNumber,'adGenPluggablePortVendorSerialNumber':adGenPluggablePortVendorSerialNumber,'adGenPluggablePortAdtranName':adGenPluggablePortAdtranName,'adGenPluggablePortAdtranPartNumber':adGenPluggablePortAdtranPartNumber,'adGenPluggablePortAdtranClei':adGenPluggablePortAdtranClei,'adGenPluggablePortWavelength':adGenPluggablePortWavelength,'adGenPluggablePortMinBitRate':adGenPluggablePortMinBitRate,'adGenPluggablePortMaxBitRate':adGenPluggablePortMaxBitRate,'adGenPluggablePortReachLength':adGenPluggablePortReachLength,'adGenPluggablePortReachUnits':adGenPluggablePortReachUnits,'adGenPluggablePortRxPower':adGenPluggablePortRxPower,'adGenPluggablePortRxPowerUnits':adGenPluggablePortRxPowerUnits,'adGenPluggablePortTxPower':adGenPluggablePortTxPower,'adGenPluggablePortTxPowerUnits':adGenPluggablePortTxPowerUnits,'adGenPluggablePortTxBias':adGenPluggablePortTxBias,'adGenPluggablePortTxBiasUnits':adGenPluggablePortTxBiasUnits,'adGenPluggablePortTemperature':adGenPluggablePortTemperature,'adGenPluggablePortTemperatureUnits':adGenPluggablePortTemperatureUnits,'adGenPluggablePortVoltage':adGenPluggablePortVoltage,'adGenPluggablePortVendorRevision':adGenPluggablePortVendorRevision,'adGenPluggablePortWavelengthPicoMeter':adGenPluggablePortWavelengthPicoMeter,'adGenPluggableNumberOfXcvrChannels':adGenPluggableNumberOfXcvrChannels,'adGenPluggablePortChannelTable':adGenPluggablePortChannelTable,'adGenPluggablePortChannelEntry':adGenPluggablePortChannelEntry,'adGenPluggablePortChannelModuleIndex':adGenPluggablePortChannelModuleIndex,_j:adGenPluggablePortChannelXcvrIndex,'adGenPluggablePortChannelRxPower':adGenPluggablePortChannelRxPower,'adGenPluggablePortChannelRxPowerUnits':adGenPluggablePortChannelRxPowerUnits,'adGenPluggablePortChannelTxPower':adGenPluggablePortChannelTxPower,'adGenPluggablePortChannelTxPowerUnits':adGenPluggablePortChannelTxPowerUnits,'adGenPluggablePortChannelTxBias':adGenPluggablePortChannelTxBias,'adGenPluggablePortChannelTxBiasUnits':adGenPluggablePortChannelTxBiasUnits,'adGenPluggablePortStats':adGenPluggablePortStats,'adGenPluggablePortTotalStatsTable':adGenPluggablePortTotalStatsTable,'adGenPluggablePortTotalStatsEntry':adGenPluggablePortTotalStatsEntry,_k:adGenPluggablePortTotalStatsIndex,'adGenPluggablePortTotalStatsMaxRxPower':adGenPluggablePortTotalStatsMaxRxPower,'adGenPluggablePortTotalStatsMinRxPower':adGenPluggablePortTotalStatsMinRxPower,'adGenPluggablePortTotalStatsAvgRxPower':adGenPluggablePortTotalStatsAvgRxPower,'adGenPluggablePortTotalStatsMaxTxPower':adGenPluggablePortTotalStatsMaxTxPower,'adGenPluggablePortTotalStatsMinTxPower':adGenPluggablePortTotalStatsMinTxPower,'adGenPluggablePortTotalStatsAvgTxPower':adGenPluggablePortTotalStatsAvgTxPower,'adGenPluggablePortCurrentStatsTable':adGenPluggablePortCurrentStatsTable,'adGenPluggablePortCurrentStatsEntry':adGenPluggablePortCurrentStatsEntry,_l:adGenPluggablePortCurrentStatsIndex,'adGenPluggablePortCurrentStatsMaxRxPower':adGenPluggablePortCurrentStatsMaxRxPower,'adGenPluggablePortCurrentStatsMinRxPower':adGenPluggablePortCurrentStatsMinRxPower,'adGenPluggablePortCurrentStatsAvgRxPower':adGenPluggablePortCurrentStatsAvgRxPower,'adGenPluggablePortCurrentStatsMaxTxPower':adGenPluggablePortCurrentStatsMaxTxPower,'adGenPluggablePortCurrentStatsMinTxPower':adGenPluggablePortCurrentStatsMinTxPower,'adGenPluggablePortCurrentStatsAvgTxPower':adGenPluggablePortCurrentStatsAvgTxPower,'adGenPluggablePortDayStatsTable':adGenPluggablePortDayStatsTable,'adGenPluggablePortDayStatsEntry':adGenPluggablePortDayStatsEntry,_m:adGenPluggablePortDayStatsIndex,'adGenPluggablePortDayStatsMaxRxPower':adGenPluggablePortDayStatsMaxRxPower,'adGenPluggablePortDayStatsMinRxPower':adGenPluggablePortDayStatsMinRxPower,'adGenPluggablePortDayStatsAvgRxPower':adGenPluggablePortDayStatsAvgRxPower,'adGenPluggablePortDayStatsMaxTxPower':adGenPluggablePortDayStatsMaxTxPower,'adGenPluggablePortDayStatsMinTxPower':adGenPluggablePortDayStatsMinTxPower,'adGenPluggablePortDayStatsAvgTxPower':adGenPluggablePortDayStatsAvgTxPower,'adGenPluggablePortIntervalStatsTable':adGenPluggablePortIntervalStatsTable,'adGenPluggablePortIntervalStatsEntry':adGenPluggablePortIntervalStatsEntry,_n:adGenPluggablePortIntervalStatsIndex,_o:adGenPluggablePortIntervalStatsInterval,'adGenPluggablePortIntervalStatsMaxRxPower':adGenPluggablePortIntervalStatsMaxRxPower,'adGenPluggablePortIntervalStatsMinRxPower':adGenPluggablePortIntervalStatsMinRxPower,'adGenPluggablePortIntervalStatsAvgRxPower':adGenPluggablePortIntervalStatsAvgRxPower,'adGenPluggablePortIntervalStatsMaxTxPower':adGenPluggablePortIntervalStatsMaxTxPower,'adGenPluggablePortIntervalStatsMinTxPower':adGenPluggablePortIntervalStatsMinTxPower,'adGenPluggablePortIntervalStatsAvgTxPower':adGenPluggablePortIntervalStatsAvgTxPower,'adGenPluggablePortScalars':adGenPluggablePortScalars,'adGenPluggablePortAlarmLevel':adGenPluggablePortAlarmLevel,'adGenPluggablePortTraps':adGenPluggablePortTraps,'adGenPluggablePortAlarms':adGenPluggablePortAlarms,'adGenPluggablePortTxFaultClear':adGenPluggablePortTxFaultClear,'adGenPluggablePortTxFaultSet':adGenPluggablePortTxFaultSet,'adGenPluggablePortMissingClear':adGenPluggablePortMissingClear,'adGenPluggablePortMissingSet':adGenPluggablePortMissingSet,'adGenPluggablePortUnsupportedClear':adGenPluggablePortUnsupportedClear,'adGenPluggablePortUnsupportedSet':adGenPluggablePortUnsupportedSet,'adGenPluggablePortMismatchClear':adGenPluggablePortMismatchClear,'adGenPluggablePortMismatchSet':adGenPluggablePortMismatchSet,'adGenPluggablePortTempClear':adGenPluggablePortTempClear,'adGenPluggablePortTempSet':adGenPluggablePortTempSet,'adGenPluggablePortProvWavelengthMismatchClear':adGenPluggablePortProvWavelengthMismatchClear,'adGenPluggablePortProvWavelengthMismatchSet':adGenPluggablePortProvWavelengthMismatchSet,'adGenPluggablePortProv':adGenPluggablePortProv,'adGenPluggablePortProvTable':adGenPluggablePortProvTable,'adGenPluggablePortProvEntry':adGenPluggablePortProvEntry,'adGenPluggablePortProvWaveLength':adGenPluggablePortProvWaveLength,'adGenPluggablePortProvChannelNumber':adGenPluggablePortProvChannelNumber,'adGenPluggableAlarmSlotProvTable':adGenPluggableAlarmSlotProvTable,'adGenPluggableAlarmSlotProvEntry':adGenPluggableAlarmSlotProvEntry,'adGenPluggableAlarmSlotTxFaultLevel':adGenPluggableAlarmSlotTxFaultLevel,'adGenPluggableAlarmSlotMissingLevel':adGenPluggableAlarmSlotMissingLevel,'adGenPluggablePortMIB':adGenPluggablePortMIB})