_AZ='sdpPwPortId'
_AY='pwTemplateIgmpSnpgSrcAddr'
_AX='pwTemplateIgmpSnpgSrcAddrType'
_AW='pwTemplateIgmpSnpgGrpAddr'
_AV='pwTemplateIgmpSnpgGrpAddrType'
_AU='sdpFCMappingFCName'
_AT='deprecated'
_AS='pwFwdingStandby'
_AR='psnEgressFault'
_AQ='psnIngressFault'
_AP='lacEgresssFault'
_AO='lacIngressFault'
_AN='pwNotForwarding'
_AM='withdrawnIngressVcLabel'
_AL='operGrpDown'
_AK='standbySigSlaveTxDown'
_AJ='oamUpMepFault'
_AI='oamDownMepFault'
_AH='mhStandby'
_AG='outOfResource'
_AF='notManagedByMcRing'
_AE='meshSdpDown'
_AD='pwPeerFaultStatusBits'
_AC='insufficientBandwidth'
_AB='svcParamMismatch'
_AA='labelsExhausted'
_A9='releasedIngressVcLabel'
_A8='iesIfAdminDown'
_A7='relearnLimitExceeded'
_A6='vcTypeMismatch'
_A5='noEgressVcLabel'
_A4='noIngressVcLabel'
_A3='sdpOperDown'
_A2='sapOperDown'
_A1='svcAdminDown'
_A0='sdpBindAdminDown'
_z='accessible-for-notify'
_y='disabled'
_x='transportTunnelDown'
_w='invalidEgressInterface'
_v='TmnxVPNRouteDistinguisher'
_u='TmnxPortID'
_t='TmnxIgmpVersion'
_s='TmnxBsxTransitIpPolicyIdOrZero'
_r='TmnxBsxTransPrefPolicyIdOrZero'
_q='TmnxBsxAarpServiceRefType'
_p='TmnxBsxAarpIdOrZero'
_o='TSdpIngressPolicyID'
_n='TSdpEgressPolicyID'
_m='TItemDescription'
_l='TFdbTableSizeProfileID'
_k='TCpmProtPolicyID'
_j='ServObjDesc'
_i='TlsLimitMacMove'
_h='SdpBindVcType'
_g='SdpBindBandwidth'
_f='pwTemplateId'
_e='sdpPathMtuTooSmall'
_d='svcMtuMismatch'
_c='down'
_b='TmnxVRtrMplsLspID'
_a='TQosQGrpInstanceIDorZero'
_Z='sdpId'
_Y='TmnxMplsTpNodeID'
_X='TmnxMplsTpGlobalID'
_W='ServiceAdminStatus'
_V='ServObjName'
_U='InetAddress'
_T='sdpBindId'
_S='kilo-bits per second'
_R='tnSvcId'
_Q='TN-SERV-MIB'
_P='seconds'
_O='TFilterID'
_N='TmnxEnabledDisabled'
_M='TNamedItemOrEmpty'
_L='not-accessible'
_K='Bits'
_J='tnSysSwitchId'
_I='TROPIC-SYSTEM-MIB'
_H='TN-SDP-MIB'
_G='TruthValue'
_F='Integer32'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_U,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
L2RouteOrigin,LspIdList,PWTemplateId,SdpBindBandwidth,SdpBindVcType,SdpId,ServObjName,TlsLimitMacMove,VpnId,tnServObjs,tnSvcId=mibBuilder.importSymbols(_Q,'L2RouteOrigin','LspIdList','PWTemplateId',_g,_h,'SdpId',_V,_i,'VpnId','tnServObjs',_R)
SdpBindId,ServObjDesc,ServiceAdminStatus,TCpmProtPolicyID,TFdbTableSizeProfileID,TFilterID,TItemDescription,TNamedItem,TNamedItemOrEmpty,TQosQGrpInstanceIDorZero,TSdpEgressPolicyID,TSdpIngressPolicyID,TmnxBsxAarpIdOrZero,TmnxBsxAarpServiceRefType,TmnxBsxTransPrefPolicyIdOrZero,TmnxBsxTransitIpPolicyIdOrZero,TmnxCustId,TmnxEnabledDisabled,TmnxIgmpVersion,TmnxMplsTpGlobalID,TmnxMplsTpNodeID,TmnxOperState,TmnxPortID,TmnxServId,TmnxVPNRouteDistinguisher,TmnxVRtrMplsLspID,TmnxVcId=mibBuilder.importSymbols('TN-TC-MIB','SdpBindId',_j,_W,_k,_l,_O,_m,'TNamedItem',_M,_a,_n,_o,_p,_q,_r,_s,'TmnxCustId',_N,_t,_X,_Y,'TmnxOperState',_u,'TmnxServId',_v,_b,'TmnxVcId')
tnSRMIBModules,=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules')
tnSysSwitchId,=mibBuilder.importSymbols(_I,_J)
tnServicesSdpMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,56))
if mibBuilder.loadTexts:tnServicesSdpMIBModule.setRevisions(('2020-08-21 00:00','2019-08-30 00:00','2019-08-16 00:00','2018-12-21 00:00','2018-08-31 00:00','2018-07-20 00:00','2015-08-13 00:00','2015-06-16 00:00','2011-02-01 00:00','2009-02-28 00:00','2008-07-01 00:00','2007-10-01 00:00'))
_TnSdpObjs_ObjectIdentity=ObjectIdentity
tnSdpObjs=_TnSdpObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,4,4))
_SdpNumEntries_Type=Integer32
_SdpNumEntries_Object=MibScalar
sdpNumEntries=_SdpNumEntries_Object((1,3,6,1,4,1,7483,6,1,2,4,4,1),_SdpNumEntries_Type())
sdpNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpNumEntries.setStatus(_A)
_SdpNextFreeId_Type=SdpId
_SdpNextFreeId_Object=MibScalar
sdpNextFreeId=_SdpNextFreeId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,2),_SdpNextFreeId_Type())
sdpNextFreeId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpNextFreeId.setStatus(_A)
_SdpInfoTable_Object=MibTable
sdpInfoTable=_SdpInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3))
if mibBuilder.loadTexts:sdpInfoTable.setStatus(_A)
_SdpInfoEntry_Object=MibTableRow
sdpInfoEntry=_SdpInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1))
sdpInfoEntry.setIndexNames((0,_I,_J),(0,_H,_Z))
if mibBuilder.loadTexts:sdpInfoEntry.setStatus(_A)
_SdpId_Type=SdpId
_SdpId_Object=MibTableColumn
sdpId=_SdpId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,1),_SdpId_Type())
sdpId.setMaxAccess(_L)
if mibBuilder.loadTexts:sdpId.setStatus(_A)
_SdpRowStatus_Type=RowStatus
_SdpRowStatus_Object=MibTableColumn
sdpRowStatus=_SdpRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,2),_SdpRowStatus_Type())
sdpRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpRowStatus.setStatus(_A)
class _SdpDelivery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gre',1),('mpls',2)))
_SdpDelivery_Type.__name__=_F
_SdpDelivery_Object=MibTableColumn
sdpDelivery=_SdpDelivery_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,3),_SdpDelivery_Type())
sdpDelivery.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpDelivery.setStatus(_A)
_SdpFarEndIpAddress_Type=IpAddress
_SdpFarEndIpAddress_Object=MibTableColumn
sdpFarEndIpAddress=_SdpFarEndIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,4),_SdpFarEndIpAddress_Type())
sdpFarEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpFarEndIpAddress.setStatus(_A)
_SdpLspList_Type=LspIdList
_SdpLspList_Object=MibTableColumn
sdpLspList=_SdpLspList_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,5),_SdpLspList_Type())
sdpLspList.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpLspList.setStatus(_A)
class _SdpDescription_Type(ServObjDesc):defaultValue=OctetString('')
_SdpDescription_Type.__name__=_j
_SdpDescription_Object=MibTableColumn
sdpDescription=_SdpDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,6),_SdpDescription_Type())
sdpDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpDescription.setStatus(_A)
class _SdpLabelSignaling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('tldp',2),('bgp',3)))
_SdpLabelSignaling_Type.__name__=_F
_SdpLabelSignaling_Object=MibTableColumn
sdpLabelSignaling=_SdpLabelSignaling_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,7),_SdpLabelSignaling_Type())
sdpLabelSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpLabelSignaling.setStatus(_A)
class _SdpAdminStatus_Type(ServiceAdminStatus):defaultValue=2
_SdpAdminStatus_Type.__name__=_W
_SdpAdminStatus_Object=MibTableColumn
sdpAdminStatus=_SdpAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,8),_SdpAdminStatus_Type())
sdpAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpAdminStatus.setStatus(_A)
class _SdpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('up',1),('notAlive',2),('notReady',3),(_w,4),(_x,5),(_c,6)))
_SdpOperStatus_Type.__name__=_F
_SdpOperStatus_Object=MibTableColumn
sdpOperStatus=_SdpOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,9),_SdpOperStatus_Type())
sdpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpOperStatus.setStatus(_A)
class _SdpAdminPathMtu_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1518,9586))
_SdpAdminPathMtu_Type.__name__=_F
_SdpAdminPathMtu_Object=MibTableColumn
sdpAdminPathMtu=_SdpAdminPathMtu_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,10),_SdpAdminPathMtu_Type())
sdpAdminPathMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpAdminPathMtu.setStatus(_A)
_SdpOperPathMtu_Type=Integer32
_SdpOperPathMtu_Object=MibTableColumn
sdpOperPathMtu=_SdpOperPathMtu_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,11),_SdpOperPathMtu_Type())
sdpOperPathMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpOperPathMtu.setStatus(_A)
class _SdpKeepAliveAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_y,2)))
_SdpKeepAliveAdminStatus_Type.__name__=_F
_SdpKeepAliveAdminStatus_Object=MibTableColumn
sdpKeepAliveAdminStatus=_SdpKeepAliveAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,12),_SdpKeepAliveAdminStatus_Type())
sdpKeepAliveAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveAdminStatus.setStatus(_A)
class _SdpKeepAliveOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('alive',1),('noResponse',2),('senderIdInvalid',3),('responderIdError',4),(_y,5)))
_SdpKeepAliveOperStatus_Type.__name__=_F
_SdpKeepAliveOperStatus_Object=MibTableColumn
sdpKeepAliveOperStatus=_SdpKeepAliveOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,13),_SdpKeepAliveOperStatus_Type())
sdpKeepAliveOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpKeepAliveOperStatus.setStatus(_A)
class _SdpKeepAliveHelloTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_SdpKeepAliveHelloTime_Type.__name__=_F
_SdpKeepAliveHelloTime_Object=MibTableColumn
sdpKeepAliveHelloTime=_SdpKeepAliveHelloTime_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,14),_SdpKeepAliveHelloTime_Type())
sdpKeepAliveHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveHelloTime.setStatus(_A)
class _SdpKeepAliveMaxDropCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_SdpKeepAliveMaxDropCount_Type.__name__=_F
_SdpKeepAliveMaxDropCount_Object=MibTableColumn
sdpKeepAliveMaxDropCount=_SdpKeepAliveMaxDropCount_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,15),_SdpKeepAliveMaxDropCount_Type())
sdpKeepAliveMaxDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveMaxDropCount.setStatus(_A)
class _SdpKeepAliveHoldDownTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_SdpKeepAliveHoldDownTime_Type.__name__=_F
_SdpKeepAliveHoldDownTime_Object=MibTableColumn
sdpKeepAliveHoldDownTime=_SdpKeepAliveHoldDownTime_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,16),_SdpKeepAliveHoldDownTime_Type())
sdpKeepAliveHoldDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveHoldDownTime.setStatus(_A)
_SdpLastMgmtChange_Type=TimeStamp
_SdpLastMgmtChange_Object=MibTableColumn
sdpLastMgmtChange=_SdpLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,17),_SdpLastMgmtChange_Type())
sdpLastMgmtChange.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpLastMgmtChange.setStatus(_A)
class _SdpKeepAliveHelloMessageLength_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(40,9198))
_SdpKeepAliveHelloMessageLength_Type.__name__=_F
_SdpKeepAliveHelloMessageLength_Object=MibTableColumn
sdpKeepAliveHelloMessageLength=_SdpKeepAliveHelloMessageLength_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,18),_SdpKeepAliveHelloMessageLength_Type())
sdpKeepAliveHelloMessageLength.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveHelloMessageLength.setStatus(_A)
_SdpKeepAliveNumHelloRequestMessages_Type=Unsigned32
_SdpKeepAliveNumHelloRequestMessages_Object=MibTableColumn
sdpKeepAliveNumHelloRequestMessages=_SdpKeepAliveNumHelloRequestMessages_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,19),_SdpKeepAliveNumHelloRequestMessages_Type())
sdpKeepAliveNumHelloRequestMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpKeepAliveNumHelloRequestMessages.setStatus(_A)
_SdpKeepAliveNumHelloResponseMessages_Type=Unsigned32
_SdpKeepAliveNumHelloResponseMessages_Object=MibTableColumn
sdpKeepAliveNumHelloResponseMessages=_SdpKeepAliveNumHelloResponseMessages_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,20),_SdpKeepAliveNumHelloResponseMessages_Type())
sdpKeepAliveNumHelloResponseMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpKeepAliveNumHelloResponseMessages.setStatus(_A)
_SdpKeepAliveNumLateHelloResponseMessages_Type=Unsigned32
_SdpKeepAliveNumLateHelloResponseMessages_Object=MibTableColumn
sdpKeepAliveNumLateHelloResponseMessages=_SdpKeepAliveNumLateHelloResponseMessages_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,21),_SdpKeepAliveNumLateHelloResponseMessages_Type())
sdpKeepAliveNumLateHelloResponseMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpKeepAliveNumLateHelloResponseMessages.setStatus(_A)
class _SdpKeepAliveHelloRequestTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SdpKeepAliveHelloRequestTimeout_Type.__name__=_F
_SdpKeepAliveHelloRequestTimeout_Object=MibTableColumn
sdpKeepAliveHelloRequestTimeout=_SdpKeepAliveHelloRequestTimeout_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,22),_SdpKeepAliveHelloRequestTimeout_Type())
sdpKeepAliveHelloRequestTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpKeepAliveHelloRequestTimeout.setStatus(_A)
class _SdpLdpEnabled_Type(TruthValue):defaultValue=2
_SdpLdpEnabled_Type.__name__=_G
_SdpLdpEnabled_Object=MibTableColumn
sdpLdpEnabled=_SdpLdpEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,23),_SdpLdpEnabled_Type())
sdpLdpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpLdpEnabled.setStatus(_A)
class _SdpVlanVcEtype_Type(Unsigned32):defaultValue=33024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_SdpVlanVcEtype_Type.__name__=_D
_SdpVlanVcEtype_Object=MibTableColumn
sdpVlanVcEtype=_SdpVlanVcEtype_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,24),_SdpVlanVcEtype_Type())
sdpVlanVcEtype.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpVlanVcEtype.setStatus(_A)
class _SdpAdvertisedVllMtuOverride_Type(TruthValue):defaultValue=2
_SdpAdvertisedVllMtuOverride_Type.__name__=_G
_SdpAdvertisedVllMtuOverride_Object=MibTableColumn
sdpAdvertisedVllMtuOverride=_SdpAdvertisedVllMtuOverride_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,25),_SdpAdvertisedVllMtuOverride_Type())
sdpAdvertisedVllMtuOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpAdvertisedVllMtuOverride.setStatus(_A)
class _SdpOperFlags_Type(Bits):namedValues=NamedValues(*(('sdpAdminDown',0),('signalingSessionDown',1),(_x,2),('keepaliveFailure',3),(_w,4),('noSystemIpAddress',5),('transportTunnelUnstable',6),('notOnBindingPort',7)))
_SdpOperFlags_Type.__name__=_K
_SdpOperFlags_Object=MibTableColumn
sdpOperFlags=_SdpOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,26),_SdpOperFlags_Type())
sdpOperFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpOperFlags.setStatus(_A)
_SdpLastStatusChange_Type=TimeStamp
_SdpLastStatusChange_Object=MibTableColumn
sdpLastStatusChange=_SdpLastStatusChange_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,27),_SdpLastStatusChange_Type())
sdpLastStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpLastStatusChange.setStatus(_A)
_SdpMvplsMgmtService_Type=TmnxServId
_SdpMvplsMgmtService_Object=MibTableColumn
sdpMvplsMgmtService=_SdpMvplsMgmtService_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,28),_SdpMvplsMgmtService_Type())
sdpMvplsMgmtService.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpMvplsMgmtService.setStatus(_A)
_SdpMvplsMgmtSdpBndId_Type=SdpBindId
_SdpMvplsMgmtSdpBndId_Object=MibTableColumn
sdpMvplsMgmtSdpBndId=_SdpMvplsMgmtSdpBndId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,29),_SdpMvplsMgmtSdpBndId_Type())
sdpMvplsMgmtSdpBndId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpMvplsMgmtSdpBndId.setStatus(_A)
class _SdpCollectAcctStats_Type(TruthValue):defaultValue=2
_SdpCollectAcctStats_Type.__name__=_G
_SdpCollectAcctStats_Object=MibTableColumn
sdpCollectAcctStats=_SdpCollectAcctStats_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,30),_SdpCollectAcctStats_Type())
sdpCollectAcctStats.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpCollectAcctStats.setStatus(_A)
class _SdpAccountingPolicyId_Type(Unsigned32):defaultValue=0
_SdpAccountingPolicyId_Type.__name__=_D
_SdpAccountingPolicyId_Object=MibTableColumn
sdpAccountingPolicyId=_SdpAccountingPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,31),_SdpAccountingPolicyId_Type())
sdpAccountingPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpAccountingPolicyId.setStatus(_A)
class _SdpClassFwdingEnabled_Type(TruthValue):defaultValue=2
_SdpClassFwdingEnabled_Type.__name__=_G
_SdpClassFwdingEnabled_Object=MibTableColumn
sdpClassFwdingEnabled=_SdpClassFwdingEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,32),_SdpClassFwdingEnabled_Type())
sdpClassFwdingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpClassFwdingEnabled.setStatus(_A)
class _SdpClassFwdingDefaultLsp_Type(TmnxVRtrMplsLspID):defaultValue=0
_SdpClassFwdingDefaultLsp_Type.__name__=_b
_SdpClassFwdingDefaultLsp_Object=MibTableColumn
sdpClassFwdingDefaultLsp=_SdpClassFwdingDefaultLsp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,33),_SdpClassFwdingDefaultLsp_Type())
sdpClassFwdingDefaultLsp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpClassFwdingDefaultLsp.setStatus(_A)
class _SdpClassFwdingMcLsp_Type(TmnxVRtrMplsLspID):defaultValue=0
_SdpClassFwdingMcLsp_Type.__name__=_b
_SdpClassFwdingMcLsp_Object=MibTableColumn
sdpClassFwdingMcLsp=_SdpClassFwdingMcLsp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,34),_SdpClassFwdingMcLsp_Type())
sdpClassFwdingMcLsp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpClassFwdingMcLsp.setStatus(_A)
class _SdpMetric_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SdpMetric_Type.__name__=_D
_SdpMetric_Object=MibTableColumn
sdpMetric=_SdpMetric_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,35),_SdpMetric_Type())
sdpMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpMetric.setStatus(_A)
_SdpAutoSdp_Type=TruthValue
_SdpAutoSdp_Object=MibTableColumn
sdpAutoSdp=_SdpAutoSdp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,36),_SdpAutoSdp_Type())
sdpAutoSdp.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpAutoSdp.setStatus(_A)
_SdpSnmpAllowed_Type=TruthValue
_SdpSnmpAllowed_Object=MibTableColumn
sdpSnmpAllowed=_SdpSnmpAllowed_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,37),_SdpSnmpAllowed_Type())
sdpSnmpAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpSnmpAllowed.setStatus(_A)
class _SdpPBBEtype_Type(Unsigned32):defaultValue=35047;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1536,65535))
_SdpPBBEtype_Type.__name__=_D
_SdpPBBEtype_Object=MibTableColumn
sdpPBBEtype=_SdpPBBEtype_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,38),_SdpPBBEtype_Type())
sdpPBBEtype.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPBBEtype.setStatus(_A)
class _SdpBandwidthBookingFactor_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_SdpBandwidthBookingFactor_Type.__name__=_D
_SdpBandwidthBookingFactor_Object=MibTableColumn
sdpBandwidthBookingFactor=_SdpBandwidthBookingFactor_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,39),_SdpBandwidthBookingFactor_Type())
sdpBandwidthBookingFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBandwidthBookingFactor.setStatus(_A)
_SdpOperBandwidth_Type=Unsigned32
_SdpOperBandwidth_Object=MibTableColumn
sdpOperBandwidth=_SdpOperBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,40),_SdpOperBandwidth_Type())
sdpOperBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpOperBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpOperBandwidth.setUnits(_S)
_SdpAvailableBandwidth_Type=Unsigned32
_SdpAvailableBandwidth_Object=MibTableColumn
sdpAvailableBandwidth=_SdpAvailableBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,41),_SdpAvailableBandwidth_Type())
sdpAvailableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpAvailableBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpAvailableBandwidth.setUnits(_S)
_SdpMaxBookableBandwidth_Type=Unsigned32
_SdpMaxBookableBandwidth_Object=MibTableColumn
sdpMaxBookableBandwidth=_SdpMaxBookableBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,42),_SdpMaxBookableBandwidth_Type())
sdpMaxBookableBandwidth.setMaxAccess(_z)
if mibBuilder.loadTexts:sdpMaxBookableBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpMaxBookableBandwidth.setUnits(_S)
_SdpBookedBandwidth_Type=Unsigned32
_SdpBookedBandwidth_Object=MibTableColumn
sdpBookedBandwidth=_SdpBookedBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,43),_SdpBookedBandwidth_Type())
sdpBookedBandwidth.setMaxAccess(_z)
if mibBuilder.loadTexts:sdpBookedBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpBookedBandwidth.setUnits(_S)
_SdpCreationOrigin_Type=L2RouteOrigin
_SdpCreationOrigin_Object=MibTableColumn
sdpCreationOrigin=_SdpCreationOrigin_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,44),_SdpCreationOrigin_Type())
sdpCreationOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpCreationOrigin.setStatus(_A)
class _SdpEnforceDiffServLspFc_Type(TruthValue):defaultValue=2
_SdpEnforceDiffServLspFc_Type.__name__=_G
_SdpEnforceDiffServLspFc_Object=MibTableColumn
sdpEnforceDiffServLspFc=_SdpEnforceDiffServLspFc_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,45),_SdpEnforceDiffServLspFc_Type())
sdpEnforceDiffServLspFc.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpEnforceDiffServLspFc.setStatus(_A)
class _SdpMixedLspModeEnabled_Type(TruthValue):defaultValue=2
_SdpMixedLspModeEnabled_Type.__name__=_G
_SdpMixedLspModeEnabled_Object=MibTableColumn
sdpMixedLspModeEnabled=_SdpMixedLspModeEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,46),_SdpMixedLspModeEnabled_Type())
sdpMixedLspModeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpMixedLspModeEnabled.setStatus(_A)
class _SdpLspRevertTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,600))
_SdpLspRevertTime_Type.__name__=_F
_SdpLspRevertTime_Object=MibTableColumn
sdpLspRevertTime=_SdpLspRevertTime_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,47),_SdpLspRevertTime_Type())
sdpLspRevertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpLspRevertTime.setStatus(_A)
if mibBuilder.loadTexts:sdpLspRevertTime.setUnits(_P)
class _SdpLspRevertTimeCountDown_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,600))
_SdpLspRevertTimeCountDown_Type.__name__=_F
_SdpLspRevertTimeCountDown_Object=MibTableColumn
sdpLspRevertTimeCountDown=_SdpLspRevertTimeCountDown_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,48),_SdpLspRevertTimeCountDown_Type())
sdpLspRevertTimeCountDown.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpLspRevertTimeCountDown.setStatus(_A)
if mibBuilder.loadTexts:sdpLspRevertTimeCountDown.setUnits(_P)
_SdpLdpLspId_Type=Unsigned32
_SdpLdpLspId_Object=MibTableColumn
sdpLdpLspId=_SdpLdpLspId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,49),_SdpLdpLspId_Type())
sdpLdpLspId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpLdpLspId.setStatus(_A)
_SdpLdpActive_Type=TruthValue
_SdpLdpActive_Object=MibTableColumn
sdpLdpActive=_SdpLdpActive_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,50),_SdpLdpActive_Type())
sdpLdpActive.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpLdpActive.setStatus('obsolete')
class _SdpNetDomainName_Type(TNamedItemOrEmpty):defaultValue=OctetString('default')
_SdpNetDomainName_Type.__name__=_M
_SdpNetDomainName_Object=MibTableColumn
sdpNetDomainName=_SdpNetDomainName_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,51),_SdpNetDomainName_Type())
sdpNetDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpNetDomainName.setStatus(_A)
class _SdpEgressIfsNetDomainConsistent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('consistent',2),('inconsistent',3)))
_SdpEgressIfsNetDomainConsistent_Type.__name__=_F
_SdpEgressIfsNetDomainConsistent_Object=MibTableColumn
sdpEgressIfsNetDomainConsistent=_SdpEgressIfsNetDomainConsistent_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,52),_SdpEgressIfsNetDomainConsistent_Type())
sdpEgressIfsNetDomainConsistent.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpEgressIfsNetDomainConsistent.setStatus(_A)
class _SdpBgpTunnelEnabled_Type(TruthValue):defaultValue=2
_SdpBgpTunnelEnabled_Type.__name__=_G
_SdpBgpTunnelEnabled_Object=MibTableColumn
sdpBgpTunnelEnabled=_SdpBgpTunnelEnabled_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,53),_SdpBgpTunnelEnabled_Type())
sdpBgpTunnelEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBgpTunnelEnabled.setStatus(_A)
_SdpBgpTunnelLspId_Type=Unsigned32
_SdpBgpTunnelLspId_Object=MibTableColumn
sdpBgpTunnelLspId=_SdpBgpTunnelLspId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,54),_SdpBgpTunnelLspId_Type())
sdpBgpTunnelLspId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBgpTunnelLspId.setStatus(_A)
_SdpTunnelFarEndIpAddress_Type=IpAddress
_SdpTunnelFarEndIpAddress_Object=MibTableColumn
sdpTunnelFarEndIpAddress=_SdpTunnelFarEndIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,55),_SdpTunnelFarEndIpAddress_Type())
sdpTunnelFarEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpTunnelFarEndIpAddress.setStatus(_A)
class _SdpActiveLspType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('not-applicable',0),('rsvp',1),('ldp',2),('bgp',3),('none',4)))
_SdpActiveLspType_Type.__name__=_F
_SdpActiveLspType_Object=MibTableColumn
sdpActiveLspType=_SdpActiveLspType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,56),_SdpActiveLspType_Type())
sdpActiveLspType.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpActiveLspType.setStatus(_A)
class _SdpBindingPort_Type(TmnxPortID):defaultValue=503316480
_SdpBindingPort_Type.__name__=_u
_SdpBindingPort_Object=MibTableColumn
sdpBindingPort=_SdpBindingPort_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,57),_SdpBindingPort_Type())
sdpBindingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindingPort.setStatus(_A)
class _SdpFarEndNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_SdpFarEndNodeId_Type.__name__=_Y
_SdpFarEndNodeId_Object=MibTableColumn
sdpFarEndNodeId=_SdpFarEndNodeId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,58),_SdpFarEndNodeId_Type())
sdpFarEndNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpFarEndNodeId.setStatus(_A)
class _SdpFarEndGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_SdpFarEndGlobalId_Type.__name__=_X
_SdpFarEndGlobalId_Object=MibTableColumn
sdpFarEndGlobalId=_SdpFarEndGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,3,1,59),_SdpFarEndGlobalId_Type())
sdpFarEndGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpFarEndGlobalId.setStatus(_A)
_SdpBindTable_Object=MibTable
sdpBindTable=_SdpBindTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4))
if mibBuilder.loadTexts:sdpBindTable.setStatus(_A)
_SdpBindEntry_Object=MibTableRow
sdpBindEntry=_SdpBindEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1))
sdpBindEntry.setIndexNames((0,_I,_J),(0,_Q,_R),(0,_H,_T))
if mibBuilder.loadTexts:sdpBindEntry.setStatus(_A)
_SdpBindId_Type=SdpBindId
_SdpBindId_Object=MibTableColumn
sdpBindId=_SdpBindId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,1),_SdpBindId_Type())
sdpBindId.setMaxAccess(_L)
if mibBuilder.loadTexts:sdpBindId.setStatus(_A)
_SdpBindRowStatus_Type=RowStatus
_SdpBindRowStatus_Object=MibTableColumn
sdpBindRowStatus=_SdpBindRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,2),_SdpBindRowStatus_Type())
sdpBindRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindRowStatus.setStatus(_A)
class _SdpBindAdminIngressLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1),ValueRangeConstraint(2048,18431))
_SdpBindAdminIngressLabel_Type.__name__=_D
_SdpBindAdminIngressLabel_Object=MibTableColumn
sdpBindAdminIngressLabel=_SdpBindAdminIngressLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,3),_SdpBindAdminIngressLabel_Type())
sdpBindAdminIngressLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAdminIngressLabel.setStatus(_A)
class _SdpBindAdminEgressLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,1048575))
_SdpBindAdminEgressLabel_Type.__name__=_D
_SdpBindAdminEgressLabel_Object=MibTableColumn
sdpBindAdminEgressLabel=_SdpBindAdminEgressLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,4),_SdpBindAdminEgressLabel_Type())
sdpBindAdminEgressLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAdminEgressLabel.setStatus(_A)
class _SdpBindOperIngressLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1048575))
_SdpBindOperIngressLabel_Type.__name__=_D
_SdpBindOperIngressLabel_Object=MibTableColumn
sdpBindOperIngressLabel=_SdpBindOperIngressLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,5),_SdpBindOperIngressLabel_Type())
sdpBindOperIngressLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperIngressLabel.setStatus(_A)
class _SdpBindOperEgressLabel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1048575))
_SdpBindOperEgressLabel_Type.__name__=_D
_SdpBindOperEgressLabel_Object=MibTableColumn
sdpBindOperEgressLabel=_SdpBindOperEgressLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,6),_SdpBindOperEgressLabel_Type())
sdpBindOperEgressLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperEgressLabel.setStatus(_A)
class _SdpBindAdminStatus_Type(ServiceAdminStatus):defaultValue=1
_SdpBindAdminStatus_Type.__name__=_W
_SdpBindAdminStatus_Object=MibTableColumn
sdpBindAdminStatus=_SdpBindAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,7),_SdpBindAdminStatus_Type())
sdpBindAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAdminStatus.setStatus(_A)
class _SdpBindOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('up',1),('noEgressLabel',2),('noIngressLabel',3),('noLabels',4),(_c,5),(_d,6),(_e,7),('sdpNotReady',8),('sdpDown',9),('sapDown',10)))
_SdpBindOperStatus_Type.__name__=_F
_SdpBindOperStatus_Object=MibTableColumn
sdpBindOperStatus=_SdpBindOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,8),_SdpBindOperStatus_Type())
sdpBindOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperStatus.setStatus(_A)
_SdpBindLastMgmtChange_Type=TimeStamp
_SdpBindLastMgmtChange_Object=MibTableColumn
sdpBindLastMgmtChange=_SdpBindLastMgmtChange_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,9),_SdpBindLastMgmtChange_Type())
sdpBindLastMgmtChange.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindLastMgmtChange.setStatus(_A)
class _SdpBindType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('spoke',1),('mesh',2)))
_SdpBindType_Type.__name__=_F
_SdpBindType_Object=MibTableColumn
sdpBindType=_SdpBindType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,10),_SdpBindType_Type())
sdpBindType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindType.setStatus(_A)
class _SdpBindIngressMacFilterId_Type(TFilterID):defaultValue=0
_SdpBindIngressMacFilterId_Type.__name__=_O
_SdpBindIngressMacFilterId_Object=MibTableColumn
sdpBindIngressMacFilterId=_SdpBindIngressMacFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,11),_SdpBindIngressMacFilterId_Type())
sdpBindIngressMacFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressMacFilterId.setStatus(_A)
class _SdpBindIngressIpFilterId_Type(TFilterID):defaultValue=0
_SdpBindIngressIpFilterId_Type.__name__=_O
_SdpBindIngressIpFilterId_Object=MibTableColumn
sdpBindIngressIpFilterId=_SdpBindIngressIpFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,12),_SdpBindIngressIpFilterId_Type())
sdpBindIngressIpFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressIpFilterId.setStatus(_A)
class _SdpBindEgressMacFilterId_Type(TFilterID):defaultValue=0
_SdpBindEgressMacFilterId_Type.__name__=_O
_SdpBindEgressMacFilterId_Object=MibTableColumn
sdpBindEgressMacFilterId=_SdpBindEgressMacFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,13),_SdpBindEgressMacFilterId_Type())
sdpBindEgressMacFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressMacFilterId.setStatus(_A)
class _SdpBindEgressIpFilterId_Type(TFilterID):defaultValue=0
_SdpBindEgressIpFilterId_Type.__name__=_O
_SdpBindEgressIpFilterId_Object=MibTableColumn
sdpBindEgressIpFilterId=_SdpBindEgressIpFilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,14),_SdpBindEgressIpFilterId_Type())
sdpBindEgressIpFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressIpFilterId.setStatus(_A)
_SdpBindVpnId_Type=VpnId
_SdpBindVpnId_Object=MibTableColumn
sdpBindVpnId=_SdpBindVpnId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,15),_SdpBindVpnId_Type())
sdpBindVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindVpnId.setStatus(_A)
_SdpBindCustId_Type=TmnxCustId
_SdpBindCustId_Object=MibTableColumn
sdpBindCustId=_SdpBindCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,16),_SdpBindCustId_Type())
sdpBindCustId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindCustId.setStatus(_A)
_SdpBindVcType_Type=SdpBindVcType
_SdpBindVcType_Object=MibTableColumn
sdpBindVcType=_SdpBindVcType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,17),_SdpBindVcType_Type())
sdpBindVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindVcType.setStatus(_A)
class _SdpBindVlanVcTag_Type(Unsigned32):defaultValue=4095;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SdpBindVlanVcTag_Type.__name__=_D
_SdpBindVlanVcTag_Object=MibTableColumn
sdpBindVlanVcTag=_SdpBindVlanVcTag_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,18),_SdpBindVlanVcTag_Type())
sdpBindVlanVcTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindVlanVcTag.setStatus(_A)
class _SdpBindSplitHorizonGrp_Type(ServObjName):defaultValue=OctetString('')
_SdpBindSplitHorizonGrp_Type.__name__=_V
_SdpBindSplitHorizonGrp_Object=MibTableColumn
sdpBindSplitHorizonGrp=_SdpBindSplitHorizonGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,19),_SdpBindSplitHorizonGrp_Type())
sdpBindSplitHorizonGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindSplitHorizonGrp.setStatus(_A)
class _SdpBindOperFlags_Type(Bits):namedValues=NamedValues(*((_A0,0),(_A1,1),(_A2,2),(_A3,3),(_e,4),(_A4,5),(_A5,6),(_d,7),(_A6,8),(_A7,9),(_A8,10),(_A9,11),(_AA,12),(_AB,13),(_AC,14),(_AD,15),(_AE,16),(_AF,17),(_AG,18),(_AH,19),(_AI,20),(_AJ,21),(_AK,22),(_AL,23),(_AM,24),('vplsPmsiDown',25),('recProtSrcMac',26),('peerFaultStatusTxDown',27)))
_SdpBindOperFlags_Type.__name__=_K
_SdpBindOperFlags_Object=MibTableColumn
sdpBindOperFlags=_SdpBindOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,20),_SdpBindOperFlags_Type())
sdpBindOperFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperFlags.setStatus(_A)
_SdpBindLastStatusChange_Type=TimeStamp
_SdpBindLastStatusChange_Object=MibTableColumn
sdpBindLastStatusChange=_SdpBindLastStatusChange_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,21),_SdpBindLastStatusChange_Type())
sdpBindLastStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindLastStatusChange.setStatus(_A)
_SdpBindIesIfIndex_Type=InterfaceIndexOrZero
_SdpBindIesIfIndex_Object=MibTableColumn
sdpBindIesIfIndex=_SdpBindIesIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,22),_SdpBindIesIfIndex_Type())
sdpBindIesIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIesIfIndex.setStatus(_A)
_SdpBindMacPinning_Type=TmnxEnabledDisabled
_SdpBindMacPinning_Object=MibTableColumn
sdpBindMacPinning=_SdpBindMacPinning_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,23),_SdpBindMacPinning_Type())
sdpBindMacPinning.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindMacPinning.setStatus(_A)
class _SdpBindIngressIpv6FilterId_Type(TFilterID):defaultValue=0
_SdpBindIngressIpv6FilterId_Type.__name__=_O
_SdpBindIngressIpv6FilterId_Object=MibTableColumn
sdpBindIngressIpv6FilterId=_SdpBindIngressIpv6FilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,24),_SdpBindIngressIpv6FilterId_Type())
sdpBindIngressIpv6FilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressIpv6FilterId.setStatus(_A)
class _SdpBindEgressIpv6FilterId_Type(TFilterID):defaultValue=0
_SdpBindEgressIpv6FilterId_Type.__name__=_O
_SdpBindEgressIpv6FilterId_Object=MibTableColumn
sdpBindEgressIpv6FilterId=_SdpBindEgressIpv6FilterId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,25),_SdpBindEgressIpv6FilterId_Type())
sdpBindEgressIpv6FilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressIpv6FilterId.setStatus(_A)
class _SdpBindCollectAcctStats_Type(TruthValue):defaultValue=2
_SdpBindCollectAcctStats_Type.__name__=_G
_SdpBindCollectAcctStats_Object=MibTableColumn
sdpBindCollectAcctStats=_SdpBindCollectAcctStats_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,26),_SdpBindCollectAcctStats_Type())
sdpBindCollectAcctStats.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindCollectAcctStats.setStatus(_A)
class _SdpBindAccountingPolicyId_Type(Unsigned32):defaultValue=0
_SdpBindAccountingPolicyId_Type.__name__=_D
_SdpBindAccountingPolicyId_Object=MibTableColumn
sdpBindAccountingPolicyId=_SdpBindAccountingPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,27),_SdpBindAccountingPolicyId_Type())
sdpBindAccountingPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAccountingPolicyId.setStatus(_A)
class _SdpBindPwPeerStatusBits_Type(Bits):namedValues=NamedValues(*((_AN,0),(_AO,1),(_AP,2),(_AQ,3),(_AR,4),(_AS,5)))
_SdpBindPwPeerStatusBits_Type.__name__=_K
_SdpBindPwPeerStatusBits_Object=MibTableColumn
sdpBindPwPeerStatusBits=_SdpBindPwPeerStatusBits_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,28),_SdpBindPwPeerStatusBits_Type())
sdpBindPwPeerStatusBits.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwPeerStatusBits.setStatus(_A)
class _SdpBindPeerVccvCvBits_Type(Bits):namedValues=NamedValues(*(('icmpPing',0),('lspPing',1),('bfdFaultDetection',2),('bfdFaultDetectionAndSignalling',3)))
_SdpBindPeerVccvCvBits_Type.__name__=_K
_SdpBindPeerVccvCvBits_Object=MibTableColumn
sdpBindPeerVccvCvBits=_SdpBindPeerVccvCvBits_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,29),_SdpBindPeerVccvCvBits_Type())
sdpBindPeerVccvCvBits.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPeerVccvCvBits.setStatus(_A)
class _SdpBindPeerVccvCcBits_Type(Bits):namedValues=NamedValues(*(('pwe3ControlWord',0),('mplsRouterAlertLabel',1),('mplsPwDemultiplexorLabel',2)))
_SdpBindPeerVccvCcBits_Type.__name__=_K
_SdpBindPeerVccvCcBits_Object=MibTableColumn
sdpBindPeerVccvCcBits=_SdpBindPeerVccvCcBits_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,30),_SdpBindPeerVccvCcBits_Type())
sdpBindPeerVccvCcBits.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPeerVccvCcBits.setStatus(_A)
_SdpBindControlWordBit_Type=TruthValue
_SdpBindControlWordBit_Object=MibTableColumn
sdpBindControlWordBit=_SdpBindControlWordBit_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,31),_SdpBindControlWordBit_Type())
sdpBindControlWordBit.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindControlWordBit.setStatus(_A)
_SdpBindOperControlWord_Type=TruthValue
_SdpBindOperControlWord_Object=MibTableColumn
sdpBindOperControlWord=_SdpBindOperControlWord_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,32),_SdpBindOperControlWord_Type())
sdpBindOperControlWord.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperControlWord.setStatus(_A)
class _SdpBindEndPoint_Type(ServObjName):defaultValue=OctetString('')
_SdpBindEndPoint_Type.__name__=_V
_SdpBindEndPoint_Object=MibTableColumn
sdpBindEndPoint=_SdpBindEndPoint_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,33),_SdpBindEndPoint_Type())
sdpBindEndPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEndPoint.setStatus(_A)
class _SdpBindEndPointPrecedence_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_SdpBindEndPointPrecedence_Type.__name__=_D
_SdpBindEndPointPrecedence_Object=MibTableColumn
sdpBindEndPointPrecedence=_SdpBindEndPointPrecedence_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,34),_SdpBindEndPointPrecedence_Type())
sdpBindEndPointPrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEndPointPrecedence.setStatus(_A)
class _SdpBindIsICB_Type(TruthValue):defaultValue=2
_SdpBindIsICB_Type.__name__=_G
_SdpBindIsICB_Object=MibTableColumn
sdpBindIsICB=_SdpBindIsICB_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,35),_SdpBindIsICB_Type())
sdpBindIsICB.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIsICB.setStatus(_A)
_SdpBindPwFaultInetAddressType_Type=InetAddressType
_SdpBindPwFaultInetAddressType_Object=MibTableColumn
sdpBindPwFaultInetAddressType=_SdpBindPwFaultInetAddressType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,36),_SdpBindPwFaultInetAddressType_Type())
sdpBindPwFaultInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwFaultInetAddressType.setStatus(_A)
class _SdpBindPwFaultInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_SdpBindPwFaultInetAddress_Type.__name__=_U
_SdpBindPwFaultInetAddress_Object=MibTableColumn
sdpBindPwFaultInetAddress=_SdpBindPwFaultInetAddress_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,37),_SdpBindPwFaultInetAddress_Type())
sdpBindPwFaultInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwFaultInetAddress.setStatus(_A)
_SdpBindClassFwdingOperState_Type=TmnxOperState
_SdpBindClassFwdingOperState_Object=MibTableColumn
sdpBindClassFwdingOperState=_SdpBindClassFwdingOperState_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,38),_SdpBindClassFwdingOperState_Type())
sdpBindClassFwdingOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindClassFwdingOperState.setStatus(_A)
class _SdpBindForceVlanVcForwarding_Type(TruthValue):defaultValue=2
_SdpBindForceVlanVcForwarding_Type.__name__=_G
_SdpBindForceVlanVcForwarding_Object=MibTableColumn
sdpBindForceVlanVcForwarding=_SdpBindForceVlanVcForwarding_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,39),_SdpBindForceVlanVcForwarding_Type())
sdpBindForceVlanVcForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindForceVlanVcForwarding.setStatus(_A)
class _SdpBindAdminBandwidth_Type(SdpBindBandwidth):defaultValue=0
_SdpBindAdminBandwidth_Type.__name__=_g
_SdpBindAdminBandwidth_Object=MibTableColumn
sdpBindAdminBandwidth=_SdpBindAdminBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,40),_SdpBindAdminBandwidth_Type())
sdpBindAdminBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAdminBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpBindAdminBandwidth.setUnits(_S)
_SdpBindOperBandwidth_Type=SdpBindBandwidth
_SdpBindOperBandwidth_Object=MibTableColumn
sdpBindOperBandwidth=_SdpBindOperBandwidth_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,41),_SdpBindOperBandwidth_Type())
sdpBindOperBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperBandwidth.setStatus(_A)
if mibBuilder.loadTexts:sdpBindOperBandwidth.setUnits(_S)
_SdpBindCreationOrigin_Type=L2RouteOrigin
_SdpBindCreationOrigin_Object=MibTableColumn
sdpBindCreationOrigin=_SdpBindCreationOrigin_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,42),_SdpBindCreationOrigin_Type())
sdpBindCreationOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindCreationOrigin.setStatus(_A)
class _SdpBindDescription_Type(TItemDescription):defaultValue=OctetString('')
_SdpBindDescription_Type.__name__=_m
_SdpBindDescription_Object=MibTableColumn
sdpBindDescription=_SdpBindDescription_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,43),_SdpBindDescription_Type())
sdpBindDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindDescription.setStatus(_A)
_SdpBindSiteName_Type=TNamedItemOrEmpty
_SdpBindSiteName_Object=MibTableColumn
sdpBindSiteName=_SdpBindSiteName_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,44),_SdpBindSiteName_Type())
sdpBindSiteName.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindSiteName.setStatus(_A)
class _SdpBindHashLabel_Type(TruthValue):defaultValue=2
_SdpBindHashLabel_Type.__name__=_G
_SdpBindHashLabel_Object=MibTableColumn
sdpBindHashLabel=_SdpBindHashLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,45),_SdpBindHashLabel_Type())
sdpBindHashLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindHashLabel.setStatus(_A)
class _SdpBindIsaAaApplicationProfile_Type(ServObjName):defaultValue=OctetString('')
_SdpBindIsaAaApplicationProfile_Type.__name__=_V
_SdpBindIsaAaApplicationProfile_Object=MibTableColumn
sdpBindIsaAaApplicationProfile=_SdpBindIsaAaApplicationProfile_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,46),_SdpBindIsaAaApplicationProfile_Type())
sdpBindIsaAaApplicationProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIsaAaApplicationProfile.setStatus(_A)
class _SdpBindStandbySigSlave_Type(TruthValue):defaultValue=2
_SdpBindStandbySigSlave_Type.__name__=_G
_SdpBindStandbySigSlave_Object=MibTableColumn
sdpBindStandbySigSlave=_SdpBindStandbySigSlave_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,47),_SdpBindStandbySigSlave_Type())
sdpBindStandbySigSlave.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindStandbySigSlave.setStatus(_A)
class _SdpBindHashLabelSignalCapability_Type(TruthValue):defaultValue=2
_SdpBindHashLabelSignalCapability_Type.__name__=_G
_SdpBindHashLabelSignalCapability_Object=MibTableColumn
sdpBindHashLabelSignalCapability=_SdpBindHashLabelSignalCapability_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,48),_SdpBindHashLabelSignalCapability_Type())
sdpBindHashLabelSignalCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindHashLabelSignalCapability.setStatus(_A)
class _SdpBindIngressFlowspec_Type(TruthValue):defaultValue=2
_SdpBindIngressFlowspec_Type.__name__=_G
_SdpBindIngressFlowspec_Object=MibTableColumn
sdpBindIngressFlowspec=_SdpBindIngressFlowspec_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,49),_SdpBindIngressFlowspec_Type())
sdpBindIngressFlowspec.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressFlowspec.setStatus(_A)
class _SdpBindCpmProtPolicyId_Type(TCpmProtPolicyID):defaultValue=255
_SdpBindCpmProtPolicyId_Type.__name__=_k
_SdpBindCpmProtPolicyId_Object=MibTableColumn
sdpBindCpmProtPolicyId=_SdpBindCpmProtPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,50),_SdpBindCpmProtPolicyId_Type())
sdpBindCpmProtPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindCpmProtPolicyId.setStatus(_A)
class _SdpBindCpmProtMonitorMac_Type(TruthValue):defaultValue=2
_SdpBindCpmProtMonitorMac_Type.__name__=_G
_SdpBindCpmProtMonitorMac_Object=MibTableColumn
sdpBindCpmProtMonitorMac=_SdpBindCpmProtMonitorMac_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,51),_SdpBindCpmProtMonitorMac_Type())
sdpBindCpmProtMonitorMac.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindCpmProtMonitorMac.setStatus(_A)
class _SdpBindCpmProtEthCfmMonitorFlags_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('ethCfmMonitor',0),('ethCfmMonitorAggregate',1),('ethCfmMonitorCommittedAccessRate',2)))
_SdpBindCpmProtEthCfmMonitorFlags_Type.__name__=_K
_SdpBindCpmProtEthCfmMonitorFlags_Object=MibTableColumn
sdpBindCpmProtEthCfmMonitorFlags=_SdpBindCpmProtEthCfmMonitorFlags_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,52),_SdpBindCpmProtEthCfmMonitorFlags_Type())
sdpBindCpmProtEthCfmMonitorFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindCpmProtEthCfmMonitorFlags.setStatus(_A)
class _SdpBindTransitIpPolicyId_Type(TmnxBsxTransitIpPolicyIdOrZero):defaultValue=0
_SdpBindTransitIpPolicyId_Type.__name__=_s
_SdpBindTransitIpPolicyId_Object=MibTableColumn
sdpBindTransitIpPolicyId=_SdpBindTransitIpPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,53),_SdpBindTransitIpPolicyId_Type())
sdpBindTransitIpPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindTransitIpPolicyId.setStatus(_A)
_SdpBindPwStatusSignaling_Type=TruthValue
_SdpBindPwStatusSignaling_Object=MibTableColumn
sdpBindPwStatusSignaling=_SdpBindPwStatusSignaling_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,54),_SdpBindPwStatusSignaling_Type())
sdpBindPwStatusSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindPwStatusSignaling.setStatus(_A)
class _SdpBindOperGrp_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_SdpBindOperGrp_Type.__name__=_M
_SdpBindOperGrp_Object=MibTableColumn
sdpBindOperGrp=_SdpBindOperGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,55),_SdpBindOperGrp_Type())
sdpBindOperGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindOperGrp.setStatus(_A)
class _SdpBindMonitorOperGrp_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_SdpBindMonitorOperGrp_Type.__name__=_M
_SdpBindMonitorOperGrp_Object=MibTableColumn
sdpBindMonitorOperGrp=_SdpBindMonitorOperGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,56),_SdpBindMonitorOperGrp_Type())
sdpBindMonitorOperGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindMonitorOperGrp.setStatus(_A)
_SdpBindOperHashLabel_Type=TruthValue
_SdpBindOperHashLabel_Object=MibTableColumn
sdpBindOperHashLabel=_SdpBindOperHashLabel_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,57),_SdpBindOperHashLabel_Type())
sdpBindOperHashLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindOperHashLabel.setStatus(_A)
class _SdpBindTransitPrefixPolicyId_Type(TmnxBsxTransPrefPolicyIdOrZero):defaultValue=0
_SdpBindTransitPrefixPolicyId_Type.__name__=_r
_SdpBindTransitPrefixPolicyId_Object=MibTableColumn
sdpBindTransitPrefixPolicyId=_SdpBindTransitPrefixPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,58),_SdpBindTransitPrefixPolicyId_Type())
sdpBindTransitPrefixPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindTransitPrefixPolicyId.setStatus(_A)
class _SdpBindAarpId_Type(TmnxBsxAarpIdOrZero):defaultValue=0
_SdpBindAarpId_Type.__name__=_p
_SdpBindAarpId_Object=MibTableColumn
sdpBindAarpId=_SdpBindAarpId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,59),_SdpBindAarpId_Type())
sdpBindAarpId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAarpId.setStatus(_A)
class _SdpBindIngressQoSNetworkPlcyId_Type(TSdpIngressPolicyID):defaultValue=0
_SdpBindIngressQoSNetworkPlcyId_Type.__name__=_o
_SdpBindIngressQoSNetworkPlcyId_Object=MibTableColumn
sdpBindIngressQoSNetworkPlcyId=_SdpBindIngressQoSNetworkPlcyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,60),_SdpBindIngressQoSNetworkPlcyId_Type())
sdpBindIngressQoSNetworkPlcyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressQoSNetworkPlcyId.setStatus(_A)
class _SdpBindEgressQoSNetworkPlcyId_Type(TSdpEgressPolicyID):defaultValue=0
_SdpBindEgressQoSNetworkPlcyId_Type.__name__=_n
_SdpBindEgressQoSNetworkPlcyId_Object=MibTableColumn
sdpBindEgressQoSNetworkPlcyId=_SdpBindEgressQoSNetworkPlcyId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,61),_SdpBindEgressQoSNetworkPlcyId_Type())
sdpBindEgressQoSNetworkPlcyId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressQoSNetworkPlcyId.setStatus(_A)
class _SdpBindIngressQoSFpRedirectQGrp_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_SdpBindIngressQoSFpRedirectQGrp_Type.__name__=_M
_SdpBindIngressQoSFpRedirectQGrp_Object=MibTableColumn
sdpBindIngressQoSFpRedirectQGrp=_SdpBindIngressQoSFpRedirectQGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,62),_SdpBindIngressQoSFpRedirectQGrp_Type())
sdpBindIngressQoSFpRedirectQGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressQoSFpRedirectQGrp.setStatus(_A)
class _SdpBindEgressQoSPortRedirectQGrp_Type(TNamedItemOrEmpty):defaultValue=OctetString('')
_SdpBindEgressQoSPortRedirectQGrp_Type.__name__=_M
_SdpBindEgressQoSPortRedirectQGrp_Object=MibTableColumn
sdpBindEgressQoSPortRedirectQGrp=_SdpBindEgressQoSPortRedirectQGrp_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,63),_SdpBindEgressQoSPortRedirectQGrp_Type())
sdpBindEgressQoSPortRedirectQGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressQoSPortRedirectQGrp.setStatus(_A)
class _SdpBindIngressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):defaultValue=0
_SdpBindIngressQoSInstanceId_Type.__name__=_a
_SdpBindIngressQoSInstanceId_Object=MibTableColumn
sdpBindIngressQoSInstanceId=_SdpBindIngressQoSInstanceId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,64),_SdpBindIngressQoSInstanceId_Type())
sdpBindIngressQoSInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindIngressQoSInstanceId.setStatus(_A)
class _SdpBindEgressQoSInstanceId_Type(TQosQGrpInstanceIDorZero):defaultValue=0
_SdpBindEgressQoSInstanceId_Type.__name__=_a
_SdpBindEgressQoSInstanceId_Object=MibTableColumn
sdpBindEgressQoSInstanceId=_SdpBindEgressQoSInstanceId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,65),_SdpBindEgressQoSInstanceId_Type())
sdpBindEgressQoSInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindEgressQoSInstanceId.setStatus(_A)
class _SdpBindAarpServRefType_Type(TmnxBsxAarpServiceRefType):defaultValue=0
_SdpBindAarpServRefType_Type.__name__=_q
_SdpBindAarpServRefType_Object=MibTableColumn
sdpBindAarpServRefType=_SdpBindAarpServRefType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,66),_SdpBindAarpServRefType_Type())
sdpBindAarpServRefType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindAarpServRefType.setStatus(_A)
class _SdpBindPwLocalStatusBits_Type(Bits):namedValues=NamedValues(*((_AN,0),(_AO,1),(_AP,2),(_AQ,3),(_AR,4),(_AS,5)))
_SdpBindPwLocalStatusBits_Type.__name__=_K
_SdpBindPwLocalStatusBits_Object=MibTableColumn
sdpBindPwLocalStatusBits=_SdpBindPwLocalStatusBits_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,67),_SdpBindPwLocalStatusBits_Type())
sdpBindPwLocalStatusBits.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwLocalStatusBits.setStatus(_A)
class _SdpBindBlockOnPeerFault_Type(TruthValue):defaultValue=2
_SdpBindBlockOnPeerFault_Type.__name__=_G
_SdpBindBlockOnPeerFault_Object=MibTableColumn
sdpBindBlockOnPeerFault=_SdpBindBlockOnPeerFault_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,68),_SdpBindBlockOnPeerFault_Type())
sdpBindBlockOnPeerFault.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindBlockOnPeerFault.setStatus(_A)
class _SdpBindStatsCounterEnable_Type(TruthValue):defaultValue=1
_SdpBindStatsCounterEnable_Type.__name__=_G
_SdpBindStatsCounterEnable_Object=MibTableColumn
sdpBindStatsCounterEnable=_SdpBindStatsCounterEnable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,4,1,69),_SdpBindStatsCounterEnable_Type())
sdpBindStatsCounterEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindStatsCounterEnable.setStatus(_AT)
_SdpBindBaseStatsTable_Object=MibTable
sdpBindBaseStatsTable=_SdpBindBaseStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5))
if mibBuilder.loadTexts:sdpBindBaseStatsTable.setStatus(_A)
_SdpBindBaseStatsEntry_Object=MibTableRow
sdpBindBaseStatsEntry=_SdpBindBaseStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1))
sdpBindBaseStatsEntry.setIndexNames((0,_I,_J),(0,_Q,_R),(0,_H,_T))
if mibBuilder.loadTexts:sdpBindBaseStatsEntry.setStatus(_A)
_SdpBindBaseStatsIngressForwardedPackets_Type=Counter64
_SdpBindBaseStatsIngressForwardedPackets_Object=MibTableColumn
sdpBindBaseStatsIngressForwardedPackets=_SdpBindBaseStatsIngressForwardedPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,1),_SdpBindBaseStatsIngressForwardedPackets_Type())
sdpBindBaseStatsIngressForwardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsIngressForwardedPackets.setStatus(_A)
_SdpBindBaseStatsIngressDroppedPackets_Type=Counter64
_SdpBindBaseStatsIngressDroppedPackets_Object=MibTableColumn
sdpBindBaseStatsIngressDroppedPackets=_SdpBindBaseStatsIngressDroppedPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,2),_SdpBindBaseStatsIngressDroppedPackets_Type())
sdpBindBaseStatsIngressDroppedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsIngressDroppedPackets.setStatus(_A)
_SdpBindBaseStatsEgressForwardedPackets_Type=Counter64
_SdpBindBaseStatsEgressForwardedPackets_Object=MibTableColumn
sdpBindBaseStatsEgressForwardedPackets=_SdpBindBaseStatsEgressForwardedPackets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,3),_SdpBindBaseStatsEgressForwardedPackets_Type())
sdpBindBaseStatsEgressForwardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsEgressForwardedPackets.setStatus(_A)
_SdpBindBaseStatsEgressForwardedOctets_Type=Counter64
_SdpBindBaseStatsEgressForwardedOctets_Object=MibTableColumn
sdpBindBaseStatsEgressForwardedOctets=_SdpBindBaseStatsEgressForwardedOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,4),_SdpBindBaseStatsEgressForwardedOctets_Type())
sdpBindBaseStatsEgressForwardedOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsEgressForwardedOctets.setStatus(_A)
_SdpBindBaseStatsCustId_Type=TmnxCustId
_SdpBindBaseStatsCustId_Object=MibTableColumn
sdpBindBaseStatsCustId=_SdpBindBaseStatsCustId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,5),_SdpBindBaseStatsCustId_Type())
sdpBindBaseStatsCustId.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsCustId.setStatus(_A)
_SdpBindBaseStatsIngFwdOctets_Type=Counter64
_SdpBindBaseStatsIngFwdOctets_Object=MibTableColumn
sdpBindBaseStatsIngFwdOctets=_SdpBindBaseStatsIngFwdOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,6),_SdpBindBaseStatsIngFwdOctets_Type())
sdpBindBaseStatsIngFwdOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsIngFwdOctets.setStatus(_A)
_SdpBindBaseStatsIngDropOctets_Type=Counter64
_SdpBindBaseStatsIngDropOctets_Object=MibTableColumn
sdpBindBaseStatsIngDropOctets=_SdpBindBaseStatsIngDropOctets_Object((1,3,6,1,4,1,7483,6,1,2,4,4,5,1,7),_SdpBindBaseStatsIngDropOctets_Type())
sdpBindBaseStatsIngDropOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindBaseStatsIngDropOctets.setStatus(_A)
_SdpBindTlsTable_Object=MibTable
sdpBindTlsTable=_SdpBindTlsTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6))
if mibBuilder.loadTexts:sdpBindTlsTable.setStatus(_A)
_SdpBindTlsEntry_Object=MibTableRow
sdpBindTlsEntry=_SdpBindTlsEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1))
sdpBindTlsEntry.setIndexNames((0,_I,_J),(0,_Q,_R),(0,_H,_T))
if mibBuilder.loadTexts:sdpBindTlsEntry.setStatus(_A)
class _SdpBindTlsMacAddressLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,511999))
_SdpBindTlsMacAddressLimit_Type.__name__=_F
_SdpBindTlsMacAddressLimit_Object=MibTableColumn
sdpBindTlsMacAddressLimit=_SdpBindTlsMacAddressLimit_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,19),_SdpBindTlsMacAddressLimit_Type())
sdpBindTlsMacAddressLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsMacAddressLimit.setStatus(_A)
_SdpBindTlsNumMacAddresses_Type=Integer32
_SdpBindTlsNumMacAddresses_Object=MibTableColumn
sdpBindTlsNumMacAddresses=_SdpBindTlsNumMacAddresses_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,20),_SdpBindTlsNumMacAddresses_Type())
sdpBindTlsNumMacAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindTlsNumMacAddresses.setStatus(_A)
_SdpBindTlsNumStaticMacAddresses_Type=Integer32
_SdpBindTlsNumStaticMacAddresses_Object=MibTableColumn
sdpBindTlsNumStaticMacAddresses=_SdpBindTlsNumStaticMacAddresses_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,21),_SdpBindTlsNumStaticMacAddresses_Type())
sdpBindTlsNumStaticMacAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindTlsNumStaticMacAddresses.setStatus(_A)
class _SdpBindTlsMacLearning_Type(TmnxEnabledDisabled):defaultValue=1
_SdpBindTlsMacLearning_Type.__name__=_N
_SdpBindTlsMacLearning_Object=MibTableColumn
sdpBindTlsMacLearning=_SdpBindTlsMacLearning_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,22),_SdpBindTlsMacLearning_Type())
sdpBindTlsMacLearning.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsMacLearning.setStatus(_A)
class _SdpBindTlsMacAgeing_Type(TmnxEnabledDisabled):defaultValue=1
_SdpBindTlsMacAgeing_Type.__name__=_N
_SdpBindTlsMacAgeing_Object=MibTableColumn
sdpBindTlsMacAgeing=_SdpBindTlsMacAgeing_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,23),_SdpBindTlsMacAgeing_Type())
sdpBindTlsMacAgeing.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsMacAgeing.setStatus(_A)
class _SdpBindTlsLimitMacMove_Type(TlsLimitMacMove):defaultValue=1
_SdpBindTlsLimitMacMove_Type.__name__=_i
_SdpBindTlsLimitMacMove_Object=MibTableColumn
sdpBindTlsLimitMacMove=_SdpBindTlsLimitMacMove_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,31),_SdpBindTlsLimitMacMove_Type())
sdpBindTlsLimitMacMove.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsLimitMacMove.setStatus(_A)
class _SdpBindTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):defaultValue=2
_SdpBindTlsDiscardUnknownSource_Type.__name__=_N
_SdpBindTlsDiscardUnknownSource_Object=MibTableColumn
sdpBindTlsDiscardUnknownSource=_SdpBindTlsDiscardUnknownSource_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,32),_SdpBindTlsDiscardUnknownSource_Type())
sdpBindTlsDiscardUnknownSource.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsDiscardUnknownSource.setStatus(_A)
class _SdpBindTlsL2ptTermination_Type(TmnxEnabledDisabled):defaultValue=2
_SdpBindTlsL2ptTermination_Type.__name__=_N
_SdpBindTlsL2ptTermination_Object=MibTableColumn
sdpBindTlsL2ptTermination=_SdpBindTlsL2ptTermination_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,37),_SdpBindTlsL2ptTermination_Type())
sdpBindTlsL2ptTermination.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsL2ptTermination.setStatus(_A)
class _SdpBindTlsIgnoreStandbySig_Type(TruthValue):defaultValue=2
_SdpBindTlsIgnoreStandbySig_Type.__name__=_G
_SdpBindTlsIgnoreStandbySig_Object=MibTableColumn
sdpBindTlsIgnoreStandbySig=_SdpBindTlsIgnoreStandbySig_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,48),_SdpBindTlsIgnoreStandbySig_Type())
sdpBindTlsIgnoreStandbySig.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsIgnoreStandbySig.setStatus(_A)
class _SdpBindTlsBlockOnMeshFail_Type(TruthValue):defaultValue=2
_SdpBindTlsBlockOnMeshFail_Type.__name__=_G
_SdpBindTlsBlockOnMeshFail_Object=MibTableColumn
sdpBindTlsBlockOnMeshFail=_SdpBindTlsBlockOnMeshFail_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,49),_SdpBindTlsBlockOnMeshFail_Type())
sdpBindTlsBlockOnMeshFail.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsBlockOnMeshFail.setStatus(_A)
class _SdpBindTlsFdbTableSizeProfId_Type(TFdbTableSizeProfileID):defaultValue=1
_SdpBindTlsFdbTableSizeProfId_Type.__name__=_l
_SdpBindTlsFdbTableSizeProfId_Object=MibTableColumn
sdpBindTlsFdbTableSizeProfId=_SdpBindTlsFdbTableSizeProfId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,6,1,55),_SdpBindTlsFdbTableSizeProfId_Type())
sdpBindTlsFdbTableSizeProfId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindTlsFdbTableSizeProfId.setStatus(_AT)
_SdpFCMappingTable_Object=MibTable
sdpFCMappingTable=_SdpFCMappingTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,12))
if mibBuilder.loadTexts:sdpFCMappingTable.setStatus(_A)
_SdpFCMappingEntry_Object=MibTableRow
sdpFCMappingEntry=_SdpFCMappingEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,12,1))
sdpFCMappingEntry.setIndexNames((0,_I,_J),(0,_H,_Z),(0,_H,_AU))
if mibBuilder.loadTexts:sdpFCMappingEntry.setStatus(_A)
_SdpFCMappingFCName_Type=TNamedItem
_SdpFCMappingFCName_Object=MibTableColumn
sdpFCMappingFCName=_SdpFCMappingFCName_Object((1,3,6,1,4,1,7483,6,1,2,4,4,12,1,1),_SdpFCMappingFCName_Type())
sdpFCMappingFCName.setMaxAccess(_L)
if mibBuilder.loadTexts:sdpFCMappingFCName.setStatus(_A)
_SdpFCMappingRowStatus_Type=RowStatus
_SdpFCMappingRowStatus_Object=MibTableColumn
sdpFCMappingRowStatus=_SdpFCMappingRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,12,1,2),_SdpFCMappingRowStatus_Type())
sdpFCMappingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpFCMappingRowStatus.setStatus(_A)
_SdpFCMappingLspId_Type=TmnxVRtrMplsLspID
_SdpFCMappingLspId_Object=MibTableColumn
sdpFCMappingLspId=_SdpFCMappingLspId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,12,1,3),_SdpFCMappingLspId_Type())
sdpFCMappingLspId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpFCMappingLspId.setStatus(_A)
_PwTemplateTableLastChanged_Type=TimeStamp
_PwTemplateTableLastChanged_Object=MibScalar
pwTemplateTableLastChanged=_PwTemplateTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,17),_PwTemplateTableLastChanged_Type())
pwTemplateTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTemplateTableLastChanged.setStatus(_A)
_PwTemplateTable_Object=MibTable
pwTemplateTable=_PwTemplateTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18))
if mibBuilder.loadTexts:pwTemplateTable.setStatus(_A)
_PwTemplateEntry_Object=MibTableRow
pwTemplateEntry=_PwTemplateEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1))
pwTemplateEntry.setIndexNames((0,_I,_J),(0,_H,_f))
if mibBuilder.loadTexts:pwTemplateEntry.setStatus(_A)
_PwTemplateId_Type=PWTemplateId
_PwTemplateId_Object=MibTableColumn
pwTemplateId=_PwTemplateId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,1),_PwTemplateId_Type())
pwTemplateId.setMaxAccess(_L)
if mibBuilder.loadTexts:pwTemplateId.setStatus(_A)
_PwTemplateLastChanged_Type=TimeStamp
_PwTemplateLastChanged_Object=MibTableColumn
pwTemplateLastChanged=_PwTemplateLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,3),_PwTemplateLastChanged_Type())
pwTemplateLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTemplateLastChanged.setStatus(_A)
class _PwTemplateIgmpFastLeave_Type(TmnxEnabledDisabled):defaultValue=2
_PwTemplateIgmpFastLeave_Type.__name__=_N
_PwTemplateIgmpFastLeave_Object=MibTableColumn
pwTemplateIgmpFastLeave=_PwTemplateIgmpFastLeave_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,25),_PwTemplateIgmpFastLeave_Type())
pwTemplateIgmpFastLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpFastLeave.setStatus(_A)
class _PwTemplateIgmpLastMembIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_PwTemplateIgmpLastMembIntvl_Type.__name__=_D
_PwTemplateIgmpLastMembIntvl_Object=MibTableColumn
pwTemplateIgmpLastMembIntvl=_PwTemplateIgmpLastMembIntvl_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,27),_PwTemplateIgmpLastMembIntvl_Type())
pwTemplateIgmpLastMembIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpLastMembIntvl.setStatus(_A)
if mibBuilder.loadTexts:pwTemplateIgmpLastMembIntvl.setUnits('deci-seconds')
class _PwTemplateIgmpMaxNbrGrps_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_PwTemplateIgmpMaxNbrGrps_Type.__name__=_D
_PwTemplateIgmpMaxNbrGrps_Object=MibTableColumn
pwTemplateIgmpMaxNbrGrps=_PwTemplateIgmpMaxNbrGrps_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,28),_PwTemplateIgmpMaxNbrGrps_Type())
pwTemplateIgmpMaxNbrGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpMaxNbrGrps.setStatus(_A)
class _PwTemplateIgmpGenQueryIntvl_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,1024))
_PwTemplateIgmpGenQueryIntvl_Type.__name__=_D
_PwTemplateIgmpGenQueryIntvl_Object=MibTableColumn
pwTemplateIgmpGenQueryIntvl=_PwTemplateIgmpGenQueryIntvl_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,29),_PwTemplateIgmpGenQueryIntvl_Type())
pwTemplateIgmpGenQueryIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpGenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:pwTemplateIgmpGenQueryIntvl.setUnits(_P)
class _PwTemplateIgmpQueryRespIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_PwTemplateIgmpQueryRespIntvl_Type.__name__=_D
_PwTemplateIgmpQueryRespIntvl_Object=MibTableColumn
pwTemplateIgmpQueryRespIntvl=_PwTemplateIgmpQueryRespIntvl_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,30),_PwTemplateIgmpQueryRespIntvl_Type())
pwTemplateIgmpQueryRespIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpQueryRespIntvl.setStatus(_A)
if mibBuilder.loadTexts:pwTemplateIgmpQueryRespIntvl.setUnits(_P)
class _PwTemplateIgmpRobustCount_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_PwTemplateIgmpRobustCount_Type.__name__=_D
_PwTemplateIgmpRobustCount_Object=MibTableColumn
pwTemplateIgmpRobustCount=_PwTemplateIgmpRobustCount_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,31),_PwTemplateIgmpRobustCount_Type())
pwTemplateIgmpRobustCount.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpRobustCount.setStatus(_A)
class _PwTemplateIgmpSendQueries_Type(TmnxEnabledDisabled):defaultValue=2
_PwTemplateIgmpSendQueries_Type.__name__=_N
_PwTemplateIgmpSendQueries_Object=MibTableColumn
pwTemplateIgmpSendQueries=_PwTemplateIgmpSendQueries_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,32),_PwTemplateIgmpSendQueries_Type())
pwTemplateIgmpSendQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpSendQueries.setStatus(_A)
class _PwTemplateIgmpVersion_Type(TmnxIgmpVersion):defaultValue=3
_PwTemplateIgmpVersion_Type.__name__=_t
_PwTemplateIgmpVersion_Object=MibTableColumn
pwTemplateIgmpVersion=_PwTemplateIgmpVersion_Object((1,3,6,1,4,1,7483,6,1,2,4,4,18,1,36),_PwTemplateIgmpVersion_Type())
pwTemplateIgmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpVersion.setStatus(_A)
_PwTemplateIgmpSnpgGrpSrcTblLC_Type=TimeStamp
_PwTemplateIgmpSnpgGrpSrcTblLC_Object=MibScalar
pwTemplateIgmpSnpgGrpSrcTblLC=_PwTemplateIgmpSnpgGrpSrcTblLC_Object((1,3,6,1,4,1,7483,6,1,2,4,4,19),_PwTemplateIgmpSnpgGrpSrcTblLC_Type())
pwTemplateIgmpSnpgGrpSrcTblLC.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgGrpSrcTblLC.setStatus(_A)
_PwTemplateIgmpSnpgGrpSrcTable_Object=MibTable
pwTemplateIgmpSnpgGrpSrcTable=_PwTemplateIgmpSnpgGrpSrcTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20))
if mibBuilder.loadTexts:pwTemplateIgmpSnpgGrpSrcTable.setStatus(_A)
_PwTemplateIgmpSnpgGrpSrcEntry_Object=MibTableRow
pwTemplateIgmpSnpgGrpSrcEntry=_PwTemplateIgmpSnpgGrpSrcEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1))
pwTemplateIgmpSnpgGrpSrcEntry.setIndexNames((0,_I,_J),(0,_H,_f),(0,_H,_AV),(0,_H,_AW),(0,_H,_AX),(0,_H,_AY))
if mibBuilder.loadTexts:pwTemplateIgmpSnpgGrpSrcEntry.setStatus(_A)
_PwTemplateIgmpSnpgGrpAddrType_Type=InetAddressType
_PwTemplateIgmpSnpgGrpAddrType_Object=MibTableColumn
pwTemplateIgmpSnpgGrpAddrType=_PwTemplateIgmpSnpgGrpAddrType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,1),_PwTemplateIgmpSnpgGrpAddrType_Type())
pwTemplateIgmpSnpgGrpAddrType.setMaxAccess(_L)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgGrpAddrType.setStatus(_A)
class _PwTemplateIgmpSnpgGrpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_PwTemplateIgmpSnpgGrpAddr_Type.__name__=_U
_PwTemplateIgmpSnpgGrpAddr_Object=MibTableColumn
pwTemplateIgmpSnpgGrpAddr=_PwTemplateIgmpSnpgGrpAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,2),_PwTemplateIgmpSnpgGrpAddr_Type())
pwTemplateIgmpSnpgGrpAddr.setMaxAccess(_L)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgGrpAddr.setStatus(_A)
_PwTemplateIgmpSnpgSrcAddrType_Type=InetAddressType
_PwTemplateIgmpSnpgSrcAddrType_Object=MibTableColumn
pwTemplateIgmpSnpgSrcAddrType=_PwTemplateIgmpSnpgSrcAddrType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,3),_PwTemplateIgmpSnpgSrcAddrType_Type())
pwTemplateIgmpSnpgSrcAddrType.setMaxAccess(_L)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgSrcAddrType.setStatus(_A)
class _PwTemplateIgmpSnpgSrcAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4))
_PwTemplateIgmpSnpgSrcAddr_Type.__name__=_U
_PwTemplateIgmpSnpgSrcAddr_Object=MibTableColumn
pwTemplateIgmpSnpgSrcAddr=_PwTemplateIgmpSnpgSrcAddr_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,4),_PwTemplateIgmpSnpgSrcAddr_Type())
pwTemplateIgmpSnpgSrcAddr.setMaxAccess(_L)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgSrcAddr.setStatus(_A)
_PwTemplateIgmpSnpgRowStatus_Type=RowStatus
_PwTemplateIgmpSnpgRowStatus_Object=MibTableColumn
pwTemplateIgmpSnpgRowStatus=_PwTemplateIgmpSnpgRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,5),_PwTemplateIgmpSnpgRowStatus_Type())
pwTemplateIgmpSnpgRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgRowStatus.setStatus(_A)
_PwTemplateIgmpSnpgLastChngd_Type=TimeStamp
_PwTemplateIgmpSnpgLastChngd_Object=MibTableColumn
pwTemplateIgmpSnpgLastChngd=_PwTemplateIgmpSnpgLastChngd_Object((1,3,6,1,4,1,7483,6,1,2,4,4,20,1,6),_PwTemplateIgmpSnpgLastChngd_Type())
pwTemplateIgmpSnpgLastChngd.setMaxAccess(_C)
if mibBuilder.loadTexts:pwTemplateIgmpSnpgLastChngd.setStatus(_A)
_SdpPwPortTblLastChanged_Type=TimeStamp
_SdpPwPortTblLastChanged_Object=MibScalar
sdpPwPortTblLastChanged=_SdpPwPortTblLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,40),_SdpPwPortTblLastChanged_Type())
sdpPwPortTblLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpPwPortTblLastChanged.setStatus(_A)
_SdpPwPortTable_Object=MibTable
sdpPwPortTable=_SdpPwPortTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41))
if mibBuilder.loadTexts:sdpPwPortTable.setStatus(_A)
_SdpPwPortEntry_Object=MibTableRow
sdpPwPortEntry=_SdpPwPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1))
sdpPwPortEntry.setIndexNames((0,_I,_J),(0,_H,_Z),(0,_H,_AZ))
if mibBuilder.loadTexts:sdpPwPortEntry.setStatus(_A)
class _SdpPwPortId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10239))
_SdpPwPortId_Type.__name__=_D
_SdpPwPortId_Object=MibTableColumn
sdpPwPortId=_SdpPwPortId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,1),_SdpPwPortId_Type())
sdpPwPortId.setMaxAccess(_L)
if mibBuilder.loadTexts:sdpPwPortId.setStatus(_A)
_SdpPwPortRowStatus_Type=RowStatus
_SdpPwPortRowStatus_Object=MibTableColumn
sdpPwPortRowStatus=_SdpPwPortRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,2),_SdpPwPortRowStatus_Type())
sdpPwPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortRowStatus.setStatus(_A)
_SdpPwPortLastChgd_Type=TimeStamp
_SdpPwPortLastChgd_Object=MibTableColumn
sdpPwPortLastChgd=_SdpPwPortLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,3),_SdpPwPortLastChgd_Type())
sdpPwPortLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpPwPortLastChgd.setStatus(_A)
class _SdpPwPortAdminStatus_Type(ServiceAdminStatus):defaultValue=2
_SdpPwPortAdminStatus_Type.__name__=_W
_SdpPwPortAdminStatus_Object=MibTableColumn
sdpPwPortAdminStatus=_SdpPwPortAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,4),_SdpPwPortAdminStatus_Type())
sdpPwPortAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortAdminStatus.setStatus(_A)
_SdpPwPortVcId_Type=TmnxVcId
_SdpPwPortVcId_Object=MibTableColumn
sdpPwPortVcId=_SdpPwPortVcId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,5),_SdpPwPortVcId_Type())
sdpPwPortVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortVcId.setStatus(_A)
class _SdpPwPortEncapType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,10)));namedValues=NamedValues(*(('dot1q',2),('qinq',10)))
_SdpPwPortEncapType_Type.__name__=_F
_SdpPwPortEncapType_Object=MibTableColumn
sdpPwPortEncapType=_SdpPwPortEncapType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,6),_SdpPwPortEncapType_Type())
sdpPwPortEncapType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortEncapType.setStatus(_A)
class _SdpPwPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*(('up',1),(_c,5)))
_SdpPwPortOperStatus_Type.__name__=_F
_SdpPwPortOperStatus_Object=MibTableColumn
sdpPwPortOperStatus=_SdpPwPortOperStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,7),_SdpPwPortOperStatus_Type())
sdpPwPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpPwPortOperStatus.setStatus(_A)
class _SdpPwPortOperFlags_Type(Bits):namedValues=NamedValues(*((_A0,0),(_A1,1),(_A2,2),(_A3,3),(_e,4),(_A4,5),(_A5,6),(_d,7),(_A6,8),(_A7,9),(_A8,10),(_A9,11),(_AA,12),(_AB,13),(_AC,14),(_AD,15),(_AE,16),(_AF,17),(_AG,18),(_AH,19),(_AI,20),(_AJ,21),(_AK,22),(_AL,23),(_AM,24)))
_SdpPwPortOperFlags_Type.__name__=_K
_SdpPwPortOperFlags_Object=MibTableColumn
sdpPwPortOperFlags=_SdpPwPortOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,8),_SdpPwPortOperFlags_Type())
sdpPwPortOperFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpPwPortOperFlags.setStatus(_A)
class _SdpPwPortVcType_Type(SdpBindVcType):defaultValue=2
_SdpPwPortVcType_Type.__name__=_h
_SdpPwPortVcType_Object=MibTableColumn
sdpPwPortVcType=_SdpPwPortVcType_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,9),_SdpPwPortVcType_Type())
sdpPwPortVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortVcType.setStatus(_A)
class _SdpPwPortVlanVcTag_Type(Unsigned32):defaultValue=4095;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_SdpPwPortVlanVcTag_Type.__name__=_D
_SdpPwPortVlanVcTag_Object=MibTableColumn
sdpPwPortVlanVcTag=_SdpPwPortVlanVcTag_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,10),_SdpPwPortVlanVcTag_Type())
sdpPwPortVlanVcTag.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortVlanVcTag.setStatus(_A)
class _SdpPwPortEgrShapVPort_Type(TNamedItemOrEmpty):defaultHexValue=''
_SdpPwPortEgrShapVPort_Type.__name__=_M
_SdpPwPortEgrShapVPort_Object=MibTableColumn
sdpPwPortEgrShapVPort=_SdpPwPortEgrShapVPort_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,11),_SdpPwPortEgrShapVPort_Type())
sdpPwPortEgrShapVPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortEgrShapVPort.setStatus(_A)
class _SdpPwPortEgrShapDefIntDestId_Type(TNamedItemOrEmpty):defaultHexValue=''
_SdpPwPortEgrShapDefIntDestId_Type.__name__=_M
_SdpPwPortEgrShapDefIntDestId_Object=MibTableColumn
sdpPwPortEgrShapDefIntDestId=_SdpPwPortEgrShapDefIntDestId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,41,1,12),_SdpPwPortEgrShapDefIntDestId_Type())
sdpPwPortEgrShapDefIntDestId.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpPwPortEgrShapDefIntDestId.setStatus(_A)
_SdpBindPwPathTableLastChanged_Type=TimeStamp
_SdpBindPwPathTableLastChanged_Object=MibScalar
sdpBindPwPathTableLastChanged=_SdpBindPwPathTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,50),_SdpBindPwPathTableLastChanged_Type())
sdpBindPwPathTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwPathTableLastChanged.setStatus(_A)
_SdpBindPwPathTable_Object=MibTable
sdpBindPwPathTable=_SdpBindPwPathTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51))
if mibBuilder.loadTexts:sdpBindPwPathTable.setStatus(_A)
_SdpBindPwPathEntry_Object=MibTableRow
sdpBindPwPathEntry=_SdpBindPwPathEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1))
sdpBindPwPathEntry.setIndexNames((0,_I,_J),(0,_Q,_R),(0,_H,_T))
if mibBuilder.loadTexts:sdpBindPwPathEntry.setStatus(_A)
_SdpBindPwPathRowStatus_Type=RowStatus
_SdpBindPwPathRowStatus_Object=MibTableColumn
sdpBindPwPathRowStatus=_SdpBindPwPathRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,1),_SdpBindPwPathRowStatus_Type())
sdpBindPwPathRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sdpBindPwPathRowStatus.setStatus(_A)
_SdpBindPwPathLastChanged_Type=TimeStamp
_SdpBindPwPathLastChanged_Object=MibTableColumn
sdpBindPwPathLastChanged=_SdpBindPwPathLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,2),_SdpBindPwPathLastChanged_Type())
sdpBindPwPathLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindPwPathLastChanged.setStatus(_A)
class _SdpBindPwPathAgi_Type(TmnxVPNRouteDistinguisher):defaultHexValue='0000000000000000'
_SdpBindPwPathAgi_Type.__name__=_v
_SdpBindPwPathAgi_Object=MibTableColumn
sdpBindPwPathAgi=_SdpBindPwPathAgi_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,3),_SdpBindPwPathAgi_Type())
sdpBindPwPathAgi.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathAgi.setStatus(_A)
class _SdpBindPwPathSaiiGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_SdpBindPwPathSaiiGlobalId_Type.__name__=_X
_SdpBindPwPathSaiiGlobalId_Object=MibTableColumn
sdpBindPwPathSaiiGlobalId=_SdpBindPwPathSaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,4),_SdpBindPwPathSaiiGlobalId_Type())
sdpBindPwPathSaiiGlobalId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathSaiiGlobalId.setStatus(_A)
class _SdpBindPwPathSaiiNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_SdpBindPwPathSaiiNodeId_Type.__name__=_Y
_SdpBindPwPathSaiiNodeId_Object=MibTableColumn
sdpBindPwPathSaiiNodeId=_SdpBindPwPathSaiiNodeId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,5),_SdpBindPwPathSaiiNodeId_Type())
sdpBindPwPathSaiiNodeId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathSaiiNodeId.setStatus(_A)
class _SdpBindPwPathSaiiAcId_Type(Unsigned32):defaultValue=0
_SdpBindPwPathSaiiAcId_Type.__name__=_D
_SdpBindPwPathSaiiAcId_Object=MibTableColumn
sdpBindPwPathSaiiAcId=_SdpBindPwPathSaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,6),_SdpBindPwPathSaiiAcId_Type())
sdpBindPwPathSaiiAcId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathSaiiAcId.setStatus(_A)
class _SdpBindPwPathTaiiGlobalId_Type(TmnxMplsTpGlobalID):defaultValue=0
_SdpBindPwPathTaiiGlobalId_Type.__name__=_X
_SdpBindPwPathTaiiGlobalId_Object=MibTableColumn
sdpBindPwPathTaiiGlobalId=_SdpBindPwPathTaiiGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,7),_SdpBindPwPathTaiiGlobalId_Type())
sdpBindPwPathTaiiGlobalId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathTaiiGlobalId.setStatus(_A)
class _SdpBindPwPathTaiiNodeId_Type(TmnxMplsTpNodeID):defaultValue=0
_SdpBindPwPathTaiiNodeId_Type.__name__=_Y
_SdpBindPwPathTaiiNodeId_Object=MibTableColumn
sdpBindPwPathTaiiNodeId=_SdpBindPwPathTaiiNodeId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,8),_SdpBindPwPathTaiiNodeId_Type())
sdpBindPwPathTaiiNodeId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathTaiiNodeId.setStatus(_A)
class _SdpBindPwPathTaiiAcId_Type(Unsigned32):defaultValue=0
_SdpBindPwPathTaiiAcId_Type.__name__=_D
_SdpBindPwPathTaiiAcId_Object=MibTableColumn
sdpBindPwPathTaiiAcId=_SdpBindPwPathTaiiAcId_Object((1,3,6,1,4,1,7483,6,1,2,4,4,51,1,9),_SdpBindPwPathTaiiAcId_Type())
sdpBindPwPathTaiiAcId.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindPwPathTaiiAcId.setStatus(_A)
_SdpBindCtrlChanPwTableLastChgd_Type=TimeStamp
_SdpBindCtrlChanPwTableLastChgd_Object=MibScalar
sdpBindCtrlChanPwTableLastChgd=_SdpBindCtrlChanPwTableLastChgd_Object((1,3,6,1,4,1,7483,6,1,2,4,4,52),_SdpBindCtrlChanPwTableLastChgd_Type())
sdpBindCtrlChanPwTableLastChgd.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindCtrlChanPwTableLastChgd.setStatus(_A)
_SdpBindCtrlChanPwTable_Object=MibTable
sdpBindCtrlChanPwTable=_SdpBindCtrlChanPwTable_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53))
if mibBuilder.loadTexts:sdpBindCtrlChanPwTable.setStatus(_A)
_SdpBindCtrlChanPwEntry_Object=MibTableRow
sdpBindCtrlChanPwEntry=_SdpBindCtrlChanPwEntry_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1))
sdpBindCtrlChanPwEntry.setIndexNames((0,_I,_J),(0,_Q,_R),(0,_H,_T))
if mibBuilder.loadTexts:sdpBindCtrlChanPwEntry.setStatus(_A)
_SdpBindCtrlChanPwLastChanged_Type=TimeStamp
_SdpBindCtrlChanPwLastChanged_Object=MibTableColumn
sdpBindCtrlChanPwLastChanged=_SdpBindCtrlChanPwLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,1),_SdpBindCtrlChanPwLastChanged_Type())
sdpBindCtrlChanPwLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindCtrlChanPwLastChanged.setStatus(_A)
class _SdpBindCtrlChanPwStatus_Type(TmnxEnabledDisabled):defaultValue=2
_SdpBindCtrlChanPwStatus_Type.__name__=_N
_SdpBindCtrlChanPwStatus_Object=MibTableColumn
sdpBindCtrlChanPwStatus=_SdpBindCtrlChanPwStatus_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,2),_SdpBindCtrlChanPwStatus_Type())
sdpBindCtrlChanPwStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwStatus.setStatus(_A)
class _SdpBindCtrlChanPwRefreshTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,65535))
_SdpBindCtrlChanPwRefreshTimer_Type.__name__=_D
_SdpBindCtrlChanPwRefreshTimer_Object=MibTableColumn
sdpBindCtrlChanPwRefreshTimer=_SdpBindCtrlChanPwRefreshTimer_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,3),_SdpBindCtrlChanPwRefreshTimer_Type())
sdpBindCtrlChanPwRefreshTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRefreshTimer.setStatus(_A)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRefreshTimer.setUnits(_P)
_SdpBindCtrlChanPwPeerExpired_Type=TruthValue
_SdpBindCtrlChanPwPeerExpired_Object=MibTableColumn
sdpBindCtrlChanPwPeerExpired=_SdpBindCtrlChanPwPeerExpired_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,4),_SdpBindCtrlChanPwPeerExpired_Type())
sdpBindCtrlChanPwPeerExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpBindCtrlChanPwPeerExpired.setStatus(_A)
class _SdpBindCtrlChanPwRequestTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,65535))
_SdpBindCtrlChanPwRequestTimer_Type.__name__=_D
_SdpBindCtrlChanPwRequestTimer_Object=MibTableColumn
sdpBindCtrlChanPwRequestTimer=_SdpBindCtrlChanPwRequestTimer_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,5),_SdpBindCtrlChanPwRequestTimer_Type())
sdpBindCtrlChanPwRequestTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRequestTimer.setStatus(_A)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRequestTimer.setUnits(_P)
class _SdpBindCtrlChanPwRetryTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,60))
_SdpBindCtrlChanPwRetryTimer_Type.__name__=_D
_SdpBindCtrlChanPwRetryTimer_Object=MibTableColumn
sdpBindCtrlChanPwRetryTimer=_SdpBindCtrlChanPwRetryTimer_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,6),_SdpBindCtrlChanPwRetryTimer_Type())
sdpBindCtrlChanPwRetryTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRetryTimer.setStatus(_A)
if mibBuilder.loadTexts:sdpBindCtrlChanPwRetryTimer.setUnits(_P)
class _SdpBindCtrlChanPwTimeoutMult_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,15))
_SdpBindCtrlChanPwTimeoutMult_Type.__name__=_D
_SdpBindCtrlChanPwTimeoutMult_Object=MibTableColumn
sdpBindCtrlChanPwTimeoutMult=_SdpBindCtrlChanPwTimeoutMult_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,7),_SdpBindCtrlChanPwTimeoutMult_Type())
sdpBindCtrlChanPwTimeoutMult.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwTimeoutMult.setStatus(_A)
class _SdpBindCtrlChanPwAck_Type(TruthValue):defaultValue=2
_SdpBindCtrlChanPwAck_Type.__name__=_G
_SdpBindCtrlChanPwAck_Object=MibTableColumn
sdpBindCtrlChanPwAck=_SdpBindCtrlChanPwAck_Object((1,3,6,1,4,1,7483,6,1,2,4,4,53,1,8),_SdpBindCtrlChanPwAck_Type())
sdpBindCtrlChanPwAck.setMaxAccess(_E)
if mibBuilder.loadTexts:sdpBindCtrlChanPwAck.setStatus(_A)
_SdpInfoScalar1_Type=Unsigned32
_SdpInfoScalar1_Object=MibScalar
sdpInfoScalar1=_SdpInfoScalar1_Object((1,3,6,1,4,1,7483,6,1,2,4,4,101),_SdpInfoScalar1_Type())
sdpInfoScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpInfoScalar1.setStatus(_A)
_SdpInfoScalar2_Type=Unsigned32
_SdpInfoScalar2_Object=MibScalar
sdpInfoScalar2=_SdpInfoScalar2_Object((1,3,6,1,4,1,7483,6,1,2,4,4,102),_SdpInfoScalar2_Type())
sdpInfoScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:sdpInfoScalar2.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'tnServicesSdpMIBModule':tnServicesSdpMIBModule,'tnSdpObjs':tnSdpObjs,'sdpNumEntries':sdpNumEntries,'sdpNextFreeId':sdpNextFreeId,'sdpInfoTable':sdpInfoTable,'sdpInfoEntry':sdpInfoEntry,_Z:sdpId,'sdpRowStatus':sdpRowStatus,'sdpDelivery':sdpDelivery,'sdpFarEndIpAddress':sdpFarEndIpAddress,'sdpLspList':sdpLspList,'sdpDescription':sdpDescription,'sdpLabelSignaling':sdpLabelSignaling,'sdpAdminStatus':sdpAdminStatus,'sdpOperStatus':sdpOperStatus,'sdpAdminPathMtu':sdpAdminPathMtu,'sdpOperPathMtu':sdpOperPathMtu,'sdpKeepAliveAdminStatus':sdpKeepAliveAdminStatus,'sdpKeepAliveOperStatus':sdpKeepAliveOperStatus,'sdpKeepAliveHelloTime':sdpKeepAliveHelloTime,'sdpKeepAliveMaxDropCount':sdpKeepAliveMaxDropCount,'sdpKeepAliveHoldDownTime':sdpKeepAliveHoldDownTime,'sdpLastMgmtChange':sdpLastMgmtChange,'sdpKeepAliveHelloMessageLength':sdpKeepAliveHelloMessageLength,'sdpKeepAliveNumHelloRequestMessages':sdpKeepAliveNumHelloRequestMessages,'sdpKeepAliveNumHelloResponseMessages':sdpKeepAliveNumHelloResponseMessages,'sdpKeepAliveNumLateHelloResponseMessages':sdpKeepAliveNumLateHelloResponseMessages,'sdpKeepAliveHelloRequestTimeout':sdpKeepAliveHelloRequestTimeout,'sdpLdpEnabled':sdpLdpEnabled,'sdpVlanVcEtype':sdpVlanVcEtype,'sdpAdvertisedVllMtuOverride':sdpAdvertisedVllMtuOverride,'sdpOperFlags':sdpOperFlags,'sdpLastStatusChange':sdpLastStatusChange,'sdpMvplsMgmtService':sdpMvplsMgmtService,'sdpMvplsMgmtSdpBndId':sdpMvplsMgmtSdpBndId,'sdpCollectAcctStats':sdpCollectAcctStats,'sdpAccountingPolicyId':sdpAccountingPolicyId,'sdpClassFwdingEnabled':sdpClassFwdingEnabled,'sdpClassFwdingDefaultLsp':sdpClassFwdingDefaultLsp,'sdpClassFwdingMcLsp':sdpClassFwdingMcLsp,'sdpMetric':sdpMetric,'sdpAutoSdp':sdpAutoSdp,'sdpSnmpAllowed':sdpSnmpAllowed,'sdpPBBEtype':sdpPBBEtype,'sdpBandwidthBookingFactor':sdpBandwidthBookingFactor,'sdpOperBandwidth':sdpOperBandwidth,'sdpAvailableBandwidth':sdpAvailableBandwidth,'sdpMaxBookableBandwidth':sdpMaxBookableBandwidth,'sdpBookedBandwidth':sdpBookedBandwidth,'sdpCreationOrigin':sdpCreationOrigin,'sdpEnforceDiffServLspFc':sdpEnforceDiffServLspFc,'sdpMixedLspModeEnabled':sdpMixedLspModeEnabled,'sdpLspRevertTime':sdpLspRevertTime,'sdpLspRevertTimeCountDown':sdpLspRevertTimeCountDown,'sdpLdpLspId':sdpLdpLspId,'sdpLdpActive':sdpLdpActive,'sdpNetDomainName':sdpNetDomainName,'sdpEgressIfsNetDomainConsistent':sdpEgressIfsNetDomainConsistent,'sdpBgpTunnelEnabled':sdpBgpTunnelEnabled,'sdpBgpTunnelLspId':sdpBgpTunnelLspId,'sdpTunnelFarEndIpAddress':sdpTunnelFarEndIpAddress,'sdpActiveLspType':sdpActiveLspType,'sdpBindingPort':sdpBindingPort,'sdpFarEndNodeId':sdpFarEndNodeId,'sdpFarEndGlobalId':sdpFarEndGlobalId,'sdpBindTable':sdpBindTable,'sdpBindEntry':sdpBindEntry,_T:sdpBindId,'sdpBindRowStatus':sdpBindRowStatus,'sdpBindAdminIngressLabel':sdpBindAdminIngressLabel,'sdpBindAdminEgressLabel':sdpBindAdminEgressLabel,'sdpBindOperIngressLabel':sdpBindOperIngressLabel,'sdpBindOperEgressLabel':sdpBindOperEgressLabel,'sdpBindAdminStatus':sdpBindAdminStatus,'sdpBindOperStatus':sdpBindOperStatus,'sdpBindLastMgmtChange':sdpBindLastMgmtChange,'sdpBindType':sdpBindType,'sdpBindIngressMacFilterId':sdpBindIngressMacFilterId,'sdpBindIngressIpFilterId':sdpBindIngressIpFilterId,'sdpBindEgressMacFilterId':sdpBindEgressMacFilterId,'sdpBindEgressIpFilterId':sdpBindEgressIpFilterId,'sdpBindVpnId':sdpBindVpnId,'sdpBindCustId':sdpBindCustId,'sdpBindVcType':sdpBindVcType,'sdpBindVlanVcTag':sdpBindVlanVcTag,'sdpBindSplitHorizonGrp':sdpBindSplitHorizonGrp,'sdpBindOperFlags':sdpBindOperFlags,'sdpBindLastStatusChange':sdpBindLastStatusChange,'sdpBindIesIfIndex':sdpBindIesIfIndex,'sdpBindMacPinning':sdpBindMacPinning,'sdpBindIngressIpv6FilterId':sdpBindIngressIpv6FilterId,'sdpBindEgressIpv6FilterId':sdpBindEgressIpv6FilterId,'sdpBindCollectAcctStats':sdpBindCollectAcctStats,'sdpBindAccountingPolicyId':sdpBindAccountingPolicyId,'sdpBindPwPeerStatusBits':sdpBindPwPeerStatusBits,'sdpBindPeerVccvCvBits':sdpBindPeerVccvCvBits,'sdpBindPeerVccvCcBits':sdpBindPeerVccvCcBits,'sdpBindControlWordBit':sdpBindControlWordBit,'sdpBindOperControlWord':sdpBindOperControlWord,'sdpBindEndPoint':sdpBindEndPoint,'sdpBindEndPointPrecedence':sdpBindEndPointPrecedence,'sdpBindIsICB':sdpBindIsICB,'sdpBindPwFaultInetAddressType':sdpBindPwFaultInetAddressType,'sdpBindPwFaultInetAddress':sdpBindPwFaultInetAddress,'sdpBindClassFwdingOperState':sdpBindClassFwdingOperState,'sdpBindForceVlanVcForwarding':sdpBindForceVlanVcForwarding,'sdpBindAdminBandwidth':sdpBindAdminBandwidth,'sdpBindOperBandwidth':sdpBindOperBandwidth,'sdpBindCreationOrigin':sdpBindCreationOrigin,'sdpBindDescription':sdpBindDescription,'sdpBindSiteName':sdpBindSiteName,'sdpBindHashLabel':sdpBindHashLabel,'sdpBindIsaAaApplicationProfile':sdpBindIsaAaApplicationProfile,'sdpBindStandbySigSlave':sdpBindStandbySigSlave,'sdpBindHashLabelSignalCapability':sdpBindHashLabelSignalCapability,'sdpBindIngressFlowspec':sdpBindIngressFlowspec,'sdpBindCpmProtPolicyId':sdpBindCpmProtPolicyId,'sdpBindCpmProtMonitorMac':sdpBindCpmProtMonitorMac,'sdpBindCpmProtEthCfmMonitorFlags':sdpBindCpmProtEthCfmMonitorFlags,'sdpBindTransitIpPolicyId':sdpBindTransitIpPolicyId,'sdpBindPwStatusSignaling':sdpBindPwStatusSignaling,'sdpBindOperGrp':sdpBindOperGrp,'sdpBindMonitorOperGrp':sdpBindMonitorOperGrp,'sdpBindOperHashLabel':sdpBindOperHashLabel,'sdpBindTransitPrefixPolicyId':sdpBindTransitPrefixPolicyId,'sdpBindAarpId':sdpBindAarpId,'sdpBindIngressQoSNetworkPlcyId':sdpBindIngressQoSNetworkPlcyId,'sdpBindEgressQoSNetworkPlcyId':sdpBindEgressQoSNetworkPlcyId,'sdpBindIngressQoSFpRedirectQGrp':sdpBindIngressQoSFpRedirectQGrp,'sdpBindEgressQoSPortRedirectQGrp':sdpBindEgressQoSPortRedirectQGrp,'sdpBindIngressQoSInstanceId':sdpBindIngressQoSInstanceId,'sdpBindEgressQoSInstanceId':sdpBindEgressQoSInstanceId,'sdpBindAarpServRefType':sdpBindAarpServRefType,'sdpBindPwLocalStatusBits':sdpBindPwLocalStatusBits,'sdpBindBlockOnPeerFault':sdpBindBlockOnPeerFault,'sdpBindStatsCounterEnable':sdpBindStatsCounterEnable,'sdpBindBaseStatsTable':sdpBindBaseStatsTable,'sdpBindBaseStatsEntry':sdpBindBaseStatsEntry,'sdpBindBaseStatsIngressForwardedPackets':sdpBindBaseStatsIngressForwardedPackets,'sdpBindBaseStatsIngressDroppedPackets':sdpBindBaseStatsIngressDroppedPackets,'sdpBindBaseStatsEgressForwardedPackets':sdpBindBaseStatsEgressForwardedPackets,'sdpBindBaseStatsEgressForwardedOctets':sdpBindBaseStatsEgressForwardedOctets,'sdpBindBaseStatsCustId':sdpBindBaseStatsCustId,'sdpBindBaseStatsIngFwdOctets':sdpBindBaseStatsIngFwdOctets,'sdpBindBaseStatsIngDropOctets':sdpBindBaseStatsIngDropOctets,'sdpBindTlsTable':sdpBindTlsTable,'sdpBindTlsEntry':sdpBindTlsEntry,'sdpBindTlsMacAddressLimit':sdpBindTlsMacAddressLimit,'sdpBindTlsNumMacAddresses':sdpBindTlsNumMacAddresses,'sdpBindTlsNumStaticMacAddresses':sdpBindTlsNumStaticMacAddresses,'sdpBindTlsMacLearning':sdpBindTlsMacLearning,'sdpBindTlsMacAgeing':sdpBindTlsMacAgeing,'sdpBindTlsLimitMacMove':sdpBindTlsLimitMacMove,'sdpBindTlsDiscardUnknownSource':sdpBindTlsDiscardUnknownSource,'sdpBindTlsL2ptTermination':sdpBindTlsL2ptTermination,'sdpBindTlsIgnoreStandbySig':sdpBindTlsIgnoreStandbySig,'sdpBindTlsBlockOnMeshFail':sdpBindTlsBlockOnMeshFail,'sdpBindTlsFdbTableSizeProfId':sdpBindTlsFdbTableSizeProfId,'sdpFCMappingTable':sdpFCMappingTable,'sdpFCMappingEntry':sdpFCMappingEntry,_AU:sdpFCMappingFCName,'sdpFCMappingRowStatus':sdpFCMappingRowStatus,'sdpFCMappingLspId':sdpFCMappingLspId,'pwTemplateTableLastChanged':pwTemplateTableLastChanged,'pwTemplateTable':pwTemplateTable,'pwTemplateEntry':pwTemplateEntry,_f:pwTemplateId,'pwTemplateLastChanged':pwTemplateLastChanged,'pwTemplateIgmpFastLeave':pwTemplateIgmpFastLeave,'pwTemplateIgmpLastMembIntvl':pwTemplateIgmpLastMembIntvl,'pwTemplateIgmpMaxNbrGrps':pwTemplateIgmpMaxNbrGrps,'pwTemplateIgmpGenQueryIntvl':pwTemplateIgmpGenQueryIntvl,'pwTemplateIgmpQueryRespIntvl':pwTemplateIgmpQueryRespIntvl,'pwTemplateIgmpRobustCount':pwTemplateIgmpRobustCount,'pwTemplateIgmpSendQueries':pwTemplateIgmpSendQueries,'pwTemplateIgmpVersion':pwTemplateIgmpVersion,'pwTemplateIgmpSnpgGrpSrcTblLC':pwTemplateIgmpSnpgGrpSrcTblLC,'pwTemplateIgmpSnpgGrpSrcTable':pwTemplateIgmpSnpgGrpSrcTable,'pwTemplateIgmpSnpgGrpSrcEntry':pwTemplateIgmpSnpgGrpSrcEntry,_AV:pwTemplateIgmpSnpgGrpAddrType,_AW:pwTemplateIgmpSnpgGrpAddr,_AX:pwTemplateIgmpSnpgSrcAddrType,_AY:pwTemplateIgmpSnpgSrcAddr,'pwTemplateIgmpSnpgRowStatus':pwTemplateIgmpSnpgRowStatus,'pwTemplateIgmpSnpgLastChngd':pwTemplateIgmpSnpgLastChngd,'sdpPwPortTblLastChanged':sdpPwPortTblLastChanged,'sdpPwPortTable':sdpPwPortTable,'sdpPwPortEntry':sdpPwPortEntry,_AZ:sdpPwPortId,'sdpPwPortRowStatus':sdpPwPortRowStatus,'sdpPwPortLastChgd':sdpPwPortLastChgd,'sdpPwPortAdminStatus':sdpPwPortAdminStatus,'sdpPwPortVcId':sdpPwPortVcId,'sdpPwPortEncapType':sdpPwPortEncapType,'sdpPwPortOperStatus':sdpPwPortOperStatus,'sdpPwPortOperFlags':sdpPwPortOperFlags,'sdpPwPortVcType':sdpPwPortVcType,'sdpPwPortVlanVcTag':sdpPwPortVlanVcTag,'sdpPwPortEgrShapVPort':sdpPwPortEgrShapVPort,'sdpPwPortEgrShapDefIntDestId':sdpPwPortEgrShapDefIntDestId,'sdpBindPwPathTableLastChanged':sdpBindPwPathTableLastChanged,'sdpBindPwPathTable':sdpBindPwPathTable,'sdpBindPwPathEntry':sdpBindPwPathEntry,'sdpBindPwPathRowStatus':sdpBindPwPathRowStatus,'sdpBindPwPathLastChanged':sdpBindPwPathLastChanged,'sdpBindPwPathAgi':sdpBindPwPathAgi,'sdpBindPwPathSaiiGlobalId':sdpBindPwPathSaiiGlobalId,'sdpBindPwPathSaiiNodeId':sdpBindPwPathSaiiNodeId,'sdpBindPwPathSaiiAcId':sdpBindPwPathSaiiAcId,'sdpBindPwPathTaiiGlobalId':sdpBindPwPathTaiiGlobalId,'sdpBindPwPathTaiiNodeId':sdpBindPwPathTaiiNodeId,'sdpBindPwPathTaiiAcId':sdpBindPwPathTaiiAcId,'sdpBindCtrlChanPwTableLastChgd':sdpBindCtrlChanPwTableLastChgd,'sdpBindCtrlChanPwTable':sdpBindCtrlChanPwTable,'sdpBindCtrlChanPwEntry':sdpBindCtrlChanPwEntry,'sdpBindCtrlChanPwLastChanged':sdpBindCtrlChanPwLastChanged,'sdpBindCtrlChanPwStatus':sdpBindCtrlChanPwStatus,'sdpBindCtrlChanPwRefreshTimer':sdpBindCtrlChanPwRefreshTimer,'sdpBindCtrlChanPwPeerExpired':sdpBindCtrlChanPwPeerExpired,'sdpBindCtrlChanPwRequestTimer':sdpBindCtrlChanPwRequestTimer,'sdpBindCtrlChanPwRetryTimer':sdpBindCtrlChanPwRetryTimer,'sdpBindCtrlChanPwTimeoutMult':sdpBindCtrlChanPwTimeoutMult,'sdpBindCtrlChanPwAck':sdpBindCtrlChanPwAck,'sdpInfoScalar1':sdpInfoScalar1,'sdpInfoScalar2':sdpInfoScalar2})