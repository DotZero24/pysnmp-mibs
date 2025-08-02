_K='twampNearEndTestIndex'
_J='twampFarEndTestIndex'
_I='twampTestIndex'
_H='yes'
_G='twampSessionId'
_F='Integer32'
_E='TWAMP-MIB'
_D='Unsigned32'
_C='ms'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
datacomDevicesMIBs,=mibBuilder.importSymbols('DATACOM-SMI','datacomDevicesMIBs')
InetAddress,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
twampMIB=ModuleIdentity((1,3,6,1,4,1,3709,3,6,7))
if mibBuilder.loadTexts:twampMIB.setRevisions(('2019-10-23 00:00',))
class TwampTestLossRatio(TextualConvention,Unsigned32):status=_A;displayHint='d-2';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
class TwampMeasure(TextualConvention,Integer32):status=_A;displayHint='d-2'
_TwampSessionTable_Object=MibTable
twampSessionTable=_TwampSessionTable_Object((1,3,6,1,4,1,3709,3,6,7,1))
if mibBuilder.loadTexts:twampSessionTable.setStatus(_A)
_TwampSessionEntry_Object=MibTableRow
twampSessionEntry=_TwampSessionEntry_Object((1,3,6,1,4,1,3709,3,6,7,1,1))
twampSessionEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:twampSessionEntry.setStatus(_A)
class _TwampSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampSessionId_Type.__name__=_D
_TwampSessionId_Object=MibTableColumn
twampSessionId=_TwampSessionId_Object((1,3,6,1,4,1,3709,3,6,7,1,1,1),_TwampSessionId_Type())
twampSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionId.setStatus(_A)
class _TwampSessionDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TwampSessionDuration_Type.__name__=_D
_TwampSessionDuration_Object=MibTableColumn
twampSessionDuration=_TwampSessionDuration_Object((1,3,6,1,4,1,3709,3,6,7,1,1,2),_TwampSessionDuration_Type())
twampSessionDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionDuration.setStatus(_A)
if mibBuilder.loadTexts:twampSessionDuration.setUnits('s')
class _TwampSessionInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TwampSessionInterval_Type.__name__=_D
_TwampSessionInterval_Object=MibTableColumn
twampSessionInterval=_TwampSessionInterval_Object((1,3,6,1,4,1,3709,3,6,7,1,1,3),_TwampSessionInterval_Type())
twampSessionInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionInterval.setStatus(_A)
if mibBuilder.loadTexts:twampSessionInterval.setUnits('s')
class _TwampSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('inactive',0),('active',1)))
_TwampSessionState_Type.__name__=_F
_TwampSessionState_Object=MibTableColumn
twampSessionState=_TwampSessionState_Object((1,3,6,1,4,1,3709,3,6,7,1,1,4),_TwampSessionState_Type())
twampSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionState.setStatus(_A)
_TwampSessionSrcAddr_Type=InetAddress
_TwampSessionSrcAddr_Object=MibTableColumn
twampSessionSrcAddr=_TwampSessionSrcAddr_Object((1,3,6,1,4,1,3709,3,6,7,1,1,5),_TwampSessionSrcAddr_Type())
twampSessionSrcAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionSrcAddr.setStatus(_A)
_TwampSessionDstAddr_Type=InetAddress
_TwampSessionDstAddr_Object=MibTableColumn
twampSessionDstAddr=_TwampSessionDstAddr_Object((1,3,6,1,4,1,3709,3,6,7,1,1,6),_TwampSessionDstAddr_Type())
twampSessionDstAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionDstAddr.setStatus(_A)
_TwampSessionDstPort_Type=InetPortNumber
_TwampSessionDstPort_Object=MibTableColumn
twampSessionDstPort=_TwampSessionDstPort_Object((1,3,6,1,4,1,3709,3,6,7,1,1,7),_TwampSessionDstPort_Type())
twampSessionDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionDstPort.setStatus(_A)
class _TwampSessionPktSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TwampSessionPktSize_Type.__name__=_D
_TwampSessionPktSize_Object=MibTableColumn
twampSessionPktSize=_TwampSessionPktSize_Object((1,3,6,1,4,1,3709,3,6,7,1,1,8),_TwampSessionPktSize_Type())
twampSessionPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionPktSize.setStatus(_A)
if mibBuilder.loadTexts:twampSessionPktSize.setUnits('B')
class _TwampSessionDSCP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_TwampSessionDSCP_Type.__name__=_D
_TwampSessionDSCP_Object=MibTableColumn
twampSessionDSCP=_TwampSessionDSCP_Object((1,3,6,1,4,1,3709,3,6,7,1,1,9),_TwampSessionDSCP_Type())
twampSessionDSCP.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionDSCP.setStatus(_A)
class _TwampSessionTotalTests_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampSessionTotalTests_Type.__name__=_D
_TwampSessionTotalTests_Object=MibTableColumn
twampSessionTotalTests=_TwampSessionTotalTests_Object((1,3,6,1,4,1,3709,3,6,7,1,1,10),_TwampSessionTotalTests_Type())
twampSessionTotalTests.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionTotalTests.setStatus(_A)
class _TwampSessionTotalTxPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampSessionTotalTxPkts_Type.__name__=_D
_TwampSessionTotalTxPkts_Object=MibTableColumn
twampSessionTotalTxPkts=_TwampSessionTotalTxPkts_Object((1,3,6,1,4,1,3709,3,6,7,1,1,11),_TwampSessionTotalTxPkts_Type())
twampSessionTotalTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionTotalTxPkts.setStatus(_A)
class _TwampSessionTotalRxPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampSessionTotalRxPkts_Type.__name__=_D
_TwampSessionTotalRxPkts_Object=MibTableColumn
twampSessionTotalRxPkts=_TwampSessionTotalRxPkts_Object((1,3,6,1,4,1,3709,3,6,7,1,1,12),_TwampSessionTotalRxPkts_Type())
twampSessionTotalRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampSessionTotalRxPkts.setStatus(_A)
_TwampTestTable_Object=MibTable
twampTestTable=_TwampTestTable_Object((1,3,6,1,4,1,3709,3,6,7,2))
if mibBuilder.loadTexts:twampTestTable.setStatus(_A)
_TwampTestEntry_Object=MibTableRow
twampTestEntry=_TwampTestEntry_Object((1,3,6,1,4,1,3709,3,6,7,2,1))
twampTestEntry.setIndexNames((0,_E,_G),(0,_E,_I))
if mibBuilder.loadTexts:twampTestEntry.setStatus(_A)
class _TwampTestSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampTestSessionId_Type.__name__=_D
_TwampTestSessionId_Object=MibTableColumn
twampTestSessionId=_TwampTestSessionId_Object((1,3,6,1,4,1,3709,3,6,7,2,1,1),_TwampTestSessionId_Type())
twampTestSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestSessionId.setStatus(_A)
class _TwampTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampTestIndex_Type.__name__=_D
_TwampTestIndex_Object=MibTableColumn
twampTestIndex=_TwampTestIndex_Object((1,3,6,1,4,1,3709,3,6,7,2,1,2),_TwampTestIndex_Type())
twampTestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestIndex.setStatus(_A)
class _TwampTestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampTestId_Type.__name__=_D
_TwampTestId_Object=MibTableColumn
twampTestId=_TwampTestId_Object((1,3,6,1,4,1,3709,3,6,7,2,1,3),_TwampTestId_Type())
twampTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestId.setStatus(_A)
_TwampTestDelayMin_Type=TwampMeasure
_TwampTestDelayMin_Object=MibTableColumn
twampTestDelayMin=_TwampTestDelayMin_Object((1,3,6,1,4,1,3709,3,6,7,2,1,4),_TwampTestDelayMin_Type())
twampTestDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampTestDelayMin.setUnits(_C)
_TwampTestDelayMax_Type=TwampMeasure
_TwampTestDelayMax_Object=MibTableColumn
twampTestDelayMax=_TwampTestDelayMax_Object((1,3,6,1,4,1,3709,3,6,7,2,1,5),_TwampTestDelayMax_Type())
twampTestDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampTestDelayMax.setUnits(_C)
_TwampTestDelayAvg_Type=TwampMeasure
_TwampTestDelayAvg_Object=MibTableColumn
twampTestDelayAvg=_TwampTestDelayAvg_Object((1,3,6,1,4,1,3709,3,6,7,2,1,6),_TwampTestDelayAvg_Type())
twampTestDelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestDelayAvg.setStatus(_A)
if mibBuilder.loadTexts:twampTestDelayAvg.setUnits(_C)
_TwampTestJitterMin_Type=TwampMeasure
_TwampTestJitterMin_Object=MibTableColumn
twampTestJitterMin=_TwampTestJitterMin_Object((1,3,6,1,4,1,3709,3,6,7,2,1,7),_TwampTestJitterMin_Type())
twampTestJitterMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestJitterMin.setStatus(_A)
if mibBuilder.loadTexts:twampTestJitterMin.setUnits(_C)
_TwampTestJitterMax_Type=TwampMeasure
_TwampTestJitterMax_Object=MibTableColumn
twampTestJitterMax=_TwampTestJitterMax_Object((1,3,6,1,4,1,3709,3,6,7,2,1,8),_TwampTestJitterMax_Type())
twampTestJitterMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestJitterMax.setStatus(_A)
if mibBuilder.loadTexts:twampTestJitterMax.setUnits(_C)
_TwampTestJitterAvg_Type=TwampMeasure
_TwampTestJitterAvg_Object=MibTableColumn
twampTestJitterAvg=_TwampTestJitterAvg_Object((1,3,6,1,4,1,3709,3,6,7,2,1,9),_TwampTestJitterAvg_Type())
twampTestJitterAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestJitterAvg.setStatus(_A)
if mibBuilder.loadTexts:twampTestJitterAvg.setUnits(_C)
_TwampTestTxPkts_Type=Unsigned32
_TwampTestTxPkts_Object=MibTableColumn
twampTestTxPkts=_TwampTestTxPkts_Object((1,3,6,1,4,1,3709,3,6,7,2,1,10),_TwampTestTxPkts_Type())
twampTestTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestTxPkts.setStatus(_A)
_TwampTestRxPkts_Type=Unsigned32
_TwampTestRxPkts_Object=MibTableColumn
twampTestRxPkts=_TwampTestRxPkts_Object((1,3,6,1,4,1,3709,3,6,7,2,1,11),_TwampTestRxPkts_Type())
twampTestRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestRxPkts.setStatus(_A)
_TwampTestLossRatio_Type=TwampTestLossRatio
_TwampTestLossRatio_Object=MibTableColumn
twampTestLossRatio=_TwampTestLossRatio_Object((1,3,6,1,4,1,3709,3,6,7,2,1,12),_TwampTestLossRatio_Type())
twampTestLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestLossRatio.setStatus(_A)
class _TwampTestConnectivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_H,1)))
_TwampTestConnectivity_Type.__name__=_F
_TwampTestConnectivity_Object=MibTableColumn
twampTestConnectivity=_TwampTestConnectivity_Object((1,3,6,1,4,1,3709,3,6,7,2,1,13),_TwampTestConnectivity_Type())
twampTestConnectivity.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestConnectivity.setStatus(_A)
_TwampTestRoundTripDelayMin_Type=TwampMeasure
_TwampTestRoundTripDelayMin_Object=MibTableColumn
twampTestRoundTripDelayMin=_TwampTestRoundTripDelayMin_Object((1,3,6,1,4,1,3709,3,6,7,2,1,14),_TwampTestRoundTripDelayMin_Type())
twampTestRoundTripDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestRoundTripDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampTestRoundTripDelayMin.setUnits(_C)
_TwampTestRoundTripDelayMax_Type=TwampMeasure
_TwampTestRoundTripDelayMax_Object=MibTableColumn
twampTestRoundTripDelayMax=_TwampTestRoundTripDelayMax_Object((1,3,6,1,4,1,3709,3,6,7,2,1,15),_TwampTestRoundTripDelayMax_Type())
twampTestRoundTripDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestRoundTripDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampTestRoundTripDelayMax.setUnits(_C)
_TwampTestRoundTripDelayAvg_Type=TwampMeasure
_TwampTestRoundTripDelayAvg_Object=MibTableColumn
twampTestRoundTripDelayAvg=_TwampTestRoundTripDelayAvg_Object((1,3,6,1,4,1,3709,3,6,7,2,1,16),_TwampTestRoundTripDelayAvg_Type())
twampTestRoundTripDelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampTestRoundTripDelayAvg.setStatus(_A)
if mibBuilder.loadTexts:twampTestRoundTripDelayAvg.setUnits(_C)
_TwampFarEndTestTable_Object=MibTable
twampFarEndTestTable=_TwampFarEndTestTable_Object((1,3,6,1,4,1,3709,3,6,7,3))
if mibBuilder.loadTexts:twampFarEndTestTable.setStatus(_A)
_TwampFarEndTestEntry_Object=MibTableRow
twampFarEndTestEntry=_TwampFarEndTestEntry_Object((1,3,6,1,4,1,3709,3,6,7,3,1))
twampFarEndTestEntry.setIndexNames((0,_E,_G),(0,_E,_J))
if mibBuilder.loadTexts:twampFarEndTestEntry.setStatus(_A)
class _TwampFarEndTestSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampFarEndTestSessionId_Type.__name__=_D
_TwampFarEndTestSessionId_Object=MibTableColumn
twampFarEndTestSessionId=_TwampFarEndTestSessionId_Object((1,3,6,1,4,1,3709,3,6,7,3,1,1),_TwampFarEndTestSessionId_Type())
twampFarEndTestSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestSessionId.setStatus(_A)
class _TwampFarEndTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampFarEndTestIndex_Type.__name__=_D
_TwampFarEndTestIndex_Object=MibTableColumn
twampFarEndTestIndex=_TwampFarEndTestIndex_Object((1,3,6,1,4,1,3709,3,6,7,3,1,2),_TwampFarEndTestIndex_Type())
twampFarEndTestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestIndex.setStatus(_A)
class _TwampFarEndTestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampFarEndTestId_Type.__name__=_D
_TwampFarEndTestId_Object=MibTableColumn
twampFarEndTestId=_TwampFarEndTestId_Object((1,3,6,1,4,1,3709,3,6,7,3,1,3),_TwampFarEndTestId_Type())
twampFarEndTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestId.setStatus(_A)
_TwampFarEndTestDelayMin_Type=TwampMeasure
_TwampFarEndTestDelayMin_Object=MibTableColumn
twampFarEndTestDelayMin=_TwampFarEndTestDelayMin_Object((1,3,6,1,4,1,3709,3,6,7,3,1,4),_TwampFarEndTestDelayMin_Type())
twampFarEndTestDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestDelayMin.setUnits(_C)
_TwampFarEndTestDelayMax_Type=TwampMeasure
_TwampFarEndTestDelayMax_Object=MibTableColumn
twampFarEndTestDelayMax=_TwampFarEndTestDelayMax_Object((1,3,6,1,4,1,3709,3,6,7,3,1,5),_TwampFarEndTestDelayMax_Type())
twampFarEndTestDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestDelayMax.setUnits(_C)
_TwampFarEndTestDelayAvg_Type=TwampMeasure
_TwampFarEndTestDelayAvg_Object=MibTableColumn
twampFarEndTestDelayAvg=_TwampFarEndTestDelayAvg_Object((1,3,6,1,4,1,3709,3,6,7,3,1,6),_TwampFarEndTestDelayAvg_Type())
twampFarEndTestDelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestDelayAvg.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestDelayAvg.setUnits(_C)
_TwampFarEndTestJitterMin_Type=TwampMeasure
_TwampFarEndTestJitterMin_Object=MibTableColumn
twampFarEndTestJitterMin=_TwampFarEndTestJitterMin_Object((1,3,6,1,4,1,3709,3,6,7,3,1,7),_TwampFarEndTestJitterMin_Type())
twampFarEndTestJitterMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestJitterMin.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestJitterMin.setUnits(_C)
_TwampFarEndTestJitterMax_Type=TwampMeasure
_TwampFarEndTestJitterMax_Object=MibTableColumn
twampFarEndTestJitterMax=_TwampFarEndTestJitterMax_Object((1,3,6,1,4,1,3709,3,6,7,3,1,8),_TwampFarEndTestJitterMax_Type())
twampFarEndTestJitterMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestJitterMax.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestJitterMax.setUnits(_C)
_TwampFarEndTestJitterAvg_Type=TwampMeasure
_TwampFarEndTestJitterAvg_Object=MibTableColumn
twampFarEndTestJitterAvg=_TwampFarEndTestJitterAvg_Object((1,3,6,1,4,1,3709,3,6,7,3,1,9),_TwampFarEndTestJitterAvg_Type())
twampFarEndTestJitterAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestJitterAvg.setStatus(_A)
if mibBuilder.loadTexts:twampFarEndTestJitterAvg.setUnits(_C)
_TwampFarEndTestTxPkts_Type=Unsigned32
_TwampFarEndTestTxPkts_Object=MibTableColumn
twampFarEndTestTxPkts=_TwampFarEndTestTxPkts_Object((1,3,6,1,4,1,3709,3,6,7,3,1,10),_TwampFarEndTestTxPkts_Type())
twampFarEndTestTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestTxPkts.setStatus(_A)
_TwampFarEndTestRxPkts_Type=Unsigned32
_TwampFarEndTestRxPkts_Object=MibTableColumn
twampFarEndTestRxPkts=_TwampFarEndTestRxPkts_Object((1,3,6,1,4,1,3709,3,6,7,3,1,11),_TwampFarEndTestRxPkts_Type())
twampFarEndTestRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestRxPkts.setStatus(_A)
_TwampFarEndTestLossRatio_Type=TwampTestLossRatio
_TwampFarEndTestLossRatio_Object=MibTableColumn
twampFarEndTestLossRatio=_TwampFarEndTestLossRatio_Object((1,3,6,1,4,1,3709,3,6,7,3,1,12),_TwampFarEndTestLossRatio_Type())
twampFarEndTestLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestLossRatio.setStatus(_A)
class _TwampFarEndTestConnectivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_H,1)))
_TwampFarEndTestConnectivity_Type.__name__=_F
_TwampFarEndTestConnectivity_Object=MibTableColumn
twampFarEndTestConnectivity=_TwampFarEndTestConnectivity_Object((1,3,6,1,4,1,3709,3,6,7,3,1,13),_TwampFarEndTestConnectivity_Type())
twampFarEndTestConnectivity.setMaxAccess(_B)
if mibBuilder.loadTexts:twampFarEndTestConnectivity.setStatus(_A)
_TwampNearEndTestTable_Object=MibTable
twampNearEndTestTable=_TwampNearEndTestTable_Object((1,3,6,1,4,1,3709,3,6,7,4))
if mibBuilder.loadTexts:twampNearEndTestTable.setStatus(_A)
_TwampNearEndTestEntry_Object=MibTableRow
twampNearEndTestEntry=_TwampNearEndTestEntry_Object((1,3,6,1,4,1,3709,3,6,7,4,1))
twampNearEndTestEntry.setIndexNames((0,_E,_G),(0,_E,_K))
if mibBuilder.loadTexts:twampNearEndTestEntry.setStatus(_A)
class _TwampNearEndTestSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampNearEndTestSessionId_Type.__name__=_D
_TwampNearEndTestSessionId_Object=MibTableColumn
twampNearEndTestSessionId=_TwampNearEndTestSessionId_Object((1,3,6,1,4,1,3709,3,6,7,4,1,1),_TwampNearEndTestSessionId_Type())
twampNearEndTestSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestSessionId.setStatus(_A)
class _TwampNearEndTestIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampNearEndTestIndex_Type.__name__=_D
_TwampNearEndTestIndex_Object=MibTableColumn
twampNearEndTestIndex=_TwampNearEndTestIndex_Object((1,3,6,1,4,1,3709,3,6,7,4,1,2),_TwampNearEndTestIndex_Type())
twampNearEndTestIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestIndex.setStatus(_A)
class _TwampNearEndTestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_TwampNearEndTestId_Type.__name__=_D
_TwampNearEndTestId_Object=MibTableColumn
twampNearEndTestId=_TwampNearEndTestId_Object((1,3,6,1,4,1,3709,3,6,7,4,1,3),_TwampNearEndTestId_Type())
twampNearEndTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestId.setStatus(_A)
_TwampNearEndTestDelayMin_Type=TwampMeasure
_TwampNearEndTestDelayMin_Object=MibTableColumn
twampNearEndTestDelayMin=_TwampNearEndTestDelayMin_Object((1,3,6,1,4,1,3709,3,6,7,4,1,4),_TwampNearEndTestDelayMin_Type())
twampNearEndTestDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestDelayMin.setUnits(_C)
_TwampNearEndTestDelayMax_Type=TwampMeasure
_TwampNearEndTestDelayMax_Object=MibTableColumn
twampNearEndTestDelayMax=_TwampNearEndTestDelayMax_Object((1,3,6,1,4,1,3709,3,6,7,4,1,5),_TwampNearEndTestDelayMax_Type())
twampNearEndTestDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestDelayMax.setUnits(_C)
_TwampNearEndTestDelayAvg_Type=TwampMeasure
_TwampNearEndTestDelayAvg_Object=MibTableColumn
twampNearEndTestDelayAvg=_TwampNearEndTestDelayAvg_Object((1,3,6,1,4,1,3709,3,6,7,4,1,6),_TwampNearEndTestDelayAvg_Type())
twampNearEndTestDelayAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestDelayAvg.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestDelayAvg.setUnits(_C)
_TwampNearEndTestJitterMin_Type=TwampMeasure
_TwampNearEndTestJitterMin_Object=MibTableColumn
twampNearEndTestJitterMin=_TwampNearEndTestJitterMin_Object((1,3,6,1,4,1,3709,3,6,7,4,1,7),_TwampNearEndTestJitterMin_Type())
twampNearEndTestJitterMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestJitterMin.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestJitterMin.setUnits(_C)
_TwampNearEndTestJitterMax_Type=TwampMeasure
_TwampNearEndTestJitterMax_Object=MibTableColumn
twampNearEndTestJitterMax=_TwampNearEndTestJitterMax_Object((1,3,6,1,4,1,3709,3,6,7,4,1,8),_TwampNearEndTestJitterMax_Type())
twampNearEndTestJitterMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestJitterMax.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestJitterMax.setUnits(_C)
_TwampNearEndTestJitterAvg_Type=TwampMeasure
_TwampNearEndTestJitterAvg_Object=MibTableColumn
twampNearEndTestJitterAvg=_TwampNearEndTestJitterAvg_Object((1,3,6,1,4,1,3709,3,6,7,4,1,9),_TwampNearEndTestJitterAvg_Type())
twampNearEndTestJitterAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestJitterAvg.setStatus(_A)
if mibBuilder.loadTexts:twampNearEndTestJitterAvg.setUnits(_C)
_TwampNearEndTestTxPkts_Type=Unsigned32
_TwampNearEndTestTxPkts_Object=MibTableColumn
twampNearEndTestTxPkts=_TwampNearEndTestTxPkts_Object((1,3,6,1,4,1,3709,3,6,7,4,1,10),_TwampNearEndTestTxPkts_Type())
twampNearEndTestTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestTxPkts.setStatus(_A)
_TwampNearEndTestRxPkts_Type=Unsigned32
_TwampNearEndTestRxPkts_Object=MibTableColumn
twampNearEndTestRxPkts=_TwampNearEndTestRxPkts_Object((1,3,6,1,4,1,3709,3,6,7,4,1,11),_TwampNearEndTestRxPkts_Type())
twampNearEndTestRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestRxPkts.setStatus(_A)
_TwampNearEndTestLossRatio_Type=TwampTestLossRatio
_TwampNearEndTestLossRatio_Object=MibTableColumn
twampNearEndTestLossRatio=_TwampNearEndTestLossRatio_Object((1,3,6,1,4,1,3709,3,6,7,4,1,12),_TwampNearEndTestLossRatio_Type())
twampNearEndTestLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestLossRatio.setStatus(_A)
class _TwampNearEndTestConnectivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),(_H,1)))
_TwampNearEndTestConnectivity_Type.__name__=_F
_TwampNearEndTestConnectivity_Object=MibTableColumn
twampNearEndTestConnectivity=_TwampNearEndTestConnectivity_Object((1,3,6,1,4,1,3709,3,6,7,4,1,13),_TwampNearEndTestConnectivity_Type())
twampNearEndTestConnectivity.setMaxAccess(_B)
if mibBuilder.loadTexts:twampNearEndTestConnectivity.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'TwampTestLossRatio':TwampTestLossRatio,'TwampMeasure':TwampMeasure,'twampMIB':twampMIB,'twampSessionTable':twampSessionTable,'twampSessionEntry':twampSessionEntry,_G:twampSessionId,'twampSessionDuration':twampSessionDuration,'twampSessionInterval':twampSessionInterval,'twampSessionState':twampSessionState,'twampSessionSrcAddr':twampSessionSrcAddr,'twampSessionDstAddr':twampSessionDstAddr,'twampSessionDstPort':twampSessionDstPort,'twampSessionPktSize':twampSessionPktSize,'twampSessionDSCP':twampSessionDSCP,'twampSessionTotalTests':twampSessionTotalTests,'twampSessionTotalTxPkts':twampSessionTotalTxPkts,'twampSessionTotalRxPkts':twampSessionTotalRxPkts,'twampTestTable':twampTestTable,'twampTestEntry':twampTestEntry,'twampTestSessionId':twampTestSessionId,_I:twampTestIndex,'twampTestId':twampTestId,'twampTestDelayMin':twampTestDelayMin,'twampTestDelayMax':twampTestDelayMax,'twampTestDelayAvg':twampTestDelayAvg,'twampTestJitterMin':twampTestJitterMin,'twampTestJitterMax':twampTestJitterMax,'twampTestJitterAvg':twampTestJitterAvg,'twampTestTxPkts':twampTestTxPkts,'twampTestRxPkts':twampTestRxPkts,'twampTestLossRatio':twampTestLossRatio,'twampTestConnectivity':twampTestConnectivity,'twampTestRoundTripDelayMin':twampTestRoundTripDelayMin,'twampTestRoundTripDelayMax':twampTestRoundTripDelayMax,'twampTestRoundTripDelayAvg':twampTestRoundTripDelayAvg,'twampFarEndTestTable':twampFarEndTestTable,'twampFarEndTestEntry':twampFarEndTestEntry,'twampFarEndTestSessionId':twampFarEndTestSessionId,_J:twampFarEndTestIndex,'twampFarEndTestId':twampFarEndTestId,'twampFarEndTestDelayMin':twampFarEndTestDelayMin,'twampFarEndTestDelayMax':twampFarEndTestDelayMax,'twampFarEndTestDelayAvg':twampFarEndTestDelayAvg,'twampFarEndTestJitterMin':twampFarEndTestJitterMin,'twampFarEndTestJitterMax':twampFarEndTestJitterMax,'twampFarEndTestJitterAvg':twampFarEndTestJitterAvg,'twampFarEndTestTxPkts':twampFarEndTestTxPkts,'twampFarEndTestRxPkts':twampFarEndTestRxPkts,'twampFarEndTestLossRatio':twampFarEndTestLossRatio,'twampFarEndTestConnectivity':twampFarEndTestConnectivity,'twampNearEndTestTable':twampNearEndTestTable,'twampNearEndTestEntry':twampNearEndTestEntry,'twampNearEndTestSessionId':twampNearEndTestSessionId,_K:twampNearEndTestIndex,'twampNearEndTestId':twampNearEndTestId,'twampNearEndTestDelayMin':twampNearEndTestDelayMin,'twampNearEndTestDelayMax':twampNearEndTestDelayMax,'twampNearEndTestDelayAvg':twampNearEndTestDelayAvg,'twampNearEndTestJitterMin':twampNearEndTestJitterMin,'twampNearEndTestJitterMax':twampNearEndTestJitterMax,'twampNearEndTestJitterAvg':twampNearEndTestJitterAvg,'twampNearEndTestTxPkts':twampNearEndTestTxPkts,'twampNearEndTestRxPkts':twampNearEndTestRxPkts,'twampNearEndTestLossRatio':twampNearEndTestLossRatio,'twampNearEndTestConnectivity':twampNearEndTestConnectivity})