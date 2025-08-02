_q='sfpsSubnetResolveHashIndex'
_p='sfpsSubnetResolveSourceHash'
_o='sfpsSubnetResolveTargetTag'
_n='invalid'
_m='internal'
_l='external'
_k='clearTable'
_j='delete'
_i='sfpsTableResolveHashIndex'
_h='sfpsTableResolveHash'
_g='sfpsTableResolveTag'
_f='sfpsUnresolveTableHashIndex'
_e='sfpsUnresolveTableHash'
_d='set-parameter'
_c='aoInetIPMask'
_b='aoNetBiosName'
_a='aoHostName'
_Z='aoVlan'
_Y='aoEmpty'
_X='aoAtDDP'
_W='aoMacDXMcast'
_V='aoInetRIP'
_U='aoInetRPC'
_T='aoInetIP'
_S='aoIpxIpx'
_R='aoInetUDP'
_Q='aoInetYP'
_P='aoIpxRIP'
_O='aoIpxSap'
_N='aoMacDX'
_M='sfpsBlockResolveTableHashIndex'
_L='sfpsBlockResolveTableHash'
_K='sfpsSwitchResolveCallTag'
_J='sfpsSwitchResolveSwitch'
_I='sfpsServiceCenterResolveHashLeaf'
_H='enable'
_G='disable'
_F='other'
_E='CTRON-SFPS-RESOLVE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsBlockResolve,sfpsBlockResolveAPI,sfpsBlockResolveStats,sfpsISPResolve,sfpsMobilityStats,sfpsRelayAgentResolve,sfpsRelayAgentResolveStats,sfpsResolveStats,sfpsSubnetResolve,sfpsSubnetResolveAPI,sfpsSubnetResolveNvram,sfpsSubnetResolveStats,sfpsSwitchResolve,sfpsTableResolve,sfpsTableResolveAPI,sfpsUnresolve,sfpsUnresolveTableAPI,sfpsUnresolveTableStats=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsBlockResolve','sfpsBlockResolveAPI','sfpsBlockResolveStats','sfpsISPResolve','sfpsMobilityStats','sfpsRelayAgentResolve','sfpsRelayAgentResolveStats','sfpsResolveStats','sfpsSubnetResolve','sfpsSubnetResolveAPI','sfpsSubnetResolveNvram','sfpsSubnetResolveStats','sfpsSwitchResolve','sfpsTableResolve','sfpsTableResolveAPI','sfpsUnresolve','sfpsUnresolveTableAPI','sfpsUnresolveTableStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SfpsServiceCenterResolveTable_Object=MibTable
sfpsServiceCenterResolveTable=_SfpsServiceCenterResolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1))
if mibBuilder.loadTexts:sfpsServiceCenterResolveTable.setStatus(_A)
_SfpsServiceCenterResolveEntry_Object=MibTableRow
sfpsServiceCenterResolveEntry=_SfpsServiceCenterResolveEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1))
sfpsServiceCenterResolveEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:sfpsServiceCenterResolveEntry.setStatus(_A)
_SfpsServiceCenterResolveHashLeaf_Type=HexInteger
_SfpsServiceCenterResolveHashLeaf_Object=MibTableColumn
sfpsServiceCenterResolveHashLeaf=_SfpsServiceCenterResolveHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,1),_SfpsServiceCenterResolveHashLeaf_Type())
sfpsServiceCenterResolveHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveHashLeaf.setStatus(_A)
_SfpsServiceCenterResolveMetric_Type=Integer32
_SfpsServiceCenterResolveMetric_Object=MibTableColumn
sfpsServiceCenterResolveMetric=_SfpsServiceCenterResolveMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,2),_SfpsServiceCenterResolveMetric_Type())
sfpsServiceCenterResolveMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveMetric.setStatus(_A)
_SfpsServiceCenterResolveName_Type=DisplayString
_SfpsServiceCenterResolveName_Object=MibTableColumn
sfpsServiceCenterResolveName=_SfpsServiceCenterResolveName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,3),_SfpsServiceCenterResolveName_Type())
sfpsServiceCenterResolveName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveName.setStatus(_A)
class _SfpsServiceCenterResolveOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterResolveOperStatus_Type.__name__=_D
_SfpsServiceCenterResolveOperStatus_Object=MibTableColumn
sfpsServiceCenterResolveOperStatus=_SfpsServiceCenterResolveOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,4),_SfpsServiceCenterResolveOperStatus_Type())
sfpsServiceCenterResolveOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveOperStatus.setStatus(_A)
class _SfpsServiceCenterResolveAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsServiceCenterResolveAdminStatus_Type.__name__=_D
_SfpsServiceCenterResolveAdminStatus_Object=MibTableColumn
sfpsServiceCenterResolveAdminStatus=_SfpsServiceCenterResolveAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,5),_SfpsServiceCenterResolveAdminStatus_Type())
sfpsServiceCenterResolveAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsServiceCenterResolveAdminStatus.setStatus(_A)
_SfpsServiceCenterResolveStatusTime_Type=TimeTicks
_SfpsServiceCenterResolveStatusTime_Object=MibTableColumn
sfpsServiceCenterResolveStatusTime=_SfpsServiceCenterResolveStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,6),_SfpsServiceCenterResolveStatusTime_Type())
sfpsServiceCenterResolveStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveStatusTime.setStatus(_A)
_SfpsServiceCenterResolveRequests_Type=Integer32
_SfpsServiceCenterResolveRequests_Object=MibTableColumn
sfpsServiceCenterResolveRequests=_SfpsServiceCenterResolveRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,7),_SfpsServiceCenterResolveRequests_Type())
sfpsServiceCenterResolveRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveRequests.setStatus(_A)
_SfpsServiceCenterResolveResponses_Type=Integer32
_SfpsServiceCenterResolveResponses_Object=MibTableColumn
sfpsServiceCenterResolveResponses=_SfpsServiceCenterResolveResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,1,1,8),_SfpsServiceCenterResolveResponses_Type())
sfpsServiceCenterResolveResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterResolveResponses.setStatus(_A)
_SfpsSwitchResolveTable_Object=MibTable
sfpsSwitchResolveTable=_SfpsSwitchResolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1))
if mibBuilder.loadTexts:sfpsSwitchResolveTable.setStatus(_A)
_SfpsSwitchResolveEntry_Object=MibTableRow
sfpsSwitchResolveEntry=_SfpsSwitchResolveEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1))
sfpsSwitchResolveEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:sfpsSwitchResolveEntry.setStatus(_A)
_SfpsSwitchResolveSwitch_Type=OctetString
_SfpsSwitchResolveSwitch_Object=MibTableColumn
sfpsSwitchResolveSwitch=_SfpsSwitchResolveSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,1),_SfpsSwitchResolveSwitch_Type())
sfpsSwitchResolveSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveSwitch.setStatus(_A)
_SfpsSwitchResolveCallTag_Type=Integer32
_SfpsSwitchResolveCallTag_Object=MibTableColumn
sfpsSwitchResolveCallTag=_SfpsSwitchResolveCallTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,2),_SfpsSwitchResolveCallTag_Type())
sfpsSwitchResolveCallTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveCallTag.setStatus(_A)
_SfpsSwitchResolvePortNum_Type=Integer32
_SfpsSwitchResolvePortNum_Object=MibTableColumn
sfpsSwitchResolvePortNum=_SfpsSwitchResolvePortNum_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,3),_SfpsSwitchResolvePortNum_Type())
sfpsSwitchResolvePortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolvePortNum.setStatus(_A)
_SfpsSwitchResolveNeighborSw_Type=OctetString
_SfpsSwitchResolveNeighborSw_Object=MibTableColumn
sfpsSwitchResolveNeighborSw=_SfpsSwitchResolveNeighborSw_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,4),_SfpsSwitchResolveNeighborSw_Type())
sfpsSwitchResolveNeighborSw.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveNeighborSw.setStatus(_A)
_SfpsSwitchResolveRequestCount_Type=Integer32
_SfpsSwitchResolveRequestCount_Object=MibTableColumn
sfpsSwitchResolveRequestCount=_SfpsSwitchResolveRequestCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,5),_SfpsSwitchResolveRequestCount_Type())
sfpsSwitchResolveRequestCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveRequestCount.setStatus(_A)
_SfpsSwitchResolveResponseCount_Type=Integer32
_SfpsSwitchResolveResponseCount_Object=MibTableColumn
sfpsSwitchResolveResponseCount=_SfpsSwitchResolveResponseCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,6),_SfpsSwitchResolveResponseCount_Type())
sfpsSwitchResolveResponseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveResponseCount.setStatus(_A)
_SfpsSwitchResolveMobilityRetry_Type=Integer32
_SfpsSwitchResolveMobilityRetry_Object=MibTableColumn
sfpsSwitchResolveMobilityRetry=_SfpsSwitchResolveMobilityRetry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,7),_SfpsSwitchResolveMobilityRetry_Type())
sfpsSwitchResolveMobilityRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveMobilityRetry.setStatus(_A)
_SfpsSwitchResolveEventId_Type=Integer32
_SfpsSwitchResolveEventId_Object=MibTableColumn
sfpsSwitchResolveEventId=_SfpsSwitchResolveEventId_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,2,1,1,8),_SfpsSwitchResolveEventId_Type())
sfpsSwitchResolveEventId.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchResolveEventId.setStatus(_A)
_SfpsResolveStatsRequests_Type=Integer32
_SfpsResolveStatsRequests_Object=MibScalar
sfpsResolveStatsRequests=_SfpsResolveStatsRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,1),_SfpsResolveStatsRequests_Type())
sfpsResolveStatsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsRequests.setStatus(_A)
_SfpsResolveStatsResponses_Type=Integer32
_SfpsResolveStatsResponses_Object=MibScalar
sfpsResolveStatsResponses=_SfpsResolveStatsResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,2),_SfpsResolveStatsResponses_Type())
sfpsResolveStatsResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsResponses.setStatus(_A)
_SfpsResolveStatsAcks_Type=Integer32
_SfpsResolveStatsAcks_Object=MibScalar
sfpsResolveStatsAcks=_SfpsResolveStatsAcks_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,3),_SfpsResolveStatsAcks_Type())
sfpsResolveStatsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsAcks.setStatus(_A)
_SfpsResolveStatsNaks_Type=Integer32
_SfpsResolveStatsNaks_Object=MibScalar
sfpsResolveStatsNaks=_SfpsResolveStatsNaks_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,4),_SfpsResolveStatsNaks_Type())
sfpsResolveStatsNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsNaks.setStatus(_A)
_SfpsResolveStatsUnknowns_Type=Integer32
_SfpsResolveStatsUnknowns_Object=MibScalar
sfpsResolveStatsUnknowns=_SfpsResolveStatsUnknowns_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,5),_SfpsResolveStatsUnknowns_Type())
sfpsResolveStatsUnknowns.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsUnknowns.setStatus(_A)
_SfpsResolveStatsNoAnswer_Type=Integer32
_SfpsResolveStatsNoAnswer_Object=MibScalar
sfpsResolveStatsNoAnswer=_SfpsResolveStatsNoAnswer_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,6),_SfpsResolveStatsNoAnswer_Type())
sfpsResolveStatsNoAnswer.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsNoAnswer.setStatus(_A)
_SfpsResolveStatsTimeout_Type=Integer32
_SfpsResolveStatsTimeout_Object=MibScalar
sfpsResolveStatsTimeout=_SfpsResolveStatsTimeout_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,7),_SfpsResolveStatsTimeout_Type())
sfpsResolveStatsTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsTimeout.setStatus(_A)
_SfpsResolveStatsAvgResponseTime_Type=Integer32
_SfpsResolveStatsAvgResponseTime_Object=MibScalar
sfpsResolveStatsAvgResponseTime=_SfpsResolveStatsAvgResponseTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,8),_SfpsResolveStatsAvgResponseTime_Type())
sfpsResolveStatsAvgResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsAvgResponseTime.setStatus(_A)
_SfpsResolveStatsTableSize_Type=Integer32
_SfpsResolveStatsTableSize_Object=MibScalar
sfpsResolveStatsTableSize=_SfpsResolveStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,9),_SfpsResolveStatsTableSize_Type())
sfpsResolveStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsTableSize.setStatus(_A)
_SfpsResolveStatsTableHigh_Type=Integer32
_SfpsResolveStatsTableHigh_Object=MibScalar
sfpsResolveStatsTableHigh=_SfpsResolveStatsTableHigh_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,10),_SfpsResolveStatsTableHigh_Type())
sfpsResolveStatsTableHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsTableHigh.setStatus(_A)
_SfpsResolveStatsErrorCount_Type=Integer32
_SfpsResolveStatsErrorCount_Object=MibScalar
sfpsResolveStatsErrorCount=_SfpsResolveStatsErrorCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,11),_SfpsResolveStatsErrorCount_Type())
sfpsResolveStatsErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsErrorCount.setStatus(_A)
_SfpsResolveStatsStaleCount_Type=Integer32
_SfpsResolveStatsStaleCount_Object=MibScalar
sfpsResolveStatsStaleCount=_SfpsResolveStatsStaleCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,12),_SfpsResolveStatsStaleCount_Type())
sfpsResolveStatsStaleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsStaleCount.setStatus(_A)
_SfpsResolveStatsDupMsgCount_Type=Integer32
_SfpsResolveStatsDupMsgCount_Object=MibScalar
sfpsResolveStatsDupMsgCount=_SfpsResolveStatsDupMsgCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,13),_SfpsResolveStatsDupMsgCount_Type())
sfpsResolveStatsDupMsgCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsDupMsgCount.setStatus(_A)
_SfpsResolveStatsReqRcvd_Type=Integer32
_SfpsResolveStatsReqRcvd_Object=MibScalar
sfpsResolveStatsReqRcvd=_SfpsResolveStatsReqRcvd_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,14),_SfpsResolveStatsReqRcvd_Type())
sfpsResolveStatsReqRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsReqRcvd.setStatus(_A)
_SfpsResolveStatsRespAcksSent_Type=Integer32
_SfpsResolveStatsRespAcksSent_Object=MibScalar
sfpsResolveStatsRespAcksSent=_SfpsResolveStatsRespAcksSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,15),_SfpsResolveStatsRespAcksSent_Type())
sfpsResolveStatsRespAcksSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsRespAcksSent.setStatus(_A)
_SfpsResolveStatsRespNaksSent_Type=Integer32
_SfpsResolveStatsRespNaksSent_Object=MibScalar
sfpsResolveStatsRespNaksSent=_SfpsResolveStatsRespNaksSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,16),_SfpsResolveStatsRespNaksSent_Type())
sfpsResolveStatsRespNaksSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsRespNaksSent.setStatus(_A)
_SfpsResolveStatsRespUnknownsSent_Type=Integer32
_SfpsResolveStatsRespUnknownsSent_Object=MibScalar
sfpsResolveStatsRespUnknownsSent=_SfpsResolveStatsRespUnknownsSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,17),_SfpsResolveStatsRespUnknownsSent_Type())
sfpsResolveStatsRespUnknownsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsRespUnknownsSent.setStatus(_A)
_SfpsResolveStatsRespRecvd_Type=Integer32
_SfpsResolveStatsRespRecvd_Object=MibScalar
sfpsResolveStatsRespRecvd=_SfpsResolveStatsRespRecvd_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,18),_SfpsResolveStatsRespRecvd_Type())
sfpsResolveStatsRespRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsRespRecvd.setStatus(_A)
_SfpsResolveStatsResolveMask_Type=OctetString
_SfpsResolveStatsResolveMask_Object=MibScalar
sfpsResolveStatsResolveMask=_SfpsResolveStatsResolveMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,19),_SfpsResolveStatsResolveMask_Type())
sfpsResolveStatsResolveMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsResolveMask.setStatus(_A)
_SfpsResolveStatsINBMask_Type=OctetString
_SfpsResolveStatsINBMask_Object=MibScalar
sfpsResolveStatsINBMask=_SfpsResolveStatsINBMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,20),_SfpsResolveStatsINBMask_Type())
sfpsResolveStatsINBMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsINBMask.setStatus(_A)
_SfpsResolveStatsFloodMask_Type=OctetString
_SfpsResolveStatsFloodMask_Object=MibScalar
sfpsResolveStatsFloodMask=_SfpsResolveStatsFloodMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,21),_SfpsResolveStatsFloodMask_Type())
sfpsResolveStatsFloodMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsFloodMask.setStatus(_A)
_SfpsResolveStatsChangeCount_Type=Integer32
_SfpsResolveStatsChangeCount_Object=MibScalar
sfpsResolveStatsChangeCount=_SfpsResolveStatsChangeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,22),_SfpsResolveStatsChangeCount_Type())
sfpsResolveStatsChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsChangeCount.setStatus(_A)
_SfpsResolveStatsChangeTime_Type=TimeTicks
_SfpsResolveStatsChangeTime_Object=MibScalar
sfpsResolveStatsChangeTime=_SfpsResolveStatsChangeTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,23),_SfpsResolveStatsChangeTime_Type())
sfpsResolveStatsChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsChangeTime.setStatus(_A)
_SfpsResolveStatsResetStats_Type=Integer32
_SfpsResolveStatsResetStats_Object=MibScalar
sfpsResolveStatsResetStats=_SfpsResolveStatsResetStats_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,24),_SfpsResolveStatsResetStats_Type())
sfpsResolveStatsResetStats.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsResetStats.setStatus(_A)
_SfpsResolveStatsAnswerUnknown_Type=Integer32
_SfpsResolveStatsAnswerUnknown_Object=MibScalar
sfpsResolveStatsAnswerUnknown=_SfpsResolveStatsAnswerUnknown_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,25),_SfpsResolveStatsAnswerUnknown_Type())
sfpsResolveStatsAnswerUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsAnswerUnknown.setStatus(_A)
_SfpsResolveStatsDisableProxy_Type=Integer32
_SfpsResolveStatsDisableProxy_Object=MibScalar
sfpsResolveStatsDisableProxy=_SfpsResolveStatsDisableProxy_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,26),_SfpsResolveStatsDisableProxy_Type())
sfpsResolveStatsDisableProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsDisableProxy.setStatus(_A)
_SfpsResolveStatsDisableLayer3_Type=Integer32
_SfpsResolveStatsDisableLayer3_Object=MibScalar
sfpsResolveStatsDisableLayer3=_SfpsResolveStatsDisableLayer3_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,27),_SfpsResolveStatsDisableLayer3_Type())
sfpsResolveStatsDisableLayer3.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsDisableLayer3.setStatus(_A)
_SfpsResolveStatsCSPDaveMalPkts_Type=Integer32
_SfpsResolveStatsCSPDaveMalPkts_Object=MibScalar
sfpsResolveStatsCSPDaveMalPkts=_SfpsResolveStatsCSPDaveMalPkts_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,28),_SfpsResolveStatsCSPDaveMalPkts_Type())
sfpsResolveStatsCSPDaveMalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsCSPDaveMalPkts.setStatus(_A)
_SfpsResolveStatsStaleTimeOut_Type=Integer32
_SfpsResolveStatsStaleTimeOut_Object=MibScalar
sfpsResolveStatsStaleTimeOut=_SfpsResolveStatsStaleTimeOut_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,29),_SfpsResolveStatsStaleTimeOut_Type())
sfpsResolveStatsStaleTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsStaleTimeOut.setStatus(_A)
_SfpsResolveStatsMaxResponseTime_Type=Integer32
_SfpsResolveStatsMaxResponseTime_Object=MibScalar
sfpsResolveStatsMaxResponseTime=_SfpsResolveStatsMaxResponseTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,30),_SfpsResolveStatsMaxResponseTime_Type())
sfpsResolveStatsMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsResolveStatsMaxResponseTime.setStatus(_A)
_SfpsResolveStatsStaleEntryLost_Type=Integer32
_SfpsResolveStatsStaleEntryLost_Object=MibScalar
sfpsResolveStatsStaleEntryLost=_SfpsResolveStatsStaleEntryLost_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,31),_SfpsResolveStatsStaleEntryLost_Type())
sfpsResolveStatsStaleEntryLost.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsStaleEntryLost.setStatus(_A)
_SfpsResolveStatsDaveEntryLost_Type=Integer32
_SfpsResolveStatsDaveEntryLost_Object=MibScalar
sfpsResolveStatsDaveEntryLost=_SfpsResolveStatsDaveEntryLost_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,3,32),_SfpsResolveStatsDaveEntryLost_Type())
sfpsResolveStatsDaveEntryLost.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsResolveStatsDaveEntryLost.setStatus(_A)
_SfpsBlockResolveTable_Object=MibTable
sfpsBlockResolveTable=_SfpsBlockResolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1))
if mibBuilder.loadTexts:sfpsBlockResolveTable.setStatus(_A)
_SfpsBlockResolveTableEntry_Object=MibTableRow
sfpsBlockResolveTableEntry=_SfpsBlockResolveTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1))
sfpsBlockResolveTableEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:sfpsBlockResolveTableEntry.setStatus(_A)
_SfpsBlockResolveTableHash_Type=Integer32
_SfpsBlockResolveTableHash_Object=MibTableColumn
sfpsBlockResolveTableHash=_SfpsBlockResolveTableHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,1),_SfpsBlockResolveTableHash_Type())
sfpsBlockResolveTableHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableHash.setStatus(_A)
_SfpsBlockResolveTableHashIndex_Type=Integer32
_SfpsBlockResolveTableHashIndex_Object=MibTableColumn
sfpsBlockResolveTableHashIndex=_SfpsBlockResolveTableHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,2),_SfpsBlockResolveTableHashIndex_Type())
sfpsBlockResolveTableHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableHashIndex.setStatus(_A)
class _SfpsBlockResolveTableAOType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7),(_U,8),(_V,9),(_W,10),(_X,11),(_Y,12),(_Z,13),(_a,14),(_b,15),(_c,16)))
_SfpsBlockResolveTableAOType_Type.__name__=_D
_SfpsBlockResolveTableAOType_Object=MibTableColumn
sfpsBlockResolveTableAOType=_SfpsBlockResolveTableAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,3),_SfpsBlockResolveTableAOType_Type())
sfpsBlockResolveTableAOType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableAOType.setStatus(_A)
_SfpsBlockResolveTableAOValue_Type=DisplayString
_SfpsBlockResolveTableAOValue_Object=MibTableColumn
sfpsBlockResolveTableAOValue=_SfpsBlockResolveTableAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,4),_SfpsBlockResolveTableAOValue_Type())
sfpsBlockResolveTableAOValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableAOValue.setStatus(_A)
_SfpsBlockResolveTableStartTime_Type=TimeTicks
_SfpsBlockResolveTableStartTime_Object=MibTableColumn
sfpsBlockResolveTableStartTime=_SfpsBlockResolveTableStartTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,5),_SfpsBlockResolveTableStartTime_Type())
sfpsBlockResolveTableStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableStartTime.setStatus(_A)
_SfpsBlockResolveTableNumBlocked_Type=Counter32
_SfpsBlockResolveTableNumBlocked_Object=MibTableColumn
sfpsBlockResolveTableNumBlocked=_SfpsBlockResolveTableNumBlocked_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,6),_SfpsBlockResolveTableNumBlocked_Type())
sfpsBlockResolveTableNumBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableNumBlocked.setStatus(_A)
_SfpsBlockResolveTableNumSent_Type=Counter32
_SfpsBlockResolveTableNumSent_Object=MibTableColumn
sfpsBlockResolveTableNumSent=_SfpsBlockResolveTableNumSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,7),_SfpsBlockResolveTableNumSent_Type())
sfpsBlockResolveTableNumSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableNumSent.setStatus(_A)
_SfpsBlockResolveTableLastSeen_Type=TimeTicks
_SfpsBlockResolveTableLastSeen_Object=MibTableColumn
sfpsBlockResolveTableLastSeen=_SfpsBlockResolveTableLastSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,8),_SfpsBlockResolveTableLastSeen_Type())
sfpsBlockResolveTableLastSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableLastSeen.setStatus(_A)
_SfpsBlockResolveTableAvgPeriod_Type=Integer32
_SfpsBlockResolveTableAvgPeriod_Object=MibTableColumn
sfpsBlockResolveTableAvgPeriod=_SfpsBlockResolveTableAvgPeriod_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,1,1,9),_SfpsBlockResolveTableAvgPeriod_Type())
sfpsBlockResolveTableAvgPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveTableAvgPeriod.setStatus(_A)
class _SfpsBlockResolveAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('add-entry',2),('del-entry',3),(_d,4),('reset',5)))
_SfpsBlockResolveAPIVerb_Type.__name__=_D
_SfpsBlockResolveAPIVerb_Object=MibScalar
sfpsBlockResolveAPIVerb=_SfpsBlockResolveAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,1),_SfpsBlockResolveAPIVerb_Type())
sfpsBlockResolveAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPIVerb.setStatus(_A)
_SfpsBlockResolveAPIAOType_Type=DisplayString
_SfpsBlockResolveAPIAOType_Object=MibScalar
sfpsBlockResolveAPIAOType=_SfpsBlockResolveAPIAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,2),_SfpsBlockResolveAPIAOType_Type())
sfpsBlockResolveAPIAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPIAOType.setStatus(_A)
_SfpsBlockResolveAPIAOValue_Type=DisplayString
_SfpsBlockResolveAPIAOValue_Object=MibScalar
sfpsBlockResolveAPIAOValue=_SfpsBlockResolveAPIAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,3),_SfpsBlockResolveAPIAOValue_Type())
sfpsBlockResolveAPIAOValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPIAOValue.setStatus(_A)
_SfpsBlockResolveAPITestCount_Type=Integer32
_SfpsBlockResolveAPITestCount_Object=MibScalar
sfpsBlockResolveAPITestCount=_SfpsBlockResolveAPITestCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,4),_SfpsBlockResolveAPITestCount_Type())
sfpsBlockResolveAPITestCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPITestCount.setStatus(_A)
_SfpsBlockResolveAPIThreshold_Type=Integer32
_SfpsBlockResolveAPIThreshold_Object=MibScalar
sfpsBlockResolveAPIThreshold=_SfpsBlockResolveAPIThreshold_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,5),_SfpsBlockResolveAPIThreshold_Type())
sfpsBlockResolveAPIThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPIThreshold.setStatus(_A)
_SfpsBlockResolveAPISendPeriod_Type=Integer32
_SfpsBlockResolveAPISendPeriod_Object=MibScalar
sfpsBlockResolveAPISendPeriod=_SfpsBlockResolveAPISendPeriod_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,2,6),_SfpsBlockResolveAPISendPeriod_Type())
sfpsBlockResolveAPISendPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsBlockResolveAPISendPeriod.setStatus(_A)
_SfpsBlockResolveStatsNumEntries_Type=Integer32
_SfpsBlockResolveStatsNumEntries_Object=MibScalar
sfpsBlockResolveStatsNumEntries=_SfpsBlockResolveStatsNumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,1),_SfpsBlockResolveStatsNumEntries_Type())
sfpsBlockResolveStatsNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsNumEntries.setStatus(_A)
_SfpsBlockResolveStatsTableSize_Type=Integer32
_SfpsBlockResolveStatsTableSize_Object=MibScalar
sfpsBlockResolveStatsTableSize=_SfpsBlockResolveStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,2),_SfpsBlockResolveStatsTableSize_Type())
sfpsBlockResolveStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsTableSize.setStatus(_A)
_SfpsBlockResolveStatsTotalReqSeen_Type=Integer32
_SfpsBlockResolveStatsTotalReqSeen_Object=MibScalar
sfpsBlockResolveStatsTotalReqSeen=_SfpsBlockResolveStatsTotalReqSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,3),_SfpsBlockResolveStatsTotalReqSeen_Type())
sfpsBlockResolveStatsTotalReqSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsTotalReqSeen.setStatus(_A)
_SfpsBlockResolveStatsTotalBlocked_Type=Integer32
_SfpsBlockResolveStatsTotalBlocked_Object=MibScalar
sfpsBlockResolveStatsTotalBlocked=_SfpsBlockResolveStatsTotalBlocked_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,4),_SfpsBlockResolveStatsTotalBlocked_Type())
sfpsBlockResolveStatsTotalBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsTotalBlocked.setStatus(_A)
_SfpsBlockResolveStatsTotalSent_Type=Integer32
_SfpsBlockResolveStatsTotalSent_Object=MibScalar
sfpsBlockResolveStatsTotalSent=_SfpsBlockResolveStatsTotalSent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,5),_SfpsBlockResolveStatsTotalSent_Type())
sfpsBlockResolveStatsTotalSent.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsTotalSent.setStatus(_A)
_SfpsBlockResolveStatsAvgReqTime_Type=Integer32
_SfpsBlockResolveStatsAvgReqTime_Object=MibScalar
sfpsBlockResolveStatsAvgReqTime=_SfpsBlockResolveStatsAvgReqTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,4,3,6),_SfpsBlockResolveStatsAvgReqTime_Type())
sfpsBlockResolveStatsAvgReqTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsBlockResolveStatsAvgReqTime.setStatus(_A)
_SfpsUnresolveTable_Object=MibTable
sfpsUnresolveTable=_SfpsUnresolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1))
if mibBuilder.loadTexts:sfpsUnresolveTable.setStatus(_A)
_SfpsUnresolveTableEntry_Object=MibTableRow
sfpsUnresolveTableEntry=_SfpsUnresolveTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1))
sfpsUnresolveTableEntry.setIndexNames((0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:sfpsUnresolveTableEntry.setStatus(_A)
_SfpsUnresolveTableHash_Type=Integer32
_SfpsUnresolveTableHash_Object=MibTableColumn
sfpsUnresolveTableHash=_SfpsUnresolveTableHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,1),_SfpsUnresolveTableHash_Type())
sfpsUnresolveTableHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableHash.setStatus(_A)
_SfpsUnresolveTableHashIndex_Type=Integer32
_SfpsUnresolveTableHashIndex_Object=MibTableColumn
sfpsUnresolveTableHashIndex=_SfpsUnresolveTableHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,2),_SfpsUnresolveTableHashIndex_Type())
sfpsUnresolveTableHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableHashIndex.setStatus(_A)
class _SfpsUnresolveTableAOType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),(_Q,4),(_R,5),(_S,6),(_T,7),(_U,8),(_V,9),(_W,10),(_X,11),(_Y,12),(_Z,13),(_a,14),(_b,15),('aoNBT',16),(_c,17),('aoIpxSap8022',18),('aoIpxSapSnap',19),('aoIpxSapEnet',20),('aoDHCPXID',21),('aoipxRip8022',22),('aoipxRipSnap',23),('aoipxRipEnet',24)))
_SfpsUnresolveTableAOType_Type.__name__=_D
_SfpsUnresolveTableAOType_Object=MibTableColumn
sfpsUnresolveTableAOType=_SfpsUnresolveTableAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,3),_SfpsUnresolveTableAOType_Type())
sfpsUnresolveTableAOType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableAOType.setStatus(_A)
_SfpsUnresolveTableAOValue_Type=DisplayString
_SfpsUnresolveTableAOValue_Object=MibTableColumn
sfpsUnresolveTableAOValue=_SfpsUnresolveTableAOValue_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,4),_SfpsUnresolveTableAOValue_Type())
sfpsUnresolveTableAOValue.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableAOValue.setStatus(_A)
_SfpsUnresolveTableNumMisses_Type=Integer32
_SfpsUnresolveTableNumMisses_Object=MibTableColumn
sfpsUnresolveTableNumMisses=_SfpsUnresolveTableNumMisses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,5),_SfpsUnresolveTableNumMisses_Type())
sfpsUnresolveTableNumMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableNumMisses.setStatus(_A)
_SfpsUnresolveTableLastMissTime_Type=TimeTicks
_SfpsUnresolveTableLastMissTime_Object=MibTableColumn
sfpsUnresolveTableLastMissTime=_SfpsUnresolveTableLastMissTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,6),_SfpsUnresolveTableLastMissTime_Type())
sfpsUnresolveTableLastMissTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableLastMissTime.setStatus(_A)
_SfpsUnresolveTableLastCallProc_Type=Integer32
_SfpsUnresolveTableLastCallProc_Object=MibTableColumn
sfpsUnresolveTableLastCallProc=_SfpsUnresolveTableLastCallProc_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,7),_SfpsUnresolveTableLastCallProc_Type())
sfpsUnresolveTableLastCallProc.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableLastCallProc.setStatus(_A)
_SfpsUnresolveTableSrcMAC_Type=SfpsAddress
_SfpsUnresolveTableSrcMAC_Object=MibTableColumn
sfpsUnresolveTableSrcMAC=_SfpsUnresolveTableSrcMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,8),_SfpsUnresolveTableSrcMAC_Type())
sfpsUnresolveTableSrcMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableSrcMAC.setStatus(_A)
_SfpsUnresolveTableAvgPeriod_Type=Integer32
_SfpsUnresolveTableAvgPeriod_Object=MibTableColumn
sfpsUnresolveTableAvgPeriod=_SfpsUnresolveTableAvgPeriod_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,9),_SfpsUnresolveTableAvgPeriod_Type())
sfpsUnresolveTableAvgPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableAvgPeriod.setStatus(_A)
class _SfpsUnresolveTableBlockFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_SfpsUnresolveTableBlockFlag_Type.__name__=_D
_SfpsUnresolveTableBlockFlag_Object=MibTableColumn
sfpsUnresolveTableBlockFlag=_SfpsUnresolveTableBlockFlag_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,1,1,10),_SfpsUnresolveTableBlockFlag_Type())
sfpsUnresolveTableBlockFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableBlockFlag.setStatus(_A)
class _SfpsUnresolveTableAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_d,1),('reset',2),(_F,3)))
_SfpsUnresolveTableAPIVerb_Type.__name__=_D
_SfpsUnresolveTableAPIVerb_Object=MibScalar
sfpsUnresolveTableAPIVerb=_SfpsUnresolveTableAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,2,1),_SfpsUnresolveTableAPIVerb_Type())
sfpsUnresolveTableAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsUnresolveTableAPIVerb.setStatus(_A)
_SfpsUnresolveTableAPIAgeOutTime_Type=Integer32
_SfpsUnresolveTableAPIAgeOutTime_Object=MibScalar
sfpsUnresolveTableAPIAgeOutTime=_SfpsUnresolveTableAPIAgeOutTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,2,2),_SfpsUnresolveTableAPIAgeOutTime_Type())
sfpsUnresolveTableAPIAgeOutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsUnresolveTableAPIAgeOutTime.setStatus(_A)
class _SfpsUnresolveTableAPIBlockHoldDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('disabled',2),('enabled',3)))
_SfpsUnresolveTableAPIBlockHoldDown_Type.__name__=_D
_SfpsUnresolveTableAPIBlockHoldDown_Object=MibScalar
sfpsUnresolveTableAPIBlockHoldDown=_SfpsUnresolveTableAPIBlockHoldDown_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,2,3),_SfpsUnresolveTableAPIBlockHoldDown_Type())
sfpsUnresolveTableAPIBlockHoldDown.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsUnresolveTableAPIBlockHoldDown.setStatus(_A)
_SfpsUnresolveTableStatsNumEntries_Type=Integer32
_SfpsUnresolveTableStatsNumEntries_Object=MibScalar
sfpsUnresolveTableStatsNumEntries=_SfpsUnresolveTableStatsNumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,3,1),_SfpsUnresolveTableStatsNumEntries_Type())
sfpsUnresolveTableStatsNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableStatsNumEntries.setStatus(_A)
_SfpsUnresolveTableStatsTableSize_Type=Integer32
_SfpsUnresolveTableStatsTableSize_Object=MibScalar
sfpsUnresolveTableStatsTableSize=_SfpsUnresolveTableStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,3,2),_SfpsUnresolveTableStatsTableSize_Type())
sfpsUnresolveTableStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableStatsTableSize.setStatus(_A)
_SfpsUnresolveTableStatsTableFullCount_Type=Integer32
_SfpsUnresolveTableStatsTableFullCount_Object=MibScalar
sfpsUnresolveTableStatsTableFullCount=_SfpsUnresolveTableStatsTableFullCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,3,3),_SfpsUnresolveTableStatsTableFullCount_Type())
sfpsUnresolveTableStatsTableFullCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableStatsTableFullCount.setStatus(_A)
_SfpsUnresolveTableStatsTotalReqSeen_Type=Integer32
_SfpsUnresolveTableStatsTotalReqSeen_Object=MibScalar
sfpsUnresolveTableStatsTotalReqSeen=_SfpsUnresolveTableStatsTotalReqSeen_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,3,4),_SfpsUnresolveTableStatsTotalReqSeen_Type())
sfpsUnresolveTableStatsTotalReqSeen.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableStatsTotalReqSeen.setStatus(_A)
_SfpsUnresolveTableStatsAvgReqTime_Type=Integer32
_SfpsUnresolveTableStatsAvgReqTime_Object=MibScalar
sfpsUnresolveTableStatsAvgReqTime=_SfpsUnresolveTableStatsAvgReqTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,5,3,5),_SfpsUnresolveTableStatsAvgReqTime_Type())
sfpsUnresolveTableStatsAvgReqTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsUnresolveTableStatsAvgReqTime.setStatus(_A)
_SfpsTableResolveTable_Object=MibTable
sfpsTableResolveTable=_SfpsTableResolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1))
if mibBuilder.loadTexts:sfpsTableResolveTable.setStatus(_A)
_SfpsTableResolveTableEntry_Object=MibTableRow
sfpsTableResolveTableEntry=_SfpsTableResolveTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1))
sfpsTableResolveTableEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_i))
if mibBuilder.loadTexts:sfpsTableResolveTableEntry.setStatus(_A)
_SfpsTableResolveTag_Type=Integer32
_SfpsTableResolveTag_Object=MibTableColumn
sfpsTableResolveTag=_SfpsTableResolveTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,1),_SfpsTableResolveTag_Type())
sfpsTableResolveTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveTag.setStatus(_A)
_SfpsTableResolveHash_Type=Integer32
_SfpsTableResolveHash_Object=MibTableColumn
sfpsTableResolveHash=_SfpsTableResolveHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,2),_SfpsTableResolveHash_Type())
sfpsTableResolveHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveHash.setStatus(_A)
_SfpsTableResolveHashIndex_Type=Integer32
_SfpsTableResolveHashIndex_Object=MibTableColumn
sfpsTableResolveHashIndex=_SfpsTableResolveHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,3),_SfpsTableResolveHashIndex_Type())
sfpsTableResolveHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveHashIndex.setStatus(_A)
_SfpsTableResolveSrcType_Type=DisplayString
_SfpsTableResolveSrcType_Object=MibTableColumn
sfpsTableResolveSrcType=_SfpsTableResolveSrcType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,4),_SfpsTableResolveSrcType_Type())
sfpsTableResolveSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveSrcType.setStatus(_A)
_SfpsTableResolveSrcLoad_Type=DisplayString
_SfpsTableResolveSrcLoad_Object=MibTableColumn
sfpsTableResolveSrcLoad=_SfpsTableResolveSrcLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,5),_SfpsTableResolveSrcLoad_Type())
sfpsTableResolveSrcLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveSrcLoad.setStatus(_A)
_SfpsTableResolveTrgType_Type=DisplayString
_SfpsTableResolveTrgType_Object=MibTableColumn
sfpsTableResolveTrgType=_SfpsTableResolveTrgType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,6),_SfpsTableResolveTrgType_Type())
sfpsTableResolveTrgType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveTrgType.setStatus(_A)
_SfpsTableResolveTrgLoad_Type=DisplayString
_SfpsTableResolveTrgLoad_Object=MibTableColumn
sfpsTableResolveTrgLoad=_SfpsTableResolveTrgLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,1,1,7),_SfpsTableResolveTrgLoad_Type())
sfpsTableResolveTrgLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsTableResolveTrgLoad.setStatus(_A)
class _SfpsTableResolveAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('add',2),(_j,3),('modify',4),(_k,5)))
_SfpsTableResolveAPIVerb_Type.__name__=_D
_SfpsTableResolveAPIVerb_Object=MibScalar
sfpsTableResolveAPIVerb=_SfpsTableResolveAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,1),_SfpsTableResolveAPIVerb_Type())
sfpsTableResolveAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIVerb.setStatus(_A)
_SfpsTableResolveAPISrcAOType_Type=DisplayString
_SfpsTableResolveAPISrcAOType_Object=MibScalar
sfpsTableResolveAPISrcAOType=_SfpsTableResolveAPISrcAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,2),_SfpsTableResolveAPISrcAOType_Type())
sfpsTableResolveAPISrcAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPISrcAOType.setStatus(_A)
_SfpsTableResolveAPISrcAOLoad_Type=DisplayString
_SfpsTableResolveAPISrcAOLoad_Object=MibScalar
sfpsTableResolveAPISrcAOLoad=_SfpsTableResolveAPISrcAOLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,3),_SfpsTableResolveAPISrcAOLoad_Type())
sfpsTableResolveAPISrcAOLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPISrcAOLoad.setStatus(_A)
_SfpsTableResolveAPITrgAOType_Type=DisplayString
_SfpsTableResolveAPITrgAOType_Object=MibScalar
sfpsTableResolveAPITrgAOType=_SfpsTableResolveAPITrgAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,4),_SfpsTableResolveAPITrgAOType_Type())
sfpsTableResolveAPITrgAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPITrgAOType.setStatus(_A)
_SfpsTableResolveAPITrgAOLoad_Type=DisplayString
_SfpsTableResolveAPITrgAOLoad_Object=MibScalar
sfpsTableResolveAPITrgAOLoad=_SfpsTableResolveAPITrgAOLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,5),_SfpsTableResolveAPITrgAOLoad_Type())
sfpsTableResolveAPITrgAOLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPITrgAOLoad.setStatus(_A)
_SfpsTableResolveAPIVlanAOLoad_Type=DisplayString
_SfpsTableResolveAPIVlanAOLoad_Object=MibScalar
sfpsTableResolveAPIVlanAOLoad=_SfpsTableResolveAPIVlanAOLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,6),_SfpsTableResolveAPIVlanAOLoad_Type())
sfpsTableResolveAPIVlanAOLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIVlanAOLoad.setStatus(_A)
_SfpsTableResolveAPIDestSwMac_Type=DisplayString
_SfpsTableResolveAPIDestSwMac_Object=MibScalar
sfpsTableResolveAPIDestSwMac=_SfpsTableResolveAPIDestSwMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,7),_SfpsTableResolveAPIDestSwMac_Type())
sfpsTableResolveAPIDestSwMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIDestSwMac.setStatus(_A)
class _SfpsTableResolveAPIScopeToVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsTableResolveAPIScopeToVlan_Type.__name__=_D
_SfpsTableResolveAPIScopeToVlan_Object=MibScalar
sfpsTableResolveAPIScopeToVlan=_SfpsTableResolveAPIScopeToVlan_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,8),_SfpsTableResolveAPIScopeToVlan_Type())
sfpsTableResolveAPIScopeToVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIScopeToVlan.setStatus(_A)
class _SfpsTableResolveAPINVRAMEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsTableResolveAPINVRAMEntry_Type.__name__=_D
_SfpsTableResolveAPINVRAMEntry_Object=MibScalar
sfpsTableResolveAPINVRAMEntry=_SfpsTableResolveAPINVRAMEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,9),_SfpsTableResolveAPINVRAMEntry_Type())
sfpsTableResolveAPINVRAMEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPINVRAMEntry.setStatus(_A)
_SfpsTableResolveAPIMask_Type=HexInteger
_SfpsTableResolveAPIMask_Object=MibScalar
sfpsTableResolveAPIMask=_SfpsTableResolveAPIMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,10),_SfpsTableResolveAPIMask_Type())
sfpsTableResolveAPIMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIMask.setStatus(_A)
class _SfpsTableResolveAPIResolveOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ack',1),('nak',2)))
_SfpsTableResolveAPIResolveOption_Type.__name__=_D
_SfpsTableResolveAPIResolveOption_Object=MibScalar
sfpsTableResolveAPIResolveOption=_SfpsTableResolveAPIResolveOption_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,11),_SfpsTableResolveAPIResolveOption_Type())
sfpsTableResolveAPIResolveOption.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIResolveOption.setStatus(_A)
class _SfpsTableResolveAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsTableResolveAPIAdminStatus_Type.__name__=_D
_SfpsTableResolveAPIAdminStatus_Object=MibScalar
sfpsTableResolveAPIAdminStatus=_SfpsTableResolveAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,6,2,12),_SfpsTableResolveAPIAdminStatus_Type())
sfpsTableResolveAPIAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsTableResolveAPIAdminStatus.setStatus(_A)
_SfpsSubnetResolveStatsRequests_Type=Integer32
_SfpsSubnetResolveStatsRequests_Object=MibScalar
sfpsSubnetResolveStatsRequests=_SfpsSubnetResolveStatsRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,1),_SfpsSubnetResolveStatsRequests_Type())
sfpsSubnetResolveStatsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsRequests.setStatus(_A)
_SfpsSubnetResolveStatsAcks_Type=Integer32
_SfpsSubnetResolveStatsAcks_Object=MibScalar
sfpsSubnetResolveStatsAcks=_SfpsSubnetResolveStatsAcks_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,2),_SfpsSubnetResolveStatsAcks_Type())
sfpsSubnetResolveStatsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsAcks.setStatus(_A)
_SfpsSubnetResolveStatsUnknowns_Type=Integer32
_SfpsSubnetResolveStatsUnknowns_Object=MibScalar
sfpsSubnetResolveStatsUnknowns=_SfpsSubnetResolveStatsUnknowns_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,3),_SfpsSubnetResolveStatsUnknowns_Type())
sfpsSubnetResolveStatsUnknowns.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsUnknowns.setStatus(_A)
_SfpsSubnetResolveStatsInternalUnknowns_Type=Integer32
_SfpsSubnetResolveStatsInternalUnknowns_Object=MibScalar
sfpsSubnetResolveStatsInternalUnknowns=_SfpsSubnetResolveStatsInternalUnknowns_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,4),_SfpsSubnetResolveStatsInternalUnknowns_Type())
sfpsSubnetResolveStatsInternalUnknowns.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsInternalUnknowns.setStatus(_A)
_SfpsSubnetResolveStatsGatewayAcks_Type=Integer32
_SfpsSubnetResolveStatsGatewayAcks_Object=MibScalar
sfpsSubnetResolveStatsGatewayAcks=_SfpsSubnetResolveStatsGatewayAcks_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,5),_SfpsSubnetResolveStatsGatewayAcks_Type())
sfpsSubnetResolveStatsGatewayAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsGatewayAcks.setStatus(_A)
_SfpsSubnetResolveStatsErrors_Type=Integer32
_SfpsSubnetResolveStatsErrors_Object=MibScalar
sfpsSubnetResolveStatsErrors=_SfpsSubnetResolveStatsErrors_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,6),_SfpsSubnetResolveStatsErrors_Type())
sfpsSubnetResolveStatsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsErrors.setStatus(_A)
_SfpsSubnetResolveStatsMaxTblSize_Type=Integer32
_SfpsSubnetResolveStatsMaxTblSize_Object=MibScalar
sfpsSubnetResolveStatsMaxTblSize=_SfpsSubnetResolveStatsMaxTblSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,7),_SfpsSubnetResolveStatsMaxTblSize_Type())
sfpsSubnetResolveStatsMaxTblSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsMaxTblSize.setStatus(_A)
_SfpsSubnetResolveStatsTableSize_Type=Integer32
_SfpsSubnetResolveStatsTableSize_Object=MibScalar
sfpsSubnetResolveStatsTableSize=_SfpsSubnetResolveStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,1,8),_SfpsSubnetResolveStatsTableSize_Type())
sfpsSubnetResolveStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveStatsTableSize.setStatus(_A)
class _SfpsSubnetResolveAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('add',2),(_j,3),('updateMask',4),('setDefGateway',5),('clearDefGateway',6),(_k,7)))
_SfpsSubnetResolveAPIVerb_Type.__name__=_D
_SfpsSubnetResolveAPIVerb_Object=MibScalar
sfpsSubnetResolveAPIVerb=_SfpsSubnetResolveAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,1),_SfpsSubnetResolveAPIVerb_Type())
sfpsSubnetResolveAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPIVerb.setStatus(_A)
_SfpsSubnetResolveAPISrcAOType_Type=DisplayString
_SfpsSubnetResolveAPISrcAOType_Object=MibScalar
sfpsSubnetResolveAPISrcAOType=_SfpsSubnetResolveAPISrcAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,2),_SfpsSubnetResolveAPISrcAOType_Type())
sfpsSubnetResolveAPISrcAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPISrcAOType.setStatus(_A)
_SfpsSubnetResolveAPISrcAPLoad_Type=DisplayString
_SfpsSubnetResolveAPISrcAPLoad_Object=MibScalar
sfpsSubnetResolveAPISrcAPLoad=_SfpsSubnetResolveAPISrcAPLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,3),_SfpsSubnetResolveAPISrcAPLoad_Type())
sfpsSubnetResolveAPISrcAPLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPISrcAPLoad.setStatus(_A)
_SfpsSubnetResolveAPITrgAOType_Type=DisplayString
_SfpsSubnetResolveAPITrgAOType_Object=MibScalar
sfpsSubnetResolveAPITrgAOType=_SfpsSubnetResolveAPITrgAOType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,4),_SfpsSubnetResolveAPITrgAOType_Type())
sfpsSubnetResolveAPITrgAOType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPITrgAOType.setStatus(_A)
_SfpsSubnetResolveAPITrgAOLoad_Type=DisplayString
_SfpsSubnetResolveAPITrgAOLoad_Object=MibScalar
sfpsSubnetResolveAPITrgAOLoad=_SfpsSubnetResolveAPITrgAOLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,5),_SfpsSubnetResolveAPITrgAOLoad_Type())
sfpsSubnetResolveAPITrgAOLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPITrgAOLoad.setStatus(_A)
class _SfpsSubnetResolveAPIRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_SfpsSubnetResolveAPIRouteType_Type.__name__=_D
_SfpsSubnetResolveAPIRouteType_Object=MibScalar
sfpsSubnetResolveAPIRouteType=_SfpsSubnetResolveAPIRouteType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,6),_SfpsSubnetResolveAPIRouteType_Type())
sfpsSubnetResolveAPIRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPIRouteType.setStatus(_A)
class _SfpsSubnetResolveAPINVRAMEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsSubnetResolveAPINVRAMEntry_Type.__name__=_D
_SfpsSubnetResolveAPINVRAMEntry_Object=MibScalar
sfpsSubnetResolveAPINVRAMEntry=_SfpsSubnetResolveAPINVRAMEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,7),_SfpsSubnetResolveAPINVRAMEntry_Type())
sfpsSubnetResolveAPINVRAMEntry.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPINVRAMEntry.setStatus(_A)
class _SfpsSubnetResolveAPIAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsSubnetResolveAPIAdminStatus_Type.__name__=_D
_SfpsSubnetResolveAPIAdminStatus_Object=MibScalar
sfpsSubnetResolveAPIAdminStatus=_SfpsSubnetResolveAPIAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,8),_SfpsSubnetResolveAPIAdminStatus_Type())
sfpsSubnetResolveAPIAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPIAdminStatus.setStatus(_A)
_SfpsSubnetResolveAPIDefGateway_Type=DisplayString
_SfpsSubnetResolveAPIDefGateway_Object=MibScalar
sfpsSubnetResolveAPIDefGateway=_SfpsSubnetResolveAPIDefGateway_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,9),_SfpsSubnetResolveAPIDefGateway_Type())
sfpsSubnetResolveAPIDefGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPIDefGateway.setStatus(_A)
_SfpsSubnetResolveAPISubnetMask_Type=HexInteger
_SfpsSubnetResolveAPISubnetMask_Object=MibScalar
sfpsSubnetResolveAPISubnetMask=_SfpsSubnetResolveAPISubnetMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,2,10),_SfpsSubnetResolveAPISubnetMask_Type())
sfpsSubnetResolveAPISubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSubnetResolveAPISubnetMask.setStatus(_A)
_SfpsSubnetResolveTable_Object=MibTable
sfpsSubnetResolveTable=_SfpsSubnetResolveTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3))
if mibBuilder.loadTexts:sfpsSubnetResolveTable.setStatus(_A)
_SfpsSubnetResolveEntry_Object=MibTableRow
sfpsSubnetResolveEntry=_SfpsSubnetResolveEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1))
sfpsSubnetResolveEntry.setIndexNames((0,_E,_o),(0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:sfpsSubnetResolveEntry.setStatus(_A)
_SfpsSubnetResolveTargetTag_Type=Integer32
_SfpsSubnetResolveTargetTag_Object=MibTableColumn
sfpsSubnetResolveTargetTag=_SfpsSubnetResolveTargetTag_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,1),_SfpsSubnetResolveTargetTag_Type())
sfpsSubnetResolveTargetTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveTargetTag.setStatus(_A)
_SfpsSubnetResolveSourceHash_Type=Integer32
_SfpsSubnetResolveSourceHash_Object=MibTableColumn
sfpsSubnetResolveSourceHash=_SfpsSubnetResolveSourceHash_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,2),_SfpsSubnetResolveSourceHash_Type())
sfpsSubnetResolveSourceHash.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveSourceHash.setStatus(_A)
_SfpsSubnetResolveHashIndex_Type=Integer32
_SfpsSubnetResolveHashIndex_Object=MibTableColumn
sfpsSubnetResolveHashIndex=_SfpsSubnetResolveHashIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,3),_SfpsSubnetResolveHashIndex_Type())
sfpsSubnetResolveHashIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveHashIndex.setStatus(_A)
_SfpsSubnetResolveSrcType_Type=DisplayString
_SfpsSubnetResolveSrcType_Object=MibTableColumn
sfpsSubnetResolveSrcType=_SfpsSubnetResolveSrcType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,4),_SfpsSubnetResolveSrcType_Type())
sfpsSubnetResolveSrcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveSrcType.setStatus(_A)
_SfpsSubnetResolveSrcLoad_Type=DisplayString
_SfpsSubnetResolveSrcLoad_Object=MibTableColumn
sfpsSubnetResolveSrcLoad=_SfpsSubnetResolveSrcLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,5),_SfpsSubnetResolveSrcLoad_Type())
sfpsSubnetResolveSrcLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveSrcLoad.setStatus(_A)
_SfpsSubnetResolveTrgType_Type=DisplayString
_SfpsSubnetResolveTrgType_Object=MibTableColumn
sfpsSubnetResolveTrgType=_SfpsSubnetResolveTrgType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,6),_SfpsSubnetResolveTrgType_Type())
sfpsSubnetResolveTrgType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveTrgType.setStatus(_A)
_SfpsSubnetResolveTrgLoad_Type=DisplayString
_SfpsSubnetResolveTrgLoad_Object=MibTableColumn
sfpsSubnetResolveTrgLoad=_SfpsSubnetResolveTrgLoad_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,7),_SfpsSubnetResolveTrgLoad_Type())
sfpsSubnetResolveTrgLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveTrgLoad.setStatus(_A)
class _SfpsSubnetResolveRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_m,2),(_n,3)))
_SfpsSubnetResolveRouteType_Type.__name__=_D
_SfpsSubnetResolveRouteType_Object=MibTableColumn
sfpsSubnetResolveRouteType=_SfpsSubnetResolveRouteType_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,8),_SfpsSubnetResolveRouteType_Type())
sfpsSubnetResolveRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveRouteType.setStatus(_A)
_SfpsSubnetResolveRelativeCnt_Type=Integer32
_SfpsSubnetResolveRelativeCnt_Object=MibTableColumn
sfpsSubnetResolveRelativeCnt=_SfpsSubnetResolveRelativeCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,9),_SfpsSubnetResolveRelativeCnt_Type())
sfpsSubnetResolveRelativeCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveRelativeCnt.setStatus(_A)
_SfpsSubnetResolveAbsoluteCnt_Type=Integer32
_SfpsSubnetResolveAbsoluteCnt_Object=MibTableColumn
sfpsSubnetResolveAbsoluteCnt=_SfpsSubnetResolveAbsoluteCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,10),_SfpsSubnetResolveAbsoluteCnt_Type())
sfpsSubnetResolveAbsoluteCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveAbsoluteCnt.setStatus(_A)
class _SfpsSubnetResolveNVRAMEntry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsSubnetResolveNVRAMEntry_Type.__name__=_D
_SfpsSubnetResolveNVRAMEntry_Object=MibTableColumn
sfpsSubnetResolveNVRAMEntry=_SfpsSubnetResolveNVRAMEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,11),_SfpsSubnetResolveNVRAMEntry_Type())
sfpsSubnetResolveNVRAMEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveNVRAMEntry.setStatus(_A)
class _SfpsSubnetResolveAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3)))
_SfpsSubnetResolveAdminStatus_Type.__name__=_D
_SfpsSubnetResolveAdminStatus_Object=MibTableColumn
sfpsSubnetResolveAdminStatus=_SfpsSubnetResolveAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,12),_SfpsSubnetResolveAdminStatus_Type())
sfpsSubnetResolveAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveAdminStatus.setStatus(_A)
class _SfpsSubnetResolveOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('halted',2)))
_SfpsSubnetResolveOperStatus_Type.__name__=_D
_SfpsSubnetResolveOperStatus_Object=MibTableColumn
sfpsSubnetResolveOperStatus=_SfpsSubnetResolveOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,3,1,13),_SfpsSubnetResolveOperStatus_Type())
sfpsSubnetResolveOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveOperStatus.setStatus(_A)
_SfpsSubnetResolveNvramMaskEntries_Type=Integer32
_SfpsSubnetResolveNvramMaskEntries_Object=MibScalar
sfpsSubnetResolveNvramMaskEntries=_SfpsSubnetResolveNvramMaskEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,4,2),_SfpsSubnetResolveNvramMaskEntries_Type())
sfpsSubnetResolveNvramMaskEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveNvramMaskEntries.setStatus(_A)
_SfpsSubnetResolveNvramIpEntries_Type=Integer32
_SfpsSubnetResolveNvramIpEntries_Object=MibScalar
sfpsSubnetResolveNvramIpEntries=_SfpsSubnetResolveNvramIpEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,7,4,4),_SfpsSubnetResolveNvramIpEntries_Type())
sfpsSubnetResolveNvramIpEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSubnetResolveNvramIpEntries.setStatus(_A)
_SfpsRelayAgentResolveVlanName_Type=OctetString
_SfpsRelayAgentResolveVlanName_Object=MibScalar
sfpsRelayAgentResolveVlanName=_SfpsRelayAgentResolveVlanName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,10,4,2),_SfpsRelayAgentResolveVlanName_Type())
sfpsRelayAgentResolveVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRelayAgentResolveVlanName.setStatus(_A)
_SfpsRelayAgentResolveStatsTableSize_Type=Integer32
_SfpsRelayAgentResolveStatsTableSize_Object=MibScalar
sfpsRelayAgentResolveStatsTableSize=_SfpsRelayAgentResolveStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,10,5,2),_SfpsRelayAgentResolveStatsTableSize_Type())
sfpsRelayAgentResolveStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRelayAgentResolveStatsTableSize.setStatus(_A)
_SfpsRelayAgentResolveStatsHighWater_Type=Integer32
_SfpsRelayAgentResolveStatsHighWater_Object=MibScalar
sfpsRelayAgentResolveStatsHighWater=_SfpsRelayAgentResolveStatsHighWater_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,1,10,5,3),_SfpsRelayAgentResolveStatsHighWater_Type())
sfpsRelayAgentResolveStatsHighWater.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsRelayAgentResolveStatsHighWater.setStatus(_A)
_SfpsMobilityStatsOrigSendCount_Type=Integer32
_SfpsMobilityStatsOrigSendCount_Object=MibScalar
sfpsMobilityStatsOrigSendCount=_SfpsMobilityStatsOrigSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,1),_SfpsMobilityStatsOrigSendCount_Type())
sfpsMobilityStatsOrigSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigSendCount.setStatus(_A)
_SfpsMobilityStatsOrigReceiveCount_Type=Integer32
_SfpsMobilityStatsOrigReceiveCount_Object=MibScalar
sfpsMobilityStatsOrigReceiveCount=_SfpsMobilityStatsOrigReceiveCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,2),_SfpsMobilityStatsOrigReceiveCount_Type())
sfpsMobilityStatsOrigReceiveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigReceiveCount.setStatus(_A)
_SfpsMobilityStatsOrigNUSendCount_Type=Integer32
_SfpsMobilityStatsOrigNUSendCount_Object=MibScalar
sfpsMobilityStatsOrigNUSendCount=_SfpsMobilityStatsOrigNUSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,3),_SfpsMobilityStatsOrigNUSendCount_Type())
sfpsMobilityStatsOrigNUSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigNUSendCount.setStatus(_A)
_SfpsMobilityStatsOrigNASendCount_Type=Integer32
_SfpsMobilityStatsOrigNASendCount_Object=MibScalar
sfpsMobilityStatsOrigNASendCount=_SfpsMobilityStatsOrigNASendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,4),_SfpsMobilityStatsOrigNASendCount_Type())
sfpsMobilityStatsOrigNASendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigNASendCount.setStatus(_A)
_SfpsMobilityStatsOrigNUASendReqCount_Type=Integer32
_SfpsMobilityStatsOrigNUASendReqCount_Object=MibScalar
sfpsMobilityStatsOrigNUASendReqCount=_SfpsMobilityStatsOrigNUASendReqCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,5),_SfpsMobilityStatsOrigNUASendReqCount_Type())
sfpsMobilityStatsOrigNUASendReqCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigNUASendReqCount.setStatus(_A)
_SfpsMobilityStatsOrigRetrySendCount_Type=Integer32
_SfpsMobilityStatsOrigRetrySendCount_Object=MibScalar
sfpsMobilityStatsOrigRetrySendCount=_SfpsMobilityStatsOrigRetrySendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,6),_SfpsMobilityStatsOrigRetrySendCount_Type())
sfpsMobilityStatsOrigRetrySendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigRetrySendCount.setStatus(_A)
_SfpsMobilityStatsOrigLocalMoveCount_Type=Integer32
_SfpsMobilityStatsOrigLocalMoveCount_Object=MibScalar
sfpsMobilityStatsOrigLocalMoveCount=_SfpsMobilityStatsOrigLocalMoveCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,7),_SfpsMobilityStatsOrigLocalMoveCount_Type())
sfpsMobilityStatsOrigLocalMoveCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigLocalMoveCount.setStatus(_A)
_SfpsMobilityStatsOrigUnknownCount_Type=Integer32
_SfpsMobilityStatsOrigUnknownCount_Object=MibScalar
sfpsMobilityStatsOrigUnknownCount=_SfpsMobilityStatsOrigUnknownCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,8),_SfpsMobilityStatsOrigUnknownCount_Type())
sfpsMobilityStatsOrigUnknownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigUnknownCount.setStatus(_A)
_SfpsMobilityStatsOrigAckCount_Type=Integer32
_SfpsMobilityStatsOrigAckCount_Object=MibScalar
sfpsMobilityStatsOrigAckCount=_SfpsMobilityStatsOrigAckCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,9),_SfpsMobilityStatsOrigAckCount_Type())
sfpsMobilityStatsOrigAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigAckCount.setStatus(_A)
_SfpsMobilityStatsOrigNakNodeCount_Type=Integer32
_SfpsMobilityStatsOrigNakNodeCount_Object=MibScalar
sfpsMobilityStatsOrigNakNodeCount=_SfpsMobilityStatsOrigNakNodeCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,10),_SfpsMobilityStatsOrigNakNodeCount_Type())
sfpsMobilityStatsOrigNakNodeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigNakNodeCount.setStatus(_A)
_SfpsMobilityStatsOrigNakAliasCount_Type=Integer32
_SfpsMobilityStatsOrigNakAliasCount_Object=MibScalar
sfpsMobilityStatsOrigNakAliasCount=_SfpsMobilityStatsOrigNakAliasCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,11),_SfpsMobilityStatsOrigNakAliasCount_Type())
sfpsMobilityStatsOrigNakAliasCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsOrigNakAliasCount.setStatus(_A)
_SfpsMobilityStatsErrorCount_Type=Integer32
_SfpsMobilityStatsErrorCount_Object=MibScalar
sfpsMobilityStatsErrorCount=_SfpsMobilityStatsErrorCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,12),_SfpsMobilityStatsErrorCount_Type())
sfpsMobilityStatsErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsErrorCount.setStatus(_A)
_SfpsMobilityStatsGenRecCount_Type=Integer32
_SfpsMobilityStatsGenRecCount_Object=MibScalar
sfpsMobilityStatsGenRecCount=_SfpsMobilityStatsGenRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,13),_SfpsMobilityStatsGenRecCount_Type())
sfpsMobilityStatsGenRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenRecCount.setStatus(_A)
_SfpsMobilityStatsGenSendCount_Type=Integer32
_SfpsMobilityStatsGenSendCount_Object=MibScalar
sfpsMobilityStatsGenSendCount=_SfpsMobilityStatsGenSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,14),_SfpsMobilityStatsGenSendCount_Type())
sfpsMobilityStatsGenSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenSendCount.setStatus(_A)
_SfpsMobilityStatsGenReqRecCount_Type=Integer32
_SfpsMobilityStatsGenReqRecCount_Object=MibScalar
sfpsMobilityStatsGenReqRecCount=_SfpsMobilityStatsGenReqRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,15),_SfpsMobilityStatsGenReqRecCount_Type())
sfpsMobilityStatsGenReqRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenReqRecCount.setStatus(_A)
_SfpsMobilityStatsGenReqRetryCount_Type=Integer32
_SfpsMobilityStatsGenReqRetryCount_Object=MibScalar
sfpsMobilityStatsGenReqRetryCount=_SfpsMobilityStatsGenReqRetryCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,16),_SfpsMobilityStatsGenReqRetryCount_Type())
sfpsMobilityStatsGenReqRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenReqRetryCount.setStatus(_A)
_SfpsMobilityStatsGenReqForwardCount_Type=Integer32
_SfpsMobilityStatsGenReqForwardCount_Object=MibScalar
sfpsMobilityStatsGenReqForwardCount=_SfpsMobilityStatsGenReqForwardCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,17),_SfpsMobilityStatsGenReqForwardCount_Type())
sfpsMobilityStatsGenReqForwardCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenReqForwardCount.setStatus(_A)
_SfpsMobilityStatsGenRespRecCount_Type=Integer32
_SfpsMobilityStatsGenRespRecCount_Object=MibScalar
sfpsMobilityStatsGenRespRecCount=_SfpsMobilityStatsGenRespRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,18),_SfpsMobilityStatsGenRespRecCount_Type())
sfpsMobilityStatsGenRespRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenRespRecCount.setStatus(_A)
_SfpsMobilityStatsGenRespSendCount_Type=Integer32
_SfpsMobilityStatsGenRespSendCount_Object=MibScalar
sfpsMobilityStatsGenRespSendCount=_SfpsMobilityStatsGenRespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,19),_SfpsMobilityStatsGenRespSendCount_Type())
sfpsMobilityStatsGenRespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsGenRespSendCount.setStatus(_A)
_SfpsMobilityStatsNUReqRecCount_Type=Integer32
_SfpsMobilityStatsNUReqRecCount_Object=MibScalar
sfpsMobilityStatsNUReqRecCount=_SfpsMobilityStatsNUReqRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,20),_SfpsMobilityStatsNUReqRecCount_Type())
sfpsMobilityStatsNUReqRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNUReqRecCount.setStatus(_A)
_SfpsMobilityStatsNURespSendCount_Type=Integer32
_SfpsMobilityStatsNURespSendCount_Object=MibScalar
sfpsMobilityStatsNURespSendCount=_SfpsMobilityStatsNURespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,21),_SfpsMobilityStatsNURespSendCount_Type())
sfpsMobilityStatsNURespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespSendCount.setStatus(_A)
_SfpsMobilityStatsNAReqRecCount_Type=Integer32
_SfpsMobilityStatsNAReqRecCount_Object=MibScalar
sfpsMobilityStatsNAReqRecCount=_SfpsMobilityStatsNAReqRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,22),_SfpsMobilityStatsNAReqRecCount_Type())
sfpsMobilityStatsNAReqRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNAReqRecCount.setStatus(_A)
_SfpsMobilityStatsNARespSendCount_Type=Integer32
_SfpsMobilityStatsNARespSendCount_Object=MibScalar
sfpsMobilityStatsNARespSendCount=_SfpsMobilityStatsNARespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,23),_SfpsMobilityStatsNARespSendCount_Type())
sfpsMobilityStatsNARespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNARespSendCount.setStatus(_A)
_SfpsMobilityStatsNUARespRecUnknownCount_Type=Integer32
_SfpsMobilityStatsNUARespRecUnknownCount_Object=MibScalar
sfpsMobilityStatsNUARespRecUnknownCount=_SfpsMobilityStatsNUARespRecUnknownCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,24),_SfpsMobilityStatsNUARespRecUnknownCount_Type())
sfpsMobilityStatsNUARespRecUnknownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNUARespRecUnknownCount.setStatus(_A)
_SfpsMobilityStatsNURespRecAckCount_Type=Integer32
_SfpsMobilityStatsNURespRecAckCount_Object=MibScalar
sfpsMobilityStatsNURespRecAckCount=_SfpsMobilityStatsNURespRecAckCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,25),_SfpsMobilityStatsNURespRecAckCount_Type())
sfpsMobilityStatsNURespRecAckCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespRecAckCount.setStatus(_A)
_SfpsMobilityStatsNUARespRecAliasNakCount_Type=Integer32
_SfpsMobilityStatsNUARespRecAliasNakCount_Object=MibScalar
sfpsMobilityStatsNUARespRecAliasNakCount=_SfpsMobilityStatsNUARespRecAliasNakCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,26),_SfpsMobilityStatsNUARespRecAliasNakCount_Type())
sfpsMobilityStatsNUARespRecAliasNakCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNUARespRecAliasNakCount.setStatus(_A)
_SfpsMobilityStatsNUARespRecNodeNakCount_Type=Integer32
_SfpsMobilityStatsNUARespRecNodeNakCount_Object=MibScalar
sfpsMobilityStatsNUARespRecNodeNakCount=_SfpsMobilityStatsNUARespRecNodeNakCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,27),_SfpsMobilityStatsNUARespRecNodeNakCount_Type())
sfpsMobilityStatsNUARespRecNodeNakCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNUARespRecNodeNakCount.setStatus(_A)
_SfpsMobilityStatsNURespAliasNakSendCount_Type=Integer32
_SfpsMobilityStatsNURespAliasNakSendCount_Object=MibScalar
sfpsMobilityStatsNURespAliasNakSendCount=_SfpsMobilityStatsNURespAliasNakSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,28),_SfpsMobilityStatsNURespAliasNakSendCount_Type())
sfpsMobilityStatsNURespAliasNakSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespAliasNakSendCount.setStatus(_A)
_SfpsMobilityStatsNURespNodeNakSendCount_Type=Integer32
_SfpsMobilityStatsNURespNodeNakSendCount_Object=MibScalar
sfpsMobilityStatsNURespNodeNakSendCount=_SfpsMobilityStatsNURespNodeNakSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,29),_SfpsMobilityStatsNURespNodeNakSendCount_Type())
sfpsMobilityStatsNURespNodeNakSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespNodeNakSendCount.setStatus(_A)
_SfpsMobilityStatsNURespAckSendCount_Type=Integer32
_SfpsMobilityStatsNURespAckSendCount_Object=MibScalar
sfpsMobilityStatsNURespAckSendCount=_SfpsMobilityStatsNURespAckSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,30),_SfpsMobilityStatsNURespAckSendCount_Type())
sfpsMobilityStatsNURespAckSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespAckSendCount.setStatus(_A)
_SfpsMobilityStatsNURespUnknownSendCount_Type=Integer32
_SfpsMobilityStatsNURespUnknownSendCount_Object=MibScalar
sfpsMobilityStatsNURespUnknownSendCount=_SfpsMobilityStatsNURespUnknownSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,31),_SfpsMobilityStatsNURespUnknownSendCount_Type())
sfpsMobilityStatsNURespUnknownSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsNURespUnknownSendCount.setStatus(_A)
_SfpsMobilityStatsInterNUARespRecCount_Type=Integer32
_SfpsMobilityStatsInterNUARespRecCount_Object=MibScalar
sfpsMobilityStatsInterNUARespRecCount=_SfpsMobilityStatsInterNUARespRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,32),_SfpsMobilityStatsInterNUARespRecCount_Type())
sfpsMobilityStatsInterNUARespRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNUARespRecCount.setStatus(_A)
_SfpsMobilityStatsInterNUARespSendCount_Type=Integer32
_SfpsMobilityStatsInterNUARespSendCount_Object=MibScalar
sfpsMobilityStatsInterNUARespSendCount=_SfpsMobilityStatsInterNUARespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,33),_SfpsMobilityStatsInterNUARespSendCount_Type())
sfpsMobilityStatsInterNUARespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNUARespSendCount.setStatus(_A)
_SfpsMobilityStatsInterNewUserRespRecCount_Type=Integer32
_SfpsMobilityStatsInterNewUserRespRecCount_Object=MibScalar
sfpsMobilityStatsInterNewUserRespRecCount=_SfpsMobilityStatsInterNewUserRespRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,34),_SfpsMobilityStatsInterNewUserRespRecCount_Type())
sfpsMobilityStatsInterNewUserRespRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNewUserRespRecCount.setStatus(_A)
_SfpsMobilityStatsInterNewAliasRespRecCount_Type=Integer32
_SfpsMobilityStatsInterNewAliasRespRecCount_Object=MibScalar
sfpsMobilityStatsInterNewAliasRespRecCount=_SfpsMobilityStatsInterNewAliasRespRecCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,35),_SfpsMobilityStatsInterNewAliasRespRecCount_Type())
sfpsMobilityStatsInterNewAliasRespRecCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNewAliasRespRecCount.setStatus(_A)
_SfpsMobilityStatsInterNewUserRespSendCount_Type=Integer32
_SfpsMobilityStatsInterNewUserRespSendCount_Object=MibScalar
sfpsMobilityStatsInterNewUserRespSendCount=_SfpsMobilityStatsInterNewUserRespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,36),_SfpsMobilityStatsInterNewUserRespSendCount_Type())
sfpsMobilityStatsInterNewUserRespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNewUserRespSendCount.setStatus(_A)
_SfpsMobilityStatsInterNewAliasRespSendCount_Type=Integer32
_SfpsMobilityStatsInterNewAliasRespSendCount_Object=MibScalar
sfpsMobilityStatsInterNewAliasRespSendCount=_SfpsMobilityStatsInterNewAliasRespSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,37),_SfpsMobilityStatsInterNewAliasRespSendCount_Type())
sfpsMobilityStatsInterNewAliasRespSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterNewAliasRespSendCount.setStatus(_A)
_SfpsMobilityStatsInterRespNakNodeSendCount_Type=Integer32
_SfpsMobilityStatsInterRespNakNodeSendCount_Object=MibScalar
sfpsMobilityStatsInterRespNakNodeSendCount=_SfpsMobilityStatsInterRespNakNodeSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,38),_SfpsMobilityStatsInterRespNakNodeSendCount_Type())
sfpsMobilityStatsInterRespNakNodeSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterRespNakNodeSendCount.setStatus(_A)
_SfpsMobilityStatsInterRespNakAliasSendCount_Type=Integer32
_SfpsMobilityStatsInterRespNakAliasSendCount_Object=MibScalar
sfpsMobilityStatsInterRespNakAliasSendCount=_SfpsMobilityStatsInterRespNakAliasSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,39),_SfpsMobilityStatsInterRespNakAliasSendCount_Type())
sfpsMobilityStatsInterRespNakAliasSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterRespNakAliasSendCount.setStatus(_A)
_SfpsMobilityStatsInterRespUnknownSendCount_Type=Integer32
_SfpsMobilityStatsInterRespUnknownSendCount_Object=MibScalar
sfpsMobilityStatsInterRespUnknownSendCount=_SfpsMobilityStatsInterRespUnknownSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,40),_SfpsMobilityStatsInterRespUnknownSendCount_Type())
sfpsMobilityStatsInterRespUnknownSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterRespUnknownSendCount.setStatus(_A)
_SfpsMobilityStatsInterRespAckSendCount_Type=Integer32
_SfpsMobilityStatsInterRespAckSendCount_Object=MibScalar
sfpsMobilityStatsInterRespAckSendCount=_SfpsMobilityStatsInterRespAckSendCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,41),_SfpsMobilityStatsInterRespAckSendCount_Type())
sfpsMobilityStatsInterRespAckSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsInterRespAckSendCount.setStatus(_A)
_SfpsMobilityStatsAliasOnOfSwitch_Type=Integer32
_SfpsMobilityStatsAliasOnOfSwitch_Object=MibScalar
sfpsMobilityStatsAliasOnOfSwitch=_SfpsMobilityStatsAliasOnOfSwitch_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,42),_SfpsMobilityStatsAliasOnOfSwitch_Type())
sfpsMobilityStatsAliasOnOfSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsMobilityStatsAliasOnOfSwitch.setStatus(_A)
_SfpsMobilityStatsResetCounters_Type=Integer32
_SfpsMobilityStatsResetCounters_Object=MibScalar
sfpsMobilityStatsResetCounters=_SfpsMobilityStatsResetCounters_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,43),_SfpsMobilityStatsResetCounters_Type())
sfpsMobilityStatsResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsResetCounters.setStatus(_A)
_SfpsMobilityStatsRetryCount_Type=Integer32
_SfpsMobilityStatsRetryCount_Object=MibScalar
sfpsMobilityStatsRetryCount=_SfpsMobilityStatsRetryCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,44),_SfpsMobilityStatsRetryCount_Type())
sfpsMobilityStatsRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsRetryCount.setStatus(_A)
_SfpsMobilityStatsRetryDrops_Type=Integer32
_SfpsMobilityStatsRetryDrops_Object=MibScalar
sfpsMobilityStatsRetryDrops=_SfpsMobilityStatsRetryDrops_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,45),_SfpsMobilityStatsRetryDrops_Type())
sfpsMobilityStatsRetryDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsRetryDrops.setStatus(_A)
_SfpsMobilityStatsMaxRetryReached_Type=Integer32
_SfpsMobilityStatsMaxRetryReached_Object=MibScalar
sfpsMobilityStatsMaxRetryReached=_SfpsMobilityStatsMaxRetryReached_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,46),_SfpsMobilityStatsMaxRetryReached_Type())
sfpsMobilityStatsMaxRetryReached.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsMaxRetryReached.setStatus(_A)
_SfpsMobilityStatsNewUserRetryTime_Type=Integer32
_SfpsMobilityStatsNewUserRetryTime_Object=MibScalar
sfpsMobilityStatsNewUserRetryTime=_SfpsMobilityStatsNewUserRetryTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,47),_SfpsMobilityStatsNewUserRetryTime_Type())
sfpsMobilityStatsNewUserRetryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsNewUserRetryTime.setStatus(_A)
_SfpsMobilityStatsMaxNewUserRetries_Type=Integer32
_SfpsMobilityStatsMaxNewUserRetries_Object=MibScalar
sfpsMobilityStatsMaxNewUserRetries=_SfpsMobilityStatsMaxNewUserRetries_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,48),_SfpsMobilityStatsMaxNewUserRetries_Type())
sfpsMobilityStatsMaxNewUserRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsMaxNewUserRetries.setStatus(_A)
_SfpsMobilityStatsNewUserStaleTimeout_Type=Integer32
_SfpsMobilityStatsNewUserStaleTimeout_Object=MibScalar
sfpsMobilityStatsNewUserStaleTimeout=_SfpsMobilityStatsNewUserStaleTimeout_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,49),_SfpsMobilityStatsNewUserStaleTimeout_Type())
sfpsMobilityStatsNewUserStaleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsNewUserStaleTimeout.setStatus(_A)
_SfpsMobilityStatsAvgResponseTime_Type=Integer32
_SfpsMobilityStatsAvgResponseTime_Object=MibScalar
sfpsMobilityStatsAvgResponseTime=_SfpsMobilityStatsAvgResponseTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,50),_SfpsMobilityStatsAvgResponseTime_Type())
sfpsMobilityStatsAvgResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsAvgResponseTime.setStatus(_A)
_SfpsMobilityStatsMaxResponeTime_Type=Integer32
_SfpsMobilityStatsMaxResponeTime_Object=MibScalar
sfpsMobilityStatsMaxResponeTime=_SfpsMobilityStatsMaxResponeTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,9,2,3,51),_SfpsMobilityStatsMaxResponeTime_Type())
sfpsMobilityStatsMaxResponeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsMobilityStatsMaxResponeTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HexInteger':HexInteger,'SfpsAddress':SfpsAddress,'sfpsServiceCenterResolveTable':sfpsServiceCenterResolveTable,'sfpsServiceCenterResolveEntry':sfpsServiceCenterResolveEntry,_I:sfpsServiceCenterResolveHashLeaf,'sfpsServiceCenterResolveMetric':sfpsServiceCenterResolveMetric,'sfpsServiceCenterResolveName':sfpsServiceCenterResolveName,'sfpsServiceCenterResolveOperStatus':sfpsServiceCenterResolveOperStatus,'sfpsServiceCenterResolveAdminStatus':sfpsServiceCenterResolveAdminStatus,'sfpsServiceCenterResolveStatusTime':sfpsServiceCenterResolveStatusTime,'sfpsServiceCenterResolveRequests':sfpsServiceCenterResolveRequests,'sfpsServiceCenterResolveResponses':sfpsServiceCenterResolveResponses,'sfpsSwitchResolveTable':sfpsSwitchResolveTable,'sfpsSwitchResolveEntry':sfpsSwitchResolveEntry,_J:sfpsSwitchResolveSwitch,_K:sfpsSwitchResolveCallTag,'sfpsSwitchResolvePortNum':sfpsSwitchResolvePortNum,'sfpsSwitchResolveNeighborSw':sfpsSwitchResolveNeighborSw,'sfpsSwitchResolveRequestCount':sfpsSwitchResolveRequestCount,'sfpsSwitchResolveResponseCount':sfpsSwitchResolveResponseCount,'sfpsSwitchResolveMobilityRetry':sfpsSwitchResolveMobilityRetry,'sfpsSwitchResolveEventId':sfpsSwitchResolveEventId,'sfpsResolveStatsRequests':sfpsResolveStatsRequests,'sfpsResolveStatsResponses':sfpsResolveStatsResponses,'sfpsResolveStatsAcks':sfpsResolveStatsAcks,'sfpsResolveStatsNaks':sfpsResolveStatsNaks,'sfpsResolveStatsUnknowns':sfpsResolveStatsUnknowns,'sfpsResolveStatsNoAnswer':sfpsResolveStatsNoAnswer,'sfpsResolveStatsTimeout':sfpsResolveStatsTimeout,'sfpsResolveStatsAvgResponseTime':sfpsResolveStatsAvgResponseTime,'sfpsResolveStatsTableSize':sfpsResolveStatsTableSize,'sfpsResolveStatsTableHigh':sfpsResolveStatsTableHigh,'sfpsResolveStatsErrorCount':sfpsResolveStatsErrorCount,'sfpsResolveStatsStaleCount':sfpsResolveStatsStaleCount,'sfpsResolveStatsDupMsgCount':sfpsResolveStatsDupMsgCount,'sfpsResolveStatsReqRcvd':sfpsResolveStatsReqRcvd,'sfpsResolveStatsRespAcksSent':sfpsResolveStatsRespAcksSent,'sfpsResolveStatsRespNaksSent':sfpsResolveStatsRespNaksSent,'sfpsResolveStatsRespUnknownsSent':sfpsResolveStatsRespUnknownsSent,'sfpsResolveStatsRespRecvd':sfpsResolveStatsRespRecvd,'sfpsResolveStatsResolveMask':sfpsResolveStatsResolveMask,'sfpsResolveStatsINBMask':sfpsResolveStatsINBMask,'sfpsResolveStatsFloodMask':sfpsResolveStatsFloodMask,'sfpsResolveStatsChangeCount':sfpsResolveStatsChangeCount,'sfpsResolveStatsChangeTime':sfpsResolveStatsChangeTime,'sfpsResolveStatsResetStats':sfpsResolveStatsResetStats,'sfpsResolveStatsAnswerUnknown':sfpsResolveStatsAnswerUnknown,'sfpsResolveStatsDisableProxy':sfpsResolveStatsDisableProxy,'sfpsResolveStatsDisableLayer3':sfpsResolveStatsDisableLayer3,'sfpsResolveStatsCSPDaveMalPkts':sfpsResolveStatsCSPDaveMalPkts,'sfpsResolveStatsStaleTimeOut':sfpsResolveStatsStaleTimeOut,'sfpsResolveStatsMaxResponseTime':sfpsResolveStatsMaxResponseTime,'sfpsResolveStatsStaleEntryLost':sfpsResolveStatsStaleEntryLost,'sfpsResolveStatsDaveEntryLost':sfpsResolveStatsDaveEntryLost,'sfpsBlockResolveTable':sfpsBlockResolveTable,'sfpsBlockResolveTableEntry':sfpsBlockResolveTableEntry,_L:sfpsBlockResolveTableHash,_M:sfpsBlockResolveTableHashIndex,'sfpsBlockResolveTableAOType':sfpsBlockResolveTableAOType,'sfpsBlockResolveTableAOValue':sfpsBlockResolveTableAOValue,'sfpsBlockResolveTableStartTime':sfpsBlockResolveTableStartTime,'sfpsBlockResolveTableNumBlocked':sfpsBlockResolveTableNumBlocked,'sfpsBlockResolveTableNumSent':sfpsBlockResolveTableNumSent,'sfpsBlockResolveTableLastSeen':sfpsBlockResolveTableLastSeen,'sfpsBlockResolveTableAvgPeriod':sfpsBlockResolveTableAvgPeriod,'sfpsBlockResolveAPIVerb':sfpsBlockResolveAPIVerb,'sfpsBlockResolveAPIAOType':sfpsBlockResolveAPIAOType,'sfpsBlockResolveAPIAOValue':sfpsBlockResolveAPIAOValue,'sfpsBlockResolveAPITestCount':sfpsBlockResolveAPITestCount,'sfpsBlockResolveAPIThreshold':sfpsBlockResolveAPIThreshold,'sfpsBlockResolveAPISendPeriod':sfpsBlockResolveAPISendPeriod,'sfpsBlockResolveStatsNumEntries':sfpsBlockResolveStatsNumEntries,'sfpsBlockResolveStatsTableSize':sfpsBlockResolveStatsTableSize,'sfpsBlockResolveStatsTotalReqSeen':sfpsBlockResolveStatsTotalReqSeen,'sfpsBlockResolveStatsTotalBlocked':sfpsBlockResolveStatsTotalBlocked,'sfpsBlockResolveStatsTotalSent':sfpsBlockResolveStatsTotalSent,'sfpsBlockResolveStatsAvgReqTime':sfpsBlockResolveStatsAvgReqTime,'sfpsUnresolveTable':sfpsUnresolveTable,'sfpsUnresolveTableEntry':sfpsUnresolveTableEntry,_e:sfpsUnresolveTableHash,_f:sfpsUnresolveTableHashIndex,'sfpsUnresolveTableAOType':sfpsUnresolveTableAOType,'sfpsUnresolveTableAOValue':sfpsUnresolveTableAOValue,'sfpsUnresolveTableNumMisses':sfpsUnresolveTableNumMisses,'sfpsUnresolveTableLastMissTime':sfpsUnresolveTableLastMissTime,'sfpsUnresolveTableLastCallProc':sfpsUnresolveTableLastCallProc,'sfpsUnresolveTableSrcMAC':sfpsUnresolveTableSrcMAC,'sfpsUnresolveTableAvgPeriod':sfpsUnresolveTableAvgPeriod,'sfpsUnresolveTableBlockFlag':sfpsUnresolveTableBlockFlag,'sfpsUnresolveTableAPIVerb':sfpsUnresolveTableAPIVerb,'sfpsUnresolveTableAPIAgeOutTime':sfpsUnresolveTableAPIAgeOutTime,'sfpsUnresolveTableAPIBlockHoldDown':sfpsUnresolveTableAPIBlockHoldDown,'sfpsUnresolveTableStatsNumEntries':sfpsUnresolveTableStatsNumEntries,'sfpsUnresolveTableStatsTableSize':sfpsUnresolveTableStatsTableSize,'sfpsUnresolveTableStatsTableFullCount':sfpsUnresolveTableStatsTableFullCount,'sfpsUnresolveTableStatsTotalReqSeen':sfpsUnresolveTableStatsTotalReqSeen,'sfpsUnresolveTableStatsAvgReqTime':sfpsUnresolveTableStatsAvgReqTime,'sfpsTableResolveTable':sfpsTableResolveTable,'sfpsTableResolveTableEntry':sfpsTableResolveTableEntry,_g:sfpsTableResolveTag,_h:sfpsTableResolveHash,_i:sfpsTableResolveHashIndex,'sfpsTableResolveSrcType':sfpsTableResolveSrcType,'sfpsTableResolveSrcLoad':sfpsTableResolveSrcLoad,'sfpsTableResolveTrgType':sfpsTableResolveTrgType,'sfpsTableResolveTrgLoad':sfpsTableResolveTrgLoad,'sfpsTableResolveAPIVerb':sfpsTableResolveAPIVerb,'sfpsTableResolveAPISrcAOType':sfpsTableResolveAPISrcAOType,'sfpsTableResolveAPISrcAOLoad':sfpsTableResolveAPISrcAOLoad,'sfpsTableResolveAPITrgAOType':sfpsTableResolveAPITrgAOType,'sfpsTableResolveAPITrgAOLoad':sfpsTableResolveAPITrgAOLoad,'sfpsTableResolveAPIVlanAOLoad':sfpsTableResolveAPIVlanAOLoad,'sfpsTableResolveAPIDestSwMac':sfpsTableResolveAPIDestSwMac,'sfpsTableResolveAPIScopeToVlan':sfpsTableResolveAPIScopeToVlan,'sfpsTableResolveAPINVRAMEntry':sfpsTableResolveAPINVRAMEntry,'sfpsTableResolveAPIMask':sfpsTableResolveAPIMask,'sfpsTableResolveAPIResolveOption':sfpsTableResolveAPIResolveOption,'sfpsTableResolveAPIAdminStatus':sfpsTableResolveAPIAdminStatus,'sfpsSubnetResolveStatsRequests':sfpsSubnetResolveStatsRequests,'sfpsSubnetResolveStatsAcks':sfpsSubnetResolveStatsAcks,'sfpsSubnetResolveStatsUnknowns':sfpsSubnetResolveStatsUnknowns,'sfpsSubnetResolveStatsInternalUnknowns':sfpsSubnetResolveStatsInternalUnknowns,'sfpsSubnetResolveStatsGatewayAcks':sfpsSubnetResolveStatsGatewayAcks,'sfpsSubnetResolveStatsErrors':sfpsSubnetResolveStatsErrors,'sfpsSubnetResolveStatsMaxTblSize':sfpsSubnetResolveStatsMaxTblSize,'sfpsSubnetResolveStatsTableSize':sfpsSubnetResolveStatsTableSize,'sfpsSubnetResolveAPIVerb':sfpsSubnetResolveAPIVerb,'sfpsSubnetResolveAPISrcAOType':sfpsSubnetResolveAPISrcAOType,'sfpsSubnetResolveAPISrcAPLoad':sfpsSubnetResolveAPISrcAPLoad,'sfpsSubnetResolveAPITrgAOType':sfpsSubnetResolveAPITrgAOType,'sfpsSubnetResolveAPITrgAOLoad':sfpsSubnetResolveAPITrgAOLoad,'sfpsSubnetResolveAPIRouteType':sfpsSubnetResolveAPIRouteType,'sfpsSubnetResolveAPINVRAMEntry':sfpsSubnetResolveAPINVRAMEntry,'sfpsSubnetResolveAPIAdminStatus':sfpsSubnetResolveAPIAdminStatus,'sfpsSubnetResolveAPIDefGateway':sfpsSubnetResolveAPIDefGateway,'sfpsSubnetResolveAPISubnetMask':sfpsSubnetResolveAPISubnetMask,'sfpsSubnetResolveTable':sfpsSubnetResolveTable,'sfpsSubnetResolveEntry':sfpsSubnetResolveEntry,_o:sfpsSubnetResolveTargetTag,_p:sfpsSubnetResolveSourceHash,_q:sfpsSubnetResolveHashIndex,'sfpsSubnetResolveSrcType':sfpsSubnetResolveSrcType,'sfpsSubnetResolveSrcLoad':sfpsSubnetResolveSrcLoad,'sfpsSubnetResolveTrgType':sfpsSubnetResolveTrgType,'sfpsSubnetResolveTrgLoad':sfpsSubnetResolveTrgLoad,'sfpsSubnetResolveRouteType':sfpsSubnetResolveRouteType,'sfpsSubnetResolveRelativeCnt':sfpsSubnetResolveRelativeCnt,'sfpsSubnetResolveAbsoluteCnt':sfpsSubnetResolveAbsoluteCnt,'sfpsSubnetResolveNVRAMEntry':sfpsSubnetResolveNVRAMEntry,'sfpsSubnetResolveAdminStatus':sfpsSubnetResolveAdminStatus,'sfpsSubnetResolveOperStatus':sfpsSubnetResolveOperStatus,'sfpsSubnetResolveNvramMaskEntries':sfpsSubnetResolveNvramMaskEntries,'sfpsSubnetResolveNvramIpEntries':sfpsSubnetResolveNvramIpEntries,'sfpsRelayAgentResolveVlanName':sfpsRelayAgentResolveVlanName,'sfpsRelayAgentResolveStatsTableSize':sfpsRelayAgentResolveStatsTableSize,'sfpsRelayAgentResolveStatsHighWater':sfpsRelayAgentResolveStatsHighWater,'sfpsMobilityStatsOrigSendCount':sfpsMobilityStatsOrigSendCount,'sfpsMobilityStatsOrigReceiveCount':sfpsMobilityStatsOrigReceiveCount,'sfpsMobilityStatsOrigNUSendCount':sfpsMobilityStatsOrigNUSendCount,'sfpsMobilityStatsOrigNASendCount':sfpsMobilityStatsOrigNASendCount,'sfpsMobilityStatsOrigNUASendReqCount':sfpsMobilityStatsOrigNUASendReqCount,'sfpsMobilityStatsOrigRetrySendCount':sfpsMobilityStatsOrigRetrySendCount,'sfpsMobilityStatsOrigLocalMoveCount':sfpsMobilityStatsOrigLocalMoveCount,'sfpsMobilityStatsOrigUnknownCount':sfpsMobilityStatsOrigUnknownCount,'sfpsMobilityStatsOrigAckCount':sfpsMobilityStatsOrigAckCount,'sfpsMobilityStatsOrigNakNodeCount':sfpsMobilityStatsOrigNakNodeCount,'sfpsMobilityStatsOrigNakAliasCount':sfpsMobilityStatsOrigNakAliasCount,'sfpsMobilityStatsErrorCount':sfpsMobilityStatsErrorCount,'sfpsMobilityStatsGenRecCount':sfpsMobilityStatsGenRecCount,'sfpsMobilityStatsGenSendCount':sfpsMobilityStatsGenSendCount,'sfpsMobilityStatsGenReqRecCount':sfpsMobilityStatsGenReqRecCount,'sfpsMobilityStatsGenReqRetryCount':sfpsMobilityStatsGenReqRetryCount,'sfpsMobilityStatsGenReqForwardCount':sfpsMobilityStatsGenReqForwardCount,'sfpsMobilityStatsGenRespRecCount':sfpsMobilityStatsGenRespRecCount,'sfpsMobilityStatsGenRespSendCount':sfpsMobilityStatsGenRespSendCount,'sfpsMobilityStatsNUReqRecCount':sfpsMobilityStatsNUReqRecCount,'sfpsMobilityStatsNURespSendCount':sfpsMobilityStatsNURespSendCount,'sfpsMobilityStatsNAReqRecCount':sfpsMobilityStatsNAReqRecCount,'sfpsMobilityStatsNARespSendCount':sfpsMobilityStatsNARespSendCount,'sfpsMobilityStatsNUARespRecUnknownCount':sfpsMobilityStatsNUARespRecUnknownCount,'sfpsMobilityStatsNURespRecAckCount':sfpsMobilityStatsNURespRecAckCount,'sfpsMobilityStatsNUARespRecAliasNakCount':sfpsMobilityStatsNUARespRecAliasNakCount,'sfpsMobilityStatsNUARespRecNodeNakCount':sfpsMobilityStatsNUARespRecNodeNakCount,'sfpsMobilityStatsNURespAliasNakSendCount':sfpsMobilityStatsNURespAliasNakSendCount,'sfpsMobilityStatsNURespNodeNakSendCount':sfpsMobilityStatsNURespNodeNakSendCount,'sfpsMobilityStatsNURespAckSendCount':sfpsMobilityStatsNURespAckSendCount,'sfpsMobilityStatsNURespUnknownSendCount':sfpsMobilityStatsNURespUnknownSendCount,'sfpsMobilityStatsInterNUARespRecCount':sfpsMobilityStatsInterNUARespRecCount,'sfpsMobilityStatsInterNUARespSendCount':sfpsMobilityStatsInterNUARespSendCount,'sfpsMobilityStatsInterNewUserRespRecCount':sfpsMobilityStatsInterNewUserRespRecCount,'sfpsMobilityStatsInterNewAliasRespRecCount':sfpsMobilityStatsInterNewAliasRespRecCount,'sfpsMobilityStatsInterNewUserRespSendCount':sfpsMobilityStatsInterNewUserRespSendCount,'sfpsMobilityStatsInterNewAliasRespSendCount':sfpsMobilityStatsInterNewAliasRespSendCount,'sfpsMobilityStatsInterRespNakNodeSendCount':sfpsMobilityStatsInterRespNakNodeSendCount,'sfpsMobilityStatsInterRespNakAliasSendCount':sfpsMobilityStatsInterRespNakAliasSendCount,'sfpsMobilityStatsInterRespUnknownSendCount':sfpsMobilityStatsInterRespUnknownSendCount,'sfpsMobilityStatsInterRespAckSendCount':sfpsMobilityStatsInterRespAckSendCount,'sfpsMobilityStatsAliasOnOfSwitch':sfpsMobilityStatsAliasOnOfSwitch,'sfpsMobilityStatsResetCounters':sfpsMobilityStatsResetCounters,'sfpsMobilityStatsRetryCount':sfpsMobilityStatsRetryCount,'sfpsMobilityStatsRetryDrops':sfpsMobilityStatsRetryDrops,'sfpsMobilityStatsMaxRetryReached':sfpsMobilityStatsMaxRetryReached,'sfpsMobilityStatsNewUserRetryTime':sfpsMobilityStatsNewUserRetryTime,'sfpsMobilityStatsMaxNewUserRetries':sfpsMobilityStatsMaxNewUserRetries,'sfpsMobilityStatsNewUserStaleTimeout':sfpsMobilityStatsNewUserStaleTimeout,'sfpsMobilityStatsAvgResponseTime':sfpsMobilityStatsAvgResponseTime,'sfpsMobilityStatsMaxResponeTime':sfpsMobilityStatsMaxResponeTime})