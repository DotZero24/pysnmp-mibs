_BD='ciscoGslbDnsGlobalNotifStatsGroup'
_BC='ciscoGslbDnsGlobalRateLimitGroup'
_BB='ciscoGslbDnsNotifGroup'
_BA='ciscoGslbDnsNotifObjectsGroup'
_B9='ciscoGslbDnsNotifControlGroup'
_B8='ciscoGslbDnsRuleGroup'
_B7='ciscoGslbDnsSourceAddGroup'
_B6='ciscoGslbDnsDomainGroup'
_B5='ciscoGslbDnsAnswerGroup'
_B4='ciscoGslbDnsGlobalStatsGroup'
_B3='ciscoGslbDnsGlobalGroup'
_B2='ciscoGslbAnswerEventStatusChange'
_B1='ciscoGslbDnsEventClause'
_B0='cgdDnsClauseTrapRateLimit'
_A_='cgdAnsTrapRateLimit'
_Az='cgdDnsAnswerNotifEnable'
_Ay='cgdDnsClauseNotifEnable'
_Ax='cgdClauseRowStatus'
_Aw='cgdClauseStorageType'
_Av='cgdClauseHits'
_Au='cgdClauseBalanceMethod'
_At='cgdClauseAnsGrpName'
_As='cgdDnsRuleRowStatus'
_Ar='cgdDnsRuleStorageType'
_Aq='cgdDnsRuleSuccesses'
_Ap='cgdDnsRuleHits'
_Ao='cgdDNSRuleDomainList'
_An='cgdSourceAddList'
_Am='cgdThirdClauseId'
_Al='cgdSourceAddressRowStatus'
_Ak='cgdSourceAddressStorageType'
_Aj='cgdSourceAddressRate4Hr'
_Ai='cgdSourceAddressRate30Min'
_Ah='cgdSourceAddressRate5Min'
_Ag='cgdSourceAddressRate1Min'
_Af='cgdSourceAddressHits'
_Ae='cgdSourceAddressList'
_Ad='cgdSourceAddressPrefixLength'
_Ac='cgdSourceAddressAddress'
_Ab='cgdSourceAddressAddressType'
_Aa='cgdSourceAddressListRowStatus'
_AZ='cgdSourceAddressListStorageType'
_AY='cgdSourceAddressListHits'
_AX='cgdDomainRowStatus'
_AW='cgdDomainStorageType'
_AV='cgdDomainRate4Hr'
_AU='cgdDomainRate30Min'
_AT='cgdDomainRate5Min'
_AS='cgdDomainRate1Min'
_AR='cgdDomainHits'
_AQ='cgdDomainList'
_AP='cgdDomainName'
_AO='cgdDomainListRowStatus'
_AN='cgdDomainListStorageType'
_AM='cgdDomainListHits'
_AL='cgdAnswerRowStatus'
_AK='cgdAnswerStorageType'
_AJ='cgdAnswerRate4Hr'
_AI='cgdAnswerRate30Min'
_AH='cgdAnswerRate5Min'
_AG='cgdAnswerRate1Min'
_AF='cgdAnswerHits'
_AE='cgdAnswerAdminState'
_AD='cgdAnswerGrpName'
_AC='cgdAnswerGroupRowStatus'
_AB='cgdAnswerGroupStorageType'
_AA='cgdAnswerGroupHits'
_A9='cgdAnswerGroupType'
_A8='cgdDnsPollSockErrs'
_A7='cgdDnsTcpSrcPortErrs'
_A6='cgdDnsUdpSrcPortErrs'
_A5='cgdDnsQueryRatePeak'
_A4='cgdDnsQueryRateCurrent'
_A3='cgdProxLkupRcvdResps'
_A2='cgdProxLkupSentReqs'
_A1='cgdBoomServSentReqs'
_A0='cgdNSFwdRcvdResps'
_z='cgdNSFwdSentQueries'
_y='cgdDnsDroppedQueries'
_x='cgdDnsUnmatchedQueries'
_w='cgdDnsRcvdHostAddrQueries'
_v='cgdDnsRcvdQueries'
_u='cgdTotalRules'
_t='cgdTotalAnswerGroups'
_s='cgdTotalAnswers'
_r='cgdTotalSourceAddressLists'
_q='cgdTotalSourceAddresses'
_p='cgdTotalDomainLists'
_o='cgdTotalDomains'
_n='cgdDnsRuleName'
_m='cgdClauseId'
_l='cgdSourceAddressId'
_k='cgdSourceAddressListName'
_j='cgdDomainId'
_i='cgdDomainListName'
_h='cgdAnswerId'
_g='cgdAnswerGroupName'
_f='requests per second'
_e='requests'
_d='responses'
_c='traps per minute'
_b='read-write'
_a='CiscoGslbAnswerAdminState'
_Z='cgdDroppedDnsClauseNotifs'
_Y='cgdDroppedAnsNotifs'
_X='cgdAnswerPrevStatus'
_W='cgdSecondClauseId'
_V='cgdFirstClauseId'
_U='cgdAnswerStatus'
_T='cgdAnswerName'
_S='cgdAnswerAddress'
_R='cgdAnswerAddressType'
_Q='cgdAnswerType'
_P='errors'
_O='TruthValue'
_N='sysName'
_M='SNMPv2-MIB'
_L='InetAddressType'
_K='queries'
_J='Unsigned32'
_I='not-accessible'
_H='StorageType'
_G='number of hits'
_F='SnmpAdminString'
_E='hits per second'
_D='read-create'
_C='read-only'
_B='CISCO-GSLB-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoGslbAnswerAdminState,CiscoGslbAnswerStatus,CiscoGslbAnswerType,CiscoGslbBalanceMethod=mibBuilder.importSymbols('CISCO-GSLB-TC-MIB',_a,'CiscoGslbAnswerStatus','CiscoGslbAnswerType','CiscoGslbBalanceMethod')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressDNS,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressDNS','InetAddressPrefixLength',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_M,_N)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention',_O)
ciscoGslbDnsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,595))
if mibBuilder.loadTexts:ciscoGslbDnsMIB.setRevisions(('2007-04-09 00:00','2006-11-28 00:00'))
_CiscoGslbDnsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoGslbDnsMIBNotifs=_CiscoGslbDnsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,595,0))
_CiscoGslbDnsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGslbDnsMIBObjects=_CiscoGslbDnsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,595,1))
_CgdNotifControl_ObjectIdentity=ObjectIdentity
cgdNotifControl=_CgdNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,1))
class _CgdDnsClauseNotifEnable_Type(TruthValue):defaultValue=2
_CgdDnsClauseNotifEnable_Type.__name__=_O
_CgdDnsClauseNotifEnable_Object=MibScalar
cgdDnsClauseNotifEnable=_CgdDnsClauseNotifEnable_Object((1,3,6,1,4,1,9,9,595,1,1,1),_CgdDnsClauseNotifEnable_Type())
cgdDnsClauseNotifEnable.setMaxAccess(_b)
if mibBuilder.loadTexts:cgdDnsClauseNotifEnable.setStatus(_A)
class _CgdDnsAnswerNotifEnable_Type(TruthValue):defaultValue=2
_CgdDnsAnswerNotifEnable_Type.__name__=_O
_CgdDnsAnswerNotifEnable_Object=MibScalar
cgdDnsAnswerNotifEnable=_CgdDnsAnswerNotifEnable_Object((1,3,6,1,4,1,9,9,595,1,1,2),_CgdDnsAnswerNotifEnable_Type())
cgdDnsAnswerNotifEnable.setMaxAccess(_b)
if mibBuilder.loadTexts:cgdDnsAnswerNotifEnable.setStatus(_A)
_CgdNotifObjects_ObjectIdentity=ObjectIdentity
cgdNotifObjects=_CgdNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,2))
_CgdAnswerPrevStatus_Type=CiscoGslbAnswerStatus
_CgdAnswerPrevStatus_Object=MibScalar
cgdAnswerPrevStatus=_CgdAnswerPrevStatus_Object((1,3,6,1,4,1,9,9,595,1,2,1),_CgdAnswerPrevStatus_Type())
cgdAnswerPrevStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cgdAnswerPrevStatus.setStatus(_A)
_CgdGlobal_ObjectIdentity=ObjectIdentity
cgdGlobal=_CgdGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,3))
_CgdTotalDomains_Type=Unsigned32
_CgdTotalDomains_Object=MibScalar
cgdTotalDomains=_CgdTotalDomains_Object((1,3,6,1,4,1,9,9,595,1,3,1),_CgdTotalDomains_Type())
cgdTotalDomains.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalDomains.setStatus(_A)
_CgdTotalDomainLists_Type=Unsigned32
_CgdTotalDomainLists_Object=MibScalar
cgdTotalDomainLists=_CgdTotalDomainLists_Object((1,3,6,1,4,1,9,9,595,1,3,2),_CgdTotalDomainLists_Type())
cgdTotalDomainLists.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalDomainLists.setStatus(_A)
_CgdTotalSourceAddresses_Type=Unsigned32
_CgdTotalSourceAddresses_Object=MibScalar
cgdTotalSourceAddresses=_CgdTotalSourceAddresses_Object((1,3,6,1,4,1,9,9,595,1,3,3),_CgdTotalSourceAddresses_Type())
cgdTotalSourceAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalSourceAddresses.setStatus(_A)
_CgdTotalSourceAddressLists_Type=Unsigned32
_CgdTotalSourceAddressLists_Object=MibScalar
cgdTotalSourceAddressLists=_CgdTotalSourceAddressLists_Object((1,3,6,1,4,1,9,9,595,1,3,4),_CgdTotalSourceAddressLists_Type())
cgdTotalSourceAddressLists.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalSourceAddressLists.setStatus(_A)
_CgdTotalAnswers_Type=Unsigned32
_CgdTotalAnswers_Object=MibScalar
cgdTotalAnswers=_CgdTotalAnswers_Object((1,3,6,1,4,1,9,9,595,1,3,5),_CgdTotalAnswers_Type())
cgdTotalAnswers.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalAnswers.setStatus(_A)
_CgdTotalAnswerGroups_Type=Unsigned32
_CgdTotalAnswerGroups_Object=MibScalar
cgdTotalAnswerGroups=_CgdTotalAnswerGroups_Object((1,3,6,1,4,1,9,9,595,1,3,6),_CgdTotalAnswerGroups_Type())
cgdTotalAnswerGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalAnswerGroups.setStatus(_A)
_CgdTotalRules_Type=Unsigned32
_CgdTotalRules_Object=MibScalar
cgdTotalRules=_CgdTotalRules_Object((1,3,6,1,4,1,9,9,595,1,3,7),_CgdTotalRules_Type())
cgdTotalRules.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdTotalRules.setStatus(_A)
class _CgdAnsTrapRateLimit_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CgdAnsTrapRateLimit_Type.__name__=_J
_CgdAnsTrapRateLimit_Object=MibScalar
cgdAnsTrapRateLimit=_CgdAnsTrapRateLimit_Object((1,3,6,1,4,1,9,9,595,1,3,8),_CgdAnsTrapRateLimit_Type())
cgdAnsTrapRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnsTrapRateLimit.setStatus(_A)
if mibBuilder.loadTexts:cgdAnsTrapRateLimit.setUnits(_c)
class _CgdDnsClauseTrapRateLimit_Type(Unsigned32):defaultValue=25;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CgdDnsClauseTrapRateLimit_Type.__name__=_J
_CgdDnsClauseTrapRateLimit_Object=MibScalar
cgdDnsClauseTrapRateLimit=_CgdDnsClauseTrapRateLimit_Object((1,3,6,1,4,1,9,9,595,1,3,9),_CgdDnsClauseTrapRateLimit_Type())
cgdDnsClauseTrapRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsClauseTrapRateLimit.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsClauseTrapRateLimit.setUnits(_c)
_CgdGlobalStats_ObjectIdentity=ObjectIdentity
cgdGlobalStats=_CgdGlobalStats_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,4))
_CgdDnsRcvdQueries_Type=Counter32
_CgdDnsRcvdQueries_Object=MibScalar
cgdDnsRcvdQueries=_CgdDnsRcvdQueries_Object((1,3,6,1,4,1,9,9,595,1,4,1),_CgdDnsRcvdQueries_Type())
cgdDnsRcvdQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsRcvdQueries.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsRcvdQueries.setUnits(_K)
_CgdDnsRcvdHostAddrQueries_Type=Counter32
_CgdDnsRcvdHostAddrQueries_Object=MibScalar
cgdDnsRcvdHostAddrQueries=_CgdDnsRcvdHostAddrQueries_Object((1,3,6,1,4,1,9,9,595,1,4,2),_CgdDnsRcvdHostAddrQueries_Type())
cgdDnsRcvdHostAddrQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsRcvdHostAddrQueries.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsRcvdHostAddrQueries.setUnits(_K)
_CgdDnsUnmatchedQueries_Type=Counter32
_CgdDnsUnmatchedQueries_Object=MibScalar
cgdDnsUnmatchedQueries=_CgdDnsUnmatchedQueries_Object((1,3,6,1,4,1,9,9,595,1,4,3),_CgdDnsUnmatchedQueries_Type())
cgdDnsUnmatchedQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsUnmatchedQueries.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsUnmatchedQueries.setUnits(_K)
_CgdDnsDroppedQueries_Type=Counter32
_CgdDnsDroppedQueries_Object=MibScalar
cgdDnsDroppedQueries=_CgdDnsDroppedQueries_Object((1,3,6,1,4,1,9,9,595,1,4,4),_CgdDnsDroppedQueries_Type())
cgdDnsDroppedQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsDroppedQueries.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsDroppedQueries.setUnits(_K)
_CgdNSFwdSentQueries_Type=Counter32
_CgdNSFwdSentQueries_Object=MibScalar
cgdNSFwdSentQueries=_CgdNSFwdSentQueries_Object((1,3,6,1,4,1,9,9,595,1,4,5),_CgdNSFwdSentQueries_Type())
cgdNSFwdSentQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdNSFwdSentQueries.setStatus(_A)
if mibBuilder.loadTexts:cgdNSFwdSentQueries.setUnits(_K)
_CgdNSFwdRcvdResps_Type=Counter32
_CgdNSFwdRcvdResps_Object=MibScalar
cgdNSFwdRcvdResps=_CgdNSFwdRcvdResps_Object((1,3,6,1,4,1,9,9,595,1,4,6),_CgdNSFwdRcvdResps_Type())
cgdNSFwdRcvdResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdNSFwdRcvdResps.setStatus(_A)
if mibBuilder.loadTexts:cgdNSFwdRcvdResps.setUnits(_d)
_CgdBoomServSentReqs_Type=Counter32
_CgdBoomServSentReqs_Object=MibScalar
cgdBoomServSentReqs=_CgdBoomServSentReqs_Object((1,3,6,1,4,1,9,9,595,1,4,7),_CgdBoomServSentReqs_Type())
cgdBoomServSentReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdBoomServSentReqs.setStatus(_A)
if mibBuilder.loadTexts:cgdBoomServSentReqs.setUnits(_e)
_CgdProxLkupSentReqs_Type=Counter32
_CgdProxLkupSentReqs_Object=MibScalar
cgdProxLkupSentReqs=_CgdProxLkupSentReqs_Object((1,3,6,1,4,1,9,9,595,1,4,8),_CgdProxLkupSentReqs_Type())
cgdProxLkupSentReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdProxLkupSentReqs.setStatus(_A)
if mibBuilder.loadTexts:cgdProxLkupSentReqs.setUnits(_e)
_CgdProxLkupRcvdResps_Type=Counter32
_CgdProxLkupRcvdResps_Object=MibScalar
cgdProxLkupRcvdResps=_CgdProxLkupRcvdResps_Object((1,3,6,1,4,1,9,9,595,1,4,9),_CgdProxLkupRcvdResps_Type())
cgdProxLkupRcvdResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdProxLkupRcvdResps.setStatus(_A)
if mibBuilder.loadTexts:cgdProxLkupRcvdResps.setUnits(_d)
_CgdDnsQueryRateCurrent_Type=Gauge32
_CgdDnsQueryRateCurrent_Object=MibScalar
cgdDnsQueryRateCurrent=_CgdDnsQueryRateCurrent_Object((1,3,6,1,4,1,9,9,595,1,4,10),_CgdDnsQueryRateCurrent_Type())
cgdDnsQueryRateCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsQueryRateCurrent.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsQueryRateCurrent.setUnits(_f)
_CgdDnsQueryRatePeak_Type=Unsigned32
_CgdDnsQueryRatePeak_Object=MibScalar
cgdDnsQueryRatePeak=_CgdDnsQueryRatePeak_Object((1,3,6,1,4,1,9,9,595,1,4,11),_CgdDnsQueryRatePeak_Type())
cgdDnsQueryRatePeak.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsQueryRatePeak.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsQueryRatePeak.setUnits(_f)
_CgdDnsUdpSrcPortErrs_Type=Counter32
_CgdDnsUdpSrcPortErrs_Object=MibScalar
cgdDnsUdpSrcPortErrs=_CgdDnsUdpSrcPortErrs_Object((1,3,6,1,4,1,9,9,595,1,4,12),_CgdDnsUdpSrcPortErrs_Type())
cgdDnsUdpSrcPortErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsUdpSrcPortErrs.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsUdpSrcPortErrs.setUnits(_P)
_CgdDnsTcpSrcPortErrs_Type=Counter32
_CgdDnsTcpSrcPortErrs_Object=MibScalar
cgdDnsTcpSrcPortErrs=_CgdDnsTcpSrcPortErrs_Object((1,3,6,1,4,1,9,9,595,1,4,13),_CgdDnsTcpSrcPortErrs_Type())
cgdDnsTcpSrcPortErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsTcpSrcPortErrs.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsTcpSrcPortErrs.setUnits(_P)
_CgdDnsPollSockErrs_Type=Counter32
_CgdDnsPollSockErrs_Object=MibScalar
cgdDnsPollSockErrs=_CgdDnsPollSockErrs_Object((1,3,6,1,4,1,9,9,595,1,4,14),_CgdDnsPollSockErrs_Type())
cgdDnsPollSockErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsPollSockErrs.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsPollSockErrs.setUnits(_P)
_CgdDroppedAnsNotifs_Type=Unsigned32
_CgdDroppedAnsNotifs_Object=MibScalar
cgdDroppedAnsNotifs=_CgdDroppedAnsNotifs_Object((1,3,6,1,4,1,9,9,595,1,4,15),_CgdDroppedAnsNotifs_Type())
cgdDroppedAnsNotifs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDroppedAnsNotifs.setStatus(_A)
if mibBuilder.loadTexts:cgdDroppedAnsNotifs.setUnits('traps')
_CgdDroppedDnsClauseNotifs_Type=Unsigned32
_CgdDroppedDnsClauseNotifs_Object=MibScalar
cgdDroppedDnsClauseNotifs=_CgdDroppedDnsClauseNotifs_Object((1,3,6,1,4,1,9,9,595,1,4,16),_CgdDroppedDnsClauseNotifs_Type())
cgdDroppedDnsClauseNotifs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDroppedDnsClauseNotifs.setStatus(_A)
if mibBuilder.loadTexts:cgdDroppedDnsClauseNotifs.setUnits('traps')
_CgdAnswer_ObjectIdentity=ObjectIdentity
cgdAnswer=_CgdAnswer_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,5))
_CgdAnswerGroupTable_Object=MibTable
cgdAnswerGroupTable=_CgdAnswerGroupTable_Object((1,3,6,1,4,1,9,9,595,1,5,1))
if mibBuilder.loadTexts:cgdAnswerGroupTable.setStatus(_A)
_CgdAnswerGroupEntry_Object=MibTableRow
cgdAnswerGroupEntry=_CgdAnswerGroupEntry_Object((1,3,6,1,4,1,9,9,595,1,5,1,1))
cgdAnswerGroupEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:cgdAnswerGroupEntry.setStatus(_A)
class _CgdAnswerGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdAnswerGroupName_Type.__name__=_F
_CgdAnswerGroupName_Object=MibTableColumn
cgdAnswerGroupName=_CgdAnswerGroupName_Object((1,3,6,1,4,1,9,9,595,1,5,1,1,1),_CgdAnswerGroupName_Type())
cgdAnswerGroupName.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdAnswerGroupName.setStatus(_A)
_CgdAnswerGroupType_Type=CiscoGslbAnswerType
_CgdAnswerGroupType_Object=MibTableColumn
cgdAnswerGroupType=_CgdAnswerGroupType_Object((1,3,6,1,4,1,9,9,595,1,5,1,1,2),_CgdAnswerGroupType_Type())
cgdAnswerGroupType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerGroupType.setStatus(_A)
_CgdAnswerGroupHits_Type=Counter32
_CgdAnswerGroupHits_Object=MibTableColumn
cgdAnswerGroupHits=_CgdAnswerGroupHits_Object((1,3,6,1,4,1,9,9,595,1,5,1,1,3),_CgdAnswerGroupHits_Type())
cgdAnswerGroupHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerGroupHits.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerGroupHits.setUnits(_G)
class _CgdAnswerGroupStorageType_Type(StorageType):defaultValue=3
_CgdAnswerGroupStorageType_Type.__name__=_H
_CgdAnswerGroupStorageType_Object=MibTableColumn
cgdAnswerGroupStorageType=_CgdAnswerGroupStorageType_Object((1,3,6,1,4,1,9,9,595,1,5,1,1,4),_CgdAnswerGroupStorageType_Type())
cgdAnswerGroupStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerGroupStorageType.setStatus(_A)
_CgdAnswerGroupRowStatus_Type=RowStatus
_CgdAnswerGroupRowStatus_Object=MibTableColumn
cgdAnswerGroupRowStatus=_CgdAnswerGroupRowStatus_Object((1,3,6,1,4,1,9,9,595,1,5,1,1,5),_CgdAnswerGroupRowStatus_Type())
cgdAnswerGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerGroupRowStatus.setStatus(_A)
_CgdAnswerTable_Object=MibTable
cgdAnswerTable=_CgdAnswerTable_Object((1,3,6,1,4,1,9,9,595,1,5,2))
if mibBuilder.loadTexts:cgdAnswerTable.setStatus(_A)
_CgdAnswerEntry_Object=MibTableRow
cgdAnswerEntry=_CgdAnswerEntry_Object((1,3,6,1,4,1,9,9,595,1,5,2,1))
cgdAnswerEntry.setIndexNames((0,_B,_h))
if mibBuilder.loadTexts:cgdAnswerEntry.setStatus(_A)
class _CgdAnswerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgdAnswerId_Type.__name__=_J
_CgdAnswerId_Object=MibTableColumn
cgdAnswerId=_CgdAnswerId_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,1),_CgdAnswerId_Type())
cgdAnswerId.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdAnswerId.setStatus(_A)
_CgdAnswerType_Type=CiscoGslbAnswerType
_CgdAnswerType_Object=MibTableColumn
cgdAnswerType=_CgdAnswerType_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,2),_CgdAnswerType_Type())
cgdAnswerType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerType.setStatus(_A)
class _CgdAnswerAddressType_Type(InetAddressType):defaultValue=1
_CgdAnswerAddressType_Type.__name__=_L
_CgdAnswerAddressType_Object=MibTableColumn
cgdAnswerAddressType=_CgdAnswerAddressType_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,3),_CgdAnswerAddressType_Type())
cgdAnswerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerAddressType.setStatus(_A)
_CgdAnswerAddress_Type=InetAddress
_CgdAnswerAddress_Object=MibTableColumn
cgdAnswerAddress=_CgdAnswerAddress_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,4),_CgdAnswerAddress_Type())
cgdAnswerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerAddress.setStatus(_A)
class _CgdAnswerName_Type(SnmpAdminString):defaultValue=OctetString('')
_CgdAnswerName_Type.__name__=_F
_CgdAnswerName_Object=MibTableColumn
cgdAnswerName=_CgdAnswerName_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,5),_CgdAnswerName_Type())
cgdAnswerName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerName.setStatus(_A)
class _CgdAnswerGrpName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CgdAnswerGrpName_Type.__name__=_F
_CgdAnswerGrpName_Object=MibTableColumn
cgdAnswerGrpName=_CgdAnswerGrpName_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,6),_CgdAnswerGrpName_Type())
cgdAnswerGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerGrpName.setStatus(_A)
class _CgdAnswerAdminState_Type(CiscoGslbAnswerAdminState):defaultValue=2
_CgdAnswerAdminState_Type.__name__=_a
_CgdAnswerAdminState_Object=MibTableColumn
cgdAnswerAdminState=_CgdAnswerAdminState_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,7),_CgdAnswerAdminState_Type())
cgdAnswerAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerAdminState.setStatus(_A)
_CgdAnswerStatus_Type=CiscoGslbAnswerStatus
_CgdAnswerStatus_Object=MibTableColumn
cgdAnswerStatus=_CgdAnswerStatus_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,8),_CgdAnswerStatus_Type())
cgdAnswerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerStatus.setStatus(_A)
_CgdAnswerHits_Type=Counter32
_CgdAnswerHits_Object=MibTableColumn
cgdAnswerHits=_CgdAnswerHits_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,9),_CgdAnswerHits_Type())
cgdAnswerHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerHits.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerHits.setUnits(_G)
_CgdAnswerRate1Min_Type=Gauge32
_CgdAnswerRate1Min_Object=MibTableColumn
cgdAnswerRate1Min=_CgdAnswerRate1Min_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,10),_CgdAnswerRate1Min_Type())
cgdAnswerRate1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerRate1Min.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerRate1Min.setUnits(_E)
_CgdAnswerRate5Min_Type=Gauge32
_CgdAnswerRate5Min_Object=MibTableColumn
cgdAnswerRate5Min=_CgdAnswerRate5Min_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,11),_CgdAnswerRate5Min_Type())
cgdAnswerRate5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerRate5Min.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerRate5Min.setUnits(_E)
_CgdAnswerRate30Min_Type=Gauge32
_CgdAnswerRate30Min_Object=MibTableColumn
cgdAnswerRate30Min=_CgdAnswerRate30Min_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,12),_CgdAnswerRate30Min_Type())
cgdAnswerRate30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerRate30Min.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerRate30Min.setUnits(_E)
_CgdAnswerRate4Hr_Type=Gauge32
_CgdAnswerRate4Hr_Object=MibTableColumn
cgdAnswerRate4Hr=_CgdAnswerRate4Hr_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,13),_CgdAnswerRate4Hr_Type())
cgdAnswerRate4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdAnswerRate4Hr.setStatus(_A)
if mibBuilder.loadTexts:cgdAnswerRate4Hr.setUnits(_E)
class _CgdAnswerStorageType_Type(StorageType):defaultValue=3
_CgdAnswerStorageType_Type.__name__=_H
_CgdAnswerStorageType_Object=MibTableColumn
cgdAnswerStorageType=_CgdAnswerStorageType_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,14),_CgdAnswerStorageType_Type())
cgdAnswerStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerStorageType.setStatus(_A)
_CgdAnswerRowStatus_Type=RowStatus
_CgdAnswerRowStatus_Object=MibTableColumn
cgdAnswerRowStatus=_CgdAnswerRowStatus_Object((1,3,6,1,4,1,9,9,595,1,5,2,1,15),_CgdAnswerRowStatus_Type())
cgdAnswerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdAnswerRowStatus.setStatus(_A)
_CgdDomain_ObjectIdentity=ObjectIdentity
cgdDomain=_CgdDomain_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,6))
_CgdDomainListTable_Object=MibTable
cgdDomainListTable=_CgdDomainListTable_Object((1,3,6,1,4,1,9,9,595,1,6,1))
if mibBuilder.loadTexts:cgdDomainListTable.setStatus(_A)
_CgdDomainListEntry_Object=MibTableRow
cgdDomainListEntry=_CgdDomainListEntry_Object((1,3,6,1,4,1,9,9,595,1,6,1,1))
cgdDomainListEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:cgdDomainListEntry.setStatus(_A)
class _CgdDomainListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdDomainListName_Type.__name__=_F
_CgdDomainListName_Object=MibTableColumn
cgdDomainListName=_CgdDomainListName_Object((1,3,6,1,4,1,9,9,595,1,6,1,1,1),_CgdDomainListName_Type())
cgdDomainListName.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdDomainListName.setStatus(_A)
_CgdDomainListHits_Type=Counter32
_CgdDomainListHits_Object=MibTableColumn
cgdDomainListHits=_CgdDomainListHits_Object((1,3,6,1,4,1,9,9,595,1,6,1,1,2),_CgdDomainListHits_Type())
cgdDomainListHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainListHits.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainListHits.setUnits(_G)
class _CgdDomainListStorageType_Type(StorageType):defaultValue=3
_CgdDomainListStorageType_Type.__name__=_H
_CgdDomainListStorageType_Object=MibTableColumn
cgdDomainListStorageType=_CgdDomainListStorageType_Object((1,3,6,1,4,1,9,9,595,1,6,1,1,3),_CgdDomainListStorageType_Type())
cgdDomainListStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainListStorageType.setStatus(_A)
_CgdDomainListRowStatus_Type=RowStatus
_CgdDomainListRowStatus_Object=MibTableColumn
cgdDomainListRowStatus=_CgdDomainListRowStatus_Object((1,3,6,1,4,1,9,9,595,1,6,1,1,4),_CgdDomainListRowStatus_Type())
cgdDomainListRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainListRowStatus.setStatus(_A)
_CgdDomainTable_Object=MibTable
cgdDomainTable=_CgdDomainTable_Object((1,3,6,1,4,1,9,9,595,1,6,2))
if mibBuilder.loadTexts:cgdDomainTable.setStatus(_A)
_CgdDomainEntry_Object=MibTableRow
cgdDomainEntry=_CgdDomainEntry_Object((1,3,6,1,4,1,9,9,595,1,6,2,1))
cgdDomainEntry.setIndexNames((0,_B,_j))
if mibBuilder.loadTexts:cgdDomainEntry.setStatus(_A)
class _CgdDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgdDomainId_Type.__name__=_J
_CgdDomainId_Object=MibTableColumn
cgdDomainId=_CgdDomainId_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,1),_CgdDomainId_Type())
cgdDomainId.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdDomainId.setStatus(_A)
_CgdDomainName_Type=InetAddressDNS
_CgdDomainName_Object=MibTableColumn
cgdDomainName=_CgdDomainName_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,2),_CgdDomainName_Type())
cgdDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainName.setStatus(_A)
class _CgdDomainList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdDomainList_Type.__name__=_F
_CgdDomainList_Object=MibTableColumn
cgdDomainList=_CgdDomainList_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,3),_CgdDomainList_Type())
cgdDomainList.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainList.setStatus(_A)
_CgdDomainHits_Type=Counter32
_CgdDomainHits_Object=MibTableColumn
cgdDomainHits=_CgdDomainHits_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,4),_CgdDomainHits_Type())
cgdDomainHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainHits.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainHits.setUnits(_G)
_CgdDomainRate1Min_Type=Gauge32
_CgdDomainRate1Min_Object=MibTableColumn
cgdDomainRate1Min=_CgdDomainRate1Min_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,5),_CgdDomainRate1Min_Type())
cgdDomainRate1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainRate1Min.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainRate1Min.setUnits(_E)
_CgdDomainRate5Min_Type=Gauge32
_CgdDomainRate5Min_Object=MibTableColumn
cgdDomainRate5Min=_CgdDomainRate5Min_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,6),_CgdDomainRate5Min_Type())
cgdDomainRate5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainRate5Min.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainRate5Min.setUnits(_E)
_CgdDomainRate30Min_Type=Gauge32
_CgdDomainRate30Min_Object=MibTableColumn
cgdDomainRate30Min=_CgdDomainRate30Min_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,7),_CgdDomainRate30Min_Type())
cgdDomainRate30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainRate30Min.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainRate30Min.setUnits(_E)
_CgdDomainRate4Hr_Type=Gauge32
_CgdDomainRate4Hr_Object=MibTableColumn
cgdDomainRate4Hr=_CgdDomainRate4Hr_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,8),_CgdDomainRate4Hr_Type())
cgdDomainRate4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDomainRate4Hr.setStatus(_A)
if mibBuilder.loadTexts:cgdDomainRate4Hr.setUnits(_E)
class _CgdDomainStorageType_Type(StorageType):defaultValue=3
_CgdDomainStorageType_Type.__name__=_H
_CgdDomainStorageType_Object=MibTableColumn
cgdDomainStorageType=_CgdDomainStorageType_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,9),_CgdDomainStorageType_Type())
cgdDomainStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainStorageType.setStatus(_A)
_CgdDomainRowStatus_Type=RowStatus
_CgdDomainRowStatus_Object=MibTableColumn
cgdDomainRowStatus=_CgdDomainRowStatus_Object((1,3,6,1,4,1,9,9,595,1,6,2,1,10),_CgdDomainRowStatus_Type())
cgdDomainRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDomainRowStatus.setStatus(_A)
_CgdSourceAdd_ObjectIdentity=ObjectIdentity
cgdSourceAdd=_CgdSourceAdd_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,7))
_CgdSourceAddressListTable_Object=MibTable
cgdSourceAddressListTable=_CgdSourceAddressListTable_Object((1,3,6,1,4,1,9,9,595,1,7,1))
if mibBuilder.loadTexts:cgdSourceAddressListTable.setStatus(_A)
_CgdSourceAddressListEntry_Object=MibTableRow
cgdSourceAddressListEntry=_CgdSourceAddressListEntry_Object((1,3,6,1,4,1,9,9,595,1,7,1,1))
cgdSourceAddressListEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:cgdSourceAddressListEntry.setStatus(_A)
class _CgdSourceAddressListName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdSourceAddressListName_Type.__name__=_F
_CgdSourceAddressListName_Object=MibTableColumn
cgdSourceAddressListName=_CgdSourceAddressListName_Object((1,3,6,1,4,1,9,9,595,1,7,1,1,1),_CgdSourceAddressListName_Type())
cgdSourceAddressListName.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdSourceAddressListName.setStatus(_A)
_CgdSourceAddressListHits_Type=Counter32
_CgdSourceAddressListHits_Object=MibTableColumn
cgdSourceAddressListHits=_CgdSourceAddressListHits_Object((1,3,6,1,4,1,9,9,595,1,7,1,1,2),_CgdSourceAddressListHits_Type())
cgdSourceAddressListHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressListHits.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressListHits.setUnits(_G)
class _CgdSourceAddressListStorageType_Type(StorageType):defaultValue=3
_CgdSourceAddressListStorageType_Type.__name__=_H
_CgdSourceAddressListStorageType_Object=MibTableColumn
cgdSourceAddressListStorageType=_CgdSourceAddressListStorageType_Object((1,3,6,1,4,1,9,9,595,1,7,1,1,3),_CgdSourceAddressListStorageType_Type())
cgdSourceAddressListStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddressListStorageType.setStatus(_A)
_CgdSourceAddressListRowStatus_Type=RowStatus
_CgdSourceAddressListRowStatus_Object=MibTableColumn
cgdSourceAddressListRowStatus=_CgdSourceAddressListRowStatus_Object((1,3,6,1,4,1,9,9,595,1,7,1,1,4),_CgdSourceAddressListRowStatus_Type())
cgdSourceAddressListRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddressListRowStatus.setStatus(_A)
_CgdSourceAddressTable_Object=MibTable
cgdSourceAddressTable=_CgdSourceAddressTable_Object((1,3,6,1,4,1,9,9,595,1,7,2))
if mibBuilder.loadTexts:cgdSourceAddressTable.setStatus(_A)
_CgdSourceAddressEntry_Object=MibTableRow
cgdSourceAddressEntry=_CgdSourceAddressEntry_Object((1,3,6,1,4,1,9,9,595,1,7,2,1))
cgdSourceAddressEntry.setIndexNames((0,_B,_l))
if mibBuilder.loadTexts:cgdSourceAddressEntry.setStatus(_A)
class _CgdSourceAddressId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgdSourceAddressId_Type.__name__=_J
_CgdSourceAddressId_Object=MibTableColumn
cgdSourceAddressId=_CgdSourceAddressId_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,1),_CgdSourceAddressId_Type())
cgdSourceAddressId.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdSourceAddressId.setStatus(_A)
class _CgdSourceAddressAddressType_Type(InetAddressType):defaultValue=1
_CgdSourceAddressAddressType_Type.__name__=_L
_CgdSourceAddressAddressType_Object=MibTableColumn
cgdSourceAddressAddressType=_CgdSourceAddressAddressType_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,2),_CgdSourceAddressAddressType_Type())
cgdSourceAddressAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressAddressType.setStatus(_A)
_CgdSourceAddressAddress_Type=InetAddress
_CgdSourceAddressAddress_Object=MibTableColumn
cgdSourceAddressAddress=_CgdSourceAddressAddress_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,3),_CgdSourceAddressAddress_Type())
cgdSourceAddressAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressAddress.setStatus(_A)
_CgdSourceAddressPrefixLength_Type=InetAddressPrefixLength
_CgdSourceAddressPrefixLength_Object=MibTableColumn
cgdSourceAddressPrefixLength=_CgdSourceAddressPrefixLength_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,4),_CgdSourceAddressPrefixLength_Type())
cgdSourceAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressPrefixLength.setStatus(_A)
class _CgdSourceAddressList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdSourceAddressList_Type.__name__=_F
_CgdSourceAddressList_Object=MibTableColumn
cgdSourceAddressList=_CgdSourceAddressList_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,5),_CgdSourceAddressList_Type())
cgdSourceAddressList.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddressList.setStatus(_A)
_CgdSourceAddressHits_Type=Counter32
_CgdSourceAddressHits_Object=MibTableColumn
cgdSourceAddressHits=_CgdSourceAddressHits_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,6),_CgdSourceAddressHits_Type())
cgdSourceAddressHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressHits.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressHits.setUnits(_G)
_CgdSourceAddressRate1Min_Type=Gauge32
_CgdSourceAddressRate1Min_Object=MibTableColumn
cgdSourceAddressRate1Min=_CgdSourceAddressRate1Min_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,7),_CgdSourceAddressRate1Min_Type())
cgdSourceAddressRate1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressRate1Min.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressRate1Min.setUnits(_E)
_CgdSourceAddressRate5Min_Type=Gauge32
_CgdSourceAddressRate5Min_Object=MibTableColumn
cgdSourceAddressRate5Min=_CgdSourceAddressRate5Min_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,8),_CgdSourceAddressRate5Min_Type())
cgdSourceAddressRate5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressRate5Min.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressRate5Min.setUnits(_E)
_CgdSourceAddressRate30Min_Type=Gauge32
_CgdSourceAddressRate30Min_Object=MibTableColumn
cgdSourceAddressRate30Min=_CgdSourceAddressRate30Min_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,9),_CgdSourceAddressRate30Min_Type())
cgdSourceAddressRate30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressRate30Min.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressRate30Min.setUnits(_E)
_CgdSourceAddressRate4Hr_Type=Gauge32
_CgdSourceAddressRate4Hr_Object=MibTableColumn
cgdSourceAddressRate4Hr=_CgdSourceAddressRate4Hr_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,10),_CgdSourceAddressRate4Hr_Type())
cgdSourceAddressRate4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdSourceAddressRate4Hr.setStatus(_A)
if mibBuilder.loadTexts:cgdSourceAddressRate4Hr.setUnits(_E)
class _CgdSourceAddressStorageType_Type(StorageType):defaultValue=3
_CgdSourceAddressStorageType_Type.__name__=_H
_CgdSourceAddressStorageType_Object=MibTableColumn
cgdSourceAddressStorageType=_CgdSourceAddressStorageType_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,11),_CgdSourceAddressStorageType_Type())
cgdSourceAddressStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddressStorageType.setStatus(_A)
_CgdSourceAddressRowStatus_Type=RowStatus
_CgdSourceAddressRowStatus_Object=MibTableColumn
cgdSourceAddressRowStatus=_CgdSourceAddressRowStatus_Object((1,3,6,1,4,1,9,9,595,1,7,2,1,12),_CgdSourceAddressRowStatus_Type())
cgdSourceAddressRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddressRowStatus.setStatus(_A)
_CgdDnsRule_ObjectIdentity=ObjectIdentity
cgdDnsRule=_CgdDnsRule_ObjectIdentity((1,3,6,1,4,1,9,9,595,1,8))
_CgdClauseTable_Object=MibTable
cgdClauseTable=_CgdClauseTable_Object((1,3,6,1,4,1,9,9,595,1,8,1))
if mibBuilder.loadTexts:cgdClauseTable.setStatus(_A)
_CgdClauseEntry_Object=MibTableRow
cgdClauseEntry=_CgdClauseEntry_Object((1,3,6,1,4,1,9,9,595,1,8,1,1))
cgdClauseEntry.setIndexNames((0,_B,_m))
if mibBuilder.loadTexts:cgdClauseEntry.setStatus(_A)
class _CgdClauseId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgdClauseId_Type.__name__=_J
_CgdClauseId_Object=MibTableColumn
cgdClauseId=_CgdClauseId_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,1),_CgdClauseId_Type())
cgdClauseId.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdClauseId.setStatus(_A)
_CgdClauseAnsGrpName_Type=SnmpAdminString
_CgdClauseAnsGrpName_Object=MibTableColumn
cgdClauseAnsGrpName=_CgdClauseAnsGrpName_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,2),_CgdClauseAnsGrpName_Type())
cgdClauseAnsGrpName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdClauseAnsGrpName.setStatus(_A)
_CgdClauseBalanceMethod_Type=CiscoGslbBalanceMethod
_CgdClauseBalanceMethod_Object=MibTableColumn
cgdClauseBalanceMethod=_CgdClauseBalanceMethod_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,3),_CgdClauseBalanceMethod_Type())
cgdClauseBalanceMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdClauseBalanceMethod.setStatus(_A)
_CgdClauseHits_Type=Counter32
_CgdClauseHits_Object=MibTableColumn
cgdClauseHits=_CgdClauseHits_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,4),_CgdClauseHits_Type())
cgdClauseHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdClauseHits.setStatus(_A)
if mibBuilder.loadTexts:cgdClauseHits.setUnits(_G)
_CgdClauseStorageType_Type=StorageType
_CgdClauseStorageType_Object=MibTableColumn
cgdClauseStorageType=_CgdClauseStorageType_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,5),_CgdClauseStorageType_Type())
cgdClauseStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdClauseStorageType.setStatus(_A)
_CgdClauseRowStatus_Type=RowStatus
_CgdClauseRowStatus_Object=MibTableColumn
cgdClauseRowStatus=_CgdClauseRowStatus_Object((1,3,6,1,4,1,9,9,595,1,8,1,1,6),_CgdClauseRowStatus_Type())
cgdClauseRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdClauseRowStatus.setStatus(_A)
_CgdDnsRuleTable_Object=MibTable
cgdDnsRuleTable=_CgdDnsRuleTable_Object((1,3,6,1,4,1,9,9,595,1,8,2))
if mibBuilder.loadTexts:cgdDnsRuleTable.setStatus(_A)
_CgdDnsRuleEntry_Object=MibTableRow
cgdDnsRuleEntry=_CgdDnsRuleEntry_Object((1,3,6,1,4,1,9,9,595,1,8,2,1))
cgdDnsRuleEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:cgdDnsRuleEntry.setStatus(_A)
class _CgdDnsRuleName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgdDnsRuleName_Type.__name__=_F
_CgdDnsRuleName_Object=MibTableColumn
cgdDnsRuleName=_CgdDnsRuleName_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,1),_CgdDnsRuleName_Type())
cgdDnsRuleName.setMaxAccess(_I)
if mibBuilder.loadTexts:cgdDnsRuleName.setStatus(_A)
_CgdFirstClauseId_Type=Unsigned32
_CgdFirstClauseId_Object=MibTableColumn
cgdFirstClauseId=_CgdFirstClauseId_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,2),_CgdFirstClauseId_Type())
cgdFirstClauseId.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdFirstClauseId.setStatus(_A)
_CgdSecondClauseId_Type=Unsigned32
_CgdSecondClauseId_Object=MibTableColumn
cgdSecondClauseId=_CgdSecondClauseId_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,3),_CgdSecondClauseId_Type())
cgdSecondClauseId.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSecondClauseId.setStatus(_A)
_CgdThirdClauseId_Type=Unsigned32
_CgdThirdClauseId_Object=MibTableColumn
cgdThirdClauseId=_CgdThirdClauseId_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,4),_CgdThirdClauseId_Type())
cgdThirdClauseId.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdThirdClauseId.setStatus(_A)
_CgdSourceAddList_Type=SnmpAdminString
_CgdSourceAddList_Object=MibTableColumn
cgdSourceAddList=_CgdSourceAddList_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,5),_CgdSourceAddList_Type())
cgdSourceAddList.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdSourceAddList.setStatus(_A)
_CgdDNSRuleDomainList_Type=SnmpAdminString
_CgdDNSRuleDomainList_Object=MibTableColumn
cgdDNSRuleDomainList=_CgdDNSRuleDomainList_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,6),_CgdDNSRuleDomainList_Type())
cgdDNSRuleDomainList.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDNSRuleDomainList.setStatus(_A)
_CgdDnsRuleHits_Type=Counter32
_CgdDnsRuleHits_Object=MibTableColumn
cgdDnsRuleHits=_CgdDnsRuleHits_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,7),_CgdDnsRuleHits_Type())
cgdDnsRuleHits.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsRuleHits.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsRuleHits.setUnits(_G)
_CgdDnsRuleSuccesses_Type=Counter32
_CgdDnsRuleSuccesses_Object=MibTableColumn
cgdDnsRuleSuccesses=_CgdDnsRuleSuccesses_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,8),_CgdDnsRuleSuccesses_Type())
cgdDnsRuleSuccesses.setMaxAccess(_C)
if mibBuilder.loadTexts:cgdDnsRuleSuccesses.setStatus(_A)
if mibBuilder.loadTexts:cgdDnsRuleSuccesses.setUnits(_G)
class _CgdDnsRuleStorageType_Type(StorageType):defaultValue=3
_CgdDnsRuleStorageType_Type.__name__=_H
_CgdDnsRuleStorageType_Object=MibTableColumn
cgdDnsRuleStorageType=_CgdDnsRuleStorageType_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,9),_CgdDnsRuleStorageType_Type())
cgdDnsRuleStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDnsRuleStorageType.setStatus(_A)
_CgdDnsRuleRowStatus_Type=RowStatus
_CgdDnsRuleRowStatus_Object=MibTableColumn
cgdDnsRuleRowStatus=_CgdDnsRuleRowStatus_Object((1,3,6,1,4,1,9,9,595,1,8,2,1,10),_CgdDnsRuleRowStatus_Type())
cgdDnsRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgdDnsRuleRowStatus.setStatus(_A)
_CiscoGslbDnsMIBConform_ObjectIdentity=ObjectIdentity
ciscoGslbDnsMIBConform=_CiscoGslbDnsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,595,2))
_CiscoGslbDnsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGslbDnsMIBCompliances=_CiscoGslbDnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,595,2,1))
_CiscoGslbDnsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGslbDnsMIBGroups=_CiscoGslbDnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,595,2,2))
ciscoGslbDnsGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,1))
ciscoGslbDnsGlobalGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:ciscoGslbDnsGlobalGroup.setStatus(_A)
ciscoGslbDnsGlobalStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,2))
ciscoGslbDnsGlobalStatsGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:ciscoGslbDnsGlobalStatsGroup.setStatus(_A)
ciscoGslbDnsAnswerGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,3))
ciscoGslbDnsAnswerGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_AD),(_B,_AE),(_B,_U),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoGslbDnsAnswerGroup.setStatus(_A)
ciscoGslbDnsDomainGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,4))
ciscoGslbDnsDomainGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:ciscoGslbDnsDomainGroup.setStatus(_A)
ciscoGslbDnsSourceAddGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,5))
ciscoGslbDnsSourceAddGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:ciscoGslbDnsSourceAddGroup.setStatus(_A)
ciscoGslbDnsRuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,6))
ciscoGslbDnsRuleGroup.setObjects(*((_B,_V),(_B,_W),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:ciscoGslbDnsRuleGroup.setStatus(_A)
ciscoGslbDnsNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,7))
ciscoGslbDnsNotifControlGroup.setObjects(*((_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:ciscoGslbDnsNotifControlGroup.setStatus(_A)
ciscoGslbDnsNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,8))
ciscoGslbDnsNotifObjectsGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:ciscoGslbDnsNotifObjectsGroup.setStatus(_A)
ciscoGslbDnsGlobalRateLimitGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,10))
ciscoGslbDnsGlobalRateLimitGroup.setObjects(*((_B,_A_),(_B,_B0)))
if mibBuilder.loadTexts:ciscoGslbDnsGlobalRateLimitGroup.setStatus(_A)
ciscoGslbDnsGlobalNotifStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,595,2,2,11))
ciscoGslbDnsGlobalNotifStatsGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoGslbDnsGlobalNotifStatsGroup.setStatus(_A)
ciscoGslbDnsEventClause=NotificationType((1,3,6,1,4,1,9,9,595,0,1))
ciscoGslbDnsEventClause.setObjects(*((_M,_N),(_B,_V),(_B,_W),(_B,_Z)))
if mibBuilder.loadTexts:ciscoGslbDnsEventClause.setStatus(_A)
ciscoGslbAnswerEventStatusChange=NotificationType((1,3,6,1,4,1,9,9,595,0,2))
ciscoGslbAnswerEventStatusChange.setObjects(*((_M,_N),(_B,_T),(_B,_Q),(_B,_R),(_B,_S),(_B,_U),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ciscoGslbAnswerEventStatusChange.setStatus(_A)
ciscoGslbDnsNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,595,2,2,9))
ciscoGslbDnsNotifGroup.setObjects(*((_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:ciscoGslbDnsNotifGroup.setStatus(_A)
ciscoGslbDnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,595,2,1,1))
ciscoGslbDnsMIBCompliance.setObjects(*((_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD)))
if mibBuilder.loadTexts:ciscoGslbDnsMIBCompliance.setStatus('deprecated')
mibBuilder.exportSymbols(_B,**{'ciscoGslbDnsMIB':ciscoGslbDnsMIB,'ciscoGslbDnsMIBNotifs':ciscoGslbDnsMIBNotifs,_B1:ciscoGslbDnsEventClause,_B2:ciscoGslbAnswerEventStatusChange,'ciscoGslbDnsMIBObjects':ciscoGslbDnsMIBObjects,'cgdNotifControl':cgdNotifControl,_Ay:cgdDnsClauseNotifEnable,_Az:cgdDnsAnswerNotifEnable,'cgdNotifObjects':cgdNotifObjects,_X:cgdAnswerPrevStatus,'cgdGlobal':cgdGlobal,_o:cgdTotalDomains,_p:cgdTotalDomainLists,_q:cgdTotalSourceAddresses,_r:cgdTotalSourceAddressLists,_s:cgdTotalAnswers,_t:cgdTotalAnswerGroups,_u:cgdTotalRules,_A_:cgdAnsTrapRateLimit,_B0:cgdDnsClauseTrapRateLimit,'cgdGlobalStats':cgdGlobalStats,_v:cgdDnsRcvdQueries,_w:cgdDnsRcvdHostAddrQueries,_x:cgdDnsUnmatchedQueries,_y:cgdDnsDroppedQueries,_z:cgdNSFwdSentQueries,_A0:cgdNSFwdRcvdResps,_A1:cgdBoomServSentReqs,_A2:cgdProxLkupSentReqs,_A3:cgdProxLkupRcvdResps,_A4:cgdDnsQueryRateCurrent,_A5:cgdDnsQueryRatePeak,_A6:cgdDnsUdpSrcPortErrs,_A7:cgdDnsTcpSrcPortErrs,_A8:cgdDnsPollSockErrs,_Y:cgdDroppedAnsNotifs,_Z:cgdDroppedDnsClauseNotifs,'cgdAnswer':cgdAnswer,'cgdAnswerGroupTable':cgdAnswerGroupTable,'cgdAnswerGroupEntry':cgdAnswerGroupEntry,_g:cgdAnswerGroupName,_A9:cgdAnswerGroupType,_AA:cgdAnswerGroupHits,_AB:cgdAnswerGroupStorageType,_AC:cgdAnswerGroupRowStatus,'cgdAnswerTable':cgdAnswerTable,'cgdAnswerEntry':cgdAnswerEntry,_h:cgdAnswerId,_Q:cgdAnswerType,_R:cgdAnswerAddressType,_S:cgdAnswerAddress,_T:cgdAnswerName,_AD:cgdAnswerGrpName,_AE:cgdAnswerAdminState,_U:cgdAnswerStatus,_AF:cgdAnswerHits,_AG:cgdAnswerRate1Min,_AH:cgdAnswerRate5Min,_AI:cgdAnswerRate30Min,_AJ:cgdAnswerRate4Hr,_AK:cgdAnswerStorageType,_AL:cgdAnswerRowStatus,'cgdDomain':cgdDomain,'cgdDomainListTable':cgdDomainListTable,'cgdDomainListEntry':cgdDomainListEntry,_i:cgdDomainListName,_AM:cgdDomainListHits,_AN:cgdDomainListStorageType,_AO:cgdDomainListRowStatus,'cgdDomainTable':cgdDomainTable,'cgdDomainEntry':cgdDomainEntry,_j:cgdDomainId,_AP:cgdDomainName,_AQ:cgdDomainList,_AR:cgdDomainHits,_AS:cgdDomainRate1Min,_AT:cgdDomainRate5Min,_AU:cgdDomainRate30Min,_AV:cgdDomainRate4Hr,_AW:cgdDomainStorageType,_AX:cgdDomainRowStatus,'cgdSourceAdd':cgdSourceAdd,'cgdSourceAddressListTable':cgdSourceAddressListTable,'cgdSourceAddressListEntry':cgdSourceAddressListEntry,_k:cgdSourceAddressListName,_AY:cgdSourceAddressListHits,_AZ:cgdSourceAddressListStorageType,_Aa:cgdSourceAddressListRowStatus,'cgdSourceAddressTable':cgdSourceAddressTable,'cgdSourceAddressEntry':cgdSourceAddressEntry,_l:cgdSourceAddressId,_Ab:cgdSourceAddressAddressType,_Ac:cgdSourceAddressAddress,_Ad:cgdSourceAddressPrefixLength,_Ae:cgdSourceAddressList,_Af:cgdSourceAddressHits,_Ag:cgdSourceAddressRate1Min,_Ah:cgdSourceAddressRate5Min,_Ai:cgdSourceAddressRate30Min,_Aj:cgdSourceAddressRate4Hr,_Ak:cgdSourceAddressStorageType,_Al:cgdSourceAddressRowStatus,'cgdDnsRule':cgdDnsRule,'cgdClauseTable':cgdClauseTable,'cgdClauseEntry':cgdClauseEntry,_m:cgdClauseId,_At:cgdClauseAnsGrpName,_Au:cgdClauseBalanceMethod,_Av:cgdClauseHits,_Aw:cgdClauseStorageType,_Ax:cgdClauseRowStatus,'cgdDnsRuleTable':cgdDnsRuleTable,'cgdDnsRuleEntry':cgdDnsRuleEntry,_n:cgdDnsRuleName,_V:cgdFirstClauseId,_W:cgdSecondClauseId,_Am:cgdThirdClauseId,_An:cgdSourceAddList,_Ao:cgdDNSRuleDomainList,_Ap:cgdDnsRuleHits,_Aq:cgdDnsRuleSuccesses,_Ar:cgdDnsRuleStorageType,_As:cgdDnsRuleRowStatus,'ciscoGslbDnsMIBConform':ciscoGslbDnsMIBConform,'ciscoGslbDnsMIBCompliances':ciscoGslbDnsMIBCompliances,'ciscoGslbDnsMIBCompliance':ciscoGslbDnsMIBCompliance,'ciscoGslbDnsMIBGroups':ciscoGslbDnsMIBGroups,_B3:ciscoGslbDnsGlobalGroup,_B4:ciscoGslbDnsGlobalStatsGroup,_B5:ciscoGslbDnsAnswerGroup,_B6:ciscoGslbDnsDomainGroup,_B7:ciscoGslbDnsSourceAddGroup,_B8:ciscoGslbDnsRuleGroup,_B9:ciscoGslbDnsNotifControlGroup,_BA:ciscoGslbDnsNotifObjectsGroup,_BB:ciscoGslbDnsNotifGroup,_BC:ciscoGslbDnsGlobalRateLimitGroup,_BD:ciscoGslbDnsGlobalNotifStatsGroup})