_R='applTestStatus'
_Q='applTracerouteHopCount'
_P='applTracerouteResultTestId'
_O='applTracerouteTestId'
_N='service'
_M='applPingTestId'
_L='NotificationType'
_K='applTestType'
_J='ifTestId'
_I='applTestId'
_H='DisplayString'
_G='ifIndex'
_F='Integer32'
_E='IF-MIB'
_D='PDN-DIAGNOSTICS-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,ifTestId=mibBuilder.importSymbols(_E,_G,_J)
pdn_diagnostics,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-diagnostics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_H,'PhysAddress','RowStatus','TextualConvention')
_DiagTestMIBObjects_ObjectIdentity=ObjectIdentity
diagTestMIBObjects=_DiagTestMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,16,1))
_DiagIfTest_ObjectIdentity=ObjectIdentity
diagIfTest=_DiagIfTest_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,16,1,1))
_IfLoopbackTestTable_Object=MibTable
ifLoopbackTestTable=_IfLoopbackTestTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1))
if mibBuilder.loadTexts:ifLoopbackTestTable.setStatus(_A)
_IfLoopbackTestEntry_Object=MibTableRow
ifLoopbackTestEntry=_IfLoopbackTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1))
ifLoopbackTestEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ifLoopbackTestEntry.setStatus(_A)
_LoopbackTestInputNumCycles_Type=Integer32
_LoopbackTestInputNumCycles_Object=MibTableColumn
loopbackTestInputNumCycles=_LoopbackTestInputNumCycles_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,1),_LoopbackTestInputNumCycles_Type())
loopbackTestInputNumCycles.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackTestInputNumCycles.setStatus(_A)
_LoopbackTestResultsPktsSent_Type=Integer32
_LoopbackTestResultsPktsSent_Object=MibTableColumn
loopbackTestResultsPktsSent=_LoopbackTestResultsPktsSent_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,2),_LoopbackTestResultsPktsSent_Type())
loopbackTestResultsPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsPktsSent.setStatus(_A)
_LoopbackTestResultsPktsRcvdOK_Type=Integer32
_LoopbackTestResultsPktsRcvdOK_Object=MibTableColumn
loopbackTestResultsPktsRcvdOK=_LoopbackTestResultsPktsRcvdOK_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,3),_LoopbackTestResultsPktsRcvdOK_Type())
loopbackTestResultsPktsRcvdOK.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsPktsRcvdOK.setStatus(_A)
_LoopbackTestResultsPktsRcvdErr_Type=Integer32
_LoopbackTestResultsPktsRcvdErr_Object=MibTableColumn
loopbackTestResultsPktsRcvdErr=_LoopbackTestResultsPktsRcvdErr_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,4),_LoopbackTestResultsPktsRcvdErr_Type())
loopbackTestResultsPktsRcvdErr.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsPktsRcvdErr.setStatus(_A)
_LoopbackTestResultsPktsNotRcvd_Type=Integer32
_LoopbackTestResultsPktsNotRcvd_Object=MibTableColumn
loopbackTestResultsPktsNotRcvd=_LoopbackTestResultsPktsNotRcvd_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,5),_LoopbackTestResultsPktsNotRcvd_Type())
loopbackTestResultsPktsNotRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsPktsNotRcvd.setStatus(_A)
class _LoopbackTestResultsPktErrorRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_LoopbackTestResultsPktErrorRate_Type.__name__=_H
_LoopbackTestResultsPktErrorRate_Object=MibTableColumn
loopbackTestResultsPktErrorRate=_LoopbackTestResultsPktErrorRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,6),_LoopbackTestResultsPktErrorRate_Type())
loopbackTestResultsPktErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsPktErrorRate.setStatus(_A)
_LoopbackTestResultsErrSecs_Type=Integer32
_LoopbackTestResultsErrSecs_Object=MibTableColumn
loopbackTestResultsErrSecs=_LoopbackTestResultsErrSecs_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,7),_LoopbackTestResultsErrSecs_Type())
loopbackTestResultsErrSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsErrSecs.setStatus(_A)
_LoopbackTestResultsSvrErrSecs_Type=Integer32
_LoopbackTestResultsSvrErrSecs_Object=MibTableColumn
loopbackTestResultsSvrErrSecs=_LoopbackTestResultsSvrErrSecs_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,8),_LoopbackTestResultsSvrErrSecs_Type())
loopbackTestResultsSvrErrSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsSvrErrSecs.setStatus(_A)
_LoopbackTestResultsElpTime_Type=Integer32
_LoopbackTestResultsElpTime_Object=MibTableColumn
loopbackTestResultsElpTime=_LoopbackTestResultsElpTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,1,1,9),_LoopbackTestResultsElpTime_Type())
loopbackTestResultsElpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:loopbackTestResultsElpTime.setStatus(_A)
_IfBERTObjectsTable_Object=MibTable
ifBERTObjectsTable=_IfBERTObjectsTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2))
if mibBuilder.loadTexts:ifBERTObjectsTable.setStatus(_A)
_IfBERTObjectsEntry_Object=MibTableRow
ifBERTObjectsEntry=_IfBERTObjectsEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1))
ifBERTObjectsEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ifBERTObjectsEntry.setStatus(_A)
_IfBERTTestDuration_Type=Integer32
_IfBERTTestDuration_Object=MibTableColumn
ifBERTTestDuration=_IfBERTTestDuration_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,1),_IfBERTTestDuration_Type())
ifBERTTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBERTTestDuration.setStatus(_A)
_IfBERTElapsedTime_Type=Integer32
_IfBERTElapsedTime_Object=MibTableColumn
ifBERTElapsedTime=_IfBERTElapsedTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,2),_IfBERTElapsedTime_Type())
ifBERTElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTElapsedTime.setStatus(_A)
class _IfBERTDownSyncUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_IfBERTDownSyncUP_Type.__name__=_F
_IfBERTDownSyncUP_Object=MibTableColumn
ifBERTDownSyncUP=_IfBERTDownSyncUP_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,3),_IfBERTDownSyncUP_Type())
ifBERTDownSyncUP.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownSyncUP.setStatus(_A)
class _IfBERTUpSyncUP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_IfBERTUpSyncUP_Type.__name__=_F
_IfBERTUpSyncUP_Object=MibTableColumn
ifBERTUpSyncUP=_IfBERTUpSyncUP_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,4),_IfBERTUpSyncUP_Type())
ifBERTUpSyncUP.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpSyncUP.setStatus(_A)
_IfBERTSegmentsSent_Type=Integer32
_IfBERTSegmentsSent_Object=MibTableColumn
ifBERTSegmentsSent=_IfBERTSegmentsSent_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,5),_IfBERTSegmentsSent_Type())
ifBERTSegmentsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTSegmentsSent.setStatus(_A)
_IfBERTDownMBitsRcvd_Type=Integer32
_IfBERTDownMBitsRcvd_Object=MibTableColumn
ifBERTDownMBitsRcvd=_IfBERTDownMBitsRcvd_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,6),_IfBERTDownMBitsRcvd_Type())
ifBERTDownMBitsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownMBitsRcvd.setStatus(_A)
_IfBERTUpMBitsRcvd_Type=Integer32
_IfBERTUpMBitsRcvd_Object=MibTableColumn
ifBERTUpMBitsRcvd=_IfBERTUpMBitsRcvd_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,7),_IfBERTUpMBitsRcvd_Type())
ifBERTUpMBitsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpMBitsRcvd.setStatus(_A)
_IfBERTDownBitErrDetected_Type=Integer32
_IfBERTDownBitErrDetected_Object=MibTableColumn
ifBERTDownBitErrDetected=_IfBERTDownBitErrDetected_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,8),_IfBERTDownBitErrDetected_Type())
ifBERTDownBitErrDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownBitErrDetected.setStatus(_A)
_IfBERTUpBitErrDetected_Type=Integer32
_IfBERTUpBitErrDetected_Object=MibTableColumn
ifBERTUpBitErrDetected=_IfBERTUpBitErrDetected_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,9),_IfBERTUpBitErrDetected_Type())
ifBERTUpBitErrDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpBitErrDetected.setStatus(_A)
class _IfBERTDownBitErrRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_IfBERTDownBitErrRate_Type.__name__=_H
_IfBERTDownBitErrRate_Object=MibTableColumn
ifBERTDownBitErrRate=_IfBERTDownBitErrRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,10),_IfBERTDownBitErrRate_Type())
ifBERTDownBitErrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownBitErrRate.setStatus(_A)
class _IfBERTUpBitErrRate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_IfBERTUpBitErrRate_Type.__name__=_H
_IfBERTUpBitErrRate_Object=MibTableColumn
ifBERTUpBitErrRate=_IfBERTUpBitErrRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,11),_IfBERTUpBitErrRate_Type())
ifBERTUpBitErrRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpBitErrRate.setStatus(_A)
_IfBERTDownErroredSecs_Type=Integer32
_IfBERTDownErroredSecs_Object=MibTableColumn
ifBERTDownErroredSecs=_IfBERTDownErroredSecs_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,12),_IfBERTDownErroredSecs_Type())
ifBERTDownErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownErroredSecs.setStatus(_A)
_IfBERTUpErroredSecs_Type=Integer32
_IfBERTUpErroredSecs_Object=MibTableColumn
ifBERTUpErroredSecs=_IfBERTUpErroredSecs_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,13),_IfBERTUpErroredSecs_Type())
ifBERTUpErroredSecs.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpErroredSecs.setStatus(_A)
_IfBERTDownLineRate_Type=Integer32
_IfBERTDownLineRate_Object=MibTableColumn
ifBERTDownLineRate=_IfBERTDownLineRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,14),_IfBERTDownLineRate_Type())
ifBERTDownLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownLineRate.setStatus(_A)
_IfBERTUpLineRate_Type=Integer32
_IfBERTUpLineRate_Object=MibTableColumn
ifBERTUpLineRate=_IfBERTUpLineRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,15),_IfBERTUpLineRate_Type())
ifBERTUpLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpLineRate.setStatus(_A)
_IfBERTDownMargin_Type=Integer32
_IfBERTDownMargin_Object=MibTableColumn
ifBERTDownMargin=_IfBERTDownMargin_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,16),_IfBERTDownMargin_Type())
ifBERTDownMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTDownMargin.setStatus(_A)
_IfBERTUpMargin_Type=Integer32
_IfBERTUpMargin_Object=MibTableColumn
ifBERTUpMargin=_IfBERTUpMargin_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,2,1,17),_IfBERTUpMargin_Type())
ifBERTUpMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBERTUpMargin.setStatus(_A)
_IfBLERTObjectsTable_Object=MibTable
ifBLERTObjectsTable=_IfBLERTObjectsTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3))
if mibBuilder.loadTexts:ifBLERTObjectsTable.setStatus(_A)
_IfBLERTObjectsEntry_Object=MibTableRow
ifBLERTObjectsEntry=_IfBLERTObjectsEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1))
ifBLERTObjectsEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:ifBLERTObjectsEntry.setStatus(_A)
_IfBLERTTestDuration_Type=Integer32
_IfBLERTTestDuration_Object=MibTableColumn
ifBLERTTestDuration=_IfBLERTTestDuration_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,1),_IfBLERTTestDuration_Type())
ifBLERTTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ifBLERTTestDuration.setStatus(_A)
_IfBLERTElapsedTime_Type=Integer32
_IfBLERTElapsedTime_Object=MibTableColumn
ifBLERTElapsedTime=_IfBLERTElapsedTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,2),_IfBLERTElapsedTime_Type())
ifBLERTElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTElapsedTime.setStatus(_A)
_IfBLERTTxSeqCount_Type=Integer32
_IfBLERTTxSeqCount_Object=MibTableColumn
ifBLERTTxSeqCount=_IfBLERTTxSeqCount_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,3),_IfBLERTTxSeqCount_Type())
ifBLERTTxSeqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTTxSeqCount.setStatus(_A)
_IfBLERTRxSeqCount_Type=Integer32
_IfBLERTRxSeqCount_Object=MibTableColumn
ifBLERTRxSeqCount=_IfBLERTRxSeqCount_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,4),_IfBLERTRxSeqCount_Type())
ifBLERTRxSeqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTRxSeqCount.setStatus(_A)
_IfBLERTRxGoodFrames_Type=Integer32
_IfBLERTRxGoodFrames_Object=MibTableColumn
ifBLERTRxGoodFrames=_IfBLERTRxGoodFrames_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,5),_IfBLERTRxGoodFrames_Type())
ifBLERTRxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTRxGoodFrames.setStatus(_A)
_IfBLERTTxGoodFrames_Type=Integer32
_IfBLERTTxGoodFrames_Object=MibTableColumn
ifBLERTTxGoodFrames=_IfBLERTTxGoodFrames_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,6),_IfBLERTTxGoodFrames_Type())
ifBLERTTxGoodFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTTxGoodFrames.setStatus(_A)
_IfBLERTRxBadFrames_Type=Integer32
_IfBLERTRxBadFrames_Object=MibTableColumn
ifBLERTRxBadFrames=_IfBLERTRxBadFrames_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,7),_IfBLERTRxBadFrames_Type())
ifBLERTRxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTRxBadFrames.setStatus(_A)
_IfBLERTTxBadFrames_Type=Integer32
_IfBLERTTxBadFrames_Object=MibTableColumn
ifBLERTTxBadFrames=_IfBLERTTxBadFrames_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,8),_IfBLERTTxBadFrames_Type())
ifBLERTTxBadFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTTxBadFrames.setStatus(_A)
_IfBLERTDnLineRate_Type=Integer32
_IfBLERTDnLineRate_Object=MibTableColumn
ifBLERTDnLineRate=_IfBLERTDnLineRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,9),_IfBLERTDnLineRate_Type())
ifBLERTDnLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTDnLineRate.setStatus(_A)
_IfBLERTUpLineRate_Type=Integer32
_IfBLERTUpLineRate_Object=MibTableColumn
ifBLERTUpLineRate=_IfBLERTUpLineRate_Object((1,3,6,1,4,1,1795,2,24,2,16,1,1,3,1,10),_IfBLERTUpLineRate_Type())
ifBLERTUpLineRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifBLERTUpLineRate.setStatus(_A)
_DiagApplTest_ObjectIdentity=ObjectIdentity
diagApplTest=_DiagApplTest_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,16,1,2))
_ApplMaxNumberOfTests_Type=Integer32
_ApplMaxNumberOfTests_Object=MibScalar
applMaxNumberOfTests=_ApplMaxNumberOfTests_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,1),_ApplMaxNumberOfTests_Type())
applMaxNumberOfTests.setMaxAccess(_B)
if mibBuilder.loadTexts:applMaxNumberOfTests.setStatus(_A)
_ApplCurrentNumberOfTests_Type=Integer32
_ApplCurrentNumberOfTests_Object=MibScalar
applCurrentNumberOfTests=_ApplCurrentNumberOfTests_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,2),_ApplCurrentNumberOfTests_Type())
applCurrentNumberOfTests.setMaxAccess(_B)
if mibBuilder.loadTexts:applCurrentNumberOfTests.setStatus(_A)
class _ApplStopAllTests_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOp',1),('stop',2),('stopAndClear',3)))
_ApplStopAllTests_Type.__name__=_F
_ApplStopAllTests_Object=MibScalar
applStopAllTests=_ApplStopAllTests_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,3),_ApplStopAllTests_Type())
applStopAllTests.setMaxAccess(_C)
if mibBuilder.loadTexts:applStopAllTests.setStatus(_A)
_ApplNewTestId_Type=Integer32
_ApplNewTestId_Object=MibScalar
applNewTestId=_ApplNewTestId_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,4),_ApplNewTestId_Type())
applNewTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:applNewTestId.setStatus(_A)
_ApplTestStatusTable_Object=MibTable
applTestStatusTable=_ApplTestStatusTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5))
if mibBuilder.loadTexts:applTestStatusTable.setStatus(_A)
_ApplTestStatusEntry_Object=MibTableRow
applTestStatusEntry=_ApplTestStatusEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1))
applTestStatusEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:applTestStatusEntry.setStatus(_A)
_ApplTestId_Type=Integer32
_ApplTestId_Object=MibTableColumn
applTestId=_ApplTestId_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,1),_ApplTestId_Type())
applTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:applTestId.setStatus(_A)
_ApplTestType_Type=AutonomousType
_ApplTestType_Object=MibTableColumn
applTestType=_ApplTestType_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,2),_ApplTestType_Type())
applTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:applTestType.setStatus(_A)
class _ApplTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('inProgress',2),('success',3),('failed',4),('abort',5)))
_ApplTestStatus_Type.__name__=_F
_ApplTestStatus_Object=MibTableColumn
applTestStatus=_ApplTestStatus_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,3),_ApplTestStatus_Type())
applTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:applTestStatus.setStatus(_A)
class _ApplTestErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('timeout',2),('icmpError',3),('systemError',4)))
_ApplTestErrorCode_Type.__name__=_F
_ApplTestErrorCode_Object=MibTableColumn
applTestErrorCode=_ApplTestErrorCode_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,4),_ApplTestErrorCode_Type())
applTestErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:applTestErrorCode.setStatus(_A)
class _ApplTestOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_ApplTestOwner_Type.__name__=_H
_ApplTestOwner_Object=MibTableColumn
applTestOwner=_ApplTestOwner_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,5),_ApplTestOwner_Type())
applTestOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:applTestOwner.setStatus(_A)
_ApplTestRowStatus_Type=RowStatus
_ApplTestRowStatus_Object=MibTableColumn
applTestRowStatus=_ApplTestRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,5,1,6),_ApplTestRowStatus_Type())
applTestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:applTestRowStatus.setStatus(_A)
_ApplPingTestTable_Object=MibTable
applPingTestTable=_ApplPingTestTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6))
if mibBuilder.loadTexts:applPingTestTable.setStatus(_A)
_ApplPingTestEntry_Object=MibTableRow
applPingTestEntry=_ApplPingTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1))
applPingTestEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:applPingTestEntry.setStatus(_A)
_ApplPingTestId_Type=Integer32
_ApplPingTestId_Object=MibTableColumn
applPingTestId=_ApplPingTestId_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,1),_ApplPingTestId_Type())
applPingTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestId.setStatus(_A)
_ApplPingTestIpAddress_Type=IpAddress
_ApplPingTestIpAddress_Object=MibTableColumn
applPingTestIpAddress=_ApplPingTestIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,2),_ApplPingTestIpAddress_Type())
applPingTestIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestIpAddress.setStatus(_A)
_ApplPingTestSourceIpAddr_Type=IpAddress
_ApplPingTestSourceIpAddr_Object=MibTableColumn
applPingTestSourceIpAddr=_ApplPingTestSourceIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,3),_ApplPingTestSourceIpAddr_Type())
applPingTestSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestSourceIpAddr.setStatus(_A)
_ApplPingTestPacketSize_Type=Integer32
_ApplPingTestPacketSize_Object=MibTableColumn
applPingTestPacketSize=_ApplPingTestPacketSize_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,4),_ApplPingTestPacketSize_Type())
applPingTestPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestPacketSize.setStatus(_A)
_ApplPingTestTimeout_Type=Integer32
_ApplPingTestTimeout_Object=MibTableColumn
applPingTestTimeout=_ApplPingTestTimeout_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,5),_ApplPingTestTimeout_Type())
applPingTestTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestTimeout.setStatus(_A)
_ApplPingTestMaxPings_Type=Integer32
_ApplPingTestMaxPings_Object=MibTableColumn
applPingTestMaxPings=_ApplPingTestMaxPings_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,6),_ApplPingTestMaxPings_Type())
applPingTestMaxPings.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestMaxPings.setStatus(_A)
_ApplPingTestPktsSent_Type=Integer32
_ApplPingTestPktsSent_Object=MibTableColumn
applPingTestPktsSent=_ApplPingTestPktsSent_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,7),_ApplPingTestPktsSent_Type())
applPingTestPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestPktsSent.setStatus(_A)
_ApplPingTestPktsRecv_Type=Integer32
_ApplPingTestPktsRecv_Object=MibTableColumn
applPingTestPktsRecv=_ApplPingTestPktsRecv_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,8),_ApplPingTestPktsRecv_Type())
applPingTestPktsRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestPktsRecv.setStatus(_A)
_ApplPingTestMinTime_Type=Integer32
_ApplPingTestMinTime_Object=MibTableColumn
applPingTestMinTime=_ApplPingTestMinTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,9),_ApplPingTestMinTime_Type())
applPingTestMinTime.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestMinTime.setStatus(_A)
_ApplPingTestMaxTime_Type=Integer32
_ApplPingTestMaxTime_Object=MibTableColumn
applPingTestMaxTime=_ApplPingTestMaxTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,10),_ApplPingTestMaxTime_Type())
applPingTestMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestMaxTime.setStatus(_A)
_ApplPingTestAvgTime_Type=Integer32
_ApplPingTestAvgTime_Object=MibTableColumn
applPingTestAvgTime=_ApplPingTestAvgTime_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,11),_ApplPingTestAvgTime_Type())
applPingTestAvgTime.setMaxAccess(_B)
if mibBuilder.loadTexts:applPingTestAvgTime.setStatus(_A)
class _ApplPingTestDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),('mgmt',2),(_N,3)))
_ApplPingTestDomain_Type.__name__=_F
_ApplPingTestDomain_Object=MibTableColumn
applPingTestDomain=_ApplPingTestDomain_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,12),_ApplPingTestDomain_Type())
applPingTestDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestDomain.setStatus(_A)
_ApplPingTestIfIndex_Type=Integer32
_ApplPingTestIfIndex_Object=MibTableColumn
applPingTestIfIndex=_ApplPingTestIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,6,1,13),_ApplPingTestIfIndex_Type())
applPingTestIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:applPingTestIfIndex.setStatus(_A)
_ApplTracerouteConfigTable_Object=MibTable
applTracerouteConfigTable=_ApplTracerouteConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7))
if mibBuilder.loadTexts:applTracerouteConfigTable.setStatus(_A)
_ApplTracerouteConfigEntry_Object=MibTableRow
applTracerouteConfigEntry=_ApplTracerouteConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1))
applTracerouteConfigEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:applTracerouteConfigEntry.setStatus(_A)
_ApplTracerouteTestId_Type=Integer32
_ApplTracerouteTestId_Object=MibTableColumn
applTracerouteTestId=_ApplTracerouteTestId_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,1),_ApplTracerouteTestId_Type())
applTracerouteTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteTestId.setStatus(_A)
_ApplTracerouteIpAddress_Type=IpAddress
_ApplTracerouteIpAddress_Object=MibTableColumn
applTracerouteIpAddress=_ApplTracerouteIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,2),_ApplTracerouteIpAddress_Type())
applTracerouteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteIpAddress.setStatus(_A)
_ApplTracerouteSourceIpAddr_Type=IpAddress
_ApplTracerouteSourceIpAddr_Object=MibTableColumn
applTracerouteSourceIpAddr=_ApplTracerouteSourceIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,3),_ApplTracerouteSourceIpAddr_Type())
applTracerouteSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteSourceIpAddr.setStatus(_A)
_ApplTraceroutePktsSize_Type=Integer32
_ApplTraceroutePktsSize_Object=MibTableColumn
applTraceroutePktsSize=_ApplTraceroutePktsSize_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,4),_ApplTraceroutePktsSize_Type())
applTraceroutePktsSize.setMaxAccess(_C)
if mibBuilder.loadTexts:applTraceroutePktsSize.setStatus(_A)
_ApplTracerouteTimeout_Type=Integer32
_ApplTracerouteTimeout_Object=MibTableColumn
applTracerouteTimeout=_ApplTracerouteTimeout_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,5),_ApplTracerouteTimeout_Type())
applTracerouteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteTimeout.setStatus(_A)
_ApplTracerouteMaxHops_Type=Integer32
_ApplTracerouteMaxHops_Object=MibTableColumn
applTracerouteMaxHops=_ApplTracerouteMaxHops_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,6),_ApplTracerouteMaxHops_Type())
applTracerouteMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteMaxHops.setStatus(_A)
class _ApplTracerouteDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noop',1),('mgmt',2),(_N,3)))
_ApplTracerouteDomain_Type.__name__=_F
_ApplTracerouteDomain_Object=MibTableColumn
applTracerouteDomain=_ApplTracerouteDomain_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,7),_ApplTracerouteDomain_Type())
applTracerouteDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteDomain.setStatus(_A)
_ApplTracerouteIfIndex_Type=Integer32
_ApplTracerouteIfIndex_Object=MibTableColumn
applTracerouteIfIndex=_ApplTracerouteIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,7,1,8),_ApplTracerouteIfIndex_Type())
applTracerouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:applTracerouteIfIndex.setStatus(_A)
_ApplTracerouteResultTable_Object=MibTable
applTracerouteResultTable=_ApplTracerouteResultTable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8))
if mibBuilder.loadTexts:applTracerouteResultTable.setStatus(_A)
_ApplTracerouteResultEntry_Object=MibTableRow
applTracerouteResultEntry=_ApplTracerouteResultEntry_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1))
applTracerouteResultEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:applTracerouteResultEntry.setStatus(_A)
_ApplTracerouteResultTestId_Type=Integer32
_ApplTracerouteResultTestId_Object=MibTableColumn
applTracerouteResultTestId=_ApplTracerouteResultTestId_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,1),_ApplTracerouteResultTestId_Type())
applTracerouteResultTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteResultTestId.setStatus(_A)
_ApplTracerouteHopCount_Type=Integer32
_ApplTracerouteHopCount_Object=MibTableColumn
applTracerouteHopCount=_ApplTracerouteHopCount_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,2),_ApplTracerouteHopCount_Type())
applTracerouteHopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteHopCount.setStatus(_A)
_ApplTracerouteIpAddr_Type=IpAddress
_ApplTracerouteIpAddr_Object=MibTableColumn
applTracerouteIpAddr=_ApplTracerouteIpAddr_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,3),_ApplTracerouteIpAddr_Type())
applTracerouteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteIpAddr.setStatus(_A)
_ApplTraceroutePktSize_Type=Integer32
_ApplTraceroutePktSize_Object=MibTableColumn
applTraceroutePktSize=_ApplTraceroutePktSize_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,4),_ApplTraceroutePktSize_Type())
applTraceroutePktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:applTraceroutePktSize.setStatus(_A)
_ApplTracerouteProbe1RTT_Type=Integer32
_ApplTracerouteProbe1RTT_Object=MibTableColumn
applTracerouteProbe1RTT=_ApplTracerouteProbe1RTT_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,5),_ApplTracerouteProbe1RTT_Type())
applTracerouteProbe1RTT.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteProbe1RTT.setStatus(_A)
_ApplTracerouteProbe2RTT_Type=Integer32
_ApplTracerouteProbe2RTT_Object=MibTableColumn
applTracerouteProbe2RTT=_ApplTracerouteProbe2RTT_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,6),_ApplTracerouteProbe2RTT_Type())
applTracerouteProbe2RTT.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteProbe2RTT.setStatus(_A)
_ApplTracerouteProbe3RTT_Type=Integer32
_ApplTracerouteProbe3RTT_Object=MibTableColumn
applTracerouteProbe3RTT=_ApplTracerouteProbe3RTT_Object((1,3,6,1,4,1,1795,2,24,2,16,1,2,8,1,7),_ApplTracerouteProbe3RTT_Type())
applTracerouteProbe3RTT.setMaxAccess(_B)
if mibBuilder.loadTexts:applTracerouteProbe3RTT.setStatus(_A)
_DiagTest_ObjectIdentity=ObjectIdentity
diagTest=_DiagTest_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,16,1,3))
_DiagTestTrapEnable_Type=Integer32
_DiagTestTrapEnable_Object=MibScalar
diagTestTrapEnable=_DiagTestTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,16,1,3,1),_DiagTestTrapEnable_Type())
diagTestTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:diagTestTrapEnable.setStatus(_A)
_DiagTestMIBTraps_ObjectIdentity=ObjectIdentity
diagTestMIBTraps=_DiagTestMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,16,2))
diagApplTestStart=NotificationType((1,3,6,1,4,1,1795,2,24,2,16,2,0,1))
diagApplTestStart.setObjects(*((_E,_G),(_D,_I),(_D,_K)))
if mibBuilder.loadTexts:diagApplTestStart.setStatus('')
diagIfTestStart=NotificationType((1,3,6,1,4,1,1795,2,24,2,16,2,0,2))
diagIfTestStart.setObjects((_E,_J))
if mibBuilder.loadTexts:diagIfTestStart.setStatus('')
diagApplTestStop=NotificationType((1,3,6,1,4,1,1795,2,24,2,16,2,0,101))
diagApplTestStop.setObjects(*((_E,_G),(_D,_I),(_D,_K),(_D,_R)))
if mibBuilder.loadTexts:diagApplTestStop.setStatus('')
diagIfTestOver=NotificationType((1,3,6,1,4,1,1795,2,24,2,16,2,0,102))
diagIfTestOver.setObjects((_E,_J))
if mibBuilder.loadTexts:diagIfTestOver.setStatus('')
mibBuilder.exportSymbols(_D,**{'diagTestMIBObjects':diagTestMIBObjects,'diagIfTest':diagIfTest,'ifLoopbackTestTable':ifLoopbackTestTable,'ifLoopbackTestEntry':ifLoopbackTestEntry,'loopbackTestInputNumCycles':loopbackTestInputNumCycles,'loopbackTestResultsPktsSent':loopbackTestResultsPktsSent,'loopbackTestResultsPktsRcvdOK':loopbackTestResultsPktsRcvdOK,'loopbackTestResultsPktsRcvdErr':loopbackTestResultsPktsRcvdErr,'loopbackTestResultsPktsNotRcvd':loopbackTestResultsPktsNotRcvd,'loopbackTestResultsPktErrorRate':loopbackTestResultsPktErrorRate,'loopbackTestResultsErrSecs':loopbackTestResultsErrSecs,'loopbackTestResultsSvrErrSecs':loopbackTestResultsSvrErrSecs,'loopbackTestResultsElpTime':loopbackTestResultsElpTime,'ifBERTObjectsTable':ifBERTObjectsTable,'ifBERTObjectsEntry':ifBERTObjectsEntry,'ifBERTTestDuration':ifBERTTestDuration,'ifBERTElapsedTime':ifBERTElapsedTime,'ifBERTDownSyncUP':ifBERTDownSyncUP,'ifBERTUpSyncUP':ifBERTUpSyncUP,'ifBERTSegmentsSent':ifBERTSegmentsSent,'ifBERTDownMBitsRcvd':ifBERTDownMBitsRcvd,'ifBERTUpMBitsRcvd':ifBERTUpMBitsRcvd,'ifBERTDownBitErrDetected':ifBERTDownBitErrDetected,'ifBERTUpBitErrDetected':ifBERTUpBitErrDetected,'ifBERTDownBitErrRate':ifBERTDownBitErrRate,'ifBERTUpBitErrRate':ifBERTUpBitErrRate,'ifBERTDownErroredSecs':ifBERTDownErroredSecs,'ifBERTUpErroredSecs':ifBERTUpErroredSecs,'ifBERTDownLineRate':ifBERTDownLineRate,'ifBERTUpLineRate':ifBERTUpLineRate,'ifBERTDownMargin':ifBERTDownMargin,'ifBERTUpMargin':ifBERTUpMargin,'ifBLERTObjectsTable':ifBLERTObjectsTable,'ifBLERTObjectsEntry':ifBLERTObjectsEntry,'ifBLERTTestDuration':ifBLERTTestDuration,'ifBLERTElapsedTime':ifBLERTElapsedTime,'ifBLERTTxSeqCount':ifBLERTTxSeqCount,'ifBLERTRxSeqCount':ifBLERTRxSeqCount,'ifBLERTRxGoodFrames':ifBLERTRxGoodFrames,'ifBLERTTxGoodFrames':ifBLERTTxGoodFrames,'ifBLERTRxBadFrames':ifBLERTRxBadFrames,'ifBLERTTxBadFrames':ifBLERTTxBadFrames,'ifBLERTDnLineRate':ifBLERTDnLineRate,'ifBLERTUpLineRate':ifBLERTUpLineRate,'diagApplTest':diagApplTest,'applMaxNumberOfTests':applMaxNumberOfTests,'applCurrentNumberOfTests':applCurrentNumberOfTests,'applStopAllTests':applStopAllTests,'applNewTestId':applNewTestId,'applTestStatusTable':applTestStatusTable,'applTestStatusEntry':applTestStatusEntry,_I:applTestId,_K:applTestType,_R:applTestStatus,'applTestErrorCode':applTestErrorCode,'applTestOwner':applTestOwner,'applTestRowStatus':applTestRowStatus,'applPingTestTable':applPingTestTable,'applPingTestEntry':applPingTestEntry,_M:applPingTestId,'applPingTestIpAddress':applPingTestIpAddress,'applPingTestSourceIpAddr':applPingTestSourceIpAddr,'applPingTestPacketSize':applPingTestPacketSize,'applPingTestTimeout':applPingTestTimeout,'applPingTestMaxPings':applPingTestMaxPings,'applPingTestPktsSent':applPingTestPktsSent,'applPingTestPktsRecv':applPingTestPktsRecv,'applPingTestMinTime':applPingTestMinTime,'applPingTestMaxTime':applPingTestMaxTime,'applPingTestAvgTime':applPingTestAvgTime,'applPingTestDomain':applPingTestDomain,'applPingTestIfIndex':applPingTestIfIndex,'applTracerouteConfigTable':applTracerouteConfigTable,'applTracerouteConfigEntry':applTracerouteConfigEntry,_O:applTracerouteTestId,'applTracerouteIpAddress':applTracerouteIpAddress,'applTracerouteSourceIpAddr':applTracerouteSourceIpAddr,'applTraceroutePktsSize':applTraceroutePktsSize,'applTracerouteTimeout':applTracerouteTimeout,'applTracerouteMaxHops':applTracerouteMaxHops,'applTracerouteDomain':applTracerouteDomain,'applTracerouteIfIndex':applTracerouteIfIndex,'applTracerouteResultTable':applTracerouteResultTable,'applTracerouteResultEntry':applTracerouteResultEntry,_P:applTracerouteResultTestId,_Q:applTracerouteHopCount,'applTracerouteIpAddr':applTracerouteIpAddr,'applTraceroutePktSize':applTraceroutePktSize,'applTracerouteProbe1RTT':applTracerouteProbe1RTT,'applTracerouteProbe2RTT':applTracerouteProbe2RTT,'applTracerouteProbe3RTT':applTracerouteProbe3RTT,'diagTest':diagTest,'diagTestTrapEnable':diagTestTrapEnable,'diagTestMIBTraps':diagTestMIBTraps,'diagApplTestStart':diagApplTestStart,'diagIfTestStart':diagIfTestStart,'diagApplTestStop':diagApplTestStop,'diagIfTestOver':diagIfTestOver})