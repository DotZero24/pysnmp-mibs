_AS='cegBufferingAgentStatsGrpSup1'
_AR='cegSystemStatusGrpSup3'
_AQ='cegCongestionClearedNotif'
_AP='cegCongestionLowThresholdNotif'
_AO='cegCongestionHighThresholdNotif'
_AN='cegPacketDropDueToMaxBufferLimit'
_AM='cegPacketDropDueToMaxPacketLimit'
_AL='cegTotalIdleSessions'
_AK='cegActivatedIpv6DedicatedBearers'
_AJ='cegActivatedIpv4DedicatedBearers'
_AI='cegActivatedDedicatedBearers'
_AH='cegActivatedBearers'
_AG='cegActivatedGtpv2SPgwSessions'
_AF='cegActivatedGtpv2PgwSessions'
_AE='cegActivatedGtpv2SgwSessions'
_AD='cegActivatedIpv4v6Bearers'
_AC='cegCongestionClearNotifEnable'
_AB='cegCongestionLowNotifEnable'
_AA='cegCongestionHighNotifEnable'
_A9='cegCongestionHighLastDuration'
_A8='cegCongestionHighLastOccurTime'
_A7='cegCongestionLowLastDuration'
_A6='cegCongestionLowLastOccurTime'
_A5='cegTotalBufferAvailable'
_A4='cegTotalBufferedBytes'
_A3='cegTotalBufferedPackets'
_A2='cegTotalInUseBuffers'
_A1='cegBufferMaxPacketsPerBuffer'
_A0='cegBufferDiscardDataTime'
_z='cegBufferMaxSize'
_y='cegBufferingAgentEnabled'
_x='cegBufferRejLowMem'
_w='cegBufferRejMemUnavailable'
_v='cegBuffersTimedOut'
_u='cegBuffersDeleted'
_t='cegBufferBytesDequeued'
_s='cegBufferPacketsDequeued'
_r='cegBufferBytesEnqueued'
_q='cegBufferPacketsEnqueued'
_p='cegBuffersCreated'
_o='cegCongestionLowThresholdReached'
_n='cegCongestionHighThresholdReached'
_m='cegCongestionIncomingReqDrops'
_l='cegTotalIdleUsers'
_k='cegActivatedIpv4v6Sessions'
_j='cegTotalSuspendedUsers'
_i='cegTotalUsers'
_h='cegActivatedIpv6Bearers'
_g='cegActivatedIpv4Bearers'
_f='bearer'
_e='percent'
_d='Integer32'
_c='SnmpAdminString'
_b='cegSystemStatusGrpSup2'
_a='deprecated'
_Z='buffer'
_Y='cegSystemStatusGrpSup1'
_X='cegCongestionHighThreshold'
_W='cegCongestionLowThreshold'
_V='Bearers'
_U='sessions'
_T='packet'
_S='cegBufferingAgentStatusGrp'
_R='cegBufferingAgentConfigGrp'
_Q='cegBufferingAgentStatsGrp'
_P='cegOverloadProtectionNotifGrp'
_O='cegOverloadProtectionNotifMgmtGrp'
_N='cegOverloadProtectionStatusGrp'
_M='cegOverloadProtectionConfigGrp'
_L='cegOverloadProtectionStatsGrp'
_K='cegSystemStatusGrp'
_J='cegCongestionStatus'
_I='cegCongestionDfpWeight'
_H='cegVersion'
_G='Bytes'
_F='TruthValue'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-EPC-GATEWAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_c)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_d,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp',_F)
ciscoEpcGatewayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,731))
if mibBuilder.loadTexts:ciscoEpcGatewayMIB.setRevisions(('2012-02-08 00:00','2011-05-10 00:00','2011-03-04 00:00','2010-06-28 00:00','2010-05-06 00:00','2010-04-21 00:00'))
_CiscoEpcGatewayMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayMIBNotifications=_CiscoEpcGatewayMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,731,0))
_CiscoEpcGatewayMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayMIBObjects=_CiscoEpcGatewayMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,731,1))
_CiscoEpcGatewayStatistics_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayStatistics=_CiscoEpcGatewayStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,1))
_CegOverloadProtectionStats_ObjectIdentity=ObjectIdentity
cegOverloadProtectionStats=_CegOverloadProtectionStats_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,1,1))
_CegCongestionIncomingReqDrops_Type=Counter32
_CegCongestionIncomingReqDrops_Object=MibScalar
cegCongestionIncomingReqDrops=_CegCongestionIncomingReqDrops_Object((1,3,6,1,4,1,9,9,731,1,1,1,1),_CegCongestionIncomingReqDrops_Type())
cegCongestionIncomingReqDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionIncomingReqDrops.setStatus(_B)
_CegCongestionLowThresholdReached_Type=Counter32
_CegCongestionLowThresholdReached_Object=MibScalar
cegCongestionLowThresholdReached=_CegCongestionLowThresholdReached_Object((1,3,6,1,4,1,9,9,731,1,1,1,2),_CegCongestionLowThresholdReached_Type())
cegCongestionLowThresholdReached.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionLowThresholdReached.setStatus(_B)
_CegCongestionHighThresholdReached_Type=Counter32
_CegCongestionHighThresholdReached_Object=MibScalar
cegCongestionHighThresholdReached=_CegCongestionHighThresholdReached_Object((1,3,6,1,4,1,9,9,731,1,1,1,3),_CegCongestionHighThresholdReached_Type())
cegCongestionHighThresholdReached.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionHighThresholdReached.setStatus(_B)
_CegBufferStats_ObjectIdentity=ObjectIdentity
cegBufferStats=_CegBufferStats_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,1,2))
_CegBuffersCreated_Type=Counter32
_CegBuffersCreated_Object=MibScalar
cegBuffersCreated=_CegBuffersCreated_Object((1,3,6,1,4,1,9,9,731,1,1,2,1),_CegBuffersCreated_Type())
cegBuffersCreated.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBuffersCreated.setStatus(_B)
if mibBuilder.loadTexts:cegBuffersCreated.setUnits(_Z)
_CegBuffersDeleted_Type=Counter32
_CegBuffersDeleted_Object=MibScalar
cegBuffersDeleted=_CegBuffersDeleted_Object((1,3,6,1,4,1,9,9,731,1,1,2,2),_CegBuffersDeleted_Type())
cegBuffersDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBuffersDeleted.setStatus(_B)
if mibBuilder.loadTexts:cegBuffersDeleted.setUnits(_Z)
_CegBuffersTimedOut_Type=Counter32
_CegBuffersTimedOut_Object=MibScalar
cegBuffersTimedOut=_CegBuffersTimedOut_Object((1,3,6,1,4,1,9,9,731,1,1,2,3),_CegBuffersTimedOut_Type())
cegBuffersTimedOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBuffersTimedOut.setStatus(_B)
_CegBufferPacketsEnqueued_Type=Counter32
_CegBufferPacketsEnqueued_Object=MibScalar
cegBufferPacketsEnqueued=_CegBufferPacketsEnqueued_Object((1,3,6,1,4,1,9,9,731,1,1,2,4),_CegBufferPacketsEnqueued_Type())
cegBufferPacketsEnqueued.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferPacketsEnqueued.setStatus(_B)
if mibBuilder.loadTexts:cegBufferPacketsEnqueued.setUnits(_T)
_CegBufferPacketsDequeued_Type=Counter32
_CegBufferPacketsDequeued_Object=MibScalar
cegBufferPacketsDequeued=_CegBufferPacketsDequeued_Object((1,3,6,1,4,1,9,9,731,1,1,2,5),_CegBufferPacketsDequeued_Type())
cegBufferPacketsDequeued.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferPacketsDequeued.setStatus(_B)
if mibBuilder.loadTexts:cegBufferPacketsDequeued.setUnits(_T)
_CegBufferBytesEnqueued_Type=Counter32
_CegBufferBytesEnqueued_Object=MibScalar
cegBufferBytesEnqueued=_CegBufferBytesEnqueued_Object((1,3,6,1,4,1,9,9,731,1,1,2,6),_CegBufferBytesEnqueued_Type())
cegBufferBytesEnqueued.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferBytesEnqueued.setStatus(_B)
if mibBuilder.loadTexts:cegBufferBytesEnqueued.setUnits(_G)
_CegBufferBytesDequeued_Type=Counter32
_CegBufferBytesDequeued_Object=MibScalar
cegBufferBytesDequeued=_CegBufferBytesDequeued_Object((1,3,6,1,4,1,9,9,731,1,1,2,7),_CegBufferBytesDequeued_Type())
cegBufferBytesDequeued.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferBytesDequeued.setStatus(_B)
if mibBuilder.loadTexts:cegBufferBytesDequeued.setUnits(_G)
_CegBufferRejMemUnavailable_Type=Counter32
_CegBufferRejMemUnavailable_Object=MibScalar
cegBufferRejMemUnavailable=_CegBufferRejMemUnavailable_Object((1,3,6,1,4,1,9,9,731,1,1,2,8),_CegBufferRejMemUnavailable_Type())
cegBufferRejMemUnavailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferRejMemUnavailable.setStatus(_B)
_CegBufferRejLowMem_Type=Counter32
_CegBufferRejLowMem_Object=MibScalar
cegBufferRejLowMem=_CegBufferRejLowMem_Object((1,3,6,1,4,1,9,9,731,1,1,2,9),_CegBufferRejLowMem_Type())
cegBufferRejLowMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cegBufferRejLowMem.setStatus(_B)
_CegPacketDropDueToMaxPacketLimit_Type=Counter32
_CegPacketDropDueToMaxPacketLimit_Object=MibScalar
cegPacketDropDueToMaxPacketLimit=_CegPacketDropDueToMaxPacketLimit_Object((1,3,6,1,4,1,9,9,731,1,1,2,10),_CegPacketDropDueToMaxPacketLimit_Type())
cegPacketDropDueToMaxPacketLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cegPacketDropDueToMaxPacketLimit.setStatus(_B)
_CegPacketDropDueToMaxBufferLimit_Type=Counter32
_CegPacketDropDueToMaxBufferLimit_Object=MibScalar
cegPacketDropDueToMaxBufferLimit=_CegPacketDropDueToMaxBufferLimit_Object((1,3,6,1,4,1,9,9,731,1,1,2,11),_CegPacketDropDueToMaxBufferLimit_Type())
cegPacketDropDueToMaxBufferLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cegPacketDropDueToMaxBufferLimit.setStatus(_B)
_CiscoEpcGatewayConfig_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayConfig=_CiscoEpcGatewayConfig_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,2))
_CegOverloadProtectionConfig_ObjectIdentity=ObjectIdentity
cegOverloadProtectionConfig=_CegOverloadProtectionConfig_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,2,1))
class _CegCongestionLowThreshold_Type(Unsigned32):defaultValue=95;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CegCongestionLowThreshold_Type.__name__=_E
_CegCongestionLowThreshold_Object=MibScalar
cegCongestionLowThreshold=_CegCongestionLowThreshold_Object((1,3,6,1,4,1,9,9,731,1,2,1,1),_CegCongestionLowThreshold_Type())
cegCongestionLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cegCongestionLowThreshold.setStatus(_B)
if mibBuilder.loadTexts:cegCongestionLowThreshold.setUnits(_e)
class _CegCongestionHighThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CegCongestionHighThreshold_Type.__name__=_E
_CegCongestionHighThreshold_Object=MibScalar
cegCongestionHighThreshold=_CegCongestionHighThreshold_Object((1,3,6,1,4,1,9,9,731,1,2,1,2),_CegCongestionHighThreshold_Type())
cegCongestionHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cegCongestionHighThreshold.setStatus(_B)
if mibBuilder.loadTexts:cegCongestionHighThreshold.setUnits(_e)
_CegBufferingAgentConfig_ObjectIdentity=ObjectIdentity
cegBufferingAgentConfig=_CegBufferingAgentConfig_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,2,2))
class _CegBufferingAgentEnabled_Type(TruthValue):defaultValue=2
_CegBufferingAgentEnabled_Type.__name__=_F
_CegBufferingAgentEnabled_Object=MibScalar
cegBufferingAgentEnabled=_CegBufferingAgentEnabled_Object((1,3,6,1,4,1,9,9,731,1,2,2,1),_CegBufferingAgentEnabled_Type())
cegBufferingAgentEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cegBufferingAgentEnabled.setStatus(_B)
class _CegBufferMaxSize_Type(Unsigned32):defaultValue=1024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,12000))
_CegBufferMaxSize_Type.__name__=_E
_CegBufferMaxSize_Object=MibScalar
cegBufferMaxSize=_CegBufferMaxSize_Object((1,3,6,1,4,1,9,9,731,1,2,2,2),_CegBufferMaxSize_Type())
cegBufferMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cegBufferMaxSize.setStatus(_B)
if mibBuilder.loadTexts:cegBufferMaxSize.setUnits(_G)
class _CegBufferDiscardDataTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CegBufferDiscardDataTime_Type.__name__=_E
_CegBufferDiscardDataTime_Object=MibScalar
cegBufferDiscardDataTime=_CegBufferDiscardDataTime_Object((1,3,6,1,4,1,9,9,731,1,2,2,3),_CegBufferDiscardDataTime_Type())
cegBufferDiscardDataTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cegBufferDiscardDataTime.setStatus(_B)
if mibBuilder.loadTexts:cegBufferDiscardDataTime.setUnits('second')
class _CegBufferMaxPacketsPerBuffer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CegBufferMaxPacketsPerBuffer_Type.__name__=_E
_CegBufferMaxPacketsPerBuffer_Object=MibScalar
cegBufferMaxPacketsPerBuffer=_CegBufferMaxPacketsPerBuffer_Object((1,3,6,1,4,1,9,9,731,1,2,2,4),_CegBufferMaxPacketsPerBuffer_Type())
cegBufferMaxPacketsPerBuffer.setMaxAccess(_D)
if mibBuilder.loadTexts:cegBufferMaxPacketsPerBuffer.setStatus(_B)
if mibBuilder.loadTexts:cegBufferMaxPacketsPerBuffer.setUnits(_T)
_CiscoEpcGatewayStatus_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayStatus=_CiscoEpcGatewayStatus_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,3))
class _CegVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_CegVersion_Type.__name__=_c
_CegVersion_Object=MibScalar
cegVersion=_CegVersion_Object((1,3,6,1,4,1,9,9,731,1,3,1),_CegVersion_Type())
cegVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cegVersion.setStatus(_B)
_CegActivatedIpv4Bearers_Type=Gauge32
_CegActivatedIpv4Bearers_Object=MibScalar
cegActivatedIpv4Bearers=_CegActivatedIpv4Bearers_Object((1,3,6,1,4,1,9,9,731,1,3,2),_CegActivatedIpv4Bearers_Type())
cegActivatedIpv4Bearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv4Bearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv4Bearers.setUnits(_f)
_CegActivatedIpv6Bearers_Type=Gauge32
_CegActivatedIpv6Bearers_Object=MibScalar
cegActivatedIpv6Bearers=_CegActivatedIpv6Bearers_Object((1,3,6,1,4,1,9,9,731,1,3,3),_CegActivatedIpv6Bearers_Type())
cegActivatedIpv6Bearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv6Bearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv6Bearers.setUnits(_f)
_CegTotalUsers_Type=Gauge32
_CegTotalUsers_Object=MibScalar
cegTotalUsers=_CegTotalUsers_Object((1,3,6,1,4,1,9,9,731,1,3,4),_CegTotalUsers_Type())
cegTotalUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalUsers.setStatus(_B)
_CegTotalIdleUsers_Type=Gauge32
_CegTotalIdleUsers_Object=MibScalar
cegTotalIdleUsers=_CegTotalIdleUsers_Object((1,3,6,1,4,1,9,9,731,1,3,5),_CegTotalIdleUsers_Type())
cegTotalIdleUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalIdleUsers.setStatus(_B)
if mibBuilder.loadTexts:cegTotalIdleUsers.setUnits('Users')
_CegTotalSuspendedUsers_Type=Gauge32
_CegTotalSuspendedUsers_Object=MibScalar
cegTotalSuspendedUsers=_CegTotalSuspendedUsers_Object((1,3,6,1,4,1,9,9,731,1,3,6),_CegTotalSuspendedUsers_Type())
cegTotalSuspendedUsers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalSuspendedUsers.setStatus(_B)
_CegActivatedIpv4v6Sessions_Type=Gauge32
_CegActivatedIpv4v6Sessions_Object=MibScalar
cegActivatedIpv4v6Sessions=_CegActivatedIpv4v6Sessions_Object((1,3,6,1,4,1,9,9,731,1,3,7),_CegActivatedIpv4v6Sessions_Type())
cegActivatedIpv4v6Sessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv4v6Sessions.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv4v6Sessions.setUnits(_U)
_CegOverloadProtectionStatus_ObjectIdentity=ObjectIdentity
cegOverloadProtectionStatus=_CegOverloadProtectionStatus_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,3,8))
class _CegCongestionDfpWeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CegCongestionDfpWeight_Type.__name__=_E
_CegCongestionDfpWeight_Object=MibScalar
cegCongestionDfpWeight=_CegCongestionDfpWeight_Object((1,3,6,1,4,1,9,9,731,1,3,8,1),_CegCongestionDfpWeight_Type())
cegCongestionDfpWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionDfpWeight.setStatus(_B)
class _CegCongestionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('low',2),('high',3)))
_CegCongestionStatus_Type.__name__=_d
_CegCongestionStatus_Object=MibScalar
cegCongestionStatus=_CegCongestionStatus_Object((1,3,6,1,4,1,9,9,731,1,3,8,2),_CegCongestionStatus_Type())
cegCongestionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionStatus.setStatus(_B)
_CegCongestionLowLastOccurTime_Type=TimeStamp
_CegCongestionLowLastOccurTime_Object=MibScalar
cegCongestionLowLastOccurTime=_CegCongestionLowLastOccurTime_Object((1,3,6,1,4,1,9,9,731,1,3,8,3),_CegCongestionLowLastOccurTime_Type())
cegCongestionLowLastOccurTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionLowLastOccurTime.setStatus(_B)
_CegCongestionLowLastDuration_Type=TimeInterval
_CegCongestionLowLastDuration_Object=MibScalar
cegCongestionLowLastDuration=_CegCongestionLowLastDuration_Object((1,3,6,1,4,1,9,9,731,1,3,8,4),_CegCongestionLowLastDuration_Type())
cegCongestionLowLastDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionLowLastDuration.setStatus(_B)
_CegCongestionHighLastOccurTime_Type=TimeStamp
_CegCongestionHighLastOccurTime_Object=MibScalar
cegCongestionHighLastOccurTime=_CegCongestionHighLastOccurTime_Object((1,3,6,1,4,1,9,9,731,1,3,8,5),_CegCongestionHighLastOccurTime_Type())
cegCongestionHighLastOccurTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionHighLastOccurTime.setStatus(_B)
_CegCongestionHighLastDuration_Type=TimeInterval
_CegCongestionHighLastDuration_Object=MibScalar
cegCongestionHighLastDuration=_CegCongestionHighLastDuration_Object((1,3,6,1,4,1,9,9,731,1,3,8,6),_CegCongestionHighLastDuration_Type())
cegCongestionHighLastDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:cegCongestionHighLastDuration.setStatus(_B)
_CegBufferStatus_ObjectIdentity=ObjectIdentity
cegBufferStatus=_CegBufferStatus_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,3,9))
_CegTotalInUseBuffers_Type=Gauge32
_CegTotalInUseBuffers_Object=MibScalar
cegTotalInUseBuffers=_CegTotalInUseBuffers_Object((1,3,6,1,4,1,9,9,731,1,3,9,1),_CegTotalInUseBuffers_Type())
cegTotalInUseBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalInUseBuffers.setStatus(_B)
if mibBuilder.loadTexts:cegTotalInUseBuffers.setUnits(_Z)
_CegTotalBufferedPackets_Type=Gauge32
_CegTotalBufferedPackets_Object=MibScalar
cegTotalBufferedPackets=_CegTotalBufferedPackets_Object((1,3,6,1,4,1,9,9,731,1,3,9,2),_CegTotalBufferedPackets_Type())
cegTotalBufferedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalBufferedPackets.setStatus(_B)
if mibBuilder.loadTexts:cegTotalBufferedPackets.setUnits(_T)
_CegTotalBufferedBytes_Type=Gauge32
_CegTotalBufferedBytes_Object=MibScalar
cegTotalBufferedBytes=_CegTotalBufferedBytes_Object((1,3,6,1,4,1,9,9,731,1,3,9,3),_CegTotalBufferedBytes_Type())
cegTotalBufferedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalBufferedBytes.setStatus(_B)
if mibBuilder.loadTexts:cegTotalBufferedBytes.setUnits(_G)
_CegTotalBufferAvailable_Type=Gauge32
_CegTotalBufferAvailable_Object=MibScalar
cegTotalBufferAvailable=_CegTotalBufferAvailable_Object((1,3,6,1,4,1,9,9,731,1,3,9,4),_CegTotalBufferAvailable_Type())
cegTotalBufferAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalBufferAvailable.setStatus(_B)
if mibBuilder.loadTexts:cegTotalBufferAvailable.setUnits(_G)
_CegActivatedIpv4v6Bearers_Type=Gauge32
_CegActivatedIpv4v6Bearers_Object=MibScalar
cegActivatedIpv4v6Bearers=_CegActivatedIpv4v6Bearers_Object((1,3,6,1,4,1,9,9,731,1,3,10),_CegActivatedIpv4v6Bearers_Type())
cegActivatedIpv4v6Bearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv4v6Bearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv4v6Bearers.setUnits('bearers')
_CegActivatedGtpv2SgwSessions_Type=Gauge32
_CegActivatedGtpv2SgwSessions_Object=MibScalar
cegActivatedGtpv2SgwSessions=_CegActivatedGtpv2SgwSessions_Object((1,3,6,1,4,1,9,9,731,1,3,11),_CegActivatedGtpv2SgwSessions_Type())
cegActivatedGtpv2SgwSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedGtpv2SgwSessions.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedGtpv2SgwSessions.setUnits(_U)
_CegActivatedGtpv2PgwSessions_Type=Gauge32
_CegActivatedGtpv2PgwSessions_Object=MibScalar
cegActivatedGtpv2PgwSessions=_CegActivatedGtpv2PgwSessions_Object((1,3,6,1,4,1,9,9,731,1,3,12),_CegActivatedGtpv2PgwSessions_Type())
cegActivatedGtpv2PgwSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedGtpv2PgwSessions.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedGtpv2PgwSessions.setUnits(_U)
_CegActivatedGtpv2SPgwSessions_Type=Gauge32
_CegActivatedGtpv2SPgwSessions_Object=MibScalar
cegActivatedGtpv2SPgwSessions=_CegActivatedGtpv2SPgwSessions_Object((1,3,6,1,4,1,9,9,731,1,3,13),_CegActivatedGtpv2SPgwSessions_Type())
cegActivatedGtpv2SPgwSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedGtpv2SPgwSessions.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedGtpv2SPgwSessions.setUnits(_U)
_CegActivatedBearers_Type=Gauge32
_CegActivatedBearers_Object=MibScalar
cegActivatedBearers=_CegActivatedBearers_Object((1,3,6,1,4,1,9,9,731,1,3,14),_CegActivatedBearers_Type())
cegActivatedBearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedBearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedBearers.setUnits(_V)
_CegActivatedDedicatedBearers_Type=Gauge32
_CegActivatedDedicatedBearers_Object=MibScalar
cegActivatedDedicatedBearers=_CegActivatedDedicatedBearers_Object((1,3,6,1,4,1,9,9,731,1,3,15),_CegActivatedDedicatedBearers_Type())
cegActivatedDedicatedBearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedDedicatedBearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedDedicatedBearers.setUnits(_V)
_CegActivatedIpv4DedicatedBearers_Type=Gauge32
_CegActivatedIpv4DedicatedBearers_Object=MibScalar
cegActivatedIpv4DedicatedBearers=_CegActivatedIpv4DedicatedBearers_Object((1,3,6,1,4,1,9,9,731,1,3,16),_CegActivatedIpv4DedicatedBearers_Type())
cegActivatedIpv4DedicatedBearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv4DedicatedBearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv4DedicatedBearers.setUnits(_V)
_CegActivatedIpv6DedicatedBearers_Type=Gauge32
_CegActivatedIpv6DedicatedBearers_Object=MibScalar
cegActivatedIpv6DedicatedBearers=_CegActivatedIpv6DedicatedBearers_Object((1,3,6,1,4,1,9,9,731,1,3,17),_CegActivatedIpv6DedicatedBearers_Type())
cegActivatedIpv6DedicatedBearers.setMaxAccess(_C)
if mibBuilder.loadTexts:cegActivatedIpv6DedicatedBearers.setStatus(_B)
if mibBuilder.loadTexts:cegActivatedIpv6DedicatedBearers.setUnits(_V)
_CegTotalIdleSessions_Type=Gauge32
_CegTotalIdleSessions_Object=MibScalar
cegTotalIdleSessions=_CegTotalIdleSessions_Object((1,3,6,1,4,1,9,9,731,1,3,18),_CegTotalIdleSessions_Type())
cegTotalIdleSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cegTotalIdleSessions.setStatus(_B)
if mibBuilder.loadTexts:cegTotalIdleSessions.setUnits('Sessions')
_CiscoEpcGatewayNotifMgmt_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayNotifMgmt=_CiscoEpcGatewayNotifMgmt_ObjectIdentity((1,3,6,1,4,1,9,9,731,1,4))
class _CegCongestionHighNotifEnable_Type(TruthValue):defaultValue=2
_CegCongestionHighNotifEnable_Type.__name__=_F
_CegCongestionHighNotifEnable_Object=MibScalar
cegCongestionHighNotifEnable=_CegCongestionHighNotifEnable_Object((1,3,6,1,4,1,9,9,731,1,4,1),_CegCongestionHighNotifEnable_Type())
cegCongestionHighNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cegCongestionHighNotifEnable.setStatus(_B)
class _CegCongestionLowNotifEnable_Type(TruthValue):defaultValue=2
_CegCongestionLowNotifEnable_Type.__name__=_F
_CegCongestionLowNotifEnable_Object=MibScalar
cegCongestionLowNotifEnable=_CegCongestionLowNotifEnable_Object((1,3,6,1,4,1,9,9,731,1,4,2),_CegCongestionLowNotifEnable_Type())
cegCongestionLowNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cegCongestionLowNotifEnable.setStatus(_B)
class _CegCongestionClearNotifEnable_Type(TruthValue):defaultValue=2
_CegCongestionClearNotifEnable_Type.__name__=_F
_CegCongestionClearNotifEnable_Object=MibScalar
cegCongestionClearNotifEnable=_CegCongestionClearNotifEnable_Object((1,3,6,1,4,1,9,9,731,1,4,3),_CegCongestionClearNotifEnable_Type())
cegCongestionClearNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cegCongestionClearNotifEnable.setStatus(_B)
_CiscoEpcGatewayMIBConformance_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayMIBConformance=_CiscoEpcGatewayMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,731,3))
_CiscoEpcGatewayMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayMIBCompliances=_CiscoEpcGatewayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,731,3,1))
_CiscoEpcGatewayMIBGroups_ObjectIdentity=ObjectIdentity
ciscoEpcGatewayMIBGroups=_CiscoEpcGatewayMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,731,3,2))
cegSystemStatusGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,1))
cegSystemStatusGrp.setObjects(*((_A,_H),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:cegSystemStatusGrp.setStatus(_B)
cegOverloadProtectionStatsGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,2))
cegOverloadProtectionStatsGrp.setObjects(*((_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:cegOverloadProtectionStatsGrp.setStatus(_B)
cegBufferingAgentStatsGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,3))
cegBufferingAgentStatsGrp.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:cegBufferingAgentStatsGrp.setStatus(_B)
cegOverloadProtectionConfigGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,4))
cegOverloadProtectionConfigGrp.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cegOverloadProtectionConfigGrp.setStatus(_B)
cegBufferingAgentConfigGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,5))
cegBufferingAgentConfigGrp.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:cegBufferingAgentConfigGrp.setStatus(_B)
cegBufferingAgentStatusGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,6))
cegBufferingAgentStatusGrp.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:cegBufferingAgentStatusGrp.setStatus(_B)
cegOverloadProtectionStatusGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,7))
cegOverloadProtectionStatusGrp.setObjects(*((_A,_I),(_A,_J),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cegOverloadProtectionStatusGrp.setStatus(_B)
cegOverloadProtectionNotifMgmtGrp=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,8))
cegOverloadProtectionNotifMgmtGrp.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:cegOverloadProtectionNotifMgmtGrp.setStatus(_B)
cegSystemStatusGrpSup1=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,10))
cegSystemStatusGrpSup1.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:cegSystemStatusGrpSup1.setStatus(_B)
cegSystemStatusGrpSup2=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,11))
cegSystemStatusGrpSup2.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:cegSystemStatusGrpSup2.setStatus(_B)
cegSystemStatusGrpSup3=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,12))
cegSystemStatusGrpSup3.setObjects((_A,_AL))
if mibBuilder.loadTexts:cegSystemStatusGrpSup3.setStatus(_B)
cegBufferingAgentStatsGrpSup1=ObjectGroup((1,3,6,1,4,1,9,9,731,3,2,13))
cegBufferingAgentStatsGrpSup1.setObjects(*((_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cegBufferingAgentStatsGrpSup1.setStatus(_B)
cegCongestionHighThresholdNotif=NotificationType((1,3,6,1,4,1,9,9,731,0,1))
cegCongestionHighThresholdNotif.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_X)))
if mibBuilder.loadTexts:cegCongestionHighThresholdNotif.setStatus(_B)
cegCongestionLowThresholdNotif=NotificationType((1,3,6,1,4,1,9,9,731,0,2))
cegCongestionLowThresholdNotif.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cegCongestionLowThresholdNotif.setStatus(_B)
cegCongestionClearedNotif=NotificationType((1,3,6,1,4,1,9,9,731,0,3))
cegCongestionClearedNotif.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_W)))
if mibBuilder.loadTexts:cegCongestionClearedNotif.setStatus(_B)
cegOverloadProtectionNotifGrp=NotificationGroup((1,3,6,1,4,1,9,9,731,3,2,9))
cegOverloadProtectionNotifGrp.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:cegOverloadProtectionNotifGrp.setStatus(_B)
ciscoEpcGatewayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,731,3,1,1))
ciscoEpcGatewayMIBCompliance.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoEpcGatewayMIBCompliance.setStatus(_a)
ciscoEpcGatewayMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,731,3,1,2))
ciscoEpcGatewayMIBComplianceRev1.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoEpcGatewayMIBComplianceRev1.setStatus(_a)
ciscoEPCGatewayMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,731,3,1,3))
ciscoEPCGatewayMIBComplianceRev2.setObjects(*((_A,_K),(_A,_M),(_A,_O),(_A,_L),(_A,_N),(_A,_P),(_A,_Y),(_A,_b),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoEPCGatewayMIBComplianceRev2.setStatus(_a)
ciscoEpcGatewayMIBComplianceRev3=ModuleCompliance((1,3,6,1,4,1,9,9,731,3,1,4))
ciscoEpcGatewayMIBComplianceRev3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Y),(_A,_b),(_A,_AR),(_A,_Q),(_A,_R),(_A,_S),(_A,_AS)))
if mibBuilder.loadTexts:ciscoEpcGatewayMIBComplianceRev3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoEpcGatewayMIB':ciscoEpcGatewayMIB,'ciscoEpcGatewayMIBNotifications':ciscoEpcGatewayMIBNotifications,_AO:cegCongestionHighThresholdNotif,_AP:cegCongestionLowThresholdNotif,_AQ:cegCongestionClearedNotif,'ciscoEpcGatewayMIBObjects':ciscoEpcGatewayMIBObjects,'ciscoEpcGatewayStatistics':ciscoEpcGatewayStatistics,'cegOverloadProtectionStats':cegOverloadProtectionStats,_m:cegCongestionIncomingReqDrops,_o:cegCongestionLowThresholdReached,_n:cegCongestionHighThresholdReached,'cegBufferStats':cegBufferStats,_p:cegBuffersCreated,_u:cegBuffersDeleted,_v:cegBuffersTimedOut,_q:cegBufferPacketsEnqueued,_s:cegBufferPacketsDequeued,_r:cegBufferBytesEnqueued,_t:cegBufferBytesDequeued,_w:cegBufferRejMemUnavailable,_x:cegBufferRejLowMem,_AM:cegPacketDropDueToMaxPacketLimit,_AN:cegPacketDropDueToMaxBufferLimit,'ciscoEpcGatewayConfig':ciscoEpcGatewayConfig,'cegOverloadProtectionConfig':cegOverloadProtectionConfig,_W:cegCongestionLowThreshold,_X:cegCongestionHighThreshold,'cegBufferingAgentConfig':cegBufferingAgentConfig,_y:cegBufferingAgentEnabled,_z:cegBufferMaxSize,_A0:cegBufferDiscardDataTime,_A1:cegBufferMaxPacketsPerBuffer,'ciscoEpcGatewayStatus':ciscoEpcGatewayStatus,_H:cegVersion,_g:cegActivatedIpv4Bearers,_h:cegActivatedIpv6Bearers,_i:cegTotalUsers,_l:cegTotalIdleUsers,_j:cegTotalSuspendedUsers,_k:cegActivatedIpv4v6Sessions,'cegOverloadProtectionStatus':cegOverloadProtectionStatus,_I:cegCongestionDfpWeight,_J:cegCongestionStatus,_A6:cegCongestionLowLastOccurTime,_A7:cegCongestionLowLastDuration,_A8:cegCongestionHighLastOccurTime,_A9:cegCongestionHighLastDuration,'cegBufferStatus':cegBufferStatus,_A2:cegTotalInUseBuffers,_A3:cegTotalBufferedPackets,_A4:cegTotalBufferedBytes,_A5:cegTotalBufferAvailable,_AD:cegActivatedIpv4v6Bearers,_AE:cegActivatedGtpv2SgwSessions,_AF:cegActivatedGtpv2PgwSessions,_AG:cegActivatedGtpv2SPgwSessions,_AH:cegActivatedBearers,_AI:cegActivatedDedicatedBearers,_AJ:cegActivatedIpv4DedicatedBearers,_AK:cegActivatedIpv6DedicatedBearers,_AL:cegTotalIdleSessions,'ciscoEpcGatewayNotifMgmt':ciscoEpcGatewayNotifMgmt,_AA:cegCongestionHighNotifEnable,_AB:cegCongestionLowNotifEnable,_AC:cegCongestionClearNotifEnable,'ciscoEpcGatewayMIBConformance':ciscoEpcGatewayMIBConformance,'ciscoEpcGatewayMIBCompliances':ciscoEpcGatewayMIBCompliances,'ciscoEpcGatewayMIBCompliance':ciscoEpcGatewayMIBCompliance,'ciscoEpcGatewayMIBComplianceRev1':ciscoEpcGatewayMIBComplianceRev1,'ciscoEPCGatewayMIBComplianceRev2':ciscoEPCGatewayMIBComplianceRev2,'ciscoEpcGatewayMIBComplianceRev3':ciscoEpcGatewayMIBComplianceRev3,'ciscoEpcGatewayMIBGroups':ciscoEpcGatewayMIBGroups,_K:cegSystemStatusGrp,_L:cegOverloadProtectionStatsGrp,_Q:cegBufferingAgentStatsGrp,_M:cegOverloadProtectionConfigGrp,_R:cegBufferingAgentConfigGrp,_S:cegBufferingAgentStatusGrp,_N:cegOverloadProtectionStatusGrp,_O:cegOverloadProtectionNotifMgmtGrp,_P:cegOverloadProtectionNotifGrp,_Y:cegSystemStatusGrpSup1,_b:cegSystemStatusGrpSup2,_AR:cegSystemStatusGrpSup3,_AS:cegBufferingAgentStatsGrpSup1})