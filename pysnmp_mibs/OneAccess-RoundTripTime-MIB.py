_u='oacRttControlOperOverThresholdOccurred'
_t='oacRttControlOperTimeoutOccurred'
_s='oacRttControlOperConnLostOccurred'
_r='oacRttLatestRttOperEntry'
_q='oacRttReactTriggerOperEntry'
_p='oacRttControlOperEntry'
_o='oacRttStatisticsEntry'
_n='oacRttReactEntry'
_m='oacRttSchedEntry'
_l='oacRttHistoryEntry'
_k='oacRttApplSuppProtocols'
_j='oacRttApplSuppRttTypes'
_i='oacRttStatsJitterHopIndex'
_h='oacRttStatsJitterPathIndex'
_g='oacRttStatsCaptureDistIndex'
_f='oacRttHistoryCollectionSampleIndex'
_e='oacRttHistoryCollectionBucketIndex'
_d='oacRttHistoryCollectionLifeIndex'
_c='oacRttReactTriggerOacRttControlIndex'
_b='active'
_a='pending'
_Z='OacRttProtocol'
_Y='OacRttRttType'
_X='ipIcmpEcho'
_W='notApplicable'
_V='pathEcho'
_U='overThreshold'
_T='RowStatus'
_S='TimeTicks'
_R='OwnerString'
_Q='oacRttStatsCaptureHopIndex'
_P='oacRttStatsCapturePathIndex'
_O='OacRttTargetAddress'
_N='DisplayString'
_M='oacRttHistoryCollectionAddress'
_L='oacRttControlTag'
_K='oacRttStatsCaptureStartTimeIndex'
_J='seconds'
_I='TruthValue'
_H='milliseconds'
_G='oacRttControlIndex'
_F='not-accessible'
_E='read-create'
_D='OneAccess-RoundTripTime-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('IF-MIB',_R)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
oacExpIMManagement,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_S,'Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress',_T,'TextualConvention','TimeInterval','TimeStamp',_I)
oacRttChkMIB=ModuleIdentity((1,3,6,1,4,1,13191,10,3,4,1223))
if mibBuilder.loadTexts:oacRttChkMIB.setRevisions(('2011-07-29 00:00','2011-06-15 00:00','2010-07-08 10:00'))
class RttResponseSense(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,16)));namedValues=NamedValues(*(('ok',1),('disconnected',2),(_U,3),('timeout',4),('busy',5),('notConnected',6),('dropped',7),('sequenceError',8),('verifyError',9),('applicationSpecific',10),('error',16)))
class OacRttRttType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('echo',1),(_V,2)))
class OacRttProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
class OacRttTargetAddress(TextualConvention,OctetString):status=_A
class OacRttApplType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('echo',1),(_V,2),('fileIO',3),('script',4),('udpEcho',5),('tcpConnect',6),('http',7),('dns',8),('jitter',9),('dlsw',10),('dhcp',11),('ftp',12)))
class OacRttApplProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*((_W,1),(_X,2),('ipUdpEchoAppl',3),('snaRUEcho',4),('snaLU0EchoAppl',5),('snaLU2EchoAppl',6),('snaLU62Echo',7),('snaLU62EchoAppl',8),('appleTalkEcho',9),('appleTalkEchoAppl',10),('decNetEcho',11),('decNetEchoAppl',12),('ipxEcho',13),('ipxEchoAppl',14),('isoClnsEcho',15),('isoClnsEchoAppl',16),('vinesEcho',17),('vinesEchoAppl',18),('xnsEcho',19),('xnsEchoAppl',20),('apolloEcho',21),('apolloEchoAppl',22),('netbiosEchoAppl',23),('ipTcpConn',24),('httpAppl',25),('dnsAppl',26),('jitterAppl',27),('dlswAppl',28),('dhcpAppl',29),('ftpAppl',30)))
_OacRttChkObj_ObjectIdentity=ObjectIdentity
oacRttChkObj=_OacRttChkObj_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,1))
_OacRttControl_ObjectIdentity=ObjectIdentity
oacRttControl=_OacRttControl_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,1,1))
_OacRttControlTable_Object=MibTable
oacRttControlTable=_OacRttControlTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1))
if mibBuilder.loadTexts:oacRttControlTable.setStatus(_A)
_OacRttControlEntry_Object=MibTableRow
oacRttControlEntry=_OacRttControlEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1))
oacRttControlEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:oacRttControlEntry.setStatus(_A)
class _OacRttControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttControlIndex_Type.__name__=_C
_OacRttControlIndex_Object=MibTableColumn
oacRttControlIndex=_OacRttControlIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,1),_OacRttControlIndex_Type())
oacRttControlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttControlIndex.setStatus(_A)
_OacRttControlStatus_Type=RowStatus
_OacRttControlStatus_Object=MibTableColumn
oacRttControlStatus=_OacRttControlStatus_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,2),_OacRttControlStatus_Type())
oacRttControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlStatus.setStatus(_A)
class _OacRttControlTag_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OacRttControlTag_Type.__name__=_N
_OacRttControlTag_Object=MibTableColumn
oacRttControlTag=_OacRttControlTag_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,3),_OacRttControlTag_Type())
oacRttControlTag.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlTag.setStatus(_A)
class _OacRttControlFrequency_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_OacRttControlFrequency_Type.__name__=_C
_OacRttControlFrequency_Object=MibTableColumn
oacRttControlFrequency=_OacRttControlFrequency_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,4),_OacRttControlFrequency_Type())
oacRttControlFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlFrequency.setStatus(_A)
if mibBuilder.loadTexts:oacRttControlFrequency.setUnits(_J)
class _OacRttControlRttType_Type(OacRttRttType):defaultValue=1
_OacRttControlRttType_Type.__name__=_Y
_OacRttControlRttType_Object=MibTableColumn
oacRttControlRttType=_OacRttControlRttType_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,5),_OacRttControlRttType_Type())
oacRttControlRttType.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlRttType.setStatus(_A)
class _OacRttControlTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_OacRttControlTimeout_Type.__name__=_C
_OacRttControlTimeout_Object=MibTableColumn
oacRttControlTimeout=_OacRttControlTimeout_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,6),_OacRttControlTimeout_Type())
oacRttControlTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlTimeout.setStatus(_A)
if mibBuilder.loadTexts:oacRttControlTimeout.setUnits(_H)
class _OacRttControlOwner_Type(OwnerString):defaultValue=OctetString('')
_OacRttControlOwner_Type.__name__=_R
_OacRttControlOwner_Object=MibTableColumn
oacRttControlOwner=_OacRttControlOwner_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,7),_OacRttControlOwner_Type())
oacRttControlOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlOwner.setStatus(_A)
class _OacRttControlThreshold_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttControlThreshold_Type.__name__=_C
_OacRttControlThreshold_Object=MibTableColumn
oacRttControlThreshold=_OacRttControlThreshold_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,1,1,8),_OacRttControlThreshold_Type())
oacRttControlThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttControlThreshold.setStatus(_A)
if mibBuilder.loadTexts:oacRttControlThreshold.setUnits(_H)
_OacRttEchoTable_Object=MibTable
oacRttEchoTable=_OacRttEchoTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2))
if mibBuilder.loadTexts:oacRttEchoTable.setStatus(_A)
_OacRttEchoEntry_Object=MibTableRow
oacRttEchoEntry=_OacRttEchoEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1))
oacRttEchoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:oacRttEchoEntry.setStatus(_A)
class _OacRttEchoSourceAddress_Type(OacRttTargetAddress):defaultValue=OctetString('')
_OacRttEchoSourceAddress_Type.__name__=_O
_OacRttEchoSourceAddress_Object=MibTableColumn
oacRttEchoSourceAddress=_OacRttEchoSourceAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,1),_OacRttEchoSourceAddress_Type())
oacRttEchoSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoSourceAddress.setStatus(_A)
class _OacRttEchoTargetAddress_Type(OacRttTargetAddress):defaultValue=OctetString('')
_OacRttEchoTargetAddress_Type.__name__=_O
_OacRttEchoTargetAddress_Object=MibTableColumn
oacRttEchoTargetAddress=_OacRttEchoTargetAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,2),_OacRttEchoTargetAddress_Type())
oacRttEchoTargetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoTargetAddress.setStatus(_A)
class _OacRttEchoPktDataRequestSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_OacRttEchoPktDataRequestSize_Type.__name__=_C
_OacRttEchoPktDataRequestSize_Object=MibTableColumn
oacRttEchoPktDataRequestSize=_OacRttEchoPktDataRequestSize_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,3),_OacRttEchoPktDataRequestSize_Type())
oacRttEchoPktDataRequestSize.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoPktDataRequestSize.setStatus(_A)
if mibBuilder.loadTexts:oacRttEchoPktDataRequestSize.setUnits('octets')
class _OacRttEchoPktDataResponseSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_OacRttEchoPktDataResponseSize_Type.__name__=_C
_OacRttEchoPktDataResponseSize_Object=MibTableColumn
oacRttEchoPktDataResponseSize=_OacRttEchoPktDataResponseSize_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,4),_OacRttEchoPktDataResponseSize_Type())
oacRttEchoPktDataResponseSize.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoPktDataResponseSize.setStatus(_A)
class _OacRttEchoTOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OacRttEchoTOS_Type.__name__=_C
_OacRttEchoTOS_Object=MibTableColumn
oacRttEchoTOS=_OacRttEchoTOS_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,5),_OacRttEchoTOS_Type())
oacRttEchoTOS.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoTOS.setStatus(_A)
class _OacRttEchoProtocol_Type(OacRttProtocol):defaultValue=1
_OacRttEchoProtocol_Type.__name__=_Z
_OacRttEchoProtocol_Object=MibTableColumn
oacRttEchoProtocol=_OacRttEchoProtocol_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,2,1,6),_OacRttEchoProtocol_Type())
oacRttEchoProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttEchoProtocol.setStatus(_A)
_OacRttHistoryTable_Object=MibTable
oacRttHistoryTable=_OacRttHistoryTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3))
if mibBuilder.loadTexts:oacRttHistoryTable.setStatus(_A)
_OacRttHistoryEntry_Object=MibTableRow
oacRttHistoryEntry=_OacRttHistoryEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3,1))
if mibBuilder.loadTexts:oacRttHistoryEntry.setStatus(_A)
class _OacRttHistoryNumBuckets_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_OacRttHistoryNumBuckets_Type.__name__=_C
_OacRttHistoryNumBuckets_Object=MibTableColumn
oacRttHistoryNumBuckets=_OacRttHistoryNumBuckets_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3,1,1),_OacRttHistoryNumBuckets_Type())
oacRttHistoryNumBuckets.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttHistoryNumBuckets.setStatus(_A)
class _OacRttHistoryFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('all',2),(_U,3),('failures',4)))
_OacRttHistoryFilter_Type.__name__=_C
_OacRttHistoryFilter_Object=MibTableColumn
oacRttHistoryFilter=_OacRttHistoryFilter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3,1,2),_OacRttHistoryFilter_Type())
oacRttHistoryFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttHistoryFilter.setStatus(_A)
class _OacRttHistoryNumLives_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_OacRttHistoryNumLives_Type.__name__=_C
_OacRttHistoryNumLives_Object=MibTableColumn
oacRttHistoryNumLives=_OacRttHistoryNumLives_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3,1,3),_OacRttHistoryNumLives_Type())
oacRttHistoryNumLives.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttHistoryNumLives.setStatus(_A)
class _OacRttHistoryNumSamples_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_OacRttHistoryNumSamples_Type.__name__=_C
_OacRttHistoryNumSamples_Object=MibTableColumn
oacRttHistoryNumSamples=_OacRttHistoryNumSamples_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,3,1,4),_OacRttHistoryNumSamples_Type())
oacRttHistoryNumSamples.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttHistoryNumSamples.setStatus(_A)
_OacRttSchedTable_Object=MibTable
oacRttSchedTable=_OacRttSchedTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,4))
if mibBuilder.loadTexts:oacRttSchedTable.setStatus(_A)
_OacRttSchedEntry_Object=MibTableRow
oacRttSchedEntry=_OacRttSchedEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,4,1))
if mibBuilder.loadTexts:oacRttSchedEntry.setStatus(_A)
class _OacRttSchedRttStartTime_Type(TimeTicks):defaultValue=0
_OacRttSchedRttStartTime_Type.__name__=_S
_OacRttSchedRttStartTime_Object=MibTableColumn
oacRttSchedRttStartTime=_OacRttSchedRttStartTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,4,1,1),_OacRttSchedRttStartTime_Type())
oacRttSchedRttStartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttSchedRttStartTime.setStatus(_A)
class _OacRttSchedRttLife_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttSchedRttLife_Type.__name__=_C
_OacRttSchedRttLife_Object=MibTableColumn
oacRttSchedRttLife=_OacRttSchedRttLife_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,4,1,2),_OacRttSchedRttLife_Type())
oacRttSchedRttLife.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttSchedRttLife.setStatus(_A)
if mibBuilder.loadTexts:oacRttSchedRttLife.setUnits(_J)
class _OacRttSchedConceptRowAgeout_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2073600))
_OacRttSchedConceptRowAgeout_Type.__name__=_C
_OacRttSchedConceptRowAgeout_Object=MibTableColumn
oacRttSchedConceptRowAgeout=_OacRttSchedConceptRowAgeout_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,4,1,3),_OacRttSchedConceptRowAgeout_Type())
oacRttSchedConceptRowAgeout.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttSchedConceptRowAgeout.setStatus(_A)
if mibBuilder.loadTexts:oacRttSchedConceptRowAgeout.setUnits(_J)
_OacRttReactTable_Object=MibTable
oacRttReactTable=_OacRttReactTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5))
if mibBuilder.loadTexts:oacRttReactTable.setStatus(_A)
_OacRttReactEntry_Object=MibTableRow
oacRttReactEntry=_OacRttReactEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1))
if mibBuilder.loadTexts:oacRttReactEntry.setStatus(_A)
class _OacRttReactActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',1),('trapOnly',2),('nmvtOnly',3),('triggerOnly',4),('trapAndNmvt',5),('trapAndTrigger',6),('nmvtAndTrigger',7),('trapNmvtAndTrigger',8)))
_OacRttReactActionType_Type.__name__=_C
_OacRttReactActionType_Object=MibTableColumn
oacRttReactActionType=_OacRttReactActionType_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,1),_OacRttReactActionType_Type())
oacRttReactActionType.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactActionType.setStatus(_A)
class _OacRttReactThresholdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('never',1),('immediate',2),('consecutive',3),('xOfy',4),('average',5)))
_OacRttReactThresholdType_Type.__name__=_C
_OacRttReactThresholdType_Object=MibTableColumn
oacRttReactThresholdType=_OacRttReactThresholdType_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,2),_OacRttReactThresholdType_Type())
oacRttReactThresholdType.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactThresholdType.setStatus(_A)
class _OacRttReactThresholdCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_OacRttReactThresholdCount_Type.__name__=_C
_OacRttReactThresholdCount_Object=MibTableColumn
oacRttReactThresholdCount=_OacRttReactThresholdCount_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,3),_OacRttReactThresholdCount_Type())
oacRttReactThresholdCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactThresholdCount.setStatus(_A)
class _OacRttReactThresholdCount2_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_OacRttReactThresholdCount2_Type.__name__=_C
_OacRttReactThresholdCount2_Object=MibTableColumn
oacRttReactThresholdCount2=_OacRttReactThresholdCount2_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,4),_OacRttReactThresholdCount2_Type())
oacRttReactThresholdCount2.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactThresholdCount2.setStatus(_A)
class _OacRttReactConnectionEnable_Type(TruthValue):defaultValue=2
_OacRttReactConnectionEnable_Type.__name__=_I
_OacRttReactConnectionEnable_Object=MibTableColumn
oacRttReactConnectionEnable=_OacRttReactConnectionEnable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,5),_OacRttReactConnectionEnable_Type())
oacRttReactConnectionEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactConnectionEnable.setStatus(_A)
class _OacRttReactVerifyErrorEnable_Type(TruthValue):defaultValue=2
_OacRttReactVerifyErrorEnable_Type.__name__=_I
_OacRttReactVerifyErrorEnable_Object=MibTableColumn
oacRttReactVerifyErrorEnable=_OacRttReactVerifyErrorEnable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,6),_OacRttReactVerifyErrorEnable_Type())
oacRttReactVerifyErrorEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactVerifyErrorEnable.setStatus(_A)
class _OacRttReactThresholdFalling_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttReactThresholdFalling_Type.__name__=_C
_OacRttReactThresholdFalling_Object=MibTableColumn
oacRttReactThresholdFalling=_OacRttReactThresholdFalling_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,7),_OacRttReactThresholdFalling_Type())
oacRttReactThresholdFalling.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactThresholdFalling.setStatus(_A)
if mibBuilder.loadTexts:oacRttReactThresholdFalling.setUnits(_H)
class _OacRttReactTimeoutEnable_Type(TruthValue):defaultValue=2
_OacRttReactTimeoutEnable_Type.__name__=_I
_OacRttReactTimeoutEnable_Object=MibTableColumn
oacRttReactTimeoutEnable=_OacRttReactTimeoutEnable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,5,1,8),_OacRttReactTimeoutEnable_Type())
oacRttReactTimeoutEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactTimeoutEnable.setStatus(_A)
_OacRttStatisticsTable_Object=MibTable
oacRttStatisticsTable=_OacRttStatisticsTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6))
if mibBuilder.loadTexts:oacRttStatisticsTable.setStatus(_A)
_OacRttStatisticsEntry_Object=MibTableRow
oacRttStatisticsEntry=_OacRttStatisticsEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1))
if mibBuilder.loadTexts:oacRttStatisticsEntry.setStatus(_A)
class _OacRttStatisticsNumDistBuckets_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OacRttStatisticsNumDistBuckets_Type.__name__=_C
_OacRttStatisticsNumDistBuckets_Object=MibTableColumn
oacRttStatisticsNumDistBuckets=_OacRttStatisticsNumDistBuckets_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1,1),_OacRttStatisticsNumDistBuckets_Type())
oacRttStatisticsNumDistBuckets.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttStatisticsNumDistBuckets.setStatus(_A)
class _OacRttStatisticsNumHops_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_OacRttStatisticsNumHops_Type.__name__=_C
_OacRttStatisticsNumHops_Object=MibTableColumn
oacRttStatisticsNumHops=_OacRttStatisticsNumHops_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1,2),_OacRttStatisticsNumHops_Type())
oacRttStatisticsNumHops.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttStatisticsNumHops.setStatus(_A)
class _OacRttStatisticsNumPaths_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_OacRttStatisticsNumPaths_Type.__name__=_C
_OacRttStatisticsNumPaths_Object=MibTableColumn
oacRttStatisticsNumPaths=_OacRttStatisticsNumPaths_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1,3),_OacRttStatisticsNumPaths_Type())
oacRttStatisticsNumPaths.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttStatisticsNumPaths.setStatus(_A)
class _OacRttStatisticsDistInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OacRttStatisticsDistInterval_Type.__name__=_C
_OacRttStatisticsDistInterval_Object=MibTableColumn
oacRttStatisticsDistInterval=_OacRttStatisticsDistInterval_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1,4),_OacRttStatisticsDistInterval_Type())
oacRttStatisticsDistInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttStatisticsDistInterval.setStatus(_A)
if mibBuilder.loadTexts:oacRttStatisticsDistInterval.setUnits(_H)
class _OacRttStatisticsNumHourGroups_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_OacRttStatisticsNumHourGroups_Type.__name__=_C
_OacRttStatisticsNumHourGroups_Object=MibTableColumn
oacRttStatisticsNumHourGroups=_OacRttStatisticsNumHourGroups_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,6,1,5),_OacRttStatisticsNumHourGroups_Type())
oacRttStatisticsNumHourGroups.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttStatisticsNumHourGroups.setStatus(_A)
_OacRttControlOperTable_Object=MibTable
oacRttControlOperTable=_OacRttControlOperTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7))
if mibBuilder.loadTexts:oacRttControlOperTable.setStatus(_A)
_OacRttControlOperEntry_Object=MibTableRow
oacRttControlOperEntry=_OacRttControlOperEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1))
if mibBuilder.loadTexts:oacRttControlOperEntry.setStatus(_A)
class _OacRttControlOperNumRtts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttControlOperNumRtts_Type.__name__=_C
_OacRttControlOperNumRtts_Object=MibTableColumn
oacRttControlOperNumRtts=_OacRttControlOperNumRtts_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,1),_OacRttControlOperNumRtts_Type())
oacRttControlOperNumRtts.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperNumRtts.setStatus(_A)
_OacRttControlOperOctetsInUse_Type=Gauge32
_OacRttControlOperOctetsInUse_Object=MibTableColumn
oacRttControlOperOctetsInUse=_OacRttControlOperOctetsInUse_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,2),_OacRttControlOperOctetsInUse_Type())
oacRttControlOperOctetsInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperOctetsInUse.setStatus(_A)
class _OacRttControlOperDiagText_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,51))
_OacRttControlOperDiagText_Type.__name__=_N
_OacRttControlOperDiagText_Object=MibTableColumn
oacRttControlOperDiagText=_OacRttControlOperDiagText_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,3),_OacRttControlOperDiagText_Type())
oacRttControlOperDiagText.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperDiagText.setStatus(_A)
class _OacRttControlOperOverThresholdOccurred_Type(TruthValue):defaultValue=2
_OacRttControlOperOverThresholdOccurred_Type.__name__=_I
_OacRttControlOperOverThresholdOccurred_Object=MibTableColumn
oacRttControlOperOverThresholdOccurred=_OacRttControlOperOverThresholdOccurred_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,4),_OacRttControlOperOverThresholdOccurred_Type())
oacRttControlOperOverThresholdOccurred.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperOverThresholdOccurred.setStatus(_A)
class _OacRttControlOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('reset',1),('orderlyStop',2),('immediateStop',3),(_a,4),('inactive',5),(_b,6),('restart',7)))
_OacRttControlOperState_Type.__name__=_C
_OacRttControlOperState_Object=MibTableColumn
oacRttControlOperState=_OacRttControlOperState_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,5),_OacRttControlOperState_Type())
oacRttControlOperState.setMaxAccess('read-write')
if mibBuilder.loadTexts:oacRttControlOperState.setStatus(_A)
class _OacRttControlOperTimeoutOccurred_Type(TruthValue):defaultValue=2
_OacRttControlOperTimeoutOccurred_Type.__name__=_I
_OacRttControlOperTimeoutOccurred_Object=MibTableColumn
oacRttControlOperTimeoutOccurred=_OacRttControlOperTimeoutOccurred_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,6),_OacRttControlOperTimeoutOccurred_Type())
oacRttControlOperTimeoutOccurred.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperTimeoutOccurred.setStatus(_A)
class _OacRttControlOperRttLife_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttControlOperRttLife_Type.__name__=_C
_OacRttControlOperRttLife_Object=MibTableColumn
oacRttControlOperRttLife=_OacRttControlOperRttLife_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,7),_OacRttControlOperRttLife_Type())
oacRttControlOperRttLife.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperRttLife.setStatus(_A)
if mibBuilder.loadTexts:oacRttControlOperRttLife.setUnits(_J)
_OacRttControlOperModificationTime_Type=TimeStamp
_OacRttControlOperModificationTime_Object=MibTableColumn
oacRttControlOperModificationTime=_OacRttControlOperModificationTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,8),_OacRttControlOperModificationTime_Type())
oacRttControlOperModificationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperModificationTime.setStatus(_A)
class _OacRttControlOperConnLostOccurred_Type(TruthValue):defaultValue=2
_OacRttControlOperConnLostOccurred_Type.__name__=_I
_OacRttControlOperConnLostOccurred_Object=MibTableColumn
oacRttControlOperConnLostOccurred=_OacRttControlOperConnLostOccurred_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,9),_OacRttControlOperConnLostOccurred_Type())
oacRttControlOperConnLostOccurred.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperConnLostOccurred.setStatus(_A)
_OacRttControlOperResetTime_Type=TimeStamp
_OacRttControlOperResetTime_Object=MibTableColumn
oacRttControlOperResetTime=_OacRttControlOperResetTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,7,1,10),_OacRttControlOperResetTime_Type())
oacRttControlOperResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttControlOperResetTime.setStatus(_A)
_OacRttReactTriggerTable_Object=MibTable
oacRttReactTriggerTable=_OacRttReactTriggerTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,8))
if mibBuilder.loadTexts:oacRttReactTriggerTable.setStatus(_A)
_OacRttReactTriggerEntry_Object=MibTableRow
oacRttReactTriggerEntry=_OacRttReactTriggerEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,8,1))
oacRttReactTriggerEntry.setIndexNames((0,_D,_G),(0,_D,_c))
if mibBuilder.loadTexts:oacRttReactTriggerEntry.setStatus(_A)
class _OacRttReactTriggerOacRttControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttReactTriggerOacRttControlIndex_Type.__name__=_C
_OacRttReactTriggerOacRttControlIndex_Object=MibTableColumn
oacRttReactTriggerOacRttControlIndex=_OacRttReactTriggerOacRttControlIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,8,1,1),_OacRttReactTriggerOacRttControlIndex_Type())
oacRttReactTriggerOacRttControlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttReactTriggerOacRttControlIndex.setStatus(_A)
class _OacRttReactTriggerStatus_Type(RowStatus):defaultValue=4
_OacRttReactTriggerStatus_Type.__name__=_T
_OacRttReactTriggerStatus_Object=MibTableColumn
oacRttReactTriggerStatus=_OacRttReactTriggerStatus_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,8,1,2),_OacRttReactTriggerStatus_Type())
oacRttReactTriggerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oacRttReactTriggerStatus.setStatus(_A)
_OacRttReactTriggerOperTable_Object=MibTable
oacRttReactTriggerOperTable=_OacRttReactTriggerOperTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,9))
if mibBuilder.loadTexts:oacRttReactTriggerOperTable.setStatus(_A)
_OacRttReactTriggerOperEntry_Object=MibTableRow
oacRttReactTriggerOperEntry=_OacRttReactTriggerOperEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,9,1))
if mibBuilder.loadTexts:oacRttReactTriggerOperEntry.setStatus(_A)
class _OacRttReactTriggerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_b,1),(_a,2)))
_OacRttReactTriggerOperState_Type.__name__=_C
_OacRttReactTriggerOperState_Object=MibTableColumn
oacRttReactTriggerOperState=_OacRttReactTriggerOperState_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,9,1,1),_OacRttReactTriggerOperState_Type())
oacRttReactTriggerOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttReactTriggerOperState.setStatus(_A)
_OacRttLatestRttOperTable_Object=MibTable
oacRttLatestRttOperTable=_OacRttLatestRttOperTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10))
if mibBuilder.loadTexts:oacRttLatestRttOperTable.setStatus(_A)
_OacRttLatestRttOperEntry_Object=MibTableRow
oacRttLatestRttOperEntry=_OacRttLatestRttOperEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1))
if mibBuilder.loadTexts:oacRttLatestRttOperEntry.setStatus(_A)
_OacRttLatestRttOperTime_Type=TimeStamp
_OacRttLatestRttOperTime_Object=MibTableColumn
oacRttLatestRttOperTime=_OacRttLatestRttOperTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,1),_OacRttLatestRttOperTime_Type())
oacRttLatestRttOperTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperTime.setStatus(_A)
_OacRttLatestRttOperSense_Type=RttResponseSense
_OacRttLatestRttOperSense_Object=MibTableColumn
oacRttLatestRttOperSense=_OacRttLatestRttOperSense_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,2),_OacRttLatestRttOperSense_Type())
oacRttLatestRttOperSense.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperSense.setStatus(_A)
_OacRttLatestRttOperSenseDescription_Type=DisplayString
_OacRttLatestRttOperSenseDescription_Object=MibTableColumn
oacRttLatestRttOperSenseDescription=_OacRttLatestRttOperSenseDescription_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,3),_OacRttLatestRttOperSenseDescription_Type())
oacRttLatestRttOperSenseDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperSenseDescription.setStatus(_A)
_OacRttLatestRttOperAddress_Type=OacRttTargetAddress
_OacRttLatestRttOperAddress_Object=MibTableColumn
oacRttLatestRttOperAddress=_OacRttLatestRttOperAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,4),_OacRttLatestRttOperAddress_Type())
oacRttLatestRttOperAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperAddress.setStatus(_A)
_OacRttLatestRttOperCompletionTime_Type=Gauge32
_OacRttLatestRttOperCompletionTime_Object=MibTableColumn
oacRttLatestRttOperCompletionTime=_OacRttLatestRttOperCompletionTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,5),_OacRttLatestRttOperCompletionTime_Type())
oacRttLatestRttOperCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperCompletionTime.setStatus(_A)
if mibBuilder.loadTexts:oacRttLatestRttOperCompletionTime.setUnits(_H)
class _OacRttLatestRttOperApplSpecificSense_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,2147483647))
_OacRttLatestRttOperApplSpecificSense_Type.__name__=_C
_OacRttLatestRttOperApplSpecificSense_Object=MibTableColumn
oacRttLatestRttOperApplSpecificSense=_OacRttLatestRttOperApplSpecificSense_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,1,10,1,6),_OacRttLatestRttOperApplSpecificSense_Type())
oacRttLatestRttOperApplSpecificSense.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttLatestRttOperApplSpecificSense.setStatus(_A)
_OacRttHistory_ObjectIdentity=ObjectIdentity
oacRttHistory=_OacRttHistory_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,1,2))
_OacRttHistoryCollectionTable_Object=MibTable
oacRttHistoryCollectionTable=_OacRttHistoryCollectionTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1))
if mibBuilder.loadTexts:oacRttHistoryCollectionTable.setStatus(_A)
_OacRttHistoryCollectionEntry_Object=MibTableRow
oacRttHistoryCollectionEntry=_OacRttHistoryCollectionEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1))
oacRttHistoryCollectionEntry.setIndexNames((0,_D,_G),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:oacRttHistoryCollectionEntry.setStatus(_A)
class _OacRttHistoryCollectionLifeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttHistoryCollectionLifeIndex_Type.__name__=_C
_OacRttHistoryCollectionLifeIndex_Object=MibTableColumn
oacRttHistoryCollectionLifeIndex=_OacRttHistoryCollectionLifeIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,1),_OacRttHistoryCollectionLifeIndex_Type())
oacRttHistoryCollectionLifeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttHistoryCollectionLifeIndex.setStatus(_A)
class _OacRttHistoryCollectionBucketIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttHistoryCollectionBucketIndex_Type.__name__=_C
_OacRttHistoryCollectionBucketIndex_Object=MibTableColumn
oacRttHistoryCollectionBucketIndex=_OacRttHistoryCollectionBucketIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,2),_OacRttHistoryCollectionBucketIndex_Type())
oacRttHistoryCollectionBucketIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttHistoryCollectionBucketIndex.setStatus(_A)
class _OacRttHistoryCollectionSampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_OacRttHistoryCollectionSampleIndex_Type.__name__=_C
_OacRttHistoryCollectionSampleIndex_Object=MibTableColumn
oacRttHistoryCollectionSampleIndex=_OacRttHistoryCollectionSampleIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,3),_OacRttHistoryCollectionSampleIndex_Type())
oacRttHistoryCollectionSampleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttHistoryCollectionSampleIndex.setStatus(_A)
class _OacRttHistoryCollectionApplSpecificSense_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1001,2147483647))
_OacRttHistoryCollectionApplSpecificSense_Type.__name__=_C
_OacRttHistoryCollectionApplSpecificSense_Object=MibTableColumn
oacRttHistoryCollectionApplSpecificSense=_OacRttHistoryCollectionApplSpecificSense_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,4),_OacRttHistoryCollectionApplSpecificSense_Type())
oacRttHistoryCollectionApplSpecificSense.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionApplSpecificSense.setStatus(_A)
_OacRttHistoryCollectionAddress_Type=OacRttTargetAddress
_OacRttHistoryCollectionAddress_Object=MibTableColumn
oacRttHistoryCollectionAddress=_OacRttHistoryCollectionAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,5),_OacRttHistoryCollectionAddress_Type())
oacRttHistoryCollectionAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionAddress.setStatus(_A)
_OacRttHistoryCollectionSampleTime_Type=TimeStamp
_OacRttHistoryCollectionSampleTime_Object=MibTableColumn
oacRttHistoryCollectionSampleTime=_OacRttHistoryCollectionSampleTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,6),_OacRttHistoryCollectionSampleTime_Type())
oacRttHistoryCollectionSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionSampleTime.setStatus(_A)
_OacRttHistoryCollectionSense_Type=RttResponseSense
_OacRttHistoryCollectionSense_Object=MibTableColumn
oacRttHistoryCollectionSense=_OacRttHistoryCollectionSense_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,7),_OacRttHistoryCollectionSense_Type())
oacRttHistoryCollectionSense.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionSense.setStatus(_A)
_OacRttHistoryCollectionSenseDescription_Type=DisplayString
_OacRttHistoryCollectionSenseDescription_Object=MibTableColumn
oacRttHistoryCollectionSenseDescription=_OacRttHistoryCollectionSenseDescription_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,8),_OacRttHistoryCollectionSenseDescription_Type())
oacRttHistoryCollectionSenseDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionSenseDescription.setStatus(_A)
_OacRttHistoryCollectionCompletionTime_Type=Gauge32
_OacRttHistoryCollectionCompletionTime_Object=MibTableColumn
oacRttHistoryCollectionCompletionTime=_OacRttHistoryCollectionCompletionTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,2,1,1,9),_OacRttHistoryCollectionCompletionTime_Type())
oacRttHistoryCollectionCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttHistoryCollectionCompletionTime.setStatus(_A)
if mibBuilder.loadTexts:oacRttHistoryCollectionCompletionTime.setUnits(_H)
_OacRttStats_ObjectIdentity=ObjectIdentity
oacRttStats=_OacRttStats_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,1,3))
_OacRttStatsCollectTable_Object=MibTable
oacRttStatsCollectTable=_OacRttStatsCollectTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1))
if mibBuilder.loadTexts:oacRttStatsCollectTable.setStatus(_A)
_OacRttStatsCollectEntry_Object=MibTableRow
oacRttStatsCollectEntry=_OacRttStatsCollectEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1))
oacRttStatsCollectEntry.setIndexNames((0,_D,_G),(0,_D,_K),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:oacRttStatsCollectEntry.setStatus(_A)
_OacRttStatsCollectAddress_Type=OacRttTargetAddress
_OacRttStatsCollectAddress_Object=MibTableColumn
oacRttStatsCollectAddress=_OacRttStatsCollectAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,1),_OacRttStatsCollectAddress_Type())
oacRttStatsCollectAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectAddress.setStatus(_A)
class _OacRttStatsCollectNoConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectNoConnections_Type.__name__=_C
_OacRttStatsCollectNoConnections_Object=MibTableColumn
oacRttStatsCollectNoConnections=_OacRttStatsCollectNoConnections_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,2),_OacRttStatsCollectNoConnections_Type())
oacRttStatsCollectNoConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectNoConnections.setStatus(_A)
class _OacRttStatsCollectBusies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectBusies_Type.__name__=_C
_OacRttStatsCollectBusies_Object=MibTableColumn
oacRttStatsCollectBusies=_OacRttStatsCollectBusies_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,3),_OacRttStatsCollectBusies_Type())
oacRttStatsCollectBusies.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectBusies.setStatus(_A)
class _OacRttStatsCollectTimeouts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectTimeouts_Type.__name__=_C
_OacRttStatsCollectTimeouts_Object=MibTableColumn
oacRttStatsCollectTimeouts=_OacRttStatsCollectTimeouts_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,4),_OacRttStatsCollectTimeouts_Type())
oacRttStatsCollectTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectTimeouts.setStatus(_A)
class _OacRttStatsCollectSequenceErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectSequenceErrors_Type.__name__=_C
_OacRttStatsCollectSequenceErrors_Object=MibTableColumn
oacRttStatsCollectSequenceErrors=_OacRttStatsCollectSequenceErrors_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,5),_OacRttStatsCollectSequenceErrors_Type())
oacRttStatsCollectSequenceErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectSequenceErrors.setStatus(_A)
class _OacRttStatsCollectNumDisconnects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectNumDisconnects_Type.__name__=_C
_OacRttStatsCollectNumDisconnects_Object=MibTableColumn
oacRttStatsCollectNumDisconnects=_OacRttStatsCollectNumDisconnects_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,6),_OacRttStatsCollectNumDisconnects_Type())
oacRttStatsCollectNumDisconnects.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectNumDisconnects.setStatus(_A)
class _OacRttStatsCollectVerifyErrors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectVerifyErrors_Type.__name__=_C
_OacRttStatsCollectVerifyErrors_Object=MibTableColumn
oacRttStatsCollectVerifyErrors=_OacRttStatsCollectVerifyErrors_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,7),_OacRttStatsCollectVerifyErrors_Type())
oacRttStatsCollectVerifyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectVerifyErrors.setStatus(_A)
class _OacRttStatsCollectDrops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCollectDrops_Type.__name__=_C
_OacRttStatsCollectDrops_Object=MibTableColumn
oacRttStatsCollectDrops=_OacRttStatsCollectDrops_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,1,1,8),_OacRttStatsCollectDrops_Type())
oacRttStatsCollectDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCollectDrops.setStatus(_A)
_OacRttStatsCaptureTable_Object=MibTable
oacRttStatsCaptureTable=_OacRttStatsCaptureTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2))
if mibBuilder.loadTexts:oacRttStatsCaptureTable.setStatus(_A)
_OacRttStatsCaptureEntry_Object=MibTableRow
oacRttStatsCaptureEntry=_OacRttStatsCaptureEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1))
oacRttStatsCaptureEntry.setIndexNames((0,_D,_G),(0,_D,_K),(0,_D,_P),(0,_D,_Q),(0,_D,_g))
if mibBuilder.loadTexts:oacRttStatsCaptureEntry.setStatus(_A)
_OacRttStatsCaptureStartTimeIndex_Type=TimeStamp
_OacRttStatsCaptureStartTimeIndex_Object=MibTableColumn
oacRttStatsCaptureStartTimeIndex=_OacRttStatsCaptureStartTimeIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,1),_OacRttStatsCaptureStartTimeIndex_Type())
oacRttStatsCaptureStartTimeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsCaptureStartTimeIndex.setStatus(_A)
class _OacRttStatsCapturePathIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_OacRttStatsCapturePathIndex_Type.__name__=_C
_OacRttStatsCapturePathIndex_Object=MibTableColumn
oacRttStatsCapturePathIndex=_OacRttStatsCapturePathIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,2),_OacRttStatsCapturePathIndex_Type())
oacRttStatsCapturePathIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsCapturePathIndex.setStatus(_A)
class _OacRttStatsCaptureHopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_OacRttStatsCaptureHopIndex_Type.__name__=_C
_OacRttStatsCaptureHopIndex_Object=MibTableColumn
oacRttStatsCaptureHopIndex=_OacRttStatsCaptureHopIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,3),_OacRttStatsCaptureHopIndex_Type())
oacRttStatsCaptureHopIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsCaptureHopIndex.setStatus(_A)
class _OacRttStatsCaptureDistIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_OacRttStatsCaptureDistIndex_Type.__name__=_C
_OacRttStatsCaptureDistIndex_Object=MibTableColumn
oacRttStatsCaptureDistIndex=_OacRttStatsCaptureDistIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,4),_OacRttStatsCaptureDistIndex_Type())
oacRttStatsCaptureDistIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsCaptureDistIndex.setStatus(_A)
_OacRttStatsCaptureSumCompletionTime_Type=Gauge32
_OacRttStatsCaptureSumCompletionTime_Object=MibTableColumn
oacRttStatsCaptureSumCompletionTime=_OacRttStatsCaptureSumCompletionTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,5),_OacRttStatsCaptureSumCompletionTime_Type())
oacRttStatsCaptureSumCompletionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureSumCompletionTime.setStatus(_A)
if mibBuilder.loadTexts:oacRttStatsCaptureSumCompletionTime.setUnits(_H)
_OacRttStatsCaptureSumCompletionTime2Low_Type=Gauge32
_OacRttStatsCaptureSumCompletionTime2Low_Object=MibTableColumn
oacRttStatsCaptureSumCompletionTime2Low=_OacRttStatsCaptureSumCompletionTime2Low_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,6),_OacRttStatsCaptureSumCompletionTime2Low_Type())
oacRttStatsCaptureSumCompletionTime2Low.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureSumCompletionTime2Low.setStatus(_A)
_OacRttStatsCaptureSumCompletionTime2High_Type=Gauge32
_OacRttStatsCaptureSumCompletionTime2High_Object=MibTableColumn
oacRttStatsCaptureSumCompletionTime2High=_OacRttStatsCaptureSumCompletionTime2High_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,7),_OacRttStatsCaptureSumCompletionTime2High_Type())
oacRttStatsCaptureSumCompletionTime2High.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureSumCompletionTime2High.setStatus(_A)
_OacRttStatsCaptureCompletionTimeMin_Type=Gauge32
_OacRttStatsCaptureCompletionTimeMin_Object=MibTableColumn
oacRttStatsCaptureCompletionTimeMin=_OacRttStatsCaptureCompletionTimeMin_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,8),_OacRttStatsCaptureCompletionTimeMin_Type())
oacRttStatsCaptureCompletionTimeMin.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureCompletionTimeMin.setStatus(_A)
if mibBuilder.loadTexts:oacRttStatsCaptureCompletionTimeMin.setUnits(_H)
_OacRttStatsCaptureCompletionTimeMax_Type=Gauge32
_OacRttStatsCaptureCompletionTimeMax_Object=MibTableColumn
oacRttStatsCaptureCompletionTimeMax=_OacRttStatsCaptureCompletionTimeMax_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,9),_OacRttStatsCaptureCompletionTimeMax_Type())
oacRttStatsCaptureCompletionTimeMax.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureCompletionTimeMax.setStatus(_A)
if mibBuilder.loadTexts:oacRttStatsCaptureCompletionTimeMax.setUnits(_H)
class _OacRttStatsCaptureOverThresholds_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCaptureOverThresholds_Type.__name__=_C
_OacRttStatsCaptureOverThresholds_Object=MibTableColumn
oacRttStatsCaptureOverThresholds=_OacRttStatsCaptureOverThresholds_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,10),_OacRttStatsCaptureOverThresholds_Type())
oacRttStatsCaptureOverThresholds.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureOverThresholds.setStatus(_A)
class _OacRttStatsCaptureCompletions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsCaptureCompletions_Type.__name__=_C
_OacRttStatsCaptureCompletions_Object=MibTableColumn
oacRttStatsCaptureCompletions=_OacRttStatsCaptureCompletions_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,2,1,11),_OacRttStatsCaptureCompletions_Type())
oacRttStatsCaptureCompletions.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsCaptureCompletions.setStatus(_A)
_OacRttStatsTotalsTable_Object=MibTable
oacRttStatsTotalsTable=_OacRttStatsTotalsTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,3))
if mibBuilder.loadTexts:oacRttStatsTotalsTable.setStatus(_A)
_OacRttStatsTotalsEntry_Object=MibTableRow
oacRttStatsTotalsEntry=_OacRttStatsTotalsEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,3,1))
oacRttStatsTotalsEntry.setIndexNames((0,_D,_G),(0,_D,_K))
if mibBuilder.loadTexts:oacRttStatsTotalsEntry.setStatus(_A)
class _OacRttStatsTotalsInitiations_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OacRttStatsTotalsInitiations_Type.__name__=_C
_OacRttStatsTotalsInitiations_Object=MibTableColumn
oacRttStatsTotalsInitiations=_OacRttStatsTotalsInitiations_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,3,1,1),_OacRttStatsTotalsInitiations_Type())
oacRttStatsTotalsInitiations.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsTotalsInitiations.setStatus(_A)
_OacRttStatsTotalsElapsedTime_Type=TimeInterval
_OacRttStatsTotalsElapsedTime_Object=MibTableColumn
oacRttStatsTotalsElapsedTime=_OacRttStatsTotalsElapsedTime_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,3,1,2),_OacRttStatsTotalsElapsedTime_Type())
oacRttStatsTotalsElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsTotalsElapsedTime.setStatus(_A)
_OacRttStatsJitterHopTable_Object=MibTable
oacRttStatsJitterHopTable=_OacRttStatsJitterHopTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4))
if mibBuilder.loadTexts:oacRttStatsJitterHopTable.setStatus(_A)
_OacRttStatsJitterHopEntry_Object=MibTableRow
oacRttStatsJitterHopEntry=_OacRttStatsJitterHopEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1))
oacRttStatsJitterHopEntry.setIndexNames((0,_D,_G),(0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:oacRttStatsJitterHopEntry.setStatus(_A)
class _OacRttStatsJitterPathIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttStatsJitterPathIndex_Type.__name__=_C
_OacRttStatsJitterPathIndex_Object=MibTableColumn
oacRttStatsJitterPathIndex=_OacRttStatsJitterPathIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,1),_OacRttStatsJitterPathIndex_Type())
oacRttStatsJitterPathIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsJitterPathIndex.setStatus(_A)
class _OacRttStatsJitterHopIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacRttStatsJitterHopIndex_Type.__name__=_C
_OacRttStatsJitterHopIndex_Object=MibTableColumn
oacRttStatsJitterHopIndex=_OacRttStatsJitterHopIndex_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,2),_OacRttStatsJitterHopIndex_Type())
oacRttStatsJitterHopIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttStatsJitterHopIndex.setStatus(_A)
_OacRttStatsJitterHopIpAddress_Type=InetAddress
_OacRttStatsJitterHopIpAddress_Object=MibTableColumn
oacRttStatsJitterHopIpAddress=_OacRttStatsJitterHopIpAddress_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,3),_OacRttStatsJitterHopIpAddress_Type())
oacRttStatsJitterHopIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopIpAddress.setStatus(_A)
_OacRttStatsJitterHopRTT_Type=Integer32
_OacRttStatsJitterHopRTT_Object=MibTableColumn
oacRttStatsJitterHopRTT=_OacRttStatsJitterHopRTT_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,4),_OacRttStatsJitterHopRTT_Type())
oacRttStatsJitterHopRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopRTT.setStatus(_A)
_OacRttStatsJitterHopPacketLoss_Type=Integer32
_OacRttStatsJitterHopPacketLoss_Object=MibTableColumn
oacRttStatsJitterHopPacketLoss=_OacRttStatsJitterHopPacketLoss_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,5),_OacRttStatsJitterHopPacketLoss_Type())
oacRttStatsJitterHopPacketLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopPacketLoss.setStatus(_A)
_OacRttStatsJitterHopJitter_Type=Integer32
_OacRttStatsJitterHopJitter_Object=MibTableColumn
oacRttStatsJitterHopJitter=_OacRttStatsJitterHopJitter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,6),_OacRttStatsJitterHopJitter_Type())
oacRttStatsJitterHopJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopJitter.setStatus(_A)
_OacRttStatsJitterHopMinRTT_Type=Integer32
_OacRttStatsJitterHopMinRTT_Object=MibTableColumn
oacRttStatsJitterHopMinRTT=_OacRttStatsJitterHopMinRTT_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,7),_OacRttStatsJitterHopMinRTT_Type())
oacRttStatsJitterHopMinRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMinRTT.setStatus(_A)
_OacRttStatsJitterHopMaxRTT_Type=Integer32
_OacRttStatsJitterHopMaxRTT_Object=MibTableColumn
oacRttStatsJitterHopMaxRTT=_OacRttStatsJitterHopMaxRTT_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,8),_OacRttStatsJitterHopMaxRTT_Type())
oacRttStatsJitterHopMaxRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMaxRTT.setStatus(_A)
_OacRttStatsJitterHopSumRTT_Type=Integer32
_OacRttStatsJitterHopSumRTT_Object=MibTableColumn
oacRttStatsJitterHopSumRTT=_OacRttStatsJitterHopSumRTT_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,9),_OacRttStatsJitterHopSumRTT_Type())
oacRttStatsJitterHopSumRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSumRTT.setStatus(_A)
_OacRttStatsJitterHopSum2RTT_Type=Integer32
_OacRttStatsJitterHopSum2RTT_Object=MibTableColumn
oacRttStatsJitterHopSum2RTT=_OacRttStatsJitterHopSum2RTT_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,10),_OacRttStatsJitterHopSum2RTT_Type())
oacRttStatsJitterHopSum2RTT.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSum2RTT.setStatus(_A)
_OacRttStatsJitterHopMinPosJitter_Type=Integer32
_OacRttStatsJitterHopMinPosJitter_Object=MibTableColumn
oacRttStatsJitterHopMinPosJitter=_OacRttStatsJitterHopMinPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,11),_OacRttStatsJitterHopMinPosJitter_Type())
oacRttStatsJitterHopMinPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMinPosJitter.setStatus(_A)
_OacRttStatsJitterHopMaxPosJitter_Type=Integer32
_OacRttStatsJitterHopMaxPosJitter_Object=MibTableColumn
oacRttStatsJitterHopMaxPosJitter=_OacRttStatsJitterHopMaxPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,12),_OacRttStatsJitterHopMaxPosJitter_Type())
oacRttStatsJitterHopMaxPosJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMaxPosJitter.setStatus(_A)
_OacRttStatsJitterHopSumPos_Type=Integer32
_OacRttStatsJitterHopSumPos_Object=MibTableColumn
oacRttStatsJitterHopSumPos=_OacRttStatsJitterHopSumPos_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,13),_OacRttStatsJitterHopSumPos_Type())
oacRttStatsJitterHopSumPos.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSumPos.setStatus(_A)
_OacRttStatsJitterHopSum2Pos_Type=Integer32
_OacRttStatsJitterHopSum2Pos_Object=MibTableColumn
oacRttStatsJitterHopSum2Pos=_OacRttStatsJitterHopSum2Pos_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,14),_OacRttStatsJitterHopSum2Pos_Type())
oacRttStatsJitterHopSum2Pos.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSum2Pos.setStatus(_A)
_OacRttStatsJitterHopMinNegJitter_Type=Integer32
_OacRttStatsJitterHopMinNegJitter_Object=MibTableColumn
oacRttStatsJitterHopMinNegJitter=_OacRttStatsJitterHopMinNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,15),_OacRttStatsJitterHopMinNegJitter_Type())
oacRttStatsJitterHopMinNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMinNegJitter.setStatus(_A)
_OacRttStatsJitterHopMaxNegJitter_Type=Integer32
_OacRttStatsJitterHopMaxNegJitter_Object=MibTableColumn
oacRttStatsJitterHopMaxNegJitter=_OacRttStatsJitterHopMaxNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,16),_OacRttStatsJitterHopMaxNegJitter_Type())
oacRttStatsJitterHopMaxNegJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopMaxNegJitter.setStatus(_A)
_OacRttStatsJitterHopSumNeg_Type=Integer32
_OacRttStatsJitterHopSumNeg_Object=MibTableColumn
oacRttStatsJitterHopSumNeg=_OacRttStatsJitterHopSumNeg_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,17),_OacRttStatsJitterHopSumNeg_Type())
oacRttStatsJitterHopSumNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSumNeg.setStatus(_A)
_OacRttStatsJitterHopSum2Neg_Type=Integer32
_OacRttStatsJitterHopSum2Neg_Object=MibTableColumn
oacRttStatsJitterHopSum2Neg=_OacRttStatsJitterHopSum2Neg_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,18),_OacRttStatsJitterHopSum2Neg_Type())
oacRttStatsJitterHopSum2Neg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopSum2Neg.setStatus(_A)
_OacRttStatsJitterHopOutOfSequence_Type=Integer32
_OacRttStatsJitterHopOutOfSequence_Object=MibTableColumn
oacRttStatsJitterHopOutOfSequence=_OacRttStatsJitterHopOutOfSequence_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,19),_OacRttStatsJitterHopOutOfSequence_Type())
oacRttStatsJitterHopOutOfSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopOutOfSequence.setStatus(_A)
_OacRttStatsJitterHopDiscardedSamples_Type=Integer32
_OacRttStatsJitterHopDiscardedSamples_Object=MibTableColumn
oacRttStatsJitterHopDiscardedSamples=_OacRttStatsJitterHopDiscardedSamples_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,3,4,1,20),_OacRttStatsJitterHopDiscardedSamples_Type())
oacRttStatsJitterHopDiscardedSamples.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttStatsJitterHopDiscardedSamples.setStatus(_A)
_OacRttAppl_ObjectIdentity=ObjectIdentity
oacRttAppl=_OacRttAppl_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,1,4))
_OacRttApplVersion_Type=DisplayString
_OacRttApplVersion_Object=MibScalar
oacRttApplVersion=_OacRttApplVersion_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,1),_OacRttApplVersion_Type())
oacRttApplVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttApplVersion.setStatus(_A)
_OacRttApplSuppRttTypesTable_Object=MibTable
oacRttApplSuppRttTypesTable=_OacRttApplSuppRttTypesTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,2))
if mibBuilder.loadTexts:oacRttApplSuppRttTypesTable.setStatus(_A)
_OacRttApplSuppRttTypesEntry_Object=MibTableRow
oacRttApplSuppRttTypesEntry=_OacRttApplSuppRttTypesEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,2,1))
oacRttApplSuppRttTypesEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:oacRttApplSuppRttTypesEntry.setStatus(_A)
_OacRttApplSuppRttTypes_Type=OacRttApplType
_OacRttApplSuppRttTypes_Object=MibTableColumn
oacRttApplSuppRttTypes=_OacRttApplSuppRttTypes_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,2,1,1),_OacRttApplSuppRttTypes_Type())
oacRttApplSuppRttTypes.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttApplSuppRttTypes.setStatus(_A)
_OacRttApplSuppRttTypesValid_Type=TruthValue
_OacRttApplSuppRttTypesValid_Object=MibTableColumn
oacRttApplSuppRttTypesValid=_OacRttApplSuppRttTypesValid_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,2,1,2),_OacRttApplSuppRttTypesValid_Type())
oacRttApplSuppRttTypesValid.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttApplSuppRttTypesValid.setStatus(_A)
_OacRttApplSuppProtocolsTable_Object=MibTable
oacRttApplSuppProtocolsTable=_OacRttApplSuppProtocolsTable_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,3))
if mibBuilder.loadTexts:oacRttApplSuppProtocolsTable.setStatus(_A)
_OacRttApplSuppProtocolsEntry_Object=MibTableRow
oacRttApplSuppProtocolsEntry=_OacRttApplSuppProtocolsEntry_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,3,1))
oacRttApplSuppProtocolsEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:oacRttApplSuppProtocolsEntry.setStatus(_A)
_OacRttApplSuppProtocols_Type=OacRttApplProtocol
_OacRttApplSuppProtocols_Object=MibTableColumn
oacRttApplSuppProtocols=_OacRttApplSuppProtocols_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,3,1,1),_OacRttApplSuppProtocols_Type())
oacRttApplSuppProtocols.setMaxAccess(_F)
if mibBuilder.loadTexts:oacRttApplSuppProtocols.setStatus(_A)
_OacRttApplSuppProtocolsValid_Type=TruthValue
_OacRttApplSuppProtocolsValid_Object=MibTableColumn
oacRttApplSuppProtocolsValid=_OacRttApplSuppProtocolsValid_Object((1,3,6,1,4,1,13191,10,3,4,1223,1,4,3,1,2),_OacRttApplSuppProtocolsValid_Type())
oacRttApplSuppProtocolsValid.setMaxAccess(_B)
if mibBuilder.loadTexts:oacRttApplSuppProtocolsValid.setStatus(_A)
_OacRttNotificationsPrefix_ObjectIdentity=ObjectIdentity
oacRttNotificationsPrefix=_OacRttNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,2))
_OacRttNotifications_ObjectIdentity=ObjectIdentity
oacRttNotifications=_OacRttNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1223,2,0))
oacRttControlEntry.registerAugmentions((_D,_l))
oacRttHistoryEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions((_D,_m))
oacRttSchedEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions((_D,_n))
oacRttReactEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions((_D,_o))
oacRttStatisticsEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttControlEntry.registerAugmentions((_D,_p))
oacRttControlOperEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttReactTriggerEntry.registerAugmentions((_D,_q))
oacRttReactTriggerOperEntry.setIndexNames(*oacRttReactTriggerEntry.getIndexNames())
oacRttControlEntry.registerAugmentions((_D,_r))
oacRttLatestRttOperEntry.setIndexNames(*oacRttControlEntry.getIndexNames())
oacRttConnectionChangeNotification=NotificationType((1,3,6,1,4,1,13191,10,3,4,1223,2,0,1))
oacRttConnectionChangeNotification.setObjects(*((_D,_L),(_D,_M),(_D,_s)))
if mibBuilder.loadTexts:oacRttConnectionChangeNotification.setStatus(_A)
oacRttTimeoutNotification=NotificationType((1,3,6,1,4,1,13191,10,3,4,1223,2,0,2))
oacRttTimeoutNotification.setObjects(*((_D,_L),(_D,_M),(_D,_t)))
if mibBuilder.loadTexts:oacRttTimeoutNotification.setStatus(_A)
oacRttThresholdNotification=NotificationType((1,3,6,1,4,1,13191,10,3,4,1223,2,0,3))
oacRttThresholdNotification.setObjects(*((_D,_L),(_D,_M),(_D,_u)))
if mibBuilder.loadTexts:oacRttThresholdNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'RttResponseSense':RttResponseSense,_Y:OacRttRttType,_Z:OacRttProtocol,_O:OacRttTargetAddress,'OacRttApplType':OacRttApplType,'OacRttApplProtocol':OacRttApplProtocol,'oacRttChkMIB':oacRttChkMIB,'oacRttChkObj':oacRttChkObj,'oacRttControl':oacRttControl,'oacRttControlTable':oacRttControlTable,'oacRttControlEntry':oacRttControlEntry,_G:oacRttControlIndex,'oacRttControlStatus':oacRttControlStatus,_L:oacRttControlTag,'oacRttControlFrequency':oacRttControlFrequency,'oacRttControlRttType':oacRttControlRttType,'oacRttControlTimeout':oacRttControlTimeout,'oacRttControlOwner':oacRttControlOwner,'oacRttControlThreshold':oacRttControlThreshold,'oacRttEchoTable':oacRttEchoTable,'oacRttEchoEntry':oacRttEchoEntry,'oacRttEchoSourceAddress':oacRttEchoSourceAddress,'oacRttEchoTargetAddress':oacRttEchoTargetAddress,'oacRttEchoPktDataRequestSize':oacRttEchoPktDataRequestSize,'oacRttEchoPktDataResponseSize':oacRttEchoPktDataResponseSize,'oacRttEchoTOS':oacRttEchoTOS,'oacRttEchoProtocol':oacRttEchoProtocol,'oacRttHistoryTable':oacRttHistoryTable,_l:oacRttHistoryEntry,'oacRttHistoryNumBuckets':oacRttHistoryNumBuckets,'oacRttHistoryFilter':oacRttHistoryFilter,'oacRttHistoryNumLives':oacRttHistoryNumLives,'oacRttHistoryNumSamples':oacRttHistoryNumSamples,'oacRttSchedTable':oacRttSchedTable,_m:oacRttSchedEntry,'oacRttSchedRttStartTime':oacRttSchedRttStartTime,'oacRttSchedRttLife':oacRttSchedRttLife,'oacRttSchedConceptRowAgeout':oacRttSchedConceptRowAgeout,'oacRttReactTable':oacRttReactTable,_n:oacRttReactEntry,'oacRttReactActionType':oacRttReactActionType,'oacRttReactThresholdType':oacRttReactThresholdType,'oacRttReactThresholdCount':oacRttReactThresholdCount,'oacRttReactThresholdCount2':oacRttReactThresholdCount2,'oacRttReactConnectionEnable':oacRttReactConnectionEnable,'oacRttReactVerifyErrorEnable':oacRttReactVerifyErrorEnable,'oacRttReactThresholdFalling':oacRttReactThresholdFalling,'oacRttReactTimeoutEnable':oacRttReactTimeoutEnable,'oacRttStatisticsTable':oacRttStatisticsTable,_o:oacRttStatisticsEntry,'oacRttStatisticsNumDistBuckets':oacRttStatisticsNumDistBuckets,'oacRttStatisticsNumHops':oacRttStatisticsNumHops,'oacRttStatisticsNumPaths':oacRttStatisticsNumPaths,'oacRttStatisticsDistInterval':oacRttStatisticsDistInterval,'oacRttStatisticsNumHourGroups':oacRttStatisticsNumHourGroups,'oacRttControlOperTable':oacRttControlOperTable,_p:oacRttControlOperEntry,'oacRttControlOperNumRtts':oacRttControlOperNumRtts,'oacRttControlOperOctetsInUse':oacRttControlOperOctetsInUse,'oacRttControlOperDiagText':oacRttControlOperDiagText,_u:oacRttControlOperOverThresholdOccurred,'oacRttControlOperState':oacRttControlOperState,_t:oacRttControlOperTimeoutOccurred,'oacRttControlOperRttLife':oacRttControlOperRttLife,'oacRttControlOperModificationTime':oacRttControlOperModificationTime,_s:oacRttControlOperConnLostOccurred,'oacRttControlOperResetTime':oacRttControlOperResetTime,'oacRttReactTriggerTable':oacRttReactTriggerTable,'oacRttReactTriggerEntry':oacRttReactTriggerEntry,_c:oacRttReactTriggerOacRttControlIndex,'oacRttReactTriggerStatus':oacRttReactTriggerStatus,'oacRttReactTriggerOperTable':oacRttReactTriggerOperTable,_q:oacRttReactTriggerOperEntry,'oacRttReactTriggerOperState':oacRttReactTriggerOperState,'oacRttLatestRttOperTable':oacRttLatestRttOperTable,_r:oacRttLatestRttOperEntry,'oacRttLatestRttOperTime':oacRttLatestRttOperTime,'oacRttLatestRttOperSense':oacRttLatestRttOperSense,'oacRttLatestRttOperSenseDescription':oacRttLatestRttOperSenseDescription,'oacRttLatestRttOperAddress':oacRttLatestRttOperAddress,'oacRttLatestRttOperCompletionTime':oacRttLatestRttOperCompletionTime,'oacRttLatestRttOperApplSpecificSense':oacRttLatestRttOperApplSpecificSense,'oacRttHistory':oacRttHistory,'oacRttHistoryCollectionTable':oacRttHistoryCollectionTable,'oacRttHistoryCollectionEntry':oacRttHistoryCollectionEntry,_d:oacRttHistoryCollectionLifeIndex,_e:oacRttHistoryCollectionBucketIndex,_f:oacRttHistoryCollectionSampleIndex,'oacRttHistoryCollectionApplSpecificSense':oacRttHistoryCollectionApplSpecificSense,_M:oacRttHistoryCollectionAddress,'oacRttHistoryCollectionSampleTime':oacRttHistoryCollectionSampleTime,'oacRttHistoryCollectionSense':oacRttHistoryCollectionSense,'oacRttHistoryCollectionSenseDescription':oacRttHistoryCollectionSenseDescription,'oacRttHistoryCollectionCompletionTime':oacRttHistoryCollectionCompletionTime,'oacRttStats':oacRttStats,'oacRttStatsCollectTable':oacRttStatsCollectTable,'oacRttStatsCollectEntry':oacRttStatsCollectEntry,'oacRttStatsCollectAddress':oacRttStatsCollectAddress,'oacRttStatsCollectNoConnections':oacRttStatsCollectNoConnections,'oacRttStatsCollectBusies':oacRttStatsCollectBusies,'oacRttStatsCollectTimeouts':oacRttStatsCollectTimeouts,'oacRttStatsCollectSequenceErrors':oacRttStatsCollectSequenceErrors,'oacRttStatsCollectNumDisconnects':oacRttStatsCollectNumDisconnects,'oacRttStatsCollectVerifyErrors':oacRttStatsCollectVerifyErrors,'oacRttStatsCollectDrops':oacRttStatsCollectDrops,'oacRttStatsCaptureTable':oacRttStatsCaptureTable,'oacRttStatsCaptureEntry':oacRttStatsCaptureEntry,_K:oacRttStatsCaptureStartTimeIndex,_P:oacRttStatsCapturePathIndex,_Q:oacRttStatsCaptureHopIndex,_g:oacRttStatsCaptureDistIndex,'oacRttStatsCaptureSumCompletionTime':oacRttStatsCaptureSumCompletionTime,'oacRttStatsCaptureSumCompletionTime2Low':oacRttStatsCaptureSumCompletionTime2Low,'oacRttStatsCaptureSumCompletionTime2High':oacRttStatsCaptureSumCompletionTime2High,'oacRttStatsCaptureCompletionTimeMin':oacRttStatsCaptureCompletionTimeMin,'oacRttStatsCaptureCompletionTimeMax':oacRttStatsCaptureCompletionTimeMax,'oacRttStatsCaptureOverThresholds':oacRttStatsCaptureOverThresholds,'oacRttStatsCaptureCompletions':oacRttStatsCaptureCompletions,'oacRttStatsTotalsTable':oacRttStatsTotalsTable,'oacRttStatsTotalsEntry':oacRttStatsTotalsEntry,'oacRttStatsTotalsInitiations':oacRttStatsTotalsInitiations,'oacRttStatsTotalsElapsedTime':oacRttStatsTotalsElapsedTime,'oacRttStatsJitterHopTable':oacRttStatsJitterHopTable,'oacRttStatsJitterHopEntry':oacRttStatsJitterHopEntry,_h:oacRttStatsJitterPathIndex,_i:oacRttStatsJitterHopIndex,'oacRttStatsJitterHopIpAddress':oacRttStatsJitterHopIpAddress,'oacRttStatsJitterHopRTT':oacRttStatsJitterHopRTT,'oacRttStatsJitterHopPacketLoss':oacRttStatsJitterHopPacketLoss,'oacRttStatsJitterHopJitter':oacRttStatsJitterHopJitter,'oacRttStatsJitterHopMinRTT':oacRttStatsJitterHopMinRTT,'oacRttStatsJitterHopMaxRTT':oacRttStatsJitterHopMaxRTT,'oacRttStatsJitterHopSumRTT':oacRttStatsJitterHopSumRTT,'oacRttStatsJitterHopSum2RTT':oacRttStatsJitterHopSum2RTT,'oacRttStatsJitterHopMinPosJitter':oacRttStatsJitterHopMinPosJitter,'oacRttStatsJitterHopMaxPosJitter':oacRttStatsJitterHopMaxPosJitter,'oacRttStatsJitterHopSumPos':oacRttStatsJitterHopSumPos,'oacRttStatsJitterHopSum2Pos':oacRttStatsJitterHopSum2Pos,'oacRttStatsJitterHopMinNegJitter':oacRttStatsJitterHopMinNegJitter,'oacRttStatsJitterHopMaxNegJitter':oacRttStatsJitterHopMaxNegJitter,'oacRttStatsJitterHopSumNeg':oacRttStatsJitterHopSumNeg,'oacRttStatsJitterHopSum2Neg':oacRttStatsJitterHopSum2Neg,'oacRttStatsJitterHopOutOfSequence':oacRttStatsJitterHopOutOfSequence,'oacRttStatsJitterHopDiscardedSamples':oacRttStatsJitterHopDiscardedSamples,'oacRttAppl':oacRttAppl,'oacRttApplVersion':oacRttApplVersion,'oacRttApplSuppRttTypesTable':oacRttApplSuppRttTypesTable,'oacRttApplSuppRttTypesEntry':oacRttApplSuppRttTypesEntry,_j:oacRttApplSuppRttTypes,'oacRttApplSuppRttTypesValid':oacRttApplSuppRttTypesValid,'oacRttApplSuppProtocolsTable':oacRttApplSuppProtocolsTable,'oacRttApplSuppProtocolsEntry':oacRttApplSuppProtocolsEntry,_k:oacRttApplSuppProtocols,'oacRttApplSuppProtocolsValid':oacRttApplSuppProtocolsValid,'oacRttNotificationsPrefix':oacRttNotificationsPrefix,'oacRttNotifications':oacRttNotifications,'oacRttConnectionChangeNotification':oacRttConnectionChangeNotification,'oacRttTimeoutNotification':oacRttTimeoutNotification,'oacRttThresholdNotification':oacRttThresholdNotification})