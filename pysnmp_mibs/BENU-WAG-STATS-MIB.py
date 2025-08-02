_p='bWagVrgApiIpAddrUsedLowThreshold'
_o='bWagVrgApiIpAddrUsedHighThreshold'
_n='bWagCgnatPortBlocksUsedLowThreshold'
_m='bWagCgnatPortBlocksUsedHighThreshold'
_l='bWagCgnatAuthIpAddrUsedLowThreshold'
_k='bWagCgnatAuthIpAddrUsedHighThreshold'
_j='bWagDsLiteProfileStatsIndex'
_i='bWagMHNProfileStatsIndex'
_h='bWagDHCPv6StatsInterval'
_g='bWagCgnatPoolGroupIndex'
_f='bWagCgnatPoolGroupType'
_e='bWagCgnatAuthSubscriberMac'
_d='bWagCgnatUnauthPeriodIpIndex'
_c='bWagCgnatUnauthPeriodIpInterval'
_b='bWagCgnatUnauthIPStatsIndex'
_a='bWagCgnatPeriodIpIndex'
_Z='bWagCgnatPeriodIpInterval'
_Y='bWagCgnatIPStatsIndex'
_X='bWagCgnatProfileStatsIndex'
_W='bWagTunnelStatsInterval'
_V='bWagPolicyIndex'
_U='bWagPolicyType'
_T='bWagSubscriberStatsInterval'
_S='bWagDhcpTPSInterval'
_R='bWagDhcpStatsInterval'
_Q='bWagRadiusStatsInterval'
_P='2016-07-05 00:00'
_O='DisplayString'
_N='bWagDhcpTPS'
_M='bWagCgnatTotalPortBlocksPerSubscriber'
_L='bWagCgnatSubscriberMac'
_K='Integer32'
_J='bWagVRGApiIPoolIPAddresses'
_I='bWagrgApiIPPoolGroup'
_H='bWagCgnatTotalPoolIPAddresses'
_G='bWagCgnatProfileIPPoolGroup'
_F='accessible-for-notify'
_E='not-accessible'
_D='BENU-WAG-STATS-MIB'
_C='obsolete'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','TextualConvention')
benuWagStatsMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,3))
if mibBuilder.loadTexts:benuWagStatsMIB.setRevisions(('1970-01-01 00:00','2017-01-31 00:00','2017-01-20 00:00',_P,_P,'2016-05-30 00:00','2016-05-27 00:00','2016-03-03 00:00','2015-10-05 00:00','2015-09-30 00:00','2015-09-29 00:00','2015-09-26 00:00','2015-09-24 00:00','2015-09-24 00:01','2015-09-22 00:01','2015-09-22 00:00','2015-09-21 00:00','2015-09-15 00:00','2015-09-08 00:00','2015-08-06 00:00','2015-07-15 00:00','2015-06-26 00:00','2015-06-24 00:00','2015-06-12 00:00','2015-05-21 00:00','2015-05-20 00:00','2015-05-12 00:00','2015-04-15 00:00','2015-04-13 00:00','2015-04-12 00:00','2015-03-27 00:00','2015-02-27 00:00','2015-02-25 00:00','2015-02-20 00:00','2015-02-18 00:00','2015-02-17 00:00','2015-02-16 00:00','2015-01-28 00:00','2015-01-12 00:00','2015-01-08 00:00','2015-01-05 00:00','2015-01-02 00:00','2014-09-09 00:00','2014-04-28 00:00','2014-03-05 00:00','2014-02-25 00:00','2014-02-19 00:00','2014-02-14 00:00','2014-01-17 00:00','2014-01-16 00:00','2014-01-09 00:00','2013-12-31 00:00','2013-12-23 00:01','2013-12-17 00:01','2013-12-10 00:01','2013-12-10 00:00','2013-11-29 00:00','2013-11-23 00:00','2013-11-21 00:00','2013-11-13 00:00','2013-09-13 00:00','2016-07-08 00:00'))
_BWagStatsNotifications_ObjectIdentity=ObjectIdentity
bWagStatsNotifications=_BWagStatsNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,0))
if mibBuilder.loadTexts:bWagStatsNotifications.setStatus(_A)
_BWagRadiusMIBObjects_ObjectIdentity=ObjectIdentity
bWagRadiusMIBObjects=_BWagRadiusMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,1))
if mibBuilder.loadTexts:bWagRadiusMIBObjects.setStatus(_A)
_BWagRadiusTable_Object=MibTable
bWagRadiusTable=_BWagRadiusTable_Object((1,3,6,1,4,1,39406,2,1,3,1,1))
if mibBuilder.loadTexts:bWagRadiusTable.setStatus(_A)
_BWagRadiusEntry_Object=MibTableRow
bWagRadiusEntry=_BWagRadiusEntry_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1))
bWagRadiusEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:bWagRadiusEntry.setStatus(_A)
_BWagRadiusStatsInterval_Type=Integer32
_BWagRadiusStatsInterval_Object=MibTableColumn
bWagRadiusStatsInterval=_BWagRadiusStatsInterval_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,1),_BWagRadiusStatsInterval_Type())
bWagRadiusStatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagRadiusStatsInterval.setStatus(_A)
_BWagRadiusIntervalDuration_Type=Integer32
_BWagRadiusIntervalDuration_Object=MibTableColumn
bWagRadiusIntervalDuration=_BWagRadiusIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,2),_BWagRadiusIntervalDuration_Type())
bWagRadiusIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusIntervalDuration.setStatus(_A)
_BWagRadiusAuthLatencyMin_Type=Unsigned32
_BWagRadiusAuthLatencyMin_Object=MibTableColumn
bWagRadiusAuthLatencyMin=_BWagRadiusAuthLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,3),_BWagRadiusAuthLatencyMin_Type())
bWagRadiusAuthLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAuthLatencyMin.setStatus(_A)
_BWagRadiusAuthLatencyMax_Type=Unsigned32
_BWagRadiusAuthLatencyMax_Object=MibTableColumn
bWagRadiusAuthLatencyMax=_BWagRadiusAuthLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,4),_BWagRadiusAuthLatencyMax_Type())
bWagRadiusAuthLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAuthLatencyMax.setStatus(_A)
_BWagRadiusAuthLatencyAvg_Type=Unsigned32
_BWagRadiusAuthLatencyAvg_Object=MibTableColumn
bWagRadiusAuthLatencyAvg=_BWagRadiusAuthLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,5),_BWagRadiusAuthLatencyAvg_Type())
bWagRadiusAuthLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAuthLatencyAvg.setStatus(_A)
_BWagRadiusAuthLatencyLast_Type=Unsigned32
_BWagRadiusAuthLatencyLast_Object=MibTableColumn
bWagRadiusAuthLatencyLast=_BWagRadiusAuthLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,6),_BWagRadiusAuthLatencyLast_Type())
bWagRadiusAuthLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAuthLatencyLast.setStatus(_A)
_BWagRadiusAcctLatencyMin_Type=Unsigned32
_BWagRadiusAcctLatencyMin_Object=MibTableColumn
bWagRadiusAcctLatencyMin=_BWagRadiusAcctLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,7),_BWagRadiusAcctLatencyMin_Type())
bWagRadiusAcctLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctLatencyMin.setStatus(_A)
_BWagRadiusAcctLatencyMax_Type=Unsigned32
_BWagRadiusAcctLatencyMax_Object=MibTableColumn
bWagRadiusAcctLatencyMax=_BWagRadiusAcctLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,8),_BWagRadiusAcctLatencyMax_Type())
bWagRadiusAcctLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctLatencyMax.setStatus(_A)
_BWagRadiusAcctLatencyAvg_Type=Unsigned32
_BWagRadiusAcctLatencyAvg_Object=MibTableColumn
bWagRadiusAcctLatencyAvg=_BWagRadiusAcctLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,9),_BWagRadiusAcctLatencyAvg_Type())
bWagRadiusAcctLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctLatencyAvg.setStatus(_A)
_BWagRadiusAcctLatencyLast_Type=Unsigned32
_BWagRadiusAcctLatencyLast_Object=MibTableColumn
bWagRadiusAcctLatencyLast=_BWagRadiusAcctLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,10),_BWagRadiusAcctLatencyLast_Type())
bWagRadiusAcctLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctLatencyLast.setStatus(_A)
_BWagRadiusAccessRequestSent_Type=Unsigned32
_BWagRadiusAccessRequestSent_Object=MibTableColumn
bWagRadiusAccessRequestSent=_BWagRadiusAccessRequestSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,11),_BWagRadiusAccessRequestSent_Type())
bWagRadiusAccessRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAccessRequestSent.setStatus(_A)
_BWagRadiusAccessAcceptReceived_Type=Unsigned32
_BWagRadiusAccessAcceptReceived_Object=MibTableColumn
bWagRadiusAccessAcceptReceived=_BWagRadiusAccessAcceptReceived_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,12),_BWagRadiusAccessAcceptReceived_Type())
bWagRadiusAccessAcceptReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAccessAcceptReceived.setStatus(_A)
_BWagRadiusAccessRejectReceived_Type=Unsigned32
_BWagRadiusAccessRejectReceived_Object=MibTableColumn
bWagRadiusAccessRejectReceived=_BWagRadiusAccessRejectReceived_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,13),_BWagRadiusAccessRejectReceived_Type())
bWagRadiusAccessRejectReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAccessRejectReceived.setStatus(_A)
_BWagRadiusAcctRequestSent_Type=Unsigned32
_BWagRadiusAcctRequestSent_Object=MibTableColumn
bWagRadiusAcctRequestSent=_BWagRadiusAcctRequestSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,14),_BWagRadiusAcctRequestSent_Type())
bWagRadiusAcctRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctRequestSent.setStatus(_A)
_BWagRadiusAcctResponseReceived_Type=Unsigned32
_BWagRadiusAcctResponseReceived_Object=MibTableColumn
bWagRadiusAcctResponseReceived=_BWagRadiusAcctResponseReceived_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,15),_BWagRadiusAcctResponseReceived_Type())
bWagRadiusAcctResponseReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusAcctResponseReceived.setStatus(_A)
_BWagRadiusCoAAckSent_Type=Unsigned32
_BWagRadiusCoAAckSent_Object=MibTableColumn
bWagRadiusCoAAckSent=_BWagRadiusCoAAckSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,16),_BWagRadiusCoAAckSent_Type())
bWagRadiusCoAAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoAAckSent.setStatus(_A)
_BWagRadiusCoANackSent_Type=Unsigned32
_BWagRadiusCoANackSent_Object=MibTableColumn
bWagRadiusCoANackSent=_BWagRadiusCoANackSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,17),_BWagRadiusCoANackSent_Type())
bWagRadiusCoANackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoANackSent.setStatus(_A)
_BWagRadiusCoARequestReceived_Type=Unsigned32
_BWagRadiusCoARequestReceived_Object=MibTableColumn
bWagRadiusCoARequestReceived=_BWagRadiusCoARequestReceived_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,18),_BWagRadiusCoARequestReceived_Type())
bWagRadiusCoARequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoARequestReceived.setStatus(_A)
_BWagRadiusCoALatencyMin_Type=Unsigned32
_BWagRadiusCoALatencyMin_Object=MibTableColumn
bWagRadiusCoALatencyMin=_BWagRadiusCoALatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,19),_BWagRadiusCoALatencyMin_Type())
bWagRadiusCoALatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoALatencyMin.setStatus(_A)
_BWagRadiusCoALatencyMax_Type=Unsigned32
_BWagRadiusCoALatencyMax_Object=MibTableColumn
bWagRadiusCoALatencyMax=_BWagRadiusCoALatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,20),_BWagRadiusCoALatencyMax_Type())
bWagRadiusCoALatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoALatencyMax.setStatus(_A)
_BWagRadiusCoALatencyAvg_Type=Unsigned32
_BWagRadiusCoALatencyAvg_Object=MibTableColumn
bWagRadiusCoALatencyAvg=_BWagRadiusCoALatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,21),_BWagRadiusCoALatencyAvg_Type())
bWagRadiusCoALatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoALatencyAvg.setStatus(_A)
_BWagRadiusCoALatencyLast_Type=Unsigned32
_BWagRadiusCoALatencyLast_Object=MibTableColumn
bWagRadiusCoALatencyLast=_BWagRadiusCoALatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,22),_BWagRadiusCoALatencyLast_Type())
bWagRadiusCoALatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusCoALatencyLast.setStatus(_A)
_BWagRadiusDMLatencyMin_Type=Unsigned32
_BWagRadiusDMLatencyMin_Object=MibTableColumn
bWagRadiusDMLatencyMin=_BWagRadiusDMLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,23),_BWagRadiusDMLatencyMin_Type())
bWagRadiusDMLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMLatencyMin.setStatus(_A)
_BWagRadiusDMLatencyMax_Type=Unsigned32
_BWagRadiusDMLatencyMax_Object=MibTableColumn
bWagRadiusDMLatencyMax=_BWagRadiusDMLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,24),_BWagRadiusDMLatencyMax_Type())
bWagRadiusDMLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMLatencyMax.setStatus(_A)
_BWagRadiusDMLatencyAvg_Type=Unsigned32
_BWagRadiusDMLatencyAvg_Object=MibTableColumn
bWagRadiusDMLatencyAvg=_BWagRadiusDMLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,25),_BWagRadiusDMLatencyAvg_Type())
bWagRadiusDMLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMLatencyAvg.setStatus(_A)
_BWagRadiusDMLatencyLast_Type=Unsigned32
_BWagRadiusDMLatencyLast_Object=MibTableColumn
bWagRadiusDMLatencyLast=_BWagRadiusDMLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,26),_BWagRadiusDMLatencyLast_Type())
bWagRadiusDMLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMLatencyLast.setStatus(_A)
_BWagRadiusDMAckSent_Type=Unsigned32
_BWagRadiusDMAckSent_Object=MibTableColumn
bWagRadiusDMAckSent=_BWagRadiusDMAckSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,27),_BWagRadiusDMAckSent_Type())
bWagRadiusDMAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMAckSent.setStatus(_A)
_BWagRadiusDMNackSent_Type=Unsigned32
_BWagRadiusDMNackSent_Object=MibTableColumn
bWagRadiusDMNackSent=_BWagRadiusDMNackSent_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,28),_BWagRadiusDMNackSent_Type())
bWagRadiusDMNackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMNackSent.setStatus(_A)
_BWagRadiusDMRequestReceived_Type=Unsigned32
_BWagRadiusDMRequestReceived_Object=MibTableColumn
bWagRadiusDMRequestReceived=_BWagRadiusDMRequestReceived_Object((1,3,6,1,4,1,39406,2,1,3,1,1,1,29),_BWagRadiusDMRequestReceived_Type())
bWagRadiusDMRequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagRadiusDMRequestReceived.setStatus(_A)
_BWagRadiusNotifObjects_ObjectIdentity=ObjectIdentity
bWagRadiusNotifObjects=_BWagRadiusNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,2))
if mibBuilder.loadTexts:bWagRadiusNotifObjects.setStatus(_A)
_BWagDhcpMIBObjects_ObjectIdentity=ObjectIdentity
bWagDhcpMIBObjects=_BWagDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,3))
if mibBuilder.loadTexts:bWagDhcpMIBObjects.setStatus(_A)
_BWagDhcpTable_Object=MibTable
bWagDhcpTable=_BWagDhcpTable_Object((1,3,6,1,4,1,39406,2,1,3,3,1))
if mibBuilder.loadTexts:bWagDhcpTable.setStatus(_A)
_BWagDhcpEntry_Object=MibTableRow
bWagDhcpEntry=_BWagDhcpEntry_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1))
bWagDhcpEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:bWagDhcpEntry.setStatus(_A)
_BWagDhcpStatsInterval_Type=Integer32
_BWagDhcpStatsInterval_Object=MibTableColumn
bWagDhcpStatsInterval=_BWagDhcpStatsInterval_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,1),_BWagDhcpStatsInterval_Type())
bWagDhcpStatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagDhcpStatsInterval.setStatus(_A)
_BWagDhcpIntervalDuration_Type=Integer32
_BWagDhcpIntervalDuration_Object=MibTableColumn
bWagDhcpIntervalDuration=_BWagDhcpIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,2),_BWagDhcpIntervalDuration_Type())
bWagDhcpIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpIntervalDuration.setStatus(_A)
_BWagDhcpDiscoverAckIntervalMin_Type=Unsigned32
_BWagDhcpDiscoverAckIntervalMin_Object=MibTableColumn
bWagDhcpDiscoverAckIntervalMin=_BWagDhcpDiscoverAckIntervalMin_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,3),_BWagDhcpDiscoverAckIntervalMin_Type())
bWagDhcpDiscoverAckIntervalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverAckIntervalMin.setStatus(_A)
_BWagDhcpDiscoverAckIntervalMax_Type=Unsigned32
_BWagDhcpDiscoverAckIntervalMax_Object=MibTableColumn
bWagDhcpDiscoverAckIntervalMax=_BWagDhcpDiscoverAckIntervalMax_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,4),_BWagDhcpDiscoverAckIntervalMax_Type())
bWagDhcpDiscoverAckIntervalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverAckIntervalMax.setStatus(_A)
_BWagDhcpDiscoverAckIntervalAvg_Type=Unsigned32
_BWagDhcpDiscoverAckIntervalAvg_Object=MibTableColumn
bWagDhcpDiscoverAckIntervalAvg=_BWagDhcpDiscoverAckIntervalAvg_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,5),_BWagDhcpDiscoverAckIntervalAvg_Type())
bWagDhcpDiscoverAckIntervalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverAckIntervalAvg.setStatus(_A)
_BWagDhcpDiscoverAckIntervalLast_Type=Unsigned32
_BWagDhcpDiscoverAckIntervalLast_Object=MibTableColumn
bWagDhcpDiscoverAckIntervalLast=_BWagDhcpDiscoverAckIntervalLast_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,6),_BWagDhcpDiscoverAckIntervalLast_Type())
bWagDhcpDiscoverAckIntervalLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverAckIntervalLast.setStatus(_A)
_BWagDhcpRequestAckLatencyMin_Type=Unsigned32
_BWagDhcpRequestAckLatencyMin_Object=MibTableColumn
bWagDhcpRequestAckLatencyMin=_BWagDhcpRequestAckLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,7),_BWagDhcpRequestAckLatencyMin_Type())
bWagDhcpRequestAckLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpRequestAckLatencyMin.setStatus(_A)
_BWagDhcpRequestAckLatencyMax_Type=Unsigned32
_BWagDhcpRequestAckLatencyMax_Object=MibTableColumn
bWagDhcpRequestAckLatencyMax=_BWagDhcpRequestAckLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,8),_BWagDhcpRequestAckLatencyMax_Type())
bWagDhcpRequestAckLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpRequestAckLatencyMax.setStatus(_A)
_BWagDhcpRequestAckLatencyAvg_Type=Unsigned32
_BWagDhcpRequestAckLatencyAvg_Object=MibTableColumn
bWagDhcpRequestAckLatencyAvg=_BWagDhcpRequestAckLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,9),_BWagDhcpRequestAckLatencyAvg_Type())
bWagDhcpRequestAckLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpRequestAckLatencyAvg.setStatus(_A)
_BWagDhcpRequestAckLatencyLast_Type=Unsigned32
_BWagDhcpRequestAckLatencyLast_Object=MibTableColumn
bWagDhcpRequestAckLatencyLast=_BWagDhcpRequestAckLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,10),_BWagDhcpRequestAckLatencyLast_Type())
bWagDhcpRequestAckLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpRequestAckLatencyLast.setStatus(_A)
_BWagDhcpDiscoverOfferLatencyMin_Type=Unsigned32
_BWagDhcpDiscoverOfferLatencyMin_Object=MibTableColumn
bWagDhcpDiscoverOfferLatencyMin=_BWagDhcpDiscoverOfferLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,11),_BWagDhcpDiscoverOfferLatencyMin_Type())
bWagDhcpDiscoverOfferLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverOfferLatencyMin.setStatus(_A)
_BWagDhcpDiscoverOfferLatencyMax_Type=Unsigned32
_BWagDhcpDiscoverOfferLatencyMax_Object=MibTableColumn
bWagDhcpDiscoverOfferLatencyMax=_BWagDhcpDiscoverOfferLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,12),_BWagDhcpDiscoverOfferLatencyMax_Type())
bWagDhcpDiscoverOfferLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverOfferLatencyMax.setStatus(_A)
_BWagDhcpDiscoverOfferLatencyAvg_Type=Unsigned32
_BWagDhcpDiscoverOfferLatencyAvg_Object=MibTableColumn
bWagDhcpDiscoverOfferLatencyAvg=_BWagDhcpDiscoverOfferLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,13),_BWagDhcpDiscoverOfferLatencyAvg_Type())
bWagDhcpDiscoverOfferLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverOfferLatencyAvg.setStatus(_A)
_BWagDhcpDiscoverOfferLatencyLast_Type=Unsigned32
_BWagDhcpDiscoverOfferLatencyLast_Object=MibTableColumn
bWagDhcpDiscoverOfferLatencyLast=_BWagDhcpDiscoverOfferLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,14),_BWagDhcpDiscoverOfferLatencyLast_Type())
bWagDhcpDiscoverOfferLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverOfferLatencyLast.setStatus(_A)
_BWagDhcpDiscoverReceived_Type=Unsigned32
_BWagDhcpDiscoverReceived_Object=MibTableColumn
bWagDhcpDiscoverReceived=_BWagDhcpDiscoverReceived_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,15),_BWagDhcpDiscoverReceived_Type())
bWagDhcpDiscoverReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpDiscoverReceived.setStatus(_A)
_BWagDhcpOfferSent_Type=Unsigned32
_BWagDhcpOfferSent_Object=MibTableColumn
bWagDhcpOfferSent=_BWagDhcpOfferSent_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,16),_BWagDhcpOfferSent_Type())
bWagDhcpOfferSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpOfferSent.setStatus(_A)
_BWagDhcpRequestReceived_Type=Unsigned32
_BWagDhcpRequestReceived_Object=MibTableColumn
bWagDhcpRequestReceived=_BWagDhcpRequestReceived_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,17),_BWagDhcpRequestReceived_Type())
bWagDhcpRequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpRequestReceived.setStatus(_A)
_BWagDhcpAckSent_Type=Unsigned32
_BWagDhcpAckSent_Object=MibTableColumn
bWagDhcpAckSent=_BWagDhcpAckSent_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,18),_BWagDhcpAckSent_Type())
bWagDhcpAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpAckSent.setStatus(_A)
_BWagDhcpNackSent_Type=Unsigned32
_BWagDhcpNackSent_Object=MibTableColumn
bWagDhcpNackSent=_BWagDhcpNackSent_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,19),_BWagDhcpNackSent_Type())
bWagDhcpNackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpNackSent.setStatus(_A)
_BWagDhcpOfferRequestIntervalMin_Type=Unsigned32
_BWagDhcpOfferRequestIntervalMin_Object=MibTableColumn
bWagDhcpOfferRequestIntervalMin=_BWagDhcpOfferRequestIntervalMin_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,20),_BWagDhcpOfferRequestIntervalMin_Type())
bWagDhcpOfferRequestIntervalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpOfferRequestIntervalMin.setStatus(_A)
_BWagDhcpOfferRequestIntervalMax_Type=Unsigned32
_BWagDhcpOfferRequestIntervalMax_Object=MibTableColumn
bWagDhcpOfferRequestIntervalMax=_BWagDhcpOfferRequestIntervalMax_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,21),_BWagDhcpOfferRequestIntervalMax_Type())
bWagDhcpOfferRequestIntervalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpOfferRequestIntervalMax.setStatus(_A)
_BWagDhcpOfferRequestIntervalAvg_Type=Unsigned32
_BWagDhcpOfferRequestIntervalAvg_Object=MibTableColumn
bWagDhcpOfferRequestIntervalAvg=_BWagDhcpOfferRequestIntervalAvg_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,22),_BWagDhcpOfferRequestIntervalAvg_Type())
bWagDhcpOfferRequestIntervalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpOfferRequestIntervalAvg.setStatus(_A)
_BWagDhcpOfferRequestIntervalLast_Type=Unsigned32
_BWagDhcpOfferRequestIntervalLast_Object=MibTableColumn
bWagDhcpOfferRequestIntervalLast=_BWagDhcpOfferRequestIntervalLast_Object((1,3,6,1,4,1,39406,2,1,3,3,1,1,23),_BWagDhcpOfferRequestIntervalLast_Type())
bWagDhcpOfferRequestIntervalLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpOfferRequestIntervalLast.setStatus(_A)
_BWagDhcpTPSTable_Object=MibTable
bWagDhcpTPSTable=_BWagDhcpTPSTable_Object((1,3,6,1,4,1,39406,2,1,3,3,2))
if mibBuilder.loadTexts:bWagDhcpTPSTable.setStatus(_A)
_BWagDhcpTPSEntry_Object=MibTableRow
bWagDhcpTPSEntry=_BWagDhcpTPSEntry_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1))
bWagDhcpTPSEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:bWagDhcpTPSEntry.setStatus(_A)
_BWagDhcpTPSInterval_Type=Integer32
_BWagDhcpTPSInterval_Object=MibTableColumn
bWagDhcpTPSInterval=_BWagDhcpTPSInterval_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1,1),_BWagDhcpTPSInterval_Type())
bWagDhcpTPSInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagDhcpTPSInterval.setStatus(_A)
_BWagDhcpTPSIntervalDuration_Type=Unsigned32
_BWagDhcpTPSIntervalDuration_Object=MibTableColumn
bWagDhcpTPSIntervalDuration=_BWagDhcpTPSIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1,2),_BWagDhcpTPSIntervalDuration_Type())
bWagDhcpTPSIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpTPSIntervalDuration.setStatus(_A)
_BWagDhcpTPSLow_Type=Unsigned32
_BWagDhcpTPSLow_Object=MibTableColumn
bWagDhcpTPSLow=_BWagDhcpTPSLow_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1,3),_BWagDhcpTPSLow_Type())
bWagDhcpTPSLow.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpTPSLow.setStatus(_A)
_BWagDhcpTPSHigh_Type=Unsigned32
_BWagDhcpTPSHigh_Object=MibTableColumn
bWagDhcpTPSHigh=_BWagDhcpTPSHigh_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1,4),_BWagDhcpTPSHigh_Type())
bWagDhcpTPSHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpTPSHigh.setStatus(_A)
_BWagDhcpTPS_Type=Unsigned32
_BWagDhcpTPS_Object=MibTableColumn
bWagDhcpTPS=_BWagDhcpTPS_Object((1,3,6,1,4,1,39406,2,1,3,3,2,1,5),_BWagDhcpTPS_Type())
bWagDhcpTPS.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDhcpTPS.setStatus(_A)
_BWagDhcpNotifObjects_ObjectIdentity=ObjectIdentity
bWagDhcpNotifObjects=_BWagDhcpNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,4))
if mibBuilder.loadTexts:bWagDhcpNotifObjects.setStatus(_A)
_BWagSubscriberMIBObjects_ObjectIdentity=ObjectIdentity
bWagSubscriberMIBObjects=_BWagSubscriberMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,5))
if mibBuilder.loadTexts:bWagSubscriberMIBObjects.setStatus(_A)
_BWagSubscriberTable_Object=MibTable
bWagSubscriberTable=_BWagSubscriberTable_Object((1,3,6,1,4,1,39406,2,1,3,5,1))
if mibBuilder.loadTexts:bWagSubscriberTable.setStatus(_A)
_BWagSubscriberEntry_Object=MibTableRow
bWagSubscriberEntry=_BWagSubscriberEntry_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1))
bWagSubscriberEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:bWagSubscriberEntry.setStatus(_A)
_BWagSubscriberStatsInterval_Type=Integer32
_BWagSubscriberStatsInterval_Object=MibTableColumn
bWagSubscriberStatsInterval=_BWagSubscriberStatsInterval_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,1),_BWagSubscriberStatsInterval_Type())
bWagSubscriberStatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagSubscriberStatsInterval.setStatus(_A)
_BWagSubscriberIntervalDuration_Type=Integer32
_BWagSubscriberIntervalDuration_Object=MibTableColumn
bWagSubscriberIntervalDuration=_BWagSubscriberIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,2),_BWagSubscriberIntervalDuration_Type())
bWagSubscriberIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberIntervalDuration.setStatus(_A)
_BWagSubscriberActivationsCount_Type=Unsigned32
_BWagSubscriberActivationsCount_Object=MibTableColumn
bWagSubscriberActivationsCount=_BWagSubscriberActivationsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,3),_BWagSubscriberActivationsCount_Type())
bWagSubscriberActivationsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberActivationsCount.setStatus(_A)
_BWagSubscriberDeletionsCount_Type=Unsigned32
_BWagSubscriberDeletionsCount_Object=MibTableColumn
bWagSubscriberDeletionsCount=_BWagSubscriberDeletionsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,4),_BWagSubscriberDeletionsCount_Type())
bWagSubscriberDeletionsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberDeletionsCount.setStatus(_A)
_BWagSubscriberAuthenticationsCount_Type=Unsigned32
_BWagSubscriberAuthenticationsCount_Object=MibTableColumn
bWagSubscriberAuthenticationsCount=_BWagSubscriberAuthenticationsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,5),_BWagSubscriberAuthenticationsCount_Type())
bWagSubscriberAuthenticationsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAuthenticationsCount.setStatus(_A)
_BWagSubscriberRedirectionsCount_Type=Unsigned32
_BWagSubscriberRedirectionsCount_Object=MibTableColumn
bWagSubscriberRedirectionsCount=_BWagSubscriberRedirectionsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,6),_BWagSubscriberRedirectionsCount_Type())
bWagSubscriberRedirectionsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberRedirectionsCount.setStatus(_A)
_BWagSubscriberRedirectionsByAcl_Type=Unsigned32
_BWagSubscriberRedirectionsByAcl_Object=MibTableColumn
bWagSubscriberRedirectionsByAcl=_BWagSubscriberRedirectionsByAcl_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,7),_BWagSubscriberRedirectionsByAcl_Type())
bWagSubscriberRedirectionsByAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberRedirectionsByAcl.setStatus(_C)
_BWagSubscriberAPMobilityOccurencesCount_Type=Unsigned32
_BWagSubscriberAPMobilityOccurencesCount_Object=MibTableColumn
bWagSubscriberAPMobilityOccurencesCount=_BWagSubscriberAPMobilityOccurencesCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,8),_BWagSubscriberAPMobilityOccurencesCount_Type())
bWagSubscriberAPMobilityOccurencesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAPMobilityOccurencesCount.setStatus(_A)
_BWagSubscriberDeletionsByDMCount_Type=Unsigned32
_BWagSubscriberDeletionsByDMCount_Object=MibTableColumn
bWagSubscriberDeletionsByDMCount=_BWagSubscriberDeletionsByDMCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,9),_BWagSubscriberDeletionsByDMCount_Type())
bWagSubscriberDeletionsByDMCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberDeletionsByDMCount.setStatus(_A)
_BWagSubscriberIdleTimeoutCount_Type=Unsigned32
_BWagSubscriberIdleTimeoutCount_Object=MibTableColumn
bWagSubscriberIdleTimeoutCount=_BWagSubscriberIdleTimeoutCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,10),_BWagSubscriberIdleTimeoutCount_Type())
bWagSubscriberIdleTimeoutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberIdleTimeoutCount.setStatus(_A)
_BWagSubscriberSessionTimeoutPreauthCount_Type=Unsigned32
_BWagSubscriberSessionTimeoutPreauthCount_Object=MibTableColumn
bWagSubscriberSessionTimeoutPreauthCount=_BWagSubscriberSessionTimeoutPreauthCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,11),_BWagSubscriberSessionTimeoutPreauthCount_Type())
bWagSubscriberSessionTimeoutPreauthCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberSessionTimeoutPreauthCount.setStatus(_A)
_BWagSubscriberSessionTimeoutAuthviaportalCount_Type=Unsigned32
_BWagSubscriberSessionTimeoutAuthviaportalCount_Object=MibTableColumn
bWagSubscriberSessionTimeoutAuthviaportalCount=_BWagSubscriberSessionTimeoutAuthviaportalCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,12),_BWagSubscriberSessionTimeoutAuthviaportalCount_Type())
bWagSubscriberSessionTimeoutAuthviaportalCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberSessionTimeoutAuthviaportalCount.setStatus(_A)
_BWagSubscriberDroppedByLicenseManagerCount_Type=Unsigned32
_BWagSubscriberDroppedByLicenseManagerCount_Object=MibTableColumn
bWagSubscriberDroppedByLicenseManagerCount=_BWagSubscriberDroppedByLicenseManagerCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,13),_BWagSubscriberDroppedByLicenseManagerCount_Type())
bWagSubscriberDroppedByLicenseManagerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberDroppedByLicenseManagerCount.setStatus(_A)
_BWagSubscriberThrottlingOccurrencesCount_Type=Unsigned32
_BWagSubscriberThrottlingOccurrencesCount_Object=MibTableColumn
bWagSubscriberThrottlingOccurrencesCount=_BWagSubscriberThrottlingOccurrencesCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,14),_BWagSubscriberThrottlingOccurrencesCount_Type())
bWagSubscriberThrottlingOccurrencesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberThrottlingOccurrencesCount.setStatus(_C)
_BWagSubscriberThrottledCount_Type=Unsigned32
_BWagSubscriberThrottledCount_Object=MibTableColumn
bWagSubscriberThrottledCount=_BWagSubscriberThrottledCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,15),_BWagSubscriberThrottledCount_Type())
bWagSubscriberThrottledCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberThrottledCount.setStatus(_C)
_BWagSubscriberAbsoluteTimeoutCount_Type=Unsigned32
_BWagSubscriberAbsoluteTimeoutCount_Object=MibTableColumn
bWagSubscriberAbsoluteTimeoutCount=_BWagSubscriberAbsoluteTimeoutCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,16),_BWagSubscriberAbsoluteTimeoutCount_Type())
bWagSubscriberAbsoluteTimeoutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAbsoluteTimeoutCount.setStatus(_A)
_BWagSubscriberAuthsViaPortalCount_Type=Unsigned32
_BWagSubscriberAuthsViaPortalCount_Object=MibTableColumn
bWagSubscriberAuthsViaPortalCount=_BWagSubscriberAuthsViaPortalCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,17),_BWagSubscriberAuthsViaPortalCount_Type())
bWagSubscriberAuthsViaPortalCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAuthsViaPortalCount.setStatus(_A)
_BWagSubscriberAuthenticationsCountVia8021x_Type=Unsigned32
_BWagSubscriberAuthenticationsCountVia8021x_Object=MibTableColumn
bWagSubscriberAuthenticationsCountVia8021x=_BWagSubscriberAuthenticationsCountVia8021x_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,18),_BWagSubscriberAuthenticationsCountVia8021x_Type())
bWagSubscriberAuthenticationsCountVia8021x.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAuthenticationsCountVia8021x.setStatus(_A)
_BWagSubscriberAuthenticationsCountViaSingleStatic_Type=Unsigned32
_BWagSubscriberAuthenticationsCountViaSingleStatic_Object=MibTableColumn
bWagSubscriberAuthenticationsCountViaSingleStatic=_BWagSubscriberAuthenticationsCountViaSingleStatic_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,19),_BWagSubscriberAuthenticationsCountViaSingleStatic_Type())
bWagSubscriberAuthenticationsCountViaSingleStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAuthenticationsCountViaSingleStatic.setStatus(_A)
_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Type=Unsigned32
_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Object=MibTableColumn
bWagSubscriberAuthenticationsCountViaRoutedSubnet=_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,20),_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Type())
bWagSubscriberAuthenticationsCountViaRoutedSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberAuthenticationsCountViaRoutedSubnet.setStatus(_A)
_BWagSubscriberSessionTimeoutAuthVia8021x_Type=Unsigned32
_BWagSubscriberSessionTimeoutAuthVia8021x_Object=MibTableColumn
bWagSubscriberSessionTimeoutAuthVia8021x=_BWagSubscriberSessionTimeoutAuthVia8021x_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,21),_BWagSubscriberSessionTimeoutAuthVia8021x_Type())
bWagSubscriberSessionTimeoutAuthVia8021x.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberSessionTimeoutAuthVia8021x.setStatus(_A)
_BWagSubscriberHomeTotalSubsDeleted_Type=Unsigned32
_BWagSubscriberHomeTotalSubsDeleted_Object=MibTableColumn
bWagSubscriberHomeTotalSubsDeleted=_BWagSubscriberHomeTotalSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,22),_BWagSubscriberHomeTotalSubsDeleted_Type())
bWagSubscriberHomeTotalSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeTotalSubsDeleted.setStatus(_A)
_BWagSubscriberHomeTransientSubsDeleted_Type=Unsigned32
_BWagSubscriberHomeTransientSubsDeleted_Object=MibTableColumn
bWagSubscriberHomeTransientSubsDeleted=_BWagSubscriberHomeTransientSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,23),_BWagSubscriberHomeTransientSubsDeleted_Type())
bWagSubscriberHomeTransientSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeTransientSubsDeleted.setStatus(_A)
_BWagSubscriberHomeUserStaticSubsDeleted_Type=Unsigned32
_BWagSubscriberHomeUserStaticSubsDeleted_Object=MibTableColumn
bWagSubscriberHomeUserStaticSubsDeleted=_BWagSubscriberHomeUserStaticSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,24),_BWagSubscriberHomeUserStaticSubsDeleted_Type())
bWagSubscriberHomeUserStaticSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeUserStaticSubsDeleted.setStatus(_A)
_BWagSubscriberHomeDhcpStaticSubsDeleted_Type=Unsigned32
_BWagSubscriberHomeDhcpStaticSubsDeleted_Object=MibTableColumn
bWagSubscriberHomeDhcpStaticSubsDeleted=_BWagSubscriberHomeDhcpStaticSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,25),_BWagSubscriberHomeDhcpStaticSubsDeleted_Type())
bWagSubscriberHomeDhcpStaticSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeDhcpStaticSubsDeleted.setStatus(_A)
_BWagSubscriberHomeDhcpDynSubsDeleted_Type=Unsigned32
_BWagSubscriberHomeDhcpDynSubsDeleted_Object=MibTableColumn
bWagSubscriberHomeDhcpDynSubsDeleted=_BWagSubscriberHomeDhcpDynSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,26),_BWagSubscriberHomeDhcpDynSubsDeleted_Type())
bWagSubscriberHomeDhcpDynSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeDhcpDynSubsDeleted.setStatus(_A)
_BWagSubscriberHomePubStaticSubsDeleted_Type=Unsigned32
_BWagSubscriberHomePubStaticSubsDeleted_Object=MibTableColumn
bWagSubscriberHomePubStaticSubsDeleted=_BWagSubscriberHomePubStaticSubsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,27),_BWagSubscriberHomePubStaticSubsDeleted_Type())
bWagSubscriberHomePubStaticSubsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomePubStaticSubsDeleted.setStatus(_A)
_BWagSubscriberSpWifiActivationsCount_Type=Unsigned32
_BWagSubscriberSpWifiActivationsCount_Object=MibTableColumn
bWagSubscriberSpWifiActivationsCount=_BWagSubscriberSpWifiActivationsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,28),_BWagSubscriberSpWifiActivationsCount_Type())
bWagSubscriberSpWifiActivationsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberSpWifiActivationsCount.setStatus(_A)
_BWagSubscriberHomeActivationsCount_Type=Unsigned32
_BWagSubscriberHomeActivationsCount_Object=MibTableColumn
bWagSubscriberHomeActivationsCount=_BWagSubscriberHomeActivationsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,29),_BWagSubscriberHomeActivationsCount_Type())
bWagSubscriberHomeActivationsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberHomeActivationsCount.setStatus(_A)
_BWagSubscriberDsLiteActivationsCount_Type=Unsigned32
_BWagSubscriberDsLiteActivationsCount_Object=MibTableColumn
bWagSubscriberDsLiteActivationsCount=_BWagSubscriberDsLiteActivationsCount_Object((1,3,6,1,4,1,39406,2,1,3,5,1,1,30),_BWagSubscriberDsLiteActivationsCount_Type())
bWagSubscriberDsLiteActivationsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagSubscriberDsLiteActivationsCount.setStatus(_A)
_BWagNumCurrentSubscribers_Type=Unsigned32
_BWagNumCurrentSubscribers_Object=MibScalar
bWagNumCurrentSubscribers=_BWagNumCurrentSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,2),_BWagNumCurrentSubscribers_Type())
bWagNumCurrentSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentSubscribers.setStatus(_A)
_BWagNumAuthenticatedSubscribers_Type=Unsigned32
_BWagNumAuthenticatedSubscribers_Object=MibScalar
bWagNumAuthenticatedSubscribers=_BWagNumAuthenticatedSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,3),_BWagNumAuthenticatedSubscribers_Type())
bWagNumAuthenticatedSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumAuthenticatedSubscribers.setStatus(_A)
_BWagNumUnauthenticatedSubscribers_Type=Unsigned32
_BWagNumUnauthenticatedSubscribers_Object=MibScalar
bWagNumUnauthenticatedSubscribers=_BWagNumUnauthenticatedSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,4),_BWagNumUnauthenticatedSubscribers_Type())
bWagNumUnauthenticatedSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumUnauthenticatedSubscribers.setStatus(_A)
_BWagNumSubsWithPrivateIPAddress_Type=Unsigned32
_BWagNumSubsWithPrivateIPAddress_Object=MibScalar
bWagNumSubsWithPrivateIPAddress=_BWagNumSubsWithPrivateIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,5,5),_BWagNumSubsWithPrivateIPAddress_Type())
bWagNumSubsWithPrivateIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumSubsWithPrivateIPAddress.setStatus(_A)
_BWagNumAuthSubsWithPublicIPAddress_Type=Unsigned32
_BWagNumAuthSubsWithPublicIPAddress_Object=MibScalar
bWagNumAuthSubsWithPublicIPAddress=_BWagNumAuthSubsWithPublicIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,5,6),_BWagNumAuthSubsWithPublicIPAddress_Type())
bWagNumAuthSubsWithPublicIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumAuthSubsWithPublicIPAddress.setStatus(_A)
_BWagNumUnAuthSubsWithPublicIPAddress_Type=Unsigned32
_BWagNumUnAuthSubsWithPublicIPAddress_Object=MibScalar
bWagNumUnAuthSubsWithPublicIPAddress=_BWagNumUnAuthSubsWithPublicIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,5,7),_BWagNumUnAuthSubsWithPublicIPAddress_Type())
bWagNumUnAuthSubsWithPublicIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumUnAuthSubsWithPublicIPAddress.setStatus(_A)
_BWagNumMigrantSubscribersCount_Type=Unsigned32
_BWagNumMigrantSubscribersCount_Object=MibScalar
bWagNumMigrantSubscribersCount=_BWagNumMigrantSubscribersCount_Object((1,3,6,1,4,1,39406,2,1,3,5,8),_BWagNumMigrantSubscribersCount_Type())
bWagNumMigrantSubscribersCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumMigrantSubscribersCount.setStatus(_A)
_BWagNumRedirectedSubscribersCount_Type=Unsigned32
_BWagNumRedirectedSubscribersCount_Object=MibScalar
bWagNumRedirectedSubscribersCount=_BWagNumRedirectedSubscribersCount_Object((1,3,6,1,4,1,39406,2,1,3,5,9),_BWagNumRedirectedSubscribersCount_Type())
bWagNumRedirectedSubscribersCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumRedirectedSubscribersCount.setStatus(_A)
_BWagPolicyTable_Object=MibTable
bWagPolicyTable=_BWagPolicyTable_Object((1,3,6,1,4,1,39406,2,1,3,5,10))
if mibBuilder.loadTexts:bWagPolicyTable.setStatus(_A)
_BWagPolicyEntry_Object=MibTableRow
bWagPolicyEntry=_BWagPolicyEntry_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1))
bWagPolicyEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:bWagPolicyEntry.setStatus(_A)
class _BWagPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('qos',1),('li',2),('acl',3)))
_BWagPolicyType_Type.__name__=_K
_BWagPolicyType_Object=MibTableColumn
bWagPolicyType=_BWagPolicyType_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,1),_BWagPolicyType_Type())
bWagPolicyType.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagPolicyType.setStatus(_A)
_BWagPolicyIndex_Type=Integer32
_BWagPolicyIndex_Object=MibTableColumn
bWagPolicyIndex=_BWagPolicyIndex_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,2),_BWagPolicyIndex_Type())
bWagPolicyIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagPolicyIndex.setStatus(_A)
_BWagPolicyName_Type=DisplayString
_BWagPolicyName_Object=MibTableColumn
bWagPolicyName=_BWagPolicyName_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,3),_BWagPolicyName_Type())
bWagPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagPolicyName.setStatus(_A)
_BWagNumOfSubscribersWithPolicy_Type=Unsigned32
_BWagNumOfSubscribersWithPolicy_Object=MibTableColumn
bWagNumOfSubscribersWithPolicy=_BWagNumOfSubscribersWithPolicy_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,4),_BWagNumOfSubscribersWithPolicy_Type())
bWagNumOfSubscribersWithPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumOfSubscribersWithPolicy.setStatus(_A)
_BWagNumOfAuthSubscribersWithPolicy_Type=Unsigned32
_BWagNumOfAuthSubscribersWithPolicy_Object=MibTableColumn
bWagNumOfAuthSubscribersWithPolicy=_BWagNumOfAuthSubscribersWithPolicy_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,5),_BWagNumOfAuthSubscribersWithPolicy_Type())
bWagNumOfAuthSubscribersWithPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumOfAuthSubscribersWithPolicy.setStatus(_A)
_BWagNumOfUnAuthSubscribersWithPolicy_Type=Unsigned32
_BWagNumOfUnAuthSubscribersWithPolicy_Object=MibTableColumn
bWagNumOfUnAuthSubscribersWithPolicy=_BWagNumOfUnAuthSubscribersWithPolicy_Object((1,3,6,1,4,1,39406,2,1,3,5,10,1,6),_BWagNumOfUnAuthSubscribersWithPolicy_Type())
bWagNumOfUnAuthSubscribersWithPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumOfUnAuthSubscribersWithPolicy.setStatus(_A)
_BWagNumSubsAuthenticatedWithIPv6Prefix_Type=Unsigned32
_BWagNumSubsAuthenticatedWithIPv6Prefix_Object=MibScalar
bWagNumSubsAuthenticatedWithIPv6Prefix=_BWagNumSubsAuthenticatedWithIPv6Prefix_Object((1,3,6,1,4,1,39406,2,1,3,5,11),_BWagNumSubsAuthenticatedWithIPv6Prefix_Type())
bWagNumSubsAuthenticatedWithIPv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumSubsAuthenticatedWithIPv6Prefix.setStatus(_A)
_BWagNumCurrent8021xSubscribers_Type=Unsigned32
_BWagNumCurrent8021xSubscribers_Object=MibScalar
bWagNumCurrent8021xSubscribers=_BWagNumCurrent8021xSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,12),_BWagNumCurrent8021xSubscribers_Type())
bWagNumCurrent8021xSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrent8021xSubscribers.setStatus(_A)
_BWagNumPreAuthenticatedSubscribers_Type=Unsigned32
_BWagNumPreAuthenticatedSubscribers_Object=MibScalar
bWagNumPreAuthenticatedSubscribers=_BWagNumPreAuthenticatedSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,13),_BWagNumPreAuthenticatedSubscribers_Type())
bWagNumPreAuthenticatedSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumPreAuthenticatedSubscribers.setStatus(_A)
_BWagNumCurrentSingleStaticSubscribers_Type=Unsigned32
_BWagNumCurrentSingleStaticSubscribers_Object=MibScalar
bWagNumCurrentSingleStaticSubscribers=_BWagNumCurrentSingleStaticSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,14),_BWagNumCurrentSingleStaticSubscribers_Type())
bWagNumCurrentSingleStaticSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentSingleStaticSubscribers.setStatus(_A)
_BWagNumCurrentRoutedSubnetSubscribers_Type=Unsigned32
_BWagNumCurrentRoutedSubnetSubscribers_Object=MibScalar
bWagNumCurrentRoutedSubnetSubscribers=_BWagNumCurrentRoutedSubnetSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,15),_BWagNumCurrentRoutedSubnetSubscribers_Type())
bWagNumCurrentRoutedSubnetSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentRoutedSubnetSubscribers.setStatus(_A)
_BWagNumSubsUnauthenticatedWithIPv6Prefix_Type=Unsigned32
_BWagNumSubsUnauthenticatedWithIPv6Prefix_Object=MibScalar
bWagNumSubsUnauthenticatedWithIPv6Prefix=_BWagNumSubsUnauthenticatedWithIPv6Prefix_Object((1,3,6,1,4,1,39406,2,1,3,5,16),_BWagNumSubsUnauthenticatedWithIPv6Prefix_Type())
bWagNumSubsUnauthenticatedWithIPv6Prefix.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumSubsUnauthenticatedWithIPv6Prefix.setStatus(_A)
_BWagNumSubsViaStaticAuthPolicy_Type=Unsigned32
_BWagNumSubsViaStaticAuthPolicy_Object=MibScalar
bWagNumSubsViaStaticAuthPolicy=_BWagNumSubsViaStaticAuthPolicy_Object((1,3,6,1,4,1,39406,2,1,3,5,17),_BWagNumSubsViaStaticAuthPolicy_Type())
bWagNumSubsViaStaticAuthPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumSubsViaStaticAuthPolicy.setStatus(_A)
_BWagNumCurrentHomeSubscribers_Type=Unsigned32
_BWagNumCurrentHomeSubscribers_Object=MibScalar
bWagNumCurrentHomeSubscribers=_BWagNumCurrentHomeSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,18),_BWagNumCurrentHomeSubscribers_Type())
bWagNumCurrentHomeSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomeSubscribers.setStatus(_A)
_BWagNumCurrentSPWiFiSubscribers_Type=Unsigned32
_BWagNumCurrentSPWiFiSubscribers_Object=MibScalar
bWagNumCurrentSPWiFiSubscribers=_BWagNumCurrentSPWiFiSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,19),_BWagNumCurrentSPWiFiSubscribers_Type())
bWagNumCurrentSPWiFiSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentSPWiFiSubscribers.setStatus(_A)
_BWagNumCurrentHomeTransientSubs_Type=Unsigned32
_BWagNumCurrentHomeTransientSubs_Object=MibScalar
bWagNumCurrentHomeTransientSubs=_BWagNumCurrentHomeTransientSubs_Object((1,3,6,1,4,1,39406,2,1,3,5,20),_BWagNumCurrentHomeTransientSubs_Type())
bWagNumCurrentHomeTransientSubs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomeTransientSubs.setStatus(_A)
_BWagNumCurrentHomeUserStatSubs_Type=Unsigned32
_BWagNumCurrentHomeUserStatSubs_Object=MibScalar
bWagNumCurrentHomeUserStatSubs=_BWagNumCurrentHomeUserStatSubs_Object((1,3,6,1,4,1,39406,2,1,3,5,21),_BWagNumCurrentHomeUserStatSubs_Type())
bWagNumCurrentHomeUserStatSubs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomeUserStatSubs.setStatus(_A)
_BWagNumCurrentHomeDhcpStatSubs_Type=Unsigned32
_BWagNumCurrentHomeDhcpStatSubs_Object=MibScalar
bWagNumCurrentHomeDhcpStatSubs=_BWagNumCurrentHomeDhcpStatSubs_Object((1,3,6,1,4,1,39406,2,1,3,5,22),_BWagNumCurrentHomeDhcpStatSubs_Type())
bWagNumCurrentHomeDhcpStatSubs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomeDhcpStatSubs.setStatus(_A)
_BWagNumCurrentHomeDhcpDynSubs_Type=Unsigned32
_BWagNumCurrentHomeDhcpDynSubs_Object=MibScalar
bWagNumCurrentHomeDhcpDynSubs=_BWagNumCurrentHomeDhcpDynSubs_Object((1,3,6,1,4,1,39406,2,1,3,5,23),_BWagNumCurrentHomeDhcpDynSubs_Type())
bWagNumCurrentHomeDhcpDynSubs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomeDhcpDynSubs.setStatus(_A)
_BWagNumCurrentHomePubStatSubs_Type=Unsigned32
_BWagNumCurrentHomePubStatSubs_Object=MibScalar
bWagNumCurrentHomePubStatSubs=_BWagNumCurrentHomePubStatSubs_Object((1,3,6,1,4,1,39406,2,1,3,5,24),_BWagNumCurrentHomePubStatSubs_Type())
bWagNumCurrentHomePubStatSubs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentHomePubStatSubs.setStatus(_A)
_BWagNumPreAuthSpwifiSubscribers_Type=Unsigned32
_BWagNumPreAuthSpwifiSubscribers_Object=MibScalar
bWagNumPreAuthSpwifiSubscribers=_BWagNumPreAuthSpwifiSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,25),_BWagNumPreAuthSpwifiSubscribers_Type())
bWagNumPreAuthSpwifiSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumPreAuthSpwifiSubscribers.setStatus(_A)
_BWagNumPreAuthHomeSubscribers_Type=Unsigned32
_BWagNumPreAuthHomeSubscribers_Object=MibScalar
bWagNumPreAuthHomeSubscribers=_BWagNumPreAuthHomeSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,26),_BWagNumPreAuthHomeSubscribers_Type())
bWagNumPreAuthHomeSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumPreAuthHomeSubscribers.setStatus(_A)
_BWagNumPreAuthenticatedSubscribersS2aPmip6_Type=Unsigned32
_BWagNumPreAuthenticatedSubscribersS2aPmip6_Object=MibScalar
bWagNumPreAuthenticatedSubscribersS2aPmip6=_BWagNumPreAuthenticatedSubscribersS2aPmip6_Object((1,3,6,1,4,1,39406,2,1,3,5,27),_BWagNumPreAuthenticatedSubscribersS2aPmip6_Type())
bWagNumPreAuthenticatedSubscribersS2aPmip6.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumPreAuthenticatedSubscribersS2aPmip6.setStatus(_A)
_BWagNumCurrentSSIDS2aSubscribersPmip6_Type=Unsigned32
_BWagNumCurrentSSIDS2aSubscribersPmip6_Object=MibScalar
bWagNumCurrentSSIDS2aSubscribersPmip6=_BWagNumCurrentSSIDS2aSubscribersPmip6_Object((1,3,6,1,4,1,39406,2,1,3,5,28),_BWagNumCurrentSSIDS2aSubscribersPmip6_Type())
bWagNumCurrentSSIDS2aSubscribersPmip6.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentSSIDS2aSubscribersPmip6.setStatus(_A)
_BWagNumCurrentDSLiteSubscribers_Type=Unsigned32
_BWagNumCurrentDSLiteSubscribers_Object=MibScalar
bWagNumCurrentDSLiteSubscribers=_BWagNumCurrentDSLiteSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,5,29),_BWagNumCurrentDSLiteSubscribers_Type())
bWagNumCurrentDSLiteSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentDSLiteSubscribers.setStatus(_A)
_BWagSubscriberNotifObjects_ObjectIdentity=ObjectIdentity
bWagSubscriberNotifObjects=_BWagSubscriberNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,6))
if mibBuilder.loadTexts:bWagSubscriberNotifObjects.setStatus(_A)
_BWagTunnelStatsMIBObjects_ObjectIdentity=ObjectIdentity
bWagTunnelStatsMIBObjects=_BWagTunnelStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,7))
if mibBuilder.loadTexts:bWagTunnelStatsMIBObjects.setStatus(_A)
_BWagTunnelTable_Object=MibTable
bWagTunnelTable=_BWagTunnelTable_Object((1,3,6,1,4,1,39406,2,1,3,7,1))
if mibBuilder.loadTexts:bWagTunnelTable.setStatus(_A)
_BWagTunnelEntry_Object=MibTableRow
bWagTunnelEntry=_BWagTunnelEntry_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1))
bWagTunnelEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:bWagTunnelEntry.setStatus(_A)
_BWagTunnelStatsInterval_Type=Integer32
_BWagTunnelStatsInterval_Object=MibTableColumn
bWagTunnelStatsInterval=_BWagTunnelStatsInterval_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,1),_BWagTunnelStatsInterval_Type())
bWagTunnelStatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagTunnelStatsInterval.setStatus(_A)
_BWagTunnelIntervalDuration_Type=Integer32
_BWagTunnelIntervalDuration_Object=MibTableColumn
bWagTunnelIntervalDuration=_BWagTunnelIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,2),_BWagTunnelIntervalDuration_Type())
bWagTunnelIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelIntervalDuration.setStatus(_A)
_BWagTunnelPktsRxdGRE_Type=Unsigned32
_BWagTunnelPktsRxdGRE_Object=MibTableColumn
bWagTunnelPktsRxdGRE=_BWagTunnelPktsRxdGRE_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,3),_BWagTunnelPktsRxdGRE_Type())
bWagTunnelPktsRxdGRE.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdGRE.setStatus(_A)
_BWagTunnelPktsRxdGREPayloadTEB_Type=Unsigned32
_BWagTunnelPktsRxdGREPayloadTEB_Object=MibTableColumn
bWagTunnelPktsRxdGREPayloadTEB=_BWagTunnelPktsRxdGREPayloadTEB_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,4),_BWagTunnelPktsRxdGREPayloadTEB_Type())
bWagTunnelPktsRxdGREPayloadTEB.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdGREPayloadTEB.setStatus(_A)
_BWagTunnelPktsRxdGREPayloadMPLS_Type=Unsigned32
_BWagTunnelPktsRxdGREPayloadMPLS_Object=MibTableColumn
bWagTunnelPktsRxdGREPayloadMPLS=_BWagTunnelPktsRxdGREPayloadMPLS_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,5),_BWagTunnelPktsRxdGREPayloadMPLS_Type())
bWagTunnelPktsRxdGREPayloadMPLS.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdGREPayloadMPLS.setStatus(_A)
_BWagTunnelPktsEncapsulatedGRE_Type=Unsigned32
_BWagTunnelPktsEncapsulatedGRE_Object=MibTableColumn
bWagTunnelPktsEncapsulatedGRE=_BWagTunnelPktsEncapsulatedGRE_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,6),_BWagTunnelPktsEncapsulatedGRE_Type())
bWagTunnelPktsEncapsulatedGRE.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsEncapsulatedGRE.setStatus(_A)
_BWagTunnelPktsDecapsulatedGRE_Type=Unsigned32
_BWagTunnelPktsDecapsulatedGRE_Object=MibTableColumn
bWagTunnelPktsDecapsulatedGRE=_BWagTunnelPktsDecapsulatedGRE_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,7),_BWagTunnelPktsDecapsulatedGRE_Type())
bWagTunnelPktsDecapsulatedGRE.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsDecapsulatedGRE.setStatus(_A)
_BWagTunnelPktsRxdARP_Type=Unsigned32
_BWagTunnelPktsRxdARP_Object=MibTableColumn
bWagTunnelPktsRxdARP=_BWagTunnelPktsRxdARP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,8),_BWagTunnelPktsRxdARP_Type())
bWagTunnelPktsRxdARP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdARP.setStatus(_A)
_BWagTunnelPktsRxdDHCP_Type=Unsigned32
_BWagTunnelPktsRxdDHCP_Object=MibTableColumn
bWagTunnelPktsRxdDHCP=_BWagTunnelPktsRxdDHCP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,9),_BWagTunnelPktsRxdDHCP_Type())
bWagTunnelPktsRxdDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdDHCP.setStatus(_A)
_BWagTunnelPktsRxdDNS_Type=Unsigned32
_BWagTunnelPktsRxdDNS_Object=MibTableColumn
bWagTunnelPktsRxdDNS=_BWagTunnelPktsRxdDNS_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,10),_BWagTunnelPktsRxdDNS_Type())
bWagTunnelPktsRxdDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdDNS.setStatus(_C)
_BWagTunnelPktsRxdHTTP_Type=Unsigned32
_BWagTunnelPktsRxdHTTP_Object=MibTableColumn
bWagTunnelPktsRxdHTTP=_BWagTunnelPktsRxdHTTP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,11),_BWagTunnelPktsRxdHTTP_Type())
bWagTunnelPktsRxdHTTP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdHTTP.setStatus(_C)
_BWagTunnelPktsRxdHTTPGetReq_Type=Unsigned32
_BWagTunnelPktsRxdHTTPGetReq_Object=MibTableColumn
bWagTunnelPktsRxdHTTPGetReq=_BWagTunnelPktsRxdHTTPGetReq_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,12),_BWagTunnelPktsRxdHTTPGetReq_Type())
bWagTunnelPktsRxdHTTPGetReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdHTTPGetReq.setStatus(_C)
_BWagTunnelPktsTxdHTTP_Type=Unsigned32
_BWagTunnelPktsTxdHTTP_Object=MibTableColumn
bWagTunnelPktsTxdHTTP=_BWagTunnelPktsTxdHTTP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,13),_BWagTunnelPktsTxdHTTP_Type())
bWagTunnelPktsTxdHTTP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsTxdHTTP.setStatus(_C)
_BWagTunnelPktsTxdHTTPRedir_Type=Unsigned32
_BWagTunnelPktsTxdHTTPRedir_Object=MibTableColumn
bWagTunnelPktsTxdHTTPRedir=_BWagTunnelPktsTxdHTTPRedir_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,14),_BWagTunnelPktsTxdHTTPRedir_Type())
bWagTunnelPktsTxdHTTPRedir.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsTxdHTTPRedir.setStatus(_C)
_BWagTunnelPktsRxdHTTPS_Type=Unsigned32
_BWagTunnelPktsRxdHTTPS_Object=MibTableColumn
bWagTunnelPktsRxdHTTPS=_BWagTunnelPktsRxdHTTPS_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,15),_BWagTunnelPktsRxdHTTPS_Type())
bWagTunnelPktsRxdHTTPS.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdHTTPS.setStatus(_C)
_BWagTunnelPktsRxdTCPSyn_Type=Unsigned32
_BWagTunnelPktsRxdTCPSyn_Object=MibTableColumn
bWagTunnelPktsRxdTCPSyn=_BWagTunnelPktsRxdTCPSyn_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,16),_BWagTunnelPktsRxdTCPSyn_Type())
bWagTunnelPktsRxdTCPSyn.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdTCPSyn.setStatus(_C)
_BWagTunnelPktsTxdTCPSynAck_Type=Unsigned32
_BWagTunnelPktsTxdTCPSynAck_Object=MibTableColumn
bWagTunnelPktsTxdTCPSynAck=_BWagTunnelPktsTxdTCPSynAck_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,17),_BWagTunnelPktsTxdTCPSynAck_Type())
bWagTunnelPktsTxdTCPSynAck.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsTxdTCPSynAck.setStatus(_C)
_BWagTunnelPktsTxdTCPFin_Type=Unsigned32
_BWagTunnelPktsTxdTCPFin_Object=MibTableColumn
bWagTunnelPktsTxdTCPFin=_BWagTunnelPktsTxdTCPFin_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,18),_BWagTunnelPktsTxdTCPFin_Type())
bWagTunnelPktsTxdTCPFin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsTxdTCPFin.setStatus(_C)
_BWagTunnelPktsRxdTCPFinAck_Type=Unsigned32
_BWagTunnelPktsRxdTCPFinAck_Object=MibTableColumn
bWagTunnelPktsRxdTCPFinAck=_BWagTunnelPktsRxdTCPFinAck_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,19),_BWagTunnelPktsRxdTCPFinAck_Type())
bWagTunnelPktsRxdTCPFinAck.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsRxdTCPFinAck.setStatus(_C)
_BWagTunnelPktsTxdTCPAck2Fin_Type=Unsigned32
_BWagTunnelPktsTxdTCPAck2Fin_Object=MibTableColumn
bWagTunnelPktsTxdTCPAck2Fin=_BWagTunnelPktsTxdTCPAck2Fin_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,20),_BWagTunnelPktsTxdTCPAck2Fin_Type())
bWagTunnelPktsTxdTCPAck2Fin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelPktsTxdTCPAck2Fin.setStatus(_C)
_BWagTunnelCreatedDynamically_Type=Unsigned32
_BWagTunnelCreatedDynamically_Object=MibTableColumn
bWagTunnelCreatedDynamically=_BWagTunnelCreatedDynamically_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,21),_BWagTunnelCreatedDynamically_Type())
bWagTunnelCreatedDynamically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelCreatedDynamically.setStatus(_A)
_BWagTunnelCreatedStatically_Type=Unsigned32
_BWagTunnelCreatedStatically_Object=MibTableColumn
bWagTunnelCreatedStatically=_BWagTunnelCreatedStatically_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,22),_BWagTunnelCreatedStatically_Type())
bWagTunnelCreatedStatically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelCreatedStatically.setStatus(_A)
_BWagTunnelDeleted_Type=Unsigned32
_BWagTunnelDeleted_Object=MibTableColumn
bWagTunnelDeleted=_BWagTunnelDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,23),_BWagTunnelDeleted_Type())
bWagTunnelDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeleted.setStatus(_A)
_BWagTunnelDeletedDueToInactivity_Type=Unsigned32
_BWagTunnelDeletedDueToInactivity_Object=MibTableColumn
bWagTunnelDeletedDueToInactivity=_BWagTunnelDeletedDueToInactivity_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,24),_BWagTunnelDeletedDueToInactivity_Type())
bWagTunnelDeletedDueToInactivity.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToInactivity.setStatus(_A)
_BWagTunnelDeletedByCommand_Type=Unsigned32
_BWagTunnelDeletedByCommand_Object=MibTableColumn
bWagTunnelDeletedByCommand=_BWagTunnelDeletedByCommand_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,25),_BWagTunnelDeletedByCommand_Type())
bWagTunnelDeletedByCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedByCommand.setStatus(_A)
_BWagTunnelMaxSupported_Type=Unsigned32
_BWagTunnelMaxSupported_Object=MibTableColumn
bWagTunnelMaxSupported=_BWagTunnelMaxSupported_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,26),_BWagTunnelMaxSupported_Type())
bWagTunnelMaxSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelMaxSupported.setStatus(_A)
_BWagTunnelMaxCountReached_Type=Unsigned32
_BWagTunnelMaxCountReached_Object=MibTableColumn
bWagTunnelMaxCountReached=_BWagTunnelMaxCountReached_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,27),_BWagTunnelMaxCountReached_Type())
bWagTunnelMaxCountReached.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelMaxCountReached.setStatus(_A)
_BWagTunnelTunnelsLookupFound_Type=Unsigned32
_BWagTunnelTunnelsLookupFound_Object=MibTableColumn
bWagTunnelTunnelsLookupFound=_BWagTunnelTunnelsLookupFound_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,28),_BWagTunnelTunnelsLookupFound_Type())
bWagTunnelTunnelsLookupFound.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelTunnelsLookupFound.setStatus(_A)
_BWagTunnelTunnelsLookupNotFound_Type=Unsigned32
_BWagTunnelTunnelsLookupNotFound_Object=MibTableColumn
bWagTunnelTunnelsLookupNotFound=_BWagTunnelTunnelsLookupNotFound_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,29),_BWagTunnelTunnelsLookupNotFound_Type())
bWagTunnelTunnelsLookupNotFound.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelTunnelsLookupNotFound.setStatus(_A)
_BWagTunnelCountHighThreshold_Type=Unsigned32
_BWagTunnelCountHighThreshold_Object=MibTableColumn
bWagTunnelCountHighThreshold=_BWagTunnelCountHighThreshold_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,30),_BWagTunnelCountHighThreshold_Type())
bWagTunnelCountHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelCountHighThreshold.setStatus(_A)
_BWagTunnelCountLowThreshold_Type=Unsigned32
_BWagTunnelCountLowThreshold_Object=MibTableColumn
bWagTunnelCountLowThreshold=_BWagTunnelCountLowThreshold_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,31),_BWagTunnelCountLowThreshold_Type())
bWagTunnelCountLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelCountLowThreshold.setStatus(_A)
_BWagTunnelDeletedDueToReject_Type=Unsigned32
_BWagTunnelDeletedDueToReject_Object=MibTableColumn
bWagTunnelDeletedDueToReject=_BWagTunnelDeletedDueToReject_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,32),_BWagTunnelDeletedDueToReject_Type())
bWagTunnelDeletedDueToReject.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToReject.setStatus(_A)
_BWagTunnelDeletedDueToAbort_Type=Unsigned32
_BWagTunnelDeletedDueToAbort_Object=MibTableColumn
bWagTunnelDeletedDueToAbort=_BWagTunnelDeletedDueToAbort_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,33),_BWagTunnelDeletedDueToAbort_Type())
bWagTunnelDeletedDueToAbort.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToAbort.setStatus(_A)
_BWagTunnelDeletedDueToMacResFail_Type=Unsigned32
_BWagTunnelDeletedDueToMacResFail_Object=MibTableColumn
bWagTunnelDeletedDueToMacResFail=_BWagTunnelDeletedDueToMacResFail_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,34),_BWagTunnelDeletedDueToMacResFail_Type())
bWagTunnelDeletedDueToMacResFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToMacResFail.setStatus(_A)
_BWagTunnelDeletedDueToLifDown_Type=Unsigned32
_BWagTunnelDeletedDueToLifDown_Object=MibTableColumn
bWagTunnelDeletedDueToLifDown=_BWagTunnelDeletedDueToLifDown_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,35),_BWagTunnelDeletedDueToLifDown_Type())
bWagTunnelDeletedDueToLifDown.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToLifDown.setStatus(_A)
_BWagTunnelDeletedDueToB2bSubsDelete_Type=Unsigned32
_BWagTunnelDeletedDueToB2bSubsDelete_Object=MibTableColumn
bWagTunnelDeletedDueToB2bSubsDelete=_BWagTunnelDeletedDueToB2bSubsDelete_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,36),_BWagTunnelDeletedDueToB2bSubsDelete_Type())
bWagTunnelDeletedDueToB2bSubsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagTunnelDeletedDueToB2bSubsDelete.setStatus(_A)
_BWagL2tpv3TunnelPktsRxd_Type=Unsigned32
_BWagL2tpv3TunnelPktsRxd_Object=MibTableColumn
bWagL2tpv3TunnelPktsRxd=_BWagL2tpv3TunnelPktsRxd_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,37),_BWagL2tpv3TunnelPktsRxd_Type())
bWagL2tpv3TunnelPktsRxd.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsRxd.setStatus(_A)
_BWagL2tpv3TunnelPktsEncapsulated_Type=Unsigned32
_BWagL2tpv3TunnelPktsEncapsulated_Object=MibTableColumn
bWagL2tpv3TunnelPktsEncapsulated=_BWagL2tpv3TunnelPktsEncapsulated_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,38),_BWagL2tpv3TunnelPktsEncapsulated_Type())
bWagL2tpv3TunnelPktsEncapsulated.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsEncapsulated.setStatus(_A)
_BWagL2tpv3TunnelPktsDecapsulated_Type=Unsigned32
_BWagL2tpv3TunnelPktsDecapsulated_Object=MibTableColumn
bWagL2tpv3TunnelPktsDecapsulated=_BWagL2tpv3TunnelPktsDecapsulated_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,39),_BWagL2tpv3TunnelPktsDecapsulated_Type())
bWagL2tpv3TunnelPktsDecapsulated.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsDecapsulated.setStatus(_A)
_BWagL2tpv3TunnelPktsRxdARP_Type=Unsigned32
_BWagL2tpv3TunnelPktsRxdARP_Object=MibTableColumn
bWagL2tpv3TunnelPktsRxdARP=_BWagL2tpv3TunnelPktsRxdARP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,40),_BWagL2tpv3TunnelPktsRxdARP_Type())
bWagL2tpv3TunnelPktsRxdARP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsRxdARP.setStatus(_A)
_BWagL2tpv3TunnelPktsRxdDHCP_Type=Unsigned32
_BWagL2tpv3TunnelPktsRxdDHCP_Object=MibTableColumn
bWagL2tpv3TunnelPktsRxdDHCP=_BWagL2tpv3TunnelPktsRxdDHCP_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,41),_BWagL2tpv3TunnelPktsRxdDHCP_Type())
bWagL2tpv3TunnelPktsRxdDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsRxdDHCP.setStatus(_A)
_BWagL2tpv3TunnelPktsRxdDNS_Type=Unsigned32
_BWagL2tpv3TunnelPktsRxdDNS_Object=MibTableColumn
bWagL2tpv3TunnelPktsRxdDNS=_BWagL2tpv3TunnelPktsRxdDNS_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,42),_BWagL2tpv3TunnelPktsRxdDNS_Type())
bWagL2tpv3TunnelPktsRxdDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelPktsRxdDNS.setStatus(_C)
_BWagL2tpv3TunnelCreatedDynamically_Type=Unsigned32
_BWagL2tpv3TunnelCreatedDynamically_Object=MibTableColumn
bWagL2tpv3TunnelCreatedDynamically=_BWagL2tpv3TunnelCreatedDynamically_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,43),_BWagL2tpv3TunnelCreatedDynamically_Type())
bWagL2tpv3TunnelCreatedDynamically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelCreatedDynamically.setStatus(_A)
_BWagL2tpv3TunnelDeleted_Type=Unsigned32
_BWagL2tpv3TunnelDeleted_Object=MibTableColumn
bWagL2tpv3TunnelDeleted=_BWagL2tpv3TunnelDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,44),_BWagL2tpv3TunnelDeleted_Type())
bWagL2tpv3TunnelDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelDeleted.setStatus(_A)
_BWagL2tpv3TunnelDeletedDueToInactivity_Type=Unsigned32
_BWagL2tpv3TunnelDeletedDueToInactivity_Object=MibTableColumn
bWagL2tpv3TunnelDeletedDueToInactivity=_BWagL2tpv3TunnelDeletedDueToInactivity_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,45),_BWagL2tpv3TunnelDeletedDueToInactivity_Type())
bWagL2tpv3TunnelDeletedDueToInactivity.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelDeletedDueToInactivity.setStatus(_A)
_BWagL2tpv3TunnelDeletedByCommand_Type=Unsigned32
_BWagL2tpv3TunnelDeletedByCommand_Object=MibTableColumn
bWagL2tpv3TunnelDeletedByCommand=_BWagL2tpv3TunnelDeletedByCommand_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,46),_BWagL2tpv3TunnelDeletedByCommand_Type())
bWagL2tpv3TunnelDeletedByCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelDeletedByCommand.setStatus(_A)
_BWagL2tpv3TunnelDeletedDueToLifDown_Type=Unsigned32
_BWagL2tpv3TunnelDeletedDueToLifDown_Object=MibTableColumn
bWagL2tpv3TunnelDeletedDueToLifDown=_BWagL2tpv3TunnelDeletedDueToLifDown_Object((1,3,6,1,4,1,39406,2,1,3,7,1,1,47),_BWagL2tpv3TunnelDeletedDueToLifDown_Type())
bWagL2tpv3TunnelDeletedDueToLifDown.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagL2tpv3TunnelDeletedDueToLifDown.setStatus(_A)
_BWagNumCurrentTunnels_Type=Unsigned32
_BWagNumCurrentTunnels_Object=MibScalar
bWagNumCurrentTunnels=_BWagNumCurrentTunnels_Object((1,3,6,1,4,1,39406,2,1,3,7,2),_BWagNumCurrentTunnels_Type())
bWagNumCurrentTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnels.setStatus(_A)
_BWagNumTunnelsCreatedDynamically_Type=Counter64
_BWagNumTunnelsCreatedDynamically_Object=MibScalar
bWagNumTunnelsCreatedDynamically=_BWagNumTunnelsCreatedDynamically_Object((1,3,6,1,4,1,39406,2,1,3,7,3),_BWagNumTunnelsCreatedDynamically_Type())
bWagNumTunnelsCreatedDynamically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsCreatedDynamically.setStatus(_A)
_BWagNumTunnelsCreatedStatically_Type=Counter64
_BWagNumTunnelsCreatedStatically_Object=MibScalar
bWagNumTunnelsCreatedStatically=_BWagNumTunnelsCreatedStatically_Object((1,3,6,1,4,1,39406,2,1,3,7,4),_BWagNumTunnelsCreatedStatically_Type())
bWagNumTunnelsCreatedStatically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsCreatedStatically.setStatus(_A)
_BWagNumTunnelsDeleted_Type=Counter64
_BWagNumTunnelsDeleted_Object=MibScalar
bWagNumTunnelsDeleted=_BWagNumTunnelsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,5),_BWagNumTunnelsDeleted_Type())
bWagNumTunnelsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsDeleted.setStatus(_A)
_BWagNumTunnelsInactiveDeleted_Type=Counter64
_BWagNumTunnelsInactiveDeleted_Object=MibScalar
bWagNumTunnelsInactiveDeleted=_BWagNumTunnelsInactiveDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,6),_BWagNumTunnelsInactiveDeleted_Type())
bWagNumTunnelsInactiveDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsInactiveDeleted.setStatus(_A)
_BWagNumTunnelsDeletedByCommand_Type=Counter64
_BWagNumTunnelsDeletedByCommand_Object=MibScalar
bWagNumTunnelsDeletedByCommand=_BWagNumTunnelsDeletedByCommand_Object((1,3,6,1,4,1,39406,2,1,3,7,7),_BWagNumTunnelsDeletedByCommand_Type())
bWagNumTunnelsDeletedByCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsDeletedByCommand.setStatus(_A)
_BWagNumTunnelsSubsAssociated_Type=Unsigned32
_BWagNumTunnelsSubsAssociated_Object=MibScalar
bWagNumTunnelsSubsAssociated=_BWagNumTunnelsSubsAssociated_Object((1,3,6,1,4,1,39406,2,1,3,7,8),_BWagNumTunnelsSubsAssociated_Type())
bWagNumTunnelsSubsAssociated.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsSubsAssociated.setStatus(_A)
_BWagNumTunnelsSchedDeletion_Type=Unsigned32
_BWagNumTunnelsSchedDeletion_Object=MibScalar
bWagNumTunnelsSchedDeletion=_BWagNumTunnelsSchedDeletion_Object((1,3,6,1,4,1,39406,2,1,3,7,9),_BWagNumTunnelsSchedDeletion_Type())
bWagNumTunnelsSchedDeletion.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsSchedDeletion.setStatus(_A)
_BWagNumCurrentTunnelsIPv4_Type=Unsigned32
_BWagNumCurrentTunnelsIPv4_Object=MibScalar
bWagNumCurrentTunnelsIPv4=_BWagNumCurrentTunnelsIPv4_Object((1,3,6,1,4,1,39406,2,1,3,7,10),_BWagNumCurrentTunnelsIPv4_Type())
bWagNumCurrentTunnelsIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnelsIPv4.setStatus(_A)
_BWagNumCurrentTunnelsIPv6_Type=Unsigned32
_BWagNumCurrentTunnelsIPv6_Object=MibScalar
bWagNumCurrentTunnelsIPv6=_BWagNumCurrentTunnelsIPv6_Object((1,3,6,1,4,1,39406,2,1,3,7,11),_BWagNumCurrentTunnelsIPv6_Type())
bWagNumCurrentTunnelsIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnelsIPv6.setStatus(_A)
_BWagNumTunnelsDeletedByB2B_Type=Counter64
_BWagNumTunnelsDeletedByB2B_Object=MibScalar
bWagNumTunnelsDeletedByB2B=_BWagNumTunnelsDeletedByB2B_Object((1,3,6,1,4,1,39406,2,1,3,7,12),_BWagNumTunnelsDeletedByB2B_Type())
bWagNumTunnelsDeletedByB2B.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsDeletedByB2B.setStatus(_A)
_BWagNumTunnelsDeletedDuetoLIFDown_Type=Counter64
_BWagNumTunnelsDeletedDuetoLIFDown_Object=MibScalar
bWagNumTunnelsDeletedDuetoLIFDown=_BWagNumTunnelsDeletedDuetoLIFDown_Object((1,3,6,1,4,1,39406,2,1,3,7,13),_BWagNumTunnelsDeletedDuetoLIFDown_Type())
bWagNumTunnelsDeletedDuetoLIFDown.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumTunnelsDeletedDuetoLIFDown.setStatus(_A)
_BWagNumCurrentTunnelsSpWiFi_Type=Unsigned32
_BWagNumCurrentTunnelsSpWiFi_Object=MibScalar
bWagNumCurrentTunnelsSpWiFi=_BWagNumCurrentTunnelsSpWiFi_Object((1,3,6,1,4,1,39406,2,1,3,7,14),_BWagNumCurrentTunnelsSpWiFi_Type())
bWagNumCurrentTunnelsSpWiFi.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnelsSpWiFi.setStatus(_A)
_BWagNumCurrentTunnelsHome_Type=Unsigned32
_BWagNumCurrentTunnelsHome_Object=MibScalar
bWagNumCurrentTunnelsHome=_BWagNumCurrentTunnelsHome_Object((1,3,6,1,4,1,39406,2,1,3,7,15),_BWagNumCurrentTunnelsHome_Type())
bWagNumCurrentTunnelsHome.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnelsHome.setStatus(_A)
_BWagNumCurrTunnHomeAndSpWiFi_Type=Unsigned32
_BWagNumCurrTunnHomeAndSpWiFi_Object=MibScalar
bWagNumCurrTunnHomeAndSpWiFi=_BWagNumCurrTunnHomeAndSpWiFi_Object((1,3,6,1,4,1,39406,2,1,3,7,16),_BWagNumCurrTunnHomeAndSpWiFi_Type())
bWagNumCurrTunnHomeAndSpWiFi.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrTunnHomeAndSpWiFi.setStatus(_A)
_BWagNumCurrentTunnHomeInactive_Type=Unsigned32
_BWagNumCurrentTunnHomeInactive_Object=MibScalar
bWagNumCurrentTunnHomeInactive=_BWagNumCurrentTunnHomeInactive_Object((1,3,6,1,4,1,39406,2,1,3,7,17),_BWagNumCurrentTunnHomeInactive_Type())
bWagNumCurrentTunnHomeInactive.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnHomeInactive.setStatus(_A)
_BWagNumCurrentTunnHomeAccept_Type=Unsigned32
_BWagNumCurrentTunnHomeAccept_Object=MibScalar
bWagNumCurrentTunnHomeAccept=_BWagNumCurrentTunnHomeAccept_Object((1,3,6,1,4,1,39406,2,1,3,7,18),_BWagNumCurrentTunnHomeAccept_Type())
bWagNumCurrentTunnHomeAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnHomeAccept.setStatus(_A)
_BWagNumL2tpv3TunnelsCreatedDynamically_Type=Counter64
_BWagNumL2tpv3TunnelsCreatedDynamically_Object=MibScalar
bWagNumL2tpv3TunnelsCreatedDynamically=_BWagNumL2tpv3TunnelsCreatedDynamically_Object((1,3,6,1,4,1,39406,2,1,3,7,19),_BWagNumL2tpv3TunnelsCreatedDynamically_Type())
bWagNumL2tpv3TunnelsCreatedDynamically.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsCreatedDynamically.setStatus(_A)
_BWagNumL2tpv3TunnelsDeleted_Type=Counter64
_BWagNumL2tpv3TunnelsDeleted_Object=MibScalar
bWagNumL2tpv3TunnelsDeleted=_BWagNumL2tpv3TunnelsDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,20),_BWagNumL2tpv3TunnelsDeleted_Type())
bWagNumL2tpv3TunnelsDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsDeleted.setStatus(_A)
_BWagNumL2tpv3TunnelsInactiveDeleted_Type=Counter64
_BWagNumL2tpv3TunnelsInactiveDeleted_Object=MibScalar
bWagNumL2tpv3TunnelsInactiveDeleted=_BWagNumL2tpv3TunnelsInactiveDeleted_Object((1,3,6,1,4,1,39406,2,1,3,7,21),_BWagNumL2tpv3TunnelsInactiveDeleted_Type())
bWagNumL2tpv3TunnelsInactiveDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsInactiveDeleted.setStatus(_A)
_BWagNumL2tpv3TunnelsDeletedByCommand_Type=Counter64
_BWagNumL2tpv3TunnelsDeletedByCommand_Object=MibScalar
bWagNumL2tpv3TunnelsDeletedByCommand=_BWagNumL2tpv3TunnelsDeletedByCommand_Object((1,3,6,1,4,1,39406,2,1,3,7,22),_BWagNumL2tpv3TunnelsDeletedByCommand_Type())
bWagNumL2tpv3TunnelsDeletedByCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsDeletedByCommand.setStatus(_A)
_BWagNumL2tpv3TunnelsSubsAssociated_Type=Unsigned32
_BWagNumL2tpv3TunnelsSubsAssociated_Object=MibScalar
bWagNumL2tpv3TunnelsSubsAssociated=_BWagNumL2tpv3TunnelsSubsAssociated_Object((1,3,6,1,4,1,39406,2,1,3,7,23),_BWagNumL2tpv3TunnelsSubsAssociated_Type())
bWagNumL2tpv3TunnelsSubsAssociated.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsSubsAssociated.setStatus(_A)
_BWagNumCurrentL2tpv3TunnelsIPv4_Type=Unsigned32
_BWagNumCurrentL2tpv3TunnelsIPv4_Object=MibScalar
bWagNumCurrentL2tpv3TunnelsIPv4=_BWagNumCurrentL2tpv3TunnelsIPv4_Object((1,3,6,1,4,1,39406,2,1,3,7,24),_BWagNumCurrentL2tpv3TunnelsIPv4_Type())
bWagNumCurrentL2tpv3TunnelsIPv4.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentL2tpv3TunnelsIPv4.setStatus(_A)
_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Type=Counter64
_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Object=MibScalar
bWagNumL2tpv3TunnelsDeletedDuetoLIFDown=_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Object((1,3,6,1,4,1,39406,2,1,3,7,25),_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Type())
bWagNumL2tpv3TunnelsDeletedDuetoLIFDown.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumL2tpv3TunnelsDeletedDuetoLIFDown.setStatus(_A)
_BWagNumCurrentL2tpv3TunnelsSpWiFi_Type=Unsigned32
_BWagNumCurrentL2tpv3TunnelsSpWiFi_Object=MibScalar
bWagNumCurrentL2tpv3TunnelsSpWiFi=_BWagNumCurrentL2tpv3TunnelsSpWiFi_Object((1,3,6,1,4,1,39406,2,1,3,7,26),_BWagNumCurrentL2tpv3TunnelsSpWiFi_Type())
bWagNumCurrentL2tpv3TunnelsSpWiFi.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentL2tpv3TunnelsSpWiFi.setStatus(_A)
_BWagNumCurrentTunnelsDSLite_Type=Unsigned32
_BWagNumCurrentTunnelsDSLite_Object=MibScalar
bWagNumCurrentTunnelsDSLite=_BWagNumCurrentTunnelsDSLite_Object((1,3,6,1,4,1,39406,2,1,3,7,27),_BWagNumCurrentTunnelsDSLite_Type())
bWagNumCurrentTunnelsDSLite.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagNumCurrentTunnelsDSLite.setStatus(_A)
_BWagTunnelNotifObjects_ObjectIdentity=ObjectIdentity
bWagTunnelNotifObjects=_BWagTunnelNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,8))
if mibBuilder.loadTexts:bWagTunnelNotifObjects.setStatus(_A)
_BWagCgnatMIBObjects_ObjectIdentity=ObjectIdentity
bWagCgnatMIBObjects=_BWagCgnatMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,9))
if mibBuilder.loadTexts:bWagCgnatMIBObjects.setStatus(_A)
_BWagCgnatProfileStatsTable_Object=MibTable
bWagCgnatProfileStatsTable=_BWagCgnatProfileStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,9,1))
if mibBuilder.loadTexts:bWagCgnatProfileStatsTable.setStatus(_A)
_BWagCgnatProfileStatsEntry_Object=MibTableRow
bWagCgnatProfileStatsEntry=_BWagCgnatProfileStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1))
bWagCgnatProfileStatsEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:bWagCgnatProfileStatsEntry.setStatus(_A)
_BWagCgnatProfileStatsIndex_Type=Integer32
_BWagCgnatProfileStatsIndex_Object=MibTableColumn
bWagCgnatProfileStatsIndex=_BWagCgnatProfileStatsIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,1),_BWagCgnatProfileStatsIndex_Type())
bWagCgnatProfileStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatProfileStatsIndex.setStatus(_A)
_BWagCgnatProfileName_Type=DisplayString
_BWagCgnatProfileName_Object=MibTableColumn
bWagCgnatProfileName=_BWagCgnatProfileName_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,2),_BWagCgnatProfileName_Type())
bWagCgnatProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileName.setStatus(_A)
_BWagCgnatProfileType_Type=DisplayString
_BWagCgnatProfileType_Object=MibTableColumn
bWagCgnatProfileType=_BWagCgnatProfileType_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,3),_BWagCgnatProfileType_Type())
bWagCgnatProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileType.setStatus(_A)
_BWagCgnatProfileNATIPPoolGroup_Type=DisplayString
_BWagCgnatProfileNATIPPoolGroup_Object=MibTableColumn
bWagCgnatProfileNATIPPoolGroup=_BWagCgnatProfileNATIPPoolGroup_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,4),_BWagCgnatProfileNATIPPoolGroup_Type())
bWagCgnatProfileNATIPPoolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileNATIPPoolGroup.setStatus(_A)
_BWagCgnatProfileSubscribers_Type=Unsigned32
_BWagCgnatProfileSubscribers_Object=MibTableColumn
bWagCgnatProfileSubscribers=_BWagCgnatProfileSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,5),_BWagCgnatProfileSubscribers_Type())
bWagCgnatProfileSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileSubscribers.setStatus(_A)
_BWagCgnatProfileMaxIPAddresses_Type=Unsigned32
_BWagCgnatProfileMaxIPAddresses_Object=MibTableColumn
bWagCgnatProfileMaxIPAddresses=_BWagCgnatProfileMaxIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,6),_BWagCgnatProfileMaxIPAddresses_Type())
bWagCgnatProfileMaxIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileMaxIPAddresses.setStatus(_A)
_BWagCgnatProfileUsedIPAddresses_Type=Unsigned32
_BWagCgnatProfileUsedIPAddresses_Object=MibTableColumn
bWagCgnatProfileUsedIPAddresses=_BWagCgnatProfileUsedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,7),_BWagCgnatProfileUsedIPAddresses_Type())
bWagCgnatProfileUsedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileUsedIPAddresses.setStatus(_A)
_BWagCgnatProfileReservedIPAddresses_Type=Unsigned32
_BWagCgnatProfileReservedIPAddresses_Object=MibTableColumn
bWagCgnatProfileReservedIPAddresses=_BWagCgnatProfileReservedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,8),_BWagCgnatProfileReservedIPAddresses_Type())
bWagCgnatProfileReservedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileReservedIPAddresses.setStatus(_A)
_BWagCgnatProfileTotalPortBlocks_Type=Unsigned32
_BWagCgnatProfileTotalPortBlocks_Object=MibTableColumn
bWagCgnatProfileTotalPortBlocks=_BWagCgnatProfileTotalPortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,9),_BWagCgnatProfileTotalPortBlocks_Type())
bWagCgnatProfileTotalPortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileTotalPortBlocks.setStatus(_A)
_BWagCgnatProfilePortBlocksUsed_Type=Unsigned32
_BWagCgnatProfilePortBlocksUsed_Object=MibTableColumn
bWagCgnatProfilePortBlocksUsed=_BWagCgnatProfilePortBlocksUsed_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,10),_BWagCgnatProfilePortBlocksUsed_Type())
bWagCgnatProfilePortBlocksUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfilePortBlocksUsed.setStatus(_C)
_BWagCgnatProfilePortBlocksReused_Type=Unsigned32
_BWagCgnatProfilePortBlocksReused_Object=MibTableColumn
bWagCgnatProfilePortBlocksReused=_BWagCgnatProfilePortBlocksReused_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,11),_BWagCgnatProfilePortBlocksReused_Type())
bWagCgnatProfilePortBlocksReused.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfilePortBlocksReused.setStatus(_C)
_BWagCgnatProfileTotalPoolIPAddresses_Type=Unsigned32
_BWagCgnatProfileTotalPoolIPAddresses_Object=MibTableColumn
bWagCgnatProfileTotalPoolIPAddresses=_BWagCgnatProfileTotalPoolIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,1,1,12),_BWagCgnatProfileTotalPoolIPAddresses_Type())
bWagCgnatProfileTotalPoolIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatProfileTotalPoolIPAddresses.setStatus(_A)
_BWagCgnatIPStatsTable_Object=MibTable
bWagCgnatIPStatsTable=_BWagCgnatIPStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,9,2))
if mibBuilder.loadTexts:bWagCgnatIPStatsTable.setStatus(_A)
_BWagCgnatIPStatsEntry_Object=MibTableRow
bWagCgnatIPStatsEntry=_BWagCgnatIPStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1))
bWagCgnatIPStatsEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:bWagCgnatIPStatsEntry.setStatus(_A)
_BWagCgnatIPStatsIndex_Type=Integer32
_BWagCgnatIPStatsIndex_Object=MibTableColumn
bWagCgnatIPStatsIndex=_BWagCgnatIPStatsIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,1),_BWagCgnatIPStatsIndex_Type())
bWagCgnatIPStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatIPStatsIndex.setStatus(_A)
_BWagCgnatPublicIPAddressType_Type=InetAddressType
_BWagCgnatPublicIPAddressType_Object=MibTableColumn
bWagCgnatPublicIPAddressType=_BWagCgnatPublicIPAddressType_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,2),_BWagCgnatPublicIPAddressType_Type())
bWagCgnatPublicIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPublicIPAddressType.setStatus(_A)
_BWagCgnatPublicIPAddress_Type=InetAddress
_BWagCgnatPublicIPAddress_Object=MibTableColumn
bWagCgnatPublicIPAddress=_BWagCgnatPublicIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,3),_BWagCgnatPublicIPAddress_Type())
bWagCgnatPublicIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPublicIPAddress.setStatus(_A)
_BWagCgnatIPPortBlocksUsed_Type=Unsigned32
_BWagCgnatIPPortBlocksUsed_Object=MibTableColumn
bWagCgnatIPPortBlocksUsed=_BWagCgnatIPPortBlocksUsed_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,4),_BWagCgnatIPPortBlocksUsed_Type())
bWagCgnatIPPortBlocksUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPPortBlocksUsed.setStatus(_C)
_BWagCgnatIPPortBlocksFree_Type=Unsigned32
_BWagCgnatIPPortBlocksFree_Object=MibTableColumn
bWagCgnatIPPortBlocksFree=_BWagCgnatIPPortBlocksFree_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,5),_BWagCgnatIPPortBlocksFree_Type())
bWagCgnatIPPortBlocksFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPPortBlocksFree.setStatus(_A)
_BWagCgnatIPPortBlocksReused_Type=Unsigned32
_BWagCgnatIPPortBlocksReused_Object=MibTableColumn
bWagCgnatIPPortBlocksReused=_BWagCgnatIPPortBlocksReused_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,6),_BWagCgnatIPPortBlocksReused_Type())
bWagCgnatIPPortBlocksReused.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPPortBlocksReused.setStatus(_C)
_BWagCgnatIPSubActiveCount_Type=Unsigned32
_BWagCgnatIPSubActiveCount_Object=MibTableColumn
bWagCgnatIPSubActiveCount=_BWagCgnatIPSubActiveCount_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,7),_BWagCgnatIPSubActiveCount_Type())
bWagCgnatIPSubActiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPSubActiveCount.setStatus(_A)
_BWagCgnatIPPacketsDropped_Type=Unsigned32
_BWagCgnatIPPacketsDropped_Object=MibTableColumn
bWagCgnatIPPacketsDropped=_BWagCgnatIPPacketsDropped_Object((1,3,6,1,4,1,39406,2,1,3,9,2,1,8),_BWagCgnatIPPacketsDropped_Type())
bWagCgnatIPPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPPacketsDropped.setStatus(_C)
_BWagCgnatPeriodIpTable_Object=MibTable
bWagCgnatPeriodIpTable=_BWagCgnatPeriodIpTable_Object((1,3,6,1,4,1,39406,2,1,3,9,3))
if mibBuilder.loadTexts:bWagCgnatPeriodIpTable.setStatus(_C)
_BWagCgnatPeriodIpEntry_Object=MibTableRow
bWagCgnatPeriodIpEntry=_BWagCgnatPeriodIpEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1))
bWagCgnatPeriodIpEntry.setIndexNames((0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:bWagCgnatPeriodIpEntry.setStatus(_C)
_BWagCgnatPeriodIpInterval_Type=Integer32
_BWagCgnatPeriodIpInterval_Object=MibTableColumn
bWagCgnatPeriodIpInterval=_BWagCgnatPeriodIpInterval_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,1),_BWagCgnatPeriodIpInterval_Type())
bWagCgnatPeriodIpInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatPeriodIpInterval.setStatus(_C)
_BWagCgnatPeriodIpIndex_Type=Integer32
_BWagCgnatPeriodIpIndex_Object=MibTableColumn
bWagCgnatPeriodIpIndex=_BWagCgnatPeriodIpIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,2),_BWagCgnatPeriodIpIndex_Type())
bWagCgnatPeriodIpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatPeriodIpIndex.setStatus(_C)
_BWagCgnatIPAddressType_Type=InetAddressType
_BWagCgnatIPAddressType_Object=MibTableColumn
bWagCgnatIPAddressType=_BWagCgnatIPAddressType_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,3),_BWagCgnatIPAddressType_Type())
bWagCgnatIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPAddressType.setStatus(_C)
_BWagCgnatIPAddress_Type=InetAddress
_BWagCgnatIPAddress_Object=MibTableColumn
bWagCgnatIPAddress=_BWagCgnatIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,4),_BWagCgnatIPAddress_Type())
bWagCgnatIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIPAddress.setStatus(_C)
_BWagCgnatPacketsDropped_Type=Unsigned32
_BWagCgnatPacketsDropped_Object=MibTableColumn
bWagCgnatPacketsDropped=_BWagCgnatPacketsDropped_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,5),_BWagCgnatPacketsDropped_Type())
bWagCgnatPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPacketsDropped.setStatus(_C)
_BWagCgnatPortBlockMaxUtil_Type=Unsigned32
_BWagCgnatPortBlockMaxUtil_Object=MibTableColumn
bWagCgnatPortBlockMaxUtil=_BWagCgnatPortBlockMaxUtil_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,6),_BWagCgnatPortBlockMaxUtil_Type())
bWagCgnatPortBlockMaxUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPortBlockMaxUtil.setStatus(_C)
_BWagCgnatPortBlockMinUtil_Type=Unsigned32
_BWagCgnatPortBlockMinUtil_Object=MibTableColumn
bWagCgnatPortBlockMinUtil=_BWagCgnatPortBlockMinUtil_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,7),_BWagCgnatPortBlockMinUtil_Type())
bWagCgnatPortBlockMinUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPortBlockMinUtil.setStatus(_C)
_BWagCgnatIntervalDuration_Type=Unsigned32
_BWagCgnatIntervalDuration_Object=MibTableColumn
bWagCgnatIntervalDuration=_BWagCgnatIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,9,3,1,8),_BWagCgnatIntervalDuration_Type())
bWagCgnatIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatIntervalDuration.setStatus(_C)
_BWagCgnatUnauthIPStatsTable_Object=MibTable
bWagCgnatUnauthIPStatsTable=_BWagCgnatUnauthIPStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,9,4))
if mibBuilder.loadTexts:bWagCgnatUnauthIPStatsTable.setStatus(_A)
_BWagCgnatUnauthIPStatsEntry_Object=MibTableRow
bWagCgnatUnauthIPStatsEntry=_BWagCgnatUnauthIPStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1))
bWagCgnatUnauthIPStatsEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:bWagCgnatUnauthIPStatsEntry.setStatus(_A)
_BWagCgnatUnauthIPStatsIndex_Type=Integer32
_BWagCgnatUnauthIPStatsIndex_Object=MibTableColumn
bWagCgnatUnauthIPStatsIndex=_BWagCgnatUnauthIPStatsIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,1),_BWagCgnatUnauthIPStatsIndex_Type())
bWagCgnatUnauthIPStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatUnauthIPStatsIndex.setStatus(_A)
_BWagCgnatUnauthPublicIPAddressType_Type=InetAddressType
_BWagCgnatUnauthPublicIPAddressType_Object=MibTableColumn
bWagCgnatUnauthPublicIPAddressType=_BWagCgnatUnauthPublicIPAddressType_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,2),_BWagCgnatUnauthPublicIPAddressType_Type())
bWagCgnatUnauthPublicIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthPublicIPAddressType.setStatus(_A)
_BWagCgnatUnauthPublicIPAddress_Type=InetAddress
_BWagCgnatUnauthPublicIPAddress_Object=MibTableColumn
bWagCgnatUnauthPublicIPAddress=_BWagCgnatUnauthPublicIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,3),_BWagCgnatUnauthPublicIPAddress_Type())
bWagCgnatUnauthPublicIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthPublicIPAddress.setStatus(_A)
_BWagCgnatUnauthIPPortBlocksUsed_Type=Unsigned32
_BWagCgnatUnauthIPPortBlocksUsed_Object=MibTableColumn
bWagCgnatUnauthIPPortBlocksUsed=_BWagCgnatUnauthIPPortBlocksUsed_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,4),_BWagCgnatUnauthIPPortBlocksUsed_Type())
bWagCgnatUnauthIPPortBlocksUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPPortBlocksUsed.setStatus(_C)
_BWagCgnatUnauthIPPortBlocksFree_Type=Unsigned32
_BWagCgnatUnauthIPPortBlocksFree_Object=MibTableColumn
bWagCgnatUnauthIPPortBlocksFree=_BWagCgnatUnauthIPPortBlocksFree_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,5),_BWagCgnatUnauthIPPortBlocksFree_Type())
bWagCgnatUnauthIPPortBlocksFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPPortBlocksFree.setStatus(_A)
_BWagCgnatUnauthIPPortBlocksReused_Type=Unsigned32
_BWagCgnatUnauthIPPortBlocksReused_Object=MibTableColumn
bWagCgnatUnauthIPPortBlocksReused=_BWagCgnatUnauthIPPortBlocksReused_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,6),_BWagCgnatUnauthIPPortBlocksReused_Type())
bWagCgnatUnauthIPPortBlocksReused.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPPortBlocksReused.setStatus(_C)
_BWagCgnatUnauthIPSubActiveCount_Type=Unsigned32
_BWagCgnatUnauthIPSubActiveCount_Object=MibTableColumn
bWagCgnatUnauthIPSubActiveCount=_BWagCgnatUnauthIPSubActiveCount_Object((1,3,6,1,4,1,39406,2,1,3,9,4,1,7),_BWagCgnatUnauthIPSubActiveCount_Type())
bWagCgnatUnauthIPSubActiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPSubActiveCount.setStatus(_A)
_BWagCgnatUnauthPeriodIpTable_Object=MibTable
bWagCgnatUnauthPeriodIpTable=_BWagCgnatUnauthPeriodIpTable_Object((1,3,6,1,4,1,39406,2,1,3,9,5))
if mibBuilder.loadTexts:bWagCgnatUnauthPeriodIpTable.setStatus(_C)
_BWagCgnatUnauthPeriodIpEntry_Object=MibTableRow
bWagCgnatUnauthPeriodIpEntry=_BWagCgnatUnauthPeriodIpEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1))
bWagCgnatUnauthPeriodIpEntry.setIndexNames((0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:bWagCgnatUnauthPeriodIpEntry.setStatus(_C)
_BWagCgnatUnauthPeriodIpInterval_Type=Integer32
_BWagCgnatUnauthPeriodIpInterval_Object=MibTableColumn
bWagCgnatUnauthPeriodIpInterval=_BWagCgnatUnauthPeriodIpInterval_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,1),_BWagCgnatUnauthPeriodIpInterval_Type())
bWagCgnatUnauthPeriodIpInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatUnauthPeriodIpInterval.setStatus(_C)
_BWagCgnatUnauthPeriodIpIndex_Type=Integer32
_BWagCgnatUnauthPeriodIpIndex_Object=MibTableColumn
bWagCgnatUnauthPeriodIpIndex=_BWagCgnatUnauthPeriodIpIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,2),_BWagCgnatUnauthPeriodIpIndex_Type())
bWagCgnatUnauthPeriodIpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatUnauthPeriodIpIndex.setStatus(_C)
_BWagCgnatUnauthIPAddressType_Type=InetAddressType
_BWagCgnatUnauthIPAddressType_Object=MibTableColumn
bWagCgnatUnauthIPAddressType=_BWagCgnatUnauthIPAddressType_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,3),_BWagCgnatUnauthIPAddressType_Type())
bWagCgnatUnauthIPAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPAddressType.setStatus(_C)
_BWagCgnatUnauthIPAddress_Type=InetAddress
_BWagCgnatUnauthIPAddress_Object=MibTableColumn
bWagCgnatUnauthIPAddress=_BWagCgnatUnauthIPAddress_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,4),_BWagCgnatUnauthIPAddress_Type())
bWagCgnatUnauthIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIPAddress.setStatus(_C)
_BWagCgnatUnauthPortBlockMaxUtil_Type=Unsigned32
_BWagCgnatUnauthPortBlockMaxUtil_Object=MibTableColumn
bWagCgnatUnauthPortBlockMaxUtil=_BWagCgnatUnauthPortBlockMaxUtil_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,5),_BWagCgnatUnauthPortBlockMaxUtil_Type())
bWagCgnatUnauthPortBlockMaxUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthPortBlockMaxUtil.setStatus(_C)
_BWagCgnatUnauthPortBlockMinUtil_Type=Unsigned32
_BWagCgnatUnauthPortBlockMinUtil_Object=MibTableColumn
bWagCgnatUnauthPortBlockMinUtil=_BWagCgnatUnauthPortBlockMinUtil_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,6),_BWagCgnatUnauthPortBlockMinUtil_Type())
bWagCgnatUnauthPortBlockMinUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthPortBlockMinUtil.setStatus(_C)
_BWagCgnatUnauthIntervalDuration_Type=Unsigned32
_BWagCgnatUnauthIntervalDuration_Object=MibTableColumn
bWagCgnatUnauthIntervalDuration=_BWagCgnatUnauthIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,9,5,1,7),_BWagCgnatUnauthIntervalDuration_Type())
bWagCgnatUnauthIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatUnauthIntervalDuration.setStatus(_C)
_BWagCgnatAuthPortUtilTable_Object=MibTable
bWagCgnatAuthPortUtilTable=_BWagCgnatAuthPortUtilTable_Object((1,3,6,1,4,1,39406,2,1,3,9,6))
if mibBuilder.loadTexts:bWagCgnatAuthPortUtilTable.setStatus(_C)
_BWagCgnatAuthPortUtilEntry_Object=MibTableRow
bWagCgnatAuthPortUtilEntry=_BWagCgnatAuthPortUtilEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,6,1))
bWagCgnatAuthPortUtilEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:bWagCgnatAuthPortUtilEntry.setStatus(_C)
_BWagCgnatAuthSubscriberMac_Type=MacAddress
_BWagCgnatAuthSubscriberMac_Object=MibTableColumn
bWagCgnatAuthSubscriberMac=_BWagCgnatAuthSubscriberMac_Object((1,3,6,1,4,1,39406,2,1,3,9,6,1,1),_BWagCgnatAuthSubscriberMac_Type())
bWagCgnatAuthSubscriberMac.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatAuthSubscriberMac.setStatus(_C)
_BWagCgnatAuthSubscriberPortsUtil_Type=Unsigned32
_BWagCgnatAuthSubscriberPortsUtil_Object=MibTableColumn
bWagCgnatAuthSubscriberPortsUtil=_BWagCgnatAuthSubscriberPortsUtil_Object((1,3,6,1,4,1,39406,2,1,3,9,6,1,2),_BWagCgnatAuthSubscriberPortsUtil_Type())
bWagCgnatAuthSubscriberPortsUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatAuthSubscriberPortsUtil.setStatus(_C)
_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Type=Unsigned32
_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Object=MibScalar
bWagCgnatAuthPortRisingThresholdCrossedSubCount=_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Object((1,3,6,1,4,1,39406,2,1,3,9,7),_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Type())
bWagCgnatAuthPortRisingThresholdCrossedSubCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatAuthPortRisingThresholdCrossedSubCount.setStatus(_C)
_BWagCgnatPoolGroupStatsTable_Object=MibTable
bWagCgnatPoolGroupStatsTable=_BWagCgnatPoolGroupStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,9,8))
if mibBuilder.loadTexts:bWagCgnatPoolGroupStatsTable.setStatus(_A)
_BWagCgnatPoolGroupStatsEntry_Object=MibTableRow
bWagCgnatPoolGroupStatsEntry=_BWagCgnatPoolGroupStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1))
bWagCgnatPoolGroupStatsEntry.setIndexNames((0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:bWagCgnatPoolGroupStatsEntry.setStatus(_A)
class _BWagCgnatPoolGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('unAuthNapt',1),('authNapt',2)))
_BWagCgnatPoolGroupType_Type.__name__=_K
_BWagCgnatPoolGroupType_Object=MibTableColumn
bWagCgnatPoolGroupType=_BWagCgnatPoolGroupType_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,1),_BWagCgnatPoolGroupType_Type())
bWagCgnatPoolGroupType.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatPoolGroupType.setStatus(_A)
_BWagCgnatPoolGroupIndex_Type=Unsigned32
_BWagCgnatPoolGroupIndex_Object=MibTableColumn
bWagCgnatPoolGroupIndex=_BWagCgnatPoolGroupIndex_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,2),_BWagCgnatPoolGroupIndex_Type())
bWagCgnatPoolGroupIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagCgnatPoolGroupIndex.setStatus(_A)
class _BWagCgnatPoolGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BWagCgnatPoolGroupName_Type.__name__=_O
_BWagCgnatPoolGroupName_Object=MibTableColumn
bWagCgnatPoolGroupName=_BWagCgnatPoolGroupName_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,3),_BWagCgnatPoolGroupName_Type())
bWagCgnatPoolGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPoolGroupName.setStatus(_A)
_BWagCgnatPoolGroupSubscribers_Type=Unsigned32
_BWagCgnatPoolGroupSubscribers_Object=MibTableColumn
bWagCgnatPoolGroupSubscribers=_BWagCgnatPoolGroupSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,4),_BWagCgnatPoolGroupSubscribers_Type())
bWagCgnatPoolGroupSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPoolGroupSubscribers.setStatus(_A)
_BWagCgnatPoolGroupUsedIPAddresses_Type=Unsigned32
_BWagCgnatPoolGroupUsedIPAddresses_Object=MibTableColumn
bWagCgnatPoolGroupUsedIPAddresses=_BWagCgnatPoolGroupUsedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,5),_BWagCgnatPoolGroupUsedIPAddresses_Type())
bWagCgnatPoolGroupUsedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPoolGroupUsedIPAddresses.setStatus(_A)
_BWagCgnatPoolGroupReservedIPAddresses_Type=Unsigned32
_BWagCgnatPoolGroupReservedIPAddresses_Object=MibTableColumn
bWagCgnatPoolGroupReservedIPAddresses=_BWagCgnatPoolGroupReservedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,6),_BWagCgnatPoolGroupReservedIPAddresses_Type())
bWagCgnatPoolGroupReservedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPoolGroupReservedIPAddresses.setStatus(_A)
_BWagCgnatPoolGroupTotalIPAddresses_Type=Unsigned32
_BWagCgnatPoolGroupTotalIPAddresses_Object=MibTableColumn
bWagCgnatPoolGroupTotalIPAddresses=_BWagCgnatPoolGroupTotalIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,9,8,1,7),_BWagCgnatPoolGroupTotalIPAddresses_Type())
bWagCgnatPoolGroupTotalIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagCgnatPoolGroupTotalIPAddresses.setStatus(_A)
_BWagCgnatNotifObjects_ObjectIdentity=ObjectIdentity
bWagCgnatNotifObjects=_BWagCgnatNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,10))
if mibBuilder.loadTexts:bWagCgnatNotifObjects.setStatus(_A)
_BWagCgnatProfileIPPoolGroup_Type=DisplayString
_BWagCgnatProfileIPPoolGroup_Object=MibScalar
bWagCgnatProfileIPPoolGroup=_BWagCgnatProfileIPPoolGroup_Object((1,3,6,1,4,1,39406,2,1,3,10,1),_BWagCgnatProfileIPPoolGroup_Type())
bWagCgnatProfileIPPoolGroup.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatProfileIPPoolGroup.setStatus(_A)
_BWagCgnatTotalPoolIPAddresses_Type=Unsigned32
_BWagCgnatTotalPoolIPAddresses_Object=MibScalar
bWagCgnatTotalPoolIPAddresses=_BWagCgnatTotalPoolIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,10,2),_BWagCgnatTotalPoolIPAddresses_Type())
bWagCgnatTotalPoolIPAddresses.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatTotalPoolIPAddresses.setStatus(_A)
_BWagCgnatAuthIpAddrUsedHighThreshold_Type=Unsigned32
_BWagCgnatAuthIpAddrUsedHighThreshold_Object=MibScalar
bWagCgnatAuthIpAddrUsedHighThreshold=_BWagCgnatAuthIpAddrUsedHighThreshold_Object((1,3,6,1,4,1,39406,2,1,3,10,3),_BWagCgnatAuthIpAddrUsedHighThreshold_Type())
bWagCgnatAuthIpAddrUsedHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatAuthIpAddrUsedHighThreshold.setStatus(_A)
_BWagCgnatAuthIpAddrUsedLowThreshold_Type=Unsigned32
_BWagCgnatAuthIpAddrUsedLowThreshold_Object=MibScalar
bWagCgnatAuthIpAddrUsedLowThreshold=_BWagCgnatAuthIpAddrUsedLowThreshold_Object((1,3,6,1,4,1,39406,2,1,3,10,4),_BWagCgnatAuthIpAddrUsedLowThreshold_Type())
bWagCgnatAuthIpAddrUsedLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatAuthIpAddrUsedLowThreshold.setStatus(_A)
_BWagCgnatSubscriberMac_Type=MacAddress
_BWagCgnatSubscriberMac_Object=MibScalar
bWagCgnatSubscriberMac=_BWagCgnatSubscriberMac_Object((1,3,6,1,4,1,39406,2,1,3,10,5),_BWagCgnatSubscriberMac_Type())
bWagCgnatSubscriberMac.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatSubscriberMac.setStatus(_C)
_BWagCgnatTotalPortBlocksPerSubscriber_Type=Unsigned32
_BWagCgnatTotalPortBlocksPerSubscriber_Object=MibScalar
bWagCgnatTotalPortBlocksPerSubscriber=_BWagCgnatTotalPortBlocksPerSubscriber_Object((1,3,6,1,4,1,39406,2,1,3,10,6),_BWagCgnatTotalPortBlocksPerSubscriber_Type())
bWagCgnatTotalPortBlocksPerSubscriber.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatTotalPortBlocksPerSubscriber.setStatus(_C)
_BWagCgnatPortBlocksUsedHighThreshold_Type=Unsigned32
_BWagCgnatPortBlocksUsedHighThreshold_Object=MibScalar
bWagCgnatPortBlocksUsedHighThreshold=_BWagCgnatPortBlocksUsedHighThreshold_Object((1,3,6,1,4,1,39406,2,1,3,10,7),_BWagCgnatPortBlocksUsedHighThreshold_Type())
bWagCgnatPortBlocksUsedHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatPortBlocksUsedHighThreshold.setStatus(_C)
_BWagCgnatPortBlocksUsedLowThreshold_Type=Unsigned32
_BWagCgnatPortBlocksUsedLowThreshold_Object=MibScalar
bWagCgnatPortBlocksUsedLowThreshold=_BWagCgnatPortBlocksUsedLowThreshold_Object((1,3,6,1,4,1,39406,2,1,3,10,8),_BWagCgnatPortBlocksUsedLowThreshold_Type())
bWagCgnatPortBlocksUsedLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagCgnatPortBlocksUsedLowThreshold.setStatus(_C)
_BWagProcessingLatencyMIBObjects_ObjectIdentity=ObjectIdentity
bWagProcessingLatencyMIBObjects=_BWagProcessingLatencyMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,11))
if mibBuilder.loadTexts:bWagProcessingLatencyMIBObjects.setStatus(_A)
_BWagUpstreamProcessingLatencyPktCount_Type=Unsigned32
_BWagUpstreamProcessingLatencyPktCount_Object=MibScalar
bWagUpstreamProcessingLatencyPktCount=_BWagUpstreamProcessingLatencyPktCount_Object((1,3,6,1,4,1,39406,2,1,3,11,1),_BWagUpstreamProcessingLatencyPktCount_Type())
bWagUpstreamProcessingLatencyPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagUpstreamProcessingLatencyPktCount.setStatus(_C)
_BWagUpstreamProcessingLatencyMax_Type=Unsigned32
_BWagUpstreamProcessingLatencyMax_Object=MibScalar
bWagUpstreamProcessingLatencyMax=_BWagUpstreamProcessingLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,11,2),_BWagUpstreamProcessingLatencyMax_Type())
bWagUpstreamProcessingLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagUpstreamProcessingLatencyMax.setStatus(_C)
_BWagUpstreamProcessingLatencyMin_Type=Unsigned32
_BWagUpstreamProcessingLatencyMin_Object=MibScalar
bWagUpstreamProcessingLatencyMin=_BWagUpstreamProcessingLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,11,3),_BWagUpstreamProcessingLatencyMin_Type())
bWagUpstreamProcessingLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagUpstreamProcessingLatencyMin.setStatus(_C)
_BWagUpstreamProcessingLatencyAvg_Type=Unsigned32
_BWagUpstreamProcessingLatencyAvg_Object=MibScalar
bWagUpstreamProcessingLatencyAvg=_BWagUpstreamProcessingLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,11,4),_BWagUpstreamProcessingLatencyAvg_Type())
bWagUpstreamProcessingLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagUpstreamProcessingLatencyAvg.setStatus(_C)
_BWagDownstreamProcessingLatencyPktCount_Type=Unsigned32
_BWagDownstreamProcessingLatencyPktCount_Object=MibScalar
bWagDownstreamProcessingLatencyPktCount=_BWagDownstreamProcessingLatencyPktCount_Object((1,3,6,1,4,1,39406,2,1,3,11,5),_BWagDownstreamProcessingLatencyPktCount_Type())
bWagDownstreamProcessingLatencyPktCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDownstreamProcessingLatencyPktCount.setStatus(_C)
_BWagDownstreamProcessingLatencyMax_Type=Unsigned32
_BWagDownstreamProcessingLatencyMax_Object=MibScalar
bWagDownstreamProcessingLatencyMax=_BWagDownstreamProcessingLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,11,6),_BWagDownstreamProcessingLatencyMax_Type())
bWagDownstreamProcessingLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDownstreamProcessingLatencyMax.setStatus(_C)
_BWagDownstreamProcessingLatencyMin_Type=Unsigned32
_BWagDownstreamProcessingLatencyMin_Object=MibScalar
bWagDownstreamProcessingLatencyMin=_BWagDownstreamProcessingLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,11,7),_BWagDownstreamProcessingLatencyMin_Type())
bWagDownstreamProcessingLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDownstreamProcessingLatencyMin.setStatus(_C)
_BWagDownstreamProcessingLatencyAvg_Type=Unsigned32
_BWagDownstreamProcessingLatencyAvg_Object=MibScalar
bWagDownstreamProcessingLatencyAvg=_BWagDownstreamProcessingLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,11,8),_BWagDownstreamProcessingLatencyAvg_Type())
bWagDownstreamProcessingLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDownstreamProcessingLatencyAvg.setStatus(_C)
_BWagProcessingLatencyNotifObjects_ObjectIdentity=ObjectIdentity
bWagProcessingLatencyNotifObjects=_BWagProcessingLatencyNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,12))
if mibBuilder.loadTexts:bWagProcessingLatencyNotifObjects.setStatus(_A)
_BWagDhcpv6MIBObjects_ObjectIdentity=ObjectIdentity
bWagDhcpv6MIBObjects=_BWagDhcpv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,13))
if mibBuilder.loadTexts:bWagDhcpv6MIBObjects.setStatus(_A)
_BWagDHCPv6Table_Object=MibTable
bWagDHCPv6Table=_BWagDHCPv6Table_Object((1,3,6,1,4,1,39406,2,1,3,13,1))
if mibBuilder.loadTexts:bWagDHCPv6Table.setStatus(_A)
_BWagDHCPv6Entry_Object=MibTableRow
bWagDHCPv6Entry=_BWagDHCPv6Entry_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1))
bWagDHCPv6Entry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:bWagDHCPv6Entry.setStatus(_A)
_BWagDHCPv6StatsInterval_Type=Integer32
_BWagDHCPv6StatsInterval_Object=MibTableColumn
bWagDHCPv6StatsInterval=_BWagDHCPv6StatsInterval_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,1),_BWagDHCPv6StatsInterval_Type())
bWagDHCPv6StatsInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagDHCPv6StatsInterval.setStatus(_A)
_BWagDHCPv6IntervalDuration_Type=Integer32
_BWagDHCPv6IntervalDuration_Object=MibTableColumn
bWagDHCPv6IntervalDuration=_BWagDHCPv6IntervalDuration_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,2),_BWagDHCPv6IntervalDuration_Type())
bWagDHCPv6IntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6IntervalDuration.setStatus(_A)
_BWagDHCPv6SolicitReplyIntervalMin_Type=Unsigned32
_BWagDHCPv6SolicitReplyIntervalMin_Object=MibTableColumn
bWagDHCPv6SolicitReplyIntervalMin=_BWagDHCPv6SolicitReplyIntervalMin_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,3),_BWagDHCPv6SolicitReplyIntervalMin_Type())
bWagDHCPv6SolicitReplyIntervalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitReplyIntervalMin.setStatus(_A)
_BWagDHCPv6SolicitReplyIntervalMax_Type=Unsigned32
_BWagDHCPv6SolicitReplyIntervalMax_Object=MibTableColumn
bWagDHCPv6SolicitReplyIntervalMax=_BWagDHCPv6SolicitReplyIntervalMax_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,4),_BWagDHCPv6SolicitReplyIntervalMax_Type())
bWagDHCPv6SolicitReplyIntervalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitReplyIntervalMax.setStatus(_A)
_BWagDHCPv6SolicitReplyIntervalAvg_Type=Unsigned32
_BWagDHCPv6SolicitReplyIntervalAvg_Object=MibTableColumn
bWagDHCPv6SolicitReplyIntervalAvg=_BWagDHCPv6SolicitReplyIntervalAvg_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,5),_BWagDHCPv6SolicitReplyIntervalAvg_Type())
bWagDHCPv6SolicitReplyIntervalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitReplyIntervalAvg.setStatus(_A)
_BWagDHCPv6SolicitReplyIntervalLast_Type=Unsigned32
_BWagDHCPv6SolicitReplyIntervalLast_Object=MibTableColumn
bWagDHCPv6SolicitReplyIntervalLast=_BWagDHCPv6SolicitReplyIntervalLast_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,6),_BWagDHCPv6SolicitReplyIntervalLast_Type())
bWagDHCPv6SolicitReplyIntervalLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitReplyIntervalLast.setStatus(_A)
_BWagDHCPv6RequestReplyLatencyMin_Type=Unsigned32
_BWagDHCPv6RequestReplyLatencyMin_Object=MibTableColumn
bWagDHCPv6RequestReplyLatencyMin=_BWagDHCPv6RequestReplyLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,7),_BWagDHCPv6RequestReplyLatencyMin_Type())
bWagDHCPv6RequestReplyLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6RequestReplyLatencyMin.setStatus(_A)
_BWagDHCPv6RequestReplyLatencyMax_Type=Unsigned32
_BWagDHCPv6RequestReplyLatencyMax_Object=MibTableColumn
bWagDHCPv6RequestReplyLatencyMax=_BWagDHCPv6RequestReplyLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,8),_BWagDHCPv6RequestReplyLatencyMax_Type())
bWagDHCPv6RequestReplyLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6RequestReplyLatencyMax.setStatus(_A)
_BWagDHCPv6RequestReplyLatencyAvg_Type=Unsigned32
_BWagDHCPv6RequestReplyLatencyAvg_Object=MibTableColumn
bWagDHCPv6RequestReplyLatencyAvg=_BWagDHCPv6RequestReplyLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,9),_BWagDHCPv6RequestReplyLatencyAvg_Type())
bWagDHCPv6RequestReplyLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6RequestReplyLatencyAvg.setStatus(_A)
_BWagDHCPv6RequestReplyLatencyLast_Type=Unsigned32
_BWagDHCPv6RequestReplyLatencyLast_Object=MibTableColumn
bWagDHCPv6RequestReplyLatencyLast=_BWagDHCPv6RequestReplyLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,10),_BWagDHCPv6RequestReplyLatencyLast_Type())
bWagDHCPv6RequestReplyLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6RequestReplyLatencyLast.setStatus(_A)
_BWagDHCPv6SolicitAdvLatencyMin_Type=Unsigned32
_BWagDHCPv6SolicitAdvLatencyMin_Object=MibTableColumn
bWagDHCPv6SolicitAdvLatencyMin=_BWagDHCPv6SolicitAdvLatencyMin_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,11),_BWagDHCPv6SolicitAdvLatencyMin_Type())
bWagDHCPv6SolicitAdvLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitAdvLatencyMin.setStatus(_A)
_BWagDHCPv6SolicitAdvLatencyMax_Type=Unsigned32
_BWagDHCPv6SolicitAdvLatencyMax_Object=MibTableColumn
bWagDHCPv6SolicitAdvLatencyMax=_BWagDHCPv6SolicitAdvLatencyMax_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,12),_BWagDHCPv6SolicitAdvLatencyMax_Type())
bWagDHCPv6SolicitAdvLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitAdvLatencyMax.setStatus(_A)
_BWagDHCPv6SolicitAdvLatencyAvg_Type=Unsigned32
_BWagDHCPv6SolicitAdvLatencyAvg_Object=MibTableColumn
bWagDHCPv6SolicitAdvLatencyAvg=_BWagDHCPv6SolicitAdvLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,13),_BWagDHCPv6SolicitAdvLatencyAvg_Type())
bWagDHCPv6SolicitAdvLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitAdvLatencyAvg.setStatus(_A)
_BWagDHCPv6SolicitAdvLatencyLast_Type=Unsigned32
_BWagDHCPv6SolicitAdvLatencyLast_Object=MibTableColumn
bWagDHCPv6SolicitAdvLatencyLast=_BWagDHCPv6SolicitAdvLatencyLast_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,14),_BWagDHCPv6SolicitAdvLatencyLast_Type())
bWagDHCPv6SolicitAdvLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitAdvLatencyLast.setStatus(_A)
_BWagDHCPv6AdvRequestIntervalMin_Type=Unsigned32
_BWagDHCPv6AdvRequestIntervalMin_Object=MibTableColumn
bWagDHCPv6AdvRequestIntervalMin=_BWagDHCPv6AdvRequestIntervalMin_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,15),_BWagDHCPv6AdvRequestIntervalMin_Type())
bWagDHCPv6AdvRequestIntervalMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6AdvRequestIntervalMin.setStatus(_A)
_BWagDHCPv6AdvRequestIntervalMax_Type=Unsigned32
_BWagDHCPv6AdvRequestIntervalMax_Object=MibTableColumn
bWagDHCPv6AdvRequestIntervalMax=_BWagDHCPv6AdvRequestIntervalMax_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,16),_BWagDHCPv6AdvRequestIntervalMax_Type())
bWagDHCPv6AdvRequestIntervalMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6AdvRequestIntervalMax.setStatus(_A)
_BWagDHCPv6AdvRequestIntervalAvg_Type=Unsigned32
_BWagDHCPv6AdvRequestIntervalAvg_Object=MibTableColumn
bWagDHCPv6AdvRequestIntervalAvg=_BWagDHCPv6AdvRequestIntervalAvg_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,17),_BWagDHCPv6AdvRequestIntervalAvg_Type())
bWagDHCPv6AdvRequestIntervalAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6AdvRequestIntervalAvg.setStatus(_A)
_BWagDHCPv6AdvRequestIntervalLast_Type=Unsigned32
_BWagDHCPv6AdvRequestIntervalLast_Object=MibTableColumn
bWagDHCPv6AdvRequestIntervalLast=_BWagDHCPv6AdvRequestIntervalLast_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,18),_BWagDHCPv6AdvRequestIntervalLast_Type())
bWagDHCPv6AdvRequestIntervalLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6AdvRequestIntervalLast.setStatus(_A)
_BWagDHCPv6SolicitReceived_Type=Unsigned32
_BWagDHCPv6SolicitReceived_Object=MibTableColumn
bWagDHCPv6SolicitReceived=_BWagDHCPv6SolicitReceived_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,19),_BWagDHCPv6SolicitReceived_Type())
bWagDHCPv6SolicitReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6SolicitReceived.setStatus(_A)
_BWagDHCPv6AdvertisementSent_Type=Unsigned32
_BWagDHCPv6AdvertisementSent_Object=MibTableColumn
bWagDHCPv6AdvertisementSent=_BWagDHCPv6AdvertisementSent_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,20),_BWagDHCPv6AdvertisementSent_Type())
bWagDHCPv6AdvertisementSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6AdvertisementSent.setStatus(_A)
_BWagDHCPv6RequestReceived_Type=Unsigned32
_BWagDHCPv6RequestReceived_Object=MibTableColumn
bWagDHCPv6RequestReceived=_BWagDHCPv6RequestReceived_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,21),_BWagDHCPv6RequestReceived_Type())
bWagDHCPv6RequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6RequestReceived.setStatus(_A)
_BWagDHCPv6ReplySent_Type=Unsigned32
_BWagDHCPv6ReplySent_Object=MibTableColumn
bWagDHCPv6ReplySent=_BWagDHCPv6ReplySent_Object((1,3,6,1,4,1,39406,2,1,3,13,1,1,22),_BWagDHCPv6ReplySent_Type())
bWagDHCPv6ReplySent.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDHCPv6ReplySent.setStatus(_A)
_BWagMHNMIBObjects_ObjectIdentity=ObjectIdentity
bWagMHNMIBObjects=_BWagMHNMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,14))
if mibBuilder.loadTexts:bWagMHNMIBObjects.setStatus(_A)
_BWagMHNProfileStatsTable_Object=MibTable
bWagMHNProfileStatsTable=_BWagMHNProfileStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,14,1))
if mibBuilder.loadTexts:bWagMHNProfileStatsTable.setStatus(_A)
_BWagMHNProfileStatsEntry_Object=MibTableRow
bWagMHNProfileStatsEntry=_BWagMHNProfileStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1))
bWagMHNProfileStatsEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:bWagMHNProfileStatsEntry.setStatus(_A)
_BWagMHNProfileStatsIndex_Type=Integer32
_BWagMHNProfileStatsIndex_Object=MibTableColumn
bWagMHNProfileStatsIndex=_BWagMHNProfileStatsIndex_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,1),_BWagMHNProfileStatsIndex_Type())
bWagMHNProfileStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagMHNProfileStatsIndex.setStatus(_A)
_BWagMHNProfileName_Type=DisplayString
_BWagMHNProfileName_Object=MibTableColumn
bWagMHNProfileName=_BWagMHNProfileName_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,2),_BWagMHNProfileName_Type())
bWagMHNProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileName.setStatus(_A)
_BWagMHNProfileNATIPPoolGroup_Type=DisplayString
_BWagMHNProfileNATIPPoolGroup_Object=MibTableColumn
bWagMHNProfileNATIPPoolGroup=_BWagMHNProfileNATIPPoolGroup_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,3),_BWagMHNProfileNATIPPoolGroup_Type())
bWagMHNProfileNATIPPoolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileNATIPPoolGroup.setStatus(_A)
_BWagMHNProfileMaxSubscribers_Type=Unsigned32
_BWagMHNProfileMaxSubscribers_Object=MibTableColumn
bWagMHNProfileMaxSubscribers=_BWagMHNProfileMaxSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,4),_BWagMHNProfileMaxSubscribers_Type())
bWagMHNProfileMaxSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileMaxSubscribers.setStatus(_A)
_BWagMHNProfileMaxIPAddresses_Type=Unsigned32
_BWagMHNProfileMaxIPAddresses_Object=MibTableColumn
bWagMHNProfileMaxIPAddresses=_BWagMHNProfileMaxIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,5),_BWagMHNProfileMaxIPAddresses_Type())
bWagMHNProfileMaxIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileMaxIPAddresses.setStatus(_A)
_BWagMHNProfileUsedIPAddresses_Type=Unsigned32
_BWagMHNProfileUsedIPAddresses_Object=MibTableColumn
bWagMHNProfileUsedIPAddresses=_BWagMHNProfileUsedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,6),_BWagMHNProfileUsedIPAddresses_Type())
bWagMHNProfileUsedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileUsedIPAddresses.setStatus(_A)
_BWagMHNProfileTotalPortBlocks_Type=Unsigned32
_BWagMHNProfileTotalPortBlocks_Object=MibTableColumn
bWagMHNProfileTotalPortBlocks=_BWagMHNProfileTotalPortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,7),_BWagMHNProfileTotalPortBlocks_Type())
bWagMHNProfileTotalPortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileTotalPortBlocks.setStatus(_A)
_BWagMHNProfileTotalPoolIPAddresses_Type=Unsigned32
_BWagMHNProfileTotalPoolIPAddresses_Object=MibTableColumn
bWagMHNProfileTotalPoolIPAddresses=_BWagMHNProfileTotalPoolIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,14,1,1,8),_BWagMHNProfileTotalPoolIPAddresses_Type())
bWagMHNProfileTotalPoolIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagMHNProfileTotalPoolIPAddresses.setStatus(_A)
_BWagVrgApiNotifObjects_ObjectIdentity=ObjectIdentity
bWagVrgApiNotifObjects=_BWagVrgApiNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,15))
if mibBuilder.loadTexts:bWagVrgApiNotifObjects.setStatus(_A)
_BWagVrgApiIpAddrUsedHighThreshold_Type=Unsigned32
_BWagVrgApiIpAddrUsedHighThreshold_Object=MibScalar
bWagVrgApiIpAddrUsedHighThreshold=_BWagVrgApiIpAddrUsedHighThreshold_Object((1,3,6,1,4,1,39406,2,1,3,15,1),_BWagVrgApiIpAddrUsedHighThreshold_Type())
bWagVrgApiIpAddrUsedHighThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagVrgApiIpAddrUsedHighThreshold.setStatus(_A)
_BWagVrgApiIpAddrUsedLowThreshold_Type=Unsigned32
_BWagVrgApiIpAddrUsedLowThreshold_Object=MibScalar
bWagVrgApiIpAddrUsedLowThreshold=_BWagVrgApiIpAddrUsedLowThreshold_Object((1,3,6,1,4,1,39406,2,1,3,15,2),_BWagVrgApiIpAddrUsedLowThreshold_Type())
bWagVrgApiIpAddrUsedLowThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagVrgApiIpAddrUsedLowThreshold.setStatus(_A)
_BWagrgApiIPPoolGroup_Type=DisplayString
_BWagrgApiIPPoolGroup_Object=MibScalar
bWagrgApiIPPoolGroup=_BWagrgApiIPPoolGroup_Object((1,3,6,1,4,1,39406,2,1,3,15,3),_BWagrgApiIPPoolGroup_Type())
bWagrgApiIPPoolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagrgApiIPPoolGroup.setStatus(_A)
_BWagVRGApiIPoolIPAddresses_Type=Unsigned32
_BWagVRGApiIPoolIPAddresses_Object=MibScalar
bWagVRGApiIPoolIPAddresses=_BWagVRGApiIPoolIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,15,4),_BWagVRGApiIPoolIPAddresses_Type())
bWagVRGApiIPoolIPAddresses.setMaxAccess(_F)
if mibBuilder.loadTexts:bWagVRGApiIPoolIPAddresses.setStatus(_A)
_BWagDsLiteMIBObjects_ObjectIdentity=ObjectIdentity
bWagDsLiteMIBObjects=_BWagDsLiteMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,16))
if mibBuilder.loadTexts:bWagDsLiteMIBObjects.setStatus(_A)
_BWagDsLiteProfileStatsTable_Object=MibTable
bWagDsLiteProfileStatsTable=_BWagDsLiteProfileStatsTable_Object((1,3,6,1,4,1,39406,2,1,3,16,1))
if mibBuilder.loadTexts:bWagDsLiteProfileStatsTable.setStatus(_A)
_BWagDsLiteProfileStatsEntry_Object=MibTableRow
bWagDsLiteProfileStatsEntry=_BWagDsLiteProfileStatsEntry_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1))
bWagDsLiteProfileStatsEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:bWagDsLiteProfileStatsEntry.setStatus(_A)
_BWagDsLiteProfileStatsIndex_Type=Integer32
_BWagDsLiteProfileStatsIndex_Object=MibTableColumn
bWagDsLiteProfileStatsIndex=_BWagDsLiteProfileStatsIndex_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,1),_BWagDsLiteProfileStatsIndex_Type())
bWagDsLiteProfileStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bWagDsLiteProfileStatsIndex.setStatus(_A)
_BWagDsLiteProfileName_Type=DisplayString
_BWagDsLiteProfileName_Object=MibTableColumn
bWagDsLiteProfileName=_BWagDsLiteProfileName_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,2),_BWagDsLiteProfileName_Type())
bWagDsLiteProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileName.setStatus(_A)
_BWagDsLiteProfileType_Type=DisplayString
_BWagDsLiteProfileType_Object=MibTableColumn
bWagDsLiteProfileType=_BWagDsLiteProfileType_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,3),_BWagDsLiteProfileType_Type())
bWagDsLiteProfileType.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileType.setStatus(_A)
_BWagDsLiteProfileNATIPPoolGroup_Type=DisplayString
_BWagDsLiteProfileNATIPPoolGroup_Object=MibTableColumn
bWagDsLiteProfileNATIPPoolGroup=_BWagDsLiteProfileNATIPPoolGroup_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,4),_BWagDsLiteProfileNATIPPoolGroup_Type())
bWagDsLiteProfileNATIPPoolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileNATIPPoolGroup.setStatus(_A)
_BWagDsLiteProfileMaxIPAddresses_Type=Unsigned32
_BWagDsLiteProfileMaxIPAddresses_Object=MibTableColumn
bWagDsLiteProfileMaxIPAddresses=_BWagDsLiteProfileMaxIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,5),_BWagDsLiteProfileMaxIPAddresses_Type())
bWagDsLiteProfileMaxIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileMaxIPAddresses.setStatus(_A)
_BWagDsLiteProfileUsedIPAddresses_Type=Unsigned32
_BWagDsLiteProfileUsedIPAddresses_Object=MibTableColumn
bWagDsLiteProfileUsedIPAddresses=_BWagDsLiteProfileUsedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,6),_BWagDsLiteProfileUsedIPAddresses_Type())
bWagDsLiteProfileUsedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileUsedIPAddresses.setStatus(_A)
_BWagDsLiteProfileReservedIPAddresses_Type=Unsigned32
_BWagDsLiteProfileReservedIPAddresses_Object=MibTableColumn
bWagDsLiteProfileReservedIPAddresses=_BWagDsLiteProfileReservedIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,7),_BWagDsLiteProfileReservedIPAddresses_Type())
bWagDsLiteProfileReservedIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileReservedIPAddresses.setStatus(_A)
_BWagDsLiteProfileTotalPoolIPAddresses_Type=Unsigned32
_BWagDsLiteProfileTotalPoolIPAddresses_Object=MibTableColumn
bWagDsLiteProfileTotalPoolIPAddresses=_BWagDsLiteProfileTotalPoolIPAddresses_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,8),_BWagDsLiteProfileTotalPoolIPAddresses_Type())
bWagDsLiteProfileTotalPoolIPAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileTotalPoolIPAddresses.setStatus(_A)
_BWagDsLiteProfileMaxSubscribers_Type=Unsigned32
_BWagDsLiteProfileMaxSubscribers_Object=MibTableColumn
bWagDsLiteProfileMaxSubscribers=_BWagDsLiteProfileMaxSubscribers_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,9),_BWagDsLiteProfileMaxSubscribers_Type())
bWagDsLiteProfileMaxSubscribers.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileMaxSubscribers.setStatus(_A)
_BWagDsLiteProfileMaxTunnels_Type=Unsigned32
_BWagDsLiteProfileMaxTunnels_Object=MibTableColumn
bWagDsLiteProfileMaxTunnels=_BWagDsLiteProfileMaxTunnels_Object((1,3,6,1,4,1,39406,2,1,3,16,1,1,10),_BWagDsLiteProfileMaxTunnels_Type())
bWagDsLiteProfileMaxTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagDsLiteProfileMaxTunnels.setStatus(_C)
_BDSLitePortBlocksTotal_Type=Unsigned32
_BDSLitePortBlocksTotal_Object=MibScalar
bDSLitePortBlocksTotal=_BDSLitePortBlocksTotal_Object((1,3,6,1,4,1,39406,2,1,3,16,2),_BDSLitePortBlocksTotal_Type())
bDSLitePortBlocksTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLitePortBlocksTotal.setStatus(_A)
_BDSLitePortBlocksInUse_Type=Unsigned32
_BDSLitePortBlocksInUse_Object=MibScalar
bDSLitePortBlocksInUse=_BDSLitePortBlocksInUse_Object((1,3,6,1,4,1,39406,2,1,3,16,3),_BDSLitePortBlocksInUse_Type())
bDSLitePortBlocksInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLitePortBlocksInUse.setStatus(_A)
_BDSLiteTunnelsUsingOnePortBlock_Type=Unsigned32
_BDSLiteTunnelsUsingOnePortBlock_Object=MibScalar
bDSLiteTunnelsUsingOnePortBlock=_BDSLiteTunnelsUsingOnePortBlock_Object((1,3,6,1,4,1,39406,2,1,3,16,4),_BDSLiteTunnelsUsingOnePortBlock_Type())
bDSLiteTunnelsUsingOnePortBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLiteTunnelsUsingOnePortBlock.setStatus(_A)
_BDSLiteTunnelsUsingTwoPortBlocks_Type=Unsigned32
_BDSLiteTunnelsUsingTwoPortBlocks_Object=MibScalar
bDSLiteTunnelsUsingTwoPortBlocks=_BDSLiteTunnelsUsingTwoPortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,16,5),_BDSLiteTunnelsUsingTwoPortBlocks_Type())
bDSLiteTunnelsUsingTwoPortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLiteTunnelsUsingTwoPortBlocks.setStatus(_A)
_BDSLiteTunnelsUsingThreePortBlocks_Type=Unsigned32
_BDSLiteTunnelsUsingThreePortBlocks_Object=MibScalar
bDSLiteTunnelsUsingThreePortBlocks=_BDSLiteTunnelsUsingThreePortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,16,6),_BDSLiteTunnelsUsingThreePortBlocks_Type())
bDSLiteTunnelsUsingThreePortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLiteTunnelsUsingThreePortBlocks.setStatus(_A)
_BDSLiteTunnelsUsingFourPortBlocks_Type=Unsigned32
_BDSLiteTunnelsUsingFourPortBlocks_Object=MibScalar
bDSLiteTunnelsUsingFourPortBlocks=_BDSLiteTunnelsUsingFourPortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,16,7),_BDSLiteTunnelsUsingFourPortBlocks_Type())
bDSLiteTunnelsUsingFourPortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLiteTunnelsUsingFourPortBlocks.setStatus(_A)
_BDSLiteTunnelsUsingFivePortBlocks_Type=Unsigned32
_BDSLiteTunnelsUsingFivePortBlocks_Object=MibScalar
bDSLiteTunnelsUsingFivePortBlocks=_BDSLiteTunnelsUsingFivePortBlocks_Object((1,3,6,1,4,1,39406,2,1,3,16,8),_BDSLiteTunnelsUsingFivePortBlocks_Type())
bDSLiteTunnelsUsingFivePortBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:bDSLiteTunnelsUsingFivePortBlocks.setStatus(_A)
_BWagDsLiteNotifObjects_ObjectIdentity=ObjectIdentity
bWagDsLiteNotifObjects=_BWagDsLiteNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,17))
if mibBuilder.loadTexts:bWagDsLiteNotifObjects.setStatus(_A)
_BWagIpSystemStatsMIBObjects_ObjectIdentity=ObjectIdentity
bWagIpSystemStatsMIBObjects=_BWagIpSystemStatsMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,3,18))
if mibBuilder.loadTexts:bWagIpSystemStatsMIBObjects.setStatus(_A)
_BWagIpSystemStatsReasmReqds_Type=Counter64
_BWagIpSystemStatsReasmReqds_Object=MibScalar
bWagIpSystemStatsReasmReqds=_BWagIpSystemStatsReasmReqds_Object((1,3,6,1,4,1,39406,2,1,3,18,1),_BWagIpSystemStatsReasmReqds_Type())
bWagIpSystemStatsReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpSystemStatsReasmReqds.setStatus(_A)
_BWagIpIfStatsOutFragOKs_Type=Counter64
_BWagIpIfStatsOutFragOKs_Object=MibScalar
bWagIpIfStatsOutFragOKs=_BWagIpIfStatsOutFragOKs_Object((1,3,6,1,4,1,39406,2,1,3,18,2),_BWagIpIfStatsOutFragOKs_Type())
bWagIpIfStatsOutFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpIfStatsOutFragOKs.setStatus(_A)
_BWagIpSystemStatsReasmFails_Type=Counter64
_BWagIpSystemStatsReasmFails_Object=MibScalar
bWagIpSystemStatsReasmFails=_BWagIpSystemStatsReasmFails_Object((1,3,6,1,4,1,39406,2,1,3,18,3),_BWagIpSystemStatsReasmFails_Type())
bWagIpSystemStatsReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpSystemStatsReasmFails.setStatus(_A)
_BWagIpv6IfStatsReasmReqds_Type=Counter64
_BWagIpv6IfStatsReasmReqds_Object=MibScalar
bWagIpv6IfStatsReasmReqds=_BWagIpv6IfStatsReasmReqds_Object((1,3,6,1,4,1,39406,2,1,3,18,4),_BWagIpv6IfStatsReasmReqds_Type())
bWagIpv6IfStatsReasmReqds.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpv6IfStatsReasmReqds.setStatus(_A)
_BWagIpv6IfStatsOutFragOKs_Type=Counter64
_BWagIpv6IfStatsOutFragOKs_Object=MibScalar
bWagIpv6IfStatsOutFragOKs=_BWagIpv6IfStatsOutFragOKs_Object((1,3,6,1,4,1,39406,2,1,3,18,5),_BWagIpv6IfStatsOutFragOKs_Type())
bWagIpv6IfStatsOutFragOKs.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpv6IfStatsOutFragOKs.setStatus(_A)
_BWagIpv6IfStatsReasmFails_Type=Counter64
_BWagIpv6IfStatsReasmFails_Object=MibScalar
bWagIpv6IfStatsReasmFails=_BWagIpv6IfStatsReasmFails_Object((1,3,6,1,4,1,39406,2,1,3,18,6),_BWagIpv6IfStatsReasmFails_Type())
bWagIpv6IfStatsReasmFails.setMaxAccess(_B)
if mibBuilder.loadTexts:bWagIpv6IfStatsReasmFails.setStatus(_A)
bWagCgnatAuthIpAddrHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,1))
bWagCgnatAuthIpAddrHighThresholdReached.setObjects(*((_D,_G),(_D,_H),(_D,_k)))
if mibBuilder.loadTexts:bWagCgnatAuthIpAddrHighThresholdReached.setStatus(_A)
bWagCgnatAuthIpAddrLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,2))
bWagCgnatAuthIpAddrLowThresholdReached.setObjects(*((_D,_G),(_D,_H),(_D,_l)))
if mibBuilder.loadTexts:bWagCgnatAuthIpAddrLowThresholdReached.setStatus(_A)
bWagCgnatAuthIpAddressesExhausted=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,3))
bWagCgnatAuthIpAddressesExhausted.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:bWagCgnatAuthIpAddressesExhausted.setStatus(_A)
bWagCgnatPortBlocksUsedHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,4))
bWagCgnatPortBlocksUsedHighThresholdReached.setObjects(*((_D,_L),(_D,_M),(_D,_m)))
if mibBuilder.loadTexts:bWagCgnatPortBlocksUsedHighThresholdReached.setStatus(_C)
bWagCgnatPortBlocksUsedLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,5))
bWagCgnatPortBlocksUsedLowThresholdReached.setObjects(*((_D,_L),(_D,_M),(_D,_n)))
if mibBuilder.loadTexts:bWagCgnatPortBlocksUsedLowThresholdReached.setStatus(_C)
bWagDhcpTPSHighReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,6))
bWagDhcpTPSHighReached.setObjects((_D,_N))
if mibBuilder.loadTexts:bWagDhcpTPSHighReached.setStatus(_A)
bWagDhcpTPSLowReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,7))
bWagDhcpTPSLowReached.setObjects((_D,_N))
if mibBuilder.loadTexts:bWagDhcpTPSLowReached.setStatus(_A)
bWagVrgApiIpAddrUsedHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,8))
bWagVrgApiIpAddrUsedHighThresholdReached.setObjects(*((_D,_I),(_D,_J),(_D,_o)))
if mibBuilder.loadTexts:bWagVrgApiIpAddrUsedHighThresholdReached.setStatus(_A)
bWagVrgApiIpAddrUsedLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,9))
bWagVrgApiIpAddrUsedLowThresholdReached.setObjects(*((_D,_I),(_D,_J),(_D,_p)))
if mibBuilder.loadTexts:bWagVrgApiIpAddrUsedLowThresholdReached.setStatus(_A)
bWagVrgApiIpAddressesExhausted=NotificationType((1,3,6,1,4,1,39406,2,1,3,0,10))
bWagVrgApiIpAddressesExhausted.setObjects(*((_D,_I),(_D,_J)))
if mibBuilder.loadTexts:bWagVrgApiIpAddressesExhausted.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'benuWagStatsMIB':benuWagStatsMIB,'bWagStatsNotifications':bWagStatsNotifications,'bWagCgnatAuthIpAddrHighThresholdReached':bWagCgnatAuthIpAddrHighThresholdReached,'bWagCgnatAuthIpAddrLowThresholdReached':bWagCgnatAuthIpAddrLowThresholdReached,'bWagCgnatAuthIpAddressesExhausted':bWagCgnatAuthIpAddressesExhausted,'bWagCgnatPortBlocksUsedHighThresholdReached':bWagCgnatPortBlocksUsedHighThresholdReached,'bWagCgnatPortBlocksUsedLowThresholdReached':bWagCgnatPortBlocksUsedLowThresholdReached,'bWagDhcpTPSHighReached':bWagDhcpTPSHighReached,'bWagDhcpTPSLowReached':bWagDhcpTPSLowReached,'bWagVrgApiIpAddrUsedHighThresholdReached':bWagVrgApiIpAddrUsedHighThresholdReached,'bWagVrgApiIpAddrUsedLowThresholdReached':bWagVrgApiIpAddrUsedLowThresholdReached,'bWagVrgApiIpAddressesExhausted':bWagVrgApiIpAddressesExhausted,'bWagRadiusMIBObjects':bWagRadiusMIBObjects,'bWagRadiusTable':bWagRadiusTable,'bWagRadiusEntry':bWagRadiusEntry,_Q:bWagRadiusStatsInterval,'bWagRadiusIntervalDuration':bWagRadiusIntervalDuration,'bWagRadiusAuthLatencyMin':bWagRadiusAuthLatencyMin,'bWagRadiusAuthLatencyMax':bWagRadiusAuthLatencyMax,'bWagRadiusAuthLatencyAvg':bWagRadiusAuthLatencyAvg,'bWagRadiusAuthLatencyLast':bWagRadiusAuthLatencyLast,'bWagRadiusAcctLatencyMin':bWagRadiusAcctLatencyMin,'bWagRadiusAcctLatencyMax':bWagRadiusAcctLatencyMax,'bWagRadiusAcctLatencyAvg':bWagRadiusAcctLatencyAvg,'bWagRadiusAcctLatencyLast':bWagRadiusAcctLatencyLast,'bWagRadiusAccessRequestSent':bWagRadiusAccessRequestSent,'bWagRadiusAccessAcceptReceived':bWagRadiusAccessAcceptReceived,'bWagRadiusAccessRejectReceived':bWagRadiusAccessRejectReceived,'bWagRadiusAcctRequestSent':bWagRadiusAcctRequestSent,'bWagRadiusAcctResponseReceived':bWagRadiusAcctResponseReceived,'bWagRadiusCoAAckSent':bWagRadiusCoAAckSent,'bWagRadiusCoANackSent':bWagRadiusCoANackSent,'bWagRadiusCoARequestReceived':bWagRadiusCoARequestReceived,'bWagRadiusCoALatencyMin':bWagRadiusCoALatencyMin,'bWagRadiusCoALatencyMax':bWagRadiusCoALatencyMax,'bWagRadiusCoALatencyAvg':bWagRadiusCoALatencyAvg,'bWagRadiusCoALatencyLast':bWagRadiusCoALatencyLast,'bWagRadiusDMLatencyMin':bWagRadiusDMLatencyMin,'bWagRadiusDMLatencyMax':bWagRadiusDMLatencyMax,'bWagRadiusDMLatencyAvg':bWagRadiusDMLatencyAvg,'bWagRadiusDMLatencyLast':bWagRadiusDMLatencyLast,'bWagRadiusDMAckSent':bWagRadiusDMAckSent,'bWagRadiusDMNackSent':bWagRadiusDMNackSent,'bWagRadiusDMRequestReceived':bWagRadiusDMRequestReceived,'bWagRadiusNotifObjects':bWagRadiusNotifObjects,'bWagDhcpMIBObjects':bWagDhcpMIBObjects,'bWagDhcpTable':bWagDhcpTable,'bWagDhcpEntry':bWagDhcpEntry,_R:bWagDhcpStatsInterval,'bWagDhcpIntervalDuration':bWagDhcpIntervalDuration,'bWagDhcpDiscoverAckIntervalMin':bWagDhcpDiscoverAckIntervalMin,'bWagDhcpDiscoverAckIntervalMax':bWagDhcpDiscoverAckIntervalMax,'bWagDhcpDiscoverAckIntervalAvg':bWagDhcpDiscoverAckIntervalAvg,'bWagDhcpDiscoverAckIntervalLast':bWagDhcpDiscoverAckIntervalLast,'bWagDhcpRequestAckLatencyMin':bWagDhcpRequestAckLatencyMin,'bWagDhcpRequestAckLatencyMax':bWagDhcpRequestAckLatencyMax,'bWagDhcpRequestAckLatencyAvg':bWagDhcpRequestAckLatencyAvg,'bWagDhcpRequestAckLatencyLast':bWagDhcpRequestAckLatencyLast,'bWagDhcpDiscoverOfferLatencyMin':bWagDhcpDiscoverOfferLatencyMin,'bWagDhcpDiscoverOfferLatencyMax':bWagDhcpDiscoverOfferLatencyMax,'bWagDhcpDiscoverOfferLatencyAvg':bWagDhcpDiscoverOfferLatencyAvg,'bWagDhcpDiscoverOfferLatencyLast':bWagDhcpDiscoverOfferLatencyLast,'bWagDhcpDiscoverReceived':bWagDhcpDiscoverReceived,'bWagDhcpOfferSent':bWagDhcpOfferSent,'bWagDhcpRequestReceived':bWagDhcpRequestReceived,'bWagDhcpAckSent':bWagDhcpAckSent,'bWagDhcpNackSent':bWagDhcpNackSent,'bWagDhcpOfferRequestIntervalMin':bWagDhcpOfferRequestIntervalMin,'bWagDhcpOfferRequestIntervalMax':bWagDhcpOfferRequestIntervalMax,'bWagDhcpOfferRequestIntervalAvg':bWagDhcpOfferRequestIntervalAvg,'bWagDhcpOfferRequestIntervalLast':bWagDhcpOfferRequestIntervalLast,'bWagDhcpTPSTable':bWagDhcpTPSTable,'bWagDhcpTPSEntry':bWagDhcpTPSEntry,_S:bWagDhcpTPSInterval,'bWagDhcpTPSIntervalDuration':bWagDhcpTPSIntervalDuration,'bWagDhcpTPSLow':bWagDhcpTPSLow,'bWagDhcpTPSHigh':bWagDhcpTPSHigh,_N:bWagDhcpTPS,'bWagDhcpNotifObjects':bWagDhcpNotifObjects,'bWagSubscriberMIBObjects':bWagSubscriberMIBObjects,'bWagSubscriberTable':bWagSubscriberTable,'bWagSubscriberEntry':bWagSubscriberEntry,_T:bWagSubscriberStatsInterval,'bWagSubscriberIntervalDuration':bWagSubscriberIntervalDuration,'bWagSubscriberActivationsCount':bWagSubscriberActivationsCount,'bWagSubscriberDeletionsCount':bWagSubscriberDeletionsCount,'bWagSubscriberAuthenticationsCount':bWagSubscriberAuthenticationsCount,'bWagSubscriberRedirectionsCount':bWagSubscriberRedirectionsCount,'bWagSubscriberRedirectionsByAcl':bWagSubscriberRedirectionsByAcl,'bWagSubscriberAPMobilityOccurencesCount':bWagSubscriberAPMobilityOccurencesCount,'bWagSubscriberDeletionsByDMCount':bWagSubscriberDeletionsByDMCount,'bWagSubscriberIdleTimeoutCount':bWagSubscriberIdleTimeoutCount,'bWagSubscriberSessionTimeoutPreauthCount':bWagSubscriberSessionTimeoutPreauthCount,'bWagSubscriberSessionTimeoutAuthviaportalCount':bWagSubscriberSessionTimeoutAuthviaportalCount,'bWagSubscriberDroppedByLicenseManagerCount':bWagSubscriberDroppedByLicenseManagerCount,'bWagSubscriberThrottlingOccurrencesCount':bWagSubscriberThrottlingOccurrencesCount,'bWagSubscriberThrottledCount':bWagSubscriberThrottledCount,'bWagSubscriberAbsoluteTimeoutCount':bWagSubscriberAbsoluteTimeoutCount,'bWagSubscriberAuthsViaPortalCount':bWagSubscriberAuthsViaPortalCount,'bWagSubscriberAuthenticationsCountVia8021x':bWagSubscriberAuthenticationsCountVia8021x,'bWagSubscriberAuthenticationsCountViaSingleStatic':bWagSubscriberAuthenticationsCountViaSingleStatic,'bWagSubscriberAuthenticationsCountViaRoutedSubnet':bWagSubscriberAuthenticationsCountViaRoutedSubnet,'bWagSubscriberSessionTimeoutAuthVia8021x':bWagSubscriberSessionTimeoutAuthVia8021x,'bWagSubscriberHomeTotalSubsDeleted':bWagSubscriberHomeTotalSubsDeleted,'bWagSubscriberHomeTransientSubsDeleted':bWagSubscriberHomeTransientSubsDeleted,'bWagSubscriberHomeUserStaticSubsDeleted':bWagSubscriberHomeUserStaticSubsDeleted,'bWagSubscriberHomeDhcpStaticSubsDeleted':bWagSubscriberHomeDhcpStaticSubsDeleted,'bWagSubscriberHomeDhcpDynSubsDeleted':bWagSubscriberHomeDhcpDynSubsDeleted,'bWagSubscriberHomePubStaticSubsDeleted':bWagSubscriberHomePubStaticSubsDeleted,'bWagSubscriberSpWifiActivationsCount':bWagSubscriberSpWifiActivationsCount,'bWagSubscriberHomeActivationsCount':bWagSubscriberHomeActivationsCount,'bWagSubscriberDsLiteActivationsCount':bWagSubscriberDsLiteActivationsCount,'bWagNumCurrentSubscribers':bWagNumCurrentSubscribers,'bWagNumAuthenticatedSubscribers':bWagNumAuthenticatedSubscribers,'bWagNumUnauthenticatedSubscribers':bWagNumUnauthenticatedSubscribers,'bWagNumSubsWithPrivateIPAddress':bWagNumSubsWithPrivateIPAddress,'bWagNumAuthSubsWithPublicIPAddress':bWagNumAuthSubsWithPublicIPAddress,'bWagNumUnAuthSubsWithPublicIPAddress':bWagNumUnAuthSubsWithPublicIPAddress,'bWagNumMigrantSubscribersCount':bWagNumMigrantSubscribersCount,'bWagNumRedirectedSubscribersCount':bWagNumRedirectedSubscribersCount,'bWagPolicyTable':bWagPolicyTable,'bWagPolicyEntry':bWagPolicyEntry,_U:bWagPolicyType,_V:bWagPolicyIndex,'bWagPolicyName':bWagPolicyName,'bWagNumOfSubscribersWithPolicy':bWagNumOfSubscribersWithPolicy,'bWagNumOfAuthSubscribersWithPolicy':bWagNumOfAuthSubscribersWithPolicy,'bWagNumOfUnAuthSubscribersWithPolicy':bWagNumOfUnAuthSubscribersWithPolicy,'bWagNumSubsAuthenticatedWithIPv6Prefix':bWagNumSubsAuthenticatedWithIPv6Prefix,'bWagNumCurrent8021xSubscribers':bWagNumCurrent8021xSubscribers,'bWagNumPreAuthenticatedSubscribers':bWagNumPreAuthenticatedSubscribers,'bWagNumCurrentSingleStaticSubscribers':bWagNumCurrentSingleStaticSubscribers,'bWagNumCurrentRoutedSubnetSubscribers':bWagNumCurrentRoutedSubnetSubscribers,'bWagNumSubsUnauthenticatedWithIPv6Prefix':bWagNumSubsUnauthenticatedWithIPv6Prefix,'bWagNumSubsViaStaticAuthPolicy':bWagNumSubsViaStaticAuthPolicy,'bWagNumCurrentHomeSubscribers':bWagNumCurrentHomeSubscribers,'bWagNumCurrentSPWiFiSubscribers':bWagNumCurrentSPWiFiSubscribers,'bWagNumCurrentHomeTransientSubs':bWagNumCurrentHomeTransientSubs,'bWagNumCurrentHomeUserStatSubs':bWagNumCurrentHomeUserStatSubs,'bWagNumCurrentHomeDhcpStatSubs':bWagNumCurrentHomeDhcpStatSubs,'bWagNumCurrentHomeDhcpDynSubs':bWagNumCurrentHomeDhcpDynSubs,'bWagNumCurrentHomePubStatSubs':bWagNumCurrentHomePubStatSubs,'bWagNumPreAuthSpwifiSubscribers':bWagNumPreAuthSpwifiSubscribers,'bWagNumPreAuthHomeSubscribers':bWagNumPreAuthHomeSubscribers,'bWagNumPreAuthenticatedSubscribersS2aPmip6':bWagNumPreAuthenticatedSubscribersS2aPmip6,'bWagNumCurrentSSIDS2aSubscribersPmip6':bWagNumCurrentSSIDS2aSubscribersPmip6,'bWagNumCurrentDSLiteSubscribers':bWagNumCurrentDSLiteSubscribers,'bWagSubscriberNotifObjects':bWagSubscriberNotifObjects,'bWagTunnelStatsMIBObjects':bWagTunnelStatsMIBObjects,'bWagTunnelTable':bWagTunnelTable,'bWagTunnelEntry':bWagTunnelEntry,_W:bWagTunnelStatsInterval,'bWagTunnelIntervalDuration':bWagTunnelIntervalDuration,'bWagTunnelPktsRxdGRE':bWagTunnelPktsRxdGRE,'bWagTunnelPktsRxdGREPayloadTEB':bWagTunnelPktsRxdGREPayloadTEB,'bWagTunnelPktsRxdGREPayloadMPLS':bWagTunnelPktsRxdGREPayloadMPLS,'bWagTunnelPktsEncapsulatedGRE':bWagTunnelPktsEncapsulatedGRE,'bWagTunnelPktsDecapsulatedGRE':bWagTunnelPktsDecapsulatedGRE,'bWagTunnelPktsRxdARP':bWagTunnelPktsRxdARP,'bWagTunnelPktsRxdDHCP':bWagTunnelPktsRxdDHCP,'bWagTunnelPktsRxdDNS':bWagTunnelPktsRxdDNS,'bWagTunnelPktsRxdHTTP':bWagTunnelPktsRxdHTTP,'bWagTunnelPktsRxdHTTPGetReq':bWagTunnelPktsRxdHTTPGetReq,'bWagTunnelPktsTxdHTTP':bWagTunnelPktsTxdHTTP,'bWagTunnelPktsTxdHTTPRedir':bWagTunnelPktsTxdHTTPRedir,'bWagTunnelPktsRxdHTTPS':bWagTunnelPktsRxdHTTPS,'bWagTunnelPktsRxdTCPSyn':bWagTunnelPktsRxdTCPSyn,'bWagTunnelPktsTxdTCPSynAck':bWagTunnelPktsTxdTCPSynAck,'bWagTunnelPktsTxdTCPFin':bWagTunnelPktsTxdTCPFin,'bWagTunnelPktsRxdTCPFinAck':bWagTunnelPktsRxdTCPFinAck,'bWagTunnelPktsTxdTCPAck2Fin':bWagTunnelPktsTxdTCPAck2Fin,'bWagTunnelCreatedDynamically':bWagTunnelCreatedDynamically,'bWagTunnelCreatedStatically':bWagTunnelCreatedStatically,'bWagTunnelDeleted':bWagTunnelDeleted,'bWagTunnelDeletedDueToInactivity':bWagTunnelDeletedDueToInactivity,'bWagTunnelDeletedByCommand':bWagTunnelDeletedByCommand,'bWagTunnelMaxSupported':bWagTunnelMaxSupported,'bWagTunnelMaxCountReached':bWagTunnelMaxCountReached,'bWagTunnelTunnelsLookupFound':bWagTunnelTunnelsLookupFound,'bWagTunnelTunnelsLookupNotFound':bWagTunnelTunnelsLookupNotFound,'bWagTunnelCountHighThreshold':bWagTunnelCountHighThreshold,'bWagTunnelCountLowThreshold':bWagTunnelCountLowThreshold,'bWagTunnelDeletedDueToReject':bWagTunnelDeletedDueToReject,'bWagTunnelDeletedDueToAbort':bWagTunnelDeletedDueToAbort,'bWagTunnelDeletedDueToMacResFail':bWagTunnelDeletedDueToMacResFail,'bWagTunnelDeletedDueToLifDown':bWagTunnelDeletedDueToLifDown,'bWagTunnelDeletedDueToB2bSubsDelete':bWagTunnelDeletedDueToB2bSubsDelete,'bWagL2tpv3TunnelPktsRxd':bWagL2tpv3TunnelPktsRxd,'bWagL2tpv3TunnelPktsEncapsulated':bWagL2tpv3TunnelPktsEncapsulated,'bWagL2tpv3TunnelPktsDecapsulated':bWagL2tpv3TunnelPktsDecapsulated,'bWagL2tpv3TunnelPktsRxdARP':bWagL2tpv3TunnelPktsRxdARP,'bWagL2tpv3TunnelPktsRxdDHCP':bWagL2tpv3TunnelPktsRxdDHCP,'bWagL2tpv3TunnelPktsRxdDNS':bWagL2tpv3TunnelPktsRxdDNS,'bWagL2tpv3TunnelCreatedDynamically':bWagL2tpv3TunnelCreatedDynamically,'bWagL2tpv3TunnelDeleted':bWagL2tpv3TunnelDeleted,'bWagL2tpv3TunnelDeletedDueToInactivity':bWagL2tpv3TunnelDeletedDueToInactivity,'bWagL2tpv3TunnelDeletedByCommand':bWagL2tpv3TunnelDeletedByCommand,'bWagL2tpv3TunnelDeletedDueToLifDown':bWagL2tpv3TunnelDeletedDueToLifDown,'bWagNumCurrentTunnels':bWagNumCurrentTunnels,'bWagNumTunnelsCreatedDynamically':bWagNumTunnelsCreatedDynamically,'bWagNumTunnelsCreatedStatically':bWagNumTunnelsCreatedStatically,'bWagNumTunnelsDeleted':bWagNumTunnelsDeleted,'bWagNumTunnelsInactiveDeleted':bWagNumTunnelsInactiveDeleted,'bWagNumTunnelsDeletedByCommand':bWagNumTunnelsDeletedByCommand,'bWagNumTunnelsSubsAssociated':bWagNumTunnelsSubsAssociated,'bWagNumTunnelsSchedDeletion':bWagNumTunnelsSchedDeletion,'bWagNumCurrentTunnelsIPv4':bWagNumCurrentTunnelsIPv4,'bWagNumCurrentTunnelsIPv6':bWagNumCurrentTunnelsIPv6,'bWagNumTunnelsDeletedByB2B':bWagNumTunnelsDeletedByB2B,'bWagNumTunnelsDeletedDuetoLIFDown':bWagNumTunnelsDeletedDuetoLIFDown,'bWagNumCurrentTunnelsSpWiFi':bWagNumCurrentTunnelsSpWiFi,'bWagNumCurrentTunnelsHome':bWagNumCurrentTunnelsHome,'bWagNumCurrTunnHomeAndSpWiFi':bWagNumCurrTunnHomeAndSpWiFi,'bWagNumCurrentTunnHomeInactive':bWagNumCurrentTunnHomeInactive,'bWagNumCurrentTunnHomeAccept':bWagNumCurrentTunnHomeAccept,'bWagNumL2tpv3TunnelsCreatedDynamically':bWagNumL2tpv3TunnelsCreatedDynamically,'bWagNumL2tpv3TunnelsDeleted':bWagNumL2tpv3TunnelsDeleted,'bWagNumL2tpv3TunnelsInactiveDeleted':bWagNumL2tpv3TunnelsInactiveDeleted,'bWagNumL2tpv3TunnelsDeletedByCommand':bWagNumL2tpv3TunnelsDeletedByCommand,'bWagNumL2tpv3TunnelsSubsAssociated':bWagNumL2tpv3TunnelsSubsAssociated,'bWagNumCurrentL2tpv3TunnelsIPv4':bWagNumCurrentL2tpv3TunnelsIPv4,'bWagNumL2tpv3TunnelsDeletedDuetoLIFDown':bWagNumL2tpv3TunnelsDeletedDuetoLIFDown,'bWagNumCurrentL2tpv3TunnelsSpWiFi':bWagNumCurrentL2tpv3TunnelsSpWiFi,'bWagNumCurrentTunnelsDSLite':bWagNumCurrentTunnelsDSLite,'bWagTunnelNotifObjects':bWagTunnelNotifObjects,'bWagCgnatMIBObjects':bWagCgnatMIBObjects,'bWagCgnatProfileStatsTable':bWagCgnatProfileStatsTable,'bWagCgnatProfileStatsEntry':bWagCgnatProfileStatsEntry,_X:bWagCgnatProfileStatsIndex,'bWagCgnatProfileName':bWagCgnatProfileName,'bWagCgnatProfileType':bWagCgnatProfileType,'bWagCgnatProfileNATIPPoolGroup':bWagCgnatProfileNATIPPoolGroup,'bWagCgnatProfileSubscribers':bWagCgnatProfileSubscribers,'bWagCgnatProfileMaxIPAddresses':bWagCgnatProfileMaxIPAddresses,'bWagCgnatProfileUsedIPAddresses':bWagCgnatProfileUsedIPAddresses,'bWagCgnatProfileReservedIPAddresses':bWagCgnatProfileReservedIPAddresses,'bWagCgnatProfileTotalPortBlocks':bWagCgnatProfileTotalPortBlocks,'bWagCgnatProfilePortBlocksUsed':bWagCgnatProfilePortBlocksUsed,'bWagCgnatProfilePortBlocksReused':bWagCgnatProfilePortBlocksReused,'bWagCgnatProfileTotalPoolIPAddresses':bWagCgnatProfileTotalPoolIPAddresses,'bWagCgnatIPStatsTable':bWagCgnatIPStatsTable,'bWagCgnatIPStatsEntry':bWagCgnatIPStatsEntry,_Y:bWagCgnatIPStatsIndex,'bWagCgnatPublicIPAddressType':bWagCgnatPublicIPAddressType,'bWagCgnatPublicIPAddress':bWagCgnatPublicIPAddress,'bWagCgnatIPPortBlocksUsed':bWagCgnatIPPortBlocksUsed,'bWagCgnatIPPortBlocksFree':bWagCgnatIPPortBlocksFree,'bWagCgnatIPPortBlocksReused':bWagCgnatIPPortBlocksReused,'bWagCgnatIPSubActiveCount':bWagCgnatIPSubActiveCount,'bWagCgnatIPPacketsDropped':bWagCgnatIPPacketsDropped,'bWagCgnatPeriodIpTable':bWagCgnatPeriodIpTable,'bWagCgnatPeriodIpEntry':bWagCgnatPeriodIpEntry,_Z:bWagCgnatPeriodIpInterval,_a:bWagCgnatPeriodIpIndex,'bWagCgnatIPAddressType':bWagCgnatIPAddressType,'bWagCgnatIPAddress':bWagCgnatIPAddress,'bWagCgnatPacketsDropped':bWagCgnatPacketsDropped,'bWagCgnatPortBlockMaxUtil':bWagCgnatPortBlockMaxUtil,'bWagCgnatPortBlockMinUtil':bWagCgnatPortBlockMinUtil,'bWagCgnatIntervalDuration':bWagCgnatIntervalDuration,'bWagCgnatUnauthIPStatsTable':bWagCgnatUnauthIPStatsTable,'bWagCgnatUnauthIPStatsEntry':bWagCgnatUnauthIPStatsEntry,_b:bWagCgnatUnauthIPStatsIndex,'bWagCgnatUnauthPublicIPAddressType':bWagCgnatUnauthPublicIPAddressType,'bWagCgnatUnauthPublicIPAddress':bWagCgnatUnauthPublicIPAddress,'bWagCgnatUnauthIPPortBlocksUsed':bWagCgnatUnauthIPPortBlocksUsed,'bWagCgnatUnauthIPPortBlocksFree':bWagCgnatUnauthIPPortBlocksFree,'bWagCgnatUnauthIPPortBlocksReused':bWagCgnatUnauthIPPortBlocksReused,'bWagCgnatUnauthIPSubActiveCount':bWagCgnatUnauthIPSubActiveCount,'bWagCgnatUnauthPeriodIpTable':bWagCgnatUnauthPeriodIpTable,'bWagCgnatUnauthPeriodIpEntry':bWagCgnatUnauthPeriodIpEntry,_c:bWagCgnatUnauthPeriodIpInterval,_d:bWagCgnatUnauthPeriodIpIndex,'bWagCgnatUnauthIPAddressType':bWagCgnatUnauthIPAddressType,'bWagCgnatUnauthIPAddress':bWagCgnatUnauthIPAddress,'bWagCgnatUnauthPortBlockMaxUtil':bWagCgnatUnauthPortBlockMaxUtil,'bWagCgnatUnauthPortBlockMinUtil':bWagCgnatUnauthPortBlockMinUtil,'bWagCgnatUnauthIntervalDuration':bWagCgnatUnauthIntervalDuration,'bWagCgnatAuthPortUtilTable':bWagCgnatAuthPortUtilTable,'bWagCgnatAuthPortUtilEntry':bWagCgnatAuthPortUtilEntry,_e:bWagCgnatAuthSubscriberMac,'bWagCgnatAuthSubscriberPortsUtil':bWagCgnatAuthSubscriberPortsUtil,'bWagCgnatAuthPortRisingThresholdCrossedSubCount':bWagCgnatAuthPortRisingThresholdCrossedSubCount,'bWagCgnatPoolGroupStatsTable':bWagCgnatPoolGroupStatsTable,'bWagCgnatPoolGroupStatsEntry':bWagCgnatPoolGroupStatsEntry,_f:bWagCgnatPoolGroupType,_g:bWagCgnatPoolGroupIndex,'bWagCgnatPoolGroupName':bWagCgnatPoolGroupName,'bWagCgnatPoolGroupSubscribers':bWagCgnatPoolGroupSubscribers,'bWagCgnatPoolGroupUsedIPAddresses':bWagCgnatPoolGroupUsedIPAddresses,'bWagCgnatPoolGroupReservedIPAddresses':bWagCgnatPoolGroupReservedIPAddresses,'bWagCgnatPoolGroupTotalIPAddresses':bWagCgnatPoolGroupTotalIPAddresses,'bWagCgnatNotifObjects':bWagCgnatNotifObjects,_G:bWagCgnatProfileIPPoolGroup,_H:bWagCgnatTotalPoolIPAddresses,_k:bWagCgnatAuthIpAddrUsedHighThreshold,_l:bWagCgnatAuthIpAddrUsedLowThreshold,_L:bWagCgnatSubscriberMac,_M:bWagCgnatTotalPortBlocksPerSubscriber,_m:bWagCgnatPortBlocksUsedHighThreshold,_n:bWagCgnatPortBlocksUsedLowThreshold,'bWagProcessingLatencyMIBObjects':bWagProcessingLatencyMIBObjects,'bWagUpstreamProcessingLatencyPktCount':bWagUpstreamProcessingLatencyPktCount,'bWagUpstreamProcessingLatencyMax':bWagUpstreamProcessingLatencyMax,'bWagUpstreamProcessingLatencyMin':bWagUpstreamProcessingLatencyMin,'bWagUpstreamProcessingLatencyAvg':bWagUpstreamProcessingLatencyAvg,'bWagDownstreamProcessingLatencyPktCount':bWagDownstreamProcessingLatencyPktCount,'bWagDownstreamProcessingLatencyMax':bWagDownstreamProcessingLatencyMax,'bWagDownstreamProcessingLatencyMin':bWagDownstreamProcessingLatencyMin,'bWagDownstreamProcessingLatencyAvg':bWagDownstreamProcessingLatencyAvg,'bWagProcessingLatencyNotifObjects':bWagProcessingLatencyNotifObjects,'bWagDhcpv6MIBObjects':bWagDhcpv6MIBObjects,'bWagDHCPv6Table':bWagDHCPv6Table,'bWagDHCPv6Entry':bWagDHCPv6Entry,_h:bWagDHCPv6StatsInterval,'bWagDHCPv6IntervalDuration':bWagDHCPv6IntervalDuration,'bWagDHCPv6SolicitReplyIntervalMin':bWagDHCPv6SolicitReplyIntervalMin,'bWagDHCPv6SolicitReplyIntervalMax':bWagDHCPv6SolicitReplyIntervalMax,'bWagDHCPv6SolicitReplyIntervalAvg':bWagDHCPv6SolicitReplyIntervalAvg,'bWagDHCPv6SolicitReplyIntervalLast':bWagDHCPv6SolicitReplyIntervalLast,'bWagDHCPv6RequestReplyLatencyMin':bWagDHCPv6RequestReplyLatencyMin,'bWagDHCPv6RequestReplyLatencyMax':bWagDHCPv6RequestReplyLatencyMax,'bWagDHCPv6RequestReplyLatencyAvg':bWagDHCPv6RequestReplyLatencyAvg,'bWagDHCPv6RequestReplyLatencyLast':bWagDHCPv6RequestReplyLatencyLast,'bWagDHCPv6SolicitAdvLatencyMin':bWagDHCPv6SolicitAdvLatencyMin,'bWagDHCPv6SolicitAdvLatencyMax':bWagDHCPv6SolicitAdvLatencyMax,'bWagDHCPv6SolicitAdvLatencyAvg':bWagDHCPv6SolicitAdvLatencyAvg,'bWagDHCPv6SolicitAdvLatencyLast':bWagDHCPv6SolicitAdvLatencyLast,'bWagDHCPv6AdvRequestIntervalMin':bWagDHCPv6AdvRequestIntervalMin,'bWagDHCPv6AdvRequestIntervalMax':bWagDHCPv6AdvRequestIntervalMax,'bWagDHCPv6AdvRequestIntervalAvg':bWagDHCPv6AdvRequestIntervalAvg,'bWagDHCPv6AdvRequestIntervalLast':bWagDHCPv6AdvRequestIntervalLast,'bWagDHCPv6SolicitReceived':bWagDHCPv6SolicitReceived,'bWagDHCPv6AdvertisementSent':bWagDHCPv6AdvertisementSent,'bWagDHCPv6RequestReceived':bWagDHCPv6RequestReceived,'bWagDHCPv6ReplySent':bWagDHCPv6ReplySent,'bWagMHNMIBObjects':bWagMHNMIBObjects,'bWagMHNProfileStatsTable':bWagMHNProfileStatsTable,'bWagMHNProfileStatsEntry':bWagMHNProfileStatsEntry,_i:bWagMHNProfileStatsIndex,'bWagMHNProfileName':bWagMHNProfileName,'bWagMHNProfileNATIPPoolGroup':bWagMHNProfileNATIPPoolGroup,'bWagMHNProfileMaxSubscribers':bWagMHNProfileMaxSubscribers,'bWagMHNProfileMaxIPAddresses':bWagMHNProfileMaxIPAddresses,'bWagMHNProfileUsedIPAddresses':bWagMHNProfileUsedIPAddresses,'bWagMHNProfileTotalPortBlocks':bWagMHNProfileTotalPortBlocks,'bWagMHNProfileTotalPoolIPAddresses':bWagMHNProfileTotalPoolIPAddresses,'bWagVrgApiNotifObjects':bWagVrgApiNotifObjects,_o:bWagVrgApiIpAddrUsedHighThreshold,_p:bWagVrgApiIpAddrUsedLowThreshold,_I:bWagrgApiIPPoolGroup,_J:bWagVRGApiIPoolIPAddresses,'bWagDsLiteMIBObjects':bWagDsLiteMIBObjects,'bWagDsLiteProfileStatsTable':bWagDsLiteProfileStatsTable,'bWagDsLiteProfileStatsEntry':bWagDsLiteProfileStatsEntry,_j:bWagDsLiteProfileStatsIndex,'bWagDsLiteProfileName':bWagDsLiteProfileName,'bWagDsLiteProfileType':bWagDsLiteProfileType,'bWagDsLiteProfileNATIPPoolGroup':bWagDsLiteProfileNATIPPoolGroup,'bWagDsLiteProfileMaxIPAddresses':bWagDsLiteProfileMaxIPAddresses,'bWagDsLiteProfileUsedIPAddresses':bWagDsLiteProfileUsedIPAddresses,'bWagDsLiteProfileReservedIPAddresses':bWagDsLiteProfileReservedIPAddresses,'bWagDsLiteProfileTotalPoolIPAddresses':bWagDsLiteProfileTotalPoolIPAddresses,'bWagDsLiteProfileMaxSubscribers':bWagDsLiteProfileMaxSubscribers,'bWagDsLiteProfileMaxTunnels':bWagDsLiteProfileMaxTunnels,'bDSLitePortBlocksTotal':bDSLitePortBlocksTotal,'bDSLitePortBlocksInUse':bDSLitePortBlocksInUse,'bDSLiteTunnelsUsingOnePortBlock':bDSLiteTunnelsUsingOnePortBlock,'bDSLiteTunnelsUsingTwoPortBlocks':bDSLiteTunnelsUsingTwoPortBlocks,'bDSLiteTunnelsUsingThreePortBlocks':bDSLiteTunnelsUsingThreePortBlocks,'bDSLiteTunnelsUsingFourPortBlocks':bDSLiteTunnelsUsingFourPortBlocks,'bDSLiteTunnelsUsingFivePortBlocks':bDSLiteTunnelsUsingFivePortBlocks,'bWagDsLiteNotifObjects':bWagDsLiteNotifObjects,'bWagIpSystemStatsMIBObjects':bWagIpSystemStatsMIBObjects,'bWagIpSystemStatsReasmReqds':bWagIpSystemStatsReasmReqds,'bWagIpIfStatsOutFragOKs':bWagIpIfStatsOutFragOKs,'bWagIpSystemStatsReasmFails':bWagIpSystemStatsReasmFails,'bWagIpv6IfStatsReasmReqds':bWagIpv6IfStatsReasmReqds,'bWagIpv6IfStatsOutFragOKs':bWagIpv6IfStatsOutFragOKs,'bWagIpv6IfStatsReasmFails':bWagIpv6IfStatsReasmFails})