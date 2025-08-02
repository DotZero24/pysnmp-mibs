_v='cdrIPv6DropStatsGroup'
_u='cdrIPv6StatsGroup'
_t='cdrDropStatsGroup'
_s='cdrStatsGroup'
_r='cdrIPv6DropStatsReqDroppedOnMCT'
_q='cdrIPv6DropStatsIpv6ExtnHeaderPresent'
_p='cdrIPv6DropStatsVpnOptionDisabled'
_o='cdrIPv6DropStatsIPv6AddrNotConfigured'
_n='cdrIPv6DropStatsInterfaceError'
_m='cdrIPv6DropStatsDirectReplyFromServer'
_l='cdrIPv6DropStatsOptionInsertionFailed'
_k='cdrIPv6DropStatsInvalidVRF'
_j='cdrIPv6DropStatsUnknownOpInterface'
_i='cdrIPv6DropStatsInvalidPkts'
_h='cdrIPv6DropStatsMaxHopsExceeded'
_g='cdrIPv6DropStatsRelayDisabled'
_f='cdrIPv6StatsPktsDropped'
_e='cdrIPv6StatsPktsForwarded'
_d='cdrIPv6StatsPktsReceived'
_c='cdrDropStatsReqDroppedOnMCT'
_b='cdrDropStatsUntrustablePort'
_a='cdrDropStatsMalformedPkts'
_Z='cdrDropStatsOpt82ValidationFailure'
_Y='cdrDropStatsMaxHopsExceeded'
_X='cdrDropStatsUnknownVrfOrInterface'
_W='cdrDropStatsUnknownOpInterface'
_V='cdrDropStatsTxFailureClient'
_U='cdrDropStatsTxFailureServer'
_T='cdrDropStatsInterfaceError'
_S='cdrDropStatsInvalidMsgType'
_R='cdrDropStatsRelayNotEnabled'
_Q='cdrStatsPktsDropped'
_P='cdrStatsPktsForwarded'
_O='cdrStatsPktsReceived'
_N='cdrIPv6DropStatsIfIndex'
_M='cdrIPv6StatsPktType'
_L='cdrIPv6StatsIfIndex'
_K='cdrDropStatsIfIndex'
_J='decline'
_I='release'
_H='request'
_G='cdrStatsPktType'
_F='cdrStatsIfIndex'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='CISCO-DHCP-RELAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDhcpRelayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,833))
if mibBuilder.loadTexts:ciscoDhcpRelayMIB.setRevisions(('2016-09-16 00:00','2016-06-09 00:00'))
_CiscoDhcpRelayMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayMIBNotifs=_CiscoDhcpRelayMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,833,0))
_CiscoDhcpRelayMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayMIBObjects=_CiscoDhcpRelayMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,833,1))
_CiscoDhcpRelayStats_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayStats=_CiscoDhcpRelayStats_ObjectIdentity((1,3,6,1,4,1,9,9,833,1,1))
_CdrStatsTable_Object=MibTable
cdrStatsTable=_CdrStatsTable_Object((1,3,6,1,4,1,9,9,833,1,1,1))
if mibBuilder.loadTexts:cdrStatsTable.setStatus(_A)
_CdrStatsEntry_Object=MibTableRow
cdrStatsEntry=_CdrStatsEntry_Object((1,3,6,1,4,1,9,9,833,1,1,1,1))
cdrStatsEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:cdrStatsEntry.setStatus(_A)
_CdrStatsIfIndex_Type=InterfaceIndexOrZero
_CdrStatsIfIndex_Object=MibTableColumn
cdrStatsIfIndex=_CdrStatsIfIndex_Object((1,3,6,1,4,1,9,9,833,1,1,1,1,1),_CdrStatsIfIndex_Type())
cdrStatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrStatsIfIndex.setStatus(_A)
class _CdrStatsPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('discover',1),('offer',2),(_H,3),('ack',4),(_I,5),(_J,6),('inform',7),('nack',8),('dhcpL3Fwd',9),('nonDhcp',10)))
_CdrStatsPktType_Type.__name__=_E
_CdrStatsPktType_Object=MibTableColumn
cdrStatsPktType=_CdrStatsPktType_Object((1,3,6,1,4,1,9,9,833,1,1,1,1,2),_CdrStatsPktType_Type())
cdrStatsPktType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrStatsPktType.setStatus(_A)
_CdrStatsPktsReceived_Type=Counter32
_CdrStatsPktsReceived_Object=MibTableColumn
cdrStatsPktsReceived=_CdrStatsPktsReceived_Object((1,3,6,1,4,1,9,9,833,1,1,1,1,3),_CdrStatsPktsReceived_Type())
cdrStatsPktsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrStatsPktsReceived.setStatus(_A)
_CdrStatsPktsForwarded_Type=Counter32
_CdrStatsPktsForwarded_Object=MibTableColumn
cdrStatsPktsForwarded=_CdrStatsPktsForwarded_Object((1,3,6,1,4,1,9,9,833,1,1,1,1,4),_CdrStatsPktsForwarded_Type())
cdrStatsPktsForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrStatsPktsForwarded.setStatus(_A)
_CdrStatsPktsDropped_Type=Counter32
_CdrStatsPktsDropped_Object=MibTableColumn
cdrStatsPktsDropped=_CdrStatsPktsDropped_Object((1,3,6,1,4,1,9,9,833,1,1,1,1,5),_CdrStatsPktsDropped_Type())
cdrStatsPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrStatsPktsDropped.setStatus(_A)
_CdrDropStatsTable_Object=MibTable
cdrDropStatsTable=_CdrDropStatsTable_Object((1,3,6,1,4,1,9,9,833,1,1,2))
if mibBuilder.loadTexts:cdrDropStatsTable.setStatus(_A)
_CdrDropStatsEntry_Object=MibTableRow
cdrDropStatsEntry=_CdrDropStatsEntry_Object((1,3,6,1,4,1,9,9,833,1,1,2,1))
cdrDropStatsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:cdrDropStatsEntry.setStatus(_A)
_CdrDropStatsIfIndex_Type=InterfaceIndexOrZero
_CdrDropStatsIfIndex_Object=MibTableColumn
cdrDropStatsIfIndex=_CdrDropStatsIfIndex_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,1),_CdrDropStatsIfIndex_Type())
cdrDropStatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrDropStatsIfIndex.setStatus(_A)
_CdrDropStatsRelayNotEnabled_Type=Counter32
_CdrDropStatsRelayNotEnabled_Object=MibTableColumn
cdrDropStatsRelayNotEnabled=_CdrDropStatsRelayNotEnabled_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,2),_CdrDropStatsRelayNotEnabled_Type())
cdrDropStatsRelayNotEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsRelayNotEnabled.setStatus(_A)
_CdrDropStatsInvalidMsgType_Type=Counter32
_CdrDropStatsInvalidMsgType_Object=MibTableColumn
cdrDropStatsInvalidMsgType=_CdrDropStatsInvalidMsgType_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,3),_CdrDropStatsInvalidMsgType_Type())
cdrDropStatsInvalidMsgType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsInvalidMsgType.setStatus(_A)
_CdrDropStatsInterfaceError_Type=Counter32
_CdrDropStatsInterfaceError_Object=MibTableColumn
cdrDropStatsInterfaceError=_CdrDropStatsInterfaceError_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,4),_CdrDropStatsInterfaceError_Type())
cdrDropStatsInterfaceError.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsInterfaceError.setStatus(_A)
_CdrDropStatsTxFailureServer_Type=Counter32
_CdrDropStatsTxFailureServer_Object=MibTableColumn
cdrDropStatsTxFailureServer=_CdrDropStatsTxFailureServer_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,5),_CdrDropStatsTxFailureServer_Type())
cdrDropStatsTxFailureServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsTxFailureServer.setStatus(_A)
_CdrDropStatsTxFailureClient_Type=Counter32
_CdrDropStatsTxFailureClient_Object=MibTableColumn
cdrDropStatsTxFailureClient=_CdrDropStatsTxFailureClient_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,6),_CdrDropStatsTxFailureClient_Type())
cdrDropStatsTxFailureClient.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsTxFailureClient.setStatus(_A)
_CdrDropStatsUnknownOpInterface_Type=Counter32
_CdrDropStatsUnknownOpInterface_Object=MibTableColumn
cdrDropStatsUnknownOpInterface=_CdrDropStatsUnknownOpInterface_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,7),_CdrDropStatsUnknownOpInterface_Type())
cdrDropStatsUnknownOpInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsUnknownOpInterface.setStatus(_A)
_CdrDropStatsUnknownVrfOrInterface_Type=Counter32
_CdrDropStatsUnknownVrfOrInterface_Object=MibTableColumn
cdrDropStatsUnknownVrfOrInterface=_CdrDropStatsUnknownVrfOrInterface_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,8),_CdrDropStatsUnknownVrfOrInterface_Type())
cdrDropStatsUnknownVrfOrInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsUnknownVrfOrInterface.setStatus(_A)
_CdrDropStatsMaxHopsExceeded_Type=Counter32
_CdrDropStatsMaxHopsExceeded_Object=MibTableColumn
cdrDropStatsMaxHopsExceeded=_CdrDropStatsMaxHopsExceeded_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,9),_CdrDropStatsMaxHopsExceeded_Type())
cdrDropStatsMaxHopsExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsMaxHopsExceeded.setStatus(_A)
_CdrDropStatsOpt82ValidationFailure_Type=Counter32
_CdrDropStatsOpt82ValidationFailure_Object=MibTableColumn
cdrDropStatsOpt82ValidationFailure=_CdrDropStatsOpt82ValidationFailure_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,10),_CdrDropStatsOpt82ValidationFailure_Type())
cdrDropStatsOpt82ValidationFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsOpt82ValidationFailure.setStatus(_A)
_CdrDropStatsMalformedPkts_Type=Counter32
_CdrDropStatsMalformedPkts_Object=MibTableColumn
cdrDropStatsMalformedPkts=_CdrDropStatsMalformedPkts_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,11),_CdrDropStatsMalformedPkts_Type())
cdrDropStatsMalformedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsMalformedPkts.setStatus(_A)
_CdrDropStatsUntrustablePort_Type=Counter32
_CdrDropStatsUntrustablePort_Object=MibTableColumn
cdrDropStatsUntrustablePort=_CdrDropStatsUntrustablePort_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,12),_CdrDropStatsUntrustablePort_Type())
cdrDropStatsUntrustablePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsUntrustablePort.setStatus(_A)
_CdrDropStatsReqDroppedOnMCT_Type=Counter32
_CdrDropStatsReqDroppedOnMCT_Object=MibTableColumn
cdrDropStatsReqDroppedOnMCT=_CdrDropStatsReqDroppedOnMCT_Object((1,3,6,1,4,1,9,9,833,1,1,2,1,13),_CdrDropStatsReqDroppedOnMCT_Type())
cdrDropStatsReqDroppedOnMCT.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrDropStatsReqDroppedOnMCT.setStatus(_A)
_CdrIPv6StatsTable_Object=MibTable
cdrIPv6StatsTable=_CdrIPv6StatsTable_Object((1,3,6,1,4,1,9,9,833,1,1,3))
if mibBuilder.loadTexts:cdrIPv6StatsTable.setStatus(_A)
_CdrIPv6StatsEntry_Object=MibTableRow
cdrIPv6StatsEntry=_CdrIPv6StatsEntry_Object((1,3,6,1,4,1,9,9,833,1,1,3,1))
cdrIPv6StatsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cdrIPv6StatsEntry.setStatus(_A)
_CdrIPv6StatsIfIndex_Type=InterfaceIndexOrZero
_CdrIPv6StatsIfIndex_Object=MibTableColumn
cdrIPv6StatsIfIndex=_CdrIPv6StatsIfIndex_Object((1,3,6,1,4,1,9,9,833,1,1,3,1,1),_CdrIPv6StatsIfIndex_Type())
cdrIPv6StatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrIPv6StatsIfIndex.setStatus(_A)
class _CdrIPv6StatsPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('solicit',1),('advertise',2),(_H,3),('confirm',4),('renew',5),('rebind',6),('reply',7),(_I,8),(_J,9),('reconfigure',10),('infoRequest',11),('relayForward',12),('relayReply',13),('unknown',14)))
_CdrIPv6StatsPktType_Type.__name__=_E
_CdrIPv6StatsPktType_Object=MibTableColumn
cdrIPv6StatsPktType=_CdrIPv6StatsPktType_Object((1,3,6,1,4,1,9,9,833,1,1,3,1,2),_CdrIPv6StatsPktType_Type())
cdrIPv6StatsPktType.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrIPv6StatsPktType.setStatus(_A)
_CdrIPv6StatsPktsReceived_Type=Counter32
_CdrIPv6StatsPktsReceived_Object=MibTableColumn
cdrIPv6StatsPktsReceived=_CdrIPv6StatsPktsReceived_Object((1,3,6,1,4,1,9,9,833,1,1,3,1,3),_CdrIPv6StatsPktsReceived_Type())
cdrIPv6StatsPktsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6StatsPktsReceived.setStatus(_A)
_CdrIPv6StatsPktsForwarded_Type=Counter32
_CdrIPv6StatsPktsForwarded_Object=MibTableColumn
cdrIPv6StatsPktsForwarded=_CdrIPv6StatsPktsForwarded_Object((1,3,6,1,4,1,9,9,833,1,1,3,1,4),_CdrIPv6StatsPktsForwarded_Type())
cdrIPv6StatsPktsForwarded.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6StatsPktsForwarded.setStatus(_A)
_CdrIPv6StatsPktsDropped_Type=Counter32
_CdrIPv6StatsPktsDropped_Object=MibTableColumn
cdrIPv6StatsPktsDropped=_CdrIPv6StatsPktsDropped_Object((1,3,6,1,4,1,9,9,833,1,1,3,1,5),_CdrIPv6StatsPktsDropped_Type())
cdrIPv6StatsPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6StatsPktsDropped.setStatus(_A)
_CdrIPv6DropStatsTable_Object=MibTable
cdrIPv6DropStatsTable=_CdrIPv6DropStatsTable_Object((1,3,6,1,4,1,9,9,833,1,1,4))
if mibBuilder.loadTexts:cdrIPv6DropStatsTable.setStatus(_A)
_CdrIPv6DropStatsEntry_Object=MibTableRow
cdrIPv6DropStatsEntry=_CdrIPv6DropStatsEntry_Object((1,3,6,1,4,1,9,9,833,1,1,4,1))
cdrIPv6DropStatsEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cdrIPv6DropStatsEntry.setStatus(_A)
_CdrIPv6DropStatsIfIndex_Type=InterfaceIndexOrZero
_CdrIPv6DropStatsIfIndex_Object=MibTableColumn
cdrIPv6DropStatsIfIndex=_CdrIPv6DropStatsIfIndex_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,1),_CdrIPv6DropStatsIfIndex_Type())
cdrIPv6DropStatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cdrIPv6DropStatsIfIndex.setStatus(_A)
_CdrIPv6DropStatsRelayDisabled_Type=Counter32
_CdrIPv6DropStatsRelayDisabled_Object=MibTableColumn
cdrIPv6DropStatsRelayDisabled=_CdrIPv6DropStatsRelayDisabled_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,2),_CdrIPv6DropStatsRelayDisabled_Type())
cdrIPv6DropStatsRelayDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsRelayDisabled.setStatus(_A)
_CdrIPv6DropStatsMaxHopsExceeded_Type=Counter32
_CdrIPv6DropStatsMaxHopsExceeded_Object=MibTableColumn
cdrIPv6DropStatsMaxHopsExceeded=_CdrIPv6DropStatsMaxHopsExceeded_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,3),_CdrIPv6DropStatsMaxHopsExceeded_Type())
cdrIPv6DropStatsMaxHopsExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsMaxHopsExceeded.setStatus(_A)
_CdrIPv6DropStatsInvalidPkts_Type=Counter32
_CdrIPv6DropStatsInvalidPkts_Object=MibTableColumn
cdrIPv6DropStatsInvalidPkts=_CdrIPv6DropStatsInvalidPkts_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,4),_CdrIPv6DropStatsInvalidPkts_Type())
cdrIPv6DropStatsInvalidPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsInvalidPkts.setStatus(_A)
_CdrIPv6DropStatsUnknownOpInterface_Type=Counter32
_CdrIPv6DropStatsUnknownOpInterface_Object=MibTableColumn
cdrIPv6DropStatsUnknownOpInterface=_CdrIPv6DropStatsUnknownOpInterface_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,5),_CdrIPv6DropStatsUnknownOpInterface_Type())
cdrIPv6DropStatsUnknownOpInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsUnknownOpInterface.setStatus(_A)
_CdrIPv6DropStatsInvalidVRF_Type=Counter32
_CdrIPv6DropStatsInvalidVRF_Object=MibTableColumn
cdrIPv6DropStatsInvalidVRF=_CdrIPv6DropStatsInvalidVRF_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,6),_CdrIPv6DropStatsInvalidVRF_Type())
cdrIPv6DropStatsInvalidVRF.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsInvalidVRF.setStatus(_A)
_CdrIPv6DropStatsOptionInsertionFailed_Type=Counter32
_CdrIPv6DropStatsOptionInsertionFailed_Object=MibTableColumn
cdrIPv6DropStatsOptionInsertionFailed=_CdrIPv6DropStatsOptionInsertionFailed_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,7),_CdrIPv6DropStatsOptionInsertionFailed_Type())
cdrIPv6DropStatsOptionInsertionFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsOptionInsertionFailed.setStatus(_A)
_CdrIPv6DropStatsDirectReplyFromServer_Type=Counter32
_CdrIPv6DropStatsDirectReplyFromServer_Object=MibTableColumn
cdrIPv6DropStatsDirectReplyFromServer=_CdrIPv6DropStatsDirectReplyFromServer_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,8),_CdrIPv6DropStatsDirectReplyFromServer_Type())
cdrIPv6DropStatsDirectReplyFromServer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsDirectReplyFromServer.setStatus(_A)
_CdrIPv6DropStatsIPv6AddrNotConfigured_Type=Counter32
_CdrIPv6DropStatsIPv6AddrNotConfigured_Object=MibTableColumn
cdrIPv6DropStatsIPv6AddrNotConfigured=_CdrIPv6DropStatsIPv6AddrNotConfigured_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,9),_CdrIPv6DropStatsIPv6AddrNotConfigured_Type())
cdrIPv6DropStatsIPv6AddrNotConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsIPv6AddrNotConfigured.setStatus(_A)
_CdrIPv6DropStatsInterfaceError_Type=Counter32
_CdrIPv6DropStatsInterfaceError_Object=MibTableColumn
cdrIPv6DropStatsInterfaceError=_CdrIPv6DropStatsInterfaceError_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,10),_CdrIPv6DropStatsInterfaceError_Type())
cdrIPv6DropStatsInterfaceError.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsInterfaceError.setStatus(_A)
_CdrIPv6DropStatsVpnOptionDisabled_Type=Counter32
_CdrIPv6DropStatsVpnOptionDisabled_Object=MibTableColumn
cdrIPv6DropStatsVpnOptionDisabled=_CdrIPv6DropStatsVpnOptionDisabled_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,11),_CdrIPv6DropStatsVpnOptionDisabled_Type())
cdrIPv6DropStatsVpnOptionDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsVpnOptionDisabled.setStatus(_A)
_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Type=Counter32
_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Object=MibTableColumn
cdrIPv6DropStatsIpv6ExtnHeaderPresent=_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,12),_CdrIPv6DropStatsIpv6ExtnHeaderPresent_Type())
cdrIPv6DropStatsIpv6ExtnHeaderPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsIpv6ExtnHeaderPresent.setStatus(_A)
_CdrIPv6DropStatsReqDroppedOnMCT_Type=Counter32
_CdrIPv6DropStatsReqDroppedOnMCT_Object=MibTableColumn
cdrIPv6DropStatsReqDroppedOnMCT=_CdrIPv6DropStatsReqDroppedOnMCT_Object((1,3,6,1,4,1,9,9,833,1,1,4,1,13),_CdrIPv6DropStatsReqDroppedOnMCT_Type())
cdrIPv6DropStatsReqDroppedOnMCT.setMaxAccess(_C)
if mibBuilder.loadTexts:cdrIPv6DropStatsReqDroppedOnMCT.setStatus(_A)
_CiscoDhcpRelayMIBConform_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayMIBConform=_CiscoDhcpRelayMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,833,2))
_CiscoDhcpRelayMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayMIBCompliances=_CiscoDhcpRelayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,833,2,1))
_CiscoDhcpRelayMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDhcpRelayMIBGroups=_CiscoDhcpRelayMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,833,2,2))
cdrStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,833,2,2,1))
cdrStatsGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cdrStatsGroup.setStatus(_A)
cdrDropStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,833,2,2,2))
cdrDropStatsGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cdrDropStatsGroup.setStatus(_A)
cdrIPv6StatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,833,2,2,3))
cdrIPv6StatsGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cdrIPv6StatsGroup.setStatus(_A)
cdrIPv6DropStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,833,2,2,4))
cdrIPv6DropStatsGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cdrIPv6DropStatsGroup.setStatus(_A)
ciscoDhcpRelayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,833,2,1,1))
ciscoDhcpRelayMIBCompliance.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ciscoDhcpRelayMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDhcpRelayMIB':ciscoDhcpRelayMIB,'ciscoDhcpRelayMIBNotifs':ciscoDhcpRelayMIBNotifs,'ciscoDhcpRelayMIBObjects':ciscoDhcpRelayMIBObjects,'ciscoDhcpRelayStats':ciscoDhcpRelayStats,'cdrStatsTable':cdrStatsTable,'cdrStatsEntry':cdrStatsEntry,_F:cdrStatsIfIndex,_G:cdrStatsPktType,_O:cdrStatsPktsReceived,_P:cdrStatsPktsForwarded,_Q:cdrStatsPktsDropped,'cdrDropStatsTable':cdrDropStatsTable,'cdrDropStatsEntry':cdrDropStatsEntry,_K:cdrDropStatsIfIndex,_R:cdrDropStatsRelayNotEnabled,_S:cdrDropStatsInvalidMsgType,_T:cdrDropStatsInterfaceError,_U:cdrDropStatsTxFailureServer,_V:cdrDropStatsTxFailureClient,_W:cdrDropStatsUnknownOpInterface,_X:cdrDropStatsUnknownVrfOrInterface,_Y:cdrDropStatsMaxHopsExceeded,_Z:cdrDropStatsOpt82ValidationFailure,_a:cdrDropStatsMalformedPkts,_b:cdrDropStatsUntrustablePort,_c:cdrDropStatsReqDroppedOnMCT,'cdrIPv6StatsTable':cdrIPv6StatsTable,'cdrIPv6StatsEntry':cdrIPv6StatsEntry,_L:cdrIPv6StatsIfIndex,_M:cdrIPv6StatsPktType,_d:cdrIPv6StatsPktsReceived,_e:cdrIPv6StatsPktsForwarded,_f:cdrIPv6StatsPktsDropped,'cdrIPv6DropStatsTable':cdrIPv6DropStatsTable,'cdrIPv6DropStatsEntry':cdrIPv6DropStatsEntry,_N:cdrIPv6DropStatsIfIndex,_g:cdrIPv6DropStatsRelayDisabled,_h:cdrIPv6DropStatsMaxHopsExceeded,_i:cdrIPv6DropStatsInvalidPkts,_j:cdrIPv6DropStatsUnknownOpInterface,_k:cdrIPv6DropStatsInvalidVRF,_l:cdrIPv6DropStatsOptionInsertionFailed,_m:cdrIPv6DropStatsDirectReplyFromServer,_o:cdrIPv6DropStatsIPv6AddrNotConfigured,_n:cdrIPv6DropStatsInterfaceError,_p:cdrIPv6DropStatsVpnOptionDisabled,_q:cdrIPv6DropStatsIpv6ExtnHeaderPresent,_r:cdrIPv6DropStatsReqDroppedOnMCT,'ciscoDhcpRelayMIBConform':ciscoDhcpRelayMIBConform,'ciscoDhcpRelayMIBCompliances':ciscoDhcpRelayMIBCompliances,'ciscoDhcpRelayMIBCompliance':ciscoDhcpRelayMIBCompliance,'ciscoDhcpRelayMIBGroups':ciscoDhcpRelayMIBGroups,_s:cdrStatsGroup,_t:cdrDropStatsGroup,_u:cdrIPv6StatsGroup,_v:cdrIPv6DropStatsGroup})