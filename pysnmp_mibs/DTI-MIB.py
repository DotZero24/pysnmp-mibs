_AN='dtiClientGroup'
_AM='dtiServerGroup'
_AL='dtiBaseGroup'
_AK='dtiProtocolClientFsmStatsHoldoverActiveTime'
_AJ='dtiProtocolClientFsmStatsNormalActiveTime'
_AI='dtiProtocolClientFsmStatsT7Count'
_AH='dtiProtocolClientFsmStatsT6Count'
_AG='dtiProtocolClientFsmStatsT4Count'
_AF='dtiProtocolClientFsmStatsT3Count'
_AE='dtiServerGlobalToDValue'
_AD='dtiServerGlobalToDMethod'
_AC='dtiServerGlobalJitterTimeInterval'
_AB='dtiServerGlobalErrorRateInterval'
_AA='dtiServerGlobalTimeInterval'
_A9='dtiServerToDSources'
_A8='dtiServerExternalTimingSource'
_A7='dtiServerHopCount'
_A6='dtiServerRootClockType'
_A5='dtiProtocolControlToDValue'
_A4='dtiProtocolControlTestMode'
_A3='dtiProtocolControlJitterTimeInterval'
_A2='dtiProtocolControlErrorRateInterval'
_A1='dtiProtocolControlTimeInterval'
_A0='dtiProtocolServerClientStableFlag'
_z='dtiProtocolPerformanceWanderTSeconds'
_y='dtiProtocolPerformanceWander35Second'
_x='dtiProtocolPerformancePeakToPeakJitter'
_w='dtiProtocolPerformanceFrameErrorRate'
_v='dtiProtocolPerformanceDelay'
_u='dtiPathTraceabilityServerProtVersion'
_t='dtiPathTraceabilityRootServerProtVersion'
_s='dtiPathTraceabilityServerOutPhyIdx'
_r='dtiPathTraceabilityServerInetAddr'
_q='dtiPathTraceabilityServerInetAddrType'
_p='dtiPathTraceabilityRootServerOutPhyIdx'
_o='dtiPathTraceabilityRootServerInetAddr'
_n='dtiPathTraceabilityRootServerInetAddrType'
_m='dtiProtocolClientPathTraceability'
_l='dtiProtocolClientVersion'
_k='dtiProtocolClientPhaseError'
_j='dtiProtocolServerCableAdvanceValue'
_i='dtiProtocolServerCableAdvanceFlag'
_h='dtiProtocolServerToDValue'
_g='dtiProtocolServerToDType'
_f='dtiProtocolClientStatusFlag'
_e='dtiProtocolServerStatusFlag'
_d='dtiProtocolClientClockType'
_c='dtiProtocolEntityType'
_b='dtiProtocolServerToDState'
_a='milliseconds'
_Z='dtiPathTraceabilityIndex'
_Y='testMode'
_X='holdoverMode'
_W='normalMode'
_V='fastTrackingMode'
_U='freerun'
_T='warmup'
_S='unknown'
_R='ituIII'
_Q='picoseconds'
_P='ntpv4'
_O='userTime'
_N='default'
_M='invalid'
_L='valid'
_K='gps'
_J='OctetString'
_I='ifIndex'
_H='IF-MIB'
_G='seconds'
_F='read-write'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='DTI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjDocsis,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjDocsis')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dtiMib=ModuleIdentity((1,3,6,1,4,1,4491,2,1,7))
if mibBuilder.loadTexts:dtiMib.setRevisions(('2006-06-28 00:00','2005-08-05 00:00'))
class DtiCableAdvance(TextualConvention,OctetString):status=_A;displayHint='2d-1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_DtiNotifications_ObjectIdentity=ObjectIdentity
dtiNotifications=_DtiNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,0))
_DtiMibObjects_ObjectIdentity=ObjectIdentity
dtiMibObjects=_DtiMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1))
_DtiProtocolObjects_ObjectIdentity=ObjectIdentity
dtiProtocolObjects=_DtiProtocolObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1,1))
_DtiProtocolTable_Object=MibTable
dtiProtocolTable=_DtiProtocolTable_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1))
if mibBuilder.loadTexts:dtiProtocolTable.setStatus(_A)
_DtiProtocolEntry_Object=MibTableRow
dtiProtocolEntry=_DtiProtocolEntry_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1))
dtiProtocolEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dtiProtocolEntry.setStatus(_A)
class _DtiProtocolEntityType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('root',1),('server',2),('client',3)))
_DtiProtocolEntityType_Type.__name__=_D
_DtiProtocolEntityType_Object=MibTableColumn
dtiProtocolEntityType=_DtiProtocolEntityType_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,1),_DtiProtocolEntityType_Type())
dtiProtocolEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolEntityType.setStatus(_A)
class _DtiProtocolClientClockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ituI',1),('ituII',2),(_R,3),('st3',4),('dtiClock',5)))
_DtiProtocolClientClockType_Type.__name__=_D
_DtiProtocolClientClockType_Object=MibTableColumn
dtiProtocolClientClockType=_DtiProtocolClientClockType_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,2),_DtiProtocolClientClockType_Type())
dtiProtocolClientClockType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientClockType.setStatus(_A)
class _DtiProtocolServerStatusFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),('clientStable',6),(_Y,7)))
_DtiProtocolServerStatusFlag_Type.__name__=_D
_DtiProtocolServerStatusFlag_Object=MibTableColumn
dtiProtocolServerStatusFlag=_DtiProtocolServerStatusFlag_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,3),_DtiProtocolServerStatusFlag_Type())
dtiProtocolServerStatusFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerStatusFlag.setStatus(_A)
class _DtiProtocolClientStatusFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),(_V,3),(_W,4),(_X,5),('bridgingMode',6),(_Y,7)))
_DtiProtocolClientStatusFlag_Type.__name__=_D
_DtiProtocolClientStatusFlag_Object=MibTableColumn
dtiProtocolClientStatusFlag=_DtiProtocolClientStatusFlag_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,4),_DtiProtocolClientStatusFlag_Type())
dtiProtocolClientStatusFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientStatusFlag.setStatus(_A)
class _DtiProtocolServerToDState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_DtiProtocolServerToDState_Type.__name__=_D
_DtiProtocolServerToDState_Object=MibTableColumn
dtiProtocolServerToDState=_DtiProtocolServerToDState_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,5),_DtiProtocolServerToDState_Type())
dtiProtocolServerToDState.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerToDState.setStatus(_A)
class _DtiProtocolServerToDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_K,4)))
_DtiProtocolServerToDType_Type.__name__=_D
_DtiProtocolServerToDType_Object=MibTableColumn
dtiProtocolServerToDType=_DtiProtocolServerToDType_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,6),_DtiProtocolServerToDType_Type())
dtiProtocolServerToDType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerToDType.setStatus(_A)
class _DtiProtocolServerToDValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(33,33))
_DtiProtocolServerToDValue_Type.__name__=_J
_DtiProtocolServerToDValue_Object=MibTableColumn
dtiProtocolServerToDValue=_DtiProtocolServerToDValue_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,7),_DtiProtocolServerToDValue_Type())
dtiProtocolServerToDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerToDValue.setStatus(_A)
class _DtiProtocolServerCableAdvanceFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_M,2),('manual',3)))
_DtiProtocolServerCableAdvanceFlag_Type.__name__=_D
_DtiProtocolServerCableAdvanceFlag_Object=MibTableColumn
dtiProtocolServerCableAdvanceFlag=_DtiProtocolServerCableAdvanceFlag_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,8),_DtiProtocolServerCableAdvanceFlag_Type())
dtiProtocolServerCableAdvanceFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerCableAdvanceFlag.setStatus(_A)
_DtiProtocolServerCableAdvanceValue_Type=DtiCableAdvance
_DtiProtocolServerCableAdvanceValue_Object=MibTableColumn
dtiProtocolServerCableAdvanceValue=_DtiProtocolServerCableAdvanceValue_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,9),_DtiProtocolServerCableAdvanceValue_Type())
dtiProtocolServerCableAdvanceValue.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolServerCableAdvanceValue.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolServerCableAdvanceValue.setUnits('clockSamples')
class _DtiProtocolClientPhaseError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-32767,32767))
_DtiProtocolClientPhaseError_Type.__name__=_D
_DtiProtocolClientPhaseError_Object=MibTableColumn
dtiProtocolClientPhaseError=_DtiProtocolClientPhaseError_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,10),_DtiProtocolClientPhaseError_Type())
dtiProtocolClientPhaseError.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientPhaseError.setStatus(_A)
class _DtiProtocolClientVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_DtiProtocolClientVersion_Type.__name__=_E
_DtiProtocolClientVersion_Object=MibTableColumn
dtiProtocolClientVersion=_DtiProtocolClientVersion_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,11),_DtiProtocolClientVersion_Type())
dtiProtocolClientVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientVersion.setStatus(_A)
class _DtiProtocolClientPathTraceability_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_DtiProtocolClientPathTraceability_Type.__name__=_E
_DtiProtocolClientPathTraceability_Object=MibTableColumn
dtiProtocolClientPathTraceability=_DtiProtocolClientPathTraceability_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,12),_DtiProtocolClientPathTraceability_Type())
dtiProtocolClientPathTraceability.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientPathTraceability.setStatus(_A)
class _DtiProtocolServerClientStableFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_DtiProtocolServerClientStableFlag_Type.__name__=_D
_DtiProtocolServerClientStableFlag_Object=MibTableColumn
dtiProtocolServerClientStableFlag=_DtiProtocolServerClientStableFlag_Object((1,3,6,1,4,1,4491,2,1,7,1,1,1,1,13),_DtiProtocolServerClientStableFlag_Type())
dtiProtocolServerClientStableFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolServerClientStableFlag.setStatus(_A)
_DtiProtocolControlTable_Object=MibTable
dtiProtocolControlTable=_DtiProtocolControlTable_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2))
if mibBuilder.loadTexts:dtiProtocolControlTable.setStatus(_A)
_DtiProtocolControlEntry_Object=MibTableRow
dtiProtocolControlEntry=_DtiProtocolControlEntry_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1))
dtiProtocolControlEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dtiProtocolControlEntry.setStatus(_A)
class _DtiProtocolControlTimeInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiProtocolControlTimeInterval_Type.__name__=_E
_DtiProtocolControlTimeInterval_Object=MibTableColumn
dtiProtocolControlTimeInterval=_DtiProtocolControlTimeInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1,1),_DtiProtocolControlTimeInterval_Type())
dtiProtocolControlTimeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolControlTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolControlTimeInterval.setUnits(_G)
class _DtiProtocolControlErrorRateInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiProtocolControlErrorRateInterval_Type.__name__=_E
_DtiProtocolControlErrorRateInterval_Object=MibTableColumn
dtiProtocolControlErrorRateInterval=_DtiProtocolControlErrorRateInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1,2),_DtiProtocolControlErrorRateInterval_Type())
dtiProtocolControlErrorRateInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolControlErrorRateInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolControlErrorRateInterval.setUnits(_G)
class _DtiProtocolControlJitterTimeInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiProtocolControlJitterTimeInterval_Type.__name__=_E
_DtiProtocolControlJitterTimeInterval_Object=MibTableColumn
dtiProtocolControlJitterTimeInterval=_DtiProtocolControlJitterTimeInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1,3),_DtiProtocolControlJitterTimeInterval_Type())
dtiProtocolControlJitterTimeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolControlJitterTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolControlJitterTimeInterval.setUnits(_G)
_DtiProtocolControlTestMode_Type=TruthValue
_DtiProtocolControlTestMode_Object=MibTableColumn
dtiProtocolControlTestMode=_DtiProtocolControlTestMode_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1,4),_DtiProtocolControlTestMode_Type())
dtiProtocolControlTestMode.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolControlTestMode.setStatus(_A)
class _DtiProtocolControlToDValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(33,33))
_DtiProtocolControlToDValue_Type.__name__=_J
_DtiProtocolControlToDValue_Object=MibTableColumn
dtiProtocolControlToDValue=_DtiProtocolControlToDValue_Object((1,3,6,1,4,1,4491,2,1,7,1,1,2,1,5),_DtiProtocolControlToDValue_Type())
dtiProtocolControlToDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiProtocolControlToDValue.setStatus(_A)
_DtiProtocolPerformanceTable_Object=MibTable
dtiProtocolPerformanceTable=_DtiProtocolPerformanceTable_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3))
if mibBuilder.loadTexts:dtiProtocolPerformanceTable.setStatus(_A)
_DtiProtocolPerformanceEntry_Object=MibTableRow
dtiProtocolPerformanceEntry=_DtiProtocolPerformanceEntry_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1))
dtiProtocolPerformanceEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dtiProtocolPerformanceEntry.setStatus(_A)
_DtiProtocolPerformanceDelay_Type=Unsigned32
_DtiProtocolPerformanceDelay_Object=MibTableColumn
dtiProtocolPerformanceDelay=_DtiProtocolPerformanceDelay_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1,1),_DtiProtocolPerformanceDelay_Type())
dtiProtocolPerformanceDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolPerformanceDelay.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolPerformanceDelay.setUnits('nanoseconds')
_DtiProtocolPerformanceFrameErrorRate_Type=Unsigned32
_DtiProtocolPerformanceFrameErrorRate_Object=MibTableColumn
dtiProtocolPerformanceFrameErrorRate=_DtiProtocolPerformanceFrameErrorRate_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1,2),_DtiProtocolPerformanceFrameErrorRate_Type())
dtiProtocolPerformanceFrameErrorRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolPerformanceFrameErrorRate.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolPerformanceFrameErrorRate.setUnits('FER')
class _DtiProtocolPerformancePeakToPeakJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-10000,10000))
_DtiProtocolPerformancePeakToPeakJitter_Type.__name__=_D
_DtiProtocolPerformancePeakToPeakJitter_Object=MibTableColumn
dtiProtocolPerformancePeakToPeakJitter=_DtiProtocolPerformancePeakToPeakJitter_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1,3),_DtiProtocolPerformancePeakToPeakJitter_Type())
dtiProtocolPerformancePeakToPeakJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolPerformancePeakToPeakJitter.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolPerformancePeakToPeakJitter.setUnits(_Q)
class _DtiProtocolPerformanceWander35Second_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DtiProtocolPerformanceWander35Second_Type.__name__=_E
_DtiProtocolPerformanceWander35Second_Object=MibTableColumn
dtiProtocolPerformanceWander35Second=_DtiProtocolPerformanceWander35Second_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1,4),_DtiProtocolPerformanceWander35Second_Type())
dtiProtocolPerformanceWander35Second.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolPerformanceWander35Second.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolPerformanceWander35Second.setUnits(_Q)
class _DtiProtocolPerformanceWanderTSeconds_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DtiProtocolPerformanceWanderTSeconds_Type.__name__=_E
_DtiProtocolPerformanceWanderTSeconds_Object=MibTableColumn
dtiProtocolPerformanceWanderTSeconds=_DtiProtocolPerformanceWanderTSeconds_Object((1,3,6,1,4,1,4491,2,1,7,1,1,3,1,5),_DtiProtocolPerformanceWanderTSeconds_Type())
dtiProtocolPerformanceWanderTSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolPerformanceWanderTSeconds.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolPerformanceWanderTSeconds.setUnits(_Q)
_DtiPathTraceabilityTable_Object=MibTable
dtiPathTraceabilityTable=_DtiPathTraceabilityTable_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4))
if mibBuilder.loadTexts:dtiPathTraceabilityTable.setStatus(_A)
_DtiPathTraceabilityEntry_Object=MibTableRow
dtiPathTraceabilityEntry=_DtiPathTraceabilityEntry_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1))
dtiPathTraceabilityEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:dtiPathTraceabilityEntry.setStatus(_A)
class _DtiPathTraceabilityIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_DtiPathTraceabilityIndex_Type.__name__=_E
_DtiPathTraceabilityIndex_Object=MibTableColumn
dtiPathTraceabilityIndex=_DtiPathTraceabilityIndex_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,1),_DtiPathTraceabilityIndex_Type())
dtiPathTraceabilityIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dtiPathTraceabilityIndex.setStatus(_A)
_DtiPathTraceabilityRootServerInetAddrType_Type=InetAddressType
_DtiPathTraceabilityRootServerInetAddrType_Object=MibTableColumn
dtiPathTraceabilityRootServerInetAddrType=_DtiPathTraceabilityRootServerInetAddrType_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,2),_DtiPathTraceabilityRootServerInetAddrType_Type())
dtiPathTraceabilityRootServerInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityRootServerInetAddrType.setStatus(_A)
_DtiPathTraceabilityRootServerInetAddr_Type=InetAddress
_DtiPathTraceabilityRootServerInetAddr_Object=MibTableColumn
dtiPathTraceabilityRootServerInetAddr=_DtiPathTraceabilityRootServerInetAddr_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,3),_DtiPathTraceabilityRootServerInetAddr_Type())
dtiPathTraceabilityRootServerInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityRootServerInetAddr.setStatus(_A)
_DtiPathTraceabilityRootServerOutPhyIdx_Type=PhysicalIndex
_DtiPathTraceabilityRootServerOutPhyIdx_Object=MibTableColumn
dtiPathTraceabilityRootServerOutPhyIdx=_DtiPathTraceabilityRootServerOutPhyIdx_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,4),_DtiPathTraceabilityRootServerOutPhyIdx_Type())
dtiPathTraceabilityRootServerOutPhyIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityRootServerOutPhyIdx.setStatus(_A)
_DtiPathTraceabilityServerInetAddrType_Type=InetAddressType
_DtiPathTraceabilityServerInetAddrType_Object=MibTableColumn
dtiPathTraceabilityServerInetAddrType=_DtiPathTraceabilityServerInetAddrType_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,5),_DtiPathTraceabilityServerInetAddrType_Type())
dtiPathTraceabilityServerInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityServerInetAddrType.setStatus(_A)
_DtiPathTraceabilityServerInetAddr_Type=InetAddress
_DtiPathTraceabilityServerInetAddr_Object=MibTableColumn
dtiPathTraceabilityServerInetAddr=_DtiPathTraceabilityServerInetAddr_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,6),_DtiPathTraceabilityServerInetAddr_Type())
dtiPathTraceabilityServerInetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityServerInetAddr.setStatus(_A)
_DtiPathTraceabilityServerOutPhyIdx_Type=PhysicalIndex
_DtiPathTraceabilityServerOutPhyIdx_Object=MibTableColumn
dtiPathTraceabilityServerOutPhyIdx=_DtiPathTraceabilityServerOutPhyIdx_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,7),_DtiPathTraceabilityServerOutPhyIdx_Type())
dtiPathTraceabilityServerOutPhyIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityServerOutPhyIdx.setStatus(_A)
_DtiPathTraceabilityRootServerProtVersion_Type=Unsigned32
_DtiPathTraceabilityRootServerProtVersion_Object=MibTableColumn
dtiPathTraceabilityRootServerProtVersion=_DtiPathTraceabilityRootServerProtVersion_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,8),_DtiPathTraceabilityRootServerProtVersion_Type())
dtiPathTraceabilityRootServerProtVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityRootServerProtVersion.setStatus(_A)
_DtiPathTraceabilityServerProtVersion_Type=Unsigned32
_DtiPathTraceabilityServerProtVersion_Object=MibTableColumn
dtiPathTraceabilityServerProtVersion=_DtiPathTraceabilityServerProtVersion_Object((1,3,6,1,4,1,4491,2,1,7,1,1,4,1,9),_DtiPathTraceabilityServerProtVersion_Type())
dtiPathTraceabilityServerProtVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiPathTraceabilityServerProtVersion.setStatus(_A)
_DtiProtocolClientFsmStatsTable_Object=MibTable
dtiProtocolClientFsmStatsTable=_DtiProtocolClientFsmStatsTable_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6))
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsTable.setStatus(_A)
_DtiProtocolClientFsmStatsEntry_Object=MibTableRow
dtiProtocolClientFsmStatsEntry=_DtiProtocolClientFsmStatsEntry_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1))
dtiProtocolClientFsmStatsEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsEntry.setStatus(_A)
_DtiProtocolClientFsmStatsT3Count_Type=Counter32
_DtiProtocolClientFsmStatsT3Count_Object=MibTableColumn
dtiProtocolClientFsmStatsT3Count=_DtiProtocolClientFsmStatsT3Count_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,1),_DtiProtocolClientFsmStatsT3Count_Type())
dtiProtocolClientFsmStatsT3Count.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsT3Count.setStatus(_A)
_DtiProtocolClientFsmStatsT4Count_Type=Counter32
_DtiProtocolClientFsmStatsT4Count_Object=MibTableColumn
dtiProtocolClientFsmStatsT4Count=_DtiProtocolClientFsmStatsT4Count_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,2),_DtiProtocolClientFsmStatsT4Count_Type())
dtiProtocolClientFsmStatsT4Count.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsT4Count.setStatus(_A)
_DtiProtocolClientFsmStatsT6Count_Type=Counter32
_DtiProtocolClientFsmStatsT6Count_Object=MibTableColumn
dtiProtocolClientFsmStatsT6Count=_DtiProtocolClientFsmStatsT6Count_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,3),_DtiProtocolClientFsmStatsT6Count_Type())
dtiProtocolClientFsmStatsT6Count.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsT6Count.setStatus(_A)
_DtiProtocolClientFsmStatsT7Count_Type=Counter32
_DtiProtocolClientFsmStatsT7Count_Object=MibTableColumn
dtiProtocolClientFsmStatsT7Count=_DtiProtocolClientFsmStatsT7Count_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,4),_DtiProtocolClientFsmStatsT7Count_Type())
dtiProtocolClientFsmStatsT7Count.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsT7Count.setStatus(_A)
_DtiProtocolClientFsmStatsNormalActiveTime_Type=Counter32
_DtiProtocolClientFsmStatsNormalActiveTime_Object=MibTableColumn
dtiProtocolClientFsmStatsNormalActiveTime=_DtiProtocolClientFsmStatsNormalActiveTime_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,5),_DtiProtocolClientFsmStatsNormalActiveTime_Type())
dtiProtocolClientFsmStatsNormalActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsNormalActiveTime.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsNormalActiveTime.setUnits(_a)
_DtiProtocolClientFsmStatsHoldoverActiveTime_Type=Counter32
_DtiProtocolClientFsmStatsHoldoverActiveTime_Object=MibTableColumn
dtiProtocolClientFsmStatsHoldoverActiveTime=_DtiProtocolClientFsmStatsHoldoverActiveTime_Object((1,3,6,1,4,1,4491,2,1,7,1,1,6,1,6),_DtiProtocolClientFsmStatsHoldoverActiveTime_Type())
dtiProtocolClientFsmStatsHoldoverActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsHoldoverActiveTime.setStatus(_A)
if mibBuilder.loadTexts:dtiProtocolClientFsmStatsHoldoverActiveTime.setUnits(_a)
_DtiServerObjects_ObjectIdentity=ObjectIdentity
dtiServerObjects=_DtiServerObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1,2))
_DtiServerProperties_ObjectIdentity=ObjectIdentity
dtiServerProperties=_DtiServerProperties_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1,2,1))
class _DtiServerRootClockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ituI',1),('ituII',2),(_R,3),('st3',4)))
_DtiServerRootClockType_Type.__name__=_D
_DtiServerRootClockType_Object=MibScalar
dtiServerRootClockType=_DtiServerRootClockType_Object((1,3,6,1,4,1,4491,2,1,7,1,2,1,1),_DtiServerRootClockType_Type())
dtiServerRootClockType.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiServerRootClockType.setStatus(_A)
class _DtiServerHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('root',1),('proxy',2)))
_DtiServerHopCount_Type.__name__=_D
_DtiServerHopCount_Object=MibScalar
dtiServerHopCount=_DtiServerHopCount_Object((1,3,6,1,4,1,4491,2,1,7,1,2,1,2),_DtiServerHopCount_Type())
dtiServerHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiServerHopCount.setStatus(_A)
class _DtiServerExternalTimingSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noExternal',1),(_K,2),('network',3)))
_DtiServerExternalTimingSource_Type.__name__=_D
_DtiServerExternalTimingSource_Object=MibScalar
dtiServerExternalTimingSource=_DtiServerExternalTimingSource_Object((1,3,6,1,4,1,4491,2,1,7,1,2,1,3),_DtiServerExternalTimingSource_Type())
dtiServerExternalTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiServerExternalTimingSource.setStatus(_A)
class _DtiServerToDSources_Type(Bits):namedValues=NamedValues(*((_N,0),(_O,1),(_P,2),(_K,3)))
_DtiServerToDSources_Type.__name__='Bits'
_DtiServerToDSources_Object=MibScalar
dtiServerToDSources=_DtiServerToDSources_Object((1,3,6,1,4,1,4491,2,1,7,1,2,1,4),_DtiServerToDSources_Type())
dtiServerToDSources.setMaxAccess(_C)
if mibBuilder.loadTexts:dtiServerToDSources.setStatus(_A)
_DtiServerGlobalParameters_ObjectIdentity=ObjectIdentity
dtiServerGlobalParameters=_DtiServerGlobalParameters_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1,2,2))
class _DtiServerGlobalTimeInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiServerGlobalTimeInterval_Type.__name__=_E
_DtiServerGlobalTimeInterval_Object=MibScalar
dtiServerGlobalTimeInterval=_DtiServerGlobalTimeInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,2,2,1),_DtiServerGlobalTimeInterval_Type())
dtiServerGlobalTimeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiServerGlobalTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiServerGlobalTimeInterval.setUnits(_G)
class _DtiServerGlobalErrorRateInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiServerGlobalErrorRateInterval_Type.__name__=_E
_DtiServerGlobalErrorRateInterval_Object=MibScalar
dtiServerGlobalErrorRateInterval=_DtiServerGlobalErrorRateInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,2,2,2),_DtiServerGlobalErrorRateInterval_Type())
dtiServerGlobalErrorRateInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiServerGlobalErrorRateInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiServerGlobalErrorRateInterval.setUnits(_G)
class _DtiServerGlobalJitterTimeInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_DtiServerGlobalJitterTimeInterval_Type.__name__=_E
_DtiServerGlobalJitterTimeInterval_Object=MibScalar
dtiServerGlobalJitterTimeInterval=_DtiServerGlobalJitterTimeInterval_Object((1,3,6,1,4,1,4491,2,1,7,1,2,2,3),_DtiServerGlobalJitterTimeInterval_Type())
dtiServerGlobalJitterTimeInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiServerGlobalJitterTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:dtiServerGlobalJitterTimeInterval.setUnits(_G)
class _DtiServerGlobalToDMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_K,4)))
_DtiServerGlobalToDMethod_Type.__name__=_D
_DtiServerGlobalToDMethod_Object=MibScalar
dtiServerGlobalToDMethod=_DtiServerGlobalToDMethod_Object((1,3,6,1,4,1,4491,2,1,7,1,2,2,4),_DtiServerGlobalToDMethod_Type())
dtiServerGlobalToDMethod.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiServerGlobalToDMethod.setStatus(_A)
class _DtiServerGlobalToDValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(33,33))
_DtiServerGlobalToDValue_Type.__name__=_J
_DtiServerGlobalToDValue_Object=MibScalar
dtiServerGlobalToDValue=_DtiServerGlobalToDValue_Object((1,3,6,1,4,1,4491,2,1,7,1,2,2,5),_DtiServerGlobalToDValue_Type())
dtiServerGlobalToDValue.setMaxAccess(_F)
if mibBuilder.loadTexts:dtiServerGlobalToDValue.setStatus(_A)
_DtiClientObjects_ObjectIdentity=ObjectIdentity
dtiClientObjects=_DtiClientObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,1,3))
_DtiMibConformance_ObjectIdentity=ObjectIdentity
dtiMibConformance=_DtiMibConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,2))
_DtiMibCompliances_ObjectIdentity=ObjectIdentity
dtiMibCompliances=_DtiMibCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,2,1))
_DtiMibGroups_ObjectIdentity=ObjectIdentity
dtiMibGroups=_DtiMibGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,7,2,2))
dtiBaseGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,7,2,2,1))
dtiBaseGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:dtiBaseGroup.setStatus(_A)
dtiServerGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,7,2,2,2))
dtiServerGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:dtiServerGroup.setStatus(_A)
dtiClientGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,7,2,2,3))
dtiClientGroup.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:dtiClientGroup.setStatus(_A)
dtiMibCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,7,2,1,1))
dtiMibCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:dtiMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DtiCableAdvance':DtiCableAdvance,'dtiMib':dtiMib,'dtiNotifications':dtiNotifications,'dtiMibObjects':dtiMibObjects,'dtiProtocolObjects':dtiProtocolObjects,'dtiProtocolTable':dtiProtocolTable,'dtiProtocolEntry':dtiProtocolEntry,_c:dtiProtocolEntityType,_d:dtiProtocolClientClockType,_e:dtiProtocolServerStatusFlag,_f:dtiProtocolClientStatusFlag,_b:dtiProtocolServerToDState,_g:dtiProtocolServerToDType,_h:dtiProtocolServerToDValue,_i:dtiProtocolServerCableAdvanceFlag,_j:dtiProtocolServerCableAdvanceValue,_k:dtiProtocolClientPhaseError,_l:dtiProtocolClientVersion,_m:dtiProtocolClientPathTraceability,_A0:dtiProtocolServerClientStableFlag,'dtiProtocolControlTable':dtiProtocolControlTable,'dtiProtocolControlEntry':dtiProtocolControlEntry,_A1:dtiProtocolControlTimeInterval,_A2:dtiProtocolControlErrorRateInterval,_A3:dtiProtocolControlJitterTimeInterval,_A4:dtiProtocolControlTestMode,_A5:dtiProtocolControlToDValue,'dtiProtocolPerformanceTable':dtiProtocolPerformanceTable,'dtiProtocolPerformanceEntry':dtiProtocolPerformanceEntry,_v:dtiProtocolPerformanceDelay,_w:dtiProtocolPerformanceFrameErrorRate,_x:dtiProtocolPerformancePeakToPeakJitter,_y:dtiProtocolPerformanceWander35Second,_z:dtiProtocolPerformanceWanderTSeconds,'dtiPathTraceabilityTable':dtiPathTraceabilityTable,'dtiPathTraceabilityEntry':dtiPathTraceabilityEntry,_Z:dtiPathTraceabilityIndex,_n:dtiPathTraceabilityRootServerInetAddrType,_o:dtiPathTraceabilityRootServerInetAddr,_p:dtiPathTraceabilityRootServerOutPhyIdx,_q:dtiPathTraceabilityServerInetAddrType,_r:dtiPathTraceabilityServerInetAddr,_s:dtiPathTraceabilityServerOutPhyIdx,_t:dtiPathTraceabilityRootServerProtVersion,_u:dtiPathTraceabilityServerProtVersion,'dtiProtocolClientFsmStatsTable':dtiProtocolClientFsmStatsTable,'dtiProtocolClientFsmStatsEntry':dtiProtocolClientFsmStatsEntry,_AF:dtiProtocolClientFsmStatsT3Count,_AG:dtiProtocolClientFsmStatsT4Count,_AH:dtiProtocolClientFsmStatsT6Count,_AI:dtiProtocolClientFsmStatsT7Count,_AJ:dtiProtocolClientFsmStatsNormalActiveTime,_AK:dtiProtocolClientFsmStatsHoldoverActiveTime,'dtiServerObjects':dtiServerObjects,'dtiServerProperties':dtiServerProperties,_A6:dtiServerRootClockType,_A7:dtiServerHopCount,_A8:dtiServerExternalTimingSource,_A9:dtiServerToDSources,'dtiServerGlobalParameters':dtiServerGlobalParameters,_AA:dtiServerGlobalTimeInterval,_AB:dtiServerGlobalErrorRateInterval,_AC:dtiServerGlobalJitterTimeInterval,_AD:dtiServerGlobalToDMethod,_AE:dtiServerGlobalToDValue,'dtiClientObjects':dtiClientObjects,'dtiMibConformance':dtiMibConformance,'dtiMibCompliances':dtiMibCompliances,'dtiMibCompliance':dtiMibCompliance,'dtiMibGroups':dtiMibGroups,_AL:dtiBaseGroup,_AM:dtiServerGroup,_AN:dtiClientGroup})