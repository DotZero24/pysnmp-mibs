_X='l2tpErrTrapType'
_W='l2tpSessionStatus'
_V='l2tpRemoteSessionId'
_U='l2tpLocalSessionId'
_T='l2tpTotalActiveSessions'
_S='l2tpTotalConfiguredSessions'
_R='l2tpTotalConfiguredPw'
_Q='l2tpGlobalEnable'
_P='l2tpPortStatsIfIndex'
_O='l2tpSessionRemoteEndId'
_N='l2tpXconnectId'
_M='l2tpXconnectIfIndex'
_L='l2tpPwIndex'
_K='l2tpPortIfIndex'
_J='l2tpRemoteEndId'
_I='EnabledStatus'
_H='read-write'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='FutureL2tp-MIB'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp','TruthValue')
futureL2tpMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,108))
if mibBuilder.loadTexts:futureL2tpMIB.setRevisions(('2012-09-05 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_L2tp_ObjectIdentity=ObjectIdentity
l2tp=_L2tp_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1))
_L2tpGlobalInfo_ObjectIdentity=ObjectIdentity
l2tpGlobalInfo=_L2tpGlobalInfo_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,1))
class _L2tpSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_L2tpSystemControl_Type.__name__=_E
_L2tpSystemControl_Object=MibScalar
l2tpSystemControl=_L2tpSystemControl_Object((1,3,6,1,4,1,29601,2,108,1,1,1),_L2tpSystemControl_Type())
l2tpSystemControl.setMaxAccess(_H)
if mibBuilder.loadTexts:l2tpSystemControl.setStatus(_A)
class _L2tpGlobalEnable_Type(EnabledStatus):defaultValue=2
_L2tpGlobalEnable_Type.__name__=_I
_L2tpGlobalEnable_Object=MibScalar
l2tpGlobalEnable=_L2tpGlobalEnable_Object((1,3,6,1,4,1,29601,2,108,1,1,2),_L2tpGlobalEnable_Type())
l2tpGlobalEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:l2tpGlobalEnable.setStatus(_A)
class _L2tpVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('version3',1))
_L2tpVersion_Type.__name__=_E
_L2tpVersion_Object=MibScalar
l2tpVersion=_L2tpVersion_Object((1,3,6,1,4,1,29601,2,108,1,1,3),_L2tpVersion_Type())
l2tpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpVersion.setStatus(_A)
_L2tpTotalConfiguredPw_Type=Counter32
_L2tpTotalConfiguredPw_Object=MibScalar
l2tpTotalConfiguredPw=_L2tpTotalConfiguredPw_Object((1,3,6,1,4,1,29601,2,108,1,1,4),_L2tpTotalConfiguredPw_Type())
l2tpTotalConfiguredPw.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpTotalConfiguredPw.setStatus(_A)
_L2tpTotalConfiguredSessions_Type=Counter32
_L2tpTotalConfiguredSessions_Object=MibScalar
l2tpTotalConfiguredSessions=_L2tpTotalConfiguredSessions_Object((1,3,6,1,4,1,29601,2,108,1,1,5),_L2tpTotalConfiguredSessions_Type())
l2tpTotalConfiguredSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpTotalConfiguredSessions.setStatus(_A)
_L2tpTotalActiveSessions_Type=Counter32
_L2tpTotalActiveSessions_Object=MibScalar
l2tpTotalActiveSessions=_L2tpTotalActiveSessions_Object((1,3,6,1,4,1,29601,2,108,1,1,6),_L2tpTotalActiveSessions_Type())
l2tpTotalActiveSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpTotalActiveSessions.setStatus(_A)
_L2tpClearGlobalStats_Type=TruthValue
_L2tpClearGlobalStats_Object=MibScalar
l2tpClearGlobalStats=_L2tpClearGlobalStats_Object((1,3,6,1,4,1,29601,2,108,1,1,7),_L2tpClearGlobalStats_Type())
l2tpClearGlobalStats.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpClearGlobalStats.setStatus(_A)
_L2tpClearSessionStats_Type=TruthValue
_L2tpClearSessionStats_Object=MibScalar
l2tpClearSessionStats=_L2tpClearSessionStats_Object((1,3,6,1,4,1,29601,2,108,1,1,8),_L2tpClearSessionStats_Type())
l2tpClearSessionStats.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpClearSessionStats.setStatus(_A)
_L2tpInvalidEncapInfoDrop_Type=Counter32
_L2tpInvalidEncapInfoDrop_Object=MibScalar
l2tpInvalidEncapInfoDrop=_L2tpInvalidEncapInfoDrop_Object((1,3,6,1,4,1,29601,2,108,1,1,9),_L2tpInvalidEncapInfoDrop_Type())
l2tpInvalidEncapInfoDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpInvalidEncapInfoDrop.setStatus(_A)
_L2tpInvalidDecapInfoDrop_Type=Counter32
_L2tpInvalidDecapInfoDrop_Object=MibScalar
l2tpInvalidDecapInfoDrop=_L2tpInvalidDecapInfoDrop_Object((1,3,6,1,4,1,29601,2,108,1,1,10),_L2tpInvalidDecapInfoDrop_Type())
l2tpInvalidDecapInfoDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpInvalidDecapInfoDrop.setStatus(_A)
_L2tpInvalidSessionStatsInfoDrop_Type=Counter32
_L2tpInvalidSessionStatsInfoDrop_Object=MibScalar
l2tpInvalidSessionStatsInfoDrop=_L2tpInvalidSessionStatsInfoDrop_Object((1,3,6,1,4,1,29601,2,108,1,1,11),_L2tpInvalidSessionStatsInfoDrop_Type())
l2tpInvalidSessionStatsInfoDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpInvalidSessionStatsInfoDrop.setStatus(_A)
_L2tpInvalidL2tpPacketDrop_Type=Counter32
_L2tpInvalidL2tpPacketDrop_Object=MibScalar
l2tpInvalidL2tpPacketDrop=_L2tpInvalidL2tpPacketDrop_Object((1,3,6,1,4,1,29601,2,108,1,1,12),_L2tpInvalidL2tpPacketDrop_Type())
l2tpInvalidL2tpPacketDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpInvalidL2tpPacketDrop.setStatus(_A)
_L2tpTotalEncapedPackets_Type=Counter32
_L2tpTotalEncapedPackets_Object=MibScalar
l2tpTotalEncapedPackets=_L2tpTotalEncapedPackets_Object((1,3,6,1,4,1,29601,2,108,1,1,13),_L2tpTotalEncapedPackets_Type())
l2tpTotalEncapedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpTotalEncapedPackets.setStatus(_A)
_L2tpTotalDecapedPackets_Type=Counter32
_L2tpTotalDecapedPackets_Object=MibScalar
l2tpTotalDecapedPackets=_L2tpTotalDecapedPackets_Object((1,3,6,1,4,1,29601,2,108,1,1,14),_L2tpTotalDecapedPackets_Type())
l2tpTotalDecapedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpTotalDecapedPackets.setStatus(_A)
class _L2tpTrcFlag_Type(Integer32):defaultValue=0
_L2tpTrcFlag_Type.__name__=_E
_L2tpTrcFlag_Object=MibScalar
l2tpTrcFlag=_L2tpTrcFlag_Object((1,3,6,1,4,1,29601,2,108,1,1,15),_L2tpTrcFlag_Type())
l2tpTrcFlag.setMaxAccess(_H)
if mibBuilder.loadTexts:l2tpTrcFlag.setStatus(_A)
class _L2tpErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('memfail',1),('bufffail',2)))
_L2tpErrTrapType_Type.__name__=_E
_L2tpErrTrapType_Object=MibScalar
l2tpErrTrapType=_L2tpErrTrapType_Object((1,3,6,1,4,1,29601,2,108,1,1,16),_L2tpErrTrapType_Type())
l2tpErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpErrTrapType.setStatus(_A)
class _L2tpSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_L2tpSetTraps_Type.__name__=_E
_L2tpSetTraps_Object=MibScalar
l2tpSetTraps=_L2tpSetTraps_Object((1,3,6,1,4,1,29601,2,108,1,1,17),_L2tpSetTraps_Type())
l2tpSetTraps.setMaxAccess(_H)
if mibBuilder.loadTexts:l2tpSetTraps.setStatus(_A)
_L2tpPort_ObjectIdentity=ObjectIdentity
l2tpPort=_L2tpPort_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,2))
_L2tpPortTable_Object=MibTable
l2tpPortTable=_L2tpPortTable_Object((1,3,6,1,4,1,29601,2,108,1,2,1))
if mibBuilder.loadTexts:l2tpPortTable.setStatus(_A)
_L2tpPortEntry_Object=MibTableRow
l2tpPortEntry=_L2tpPortEntry_Object((1,3,6,1,4,1,29601,2,108,1,2,1,1))
l2tpPortEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:l2tpPortEntry.setStatus(_A)
_L2tpPortIfIndex_Type=Integer32
_L2tpPortIfIndex_Object=MibTableColumn
l2tpPortIfIndex=_L2tpPortIfIndex_Object((1,3,6,1,4,1,29601,2,108,1,2,1,1,1),_L2tpPortIfIndex_Type())
l2tpPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpPortIfIndex.setStatus(_A)
_L2tpEnabledStatus_Type=EnabledStatus
_L2tpEnabledStatus_Object=MibTableColumn
l2tpEnabledStatus=_L2tpEnabledStatus_Object((1,3,6,1,4,1,29601,2,108,1,2,1,1,2),_L2tpEnabledStatus_Type())
l2tpEnabledStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpEnabledStatus.setStatus(_A)
class _L2tpPortEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('port',1),('port-vlan',2),('qinq',3),('qinAny',4)))
_L2tpPortEncapType_Type.__name__=_E
_L2tpPortEncapType_Object=MibTableColumn
l2tpPortEncapType=_L2tpPortEncapType_Object((1,3,6,1,4,1,29601,2,108,1,2,1,1,3),_L2tpPortEncapType_Type())
l2tpPortEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpPortEncapType.setStatus(_A)
_L2tpPortRowStatus_Type=RowStatus
_L2tpPortRowStatus_Object=MibTableColumn
l2tpPortRowStatus=_L2tpPortRowStatus_Object((1,3,6,1,4,1,29601,2,108,1,2,1,1,4),_L2tpPortRowStatus_Type())
l2tpPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpPortRowStatus.setStatus(_A)
_L2tpPseudowire_ObjectIdentity=ObjectIdentity
l2tpPseudowire=_L2tpPseudowire_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,3))
_L2tpPseudowireTable_Object=MibTable
l2tpPseudowireTable=_L2tpPseudowireTable_Object((1,3,6,1,4,1,29601,2,108,1,3,1))
if mibBuilder.loadTexts:l2tpPseudowireTable.setStatus(_A)
_L2tpPseudowireEntry_Object=MibTableRow
l2tpPseudowireEntry=_L2tpPseudowireEntry_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1))
l2tpPseudowireEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:l2tpPseudowireEntry.setStatus(_A)
_L2tpPwIndex_Type=Unsigned32
_L2tpPwIndex_Object=MibTableColumn
l2tpPwIndex=_L2tpPwIndex_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,1),_L2tpPwIndex_Type())
l2tpPwIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpPwIndex.setStatus(_A)
class _L2tpPwEncapMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('l2tpv3',1),('mpls',2)))
_L2tpPwEncapMode_Type.__name__=_E
_L2tpPwEncapMode_Object=MibTableColumn
l2tpPwEncapMode=_L2tpPwEncapMode_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,2),_L2tpPwEncapMode_Type())
l2tpPwEncapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPwEncapMode.setStatus(_A)
class _L2tpIPSecEnabledStatus_Type(EnabledStatus):defaultValue=2
_L2tpIPSecEnabledStatus_Type.__name__=_I
_L2tpIPSecEnabledStatus_Object=MibTableColumn
l2tpIPSecEnabledStatus=_L2tpIPSecEnabledStatus_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,3),_L2tpIPSecEnabledStatus_Type())
l2tpIPSecEnabledStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpIPSecEnabledStatus.setStatus(_A)
class _L2tpIPSecMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tunnel',1),('transparent',2)))
_L2tpIPSecMode_Type.__name__=_E
_L2tpIPSecMode_Object=MibTableColumn
l2tpIPSecMode=_L2tpIPSecMode_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,4),_L2tpIPSecMode_Type())
l2tpIPSecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpIPSecMode.setStatus(_A)
_L2tpPwLoopBack_Type=DisplayString
_L2tpPwLoopBack_Object=MibTableColumn
l2tpPwLoopBack=_L2tpPwLoopBack_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,5),_L2tpPwLoopBack_Type())
l2tpPwLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpPwLoopBack.setStatus(_A)
_L2tpRemoteIpAddress_Type=IpAddress
_L2tpRemoteIpAddress_Object=MibTableColumn
l2tpRemoteIpAddress=_L2tpRemoteIpAddress_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,6),_L2tpRemoteIpAddress_Type())
l2tpRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpRemoteIpAddress.setStatus(_A)
_L2tpPwSrcMacAddr_Type=MacAddress
_L2tpPwSrcMacAddr_Object=MibTableColumn
l2tpPwSrcMacAddr=_L2tpPwSrcMacAddr_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,7),_L2tpPwSrcMacAddr_Type())
l2tpPwSrcMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPwSrcMacAddr.setStatus(_A)
_L2tpPwDestMacAddr_Type=MacAddress
_L2tpPwDestMacAddr_Object=MibTableColumn
l2tpPwDestMacAddr=_L2tpPwDestMacAddr_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,8),_L2tpPwDestMacAddr_Type())
l2tpPwDestMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPwDestMacAddr.setStatus(_A)
_L2tpPwRowStatus_Type=RowStatus
_L2tpPwRowStatus_Object=MibTableColumn
l2tpPwRowStatus=_L2tpPwRowStatus_Object((1,3,6,1,4,1,29601,2,108,1,3,1,1,9),_L2tpPwRowStatus_Type())
l2tpPwRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpPwRowStatus.setStatus(_A)
_L2tpSession_ObjectIdentity=ObjectIdentity
l2tpSession=_L2tpSession_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,4))
_L2tpSessionTable_Object=MibTable
l2tpSessionTable=_L2tpSessionTable_Object((1,3,6,1,4,1,29601,2,108,1,4,1))
if mibBuilder.loadTexts:l2tpSessionTable.setStatus(_A)
_L2tpSessionEntry_Object=MibTableRow
l2tpSessionEntry=_L2tpSessionEntry_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1))
l2tpSessionEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:l2tpSessionEntry.setStatus(_A)
class _L2tpRemoteEndId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpRemoteEndId_Type.__name__=_G
_L2tpRemoteEndId_Object=MibTableColumn
l2tpRemoteEndId=_L2tpRemoteEndId_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,1),_L2tpRemoteEndId_Type())
l2tpRemoteEndId.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpRemoteEndId.setStatus(_A)
class _L2tpLocalSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpLocalSessionId_Type.__name__=_G
_L2tpLocalSessionId_Object=MibTableColumn
l2tpLocalSessionId=_L2tpLocalSessionId_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,2),_L2tpLocalSessionId_Type())
l2tpLocalSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpLocalSessionId.setStatus(_A)
class _L2tpRemoteSessionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpRemoteSessionId_Type.__name__=_G
_L2tpRemoteSessionId_Object=MibTableColumn
l2tpRemoteSessionId=_L2tpRemoteSessionId_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,3),_L2tpRemoteSessionId_Type())
l2tpRemoteSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpRemoteSessionId.setStatus(_A)
_L2tpSessionPwIndex_Type=Integer32
_L2tpSessionPwIndex_Object=MibTableColumn
l2tpSessionPwIndex=_L2tpSessionPwIndex_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,4),_L2tpSessionPwIndex_Type())
l2tpSessionPwIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionPwIndex.setStatus(_A)
class _L2tpSessionCookieSize_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('four-byte',1),('eight-byte',2),('none',3)))
_L2tpSessionCookieSize_Type.__name__=_E
_L2tpSessionCookieSize_Object=MibTableColumn
l2tpSessionCookieSize=_L2tpSessionCookieSize_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,5),_L2tpSessionCookieSize_Type())
l2tpSessionCookieSize.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionCookieSize.setStatus(_A)
_L2tpSessionLocalCookie_Type=OctetString
_L2tpSessionLocalCookie_Object=MibTableColumn
l2tpSessionLocalCookie=_L2tpSessionLocalCookie_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,6),_L2tpSessionLocalCookie_Type())
l2tpSessionLocalCookie.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionLocalCookie.setStatus(_A)
_L2tpSessionRemoteCookie_Type=OctetString
_L2tpSessionRemoteCookie_Object=MibTableColumn
l2tpSessionRemoteCookie=_L2tpSessionRemoteCookie_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,7),_L2tpSessionRemoteCookie_Type())
l2tpSessionRemoteCookie.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRemoteCookie.setStatus(_A)
class _L2tpSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_L2tpSessionStatus_Type.__name__=_E
_L2tpSessionStatus_Object=MibTableColumn
l2tpSessionStatus=_L2tpSessionStatus_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,8),_L2tpSessionStatus_Type())
l2tpSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpSessionStatus.setStatus(_A)
_L2tpSessionClearStatistics_Type=TruthValue
_L2tpSessionClearStatistics_Object=MibTableColumn
l2tpSessionClearStatistics=_L2tpSessionClearStatistics_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,9),_L2tpSessionClearStatistics_Type())
l2tpSessionClearStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionClearStatistics.setStatus(_A)
_L2tpSessionRowStatus_Type=RowStatus
_L2tpSessionRowStatus_Object=MibTableColumn
l2tpSessionRowStatus=_L2tpSessionRowStatus_Object((1,3,6,1,4,1,29601,2,108,1,4,1,1,10),_L2tpSessionRowStatus_Type())
l2tpSessionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpSessionRowStatus.setStatus(_A)
_L2tpXconnect_ObjectIdentity=ObjectIdentity
l2tpXconnect=_L2tpXconnect_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,5))
_L2tpXconnectTable_Object=MibTable
l2tpXconnectTable=_L2tpXconnectTable_Object((1,3,6,1,4,1,29601,2,108,1,5,1))
if mibBuilder.loadTexts:l2tpXconnectTable.setStatus(_A)
_L2tpXconnectEntry_Object=MibTableRow
l2tpXconnectEntry=_L2tpXconnectEntry_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1))
l2tpXconnectEntry.setIndexNames((0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:l2tpXconnectEntry.setStatus(_A)
_L2tpXconnectIfIndex_Type=Integer32
_L2tpXconnectIfIndex_Object=MibTableColumn
l2tpXconnectIfIndex=_L2tpXconnectIfIndex_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,1),_L2tpXconnectIfIndex_Type())
l2tpXconnectIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpXconnectIfIndex.setStatus(_A)
class _L2tpXconnectId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpXconnectId_Type.__name__=_G
_L2tpXconnectId_Object=MibTableColumn
l2tpXconnectId=_L2tpXconnectId_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,2),_L2tpXconnectId_Type())
l2tpXconnectId.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpXconnectId.setStatus(_A)
class _L2tpXconnectRemoteEndId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_L2tpXconnectRemoteEndId_Type.__name__=_G
_L2tpXconnectRemoteEndId_Object=MibTableColumn
l2tpXconnectRemoteEndId=_L2tpXconnectRemoteEndId_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,3),_L2tpXconnectRemoteEndId_Type())
l2tpXconnectRemoteEndId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpXconnectRemoteEndId.setStatus(_A)
class _L2tpXconnectInnerVlanId_Type(Integer32):defaultValue=1
_L2tpXconnectInnerVlanId_Type.__name__=_E
_L2tpXconnectInnerVlanId_Object=MibTableColumn
l2tpXconnectInnerVlanId=_L2tpXconnectInnerVlanId_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,4),_L2tpXconnectInnerVlanId_Type())
l2tpXconnectInnerVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpXconnectInnerVlanId.setStatus(_A)
class _L2tpXconnectOuterVlanId_Type(Integer32):defaultValue=1
_L2tpXconnectOuterVlanId_Type.__name__=_E
_L2tpXconnectOuterVlanId_Object=MibTableColumn
l2tpXconnectOuterVlanId=_L2tpXconnectOuterVlanId_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,5),_L2tpXconnectOuterVlanId_Type())
l2tpXconnectOuterVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpXconnectOuterVlanId.setStatus(_A)
_L2tpXconnectRowStatus_Type=RowStatus
_L2tpXconnectRowStatus_Object=MibTableColumn
l2tpXconnectRowStatus=_L2tpXconnectRowStatus_Object((1,3,6,1,4,1,29601,2,108,1,5,1,1,6),_L2tpXconnectRowStatus_Type())
l2tpXconnectRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:l2tpXconnectRowStatus.setStatus(_A)
_L2tpSessionStats_ObjectIdentity=ObjectIdentity
l2tpSessionStats=_L2tpSessionStats_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,6))
_L2tpSessionStatsTable_Object=MibTable
l2tpSessionStatsTable=_L2tpSessionStatsTable_Object((1,3,6,1,4,1,29601,2,108,1,6,1))
if mibBuilder.loadTexts:l2tpSessionStatsTable.setStatus(_A)
_L2tpSessionStatsEntry_Object=MibTableRow
l2tpSessionStatsEntry=_L2tpSessionStatsEntry_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1))
l2tpSessionStatsEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:l2tpSessionStatsEntry.setStatus(_A)
_L2tpSessionRemoteEndId_Type=Unsigned32
_L2tpSessionRemoteEndId_Object=MibTableColumn
l2tpSessionRemoteEndId=_L2tpSessionRemoteEndId_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1,1),_L2tpSessionRemoteEndId_Type())
l2tpSessionRemoteEndId.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpSessionRemoteEndId.setStatus(_A)
_L2tpSessionStatsTotalEncap_Type=Counter32
_L2tpSessionStatsTotalEncap_Object=MibTableColumn
l2tpSessionStatsTotalEncap=_L2tpSessionStatsTotalEncap_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1,2),_L2tpSessionStatsTotalEncap_Type())
l2tpSessionStatsTotalEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpSessionStatsTotalEncap.setStatus(_A)
_L2tpSessionStatsTotalDecap_Type=Counter32
_L2tpSessionStatsTotalDecap_Object=MibTableColumn
l2tpSessionStatsTotalDecap=_L2tpSessionStatsTotalDecap_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1,3),_L2tpSessionStatsTotalDecap_Type())
l2tpSessionStatsTotalDecap.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpSessionStatsTotalDecap.setStatus(_A)
_L2tpSessionStatsCookieMismatch_Type=Counter32
_L2tpSessionStatsCookieMismatch_Object=MibTableColumn
l2tpSessionStatsCookieMismatch=_L2tpSessionStatsCookieMismatch_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1,4),_L2tpSessionStatsCookieMismatch_Type())
l2tpSessionStatsCookieMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpSessionStatsCookieMismatch.setStatus(_A)
_L2tpSessionStatsInvalidPeerIp_Type=Counter32
_L2tpSessionStatsInvalidPeerIp_Object=MibTableColumn
l2tpSessionStatsInvalidPeerIp=_L2tpSessionStatsInvalidPeerIp_Object((1,3,6,1,4,1,29601,2,108,1,6,1,1,5),_L2tpSessionStatsInvalidPeerIp_Type())
l2tpSessionStatsInvalidPeerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpSessionStatsInvalidPeerIp.setStatus(_A)
_L2tpPortStats_ObjectIdentity=ObjectIdentity
l2tpPortStats=_L2tpPortStats_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,7))
_L2tpPortStatsTable_Object=MibTable
l2tpPortStatsTable=_L2tpPortStatsTable_Object((1,3,6,1,4,1,29601,2,108,1,7,1))
if mibBuilder.loadTexts:l2tpPortStatsTable.setStatus(_A)
_L2tpPortStatsEntry_Object=MibTableRow
l2tpPortStatsEntry=_L2tpPortStatsEntry_Object((1,3,6,1,4,1,29601,2,108,1,7,1,1))
l2tpPortStatsEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:l2tpPortStatsEntry.setStatus(_A)
_L2tpPortStatsIfIndex_Type=Integer32
_L2tpPortStatsIfIndex_Object=MibTableColumn
l2tpPortStatsIfIndex=_L2tpPortStatsIfIndex_Object((1,3,6,1,4,1,29601,2,108,1,7,1,1,1),_L2tpPortStatsIfIndex_Type())
l2tpPortStatsIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:l2tpPortStatsIfIndex.setStatus(_A)
_L2tpPortStatsInvalidFrames_Type=Counter32
_L2tpPortStatsInvalidFrames_Object=MibTableColumn
l2tpPortStatsInvalidFrames=_L2tpPortStatsInvalidFrames_Object((1,3,6,1,4,1,29601,2,108,1,7,1,1,2),_L2tpPortStatsInvalidFrames_Type())
l2tpPortStatsInvalidFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPortStatsInvalidFrames.setStatus(_A)
_L2tpPortTotalTx_Type=Counter32
_L2tpPortTotalTx_Object=MibTableColumn
l2tpPortTotalTx=_L2tpPortTotalTx_Object((1,3,6,1,4,1,29601,2,108,1,7,1,1,3),_L2tpPortTotalTx_Type())
l2tpPortTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPortTotalTx.setStatus(_A)
_L2tpPortTotalRx_Type=Counter32
_L2tpPortTotalRx_Object=MibTableColumn
l2tpPortTotalRx=_L2tpPortTotalRx_Object((1,3,6,1,4,1,29601,2,108,1,7,1,1,4),_L2tpPortTotalRx_Type())
l2tpPortTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:l2tpPortTotalRx.setStatus(_A)
_L2tpNotifications_ObjectIdentity=ObjectIdentity
l2tpNotifications=_L2tpNotifications_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,8))
_L2tpTraps_ObjectIdentity=ObjectIdentity
l2tpTraps=_L2tpTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,108,1,8,0))
l2tpTrapGlobalInfo=NotificationType((1,3,6,1,4,1,29601,2,108,1,8,0,1))
l2tpTrapGlobalInfo.setObjects(*((_D,_Q),(_D,_R),(_D,_S),(_D,_T)))
if mibBuilder.loadTexts:l2tpTrapGlobalInfo.setStatus(_A)
l2tpTrapSessionStatus=NotificationType((1,3,6,1,4,1,29601,2,108,1,8,0,2))
l2tpTrapSessionStatus.setObjects(*((_D,_J),(_D,_U),(_D,_V),(_D,_W)))
if mibBuilder.loadTexts:l2tpTrapSessionStatus.setStatus(_A)
l2tpErrTrap=NotificationType((1,3,6,1,4,1,29601,2,108,1,8,0,3))
l2tpErrTrap.setObjects((_D,_X))
if mibBuilder.loadTexts:l2tpErrTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_I:EnabledStatus,'futureL2tpMIB':futureL2tpMIB,'l2tp':l2tp,'l2tpGlobalInfo':l2tpGlobalInfo,'l2tpSystemControl':l2tpSystemControl,_Q:l2tpGlobalEnable,'l2tpVersion':l2tpVersion,_R:l2tpTotalConfiguredPw,_S:l2tpTotalConfiguredSessions,_T:l2tpTotalActiveSessions,'l2tpClearGlobalStats':l2tpClearGlobalStats,'l2tpClearSessionStats':l2tpClearSessionStats,'l2tpInvalidEncapInfoDrop':l2tpInvalidEncapInfoDrop,'l2tpInvalidDecapInfoDrop':l2tpInvalidDecapInfoDrop,'l2tpInvalidSessionStatsInfoDrop':l2tpInvalidSessionStatsInfoDrop,'l2tpInvalidL2tpPacketDrop':l2tpInvalidL2tpPacketDrop,'l2tpTotalEncapedPackets':l2tpTotalEncapedPackets,'l2tpTotalDecapedPackets':l2tpTotalDecapedPackets,'l2tpTrcFlag':l2tpTrcFlag,_X:l2tpErrTrapType,'l2tpSetTraps':l2tpSetTraps,'l2tpPort':l2tpPort,'l2tpPortTable':l2tpPortTable,'l2tpPortEntry':l2tpPortEntry,_K:l2tpPortIfIndex,'l2tpEnabledStatus':l2tpEnabledStatus,'l2tpPortEncapType':l2tpPortEncapType,'l2tpPortRowStatus':l2tpPortRowStatus,'l2tpPseudowire':l2tpPseudowire,'l2tpPseudowireTable':l2tpPseudowireTable,'l2tpPseudowireEntry':l2tpPseudowireEntry,_L:l2tpPwIndex,'l2tpPwEncapMode':l2tpPwEncapMode,'l2tpIPSecEnabledStatus':l2tpIPSecEnabledStatus,'l2tpIPSecMode':l2tpIPSecMode,'l2tpPwLoopBack':l2tpPwLoopBack,'l2tpRemoteIpAddress':l2tpRemoteIpAddress,'l2tpPwSrcMacAddr':l2tpPwSrcMacAddr,'l2tpPwDestMacAddr':l2tpPwDestMacAddr,'l2tpPwRowStatus':l2tpPwRowStatus,'l2tpSession':l2tpSession,'l2tpSessionTable':l2tpSessionTable,'l2tpSessionEntry':l2tpSessionEntry,_J:l2tpRemoteEndId,_U:l2tpLocalSessionId,_V:l2tpRemoteSessionId,'l2tpSessionPwIndex':l2tpSessionPwIndex,'l2tpSessionCookieSize':l2tpSessionCookieSize,'l2tpSessionLocalCookie':l2tpSessionLocalCookie,'l2tpSessionRemoteCookie':l2tpSessionRemoteCookie,_W:l2tpSessionStatus,'l2tpSessionClearStatistics':l2tpSessionClearStatistics,'l2tpSessionRowStatus':l2tpSessionRowStatus,'l2tpXconnect':l2tpXconnect,'l2tpXconnectTable':l2tpXconnectTable,'l2tpXconnectEntry':l2tpXconnectEntry,_M:l2tpXconnectIfIndex,_N:l2tpXconnectId,'l2tpXconnectRemoteEndId':l2tpXconnectRemoteEndId,'l2tpXconnectInnerVlanId':l2tpXconnectInnerVlanId,'l2tpXconnectOuterVlanId':l2tpXconnectOuterVlanId,'l2tpXconnectRowStatus':l2tpXconnectRowStatus,'l2tpSessionStats':l2tpSessionStats,'l2tpSessionStatsTable':l2tpSessionStatsTable,'l2tpSessionStatsEntry':l2tpSessionStatsEntry,_O:l2tpSessionRemoteEndId,'l2tpSessionStatsTotalEncap':l2tpSessionStatsTotalEncap,'l2tpSessionStatsTotalDecap':l2tpSessionStatsTotalDecap,'l2tpSessionStatsCookieMismatch':l2tpSessionStatsCookieMismatch,'l2tpSessionStatsInvalidPeerIp':l2tpSessionStatsInvalidPeerIp,'l2tpPortStats':l2tpPortStats,'l2tpPortStatsTable':l2tpPortStatsTable,'l2tpPortStatsEntry':l2tpPortStatsEntry,_P:l2tpPortStatsIfIndex,'l2tpPortStatsInvalidFrames':l2tpPortStatsInvalidFrames,'l2tpPortTotalTx':l2tpPortTotalTx,'l2tpPortTotalRx':l2tpPortTotalRx,'l2tpNotifications':l2tpNotifications,'l2tpTraps':l2tpTraps,'l2tpTrapGlobalInfo':l2tpTrapGlobalInfo,'l2tpTrapSessionStatus':l2tpTrapSessionStatus,'l2tpErrTrap':l2tpErrTrap})