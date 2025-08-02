_h='avRtpSessionRemInetAddr'
_g='avRtpSessionRemInetAddrType'
_f='avRtpSessionLocInetAddr'
_e='avRtpSessionLocInetAddrType'
_d='avRtpSessionRemAddrV4'
_c='avRtpSessionLocAddrV4'
_b='avRtpSessionRemAddr'
_a='avRtpSessionRemAddrType'
_Z='avRtpSumEngineID'
_Y='avRtpThresholdSet'
_X='disabled'
_W='notSupported'
_V='warning'
_U='critical'
_T='indeterminate'
_S='cleared'
_R='TimeInterval'
_Q='OctetString'
_P='avRtpQoSClearTh'
_O='avRtpQoSFaultTh'
_N='avRtpSessionDebugStr'
_M='avRtpSessionPhone'
_L='avRtpSessionCname'
_K='avRtpSessionDuration'
_J='avRtpSessionID'
_I='avRtpSessionState'
_H='accessible-for-notify'
_G='avRtpSessionSeverity'
_F='DisplayString'
_E='read-write'
_D='AVAYA-RTP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressIPv6,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention',_R,'TruthValue')
avRtpMib=ModuleIdentity((1,3,6,1,4,1,6889,2,7))
class AvRtpItuPerceivedSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),('major',4),('minor',5),(_V,6)))
class AvRtpLoss(TextualConvention,Integer32):status=_A;displayHint='d-1%';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,1000))
class AvRtpSilenceSupp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),(_X,1),('noRtp',2),('silenceFrames',3),('complex',4)))
_Avaya_ObjectIdentity=ObjectIdentity
avaya=_Avaya_ObjectIdentity((1,3,6,1,4,1,6889))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_AvRtpNotification_ObjectIdentity=ObjectIdentity
avRtpNotification=_AvRtpNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,7,0))
_AvRtpConfig_ObjectIdentity=ObjectIdentity
avRtpConfig=_AvRtpConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,7,1))
_AvRtpThresholdTable_Object=MibTable
avRtpThresholdTable=_AvRtpThresholdTable_Object((1,3,6,1,4,1,6889,2,7,1,1))
if mibBuilder.loadTexts:avRtpThresholdTable.setStatus(_A)
_AvRtpThresholdEntry_Object=MibTableRow
avRtpThresholdEntry=_AvRtpThresholdEntry_Object((1,3,6,1,4,1,6889,2,7,1,1,1))
avRtpThresholdEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:avRtpThresholdEntry.setStatus(_A)
_AvRtpThresholdSet_Type=Integer32
_AvRtpThresholdSet_Object=MibTableColumn
avRtpThresholdSet=_AvRtpThresholdSet_Object((1,3,6,1,4,1,6889,2,7,1,1,1,1),_AvRtpThresholdSet_Type())
avRtpThresholdSet.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpThresholdSet.setStatus(_A)
class _AvRtpThresholdMinStatWin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_AvRtpThresholdMinStatWin_Type.__name__=_C
_AvRtpThresholdMinStatWin_Object=MibTableColumn
avRtpThresholdMinStatWin=_AvRtpThresholdMinStatWin_Object((1,3,6,1,4,1,6889,2,7,1,1,1,2),_AvRtpThresholdMinStatWin_Type())
avRtpThresholdMinStatWin.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdMinStatWin.setStatus(_A)
_AvRtpThresholdRxCodecLoss_Type=AvRtpLoss
_AvRtpThresholdRxCodecLoss_Object=MibTableColumn
avRtpThresholdRxCodecLoss=_AvRtpThresholdRxCodecLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,3),_AvRtpThresholdRxCodecLoss_Type())
avRtpThresholdRxCodecLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxCodecLoss.setStatus(_A)
_AvRtpThresholdRxAvgCodecLoss_Type=AvRtpLoss
_AvRtpThresholdRxAvgCodecLoss_Object=MibTableColumn
avRtpThresholdRxAvgCodecLoss=_AvRtpThresholdRxAvgCodecLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,4),_AvRtpThresholdRxAvgCodecLoss_Type())
avRtpThresholdRxAvgCodecLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxAvgCodecLoss.setStatus(_A)
class _AvRtpThresholdRxCodecLossEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRxCodecLossEv_Type.__name__=_C
_AvRtpThresholdRxCodecLossEv_Object=MibTableColumn
avRtpThresholdRxCodecLossEv=_AvRtpThresholdRxCodecLossEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,5),_AvRtpThresholdRxCodecLossEv_Type())
avRtpThresholdRxCodecLossEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxCodecLossEv.setStatus(_A)
class _AvRtpThresholdCodecRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AvRtpThresholdCodecRtt_Type.__name__=_C
_AvRtpThresholdCodecRtt_Object=MibTableColumn
avRtpThresholdCodecRtt=_AvRtpThresholdCodecRtt_Object((1,3,6,1,4,1,6889,2,7,1,1,1,6),_AvRtpThresholdCodecRtt_Type())
avRtpThresholdCodecRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdCodecRtt.setStatus(_A)
class _AvRtpThresholdCodecRttEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdCodecRttEv_Type.__name__=_C
_AvRtpThresholdCodecRttEv_Object=MibTableColumn
avRtpThresholdCodecRttEv=_AvRtpThresholdCodecRttEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,7),_AvRtpThresholdCodecRttEv_Type())
avRtpThresholdCodecRttEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdCodecRttEv.setStatus(_A)
class _AvRtpThresholdEcReturnLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AvRtpThresholdEcReturnLoss_Type.__name__=_C
_AvRtpThresholdEcReturnLoss_Object=MibTableColumn
avRtpThresholdEcReturnLoss=_AvRtpThresholdEcReturnLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,8),_AvRtpThresholdEcReturnLoss_Type())
avRtpThresholdEcReturnLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdEcReturnLoss.setStatus(_A)
class _AvRtpThresholdEcReturnLossEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdEcReturnLossEv_Type.__name__=_C
_AvRtpThresholdEcReturnLossEv_Object=MibTableColumn
avRtpThresholdEcReturnLossEv=_AvRtpThresholdEcReturnLossEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,9),_AvRtpThresholdEcReturnLossEv_Type())
avRtpThresholdEcReturnLossEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdEcReturnLossEv.setStatus(_A)
_AvRtpThresholdRxLoss_Type=AvRtpLoss
_AvRtpThresholdRxLoss_Object=MibTableColumn
avRtpThresholdRxLoss=_AvRtpThresholdRxLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,10),_AvRtpThresholdRxLoss_Type())
avRtpThresholdRxLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxLoss.setStatus(_A)
class _AvRtpThresholdRxLossEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRxLossEv_Type.__name__=_C
_AvRtpThresholdRxLossEv_Object=MibTableColumn
avRtpThresholdRxLossEv=_AvRtpThresholdRxLossEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,11),_AvRtpThresholdRxLossEv_Type())
avRtpThresholdRxLossEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxLossEv.setStatus(_A)
_AvRtpThresholdRemLoss_Type=AvRtpLoss
_AvRtpThresholdRemLoss_Object=MibTableColumn
avRtpThresholdRemLoss=_AvRtpThresholdRemLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,12),_AvRtpThresholdRemLoss_Type())
avRtpThresholdRemLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRemLoss.setStatus(_A)
class _AvRtpThresholdRemLossEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRemLossEv_Type.__name__=_C
_AvRtpThresholdRemLossEv_Object=MibTableColumn
avRtpThresholdRemLossEv=_AvRtpThresholdRemLossEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,13),_AvRtpThresholdRemLossEv_Type())
avRtpThresholdRemLossEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRemLossEv.setStatus(_A)
_AvRtpThresholdAvgRxLoss_Type=AvRtpLoss
_AvRtpThresholdAvgRxLoss_Object=MibTableColumn
avRtpThresholdAvgRxLoss=_AvRtpThresholdAvgRxLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,14),_AvRtpThresholdAvgRxLoss_Type())
avRtpThresholdAvgRxLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdAvgRxLoss.setStatus(_A)
_AvRtpThresholdAvgRemLoss_Type=AvRtpLoss
_AvRtpThresholdAvgRemLoss_Object=MibTableColumn
avRtpThresholdAvgRemLoss=_AvRtpThresholdAvgRemLoss_Object((1,3,6,1,4,1,6889,2,7,1,1,1,15),_AvRtpThresholdAvgRemLoss_Type())
avRtpThresholdAvgRemLoss.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdAvgRemLoss.setStatus(_A)
class _AvRtpThresholdRxJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AvRtpThresholdRxJitter_Type.__name__=_C
_AvRtpThresholdRxJitter_Object=MibTableColumn
avRtpThresholdRxJitter=_AvRtpThresholdRxJitter_Object((1,3,6,1,4,1,6889,2,7,1,1,1,16),_AvRtpThresholdRxJitter_Type())
avRtpThresholdRxJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxJitter.setStatus(_A)
class _AvRtpThresholdRxJitterEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRxJitterEv_Type.__name__=_C
_AvRtpThresholdRxJitterEv_Object=MibTableColumn
avRtpThresholdRxJitterEv=_AvRtpThresholdRxJitterEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,17),_AvRtpThresholdRxJitterEv_Type())
avRtpThresholdRxJitterEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxJitterEv.setStatus(_A)
class _AvRtpThresholdRemJitter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AvRtpThresholdRemJitter_Type.__name__=_C
_AvRtpThresholdRemJitter_Object=MibTableColumn
avRtpThresholdRemJitter=_AvRtpThresholdRemJitter_Object((1,3,6,1,4,1,6889,2,7,1,1,1,18),_AvRtpThresholdRemJitter_Type())
avRtpThresholdRemJitter.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRemJitter.setStatus(_A)
class _AvRtpThresholdRemJitterEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRemJitterEv_Type.__name__=_C
_AvRtpThresholdRemJitterEv_Object=MibTableColumn
avRtpThresholdRemJitterEv=_AvRtpThresholdRemJitterEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,19),_AvRtpThresholdRemJitterEv_Type())
avRtpThresholdRemJitterEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRemJitterEv.setStatus(_A)
class _AvRtpThresholdRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AvRtpThresholdRtt_Type.__name__=_C
_AvRtpThresholdRtt_Object=MibTableColumn
avRtpThresholdRtt=_AvRtpThresholdRtt_Object((1,3,6,1,4,1,6889,2,7,1,1,1,20),_AvRtpThresholdRtt_Type())
avRtpThresholdRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRtt.setStatus(_A)
class _AvRtpThresholdRttEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRttEv_Type.__name__=_C
_AvRtpThresholdRttEv_Object=MibTableColumn
avRtpThresholdRttEv=_AvRtpThresholdRttEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,21),_AvRtpThresholdRttEv_Type())
avRtpThresholdRttEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRttEv.setStatus(_A)
class _AvRtpThresholdRxSsrcChangeEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AvRtpThresholdRxSsrcChangeEv_Type.__name__=_C
_AvRtpThresholdRxSsrcChangeEv_Object=MibTableColumn
avRtpThresholdRxSsrcChangeEv=_AvRtpThresholdRxSsrcChangeEv_Object((1,3,6,1,4,1,6889,2,7,1,1,1,22),_AvRtpThresholdRxSsrcChangeEv_Type())
avRtpThresholdRxSsrcChangeEv.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpThresholdRxSsrcChangeEv.setStatus(_A)
_AvRtpEnable_Type=TruthValue
_AvRtpEnable_Object=MibScalar
avRtpEnable=_AvRtpEnable_Object((1,3,6,1,4,1,6889,2,7,1,2),_AvRtpEnable_Type())
avRtpEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpEnable.setStatus(_A)
_AvRtpQoSTrapEnable_Type=TruthValue
_AvRtpQoSTrapEnable_Object=MibScalar
avRtpQoSTrapEnable=_AvRtpQoSTrapEnable_Object((1,3,6,1,4,1,6889,2,7,1,3),_AvRtpQoSTrapEnable_Type())
avRtpQoSTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSTrapEnable.setStatus(_A)
_AvRtpQoSFaultTrapEnable_Type=TruthValue
_AvRtpQoSFaultTrapEnable_Object=MibScalar
avRtpQoSFaultTrapEnable=_AvRtpQoSFaultTrapEnable_Object((1,3,6,1,4,1,6889,2,7,1,4),_AvRtpQoSFaultTrapEnable_Type())
avRtpQoSFaultTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSFaultTrapEnable.setStatus(_A)
class _AvRtpQoSFaultTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AvRtpQoSFaultTh_Type.__name__=_C
_AvRtpQoSFaultTh_Object=MibScalar
avRtpQoSFaultTh=_AvRtpQoSFaultTh_Object((1,3,6,1,4,1,6889,2,7,1,5),_AvRtpQoSFaultTh_Type())
avRtpQoSFaultTh.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSFaultTh.setStatus(_A)
class _AvRtpQoSClearTh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AvRtpQoSClearTh_Type.__name__=_C
_AvRtpQoSClearTh_Object=MibScalar
avRtpQoSClearTh=_AvRtpQoSClearTh_Object((1,3,6,1,4,1,6889,2,7,1,6),_AvRtpQoSClearTh_Type())
avRtpQoSClearTh.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSClearTh.setStatus(_A)
_AvRtpTxQoSTraps_Type=Counter32
_AvRtpTxQoSTraps_Object=MibScalar
avRtpTxQoSTraps=_AvRtpTxQoSTraps_Object((1,3,6,1,4,1,6889,2,7,1,7),_AvRtpTxQoSTraps_Type())
avRtpTxQoSTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpTxQoSTraps.setStatus(_A)
_AvRtpQoSTrapsDrop_Type=Counter32
_AvRtpQoSTrapsDrop_Object=MibScalar
avRtpQoSTrapsDrop=_AvRtpQoSTrapsDrop_Object((1,3,6,1,4,1,6889,2,7,1,8),_AvRtpQoSTrapsDrop_Type())
avRtpQoSTrapsDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpQoSTrapsDrop.setStatus(_A)
class _AvRtpQoSTrapTokenInterval_Type(TimeInterval):defaultValue=1000;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000000))
_AvRtpQoSTrapTokenInterval_Type.__name__=_R
_AvRtpQoSTrapTokenInterval_Object=MibScalar
avRtpQoSTrapTokenInterval=_AvRtpQoSTrapTokenInterval_Object((1,3,6,1,4,1,6889,2,7,1,9),_AvRtpQoSTrapTokenInterval_Type())
avRtpQoSTrapTokenInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSTrapTokenInterval.setStatus(_A)
class _AvRtpQoSTrapBucketSize_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_AvRtpQoSTrapBucketSize_Type.__name__=_C
_AvRtpQoSTrapBucketSize_Object=MibScalar
avRtpQoSTrapBucketSize=_AvRtpQoSTrapBucketSize_Object((1,3,6,1,4,1,6889,2,7,1,10),_AvRtpQoSTrapBucketSize_Type())
avRtpQoSTrapBucketSize.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpQoSTrapBucketSize.setStatus(_A)
_AvRtpDateAndTime_Type=DateAndTime
_AvRtpDateAndTime_Object=MibScalar
avRtpDateAndTime=_AvRtpDateAndTime_Object((1,3,6,1,4,1,6889,2,7,1,11),_AvRtpDateAndTime_Type())
avRtpDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpDateAndTime.setStatus(_A)
_AvRtpMaxSessionTableSize_Type=Integer32
_AvRtpMaxSessionTableSize_Object=MibScalar
avRtpMaxSessionTableSize=_AvRtpMaxSessionTableSize_Object((1,3,6,1,4,1,6889,2,7,1,12),_AvRtpMaxSessionTableSize_Type())
avRtpMaxSessionTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpMaxSessionTableSize.setStatus(_A)
_AvRtpReservedSessionTableRows_Type=Integer32
_AvRtpReservedSessionTableRows_Object=MibScalar
avRtpReservedSessionTableRows=_AvRtpReservedSessionTableRows_Object((1,3,6,1,4,1,6889,2,7,1,13),_AvRtpReservedSessionTableRows_Type())
avRtpReservedSessionTableRows.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpReservedSessionTableRows.setStatus(_A)
_AvRtpClear_Type=TruthValue
_AvRtpClear_Object=MibScalar
avRtpClear=_AvRtpClear_Object((1,3,6,1,4,1,6889,2,7,1,14),_AvRtpClear_Type())
avRtpClear.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpClear.setStatus(_A)
class _AvRtpFaultMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_AvRtpFaultMask_Type.__name__=_Q
_AvRtpFaultMask_Object=MibScalar
avRtpFaultMask=_AvRtpFaultMask_Object((1,3,6,1,4,1,6889,2,7,1,15),_AvRtpFaultMask_Type())
avRtpFaultMask.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpFaultMask.setStatus(_A)
_AvRtpSessionTable_Object=MibTable
avRtpSessionTable=_AvRtpSessionTable_Object((1,3,6,1,4,1,6889,2,7,2))
if mibBuilder.loadTexts:avRtpSessionTable.setStatus(_A)
_AvRtpSessionEntry_Object=MibTableRow
avRtpSessionEntry=_AvRtpSessionEntry_Object((1,3,6,1,4,1,6889,2,7,2,1))
avRtpSessionEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:avRtpSessionEntry.setStatus(_A)
class _AvRtpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('activeWithEvent',2),('terminated',3),('terminatedWithEvent',4)))
_AvRtpSessionState_Type.__name__=_C
_AvRtpSessionState_Object=MibTableColumn
avRtpSessionState=_AvRtpSessionState_Object((1,3,6,1,4,1,6889,2,7,2,1,1),_AvRtpSessionState_Type())
avRtpSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionState.setStatus(_A)
_AvRtpSessionID_Type=Integer32
_AvRtpSessionID_Object=MibTableColumn
avRtpSessionID=_AvRtpSessionID_Object((1,3,6,1,4,1,6889,2,7,2,1,2),_AvRtpSessionID_Type())
avRtpSessionID.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionID.setStatus(_A)
_AvRtpSessionEngineID_Type=Integer32
_AvRtpSessionEngineID_Object=MibTableColumn
avRtpSessionEngineID=_AvRtpSessionEngineID_Object((1,3,6,1,4,1,6889,2,7,2,1,3),_AvRtpSessionEngineID_Type())
avRtpSessionEngineID.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionEngineID.setStatus(_A)
_AvRtpSessionLocAddrType_Type=InetAddressType
_AvRtpSessionLocAddrType_Object=MibTableColumn
avRtpSessionLocAddrType=_AvRtpSessionLocAddrType_Object((1,3,6,1,4,1,6889,2,7,2,1,4),_AvRtpSessionLocAddrType_Type())
avRtpSessionLocAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionLocAddrType.setStatus(_A)
_AvRtpSessionLocAddr_Type=InetAddress
_AvRtpSessionLocAddr_Object=MibTableColumn
avRtpSessionLocAddr=_AvRtpSessionLocAddr_Object((1,3,6,1,4,1,6889,2,7,2,1,5),_AvRtpSessionLocAddr_Type())
avRtpSessionLocAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionLocAddr.setStatus(_A)
_AvRtpSessionLocAddrV4_Type=IpAddress
_AvRtpSessionLocAddrV4_Object=MibTableColumn
avRtpSessionLocAddrV4=_AvRtpSessionLocAddrV4_Object((1,3,6,1,4,1,6889,2,7,2,1,6),_AvRtpSessionLocAddrV4_Type())
avRtpSessionLocAddrV4.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionLocAddrV4.setStatus(_A)
_AvRtpSessionLocAddrV6_Type=InetAddressIPv6
_AvRtpSessionLocAddrV6_Object=MibTableColumn
avRtpSessionLocAddrV6=_AvRtpSessionLocAddrV6_Object((1,3,6,1,4,1,6889,2,7,2,1,7),_AvRtpSessionLocAddrV6_Type())
avRtpSessionLocAddrV6.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionLocAddrV6.setStatus(_A)
_AvRtpSessionRemAddrType_Type=InetAddressType
_AvRtpSessionRemAddrType_Object=MibTableColumn
avRtpSessionRemAddrType=_AvRtpSessionRemAddrType_Object((1,3,6,1,4,1,6889,2,7,2,1,8),_AvRtpSessionRemAddrType_Type())
avRtpSessionRemAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAddrType.setStatus(_A)
_AvRtpSessionRemAddr_Type=InetAddress
_AvRtpSessionRemAddr_Object=MibTableColumn
avRtpSessionRemAddr=_AvRtpSessionRemAddr_Object((1,3,6,1,4,1,6889,2,7,2,1,9),_AvRtpSessionRemAddr_Type())
avRtpSessionRemAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAddr.setStatus(_A)
_AvRtpSessionRemAddrV4_Type=IpAddress
_AvRtpSessionRemAddrV4_Object=MibTableColumn
avRtpSessionRemAddrV4=_AvRtpSessionRemAddrV4_Object((1,3,6,1,4,1,6889,2,7,2,1,10),_AvRtpSessionRemAddrV4_Type())
avRtpSessionRemAddrV4.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAddrV4.setStatus(_A)
_AvRtpSessionRemAddrV6_Type=InetAddressIPv6
_AvRtpSessionRemAddrV6_Object=MibTableColumn
avRtpSessionRemAddrV6=_AvRtpSessionRemAddrV6_Object((1,3,6,1,4,1,6889,2,7,2,1,11),_AvRtpSessionRemAddrV6_Type())
avRtpSessionRemAddrV6.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAddrV6.setStatus(_A)
_AvRtpSessionLocPort_Type=InetPortNumber
_AvRtpSessionLocPort_Object=MibTableColumn
avRtpSessionLocPort=_AvRtpSessionLocPort_Object((1,3,6,1,4,1,6889,2,7,2,1,12),_AvRtpSessionLocPort_Type())
avRtpSessionLocPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionLocPort.setStatus(_A)
_AvRtpSessionRemPort_Type=InetPortNumber
_AvRtpSessionRemPort_Object=MibTableColumn
avRtpSessionRemPort=_AvRtpSessionRemPort_Object((1,3,6,1,4,1,6889,2,7,2,1,13),_AvRtpSessionRemPort_Type())
avRtpSessionRemPort.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemPort.setStatus(_A)
_AvRtpSessionStartTime_Type=DateAndTime
_AvRtpSessionStartTime_Object=MibTableColumn
avRtpSessionStartTime=_AvRtpSessionStartTime_Object((1,3,6,1,4,1,6889,2,7,2,1,14),_AvRtpSessionStartTime_Type())
avRtpSessionStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionStartTime.setStatus(_A)
_AvRtpSessionEndTime_Type=DateAndTime
_AvRtpSessionEndTime_Object=MibTableColumn
avRtpSessionEndTime=_AvRtpSessionEndTime_Object((1,3,6,1,4,1,6889,2,7,2,1,15),_AvRtpSessionEndTime_Type())
avRtpSessionEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionEndTime.setStatus(_A)
_AvRtpSessionDuration_Type=TimeInterval
_AvRtpSessionDuration_Object=MibTableColumn
avRtpSessionDuration=_AvRtpSessionDuration_Object((1,3,6,1,4,1,6889,2,7,2,1,16),_AvRtpSessionDuration_Type())
avRtpSessionDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionDuration.setStatus(_A)
class _AvRtpSessionCname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_AvRtpSessionCname_Type.__name__=_F
_AvRtpSessionCname_Object=MibTableColumn
avRtpSessionCname=_AvRtpSessionCname_Object((1,3,6,1,4,1,6889,2,7,2,1,17),_AvRtpSessionCname_Type())
avRtpSessionCname.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionCname.setStatus(_A)
class _AvRtpSessionPhone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_AvRtpSessionPhone_Type.__name__=_F
_AvRtpSessionPhone_Object=MibTableColumn
avRtpSessionPhone=_AvRtpSessionPhone_Object((1,3,6,1,4,1,6889,2,7,2,1,18),_AvRtpSessionPhone_Type())
avRtpSessionPhone.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionPhone.setStatus(_A)
class _AvRtpSessionSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),('major',4),('minor',5),(_V,6)))
_AvRtpSessionSeverity_Type.__name__=_C
_AvRtpSessionSeverity_Object=MibTableColumn
avRtpSessionSeverity=_AvRtpSessionSeverity_Object((1,3,6,1,4,1,6889,2,7,2,1,19),_AvRtpSessionSeverity_Type())
avRtpSessionSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionSeverity.setStatus(_A)
_AvRtpSessionTxLen_Type=Integer32
_AvRtpSessionTxLen_Object=MibTableColumn
avRtpSessionTxLen=_AvRtpSessionTxLen_Object((1,3,6,1,4,1,6889,2,7,2,1,20),_AvRtpSessionTxLen_Type())
avRtpSessionTxLen.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxLen.setStatus(_A)
class _AvRtpSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,8,9,15,18,128,129,130,131,132,133,134,135,136,137,138,139,140,255)));namedValues=NamedValues(*(('g711u',0),('g723',4),('g711a',8),('g722',9),('g728',15),('g729',18),('avayaFaxRelay',128),('t38fax',129),('faxPassThru',130),('ttyRelay',131),('ttyPassThru',132),('modemRelay',133),('modemPassThru',134),('clearChannel',135),('g729a',136),('g729ab',137),('g729b',138),('g726a32',139),('opus',140),('unspecified',255)))
_AvRtpSessionType_Type.__name__=_C
_AvRtpSessionType_Object=MibTableColumn
avRtpSessionType=_AvRtpSessionType_Object((1,3,6,1,4,1,6889,2,7,2,1,21),_AvRtpSessionType_Type())
avRtpSessionType.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionType.setStatus(_A)
_AvRtpSessionTxInterval_Type=Integer32
_AvRtpSessionTxInterval_Object=MibTableColumn
avRtpSessionTxInterval=_AvRtpSessionTxInterval_Object((1,3,6,1,4,1,6889,2,7,2,1,22),_AvRtpSessionTxInterval_Type())
avRtpSessionTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxInterval.setStatus(_A)
class _AvRtpSessionTxEncryp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('unknown',-1),('encryptionOff',0),('encryptionAEAv2',1),('encryptionAES',2),('srtpAesCm128',4),('srtpAesCm128HmacSha180',5),('srtpAesCm128HmacSha132',6),('srtpF8128HmacSha180',7),('srtpHmacSha180',8),('srtpHmacSha132',9),('srtp',10),('srtpAesCm256',11),('srtpAesCm256HmacSha180',12),('srtpAesCm256HmacSha132',13)))
_AvRtpSessionTxEncryp_Type.__name__=_C
_AvRtpSessionTxEncryp_Object=MibTableColumn
avRtpSessionTxEncryp=_AvRtpSessionTxEncryp_Object((1,3,6,1,4,1,6889,2,7,2,1,23),_AvRtpSessionTxEncryp_Type())
avRtpSessionTxEncryp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxEncryp.setStatus(_A)
class _AvRtpSessionTxDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AvRtpSessionTxDscp_Type.__name__=_C
_AvRtpSessionTxDscp_Object=MibTableColumn
avRtpSessionTxDscp=_AvRtpSessionTxDscp_Object((1,3,6,1,4,1,6889,2,7,2,1,24),_AvRtpSessionTxDscp_Type())
avRtpSessionTxDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxDscp.setStatus(_A)
class _AvRtpSessionTxVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_AvRtpSessionTxVlan_Type.__name__=_C
_AvRtpSessionTxVlan_Object=MibTableColumn
avRtpSessionTxVlan=_AvRtpSessionTxVlan_Object((1,3,6,1,4,1,6889,2,7,2,1,25),_AvRtpSessionTxVlan_Type())
avRtpSessionTxVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxVlan.setStatus(_A)
class _AvRtpSessionTxL2Pri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_AvRtpSessionTxL2Pri_Type.__name__=_C
_AvRtpSessionTxL2Pri_Object=MibTableColumn
avRtpSessionTxL2Pri=_AvRtpSessionTxL2Pri_Object((1,3,6,1,4,1,6889,2,7,2,1,26),_AvRtpSessionTxL2Pri_Type())
avRtpSessionTxL2Pri.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxL2Pri.setStatus(_A)
_AvRtpSessionTxSilenceSupp_Type=AvRtpSilenceSupp
_AvRtpSessionTxSilenceSupp_Object=MibTableColumn
avRtpSessionTxSilenceSupp=_AvRtpSessionTxSilenceSupp_Object((1,3,6,1,4,1,6889,2,7,2,1,27),_AvRtpSessionTxSilenceSupp_Type())
avRtpSessionTxSilenceSupp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxSilenceSupp.setStatus(_A)
_AvRtpSessionTxSsrc_Type=Unsigned32
_AvRtpSessionTxSsrc_Object=MibTableColumn
avRtpSessionTxSsrc=_AvRtpSessionTxSsrc_Object((1,3,6,1,4,1,6889,2,7,2,1,28),_AvRtpSessionTxSsrc_Type())
avRtpSessionTxSsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxSsrc.setStatus(_A)
class _AvRtpSessionTxRsvp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unused',0),(_X,1),('pending',2),('failed',3),('reserved',4)))
_AvRtpSessionTxRsvp_Type.__name__=_C
_AvRtpSessionTxRsvp_Object=MibTableColumn
avRtpSessionTxRsvp=_AvRtpSessionTxRsvp_Object((1,3,6,1,4,1,6889,2,7,2,1,29),_AvRtpSessionTxRsvp_Type())
avRtpSessionTxRsvp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxRsvp.setStatus(_A)
_AvRtpSessionTxResvFail_Type=Gauge32
_AvRtpSessionTxResvFail_Object=MibTableColumn
avRtpSessionTxResvFail=_AvRtpSessionTxResvFail_Object((1,3,6,1,4,1,6889,2,7,2,1,30),_AvRtpSessionTxResvFail_Type())
avRtpSessionTxResvFail.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxResvFail.setStatus(_A)
_AvRtpSessionStatInterval_Type=TimeInterval
_AvRtpSessionStatInterval_Object=MibTableColumn
avRtpSessionStatInterval=_AvRtpSessionStatInterval_Object((1,3,6,1,4,1,6889,2,7,2,1,31),_AvRtpSessionStatInterval_Type())
avRtpSessionStatInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionStatInterval.setStatus(_A)
_AvRtpSessionRxCodecPlayTime_Type=Counter32
_AvRtpSessionRxCodecPlayTime_Object=MibTableColumn
avRtpSessionRxCodecPlayTime=_AvRtpSessionRxCodecPlayTime_Object((1,3,6,1,4,1,6889,2,7,2,1,32),_AvRtpSessionRxCodecPlayTime_Type())
avRtpSessionRxCodecPlayTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxCodecPlayTime.setStatus(_A)
_AvRtpSessionRxCodecLossCount_Type=Counter32
_AvRtpSessionRxCodecLossCount_Object=MibTableColumn
avRtpSessionRxCodecLossCount=_AvRtpSessionRxCodecLossCount_Object((1,3,6,1,4,1,6889,2,7,2,1,33),_AvRtpSessionRxCodecLossCount_Type())
avRtpSessionRxCodecLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxCodecLossCount.setStatus(_A)
_AvRtpSessionRxCodecLoss_Type=AvRtpLoss
_AvRtpSessionRxCodecLoss_Object=MibTableColumn
avRtpSessionRxCodecLoss=_AvRtpSessionRxCodecLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,34),_AvRtpSessionRxCodecLoss_Type())
avRtpSessionRxCodecLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxCodecLoss.setStatus(_A)
_AvRtpSessionRxAvgCodecLoss_Type=AvRtpLoss
_AvRtpSessionRxAvgCodecLoss_Object=MibTableColumn
avRtpSessionRxAvgCodecLoss=_AvRtpSessionRxAvgCodecLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,35),_AvRtpSessionRxAvgCodecLoss_Type())
avRtpSessionRxAvgCodecLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxAvgCodecLoss.setStatus(_A)
_AvRtpSessionRxCodecLossEv_Type=Counter32
_AvRtpSessionRxCodecLossEv_Object=MibTableColumn
avRtpSessionRxCodecLossEv=_AvRtpSessionRxCodecLossEv_Object((1,3,6,1,4,1,6889,2,7,2,1,36),_AvRtpSessionRxCodecLossEv_Type())
avRtpSessionRxCodecLossEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxCodecLossEv.setStatus(_A)
_AvRtpSessionRxLoss_Type=AvRtpLoss
_AvRtpSessionRxLoss_Object=MibTableColumn
avRtpSessionRxLoss=_AvRtpSessionRxLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,37),_AvRtpSessionRxLoss_Type())
avRtpSessionRxLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxLoss.setStatus(_A)
_AvRtpSessionRxAvgLoss_Type=AvRtpLoss
_AvRtpSessionRxAvgLoss_Object=MibTableColumn
avRtpSessionRxAvgLoss=_AvRtpSessionRxAvgLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,38),_AvRtpSessionRxAvgLoss_Type())
avRtpSessionRxAvgLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxAvgLoss.setStatus(_A)
_AvRtpSessionRxLossEv_Type=Counter32
_AvRtpSessionRxLossEv_Object=MibTableColumn
avRtpSessionRxLossEv=_AvRtpSessionRxLossEv_Object((1,3,6,1,4,1,6889,2,7,2,1,39),_AvRtpSessionRxLossEv_Type())
avRtpSessionRxLossEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxLossEv.setStatus(_A)
_AvRtpSessionRx_Type=Counter32
_AvRtpSessionRx_Object=MibTableColumn
avRtpSessionRx=_AvRtpSessionRx_Object((1,3,6,1,4,1,6889,2,7,2,1,40),_AvRtpSessionRx_Type())
avRtpSessionRx.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRx.setStatus(_A)
_AvRtpSessionRxLossCount_Type=Counter32
_AvRtpSessionRxLossCount_Object=MibTableColumn
avRtpSessionRxLossCount=_AvRtpSessionRxLossCount_Object((1,3,6,1,4,1,6889,2,7,2,1,41),_AvRtpSessionRxLossCount_Type())
avRtpSessionRxLossCount.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxLossCount.setStatus(_A)
_AvRtpSessionRxSeqFall_Type=Counter32
_AvRtpSessionRxSeqFall_Object=MibTableColumn
avRtpSessionRxSeqFall=_AvRtpSessionRxSeqFall_Object((1,3,6,1,4,1,6889,2,7,2,1,42),_AvRtpSessionRxSeqFall_Type())
avRtpSessionRxSeqFall.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxSeqFall.setStatus(_A)
_AvRtpSessionRxDup_Type=Counter32
_AvRtpSessionRxDup_Object=MibTableColumn
avRtpSessionRxDup=_AvRtpSessionRxDup_Object((1,3,6,1,4,1,6889,2,7,2,1,43),_AvRtpSessionRxDup_Type())
avRtpSessionRxDup.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxDup.setStatus(_A)
_AvRtpSessionRxJBufUnderruns_Type=Gauge32
_AvRtpSessionRxJBufUnderruns_Object=MibTableColumn
avRtpSessionRxJBufUnderruns=_AvRtpSessionRxJBufUnderruns_Object((1,3,6,1,4,1,6889,2,7,2,1,44),_AvRtpSessionRxJBufUnderruns_Type())
avRtpSessionRxJBufUnderruns.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxJBufUnderruns.setStatus(_A)
_AvRtpSessionRxJBufOverruns_Type=Gauge32
_AvRtpSessionRxJBufOverruns_Object=MibTableColumn
avRtpSessionRxJBufOverruns=_AvRtpSessionRxJBufOverruns_Object((1,3,6,1,4,1,6889,2,7,2,1,45),_AvRtpSessionRxJBufOverruns_Type())
avRtpSessionRxJBufOverruns.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxJBufOverruns.setStatus(_A)
_AvRtpSessionRxJBufDelay_Type=Integer32
_AvRtpSessionRxJBufDelay_Object=MibTableColumn
avRtpSessionRxJBufDelay=_AvRtpSessionRxJBufDelay_Object((1,3,6,1,4,1,6889,2,7,2,1,46),_AvRtpSessionRxJBufDelay_Type())
avRtpSessionRxJBufDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxJBufDelay.setStatus(_A)
_AvRtpSessionRxMaxJBufDelay_Type=Integer32
_AvRtpSessionRxMaxJBufDelay_Object=MibTableColumn
avRtpSessionRxMaxJBufDelay=_AvRtpSessionRxMaxJBufDelay_Object((1,3,6,1,4,1,6889,2,7,2,1,47),_AvRtpSessionRxMaxJBufDelay_Type())
avRtpSessionRxMaxJBufDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxMaxJBufDelay.setStatus(_A)
_AvRtpSessionRxJitter_Type=Integer32
_AvRtpSessionRxJitter_Object=MibTableColumn
avRtpSessionRxJitter=_AvRtpSessionRxJitter_Object((1,3,6,1,4,1,6889,2,7,2,1,48),_AvRtpSessionRxJitter_Type())
avRtpSessionRxJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxJitter.setStatus(_A)
_AvRtpSessionRxAvgJitter_Type=Integer32
_AvRtpSessionRxAvgJitter_Object=MibTableColumn
avRtpSessionRxAvgJitter=_AvRtpSessionRxAvgJitter_Object((1,3,6,1,4,1,6889,2,7,2,1,49),_AvRtpSessionRxAvgJitter_Type())
avRtpSessionRxAvgJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxAvgJitter.setStatus(_A)
_AvRtpSessionRxJitterEv_Type=Counter32
_AvRtpSessionRxJitterEv_Object=MibTableColumn
avRtpSessionRxJitterEv=_AvRtpSessionRxJitterEv_Object((1,3,6,1,4,1,6889,2,7,2,1,50),_AvRtpSessionRxJitterEv_Type())
avRtpSessionRxJitterEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxJitterEv.setStatus(_A)
class _AvRtpSessionRxTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvRtpSessionRxTtl_Type.__name__=_C
_AvRtpSessionRxTtl_Object=MibTableColumn
avRtpSessionRxTtl=_AvRtpSessionRxTtl_Object((1,3,6,1,4,1,6889,2,7,2,1,51),_AvRtpSessionRxTtl_Type())
avRtpSessionRxTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxTtl.setStatus(_A)
class _AvRtpSessionRxMinTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvRtpSessionRxMinTtl_Type.__name__=_C
_AvRtpSessionRxMinTtl_Object=MibTableColumn
avRtpSessionRxMinTtl=_AvRtpSessionRxMinTtl_Object((1,3,6,1,4,1,6889,2,7,2,1,52),_AvRtpSessionRxMinTtl_Type())
avRtpSessionRxMinTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxMinTtl.setStatus(_A)
class _AvRtpSessionRxMaxTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvRtpSessionRxMaxTtl_Type.__name__=_C
_AvRtpSessionRxMaxTtl_Object=MibTableColumn
avRtpSessionRxMaxTtl=_AvRtpSessionRxMaxTtl_Object((1,3,6,1,4,1,6889,2,7,2,1,53),_AvRtpSessionRxMaxTtl_Type())
avRtpSessionRxMaxTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxMaxTtl.setStatus(_A)
class _AvRtpSessionRxDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AvRtpSessionRxDscp_Type.__name__=_C
_AvRtpSessionRxDscp_Object=MibTableColumn
avRtpSessionRxDscp=_AvRtpSessionRxDscp_Object((1,3,6,1,4,1,6889,2,7,2,1,54),_AvRtpSessionRxDscp_Type())
avRtpSessionRxDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxDscp.setStatus(_A)
class _AvRtpSessionRxL2Pri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_AvRtpSessionRxL2Pri_Type.__name__=_C
_AvRtpSessionRxL2Pri_Object=MibTableColumn
avRtpSessionRxL2Pri=_AvRtpSessionRxL2Pri_Object((1,3,6,1,4,1,6889,2,7,2,1,55),_AvRtpSessionRxL2Pri_Type())
avRtpSessionRxL2Pri.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxL2Pri.setStatus(_A)
_AvRtpSessionRxSilenceSupp_Type=AvRtpSilenceSupp
_AvRtpSessionRxSilenceSupp_Object=MibTableColumn
avRtpSessionRxSilenceSupp=_AvRtpSessionRxSilenceSupp_Object((1,3,6,1,4,1,6889,2,7,2,1,56),_AvRtpSessionRxSilenceSupp_Type())
avRtpSessionRxSilenceSupp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxSilenceSupp.setStatus(_A)
_AvRtpSessionRxSsrc_Type=Unsigned32
_AvRtpSessionRxSsrc_Object=MibTableColumn
avRtpSessionRxSsrc=_AvRtpSessionRxSsrc_Object((1,3,6,1,4,1,6889,2,7,2,1,57),_AvRtpSessionRxSsrc_Type())
avRtpSessionRxSsrc.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxSsrc.setStatus(_A)
_AvRtpSessionRxSsrcChange_Type=Counter32
_AvRtpSessionRxSsrcChange_Object=MibTableColumn
avRtpSessionRxSsrcChange=_AvRtpSessionRxSsrcChange_Object((1,3,6,1,4,1,6889,2,7,2,1,58),_AvRtpSessionRxSsrcChange_Type())
avRtpSessionRxSsrcChange.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxSsrcChange.setStatus(_A)
_AvRtpSessionTxRtcp_Type=Counter32
_AvRtpSessionTxRtcp_Object=MibTableColumn
avRtpSessionTxRtcp=_AvRtpSessionTxRtcp_Object((1,3,6,1,4,1,6889,2,7,2,1,59),_AvRtpSessionTxRtcp_Type())
avRtpSessionTxRtcp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxRtcp.setStatus(_A)
_AvRtpSessionRxRtcp_Type=Counter32
_AvRtpSessionRxRtcp_Object=MibTableColumn
avRtpSessionRxRtcp=_AvRtpSessionRxRtcp_Object((1,3,6,1,4,1,6889,2,7,2,1,60),_AvRtpSessionRxRtcp_Type())
avRtpSessionRxRtcp.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxRtcp.setStatus(_A)
_AvRtpSessionCodecRtt_Type=Integer32
_AvRtpSessionCodecRtt_Object=MibTableColumn
avRtpSessionCodecRtt=_AvRtpSessionCodecRtt_Object((1,3,6,1,4,1,6889,2,7,2,1,61),_AvRtpSessionCodecRtt_Type())
avRtpSessionCodecRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionCodecRtt.setStatus(_A)
_AvRtpSessionAvgCodecRtt_Type=Integer32
_AvRtpSessionAvgCodecRtt_Object=MibTableColumn
avRtpSessionAvgCodecRtt=_AvRtpSessionAvgCodecRtt_Object((1,3,6,1,4,1,6889,2,7,2,1,62),_AvRtpSessionAvgCodecRtt_Type())
avRtpSessionAvgCodecRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionAvgCodecRtt.setStatus(_A)
_AvRtpSessionCodecRttEv_Type=Counter32
_AvRtpSessionCodecRttEv_Object=MibTableColumn
avRtpSessionCodecRttEv=_AvRtpSessionCodecRttEv_Object((1,3,6,1,4,1,6889,2,7,2,1,63),_AvRtpSessionCodecRttEv_Type())
avRtpSessionCodecRttEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionCodecRttEv.setStatus(_A)
_AvRtpSessionRtt_Type=Integer32
_AvRtpSessionRtt_Object=MibTableColumn
avRtpSessionRtt=_AvRtpSessionRtt_Object((1,3,6,1,4,1,6889,2,7,2,1,64),_AvRtpSessionRtt_Type())
avRtpSessionRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRtt.setStatus(_A)
_AvRtpSessionAvgRtt_Type=Integer32
_AvRtpSessionAvgRtt_Object=MibTableColumn
avRtpSessionAvgRtt=_AvRtpSessionAvgRtt_Object((1,3,6,1,4,1,6889,2,7,2,1,65),_AvRtpSessionAvgRtt_Type())
avRtpSessionAvgRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionAvgRtt.setStatus(_A)
_AvRtpSessionRttEv_Type=Counter32
_AvRtpSessionRttEv_Object=MibTableColumn
avRtpSessionRttEv=_AvRtpSessionRttEv_Object((1,3,6,1,4,1,6889,2,7,2,1,66),_AvRtpSessionRttEv_Type())
avRtpSessionRttEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRttEv.setStatus(_A)
_AvRtpSessionRemLoss_Type=AvRtpLoss
_AvRtpSessionRemLoss_Object=MibTableColumn
avRtpSessionRemLoss=_AvRtpSessionRemLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,67),_AvRtpSessionRemLoss_Type())
avRtpSessionRemLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemLoss.setStatus(_A)
_AvRtpSessionRemAvgLoss_Type=AvRtpLoss
_AvRtpSessionRemAvgLoss_Object=MibTableColumn
avRtpSessionRemAvgLoss=_AvRtpSessionRemAvgLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,68),_AvRtpSessionRemAvgLoss_Type())
avRtpSessionRemAvgLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAvgLoss.setStatus(_A)
_AvRtpSessionRemLossEv_Type=Counter32
_AvRtpSessionRemLossEv_Object=MibTableColumn
avRtpSessionRemLossEv=_AvRtpSessionRemLossEv_Object((1,3,6,1,4,1,6889,2,7,2,1,69),_AvRtpSessionRemLossEv_Type())
avRtpSessionRemLossEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemLossEv.setStatus(_A)
_AvRtpSessionRemJitter_Type=Integer32
_AvRtpSessionRemJitter_Object=MibTableColumn
avRtpSessionRemJitter=_AvRtpSessionRemJitter_Object((1,3,6,1,4,1,6889,2,7,2,1,70),_AvRtpSessionRemJitter_Type())
avRtpSessionRemJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemJitter.setStatus(_A)
_AvRtpSessionRemAvgJitter_Type=Integer32
_AvRtpSessionRemAvgJitter_Object=MibTableColumn
avRtpSessionRemAvgJitter=_AvRtpSessionRemAvgJitter_Object((1,3,6,1,4,1,6889,2,7,2,1,71),_AvRtpSessionRemAvgJitter_Type())
avRtpSessionRemAvgJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemAvgJitter.setStatus(_A)
_AvRtpSessionRemJitterEv_Type=Counter32
_AvRtpSessionRemJitterEv_Object=MibTableColumn
avRtpSessionRemJitterEv=_AvRtpSessionRemJitterEv_Object((1,3,6,1,4,1,6889,2,7,2,1,72),_AvRtpSessionRemJitterEv_Type())
avRtpSessionRemJitterEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRemJitterEv.setStatus(_A)
_AvRtpSessionEcTailLen_Type=Integer32
_AvRtpSessionEcTailLen_Object=MibTableColumn
avRtpSessionEcTailLen=_AvRtpSessionEcTailLen_Object((1,3,6,1,4,1,6889,2,7,2,1,73),_AvRtpSessionEcTailLen_Type())
avRtpSessionEcTailLen.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionEcTailLen.setStatus(_A)
class _AvRtpSessionEcReturnLoss_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AvRtpSessionEcReturnLoss_Type.__name__=_C
_AvRtpSessionEcReturnLoss_Object=MibTableColumn
avRtpSessionEcReturnLoss=_AvRtpSessionEcReturnLoss_Object((1,3,6,1,4,1,6889,2,7,2,1,74),_AvRtpSessionEcReturnLoss_Type())
avRtpSessionEcReturnLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionEcReturnLoss.setStatus(_A)
_AvRtpSessionEcReturnLossEv_Type=Counter32
_AvRtpSessionEcReturnLossEv_Object=MibTableColumn
avRtpSessionEcReturnLossEv=_AvRtpSessionEcReturnLossEv_Object((1,3,6,1,4,1,6889,2,7,2,1,75),_AvRtpSessionEcReturnLossEv_Type())
avRtpSessionEcReturnLossEv.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionEcReturnLossEv.setStatus(_A)
class _AvRtpSessionAEC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),('none',1),('halfDuplex',2),('fullDuplex',3),('aec',4)))
_AvRtpSessionAEC_Type.__name__=_C
_AvRtpSessionAEC_Object=MibTableColumn
avRtpSessionAEC=_AvRtpSessionAEC_Object((1,3,6,1,4,1,6889,2,7,2,1,76),_AvRtpSessionAEC_Type())
avRtpSessionAEC.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionAEC.setStatus(_A)
class _AvRtpSessionDebugStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvRtpSessionDebugStr_Type.__name__=_F
_AvRtpSessionDebugStr_Object=MibTableColumn
avRtpSessionDebugStr=_AvRtpSessionDebugStr_Object((1,3,6,1,4,1,6889,2,7,2,1,77),_AvRtpSessionDebugStr_Type())
avRtpSessionDebugStr.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionDebugStr.setStatus(_A)
class _AvRtpSessionTxFlowLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_AvRtpSessionTxFlowLabel_Type.__name__=_C
_AvRtpSessionTxFlowLabel_Object=MibTableColumn
avRtpSessionTxFlowLabel=_AvRtpSessionTxFlowLabel_Object((1,3,6,1,4,1,6889,2,7,2,1,78),_AvRtpSessionTxFlowLabel_Type())
avRtpSessionTxFlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionTxFlowLabel.setStatus(_A)
class _AvRtpSessionRxFlowLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_AvRtpSessionRxFlowLabel_Type.__name__=_C
_AvRtpSessionRxFlowLabel_Object=MibTableColumn
avRtpSessionRxFlowLabel=_AvRtpSessionRxFlowLabel_Object((1,3,6,1,4,1,6889,2,7,2,1,79),_AvRtpSessionRxFlowLabel_Type())
avRtpSessionRxFlowLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSessionRxFlowLabel.setStatus(_A)
_AvRtpSumTable_Object=MibTable
avRtpSumTable=_AvRtpSumTable_Object((1,3,6,1,4,1,6889,2,7,3))
if mibBuilder.loadTexts:avRtpSumTable.setStatus(_A)
_AvRtpSumEntry_Object=MibTableRow
avRtpSumEntry=_AvRtpSumEntry_Object((1,3,6,1,4,1,6889,2,7,3,1))
avRtpSumEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:avRtpSumEntry.setStatus(_A)
_AvRtpSumEngineID_Type=Integer32
_AvRtpSumEngineID_Object=MibTableColumn
avRtpSumEngineID=_AvRtpSumEngineID_Object((1,3,6,1,4,1,6889,2,7,3,1,1),_AvRtpSumEngineID_Type())
avRtpSumEngineID.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumEngineID.setStatus(_A)
class _AvRtpSumEngineDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvRtpSumEngineDescr_Type.__name__=_F
_AvRtpSumEngineDescr_Object=MibTableColumn
avRtpSumEngineDescr=_AvRtpSumEngineDescr_Object((1,3,6,1,4,1,6889,2,7,3,1,2),_AvRtpSumEngineDescr_Type())
avRtpSumEngineDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumEngineDescr.setStatus(_A)
_AvRtpSumPeriod_Type=TimeInterval
_AvRtpSumPeriod_Object=MibTableColumn
avRtpSumPeriod=_AvRtpSumPeriod_Object((1,3,6,1,4,1,6889,2,7,3,1,3),_AvRtpSumPeriod_Type())
avRtpSumPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumPeriod.setStatus(_A)
_AvRtpSumActiveFlows_Type=Integer32
_AvRtpSumActiveFlows_Object=MibTableColumn
avRtpSumActiveFlows=_AvRtpSumActiveFlows_Object((1,3,6,1,4,1,6889,2,7,3,1,4),_AvRtpSumActiveFlows_Type())
avRtpSumActiveFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumActiveFlows.setStatus(_A)
_AvRtpSumActiveQosEvents_Type=Integer32
_AvRtpSumActiveQosEvents_Object=MibTableColumn
avRtpSumActiveQosEvents=_AvRtpSumActiveQosEvents_Object((1,3,6,1,4,1,6889,2,7,3,1,5),_AvRtpSumActiveQosEvents_Type())
avRtpSumActiveQosEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumActiveQosEvents.setStatus(_A)
_AvRtpSumTotalFlows_Type=Counter32
_AvRtpSumTotalFlows_Object=MibTableColumn
avRtpSumTotalFlows=_AvRtpSumTotalFlows_Object((1,3,6,1,4,1,6889,2,7,3,1,6),_AvRtpSumTotalFlows_Type())
avRtpSumTotalFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumTotalFlows.setStatus(_A)
_AvRtpSumTotalFlowsQoSEvents_Type=Counter32
_AvRtpSumTotalFlowsQoSEvents_Object=MibTableColumn
avRtpSumTotalFlowsQoSEvents=_AvRtpSumTotalFlowsQoSEvents_Object((1,3,6,1,4,1,6889,2,7,3,1,7),_AvRtpSumTotalFlowsQoSEvents_Type())
avRtpSumTotalFlowsQoSEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumTotalFlowsQoSEvents.setStatus(_A)
class _AvRtpSumTxTTL_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvRtpSumTxTTL_Type.__name__=_C
_AvRtpSumTxTTL_Object=MibTableColumn
avRtpSumTxTTL=_AvRtpSumTxTTL_Object((1,3,6,1,4,1,6889,2,7,3,1,8),_AvRtpSumTxTTL_Type())
avRtpSumTxTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumTxTTL.setStatus(_A)
_AvRtpSumSessionDuration_Type=Counter32
_AvRtpSumSessionDuration_Object=MibTableColumn
avRtpSumSessionDuration=_AvRtpSumSessionDuration_Object((1,3,6,1,4,1,6889,2,7,3,1,9),_AvRtpSumSessionDuration_Type())
avRtpSumSessionDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpSumSessionDuration.setStatus(_A)
_AvRtpSumClear_Type=TruthValue
_AvRtpSumClear_Object=MibTableColumn
avRtpSumClear=_AvRtpSumClear_Object((1,3,6,1,4,1,6889,2,7,3,1,10),_AvRtpSumClear_Type())
avRtpSumClear.setMaxAccess(_E)
if mibBuilder.loadTexts:avRtpSumClear.setStatus(_A)
_AvRtpLookupTable_Object=MibTable
avRtpLookupTable=_AvRtpLookupTable_Object((1,3,6,1,4,1,6889,2,7,4))
if mibBuilder.loadTexts:avRtpLookupTable.setStatus(_A)
_AvRtpLookupEntry_Object=MibTableRow
avRtpLookupEntry=_AvRtpLookupEntry_Object((1,3,6,1,4,1,6889,2,7,4,1))
avRtpLookupEntry.setIndexNames((0,_D,_a),(0,_D,_b),(0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:avRtpLookupEntry.setStatus(_A)
_AvRtpLookupStartTime_Type=DateAndTime
_AvRtpLookupStartTime_Object=MibTableColumn
avRtpLookupStartTime=_AvRtpLookupStartTime_Object((1,3,6,1,4,1,6889,2,7,4,1,1),_AvRtpLookupStartTime_Type())
avRtpLookupStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:avRtpLookupStartTime.setStatus(_A)
_AvRtpNotificationVarbinds_ObjectIdentity=ObjectIdentity
avRtpNotificationVarbinds=_AvRtpNotificationVarbinds_ObjectIdentity((1,3,6,1,4,1,6889,2,7,5))
if mibBuilder.loadTexts:avRtpNotificationVarbinds.setStatus(_A)
_AvRtpSessionLocInetAddrType_Type=InetAddressType
_AvRtpSessionLocInetAddrType_Object=MibScalar
avRtpSessionLocInetAddrType=_AvRtpSessionLocInetAddrType_Object((1,3,6,1,4,1,6889,2,7,5,1),_AvRtpSessionLocInetAddrType_Type())
avRtpSessionLocInetAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:avRtpSessionLocInetAddrType.setStatus(_A)
_AvRtpSessionLocInetAddr_Type=InetAddress
_AvRtpSessionLocInetAddr_Object=MibScalar
avRtpSessionLocInetAddr=_AvRtpSessionLocInetAddr_Object((1,3,6,1,4,1,6889,2,7,5,2),_AvRtpSessionLocInetAddr_Type())
avRtpSessionLocInetAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:avRtpSessionLocInetAddr.setStatus(_A)
_AvRtpSessionRemInetAddrType_Type=InetAddressType
_AvRtpSessionRemInetAddrType_Object=MibScalar
avRtpSessionRemInetAddrType=_AvRtpSessionRemInetAddrType_Object((1,3,6,1,4,1,6889,2,7,5,3),_AvRtpSessionRemInetAddrType_Type())
avRtpSessionRemInetAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:avRtpSessionRemInetAddrType.setStatus(_A)
_AvRtpSessionRemInetAddr_Type=InetAddress
_AvRtpSessionRemInetAddr_Object=MibScalar
avRtpSessionRemInetAddr=_AvRtpSessionRemInetAddr_Object((1,3,6,1,4,1,6889,2,7,5,4),_AvRtpSessionRemInetAddr_Type())
avRtpSessionRemInetAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:avRtpSessionRemInetAddr.setStatus(_A)
avRtpQoSTrap=NotificationType((1,3,6,1,4,1,6889,2,7,0,1))
avRtpQoSTrap.setObjects(*((_D,_c),(_D,_d),(_D,_K),(_D,_L),(_D,_M),(_D,_G),(_D,_N)))
if mibBuilder.loadTexts:avRtpQoSTrap.setStatus(_A)
avRtpQoSFault=NotificationType((1,3,6,1,4,1,6889,2,7,0,2))
avRtpQoSFault.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:avRtpQoSFault.setStatus(_A)
avRtpQoSClear=NotificationType((1,3,6,1,4,1,6889,2,7,0,3))
avRtpQoSClear.setObjects(*((_D,_O),(_D,_P),(_D,_G)))
if mibBuilder.loadTexts:avRtpQoSClear.setStatus(_A)
avRtpQoSInetTrap=NotificationType((1,3,6,1,4,1,6889,2,7,0,4))
avRtpQoSInetTrap.setObjects(*((_D,_e),(_D,_f),(_D,_g),(_D,_h),(_D,_K),(_D,_L),(_D,_M),(_D,_G),(_D,_N)))
if mibBuilder.loadTexts:avRtpQoSInetTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AvRtpItuPerceivedSeverity':AvRtpItuPerceivedSeverity,'AvRtpLoss':AvRtpLoss,'AvRtpSilenceSupp':AvRtpSilenceSupp,'avaya':avaya,'mibs':mibs,'avRtpMib':avRtpMib,'avRtpNotification':avRtpNotification,'avRtpQoSTrap':avRtpQoSTrap,'avRtpQoSFault':avRtpQoSFault,'avRtpQoSClear':avRtpQoSClear,'avRtpQoSInetTrap':avRtpQoSInetTrap,'avRtpConfig':avRtpConfig,'avRtpThresholdTable':avRtpThresholdTable,'avRtpThresholdEntry':avRtpThresholdEntry,_Y:avRtpThresholdSet,'avRtpThresholdMinStatWin':avRtpThresholdMinStatWin,'avRtpThresholdRxCodecLoss':avRtpThresholdRxCodecLoss,'avRtpThresholdRxAvgCodecLoss':avRtpThresholdRxAvgCodecLoss,'avRtpThresholdRxCodecLossEv':avRtpThresholdRxCodecLossEv,'avRtpThresholdCodecRtt':avRtpThresholdCodecRtt,'avRtpThresholdCodecRttEv':avRtpThresholdCodecRttEv,'avRtpThresholdEcReturnLoss':avRtpThresholdEcReturnLoss,'avRtpThresholdEcReturnLossEv':avRtpThresholdEcReturnLossEv,'avRtpThresholdRxLoss':avRtpThresholdRxLoss,'avRtpThresholdRxLossEv':avRtpThresholdRxLossEv,'avRtpThresholdRemLoss':avRtpThresholdRemLoss,'avRtpThresholdRemLossEv':avRtpThresholdRemLossEv,'avRtpThresholdAvgRxLoss':avRtpThresholdAvgRxLoss,'avRtpThresholdAvgRemLoss':avRtpThresholdAvgRemLoss,'avRtpThresholdRxJitter':avRtpThresholdRxJitter,'avRtpThresholdRxJitterEv':avRtpThresholdRxJitterEv,'avRtpThresholdRemJitter':avRtpThresholdRemJitter,'avRtpThresholdRemJitterEv':avRtpThresholdRemJitterEv,'avRtpThresholdRtt':avRtpThresholdRtt,'avRtpThresholdRttEv':avRtpThresholdRttEv,'avRtpThresholdRxSsrcChangeEv':avRtpThresholdRxSsrcChangeEv,'avRtpEnable':avRtpEnable,'avRtpQoSTrapEnable':avRtpQoSTrapEnable,'avRtpQoSFaultTrapEnable':avRtpQoSFaultTrapEnable,_O:avRtpQoSFaultTh,_P:avRtpQoSClearTh,'avRtpTxQoSTraps':avRtpTxQoSTraps,'avRtpQoSTrapsDrop':avRtpQoSTrapsDrop,'avRtpQoSTrapTokenInterval':avRtpQoSTrapTokenInterval,'avRtpQoSTrapBucketSize':avRtpQoSTrapBucketSize,'avRtpDateAndTime':avRtpDateAndTime,'avRtpMaxSessionTableSize':avRtpMaxSessionTableSize,'avRtpReservedSessionTableRows':avRtpReservedSessionTableRows,'avRtpClear':avRtpClear,'avRtpFaultMask':avRtpFaultMask,'avRtpSessionTable':avRtpSessionTable,'avRtpSessionEntry':avRtpSessionEntry,_I:avRtpSessionState,_J:avRtpSessionID,'avRtpSessionEngineID':avRtpSessionEngineID,'avRtpSessionLocAddrType':avRtpSessionLocAddrType,'avRtpSessionLocAddr':avRtpSessionLocAddr,_c:avRtpSessionLocAddrV4,'avRtpSessionLocAddrV6':avRtpSessionLocAddrV6,_a:avRtpSessionRemAddrType,_b:avRtpSessionRemAddr,_d:avRtpSessionRemAddrV4,'avRtpSessionRemAddrV6':avRtpSessionRemAddrV6,'avRtpSessionLocPort':avRtpSessionLocPort,'avRtpSessionRemPort':avRtpSessionRemPort,'avRtpSessionStartTime':avRtpSessionStartTime,'avRtpSessionEndTime':avRtpSessionEndTime,_K:avRtpSessionDuration,_L:avRtpSessionCname,_M:avRtpSessionPhone,_G:avRtpSessionSeverity,'avRtpSessionTxLen':avRtpSessionTxLen,'avRtpSessionType':avRtpSessionType,'avRtpSessionTxInterval':avRtpSessionTxInterval,'avRtpSessionTxEncryp':avRtpSessionTxEncryp,'avRtpSessionTxDscp':avRtpSessionTxDscp,'avRtpSessionTxVlan':avRtpSessionTxVlan,'avRtpSessionTxL2Pri':avRtpSessionTxL2Pri,'avRtpSessionTxSilenceSupp':avRtpSessionTxSilenceSupp,'avRtpSessionTxSsrc':avRtpSessionTxSsrc,'avRtpSessionTxRsvp':avRtpSessionTxRsvp,'avRtpSessionTxResvFail':avRtpSessionTxResvFail,'avRtpSessionStatInterval':avRtpSessionStatInterval,'avRtpSessionRxCodecPlayTime':avRtpSessionRxCodecPlayTime,'avRtpSessionRxCodecLossCount':avRtpSessionRxCodecLossCount,'avRtpSessionRxCodecLoss':avRtpSessionRxCodecLoss,'avRtpSessionRxAvgCodecLoss':avRtpSessionRxAvgCodecLoss,'avRtpSessionRxCodecLossEv':avRtpSessionRxCodecLossEv,'avRtpSessionRxLoss':avRtpSessionRxLoss,'avRtpSessionRxAvgLoss':avRtpSessionRxAvgLoss,'avRtpSessionRxLossEv':avRtpSessionRxLossEv,'avRtpSessionRx':avRtpSessionRx,'avRtpSessionRxLossCount':avRtpSessionRxLossCount,'avRtpSessionRxSeqFall':avRtpSessionRxSeqFall,'avRtpSessionRxDup':avRtpSessionRxDup,'avRtpSessionRxJBufUnderruns':avRtpSessionRxJBufUnderruns,'avRtpSessionRxJBufOverruns':avRtpSessionRxJBufOverruns,'avRtpSessionRxJBufDelay':avRtpSessionRxJBufDelay,'avRtpSessionRxMaxJBufDelay':avRtpSessionRxMaxJBufDelay,'avRtpSessionRxJitter':avRtpSessionRxJitter,'avRtpSessionRxAvgJitter':avRtpSessionRxAvgJitter,'avRtpSessionRxJitterEv':avRtpSessionRxJitterEv,'avRtpSessionRxTtl':avRtpSessionRxTtl,'avRtpSessionRxMinTtl':avRtpSessionRxMinTtl,'avRtpSessionRxMaxTtl':avRtpSessionRxMaxTtl,'avRtpSessionRxDscp':avRtpSessionRxDscp,'avRtpSessionRxL2Pri':avRtpSessionRxL2Pri,'avRtpSessionRxSilenceSupp':avRtpSessionRxSilenceSupp,'avRtpSessionRxSsrc':avRtpSessionRxSsrc,'avRtpSessionRxSsrcChange':avRtpSessionRxSsrcChange,'avRtpSessionTxRtcp':avRtpSessionTxRtcp,'avRtpSessionRxRtcp':avRtpSessionRxRtcp,'avRtpSessionCodecRtt':avRtpSessionCodecRtt,'avRtpSessionAvgCodecRtt':avRtpSessionAvgCodecRtt,'avRtpSessionCodecRttEv':avRtpSessionCodecRttEv,'avRtpSessionRtt':avRtpSessionRtt,'avRtpSessionAvgRtt':avRtpSessionAvgRtt,'avRtpSessionRttEv':avRtpSessionRttEv,'avRtpSessionRemLoss':avRtpSessionRemLoss,'avRtpSessionRemAvgLoss':avRtpSessionRemAvgLoss,'avRtpSessionRemLossEv':avRtpSessionRemLossEv,'avRtpSessionRemJitter':avRtpSessionRemJitter,'avRtpSessionRemAvgJitter':avRtpSessionRemAvgJitter,'avRtpSessionRemJitterEv':avRtpSessionRemJitterEv,'avRtpSessionEcTailLen':avRtpSessionEcTailLen,'avRtpSessionEcReturnLoss':avRtpSessionEcReturnLoss,'avRtpSessionEcReturnLossEv':avRtpSessionEcReturnLossEv,'avRtpSessionAEC':avRtpSessionAEC,_N:avRtpSessionDebugStr,'avRtpSessionTxFlowLabel':avRtpSessionTxFlowLabel,'avRtpSessionRxFlowLabel':avRtpSessionRxFlowLabel,'avRtpSumTable':avRtpSumTable,'avRtpSumEntry':avRtpSumEntry,_Z:avRtpSumEngineID,'avRtpSumEngineDescr':avRtpSumEngineDescr,'avRtpSumPeriod':avRtpSumPeriod,'avRtpSumActiveFlows':avRtpSumActiveFlows,'avRtpSumActiveQosEvents':avRtpSumActiveQosEvents,'avRtpSumTotalFlows':avRtpSumTotalFlows,'avRtpSumTotalFlowsQoSEvents':avRtpSumTotalFlowsQoSEvents,'avRtpSumTxTTL':avRtpSumTxTTL,'avRtpSumSessionDuration':avRtpSumSessionDuration,'avRtpSumClear':avRtpSumClear,'avRtpLookupTable':avRtpLookupTable,'avRtpLookupEntry':avRtpLookupEntry,'avRtpLookupStartTime':avRtpLookupStartTime,'avRtpNotificationVarbinds':avRtpNotificationVarbinds,_e:avRtpSessionLocInetAddrType,_f:avRtpSessionLocInetAddr,_g:avRtpSessionRemInetAddrType,_h:avRtpSessionRemInetAddr})