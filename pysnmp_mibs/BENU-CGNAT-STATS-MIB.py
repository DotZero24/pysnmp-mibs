_R='bCgnatTunnelPortBlocksUsedLowThreshold'
_Q='bCgnatTunnelPortBlocksUsedHighThreshold'
_P='bCgnatPortBlocksUsedLowThreshold'
_O='bCgnatPortBlocksUsedHighThreshold'
_N='bCgnatAuthPortUtilIndex'
_M='bCgnatUnauthStatsIndex'
_L='bCgnatAuthStatsIndex'
_K='bCgnatPortParity'
_J='bCgnatOddPortsForTunnel'
_I='bCgnatEvenPortsForTunnel'
_H='bCgnatThresholdTunnelId'
_G='bCgnatTotalPortBlocksPerSubscriber'
_F='bCgnatSubscriberMac'
_E='not-accessible'
_D='accessible-for-notify'
_C='BENU-CGNAT-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuWAG,=mibBuilder.importSymbols('BENU-WAG-MIB','benuWAG')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
benuCgnatStatsMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,9))
if mibBuilder.loadTexts:benuCgnatStatsMIB.setRevisions(('2017-01-24 00:00','2017-01-04 00:00','2016-12-22 00:00','2015-01-27 00:00','2014-12-10 00:00','2014-11-24 00:00'))
_BCgnatNotifications_ObjectIdentity=ObjectIdentity
bCgnatNotifications=_BCgnatNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,9,0))
if mibBuilder.loadTexts:bCgnatNotifications.setStatus(_A)
_BCgnatMIBObjects_ObjectIdentity=ObjectIdentity
bCgnatMIBObjects=_BCgnatMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,9,1))
if mibBuilder.loadTexts:bCgnatMIBObjects.setStatus(_A)
_BCgnatAuthStatsTable_Object=MibTable
bCgnatAuthStatsTable=_BCgnatAuthStatsTable_Object((1,3,6,1,4,1,39406,2,1,9,1,1))
if mibBuilder.loadTexts:bCgnatAuthStatsTable.setStatus(_A)
_BCgnatAuthStatsEntry_Object=MibTableRow
bCgnatAuthStatsEntry=_BCgnatAuthStatsEntry_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1))
bCgnatAuthStatsEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:bCgnatAuthStatsEntry.setStatus(_A)
_BCgnatAuthStatsIndex_Type=Integer32
_BCgnatAuthStatsIndex_Object=MibTableColumn
bCgnatAuthStatsIndex=_BCgnatAuthStatsIndex_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,1),_BCgnatAuthStatsIndex_Type())
bCgnatAuthStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bCgnatAuthStatsIndex.setStatus(_A)
_BCgnatAuthProfileName_Type=DisplayString
_BCgnatAuthProfileName_Object=MibTableColumn
bCgnatAuthProfileName=_BCgnatAuthProfileName_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,2),_BCgnatAuthProfileName_Type())
bCgnatAuthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthProfileName.setStatus(_A)
_BCgnatAuthDomainPublicIpZeroCount_Type=Counter64
_BCgnatAuthDomainPublicIpZeroCount_Object=MibTableColumn
bCgnatAuthDomainPublicIpZeroCount=_BCgnatAuthDomainPublicIpZeroCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,3),_BCgnatAuthDomainPublicIpZeroCount_Type())
bCgnatAuthDomainPublicIpZeroCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDomainPublicIpZeroCount.setStatus(_A)
_BCgnatAuthDomainNoFreePortCount_Type=Counter64
_BCgnatAuthDomainNoFreePortCount_Object=MibTableColumn
bCgnatAuthDomainNoFreePortCount=_BCgnatAuthDomainNoFreePortCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,4),_BCgnatAuthDomainNoFreePortCount_Type())
bCgnatAuthDomainNoFreePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDomainNoFreePortCount.setStatus(_A)
_BCgnatAuthFlowAddSuccessCount_Type=Counter64
_BCgnatAuthFlowAddSuccessCount_Object=MibTableColumn
bCgnatAuthFlowAddSuccessCount=_BCgnatAuthFlowAddSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,5),_BCgnatAuthFlowAddSuccessCount_Type())
bCgnatAuthFlowAddSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowAddSuccessCount.setStatus(_A)
_BCgnatAuthFlowAddFailureCount_Type=Counter64
_BCgnatAuthFlowAddFailureCount_Object=MibTableColumn
bCgnatAuthFlowAddFailureCount=_BCgnatAuthFlowAddFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,6),_BCgnatAuthFlowAddFailureCount_Type())
bCgnatAuthFlowAddFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowAddFailureCount.setStatus(_A)
_BCgnatAuthTimerAllocFailureCount_Type=Counter64
_BCgnatAuthTimerAllocFailureCount_Object=MibTableColumn
bCgnatAuthTimerAllocFailureCount=_BCgnatAuthTimerAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,7),_BCgnatAuthTimerAllocFailureCount_Type())
bCgnatAuthTimerAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthTimerAllocFailureCount.setStatus(_A)
_BCgnatAuthFlowDeleteSuccessCount_Type=Counter64
_BCgnatAuthFlowDeleteSuccessCount_Object=MibTableColumn
bCgnatAuthFlowDeleteSuccessCount=_BCgnatAuthFlowDeleteSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,8),_BCgnatAuthFlowDeleteSuccessCount_Type())
bCgnatAuthFlowDeleteSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeleteSuccessCount.setStatus(_A)
_BCgnatAuthFlowDeleteFailureCount_Type=Counter64
_BCgnatAuthFlowDeleteFailureCount_Object=MibTableColumn
bCgnatAuthFlowDeleteFailureCount=_BCgnatAuthFlowDeleteFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,9),_BCgnatAuthFlowDeleteFailureCount_Type())
bCgnatAuthFlowDeleteFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeleteFailureCount.setStatus(_A)
_BCgnatAuthUnsupportedL4DropCount_Type=Counter64
_BCgnatAuthUnsupportedL4DropCount_Object=MibTableColumn
bCgnatAuthUnsupportedL4DropCount=_BCgnatAuthUnsupportedL4DropCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,10),_BCgnatAuthUnsupportedL4DropCount_Type())
bCgnatAuthUnsupportedL4DropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUnsupportedL4DropCount.setStatus(_A)
_BCgnatAuthNatflowSyncFailureCount_Type=Counter64
_BCgnatAuthNatflowSyncFailureCount_Object=MibTableColumn
bCgnatAuthNatflowSyncFailureCount=_BCgnatAuthNatflowSyncFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,11),_BCgnatAuthNatflowSyncFailureCount_Type())
bCgnatAuthNatflowSyncFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthNatflowSyncFailureCount.setStatus(_A)
_BCgnatAuthIcmpIdAllocSuccessCount_Type=Counter64
_BCgnatAuthIcmpIdAllocSuccessCount_Object=MibTableColumn
bCgnatAuthIcmpIdAllocSuccessCount=_BCgnatAuthIcmpIdAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,12),_BCgnatAuthIcmpIdAllocSuccessCount_Type())
bCgnatAuthIcmpIdAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthIcmpIdAllocSuccessCount.setStatus(_A)
_BCgnatAuthTcpPortAllocSuccessCount_Type=Counter64
_BCgnatAuthTcpPortAllocSuccessCount_Object=MibTableColumn
bCgnatAuthTcpPortAllocSuccessCount=_BCgnatAuthTcpPortAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,13),_BCgnatAuthTcpPortAllocSuccessCount_Type())
bCgnatAuthTcpPortAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthTcpPortAllocSuccessCount.setStatus(_A)
_BCgnatAuthUdpPortAllocSuccessCount_Type=Counter64
_BCgnatAuthUdpPortAllocSuccessCount_Object=MibTableColumn
bCgnatAuthUdpPortAllocSuccessCount=_BCgnatAuthUdpPortAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,14),_BCgnatAuthUdpPortAllocSuccessCount_Type())
bCgnatAuthUdpPortAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUdpPortAllocSuccessCount.setStatus(_A)
_BCgnatAuthIcmpIdAllocFailureCount_Type=Counter64
_BCgnatAuthIcmpIdAllocFailureCount_Object=MibTableColumn
bCgnatAuthIcmpIdAllocFailureCount=_BCgnatAuthIcmpIdAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,15),_BCgnatAuthIcmpIdAllocFailureCount_Type())
bCgnatAuthIcmpIdAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthIcmpIdAllocFailureCount.setStatus(_A)
_BCgnatAuthTcpPortAllocFailureCount_Type=Counter64
_BCgnatAuthTcpPortAllocFailureCount_Object=MibTableColumn
bCgnatAuthTcpPortAllocFailureCount=_BCgnatAuthTcpPortAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,16),_BCgnatAuthTcpPortAllocFailureCount_Type())
bCgnatAuthTcpPortAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthTcpPortAllocFailureCount.setStatus(_A)
_BCgnatAuthUdpPortAllocFailureCount_Type=Counter64
_BCgnatAuthUdpPortAllocFailureCount_Object=MibTableColumn
bCgnatAuthUdpPortAllocFailureCount=_BCgnatAuthUdpPortAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,17),_BCgnatAuthUdpPortAllocFailureCount_Type())
bCgnatAuthUdpPortAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUdpPortAllocFailureCount.setStatus(_A)
_BCgnatAuthIcmpIdReleaseSuccessCount_Type=Counter64
_BCgnatAuthIcmpIdReleaseSuccessCount_Object=MibTableColumn
bCgnatAuthIcmpIdReleaseSuccessCount=_BCgnatAuthIcmpIdReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,18),_BCgnatAuthIcmpIdReleaseSuccessCount_Type())
bCgnatAuthIcmpIdReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthIcmpIdReleaseSuccessCount.setStatus(_A)
_BCgnatAuthTcpPortReleaseSuccessCount_Type=Counter64
_BCgnatAuthTcpPortReleaseSuccessCount_Object=MibTableColumn
bCgnatAuthTcpPortReleaseSuccessCount=_BCgnatAuthTcpPortReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,19),_BCgnatAuthTcpPortReleaseSuccessCount_Type())
bCgnatAuthTcpPortReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthTcpPortReleaseSuccessCount.setStatus(_A)
_BCgnatAuthUdpPortReleaseSuccessCount_Type=Counter64
_BCgnatAuthUdpPortReleaseSuccessCount_Object=MibTableColumn
bCgnatAuthUdpPortReleaseSuccessCount=_BCgnatAuthUdpPortReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,20),_BCgnatAuthUdpPortReleaseSuccessCount_Type())
bCgnatAuthUdpPortReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUdpPortReleaseSuccessCount.setStatus(_A)
_BCgnatAuthIcmpIdReleaseFailureCount_Type=Counter64
_BCgnatAuthIcmpIdReleaseFailureCount_Object=MibTableColumn
bCgnatAuthIcmpIdReleaseFailureCount=_BCgnatAuthIcmpIdReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,21),_BCgnatAuthIcmpIdReleaseFailureCount_Type())
bCgnatAuthIcmpIdReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthIcmpIdReleaseFailureCount.setStatus(_A)
_BCgnatAuthTcpPortReleaseFailureCount_Type=Counter64
_BCgnatAuthTcpPortReleaseFailureCount_Object=MibTableColumn
bCgnatAuthTcpPortReleaseFailureCount=_BCgnatAuthTcpPortReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,22),_BCgnatAuthTcpPortReleaseFailureCount_Type())
bCgnatAuthTcpPortReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthTcpPortReleaseFailureCount.setStatus(_A)
_BCgnatAuthUdpPortReleaseFailureCount_Type=Counter64
_BCgnatAuthUdpPortReleaseFailureCount_Object=MibTableColumn
bCgnatAuthUdpPortReleaseFailureCount=_BCgnatAuthUdpPortReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,23),_BCgnatAuthUdpPortReleaseFailureCount_Type())
bCgnatAuthUdpPortReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUdpPortReleaseFailureCount.setStatus(_A)
_BCgnatAuthMaxCgnatPortsExceeded_Type=Counter64
_BCgnatAuthMaxCgnatPortsExceeded_Object=MibTableColumn
bCgnatAuthMaxCgnatPortsExceeded=_BCgnatAuthMaxCgnatPortsExceeded_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,24),_BCgnatAuthMaxCgnatPortsExceeded_Type())
bCgnatAuthMaxCgnatPortsExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthMaxCgnatPortsExceeded.setStatus(_A)
_BCgnatAuthMaxIcmpIdsExceeded_Type=Counter64
_BCgnatAuthMaxIcmpIdsExceeded_Object=MibTableColumn
bCgnatAuthMaxIcmpIdsExceeded=_BCgnatAuthMaxIcmpIdsExceeded_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,25),_BCgnatAuthMaxIcmpIdsExceeded_Type())
bCgnatAuthMaxIcmpIdsExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthMaxIcmpIdsExceeded.setStatus(_A)
_BCgnatAuthFlowDeleteRcvd_Type=Counter64
_BCgnatAuthFlowDeleteRcvd_Object=MibTableColumn
bCgnatAuthFlowDeleteRcvd=_BCgnatAuthFlowDeleteRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,26),_BCgnatAuthFlowDeleteRcvd_Type())
bCgnatAuthFlowDeleteRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeleteRcvd.setStatus(_A)
_BCgnatAuthFlowDeleteSent_Type=Counter64
_BCgnatAuthFlowDeleteSent_Object=MibTableColumn
bCgnatAuthFlowDeleteSent=_BCgnatAuthFlowDeleteSent_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,27),_BCgnatAuthFlowDeleteSent_Type())
bCgnatAuthFlowDeleteSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeleteSent.setStatus(_A)
_BCgnatAuthFlowDeleteFindFailure_Type=Counter64
_BCgnatAuthFlowDeleteFindFailure_Object=MibTableColumn
bCgnatAuthFlowDeleteFindFailure=_BCgnatAuthFlowDeleteFindFailure_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,28),_BCgnatAuthFlowDeleteFindFailure_Type())
bCgnatAuthFlowDeleteFindFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeleteFindFailure.setStatus(_A)
_BCgnatAuthDnsFlowAlloc_Type=Counter64
_BCgnatAuthDnsFlowAlloc_Object=MibTableColumn
bCgnatAuthDnsFlowAlloc=_BCgnatAuthDnsFlowAlloc_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,29),_BCgnatAuthDnsFlowAlloc_Type())
bCgnatAuthDnsFlowAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowAlloc.setStatus(_A)
_BCgnatAuthDnsFlowRelease_Type=Counter64
_BCgnatAuthDnsFlowRelease_Object=MibTableColumn
bCgnatAuthDnsFlowRelease=_BCgnatAuthDnsFlowRelease_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,30),_BCgnatAuthDnsFlowRelease_Type())
bCgnatAuthDnsFlowRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowRelease.setStatus(_A)
_BCgnatAuthDnsFlowAllocSuccessCount_Type=Counter64
_BCgnatAuthDnsFlowAllocSuccessCount_Object=MibTableColumn
bCgnatAuthDnsFlowAllocSuccessCount=_BCgnatAuthDnsFlowAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,31),_BCgnatAuthDnsFlowAllocSuccessCount_Type())
bCgnatAuthDnsFlowAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowAllocSuccessCount.setStatus(_A)
_BCgnatAuthDnsFlowReleaseSuccessCount_Type=Counter64
_BCgnatAuthDnsFlowReleaseSuccessCount_Object=MibTableColumn
bCgnatAuthDnsFlowReleaseSuccessCount=_BCgnatAuthDnsFlowReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,32),_BCgnatAuthDnsFlowReleaseSuccessCount_Type())
bCgnatAuthDnsFlowReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowReleaseSuccessCount.setStatus(_A)
_BCgnatAuthDnsFlowAllocFailureCount_Type=Counter64
_BCgnatAuthDnsFlowAllocFailureCount_Object=MibTableColumn
bCgnatAuthDnsFlowAllocFailureCount=_BCgnatAuthDnsFlowAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,33),_BCgnatAuthDnsFlowAllocFailureCount_Type())
bCgnatAuthDnsFlowAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowAllocFailureCount.setStatus(_A)
_BCgnatAuthDnsFlowReleaseFailureCount_Type=Counter64
_BCgnatAuthDnsFlowReleaseFailureCount_Object=MibTableColumn
bCgnatAuthDnsFlowReleaseFailureCount=_BCgnatAuthDnsFlowReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,34),_BCgnatAuthDnsFlowReleaseFailureCount_Type())
bCgnatAuthDnsFlowReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthDnsFlowReleaseFailureCount.setStatus(_A)
_BCgnatAuthPortsThresholdExceededSent_Type=Counter64
_BCgnatAuthPortsThresholdExceededSent_Object=MibTableColumn
bCgnatAuthPortsThresholdExceededSent=_BCgnatAuthPortsThresholdExceededSent_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,35),_BCgnatAuthPortsThresholdExceededSent_Type())
bCgnatAuthPortsThresholdExceededSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortsThresholdExceededSent.setStatus(_A)
_BCgnatAuthPortsThresholdExceededRcvd_Type=Counter64
_BCgnatAuthPortsThresholdExceededRcvd_Object=MibTableColumn
bCgnatAuthPortsThresholdExceededRcvd=_BCgnatAuthPortsThresholdExceededRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,36),_BCgnatAuthPortsThresholdExceededRcvd_Type())
bCgnatAuthPortsThresholdExceededRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortsThresholdExceededRcvd.setStatus(_A)
_BCgnatAuthPortsThresholdExceededInt_Type=Counter64
_BCgnatAuthPortsThresholdExceededInt_Object=MibTableColumn
bCgnatAuthPortsThresholdExceededInt=_BCgnatAuthPortsThresholdExceededInt_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,37),_BCgnatAuthPortsThresholdExceededInt_Type())
bCgnatAuthPortsThresholdExceededInt.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortsThresholdExceededInt.setStatus(_A)
_BCgnatAuthPortsThresholdExceededErr_Type=Counter64
_BCgnatAuthPortsThresholdExceededErr_Object=MibTableColumn
bCgnatAuthPortsThresholdExceededErr=_BCgnatAuthPortsThresholdExceededErr_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,38),_BCgnatAuthPortsThresholdExceededErr_Type())
bCgnatAuthPortsThresholdExceededErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortsThresholdExceededErr.setStatus(_A)
_BCgnatAuthUnsupportedActionIdRcvd_Type=Counter64
_BCgnatAuthUnsupportedActionIdRcvd_Object=MibTableColumn
bCgnatAuthUnsupportedActionIdRcvd=_BCgnatAuthUnsupportedActionIdRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,39),_BCgnatAuthUnsupportedActionIdRcvd_Type())
bCgnatAuthUnsupportedActionIdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUnsupportedActionIdRcvd.setStatus(_A)
_BCgnatAuthNonTcpSynPortAllocDrop_Type=Counter64
_BCgnatAuthNonTcpSynPortAllocDrop_Object=MibTableColumn
bCgnatAuthNonTcpSynPortAllocDrop=_BCgnatAuthNonTcpSynPortAllocDrop_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,40),_BCgnatAuthNonTcpSynPortAllocDrop_Type())
bCgnatAuthNonTcpSynPortAllocDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthNonTcpSynPortAllocDrop.setStatus(_A)
_BCgnatAuthFlowDeletedTimer_Type=Counter64
_BCgnatAuthFlowDeletedTimer_Object=MibTableColumn
bCgnatAuthFlowDeletedTimer=_BCgnatAuthFlowDeletedTimer_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,41),_BCgnatAuthFlowDeletedTimer_Type())
bCgnatAuthFlowDeletedTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeletedTimer.setStatus(_A)
_BCgnatAuthFlowDeletedSessionEnded_Type=Counter64
_BCgnatAuthFlowDeletedSessionEnded_Object=MibTableColumn
bCgnatAuthFlowDeletedSessionEnded=_BCgnatAuthFlowDeletedSessionEnded_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,42),_BCgnatAuthFlowDeletedSessionEnded_Type())
bCgnatAuthFlowDeletedSessionEnded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeletedSessionEnded.setStatus(_A)
_BCgnatAuthFlowDeletedSubClear_Type=Counter64
_BCgnatAuthFlowDeletedSubClear_Object=MibTableColumn
bCgnatAuthFlowDeletedSubClear=_BCgnatAuthFlowDeletedSubClear_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,43),_BCgnatAuthFlowDeletedSubClear_Type())
bCgnatAuthFlowDeletedSubClear.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthFlowDeletedSubClear.setStatus(_A)
_BCgnatAuthNatFlowDelErrSubIdMismatch_Type=Counter64
_BCgnatAuthNatFlowDelErrSubIdMismatch_Object=MibTableColumn
bCgnatAuthNatFlowDelErrSubIdMismatch=_BCgnatAuthNatFlowDelErrSubIdMismatch_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,44),_BCgnatAuthNatFlowDelErrSubIdMismatch_Type())
bCgnatAuthNatFlowDelErrSubIdMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthNatFlowDelErrSubIdMismatch.setStatus(_A)
_BCgnatAuthNatFlowDelErrValidFlagNotSet_Type=Counter64
_BCgnatAuthNatFlowDelErrValidFlagNotSet_Object=MibTableColumn
bCgnatAuthNatFlowDelErrValidFlagNotSet=_BCgnatAuthNatFlowDelErrValidFlagNotSet_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,45),_BCgnatAuthNatFlowDelErrValidFlagNotSet_Type())
bCgnatAuthNatFlowDelErrValidFlagNotSet.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthNatFlowDelErrValidFlagNotSet.setStatus(_A)
_BCgnatAuthIcmpPortUnreachableSent_Type=Counter64
_BCgnatAuthIcmpPortUnreachableSent_Object=MibTableColumn
bCgnatAuthIcmpPortUnreachableSent=_BCgnatAuthIcmpPortUnreachableSent_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,46),_BCgnatAuthIcmpPortUnreachableSent_Type())
bCgnatAuthIcmpPortUnreachableSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthIcmpPortUnreachableSent.setStatus(_A)
_BCgnatAuthPortsNotAvailableDrop_Type=Counter64
_BCgnatAuthPortsNotAvailableDrop_Object=MibTableColumn
bCgnatAuthPortsNotAvailableDrop=_BCgnatAuthPortsNotAvailableDrop_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,47),_BCgnatAuthPortsNotAvailableDrop_Type())
bCgnatAuthPortsNotAvailableDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortsNotAvailableDrop.setStatus(_A)
_BCgnatAuthUnsupportedPrivatePortDropCount_Type=Counter64
_BCgnatAuthUnsupportedPrivatePortDropCount_Object=MibTableColumn
bCgnatAuthUnsupportedPrivatePortDropCount=_BCgnatAuthUnsupportedPrivatePortDropCount_Object((1,3,6,1,4,1,39406,2,1,9,1,1,1,48),_BCgnatAuthUnsupportedPrivatePortDropCount_Type())
bCgnatAuthUnsupportedPrivatePortDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthUnsupportedPrivatePortDropCount.setStatus(_A)
_BCgnatUnauthStatsTable_Object=MibTable
bCgnatUnauthStatsTable=_BCgnatUnauthStatsTable_Object((1,3,6,1,4,1,39406,2,1,9,1,2))
if mibBuilder.loadTexts:bCgnatUnauthStatsTable.setStatus(_A)
_BCgnatUnauthStatsEntry_Object=MibTableRow
bCgnatUnauthStatsEntry=_BCgnatUnauthStatsEntry_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1))
bCgnatUnauthStatsEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:bCgnatUnauthStatsEntry.setStatus(_A)
_BCgnatUnauthStatsIndex_Type=Integer32
_BCgnatUnauthStatsIndex_Object=MibTableColumn
bCgnatUnauthStatsIndex=_BCgnatUnauthStatsIndex_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,1),_BCgnatUnauthStatsIndex_Type())
bCgnatUnauthStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bCgnatUnauthStatsIndex.setStatus(_A)
_BCgnatUnauthProfileName_Type=DisplayString
_BCgnatUnauthProfileName_Object=MibTableColumn
bCgnatUnauthProfileName=_BCgnatUnauthProfileName_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,2),_BCgnatUnauthProfileName_Type())
bCgnatUnauthProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthProfileName.setStatus(_A)
_BCgnatUnauthDomainPublicIpZeroCount_Type=Counter64
_BCgnatUnauthDomainPublicIpZeroCount_Object=MibTableColumn
bCgnatUnauthDomainPublicIpZeroCount=_BCgnatUnauthDomainPublicIpZeroCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,3),_BCgnatUnauthDomainPublicIpZeroCount_Type())
bCgnatUnauthDomainPublicIpZeroCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDomainPublicIpZeroCount.setStatus(_A)
_BCgnatUnauthDomainNoFreePortCount_Type=Counter64
_BCgnatUnauthDomainNoFreePortCount_Object=MibTableColumn
bCgnatUnauthDomainNoFreePortCount=_BCgnatUnauthDomainNoFreePortCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,4),_BCgnatUnauthDomainNoFreePortCount_Type())
bCgnatUnauthDomainNoFreePortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDomainNoFreePortCount.setStatus(_A)
_BCgnatUnauthFlowAddSuccessCount_Type=Counter64
_BCgnatUnauthFlowAddSuccessCount_Object=MibTableColumn
bCgnatUnauthFlowAddSuccessCount=_BCgnatUnauthFlowAddSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,5),_BCgnatUnauthFlowAddSuccessCount_Type())
bCgnatUnauthFlowAddSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowAddSuccessCount.setStatus(_A)
_BCgnatUnauthFlowAddFailureCount_Type=Counter64
_BCgnatUnauthFlowAddFailureCount_Object=MibTableColumn
bCgnatUnauthFlowAddFailureCount=_BCgnatUnauthFlowAddFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,6),_BCgnatUnauthFlowAddFailureCount_Type())
bCgnatUnauthFlowAddFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowAddFailureCount.setStatus(_A)
_BCgnatUnauthTimerAllocFailureCount_Type=Counter64
_BCgnatUnauthTimerAllocFailureCount_Object=MibTableColumn
bCgnatUnauthTimerAllocFailureCount=_BCgnatUnauthTimerAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,7),_BCgnatUnauthTimerAllocFailureCount_Type())
bCgnatUnauthTimerAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthTimerAllocFailureCount.setStatus(_A)
_BCgnatUnauthFlowDeleteSuccessCount_Type=Counter64
_BCgnatUnauthFlowDeleteSuccessCount_Object=MibTableColumn
bCgnatUnauthFlowDeleteSuccessCount=_BCgnatUnauthFlowDeleteSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,8),_BCgnatUnauthFlowDeleteSuccessCount_Type())
bCgnatUnauthFlowDeleteSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeleteSuccessCount.setStatus(_A)
_BCgnatUnauthFlowDeleteFailureCount_Type=Counter64
_BCgnatUnauthFlowDeleteFailureCount_Object=MibTableColumn
bCgnatUnauthFlowDeleteFailureCount=_BCgnatUnauthFlowDeleteFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,9),_BCgnatUnauthFlowDeleteFailureCount_Type())
bCgnatUnauthFlowDeleteFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeleteFailureCount.setStatus(_A)
_BCgnatUnauthUnsupportedL4DropCount_Type=Counter64
_BCgnatUnauthUnsupportedL4DropCount_Object=MibTableColumn
bCgnatUnauthUnsupportedL4DropCount=_BCgnatUnauthUnsupportedL4DropCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,10),_BCgnatUnauthUnsupportedL4DropCount_Type())
bCgnatUnauthUnsupportedL4DropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUnsupportedL4DropCount.setStatus(_A)
_BCgnatUnauthNatflowSyncFailureCount_Type=Counter64
_BCgnatUnauthNatflowSyncFailureCount_Object=MibTableColumn
bCgnatUnauthNatflowSyncFailureCount=_BCgnatUnauthNatflowSyncFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,11),_BCgnatUnauthNatflowSyncFailureCount_Type())
bCgnatUnauthNatflowSyncFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthNatflowSyncFailureCount.setStatus(_A)
_BCgnatUnauthIcmpIdAllocSuccessCount_Type=Counter64
_BCgnatUnauthIcmpIdAllocSuccessCount_Object=MibTableColumn
bCgnatUnauthIcmpIdAllocSuccessCount=_BCgnatUnauthIcmpIdAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,12),_BCgnatUnauthIcmpIdAllocSuccessCount_Type())
bCgnatUnauthIcmpIdAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthIcmpIdAllocSuccessCount.setStatus(_A)
_BCgnatUnauthTcpPortAllocSuccessCount_Type=Counter64
_BCgnatUnauthTcpPortAllocSuccessCount_Object=MibTableColumn
bCgnatUnauthTcpPortAllocSuccessCount=_BCgnatUnauthTcpPortAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,13),_BCgnatUnauthTcpPortAllocSuccessCount_Type())
bCgnatUnauthTcpPortAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthTcpPortAllocSuccessCount.setStatus(_A)
_BCgnatUnauthUdpPortAllocSuccessCount_Type=Counter64
_BCgnatUnauthUdpPortAllocSuccessCount_Object=MibTableColumn
bCgnatUnauthUdpPortAllocSuccessCount=_BCgnatUnauthUdpPortAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,14),_BCgnatUnauthUdpPortAllocSuccessCount_Type())
bCgnatUnauthUdpPortAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUdpPortAllocSuccessCount.setStatus(_A)
_BCgnatUnauthIcmpIdAllocFailureCount_Type=Counter64
_BCgnatUnauthIcmpIdAllocFailureCount_Object=MibTableColumn
bCgnatUnauthIcmpIdAllocFailureCount=_BCgnatUnauthIcmpIdAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,15),_BCgnatUnauthIcmpIdAllocFailureCount_Type())
bCgnatUnauthIcmpIdAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthIcmpIdAllocFailureCount.setStatus(_A)
_BCgnatUnauthTcpPortAllocFailureCount_Type=Counter64
_BCgnatUnauthTcpPortAllocFailureCount_Object=MibTableColumn
bCgnatUnauthTcpPortAllocFailureCount=_BCgnatUnauthTcpPortAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,16),_BCgnatUnauthTcpPortAllocFailureCount_Type())
bCgnatUnauthTcpPortAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthTcpPortAllocFailureCount.setStatus(_A)
_BCgnatUnauthUdpPortAllocFailureCount_Type=Counter64
_BCgnatUnauthUdpPortAllocFailureCount_Object=MibTableColumn
bCgnatUnauthUdpPortAllocFailureCount=_BCgnatUnauthUdpPortAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,17),_BCgnatUnauthUdpPortAllocFailureCount_Type())
bCgnatUnauthUdpPortAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUdpPortAllocFailureCount.setStatus(_A)
_BCgnatUnauthIcmpIdReleaseSuccessCount_Type=Counter64
_BCgnatUnauthIcmpIdReleaseSuccessCount_Object=MibTableColumn
bCgnatUnauthIcmpIdReleaseSuccessCount=_BCgnatUnauthIcmpIdReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,18),_BCgnatUnauthIcmpIdReleaseSuccessCount_Type())
bCgnatUnauthIcmpIdReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthIcmpIdReleaseSuccessCount.setStatus(_A)
_BCgnatUnauthTcpPortReleaseSuccessCount_Type=Counter64
_BCgnatUnauthTcpPortReleaseSuccessCount_Object=MibTableColumn
bCgnatUnauthTcpPortReleaseSuccessCount=_BCgnatUnauthTcpPortReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,19),_BCgnatUnauthTcpPortReleaseSuccessCount_Type())
bCgnatUnauthTcpPortReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthTcpPortReleaseSuccessCount.setStatus(_A)
_BCgnatUnauthUdpPortReleaseSuccessCount_Type=Counter64
_BCgnatUnauthUdpPortReleaseSuccessCount_Object=MibTableColumn
bCgnatUnauthUdpPortReleaseSuccessCount=_BCgnatUnauthUdpPortReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,20),_BCgnatUnauthUdpPortReleaseSuccessCount_Type())
bCgnatUnauthUdpPortReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUdpPortReleaseSuccessCount.setStatus(_A)
_BCgnatUnauthIcmpIdReleaseFailureCount_Type=Counter64
_BCgnatUnauthIcmpIdReleaseFailureCount_Object=MibTableColumn
bCgnatUnauthIcmpIdReleaseFailureCount=_BCgnatUnauthIcmpIdReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,21),_BCgnatUnauthIcmpIdReleaseFailureCount_Type())
bCgnatUnauthIcmpIdReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthIcmpIdReleaseFailureCount.setStatus(_A)
_BCgnatUnauthTcpPortReleaseFailureCount_Type=Counter64
_BCgnatUnauthTcpPortReleaseFailureCount_Object=MibTableColumn
bCgnatUnauthTcpPortReleaseFailureCount=_BCgnatUnauthTcpPortReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,22),_BCgnatUnauthTcpPortReleaseFailureCount_Type())
bCgnatUnauthTcpPortReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthTcpPortReleaseFailureCount.setStatus(_A)
_BCgnatUnauthUdpPortReleaseFailureCount_Type=Counter64
_BCgnatUnauthUdpPortReleaseFailureCount_Object=MibTableColumn
bCgnatUnauthUdpPortReleaseFailureCount=_BCgnatUnauthUdpPortReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,23),_BCgnatUnauthUdpPortReleaseFailureCount_Type())
bCgnatUnauthUdpPortReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUdpPortReleaseFailureCount.setStatus(_A)
_BCgnatUnauthMaxCgnatPortsExceeded_Type=Counter64
_BCgnatUnauthMaxCgnatPortsExceeded_Object=MibTableColumn
bCgnatUnauthMaxCgnatPortsExceeded=_BCgnatUnauthMaxCgnatPortsExceeded_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,24),_BCgnatUnauthMaxCgnatPortsExceeded_Type())
bCgnatUnauthMaxCgnatPortsExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthMaxCgnatPortsExceeded.setStatus(_A)
_BCgnatUnauthMaxIcmpIdsExceeded_Type=Counter64
_BCgnatUnauthMaxIcmpIdsExceeded_Object=MibTableColumn
bCgnatUnauthMaxIcmpIdsExceeded=_BCgnatUnauthMaxIcmpIdsExceeded_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,25),_BCgnatUnauthMaxIcmpIdsExceeded_Type())
bCgnatUnauthMaxIcmpIdsExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthMaxIcmpIdsExceeded.setStatus(_A)
_BCgnatUnauthFlowDeleteRcvd_Type=Counter64
_BCgnatUnauthFlowDeleteRcvd_Object=MibTableColumn
bCgnatUnauthFlowDeleteRcvd=_BCgnatUnauthFlowDeleteRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,26),_BCgnatUnauthFlowDeleteRcvd_Type())
bCgnatUnauthFlowDeleteRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeleteRcvd.setStatus(_A)
_BCgnatUnauthFlowDeleteSent_Type=Counter64
_BCgnatUnauthFlowDeleteSent_Object=MibTableColumn
bCgnatUnauthFlowDeleteSent=_BCgnatUnauthFlowDeleteSent_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,27),_BCgnatUnauthFlowDeleteSent_Type())
bCgnatUnauthFlowDeleteSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeleteSent.setStatus(_A)
_BCgnatUnauthFlowDeleteFindFailure_Type=Counter64
_BCgnatUnauthFlowDeleteFindFailure_Object=MibTableColumn
bCgnatUnauthFlowDeleteFindFailure=_BCgnatUnauthFlowDeleteFindFailure_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,28),_BCgnatUnauthFlowDeleteFindFailure_Type())
bCgnatUnauthFlowDeleteFindFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeleteFindFailure.setStatus(_A)
_BCgnatUnauthDnsFlowAlloc_Type=Counter64
_BCgnatUnauthDnsFlowAlloc_Object=MibTableColumn
bCgnatUnauthDnsFlowAlloc=_BCgnatUnauthDnsFlowAlloc_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,29),_BCgnatUnauthDnsFlowAlloc_Type())
bCgnatUnauthDnsFlowAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowAlloc.setStatus(_A)
_BCgnatUnauthDnsFlowRelease_Type=Counter64
_BCgnatUnauthDnsFlowRelease_Object=MibTableColumn
bCgnatUnauthDnsFlowRelease=_BCgnatUnauthDnsFlowRelease_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,30),_BCgnatUnauthDnsFlowRelease_Type())
bCgnatUnauthDnsFlowRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowRelease.setStatus(_A)
_BCgnatUnauthDnsFlowAllocSuccessCount_Type=Counter64
_BCgnatUnauthDnsFlowAllocSuccessCount_Object=MibTableColumn
bCgnatUnauthDnsFlowAllocSuccessCount=_BCgnatUnauthDnsFlowAllocSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,31),_BCgnatUnauthDnsFlowAllocSuccessCount_Type())
bCgnatUnauthDnsFlowAllocSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowAllocSuccessCount.setStatus(_A)
_BCgnatUnauthDnsFlowReleaseSuccessCount_Type=Counter64
_BCgnatUnauthDnsFlowReleaseSuccessCount_Object=MibTableColumn
bCgnatUnauthDnsFlowReleaseSuccessCount=_BCgnatUnauthDnsFlowReleaseSuccessCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,32),_BCgnatUnauthDnsFlowReleaseSuccessCount_Type())
bCgnatUnauthDnsFlowReleaseSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowReleaseSuccessCount.setStatus(_A)
_BCgnatUnauthDnsFlowAllocFailureCount_Type=Counter64
_BCgnatUnauthDnsFlowAllocFailureCount_Object=MibTableColumn
bCgnatUnauthDnsFlowAllocFailureCount=_BCgnatUnauthDnsFlowAllocFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,33),_BCgnatUnauthDnsFlowAllocFailureCount_Type())
bCgnatUnauthDnsFlowAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowAllocFailureCount.setStatus(_A)
_BCgnatUnauthDnsFlowReleaseFailureCount_Type=Counter64
_BCgnatUnauthDnsFlowReleaseFailureCount_Object=MibTableColumn
bCgnatUnauthDnsFlowReleaseFailureCount=_BCgnatUnauthDnsFlowReleaseFailureCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,34),_BCgnatUnauthDnsFlowReleaseFailureCount_Type())
bCgnatUnauthDnsFlowReleaseFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthDnsFlowReleaseFailureCount.setStatus(_A)
_BCgnatUnauthPortsThresholdExceededSent_Type=Counter64
_BCgnatUnauthPortsThresholdExceededSent_Object=MibTableColumn
bCgnatUnauthPortsThresholdExceededSent=_BCgnatUnauthPortsThresholdExceededSent_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,35),_BCgnatUnauthPortsThresholdExceededSent_Type())
bCgnatUnauthPortsThresholdExceededSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthPortsThresholdExceededSent.setStatus(_A)
_BCgnatUnauthPortsThresholdExceededRcvd_Type=Counter64
_BCgnatUnauthPortsThresholdExceededRcvd_Object=MibTableColumn
bCgnatUnauthPortsThresholdExceededRcvd=_BCgnatUnauthPortsThresholdExceededRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,36),_BCgnatUnauthPortsThresholdExceededRcvd_Type())
bCgnatUnauthPortsThresholdExceededRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthPortsThresholdExceededRcvd.setStatus(_A)
_BCgnatUnauthPortsThresholdExceededInt_Type=Counter64
_BCgnatUnauthPortsThresholdExceededInt_Object=MibTableColumn
bCgnatUnauthPortsThresholdExceededInt=_BCgnatUnauthPortsThresholdExceededInt_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,37),_BCgnatUnauthPortsThresholdExceededInt_Type())
bCgnatUnauthPortsThresholdExceededInt.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthPortsThresholdExceededInt.setStatus(_A)
_BCgnatUnauthPortsThresholdExceededErr_Type=Counter64
_BCgnatUnauthPortsThresholdExceededErr_Object=MibTableColumn
bCgnatUnauthPortsThresholdExceededErr=_BCgnatUnauthPortsThresholdExceededErr_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,38),_BCgnatUnauthPortsThresholdExceededErr_Type())
bCgnatUnauthPortsThresholdExceededErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthPortsThresholdExceededErr.setStatus(_A)
_BCgnatUnauthUnsupportedActionIdRcvd_Type=Counter64
_BCgnatUnauthUnsupportedActionIdRcvd_Object=MibTableColumn
bCgnatUnauthUnsupportedActionIdRcvd=_BCgnatUnauthUnsupportedActionIdRcvd_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,39),_BCgnatUnauthUnsupportedActionIdRcvd_Type())
bCgnatUnauthUnsupportedActionIdRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUnsupportedActionIdRcvd.setStatus(_A)
_BCgnatUnauthNonTcpSynPortAllocDrop_Type=Counter64
_BCgnatUnauthNonTcpSynPortAllocDrop_Object=MibTableColumn
bCgnatUnauthNonTcpSynPortAllocDrop=_BCgnatUnauthNonTcpSynPortAllocDrop_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,40),_BCgnatUnauthNonTcpSynPortAllocDrop_Type())
bCgnatUnauthNonTcpSynPortAllocDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthNonTcpSynPortAllocDrop.setStatus(_A)
_BCgnatUnauthFlowDeletedTimer_Type=Counter64
_BCgnatUnauthFlowDeletedTimer_Object=MibTableColumn
bCgnatUnauthFlowDeletedTimer=_BCgnatUnauthFlowDeletedTimer_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,41),_BCgnatUnauthFlowDeletedTimer_Type())
bCgnatUnauthFlowDeletedTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeletedTimer.setStatus(_A)
_BCgnatUnauthFlowDeletedSessionEnded_Type=Counter64
_BCgnatUnauthFlowDeletedSessionEnded_Object=MibTableColumn
bCgnatUnauthFlowDeletedSessionEnded=_BCgnatUnauthFlowDeletedSessionEnded_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,42),_BCgnatUnauthFlowDeletedSessionEnded_Type())
bCgnatUnauthFlowDeletedSessionEnded.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeletedSessionEnded.setStatus(_A)
_BCgnatUnauthFlowDeletedSubClear_Type=Counter64
_BCgnatUnauthFlowDeletedSubClear_Object=MibTableColumn
bCgnatUnauthFlowDeletedSubClear=_BCgnatUnauthFlowDeletedSubClear_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,43),_BCgnatUnauthFlowDeletedSubClear_Type())
bCgnatUnauthFlowDeletedSubClear.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthFlowDeletedSubClear.setStatus(_A)
_BCgnatUnauthNatFlowDelErrSubIdMismatch_Type=Counter64
_BCgnatUnauthNatFlowDelErrSubIdMismatch_Object=MibTableColumn
bCgnatUnauthNatFlowDelErrSubIdMismatch=_BCgnatUnauthNatFlowDelErrSubIdMismatch_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,44),_BCgnatUnauthNatFlowDelErrSubIdMismatch_Type())
bCgnatUnauthNatFlowDelErrSubIdMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthNatFlowDelErrSubIdMismatch.setStatus(_A)
_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Type=Counter64
_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Object=MibTableColumn
bCgnatUnauthNatFlowDelErrValidFlagNotSet=_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,45),_BCgnatUnauthNatFlowDelErrValidFlagNotSet_Type())
bCgnatUnauthNatFlowDelErrValidFlagNotSet.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthNatFlowDelErrValidFlagNotSet.setStatus(_A)
_BCgnatUnauthIcmpPortUnreachableSent_Type=Counter64
_BCgnatUnauthIcmpPortUnreachableSent_Object=MibTableColumn
bCgnatUnauthIcmpPortUnreachableSent=_BCgnatUnauthIcmpPortUnreachableSent_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,46),_BCgnatUnauthIcmpPortUnreachableSent_Type())
bCgnatUnauthIcmpPortUnreachableSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthIcmpPortUnreachableSent.setStatus(_A)
_BCgnatUnauthPortsNotAvailableDrop_Type=Counter64
_BCgnatUnauthPortsNotAvailableDrop_Object=MibTableColumn
bCgnatUnauthPortsNotAvailableDrop=_BCgnatUnauthPortsNotAvailableDrop_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,47),_BCgnatUnauthPortsNotAvailableDrop_Type())
bCgnatUnauthPortsNotAvailableDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthPortsNotAvailableDrop.setStatus(_A)
_BCgnatUnauthUnsupportedPrivatePortDropCount_Type=Counter64
_BCgnatUnauthUnsupportedPrivatePortDropCount_Object=MibTableColumn
bCgnatUnauthUnsupportedPrivatePortDropCount=_BCgnatUnauthUnsupportedPrivatePortDropCount_Object((1,3,6,1,4,1,39406,2,1,9,1,2,1,48),_BCgnatUnauthUnsupportedPrivatePortDropCount_Type())
bCgnatUnauthUnsupportedPrivatePortDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatUnauthUnsupportedPrivatePortDropCount.setStatus(_A)
_BCgnatAuthPortUtilTable_Object=MibTable
bCgnatAuthPortUtilTable=_BCgnatAuthPortUtilTable_Object((1,3,6,1,4,1,39406,2,1,9,1,3))
if mibBuilder.loadTexts:bCgnatAuthPortUtilTable.setStatus(_A)
_BCgnatAuthPortUtilEntry_Object=MibTableRow
bCgnatAuthPortUtilEntry=_BCgnatAuthPortUtilEntry_Object((1,3,6,1,4,1,39406,2,1,9,1,3,1))
bCgnatAuthPortUtilEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:bCgnatAuthPortUtilEntry.setStatus(_A)
_BCgnatAuthPortUtilIndex_Type=Unsigned32
_BCgnatAuthPortUtilIndex_Object=MibTableColumn
bCgnatAuthPortUtilIndex=_BCgnatAuthPortUtilIndex_Object((1,3,6,1,4,1,39406,2,1,9,1,3,1,1),_BCgnatAuthPortUtilIndex_Type())
bCgnatAuthPortUtilIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bCgnatAuthPortUtilIndex.setStatus(_A)
_BCgnatAuthSubscriberMac_Type=MacAddress
_BCgnatAuthSubscriberMac_Object=MibTableColumn
bCgnatAuthSubscriberMac=_BCgnatAuthSubscriberMac_Object((1,3,6,1,4,1,39406,2,1,9,1,3,1,2),_BCgnatAuthSubscriberMac_Type())
bCgnatAuthSubscriberMac.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthSubscriberMac.setStatus(_A)
_BCgnatAuthSubscriberPortsFree_Type=Unsigned32
_BCgnatAuthSubscriberPortsFree_Object=MibTableColumn
bCgnatAuthSubscriberPortsFree=_BCgnatAuthSubscriberPortsFree_Object((1,3,6,1,4,1,39406,2,1,9,1,3,1,3),_BCgnatAuthSubscriberPortsFree_Type())
bCgnatAuthSubscriberPortsFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthSubscriberPortsFree.setStatus(_A)
_BCgnatAuthPortRisingThresholdCrossedSubCount_Type=Unsigned32
_BCgnatAuthPortRisingThresholdCrossedSubCount_Object=MibScalar
bCgnatAuthPortRisingThresholdCrossedSubCount=_BCgnatAuthPortRisingThresholdCrossedSubCount_Object((1,3,6,1,4,1,39406,2,1,9,1,4),_BCgnatAuthPortRisingThresholdCrossedSubCount_Type())
bCgnatAuthPortRisingThresholdCrossedSubCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bCgnatAuthPortRisingThresholdCrossedSubCount.setStatus(_A)
_BDslitePortBlockRisingThresholdCrossedTunCount_Type=Unsigned32
_BDslitePortBlockRisingThresholdCrossedTunCount_Object=MibScalar
bDslitePortBlockRisingThresholdCrossedTunCount=_BDslitePortBlockRisingThresholdCrossedTunCount_Object((1,3,6,1,4,1,39406,2,1,9,1,5),_BDslitePortBlockRisingThresholdCrossedTunCount_Type())
bDslitePortBlockRisingThresholdCrossedTunCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bDslitePortBlockRisingThresholdCrossedTunCount.setStatus(_A)
_BCgnatNotifObjects_ObjectIdentity=ObjectIdentity
bCgnatNotifObjects=_BCgnatNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,9,2))
if mibBuilder.loadTexts:bCgnatNotifObjects.setStatus(_A)
_BCgnatSubscriberMac_Type=MacAddress
_BCgnatSubscriberMac_Object=MibScalar
bCgnatSubscriberMac=_BCgnatSubscriberMac_Object((1,3,6,1,4,1,39406,2,1,9,2,1),_BCgnatSubscriberMac_Type())
bCgnatSubscriberMac.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatSubscriberMac.setStatus(_A)
_BCgnatTotalPortBlocksPerSubscriber_Type=Unsigned32
_BCgnatTotalPortBlocksPerSubscriber_Object=MibScalar
bCgnatTotalPortBlocksPerSubscriber=_BCgnatTotalPortBlocksPerSubscriber_Object((1,3,6,1,4,1,39406,2,1,9,2,2),_BCgnatTotalPortBlocksPerSubscriber_Type())
bCgnatTotalPortBlocksPerSubscriber.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatTotalPortBlocksPerSubscriber.setStatus(_A)
_BCgnatPortBlocksUsedHighThreshold_Type=Unsigned32
_BCgnatPortBlocksUsedHighThreshold_Object=MibScalar
bCgnatPortBlocksUsedHighThreshold=_BCgnatPortBlocksUsedHighThreshold_Object((1,3,6,1,4,1,39406,2,1,9,2,3),_BCgnatPortBlocksUsedHighThreshold_Type())
bCgnatPortBlocksUsedHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatPortBlocksUsedHighThreshold.setStatus(_A)
_BCgnatPortBlocksUsedLowThreshold_Type=Unsigned32
_BCgnatPortBlocksUsedLowThreshold_Object=MibScalar
bCgnatPortBlocksUsedLowThreshold=_BCgnatPortBlocksUsedLowThreshold_Object((1,3,6,1,4,1,39406,2,1,9,2,4),_BCgnatPortBlocksUsedLowThreshold_Type())
bCgnatPortBlocksUsedLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatPortBlocksUsedLowThreshold.setStatus(_A)
_BCgnatThresholdTunnelId_Type=Unsigned32
_BCgnatThresholdTunnelId_Object=MibScalar
bCgnatThresholdTunnelId=_BCgnatThresholdTunnelId_Object((1,3,6,1,4,1,39406,2,1,9,2,5),_BCgnatThresholdTunnelId_Type())
bCgnatThresholdTunnelId.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatThresholdTunnelId.setStatus(_A)
_BCgnatEvenPortsForTunnel_Type=Unsigned32
_BCgnatEvenPortsForTunnel_Object=MibScalar
bCgnatEvenPortsForTunnel=_BCgnatEvenPortsForTunnel_Object((1,3,6,1,4,1,39406,2,1,9,2,6),_BCgnatEvenPortsForTunnel_Type())
bCgnatEvenPortsForTunnel.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatEvenPortsForTunnel.setStatus(_A)
_BCgnatOddPortsForTunnel_Type=Unsigned32
_BCgnatOddPortsForTunnel_Object=MibScalar
bCgnatOddPortsForTunnel=_BCgnatOddPortsForTunnel_Object((1,3,6,1,4,1,39406,2,1,9,2,7),_BCgnatOddPortsForTunnel_Type())
bCgnatOddPortsForTunnel.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatOddPortsForTunnel.setStatus(_A)
_BCgnatPortParity_Type=Unsigned32
_BCgnatPortParity_Object=MibScalar
bCgnatPortParity=_BCgnatPortParity_Object((1,3,6,1,4,1,39406,2,1,9,2,8),_BCgnatPortParity_Type())
bCgnatPortParity.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatPortParity.setStatus(_A)
_BCgnatTunnelPortBlocksUsedHighThreshold_Type=Unsigned32
_BCgnatTunnelPortBlocksUsedHighThreshold_Object=MibScalar
bCgnatTunnelPortBlocksUsedHighThreshold=_BCgnatTunnelPortBlocksUsedHighThreshold_Object((1,3,6,1,4,1,39406,2,1,9,2,9),_BCgnatTunnelPortBlocksUsedHighThreshold_Type())
bCgnatTunnelPortBlocksUsedHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatTunnelPortBlocksUsedHighThreshold.setStatus(_A)
_BCgnatTunnelPortBlocksUsedLowThreshold_Type=Unsigned32
_BCgnatTunnelPortBlocksUsedLowThreshold_Object=MibScalar
bCgnatTunnelPortBlocksUsedLowThreshold=_BCgnatTunnelPortBlocksUsedLowThreshold_Object((1,3,6,1,4,1,39406,2,1,9,2,10),_BCgnatTunnelPortBlocksUsedLowThreshold_Type())
bCgnatTunnelPortBlocksUsedLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bCgnatTunnelPortBlocksUsedLowThreshold.setStatus(_A)
bCgnatPortBlocksUsedHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,9,0,1))
bCgnatPortBlocksUsedHighThresholdReached.setObjects(*((_C,_F),(_C,_G),(_C,_O)))
if mibBuilder.loadTexts:bCgnatPortBlocksUsedHighThresholdReached.setStatus(_A)
bCgnatPortBlocksUsedLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,9,0,2))
bCgnatPortBlocksUsedLowThresholdReached.setObjects(*((_C,_F),(_C,_G),(_C,_P)))
if mibBuilder.loadTexts:bCgnatPortBlocksUsedLowThresholdReached.setStatus(_A)
bCgnatTunnelPortBlocksUsedHighThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,9,0,3))
bCgnatTunnelPortBlocksUsedHighThresholdReached.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_Q)))
if mibBuilder.loadTexts:bCgnatTunnelPortBlocksUsedHighThresholdReached.setStatus(_A)
bCgnatTunnelPortBlocksUsedLowThresholdReached=NotificationType((1,3,6,1,4,1,39406,2,1,9,0,4))
bCgnatTunnelPortBlocksUsedLowThresholdReached.setObjects(*((_C,_H),(_C,_I),(_C,_J),(_C,_K),(_C,_R)))
if mibBuilder.loadTexts:bCgnatTunnelPortBlocksUsedLowThresholdReached.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'benuCgnatStatsMIB':benuCgnatStatsMIB,'bCgnatNotifications':bCgnatNotifications,'bCgnatPortBlocksUsedHighThresholdReached':bCgnatPortBlocksUsedHighThresholdReached,'bCgnatPortBlocksUsedLowThresholdReached':bCgnatPortBlocksUsedLowThresholdReached,'bCgnatTunnelPortBlocksUsedHighThresholdReached':bCgnatTunnelPortBlocksUsedHighThresholdReached,'bCgnatTunnelPortBlocksUsedLowThresholdReached':bCgnatTunnelPortBlocksUsedLowThresholdReached,'bCgnatMIBObjects':bCgnatMIBObjects,'bCgnatAuthStatsTable':bCgnatAuthStatsTable,'bCgnatAuthStatsEntry':bCgnatAuthStatsEntry,_L:bCgnatAuthStatsIndex,'bCgnatAuthProfileName':bCgnatAuthProfileName,'bCgnatAuthDomainPublicIpZeroCount':bCgnatAuthDomainPublicIpZeroCount,'bCgnatAuthDomainNoFreePortCount':bCgnatAuthDomainNoFreePortCount,'bCgnatAuthFlowAddSuccessCount':bCgnatAuthFlowAddSuccessCount,'bCgnatAuthFlowAddFailureCount':bCgnatAuthFlowAddFailureCount,'bCgnatAuthTimerAllocFailureCount':bCgnatAuthTimerAllocFailureCount,'bCgnatAuthFlowDeleteSuccessCount':bCgnatAuthFlowDeleteSuccessCount,'bCgnatAuthFlowDeleteFailureCount':bCgnatAuthFlowDeleteFailureCount,'bCgnatAuthUnsupportedL4DropCount':bCgnatAuthUnsupportedL4DropCount,'bCgnatAuthNatflowSyncFailureCount':bCgnatAuthNatflowSyncFailureCount,'bCgnatAuthIcmpIdAllocSuccessCount':bCgnatAuthIcmpIdAllocSuccessCount,'bCgnatAuthTcpPortAllocSuccessCount':bCgnatAuthTcpPortAllocSuccessCount,'bCgnatAuthUdpPortAllocSuccessCount':bCgnatAuthUdpPortAllocSuccessCount,'bCgnatAuthIcmpIdAllocFailureCount':bCgnatAuthIcmpIdAllocFailureCount,'bCgnatAuthTcpPortAllocFailureCount':bCgnatAuthTcpPortAllocFailureCount,'bCgnatAuthUdpPortAllocFailureCount':bCgnatAuthUdpPortAllocFailureCount,'bCgnatAuthIcmpIdReleaseSuccessCount':bCgnatAuthIcmpIdReleaseSuccessCount,'bCgnatAuthTcpPortReleaseSuccessCount':bCgnatAuthTcpPortReleaseSuccessCount,'bCgnatAuthUdpPortReleaseSuccessCount':bCgnatAuthUdpPortReleaseSuccessCount,'bCgnatAuthIcmpIdReleaseFailureCount':bCgnatAuthIcmpIdReleaseFailureCount,'bCgnatAuthTcpPortReleaseFailureCount':bCgnatAuthTcpPortReleaseFailureCount,'bCgnatAuthUdpPortReleaseFailureCount':bCgnatAuthUdpPortReleaseFailureCount,'bCgnatAuthMaxCgnatPortsExceeded':bCgnatAuthMaxCgnatPortsExceeded,'bCgnatAuthMaxIcmpIdsExceeded':bCgnatAuthMaxIcmpIdsExceeded,'bCgnatAuthFlowDeleteRcvd':bCgnatAuthFlowDeleteRcvd,'bCgnatAuthFlowDeleteSent':bCgnatAuthFlowDeleteSent,'bCgnatAuthFlowDeleteFindFailure':bCgnatAuthFlowDeleteFindFailure,'bCgnatAuthDnsFlowAlloc':bCgnatAuthDnsFlowAlloc,'bCgnatAuthDnsFlowRelease':bCgnatAuthDnsFlowRelease,'bCgnatAuthDnsFlowAllocSuccessCount':bCgnatAuthDnsFlowAllocSuccessCount,'bCgnatAuthDnsFlowReleaseSuccessCount':bCgnatAuthDnsFlowReleaseSuccessCount,'bCgnatAuthDnsFlowAllocFailureCount':bCgnatAuthDnsFlowAllocFailureCount,'bCgnatAuthDnsFlowReleaseFailureCount':bCgnatAuthDnsFlowReleaseFailureCount,'bCgnatAuthPortsThresholdExceededSent':bCgnatAuthPortsThresholdExceededSent,'bCgnatAuthPortsThresholdExceededRcvd':bCgnatAuthPortsThresholdExceededRcvd,'bCgnatAuthPortsThresholdExceededInt':bCgnatAuthPortsThresholdExceededInt,'bCgnatAuthPortsThresholdExceededErr':bCgnatAuthPortsThresholdExceededErr,'bCgnatAuthUnsupportedActionIdRcvd':bCgnatAuthUnsupportedActionIdRcvd,'bCgnatAuthNonTcpSynPortAllocDrop':bCgnatAuthNonTcpSynPortAllocDrop,'bCgnatAuthFlowDeletedTimer':bCgnatAuthFlowDeletedTimer,'bCgnatAuthFlowDeletedSessionEnded':bCgnatAuthFlowDeletedSessionEnded,'bCgnatAuthFlowDeletedSubClear':bCgnatAuthFlowDeletedSubClear,'bCgnatAuthNatFlowDelErrSubIdMismatch':bCgnatAuthNatFlowDelErrSubIdMismatch,'bCgnatAuthNatFlowDelErrValidFlagNotSet':bCgnatAuthNatFlowDelErrValidFlagNotSet,'bCgnatAuthIcmpPortUnreachableSent':bCgnatAuthIcmpPortUnreachableSent,'bCgnatAuthPortsNotAvailableDrop':bCgnatAuthPortsNotAvailableDrop,'bCgnatAuthUnsupportedPrivatePortDropCount':bCgnatAuthUnsupportedPrivatePortDropCount,'bCgnatUnauthStatsTable':bCgnatUnauthStatsTable,'bCgnatUnauthStatsEntry':bCgnatUnauthStatsEntry,_M:bCgnatUnauthStatsIndex,'bCgnatUnauthProfileName':bCgnatUnauthProfileName,'bCgnatUnauthDomainPublicIpZeroCount':bCgnatUnauthDomainPublicIpZeroCount,'bCgnatUnauthDomainNoFreePortCount':bCgnatUnauthDomainNoFreePortCount,'bCgnatUnauthFlowAddSuccessCount':bCgnatUnauthFlowAddSuccessCount,'bCgnatUnauthFlowAddFailureCount':bCgnatUnauthFlowAddFailureCount,'bCgnatUnauthTimerAllocFailureCount':bCgnatUnauthTimerAllocFailureCount,'bCgnatUnauthFlowDeleteSuccessCount':bCgnatUnauthFlowDeleteSuccessCount,'bCgnatUnauthFlowDeleteFailureCount':bCgnatUnauthFlowDeleteFailureCount,'bCgnatUnauthUnsupportedL4DropCount':bCgnatUnauthUnsupportedL4DropCount,'bCgnatUnauthNatflowSyncFailureCount':bCgnatUnauthNatflowSyncFailureCount,'bCgnatUnauthIcmpIdAllocSuccessCount':bCgnatUnauthIcmpIdAllocSuccessCount,'bCgnatUnauthTcpPortAllocSuccessCount':bCgnatUnauthTcpPortAllocSuccessCount,'bCgnatUnauthUdpPortAllocSuccessCount':bCgnatUnauthUdpPortAllocSuccessCount,'bCgnatUnauthIcmpIdAllocFailureCount':bCgnatUnauthIcmpIdAllocFailureCount,'bCgnatUnauthTcpPortAllocFailureCount':bCgnatUnauthTcpPortAllocFailureCount,'bCgnatUnauthUdpPortAllocFailureCount':bCgnatUnauthUdpPortAllocFailureCount,'bCgnatUnauthIcmpIdReleaseSuccessCount':bCgnatUnauthIcmpIdReleaseSuccessCount,'bCgnatUnauthTcpPortReleaseSuccessCount':bCgnatUnauthTcpPortReleaseSuccessCount,'bCgnatUnauthUdpPortReleaseSuccessCount':bCgnatUnauthUdpPortReleaseSuccessCount,'bCgnatUnauthIcmpIdReleaseFailureCount':bCgnatUnauthIcmpIdReleaseFailureCount,'bCgnatUnauthTcpPortReleaseFailureCount':bCgnatUnauthTcpPortReleaseFailureCount,'bCgnatUnauthUdpPortReleaseFailureCount':bCgnatUnauthUdpPortReleaseFailureCount,'bCgnatUnauthMaxCgnatPortsExceeded':bCgnatUnauthMaxCgnatPortsExceeded,'bCgnatUnauthMaxIcmpIdsExceeded':bCgnatUnauthMaxIcmpIdsExceeded,'bCgnatUnauthFlowDeleteRcvd':bCgnatUnauthFlowDeleteRcvd,'bCgnatUnauthFlowDeleteSent':bCgnatUnauthFlowDeleteSent,'bCgnatUnauthFlowDeleteFindFailure':bCgnatUnauthFlowDeleteFindFailure,'bCgnatUnauthDnsFlowAlloc':bCgnatUnauthDnsFlowAlloc,'bCgnatUnauthDnsFlowRelease':bCgnatUnauthDnsFlowRelease,'bCgnatUnauthDnsFlowAllocSuccessCount':bCgnatUnauthDnsFlowAllocSuccessCount,'bCgnatUnauthDnsFlowReleaseSuccessCount':bCgnatUnauthDnsFlowReleaseSuccessCount,'bCgnatUnauthDnsFlowAllocFailureCount':bCgnatUnauthDnsFlowAllocFailureCount,'bCgnatUnauthDnsFlowReleaseFailureCount':bCgnatUnauthDnsFlowReleaseFailureCount,'bCgnatUnauthPortsThresholdExceededSent':bCgnatUnauthPortsThresholdExceededSent,'bCgnatUnauthPortsThresholdExceededRcvd':bCgnatUnauthPortsThresholdExceededRcvd,'bCgnatUnauthPortsThresholdExceededInt':bCgnatUnauthPortsThresholdExceededInt,'bCgnatUnauthPortsThresholdExceededErr':bCgnatUnauthPortsThresholdExceededErr,'bCgnatUnauthUnsupportedActionIdRcvd':bCgnatUnauthUnsupportedActionIdRcvd,'bCgnatUnauthNonTcpSynPortAllocDrop':bCgnatUnauthNonTcpSynPortAllocDrop,'bCgnatUnauthFlowDeletedTimer':bCgnatUnauthFlowDeletedTimer,'bCgnatUnauthFlowDeletedSessionEnded':bCgnatUnauthFlowDeletedSessionEnded,'bCgnatUnauthFlowDeletedSubClear':bCgnatUnauthFlowDeletedSubClear,'bCgnatUnauthNatFlowDelErrSubIdMismatch':bCgnatUnauthNatFlowDelErrSubIdMismatch,'bCgnatUnauthNatFlowDelErrValidFlagNotSet':bCgnatUnauthNatFlowDelErrValidFlagNotSet,'bCgnatUnauthIcmpPortUnreachableSent':bCgnatUnauthIcmpPortUnreachableSent,'bCgnatUnauthPortsNotAvailableDrop':bCgnatUnauthPortsNotAvailableDrop,'bCgnatUnauthUnsupportedPrivatePortDropCount':bCgnatUnauthUnsupportedPrivatePortDropCount,'bCgnatAuthPortUtilTable':bCgnatAuthPortUtilTable,'bCgnatAuthPortUtilEntry':bCgnatAuthPortUtilEntry,_N:bCgnatAuthPortUtilIndex,'bCgnatAuthSubscriberMac':bCgnatAuthSubscriberMac,'bCgnatAuthSubscriberPortsFree':bCgnatAuthSubscriberPortsFree,'bCgnatAuthPortRisingThresholdCrossedSubCount':bCgnatAuthPortRisingThresholdCrossedSubCount,'bDslitePortBlockRisingThresholdCrossedTunCount':bDslitePortBlockRisingThresholdCrossedTunCount,'bCgnatNotifObjects':bCgnatNotifObjects,_F:bCgnatSubscriberMac,_G:bCgnatTotalPortBlocksPerSubscriber,_O:bCgnatPortBlocksUsedHighThreshold,_P:bCgnatPortBlocksUsedLowThreshold,_H:bCgnatThresholdTunnelId,_I:bCgnatEvenPortsForTunnel,_J:bCgnatOddPortsForTunnel,_K:bCgnatPortParity,_Q:bCgnatTunnelPortBlocksUsedHighThreshold,_R:bCgnatTunnelPortBlocksUsedLowThreshold})