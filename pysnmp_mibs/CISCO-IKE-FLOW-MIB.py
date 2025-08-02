_AS='cifIkeFlowNotifCntlGroup'
_AR='cifIkeFlowNotificationGroup'
_AQ='cifIkeFlowModeConfigHistoryGroup'
_AP='cifIkeFlowNewGroupHistoryGroup'
_AO='cifIkeFlowHistoryGroup'
_AN='cifIkeFlowModeConfigGroup'
_AM='cifIkeFlowXauthGroup'
_AL='cifIkeFlowNewGroupGroup'
_AK='ciscoIkeFlowActivityGroup'
_AJ='ciscoIkeFlowOutNewGrpRejected'
_AI='ciscoIkeFlowInNewGrpRejected'
_AH='cifIkeNotifCntlOutNewGrpRejected'
_AG='cifIkeNotifCntlInNewGrpRejected'
_AF='cifIkeTunHistOutConfigsRejects'
_AE='cifIkeTunHistInConfigsRejects'
_AD='cifIkeTunHistOutConfigs'
_AC='cifIkeTunHistInConfigs'
_AB='cifIkeTunHistOutNewGrpRejectReqs'
_AA='cifIkeTunHistInNewGrpRejectReqs'
_A9='cifIkeTunHistOutNewGrpReqs'
_A8='cifIkeTunHistInNewGrpReqs'
_A7='cifIkeTunHistOutP2ExchgRejects'
_A6='cifIkeTunHistOutP2ExchgInvalids'
_A5='cifIkeTunHistOutP2Exchgs'
_A4='cifIkeTunHistInP2ExchgRejects'
_A3='cifIkeTunHistInP2ExchgInvalids'
_A2='cifIkeTunHistInP2Exchgs'
_A1='cifIkeTunHistTotalSas'
_A0='cifIkeTunHistTotalRefreshes'
_z='cifIkeTunHistDHGrp'
_y='cifIkeTunHistNegoMode'
_x='cifIkeTunOutConfigRejects'
_w='cifIkeTunInConfigRejects'
_v='cifIkeTunOutConfigs'
_u='cifIkeTunInConfigs'
_t='cifIkeGlobalOutXauthFailures'
_s='cifIkeGlobalInXauthFailures'
_r='cifIkeGlobalInXauths'
_q='cifIkeTunOutNewGrpRejectedReqs'
_p='cifIkeTunInNewGrpRejectedReqs'
_o='cifIkeTunOutNewGrpReqs'
_n='cifIkeTunInNewGrpReqs'
_m='cifIkeGlobalOutNewGrpRejectReqs'
_l='cifIkeGlobalInNewGrpRejectReqs'
_k='cifIkeGlobalOutNewGrpReqs'
_j='cifIkeGlobalInNewGrpReqs'
_i='cifIkeTunOutP2ExchgRejects'
_h='cifIkeTunOutP2ExchgInvalids'
_g='cifIkeTunOutP2Exchgs'
_f='cifIkeTunInP2SaDelRequests'
_e='cifIkeTunInP2ExchgRejects'
_d='cifIkeTunInP2ExchgInvalids'
_c='cifIkeTunInP2Exchgs'
_b='cifIkeTunTotalRefreshes'
_a='cifIkeTunSaRefreshThreshold'
_Z='cifIkeTunDHGrp'
_Y='cifIkeTunNegoMode'
_X='cifIkeGlobalOutP2ExchgRejects'
_W='cifIkeGlobalOutP2ExchgInvalids'
_V='cifIkeGlobalOutP2Exchgs'
_U='cifIkeGlobalInP2ExchgRejects'
_T='cifIkeGlobalInP2ExchgInvalids'
_S='cifIkeGlobalInP2Exchgs'
_R='read-write'
_Q='Notification Payloads'
_P='QM Exchanges'
_O='Unsigned32'
_N='cisgIpsSgTunIndex'
_M='cisgIpsSgTunHistIndex'
_L='Failures'
_K='TruthValue'
_J='cisgIpsSgFailRemoteAddress'
_I='cisgIpsSgFailLocalAddress'
_H='cisgIpsSgProtocol'
_G='Mode Configuration Setting Payloads'
_F='CISCO-IPSEC-SIGNALING-MIB'
_E='Negotiations'
_D='SA Payloads'
_C='read-only'
_B='CISCO-IKE-FLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cisgIpsSgFailLocalAddress,cisgIpsSgFailRemoteAddress,cisgIpsSgProtocol,cisgIpsSgTunHistIndex,cisgIpsSgTunIndex=mibBuilder.importSymbols(_F,_I,_J,_H,_M,_N)
CIPsecDiffHellmanGrp,CIPsecIkeNegoMode=mibBuilder.importSymbols('CISCO-IPSEC-TC','CIPsecDiffHellmanGrp','CIPsecIkeNegoMode')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_K)
ciscoIkeFlowMIB=ModuleIdentity((1,3,6,1,4,1,9,9,429))
if mibBuilder.loadTexts:ciscoIkeFlowMIB.setRevisions(('2004-09-14 00:00',))
_CiscoIkeFlowMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIkeFlowMIBNotifs=_CiscoIkeFlowMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,429,0))
_CiscoIkeFlowMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIkeFlowMIBObjects=_CiscoIkeFlowMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,429,1))
_CifIkeCurrentActivity_ObjectIdentity=ObjectIdentity
cifIkeCurrentActivity=_CifIkeCurrentActivity_ObjectIdentity((1,3,6,1,4,1,9,9,429,1,1))
_CifIkeGlobalStatsTable_Object=MibTable
cifIkeGlobalStatsTable=_CifIkeGlobalStatsTable_Object((1,3,6,1,4,1,9,9,429,1,1,1))
if mibBuilder.loadTexts:cifIkeGlobalStatsTable.setStatus(_A)
_CifIkeGlobalStatsEntry_Object=MibTableRow
cifIkeGlobalStatsEntry=_CifIkeGlobalStatsEntry_Object((1,3,6,1,4,1,9,9,429,1,1,1,1))
cifIkeGlobalStatsEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:cifIkeGlobalStatsEntry.setStatus(_A)
_CifIkeGlobalInP2Exchgs_Type=Counter64
_CifIkeGlobalInP2Exchgs_Object=MibTableColumn
cifIkeGlobalInP2Exchgs=_CifIkeGlobalInP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,1),_CifIkeGlobalInP2Exchgs_Type())
cifIkeGlobalInP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInP2Exchgs.setUnits(_D)
_CifIkeGlobalInP2ExchgInvalids_Type=Counter64
_CifIkeGlobalInP2ExchgInvalids_Object=MibTableColumn
cifIkeGlobalInP2ExchgInvalids=_CifIkeGlobalInP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,2),_CifIkeGlobalInP2ExchgInvalids_Type())
cifIkeGlobalInP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInP2ExchgInvalids.setUnits(_D)
_CifIkeGlobalInP2ExchgRejects_Type=Counter64
_CifIkeGlobalInP2ExchgRejects_Object=MibTableColumn
cifIkeGlobalInP2ExchgRejects=_CifIkeGlobalInP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,3),_CifIkeGlobalInP2ExchgRejects_Type())
cifIkeGlobalInP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInP2ExchgRejects.setUnits(_D)
_CifIkeGlobalOutP2Exchgs_Type=Counter64
_CifIkeGlobalOutP2Exchgs_Object=MibTableColumn
cifIkeGlobalOutP2Exchgs=_CifIkeGlobalOutP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,4),_CifIkeGlobalOutP2Exchgs_Type())
cifIkeGlobalOutP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutP2Exchgs.setUnits(_D)
_CifIkeGlobalOutP2ExchgInvalids_Type=Counter64
_CifIkeGlobalOutP2ExchgInvalids_Object=MibTableColumn
cifIkeGlobalOutP2ExchgInvalids=_CifIkeGlobalOutP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,5),_CifIkeGlobalOutP2ExchgInvalids_Type())
cifIkeGlobalOutP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutP2ExchgInvalids.setUnits(_D)
_CifIkeGlobalOutP2ExchgRejects_Type=Counter64
_CifIkeGlobalOutP2ExchgRejects_Object=MibTableColumn
cifIkeGlobalOutP2ExchgRejects=_CifIkeGlobalOutP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,6),_CifIkeGlobalOutP2ExchgRejects_Type())
cifIkeGlobalOutP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutP2ExchgRejects.setUnits(_D)
_CifIkeGlobalInXauths_Type=Counter64
_CifIkeGlobalInXauths_Object=MibTableColumn
cifIkeGlobalInXauths=_CifIkeGlobalInXauths_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,7),_CifIkeGlobalInXauths_Type())
cifIkeGlobalInXauths.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInXauths.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInXauths.setUnits(_L)
_CifIkeGlobalInXauthFailures_Type=Counter64
_CifIkeGlobalInXauthFailures_Object=MibTableColumn
cifIkeGlobalInXauthFailures=_CifIkeGlobalInXauthFailures_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,8),_CifIkeGlobalInXauthFailures_Type())
cifIkeGlobalInXauthFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInXauthFailures.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInXauthFailures.setUnits(_L)
_CifIkeGlobalOutXauthFailures_Type=Counter64
_CifIkeGlobalOutXauthFailures_Object=MibTableColumn
cifIkeGlobalOutXauthFailures=_CifIkeGlobalOutXauthFailures_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,9),_CifIkeGlobalOutXauthFailures_Type())
cifIkeGlobalOutXauthFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutXauthFailures.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutXauthFailures.setUnits(_L)
_CifIkeGlobalInNewGrpReqs_Type=Counter64
_CifIkeGlobalInNewGrpReqs_Object=MibTableColumn
cifIkeGlobalInNewGrpReqs=_CifIkeGlobalInNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,10),_CifIkeGlobalInNewGrpReqs_Type())
cifIkeGlobalInNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInNewGrpReqs.setUnits(_E)
_CifIkeGlobalOutNewGrpReqs_Type=Counter64
_CifIkeGlobalOutNewGrpReqs_Object=MibTableColumn
cifIkeGlobalOutNewGrpReqs=_CifIkeGlobalOutNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,11),_CifIkeGlobalOutNewGrpReqs_Type())
cifIkeGlobalOutNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutNewGrpReqs.setUnits(_E)
_CifIkeGlobalInNewGrpRejectReqs_Type=Counter64
_CifIkeGlobalInNewGrpRejectReqs_Object=MibTableColumn
cifIkeGlobalInNewGrpRejectReqs=_CifIkeGlobalInNewGrpRejectReqs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,12),_CifIkeGlobalInNewGrpRejectReqs_Type())
cifIkeGlobalInNewGrpRejectReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalInNewGrpRejectReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalInNewGrpRejectReqs.setUnits(_E)
_CifIkeGlobalOutNewGrpRejectReqs_Type=Counter64
_CifIkeGlobalOutNewGrpRejectReqs_Object=MibTableColumn
cifIkeGlobalOutNewGrpRejectReqs=_CifIkeGlobalOutNewGrpRejectReqs_Object((1,3,6,1,4,1,9,9,429,1,1,1,1,13),_CifIkeGlobalOutNewGrpRejectReqs_Type())
cifIkeGlobalOutNewGrpRejectReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeGlobalOutNewGrpRejectReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeGlobalOutNewGrpRejectReqs.setUnits(_E)
_CifIkeTunnelTable_Object=MibTable
cifIkeTunnelTable=_CifIkeTunnelTable_Object((1,3,6,1,4,1,9,9,429,1,1,3))
if mibBuilder.loadTexts:cifIkeTunnelTable.setStatus(_A)
_CifIkeTunnelEntry_Object=MibTableRow
cifIkeTunnelEntry=_CifIkeTunnelEntry_Object((1,3,6,1,4,1,9,9,429,1,1,3,1))
cifIkeTunnelEntry.setIndexNames((0,_F,_H),(0,_F,_N))
if mibBuilder.loadTexts:cifIkeTunnelEntry.setStatus(_A)
_CifIkeTunNegoMode_Type=CIPsecIkeNegoMode
_CifIkeTunNegoMode_Object=MibTableColumn
cifIkeTunNegoMode=_CifIkeTunNegoMode_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,1),_CifIkeTunNegoMode_Type())
cifIkeTunNegoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunNegoMode.setStatus(_A)
_CifIkeTunDHGrp_Type=CIPsecDiffHellmanGrp
_CifIkeTunDHGrp_Object=MibTableColumn
cifIkeTunDHGrp=_CifIkeTunDHGrp_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,2),_CifIkeTunDHGrp_Type())
cifIkeTunDHGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunDHGrp.setStatus(_A)
class _CifIkeTunSaRefreshThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CifIkeTunSaRefreshThreshold_Type.__name__=_O
_CifIkeTunSaRefreshThreshold_Object=MibTableColumn
cifIkeTunSaRefreshThreshold=_CifIkeTunSaRefreshThreshold_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,3),_CifIkeTunSaRefreshThreshold_Type())
cifIkeTunSaRefreshThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunSaRefreshThreshold.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunSaRefreshThreshold.setUnits('seconds')
_CifIkeTunTotalRefreshes_Type=Counter32
_CifIkeTunTotalRefreshes_Object=MibTableColumn
cifIkeTunTotalRefreshes=_CifIkeTunTotalRefreshes_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,4),_CifIkeTunTotalRefreshes_Type())
cifIkeTunTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunTotalRefreshes.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunTotalRefreshes.setUnits(_P)
_CifIkeTunInP2Exchgs_Type=Counter32
_CifIkeTunInP2Exchgs_Object=MibTableColumn
cifIkeTunInP2Exchgs=_CifIkeTunInP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,5),_CifIkeTunInP2Exchgs_Type())
cifIkeTunInP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInP2Exchgs.setUnits(_D)
_CifIkeTunInP2ExchgInvalids_Type=Counter32
_CifIkeTunInP2ExchgInvalids_Object=MibTableColumn
cifIkeTunInP2ExchgInvalids=_CifIkeTunInP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,6),_CifIkeTunInP2ExchgInvalids_Type())
cifIkeTunInP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInP2ExchgInvalids.setUnits(_D)
_CifIkeTunInP2ExchgRejects_Type=Counter32
_CifIkeTunInP2ExchgRejects_Object=MibTableColumn
cifIkeTunInP2ExchgRejects=_CifIkeTunInP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,7),_CifIkeTunInP2ExchgRejects_Type())
cifIkeTunInP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInP2ExchgRejects.setUnits(_D)
_CifIkeTunInP2SaDelRequests_Type=Counter32
_CifIkeTunInP2SaDelRequests_Object=MibTableColumn
cifIkeTunInP2SaDelRequests=_CifIkeTunInP2SaDelRequests_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,8),_CifIkeTunInP2SaDelRequests_Type())
cifIkeTunInP2SaDelRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInP2SaDelRequests.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInP2SaDelRequests.setUnits(_Q)
_CifIkeTunOutP2Exchgs_Type=Counter32
_CifIkeTunOutP2Exchgs_Object=MibTableColumn
cifIkeTunOutP2Exchgs=_CifIkeTunOutP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,9),_CifIkeTunOutP2Exchgs_Type())
cifIkeTunOutP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutP2Exchgs.setUnits(_D)
_CifIkeTunOutP2ExchgInvalids_Type=Counter32
_CifIkeTunOutP2ExchgInvalids_Object=MibTableColumn
cifIkeTunOutP2ExchgInvalids=_CifIkeTunOutP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,10),_CifIkeTunOutP2ExchgInvalids_Type())
cifIkeTunOutP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutP2ExchgInvalids.setUnits(_D)
_CifIkeTunOutP2ExchgRejects_Type=Counter32
_CifIkeTunOutP2ExchgRejects_Object=MibTableColumn
cifIkeTunOutP2ExchgRejects=_CifIkeTunOutP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,11),_CifIkeTunOutP2ExchgRejects_Type())
cifIkeTunOutP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutP2ExchgRejects.setUnits(_D)
_CifIkeTunInNewGrpReqs_Type=Counter32
_CifIkeTunInNewGrpReqs_Object=MibTableColumn
cifIkeTunInNewGrpReqs=_CifIkeTunInNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,12),_CifIkeTunInNewGrpReqs_Type())
cifIkeTunInNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInNewGrpReqs.setUnits(_E)
_CifIkeTunOutNewGrpReqs_Type=Counter32
_CifIkeTunOutNewGrpReqs_Object=MibTableColumn
cifIkeTunOutNewGrpReqs=_CifIkeTunOutNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,13),_CifIkeTunOutNewGrpReqs_Type())
cifIkeTunOutNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutNewGrpReqs.setUnits(_E)
_CifIkeTunInNewGrpRejectedReqs_Type=Counter32
_CifIkeTunInNewGrpRejectedReqs_Object=MibTableColumn
cifIkeTunInNewGrpRejectedReqs=_CifIkeTunInNewGrpRejectedReqs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,14),_CifIkeTunInNewGrpRejectedReqs_Type())
cifIkeTunInNewGrpRejectedReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInNewGrpRejectedReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInNewGrpRejectedReqs.setUnits(_E)
_CifIkeTunOutNewGrpRejectedReqs_Type=Counter32
_CifIkeTunOutNewGrpRejectedReqs_Object=MibTableColumn
cifIkeTunOutNewGrpRejectedReqs=_CifIkeTunOutNewGrpRejectedReqs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,15),_CifIkeTunOutNewGrpRejectedReqs_Type())
cifIkeTunOutNewGrpRejectedReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutNewGrpRejectedReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutNewGrpRejectedReqs.setUnits(_E)
_CifIkeTunInConfigs_Type=Counter32
_CifIkeTunInConfigs_Object=MibTableColumn
cifIkeTunInConfigs=_CifIkeTunInConfigs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,16),_CifIkeTunInConfigs_Type())
cifIkeTunInConfigs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInConfigs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInConfigs.setUnits(_G)
_CifIkeTunOutConfigs_Type=Counter32
_CifIkeTunOutConfigs_Object=MibTableColumn
cifIkeTunOutConfigs=_CifIkeTunOutConfigs_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,17),_CifIkeTunOutConfigs_Type())
cifIkeTunOutConfigs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutConfigs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutConfigs.setUnits(_G)
_CifIkeTunInConfigRejects_Type=Counter32
_CifIkeTunInConfigRejects_Object=MibTableColumn
cifIkeTunInConfigRejects=_CifIkeTunInConfigRejects_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,18),_CifIkeTunInConfigRejects_Type())
cifIkeTunInConfigRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunInConfigRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunInConfigRejects.setUnits(_G)
_CifIkeTunOutConfigRejects_Type=Counter32
_CifIkeTunOutConfigRejects_Object=MibTableColumn
cifIkeTunOutConfigRejects=_CifIkeTunOutConfigRejects_Object((1,3,6,1,4,1,9,9,429,1,1,3,1,19),_CifIkeTunOutConfigRejects_Type())
cifIkeTunOutConfigRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunOutConfigRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunOutConfigRejects.setUnits(_G)
_CifIkeHistory_ObjectIdentity=ObjectIdentity
cifIkeHistory=_CifIkeHistory_ObjectIdentity((1,3,6,1,4,1,9,9,429,1,2))
_CifIkeTunnelHistTable_Object=MibTable
cifIkeTunnelHistTable=_CifIkeTunnelHistTable_Object((1,3,6,1,4,1,9,9,429,1,2,1))
if mibBuilder.loadTexts:cifIkeTunnelHistTable.setStatus(_A)
_CifIkeTunnelHistEntry_Object=MibTableRow
cifIkeTunnelHistEntry=_CifIkeTunnelHistEntry_Object((1,3,6,1,4,1,9,9,429,1,2,1,1))
cifIkeTunnelHistEntry.setIndexNames((0,_F,_H),(0,_F,_M))
if mibBuilder.loadTexts:cifIkeTunnelHistEntry.setStatus(_A)
_CifIkeTunHistNegoMode_Type=CIPsecIkeNegoMode
_CifIkeTunHistNegoMode_Object=MibTableColumn
cifIkeTunHistNegoMode=_CifIkeTunHistNegoMode_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,1),_CifIkeTunHistNegoMode_Type())
cifIkeTunHistNegoMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistNegoMode.setStatus(_A)
_CifIkeTunHistDHGrp_Type=CIPsecDiffHellmanGrp
_CifIkeTunHistDHGrp_Object=MibTableColumn
cifIkeTunHistDHGrp=_CifIkeTunHistDHGrp_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,2),_CifIkeTunHistDHGrp_Type())
cifIkeTunHistDHGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistDHGrp.setStatus(_A)
_CifIkeTunHistTotalRefreshes_Type=Counter32
_CifIkeTunHistTotalRefreshes_Object=MibTableColumn
cifIkeTunHistTotalRefreshes=_CifIkeTunHistTotalRefreshes_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,3),_CifIkeTunHistTotalRefreshes_Type())
cifIkeTunHistTotalRefreshes.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistTotalRefreshes.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistTotalRefreshes.setUnits(_P)
_CifIkeTunHistTotalSas_Type=Counter32
_CifIkeTunHistTotalSas_Object=MibTableColumn
cifIkeTunHistTotalSas=_CifIkeTunHistTotalSas_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,4),_CifIkeTunHistTotalSas_Type())
cifIkeTunHistTotalSas.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistTotalSas.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistTotalSas.setUnits('SAs')
_CifIkeTunHistInP2Exchgs_Type=Counter32
_CifIkeTunHistInP2Exchgs_Object=MibTableColumn
cifIkeTunHistInP2Exchgs=_CifIkeTunHistInP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,5),_CifIkeTunHistInP2Exchgs_Type())
cifIkeTunHistInP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInP2Exchgs.setUnits(_D)
_CifIkeTunHistInP2ExchgInvalids_Type=Counter32
_CifIkeTunHistInP2ExchgInvalids_Object=MibTableColumn
cifIkeTunHistInP2ExchgInvalids=_CifIkeTunHistInP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,6),_CifIkeTunHistInP2ExchgInvalids_Type())
cifIkeTunHistInP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInP2ExchgInvalids.setUnits(_D)
_CifIkeTunHistInP2ExchgRejects_Type=Counter32
_CifIkeTunHistInP2ExchgRejects_Object=MibTableColumn
cifIkeTunHistInP2ExchgRejects=_CifIkeTunHistInP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,7),_CifIkeTunHistInP2ExchgRejects_Type())
cifIkeTunHistInP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInP2ExchgRejects.setUnits(_D)
_CifIkeTunHistOutP2Exchgs_Type=Counter32
_CifIkeTunHistOutP2Exchgs_Object=MibTableColumn
cifIkeTunHistOutP2Exchgs=_CifIkeTunHistOutP2Exchgs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,8),_CifIkeTunHistOutP2Exchgs_Type())
cifIkeTunHistOutP2Exchgs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutP2Exchgs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutP2Exchgs.setUnits(_Q)
_CifIkeTunHistOutP2ExchgInvalids_Type=Counter32
_CifIkeTunHistOutP2ExchgInvalids_Object=MibTableColumn
cifIkeTunHistOutP2ExchgInvalids=_CifIkeTunHistOutP2ExchgInvalids_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,9),_CifIkeTunHistOutP2ExchgInvalids_Type())
cifIkeTunHistOutP2ExchgInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutP2ExchgInvalids.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutP2ExchgInvalids.setUnits(_D)
_CifIkeTunHistOutP2ExchgRejects_Type=Counter32
_CifIkeTunHistOutP2ExchgRejects_Object=MibTableColumn
cifIkeTunHistOutP2ExchgRejects=_CifIkeTunHistOutP2ExchgRejects_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,10),_CifIkeTunHistOutP2ExchgRejects_Type())
cifIkeTunHistOutP2ExchgRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutP2ExchgRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutP2ExchgRejects.setUnits(_D)
_CifIkeTunHistInNewGrpReqs_Type=Counter32
_CifIkeTunHistInNewGrpReqs_Object=MibTableColumn
cifIkeTunHistInNewGrpReqs=_CifIkeTunHistInNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,11),_CifIkeTunHistInNewGrpReqs_Type())
cifIkeTunHistInNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInNewGrpReqs.setUnits(_E)
_CifIkeTunHistOutNewGrpReqs_Type=Counter32
_CifIkeTunHistOutNewGrpReqs_Object=MibTableColumn
cifIkeTunHistOutNewGrpReqs=_CifIkeTunHistOutNewGrpReqs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,12),_CifIkeTunHistOutNewGrpReqs_Type())
cifIkeTunHistOutNewGrpReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutNewGrpReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutNewGrpReqs.setUnits(_E)
_CifIkeTunHistInNewGrpRejectReqs_Type=Counter32
_CifIkeTunHistInNewGrpRejectReqs_Object=MibTableColumn
cifIkeTunHistInNewGrpRejectReqs=_CifIkeTunHistInNewGrpRejectReqs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,13),_CifIkeTunHistInNewGrpRejectReqs_Type())
cifIkeTunHistInNewGrpRejectReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInNewGrpRejectReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInNewGrpRejectReqs.setUnits(_E)
_CifIkeTunHistOutNewGrpRejectReqs_Type=Counter32
_CifIkeTunHistOutNewGrpRejectReqs_Object=MibTableColumn
cifIkeTunHistOutNewGrpRejectReqs=_CifIkeTunHistOutNewGrpRejectReqs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,14),_CifIkeTunHistOutNewGrpRejectReqs_Type())
cifIkeTunHistOutNewGrpRejectReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutNewGrpRejectReqs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutNewGrpRejectReqs.setUnits(_E)
_CifIkeTunHistInConfigs_Type=Counter32
_CifIkeTunHistInConfigs_Object=MibTableColumn
cifIkeTunHistInConfigs=_CifIkeTunHistInConfigs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,15),_CifIkeTunHistInConfigs_Type())
cifIkeTunHistInConfigs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInConfigs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInConfigs.setUnits(_G)
_CifIkeTunHistOutConfigs_Type=Counter32
_CifIkeTunHistOutConfigs_Object=MibTableColumn
cifIkeTunHistOutConfigs=_CifIkeTunHistOutConfigs_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,16),_CifIkeTunHistOutConfigs_Type())
cifIkeTunHistOutConfigs.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutConfigs.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutConfigs.setUnits(_G)
_CifIkeTunHistInConfigsRejects_Type=Counter32
_CifIkeTunHistInConfigsRejects_Object=MibTableColumn
cifIkeTunHistInConfigsRejects=_CifIkeTunHistInConfigsRejects_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,17),_CifIkeTunHistInConfigsRejects_Type())
cifIkeTunHistInConfigsRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistInConfigsRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistInConfigsRejects.setUnits(_G)
_CifIkeTunHistOutConfigsRejects_Type=Counter32
_CifIkeTunHistOutConfigsRejects_Object=MibTableColumn
cifIkeTunHistOutConfigsRejects=_CifIkeTunHistOutConfigsRejects_Object((1,3,6,1,4,1,9,9,429,1,2,1,1,18),_CifIkeTunHistOutConfigsRejects_Type())
cifIkeTunHistOutConfigsRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:cifIkeTunHistOutConfigsRejects.setStatus(_A)
if mibBuilder.loadTexts:cifIkeTunHistOutConfigsRejects.setUnits(_G)
_CifIkeNotifControl_ObjectIdentity=ObjectIdentity
cifIkeNotifControl=_CifIkeNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,429,1,3))
class _CifIkeNotifCntlInNewGrpRejected_Type(TruthValue):defaultValue=2
_CifIkeNotifCntlInNewGrpRejected_Type.__name__=_K
_CifIkeNotifCntlInNewGrpRejected_Object=MibScalar
cifIkeNotifCntlInNewGrpRejected=_CifIkeNotifCntlInNewGrpRejected_Object((1,3,6,1,4,1,9,9,429,1,3,1),_CifIkeNotifCntlInNewGrpRejected_Type())
cifIkeNotifCntlInNewGrpRejected.setMaxAccess(_R)
if mibBuilder.loadTexts:cifIkeNotifCntlInNewGrpRejected.setStatus(_A)
class _CifIkeNotifCntlOutNewGrpRejected_Type(TruthValue):defaultValue=2
_CifIkeNotifCntlOutNewGrpRejected_Type.__name__=_K
_CifIkeNotifCntlOutNewGrpRejected_Object=MibScalar
cifIkeNotifCntlOutNewGrpRejected=_CifIkeNotifCntlOutNewGrpRejected_Object((1,3,6,1,4,1,9,9,429,1,3,2),_CifIkeNotifCntlOutNewGrpRejected_Type())
cifIkeNotifCntlOutNewGrpRejected.setMaxAccess(_R)
if mibBuilder.loadTexts:cifIkeNotifCntlOutNewGrpRejected.setStatus(_A)
_CiscoIkeFlowMIBConform_ObjectIdentity=ObjectIdentity
ciscoIkeFlowMIBConform=_CiscoIkeFlowMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,429,2))
_CiscoIkeFlowMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIkeFlowMIBCompliances=_CiscoIkeFlowMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,429,2,1))
_CiscoIkeFlowMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIkeFlowMIBGroups=_CiscoIkeFlowMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,429,2,2))
ciscoIkeFlowActivityGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,1))
ciscoIkeFlowActivityGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ciscoIkeFlowActivityGroup.setStatus(_A)
cifIkeFlowNewGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,2))
cifIkeFlowNewGroupGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cifIkeFlowNewGroupGroup.setStatus(_A)
cifIkeFlowXauthGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,3))
cifIkeFlowXauthGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cifIkeFlowXauthGroup.setStatus(_A)
cifIkeFlowModeConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,4))
cifIkeFlowModeConfigGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:cifIkeFlowModeConfigGroup.setStatus(_A)
cifIkeFlowHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,5))
cifIkeFlowHistoryGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:cifIkeFlowHistoryGroup.setStatus(_A)
cifIkeFlowNewGroupHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,6))
cifIkeFlowNewGroupHistoryGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cifIkeFlowNewGroupHistoryGroup.setStatus(_A)
cifIkeFlowModeConfigHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,7))
cifIkeFlowModeConfigHistoryGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:cifIkeFlowModeConfigHistoryGroup.setStatus(_A)
cifIkeFlowNotifCntlGroup=ObjectGroup((1,3,6,1,4,1,9,9,429,2,2,8))
cifIkeFlowNotifCntlGroup.setObjects(*((_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cifIkeFlowNotifCntlGroup.setStatus(_A)
ciscoIkeFlowInNewGrpRejected=NotificationType((1,3,6,1,4,1,9,9,429,0,1))
ciscoIkeFlowInNewGrpRejected.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:ciscoIkeFlowInNewGrpRejected.setStatus(_A)
ciscoIkeFlowOutNewGrpRejected=NotificationType((1,3,6,1,4,1,9,9,429,0,2))
ciscoIkeFlowOutNewGrpRejected.setObjects(*((_F,_I),(_F,_J)))
if mibBuilder.loadTexts:ciscoIkeFlowOutNewGrpRejected.setStatus(_A)
cifIkeFlowNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,429,2,2,9))
cifIkeFlowNotificationGroup.setObjects(*((_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cifIkeFlowNotificationGroup.setStatus(_A)
ciscoIkeFlowMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,429,2,1,1))
ciscoIkeFlowMIBCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:ciscoIkeFlowMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIkeFlowMIB':ciscoIkeFlowMIB,'ciscoIkeFlowMIBNotifs':ciscoIkeFlowMIBNotifs,_AI:ciscoIkeFlowInNewGrpRejected,_AJ:ciscoIkeFlowOutNewGrpRejected,'ciscoIkeFlowMIBObjects':ciscoIkeFlowMIBObjects,'cifIkeCurrentActivity':cifIkeCurrentActivity,'cifIkeGlobalStatsTable':cifIkeGlobalStatsTable,'cifIkeGlobalStatsEntry':cifIkeGlobalStatsEntry,_S:cifIkeGlobalInP2Exchgs,_T:cifIkeGlobalInP2ExchgInvalids,_U:cifIkeGlobalInP2ExchgRejects,_V:cifIkeGlobalOutP2Exchgs,_W:cifIkeGlobalOutP2ExchgInvalids,_X:cifIkeGlobalOutP2ExchgRejects,_r:cifIkeGlobalInXauths,_s:cifIkeGlobalInXauthFailures,_t:cifIkeGlobalOutXauthFailures,_j:cifIkeGlobalInNewGrpReqs,_k:cifIkeGlobalOutNewGrpReqs,_l:cifIkeGlobalInNewGrpRejectReqs,_m:cifIkeGlobalOutNewGrpRejectReqs,'cifIkeTunnelTable':cifIkeTunnelTable,'cifIkeTunnelEntry':cifIkeTunnelEntry,_Y:cifIkeTunNegoMode,_Z:cifIkeTunDHGrp,_a:cifIkeTunSaRefreshThreshold,_b:cifIkeTunTotalRefreshes,_c:cifIkeTunInP2Exchgs,_d:cifIkeTunInP2ExchgInvalids,_e:cifIkeTunInP2ExchgRejects,_f:cifIkeTunInP2SaDelRequests,_g:cifIkeTunOutP2Exchgs,_h:cifIkeTunOutP2ExchgInvalids,_i:cifIkeTunOutP2ExchgRejects,_n:cifIkeTunInNewGrpReqs,_o:cifIkeTunOutNewGrpReqs,_p:cifIkeTunInNewGrpRejectedReqs,_q:cifIkeTunOutNewGrpRejectedReqs,_u:cifIkeTunInConfigs,_v:cifIkeTunOutConfigs,_w:cifIkeTunInConfigRejects,_x:cifIkeTunOutConfigRejects,'cifIkeHistory':cifIkeHistory,'cifIkeTunnelHistTable':cifIkeTunnelHistTable,'cifIkeTunnelHistEntry':cifIkeTunnelHistEntry,_y:cifIkeTunHistNegoMode,_z:cifIkeTunHistDHGrp,_A0:cifIkeTunHistTotalRefreshes,_A1:cifIkeTunHistTotalSas,_A2:cifIkeTunHistInP2Exchgs,_A3:cifIkeTunHistInP2ExchgInvalids,_A4:cifIkeTunHistInP2ExchgRejects,_A5:cifIkeTunHistOutP2Exchgs,_A6:cifIkeTunHistOutP2ExchgInvalids,_A7:cifIkeTunHistOutP2ExchgRejects,_A8:cifIkeTunHistInNewGrpReqs,_A9:cifIkeTunHistOutNewGrpReqs,_AA:cifIkeTunHistInNewGrpRejectReqs,_AB:cifIkeTunHistOutNewGrpRejectReqs,_AC:cifIkeTunHistInConfigs,_AD:cifIkeTunHistOutConfigs,_AE:cifIkeTunHistInConfigsRejects,_AF:cifIkeTunHistOutConfigsRejects,'cifIkeNotifControl':cifIkeNotifControl,_AG:cifIkeNotifCntlInNewGrpRejected,_AH:cifIkeNotifCntlOutNewGrpRejected,'ciscoIkeFlowMIBConform':ciscoIkeFlowMIBConform,'ciscoIkeFlowMIBCompliances':ciscoIkeFlowMIBCompliances,'ciscoIkeFlowMIBCompliance':ciscoIkeFlowMIBCompliance,'ciscoIkeFlowMIBGroups':ciscoIkeFlowMIBGroups,_AK:ciscoIkeFlowActivityGroup,_AL:cifIkeFlowNewGroupGroup,_AM:cifIkeFlowXauthGroup,_AN:cifIkeFlowModeConfigGroup,_AO:cifIkeFlowHistoryGroup,_AP:cifIkeFlowNewGroupHistoryGroup,_AQ:cifIkeFlowModeConfigHistoryGroup,_AS:cifIkeFlowNotifCntlGroup,_AR:cifIkeFlowNotificationGroup})