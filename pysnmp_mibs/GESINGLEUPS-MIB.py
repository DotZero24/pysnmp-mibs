_e='upsOutputPercentLoadgen'
_d='upsOutputNumLinesgen'
_c='upsBatteryTemperaturegen'
_b='upsSecondsOnBatterygen'
_a='upsParameterLineIndexgen'
_Z='upsEventLineIndexgen'
_Y='enabled'
_X='disabled'
_W='upsReceptacleLineIndexgen'
_V='upsAlarmIdgen'
_U='upsBypassLineIndexgen'
_T='upsOutputLineIndexgen'
_S='upsInputLineIndexgen'
_R='0.1 Amp DC'
_Q='percent'
_P='upsTestIdgen'
_O='upsShutdownAfterDelaygen'
_N='0.1 RMS Amp'
_M='minutes'
_L='Watts'
_K='off'
_J='on'
_I='0.1 Hertz'
_H='seconds'
_G='not-accessible'
_F='RMS Volts'
_E='GESINGLEUPS-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
imv=ModuleIdentity((1,3,6,1,4,1,818))
if mibBuilder.loadTexts:imv.setRevisions(('2010-07-05 00:00','2008-01-08 00:00'))
class PositiveInteger32(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NonNegativeInteger32(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_GeHardware_ObjectIdentity=ObjectIdentity
geHardware=_GeHardware_ObjectIdentity((1,3,6,1,4,1,818,1))
_GeUPS_ObjectIdentity=ObjectIdentity
geUPS=_GeUPS_ObjectIdentity((1,3,6,1,4,1,818,1,1))
_GeDiscoveredUPSsMask_Type=Integer32
_GeDiscoveredUPSsMask_Object=MibScalar
geDiscoveredUPSsMask=_GeDiscoveredUPSsMask_Object((1,3,6,1,4,1,818,1,1,1),_GeDiscoveredUPSsMask_Type())
geDiscoveredUPSsMask.setMaxAccess(_B)
if mibBuilder.loadTexts:geDiscoveredUPSsMask.setStatus(_A)
_GeRequestPacket_Type=DisplayString
_GeRequestPacket_Object=MibScalar
geRequestPacket=_GeRequestPacket_Object((1,3,6,1,4,1,818,1,1,2),_GeRequestPacket_Type())
geRequestPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:geRequestPacket.setStatus(_A)
_GeReplyPacket_Type=DisplayString
_GeReplyPacket_Object=MibScalar
geReplyPacket=_GeReplyPacket_Object((1,3,6,1,4,1,818,1,1,3),_GeReplyPacket_Type())
geReplyPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:geReplyPacket.setStatus(_A)
_GeGenericUPS_ObjectIdentity=ObjectIdentity
geGenericUPS=_GeGenericUPS_ObjectIdentity((1,3,6,1,4,1,818,1,1,10))
_UpsIdentgen_ObjectIdentity=ObjectIdentity
upsIdentgen=_UpsIdentgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,1))
_UpsIdentManufacturergen_Type=DisplayString
_UpsIdentManufacturergen_Object=MibScalar
upsIdentManufacturergen=_UpsIdentManufacturergen_Object((1,3,6,1,4,1,818,1,1,10,1,1),_UpsIdentManufacturergen_Type())
upsIdentManufacturergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentManufacturergen.setStatus(_A)
_UpsIdentModelgen_Type=DisplayString
_UpsIdentModelgen_Object=MibScalar
upsIdentModelgen=_UpsIdentModelgen_Object((1,3,6,1,4,1,818,1,1,10,1,2),_UpsIdentModelgen_Type())
upsIdentModelgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentModelgen.setStatus(_A)
_UpsIdentUPSSoftwareVersiongen_Type=DisplayString
_UpsIdentUPSSoftwareVersiongen_Object=MibScalar
upsIdentUPSSoftwareVersiongen=_UpsIdentUPSSoftwareVersiongen_Object((1,3,6,1,4,1,818,1,1,10,1,3),_UpsIdentUPSSoftwareVersiongen_Type())
upsIdentUPSSoftwareVersiongen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUPSSoftwareVersiongen.setStatus(_A)
_UpsIdentAgentSoftwareVersiongen_Type=DisplayString
_UpsIdentAgentSoftwareVersiongen_Object=MibScalar
upsIdentAgentSoftwareVersiongen=_UpsIdentAgentSoftwareVersiongen_Object((1,3,6,1,4,1,818,1,1,10,1,4),_UpsIdentAgentSoftwareVersiongen_Type())
upsIdentAgentSoftwareVersiongen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentAgentSoftwareVersiongen.setStatus(_A)
_UpsIdentNamegen_Type=DisplayString
_UpsIdentNamegen_Object=MibScalar
upsIdentNamegen=_UpsIdentNamegen_Object((1,3,6,1,4,1,818,1,1,10,1,5),_UpsIdentNamegen_Type())
upsIdentNamegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentNamegen.setStatus(_A)
_UpsIdentAttachedDevicesgen_Type=DisplayString
_UpsIdentAttachedDevicesgen_Object=MibScalar
upsIdentAttachedDevicesgen=_UpsIdentAttachedDevicesgen_Object((1,3,6,1,4,1,818,1,1,10,1,6),_UpsIdentAttachedDevicesgen_Type())
upsIdentAttachedDevicesgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsIdentAttachedDevicesgen.setStatus(_A)
_UpsIdentUPSSerialNumbergen_Type=DisplayString
_UpsIdentUPSSerialNumbergen_Object=MibScalar
upsIdentUPSSerialNumbergen=_UpsIdentUPSSerialNumbergen_Object((1,3,6,1,4,1,818,1,1,10,1,7),_UpsIdentUPSSerialNumbergen_Type())
upsIdentUPSSerialNumbergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentUPSSerialNumbergen.setStatus(_A)
_UpsIdentComProtVersiongen_Type=DisplayString
_UpsIdentComProtVersiongen_Object=MibScalar
upsIdentComProtVersiongen=_UpsIdentComProtVersiongen_Object((1,3,6,1,4,1,818,1,1,10,1,8),_UpsIdentComProtVersiongen_Type())
upsIdentComProtVersiongen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentComProtVersiongen.setStatus(_A)
_UpsIdentOperatingTimegen_Type=NonNegativeInteger32
_UpsIdentOperatingTimegen_Object=MibScalar
upsIdentOperatingTimegen=_UpsIdentOperatingTimegen_Object((1,3,6,1,4,1,818,1,1,10,1,9),_UpsIdentOperatingTimegen_Type())
upsIdentOperatingTimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsIdentOperatingTimegen.setStatus(_A)
if mibBuilder.loadTexts:upsIdentOperatingTimegen.setUnits(_H)
_UpsBatterygen_ObjectIdentity=ObjectIdentity
upsBatterygen=_UpsBatterygen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,2))
class _UpsBatteryStatusgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_UpsBatteryStatusgen_Type.__name__=_D
_UpsBatteryStatusgen_Object=MibScalar
upsBatteryStatusgen=_UpsBatteryStatusgen_Object((1,3,6,1,4,1,818,1,1,10,2,1),_UpsBatteryStatusgen_Type())
upsBatteryStatusgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryStatusgen.setStatus(_A)
_UpsSecondsOnBatterygen_Type=Integer32
_UpsSecondsOnBatterygen_Object=MibScalar
upsSecondsOnBatterygen=_UpsSecondsOnBatterygen_Object((1,3,6,1,4,1,818,1,1,10,2,2),_UpsSecondsOnBatterygen_Type())
upsSecondsOnBatterygen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsSecondsOnBatterygen.setStatus(_A)
if mibBuilder.loadTexts:upsSecondsOnBatterygen.setUnits(_H)
_UpsEstimatedMinutesRemaininggen_Type=PositiveInteger32
_UpsEstimatedMinutesRemaininggen_Object=MibScalar
upsEstimatedMinutesRemaininggen=_UpsEstimatedMinutesRemaininggen_Object((1,3,6,1,4,1,818,1,1,10,2,3),_UpsEstimatedMinutesRemaininggen_Type())
upsEstimatedMinutesRemaininggen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaininggen.setStatus(_A)
if mibBuilder.loadTexts:upsEstimatedMinutesRemaininggen.setUnits(_M)
class _UpsEstimatedChargeRemaininggen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_UpsEstimatedChargeRemaininggen_Type.__name__=_D
_UpsEstimatedChargeRemaininggen_Object=MibScalar
upsEstimatedChargeRemaininggen=_UpsEstimatedChargeRemaininggen_Object((1,3,6,1,4,1,818,1,1,10,2,4),_UpsEstimatedChargeRemaininggen_Type())
upsEstimatedChargeRemaininggen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEstimatedChargeRemaininggen.setStatus(_A)
if mibBuilder.loadTexts:upsEstimatedChargeRemaininggen.setUnits(_Q)
_UpsBatteryVoltagegen_Type=NonNegativeInteger32
_UpsBatteryVoltagegen_Object=MibScalar
upsBatteryVoltagegen=_UpsBatteryVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,2,5),_UpsBatteryVoltagegen_Type())
upsBatteryVoltagegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryVoltagegen.setUnits('0.1 Volt DC')
_UpsBatteryCurrentgen_Type=Integer32
_UpsBatteryCurrentgen_Object=MibScalar
upsBatteryCurrentgen=_UpsBatteryCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,2,6),_UpsBatteryCurrentgen_Type())
upsBatteryCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryCurrentgen.setUnits(_R)
_UpsBatteryTemperaturegen_Type=Integer32
_UpsBatteryTemperaturegen_Object=MibScalar
upsBatteryTemperaturegen=_UpsBatteryTemperaturegen_Object((1,3,6,1,4,1,818,1,1,10,2,7),_UpsBatteryTemperaturegen_Type())
upsBatteryTemperaturegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryTemperaturegen.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryTemperaturegen.setUnits('degrees Centigrade')
_UpsBatteryRipplegen_Type=Integer32
_UpsBatteryRipplegen_Object=MibScalar
upsBatteryRipplegen=_UpsBatteryRipplegen_Object((1,3,6,1,4,1,818,1,1,10,2,8),_UpsBatteryRipplegen_Type())
upsBatteryRipplegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBatteryRipplegen.setStatus(_A)
if mibBuilder.loadTexts:upsBatteryRipplegen.setUnits('0.1 Volt RMS')
_UpsInputgen_ObjectIdentity=ObjectIdentity
upsInputgen=_UpsInputgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,3))
_UpsInputLineBadsgen_Type=Counter32
_UpsInputLineBadsgen_Object=MibScalar
upsInputLineBadsgen=_UpsInputLineBadsgen_Object((1,3,6,1,4,1,818,1,1,10,3,1),_UpsInputLineBadsgen_Type())
upsInputLineBadsgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputLineBadsgen.setStatus(_A)
_UpsInputNumLinesgen_Type=NonNegativeInteger32
_UpsInputNumLinesgen_Object=MibScalar
upsInputNumLinesgen=_UpsInputNumLinesgen_Object((1,3,6,1,4,1,818,1,1,10,3,2),_UpsInputNumLinesgen_Type())
upsInputNumLinesgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputNumLinesgen.setStatus(_A)
_UpsInputGenTable_Object=MibTable
upsInputGenTable=_UpsInputGenTable_Object((1,3,6,1,4,1,818,1,1,10,3,3))
if mibBuilder.loadTexts:upsInputGenTable.setStatus(_A)
_UpsInputGenEntry_Object=MibTableRow
upsInputGenEntry=_UpsInputGenEntry_Object((1,3,6,1,4,1,818,1,1,10,3,3,1))
upsInputGenEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:upsInputGenEntry.setStatus(_A)
_UpsInputLineIndexgen_Type=PositiveInteger32
_UpsInputLineIndexgen_Object=MibTableColumn
upsInputLineIndexgen=_UpsInputLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,1),_UpsInputLineIndexgen_Type())
upsInputLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsInputLineIndexgen.setStatus(_A)
_UpsInputFrequencygen_Type=NonNegativeInteger32
_UpsInputFrequencygen_Object=MibTableColumn
upsInputFrequencygen=_UpsInputFrequencygen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,2),_UpsInputFrequencygen_Type())
upsInputFrequencygen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputFrequencygen.setStatus(_A)
if mibBuilder.loadTexts:upsInputFrequencygen.setUnits(_I)
_UpsInputVoltagegen_Type=NonNegativeInteger32
_UpsInputVoltagegen_Object=MibTableColumn
upsInputVoltagegen=_UpsInputVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,3),_UpsInputVoltagegen_Type())
upsInputVoltagegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltagegen.setUnits(_F)
_UpsInputCurrentgen_Type=NonNegativeInteger32
_UpsInputCurrentgen_Object=MibTableColumn
upsInputCurrentgen=_UpsInputCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,4),_UpsInputCurrentgen_Type())
upsInputCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsInputCurrentgen.setUnits(_N)
_UpsInputTruePowergen_Type=NonNegativeInteger32
_UpsInputTruePowergen_Object=MibTableColumn
upsInputTruePowergen=_UpsInputTruePowergen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,5),_UpsInputTruePowergen_Type())
upsInputTruePowergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputTruePowergen.setStatus(_A)
if mibBuilder.loadTexts:upsInputTruePowergen.setUnits(_L)
_UpsInputVoltageMingen_Type=NonNegativeInteger32
_UpsInputVoltageMingen_Object=MibTableColumn
upsInputVoltageMingen=_UpsInputVoltageMingen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,6),_UpsInputVoltageMingen_Type())
upsInputVoltageMingen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltageMingen.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageMingen.setUnits(_F)
_UpsInputVoltageMaxgen_Type=NonNegativeInteger32
_UpsInputVoltageMaxgen_Object=MibTableColumn
upsInputVoltageMaxgen=_UpsInputVoltageMaxgen_Object((1,3,6,1,4,1,818,1,1,10,3,3,1,7),_UpsInputVoltageMaxgen_Type())
upsInputVoltageMaxgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsInputVoltageMaxgen.setStatus(_A)
if mibBuilder.loadTexts:upsInputVoltageMaxgen.setUnits(_F)
_UpsOutputgen_ObjectIdentity=ObjectIdentity
upsOutputgen=_UpsOutputgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,4))
class _UpsOutputSourcegen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('none',2),('normal',3),('bypass',4),('battery',5),('booster',6),('reducer',7)))
_UpsOutputSourcegen_Type.__name__=_D
_UpsOutputSourcegen_Object=MibScalar
upsOutputSourcegen=_UpsOutputSourcegen_Object((1,3,6,1,4,1,818,1,1,10,4,1),_UpsOutputSourcegen_Type())
upsOutputSourcegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputSourcegen.setStatus(_A)
_UpsOutputFrequencygen_Type=NonNegativeInteger32
_UpsOutputFrequencygen_Object=MibScalar
upsOutputFrequencygen=_UpsOutputFrequencygen_Object((1,3,6,1,4,1,818,1,1,10,4,2),_UpsOutputFrequencygen_Type())
upsOutputFrequencygen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputFrequencygen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputFrequencygen.setUnits(_I)
_UpsOutputNumLinesgen_Type=NonNegativeInteger32
_UpsOutputNumLinesgen_Object=MibScalar
upsOutputNumLinesgen=_UpsOutputNumLinesgen_Object((1,3,6,1,4,1,818,1,1,10,4,3),_UpsOutputNumLinesgen_Type())
upsOutputNumLinesgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputNumLinesgen.setStatus(_A)
_UpsOutputGenTable_Object=MibTable
upsOutputGenTable=_UpsOutputGenTable_Object((1,3,6,1,4,1,818,1,1,10,4,4))
if mibBuilder.loadTexts:upsOutputGenTable.setStatus(_A)
_UpsOutputGenEntry_Object=MibTableRow
upsOutputGenEntry=_UpsOutputGenEntry_Object((1,3,6,1,4,1,818,1,1,10,4,4,1))
upsOutputGenEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:upsOutputGenEntry.setStatus(_A)
_UpsOutputLineIndexgen_Type=PositiveInteger32
_UpsOutputLineIndexgen_Object=MibTableColumn
upsOutputLineIndexgen=_UpsOutputLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,1),_UpsOutputLineIndexgen_Type())
upsOutputLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsOutputLineIndexgen.setStatus(_A)
_UpsOutputVoltagegen_Type=NonNegativeInteger32
_UpsOutputVoltagegen_Object=MibTableColumn
upsOutputVoltagegen=_UpsOutputVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,2),_UpsOutputVoltagegen_Type())
upsOutputVoltagegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputVoltagegen.setUnits(_F)
_UpsOutputCurrentgen_Type=NonNegativeInteger32
_UpsOutputCurrentgen_Object=MibTableColumn
upsOutputCurrentgen=_UpsOutputCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,3),_UpsOutputCurrentgen_Type())
upsOutputCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputCurrentgen.setUnits(_N)
_UpsOutputPowergen_Type=NonNegativeInteger32
_UpsOutputPowergen_Object=MibTableColumn
upsOutputPowergen=_UpsOutputPowergen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,4),_UpsOutputPowergen_Type())
upsOutputPowergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPowergen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPowergen.setUnits(_L)
class _UpsOutputPercentLoadgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200))
_UpsOutputPercentLoadgen_Type.__name__=_D
_UpsOutputPercentLoadgen_Object=MibTableColumn
upsOutputPercentLoadgen=_UpsOutputPercentLoadgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,5),_UpsOutputPercentLoadgen_Type())
upsOutputPercentLoadgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPercentLoadgen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPercentLoadgen.setUnits(_Q)
class _UpsOutputPowerFactorgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-99,100))
_UpsOutputPowerFactorgen_Type.__name__=_D
_UpsOutputPowerFactorgen_Object=MibTableColumn
upsOutputPowerFactorgen=_UpsOutputPowerFactorgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,6),_UpsOutputPowerFactorgen_Type())
upsOutputPowerFactorgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPowerFactorgen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPowerFactorgen.setUnits('0.01 cos phi')
_UpsOutputPeakCurrentgen_Type=Integer32
_UpsOutputPeakCurrentgen_Object=MibTableColumn
upsOutputPeakCurrentgen=_UpsOutputPeakCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,7),_UpsOutputPeakCurrentgen_Type())
upsOutputPeakCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputPeakCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputPeakCurrentgen.setUnits('Amps')
_UpsOutputShareCurrentgen_Type=Integer32
_UpsOutputShareCurrentgen_Object=MibTableColumn
upsOutputShareCurrentgen=_UpsOutputShareCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,4,4,1,8),_UpsOutputShareCurrentgen_Type())
upsOutputShareCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsOutputShareCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsOutputShareCurrentgen.setUnits('Amps')
_UpsBypassgen_ObjectIdentity=ObjectIdentity
upsBypassgen=_UpsBypassgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,5))
_UpsBypassFrequencygen_Type=NonNegativeInteger32
_UpsBypassFrequencygen_Object=MibScalar
upsBypassFrequencygen=_UpsBypassFrequencygen_Object((1,3,6,1,4,1,818,1,1,10,5,1),_UpsBypassFrequencygen_Type())
upsBypassFrequencygen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassFrequencygen.setStatus(_A)
if mibBuilder.loadTexts:upsBypassFrequencygen.setUnits(_I)
_UpsBypassNumLinesgen_Type=NonNegativeInteger32
_UpsBypassNumLinesgen_Object=MibScalar
upsBypassNumLinesgen=_UpsBypassNumLinesgen_Object((1,3,6,1,4,1,818,1,1,10,5,2),_UpsBypassNumLinesgen_Type())
upsBypassNumLinesgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassNumLinesgen.setStatus(_A)
_UpsBypassGenTable_Object=MibTable
upsBypassGenTable=_UpsBypassGenTable_Object((1,3,6,1,4,1,818,1,1,10,5,3))
if mibBuilder.loadTexts:upsBypassGenTable.setStatus(_A)
_UpsBypassGenEntry_Object=MibTableRow
upsBypassGenEntry=_UpsBypassGenEntry_Object((1,3,6,1,4,1,818,1,1,10,5,3,1))
upsBypassGenEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:upsBypassGenEntry.setStatus(_A)
_UpsBypassLineIndexgen_Type=PositiveInteger32
_UpsBypassLineIndexgen_Object=MibTableColumn
upsBypassLineIndexgen=_UpsBypassLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,5,3,1,1),_UpsBypassLineIndexgen_Type())
upsBypassLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsBypassLineIndexgen.setStatus(_A)
_UpsBypassVoltagegen_Type=NonNegativeInteger32
_UpsBypassVoltagegen_Object=MibTableColumn
upsBypassVoltagegen=_UpsBypassVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,5,3,1,2),_UpsBypassVoltagegen_Type())
upsBypassVoltagegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsBypassVoltagegen.setUnits(_F)
_UpsBypassCurrentgen_Type=NonNegativeInteger32
_UpsBypassCurrentgen_Object=MibTableColumn
upsBypassCurrentgen=_UpsBypassCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,5,3,1,3),_UpsBypassCurrentgen_Type())
upsBypassCurrentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsBypassCurrentgen.setUnits(_N)
_UpsBypassPowergen_Type=NonNegativeInteger32
_UpsBypassPowergen_Object=MibTableColumn
upsBypassPowergen=_UpsBypassPowergen_Object((1,3,6,1,4,1,818,1,1,10,5,3,1,4),_UpsBypassPowergen_Type())
upsBypassPowergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsBypassPowergen.setStatus(_A)
if mibBuilder.loadTexts:upsBypassPowergen.setUnits(_L)
_UpsAlarmgen_ObjectIdentity=ObjectIdentity
upsAlarmgen=_UpsAlarmgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6))
_UpsAlarmsPresentgen_Type=Gauge32
_UpsAlarmsPresentgen_Object=MibScalar
upsAlarmsPresentgen=_UpsAlarmsPresentgen_Object((1,3,6,1,4,1,818,1,1,10,6,1),_UpsAlarmsPresentgen_Type())
upsAlarmsPresentgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmsPresentgen.setStatus(_A)
_UpsAlarmGenTable_Object=MibTable
upsAlarmGenTable=_UpsAlarmGenTable_Object((1,3,6,1,4,1,818,1,1,10,6,2))
if mibBuilder.loadTexts:upsAlarmGenTable.setStatus(_A)
_UpsAlarmGenEntry_Object=MibTableRow
upsAlarmGenEntry=_UpsAlarmGenEntry_Object((1,3,6,1,4,1,818,1,1,10,6,2,1))
upsAlarmGenEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:upsAlarmGenEntry.setStatus(_A)
_UpsAlarmIdgen_Type=PositiveInteger32
_UpsAlarmIdgen_Object=MibTableColumn
upsAlarmIdgen=_UpsAlarmIdgen_Object((1,3,6,1,4,1,818,1,1,10,6,2,1,1),_UpsAlarmIdgen_Type())
upsAlarmIdgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsAlarmIdgen.setStatus(_A)
_UpsAlarmDescrgen_Type=AutonomousType
_UpsAlarmDescrgen_Object=MibTableColumn
upsAlarmDescrgen=_UpsAlarmDescrgen_Object((1,3,6,1,4,1,818,1,1,10,6,2,1,2),_UpsAlarmDescrgen_Type())
upsAlarmDescrgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmDescrgen.setStatus(_A)
_UpsAlarmTimegen_Type=TimeStamp
_UpsAlarmTimegen_Object=MibTableColumn
upsAlarmTimegen=_UpsAlarmTimegen_Object((1,3,6,1,4,1,818,1,1,10,6,2,1,3),_UpsAlarmTimegen_Type())
upsAlarmTimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmTimegen.setStatus(_A)
_UpsWellKnownAlarmsgen_ObjectIdentity=ObjectIdentity
upsWellKnownAlarmsgen=_UpsWellKnownAlarmsgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3))
_UpsAlarmBatteryBadgen_ObjectIdentity=ObjectIdentity
upsAlarmBatteryBadgen=_UpsAlarmBatteryBadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,1))
if mibBuilder.loadTexts:upsAlarmBatteryBadgen.setStatus(_A)
_UpsAlarmOnBatterygen_ObjectIdentity=ObjectIdentity
upsAlarmOnBatterygen=_UpsAlarmOnBatterygen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,2))
if mibBuilder.loadTexts:upsAlarmOnBatterygen.setStatus(_A)
_UpsAlarmLowBatterygen_ObjectIdentity=ObjectIdentity
upsAlarmLowBatterygen=_UpsAlarmLowBatterygen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,3))
if mibBuilder.loadTexts:upsAlarmLowBatterygen.setStatus(_A)
_UpsAlarmDepletedBatterygen_ObjectIdentity=ObjectIdentity
upsAlarmDepletedBatterygen=_UpsAlarmDepletedBatterygen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,4))
if mibBuilder.loadTexts:upsAlarmDepletedBatterygen.setStatus(_A)
_UpsAlarmTempBadgen_ObjectIdentity=ObjectIdentity
upsAlarmTempBadgen=_UpsAlarmTempBadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,5))
if mibBuilder.loadTexts:upsAlarmTempBadgen.setStatus(_A)
_UpsAlarmInputBadgen_ObjectIdentity=ObjectIdentity
upsAlarmInputBadgen=_UpsAlarmInputBadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,6))
if mibBuilder.loadTexts:upsAlarmInputBadgen.setStatus(_A)
_UpsAlarmOutputBadgen_ObjectIdentity=ObjectIdentity
upsAlarmOutputBadgen=_UpsAlarmOutputBadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,7))
if mibBuilder.loadTexts:upsAlarmOutputBadgen.setStatus(_A)
_UpsAlarmOutputOverloadgen_ObjectIdentity=ObjectIdentity
upsAlarmOutputOverloadgen=_UpsAlarmOutputOverloadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,8))
if mibBuilder.loadTexts:upsAlarmOutputOverloadgen.setStatus(_A)
_UpsAlarmOnBypassgen_ObjectIdentity=ObjectIdentity
upsAlarmOnBypassgen=_UpsAlarmOnBypassgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,9))
if mibBuilder.loadTexts:upsAlarmOnBypassgen.setStatus(_A)
_UpsAlarmBypassBadgen_ObjectIdentity=ObjectIdentity
upsAlarmBypassBadgen=_UpsAlarmBypassBadgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,10))
if mibBuilder.loadTexts:upsAlarmBypassBadgen.setStatus(_A)
_UpsAlarmOutputOffAsRequestedgen_ObjectIdentity=ObjectIdentity
upsAlarmOutputOffAsRequestedgen=_UpsAlarmOutputOffAsRequestedgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,11))
if mibBuilder.loadTexts:upsAlarmOutputOffAsRequestedgen.setStatus(_A)
_UpsAlarmUpsOffAsRequestedgen_ObjectIdentity=ObjectIdentity
upsAlarmUpsOffAsRequestedgen=_UpsAlarmUpsOffAsRequestedgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,12))
if mibBuilder.loadTexts:upsAlarmUpsOffAsRequestedgen.setStatus(_A)
_UpsAlarmChargerFailedgen_ObjectIdentity=ObjectIdentity
upsAlarmChargerFailedgen=_UpsAlarmChargerFailedgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,13))
if mibBuilder.loadTexts:upsAlarmChargerFailedgen.setStatus(_A)
_UpsAlarmUpsOutputOffgen_ObjectIdentity=ObjectIdentity
upsAlarmUpsOutputOffgen=_UpsAlarmUpsOutputOffgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,14))
if mibBuilder.loadTexts:upsAlarmUpsOutputOffgen.setStatus(_A)
_UpsAlarmUpsSystemOffgen_ObjectIdentity=ObjectIdentity
upsAlarmUpsSystemOffgen=_UpsAlarmUpsSystemOffgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,15))
if mibBuilder.loadTexts:upsAlarmUpsSystemOffgen.setStatus(_A)
_UpsAlarmFanFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmFanFailuregen=_UpsAlarmFanFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,16))
if mibBuilder.loadTexts:upsAlarmFanFailuregen.setStatus(_A)
_UpsAlarmFuseFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmFuseFailuregen=_UpsAlarmFuseFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,17))
if mibBuilder.loadTexts:upsAlarmFuseFailuregen.setStatus(_A)
_UpsAlarmGeneralFaultgen_ObjectIdentity=ObjectIdentity
upsAlarmGeneralFaultgen=_UpsAlarmGeneralFaultgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,18))
if mibBuilder.loadTexts:upsAlarmGeneralFaultgen.setStatus(_A)
_UpsAlarmDiagnosticTestFailedgen_ObjectIdentity=ObjectIdentity
upsAlarmDiagnosticTestFailedgen=_UpsAlarmDiagnosticTestFailedgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,19))
if mibBuilder.loadTexts:upsAlarmDiagnosticTestFailedgen.setStatus(_A)
_UpsAlarmCommunicationsLostgen_ObjectIdentity=ObjectIdentity
upsAlarmCommunicationsLostgen=_UpsAlarmCommunicationsLostgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,20))
if mibBuilder.loadTexts:upsAlarmCommunicationsLostgen.setStatus(_A)
_UpsAlarmAwaitingPowergen_ObjectIdentity=ObjectIdentity
upsAlarmAwaitingPowergen=_UpsAlarmAwaitingPowergen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,21))
if mibBuilder.loadTexts:upsAlarmAwaitingPowergen.setStatus(_A)
_UpsAlarmShutdownPendinggen_ObjectIdentity=ObjectIdentity
upsAlarmShutdownPendinggen=_UpsAlarmShutdownPendinggen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,22))
if mibBuilder.loadTexts:upsAlarmShutdownPendinggen.setStatus(_A)
_UpsAlarmShutdownImminentgen_ObjectIdentity=ObjectIdentity
upsAlarmShutdownImminentgen=_UpsAlarmShutdownImminentgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,23))
if mibBuilder.loadTexts:upsAlarmShutdownImminentgen.setStatus(_A)
_UpsAlarmTestInProgressgen_ObjectIdentity=ObjectIdentity
upsAlarmTestInProgressgen=_UpsAlarmTestInProgressgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,24))
if mibBuilder.loadTexts:upsAlarmTestInProgressgen.setStatus(_A)
_UpsAlarmReceptacleOffgen_ObjectIdentity=ObjectIdentity
upsAlarmReceptacleOffgen=_UpsAlarmReceptacleOffgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,25))
if mibBuilder.loadTexts:upsAlarmReceptacleOffgen.setStatus(_A)
_UpsAlarmHighSpeedBusFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmHighSpeedBusFailuregen=_UpsAlarmHighSpeedBusFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,26))
if mibBuilder.loadTexts:upsAlarmHighSpeedBusFailuregen.setStatus(_A)
_UpsAlarmHighSpeedBusJACRCFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmHighSpeedBusJACRCFailuregen=_UpsAlarmHighSpeedBusJACRCFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,27))
if mibBuilder.loadTexts:upsAlarmHighSpeedBusJACRCFailuregen.setStatus(_A)
_UpsAlarmConnectivityBusFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmConnectivityBusFailuregen=_UpsAlarmConnectivityBusFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,28))
if mibBuilder.loadTexts:upsAlarmConnectivityBusFailuregen.setStatus(_A)
_UpsAlarmHighSpeedBusJBCRCFailuregen_ObjectIdentity=ObjectIdentity
upsAlarmHighSpeedBusJBCRCFailuregen=_UpsAlarmHighSpeedBusJBCRCFailuregen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,29))
if mibBuilder.loadTexts:upsAlarmHighSpeedBusJBCRCFailuregen.setStatus(_A)
_UpsAlarmCurrentSharinggen_ObjectIdentity=ObjectIdentity
upsAlarmCurrentSharinggen=_UpsAlarmCurrentSharinggen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,30))
if mibBuilder.loadTexts:upsAlarmCurrentSharinggen.setStatus(_A)
_UpsAlarmDCRipplegen_ObjectIdentity=ObjectIdentity
upsAlarmDCRipplegen=_UpsAlarmDCRipplegen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,6,3,31))
if mibBuilder.loadTexts:upsAlarmDCRipplegen.setStatus(_A)
_UpsAlarmMaskAgen_Type=Unsigned32
_UpsAlarmMaskAgen_Object=MibScalar
upsAlarmMaskAgen=_UpsAlarmMaskAgen_Object((1,3,6,1,4,1,818,1,1,10,6,4),_UpsAlarmMaskAgen_Type())
upsAlarmMaskAgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsAlarmMaskAgen.setStatus(_A)
_UpsTestgen_ObjectIdentity=ObjectIdentity
upsTestgen=_UpsTestgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7))
_UpsTestIdgen_Type=ObjectIdentifier
_UpsTestIdgen_Object=MibScalar
upsTestIdgen=_UpsTestIdgen_Object((1,3,6,1,4,1,818,1,1,10,7,1),_UpsTestIdgen_Type())
upsTestIdgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestIdgen.setStatus(_A)
_UpsTestSpinLockgen_Type=TestAndIncr
_UpsTestSpinLockgen_Object=MibScalar
upsTestSpinLockgen=_UpsTestSpinLockgen_Object((1,3,6,1,4,1,818,1,1,10,7,2),_UpsTestSpinLockgen_Type())
upsTestSpinLockgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTestSpinLockgen.setStatus(_A)
class _UpsTestResultsSummarygen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('donePass',1),('doneWarning',2),('doneError',3),('aborted',4),('inProgress',5),('noTestsInitiated',6)))
_UpsTestResultsSummarygen_Type.__name__=_D
_UpsTestResultsSummarygen_Object=MibScalar
upsTestResultsSummarygen=_UpsTestResultsSummarygen_Object((1,3,6,1,4,1,818,1,1,10,7,3),_UpsTestResultsSummarygen_Type())
upsTestResultsSummarygen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestResultsSummarygen.setStatus(_A)
_UpsTestResultsDetailgen_Type=DisplayString
_UpsTestResultsDetailgen_Object=MibScalar
upsTestResultsDetailgen=_UpsTestResultsDetailgen_Object((1,3,6,1,4,1,818,1,1,10,7,4),_UpsTestResultsDetailgen_Type())
upsTestResultsDetailgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestResultsDetailgen.setStatus(_A)
_UpsTestStartTimegen_Type=TimeStamp
_UpsTestStartTimegen_Object=MibScalar
upsTestStartTimegen=_UpsTestStartTimegen_Object((1,3,6,1,4,1,818,1,1,10,7,5),_UpsTestStartTimegen_Type())
upsTestStartTimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestStartTimegen.setStatus(_A)
_UpsTestElapsedTimegen_Type=TimeInterval
_UpsTestElapsedTimegen_Object=MibScalar
upsTestElapsedTimegen=_UpsTestElapsedTimegen_Object((1,3,6,1,4,1,818,1,1,10,7,6),_UpsTestElapsedTimegen_Type())
upsTestElapsedTimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsTestElapsedTimegen.setStatus(_A)
_UpsWellKnownTestsgen_ObjectIdentity=ObjectIdentity
upsWellKnownTestsgen=_UpsWellKnownTestsgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7))
_UpsTestNoTestsInitiatedgen_ObjectIdentity=ObjectIdentity
upsTestNoTestsInitiatedgen=_UpsTestNoTestsInitiatedgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7,1))
if mibBuilder.loadTexts:upsTestNoTestsInitiatedgen.setStatus(_A)
_UpsTestAbortTestInProgressgen_ObjectIdentity=ObjectIdentity
upsTestAbortTestInProgressgen=_UpsTestAbortTestInProgressgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7,2))
if mibBuilder.loadTexts:upsTestAbortTestInProgressgen.setStatus(_A)
_UpsTestGeneralSystemsTestgen_ObjectIdentity=ObjectIdentity
upsTestGeneralSystemsTestgen=_UpsTestGeneralSystemsTestgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7,3))
if mibBuilder.loadTexts:upsTestGeneralSystemsTestgen.setStatus(_A)
_UpsTestQuickBatteryTestgen_ObjectIdentity=ObjectIdentity
upsTestQuickBatteryTestgen=_UpsTestQuickBatteryTestgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7,4))
if mibBuilder.loadTexts:upsTestQuickBatteryTestgen.setStatus(_A)
_UpsTestDeepBatteryCalibrationgen_ObjectIdentity=ObjectIdentity
upsTestDeepBatteryCalibrationgen=_UpsTestDeepBatteryCalibrationgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,7,7,5))
if mibBuilder.loadTexts:upsTestDeepBatteryCalibrationgen.setStatus(_A)
_UpsControlgen_ObjectIdentity=ObjectIdentity
upsControlgen=_UpsControlgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,8))
class _UpsShutdownTypegen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('output',1),('system',2)))
_UpsShutdownTypegen_Type.__name__=_D
_UpsShutdownTypegen_Object=MibScalar
upsShutdownTypegen=_UpsShutdownTypegen_Object((1,3,6,1,4,1,818,1,1,10,8,1),_UpsShutdownTypegen_Type())
upsShutdownTypegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsShutdownTypegen.setStatus(_A)
class _UpsShutdownAfterDelaygen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_UpsShutdownAfterDelaygen_Type.__name__=_D
_UpsShutdownAfterDelaygen_Object=MibScalar
upsShutdownAfterDelaygen=_UpsShutdownAfterDelaygen_Object((1,3,6,1,4,1,818,1,1,10,8,2),_UpsShutdownAfterDelaygen_Type())
upsShutdownAfterDelaygen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsShutdownAfterDelaygen.setStatus(_A)
if mibBuilder.loadTexts:upsShutdownAfterDelaygen.setUnits(_H)
class _UpsStartupAfterDelaygen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_UpsStartupAfterDelaygen_Type.__name__=_D
_UpsStartupAfterDelaygen_Object=MibScalar
upsStartupAfterDelaygen=_UpsStartupAfterDelaygen_Object((1,3,6,1,4,1,818,1,1,10,8,3),_UpsStartupAfterDelaygen_Type())
upsStartupAfterDelaygen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsStartupAfterDelaygen.setStatus(_A)
if mibBuilder.loadTexts:upsStartupAfterDelaygen.setUnits(_H)
class _UpsRebootWithDurationgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,300))
_UpsRebootWithDurationgen_Type.__name__=_D
_UpsRebootWithDurationgen_Object=MibScalar
upsRebootWithDurationgen=_UpsRebootWithDurationgen_Object((1,3,6,1,4,1,818,1,1,10,8,4),_UpsRebootWithDurationgen_Type())
upsRebootWithDurationgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsRebootWithDurationgen.setStatus(_A)
if mibBuilder.loadTexts:upsRebootWithDurationgen.setUnits(_H)
class _UpsAutoRestartgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpsAutoRestartgen_Type.__name__=_D
_UpsAutoRestartgen_Object=MibScalar
upsAutoRestartgen=_UpsAutoRestartgen_Object((1,3,6,1,4,1,818,1,1,10,8,5),_UpsAutoRestartgen_Type())
upsAutoRestartgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsAutoRestartgen.setStatus(_A)
_UpsReceptaclesNumgen_Type=NonNegativeInteger32
_UpsReceptaclesNumgen_Object=MibScalar
upsReceptaclesNumgen=_UpsReceptaclesNumgen_Object((1,3,6,1,4,1,818,1,1,10,8,6),_UpsReceptaclesNumgen_Type())
upsReceptaclesNumgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsReceptaclesNumgen.setStatus(_A)
_UpsReceptacleGenTable_Object=MibTable
upsReceptacleGenTable=_UpsReceptacleGenTable_Object((1,3,6,1,4,1,818,1,1,10,8,7))
if mibBuilder.loadTexts:upsReceptacleGenTable.setStatus(_A)
_UpsReceptacleGenEntry_Object=MibTableRow
upsReceptacleGenEntry=_UpsReceptacleGenEntry_Object((1,3,6,1,4,1,818,1,1,10,8,7,1))
upsReceptacleGenEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:upsReceptacleGenEntry.setStatus(_A)
_UpsReceptacleLineIndexgen_Type=PositiveInteger32
_UpsReceptacleLineIndexgen_Object=MibTableColumn
upsReceptacleLineIndexgen=_UpsReceptacleLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,8,7,1,1),_UpsReceptacleLineIndexgen_Type())
upsReceptacleLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsReceptacleLineIndexgen.setStatus(_A)
class _UpsReceptacleOnOffgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpsReceptacleOnOffgen_Type.__name__=_D
_UpsReceptacleOnOffgen_Object=MibTableColumn
upsReceptacleOnOffgen=_UpsReceptacleOnOffgen_Object((1,3,6,1,4,1,818,1,1,10,8,7,1,2),_UpsReceptacleOnOffgen_Type())
upsReceptacleOnOffgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsReceptacleOnOffgen.setStatus(_A)
class _UpsUPSModegen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('offLine',1),('onLine',2),('ecomode',3),('iem',4)))
_UpsUPSModegen_Type.__name__=_D
_UpsUPSModegen_Object=MibScalar
upsUPSModegen=_UpsUPSModegen_Object((1,3,6,1,4,1,818,1,1,10,8,8),_UpsUPSModegen_Type())
upsUPSModegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsUPSModegen.setStatus(_A)
class _UpsRectifierOnOffgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpsRectifierOnOffgen_Type.__name__=_D
_UpsRectifierOnOffgen_Object=MibScalar
upsRectifierOnOffgen=_UpsRectifierOnOffgen_Object((1,3,6,1,4,1,818,1,1,10,8,9),_UpsRectifierOnOffgen_Type())
upsRectifierOnOffgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsRectifierOnOffgen.setStatus(_A)
class _UpsBatteryChargeMethodgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normalcharge',1),('boostcharge',2)))
_UpsBatteryChargeMethodgen_Type.__name__=_D
_UpsBatteryChargeMethodgen_Object=MibScalar
upsBatteryChargeMethodgen=_UpsBatteryChargeMethodgen_Object((1,3,6,1,4,1,818,1,1,10,8,10),_UpsBatteryChargeMethodgen_Type())
upsBatteryChargeMethodgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBatteryChargeMethodgen.setStatus(_A)
class _UpsInverterOnOffgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpsInverterOnOffgen_Type.__name__=_D
_UpsInverterOnOffgen_Object=MibScalar
upsInverterOnOffgen=_UpsInverterOnOffgen_Object((1,3,6,1,4,1,818,1,1,10,8,11),_UpsInverterOnOffgen_Type())
upsInverterOnOffgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsInverterOnOffgen.setStatus(_A)
class _UpsBypassOnOffgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_UpsBypassOnOffgen_Type.__name__=_D
_UpsBypassOnOffgen_Object=MibScalar
upsBypassOnOffgen=_UpsBypassOnOffgen_Object((1,3,6,1,4,1,818,1,1,10,8,12),_UpsBypassOnOffgen_Type())
upsBypassOnOffgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsBypassOnOffgen.setStatus(_A)
class _UpsLoadSourcegen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('onbypass',1),('onInverter',2),('onDetour',3),('loadOff',4),('other',5)))
_UpsLoadSourcegen_Type.__name__=_D
_UpsLoadSourcegen_Object=MibScalar
upsLoadSourcegen=_UpsLoadSourcegen_Object((1,3,6,1,4,1,818,1,1,10,8,13),_UpsLoadSourcegen_Type())
upsLoadSourcegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsLoadSourcegen.setStatus(_A)
_UpsConfiggen_ObjectIdentity=ObjectIdentity
upsConfiggen=_UpsConfiggen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,9))
_UpsConfigInputVoltagegen_Type=NonNegativeInteger32
_UpsConfigInputVoltagegen_Object=MibScalar
upsConfigInputVoltagegen=_UpsConfigInputVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,9,1),_UpsConfigInputVoltagegen_Type())
upsConfigInputVoltagegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigInputVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigInputVoltagegen.setUnits(_F)
_UpsConfigInputFreqgen_Type=NonNegativeInteger32
_UpsConfigInputFreqgen_Object=MibScalar
upsConfigInputFreqgen=_UpsConfigInputFreqgen_Object((1,3,6,1,4,1,818,1,1,10,9,2),_UpsConfigInputFreqgen_Type())
upsConfigInputFreqgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigInputFreqgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigInputFreqgen.setUnits(_I)
_UpsConfigOutputVoltagegen_Type=NonNegativeInteger32
_UpsConfigOutputVoltagegen_Object=MibScalar
upsConfigOutputVoltagegen=_UpsConfigOutputVoltagegen_Object((1,3,6,1,4,1,818,1,1,10,9,3),_UpsConfigOutputVoltagegen_Type())
upsConfigOutputVoltagegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigOutputVoltagegen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigOutputVoltagegen.setUnits(_F)
_UpsConfigOutputFreqgen_Type=NonNegativeInteger32
_UpsConfigOutputFreqgen_Object=MibScalar
upsConfigOutputFreqgen=_UpsConfigOutputFreqgen_Object((1,3,6,1,4,1,818,1,1,10,9,4),_UpsConfigOutputFreqgen_Type())
upsConfigOutputFreqgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigOutputFreqgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigOutputFreqgen.setUnits(_I)
_UpsConfigOutputVAgen_Type=NonNegativeInteger32
_UpsConfigOutputVAgen_Object=MibScalar
upsConfigOutputVAgen=_UpsConfigOutputVAgen_Object((1,3,6,1,4,1,818,1,1,10,9,5),_UpsConfigOutputVAgen_Type())
upsConfigOutputVAgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigOutputVAgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigOutputVAgen.setUnits('Volt-Amps')
_UpsConfigOutputPowergen_Type=NonNegativeInteger32
_UpsConfigOutputPowergen_Object=MibScalar
upsConfigOutputPowergen=_UpsConfigOutputPowergen_Object((1,3,6,1,4,1,818,1,1,10,9,6),_UpsConfigOutputPowergen_Type())
upsConfigOutputPowergen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsConfigOutputPowergen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigOutputPowergen.setUnits(_L)
_UpsConfigLowBattTimegen_Type=NonNegativeInteger32
_UpsConfigLowBattTimegen_Object=MibScalar
upsConfigLowBattTimegen=_UpsConfigLowBattTimegen_Object((1,3,6,1,4,1,818,1,1,10,9,7),_UpsConfigLowBattTimegen_Type())
upsConfigLowBattTimegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigLowBattTimegen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigLowBattTimegen.setUnits(_M)
class _UpsConfigAudibleStatusgen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),('muted',3)))
_UpsConfigAudibleStatusgen_Type.__name__=_D
_UpsConfigAudibleStatusgen_Object=MibScalar
upsConfigAudibleStatusgen=_UpsConfigAudibleStatusgen_Object((1,3,6,1,4,1,818,1,1,10,9,8),_UpsConfigAudibleStatusgen_Type())
upsConfigAudibleStatusgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigAudibleStatusgen.setStatus(_A)
_UpsConfigLowVoltageTransferPointgen_Type=NonNegativeInteger32
_UpsConfigLowVoltageTransferPointgen_Object=MibScalar
upsConfigLowVoltageTransferPointgen=_UpsConfigLowVoltageTransferPointgen_Object((1,3,6,1,4,1,818,1,1,10,9,9),_UpsConfigLowVoltageTransferPointgen_Type())
upsConfigLowVoltageTransferPointgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigLowVoltageTransferPointgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigLowVoltageTransferPointgen.setUnits(_F)
_UpsConfigHighVoltageTransferPointgen_Type=NonNegativeInteger32
_UpsConfigHighVoltageTransferPointgen_Object=MibScalar
upsConfigHighVoltageTransferPointgen=_UpsConfigHighVoltageTransferPointgen_Object((1,3,6,1,4,1,818,1,1,10,9,10),_UpsConfigHighVoltageTransferPointgen_Type())
upsConfigHighVoltageTransferPointgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigHighVoltageTransferPointgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigHighVoltageTransferPointgen.setUnits(_F)
_UpsConfigBatteryCapacitygen_Type=NonNegativeInteger32
_UpsConfigBatteryCapacitygen_Object=MibScalar
upsConfigBatteryCapacitygen=_UpsConfigBatteryCapacitygen_Object((1,3,6,1,4,1,818,1,1,10,9,11),_UpsConfigBatteryCapacitygen_Type())
upsConfigBatteryCapacitygen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigBatteryCapacitygen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigBatteryCapacitygen.setUnits('Amps Hours')
_UpsConfigBatteryChargeCurrentgen_Type=NonNegativeInteger32
_UpsConfigBatteryChargeCurrentgen_Object=MibScalar
upsConfigBatteryChargeCurrentgen=_UpsConfigBatteryChargeCurrentgen_Object((1,3,6,1,4,1,818,1,1,10,9,12),_UpsConfigBatteryChargeCurrentgen_Type())
upsConfigBatteryChargeCurrentgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigBatteryChargeCurrentgen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigBatteryChargeCurrentgen.setUnits(_R)
class _UpsConfigNoLoadShutdowngen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),(_Y,2)))
_UpsConfigNoLoadShutdowngen_Type.__name__=_D
_UpsConfigNoLoadShutdowngen_Object=MibScalar
upsConfigNoLoadShutdowngen=_UpsConfigNoLoadShutdowngen_Object((1,3,6,1,4,1,818,1,1,10,9,13),_UpsConfigNoLoadShutdowngen_Type())
upsConfigNoLoadShutdowngen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigNoLoadShutdowngen.setStatus(_A)
_UpsConfigStartDelaygen_Type=PositiveInteger32
_UpsConfigStartDelaygen_Object=MibScalar
upsConfigStartDelaygen=_UpsConfigStartDelaygen_Object((1,3,6,1,4,1,818,1,1,10,9,14),_UpsConfigStartDelaygen_Type())
upsConfigStartDelaygen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsConfigStartDelaygen.setStatus(_A)
if mibBuilder.loadTexts:upsConfigStartDelaygen.setUnits(_M)
_UpsGetSetgen_ObjectIdentity=ObjectIdentity
upsGetSetgen=_UpsGetSetgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,10))
_UpsEventGetNextgen_Type=PositiveInteger32
_UpsEventGetNextgen_Object=MibScalar
upsEventGetNextgen=_UpsEventGetNextgen_Object((1,3,6,1,4,1,818,1,1,10,10,1),_UpsEventGetNextgen_Type())
upsEventGetNextgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEventGetNextgen.setStatus(_A)
_UpsEventGetPreviousgen_Type=PositiveInteger32
_UpsEventGetPreviousgen_Object=MibScalar
upsEventGetPreviousgen=_UpsEventGetPreviousgen_Object((1,3,6,1,4,1,818,1,1,10,10,2),_UpsEventGetPreviousgen_Type())
upsEventGetPreviousgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEventGetPreviousgen.setStatus(_A)
_UpsEventSetStartingTimeStampgen_Type=NonNegativeInteger32
_UpsEventSetStartingTimeStampgen_Object=MibScalar
upsEventSetStartingTimeStampgen=_UpsEventSetStartingTimeStampgen_Object((1,3,6,1,4,1,818,1,1,10,10,3),_UpsEventSetStartingTimeStampgen_Type())
upsEventSetStartingTimeStampgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEventSetStartingTimeStampgen.setStatus(_A)
_UpsEventRetreiveCurrentTimeStampgen_Type=NonNegativeInteger32
_UpsEventRetreiveCurrentTimeStampgen_Object=MibScalar
upsEventRetreiveCurrentTimeStampgen=_UpsEventRetreiveCurrentTimeStampgen_Object((1,3,6,1,4,1,818,1,1,10,10,4),_UpsEventRetreiveCurrentTimeStampgen_Type())
upsEventRetreiveCurrentTimeStampgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEventRetreiveCurrentTimeStampgen.setStatus(_A)
_UpsEventTableSizegen_Type=NonNegativeInteger32
_UpsEventTableSizegen_Object=MibScalar
upsEventTableSizegen=_UpsEventTableSizegen_Object((1,3,6,1,4,1,818,1,1,10,10,5),_UpsEventTableSizegen_Type())
upsEventTableSizegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEventTableSizegen.setStatus(_A)
_UpsEventGenTable_Object=MibTable
upsEventGenTable=_UpsEventGenTable_Object((1,3,6,1,4,1,818,1,1,10,10,6))
if mibBuilder.loadTexts:upsEventGenTable.setStatus(_A)
_UpsEventGenEntry_Object=MibTableRow
upsEventGenEntry=_UpsEventGenEntry_Object((1,3,6,1,4,1,818,1,1,10,10,6,1))
upsEventGenEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:upsEventGenEntry.setStatus(_A)
_UpsEventLineIndexgen_Type=PositiveInteger32
_UpsEventLineIndexgen_Object=MibTableColumn
upsEventLineIndexgen=_UpsEventLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,10,6,1,1),_UpsEventLineIndexgen_Type())
upsEventLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsEventLineIndexgen.setStatus(_A)
_UpsEventCodegen_Type=Integer32
_UpsEventCodegen_Object=MibTableColumn
upsEventCodegen=_UpsEventCodegen_Object((1,3,6,1,4,1,818,1,1,10,10,6,1,2),_UpsEventCodegen_Type())
upsEventCodegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEventCodegen.setStatus(_A)
_UpsEventStatusgen_Type=NonNegativeInteger32
_UpsEventStatusgen_Object=MibTableColumn
upsEventStatusgen=_UpsEventStatusgen_Object((1,3,6,1,4,1,818,1,1,10,10,6,1,3),_UpsEventStatusgen_Type())
upsEventStatusgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEventStatusgen.setStatus(_A)
_UpsEventTimegen_Type=NonNegativeInteger32
_UpsEventTimegen_Object=MibTableColumn
upsEventTimegen=_UpsEventTimegen_Object((1,3,6,1,4,1,818,1,1,10,10,6,1,4),_UpsEventTimegen_Type())
upsEventTimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsEventTimegen.setStatus(_A)
_UpsParametersReadgen_Type=PositiveInteger32
_UpsParametersReadgen_Object=MibScalar
upsParametersReadgen=_UpsParametersReadgen_Object((1,3,6,1,4,1,818,1,1,10,10,7),_UpsParametersReadgen_Type())
upsParametersReadgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsParametersReadgen.setStatus(_A)
_UpsParametersWritegen_Type=PositiveInteger32
_UpsParametersWritegen_Object=MibScalar
upsParametersWritegen=_UpsParametersWritegen_Object((1,3,6,1,4,1,818,1,1,10,10,8),_UpsParametersWritegen_Type())
upsParametersWritegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsParametersWritegen.setStatus(_A)
_UpsParametersStartAddressgen_Type=NonNegativeInteger32
_UpsParametersStartAddressgen_Object=MibScalar
upsParametersStartAddressgen=_UpsParametersStartAddressgen_Object((1,3,6,1,4,1,818,1,1,10,10,9),_UpsParametersStartAddressgen_Type())
upsParametersStartAddressgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsParametersStartAddressgen.setStatus(_A)
_UpsParameterTableSizegen_Type=NonNegativeInteger32
_UpsParameterTableSizegen_Object=MibScalar
upsParameterTableSizegen=_UpsParameterTableSizegen_Object((1,3,6,1,4,1,818,1,1,10,10,10),_UpsParameterTableSizegen_Type())
upsParameterTableSizegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsParameterTableSizegen.setStatus(_A)
_UpsParameterGenTable_Object=MibTable
upsParameterGenTable=_UpsParameterGenTable_Object((1,3,6,1,4,1,818,1,1,10,10,11))
if mibBuilder.loadTexts:upsParameterGenTable.setStatus(_A)
_UpsParameterGenEntry_Object=MibTableRow
upsParameterGenEntry=_UpsParameterGenEntry_Object((1,3,6,1,4,1,818,1,1,10,10,11,1))
upsParameterGenEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:upsParameterGenEntry.setStatus(_A)
_UpsParameterLineIndexgen_Type=PositiveInteger32
_UpsParameterLineIndexgen_Object=MibTableColumn
upsParameterLineIndexgen=_UpsParameterLineIndexgen_Object((1,3,6,1,4,1,818,1,1,10,10,11,1,1),_UpsParameterLineIndexgen_Type())
upsParameterLineIndexgen.setMaxAccess(_G)
if mibBuilder.loadTexts:upsParameterLineIndexgen.setStatus(_A)
_UpsParameterValuegen_Type=Integer32
_UpsParameterValuegen_Object=MibTableColumn
upsParameterValuegen=_UpsParameterValuegen_Object((1,3,6,1,4,1,818,1,1,10,10,11,1,2),_UpsParameterValuegen_Type())
upsParameterValuegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsParameterValuegen.setStatus(_A)
_UpsStatusgen_Type=NonNegativeInteger32
_UpsStatusgen_Object=MibScalar
upsStatusgen=_UpsStatusgen_Object((1,3,6,1,4,1,818,1,1,10,10,12),_UpsStatusgen_Type())
upsStatusgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsStatusgen.setStatus(_A)
_UpsMainsStatisticsMBfailgen_Type=NonNegativeInteger32
_UpsMainsStatisticsMBfailgen_Object=MibScalar
upsMainsStatisticsMBfailgen=_UpsMainsStatisticsMBfailgen_Object((1,3,6,1,4,1,818,1,1,10,10,13),_UpsMainsStatisticsMBfailgen_Type())
upsMainsStatisticsMBfailgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsMBfailgen.setStatus(_A)
_UpsMainsStatisticsMRfailgen_Type=NonNegativeInteger32
_UpsMainsStatisticsMRfailgen_Object=MibScalar
upsMainsStatisticsMRfailgen=_UpsMainsStatisticsMRfailgen_Object((1,3,6,1,4,1,818,1,1,10,10,14),_UpsMainsStatisticsMRfailgen_Type())
upsMainsStatisticsMRfailgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsMRfailgen.setStatus(_A)
_UpsMainsStatisticsB2gen_Type=NonNegativeInteger32
_UpsMainsStatisticsB2gen_Object=MibScalar
upsMainsStatisticsB2gen=_UpsMainsStatisticsB2gen_Object((1,3,6,1,4,1,818,1,1,10,10,15),_UpsMainsStatisticsB2gen_Type())
upsMainsStatisticsB2gen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsB2gen.setStatus(_A)
_UpsMainsStatisticsB5gen_Type=NonNegativeInteger32
_UpsMainsStatisticsB5gen_Object=MibScalar
upsMainsStatisticsB5gen=_UpsMainsStatisticsB5gen_Object((1,3,6,1,4,1,818,1,1,10,10,16),_UpsMainsStatisticsB5gen_Type())
upsMainsStatisticsB5gen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsB5gen.setStatus(_A)
_UpsMainsStatisticsB10gen_Type=NonNegativeInteger32
_UpsMainsStatisticsB10gen_Object=MibScalar
upsMainsStatisticsB10gen=_UpsMainsStatisticsB10gen_Object((1,3,6,1,4,1,818,1,1,10,10,17),_UpsMainsStatisticsB10gen_Type())
upsMainsStatisticsB10gen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsB10gen.setStatus(_A)
_UpsMainsStatisticsB200gen_Type=NonNegativeInteger32
_UpsMainsStatisticsB200gen_Object=MibScalar
upsMainsStatisticsB200gen=_UpsMainsStatisticsB200gen_Object((1,3,6,1,4,1,818,1,1,10,10,18),_UpsMainsStatisticsB200gen_Type())
upsMainsStatisticsB200gen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsB200gen.setStatus(_A)
_UpsMainsStatisticsBypRelgen_Type=NonNegativeInteger32
_UpsMainsStatisticsBypRelgen_Object=MibScalar
upsMainsStatisticsBypRelgen=_UpsMainsStatisticsBypRelgen_Object((1,3,6,1,4,1,818,1,1,10,10,19),_UpsMainsStatisticsBypRelgen_Type())
upsMainsStatisticsBypRelgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsMainsStatisticsBypRelgen.setStatus(_A)
_UpsTimegen_Type=NonNegativeInteger32
_UpsTimegen_Object=MibScalar
upsTimegen=_UpsTimegen_Object((1,3,6,1,4,1,818,1,1,10,10,20),_UpsTimegen_Type())
upsTimegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsTimegen.setStatus(_A)
_UpsRequestPermissiongen_Type=DisplayString
_UpsRequestPermissiongen_Object=MibScalar
upsRequestPermissiongen=_UpsRequestPermissiongen_Object((1,3,6,1,4,1,818,1,1,10,10,21),_UpsRequestPermissiongen_Type())
upsRequestPermissiongen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsRequestPermissiongen.setStatus(_A)
_UpsEventGetCodegen_Type=Integer32
_UpsEventGetCodegen_Object=MibScalar
upsEventGetCodegen=_UpsEventGetCodegen_Object((1,3,6,1,4,1,818,1,1,10,10,22),_UpsEventGetCodegen_Type())
upsEventGetCodegen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEventGetCodegen.setStatus(_A)
_UpsEventSpinLockgen_Type=TestAndIncr
_UpsEventSpinLockgen_Object=MibScalar
upsEventSpinLockgen=_UpsEventSpinLockgen_Object((1,3,6,1,4,1,818,1,1,10,10,23),_UpsEventSpinLockgen_Type())
upsEventSpinLockgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsEventSpinLockgen.setStatus(_A)
_UpsParameterSpinLockgen_Type=TestAndIncr
_UpsParameterSpinLockgen_Object=MibScalar
upsParameterSpinLockgen=_UpsParameterSpinLockgen_Object((1,3,6,1,4,1,818,1,1,10,10,24),_UpsParameterSpinLockgen_Type())
upsParameterSpinLockgen.setMaxAccess(_C)
if mibBuilder.loadTexts:upsParameterSpinLockgen.setStatus(_A)
_GeUPSTrapsgen_ObjectIdentity=ObjectIdentity
geUPSTrapsgen=_GeUPSTrapsgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,11))
_UpsDiagnosticgen_ObjectIdentity=ObjectIdentity
upsDiagnosticgen=_UpsDiagnosticgen_ObjectIdentity((1,3,6,1,4,1,818,1,1,10,12))
_UpsDiagnosticBusJACommunicationStatusgen_Type=Integer32
_UpsDiagnosticBusJACommunicationStatusgen_Object=MibScalar
upsDiagnosticBusJACommunicationStatusgen=_UpsDiagnosticBusJACommunicationStatusgen_Object((1,3,6,1,4,1,818,1,1,10,12,1),_UpsDiagnosticBusJACommunicationStatusgen_Type())
upsDiagnosticBusJACommunicationStatusgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticBusJACommunicationStatusgen.setStatus(_A)
_UpsDiagnosticBusJBCommunicationStatusgen_Type=Integer32
_UpsDiagnosticBusJBCommunicationStatusgen_Object=MibScalar
upsDiagnosticBusJBCommunicationStatusgen=_UpsDiagnosticBusJBCommunicationStatusgen_Object((1,3,6,1,4,1,818,1,1,10,12,2),_UpsDiagnosticBusJBCommunicationStatusgen_Type())
upsDiagnosticBusJBCommunicationStatusgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticBusJBCommunicationStatusgen.setStatus(_A)
_UpsDiagnosticBatteryLifetimegen_Type=Integer32
_UpsDiagnosticBatteryLifetimegen_Object=MibScalar
upsDiagnosticBatteryLifetimegen=_UpsDiagnosticBatteryLifetimegen_Object((1,3,6,1,4,1,818,1,1,10,12,3),_UpsDiagnosticBatteryLifetimegen_Type())
upsDiagnosticBatteryLifetimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticBatteryLifetimegen.setStatus(_A)
_UpsDiagnosticFansLifetimegen_Type=Integer32
_UpsDiagnosticFansLifetimegen_Object=MibScalar
upsDiagnosticFansLifetimegen=_UpsDiagnosticFansLifetimegen_Object((1,3,6,1,4,1,818,1,1,10,12,4),_UpsDiagnosticFansLifetimegen_Type())
upsDiagnosticFansLifetimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticFansLifetimegen.setStatus(_A)
_UpsDiagnosticDCcapacitorsLifetimegen_Type=Integer32
_UpsDiagnosticDCcapacitorsLifetimegen_Object=MibScalar
upsDiagnosticDCcapacitorsLifetimegen=_UpsDiagnosticDCcapacitorsLifetimegen_Object((1,3,6,1,4,1,818,1,1,10,12,5),_UpsDiagnosticDCcapacitorsLifetimegen_Type())
upsDiagnosticDCcapacitorsLifetimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticDCcapacitorsLifetimegen.setStatus(_A)
_UpsDiagnosticACcapacitorsLifetimegen_Type=Integer32
_UpsDiagnosticACcapacitorsLifetimegen_Object=MibScalar
upsDiagnosticACcapacitorsLifetimegen=_UpsDiagnosticACcapacitorsLifetimegen_Object((1,3,6,1,4,1,818,1,1,10,12,6),_UpsDiagnosticACcapacitorsLifetimegen_Type())
upsDiagnosticACcapacitorsLifetimegen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticACcapacitorsLifetimegen.setStatus(_A)
_UpsDiagnosticGlobalServiceCheckgen_Type=Integer32
_UpsDiagnosticGlobalServiceCheckgen_Object=MibScalar
upsDiagnosticGlobalServiceCheckgen=_UpsDiagnosticGlobalServiceCheckgen_Object((1,3,6,1,4,1,818,1,1,10,12,7),_UpsDiagnosticGlobalServiceCheckgen_Type())
upsDiagnosticGlobalServiceCheckgen.setMaxAccess(_B)
if mibBuilder.loadTexts:upsDiagnosticGlobalServiceCheckgen.setStatus(_A)
_GeDevices_ObjectIdentity=ObjectIdentity
geDevices=_GeDevices_ObjectIdentity((1,3,6,1,4,1,818,1,100))
_GeDevicesDescriptions_ObjectIdentity=ObjectIdentity
geDevicesDescriptions=_GeDevicesDescriptions_ObjectIdentity((1,3,6,1,4,1,818,1,100,1))
_AdvSNMPWebIntCard_ObjectIdentity=ObjectIdentity
advSNMPWebIntCard=_AdvSNMPWebIntCard_ObjectIdentity((1,3,6,1,4,1,818,1,100,1,1))
_SnmpWebIntCard_ObjectIdentity=ObjectIdentity
snmpWebIntCard=_SnmpWebIntCard_ObjectIdentity((1,3,6,1,4,1,818,1,100,1,2))
_SnmpWebIntBox_ObjectIdentity=ObjectIdentity
snmpWebIntBox=_SnmpWebIntBox_ObjectIdentity((1,3,6,1,4,1,818,1,100,1,3))
upsTrapAlarmBatteryBadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,1))
if mibBuilder.loadTexts:upsTrapAlarmBatteryBadgen.setStatus(_A)
upsTrapAlarmOnBatterygen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,2))
upsTrapAlarmOnBatterygen.setObjects((_E,_b))
if mibBuilder.loadTexts:upsTrapAlarmOnBatterygen.setStatus(_A)
upsTrapAlarmLowBatterygen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,3))
if mibBuilder.loadTexts:upsTrapAlarmLowBatterygen.setStatus(_A)
upsTrapAlarmDepletedBatterygen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,4))
if mibBuilder.loadTexts:upsTrapAlarmDepletedBatterygen.setStatus(_A)
upsTrapAlarmTempBadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,5))
upsTrapAlarmTempBadgen.setObjects((_E,_c))
if mibBuilder.loadTexts:upsTrapAlarmTempBadgen.setStatus(_A)
upsTrapAlarmInputBadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,6))
if mibBuilder.loadTexts:upsTrapAlarmInputBadgen.setStatus(_A)
upsTrapAlarmOutputBadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,7))
if mibBuilder.loadTexts:upsTrapAlarmOutputBadgen.setStatus(_A)
upsTrapAlarmOutputOverloadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,8))
upsTrapAlarmOutputOverloadgen.setObjects(*((_E,_d),(_E,_e)))
if mibBuilder.loadTexts:upsTrapAlarmOutputOverloadgen.setStatus(_A)
upsTrapAlarmOnBypassgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,9))
if mibBuilder.loadTexts:upsTrapAlarmOnBypassgen.setStatus(_A)
upsTrapAlarmBypassBadgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,10))
if mibBuilder.loadTexts:upsTrapAlarmBypassBadgen.setStatus(_A)
upsTrapAlarmOutputOffAsRequestedgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,11))
if mibBuilder.loadTexts:upsTrapAlarmOutputOffAsRequestedgen.setStatus(_A)
upsTrapAlarmUpsOffAsRequestedgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,12))
if mibBuilder.loadTexts:upsTrapAlarmUpsOffAsRequestedgen.setStatus(_A)
upsTrapAlarmChargerFailedgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,13))
if mibBuilder.loadTexts:upsTrapAlarmChargerFailedgen.setStatus(_A)
upsTrapAlarmUpsOutputOffgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,14))
if mibBuilder.loadTexts:upsTrapAlarmUpsOutputOffgen.setStatus(_A)
upsTrapAlarmUpsSystemOffgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,15))
if mibBuilder.loadTexts:upsTrapAlarmUpsSystemOffgen.setStatus(_A)
upsTrapAlarmFanFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,16))
if mibBuilder.loadTexts:upsTrapAlarmFanFailuregen.setStatus(_A)
upsTrapAlarmFuseFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,17))
if mibBuilder.loadTexts:upsTrapAlarmFuseFailuregen.setStatus(_A)
upsTrapAlarmGeneralFaultgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,18))
if mibBuilder.loadTexts:upsTrapAlarmGeneralFaultgen.setStatus(_A)
upsTrapAlarmDiagnosticTestFailedgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,19))
if mibBuilder.loadTexts:upsTrapAlarmDiagnosticTestFailedgen.setStatus(_A)
upsTrapAlarmCommunicationsLostgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,20))
if mibBuilder.loadTexts:upsTrapAlarmCommunicationsLostgen.setStatus(_A)
upsTrapAlarmAwaitingPowergen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,21))
if mibBuilder.loadTexts:upsTrapAlarmAwaitingPowergen.setStatus(_A)
upsTrapAlarmShutdownPendinggen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,22))
upsTrapAlarmShutdownPendinggen.setObjects((_E,_O))
if mibBuilder.loadTexts:upsTrapAlarmShutdownPendinggen.setStatus(_A)
upsTrapAlarmShutdownImminentgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,23))
if mibBuilder.loadTexts:upsTrapAlarmShutdownImminentgen.setStatus(_A)
upsTrapAlarmTestInProgressgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,24))
upsTrapAlarmTestInProgressgen.setObjects((_E,_P))
if mibBuilder.loadTexts:upsTrapAlarmTestInProgressgen.setStatus(_A)
upsTrapAlarmReceptacleOffgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,25))
if mibBuilder.loadTexts:upsTrapAlarmReceptacleOffgen.setStatus(_A)
upsTrapAlarmHighspeedBusFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,26))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusFailuregen.setStatus(_A)
upsTrapAlarmHighspeedBusJACRCFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,27))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusJACRCFailuregen.setStatus(_A)
upsTrapAlarmConnectivityBusFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,28))
if mibBuilder.loadTexts:upsTrapAlarmConnectivityBusFailuregen.setStatus(_A)
upsTrapAlarmHighspeedBusJBCRCFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,29))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusJBCRCFailuregen.setStatus(_A)
upsTrapAlarmCurrentSharingFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,30))
if mibBuilder.loadTexts:upsTrapAlarmCurrentSharingFailuregen.setStatus(_A)
upsTrapAlarmDCRippleFailuregen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,31))
if mibBuilder.loadTexts:upsTrapAlarmDCRippleFailuregen.setStatus(_A)
upsTrapAlarmBatteryBadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,33))
if mibBuilder.loadTexts:upsTrapAlarmBatteryBadRestoredgen.setStatus(_A)
upsTrapAlarmOnBatteryRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,34))
if mibBuilder.loadTexts:upsTrapAlarmOnBatteryRestoredgen.setStatus(_A)
upsTrapAlarmLowBatteryRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,35))
if mibBuilder.loadTexts:upsTrapAlarmLowBatteryRestoredgen.setStatus(_A)
upsTrapAlarmDepletedBatteryRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,36))
if mibBuilder.loadTexts:upsTrapAlarmDepletedBatteryRestoredgen.setStatus(_A)
upsTrapAlarmTempBadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,37))
if mibBuilder.loadTexts:upsTrapAlarmTempBadRestoredgen.setStatus(_A)
upsTrapAlarmInputBadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,38))
if mibBuilder.loadTexts:upsTrapAlarmInputBadRestoredgen.setStatus(_A)
upsTrapAlarmOutputBadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,39))
if mibBuilder.loadTexts:upsTrapAlarmOutputBadRestoredgen.setStatus(_A)
upsTrapAlarmOutputOverloadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,40))
if mibBuilder.loadTexts:upsTrapAlarmOutputOverloadRestoredgen.setStatus(_A)
upsTrapAlarmOnBypassRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,41))
if mibBuilder.loadTexts:upsTrapAlarmOnBypassRestoredgen.setStatus(_A)
upsTrapAlarmBypassBadRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,42))
if mibBuilder.loadTexts:upsTrapAlarmBypassBadRestoredgen.setStatus(_A)
upsTrapAlarmOutputOffAsRequestedRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,43))
if mibBuilder.loadTexts:upsTrapAlarmOutputOffAsRequestedRestoredgen.setStatus(_A)
upsTrapAlarmUpsOffAsRequestedRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,44))
if mibBuilder.loadTexts:upsTrapAlarmUpsOffAsRequestedRestoredgen.setStatus(_A)
upsTrapAlarmChargerFailedRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,45))
if mibBuilder.loadTexts:upsTrapAlarmChargerFailedRestoredgen.setStatus(_A)
upsTrapAlarmUpsOutputOngen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,46))
if mibBuilder.loadTexts:upsTrapAlarmUpsOutputOngen.setStatus(_A)
upsTrapAlarmUpsSystemOngen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,47))
if mibBuilder.loadTexts:upsTrapAlarmUpsSystemOngen.setStatus(_A)
upsTrapAlarmFanFailureRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,48))
if mibBuilder.loadTexts:upsTrapAlarmFanFailureRestoredgen.setStatus(_A)
upsTrapAlarmFuseFailureRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,49))
if mibBuilder.loadTexts:upsTrapAlarmFuseFailureRestoredgen.setStatus(_A)
upsTrapAlarmGeneralFaultRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,50))
if mibBuilder.loadTexts:upsTrapAlarmGeneralFaultRestoredgen.setStatus(_A)
upsTrapAlarmDiagnosticTestFailedRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,51))
if mibBuilder.loadTexts:upsTrapAlarmDiagnosticTestFailedRestoredgen.setStatus(_A)
upsTrapAlarmCommunicationsLostRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,52))
if mibBuilder.loadTexts:upsTrapAlarmCommunicationsLostRestoredgen.setStatus(_A)
upsTrapAlarmAwaitingPowerRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,53))
if mibBuilder.loadTexts:upsTrapAlarmAwaitingPowerRestoredgen.setStatus(_A)
upsTrapAlarmShutdownPendingRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,54))
upsTrapAlarmShutdownPendingRestoredgen.setObjects((_E,_O))
if mibBuilder.loadTexts:upsTrapAlarmShutdownPendingRestoredgen.setStatus(_A)
upsTrapAlarmShutdownImminentRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,55))
if mibBuilder.loadTexts:upsTrapAlarmShutdownImminentRestoredgen.setStatus(_A)
upsTrapAlarmTestInProgressRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,56))
upsTrapAlarmTestInProgressRestoredgen.setObjects((_E,_P))
if mibBuilder.loadTexts:upsTrapAlarmTestInProgressRestoredgen.setStatus(_A)
upsTrapAlarmReceptacleOn=NotificationType((1,3,6,1,4,1,818,1,1,10,11,57))
if mibBuilder.loadTexts:upsTrapAlarmReceptacleOn.setStatus(_A)
upsTrapAlarmHighspeedBusRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,58))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusRestoredgen.setStatus(_A)
upsTrapAlarmHighspeedBusJACRCRestoredAgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,59))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusJACRCRestoredAgen.setStatus(_A)
upsTrapAlarmConnectivityBusRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,60))
if mibBuilder.loadTexts:upsTrapAlarmConnectivityBusRestoredgen.setStatus(_A)
upsTrapAlarmHighspeedBusJBCRCRestoredBgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,61))
if mibBuilder.loadTexts:upsTrapAlarmHighspeedBusJBCRCRestoredBgen.setStatus(_A)
upsTrapAlarmCurrentSharingRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,62))
if mibBuilder.loadTexts:upsTrapAlarmCurrentSharingRestoredgen.setStatus(_A)
upsTrapAlarmDCRippleRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,63))
if mibBuilder.loadTexts:upsTrapAlarmDCRippleRestoredgen.setStatus(_A)
upsTrapAlarmValueLowgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,129))
if mibBuilder.loadTexts:upsTrapAlarmValueLowgen.setStatus(_A)
upsTrapAlarmValueHighgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,130))
if mibBuilder.loadTexts:upsTrapAlarmValueHighgen.setStatus(_A)
upsTrapAlarmValueLowRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,133))
if mibBuilder.loadTexts:upsTrapAlarmValueLowRestoredgen.setStatus(_A)
upsTrapAlarmValueHighRestoredgen=NotificationType((1,3,6,1,4,1,818,1,1,10,11,134))
if mibBuilder.loadTexts:upsTrapAlarmValueHighRestoredgen.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PositiveInteger32':PositiveInteger32,'NonNegativeInteger32':NonNegativeInteger32,'imv':imv,'geHardware':geHardware,'geUPS':geUPS,'geDiscoveredUPSsMask':geDiscoveredUPSsMask,'geRequestPacket':geRequestPacket,'geReplyPacket':geReplyPacket,'geGenericUPS':geGenericUPS,'upsIdentgen':upsIdentgen,'upsIdentManufacturergen':upsIdentManufacturergen,'upsIdentModelgen':upsIdentModelgen,'upsIdentUPSSoftwareVersiongen':upsIdentUPSSoftwareVersiongen,'upsIdentAgentSoftwareVersiongen':upsIdentAgentSoftwareVersiongen,'upsIdentNamegen':upsIdentNamegen,'upsIdentAttachedDevicesgen':upsIdentAttachedDevicesgen,'upsIdentUPSSerialNumbergen':upsIdentUPSSerialNumbergen,'upsIdentComProtVersiongen':upsIdentComProtVersiongen,'upsIdentOperatingTimegen':upsIdentOperatingTimegen,'upsBatterygen':upsBatterygen,'upsBatteryStatusgen':upsBatteryStatusgen,_b:upsSecondsOnBatterygen,'upsEstimatedMinutesRemaininggen':upsEstimatedMinutesRemaininggen,'upsEstimatedChargeRemaininggen':upsEstimatedChargeRemaininggen,'upsBatteryVoltagegen':upsBatteryVoltagegen,'upsBatteryCurrentgen':upsBatteryCurrentgen,_c:upsBatteryTemperaturegen,'upsBatteryRipplegen':upsBatteryRipplegen,'upsInputgen':upsInputgen,'upsInputLineBadsgen':upsInputLineBadsgen,'upsInputNumLinesgen':upsInputNumLinesgen,'upsInputGenTable':upsInputGenTable,'upsInputGenEntry':upsInputGenEntry,_S:upsInputLineIndexgen,'upsInputFrequencygen':upsInputFrequencygen,'upsInputVoltagegen':upsInputVoltagegen,'upsInputCurrentgen':upsInputCurrentgen,'upsInputTruePowergen':upsInputTruePowergen,'upsInputVoltageMingen':upsInputVoltageMingen,'upsInputVoltageMaxgen':upsInputVoltageMaxgen,'upsOutputgen':upsOutputgen,'upsOutputSourcegen':upsOutputSourcegen,'upsOutputFrequencygen':upsOutputFrequencygen,_d:upsOutputNumLinesgen,'upsOutputGenTable':upsOutputGenTable,'upsOutputGenEntry':upsOutputGenEntry,_T:upsOutputLineIndexgen,'upsOutputVoltagegen':upsOutputVoltagegen,'upsOutputCurrentgen':upsOutputCurrentgen,'upsOutputPowergen':upsOutputPowergen,_e:upsOutputPercentLoadgen,'upsOutputPowerFactorgen':upsOutputPowerFactorgen,'upsOutputPeakCurrentgen':upsOutputPeakCurrentgen,'upsOutputShareCurrentgen':upsOutputShareCurrentgen,'upsBypassgen':upsBypassgen,'upsBypassFrequencygen':upsBypassFrequencygen,'upsBypassNumLinesgen':upsBypassNumLinesgen,'upsBypassGenTable':upsBypassGenTable,'upsBypassGenEntry':upsBypassGenEntry,_U:upsBypassLineIndexgen,'upsBypassVoltagegen':upsBypassVoltagegen,'upsBypassCurrentgen':upsBypassCurrentgen,'upsBypassPowergen':upsBypassPowergen,'upsAlarmgen':upsAlarmgen,'upsAlarmsPresentgen':upsAlarmsPresentgen,'upsAlarmGenTable':upsAlarmGenTable,'upsAlarmGenEntry':upsAlarmGenEntry,_V:upsAlarmIdgen,'upsAlarmDescrgen':upsAlarmDescrgen,'upsAlarmTimegen':upsAlarmTimegen,'upsWellKnownAlarmsgen':upsWellKnownAlarmsgen,'upsAlarmBatteryBadgen':upsAlarmBatteryBadgen,'upsAlarmOnBatterygen':upsAlarmOnBatterygen,'upsAlarmLowBatterygen':upsAlarmLowBatterygen,'upsAlarmDepletedBatterygen':upsAlarmDepletedBatterygen,'upsAlarmTempBadgen':upsAlarmTempBadgen,'upsAlarmInputBadgen':upsAlarmInputBadgen,'upsAlarmOutputBadgen':upsAlarmOutputBadgen,'upsAlarmOutputOverloadgen':upsAlarmOutputOverloadgen,'upsAlarmOnBypassgen':upsAlarmOnBypassgen,'upsAlarmBypassBadgen':upsAlarmBypassBadgen,'upsAlarmOutputOffAsRequestedgen':upsAlarmOutputOffAsRequestedgen,'upsAlarmUpsOffAsRequestedgen':upsAlarmUpsOffAsRequestedgen,'upsAlarmChargerFailedgen':upsAlarmChargerFailedgen,'upsAlarmUpsOutputOffgen':upsAlarmUpsOutputOffgen,'upsAlarmUpsSystemOffgen':upsAlarmUpsSystemOffgen,'upsAlarmFanFailuregen':upsAlarmFanFailuregen,'upsAlarmFuseFailuregen':upsAlarmFuseFailuregen,'upsAlarmGeneralFaultgen':upsAlarmGeneralFaultgen,'upsAlarmDiagnosticTestFailedgen':upsAlarmDiagnosticTestFailedgen,'upsAlarmCommunicationsLostgen':upsAlarmCommunicationsLostgen,'upsAlarmAwaitingPowergen':upsAlarmAwaitingPowergen,'upsAlarmShutdownPendinggen':upsAlarmShutdownPendinggen,'upsAlarmShutdownImminentgen':upsAlarmShutdownImminentgen,'upsAlarmTestInProgressgen':upsAlarmTestInProgressgen,'upsAlarmReceptacleOffgen':upsAlarmReceptacleOffgen,'upsAlarmHighSpeedBusFailuregen':upsAlarmHighSpeedBusFailuregen,'upsAlarmHighSpeedBusJACRCFailuregen':upsAlarmHighSpeedBusJACRCFailuregen,'upsAlarmConnectivityBusFailuregen':upsAlarmConnectivityBusFailuregen,'upsAlarmHighSpeedBusJBCRCFailuregen':upsAlarmHighSpeedBusJBCRCFailuregen,'upsAlarmCurrentSharinggen':upsAlarmCurrentSharinggen,'upsAlarmDCRipplegen':upsAlarmDCRipplegen,'upsAlarmMaskAgen':upsAlarmMaskAgen,'upsTestgen':upsTestgen,_P:upsTestIdgen,'upsTestSpinLockgen':upsTestSpinLockgen,'upsTestResultsSummarygen':upsTestResultsSummarygen,'upsTestResultsDetailgen':upsTestResultsDetailgen,'upsTestStartTimegen':upsTestStartTimegen,'upsTestElapsedTimegen':upsTestElapsedTimegen,'upsWellKnownTestsgen':upsWellKnownTestsgen,'upsTestNoTestsInitiatedgen':upsTestNoTestsInitiatedgen,'upsTestAbortTestInProgressgen':upsTestAbortTestInProgressgen,'upsTestGeneralSystemsTestgen':upsTestGeneralSystemsTestgen,'upsTestQuickBatteryTestgen':upsTestQuickBatteryTestgen,'upsTestDeepBatteryCalibrationgen':upsTestDeepBatteryCalibrationgen,'upsControlgen':upsControlgen,'upsShutdownTypegen':upsShutdownTypegen,_O:upsShutdownAfterDelaygen,'upsStartupAfterDelaygen':upsStartupAfterDelaygen,'upsRebootWithDurationgen':upsRebootWithDurationgen,'upsAutoRestartgen':upsAutoRestartgen,'upsReceptaclesNumgen':upsReceptaclesNumgen,'upsReceptacleGenTable':upsReceptacleGenTable,'upsReceptacleGenEntry':upsReceptacleGenEntry,_W:upsReceptacleLineIndexgen,'upsReceptacleOnOffgen':upsReceptacleOnOffgen,'upsUPSModegen':upsUPSModegen,'upsRectifierOnOffgen':upsRectifierOnOffgen,'upsBatteryChargeMethodgen':upsBatteryChargeMethodgen,'upsInverterOnOffgen':upsInverterOnOffgen,'upsBypassOnOffgen':upsBypassOnOffgen,'upsLoadSourcegen':upsLoadSourcegen,'upsConfiggen':upsConfiggen,'upsConfigInputVoltagegen':upsConfigInputVoltagegen,'upsConfigInputFreqgen':upsConfigInputFreqgen,'upsConfigOutputVoltagegen':upsConfigOutputVoltagegen,'upsConfigOutputFreqgen':upsConfigOutputFreqgen,'upsConfigOutputVAgen':upsConfigOutputVAgen,'upsConfigOutputPowergen':upsConfigOutputPowergen,'upsConfigLowBattTimegen':upsConfigLowBattTimegen,'upsConfigAudibleStatusgen':upsConfigAudibleStatusgen,'upsConfigLowVoltageTransferPointgen':upsConfigLowVoltageTransferPointgen,'upsConfigHighVoltageTransferPointgen':upsConfigHighVoltageTransferPointgen,'upsConfigBatteryCapacitygen':upsConfigBatteryCapacitygen,'upsConfigBatteryChargeCurrentgen':upsConfigBatteryChargeCurrentgen,'upsConfigNoLoadShutdowngen':upsConfigNoLoadShutdowngen,'upsConfigStartDelaygen':upsConfigStartDelaygen,'upsGetSetgen':upsGetSetgen,'upsEventGetNextgen':upsEventGetNextgen,'upsEventGetPreviousgen':upsEventGetPreviousgen,'upsEventSetStartingTimeStampgen':upsEventSetStartingTimeStampgen,'upsEventRetreiveCurrentTimeStampgen':upsEventRetreiveCurrentTimeStampgen,'upsEventTableSizegen':upsEventTableSizegen,'upsEventGenTable':upsEventGenTable,'upsEventGenEntry':upsEventGenEntry,_Z:upsEventLineIndexgen,'upsEventCodegen':upsEventCodegen,'upsEventStatusgen':upsEventStatusgen,'upsEventTimegen':upsEventTimegen,'upsParametersReadgen':upsParametersReadgen,'upsParametersWritegen':upsParametersWritegen,'upsParametersStartAddressgen':upsParametersStartAddressgen,'upsParameterTableSizegen':upsParameterTableSizegen,'upsParameterGenTable':upsParameterGenTable,'upsParameterGenEntry':upsParameterGenEntry,_a:upsParameterLineIndexgen,'upsParameterValuegen':upsParameterValuegen,'upsStatusgen':upsStatusgen,'upsMainsStatisticsMBfailgen':upsMainsStatisticsMBfailgen,'upsMainsStatisticsMRfailgen':upsMainsStatisticsMRfailgen,'upsMainsStatisticsB2gen':upsMainsStatisticsB2gen,'upsMainsStatisticsB5gen':upsMainsStatisticsB5gen,'upsMainsStatisticsB10gen':upsMainsStatisticsB10gen,'upsMainsStatisticsB200gen':upsMainsStatisticsB200gen,'upsMainsStatisticsBypRelgen':upsMainsStatisticsBypRelgen,'upsTimegen':upsTimegen,'upsRequestPermissiongen':upsRequestPermissiongen,'upsEventGetCodegen':upsEventGetCodegen,'upsEventSpinLockgen':upsEventSpinLockgen,'upsParameterSpinLockgen':upsParameterSpinLockgen,'geUPSTrapsgen':geUPSTrapsgen,'upsTrapAlarmBatteryBadgen':upsTrapAlarmBatteryBadgen,'upsTrapAlarmOnBatterygen':upsTrapAlarmOnBatterygen,'upsTrapAlarmLowBatterygen':upsTrapAlarmLowBatterygen,'upsTrapAlarmDepletedBatterygen':upsTrapAlarmDepletedBatterygen,'upsTrapAlarmTempBadgen':upsTrapAlarmTempBadgen,'upsTrapAlarmInputBadgen':upsTrapAlarmInputBadgen,'upsTrapAlarmOutputBadgen':upsTrapAlarmOutputBadgen,'upsTrapAlarmOutputOverloadgen':upsTrapAlarmOutputOverloadgen,'upsTrapAlarmOnBypassgen':upsTrapAlarmOnBypassgen,'upsTrapAlarmBypassBadgen':upsTrapAlarmBypassBadgen,'upsTrapAlarmOutputOffAsRequestedgen':upsTrapAlarmOutputOffAsRequestedgen,'upsTrapAlarmUpsOffAsRequestedgen':upsTrapAlarmUpsOffAsRequestedgen,'upsTrapAlarmChargerFailedgen':upsTrapAlarmChargerFailedgen,'upsTrapAlarmUpsOutputOffgen':upsTrapAlarmUpsOutputOffgen,'upsTrapAlarmUpsSystemOffgen':upsTrapAlarmUpsSystemOffgen,'upsTrapAlarmFanFailuregen':upsTrapAlarmFanFailuregen,'upsTrapAlarmFuseFailuregen':upsTrapAlarmFuseFailuregen,'upsTrapAlarmGeneralFaultgen':upsTrapAlarmGeneralFaultgen,'upsTrapAlarmDiagnosticTestFailedgen':upsTrapAlarmDiagnosticTestFailedgen,'upsTrapAlarmCommunicationsLostgen':upsTrapAlarmCommunicationsLostgen,'upsTrapAlarmAwaitingPowergen':upsTrapAlarmAwaitingPowergen,'upsTrapAlarmShutdownPendinggen':upsTrapAlarmShutdownPendinggen,'upsTrapAlarmShutdownImminentgen':upsTrapAlarmShutdownImminentgen,'upsTrapAlarmTestInProgressgen':upsTrapAlarmTestInProgressgen,'upsTrapAlarmReceptacleOffgen':upsTrapAlarmReceptacleOffgen,'upsTrapAlarmHighspeedBusFailuregen':upsTrapAlarmHighspeedBusFailuregen,'upsTrapAlarmHighspeedBusJACRCFailuregen':upsTrapAlarmHighspeedBusJACRCFailuregen,'upsTrapAlarmConnectivityBusFailuregen':upsTrapAlarmConnectivityBusFailuregen,'upsTrapAlarmHighspeedBusJBCRCFailuregen':upsTrapAlarmHighspeedBusJBCRCFailuregen,'upsTrapAlarmCurrentSharingFailuregen':upsTrapAlarmCurrentSharingFailuregen,'upsTrapAlarmDCRippleFailuregen':upsTrapAlarmDCRippleFailuregen,'upsTrapAlarmBatteryBadRestoredgen':upsTrapAlarmBatteryBadRestoredgen,'upsTrapAlarmOnBatteryRestoredgen':upsTrapAlarmOnBatteryRestoredgen,'upsTrapAlarmLowBatteryRestoredgen':upsTrapAlarmLowBatteryRestoredgen,'upsTrapAlarmDepletedBatteryRestoredgen':upsTrapAlarmDepletedBatteryRestoredgen,'upsTrapAlarmTempBadRestoredgen':upsTrapAlarmTempBadRestoredgen,'upsTrapAlarmInputBadRestoredgen':upsTrapAlarmInputBadRestoredgen,'upsTrapAlarmOutputBadRestoredgen':upsTrapAlarmOutputBadRestoredgen,'upsTrapAlarmOutputOverloadRestoredgen':upsTrapAlarmOutputOverloadRestoredgen,'upsTrapAlarmOnBypassRestoredgen':upsTrapAlarmOnBypassRestoredgen,'upsTrapAlarmBypassBadRestoredgen':upsTrapAlarmBypassBadRestoredgen,'upsTrapAlarmOutputOffAsRequestedRestoredgen':upsTrapAlarmOutputOffAsRequestedRestoredgen,'upsTrapAlarmUpsOffAsRequestedRestoredgen':upsTrapAlarmUpsOffAsRequestedRestoredgen,'upsTrapAlarmChargerFailedRestoredgen':upsTrapAlarmChargerFailedRestoredgen,'upsTrapAlarmUpsOutputOngen':upsTrapAlarmUpsOutputOngen,'upsTrapAlarmUpsSystemOngen':upsTrapAlarmUpsSystemOngen,'upsTrapAlarmFanFailureRestoredgen':upsTrapAlarmFanFailureRestoredgen,'upsTrapAlarmFuseFailureRestoredgen':upsTrapAlarmFuseFailureRestoredgen,'upsTrapAlarmGeneralFaultRestoredgen':upsTrapAlarmGeneralFaultRestoredgen,'upsTrapAlarmDiagnosticTestFailedRestoredgen':upsTrapAlarmDiagnosticTestFailedRestoredgen,'upsTrapAlarmCommunicationsLostRestoredgen':upsTrapAlarmCommunicationsLostRestoredgen,'upsTrapAlarmAwaitingPowerRestoredgen':upsTrapAlarmAwaitingPowerRestoredgen,'upsTrapAlarmShutdownPendingRestoredgen':upsTrapAlarmShutdownPendingRestoredgen,'upsTrapAlarmShutdownImminentRestoredgen':upsTrapAlarmShutdownImminentRestoredgen,'upsTrapAlarmTestInProgressRestoredgen':upsTrapAlarmTestInProgressRestoredgen,'upsTrapAlarmReceptacleOn':upsTrapAlarmReceptacleOn,'upsTrapAlarmHighspeedBusRestoredgen':upsTrapAlarmHighspeedBusRestoredgen,'upsTrapAlarmHighspeedBusJACRCRestoredAgen':upsTrapAlarmHighspeedBusJACRCRestoredAgen,'upsTrapAlarmConnectivityBusRestoredgen':upsTrapAlarmConnectivityBusRestoredgen,'upsTrapAlarmHighspeedBusJBCRCRestoredBgen':upsTrapAlarmHighspeedBusJBCRCRestoredBgen,'upsTrapAlarmCurrentSharingRestoredgen':upsTrapAlarmCurrentSharingRestoredgen,'upsTrapAlarmDCRippleRestoredgen':upsTrapAlarmDCRippleRestoredgen,'upsTrapAlarmValueLowgen':upsTrapAlarmValueLowgen,'upsTrapAlarmValueHighgen':upsTrapAlarmValueHighgen,'upsTrapAlarmValueLowRestoredgen':upsTrapAlarmValueLowRestoredgen,'upsTrapAlarmValueHighRestoredgen':upsTrapAlarmValueHighRestoredgen,'upsDiagnosticgen':upsDiagnosticgen,'upsDiagnosticBusJACommunicationStatusgen':upsDiagnosticBusJACommunicationStatusgen,'upsDiagnosticBusJBCommunicationStatusgen':upsDiagnosticBusJBCommunicationStatusgen,'upsDiagnosticBatteryLifetimegen':upsDiagnosticBatteryLifetimegen,'upsDiagnosticFansLifetimegen':upsDiagnosticFansLifetimegen,'upsDiagnosticDCcapacitorsLifetimegen':upsDiagnosticDCcapacitorsLifetimegen,'upsDiagnosticACcapacitorsLifetimegen':upsDiagnosticACcapacitorsLifetimegen,'upsDiagnosticGlobalServiceCheckgen':upsDiagnosticGlobalServiceCheckgen,'geDevices':geDevices,'geDevicesDescriptions':geDevicesDescriptions,'advSNMPWebIntCard':advSNMPWebIntCard,'snmpWebIntCard':snmpWebIntCard,'snmpWebIntBox':snmpWebIntBox})