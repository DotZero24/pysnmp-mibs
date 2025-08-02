_K='h3cTransceiverITUChanIdx'
_J='not-accessible'
_I='h3cTransceiverChannelIndex'
_H='H3C-TRANSCEIVER-INFO-MIB'
_G='Unsigned32'
_F='Integer32'
_E='OctetString'
_D='ifIndex'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cTransceiver=ModuleIdentity((1,3,6,1,4,1,2011,10,2,70))
if mibBuilder.loadTexts:h3cTransceiver.setRevisions(('2018-01-03 00:00','2016-03-09 00:00','2015-12-25 00:00','2014-08-11 10:50','2013-06-06 00:00','2012-06-06 00:00','2009-12-29 00:00','2006-06-08 00:00','2006-01-10 00:00'))
_H3cTransceiverInfoAdm_ObjectIdentity=ObjectIdentity
h3cTransceiverInfoAdm=_H3cTransceiverInfoAdm_ObjectIdentity((1,3,6,1,4,1,2011,10,2,70,1))
_H3cTransceiverInfoTable_Object=MibTable
h3cTransceiverInfoTable=_H3cTransceiverInfoTable_Object((1,3,6,1,4,1,2011,10,2,70,1,1))
if mibBuilder.loadTexts:h3cTransceiverInfoTable.setStatus(_A)
_H3cTransceiverInfoEntry_Object=MibTableRow
h3cTransceiverInfoEntry=_H3cTransceiverInfoEntry_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1))
h3cTransceiverInfoEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:h3cTransceiverInfoEntry.setStatus(_A)
_H3cTransceiverHardwareType_Type=OctetString
_H3cTransceiverHardwareType_Object=MibTableColumn
h3cTransceiverHardwareType=_H3cTransceiverHardwareType_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,1),_H3cTransceiverHardwareType_Type())
h3cTransceiverHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverHardwareType.setStatus(_A)
_H3cTransceiverType_Type=OctetString
_H3cTransceiverType_Object=MibTableColumn
h3cTransceiverType=_H3cTransceiverType_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,2),_H3cTransceiverType_Type())
h3cTransceiverType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverType.setStatus(_A)
_H3cTransceiverWaveLength_Type=Integer32
_H3cTransceiverWaveLength_Object=MibTableColumn
h3cTransceiverWaveLength=_H3cTransceiverWaveLength_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,3),_H3cTransceiverWaveLength_Type())
h3cTransceiverWaveLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverWaveLength.setStatus(_A)
_H3cTransceiverVendorName_Type=OctetString
_H3cTransceiverVendorName_Object=MibTableColumn
h3cTransceiverVendorName=_H3cTransceiverVendorName_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,4),_H3cTransceiverVendorName_Type())
h3cTransceiverVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVendorName.setStatus(_A)
_H3cTransceiverSerialNumber_Type=OctetString
_H3cTransceiverSerialNumber_Object=MibTableColumn
h3cTransceiverSerialNumber=_H3cTransceiverSerialNumber_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,5),_H3cTransceiverSerialNumber_Type())
h3cTransceiverSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverSerialNumber.setStatus(_A)
class _H3cTransceiverFiberDiameterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,65535)));namedValues=NamedValues(*(('fiber9',1),('fiber50',2),('fiber625',3),('copper',4),('unknown',65535)))
_H3cTransceiverFiberDiameterType_Type.__name__=_F
_H3cTransceiverFiberDiameterType_Object=MibTableColumn
h3cTransceiverFiberDiameterType=_H3cTransceiverFiberDiameterType_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,6),_H3cTransceiverFiberDiameterType_Type())
h3cTransceiverFiberDiameterType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverFiberDiameterType.setStatus(_A)
_H3cTransceiverTransferDistance_Type=Integer32
_H3cTransceiverTransferDistance_Object=MibTableColumn
h3cTransceiverTransferDistance=_H3cTransceiverTransferDistance_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,7),_H3cTransceiverTransferDistance_Type())
h3cTransceiverTransferDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTransferDistance.setStatus(_A)
_H3cTransceiverDiagnostic_Type=TruthValue
_H3cTransceiverDiagnostic_Object=MibTableColumn
h3cTransceiverDiagnostic=_H3cTransceiverDiagnostic_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,8),_H3cTransceiverDiagnostic_Type())
h3cTransceiverDiagnostic.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverDiagnostic.setStatus(_A)
_H3cTransceiverCurTXPower_Type=Integer32
_H3cTransceiverCurTXPower_Object=MibTableColumn
h3cTransceiverCurTXPower=_H3cTransceiverCurTXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,9),_H3cTransceiverCurTXPower_Type())
h3cTransceiverCurTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurTXPower.setStatus(_A)
_H3cTransceiverMaxTXPower_Type=Integer32
_H3cTransceiverMaxTXPower_Object=MibTableColumn
h3cTransceiverMaxTXPower=_H3cTransceiverMaxTXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,10),_H3cTransceiverMaxTXPower_Type())
h3cTransceiverMaxTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMaxTXPower.setStatus(_A)
_H3cTransceiverMinTXPower_Type=Integer32
_H3cTransceiverMinTXPower_Object=MibTableColumn
h3cTransceiverMinTXPower=_H3cTransceiverMinTXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,11),_H3cTransceiverMinTXPower_Type())
h3cTransceiverMinTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMinTXPower.setStatus(_A)
_H3cTransceiverCurRXPower_Type=Integer32
_H3cTransceiverCurRXPower_Object=MibTableColumn
h3cTransceiverCurRXPower=_H3cTransceiverCurRXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,12),_H3cTransceiverCurRXPower_Type())
h3cTransceiverCurRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurRXPower.setStatus(_A)
_H3cTransceiverMaxRXPower_Type=Integer32
_H3cTransceiverMaxRXPower_Object=MibTableColumn
h3cTransceiverMaxRXPower=_H3cTransceiverMaxRXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,13),_H3cTransceiverMaxRXPower_Type())
h3cTransceiverMaxRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMaxRXPower.setStatus(_A)
_H3cTransceiverMinRXPower_Type=Integer32
_H3cTransceiverMinRXPower_Object=MibTableColumn
h3cTransceiverMinRXPower=_H3cTransceiverMinRXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,14),_H3cTransceiverMinRXPower_Type())
h3cTransceiverMinRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverMinRXPower.setStatus(_A)
_H3cTransceiverTemperature_Type=Integer32
_H3cTransceiverTemperature_Object=MibTableColumn
h3cTransceiverTemperature=_H3cTransceiverTemperature_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,15),_H3cTransceiverTemperature_Type())
h3cTransceiverTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTemperature.setStatus(_A)
_H3cTransceiverVoltage_Type=Integer32
_H3cTransceiverVoltage_Object=MibTableColumn
h3cTransceiverVoltage=_H3cTransceiverVoltage_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,16),_H3cTransceiverVoltage_Type())
h3cTransceiverVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVoltage.setStatus(_A)
_H3cTransceiverBiasCurrent_Type=Integer32
_H3cTransceiverBiasCurrent_Object=MibTableColumn
h3cTransceiverBiasCurrent=_H3cTransceiverBiasCurrent_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,17),_H3cTransceiverBiasCurrent_Type())
h3cTransceiverBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasCurrent.setStatus(_A)
_H3cTransceiverTempHiAlarm_Type=Integer32
_H3cTransceiverTempHiAlarm_Object=MibTableColumn
h3cTransceiverTempHiAlarm=_H3cTransceiverTempHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,18),_H3cTransceiverTempHiAlarm_Type())
h3cTransceiverTempHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTempHiAlarm.setStatus(_A)
_H3cTransceiverTempLoAlarm_Type=Integer32
_H3cTransceiverTempLoAlarm_Object=MibTableColumn
h3cTransceiverTempLoAlarm=_H3cTransceiverTempLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,19),_H3cTransceiverTempLoAlarm_Type())
h3cTransceiverTempLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTempLoAlarm.setStatus(_A)
_H3cTransceiverTempHiWarn_Type=Integer32
_H3cTransceiverTempHiWarn_Object=MibTableColumn
h3cTransceiverTempHiWarn=_H3cTransceiverTempHiWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,20),_H3cTransceiverTempHiWarn_Type())
h3cTransceiverTempHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTempHiWarn.setStatus(_A)
_H3cTransceiverTempLoWarn_Type=Integer32
_H3cTransceiverTempLoWarn_Object=MibTableColumn
h3cTransceiverTempLoWarn=_H3cTransceiverTempLoWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,21),_H3cTransceiverTempLoWarn_Type())
h3cTransceiverTempLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverTempLoWarn.setStatus(_A)
_H3cTransceiverVccHiAlarm_Type=Integer32
_H3cTransceiverVccHiAlarm_Object=MibTableColumn
h3cTransceiverVccHiAlarm=_H3cTransceiverVccHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,22),_H3cTransceiverVccHiAlarm_Type())
h3cTransceiverVccHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVccHiAlarm.setStatus(_A)
_H3cTransceiverVccLoAlarm_Type=Integer32
_H3cTransceiverVccLoAlarm_Object=MibTableColumn
h3cTransceiverVccLoAlarm=_H3cTransceiverVccLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,23),_H3cTransceiverVccLoAlarm_Type())
h3cTransceiverVccLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVccLoAlarm.setStatus(_A)
_H3cTransceiverVccHiWarn_Type=Integer32
_H3cTransceiverVccHiWarn_Object=MibTableColumn
h3cTransceiverVccHiWarn=_H3cTransceiverVccHiWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,24),_H3cTransceiverVccHiWarn_Type())
h3cTransceiverVccHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVccHiWarn.setStatus(_A)
_H3cTransceiverVccLoWarn_Type=Integer32
_H3cTransceiverVccLoWarn_Object=MibTableColumn
h3cTransceiverVccLoWarn=_H3cTransceiverVccLoWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,25),_H3cTransceiverVccLoWarn_Type())
h3cTransceiverVccLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVccLoWarn.setStatus(_A)
_H3cTransceiverBiasHiAlarm_Type=Integer32
_H3cTransceiverBiasHiAlarm_Object=MibTableColumn
h3cTransceiverBiasHiAlarm=_H3cTransceiverBiasHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,26),_H3cTransceiverBiasHiAlarm_Type())
h3cTransceiverBiasHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasHiAlarm.setStatus(_A)
_H3cTransceiverBiasLoAlarm_Type=Integer32
_H3cTransceiverBiasLoAlarm_Object=MibTableColumn
h3cTransceiverBiasLoAlarm=_H3cTransceiverBiasLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,27),_H3cTransceiverBiasLoAlarm_Type())
h3cTransceiverBiasLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasLoAlarm.setStatus(_A)
_H3cTransceiverBiasHiWarn_Type=Integer32
_H3cTransceiverBiasHiWarn_Object=MibTableColumn
h3cTransceiverBiasHiWarn=_H3cTransceiverBiasHiWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,28),_H3cTransceiverBiasHiWarn_Type())
h3cTransceiverBiasHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasHiWarn.setStatus(_A)
_H3cTransceiverBiasLoWarn_Type=Integer32
_H3cTransceiverBiasLoWarn_Object=MibTableColumn
h3cTransceiverBiasLoWarn=_H3cTransceiverBiasLoWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,29),_H3cTransceiverBiasLoWarn_Type())
h3cTransceiverBiasLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverBiasLoWarn.setStatus(_A)
_H3cTransceiverPwrOutHiAlarm_Type=Integer32
_H3cTransceiverPwrOutHiAlarm_Object=MibTableColumn
h3cTransceiverPwrOutHiAlarm=_H3cTransceiverPwrOutHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,30),_H3cTransceiverPwrOutHiAlarm_Type())
h3cTransceiverPwrOutHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverPwrOutHiAlarm.setStatus(_A)
_H3cTransceiverPwrOutLoAlarm_Type=Integer32
_H3cTransceiverPwrOutLoAlarm_Object=MibTableColumn
h3cTransceiverPwrOutLoAlarm=_H3cTransceiverPwrOutLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,31),_H3cTransceiverPwrOutLoAlarm_Type())
h3cTransceiverPwrOutLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverPwrOutLoAlarm.setStatus(_A)
_H3cTransceiverPwrOutHiWarn_Type=Integer32
_H3cTransceiverPwrOutHiWarn_Object=MibTableColumn
h3cTransceiverPwrOutHiWarn=_H3cTransceiverPwrOutHiWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,32),_H3cTransceiverPwrOutHiWarn_Type())
h3cTransceiverPwrOutHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverPwrOutHiWarn.setStatus(_A)
_H3cTransceiverPwrOutLoWarn_Type=Integer32
_H3cTransceiverPwrOutLoWarn_Object=MibTableColumn
h3cTransceiverPwrOutLoWarn=_H3cTransceiverPwrOutLoWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,33),_H3cTransceiverPwrOutLoWarn_Type())
h3cTransceiverPwrOutLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverPwrOutLoWarn.setStatus(_A)
_H3cTransceiverRcvPwrHiAlarm_Type=Integer32
_H3cTransceiverRcvPwrHiAlarm_Object=MibTableColumn
h3cTransceiverRcvPwrHiAlarm=_H3cTransceiverRcvPwrHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,34),_H3cTransceiverRcvPwrHiAlarm_Type())
h3cTransceiverRcvPwrHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverRcvPwrHiAlarm.setStatus(_A)
_H3cTransceiverRcvPwrLoAlarm_Type=Integer32
_H3cTransceiverRcvPwrLoAlarm_Object=MibTableColumn
h3cTransceiverRcvPwrLoAlarm=_H3cTransceiverRcvPwrLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,35),_H3cTransceiverRcvPwrLoAlarm_Type())
h3cTransceiverRcvPwrLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverRcvPwrLoAlarm.setStatus(_A)
_H3cTransceiverRcvPwrHiWarn_Type=Integer32
_H3cTransceiverRcvPwrHiWarn_Object=MibTableColumn
h3cTransceiverRcvPwrHiWarn=_H3cTransceiverRcvPwrHiWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,36),_H3cTransceiverRcvPwrHiWarn_Type())
h3cTransceiverRcvPwrHiWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverRcvPwrHiWarn.setStatus(_A)
_H3cTransceiverRcvPwrLoWarn_Type=Integer32
_H3cTransceiverRcvPwrLoWarn_Object=MibTableColumn
h3cTransceiverRcvPwrLoWarn=_H3cTransceiverRcvPwrLoWarn_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,37),_H3cTransceiverRcvPwrLoWarn_Type())
h3cTransceiverRcvPwrLoWarn.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverRcvPwrLoWarn.setStatus(_A)
class _H3cTransceiverErrors_Type(Bits):namedValues=NamedValues(*(('xcvrIOError',0),('xcvrChecksum',1),('xcvrTypeAndPortConfigMismatch',2),('xcvrTypeNotSupported',3),('wisLocalFault',4),('rcvOpticalPowerFault',5),('pmapmdReceiverLocalFault',6),('pcsReceiveLocalFault',7),('phyXSReceiveLocalFault',8),('laserBiasCurrentFault',9),('laserTemperatureFault',10),('laserOutputPowerFault',11),('txFault',12),('pmapmdTransmitterLocalFault',13),('pcsTransmitLocalFault',14),('phyXSTransmitLocalFault',15),('rxLossOfSignal',16),('tecError',17),('wavelengthUnlocked',18),('txIsNotReadyDueToTuning',19)))
_H3cTransceiverErrors_Type.__name__='Bits'
_H3cTransceiverErrors_Object=MibTableColumn
h3cTransceiverErrors=_H3cTransceiverErrors_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,38),_H3cTransceiverErrors_Type())
h3cTransceiverErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverErrors.setStatus(_A)
class _H3cTransceiverVendorOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cTransceiverVendorOUI_Type.__name__=_E
_H3cTransceiverVendorOUI_Object=MibTableColumn
h3cTransceiverVendorOUI=_H3cTransceiverVendorOUI_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,39),_H3cTransceiverVendorOUI_Type())
h3cTransceiverVendorOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverVendorOUI.setStatus(_A)
class _H3cTransceiverRevisionNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cTransceiverRevisionNumber_Type.__name__=_E
_H3cTransceiverRevisionNumber_Object=MibTableColumn
h3cTransceiverRevisionNumber=_H3cTransceiverRevisionNumber_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,40),_H3cTransceiverRevisionNumber_Type())
h3cTransceiverRevisionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverRevisionNumber.setStatus(_A)
_H3cTransceiverFrequency_Type=Integer32
_H3cTransceiverFrequency_Object=MibTableColumn
h3cTransceiverFrequency=_H3cTransceiverFrequency_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,41),_H3cTransceiverFrequency_Type())
h3cTransceiverFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverFrequency.setStatus(_A)
class _H3cTransceiverActiveITUChannel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cTransceiverActiveITUChannel_Type.__name__=_G
_H3cTransceiverActiveITUChannel_Object=MibTableColumn
h3cTransceiverActiveITUChannel=_H3cTransceiverActiveITUChannel_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,42),_H3cTransceiverActiveITUChannel_Type())
h3cTransceiverActiveITUChannel.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cTransceiverActiveITUChannel.setStatus(_A)
_H3cTransceiverCurWaveErr_Type=Integer32
_H3cTransceiverCurWaveErr_Object=MibTableColumn
h3cTransceiverCurWaveErr=_H3cTransceiverCurWaveErr_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,43),_H3cTransceiverCurWaveErr_Type())
h3cTransceiverCurWaveErr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurWaveErr.setStatus(_A)
_H3cTransceiverWaveErrHiAlarm_Type=Integer32
_H3cTransceiverWaveErrHiAlarm_Object=MibTableColumn
h3cTransceiverWaveErrHiAlarm=_H3cTransceiverWaveErrHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,44),_H3cTransceiverWaveErrHiAlarm_Type())
h3cTransceiverWaveErrHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverWaveErrHiAlarm.setStatus(_A)
_H3cTransceiverWaveErrLoAlarm_Type=Integer32
_H3cTransceiverWaveErrLoAlarm_Object=MibTableColumn
h3cTransceiverWaveErrLoAlarm=_H3cTransceiverWaveErrLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,45),_H3cTransceiverWaveErrLoAlarm_Type())
h3cTransceiverWaveErrLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverWaveErrLoAlarm.setStatus(_A)
_H3cTransceiverCurFreqErr_Type=Integer32
_H3cTransceiverCurFreqErr_Object=MibTableColumn
h3cTransceiverCurFreqErr=_H3cTransceiverCurFreqErr_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,46),_H3cTransceiverCurFreqErr_Type())
h3cTransceiverCurFreqErr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverCurFreqErr.setStatus(_A)
_H3cTransceiverFreqErrHiAlarm_Type=Integer32
_H3cTransceiverFreqErrHiAlarm_Object=MibTableColumn
h3cTransceiverFreqErrHiAlarm=_H3cTransceiverFreqErrHiAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,47),_H3cTransceiverFreqErrHiAlarm_Type())
h3cTransceiverFreqErrHiAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverFreqErrHiAlarm.setStatus(_A)
_H3cTransceiverFreqErrLoAlarm_Type=Integer32
_H3cTransceiverFreqErrLoAlarm_Object=MibTableColumn
h3cTransceiverFreqErrLoAlarm=_H3cTransceiverFreqErrLoAlarm_Object((1,3,6,1,4,1,2011,10,2,70,1,1,1,48),_H3cTransceiverFreqErrLoAlarm_Type())
h3cTransceiverFreqErrLoAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverFreqErrLoAlarm.setStatus(_A)
_H3cTransceiverChannelTable_Object=MibTable
h3cTransceiverChannelTable=_H3cTransceiverChannelTable_Object((1,3,6,1,4,1,2011,10,2,70,1,2))
if mibBuilder.loadTexts:h3cTransceiverChannelTable.setStatus(_A)
_H3cTransceiverChannelEntry_Object=MibTableRow
h3cTransceiverChannelEntry=_H3cTransceiverChannelEntry_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1))
h3cTransceiverChannelEntry.setIndexNames((0,_C,_D),(0,_H,_I))
if mibBuilder.loadTexts:h3cTransceiverChannelEntry.setStatus(_A)
class _H3cTransceiverChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cTransceiverChannelIndex_Type.__name__=_F
_H3cTransceiverChannelIndex_Object=MibTableColumn
h3cTransceiverChannelIndex=_H3cTransceiverChannelIndex_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,1),_H3cTransceiverChannelIndex_Type())
h3cTransceiverChannelIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTransceiverChannelIndex.setStatus(_A)
_H3cTransceiverChannelCurTXPower_Type=Integer32
_H3cTransceiverChannelCurTXPower_Object=MibTableColumn
h3cTransceiverChannelCurTXPower=_H3cTransceiverChannelCurTXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,2),_H3cTransceiverChannelCurTXPower_Type())
h3cTransceiverChannelCurTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelCurTXPower.setStatus(_A)
_H3cTransceiverChannelCurRXPower_Type=Integer32
_H3cTransceiverChannelCurRXPower_Object=MibTableColumn
h3cTransceiverChannelCurRXPower=_H3cTransceiverChannelCurRXPower_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,3),_H3cTransceiverChannelCurRXPower_Type())
h3cTransceiverChannelCurRXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelCurRXPower.setStatus(_A)
_H3cTransceiverChannelTemperature_Type=Integer32
_H3cTransceiverChannelTemperature_Object=MibTableColumn
h3cTransceiverChannelTemperature=_H3cTransceiverChannelTemperature_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,4),_H3cTransceiverChannelTemperature_Type())
h3cTransceiverChannelTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelTemperature.setStatus(_A)
_H3cTransceiverChannelBiasCurrent_Type=Integer32
_H3cTransceiverChannelBiasCurrent_Object=MibTableColumn
h3cTransceiverChannelBiasCurrent=_H3cTransceiverChannelBiasCurrent_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,5),_H3cTransceiverChannelBiasCurrent_Type())
h3cTransceiverChannelBiasCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelBiasCurrent.setStatus(_A)
_H3cTransceiverChannelBiasHiAm_Type=Integer32
_H3cTransceiverChannelBiasHiAm_Object=MibTableColumn
h3cTransceiverChannelBiasHiAm=_H3cTransceiverChannelBiasHiAm_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,6),_H3cTransceiverChannelBiasHiAm_Type())
h3cTransceiverChannelBiasHiAm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelBiasHiAm.setStatus(_A)
_H3cTransceiverChannelBiasLoAm_Type=Integer32
_H3cTransceiverChannelBiasLoAm_Object=MibTableColumn
h3cTransceiverChannelBiasLoAm=_H3cTransceiverChannelBiasLoAm_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,7),_H3cTransceiverChannelBiasLoAm_Type())
h3cTransceiverChannelBiasLoAm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelBiasLoAm.setStatus(_A)
_H3cTransceiverChannelTXPwrHiAm_Type=Integer32
_H3cTransceiverChannelTXPwrHiAm_Object=MibTableColumn
h3cTransceiverChannelTXPwrHiAm=_H3cTransceiverChannelTXPwrHiAm_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,8),_H3cTransceiverChannelTXPwrHiAm_Type())
h3cTransceiverChannelTXPwrHiAm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelTXPwrHiAm.setStatus(_A)
_H3cTransceiverChannelTXPwrLoAm_Type=Integer32
_H3cTransceiverChannelTXPwrLoAm_Object=MibTableColumn
h3cTransceiverChannelTXPwrLoAm=_H3cTransceiverChannelTXPwrLoAm_Object((1,3,6,1,4,1,2011,10,2,70,1,2,1,9),_H3cTransceiverChannelTXPwrLoAm_Type())
h3cTransceiverChannelTXPwrLoAm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverChannelTXPwrLoAm.setStatus(_A)
_H3cTransceiverITUChanTable_Object=MibTable
h3cTransceiverITUChanTable=_H3cTransceiverITUChanTable_Object((1,3,6,1,4,1,2011,10,2,70,1,3))
if mibBuilder.loadTexts:h3cTransceiverITUChanTable.setStatus(_A)
_H3cTransceiverITUChanEntry_Object=MibTableRow
h3cTransceiverITUChanEntry=_H3cTransceiverITUChanEntry_Object((1,3,6,1,4,1,2011,10,2,70,1,3,1))
h3cTransceiverITUChanEntry.setIndexNames((0,_C,_D),(0,_H,_K))
if mibBuilder.loadTexts:h3cTransceiverITUChanEntry.setStatus(_A)
class _H3cTransceiverITUChanIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cTransceiverITUChanIdx_Type.__name__=_G
_H3cTransceiverITUChanIdx_Object=MibTableColumn
h3cTransceiverITUChanIdx=_H3cTransceiverITUChanIdx_Object((1,3,6,1,4,1,2011,10,2,70,1,3,1,1),_H3cTransceiverITUChanIdx_Type())
h3cTransceiverITUChanIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cTransceiverITUChanIdx.setStatus(_A)
_H3cTransceiverITUChanFreq_Type=Integer32
_H3cTransceiverITUChanFreq_Object=MibTableColumn
h3cTransceiverITUChanFreq=_H3cTransceiverITUChanFreq_Object((1,3,6,1,4,1,2011,10,2,70,1,3,1,2),_H3cTransceiverITUChanFreq_Type())
h3cTransceiverITUChanFreq.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverITUChanFreq.setStatus(_A)
_H3cTransceiverITUChanWaveLth_Type=Integer32
_H3cTransceiverITUChanWaveLth_Object=MibTableColumn
h3cTransceiverITUChanWaveLth=_H3cTransceiverITUChanWaveLth_Object((1,3,6,1,4,1,2011,10,2,70,1,3,1,3),_H3cTransceiverITUChanWaveLth_Type())
h3cTransceiverITUChanWaveLth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cTransceiverITUChanWaveLth.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'h3cTransceiver':h3cTransceiver,'h3cTransceiverInfoAdm':h3cTransceiverInfoAdm,'h3cTransceiverInfoTable':h3cTransceiverInfoTable,'h3cTransceiverInfoEntry':h3cTransceiverInfoEntry,'h3cTransceiverHardwareType':h3cTransceiverHardwareType,'h3cTransceiverType':h3cTransceiverType,'h3cTransceiverWaveLength':h3cTransceiverWaveLength,'h3cTransceiverVendorName':h3cTransceiverVendorName,'h3cTransceiverSerialNumber':h3cTransceiverSerialNumber,'h3cTransceiverFiberDiameterType':h3cTransceiverFiberDiameterType,'h3cTransceiverTransferDistance':h3cTransceiverTransferDistance,'h3cTransceiverDiagnostic':h3cTransceiverDiagnostic,'h3cTransceiverCurTXPower':h3cTransceiverCurTXPower,'h3cTransceiverMaxTXPower':h3cTransceiverMaxTXPower,'h3cTransceiverMinTXPower':h3cTransceiverMinTXPower,'h3cTransceiverCurRXPower':h3cTransceiverCurRXPower,'h3cTransceiverMaxRXPower':h3cTransceiverMaxRXPower,'h3cTransceiverMinRXPower':h3cTransceiverMinRXPower,'h3cTransceiverTemperature':h3cTransceiverTemperature,'h3cTransceiverVoltage':h3cTransceiverVoltage,'h3cTransceiverBiasCurrent':h3cTransceiverBiasCurrent,'h3cTransceiverTempHiAlarm':h3cTransceiverTempHiAlarm,'h3cTransceiverTempLoAlarm':h3cTransceiverTempLoAlarm,'h3cTransceiverTempHiWarn':h3cTransceiverTempHiWarn,'h3cTransceiverTempLoWarn':h3cTransceiverTempLoWarn,'h3cTransceiverVccHiAlarm':h3cTransceiverVccHiAlarm,'h3cTransceiverVccLoAlarm':h3cTransceiverVccLoAlarm,'h3cTransceiverVccHiWarn':h3cTransceiverVccHiWarn,'h3cTransceiverVccLoWarn':h3cTransceiverVccLoWarn,'h3cTransceiverBiasHiAlarm':h3cTransceiverBiasHiAlarm,'h3cTransceiverBiasLoAlarm':h3cTransceiverBiasLoAlarm,'h3cTransceiverBiasHiWarn':h3cTransceiverBiasHiWarn,'h3cTransceiverBiasLoWarn':h3cTransceiverBiasLoWarn,'h3cTransceiverPwrOutHiAlarm':h3cTransceiverPwrOutHiAlarm,'h3cTransceiverPwrOutLoAlarm':h3cTransceiverPwrOutLoAlarm,'h3cTransceiverPwrOutHiWarn':h3cTransceiverPwrOutHiWarn,'h3cTransceiverPwrOutLoWarn':h3cTransceiverPwrOutLoWarn,'h3cTransceiverRcvPwrHiAlarm':h3cTransceiverRcvPwrHiAlarm,'h3cTransceiverRcvPwrLoAlarm':h3cTransceiverRcvPwrLoAlarm,'h3cTransceiverRcvPwrHiWarn':h3cTransceiverRcvPwrHiWarn,'h3cTransceiverRcvPwrLoWarn':h3cTransceiverRcvPwrLoWarn,'h3cTransceiverErrors':h3cTransceiverErrors,'h3cTransceiverVendorOUI':h3cTransceiverVendorOUI,'h3cTransceiverRevisionNumber':h3cTransceiverRevisionNumber,'h3cTransceiverFrequency':h3cTransceiverFrequency,'h3cTransceiverActiveITUChannel':h3cTransceiverActiveITUChannel,'h3cTransceiverCurWaveErr':h3cTransceiverCurWaveErr,'h3cTransceiverWaveErrHiAlarm':h3cTransceiverWaveErrHiAlarm,'h3cTransceiverWaveErrLoAlarm':h3cTransceiverWaveErrLoAlarm,'h3cTransceiverCurFreqErr':h3cTransceiverCurFreqErr,'h3cTransceiverFreqErrHiAlarm':h3cTransceiverFreqErrHiAlarm,'h3cTransceiverFreqErrLoAlarm':h3cTransceiverFreqErrLoAlarm,'h3cTransceiverChannelTable':h3cTransceiverChannelTable,'h3cTransceiverChannelEntry':h3cTransceiverChannelEntry,_I:h3cTransceiverChannelIndex,'h3cTransceiverChannelCurTXPower':h3cTransceiverChannelCurTXPower,'h3cTransceiverChannelCurRXPower':h3cTransceiverChannelCurRXPower,'h3cTransceiverChannelTemperature':h3cTransceiverChannelTemperature,'h3cTransceiverChannelBiasCurrent':h3cTransceiverChannelBiasCurrent,'h3cTransceiverChannelBiasHiAm':h3cTransceiverChannelBiasHiAm,'h3cTransceiverChannelBiasLoAm':h3cTransceiverChannelBiasLoAm,'h3cTransceiverChannelTXPwrHiAm':h3cTransceiverChannelTXPwrHiAm,'h3cTransceiverChannelTXPwrLoAm':h3cTransceiverChannelTXPwrLoAm,'h3cTransceiverITUChanTable':h3cTransceiverITUChanTable,'h3cTransceiverITUChanEntry':h3cTransceiverITUChanEntry,_K:h3cTransceiverITUChanIdx,'h3cTransceiverITUChanFreq':h3cTransceiverITUChanFreq,'h3cTransceiverITUChanWaveLth':h3cTransceiverITUChanWaveLth})