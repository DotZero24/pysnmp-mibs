_Ax='hpicfXcvrChannelInfoGroup'
_Aw='hpicfXcvrInfoGroup2'
_Av='hpicfXcvrInfoGroup1'
_Au='hpicfXcvrInfoGroup'
_At='hpicfXcvrChannelErrors'
_As='hpicfXcvrChannelAlarms'
_Ar='hpicfXcvrChannelRxPower'
_Aq='hpicfXcvrChannelTxPower'
_Ap='hpicfXcvrChannelTxBias'
_Ao='hpicfXcvrManufacDate'
_An='hpicfXcvrDiagnosticsTimeStamp'
_Am='hpicfXcvrChannel'
_Al='rxLossOfSignal'
_Ak='txBiasHighAlarm'
_Aj='txBiasLowAlarm'
_Ai='txPowerHighAlarm'
_Ah='txPowerLowAlarm'
_Ag='rxPowerHighAlarm'
_Af='rxPowerLowAlarm'
_Ae='txBiasHighWarning'
_Ad='txBiasLowWarning'
_Ac='txPowerHighWarning'
_Ab='txPowerLowWarning'
_Aa='rxPowerHighWarning'
_AZ='rxPowerLowWarning'
_AY='hpicfXcvrDiagnosticsTimeTicks'
_AX='ifIndex'
_AW='IF-MIB'
_AV='hpicfXcvrMdiPairCDSwap'
_AU='hpicfXcvrMdiPairABSwap'
_AT='hpicfXcvrMdiPairDSkew'
_AS='hpicfXcvrMdiPairDPolaritySwap'
_AR='hpicfXcvrMdiPairDDistanceToFault'
_AQ='hpicfXcvrMdiPairDCableLength'
_AP='hpicfXcvrMdiPairDCableStatus'
_AO='hpicfXcvrMdiPairCSkew'
_AN='hpicfXcvrMdiPairCPolaritySwap'
_AM='hpicfXcvrMdiPairCDistanceToFault'
_AL='hpicfXcvrMdiPairCCableLength'
_AK='hpicfXcvrMdiPairCCableStatus'
_AJ='hpicfXcvrMdiPairBSkew'
_AI='hpicfXcvrMdiPairBPolaritySwap'
_AH='hpicfXcvrMdiPairBDistanceToFault'
_AG='hpicfXcvrMdiPairBCableLength'
_AF='hpicfXcvrMdiPairBCableStatus'
_AE='hpicfXcvrMdiPairASkew'
_AD='hpicfXcvrMdiPairAPolaritySwap'
_AC='hpicfXcvrMdiPairADistanceToFault'
_AB='hpicfXcvrMdiPairACableLength'
_AA='hpicfXcvrMdiPairACableStatus'
_A9='hpicfXcvrPhyDuplex'
_A8='hpicfXcvrPhySpeed'
_A7='hpicfXcvrPhyLinkStatus'
_A6='hpicfXcvrRcvPwrLoWarn'
_A5='hpicfXcvrRcvPwrHiWarn'
_A4='hpicfXcvrRcvPwrLoAlarm'
_A3='hpicfXcvrRcvPwrHiAlarm'
_A2='hpicfXcvrPwrOutLoWarn'
_A1='hpicfXcvrPwrOutHiWarn'
_A0='hpicfXcvrPwrOutLoAlarm'
_z='hpicfXcvrPwrOutHiAlarm'
_y='hpicfXcvrBiasLoWarn'
_x='hpicfXcvrBiasHiWarn'
_w='hpicfXcvrBiasLoAlarm'
_v='hpicfXcvrBiasHiAlarm'
_u='hpicfXcvrVccLoWarn'
_t='hpicfXcvrVccHiWarn'
_s='hpicfXcvrVccLoAlarm'
_r='hpicfXcvrVccHiAlarm'
_q='hpicfXcvrTempLoWarn'
_p='hpicfXcvrTempHiWarn'
_o='hpicfXcvrTempLoAlarm'
_n='hpicfXcvrTempHiAlarm'
_m='hpicfXcvrErrors'
_l='hpicfXcvrAlarms'
_k='hpicfXcvrTxPower'
_j='hpicfXcvrRxPower'
_i='hpicfXcvrBias'
_h='hpicfXcvrVoltage'
_g='hpicfXcvrTemp'
_f='hpicfXcvrDiagnosticsUpdate'
_e='hpicfXcvrDiagnostics'
_d='hpicfXcvrTxDist'
_c='hpicfXcvrWavelength'
_b='hpicfXcvrConnectorType'
_a='hpicfXcvrType'
_Z='hpicfXcvrSerial'
_Y='hpicfXcvrModel'
_X='hpicfXcvrPortDesc'
_W='hpicfXcvrPortIndex'
_V='nanoseconds'
_U='reversed'
_T='impedanceMismatch'
_S='failed'
_R='open'
_Q='short'
_P='thousandths of dBm'
_O='deprecated'
_N='hundreds of microvolts'
_M='thousandths of degrees Celsius'
_L='Bits'
_K='microamps'
_J='meters'
_I='normal'
_H='tenths of microwatts'
_G='SnmpAdminString'
_F='unspecified'
_E='Integer32'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='HP-ICF-TRANSCEIVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_AW,_AX)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpicfTransceiverMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82))
if mibBuilder.loadTexts:hpicfTransceiverMIB.setRevisions(('2016-02-23 00:00','2016-02-01 00:00','2015-02-17 00:00','2012-02-22 00:00','2011-07-25 00:00','2011-06-08 00:00','2011-03-14 00:00','2011-03-02 00:00'))
_HpicfXcvrObjects_ObjectIdentity=ObjectIdentity
hpicfXcvrObjects=_HpicfXcvrObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82,1))
_HpicfXcvrInfo_ObjectIdentity=ObjectIdentity
hpicfXcvrInfo=_HpicfXcvrInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1))
_HpicfXcvrInfoTable_Object=MibTable
hpicfXcvrInfoTable=_HpicfXcvrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1))
if mibBuilder.loadTexts:hpicfXcvrInfoTable.setStatus(_B)
_HpicfXcvrInfoEntry_Object=MibTableRow
hpicfXcvrInfoEntry=_HpicfXcvrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1))
hpicfXcvrInfoEntry.setIndexNames((0,_AW,_AX))
if mibBuilder.loadTexts:hpicfXcvrInfoEntry.setStatus(_B)
class _HpicfXcvrPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpicfXcvrPortIndex_Type.__name__=_E
_HpicfXcvrPortIndex_Object=MibTableColumn
hpicfXcvrPortIndex=_HpicfXcvrPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,1),_HpicfXcvrPortIndex_Type())
hpicfXcvrPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPortIndex.setStatus(_B)
class _HpicfXcvrPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_HpicfXcvrPortDesc_Type.__name__=_G
_HpicfXcvrPortDesc_Object=MibTableColumn
hpicfXcvrPortDesc=_HpicfXcvrPortDesc_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,2),_HpicfXcvrPortDesc_Type())
hpicfXcvrPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPortDesc.setStatus(_B)
class _HpicfXcvrModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfXcvrModel_Type.__name__=_G
_HpicfXcvrModel_Object=MibTableColumn
hpicfXcvrModel=_HpicfXcvrModel_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,3),_HpicfXcvrModel_Type())
hpicfXcvrModel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrModel.setStatus(_B)
class _HpicfXcvrSerial_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfXcvrSerial_Type.__name__=_G
_HpicfXcvrSerial_Object=MibTableColumn
hpicfXcvrSerial=_HpicfXcvrSerial_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,4),_HpicfXcvrSerial_Type())
hpicfXcvrSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrSerial.setStatus(_B)
class _HpicfXcvrType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpicfXcvrType_Type.__name__=_G
_HpicfXcvrType_Object=MibTableColumn
hpicfXcvrType=_HpicfXcvrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,5),_HpicfXcvrType_Type())
hpicfXcvrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrType.setStatus(_B)
class _HpicfXcvrConnectorType_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpicfXcvrConnectorType_Type.__name__=_G
_HpicfXcvrConnectorType_Object=MibTableColumn
hpicfXcvrConnectorType=_HpicfXcvrConnectorType_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,6),_HpicfXcvrConnectorType_Type())
hpicfXcvrConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrConnectorType.setStatus(_B)
class _HpicfXcvrWavelength_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,96))
_HpicfXcvrWavelength_Type.__name__=_G
_HpicfXcvrWavelength_Object=MibTableColumn
hpicfXcvrWavelength=_HpicfXcvrWavelength_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,7),_HpicfXcvrWavelength_Type())
hpicfXcvrWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrWavelength.setStatus(_B)
class _HpicfXcvrTxDist_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpicfXcvrTxDist_Type.__name__=_G
_HpicfXcvrTxDist_Object=MibTableColumn
hpicfXcvrTxDist=_HpicfXcvrTxDist_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,8),_HpicfXcvrTxDist_Type())
hpicfXcvrTxDist.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTxDist.setStatus(_B)
class _HpicfXcvrDiagnostics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('dom',1),('vct',2),('other',3)))
_HpicfXcvrDiagnostics_Type.__name__=_E
_HpicfXcvrDiagnostics_Object=MibTableColumn
hpicfXcvrDiagnostics=_HpicfXcvrDiagnostics_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,9),_HpicfXcvrDiagnostics_Type())
hpicfXcvrDiagnostics.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrDiagnostics.setStatus(_B)
_HpicfXcvrDiagnosticsUpdate_Type=TruthValue
_HpicfXcvrDiagnosticsUpdate_Object=MibTableColumn
hpicfXcvrDiagnosticsUpdate=_HpicfXcvrDiagnosticsUpdate_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,10),_HpicfXcvrDiagnosticsUpdate_Type())
hpicfXcvrDiagnosticsUpdate.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfXcvrDiagnosticsUpdate.setStatus(_B)
_HpicfXcvrTemp_Type=Integer32
_HpicfXcvrTemp_Object=MibTableColumn
hpicfXcvrTemp=_HpicfXcvrTemp_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,11),_HpicfXcvrTemp_Type())
hpicfXcvrTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTemp.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTemp.setUnits(_M)
class _HpicfXcvrVoltage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrVoltage_Type.__name__=_D
_HpicfXcvrVoltage_Object=MibTableColumn
hpicfXcvrVoltage=_HpicfXcvrVoltage_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,12),_HpicfXcvrVoltage_Type())
hpicfXcvrVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrVoltage.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrVoltage.setUnits(_N)
class _HpicfXcvrBias_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrBias_Type.__name__=_D
_HpicfXcvrBias_Object=MibTableColumn
hpicfXcvrBias=_HpicfXcvrBias_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,13),_HpicfXcvrBias_Type())
hpicfXcvrBias.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrBias.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrBias.setUnits(_K)
_HpicfXcvrTxPower_Type=Integer32
_HpicfXcvrTxPower_Object=MibTableColumn
hpicfXcvrTxPower=_HpicfXcvrTxPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,14),_HpicfXcvrTxPower_Type())
hpicfXcvrTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTxPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTxPower.setUnits(_P)
_HpicfXcvrRxPower_Type=Integer32
_HpicfXcvrRxPower_Object=MibTableColumn
hpicfXcvrRxPower=_HpicfXcvrRxPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,15),_HpicfXcvrRxPower_Type())
hpicfXcvrRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrRxPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrRxPower.setUnits(_P)
class _HpicfXcvrAlarms_Type(Bits):namedValues=NamedValues(*((_AZ,0),(_Aa,1),(_Ab,2),(_Ac,3),(_Ad,4),(_Ae,5),('vccLowWarning',6),('vccHighWarning',7),('tempLowWarning',8),('tempHighWarning',9),(_Af,10),(_Ag,11),(_Ah,12),(_Ai,13),(_Aj,14),(_Ak,15),('vccLowAlarm',16),('vccHighAlarm',17),('tempLowAlarm',18),('tempHighAlarm',19)))
_HpicfXcvrAlarms_Type.__name__=_L
_HpicfXcvrAlarms_Object=MibTableColumn
hpicfXcvrAlarms=_HpicfXcvrAlarms_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,16),_HpicfXcvrAlarms_Type())
hpicfXcvrAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrAlarms.setStatus(_B)
class _HpicfXcvrErrors_Type(Bits):namedValues=NamedValues(*(('xcvrIOError',0),('xcvrChecksum',1),('xcvrTypeAndPortConfigMismatch',2),('xcvrTypeNotSupported',3),('wisLocalFault',4),('rcvOpticalPowerFault',5),('pmapmdReceiverLocalFault',6),('pcsReceiveLocalFault',7),('phyXSReceiveLocalFault',8),('laserBiasCurrentFault',9),('laserTemperatureFault',10),('laserOutputPowerFault',11),('txFault',12),('pmapmdTransmitterLocalFault',13),('pcsTransmitLocalFault',14),('phyXSTransmitLocalFault',15),(_Al,16)))
_HpicfXcvrErrors_Type.__name__=_L
_HpicfXcvrErrors_Object=MibTableColumn
hpicfXcvrErrors=_HpicfXcvrErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,17),_HpicfXcvrErrors_Type())
hpicfXcvrErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrErrors.setStatus(_B)
_HpicfXcvrTempHiAlarm_Type=Integer32
_HpicfXcvrTempHiAlarm_Object=MibTableColumn
hpicfXcvrTempHiAlarm=_HpicfXcvrTempHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,18),_HpicfXcvrTempHiAlarm_Type())
hpicfXcvrTempHiAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTempHiAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTempHiAlarm.setUnits(_M)
_HpicfXcvrTempLoAlarm_Type=Integer32
_HpicfXcvrTempLoAlarm_Object=MibTableColumn
hpicfXcvrTempLoAlarm=_HpicfXcvrTempLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,19),_HpicfXcvrTempLoAlarm_Type())
hpicfXcvrTempLoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTempLoAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTempLoAlarm.setUnits(_M)
_HpicfXcvrTempHiWarn_Type=Integer32
_HpicfXcvrTempHiWarn_Object=MibTableColumn
hpicfXcvrTempHiWarn=_HpicfXcvrTempHiWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,20),_HpicfXcvrTempHiWarn_Type())
hpicfXcvrTempHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTempHiWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTempHiWarn.setUnits(_M)
_HpicfXcvrTempLoWarn_Type=Integer32
_HpicfXcvrTempLoWarn_Object=MibTableColumn
hpicfXcvrTempLoWarn=_HpicfXcvrTempLoWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,21),_HpicfXcvrTempLoWarn_Type())
hpicfXcvrTempLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrTempLoWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrTempLoWarn.setUnits(_M)
class _HpicfXcvrVccHiAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrVccHiAlarm_Type.__name__=_D
_HpicfXcvrVccHiAlarm_Object=MibTableColumn
hpicfXcvrVccHiAlarm=_HpicfXcvrVccHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,22),_HpicfXcvrVccHiAlarm_Type())
hpicfXcvrVccHiAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrVccHiAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrVccHiAlarm.setUnits(_N)
class _HpicfXcvrVccLoAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrVccLoAlarm_Type.__name__=_D
_HpicfXcvrVccLoAlarm_Object=MibTableColumn
hpicfXcvrVccLoAlarm=_HpicfXcvrVccLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,23),_HpicfXcvrVccLoAlarm_Type())
hpicfXcvrVccLoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrVccLoAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrVccLoAlarm.setUnits(_N)
class _HpicfXcvrVccHiWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrVccHiWarn_Type.__name__=_D
_HpicfXcvrVccHiWarn_Object=MibTableColumn
hpicfXcvrVccHiWarn=_HpicfXcvrVccHiWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,24),_HpicfXcvrVccHiWarn_Type())
hpicfXcvrVccHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrVccHiWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrVccHiWarn.setUnits(_N)
class _HpicfXcvrVccLoWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrVccLoWarn_Type.__name__=_D
_HpicfXcvrVccLoWarn_Object=MibTableColumn
hpicfXcvrVccLoWarn=_HpicfXcvrVccLoWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,25),_HpicfXcvrVccLoWarn_Type())
hpicfXcvrVccLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrVccLoWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrVccLoWarn.setUnits(_N)
class _HpicfXcvrBiasHiAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrBiasHiAlarm_Type.__name__=_D
_HpicfXcvrBiasHiAlarm_Object=MibTableColumn
hpicfXcvrBiasHiAlarm=_HpicfXcvrBiasHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,26),_HpicfXcvrBiasHiAlarm_Type())
hpicfXcvrBiasHiAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrBiasHiAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrBiasHiAlarm.setUnits(_K)
class _HpicfXcvrBiasLoAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrBiasLoAlarm_Type.__name__=_D
_HpicfXcvrBiasLoAlarm_Object=MibTableColumn
hpicfXcvrBiasLoAlarm=_HpicfXcvrBiasLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,27),_HpicfXcvrBiasLoAlarm_Type())
hpicfXcvrBiasLoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrBiasLoAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrBiasLoAlarm.setUnits(_K)
class _HpicfXcvrBiasHiWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrBiasHiWarn_Type.__name__=_D
_HpicfXcvrBiasHiWarn_Object=MibTableColumn
hpicfXcvrBiasHiWarn=_HpicfXcvrBiasHiWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,28),_HpicfXcvrBiasHiWarn_Type())
hpicfXcvrBiasHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrBiasHiWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrBiasHiWarn.setUnits(_K)
class _HpicfXcvrBiasLoWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrBiasLoWarn_Type.__name__=_D
_HpicfXcvrBiasLoWarn_Object=MibTableColumn
hpicfXcvrBiasLoWarn=_HpicfXcvrBiasLoWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,29),_HpicfXcvrBiasLoWarn_Type())
hpicfXcvrBiasLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrBiasLoWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrBiasLoWarn.setUnits(_K)
class _HpicfXcvrPwrOutHiAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrPwrOutHiAlarm_Type.__name__=_D
_HpicfXcvrPwrOutHiAlarm_Object=MibTableColumn
hpicfXcvrPwrOutHiAlarm=_HpicfXcvrPwrOutHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,30),_HpicfXcvrPwrOutHiAlarm_Type())
hpicfXcvrPwrOutHiAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPwrOutHiAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrPwrOutHiAlarm.setUnits(_H)
class _HpicfXcvrPwrOutLoAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrPwrOutLoAlarm_Type.__name__=_D
_HpicfXcvrPwrOutLoAlarm_Object=MibTableColumn
hpicfXcvrPwrOutLoAlarm=_HpicfXcvrPwrOutLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,31),_HpicfXcvrPwrOutLoAlarm_Type())
hpicfXcvrPwrOutLoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPwrOutLoAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrPwrOutLoAlarm.setUnits(_H)
class _HpicfXcvrPwrOutHiWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrPwrOutHiWarn_Type.__name__=_D
_HpicfXcvrPwrOutHiWarn_Object=MibTableColumn
hpicfXcvrPwrOutHiWarn=_HpicfXcvrPwrOutHiWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,32),_HpicfXcvrPwrOutHiWarn_Type())
hpicfXcvrPwrOutHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPwrOutHiWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrPwrOutHiWarn.setUnits(_H)
class _HpicfXcvrPwrOutLoWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrPwrOutLoWarn_Type.__name__=_D
_HpicfXcvrPwrOutLoWarn_Object=MibTableColumn
hpicfXcvrPwrOutLoWarn=_HpicfXcvrPwrOutLoWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,33),_HpicfXcvrPwrOutLoWarn_Type())
hpicfXcvrPwrOutLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPwrOutLoWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrPwrOutLoWarn.setUnits(_H)
class _HpicfXcvrRcvPwrHiAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrRcvPwrHiAlarm_Type.__name__=_D
_HpicfXcvrRcvPwrHiAlarm_Object=MibTableColumn
hpicfXcvrRcvPwrHiAlarm=_HpicfXcvrRcvPwrHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,34),_HpicfXcvrRcvPwrHiAlarm_Type())
hpicfXcvrRcvPwrHiAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrHiAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrHiAlarm.setUnits(_H)
class _HpicfXcvrRcvPwrLoAlarm_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrRcvPwrLoAlarm_Type.__name__=_D
_HpicfXcvrRcvPwrLoAlarm_Object=MibTableColumn
hpicfXcvrRcvPwrLoAlarm=_HpicfXcvrRcvPwrLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,35),_HpicfXcvrRcvPwrLoAlarm_Type())
hpicfXcvrRcvPwrLoAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrLoAlarm.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrLoAlarm.setUnits(_H)
class _HpicfXcvrRcvPwrHiWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrRcvPwrHiWarn_Type.__name__=_D
_HpicfXcvrRcvPwrHiWarn_Object=MibTableColumn
hpicfXcvrRcvPwrHiWarn=_HpicfXcvrRcvPwrHiWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,36),_HpicfXcvrRcvPwrHiWarn_Type())
hpicfXcvrRcvPwrHiWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrHiWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrHiWarn.setUnits(_H)
class _HpicfXcvrRcvPwrLoWarn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrRcvPwrLoWarn_Type.__name__=_D
_HpicfXcvrRcvPwrLoWarn_Object=MibTableColumn
hpicfXcvrRcvPwrLoWarn=_HpicfXcvrRcvPwrLoWarn_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,37),_HpicfXcvrRcvPwrLoWarn_Type())
hpicfXcvrRcvPwrLoWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrLoWarn.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrRcvPwrLoWarn.setUnits(_H)
class _HpicfXcvrDiagnosticsTimeStamp_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpicfXcvrDiagnosticsTimeStamp_Type.__name__=_G
_HpicfXcvrDiagnosticsTimeStamp_Object=MibTableColumn
hpicfXcvrDiagnosticsTimeStamp=_HpicfXcvrDiagnosticsTimeStamp_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,38),_HpicfXcvrDiagnosticsTimeStamp_Type())
hpicfXcvrDiagnosticsTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrDiagnosticsTimeStamp.setStatus(_O)
class _HpicfXcvrPhyLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_HpicfXcvrPhyLinkStatus_Type.__name__=_E
_HpicfXcvrPhyLinkStatus_Object=MibTableColumn
hpicfXcvrPhyLinkStatus=_HpicfXcvrPhyLinkStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,39),_HpicfXcvrPhyLinkStatus_Type())
hpicfXcvrPhyLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPhyLinkStatus.setStatus(_B)
class _HpicfXcvrPhySpeed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrPhySpeed_Type.__name__=_D
_HpicfXcvrPhySpeed_Object=MibTableColumn
hpicfXcvrPhySpeed=_HpicfXcvrPhySpeed_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,40),_HpicfXcvrPhySpeed_Type())
hpicfXcvrPhySpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPhySpeed.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrPhySpeed.setUnits('megabits per second')
class _HpicfXcvrPhyDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('half',0),('full',1),(_F,2)))
_HpicfXcvrPhyDuplex_Type.__name__=_E
_HpicfXcvrPhyDuplex_Object=MibTableColumn
hpicfXcvrPhyDuplex=_HpicfXcvrPhyDuplex_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,41),_HpicfXcvrPhyDuplex_Type())
hpicfXcvrPhyDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrPhyDuplex.setStatus(_B)
class _HpicfXcvrMdiPairACableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_F,5)))
_HpicfXcvrMdiPairACableStatus_Type.__name__=_E
_HpicfXcvrMdiPairACableStatus_Object=MibTableColumn
hpicfXcvrMdiPairACableStatus=_HpicfXcvrMdiPairACableStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,42),_HpicfXcvrMdiPairACableStatus_Type())
hpicfXcvrMdiPairACableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairACableStatus.setStatus(_B)
class _HpicfXcvrMdiPairACableLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairACableLength_Type.__name__=_D
_HpicfXcvrMdiPairACableLength_Object=MibTableColumn
hpicfXcvrMdiPairACableLength=_HpicfXcvrMdiPairACableLength_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,43),_HpicfXcvrMdiPairACableLength_Type())
hpicfXcvrMdiPairACableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairACableLength.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairACableLength.setUnits(_J)
class _HpicfXcvrMdiPairADistanceToFault_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairADistanceToFault_Type.__name__=_D
_HpicfXcvrMdiPairADistanceToFault_Object=MibTableColumn
hpicfXcvrMdiPairADistanceToFault=_HpicfXcvrMdiPairADistanceToFault_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,44),_HpicfXcvrMdiPairADistanceToFault_Type())
hpicfXcvrMdiPairADistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairADistanceToFault.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairADistanceToFault.setUnits(_J)
class _HpicfXcvrMdiPairAPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_U,1),(_F,2)))
_HpicfXcvrMdiPairAPolaritySwap_Type.__name__=_E
_HpicfXcvrMdiPairAPolaritySwap_Object=MibTableColumn
hpicfXcvrMdiPairAPolaritySwap=_HpicfXcvrMdiPairAPolaritySwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,45),_HpicfXcvrMdiPairAPolaritySwap_Type())
hpicfXcvrMdiPairAPolaritySwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairAPolaritySwap.setStatus(_B)
class _HpicfXcvrMdiPairASkew_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairASkew_Type.__name__=_D
_HpicfXcvrMdiPairASkew_Object=MibTableColumn
hpicfXcvrMdiPairASkew=_HpicfXcvrMdiPairASkew_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,46),_HpicfXcvrMdiPairASkew_Type())
hpicfXcvrMdiPairASkew.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairASkew.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairASkew.setUnits(_V)
class _HpicfXcvrMdiPairBCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_F,5)))
_HpicfXcvrMdiPairBCableStatus_Type.__name__=_E
_HpicfXcvrMdiPairBCableStatus_Object=MibTableColumn
hpicfXcvrMdiPairBCableStatus=_HpicfXcvrMdiPairBCableStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,47),_HpicfXcvrMdiPairBCableStatus_Type())
hpicfXcvrMdiPairBCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBCableStatus.setStatus(_B)
class _HpicfXcvrMdiPairBCableLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairBCableLength_Type.__name__=_D
_HpicfXcvrMdiPairBCableLength_Object=MibTableColumn
hpicfXcvrMdiPairBCableLength=_HpicfXcvrMdiPairBCableLength_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,48),_HpicfXcvrMdiPairBCableLength_Type())
hpicfXcvrMdiPairBCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBCableLength.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBCableLength.setUnits(_J)
class _HpicfXcvrMdiPairBDistanceToFault_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairBDistanceToFault_Type.__name__=_D
_HpicfXcvrMdiPairBDistanceToFault_Object=MibTableColumn
hpicfXcvrMdiPairBDistanceToFault=_HpicfXcvrMdiPairBDistanceToFault_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,49),_HpicfXcvrMdiPairBDistanceToFault_Type())
hpicfXcvrMdiPairBDistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBDistanceToFault.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBDistanceToFault.setUnits(_J)
class _HpicfXcvrMdiPairBPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_U,1),(_F,2)))
_HpicfXcvrMdiPairBPolaritySwap_Type.__name__=_E
_HpicfXcvrMdiPairBPolaritySwap_Object=MibTableColumn
hpicfXcvrMdiPairBPolaritySwap=_HpicfXcvrMdiPairBPolaritySwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,50),_HpicfXcvrMdiPairBPolaritySwap_Type())
hpicfXcvrMdiPairBPolaritySwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBPolaritySwap.setStatus(_B)
class _HpicfXcvrMdiPairBSkew_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairBSkew_Type.__name__=_D
_HpicfXcvrMdiPairBSkew_Object=MibTableColumn
hpicfXcvrMdiPairBSkew=_HpicfXcvrMdiPairBSkew_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,51),_HpicfXcvrMdiPairBSkew_Type())
hpicfXcvrMdiPairBSkew.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBSkew.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairBSkew.setUnits(_V)
class _HpicfXcvrMdiPairCCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_F,5)))
_HpicfXcvrMdiPairCCableStatus_Type.__name__=_E
_HpicfXcvrMdiPairCCableStatus_Object=MibTableColumn
hpicfXcvrMdiPairCCableStatus=_HpicfXcvrMdiPairCCableStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,52),_HpicfXcvrMdiPairCCableStatus_Type())
hpicfXcvrMdiPairCCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCCableStatus.setStatus(_B)
class _HpicfXcvrMdiPairCCableLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairCCableLength_Type.__name__=_D
_HpicfXcvrMdiPairCCableLength_Object=MibTableColumn
hpicfXcvrMdiPairCCableLength=_HpicfXcvrMdiPairCCableLength_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,53),_HpicfXcvrMdiPairCCableLength_Type())
hpicfXcvrMdiPairCCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCCableLength.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCCableLength.setUnits(_J)
class _HpicfXcvrMdiPairCDistanceToFault_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairCDistanceToFault_Type.__name__=_D
_HpicfXcvrMdiPairCDistanceToFault_Object=MibTableColumn
hpicfXcvrMdiPairCDistanceToFault=_HpicfXcvrMdiPairCDistanceToFault_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,54),_HpicfXcvrMdiPairCDistanceToFault_Type())
hpicfXcvrMdiPairCDistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCDistanceToFault.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCDistanceToFault.setUnits(_J)
class _HpicfXcvrMdiPairCPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_U,1),(_F,2)))
_HpicfXcvrMdiPairCPolaritySwap_Type.__name__=_E
_HpicfXcvrMdiPairCPolaritySwap_Object=MibTableColumn
hpicfXcvrMdiPairCPolaritySwap=_HpicfXcvrMdiPairCPolaritySwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,55),_HpicfXcvrMdiPairCPolaritySwap_Type())
hpicfXcvrMdiPairCPolaritySwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCPolaritySwap.setStatus(_B)
class _HpicfXcvrMdiPairCSkew_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairCSkew_Type.__name__=_D
_HpicfXcvrMdiPairCSkew_Object=MibTableColumn
hpicfXcvrMdiPairCSkew=_HpicfXcvrMdiPairCSkew_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,56),_HpicfXcvrMdiPairCSkew_Type())
hpicfXcvrMdiPairCSkew.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCSkew.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCSkew.setUnits(_V)
class _HpicfXcvrMdiPairDCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_F,5)))
_HpicfXcvrMdiPairDCableStatus_Type.__name__=_E
_HpicfXcvrMdiPairDCableStatus_Object=MibTableColumn
hpicfXcvrMdiPairDCableStatus=_HpicfXcvrMdiPairDCableStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,57),_HpicfXcvrMdiPairDCableStatus_Type())
hpicfXcvrMdiPairDCableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDCableStatus.setStatus(_B)
class _HpicfXcvrMdiPairDCableLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairDCableLength_Type.__name__=_D
_HpicfXcvrMdiPairDCableLength_Object=MibTableColumn
hpicfXcvrMdiPairDCableLength=_HpicfXcvrMdiPairDCableLength_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,58),_HpicfXcvrMdiPairDCableLength_Type())
hpicfXcvrMdiPairDCableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDCableLength.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDCableLength.setUnits(_J)
class _HpicfXcvrMdiPairDDistanceToFault_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairDDistanceToFault_Type.__name__=_D
_HpicfXcvrMdiPairDDistanceToFault_Object=MibTableColumn
hpicfXcvrMdiPairDDistanceToFault=_HpicfXcvrMdiPairDDistanceToFault_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,59),_HpicfXcvrMdiPairDDistanceToFault_Type())
hpicfXcvrMdiPairDDistanceToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDDistanceToFault.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDDistanceToFault.setUnits(_J)
class _HpicfXcvrMdiPairDPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),(_U,1),(_F,2)))
_HpicfXcvrMdiPairDPolaritySwap_Type.__name__=_E
_HpicfXcvrMdiPairDPolaritySwap_Object=MibTableColumn
hpicfXcvrMdiPairDPolaritySwap=_HpicfXcvrMdiPairDPolaritySwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,60),_HpicfXcvrMdiPairDPolaritySwap_Type())
hpicfXcvrMdiPairDPolaritySwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDPolaritySwap.setStatus(_B)
class _HpicfXcvrMdiPairDSkew_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfXcvrMdiPairDSkew_Type.__name__=_D
_HpicfXcvrMdiPairDSkew_Object=MibTableColumn
hpicfXcvrMdiPairDSkew=_HpicfXcvrMdiPairDSkew_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,61),_HpicfXcvrMdiPairDSkew_Type())
hpicfXcvrMdiPairDSkew.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDSkew.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrMdiPairDSkew.setUnits(_V)
class _HpicfXcvrMdiPairABSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mdi',0),('mdix',1),(_F,2)))
_HpicfXcvrMdiPairABSwap_Type.__name__=_E
_HpicfXcvrMdiPairABSwap_Object=MibTableColumn
hpicfXcvrMdiPairABSwap=_HpicfXcvrMdiPairABSwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,62),_HpicfXcvrMdiPairABSwap_Type())
hpicfXcvrMdiPairABSwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairABSwap.setStatus(_B)
class _HpicfXcvrMdiPairCDSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('mdi',0),('mdix',1),(_F,2)))
_HpicfXcvrMdiPairCDSwap_Type.__name__=_E
_HpicfXcvrMdiPairCDSwap_Object=MibTableColumn
hpicfXcvrMdiPairCDSwap=_HpicfXcvrMdiPairCDSwap_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,63),_HpicfXcvrMdiPairCDSwap_Type())
hpicfXcvrMdiPairCDSwap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrMdiPairCDSwap.setStatus(_B)
_HpicfXcvrDiagnosticsTimeTicks_Type=TimeTicks
_HpicfXcvrDiagnosticsTimeTicks_Object=MibTableColumn
hpicfXcvrDiagnosticsTimeTicks=_HpicfXcvrDiagnosticsTimeTicks_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,64),_HpicfXcvrDiagnosticsTimeTicks_Type())
hpicfXcvrDiagnosticsTimeTicks.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrDiagnosticsTimeTicks.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrDiagnosticsTimeTicks.setUnits('centi-seconds')
class _HpicfXcvrManufacDate_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HpicfXcvrManufacDate_Type.__name__=_G
_HpicfXcvrManufacDate_Object=MibTableColumn
hpicfXcvrManufacDate=_HpicfXcvrManufacDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,1,1,65),_HpicfXcvrManufacDate_Type())
hpicfXcvrManufacDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrManufacDate.setStatus(_B)
_HpicfXcvrChannelInfoTable_Object=MibTable
hpicfXcvrChannelInfoTable=_HpicfXcvrChannelInfoTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2))
if mibBuilder.loadTexts:hpicfXcvrChannelInfoTable.setStatus(_B)
_HpicfXcvrChannelInfoEntry_Object=MibTableRow
hpicfXcvrChannelInfoEntry=_HpicfXcvrChannelInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1))
hpicfXcvrChannelInfoEntry.setIndexNames((0,_AW,_AX),(0,_A,_Am))
if mibBuilder.loadTexts:hpicfXcvrChannelInfoEntry.setStatus(_B)
_HpicfXcvrChannel_Type=Unsigned32
_HpicfXcvrChannel_Object=MibTableColumn
hpicfXcvrChannel=_HpicfXcvrChannel_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,1),_HpicfXcvrChannel_Type())
hpicfXcvrChannel.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfXcvrChannel.setStatus(_B)
class _HpicfXcvrChannelTxBias_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfXcvrChannelTxBias_Type.__name__=_D
_HpicfXcvrChannelTxBias_Object=MibTableColumn
hpicfXcvrChannelTxBias=_HpicfXcvrChannelTxBias_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,2),_HpicfXcvrChannelTxBias_Type())
hpicfXcvrChannelTxBias.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrChannelTxBias.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrChannelTxBias.setUnits(_K)
_HpicfXcvrChannelTxPower_Type=Integer32
_HpicfXcvrChannelTxPower_Object=MibTableColumn
hpicfXcvrChannelTxPower=_HpicfXcvrChannelTxPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,3),_HpicfXcvrChannelTxPower_Type())
hpicfXcvrChannelTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrChannelTxPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrChannelTxPower.setUnits(_P)
_HpicfXcvrChannelRxPower_Type=Integer32
_HpicfXcvrChannelRxPower_Object=MibTableColumn
hpicfXcvrChannelRxPower=_HpicfXcvrChannelRxPower_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,4),_HpicfXcvrChannelRxPower_Type())
hpicfXcvrChannelRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrChannelRxPower.setStatus(_B)
if mibBuilder.loadTexts:hpicfXcvrChannelRxPower.setUnits(_P)
class _HpicfXcvrChannelAlarms_Type(Bits):namedValues=NamedValues(*((_AZ,0),(_Aa,1),(_Ab,2),(_Ac,3),(_Ad,4),(_Ae,5),(_Af,6),(_Ag,7),(_Ah,8),(_Ai,9),(_Aj,10),(_Ak,11)))
_HpicfXcvrChannelAlarms_Type.__name__=_L
_HpicfXcvrChannelAlarms_Object=MibTableColumn
hpicfXcvrChannelAlarms=_HpicfXcvrChannelAlarms_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,5),_HpicfXcvrChannelAlarms_Type())
hpicfXcvrChannelAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrChannelAlarms.setStatus(_B)
class _HpicfXcvrChannelErrors_Type(Bits):namedValues=NamedValues(*(('txFault',0),('txLossOfSignal',1),(_Al,2)))
_HpicfXcvrChannelErrors_Type.__name__=_L
_HpicfXcvrChannelErrors_Object=MibTableColumn
hpicfXcvrChannelErrors=_HpicfXcvrChannelErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,82,1,1,2,1,6),_HpicfXcvrChannelErrors_Type())
hpicfXcvrChannelErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfXcvrChannelErrors.setStatus(_B)
_HpicfXcvrConformance_ObjectIdentity=ObjectIdentity
hpicfXcvrConformance=_HpicfXcvrConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82,2))
_HpicfXcvrGroups_ObjectIdentity=ObjectIdentity
hpicfXcvrGroups=_HpicfXcvrGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82,2,1))
_HpicfXcvrCompliances_ObjectIdentity=ObjectIdentity
hpicfXcvrCompliances=_HpicfXcvrCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,82,2,2))
hpicfXcvrInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,82,2,1,1))
hpicfXcvrInfoGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_An),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:hpicfXcvrInfoGroup.setStatus(_O)
hpicfXcvrInfoGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,82,2,1,2))
hpicfXcvrInfoGroup1.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AY)))
if mibBuilder.loadTexts:hpicfXcvrInfoGroup1.setStatus(_O)
hpicfXcvrInfoGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,82,2,1,3))
hpicfXcvrInfoGroup2.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AY),(_A,_Ao)))
if mibBuilder.loadTexts:hpicfXcvrInfoGroup2.setStatus(_B)
hpicfXcvrChannelInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,82,2,1,4))
hpicfXcvrChannelInfoGroup.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:hpicfXcvrChannelInfoGroup.setStatus(_B)
hpicfXcvrCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,82,2,2,1))
hpicfXcvrCompliance.setObjects((_A,_Au))
if mibBuilder.loadTexts:hpicfXcvrCompliance.setStatus(_O)
hpicfXcvrCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,82,2,2,2))
hpicfXcvrCompliance1.setObjects((_A,_Av))
if mibBuilder.loadTexts:hpicfXcvrCompliance1.setStatus(_O)
hpicfXcvrCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,82,2,2,3))
hpicfXcvrCompliance2.setObjects((_A,_Aw))
if mibBuilder.loadTexts:hpicfXcvrCompliance2.setStatus(_B)
hpicfXcvrChannelCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,82,2,2,4))
hpicfXcvrChannelCompliance.setObjects((_A,_Ax))
if mibBuilder.loadTexts:hpicfXcvrChannelCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfTransceiverMIB':hpicfTransceiverMIB,'hpicfXcvrObjects':hpicfXcvrObjects,'hpicfXcvrInfo':hpicfXcvrInfo,'hpicfXcvrInfoTable':hpicfXcvrInfoTable,'hpicfXcvrInfoEntry':hpicfXcvrInfoEntry,_W:hpicfXcvrPortIndex,_X:hpicfXcvrPortDesc,_Y:hpicfXcvrModel,_Z:hpicfXcvrSerial,_a:hpicfXcvrType,_b:hpicfXcvrConnectorType,_c:hpicfXcvrWavelength,_d:hpicfXcvrTxDist,_e:hpicfXcvrDiagnostics,_f:hpicfXcvrDiagnosticsUpdate,_g:hpicfXcvrTemp,_h:hpicfXcvrVoltage,_i:hpicfXcvrBias,_k:hpicfXcvrTxPower,_j:hpicfXcvrRxPower,_l:hpicfXcvrAlarms,_m:hpicfXcvrErrors,_n:hpicfXcvrTempHiAlarm,_o:hpicfXcvrTempLoAlarm,_p:hpicfXcvrTempHiWarn,_q:hpicfXcvrTempLoWarn,_r:hpicfXcvrVccHiAlarm,_s:hpicfXcvrVccLoAlarm,_t:hpicfXcvrVccHiWarn,_u:hpicfXcvrVccLoWarn,_v:hpicfXcvrBiasHiAlarm,_w:hpicfXcvrBiasLoAlarm,_x:hpicfXcvrBiasHiWarn,_y:hpicfXcvrBiasLoWarn,_z:hpicfXcvrPwrOutHiAlarm,_A0:hpicfXcvrPwrOutLoAlarm,_A1:hpicfXcvrPwrOutHiWarn,_A2:hpicfXcvrPwrOutLoWarn,_A3:hpicfXcvrRcvPwrHiAlarm,_A4:hpicfXcvrRcvPwrLoAlarm,_A5:hpicfXcvrRcvPwrHiWarn,_A6:hpicfXcvrRcvPwrLoWarn,_An:hpicfXcvrDiagnosticsTimeStamp,_A7:hpicfXcvrPhyLinkStatus,_A8:hpicfXcvrPhySpeed,_A9:hpicfXcvrPhyDuplex,_AA:hpicfXcvrMdiPairACableStatus,_AB:hpicfXcvrMdiPairACableLength,_AC:hpicfXcvrMdiPairADistanceToFault,_AD:hpicfXcvrMdiPairAPolaritySwap,_AE:hpicfXcvrMdiPairASkew,_AF:hpicfXcvrMdiPairBCableStatus,_AG:hpicfXcvrMdiPairBCableLength,_AH:hpicfXcvrMdiPairBDistanceToFault,_AI:hpicfXcvrMdiPairBPolaritySwap,_AJ:hpicfXcvrMdiPairBSkew,_AK:hpicfXcvrMdiPairCCableStatus,_AL:hpicfXcvrMdiPairCCableLength,_AM:hpicfXcvrMdiPairCDistanceToFault,_AN:hpicfXcvrMdiPairCPolaritySwap,_AO:hpicfXcvrMdiPairCSkew,_AP:hpicfXcvrMdiPairDCableStatus,_AQ:hpicfXcvrMdiPairDCableLength,_AR:hpicfXcvrMdiPairDDistanceToFault,_AS:hpicfXcvrMdiPairDPolaritySwap,_AT:hpicfXcvrMdiPairDSkew,_AU:hpicfXcvrMdiPairABSwap,_AV:hpicfXcvrMdiPairCDSwap,_AY:hpicfXcvrDiagnosticsTimeTicks,_Ao:hpicfXcvrManufacDate,'hpicfXcvrChannelInfoTable':hpicfXcvrChannelInfoTable,'hpicfXcvrChannelInfoEntry':hpicfXcvrChannelInfoEntry,_Am:hpicfXcvrChannel,_Ap:hpicfXcvrChannelTxBias,_Aq:hpicfXcvrChannelTxPower,_Ar:hpicfXcvrChannelRxPower,_As:hpicfXcvrChannelAlarms,_At:hpicfXcvrChannelErrors,'hpicfXcvrConformance':hpicfXcvrConformance,'hpicfXcvrGroups':hpicfXcvrGroups,_Au:hpicfXcvrInfoGroup,_Av:hpicfXcvrInfoGroup1,_Aw:hpicfXcvrInfoGroup2,_Ax:hpicfXcvrChannelInfoGroup,'hpicfXcvrCompliances':hpicfXcvrCompliances,'hpicfXcvrCompliance':hpicfXcvrCompliance,'hpicfXcvrCompliance1':hpicfXcvrCompliance1,'hpicfXcvrCompliance2':hpicfXcvrCompliance2,'hpicfXcvrChannelCompliance':hpicfXcvrChannelCompliance})