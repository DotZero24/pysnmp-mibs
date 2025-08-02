_BV='cefHCStatsGroup'
_BU='cefDistributedGroup'
_BT='cefNotificationGroup'
_BS='cefNotifCntlGroup'
_BR='cefInconsistencyDetection'
_BQ='cefPeerFIBStateChange'
_BP='cefPeerStateChange'
_BO='cefResourceFailure'
_BN='cefInconsistencyNotifEnable'
_BM='cefNotifThrottlingInterval'
_BL='cefPeerFIBStateChangeNotifEnable'
_BK='cefPeerStateChangeNotifEnable'
_BJ='cefResourceFailureNotifEnable'
_BI='cefSwitchingHCPunt2Host'
_BH='cefSwitchingHCPunt'
_BG='cefSwitchingHCDrop'
_BF='cefStatsPrefixHCElements'
_BE='cefStatsPrefixHCDeletes'
_BD='cefStatsPrefixHCInserts'
_BC='cefStatsPrefixHCQueries'
_BB='cefAdjHCBytes'
_BA='cefAdjHCPkts'
_B9='cefPrefixExternalNRHCBytes'
_B8='cefPrefixExternalNRHCPkts'
_B7='cefPrefixInternalNRHCBytes'
_B6='cefPrefixInternalNRHCPkts'
_B5='cefPrefixHCBytes'
_B4='cefPrefixHCPkts'
_B3='cefInconsistencyResetStatus'
_B2='cefInconsistencyReset'
_B1='cefInconsistencyReason'
_B0='cefInconsistencyEntity'
_A_='cefInconsistencyCCType'
_Az='cefInconsistencyVrfName'
_Ay='cefInconsistencyPrefixLen'
_Ax='cefInconsistencyPrefixAddr'
_Aw='cefInconsistencyPrefixType'
_Av='cefCCQueriesIterated'
_Au='cefCCQueriesChecked'
_At='cefCCQueriesIgnored'
_As='cefCCQueriesSent'
_Ar='cefCCPeriod'
_Aq='cefCCCount'
_Ap='cefCCEnabled'
_Ao='cefCCGlobalFullScanAction'
_An='cefCCGlobalFullScanStatus'
_Am='cefCCGlobalErrorMsgEnabled'
_Al='cefCCGlobalAutoRepairHoldDown'
_Ak='cefCCGlobalAutoRepairDelay'
_Aj='cefCCGlobalAutoRepairEnabled'
_Ai='cefPeerNumberOfResets'
_Ah='cefCfgDistributionOperState'
_Ag='cefCfgDistributionAdminState'
_Af='cefSwitchingPunt2Host'
_Ae='cefSwitchingPunt'
_Ad='cefSwitchingDrop'
_Ac='cefSwitchingPath'
_Ab='cefStatsPrefixElements'
_Aa='cefStatsPrefixDeletes'
_AZ='cefStatsPrefixInserts'
_AY='cefStatsPrefixQueries'
_AX='cefIntNonrecursiveAccouting'
_AW='cefIntLoadSharing'
_AV='cefIntSwitchingState'
_AU='cefResourceMemoryUsed'
_AT='cefCfgTrafficStatsUpdateRate'
_AS='cefCfgTrafficStatsLoadInterval'
_AR='cefCfgLoadSharingID'
_AQ='cefCfgLoadSharingAlgorithm'
_AP='cefCfgAccountingMap'
_AO='cefCfgOperState'
_AN='cefCfgAdminState'
_AM='cefFESelectionWeight'
_AL='cefFESelectionVrfName'
_AK='cefFESelectionAdjConnId'
_AJ='cefFESelectionAdjNextHopAddr'
_AI='cefFESelectionAdjNextHopAddrType'
_AH='cefFESelectionAdjInterface'
_AG='cefFESelectionAdjLinkType'
_AF='cefFESelectionLabels'
_AE='cefFESelectionSpecial'
_AD='cefAdjBytes'
_AC='cefAdjPkts'
_AB='cefAdjForwardingInfo'
_AA='cefAdjMTU'
_A9='cefAdjFixup'
_A8='cefAdjEncap'
_A7='cefAdjSource'
_A6='cefAdjSummaryRedirect'
_A5='cefAdjSummaryFixup'
_A4='cefAdjSummaryIncomplete'
_A3='cefAdjSummaryComplete'
_A2='cefPathRecurseVrfName'
_A1='cefPathNextHopAddr'
_A0='cefPathInterface'
_z='cefPathType'
_y='cefLMPrefixRowStatus'
_x='cefLMPrefixLen'
_w='cefLMPrefixAddr'
_v='cefLMPrefixState'
_u='cefLMPrefixSpinLock'
_t='cefPrefixExternalNRBytes'
_s='cefPrefixExternalNRPkts'
_r='cefPrefixInternalNRBytes'
_q='cefPrefixInternalNRPkts'
_p='cefPrefixBytes'
_o='cefPrefixPkts'
_n='cefPrefixForwardingInfo'
_m='cefFIBSummaryFwdPrefixes'
_l='cefSwitchingIndex'
_k='cefStatsPrefixLen'
_j='cefInconsistencyRecId'
_i='cefCCType'
_h='cefFESelectionId'
_g='cefFESelectionName'
_f='cefAdjConnId'
_e='cefAdjNextHopAddr'
_d='cefAdjNextHopAddrType'
_c='cefPathId'
_b='cefLMPrefixDestAddr'
_a='cefLMPrefixDestAddrType'
_Z='entLastInconsistencyDetectTime'
_Y='cefPeerFIBOperState'
_X='cefPeerOperState'
_W='cefResourceFailureReason'
_V='entPeerPhysicalIndex'
_U='cefAdjSummaryLinkType'
_T='cefPrefixLen'
_S='cefPrefixAddr'
_R='cefPrefixType'
_Q='SnmpAdminString'
_P='ifIndex'
_O='IF-MIB'
_N='CefCCAction'
_M='seconds'
_L='Unsigned32'
_K='bytes'
_J='cefFIBIpVersion'
_I='Integer32'
_H='packets'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='CISCO-CEF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CefAdjLinkType,CefAdjacencySource,CefAdminStatus,CefCCAction,CefCCStatus,CefCCType,CefFailureReason,CefForwardingElementSpecialType,CefIpVersion,CefMplsLabelList,CefOperStatus,CefPathType,CefPrefixSearchState=mibBuilder.importSymbols('CISCO-CEF-TC','CefAdjLinkType','CefAdjacencySource','CefAdminStatus',_N,'CefCCStatus','CefCCType','CefFailureReason','CefForwardingElementSpecialType','CefIpVersion','CefMplsLabelList','CefOperStatus','CefPathType','CefPrefixSearchState')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_F,'PhysicalIndex',_G)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_O,'InterfaceIndexOrZero',_P)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
MplsVpnId,=mibBuilder.importSymbols('MPLS-VPN-MIB','MplsVpnId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
ciscoCefMIB=ModuleIdentity((1,3,6,1,4,1,9,9,492))
if mibBuilder.loadTexts:ciscoCefMIB.setRevisions(('2006-01-30 00:00',))
_CiscoCefMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCefMIBNotifs=_CiscoCefMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,492,0))
_CiscoCefMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCefMIBObjects=_CiscoCefMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,492,1))
_CefFIB_ObjectIdentity=ObjectIdentity
cefFIB=_CefFIB_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,1))
_CefFIBSummary_ObjectIdentity=ObjectIdentity
cefFIBSummary=_CefFIBSummary_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,1,1))
_CefFIBSummaryTable_Object=MibTable
cefFIBSummaryTable=_CefFIBSummaryTable_Object((1,3,6,1,4,1,9,9,492,1,1,1,1))
if mibBuilder.loadTexts:cefFIBSummaryTable.setStatus(_A)
_CefFIBSummaryEntry_Object=MibTableRow
cefFIBSummaryEntry=_CefFIBSummaryEntry_Object((1,3,6,1,4,1,9,9,492,1,1,1,1,1))
cefFIBSummaryEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:cefFIBSummaryEntry.setStatus(_A)
_CefFIBIpVersion_Type=CefIpVersion
_CefFIBIpVersion_Object=MibTableColumn
cefFIBIpVersion=_CefFIBIpVersion_Object((1,3,6,1,4,1,9,9,492,1,1,1,1,1,1),_CefFIBIpVersion_Type())
cefFIBIpVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:cefFIBIpVersion.setStatus(_A)
_CefFIBSummaryFwdPrefixes_Type=Unsigned32
_CefFIBSummaryFwdPrefixes_Object=MibTableColumn
cefFIBSummaryFwdPrefixes=_CefFIBSummaryFwdPrefixes_Object((1,3,6,1,4,1,9,9,492,1,1,1,1,1,2),_CefFIBSummaryFwdPrefixes_Type())
cefFIBSummaryFwdPrefixes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFIBSummaryFwdPrefixes.setStatus(_A)
_CefPrefixTable_Object=MibTable
cefPrefixTable=_CefPrefixTable_Object((1,3,6,1,4,1,9,9,492,1,1,2))
if mibBuilder.loadTexts:cefPrefixTable.setStatus(_A)
_CefPrefixEntry_Object=MibTableRow
cefPrefixEntry=_CefPrefixEntry_Object((1,3,6,1,4,1,9,9,492,1,1,2,1))
cefPrefixEntry.setIndexNames((0,_F,_G),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cefPrefixEntry.setStatus(_A)
_CefPrefixType_Type=InetAddressType
_CefPrefixType_Object=MibTableColumn
cefPrefixType=_CefPrefixType_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,1),_CefPrefixType_Type())
cefPrefixType.setMaxAccess(_E)
if mibBuilder.loadTexts:cefPrefixType.setStatus(_A)
_CefPrefixAddr_Type=InetAddress
_CefPrefixAddr_Object=MibTableColumn
cefPrefixAddr=_CefPrefixAddr_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,2),_CefPrefixAddr_Type())
cefPrefixAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cefPrefixAddr.setStatus(_A)
_CefPrefixLen_Type=InetAddressPrefixLength
_CefPrefixLen_Object=MibTableColumn
cefPrefixLen=_CefPrefixLen_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,3),_CefPrefixLen_Type())
cefPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:cefPrefixLen.setStatus(_A)
_CefPrefixForwardingInfo_Type=SnmpAdminString
_CefPrefixForwardingInfo_Object=MibTableColumn
cefPrefixForwardingInfo=_CefPrefixForwardingInfo_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,4),_CefPrefixForwardingInfo_Type())
cefPrefixForwardingInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixForwardingInfo.setStatus(_A)
_CefPrefixPkts_Type=Counter32
_CefPrefixPkts_Object=MibTableColumn
cefPrefixPkts=_CefPrefixPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,5),_CefPrefixPkts_Type())
cefPrefixPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixPkts.setUnits(_H)
_CefPrefixHCPkts_Type=Counter64
_CefPrefixHCPkts_Object=MibTableColumn
cefPrefixHCPkts=_CefPrefixHCPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,6),_CefPrefixHCPkts_Type())
cefPrefixHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixHCPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixHCPkts.setUnits(_H)
_CefPrefixBytes_Type=Counter32
_CefPrefixBytes_Object=MibTableColumn
cefPrefixBytes=_CefPrefixBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,7),_CefPrefixBytes_Type())
cefPrefixBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixBytes.setUnits(_K)
_CefPrefixHCBytes_Type=Counter64
_CefPrefixHCBytes_Object=MibTableColumn
cefPrefixHCBytes=_CefPrefixHCBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,8),_CefPrefixHCBytes_Type())
cefPrefixHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixHCBytes.setUnits(_K)
_CefPrefixInternalNRPkts_Type=Counter32
_CefPrefixInternalNRPkts_Object=MibTableColumn
cefPrefixInternalNRPkts=_CefPrefixInternalNRPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,9),_CefPrefixInternalNRPkts_Type())
cefPrefixInternalNRPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixInternalNRPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixInternalNRPkts.setUnits(_H)
_CefPrefixInternalNRHCPkts_Type=Counter64
_CefPrefixInternalNRHCPkts_Object=MibTableColumn
cefPrefixInternalNRHCPkts=_CefPrefixInternalNRHCPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,10),_CefPrefixInternalNRHCPkts_Type())
cefPrefixInternalNRHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixInternalNRHCPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixInternalNRHCPkts.setUnits(_H)
_CefPrefixInternalNRBytes_Type=Counter32
_CefPrefixInternalNRBytes_Object=MibTableColumn
cefPrefixInternalNRBytes=_CefPrefixInternalNRBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,11),_CefPrefixInternalNRBytes_Type())
cefPrefixInternalNRBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixInternalNRBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixInternalNRBytes.setUnits(_K)
_CefPrefixInternalNRHCBytes_Type=Counter64
_CefPrefixInternalNRHCBytes_Object=MibTableColumn
cefPrefixInternalNRHCBytes=_CefPrefixInternalNRHCBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,12),_CefPrefixInternalNRHCBytes_Type())
cefPrefixInternalNRHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixInternalNRHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixInternalNRHCBytes.setUnits(_K)
_CefPrefixExternalNRPkts_Type=Counter32
_CefPrefixExternalNRPkts_Object=MibTableColumn
cefPrefixExternalNRPkts=_CefPrefixExternalNRPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,13),_CefPrefixExternalNRPkts_Type())
cefPrefixExternalNRPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixExternalNRPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixExternalNRPkts.setUnits(_H)
_CefPrefixExternalNRHCPkts_Type=Counter64
_CefPrefixExternalNRHCPkts_Object=MibTableColumn
cefPrefixExternalNRHCPkts=_CefPrefixExternalNRHCPkts_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,14),_CefPrefixExternalNRHCPkts_Type())
cefPrefixExternalNRHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixExternalNRHCPkts.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixExternalNRHCPkts.setUnits(_H)
_CefPrefixExternalNRBytes_Type=Counter32
_CefPrefixExternalNRBytes_Object=MibTableColumn
cefPrefixExternalNRBytes=_CefPrefixExternalNRBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,15),_CefPrefixExternalNRBytes_Type())
cefPrefixExternalNRBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixExternalNRBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixExternalNRBytes.setUnits(_K)
_CefPrefixExternalNRHCBytes_Type=Counter64
_CefPrefixExternalNRHCBytes_Object=MibTableColumn
cefPrefixExternalNRHCBytes=_CefPrefixExternalNRHCBytes_Object((1,3,6,1,4,1,9,9,492,1,1,2,1,16),_CefPrefixExternalNRHCBytes_Type())
cefPrefixExternalNRHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPrefixExternalNRHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cefPrefixExternalNRHCBytes.setUnits(_K)
_CefLMPrefixSpinLock_Type=TestAndIncr
_CefLMPrefixSpinLock_Object=MibScalar
cefLMPrefixSpinLock=_CefLMPrefixSpinLock_Object((1,3,6,1,4,1,9,9,492,1,1,3),_CefLMPrefixSpinLock_Type())
cefLMPrefixSpinLock.setMaxAccess(_D)
if mibBuilder.loadTexts:cefLMPrefixSpinLock.setStatus(_A)
_CefLMPrefixTable_Object=MibTable
cefLMPrefixTable=_CefLMPrefixTable_Object((1,3,6,1,4,1,9,9,492,1,1,4))
if mibBuilder.loadTexts:cefLMPrefixTable.setStatus(_A)
_CefLMPrefixEntry_Object=MibTableRow
cefLMPrefixEntry=_CefLMPrefixEntry_Object((1,3,6,1,4,1,9,9,492,1,1,4,1))
cefLMPrefixEntry.setIndexNames((0,_F,_G),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:cefLMPrefixEntry.setStatus(_A)
_CefLMPrefixDestAddrType_Type=InetAddressType
_CefLMPrefixDestAddrType_Object=MibTableColumn
cefLMPrefixDestAddrType=_CefLMPrefixDestAddrType_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,1),_CefLMPrefixDestAddrType_Type())
cefLMPrefixDestAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cefLMPrefixDestAddrType.setStatus(_A)
_CefLMPrefixDestAddr_Type=InetAddress
_CefLMPrefixDestAddr_Object=MibTableColumn
cefLMPrefixDestAddr=_CefLMPrefixDestAddr_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,2),_CefLMPrefixDestAddr_Type())
cefLMPrefixDestAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cefLMPrefixDestAddr.setStatus(_A)
_CefLMPrefixState_Type=CefPrefixSearchState
_CefLMPrefixState_Object=MibTableColumn
cefLMPrefixState=_CefLMPrefixState_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,3),_CefLMPrefixState_Type())
cefLMPrefixState.setMaxAccess(_C)
if mibBuilder.loadTexts:cefLMPrefixState.setStatus(_A)
_CefLMPrefixAddr_Type=InetAddress
_CefLMPrefixAddr_Object=MibTableColumn
cefLMPrefixAddr=_CefLMPrefixAddr_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,4),_CefLMPrefixAddr_Type())
cefLMPrefixAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefLMPrefixAddr.setStatus(_A)
_CefLMPrefixLen_Type=InetAddressPrefixLength
_CefLMPrefixLen_Object=MibTableColumn
cefLMPrefixLen=_CefLMPrefixLen_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,5),_CefLMPrefixLen_Type())
cefLMPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:cefLMPrefixLen.setStatus(_A)
_CefLMPrefixRowStatus_Type=RowStatus
_CefLMPrefixRowStatus_Object=MibTableColumn
cefLMPrefixRowStatus=_CefLMPrefixRowStatus_Object((1,3,6,1,4,1,9,9,492,1,1,4,1,6),_CefLMPrefixRowStatus_Type())
cefLMPrefixRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:cefLMPrefixRowStatus.setStatus(_A)
_CefPathTable_Object=MibTable
cefPathTable=_CefPathTable_Object((1,3,6,1,4,1,9,9,492,1,1,5))
if mibBuilder.loadTexts:cefPathTable.setStatus(_A)
_CefPathEntry_Object=MibTableRow
cefPathEntry=_CefPathEntry_Object((1,3,6,1,4,1,9,9,492,1,1,5,1))
cefPathEntry.setIndexNames((0,_F,_G),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_c))
if mibBuilder.loadTexts:cefPathEntry.setStatus(_A)
class _CefPathId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CefPathId_Type.__name__=_I
_CefPathId_Object=MibTableColumn
cefPathId=_CefPathId_Object((1,3,6,1,4,1,9,9,492,1,1,5,1,1),_CefPathId_Type())
cefPathId.setMaxAccess(_E)
if mibBuilder.loadTexts:cefPathId.setStatus(_A)
_CefPathType_Type=CefPathType
_CefPathType_Object=MibTableColumn
cefPathType=_CefPathType_Object((1,3,6,1,4,1,9,9,492,1,1,5,1,2),_CefPathType_Type())
cefPathType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPathType.setStatus(_A)
_CefPathInterface_Type=InterfaceIndexOrZero
_CefPathInterface_Object=MibTableColumn
cefPathInterface=_CefPathInterface_Object((1,3,6,1,4,1,9,9,492,1,1,5,1,3),_CefPathInterface_Type())
cefPathInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPathInterface.setStatus(_A)
_CefPathNextHopAddr_Type=InetAddress
_CefPathNextHopAddr_Object=MibTableColumn
cefPathNextHopAddr=_CefPathNextHopAddr_Object((1,3,6,1,4,1,9,9,492,1,1,5,1,4),_CefPathNextHopAddr_Type())
cefPathNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPathNextHopAddr.setStatus(_A)
_CefPathRecurseVrfName_Type=MplsVpnId
_CefPathRecurseVrfName_Object=MibTableColumn
cefPathRecurseVrfName=_CefPathRecurseVrfName_Object((1,3,6,1,4,1,9,9,492,1,1,5,1,5),_CefPathRecurseVrfName_Type())
cefPathRecurseVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPathRecurseVrfName.setStatus(_A)
_CefAdj_ObjectIdentity=ObjectIdentity
cefAdj=_CefAdj_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,2))
_CefAdjSummary_ObjectIdentity=ObjectIdentity
cefAdjSummary=_CefAdjSummary_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,2,1))
_CefAdjSummaryTable_Object=MibTable
cefAdjSummaryTable=_CefAdjSummaryTable_Object((1,3,6,1,4,1,9,9,492,1,2,1,1))
if mibBuilder.loadTexts:cefAdjSummaryTable.setStatus(_A)
_CefAdjSummaryEntry_Object=MibTableRow
cefAdjSummaryEntry=_CefAdjSummaryEntry_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1))
cefAdjSummaryEntry.setIndexNames((0,_F,_G),(0,_B,_U))
if mibBuilder.loadTexts:cefAdjSummaryEntry.setStatus(_A)
_CefAdjSummaryLinkType_Type=CefAdjLinkType
_CefAdjSummaryLinkType_Object=MibTableColumn
cefAdjSummaryLinkType=_CefAdjSummaryLinkType_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1,1),_CefAdjSummaryLinkType_Type())
cefAdjSummaryLinkType.setMaxAccess(_E)
if mibBuilder.loadTexts:cefAdjSummaryLinkType.setStatus(_A)
_CefAdjSummaryComplete_Type=Unsigned32
_CefAdjSummaryComplete_Object=MibTableColumn
cefAdjSummaryComplete=_CefAdjSummaryComplete_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1,2),_CefAdjSummaryComplete_Type())
cefAdjSummaryComplete.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjSummaryComplete.setStatus(_A)
_CefAdjSummaryIncomplete_Type=Unsigned32
_CefAdjSummaryIncomplete_Object=MibTableColumn
cefAdjSummaryIncomplete=_CefAdjSummaryIncomplete_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1,3),_CefAdjSummaryIncomplete_Type())
cefAdjSummaryIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjSummaryIncomplete.setStatus(_A)
_CefAdjSummaryFixup_Type=Unsigned32
_CefAdjSummaryFixup_Object=MibTableColumn
cefAdjSummaryFixup=_CefAdjSummaryFixup_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1,4),_CefAdjSummaryFixup_Type())
cefAdjSummaryFixup.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjSummaryFixup.setStatus(_A)
_CefAdjSummaryRedirect_Type=Unsigned32
_CefAdjSummaryRedirect_Object=MibTableColumn
cefAdjSummaryRedirect=_CefAdjSummaryRedirect_Object((1,3,6,1,4,1,9,9,492,1,2,1,1,1,5),_CefAdjSummaryRedirect_Type())
cefAdjSummaryRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjSummaryRedirect.setStatus(_A)
_CefAdjTable_Object=MibTable
cefAdjTable=_CefAdjTable_Object((1,3,6,1,4,1,9,9,492,1,2,2))
if mibBuilder.loadTexts:cefAdjTable.setStatus(_A)
_CefAdjEntry_Object=MibTableRow
cefAdjEntry=_CefAdjEntry_Object((1,3,6,1,4,1,9,9,492,1,2,2,1))
cefAdjEntry.setIndexNames((0,_F,_G),(0,_O,_P),(0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_U))
if mibBuilder.loadTexts:cefAdjEntry.setStatus(_A)
_CefAdjNextHopAddrType_Type=InetAddressType
_CefAdjNextHopAddrType_Object=MibTableColumn
cefAdjNextHopAddrType=_CefAdjNextHopAddrType_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,1),_CefAdjNextHopAddrType_Type())
cefAdjNextHopAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cefAdjNextHopAddrType.setStatus(_A)
_CefAdjNextHopAddr_Type=InetAddress
_CefAdjNextHopAddr_Object=MibTableColumn
cefAdjNextHopAddr=_CefAdjNextHopAddr_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,2),_CefAdjNextHopAddr_Type())
cefAdjNextHopAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cefAdjNextHopAddr.setStatus(_A)
class _CefAdjConnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_CefAdjConnId_Type.__name__=_L
_CefAdjConnId_Object=MibTableColumn
cefAdjConnId=_CefAdjConnId_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,3),_CefAdjConnId_Type())
cefAdjConnId.setMaxAccess(_E)
if mibBuilder.loadTexts:cefAdjConnId.setStatus(_A)
_CefAdjSource_Type=CefAdjacencySource
_CefAdjSource_Object=MibTableColumn
cefAdjSource=_CefAdjSource_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,4),_CefAdjSource_Type())
cefAdjSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjSource.setStatus(_A)
_CefAdjEncap_Type=SnmpAdminString
_CefAdjEncap_Object=MibTableColumn
cefAdjEncap=_CefAdjEncap_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,5),_CefAdjEncap_Type())
cefAdjEncap.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjEncap.setStatus(_A)
_CefAdjFixup_Type=SnmpAdminString
_CefAdjFixup_Object=MibTableColumn
cefAdjFixup=_CefAdjFixup_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,6),_CefAdjFixup_Type())
cefAdjFixup.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjFixup.setStatus(_A)
class _CefAdjMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CefAdjMTU_Type.__name__=_L
_CefAdjMTU_Object=MibTableColumn
cefAdjMTU=_CefAdjMTU_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,7),_CefAdjMTU_Type())
cefAdjMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjMTU.setStatus(_A)
if mibBuilder.loadTexts:cefAdjMTU.setUnits(_K)
_CefAdjForwardingInfo_Type=SnmpAdminString
_CefAdjForwardingInfo_Object=MibTableColumn
cefAdjForwardingInfo=_CefAdjForwardingInfo_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,8),_CefAdjForwardingInfo_Type())
cefAdjForwardingInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjForwardingInfo.setStatus(_A)
_CefAdjPkts_Type=Counter32
_CefAdjPkts_Object=MibTableColumn
cefAdjPkts=_CefAdjPkts_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,9),_CefAdjPkts_Type())
cefAdjPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjPkts.setStatus(_A)
if mibBuilder.loadTexts:cefAdjPkts.setUnits(_H)
_CefAdjHCPkts_Type=Counter64
_CefAdjHCPkts_Object=MibTableColumn
cefAdjHCPkts=_CefAdjHCPkts_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,10),_CefAdjHCPkts_Type())
cefAdjHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjHCPkts.setStatus(_A)
if mibBuilder.loadTexts:cefAdjHCPkts.setUnits(_H)
_CefAdjBytes_Type=Counter32
_CefAdjBytes_Object=MibTableColumn
cefAdjBytes=_CefAdjBytes_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,11),_CefAdjBytes_Type())
cefAdjBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjBytes.setStatus(_A)
if mibBuilder.loadTexts:cefAdjBytes.setUnits(_K)
_CefAdjHCBytes_Type=Counter64
_CefAdjHCBytes_Object=MibTableColumn
cefAdjHCBytes=_CefAdjHCBytes_Object((1,3,6,1,4,1,9,9,492,1,2,2,1,12),_CefAdjHCBytes_Type())
cefAdjHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefAdjHCBytes.setStatus(_A)
if mibBuilder.loadTexts:cefAdjHCBytes.setUnits(_K)
_CefFE_ObjectIdentity=ObjectIdentity
cefFE=_CefFE_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,3))
_CefFESelectionTable_Object=MibTable
cefFESelectionTable=_CefFESelectionTable_Object((1,3,6,1,4,1,9,9,492,1,3,1))
if mibBuilder.loadTexts:cefFESelectionTable.setStatus(_A)
_CefFESelectionEntry_Object=MibTableRow
cefFESelectionEntry=_CefFESelectionEntry_Object((1,3,6,1,4,1,9,9,492,1,3,1,1))
cefFESelectionEntry.setIndexNames((0,_F,_G),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:cefFESelectionEntry.setStatus(_A)
class _CefFESelectionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CefFESelectionName_Type.__name__=_Q
_CefFESelectionName_Object=MibTableColumn
cefFESelectionName=_CefFESelectionName_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,1),_CefFESelectionName_Type())
cefFESelectionName.setMaxAccess(_E)
if mibBuilder.loadTexts:cefFESelectionName.setStatus(_A)
class _CefFESelectionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CefFESelectionId_Type.__name__=_I
_CefFESelectionId_Object=MibTableColumn
cefFESelectionId=_CefFESelectionId_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,2),_CefFESelectionId_Type())
cefFESelectionId.setMaxAccess(_E)
if mibBuilder.loadTexts:cefFESelectionId.setStatus(_A)
_CefFESelectionSpecial_Type=CefForwardingElementSpecialType
_CefFESelectionSpecial_Object=MibTableColumn
cefFESelectionSpecial=_CefFESelectionSpecial_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,3),_CefFESelectionSpecial_Type())
cefFESelectionSpecial.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionSpecial.setStatus(_A)
_CefFESelectionLabels_Type=CefMplsLabelList
_CefFESelectionLabels_Object=MibTableColumn
cefFESelectionLabels=_CefFESelectionLabels_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,4),_CefFESelectionLabels_Type())
cefFESelectionLabels.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionLabels.setStatus(_A)
_CefFESelectionAdjLinkType_Type=CefAdjLinkType
_CefFESelectionAdjLinkType_Object=MibTableColumn
cefFESelectionAdjLinkType=_CefFESelectionAdjLinkType_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,5),_CefFESelectionAdjLinkType_Type())
cefFESelectionAdjLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionAdjLinkType.setStatus(_A)
_CefFESelectionAdjInterface_Type=InterfaceIndexOrZero
_CefFESelectionAdjInterface_Object=MibTableColumn
cefFESelectionAdjInterface=_CefFESelectionAdjInterface_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,6),_CefFESelectionAdjInterface_Type())
cefFESelectionAdjInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionAdjInterface.setStatus(_A)
_CefFESelectionAdjNextHopAddrType_Type=InetAddressType
_CefFESelectionAdjNextHopAddrType_Object=MibTableColumn
cefFESelectionAdjNextHopAddrType=_CefFESelectionAdjNextHopAddrType_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,7),_CefFESelectionAdjNextHopAddrType_Type())
cefFESelectionAdjNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionAdjNextHopAddrType.setStatus(_A)
_CefFESelectionAdjNextHopAddr_Type=InetAddress
_CefFESelectionAdjNextHopAddr_Object=MibTableColumn
cefFESelectionAdjNextHopAddr=_CefFESelectionAdjNextHopAddr_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,8),_CefFESelectionAdjNextHopAddr_Type())
cefFESelectionAdjNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionAdjNextHopAddr.setStatus(_A)
class _CefFESelectionAdjConnId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_CefFESelectionAdjConnId_Type.__name__=_L
_CefFESelectionAdjConnId_Object=MibTableColumn
cefFESelectionAdjConnId=_CefFESelectionAdjConnId_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,9),_CefFESelectionAdjConnId_Type())
cefFESelectionAdjConnId.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionAdjConnId.setStatus(_A)
_CefFESelectionVrfName_Type=MplsVpnId
_CefFESelectionVrfName_Object=MibTableColumn
cefFESelectionVrfName=_CefFESelectionVrfName_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,10),_CefFESelectionVrfName_Type())
cefFESelectionVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionVrfName.setStatus(_A)
class _CefFESelectionWeight_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_CefFESelectionWeight_Type.__name__=_L
_CefFESelectionWeight_Object=MibTableColumn
cefFESelectionWeight=_CefFESelectionWeight_Object((1,3,6,1,4,1,9,9,492,1,3,1,1,11),_CefFESelectionWeight_Type())
cefFESelectionWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:cefFESelectionWeight.setStatus(_A)
_CefGlobal_ObjectIdentity=ObjectIdentity
cefGlobal=_CefGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,4))
_CefCfgTable_Object=MibTable
cefCfgTable=_CefCfgTable_Object((1,3,6,1,4,1,9,9,492,1,4,1))
if mibBuilder.loadTexts:cefCfgTable.setStatus(_A)
_CefCfgEntry_Object=MibTableRow
cefCfgEntry=_CefCfgEntry_Object((1,3,6,1,4,1,9,9,492,1,4,1,1))
cefCfgEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:cefCfgEntry.setStatus(_A)
_CefCfgAdminState_Type=CefAdminStatus
_CefCfgAdminState_Object=MibTableColumn
cefCfgAdminState=_CefCfgAdminState_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,1),_CefCfgAdminState_Type())
cefCfgAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgAdminState.setStatus(_A)
_CefCfgOperState_Type=CefOperStatus
_CefCfgOperState_Object=MibTableColumn
cefCfgOperState=_CefCfgOperState_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,2),_CefCfgOperState_Type())
cefCfgOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCfgOperState.setStatus(_A)
_CefCfgDistributionAdminState_Type=CefAdminStatus
_CefCfgDistributionAdminState_Object=MibTableColumn
cefCfgDistributionAdminState=_CefCfgDistributionAdminState_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,3),_CefCfgDistributionAdminState_Type())
cefCfgDistributionAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgDistributionAdminState.setStatus(_A)
_CefCfgDistributionOperState_Type=CefOperStatus
_CefCfgDistributionOperState_Object=MibTableColumn
cefCfgDistributionOperState=_CefCfgDistributionOperState_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,4),_CefCfgDistributionOperState_Type())
cefCfgDistributionOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCfgDistributionOperState.setStatus(_A)
class _CefCfgAccountingMap_Type(Bits):namedValues=NamedValues(*(('nonRecursive',0),('perPrefix',1),('prefixLength',2)))
_CefCfgAccountingMap_Type.__name__='Bits'
_CefCfgAccountingMap_Object=MibTableColumn
cefCfgAccountingMap=_CefCfgAccountingMap_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,5),_CefCfgAccountingMap_Type())
cefCfgAccountingMap.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgAccountingMap.setStatus(_A)
class _CefCfgLoadSharingAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('original',2),('tunnel',3),('universal',4)))
_CefCfgLoadSharingAlgorithm_Type.__name__=_I
_CefCfgLoadSharingAlgorithm_Object=MibTableColumn
cefCfgLoadSharingAlgorithm=_CefCfgLoadSharingAlgorithm_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,6),_CefCfgLoadSharingAlgorithm_Type())
cefCfgLoadSharingAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgLoadSharingAlgorithm.setStatus(_A)
class _CefCfgLoadSharingID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_CefCfgLoadSharingID_Type.__name__=_L
_CefCfgLoadSharingID_Object=MibTableColumn
cefCfgLoadSharingID=_CefCfgLoadSharingID_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,7),_CefCfgLoadSharingID_Type())
cefCfgLoadSharingID.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgLoadSharingID.setStatus(_A)
_CefCfgTrafficStatsLoadInterval_Type=Unsigned32
_CefCfgTrafficStatsLoadInterval_Object=MibTableColumn
cefCfgTrafficStatsLoadInterval=_CefCfgTrafficStatsLoadInterval_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,8),_CefCfgTrafficStatsLoadInterval_Type())
cefCfgTrafficStatsLoadInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgTrafficStatsLoadInterval.setStatus(_A)
if mibBuilder.loadTexts:cefCfgTrafficStatsLoadInterval.setUnits(_M)
class _CefCfgTrafficStatsUpdateRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,65535))
_CefCfgTrafficStatsUpdateRate_Type.__name__=_L
_CefCfgTrafficStatsUpdateRate_Object=MibTableColumn
cefCfgTrafficStatsUpdateRate=_CefCfgTrafficStatsUpdateRate_Object((1,3,6,1,4,1,9,9,492,1,4,1,1,9),_CefCfgTrafficStatsUpdateRate_Type())
cefCfgTrafficStatsUpdateRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCfgTrafficStatsUpdateRate.setStatus(_A)
if mibBuilder.loadTexts:cefCfgTrafficStatsUpdateRate.setUnits(_M)
_CefResourceTable_Object=MibTable
cefResourceTable=_CefResourceTable_Object((1,3,6,1,4,1,9,9,492,1,4,2))
if mibBuilder.loadTexts:cefResourceTable.setStatus(_A)
_CefResourceEntry_Object=MibTableRow
cefResourceEntry=_CefResourceEntry_Object((1,3,6,1,4,1,9,9,492,1,4,2,1))
cefResourceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cefResourceEntry.setStatus(_A)
_CefResourceMemoryUsed_Type=Gauge32
_CefResourceMemoryUsed_Object=MibTableColumn
cefResourceMemoryUsed=_CefResourceMemoryUsed_Object((1,3,6,1,4,1,9,9,492,1,4,2,1,1),_CefResourceMemoryUsed_Type())
cefResourceMemoryUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cefResourceMemoryUsed.setStatus(_A)
if mibBuilder.loadTexts:cefResourceMemoryUsed.setUnits(_K)
_CefResourceFailureReason_Type=CefFailureReason
_CefResourceFailureReason_Object=MibTableColumn
cefResourceFailureReason=_CefResourceFailureReason_Object((1,3,6,1,4,1,9,9,492,1,4,2,1,2),_CefResourceFailureReason_Type())
cefResourceFailureReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cefResourceFailureReason.setStatus(_A)
_CefInterface_ObjectIdentity=ObjectIdentity
cefInterface=_CefInterface_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,5))
_CefIntTable_Object=MibTable
cefIntTable=_CefIntTable_Object((1,3,6,1,4,1,9,9,492,1,5,1))
if mibBuilder.loadTexts:cefIntTable.setStatus(_A)
_CefIntEntry_Object=MibTableRow
cefIntEntry=_CefIntEntry_Object((1,3,6,1,4,1,9,9,492,1,5,1,1))
cefIntEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_O,_P))
if mibBuilder.loadTexts:cefIntEntry.setStatus(_A)
class _CefIntSwitchingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cefEnabled',1),('distCefEnabled',2),('cefDisabled',3)))
_CefIntSwitchingState_Type.__name__=_I
_CefIntSwitchingState_Object=MibTableColumn
cefIntSwitchingState=_CefIntSwitchingState_Object((1,3,6,1,4,1,9,9,492,1,5,1,1,1),_CefIntSwitchingState_Type())
cefIntSwitchingState.setMaxAccess(_D)
if mibBuilder.loadTexts:cefIntSwitchingState.setStatus(_A)
class _CefIntLoadSharing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('perPacket',1),('perDestination',2)))
_CefIntLoadSharing_Type.__name__=_I
_CefIntLoadSharing_Object=MibTableColumn
cefIntLoadSharing=_CefIntLoadSharing_Object((1,3,6,1,4,1,9,9,492,1,5,1,1,2),_CefIntLoadSharing_Type())
cefIntLoadSharing.setMaxAccess(_D)
if mibBuilder.loadTexts:cefIntLoadSharing.setStatus(_A)
class _CefIntNonrecursiveAccouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_CefIntNonrecursiveAccouting_Type.__name__=_I
_CefIntNonrecursiveAccouting_Object=MibTableColumn
cefIntNonrecursiveAccouting=_CefIntNonrecursiveAccouting_Object((1,3,6,1,4,1,9,9,492,1,5,1,1,3),_CefIntNonrecursiveAccouting_Type())
cefIntNonrecursiveAccouting.setMaxAccess(_D)
if mibBuilder.loadTexts:cefIntNonrecursiveAccouting.setStatus(_A)
_CefPeer_ObjectIdentity=ObjectIdentity
cefPeer=_CefPeer_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,6))
_CefPeerTable_Object=MibTable
cefPeerTable=_CefPeerTable_Object((1,3,6,1,4,1,9,9,492,1,6,1))
if mibBuilder.loadTexts:cefPeerTable.setStatus(_A)
_CefPeerEntry_Object=MibTableRow
cefPeerEntry=_CefPeerEntry_Object((1,3,6,1,4,1,9,9,492,1,6,1,1))
cefPeerEntry.setIndexNames((0,_F,_G),(0,_B,_V))
if mibBuilder.loadTexts:cefPeerEntry.setStatus(_A)
_EntPeerPhysicalIndex_Type=PhysicalIndex
_EntPeerPhysicalIndex_Object=MibTableColumn
entPeerPhysicalIndex=_EntPeerPhysicalIndex_Object((1,3,6,1,4,1,9,9,492,1,6,1,1,1),_EntPeerPhysicalIndex_Type())
entPeerPhysicalIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:entPeerPhysicalIndex.setStatus(_A)
class _CefPeerOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('peerDisabled',1),('peerUp',2),('peerHold',3)))
_CefPeerOperState_Type.__name__=_I
_CefPeerOperState_Object=MibTableColumn
cefPeerOperState=_CefPeerOperState_Object((1,3,6,1,4,1,9,9,492,1,6,1,1,2),_CefPeerOperState_Type())
cefPeerOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPeerOperState.setStatus(_A)
_CefPeerNumberOfResets_Type=Counter32
_CefPeerNumberOfResets_Object=MibTableColumn
cefPeerNumberOfResets=_CefPeerNumberOfResets_Object((1,3,6,1,4,1,9,9,492,1,6,1,1,3),_CefPeerNumberOfResets_Type())
cefPeerNumberOfResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPeerNumberOfResets.setStatus(_A)
_CefPeerFIBTable_Object=MibTable
cefPeerFIBTable=_CefPeerFIBTable_Object((1,3,6,1,4,1,9,9,492,1,6,2))
if mibBuilder.loadTexts:cefPeerFIBTable.setStatus(_A)
_CefPeerFIBEntry_Object=MibTableRow
cefPeerFIBEntry=_CefPeerFIBEntry_Object((1,3,6,1,4,1,9,9,492,1,6,2,1))
cefPeerFIBEntry.setIndexNames((0,_F,_G),(0,_B,_V),(0,_B,_J))
if mibBuilder.loadTexts:cefPeerFIBEntry.setStatus(_A)
class _CefPeerFIBOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('peerFIBDown',1),('peerFIBUp',2),('peerFIBReloadRequest',3),('peerFIBReloading',4),('peerFIBSynced',5)))
_CefPeerFIBOperState_Type.__name__=_I
_CefPeerFIBOperState_Object=MibTableColumn
cefPeerFIBOperState=_CefPeerFIBOperState_Object((1,3,6,1,4,1,9,9,492,1,6,2,1,1),_CefPeerFIBOperState_Type())
cefPeerFIBOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cefPeerFIBOperState.setStatus(_A)
_CefCC_ObjectIdentity=ObjectIdentity
cefCC=_CefCC_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,7))
_CefCCGlobalTable_Object=MibTable
cefCCGlobalTable=_CefCCGlobalTable_Object((1,3,6,1,4,1,9,9,492,1,7,1))
if mibBuilder.loadTexts:cefCCGlobalTable.setStatus(_A)
_CefCCGlobalEntry_Object=MibTableRow
cefCCGlobalEntry=_CefCCGlobalEntry_Object((1,3,6,1,4,1,9,9,492,1,7,1,1))
cefCCGlobalEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cefCCGlobalEntry.setStatus(_A)
_CefCCGlobalAutoRepairEnabled_Type=TruthValue
_CefCCGlobalAutoRepairEnabled_Object=MibTableColumn
cefCCGlobalAutoRepairEnabled=_CefCCGlobalAutoRepairEnabled_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,1),_CefCCGlobalAutoRepairEnabled_Type())
cefCCGlobalAutoRepairEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCGlobalAutoRepairEnabled.setStatus(_A)
_CefCCGlobalAutoRepairDelay_Type=Unsigned32
_CefCCGlobalAutoRepairDelay_Object=MibTableColumn
cefCCGlobalAutoRepairDelay=_CefCCGlobalAutoRepairDelay_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,2),_CefCCGlobalAutoRepairDelay_Type())
cefCCGlobalAutoRepairDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCGlobalAutoRepairDelay.setStatus(_A)
if mibBuilder.loadTexts:cefCCGlobalAutoRepairDelay.setUnits(_M)
_CefCCGlobalAutoRepairHoldDown_Type=Unsigned32
_CefCCGlobalAutoRepairHoldDown_Object=MibTableColumn
cefCCGlobalAutoRepairHoldDown=_CefCCGlobalAutoRepairHoldDown_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,3),_CefCCGlobalAutoRepairHoldDown_Type())
cefCCGlobalAutoRepairHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCGlobalAutoRepairHoldDown.setStatus(_A)
if mibBuilder.loadTexts:cefCCGlobalAutoRepairHoldDown.setUnits(_M)
_CefCCGlobalErrorMsgEnabled_Type=TruthValue
_CefCCGlobalErrorMsgEnabled_Object=MibTableColumn
cefCCGlobalErrorMsgEnabled=_CefCCGlobalErrorMsgEnabled_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,4),_CefCCGlobalErrorMsgEnabled_Type())
cefCCGlobalErrorMsgEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCGlobalErrorMsgEnabled.setStatus(_A)
class _CefCCGlobalFullScanAction_Type(CefCCAction):defaultValue=3
_CefCCGlobalFullScanAction_Type.__name__=_N
_CefCCGlobalFullScanAction_Object=MibTableColumn
cefCCGlobalFullScanAction=_CefCCGlobalFullScanAction_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,5),_CefCCGlobalFullScanAction_Type())
cefCCGlobalFullScanAction.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCGlobalFullScanAction.setStatus(_A)
_CefCCGlobalFullScanStatus_Type=CefCCStatus
_CefCCGlobalFullScanStatus_Object=MibTableColumn
cefCCGlobalFullScanStatus=_CefCCGlobalFullScanStatus_Object((1,3,6,1,4,1,9,9,492,1,7,1,1,6),_CefCCGlobalFullScanStatus_Type())
cefCCGlobalFullScanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCCGlobalFullScanStatus.setStatus(_A)
_CefCCTypeTable_Object=MibTable
cefCCTypeTable=_CefCCTypeTable_Object((1,3,6,1,4,1,9,9,492,1,7,2))
if mibBuilder.loadTexts:cefCCTypeTable.setStatus(_A)
_CefCCTypeEntry_Object=MibTableRow
cefCCTypeEntry=_CefCCTypeEntry_Object((1,3,6,1,4,1,9,9,492,1,7,2,1))
cefCCTypeEntry.setIndexNames((0,_B,_J),(0,_B,_i))
if mibBuilder.loadTexts:cefCCTypeEntry.setStatus(_A)
_CefCCType_Type=CefCCType
_CefCCType_Object=MibTableColumn
cefCCType=_CefCCType_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,1),_CefCCType_Type())
cefCCType.setMaxAccess(_E)
if mibBuilder.loadTexts:cefCCType.setStatus(_A)
_CefCCEnabled_Type=TruthValue
_CefCCEnabled_Object=MibTableColumn
cefCCEnabled=_CefCCEnabled_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,2),_CefCCEnabled_Type())
cefCCEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCEnabled.setStatus(_A)
_CefCCCount_Type=Unsigned32
_CefCCCount_Object=MibTableColumn
cefCCCount=_CefCCCount_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,3),_CefCCCount_Type())
cefCCCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCCount.setStatus(_A)
_CefCCPeriod_Type=Unsigned32
_CefCCPeriod_Object=MibTableColumn
cefCCPeriod=_CefCCPeriod_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,4),_CefCCPeriod_Type())
cefCCPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cefCCPeriod.setStatus(_A)
if mibBuilder.loadTexts:cefCCPeriod.setUnits(_M)
_CefCCQueriesSent_Type=Counter32
_CefCCQueriesSent_Object=MibTableColumn
cefCCQueriesSent=_CefCCQueriesSent_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,5),_CefCCQueriesSent_Type())
cefCCQueriesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCCQueriesSent.setStatus(_A)
_CefCCQueriesIgnored_Type=Counter32
_CefCCQueriesIgnored_Object=MibTableColumn
cefCCQueriesIgnored=_CefCCQueriesIgnored_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,6),_CefCCQueriesIgnored_Type())
cefCCQueriesIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCCQueriesIgnored.setStatus(_A)
_CefCCQueriesChecked_Type=Counter32
_CefCCQueriesChecked_Object=MibTableColumn
cefCCQueriesChecked=_CefCCQueriesChecked_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,7),_CefCCQueriesChecked_Type())
cefCCQueriesChecked.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCCQueriesChecked.setStatus(_A)
_CefCCQueriesIterated_Type=Counter32
_CefCCQueriesIterated_Object=MibTableColumn
cefCCQueriesIterated=_CefCCQueriesIterated_Object((1,3,6,1,4,1,9,9,492,1,7,2,1,8),_CefCCQueriesIterated_Type())
cefCCQueriesIterated.setMaxAccess(_C)
if mibBuilder.loadTexts:cefCCQueriesIterated.setStatus(_A)
_CefInconsistencyRecordTable_Object=MibTable
cefInconsistencyRecordTable=_CefInconsistencyRecordTable_Object((1,3,6,1,4,1,9,9,492,1,7,3))
if mibBuilder.loadTexts:cefInconsistencyRecordTable.setStatus(_A)
_CefInconsistencyRecordEntry_Object=MibTableRow
cefInconsistencyRecordEntry=_CefInconsistencyRecordEntry_Object((1,3,6,1,4,1,9,9,492,1,7,3,1))
cefInconsistencyRecordEntry.setIndexNames((0,_B,_J),(0,_B,_j))
if mibBuilder.loadTexts:cefInconsistencyRecordEntry.setStatus(_A)
class _CefInconsistencyRecId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CefInconsistencyRecId_Type.__name__=_I
_CefInconsistencyRecId_Object=MibTableColumn
cefInconsistencyRecId=_CefInconsistencyRecId_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,1),_CefInconsistencyRecId_Type())
cefInconsistencyRecId.setMaxAccess(_E)
if mibBuilder.loadTexts:cefInconsistencyRecId.setStatus(_A)
_CefInconsistencyPrefixType_Type=InetAddressType
_CefInconsistencyPrefixType_Object=MibTableColumn
cefInconsistencyPrefixType=_CefInconsistencyPrefixType_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,2),_CefInconsistencyPrefixType_Type())
cefInconsistencyPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyPrefixType.setStatus(_A)
_CefInconsistencyPrefixAddr_Type=InetAddress
_CefInconsistencyPrefixAddr_Object=MibTableColumn
cefInconsistencyPrefixAddr=_CefInconsistencyPrefixAddr_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,3),_CefInconsistencyPrefixAddr_Type())
cefInconsistencyPrefixAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyPrefixAddr.setStatus(_A)
_CefInconsistencyPrefixLen_Type=InetAddressPrefixLength
_CefInconsistencyPrefixLen_Object=MibTableColumn
cefInconsistencyPrefixLen=_CefInconsistencyPrefixLen_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,4),_CefInconsistencyPrefixLen_Type())
cefInconsistencyPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyPrefixLen.setStatus(_A)
_CefInconsistencyVrfName_Type=MplsVpnId
_CefInconsistencyVrfName_Object=MibTableColumn
cefInconsistencyVrfName=_CefInconsistencyVrfName_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,5),_CefInconsistencyVrfName_Type())
cefInconsistencyVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyVrfName.setStatus(_A)
_CefInconsistencyCCType_Type=CefCCType
_CefInconsistencyCCType_Object=MibTableColumn
cefInconsistencyCCType=_CefInconsistencyCCType_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,6),_CefInconsistencyCCType_Type())
cefInconsistencyCCType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyCCType.setStatus(_A)
_CefInconsistencyEntity_Type=EntPhysicalIndexOrZero
_CefInconsistencyEntity_Object=MibTableColumn
cefInconsistencyEntity=_CefInconsistencyEntity_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,7),_CefInconsistencyEntity_Type())
cefInconsistencyEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyEntity.setStatus(_A)
class _CefInconsistencyReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('missing',1),('checksumErr',2),('unknown',3)))
_CefInconsistencyReason_Type.__name__=_I
_CefInconsistencyReason_Object=MibTableColumn
cefInconsistencyReason=_CefInconsistencyReason_Object((1,3,6,1,4,1,9,9,492,1,7,3,1,8),_CefInconsistencyReason_Type())
cefInconsistencyReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyReason.setStatus(_A)
_EntLastInconsistencyDetectTime_Type=TimeStamp
_EntLastInconsistencyDetectTime_Object=MibScalar
entLastInconsistencyDetectTime=_EntLastInconsistencyDetectTime_Object((1,3,6,1,4,1,9,9,492,1,7,4),_EntLastInconsistencyDetectTime_Type())
entLastInconsistencyDetectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:entLastInconsistencyDetectTime.setStatus(_A)
class _CefInconsistencyReset_Type(CefCCAction):defaultValue=3
_CefInconsistencyReset_Type.__name__=_N
_CefInconsistencyReset_Object=MibScalar
cefInconsistencyReset=_CefInconsistencyReset_Object((1,3,6,1,4,1,9,9,492,1,7,5),_CefInconsistencyReset_Type())
cefInconsistencyReset.setMaxAccess(_D)
if mibBuilder.loadTexts:cefInconsistencyReset.setStatus(_A)
_CefInconsistencyResetStatus_Type=CefCCStatus
_CefInconsistencyResetStatus_Object=MibScalar
cefInconsistencyResetStatus=_CefInconsistencyResetStatus_Object((1,3,6,1,4,1,9,9,492,1,7,6),_CefInconsistencyResetStatus_Type())
cefInconsistencyResetStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefInconsistencyResetStatus.setStatus(_A)
_CefStats_ObjectIdentity=ObjectIdentity
cefStats=_CefStats_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,8))
_CefStatsPrefixLenTable_Object=MibTable
cefStatsPrefixLenTable=_CefStatsPrefixLenTable_Object((1,3,6,1,4,1,9,9,492,1,8,1))
if mibBuilder.loadTexts:cefStatsPrefixLenTable.setStatus(_A)
_CefStatsPrefixLenEntry_Object=MibTableRow
cefStatsPrefixLenEntry=_CefStatsPrefixLenEntry_Object((1,3,6,1,4,1,9,9,492,1,8,1,1))
cefStatsPrefixLenEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_k))
if mibBuilder.loadTexts:cefStatsPrefixLenEntry.setStatus(_A)
_CefStatsPrefixLen_Type=InetAddressPrefixLength
_CefStatsPrefixLen_Object=MibTableColumn
cefStatsPrefixLen=_CefStatsPrefixLen_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,1),_CefStatsPrefixLen_Type())
cefStatsPrefixLen.setMaxAccess(_E)
if mibBuilder.loadTexts:cefStatsPrefixLen.setStatus(_A)
_CefStatsPrefixQueries_Type=Counter32
_CefStatsPrefixQueries_Object=MibTableColumn
cefStatsPrefixQueries=_CefStatsPrefixQueries_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,2),_CefStatsPrefixQueries_Type())
cefStatsPrefixQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixQueries.setStatus(_A)
_CefStatsPrefixHCQueries_Type=Counter64
_CefStatsPrefixHCQueries_Object=MibTableColumn
cefStatsPrefixHCQueries=_CefStatsPrefixHCQueries_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,3),_CefStatsPrefixHCQueries_Type())
cefStatsPrefixHCQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixHCQueries.setStatus(_A)
_CefStatsPrefixInserts_Type=Counter32
_CefStatsPrefixInserts_Object=MibTableColumn
cefStatsPrefixInserts=_CefStatsPrefixInserts_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,4),_CefStatsPrefixInserts_Type())
cefStatsPrefixInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixInserts.setStatus(_A)
_CefStatsPrefixHCInserts_Type=Counter64
_CefStatsPrefixHCInserts_Object=MibTableColumn
cefStatsPrefixHCInserts=_CefStatsPrefixHCInserts_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,5),_CefStatsPrefixHCInserts_Type())
cefStatsPrefixHCInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixHCInserts.setStatus(_A)
_CefStatsPrefixDeletes_Type=Counter32
_CefStatsPrefixDeletes_Object=MibTableColumn
cefStatsPrefixDeletes=_CefStatsPrefixDeletes_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,6),_CefStatsPrefixDeletes_Type())
cefStatsPrefixDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixDeletes.setStatus(_A)
_CefStatsPrefixHCDeletes_Type=Counter64
_CefStatsPrefixHCDeletes_Object=MibTableColumn
cefStatsPrefixHCDeletes=_CefStatsPrefixHCDeletes_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,7),_CefStatsPrefixHCDeletes_Type())
cefStatsPrefixHCDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixHCDeletes.setStatus(_A)
_CefStatsPrefixElements_Type=Gauge32
_CefStatsPrefixElements_Object=MibTableColumn
cefStatsPrefixElements=_CefStatsPrefixElements_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,8),_CefStatsPrefixElements_Type())
cefStatsPrefixElements.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixElements.setStatus(_A)
_CefStatsPrefixHCElements_Type=CounterBasedGauge64
_CefStatsPrefixHCElements_Object=MibTableColumn
cefStatsPrefixHCElements=_CefStatsPrefixHCElements_Object((1,3,6,1,4,1,9,9,492,1,8,1,1,9),_CefStatsPrefixHCElements_Type())
cefStatsPrefixHCElements.setMaxAccess(_C)
if mibBuilder.loadTexts:cefStatsPrefixHCElements.setStatus(_A)
_CefSwitchingStatsTable_Object=MibTable
cefSwitchingStatsTable=_CefSwitchingStatsTable_Object((1,3,6,1,4,1,9,9,492,1,8,2))
if mibBuilder.loadTexts:cefSwitchingStatsTable.setStatus(_A)
_CefSwitchingStatsEntry_Object=MibTableRow
cefSwitchingStatsEntry=_CefSwitchingStatsEntry_Object((1,3,6,1,4,1,9,9,492,1,8,2,1))
cefSwitchingStatsEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_l))
if mibBuilder.loadTexts:cefSwitchingStatsEntry.setStatus(_A)
class _CefSwitchingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CefSwitchingIndex_Type.__name__=_I
_CefSwitchingIndex_Object=MibTableColumn
cefSwitchingIndex=_CefSwitchingIndex_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,1),_CefSwitchingIndex_Type())
cefSwitchingIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cefSwitchingIndex.setStatus(_A)
class _CefSwitchingPath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CefSwitchingPath_Type.__name__=_Q
_CefSwitchingPath_Object=MibTableColumn
cefSwitchingPath=_CefSwitchingPath_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,2),_CefSwitchingPath_Type())
cefSwitchingPath.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingPath.setStatus(_A)
_CefSwitchingDrop_Type=Counter32
_CefSwitchingDrop_Object=MibTableColumn
cefSwitchingDrop=_CefSwitchingDrop_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,3),_CefSwitchingDrop_Type())
cefSwitchingDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingDrop.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingDrop.setUnits(_H)
_CefSwitchingHCDrop_Type=Counter64
_CefSwitchingHCDrop_Object=MibTableColumn
cefSwitchingHCDrop=_CefSwitchingHCDrop_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,4),_CefSwitchingHCDrop_Type())
cefSwitchingHCDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingHCDrop.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingHCDrop.setUnits(_H)
_CefSwitchingPunt_Type=Counter32
_CefSwitchingPunt_Object=MibTableColumn
cefSwitchingPunt=_CefSwitchingPunt_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,5),_CefSwitchingPunt_Type())
cefSwitchingPunt.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingPunt.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingPunt.setUnits(_H)
_CefSwitchingHCPunt_Type=Counter64
_CefSwitchingHCPunt_Object=MibTableColumn
cefSwitchingHCPunt=_CefSwitchingHCPunt_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,6),_CefSwitchingHCPunt_Type())
cefSwitchingHCPunt.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingHCPunt.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingHCPunt.setUnits(_H)
_CefSwitchingPunt2Host_Type=Counter32
_CefSwitchingPunt2Host_Object=MibTableColumn
cefSwitchingPunt2Host=_CefSwitchingPunt2Host_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,7),_CefSwitchingPunt2Host_Type())
cefSwitchingPunt2Host.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingPunt2Host.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingPunt2Host.setUnits(_H)
_CefSwitchingHCPunt2Host_Type=Counter64
_CefSwitchingHCPunt2Host_Object=MibTableColumn
cefSwitchingHCPunt2Host=_CefSwitchingHCPunt2Host_Object((1,3,6,1,4,1,9,9,492,1,8,2,1,8),_CefSwitchingHCPunt2Host_Type())
cefSwitchingHCPunt2Host.setMaxAccess(_C)
if mibBuilder.loadTexts:cefSwitchingHCPunt2Host.setStatus(_A)
if mibBuilder.loadTexts:cefSwitchingHCPunt2Host.setUnits(_H)
_CefNotifCntl_ObjectIdentity=ObjectIdentity
cefNotifCntl=_CefNotifCntl_ObjectIdentity((1,3,6,1,4,1,9,9,492,1,9))
_CefResourceFailureNotifEnable_Type=TruthValue
_CefResourceFailureNotifEnable_Object=MibScalar
cefResourceFailureNotifEnable=_CefResourceFailureNotifEnable_Object((1,3,6,1,4,1,9,9,492,1,9,1),_CefResourceFailureNotifEnable_Type())
cefResourceFailureNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cefResourceFailureNotifEnable.setStatus(_A)
_CefPeerStateChangeNotifEnable_Type=TruthValue
_CefPeerStateChangeNotifEnable_Object=MibScalar
cefPeerStateChangeNotifEnable=_CefPeerStateChangeNotifEnable_Object((1,3,6,1,4,1,9,9,492,1,9,2),_CefPeerStateChangeNotifEnable_Type())
cefPeerStateChangeNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cefPeerStateChangeNotifEnable.setStatus(_A)
_CefPeerFIBStateChangeNotifEnable_Type=TruthValue
_CefPeerFIBStateChangeNotifEnable_Object=MibScalar
cefPeerFIBStateChangeNotifEnable=_CefPeerFIBStateChangeNotifEnable_Object((1,3,6,1,4,1,9,9,492,1,9,3),_CefPeerFIBStateChangeNotifEnable_Type())
cefPeerFIBStateChangeNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cefPeerFIBStateChangeNotifEnable.setStatus(_A)
class _CefNotifThrottlingInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,3600))
_CefNotifThrottlingInterval_Type.__name__=_I
_CefNotifThrottlingInterval_Object=MibScalar
cefNotifThrottlingInterval=_CefNotifThrottlingInterval_Object((1,3,6,1,4,1,9,9,492,1,9,4),_CefNotifThrottlingInterval_Type())
cefNotifThrottlingInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cefNotifThrottlingInterval.setStatus(_A)
if mibBuilder.loadTexts:cefNotifThrottlingInterval.setUnits(_M)
_CefInconsistencyNotifEnable_Type=TruthValue
_CefInconsistencyNotifEnable_Object=MibScalar
cefInconsistencyNotifEnable=_CefInconsistencyNotifEnable_Object((1,3,6,1,4,1,9,9,492,1,9,5),_CefInconsistencyNotifEnable_Type())
cefInconsistencyNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cefInconsistencyNotifEnable.setStatus(_A)
_CiscoCefMIBConform_ObjectIdentity=ObjectIdentity
ciscoCefMIBConform=_CiscoCefMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,492,2))
_CefMIBGroups_ObjectIdentity=ObjectIdentity
cefMIBGroups=_CefMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,492,2,1))
_CefMIBCompliances_ObjectIdentity=ObjectIdentity
cefMIBCompliances=_CefMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,492,2,2))
cefGroup=ObjectGroup((1,3,6,1,4,1,9,9,492,2,1,1))
cefGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_W),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:cefGroup.setStatus(_A)
cefDistributedGroup=ObjectGroup((1,3,6,1,4,1,9,9,492,2,1,2))
cefDistributedGroup.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_X),(_B,_Ai),(_B,_Y),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Z),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:cefDistributedGroup.setStatus(_A)
cefHCStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,492,2,1,3))
cefHCStatsGroup.setObjects(*((_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI)))
if mibBuilder.loadTexts:cefHCStatsGroup.setStatus(_A)
cefNotifCntlGroup=ObjectGroup((1,3,6,1,4,1,9,9,492,2,1,5))
cefNotifCntlGroup.setObjects(*((_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN)))
if mibBuilder.loadTexts:cefNotifCntlGroup.setStatus(_A)
cefResourceFailure=NotificationType((1,3,6,1,4,1,9,9,492,0,1))
cefResourceFailure.setObjects((_B,_W))
if mibBuilder.loadTexts:cefResourceFailure.setStatus(_A)
cefPeerStateChange=NotificationType((1,3,6,1,4,1,9,9,492,0,2))
cefPeerStateChange.setObjects((_B,_X))
if mibBuilder.loadTexts:cefPeerStateChange.setStatus(_A)
cefPeerFIBStateChange=NotificationType((1,3,6,1,4,1,9,9,492,0,3))
cefPeerFIBStateChange.setObjects((_B,_Y))
if mibBuilder.loadTexts:cefPeerFIBStateChange.setStatus(_A)
cefInconsistencyDetection=NotificationType((1,3,6,1,4,1,9,9,492,0,4))
cefInconsistencyDetection.setObjects((_B,_Z))
if mibBuilder.loadTexts:cefInconsistencyDetection.setStatus(_A)
cefNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,492,2,1,6))
cefNotificationGroup.setObjects(*((_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR)))
if mibBuilder.loadTexts:cefNotificationGroup.setStatus(_A)
cefMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,492,2,2,1))
cefMIBCompliance.setObjects(*((_B,'cefGroup'),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV)))
if mibBuilder.loadTexts:cefMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCefMIB':ciscoCefMIB,'ciscoCefMIBNotifs':ciscoCefMIBNotifs,_BO:cefResourceFailure,_BP:cefPeerStateChange,_BQ:cefPeerFIBStateChange,_BR:cefInconsistencyDetection,'ciscoCefMIBObjects':ciscoCefMIBObjects,'cefFIB':cefFIB,'cefFIBSummary':cefFIBSummary,'cefFIBSummaryTable':cefFIBSummaryTable,'cefFIBSummaryEntry':cefFIBSummaryEntry,_J:cefFIBIpVersion,_m:cefFIBSummaryFwdPrefixes,'cefPrefixTable':cefPrefixTable,'cefPrefixEntry':cefPrefixEntry,_R:cefPrefixType,_S:cefPrefixAddr,_T:cefPrefixLen,_n:cefPrefixForwardingInfo,_o:cefPrefixPkts,_B4:cefPrefixHCPkts,_p:cefPrefixBytes,_B5:cefPrefixHCBytes,_q:cefPrefixInternalNRPkts,_B6:cefPrefixInternalNRHCPkts,_r:cefPrefixInternalNRBytes,_B7:cefPrefixInternalNRHCBytes,_s:cefPrefixExternalNRPkts,_B8:cefPrefixExternalNRHCPkts,_t:cefPrefixExternalNRBytes,_B9:cefPrefixExternalNRHCBytes,_u:cefLMPrefixSpinLock,'cefLMPrefixTable':cefLMPrefixTable,'cefLMPrefixEntry':cefLMPrefixEntry,_a:cefLMPrefixDestAddrType,_b:cefLMPrefixDestAddr,_v:cefLMPrefixState,_w:cefLMPrefixAddr,_x:cefLMPrefixLen,_y:cefLMPrefixRowStatus,'cefPathTable':cefPathTable,'cefPathEntry':cefPathEntry,_c:cefPathId,_z:cefPathType,_A0:cefPathInterface,_A1:cefPathNextHopAddr,_A2:cefPathRecurseVrfName,'cefAdj':cefAdj,'cefAdjSummary':cefAdjSummary,'cefAdjSummaryTable':cefAdjSummaryTable,'cefAdjSummaryEntry':cefAdjSummaryEntry,_U:cefAdjSummaryLinkType,_A3:cefAdjSummaryComplete,_A4:cefAdjSummaryIncomplete,_A5:cefAdjSummaryFixup,_A6:cefAdjSummaryRedirect,'cefAdjTable':cefAdjTable,'cefAdjEntry':cefAdjEntry,_d:cefAdjNextHopAddrType,_e:cefAdjNextHopAddr,_f:cefAdjConnId,_A7:cefAdjSource,_A8:cefAdjEncap,_A9:cefAdjFixup,_AA:cefAdjMTU,_AB:cefAdjForwardingInfo,_AC:cefAdjPkts,_BA:cefAdjHCPkts,_AD:cefAdjBytes,_BB:cefAdjHCBytes,'cefFE':cefFE,'cefFESelectionTable':cefFESelectionTable,'cefFESelectionEntry':cefFESelectionEntry,_g:cefFESelectionName,_h:cefFESelectionId,_AE:cefFESelectionSpecial,_AF:cefFESelectionLabels,_AG:cefFESelectionAdjLinkType,_AH:cefFESelectionAdjInterface,_AI:cefFESelectionAdjNextHopAddrType,_AJ:cefFESelectionAdjNextHopAddr,_AK:cefFESelectionAdjConnId,_AL:cefFESelectionVrfName,_AM:cefFESelectionWeight,'cefGlobal':cefGlobal,'cefCfgTable':cefCfgTable,'cefCfgEntry':cefCfgEntry,_AN:cefCfgAdminState,_AO:cefCfgOperState,_Ag:cefCfgDistributionAdminState,_Ah:cefCfgDistributionOperState,_AP:cefCfgAccountingMap,_AQ:cefCfgLoadSharingAlgorithm,_AR:cefCfgLoadSharingID,_AS:cefCfgTrafficStatsLoadInterval,_AT:cefCfgTrafficStatsUpdateRate,'cefResourceTable':cefResourceTable,'cefResourceEntry':cefResourceEntry,_AU:cefResourceMemoryUsed,_W:cefResourceFailureReason,'cefInterface':cefInterface,'cefIntTable':cefIntTable,'cefIntEntry':cefIntEntry,_AV:cefIntSwitchingState,_AW:cefIntLoadSharing,_AX:cefIntNonrecursiveAccouting,'cefPeer':cefPeer,'cefPeerTable':cefPeerTable,'cefPeerEntry':cefPeerEntry,_V:entPeerPhysicalIndex,_X:cefPeerOperState,_Ai:cefPeerNumberOfResets,'cefPeerFIBTable':cefPeerFIBTable,'cefPeerFIBEntry':cefPeerFIBEntry,_Y:cefPeerFIBOperState,'cefCC':cefCC,'cefCCGlobalTable':cefCCGlobalTable,'cefCCGlobalEntry':cefCCGlobalEntry,_Aj:cefCCGlobalAutoRepairEnabled,_Ak:cefCCGlobalAutoRepairDelay,_Al:cefCCGlobalAutoRepairHoldDown,_Am:cefCCGlobalErrorMsgEnabled,_Ao:cefCCGlobalFullScanAction,_An:cefCCGlobalFullScanStatus,'cefCCTypeTable':cefCCTypeTable,'cefCCTypeEntry':cefCCTypeEntry,_i:cefCCType,_Ap:cefCCEnabled,_Aq:cefCCCount,_Ar:cefCCPeriod,_As:cefCCQueriesSent,_At:cefCCQueriesIgnored,_Au:cefCCQueriesChecked,_Av:cefCCQueriesIterated,'cefInconsistencyRecordTable':cefInconsistencyRecordTable,'cefInconsistencyRecordEntry':cefInconsistencyRecordEntry,_j:cefInconsistencyRecId,_Aw:cefInconsistencyPrefixType,_Ax:cefInconsistencyPrefixAddr,_Ay:cefInconsistencyPrefixLen,_Az:cefInconsistencyVrfName,_A_:cefInconsistencyCCType,_B0:cefInconsistencyEntity,_B1:cefInconsistencyReason,_Z:entLastInconsistencyDetectTime,_B2:cefInconsistencyReset,_B3:cefInconsistencyResetStatus,'cefStats':cefStats,'cefStatsPrefixLenTable':cefStatsPrefixLenTable,'cefStatsPrefixLenEntry':cefStatsPrefixLenEntry,_k:cefStatsPrefixLen,_AY:cefStatsPrefixQueries,_BC:cefStatsPrefixHCQueries,_AZ:cefStatsPrefixInserts,_BD:cefStatsPrefixHCInserts,_Aa:cefStatsPrefixDeletes,_BE:cefStatsPrefixHCDeletes,_Ab:cefStatsPrefixElements,_BF:cefStatsPrefixHCElements,'cefSwitchingStatsTable':cefSwitchingStatsTable,'cefSwitchingStatsEntry':cefSwitchingStatsEntry,_l:cefSwitchingIndex,_Ac:cefSwitchingPath,_Ad:cefSwitchingDrop,_BG:cefSwitchingHCDrop,_Ae:cefSwitchingPunt,_BH:cefSwitchingHCPunt,_Af:cefSwitchingPunt2Host,_BI:cefSwitchingHCPunt2Host,'cefNotifCntl':cefNotifCntl,_BJ:cefResourceFailureNotifEnable,_BK:cefPeerStateChangeNotifEnable,_BL:cefPeerFIBStateChangeNotifEnable,_BM:cefNotifThrottlingInterval,_BN:cefInconsistencyNotifEnable,'ciscoCefMIBConform':ciscoCefMIBConform,'cefMIBGroups':cefMIBGroups,'cefGroup':cefGroup,_BU:cefDistributedGroup,_BV:cefHCStatsGroup,_BS:cefNotifCntlGroup,_BT:cefNotificationGroup,'cefMIBCompliances':cefMIBCompliances,'cefMIBCompliance':cefMIBCompliance})