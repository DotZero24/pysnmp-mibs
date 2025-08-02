_B3='ituSatGeneratorPerfResult'
_B2='ituSatGeneratorConfResult'
_B1='ituSatGeneratorStatus'
_B0='tstNeThroughputIteration'
_A_='twampReportIntervalNumber'
_Az='ituSatConfPbitDirectionIndex'
_Ay='ituSatConfPbitIndex'
_Ax='ituSatResponderPerfPbitIndex'
_Aw='ituSatReportDirectionIndex'
_Av='ituSatReportTestTypeIndex'
_Au='ituSatReportPbitIndex'
_At='framelossRateReportInputRate'
_As='framelossRateReportPacketSize'
_Ar='framelossRateReportTrialNumber'
_Aq='latencyReportPacketSize'
_Ap='latencyReportTrialNumber'
_Ao='oamConnectivityFailure'
_An='tstNePerfRepGeneralResultsTrialNumber'
_Am='tstNePerfRepGeneralResultsTestType'
_Al='ituSatSingleCosFlowIdx2'
_Ak='ituSatSingleCosFlowIdx1'
_Aj='ituSatSingleCosFlowFunctionIndex'
_Ai='ituSatSingleCosFlowFunction'
_Ah='twampResSessionId'
_Ag='oneWayRadm'
_Af='outOfSync'
_Ae='twampLight'
_Ad='ituSatGeneratorPolicerPbitIndex'
_Ac='ituSatGeneratorFlowPbitIndex'
_Ab='serviceNameAndEgressPort'
_Aa='multipleSingleCosFlows'
_AZ='singleMultiCosFlow'
_AY='systemAborted'
_AX='userAborted'
_AW='completed'
_AV='twampTestProfileId'
_AU='ituSatProfilePbitIndex'
_AT='tstMepFlowIndex'
_AS='prbsWithoutCrc'
_AR='prbsWithCrc'
_AQ='alternate'
_AP='allZerosWithCrc'
_AO='allZerosWithoutCrc'
_AN='tstNePerfRepProfileId'
_AM='TruthValue'
_AL='MacAddress'
_AK='RadTestPbitValues'
_AJ='dot1agCfmMepIdentifier'
_AI='dot1agCfmMdIndex'
_AH='dot1agCfmMaIndex'
_AG='ituSatResponderName'
_AF='ituSatResponderStatus'
_AE='tstNePerfRepTestType'
_AD='throughputReportPacketSize'
_AC='throughputReportTrialNumber'
_AB='twampResponderId'
_AA='dvTca'
_A9='delayTca'
_A8='lossTca'
_A7='ituSatResponderIndex'
_A6='timeOut'
_A5='adminOff'
_A4='latency'
_A3='frameloss'
_A2='throughput'
_A1='minutes'
_A0='configuration'
_z='ituSatProfileIndex'
_y='InterfaceIndexOrZero'
_x='OctetString'
_w='twampControllerName'
_v='twampTestProfileDelayVarEventType'
_u='twampPeerDescr'
_t='ituSatGeneratorName'
_s='frames'
_r='Kbps'
_q='twampContSessionId'
_p='roundTrip'
_o='kbps'
_n='performance'
_m='ppm'
_l='IEEE8021-CFM-MIB'
_k='twampPeerAddr'
_j='twampPeerAddrType'
_i='ready'
_h='hundredth of percent'
_g='bytes'
_f='Gauge32'
_e='tstNePerfRepIteration'
_d='twampControllerId'
_c='ituSatGeneratorIndex'
_b='inProgress'
_a='notApplicable'
_Z='idle'
_Y='Bits'
_X='on'
_W='tstNePerfRepTestId'
_V='sysName'
_U='SNMPv2-MIB'
_T='off'
_S='twampContSessionStatus'
_R='SnmpAdminString'
_Q='twampContSessionName'
_P='seconds'
_O='alarmEventReason'
_N='alarmEventLogSourceName'
_M='alarmEventLogSeverity'
_L='alarmEventLogDescription'
_K='alarmEventLogDateAndTime'
_J='alarmEventLogAlarmOrEventId'
_I='not-accessible'
_H='Unsigned32'
_G='Integer32'
_F='micro seconds'
_E='RAD-TEST-MIB'
_D='RAD-GEN-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_x,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_l,_AH,_AI,_AJ)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_y)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_D,_J,_K,_L,_M,_N,_O)
systems,=mibBuilder.importSymbols('RAD-SMI-MIB','systems')
RadTestPbitValues,RadTestResult=mibBuilder.importSymbols('RAD-TC',_AK,'RadTestResult')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_U,_V)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_Y,'Counter32','Counter64',_f,_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString',_AL,'PhysAddress','RowPointer','RowStatus','TextualConvention',_AM)
radTest=ModuleIdentity((1,3,6,1,4,1,164,6,1,15))
class RadTestPerfRepFrameSize(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('s64',0),('s128',1),('s256',2),('s512',3),('s1024',4),('s1280',5),('s1518',6),('s1700',7),('s1900',8),('s2000',9),('s2048',10),('s4096',11),('s9600',12),('custom',13)))
class RadTestPerfresultFrameSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('s64',1),('s128',2),('s256',3),('s512',4),('s1024',5),('s1280',6),('s1518',7),('s1700',8),('s1900',9),('s2000',10),('s2048',11),('s4096',12),('s9600',13),('custom',14)))
class RadTestPbitIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('pbit0',0),('pbit1',1),('pbit2',2),('pbit3',3),('pbit4',4),('pbit5',5),('pbit6',6),('pbit7',7)))
_RadTestPrefRepEvents_ObjectIdentity=ObjectIdentity
radTestPrefRepEvents=_RadTestPrefRepEvents_ObjectIdentity((1,3,6,1,4,1,164,6,1,15,0))
_RadTestPrefRepProfile_ObjectIdentity=ObjectIdentity
radTestPrefRepProfile=_RadTestPrefRepProfile_ObjectIdentity((1,3,6,1,4,1,164,6,1,15,1))
_TstNePerfRepProfileTable_Object=MibTable
tstNePerfRepProfileTable=_TstNePerfRepProfileTable_Object((1,3,6,1,4,1,164,6,1,15,1,1))
if mibBuilder.loadTexts:tstNePerfRepProfileTable.setStatus(_A)
_TstNePerfRepProfileEntry_Object=MibTableRow
tstNePerfRepProfileEntry=_TstNePerfRepProfileEntry_Object((1,3,6,1,4,1,164,6,1,15,1,1,1))
tstNePerfRepProfileEntry.setIndexNames((0,_E,_AN))
if mibBuilder.loadTexts:tstNePerfRepProfileEntry.setStatus(_A)
_TstNePerfRepProfileId_Type=Unsigned32
_TstNePerfRepProfileId_Object=MibTableColumn
tstNePerfRepProfileId=_TstNePerfRepProfileId_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,1),_TstNePerfRepProfileId_Type())
tstNePerfRepProfileId.setMaxAccess(_I)
if mibBuilder.loadTexts:tstNePerfRepProfileId.setStatus(_A)
_TstNePerfRepProfileName_Type=SnmpAdminString
_TstNePerfRepProfileName_Object=MibTableColumn
tstNePerfRepProfileName=_TstNePerfRepProfileName_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,2),_TstNePerfRepProfileName_Type())
tstNePerfRepProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileName.setStatus(_A)
_TstNePerfRepProfileRowStatus_Type=RowStatus
_TstNePerfRepProfileRowStatus_Object=MibTableColumn
tstNePerfRepProfileRowStatus=_TstNePerfRepProfileRowStatus_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,3),_TstNePerfRepProfileRowStatus_Type())
tstNePerfRepProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileRowStatus.setStatus(_A)
_TstNePerfRepProfileFrameSize_Type=RadTestPerfRepFrameSize
_TstNePerfRepProfileFrameSize_Object=MibTableColumn
tstNePerfRepProfileFrameSize=_TstNePerfRepProfileFrameSize_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,4),_TstNePerfRepProfileFrameSize_Type())
tstNePerfRepProfileFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileFrameSize.setStatus(_A)
class _TstNePerfRepProfilePattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),('allOnes',2),(_AO,3),(_AP,4),(_AQ,5),(_AR,6),(_AS,7)))
_TstNePerfRepProfilePattern_Type.__name__=_G
_TstNePerfRepProfilePattern_Object=MibTableColumn
tstNePerfRepProfilePattern=_TstNePerfRepProfilePattern_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,5),_TstNePerfRepProfilePattern_Type())
tstNePerfRepProfilePattern.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfilePattern.setStatus(_A)
class _TstNePerfRepProfileDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),('uniDirectional',2),('biDirectional',3)))
_TstNePerfRepProfileDirection_Type.__name__=_G
_TstNePerfRepProfileDirection_Object=MibTableColumn
tstNePerfRepProfileDirection=_TstNePerfRepProfileDirection_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,6),_TstNePerfRepProfileDirection_Type())
tstNePerfRepProfileDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileDirection.setStatus(_A)
class _TstNePerfRepProfileTlv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('test',1),('data',2)))
_TstNePerfRepProfileTlv_Type.__name__=_G
_TstNePerfRepProfileTlv_Object=MibTableColumn
tstNePerfRepProfileTlv=_TstNePerfRepProfileTlv_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,7),_TstNePerfRepProfileTlv_Type())
tstNePerfRepProfileTlv.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileTlv.setStatus(_A)
_TstNePerfRepProfileNumberOfFramesInOneBurst_Type=Unsigned32
_TstNePerfRepProfileNumberOfFramesInOneBurst_Object=MibTableColumn
tstNePerfRepProfileNumberOfFramesInOneBurst=_TstNePerfRepProfileNumberOfFramesInOneBurst_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,8),_TstNePerfRepProfileNumberOfFramesInOneBurst_Type())
tstNePerfRepProfileNumberOfFramesInOneBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileNumberOfFramesInOneBurst.setStatus(_A)
_TstNePerfRepProfileFrameLossTolerance_Type=Unsigned32
_TstNePerfRepProfileFrameLossTolerance_Object=MibTableColumn
tstNePerfRepProfileFrameLossTolerance=_TstNePerfRepProfileFrameLossTolerance_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,9),_TstNePerfRepProfileFrameLossTolerance_Type())
tstNePerfRepProfileFrameLossTolerance.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileFrameLossTolerance.setStatus(_A)
_TstNePerfRepProfileBinarySearchResolution_Type=Unsigned32
_TstNePerfRepProfileBinarySearchResolution_Object=MibTableColumn
tstNePerfRepProfileBinarySearchResolution=_TstNePerfRepProfileBinarySearchResolution_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,10),_TstNePerfRepProfileBinarySearchResolution_Type())
tstNePerfRepProfileBinarySearchResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileBinarySearchResolution.setStatus(_A)
_TstNePerfRepProfileNumberOfTrials_Type=Unsigned32
_TstNePerfRepProfileNumberOfTrials_Object=MibTableColumn
tstNePerfRepProfileNumberOfTrials=_TstNePerfRepProfileNumberOfTrials_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,11),_TstNePerfRepProfileNumberOfTrials_Type())
tstNePerfRepProfileNumberOfTrials.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileNumberOfTrials.setStatus(_A)
class _TstNePerfRepProfileLearningFramesMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('none',2),('once',3),('oncePerTrial',4)))
_TstNePerfRepProfileLearningFramesMode_Type.__name__=_G
_TstNePerfRepProfileLearningFramesMode_Object=MibTableColumn
tstNePerfRepProfileLearningFramesMode=_TstNePerfRepProfileLearningFramesMode_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,12),_TstNePerfRepProfileLearningFramesMode_Type())
tstNePerfRepProfileLearningFramesMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileLearningFramesMode.setStatus(_A)
_TstNePerfRepProfileLearningFrames_Type=Unsigned32
_TstNePerfRepProfileLearningFrames_Object=MibTableColumn
tstNePerfRepProfileLearningFrames=_TstNePerfRepProfileLearningFrames_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,13),_TstNePerfRepProfileLearningFrames_Type())
tstNePerfRepProfileLearningFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileLearningFrames.setStatus(_A)
_TstNePerfRepProfileCustomSize_Type=Unsigned32
_TstNePerfRepProfileCustomSize_Object=MibTableColumn
tstNePerfRepProfileCustomSize=_TstNePerfRepProfileCustomSize_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,14),_TstNePerfRepProfileCustomSize_Type())
tstNePerfRepProfileCustomSize.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileCustomSize.setStatus(_A)
class _TstNePerfRepProfileTransmitLck_Type(TruthValue):defaultValue=1
_TstNePerfRepProfileTransmitLck_Type.__name__=_AM
_TstNePerfRepProfileTransmitLck_Object=MibTableColumn
tstNePerfRepProfileTransmitLck=_TstNePerfRepProfileTransmitLck_Object((1,3,6,1,4,1,164,6,1,15,1,1,1,15),_TstNePerfRepProfileTransmitLck_Type())
tstNePerfRepProfileTransmitLck.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepProfileTransmitLck.setStatus(_A)
_TstMepFlowTable_Object=MibTable
tstMepFlowTable=_TstMepFlowTable_Object((1,3,6,1,4,1,164,6,1,15,1,2))
if mibBuilder.loadTexts:tstMepFlowTable.setStatus(_A)
_TstMepFlowEntry_Object=MibTableRow
tstMepFlowEntry=_TstMepFlowEntry_Object((1,3,6,1,4,1,164,6,1,15,1,2,1))
tstMepFlowEntry.setIndexNames((0,_l,_AI),(0,_l,_AH),(0,_l,_AJ),(0,_E,_AT))
if mibBuilder.loadTexts:tstMepFlowEntry.setStatus(_A)
_TstMepFlowIndex_Type=Unsigned32
_TstMepFlowIndex_Object=MibTableColumn
tstMepFlowIndex=_TstMepFlowIndex_Object((1,3,6,1,4,1,164,6,1,15,1,2,1,1),_TstMepFlowIndex_Type())
tstMepFlowIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:tstMepFlowIndex.setStatus(_A)
_TstMepFlowFlowIdx_Type=RowPointer
_TstMepFlowFlowIdx_Object=MibTableColumn
tstMepFlowFlowIdx=_TstMepFlowFlowIdx_Object((1,3,6,1,4,1,164,6,1,15,1,2,1,2),_TstMepFlowFlowIdx_Type())
tstMepFlowFlowIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:tstMepFlowFlowIdx.setStatus(_A)
_ItuSatProfileTable_Object=MibTable
ituSatProfileTable=_ItuSatProfileTable_Object((1,3,6,1,4,1,164,6,1,15,1,3))
if mibBuilder.loadTexts:ituSatProfileTable.setStatus(_A)
_ItuSatProfileEntry_Object=MibTableRow
ituSatProfileEntry=_ItuSatProfileEntry_Object((1,3,6,1,4,1,164,6,1,15,1,3,1))
ituSatProfileEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:ituSatProfileEntry.setStatus(_A)
_ItuSatProfileIndex_Type=Unsigned32
_ItuSatProfileIndex_Object=MibTableColumn
ituSatProfileIndex=_ItuSatProfileIndex_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,1),_ItuSatProfileIndex_Type())
ituSatProfileIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatProfileIndex.setStatus(_A)
class _ItuSatProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ItuSatProfileName_Type.__name__=_R
_ItuSatProfileName_Object=MibTableColumn
ituSatProfileName=_ItuSatProfileName_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,2),_ItuSatProfileName_Type())
ituSatProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileName.setStatus(_A)
_ItuSatProfileRowStatus_Type=RowStatus
_ItuSatProfileRowStatus_Object=MibTableColumn
ituSatProfileRowStatus=_ItuSatProfileRowStatus_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,3),_ItuSatProfileRowStatus_Type())
ituSatProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileRowStatus.setStatus(_A)
class _ItuSatProfileEtherType_Type(OctetString):defaultHexValue='22E8';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_ItuSatProfileEtherType_Type.__name__=_x
_ItuSatProfileEtherType_Object=MibTableColumn
ituSatProfileEtherType=_ItuSatProfileEtherType_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,4),_ItuSatProfileEtherType_Type())
ituSatProfileEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileEtherType.setStatus(_A)
class _ItuSatProfileFrameSize_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12000))
_ItuSatProfileFrameSize_Type.__name__=_H
_ItuSatProfileFrameSize_Object=MibTableColumn
ituSatProfileFrameSize=_ItuSatProfileFrameSize_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,5),_ItuSatProfileFrameSize_Type())
ituSatProfileFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileFrameSize.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileFrameSize.setUnits(_g)
class _ItuSatProfileUniFlrThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileUniFlrThreshold_Type.__name__=_H
_ItuSatProfileUniFlrThreshold_Object=MibTableColumn
ituSatProfileUniFlrThreshold=_ItuSatProfileUniFlrThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,6),_ItuSatProfileUniFlrThreshold_Type())
ituSatProfileUniFlrThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileUniFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileUniFlrThreshold.setUnits(_m)
class _ItuSatProfileUniFtdThreshold_Type(Unsigned32):defaultValue=13000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileUniFtdThreshold_Type.__name__=_H
_ItuSatProfileUniFtdThreshold_Object=MibTableColumn
ituSatProfileUniFtdThreshold=_ItuSatProfileUniFtdThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,7),_ItuSatProfileUniFtdThreshold_Type())
ituSatProfileUniFtdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileUniFtdThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileUniFtdThreshold.setUnits(_F)
class _ItuSatProfileUniFdvThreshold_Type(Unsigned32):defaultValue=8000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileUniFdvThreshold_Type.__name__=_H
_ItuSatProfileUniFdvThreshold_Object=MibTableColumn
ituSatProfileUniFdvThreshold=_ItuSatProfileUniFdvThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,8),_ItuSatProfileUniFdvThreshold_Type())
ituSatProfileUniFdvThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileUniFdvThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileUniFdvThreshold.setUnits(_F)
class _ItuSatProfileUniAvailThreshold_Type(Unsigned32):defaultValue=9990;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ItuSatProfileUniAvailThreshold_Type.__name__=_H
_ItuSatProfileUniAvailThreshold_Object=MibTableColumn
ituSatProfileUniAvailThreshold=_ItuSatProfileUniAvailThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,9),_ItuSatProfileUniAvailThreshold_Type())
ituSatProfileUniAvailThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileUniAvailThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileUniAvailThreshold.setUnits(_h)
class _ItuSatProfileBiFlrThreshold_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileBiFlrThreshold_Type.__name__=_H
_ItuSatProfileBiFlrThreshold_Object=MibTableColumn
ituSatProfileBiFlrThreshold=_ItuSatProfileBiFlrThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,10),_ItuSatProfileBiFlrThreshold_Type())
ituSatProfileBiFlrThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileBiFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileBiFlrThreshold.setUnits(_m)
class _ItuSatProfileBiFtdThreshold_Type(Unsigned32):defaultValue=26000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileBiFtdThreshold_Type.__name__=_H
_ItuSatProfileBiFtdThreshold_Object=MibTableColumn
ituSatProfileBiFtdThreshold=_ItuSatProfileBiFtdThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,11),_ItuSatProfileBiFtdThreshold_Type())
ituSatProfileBiFtdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileBiFtdThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileBiFtdThreshold.setUnits(_F)
class _ItuSatProfileBiFdvThreshold_Type(Unsigned32):defaultValue=11000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfileBiFdvThreshold_Type.__name__=_H
_ItuSatProfileBiFdvThreshold_Object=MibTableColumn
ituSatProfileBiFdvThreshold=_ItuSatProfileBiFdvThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,12),_ItuSatProfileBiFdvThreshold_Type())
ituSatProfileBiFdvThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileBiFdvThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileBiFdvThreshold.setUnits(_F)
class _ItuSatProfileBiAvailThreshold_Type(Unsigned32):defaultValue=9990;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ItuSatProfileBiAvailThreshold_Type.__name__=_H
_ItuSatProfileBiAvailThreshold_Object=MibTableColumn
ituSatProfileBiAvailThreshold=_ItuSatProfileBiAvailThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,13),_ItuSatProfileBiAvailThreshold_Type())
ituSatProfileBiAvailThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileBiAvailThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileBiAvailThreshold.setUnits(_h)
class _ItuSatProfileScope_Type(Bits):defaultBinValue='11';namedValues=NamedValues(*((_A0,0),(_n,1)))
_ItuSatProfileScope_Type.__name__=_Y
_ItuSatProfileScope_Object=MibTableColumn
ituSatProfileScope=_ItuSatProfileScope_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,14),_ItuSatProfileScope_Type())
ituSatProfileScope.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileScope.setStatus(_A)
class _ItuSatProfileDirection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_ItuSatProfileDirection_Type.__name__=_G
_ItuSatProfileDirection_Object=MibTableColumn
ituSatProfileDirection=_ItuSatProfileDirection_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,15),_ItuSatProfileDirection_Type())
ituSatProfileDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileDirection.setStatus(_A)
class _ItuSatProfileColorMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('colorAware',1),('colorBlind',2)))
_ItuSatProfileColorMode_Type.__name__=_G
_ItuSatProfileColorMode_Object=MibTableColumn
ituSatProfileColorMode=_ItuSatProfileColorMode_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,16),_ItuSatProfileColorMode_Type())
ituSatProfileColorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileColorMode.setStatus(_A)
class _ItuSatProfileTrafficPolicing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ItuSatProfileTrafficPolicing_Type.__name__=_G
_ItuSatProfileTrafficPolicing_Object=MibTableColumn
ituSatProfileTrafficPolicing=_ItuSatProfileTrafficPolicing_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,17),_ItuSatProfileTrafficPolicing_Type())
ituSatProfileTrafficPolicing.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileTrafficPolicing.setStatus(_A)
class _ItuSatProfileCirSteps_Type(OctetString):defaultHexValue='19324B64';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ItuSatProfileCirSteps_Type.__name__=_x
_ItuSatProfileCirSteps_Object=MibTableColumn
ituSatProfileCirSteps=_ItuSatProfileCirSteps_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,18),_ItuSatProfileCirSteps_Type())
ituSatProfileCirSteps.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileCirSteps.setStatus(_A)
class _ItuSatProfileConfDuration_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(18,360))
_ItuSatProfileConfDuration_Type.__name__=_H
_ItuSatProfileConfDuration_Object=MibTableColumn
ituSatProfileConfDuration=_ItuSatProfileConfDuration_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,19),_ItuSatProfileConfDuration_Type())
ituSatProfileConfDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileConfDuration.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfileConfDuration.setUnits(_P)
class _ItuSatProfilePerfDuration_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7200))
_ItuSatProfilePerfDuration_Type.__name__=_H
_ItuSatProfilePerfDuration_Object=MibTableColumn
ituSatProfilePerfDuration=_ItuSatProfilePerfDuration_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,20),_ItuSatProfilePerfDuration_Type())
ituSatProfilePerfDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePerfDuration.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePerfDuration.setUnits(_A1)
class _ItuSatProfileRateConvention_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dataRate',1),('lineRate',2)))
_ItuSatProfileRateConvention_Type.__name__=_G
_ItuSatProfileRateConvention_Object=MibTableColumn
ituSatProfileRateConvention=_ItuSatProfileRateConvention_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,21),_ItuSatProfileRateConvention_Type())
ituSatProfileRateConvention.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileRateConvention.setStatus(_A)
class _ItuSatProfileResponderType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('y1564',1),('macSwapLoopback',2),('mef46Ll',3)))
_ItuSatProfileResponderType_Type.__name__=_G
_ItuSatProfileResponderType_Object=MibTableColumn
ituSatProfileResponderType=_ItuSatProfileResponderType_Object((1,3,6,1,4,1,164,6,1,15,1,3,1,22),_ItuSatProfileResponderType_Type())
ituSatProfileResponderType.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfileResponderType.setStatus(_A)
_ItuSatProfilePbitTable_Object=MibTable
ituSatProfilePbitTable=_ItuSatProfilePbitTable_Object((1,3,6,1,4,1,164,6,1,15,1,4))
if mibBuilder.loadTexts:ituSatProfilePbitTable.setStatus(_A)
_ItuSatProfilePbitEntry_Object=MibTableRow
ituSatProfilePbitEntry=_ItuSatProfilePbitEntry_Object((1,3,6,1,4,1,164,6,1,15,1,4,1))
ituSatProfilePbitEntry.setIndexNames((0,_E,_z),(0,_E,_AU))
if mibBuilder.loadTexts:ituSatProfilePbitEntry.setStatus(_A)
_ItuSatProfilePbitIndex_Type=RadTestPbitIndex
_ItuSatProfilePbitIndex_Object=MibTableColumn
ituSatProfilePbitIndex=_ItuSatProfilePbitIndex_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,1),_ItuSatProfilePbitIndex_Type())
ituSatProfilePbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatProfilePbitIndex.setStatus(_A)
_ItuSatProfilePbitRowStatus_Type=RowStatus
_ItuSatProfilePbitRowStatus_Object=MibTableColumn
ituSatProfilePbitRowStatus=_ItuSatProfilePbitRowStatus_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,2),_ItuSatProfilePbitRowStatus_Type())
ituSatProfilePbitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitRowStatus.setStatus(_A)
class _ItuSatProfilePbitFrameSize_Type(Unsigned32):defaultValue=512;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12000))
_ItuSatProfilePbitFrameSize_Type.__name__=_H
_ItuSatProfilePbitFrameSize_Object=MibTableColumn
ituSatProfilePbitFrameSize=_ItuSatProfilePbitFrameSize_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,3),_ItuSatProfilePbitFrameSize_Type())
ituSatProfilePbitFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitFrameSize.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitFrameSize.setUnits(_g)
class _ItuSatProfilePbitUniFlrThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitUniFlrThreshold_Type.__name__=_H
_ItuSatProfilePbitUniFlrThreshold_Object=MibTableColumn
ituSatProfilePbitUniFlrThreshold=_ItuSatProfilePbitUniFlrThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,4),_ItuSatProfilePbitUniFlrThreshold_Type())
ituSatProfilePbitUniFlrThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitUniFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitUniFlrThreshold.setUnits(_m)
class _ItuSatProfilePbitUniFtdThreshold_Type(Unsigned32):defaultValue=13;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitUniFtdThreshold_Type.__name__=_H
_ItuSatProfilePbitUniFtdThreshold_Object=MibTableColumn
ituSatProfilePbitUniFtdThreshold=_ItuSatProfilePbitUniFtdThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,5),_ItuSatProfilePbitUniFtdThreshold_Type())
ituSatProfilePbitUniFtdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitUniFtdThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitUniFtdThreshold.setUnits(_F)
class _ItuSatProfilePbitUniFdvThreshold_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitUniFdvThreshold_Type.__name__=_H
_ItuSatProfilePbitUniFdvThreshold_Object=MibTableColumn
ituSatProfilePbitUniFdvThreshold=_ItuSatProfilePbitUniFdvThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,6),_ItuSatProfilePbitUniFdvThreshold_Type())
ituSatProfilePbitUniFdvThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitUniFdvThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitUniFdvThreshold.setUnits(_F)
class _ItuSatProfilePbitUniAvailThreshold_Type(Unsigned32):defaultValue=9990;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ItuSatProfilePbitUniAvailThreshold_Type.__name__=_H
_ItuSatProfilePbitUniAvailThreshold_Object=MibTableColumn
ituSatProfilePbitUniAvailThreshold=_ItuSatProfilePbitUniAvailThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,7),_ItuSatProfilePbitUniAvailThreshold_Type())
ituSatProfilePbitUniAvailThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitUniAvailThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitUniAvailThreshold.setUnits(_h)
class _ItuSatProfilePbitBiFlrThreshold_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitBiFlrThreshold_Type.__name__=_H
_ItuSatProfilePbitBiFlrThreshold_Object=MibTableColumn
ituSatProfilePbitBiFlrThreshold=_ItuSatProfilePbitBiFlrThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,8),_ItuSatProfilePbitBiFlrThreshold_Type())
ituSatProfilePbitBiFlrThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitBiFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitBiFlrThreshold.setUnits(_m)
class _ItuSatProfilePbitBiFtdThreshold_Type(Unsigned32):defaultValue=26;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitBiFtdThreshold_Type.__name__=_H
_ItuSatProfilePbitBiFtdThreshold_Object=MibTableColumn
ituSatProfilePbitBiFtdThreshold=_ItuSatProfilePbitBiFtdThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,9),_ItuSatProfilePbitBiFtdThreshold_Type())
ituSatProfilePbitBiFtdThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitBiFtdThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitBiFtdThreshold.setUnits(_F)
class _ItuSatProfilePbitBiFdvThreshold_Type(Unsigned32):defaultValue=11;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_ItuSatProfilePbitBiFdvThreshold_Type.__name__=_H
_ItuSatProfilePbitBiFdvThreshold_Object=MibTableColumn
ituSatProfilePbitBiFdvThreshold=_ItuSatProfilePbitBiFdvThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,10),_ItuSatProfilePbitBiFdvThreshold_Type())
ituSatProfilePbitBiFdvThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitBiFdvThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitBiFdvThreshold.setUnits(_F)
class _ItuSatProfilePbitBiAvailThreshold_Type(Unsigned32):defaultValue=9990;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ItuSatProfilePbitBiAvailThreshold_Type.__name__=_H
_ItuSatProfilePbitBiAvailThreshold_Object=MibTableColumn
ituSatProfilePbitBiAvailThreshold=_ItuSatProfilePbitBiAvailThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,4,1,11),_ItuSatProfilePbitBiAvailThreshold_Type())
ituSatProfilePbitBiAvailThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatProfilePbitBiAvailThreshold.setStatus(_A)
if mibBuilder.loadTexts:ituSatProfilePbitBiAvailThreshold.setUnits(_h)
_TwampTestProfileTable_Object=MibTable
twampTestProfileTable=_TwampTestProfileTable_Object((1,3,6,1,4,1,164,6,1,15,1,5))
if mibBuilder.loadTexts:twampTestProfileTable.setStatus(_A)
_TwampTestProfileEntry_Object=MibTableRow
twampTestProfileEntry=_TwampTestProfileEntry_Object((1,3,6,1,4,1,164,6,1,15,1,5,1))
twampTestProfileEntry.setIndexNames((0,_E,_AV))
if mibBuilder.loadTexts:twampTestProfileEntry.setStatus(_A)
_TwampTestProfileId_Type=Unsigned32
_TwampTestProfileId_Object=MibTableColumn
twampTestProfileId=_TwampTestProfileId_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,1),_TwampTestProfileId_Type())
twampTestProfileId.setMaxAccess(_I)
if mibBuilder.loadTexts:twampTestProfileId.setStatus(_A)
_TwampTestProfileRowStatus_Type=RowStatus
_TwampTestProfileRowStatus_Object=MibTableColumn
twampTestProfileRowStatus=_TwampTestProfileRowStatus_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,2),_TwampTestProfileRowStatus_Type())
twampTestProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileRowStatus.setStatus(_A)
class _TwampTestProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TwampTestProfileName_Type.__name__=_R
_TwampTestProfileName_Object=MibTableColumn
twampTestProfileName=_TwampTestProfileName_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,3),_TwampTestProfileName_Type())
twampTestProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileName.setStatus(_A)
_TwampTestProfilePayloadLength_Type=Unsigned32
_TwampTestProfilePayloadLength_Object=MibTableColumn
twampTestProfilePayloadLength=_TwampTestProfilePayloadLength_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,4),_TwampTestProfilePayloadLength_Type())
twampTestProfilePayloadLength.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfilePayloadLength.setStatus(_A)
if mibBuilder.loadTexts:twampTestProfilePayloadLength.setUnits(_g)
_TwampTestProfileTxRate_Type=Unsigned32
_TwampTestProfileTxRate_Object=MibTableColumn
twampTestProfileTxRate=_TwampTestProfileTxRate_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,5),_TwampTestProfileTxRate_Type())
twampTestProfileTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileTxRate.setStatus(_A)
_TwampTestProfileLossTimeout_Type=Unsigned32
_TwampTestProfileLossTimeout_Object=MibTableColumn
twampTestProfileLossTimeout=_TwampTestProfileLossTimeout_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,6),_TwampTestProfileLossTimeout_Type())
twampTestProfileLossTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileLossTimeout.setStatus(_A)
if mibBuilder.loadTexts:twampTestProfileLossTimeout.setUnits(_F)
_TwampTestProfileLossRatioThreshold_Type=Unsigned32
_TwampTestProfileLossRatioThreshold_Object=MibTableColumn
twampTestProfileLossRatioThreshold=_TwampTestProfileLossRatioThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,7),_TwampTestProfileLossRatioThreshold_Type())
twampTestProfileLossRatioThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileLossRatioThreshold.setStatus(_A)
_TwampTestProfileDelayThreshold_Type=Unsigned32
_TwampTestProfileDelayThreshold_Object=MibTableColumn
twampTestProfileDelayThreshold=_TwampTestProfileDelayThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,8),_TwampTestProfileDelayThreshold_Type())
twampTestProfileDelayThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileDelayThreshold.setStatus(_A)
if mibBuilder.loadTexts:twampTestProfileDelayThreshold.setUnits(_F)
_TwampTestProfileDelayVarThreshold_Type=Unsigned32
_TwampTestProfileDelayVarThreshold_Object=MibTableColumn
twampTestProfileDelayVarThreshold=_TwampTestProfileDelayVarThreshold_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,9),_TwampTestProfileDelayVarThreshold_Type())
twampTestProfileDelayVarThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileDelayVarThreshold.setStatus(_A)
if mibBuilder.loadTexts:twampTestProfileDelayVarThreshold.setUnits(_F)
class _TwampTestProfileDelayVarEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('pdvMax',2),('ipdvMax',3)))
_TwampTestProfileDelayVarEventType_Type.__name__=_G
_TwampTestProfileDelayVarEventType_Object=MibTableColumn
twampTestProfileDelayVarEventType=_TwampTestProfileDelayVarEventType_Object((1,3,6,1,4,1,164,6,1,15,1,5,1,10),_TwampTestProfileDelayVarEventType_Type())
twampTestProfileDelayVarEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:twampTestProfileDelayVarEventType.setStatus(_A)
_RadTestPrefRepTest_ObjectIdentity=ObjectIdentity
radTestPrefRepTest=_RadTestPrefRepTest_ObjectIdentity((1,3,6,1,4,1,164,6,1,15,2))
_TstNePerfRepTestTable_Object=MibTable
tstNePerfRepTestTable=_TstNePerfRepTestTable_Object((1,3,6,1,4,1,164,6,1,15,2,1))
if mibBuilder.loadTexts:tstNePerfRepTestTable.setStatus(_A)
_TstNePerfRepTestEntry_Object=MibTableRow
tstNePerfRepTestEntry=_TstNePerfRepTestEntry_Object((1,3,6,1,4,1,164,6,1,15,2,1,1))
tstNePerfRepTestEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:tstNePerfRepTestEntry.setStatus(_A)
_TstNePerfRepTestId_Type=Unsigned32
_TstNePerfRepTestId_Object=MibTableColumn
tstNePerfRepTestId=_TstNePerfRepTestId_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,1),_TstNePerfRepTestId_Type())
tstNePerfRepTestId.setMaxAccess(_I)
if mibBuilder.loadTexts:tstNePerfRepTestId.setStatus(_A)
_TstNePerfRepTestRowStatus_Type=RowStatus
_TstNePerfRepTestRowStatus_Object=MibTableColumn
tstNePerfRepTestRowStatus=_TstNePerfRepTestRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,2),_TstNePerfRepTestRowStatus_Type())
tstNePerfRepTestRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestRowStatus.setStatus(_A)
class _TstNePerfRepTestType_Type(Bits):namedValues=NamedValues(*((_A2,0),(_A3,1),(_A4,2)))
_TstNePerfRepTestType_Type.__name__=_Y
_TstNePerfRepTestType_Object=MibTableColumn
tstNePerfRepTestType=_TstNePerfRepTestType_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,3),_TstNePerfRepTestType_Type())
tstNePerfRepTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestType.setStatus(_A)
_TstNePerfRepTestProfileId_Type=Unsigned32
_TstNePerfRepTestProfileId_Object=MibTableColumn
tstNePerfRepTestProfileId=_TstNePerfRepTestProfileId_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,4),_TstNePerfRepTestProfileId_Type())
tstNePerfRepTestProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestProfileId.setStatus(_A)
_TstNePerfRepTestEntity_Type=RowPointer
_TstNePerfRepTestEntity_Object=MibTableColumn
tstNePerfRepTestEntity=_TstNePerfRepTestEntity_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,5),_TstNePerfRepTestEntity_Type())
tstNePerfRepTestEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestEntity.setStatus(_A)
class _TstNePerfRepTestActivation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_T,1),('now',2),('dateAndTime',3),('daily',4),('cancelTest',255)))
_TstNePerfRepTestActivation_Type.__name__=_G
_TstNePerfRepTestActivation_Object=MibTableColumn
tstNePerfRepTestActivation=_TstNePerfRepTestActivation_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,6),_TstNePerfRepTestActivation_Type())
tstNePerfRepTestActivation.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestActivation.setStatus(_A)
class _TstNePerfRepTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_A5,1),(_b,2),('pending',3),(_AW,4),(_A6,5)))
_TstNePerfRepTestStatus_Type.__name__=_G
_TstNePerfRepTestStatus_Object=MibTableColumn
tstNePerfRepTestStatus=_TstNePerfRepTestStatus_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,7),_TstNePerfRepTestStatus_Type())
tstNePerfRepTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepTestStatus.setStatus(_A)
_TstNePerfRepTestActivationDateAndTime_Type=DateAndTime
_TstNePerfRepTestActivationDateAndTime_Object=MibTableColumn
tstNePerfRepTestActivationDateAndTime=_TstNePerfRepTestActivationDateAndTime_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,8),_TstNePerfRepTestActivationDateAndTime_Type())
tstNePerfRepTestActivationDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestActivationDateAndTime.setStatus(_A)
_TstNePerfRepTestActivationRecurrenceTime_Type=Unsigned32
_TstNePerfRepTestActivationRecurrenceTime_Object=MibTableColumn
tstNePerfRepTestActivationRecurrenceTime=_TstNePerfRepTestActivationRecurrenceTime_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,9),_TstNePerfRepTestActivationRecurrenceTime_Type())
tstNePerfRepTestActivationRecurrenceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestActivationRecurrenceTime.setStatus(_A)
_TstNePerfRepTestMaxRate_Type=Unsigned32
_TstNePerfRepTestMaxRate_Object=MibTableColumn
tstNePerfRepTestMaxRate=_TstNePerfRepTestMaxRate_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,10),_TstNePerfRepTestMaxRate_Type())
tstNePerfRepTestMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestMaxRate.setStatus(_A)
_TstNePerfRepTestElapsedTime_Type=TimeTicks
_TstNePerfRepTestElapsedTime_Object=MibTableColumn
tstNePerfRepTestElapsedTime=_TstNePerfRepTestElapsedTime_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,11),_TstNePerfRepTestElapsedTime_Type())
tstNePerfRepTestElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepTestElapsedTime.setStatus(_A)
class _TstNePerfRepTestResetResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),(_X,3)))
_TstNePerfRepTestResetResults_Type.__name__=_G
_TstNePerfRepTestResetResults_Object=MibTableColumn
tstNePerfRepTestResetResults=_TstNePerfRepTestResetResults_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,12),_TstNePerfRepTestResetResults_Type())
tstNePerfRepTestResetResults.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestResetResults.setStatus(_A)
class _TstNePerfRepTestRateConvention_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('lineRate',2),('dataRate',3)))
_TstNePerfRepTestRateConvention_Type.__name__=_G
_TstNePerfRepTestRateConvention_Object=MibTableColumn
tstNePerfRepTestRateConvention=_TstNePerfRepTestRateConvention_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,13),_TstNePerfRepTestRateConvention_Type())
tstNePerfRepTestRateConvention.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestRateConvention.setStatus(_A)
_TstNePerfRepTestFrameCompensation_Type=Unsigned32
_TstNePerfRepTestFrameCompensation_Object=MibTableColumn
tstNePerfRepTestFrameCompensation=_TstNePerfRepTestFrameCompensation_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,14),_TstNePerfRepTestFrameCompensation_Type())
tstNePerfRepTestFrameCompensation.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestFrameCompensation.setStatus(_A)
class _TstNePerfRepTestMaxTestDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,60))
_TstNePerfRepTestMaxTestDuration_Type.__name__=_H
_TstNePerfRepTestMaxTestDuration_Object=MibTableColumn
tstNePerfRepTestMaxTestDuration=_TstNePerfRepTestMaxTestDuration_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,15),_TstNePerfRepTestMaxTestDuration_Type())
tstNePerfRepTestMaxTestDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestMaxTestDuration.setStatus(_A)
_TstNePerfRepTestAssociatedFlow_Type=RowPointer
_TstNePerfRepTestAssociatedFlow_Object=MibTableColumn
tstNePerfRepTestAssociatedFlow=_TstNePerfRepTestAssociatedFlow_Object((1,3,6,1,4,1,164,6,1,15,2,1,1,16),_TstNePerfRepTestAssociatedFlow_Type())
tstNePerfRepTestAssociatedFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:tstNePerfRepTestAssociatedFlow.setStatus(_A)
_ItuSatGeneratorTable_Object=MibTable
ituSatGeneratorTable=_ItuSatGeneratorTable_Object((1,3,6,1,4,1,164,6,1,15,2,2))
if mibBuilder.loadTexts:ituSatGeneratorTable.setStatus(_A)
_ItuSatGeneratorEntry_Object=MibTableRow
ituSatGeneratorEntry=_ItuSatGeneratorEntry_Object((1,3,6,1,4,1,164,6,1,15,2,2,1))
ituSatGeneratorEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:ituSatGeneratorEntry.setStatus(_A)
_ItuSatGeneratorIndex_Type=Unsigned32
_ItuSatGeneratorIndex_Object=MibTableColumn
ituSatGeneratorIndex=_ItuSatGeneratorIndex_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,1),_ItuSatGeneratorIndex_Type())
ituSatGeneratorIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatGeneratorIndex.setStatus(_A)
class _ItuSatGeneratorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ItuSatGeneratorName_Type.__name__=_R
_ItuSatGeneratorName_Object=MibTableColumn
ituSatGeneratorName=_ItuSatGeneratorName_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,2),_ItuSatGeneratorName_Type())
ituSatGeneratorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorName.setStatus(_A)
_ItuSatGeneratorRowStatus_Type=RowStatus
_ItuSatGeneratorRowStatus_Object=MibTableColumn
ituSatGeneratorRowStatus=_ItuSatGeneratorRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,3),_ItuSatGeneratorRowStatus_Type())
ituSatGeneratorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorRowStatus.setStatus(_A)
_ItuSatGeneratorServicePointer_Type=RowPointer
_ItuSatGeneratorServicePointer_Object=MibTableColumn
ituSatGeneratorServicePointer=_ItuSatGeneratorServicePointer_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,4),_ItuSatGeneratorServicePointer_Type())
ituSatGeneratorServicePointer.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorServicePointer.setStatus(_A)
class _ItuSatGeneratorProvisionedPbits_Type(RadTestPbitValues):defaultBinValue='0'
_ItuSatGeneratorProvisionedPbits_Type.__name__=_AK
_ItuSatGeneratorProvisionedPbits_Object=MibTableColumn
ituSatGeneratorProvisionedPbits=_ItuSatGeneratorProvisionedPbits_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,5),_ItuSatGeneratorProvisionedPbits_Type())
ituSatGeneratorProvisionedPbits.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorProvisionedPbits.setStatus(_A)
class _ItuSatGeneratorProfile_Type(Unsigned32):defaultValue=0
_ItuSatGeneratorProfile_Type.__name__=_H
_ItuSatGeneratorProfile_Object=MibTableColumn
ituSatGeneratorProfile=_ItuSatGeneratorProfile_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,6),_ItuSatGeneratorProfile_Type())
ituSatGeneratorProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorProfile.setStatus(_A)
class _ItuSatGeneratorCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_ItuSatGeneratorCmd_Type.__name__=_G
_ItuSatGeneratorCmd_Object=MibTableColumn
ituSatGeneratorCmd=_ItuSatGeneratorCmd_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,7),_ItuSatGeneratorCmd_Type())
ituSatGeneratorCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorCmd.setStatus(_A)
_ItuSatGeneratorConfChanged_Type=TruthValue
_ItuSatGeneratorConfChanged_Object=MibTableColumn
ituSatGeneratorConfChanged=_ItuSatGeneratorConfChanged_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,8),_ItuSatGeneratorConfChanged_Type())
ituSatGeneratorConfChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorConfChanged.setStatus(_A)
class _ItuSatGeneratorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Z,1),(_i,2),(_b,3),('passed',4),('failed',5),(_AX,6),(_AY,7),('llFailure',8)))
_ItuSatGeneratorStatus_Type.__name__=_G
_ItuSatGeneratorStatus_Object=MibTableColumn
ituSatGeneratorStatus=_ItuSatGeneratorStatus_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,9),_ItuSatGeneratorStatus_Type())
ituSatGeneratorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorStatus.setStatus(_A)
_ItuSatGeneratorTimeRemaining_Type=Unsigned32
_ItuSatGeneratorTimeRemaining_Object=MibTableColumn
ituSatGeneratorTimeRemaining=_ItuSatGeneratorTimeRemaining_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,10),_ItuSatGeneratorTimeRemaining_Type())
ituSatGeneratorTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorTimeRemaining.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorTimeRemaining.setUnits(_P)
class _ItuSatGeneratorCurrentPhase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_A0,2),(_n,3)))
_ItuSatGeneratorCurrentPhase_Type.__name__=_G
_ItuSatGeneratorCurrentPhase_Object=MibTableColumn
ituSatGeneratorCurrentPhase=_ItuSatGeneratorCurrentPhase_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,11),_ItuSatGeneratorCurrentPhase_Type())
ituSatGeneratorCurrentPhase.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorCurrentPhase.setStatus(_A)
_ItuSatGeneratorDestination_Type=MacAddress
_ItuSatGeneratorDestination_Object=MibTableColumn
ituSatGeneratorDestination=_ItuSatGeneratorDestination_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,12),_ItuSatGeneratorDestination_Type())
ituSatGeneratorDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorDestination.setStatus(_A)
_ItuSatGeneratorSource_Type=MacAddress
_ItuSatGeneratorSource_Object=MibTableColumn
ituSatGeneratorSource=_ItuSatGeneratorSource_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,13),_ItuSatGeneratorSource_Type())
ituSatGeneratorSource.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorSource.setStatus(_A)
class _ItuSatGeneratorInnerTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ItuSatGeneratorInnerTag_Type.__name__=_H
_ItuSatGeneratorInnerTag_Object=MibTableColumn
ituSatGeneratorInnerTag=_ItuSatGeneratorInnerTag_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,14),_ItuSatGeneratorInnerTag_Type())
ituSatGeneratorInnerTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorInnerTag.setStatus(_A)
class _ItuSatGeneratorOuterTag_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ItuSatGeneratorOuterTag_Type.__name__=_H
_ItuSatGeneratorOuterTag_Object=MibTableColumn
ituSatGeneratorOuterTag=_ItuSatGeneratorOuterTag_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,15),_ItuSatGeneratorOuterTag_Type())
ituSatGeneratorOuterTag.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorOuterTag.setStatus(_A)
_ItuSatGeneratorTestedPbits_Type=RadTestPbitValues
_ItuSatGeneratorTestedPbits_Object=MibTableColumn
ituSatGeneratorTestedPbits=_ItuSatGeneratorTestedPbits_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,16),_ItuSatGeneratorTestedPbits_Type())
ituSatGeneratorTestedPbits.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorTestedPbits.setStatus(_A)
_ItuSatGeneratorStartTime_Type=DateAndTime
_ItuSatGeneratorStartTime_Object=MibTableColumn
ituSatGeneratorStartTime=_ItuSatGeneratorStartTime_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,17),_ItuSatGeneratorStartTime_Type())
ituSatGeneratorStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorStartTime.setStatus(_A)
_ItuSatGeneratorEndTime_Type=DateAndTime
_ItuSatGeneratorEndTime_Object=MibTableColumn
ituSatGeneratorEndTime=_ItuSatGeneratorEndTime_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,18),_ItuSatGeneratorEndTime_Type())
ituSatGeneratorEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorEndTime.setStatus(_A)
_ItuSatGeneratorTimeElapsed_Type=Unsigned32
_ItuSatGeneratorTimeElapsed_Object=MibTableColumn
ituSatGeneratorTimeElapsed=_ItuSatGeneratorTimeElapsed_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,19),_ItuSatGeneratorTimeElapsed_Type())
ituSatGeneratorTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorTimeElapsed.setUnits(_P)
_ItuSatGeneratorConfResult_Type=RadTestResult
_ItuSatGeneratorConfResult_Object=MibTableColumn
ituSatGeneratorConfResult=_ItuSatGeneratorConfResult_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,20),_ItuSatGeneratorConfResult_Type())
ituSatGeneratorConfResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorConfResult.setStatus(_A)
_ItuSatGeneratorPerfResult_Type=RadTestResult
_ItuSatGeneratorPerfResult_Object=MibTableColumn
ituSatGeneratorPerfResult=_ItuSatGeneratorPerfResult_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,21),_ItuSatGeneratorPerfResult_Type())
ituSatGeneratorPerfResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorPerfResult.setStatus(_A)
class _ItuSatGeneratorConfDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(18,360))
_ItuSatGeneratorConfDuration_Type.__name__=_H
_ItuSatGeneratorConfDuration_Object=MibTableColumn
ituSatGeneratorConfDuration=_ItuSatGeneratorConfDuration_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,22),_ItuSatGeneratorConfDuration_Type())
ituSatGeneratorConfDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorConfDuration.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorConfDuration.setUnits(_P)
class _ItuSatGeneratorPerfDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,7200))
_ItuSatGeneratorPerfDuration_Type.__name__=_H
_ItuSatGeneratorPerfDuration_Object=MibTableColumn
ituSatGeneratorPerfDuration=_ItuSatGeneratorPerfDuration_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,23),_ItuSatGeneratorPerfDuration_Type())
ituSatGeneratorPerfDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorPerfDuration.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorPerfDuration.setUnits(_A1)
class _ItuSatGeneratorScope_Type(Bits):namedValues=NamedValues(*((_A0,0),(_n,1)))
_ItuSatGeneratorScope_Type.__name__=_Y
_ItuSatGeneratorScope_Object=MibTableColumn
ituSatGeneratorScope=_ItuSatGeneratorScope_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,24),_ItuSatGeneratorScope_Type())
ituSatGeneratorScope.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorScope.setStatus(_A)
class _ItuSatGeneratorServiceBinding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ma',1),(_AZ,2),(_Aa,3),(_Ab,4)))
_ItuSatGeneratorServiceBinding_Type.__name__=_G
_ItuSatGeneratorServiceBinding_Object=MibTableColumn
ituSatGeneratorServiceBinding=_ItuSatGeneratorServiceBinding_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,25),_ItuSatGeneratorServiceBinding_Type())
ituSatGeneratorServiceBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorServiceBinding.setStatus(_A)
class _ItuSatGeneratorServiceName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ItuSatGeneratorServiceName_Type.__name__=_R
_ItuSatGeneratorServiceName_Object=MibTableColumn
ituSatGeneratorServiceName=_ItuSatGeneratorServiceName_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,26),_ItuSatGeneratorServiceName_Type())
ituSatGeneratorServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorServiceName.setStatus(_A)
class _ItuSatGeneratorEgressPort_Type(InterfaceIndexOrZero):defaultValue=0
_ItuSatGeneratorEgressPort_Type.__name__=_y
_ItuSatGeneratorEgressPort_Object=MibTableColumn
ituSatGeneratorEgressPort=_ItuSatGeneratorEgressPort_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,27),_ItuSatGeneratorEgressPort_Type())
ituSatGeneratorEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorEgressPort.setStatus(_A)
class _ItuSatGeneratorProvisionedDestination_Type(MacAddress):defaultHexValue='000000000000'
_ItuSatGeneratorProvisionedDestination_Type.__name__=_AL
_ItuSatGeneratorProvisionedDestination_Object=MibTableColumn
ituSatGeneratorProvisionedDestination=_ItuSatGeneratorProvisionedDestination_Object((1,3,6,1,4,1,164,6,1,15,2,2,1,28),_ItuSatGeneratorProvisionedDestination_Type())
ituSatGeneratorProvisionedDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorProvisionedDestination.setStatus(_A)
_ItuSatGeneratorFlowTable_Object=MibTable
ituSatGeneratorFlowTable=_ItuSatGeneratorFlowTable_Object((1,3,6,1,4,1,164,6,1,15,2,3))
if mibBuilder.loadTexts:ituSatGeneratorFlowTable.setStatus(_A)
_ItuSatGeneratorFlowEntry_Object=MibTableRow
ituSatGeneratorFlowEntry=_ItuSatGeneratorFlowEntry_Object((1,3,6,1,4,1,164,6,1,15,2,3,1))
ituSatGeneratorFlowEntry.setIndexNames((0,_E,_c),(0,_E,_Ac))
if mibBuilder.loadTexts:ituSatGeneratorFlowEntry.setStatus(_A)
_ItuSatGeneratorFlowPbitIndex_Type=RadTestPbitIndex
_ItuSatGeneratorFlowPbitIndex_Object=MibTableColumn
ituSatGeneratorFlowPbitIndex=_ItuSatGeneratorFlowPbitIndex_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,1),_ItuSatGeneratorFlowPbitIndex_Type())
ituSatGeneratorFlowPbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatGeneratorFlowPbitIndex.setStatus(_A)
_ItuSatGeneratorFlowNameTx_Type=SnmpAdminString
_ItuSatGeneratorFlowNameTx_Object=MibTableColumn
ituSatGeneratorFlowNameTx=_ItuSatGeneratorFlowNameTx_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,2),_ItuSatGeneratorFlowNameTx_Type())
ituSatGeneratorFlowNameTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowNameTx.setStatus(_A)
_ItuSatGeneratorFlowNameRx_Type=SnmpAdminString
_ItuSatGeneratorFlowNameRx_Object=MibTableColumn
ituSatGeneratorFlowNameRx=_ItuSatGeneratorFlowNameRx_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,3),_ItuSatGeneratorFlowNameRx_Type())
ituSatGeneratorFlowNameRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowNameRx.setStatus(_A)
_ItuSatGeneratorFlowCir_Type=Unsigned32
_ItuSatGeneratorFlowCir_Object=MibTableColumn
ituSatGeneratorFlowCir=_ItuSatGeneratorFlowCir_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,4),_ItuSatGeneratorFlowCir_Type())
ituSatGeneratorFlowCir.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowCir.setStatus(_A)
_ItuSatGeneratorFlowEir_Type=Unsigned32
_ItuSatGeneratorFlowEir_Object=MibTableColumn
ituSatGeneratorFlowEir=_ItuSatGeneratorFlowEir_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,5),_ItuSatGeneratorFlowEir_Type())
ituSatGeneratorFlowEir.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowEir.setStatus(_A)
class _ItuSatGeneratorFlowAssociatedMEP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_ItuSatGeneratorFlowAssociatedMEP_Type.__name__=_H
_ItuSatGeneratorFlowAssociatedMEP_Object=MibTableColumn
ituSatGeneratorFlowAssociatedMEP=_ItuSatGeneratorFlowAssociatedMEP_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,6),_ItuSatGeneratorFlowAssociatedMEP_Type())
ituSatGeneratorFlowAssociatedMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowAssociatedMEP.setStatus(_A)
class _ItuSatGeneratorFlowAssociatedService_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ItuSatGeneratorFlowAssociatedService_Type.__name__=_H
_ItuSatGeneratorFlowAssociatedService_Object=MibTableColumn
ituSatGeneratorFlowAssociatedService=_ItuSatGeneratorFlowAssociatedService_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,7),_ItuSatGeneratorFlowAssociatedService_Type())
ituSatGeneratorFlowAssociatedService.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowAssociatedService.setStatus(_A)
class _ItuSatGeneratorFlowBwpInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flow',1),('test',2)))
_ItuSatGeneratorFlowBwpInUse_Type.__name__=_G
_ItuSatGeneratorFlowBwpInUse_Object=MibTableColumn
ituSatGeneratorFlowBwpInUse=_ItuSatGeneratorFlowBwpInUse_Object((1,3,6,1,4,1,164,6,1,15,2,3,1,8),_ItuSatGeneratorFlowBwpInUse_Type())
ituSatGeneratorFlowBwpInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatGeneratorFlowBwpInUse.setStatus(_A)
_ItuSatResponderTable_Object=MibTable
ituSatResponderTable=_ItuSatResponderTable_Object((1,3,6,1,4,1,164,6,1,15,2,4))
if mibBuilder.loadTexts:ituSatResponderTable.setStatus(_A)
_ItuSatResponderEntry_Object=MibTableRow
ituSatResponderEntry=_ItuSatResponderEntry_Object((1,3,6,1,4,1,164,6,1,15,2,4,1))
ituSatResponderEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:ituSatResponderEntry.setStatus(_A)
_ItuSatResponderIndex_Type=Unsigned32
_ItuSatResponderIndex_Object=MibTableColumn
ituSatResponderIndex=_ItuSatResponderIndex_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,1),_ItuSatResponderIndex_Type())
ituSatResponderIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatResponderIndex.setStatus(_A)
class _ItuSatResponderName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ItuSatResponderName_Type.__name__=_R
_ItuSatResponderName_Object=MibTableColumn
ituSatResponderName=_ItuSatResponderName_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,2),_ItuSatResponderName_Type())
ituSatResponderName.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderName.setStatus(_A)
_ItuSatResponderRowStatus_Type=RowStatus
_ItuSatResponderRowStatus_Object=MibTableColumn
ituSatResponderRowStatus=_ItuSatResponderRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,3),_ItuSatResponderRowStatus_Type())
ituSatResponderRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderRowStatus.setStatus(_A)
_ItuSatResponderServicePointer_Type=RowPointer
_ItuSatResponderServicePointer_Object=MibTableColumn
ituSatResponderServicePointer=_ItuSatResponderServicePointer_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,4),_ItuSatResponderServicePointer_Type())
ituSatResponderServicePointer.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderServicePointer.setStatus(_A)
class _ItuSatResponderProfile_Type(Unsigned32):defaultValue=0
_ItuSatResponderProfile_Type.__name__=_H
_ItuSatResponderProfile_Object=MibTableColumn
ituSatResponderProfile=_ItuSatResponderProfile_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,5),_ItuSatResponderProfile_Type())
ituSatResponderProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderProfile.setStatus(_A)
class _ItuSatResponderCmd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_ItuSatResponderCmd_Type.__name__=_G
_ItuSatResponderCmd_Object=MibTableColumn
ituSatResponderCmd=_ItuSatResponderCmd_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,6),_ItuSatResponderCmd_Type())
ituSatResponderCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderCmd.setStatus(_A)
class _ItuSatResponderStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_i,2),(_b,3)))
_ItuSatResponderStatus_Type.__name__=_G
_ItuSatResponderStatus_Object=MibTableColumn
ituSatResponderStatus=_ItuSatResponderStatus_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,7),_ItuSatResponderStatus_Type())
ituSatResponderStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatResponderStatus.setStatus(_A)
class _ItuSatResponderServiceBinding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ma',1),(_AZ,2),(_Aa,3),(_Ab,4)))
_ItuSatResponderServiceBinding_Type.__name__=_G
_ItuSatResponderServiceBinding_Object=MibTableColumn
ituSatResponderServiceBinding=_ItuSatResponderServiceBinding_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,8),_ItuSatResponderServiceBinding_Type())
ituSatResponderServiceBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderServiceBinding.setStatus(_A)
class _ItuSatResponderServiceName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ItuSatResponderServiceName_Type.__name__=_R
_ItuSatResponderServiceName_Object=MibTableColumn
ituSatResponderServiceName=_ItuSatResponderServiceName_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,9),_ItuSatResponderServiceName_Type())
ituSatResponderServiceName.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderServiceName.setStatus(_A)
class _ItuSatResponderEgressPort_Type(InterfaceIndexOrZero):defaultValue=0
_ItuSatResponderEgressPort_Type.__name__=_y
_ItuSatResponderEgressPort_Object=MibTableColumn
ituSatResponderEgressPort=_ItuSatResponderEgressPort_Object((1,3,6,1,4,1,164,6,1,15,2,4,1,10),_ItuSatResponderEgressPort_Type())
ituSatResponderEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatResponderEgressPort.setStatus(_A)
_ItuSatGeneratorPolicerTable_Object=MibTable
ituSatGeneratorPolicerTable=_ItuSatGeneratorPolicerTable_Object((1,3,6,1,4,1,164,6,1,15,2,5))
if mibBuilder.loadTexts:ituSatGeneratorPolicerTable.setStatus(_A)
_ItuSatGeneratorPolicerEntry_Object=MibTableRow
ituSatGeneratorPolicerEntry=_ItuSatGeneratorPolicerEntry_Object((1,3,6,1,4,1,164,6,1,15,2,5,1))
ituSatGeneratorPolicerEntry.setIndexNames((0,_E,_c),(0,_E,_Ad))
if mibBuilder.loadTexts:ituSatGeneratorPolicerEntry.setStatus(_A)
_ItuSatGeneratorPolicerPbitIndex_Type=RadTestPbitIndex
_ItuSatGeneratorPolicerPbitIndex_Object=MibTableColumn
ituSatGeneratorPolicerPbitIndex=_ItuSatGeneratorPolicerPbitIndex_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,1),_ItuSatGeneratorPolicerPbitIndex_Type())
ituSatGeneratorPolicerPbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatGeneratorPolicerPbitIndex.setStatus(_A)
_ItuSatGeneratorPolicerRowStatus_Type=RowStatus
_ItuSatGeneratorPolicerRowStatus_Object=MibTableColumn
ituSatGeneratorPolicerRowStatus=_ItuSatGeneratorPolicerRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,2),_ItuSatGeneratorPolicerRowStatus_Type())
ituSatGeneratorPolicerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerRowStatus.setStatus(_A)
class _ItuSatGeneratorPolicerCir_Type(Gauge32):defaultValue=0
_ItuSatGeneratorPolicerCir_Type.__name__=_f
_ItuSatGeneratorPolicerCir_Object=MibTableColumn
ituSatGeneratorPolicerCir=_ItuSatGeneratorPolicerCir_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,3),_ItuSatGeneratorPolicerCir_Type())
ituSatGeneratorPolicerCir.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerCir.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorPolicerCir.setUnits(_o)
class _ItuSatGeneratorPolicerCbs_Type(Gauge32):defaultValue=0
_ItuSatGeneratorPolicerCbs_Type.__name__=_f
_ItuSatGeneratorPolicerCbs_Object=MibTableColumn
ituSatGeneratorPolicerCbs=_ItuSatGeneratorPolicerCbs_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,4),_ItuSatGeneratorPolicerCbs_Type())
ituSatGeneratorPolicerCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerCbs.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorPolicerCbs.setUnits(_g)
class _ItuSatGeneratorPolicerEir_Type(Gauge32):defaultValue=0
_ItuSatGeneratorPolicerEir_Type.__name__=_f
_ItuSatGeneratorPolicerEir_Object=MibTableColumn
ituSatGeneratorPolicerEir=_ItuSatGeneratorPolicerEir_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,5),_ItuSatGeneratorPolicerEir_Type())
ituSatGeneratorPolicerEir.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerEir.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorPolicerEir.setUnits(_o)
class _ItuSatGeneratorPolicerEbs_Type(Gauge32):defaultValue=0
_ItuSatGeneratorPolicerEbs_Type.__name__=_f
_ItuSatGeneratorPolicerEbs_Object=MibTableColumn
ituSatGeneratorPolicerEbs=_ItuSatGeneratorPolicerEbs_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,6),_ItuSatGeneratorPolicerEbs_Type())
ituSatGeneratorPolicerEbs.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerEbs.setStatus(_A)
if mibBuilder.loadTexts:ituSatGeneratorPolicerEbs.setUnits(_g)
class _ItuSatGeneratorPolicerProfile_Type(Unsigned32):defaultValue=0
_ItuSatGeneratorPolicerProfile_Type.__name__=_H
_ItuSatGeneratorPolicerProfile_Object=MibTableColumn
ituSatGeneratorPolicerProfile=_ItuSatGeneratorPolicerProfile_Object((1,3,6,1,4,1,164,6,1,15,2,5,1,7),_ItuSatGeneratorPolicerProfile_Type())
ituSatGeneratorPolicerProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatGeneratorPolicerProfile.setStatus(_A)
_TwampControllerTable_Object=MibTable
twampControllerTable=_TwampControllerTable_Object((1,3,6,1,4,1,164,6,1,15,2,6))
if mibBuilder.loadTexts:twampControllerTable.setStatus(_A)
_TwampControllerEntry_Object=MibTableRow
twampControllerEntry=_TwampControllerEntry_Object((1,3,6,1,4,1,164,6,1,15,2,6,1))
twampControllerEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:twampControllerEntry.setStatus(_A)
_TwampControllerId_Type=Unsigned32
_TwampControllerId_Object=MibTableColumn
twampControllerId=_TwampControllerId_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,1),_TwampControllerId_Type())
twampControllerId.setMaxAccess(_I)
if mibBuilder.loadTexts:twampControllerId.setStatus(_A)
_TwampControllerRowStatus_Type=RowStatus
_TwampControllerRowStatus_Object=MibTableColumn
twampControllerRowStatus=_TwampControllerRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,2),_TwampControllerRowStatus_Type())
twampControllerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerRowStatus.setStatus(_A)
class _TwampControllerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TwampControllerName_Type.__name__=_R
_TwampControllerName_Object=MibTableColumn
twampControllerName=_TwampControllerName_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,3),_TwampControllerName_Type())
twampControllerName.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerName.setStatus(_A)
class _TwampControllerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A5,1),(_Z,2),(_i,3),(_b,4)))
_TwampControllerStatus_Type.__name__=_G
_TwampControllerStatus_Object=MibTableColumn
twampControllerStatus=_TwampControllerStatus_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,4),_TwampControllerStatus_Type())
twampControllerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:twampControllerStatus.setStatus(_A)
class _TwampControllerType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('twamp',2),(_Ae,3)))
_TwampControllerType_Type.__name__=_G
_TwampControllerType_Object=MibTableColumn
twampControllerType=_TwampControllerType_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,5),_TwampControllerType_Type())
twampControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerType.setStatus(_A)
class _TwampControllerL2Probe_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampControllerL2Probe_Type.__name__=_G
_TwampControllerL2Probe_Object=MibTableColumn
twampControllerL2Probe=_TwampControllerL2Probe_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,6),_TwampControllerL2Probe_Type())
twampControllerL2Probe.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerL2Probe.setStatus(_A)
_TwampControllerIngressEgressPort_Type=InterfaceIndexOrZero
_TwampControllerIngressEgressPort_Object=MibTableColumn
twampControllerIngressEgressPort=_TwampControllerIngressEgressPort_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,7),_TwampControllerIngressEgressPort_Type())
twampControllerIngressEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerIngressEgressPort.setStatus(_A)
class _TwampControllerOuterVlan_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(4294967295,4294967295))
_TwampControllerOuterVlan_Type.__name__=_H
_TwampControllerOuterVlan_Object=MibTableColumn
twampControllerOuterVlan=_TwampControllerOuterVlan_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,8),_TwampControllerOuterVlan_Type())
twampControllerOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerOuterVlan.setStatus(_A)
class _TwampControllerInnerVlan_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(4294967295,4294967295))
_TwampControllerInnerVlan_Type.__name__=_H
_TwampControllerInnerVlan_Object=MibTableColumn
twampControllerInnerVlan=_TwampControllerInnerVlan_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,9),_TwampControllerInnerVlan_Type())
twampControllerInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerInnerVlan.setStatus(_A)
class _TwampControllerOuterPbit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TwampControllerOuterPbit_Type.__name__=_H
_TwampControllerOuterPbit_Object=MibTableColumn
twampControllerOuterPbit=_TwampControllerOuterPbit_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,10),_TwampControllerOuterPbit_Type())
twampControllerOuterPbit.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerOuterPbit.setStatus(_A)
class _TwampControllerInnerPbit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TwampControllerInnerPbit_Type.__name__=_H
_TwampControllerInnerPbit_Object=MibTableColumn
twampControllerInnerPbit=_TwampControllerInnerPbit_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,11),_TwampControllerInnerPbit_Type())
twampControllerInnerPbit.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerInnerPbit.setStatus(_A)
_TwampControllerRouterEntity_Type=Unsigned32
_TwampControllerRouterEntity_Object=MibTableColumn
twampControllerRouterEntity=_TwampControllerRouterEntity_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,12),_TwampControllerRouterEntity_Type())
twampControllerRouterEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerRouterEntity.setStatus(_A)
_TwampControllerLocalAddrType_Type=InetAddressType
_TwampControllerLocalAddrType_Object=MibTableColumn
twampControllerLocalAddrType=_TwampControllerLocalAddrType_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,13),_TwampControllerLocalAddrType_Type())
twampControllerLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerLocalAddrType.setStatus(_A)
_TwampControllerLocalAddr_Type=InetAddress
_TwampControllerLocalAddr_Object=MibTableColumn
twampControllerLocalAddr=_TwampControllerLocalAddr_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,14),_TwampControllerLocalAddr_Type())
twampControllerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:twampControllerLocalAddr.setStatus(_A)
_TwampControllerAssociatedRI_Type=InterfaceIndexOrZero
_TwampControllerAssociatedRI_Object=MibTableColumn
twampControllerAssociatedRI=_TwampControllerAssociatedRI_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,15),_TwampControllerAssociatedRI_Type())
twampControllerAssociatedRI.setMaxAccess(_B)
if mibBuilder.loadTexts:twampControllerAssociatedRI.setStatus(_A)
class _TwampControllerTodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),(_Af,2),('sync',3),(_a,4)))
_TwampControllerTodStatus_Type.__name__=_G
_TwampControllerTodStatus_Object=MibTableColumn
twampControllerTodStatus=_TwampControllerTodStatus_Object((1,3,6,1,4,1,164,6,1,15,2,6,1,16),_TwampControllerTodStatus_Type())
twampControllerTodStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:twampControllerTodStatus.setStatus(_A)
_TwampPeerTable_Object=MibTable
twampPeerTable=_TwampPeerTable_Object((1,3,6,1,4,1,164,6,1,15,2,7))
if mibBuilder.loadTexts:twampPeerTable.setStatus(_A)
_TwampPeerEntry_Object=MibTableRow
twampPeerEntry=_TwampPeerEntry_Object((1,3,6,1,4,1,164,6,1,15,2,7,1))
twampPeerEntry.setIndexNames((0,_E,_d),(0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:twampPeerEntry.setStatus(_A)
_TwampPeerAddrType_Type=InetAddressType
_TwampPeerAddrType_Object=MibTableColumn
twampPeerAddrType=_TwampPeerAddrType_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,1),_TwampPeerAddrType_Type())
twampPeerAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:twampPeerAddrType.setStatus(_A)
_TwampPeerAddr_Type=InetAddress
_TwampPeerAddr_Object=MibTableColumn
twampPeerAddr=_TwampPeerAddr_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,2),_TwampPeerAddr_Type())
twampPeerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:twampPeerAddr.setStatus(_A)
_TwampPeerRowStatus_Type=RowStatus
_TwampPeerRowStatus_Object=MibTableColumn
twampPeerRowStatus=_TwampPeerRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,3),_TwampPeerRowStatus_Type())
twampPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerRowStatus.setStatus(_A)
class _TwampPeerActivateCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),(_X,3)))
_TwampPeerActivateCmd_Type.__name__=_G
_TwampPeerActivateCmd_Object=MibTableColumn
twampPeerActivateCmd=_TwampPeerActivateCmd_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,4),_TwampPeerActivateCmd_Type())
twampPeerActivateCmd.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerActivateCmd.setStatus(_A)
_TwampPeerActivateDuration_Type=Unsigned32
_TwampPeerActivateDuration_Object=MibTableColumn
twampPeerActivateDuration=_TwampPeerActivateDuration_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,5),_TwampPeerActivateDuration_Type())
twampPeerActivateDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerActivateDuration.setStatus(_A)
if mibBuilder.loadTexts:twampPeerActivateDuration.setUnits(_A1)
_TwampPeerStartDateAndTime_Type=DateAndTime
_TwampPeerStartDateAndTime_Object=MibTableColumn
twampPeerStartDateAndTime=_TwampPeerStartDateAndTime_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,6),_TwampPeerStartDateAndTime_Type())
twampPeerStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampPeerStartDateAndTime.setStatus(_A)
class _TwampPeerCalcMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),('oneWay',2),(_Ag,3)))
_TwampPeerCalcMode_Type.__name__=_G
_TwampPeerCalcMode_Object=MibTableColumn
twampPeerCalcMode=_TwampPeerCalcMode_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,7),_TwampPeerCalcMode_Type())
twampPeerCalcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerCalcMode.setStatus(_A)
class _TwampPeerResponderSeqNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampPeerResponderSeqNum_Type.__name__=_G
_TwampPeerResponderSeqNum_Object=MibTableColumn
twampPeerResponderSeqNum=_TwampPeerResponderSeqNum_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,8),_TwampPeerResponderSeqNum_Type())
twampPeerResponderSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerResponderSeqNum.setStatus(_A)
class _TwampPeerResponderTodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_Af,2),('sync',3)))
_TwampPeerResponderTodStatus_Type.__name__=_G
_TwampPeerResponderTodStatus_Object=MibTableColumn
twampPeerResponderTodStatus=_TwampPeerResponderTodStatus_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,9),_TwampPeerResponderTodStatus_Type())
twampPeerResponderTodStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:twampPeerResponderTodStatus.setStatus(_A)
_TwampPeerElapsedTime_Type=Unsigned32
_TwampPeerElapsedTime_Object=MibTableColumn
twampPeerElapsedTime=_TwampPeerElapsedTime_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,10),_TwampPeerElapsedTime_Type())
twampPeerElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampPeerElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:twampPeerElapsedTime.setUnits(_P)
class _TwampPeerDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_TwampPeerDescr_Type.__name__=_R
_TwampPeerDescr_Object=MibTableColumn
twampPeerDescr=_TwampPeerDescr_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,11),_TwampPeerDescr_Type())
twampPeerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:twampPeerDescr.setStatus(_A)
class _TwampPeerLastCalcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_p,1),('oneWay',2),(_Ag,3)))
_TwampPeerLastCalcMode_Type.__name__=_G
_TwampPeerLastCalcMode_Object=MibTableColumn
twampPeerLastCalcMode=_TwampPeerLastCalcMode_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,12),_TwampPeerLastCalcMode_Type())
twampPeerLastCalcMode.setMaxAccess(_B)
if mibBuilder.loadTexts:twampPeerLastCalcMode.setStatus(_A)
class _TwampPeerLastResponderSeqNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampPeerLastResponderSeqNum_Type.__name__=_G
_TwampPeerLastResponderSeqNum_Object=MibTableColumn
twampPeerLastResponderSeqNum=_TwampPeerLastResponderSeqNum_Object((1,3,6,1,4,1,164,6,1,15,2,7,1,13),_TwampPeerLastResponderSeqNum_Type())
twampPeerLastResponderSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampPeerLastResponderSeqNum.setStatus(_A)
_TwampContSessionTable_Object=MibTable
twampContSessionTable=_TwampContSessionTable_Object((1,3,6,1,4,1,164,6,1,15,2,8))
if mibBuilder.loadTexts:twampContSessionTable.setStatus(_A)
_TwampContSessionEntry_Object=MibTableRow
twampContSessionEntry=_TwampContSessionEntry_Object((1,3,6,1,4,1,164,6,1,15,2,8,1))
twampContSessionEntry.setIndexNames((0,_E,_d),(0,_E,_j),(0,_E,_k),(0,_E,_q))
if mibBuilder.loadTexts:twampContSessionEntry.setStatus(_A)
_TwampContSessionId_Type=Unsigned32
_TwampContSessionId_Object=MibTableColumn
twampContSessionId=_TwampContSessionId_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,1),_TwampContSessionId_Type())
twampContSessionId.setMaxAccess(_I)
if mibBuilder.loadTexts:twampContSessionId.setStatus(_A)
_TwampContSessionRowStatus_Type=RowStatus
_TwampContSessionRowStatus_Object=MibTableColumn
twampContSessionRowStatus=_TwampContSessionRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,2),_TwampContSessionRowStatus_Type())
twampContSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampContSessionRowStatus.setStatus(_A)
class _TwampContSessionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TwampContSessionName_Type.__name__=_R
_TwampContSessionName_Object=MibTableColumn
twampContSessionName=_TwampContSessionName_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,3),_TwampContSessionName_Type())
twampContSessionName.setMaxAccess(_C)
if mibBuilder.loadTexts:twampContSessionName.setStatus(_A)
_TwampContSessionStartDateAndTime_Type=DateAndTime
_TwampContSessionStartDateAndTime_Object=MibTableColumn
twampContSessionStartDateAndTime=_TwampContSessionStartDateAndTime_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,4),_TwampContSessionStartDateAndTime_Type())
twampContSessionStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionStartDateAndTime.setStatus(_A)
class _TwampContSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_Z,2),(_i,3),(_b,4),(_AW,5),(_AX,6),(_AY,7)))
_TwampContSessionStatus_Type.__name__=_G
_TwampContSessionStatus_Object=MibTableColumn
twampContSessionStatus=_TwampContSessionStatus_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,5),_TwampContSessionStatus_Type())
twampContSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionStatus.setStatus(_A)
_TwampContSessionLocalL4PortNumber_Type=InetPortNumber
_TwampContSessionLocalL4PortNumber_Object=MibTableColumn
twampContSessionLocalL4PortNumber=_TwampContSessionLocalL4PortNumber_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,6),_TwampContSessionLocalL4PortNumber_Type())
twampContSessionLocalL4PortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionLocalL4PortNumber.setStatus(_A)
_TwampContSessionPeerL4PortNumber_Type=InetPortNumber
_TwampContSessionPeerL4PortNumber_Object=MibTableColumn
twampContSessionPeerL4PortNumber=_TwampContSessionPeerL4PortNumber_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,7),_TwampContSessionPeerL4PortNumber_Type())
twampContSessionPeerL4PortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:twampContSessionPeerL4PortNumber.setStatus(_A)
class _TwampContSessionPeerDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_TwampContSessionPeerDscp_Type.__name__=_H
_TwampContSessionPeerDscp_Object=MibTableColumn
twampContSessionPeerDscp=_TwampContSessionPeerDscp_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,8),_TwampContSessionPeerDscp_Type())
twampContSessionPeerDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:twampContSessionPeerDscp.setStatus(_A)
_TwampContSessionTestProfileId_Type=Unsigned32
_TwampContSessionTestProfileId_Object=MibTableColumn
twampContSessionTestProfileId=_TwampContSessionTestProfileId_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,9),_TwampContSessionTestProfileId_Type())
twampContSessionTestProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:twampContSessionTestProfileId.setStatus(_A)
_TwampContSessionTxPackets_Type=Counter64
_TwampContSessionTxPackets_Object=MibTableColumn
twampContSessionTxPackets=_TwampContSessionTxPackets_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,10),_TwampContSessionTxPackets_Type())
twampContSessionTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionTxPackets.setStatus(_A)
_TwampContSessionRxPackets_Type=Counter64
_TwampContSessionRxPackets_Object=MibTableColumn
twampContSessionRxPackets=_TwampContSessionRxPackets_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,11),_TwampContSessionRxPackets_Type())
twampContSessionRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionRxPackets.setStatus(_A)
class _TwampContSessionResult_Type(Bits):namedValues=NamedValues(*((_A8,0),(_A9,1),(_AA,2)))
_TwampContSessionResult_Type.__name__=_Y
_TwampContSessionResult_Object=MibTableColumn
twampContSessionResult=_TwampContSessionResult_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,12),_TwampContSessionResult_Type())
twampContSessionResult.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionResult.setStatus(_A)
_TwampContSessionConfChanged_Type=TruthValue
_TwampContSessionConfChanged_Object=MibTableColumn
twampContSessionConfChanged=_TwampContSessionConfChanged_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,13),_TwampContSessionConfChanged_Type())
twampContSessionConfChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionConfChanged.setStatus(_A)
_TwampContSessionConvertedIndex_Type=Unsigned32
_TwampContSessionConvertedIndex_Object=MibTableColumn
twampContSessionConvertedIndex=_TwampContSessionConvertedIndex_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,14),_TwampContSessionConvertedIndex_Type())
twampContSessionConvertedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionConvertedIndex.setStatus(_A)
class _TwampContSessionResultFwd_Type(Bits):namedValues=NamedValues(*((_A8,0),(_A9,1),(_AA,2)))
_TwampContSessionResultFwd_Type.__name__=_Y
_TwampContSessionResultFwd_Object=MibTableColumn
twampContSessionResultFwd=_TwampContSessionResultFwd_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,15),_TwampContSessionResultFwd_Type())
twampContSessionResultFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionResultFwd.setStatus(_A)
class _TwampContSessionResultBck_Type(Bits):namedValues=NamedValues(*((_A8,0),(_A9,1),(_AA,2)))
_TwampContSessionResultBck_Type.__name__=_Y
_TwampContSessionResultBck_Object=MibTableColumn
twampContSessionResultBck=_TwampContSessionResultBck_Object((1,3,6,1,4,1,164,6,1,15,2,8,1,16),_TwampContSessionResultBck_Type())
twampContSessionResultBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampContSessionResultBck.setStatus(_A)
_TwampResponderTable_Object=MibTable
twampResponderTable=_TwampResponderTable_Object((1,3,6,1,4,1,164,6,1,15,2,9))
if mibBuilder.loadTexts:twampResponderTable.setStatus(_A)
_TwampResponderEntry_Object=MibTableRow
twampResponderEntry=_TwampResponderEntry_Object((1,3,6,1,4,1,164,6,1,15,2,9,1))
twampResponderEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:twampResponderEntry.setStatus(_A)
_TwampResponderId_Type=Unsigned32
_TwampResponderId_Object=MibTableColumn
twampResponderId=_TwampResponderId_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,1),_TwampResponderId_Type())
twampResponderId.setMaxAccess(_I)
if mibBuilder.loadTexts:twampResponderId.setStatus(_A)
_TwampResponderRowStatus_Type=RowStatus
_TwampResponderRowStatus_Object=MibTableColumn
twampResponderRowStatus=_TwampResponderRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,2),_TwampResponderRowStatus_Type())
twampResponderRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderRowStatus.setStatus(_A)
class _TwampResponderName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TwampResponderName_Type.__name__=_R
_TwampResponderName_Object=MibTableColumn
twampResponderName=_TwampResponderName_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,3),_TwampResponderName_Type())
twampResponderName.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderName.setStatus(_A)
class _TwampResponderStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A5,1),(_Z,2),(_i,3)))
_TwampResponderStatus_Type.__name__=_G
_TwampResponderStatus_Object=MibTableColumn
twampResponderStatus=_TwampResponderStatus_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,4),_TwampResponderStatus_Type())
twampResponderStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:twampResponderStatus.setStatus(_A)
class _TwampResponderType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('twamp',2),(_Ae,3),('udpEchoPlus',4)))
_TwampResponderType_Type.__name__=_G
_TwampResponderType_Object=MibTableColumn
twampResponderType=_TwampResponderType_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,5),_TwampResponderType_Type())
twampResponderType.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderType.setStatus(_A)
class _TwampResponderL2Probe_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampResponderL2Probe_Type.__name__=_G
_TwampResponderL2Probe_Object=MibTableColumn
twampResponderL2Probe=_TwampResponderL2Probe_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,6),_TwampResponderL2Probe_Type())
twampResponderL2Probe.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderL2Probe.setStatus(_A)
_TwampResponderIngressEgressPort_Type=InterfaceIndexOrZero
_TwampResponderIngressEgressPort_Object=MibTableColumn
twampResponderIngressEgressPort=_TwampResponderIngressEgressPort_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,7),_TwampResponderIngressEgressPort_Type())
twampResponderIngressEgressPort.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderIngressEgressPort.setStatus(_A)
class _TwampResponderOuterVlan_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(4294967295,4294967295))
_TwampResponderOuterVlan_Type.__name__=_H
_TwampResponderOuterVlan_Object=MibTableColumn
twampResponderOuterVlan=_TwampResponderOuterVlan_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,8),_TwampResponderOuterVlan_Type())
twampResponderOuterVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderOuterVlan.setStatus(_A)
class _TwampResponderInnerVlan_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095),ValueRangeConstraint(4294967295,4294967295))
_TwampResponderInnerVlan_Type.__name__=_H
_TwampResponderInnerVlan_Object=MibTableColumn
twampResponderInnerVlan=_TwampResponderInnerVlan_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,9),_TwampResponderInnerVlan_Type())
twampResponderInnerVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderInnerVlan.setStatus(_A)
class _TwampResponderOuterPbit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(254,254))
_TwampResponderOuterPbit_Type.__name__=_H
_TwampResponderOuterPbit_Object=MibTableColumn
twampResponderOuterPbit=_TwampResponderOuterPbit_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,10),_TwampResponderOuterPbit_Type())
twampResponderOuterPbit.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderOuterPbit.setStatus(_A)
class _TwampResponderInnerPbit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(254,254))
_TwampResponderInnerPbit_Type.__name__=_H
_TwampResponderInnerPbit_Object=MibTableColumn
twampResponderInnerPbit=_TwampResponderInnerPbit_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,11),_TwampResponderInnerPbit_Type())
twampResponderInnerPbit.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderInnerPbit.setStatus(_A)
_TwampResponderRouterEntity_Type=Unsigned32
_TwampResponderRouterEntity_Object=MibTableColumn
twampResponderRouterEntity=_TwampResponderRouterEntity_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,12),_TwampResponderRouterEntity_Type())
twampResponderRouterEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderRouterEntity.setStatus(_A)
_TwampResponderLocalAddrType_Type=InetAddressType
_TwampResponderLocalAddrType_Object=MibTableColumn
twampResponderLocalAddrType=_TwampResponderLocalAddrType_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,13),_TwampResponderLocalAddrType_Type())
twampResponderLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderLocalAddrType.setStatus(_A)
_TwampResponderLocalAddr_Type=InetAddress
_TwampResponderLocalAddr_Object=MibTableColumn
twampResponderLocalAddr=_TwampResponderLocalAddr_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,14),_TwampResponderLocalAddr_Type())
twampResponderLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderLocalAddr.setStatus(_A)
_TwampResponderAssociatedRI_Type=InterfaceIndexOrZero
_TwampResponderAssociatedRI_Object=MibTableColumn
twampResponderAssociatedRI=_TwampResponderAssociatedRI_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,15),_TwampResponderAssociatedRI_Type())
twampResponderAssociatedRI.setMaxAccess(_B)
if mibBuilder.loadTexts:twampResponderAssociatedRI.setStatus(_A)
class _TwampResponderTxSeqNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampResponderTxSeqNum_Type.__name__=_G
_TwampResponderTxSeqNum_Object=MibTableColumn
twampResponderTxSeqNum=_TwampResponderTxSeqNum_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,16),_TwampResponderTxSeqNum_Type())
twampResponderTxSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderTxSeqNum.setStatus(_A)
class _TwampResponderTxExtendedInfo_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_X,2)))
_TwampResponderTxExtendedInfo_Type.__name__=_G
_TwampResponderTxExtendedInfo_Object=MibTableColumn
twampResponderTxExtendedInfo=_TwampResponderTxExtendedInfo_Object((1,3,6,1,4,1,164,6,1,15,2,9,1,17),_TwampResponderTxExtendedInfo_Type())
twampResponderTxExtendedInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResponderTxExtendedInfo.setStatus(_A)
_TwampResSessionTable_Object=MibTable
twampResSessionTable=_TwampResSessionTable_Object((1,3,6,1,4,1,164,6,1,15,2,10))
if mibBuilder.loadTexts:twampResSessionTable.setStatus(_A)
_TwampResSessionEntry_Object=MibTableRow
twampResSessionEntry=_TwampResSessionEntry_Object((1,3,6,1,4,1,164,6,1,15,2,10,1))
twampResSessionEntry.setIndexNames((0,_E,_AB),(0,_E,_Ah))
if mibBuilder.loadTexts:twampResSessionEntry.setStatus(_A)
_TwampResSessionId_Type=Unsigned32
_TwampResSessionId_Object=MibTableColumn
twampResSessionId=_TwampResSessionId_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,1),_TwampResSessionId_Type())
twampResSessionId.setMaxAccess(_I)
if mibBuilder.loadTexts:twampResSessionId.setStatus(_A)
_TwampResSessionRowStatus_Type=RowStatus
_TwampResSessionRowStatus_Object=MibTableColumn
twampResSessionRowStatus=_TwampResSessionRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,2),_TwampResSessionRowStatus_Type())
twampResSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResSessionRowStatus.setStatus(_A)
class _TwampResSessionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TwampResSessionName_Type.__name__=_R
_TwampResSessionName_Object=MibTableColumn
twampResSessionName=_TwampResSessionName_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,3),_TwampResSessionName_Type())
twampResSessionName.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResSessionName.setStatus(_A)
_TwampResSessionLocalL4PortNumber_Type=InetPortNumber
_TwampResSessionLocalL4PortNumber_Object=MibTableColumn
twampResSessionLocalL4PortNumber=_TwampResSessionLocalL4PortNumber_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,4),_TwampResSessionLocalL4PortNumber_Type())
twampResSessionLocalL4PortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:twampResSessionLocalL4PortNumber.setStatus(_A)
_TwampResSessionTxPackets_Type=Counter64
_TwampResSessionTxPackets_Object=MibTableColumn
twampResSessionTxPackets=_TwampResSessionTxPackets_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,5),_TwampResSessionTxPackets_Type())
twampResSessionTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampResSessionTxPackets.setStatus(_A)
_TwampResSessionRxPackets_Type=Counter64
_TwampResSessionRxPackets_Object=MibTableColumn
twampResSessionRxPackets=_TwampResSessionRxPackets_Object((1,3,6,1,4,1,164,6,1,15,2,10,1,6),_TwampResSessionRxPackets_Type())
twampResSessionRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampResSessionRxPackets.setStatus(_A)
_ItuSatSingleCosFlowTable_Object=MibTable
ituSatSingleCosFlowTable=_ItuSatSingleCosFlowTable_Object((1,3,6,1,4,1,164,6,1,15,2,15))
if mibBuilder.loadTexts:ituSatSingleCosFlowTable.setStatus(_A)
_ItuSatSingleCosFlowEntry_Object=MibTableRow
ituSatSingleCosFlowEntry=_ItuSatSingleCosFlowEntry_Object((1,3,6,1,4,1,164,6,1,15,2,15,1))
ituSatSingleCosFlowEntry.setIndexNames((0,_E,_Ai),(0,_E,_Aj),(0,_E,_Ak),(0,_E,_Al))
if mibBuilder.loadTexts:ituSatSingleCosFlowEntry.setStatus(_A)
class _ItuSatSingleCosFlowFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('generator',1),('responder',2)))
_ItuSatSingleCosFlowFunction_Type.__name__=_G
_ItuSatSingleCosFlowFunction_Object=MibTableColumn
ituSatSingleCosFlowFunction=_ItuSatSingleCosFlowFunction_Object((1,3,6,1,4,1,164,6,1,15,2,15,1,1),_ItuSatSingleCosFlowFunction_Type())
ituSatSingleCosFlowFunction.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatSingleCosFlowFunction.setStatus(_A)
_ItuSatSingleCosFlowFunctionIndex_Type=Unsigned32
_ItuSatSingleCosFlowFunctionIndex_Object=MibTableColumn
ituSatSingleCosFlowFunctionIndex=_ItuSatSingleCosFlowFunctionIndex_Object((1,3,6,1,4,1,164,6,1,15,2,15,1,2),_ItuSatSingleCosFlowFunctionIndex_Type())
ituSatSingleCosFlowFunctionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatSingleCosFlowFunctionIndex.setStatus(_A)
_ItuSatSingleCosFlowIdx1_Type=Unsigned32
_ItuSatSingleCosFlowIdx1_Object=MibTableColumn
ituSatSingleCosFlowIdx1=_ItuSatSingleCosFlowIdx1_Object((1,3,6,1,4,1,164,6,1,15,2,15,1,3),_ItuSatSingleCosFlowIdx1_Type())
ituSatSingleCosFlowIdx1.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatSingleCosFlowIdx1.setStatus(_A)
_ItuSatSingleCosFlowIdx2_Type=Unsigned32
_ItuSatSingleCosFlowIdx2_Object=MibTableColumn
ituSatSingleCosFlowIdx2=_ItuSatSingleCosFlowIdx2_Object((1,3,6,1,4,1,164,6,1,15,2,15,1,4),_ItuSatSingleCosFlowIdx2_Type())
ituSatSingleCosFlowIdx2.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatSingleCosFlowIdx2.setStatus(_A)
_ItuSatSingleCosFlowRowStatus_Type=RowStatus
_ItuSatSingleCosFlowRowStatus_Object=MibTableColumn
ituSatSingleCosFlowRowStatus=_ItuSatSingleCosFlowRowStatus_Object((1,3,6,1,4,1,164,6,1,15,2,15,1,5),_ItuSatSingleCosFlowRowStatus_Type())
ituSatSingleCosFlowRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ituSatSingleCosFlowRowStatus.setStatus(_A)
_RadTestPerfRepResults_ObjectIdentity=ObjectIdentity
radTestPerfRepResults=_RadTestPerfRepResults_ObjectIdentity((1,3,6,1,4,1,164,6,1,15,3))
_TstNePerfRepGeneralResultsTable_Object=MibTable
tstNePerfRepGeneralResultsTable=_TstNePerfRepGeneralResultsTable_Object((1,3,6,1,4,1,164,6,1,15,3,1))
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsTable.setStatus(_A)
_TstNePerfRepGeneralResultsEntry_Object=MibTableRow
tstNePerfRepGeneralResultsEntry=_TstNePerfRepGeneralResultsEntry_Object((1,3,6,1,4,1,164,6,1,15,3,1,1))
tstNePerfRepGeneralResultsEntry.setIndexNames((0,_E,_W),(0,_E,_e),(0,_E,_Am),(0,_E,_An))
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsEntry.setStatus(_A)
class _TstNePerfRepGeneralResultsTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_A2,1),(_A3,2),(_A4,3)))
_TstNePerfRepGeneralResultsTestType_Type.__name__=_G
_TstNePerfRepGeneralResultsTestType_Object=MibTableColumn
tstNePerfRepGeneralResultsTestType=_TstNePerfRepGeneralResultsTestType_Object((1,3,6,1,4,1,164,6,1,15,3,1,1,1),_TstNePerfRepGeneralResultsTestType_Type())
tstNePerfRepGeneralResultsTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsTestType.setStatus(_A)
_TstNePerfRepGeneralResultsTrialNumber_Type=Unsigned32
_TstNePerfRepGeneralResultsTrialNumber_Object=MibTableColumn
tstNePerfRepGeneralResultsTrialNumber=_TstNePerfRepGeneralResultsTrialNumber_Object((1,3,6,1,4,1,164,6,1,15,3,1,1,2),_TstNePerfRepGeneralResultsTrialNumber_Type())
tstNePerfRepGeneralResultsTrialNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsTrialNumber.setStatus(_A)
class _TstNePerfRepGeneralResultsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*(('success',1),('fail',2),('linkDown',3),(_Ao,4),(_A6,5),(_a,255)))
_TstNePerfRepGeneralResultsStatus_Type.__name__=_G
_TstNePerfRepGeneralResultsStatus_Object=MibTableColumn
tstNePerfRepGeneralResultsStatus=_TstNePerfRepGeneralResultsStatus_Object((1,3,6,1,4,1,164,6,1,15,3,1,1,3),_TstNePerfRepGeneralResultsStatus_Type())
tstNePerfRepGeneralResultsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsStatus.setStatus(_A)
_TstNePerfRepGeneralResultsDuration_Type=TimeTicks
_TstNePerfRepGeneralResultsDuration_Object=MibTableColumn
tstNePerfRepGeneralResultsDuration=_TstNePerfRepGeneralResultsDuration_Object((1,3,6,1,4,1,164,6,1,15,3,1,1,4),_TstNePerfRepGeneralResultsDuration_Type())
tstNePerfRepGeneralResultsDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepGeneralResultsDuration.setStatus(_A)
_ThroughputReportTable_Object=MibTable
throughputReportTable=_ThroughputReportTable_Object((1,3,6,1,4,1,164,6,1,15,3,2))
if mibBuilder.loadTexts:throughputReportTable.setStatus(_A)
_ThroughputReportEntry_Object=MibTableRow
throughputReportEntry=_ThroughputReportEntry_Object((1,3,6,1,4,1,164,6,1,15,3,2,1))
throughputReportEntry.setIndexNames((0,_E,_W),(0,_E,_e),(0,_E,_AC),(0,_E,_AD))
if mibBuilder.loadTexts:throughputReportEntry.setStatus(_A)
_ThroughputReportTrialNumber_Type=Unsigned32
_ThroughputReportTrialNumber_Object=MibTableColumn
throughputReportTrialNumber=_ThroughputReportTrialNumber_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,1),_ThroughputReportTrialNumber_Type())
throughputReportTrialNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:throughputReportTrialNumber.setStatus(_A)
_ThroughputReportPacketSize_Type=RadTestPerfresultFrameSize
_ThroughputReportPacketSize_Object=MibTableColumn
throughputReportPacketSize=_ThroughputReportPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,2),_ThroughputReportPacketSize_Type())
throughputReportPacketSize.setMaxAccess(_I)
if mibBuilder.loadTexts:throughputReportPacketSize.setStatus(_A)
_ThroughputReportThroughputTheoretical_Type=Gauge32
_ThroughputReportThroughputTheoretical_Object=MibTableColumn
throughputReportThroughputTheoretical=_ThroughputReportThroughputTheoretical_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,3),_ThroughputReportThroughputTheoretical_Type())
throughputReportThroughputTheoretical.setMaxAccess(_B)
if mibBuilder.loadTexts:throughputReportThroughputTheoretical.setStatus(_A)
_ThroughputReportResults_Type=Gauge32
_ThroughputReportResults_Object=MibTableColumn
throughputReportResults=_ThroughputReportResults_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,4),_ThroughputReportResults_Type())
throughputReportResults.setMaxAccess(_B)
if mibBuilder.loadTexts:throughputReportResults.setStatus(_A)
class _ThroughputReportDataPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),('allOnes',2),(_AO,3),(_AP,4),(_AQ,5),(_AR,6),(_AS,7)))
_ThroughputReportDataPattern_Type.__name__=_G
_ThroughputReportDataPattern_Object=MibTableColumn
throughputReportDataPattern=_ThroughputReportDataPattern_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,5),_ThroughputReportDataPattern_Type())
throughputReportDataPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:throughputReportDataPattern.setStatus(_A)
_ThroughputReportResultsBps_Type=Gauge32
_ThroughputReportResultsBps_Object=MibTableColumn
throughputReportResultsBps=_ThroughputReportResultsBps_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,6),_ThroughputReportResultsBps_Type())
throughputReportResultsBps.setMaxAccess(_B)
if mibBuilder.loadTexts:throughputReportResultsBps.setStatus(_A)
_ThroughputReportCustomPacketSize_Type=Unsigned32
_ThroughputReportCustomPacketSize_Object=MibTableColumn
throughputReportCustomPacketSize=_ThroughputReportCustomPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,2,1,7),_ThroughputReportCustomPacketSize_Type())
throughputReportCustomPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:throughputReportCustomPacketSize.setStatus(_A)
_LatencyReportTable_Object=MibTable
latencyReportTable=_LatencyReportTable_Object((1,3,6,1,4,1,164,6,1,15,3,3))
if mibBuilder.loadTexts:latencyReportTable.setStatus(_A)
_LatencyReportEntry_Object=MibTableRow
latencyReportEntry=_LatencyReportEntry_Object((1,3,6,1,4,1,164,6,1,15,3,3,1))
latencyReportEntry.setIndexNames((0,_E,_W),(0,_E,_e),(0,_E,_Ap),(0,_E,_Aq))
if mibBuilder.loadTexts:latencyReportEntry.setStatus(_A)
_LatencyReportTrialNumber_Type=Unsigned32
_LatencyReportTrialNumber_Object=MibTableColumn
latencyReportTrialNumber=_LatencyReportTrialNumber_Object((1,3,6,1,4,1,164,6,1,15,3,3,1,1),_LatencyReportTrialNumber_Type())
latencyReportTrialNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:latencyReportTrialNumber.setStatus(_A)
_LatencyReportPacketSize_Type=RadTestPerfresultFrameSize
_LatencyReportPacketSize_Object=MibTableColumn
latencyReportPacketSize=_LatencyReportPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,3,1,2),_LatencyReportPacketSize_Type())
latencyReportPacketSize.setMaxAccess(_I)
if mibBuilder.loadTexts:latencyReportPacketSize.setStatus(_A)
class _LatencyReportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('storeAndForward',1),('bitForwarding',2)))
_LatencyReportType_Type.__name__=_G
_LatencyReportType_Object=MibTableColumn
latencyReportType=_LatencyReportType_Object((1,3,6,1,4,1,164,6,1,15,3,3,1,3),_LatencyReportType_Type())
latencyReportType.setMaxAccess(_B)
if mibBuilder.loadTexts:latencyReportType.setStatus(_A)
_LatencyReportResult_Type=Gauge32
_LatencyReportResult_Object=MibTableColumn
latencyReportResult=_LatencyReportResult_Object((1,3,6,1,4,1,164,6,1,15,3,3,1,4),_LatencyReportResult_Type())
latencyReportResult.setMaxAccess(_B)
if mibBuilder.loadTexts:latencyReportResult.setStatus(_A)
if mibBuilder.loadTexts:latencyReportResult.setUnits(_F)
_LatencyReportCustomPacketSize_Type=Unsigned32
_LatencyReportCustomPacketSize_Object=MibTableColumn
latencyReportCustomPacketSize=_LatencyReportCustomPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,3,1,5),_LatencyReportCustomPacketSize_Type())
latencyReportCustomPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:latencyReportCustomPacketSize.setStatus(_A)
_FramelossRateReportTable_Object=MibTable
framelossRateReportTable=_FramelossRateReportTable_Object((1,3,6,1,4,1,164,6,1,15,3,4))
if mibBuilder.loadTexts:framelossRateReportTable.setStatus(_A)
_FramelossRateReportEntry_Object=MibTableRow
framelossRateReportEntry=_FramelossRateReportEntry_Object((1,3,6,1,4,1,164,6,1,15,3,4,1))
framelossRateReportEntry.setIndexNames((0,_E,_W),(0,_E,_e),(0,_E,_Ar),(0,_E,_As),(0,_E,_At))
if mibBuilder.loadTexts:framelossRateReportEntry.setStatus(_A)
_FramelossRateReportTrialNumber_Type=Unsigned32
_FramelossRateReportTrialNumber_Object=MibTableColumn
framelossRateReportTrialNumber=_FramelossRateReportTrialNumber_Object((1,3,6,1,4,1,164,6,1,15,3,4,1,1),_FramelossRateReportTrialNumber_Type())
framelossRateReportTrialNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:framelossRateReportTrialNumber.setStatus(_A)
_FramelossRateReportPacketSize_Type=RadTestPerfresultFrameSize
_FramelossRateReportPacketSize_Object=MibTableColumn
framelossRateReportPacketSize=_FramelossRateReportPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,4,1,2),_FramelossRateReportPacketSize_Type())
framelossRateReportPacketSize.setMaxAccess(_I)
if mibBuilder.loadTexts:framelossRateReportPacketSize.setStatus(_A)
_FramelossRateReportInputRate_Type=Unsigned32
_FramelossRateReportInputRate_Object=MibTableColumn
framelossRateReportInputRate=_FramelossRateReportInputRate_Object((1,3,6,1,4,1,164,6,1,15,3,4,1,3),_FramelossRateReportInputRate_Type())
framelossRateReportInputRate.setMaxAccess(_I)
if mibBuilder.loadTexts:framelossRateReportInputRate.setStatus(_A)
_FramelossRateReportResults_Type=Gauge32
_FramelossRateReportResults_Object=MibTableColumn
framelossRateReportResults=_FramelossRateReportResults_Object((1,3,6,1,4,1,164,6,1,15,3,4,1,4),_FramelossRateReportResults_Type())
framelossRateReportResults.setMaxAccess(_B)
if mibBuilder.loadTexts:framelossRateReportResults.setStatus(_A)
_FramelossRateReportCustomPacketSize_Type=Unsigned32
_FramelossRateReportCustomPacketSize_Object=MibTableColumn
framelossRateReportCustomPacketSize=_FramelossRateReportCustomPacketSize_Object((1,3,6,1,4,1,164,6,1,15,3,4,1,5),_FramelossRateReportCustomPacketSize_Type())
framelossRateReportCustomPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:framelossRateReportCustomPacketSize.setStatus(_A)
_TstNePerfRepStatusTable_Object=MibTable
tstNePerfRepStatusTable=_TstNePerfRepStatusTable_Object((1,3,6,1,4,1,164,6,1,15,3,5))
if mibBuilder.loadTexts:tstNePerfRepStatusTable.setStatus(_A)
_TstNePerfRepStatusEntry_Object=MibTableRow
tstNePerfRepStatusEntry=_TstNePerfRepStatusEntry_Object((1,3,6,1,4,1,164,6,1,15,3,5,1))
tstNePerfRepStatusEntry.setIndexNames((0,_E,_W),(0,_E,_e))
if mibBuilder.loadTexts:tstNePerfRepStatusEntry.setStatus(_A)
_TstNePerfRepIteration_Type=Unsigned32
_TstNePerfRepIteration_Object=MibTableColumn
tstNePerfRepIteration=_TstNePerfRepIteration_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,1),_TstNePerfRepIteration_Type())
tstNePerfRepIteration.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepIteration.setStatus(_A)
_TstNePerfRepStartTime_Type=DateAndTime
_TstNePerfRepStartTime_Object=MibTableColumn
tstNePerfRepStartTime=_TstNePerfRepStartTime_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,2),_TstNePerfRepStartTime_Type())
tstNePerfRepStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepStartTime.setStatus(_A)
_TstNePerfRepDuration_Type=TimeTicks
_TstNePerfRepDuration_Object=MibTableColumn
tstNePerfRepDuration=_TstNePerfRepDuration_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,3),_TstNePerfRepDuration_Type())
tstNePerfRepDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepDuration.setStatus(_A)
class _TstNePerfRepStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_Z,1),(_b,2),('success',3),('fail',4),(_Ao,5),('other',6),(_A6,7),('pending',8)))
_TstNePerfRepStatus_Type.__name__=_G
_TstNePerfRepStatus_Object=MibTableColumn
tstNePerfRepStatus=_TstNePerfRepStatus_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,4),_TstNePerfRepStatus_Type())
tstNePerfRepStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepStatus.setStatus(_A)
class _TstNePerfRepType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_a,1),(_A2,2),(_A3,3),(_A4,4)))
_TstNePerfRepType_Type.__name__=_G
_TstNePerfRepType_Object=MibTableColumn
tstNePerfRepType=_TstNePerfRepType_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,5),_TstNePerfRepType_Type())
tstNePerfRepType.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepType.setStatus(_A)
_TstNePerfRepIterationNum_Type=Unsigned32
_TstNePerfRepIterationNum_Object=MibTableColumn
tstNePerfRepIterationNum=_TstNePerfRepIterationNum_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,6),_TstNePerfRepIterationNum_Type())
tstNePerfRepIterationNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepIterationNum.setStatus(_A)
_TstNePerfRepTrial_Type=Unsigned32
_TstNePerfRepTrial_Object=MibTableColumn
tstNePerfRepTrial=_TstNePerfRepTrial_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,7),_TstNePerfRepTrial_Type())
tstNePerfRepTrial.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepTrial.setStatus(_A)
_TstNePerfRepAttemptNum_Type=Unsigned32
_TstNePerfRepAttemptNum_Object=MibTableColumn
tstNePerfRepAttemptNum=_TstNePerfRepAttemptNum_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,8),_TstNePerfRepAttemptNum_Type())
tstNePerfRepAttemptNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepAttemptNum.setStatus(_A)
_TstNePerfRepFrameSize_Type=Unsigned32
_TstNePerfRepFrameSize_Object=MibTableColumn
tstNePerfRepFrameSize=_TstNePerfRepFrameSize_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,9),_TstNePerfRepFrameSize_Type())
tstNePerfRepFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepFrameSize.setStatus(_A)
_TstNePerfRepLatencyNum_Type=Unsigned32
_TstNePerfRepLatencyNum_Object=MibTableColumn
tstNePerfRepLatencyNum=_TstNePerfRepLatencyNum_Object((1,3,6,1,4,1,164,6,1,15,3,5,1,10),_TstNePerfRepLatencyNum_Type())
tstNePerfRepLatencyNum.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNePerfRepLatencyNum.setStatus(_A)
_ItuSatReportTable_Object=MibTable
ituSatReportTable=_ItuSatReportTable_Object((1,3,6,1,4,1,164,6,1,15,3,6))
if mibBuilder.loadTexts:ituSatReportTable.setStatus(_A)
_ItuSatReportEntry_Object=MibTableRow
ituSatReportEntry=_ItuSatReportEntry_Object((1,3,6,1,4,1,164,6,1,15,3,6,1))
ituSatReportEntry.setIndexNames((0,_E,_c),(0,_E,_Au),(0,_E,_Av),(0,_E,_Aw))
if mibBuilder.loadTexts:ituSatReportEntry.setStatus(_A)
_ItuSatReportPbitIndex_Type=RadTestPbitIndex
_ItuSatReportPbitIndex_Object=MibTableColumn
ituSatReportPbitIndex=_ItuSatReportPbitIndex_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,1),_ItuSatReportPbitIndex_Type())
ituSatReportPbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatReportPbitIndex.setStatus(_A)
class _ItuSatReportTestTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cirStep1',1),('cirStep2',2),('cirStep3',3),('cirStep4',4),('eir',5),('policing',6),(_n,7)))
_ItuSatReportTestTypeIndex_Type.__name__=_G
_ItuSatReportTestTypeIndex_Object=MibTableColumn
ituSatReportTestTypeIndex=_ItuSatReportTestTypeIndex_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,2),_ItuSatReportTestTypeIndex_Type())
ituSatReportTestTypeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatReportTestTypeIndex.setStatus(_A)
class _ItuSatReportDirectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward',1),('backward',2),(_p,3)))
_ItuSatReportDirectionIndex_Type.__name__=_G
_ItuSatReportDirectionIndex_Object=MibTableColumn
ituSatReportDirectionIndex=_ItuSatReportDirectionIndex_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,3),_ItuSatReportDirectionIndex_Type())
ituSatReportDirectionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatReportDirectionIndex.setStatus(_A)
_ItuSatReportResult_Type=RadTestResult
_ItuSatReportResult_Object=MibTableColumn
ituSatReportResult=_ItuSatReportResult_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,4),_ItuSatReportResult_Type())
ituSatReportResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportResult.setStatus(_A)
_ItuSatReportTxRate_Type=Gauge32
_ItuSatReportTxRate_Object=MibTableColumn
ituSatReportTxRate=_ItuSatReportTxRate_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,5),_ItuSatReportTxRate_Type())
ituSatReportTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTxRate.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTxRate.setUnits(_r)
_ItuSatReportIrMin_Type=Gauge32
_ItuSatReportIrMin_Object=MibTableColumn
ituSatReportIrMin=_ItuSatReportIrMin_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,6),_ItuSatReportIrMin_Type())
ituSatReportIrMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportIrMin.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportIrMin.setUnits(_r)
_ItuSatReportIrAverage_Type=Gauge32
_ItuSatReportIrAverage_Object=MibTableColumn
ituSatReportIrAverage=_ItuSatReportIrAverage_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,7),_ItuSatReportIrAverage_Type())
ituSatReportIrAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportIrAverage.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportIrAverage.setUnits(_r)
_ItuSatReportIrMax_Type=Gauge32
_ItuSatReportIrMax_Object=MibTableColumn
ituSatReportIrMax=_ItuSatReportIrMax_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,8),_ItuSatReportIrMax_Type())
ituSatReportIrMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportIrMax.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportIrMax.setUnits(_r)
_ItuSatReportTxFrames_Type=Counter64
_ItuSatReportTxFrames_Object=MibTableColumn
ituSatReportTxFrames=_ItuSatReportTxFrames_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,9),_ItuSatReportTxFrames_Type())
ituSatReportTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTxFrames.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTxFrames.setUnits(_s)
_ItuSatReportLostFrames_Type=Counter64
_ItuSatReportLostFrames_Object=MibTableColumn
ituSatReportLostFrames=_ItuSatReportLostFrames_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,10),_ItuSatReportLostFrames_Type())
ituSatReportLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportLostFrames.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportLostFrames.setUnits(_s)
_ItuSatReportFtdMin_Type=Gauge32
_ItuSatReportFtdMin_Object=MibTableColumn
ituSatReportFtdMin=_ItuSatReportFtdMin_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,11),_ItuSatReportFtdMin_Type())
ituSatReportFtdMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFtdMin.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFtdMin.setUnits(_F)
_ItuSatReportFtdAverage_Type=Gauge32
_ItuSatReportFtdAverage_Object=MibTableColumn
ituSatReportFtdAverage=_ItuSatReportFtdAverage_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,12),_ItuSatReportFtdAverage_Type())
ituSatReportFtdAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFtdAverage.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFtdAverage.setUnits(_F)
_ItuSatReportFtdMax_Type=Gauge32
_ItuSatReportFtdMax_Object=MibTableColumn
ituSatReportFtdMax=_ItuSatReportFtdMax_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,13),_ItuSatReportFtdMax_Type())
ituSatReportFtdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFtdMax.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFtdMax.setUnits(_F)
_ItuSatReportFtdStd_Type=Gauge32
_ItuSatReportFtdStd_Object=MibTableColumn
ituSatReportFtdStd=_ItuSatReportFtdStd_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,14),_ItuSatReportFtdStd_Type())
ituSatReportFtdStd.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFtdStd.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFtdStd.setUnits(_F)
_ItuSatReportFdvAverage_Type=Gauge32
_ItuSatReportFdvAverage_Object=MibTableColumn
ituSatReportFdvAverage=_ItuSatReportFdvAverage_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,15),_ItuSatReportFdvAverage_Type())
ituSatReportFdvAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFdvAverage.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFdvAverage.setUnits(_F)
_ItuSatReportFdvMax_Type=Gauge32
_ItuSatReportFdvMax_Object=MibTableColumn
ituSatReportFdvMax=_ItuSatReportFdvMax_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,16),_ItuSatReportFdvMax_Type())
ituSatReportFdvMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportFdvMax.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportFdvMax.setUnits(_F)
_ItuSatReportUas_Type=Counter32
_ItuSatReportUas_Object=MibTableColumn
ituSatReportUas=_ItuSatReportUas_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,17),_ItuSatReportUas_Type())
ituSatReportUas.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportUas.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportUas.setUnits(_P)
class _ItuSatReportAvailability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_ItuSatReportAvailability_Type.__name__=_H
_ItuSatReportAvailability_Object=MibTableColumn
ituSatReportAvailability=_ItuSatReportAvailability_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,18),_ItuSatReportAvailability_Type())
ituSatReportAvailability.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportAvailability.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportAvailability.setUnits(_h)
_ItuSatReportTotalTxRate_Type=Gauge32
_ItuSatReportTotalTxRate_Object=MibTableColumn
ituSatReportTotalTxRate=_ItuSatReportTotalTxRate_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,19),_ItuSatReportTotalTxRate_Type())
ituSatReportTotalTxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTotalTxRate.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTotalTxRate.setUnits(_o)
_ItuSatReportTotalIrAverage_Type=Gauge32
_ItuSatReportTotalIrAverage_Object=MibTableColumn
ituSatReportTotalIrAverage=_ItuSatReportTotalIrAverage_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,20),_ItuSatReportTotalIrAverage_Type())
ituSatReportTotalIrAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTotalIrAverage.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTotalIrAverage.setUnits(_o)
_ItuSatReportTotalTxFrames_Type=Counter64
_ItuSatReportTotalTxFrames_Object=MibTableColumn
ituSatReportTotalTxFrames=_ItuSatReportTotalTxFrames_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,21),_ItuSatReportTotalTxFrames_Type())
ituSatReportTotalTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTotalTxFrames.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTotalTxFrames.setUnits(_s)
_ItuSatReportTotalLostFrames_Type=Counter64
_ItuSatReportTotalLostFrames_Object=MibTableColumn
ituSatReportTotalLostFrames=_ItuSatReportTotalLostFrames_Object((1,3,6,1,4,1,164,6,1,15,3,6,1,22),_ItuSatReportTotalLostFrames_Type())
ituSatReportTotalLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatReportTotalLostFrames.setStatus(_A)
if mibBuilder.loadTexts:ituSatReportTotalLostFrames.setUnits(_s)
_ItuSatResponderPerfTable_Object=MibTable
ituSatResponderPerfTable=_ItuSatResponderPerfTable_Object((1,3,6,1,4,1,164,6,1,15,3,7))
if mibBuilder.loadTexts:ituSatResponderPerfTable.setStatus(_A)
_ItuSatResponderPerfEntry_Object=MibTableRow
ituSatResponderPerfEntry=_ItuSatResponderPerfEntry_Object((1,3,6,1,4,1,164,6,1,15,3,7,1))
ituSatResponderPerfEntry.setIndexNames((0,_E,_A7),(0,_E,_Ax))
if mibBuilder.loadTexts:ituSatResponderPerfEntry.setStatus(_A)
_ItuSatResponderPerfPbitIndex_Type=RadTestPbitIndex
_ItuSatResponderPerfPbitIndex_Object=MibTableColumn
ituSatResponderPerfPbitIndex=_ItuSatResponderPerfPbitIndex_Object((1,3,6,1,4,1,164,6,1,15,3,7,1,1),_ItuSatResponderPerfPbitIndex_Type())
ituSatResponderPerfPbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatResponderPerfPbitIndex.setStatus(_A)
_ItuSatResponderPerfRxFrames_Type=Counter64
_ItuSatResponderPerfRxFrames_Object=MibTableColumn
ituSatResponderPerfRxFrames=_ItuSatResponderPerfRxFrames_Object((1,3,6,1,4,1,164,6,1,15,3,7,1,2),_ItuSatResponderPerfRxFrames_Type())
ituSatResponderPerfRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatResponderPerfRxFrames.setStatus(_A)
_ItuSatResponderPerfTxFrames_Type=Counter64
_ItuSatResponderPerfTxFrames_Object=MibTableColumn
ituSatResponderPerfTxFrames=_ItuSatResponderPerfTxFrames_Object((1,3,6,1,4,1,164,6,1,15,3,7,1,3),_ItuSatResponderPerfTxFrames_Type())
ituSatResponderPerfTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatResponderPerfTxFrames.setStatus(_A)
class _ItuSatResponderPerfAssociatedMEP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_ItuSatResponderPerfAssociatedMEP_Type.__name__=_H
_ItuSatResponderPerfAssociatedMEP_Object=MibTableColumn
ituSatResponderPerfAssociatedMEP=_ItuSatResponderPerfAssociatedMEP_Object((1,3,6,1,4,1,164,6,1,15,3,7,1,4),_ItuSatResponderPerfAssociatedMEP_Type())
ituSatResponderPerfAssociatedMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatResponderPerfAssociatedMEP.setStatus(_A)
class _ItuSatResponderPerfAssociatedService_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_ItuSatResponderPerfAssociatedService_Type.__name__=_H
_ItuSatResponderPerfAssociatedService_Object=MibTableColumn
ituSatResponderPerfAssociatedService=_ItuSatResponderPerfAssociatedService_Object((1,3,6,1,4,1,164,6,1,15,3,7,1,5),_ItuSatResponderPerfAssociatedService_Type())
ituSatResponderPerfAssociatedService.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatResponderPerfAssociatedService.setStatus(_A)
_ItuSatConfPbitTable_Object=MibTable
ituSatConfPbitTable=_ItuSatConfPbitTable_Object((1,3,6,1,4,1,164,6,1,15,3,8))
if mibBuilder.loadTexts:ituSatConfPbitTable.setStatus(_A)
_ItuSatConfPbitEntry_Object=MibTableRow
ituSatConfPbitEntry=_ItuSatConfPbitEntry_Object((1,3,6,1,4,1,164,6,1,15,3,8,1))
ituSatConfPbitEntry.setIndexNames((0,_E,_c),(0,_E,_Ay),(0,_E,_Az))
if mibBuilder.loadTexts:ituSatConfPbitEntry.setStatus(_A)
_ItuSatConfPbitIndex_Type=RadTestPbitIndex
_ItuSatConfPbitIndex_Object=MibTableColumn
ituSatConfPbitIndex=_ItuSatConfPbitIndex_Object((1,3,6,1,4,1,164,6,1,15,3,8,1,1),_ItuSatConfPbitIndex_Type())
ituSatConfPbitIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatConfPbitIndex.setStatus(_A)
class _ItuSatConfPbitDirectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forward',1),('backward',2),(_p,3)))
_ItuSatConfPbitDirectionIndex_Type.__name__=_G
_ItuSatConfPbitDirectionIndex_Object=MibTableColumn
ituSatConfPbitDirectionIndex=_ItuSatConfPbitDirectionIndex_Object((1,3,6,1,4,1,164,6,1,15,3,8,1,2),_ItuSatConfPbitDirectionIndex_Type())
ituSatConfPbitDirectionIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ituSatConfPbitDirectionIndex.setStatus(_A)
_ItuSatConfPbitResult_Type=RadTestResult
_ItuSatConfPbitResult_Object=MibTableColumn
ituSatConfPbitResult=_ItuSatConfPbitResult_Object((1,3,6,1,4,1,164,6,1,15,3,8,1,3),_ItuSatConfPbitResult_Type())
ituSatConfPbitResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ituSatConfPbitResult.setStatus(_A)
_TwampReportCurrentTable_Object=MibTable
twampReportCurrentTable=_TwampReportCurrentTable_Object((1,3,6,1,4,1,164,6,1,15,3,9))
if mibBuilder.loadTexts:twampReportCurrentTable.setStatus(_A)
_TwampReportCurrentEntry_Object=MibTableRow
twampReportCurrentEntry=_TwampReportCurrentEntry_Object((1,3,6,1,4,1,164,6,1,15,3,9,1))
twampReportCurrentEntry.setIndexNames((0,_E,_d),(0,_E,_j),(0,_E,_k),(0,_E,_q))
if mibBuilder.loadTexts:twampReportCurrentEntry.setStatus(_A)
_TwampReportCurrentStartDateAndTime_Type=DateAndTime
_TwampReportCurrentStartDateAndTime_Object=MibTableColumn
twampReportCurrentStartDateAndTime=_TwampReportCurrentStartDateAndTime_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,1),_TwampReportCurrentStartDateAndTime_Type())
twampReportCurrentStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentStartDateAndTime.setStatus(_A)
_TwampReportCurrentElapsedTime_Type=Unsigned32
_TwampReportCurrentElapsedTime_Object=MibTableColumn
twampReportCurrentElapsedTime=_TwampReportCurrentElapsedTime_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,2),_TwampReportCurrentElapsedTime_Type())
twampReportCurrentElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentElapsedTime.setStatus(_A)
_TwampReportCurrentTxPackets_Type=Counter64
_TwampReportCurrentTxPackets_Object=MibTableColumn
twampReportCurrentTxPackets=_TwampReportCurrentTxPackets_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,3),_TwampReportCurrentTxPackets_Type())
twampReportCurrentTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentTxPackets.setStatus(_A)
_TwampReportCurrentRxValidPackets_Type=Counter64
_TwampReportCurrentRxValidPackets_Object=MibTableColumn
twampReportCurrentRxValidPackets=_TwampReportCurrentRxValidPackets_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,4),_TwampReportCurrentRxValidPackets_Type())
twampReportCurrentRxValidPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentRxValidPackets.setStatus(_A)
_TwampReportCurrentLossPackets_Type=Counter64
_TwampReportCurrentLossPackets_Object=MibTableColumn
twampReportCurrentLossPackets=_TwampReportCurrentLossPackets_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,5),_TwampReportCurrentLossPackets_Type())
twampReportCurrentLossPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentLossPackets.setStatus(_A)
_TwampReportCurrentAvailableSeconds_Type=Counter32
_TwampReportCurrentAvailableSeconds_Object=MibTableColumn
twampReportCurrentAvailableSeconds=_TwampReportCurrentAvailableSeconds_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,6),_TwampReportCurrentAvailableSeconds_Type())
twampReportCurrentAvailableSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentAvailableSeconds.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentAvailableSeconds.setUnits(_P)
_TwampReportCurrentDelayMin_Type=Counter32
_TwampReportCurrentDelayMin_Object=MibTableColumn
twampReportCurrentDelayMin=_TwampReportCurrentDelayMin_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,7),_TwampReportCurrentDelayMin_Type())
twampReportCurrentDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayMin.setUnits(_F)
_TwampReportCurrentDelayMax_Type=Counter32
_TwampReportCurrentDelayMax_Object=MibTableColumn
twampReportCurrentDelayMax=_TwampReportCurrentDelayMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,8),_TwampReportCurrentDelayMax_Type())
twampReportCurrentDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayMax.setUnits(_F)
_TwampReportCurrentDelaySum_Type=Counter64
_TwampReportCurrentDelaySum_Object=MibTableColumn
twampReportCurrentDelaySum=_TwampReportCurrentDelaySum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,9),_TwampReportCurrentDelaySum_Type())
twampReportCurrentDelaySum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelaySum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelaySum.setUnits(_F)
_TwampReportCurrentDelayAverage_Type=Counter32
_TwampReportCurrentDelayAverage_Object=MibTableColumn
twampReportCurrentDelayAverage=_TwampReportCurrentDelayAverage_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,10),_TwampReportCurrentDelayAverage_Type())
twampReportCurrentDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayAverage.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayAverage.setUnits(_F)
_TwampReportCurrentDelayedPackets_Type=Counter32
_TwampReportCurrentDelayedPackets_Object=MibTableColumn
twampReportCurrentDelayedPackets=_TwampReportCurrentDelayedPackets_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,11),_TwampReportCurrentDelayedPackets_Type())
twampReportCurrentDelayedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayedPackets.setStatus(_A)
_TwampReportCurrentPdvMax_Type=Counter32
_TwampReportCurrentPdvMax_Object=MibTableColumn
twampReportCurrentPdvMax=_TwampReportCurrentPdvMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,12),_TwampReportCurrentPdvMax_Type())
twampReportCurrentPdvMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentPdvMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentPdvMax.setUnits(_F)
_TwampReportCurrentIpdvMax_Type=Counter32
_TwampReportCurrentIpdvMax_Object=MibTableColumn
twampReportCurrentIpdvMax=_TwampReportCurrentIpdvMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,13),_TwampReportCurrentIpdvMax_Type())
twampReportCurrentIpdvMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvMax.setUnits(_F)
_TwampReportCurrentIpdvSum_Type=Counter64
_TwampReportCurrentIpdvSum_Object=MibTableColumn
twampReportCurrentIpdvSum=_TwampReportCurrentIpdvSum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,14),_TwampReportCurrentIpdvSum_Type())
twampReportCurrentIpdvSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvSum.setUnits(_F)
_TwampReportCurrentIpdvValidResults_Type=Counter64
_TwampReportCurrentIpdvValidResults_Object=MibTableColumn
twampReportCurrentIpdvValidResults=_TwampReportCurrentIpdvValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,15),_TwampReportCurrentIpdvValidResults_Type())
twampReportCurrentIpdvValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvValidResults.setStatus(_A)
_TwampReportCurrentIpdvFwdMax_Type=Counter64
_TwampReportCurrentIpdvFwdMax_Object=MibTableColumn
twampReportCurrentIpdvFwdMax=_TwampReportCurrentIpdvFwdMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,16),_TwampReportCurrentIpdvFwdMax_Type())
twampReportCurrentIpdvFwdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvFwdMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvFwdMax.setUnits(_F)
_TwampReportCurrentIpdvFwdSum_Type=Counter64
_TwampReportCurrentIpdvFwdSum_Object=MibTableColumn
twampReportCurrentIpdvFwdSum=_TwampReportCurrentIpdvFwdSum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,17),_TwampReportCurrentIpdvFwdSum_Type())
twampReportCurrentIpdvFwdSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvFwdSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvFwdSum.setUnits(_F)
_TwampReportCurrentIpdvFwdValidResults_Type=Counter64
_TwampReportCurrentIpdvFwdValidResults_Object=MibTableColumn
twampReportCurrentIpdvFwdValidResults=_TwampReportCurrentIpdvFwdValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,18),_TwampReportCurrentIpdvFwdValidResults_Type())
twampReportCurrentIpdvFwdValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvFwdValidResults.setStatus(_A)
_TwampReportCurrentIpdvBckMax_Type=Counter64
_TwampReportCurrentIpdvBckMax_Object=MibTableColumn
twampReportCurrentIpdvBckMax=_TwampReportCurrentIpdvBckMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,19),_TwampReportCurrentIpdvBckMax_Type())
twampReportCurrentIpdvBckMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvBckMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvBckMax.setUnits(_F)
_TwampReportCurrentIpdvBckSum_Type=Counter64
_TwampReportCurrentIpdvBckSum_Object=MibTableColumn
twampReportCurrentIpdvBckSum=_TwampReportCurrentIpdvBckSum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,20),_TwampReportCurrentIpdvBckSum_Type())
twampReportCurrentIpdvBckSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvBckSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentIpdvBckSum.setUnits(_F)
_TwampReportCurrentIpdvBckValidResults_Type=Counter64
_TwampReportCurrentIpdvBckValidResults_Object=MibTableColumn
twampReportCurrentIpdvBckValidResults=_TwampReportCurrentIpdvBckValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,21),_TwampReportCurrentIpdvBckValidResults_Type())
twampReportCurrentIpdvBckValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentIpdvBckValidResults.setStatus(_A)
_TwampReportCurrentReorderedFwd_Type=Counter32
_TwampReportCurrentReorderedFwd_Object=MibTableColumn
twampReportCurrentReorderedFwd=_TwampReportCurrentReorderedFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,22),_TwampReportCurrentReorderedFwd_Type())
twampReportCurrentReorderedFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentReorderedFwd.setStatus(_A)
_TwampReportCurrentReorderedBck_Type=Counter32
_TwampReportCurrentReorderedBck_Object=MibTableColumn
twampReportCurrentReorderedBck=_TwampReportCurrentReorderedBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,23),_TwampReportCurrentReorderedBck_Type())
twampReportCurrentReorderedBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentReorderedBck.setStatus(_A)
_TwampReportCurrentDuplicateFwd_Type=Counter32
_TwampReportCurrentDuplicateFwd_Object=MibTableColumn
twampReportCurrentDuplicateFwd=_TwampReportCurrentDuplicateFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,24),_TwampReportCurrentDuplicateFwd_Type())
twampReportCurrentDuplicateFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDuplicateFwd.setStatus(_A)
_TwampReportCurrentDuplicateBck_Type=Counter32
_TwampReportCurrentDuplicateBck_Object=MibTableColumn
twampReportCurrentDuplicateBck=_TwampReportCurrentDuplicateBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,25),_TwampReportCurrentDuplicateBck_Type())
twampReportCurrentDuplicateBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDuplicateBck.setStatus(_A)
_TwampReportCurrentFragmentedFwd_Type=Counter32
_TwampReportCurrentFragmentedFwd_Object=MibTableColumn
twampReportCurrentFragmentedFwd=_TwampReportCurrentFragmentedFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,26),_TwampReportCurrentFragmentedFwd_Type())
twampReportCurrentFragmentedFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentFragmentedFwd.setStatus(_A)
_TwampReportCurrentFragmentedBck_Type=Counter32
_TwampReportCurrentFragmentedBck_Object=MibTableColumn
twampReportCurrentFragmentedBck=_TwampReportCurrentFragmentedBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,27),_TwampReportCurrentFragmentedBck_Type())
twampReportCurrentFragmentedBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentFragmentedBck.setStatus(_A)
_TwampReportCurrentDelayFwdMin_Type=Counter32
_TwampReportCurrentDelayFwdMin_Object=MibTableColumn
twampReportCurrentDelayFwdMin=_TwampReportCurrentDelayFwdMin_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,28),_TwampReportCurrentDelayFwdMin_Type())
twampReportCurrentDelayFwdMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdMin.setUnits(_F)
_TwampReportCurrentDelayFwdMax_Type=Counter32
_TwampReportCurrentDelayFwdMax_Object=MibTableColumn
twampReportCurrentDelayFwdMax=_TwampReportCurrentDelayFwdMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,29),_TwampReportCurrentDelayFwdMax_Type())
twampReportCurrentDelayFwdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdMax.setUnits(_F)
_TwampReportCurrentDelayFwdSum_Type=Counter64
_TwampReportCurrentDelayFwdSum_Object=MibTableColumn
twampReportCurrentDelayFwdSum=_TwampReportCurrentDelayFwdSum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,30),_TwampReportCurrentDelayFwdSum_Type())
twampReportCurrentDelayFwdSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayFwdSum.setUnits(_F)
_TwampReportCurrentDelayBckMin_Type=Counter32
_TwampReportCurrentDelayBckMin_Object=MibTableColumn
twampReportCurrentDelayBckMin=_TwampReportCurrentDelayBckMin_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,31),_TwampReportCurrentDelayBckMin_Type())
twampReportCurrentDelayBckMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayBckMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayBckMin.setUnits(_F)
_TwampReportCurrentDelayBckMax_Type=Counter32
_TwampReportCurrentDelayBckMax_Object=MibTableColumn
twampReportCurrentDelayBckMax=_TwampReportCurrentDelayBckMax_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,32),_TwampReportCurrentDelayBckMax_Type())
twampReportCurrentDelayBckMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayBckMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayBckMax.setUnits(_F)
_TwampReportCurrentDelayBckSum_Type=Counter64
_TwampReportCurrentDelayBckSum_Object=MibTableColumn
twampReportCurrentDelayBckSum=_TwampReportCurrentDelayBckSum_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,33),_TwampReportCurrentDelayBckSum_Type())
twampReportCurrentDelayBckSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayBckSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentDelayBckSum.setUnits(_F)
_TwampReportCurrentDelayedPacketsFwd_Type=Counter32
_TwampReportCurrentDelayedPacketsFwd_Object=MibTableColumn
twampReportCurrentDelayedPacketsFwd=_TwampReportCurrentDelayedPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,34),_TwampReportCurrentDelayedPacketsFwd_Type())
twampReportCurrentDelayedPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayedPacketsFwd.setStatus(_A)
_TwampReportCurrentDelayedPacketsBck_Type=Counter32
_TwampReportCurrentDelayedPacketsBck_Object=MibTableColumn
twampReportCurrentDelayedPacketsBck=_TwampReportCurrentDelayedPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,35),_TwampReportCurrentDelayedPacketsBck_Type())
twampReportCurrentDelayedPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentDelayedPacketsBck.setStatus(_A)
_TwampReportCurrentPdvMaxFwd_Type=Counter32
_TwampReportCurrentPdvMaxFwd_Object=MibTableColumn
twampReportCurrentPdvMaxFwd=_TwampReportCurrentPdvMaxFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,36),_TwampReportCurrentPdvMaxFwd_Type())
twampReportCurrentPdvMaxFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentPdvMaxFwd.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentPdvMaxFwd.setUnits(_F)
_TwampReportCurrentPdvMaxBck_Type=Counter32
_TwampReportCurrentPdvMaxBck_Object=MibTableColumn
twampReportCurrentPdvMaxBck=_TwampReportCurrentPdvMaxBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,37),_TwampReportCurrentPdvMaxBck_Type())
twampReportCurrentPdvMaxBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentPdvMaxBck.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentPdvMaxBck.setUnits(_F)
_TwampReportCurrentTxPacketsFwd_Type=Counter64
_TwampReportCurrentTxPacketsFwd_Object=MibTableColumn
twampReportCurrentTxPacketsFwd=_TwampReportCurrentTxPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,38),_TwampReportCurrentTxPacketsFwd_Type())
twampReportCurrentTxPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentTxPacketsFwd.setStatus(_A)
_TwampReportCurrentTxPacketsBck_Type=Counter64
_TwampReportCurrentTxPacketsBck_Object=MibTableColumn
twampReportCurrentTxPacketsBck=_TwampReportCurrentTxPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,39),_TwampReportCurrentTxPacketsBck_Type())
twampReportCurrentTxPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentTxPacketsBck.setStatus(_A)
_TwampReportCurrentRxValidPacketsFwd_Type=Counter64
_TwampReportCurrentRxValidPacketsFwd_Object=MibTableColumn
twampReportCurrentRxValidPacketsFwd=_TwampReportCurrentRxValidPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,40),_TwampReportCurrentRxValidPacketsFwd_Type())
twampReportCurrentRxValidPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentRxValidPacketsFwd.setStatus(_A)
_TwampReportCurrentRxValidPacketsBck_Type=Counter64
_TwampReportCurrentRxValidPacketsBck_Object=MibTableColumn
twampReportCurrentRxValidPacketsBck=_TwampReportCurrentRxValidPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,41),_TwampReportCurrentRxValidPacketsBck_Type())
twampReportCurrentRxValidPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentRxValidPacketsBck.setStatus(_A)
_TwampReportCurrentLossPacketsFwd_Type=Counter64
_TwampReportCurrentLossPacketsFwd_Object=MibTableColumn
twampReportCurrentLossPacketsFwd=_TwampReportCurrentLossPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,42),_TwampReportCurrentLossPacketsFwd_Type())
twampReportCurrentLossPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentLossPacketsFwd.setStatus(_A)
_TwampReportCurrentLossPacketsBck_Type=Counter64
_TwampReportCurrentLossPacketsBck_Object=MibTableColumn
twampReportCurrentLossPacketsBck=_TwampReportCurrentLossPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,43),_TwampReportCurrentLossPacketsBck_Type())
twampReportCurrentLossPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentLossPacketsBck.setStatus(_A)
_TwampReportCurrentAvailableSecondsFwd_Type=Counter32
_TwampReportCurrentAvailableSecondsFwd_Object=MibTableColumn
twampReportCurrentAvailableSecondsFwd=_TwampReportCurrentAvailableSecondsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,44),_TwampReportCurrentAvailableSecondsFwd_Type())
twampReportCurrentAvailableSecondsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentAvailableSecondsFwd.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentAvailableSecondsFwd.setUnits(_P)
_TwampReportCurrentAvailableSecondsBck_Type=Counter32
_TwampReportCurrentAvailableSecondsBck_Object=MibTableColumn
twampReportCurrentAvailableSecondsBck=_TwampReportCurrentAvailableSecondsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,45),_TwampReportCurrentAvailableSecondsBck_Type())
twampReportCurrentAvailableSecondsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentAvailableSecondsBck.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentAvailableSecondsBck.setUnits(_P)
_TwampReportCurrentRxSyncValidPacketsFwd_Type=Counter64
_TwampReportCurrentRxSyncValidPacketsFwd_Object=MibTableColumn
twampReportCurrentRxSyncValidPacketsFwd=_TwampReportCurrentRxSyncValidPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,46),_TwampReportCurrentRxSyncValidPacketsFwd_Type())
twampReportCurrentRxSyncValidPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentRxSyncValidPacketsFwd.setStatus(_A)
_TwampReportCurrentRxSyncValidPacketsBck_Type=Counter64
_TwampReportCurrentRxSyncValidPacketsBck_Object=MibTableColumn
twampReportCurrentRxSyncValidPacketsBck=_TwampReportCurrentRxSyncValidPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,47),_TwampReportCurrentRxSyncValidPacketsBck_Type())
twampReportCurrentRxSyncValidPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentRxSyncValidPacketsBck.setStatus(_A)
_TwampReportCurrentSyncSeconds_Type=Counter32
_TwampReportCurrentSyncSeconds_Object=MibTableColumn
twampReportCurrentSyncSeconds=_TwampReportCurrentSyncSeconds_Object((1,3,6,1,4,1,164,6,1,15,3,9,1,48),_TwampReportCurrentSyncSeconds_Type())
twampReportCurrentSyncSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportCurrentSyncSeconds.setStatus(_A)
if mibBuilder.loadTexts:twampReportCurrentSyncSeconds.setUnits(_P)
_TwampReportIntervalTable_Object=MibTable
twampReportIntervalTable=_TwampReportIntervalTable_Object((1,3,6,1,4,1,164,6,1,15,3,10))
if mibBuilder.loadTexts:twampReportIntervalTable.setStatus(_A)
_TwampReportIntervalEntry_Object=MibTableRow
twampReportIntervalEntry=_TwampReportIntervalEntry_Object((1,3,6,1,4,1,164,6,1,15,3,10,1))
twampReportIntervalEntry.setIndexNames((0,_E,_d),(0,_E,_j),(0,_E,_k),(0,_E,_q),(0,_E,_A_))
if mibBuilder.loadTexts:twampReportIntervalEntry.setStatus(_A)
_TwampReportIntervalNumber_Type=Unsigned32
_TwampReportIntervalNumber_Object=MibTableColumn
twampReportIntervalNumber=_TwampReportIntervalNumber_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,1),_TwampReportIntervalNumber_Type())
twampReportIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:twampReportIntervalNumber.setStatus(_A)
_TwampReportIntervalStartDateAndTime_Type=DateAndTime
_TwampReportIntervalStartDateAndTime_Object=MibTableColumn
twampReportIntervalStartDateAndTime=_TwampReportIntervalStartDateAndTime_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,2),_TwampReportIntervalStartDateAndTime_Type())
twampReportIntervalStartDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalStartDateAndTime.setStatus(_A)
_TwampReportIntervalElapsedTime_Type=Unsigned32
_TwampReportIntervalElapsedTime_Object=MibTableColumn
twampReportIntervalElapsedTime=_TwampReportIntervalElapsedTime_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,3),_TwampReportIntervalElapsedTime_Type())
twampReportIntervalElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalElapsedTime.setStatus(_A)
_TwampReportIntervalTxPackets_Type=Counter64
_TwampReportIntervalTxPackets_Object=MibTableColumn
twampReportIntervalTxPackets=_TwampReportIntervalTxPackets_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,4),_TwampReportIntervalTxPackets_Type())
twampReportIntervalTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalTxPackets.setStatus(_A)
_TwampReportIntervalRxValidPackets_Type=Counter64
_TwampReportIntervalRxValidPackets_Object=MibTableColumn
twampReportIntervalRxValidPackets=_TwampReportIntervalRxValidPackets_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,5),_TwampReportIntervalRxValidPackets_Type())
twampReportIntervalRxValidPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalRxValidPackets.setStatus(_A)
_TwampReportIntervalLossPackets_Type=Counter64
_TwampReportIntervalLossPackets_Object=MibTableColumn
twampReportIntervalLossPackets=_TwampReportIntervalLossPackets_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,6),_TwampReportIntervalLossPackets_Type())
twampReportIntervalLossPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalLossPackets.setStatus(_A)
_TwampReportIntervalAvailableSeconds_Type=Counter32
_TwampReportIntervalAvailableSeconds_Object=MibTableColumn
twampReportIntervalAvailableSeconds=_TwampReportIntervalAvailableSeconds_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,7),_TwampReportIntervalAvailableSeconds_Type())
twampReportIntervalAvailableSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalAvailableSeconds.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalAvailableSeconds.setUnits(_P)
_TwampReportIntervalDelayMin_Type=Counter32
_TwampReportIntervalDelayMin_Object=MibTableColumn
twampReportIntervalDelayMin=_TwampReportIntervalDelayMin_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,8),_TwampReportIntervalDelayMin_Type())
twampReportIntervalDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayMin.setUnits(_F)
_TwampReportIntervalDelayMax_Type=Counter32
_TwampReportIntervalDelayMax_Object=MibTableColumn
twampReportIntervalDelayMax=_TwampReportIntervalDelayMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,9),_TwampReportIntervalDelayMax_Type())
twampReportIntervalDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayMax.setUnits(_F)
_TwampReportIntervalDelaySum_Type=Counter64
_TwampReportIntervalDelaySum_Object=MibTableColumn
twampReportIntervalDelaySum=_TwampReportIntervalDelaySum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,10),_TwampReportIntervalDelaySum_Type())
twampReportIntervalDelaySum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelaySum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelaySum.setUnits(_F)
_TwampReportIntervalDelayAverage_Type=Counter32
_TwampReportIntervalDelayAverage_Object=MibTableColumn
twampReportIntervalDelayAverage=_TwampReportIntervalDelayAverage_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,11),_TwampReportIntervalDelayAverage_Type())
twampReportIntervalDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayAverage.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayAverage.setUnits(_F)
_TwampReportIntervalDelayedPackets_Type=Counter32
_TwampReportIntervalDelayedPackets_Object=MibTableColumn
twampReportIntervalDelayedPackets=_TwampReportIntervalDelayedPackets_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,12),_TwampReportIntervalDelayedPackets_Type())
twampReportIntervalDelayedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayedPackets.setStatus(_A)
_TwampReportIntervalPdvMax_Type=Counter32
_TwampReportIntervalPdvMax_Object=MibTableColumn
twampReportIntervalPdvMax=_TwampReportIntervalPdvMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,13),_TwampReportIntervalPdvMax_Type())
twampReportIntervalPdvMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalPdvMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalPdvMax.setUnits(_F)
_TwampReportIntervalIpdvMax_Type=Counter32
_TwampReportIntervalIpdvMax_Object=MibTableColumn
twampReportIntervalIpdvMax=_TwampReportIntervalIpdvMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,14),_TwampReportIntervalIpdvMax_Type())
twampReportIntervalIpdvMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvMax.setUnits(_F)
_TwampReportIntervalIpdvSum_Type=Counter64
_TwampReportIntervalIpdvSum_Object=MibTableColumn
twampReportIntervalIpdvSum=_TwampReportIntervalIpdvSum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,15),_TwampReportIntervalIpdvSum_Type())
twampReportIntervalIpdvSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvSum.setUnits(_F)
_TwampReportIntervalIpdvValidResults_Type=Counter64
_TwampReportIntervalIpdvValidResults_Object=MibTableColumn
twampReportIntervalIpdvValidResults=_TwampReportIntervalIpdvValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,16),_TwampReportIntervalIpdvValidResults_Type())
twampReportIntervalIpdvValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvValidResults.setStatus(_A)
_TwampReportIntervalIpdvFwdMax_Type=Counter64
_TwampReportIntervalIpdvFwdMax_Object=MibTableColumn
twampReportIntervalIpdvFwdMax=_TwampReportIntervalIpdvFwdMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,17),_TwampReportIntervalIpdvFwdMax_Type())
twampReportIntervalIpdvFwdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvFwdMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvFwdMax.setUnits(_F)
_TwampReportIntervalIpdvFwdSum_Type=Counter64
_TwampReportIntervalIpdvFwdSum_Object=MibTableColumn
twampReportIntervalIpdvFwdSum=_TwampReportIntervalIpdvFwdSum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,18),_TwampReportIntervalIpdvFwdSum_Type())
twampReportIntervalIpdvFwdSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvFwdSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvFwdSum.setUnits(_F)
_TwampReportIntervalIpdvFwdValidResults_Type=Counter64
_TwampReportIntervalIpdvFwdValidResults_Object=MibTableColumn
twampReportIntervalIpdvFwdValidResults=_TwampReportIntervalIpdvFwdValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,19),_TwampReportIntervalIpdvFwdValidResults_Type())
twampReportIntervalIpdvFwdValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvFwdValidResults.setStatus(_A)
_TwampReportIntervalIpdvBckMax_Type=Counter64
_TwampReportIntervalIpdvBckMax_Object=MibTableColumn
twampReportIntervalIpdvBckMax=_TwampReportIntervalIpdvBckMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,20),_TwampReportIntervalIpdvBckMax_Type())
twampReportIntervalIpdvBckMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvBckMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvBckMax.setUnits(_F)
_TwampReportIntervalIpdvBckSum_Type=Counter64
_TwampReportIntervalIpdvBckSum_Object=MibTableColumn
twampReportIntervalIpdvBckSum=_TwampReportIntervalIpdvBckSum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,21),_TwampReportIntervalIpdvBckSum_Type())
twampReportIntervalIpdvBckSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvBckSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalIpdvBckSum.setUnits(_F)
_TwampReportIntervalIpdvBckValidResults_Type=Counter64
_TwampReportIntervalIpdvBckValidResults_Object=MibTableColumn
twampReportIntervalIpdvBckValidResults=_TwampReportIntervalIpdvBckValidResults_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,22),_TwampReportIntervalIpdvBckValidResults_Type())
twampReportIntervalIpdvBckValidResults.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalIpdvBckValidResults.setStatus(_A)
_TwampReportIntervalReorderedFwd_Type=Counter32
_TwampReportIntervalReorderedFwd_Object=MibTableColumn
twampReportIntervalReorderedFwd=_TwampReportIntervalReorderedFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,23),_TwampReportIntervalReorderedFwd_Type())
twampReportIntervalReorderedFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalReorderedFwd.setStatus(_A)
_TwampReportIntervalReorderedBck_Type=Counter32
_TwampReportIntervalReorderedBck_Object=MibTableColumn
twampReportIntervalReorderedBck=_TwampReportIntervalReorderedBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,24),_TwampReportIntervalReorderedBck_Type())
twampReportIntervalReorderedBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalReorderedBck.setStatus(_A)
_TwampReportIntervalDuplicateFwd_Type=Counter32
_TwampReportIntervalDuplicateFwd_Object=MibTableColumn
twampReportIntervalDuplicateFwd=_TwampReportIntervalDuplicateFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,25),_TwampReportIntervalDuplicateFwd_Type())
twampReportIntervalDuplicateFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDuplicateFwd.setStatus(_A)
_TwampReportIntervalDuplicateBck_Type=Counter32
_TwampReportIntervalDuplicateBck_Object=MibTableColumn
twampReportIntervalDuplicateBck=_TwampReportIntervalDuplicateBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,26),_TwampReportIntervalDuplicateBck_Type())
twampReportIntervalDuplicateBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDuplicateBck.setStatus(_A)
_TwampReportIntervalFragmentedFwd_Type=Counter32
_TwampReportIntervalFragmentedFwd_Object=MibTableColumn
twampReportIntervalFragmentedFwd=_TwampReportIntervalFragmentedFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,27),_TwampReportIntervalFragmentedFwd_Type())
twampReportIntervalFragmentedFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalFragmentedFwd.setStatus(_A)
_TwampReportIntervalFragmentedBck_Type=Counter32
_TwampReportIntervalFragmentedBck_Object=MibTableColumn
twampReportIntervalFragmentedBck=_TwampReportIntervalFragmentedBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,28),_TwampReportIntervalFragmentedBck_Type())
twampReportIntervalFragmentedBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalFragmentedBck.setStatus(_A)
_TwampReportIntervalDelayFwdMin_Type=Counter32
_TwampReportIntervalDelayFwdMin_Object=MibTableColumn
twampReportIntervalDelayFwdMin=_TwampReportIntervalDelayFwdMin_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,29),_TwampReportIntervalDelayFwdMin_Type())
twampReportIntervalDelayFwdMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdMin.setUnits(_F)
_TwampReportIntervalDelayFwdMax_Type=Counter32
_TwampReportIntervalDelayFwdMax_Object=MibTableColumn
twampReportIntervalDelayFwdMax=_TwampReportIntervalDelayFwdMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,30),_TwampReportIntervalDelayFwdMax_Type())
twampReportIntervalDelayFwdMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdMax.setUnits(_F)
_TwampReportIntervalDelayFwdSum_Type=Counter64
_TwampReportIntervalDelayFwdSum_Object=MibTableColumn
twampReportIntervalDelayFwdSum=_TwampReportIntervalDelayFwdSum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,31),_TwampReportIntervalDelayFwdSum_Type())
twampReportIntervalDelayFwdSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayFwdSum.setUnits(_F)
_TwampReportIntervalDelayBckMin_Type=Counter32
_TwampReportIntervalDelayBckMin_Object=MibTableColumn
twampReportIntervalDelayBckMin=_TwampReportIntervalDelayBckMin_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,32),_TwampReportIntervalDelayBckMin_Type())
twampReportIntervalDelayBckMin.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayBckMin.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayBckMin.setUnits(_F)
_TwampReportIntervalDelayBckMax_Type=Counter32
_TwampReportIntervalDelayBckMax_Object=MibTableColumn
twampReportIntervalDelayBckMax=_TwampReportIntervalDelayBckMax_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,33),_TwampReportIntervalDelayBckMax_Type())
twampReportIntervalDelayBckMax.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayBckMax.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayBckMax.setUnits(_F)
_TwampReportIntervalDelayBckSum_Type=Counter64
_TwampReportIntervalDelayBckSum_Object=MibTableColumn
twampReportIntervalDelayBckSum=_TwampReportIntervalDelayBckSum_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,34),_TwampReportIntervalDelayBckSum_Type())
twampReportIntervalDelayBckSum.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayBckSum.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalDelayBckSum.setUnits(_F)
_TwampReportIntervalDelayedPacketsFwd_Type=Counter32
_TwampReportIntervalDelayedPacketsFwd_Object=MibTableColumn
twampReportIntervalDelayedPacketsFwd=_TwampReportIntervalDelayedPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,35),_TwampReportIntervalDelayedPacketsFwd_Type())
twampReportIntervalDelayedPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayedPacketsFwd.setStatus(_A)
_TwampReportIntervalDelayedPacketsBck_Type=Counter32
_TwampReportIntervalDelayedPacketsBck_Object=MibTableColumn
twampReportIntervalDelayedPacketsBck=_TwampReportIntervalDelayedPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,36),_TwampReportIntervalDelayedPacketsBck_Type())
twampReportIntervalDelayedPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalDelayedPacketsBck.setStatus(_A)
_TwampReportIntervalPdvMaxFwd_Type=Counter32
_TwampReportIntervalPdvMaxFwd_Object=MibTableColumn
twampReportIntervalPdvMaxFwd=_TwampReportIntervalPdvMaxFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,37),_TwampReportIntervalPdvMaxFwd_Type())
twampReportIntervalPdvMaxFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalPdvMaxFwd.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalPdvMaxFwd.setUnits(_F)
_TwampReportIntervalPdvMaxBck_Type=Counter32
_TwampReportIntervalPdvMaxBck_Object=MibTableColumn
twampReportIntervalPdvMaxBck=_TwampReportIntervalPdvMaxBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,38),_TwampReportIntervalPdvMaxBck_Type())
twampReportIntervalPdvMaxBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalPdvMaxBck.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalPdvMaxBck.setUnits(_F)
_TwampReportIntervalTxPacketsFwd_Type=Counter64
_TwampReportIntervalTxPacketsFwd_Object=MibTableColumn
twampReportIntervalTxPacketsFwd=_TwampReportIntervalTxPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,39),_TwampReportIntervalTxPacketsFwd_Type())
twampReportIntervalTxPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalTxPacketsFwd.setStatus(_A)
_TwampReportIntervalValidData_Type=TruthValue
_TwampReportIntervalValidData_Object=MibTableColumn
twampReportIntervalValidData=_TwampReportIntervalValidData_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,40),_TwampReportIntervalValidData_Type())
twampReportIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalValidData.setStatus(_A)
_TwampReportIntervalTxPacketsBck_Type=Counter64
_TwampReportIntervalTxPacketsBck_Object=MibTableColumn
twampReportIntervalTxPacketsBck=_TwampReportIntervalTxPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,41),_TwampReportIntervalTxPacketsBck_Type())
twampReportIntervalTxPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalTxPacketsBck.setStatus(_A)
_TwampReportIntervalRxValidPacketsFwd_Type=Counter64
_TwampReportIntervalRxValidPacketsFwd_Object=MibTableColumn
twampReportIntervalRxValidPacketsFwd=_TwampReportIntervalRxValidPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,42),_TwampReportIntervalRxValidPacketsFwd_Type())
twampReportIntervalRxValidPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalRxValidPacketsFwd.setStatus(_A)
_TwampReportIntervalRxValidPacketsBck_Type=Counter64
_TwampReportIntervalRxValidPacketsBck_Object=MibTableColumn
twampReportIntervalRxValidPacketsBck=_TwampReportIntervalRxValidPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,43),_TwampReportIntervalRxValidPacketsBck_Type())
twampReportIntervalRxValidPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalRxValidPacketsBck.setStatus(_A)
_TwampReportIntervalLossPacketsFwd_Type=Counter64
_TwampReportIntervalLossPacketsFwd_Object=MibTableColumn
twampReportIntervalLossPacketsFwd=_TwampReportIntervalLossPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,44),_TwampReportIntervalLossPacketsFwd_Type())
twampReportIntervalLossPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalLossPacketsFwd.setStatus(_A)
_TwampReportIntervalLossPacketsBck_Type=Counter64
_TwampReportIntervalLossPacketsBck_Object=MibTableColumn
twampReportIntervalLossPacketsBck=_TwampReportIntervalLossPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,45),_TwampReportIntervalLossPacketsBck_Type())
twampReportIntervalLossPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalLossPacketsBck.setStatus(_A)
_TwampReportIntervalAvailableSecondsFwd_Type=Counter32
_TwampReportIntervalAvailableSecondsFwd_Object=MibTableColumn
twampReportIntervalAvailableSecondsFwd=_TwampReportIntervalAvailableSecondsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,46),_TwampReportIntervalAvailableSecondsFwd_Type())
twampReportIntervalAvailableSecondsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalAvailableSecondsFwd.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalAvailableSecondsFwd.setUnits(_P)
_TwampReportIntervalAvailableSecondsBck_Type=Counter32
_TwampReportIntervalAvailableSecondsBck_Object=MibTableColumn
twampReportIntervalAvailableSecondsBck=_TwampReportIntervalAvailableSecondsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,47),_TwampReportIntervalAvailableSecondsBck_Type())
twampReportIntervalAvailableSecondsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalAvailableSecondsBck.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalAvailableSecondsBck.setUnits(_P)
_TwampReportIntervalRxSyncValidPacketsFwd_Type=Counter64
_TwampReportIntervalRxSyncValidPacketsFwd_Object=MibTableColumn
twampReportIntervalRxSyncValidPacketsFwd=_TwampReportIntervalRxSyncValidPacketsFwd_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,48),_TwampReportIntervalRxSyncValidPacketsFwd_Type())
twampReportIntervalRxSyncValidPacketsFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalRxSyncValidPacketsFwd.setStatus(_A)
_TwampReportIntervalRxSyncValidPacketsBck_Type=Counter64
_TwampReportIntervalRxSyncValidPacketsBck_Object=MibTableColumn
twampReportIntervalRxSyncValidPacketsBck=_TwampReportIntervalRxSyncValidPacketsBck_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,49),_TwampReportIntervalRxSyncValidPacketsBck_Type())
twampReportIntervalRxSyncValidPacketsBck.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalRxSyncValidPacketsBck.setStatus(_A)
_TwampReportIntervalSyncSeconds_Type=Counter32
_TwampReportIntervalSyncSeconds_Object=MibTableColumn
twampReportIntervalSyncSeconds=_TwampReportIntervalSyncSeconds_Object((1,3,6,1,4,1,164,6,1,15,3,10,1,50),_TwampReportIntervalSyncSeconds_Type())
twampReportIntervalSyncSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:twampReportIntervalSyncSeconds.setStatus(_A)
if mibBuilder.loadTexts:twampReportIntervalSyncSeconds.setUnits(_P)
_TstNeThroughputIterationTable_Object=MibTable
tstNeThroughputIterationTable=_TstNeThroughputIterationTable_Object((1,3,6,1,4,1,164,6,1,15,3,12))
if mibBuilder.loadTexts:tstNeThroughputIterationTable.setStatus(_A)
_TstNeThroughputIterationEntry_Object=MibTableRow
tstNeThroughputIterationEntry=_TstNeThroughputIterationEntry_Object((1,3,6,1,4,1,164,6,1,15,3,12,1))
tstNeThroughputIterationEntry.setIndexNames((0,_E,_W),(0,_E,_AC),(0,_E,_AD),(0,_E,_B0))
if mibBuilder.loadTexts:tstNeThroughputIterationEntry.setStatus(_A)
_TstNeThroughputIteration_Type=Gauge32
_TstNeThroughputIteration_Object=MibTableColumn
tstNeThroughputIteration=_TstNeThroughputIteration_Object((1,3,6,1,4,1,164,6,1,15,3,12,1,1),_TstNeThroughputIteration_Type())
tstNeThroughputIteration.setMaxAccess(_I)
if mibBuilder.loadTexts:tstNeThroughputIteration.setStatus(_A)
_TstNeThroughputIterationBPS_Type=Unsigned32
_TstNeThroughputIterationBPS_Object=MibTableColumn
tstNeThroughputIterationBPS=_TstNeThroughputIterationBPS_Object((1,3,6,1,4,1,164,6,1,15,3,12,1,2),_TstNeThroughputIterationBPS_Type())
tstNeThroughputIterationBPS.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNeThroughputIterationBPS.setStatus(_A)
_TstNeThroughputLossPacket_Type=Gauge32
_TstNeThroughputLossPacket_Object=MibTableColumn
tstNeThroughputLossPacket=_TstNeThroughputLossPacket_Object((1,3,6,1,4,1,164,6,1,15,3,12,1,3),_TstNeThroughputLossPacket_Type())
tstNeThroughputLossPacket.setMaxAccess(_B)
if mibBuilder.loadTexts:tstNeThroughputLossPacket.setStatus(_A)
systemRfc2544TestStart=NotificationType((1,3,6,1,4,1,164,6,1,15,0,2))
systemRfc2544TestStart.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_AE)))
if mibBuilder.loadTexts:systemRfc2544TestStart.setStatus(_A)
systemRfc2544TestEnd=NotificationType((1,3,6,1,4,1,164,6,1,15,0,3))
systemRfc2544TestEnd.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_AE)))
if mibBuilder.loadTexts:systemRfc2544TestEnd.setStatus(_A)
systemItuSatTestStart=NotificationType((1,3,6,1,4,1,164,6,1,15,0,4))
systemItuSatTestStart.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_B1),(_E,_t)))
if mibBuilder.loadTexts:systemItuSatTestStart.setStatus(_A)
systemItuSatConfigurationTestEnd=NotificationType((1,3,6,1,4,1,164,6,1,15,0,5))
systemItuSatConfigurationTestEnd.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_B2),(_E,_t)))
if mibBuilder.loadTexts:systemItuSatConfigurationTestEnd.setStatus(_A)
systemItuSatPerformanceTestEnd=NotificationType((1,3,6,1,4,1,164,6,1,15,0,6))
systemItuSatPerformanceTestEnd.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_B3),(_E,_t)))
if mibBuilder.loadTexts:systemItuSatPerformanceTestEnd.setStatus(_A)
systemItuSatResponderActivated=NotificationType((1,3,6,1,4,1,164,6,1,15,0,7))
systemItuSatResponderActivated.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:systemItuSatResponderActivated.setStatus(_A)
systemItuSatResponderDeactivated=NotificationType((1,3,6,1,4,1,164,6,1,15,0,8))
systemItuSatResponderDeactivated.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_U,_V),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:systemItuSatResponderDeactivated.setStatus(_A)
twampPeerTestStarted=NotificationType((1,3,6,1,4,1,164,6,1,15,0,9))
twampPeerTestStarted.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_u)))
if mibBuilder.loadTexts:twampPeerTestStarted.setStatus(_A)
twampPeerTestStopped=NotificationType((1,3,6,1,4,1,164,6,1,15,0,10))
twampPeerTestStopped.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_u)))
if mibBuilder.loadTexts:twampPeerTestStopped.setStatus(_A)
twampSessionLossRatioTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,11))
twampSessionLossRatioTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionLossRatioTca.setStatus(_A)
twampSessionDelayTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,12))
twampSessionDelayTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionDelayTca.setStatus(_A)
twampSessionDelayVarTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,13))
twampSessionDelayVarTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S),(_E,_v)))
if mibBuilder.loadTexts:twampSessionDelayVarTca.setStatus(_A)
twampSessionUnavailable=NotificationType((1,3,6,1,4,1,164,6,1,15,0,14))
twampSessionUnavailable.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_w)))
if mibBuilder.loadTexts:twampSessionUnavailable.setStatus(_A)
twampSessionForwardUnavailable=NotificationType((1,3,6,1,4,1,164,6,1,15,0,15))
twampSessionForwardUnavailable.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_w)))
if mibBuilder.loadTexts:twampSessionForwardUnavailable.setStatus(_A)
twampSessionBackwardUnavailable=NotificationType((1,3,6,1,4,1,164,6,1,15,0,16))
twampSessionBackwardUnavailable.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_w)))
if mibBuilder.loadTexts:twampSessionBackwardUnavailable.setStatus(_A)
twampSessionForwardLossRatioTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,17))
twampSessionForwardLossRatioTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionForwardLossRatioTca.setStatus(_A)
twampSessionForwardDelayTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,18))
twampSessionForwardDelayTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionForwardDelayTca.setStatus(_A)
twampSessionForwardDelayVarTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,19))
twampSessionForwardDelayVarTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S),(_E,_v)))
if mibBuilder.loadTexts:twampSessionForwardDelayVarTca.setStatus(_A)
twampSessionBackwardLossRatioTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,20))
twampSessionBackwardLossRatioTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionBackwardLossRatioTca.setStatus(_A)
twampSessionBackwardDelayTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,21))
twampSessionBackwardDelayTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S)))
if mibBuilder.loadTexts:twampSessionBackwardDelayTca.setStatus(_A)
twampSessionBackwardDelayVarTca=NotificationType((1,3,6,1,4,1,164,6,1,15,0,22))
twampSessionBackwardDelayVarTca.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_Q),(_E,_S),(_E,_v)))
if mibBuilder.loadTexts:twampSessionBackwardDelayVarTca.setStatus(_A)
twampPeerTodAccuracyOutOfLimit=NotificationType((1,3,6,1,4,1,164,6,1,15,0,37))
twampPeerTodAccuracyOutOfLimit.setObjects(*((_D,_N),(_D,_J),(_D,_L),(_D,_M),(_D,_K),(_D,_O),(_E,_u)))
if mibBuilder.loadTexts:twampPeerTodAccuracyOutOfLimit.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RadTestPerfRepFrameSize':RadTestPerfRepFrameSize,'RadTestPerfresultFrameSize':RadTestPerfresultFrameSize,'RadTestPbitIndex':RadTestPbitIndex,'radTest':radTest,'radTestPrefRepEvents':radTestPrefRepEvents,'systemRfc2544TestStart':systemRfc2544TestStart,'systemRfc2544TestEnd':systemRfc2544TestEnd,'systemItuSatTestStart':systemItuSatTestStart,'systemItuSatConfigurationTestEnd':systemItuSatConfigurationTestEnd,'systemItuSatPerformanceTestEnd':systemItuSatPerformanceTestEnd,'systemItuSatResponderActivated':systemItuSatResponderActivated,'systemItuSatResponderDeactivated':systemItuSatResponderDeactivated,'twampPeerTestStarted':twampPeerTestStarted,'twampPeerTestStopped':twampPeerTestStopped,'twampSessionLossRatioTca':twampSessionLossRatioTca,'twampSessionDelayTca':twampSessionDelayTca,'twampSessionDelayVarTca':twampSessionDelayVarTca,'twampSessionUnavailable':twampSessionUnavailable,'twampSessionForwardUnavailable':twampSessionForwardUnavailable,'twampSessionBackwardUnavailable':twampSessionBackwardUnavailable,'twampSessionForwardLossRatioTca':twampSessionForwardLossRatioTca,'twampSessionForwardDelayTca':twampSessionForwardDelayTca,'twampSessionForwardDelayVarTca':twampSessionForwardDelayVarTca,'twampSessionBackwardLossRatioTca':twampSessionBackwardLossRatioTca,'twampSessionBackwardDelayTca':twampSessionBackwardDelayTca,'twampSessionBackwardDelayVarTca':twampSessionBackwardDelayVarTca,'twampPeerTodAccuracyOutOfLimit':twampPeerTodAccuracyOutOfLimit,'radTestPrefRepProfile':radTestPrefRepProfile,'tstNePerfRepProfileTable':tstNePerfRepProfileTable,'tstNePerfRepProfileEntry':tstNePerfRepProfileEntry,_AN:tstNePerfRepProfileId,'tstNePerfRepProfileName':tstNePerfRepProfileName,'tstNePerfRepProfileRowStatus':tstNePerfRepProfileRowStatus,'tstNePerfRepProfileFrameSize':tstNePerfRepProfileFrameSize,'tstNePerfRepProfilePattern':tstNePerfRepProfilePattern,'tstNePerfRepProfileDirection':tstNePerfRepProfileDirection,'tstNePerfRepProfileTlv':tstNePerfRepProfileTlv,'tstNePerfRepProfileNumberOfFramesInOneBurst':tstNePerfRepProfileNumberOfFramesInOneBurst,'tstNePerfRepProfileFrameLossTolerance':tstNePerfRepProfileFrameLossTolerance,'tstNePerfRepProfileBinarySearchResolution':tstNePerfRepProfileBinarySearchResolution,'tstNePerfRepProfileNumberOfTrials':tstNePerfRepProfileNumberOfTrials,'tstNePerfRepProfileLearningFramesMode':tstNePerfRepProfileLearningFramesMode,'tstNePerfRepProfileLearningFrames':tstNePerfRepProfileLearningFrames,'tstNePerfRepProfileCustomSize':tstNePerfRepProfileCustomSize,'tstNePerfRepProfileTransmitLck':tstNePerfRepProfileTransmitLck,'tstMepFlowTable':tstMepFlowTable,'tstMepFlowEntry':tstMepFlowEntry,_AT:tstMepFlowIndex,'tstMepFlowFlowIdx':tstMepFlowFlowIdx,'ituSatProfileTable':ituSatProfileTable,'ituSatProfileEntry':ituSatProfileEntry,_z:ituSatProfileIndex,'ituSatProfileName':ituSatProfileName,'ituSatProfileRowStatus':ituSatProfileRowStatus,'ituSatProfileEtherType':ituSatProfileEtherType,'ituSatProfileFrameSize':ituSatProfileFrameSize,'ituSatProfileUniFlrThreshold':ituSatProfileUniFlrThreshold,'ituSatProfileUniFtdThreshold':ituSatProfileUniFtdThreshold,'ituSatProfileUniFdvThreshold':ituSatProfileUniFdvThreshold,'ituSatProfileUniAvailThreshold':ituSatProfileUniAvailThreshold,'ituSatProfileBiFlrThreshold':ituSatProfileBiFlrThreshold,'ituSatProfileBiFtdThreshold':ituSatProfileBiFtdThreshold,'ituSatProfileBiFdvThreshold':ituSatProfileBiFdvThreshold,'ituSatProfileBiAvailThreshold':ituSatProfileBiAvailThreshold,'ituSatProfileScope':ituSatProfileScope,'ituSatProfileDirection':ituSatProfileDirection,'ituSatProfileColorMode':ituSatProfileColorMode,'ituSatProfileTrafficPolicing':ituSatProfileTrafficPolicing,'ituSatProfileCirSteps':ituSatProfileCirSteps,'ituSatProfileConfDuration':ituSatProfileConfDuration,'ituSatProfilePerfDuration':ituSatProfilePerfDuration,'ituSatProfileRateConvention':ituSatProfileRateConvention,'ituSatProfileResponderType':ituSatProfileResponderType,'ituSatProfilePbitTable':ituSatProfilePbitTable,'ituSatProfilePbitEntry':ituSatProfilePbitEntry,_AU:ituSatProfilePbitIndex,'ituSatProfilePbitRowStatus':ituSatProfilePbitRowStatus,'ituSatProfilePbitFrameSize':ituSatProfilePbitFrameSize,'ituSatProfilePbitUniFlrThreshold':ituSatProfilePbitUniFlrThreshold,'ituSatProfilePbitUniFtdThreshold':ituSatProfilePbitUniFtdThreshold,'ituSatProfilePbitUniFdvThreshold':ituSatProfilePbitUniFdvThreshold,'ituSatProfilePbitUniAvailThreshold':ituSatProfilePbitUniAvailThreshold,'ituSatProfilePbitBiFlrThreshold':ituSatProfilePbitBiFlrThreshold,'ituSatProfilePbitBiFtdThreshold':ituSatProfilePbitBiFtdThreshold,'ituSatProfilePbitBiFdvThreshold':ituSatProfilePbitBiFdvThreshold,'ituSatProfilePbitBiAvailThreshold':ituSatProfilePbitBiAvailThreshold,'twampTestProfileTable':twampTestProfileTable,'twampTestProfileEntry':twampTestProfileEntry,_AV:twampTestProfileId,'twampTestProfileRowStatus':twampTestProfileRowStatus,'twampTestProfileName':twampTestProfileName,'twampTestProfilePayloadLength':twampTestProfilePayloadLength,'twampTestProfileTxRate':twampTestProfileTxRate,'twampTestProfileLossTimeout':twampTestProfileLossTimeout,'twampTestProfileLossRatioThreshold':twampTestProfileLossRatioThreshold,'twampTestProfileDelayThreshold':twampTestProfileDelayThreshold,'twampTestProfileDelayVarThreshold':twampTestProfileDelayVarThreshold,_v:twampTestProfileDelayVarEventType,'radTestPrefRepTest':radTestPrefRepTest,'tstNePerfRepTestTable':tstNePerfRepTestTable,'tstNePerfRepTestEntry':tstNePerfRepTestEntry,_W:tstNePerfRepTestId,'tstNePerfRepTestRowStatus':tstNePerfRepTestRowStatus,_AE:tstNePerfRepTestType,'tstNePerfRepTestProfileId':tstNePerfRepTestProfileId,'tstNePerfRepTestEntity':tstNePerfRepTestEntity,'tstNePerfRepTestActivation':tstNePerfRepTestActivation,'tstNePerfRepTestStatus':tstNePerfRepTestStatus,'tstNePerfRepTestActivationDateAndTime':tstNePerfRepTestActivationDateAndTime,'tstNePerfRepTestActivationRecurrenceTime':tstNePerfRepTestActivationRecurrenceTime,'tstNePerfRepTestMaxRate':tstNePerfRepTestMaxRate,'tstNePerfRepTestElapsedTime':tstNePerfRepTestElapsedTime,'tstNePerfRepTestResetResults':tstNePerfRepTestResetResults,'tstNePerfRepTestRateConvention':tstNePerfRepTestRateConvention,'tstNePerfRepTestFrameCompensation':tstNePerfRepTestFrameCompensation,'tstNePerfRepTestMaxTestDuration':tstNePerfRepTestMaxTestDuration,'tstNePerfRepTestAssociatedFlow':tstNePerfRepTestAssociatedFlow,'ituSatGeneratorTable':ituSatGeneratorTable,'ituSatGeneratorEntry':ituSatGeneratorEntry,_c:ituSatGeneratorIndex,_t:ituSatGeneratorName,'ituSatGeneratorRowStatus':ituSatGeneratorRowStatus,'ituSatGeneratorServicePointer':ituSatGeneratorServicePointer,'ituSatGeneratorProvisionedPbits':ituSatGeneratorProvisionedPbits,'ituSatGeneratorProfile':ituSatGeneratorProfile,'ituSatGeneratorCmd':ituSatGeneratorCmd,'ituSatGeneratorConfChanged':ituSatGeneratorConfChanged,_B1:ituSatGeneratorStatus,'ituSatGeneratorTimeRemaining':ituSatGeneratorTimeRemaining,'ituSatGeneratorCurrentPhase':ituSatGeneratorCurrentPhase,'ituSatGeneratorDestination':ituSatGeneratorDestination,'ituSatGeneratorSource':ituSatGeneratorSource,'ituSatGeneratorInnerTag':ituSatGeneratorInnerTag,'ituSatGeneratorOuterTag':ituSatGeneratorOuterTag,'ituSatGeneratorTestedPbits':ituSatGeneratorTestedPbits,'ituSatGeneratorStartTime':ituSatGeneratorStartTime,'ituSatGeneratorEndTime':ituSatGeneratorEndTime,'ituSatGeneratorTimeElapsed':ituSatGeneratorTimeElapsed,_B2:ituSatGeneratorConfResult,_B3:ituSatGeneratorPerfResult,'ituSatGeneratorConfDuration':ituSatGeneratorConfDuration,'ituSatGeneratorPerfDuration':ituSatGeneratorPerfDuration,'ituSatGeneratorScope':ituSatGeneratorScope,'ituSatGeneratorServiceBinding':ituSatGeneratorServiceBinding,'ituSatGeneratorServiceName':ituSatGeneratorServiceName,'ituSatGeneratorEgressPort':ituSatGeneratorEgressPort,'ituSatGeneratorProvisionedDestination':ituSatGeneratorProvisionedDestination,'ituSatGeneratorFlowTable':ituSatGeneratorFlowTable,'ituSatGeneratorFlowEntry':ituSatGeneratorFlowEntry,_Ac:ituSatGeneratorFlowPbitIndex,'ituSatGeneratorFlowNameTx':ituSatGeneratorFlowNameTx,'ituSatGeneratorFlowNameRx':ituSatGeneratorFlowNameRx,'ituSatGeneratorFlowCir':ituSatGeneratorFlowCir,'ituSatGeneratorFlowEir':ituSatGeneratorFlowEir,'ituSatGeneratorFlowAssociatedMEP':ituSatGeneratorFlowAssociatedMEP,'ituSatGeneratorFlowAssociatedService':ituSatGeneratorFlowAssociatedService,'ituSatGeneratorFlowBwpInUse':ituSatGeneratorFlowBwpInUse,'ituSatResponderTable':ituSatResponderTable,'ituSatResponderEntry':ituSatResponderEntry,_A7:ituSatResponderIndex,_AG:ituSatResponderName,'ituSatResponderRowStatus':ituSatResponderRowStatus,'ituSatResponderServicePointer':ituSatResponderServicePointer,'ituSatResponderProfile':ituSatResponderProfile,'ituSatResponderCmd':ituSatResponderCmd,_AF:ituSatResponderStatus,'ituSatResponderServiceBinding':ituSatResponderServiceBinding,'ituSatResponderServiceName':ituSatResponderServiceName,'ituSatResponderEgressPort':ituSatResponderEgressPort,'ituSatGeneratorPolicerTable':ituSatGeneratorPolicerTable,'ituSatGeneratorPolicerEntry':ituSatGeneratorPolicerEntry,_Ad:ituSatGeneratorPolicerPbitIndex,'ituSatGeneratorPolicerRowStatus':ituSatGeneratorPolicerRowStatus,'ituSatGeneratorPolicerCir':ituSatGeneratorPolicerCir,'ituSatGeneratorPolicerCbs':ituSatGeneratorPolicerCbs,'ituSatGeneratorPolicerEir':ituSatGeneratorPolicerEir,'ituSatGeneratorPolicerEbs':ituSatGeneratorPolicerEbs,'ituSatGeneratorPolicerProfile':ituSatGeneratorPolicerProfile,'twampControllerTable':twampControllerTable,'twampControllerEntry':twampControllerEntry,_d:twampControllerId,'twampControllerRowStatus':twampControllerRowStatus,_w:twampControllerName,'twampControllerStatus':twampControllerStatus,'twampControllerType':twampControllerType,'twampControllerL2Probe':twampControllerL2Probe,'twampControllerIngressEgressPort':twampControllerIngressEgressPort,'twampControllerOuterVlan':twampControllerOuterVlan,'twampControllerInnerVlan':twampControllerInnerVlan,'twampControllerOuterPbit':twampControllerOuterPbit,'twampControllerInnerPbit':twampControllerInnerPbit,'twampControllerRouterEntity':twampControllerRouterEntity,'twampControllerLocalAddrType':twampControllerLocalAddrType,'twampControllerLocalAddr':twampControllerLocalAddr,'twampControllerAssociatedRI':twampControllerAssociatedRI,'twampControllerTodStatus':twampControllerTodStatus,'twampPeerTable':twampPeerTable,'twampPeerEntry':twampPeerEntry,_j:twampPeerAddrType,_k:twampPeerAddr,'twampPeerRowStatus':twampPeerRowStatus,'twampPeerActivateCmd':twampPeerActivateCmd,'twampPeerActivateDuration':twampPeerActivateDuration,'twampPeerStartDateAndTime':twampPeerStartDateAndTime,'twampPeerCalcMode':twampPeerCalcMode,'twampPeerResponderSeqNum':twampPeerResponderSeqNum,'twampPeerResponderTodStatus':twampPeerResponderTodStatus,'twampPeerElapsedTime':twampPeerElapsedTime,_u:twampPeerDescr,'twampPeerLastCalcMode':twampPeerLastCalcMode,'twampPeerLastResponderSeqNum':twampPeerLastResponderSeqNum,'twampContSessionTable':twampContSessionTable,'twampContSessionEntry':twampContSessionEntry,_q:twampContSessionId,'twampContSessionRowStatus':twampContSessionRowStatus,_Q:twampContSessionName,'twampContSessionStartDateAndTime':twampContSessionStartDateAndTime,_S:twampContSessionStatus,'twampContSessionLocalL4PortNumber':twampContSessionLocalL4PortNumber,'twampContSessionPeerL4PortNumber':twampContSessionPeerL4PortNumber,'twampContSessionPeerDscp':twampContSessionPeerDscp,'twampContSessionTestProfileId':twampContSessionTestProfileId,'twampContSessionTxPackets':twampContSessionTxPackets,'twampContSessionRxPackets':twampContSessionRxPackets,'twampContSessionResult':twampContSessionResult,'twampContSessionConfChanged':twampContSessionConfChanged,'twampContSessionConvertedIndex':twampContSessionConvertedIndex,'twampContSessionResultFwd':twampContSessionResultFwd,'twampContSessionResultBck':twampContSessionResultBck,'twampResponderTable':twampResponderTable,'twampResponderEntry':twampResponderEntry,_AB:twampResponderId,'twampResponderRowStatus':twampResponderRowStatus,'twampResponderName':twampResponderName,'twampResponderStatus':twampResponderStatus,'twampResponderType':twampResponderType,'twampResponderL2Probe':twampResponderL2Probe,'twampResponderIngressEgressPort':twampResponderIngressEgressPort,'twampResponderOuterVlan':twampResponderOuterVlan,'twampResponderInnerVlan':twampResponderInnerVlan,'twampResponderOuterPbit':twampResponderOuterPbit,'twampResponderInnerPbit':twampResponderInnerPbit,'twampResponderRouterEntity':twampResponderRouterEntity,'twampResponderLocalAddrType':twampResponderLocalAddrType,'twampResponderLocalAddr':twampResponderLocalAddr,'twampResponderAssociatedRI':twampResponderAssociatedRI,'twampResponderTxSeqNum':twampResponderTxSeqNum,'twampResponderTxExtendedInfo':twampResponderTxExtendedInfo,'twampResSessionTable':twampResSessionTable,'twampResSessionEntry':twampResSessionEntry,_Ah:twampResSessionId,'twampResSessionRowStatus':twampResSessionRowStatus,'twampResSessionName':twampResSessionName,'twampResSessionLocalL4PortNumber':twampResSessionLocalL4PortNumber,'twampResSessionTxPackets':twampResSessionTxPackets,'twampResSessionRxPackets':twampResSessionRxPackets,'ituSatSingleCosFlowTable':ituSatSingleCosFlowTable,'ituSatSingleCosFlowEntry':ituSatSingleCosFlowEntry,_Ai:ituSatSingleCosFlowFunction,_Aj:ituSatSingleCosFlowFunctionIndex,_Ak:ituSatSingleCosFlowIdx1,_Al:ituSatSingleCosFlowIdx2,'ituSatSingleCosFlowRowStatus':ituSatSingleCosFlowRowStatus,'radTestPerfRepResults':radTestPerfRepResults,'tstNePerfRepGeneralResultsTable':tstNePerfRepGeneralResultsTable,'tstNePerfRepGeneralResultsEntry':tstNePerfRepGeneralResultsEntry,_Am:tstNePerfRepGeneralResultsTestType,_An:tstNePerfRepGeneralResultsTrialNumber,'tstNePerfRepGeneralResultsStatus':tstNePerfRepGeneralResultsStatus,'tstNePerfRepGeneralResultsDuration':tstNePerfRepGeneralResultsDuration,'throughputReportTable':throughputReportTable,'throughputReportEntry':throughputReportEntry,_AC:throughputReportTrialNumber,_AD:throughputReportPacketSize,'throughputReportThroughputTheoretical':throughputReportThroughputTheoretical,'throughputReportResults':throughputReportResults,'throughputReportDataPattern':throughputReportDataPattern,'throughputReportResultsBps':throughputReportResultsBps,'throughputReportCustomPacketSize':throughputReportCustomPacketSize,'latencyReportTable':latencyReportTable,'latencyReportEntry':latencyReportEntry,_Ap:latencyReportTrialNumber,_Aq:latencyReportPacketSize,'latencyReportType':latencyReportType,'latencyReportResult':latencyReportResult,'latencyReportCustomPacketSize':latencyReportCustomPacketSize,'framelossRateReportTable':framelossRateReportTable,'framelossRateReportEntry':framelossRateReportEntry,_Ar:framelossRateReportTrialNumber,_As:framelossRateReportPacketSize,_At:framelossRateReportInputRate,'framelossRateReportResults':framelossRateReportResults,'framelossRateReportCustomPacketSize':framelossRateReportCustomPacketSize,'tstNePerfRepStatusTable':tstNePerfRepStatusTable,'tstNePerfRepStatusEntry':tstNePerfRepStatusEntry,_e:tstNePerfRepIteration,'tstNePerfRepStartTime':tstNePerfRepStartTime,'tstNePerfRepDuration':tstNePerfRepDuration,'tstNePerfRepStatus':tstNePerfRepStatus,'tstNePerfRepType':tstNePerfRepType,'tstNePerfRepIterationNum':tstNePerfRepIterationNum,'tstNePerfRepTrial':tstNePerfRepTrial,'tstNePerfRepAttemptNum':tstNePerfRepAttemptNum,'tstNePerfRepFrameSize':tstNePerfRepFrameSize,'tstNePerfRepLatencyNum':tstNePerfRepLatencyNum,'ituSatReportTable':ituSatReportTable,'ituSatReportEntry':ituSatReportEntry,_Au:ituSatReportPbitIndex,_Av:ituSatReportTestTypeIndex,_Aw:ituSatReportDirectionIndex,'ituSatReportResult':ituSatReportResult,'ituSatReportTxRate':ituSatReportTxRate,'ituSatReportIrMin':ituSatReportIrMin,'ituSatReportIrAverage':ituSatReportIrAverage,'ituSatReportIrMax':ituSatReportIrMax,'ituSatReportTxFrames':ituSatReportTxFrames,'ituSatReportLostFrames':ituSatReportLostFrames,'ituSatReportFtdMin':ituSatReportFtdMin,'ituSatReportFtdAverage':ituSatReportFtdAverage,'ituSatReportFtdMax':ituSatReportFtdMax,'ituSatReportFtdStd':ituSatReportFtdStd,'ituSatReportFdvAverage':ituSatReportFdvAverage,'ituSatReportFdvMax':ituSatReportFdvMax,'ituSatReportUas':ituSatReportUas,'ituSatReportAvailability':ituSatReportAvailability,'ituSatReportTotalTxRate':ituSatReportTotalTxRate,'ituSatReportTotalIrAverage':ituSatReportTotalIrAverage,'ituSatReportTotalTxFrames':ituSatReportTotalTxFrames,'ituSatReportTotalLostFrames':ituSatReportTotalLostFrames,'ituSatResponderPerfTable':ituSatResponderPerfTable,'ituSatResponderPerfEntry':ituSatResponderPerfEntry,_Ax:ituSatResponderPerfPbitIndex,'ituSatResponderPerfRxFrames':ituSatResponderPerfRxFrames,'ituSatResponderPerfTxFrames':ituSatResponderPerfTxFrames,'ituSatResponderPerfAssociatedMEP':ituSatResponderPerfAssociatedMEP,'ituSatResponderPerfAssociatedService':ituSatResponderPerfAssociatedService,'ituSatConfPbitTable':ituSatConfPbitTable,'ituSatConfPbitEntry':ituSatConfPbitEntry,_Ay:ituSatConfPbitIndex,_Az:ituSatConfPbitDirectionIndex,'ituSatConfPbitResult':ituSatConfPbitResult,'twampReportCurrentTable':twampReportCurrentTable,'twampReportCurrentEntry':twampReportCurrentEntry,'twampReportCurrentStartDateAndTime':twampReportCurrentStartDateAndTime,'twampReportCurrentElapsedTime':twampReportCurrentElapsedTime,'twampReportCurrentTxPackets':twampReportCurrentTxPackets,'twampReportCurrentRxValidPackets':twampReportCurrentRxValidPackets,'twampReportCurrentLossPackets':twampReportCurrentLossPackets,'twampReportCurrentAvailableSeconds':twampReportCurrentAvailableSeconds,'twampReportCurrentDelayMin':twampReportCurrentDelayMin,'twampReportCurrentDelayMax':twampReportCurrentDelayMax,'twampReportCurrentDelaySum':twampReportCurrentDelaySum,'twampReportCurrentDelayAverage':twampReportCurrentDelayAverage,'twampReportCurrentDelayedPackets':twampReportCurrentDelayedPackets,'twampReportCurrentPdvMax':twampReportCurrentPdvMax,'twampReportCurrentIpdvMax':twampReportCurrentIpdvMax,'twampReportCurrentIpdvSum':twampReportCurrentIpdvSum,'twampReportCurrentIpdvValidResults':twampReportCurrentIpdvValidResults,'twampReportCurrentIpdvFwdMax':twampReportCurrentIpdvFwdMax,'twampReportCurrentIpdvFwdSum':twampReportCurrentIpdvFwdSum,'twampReportCurrentIpdvFwdValidResults':twampReportCurrentIpdvFwdValidResults,'twampReportCurrentIpdvBckMax':twampReportCurrentIpdvBckMax,'twampReportCurrentIpdvBckSum':twampReportCurrentIpdvBckSum,'twampReportCurrentIpdvBckValidResults':twampReportCurrentIpdvBckValidResults,'twampReportCurrentReorderedFwd':twampReportCurrentReorderedFwd,'twampReportCurrentReorderedBck':twampReportCurrentReorderedBck,'twampReportCurrentDuplicateFwd':twampReportCurrentDuplicateFwd,'twampReportCurrentDuplicateBck':twampReportCurrentDuplicateBck,'twampReportCurrentFragmentedFwd':twampReportCurrentFragmentedFwd,'twampReportCurrentFragmentedBck':twampReportCurrentFragmentedBck,'twampReportCurrentDelayFwdMin':twampReportCurrentDelayFwdMin,'twampReportCurrentDelayFwdMax':twampReportCurrentDelayFwdMax,'twampReportCurrentDelayFwdSum':twampReportCurrentDelayFwdSum,'twampReportCurrentDelayBckMin':twampReportCurrentDelayBckMin,'twampReportCurrentDelayBckMax':twampReportCurrentDelayBckMax,'twampReportCurrentDelayBckSum':twampReportCurrentDelayBckSum,'twampReportCurrentDelayedPacketsFwd':twampReportCurrentDelayedPacketsFwd,'twampReportCurrentDelayedPacketsBck':twampReportCurrentDelayedPacketsBck,'twampReportCurrentPdvMaxFwd':twampReportCurrentPdvMaxFwd,'twampReportCurrentPdvMaxBck':twampReportCurrentPdvMaxBck,'twampReportCurrentTxPacketsFwd':twampReportCurrentTxPacketsFwd,'twampReportCurrentTxPacketsBck':twampReportCurrentTxPacketsBck,'twampReportCurrentRxValidPacketsFwd':twampReportCurrentRxValidPacketsFwd,'twampReportCurrentRxValidPacketsBck':twampReportCurrentRxValidPacketsBck,'twampReportCurrentLossPacketsFwd':twampReportCurrentLossPacketsFwd,'twampReportCurrentLossPacketsBck':twampReportCurrentLossPacketsBck,'twampReportCurrentAvailableSecondsFwd':twampReportCurrentAvailableSecondsFwd,'twampReportCurrentAvailableSecondsBck':twampReportCurrentAvailableSecondsBck,'twampReportCurrentRxSyncValidPacketsFwd':twampReportCurrentRxSyncValidPacketsFwd,'twampReportCurrentRxSyncValidPacketsBck':twampReportCurrentRxSyncValidPacketsBck,'twampReportCurrentSyncSeconds':twampReportCurrentSyncSeconds,'twampReportIntervalTable':twampReportIntervalTable,'twampReportIntervalEntry':twampReportIntervalEntry,_A_:twampReportIntervalNumber,'twampReportIntervalStartDateAndTime':twampReportIntervalStartDateAndTime,'twampReportIntervalElapsedTime':twampReportIntervalElapsedTime,'twampReportIntervalTxPackets':twampReportIntervalTxPackets,'twampReportIntervalRxValidPackets':twampReportIntervalRxValidPackets,'twampReportIntervalLossPackets':twampReportIntervalLossPackets,'twampReportIntervalAvailableSeconds':twampReportIntervalAvailableSeconds,'twampReportIntervalDelayMin':twampReportIntervalDelayMin,'twampReportIntervalDelayMax':twampReportIntervalDelayMax,'twampReportIntervalDelaySum':twampReportIntervalDelaySum,'twampReportIntervalDelayAverage':twampReportIntervalDelayAverage,'twampReportIntervalDelayedPackets':twampReportIntervalDelayedPackets,'twampReportIntervalPdvMax':twampReportIntervalPdvMax,'twampReportIntervalIpdvMax':twampReportIntervalIpdvMax,'twampReportIntervalIpdvSum':twampReportIntervalIpdvSum,'twampReportIntervalIpdvValidResults':twampReportIntervalIpdvValidResults,'twampReportIntervalIpdvFwdMax':twampReportIntervalIpdvFwdMax,'twampReportIntervalIpdvFwdSum':twampReportIntervalIpdvFwdSum,'twampReportIntervalIpdvFwdValidResults':twampReportIntervalIpdvFwdValidResults,'twampReportIntervalIpdvBckMax':twampReportIntervalIpdvBckMax,'twampReportIntervalIpdvBckSum':twampReportIntervalIpdvBckSum,'twampReportIntervalIpdvBckValidResults':twampReportIntervalIpdvBckValidResults,'twampReportIntervalReorderedFwd':twampReportIntervalReorderedFwd,'twampReportIntervalReorderedBck':twampReportIntervalReorderedBck,'twampReportIntervalDuplicateFwd':twampReportIntervalDuplicateFwd,'twampReportIntervalDuplicateBck':twampReportIntervalDuplicateBck,'twampReportIntervalFragmentedFwd':twampReportIntervalFragmentedFwd,'twampReportIntervalFragmentedBck':twampReportIntervalFragmentedBck,'twampReportIntervalDelayFwdMin':twampReportIntervalDelayFwdMin,'twampReportIntervalDelayFwdMax':twampReportIntervalDelayFwdMax,'twampReportIntervalDelayFwdSum':twampReportIntervalDelayFwdSum,'twampReportIntervalDelayBckMin':twampReportIntervalDelayBckMin,'twampReportIntervalDelayBckMax':twampReportIntervalDelayBckMax,'twampReportIntervalDelayBckSum':twampReportIntervalDelayBckSum,'twampReportIntervalDelayedPacketsFwd':twampReportIntervalDelayedPacketsFwd,'twampReportIntervalDelayedPacketsBck':twampReportIntervalDelayedPacketsBck,'twampReportIntervalPdvMaxFwd':twampReportIntervalPdvMaxFwd,'twampReportIntervalPdvMaxBck':twampReportIntervalPdvMaxBck,'twampReportIntervalTxPacketsFwd':twampReportIntervalTxPacketsFwd,'twampReportIntervalValidData':twampReportIntervalValidData,'twampReportIntervalTxPacketsBck':twampReportIntervalTxPacketsBck,'twampReportIntervalRxValidPacketsFwd':twampReportIntervalRxValidPacketsFwd,'twampReportIntervalRxValidPacketsBck':twampReportIntervalRxValidPacketsBck,'twampReportIntervalLossPacketsFwd':twampReportIntervalLossPacketsFwd,'twampReportIntervalLossPacketsBck':twampReportIntervalLossPacketsBck,'twampReportIntervalAvailableSecondsFwd':twampReportIntervalAvailableSecondsFwd,'twampReportIntervalAvailableSecondsBck':twampReportIntervalAvailableSecondsBck,'twampReportIntervalRxSyncValidPacketsFwd':twampReportIntervalRxSyncValidPacketsFwd,'twampReportIntervalRxSyncValidPacketsBck':twampReportIntervalRxSyncValidPacketsBck,'twampReportIntervalSyncSeconds':twampReportIntervalSyncSeconds,'tstNeThroughputIterationTable':tstNeThroughputIterationTable,'tstNeThroughputIterationEntry':tstNeThroughputIterationEntry,_B0:tstNeThroughputIteration,'tstNeThroughputIterationBPS':tstNeThroughputIterationBPS,'tstNeThroughputLossPacket':tstNeThroughputLossPacket})