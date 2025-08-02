_j='fsMIRipPeerAddress'
_i='fsMIRipDistInOutRouteMapType'
_h='fsMIRipDistInOutRouteMapName'
_g='fsMIRipCryptoAuthKeyId'
_f='fsMIRipCryptoAuthAddress'
_e='fsMIRipCryptoAuthIfIndex'
_d='fsMIRipAggAddressMask'
_c='fsMIRipAggAddress'
_b='fsMIRipIfIndex'
_a='fsMIRip2NextHop'
_Z='fsMIRip2Tos'
_Y='fsMIRip2DestMask'
_X='fsMIRip2DestNet'
_W='fsMIRip2NBRUnicastIpAddr'
_V='fsMIRipMd5AuthKeyId'
_U='fsMIRipMd5AuthAddress'
_T='fsMIRip2IfConfAddress'
_S='fsMIRip2TrustNBRIpAddr'
_R='disable'
_Q='fsMIRipAuthKeyId'
_P='fsMIRipAuthIfIndex'
_O='fsMIRip2ContextId'
_N='TruthValue'
_M='DisplayString'
_L='InterfaceIndex'
_K='OctetString'
_J='accessible-for-notify'
_I='disabled'
_H='enabled'
_G='read-only'
_F='fsMIRipContextId'
_E='not-accessible'
_D='SUPERMICRO-MIRIP2-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_M,'PhysAddress','RowStatus','TextualConvention',_N)
fsMIRip=ModuleIdentity((1,3,6,1,4,1,10876,101,1,151))
if mibBuilder.loadTexts:fsMIRip.setRevisions(('2012-09-05 00:00',))
_FsMIRip2GeneralGroup_ObjectIdentity=ObjectIdentity
fsMIRip2GeneralGroup=_FsMIRip2GeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,1))
_FsMIRip2GlobalTable_Object=MibTable
fsMIRip2GlobalTable=_FsMIRip2GlobalTable_Object((1,3,6,1,4,1,10876,101,1,151,1,1))
if mibBuilder.loadTexts:fsMIRip2GlobalTable.setStatus(_A)
_FsMIRip2GlobalEntry_Object=MibTableRow
fsMIRip2GlobalEntry=_FsMIRip2GlobalEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1))
fsMIRip2GlobalEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIRip2GlobalEntry.setStatus(_A)
class _FsMIRipContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipContextId_Type.__name__=_C
_FsMIRipContextId_Object=MibTableColumn
fsMIRipContextId=_FsMIRipContextId_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,1),_FsMIRipContextId_Type())
fsMIRipContextId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipContextId.setStatus(_A)
class _FsMIRip2Security_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('minimumSecurity',1),('maximumSecurity',2)))
_FsMIRip2Security_Type.__name__=_C
_FsMIRip2Security_Object=MibTableColumn
fsMIRip2Security=_FsMIRip2Security_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,2),_FsMIRip2Security_Type())
fsMIRip2Security.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2Security.setStatus(_A)
class _FsMIRip2Peers_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIRip2Peers_Type.__name__=_C
_FsMIRip2Peers_Object=MibTableColumn
fsMIRip2Peers=_FsMIRip2Peers_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,3),_FsMIRip2Peers_Type())
fsMIRip2Peers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2Peers.setStatus(_A)
class _FsMIRip2TrustNBRListEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRip2TrustNBRListEnable_Type.__name__=_C
_FsMIRip2TrustNBRListEnable_Object=MibTableColumn
fsMIRip2TrustNBRListEnable=_FsMIRip2TrustNBRListEnable_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,4),_FsMIRip2TrustNBRListEnable_Type())
fsMIRip2TrustNBRListEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2TrustNBRListEnable.setStatus(_A)
_FsMIRip2NumberOfDroppedPkts_Type=Counter32
_FsMIRip2NumberOfDroppedPkts_Object=MibTableColumn
fsMIRip2NumberOfDroppedPkts=_FsMIRip2NumberOfDroppedPkts_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,5),_FsMIRip2NumberOfDroppedPkts_Type())
fsMIRip2NumberOfDroppedPkts.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2NumberOfDroppedPkts.setStatus(_A)
class _FsMIRip2SpacingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRip2SpacingEnable_Type.__name__=_C
_FsMIRip2SpacingEnable_Object=MibTableColumn
fsMIRip2SpacingEnable=_FsMIRip2SpacingEnable_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,6),_FsMIRip2SpacingEnable_Type())
fsMIRip2SpacingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2SpacingEnable.setStatus(_A)
class _FsMIRip2AutoSummaryStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRip2AutoSummaryStatus_Type.__name__=_C
_FsMIRip2AutoSummaryStatus_Object=MibTableColumn
fsMIRip2AutoSummaryStatus=_FsMIRip2AutoSummaryStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,7),_FsMIRip2AutoSummaryStatus_Type())
fsMIRip2AutoSummaryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2AutoSummaryStatus.setStatus(_A)
class _FsMIRip2RetransTimeoutInt_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,10))
_FsMIRip2RetransTimeoutInt_Type.__name__=_C
_FsMIRip2RetransTimeoutInt_Object=MibTableColumn
fsMIRip2RetransTimeoutInt=_FsMIRip2RetransTimeoutInt_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,8),_FsMIRip2RetransTimeoutInt_Type())
fsMIRip2RetransTimeoutInt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2RetransTimeoutInt.setStatus(_A)
class _FsMIRip2MaxRetransmissions_Type(Integer32):defaultValue=36;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,40))
_FsMIRip2MaxRetransmissions_Type.__name__=_C
_FsMIRip2MaxRetransmissions_Object=MibTableColumn
fsMIRip2MaxRetransmissions=_FsMIRip2MaxRetransmissions_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,9),_FsMIRip2MaxRetransmissions_Type())
fsMIRip2MaxRetransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2MaxRetransmissions.setStatus(_A)
class _FsMIRip2OverSubscriptionTimeout_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,300))
_FsMIRip2OverSubscriptionTimeout_Type.__name__=_C
_FsMIRip2OverSubscriptionTimeout_Object=MibTableColumn
fsMIRip2OverSubscriptionTimeout=_FsMIRip2OverSubscriptionTimeout_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,10),_FsMIRip2OverSubscriptionTimeout_Type())
fsMIRip2OverSubscriptionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2OverSubscriptionTimeout.setStatus(_A)
class _FsMIRip2Propagate_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_R,2)))
_FsMIRip2Propagate_Type.__name__=_C
_FsMIRip2Propagate_Object=MibTableColumn
fsMIRip2Propagate=_FsMIRip2Propagate_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,11),_FsMIRip2Propagate_Type())
fsMIRip2Propagate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2Propagate.setStatus(_A)
class _FsMIRipTrcFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipTrcFlag_Type.__name__=_C
_FsMIRipTrcFlag_Object=MibTableColumn
fsMIRipTrcFlag=_FsMIRipTrcFlag_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,12),_FsMIRipTrcFlag_Type())
fsMIRipTrcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipTrcFlag.setStatus(_A)
_FsMIRipRowStatus_Type=RowStatus
_FsMIRipRowStatus_Object=MibTableColumn
fsMIRipRowStatus=_FsMIRipRowStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,13),_FsMIRipRowStatus_Type())
fsMIRipRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRowStatus.setStatus(_A)
class _FsMIRipAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRipAdminStatus_Type.__name__=_C
_FsMIRipAdminStatus_Object=MibTableColumn
fsMIRipAdminStatus=_FsMIRipAdminStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,14),_FsMIRipAdminStatus_Type())
fsMIRipAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipAdminStatus.setStatus(_A)
class _FsMIRip2LastAuthKeyLifetimeStatus_Type(TruthValue):defaultValue=1
_FsMIRip2LastAuthKeyLifetimeStatus_Type.__name__=_N
_FsMIRip2LastAuthKeyLifetimeStatus_Object=MibTableColumn
fsMIRip2LastAuthKeyLifetimeStatus=_FsMIRip2LastAuthKeyLifetimeStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,15),_FsMIRip2LastAuthKeyLifetimeStatus_Type())
fsMIRip2LastAuthKeyLifetimeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2LastAuthKeyLifetimeStatus.setStatus(_A)
_FsMIRipRtCount_Type=Integer32
_FsMIRipRtCount_Object=MibTableColumn
fsMIRipRtCount=_FsMIRipRtCount_Object((1,3,6,1,4,1,10876,101,1,151,1,1,1,16),_FsMIRipRtCount_Type())
fsMIRipRtCount.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRipRtCount.setStatus(_A)
class _FsMIRipGlobalTrcFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipGlobalTrcFlag_Type.__name__=_C
_FsMIRipGlobalTrcFlag_Object=MibScalar
fsMIRipGlobalTrcFlag=_FsMIRipGlobalTrcFlag_Object((1,3,6,1,4,1,10876,101,1,151,1,2),_FsMIRipGlobalTrcFlag_Type())
fsMIRipGlobalTrcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipGlobalTrcFlag.setStatus(_A)
_FsMIRip2NBRTrustListTable_Object=MibTable
fsMIRip2NBRTrustListTable=_FsMIRip2NBRTrustListTable_Object((1,3,6,1,4,1,10876,101,1,151,1,3))
if mibBuilder.loadTexts:fsMIRip2NBRTrustListTable.setStatus(_A)
_FsMIRip2NBRTrustListEntry_Object=MibTableRow
fsMIRip2NBRTrustListEntry=_FsMIRip2NBRTrustListEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,3,1))
fsMIRip2NBRTrustListEntry.setIndexNames((0,_D,_F),(0,_D,_S))
if mibBuilder.loadTexts:fsMIRip2NBRTrustListEntry.setStatus(_A)
_FsMIRip2TrustNBRIpAddr_Type=IpAddress
_FsMIRip2TrustNBRIpAddr_Object=MibTableColumn
fsMIRip2TrustNBRIpAddr=_FsMIRip2TrustNBRIpAddr_Object((1,3,6,1,4,1,10876,101,1,151,1,3,1,1),_FsMIRip2TrustNBRIpAddr_Type())
fsMIRip2TrustNBRIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2TrustNBRIpAddr.setStatus(_A)
_FsMIRip2TrustNBRRowStatus_Type=RowStatus
_FsMIRip2TrustNBRRowStatus_Object=MibTableColumn
fsMIRip2TrustNBRRowStatus=_FsMIRip2TrustNBRRowStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,3,1,2),_FsMIRip2TrustNBRRowStatus_Type())
fsMIRip2TrustNBRRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2TrustNBRRowStatus.setStatus(_A)
_FsMIRip2IfConfTable_Object=MibTable
fsMIRip2IfConfTable=_FsMIRip2IfConfTable_Object((1,3,6,1,4,1,10876,101,1,151,1,4))
if mibBuilder.loadTexts:fsMIRip2IfConfTable.setStatus(_A)
_FsMIRip2IfConfEntry_Object=MibTableRow
fsMIRip2IfConfEntry=_FsMIRip2IfConfEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1))
fsMIRip2IfConfEntry.setIndexNames((0,_D,_F),(0,_D,_T))
if mibBuilder.loadTexts:fsMIRip2IfConfEntry.setStatus(_A)
_FsMIRip2IfConfAddress_Type=IpAddress
_FsMIRip2IfConfAddress_Object=MibTableColumn
fsMIRip2IfConfAddress=_FsMIRip2IfConfAddress_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,1),_FsMIRip2IfConfAddress_Type())
fsMIRip2IfConfAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2IfConfAddress.setStatus(_A)
class _FsMIRip2IfAdminStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('passive',3)))
_FsMIRip2IfAdminStat_Type.__name__=_C
_FsMIRip2IfAdminStat_Object=MibTableColumn
fsMIRip2IfAdminStat=_FsMIRip2IfAdminStat_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,2),_FsMIRip2IfAdminStat_Type())
fsMIRip2IfAdminStat.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfAdminStat.setStatus(_A)
class _FsMIRip2IfConfOperState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operup',1),('operdown',2)))
_FsMIRip2IfConfOperState_Type.__name__=_C
_FsMIRip2IfConfOperState_Object=MibTableColumn
fsMIRip2IfConfOperState=_FsMIRip2IfConfOperState_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,3),_FsMIRip2IfConfOperState_Type())
fsMIRip2IfConfOperState.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2IfConfOperState.setStatus(_A)
class _FsMIRip2IfConfUpdateTmr_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_FsMIRip2IfConfUpdateTmr_Type.__name__=_C
_FsMIRip2IfConfUpdateTmr_Object=MibTableColumn
fsMIRip2IfConfUpdateTmr=_FsMIRip2IfConfUpdateTmr_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,4),_FsMIRip2IfConfUpdateTmr_Type())
fsMIRip2IfConfUpdateTmr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfConfUpdateTmr.setStatus(_A)
class _FsMIRip2IfConfGarbgCollectTmr_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,180))
_FsMIRip2IfConfGarbgCollectTmr_Type.__name__=_C
_FsMIRip2IfConfGarbgCollectTmr_Object=MibTableColumn
fsMIRip2IfConfGarbgCollectTmr=_FsMIRip2IfConfGarbgCollectTmr_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,5),_FsMIRip2IfConfGarbgCollectTmr_Type())
fsMIRip2IfConfGarbgCollectTmr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfConfGarbgCollectTmr.setStatus(_A)
class _FsMIRip2IfConfRouteAgeTmr_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,500))
_FsMIRip2IfConfRouteAgeTmr_Type.__name__=_C
_FsMIRip2IfConfRouteAgeTmr_Object=MibTableColumn
fsMIRip2IfConfRouteAgeTmr=_FsMIRip2IfConfRouteAgeTmr_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,6),_FsMIRip2IfConfRouteAgeTmr_Type())
fsMIRip2IfConfRouteAgeTmr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfConfRouteAgeTmr.setStatus(_A)
class _FsMIRip2IfSplitHorizonStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('splitHorizon',1),('splitHorizonWithPoisRev',2),(_R,3)))
_FsMIRip2IfSplitHorizonStatus_Type.__name__=_C
_FsMIRip2IfSplitHorizonStatus_Object=MibTableColumn
fsMIRip2IfSplitHorizonStatus=_FsMIRip2IfSplitHorizonStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,7),_FsMIRip2IfSplitHorizonStatus_Type())
fsMIRip2IfSplitHorizonStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfSplitHorizonStatus.setStatus(_A)
class _FsMIRip2IfConfDefRtInstall_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('installDefRt',1),('doNotInstallDefRt',2)))
_FsMIRip2IfConfDefRtInstall_Type.__name__=_C
_FsMIRip2IfConfDefRtInstall_Object=MibTableColumn
fsMIRip2IfConfDefRtInstall=_FsMIRip2IfConfDefRtInstall_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,8),_FsMIRip2IfConfDefRtInstall_Type())
fsMIRip2IfConfDefRtInstall.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfConfDefRtInstall.setStatus(_A)
class _FsMIRip2IfConfSpacingTmr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360))
_FsMIRip2IfConfSpacingTmr_Type.__name__=_C
_FsMIRip2IfConfSpacingTmr_Object=MibTableColumn
fsMIRip2IfConfSpacingTmr=_FsMIRip2IfConfSpacingTmr_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,9),_FsMIRip2IfConfSpacingTmr_Type())
fsMIRip2IfConfSpacingTmr.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2IfConfSpacingTmr.setStatus(_A)
class _FsMIRip2IfConfInUseKey_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRip2IfConfInUseKey_Type.__name__=_C
_FsMIRip2IfConfInUseKey_Object=MibTableColumn
fsMIRip2IfConfInUseKey=_FsMIRip2IfConfInUseKey_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,10),_FsMIRip2IfConfInUseKey_Type())
fsMIRip2IfConfInUseKey.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2IfConfInUseKey.setStatus(_A)
class _FsMIRip2IfConfAuthLastKeyStatus_Type(TruthValue):defaultValue=2
_FsMIRip2IfConfAuthLastKeyStatus_Type.__name__=_N
_FsMIRip2IfConfAuthLastKeyStatus_Object=MibTableColumn
fsMIRip2IfConfAuthLastKeyStatus=_FsMIRip2IfConfAuthLastKeyStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,4,1,11),_FsMIRip2IfConfAuthLastKeyStatus_Type())
fsMIRip2IfConfAuthLastKeyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2IfConfAuthLastKeyStatus.setStatus(_A)
_FsMIRipMd5AuthTable_Object=MibTable
fsMIRipMd5AuthTable=_FsMIRipMd5AuthTable_Object((1,3,6,1,4,1,10876,101,1,151,1,5))
if mibBuilder.loadTexts:fsMIRipMd5AuthTable.setStatus(_A)
_FsMIRipMd5AuthEntry_Object=MibTableRow
fsMIRipMd5AuthEntry=_FsMIRipMd5AuthEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1))
fsMIRipMd5AuthEntry.setIndexNames((0,_D,_F),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:fsMIRipMd5AuthEntry.setStatus(_A)
_FsMIRipMd5AuthAddress_Type=IpAddress
_FsMIRipMd5AuthAddress_Object=MibTableColumn
fsMIRipMd5AuthAddress=_FsMIRipMd5AuthAddress_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,1),_FsMIRipMd5AuthAddress_Type())
fsMIRipMd5AuthAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipMd5AuthAddress.setStatus(_A)
class _FsMIRipMd5AuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipMd5AuthKeyId_Type.__name__=_C
_FsMIRipMd5AuthKeyId_Object=MibTableColumn
fsMIRipMd5AuthKeyId=_FsMIRipMd5AuthKeyId_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,2),_FsMIRipMd5AuthKeyId_Type())
fsMIRipMd5AuthKeyId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipMd5AuthKeyId.setStatus(_A)
class _FsMIRipMd5AuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIRipMd5AuthKey_Type.__name__=_K
_FsMIRipMd5AuthKey_Object=MibTableColumn
fsMIRipMd5AuthKey=_FsMIRipMd5AuthKey_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,3),_FsMIRipMd5AuthKey_Type())
fsMIRipMd5AuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipMd5AuthKey.setStatus(_A)
_FsMIRipMd5KeyStartTime_Type=Integer32
_FsMIRipMd5KeyStartTime_Object=MibTableColumn
fsMIRipMd5KeyStartTime=_FsMIRipMd5KeyStartTime_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,4),_FsMIRipMd5KeyStartTime_Type())
fsMIRipMd5KeyStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipMd5KeyStartTime.setStatus(_A)
_FsMIRipMd5KeyExpiryTime_Type=Integer32
_FsMIRipMd5KeyExpiryTime_Object=MibTableColumn
fsMIRipMd5KeyExpiryTime=_FsMIRipMd5KeyExpiryTime_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,5),_FsMIRipMd5KeyExpiryTime_Type())
fsMIRipMd5KeyExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipMd5KeyExpiryTime.setStatus(_A)
_FsMIRipMd5KeyRowStatus_Type=RowStatus
_FsMIRipMd5KeyRowStatus_Object=MibTableColumn
fsMIRipMd5KeyRowStatus=_FsMIRipMd5KeyRowStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,5,1,6),_FsMIRipMd5KeyRowStatus_Type())
fsMIRipMd5KeyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipMd5KeyRowStatus.setStatus(_A)
_FsMIRip2NBRUnicastListTable_Object=MibTable
fsMIRip2NBRUnicastListTable=_FsMIRip2NBRUnicastListTable_Object((1,3,6,1,4,1,10876,101,1,151,1,6))
if mibBuilder.loadTexts:fsMIRip2NBRUnicastListTable.setStatus(_A)
_FsMIRip2NBRUnicastListEntry_Object=MibTableRow
fsMIRip2NBRUnicastListEntry=_FsMIRip2NBRUnicastListEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,6,1))
fsMIRip2NBRUnicastListEntry.setIndexNames((0,_D,_F),(0,_D,_W))
if mibBuilder.loadTexts:fsMIRip2NBRUnicastListEntry.setStatus(_A)
_FsMIRip2NBRUnicastIpAddr_Type=IpAddress
_FsMIRip2NBRUnicastIpAddr_Object=MibTableColumn
fsMIRip2NBRUnicastIpAddr=_FsMIRip2NBRUnicastIpAddr_Object((1,3,6,1,4,1,10876,101,1,151,1,6,1,1),_FsMIRip2NBRUnicastIpAddr_Type())
fsMIRip2NBRUnicastIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2NBRUnicastIpAddr.setStatus(_A)
_FsMIRip2NBRUnicastNBRRowStatus_Type=RowStatus
_FsMIRip2NBRUnicastNBRRowStatus_Object=MibTableColumn
fsMIRip2NBRUnicastNBRRowStatus=_FsMIRip2NBRUnicastNBRRowStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,6,1,2),_FsMIRip2NBRUnicastNBRRowStatus_Type())
fsMIRip2NBRUnicastNBRRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRip2NBRUnicastNBRRowStatus.setStatus(_A)
_FsMIRip2LocalRouteTable_Object=MibTable
fsMIRip2LocalRouteTable=_FsMIRip2LocalRouteTable_Object((1,3,6,1,4,1,10876,101,1,151,1,7))
if mibBuilder.loadTexts:fsMIRip2LocalRouteTable.setStatus(_A)
_FsMIRip2LocalRouteEntry_Object=MibTableRow
fsMIRip2LocalRouteEntry=_FsMIRip2LocalRouteEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1))
fsMIRip2LocalRouteEntry.setIndexNames((0,_D,_F),(0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:fsMIRip2LocalRouteEntry.setStatus(_A)
_FsMIRip2DestNet_Type=IpAddress
_FsMIRip2DestNet_Object=MibTableColumn
fsMIRip2DestNet=_FsMIRip2DestNet_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,1),_FsMIRip2DestNet_Type())
fsMIRip2DestNet.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2DestNet.setStatus(_A)
_FsMIRip2DestMask_Type=IpAddress
_FsMIRip2DestMask_Object=MibTableColumn
fsMIRip2DestMask=_FsMIRip2DestMask_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,2),_FsMIRip2DestMask_Type())
fsMIRip2DestMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2DestMask.setStatus(_A)
class _FsMIRip2Tos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsMIRip2Tos_Type.__name__=_C
_FsMIRip2Tos_Object=MibTableColumn
fsMIRip2Tos=_FsMIRip2Tos_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,3),_FsMIRip2Tos_Type())
fsMIRip2Tos.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2Tos.setStatus(_A)
_FsMIRip2NextHop_Type=IpAddress
_FsMIRip2NextHop_Object=MibTableColumn
fsMIRip2NextHop=_FsMIRip2NextHop_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,4),_FsMIRip2NextHop_Type())
fsMIRip2NextHop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRip2NextHop.setStatus(_A)
_FsMIRip2RtIfIndex_Type=Integer32
_FsMIRip2RtIfIndex_Object=MibTableColumn
fsMIRip2RtIfIndex=_FsMIRip2RtIfIndex_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,5),_FsMIRip2RtIfIndex_Type())
fsMIRip2RtIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2RtIfIndex.setStatus(_A)
_FsMIRip2RtType_Type=Integer32
_FsMIRip2RtType_Object=MibTableColumn
fsMIRip2RtType=_FsMIRip2RtType_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,6),_FsMIRip2RtType_Type())
fsMIRip2RtType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2RtType.setStatus(_A)
_FsMIRip2Proto_Type=Integer32
_FsMIRip2Proto_Object=MibTableColumn
fsMIRip2Proto=_FsMIRip2Proto_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,7),_FsMIRip2Proto_Type())
fsMIRip2Proto.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2Proto.setStatus(_A)
_FsMIRip2ChgTime_Type=Integer32
_FsMIRip2ChgTime_Object=MibTableColumn
fsMIRip2ChgTime=_FsMIRip2ChgTime_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,8),_FsMIRip2ChgTime_Type())
fsMIRip2ChgTime.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2ChgTime.setStatus(_A)
_FsMIRip2Metric_Type=Integer32
_FsMIRip2Metric_Object=MibTableColumn
fsMIRip2Metric=_FsMIRip2Metric_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,9),_FsMIRip2Metric_Type())
fsMIRip2Metric.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2Metric.setStatus(_A)
_FsMIRip2RowStatus_Type=Integer32
_FsMIRip2RowStatus_Object=MibTableColumn
fsMIRip2RowStatus=_FsMIRip2RowStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,10),_FsMIRip2RowStatus_Type())
fsMIRip2RowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2RowStatus.setStatus(_A)
_FsMIRip2Gateway_Type=IpAddress
_FsMIRip2Gateway_Object=MibTableColumn
fsMIRip2Gateway=_FsMIRip2Gateway_Object((1,3,6,1,4,1,10876,101,1,151,1,7,1,11),_FsMIRip2Gateway_Type())
fsMIRip2Gateway.setMaxAccess(_G)
if mibBuilder.loadTexts:fsMIRip2Gateway.setStatus(_A)
_FsMIRipAggTable_Object=MibTable
fsMIRipAggTable=_FsMIRipAggTable_Object((1,3,6,1,4,1,10876,101,1,151,1,8))
if mibBuilder.loadTexts:fsMIRipAggTable.setStatus(_A)
_FsMIRipAggEntry_Object=MibTableRow
fsMIRipAggEntry=_FsMIRipAggEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,8,1))
fsMIRipAggEntry.setIndexNames((0,_D,_F),(0,_D,_b),(0,_D,_c),(0,_D,_d))
if mibBuilder.loadTexts:fsMIRipAggEntry.setStatus(_A)
class _FsMIRipIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FsMIRipIfIndex_Type.__name__=_C
_FsMIRipIfIndex_Object=MibTableColumn
fsMIRipIfIndex=_FsMIRipIfIndex_Object((1,3,6,1,4,1,10876,101,1,151,1,8,1,1),_FsMIRipIfIndex_Type())
fsMIRipIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipIfIndex.setStatus(_A)
_FsMIRipAggAddress_Type=IpAddress
_FsMIRipAggAddress_Object=MibTableColumn
fsMIRipAggAddress=_FsMIRipAggAddress_Object((1,3,6,1,4,1,10876,101,1,151,1,8,1,2),_FsMIRipAggAddress_Type())
fsMIRipAggAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipAggAddress.setStatus(_A)
_FsMIRipAggAddressMask_Type=IpAddress
_FsMIRipAggAddressMask_Object=MibTableColumn
fsMIRipAggAddressMask=_FsMIRipAggAddressMask_Object((1,3,6,1,4,1,10876,101,1,151,1,8,1,3),_FsMIRipAggAddressMask_Type())
fsMIRipAggAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipAggAddressMask.setStatus(_A)
_FsMIRipAggStatus_Type=RowStatus
_FsMIRipAggStatus_Object=MibTableColumn
fsMIRipAggStatus=_FsMIRipAggStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,8,1,4),_FsMIRipAggStatus_Type())
fsMIRipAggStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipAggStatus.setStatus(_A)
_FsMIRipCryptoAuthTable_Object=MibTable
fsMIRipCryptoAuthTable=_FsMIRipCryptoAuthTable_Object((1,3,6,1,4,1,10876,101,1,151,1,9))
if mibBuilder.loadTexts:fsMIRipCryptoAuthTable.setStatus(_A)
_FsMIRipCryptoAuthEntry_Object=MibTableRow
fsMIRipCryptoAuthEntry=_FsMIRipCryptoAuthEntry_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1))
fsMIRipCryptoAuthEntry.setIndexNames((0,_D,_F),(0,_D,_e),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:fsMIRipCryptoAuthEntry.setStatus(_A)
class _FsMIRipCryptoAuthIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRipCryptoAuthIfIndex_Type.__name__=_L
_FsMIRipCryptoAuthIfIndex_Object=MibTableColumn
fsMIRipCryptoAuthIfIndex=_FsMIRipCryptoAuthIfIndex_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,1),_FsMIRipCryptoAuthIfIndex_Type())
fsMIRipCryptoAuthIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipCryptoAuthIfIndex.setStatus(_A)
_FsMIRipCryptoAuthAddress_Type=IpAddress
_FsMIRipCryptoAuthAddress_Object=MibTableColumn
fsMIRipCryptoAuthAddress=_FsMIRipCryptoAuthAddress_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,2),_FsMIRipCryptoAuthAddress_Type())
fsMIRipCryptoAuthAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipCryptoAuthAddress.setStatus(_A)
class _FsMIRipCryptoAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipCryptoAuthKeyId_Type.__name__=_C
_FsMIRipCryptoAuthKeyId_Object=MibTableColumn
fsMIRipCryptoAuthKeyId=_FsMIRipCryptoAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,3),_FsMIRipCryptoAuthKeyId_Type())
fsMIRipCryptoAuthKeyId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipCryptoAuthKeyId.setStatus(_A)
class _FsMIRipCryptoAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsMIRipCryptoAuthKey_Type.__name__=_K
_FsMIRipCryptoAuthKey_Object=MibTableColumn
fsMIRipCryptoAuthKey=_FsMIRipCryptoAuthKey_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,4),_FsMIRipCryptoAuthKey_Type())
fsMIRipCryptoAuthKey.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoAuthKey.setStatus(_A)
_FsMIRipCryptoKeyStartAccept_Type=DateAndTime
_FsMIRipCryptoKeyStartAccept_Object=MibTableColumn
fsMIRipCryptoKeyStartAccept=_FsMIRipCryptoKeyStartAccept_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,5),_FsMIRipCryptoKeyStartAccept_Type())
fsMIRipCryptoKeyStartAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoKeyStartAccept.setStatus(_A)
_FsMIRipCryptoKeyStartGenerate_Type=DateAndTime
_FsMIRipCryptoKeyStartGenerate_Object=MibTableColumn
fsMIRipCryptoKeyStartGenerate=_FsMIRipCryptoKeyStartGenerate_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,6),_FsMIRipCryptoKeyStartGenerate_Type())
fsMIRipCryptoKeyStartGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoKeyStartGenerate.setStatus(_A)
_FsMIRipCryptoKeyStopGenerate_Type=DateAndTime
_FsMIRipCryptoKeyStopGenerate_Object=MibTableColumn
fsMIRipCryptoKeyStopGenerate=_FsMIRipCryptoKeyStopGenerate_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,7),_FsMIRipCryptoKeyStopGenerate_Type())
fsMIRipCryptoKeyStopGenerate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoKeyStopGenerate.setStatus(_A)
_FsMIRipCryptoKeyStopAccept_Type=DateAndTime
_FsMIRipCryptoKeyStopAccept_Object=MibTableColumn
fsMIRipCryptoKeyStopAccept=_FsMIRipCryptoKeyStopAccept_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,8),_FsMIRipCryptoKeyStopAccept_Type())
fsMIRipCryptoKeyStopAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoKeyStopAccept.setStatus(_A)
class _FsMIRipCryptoKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('delete',2)))
_FsMIRipCryptoKeyStatus_Type.__name__=_C
_FsMIRipCryptoKeyStatus_Object=MibTableColumn
fsMIRipCryptoKeyStatus=_FsMIRipCryptoKeyStatus_Object((1,3,6,1,4,1,10876,101,1,151,1,9,1,9),_FsMIRipCryptoKeyStatus_Type())
fsMIRipCryptoKeyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipCryptoKeyStatus.setStatus(_A)
_FsMIRipRRDGeneralGroup_ObjectIdentity=ObjectIdentity
fsMIRipRRDGeneralGroup=_FsMIRipRRDGeneralGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,2))
_FsMIRipRRDGlobalTable_Object=MibTable
fsMIRipRRDGlobalTable=_FsMIRipRRDGlobalTable_Object((1,3,6,1,4,1,10876,101,1,151,2,1))
if mibBuilder.loadTexts:fsMIRipRRDGlobalTable.setStatus(_A)
_FsMIRipRRDGlobalEntry_Object=MibTableRow
fsMIRipRRDGlobalEntry=_FsMIRipRRDGlobalEntry_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1))
fsMIRipRRDGlobalEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIRipRRDGlobalEntry.setStatus(_A)
class _FsMIRipRRDGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsMIRipRRDGlobalStatus_Type.__name__=_C
_FsMIRipRRDGlobalStatus_Object=MibTableColumn
fsMIRipRRDGlobalStatus=_FsMIRipRRDGlobalStatus_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,1),_FsMIRipRRDGlobalStatus_Type())
fsMIRipRRDGlobalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDGlobalStatus.setStatus(_A)
class _FsMIRipRRDSrcProtoMaskEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRipRRDSrcProtoMaskEnable_Type.__name__=_C
_FsMIRipRRDSrcProtoMaskEnable_Object=MibTableColumn
fsMIRipRRDSrcProtoMaskEnable=_FsMIRipRRDSrcProtoMaskEnable_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,2),_FsMIRipRRDSrcProtoMaskEnable_Type())
fsMIRipRRDSrcProtoMaskEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDSrcProtoMaskEnable.setStatus(_A)
class _FsMIRipRRDSrcProtoMaskDisable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRipRRDSrcProtoMaskDisable_Type.__name__=_C
_FsMIRipRRDSrcProtoMaskDisable_Object=MibTableColumn
fsMIRipRRDSrcProtoMaskDisable=_FsMIRipRRDSrcProtoMaskDisable_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,3),_FsMIRipRRDSrcProtoMaskDisable_Type())
fsMIRipRRDSrcProtoMaskDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDSrcProtoMaskDisable.setStatus(_A)
class _FsMIRipRRDRouteTagType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('automatic',2)))
_FsMIRipRRDRouteTagType_Type.__name__=_C
_FsMIRipRRDRouteTagType_Object=MibTableColumn
fsMIRipRRDRouteTagType=_FsMIRipRRDRouteTagType_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,4),_FsMIRipRRDRouteTagType_Type())
fsMIRipRRDRouteTagType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDRouteTagType.setStatus(_A)
class _FsMIRipRRDRouteTag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRipRRDRouteTag_Type.__name__=_C
_FsMIRipRRDRouteTag_Object=MibTableColumn
fsMIRipRRDRouteTag=_FsMIRipRRDRouteTag_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,5),_FsMIRipRRDRouteTag_Type())
fsMIRipRRDRouteTag.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDRouteTag.setStatus(_A)
class _FsMIRipRRDRouteDefMetric_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsMIRipRRDRouteDefMetric_Type.__name__=_C
_FsMIRipRRDRouteDefMetric_Object=MibTableColumn
fsMIRipRRDRouteDefMetric=_FsMIRipRRDRouteDefMetric_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,6),_FsMIRipRRDRouteDefMetric_Type())
fsMIRipRRDRouteDefMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDRouteDefMetric.setStatus(_A)
class _FsMIRipRRDRouteMapEnable_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_FsMIRipRRDRouteMapEnable_Type.__name__=_M
_FsMIRipRRDRouteMapEnable_Object=MibTableColumn
fsMIRipRRDRouteMapEnable=_FsMIRipRRDRouteMapEnable_Object((1,3,6,1,4,1,10876,101,1,151,2,1,1,7),_FsMIRipRRDRouteMapEnable_Type())
fsMIRipRRDRouteMapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipRRDRouteMapEnable.setStatus(_A)
_FsMIripDistInOutRouteMap_ObjectIdentity=ObjectIdentity
fsMIripDistInOutRouteMap=_FsMIripDistInOutRouteMap_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,3))
_FsMIRipDistInOutRouteMapTable_Object=MibTable
fsMIRipDistInOutRouteMapTable=_FsMIRipDistInOutRouteMapTable_Object((1,3,6,1,4,1,10876,101,1,151,3,1))
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapTable.setStatus(_A)
_FsMIRipDistInOutRouteMapEntry_Object=MibTableRow
fsMIRipDistInOutRouteMapEntry=_FsMIRipDistInOutRouteMapEntry_Object((1,3,6,1,4,1,10876,101,1,151,3,1,1))
fsMIRipDistInOutRouteMapEntry.setIndexNames((0,_D,_F),(0,_D,_h),(0,_D,_i))
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapEntry.setStatus(_A)
class _FsMIRipDistInOutRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_FsMIRipDistInOutRouteMapName_Type.__name__=_M
_FsMIRipDistInOutRouteMapName_Object=MibTableColumn
fsMIRipDistInOutRouteMapName=_FsMIRipDistInOutRouteMapName_Object((1,3,6,1,4,1,10876,101,1,151,3,1,1,1),_FsMIRipDistInOutRouteMapName_Type())
fsMIRipDistInOutRouteMapName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapName.setStatus(_A)
class _FsMIRipDistInOutRouteMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_FsMIRipDistInOutRouteMapType_Type.__name__=_C
_FsMIRipDistInOutRouteMapType_Object=MibTableColumn
fsMIRipDistInOutRouteMapType=_FsMIRipDistInOutRouteMapType_Object((1,3,6,1,4,1,10876,101,1,151,3,1,1,2),_FsMIRipDistInOutRouteMapType_Type())
fsMIRipDistInOutRouteMapType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapType.setStatus(_A)
class _FsMIRipDistInOutRouteMapValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsMIRipDistInOutRouteMapValue_Type.__name__=_C
_FsMIRipDistInOutRouteMapValue_Object=MibTableColumn
fsMIRipDistInOutRouteMapValue=_FsMIRipDistInOutRouteMapValue_Object((1,3,6,1,4,1,10876,101,1,151,3,1,1,3),_FsMIRipDistInOutRouteMapValue_Type())
fsMIRipDistInOutRouteMapValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapValue.setStatus(_A)
_FsMIRipDistInOutRouteMapRowStatus_Type=RowStatus
_FsMIRipDistInOutRouteMapRowStatus_Object=MibTableColumn
fsMIRipDistInOutRouteMapRowStatus=_FsMIRipDistInOutRouteMapRowStatus_Object((1,3,6,1,4,1,10876,101,1,151,3,1,1,4),_FsMIRipDistInOutRouteMapRowStatus_Type())
fsMIRipDistInOutRouteMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipDistInOutRouteMapRowStatus.setStatus(_A)
_FsMIripPreferenceGroup_ObjectIdentity=ObjectIdentity
fsMIripPreferenceGroup=_FsMIripPreferenceGroup_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,4))
_FsMIRipPreferenceTable_Object=MibTable
fsMIRipPreferenceTable=_FsMIRipPreferenceTable_Object((1,3,6,1,4,1,10876,101,1,151,4,1))
if mibBuilder.loadTexts:fsMIRipPreferenceTable.setStatus(_A)
_FsMIRipPreferenceEntry_Object=MibTableRow
fsMIRipPreferenceEntry=_FsMIRipPreferenceEntry_Object((1,3,6,1,4,1,10876,101,1,151,4,1,1))
fsMIRipPreferenceEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIRipPreferenceEntry.setStatus(_A)
class _FsMIRipPreferenceValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipPreferenceValue_Type.__name__=_C
_FsMIRipPreferenceValue_Object=MibTableColumn
fsMIRipPreferenceValue=_FsMIRipPreferenceValue_Object((1,3,6,1,4,1,10876,101,1,151,4,1,1,1),_FsMIRipPreferenceValue_Type())
fsMIRipPreferenceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRipPreferenceValue.setStatus(_A)
_FsMIRip2TrapsControl_ObjectIdentity=ObjectIdentity
fsMIRip2TrapsControl=_FsMIRip2TrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,5))
class _FsMIRip2ContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRip2ContextId_Type.__name__=_C
_FsMIRip2ContextId_Object=MibScalar
fsMIRip2ContextId=_FsMIRip2ContextId_Object((1,3,6,1,4,1,10876,101,1,151,5,1),_FsMIRip2ContextId_Type())
fsMIRip2ContextId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIRip2ContextId.setStatus(_A)
class _FsMIRipAuthIfIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRipAuthIfIndex_Type.__name__=_L
_FsMIRipAuthIfIndex_Object=MibScalar
fsMIRipAuthIfIndex=_FsMIRipAuthIfIndex_Object((1,3,6,1,4,1,10876,101,1,151,5,2),_FsMIRipAuthIfIndex_Type())
fsMIRipAuthIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIRipAuthIfIndex.setStatus(_A)
class _FsMIRipAuthKeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRipAuthKeyId_Type.__name__=_C
_FsMIRipAuthKeyId_Object=MibScalar
fsMIRipAuthKeyId=_FsMIRipAuthKeyId_Object((1,3,6,1,4,1,10876,101,1,151,5,3),_FsMIRipAuthKeyId_Type())
fsMIRipAuthKeyId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIRipAuthKeyId.setStatus(_A)
_FsMIRipPeerAddress_Type=IpAddress
_FsMIRipPeerAddress_Object=MibScalar
fsMIRipPeerAddress=_FsMIRipPeerAddress_Object((1,3,6,1,4,1,10876,101,1,151,5,4),_FsMIRipPeerAddress_Type())
fsMIRipPeerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:fsMIRipPeerAddress.setStatus(_A)
_FsMIRip2Notification_ObjectIdentity=ObjectIdentity
fsMIRip2Notification=_FsMIRip2Notification_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,6))
_FsMIRip2Traps_ObjectIdentity=ObjectIdentity
fsMIRip2Traps=_FsMIRip2Traps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,151,6,0))
fsMIRip2AuthenticationFailure=NotificationType((1,3,6,1,4,1,10876,101,1,151,6,0,1))
fsMIRip2AuthenticationFailure.setObjects(*((_D,_O),(_D,_j),(_D,_P),(_D,_Q)))
if mibBuilder.loadTexts:fsMIRip2AuthenticationFailure.setStatus(_A)
fsMIRip2AuthLastKey=NotificationType((1,3,6,1,4,1,10876,101,1,151,6,0,2))
fsMIRip2AuthLastKey.setObjects(*((_D,_O),(_D,_P),(_D,_Q)))
if mibBuilder.loadTexts:fsMIRip2AuthLastKey.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsMIRip':fsMIRip,'fsMIRip2GeneralGroup':fsMIRip2GeneralGroup,'fsMIRip2GlobalTable':fsMIRip2GlobalTable,'fsMIRip2GlobalEntry':fsMIRip2GlobalEntry,_F:fsMIRipContextId,'fsMIRip2Security':fsMIRip2Security,'fsMIRip2Peers':fsMIRip2Peers,'fsMIRip2TrustNBRListEnable':fsMIRip2TrustNBRListEnable,'fsMIRip2NumberOfDroppedPkts':fsMIRip2NumberOfDroppedPkts,'fsMIRip2SpacingEnable':fsMIRip2SpacingEnable,'fsMIRip2AutoSummaryStatus':fsMIRip2AutoSummaryStatus,'fsMIRip2RetransTimeoutInt':fsMIRip2RetransTimeoutInt,'fsMIRip2MaxRetransmissions':fsMIRip2MaxRetransmissions,'fsMIRip2OverSubscriptionTimeout':fsMIRip2OverSubscriptionTimeout,'fsMIRip2Propagate':fsMIRip2Propagate,'fsMIRipTrcFlag':fsMIRipTrcFlag,'fsMIRipRowStatus':fsMIRipRowStatus,'fsMIRipAdminStatus':fsMIRipAdminStatus,'fsMIRip2LastAuthKeyLifetimeStatus':fsMIRip2LastAuthKeyLifetimeStatus,'fsMIRipRtCount':fsMIRipRtCount,'fsMIRipGlobalTrcFlag':fsMIRipGlobalTrcFlag,'fsMIRip2NBRTrustListTable':fsMIRip2NBRTrustListTable,'fsMIRip2NBRTrustListEntry':fsMIRip2NBRTrustListEntry,_S:fsMIRip2TrustNBRIpAddr,'fsMIRip2TrustNBRRowStatus':fsMIRip2TrustNBRRowStatus,'fsMIRip2IfConfTable':fsMIRip2IfConfTable,'fsMIRip2IfConfEntry':fsMIRip2IfConfEntry,_T:fsMIRip2IfConfAddress,'fsMIRip2IfAdminStat':fsMIRip2IfAdminStat,'fsMIRip2IfConfOperState':fsMIRip2IfConfOperState,'fsMIRip2IfConfUpdateTmr':fsMIRip2IfConfUpdateTmr,'fsMIRip2IfConfGarbgCollectTmr':fsMIRip2IfConfGarbgCollectTmr,'fsMIRip2IfConfRouteAgeTmr':fsMIRip2IfConfRouteAgeTmr,'fsMIRip2IfSplitHorizonStatus':fsMIRip2IfSplitHorizonStatus,'fsMIRip2IfConfDefRtInstall':fsMIRip2IfConfDefRtInstall,'fsMIRip2IfConfSpacingTmr':fsMIRip2IfConfSpacingTmr,'fsMIRip2IfConfInUseKey':fsMIRip2IfConfInUseKey,'fsMIRip2IfConfAuthLastKeyStatus':fsMIRip2IfConfAuthLastKeyStatus,'fsMIRipMd5AuthTable':fsMIRipMd5AuthTable,'fsMIRipMd5AuthEntry':fsMIRipMd5AuthEntry,_U:fsMIRipMd5AuthAddress,_V:fsMIRipMd5AuthKeyId,'fsMIRipMd5AuthKey':fsMIRipMd5AuthKey,'fsMIRipMd5KeyStartTime':fsMIRipMd5KeyStartTime,'fsMIRipMd5KeyExpiryTime':fsMIRipMd5KeyExpiryTime,'fsMIRipMd5KeyRowStatus':fsMIRipMd5KeyRowStatus,'fsMIRip2NBRUnicastListTable':fsMIRip2NBRUnicastListTable,'fsMIRip2NBRUnicastListEntry':fsMIRip2NBRUnicastListEntry,_W:fsMIRip2NBRUnicastIpAddr,'fsMIRip2NBRUnicastNBRRowStatus':fsMIRip2NBRUnicastNBRRowStatus,'fsMIRip2LocalRouteTable':fsMIRip2LocalRouteTable,'fsMIRip2LocalRouteEntry':fsMIRip2LocalRouteEntry,_X:fsMIRip2DestNet,_Y:fsMIRip2DestMask,_Z:fsMIRip2Tos,_a:fsMIRip2NextHop,'fsMIRip2RtIfIndex':fsMIRip2RtIfIndex,'fsMIRip2RtType':fsMIRip2RtType,'fsMIRip2Proto':fsMIRip2Proto,'fsMIRip2ChgTime':fsMIRip2ChgTime,'fsMIRip2Metric':fsMIRip2Metric,'fsMIRip2RowStatus':fsMIRip2RowStatus,'fsMIRip2Gateway':fsMIRip2Gateway,'fsMIRipAggTable':fsMIRipAggTable,'fsMIRipAggEntry':fsMIRipAggEntry,_b:fsMIRipIfIndex,_c:fsMIRipAggAddress,_d:fsMIRipAggAddressMask,'fsMIRipAggStatus':fsMIRipAggStatus,'fsMIRipCryptoAuthTable':fsMIRipCryptoAuthTable,'fsMIRipCryptoAuthEntry':fsMIRipCryptoAuthEntry,_e:fsMIRipCryptoAuthIfIndex,_f:fsMIRipCryptoAuthAddress,_g:fsMIRipCryptoAuthKeyId,'fsMIRipCryptoAuthKey':fsMIRipCryptoAuthKey,'fsMIRipCryptoKeyStartAccept':fsMIRipCryptoKeyStartAccept,'fsMIRipCryptoKeyStartGenerate':fsMIRipCryptoKeyStartGenerate,'fsMIRipCryptoKeyStopGenerate':fsMIRipCryptoKeyStopGenerate,'fsMIRipCryptoKeyStopAccept':fsMIRipCryptoKeyStopAccept,'fsMIRipCryptoKeyStatus':fsMIRipCryptoKeyStatus,'fsMIRipRRDGeneralGroup':fsMIRipRRDGeneralGroup,'fsMIRipRRDGlobalTable':fsMIRipRRDGlobalTable,'fsMIRipRRDGlobalEntry':fsMIRipRRDGlobalEntry,'fsMIRipRRDGlobalStatus':fsMIRipRRDGlobalStatus,'fsMIRipRRDSrcProtoMaskEnable':fsMIRipRRDSrcProtoMaskEnable,'fsMIRipRRDSrcProtoMaskDisable':fsMIRipRRDSrcProtoMaskDisable,'fsMIRipRRDRouteTagType':fsMIRipRRDRouteTagType,'fsMIRipRRDRouteTag':fsMIRipRRDRouteTag,'fsMIRipRRDRouteDefMetric':fsMIRipRRDRouteDefMetric,'fsMIRipRRDRouteMapEnable':fsMIRipRRDRouteMapEnable,'fsMIripDistInOutRouteMap':fsMIripDistInOutRouteMap,'fsMIRipDistInOutRouteMapTable':fsMIRipDistInOutRouteMapTable,'fsMIRipDistInOutRouteMapEntry':fsMIRipDistInOutRouteMapEntry,_h:fsMIRipDistInOutRouteMapName,_i:fsMIRipDistInOutRouteMapType,'fsMIRipDistInOutRouteMapValue':fsMIRipDistInOutRouteMapValue,'fsMIRipDistInOutRouteMapRowStatus':fsMIRipDistInOutRouteMapRowStatus,'fsMIripPreferenceGroup':fsMIripPreferenceGroup,'fsMIRipPreferenceTable':fsMIRipPreferenceTable,'fsMIRipPreferenceEntry':fsMIRipPreferenceEntry,'fsMIRipPreferenceValue':fsMIRipPreferenceValue,'fsMIRip2TrapsControl':fsMIRip2TrapsControl,_O:fsMIRip2ContextId,_P:fsMIRipAuthIfIndex,_Q:fsMIRipAuthKeyId,_j:fsMIRipPeerAddress,'fsMIRip2Notification':fsMIRip2Notification,'fsMIRip2Traps':fsMIRip2Traps,'fsMIRip2AuthenticationFailure':fsMIRip2AuthenticationFailure,'fsMIRip2AuthLastKey':fsMIRip2AuthLastKey})