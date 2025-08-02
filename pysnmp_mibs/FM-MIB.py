_M='fsFmVarResponseId'
_L='FM-MIB'
_K='OctetString'
_J='Unsigned32'
_I='ifIndex'
_H='IF-MIB'
_G='warning'
_F='none'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
fsfm=ModuleIdentity((1,3,6,1,4,1,10876,101,1,122))
if mibBuilder.loadTexts:fsfm.setRevisions(('2012-09-05 00:00',))
_FsFmSystem_ObjectIdentity=ObjectIdentity
fsFmSystem=_FsFmSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,1,122,1))
class _FsFmSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsFmSystemControl_Type.__name__=_D
_FsFmSystemControl_Object=MibScalar
fsFmSystemControl=_FsFmSystemControl_Object((1,3,6,1,4,1,10876,101,1,122,1,1),_FsFmSystemControl_Type())
fsFmSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmSystemControl.setStatus(_A)
class _FsFmModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsFmModuleStatus_Type.__name__=_D
_FsFmModuleStatus_Object=MibScalar
fsFmModuleStatus=_FsFmModuleStatus_Object((1,3,6,1,4,1,10876,101,1,122,1,2),_FsFmModuleStatus_Type())
fsFmModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmModuleStatus.setStatus(_A)
class _FsFmTraceOption_Type(Integer32):defaultValue=262144
_FsFmTraceOption_Type.__name__=_D
_FsFmTraceOption_Object=MibScalar
fsFmTraceOption=_FsFmTraceOption_Object((1,3,6,1,4,1,10876,101,1,122,1,3),_FsFmTraceOption_Type())
fsFmTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmTraceOption.setStatus(_A)
_FsFmLinkEvent_ObjectIdentity=ObjectIdentity
fsFmLinkEvent=_FsFmLinkEvent_ObjectIdentity((1,3,6,1,4,1,10876,101,1,122,2))
_FsFmLinkEventTable_Object=MibTable
fsFmLinkEventTable=_FsFmLinkEventTable_Object((1,3,6,1,4,1,10876,101,1,122,2,1))
if mibBuilder.loadTexts:fsFmLinkEventTable.setStatus(_A)
_FsFmLinkEventEntry_Object=MibTableRow
fsFmLinkEventEntry=_FsFmLinkEventEntry_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1))
fsFmLinkEventEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsFmLinkEventEntry.setStatus(_A)
class _FsFmSymPeriodAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmSymPeriodAction_Type.__name__=_D
_FsFmSymPeriodAction_Object=MibTableColumn
fsFmSymPeriodAction=_FsFmSymPeriodAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,1),_FsFmSymPeriodAction_Type())
fsFmSymPeriodAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmSymPeriodAction.setStatus(_A)
class _FsFmFrameAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmFrameAction_Type.__name__=_D
_FsFmFrameAction_Object=MibTableColumn
fsFmFrameAction=_FsFmFrameAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,2),_FsFmFrameAction_Type())
fsFmFrameAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmFrameAction.setStatus(_A)
class _FsFmFramePeriodAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmFramePeriodAction_Type.__name__=_D
_FsFmFramePeriodAction_Object=MibTableColumn
fsFmFramePeriodAction=_FsFmFramePeriodAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,3),_FsFmFramePeriodAction_Type())
fsFmFramePeriodAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmFramePeriodAction.setStatus(_A)
class _FsFmFrameSecSummAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmFrameSecSummAction_Type.__name__=_D
_FsFmFrameSecSummAction_Object=MibTableColumn
fsFmFrameSecSummAction=_FsFmFrameSecSummAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,4),_FsFmFrameSecSummAction_Type())
fsFmFrameSecSummAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmFrameSecSummAction.setStatus(_A)
class _FsFmCriticalEventAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmCriticalEventAction_Type.__name__=_D
_FsFmCriticalEventAction_Object=MibTableColumn
fsFmCriticalEventAction=_FsFmCriticalEventAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,5),_FsFmCriticalEventAction_Type())
fsFmCriticalEventAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmCriticalEventAction.setStatus(_A)
class _FsFmDyingGaspAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmDyingGaspAction_Type.__name__=_D
_FsFmDyingGaspAction_Object=MibTableColumn
fsFmDyingGaspAction=_FsFmDyingGaspAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,6),_FsFmDyingGaspAction_Type())
fsFmDyingGaspAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmDyingGaspAction.setStatus(_A)
class _FsFmLinkFaultAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsFmLinkFaultAction_Type.__name__=_D
_FsFmLinkFaultAction_Object=MibTableColumn
fsFmLinkFaultAction=_FsFmLinkFaultAction_Object((1,3,6,1,4,1,10876,101,1,122,2,1,1,7),_FsFmLinkFaultAction_Type())
fsFmLinkFaultAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLinkFaultAction.setStatus(_A)
_FsFmLoopback_ObjectIdentity=ObjectIdentity
fsFmLoopback=_FsFmLoopback_ObjectIdentity((1,3,6,1,4,1,10876,101,1,122,3))
_FsFmLoopbackTable_Object=MibTable
fsFmLoopbackTable=_FsFmLoopbackTable_Object((1,3,6,1,4,1,10876,101,1,122,3,1))
if mibBuilder.loadTexts:fsFmLoopbackTable.setStatus(_A)
_FsFmLoopbackEntry_Object=MibTableRow
fsFmLoopbackEntry=_FsFmLoopbackEntry_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1))
fsFmLoopbackEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsFmLoopbackEntry.setStatus(_A)
class _FsFmLoopbackStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoopback',1),('remoteLoopback',2),('unknown',3)))
_FsFmLoopbackStatus_Type.__name__=_D
_FsFmLoopbackStatus_Object=MibTableColumn
fsFmLoopbackStatus=_FsFmLoopbackStatus_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,1),_FsFmLoopbackStatus_Type())
fsFmLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLoopbackStatus.setStatus(_A)
class _FsFmLBTestPattern_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsFmLBTestPattern_Type.__name__=_K
_FsFmLBTestPattern_Object=MibTableColumn
fsFmLBTestPattern=_FsFmLBTestPattern_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,2),_FsFmLBTestPattern_Type())
fsFmLBTestPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLBTestPattern.setStatus(_A)
class _FsFmLBTestPktSize_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1500))
_FsFmLBTestPktSize_Type.__name__=_J
_FsFmLBTestPktSize_Object=MibTableColumn
fsFmLBTestPktSize=_FsFmLBTestPktSize_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,3),_FsFmLBTestPktSize_Type())
fsFmLBTestPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLBTestPktSize.setStatus(_A)
class _FsFmLBTestCount_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsFmLBTestCount_Type.__name__=_J
_FsFmLBTestCount_Object=MibTableColumn
fsFmLBTestCount=_FsFmLBTestCount_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,4),_FsFmLBTestCount_Type())
fsFmLBTestCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLBTestCount.setStatus(_A)
class _FsFmLBTestWaitTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsFmLBTestWaitTime_Type.__name__=_D
_FsFmLBTestWaitTime_Object=MibTableColumn
fsFmLBTestWaitTime=_FsFmLBTestWaitTime_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,5),_FsFmLBTestWaitTime_Type())
fsFmLBTestWaitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLBTestWaitTime.setStatus(_A)
class _FsFmLBTestCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noLoopbackTest',1),('startLoopbackTest',2)))
_FsFmLBTestCommand_Type.__name__=_D
_FsFmLBTestCommand_Object=MibTableColumn
fsFmLBTestCommand=_FsFmLBTestCommand_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,6),_FsFmLBTestCommand_Type())
fsFmLBTestCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmLBTestCommand.setStatus(_A)
class _FsFmLBTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notInitiated',1),('loopbackTestInprogress',2),('loopbackTestCompleted',3)))
_FsFmLBTestStatus_Type.__name__=_D
_FsFmLBTestStatus_Object=MibTableColumn
fsFmLBTestStatus=_FsFmLBTestStatus_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,7),_FsFmLBTestStatus_Type())
fsFmLBTestStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestStatus.setStatus(_A)
class _FsFmLBTestStartTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_FsFmLBTestStartTimestamp_Type.__name__=_E
_FsFmLBTestStartTimestamp_Object=MibTableColumn
fsFmLBTestStartTimestamp=_FsFmLBTestStartTimestamp_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,8),_FsFmLBTestStartTimestamp_Type())
fsFmLBTestStartTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestStartTimestamp.setStatus(_A)
class _FsFmLBTestEndTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_FsFmLBTestEndTimestamp_Type.__name__=_E
_FsFmLBTestEndTimestamp_Object=MibTableColumn
fsFmLBTestEndTimestamp=_FsFmLBTestEndTimestamp_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,9),_FsFmLBTestEndTimestamp_Type())
fsFmLBTestEndTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestEndTimestamp.setStatus(_A)
_FsFmLBTestTxCount_Type=Unsigned32
_FsFmLBTestTxCount_Object=MibTableColumn
fsFmLBTestTxCount=_FsFmLBTestTxCount_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,10),_FsFmLBTestTxCount_Type())
fsFmLBTestTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestTxCount.setStatus(_A)
_FsFmLBTestRxCount_Type=Unsigned32
_FsFmLBTestRxCount_Object=MibTableColumn
fsFmLBTestRxCount=_FsFmLBTestRxCount_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,11),_FsFmLBTestRxCount_Type())
fsFmLBTestRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestRxCount.setStatus(_A)
_FsFmLBTestMatchCount_Type=Unsigned32
_FsFmLBTestMatchCount_Object=MibTableColumn
fsFmLBTestMatchCount=_FsFmLBTestMatchCount_Object((1,3,6,1,4,1,10876,101,1,122,3,1,1,12),_FsFmLBTestMatchCount_Type())
fsFmLBTestMatchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBTestMatchCount.setStatus(_A)
_FsFmLBStatsTable_Object=MibTable
fsFmLBStatsTable=_FsFmLBStatsTable_Object((1,3,6,1,4,1,10876,101,1,122,3,2))
if mibBuilder.loadTexts:fsFmLBStatsTable.setStatus(_A)
_FsFmLBStatsEntry_Object=MibTableRow
fsFmLBStatsEntry=_FsFmLBStatsEntry_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1))
fsFmLBStatsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsFmLBStatsEntry.setStatus(_A)
class _FsFmLBStatsStartTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_FsFmLBStatsStartTimestamp_Type.__name__=_E
_FsFmLBStatsStartTimestamp_Object=MibTableColumn
fsFmLBStatsStartTimestamp=_FsFmLBStatsStartTimestamp_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1,1),_FsFmLBStatsStartTimestamp_Type())
fsFmLBStatsStartTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBStatsStartTimestamp.setStatus(_A)
class _FsFmLBStatsEndTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_FsFmLBStatsEndTimestamp_Type.__name__=_E
_FsFmLBStatsEndTimestamp_Object=MibTableColumn
fsFmLBStatsEndTimestamp=_FsFmLBStatsEndTimestamp_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1,2),_FsFmLBStatsEndTimestamp_Type())
fsFmLBStatsEndTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBStatsEndTimestamp.setStatus(_A)
_FsFmLBStatsTxCount_Type=Unsigned32
_FsFmLBStatsTxCount_Object=MibTableColumn
fsFmLBStatsTxCount=_FsFmLBStatsTxCount_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1,3),_FsFmLBStatsTxCount_Type())
fsFmLBStatsTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBStatsTxCount.setStatus(_A)
_FsFmLBStatsRxCount_Type=Unsigned32
_FsFmLBStatsRxCount_Object=MibTableColumn
fsFmLBStatsRxCount=_FsFmLBStatsRxCount_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1,4),_FsFmLBStatsRxCount_Type())
fsFmLBStatsRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBStatsRxCount.setStatus(_A)
_FsFmLBStatsMatchCount_Type=Unsigned32
_FsFmLBStatsMatchCount_Object=MibTableColumn
fsFmLBStatsMatchCount=_FsFmLBStatsMatchCount_Object((1,3,6,1,4,1,10876,101,1,122,3,2,1,5),_FsFmLBStatsMatchCount_Type())
fsFmLBStatsMatchCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmLBStatsMatchCount.setStatus(_A)
_FsFmVarRetrieval_ObjectIdentity=ObjectIdentity
fsFmVarRetrieval=_FsFmVarRetrieval_ObjectIdentity((1,3,6,1,4,1,10876,101,1,122,4))
_FsFmVarRetrievalTable_Object=MibTable
fsFmVarRetrievalTable=_FsFmVarRetrievalTable_Object((1,3,6,1,4,1,10876,101,1,122,4,1))
if mibBuilder.loadTexts:fsFmVarRetrievalTable.setStatus(_A)
_FsFmVarRetrievalEntry_Object=MibTableRow
fsFmVarRetrievalEntry=_FsFmVarRetrievalEntry_Object((1,3,6,1,4,1,10876,101,1,122,4,1,1))
fsFmVarRetrievalEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsFmVarRetrievalEntry.setStatus(_A)
class _FsFmVarRetrievalMaxVar_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsFmVarRetrievalMaxVar_Type.__name__=_J
_FsFmVarRetrievalMaxVar_Object=MibTableColumn
fsFmVarRetrievalMaxVar=_FsFmVarRetrievalMaxVar_Object((1,3,6,1,4,1,10876,101,1,122,4,1,1,1),_FsFmVarRetrievalMaxVar_Type())
fsFmVarRetrievalMaxVar.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmVarRetrievalMaxVar.setStatus(_A)
class _FsFmVarRetrievalRequest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarRetrievalRequest_Type.__name__=_E
_FsFmVarRetrievalRequest_Object=MibTableColumn
fsFmVarRetrievalRequest=_FsFmVarRetrievalRequest_Object((1,3,6,1,4,1,10876,101,1,122,4,1,1,2),_FsFmVarRetrievalRequest_Type())
fsFmVarRetrievalRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmVarRetrievalRequest.setStatus(_A)
class _FsFmVarRetrievalClearResponse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notCleared',1),('clearResponseLog',2)))
_FsFmVarRetrievalClearResponse_Type.__name__=_D
_FsFmVarRetrievalClearResponse_Object=MibTableColumn
fsFmVarRetrievalClearResponse=_FsFmVarRetrievalClearResponse_Object((1,3,6,1,4,1,10876,101,1,122,4,1,1,3),_FsFmVarRetrievalClearResponse_Type())
fsFmVarRetrievalClearResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:fsFmVarRetrievalClearResponse.setStatus(_A)
_FsFmVarResponseTable_Object=MibTable
fsFmVarResponseTable=_FsFmVarResponseTable_Object((1,3,6,1,4,1,10876,101,1,122,4,3))
if mibBuilder.loadTexts:fsFmVarResponseTable.setStatus(_A)
_FsFmVarResponseEntry_Object=MibTableRow
fsFmVarResponseEntry=_FsFmVarResponseEntry_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1))
fsFmVarResponseEntry.setIndexNames((0,_H,_I),(0,_L,_M))
if mibBuilder.loadTexts:fsFmVarResponseEntry.setStatus(_A)
_FsFmVarResponseId_Type=Unsigned32
_FsFmVarResponseId_Object=MibTableColumn
fsFmVarResponseId=_FsFmVarResponseId_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,1),_FsFmVarResponseId_Type())
fsFmVarResponseId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsFmVarResponseId.setStatus(_A)
class _FsFmVarResponseRx1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx1_Type.__name__=_E
_FsFmVarResponseRx1_Object=MibTableColumn
fsFmVarResponseRx1=_FsFmVarResponseRx1_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,2),_FsFmVarResponseRx1_Type())
fsFmVarResponseRx1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx1.setStatus(_A)
class _FsFmVarResponseRx2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx2_Type.__name__=_E
_FsFmVarResponseRx2_Object=MibTableColumn
fsFmVarResponseRx2=_FsFmVarResponseRx2_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,3),_FsFmVarResponseRx2_Type())
fsFmVarResponseRx2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx2.setStatus(_A)
class _FsFmVarResponseRx3_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx3_Type.__name__=_E
_FsFmVarResponseRx3_Object=MibTableColumn
fsFmVarResponseRx3=_FsFmVarResponseRx3_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,4),_FsFmVarResponseRx3_Type())
fsFmVarResponseRx3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx3.setStatus(_A)
class _FsFmVarResponseRx4_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx4_Type.__name__=_E
_FsFmVarResponseRx4_Object=MibTableColumn
fsFmVarResponseRx4=_FsFmVarResponseRx4_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,5),_FsFmVarResponseRx4_Type())
fsFmVarResponseRx4.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx4.setStatus(_A)
class _FsFmVarResponseRx5_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx5_Type.__name__=_E
_FsFmVarResponseRx5_Object=MibTableColumn
fsFmVarResponseRx5=_FsFmVarResponseRx5_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,6),_FsFmVarResponseRx5_Type())
fsFmVarResponseRx5.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx5.setStatus(_A)
class _FsFmVarResponseRx6_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsFmVarResponseRx6_Type.__name__=_E
_FsFmVarResponseRx6_Object=MibTableColumn
fsFmVarResponseRx6=_FsFmVarResponseRx6_Object((1,3,6,1,4,1,10876,101,1,122,4,3,1,7),_FsFmVarResponseRx6_Type())
fsFmVarResponseRx6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFmVarResponseRx6.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'fsfm':fsfm,'fsFmSystem':fsFmSystem,'fsFmSystemControl':fsFmSystemControl,'fsFmModuleStatus':fsFmModuleStatus,'fsFmTraceOption':fsFmTraceOption,'fsFmLinkEvent':fsFmLinkEvent,'fsFmLinkEventTable':fsFmLinkEventTable,'fsFmLinkEventEntry':fsFmLinkEventEntry,'fsFmSymPeriodAction':fsFmSymPeriodAction,'fsFmFrameAction':fsFmFrameAction,'fsFmFramePeriodAction':fsFmFramePeriodAction,'fsFmFrameSecSummAction':fsFmFrameSecSummAction,'fsFmCriticalEventAction':fsFmCriticalEventAction,'fsFmDyingGaspAction':fsFmDyingGaspAction,'fsFmLinkFaultAction':fsFmLinkFaultAction,'fsFmLoopback':fsFmLoopback,'fsFmLoopbackTable':fsFmLoopbackTable,'fsFmLoopbackEntry':fsFmLoopbackEntry,'fsFmLoopbackStatus':fsFmLoopbackStatus,'fsFmLBTestPattern':fsFmLBTestPattern,'fsFmLBTestPktSize':fsFmLBTestPktSize,'fsFmLBTestCount':fsFmLBTestCount,'fsFmLBTestWaitTime':fsFmLBTestWaitTime,'fsFmLBTestCommand':fsFmLBTestCommand,'fsFmLBTestStatus':fsFmLBTestStatus,'fsFmLBTestStartTimestamp':fsFmLBTestStartTimestamp,'fsFmLBTestEndTimestamp':fsFmLBTestEndTimestamp,'fsFmLBTestTxCount':fsFmLBTestTxCount,'fsFmLBTestRxCount':fsFmLBTestRxCount,'fsFmLBTestMatchCount':fsFmLBTestMatchCount,'fsFmLBStatsTable':fsFmLBStatsTable,'fsFmLBStatsEntry':fsFmLBStatsEntry,'fsFmLBStatsStartTimestamp':fsFmLBStatsStartTimestamp,'fsFmLBStatsEndTimestamp':fsFmLBStatsEndTimestamp,'fsFmLBStatsTxCount':fsFmLBStatsTxCount,'fsFmLBStatsRxCount':fsFmLBStatsRxCount,'fsFmLBStatsMatchCount':fsFmLBStatsMatchCount,'fsFmVarRetrieval':fsFmVarRetrieval,'fsFmVarRetrievalTable':fsFmVarRetrievalTable,'fsFmVarRetrievalEntry':fsFmVarRetrievalEntry,'fsFmVarRetrievalMaxVar':fsFmVarRetrievalMaxVar,'fsFmVarRetrievalRequest':fsFmVarRetrievalRequest,'fsFmVarRetrievalClearResponse':fsFmVarRetrievalClearResponse,'fsFmVarResponseTable':fsFmVarResponseTable,'fsFmVarResponseEntry':fsFmVarResponseEntry,_M:fsFmVarResponseId,'fsFmVarResponseRx1':fsFmVarResponseRx1,'fsFmVarResponseRx2':fsFmVarResponseRx2,'fsFmVarResponseRx3':fsFmVarResponseRx3,'fsFmVarResponseRx4':fsFmVarResponseRx4,'fsFmVarResponseRx5':fsFmVarResponseRx5,'fsFmVarResponseRx6':fsFmVarResponseRx6})