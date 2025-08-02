_G='hpnicfTransceiverChannelIndex'
_F='HPN-ICF-TRANSCEIVER-INFO-MIB'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfTransceiver=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,70))
if mibBuilder.loadTexts:hpnicfTransceiver.setRevisions(('2013-07-23 16:50','2009-12-29 16:50'))
_HpnicfTransceiverInfoAdm_ObjectIdentity=ObjectIdentity
hpnicfTransceiverInfoAdm=_HpnicfTransceiverInfoAdm_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,70,1))
_HpnicfTransceiverInfoTable_Object=MibTable
hpnicfTransceiverInfoTable=_HpnicfTransceiverInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1))
if mibBuilder.loadTexts:hpnicfTransceiverInfoTable.setStatus(_A)
_HpnicfTransceiverInfoEntry_Object=MibTableRow
hpnicfTransceiverInfoEntry=_HpnicfTransceiverInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1))
hpnicfTransceiverInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfTransceiverInfoEntry.setStatus(_A)
_HpnicfTransceiverHardwareType_Type=OctetString
_HpnicfTransceiverHardwareType_Object=MibTableColumn
hpnicfTransceiverHardwareType=_HpnicfTransceiverHardwareType_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,1),_HpnicfTransceiverHardwareType_Type())
hpnicfTransceiverHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverHardwareType.setStatus(_A)
_HpnicfTransceiverType_Type=OctetString
_HpnicfTransceiverType_Object=MibTableColumn
hpnicfTransceiverType=_HpnicfTransceiverType_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,2),_HpnicfTransceiverType_Type())
hpnicfTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverType.setStatus(_A)
_HpnicfTransceiverWaveLength_Type=Integer32
_HpnicfTransceiverWaveLength_Object=MibTableColumn
hpnicfTransceiverWaveLength=_HpnicfTransceiverWaveLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,3),_HpnicfTransceiverWaveLength_Type())
hpnicfTransceiverWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverWaveLength.setStatus(_A)
_HpnicfTransceiverVendorName_Type=OctetString
_HpnicfTransceiverVendorName_Object=MibTableColumn
hpnicfTransceiverVendorName=_HpnicfTransceiverVendorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,4),_HpnicfTransceiverVendorName_Type())
hpnicfTransceiverVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVendorName.setStatus(_A)
_HpnicfTransceiverSerialNumber_Type=OctetString
_HpnicfTransceiverSerialNumber_Object=MibTableColumn
hpnicfTransceiverSerialNumber=_HpnicfTransceiverSerialNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,5),_HpnicfTransceiverSerialNumber_Type())
hpnicfTransceiverSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverSerialNumber.setStatus(_A)
class _HpnicfTransceiverFiberDiameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,65535)));namedValues=NamedValues(*(('fiber9',1),('fiber50',2),('fiber625',3),('copper',4),('unknown',65535)))
_HpnicfTransceiverFiberDiameterType_Type.__name__=_E
_HpnicfTransceiverFiberDiameterType_Object=MibTableColumn
hpnicfTransceiverFiberDiameterType=_HpnicfTransceiverFiberDiameterType_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,6),_HpnicfTransceiverFiberDiameterType_Type())
hpnicfTransceiverFiberDiameterType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverFiberDiameterType.setStatus(_A)
_HpnicfTransceiverTransferDistance_Type=Integer32
_HpnicfTransceiverTransferDistance_Object=MibTableColumn
hpnicfTransceiverTransferDistance=_HpnicfTransceiverTransferDistance_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,7),_HpnicfTransceiverTransferDistance_Type())
hpnicfTransceiverTransferDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTransferDistance.setStatus(_A)
_HpnicfTransceiverDiagnostic_Type=TruthValue
_HpnicfTransceiverDiagnostic_Object=MibTableColumn
hpnicfTransceiverDiagnostic=_HpnicfTransceiverDiagnostic_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,8),_HpnicfTransceiverDiagnostic_Type())
hpnicfTransceiverDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverDiagnostic.setStatus(_A)
_HpnicfTransceiverCurTXPower_Type=Integer32
_HpnicfTransceiverCurTXPower_Object=MibTableColumn
hpnicfTransceiverCurTXPower=_HpnicfTransceiverCurTXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,9),_HpnicfTransceiverCurTXPower_Type())
hpnicfTransceiverCurTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverCurTXPower.setStatus(_A)
_HpnicfTransceiverMaxTXPower_Type=Integer32
_HpnicfTransceiverMaxTXPower_Object=MibTableColumn
hpnicfTransceiverMaxTXPower=_HpnicfTransceiverMaxTXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,10),_HpnicfTransceiverMaxTXPower_Type())
hpnicfTransceiverMaxTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverMaxTXPower.setStatus(_A)
_HpnicfTransceiverMinTXPower_Type=Integer32
_HpnicfTransceiverMinTXPower_Object=MibTableColumn
hpnicfTransceiverMinTXPower=_HpnicfTransceiverMinTXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,11),_HpnicfTransceiverMinTXPower_Type())
hpnicfTransceiverMinTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverMinTXPower.setStatus(_A)
_HpnicfTransceiverCurRXPower_Type=Integer32
_HpnicfTransceiverCurRXPower_Object=MibTableColumn
hpnicfTransceiverCurRXPower=_HpnicfTransceiverCurRXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,12),_HpnicfTransceiverCurRXPower_Type())
hpnicfTransceiverCurRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverCurRXPower.setStatus(_A)
_HpnicfTransceiverMaxRXPower_Type=Integer32
_HpnicfTransceiverMaxRXPower_Object=MibTableColumn
hpnicfTransceiverMaxRXPower=_HpnicfTransceiverMaxRXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,13),_HpnicfTransceiverMaxRXPower_Type())
hpnicfTransceiverMaxRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverMaxRXPower.setStatus(_A)
_HpnicfTransceiverMinRXPower_Type=Integer32
_HpnicfTransceiverMinRXPower_Object=MibTableColumn
hpnicfTransceiverMinRXPower=_HpnicfTransceiverMinRXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,14),_HpnicfTransceiverMinRXPower_Type())
hpnicfTransceiverMinRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverMinRXPower.setStatus(_A)
_HpnicfTransceiverTemperature_Type=Integer32
_HpnicfTransceiverTemperature_Object=MibTableColumn
hpnicfTransceiverTemperature=_HpnicfTransceiverTemperature_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,15),_HpnicfTransceiverTemperature_Type())
hpnicfTransceiverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTemperature.setStatus(_A)
_HpnicfTransceiverVoltage_Type=Integer32
_HpnicfTransceiverVoltage_Object=MibTableColumn
hpnicfTransceiverVoltage=_HpnicfTransceiverVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,16),_HpnicfTransceiverVoltage_Type())
hpnicfTransceiverVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVoltage.setStatus(_A)
_HpnicfTransceiverBiasCurrent_Type=Integer32
_HpnicfTransceiverBiasCurrent_Object=MibTableColumn
hpnicfTransceiverBiasCurrent=_HpnicfTransceiverBiasCurrent_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,17),_HpnicfTransceiverBiasCurrent_Type())
hpnicfTransceiverBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverBiasCurrent.setStatus(_A)
_HpnicfTransceiverTempHiAlarm_Type=Integer32
_HpnicfTransceiverTempHiAlarm_Object=MibTableColumn
hpnicfTransceiverTempHiAlarm=_HpnicfTransceiverTempHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,18),_HpnicfTransceiverTempHiAlarm_Type())
hpnicfTransceiverTempHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTempHiAlarm.setStatus(_A)
_HpnicfTransceiverTempLoAlarm_Type=Integer32
_HpnicfTransceiverTempLoAlarm_Object=MibTableColumn
hpnicfTransceiverTempLoAlarm=_HpnicfTransceiverTempLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,19),_HpnicfTransceiverTempLoAlarm_Type())
hpnicfTransceiverTempLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTempLoAlarm.setStatus(_A)
_HpnicfTransceiverTempHiWarn_Type=Integer32
_HpnicfTransceiverTempHiWarn_Object=MibTableColumn
hpnicfTransceiverTempHiWarn=_HpnicfTransceiverTempHiWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,20),_HpnicfTransceiverTempHiWarn_Type())
hpnicfTransceiverTempHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTempHiWarn.setStatus(_A)
_HpnicfTransceiverTempLoWarn_Type=Integer32
_HpnicfTransceiverTempLoWarn_Object=MibTableColumn
hpnicfTransceiverTempLoWarn=_HpnicfTransceiverTempLoWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,21),_HpnicfTransceiverTempLoWarn_Type())
hpnicfTransceiverTempLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverTempLoWarn.setStatus(_A)
_HpnicfTransceiverVccHiAlarm_Type=Integer32
_HpnicfTransceiverVccHiAlarm_Object=MibTableColumn
hpnicfTransceiverVccHiAlarm=_HpnicfTransceiverVccHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,22),_HpnicfTransceiverVccHiAlarm_Type())
hpnicfTransceiverVccHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVccHiAlarm.setStatus(_A)
_HpnicfTransceiverVccLoAlarm_Type=Integer32
_HpnicfTransceiverVccLoAlarm_Object=MibTableColumn
hpnicfTransceiverVccLoAlarm=_HpnicfTransceiverVccLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,23),_HpnicfTransceiverVccLoAlarm_Type())
hpnicfTransceiverVccLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVccLoAlarm.setStatus(_A)
_HpnicfTransceiverVccHiWarn_Type=Integer32
_HpnicfTransceiverVccHiWarn_Object=MibTableColumn
hpnicfTransceiverVccHiWarn=_HpnicfTransceiverVccHiWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,24),_HpnicfTransceiverVccHiWarn_Type())
hpnicfTransceiverVccHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVccHiWarn.setStatus(_A)
_HpnicfTransceiverVccLoWarn_Type=Integer32
_HpnicfTransceiverVccLoWarn_Object=MibTableColumn
hpnicfTransceiverVccLoWarn=_HpnicfTransceiverVccLoWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,25),_HpnicfTransceiverVccLoWarn_Type())
hpnicfTransceiverVccLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverVccLoWarn.setStatus(_A)
_HpnicfTransceiverBiasHiAlarm_Type=Integer32
_HpnicfTransceiverBiasHiAlarm_Object=MibTableColumn
hpnicfTransceiverBiasHiAlarm=_HpnicfTransceiverBiasHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,26),_HpnicfTransceiverBiasHiAlarm_Type())
hpnicfTransceiverBiasHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverBiasHiAlarm.setStatus(_A)
_HpnicfTransceiverBiasLoAlarm_Type=Integer32
_HpnicfTransceiverBiasLoAlarm_Object=MibTableColumn
hpnicfTransceiverBiasLoAlarm=_HpnicfTransceiverBiasLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,27),_HpnicfTransceiverBiasLoAlarm_Type())
hpnicfTransceiverBiasLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverBiasLoAlarm.setStatus(_A)
_HpnicfTransceiverBiasHiWarn_Type=Integer32
_HpnicfTransceiverBiasHiWarn_Object=MibTableColumn
hpnicfTransceiverBiasHiWarn=_HpnicfTransceiverBiasHiWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,28),_HpnicfTransceiverBiasHiWarn_Type())
hpnicfTransceiverBiasHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverBiasHiWarn.setStatus(_A)
_HpnicfTransceiverBiasLoWarn_Type=Integer32
_HpnicfTransceiverBiasLoWarn_Object=MibTableColumn
hpnicfTransceiverBiasLoWarn=_HpnicfTransceiverBiasLoWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,29),_HpnicfTransceiverBiasLoWarn_Type())
hpnicfTransceiverBiasLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverBiasLoWarn.setStatus(_A)
_HpnicfTransceiverPwrOutHiAlarm_Type=Integer32
_HpnicfTransceiverPwrOutHiAlarm_Object=MibTableColumn
hpnicfTransceiverPwrOutHiAlarm=_HpnicfTransceiverPwrOutHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,30),_HpnicfTransceiverPwrOutHiAlarm_Type())
hpnicfTransceiverPwrOutHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverPwrOutHiAlarm.setStatus(_A)
_HpnicfTransceiverPwrOutLoAlarm_Type=Integer32
_HpnicfTransceiverPwrOutLoAlarm_Object=MibTableColumn
hpnicfTransceiverPwrOutLoAlarm=_HpnicfTransceiverPwrOutLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,31),_HpnicfTransceiverPwrOutLoAlarm_Type())
hpnicfTransceiverPwrOutLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverPwrOutLoAlarm.setStatus(_A)
_HpnicfTransceiverPwrOutHiWarn_Type=Integer32
_HpnicfTransceiverPwrOutHiWarn_Object=MibTableColumn
hpnicfTransceiverPwrOutHiWarn=_HpnicfTransceiverPwrOutHiWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,32),_HpnicfTransceiverPwrOutHiWarn_Type())
hpnicfTransceiverPwrOutHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverPwrOutHiWarn.setStatus(_A)
_HpnicfTransceiverPwrOutLoWarn_Type=Integer32
_HpnicfTransceiverPwrOutLoWarn_Object=MibTableColumn
hpnicfTransceiverPwrOutLoWarn=_HpnicfTransceiverPwrOutLoWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,33),_HpnicfTransceiverPwrOutLoWarn_Type())
hpnicfTransceiverPwrOutLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverPwrOutLoWarn.setStatus(_A)
_HpnicfTransceiverRcvPwrHiAlarm_Type=Integer32
_HpnicfTransceiverRcvPwrHiAlarm_Object=MibTableColumn
hpnicfTransceiverRcvPwrHiAlarm=_HpnicfTransceiverRcvPwrHiAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,34),_HpnicfTransceiverRcvPwrHiAlarm_Type())
hpnicfTransceiverRcvPwrHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverRcvPwrHiAlarm.setStatus(_A)
_HpnicfTransceiverRcvPwrLoAlarm_Type=Integer32
_HpnicfTransceiverRcvPwrLoAlarm_Object=MibTableColumn
hpnicfTransceiverRcvPwrLoAlarm=_HpnicfTransceiverRcvPwrLoAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,35),_HpnicfTransceiverRcvPwrLoAlarm_Type())
hpnicfTransceiverRcvPwrLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverRcvPwrLoAlarm.setStatus(_A)
_HpnicfTransceiverRcvPwrHiWarn_Type=Integer32
_HpnicfTransceiverRcvPwrHiWarn_Object=MibTableColumn
hpnicfTransceiverRcvPwrHiWarn=_HpnicfTransceiverRcvPwrHiWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,36),_HpnicfTransceiverRcvPwrHiWarn_Type())
hpnicfTransceiverRcvPwrHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverRcvPwrHiWarn.setStatus(_A)
_HpnicfTransceiverRcvPwrLoWarn_Type=Integer32
_HpnicfTransceiverRcvPwrLoWarn_Object=MibTableColumn
hpnicfTransceiverRcvPwrLoWarn=_HpnicfTransceiverRcvPwrLoWarn_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,37),_HpnicfTransceiverRcvPwrLoWarn_Type())
hpnicfTransceiverRcvPwrLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverRcvPwrLoWarn.setStatus(_A)
class _HpnicfTransceiverErrors_Type(Bits):namedValues=NamedValues(*(('xcvrIOError',0),('xcvrChecksum',1),('xcvrTypeAndPortConfigMismatch',2),('xcvrTypeNotSupported',3),('wisLocalFault',4),('rcvOpticalPowerFault',5),('pmapmdReceiverLocalFault',6),('pcsReceiveLocalFault',7),('phyXSReceiveLocalFault',8),('laserBiasCurrentFault',9),('laserTemperatureFault',10),('laserOutputPowerFault',11),('txFault',12),('pmapmdTransmitterLocalFault',13),('pcsTransmitLocalFault',14),('phyXSTransmitLocalFault',15),('rxLossOfSignal',16)))
_HpnicfTransceiverErrors_Type.__name__='Bits'
_HpnicfTransceiverErrors_Object=MibTableColumn
hpnicfTransceiverErrors=_HpnicfTransceiverErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,1,1,38),_HpnicfTransceiverErrors_Type())
hpnicfTransceiverErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverErrors.setStatus(_A)
_HpnicfTransceiverChannelTable_Object=MibTable
hpnicfTransceiverChannelTable=_HpnicfTransceiverChannelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2))
if mibBuilder.loadTexts:hpnicfTransceiverChannelTable.setStatus(_A)
_HpnicfTransceiverChannelEntry_Object=MibTableRow
hpnicfTransceiverChannelEntry=_HpnicfTransceiverChannelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1))
hpnicfTransceiverChannelEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:hpnicfTransceiverChannelEntry.setStatus(_A)
class _HpnicfTransceiverChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfTransceiverChannelIndex_Type.__name__=_E
_HpnicfTransceiverChannelIndex_Object=MibTableColumn
hpnicfTransceiverChannelIndex=_HpnicfTransceiverChannelIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1,1),_HpnicfTransceiverChannelIndex_Type())
hpnicfTransceiverChannelIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfTransceiverChannelIndex.setStatus(_A)
_HpnicfTransceiverChannelCurTXPower_Type=Integer32
_HpnicfTransceiverChannelCurTXPower_Object=MibTableColumn
hpnicfTransceiverChannelCurTXPower=_HpnicfTransceiverChannelCurTXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1,2),_HpnicfTransceiverChannelCurTXPower_Type())
hpnicfTransceiverChannelCurTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverChannelCurTXPower.setStatus(_A)
_HpnicfTransceiverChannelCurRXPower_Type=Integer32
_HpnicfTransceiverChannelCurRXPower_Object=MibTableColumn
hpnicfTransceiverChannelCurRXPower=_HpnicfTransceiverChannelCurRXPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1,3),_HpnicfTransceiverChannelCurRXPower_Type())
hpnicfTransceiverChannelCurRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverChannelCurRXPower.setStatus(_A)
_HpnicfTransceiverChannelTemperature_Type=Integer32
_HpnicfTransceiverChannelTemperature_Object=MibTableColumn
hpnicfTransceiverChannelTemperature=_HpnicfTransceiverChannelTemperature_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1,4),_HpnicfTransceiverChannelTemperature_Type())
hpnicfTransceiverChannelTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverChannelTemperature.setStatus(_A)
_HpnicfTransceiverChannelBiasCurrent_Type=Integer32
_HpnicfTransceiverChannelBiasCurrent_Object=MibTableColumn
hpnicfTransceiverChannelBiasCurrent=_HpnicfTransceiverChannelBiasCurrent_Object((1,3,6,1,4,1,11,2,14,11,15,2,70,1,2,1,5),_HpnicfTransceiverChannelBiasCurrent_Type())
hpnicfTransceiverChannelBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTransceiverChannelBiasCurrent.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hpnicfTransceiver':hpnicfTransceiver,'hpnicfTransceiverInfoAdm':hpnicfTransceiverInfoAdm,'hpnicfTransceiverInfoTable':hpnicfTransceiverInfoTable,'hpnicfTransceiverInfoEntry':hpnicfTransceiverInfoEntry,'hpnicfTransceiverHardwareType':hpnicfTransceiverHardwareType,'hpnicfTransceiverType':hpnicfTransceiverType,'hpnicfTransceiverWaveLength':hpnicfTransceiverWaveLength,'hpnicfTransceiverVendorName':hpnicfTransceiverVendorName,'hpnicfTransceiverSerialNumber':hpnicfTransceiverSerialNumber,'hpnicfTransceiverFiberDiameterType':hpnicfTransceiverFiberDiameterType,'hpnicfTransceiverTransferDistance':hpnicfTransceiverTransferDistance,'hpnicfTransceiverDiagnostic':hpnicfTransceiverDiagnostic,'hpnicfTransceiverCurTXPower':hpnicfTransceiverCurTXPower,'hpnicfTransceiverMaxTXPower':hpnicfTransceiverMaxTXPower,'hpnicfTransceiverMinTXPower':hpnicfTransceiverMinTXPower,'hpnicfTransceiverCurRXPower':hpnicfTransceiverCurRXPower,'hpnicfTransceiverMaxRXPower':hpnicfTransceiverMaxRXPower,'hpnicfTransceiverMinRXPower':hpnicfTransceiverMinRXPower,'hpnicfTransceiverTemperature':hpnicfTransceiverTemperature,'hpnicfTransceiverVoltage':hpnicfTransceiverVoltage,'hpnicfTransceiverBiasCurrent':hpnicfTransceiverBiasCurrent,'hpnicfTransceiverTempHiAlarm':hpnicfTransceiverTempHiAlarm,'hpnicfTransceiverTempLoAlarm':hpnicfTransceiverTempLoAlarm,'hpnicfTransceiverTempHiWarn':hpnicfTransceiverTempHiWarn,'hpnicfTransceiverTempLoWarn':hpnicfTransceiverTempLoWarn,'hpnicfTransceiverVccHiAlarm':hpnicfTransceiverVccHiAlarm,'hpnicfTransceiverVccLoAlarm':hpnicfTransceiverVccLoAlarm,'hpnicfTransceiverVccHiWarn':hpnicfTransceiverVccHiWarn,'hpnicfTransceiverVccLoWarn':hpnicfTransceiverVccLoWarn,'hpnicfTransceiverBiasHiAlarm':hpnicfTransceiverBiasHiAlarm,'hpnicfTransceiverBiasLoAlarm':hpnicfTransceiverBiasLoAlarm,'hpnicfTransceiverBiasHiWarn':hpnicfTransceiverBiasHiWarn,'hpnicfTransceiverBiasLoWarn':hpnicfTransceiverBiasLoWarn,'hpnicfTransceiverPwrOutHiAlarm':hpnicfTransceiverPwrOutHiAlarm,'hpnicfTransceiverPwrOutLoAlarm':hpnicfTransceiverPwrOutLoAlarm,'hpnicfTransceiverPwrOutHiWarn':hpnicfTransceiverPwrOutHiWarn,'hpnicfTransceiverPwrOutLoWarn':hpnicfTransceiverPwrOutLoWarn,'hpnicfTransceiverRcvPwrHiAlarm':hpnicfTransceiverRcvPwrHiAlarm,'hpnicfTransceiverRcvPwrLoAlarm':hpnicfTransceiverRcvPwrLoAlarm,'hpnicfTransceiverRcvPwrHiWarn':hpnicfTransceiverRcvPwrHiWarn,'hpnicfTransceiverRcvPwrLoWarn':hpnicfTransceiverRcvPwrLoWarn,'hpnicfTransceiverErrors':hpnicfTransceiverErrors,'hpnicfTransceiverChannelTable':hpnicfTransceiverChannelTable,'hpnicfTransceiverChannelEntry':hpnicfTransceiverChannelEntry,_G:hpnicfTransceiverChannelIndex,'hpnicfTransceiverChannelCurTXPower':hpnicfTransceiverChannelCurTXPower,'hpnicfTransceiverChannelCurRXPower':hpnicfTransceiverChannelCurRXPower,'hpnicfTransceiverChannelTemperature':hpnicfTransceiverChannelTemperature,'hpnicfTransceiverChannelBiasCurrent':hpnicfTransceiverChannelBiasCurrent})