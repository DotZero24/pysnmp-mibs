_b='wwpLeosBenchmarkProfileFrameSizeIndex'
_a='wwpLeosBenchmarkProfileFrameSizeProfileId'
_Z='wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex'
_Y='wwpLeosBenchmarkProfilePdvStatsProfileId'
_X='wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex'
_W='wwpLeosBenchmarkProfileLatencyStatsProfileId'
_V='wwpLeosBenchmarkProfileFramelossStatsRateIndex'
_U='wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex'
_T='wwpLeosBenchmarkProfileFramelossStatsProfileId'
_S='wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex'
_R='wwpLeosBenchmarkProfileThroughputStatsProfileId'
_Q='t15min'
_P='wwpLeosBenchmarkProfileEntryId'
_O='running'
_N='processingResults'
_M='waitingForResidualPackets'
_L='OctetString'
_K='DisplayString'
_J='done'
_I='stoppedByUser'
_H='stoppedByDurationTimer'
_G='stoppedByIntervalTimer'
_F='idle'
_E='WWP-LEOS-BENCHMARK-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'MacAddress','PhysAddress','TextualConvention','TruthValue')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosBenchmarkMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,43))
if mibBuilder.loadTexts:wwpLeosBenchmarkMIB.setRevisions(('2012-02-13 08:00','2012-02-03 08:00','2010-12-14 08:00','2010-11-25 08:00','2010-11-15 08:00'))
class BenchmarkLatencyPdvTestState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,1),('sendingTraffic',2),('waitingForTimestampData',3),(_M,4),(_N,5),(_G,6),(_H,7),(_I,8),(_J,9)))
_WwpLeosBenchmarkMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkMIBObjects=_WwpLeosBenchmarkMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1))
_WwpLeosBenchmarkModule_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkModule=_WwpLeosBenchmarkModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,1))
class _WwpLeosBenchmarkRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('reflector',2),('generator',3)))
_WwpLeosBenchmarkRole_Type.__name__=_C
_WwpLeosBenchmarkRole_Object=MibScalar
wwpLeosBenchmarkRole=_WwpLeosBenchmarkRole_Object((1,3,6,1,4,1,6141,2,60,43,1,1,1),_WwpLeosBenchmarkRole_Type())
wwpLeosBenchmarkRole.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkRole.setStatus(_A)
class _WwpLeosBenchmarkPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosBenchmarkPort_Type.__name__=_C
_WwpLeosBenchmarkPort_Object=MibScalar
wwpLeosBenchmarkPort=_WwpLeosBenchmarkPort_Object((1,3,6,1,4,1,6141,2,60,43,1,1,2),_WwpLeosBenchmarkPort_Type())
wwpLeosBenchmarkPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkPort.setStatus(_A)
class _WwpLeosBenchmarkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('inService',2),('outOfService',3)))
_WwpLeosBenchmarkMode_Type.__name__=_C
_WwpLeosBenchmarkMode_Object=MibScalar
wwpLeosBenchmarkMode=_WwpLeosBenchmarkMode_Object((1,3,6,1,4,1,6141,2,60,43,1,1,3),_WwpLeosBenchmarkMode_Type())
wwpLeosBenchmarkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkMode.setStatus(_A)
_WwpLeosBenchmarkEnable_Type=TruthValue
_WwpLeosBenchmarkEnable_Object=MibScalar
wwpLeosBenchmarkEnable=_WwpLeosBenchmarkEnable_Object((1,3,6,1,4,1,6141,2,60,43,1,1,4),_WwpLeosBenchmarkEnable_Type())
wwpLeosBenchmarkEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkEnable.setStatus(_A)
_WwpLeosBenchmarkOperEnable_Type=TruthValue
_WwpLeosBenchmarkOperEnable_Object=MibScalar
wwpLeosBenchmarkOperEnable=_WwpLeosBenchmarkOperEnable_Object((1,3,6,1,4,1,6141,2,60,43,1,1,5),_WwpLeosBenchmarkOperEnable_Type())
wwpLeosBenchmarkOperEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkOperEnable.setStatus(_A)
_WwpLeosBenchmarkLocalFpgaMac_Type=MacAddress
_WwpLeosBenchmarkLocalFpgaMac_Object=MibScalar
wwpLeosBenchmarkLocalFpgaMac=_WwpLeosBenchmarkLocalFpgaMac_Object((1,3,6,1,4,1,6141,2,60,43,1,1,6),_WwpLeosBenchmarkLocalFpgaMac_Type())
wwpLeosBenchmarkLocalFpgaMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkLocalFpgaMac.setStatus(_A)
_WwpLeosBenchmarkReflectorModule_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkReflectorModule=_WwpLeosBenchmarkReflectorModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,2))
_WwpLeosBenchmarkReflectorEnable_Type=TruthValue
_WwpLeosBenchmarkReflectorEnable_Object=MibScalar
wwpLeosBenchmarkReflectorEnable=_WwpLeosBenchmarkReflectorEnable_Object((1,3,6,1,4,1,6141,2,60,43,1,2,1),_WwpLeosBenchmarkReflectorEnable_Type())
wwpLeosBenchmarkReflectorEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkReflectorEnable.setStatus(_A)
class _WwpLeosBenchmarkReflectorVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_WwpLeosBenchmarkReflectorVid_Type.__name__=_C
_WwpLeosBenchmarkReflectorVid_Object=MibScalar
wwpLeosBenchmarkReflectorVid=_WwpLeosBenchmarkReflectorVid_Object((1,3,6,1,4,1,6141,2,60,43,1,2,2),_WwpLeosBenchmarkReflectorVid_Type())
wwpLeosBenchmarkReflectorVid.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkReflectorVid.setStatus(_A)
class _WwpLeosBenchmarkReflectorVendorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('ciena',2)))
_WwpLeosBenchmarkReflectorVendorType_Type.__name__=_C
_WwpLeosBenchmarkReflectorVendorType_Object=MibScalar
wwpLeosBenchmarkReflectorVendorType=_WwpLeosBenchmarkReflectorVendorType_Object((1,3,6,1,4,1,6141,2,60,43,1,2,3),_WwpLeosBenchmarkReflectorVendorType_Type())
wwpLeosBenchmarkReflectorVendorType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkReflectorVendorType.setStatus(_A)
_WwpLeosBenchmarkGeneratorModule_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkGeneratorModule=_WwpLeosBenchmarkGeneratorModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,3))
_WwpLeosBenchmarkGeneratorEnable_Type=TruthValue
_WwpLeosBenchmarkGeneratorEnable_Object=MibScalar
wwpLeosBenchmarkGeneratorEnable=_WwpLeosBenchmarkGeneratorEnable_Object((1,3,6,1,4,1,6141,2,60,43,1,3,1),_WwpLeosBenchmarkGeneratorEnable_Type())
wwpLeosBenchmarkGeneratorEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorEnable.setStatus(_A)
class _WwpLeosBenchmarkGeneratorprofileUnderTest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WwpLeosBenchmarkGeneratorprofileUnderTest_Type.__name__=_K
_WwpLeosBenchmarkGeneratorprofileUnderTest_Object=MibScalar
wwpLeosBenchmarkGeneratorprofileUnderTest=_WwpLeosBenchmarkGeneratorprofileUnderTest_Object((1,3,6,1,4,1,6141,2,60,43,1,3,2),_WwpLeosBenchmarkGeneratorprofileUnderTest_Type())
wwpLeosBenchmarkGeneratorprofileUnderTest.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorprofileUnderTest.setStatus(_A)
class _WwpLeosBenchmarkGeneratorThroughputTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),(_O,2),(_M,3),(_N,4),(_G,5),(_H,6),(_I,7),(_J,8)))
_WwpLeosBenchmarkGeneratorThroughputTestState_Type.__name__=_C
_WwpLeosBenchmarkGeneratorThroughputTestState_Object=MibScalar
wwpLeosBenchmarkGeneratorThroughputTestState=_WwpLeosBenchmarkGeneratorThroughputTestState_Object((1,3,6,1,4,1,6141,2,60,43,1,3,3),_WwpLeosBenchmarkGeneratorThroughputTestState_Type())
wwpLeosBenchmarkGeneratorThroughputTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorThroughputTestState.setStatus(_A)
class _WwpLeosBenchmarkGeneratorFramelossTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_F,1),('runningFirstTest',2),('waitingForResidualFirstPackets',3),('processingFirstResults',4),('runningSecondTest',5),('waitingForResidualSecondPackets',6),('processingSecondResults',7),(_G,8),(_H,9),(_I,10),(_J,11)))
_WwpLeosBenchmarkGeneratorFramelossTestState_Type.__name__=_C
_WwpLeosBenchmarkGeneratorFramelossTestState_Object=MibScalar
wwpLeosBenchmarkGeneratorFramelossTestState=_WwpLeosBenchmarkGeneratorFramelossTestState_Object((1,3,6,1,4,1,6141,2,60,43,1,3,4),_WwpLeosBenchmarkGeneratorFramelossTestState_Type())
wwpLeosBenchmarkGeneratorFramelossTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorFramelossTestState.setStatus(_A)
_WwpLeosBenchmarkGeneratorLatencyTestState_Type=BenchmarkLatencyPdvTestState
_WwpLeosBenchmarkGeneratorLatencyTestState_Object=MibScalar
wwpLeosBenchmarkGeneratorLatencyTestState=_WwpLeosBenchmarkGeneratorLatencyTestState_Object((1,3,6,1,4,1,6141,2,60,43,1,3,5),_WwpLeosBenchmarkGeneratorLatencyTestState_Type())
wwpLeosBenchmarkGeneratorLatencyTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorLatencyTestState.setStatus(_A)
_WwpLeosBenchmarkGeneratorPdvTestState_Type=BenchmarkLatencyPdvTestState
_WwpLeosBenchmarkGeneratorPdvTestState_Object=MibScalar
wwpLeosBenchmarkGeneratorPdvTestState=_WwpLeosBenchmarkGeneratorPdvTestState_Object((1,3,6,1,4,1,6141,2,60,43,1,3,6),_WwpLeosBenchmarkGeneratorPdvTestState_Type())
wwpLeosBenchmarkGeneratorPdvTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorPdvTestState.setStatus(_A)
class _WwpLeosBenchmarkGeneratorRfc2544State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),(_O,2),(_G,3),(_H,4),(_I,5),(_J,6)))
_WwpLeosBenchmarkGeneratorRfc2544State_Type.__name__=_C
_WwpLeosBenchmarkGeneratorRfc2544State_Object=MibScalar
wwpLeosBenchmarkGeneratorRfc2544State=_WwpLeosBenchmarkGeneratorRfc2544State_Object((1,3,6,1,4,1,6141,2,60,43,1,3,7),_WwpLeosBenchmarkGeneratorRfc2544State_Type())
wwpLeosBenchmarkGeneratorRfc2544State.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorRfc2544State.setStatus(_A)
_WwpLeosBenchmarkGeneratorCurrentPktSize_Type=Integer32
_WwpLeosBenchmarkGeneratorCurrentPktSize_Object=MibScalar
wwpLeosBenchmarkGeneratorCurrentPktSize=_WwpLeosBenchmarkGeneratorCurrentPktSize_Object((1,3,6,1,4,1,6141,2,60,43,1,3,8),_WwpLeosBenchmarkGeneratorCurrentPktSize_Type())
wwpLeosBenchmarkGeneratorCurrentPktSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorCurrentPktSize.setStatus(_A)
_WwpLeosBenchmarkGeneratorCurrentRate_Type=Integer32
_WwpLeosBenchmarkGeneratorCurrentRate_Object=MibScalar
wwpLeosBenchmarkGeneratorCurrentRate=_WwpLeosBenchmarkGeneratorCurrentRate_Object((1,3,6,1,4,1,6141,2,60,43,1,3,9),_WwpLeosBenchmarkGeneratorCurrentRate_Type())
wwpLeosBenchmarkGeneratorCurrentRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorCurrentRate.setStatus(_A)
_WwpLeosBenchmarkGeneratorSamplesCompleted_Type=Integer32
_WwpLeosBenchmarkGeneratorSamplesCompleted_Object=MibScalar
wwpLeosBenchmarkGeneratorSamplesCompleted=_WwpLeosBenchmarkGeneratorSamplesCompleted_Object((1,3,6,1,4,1,6141,2,60,43,1,3,10),_WwpLeosBenchmarkGeneratorSamplesCompleted_Type())
wwpLeosBenchmarkGeneratorSamplesCompleted.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorSamplesCompleted.setStatus(_A)
_WwpLeosBenchmarkGeneratorCurrentIteration_Type=Integer32
_WwpLeosBenchmarkGeneratorCurrentIteration_Object=MibScalar
wwpLeosBenchmarkGeneratorCurrentIteration=_WwpLeosBenchmarkGeneratorCurrentIteration_Object((1,3,6,1,4,1,6141,2,60,43,1,3,11),_WwpLeosBenchmarkGeneratorCurrentIteration_Type())
wwpLeosBenchmarkGeneratorCurrentIteration.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorCurrentIteration.setStatus(_A)
_WwpLeosBenchmarkGeneratorTotalIterations_Type=Integer32
_WwpLeosBenchmarkGeneratorTotalIterations_Object=MibScalar
wwpLeosBenchmarkGeneratorTotalIterations=_WwpLeosBenchmarkGeneratorTotalIterations_Object((1,3,6,1,4,1,6141,2,60,43,1,3,12),_WwpLeosBenchmarkGeneratorTotalIterations_Type())
wwpLeosBenchmarkGeneratorTotalIterations.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkGeneratorTotalIterations.setStatus(_A)
_WwpLeosBenchmarkFpgaStats_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkFpgaStats=_WwpLeosBenchmarkFpgaStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,4))
_WwpLeosBenchmarkFpgaStatsRxPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsRxPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsRxPkts=_WwpLeosBenchmarkFpgaStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,1),_WwpLeosBenchmarkFpgaStatsRxPkts_Type())
wwpLeosBenchmarkFpgaStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsRxPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsCrcPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsCrcPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsCrcPkts=_WwpLeosBenchmarkFpgaStatsCrcPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,2),_WwpLeosBenchmarkFpgaStatsCrcPkts_Type())
wwpLeosBenchmarkFpgaStatsCrcPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsCrcPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsUdpChecksumPkts=_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,3),_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Type())
wwpLeosBenchmarkFpgaStatsUdpChecksumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsUdpChecksumPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsDiscardPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsDiscardPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsDiscardPkts=_WwpLeosBenchmarkFpgaStatsDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,4),_WwpLeosBenchmarkFpgaStatsDiscardPkts_Type())
wwpLeosBenchmarkFpgaStatsDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsDiscardPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsDuplicatePkts=_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,5),_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Type())
wwpLeosBenchmarkFpgaStatsDuplicatePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsDuplicatePkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsOOSeqPkts=_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,6),_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Type())
wwpLeosBenchmarkFpgaStatsOOSeqPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsOOSeqPkts.setStatus('deprecated')
_WwpLeosBenchmarkFpgaStatsTxPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsTxPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsTxPkts=_WwpLeosBenchmarkFpgaStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,7),_WwpLeosBenchmarkFpgaStatsTxPkts_Type())
wwpLeosBenchmarkFpgaStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsTxPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsOOOPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsOOOPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsOOOPkts=_WwpLeosBenchmarkFpgaStatsOOOPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,8),_WwpLeosBenchmarkFpgaStatsOOOPkts_Type())
wwpLeosBenchmarkFpgaStatsOOOPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsOOOPkts.setStatus(_A)
_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Type=Counter64
_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Object=MibScalar
wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts=_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,4,9),_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Type())
wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts.setStatus(_A)
_WwpLeosBenchmarkPortStats_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkPortStats=_WwpLeosBenchmarkPortStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,5))
_WwpLeosBenchmarkPortStatsTxBytes_Type=Counter64
_WwpLeosBenchmarkPortStatsTxBytes_Object=MibScalar
wwpLeosBenchmarkPortStatsTxBytes=_WwpLeosBenchmarkPortStatsTxBytes_Object((1,3,6,1,4,1,6141,2,60,43,1,5,1),_WwpLeosBenchmarkPortStatsTxBytes_Type())
wwpLeosBenchmarkPortStatsTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxBytes.setStatus(_A)
_WwpLeosBenchmarkPortStatsTxPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTxPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTxPkts=_WwpLeosBenchmarkPortStatsTxPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,2),_WwpLeosBenchmarkPortStatsTxPkts_Type())
wwpLeosBenchmarkPortStatsTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsCrcErrorPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsCrcErrorPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsCrcErrorPkts=_WwpLeosBenchmarkPortStatsCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,3),_WwpLeosBenchmarkPortStatsCrcErrorPkts_Type())
wwpLeosBenchmarkPortStatsCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsCrcErrorPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsUcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsUcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsUcastPkts=_WwpLeosBenchmarkPortStatsUcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,4),_WwpLeosBenchmarkPortStatsUcastPkts_Type())
wwpLeosBenchmarkPortStatsUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsUcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsMcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsMcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsMcastPkts=_WwpLeosBenchmarkPortStatsMcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,5),_WwpLeosBenchmarkPortStatsMcastPkts_Type())
wwpLeosBenchmarkPortStatsMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsMcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsBcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsBcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsBcastPkts=_WwpLeosBenchmarkPortStatsBcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,6),_WwpLeosBenchmarkPortStatsBcastPkts_Type())
wwpLeosBenchmarkPortStatsBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsBcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsUndersizePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsUndersizePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsUndersizePkts=_WwpLeosBenchmarkPortStatsUndersizePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,7),_WwpLeosBenchmarkPortStatsUndersizePkts_Type())
wwpLeosBenchmarkPortStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsUndersizePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsOversizePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsOversizePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsOversizePkts=_WwpLeosBenchmarkPortStatsOversizePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,8),_WwpLeosBenchmarkPortStatsOversizePkts_Type())
wwpLeosBenchmarkPortStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsOversizePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsFragmentsPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsFragmentsPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsFragmentsPkts=_WwpLeosBenchmarkPortStatsFragmentsPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,9),_WwpLeosBenchmarkPortStatsFragmentsPkts_Type())
wwpLeosBenchmarkPortStatsFragmentsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsFragmentsPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsJabbersPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsJabbersPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsJabbersPkts=_WwpLeosBenchmarkPortStatsJabbersPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,10),_WwpLeosBenchmarkPortStatsJabbersPkts_Type())
wwpLeosBenchmarkPortStatsJabbersPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsJabbersPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTxPausePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTxPausePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTxPausePkts=_WwpLeosBenchmarkPortStatsTxPausePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,11),_WwpLeosBenchmarkPortStatsTxPausePkts_Type())
wwpLeosBenchmarkPortStatsTxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxPausePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTxDropPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTxDropPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTxDropPkts=_WwpLeosBenchmarkPortStatsTxDropPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,12),_WwpLeosBenchmarkPortStatsTxDropPkts_Type())
wwpLeosBenchmarkPortStatsTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxDropPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTxDiscardPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTxDiscardPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTxDiscardPkts=_WwpLeosBenchmarkPortStatsTxDiscardPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,13),_WwpLeosBenchmarkPortStatsTxDiscardPkts_Type())
wwpLeosBenchmarkPortStatsTxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxDiscardPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTxLOutRangePkts=_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,14),_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Type())
wwpLeosBenchmarkPortStatsTxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTxLOutRangePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx64OctsPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx64OctsPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx64OctsPkts=_WwpLeosBenchmarkPortStatsTx64OctsPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,15),_WwpLeosBenchmarkPortStatsTx64OctsPkts_Type())
wwpLeosBenchmarkPortStatsTx64OctsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx64OctsPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx65To127Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx65To127Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx65To127Pkts=_WwpLeosBenchmarkPortStatsTx65To127Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,16),_WwpLeosBenchmarkPortStatsTx65To127Pkts_Type())
wwpLeosBenchmarkPortStatsTx65To127Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx65To127Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx128To255Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx128To255Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx128To255Pkts=_WwpLeosBenchmarkPortStatsTx128To255Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,17),_WwpLeosBenchmarkPortStatsTx128To255Pkts_Type())
wwpLeosBenchmarkPortStatsTx128To255Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx128To255Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx256To511Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx256To511Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx256To511Pkts=_WwpLeosBenchmarkPortStatsTx256To511Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,18),_WwpLeosBenchmarkPortStatsTx256To511Pkts_Type())
wwpLeosBenchmarkPortStatsTx256To511Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx256To511Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx512To1023Pkts=_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,19),_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Type())
wwpLeosBenchmarkPortStatsTx512To1023Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx512To1023Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx1024To1518Pkts=_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,20),_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Type())
wwpLeosBenchmarkPortStatsTx1024To1518Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx1024To1518Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx1519To2047Pkts=_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,21),_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Type())
wwpLeosBenchmarkPortStatsTx1519To2047Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx1519To2047Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx2048To4095Pkts=_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,22),_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Type())
wwpLeosBenchmarkPortStatsTx2048To4095Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx2048To4095Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsTx4096To9216Pkts=_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,23),_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Type())
wwpLeosBenchmarkPortStatsTx4096To9216Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsTx4096To9216Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxBytes_Type=Counter64
_WwpLeosBenchmarkPortStatsRxBytes_Object=MibScalar
wwpLeosBenchmarkPortStatsRxBytes=_WwpLeosBenchmarkPortStatsRxBytes_Object((1,3,6,1,4,1,6141,2,60,43,1,5,24),_WwpLeosBenchmarkPortStatsRxBytes_Type())
wwpLeosBenchmarkPortStatsRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxBytes.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxPkts=_WwpLeosBenchmarkPortStatsRxPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,25),_WwpLeosBenchmarkPortStatsRxPkts_Type())
wwpLeosBenchmarkPortStatsRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxExDeferPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxExDeferPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxExDeferPkts=_WwpLeosBenchmarkPortStatsRxExDeferPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,26),_WwpLeosBenchmarkPortStatsRxExDeferPkts_Type())
wwpLeosBenchmarkPortStatsRxExDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxExDeferPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxDeferPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxDeferPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxDeferPkts=_WwpLeosBenchmarkPortStatsRxDeferPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,27),_WwpLeosBenchmarkPortStatsRxDeferPkts_Type())
wwpLeosBenchmarkPortStatsRxDeferPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxDeferPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxGiantPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxGiantPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxGiantPkts=_WwpLeosBenchmarkPortStatsRxGiantPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,28),_WwpLeosBenchmarkPortStatsRxGiantPkts_Type())
wwpLeosBenchmarkPortStatsRxGiantPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxGiantPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxUnderRunPkts=_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,29),_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Type())
wwpLeosBenchmarkPortStatsRxUnderRunPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxUnderRunPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxCrcErrorPkts=_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,30),_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Type())
wwpLeosBenchmarkPortStatsRxCrcErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxCrcErrorPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxLCheckErrorPkts=_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,31),_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Type())
wwpLeosBenchmarkPortStatsRxLCheckErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxLCheckErrorPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxLOutRangePkts=_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,32),_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Type())
wwpLeosBenchmarkPortStatsRxLOutRangePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxLOutRangePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxPausePkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxPausePkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxPausePkts=_WwpLeosBenchmarkPortStatsRxPausePkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,33),_WwpLeosBenchmarkPortStatsRxPausePkts_Type())
wwpLeosBenchmarkPortStatsRxPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxPausePkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxUcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxUcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxUcastPkts=_WwpLeosBenchmarkPortStatsRxUcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,34),_WwpLeosBenchmarkPortStatsRxUcastPkts_Type())
wwpLeosBenchmarkPortStatsRxUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxUcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxMcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxMcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxMcastPkts=_WwpLeosBenchmarkPortStatsRxMcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,35),_WwpLeosBenchmarkPortStatsRxMcastPkts_Type())
wwpLeosBenchmarkPortStatsRxMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxMcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRxBcastPkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRxBcastPkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRxBcastPkts=_WwpLeosBenchmarkPortStatsRxBcastPkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,36),_WwpLeosBenchmarkPortStatsRxBcastPkts_Type())
wwpLeosBenchmarkPortStatsRxBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRxBcastPkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx64Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx64Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx64Pkts=_WwpLeosBenchmarkPortStatsRx64Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,37),_WwpLeosBenchmarkPortStatsRx64Pkts_Type())
wwpLeosBenchmarkPortStatsRx64Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx64Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx65To127Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx65To127Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx65To127Pkts=_WwpLeosBenchmarkPortStatsRx65To127Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,38),_WwpLeosBenchmarkPortStatsRx65To127Pkts_Type())
wwpLeosBenchmarkPortStatsRx65To127Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx65To127Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx128To255Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx128To255Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx128To255Pkts=_WwpLeosBenchmarkPortStatsRx128To255Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,39),_WwpLeosBenchmarkPortStatsRx128To255Pkts_Type())
wwpLeosBenchmarkPortStatsRx128To255Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx128To255Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx256To511Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx256To511Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx256To511Pkts=_WwpLeosBenchmarkPortStatsRx256To511Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,40),_WwpLeosBenchmarkPortStatsRx256To511Pkts_Type())
wwpLeosBenchmarkPortStatsRx256To511Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx256To511Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx512To1023Pkts=_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,41),_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Type())
wwpLeosBenchmarkPortStatsRx512To1023Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx512To1023Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx1024To1518Pkts=_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,42),_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Type())
wwpLeosBenchmarkPortStatsRx1024To1518Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx1024To1518Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx1519To2047Pkts=_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,43),_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Type())
wwpLeosBenchmarkPortStatsRx1519To2047Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx1519To2047Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx2048To4095Pkts=_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,44),_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Type())
wwpLeosBenchmarkPortStatsRx2048To4095Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx2048To4095Pkts.setStatus(_A)
_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Type=Counter64
_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Object=MibScalar
wwpLeosBenchmarkPortStatsRx4096To9216Pkts=_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Object((1,3,6,1,4,1,6141,2,60,43,1,5,45),_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Type())
wwpLeosBenchmarkPortStatsRx4096To9216Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkPortStatsRx4096To9216Pkts.setStatus(_A)
_WwpLeosBenchmarkProfileObjects_ObjectIdentity=ObjectIdentity
wwpLeosBenchmarkProfileObjects=_WwpLeosBenchmarkProfileObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,43,1,6))
_WwpLeosBenchmarkProfileTable_Object=MibTable
wwpLeosBenchmarkProfileTable=_WwpLeosBenchmarkProfileTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileTable.setStatus(_A)
_WwpLeosBenchmarkProfileEntry_Object=MibTableRow
wwpLeosBenchmarkProfileEntry=_WwpLeosBenchmarkProfileEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1))
wwpLeosBenchmarkProfileEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntry.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_WwpLeosBenchmarkProfileEntryId_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryId_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryId=_WwpLeosBenchmarkProfileEntryId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,1),_WwpLeosBenchmarkProfileEntryId_Type())
wwpLeosBenchmarkProfileEntryId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryId.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_WwpLeosBenchmarkProfileEntryName_Type.__name__=_K
_WwpLeosBenchmarkProfileEntryName_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryName=_WwpLeosBenchmarkProfileEntryName_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,2),_WwpLeosBenchmarkProfileEntryName_Type())
wwpLeosBenchmarkProfileEntryName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryName.setStatus(_A)
_WwpLeosBenchmarkProfileEntryEnabled_Type=TruthValue
_WwpLeosBenchmarkProfileEntryEnabled_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryEnabled=_WwpLeosBenchmarkProfileEntryEnabled_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,3),_WwpLeosBenchmarkProfileEntryEnabled_Type())
wwpLeosBenchmarkProfileEntryEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryEnabled.setStatus(_A)
_WwpLeosBenchmarkProfileEntryStarted_Type=TruthValue
_WwpLeosBenchmarkProfileEntryStarted_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryStarted=_WwpLeosBenchmarkProfileEntryStarted_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,4),_WwpLeosBenchmarkProfileEntryStarted_Type())
wwpLeosBenchmarkProfileEntryStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryStarted.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),('t1hr',2),('t6hr',3),('tCompletion',4)))
_WwpLeosBenchmarkProfileEntryInterval_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryInterval_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryInterval=_WwpLeosBenchmarkProfileEntryInterval_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,5),_WwpLeosBenchmarkProfileEntryInterval_Type())
wwpLeosBenchmarkProfileEntryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryInterval.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),('t1hr',2),('t6hr',3),('t24hr',4),('tIndefinite',5),('tOnce',6)))
_WwpLeosBenchmarkProfileEntryDuration_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryDuration_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryDuration=_WwpLeosBenchmarkProfileEntryDuration_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,6),_WwpLeosBenchmarkProfileEntryDuration_Type())
wwpLeosBenchmarkProfileEntryDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryDuration.setStatus(_A)
_WwpLeosBenchmarkProfileEntryThroughputTest_Type=TruthValue
_WwpLeosBenchmarkProfileEntryThroughputTest_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryThroughputTest=_WwpLeosBenchmarkProfileEntryThroughputTest_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,7),_WwpLeosBenchmarkProfileEntryThroughputTest_Type())
wwpLeosBenchmarkProfileEntryThroughputTest.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryThroughputTest.setStatus(_A)
_WwpLeosBenchmarkProfileEntryFramelossTest_Type=TruthValue
_WwpLeosBenchmarkProfileEntryFramelossTest_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryFramelossTest=_WwpLeosBenchmarkProfileEntryFramelossTest_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,8),_WwpLeosBenchmarkProfileEntryFramelossTest_Type())
wwpLeosBenchmarkProfileEntryFramelossTest.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryFramelossTest.setStatus(_A)
_WwpLeosBenchmarkProfileEntryLatencyTest_Type=TruthValue
_WwpLeosBenchmarkProfileEntryLatencyTest_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryLatencyTest=_WwpLeosBenchmarkProfileEntryLatencyTest_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,9),_WwpLeosBenchmarkProfileEntryLatencyTest_Type())
wwpLeosBenchmarkProfileEntryLatencyTest.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryLatencyTest.setStatus(_A)
_WwpLeosBenchmarkProfileEntryPdvTest_Type=TruthValue
_WwpLeosBenchmarkProfileEntryPdvTest_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryPdvTest=_WwpLeosBenchmarkProfileEntryPdvTest_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,10),_WwpLeosBenchmarkProfileEntryPdvTest_Type())
wwpLeosBenchmarkProfileEntryPdvTest.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryPdvTest.setStatus(_A)
_WwpLeosBenchmarkProfileEntryRfc2544Suite_Type=TruthValue
_WwpLeosBenchmarkProfileEntryRfc2544Suite_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryRfc2544Suite=_WwpLeosBenchmarkProfileEntryRfc2544Suite_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,11),_WwpLeosBenchmarkProfileEntryRfc2544Suite_Type())
wwpLeosBenchmarkProfileEntryRfc2544Suite.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryRfc2544Suite.setStatus(_A)
_WwpLeosBenchmarkProfileEntryDstmac_Type=MacAddress
_WwpLeosBenchmarkProfileEntryDstmac_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryDstmac=_WwpLeosBenchmarkProfileEntryDstmac_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,12),_WwpLeosBenchmarkProfileEntryDstmac_Type())
wwpLeosBenchmarkProfileEntryDstmac.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryDstmac.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('untagged',1),('dot1q',2)))
_WwpLeosBenchmarkProfileEntryEncapType_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryEncapType_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryEncapType=_WwpLeosBenchmarkProfileEntryEncapType_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,13),_WwpLeosBenchmarkProfileEntryEncapType_Type())
wwpLeosBenchmarkProfileEntryEncapType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryEncapType.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBenchmarkProfileEntryVid_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryVid_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryVid=_WwpLeosBenchmarkProfileEntryVid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,14),_WwpLeosBenchmarkProfileEntryVid_Type())
wwpLeosBenchmarkProfileEntryVid.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryVid.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryPcp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosBenchmarkProfileEntryPcp_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryPcp_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryPcp=_WwpLeosBenchmarkProfileEntryPcp_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,15),_WwpLeosBenchmarkProfileEntryPcp_Type())
wwpLeosBenchmarkProfileEntryPcp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryPcp.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryCfi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_WwpLeosBenchmarkProfileEntryCfi_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryCfi_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryCfi=_WwpLeosBenchmarkProfileEntryCfi_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,16),_WwpLeosBenchmarkProfileEntryCfi_Type())
wwpLeosBenchmarkProfileEntryCfi.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryCfi.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryTpid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosBenchmarkProfileEntryTpid_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryTpid_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryTpid=_WwpLeosBenchmarkProfileEntryTpid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,17),_WwpLeosBenchmarkProfileEntryTpid_Type())
wwpLeosBenchmarkProfileEntryTpid.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryTpid.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryPduType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethernet',1),('ip',2),('udpecho',3)))
_WwpLeosBenchmarkProfileEntryPduType_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryPduType_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryPduType=_WwpLeosBenchmarkProfileEntryPduType_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,18),_WwpLeosBenchmarkProfileEntryPduType_Type())
wwpLeosBenchmarkProfileEntryPduType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryPduType.setStatus(_A)
_WwpLeosBenchmarkProfileEntrySrcIpAddr_Type=IpAddress
_WwpLeosBenchmarkProfileEntrySrcIpAddr_Object=MibTableColumn
wwpLeosBenchmarkProfileEntrySrcIpAddr=_WwpLeosBenchmarkProfileEntrySrcIpAddr_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,19),_WwpLeosBenchmarkProfileEntrySrcIpAddr_Type())
wwpLeosBenchmarkProfileEntrySrcIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntrySrcIpAddr.setStatus(_A)
_WwpLeosBenchmarkProfileEntryDstIpAddr_Type=IpAddress
_WwpLeosBenchmarkProfileEntryDstIpAddr_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryDstIpAddr=_WwpLeosBenchmarkProfileEntryDstIpAddr_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,20),_WwpLeosBenchmarkProfileEntryDstIpAddr_Type())
wwpLeosBenchmarkProfileEntryDstIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryDstIpAddr.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosBenchmarkProfileEntryDscp_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryDscp_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryDscp=_WwpLeosBenchmarkProfileEntryDscp_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,21),_WwpLeosBenchmarkProfileEntryDscp_Type())
wwpLeosBenchmarkProfileEntryDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryDscp.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryCustomPayload_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_WwpLeosBenchmarkProfileEntryCustomPayload_Type.__name__=_L
_WwpLeosBenchmarkProfileEntryCustomPayload_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryCustomPayload=_WwpLeosBenchmarkProfileEntryCustomPayload_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,22),_WwpLeosBenchmarkProfileEntryCustomPayload_Type())
wwpLeosBenchmarkProfileEntryCustomPayload.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryCustomPayload.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_WwpLeosBenchmarkProfileEntryBandwidth_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryBandwidth_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryBandwidth=_WwpLeosBenchmarkProfileEntryBandwidth_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,23),_WwpLeosBenchmarkProfileEntryBandwidth_Type())
wwpLeosBenchmarkProfileEntryBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryBandwidth.setStatus(_A)
_WwpLeosBenchmarkProfileEntryVidValidation_Type=TruthValue
_WwpLeosBenchmarkProfileEntryVidValidation_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryVidValidation=_WwpLeosBenchmarkProfileEntryVidValidation_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,24),_WwpLeosBenchmarkProfileEntryVidValidation_Type())
wwpLeosBenchmarkProfileEntryVidValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryVidValidation.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryMaxSearches_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_WwpLeosBenchmarkProfileEntryMaxSearches_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryMaxSearches_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryMaxSearches=_WwpLeosBenchmarkProfileEntryMaxSearches_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,25),_WwpLeosBenchmarkProfileEntryMaxSearches_Type())
wwpLeosBenchmarkProfileEntryMaxSearches.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryMaxSearches.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryMaxSamples_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,20))
_WwpLeosBenchmarkProfileEntryMaxSamples_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryMaxSamples_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryMaxSamples=_WwpLeosBenchmarkProfileEntryMaxSamples_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,26),_WwpLeosBenchmarkProfileEntryMaxSamples_Type())
wwpLeosBenchmarkProfileEntryMaxSamples.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryMaxSamples.setStatus(_A)
class _WwpLeosBenchmarkProfileEntrySamplingInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_WwpLeosBenchmarkProfileEntrySamplingInterval_Type.__name__=_C
_WwpLeosBenchmarkProfileEntrySamplingInterval_Object=MibTableColumn
wwpLeosBenchmarkProfileEntrySamplingInterval=_WwpLeosBenchmarkProfileEntrySamplingInterval_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,27),_WwpLeosBenchmarkProfileEntrySamplingInterval_Type())
wwpLeosBenchmarkProfileEntrySamplingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntrySamplingInterval.setStatus(_A)
class _WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('profileBandwidth',1),('maximumThroughput',2),('maximumLineRate',3)))
_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type.__name__=_C
_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Object=MibTableColumn
wwpLeosBenchmarkProfileEntryFrameLossStartBw=_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Object((1,3,6,1,4,1,6141,2,60,43,1,6,1,1,28),_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type())
wwpLeosBenchmarkProfileEntryFrameLossStartBw.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileEntryFrameLossStartBw.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatisticsTable_Object=MibTable
wwpLeosBenchmarkProfileThroughputStatisticsTable=_WwpLeosBenchmarkProfileThroughputStatisticsTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatisticsTable.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsEntry_Object=MibTableRow
wwpLeosBenchmarkProfileThroughputStatsEntry=_WwpLeosBenchmarkProfileThroughputStatsEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1))
wwpLeosBenchmarkProfileThroughputStatsEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsEntry.setStatus(_A)
class _WwpLeosBenchmarkProfileThroughputStatsProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WwpLeosBenchmarkProfileThroughputStatsProfileId_Type.__name__=_C
_WwpLeosBenchmarkProfileThroughputStatsProfileId_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsProfileId=_WwpLeosBenchmarkProfileThroughputStatsProfileId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,1),_WwpLeosBenchmarkProfileThroughputStatsProfileId_Type())
wwpLeosBenchmarkProfileThroughputStatsProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsProfileId.setStatus(_A)
class _WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type.__name__=_C
_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex=_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,2),_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type())
wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Type=Integer32
_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsFrameSize=_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,3),_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Type())
wwpLeosBenchmarkProfileThroughputStatsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsFrameSize.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsMin_Type=Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsMin_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsMin=_WwpLeosBenchmarkProfileThroughputStatsMin_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,4),_WwpLeosBenchmarkProfileThroughputStatsMin_Type())
wwpLeosBenchmarkProfileThroughputStatsMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsMin.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsMax_Type=Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsMax_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsMax=_WwpLeosBenchmarkProfileThroughputStatsMax_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,5),_WwpLeosBenchmarkProfileThroughputStatsMax_Type())
wwpLeosBenchmarkProfileThroughputStatsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsMax.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsAvg_Type=Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsAvg_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsAvg=_WwpLeosBenchmarkProfileThroughputStatsAvg_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,6),_WwpLeosBenchmarkProfileThroughputStatsAvg_Type())
wwpLeosBenchmarkProfileThroughputStatsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsAvg.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsIterations_Type=Integer32
_WwpLeosBenchmarkProfileThroughputStatsIterations_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsIterations=_WwpLeosBenchmarkProfileThroughputStatsIterations_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,7),_WwpLeosBenchmarkProfileThroughputStatsIterations_Type())
wwpLeosBenchmarkProfileThroughputStatsIterations.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsIterations.setStatus(_A)
class _WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type.__name__=_C
_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsActiveVid=_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,8),_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type())
wwpLeosBenchmarkProfileThroughputStatsActiveVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsActiveVid.setStatus(_A)
_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Type=MacAddress
_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Object=MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsActiveDstMac=_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Object((1,3,6,1,4,1,6141,2,60,43,1,6,2,1,9),_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Type())
wwpLeosBenchmarkProfileThroughputStatsActiveDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileThroughputStatsActiveDstMac.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatisticsTable_Object=MibTable
wwpLeosBenchmarkProfileFramelossStatisticsTable=_WwpLeosBenchmarkProfileFramelossStatisticsTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatisticsTable.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsEntry_Object=MibTableRow
wwpLeosBenchmarkProfileFramelossStatsEntry=_WwpLeosBenchmarkProfileFramelossStatsEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1))
wwpLeosBenchmarkProfileFramelossStatsEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsEntry.setStatus(_A)
class _WwpLeosBenchmarkProfileFramelossStatsProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WwpLeosBenchmarkProfileFramelossStatsProfileId_Type.__name__=_C
_WwpLeosBenchmarkProfileFramelossStatsProfileId_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsProfileId=_WwpLeosBenchmarkProfileFramelossStatsProfileId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,1),_WwpLeosBenchmarkProfileFramelossStatsProfileId_Type())
wwpLeosBenchmarkProfileFramelossStatsProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsProfileId.setStatus(_A)
class _WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type.__name__=_C
_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex=_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,2),_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type())
wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex.setStatus(_A)
class _WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type.__name__=_C
_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsRateIndex=_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,3),_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type())
wwpLeosBenchmarkProfileFramelossStatsRateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsRateIndex.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Type=Integer32
_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFrameSize=_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,4),_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Type())
wwpLeosBenchmarkProfileFramelossStatsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsFrameSize.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsRate_Type=Integer32
_WwpLeosBenchmarkProfileFramelossStatsRate_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsRate=_WwpLeosBenchmarkProfileFramelossStatsRate_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,5),_WwpLeosBenchmarkProfileFramelossStatsRate_Type())
wwpLeosBenchmarkProfileFramelossStatsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsRate.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsFirst_Type=Unsigned32
_WwpLeosBenchmarkProfileFramelossStatsFirst_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFirst=_WwpLeosBenchmarkProfileFramelossStatsFirst_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,6),_WwpLeosBenchmarkProfileFramelossStatsFirst_Type())
wwpLeosBenchmarkProfileFramelossStatsFirst.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsFirst.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsSecond_Type=Unsigned32
_WwpLeosBenchmarkProfileFramelossStatsSecond_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsSecond=_WwpLeosBenchmarkProfileFramelossStatsSecond_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,7),_WwpLeosBenchmarkProfileFramelossStatsSecond_Type())
wwpLeosBenchmarkProfileFramelossStatsSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsSecond.setStatus(_A)
class _WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type.__name__=_C
_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsActiveVid=_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,8),_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type())
wwpLeosBenchmarkProfileFramelossStatsActiveVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsActiveVid.setStatus(_A)
_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Type=MacAddress
_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Object=MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsActiveDstMac=_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Object((1,3,6,1,4,1,6141,2,60,43,1,6,3,1,9),_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Type())
wwpLeosBenchmarkProfileFramelossStatsActiveDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFramelossStatsActiveDstMac.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatisticsTable_Object=MibTable
wwpLeosBenchmarkProfileLatencyStatisticsTable=_WwpLeosBenchmarkProfileLatencyStatisticsTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatisticsTable.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsEntry_Object=MibTableRow
wwpLeosBenchmarkProfileLatencyStatsEntry=_WwpLeosBenchmarkProfileLatencyStatsEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1))
wwpLeosBenchmarkProfileLatencyStatsEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsEntry.setStatus(_A)
class _WwpLeosBenchmarkProfileLatencyStatsProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WwpLeosBenchmarkProfileLatencyStatsProfileId_Type.__name__=_C
_WwpLeosBenchmarkProfileLatencyStatsProfileId_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsProfileId=_WwpLeosBenchmarkProfileLatencyStatsProfileId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,1),_WwpLeosBenchmarkProfileLatencyStatsProfileId_Type())
wwpLeosBenchmarkProfileLatencyStatsProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsProfileId.setStatus(_A)
class _WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type.__name__=_C
_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex=_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,2),_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type())
wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Type=Integer32
_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsFrameSize=_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,3),_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Type())
wwpLeosBenchmarkProfileLatencyStatsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsFrameSize.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsMin_Type=Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsMin_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsMin=_WwpLeosBenchmarkProfileLatencyStatsMin_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,4),_WwpLeosBenchmarkProfileLatencyStatsMin_Type())
wwpLeosBenchmarkProfileLatencyStatsMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsMin.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsMax_Type=Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsMax_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsMax=_WwpLeosBenchmarkProfileLatencyStatsMax_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,5),_WwpLeosBenchmarkProfileLatencyStatsMax_Type())
wwpLeosBenchmarkProfileLatencyStatsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsMax.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsAvg_Type=Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsAvg_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsAvg=_WwpLeosBenchmarkProfileLatencyStatsAvg_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,6),_WwpLeosBenchmarkProfileLatencyStatsAvg_Type())
wwpLeosBenchmarkProfileLatencyStatsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsAvg.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsSamples_Type=Integer32
_WwpLeosBenchmarkProfileLatencyStatsSamples_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsSamples=_WwpLeosBenchmarkProfileLatencyStatsSamples_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,7),_WwpLeosBenchmarkProfileLatencyStatsSamples_Type())
wwpLeosBenchmarkProfileLatencyStatsSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsSamples.setStatus(_A)
class _WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type.__name__=_C
_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsActiveVid=_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,8),_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type())
wwpLeosBenchmarkProfileLatencyStatsActiveVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsActiveVid.setStatus(_A)
_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Type=MacAddress
_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Object=MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsActiveDstMac=_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Object((1,3,6,1,4,1,6141,2,60,43,1,6,4,1,9),_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Type())
wwpLeosBenchmarkProfileLatencyStatsActiveDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileLatencyStatsActiveDstMac.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatisticsTable_Object=MibTable
wwpLeosBenchmarkProfilePdvStatisticsTable=_WwpLeosBenchmarkProfilePdvStatisticsTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatisticsTable.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatsEntry_Object=MibTableRow
wwpLeosBenchmarkProfilePdvStatsEntry=_WwpLeosBenchmarkProfilePdvStatsEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1))
wwpLeosBenchmarkProfilePdvStatsEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsEntry.setStatus(_A)
class _WwpLeosBenchmarkProfilePdvStatsProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WwpLeosBenchmarkProfilePdvStatsProfileId_Type.__name__=_C
_WwpLeosBenchmarkProfilePdvStatsProfileId_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsProfileId=_WwpLeosBenchmarkProfilePdvStatsProfileId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,1),_WwpLeosBenchmarkProfilePdvStatsProfileId_Type())
wwpLeosBenchmarkProfilePdvStatsProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsProfileId.setStatus(_A)
class _WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type.__name__=_C
_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex=_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,2),_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type())
wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatsFrameSize_Type=Integer32
_WwpLeosBenchmarkProfilePdvStatsFrameSize_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsFrameSize=_WwpLeosBenchmarkProfilePdvStatsFrameSize_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,3),_WwpLeosBenchmarkProfilePdvStatsFrameSize_Type())
wwpLeosBenchmarkProfilePdvStatsFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsFrameSize.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatsAvg_Type=Unsigned32
_WwpLeosBenchmarkProfilePdvStatsAvg_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsAvg=_WwpLeosBenchmarkProfilePdvStatsAvg_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,4),_WwpLeosBenchmarkProfilePdvStatsAvg_Type())
wwpLeosBenchmarkProfilePdvStatsAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsAvg.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatsSamples_Type=Integer32
_WwpLeosBenchmarkProfilePdvStatsSamples_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsSamples=_WwpLeosBenchmarkProfilePdvStatsSamples_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,5),_WwpLeosBenchmarkProfilePdvStatsSamples_Type())
wwpLeosBenchmarkProfilePdvStatsSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsSamples.setStatus(_A)
class _WwpLeosBenchmarkProfilePdvStatsActiveVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_WwpLeosBenchmarkProfilePdvStatsActiveVid_Type.__name__=_C
_WwpLeosBenchmarkProfilePdvStatsActiveVid_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsActiveVid=_WwpLeosBenchmarkProfilePdvStatsActiveVid_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,6),_WwpLeosBenchmarkProfilePdvStatsActiveVid_Type())
wwpLeosBenchmarkProfilePdvStatsActiveVid.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsActiveVid.setStatus(_A)
_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Type=MacAddress
_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Object=MibTableColumn
wwpLeosBenchmarkProfilePdvStatsActiveDstMac=_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Object((1,3,6,1,4,1,6141,2,60,43,1,6,5,1,7),_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Type())
wwpLeosBenchmarkProfilePdvStatsActiveDstMac.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfilePdvStatsActiveDstMac.setStatus(_A)
_WwpLeosBenchmarkProfileFrameSizeTable_Object=MibTable
wwpLeosBenchmarkProfileFrameSizeTable=_WwpLeosBenchmarkProfileFrameSizeTable_Object((1,3,6,1,4,1,6141,2,60,43,1,6,6))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFrameSizeTable.setStatus(_A)
_WwpLeosBenchmarkProfileFrameSizeEntry_Object=MibTableRow
wwpLeosBenchmarkProfileFrameSizeEntry=_WwpLeosBenchmarkProfileFrameSizeEntry_Object((1,3,6,1,4,1,6141,2,60,43,1,6,6,1))
wwpLeosBenchmarkProfileFrameSizeEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFrameSizeEntry.setStatus(_A)
class _WwpLeosBenchmarkProfileFrameSizeProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_WwpLeosBenchmarkProfileFrameSizeProfileId_Type.__name__=_C
_WwpLeosBenchmarkProfileFrameSizeProfileId_Object=MibTableColumn
wwpLeosBenchmarkProfileFrameSizeProfileId=_WwpLeosBenchmarkProfileFrameSizeProfileId_Object((1,3,6,1,4,1,6141,2,60,43,1,6,6,1,1),_WwpLeosBenchmarkProfileFrameSizeProfileId_Type())
wwpLeosBenchmarkProfileFrameSizeProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFrameSizeProfileId.setStatus(_A)
class _WwpLeosBenchmarkProfileFrameSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_WwpLeosBenchmarkProfileFrameSizeIndex_Type.__name__=_C
_WwpLeosBenchmarkProfileFrameSizeIndex_Object=MibTableColumn
wwpLeosBenchmarkProfileFrameSizeIndex=_WwpLeosBenchmarkProfileFrameSizeIndex_Object((1,3,6,1,4,1,6141,2,60,43,1,6,6,1,2),_WwpLeosBenchmarkProfileFrameSizeIndex_Type())
wwpLeosBenchmarkProfileFrameSizeIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFrameSizeIndex.setStatus(_A)
_WwpLeosBenchmarkProfileFrameSize_Type=Integer32
_WwpLeosBenchmarkProfileFrameSize_Object=MibTableColumn
wwpLeosBenchmarkProfileFrameSize=_WwpLeosBenchmarkProfileFrameSize_Object((1,3,6,1,4,1,6141,2,60,43,1,6,6,1,3),_WwpLeosBenchmarkProfileFrameSize_Type())
wwpLeosBenchmarkProfileFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosBenchmarkProfileFrameSize.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'BenchmarkLatencyPdvTestState':BenchmarkLatencyPdvTestState,'wwpLeosBenchmarkMIB':wwpLeosBenchmarkMIB,'wwpLeosBenchmarkMIBObjects':wwpLeosBenchmarkMIBObjects,'wwpLeosBenchmarkModule':wwpLeosBenchmarkModule,'wwpLeosBenchmarkRole':wwpLeosBenchmarkRole,'wwpLeosBenchmarkPort':wwpLeosBenchmarkPort,'wwpLeosBenchmarkMode':wwpLeosBenchmarkMode,'wwpLeosBenchmarkEnable':wwpLeosBenchmarkEnable,'wwpLeosBenchmarkOperEnable':wwpLeosBenchmarkOperEnable,'wwpLeosBenchmarkLocalFpgaMac':wwpLeosBenchmarkLocalFpgaMac,'wwpLeosBenchmarkReflectorModule':wwpLeosBenchmarkReflectorModule,'wwpLeosBenchmarkReflectorEnable':wwpLeosBenchmarkReflectorEnable,'wwpLeosBenchmarkReflectorVid':wwpLeosBenchmarkReflectorVid,'wwpLeosBenchmarkReflectorVendorType':wwpLeosBenchmarkReflectorVendorType,'wwpLeosBenchmarkGeneratorModule':wwpLeosBenchmarkGeneratorModule,'wwpLeosBenchmarkGeneratorEnable':wwpLeosBenchmarkGeneratorEnable,'wwpLeosBenchmarkGeneratorprofileUnderTest':wwpLeosBenchmarkGeneratorprofileUnderTest,'wwpLeosBenchmarkGeneratorThroughputTestState':wwpLeosBenchmarkGeneratorThroughputTestState,'wwpLeosBenchmarkGeneratorFramelossTestState':wwpLeosBenchmarkGeneratorFramelossTestState,'wwpLeosBenchmarkGeneratorLatencyTestState':wwpLeosBenchmarkGeneratorLatencyTestState,'wwpLeosBenchmarkGeneratorPdvTestState':wwpLeosBenchmarkGeneratorPdvTestState,'wwpLeosBenchmarkGeneratorRfc2544State':wwpLeosBenchmarkGeneratorRfc2544State,'wwpLeosBenchmarkGeneratorCurrentPktSize':wwpLeosBenchmarkGeneratorCurrentPktSize,'wwpLeosBenchmarkGeneratorCurrentRate':wwpLeosBenchmarkGeneratorCurrentRate,'wwpLeosBenchmarkGeneratorSamplesCompleted':wwpLeosBenchmarkGeneratorSamplesCompleted,'wwpLeosBenchmarkGeneratorCurrentIteration':wwpLeosBenchmarkGeneratorCurrentIteration,'wwpLeosBenchmarkGeneratorTotalIterations':wwpLeosBenchmarkGeneratorTotalIterations,'wwpLeosBenchmarkFpgaStats':wwpLeosBenchmarkFpgaStats,'wwpLeosBenchmarkFpgaStatsRxPkts':wwpLeosBenchmarkFpgaStatsRxPkts,'wwpLeosBenchmarkFpgaStatsCrcPkts':wwpLeosBenchmarkFpgaStatsCrcPkts,'wwpLeosBenchmarkFpgaStatsUdpChecksumPkts':wwpLeosBenchmarkFpgaStatsUdpChecksumPkts,'wwpLeosBenchmarkFpgaStatsDiscardPkts':wwpLeosBenchmarkFpgaStatsDiscardPkts,'wwpLeosBenchmarkFpgaStatsDuplicatePkts':wwpLeosBenchmarkFpgaStatsDuplicatePkts,'wwpLeosBenchmarkFpgaStatsOOSeqPkts':wwpLeosBenchmarkFpgaStatsOOSeqPkts,'wwpLeosBenchmarkFpgaStatsTxPkts':wwpLeosBenchmarkFpgaStatsTxPkts,'wwpLeosBenchmarkFpgaStatsOOOPkts':wwpLeosBenchmarkFpgaStatsOOOPkts,'wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts':wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts,'wwpLeosBenchmarkPortStats':wwpLeosBenchmarkPortStats,'wwpLeosBenchmarkPortStatsTxBytes':wwpLeosBenchmarkPortStatsTxBytes,'wwpLeosBenchmarkPortStatsTxPkts':wwpLeosBenchmarkPortStatsTxPkts,'wwpLeosBenchmarkPortStatsCrcErrorPkts':wwpLeosBenchmarkPortStatsCrcErrorPkts,'wwpLeosBenchmarkPortStatsUcastPkts':wwpLeosBenchmarkPortStatsUcastPkts,'wwpLeosBenchmarkPortStatsMcastPkts':wwpLeosBenchmarkPortStatsMcastPkts,'wwpLeosBenchmarkPortStatsBcastPkts':wwpLeosBenchmarkPortStatsBcastPkts,'wwpLeosBenchmarkPortStatsUndersizePkts':wwpLeosBenchmarkPortStatsUndersizePkts,'wwpLeosBenchmarkPortStatsOversizePkts':wwpLeosBenchmarkPortStatsOversizePkts,'wwpLeosBenchmarkPortStatsFragmentsPkts':wwpLeosBenchmarkPortStatsFragmentsPkts,'wwpLeosBenchmarkPortStatsJabbersPkts':wwpLeosBenchmarkPortStatsJabbersPkts,'wwpLeosBenchmarkPortStatsTxPausePkts':wwpLeosBenchmarkPortStatsTxPausePkts,'wwpLeosBenchmarkPortStatsTxDropPkts':wwpLeosBenchmarkPortStatsTxDropPkts,'wwpLeosBenchmarkPortStatsTxDiscardPkts':wwpLeosBenchmarkPortStatsTxDiscardPkts,'wwpLeosBenchmarkPortStatsTxLOutRangePkts':wwpLeosBenchmarkPortStatsTxLOutRangePkts,'wwpLeosBenchmarkPortStatsTx64OctsPkts':wwpLeosBenchmarkPortStatsTx64OctsPkts,'wwpLeosBenchmarkPortStatsTx65To127Pkts':wwpLeosBenchmarkPortStatsTx65To127Pkts,'wwpLeosBenchmarkPortStatsTx128To255Pkts':wwpLeosBenchmarkPortStatsTx128To255Pkts,'wwpLeosBenchmarkPortStatsTx256To511Pkts':wwpLeosBenchmarkPortStatsTx256To511Pkts,'wwpLeosBenchmarkPortStatsTx512To1023Pkts':wwpLeosBenchmarkPortStatsTx512To1023Pkts,'wwpLeosBenchmarkPortStatsTx1024To1518Pkts':wwpLeosBenchmarkPortStatsTx1024To1518Pkts,'wwpLeosBenchmarkPortStatsTx1519To2047Pkts':wwpLeosBenchmarkPortStatsTx1519To2047Pkts,'wwpLeosBenchmarkPortStatsTx2048To4095Pkts':wwpLeosBenchmarkPortStatsTx2048To4095Pkts,'wwpLeosBenchmarkPortStatsTx4096To9216Pkts':wwpLeosBenchmarkPortStatsTx4096To9216Pkts,'wwpLeosBenchmarkPortStatsRxBytes':wwpLeosBenchmarkPortStatsRxBytes,'wwpLeosBenchmarkPortStatsRxPkts':wwpLeosBenchmarkPortStatsRxPkts,'wwpLeosBenchmarkPortStatsRxExDeferPkts':wwpLeosBenchmarkPortStatsRxExDeferPkts,'wwpLeosBenchmarkPortStatsRxDeferPkts':wwpLeosBenchmarkPortStatsRxDeferPkts,'wwpLeosBenchmarkPortStatsRxGiantPkts':wwpLeosBenchmarkPortStatsRxGiantPkts,'wwpLeosBenchmarkPortStatsRxUnderRunPkts':wwpLeosBenchmarkPortStatsRxUnderRunPkts,'wwpLeosBenchmarkPortStatsRxCrcErrorPkts':wwpLeosBenchmarkPortStatsRxCrcErrorPkts,'wwpLeosBenchmarkPortStatsRxLCheckErrorPkts':wwpLeosBenchmarkPortStatsRxLCheckErrorPkts,'wwpLeosBenchmarkPortStatsRxLOutRangePkts':wwpLeosBenchmarkPortStatsRxLOutRangePkts,'wwpLeosBenchmarkPortStatsRxPausePkts':wwpLeosBenchmarkPortStatsRxPausePkts,'wwpLeosBenchmarkPortStatsRxUcastPkts':wwpLeosBenchmarkPortStatsRxUcastPkts,'wwpLeosBenchmarkPortStatsRxMcastPkts':wwpLeosBenchmarkPortStatsRxMcastPkts,'wwpLeosBenchmarkPortStatsRxBcastPkts':wwpLeosBenchmarkPortStatsRxBcastPkts,'wwpLeosBenchmarkPortStatsRx64Pkts':wwpLeosBenchmarkPortStatsRx64Pkts,'wwpLeosBenchmarkPortStatsRx65To127Pkts':wwpLeosBenchmarkPortStatsRx65To127Pkts,'wwpLeosBenchmarkPortStatsRx128To255Pkts':wwpLeosBenchmarkPortStatsRx128To255Pkts,'wwpLeosBenchmarkPortStatsRx256To511Pkts':wwpLeosBenchmarkPortStatsRx256To511Pkts,'wwpLeosBenchmarkPortStatsRx512To1023Pkts':wwpLeosBenchmarkPortStatsRx512To1023Pkts,'wwpLeosBenchmarkPortStatsRx1024To1518Pkts':wwpLeosBenchmarkPortStatsRx1024To1518Pkts,'wwpLeosBenchmarkPortStatsRx1519To2047Pkts':wwpLeosBenchmarkPortStatsRx1519To2047Pkts,'wwpLeosBenchmarkPortStatsRx2048To4095Pkts':wwpLeosBenchmarkPortStatsRx2048To4095Pkts,'wwpLeosBenchmarkPortStatsRx4096To9216Pkts':wwpLeosBenchmarkPortStatsRx4096To9216Pkts,'wwpLeosBenchmarkProfileObjects':wwpLeosBenchmarkProfileObjects,'wwpLeosBenchmarkProfileTable':wwpLeosBenchmarkProfileTable,'wwpLeosBenchmarkProfileEntry':wwpLeosBenchmarkProfileEntry,_P:wwpLeosBenchmarkProfileEntryId,'wwpLeosBenchmarkProfileEntryName':wwpLeosBenchmarkProfileEntryName,'wwpLeosBenchmarkProfileEntryEnabled':wwpLeosBenchmarkProfileEntryEnabled,'wwpLeosBenchmarkProfileEntryStarted':wwpLeosBenchmarkProfileEntryStarted,'wwpLeosBenchmarkProfileEntryInterval':wwpLeosBenchmarkProfileEntryInterval,'wwpLeosBenchmarkProfileEntryDuration':wwpLeosBenchmarkProfileEntryDuration,'wwpLeosBenchmarkProfileEntryThroughputTest':wwpLeosBenchmarkProfileEntryThroughputTest,'wwpLeosBenchmarkProfileEntryFramelossTest':wwpLeosBenchmarkProfileEntryFramelossTest,'wwpLeosBenchmarkProfileEntryLatencyTest':wwpLeosBenchmarkProfileEntryLatencyTest,'wwpLeosBenchmarkProfileEntryPdvTest':wwpLeosBenchmarkProfileEntryPdvTest,'wwpLeosBenchmarkProfileEntryRfc2544Suite':wwpLeosBenchmarkProfileEntryRfc2544Suite,'wwpLeosBenchmarkProfileEntryDstmac':wwpLeosBenchmarkProfileEntryDstmac,'wwpLeosBenchmarkProfileEntryEncapType':wwpLeosBenchmarkProfileEntryEncapType,'wwpLeosBenchmarkProfileEntryVid':wwpLeosBenchmarkProfileEntryVid,'wwpLeosBenchmarkProfileEntryPcp':wwpLeosBenchmarkProfileEntryPcp,'wwpLeosBenchmarkProfileEntryCfi':wwpLeosBenchmarkProfileEntryCfi,'wwpLeosBenchmarkProfileEntryTpid':wwpLeosBenchmarkProfileEntryTpid,'wwpLeosBenchmarkProfileEntryPduType':wwpLeosBenchmarkProfileEntryPduType,'wwpLeosBenchmarkProfileEntrySrcIpAddr':wwpLeosBenchmarkProfileEntrySrcIpAddr,'wwpLeosBenchmarkProfileEntryDstIpAddr':wwpLeosBenchmarkProfileEntryDstIpAddr,'wwpLeosBenchmarkProfileEntryDscp':wwpLeosBenchmarkProfileEntryDscp,'wwpLeosBenchmarkProfileEntryCustomPayload':wwpLeosBenchmarkProfileEntryCustomPayload,'wwpLeosBenchmarkProfileEntryBandwidth':wwpLeosBenchmarkProfileEntryBandwidth,'wwpLeosBenchmarkProfileEntryVidValidation':wwpLeosBenchmarkProfileEntryVidValidation,'wwpLeosBenchmarkProfileEntryMaxSearches':wwpLeosBenchmarkProfileEntryMaxSearches,'wwpLeosBenchmarkProfileEntryMaxSamples':wwpLeosBenchmarkProfileEntryMaxSamples,'wwpLeosBenchmarkProfileEntrySamplingInterval':wwpLeosBenchmarkProfileEntrySamplingInterval,'wwpLeosBenchmarkProfileEntryFrameLossStartBw':wwpLeosBenchmarkProfileEntryFrameLossStartBw,'wwpLeosBenchmarkProfileThroughputStatisticsTable':wwpLeosBenchmarkProfileThroughputStatisticsTable,'wwpLeosBenchmarkProfileThroughputStatsEntry':wwpLeosBenchmarkProfileThroughputStatsEntry,_R:wwpLeosBenchmarkProfileThroughputStatsProfileId,_S:wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex,'wwpLeosBenchmarkProfileThroughputStatsFrameSize':wwpLeosBenchmarkProfileThroughputStatsFrameSize,'wwpLeosBenchmarkProfileThroughputStatsMin':wwpLeosBenchmarkProfileThroughputStatsMin,'wwpLeosBenchmarkProfileThroughputStatsMax':wwpLeosBenchmarkProfileThroughputStatsMax,'wwpLeosBenchmarkProfileThroughputStatsAvg':wwpLeosBenchmarkProfileThroughputStatsAvg,'wwpLeosBenchmarkProfileThroughputStatsIterations':wwpLeosBenchmarkProfileThroughputStatsIterations,'wwpLeosBenchmarkProfileThroughputStatsActiveVid':wwpLeosBenchmarkProfileThroughputStatsActiveVid,'wwpLeosBenchmarkProfileThroughputStatsActiveDstMac':wwpLeosBenchmarkProfileThroughputStatsActiveDstMac,'wwpLeosBenchmarkProfileFramelossStatisticsTable':wwpLeosBenchmarkProfileFramelossStatisticsTable,'wwpLeosBenchmarkProfileFramelossStatsEntry':wwpLeosBenchmarkProfileFramelossStatsEntry,_T:wwpLeosBenchmarkProfileFramelossStatsProfileId,_U:wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex,_V:wwpLeosBenchmarkProfileFramelossStatsRateIndex,'wwpLeosBenchmarkProfileFramelossStatsFrameSize':wwpLeosBenchmarkProfileFramelossStatsFrameSize,'wwpLeosBenchmarkProfileFramelossStatsRate':wwpLeosBenchmarkProfileFramelossStatsRate,'wwpLeosBenchmarkProfileFramelossStatsFirst':wwpLeosBenchmarkProfileFramelossStatsFirst,'wwpLeosBenchmarkProfileFramelossStatsSecond':wwpLeosBenchmarkProfileFramelossStatsSecond,'wwpLeosBenchmarkProfileFramelossStatsActiveVid':wwpLeosBenchmarkProfileFramelossStatsActiveVid,'wwpLeosBenchmarkProfileFramelossStatsActiveDstMac':wwpLeosBenchmarkProfileFramelossStatsActiveDstMac,'wwpLeosBenchmarkProfileLatencyStatisticsTable':wwpLeosBenchmarkProfileLatencyStatisticsTable,'wwpLeosBenchmarkProfileLatencyStatsEntry':wwpLeosBenchmarkProfileLatencyStatsEntry,_W:wwpLeosBenchmarkProfileLatencyStatsProfileId,_X:wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex,'wwpLeosBenchmarkProfileLatencyStatsFrameSize':wwpLeosBenchmarkProfileLatencyStatsFrameSize,'wwpLeosBenchmarkProfileLatencyStatsMin':wwpLeosBenchmarkProfileLatencyStatsMin,'wwpLeosBenchmarkProfileLatencyStatsMax':wwpLeosBenchmarkProfileLatencyStatsMax,'wwpLeosBenchmarkProfileLatencyStatsAvg':wwpLeosBenchmarkProfileLatencyStatsAvg,'wwpLeosBenchmarkProfileLatencyStatsSamples':wwpLeosBenchmarkProfileLatencyStatsSamples,'wwpLeosBenchmarkProfileLatencyStatsActiveVid':wwpLeosBenchmarkProfileLatencyStatsActiveVid,'wwpLeosBenchmarkProfileLatencyStatsActiveDstMac':wwpLeosBenchmarkProfileLatencyStatsActiveDstMac,'wwpLeosBenchmarkProfilePdvStatisticsTable':wwpLeosBenchmarkProfilePdvStatisticsTable,'wwpLeosBenchmarkProfilePdvStatsEntry':wwpLeosBenchmarkProfilePdvStatsEntry,_Y:wwpLeosBenchmarkProfilePdvStatsProfileId,_Z:wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex,'wwpLeosBenchmarkProfilePdvStatsFrameSize':wwpLeosBenchmarkProfilePdvStatsFrameSize,'wwpLeosBenchmarkProfilePdvStatsAvg':wwpLeosBenchmarkProfilePdvStatsAvg,'wwpLeosBenchmarkProfilePdvStatsSamples':wwpLeosBenchmarkProfilePdvStatsSamples,'wwpLeosBenchmarkProfilePdvStatsActiveVid':wwpLeosBenchmarkProfilePdvStatsActiveVid,'wwpLeosBenchmarkProfilePdvStatsActiveDstMac':wwpLeosBenchmarkProfilePdvStatsActiveDstMac,'wwpLeosBenchmarkProfileFrameSizeTable':wwpLeosBenchmarkProfileFrameSizeTable,'wwpLeosBenchmarkProfileFrameSizeEntry':wwpLeosBenchmarkProfileFrameSizeEntry,_a:wwpLeosBenchmarkProfileFrameSizeProfileId,_b:wwpLeosBenchmarkProfileFrameSizeIndex,'wwpLeosBenchmarkProfileFrameSize':wwpLeosBenchmarkProfileFrameSize})