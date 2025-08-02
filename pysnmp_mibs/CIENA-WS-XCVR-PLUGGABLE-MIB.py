_A9='cienaWsXcvrPluggableGroup'
_A8='cwsXcvrSerdesConfigSerdesRxEmphasis'
_A7='cwsXcvrSerdesConfigSerdesRxAmplitude'
_A6='cwsXcvrSerdesConfigSerdesTxEq'
_A5='cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault'
_A4='cwsXcvrPluggableChannelDiagnosticsTransmitterFault'
_A3='cwsXcvrThresholdLowWarningThreshold'
_A2='cwsXcvrThresholdHighWarningThreshold'
_A1='cwsXcvrThresholdLowAlarmThreshold'
_A0='cwsXcvrThresholdHighAlarmThreshold'
_z='cwsXcvrStatusLowWarningStatus'
_y='cwsXcvrStatusHighWarningStatus'
_x='cwsXcvrStatusLowAlarmStatus'
_w='cwsXcvrStatusHighAlarmStatus'
_v='cwsXcvrPluggableSupplyVoltageActual'
_u='cwsXcvrPluggableOptionsAstPage01hProvided'
_t='cwsXcvrPluggableOptionsUserEepromPage02hProvided'
_s='cwsXcvrPluggableOptionsRxCdrLossOfLockFlag'
_r='cwsXcvrPluggableOptionsTxCdrLossOfLockFlag'
_q='cwsXcvrPluggableOptionsRxoutamfixedprogramsetting'
_p='cwsXcvrPluggableOptionsRxoutemfixedprogramsetting'
_o='cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting'
_n='cwsXcvrPluggableOptionsTxinpeqautoadaptcapable'
_m='cwsXcvrPluggableOptionsOptionsRaw'
_l='cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature'
_k='cwsXcvrPluggableDeviceTechnologyTransmitterTunable'
_j='cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw'
_i='cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw'
_h='cwsXcvrPluggableTransceiverCodeSpecificationCompliance'
_g='cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented'
_f='cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw'
_e='cwsXcvrPluggableVendorTransmitterEncodingRaw'
_d='cwsXcvrPluggableVendorTransmitterEncodingDescription'
_c='cwsXcvrPluggableVendorTransmitterWavelengthRaw'
_b='cwsXcvrPluggableVendorTransmitterWavelength'
_a='cwsXcvrPluggableDeviceIdConnectorTypeRaw'
_Z='cwsXcvrPluggableDeviceIdClei'
_Y='cwsXcvrPluggableDeviceIdPowerConsumption'
_X='cwsXcvrPluggableDeviceIdExtendedIdentifierRaw'
_W='cwsXcvrPluggableDeviceIdIdentifierRaw'
_V='cwsXcvrPluggableDeviceIdIdentifier'
_U='cwsXcvrPluggableVendorIdRevisionCompliance'
_T='cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry'
_S='cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry'
_R='cwsXcvrAugXcvrPluggableVendorTransmitterEntry'
_Q='cwsXcvrAugXcvrPluggableDeviceIdEntry'
_P='cwsXcvrAugXcvrPluggableVendorIdEntry'
_O='cwsXcvrPluggableSerdesConfigTableSnmpKey'
_N='cwsXcvrPluggableThresholdTableSnmpKey'
_M='cwsXcvrPluggableStatusTableSnmpKey'
_L='cwsXcvrPluggableSupplyVoltageTableSnmpKey'
_K='cwsXcvrPluggableOptionsTableSnmpKey'
_J='cwsXcvrPluggableDeviceTechnologyTableSnmpKey'
_I='cwsXcvrPluggableTransceiverCodeTableSnmpKey'
_H='cwsXcvrPluggableVendorOuiTableSnmpKey'
_G='read-write'
_F='not-accessible'
_E='cwsXcvrXcvrsXcvrIndex'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-XCVR-PLUGGABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
ChannelsNumber,Decimal2Dig,StringMaxl16,StringMaxl32,XcvrId,XcvrSerdesRxAmplitude,XcvrSerdesRxEmphasis,XcvrSerdesTxEq=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','ChannelsNumber','Decimal2Dig','StringMaxl16','StringMaxl32','XcvrId','XcvrSerdesRxAmplitude','XcvrSerdesRxEmphasis','XcvrSerdesTxEq')
cwsXcvrChannelDiagnosticsEntry,cwsXcvrDeviceIdEntry,cwsXcvrVendorDiagnosticMonitoringEntry,cwsXcvrVendorIdEntry,cwsXcvrVendorTransmitterEntry=mibBuilder.importSymbols('CIENA-WS-XCVR-MIB','cwsXcvrChannelDiagnosticsEntry','cwsXcvrDeviceIdEntry','cwsXcvrVendorDiagnosticMonitoringEntry','cwsXcvrVendorIdEntry','cwsXcvrVendorTransmitterEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsXcvrPluggableMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,17))
if mibBuilder.loadTexts:cienaWsXcvrPluggableMIB.setRevisions(('2017-07-24 00:00','2017-03-02 00:00','2016-12-12 00:00','2016-06-14 00:00','2015-02-25 00:00'))
_CienaWsXcvrPluggableObjects_ObjectIdentity=ObjectIdentity
cienaWsXcvrPluggableObjects=_CienaWsXcvrPluggableObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,17,1))
_CienaWsXcvrPluggableConformance_ObjectIdentity=ObjectIdentity
cienaWsXcvrPluggableConformance=_CienaWsXcvrPluggableConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,17,2))
_CienaWsXcvrPluggableGroups_ObjectIdentity=ObjectIdentity
cienaWsXcvrPluggableGroups=_CienaWsXcvrPluggableGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,17,2,1))
_CienaWsXcvrPluggableCompliances_ObjectIdentity=ObjectIdentity
cienaWsXcvrPluggableCompliances=_CienaWsXcvrPluggableCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,17,2,2))
_CwsXcvrAugXcvrPluggableVendorIdTable_Object=MibTable
cwsXcvrAugXcvrPluggableVendorIdTable=_CwsXcvrAugXcvrPluggableVendorIdTable_Object((1,3,6,1,4,1,1271,3,4,17,3))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorIdTable.setStatus(_A)
_CwsXcvrAugXcvrPluggableVendorIdEntry_Object=MibTableRow
cwsXcvrAugXcvrPluggableVendorIdEntry=_CwsXcvrAugXcvrPluggableVendorIdEntry_Object((1,3,6,1,4,1,1271,3,4,17,3,1))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorIdEntry.setStatus(_A)
class _CwsXcvrPluggableVendorIdRevisionCompliance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notspecified',0),('rv47',1),('rv472h',2),('rv13',3),('rv14',4),('rv15',5),('rv20',6),('rv20and26and27',7)))
_CwsXcvrPluggableVendorIdRevisionCompliance_Type.__name__=_D
_CwsXcvrPluggableVendorIdRevisionCompliance_Object=MibTableColumn
cwsXcvrPluggableVendorIdRevisionCompliance=_CwsXcvrPluggableVendorIdRevisionCompliance_Object((1,3,6,1,4,1,1271,3,4,17,3,1,1),_CwsXcvrPluggableVendorIdRevisionCompliance_Type())
cwsXcvrPluggableVendorIdRevisionCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorIdRevisionCompliance.setStatus(_A)
_CwsXcvrPluggableVendorOuiTable_Object=MibTable
cwsXcvrPluggableVendorOuiTable=_CwsXcvrPluggableVendorOuiTable_Object((1,3,6,1,4,1,1271,3,4,17,4))
if mibBuilder.loadTexts:cwsXcvrPluggableVendorOuiTable.setStatus(_A)
_CwsXcvrPluggableVendorOuiEntry_Object=MibTableRow
cwsXcvrPluggableVendorOuiEntry=_CwsXcvrPluggableVendorOuiEntry_Object((1,3,6,1,4,1,1271,3,4,17,4,1))
cwsXcvrPluggableVendorOuiEntry.setIndexNames((0,_B,_E),(0,_B,'cwsXcvrVendorIdTableSnmpKey'),(0,_B,_H))
if mibBuilder.loadTexts:cwsXcvrPluggableVendorOuiEntry.setStatus(_A)
class _CwsXcvrPluggableVendorOuiTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableVendorOuiTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableVendorOuiTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableVendorOuiTableSnmpKey=_CwsXcvrPluggableVendorOuiTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,4,1,1),_CwsXcvrPluggableVendorOuiTableSnmpKey_Type())
cwsXcvrPluggableVendorOuiTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorOuiTableSnmpKey.setStatus(_A)
_CwsXcvrPluggableVendorOui_Type=Unsigned32
_CwsXcvrPluggableVendorOui_Object=MibTableColumn
cwsXcvrPluggableVendorOui=_CwsXcvrPluggableVendorOui_Object((1,3,6,1,4,1,1271,3,4,17,4,1,2),_CwsXcvrPluggableVendorOui_Type())
cwsXcvrPluggableVendorOui.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorOui.setStatus(_A)
_CwsXcvrAugXcvrPluggableDeviceIdTable_Object=MibTable
cwsXcvrAugXcvrPluggableDeviceIdTable=_CwsXcvrAugXcvrPluggableDeviceIdTable_Object((1,3,6,1,4,1,1271,3,4,17,5))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableDeviceIdTable.setStatus(_A)
_CwsXcvrAugXcvrPluggableDeviceIdEntry_Object=MibTableRow
cwsXcvrAugXcvrPluggableDeviceIdEntry=_CwsXcvrAugXcvrPluggableDeviceIdEntry_Object((1,3,6,1,4,1,1271,3,4,17,5,1))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableDeviceIdEntry.setStatus(_A)
class _CwsXcvrPluggableDeviceIdIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,256)));namedValues=NamedValues(*(('unknownorunspecified',0),('gbic',1),('moduleconnectorsolderedtomotherboard',2),('fpsfpplussfp',3),('xbi300pin',4),('xenpak',5),('xfp',6),('xff',7),('xfpe',8),('xpak',9),('x2',10),('wdmsfporsf',11),('qsfp',12),('qsfpplus',13),('cxp',14),('shieldedminimultilanehd4x',15),('qsfp28',17),('cxp2',18),('cdfpstyle1or2',19),('shieldedminimultilanehd4xfanout',20),('shieldedminimultilanehd8xfanout',21),('cdfpstyle3',22),('wavelogic3extreme',256)))
_CwsXcvrPluggableDeviceIdIdentifier_Type.__name__=_D
_CwsXcvrPluggableDeviceIdIdentifier_Object=MibTableColumn
cwsXcvrPluggableDeviceIdIdentifier=_CwsXcvrPluggableDeviceIdIdentifier_Object((1,3,6,1,4,1,1271,3,4,17,5,1,1),_CwsXcvrPluggableDeviceIdIdentifier_Type())
cwsXcvrPluggableDeviceIdIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdIdentifier.setStatus(_A)
_CwsXcvrPluggableDeviceIdIdentifierRaw_Type=StringMaxl32
_CwsXcvrPluggableDeviceIdIdentifierRaw_Object=MibTableColumn
cwsXcvrPluggableDeviceIdIdentifierRaw=_CwsXcvrPluggableDeviceIdIdentifierRaw_Object((1,3,6,1,4,1,1271,3,4,17,5,1,2),_CwsXcvrPluggableDeviceIdIdentifierRaw_Type())
cwsXcvrPluggableDeviceIdIdentifierRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdIdentifierRaw.setStatus(_A)
_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Type=StringMaxl32
_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Object=MibTableColumn
cwsXcvrPluggableDeviceIdExtendedIdentifierRaw=_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Object((1,3,6,1,4,1,1271,3,4,17,5,1,3),_CwsXcvrPluggableDeviceIdExtendedIdentifierRaw_Type())
cwsXcvrPluggableDeviceIdExtendedIdentifierRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdExtendedIdentifierRaw.setStatus(_A)
class _CwsXcvrPluggableDeviceIdPowerConsumption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('class1module15wmax',0),('class2module20wmax',1),('class3module25wmax',2),('class4module35wmax',3)))
_CwsXcvrPluggableDeviceIdPowerConsumption_Type.__name__=_D
_CwsXcvrPluggableDeviceIdPowerConsumption_Object=MibTableColumn
cwsXcvrPluggableDeviceIdPowerConsumption=_CwsXcvrPluggableDeviceIdPowerConsumption_Object((1,3,6,1,4,1,1271,3,4,17,5,1,4),_CwsXcvrPluggableDeviceIdPowerConsumption_Type())
cwsXcvrPluggableDeviceIdPowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdPowerConsumption.setStatus(_A)
_CwsXcvrPluggableDeviceIdClei_Type=StringMaxl16
_CwsXcvrPluggableDeviceIdClei_Object=MibTableColumn
cwsXcvrPluggableDeviceIdClei=_CwsXcvrPluggableDeviceIdClei_Object((1,3,6,1,4,1,1271,3,4,17,5,1,5),_CwsXcvrPluggableDeviceIdClei_Type())
cwsXcvrPluggableDeviceIdClei.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdClei.setStatus(_A)
_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Type=StringMaxl32
_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Object=MibTableColumn
cwsXcvrPluggableDeviceIdConnectorTypeRaw=_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Object((1,3,6,1,4,1,1271,3,4,17,5,1,6),_CwsXcvrPluggableDeviceIdConnectorTypeRaw_Type())
cwsXcvrPluggableDeviceIdConnectorTypeRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceIdConnectorTypeRaw.setStatus(_A)
_CwsXcvrAugXcvrPluggableVendorTransmitterTable_Object=MibTable
cwsXcvrAugXcvrPluggableVendorTransmitterTable=_CwsXcvrAugXcvrPluggableVendorTransmitterTable_Object((1,3,6,1,4,1,1271,3,4,17,6))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorTransmitterTable.setStatus(_A)
_CwsXcvrAugXcvrPluggableVendorTransmitterEntry_Object=MibTableRow
cwsXcvrAugXcvrPluggableVendorTransmitterEntry=_CwsXcvrAugXcvrPluggableVendorTransmitterEntry_Object((1,3,6,1,4,1,1271,3,4,17,6,1))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorTransmitterEntry.setStatus(_A)
_CwsXcvrPluggableVendorTransmitterWavelength_Type=Decimal2Dig
_CwsXcvrPluggableVendorTransmitterWavelength_Object=MibTableColumn
cwsXcvrPluggableVendorTransmitterWavelength=_CwsXcvrPluggableVendorTransmitterWavelength_Object((1,3,6,1,4,1,1271,3,4,17,6,1,1),_CwsXcvrPluggableVendorTransmitterWavelength_Type())
cwsXcvrPluggableVendorTransmitterWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorTransmitterWavelength.setStatus(_A)
_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Type=StringMaxl32
_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Object=MibTableColumn
cwsXcvrPluggableVendorTransmitterWavelengthRaw=_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Object((1,3,6,1,4,1,1271,3,4,17,6,1,2),_CwsXcvrPluggableVendorTransmitterWavelengthRaw_Type())
cwsXcvrPluggableVendorTransmitterWavelengthRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorTransmitterWavelengthRaw.setStatus(_A)
class _CwsXcvrPluggableVendorTransmitterEncodingDescription_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unspecified',0),('encoding8b10b',1),('encoding4b5b',2),('nrz',3),('sonetscrambled',4),('encoding64b66b',5),('manchester',6),('encoding256b257b',7)))
_CwsXcvrPluggableVendorTransmitterEncodingDescription_Type.__name__=_D
_CwsXcvrPluggableVendorTransmitterEncodingDescription_Object=MibTableColumn
cwsXcvrPluggableVendorTransmitterEncodingDescription=_CwsXcvrPluggableVendorTransmitterEncodingDescription_Object((1,3,6,1,4,1,1271,3,4,17,6,1,3),_CwsXcvrPluggableVendorTransmitterEncodingDescription_Type())
cwsXcvrPluggableVendorTransmitterEncodingDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorTransmitterEncodingDescription.setStatus(_A)
_CwsXcvrPluggableVendorTransmitterEncodingRaw_Type=StringMaxl32
_CwsXcvrPluggableVendorTransmitterEncodingRaw_Object=MibTableColumn
cwsXcvrPluggableVendorTransmitterEncodingRaw=_CwsXcvrPluggableVendorTransmitterEncodingRaw_Object((1,3,6,1,4,1,1271,3,4,17,6,1,4),_CwsXcvrPluggableVendorTransmitterEncodingRaw_Type())
cwsXcvrPluggableVendorTransmitterEncodingRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorTransmitterEncodingRaw.setStatus(_A)
_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable_Object=MibTable
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable=_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable_Object((1,3,6,1,4,1,1271,3,4,17,7))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable.setStatus(_A)
_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry_Object=MibTableRow
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry=_CwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry_Object((1,3,6,1,4,1,1271,3,4,17,7,1))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry.setStatus(_A)
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Type=StringMaxl32
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Object=MibTableColumn
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw=_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Object((1,3,6,1,4,1,1271,3,4,17,7,1,1),_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw_Type())
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw.setStatus(_A)
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Type=TruthValue
_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Object=MibTableColumn
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented=_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Object((1,3,6,1,4,1,1271,3,4,17,7,1,2),_CwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented_Type())
cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented.setStatus(_A)
_CwsXcvrPluggableTransceiverCodeTable_Object=MibTable
cwsXcvrPluggableTransceiverCodeTable=_CwsXcvrPluggableTransceiverCodeTable_Object((1,3,6,1,4,1,1271,3,4,17,8))
if mibBuilder.loadTexts:cwsXcvrPluggableTransceiverCodeTable.setStatus(_A)
_CwsXcvrPluggableTransceiverCodeEntry_Object=MibTableRow
cwsXcvrPluggableTransceiverCodeEntry=_CwsXcvrPluggableTransceiverCodeEntry_Object((1,3,6,1,4,1,1271,3,4,17,8,1))
cwsXcvrPluggableTransceiverCodeEntry.setIndexNames((0,_B,_E),(0,_B,_I))
if mibBuilder.loadTexts:cwsXcvrPluggableTransceiverCodeEntry.setStatus(_A)
class _CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableTransceiverCodeTableSnmpKey=_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,8,1,1),_CwsXcvrPluggableTransceiverCodeTableSnmpKey_Type())
cwsXcvrPluggableTransceiverCodeTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableTransceiverCodeTableSnmpKey.setStatus(_A)
class _CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type(Bits):namedValues=NamedValues(*(('speccompliance40gactivecablexlppi',0),('speccompliance40gbaselr4',1),('speccompliance40gbasesr4',2),('speccompliance40gbasecr4',3),('speccompliance10gbasesr',4),('speccompliance10gbaselr',5),('speccompliance10gbaselrm',6),('extendedspeccompliance100gactiveopticalcable',8),('extendedspeccompliance100gbasesr4',9),('extendedspeccompliance100gbaselr4',10),('extendedspeccompliance100gbaseer4',11),('extendedspeccompliance100gbasesr10',12),('extendedspeccompliance100gcwdm4msawithfec',13),('extendedspeccompliance100gpsm4parallelsmf',14),('extendedspeccompliance100gactivecoppercable',15),('extendedspeccompliance100gcwdmmsawithoutfec',16),('extendedspeccompliance100gbasecr4',18),('extendedspeccompliance40gbaseer4',23),('extendedspeccompliance4x10gbasesr',24),('extendedspeccompliance40gpsm4parallelsmf',25),('extendedspeccomplianceg9591p1i12d1',26),('extendedspeccomplianceg9591p1s12d2',27),('extendedspeccomplianceg9591p1l12d2',28),('extspeccode10gbasetwithsfi',29),('unknown',30)))
_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type.__name__='Bits'
_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Object=MibTableColumn
cwsXcvrPluggableTransceiverCodeSpecificationCompliance=_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Object((1,3,6,1,4,1,1271,3,4,17,8,1,2),_CwsXcvrPluggableTransceiverCodeSpecificationCompliance_Type())
cwsXcvrPluggableTransceiverCodeSpecificationCompliance.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrPluggableTransceiverCodeSpecificationCompliance.setStatus(_A)
_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Type=StringMaxl32
_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Object=MibTableColumn
cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw=_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Object((1,3,6,1,4,1,1271,3,4,17,8,1,3),_CwsXcvrPluggableTransceiverCodeTransceiverCodeRaw_Type())
cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw.setStatus(_A)
_CwsXcvrPluggableDeviceTechnologyTable_Object=MibTable
cwsXcvrPluggableDeviceTechnologyTable=_CwsXcvrPluggableDeviceTechnologyTable_Object((1,3,6,1,4,1,1271,3,4,17,9))
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyTable.setStatus(_A)
_CwsXcvrPluggableDeviceTechnologyEntry_Object=MibTableRow
cwsXcvrPluggableDeviceTechnologyEntry=_CwsXcvrPluggableDeviceTechnologyEntry_Object((1,3,6,1,4,1,1271,3,4,17,9,1))
cwsXcvrPluggableDeviceTechnologyEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyEntry.setStatus(_A)
class _CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableDeviceTechnologyTableSnmpKey=_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,9,1,1),_CwsXcvrPluggableDeviceTechnologyTableSnmpKey_Type())
cwsXcvrPluggableDeviceTechnologyTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyTableSnmpKey.setStatus(_A)
_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Type=StringMaxl32
_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Object=MibTableColumn
cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw=_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Object((1,3,6,1,4,1,1271,3,4,17,9,1,2),_CwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw_Type())
cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw.setStatus(_A)
_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Type=TruthValue
_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Object=MibTableColumn
cwsXcvrPluggableDeviceTechnologyTransmitterTunable=_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Object((1,3,6,1,4,1,1271,3,4,17,9,1,3),_CwsXcvrPluggableDeviceTechnologyTransmitterTunable_Type())
cwsXcvrPluggableDeviceTechnologyTransmitterTunable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyTransmitterTunable.setStatus(_A)
_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Type=Unsigned32
_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Object=MibTableColumn
cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature=_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Object((1,3,6,1,4,1,1271,3,4,17,9,1,4),_CwsXcvrPluggableDeviceTechnologyMaxCaseTemperature_Type())
cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature.setStatus(_A)
_CwsXcvrPluggableOptionsTable_Object=MibTable
cwsXcvrPluggableOptionsTable=_CwsXcvrPluggableOptionsTable_Object((1,3,6,1,4,1,1271,3,4,17,10))
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsTable.setStatus(_A)
_CwsXcvrPluggableOptionsEntry_Object=MibTableRow
cwsXcvrPluggableOptionsEntry=_CwsXcvrPluggableOptionsEntry_Object((1,3,6,1,4,1,1271,3,4,17,10,1))
cwsXcvrPluggableOptionsEntry.setIndexNames((0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsEntry.setStatus(_A)
class _CwsXcvrPluggableOptionsTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableOptionsTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableOptionsTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableOptionsTableSnmpKey=_CwsXcvrPluggableOptionsTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,10,1,1),_CwsXcvrPluggableOptionsTableSnmpKey_Type())
cwsXcvrPluggableOptionsTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsTableSnmpKey.setStatus(_A)
_CwsXcvrPluggableOptionsOptionsRaw_Type=StringMaxl32
_CwsXcvrPluggableOptionsOptionsRaw_Object=MibTableColumn
cwsXcvrPluggableOptionsOptionsRaw=_CwsXcvrPluggableOptionsOptionsRaw_Object((1,3,6,1,4,1,1271,3,4,17,10,1,2),_CwsXcvrPluggableOptionsOptionsRaw_Type())
cwsXcvrPluggableOptionsOptionsRaw.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsOptionsRaw.setStatus(_A)
_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Type=TruthValue
_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Object=MibTableColumn
cwsXcvrPluggableOptionsTxinpeqautoadaptcapable=_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Object((1,3,6,1,4,1,1271,3,4,17,10,1,3),_CwsXcvrPluggableOptionsTxinpeqautoadaptcapable_Type())
cwsXcvrPluggableOptionsTxinpeqautoadaptcapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsTxinpeqautoadaptcapable.setStatus(_A)
_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Type=TruthValue
_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Object=MibTableColumn
cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting=_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Object((1,3,6,1,4,1,1271,3,4,17,10,1,4),_CwsXcvrPluggableOptionsTxinpeqfixedprogramsetting_Type())
cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting.setStatus(_A)
_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Type=TruthValue
_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Object=MibTableColumn
cwsXcvrPluggableOptionsRxoutemfixedprogramsetting=_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Object((1,3,6,1,4,1,1271,3,4,17,10,1,5),_CwsXcvrPluggableOptionsRxoutemfixedprogramsetting_Type())
cwsXcvrPluggableOptionsRxoutemfixedprogramsetting.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsRxoutemfixedprogramsetting.setStatus(_A)
_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Type=TruthValue
_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Object=MibTableColumn
cwsXcvrPluggableOptionsRxoutamfixedprogramsetting=_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Object((1,3,6,1,4,1,1271,3,4,17,10,1,6),_CwsXcvrPluggableOptionsRxoutamfixedprogramsetting_Type())
cwsXcvrPluggableOptionsRxoutamfixedprogramsetting.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsRxoutamfixedprogramsetting.setStatus(_A)
_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Type=TruthValue
_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Object=MibTableColumn
cwsXcvrPluggableOptionsTxCdrLossOfLockFlag=_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Object((1,3,6,1,4,1,1271,3,4,17,10,1,7),_CwsXcvrPluggableOptionsTxCdrLossOfLockFlag_Type())
cwsXcvrPluggableOptionsTxCdrLossOfLockFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsTxCdrLossOfLockFlag.setStatus(_A)
_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Type=TruthValue
_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Object=MibTableColumn
cwsXcvrPluggableOptionsRxCdrLossOfLockFlag=_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Object((1,3,6,1,4,1,1271,3,4,17,10,1,8),_CwsXcvrPluggableOptionsRxCdrLossOfLockFlag_Type())
cwsXcvrPluggableOptionsRxCdrLossOfLockFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsRxCdrLossOfLockFlag.setStatus(_A)
_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Type=TruthValue
_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Object=MibTableColumn
cwsXcvrPluggableOptionsUserEepromPage02hProvided=_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Object((1,3,6,1,4,1,1271,3,4,17,10,1,9),_CwsXcvrPluggableOptionsUserEepromPage02hProvided_Type())
cwsXcvrPluggableOptionsUserEepromPage02hProvided.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsUserEepromPage02hProvided.setStatus(_A)
_CwsXcvrPluggableOptionsAstPage01hProvided_Type=TruthValue
_CwsXcvrPluggableOptionsAstPage01hProvided_Object=MibTableColumn
cwsXcvrPluggableOptionsAstPage01hProvided=_CwsXcvrPluggableOptionsAstPage01hProvided_Object((1,3,6,1,4,1,1271,3,4,17,10,1,10),_CwsXcvrPluggableOptionsAstPage01hProvided_Type())
cwsXcvrPluggableOptionsAstPage01hProvided.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableOptionsAstPage01hProvided.setStatus(_A)
_CwsXcvrPluggableSupplyVoltageTable_Object=MibTable
cwsXcvrPluggableSupplyVoltageTable=_CwsXcvrPluggableSupplyVoltageTable_Object((1,3,6,1,4,1,1271,3,4,17,11))
if mibBuilder.loadTexts:cwsXcvrPluggableSupplyVoltageTable.setStatus(_A)
_CwsXcvrPluggableSupplyVoltageEntry_Object=MibTableRow
cwsXcvrPluggableSupplyVoltageEntry=_CwsXcvrPluggableSupplyVoltageEntry_Object((1,3,6,1,4,1,1271,3,4,17,11,1))
cwsXcvrPluggableSupplyVoltageEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:cwsXcvrPluggableSupplyVoltageEntry.setStatus(_A)
class _CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableSupplyVoltageTableSnmpKey=_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,11,1,1),_CwsXcvrPluggableSupplyVoltageTableSnmpKey_Type())
cwsXcvrPluggableSupplyVoltageTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableSupplyVoltageTableSnmpKey.setStatus(_A)
_CwsXcvrPluggableSupplyVoltageActual_Type=Decimal2Dig
_CwsXcvrPluggableSupplyVoltageActual_Object=MibTableColumn
cwsXcvrPluggableSupplyVoltageActual=_CwsXcvrPluggableSupplyVoltageActual_Object((1,3,6,1,4,1,1271,3,4,17,11,1,2),_CwsXcvrPluggableSupplyVoltageActual_Type())
cwsXcvrPluggableSupplyVoltageActual.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableSupplyVoltageActual.setStatus(_A)
_CwsXcvrPluggableStatusTable_Object=MibTable
cwsXcvrPluggableStatusTable=_CwsXcvrPluggableStatusTable_Object((1,3,6,1,4,1,1271,3,4,17,12))
if mibBuilder.loadTexts:cwsXcvrPluggableStatusTable.setStatus(_A)
_CwsXcvrPluggableStatusEntry_Object=MibTableRow
cwsXcvrPluggableStatusEntry=_CwsXcvrPluggableStatusEntry_Object((1,3,6,1,4,1,1271,3,4,17,12,1))
cwsXcvrPluggableStatusEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:cwsXcvrPluggableStatusEntry.setStatus(_A)
class _CwsXcvrPluggableStatusTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableStatusTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableStatusTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableStatusTableSnmpKey=_CwsXcvrPluggableStatusTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,12,1,1),_CwsXcvrPluggableStatusTableSnmpKey_Type())
cwsXcvrPluggableStatusTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableStatusTableSnmpKey.setStatus(_A)
_CwsXcvrStatusHighAlarmStatus_Type=TruthValue
_CwsXcvrStatusHighAlarmStatus_Object=MibTableColumn
cwsXcvrStatusHighAlarmStatus=_CwsXcvrStatusHighAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,17,12,1,2),_CwsXcvrStatusHighAlarmStatus_Type())
cwsXcvrStatusHighAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrStatusHighAlarmStatus.setStatus(_A)
_CwsXcvrStatusLowAlarmStatus_Type=TruthValue
_CwsXcvrStatusLowAlarmStatus_Object=MibTableColumn
cwsXcvrStatusLowAlarmStatus=_CwsXcvrStatusLowAlarmStatus_Object((1,3,6,1,4,1,1271,3,4,17,12,1,3),_CwsXcvrStatusLowAlarmStatus_Type())
cwsXcvrStatusLowAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrStatusLowAlarmStatus.setStatus(_A)
_CwsXcvrStatusHighWarningStatus_Type=TruthValue
_CwsXcvrStatusHighWarningStatus_Object=MibTableColumn
cwsXcvrStatusHighWarningStatus=_CwsXcvrStatusHighWarningStatus_Object((1,3,6,1,4,1,1271,3,4,17,12,1,4),_CwsXcvrStatusHighWarningStatus_Type())
cwsXcvrStatusHighWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrStatusHighWarningStatus.setStatus(_A)
_CwsXcvrStatusLowWarningStatus_Type=TruthValue
_CwsXcvrStatusLowWarningStatus_Object=MibTableColumn
cwsXcvrStatusLowWarningStatus=_CwsXcvrStatusLowWarningStatus_Object((1,3,6,1,4,1,1271,3,4,17,12,1,5),_CwsXcvrStatusLowWarningStatus_Type())
cwsXcvrStatusLowWarningStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrStatusLowWarningStatus.setStatus(_A)
_CwsXcvrPluggableThresholdTable_Object=MibTable
cwsXcvrPluggableThresholdTable=_CwsXcvrPluggableThresholdTable_Object((1,3,6,1,4,1,1271,3,4,17,13))
if mibBuilder.loadTexts:cwsXcvrPluggableThresholdTable.setStatus(_A)
_CwsXcvrPluggableThresholdEntry_Object=MibTableRow
cwsXcvrPluggableThresholdEntry=_CwsXcvrPluggableThresholdEntry_Object((1,3,6,1,4,1,1271,3,4,17,13,1))
cwsXcvrPluggableThresholdEntry.setIndexNames((0,_B,_E),(0,_B,_N))
if mibBuilder.loadTexts:cwsXcvrPluggableThresholdEntry.setStatus(_A)
class _CwsXcvrPluggableThresholdTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableThresholdTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableThresholdTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableThresholdTableSnmpKey=_CwsXcvrPluggableThresholdTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,13,1,1),_CwsXcvrPluggableThresholdTableSnmpKey_Type())
cwsXcvrPluggableThresholdTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableThresholdTableSnmpKey.setStatus(_A)
_CwsXcvrThresholdHighAlarmThreshold_Type=Decimal2Dig
_CwsXcvrThresholdHighAlarmThreshold_Object=MibTableColumn
cwsXcvrThresholdHighAlarmThreshold=_CwsXcvrThresholdHighAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,17,13,1,2),_CwsXcvrThresholdHighAlarmThreshold_Type())
cwsXcvrThresholdHighAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrThresholdHighAlarmThreshold.setStatus(_A)
_CwsXcvrThresholdLowAlarmThreshold_Type=Decimal2Dig
_CwsXcvrThresholdLowAlarmThreshold_Object=MibTableColumn
cwsXcvrThresholdLowAlarmThreshold=_CwsXcvrThresholdLowAlarmThreshold_Object((1,3,6,1,4,1,1271,3,4,17,13,1,3),_CwsXcvrThresholdLowAlarmThreshold_Type())
cwsXcvrThresholdLowAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrThresholdLowAlarmThreshold.setStatus(_A)
_CwsXcvrThresholdHighWarningThreshold_Type=Decimal2Dig
_CwsXcvrThresholdHighWarningThreshold_Object=MibTableColumn
cwsXcvrThresholdHighWarningThreshold=_CwsXcvrThresholdHighWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,17,13,1,4),_CwsXcvrThresholdHighWarningThreshold_Type())
cwsXcvrThresholdHighWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrThresholdHighWarningThreshold.setStatus(_A)
_CwsXcvrThresholdLowWarningThreshold_Type=Decimal2Dig
_CwsXcvrThresholdLowWarningThreshold_Object=MibTableColumn
cwsXcvrThresholdLowWarningThreshold=_CwsXcvrThresholdLowWarningThreshold_Object((1,3,6,1,4,1,1271,3,4,17,13,1,5),_CwsXcvrThresholdLowWarningThreshold_Type())
cwsXcvrThresholdLowWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrThresholdLowWarningThreshold.setStatus(_A)
_CwsXcvrAugXcvrPluggableChannelDiagnosticsTable_Object=MibTable
cwsXcvrAugXcvrPluggableChannelDiagnosticsTable=_CwsXcvrAugXcvrPluggableChannelDiagnosticsTable_Object((1,3,6,1,4,1,1271,3,4,17,14))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableChannelDiagnosticsTable.setStatus(_A)
_CwsXcvrAugXcvrPluggableChannelDiagnosticsEntry_Object=MibTableRow
cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry=_CwsXcvrAugXcvrPluggableChannelDiagnosticsEntry_Object((1,3,6,1,4,1,1271,3,4,17,14,1))
if mibBuilder.loadTexts:cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry.setStatus(_A)
_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Type=TruthValue
_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Object=MibTableColumn
cwsXcvrPluggableChannelDiagnosticsTransmitterFault=_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Object((1,3,6,1,4,1,1271,3,4,17,14,1,1),_CwsXcvrPluggableChannelDiagnosticsTransmitterFault_Type())
cwsXcvrPluggableChannelDiagnosticsTransmitterFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableChannelDiagnosticsTransmitterFault.setStatus(_A)
_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Type=TruthValue
_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Object=MibTableColumn
cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault=_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Object((1,3,6,1,4,1,1271,3,4,17,14,1,2),_CwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault_Type())
cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault.setStatus(_A)
_CwsXcvrPluggableSerdesConfigTable_Object=MibTable
cwsXcvrPluggableSerdesConfigTable=_CwsXcvrPluggableSerdesConfigTable_Object((1,3,6,1,4,1,1271,3,4,17,15))
if mibBuilder.loadTexts:cwsXcvrPluggableSerdesConfigTable.setStatus(_A)
_CwsXcvrPluggableSerdesConfigEntry_Object=MibTableRow
cwsXcvrPluggableSerdesConfigEntry=_CwsXcvrPluggableSerdesConfigEntry_Object((1,3,6,1,4,1,1271,3,4,17,15,1))
cwsXcvrPluggableSerdesConfigEntry.setIndexNames((0,_B,_E),(0,_B,_O))
if mibBuilder.loadTexts:cwsXcvrPluggableSerdesConfigEntry.setStatus(_A)
class _CwsXcvrPluggableSerdesConfigTableSnmpKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsXcvrPluggableSerdesConfigTableSnmpKey_Type.__name__=_D
_CwsXcvrPluggableSerdesConfigTableSnmpKey_Object=MibTableColumn
cwsXcvrPluggableSerdesConfigTableSnmpKey=_CwsXcvrPluggableSerdesConfigTableSnmpKey_Object((1,3,6,1,4,1,1271,3,4,17,15,1,1),_CwsXcvrPluggableSerdesConfigTableSnmpKey_Type())
cwsXcvrPluggableSerdesConfigTableSnmpKey.setMaxAccess(_F)
if mibBuilder.loadTexts:cwsXcvrPluggableSerdesConfigTableSnmpKey.setStatus(_A)
_CwsXcvrSerdesConfigSerdesTxEq_Type=XcvrSerdesTxEq
_CwsXcvrSerdesConfigSerdesTxEq_Object=MibTableColumn
cwsXcvrSerdesConfigSerdesTxEq=_CwsXcvrSerdesConfigSerdesTxEq_Object((1,3,6,1,4,1,1271,3,4,17,15,1,2),_CwsXcvrSerdesConfigSerdesTxEq_Type())
cwsXcvrSerdesConfigSerdesTxEq.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrSerdesConfigSerdesTxEq.setStatus(_A)
_CwsXcvrSerdesConfigSerdesRxAmplitude_Type=XcvrSerdesRxAmplitude
_CwsXcvrSerdesConfigSerdesRxAmplitude_Object=MibTableColumn
cwsXcvrSerdesConfigSerdesRxAmplitude=_CwsXcvrSerdesConfigSerdesRxAmplitude_Object((1,3,6,1,4,1,1271,3,4,17,15,1,3),_CwsXcvrSerdesConfigSerdesRxAmplitude_Type())
cwsXcvrSerdesConfigSerdesRxAmplitude.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrSerdesConfigSerdesRxAmplitude.setStatus(_A)
_CwsXcvrSerdesConfigSerdesRxEmphasis_Type=XcvrSerdesRxEmphasis
_CwsXcvrSerdesConfigSerdesRxEmphasis_Object=MibTableColumn
cwsXcvrSerdesConfigSerdesRxEmphasis=_CwsXcvrSerdesConfigSerdesRxEmphasis_Object((1,3,6,1,4,1,1271,3,4,17,15,1,4),_CwsXcvrSerdesConfigSerdesRxEmphasis_Type())
cwsXcvrSerdesConfigSerdesRxEmphasis.setMaxAccess(_G)
if mibBuilder.loadTexts:cwsXcvrSerdesConfigSerdesRxEmphasis.setStatus(_A)
cwsXcvrVendorIdEntry.registerAugmentions((_B,_P))
cwsXcvrAugXcvrPluggableVendorIdEntry.setIndexNames(*cwsXcvrVendorIdEntry.getIndexNames())
cwsXcvrDeviceIdEntry.registerAugmentions((_B,_Q))
cwsXcvrAugXcvrPluggableDeviceIdEntry.setIndexNames(*cwsXcvrDeviceIdEntry.getIndexNames())
cwsXcvrVendorTransmitterEntry.registerAugmentions((_B,_R))
cwsXcvrAugXcvrPluggableVendorTransmitterEntry.setIndexNames(*cwsXcvrVendorTransmitterEntry.getIndexNames())
cwsXcvrVendorDiagnosticMonitoringEntry.registerAugmentions((_B,_S))
cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry.setIndexNames(*cwsXcvrVendorDiagnosticMonitoringEntry.getIndexNames())
cwsXcvrChannelDiagnosticsEntry.registerAugmentions((_B,_T))
cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry.setIndexNames(*cwsXcvrChannelDiagnosticsEntry.getIndexNames())
cienaWsXcvrPluggableGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,17,2,1,1))
cienaWsXcvrPluggableGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cienaWsXcvrPluggableGroup.setStatus(_A)
cienaWsXcvrPluggableCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,17,2,2,1))
cienaWsXcvrPluggableCompliance.setObjects((_B,_A9))
if mibBuilder.loadTexts:cienaWsXcvrPluggableCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cienaWsXcvrPluggableMIB':cienaWsXcvrPluggableMIB,'cienaWsXcvrPluggableObjects':cienaWsXcvrPluggableObjects,'cienaWsXcvrPluggableConformance':cienaWsXcvrPluggableConformance,'cienaWsXcvrPluggableGroups':cienaWsXcvrPluggableGroups,_A9:cienaWsXcvrPluggableGroup,'cienaWsXcvrPluggableCompliances':cienaWsXcvrPluggableCompliances,'cienaWsXcvrPluggableCompliance':cienaWsXcvrPluggableCompliance,'cwsXcvrAugXcvrPluggableVendorIdTable':cwsXcvrAugXcvrPluggableVendorIdTable,_P:cwsXcvrAugXcvrPluggableVendorIdEntry,_U:cwsXcvrPluggableVendorIdRevisionCompliance,'cwsXcvrPluggableVendorOuiTable':cwsXcvrPluggableVendorOuiTable,'cwsXcvrPluggableVendorOuiEntry':cwsXcvrPluggableVendorOuiEntry,_H:cwsXcvrPluggableVendorOuiTableSnmpKey,'cwsXcvrPluggableVendorOui':cwsXcvrPluggableVendorOui,'cwsXcvrAugXcvrPluggableDeviceIdTable':cwsXcvrAugXcvrPluggableDeviceIdTable,_Q:cwsXcvrAugXcvrPluggableDeviceIdEntry,_V:cwsXcvrPluggableDeviceIdIdentifier,_W:cwsXcvrPluggableDeviceIdIdentifierRaw,_X:cwsXcvrPluggableDeviceIdExtendedIdentifierRaw,_Y:cwsXcvrPluggableDeviceIdPowerConsumption,_Z:cwsXcvrPluggableDeviceIdClei,_a:cwsXcvrPluggableDeviceIdConnectorTypeRaw,'cwsXcvrAugXcvrPluggableVendorTransmitterTable':cwsXcvrAugXcvrPluggableVendorTransmitterTable,_R:cwsXcvrAugXcvrPluggableVendorTransmitterEntry,_b:cwsXcvrPluggableVendorTransmitterWavelength,_c:cwsXcvrPluggableVendorTransmitterWavelengthRaw,_d:cwsXcvrPluggableVendorTransmitterEncodingDescription,_e:cwsXcvrPluggableVendorTransmitterEncodingRaw,'cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable':cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringTable,_S:cwsXcvrAugXcvrPluggableVendorDiagnosticMonitoringEntry,_f:cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringTypeRaw,_g:cwsXcvrPluggableVendorDiagnosticMonitoringDiagnosticMonitoringImplemented,'cwsXcvrPluggableTransceiverCodeTable':cwsXcvrPluggableTransceiverCodeTable,'cwsXcvrPluggableTransceiverCodeEntry':cwsXcvrPluggableTransceiverCodeEntry,_I:cwsXcvrPluggableTransceiverCodeTableSnmpKey,_h:cwsXcvrPluggableTransceiverCodeSpecificationCompliance,_i:cwsXcvrPluggableTransceiverCodeTransceiverCodeRaw,'cwsXcvrPluggableDeviceTechnologyTable':cwsXcvrPluggableDeviceTechnologyTable,'cwsXcvrPluggableDeviceTechnologyEntry':cwsXcvrPluggableDeviceTechnologyEntry,_J:cwsXcvrPluggableDeviceTechnologyTableSnmpKey,_j:cwsXcvrPluggableDeviceTechnologyDeviceTechnologyRaw,_k:cwsXcvrPluggableDeviceTechnologyTransmitterTunable,_l:cwsXcvrPluggableDeviceTechnologyMaxCaseTemperature,'cwsXcvrPluggableOptionsTable':cwsXcvrPluggableOptionsTable,'cwsXcvrPluggableOptionsEntry':cwsXcvrPluggableOptionsEntry,_K:cwsXcvrPluggableOptionsTableSnmpKey,_m:cwsXcvrPluggableOptionsOptionsRaw,_n:cwsXcvrPluggableOptionsTxinpeqautoadaptcapable,_o:cwsXcvrPluggableOptionsTxinpeqfixedprogramsetting,_p:cwsXcvrPluggableOptionsRxoutemfixedprogramsetting,_q:cwsXcvrPluggableOptionsRxoutamfixedprogramsetting,_r:cwsXcvrPluggableOptionsTxCdrLossOfLockFlag,_s:cwsXcvrPluggableOptionsRxCdrLossOfLockFlag,_t:cwsXcvrPluggableOptionsUserEepromPage02hProvided,_u:cwsXcvrPluggableOptionsAstPage01hProvided,'cwsXcvrPluggableSupplyVoltageTable':cwsXcvrPluggableSupplyVoltageTable,'cwsXcvrPluggableSupplyVoltageEntry':cwsXcvrPluggableSupplyVoltageEntry,_L:cwsXcvrPluggableSupplyVoltageTableSnmpKey,_v:cwsXcvrPluggableSupplyVoltageActual,'cwsXcvrPluggableStatusTable':cwsXcvrPluggableStatusTable,'cwsXcvrPluggableStatusEntry':cwsXcvrPluggableStatusEntry,_M:cwsXcvrPluggableStatusTableSnmpKey,_w:cwsXcvrStatusHighAlarmStatus,_x:cwsXcvrStatusLowAlarmStatus,_y:cwsXcvrStatusHighWarningStatus,_z:cwsXcvrStatusLowWarningStatus,'cwsXcvrPluggableThresholdTable':cwsXcvrPluggableThresholdTable,'cwsXcvrPluggableThresholdEntry':cwsXcvrPluggableThresholdEntry,_N:cwsXcvrPluggableThresholdTableSnmpKey,_A0:cwsXcvrThresholdHighAlarmThreshold,_A1:cwsXcvrThresholdLowAlarmThreshold,_A2:cwsXcvrThresholdHighWarningThreshold,_A3:cwsXcvrThresholdLowWarningThreshold,'cwsXcvrAugXcvrPluggableChannelDiagnosticsTable':cwsXcvrAugXcvrPluggableChannelDiagnosticsTable,_T:cwsXcvrAugXcvrPluggableChannelDiagnosticsEntry,_A4:cwsXcvrPluggableChannelDiagnosticsTransmitterFault,_A5:cwsXcvrPluggableChannelDiagnosticsTxAdaptiveEqFault,'cwsXcvrPluggableSerdesConfigTable':cwsXcvrPluggableSerdesConfigTable,'cwsXcvrPluggableSerdesConfigEntry':cwsXcvrPluggableSerdesConfigEntry,_O:cwsXcvrPluggableSerdesConfigTableSnmpKey,_A6:cwsXcvrSerdesConfigSerdesTxEq,_A7:cwsXcvrSerdesConfigSerdesRxAmplitude,_A8:cwsXcvrSerdesConfigSerdesRxEmphasis})