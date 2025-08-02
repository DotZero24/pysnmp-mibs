_K='ifIndex'
_J='IF-MIB'
_I='disable'
_H='enable'
_G='read-write'
_F='na'
_E='fail'
_D='pass'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenGr909,adGenGr909ID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenGr909','adGenGr909ID')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenGr909MIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,19,1))
if mibBuilder.loadTexts:adGenGr909MIB.setRevisions(('2012-03-07 00:00','2012-02-03 08:32','2007-03-30 08:32'))
_AdGenGr909Table_Object=MibTable
adGenGr909Table=_AdGenGr909Table_Object((1,3,6,1,4,1,664,5,67,1,19,1))
if mibBuilder.loadTexts:adGenGr909Table.setStatus(_A)
_AdGenGr909Entry_Object=MibTableRow
adGenGr909Entry=_AdGenGr909Entry_Object((1,3,6,1,4,1,664,5,67,1,19,1,1))
adGenGr909Entry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:adGenGr909Entry.setStatus(_A)
class _AdGenGr909HPTResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909HPTResult_Type.__name__=_C
_AdGenGr909HPTResult_Object=MibTableColumn
adGenGr909HPTResult=_AdGenGr909HPTResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,1),_AdGenGr909HPTResult_Type())
adGenGr909HPTResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909HPTResult.setStatus(_A)
class _AdGenGr909FEMFResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909FEMFResult_Type.__name__=_C
_AdGenGr909FEMFResult_Object=MibTableColumn
adGenGr909FEMFResult=_AdGenGr909FEMFResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,2),_AdGenGr909FEMFResult_Type())
adGenGr909FEMFResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FEMFResult.setStatus(_A)
class _AdGenGr909RFaultResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909RFaultResult_Type.__name__=_C
_AdGenGr909RFaultResult_Object=MibTableColumn
adGenGr909RFaultResult=_AdGenGr909RFaultResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,3),_AdGenGr909RFaultResult_Type())
adGenGr909RFaultResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909RFaultResult.setStatus(_A)
class _AdGenGr909RingerResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909RingerResult_Type.__name__=_C
_AdGenGr909RingerResult_Object=MibTableColumn
adGenGr909RingerResult=_AdGenGr909RingerResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,4),_AdGenGr909RingerResult_Type())
adGenGr909RingerResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909RingerResult.setStatus(_A)
class _AdGenGr909ROHResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909ROHResult_Type.__name__=_C
_AdGenGr909ROHResult_Object=MibTableColumn
adGenGr909ROHResult=_AdGenGr909ROHResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,5),_AdGenGr909ROHResult_Type())
adGenGr909ROHResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909ROHResult.setStatus(_A)
_AdGenGr909FVAcTipToGndMeas_Type=DisplayString
_AdGenGr909FVAcTipToGndMeas_Object=MibTableColumn
adGenGr909FVAcTipToGndMeas=_AdGenGr909FVAcTipToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,6),_AdGenGr909FVAcTipToGndMeas_Type())
adGenGr909FVAcTipToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVAcTipToGndMeas.setStatus(_A)
_AdGenGr909FVAcRingToGndMeas_Type=DisplayString
_AdGenGr909FVAcRingToGndMeas_Object=MibTableColumn
adGenGr909FVAcRingToGndMeas=_AdGenGr909FVAcRingToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,7),_AdGenGr909FVAcRingToGndMeas_Type())
adGenGr909FVAcRingToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVAcRingToGndMeas.setStatus(_A)
_AdGenGr909FVDcTipToGndMeas_Type=DisplayString
_AdGenGr909FVDcTipToGndMeas_Object=MibTableColumn
adGenGr909FVDcTipToGndMeas=_AdGenGr909FVDcTipToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,8),_AdGenGr909FVDcTipToGndMeas_Type())
adGenGr909FVDcTipToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVDcTipToGndMeas.setStatus(_A)
_AdGenGr909FVDcRingToGndMeas_Type=DisplayString
_AdGenGr909FVDcRingToGndMeas_Object=MibTableColumn
adGenGr909FVDcRingToGndMeas=_AdGenGr909FVDcRingToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,9),_AdGenGr909FVDcRingToGndMeas_Type())
adGenGr909FVDcRingToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVDcRingToGndMeas.setStatus(_A)
class _AdGenGr909FVAcTipToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909FVAcTipToGndResult_Type.__name__=_C
_AdGenGr909FVAcTipToGndResult_Object=MibTableColumn
adGenGr909FVAcTipToGndResult=_AdGenGr909FVAcTipToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,10),_AdGenGr909FVAcTipToGndResult_Type())
adGenGr909FVAcTipToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVAcTipToGndResult.setStatus(_A)
class _AdGenGr909FVAcRingToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909FVAcRingToGndResult_Type.__name__=_C
_AdGenGr909FVAcRingToGndResult_Object=MibTableColumn
adGenGr909FVAcRingToGndResult=_AdGenGr909FVAcRingToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,11),_AdGenGr909FVAcRingToGndResult_Type())
adGenGr909FVAcRingToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVAcRingToGndResult.setStatus(_A)
class _AdGenGr909FVDcTipToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909FVDcTipToGndResult_Type.__name__=_C
_AdGenGr909FVDcTipToGndResult_Object=MibTableColumn
adGenGr909FVDcTipToGndResult=_AdGenGr909FVDcTipToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,12),_AdGenGr909FVDcTipToGndResult_Type())
adGenGr909FVDcTipToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVDcTipToGndResult.setStatus(_A)
class _AdGenGr909FVDcRingToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909FVDcRingToGndResult_Type.__name__=_C
_AdGenGr909FVDcRingToGndResult_Object=MibTableColumn
adGenGr909FVDcRingToGndResult=_AdGenGr909FVDcRingToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,13),_AdGenGr909FVDcRingToGndResult_Type())
adGenGr909FVDcRingToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FVDcRingToGndResult.setStatus(_A)
_AdGenGr909LoopImpTipToRingMeas_Type=DisplayString
_AdGenGr909LoopImpTipToRingMeas_Object=MibTableColumn
adGenGr909LoopImpTipToRingMeas=_AdGenGr909LoopImpTipToRingMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,14),_AdGenGr909LoopImpTipToRingMeas_Type())
adGenGr909LoopImpTipToRingMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpTipToRingMeas.setStatus(_A)
_AdGenGr909LoopImpTipToGndMeas_Type=DisplayString
_AdGenGr909LoopImpTipToGndMeas_Object=MibTableColumn
adGenGr909LoopImpTipToGndMeas=_AdGenGr909LoopImpTipToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,15),_AdGenGr909LoopImpTipToGndMeas_Type())
adGenGr909LoopImpTipToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpTipToGndMeas.setStatus(_A)
_AdGenGr909LoopImpRingToGndMeas_Type=DisplayString
_AdGenGr909LoopImpRingToGndMeas_Object=MibTableColumn
adGenGr909LoopImpRingToGndMeas=_AdGenGr909LoopImpRingToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,16),_AdGenGr909LoopImpRingToGndMeas_Type())
adGenGr909LoopImpRingToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpRingToGndMeas.setStatus(_A)
class _AdGenGr909LoopImpTipToRingResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909LoopImpTipToRingResult_Type.__name__=_C
_AdGenGr909LoopImpTipToRingResult_Object=MibTableColumn
adGenGr909LoopImpTipToRingResult=_AdGenGr909LoopImpTipToRingResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,17),_AdGenGr909LoopImpTipToRingResult_Type())
adGenGr909LoopImpTipToRingResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpTipToRingResult.setStatus(_A)
class _AdGenGr909LoopImpTipToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909LoopImpTipToGndResult_Type.__name__=_C
_AdGenGr909LoopImpTipToGndResult_Object=MibTableColumn
adGenGr909LoopImpTipToGndResult=_AdGenGr909LoopImpTipToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,18),_AdGenGr909LoopImpTipToGndResult_Type())
adGenGr909LoopImpTipToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpTipToGndResult.setStatus(_A)
class _AdGenGr909LoopImpRingToGndResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_AdGenGr909LoopImpRingToGndResult_Type.__name__=_C
_AdGenGr909LoopImpRingToGndResult_Object=MibTableColumn
adGenGr909LoopImpRingToGndResult=_AdGenGr909LoopImpRingToGndResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,19),_AdGenGr909LoopImpRingToGndResult_Type())
adGenGr909LoopImpRingToGndResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopImpRingToGndResult.setStatus(_A)
_AdGenGr909RingerMeas_Type=DisplayString
_AdGenGr909RingerMeas_Object=MibTableColumn
adGenGr909RingerMeas=_AdGenGr909RingerMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,20),_AdGenGr909RingerMeas_Type())
adGenGr909RingerMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909RingerMeas.setStatus(_A)
_AdGenGr909LastTestComplete_Type=DisplayString
_AdGenGr909LastTestComplete_Object=MibTableColumn
adGenGr909LastTestComplete=_AdGenGr909LastTestComplete_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,21),_AdGenGr909LastTestComplete_Type())
adGenGr909LastTestComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LastTestComplete.setStatus(_A)
_AdGenGr909LastTestAttempt_Type=DisplayString
_AdGenGr909LastTestAttempt_Object=MibTableColumn
adGenGr909LastTestAttempt=_AdGenGr909LastTestAttempt_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,22),_AdGenGr909LastTestAttempt_Type())
adGenGr909LastTestAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LastTestAttempt.setStatus(_A)
class _AdGenGr909LastTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('complete',2),('fault',3),('running',4)))
_AdGenGr909LastTestResult_Type.__name__=_C
_AdGenGr909LastTestResult_Object=MibTableColumn
adGenGr909LastTestResult=_AdGenGr909LastTestResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,23),_AdGenGr909LastTestResult_Type())
adGenGr909LastTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LastTestResult.setStatus(_A)
_AdGenGr909FailureCode_Type=DisplayString
_AdGenGr909FailureCode_Object=MibTableColumn
adGenGr909FailureCode=_AdGenGr909FailureCode_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,24),_AdGenGr909FailureCode_Type())
adGenGr909FailureCode.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909FailureCode.setStatus(_A)
class _AdGenGr909BeginTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('begin',1))
_AdGenGr909BeginTest_Type.__name__=_C
_AdGenGr909BeginTest_Object=MibTableColumn
adGenGr909BeginTest=_AdGenGr909BeginTest_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,25),_AdGenGr909BeginTest_Type())
adGenGr909BeginTest.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGr909BeginTest.setStatus(_A)
_AdGenGr909LoopCapTipToRingMeas_Type=DisplayString
_AdGenGr909LoopCapTipToRingMeas_Object=MibTableColumn
adGenGr909LoopCapTipToRingMeas=_AdGenGr909LoopCapTipToRingMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,26),_AdGenGr909LoopCapTipToRingMeas_Type())
adGenGr909LoopCapTipToRingMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopCapTipToRingMeas.setStatus(_A)
_AdGenGr909LoopCapTipToGndMeas_Type=DisplayString
_AdGenGr909LoopCapTipToGndMeas_Object=MibTableColumn
adGenGr909LoopCapTipToGndMeas=_AdGenGr909LoopCapTipToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,27),_AdGenGr909LoopCapTipToGndMeas_Type())
adGenGr909LoopCapTipToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopCapTipToGndMeas.setStatus(_A)
_AdGenGr909LoopCapRingToGndMeas_Type=DisplayString
_AdGenGr909LoopCapRingToGndMeas_Object=MibTableColumn
adGenGr909LoopCapRingToGndMeas=_AdGenGr909LoopCapRingToGndMeas_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,28),_AdGenGr909LoopCapRingToGndMeas_Type())
adGenGr909LoopCapRingToGndMeas.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoopCapRingToGndMeas.setStatus(_A)
class _AdGenGr909IdleNoiseMeasure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120000))
_AdGenGr909IdleNoiseMeasure_Type.__name__=_C
_AdGenGr909IdleNoiseMeasure_Object=MibTableColumn
adGenGr909IdleNoiseMeasure=_AdGenGr909IdleNoiseMeasure_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,29),_AdGenGr909IdleNoiseMeasure_Type())
adGenGr909IdleNoiseMeasure.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909IdleNoiseMeasure.setStatus(_A)
if mibBuilder.loadTexts:adGenGr909IdleNoiseMeasure.setUnits('-0.001 dBm')
class _AdGenGr909IdleNoiseResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_AdGenGr909IdleNoiseResult_Type.__name__=_C
_AdGenGr909IdleNoiseResult_Object=MibTableColumn
adGenGr909IdleNoiseResult=_AdGenGr909IdleNoiseResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,30),_AdGenGr909IdleNoiseResult_Type())
adGenGr909IdleNoiseResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909IdleNoiseResult.setStatus(_A)
class _AdGenGr909NumLoadCoils_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AdGenGr909NumLoadCoils_Type.__name__=_C
_AdGenGr909NumLoadCoils_Object=MibTableColumn
adGenGr909NumLoadCoils=_AdGenGr909NumLoadCoils_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,31),_AdGenGr909NumLoadCoils_Type())
adGenGr909NumLoadCoils.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909NumLoadCoils.setStatus(_A)
_AdGenGr909LoadCoilsDistance_Type=OctetString
_AdGenGr909LoadCoilsDistance_Object=MibTableColumn
adGenGr909LoadCoilsDistance=_AdGenGr909LoadCoilsDistance_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,32),_AdGenGr909LoadCoilsDistance_Type())
adGenGr909LoadCoilsDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoadCoilsDistance.setStatus(_A)
class _AdGenGr909LoadCoilsResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_AdGenGr909LoadCoilsResult_Type.__name__=_C
_AdGenGr909LoadCoilsResult_Object=MibTableColumn
adGenGr909LoadCoilsResult=_AdGenGr909LoadCoilsResult_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,33),_AdGenGr909LoadCoilsResult_Type())
adGenGr909LoadCoilsResult.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenGr909LoadCoilsResult.setStatus(_A)
class _AdGenGr909TestFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AdGenGr909TestFlag_Type.__name__=_C
_AdGenGr909TestFlag_Object=MibTableColumn
adGenGr909TestFlag=_AdGenGr909TestFlag_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,34),_AdGenGr909TestFlag_Type())
adGenGr909TestFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGr909TestFlag.setStatus(_A)
class _AdGenGr909TestCapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AdGenGr909TestCapFlag_Type.__name__=_C
_AdGenGr909TestCapFlag_Object=MibTableColumn
adGenGr909TestCapFlag=_AdGenGr909TestCapFlag_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,35),_AdGenGr909TestCapFlag_Type())
adGenGr909TestCapFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGr909TestCapFlag.setStatus(_A)
class _AdGenGr909TestNoiseFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AdGenGr909TestNoiseFlag_Type.__name__=_C
_AdGenGr909TestNoiseFlag_Object=MibTableColumn
adGenGr909TestNoiseFlag=_AdGenGr909TestNoiseFlag_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,36),_AdGenGr909TestNoiseFlag_Type())
adGenGr909TestNoiseFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGr909TestNoiseFlag.setStatus(_A)
class _AdGenGr909TestLoadCoilFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AdGenGr909TestLoadCoilFlag_Type.__name__=_C
_AdGenGr909TestLoadCoilFlag_Object=MibTableColumn
adGenGr909TestLoadCoilFlag=_AdGenGr909TestLoadCoilFlag_Object((1,3,6,1,4,1,664,5,67,1,19,1,1,37),_AdGenGr909TestLoadCoilFlag_Type())
adGenGr909TestLoadCoilFlag.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenGr909TestLoadCoilFlag.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-TA5K-GR909-MIB',**{'adGenGr909Table':adGenGr909Table,'adGenGr909Entry':adGenGr909Entry,'adGenGr909HPTResult':adGenGr909HPTResult,'adGenGr909FEMFResult':adGenGr909FEMFResult,'adGenGr909RFaultResult':adGenGr909RFaultResult,'adGenGr909RingerResult':adGenGr909RingerResult,'adGenGr909ROHResult':adGenGr909ROHResult,'adGenGr909FVAcTipToGndMeas':adGenGr909FVAcTipToGndMeas,'adGenGr909FVAcRingToGndMeas':adGenGr909FVAcRingToGndMeas,'adGenGr909FVDcTipToGndMeas':adGenGr909FVDcTipToGndMeas,'adGenGr909FVDcRingToGndMeas':adGenGr909FVDcRingToGndMeas,'adGenGr909FVAcTipToGndResult':adGenGr909FVAcTipToGndResult,'adGenGr909FVAcRingToGndResult':adGenGr909FVAcRingToGndResult,'adGenGr909FVDcTipToGndResult':adGenGr909FVDcTipToGndResult,'adGenGr909FVDcRingToGndResult':adGenGr909FVDcRingToGndResult,'adGenGr909LoopImpTipToRingMeas':adGenGr909LoopImpTipToRingMeas,'adGenGr909LoopImpTipToGndMeas':adGenGr909LoopImpTipToGndMeas,'adGenGr909LoopImpRingToGndMeas':adGenGr909LoopImpRingToGndMeas,'adGenGr909LoopImpTipToRingResult':adGenGr909LoopImpTipToRingResult,'adGenGr909LoopImpTipToGndResult':adGenGr909LoopImpTipToGndResult,'adGenGr909LoopImpRingToGndResult':adGenGr909LoopImpRingToGndResult,'adGenGr909RingerMeas':adGenGr909RingerMeas,'adGenGr909LastTestComplete':adGenGr909LastTestComplete,'adGenGr909LastTestAttempt':adGenGr909LastTestAttempt,'adGenGr909LastTestResult':adGenGr909LastTestResult,'adGenGr909FailureCode':adGenGr909FailureCode,'adGenGr909BeginTest':adGenGr909BeginTest,'adGenGr909LoopCapTipToRingMeas':adGenGr909LoopCapTipToRingMeas,'adGenGr909LoopCapTipToGndMeas':adGenGr909LoopCapTipToGndMeas,'adGenGr909LoopCapRingToGndMeas':adGenGr909LoopCapRingToGndMeas,'adGenGr909IdleNoiseMeasure':adGenGr909IdleNoiseMeasure,'adGenGr909IdleNoiseResult':adGenGr909IdleNoiseResult,'adGenGr909NumLoadCoils':adGenGr909NumLoadCoils,'adGenGr909LoadCoilsDistance':adGenGr909LoadCoilsDistance,'adGenGr909LoadCoilsResult':adGenGr909LoadCoilsResult,'adGenGr909TestFlag':adGenGr909TestFlag,'adGenGr909TestCapFlag':adGenGr909TestCapFlag,'adGenGr909TestNoiseFlag':adGenGr909TestNoiseFlag,'adGenGr909TestLoadCoilFlag':adGenGr909TestLoadCoilFlag,'adGenGr909MIB':adGenGr909MIB})