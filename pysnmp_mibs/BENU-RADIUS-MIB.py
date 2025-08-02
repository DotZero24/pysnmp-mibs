_n='bAAAGroupOutstandingCoAReqsHighThreshold'
_m='bAAAGroupOutstandingCoAReqsLowThreshold'
_l='bAAAGroupOutstandingAcctReqsHighThreshold'
_k='bAAAGroupOutstandingAcctReqsLowThreshold'
_j='bAAAGroupOutstandingAuthReqsHighThreshold'
_i='bAAAGroupOutstandingAuthReqsLowThreshold'
_h='bRadiusProxyAuthTPSInterval'
_g='bRadiusProxyAcctServerIndex'
_f='bRadiusProxyAcctStatsInterval'
_e='bRadiusProxyAuthServerIndex'
_d='bRadiusProxyAuthStatsInterval'
_c='accessible-for-notify'
_b='bRadiusAuthInstanceIndex'
_a='bRadiusAuthLatencyStatsInterval'
_Z='bAAAGroupCoAIndex'
_Y='bAAAGroupCoAStatsInterval'
_X='bAAAGroupAcctIndex'
_W='bAAAGroupAcctStatsInterval'
_V='bAAAGroupAuthIndex'
_U='bAAAGroupAuthStatsInterval'
_T='bRadiusCoAClientIndex'
_S='bRadiusCOAStatsInterval'
_R='bRadiusAcctServerIndex'
_Q='bRadiusAcctStatsInterval'
_P='bRadiusAuthServerIndex'
_O='bRadiusAuthStatsInterval'
_N='bRadiusProxyAuthTPS'
_M='bAAAGroupMaximumOutstandingCoAReqs'
_L='bAAAGroupCoAName'
_K='bAAAGroupMaximumOutstandingAcctReqs'
_J='bAAAGroupAcctName'
_I='bAAAGroupMaximumOutstandingAuthReqs'
_H='bAAAGroupAuthName'
_G='bRadiusServerIPAddress'
_F='bRadiusServerIPAddrType'
_E='microseconds'
_D='not-accessible'
_C='BENU-RADIUS-MIB'
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
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
benuRadiusMIB=ModuleIdentity((1,3,6,1,4,1,39406,2,1,4))
if mibBuilder.loadTexts:benuRadiusMIB.setRevisions(('2016-07-28 00:00','2016-03-17 00:00','2015-06-24 00:00','2015-05-21 00:00','2015-05-20 00:00','2015-03-16 00:00','2015-03-02 00:00','2015-02-24 00:00','2015-01-26 00:00','2015-01-02 00:00','2014-12-02 00:00','2014-07-17 00:00','2014-05-19 00:00','2013-04-18 00:00'))
class BenuRadiusInstance(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('radiusInstance0',1))
_BRadiusNotifications_ObjectIdentity=ObjectIdentity
bRadiusNotifications=_BRadiusNotifications_ObjectIdentity((1,3,6,1,4,1,39406,2,1,4,0))
if mibBuilder.loadTexts:bRadiusNotifications.setStatus(_A)
_BRadiusMIBObjects_ObjectIdentity=ObjectIdentity
bRadiusMIBObjects=_BRadiusMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,4,1))
if mibBuilder.loadTexts:bRadiusMIBObjects.setStatus(_A)
_BRadiusServerAuthTable_Object=MibTable
bRadiusServerAuthTable=_BRadiusServerAuthTable_Object((1,3,6,1,4,1,39406,2,1,4,1,1))
if mibBuilder.loadTexts:bRadiusServerAuthTable.setStatus(_A)
_BRadiusServerAuthEntry_Object=MibTableRow
bRadiusServerAuthEntry=_BRadiusServerAuthEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1))
bRadiusServerAuthEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:bRadiusServerAuthEntry.setStatus(_A)
_BRadiusAuthStatsInterval_Type=Integer32
_BRadiusAuthStatsInterval_Object=MibTableColumn
bRadiusAuthStatsInterval=_BRadiusAuthStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,1),_BRadiusAuthStatsInterval_Type())
bRadiusAuthStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAuthStatsInterval.setStatus(_A)
_BRadiusAuthServerIndex_Type=Integer32
_BRadiusAuthServerIndex_Object=MibTableColumn
bRadiusAuthServerIndex=_BRadiusAuthServerIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,2),_BRadiusAuthServerIndex_Type())
bRadiusAuthServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAuthServerIndex.setStatus(_A)
_BRadiusAuthServerInetAddressType_Type=InetAddressType
_BRadiusAuthServerInetAddressType_Object=MibTableColumn
bRadiusAuthServerInetAddressType=_BRadiusAuthServerInetAddressType_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,3),_BRadiusAuthServerInetAddressType_Type())
bRadiusAuthServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthServerInetAddressType.setStatus(_A)
_BRadiusAuthServerInetAddress_Type=InetAddress
_BRadiusAuthServerInetAddress_Object=MibTableColumn
bRadiusAuthServerInetAddress=_BRadiusAuthServerInetAddress_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,4),_BRadiusAuthServerInetAddress_Type())
bRadiusAuthServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthServerInetAddress.setStatus(_A)
_BRadiusAuthIntervalDuration_Type=Integer32
_BRadiusAuthIntervalDuration_Object=MibTableColumn
bRadiusAuthIntervalDuration=_BRadiusAuthIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,5),_BRadiusAuthIntervalDuration_Type())
bRadiusAuthIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthIntervalDuration.setStatus(_A)
_BRadiusAccessRequestSent_Type=Unsigned32
_BRadiusAccessRequestSent_Object=MibTableColumn
bRadiusAccessRequestSent=_BRadiusAccessRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,6),_BRadiusAccessRequestSent_Type())
bRadiusAccessRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRequestSent.setStatus(_A)
_BRadiusAccessAcceptReceived_Type=Unsigned32
_BRadiusAccessAcceptReceived_Object=MibTableColumn
bRadiusAccessAcceptReceived=_BRadiusAccessAcceptReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,7),_BRadiusAccessAcceptReceived_Type())
bRadiusAccessAcceptReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessAcceptReceived.setStatus(_A)
_BRadiusAccessRejectReceived_Type=Unsigned32
_BRadiusAccessRejectReceived_Object=MibTableColumn
bRadiusAccessRejectReceived=_BRadiusAccessRejectReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,8),_BRadiusAccessRejectReceived_Type())
bRadiusAccessRejectReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRejectReceived.setStatus(_A)
_BRadiusAccessChallengeReceived_Type=Unsigned32
_BRadiusAccessChallengeReceived_Object=MibTableColumn
bRadiusAccessChallengeReceived=_BRadiusAccessChallengeReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,9),_BRadiusAccessChallengeReceived_Type())
bRadiusAccessChallengeReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessChallengeReceived.setStatus(_A)
_BRadiusAccessRequestResent_Type=Unsigned32
_BRadiusAccessRequestResent_Object=MibTableColumn
bRadiusAccessRequestResent=_BRadiusAccessRequestResent_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,10),_BRadiusAccessRequestResent_Type())
bRadiusAccessRequestResent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRequestResent.setStatus(_A)
_BRadiusAccessRequestDropped_Type=Unsigned32
_BRadiusAccessRequestDropped_Object=MibTableColumn
bRadiusAccessRequestDropped=_BRadiusAccessRequestDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,11),_BRadiusAccessRequestDropped_Type())
bRadiusAccessRequestDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRequestDropped.setStatus(_A)
_BRadiusAccessRequestTimedOut_Type=Unsigned32
_BRadiusAccessRequestTimedOut_Object=MibTableColumn
bRadiusAccessRequestTimedOut=_BRadiusAccessRequestTimedOut_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,12),_BRadiusAccessRequestTimedOut_Type())
bRadiusAccessRequestTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRequestTimedOut.setStatus(_A)
_BRadiusAccessRequestSentFail_Type=Unsigned32
_BRadiusAccessRequestSentFail_Object=MibTableColumn
bRadiusAccessRequestSentFail=_BRadiusAccessRequestSentFail_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,13),_BRadiusAccessRequestSentFail_Type())
bRadiusAccessRequestSentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessRequestSentFail.setStatus(_A)
_BRadiusAccessPeakRequestPending_Type=Unsigned32
_BRadiusAccessPeakRequestPending_Object=MibTableColumn
bRadiusAccessPeakRequestPending=_BRadiusAccessPeakRequestPending_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,14),_BRadiusAccessPeakRequestPending_Type())
bRadiusAccessPeakRequestPending.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessPeakRequestPending.setStatus(_A)
_BRadiusAccessMalformedRespDropped_Type=Unsigned32
_BRadiusAccessMalformedRespDropped_Object=MibTableColumn
bRadiusAccessMalformedRespDropped=_BRadiusAccessMalformedRespDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,15),_BRadiusAccessMalformedRespDropped_Type())
bRadiusAccessMalformedRespDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessMalformedRespDropped.setStatus(_A)
_BRadiusAccessBadAuthenticatorRcvd_Type=Unsigned32
_BRadiusAccessBadAuthenticatorRcvd_Object=MibTableColumn
bRadiusAccessBadAuthenticatorRcvd=_BRadiusAccessBadAuthenticatorRcvd_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,16),_BRadiusAccessBadAuthenticatorRcvd_Type())
bRadiusAccessBadAuthenticatorRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessBadAuthenticatorRcvd.setStatus(_A)
_BRadiusAccessServerMarkedDead_Type=Unsigned32
_BRadiusAccessServerMarkedDead_Object=MibTableColumn
bRadiusAccessServerMarkedDead=_BRadiusAccessServerMarkedDead_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,17),_BRadiusAccessServerMarkedDead_Type())
bRadiusAccessServerMarkedDead.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAccessServerMarkedDead.setStatus(_A)
_BRadiusAuthLatencyMin_Type=Unsigned32
_BRadiusAuthLatencyMin_Object=MibTableColumn
bRadiusAuthLatencyMin=_BRadiusAuthLatencyMin_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,18),_BRadiusAuthLatencyMin_Type())
bRadiusAuthLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthLatencyMin.setStatus(_A)
_BRadiusAuthLatencyMax_Type=Unsigned32
_BRadiusAuthLatencyMax_Object=MibTableColumn
bRadiusAuthLatencyMax=_BRadiusAuthLatencyMax_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,19),_BRadiusAuthLatencyMax_Type())
bRadiusAuthLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthLatencyMax.setStatus(_A)
_BRadiusAuthLatencyAvg_Type=Unsigned32
_BRadiusAuthLatencyAvg_Object=MibTableColumn
bRadiusAuthLatencyAvg=_BRadiusAuthLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,20),_BRadiusAuthLatencyAvg_Type())
bRadiusAuthLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthLatencyAvg.setStatus(_A)
_BRadiusAuthLatencyLast_Type=Unsigned32
_BRadiusAuthLatencyLast_Object=MibTableColumn
bRadiusAuthLatencyLast=_BRadiusAuthLatencyLast_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,21),_BRadiusAuthLatencyLast_Type())
bRadiusAuthLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthLatencyLast.setStatus(_A)
_BRadiusAuthAAAGroupName_Type=DisplayString
_BRadiusAuthAAAGroupName_Object=MibTableColumn
bRadiusAuthAAAGroupName=_BRadiusAuthAAAGroupName_Object((1,3,6,1,4,1,39406,2,1,4,1,1,1,22),_BRadiusAuthAAAGroupName_Type())
bRadiusAuthAAAGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthAAAGroupName.setStatus(_A)
_BRadiusServerAcctTable_Object=MibTable
bRadiusServerAcctTable=_BRadiusServerAcctTable_Object((1,3,6,1,4,1,39406,2,1,4,1,2))
if mibBuilder.loadTexts:bRadiusServerAcctTable.setStatus(_A)
_BRadiusServerAcctEntry_Object=MibTableRow
bRadiusServerAcctEntry=_BRadiusServerAcctEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1))
bRadiusServerAcctEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:bRadiusServerAcctEntry.setStatus(_A)
_BRadiusAcctStatsInterval_Type=Integer32
_BRadiusAcctStatsInterval_Object=MibTableColumn
bRadiusAcctStatsInterval=_BRadiusAcctStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,1),_BRadiusAcctStatsInterval_Type())
bRadiusAcctStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAcctStatsInterval.setStatus(_A)
_BRadiusAcctServerIndex_Type=Integer32
_BRadiusAcctServerIndex_Object=MibTableColumn
bRadiusAcctServerIndex=_BRadiusAcctServerIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,2),_BRadiusAcctServerIndex_Type())
bRadiusAcctServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAcctServerIndex.setStatus(_A)
_BRadiusAcctServerInetAddressType_Type=InetAddressType
_BRadiusAcctServerInetAddressType_Object=MibTableColumn
bRadiusAcctServerInetAddressType=_BRadiusAcctServerInetAddressType_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,3),_BRadiusAcctServerInetAddressType_Type())
bRadiusAcctServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctServerInetAddressType.setStatus(_A)
_BRadiusAcctServerInetAddress_Type=InetAddress
_BRadiusAcctServerInetAddress_Object=MibTableColumn
bRadiusAcctServerInetAddress=_BRadiusAcctServerInetAddress_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,4),_BRadiusAcctServerInetAddress_Type())
bRadiusAcctServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctServerInetAddress.setStatus(_A)
_BRadiusAcctIntervalDuration_Type=Integer32
_BRadiusAcctIntervalDuration_Object=MibTableColumn
bRadiusAcctIntervalDuration=_BRadiusAcctIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,5),_BRadiusAcctIntervalDuration_Type())
bRadiusAcctIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctIntervalDuration.setStatus(_A)
_BRadiusAcctRequestSent_Type=Unsigned32
_BRadiusAcctRequestSent_Object=MibTableColumn
bRadiusAcctRequestSent=_BRadiusAcctRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,6),_BRadiusAcctRequestSent_Type())
bRadiusAcctRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctRequestSent.setStatus(_A)
_BRadiusAcctStartRequestSent_Type=Unsigned32
_BRadiusAcctStartRequestSent_Object=MibTableColumn
bRadiusAcctStartRequestSent=_BRadiusAcctStartRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,7),_BRadiusAcctStartRequestSent_Type())
bRadiusAcctStartRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctStartRequestSent.setStatus(_A)
_BRadiusAcctStopRequestSent_Type=Unsigned32
_BRadiusAcctStopRequestSent_Object=MibTableColumn
bRadiusAcctStopRequestSent=_BRadiusAcctStopRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,8),_BRadiusAcctStopRequestSent_Type())
bRadiusAcctStopRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctStopRequestSent.setStatus(_A)
_BRadiusAcctInterimUpdateSent_Type=Unsigned32
_BRadiusAcctInterimUpdateSent_Object=MibTableColumn
bRadiusAcctInterimUpdateSent=_BRadiusAcctInterimUpdateSent_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,9),_BRadiusAcctInterimUpdateSent_Type())
bRadiusAcctInterimUpdateSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctInterimUpdateSent.setStatus(_A)
_BRadiusAcctResponseReceived_Type=Unsigned32
_BRadiusAcctResponseReceived_Object=MibTableColumn
bRadiusAcctResponseReceived=_BRadiusAcctResponseReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,10),_BRadiusAcctResponseReceived_Type())
bRadiusAcctResponseReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctResponseReceived.setStatus(_A)
_BRadiusAcctRequestResent_Type=Unsigned32
_BRadiusAcctRequestResent_Object=MibTableColumn
bRadiusAcctRequestResent=_BRadiusAcctRequestResent_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,11),_BRadiusAcctRequestResent_Type())
bRadiusAcctRequestResent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctRequestResent.setStatus(_A)
_BRadiusAcctRequestDropped_Type=Unsigned32
_BRadiusAcctRequestDropped_Object=MibTableColumn
bRadiusAcctRequestDropped=_BRadiusAcctRequestDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,12),_BRadiusAcctRequestDropped_Type())
bRadiusAcctRequestDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctRequestDropped.setStatus(_A)
_BRadiusAcctRequestTimedOut_Type=Unsigned32
_BRadiusAcctRequestTimedOut_Object=MibTableColumn
bRadiusAcctRequestTimedOut=_BRadiusAcctRequestTimedOut_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,13),_BRadiusAcctRequestTimedOut_Type())
bRadiusAcctRequestTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctRequestTimedOut.setStatus(_A)
_BRadiusAcctRequestSentFail_Type=Unsigned32
_BRadiusAcctRequestSentFail_Object=MibTableColumn
bRadiusAcctRequestSentFail=_BRadiusAcctRequestSentFail_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,14),_BRadiusAcctRequestSentFail_Type())
bRadiusAcctRequestSentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctRequestSentFail.setStatus(_A)
_BRadiusAcctPeakRequestPending_Type=Unsigned32
_BRadiusAcctPeakRequestPending_Object=MibTableColumn
bRadiusAcctPeakRequestPending=_BRadiusAcctPeakRequestPending_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,15),_BRadiusAcctPeakRequestPending_Type())
bRadiusAcctPeakRequestPending.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctPeakRequestPending.setStatus(_A)
_BRadiusAcctMalformedRespDropped_Type=Unsigned32
_BRadiusAcctMalformedRespDropped_Object=MibTableColumn
bRadiusAcctMalformedRespDropped=_BRadiusAcctMalformedRespDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,16),_BRadiusAcctMalformedRespDropped_Type())
bRadiusAcctMalformedRespDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctMalformedRespDropped.setStatus(_A)
_BRadiusAcctBadAuthenticatorRcvd_Type=Unsigned32
_BRadiusAcctBadAuthenticatorRcvd_Object=MibTableColumn
bRadiusAcctBadAuthenticatorRcvd=_BRadiusAcctBadAuthenticatorRcvd_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,17),_BRadiusAcctBadAuthenticatorRcvd_Type())
bRadiusAcctBadAuthenticatorRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctBadAuthenticatorRcvd.setStatus(_A)
_BRadiusAcctServerMarkedDead_Type=Unsigned32
_BRadiusAcctServerMarkedDead_Object=MibTableColumn
bRadiusAcctServerMarkedDead=_BRadiusAcctServerMarkedDead_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,18),_BRadiusAcctServerMarkedDead_Type())
bRadiusAcctServerMarkedDead.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctServerMarkedDead.setStatus(_A)
_BRadiusAcctLatencyMin_Type=Unsigned32
_BRadiusAcctLatencyMin_Object=MibTableColumn
bRadiusAcctLatencyMin=_BRadiusAcctLatencyMin_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,19),_BRadiusAcctLatencyMin_Type())
bRadiusAcctLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctLatencyMin.setStatus(_A)
_BRadiusAcctLatencyMax_Type=Unsigned32
_BRadiusAcctLatencyMax_Object=MibTableColumn
bRadiusAcctLatencyMax=_BRadiusAcctLatencyMax_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,20),_BRadiusAcctLatencyMax_Type())
bRadiusAcctLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctLatencyMax.setStatus(_A)
_BRadiusAcctLatencyAvg_Type=Unsigned32
_BRadiusAcctLatencyAvg_Object=MibTableColumn
bRadiusAcctLatencyAvg=_BRadiusAcctLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,21),_BRadiusAcctLatencyAvg_Type())
bRadiusAcctLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctLatencyAvg.setStatus(_A)
_BRadiusAcctLatencyLast_Type=Unsigned32
_BRadiusAcctLatencyLast_Object=MibTableColumn
bRadiusAcctLatencyLast=_BRadiusAcctLatencyLast_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,22),_BRadiusAcctLatencyLast_Type())
bRadiusAcctLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctLatencyLast.setStatus(_A)
_BRadiusAcctAAAGroupName_Type=DisplayString
_BRadiusAcctAAAGroupName_Object=MibTableColumn
bRadiusAcctAAAGroupName=_BRadiusAcctAAAGroupName_Object((1,3,6,1,4,1,39406,2,1,4,1,2,1,23),_BRadiusAcctAAAGroupName_Type())
bRadiusAcctAAAGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAcctAAAGroupName.setStatus(_A)
_BRadiusClientCoATable_Object=MibTable
bRadiusClientCoATable=_BRadiusClientCoATable_Object((1,3,6,1,4,1,39406,2,1,4,1,3))
if mibBuilder.loadTexts:bRadiusClientCoATable.setStatus(_A)
_BRadiusClientCoAEntry_Object=MibTableRow
bRadiusClientCoAEntry=_BRadiusClientCoAEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1))
bRadiusClientCoAEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:bRadiusClientCoAEntry.setStatus(_A)
_BRadiusCOAStatsInterval_Type=Integer32
_BRadiusCOAStatsInterval_Object=MibTableColumn
bRadiusCOAStatsInterval=_BRadiusCOAStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,1),_BRadiusCOAStatsInterval_Type())
bRadiusCOAStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusCOAStatsInterval.setStatus(_A)
_BRadiusCoAClientIndex_Type=Integer32
_BRadiusCoAClientIndex_Object=MibTableColumn
bRadiusCoAClientIndex=_BRadiusCoAClientIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,2),_BRadiusCoAClientIndex_Type())
bRadiusCoAClientIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusCoAClientIndex.setStatus(_A)
_BRadiusCoAClientInetAddressType_Type=InetAddressType
_BRadiusCoAClientInetAddressType_Object=MibTableColumn
bRadiusCoAClientInetAddressType=_BRadiusCoAClientInetAddressType_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,3),_BRadiusCoAClientInetAddressType_Type())
bRadiusCoAClientInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAClientInetAddressType.setStatus(_A)
_BRadiusCoAClientInetAddress_Type=InetAddress
_BRadiusCoAClientInetAddress_Object=MibTableColumn
bRadiusCoAClientInetAddress=_BRadiusCoAClientInetAddress_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,4),_BRadiusCoAClientInetAddress_Type())
bRadiusCoAClientInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAClientInetAddress.setStatus(_A)
_BRadiusCoAIntervalDuration_Type=Integer32
_BRadiusCoAIntervalDuration_Object=MibTableColumn
bRadiusCoAIntervalDuration=_BRadiusCoAIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,5),_BRadiusCoAIntervalDuration_Type())
bRadiusCoAIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAIntervalDuration.setStatus(_A)
_BRadiusCoAAckSent_Type=Unsigned32
_BRadiusCoAAckSent_Object=MibTableColumn
bRadiusCoAAckSent=_BRadiusCoAAckSent_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,6),_BRadiusCoAAckSent_Type())
bRadiusCoAAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAAckSent.setStatus(_A)
_BRadiusCoANackSent_Type=Unsigned32
_BRadiusCoANackSent_Object=MibTableColumn
bRadiusCoANackSent=_BRadiusCoANackSent_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,7),_BRadiusCoANackSent_Type())
bRadiusCoANackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoANackSent.setStatus(_A)
_BRadiusCoARequestReceived_Type=Unsigned32
_BRadiusCoARequestReceived_Object=MibTableColumn
bRadiusCoARequestReceived=_BRadiusCoARequestReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,8),_BRadiusCoARequestReceived_Type())
bRadiusCoARequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoARequestReceived.setStatus(_A)
_BRadiusCoARequestDropped_Type=Unsigned32
_BRadiusCoARequestDropped_Object=MibTableColumn
bRadiusCoARequestDropped=_BRadiusCoARequestDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,9),_BRadiusCoARequestDropped_Type())
bRadiusCoARequestDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoARequestDropped.setStatus(_A)
_BRadiusCoAReqDropDueToDupReq_Type=Unsigned32
_BRadiusCoAReqDropDueToDupReq_Object=MibTableColumn
bRadiusCoAReqDropDueToDupReq=_BRadiusCoAReqDropDueToDupReq_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,10),_BRadiusCoAReqDropDueToDupReq_Type())
bRadiusCoAReqDropDueToDupReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAReqDropDueToDupReq.setStatus(_A)
_BRadiusCoAReqDropDueToInvalidTime_Type=Unsigned32
_BRadiusCoAReqDropDueToInvalidTime_Object=MibTableColumn
bRadiusCoAReqDropDueToInvalidTime=_BRadiusCoAReqDropDueToInvalidTime_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,11),_BRadiusCoAReqDropDueToInvalidTime_Type())
bRadiusCoAReqDropDueToInvalidTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAReqDropDueToInvalidTime.setStatus(_A)
_BRadiusCoAReqDropDueToBadAuthenticator_Type=Unsigned32
_BRadiusCoAReqDropDueToBadAuthenticator_Object=MibTableColumn
bRadiusCoAReqDropDueToBadAuthenticator=_BRadiusCoAReqDropDueToBadAuthenticator_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,12),_BRadiusCoAReqDropDueToBadAuthenticator_Type())
bRadiusCoAReqDropDueToBadAuthenticator.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAReqDropDueToBadAuthenticator.setStatus(_A)
_BRadiusCoANackDueToInvalidReq_Type=Unsigned32
_BRadiusCoANackDueToInvalidReq_Object=MibTableColumn
bRadiusCoANackDueToInvalidReq=_BRadiusCoANackDueToInvalidReq_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,13),_BRadiusCoANackDueToInvalidReq_Type())
bRadiusCoANackDueToInvalidReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoANackDueToInvalidReq.setStatus(_A)
_BRadiusCoANackDueToExceedMaxOutstanding_Type=Unsigned32
_BRadiusCoANackDueToExceedMaxOutstanding_Object=MibTableColumn
bRadiusCoANackDueToExceedMaxOutstanding=_BRadiusCoANackDueToExceedMaxOutstanding_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,14),_BRadiusCoANackDueToExceedMaxOutstanding_Type())
bRadiusCoANackDueToExceedMaxOutstanding.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoANackDueToExceedMaxOutstanding.setStatus(_A)
_BRadiusDisconnectRequestReceived_Type=Unsigned32
_BRadiusDisconnectRequestReceived_Object=MibTableColumn
bRadiusDisconnectRequestReceived=_BRadiusDisconnectRequestReceived_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,15),_BRadiusDisconnectRequestReceived_Type())
bRadiusDisconnectRequestReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectRequestReceived.setStatus(_A)
_BRadiusDisconnectAckSent_Type=Unsigned32
_BRadiusDisconnectAckSent_Object=MibTableColumn
bRadiusDisconnectAckSent=_BRadiusDisconnectAckSent_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,16),_BRadiusDisconnectAckSent_Type())
bRadiusDisconnectAckSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectAckSent.setStatus(_A)
_BRadiusDisconnectNackSent_Type=Unsigned32
_BRadiusDisconnectNackSent_Object=MibTableColumn
bRadiusDisconnectNackSent=_BRadiusDisconnectNackSent_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,17),_BRadiusDisconnectNackSent_Type())
bRadiusDisconnectNackSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectNackSent.setStatus(_A)
_BRadiusDisconnectRequestDropped_Type=Unsigned32
_BRadiusDisconnectRequestDropped_Object=MibTableColumn
bRadiusDisconnectRequestDropped=_BRadiusDisconnectRequestDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,18),_BRadiusDisconnectRequestDropped_Type())
bRadiusDisconnectRequestDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectRequestDropped.setStatus(_A)
_BRadiusDisconnectReqDropDueToDupReq_Type=Unsigned32
_BRadiusDisconnectReqDropDueToDupReq_Object=MibTableColumn
bRadiusDisconnectReqDropDueToDupReq=_BRadiusDisconnectReqDropDueToDupReq_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,19),_BRadiusDisconnectReqDropDueToDupReq_Type())
bRadiusDisconnectReqDropDueToDupReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectReqDropDueToDupReq.setStatus(_A)
_BRadiusDisconnectReqDropDueToInvalidTime_Type=Unsigned32
_BRadiusDisconnectReqDropDueToInvalidTime_Object=MibTableColumn
bRadiusDisconnectReqDropDueToInvalidTime=_BRadiusDisconnectReqDropDueToInvalidTime_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,20),_BRadiusDisconnectReqDropDueToInvalidTime_Type())
bRadiusDisconnectReqDropDueToInvalidTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectReqDropDueToInvalidTime.setStatus(_A)
_BRadiusDisconnectReqDropDueToBadAuthenticator_Type=Unsigned32
_BRadiusDisconnectReqDropDueToBadAuthenticator_Object=MibTableColumn
bRadiusDisconnectReqDropDueToBadAuthenticator=_BRadiusDisconnectReqDropDueToBadAuthenticator_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,21),_BRadiusDisconnectReqDropDueToBadAuthenticator_Type())
bRadiusDisconnectReqDropDueToBadAuthenticator.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectReqDropDueToBadAuthenticator.setStatus(_A)
_BRadiusDisconnectNackDueToInvalidReq_Type=Unsigned32
_BRadiusDisconnectNackDueToInvalidReq_Object=MibTableColumn
bRadiusDisconnectNackDueToInvalidReq=_BRadiusDisconnectNackDueToInvalidReq_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,22),_BRadiusDisconnectNackDueToInvalidReq_Type())
bRadiusDisconnectNackDueToInvalidReq.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectNackDueToInvalidReq.setStatus(_A)
_BRadiusDisconnectNackDueToExceedMaxOutstanding_Type=Unsigned32
_BRadiusDisconnectNackDueToExceedMaxOutstanding_Object=MibTableColumn
bRadiusDisconnectNackDueToExceedMaxOutstanding=_BRadiusDisconnectNackDueToExceedMaxOutstanding_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,23),_BRadiusDisconnectNackDueToExceedMaxOutstanding_Type())
bRadiusDisconnectNackDueToExceedMaxOutstanding.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusDisconnectNackDueToExceedMaxOutstanding.setStatus(_A)
_BRadiusCoALatencyMin_Type=Unsigned32
_BRadiusCoALatencyMin_Object=MibTableColumn
bRadiusCoALatencyMin=_BRadiusCoALatencyMin_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,24),_BRadiusCoALatencyMin_Type())
bRadiusCoALatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoALatencyMin.setStatus(_A)
_BRadiusCoALatencyMax_Type=Unsigned32
_BRadiusCoALatencyMax_Object=MibTableColumn
bRadiusCoALatencyMax=_BRadiusCoALatencyMax_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,25),_BRadiusCoALatencyMax_Type())
bRadiusCoALatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoALatencyMax.setStatus(_A)
_BRadiusCoALatencyAvg_Type=Unsigned32
_BRadiusCoALatencyAvg_Object=MibTableColumn
bRadiusCoALatencyAvg=_BRadiusCoALatencyAvg_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,26),_BRadiusCoALatencyAvg_Type())
bRadiusCoALatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoALatencyAvg.setStatus(_A)
_BRadiusCoALatencyLast_Type=Unsigned32
_BRadiusCoALatencyLast_Object=MibTableColumn
bRadiusCoALatencyLast=_BRadiusCoALatencyLast_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,27),_BRadiusCoALatencyLast_Type())
bRadiusCoALatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoALatencyLast.setStatus(_A)
_BRadiusCoADMLatencyMin_Type=Unsigned32
_BRadiusCoADMLatencyMin_Object=MibTableColumn
bRadiusCoADMLatencyMin=_BRadiusCoADMLatencyMin_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,28),_BRadiusCoADMLatencyMin_Type())
bRadiusCoADMLatencyMin.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoADMLatencyMin.setStatus(_A)
_BRadiusCoADMLatencyMax_Type=Unsigned32
_BRadiusCoADMLatencyMax_Object=MibTableColumn
bRadiusCoADMLatencyMax=_BRadiusCoADMLatencyMax_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,29),_BRadiusCoADMLatencyMax_Type())
bRadiusCoADMLatencyMax.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoADMLatencyMax.setStatus(_A)
_BRadiusCoADMLatencyAvg_Type=Unsigned32
_BRadiusCoADMLatencyAvg_Object=MibTableColumn
bRadiusCoADMLatencyAvg=_BRadiusCoADMLatencyAvg_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,30),_BRadiusCoADMLatencyAvg_Type())
bRadiusCoADMLatencyAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoADMLatencyAvg.setStatus(_A)
_BRadiusCoADMLatencyLast_Type=Unsigned32
_BRadiusCoADMLatencyLast_Object=MibTableColumn
bRadiusCoADMLatencyLast=_BRadiusCoADMLatencyLast_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,31),_BRadiusCoADMLatencyLast_Type())
bRadiusCoADMLatencyLast.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoADMLatencyLast.setStatus(_A)
_BRadiusCoAAAAGroupName_Type=DisplayString
_BRadiusCoAAAAGroupName_Object=MibTableColumn
bRadiusCoAAAAGroupName=_BRadiusCoAAAAGroupName_Object((1,3,6,1,4,1,39406,2,1,4,1,3,1,32),_BRadiusCoAAAAGroupName_Type())
bRadiusCoAAAAGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusCoAAAAGroupName.setStatus(_A)
_BAAAGroupAuthTable_Object=MibTable
bAAAGroupAuthTable=_BAAAGroupAuthTable_Object((1,3,6,1,4,1,39406,2,1,4,1,4))
if mibBuilder.loadTexts:bAAAGroupAuthTable.setStatus(_A)
_BAAAGroupAuthEntry_Object=MibTableRow
bAAAGroupAuthEntry=_BAAAGroupAuthEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1))
bAAAGroupAuthEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:bAAAGroupAuthEntry.setStatus(_A)
_BAAAGroupAuthStatsInterval_Type=Integer32
_BAAAGroupAuthStatsInterval_Object=MibTableColumn
bAAAGroupAuthStatsInterval=_BAAAGroupAuthStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,1),_BAAAGroupAuthStatsInterval_Type())
bAAAGroupAuthStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupAuthStatsInterval.setStatus(_A)
_BAAAGroupAuthIndex_Type=Integer32
_BAAAGroupAuthIndex_Object=MibTableColumn
bAAAGroupAuthIndex=_BAAAGroupAuthIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,2),_BAAAGroupAuthIndex_Type())
bAAAGroupAuthIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupAuthIndex.setStatus(_A)
_BAAAGroupAuthName_Type=DisplayString
_BAAAGroupAuthName_Object=MibTableColumn
bAAAGroupAuthName=_BAAAGroupAuthName_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,3),_BAAAGroupAuthName_Type())
bAAAGroupAuthName.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAuthName.setStatus(_A)
_BAAAGroupAuthIntervalDuration_Type=Integer32
_BAAAGroupAuthIntervalDuration_Object=MibTableColumn
bAAAGroupAuthIntervalDuration=_BAAAGroupAuthIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,4),_BAAAGroupAuthIntervalDuration_Type())
bAAAGroupAuthIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAuthIntervalDuration.setStatus(_A)
_BAAAGroupMaximumOutstandingAuthReqs_Type=Unsigned32
_BAAAGroupMaximumOutstandingAuthReqs_Object=MibTableColumn
bAAAGroupMaximumOutstandingAuthReqs=_BAAAGroupMaximumOutstandingAuthReqs_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,5),_BAAAGroupMaximumOutstandingAuthReqs_Type())
bAAAGroupMaximumOutstandingAuthReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupMaximumOutstandingAuthReqs.setStatus(_A)
_BAAAGroupPeakOutstandingAuthReqsReached_Type=Unsigned32
_BAAAGroupPeakOutstandingAuthReqsReached_Object=MibTableColumn
bAAAGroupPeakOutstandingAuthReqsReached=_BAAAGroupPeakOutstandingAuthReqsReached_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,6),_BAAAGroupPeakOutstandingAuthReqsReached_Type())
bAAAGroupPeakOutstandingAuthReqsReached.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupPeakOutstandingAuthReqsReached.setStatus(_A)
_BAAAGroupAuthReqsDropped_Type=Unsigned32
_BAAAGroupAuthReqsDropped_Object=MibTableColumn
bAAAGroupAuthReqsDropped=_BAAAGroupAuthReqsDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,7),_BAAAGroupAuthReqsDropped_Type())
bAAAGroupAuthReqsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAuthReqsDropped.setStatus(_A)
_BAAAGroupOutstandingAuthReqsHighThreshold_Type=Unsigned32
_BAAAGroupOutstandingAuthReqsHighThreshold_Object=MibTableColumn
bAAAGroupOutstandingAuthReqsHighThreshold=_BAAAGroupOutstandingAuthReqsHighThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,8),_BAAAGroupOutstandingAuthReqsHighThreshold_Type())
bAAAGroupOutstandingAuthReqsHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingAuthReqsHighThreshold.setStatus(_A)
_BAAAGroupOutstandingAuthReqsLowThreshold_Type=Unsigned32
_BAAAGroupOutstandingAuthReqsLowThreshold_Object=MibTableColumn
bAAAGroupOutstandingAuthReqsLowThreshold=_BAAAGroupOutstandingAuthReqsLowThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,9),_BAAAGroupOutstandingAuthReqsLowThreshold_Type())
bAAAGroupOutstandingAuthReqsLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingAuthReqsLowThreshold.setStatus(_A)
_BAAAGroupAuthCurrentOutstanding_Type=Unsigned32
_BAAAGroupAuthCurrentOutstanding_Object=MibTableColumn
bAAAGroupAuthCurrentOutstanding=_BAAAGroupAuthCurrentOutstanding_Object((1,3,6,1,4,1,39406,2,1,4,1,4,1,10),_BAAAGroupAuthCurrentOutstanding_Type())
bAAAGroupAuthCurrentOutstanding.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAuthCurrentOutstanding.setStatus(_A)
_BAAAGroupAcctTable_Object=MibTable
bAAAGroupAcctTable=_BAAAGroupAcctTable_Object((1,3,6,1,4,1,39406,2,1,4,1,5))
if mibBuilder.loadTexts:bAAAGroupAcctTable.setStatus(_A)
_BAAAGroupAcctEntry_Object=MibTableRow
bAAAGroupAcctEntry=_BAAAGroupAcctEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1))
bAAAGroupAcctEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:bAAAGroupAcctEntry.setStatus(_A)
_BAAAGroupAcctStatsInterval_Type=Integer32
_BAAAGroupAcctStatsInterval_Object=MibTableColumn
bAAAGroupAcctStatsInterval=_BAAAGroupAcctStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,1),_BAAAGroupAcctStatsInterval_Type())
bAAAGroupAcctStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupAcctStatsInterval.setStatus(_A)
_BAAAGroupAcctIndex_Type=Integer32
_BAAAGroupAcctIndex_Object=MibTableColumn
bAAAGroupAcctIndex=_BAAAGroupAcctIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,2),_BAAAGroupAcctIndex_Type())
bAAAGroupAcctIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupAcctIndex.setStatus(_A)
_BAAAGroupAcctName_Type=DisplayString
_BAAAGroupAcctName_Object=MibTableColumn
bAAAGroupAcctName=_BAAAGroupAcctName_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,3),_BAAAGroupAcctName_Type())
bAAAGroupAcctName.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAcctName.setStatus(_A)
_BAAAGroupAcctIntervalDuration_Type=Integer32
_BAAAGroupAcctIntervalDuration_Object=MibTableColumn
bAAAGroupAcctIntervalDuration=_BAAAGroupAcctIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,4),_BAAAGroupAcctIntervalDuration_Type())
bAAAGroupAcctIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAcctIntervalDuration.setStatus(_A)
_BAAAGroupMaximumOutstandingAcctReqs_Type=Unsigned32
_BAAAGroupMaximumOutstandingAcctReqs_Object=MibTableColumn
bAAAGroupMaximumOutstandingAcctReqs=_BAAAGroupMaximumOutstandingAcctReqs_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,5),_BAAAGroupMaximumOutstandingAcctReqs_Type())
bAAAGroupMaximumOutstandingAcctReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupMaximumOutstandingAcctReqs.setStatus(_A)
_BAAAGroupPeakOutstandingAcctReqsReached_Type=Unsigned32
_BAAAGroupPeakOutstandingAcctReqsReached_Object=MibTableColumn
bAAAGroupPeakOutstandingAcctReqsReached=_BAAAGroupPeakOutstandingAcctReqsReached_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,6),_BAAAGroupPeakOutstandingAcctReqsReached_Type())
bAAAGroupPeakOutstandingAcctReqsReached.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupPeakOutstandingAcctReqsReached.setStatus(_A)
_BAAAGroupAcctReqsDropped_Type=Unsigned32
_BAAAGroupAcctReqsDropped_Object=MibTableColumn
bAAAGroupAcctReqsDropped=_BAAAGroupAcctReqsDropped_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,7),_BAAAGroupAcctReqsDropped_Type())
bAAAGroupAcctReqsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAcctReqsDropped.setStatus(_A)
_BAAAGroupOutstandingAcctReqsHighThreshold_Type=Unsigned32
_BAAAGroupOutstandingAcctReqsHighThreshold_Object=MibTableColumn
bAAAGroupOutstandingAcctReqsHighThreshold=_BAAAGroupOutstandingAcctReqsHighThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,8),_BAAAGroupOutstandingAcctReqsHighThreshold_Type())
bAAAGroupOutstandingAcctReqsHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingAcctReqsHighThreshold.setStatus(_A)
_BAAAGroupOutstandingAcctReqsLowThreshold_Type=Unsigned32
_BAAAGroupOutstandingAcctReqsLowThreshold_Object=MibTableColumn
bAAAGroupOutstandingAcctReqsLowThreshold=_BAAAGroupOutstandingAcctReqsLowThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,9),_BAAAGroupOutstandingAcctReqsLowThreshold_Type())
bAAAGroupOutstandingAcctReqsLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingAcctReqsLowThreshold.setStatus(_A)
_BAAAGroupAcctCurrentOutstanding_Type=Unsigned32
_BAAAGroupAcctCurrentOutstanding_Object=MibTableColumn
bAAAGroupAcctCurrentOutstanding=_BAAAGroupAcctCurrentOutstanding_Object((1,3,6,1,4,1,39406,2,1,4,1,5,1,10),_BAAAGroupAcctCurrentOutstanding_Type())
bAAAGroupAcctCurrentOutstanding.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupAcctCurrentOutstanding.setStatus(_A)
_BAAAGroupCoATable_Object=MibTable
bAAAGroupCoATable=_BAAAGroupCoATable_Object((1,3,6,1,4,1,39406,2,1,4,1,6))
if mibBuilder.loadTexts:bAAAGroupCoATable.setStatus(_A)
_BAAAGroupCoAEntry_Object=MibTableRow
bAAAGroupCoAEntry=_BAAAGroupCoAEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1))
bAAAGroupCoAEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:bAAAGroupCoAEntry.setStatus(_A)
_BAAAGroupCoAStatsInterval_Type=Integer32
_BAAAGroupCoAStatsInterval_Object=MibTableColumn
bAAAGroupCoAStatsInterval=_BAAAGroupCoAStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,1),_BAAAGroupCoAStatsInterval_Type())
bAAAGroupCoAStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupCoAStatsInterval.setStatus(_A)
_BAAAGroupCoAIndex_Type=Integer32
_BAAAGroupCoAIndex_Object=MibTableColumn
bAAAGroupCoAIndex=_BAAAGroupCoAIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,2),_BAAAGroupCoAIndex_Type())
bAAAGroupCoAIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bAAAGroupCoAIndex.setStatus(_A)
_BAAAGroupCoAName_Type=DisplayString
_BAAAGroupCoAName_Object=MibTableColumn
bAAAGroupCoAName=_BAAAGroupCoAName_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,3),_BAAAGroupCoAName_Type())
bAAAGroupCoAName.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupCoAName.setStatus(_A)
_BAAAGroupCoAIntervalDuration_Type=Integer32
_BAAAGroupCoAIntervalDuration_Object=MibTableColumn
bAAAGroupCoAIntervalDuration=_BAAAGroupCoAIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,4),_BAAAGroupCoAIntervalDuration_Type())
bAAAGroupCoAIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupCoAIntervalDuration.setStatus(_A)
_BAAAGroupCoANumOfClients_Type=Unsigned32
_BAAAGroupCoANumOfClients_Object=MibTableColumn
bAAAGroupCoANumOfClients=_BAAAGroupCoANumOfClients_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,5),_BAAAGroupCoANumOfClients_Type())
bAAAGroupCoANumOfClients.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupCoANumOfClients.setStatus(_A)
_BAAAGroupCoAReqsDropDueToInvalidClient_Type=Unsigned32
_BAAAGroupCoAReqsDropDueToInvalidClient_Object=MibTableColumn
bAAAGroupCoAReqsDropDueToInvalidClient=_BAAAGroupCoAReqsDropDueToInvalidClient_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,6),_BAAAGroupCoAReqsDropDueToInvalidClient_Type())
bAAAGroupCoAReqsDropDueToInvalidClient.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupCoAReqsDropDueToInvalidClient.setStatus(_A)
_BAAAGroupDisconnectReqsDropDueToInvalidClient_Type=Unsigned32
_BAAAGroupDisconnectReqsDropDueToInvalidClient_Object=MibTableColumn
bAAAGroupDisconnectReqsDropDueToInvalidClient=_BAAAGroupDisconnectReqsDropDueToInvalidClient_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,7),_BAAAGroupDisconnectReqsDropDueToInvalidClient_Type())
bAAAGroupDisconnectReqsDropDueToInvalidClient.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupDisconnectReqsDropDueToInvalidClient.setStatus(_A)
_BAAAGroupMaximumOutstandingCoAReqs_Type=Unsigned32
_BAAAGroupMaximumOutstandingCoAReqs_Object=MibTableColumn
bAAAGroupMaximumOutstandingCoAReqs=_BAAAGroupMaximumOutstandingCoAReqs_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,8),_BAAAGroupMaximumOutstandingCoAReqs_Type())
bAAAGroupMaximumOutstandingCoAReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupMaximumOutstandingCoAReqs.setStatus(_A)
_BAAAGroupPeakOutstandingCoAReqs_Type=Unsigned32
_BAAAGroupPeakOutstandingCoAReqs_Object=MibTableColumn
bAAAGroupPeakOutstandingCoAReqs=_BAAAGroupPeakOutstandingCoAReqs_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,9),_BAAAGroupPeakOutstandingCoAReqs_Type())
bAAAGroupPeakOutstandingCoAReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupPeakOutstandingCoAReqs.setStatus(_A)
_BAAAGroupOutstandingCoAReqsHighThreshold_Type=Unsigned32
_BAAAGroupOutstandingCoAReqsHighThreshold_Object=MibTableColumn
bAAAGroupOutstandingCoAReqsHighThreshold=_BAAAGroupOutstandingCoAReqsHighThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,10),_BAAAGroupOutstandingCoAReqsHighThreshold_Type())
bAAAGroupOutstandingCoAReqsHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingCoAReqsHighThreshold.setStatus(_A)
_BAAAGroupOutstandingCoAReqsLowThreshold_Type=Unsigned32
_BAAAGroupOutstandingCoAReqsLowThreshold_Object=MibTableColumn
bAAAGroupOutstandingCoAReqsLowThreshold=_BAAAGroupOutstandingCoAReqsLowThreshold_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,11),_BAAAGroupOutstandingCoAReqsLowThreshold_Type())
bAAAGroupOutstandingCoAReqsLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupOutstandingCoAReqsLowThreshold.setStatus(_A)
_BAAAGroupCoaCurrentOutstanding_Type=Unsigned32
_BAAAGroupCoaCurrentOutstanding_Object=MibTableColumn
bAAAGroupCoaCurrentOutstanding=_BAAAGroupCoaCurrentOutstanding_Object((1,3,6,1,4,1,39406,2,1,4,1,6,1,12),_BAAAGroupCoaCurrentOutstanding_Type())
bAAAGroupCoaCurrentOutstanding.setMaxAccess(_B)
if mibBuilder.loadTexts:bAAAGroupCoaCurrentOutstanding.setStatus(_A)
_BRadiusLatencyAuthTable_Object=MibTable
bRadiusLatencyAuthTable=_BRadiusLatencyAuthTable_Object((1,3,6,1,4,1,39406,2,1,4,1,7))
if mibBuilder.loadTexts:bRadiusLatencyAuthTable.setStatus(_A)
_BRadiusLatencyAuthEntry_Object=MibTableRow
bRadiusLatencyAuthEntry=_BRadiusLatencyAuthEntry_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1))
bRadiusLatencyAuthEntry.setIndexNames((0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:bRadiusLatencyAuthEntry.setStatus(_A)
_BRadiusAuthLatencyStatsInterval_Type=Integer32
_BRadiusAuthLatencyStatsInterval_Object=MibTableColumn
bRadiusAuthLatencyStatsInterval=_BRadiusAuthLatencyStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,1),_BRadiusAuthLatencyStatsInterval_Type())
bRadiusAuthLatencyStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAuthLatencyStatsInterval.setStatus(_A)
_BRadiusAuthInstanceIndex_Type=BenuRadiusInstance
_BRadiusAuthInstanceIndex_Object=MibTableColumn
bRadiusAuthInstanceIndex=_BRadiusAuthInstanceIndex_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,2),_BRadiusAuthInstanceIndex_Type())
bRadiusAuthInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusAuthInstanceIndex.setStatus(_A)
_BRadiusAuthLatencyIntervalDuration_Type=Integer32
_BRadiusAuthLatencyIntervalDuration_Object=MibTableColumn
bRadiusAuthLatencyIntervalDuration=_BRadiusAuthLatencyIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,3),_BRadiusAuthLatencyIntervalDuration_Type())
bRadiusAuthLatencyIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthLatencyIntervalDuration.setStatus(_A)
_BRadiusAuthRequestTotalPackets_Type=Unsigned32
_BRadiusAuthRequestTotalPackets_Object=MibTableColumn
bRadiusAuthRequestTotalPackets=_BRadiusAuthRequestTotalPackets_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,4),_BRadiusAuthRequestTotalPackets_Type())
bRadiusAuthRequestTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthRequestTotalPackets.setStatus(_A)
_BRadiusAuthRequestMaximumProcessingTime_Type=Unsigned32
_BRadiusAuthRequestMaximumProcessingTime_Object=MibTableColumn
bRadiusAuthRequestMaximumProcessingTime=_BRadiusAuthRequestMaximumProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,5),_BRadiusAuthRequestMaximumProcessingTime_Type())
bRadiusAuthRequestMaximumProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthRequestMaximumProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthRequestMaximumProcessingTime.setUnits(_E)
_BRadiusAuthRequestMinimumProcessingTime_Type=Unsigned32
_BRadiusAuthRequestMinimumProcessingTime_Object=MibTableColumn
bRadiusAuthRequestMinimumProcessingTime=_BRadiusAuthRequestMinimumProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,6),_BRadiusAuthRequestMinimumProcessingTime_Type())
bRadiusAuthRequestMinimumProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthRequestMinimumProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthRequestMinimumProcessingTime.setUnits(_E)
_BRadiusAuthRequestAverageProcessingTime_Type=Unsigned32
_BRadiusAuthRequestAverageProcessingTime_Object=MibTableColumn
bRadiusAuthRequestAverageProcessingTime=_BRadiusAuthRequestAverageProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,7),_BRadiusAuthRequestAverageProcessingTime_Type())
bRadiusAuthRequestAverageProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthRequestAverageProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthRequestAverageProcessingTime.setUnits(_E)
_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Type=Unsigned32
_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Object=MibTableColumn
bRadiusAuthRequestProcessingTimeGreaterthan1MS=_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,8),_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Type())
bRadiusAuthRequestProcessingTimeGreaterthan1MS.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthRequestProcessingTimeGreaterthan1MS.setStatus(_A)
_BRadiusAuthResponseTotalPackets_Type=Unsigned32
_BRadiusAuthResponseTotalPackets_Object=MibTableColumn
bRadiusAuthResponseTotalPackets=_BRadiusAuthResponseTotalPackets_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,9),_BRadiusAuthResponseTotalPackets_Type())
bRadiusAuthResponseTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthResponseTotalPackets.setStatus(_A)
_BRadiusAuthResponseMaximumProcessingTime_Type=Unsigned32
_BRadiusAuthResponseMaximumProcessingTime_Object=MibTableColumn
bRadiusAuthResponseMaximumProcessingTime=_BRadiusAuthResponseMaximumProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,10),_BRadiusAuthResponseMaximumProcessingTime_Type())
bRadiusAuthResponseMaximumProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthResponseMaximumProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthResponseMaximumProcessingTime.setUnits(_E)
_BRadiusAuthResponseMinimumProcessingTime_Type=Unsigned32
_BRadiusAuthResponseMinimumProcessingTime_Object=MibTableColumn
bRadiusAuthResponseMinimumProcessingTime=_BRadiusAuthResponseMinimumProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,11),_BRadiusAuthResponseMinimumProcessingTime_Type())
bRadiusAuthResponseMinimumProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthResponseMinimumProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthResponseMinimumProcessingTime.setUnits(_E)
_BRadiusAuthResponseAverageProcessingTime_Type=Unsigned32
_BRadiusAuthResponseAverageProcessingTime_Object=MibTableColumn
bRadiusAuthResponseAverageProcessingTime=_BRadiusAuthResponseAverageProcessingTime_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,12),_BRadiusAuthResponseAverageProcessingTime_Type())
bRadiusAuthResponseAverageProcessingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthResponseAverageProcessingTime.setStatus(_A)
if mibBuilder.loadTexts:bRadiusAuthResponseAverageProcessingTime.setUnits(_E)
_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Type=Unsigned32
_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Object=MibTableColumn
bRadiusAuthResponseProcessingTimeGreaterthan1MS=_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Object((1,3,6,1,4,1,39406,2,1,4,1,7,1,13),_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Type())
bRadiusAuthResponseProcessingTimeGreaterthan1MS.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusAuthResponseProcessingTimeGreaterthan1MS.setStatus(_A)
_BRadiusNotifObjects_ObjectIdentity=ObjectIdentity
bRadiusNotifObjects=_BRadiusNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,4,2))
if mibBuilder.loadTexts:bRadiusNotifObjects.setStatus(_A)
_BRadiusServerIPAddrType_Type=InetAddressType
_BRadiusServerIPAddrType_Object=MibScalar
bRadiusServerIPAddrType=_BRadiusServerIPAddrType_Object((1,3,6,1,4,1,39406,2,1,4,2,1),_BRadiusServerIPAddrType_Type())
bRadiusServerIPAddrType.setMaxAccess(_c)
if mibBuilder.loadTexts:bRadiusServerIPAddrType.setStatus(_A)
_BRadiusServerIPAddress_Type=InetAddress
_BRadiusServerIPAddress_Object=MibScalar
bRadiusServerIPAddress=_BRadiusServerIPAddress_Object((1,3,6,1,4,1,39406,2,1,4,2,2),_BRadiusServerIPAddress_Type())
bRadiusServerIPAddress.setMaxAccess(_c)
if mibBuilder.loadTexts:bRadiusServerIPAddress.setStatus(_A)
_BRadiusProxyMIBObjects_ObjectIdentity=ObjectIdentity
bRadiusProxyMIBObjects=_BRadiusProxyMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,4,3))
if mibBuilder.loadTexts:bRadiusProxyMIBObjects.setStatus(_A)
_BRadiusProxyServerAuthTable_Object=MibTable
bRadiusProxyServerAuthTable=_BRadiusProxyServerAuthTable_Object((1,3,6,1,4,1,39406,2,1,4,3,1))
if mibBuilder.loadTexts:bRadiusProxyServerAuthTable.setStatus(_A)
_BRadiusProxyServerAuthEntry_Object=MibTableRow
bRadiusProxyServerAuthEntry=_BRadiusProxyServerAuthEntry_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1))
bRadiusProxyServerAuthEntry.setIndexNames((0,_C,_d),(0,_C,_e))
if mibBuilder.loadTexts:bRadiusProxyServerAuthEntry.setStatus(_A)
_BRadiusProxyAuthStatsInterval_Type=Integer32
_BRadiusProxyAuthStatsInterval_Object=MibTableColumn
bRadiusProxyAuthStatsInterval=_BRadiusProxyAuthStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,1),_BRadiusProxyAuthStatsInterval_Type())
bRadiusProxyAuthStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusProxyAuthStatsInterval.setStatus(_A)
_BRadiusProxyAuthServerIndex_Type=Integer32
_BRadiusProxyAuthServerIndex_Object=MibTableColumn
bRadiusProxyAuthServerIndex=_BRadiusProxyAuthServerIndex_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,2),_BRadiusProxyAuthServerIndex_Type())
bRadiusProxyAuthServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusProxyAuthServerIndex.setStatus(_A)
_BRadiusProxyAuthServerInetAddressType_Type=InetAddressType
_BRadiusProxyAuthServerInetAddressType_Object=MibTableColumn
bRadiusProxyAuthServerInetAddressType=_BRadiusProxyAuthServerInetAddressType_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,3),_BRadiusProxyAuthServerInetAddressType_Type())
bRadiusProxyAuthServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthServerInetAddressType.setStatus(_A)
_BRadiusProxyAuthServerInetAddress_Type=InetAddress
_BRadiusProxyAuthServerInetAddress_Object=MibTableColumn
bRadiusProxyAuthServerInetAddress=_BRadiusProxyAuthServerInetAddress_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,4),_BRadiusProxyAuthServerInetAddress_Type())
bRadiusProxyAuthServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthServerInetAddress.setStatus(_A)
_BRadiusProxyAuthIntervalDuration_Type=Integer32
_BRadiusProxyAuthIntervalDuration_Object=MibTableColumn
bRadiusProxyAuthIntervalDuration=_BRadiusProxyAuthIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,5),_BRadiusProxyAuthIntervalDuration_Type())
bRadiusProxyAuthIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthIntervalDuration.setStatus(_A)
_BRadiusProxyAccessRequestRcvd_Type=Unsigned32
_BRadiusProxyAccessRequestRcvd_Object=MibTableColumn
bRadiusProxyAccessRequestRcvd=_BRadiusProxyAccessRequestRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,6),_BRadiusProxyAccessRequestRcvd_Type())
bRadiusProxyAccessRequestRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessRequestRcvd.setStatus(_A)
_BRadiusProxyAccessUnknownTypeRcvd_Type=Unsigned32
_BRadiusProxyAccessUnknownTypeRcvd_Object=MibTableColumn
bRadiusProxyAccessUnknownTypeRcvd=_BRadiusProxyAccessUnknownTypeRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,7),_BRadiusProxyAccessUnknownTypeRcvd_Type())
bRadiusProxyAccessUnknownTypeRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessUnknownTypeRcvd.setStatus(_A)
_BRadiusProxyAccessUnknownClientRcvd_Type=Unsigned32
_BRadiusProxyAccessUnknownClientRcvd_Object=MibTableColumn
bRadiusProxyAccessUnknownClientRcvd=_BRadiusProxyAccessUnknownClientRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,8),_BRadiusProxyAccessUnknownClientRcvd_Type())
bRadiusProxyAccessUnknownClientRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessUnknownClientRcvd.setStatus(_A)
_BRadiusProxyAccessRequestDropped_Type=Unsigned32
_BRadiusProxyAccessRequestDropped_Object=MibTableColumn
bRadiusProxyAccessRequestDropped=_BRadiusProxyAccessRequestDropped_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,9),_BRadiusProxyAccessRequestDropped_Type())
bRadiusProxyAccessRequestDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessRequestDropped.setStatus(_A)
_BRadiusProxyAccessSentFail_Type=Unsigned32
_BRadiusProxyAccessSentFail_Object=MibTableColumn
bRadiusProxyAccessSentFail=_BRadiusProxyAccessSentFail_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,10),_BRadiusProxyAccessSentFail_Type())
bRadiusProxyAccessSentFail.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessSentFail.setStatus(_A)
_BRadiusProxyAccessBadAuthenticatorRcvd_Type=Unsigned32
_BRadiusProxyAccessBadAuthenticatorRcvd_Object=MibTableColumn
bRadiusProxyAccessBadAuthenticatorRcvd=_BRadiusProxyAccessBadAuthenticatorRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,11),_BRadiusProxyAccessBadAuthenticatorRcvd_Type())
bRadiusProxyAccessBadAuthenticatorRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessBadAuthenticatorRcvd.setStatus(_A)
_BRadiusProxyAccessAcceptRcvd_Type=Unsigned32
_BRadiusProxyAccessAcceptRcvd_Object=MibTableColumn
bRadiusProxyAccessAcceptRcvd=_BRadiusProxyAccessAcceptRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,12),_BRadiusProxyAccessAcceptRcvd_Type())
bRadiusProxyAccessAcceptRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessAcceptRcvd.setStatus(_A)
_BRadiusProxyAccessRejectRcvd_Type=Unsigned32
_BRadiusProxyAccessRejectRcvd_Object=MibTableColumn
bRadiusProxyAccessRejectRcvd=_BRadiusProxyAccessRejectRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,13),_BRadiusProxyAccessRejectRcvd_Type())
bRadiusProxyAccessRejectRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessRejectRcvd.setStatus(_A)
_BRadiusProxyAccessChallengeRcvd_Type=Unsigned32
_BRadiusProxyAccessChallengeRcvd_Object=MibTableColumn
bRadiusProxyAccessChallengeRcvd=_BRadiusProxyAccessChallengeRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,14),_BRadiusProxyAccessChallengeRcvd_Type())
bRadiusProxyAccessChallengeRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAccessChallengeRcvd.setStatus(_A)
_BRadiusProxySubscriberBlocked_Type=Unsigned32
_BRadiusProxySubscriberBlocked_Object=MibTableColumn
bRadiusProxySubscriberBlocked=_BRadiusProxySubscriberBlocked_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,15),_BRadiusProxySubscriberBlocked_Type())
bRadiusProxySubscriberBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxySubscriberBlocked.setStatus(_A)
_BRadiusProxySubscriberDeleted_Type=Unsigned32
_BRadiusProxySubscriberDeleted_Object=MibTableColumn
bRadiusProxySubscriberDeleted=_BRadiusProxySubscriberDeleted_Object((1,3,6,1,4,1,39406,2,1,4,3,1,1,16),_BRadiusProxySubscriberDeleted_Type())
bRadiusProxySubscriberDeleted.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxySubscriberDeleted.setStatus(_A)
_BRadiusProxyServerAcctTable_Object=MibTable
bRadiusProxyServerAcctTable=_BRadiusProxyServerAcctTable_Object((1,3,6,1,4,1,39406,2,1,4,3,2))
if mibBuilder.loadTexts:bRadiusProxyServerAcctTable.setStatus(_A)
_BRadiusProxyServerAcctEntry_Object=MibTableRow
bRadiusProxyServerAcctEntry=_BRadiusProxyServerAcctEntry_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1))
bRadiusProxyServerAcctEntry.setIndexNames((0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:bRadiusProxyServerAcctEntry.setStatus(_A)
_BRadiusProxyAcctStatsInterval_Type=Integer32
_BRadiusProxyAcctStatsInterval_Object=MibTableColumn
bRadiusProxyAcctStatsInterval=_BRadiusProxyAcctStatsInterval_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,1),_BRadiusProxyAcctStatsInterval_Type())
bRadiusProxyAcctStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusProxyAcctStatsInterval.setStatus(_A)
_BRadiusProxyAcctServerIndex_Type=Integer32
_BRadiusProxyAcctServerIndex_Object=MibTableColumn
bRadiusProxyAcctServerIndex=_BRadiusProxyAcctServerIndex_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,2),_BRadiusProxyAcctServerIndex_Type())
bRadiusProxyAcctServerIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusProxyAcctServerIndex.setStatus(_A)
_BRadiusProxyAcctServerInetAddressType_Type=InetAddressType
_BRadiusProxyAcctServerInetAddressType_Object=MibTableColumn
bRadiusProxyAcctServerInetAddressType=_BRadiusProxyAcctServerInetAddressType_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,3),_BRadiusProxyAcctServerInetAddressType_Type())
bRadiusProxyAcctServerInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctServerInetAddressType.setStatus(_A)
_BRadiusProxyAcctServerInetAddress_Type=InetAddress
_BRadiusProxyAcctServerInetAddress_Object=MibTableColumn
bRadiusProxyAcctServerInetAddress=_BRadiusProxyAcctServerInetAddress_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,4),_BRadiusProxyAcctServerInetAddress_Type())
bRadiusProxyAcctServerInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctServerInetAddress.setStatus(_A)
_BRadiusProxyAcctIntervalDuration_Type=Integer32
_BRadiusProxyAcctIntervalDuration_Object=MibTableColumn
bRadiusProxyAcctIntervalDuration=_BRadiusProxyAcctIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,5),_BRadiusProxyAcctIntervalDuration_Type())
bRadiusProxyAcctIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctIntervalDuration.setStatus(_A)
_BRadiusProxyAcctRequestRcvd_Type=Unsigned32
_BRadiusProxyAcctRequestRcvd_Object=MibTableColumn
bRadiusProxyAcctRequestRcvd=_BRadiusProxyAcctRequestRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,6),_BRadiusProxyAcctRequestRcvd_Type())
bRadiusProxyAcctRequestRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctRequestRcvd.setStatus(_A)
_BRadiusProxyAcctRequestSent_Type=Unsigned32
_BRadiusProxyAcctRequestSent_Object=MibTableColumn
bRadiusProxyAcctRequestSent=_BRadiusProxyAcctRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,7),_BRadiusProxyAcctRequestSent_Type())
bRadiusProxyAcctRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctRequestSent.setStatus(_A)
_BRadiusProxyAcctStartRequestRcvd_Type=Unsigned32
_BRadiusProxyAcctStartRequestRcvd_Object=MibTableColumn
bRadiusProxyAcctStartRequestRcvd=_BRadiusProxyAcctStartRequestRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,8),_BRadiusProxyAcctStartRequestRcvd_Type())
bRadiusProxyAcctStartRequestRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctStartRequestRcvd.setStatus(_A)
_BRadiusProxyAcctStopRequestRcvd_Type=Unsigned32
_BRadiusProxyAcctStopRequestRcvd_Object=MibTableColumn
bRadiusProxyAcctStopRequestRcvd=_BRadiusProxyAcctStopRequestRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,9),_BRadiusProxyAcctStopRequestRcvd_Type())
bRadiusProxyAcctStopRequestRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctStopRequestRcvd.setStatus(_A)
_BRadiusProxyAcctInterimUpdateRcvd_Type=Unsigned32
_BRadiusProxyAcctInterimUpdateRcvd_Object=MibTableColumn
bRadiusProxyAcctInterimUpdateRcvd=_BRadiusProxyAcctInterimUpdateRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,10),_BRadiusProxyAcctInterimUpdateRcvd_Type())
bRadiusProxyAcctInterimUpdateRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctInterimUpdateRcvd.setStatus(_A)
_BRadiusProxyAcctStartRequestSent_Type=Unsigned32
_BRadiusProxyAcctStartRequestSent_Object=MibTableColumn
bRadiusProxyAcctStartRequestSent=_BRadiusProxyAcctStartRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,11),_BRadiusProxyAcctStartRequestSent_Type())
bRadiusProxyAcctStartRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctStartRequestSent.setStatus(_A)
_BRadiusProxyAcctStopRequestSent_Type=Unsigned32
_BRadiusProxyAcctStopRequestSent_Object=MibTableColumn
bRadiusProxyAcctStopRequestSent=_BRadiusProxyAcctStopRequestSent_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,12),_BRadiusProxyAcctStopRequestSent_Type())
bRadiusProxyAcctStopRequestSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctStopRequestSent.setStatus(_A)
_BRadiusProxyAcctInterimUpdateSent_Type=Unsigned32
_BRadiusProxyAcctInterimUpdateSent_Object=MibTableColumn
bRadiusProxyAcctInterimUpdateSent=_BRadiusProxyAcctInterimUpdateSent_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,13),_BRadiusProxyAcctInterimUpdateSent_Type())
bRadiusProxyAcctInterimUpdateSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctInterimUpdateSent.setStatus(_A)
_BRadiusProxyAcctResponseRcvd_Type=Unsigned32
_BRadiusProxyAcctResponseRcvd_Object=MibTableColumn
bRadiusProxyAcctResponseRcvd=_BRadiusProxyAcctResponseRcvd_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,14),_BRadiusProxyAcctResponseRcvd_Type())
bRadiusProxyAcctResponseRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctResponseRcvd.setStatus(_A)
_BRadiusProxyAcctResponseSent_Type=Unsigned32
_BRadiusProxyAcctResponseSent_Object=MibTableColumn
bRadiusProxyAcctResponseSent=_BRadiusProxyAcctResponseSent_Object((1,3,6,1,4,1,39406,2,1,4,3,2,1,15),_BRadiusProxyAcctResponseSent_Type())
bRadiusProxyAcctResponseSent.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAcctResponseSent.setStatus(_A)
_BRadiusProxyAuthTPSTable_Object=MibTable
bRadiusProxyAuthTPSTable=_BRadiusProxyAuthTPSTable_Object((1,3,6,1,4,1,39406,2,1,4,3,3))
if mibBuilder.loadTexts:bRadiusProxyAuthTPSTable.setStatus(_A)
_BRadiusProxyAuthTPSEntry_Object=MibTableRow
bRadiusProxyAuthTPSEntry=_BRadiusProxyAuthTPSEntry_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1))
bRadiusProxyAuthTPSEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:bRadiusProxyAuthTPSEntry.setStatus(_A)
_BRadiusProxyAuthTPSInterval_Type=Integer32
_BRadiusProxyAuthTPSInterval_Object=MibTableColumn
bRadiusProxyAuthTPSInterval=_BRadiusProxyAuthTPSInterval_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1,1),_BRadiusProxyAuthTPSInterval_Type())
bRadiusProxyAuthTPSInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:bRadiusProxyAuthTPSInterval.setStatus(_A)
_BRadiusProxyAuthTPSIntervalDuration_Type=Unsigned32
_BRadiusProxyAuthTPSIntervalDuration_Object=MibTableColumn
bRadiusProxyAuthTPSIntervalDuration=_BRadiusProxyAuthTPSIntervalDuration_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1,2),_BRadiusProxyAuthTPSIntervalDuration_Type())
bRadiusProxyAuthTPSIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthTPSIntervalDuration.setStatus(_A)
_BRadiusProxyAuthTPSLow_Type=Unsigned32
_BRadiusProxyAuthTPSLow_Object=MibTableColumn
bRadiusProxyAuthTPSLow=_BRadiusProxyAuthTPSLow_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1,3),_BRadiusProxyAuthTPSLow_Type())
bRadiusProxyAuthTPSLow.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthTPSLow.setStatus(_A)
_BRadiusProxyAuthTPSHigh_Type=Unsigned32
_BRadiusProxyAuthTPSHigh_Object=MibTableColumn
bRadiusProxyAuthTPSHigh=_BRadiusProxyAuthTPSHigh_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1,4),_BRadiusProxyAuthTPSHigh_Type())
bRadiusProxyAuthTPSHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthTPSHigh.setStatus(_A)
_BRadiusProxyAuthTPS_Type=Unsigned32
_BRadiusProxyAuthTPS_Object=MibTableColumn
bRadiusProxyAuthTPS=_BRadiusProxyAuthTPS_Object((1,3,6,1,4,1,39406,2,1,4,3,3,1,5),_BRadiusProxyAuthTPS_Type())
bRadiusProxyAuthTPS.setMaxAccess(_B)
if mibBuilder.loadTexts:bRadiusProxyAuthTPS.setStatus(_A)
_BRadiusProxyNotifObjects_ObjectIdentity=ObjectIdentity
bRadiusProxyNotifObjects=_BRadiusProxyNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,2,1,4,4))
if mibBuilder.loadTexts:bRadiusProxyNotifObjects.setStatus(_A)
bAAAGroupOutstandingAuthReqsLow=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,1))
bAAAGroupOutstandingAuthReqsLow.setObjects(*((_C,_H),(_C,_I),(_C,_i)))
if mibBuilder.loadTexts:bAAAGroupOutstandingAuthReqsLow.setStatus(_A)
bAAAGroupOutstandingAuthReqsHigh=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,2))
bAAAGroupOutstandingAuthReqsHigh.setObjects(*((_C,_H),(_C,_I),(_C,_j)))
if mibBuilder.loadTexts:bAAAGroupOutstandingAuthReqsHigh.setStatus(_A)
bAAAGroupOutstandingAcctReqsLow=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,3))
bAAAGroupOutstandingAcctReqsLow.setObjects(*((_C,_J),(_C,_K),(_C,_k)))
if mibBuilder.loadTexts:bAAAGroupOutstandingAcctReqsLow.setStatus(_A)
bAAAGroupOutstandingAcctReqsHigh=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,4))
bAAAGroupOutstandingAcctReqsHigh.setObjects(*((_C,_J),(_C,_K),(_C,_l)))
if mibBuilder.loadTexts:bAAAGroupOutstandingAcctReqsHigh.setStatus(_A)
bAAAGroupOutstandingCoAReqsLow=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,5))
bAAAGroupOutstandingCoAReqsLow.setObjects(*((_C,_L),(_C,_M),(_C,_m)))
if mibBuilder.loadTexts:bAAAGroupOutstandingCoAReqsLow.setStatus(_A)
bAAAGroupOutstandingCoAReqsHigh=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,6))
bAAAGroupOutstandingCoAReqsHigh.setObjects(*((_C,_L),(_C,_M),(_C,_n)))
if mibBuilder.loadTexts:bAAAGroupOutstandingCoAReqsHigh.setStatus(_A)
bRadiusAuthServerMarkedDead=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,7))
bRadiusAuthServerMarkedDead.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:bRadiusAuthServerMarkedDead.setStatus(_A)
bRadiusAuthServerMarkedAlive=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,8))
bRadiusAuthServerMarkedAlive.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:bRadiusAuthServerMarkedAlive.setStatus(_A)
bRadiusAccountingServerMarkedDead=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,9))
bRadiusAccountingServerMarkedDead.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:bRadiusAccountingServerMarkedDead.setStatus(_A)
bRadiusAccountingServerMarkedAlive=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,10))
bRadiusAccountingServerMarkedAlive.setObjects(*((_C,_F),(_C,_G)))
if mibBuilder.loadTexts:bRadiusAccountingServerMarkedAlive.setStatus(_A)
bRadiusProxyAuthTPSLowReached=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,11))
bRadiusProxyAuthTPSLowReached.setObjects((_C,_N))
if mibBuilder.loadTexts:bRadiusProxyAuthTPSLowReached.setStatus(_A)
bRadiusProxyAuthTPSHighReached=NotificationType((1,3,6,1,4,1,39406,2,1,4,0,12))
bRadiusProxyAuthTPSHighReached.setObjects((_C,_N))
if mibBuilder.loadTexts:bRadiusProxyAuthTPSHighReached.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BenuRadiusInstance':BenuRadiusInstance,'benuRadiusMIB':benuRadiusMIB,'bRadiusNotifications':bRadiusNotifications,'bAAAGroupOutstandingAuthReqsLow':bAAAGroupOutstandingAuthReqsLow,'bAAAGroupOutstandingAuthReqsHigh':bAAAGroupOutstandingAuthReqsHigh,'bAAAGroupOutstandingAcctReqsLow':bAAAGroupOutstandingAcctReqsLow,'bAAAGroupOutstandingAcctReqsHigh':bAAAGroupOutstandingAcctReqsHigh,'bAAAGroupOutstandingCoAReqsLow':bAAAGroupOutstandingCoAReqsLow,'bAAAGroupOutstandingCoAReqsHigh':bAAAGroupOutstandingCoAReqsHigh,'bRadiusAuthServerMarkedDead':bRadiusAuthServerMarkedDead,'bRadiusAuthServerMarkedAlive':bRadiusAuthServerMarkedAlive,'bRadiusAccountingServerMarkedDead':bRadiusAccountingServerMarkedDead,'bRadiusAccountingServerMarkedAlive':bRadiusAccountingServerMarkedAlive,'bRadiusProxyAuthTPSLowReached':bRadiusProxyAuthTPSLowReached,'bRadiusProxyAuthTPSHighReached':bRadiusProxyAuthTPSHighReached,'bRadiusMIBObjects':bRadiusMIBObjects,'bRadiusServerAuthTable':bRadiusServerAuthTable,'bRadiusServerAuthEntry':bRadiusServerAuthEntry,_O:bRadiusAuthStatsInterval,_P:bRadiusAuthServerIndex,'bRadiusAuthServerInetAddressType':bRadiusAuthServerInetAddressType,'bRadiusAuthServerInetAddress':bRadiusAuthServerInetAddress,'bRadiusAuthIntervalDuration':bRadiusAuthIntervalDuration,'bRadiusAccessRequestSent':bRadiusAccessRequestSent,'bRadiusAccessAcceptReceived':bRadiusAccessAcceptReceived,'bRadiusAccessRejectReceived':bRadiusAccessRejectReceived,'bRadiusAccessChallengeReceived':bRadiusAccessChallengeReceived,'bRadiusAccessRequestResent':bRadiusAccessRequestResent,'bRadiusAccessRequestDropped':bRadiusAccessRequestDropped,'bRadiusAccessRequestTimedOut':bRadiusAccessRequestTimedOut,'bRadiusAccessRequestSentFail':bRadiusAccessRequestSentFail,'bRadiusAccessPeakRequestPending':bRadiusAccessPeakRequestPending,'bRadiusAccessMalformedRespDropped':bRadiusAccessMalformedRespDropped,'bRadiusAccessBadAuthenticatorRcvd':bRadiusAccessBadAuthenticatorRcvd,'bRadiusAccessServerMarkedDead':bRadiusAccessServerMarkedDead,'bRadiusAuthLatencyMin':bRadiusAuthLatencyMin,'bRadiusAuthLatencyMax':bRadiusAuthLatencyMax,'bRadiusAuthLatencyAvg':bRadiusAuthLatencyAvg,'bRadiusAuthLatencyLast':bRadiusAuthLatencyLast,'bRadiusAuthAAAGroupName':bRadiusAuthAAAGroupName,'bRadiusServerAcctTable':bRadiusServerAcctTable,'bRadiusServerAcctEntry':bRadiusServerAcctEntry,_Q:bRadiusAcctStatsInterval,_R:bRadiusAcctServerIndex,'bRadiusAcctServerInetAddressType':bRadiusAcctServerInetAddressType,'bRadiusAcctServerInetAddress':bRadiusAcctServerInetAddress,'bRadiusAcctIntervalDuration':bRadiusAcctIntervalDuration,'bRadiusAcctRequestSent':bRadiusAcctRequestSent,'bRadiusAcctStartRequestSent':bRadiusAcctStartRequestSent,'bRadiusAcctStopRequestSent':bRadiusAcctStopRequestSent,'bRadiusAcctInterimUpdateSent':bRadiusAcctInterimUpdateSent,'bRadiusAcctResponseReceived':bRadiusAcctResponseReceived,'bRadiusAcctRequestResent':bRadiusAcctRequestResent,'bRadiusAcctRequestDropped':bRadiusAcctRequestDropped,'bRadiusAcctRequestTimedOut':bRadiusAcctRequestTimedOut,'bRadiusAcctRequestSentFail':bRadiusAcctRequestSentFail,'bRadiusAcctPeakRequestPending':bRadiusAcctPeakRequestPending,'bRadiusAcctMalformedRespDropped':bRadiusAcctMalformedRespDropped,'bRadiusAcctBadAuthenticatorRcvd':bRadiusAcctBadAuthenticatorRcvd,'bRadiusAcctServerMarkedDead':bRadiusAcctServerMarkedDead,'bRadiusAcctLatencyMin':bRadiusAcctLatencyMin,'bRadiusAcctLatencyMax':bRadiusAcctLatencyMax,'bRadiusAcctLatencyAvg':bRadiusAcctLatencyAvg,'bRadiusAcctLatencyLast':bRadiusAcctLatencyLast,'bRadiusAcctAAAGroupName':bRadiusAcctAAAGroupName,'bRadiusClientCoATable':bRadiusClientCoATable,'bRadiusClientCoAEntry':bRadiusClientCoAEntry,_S:bRadiusCOAStatsInterval,_T:bRadiusCoAClientIndex,'bRadiusCoAClientInetAddressType':bRadiusCoAClientInetAddressType,'bRadiusCoAClientInetAddress':bRadiusCoAClientInetAddress,'bRadiusCoAIntervalDuration':bRadiusCoAIntervalDuration,'bRadiusCoAAckSent':bRadiusCoAAckSent,'bRadiusCoANackSent':bRadiusCoANackSent,'bRadiusCoARequestReceived':bRadiusCoARequestReceived,'bRadiusCoARequestDropped':bRadiusCoARequestDropped,'bRadiusCoAReqDropDueToDupReq':bRadiusCoAReqDropDueToDupReq,'bRadiusCoAReqDropDueToInvalidTime':bRadiusCoAReqDropDueToInvalidTime,'bRadiusCoAReqDropDueToBadAuthenticator':bRadiusCoAReqDropDueToBadAuthenticator,'bRadiusCoANackDueToInvalidReq':bRadiusCoANackDueToInvalidReq,'bRadiusCoANackDueToExceedMaxOutstanding':bRadiusCoANackDueToExceedMaxOutstanding,'bRadiusDisconnectRequestReceived':bRadiusDisconnectRequestReceived,'bRadiusDisconnectAckSent':bRadiusDisconnectAckSent,'bRadiusDisconnectNackSent':bRadiusDisconnectNackSent,'bRadiusDisconnectRequestDropped':bRadiusDisconnectRequestDropped,'bRadiusDisconnectReqDropDueToDupReq':bRadiusDisconnectReqDropDueToDupReq,'bRadiusDisconnectReqDropDueToInvalidTime':bRadiusDisconnectReqDropDueToInvalidTime,'bRadiusDisconnectReqDropDueToBadAuthenticator':bRadiusDisconnectReqDropDueToBadAuthenticator,'bRadiusDisconnectNackDueToInvalidReq':bRadiusDisconnectNackDueToInvalidReq,'bRadiusDisconnectNackDueToExceedMaxOutstanding':bRadiusDisconnectNackDueToExceedMaxOutstanding,'bRadiusCoALatencyMin':bRadiusCoALatencyMin,'bRadiusCoALatencyMax':bRadiusCoALatencyMax,'bRadiusCoALatencyAvg':bRadiusCoALatencyAvg,'bRadiusCoALatencyLast':bRadiusCoALatencyLast,'bRadiusCoADMLatencyMin':bRadiusCoADMLatencyMin,'bRadiusCoADMLatencyMax':bRadiusCoADMLatencyMax,'bRadiusCoADMLatencyAvg':bRadiusCoADMLatencyAvg,'bRadiusCoADMLatencyLast':bRadiusCoADMLatencyLast,'bRadiusCoAAAAGroupName':bRadiusCoAAAAGroupName,'bAAAGroupAuthTable':bAAAGroupAuthTable,'bAAAGroupAuthEntry':bAAAGroupAuthEntry,_U:bAAAGroupAuthStatsInterval,_V:bAAAGroupAuthIndex,_H:bAAAGroupAuthName,'bAAAGroupAuthIntervalDuration':bAAAGroupAuthIntervalDuration,_I:bAAAGroupMaximumOutstandingAuthReqs,'bAAAGroupPeakOutstandingAuthReqsReached':bAAAGroupPeakOutstandingAuthReqsReached,'bAAAGroupAuthReqsDropped':bAAAGroupAuthReqsDropped,_j:bAAAGroupOutstandingAuthReqsHighThreshold,_i:bAAAGroupOutstandingAuthReqsLowThreshold,'bAAAGroupAuthCurrentOutstanding':bAAAGroupAuthCurrentOutstanding,'bAAAGroupAcctTable':bAAAGroupAcctTable,'bAAAGroupAcctEntry':bAAAGroupAcctEntry,_W:bAAAGroupAcctStatsInterval,_X:bAAAGroupAcctIndex,_J:bAAAGroupAcctName,'bAAAGroupAcctIntervalDuration':bAAAGroupAcctIntervalDuration,_K:bAAAGroupMaximumOutstandingAcctReqs,'bAAAGroupPeakOutstandingAcctReqsReached':bAAAGroupPeakOutstandingAcctReqsReached,'bAAAGroupAcctReqsDropped':bAAAGroupAcctReqsDropped,_l:bAAAGroupOutstandingAcctReqsHighThreshold,_k:bAAAGroupOutstandingAcctReqsLowThreshold,'bAAAGroupAcctCurrentOutstanding':bAAAGroupAcctCurrentOutstanding,'bAAAGroupCoATable':bAAAGroupCoATable,'bAAAGroupCoAEntry':bAAAGroupCoAEntry,_Y:bAAAGroupCoAStatsInterval,_Z:bAAAGroupCoAIndex,_L:bAAAGroupCoAName,'bAAAGroupCoAIntervalDuration':bAAAGroupCoAIntervalDuration,'bAAAGroupCoANumOfClients':bAAAGroupCoANumOfClients,'bAAAGroupCoAReqsDropDueToInvalidClient':bAAAGroupCoAReqsDropDueToInvalidClient,'bAAAGroupDisconnectReqsDropDueToInvalidClient':bAAAGroupDisconnectReqsDropDueToInvalidClient,_M:bAAAGroupMaximumOutstandingCoAReqs,'bAAAGroupPeakOutstandingCoAReqs':bAAAGroupPeakOutstandingCoAReqs,_n:bAAAGroupOutstandingCoAReqsHighThreshold,_m:bAAAGroupOutstandingCoAReqsLowThreshold,'bAAAGroupCoaCurrentOutstanding':bAAAGroupCoaCurrentOutstanding,'bRadiusLatencyAuthTable':bRadiusLatencyAuthTable,'bRadiusLatencyAuthEntry':bRadiusLatencyAuthEntry,_a:bRadiusAuthLatencyStatsInterval,_b:bRadiusAuthInstanceIndex,'bRadiusAuthLatencyIntervalDuration':bRadiusAuthLatencyIntervalDuration,'bRadiusAuthRequestTotalPackets':bRadiusAuthRequestTotalPackets,'bRadiusAuthRequestMaximumProcessingTime':bRadiusAuthRequestMaximumProcessingTime,'bRadiusAuthRequestMinimumProcessingTime':bRadiusAuthRequestMinimumProcessingTime,'bRadiusAuthRequestAverageProcessingTime':bRadiusAuthRequestAverageProcessingTime,'bRadiusAuthRequestProcessingTimeGreaterthan1MS':bRadiusAuthRequestProcessingTimeGreaterthan1MS,'bRadiusAuthResponseTotalPackets':bRadiusAuthResponseTotalPackets,'bRadiusAuthResponseMaximumProcessingTime':bRadiusAuthResponseMaximumProcessingTime,'bRadiusAuthResponseMinimumProcessingTime':bRadiusAuthResponseMinimumProcessingTime,'bRadiusAuthResponseAverageProcessingTime':bRadiusAuthResponseAverageProcessingTime,'bRadiusAuthResponseProcessingTimeGreaterthan1MS':bRadiusAuthResponseProcessingTimeGreaterthan1MS,'bRadiusNotifObjects':bRadiusNotifObjects,_F:bRadiusServerIPAddrType,_G:bRadiusServerIPAddress,'bRadiusProxyMIBObjects':bRadiusProxyMIBObjects,'bRadiusProxyServerAuthTable':bRadiusProxyServerAuthTable,'bRadiusProxyServerAuthEntry':bRadiusProxyServerAuthEntry,_d:bRadiusProxyAuthStatsInterval,_e:bRadiusProxyAuthServerIndex,'bRadiusProxyAuthServerInetAddressType':bRadiusProxyAuthServerInetAddressType,'bRadiusProxyAuthServerInetAddress':bRadiusProxyAuthServerInetAddress,'bRadiusProxyAuthIntervalDuration':bRadiusProxyAuthIntervalDuration,'bRadiusProxyAccessRequestRcvd':bRadiusProxyAccessRequestRcvd,'bRadiusProxyAccessUnknownTypeRcvd':bRadiusProxyAccessUnknownTypeRcvd,'bRadiusProxyAccessUnknownClientRcvd':bRadiusProxyAccessUnknownClientRcvd,'bRadiusProxyAccessRequestDropped':bRadiusProxyAccessRequestDropped,'bRadiusProxyAccessSentFail':bRadiusProxyAccessSentFail,'bRadiusProxyAccessBadAuthenticatorRcvd':bRadiusProxyAccessBadAuthenticatorRcvd,'bRadiusProxyAccessAcceptRcvd':bRadiusProxyAccessAcceptRcvd,'bRadiusProxyAccessRejectRcvd':bRadiusProxyAccessRejectRcvd,'bRadiusProxyAccessChallengeRcvd':bRadiusProxyAccessChallengeRcvd,'bRadiusProxySubscriberBlocked':bRadiusProxySubscriberBlocked,'bRadiusProxySubscriberDeleted':bRadiusProxySubscriberDeleted,'bRadiusProxyServerAcctTable':bRadiusProxyServerAcctTable,'bRadiusProxyServerAcctEntry':bRadiusProxyServerAcctEntry,_f:bRadiusProxyAcctStatsInterval,_g:bRadiusProxyAcctServerIndex,'bRadiusProxyAcctServerInetAddressType':bRadiusProxyAcctServerInetAddressType,'bRadiusProxyAcctServerInetAddress':bRadiusProxyAcctServerInetAddress,'bRadiusProxyAcctIntervalDuration':bRadiusProxyAcctIntervalDuration,'bRadiusProxyAcctRequestRcvd':bRadiusProxyAcctRequestRcvd,'bRadiusProxyAcctRequestSent':bRadiusProxyAcctRequestSent,'bRadiusProxyAcctStartRequestRcvd':bRadiusProxyAcctStartRequestRcvd,'bRadiusProxyAcctStopRequestRcvd':bRadiusProxyAcctStopRequestRcvd,'bRadiusProxyAcctInterimUpdateRcvd':bRadiusProxyAcctInterimUpdateRcvd,'bRadiusProxyAcctStartRequestSent':bRadiusProxyAcctStartRequestSent,'bRadiusProxyAcctStopRequestSent':bRadiusProxyAcctStopRequestSent,'bRadiusProxyAcctInterimUpdateSent':bRadiusProxyAcctInterimUpdateSent,'bRadiusProxyAcctResponseRcvd':bRadiusProxyAcctResponseRcvd,'bRadiusProxyAcctResponseSent':bRadiusProxyAcctResponseSent,'bRadiusProxyAuthTPSTable':bRadiusProxyAuthTPSTable,'bRadiusProxyAuthTPSEntry':bRadiusProxyAuthTPSEntry,_h:bRadiusProxyAuthTPSInterval,'bRadiusProxyAuthTPSIntervalDuration':bRadiusProxyAuthTPSIntervalDuration,'bRadiusProxyAuthTPSLow':bRadiusProxyAuthTPSLow,'bRadiusProxyAuthTPSHigh':bRadiusProxyAuthTPSHigh,_N:bRadiusProxyAuthTPS,'bRadiusProxyNotifObjects':bRadiusProxyNotifObjects})