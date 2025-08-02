_Ab='cDhcpv4SrvExtNotifyGroup'
_Aa='cDhcpv4ServerSubnetFreeAddressHigh'
_AZ='cDhcpv4ServerSubnetFreeAddressLow'
_AY='cDhcpv4ServerIfLeaseLimitExceeded'
_AX='cDhcpv4ServerIfLeaseLimitDefault'
_AW='cDhcpv4ServerSubnetFreeAddressHighEnable'
_AV='cDhcpv4ServerSubnetFreeAddressLowEnable'
_AU='cDhcpv4ServerIfLeaseLimitEnable'
_AT='cDhcpv4ServerSubnetEndAddress'
_AS='cDhcpv4ServerSubnetStartAddress'
_AR='cDhcpv4ServerDefaultRouterAddress'
_AQ='cDhcpv4ConfigIntervalSample'
_AP='cDhcpv4FOIntDeltaTime'
_AO='cDhcpv4FOIntEndTime'
_AN='cDhcpv4FOIntPacketsDropped'
_AM='cDhcpv4FOIntUpdateDoneSent'
_AL='cDhcpv4FOIntUpdateReqsSent'
_AK='cDhcpv4FOIntPollsSent'
_AJ='cDhcpv4FOIntPoolResponsesSent'
_AI='cDhcpv4FOIntBindingNaksSent'
_AH='cDhcpv4FOIntBindingAcksSent'
_AG='cDhcpv4FOIntBindingUpdsSent'
_AF='cDhcpv4FOIntPacketsSent'
_AE='cDhcpv4FOIntUpdateDoneRcvd'
_AD='cDhcpv4FOIntUpdateReqsRcvd'
_AC='cDhcpv4FOIntPollsRcvd'
_AB='cDhcpv4FOIntPoolRequestsRcvd'
_AA='cDhcpv4FOIntBindingNaksRcvd'
_A9='cDhcpv4FOIntBindingAcksRcvd'
_A8='cDhcpv4FOIntBindingUpdsRcvd'
_A7='cDhcpv4FOIntPacketsRcvd'
_A6='cDhcpv4FOPacketsDropped'
_A5='cDhcpv4FOUpdateDoneSent'
_A4='cDhcpv4FOUpdateRequestsSent'
_A3='cDhcpv4FOPollsSent'
_A2='cDhcpv4FOPoolResponsesSent'
_A1='cDhcpv4FOBindingNaksSent'
_A0='cDhcpv4FOBindingAcksSent'
_z='cDhcpv4FOBindingUpdatesSent'
_y='cDhcpv4FOPacketsSent'
_x='cDhcpv4FOUpdateDoneRcvd'
_w='cDhcpv4FOUpdateRequestsRcvd'
_v='cDhcpv4FOPollsRcvd'
_u='cDhcpv4FOPoolRequestsRcvd'
_t='cDhcpv4FOBindingNaksRcvd'
_s='cDhcpv4FOBindingAcksRcvd'
_r='cDhcpv4FOBindingUpdsRcvd'
_q='cDhcpv4FOPacketsRcvd'
_p='cDhcpv4IntDeltaTime'
_o='cDhcpv4IntEndTime'
_n='cDhcpv4IntReqBuffersInUse'
_m='cDhcpv4IntRespBuffersInUse'
_l='cDhcpv4IntReleases'
_k='cDhcpv4IntLeaseQueries'
_j='cDhcpv4IntInforms'
_i='cDhcpv4IntNaks'
_h='cDhcpv4IntAcks'
_g='cDhcpv4IntDeclines'
_f='cDhcpv4IntRequests'
_e='cDhcpv4IntOffers'
_d='cDhcpv4IntDiscovers'
_c='cDhcpv4StatisticsResetTime'
_b='cDhcpv4LeaseQueries'
_a='cDhcpv4SrvResetTime'
_Z='cDhcpv4SrvStartTime'
_Y='cDhcpv4SrvExtSubnetEntry'
_X='buffers'
_W='ifName'
_V='ifIndex'
_U='cDhcpv4ServerSubnetFreeAddrLowThreshold'
_T='cDhcpv4ServerSubnetFreeAddrHighThreshold'
_S='cDhcpv4ServerClientPhysicalAddress'
_R='cDhcpv4CfgObjectsGroup'
_Q='cDhcpv4FOCountersIntervalGroup'
_P='cDhcpv4FOCountersGroup'
_O='cDhcpv4CountersIntervalGroup'
_N='cDhcpv4ExtCountersGroup'
_M='cDhcpv4SrvExtSystemObjects'
_L='cDhcpv4ServerIfLeaseLimit'
_K='milliseconds'
_J='Unsigned32'
_I='IF-MIB'
_H='cDhcpv4ServerSubnetFreeAddresses'
_G='TruthValue'
_F='CISCO-IETF-DHCP-SERVER-MIB'
_E='read-write'
_D='packets'
_C='read-only'
_B='current'
_A='CISCO-IETF-DHCP-SERVER-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cDhcpv4ServerClientPhysicalAddress,cDhcpv4ServerSubnetEntry,cDhcpv4ServerSubnetFreeAddrHighThreshold,cDhcpv4ServerSubnetFreeAddrLowThreshold,cDhcpv4ServerSubnetFreeAddresses=mibBuilder.importSymbols(_F,_S,'cDhcpv4ServerSubnetEntry',_T,_U,_H)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,ifName=mibBuilder.importSymbols(_I,_V,_W)
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp',_G)
ciscoIetfDhcpSrvExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,122))
if mibBuilder.loadTexts:ciscoIetfDhcpSrvExtMIB.setRevisions(('2007-03-15 12:00','2005-05-04 12:00'))
_CiscoIetfDhcpv4SrvExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBNotifs=_CiscoIetfDhcpv4SrvExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,10,122,0))
_CDhcpv4SrvExtNotifyPrefix_ObjectIdentity=ObjectIdentity
cDhcpv4SrvExtNotifyPrefix=_CDhcpv4SrvExtNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,122,0,2))
_CDhcpv4SrvExtNotify_ObjectIdentity=ObjectIdentity
cDhcpv4SrvExtNotify=_CDhcpv4SrvExtNotify_ObjectIdentity((1,3,6,1,4,1,9,10,122,0,2,0))
_CiscoIetfDhcpv4SrvExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBObjects=_CiscoIetfDhcpv4SrvExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,122,1))
_CDhcpv4SrvExtSystem_ObjectIdentity=ObjectIdentity
cDhcpv4SrvExtSystem=_CDhcpv4SrvExtSystem_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,1))
_CDhcpv4SrvStartTime_Type=TimeStamp
_CDhcpv4SrvStartTime_Object=MibScalar
cDhcpv4SrvStartTime=_CDhcpv4SrvStartTime_Object((1,3,6,1,4,1,9,10,122,1,1,1),_CDhcpv4SrvStartTime_Type())
cDhcpv4SrvStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4SrvStartTime.setStatus(_B)
_CDhcpv4SrvResetTime_Type=TimeStamp
_CDhcpv4SrvResetTime_Object=MibScalar
cDhcpv4SrvResetTime=_CDhcpv4SrvResetTime_Object((1,3,6,1,4,1,9,10,122,1,1,2),_CDhcpv4SrvResetTime_Type())
cDhcpv4SrvResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4SrvResetTime.setStatus(_B)
_CDhcpv4ExtCounters_ObjectIdentity=ObjectIdentity
cDhcpv4ExtCounters=_CDhcpv4ExtCounters_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,2))
_CDhcpv4LeaseQueries_Type=Counter32
_CDhcpv4LeaseQueries_Object=MibScalar
cDhcpv4LeaseQueries=_CDhcpv4LeaseQueries_Object((1,3,6,1,4,1,9,10,122,1,2,1),_CDhcpv4LeaseQueries_Type())
cDhcpv4LeaseQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4LeaseQueries.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4LeaseQueries.setUnits(_D)
_CDhcpv4StatisticsResetTime_Type=TimeStamp
_CDhcpv4StatisticsResetTime_Object=MibScalar
cDhcpv4StatisticsResetTime=_CDhcpv4StatisticsResetTime_Object((1,3,6,1,4,1,9,10,122,1,2,2),_CDhcpv4StatisticsResetTime_Type())
cDhcpv4StatisticsResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4StatisticsResetTime.setStatus(_B)
_CDhcpv4IntervalCounters_ObjectIdentity=ObjectIdentity
cDhcpv4IntervalCounters=_CDhcpv4IntervalCounters_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,3))
_CDhcpv4IntDiscovers_Type=Unsigned32
_CDhcpv4IntDiscovers_Object=MibScalar
cDhcpv4IntDiscovers=_CDhcpv4IntDiscovers_Object((1,3,6,1,4,1,9,10,122,1,3,1),_CDhcpv4IntDiscovers_Type())
cDhcpv4IntDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntDiscovers.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntDiscovers.setUnits(_D)
_CDhcpv4IntOffers_Type=Unsigned32
_CDhcpv4IntOffers_Object=MibScalar
cDhcpv4IntOffers=_CDhcpv4IntOffers_Object((1,3,6,1,4,1,9,10,122,1,3,2),_CDhcpv4IntOffers_Type())
cDhcpv4IntOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntOffers.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntOffers.setUnits(_D)
_CDhcpv4IntRequests_Type=Unsigned32
_CDhcpv4IntRequests_Object=MibScalar
cDhcpv4IntRequests=_CDhcpv4IntRequests_Object((1,3,6,1,4,1,9,10,122,1,3,3),_CDhcpv4IntRequests_Type())
cDhcpv4IntRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntRequests.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntRequests.setUnits(_D)
_CDhcpv4IntDeclines_Type=Unsigned32
_CDhcpv4IntDeclines_Object=MibScalar
cDhcpv4IntDeclines=_CDhcpv4IntDeclines_Object((1,3,6,1,4,1,9,10,122,1,3,4),_CDhcpv4IntDeclines_Type())
cDhcpv4IntDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntDeclines.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntDeclines.setUnits(_D)
_CDhcpv4IntAcks_Type=Unsigned32
_CDhcpv4IntAcks_Object=MibScalar
cDhcpv4IntAcks=_CDhcpv4IntAcks_Object((1,3,6,1,4,1,9,10,122,1,3,5),_CDhcpv4IntAcks_Type())
cDhcpv4IntAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntAcks.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntAcks.setUnits(_D)
_CDhcpv4IntNaks_Type=Unsigned32
_CDhcpv4IntNaks_Object=MibScalar
cDhcpv4IntNaks=_CDhcpv4IntNaks_Object((1,3,6,1,4,1,9,10,122,1,3,6),_CDhcpv4IntNaks_Type())
cDhcpv4IntNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntNaks.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntNaks.setUnits(_D)
_CDhcpv4IntReleases_Type=Unsigned32
_CDhcpv4IntReleases_Object=MibScalar
cDhcpv4IntReleases=_CDhcpv4IntReleases_Object((1,3,6,1,4,1,9,10,122,1,3,7),_CDhcpv4IntReleases_Type())
cDhcpv4IntReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntReleases.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntReleases.setUnits(_D)
_CDhcpv4IntInforms_Type=Unsigned32
_CDhcpv4IntInforms_Object=MibScalar
cDhcpv4IntInforms=_CDhcpv4IntInforms_Object((1,3,6,1,4,1,9,10,122,1,3,8),_CDhcpv4IntInforms_Type())
cDhcpv4IntInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntInforms.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntInforms.setUnits(_D)
_CDhcpv4IntLeaseQueries_Type=Unsigned32
_CDhcpv4IntLeaseQueries_Object=MibScalar
cDhcpv4IntLeaseQueries=_CDhcpv4IntLeaseQueries_Object((1,3,6,1,4,1,9,10,122,1,3,9),_CDhcpv4IntLeaseQueries_Type())
cDhcpv4IntLeaseQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntLeaseQueries.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntLeaseQueries.setUnits(_D)
_CDhcpv4IntReqBuffersInUse_Type=Gauge32
_CDhcpv4IntReqBuffersInUse_Object=MibScalar
cDhcpv4IntReqBuffersInUse=_CDhcpv4IntReqBuffersInUse_Object((1,3,6,1,4,1,9,10,122,1,3,10),_CDhcpv4IntReqBuffersInUse_Type())
cDhcpv4IntReqBuffersInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntReqBuffersInUse.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntReqBuffersInUse.setUnits(_X)
_CDhcpv4IntRespBuffersInUse_Type=Gauge32
_CDhcpv4IntRespBuffersInUse_Object=MibScalar
cDhcpv4IntRespBuffersInUse=_CDhcpv4IntRespBuffersInUse_Object((1,3,6,1,4,1,9,10,122,1,3,11),_CDhcpv4IntRespBuffersInUse_Type())
cDhcpv4IntRespBuffersInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntRespBuffersInUse.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntRespBuffersInUse.setUnits(_X)
_CDhcpv4IntEndTime_Type=TimeStamp
_CDhcpv4IntEndTime_Object=MibScalar
cDhcpv4IntEndTime=_CDhcpv4IntEndTime_Object((1,3,6,1,4,1,9,10,122,1,3,12),_CDhcpv4IntEndTime_Type())
cDhcpv4IntEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntEndTime.setStatus(_B)
_CDhcpv4IntDeltaTime_Type=TimeInterval
_CDhcpv4IntDeltaTime_Object=MibScalar
cDhcpv4IntDeltaTime=_CDhcpv4IntDeltaTime_Object((1,3,6,1,4,1,9,10,122,1,3,13),_CDhcpv4IntDeltaTime_Type())
cDhcpv4IntDeltaTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4IntDeltaTime.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4IntDeltaTime.setUnits(_K)
_CDhcpv4FailoverCounters_ObjectIdentity=ObjectIdentity
cDhcpv4FailoverCounters=_CDhcpv4FailoverCounters_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,4))
_CDhcpv4FOPacketsRcvd_Type=Counter32
_CDhcpv4FOPacketsRcvd_Object=MibScalar
cDhcpv4FOPacketsRcvd=_CDhcpv4FOPacketsRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,1),_CDhcpv4FOPacketsRcvd_Type())
cDhcpv4FOPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPacketsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPacketsRcvd.setUnits(_D)
_CDhcpv4FOBindingUpdsRcvd_Type=Counter32
_CDhcpv4FOBindingUpdsRcvd_Object=MibScalar
cDhcpv4FOBindingUpdsRcvd=_CDhcpv4FOBindingUpdsRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,2),_CDhcpv4FOBindingUpdsRcvd_Type())
cDhcpv4FOBindingUpdsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingUpdsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingUpdsRcvd.setUnits(_D)
_CDhcpv4FOBindingAcksRcvd_Type=Counter32
_CDhcpv4FOBindingAcksRcvd_Object=MibScalar
cDhcpv4FOBindingAcksRcvd=_CDhcpv4FOBindingAcksRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,3),_CDhcpv4FOBindingAcksRcvd_Type())
cDhcpv4FOBindingAcksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingAcksRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingAcksRcvd.setUnits(_D)
_CDhcpv4FOBindingNaksRcvd_Type=Counter32
_CDhcpv4FOBindingNaksRcvd_Object=MibScalar
cDhcpv4FOBindingNaksRcvd=_CDhcpv4FOBindingNaksRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,4),_CDhcpv4FOBindingNaksRcvd_Type())
cDhcpv4FOBindingNaksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingNaksRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingNaksRcvd.setUnits(_D)
_CDhcpv4FOPoolRequestsRcvd_Type=Counter32
_CDhcpv4FOPoolRequestsRcvd_Object=MibScalar
cDhcpv4FOPoolRequestsRcvd=_CDhcpv4FOPoolRequestsRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,5),_CDhcpv4FOPoolRequestsRcvd_Type())
cDhcpv4FOPoolRequestsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPoolRequestsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPoolRequestsRcvd.setUnits(_D)
_CDhcpv4FOPollsRcvd_Type=Counter32
_CDhcpv4FOPollsRcvd_Object=MibScalar
cDhcpv4FOPollsRcvd=_CDhcpv4FOPollsRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,6),_CDhcpv4FOPollsRcvd_Type())
cDhcpv4FOPollsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPollsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPollsRcvd.setUnits(_D)
_CDhcpv4FOUpdateRequestsRcvd_Type=Counter32
_CDhcpv4FOUpdateRequestsRcvd_Object=MibScalar
cDhcpv4FOUpdateRequestsRcvd=_CDhcpv4FOUpdateRequestsRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,7),_CDhcpv4FOUpdateRequestsRcvd_Type())
cDhcpv4FOUpdateRequestsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOUpdateRequestsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOUpdateRequestsRcvd.setUnits(_D)
_CDhcpv4FOUpdateDoneRcvd_Type=Counter32
_CDhcpv4FOUpdateDoneRcvd_Object=MibScalar
cDhcpv4FOUpdateDoneRcvd=_CDhcpv4FOUpdateDoneRcvd_Object((1,3,6,1,4,1,9,10,122,1,4,8),_CDhcpv4FOUpdateDoneRcvd_Type())
cDhcpv4FOUpdateDoneRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOUpdateDoneRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOUpdateDoneRcvd.setUnits(_D)
_CDhcpv4FOPacketsSent_Type=Counter32
_CDhcpv4FOPacketsSent_Object=MibScalar
cDhcpv4FOPacketsSent=_CDhcpv4FOPacketsSent_Object((1,3,6,1,4,1,9,10,122,1,4,9),_CDhcpv4FOPacketsSent_Type())
cDhcpv4FOPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPacketsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPacketsSent.setUnits(_D)
_CDhcpv4FOBindingUpdatesSent_Type=Counter32
_CDhcpv4FOBindingUpdatesSent_Object=MibScalar
cDhcpv4FOBindingUpdatesSent=_CDhcpv4FOBindingUpdatesSent_Object((1,3,6,1,4,1,9,10,122,1,4,10),_CDhcpv4FOBindingUpdatesSent_Type())
cDhcpv4FOBindingUpdatesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingUpdatesSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingUpdatesSent.setUnits(_D)
_CDhcpv4FOBindingAcksSent_Type=Counter32
_CDhcpv4FOBindingAcksSent_Object=MibScalar
cDhcpv4FOBindingAcksSent=_CDhcpv4FOBindingAcksSent_Object((1,3,6,1,4,1,9,10,122,1,4,11),_CDhcpv4FOBindingAcksSent_Type())
cDhcpv4FOBindingAcksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingAcksSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingAcksSent.setUnits(_D)
_CDhcpv4FOBindingNaksSent_Type=Counter32
_CDhcpv4FOBindingNaksSent_Object=MibScalar
cDhcpv4FOBindingNaksSent=_CDhcpv4FOBindingNaksSent_Object((1,3,6,1,4,1,9,10,122,1,4,12),_CDhcpv4FOBindingNaksSent_Type())
cDhcpv4FOBindingNaksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOBindingNaksSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOBindingNaksSent.setUnits(_D)
_CDhcpv4FOPoolResponsesSent_Type=Counter32
_CDhcpv4FOPoolResponsesSent_Object=MibScalar
cDhcpv4FOPoolResponsesSent=_CDhcpv4FOPoolResponsesSent_Object((1,3,6,1,4,1,9,10,122,1,4,13),_CDhcpv4FOPoolResponsesSent_Type())
cDhcpv4FOPoolResponsesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPoolResponsesSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPoolResponsesSent.setUnits(_D)
_CDhcpv4FOPollsSent_Type=Counter32
_CDhcpv4FOPollsSent_Object=MibScalar
cDhcpv4FOPollsSent=_CDhcpv4FOPollsSent_Object((1,3,6,1,4,1,9,10,122,1,4,14),_CDhcpv4FOPollsSent_Type())
cDhcpv4FOPollsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPollsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPollsSent.setUnits(_D)
_CDhcpv4FOUpdateRequestsSent_Type=Counter32
_CDhcpv4FOUpdateRequestsSent_Object=MibScalar
cDhcpv4FOUpdateRequestsSent=_CDhcpv4FOUpdateRequestsSent_Object((1,3,6,1,4,1,9,10,122,1,4,15),_CDhcpv4FOUpdateRequestsSent_Type())
cDhcpv4FOUpdateRequestsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOUpdateRequestsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOUpdateRequestsSent.setUnits(_D)
_CDhcpv4FOUpdateDoneSent_Type=Counter32
_CDhcpv4FOUpdateDoneSent_Object=MibScalar
cDhcpv4FOUpdateDoneSent=_CDhcpv4FOUpdateDoneSent_Object((1,3,6,1,4,1,9,10,122,1,4,16),_CDhcpv4FOUpdateDoneSent_Type())
cDhcpv4FOUpdateDoneSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOUpdateDoneSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOUpdateDoneSent.setUnits(_D)
_CDhcpv4FOPacketsDropped_Type=Counter32
_CDhcpv4FOPacketsDropped_Object=MibScalar
cDhcpv4FOPacketsDropped=_CDhcpv4FOPacketsDropped_Object((1,3,6,1,4,1,9,10,122,1,4,17),_CDhcpv4FOPacketsDropped_Type())
cDhcpv4FOPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOPacketsDropped.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOPacketsDropped.setUnits(_D)
_CDhcpv4FailoverIntervalCounters_ObjectIdentity=ObjectIdentity
cDhcpv4FailoverIntervalCounters=_CDhcpv4FailoverIntervalCounters_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,5))
_CDhcpv4FOIntPacketsRcvd_Type=Unsigned32
_CDhcpv4FOIntPacketsRcvd_Object=MibScalar
cDhcpv4FOIntPacketsRcvd=_CDhcpv4FOIntPacketsRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,1),_CDhcpv4FOIntPacketsRcvd_Type())
cDhcpv4FOIntPacketsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsRcvd.setUnits(_D)
_CDhcpv4FOIntBindingUpdsRcvd_Type=Unsigned32
_CDhcpv4FOIntBindingUpdsRcvd_Object=MibScalar
cDhcpv4FOIntBindingUpdsRcvd=_CDhcpv4FOIntBindingUpdsRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,2),_CDhcpv4FOIntBindingUpdsRcvd_Type())
cDhcpv4FOIntBindingUpdsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingUpdsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingUpdsRcvd.setUnits(_D)
_CDhcpv4FOIntBindingAcksRcvd_Type=Unsigned32
_CDhcpv4FOIntBindingAcksRcvd_Object=MibScalar
cDhcpv4FOIntBindingAcksRcvd=_CDhcpv4FOIntBindingAcksRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,3),_CDhcpv4FOIntBindingAcksRcvd_Type())
cDhcpv4FOIntBindingAcksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingAcksRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingAcksRcvd.setUnits(_D)
_CDhcpv4FOIntBindingNaksRcvd_Type=Unsigned32
_CDhcpv4FOIntBindingNaksRcvd_Object=MibScalar
cDhcpv4FOIntBindingNaksRcvd=_CDhcpv4FOIntBindingNaksRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,4),_CDhcpv4FOIntBindingNaksRcvd_Type())
cDhcpv4FOIntBindingNaksRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingNaksRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingNaksRcvd.setUnits(_D)
_CDhcpv4FOIntPoolRequestsRcvd_Type=Unsigned32
_CDhcpv4FOIntPoolRequestsRcvd_Object=MibScalar
cDhcpv4FOIntPoolRequestsRcvd=_CDhcpv4FOIntPoolRequestsRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,5),_CDhcpv4FOIntPoolRequestsRcvd_Type())
cDhcpv4FOIntPoolRequestsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPoolRequestsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPoolRequestsRcvd.setUnits(_D)
_CDhcpv4FOIntPollsRcvd_Type=Unsigned32
_CDhcpv4FOIntPollsRcvd_Object=MibScalar
cDhcpv4FOIntPollsRcvd=_CDhcpv4FOIntPollsRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,6),_CDhcpv4FOIntPollsRcvd_Type())
cDhcpv4FOIntPollsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPollsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPollsRcvd.setUnits(_D)
_CDhcpv4FOIntUpdateReqsRcvd_Type=Unsigned32
_CDhcpv4FOIntUpdateReqsRcvd_Object=MibScalar
cDhcpv4FOIntUpdateReqsRcvd=_CDhcpv4FOIntUpdateReqsRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,7),_CDhcpv4FOIntUpdateReqsRcvd_Type())
cDhcpv4FOIntUpdateReqsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateReqsRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateReqsRcvd.setUnits(_D)
_CDhcpv4FOIntUpdateDoneRcvd_Type=Unsigned32
_CDhcpv4FOIntUpdateDoneRcvd_Object=MibScalar
cDhcpv4FOIntUpdateDoneRcvd=_CDhcpv4FOIntUpdateDoneRcvd_Object((1,3,6,1,4,1,9,10,122,1,5,8),_CDhcpv4FOIntUpdateDoneRcvd_Type())
cDhcpv4FOIntUpdateDoneRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateDoneRcvd.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateDoneRcvd.setUnits(_D)
_CDhcpv4FOIntPacketsSent_Type=Unsigned32
_CDhcpv4FOIntPacketsSent_Object=MibScalar
cDhcpv4FOIntPacketsSent=_CDhcpv4FOIntPacketsSent_Object((1,3,6,1,4,1,9,10,122,1,5,9),_CDhcpv4FOIntPacketsSent_Type())
cDhcpv4FOIntPacketsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsSent.setUnits(_D)
_CDhcpv4FOIntBindingUpdsSent_Type=Unsigned32
_CDhcpv4FOIntBindingUpdsSent_Object=MibScalar
cDhcpv4FOIntBindingUpdsSent=_CDhcpv4FOIntBindingUpdsSent_Object((1,3,6,1,4,1,9,10,122,1,5,10),_CDhcpv4FOIntBindingUpdsSent_Type())
cDhcpv4FOIntBindingUpdsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingUpdsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingUpdsSent.setUnits(_D)
_CDhcpv4FOIntBindingAcksSent_Type=Unsigned32
_CDhcpv4FOIntBindingAcksSent_Object=MibScalar
cDhcpv4FOIntBindingAcksSent=_CDhcpv4FOIntBindingAcksSent_Object((1,3,6,1,4,1,9,10,122,1,5,11),_CDhcpv4FOIntBindingAcksSent_Type())
cDhcpv4FOIntBindingAcksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingAcksSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingAcksSent.setUnits(_D)
_CDhcpv4FOIntBindingNaksSent_Type=Unsigned32
_CDhcpv4FOIntBindingNaksSent_Object=MibScalar
cDhcpv4FOIntBindingNaksSent=_CDhcpv4FOIntBindingNaksSent_Object((1,3,6,1,4,1,9,10,122,1,5,12),_CDhcpv4FOIntBindingNaksSent_Type())
cDhcpv4FOIntBindingNaksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingNaksSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntBindingNaksSent.setUnits(_D)
_CDhcpv4FOIntPoolResponsesSent_Type=Unsigned32
_CDhcpv4FOIntPoolResponsesSent_Object=MibScalar
cDhcpv4FOIntPoolResponsesSent=_CDhcpv4FOIntPoolResponsesSent_Object((1,3,6,1,4,1,9,10,122,1,5,13),_CDhcpv4FOIntPoolResponsesSent_Type())
cDhcpv4FOIntPoolResponsesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPoolResponsesSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPoolResponsesSent.setUnits(_D)
_CDhcpv4FOIntPollsSent_Type=Unsigned32
_CDhcpv4FOIntPollsSent_Object=MibScalar
cDhcpv4FOIntPollsSent=_CDhcpv4FOIntPollsSent_Object((1,3,6,1,4,1,9,10,122,1,5,14),_CDhcpv4FOIntPollsSent_Type())
cDhcpv4FOIntPollsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPollsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPollsSent.setUnits(_D)
_CDhcpv4FOIntUpdateReqsSent_Type=Unsigned32
_CDhcpv4FOIntUpdateReqsSent_Object=MibScalar
cDhcpv4FOIntUpdateReqsSent=_CDhcpv4FOIntUpdateReqsSent_Object((1,3,6,1,4,1,9,10,122,1,5,15),_CDhcpv4FOIntUpdateReqsSent_Type())
cDhcpv4FOIntUpdateReqsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateReqsSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateReqsSent.setUnits(_D)
_CDhcpv4FOIntUpdateDoneSent_Type=Unsigned32
_CDhcpv4FOIntUpdateDoneSent_Object=MibScalar
cDhcpv4FOIntUpdateDoneSent=_CDhcpv4FOIntUpdateDoneSent_Object((1,3,6,1,4,1,9,10,122,1,5,16),_CDhcpv4FOIntUpdateDoneSent_Type())
cDhcpv4FOIntUpdateDoneSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateDoneSent.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntUpdateDoneSent.setUnits(_D)
_CDhcpv4FOIntPacketsDropped_Type=Unsigned32
_CDhcpv4FOIntPacketsDropped_Object=MibScalar
cDhcpv4FOIntPacketsDropped=_CDhcpv4FOIntPacketsDropped_Object((1,3,6,1,4,1,9,10,122,1,5,17),_CDhcpv4FOIntPacketsDropped_Type())
cDhcpv4FOIntPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsDropped.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntPacketsDropped.setUnits(_D)
_CDhcpv4FOIntEndTime_Type=TimeStamp
_CDhcpv4FOIntEndTime_Object=MibScalar
cDhcpv4FOIntEndTime=_CDhcpv4FOIntEndTime_Object((1,3,6,1,4,1,9,10,122,1,5,18),_CDhcpv4FOIntEndTime_Type())
cDhcpv4FOIntEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntEndTime.setStatus(_B)
_CDhcpv4FOIntDeltaTime_Type=TimeInterval
_CDhcpv4FOIntDeltaTime_Object=MibScalar
cDhcpv4FOIntDeltaTime=_CDhcpv4FOIntDeltaTime_Object((1,3,6,1,4,1,9,10,122,1,5,19),_CDhcpv4FOIntDeltaTime_Type())
cDhcpv4FOIntDeltaTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4FOIntDeltaTime.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4FOIntDeltaTime.setUnits(_K)
_CDhcpv4CfgObjects_ObjectIdentity=ObjectIdentity
cDhcpv4CfgObjects=_CDhcpv4CfgObjects_ObjectIdentity((1,3,6,1,4,1,9,10,122,1,6))
_CDhcpv4ConfigIntervalSample_Type=TimeInterval
_CDhcpv4ConfigIntervalSample_Object=MibScalar
cDhcpv4ConfigIntervalSample=_CDhcpv4ConfigIntervalSample_Object((1,3,6,1,4,1,9,10,122,1,6,1),_CDhcpv4ConfigIntervalSample_Type())
cDhcpv4ConfigIntervalSample.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ConfigIntervalSample.setStatus(_B)
if mibBuilder.loadTexts:cDhcpv4ConfigIntervalSample.setUnits(_K)
_CDhcpv4SrvExtSubnetTable_Object=MibTable
cDhcpv4SrvExtSubnetTable=_CDhcpv4SrvExtSubnetTable_Object((1,3,6,1,4,1,9,10,122,1,6,2))
if mibBuilder.loadTexts:cDhcpv4SrvExtSubnetTable.setStatus(_B)
_CDhcpv4SrvExtSubnetEntry_Object=MibTableRow
cDhcpv4SrvExtSubnetEntry=_CDhcpv4SrvExtSubnetEntry_Object((1,3,6,1,4,1,9,10,122,1,6,2,1))
if mibBuilder.loadTexts:cDhcpv4SrvExtSubnetEntry.setStatus(_B)
_CDhcpv4ServerDefaultRouterAddress_Type=InetAddressIPv4
_CDhcpv4ServerDefaultRouterAddress_Object=MibTableColumn
cDhcpv4ServerDefaultRouterAddress=_CDhcpv4ServerDefaultRouterAddress_Object((1,3,6,1,4,1,9,10,122,1,6,2,1,1),_CDhcpv4ServerDefaultRouterAddress_Type())
cDhcpv4ServerDefaultRouterAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerDefaultRouterAddress.setStatus(_B)
_CDhcpv4ServerSubnetStartAddress_Type=InetAddressIPv4
_CDhcpv4ServerSubnetStartAddress_Object=MibTableColumn
cDhcpv4ServerSubnetStartAddress=_CDhcpv4ServerSubnetStartAddress_Object((1,3,6,1,4,1,9,10,122,1,6,2,1,2),_CDhcpv4ServerSubnetStartAddress_Type())
cDhcpv4ServerSubnetStartAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetStartAddress.setStatus(_B)
_CDhcpv4ServerSubnetEndAddress_Type=InetAddressIPv4
_CDhcpv4ServerSubnetEndAddress_Object=MibTableColumn
cDhcpv4ServerSubnetEndAddress=_CDhcpv4ServerSubnetEndAddress_Object((1,3,6,1,4,1,9,10,122,1,6,2,1,3),_CDhcpv4ServerSubnetEndAddress_Type())
cDhcpv4ServerSubnetEndAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetEndAddress.setStatus(_B)
class _CDhcpv4ServerIfLeaseLimitEnable_Type(TruthValue):defaultValue=2
_CDhcpv4ServerIfLeaseLimitEnable_Type.__name__=_G
_CDhcpv4ServerIfLeaseLimitEnable_Object=MibScalar
cDhcpv4ServerIfLeaseLimitEnable=_CDhcpv4ServerIfLeaseLimitEnable_Object((1,3,6,1,4,1,9,10,122,1,6,3),_CDhcpv4ServerIfLeaseLimitEnable_Type())
cDhcpv4ServerIfLeaseLimitEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerIfLeaseLimitEnable.setStatus(_B)
class _CDhcpv4ServerSubnetFreeAddressLowEnable_Type(TruthValue):defaultValue=2
_CDhcpv4ServerSubnetFreeAddressLowEnable_Type.__name__=_G
_CDhcpv4ServerSubnetFreeAddressLowEnable_Object=MibScalar
cDhcpv4ServerSubnetFreeAddressLowEnable=_CDhcpv4ServerSubnetFreeAddressLowEnable_Object((1,3,6,1,4,1,9,10,122,1,6,4),_CDhcpv4ServerSubnetFreeAddressLowEnable_Type())
cDhcpv4ServerSubnetFreeAddressLowEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddressLowEnable.setStatus(_B)
class _CDhcpv4ServerSubnetFreeAddressHighEnable_Type(TruthValue):defaultValue=2
_CDhcpv4ServerSubnetFreeAddressHighEnable_Type.__name__=_G
_CDhcpv4ServerSubnetFreeAddressHighEnable_Object=MibScalar
cDhcpv4ServerSubnetFreeAddressHighEnable=_CDhcpv4ServerSubnetFreeAddressHighEnable_Object((1,3,6,1,4,1,9,10,122,1,6,5),_CDhcpv4ServerSubnetFreeAddressHighEnable_Type())
cDhcpv4ServerSubnetFreeAddressHighEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddressHighEnable.setStatus(_B)
class _CDhcpv4ServerIfLeaseLimitDefault_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CDhcpv4ServerIfLeaseLimitDefault_Type.__name__=_J
_CDhcpv4ServerIfLeaseLimitDefault_Object=MibScalar
cDhcpv4ServerIfLeaseLimitDefault=_CDhcpv4ServerIfLeaseLimitDefault_Object((1,3,6,1,4,1,9,10,122,1,6,6),_CDhcpv4ServerIfLeaseLimitDefault_Type())
cDhcpv4ServerIfLeaseLimitDefault.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerIfLeaseLimitDefault.setStatus(_B)
_CDhcpv4SrvIfCfgTable_Object=MibTable
cDhcpv4SrvIfCfgTable=_CDhcpv4SrvIfCfgTable_Object((1,3,6,1,4,1,9,10,122,1,6,7))
if mibBuilder.loadTexts:cDhcpv4SrvIfCfgTable.setStatus(_B)
_CDhcpv4SrvIfCfgEntry_Object=MibTableRow
cDhcpv4SrvIfCfgEntry=_CDhcpv4SrvIfCfgEntry_Object((1,3,6,1,4,1,9,10,122,1,6,7,1))
cDhcpv4SrvIfCfgEntry.setIndexNames((0,_I,_V))
if mibBuilder.loadTexts:cDhcpv4SrvIfCfgEntry.setStatus(_B)
class _CDhcpv4ServerIfLeaseLimit_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CDhcpv4ServerIfLeaseLimit_Type.__name__=_J
_CDhcpv4ServerIfLeaseLimit_Object=MibTableColumn
cDhcpv4ServerIfLeaseLimit=_CDhcpv4ServerIfLeaseLimit_Object((1,3,6,1,4,1,9,10,122,1,6,7,1,1),_CDhcpv4ServerIfLeaseLimit_Type())
cDhcpv4ServerIfLeaseLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:cDhcpv4ServerIfLeaseLimit.setStatus(_B)
_CiscoIetfDhcpv4SrvExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBConform=_CiscoIetfDhcpv4SrvExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,10,122,2))
_CDhcpv4SrvExtCompliances_ObjectIdentity=ObjectIdentity
cDhcpv4SrvExtCompliances=_CDhcpv4SrvExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,122,2,1))
_CDhcpv4SrvExtGroups_ObjectIdentity=ObjectIdentity
cDhcpv4SrvExtGroups=_CDhcpv4SrvExtGroups_ObjectIdentity((1,3,6,1,4,1,9,10,122,2,2))
cDhcpv4ServerSubnetEntry.registerAugmentions((_A,_Y))
cDhcpv4SrvExtSubnetEntry.setIndexNames(*cDhcpv4ServerSubnetEntry.getIndexNames())
cDhcpv4SrvExtSystemObjects=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,1))
cDhcpv4SrvExtSystemObjects.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cDhcpv4SrvExtSystemObjects.setStatus(_B)
cDhcpv4ExtCountersGroup=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,2))
cDhcpv4ExtCountersGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:cDhcpv4ExtCountersGroup.setStatus(_B)
cDhcpv4CountersIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,3))
cDhcpv4CountersIntervalGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cDhcpv4CountersIntervalGroup.setStatus(_B)
cDhcpv4FOCountersGroup=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,4))
cDhcpv4FOCountersGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:cDhcpv4FOCountersGroup.setStatus(_B)
cDhcpv4FOCountersIntervalGroup=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,5))
cDhcpv4FOCountersIntervalGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:cDhcpv4FOCountersIntervalGroup.setStatus(_B)
cDhcpv4CfgObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,10,122,2,2,6))
cDhcpv4CfgObjectsGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_L)))
if mibBuilder.loadTexts:cDhcpv4CfgObjectsGroup.setStatus(_B)
cDhcpv4ServerIfLeaseLimitExceeded=NotificationType((1,3,6,1,4,1,9,10,122,0,2,0,1))
cDhcpv4ServerIfLeaseLimitExceeded.setObjects(*((_I,_W),(_F,_S),(_A,_L)))
if mibBuilder.loadTexts:cDhcpv4ServerIfLeaseLimitExceeded.setStatus(_B)
cDhcpv4ServerSubnetFreeAddressLow=NotificationType((1,3,6,1,4,1,9,10,122,0,2,0,2))
cDhcpv4ServerSubnetFreeAddressLow.setObjects(*((_F,_H),(_F,_U)))
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddressLow.setStatus(_B)
cDhcpv4ServerSubnetFreeAddressHigh=NotificationType((1,3,6,1,4,1,9,10,122,0,2,0,3))
cDhcpv4ServerSubnetFreeAddressHigh.setObjects(*((_F,_H),(_F,_T)))
if mibBuilder.loadTexts:cDhcpv4ServerSubnetFreeAddressHigh.setStatus(_B)
cDhcpv4SrvExtNotifyGroup=NotificationGroup((1,3,6,1,4,1,9,10,122,2,2,7))
cDhcpv4SrvExtNotifyGroup.setObjects(*((_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:cDhcpv4SrvExtNotifyGroup.setStatus(_B)
cDhcpv4SrvExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,122,2,1,1))
cDhcpv4SrvExtCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:cDhcpv4SrvExtCompliance.setStatus('deprecated')
cDhcpv4SrvExtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,122,2,1,2))
cDhcpv4SrvExtComplianceRev1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_Ab)))
if mibBuilder.loadTexts:cDhcpv4SrvExtComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIetfDhcpSrvExtMIB':ciscoIetfDhcpSrvExtMIB,'ciscoIetfDhcpv4SrvExtMIBNotifs':ciscoIetfDhcpv4SrvExtMIBNotifs,'cDhcpv4SrvExtNotifyPrefix':cDhcpv4SrvExtNotifyPrefix,'cDhcpv4SrvExtNotify':cDhcpv4SrvExtNotify,_AY:cDhcpv4ServerIfLeaseLimitExceeded,_AZ:cDhcpv4ServerSubnetFreeAddressLow,_Aa:cDhcpv4ServerSubnetFreeAddressHigh,'ciscoIetfDhcpv4SrvExtMIBObjects':ciscoIetfDhcpv4SrvExtMIBObjects,'cDhcpv4SrvExtSystem':cDhcpv4SrvExtSystem,_Z:cDhcpv4SrvStartTime,_a:cDhcpv4SrvResetTime,'cDhcpv4ExtCounters':cDhcpv4ExtCounters,_b:cDhcpv4LeaseQueries,_c:cDhcpv4StatisticsResetTime,'cDhcpv4IntervalCounters':cDhcpv4IntervalCounters,_d:cDhcpv4IntDiscovers,_e:cDhcpv4IntOffers,_f:cDhcpv4IntRequests,_g:cDhcpv4IntDeclines,_h:cDhcpv4IntAcks,_i:cDhcpv4IntNaks,_l:cDhcpv4IntReleases,_j:cDhcpv4IntInforms,_k:cDhcpv4IntLeaseQueries,_n:cDhcpv4IntReqBuffersInUse,_m:cDhcpv4IntRespBuffersInUse,_o:cDhcpv4IntEndTime,_p:cDhcpv4IntDeltaTime,'cDhcpv4FailoverCounters':cDhcpv4FailoverCounters,_q:cDhcpv4FOPacketsRcvd,_r:cDhcpv4FOBindingUpdsRcvd,_s:cDhcpv4FOBindingAcksRcvd,_t:cDhcpv4FOBindingNaksRcvd,_u:cDhcpv4FOPoolRequestsRcvd,_v:cDhcpv4FOPollsRcvd,_w:cDhcpv4FOUpdateRequestsRcvd,_x:cDhcpv4FOUpdateDoneRcvd,_y:cDhcpv4FOPacketsSent,_z:cDhcpv4FOBindingUpdatesSent,_A0:cDhcpv4FOBindingAcksSent,_A1:cDhcpv4FOBindingNaksSent,_A2:cDhcpv4FOPoolResponsesSent,_A3:cDhcpv4FOPollsSent,_A4:cDhcpv4FOUpdateRequestsSent,_A5:cDhcpv4FOUpdateDoneSent,_A6:cDhcpv4FOPacketsDropped,'cDhcpv4FailoverIntervalCounters':cDhcpv4FailoverIntervalCounters,_A7:cDhcpv4FOIntPacketsRcvd,_A8:cDhcpv4FOIntBindingUpdsRcvd,_A9:cDhcpv4FOIntBindingAcksRcvd,_AA:cDhcpv4FOIntBindingNaksRcvd,_AB:cDhcpv4FOIntPoolRequestsRcvd,_AC:cDhcpv4FOIntPollsRcvd,_AD:cDhcpv4FOIntUpdateReqsRcvd,_AE:cDhcpv4FOIntUpdateDoneRcvd,_AF:cDhcpv4FOIntPacketsSent,_AG:cDhcpv4FOIntBindingUpdsSent,_AH:cDhcpv4FOIntBindingAcksSent,_AI:cDhcpv4FOIntBindingNaksSent,_AJ:cDhcpv4FOIntPoolResponsesSent,_AK:cDhcpv4FOIntPollsSent,_AL:cDhcpv4FOIntUpdateReqsSent,_AM:cDhcpv4FOIntUpdateDoneSent,_AN:cDhcpv4FOIntPacketsDropped,_AO:cDhcpv4FOIntEndTime,_AP:cDhcpv4FOIntDeltaTime,'cDhcpv4CfgObjects':cDhcpv4CfgObjects,_AQ:cDhcpv4ConfigIntervalSample,'cDhcpv4SrvExtSubnetTable':cDhcpv4SrvExtSubnetTable,_Y:cDhcpv4SrvExtSubnetEntry,_AR:cDhcpv4ServerDefaultRouterAddress,_AS:cDhcpv4ServerSubnetStartAddress,_AT:cDhcpv4ServerSubnetEndAddress,_AU:cDhcpv4ServerIfLeaseLimitEnable,_AV:cDhcpv4ServerSubnetFreeAddressLowEnable,_AW:cDhcpv4ServerSubnetFreeAddressHighEnable,_AX:cDhcpv4ServerIfLeaseLimitDefault,'cDhcpv4SrvIfCfgTable':cDhcpv4SrvIfCfgTable,'cDhcpv4SrvIfCfgEntry':cDhcpv4SrvIfCfgEntry,_L:cDhcpv4ServerIfLeaseLimit,'ciscoIetfDhcpv4SrvExtMIBConform':ciscoIetfDhcpv4SrvExtMIBConform,'cDhcpv4SrvExtCompliances':cDhcpv4SrvExtCompliances,'cDhcpv4SrvExtCompliance':cDhcpv4SrvExtCompliance,'cDhcpv4SrvExtComplianceRev1':cDhcpv4SrvExtComplianceRev1,'cDhcpv4SrvExtGroups':cDhcpv4SrvExtGroups,_M:cDhcpv4SrvExtSystemObjects,_N:cDhcpv4ExtCountersGroup,_O:cDhcpv4CountersIntervalGroup,_P:cDhcpv4FOCountersGroup,_Q:cDhcpv4FOCountersIntervalGroup,_R:cDhcpv4CfgObjectsGroup,_Ab:cDhcpv4SrvExtNotifyGroup})