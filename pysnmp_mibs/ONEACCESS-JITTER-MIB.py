_Af='oacJitterGeneralGroup'
_Ae='oacJitterStatsHistoryDeviationDS'
_Ad='oacJitterStatsHistoryDeviationSD'
_Ac='oacJitterStatsHistorySum2NegDS'
_Ab='oacJitterStatsHistorySum2PosDS'
_Aa='oacJitterStatsHistorySum2NegSD'
_AZ='oacJitterStatsHistorySum2PosSD'
_AY='oacJitterStatsHistoryMaxNegDS'
_AX='oacJitterStatsHistoryMaxPosDS'
_AW='oacJitterStatsHistoryMaxNegSD'
_AV='oacJitterStatsHistoryMaxPosSD'
_AU='oacJitterStatsHistoryPacketLoss'
_AT='oacJitterStatsHistoryPacketLateArrival'
_AS='oacJitterStatsHistoryPacketOutOfSequence'
_AR='oacJitterStatsHistoryPacketLossDS'
_AQ='oacJitterStatsHistoryPacketLossSD'
_AP='oacJitterStatsHistoryNumNegDS'
_AO='oacJitterStatsHistorySumNegDS'
_AN='oacJitterStatsHistoryNumPosDS'
_AM='oacJitterStatsHistorySumPosDS'
_AL='oacJitterStatsHistoryNumNegSD'
_AK='oacJitterStatsHistorySumNegSD'
_AJ='oacJitterStatsHistoryNumPosSD'
_AI='oacJitterStatsHistorySumPosSD'
_AH='oacJitterStatsHistoryNumNegJitter'
_AG='oacJitterStatsHistorySumNegJitter'
_AF='oacJitterStatsHistoryNumPosJitter'
_AE='oacJitterStatsHistorySumPosJitter'
_AD='oacJitterStatsHistoryMaxRTT'
_AC='oacJitterStatsHistoryMinRTT'
_AB='oacJitterStatsHistorySumRTT'
_AA='oacJitterStatsHistoryAvgRTT'
_A9='oacJitterStatsHistoryPacketRecv'
_A8='oacJitterStatsHistoryNumRTT'
_A7='oacJitterStatsHistoryTime'
_A6='oacJitterStatsHistoryCompleted'
_A5='oacJitterStatsPacketLoss'
_A4='oacJitterStatsPacketLateArrival'
_A3='oacJitterStatsPacketOutOfSequence'
_A2='oacJitterStatsPacketLossDS'
_A1='oacJitterStatsPacketLossSD'
_A0='oacJitterStatsDeviationDS'
_z='oacJitterStatsDeviationSD'
_y='oacJitterStatsSum2NegDS'
_x='oacJitterStatsSum2PosDS'
_w='oacJitterStatsSum2NegSD'
_v='oacJitterStatsSum2PosSD'
_u='oacJitterStatsMaxNegDS'
_t='oacJitterStatsNumNegDS'
_s='oacJitterStatsSumNegDS'
_r='oacJitterStatsMaxPosDS'
_q='oacJitterStatsNumPosDS'
_p='oacJitterStatsSumPosDS'
_o='oacJitterStatsMaxNegSD'
_n='oacJitterStatsNumNegSD'
_m='oacJitterStatsSumNegSD'
_l='oacJitterStatsMaxPosSD'
_k='oacJitterStatsNumPosSD'
_j='oacJitterStatsSumPosSD'
_i='oacJitterStatsNumNegJitter'
_h='oacJitterStatsSumNegJitter'
_g='oacJitterStatsNumPosJitter'
_f='oacJitterStatsSumPosJitter'
_e='oacJitterStatsMaxRTT'
_d='oacJitterStatsMinRTT'
_c='oacJitterStatsSumRTT'
_b='oacJitterStatsAvgRTT'
_a='oacJitterStatsPacketRecv'
_Z='oacJitterStatsNumRTT'
_Y='oacJitterStatsTime'
_X='oacJitterStatsCompleted'
_W='oacJitterControlTos'
_V='oacJitterControlPacketCount'
_U='oacJitterControlPktDataRequestSize'
_T='oacJitterControlInterval'
_S='oacJitterControlSourceAddress'
_R='oacJitterControlTargetPort'
_Q='oacJitterControlTargetAddress'
_P='oacJitterControlStatus'
_O='oacJitterControlTimeout'
_N='oacJitterControlFrequency'
_M='oacJitterControlType'
_L='oacJitterControlOwner'
_K='oacJitterStatsHistoryIndex'
_J='milliseconds'
_I='OacJitterControlJitterType'
_H='OwnerString'
_G='OctetString'
_F='oacJitterControlIndex'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='ONEACCESS-JITTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OwnerString,=mibBuilder.importSymbols('IF-MIB',_H)
InetAddress,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress')
oacExpIMManagement,oacMIBModules,oacRequirements=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement','oacMIBModules','oacRequirements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
oacJitterMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2000))
if mibBuilder.loadTexts:oacJitterMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 10:00'))
class OacJitterControlJitterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('jitter-ICMP-TIMESTAMP',1),('jitter-UDP-PING',2),('jitter-UDP-PING-TIMESTAMP',3)))
class OacJitterResponseSense(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,16)));namedValues=NamedValues(*(('ok',1),('disconnected',2),('overThreshold',3),('timeout',4),('busy',5),('notConnected',6),('dropped',7),('sequenceError',8),('verifyError',9),('applicationSpecific',10),('noStatisticsAvailable',11),('error',16)))
_OacJitterConformance_ObjectIdentity=ObjectIdentity
oacJitterConformance=_OacJitterConformance_ObjectIdentity((1,3,6,1,4,1,13191,5,2000))
_OacJitterGroups_ObjectIdentity=ObjectIdentity
oacJitterGroups=_OacJitterGroups_ObjectIdentity((1,3,6,1,4,1,13191,5,2000,1))
_OacJitterCompliances_ObjectIdentity=ObjectIdentity
oacJitterCompliances=_OacJitterCompliances_ObjectIdentity((1,3,6,1,4,1,13191,5,2000,2))
_OacExpIMJitter_ObjectIdentity=ObjectIdentity
oacExpIMJitter=_OacExpIMJitter_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,5))
_OacJitterObjects_ObjectIdentity=ObjectIdentity
oacJitterObjects=_OacJitterObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,5,1))
_OacJitterControlTable_Object=MibTable
oacJitterControlTable=_OacJitterControlTable_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1))
if mibBuilder.loadTexts:oacJitterControlTable.setStatus(_A)
_OacJitterControlEntry_Object=MibTableRow
oacJitterControlEntry=_OacJitterControlEntry_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1))
oacJitterControlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:oacJitterControlEntry.setStatus(_A)
class _OacJitterControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OacJitterControlIndex_Type.__name__=_D
_OacJitterControlIndex_Object=MibTableColumn
oacJitterControlIndex=_OacJitterControlIndex_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,1),_OacJitterControlIndex_Type())
oacJitterControlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:oacJitterControlIndex.setStatus(_A)
class _OacJitterControlOwner_Type(OwnerString):defaultValue=OctetString('')
_OacJitterControlOwner_Type.__name__=_H
_OacJitterControlOwner_Object=MibTableColumn
oacJitterControlOwner=_OacJitterControlOwner_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,2),_OacJitterControlOwner_Type())
oacJitterControlOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlOwner.setStatus(_A)
class _OacJitterControlType_Type(OacJitterControlJitterType):defaultValue=1
_OacJitterControlType_Type.__name__=_I
_OacJitterControlType_Object=MibTableColumn
oacJitterControlType=_OacJitterControlType_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,3),_OacJitterControlType_Type())
oacJitterControlType.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlType.setStatus(_A)
class _OacJitterControlFrequency_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800))
_OacJitterControlFrequency_Type.__name__=_D
_OacJitterControlFrequency_Object=MibTableColumn
oacJitterControlFrequency=_OacJitterControlFrequency_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,4),_OacJitterControlFrequency_Type())
oacJitterControlFrequency.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlFrequency.setStatus(_A)
if mibBuilder.loadTexts:oacJitterControlFrequency.setUnits('seconds')
class _OacJitterControlTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_OacJitterControlTimeout_Type.__name__=_D
_OacJitterControlTimeout_Object=MibTableColumn
oacJitterControlTimeout=_OacJitterControlTimeout_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,5),_OacJitterControlTimeout_Type())
oacJitterControlTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlTimeout.setStatus(_A)
if mibBuilder.loadTexts:oacJitterControlTimeout.setUnits(_J)
_OacJitterControlTargetAddress_Type=InetAddress
_OacJitterControlTargetAddress_Object=MibTableColumn
oacJitterControlTargetAddress=_OacJitterControlTargetAddress_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,6),_OacJitterControlTargetAddress_Type())
oacJitterControlTargetAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlTargetAddress.setStatus(_A)
_OacJitterControlTargetPort_Type=Integer32
_OacJitterControlTargetPort_Object=MibTableColumn
oacJitterControlTargetPort=_OacJitterControlTargetPort_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,7),_OacJitterControlTargetPort_Type())
oacJitterControlTargetPort.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlTargetPort.setStatus(_A)
_OacJitterControlSourceAddress_Type=InetAddress
_OacJitterControlSourceAddress_Object=MibTableColumn
oacJitterControlSourceAddress=_OacJitterControlSourceAddress_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,8),_OacJitterControlSourceAddress_Type())
oacJitterControlSourceAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlSourceAddress.setStatus(_A)
_OacJitterControlInterval_Type=Integer32
_OacJitterControlInterval_Object=MibTableColumn
oacJitterControlInterval=_OacJitterControlInterval_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,9),_OacJitterControlInterval_Type())
oacJitterControlInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlInterval.setStatus(_A)
if mibBuilder.loadTexts:oacJitterControlInterval.setUnits(_J)
class _OacJitterControlPktDataRequestSize_Type(Integer32):defaultValue=32
_OacJitterControlPktDataRequestSize_Type.__name__=_D
_OacJitterControlPktDataRequestSize_Object=MibTableColumn
oacJitterControlPktDataRequestSize=_OacJitterControlPktDataRequestSize_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,10),_OacJitterControlPktDataRequestSize_Type())
oacJitterControlPktDataRequestSize.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlPktDataRequestSize.setStatus(_A)
if mibBuilder.loadTexts:oacJitterControlPktDataRequestSize.setUnits('bytes')
class _OacJitterControlPacketCount_Type(Integer32):defaultValue=10
_OacJitterControlPacketCount_Type.__name__=_D
_OacJitterControlPacketCount_Object=MibTableColumn
oacJitterControlPacketCount=_OacJitterControlPacketCount_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,11),_OacJitterControlPacketCount_Type())
oacJitterControlPacketCount.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlPacketCount.setStatus(_A)
class _OacJitterControlTos_Type(Integer32):defaultValue=0
_OacJitterControlTos_Type.__name__=_D
_OacJitterControlTos_Object=MibTableColumn
oacJitterControlTos=_OacJitterControlTos_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,12),_OacJitterControlTos_Type())
oacJitterControlTos.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlTos.setStatus(_A)
_OacJitterControlStatus_Type=RowStatus
_OacJitterControlStatus_Object=MibTableColumn
oacJitterControlStatus=_OacJitterControlStatus_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,13),_OacJitterControlStatus_Type())
oacJitterControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oacJitterControlStatus.setStatus(_A)
class _OacJitterControlVrfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacJitterControlVrfName_Type.__name__=_G
_OacJitterControlVrfName_Object=MibTableColumn
oacJitterControlVrfName=_OacJitterControlVrfName_Object((1,3,6,1,4,1,13191,10,3,4,5,1,1,1,14),_OacJitterControlVrfName_Type())
oacJitterControlVrfName.setMaxAccess('read-write')
if mibBuilder.loadTexts:oacJitterControlVrfName.setStatus(_A)
_OacJitterStatsTable_Object=MibTable
oacJitterStatsTable=_OacJitterStatsTable_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2))
if mibBuilder.loadTexts:oacJitterStatsTable.setStatus(_A)
_OacJitterStatsEntry_Object=MibTableRow
oacJitterStatsEntry=_OacJitterStatsEntry_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1))
oacJitterStatsEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:oacJitterStatsEntry.setStatus(_A)
_OacJitterStatsCompleted_Type=OacJitterResponseSense
_OacJitterStatsCompleted_Object=MibTableColumn
oacJitterStatsCompleted=_OacJitterStatsCompleted_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,2),_OacJitterStatsCompleted_Type())
oacJitterStatsCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsCompleted.setStatus(_A)
_OacJitterStatsTime_Type=DateAndTime
_OacJitterStatsTime_Object=MibTableColumn
oacJitterStatsTime=_OacJitterStatsTime_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,3),_OacJitterStatsTime_Type())
oacJitterStatsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsTime.setStatus(_A)
class _OacJitterStatsNumRTT_Type(Integer32):defaultValue=0
_OacJitterStatsNumRTT_Type.__name__=_D
_OacJitterStatsNumRTT_Object=MibTableColumn
oacJitterStatsNumRTT=_OacJitterStatsNumRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,4),_OacJitterStatsNumRTT_Type())
oacJitterStatsNumRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumRTT.setStatus(_A)
_OacJitterStatsPacketRecv_Type=Integer32
_OacJitterStatsPacketRecv_Object=MibTableColumn
oacJitterStatsPacketRecv=_OacJitterStatsPacketRecv_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,5),_OacJitterStatsPacketRecv_Type())
oacJitterStatsPacketRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketRecv.setStatus(_A)
_OacJitterStatsAvgRTT_Type=Integer32
_OacJitterStatsAvgRTT_Object=MibTableColumn
oacJitterStatsAvgRTT=_OacJitterStatsAvgRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,6),_OacJitterStatsAvgRTT_Type())
oacJitterStatsAvgRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsAvgRTT.setStatus(_A)
_OacJitterStatsSumRTT_Type=Integer32
_OacJitterStatsSumRTT_Object=MibTableColumn
oacJitterStatsSumRTT=_OacJitterStatsSumRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,7),_OacJitterStatsSumRTT_Type())
oacJitterStatsSumRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumRTT.setStatus(_A)
_OacJitterStatsMinRTT_Type=Integer32
_OacJitterStatsMinRTT_Object=MibTableColumn
oacJitterStatsMinRTT=_OacJitterStatsMinRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,8),_OacJitterStatsMinRTT_Type())
oacJitterStatsMinRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMinRTT.setStatus(_A)
_OacJitterStatsMaxRTT_Type=Integer32
_OacJitterStatsMaxRTT_Object=MibTableColumn
oacJitterStatsMaxRTT=_OacJitterStatsMaxRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,9),_OacJitterStatsMaxRTT_Type())
oacJitterStatsMaxRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMaxRTT.setStatus(_A)
_OacJitterStatsSumPosJitter_Type=Integer32
_OacJitterStatsSumPosJitter_Object=MibTableColumn
oacJitterStatsSumPosJitter=_OacJitterStatsSumPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,10),_OacJitterStatsSumPosJitter_Type())
oacJitterStatsSumPosJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumPosJitter.setStatus(_A)
_OacJitterStatsNumPosJitter_Type=Integer32
_OacJitterStatsNumPosJitter_Object=MibTableColumn
oacJitterStatsNumPosJitter=_OacJitterStatsNumPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,11),_OacJitterStatsNumPosJitter_Type())
oacJitterStatsNumPosJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumPosJitter.setStatus(_A)
_OacJitterStatsSumNegJitter_Type=Integer32
_OacJitterStatsSumNegJitter_Object=MibTableColumn
oacJitterStatsSumNegJitter=_OacJitterStatsSumNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,12),_OacJitterStatsSumNegJitter_Type())
oacJitterStatsSumNegJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumNegJitter.setStatus(_A)
_OacJitterStatsNumNegJitter_Type=Integer32
_OacJitterStatsNumNegJitter_Object=MibTableColumn
oacJitterStatsNumNegJitter=_OacJitterStatsNumNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,13),_OacJitterStatsNumNegJitter_Type())
oacJitterStatsNumNegJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumNegJitter.setStatus(_A)
_OacJitterStatsSumPosSD_Type=Integer32
_OacJitterStatsSumPosSD_Object=MibTableColumn
oacJitterStatsSumPosSD=_OacJitterStatsSumPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,14),_OacJitterStatsSumPosSD_Type())
oacJitterStatsSumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumPosSD.setStatus(_A)
_OacJitterStatsNumPosSD_Type=Integer32
_OacJitterStatsNumPosSD_Object=MibTableColumn
oacJitterStatsNumPosSD=_OacJitterStatsNumPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,15),_OacJitterStatsNumPosSD_Type())
oacJitterStatsNumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumPosSD.setStatus(_A)
_OacJitterStatsSumNegSD_Type=Integer32
_OacJitterStatsSumNegSD_Object=MibTableColumn
oacJitterStatsSumNegSD=_OacJitterStatsSumNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,16),_OacJitterStatsSumNegSD_Type())
oacJitterStatsSumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumNegSD.setStatus(_A)
_OacJitterStatsNumNegSD_Type=Integer32
_OacJitterStatsNumNegSD_Object=MibTableColumn
oacJitterStatsNumNegSD=_OacJitterStatsNumNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,17),_OacJitterStatsNumNegSD_Type())
oacJitterStatsNumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumNegSD.setStatus(_A)
_OacJitterStatsSumPosDS_Type=Integer32
_OacJitterStatsSumPosDS_Object=MibTableColumn
oacJitterStatsSumPosDS=_OacJitterStatsSumPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,18),_OacJitterStatsSumPosDS_Type())
oacJitterStatsSumPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumPosDS.setStatus(_A)
_OacJitterStatsNumPosDS_Type=Integer32
_OacJitterStatsNumPosDS_Object=MibTableColumn
oacJitterStatsNumPosDS=_OacJitterStatsNumPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,19),_OacJitterStatsNumPosDS_Type())
oacJitterStatsNumPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumPosDS.setStatus(_A)
_OacJitterStatsSumNegDS_Type=Integer32
_OacJitterStatsSumNegDS_Object=MibTableColumn
oacJitterStatsSumNegDS=_OacJitterStatsSumNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,20),_OacJitterStatsSumNegDS_Type())
oacJitterStatsSumNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSumNegDS.setStatus(_A)
_OacJitterStatsNumNegDS_Type=Integer32
_OacJitterStatsNumNegDS_Object=MibTableColumn
oacJitterStatsNumNegDS=_OacJitterStatsNumNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,21),_OacJitterStatsNumNegDS_Type())
oacJitterStatsNumNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsNumNegDS.setStatus(_A)
class _OacJitterStatsPacketLossSD_Type(Integer32):defaultValue=0
_OacJitterStatsPacketLossSD_Type.__name__=_D
_OacJitterStatsPacketLossSD_Object=MibTableColumn
oacJitterStatsPacketLossSD=_OacJitterStatsPacketLossSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,22),_OacJitterStatsPacketLossSD_Type())
oacJitterStatsPacketLossSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketLossSD.setStatus(_A)
class _OacJitterStatsPacketLossDS_Type(Integer32):defaultValue=0
_OacJitterStatsPacketLossDS_Type.__name__=_D
_OacJitterStatsPacketLossDS_Object=MibTableColumn
oacJitterStatsPacketLossDS=_OacJitterStatsPacketLossDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,23),_OacJitterStatsPacketLossDS_Type())
oacJitterStatsPacketLossDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketLossDS.setStatus(_A)
class _OacJitterStatsPacketOutOfSequence_Type(Integer32):defaultValue=0
_OacJitterStatsPacketOutOfSequence_Type.__name__=_D
_OacJitterStatsPacketOutOfSequence_Object=MibTableColumn
oacJitterStatsPacketOutOfSequence=_OacJitterStatsPacketOutOfSequence_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,24),_OacJitterStatsPacketOutOfSequence_Type())
oacJitterStatsPacketOutOfSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketOutOfSequence.setStatus(_A)
class _OacJitterStatsPacketLateArrival_Type(Integer32):defaultValue=0
_OacJitterStatsPacketLateArrival_Type.__name__=_D
_OacJitterStatsPacketLateArrival_Object=MibTableColumn
oacJitterStatsPacketLateArrival=_OacJitterStatsPacketLateArrival_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,25),_OacJitterStatsPacketLateArrival_Type())
oacJitterStatsPacketLateArrival.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketLateArrival.setStatus(_A)
class _OacJitterStatsPacketLoss_Type(Integer32):defaultValue=0
_OacJitterStatsPacketLoss_Type.__name__=_D
_OacJitterStatsPacketLoss_Object=MibTableColumn
oacJitterStatsPacketLoss=_OacJitterStatsPacketLoss_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,26),_OacJitterStatsPacketLoss_Type())
oacJitterStatsPacketLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsPacketLoss.setStatus(_A)
_OacJitterStatsMaxPosSD_Type=Integer32
_OacJitterStatsMaxPosSD_Object=MibTableColumn
oacJitterStatsMaxPosSD=_OacJitterStatsMaxPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,27),_OacJitterStatsMaxPosSD_Type())
oacJitterStatsMaxPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMaxPosSD.setStatus(_A)
_OacJitterStatsMaxNegSD_Type=Integer32
_OacJitterStatsMaxNegSD_Object=MibTableColumn
oacJitterStatsMaxNegSD=_OacJitterStatsMaxNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,28),_OacJitterStatsMaxNegSD_Type())
oacJitterStatsMaxNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMaxNegSD.setStatus(_A)
_OacJitterStatsMaxPosDS_Type=Integer32
_OacJitterStatsMaxPosDS_Object=MibTableColumn
oacJitterStatsMaxPosDS=_OacJitterStatsMaxPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,29),_OacJitterStatsMaxPosDS_Type())
oacJitterStatsMaxPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMaxPosDS.setStatus(_A)
_OacJitterStatsMaxNegDS_Type=Integer32
_OacJitterStatsMaxNegDS_Object=MibTableColumn
oacJitterStatsMaxNegDS=_OacJitterStatsMaxNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,30),_OacJitterStatsMaxNegDS_Type())
oacJitterStatsMaxNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsMaxNegDS.setStatus(_A)
_OacJitterStatsSum2PosSD_Type=Integer32
_OacJitterStatsSum2PosSD_Object=MibTableColumn
oacJitterStatsSum2PosSD=_OacJitterStatsSum2PosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,31),_OacJitterStatsSum2PosSD_Type())
oacJitterStatsSum2PosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSum2PosSD.setStatus(_A)
_OacJitterStatsSum2NegSD_Type=Integer32
_OacJitterStatsSum2NegSD_Object=MibTableColumn
oacJitterStatsSum2NegSD=_OacJitterStatsSum2NegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,32),_OacJitterStatsSum2NegSD_Type())
oacJitterStatsSum2NegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSum2NegSD.setStatus(_A)
_OacJitterStatsSum2PosDS_Type=Integer32
_OacJitterStatsSum2PosDS_Object=MibTableColumn
oacJitterStatsSum2PosDS=_OacJitterStatsSum2PosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,33),_OacJitterStatsSum2PosDS_Type())
oacJitterStatsSum2PosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSum2PosDS.setStatus(_A)
_OacJitterStatsSum2NegDS_Type=Integer32
_OacJitterStatsSum2NegDS_Object=MibTableColumn
oacJitterStatsSum2NegDS=_OacJitterStatsSum2NegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,34),_OacJitterStatsSum2NegDS_Type())
oacJitterStatsSum2NegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsSum2NegDS.setStatus(_A)
_OacJitterStatsDeviationSD_Type=Integer32
_OacJitterStatsDeviationSD_Object=MibTableColumn
oacJitterStatsDeviationSD=_OacJitterStatsDeviationSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,35),_OacJitterStatsDeviationSD_Type())
oacJitterStatsDeviationSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsDeviationSD.setStatus(_A)
_OacJitterStatsDeviationDS_Type=Integer32
_OacJitterStatsDeviationDS_Object=MibTableColumn
oacJitterStatsDeviationDS=_OacJitterStatsDeviationDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,2,1,36),_OacJitterStatsDeviationDS_Type())
oacJitterStatsDeviationDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsDeviationDS.setStatus(_A)
_OacJitterStatsHistoryTable_Object=MibTable
oacJitterStatsHistoryTable=_OacJitterStatsHistoryTable_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3))
if mibBuilder.loadTexts:oacJitterStatsHistoryTable.setStatus(_A)
_OacJitterStatsHistoryEntry_Object=MibTableRow
oacJitterStatsHistoryEntry=_OacJitterStatsHistoryEntry_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1))
oacJitterStatsHistoryEntry.setIndexNames((0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:oacJitterStatsHistoryEntry.setStatus(_A)
_OacJitterStatsHistoryIndex_Type=Integer32
_OacJitterStatsHistoryIndex_Object=MibTableColumn
oacJitterStatsHistoryIndex=_OacJitterStatsHistoryIndex_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,1),_OacJitterStatsHistoryIndex_Type())
oacJitterStatsHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryIndex.setStatus(_A)
_OacJitterStatsHistoryCompleted_Type=OacJitterResponseSense
_OacJitterStatsHistoryCompleted_Object=MibTableColumn
oacJitterStatsHistoryCompleted=_OacJitterStatsHistoryCompleted_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,2),_OacJitterStatsHistoryCompleted_Type())
oacJitterStatsHistoryCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryCompleted.setStatus(_A)
_OacJitterStatsHistoryTime_Type=DateAndTime
_OacJitterStatsHistoryTime_Object=MibTableColumn
oacJitterStatsHistoryTime=_OacJitterStatsHistoryTime_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,3),_OacJitterStatsHistoryTime_Type())
oacJitterStatsHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryTime.setStatus(_A)
class _OacJitterStatsHistoryNumRTT_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryNumRTT_Type.__name__=_D
_OacJitterStatsHistoryNumRTT_Object=MibTableColumn
oacJitterStatsHistoryNumRTT=_OacJitterStatsHistoryNumRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,4),_OacJitterStatsHistoryNumRTT_Type())
oacJitterStatsHistoryNumRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumRTT.setStatus(_A)
_OacJitterStatsHistoryPacketRecv_Type=Integer32
_OacJitterStatsHistoryPacketRecv_Object=MibTableColumn
oacJitterStatsHistoryPacketRecv=_OacJitterStatsHistoryPacketRecv_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,5),_OacJitterStatsHistoryPacketRecv_Type())
oacJitterStatsHistoryPacketRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketRecv.setStatus(_A)
_OacJitterStatsHistoryAvgRTT_Type=Integer32
_OacJitterStatsHistoryAvgRTT_Object=MibTableColumn
oacJitterStatsHistoryAvgRTT=_OacJitterStatsHistoryAvgRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,6),_OacJitterStatsHistoryAvgRTT_Type())
oacJitterStatsHistoryAvgRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryAvgRTT.setStatus(_A)
_OacJitterStatsHistorySumRTT_Type=Integer32
_OacJitterStatsHistorySumRTT_Object=MibTableColumn
oacJitterStatsHistorySumRTT=_OacJitterStatsHistorySumRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,7),_OacJitterStatsHistorySumRTT_Type())
oacJitterStatsHistorySumRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumRTT.setStatus(_A)
_OacJitterStatsHistoryMinRTT_Type=Integer32
_OacJitterStatsHistoryMinRTT_Object=MibTableColumn
oacJitterStatsHistoryMinRTT=_OacJitterStatsHistoryMinRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,8),_OacJitterStatsHistoryMinRTT_Type())
oacJitterStatsHistoryMinRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMinRTT.setStatus(_A)
_OacJitterStatsHistoryMaxRTT_Type=Integer32
_OacJitterStatsHistoryMaxRTT_Object=MibTableColumn
oacJitterStatsHistoryMaxRTT=_OacJitterStatsHistoryMaxRTT_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,9),_OacJitterStatsHistoryMaxRTT_Type())
oacJitterStatsHistoryMaxRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMaxRTT.setStatus(_A)
_OacJitterStatsHistorySumPosJitter_Type=Integer32
_OacJitterStatsHistorySumPosJitter_Object=MibTableColumn
oacJitterStatsHistorySumPosJitter=_OacJitterStatsHistorySumPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,10),_OacJitterStatsHistorySumPosJitter_Type())
oacJitterStatsHistorySumPosJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumPosJitter.setStatus(_A)
_OacJitterStatsHistoryNumPosJitter_Type=Integer32
_OacJitterStatsHistoryNumPosJitter_Object=MibTableColumn
oacJitterStatsHistoryNumPosJitter=_OacJitterStatsHistoryNumPosJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,11),_OacJitterStatsHistoryNumPosJitter_Type())
oacJitterStatsHistoryNumPosJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumPosJitter.setStatus(_A)
_OacJitterStatsHistorySumNegJitter_Type=Integer32
_OacJitterStatsHistorySumNegJitter_Object=MibTableColumn
oacJitterStatsHistorySumNegJitter=_OacJitterStatsHistorySumNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,12),_OacJitterStatsHistorySumNegJitter_Type())
oacJitterStatsHistorySumNegJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumNegJitter.setStatus(_A)
_OacJitterStatsHistoryNumNegJitter_Type=Integer32
_OacJitterStatsHistoryNumNegJitter_Object=MibTableColumn
oacJitterStatsHistoryNumNegJitter=_OacJitterStatsHistoryNumNegJitter_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,13),_OacJitterStatsHistoryNumNegJitter_Type())
oacJitterStatsHistoryNumNegJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumNegJitter.setStatus(_A)
_OacJitterStatsHistorySumPosSD_Type=Integer32
_OacJitterStatsHistorySumPosSD_Object=MibTableColumn
oacJitterStatsHistorySumPosSD=_OacJitterStatsHistorySumPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,14),_OacJitterStatsHistorySumPosSD_Type())
oacJitterStatsHistorySumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumPosSD.setStatus(_A)
_OacJitterStatsHistoryNumPosSD_Type=Integer32
_OacJitterStatsHistoryNumPosSD_Object=MibTableColumn
oacJitterStatsHistoryNumPosSD=_OacJitterStatsHistoryNumPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,15),_OacJitterStatsHistoryNumPosSD_Type())
oacJitterStatsHistoryNumPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumPosSD.setStatus(_A)
_OacJitterStatsHistorySumNegSD_Type=Integer32
_OacJitterStatsHistorySumNegSD_Object=MibTableColumn
oacJitterStatsHistorySumNegSD=_OacJitterStatsHistorySumNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,16),_OacJitterStatsHistorySumNegSD_Type())
oacJitterStatsHistorySumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumNegSD.setStatus(_A)
_OacJitterStatsHistoryNumNegSD_Type=Integer32
_OacJitterStatsHistoryNumNegSD_Object=MibTableColumn
oacJitterStatsHistoryNumNegSD=_OacJitterStatsHistoryNumNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,17),_OacJitterStatsHistoryNumNegSD_Type())
oacJitterStatsHistoryNumNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumNegSD.setStatus(_A)
_OacJitterStatsHistorySumPosDS_Type=Integer32
_OacJitterStatsHistorySumPosDS_Object=MibTableColumn
oacJitterStatsHistorySumPosDS=_OacJitterStatsHistorySumPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,18),_OacJitterStatsHistorySumPosDS_Type())
oacJitterStatsHistorySumPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumPosDS.setStatus(_A)
_OacJitterStatsHistoryNumPosDS_Type=Integer32
_OacJitterStatsHistoryNumPosDS_Object=MibTableColumn
oacJitterStatsHistoryNumPosDS=_OacJitterStatsHistoryNumPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,19),_OacJitterStatsHistoryNumPosDS_Type())
oacJitterStatsHistoryNumPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumPosDS.setStatus(_A)
_OacJitterStatsHistorySumNegDS_Type=Integer32
_OacJitterStatsHistorySumNegDS_Object=MibTableColumn
oacJitterStatsHistorySumNegDS=_OacJitterStatsHistorySumNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,20),_OacJitterStatsHistorySumNegDS_Type())
oacJitterStatsHistorySumNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySumNegDS.setStatus(_A)
_OacJitterStatsHistoryNumNegDS_Type=Integer32
_OacJitterStatsHistoryNumNegDS_Object=MibTableColumn
oacJitterStatsHistoryNumNegDS=_OacJitterStatsHistoryNumNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,21),_OacJitterStatsHistoryNumNegDS_Type())
oacJitterStatsHistoryNumNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryNumNegDS.setStatus(_A)
class _OacJitterStatsHistoryPacketLossSD_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryPacketLossSD_Type.__name__=_D
_OacJitterStatsHistoryPacketLossSD_Object=MibTableColumn
oacJitterStatsHistoryPacketLossSD=_OacJitterStatsHistoryPacketLossSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,22),_OacJitterStatsHistoryPacketLossSD_Type())
oacJitterStatsHistoryPacketLossSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketLossSD.setStatus(_A)
class _OacJitterStatsHistoryPacketLossDS_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryPacketLossDS_Type.__name__=_D
_OacJitterStatsHistoryPacketLossDS_Object=MibTableColumn
oacJitterStatsHistoryPacketLossDS=_OacJitterStatsHistoryPacketLossDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,23),_OacJitterStatsHistoryPacketLossDS_Type())
oacJitterStatsHistoryPacketLossDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketLossDS.setStatus(_A)
class _OacJitterStatsHistoryPacketOutOfSequence_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryPacketOutOfSequence_Type.__name__=_D
_OacJitterStatsHistoryPacketOutOfSequence_Object=MibTableColumn
oacJitterStatsHistoryPacketOutOfSequence=_OacJitterStatsHistoryPacketOutOfSequence_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,24),_OacJitterStatsHistoryPacketOutOfSequence_Type())
oacJitterStatsHistoryPacketOutOfSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketOutOfSequence.setStatus(_A)
class _OacJitterStatsHistoryPacketLateArrival_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryPacketLateArrival_Type.__name__=_D
_OacJitterStatsHistoryPacketLateArrival_Object=MibTableColumn
oacJitterStatsHistoryPacketLateArrival=_OacJitterStatsHistoryPacketLateArrival_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,25),_OacJitterStatsHistoryPacketLateArrival_Type())
oacJitterStatsHistoryPacketLateArrival.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketLateArrival.setStatus(_A)
class _OacJitterStatsHistoryPacketLoss_Type(Integer32):defaultValue=0
_OacJitterStatsHistoryPacketLoss_Type.__name__=_D
_OacJitterStatsHistoryPacketLoss_Object=MibTableColumn
oacJitterStatsHistoryPacketLoss=_OacJitterStatsHistoryPacketLoss_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,26),_OacJitterStatsHistoryPacketLoss_Type())
oacJitterStatsHistoryPacketLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryPacketLoss.setStatus(_A)
_OacJitterStatsHistoryMaxPosSD_Type=Integer32
_OacJitterStatsHistoryMaxPosSD_Object=MibTableColumn
oacJitterStatsHistoryMaxPosSD=_OacJitterStatsHistoryMaxPosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,27),_OacJitterStatsHistoryMaxPosSD_Type())
oacJitterStatsHistoryMaxPosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMaxPosSD.setStatus(_A)
_OacJitterStatsHistoryMaxNegSD_Type=Integer32
_OacJitterStatsHistoryMaxNegSD_Object=MibTableColumn
oacJitterStatsHistoryMaxNegSD=_OacJitterStatsHistoryMaxNegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,28),_OacJitterStatsHistoryMaxNegSD_Type())
oacJitterStatsHistoryMaxNegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMaxNegSD.setStatus(_A)
_OacJitterStatsHistoryMaxPosDS_Type=Integer32
_OacJitterStatsHistoryMaxPosDS_Object=MibTableColumn
oacJitterStatsHistoryMaxPosDS=_OacJitterStatsHistoryMaxPosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,29),_OacJitterStatsHistoryMaxPosDS_Type())
oacJitterStatsHistoryMaxPosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMaxPosDS.setStatus(_A)
_OacJitterStatsHistoryMaxNegDS_Type=Integer32
_OacJitterStatsHistoryMaxNegDS_Object=MibTableColumn
oacJitterStatsHistoryMaxNegDS=_OacJitterStatsHistoryMaxNegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,30),_OacJitterStatsHistoryMaxNegDS_Type())
oacJitterStatsHistoryMaxNegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryMaxNegDS.setStatus(_A)
_OacJitterStatsHistorySum2PosSD_Type=Integer32
_OacJitterStatsHistorySum2PosSD_Object=MibTableColumn
oacJitterStatsHistorySum2PosSD=_OacJitterStatsHistorySum2PosSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,31),_OacJitterStatsHistorySum2PosSD_Type())
oacJitterStatsHistorySum2PosSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySum2PosSD.setStatus(_A)
_OacJitterStatsHistorySum2NegSD_Type=Integer32
_OacJitterStatsHistorySum2NegSD_Object=MibTableColumn
oacJitterStatsHistorySum2NegSD=_OacJitterStatsHistorySum2NegSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,32),_OacJitterStatsHistorySum2NegSD_Type())
oacJitterStatsHistorySum2NegSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySum2NegSD.setStatus(_A)
_OacJitterStatsHistorySum2PosDS_Type=Integer32
_OacJitterStatsHistorySum2PosDS_Object=MibTableColumn
oacJitterStatsHistorySum2PosDS=_OacJitterStatsHistorySum2PosDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,33),_OacJitterStatsHistorySum2PosDS_Type())
oacJitterStatsHistorySum2PosDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySum2PosDS.setStatus(_A)
_OacJitterStatsHistorySum2NegDS_Type=Integer32
_OacJitterStatsHistorySum2NegDS_Object=MibTableColumn
oacJitterStatsHistorySum2NegDS=_OacJitterStatsHistorySum2NegDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,34),_OacJitterStatsHistorySum2NegDS_Type())
oacJitterStatsHistorySum2NegDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistorySum2NegDS.setStatus(_A)
_OacJitterStatsHistoryDeviationSD_Type=Integer32
_OacJitterStatsHistoryDeviationSD_Object=MibTableColumn
oacJitterStatsHistoryDeviationSD=_OacJitterStatsHistoryDeviationSD_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,35),_OacJitterStatsHistoryDeviationSD_Type())
oacJitterStatsHistoryDeviationSD.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryDeviationSD.setStatus(_A)
_OacJitterStatsHistoryDeviationDS_Type=Integer32
_OacJitterStatsHistoryDeviationDS_Object=MibTableColumn
oacJitterStatsHistoryDeviationDS=_OacJitterStatsHistoryDeviationDS_Object((1,3,6,1,4,1,13191,10,3,4,5,1,3,1,36),_OacJitterStatsHistoryDeviationDS_Type())
oacJitterStatsHistoryDeviationDS.setMaxAccess(_C)
if mibBuilder.loadTexts:oacJitterStatsHistoryDeviationDS.setStatus(_A)
oacJitterGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,5,2000,1,1))
oacJitterGeneralGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:oacJitterGeneralGroup.setStatus(_A)
oacJitterCompliance=ModuleCompliance((1,3,6,1,4,1,13191,5,2000,2,1))
oacJitterCompliance.setObjects((_B,_Af))
if mibBuilder.loadTexts:oacJitterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_I:OacJitterControlJitterType,'OacJitterResponseSense':OacJitterResponseSense,'oacJitterMIBModule':oacJitterMIBModule,'oacJitterConformance':oacJitterConformance,'oacJitterGroups':oacJitterGroups,_Af:oacJitterGeneralGroup,'oacJitterCompliances':oacJitterCompliances,'oacJitterCompliance':oacJitterCompliance,'oacExpIMJitter':oacExpIMJitter,'oacJitterObjects':oacJitterObjects,'oacJitterControlTable':oacJitterControlTable,'oacJitterControlEntry':oacJitterControlEntry,_F:oacJitterControlIndex,_L:oacJitterControlOwner,_M:oacJitterControlType,_N:oacJitterControlFrequency,_O:oacJitterControlTimeout,_Q:oacJitterControlTargetAddress,_R:oacJitterControlTargetPort,_S:oacJitterControlSourceAddress,_T:oacJitterControlInterval,_U:oacJitterControlPktDataRequestSize,_V:oacJitterControlPacketCount,_W:oacJitterControlTos,_P:oacJitterControlStatus,'oacJitterControlVrfName':oacJitterControlVrfName,'oacJitterStatsTable':oacJitterStatsTable,'oacJitterStatsEntry':oacJitterStatsEntry,_X:oacJitterStatsCompleted,_Y:oacJitterStatsTime,_Z:oacJitterStatsNumRTT,_a:oacJitterStatsPacketRecv,_b:oacJitterStatsAvgRTT,_c:oacJitterStatsSumRTT,_d:oacJitterStatsMinRTT,_e:oacJitterStatsMaxRTT,_f:oacJitterStatsSumPosJitter,_g:oacJitterStatsNumPosJitter,_h:oacJitterStatsSumNegJitter,_i:oacJitterStatsNumNegJitter,_j:oacJitterStatsSumPosSD,_k:oacJitterStatsNumPosSD,_m:oacJitterStatsSumNegSD,_n:oacJitterStatsNumNegSD,_p:oacJitterStatsSumPosDS,_q:oacJitterStatsNumPosDS,_s:oacJitterStatsSumNegDS,_t:oacJitterStatsNumNegDS,_A1:oacJitterStatsPacketLossSD,_A2:oacJitterStatsPacketLossDS,_A3:oacJitterStatsPacketOutOfSequence,_A4:oacJitterStatsPacketLateArrival,_A5:oacJitterStatsPacketLoss,_l:oacJitterStatsMaxPosSD,_o:oacJitterStatsMaxNegSD,_r:oacJitterStatsMaxPosDS,_u:oacJitterStatsMaxNegDS,_v:oacJitterStatsSum2PosSD,_w:oacJitterStatsSum2NegSD,_x:oacJitterStatsSum2PosDS,_y:oacJitterStatsSum2NegDS,_z:oacJitterStatsDeviationSD,_A0:oacJitterStatsDeviationDS,'oacJitterStatsHistoryTable':oacJitterStatsHistoryTable,'oacJitterStatsHistoryEntry':oacJitterStatsHistoryEntry,_K:oacJitterStatsHistoryIndex,_A6:oacJitterStatsHistoryCompleted,_A7:oacJitterStatsHistoryTime,_A8:oacJitterStatsHistoryNumRTT,_A9:oacJitterStatsHistoryPacketRecv,_AA:oacJitterStatsHistoryAvgRTT,_AB:oacJitterStatsHistorySumRTT,_AC:oacJitterStatsHistoryMinRTT,_AD:oacJitterStatsHistoryMaxRTT,_AE:oacJitterStatsHistorySumPosJitter,_AF:oacJitterStatsHistoryNumPosJitter,_AG:oacJitterStatsHistorySumNegJitter,_AH:oacJitterStatsHistoryNumNegJitter,_AI:oacJitterStatsHistorySumPosSD,_AJ:oacJitterStatsHistoryNumPosSD,_AK:oacJitterStatsHistorySumNegSD,_AL:oacJitterStatsHistoryNumNegSD,_AM:oacJitterStatsHistorySumPosDS,_AN:oacJitterStatsHistoryNumPosDS,_AO:oacJitterStatsHistorySumNegDS,_AP:oacJitterStatsHistoryNumNegDS,_AQ:oacJitterStatsHistoryPacketLossSD,_AR:oacJitterStatsHistoryPacketLossDS,_AS:oacJitterStatsHistoryPacketOutOfSequence,_AT:oacJitterStatsHistoryPacketLateArrival,_AU:oacJitterStatsHistoryPacketLoss,_AV:oacJitterStatsHistoryMaxPosSD,_AW:oacJitterStatsHistoryMaxNegSD,_AX:oacJitterStatsHistoryMaxPosDS,_AY:oacJitterStatsHistoryMaxNegDS,_AZ:oacJitterStatsHistorySum2PosSD,_Aa:oacJitterStatsHistorySum2NegSD,_Ab:oacJitterStatsHistorySum2PosDS,_Ac:oacJitterStatsHistorySum2NegDS,_Ad:oacJitterStatsHistoryDeviationSD,_Ae:oacJitterStatsHistoryDeviationDS})