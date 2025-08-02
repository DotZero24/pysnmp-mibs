_AM='csmSdgCacheStatisticsGroup'
_AL='csmControllerStatisticsGroup'
_AK='csmSdgStatisticsGroup'
_AJ='csmGlobalStatisticsGroup'
_AI='csmNumOfPTRRecords'
_AH='csmNumOfAAAARecords'
_AG='csmNumOfARecords'
_AF='csmNumOfSRVRecords'
_AE='csmNumOfTXTRecords'
_AD='csmNumOfSrvTypes'
_AC='csmCntrlSrcInterface'
_AB='csmCntrlIpAddrType'
_AA='csmCntrlNextQueryTime'
_A9='csmCntrlTotalQueryExported'
_A8='csmCntrlPendingQueries'
_A7='csmCntrlQueryTimer'
_A6='csmCntrlQueryQueueSize'
_A5='csmCntrlQuerySuppression'
_A4='csmCntrlNextAnnouncementTime'
_A3='csmCntrlAnnouncementsExported'
_A2='csmCntrlPendingAnnouncements'
_A1='csmCntrlAnnouncementTimer'
_A0='csmCntrlAnnouncementQueueSize'
_z='csmCntrlDestPort'
_y='csmCntrlSrcPort'
_x='csmCntrlIpAddr'
_w='csmCntrlPktRcvdCnt'
_v='csmCntrlBCPWithdrawMsgSent'
_u='csmCntrlIpv6ServiceAdvertised'
_t='csmCntrlIpv4ServiceAdvertised'
_s='csmCntrlIpv6QueryResponses'
_r='csmCntrlIpv6QueryRequests'
_q='csmCntrlIpv4QueryRequests'
_p='csmCntrlIpv4QueryResponses'
_o='csmCntrlLastResync'
_n='csmCntrlTotalResync'
_m='csmCntrlTotalBCPMsgRcvd'
_l='csmCntrlTotalBCPMsgSent'
_k='csmCntrlDeadTimer'
_j='csmCntrlKeepAliveTimer'
_i='csmCntrlMD5Status'
_h='csmCntrlConnState'
_g='csmQueriesReceived'
_f='csmAdvertisementsReceived'
_e='csmIpv6PakSent'
_d='csmIpv4PakSent'
_c='csmMdnsGatewayState'
_b='csmIpv6QueryRcvdCnt'
_a='csmIpv6AdvertisementsRcvdCnt'
_Z='csmIpv4QueryRcvdCnt'
_Y='csmIpv4AdvertisementsRcvdCnt'
_X='csmIpv6QuerySentCnt'
_W='csmIpv6AdvertisementsSentCnt'
_V='csmIpv4QuerySentCnt'
_U='csmIpv4AdvertisementsSentCnt'
_T='csmPakDropped'
_S='csmMdnsPakRcvd'
_R='csmMdnsPakRateLtd'
_Q='csmUnicastSentCnt'
_P='csmMdnsPakSent'
_O='csmCacheMemInUse'
_N='csmCacheLimit'
_M='csmAvgOutRateHr'
_L='csmAvgOutRateFMin'
_K='csmAvgOutRateMin'
_J='csmAvgInRateHr'
_I='csmAvgInRateFMin'
_H='csmAvgInRateMin'
_G='csmCacheInterface'
_F='not-accessible'
_E='csmInterface'
_D='0'
_C='read-only'
_B='CISCO-SDG-MDNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,InterfaceIndexOrZero,TimeIntervalMin=mibBuilder.importSymbols('CISCO-TC','CiscoPort','InterfaceIndexOrZero','TimeIntervalMin')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeInterval','TruthValue')
ciscoSdgMdnsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,851))
if mibBuilder.loadTexts:ciscoSdgMdnsMIB.setRevisions(('2017-05-16 00:00',))
_CSdgMdnsMIBObjects_ObjectIdentity=ObjectIdentity
cSdgMdnsMIBObjects=_CSdgMdnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,851,1))
_CsmStatistics_ObjectIdentity=ObjectIdentity
csmStatistics=_CsmStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,851,1,1))
_CsmGlobalStatistics_ObjectIdentity=ObjectIdentity
csmGlobalStatistics=_CsmGlobalStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,851,1,1,1))
_CsmAvgInRateMin_Type=TimeIntervalMin
_CsmAvgInRateMin_Object=MibScalar
csmAvgInRateMin=_CsmAvgInRateMin_Object((1,3,6,1,4,1,9,9,851,1,1,1,1),_CsmAvgInRateMin_Type())
csmAvgInRateMin.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgInRateMin.setStatus(_A)
_CsmAvgInRateFMin_Type=TimeIntervalMin
_CsmAvgInRateFMin_Object=MibScalar
csmAvgInRateFMin=_CsmAvgInRateFMin_Object((1,3,6,1,4,1,9,9,851,1,1,1,2),_CsmAvgInRateFMin_Type())
csmAvgInRateFMin.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgInRateFMin.setStatus(_A)
_CsmAvgInRateHr_Type=TimeIntervalMin
_CsmAvgInRateHr_Object=MibScalar
csmAvgInRateHr=_CsmAvgInRateHr_Object((1,3,6,1,4,1,9,9,851,1,1,1,3),_CsmAvgInRateHr_Type())
csmAvgInRateHr.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgInRateHr.setStatus(_A)
_CsmAvgOutRateMin_Type=TimeIntervalMin
_CsmAvgOutRateMin_Object=MibScalar
csmAvgOutRateMin=_CsmAvgOutRateMin_Object((1,3,6,1,4,1,9,9,851,1,1,1,4),_CsmAvgOutRateMin_Type())
csmAvgOutRateMin.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgOutRateMin.setStatus(_A)
_CsmAvgOutRateFMin_Type=TimeIntervalMin
_CsmAvgOutRateFMin_Object=MibScalar
csmAvgOutRateFMin=_CsmAvgOutRateFMin_Object((1,3,6,1,4,1,9,9,851,1,1,1,5),_CsmAvgOutRateFMin_Type())
csmAvgOutRateFMin.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgOutRateFMin.setStatus(_A)
_CsmAvgOutRateHr_Type=TimeIntervalMin
_CsmAvgOutRateHr_Object=MibScalar
csmAvgOutRateHr=_CsmAvgOutRateHr_Object((1,3,6,1,4,1,9,9,851,1,1,1,6),_CsmAvgOutRateHr_Type())
csmAvgOutRateHr.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAvgOutRateHr.setStatus(_A)
_CsmCacheLimit_Type=Integer32
_CsmCacheLimit_Object=MibScalar
csmCacheLimit=_CsmCacheLimit_Object((1,3,6,1,4,1,9,9,851,1,1,1,7),_CsmCacheLimit_Type())
csmCacheLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCacheLimit.setStatus(_A)
if mibBuilder.loadTexts:csmCacheLimit.setUnits(_D)
_CsmCacheMemInUse_Type=Integer32
_CsmCacheMemInUse_Object=MibScalar
csmCacheMemInUse=_CsmCacheMemInUse_Object((1,3,6,1,4,1,9,9,851,1,1,1,8),_CsmCacheMemInUse_Type())
csmCacheMemInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCacheMemInUse.setStatus(_A)
if mibBuilder.loadTexts:csmCacheMemInUse.setUnits(_D)
_CsmSdgStatisticsTable_Object=MibTable
csmSdgStatisticsTable=_CsmSdgStatisticsTable_Object((1,3,6,1,4,1,9,9,851,1,1,2))
if mibBuilder.loadTexts:csmSdgStatisticsTable.setStatus(_A)
_CsmSdgStatisticsEntry_Object=MibTableRow
csmSdgStatisticsEntry=_CsmSdgStatisticsEntry_Object((1,3,6,1,4,1,9,9,851,1,1,2,1))
csmSdgStatisticsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:csmSdgStatisticsEntry.setStatus(_A)
_CsmInterface_Type=InterfaceIndexOrZero
_CsmInterface_Object=MibTableColumn
csmInterface=_CsmInterface_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,1),_CsmInterface_Type())
csmInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:csmInterface.setStatus(_A)
_CsmMdnsPakSent_Type=Counter32
_CsmMdnsPakSent_Object=MibTableColumn
csmMdnsPakSent=_CsmMdnsPakSent_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,2),_CsmMdnsPakSent_Type())
csmMdnsPakSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csmMdnsPakSent.setStatus(_A)
_CsmIpv4PakSent_Type=Counter32
_CsmIpv4PakSent_Object=MibTableColumn
csmIpv4PakSent=_CsmIpv4PakSent_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,3),_CsmIpv4PakSent_Type())
csmIpv4PakSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv4PakSent.setStatus(_A)
_CsmIpv6PakSent_Type=Counter32
_CsmIpv6PakSent_Object=MibTableColumn
csmIpv6PakSent=_CsmIpv6PakSent_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,4),_CsmIpv6PakSent_Type())
csmIpv6PakSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv6PakSent.setStatus(_A)
_CsmIpv4AdvertisementsSentCnt_Type=Counter32
_CsmIpv4AdvertisementsSentCnt_Object=MibTableColumn
csmIpv4AdvertisementsSentCnt=_CsmIpv4AdvertisementsSentCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,5),_CsmIpv4AdvertisementsSentCnt_Type())
csmIpv4AdvertisementsSentCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv4AdvertisementsSentCnt.setStatus(_A)
_CsmIpv6AdvertisementsSentCnt_Type=Counter32
_CsmIpv6AdvertisementsSentCnt_Object=MibTableColumn
csmIpv6AdvertisementsSentCnt=_CsmIpv6AdvertisementsSentCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,6),_CsmIpv6AdvertisementsSentCnt_Type())
csmIpv6AdvertisementsSentCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv6AdvertisementsSentCnt.setStatus(_A)
_CsmIpv4QuerySentCnt_Type=Counter32
_CsmIpv4QuerySentCnt_Object=MibTableColumn
csmIpv4QuerySentCnt=_CsmIpv4QuerySentCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,7),_CsmIpv4QuerySentCnt_Type())
csmIpv4QuerySentCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv4QuerySentCnt.setStatus(_A)
_CsmIpv6QuerySentCnt_Type=Counter32
_CsmIpv6QuerySentCnt_Object=MibTableColumn
csmIpv6QuerySentCnt=_CsmIpv6QuerySentCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,8),_CsmIpv6QuerySentCnt_Type())
csmIpv6QuerySentCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv6QuerySentCnt.setStatus(_A)
_CsmUnicastSentCnt_Type=Counter32
_CsmUnicastSentCnt_Object=MibTableColumn
csmUnicastSentCnt=_CsmUnicastSentCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,9),_CsmUnicastSentCnt_Type())
csmUnicastSentCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmUnicastSentCnt.setStatus(_A)
_CsmMdnsPakRateLtd_Type=Counter32
_CsmMdnsPakRateLtd_Object=MibTableColumn
csmMdnsPakRateLtd=_CsmMdnsPakRateLtd_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,10),_CsmMdnsPakRateLtd_Type())
csmMdnsPakRateLtd.setMaxAccess(_C)
if mibBuilder.loadTexts:csmMdnsPakRateLtd.setStatus(_A)
_CsmMdnsPakRcvd_Type=Counter32
_CsmMdnsPakRcvd_Object=MibTableColumn
csmMdnsPakRcvd=_CsmMdnsPakRcvd_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,11),_CsmMdnsPakRcvd_Type())
csmMdnsPakRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:csmMdnsPakRcvd.setStatus(_A)
_CsmAdvertisementsReceived_Type=Counter32
_CsmAdvertisementsReceived_Object=MibTableColumn
csmAdvertisementsReceived=_CsmAdvertisementsReceived_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,12),_CsmAdvertisementsReceived_Type())
csmAdvertisementsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:csmAdvertisementsReceived.setStatus(_A)
_CsmQueriesReceived_Type=Counter32
_CsmQueriesReceived_Object=MibTableColumn
csmQueriesReceived=_CsmQueriesReceived_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,13),_CsmQueriesReceived_Type())
csmQueriesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:csmQueriesReceived.setStatus(_A)
_CsmIpv4AdvertisementsRcvdCnt_Type=Counter32
_CsmIpv4AdvertisementsRcvdCnt_Object=MibTableColumn
csmIpv4AdvertisementsRcvdCnt=_CsmIpv4AdvertisementsRcvdCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,14),_CsmIpv4AdvertisementsRcvdCnt_Type())
csmIpv4AdvertisementsRcvdCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv4AdvertisementsRcvdCnt.setStatus(_A)
_CsmIpv6AdvertisementsRcvdCnt_Type=Counter32
_CsmIpv6AdvertisementsRcvdCnt_Object=MibTableColumn
csmIpv6AdvertisementsRcvdCnt=_CsmIpv6AdvertisementsRcvdCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,15),_CsmIpv6AdvertisementsRcvdCnt_Type())
csmIpv6AdvertisementsRcvdCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv6AdvertisementsRcvdCnt.setStatus(_A)
_CsmIpv4QueryRcvdCnt_Type=Counter32
_CsmIpv4QueryRcvdCnt_Object=MibTableColumn
csmIpv4QueryRcvdCnt=_CsmIpv4QueryRcvdCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,16),_CsmIpv4QueryRcvdCnt_Type())
csmIpv4QueryRcvdCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv4QueryRcvdCnt.setStatus(_A)
_CsmIpv6QueryRcvdCnt_Type=Counter32
_CsmIpv6QueryRcvdCnt_Object=MibTableColumn
csmIpv6QueryRcvdCnt=_CsmIpv6QueryRcvdCnt_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,17),_CsmIpv6QueryRcvdCnt_Type())
csmIpv6QueryRcvdCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmIpv6QueryRcvdCnt.setStatus(_A)
_CsmPakDropped_Type=Counter32
_CsmPakDropped_Object=MibTableColumn
csmPakDropped=_CsmPakDropped_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,18),_CsmPakDropped_Type())
csmPakDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:csmPakDropped.setStatus(_A)
_CsmMdnsGatewayState_Type=Integer32
_CsmMdnsGatewayState_Object=MibTableColumn
csmMdnsGatewayState=_CsmMdnsGatewayState_Object((1,3,6,1,4,1,9,9,851,1,1,2,1,19),_CsmMdnsGatewayState_Type())
csmMdnsGatewayState.setMaxAccess(_C)
if mibBuilder.loadTexts:csmMdnsGatewayState.setStatus(_A)
_CsmControllerStatistics_ObjectIdentity=ObjectIdentity
csmControllerStatistics=_CsmControllerStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,851,1,1,3))
_CsmCntrlIpAddrType_Type=InetAddressType
_CsmCntrlIpAddrType_Object=MibScalar
csmCntrlIpAddrType=_CsmCntrlIpAddrType_Object((1,3,6,1,4,1,9,9,851,1,1,3,1),_CsmCntrlIpAddrType_Type())
csmCntrlIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpAddrType.setStatus(_A)
_CsmCntrlIpAddr_Type=InetAddress
_CsmCntrlIpAddr_Object=MibScalar
csmCntrlIpAddr=_CsmCntrlIpAddr_Object((1,3,6,1,4,1,9,9,851,1,1,3,2),_CsmCntrlIpAddr_Type())
csmCntrlIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpAddr.setStatus(_A)
_CsmCntrlConnState_Type=Integer32
_CsmCntrlConnState_Object=MibScalar
csmCntrlConnState=_CsmCntrlConnState_Object((1,3,6,1,4,1,9,9,851,1,1,3,3),_CsmCntrlConnState_Type())
csmCntrlConnState.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlConnState.setStatus(_A)
_CsmCntrlSrcPort_Type=CiscoPort
_CsmCntrlSrcPort_Object=MibScalar
csmCntrlSrcPort=_CsmCntrlSrcPort_Object((1,3,6,1,4,1,9,9,851,1,1,3,4),_CsmCntrlSrcPort_Type())
csmCntrlSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlSrcPort.setStatus(_A)
_CsmCntrlDestPort_Type=CiscoPort
_CsmCntrlDestPort_Object=MibScalar
csmCntrlDestPort=_CsmCntrlDestPort_Object((1,3,6,1,4,1,9,9,851,1,1,3,5),_CsmCntrlDestPort_Type())
csmCntrlDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlDestPort.setStatus(_A)
_CsmCntrlSrcInterface_Type=OctetString
_CsmCntrlSrcInterface_Object=MibScalar
csmCntrlSrcInterface=_CsmCntrlSrcInterface_Object((1,3,6,1,4,1,9,9,851,1,1,3,6),_CsmCntrlSrcInterface_Type())
csmCntrlSrcInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlSrcInterface.setStatus(_A)
_CsmCntrlMD5Status_Type=TruthValue
_CsmCntrlMD5Status_Object=MibScalar
csmCntrlMD5Status=_CsmCntrlMD5Status_Object((1,3,6,1,4,1,9,9,851,1,1,3,7),_CsmCntrlMD5Status_Type())
csmCntrlMD5Status.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlMD5Status.setStatus(_A)
_CsmCntrlKeepAliveTimer_Type=TimeInterval
_CsmCntrlKeepAliveTimer_Object=MibScalar
csmCntrlKeepAliveTimer=_CsmCntrlKeepAliveTimer_Object((1,3,6,1,4,1,9,9,851,1,1,3,8),_CsmCntrlKeepAliveTimer_Type())
csmCntrlKeepAliveTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlKeepAliveTimer.setStatus(_A)
_CsmCntrlDeadTimer_Type=TimeInterval
_CsmCntrlDeadTimer_Object=MibScalar
csmCntrlDeadTimer=_CsmCntrlDeadTimer_Object((1,3,6,1,4,1,9,9,851,1,1,3,9),_CsmCntrlDeadTimer_Type())
csmCntrlDeadTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlDeadTimer.setStatus(_A)
_CsmCntrlTotalBCPMsgSent_Type=Counter32
_CsmCntrlTotalBCPMsgSent_Object=MibScalar
csmCntrlTotalBCPMsgSent=_CsmCntrlTotalBCPMsgSent_Object((1,3,6,1,4,1,9,9,851,1,1,3,10),_CsmCntrlTotalBCPMsgSent_Type())
csmCntrlTotalBCPMsgSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlTotalBCPMsgSent.setStatus(_A)
_CsmCntrlTotalBCPMsgRcvd_Type=Counter32
_CsmCntrlTotalBCPMsgRcvd_Object=MibScalar
csmCntrlTotalBCPMsgRcvd=_CsmCntrlTotalBCPMsgRcvd_Object((1,3,6,1,4,1,9,9,851,1,1,3,11),_CsmCntrlTotalBCPMsgRcvd_Type())
csmCntrlTotalBCPMsgRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlTotalBCPMsgRcvd.setStatus(_A)
_CsmCntrlBCPWithdrawMsgSent_Type=Counter32
_CsmCntrlBCPWithdrawMsgSent_Object=MibScalar
csmCntrlBCPWithdrawMsgSent=_CsmCntrlBCPWithdrawMsgSent_Object((1,3,6,1,4,1,9,9,851,1,1,3,12),_CsmCntrlBCPWithdrawMsgSent_Type())
csmCntrlBCPWithdrawMsgSent.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlBCPWithdrawMsgSent.setStatus(_A)
_CsmCntrlIpv4QueryRequests_Type=Counter32
_CsmCntrlIpv4QueryRequests_Object=MibScalar
csmCntrlIpv4QueryRequests=_CsmCntrlIpv4QueryRequests_Object((1,3,6,1,4,1,9,9,851,1,1,3,13),_CsmCntrlIpv4QueryRequests_Type())
csmCntrlIpv4QueryRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv4QueryRequests.setStatus(_A)
_CsmCntrlIpv4QueryResponses_Type=Counter32
_CsmCntrlIpv4QueryResponses_Object=MibScalar
csmCntrlIpv4QueryResponses=_CsmCntrlIpv4QueryResponses_Object((1,3,6,1,4,1,9,9,851,1,1,3,14),_CsmCntrlIpv4QueryResponses_Type())
csmCntrlIpv4QueryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv4QueryResponses.setStatus(_A)
_CsmCntrlIpv6QueryRequests_Type=Counter32
_CsmCntrlIpv6QueryRequests_Object=MibScalar
csmCntrlIpv6QueryRequests=_CsmCntrlIpv6QueryRequests_Object((1,3,6,1,4,1,9,9,851,1,1,3,15),_CsmCntrlIpv6QueryRequests_Type())
csmCntrlIpv6QueryRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv6QueryRequests.setStatus(_A)
_CsmCntrlIpv6QueryResponses_Type=Counter32
_CsmCntrlIpv6QueryResponses_Object=MibScalar
csmCntrlIpv6QueryResponses=_CsmCntrlIpv6QueryResponses_Object((1,3,6,1,4,1,9,9,851,1,1,3,16),_CsmCntrlIpv6QueryResponses_Type())
csmCntrlIpv6QueryResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv6QueryResponses.setStatus(_A)
_CsmCntrlIpv4ServiceAdvertised_Type=Counter32
_CsmCntrlIpv4ServiceAdvertised_Object=MibScalar
csmCntrlIpv4ServiceAdvertised=_CsmCntrlIpv4ServiceAdvertised_Object((1,3,6,1,4,1,9,9,851,1,1,3,17),_CsmCntrlIpv4ServiceAdvertised_Type())
csmCntrlIpv4ServiceAdvertised.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv4ServiceAdvertised.setStatus(_A)
_CsmCntrlIpv6ServiceAdvertised_Type=Counter32
_CsmCntrlIpv6ServiceAdvertised_Object=MibScalar
csmCntrlIpv6ServiceAdvertised=_CsmCntrlIpv6ServiceAdvertised_Object((1,3,6,1,4,1,9,9,851,1,1,3,18),_CsmCntrlIpv6ServiceAdvertised_Type())
csmCntrlIpv6ServiceAdvertised.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlIpv6ServiceAdvertised.setStatus(_A)
_CsmCntrlPktRcvdCnt_Type=Counter32
_CsmCntrlPktRcvdCnt_Object=MibScalar
csmCntrlPktRcvdCnt=_CsmCntrlPktRcvdCnt_Object((1,3,6,1,4,1,9,9,851,1,1,3,19),_CsmCntrlPktRcvdCnt_Type())
csmCntrlPktRcvdCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlPktRcvdCnt.setStatus(_A)
_CsmCntrlAnnouncementQueueSize_Type=Integer32
_CsmCntrlAnnouncementQueueSize_Object=MibScalar
csmCntrlAnnouncementQueueSize=_CsmCntrlAnnouncementQueueSize_Object((1,3,6,1,4,1,9,9,851,1,1,3,20),_CsmCntrlAnnouncementQueueSize_Type())
csmCntrlAnnouncementQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlAnnouncementQueueSize.setStatus(_A)
_CsmCntrlAnnouncementTimer_Type=TimeInterval
_CsmCntrlAnnouncementTimer_Object=MibScalar
csmCntrlAnnouncementTimer=_CsmCntrlAnnouncementTimer_Object((1,3,6,1,4,1,9,9,851,1,1,3,21),_CsmCntrlAnnouncementTimer_Type())
csmCntrlAnnouncementTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlAnnouncementTimer.setStatus(_A)
_CsmCntrlAnnouncementsExported_Type=Counter32
_CsmCntrlAnnouncementsExported_Object=MibScalar
csmCntrlAnnouncementsExported=_CsmCntrlAnnouncementsExported_Object((1,3,6,1,4,1,9,9,851,1,1,3,22),_CsmCntrlAnnouncementsExported_Type())
csmCntrlAnnouncementsExported.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlAnnouncementsExported.setStatus(_A)
_CsmCntrlPendingAnnouncements_Type=Counter32
_CsmCntrlPendingAnnouncements_Object=MibScalar
csmCntrlPendingAnnouncements=_CsmCntrlPendingAnnouncements_Object((1,3,6,1,4,1,9,9,851,1,1,3,23),_CsmCntrlPendingAnnouncements_Type())
csmCntrlPendingAnnouncements.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlPendingAnnouncements.setStatus(_A)
_CsmCntrlNextAnnouncementTime_Type=TimeInterval
_CsmCntrlNextAnnouncementTime_Object=MibScalar
csmCntrlNextAnnouncementTime=_CsmCntrlNextAnnouncementTime_Object((1,3,6,1,4,1,9,9,851,1,1,3,24),_CsmCntrlNextAnnouncementTime_Type())
csmCntrlNextAnnouncementTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlNextAnnouncementTime.setStatus(_A)
_CsmCntrlQuerySuppression_Type=TruthValue
_CsmCntrlQuerySuppression_Object=MibScalar
csmCntrlQuerySuppression=_CsmCntrlQuerySuppression_Object((1,3,6,1,4,1,9,9,851,1,1,3,25),_CsmCntrlQuerySuppression_Type())
csmCntrlQuerySuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlQuerySuppression.setStatus(_A)
_CsmCntrlPendingQueries_Type=Counter32
_CsmCntrlPendingQueries_Object=MibScalar
csmCntrlPendingQueries=_CsmCntrlPendingQueries_Object((1,3,6,1,4,1,9,9,851,1,1,3,26),_CsmCntrlPendingQueries_Type())
csmCntrlPendingQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlPendingQueries.setStatus(_A)
_CsmCntrlQueryQueueSize_Type=Integer32
_CsmCntrlQueryQueueSize_Object=MibScalar
csmCntrlQueryQueueSize=_CsmCntrlQueryQueueSize_Object((1,3,6,1,4,1,9,9,851,1,1,3,27),_CsmCntrlQueryQueueSize_Type())
csmCntrlQueryQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlQueryQueueSize.setStatus(_A)
_CsmCntrlQueryTimer_Type=TimeInterval
_CsmCntrlQueryTimer_Object=MibScalar
csmCntrlQueryTimer=_CsmCntrlQueryTimer_Object((1,3,6,1,4,1,9,9,851,1,1,3,28),_CsmCntrlQueryTimer_Type())
csmCntrlQueryTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlQueryTimer.setStatus(_A)
_CsmCntrlNextQueryTime_Type=TimeInterval
_CsmCntrlNextQueryTime_Object=MibScalar
csmCntrlNextQueryTime=_CsmCntrlNextQueryTime_Object((1,3,6,1,4,1,9,9,851,1,1,3,29),_CsmCntrlNextQueryTime_Type())
csmCntrlNextQueryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlNextQueryTime.setStatus(_A)
_CsmCntrlTotalQueryExported_Type=Counter32
_CsmCntrlTotalQueryExported_Object=MibScalar
csmCntrlTotalQueryExported=_CsmCntrlTotalQueryExported_Object((1,3,6,1,4,1,9,9,851,1,1,3,30),_CsmCntrlTotalQueryExported_Type())
csmCntrlTotalQueryExported.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlTotalQueryExported.setStatus(_A)
_CsmCntrlTotalResync_Type=Counter32
_CsmCntrlTotalResync_Object=MibScalar
csmCntrlTotalResync=_CsmCntrlTotalResync_Object((1,3,6,1,4,1,9,9,851,1,1,3,31),_CsmCntrlTotalResync_Type())
csmCntrlTotalResync.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlTotalResync.setStatus(_A)
_CsmCntrlLastResync_Type=DateAndTime
_CsmCntrlLastResync_Object=MibScalar
csmCntrlLastResync=_CsmCntrlLastResync_Object((1,3,6,1,4,1,9,9,851,1,1,3,32),_CsmCntrlLastResync_Type())
csmCntrlLastResync.setMaxAccess(_C)
if mibBuilder.loadTexts:csmCntrlLastResync.setStatus(_A)
_CsmSdgCacheStatisticsTable_Object=MibTable
csmSdgCacheStatisticsTable=_CsmSdgCacheStatisticsTable_Object((1,3,6,1,4,1,9,9,851,1,1,4))
if mibBuilder.loadTexts:csmSdgCacheStatisticsTable.setStatus(_A)
_CsmSdgCacheStatisticsEntry_Object=MibTableRow
csmSdgCacheStatisticsEntry=_CsmSdgCacheStatisticsEntry_Object((1,3,6,1,4,1,9,9,851,1,1,4,1))
csmSdgCacheStatisticsEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:csmSdgCacheStatisticsEntry.setStatus(_A)
_CsmCacheInterface_Type=InterfaceIndexOrZero
_CsmCacheInterface_Object=MibTableColumn
csmCacheInterface=_CsmCacheInterface_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,1),_CsmCacheInterface_Type())
csmCacheInterface.setMaxAccess(_F)
if mibBuilder.loadTexts:csmCacheInterface.setStatus(_A)
_CsmNumOfSrvTypes_Type=Integer32
_CsmNumOfSrvTypes_Object=MibTableColumn
csmNumOfSrvTypes=_CsmNumOfSrvTypes_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,2),_CsmNumOfSrvTypes_Type())
csmNumOfSrvTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfSrvTypes.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfSrvTypes.setUnits(_D)
_CsmNumOfAAAARecords_Type=Counter32
_CsmNumOfAAAARecords_Object=MibTableColumn
csmNumOfAAAARecords=_CsmNumOfAAAARecords_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,3),_CsmNumOfAAAARecords_Type())
csmNumOfAAAARecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfAAAARecords.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfAAAARecords.setUnits(_D)
_CsmNumOfTXTRecords_Type=Counter32
_CsmNumOfTXTRecords_Object=MibTableColumn
csmNumOfTXTRecords=_CsmNumOfTXTRecords_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,4),_CsmNumOfTXTRecords_Type())
csmNumOfTXTRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfTXTRecords.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfTXTRecords.setUnits(_D)
_CsmNumOfSRVRecords_Type=Counter32
_CsmNumOfSRVRecords_Object=MibTableColumn
csmNumOfSRVRecords=_CsmNumOfSRVRecords_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,5),_CsmNumOfSRVRecords_Type())
csmNumOfSRVRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfSRVRecords.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfSRVRecords.setUnits(_D)
_CsmNumOfPTRRecords_Type=Counter32
_CsmNumOfPTRRecords_Object=MibTableColumn
csmNumOfPTRRecords=_CsmNumOfPTRRecords_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,6),_CsmNumOfPTRRecords_Type())
csmNumOfPTRRecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfPTRRecords.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfPTRRecords.setUnits(_D)
_CsmNumOfARecords_Type=Counter32
_CsmNumOfARecords_Object=MibTableColumn
csmNumOfARecords=_CsmNumOfARecords_Object((1,3,6,1,4,1,9,9,851,1,1,4,1,7),_CsmNumOfARecords_Type())
csmNumOfARecords.setMaxAccess(_C)
if mibBuilder.loadTexts:csmNumOfARecords.setStatus(_A)
if mibBuilder.loadTexts:csmNumOfARecords.setUnits(_D)
_CSdgMdnsMIBConformance_ObjectIdentity=ObjectIdentity
cSdgMdnsMIBConformance=_CSdgMdnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,851,2))
_CsmMIBCompliances_ObjectIdentity=ObjectIdentity
csmMIBCompliances=_CsmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,851,2,1))
_CsmMIBGroups_ObjectIdentity=ObjectIdentity
csmMIBGroups=_CsmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,851,2,2))
csmGlobalStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,851,2,2,1))
csmGlobalStatisticsGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:csmGlobalStatisticsGroup.setStatus(_A)
csmSdgStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,851,2,2,2))
csmSdgStatisticsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:csmSdgStatisticsGroup.setStatus(_A)
csmControllerStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,851,2,2,3))
csmControllerStatisticsGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:csmControllerStatisticsGroup.setStatus(_A)
csmSdgCacheStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,851,2,2,4))
csmSdgCacheStatisticsGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:csmSdgCacheStatisticsGroup.setStatus(_A)
csmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,851,2,1,1))
csmMIBCompliance.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:csmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoSdgMdnsMIB':ciscoSdgMdnsMIB,'cSdgMdnsMIBObjects':cSdgMdnsMIBObjects,'csmStatistics':csmStatistics,'csmGlobalStatistics':csmGlobalStatistics,_H:csmAvgInRateMin,_I:csmAvgInRateFMin,_J:csmAvgInRateHr,_K:csmAvgOutRateMin,_L:csmAvgOutRateFMin,_M:csmAvgOutRateHr,_N:csmCacheLimit,_O:csmCacheMemInUse,'csmSdgStatisticsTable':csmSdgStatisticsTable,'csmSdgStatisticsEntry':csmSdgStatisticsEntry,_E:csmInterface,_P:csmMdnsPakSent,_d:csmIpv4PakSent,_e:csmIpv6PakSent,_U:csmIpv4AdvertisementsSentCnt,_W:csmIpv6AdvertisementsSentCnt,_V:csmIpv4QuerySentCnt,_X:csmIpv6QuerySentCnt,_Q:csmUnicastSentCnt,_R:csmMdnsPakRateLtd,_S:csmMdnsPakRcvd,_f:csmAdvertisementsReceived,_g:csmQueriesReceived,_Y:csmIpv4AdvertisementsRcvdCnt,_a:csmIpv6AdvertisementsRcvdCnt,_Z:csmIpv4QueryRcvdCnt,_b:csmIpv6QueryRcvdCnt,_T:csmPakDropped,_c:csmMdnsGatewayState,'csmControllerStatistics':csmControllerStatistics,_AB:csmCntrlIpAddrType,_x:csmCntrlIpAddr,_h:csmCntrlConnState,_y:csmCntrlSrcPort,_z:csmCntrlDestPort,_AC:csmCntrlSrcInterface,_i:csmCntrlMD5Status,_j:csmCntrlKeepAliveTimer,_k:csmCntrlDeadTimer,_l:csmCntrlTotalBCPMsgSent,_m:csmCntrlTotalBCPMsgRcvd,_v:csmCntrlBCPWithdrawMsgSent,_q:csmCntrlIpv4QueryRequests,_p:csmCntrlIpv4QueryResponses,_r:csmCntrlIpv6QueryRequests,_s:csmCntrlIpv6QueryResponses,_t:csmCntrlIpv4ServiceAdvertised,_u:csmCntrlIpv6ServiceAdvertised,_w:csmCntrlPktRcvdCnt,_A0:csmCntrlAnnouncementQueueSize,_A1:csmCntrlAnnouncementTimer,_A3:csmCntrlAnnouncementsExported,_A2:csmCntrlPendingAnnouncements,_A4:csmCntrlNextAnnouncementTime,_A5:csmCntrlQuerySuppression,_A8:csmCntrlPendingQueries,_A6:csmCntrlQueryQueueSize,_A7:csmCntrlQueryTimer,_AA:csmCntrlNextQueryTime,_A9:csmCntrlTotalQueryExported,_n:csmCntrlTotalResync,_o:csmCntrlLastResync,'csmSdgCacheStatisticsTable':csmSdgCacheStatisticsTable,'csmSdgCacheStatisticsEntry':csmSdgCacheStatisticsEntry,_G:csmCacheInterface,_AD:csmNumOfSrvTypes,_AH:csmNumOfAAAARecords,_AE:csmNumOfTXTRecords,_AF:csmNumOfSRVRecords,_AI:csmNumOfPTRRecords,_AG:csmNumOfARecords,'cSdgMdnsMIBConformance':cSdgMdnsMIBConformance,'csmMIBCompliances':csmMIBCompliances,'csmMIBCompliance':csmMIBCompliance,'csmMIBGroups':csmMIBGroups,_AJ:csmGlobalStatisticsGroup,_AK:csmSdgStatisticsGroup,_AL:csmControllerStatisticsGroup,_AM:csmSdgCacheStatisticsGroup})