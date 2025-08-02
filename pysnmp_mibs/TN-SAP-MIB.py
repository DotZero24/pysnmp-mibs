_A0='tnSapTlsStpException'
_z='tnSapTlsStpRootGuardViolation'
_y='tnSapTlsStpOperProtocol'
_x='tnSapOperFlags'
_w='tnSapOperStatus'
_v='tnSapAdminStatus'
_u='seconds'
_t='dynamic'
_s='iesIfAdminDown'
_r='svcAdminDown'
_q='portMtuTooSmall'
_p='egressQosMismatch'
_o='ingressQosMismatch'
_n='not-accessible'
_m='TSapIngressPolicyID'
_l='TSapEgressPolicyID'
_k='TIngHsmdaPerPacketOffsetOvr'
_j='TFdbTableSizeProfileID'
_i='TEgrHsmdaPerPacketOffsetOvr'
_h='ServObjDesc'
_g='SapLoopbackMode'
_f='TlsLimitMacMoveLevel'
_e='TlsLimitMacMove'
_d='TlsBpduTranslation'
_c='DisplayString'
_b='OctetString'
_a='pvst'
_Z='TPortSchedulerPIR'
_Y='TPolicyStatementNameOrEmpty'
_X='ServiceAdminStatus'
_W='L2ptProtocols'
_V='deci-seconds'
_U='disabled'
_T='tnSysSwitchId'
_S='TROPIC-SYSTEM-MIB'
_R='TNamedItemOrEmpty'
_Q='tnSvcVpnId'
_P='TFilterID'
_O='TmnxEnabledDisabled'
_N='ServObjName'
_M='tnCustId'
_L='Unsigned32'
_K='TruthValue'
_J='tnSapEncapValue'
_I='tnSapPortId'
_H='tnSvcId'
_G='Integer32'
_F='TN-SERV-MIB'
_E='TN-SAP-MIB'
_D='read-write'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_b,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_c,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_K)
BridgeId,L2ptProtocols,MstiInstanceIdOrZero,MvplsPruneState,ServObjName,ServType,StpExceptionCondition,StpPortRole,StpProtocol,TStpPortState,TlsBpduTranslation,TlsLimitMacMove,TlsLimitMacMoveLevel,VpnId,tnCustId,tnServNotifications,tnServObjs,tnSvcId,tnSvcVpnId,tnTstpTraps=mibBuilder.importSymbols(_F,'BridgeId',_W,'MstiInstanceIdOrZero','MvplsPruneState',_N,'ServType','StpExceptionCondition','StpPortRole','StpProtocol','TStpPortState',_d,_e,_f,'VpnId',_M,'tnServNotifications','tnServObjs',_H,_Q,'tnTstpTraps')
SapLoopbackMode,ServObjDesc,ServiceAdminStatus,TCpmProtPolicyID,TEgrHsmdaPerPacketOffsetOvr,TFdbTableSizeProfileID,TFilterID,TIngHsmdaPerPacketOffsetOvr,TNamedItemOrEmpty,TPolicyStatementNameOrEmpty,TPortSchedulerPIR,TSapEgressPolicyID,TSapIngressPolicyID,TmnxCustId,TmnxEnabledDisabled,TmnxEncapVal,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TN-TC-MIB',_g,_h,_X,'TCpmProtPolicyID',_i,_j,_P,_k,_R,_Y,_Z,_l,_m,'TmnxCustId',_O,'TmnxEncapVal','TmnxPortID','TmnxServId')
tnSRMIBModules,=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules')
tnSysSwitchId,=mibBuilder.importSymbols(_S,_T)
tnSvcSapMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,55))
if mibBuilder.loadTexts:tnSvcSapMIBModule.setRevisions(('2020-11-13 00:00','2020-11-06 00:00','2020-09-25 00:00','2020-08-14 00:00','2019-09-13 00:00','2019-08-16 00:00','2017-07-07 00:00','2016-02-15 00:00','2012-12-05 00:00','2012-09-01 00:00','2009-02-28 00:00','2008-07-01 00:00','2007-10-01 00:00'))
_TnSapObjs_ObjectIdentity=ObjectIdentity
tnSapObjs=_TnSapObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,4,3))
_TnSapBaseInfoTable_Object=MibTable
tnSapBaseInfoTable=_TnSapBaseInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2))
if mibBuilder.loadTexts:tnSapBaseInfoTable.setStatus(_A)
_TnSapBaseInfoEntry_Object=MibTableRow
tnSapBaseInfoEntry=_TnSapBaseInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1))
tnSapBaseInfoEntry.setIndexNames((0,_S,_T),(0,_F,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:tnSapBaseInfoEntry.setStatus(_A)
_TnSapPortId_Type=TmnxPortID
_TnSapPortId_Object=MibTableColumn
tnSapPortId=_TnSapPortId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,1),_TnSapPortId_Type())
tnSapPortId.setMaxAccess(_n)
if mibBuilder.loadTexts:tnSapPortId.setStatus(_A)
_TnSapEncapValue_Type=TmnxEncapVal
_TnSapEncapValue_Object=MibTableColumn
tnSapEncapValue=_TnSapEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,2),_TnSapEncapValue_Type())
tnSapEncapValue.setMaxAccess(_n)
if mibBuilder.loadTexts:tnSapEncapValue.setStatus(_A)
_TnSapRowStatus_Type=RowStatus
_TnSapRowStatus_Object=MibTableColumn
tnSapRowStatus=_TnSapRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,3),_TnSapRowStatus_Type())
tnSapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapRowStatus.setStatus(_A)
_TnSapType_Type=ServType
_TnSapType_Object=MibTableColumn
tnSapType=_TnSapType_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,4),_TnSapType_Type())
tnSapType.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapType.setStatus(_A)
class _TnSapDescription_Type(ServObjDesc):defaultValue=OctetString('')
_TnSapDescription_Type.__name__=_h
_TnSapDescription_Object=MibTableColumn
tnSapDescription=_TnSapDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,5),_TnSapDescription_Type())
tnSapDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapDescription.setStatus(_A)
class _TnSapAdminStatus_Type(ServiceAdminStatus):defaultValue=1
_TnSapAdminStatus_Type.__name__=_X
_TnSapAdminStatus_Object=MibTableColumn
tnSapAdminStatus=_TnSapAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,6),_TnSapAdminStatus_Type())
tnSapAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapAdminStatus.setStatus(_A)
class _TnSapOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_o,3),(_p,4),(_q,5),(_r,6),(_s,7)))
_TnSapOperStatus_Type.__name__=_G
_TnSapOperStatus_Object=MibTableColumn
tnSapOperStatus=_TnSapOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,7),_TnSapOperStatus_Type())
tnSapOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapOperStatus.setStatus(_A)
class _TnSapIngressQosPolicyId_Type(TSapIngressPolicyID):defaultValue=1
_TnSapIngressQosPolicyId_Type.__name__=_m
_TnSapIngressQosPolicyId_Object=MibTableColumn
tnSapIngressQosPolicyId=_TnSapIngressQosPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,8),_TnSapIngressQosPolicyId_Type())
tnSapIngressQosPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressQosPolicyId.setStatus(_A)
class _TnSapIngressMacFilterId_Type(TFilterID):defaultValue=0
_TnSapIngressMacFilterId_Type.__name__=_P
_TnSapIngressMacFilterId_Object=MibTableColumn
tnSapIngressMacFilterId=_TnSapIngressMacFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,9),_TnSapIngressMacFilterId_Type())
tnSapIngressMacFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressMacFilterId.setStatus(_A)
class _TnSapIngressIpFilterId_Type(TFilterID):defaultValue=0
_TnSapIngressIpFilterId_Type.__name__=_P
_TnSapIngressIpFilterId_Object=MibTableColumn
tnSapIngressIpFilterId=_TnSapIngressIpFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,10),_TnSapIngressIpFilterId_Type())
tnSapIngressIpFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressIpFilterId.setStatus(_A)
class _TnSapEgressQosPolicyId_Type(TSapEgressPolicyID):defaultValue=1
_TnSapEgressQosPolicyId_Type.__name__=_l
_TnSapEgressQosPolicyId_Object=MibTableColumn
tnSapEgressQosPolicyId=_TnSapEgressQosPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,11),_TnSapEgressQosPolicyId_Type())
tnSapEgressQosPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressQosPolicyId.setStatus(_A)
class _TnSapEgressMacFilterId_Type(TFilterID):defaultValue=0
_TnSapEgressMacFilterId_Type.__name__=_P
_TnSapEgressMacFilterId_Object=MibTableColumn
tnSapEgressMacFilterId=_TnSapEgressMacFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,12),_TnSapEgressMacFilterId_Type())
tnSapEgressMacFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressMacFilterId.setStatus(_A)
class _TnSapEgressIpFilterId_Type(TFilterID):defaultValue=0
_TnSapEgressIpFilterId_Type.__name__=_P
_TnSapEgressIpFilterId_Object=MibTableColumn
tnSapEgressIpFilterId=_TnSapEgressIpFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,13),_TnSapEgressIpFilterId_Type())
tnSapEgressIpFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressIpFilterId.setStatus(_A)
class _TnSapMirrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ingress',1),('egress',2),('ingressAndEgress',3),(_U,4)))
_TnSapMirrorStatus_Type.__name__=_G
_TnSapMirrorStatus_Object=MibTableColumn
tnSapMirrorStatus=_TnSapMirrorStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,14),_TnSapMirrorStatus_Type())
tnSapMirrorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMirrorStatus.setStatus(_A)
_TnSapIesIfIndex_Type=InterfaceIndexOrZero
_TnSapIesIfIndex_Object=MibTableColumn
tnSapIesIfIndex=_TnSapIesIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,15),_TnSapIesIfIndex_Type())
tnSapIesIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIesIfIndex.setStatus(_A)
_TnSapLastMgmtChange_Type=TimeStamp
_TnSapLastMgmtChange_Object=MibTableColumn
tnSapLastMgmtChange=_TnSapLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,16),_TnSapLastMgmtChange_Type())
tnSapLastMgmtChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapLastMgmtChange.setStatus(_A)
class _TnSapCollectAcctStats_Type(TruthValue):defaultValue=2
_TnSapCollectAcctStats_Type.__name__=_K
_TnSapCollectAcctStats_Object=MibTableColumn
tnSapCollectAcctStats=_TnSapCollectAcctStats_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,17),_TnSapCollectAcctStats_Type())
tnSapCollectAcctStats.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapCollectAcctStats.setStatus(_A)
class _TnSapAccountingPolicyId_Type(Unsigned32):defaultValue=0
_TnSapAccountingPolicyId_Type.__name__=_L
_TnSapAccountingPolicyId_Object=MibTableColumn
tnSapAccountingPolicyId=_TnSapAccountingPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,18),_TnSapAccountingPolicyId_Type())
tnSapAccountingPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapAccountingPolicyId.setStatus(_A)
_TnSapVpnId_Type=VpnId
_TnSapVpnId_Object=MibTableColumn
tnSapVpnId=_TnSapVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,19),_TnSapVpnId_Type())
tnSapVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapVpnId.setStatus(_A)
_TnSapCustId_Type=TmnxCustId
_TnSapCustId_Object=MibTableColumn
tnSapCustId=_TnSapCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,20),_TnSapCustId_Type())
tnSapCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapCustId.setStatus(_A)
class _TnSapCustMultSvcSite_Type(ServObjName):defaultValue=OctetString('')
_TnSapCustMultSvcSite_Type.__name__=_N
_TnSapCustMultSvcSite_Object=MibTableColumn
tnSapCustMultSvcSite=_TnSapCustMultSvcSite_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,21),_TnSapCustMultSvcSite_Type())
tnSapCustMultSvcSite.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapCustMultSvcSite.setStatus(_A)
class _TnSapIngressQosSchedulerPolicy_Type(ServObjName):defaultValue=OctetString('')
_TnSapIngressQosSchedulerPolicy_Type.__name__=_N
_TnSapIngressQosSchedulerPolicy_Object=MibTableColumn
tnSapIngressQosSchedulerPolicy=_TnSapIngressQosSchedulerPolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,22),_TnSapIngressQosSchedulerPolicy_Type())
tnSapIngressQosSchedulerPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressQosSchedulerPolicy.setStatus(_A)
class _TnSapEgressQosSchedulerPolicy_Type(ServObjName):defaultValue=OctetString('')
_TnSapEgressQosSchedulerPolicy_Type.__name__=_N
_TnSapEgressQosSchedulerPolicy_Object=MibTableColumn
tnSapEgressQosSchedulerPolicy=_TnSapEgressQosSchedulerPolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,23),_TnSapEgressQosSchedulerPolicy_Type())
tnSapEgressQosSchedulerPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressQosSchedulerPolicy.setStatus(_A)
class _TnSapSplitHorizonGrp_Type(ServObjName):defaultValue=OctetString('')
_TnSapSplitHorizonGrp_Type.__name__=_N
_TnSapSplitHorizonGrp_Object=MibTableColumn
tnSapSplitHorizonGrp=_TnSapSplitHorizonGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,24),_TnSapSplitHorizonGrp_Type())
tnSapSplitHorizonGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapSplitHorizonGrp.setStatus(_A)
class _TnSapIngressSharedQueuePolicy_Type(ServObjName):defaultValue=OctetString('')
_TnSapIngressSharedQueuePolicy_Type.__name__=_N
_TnSapIngressSharedQueuePolicy_Object=MibTableColumn
tnSapIngressSharedQueuePolicy=_TnSapIngressSharedQueuePolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,25),_TnSapIngressSharedQueuePolicy_Type())
tnSapIngressSharedQueuePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressSharedQueuePolicy.setStatus(_A)
class _TnSapIngressMatchQinQDot1PBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('default',1),('top',2),('bottom',3)))
_TnSapIngressMatchQinQDot1PBits_Type.__name__=_G
_TnSapIngressMatchQinQDot1PBits_Object=MibTableColumn
tnSapIngressMatchQinQDot1PBits=_TnSapIngressMatchQinQDot1PBits_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,26),_TnSapIngressMatchQinQDot1PBits_Type())
tnSapIngressMatchQinQDot1PBits.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressMatchQinQDot1PBits.setStatus(_A)
class _TnSapOperFlags_Type(Bits):namedValues=NamedValues(*(('sapAdminDown',0),(_r,1),(_s,2),('portOperDown',3),(_q,4),('l2OperDown',5),(_o,6),(_p,7),('relearnLimitExceeded',8),('recProtSrcMac',9),('subIfAdminDown',10),('sapIpipeNoCeIpAddr',11),('sapTodResourceUnavail',12),('sapTodMssResourceUnavail',13),('sapParamMismatch',14),('sapCemNoEcidOrMacAddr',15),('sapStandbyForMcRing',16),('sapSvcMtuTooSmall',17),('ingressNamedPoolMismatch',18),('egressNamedPoolMismatch',19),('ipMirrorNoMacAddr',20),('sapEpipeNoRingNode',21),('mcStandby',22),('mhStandby',23),('oamDownMepFault',24),('oamUpMepFault',25),('ethTunTagMisconfig',26),('ingressPolicerMismatch',27),('egressPolicerMismatch',28),('sapTlsNoRingNode',29),('ethRingPathBlocked',30),('oamTunnelMepFault',31),('operGrpDown',32),('portBouncing',33),('sapEgressHQosMgmtMismatch',34),('evpnP2mpConflict',35),('l2tpv3TunnelDown',36),('labelStackLimitExceeded',37),('sapIngQGrpRedirMismatch',38),('sapEgrQGrpRedirMismatch',39),('rstpBlocked',40),('bpduGuardBlocked',41)))
_TnSapOperFlags_Type.__name__='Bits'
_TnSapOperFlags_Object=MibTableColumn
tnSapOperFlags=_TnSapOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,27),_TnSapOperFlags_Type())
tnSapOperFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapOperFlags.setStatus(_A)
_TnSapLastStatusChange_Type=TimeStamp
_TnSapLastStatusChange_Object=MibTableColumn
tnSapLastStatusChange=_TnSapLastStatusChange_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,28),_TnSapLastStatusChange_Type())
tnSapLastStatusChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapLastStatusChange.setStatus(_A)
class _TnSapAntiSpoofing_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_U,0),('sourceIpAddr',1),('sourceMacAddr',2),('sourceIpAndMacAddr',3),('nextHopIpAndMacAddr',4)))
_TnSapAntiSpoofing_Type.__name__=_G
_TnSapAntiSpoofing_Object=MibTableColumn
tnSapAntiSpoofing=_TnSapAntiSpoofing_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,29),_TnSapAntiSpoofing_Type())
tnSapAntiSpoofing.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapAntiSpoofing.setStatus(_A)
class _TnSapIngressIpv6FilterId_Type(TFilterID):defaultValue=0
_TnSapIngressIpv6FilterId_Type.__name__=_P
_TnSapIngressIpv6FilterId_Object=MibTableColumn
tnSapIngressIpv6FilterId=_TnSapIngressIpv6FilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,30),_TnSapIngressIpv6FilterId_Type())
tnSapIngressIpv6FilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressIpv6FilterId.setStatus(_A)
class _TnSapEgressIpv6FilterId_Type(TFilterID):defaultValue=0
_TnSapEgressIpv6FilterId_Type.__name__=_P
_TnSapEgressIpv6FilterId_Object=MibTableColumn
tnSapEgressIpv6FilterId=_TnSapEgressIpv6FilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,31),_TnSapEgressIpv6FilterId_Type())
tnSapEgressIpv6FilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressIpv6FilterId.setStatus(_A)
class _TnSapTodSuite_Type(TNamedItemOrEmpty):defaultHexValue=''
_TnSapTodSuite_Type.__name__=_R
_TnSapTodSuite_Object=MibTableColumn
tnSapTodSuite=_TnSapTodSuite_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,32),_TnSapTodSuite_Type())
tnSapTodSuite.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapTodSuite.setStatus(_A)
class _TnSapIngUseMultipointShared_Type(TruthValue):defaultValue=2
_TnSapIngUseMultipointShared_Type.__name__=_K
_TnSapIngUseMultipointShared_Object=MibTableColumn
tnSapIngUseMultipointShared=_TnSapIngUseMultipointShared_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,33),_TnSapIngUseMultipointShared_Type())
tnSapIngUseMultipointShared.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngUseMultipointShared.setStatus(_A)
class _TnSapEgressQinQMarkTopOnly_Type(TruthValue):defaultValue=2
_TnSapEgressQinQMarkTopOnly_Type.__name__=_K
_TnSapEgressQinQMarkTopOnly_Object=MibTableColumn
tnSapEgressQinQMarkTopOnly=_TnSapEgressQinQMarkTopOnly_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,34),_TnSapEgressQinQMarkTopOnly_Type())
tnSapEgressQinQMarkTopOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressQinQMarkTopOnly.setStatus(_A)
class _TnSapEgressAggRateLimit_Type(TPortSchedulerPIR):defaultValue=-1
_TnSapEgressAggRateLimit_Type.__name__=_Z
_TnSapEgressAggRateLimit_Object=MibTableColumn
tnSapEgressAggRateLimit=_TnSapEgressAggRateLimit_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,35),_TnSapEgressAggRateLimit_Type())
tnSapEgressAggRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressAggRateLimit.setStatus(_A)
if mibBuilder.loadTexts:tnSapEgressAggRateLimit.setUnits('kbps')
class _TnSapEndPoint_Type(ServObjName):defaultValue=OctetString('')
_TnSapEndPoint_Type.__name__=_N
_TnSapEndPoint_Object=MibTableColumn
tnSapEndPoint=_TnSapEndPoint_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,36),_TnSapEndPoint_Type())
tnSapEndPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEndPoint.setStatus(_A)
class _TnSapIngressVlanTranslation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('vlanId',2),('copyOuter',3)))
_TnSapIngressVlanTranslation_Type.__name__=_G
_TnSapIngressVlanTranslation_Object=MibTableColumn
tnSapIngressVlanTranslation=_TnSapIngressVlanTranslation_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,37),_TnSapIngressVlanTranslation_Type())
tnSapIngressVlanTranslation.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressVlanTranslation.setStatus(_A)
class _TnSapIngressVlanTranslationId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,4094))
_TnSapIngressVlanTranslationId_Type.__name__=_G
_TnSapIngressVlanTranslationId_Object=MibTableColumn
tnSapIngressVlanTranslationId=_TnSapIngressVlanTranslationId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,38),_TnSapIngressVlanTranslationId_Type())
tnSapIngressVlanTranslationId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressVlanTranslationId.setStatus(_A)
class _TnSapSubType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,5,6,7,8)));namedValues=NamedValues(*(('regular',0),('capture',1),('managed',2),('video',3),('etree-root',5),('etree-leaf',6),('etree-branch',7),('etree-trunk',8)))
_TnSapSubType_Type.__name__=_G
_TnSapSubType_Object=MibTableColumn
tnSapSubType=_TnSapSubType_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,39),_TnSapSubType_Type())
tnSapSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapSubType.setStatus(_A)
_TnSapCpmProtPolicyId_Type=TCpmProtPolicyID
_TnSapCpmProtPolicyId_Object=MibTableColumn
tnSapCpmProtPolicyId=_TnSapCpmProtPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,40),_TnSapCpmProtPolicyId_Type())
tnSapCpmProtPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapCpmProtPolicyId.setStatus(_A)
class _TnSapCpmProtMonitorMac_Type(TruthValue):defaultValue=2
_TnSapCpmProtMonitorMac_Type.__name__=_K
_TnSapCpmProtMonitorMac_Object=MibTableColumn
tnSapCpmProtMonitorMac=_TnSapCpmProtMonitorMac_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,41),_TnSapCpmProtMonitorMac_Type())
tnSapCpmProtMonitorMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapCpmProtMonitorMac.setStatus(_A)
class _TnSapEgressFrameBasedAccounting_Type(TruthValue):defaultValue=2
_TnSapEgressFrameBasedAccounting_Type.__name__=_K
_TnSapEgressFrameBasedAccounting_Object=MibTableColumn
tnSapEgressFrameBasedAccounting=_TnSapEgressFrameBasedAccounting_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,42),_TnSapEgressFrameBasedAccounting_Type())
tnSapEgressFrameBasedAccounting.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressFrameBasedAccounting.setStatus(_A)
class _TnSapIngressAggRateLimit_Type(TPortSchedulerPIR):defaultValue=-1
_TnSapIngressAggRateLimit_Type.__name__=_Z
_TnSapIngressAggRateLimit_Object=MibTableColumn
tnSapIngressAggRateLimit=_TnSapIngressAggRateLimit_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,43),_TnSapIngressAggRateLimit_Type())
tnSapIngressAggRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressAggRateLimit.setStatus(_A)
if mibBuilder.loadTexts:tnSapIngressAggRateLimit.setUnits('kbps')
class _TnSapEgressHsmdaShaperOverride_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnSapEgressHsmdaShaperOverride_Type.__name__=_R
_TnSapEgressHsmdaShaperOverride_Object=MibTableColumn
tnSapEgressHsmdaShaperOverride=_TnSapEgressHsmdaShaperOverride_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,44),_TnSapEgressHsmdaShaperOverride_Type())
tnSapEgressHsmdaShaperOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressHsmdaShaperOverride.setStatus(_A)
class _TnSapIngressHsmdaPacketOffOvr_Type(TIngHsmdaPerPacketOffsetOvr):defaultValue=-128
_TnSapIngressHsmdaPacketOffOvr_Type.__name__=_k
_TnSapIngressHsmdaPacketOffOvr_Object=MibTableColumn
tnSapIngressHsmdaPacketOffOvr=_TnSapIngressHsmdaPacketOffOvr_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,45),_TnSapIngressHsmdaPacketOffOvr_Type())
tnSapIngressHsmdaPacketOffOvr.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIngressHsmdaPacketOffOvr.setStatus(_A)
if mibBuilder.loadTexts:tnSapIngressHsmdaPacketOffOvr.setUnits('bytes')
class _TnSapEgressHsmdaPacketOffOverride_Type(TEgrHsmdaPerPacketOffsetOvr):defaultValue=-128
_TnSapEgressHsmdaPacketOffOverride_Type.__name__=_i
_TnSapEgressHsmdaPacketOffOverride_Object=MibTableColumn
tnSapEgressHsmdaPacketOffOverride=_TnSapEgressHsmdaPacketOffOverride_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,46),_TnSapEgressHsmdaPacketOffOverride_Type())
tnSapEgressHsmdaPacketOffOverride.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEgressHsmdaPacketOffOverride.setStatus(_A)
if mibBuilder.loadTexts:tnSapEgressHsmdaPacketOffOverride.setUnits('bytes')
class _TnSapCallingStationId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_TnSapCallingStationId_Type.__name__=_c
_TnSapCallingStationId_Object=MibTableColumn
tnSapCallingStationId=_TnSapCallingStationId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,47),_TnSapCallingStationId_Type())
tnSapCallingStationId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapCallingStationId.setStatus(_A)
class _TnSapIsaAaApplicationProfile_Type(ServObjName):defaultValue=OctetString('')
_TnSapIsaAaApplicationProfile_Type.__name__=_N
_TnSapIsaAaApplicationProfile_Object=MibTableColumn
tnSapIsaAaApplicationProfile=_TnSapIsaAaApplicationProfile_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,48),_TnSapIsaAaApplicationProfile_Type())
tnSapIsaAaApplicationProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapIsaAaApplicationProfile.setStatus(_A)
class _TnSapEthRingIndex_Type(Unsigned32):defaultValue=0
_TnSapEthRingIndex_Type.__name__=_L
_TnSapEthRingIndex_Object=MibTableColumn
tnSapEthRingIndex=_TnSapEthRingIndex_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,52),_TnSapEthRingIndex_Type())
tnSapEthRingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEthRingIndex.setStatus(_A)
class _TnSapAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSapAlmProfName_Type.__name__=_b
_TnSapAlmProfName_Object=MibTableColumn
tnSapAlmProfName=_TnSapAlmProfName_Object((1,3,6,1,4,1,7483,6,1,2,4,3,2,1,53),_TnSapAlmProfName_Type())
tnSapAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapAlmProfName.setStatus(_A)
_TnSapTlsInfoTable_Object=MibTable
tnSapTlsInfoTable=_TnSapTlsInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3))
if mibBuilder.loadTexts:tnSapTlsInfoTable.setStatus(_A)
_TnSapTlsInfoEntry_Object=MibTableRow
tnSapTlsInfoEntry=_TnSapTlsInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1))
tnSapTlsInfoEntry.setIndexNames((0,_S,_T),(0,_F,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:tnSapTlsInfoEntry.setStatus(_A)
class _TnSapTlsStpAdminStatus_Type(TmnxEnabledDisabled):defaultValue=1
_TnSapTlsStpAdminStatus_Type.__name__=_O
_TnSapTlsStpAdminStatus_Object=MibTableColumn
tnSapTlsStpAdminStatus=_TnSapTlsStpAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,1),_TnSapTlsStpAdminStatus_Type())
tnSapTlsStpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpAdminStatus.setStatus(_A)
class _TnSapTlsStpPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TnSapTlsStpPriority_Type.__name__=_G
_TnSapTlsStpPriority_Object=MibTableColumn
tnSapTlsStpPriority=_TnSapTlsStpPriority_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,2),_TnSapTlsStpPriority_Type())
tnSapTlsStpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpPriority.setStatus(_A)
class _TnSapTlsStpPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_TnSapTlsStpPortNum_Type.__name__=_G
_TnSapTlsStpPortNum_Object=MibTableColumn
tnSapTlsStpPortNum=_TnSapTlsStpPortNum_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,3),_TnSapTlsStpPortNum_Type())
tnSapTlsStpPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpPortNum.setStatus(_A)
class _TnSapTlsStpPathCost_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_TnSapTlsStpPathCost_Type.__name__=_G
_TnSapTlsStpPathCost_Object=MibTableColumn
tnSapTlsStpPathCost=_TnSapTlsStpPathCost_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,4),_TnSapTlsStpPathCost_Type())
tnSapTlsStpPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpPathCost.setStatus(_A)
class _TnSapTlsStpRapidStart_Type(TmnxEnabledDisabled):defaultValue=2
_TnSapTlsStpRapidStart_Type.__name__=_O
_TnSapTlsStpRapidStart_Object=MibTableColumn
tnSapTlsStpRapidStart=_TnSapTlsStpRapidStart_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,5),_TnSapTlsStpRapidStart_Type())
tnSapTlsStpRapidStart.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpRapidStart.setStatus(_A)
class _TnSapTlsStpBpduEncap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),('dot1d',2),(_a,3)))
_TnSapTlsStpBpduEncap_Type.__name__=_G
_TnSapTlsStpBpduEncap_Object=MibTableColumn
tnSapTlsStpBpduEncap=_TnSapTlsStpBpduEncap_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,6),_TnSapTlsStpBpduEncap_Type())
tnSapTlsStpBpduEncap.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpBpduEncap.setStatus(_A)
_TnSapTlsStpPortState_Type=TStpPortState
_TnSapTlsStpPortState_Object=MibTableColumn
tnSapTlsStpPortState=_TnSapTlsStpPortState_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,7),_TnSapTlsStpPortState_Type())
tnSapTlsStpPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpPortState.setStatus(_A)
_TnSapTlsStpDesignatedBridge_Type=BridgeId
_TnSapTlsStpDesignatedBridge_Object=MibTableColumn
tnSapTlsStpDesignatedBridge=_TnSapTlsStpDesignatedBridge_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,8),_TnSapTlsStpDesignatedBridge_Type())
tnSapTlsStpDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpDesignatedBridge.setStatus(_A)
_TnSapTlsStpDesignatedPort_Type=Integer32
_TnSapTlsStpDesignatedPort_Object=MibTableColumn
tnSapTlsStpDesignatedPort=_TnSapTlsStpDesignatedPort_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,9),_TnSapTlsStpDesignatedPort_Type())
tnSapTlsStpDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpDesignatedPort.setStatus(_A)
_TnSapTlsStpForwardTransitions_Type=Gauge32
_TnSapTlsStpForwardTransitions_Object=MibTableColumn
tnSapTlsStpForwardTransitions=_TnSapTlsStpForwardTransitions_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,10),_TnSapTlsStpForwardTransitions_Type())
tnSapTlsStpForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpForwardTransitions.setStatus(_A)
_TnSapTlsStpInConfigBpdus_Type=Gauge32
_TnSapTlsStpInConfigBpdus_Object=MibTableColumn
tnSapTlsStpInConfigBpdus=_TnSapTlsStpInConfigBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,11),_TnSapTlsStpInConfigBpdus_Type())
tnSapTlsStpInConfigBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInConfigBpdus.setStatus(_A)
_TnSapTlsStpInTcnBpdus_Type=Gauge32
_TnSapTlsStpInTcnBpdus_Object=MibTableColumn
tnSapTlsStpInTcnBpdus=_TnSapTlsStpInTcnBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,12),_TnSapTlsStpInTcnBpdus_Type())
tnSapTlsStpInTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInTcnBpdus.setStatus(_A)
_TnSapTlsStpInBadBpdus_Type=Gauge32
_TnSapTlsStpInBadBpdus_Object=MibTableColumn
tnSapTlsStpInBadBpdus=_TnSapTlsStpInBadBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,13),_TnSapTlsStpInBadBpdus_Type())
tnSapTlsStpInBadBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInBadBpdus.setStatus(_A)
_TnSapTlsStpOutConfigBpdus_Type=Gauge32
_TnSapTlsStpOutConfigBpdus_Object=MibTableColumn
tnSapTlsStpOutConfigBpdus=_TnSapTlsStpOutConfigBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,14),_TnSapTlsStpOutConfigBpdus_Type())
tnSapTlsStpOutConfigBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOutConfigBpdus.setStatus(_A)
_TnSapTlsStpOutTcnBpdus_Type=Gauge32
_TnSapTlsStpOutTcnBpdus_Object=MibTableColumn
tnSapTlsStpOutTcnBpdus=_TnSapTlsStpOutTcnBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,15),_TnSapTlsStpOutTcnBpdus_Type())
tnSapTlsStpOutTcnBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOutTcnBpdus.setStatus(_A)
class _TnSapTlsStpOperBpduEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),('dot1d',2),(_a,3)))
_TnSapTlsStpOperBpduEncap_Type.__name__=_G
_TnSapTlsStpOperBpduEncap_Object=MibTableColumn
tnSapTlsStpOperBpduEncap=_TnSapTlsStpOperBpduEncap_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,16),_TnSapTlsStpOperBpduEncap_Type())
tnSapTlsStpOperBpduEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOperBpduEncap.setStatus(_A)
_TnSapTlsVpnId_Type=VpnId
_TnSapTlsVpnId_Object=MibTableColumn
tnSapTlsVpnId=_TnSapTlsVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,17),_TnSapTlsVpnId_Type())
tnSapTlsVpnId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsVpnId.setStatus(_A)
_TnSapTlsCustId_Type=TmnxCustId
_TnSapTlsCustId_Object=MibTableColumn
tnSapTlsCustId=_TnSapTlsCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,18),_TnSapTlsCustId_Type())
tnSapTlsCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsCustId.setStatus(_A)
class _TnSapTlsMacAddressLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511999))
_TnSapTlsMacAddressLimit_Type.__name__=_G
_TnSapTlsMacAddressLimit_Object=MibTableColumn
tnSapTlsMacAddressLimit=_TnSapTlsMacAddressLimit_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,19),_TnSapTlsMacAddressLimit_Type())
tnSapTlsMacAddressLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMacAddressLimit.setStatus(_A)
_TnSapTlsNumMacAddresses_Type=Integer32
_TnSapTlsNumMacAddresses_Object=MibTableColumn
tnSapTlsNumMacAddresses=_TnSapTlsNumMacAddresses_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,20),_TnSapTlsNumMacAddresses_Type())
tnSapTlsNumMacAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsNumMacAddresses.setStatus(_A)
_TnSapTlsNumStaticMacAddresses_Type=Integer32
_TnSapTlsNumStaticMacAddresses_Object=MibTableColumn
tnSapTlsNumStaticMacAddresses=_TnSapTlsNumStaticMacAddresses_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,21),_TnSapTlsNumStaticMacAddresses_Type())
tnSapTlsNumStaticMacAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsNumStaticMacAddresses.setStatus(_A)
class _TnSapTlsMacLearning_Type(TmnxEnabledDisabled):defaultValue=1
_TnSapTlsMacLearning_Type.__name__=_O
_TnSapTlsMacLearning_Object=MibTableColumn
tnSapTlsMacLearning=_TnSapTlsMacLearning_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,22),_TnSapTlsMacLearning_Type())
tnSapTlsMacLearning.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMacLearning.setStatus(_A)
class _TnSapTlsMacAgeing_Type(TmnxEnabledDisabled):defaultValue=1
_TnSapTlsMacAgeing_Type.__name__=_O
_TnSapTlsMacAgeing_Object=MibTableColumn
tnSapTlsMacAgeing=_TnSapTlsMacAgeing_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,23),_TnSapTlsMacAgeing_Type())
tnSapTlsMacAgeing.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMacAgeing.setStatus(_A)
_TnSapTlsStpOperEdge_Type=TruthValue
_TnSapTlsStpOperEdge_Object=MibTableColumn
tnSapTlsStpOperEdge=_TnSapTlsStpOperEdge_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,24),_TnSapTlsStpOperEdge_Type())
tnSapTlsStpOperEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOperEdge.setStatus(_A)
class _TnSapTlsStpAdminPointToPoint_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1)))
_TnSapTlsStpAdminPointToPoint_Type.__name__=_G
_TnSapTlsStpAdminPointToPoint_Object=MibTableColumn
tnSapTlsStpAdminPointToPoint=_TnSapTlsStpAdminPointToPoint_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,25),_TnSapTlsStpAdminPointToPoint_Type())
tnSapTlsStpAdminPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpAdminPointToPoint.setStatus(_A)
_TnSapTlsStpPortRole_Type=StpPortRole
_TnSapTlsStpPortRole_Object=MibTableColumn
tnSapTlsStpPortRole=_TnSapTlsStpPortRole_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,26),_TnSapTlsStpPortRole_Type())
tnSapTlsStpPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpPortRole.setStatus(_A)
class _TnSapTlsStpAutoEdge_Type(TmnxEnabledDisabled):defaultValue=1
_TnSapTlsStpAutoEdge_Type.__name__=_O
_TnSapTlsStpAutoEdge_Object=MibTableColumn
tnSapTlsStpAutoEdge=_TnSapTlsStpAutoEdge_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,27),_TnSapTlsStpAutoEdge_Type())
tnSapTlsStpAutoEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpAutoEdge.setStatus(_A)
_TnSapTlsStpOperProtocol_Type=StpProtocol
_TnSapTlsStpOperProtocol_Object=MibTableColumn
tnSapTlsStpOperProtocol=_TnSapTlsStpOperProtocol_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,28),_TnSapTlsStpOperProtocol_Type())
tnSapTlsStpOperProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOperProtocol.setStatus(_A)
_TnSapTlsStpInRstBpdus_Type=Gauge32
_TnSapTlsStpInRstBpdus_Object=MibTableColumn
tnSapTlsStpInRstBpdus=_TnSapTlsStpInRstBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,29),_TnSapTlsStpInRstBpdus_Type())
tnSapTlsStpInRstBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInRstBpdus.setStatus(_A)
_TnSapTlsStpOutRstBpdus_Type=Gauge32
_TnSapTlsStpOutRstBpdus_Object=MibTableColumn
tnSapTlsStpOutRstBpdus=_TnSapTlsStpOutRstBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,30),_TnSapTlsStpOutRstBpdus_Type())
tnSapTlsStpOutRstBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOutRstBpdus.setStatus(_A)
class _TnSapTlsLimitMacMove_Type(TlsLimitMacMove):defaultValue=1
_TnSapTlsLimitMacMove_Type.__name__=_e
_TnSapTlsLimitMacMove_Object=MibTableColumn
tnSapTlsLimitMacMove=_TnSapTlsLimitMacMove_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,31),_TnSapTlsLimitMacMove_Type())
tnSapTlsLimitMacMove.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsLimitMacMove.setStatus(_A)
_TnSapTlsMacPinning_Type=TmnxEnabledDisabled
_TnSapTlsMacPinning_Object=MibTableColumn
tnSapTlsMacPinning=_TnSapTlsMacPinning_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,33),_TnSapTlsMacPinning_Type())
tnSapTlsMacPinning.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMacPinning.setStatus(_A)
class _TnSapTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):defaultValue=2
_TnSapTlsDiscardUnknownSource_Type.__name__=_O
_TnSapTlsDiscardUnknownSource_Object=MibTableColumn
tnSapTlsDiscardUnknownSource=_TnSapTlsDiscardUnknownSource_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,34),_TnSapTlsDiscardUnknownSource_Type())
tnSapTlsDiscardUnknownSource.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsDiscardUnknownSource.setStatus(_A)
_TnSapTlsMvplsPruneState_Type=MvplsPruneState
_TnSapTlsMvplsPruneState_Object=MibTableColumn
tnSapTlsMvplsPruneState=_TnSapTlsMvplsPruneState_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,35),_TnSapTlsMvplsPruneState_Type())
tnSapTlsMvplsPruneState.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMvplsPruneState.setStatus(_A)
_TnSapTlsMvplsMgmtService_Type=TmnxServId
_TnSapTlsMvplsMgmtService_Object=MibTableColumn
tnSapTlsMvplsMgmtService=_TnSapTlsMvplsMgmtService_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,36),_TnSapTlsMvplsMgmtService_Type())
tnSapTlsMvplsMgmtService.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMvplsMgmtService.setStatus(_A)
_TnSapTlsMvplsMgmtPortId_Type=TmnxPortID
_TnSapTlsMvplsMgmtPortId_Object=MibTableColumn
tnSapTlsMvplsMgmtPortId=_TnSapTlsMvplsMgmtPortId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,37),_TnSapTlsMvplsMgmtPortId_Type())
tnSapTlsMvplsMgmtPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMvplsMgmtPortId.setStatus(_A)
_TnSapTlsMvplsMgmtEncapValue_Type=TmnxEncapVal
_TnSapTlsMvplsMgmtEncapValue_Object=MibTableColumn
tnSapTlsMvplsMgmtEncapValue=_TnSapTlsMvplsMgmtEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,38),_TnSapTlsMvplsMgmtEncapValue_Type())
tnSapTlsMvplsMgmtEncapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMvplsMgmtEncapValue.setStatus(_A)
class _TnSapTlsArpReplyAgent_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),('enabled',2),('enabledWithSubscrIdent',3)))
_TnSapTlsArpReplyAgent_Type.__name__=_G
_TnSapTlsArpReplyAgent_Object=MibTableColumn
tnSapTlsArpReplyAgent=_TnSapTlsArpReplyAgent_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,39),_TnSapTlsArpReplyAgent_Type())
tnSapTlsArpReplyAgent.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsArpReplyAgent.setStatus(_A)
_TnSapTlsStpException_Type=StpExceptionCondition
_TnSapTlsStpException_Object=MibTableColumn
tnSapTlsStpException=_TnSapTlsStpException_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,40),_TnSapTlsStpException_Type())
tnSapTlsStpException.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpException.setStatus(_A)
class _TnSapTlsAuthenticationPolicy_Type(TPolicyStatementNameOrEmpty):defaultHexValue=''
_TnSapTlsAuthenticationPolicy_Type.__name__=_Y
_TnSapTlsAuthenticationPolicy_Object=MibTableColumn
tnSapTlsAuthenticationPolicy=_TnSapTlsAuthenticationPolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,41),_TnSapTlsAuthenticationPolicy_Type())
tnSapTlsAuthenticationPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsAuthenticationPolicy.setStatus(_A)
class _TnSapTlsL2ptTermination_Type(TmnxEnabledDisabled):defaultValue=2
_TnSapTlsL2ptTermination_Type.__name__=_O
_TnSapTlsL2ptTermination_Object=MibTableColumn
tnSapTlsL2ptTermination=_TnSapTlsL2ptTermination_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,42),_TnSapTlsL2ptTermination_Type())
tnSapTlsL2ptTermination.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsL2ptTermination.setStatus(_A)
class _TnSapTlsBpduTranslation_Type(TlsBpduTranslation):defaultValue=2
_TnSapTlsBpduTranslation_Type.__name__=_d
_TnSapTlsBpduTranslation_Object=MibTableColumn
tnSapTlsBpduTranslation=_TnSapTlsBpduTranslation_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,43),_TnSapTlsBpduTranslation_Type())
tnSapTlsBpduTranslation.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsBpduTranslation.setStatus(_A)
class _TnSapTlsStpRootGuard_Type(TruthValue):defaultValue=2
_TnSapTlsStpRootGuard_Type.__name__=_K
_TnSapTlsStpRootGuard_Object=MibTableColumn
tnSapTlsStpRootGuard=_TnSapTlsStpRootGuard_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,44),_TnSapTlsStpRootGuard_Type())
tnSapTlsStpRootGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsStpRootGuard.setStatus(_A)
_TnSapTlsStpInsideRegion_Type=TruthValue
_TnSapTlsStpInsideRegion_Object=MibTableColumn
tnSapTlsStpInsideRegion=_TnSapTlsStpInsideRegion_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,45),_TnSapTlsStpInsideRegion_Type())
tnSapTlsStpInsideRegion.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInsideRegion.setStatus(_A)
class _TnSapTlsEgressMcastGroup_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnSapTlsEgressMcastGroup_Type.__name__=_R
_TnSapTlsEgressMcastGroup_Object=MibTableColumn
tnSapTlsEgressMcastGroup=_TnSapTlsEgressMcastGroup_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,46),_TnSapTlsEgressMcastGroup_Type())
tnSapTlsEgressMcastGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsEgressMcastGroup.setStatus(_A)
_TnSapTlsStpInMstBpdus_Type=Gauge32
_TnSapTlsStpInMstBpdus_Object=MibTableColumn
tnSapTlsStpInMstBpdus=_TnSapTlsStpInMstBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,47),_TnSapTlsStpInMstBpdus_Type())
tnSapTlsStpInMstBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpInMstBpdus.setStatus(_A)
_TnSapTlsStpOutMstBpdus_Type=Gauge32
_TnSapTlsStpOutMstBpdus_Object=MibTableColumn
tnSapTlsStpOutMstBpdus=_TnSapTlsStpOutMstBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,48),_TnSapTlsStpOutMstBpdus_Type())
tnSapTlsStpOutMstBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpOutMstBpdus.setStatus(_A)
class _TnSapTlsRestProtSrcMac_Type(TruthValue):defaultValue=2
_TnSapTlsRestProtSrcMac_Type.__name__=_K
_TnSapTlsRestProtSrcMac_Object=MibTableColumn
tnSapTlsRestProtSrcMac=_TnSapTlsRestProtSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,49),_TnSapTlsRestProtSrcMac_Type())
tnSapTlsRestProtSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsRestProtSrcMac.setStatus(_A)
class _TnSapTlsRestUnprotDstMac_Type(TruthValue):defaultValue=2
_TnSapTlsRestUnprotDstMac_Type.__name__=_K
_TnSapTlsRestUnprotDstMac_Object=MibTableColumn
tnSapTlsRestUnprotDstMac=_TnSapTlsRestUnprotDstMac_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,50),_TnSapTlsRestUnprotDstMac_Type())
tnSapTlsRestUnprotDstMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsRestUnprotDstMac.setStatus(_A)
_TnSapTlsStpRxdDesigBridge_Type=BridgeId
_TnSapTlsStpRxdDesigBridge_Object=MibTableColumn
tnSapTlsStpRxdDesigBridge=_TnSapTlsStpRxdDesigBridge_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,51),_TnSapTlsStpRxdDesigBridge_Type())
tnSapTlsStpRxdDesigBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpRxdDesigBridge.setStatus(_A)
_TnSapTlsStpRootGuardViolation_Type=TruthValue
_TnSapTlsStpRootGuardViolation_Object=MibTableColumn
tnSapTlsStpRootGuardViolation=_TnSapTlsStpRootGuardViolation_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,52),_TnSapTlsStpRootGuardViolation_Type())
tnSapTlsStpRootGuardViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsStpRootGuardViolation.setStatus(_A)
class _TnSapTlsShcvAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alarm',1),('remove',2)))
_TnSapTlsShcvAction_Type.__name__=_G
_TnSapTlsShcvAction_Object=MibTableColumn
tnSapTlsShcvAction=_TnSapTlsShcvAction_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,53),_TnSapTlsShcvAction_Type())
tnSapTlsShcvAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvAction.setStatus(_A)
_TnSapTlsShcvSrcIp_Type=IpAddress
_TnSapTlsShcvSrcIp_Object=MibTableColumn
tnSapTlsShcvSrcIp=_TnSapTlsShcvSrcIp_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,54),_TnSapTlsShcvSrcIp_Type())
tnSapTlsShcvSrcIp.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvSrcIp.setStatus(_A)
_TnSapTlsShcvSrcMac_Type=MacAddress
_TnSapTlsShcvSrcMac_Object=MibTableColumn
tnSapTlsShcvSrcMac=_TnSapTlsShcvSrcMac_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,55),_TnSapTlsShcvSrcMac_Type())
tnSapTlsShcvSrcMac.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvSrcMac.setStatus(_A)
class _TnSapTlsShcvInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6000))
_TnSapTlsShcvInterval_Type.__name__=_L
_TnSapTlsShcvInterval_Object=MibTableColumn
tnSapTlsShcvInterval=_TnSapTlsShcvInterval_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,56),_TnSapTlsShcvInterval_Type())
tnSapTlsShcvInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvInterval.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsShcvInterval.setUnits('minutes')
_TnSapTlsMvplsMgmtMsti_Type=MstiInstanceIdOrZero
_TnSapTlsMvplsMgmtMsti_Object=MibTableColumn
tnSapTlsMvplsMgmtMsti=_TnSapTlsMvplsMgmtMsti_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,57),_TnSapTlsMvplsMgmtMsti_Type())
tnSapTlsMvplsMgmtMsti.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMvplsMgmtMsti.setStatus(_A)
_TnSapTlsMacMoveNextUpTime_Type=Unsigned32
_TnSapTlsMacMoveNextUpTime_Object=MibTableColumn
tnSapTlsMacMoveNextUpTime=_TnSapTlsMacMoveNextUpTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,58),_TnSapTlsMacMoveNextUpTime_Type())
tnSapTlsMacMoveNextUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMacMoveNextUpTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsMacMoveNextUpTime.setUnits(_u)
_TnSapTlsMacMoveRateExcdLeft_Type=Unsigned32
_TnSapTlsMacMoveRateExcdLeft_Object=MibTableColumn
tnSapTlsMacMoveRateExcdLeft=_TnSapTlsMacMoveRateExcdLeft_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,59),_TnSapTlsMacMoveRateExcdLeft_Type())
tnSapTlsMacMoveRateExcdLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsMacMoveRateExcdLeft.setStatus(_A)
class _TnSapTlsRestProtSrcMacAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('alarm-only',2)))
_TnSapTlsRestProtSrcMacAction_Type.__name__=_G
_TnSapTlsRestProtSrcMacAction_Object=MibTableColumn
tnSapTlsRestProtSrcMacAction=_TnSapTlsRestProtSrcMacAction_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,60),_TnSapTlsRestProtSrcMacAction_Type())
tnSapTlsRestProtSrcMacAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsRestProtSrcMacAction.setStatus(_A)
class _TnSapTlsL2ptForceBoundary_Type(TruthValue):defaultValue=2
_TnSapTlsL2ptForceBoundary_Type.__name__=_K
_TnSapTlsL2ptForceBoundary_Object=MibTableColumn
tnSapTlsL2ptForceBoundary=_TnSapTlsL2ptForceBoundary_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,61),_TnSapTlsL2ptForceBoundary_Type())
tnSapTlsL2ptForceBoundary.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsL2ptForceBoundary.setStatus(_A)
class _TnSapTlsLimitMacMoveLevel_Type(TlsLimitMacMoveLevel):defaultValue=3
_TnSapTlsLimitMacMoveLevel_Type.__name__=_f
_TnSapTlsLimitMacMoveLevel_Object=MibTableColumn
tnSapTlsLimitMacMoveLevel=_TnSapTlsLimitMacMoveLevel_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,62),_TnSapTlsLimitMacMoveLevel_Type())
tnSapTlsLimitMacMoveLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsLimitMacMoveLevel.setStatus(_A)
class _TnSapTlsBpduTransOper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('undefined',1),(_U,2),(_a,3),('stp',4),('pvst-rw',5)))
_TnSapTlsBpduTransOper_Type.__name__=_G
_TnSapTlsBpduTransOper_Object=MibTableColumn
tnSapTlsBpduTransOper=_TnSapTlsBpduTransOper_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,63),_TnSapTlsBpduTransOper_Type())
tnSapTlsBpduTransOper.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsBpduTransOper.setStatus(_A)
class _TnSapTlsDefMtnSapPolicy_Type(TPolicyStatementNameOrEmpty):defaultValue=OctetString('')
_TnSapTlsDefMtnSapPolicy_Type.__name__=_Y
_TnSapTlsDefMtnSapPolicy_Object=MibTableColumn
tnSapTlsDefMtnSapPolicy=_TnSapTlsDefMtnSapPolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,64),_TnSapTlsDefMtnSapPolicy_Type())
tnSapTlsDefMtnSapPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsDefMtnSapPolicy.setStatus(_A)
class _TnSapTlsL2ptProtocols_Type(L2ptProtocols):defaultBinValue='1'
_TnSapTlsL2ptProtocols_Type.__name__=_W
_TnSapTlsL2ptProtocols_Object=MibTableColumn
tnSapTlsL2ptProtocols=_TnSapTlsL2ptProtocols_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,65),_TnSapTlsL2ptProtocols_Type())
tnSapTlsL2ptProtocols.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsL2ptProtocols.setStatus(_A)
class _TnSapTlsL2ptForceProtocols_Type(L2ptProtocols):defaultBinValue='1'
_TnSapTlsL2ptForceProtocols_Type.__name__=_W
_TnSapTlsL2ptForceProtocols_Object=MibTableColumn
tnSapTlsL2ptForceProtocols=_TnSapTlsL2ptForceProtocols_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,66),_TnSapTlsL2ptForceProtocols_Type())
tnSapTlsL2ptForceProtocols.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsL2ptForceProtocols.setStatus(_A)
class _TnSapTlsPppoeMtnSapTrigger_Type(TruthValue):defaultValue=2
_TnSapTlsPppoeMtnSapTrigger_Type.__name__=_K
_TnSapTlsPppoeMtnSapTrigger_Object=MibTableColumn
tnSapTlsPppoeMtnSapTrigger=_TnSapTlsPppoeMtnSapTrigger_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,67),_TnSapTlsPppoeMtnSapTrigger_Type())
tnSapTlsPppoeMtnSapTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsPppoeMtnSapTrigger.setStatus(_A)
class _TnSapTlsDhcpMtnSapTrigger_Type(TruthValue):defaultValue=2
_TnSapTlsDhcpMtnSapTrigger_Type.__name__=_K
_TnSapTlsDhcpMtnSapTrigger_Object=MibTableColumn
tnSapTlsDhcpMtnSapTrigger=_TnSapTlsDhcpMtnSapTrigger_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,68),_TnSapTlsDhcpMtnSapTrigger_Type())
tnSapTlsDhcpMtnSapTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsDhcpMtnSapTrigger.setStatus(_A)
class _TnSapTlsMrpJoinTime_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnSapTlsMrpJoinTime_Type.__name__=_L
_TnSapTlsMrpJoinTime_Object=MibTableColumn
tnSapTlsMrpJoinTime=_TnSapTlsMrpJoinTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,69),_TnSapTlsMrpJoinTime_Type())
tnSapTlsMrpJoinTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMrpJoinTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsMrpJoinTime.setUnits(_V)
class _TnSapTlsMrpLeaveTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,60))
_TnSapTlsMrpLeaveTime_Type.__name__=_L
_TnSapTlsMrpLeaveTime_Object=MibTableColumn
tnSapTlsMrpLeaveTime=_TnSapTlsMrpLeaveTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,70),_TnSapTlsMrpLeaveTime_Type())
tnSapTlsMrpLeaveTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMrpLeaveTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsMrpLeaveTime.setUnits(_V)
class _TnSapTlsMrpLeaveAllTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_TnSapTlsMrpLeaveAllTime_Type.__name__=_L
_TnSapTlsMrpLeaveAllTime_Object=MibTableColumn
tnSapTlsMrpLeaveAllTime=_TnSapTlsMrpLeaveAllTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,71),_TnSapTlsMrpLeaveAllTime_Type())
tnSapTlsMrpLeaveAllTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMrpLeaveAllTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsMrpLeaveAllTime.setUnits(_V)
class _TnSapTlsMrpPeriodicTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_TnSapTlsMrpPeriodicTime_Type.__name__=_L
_TnSapTlsMrpPeriodicTime_Object=MibTableColumn
tnSapTlsMrpPeriodicTime=_TnSapTlsMrpPeriodicTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,72),_TnSapTlsMrpPeriodicTime_Type())
tnSapTlsMrpPeriodicTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMrpPeriodicTime.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsMrpPeriodicTime.setUnits(_V)
class _TnSapTlsMrpPeriodicEnabled_Type(TruthValue):defaultValue=2
_TnSapTlsMrpPeriodicEnabled_Type.__name__=_K
_TnSapTlsMrpPeriodicEnabled_Object=MibTableColumn
tnSapTlsMrpPeriodicEnabled=_TnSapTlsMrpPeriodicEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,73),_TnSapTlsMrpPeriodicEnabled_Type())
tnSapTlsMrpPeriodicEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsMrpPeriodicEnabled.setStatus(_A)
class _TnSapTlsPppoePolicy_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_TnSapTlsPppoePolicy_Type.__name__=_R
_TnSapTlsPppoePolicy_Object=MibTableColumn
tnSapTlsPppoePolicy=_TnSapTlsPppoePolicy_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,74),_TnSapTlsPppoePolicy_Type())
tnSapTlsPppoePolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsPppoePolicy.setStatus(_A)
class _TnSapTlsArpMsapTrigger_Type(TruthValue):defaultValue=2
_TnSapTlsArpMsapTrigger_Type.__name__=_K
_TnSapTlsArpMsapTrigger_Object=MibTableColumn
tnSapTlsArpMsapTrigger=_TnSapTlsArpMsapTrigger_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,75),_TnSapTlsArpMsapTrigger_Type())
tnSapTlsArpMsapTrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsArpMsapTrigger.setStatus(_A)
_TnSapTlsInTcBitBpdus_Type=Counter32
_TnSapTlsInTcBitBpdus_Object=MibTableColumn
tnSapTlsInTcBitBpdus=_TnSapTlsInTcBitBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,76),_TnSapTlsInTcBitBpdus_Type())
tnSapTlsInTcBitBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsInTcBitBpdus.setStatus(_A)
_TnSapTlsOutTcBitBpdus_Type=Counter32
_TnSapTlsOutTcBitBpdus_Object=MibTableColumn
tnSapTlsOutTcBitBpdus=_TnSapTlsOutTcBitBpdus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,77),_TnSapTlsOutTcBitBpdus_Type())
tnSapTlsOutTcBitBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapTlsOutTcBitBpdus.setStatus(_A)
class _TnSapTlsShcvRetryTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_TnSapTlsShcvRetryTimeout_Type.__name__=_L
_TnSapTlsShcvRetryTimeout_Object=MibTableColumn
tnSapTlsShcvRetryTimeout=_TnSapTlsShcvRetryTimeout_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,81),_TnSapTlsShcvRetryTimeout_Type())
tnSapTlsShcvRetryTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvRetryTimeout.setStatus(_A)
if mibBuilder.loadTexts:tnSapTlsShcvRetryTimeout.setUnits(_u)
class _TnSapTlsShcvRetryCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,29))
_TnSapTlsShcvRetryCount_Type.__name__=_L
_TnSapTlsShcvRetryCount_Object=MibTableColumn
tnSapTlsShcvRetryCount=_TnSapTlsShcvRetryCount_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,82),_TnSapTlsShcvRetryCount_Type())
tnSapTlsShcvRetryCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsShcvRetryCount.setStatus(_A)
class _TnSapTlsFdbTableSizeProfId_Type(TFdbTableSizeProfileID):defaultValue=1
_TnSapTlsFdbTableSizeProfId_Type.__name__=_j
_TnSapTlsFdbTableSizeProfId_Object=MibTableColumn
tnSapTlsFdbTableSizeProfId=_TnSapTlsFdbTableSizeProfId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,3,1,83),_TnSapTlsFdbTableSizeProfId_Type())
tnSapTlsFdbTableSizeProfId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapTlsFdbTableSizeProfId.setStatus('deprecated')
_TnSapScalar1_Type=Unsigned32
_TnSapScalar1_Object=MibScalar
tnSapScalar1=_TnSapScalar1_Object((1,3,6,1,4,1,7483,6,1,2,4,3,5),_TnSapScalar1_Type())
tnSapScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapScalar1.setStatus(_A)
_TnSapBaseStatsTable_Object=MibTable
tnSapBaseStatsTable=_TnSapBaseStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6))
if mibBuilder.loadTexts:tnSapBaseStatsTable.setStatus(_A)
_TnSapBaseStatsEntry_Object=MibTableRow
tnSapBaseStatsEntry=_TnSapBaseStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1))
tnSapBaseStatsEntry.setIndexNames((0,_S,_T),(0,_F,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:tnSapBaseStatsEntry.setStatus(_A)
_TnSapBaseStatsIngressPchipDroppedPackets_Type=Counter64
_TnSapBaseStatsIngressPchipDroppedPackets_Object=MibTableColumn
tnSapBaseStatsIngressPchipDroppedPackets=_TnSapBaseStatsIngressPchipDroppedPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,1),_TnSapBaseStatsIngressPchipDroppedPackets_Type())
tnSapBaseStatsIngressPchipDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipDroppedPackets.setStatus(_A)
_TnSapBaseStatsIngressPchipDroppedOctets_Type=Counter64
_TnSapBaseStatsIngressPchipDroppedOctets_Object=MibTableColumn
tnSapBaseStatsIngressPchipDroppedOctets=_TnSapBaseStatsIngressPchipDroppedOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,2),_TnSapBaseStatsIngressPchipDroppedOctets_Type())
tnSapBaseStatsIngressPchipDroppedOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipDroppedOctets.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedHiPrioPackets=_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,3),_TnSapBaseStatsIngressPchipOfferedHiPrioPackets_Type())
tnSapBaseStatsIngressPchipOfferedHiPrioPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedHiPrioPackets.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedHiPrioOctets=_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,4),_TnSapBaseStatsIngressPchipOfferedHiPrioOctets_Type())
tnSapBaseStatsIngressPchipOfferedHiPrioOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedHiPrioOctets.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedLoPrioPackets=_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,5),_TnSapBaseStatsIngressPchipOfferedLoPrioPackets_Type())
tnSapBaseStatsIngressPchipOfferedLoPrioPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedLoPrioPackets.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedLoPrioOctets=_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,6),_TnSapBaseStatsIngressPchipOfferedLoPrioOctets_Type())
tnSapBaseStatsIngressPchipOfferedLoPrioOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedLoPrioOctets.setStatus(_A)
_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Type=Counter64
_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Object=MibTableColumn
tnSapBaseStatsIngressQchipDroppedHiPrioPackets=_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,7),_TnSapBaseStatsIngressQchipDroppedHiPrioPackets_Type())
tnSapBaseStatsIngressQchipDroppedHiPrioPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipDroppedHiPrioPackets.setStatus(_A)
_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Type=Counter64
_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Object=MibTableColumn
tnSapBaseStatsIngressQchipDroppedHiPrioOctets=_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,8),_TnSapBaseStatsIngressQchipDroppedHiPrioOctets_Type())
tnSapBaseStatsIngressQchipDroppedHiPrioOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipDroppedHiPrioOctets.setStatus(_A)
_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Type=Counter64
_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Object=MibTableColumn
tnSapBaseStatsIngressQchipDroppedLoPrioPackets=_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,9),_TnSapBaseStatsIngressQchipDroppedLoPrioPackets_Type())
tnSapBaseStatsIngressQchipDroppedLoPrioPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipDroppedLoPrioPackets.setStatus(_A)
_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Type=Counter64
_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Object=MibTableColumn
tnSapBaseStatsIngressQchipDroppedLoPrioOctets=_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,10),_TnSapBaseStatsIngressQchipDroppedLoPrioOctets_Type())
tnSapBaseStatsIngressQchipDroppedLoPrioOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipDroppedLoPrioOctets.setStatus(_A)
_TnSapBaseStatsIngressQchipForwardedInProfPackets_Type=Counter64
_TnSapBaseStatsIngressQchipForwardedInProfPackets_Object=MibTableColumn
tnSapBaseStatsIngressQchipForwardedInProfPackets=_TnSapBaseStatsIngressQchipForwardedInProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,11),_TnSapBaseStatsIngressQchipForwardedInProfPackets_Type())
tnSapBaseStatsIngressQchipForwardedInProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipForwardedInProfPackets.setStatus(_A)
_TnSapBaseStatsIngressQchipForwardedInProfOctets_Type=Counter64
_TnSapBaseStatsIngressQchipForwardedInProfOctets_Object=MibTableColumn
tnSapBaseStatsIngressQchipForwardedInProfOctets=_TnSapBaseStatsIngressQchipForwardedInProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,12),_TnSapBaseStatsIngressQchipForwardedInProfOctets_Type())
tnSapBaseStatsIngressQchipForwardedInProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipForwardedInProfOctets.setStatus(_A)
_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Type=Counter64
_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Object=MibTableColumn
tnSapBaseStatsIngressQchipForwardedOutProfPackets=_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,13),_TnSapBaseStatsIngressQchipForwardedOutProfPackets_Type())
tnSapBaseStatsIngressQchipForwardedOutProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipForwardedOutProfPackets.setStatus(_A)
_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Type=Counter64
_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Object=MibTableColumn
tnSapBaseStatsIngressQchipForwardedOutProfOctets=_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,14),_TnSapBaseStatsIngressQchipForwardedOutProfOctets_Type())
tnSapBaseStatsIngressQchipForwardedOutProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressQchipForwardedOutProfOctets.setStatus(_A)
_TnSapBaseStatsEgressQchipDroppedInProfPackets_Type=Counter64
_TnSapBaseStatsEgressQchipDroppedInProfPackets_Object=MibTableColumn
tnSapBaseStatsEgressQchipDroppedInProfPackets=_TnSapBaseStatsEgressQchipDroppedInProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,15),_TnSapBaseStatsEgressQchipDroppedInProfPackets_Type())
tnSapBaseStatsEgressQchipDroppedInProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipDroppedInProfPackets.setStatus(_A)
_TnSapBaseStatsEgressQchipDroppedInProfOctets_Type=Counter64
_TnSapBaseStatsEgressQchipDroppedInProfOctets_Object=MibTableColumn
tnSapBaseStatsEgressQchipDroppedInProfOctets=_TnSapBaseStatsEgressQchipDroppedInProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,16),_TnSapBaseStatsEgressQchipDroppedInProfOctets_Type())
tnSapBaseStatsEgressQchipDroppedInProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipDroppedInProfOctets.setStatus(_A)
_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Type=Counter64
_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Object=MibTableColumn
tnSapBaseStatsEgressQchipDroppedOutProfPackets=_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,17),_TnSapBaseStatsEgressQchipDroppedOutProfPackets_Type())
tnSapBaseStatsEgressQchipDroppedOutProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipDroppedOutProfPackets.setStatus(_A)
_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Type=Counter64
_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Object=MibTableColumn
tnSapBaseStatsEgressQchipDroppedOutProfOctets=_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,18),_TnSapBaseStatsEgressQchipDroppedOutProfOctets_Type())
tnSapBaseStatsEgressQchipDroppedOutProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipDroppedOutProfOctets.setStatus(_A)
_TnSapBaseStatsEgressQchipForwardedInProfPackets_Type=Counter64
_TnSapBaseStatsEgressQchipForwardedInProfPackets_Object=MibTableColumn
tnSapBaseStatsEgressQchipForwardedInProfPackets=_TnSapBaseStatsEgressQchipForwardedInProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,19),_TnSapBaseStatsEgressQchipForwardedInProfPackets_Type())
tnSapBaseStatsEgressQchipForwardedInProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipForwardedInProfPackets.setStatus(_A)
_TnSapBaseStatsEgressQchipForwardedInProfOctets_Type=Counter64
_TnSapBaseStatsEgressQchipForwardedInProfOctets_Object=MibTableColumn
tnSapBaseStatsEgressQchipForwardedInProfOctets=_TnSapBaseStatsEgressQchipForwardedInProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,20),_TnSapBaseStatsEgressQchipForwardedInProfOctets_Type())
tnSapBaseStatsEgressQchipForwardedInProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipForwardedInProfOctets.setStatus(_A)
_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Type=Counter64
_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Object=MibTableColumn
tnSapBaseStatsEgressQchipForwardedOutProfPackets=_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,21),_TnSapBaseStatsEgressQchipForwardedOutProfPackets_Type())
tnSapBaseStatsEgressQchipForwardedOutProfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipForwardedOutProfPackets.setStatus(_A)
_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Type=Counter64
_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Object=MibTableColumn
tnSapBaseStatsEgressQchipForwardedOutProfOctets=_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,22),_TnSapBaseStatsEgressQchipForwardedOutProfOctets_Type())
tnSapBaseStatsEgressQchipForwardedOutProfOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsEgressQchipForwardedOutProfOctets.setStatus(_A)
_TnSapBaseStatsCustId_Type=TmnxCustId
_TnSapBaseStatsCustId_Object=MibTableColumn
tnSapBaseStatsCustId=_TnSapBaseStatsCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,23),_TnSapBaseStatsCustId_Type())
tnSapBaseStatsCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsCustId.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedUncoloredPackets=_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,24),_TnSapBaseStatsIngressPchipOfferedUncoloredPackets_Type())
tnSapBaseStatsIngressPchipOfferedUncoloredPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedUncoloredPackets.setStatus(_A)
_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Type=Counter64
_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Object=MibTableColumn
tnSapBaseStatsIngressPchipOfferedUncoloredOctets=_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,25),_TnSapBaseStatsIngressPchipOfferedUncoloredOctets_Type())
tnSapBaseStatsIngressPchipOfferedUncoloredOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsIngressPchipOfferedUncoloredOctets.setStatus(_A)
_TnSapBaseStatsAuthenticationPktsDiscarded_Type=Counter32
_TnSapBaseStatsAuthenticationPktsDiscarded_Object=MibTableColumn
tnSapBaseStatsAuthenticationPktsDiscarded=_TnSapBaseStatsAuthenticationPktsDiscarded_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,26),_TnSapBaseStatsAuthenticationPktsDiscarded_Type())
tnSapBaseStatsAuthenticationPktsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsAuthenticationPktsDiscarded.setStatus(_A)
_TnSapBaseStatsAuthenticationPktsSuccess_Type=Counter32
_TnSapBaseStatsAuthenticationPktsSuccess_Object=MibTableColumn
tnSapBaseStatsAuthenticationPktsSuccess=_TnSapBaseStatsAuthenticationPktsSuccess_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,27),_TnSapBaseStatsAuthenticationPktsSuccess_Type())
tnSapBaseStatsAuthenticationPktsSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsAuthenticationPktsSuccess.setStatus(_A)
_TnSapBaseStatsLastClearedTime_Type=TimeStamp
_TnSapBaseStatsLastClearedTime_Object=MibTableColumn
tnSapBaseStatsLastClearedTime=_TnSapBaseStatsLastClearedTime_Object((1,3,6,1,4,1,7483,6,1,2,4,3,6,1,28),_TnSapBaseStatsLastClearedTime_Type())
tnSapBaseStatsLastClearedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapBaseStatsLastClearedTime.setStatus(_A)
_TnSapEthernetInfoTable_Object=MibTable
tnSapEthernetInfoTable=_TnSapEthernetInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43))
if mibBuilder.loadTexts:tnSapEthernetInfoTable.setStatus(_A)
_TnSapEthernetInfoEntry_Object=MibTableRow
tnSapEthernetInfoEntry=_TnSapEthernetInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1))
tnSapEthernetInfoEntry.setIndexNames((0,_S,_T),(0,_F,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:tnSapEthernetInfoEntry.setStatus(_A)
class _TnSapEthernetLLFAdminStatus_Type(ServiceAdminStatus):defaultValue=2
_TnSapEthernetLLFAdminStatus_Type.__name__=_X
_TnSapEthernetLLFAdminStatus_Object=MibTableColumn
tnSapEthernetLLFAdminStatus=_TnSapEthernetLLFAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1,1),_TnSapEthernetLLFAdminStatus_Type())
tnSapEthernetLLFAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEthernetLLFAdminStatus.setStatus(_A)
class _TnSapEthernetLLFOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fault',1),('clear',2)))
_TnSapEthernetLLFOperStatus_Type.__name__=_G
_TnSapEthernetLLFOperStatus_Object=MibTableColumn
tnSapEthernetLLFOperStatus=_TnSapEthernetLLFOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1,2),_TnSapEthernetLLFOperStatus_Type())
tnSapEthernetLLFOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapEthernetLLFOperStatus.setStatus(_A)
class _TnSapEthernetLLFId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_TnSapEthernetLLFId_Type.__name__=_L
_TnSapEthernetLLFId_Object=MibTableColumn
tnSapEthernetLLFId=_TnSapEthernetLLFId_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1,3),_TnSapEthernetLLFId_Type())
tnSapEthernetLLFId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEthernetLLFId.setStatus(_A)
class _TnSapEthernetLoopbackMode_Type(SapLoopbackMode):defaultValue=1
_TnSapEthernetLoopbackMode_Type.__name__=_g
_TnSapEthernetLoopbackMode_Object=MibTableColumn
tnSapEthernetLoopbackMode=_TnSapEthernetLoopbackMode_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1,4),_TnSapEthernetLoopbackMode_Type())
tnSapEthernetLoopbackMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEthernetLoopbackMode.setStatus(_A)
class _TnSapEthernetLoopbackMacSwapStaticMac_Type(TruthValue):defaultValue=2
_TnSapEthernetLoopbackMacSwapStaticMac_Type.__name__=_K
_TnSapEthernetLoopbackMacSwapStaticMac_Object=MibTableColumn
tnSapEthernetLoopbackMacSwapStaticMac=_TnSapEthernetLoopbackMacSwapStaticMac_Object((1,3,6,1,4,1,7483,6,1,2,4,3,43,1,5),_TnSapEthernetLoopbackMacSwapStaticMac_Type())
tnSapEthernetLoopbackMacSwapStaticMac.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSapEthernetLoopbackMacSwapStaticMac.setStatus(_A)
_TnSapTrapsPrefix_ObjectIdentity=ObjectIdentity
tnSapTrapsPrefix=_TnSapTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,3))
_TnSapTraps_ObjectIdentity=ObjectIdentity
tnSapTraps=_TnSapTraps_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,4,3,0))
tnSapStatusChanged=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,3,0,3))
tnSapStatusChanged.setObjects(*((_F,_M),(_F,_H),(_F,_Q),(_E,_I),(_E,_J),(_E,_v),(_E,_w),(_E,_x)))
if mibBuilder.loadTexts:tnSapStatusChanged.setStatus(_A)
tnSapTlsMacAddrLimitAlarmRaised=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,3,0,4))
tnSapTlsMacAddrLimitAlarmRaised.setObjects(*((_F,_M),(_F,_H),(_F,_Q),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnSapTlsMacAddrLimitAlarmRaised.setStatus(_A)
tnSapTlsMacAddrLimitAlarmCleared=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,3,0,5))
tnSapTlsMacAddrLimitAlarmCleared.setObjects(*((_F,_M),(_F,_H),(_F,_Q),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnSapTlsMacAddrLimitAlarmCleared.setStatus(_A)
tnSapDHCPLseStateMobilityError=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,3,0,22))
tnSapDHCPLseStateMobilityError.setObjects(*((_F,_M),(_F,_H),(_F,_Q),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnSapDHCPLseStateMobilityError.setStatus(_A)
tnTopologyChangeSapMajorState=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,1))
tnTopologyChangeSapMajorState.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnTopologyChangeSapMajorState.setStatus(_A)
tnNewRootSap=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,2))
tnNewRootSap.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnNewRootSap.setStatus(_A)
tnTopologyChangeSapState=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,5))
tnTopologyChangeSapState.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnTopologyChangeSapState.setStatus(_A)
tnReceivedTCN=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,6))
tnReceivedTCN.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J)))
if mibBuilder.loadTexts:tnReceivedTCN.setStatus(_A)
tnSapActiveProtocolChange=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,30))
tnSapActiveProtocolChange.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J),(_E,_y)))
if mibBuilder.loadTexts:tnSapActiveProtocolChange.setStatus(_A)
tnStpRootGuardViolation=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,35))
tnStpRootGuardViolation.setObjects(*((_F,_H),(_E,_I),(_E,_J),(_E,_z)))
if mibBuilder.loadTexts:tnStpRootGuardViolation.setStatus(_A)
tnSapStpExcepCondStateChng=NotificationType((1,3,6,1,4,1,7483,6,1,3,4,5,0,37))
tnSapStpExcepCondStateChng.setObjects(*((_F,_M),(_F,_H),(_E,_I),(_E,_J),(_E,_A0)))
if mibBuilder.loadTexts:tnSapStpExcepCondStateChng.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'tnSvcSapMIBModule':tnSvcSapMIBModule,'tnSapObjs':tnSapObjs,'tnSapBaseInfoTable':tnSapBaseInfoTable,'tnSapBaseInfoEntry':tnSapBaseInfoEntry,_I:tnSapPortId,_J:tnSapEncapValue,'tnSapRowStatus':tnSapRowStatus,'tnSapType':tnSapType,'tnSapDescription':tnSapDescription,_v:tnSapAdminStatus,_w:tnSapOperStatus,'tnSapIngressQosPolicyId':tnSapIngressQosPolicyId,'tnSapIngressMacFilterId':tnSapIngressMacFilterId,'tnSapIngressIpFilterId':tnSapIngressIpFilterId,'tnSapEgressQosPolicyId':tnSapEgressQosPolicyId,'tnSapEgressMacFilterId':tnSapEgressMacFilterId,'tnSapEgressIpFilterId':tnSapEgressIpFilterId,'tnSapMirrorStatus':tnSapMirrorStatus,'tnSapIesIfIndex':tnSapIesIfIndex,'tnSapLastMgmtChange':tnSapLastMgmtChange,'tnSapCollectAcctStats':tnSapCollectAcctStats,'tnSapAccountingPolicyId':tnSapAccountingPolicyId,'tnSapVpnId':tnSapVpnId,'tnSapCustId':tnSapCustId,'tnSapCustMultSvcSite':tnSapCustMultSvcSite,'tnSapIngressQosSchedulerPolicy':tnSapIngressQosSchedulerPolicy,'tnSapEgressQosSchedulerPolicy':tnSapEgressQosSchedulerPolicy,'tnSapSplitHorizonGrp':tnSapSplitHorizonGrp,'tnSapIngressSharedQueuePolicy':tnSapIngressSharedQueuePolicy,'tnSapIngressMatchQinQDot1PBits':tnSapIngressMatchQinQDot1PBits,_x:tnSapOperFlags,'tnSapLastStatusChange':tnSapLastStatusChange,'tnSapAntiSpoofing':tnSapAntiSpoofing,'tnSapIngressIpv6FilterId':tnSapIngressIpv6FilterId,'tnSapEgressIpv6FilterId':tnSapEgressIpv6FilterId,'tnSapTodSuite':tnSapTodSuite,'tnSapIngUseMultipointShared':tnSapIngUseMultipointShared,'tnSapEgressQinQMarkTopOnly':tnSapEgressQinQMarkTopOnly,'tnSapEgressAggRateLimit':tnSapEgressAggRateLimit,'tnSapEndPoint':tnSapEndPoint,'tnSapIngressVlanTranslation':tnSapIngressVlanTranslation,'tnSapIngressVlanTranslationId':tnSapIngressVlanTranslationId,'tnSapSubType':tnSapSubType,'tnSapCpmProtPolicyId':tnSapCpmProtPolicyId,'tnSapCpmProtMonitorMac':tnSapCpmProtMonitorMac,'tnSapEgressFrameBasedAccounting':tnSapEgressFrameBasedAccounting,'tnSapIngressAggRateLimit':tnSapIngressAggRateLimit,'tnSapEgressHsmdaShaperOverride':tnSapEgressHsmdaShaperOverride,'tnSapIngressHsmdaPacketOffOvr':tnSapIngressHsmdaPacketOffOvr,'tnSapEgressHsmdaPacketOffOverride':tnSapEgressHsmdaPacketOffOverride,'tnSapCallingStationId':tnSapCallingStationId,'tnSapIsaAaApplicationProfile':tnSapIsaAaApplicationProfile,'tnSapEthRingIndex':tnSapEthRingIndex,'tnSapAlmProfName':tnSapAlmProfName,'tnSapTlsInfoTable':tnSapTlsInfoTable,'tnSapTlsInfoEntry':tnSapTlsInfoEntry,'tnSapTlsStpAdminStatus':tnSapTlsStpAdminStatus,'tnSapTlsStpPriority':tnSapTlsStpPriority,'tnSapTlsStpPortNum':tnSapTlsStpPortNum,'tnSapTlsStpPathCost':tnSapTlsStpPathCost,'tnSapTlsStpRapidStart':tnSapTlsStpRapidStart,'tnSapTlsStpBpduEncap':tnSapTlsStpBpduEncap,'tnSapTlsStpPortState':tnSapTlsStpPortState,'tnSapTlsStpDesignatedBridge':tnSapTlsStpDesignatedBridge,'tnSapTlsStpDesignatedPort':tnSapTlsStpDesignatedPort,'tnSapTlsStpForwardTransitions':tnSapTlsStpForwardTransitions,'tnSapTlsStpInConfigBpdus':tnSapTlsStpInConfigBpdus,'tnSapTlsStpInTcnBpdus':tnSapTlsStpInTcnBpdus,'tnSapTlsStpInBadBpdus':tnSapTlsStpInBadBpdus,'tnSapTlsStpOutConfigBpdus':tnSapTlsStpOutConfigBpdus,'tnSapTlsStpOutTcnBpdus':tnSapTlsStpOutTcnBpdus,'tnSapTlsStpOperBpduEncap':tnSapTlsStpOperBpduEncap,'tnSapTlsVpnId':tnSapTlsVpnId,'tnSapTlsCustId':tnSapTlsCustId,'tnSapTlsMacAddressLimit':tnSapTlsMacAddressLimit,'tnSapTlsNumMacAddresses':tnSapTlsNumMacAddresses,'tnSapTlsNumStaticMacAddresses':tnSapTlsNumStaticMacAddresses,'tnSapTlsMacLearning':tnSapTlsMacLearning,'tnSapTlsMacAgeing':tnSapTlsMacAgeing,'tnSapTlsStpOperEdge':tnSapTlsStpOperEdge,'tnSapTlsStpAdminPointToPoint':tnSapTlsStpAdminPointToPoint,'tnSapTlsStpPortRole':tnSapTlsStpPortRole,'tnSapTlsStpAutoEdge':tnSapTlsStpAutoEdge,_y:tnSapTlsStpOperProtocol,'tnSapTlsStpInRstBpdus':tnSapTlsStpInRstBpdus,'tnSapTlsStpOutRstBpdus':tnSapTlsStpOutRstBpdus,'tnSapTlsLimitMacMove':tnSapTlsLimitMacMove,'tnSapTlsMacPinning':tnSapTlsMacPinning,'tnSapTlsDiscardUnknownSource':tnSapTlsDiscardUnknownSource,'tnSapTlsMvplsPruneState':tnSapTlsMvplsPruneState,'tnSapTlsMvplsMgmtService':tnSapTlsMvplsMgmtService,'tnSapTlsMvplsMgmtPortId':tnSapTlsMvplsMgmtPortId,'tnSapTlsMvplsMgmtEncapValue':tnSapTlsMvplsMgmtEncapValue,'tnSapTlsArpReplyAgent':tnSapTlsArpReplyAgent,_A0:tnSapTlsStpException,'tnSapTlsAuthenticationPolicy':tnSapTlsAuthenticationPolicy,'tnSapTlsL2ptTermination':tnSapTlsL2ptTermination,'tnSapTlsBpduTranslation':tnSapTlsBpduTranslation,'tnSapTlsStpRootGuard':tnSapTlsStpRootGuard,'tnSapTlsStpInsideRegion':tnSapTlsStpInsideRegion,'tnSapTlsEgressMcastGroup':tnSapTlsEgressMcastGroup,'tnSapTlsStpInMstBpdus':tnSapTlsStpInMstBpdus,'tnSapTlsStpOutMstBpdus':tnSapTlsStpOutMstBpdus,'tnSapTlsRestProtSrcMac':tnSapTlsRestProtSrcMac,'tnSapTlsRestUnprotDstMac':tnSapTlsRestUnprotDstMac,'tnSapTlsStpRxdDesigBridge':tnSapTlsStpRxdDesigBridge,_z:tnSapTlsStpRootGuardViolation,'tnSapTlsShcvAction':tnSapTlsShcvAction,'tnSapTlsShcvSrcIp':tnSapTlsShcvSrcIp,'tnSapTlsShcvSrcMac':tnSapTlsShcvSrcMac,'tnSapTlsShcvInterval':tnSapTlsShcvInterval,'tnSapTlsMvplsMgmtMsti':tnSapTlsMvplsMgmtMsti,'tnSapTlsMacMoveNextUpTime':tnSapTlsMacMoveNextUpTime,'tnSapTlsMacMoveRateExcdLeft':tnSapTlsMacMoveRateExcdLeft,'tnSapTlsRestProtSrcMacAction':tnSapTlsRestProtSrcMacAction,'tnSapTlsL2ptForceBoundary':tnSapTlsL2ptForceBoundary,'tnSapTlsLimitMacMoveLevel':tnSapTlsLimitMacMoveLevel,'tnSapTlsBpduTransOper':tnSapTlsBpduTransOper,'tnSapTlsDefMtnSapPolicy':tnSapTlsDefMtnSapPolicy,'tnSapTlsL2ptProtocols':tnSapTlsL2ptProtocols,'tnSapTlsL2ptForceProtocols':tnSapTlsL2ptForceProtocols,'tnSapTlsPppoeMtnSapTrigger':tnSapTlsPppoeMtnSapTrigger,'tnSapTlsDhcpMtnSapTrigger':tnSapTlsDhcpMtnSapTrigger,'tnSapTlsMrpJoinTime':tnSapTlsMrpJoinTime,'tnSapTlsMrpLeaveTime':tnSapTlsMrpLeaveTime,'tnSapTlsMrpLeaveAllTime':tnSapTlsMrpLeaveAllTime,'tnSapTlsMrpPeriodicTime':tnSapTlsMrpPeriodicTime,'tnSapTlsMrpPeriodicEnabled':tnSapTlsMrpPeriodicEnabled,'tnSapTlsPppoePolicy':tnSapTlsPppoePolicy,'tnSapTlsArpMsapTrigger':tnSapTlsArpMsapTrigger,'tnSapTlsInTcBitBpdus':tnSapTlsInTcBitBpdus,'tnSapTlsOutTcBitBpdus':tnSapTlsOutTcBitBpdus,'tnSapTlsShcvRetryTimeout':tnSapTlsShcvRetryTimeout,'tnSapTlsShcvRetryCount':tnSapTlsShcvRetryCount,'tnSapTlsFdbTableSizeProfId':tnSapTlsFdbTableSizeProfId,'tnSapScalar1':tnSapScalar1,'tnSapBaseStatsTable':tnSapBaseStatsTable,'tnSapBaseStatsEntry':tnSapBaseStatsEntry,'tnSapBaseStatsIngressPchipDroppedPackets':tnSapBaseStatsIngressPchipDroppedPackets,'tnSapBaseStatsIngressPchipDroppedOctets':tnSapBaseStatsIngressPchipDroppedOctets,'tnSapBaseStatsIngressPchipOfferedHiPrioPackets':tnSapBaseStatsIngressPchipOfferedHiPrioPackets,'tnSapBaseStatsIngressPchipOfferedHiPrioOctets':tnSapBaseStatsIngressPchipOfferedHiPrioOctets,'tnSapBaseStatsIngressPchipOfferedLoPrioPackets':tnSapBaseStatsIngressPchipOfferedLoPrioPackets,'tnSapBaseStatsIngressPchipOfferedLoPrioOctets':tnSapBaseStatsIngressPchipOfferedLoPrioOctets,'tnSapBaseStatsIngressQchipDroppedHiPrioPackets':tnSapBaseStatsIngressQchipDroppedHiPrioPackets,'tnSapBaseStatsIngressQchipDroppedHiPrioOctets':tnSapBaseStatsIngressQchipDroppedHiPrioOctets,'tnSapBaseStatsIngressQchipDroppedLoPrioPackets':tnSapBaseStatsIngressQchipDroppedLoPrioPackets,'tnSapBaseStatsIngressQchipDroppedLoPrioOctets':tnSapBaseStatsIngressQchipDroppedLoPrioOctets,'tnSapBaseStatsIngressQchipForwardedInProfPackets':tnSapBaseStatsIngressQchipForwardedInProfPackets,'tnSapBaseStatsIngressQchipForwardedInProfOctets':tnSapBaseStatsIngressQchipForwardedInProfOctets,'tnSapBaseStatsIngressQchipForwardedOutProfPackets':tnSapBaseStatsIngressQchipForwardedOutProfPackets,'tnSapBaseStatsIngressQchipForwardedOutProfOctets':tnSapBaseStatsIngressQchipForwardedOutProfOctets,'tnSapBaseStatsEgressQchipDroppedInProfPackets':tnSapBaseStatsEgressQchipDroppedInProfPackets,'tnSapBaseStatsEgressQchipDroppedInProfOctets':tnSapBaseStatsEgressQchipDroppedInProfOctets,'tnSapBaseStatsEgressQchipDroppedOutProfPackets':tnSapBaseStatsEgressQchipDroppedOutProfPackets,'tnSapBaseStatsEgressQchipDroppedOutProfOctets':tnSapBaseStatsEgressQchipDroppedOutProfOctets,'tnSapBaseStatsEgressQchipForwardedInProfPackets':tnSapBaseStatsEgressQchipForwardedInProfPackets,'tnSapBaseStatsEgressQchipForwardedInProfOctets':tnSapBaseStatsEgressQchipForwardedInProfOctets,'tnSapBaseStatsEgressQchipForwardedOutProfPackets':tnSapBaseStatsEgressQchipForwardedOutProfPackets,'tnSapBaseStatsEgressQchipForwardedOutProfOctets':tnSapBaseStatsEgressQchipForwardedOutProfOctets,'tnSapBaseStatsCustId':tnSapBaseStatsCustId,'tnSapBaseStatsIngressPchipOfferedUncoloredPackets':tnSapBaseStatsIngressPchipOfferedUncoloredPackets,'tnSapBaseStatsIngressPchipOfferedUncoloredOctets':tnSapBaseStatsIngressPchipOfferedUncoloredOctets,'tnSapBaseStatsAuthenticationPktsDiscarded':tnSapBaseStatsAuthenticationPktsDiscarded,'tnSapBaseStatsAuthenticationPktsSuccess':tnSapBaseStatsAuthenticationPktsSuccess,'tnSapBaseStatsLastClearedTime':tnSapBaseStatsLastClearedTime,'tnSapEthernetInfoTable':tnSapEthernetInfoTable,'tnSapEthernetInfoEntry':tnSapEthernetInfoEntry,'tnSapEthernetLLFAdminStatus':tnSapEthernetLLFAdminStatus,'tnSapEthernetLLFOperStatus':tnSapEthernetLLFOperStatus,'tnSapEthernetLLFId':tnSapEthernetLLFId,'tnSapEthernetLoopbackMode':tnSapEthernetLoopbackMode,'tnSapEthernetLoopbackMacSwapStaticMac':tnSapEthernetLoopbackMacSwapStaticMac,'tnSapTrapsPrefix':tnSapTrapsPrefix,'tnSapTraps':tnSapTraps,'tnSapStatusChanged':tnSapStatusChanged,'tnSapTlsMacAddrLimitAlarmRaised':tnSapTlsMacAddrLimitAlarmRaised,'tnSapTlsMacAddrLimitAlarmCleared':tnSapTlsMacAddrLimitAlarmCleared,'tnSapDHCPLseStateMobilityError':tnSapDHCPLseStateMobilityError,'tnTopologyChangeSapMajorState':tnTopologyChangeSapMajorState,'tnNewRootSap':tnNewRootSap,'tnTopologyChangeSapState':tnTopologyChangeSapState,'tnReceivedTCN':tnReceivedTCN,'tnSapActiveProtocolChange':tnSapActiveProtocolChange,'tnStpRootGuardViolation':tnStpRootGuardViolation,'tnSapStpExcepCondStateChng':tnSapStpExcepCondStateChng})