_AS='vsanGroupRev3'
_AR='vsanPortMembershipChange'
_AQ='vsanMembershipSummaryIntfType'
_AP='vsanFcTimerFstov'
_AO='vsanFcTimerDstov'
_AN='vsanFcTimerEdtov'
_AM='vsanFcTimerRatov'
_AL='vsanFcTimerForceFlag'
_AK='fcSwitchDropLatency'
_AJ='fcNetworkDropLatency'
_AI='vsanDynamicRowStatus'
_AH='vsanDynamicVsan'
_AG='vsanDynamicListNumber'
_AF='vsanWwnListRowStatus'
_AE='vsanWwnListWwn'
_AD='vsanWwnListNumber'
_AC='vsanIfDenyList'
_AB='vsanIfVsan'
_AA='vsanIfNumber'
_A9='vsanDenyUnknownWwn'
_A8='vsanInterOperMode'
_A7='vsanFcTimerEntry'
_A6='vsanWwnListWwnIndex'
_A5='VsanLoadBalancingType'
_A4='VsanAdminState'
_A3='VsanMediaType'
_A2='SnmpAdminString'
_A1='ListIndexOrZero'
_A0='ListIndex'
_z='vsanNotificationGroupRev1'
_y='vsanGroupRev1'
_x='vsanGroup'
_w='vsanStatusChange'
_v='vsanFcFeElementName'
_u='vsanNetworkDropLatency'
_t='vsanInorderDelivery'
_s='fcTimerDstov'
_r='fcTimerFstov'
_q='fcTimerEdtov'
_p='fcTimerRatov'
_o='vsanMembershipSummaryInterface'
_n='vsanWwnListIndex'
_m='not-accessible'
_l='vsanIndex'
_k='Unsigned32'
_j='ifIndex'
_i='IF-MIB'
_h='VsanIndex'
_g='vsanMembershipSummaryGroupRev1'
_f='vsanGroupRev2'
_e='vsanFcTimerGroup'
_d='vsanInterOperValue'
_c='fcInorderDelivery'
_b='vsanRowStatus'
_a='vsanLoadBalancingType'
_Z='vsanMtu'
_Y='vsanMediaType'
_X='vsanName'
_W='vsanLastChange'
_V='vsanNumber'
_U='TruthValue'
_T='vsanFcTimerGroupRev1'
_S='vsanOperState'
_R='vsanAdminState'
_Q='vsanNotificationGroup'
_P='notifyVsanIndex'
_O='Integer32'
_N='vsanVsanMembershipSummaryGroup'
_M='vsanWWNListGroup'
_L='vsanDynamicMembershipGroup'
_K='vsanFcLatencyGroup'
_J='vsanStaticMembershipGroup'
_I='vsanMembershipGroup'
_H='read-write'
_G='read-only'
_F='CiscoMilliSeconds'
_E='msec'
_D='deprecated'
_C='read-create'
_B='current'
_A='CISCO-VSAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId',_h)
CiscoMilliSeconds,ListIndex,ListIndexOrZero=mibBuilder.importSymbols('CISCO-TC',_F,_A0,_A1)
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_i,'InterfaceIndex',_j)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_A2)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_O,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_k,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_U)
ciscoVsanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,282))
if mibBuilder.loadTexts:ciscoVsanMIB.setRevisions(('2006-02-06 00:00','2005-12-07 00:00','2005-10-07 00:00','2005-06-07 00:00','2004-02-18 00:00','2003-12-02 00:00','2003-05-07 00:00','2003-04-23 00:00','2002-12-18 00:00','2002-11-04 00:00','2002-09-23 00:00'))
class VsanMediaType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fibreChannel',1),('ethernet',2),('infiniband',3),('other',4)))
class VsanAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('suspended',2)))
class VsanOperationalState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class VsanLoadBalancingType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('srcIdDestId',1),('srcIdDestIdOxId',2)))
_CiscoVsanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVsanMIBObjects=_CiscoVsanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,282,1))
_VsanConfiguration_ObjectIdentity=ObjectIdentity
vsanConfiguration=_VsanConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,1))
class _VsanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsanNumber_Type.__name__=_O
_VsanNumber_Object=MibScalar
vsanNumber=_VsanNumber_Object((1,3,6,1,4,1,9,9,282,1,1,1),_VsanNumber_Type())
vsanNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanNumber.setStatus(_B)
_VsanLastChange_Type=TimeStamp
_VsanLastChange_Object=MibScalar
vsanLastChange=_VsanLastChange_Object((1,3,6,1,4,1,9,9,282,1,1,2),_VsanLastChange_Type())
vsanLastChange.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanLastChange.setStatus(_B)
_VsanTable_Object=MibTable
vsanTable=_VsanTable_Object((1,3,6,1,4,1,9,9,282,1,1,3))
if mibBuilder.loadTexts:vsanTable.setStatus(_B)
_VsanEntry_Object=MibTableRow
vsanEntry=_VsanEntry_Object((1,3,6,1,4,1,9,9,282,1,1,3,1))
vsanEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:vsanEntry.setStatus(_B)
_VsanIndex_Type=VsanIndex
_VsanIndex_Object=MibTableColumn
vsanIndex=_VsanIndex_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,1),_VsanIndex_Type())
vsanIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:vsanIndex.setStatus(_B)
class _VsanName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VsanName_Type.__name__=_A2
_VsanName_Object=MibTableColumn
vsanName=_VsanName_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,2),_VsanName_Type())
vsanName.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanName.setStatus(_B)
class _VsanMediaType_Type(VsanMediaType):defaultValue=1
_VsanMediaType_Type.__name__=_A3
_VsanMediaType_Object=MibTableColumn
vsanMediaType=_VsanMediaType_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,3),_VsanMediaType_Type())
vsanMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanMediaType.setStatus(_B)
class _VsanAdminState_Type(VsanAdminState):defaultValue=1
_VsanAdminState_Type.__name__=_A4
_VsanAdminState_Object=MibTableColumn
vsanAdminState=_VsanAdminState_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,4),_VsanAdminState_Type())
vsanAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanAdminState.setStatus(_B)
class _VsanMtu_Type(Unsigned32):defaultValue=2112;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VsanMtu_Type.__name__=_k
_VsanMtu_Object=MibTableColumn
vsanMtu=_VsanMtu_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,5),_VsanMtu_Type())
vsanMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanMtu.setStatus(_B)
class _VsanLoadBalancingType_Type(VsanLoadBalancingType):defaultValue=2
_VsanLoadBalancingType_Type.__name__=_A5
_VsanLoadBalancingType_Object=MibTableColumn
vsanLoadBalancingType=_VsanLoadBalancingType_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,6),_VsanLoadBalancingType_Type())
vsanLoadBalancingType.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanLoadBalancingType.setStatus(_B)
class _VsanInterOperMode_Type(TruthValue):defaultValue=2
_VsanInterOperMode_Type.__name__=_U
_VsanInterOperMode_Object=MibTableColumn
vsanInterOperMode=_VsanInterOperMode_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,7),_VsanInterOperMode_Type())
vsanInterOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanInterOperMode.setStatus(_D)
_VsanOperState_Type=VsanOperationalState
_VsanOperState_Object=MibTableColumn
vsanOperState=_VsanOperState_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,8),_VsanOperState_Type())
vsanOperState.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanOperState.setStatus(_B)
_VsanRowStatus_Type=RowStatus
_VsanRowStatus_Object=MibTableColumn
vsanRowStatus=_VsanRowStatus_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,9),_VsanRowStatus_Type())
vsanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanRowStatus.setStatus(_B)
class _VsanInterOperValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_VsanInterOperValue_Type.__name__=_O
_VsanInterOperValue_Object=MibTableColumn
vsanInterOperValue=_VsanInterOperValue_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,10),_VsanInterOperValue_Type())
vsanInterOperValue.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanInterOperValue.setStatus(_B)
class _VsanInorderDelivery_Type(TruthValue):defaultValue=2
_VsanInorderDelivery_Type.__name__=_U
_VsanInorderDelivery_Object=MibTableColumn
vsanInorderDelivery=_VsanInorderDelivery_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,11),_VsanInorderDelivery_Type())
vsanInorderDelivery.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanInorderDelivery.setStatus(_B)
class _VsanNetworkDropLatency_Type(CiscoMilliSeconds):defaultValue=2000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,60000))
_VsanNetworkDropLatency_Type.__name__=_F
_VsanNetworkDropLatency_Object=MibTableColumn
vsanNetworkDropLatency=_VsanNetworkDropLatency_Object((1,3,6,1,4,1,9,9,282,1,1,3,1,12),_VsanNetworkDropLatency_Type())
vsanNetworkDropLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanNetworkDropLatency.setStatus(_B)
if mibBuilder.loadTexts:vsanNetworkDropLatency.setUnits(_E)
_NotifyVsanIndex_Type=VsanIndex
_NotifyVsanIndex_Object=MibScalar
notifyVsanIndex=_NotifyVsanIndex_Object((1,3,6,1,4,1,9,9,282,1,1,4),_NotifyVsanIndex_Type())
notifyVsanIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:notifyVsanIndex.setStatus(_B)
_VsanMembership_ObjectIdentity=ObjectIdentity
vsanMembership=_VsanMembership_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,2))
class _VsanDenyUnknownWwn_Type(TruthValue):defaultValue=2
_VsanDenyUnknownWwn_Type.__name__=_U
_VsanDenyUnknownWwn_Object=MibScalar
vsanDenyUnknownWwn=_VsanDenyUnknownWwn_Object((1,3,6,1,4,1,9,9,282,1,2,1),_VsanDenyUnknownWwn_Type())
vsanDenyUnknownWwn.setMaxAccess(_H)
if mibBuilder.loadTexts:vsanDenyUnknownWwn.setStatus(_B)
class _VsanWwnListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsanWwnListNumber_Type.__name__=_O
_VsanWwnListNumber_Object=MibScalar
vsanWwnListNumber=_VsanWwnListNumber_Object((1,3,6,1,4,1,9,9,282,1,2,2),_VsanWwnListNumber_Type())
vsanWwnListNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanWwnListNumber.setStatus(_B)
_VsanWwnListTable_Object=MibTable
vsanWwnListTable=_VsanWwnListTable_Object((1,3,6,1,4,1,9,9,282,1,2,3))
if mibBuilder.loadTexts:vsanWwnListTable.setStatus(_B)
_VsanWwnListEntry_Object=MibTableRow
vsanWwnListEntry=_VsanWwnListEntry_Object((1,3,6,1,4,1,9,9,282,1,2,3,1))
vsanWwnListEntry.setIndexNames((0,_A,_n),(0,_A,_A6))
if mibBuilder.loadTexts:vsanWwnListEntry.setStatus(_B)
class _VsanWwnListIndex_Type(ListIndex):subtypeSpec=ListIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VsanWwnListIndex_Type.__name__=_A0
_VsanWwnListIndex_Object=MibTableColumn
vsanWwnListIndex=_VsanWwnListIndex_Object((1,3,6,1,4,1,9,9,282,1,2,3,1,1),_VsanWwnListIndex_Type())
vsanWwnListIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:vsanWwnListIndex.setStatus(_B)
class _VsanWwnListWwnIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VsanWwnListWwnIndex_Type.__name__=_k
_VsanWwnListWwnIndex_Object=MibTableColumn
vsanWwnListWwnIndex=_VsanWwnListWwnIndex_Object((1,3,6,1,4,1,9,9,282,1,2,3,1,2),_VsanWwnListWwnIndex_Type())
vsanWwnListWwnIndex.setMaxAccess(_m)
if mibBuilder.loadTexts:vsanWwnListWwnIndex.setStatus(_B)
_VsanWwnListWwn_Type=FcNameId
_VsanWwnListWwn_Object=MibTableColumn
vsanWwnListWwn=_VsanWwnListWwn_Object((1,3,6,1,4,1,9,9,282,1,2,3,1,3),_VsanWwnListWwn_Type())
vsanWwnListWwn.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanWwnListWwn.setStatus(_B)
_VsanWwnListRowStatus_Type=RowStatus
_VsanWwnListRowStatus_Object=MibTableColumn
vsanWwnListRowStatus=_VsanWwnListRowStatus_Object((1,3,6,1,4,1,9,9,282,1,2,3,1,4),_VsanWwnListRowStatus_Type())
vsanWwnListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanWwnListRowStatus.setStatus(_B)
class _VsanIfNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsanIfNumber_Type.__name__=_O
_VsanIfNumber_Object=MibScalar
vsanIfNumber=_VsanIfNumber_Object((1,3,6,1,4,1,9,9,282,1,2,4),_VsanIfNumber_Type())
vsanIfNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanIfNumber.setStatus(_B)
_VsanIfTable_Object=MibTable
vsanIfTable=_VsanIfTable_Object((1,3,6,1,4,1,9,9,282,1,2,5))
if mibBuilder.loadTexts:vsanIfTable.setStatus(_B)
_VsanIfEntry_Object=MibTableRow
vsanIfEntry=_VsanIfEntry_Object((1,3,6,1,4,1,9,9,282,1,2,5,1))
vsanIfEntry.setIndexNames((0,_i,_j))
if mibBuilder.loadTexts:vsanIfEntry.setStatus(_B)
class _VsanIfVsan_Type(VsanIndex):defaultValue=1
_VsanIfVsan_Type.__name__=_h
_VsanIfVsan_Object=MibTableColumn
vsanIfVsan=_VsanIfVsan_Object((1,3,6,1,4,1,9,9,282,1,2,5,1,1),_VsanIfVsan_Type())
vsanIfVsan.setMaxAccess(_H)
if mibBuilder.loadTexts:vsanIfVsan.setStatus(_B)
class _VsanIfDenyList_Type(ListIndexOrZero):defaultValue=0
_VsanIfDenyList_Type.__name__=_A1
_VsanIfDenyList_Object=MibTableColumn
vsanIfDenyList=_VsanIfDenyList_Object((1,3,6,1,4,1,9,9,282,1,2,5,1,2),_VsanIfDenyList_Type())
vsanIfDenyList.setMaxAccess(_H)
if mibBuilder.loadTexts:vsanIfDenyList.setStatus(_B)
class _VsanDynamicListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsanDynamicListNumber_Type.__name__=_O
_VsanDynamicListNumber_Object=MibScalar
vsanDynamicListNumber=_VsanDynamicListNumber_Object((1,3,6,1,4,1,9,9,282,1,2,6),_VsanDynamicListNumber_Type())
vsanDynamicListNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanDynamicListNumber.setStatus(_B)
_VsanDynamicTable_Object=MibTable
vsanDynamicTable=_VsanDynamicTable_Object((1,3,6,1,4,1,9,9,282,1,2,7))
if mibBuilder.loadTexts:vsanDynamicTable.setStatus(_B)
_VsanDynamicEntry_Object=MibTableRow
vsanDynamicEntry=_VsanDynamicEntry_Object((1,3,6,1,4,1,9,9,282,1,2,7,1))
vsanDynamicEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:vsanDynamicEntry.setStatus(_B)
class _VsanDynamicVsan_Type(VsanIndex):defaultValue=1
_VsanDynamicVsan_Type.__name__=_h
_VsanDynamicVsan_Object=MibTableColumn
vsanDynamicVsan=_VsanDynamicVsan_Object((1,3,6,1,4,1,9,9,282,1,2,7,1,1),_VsanDynamicVsan_Type())
vsanDynamicVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanDynamicVsan.setStatus(_B)
_VsanDynamicRowStatus_Type=RowStatus
_VsanDynamicRowStatus_Object=MibTableColumn
vsanDynamicRowStatus=_VsanDynamicRowStatus_Object((1,3,6,1,4,1,9,9,282,1,2,7,1,2),_VsanDynamicRowStatus_Type())
vsanDynamicRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanDynamicRowStatus.setStatus(_B)
_VsanMembershipSummaryTable_Object=MibTable
vsanMembershipSummaryTable=_VsanMembershipSummaryTable_Object((1,3,6,1,4,1,9,9,282,1,2,8))
if mibBuilder.loadTexts:vsanMembershipSummaryTable.setStatus(_B)
_VsanMembershipSummaryEntry_Object=MibTableRow
vsanMembershipSummaryEntry=_VsanMembershipSummaryEntry_Object((1,3,6,1,4,1,9,9,282,1,2,8,1))
vsanMembershipSummaryEntry.setIndexNames((0,_A,_l),(0,_A,_o))
if mibBuilder.loadTexts:vsanMembershipSummaryEntry.setStatus(_B)
_VsanMembershipSummaryInterface_Type=InterfaceIndex
_VsanMembershipSummaryInterface_Object=MibTableColumn
vsanMembershipSummaryInterface=_VsanMembershipSummaryInterface_Object((1,3,6,1,4,1,9,9,282,1,2,8,1,1),_VsanMembershipSummaryInterface_Type())
vsanMembershipSummaryInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanMembershipSummaryInterface.setStatus(_B)
class _VsanMembershipSummaryIntfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('static',2),('dynamic',3)))
_VsanMembershipSummaryIntfType_Type.__name__=_O
_VsanMembershipSummaryIntfType_Object=MibTableColumn
vsanMembershipSummaryIntfType=_VsanMembershipSummaryIntfType_Object((1,3,6,1,4,1,9,9,282,1,2,8,1,2),_VsanMembershipSummaryIntfType_Type())
vsanMembershipSummaryIntfType.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanMembershipSummaryIntfType.setStatus(_B)
_VsanNotification_ObjectIdentity=ObjectIdentity
vsanNotification=_VsanNotification_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,3))
_VsanNotifications_ObjectIdentity=ObjectIdentity
vsanNotifications=_VsanNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,3,0))
_VsanFcConfiguration_ObjectIdentity=ObjectIdentity
vsanFcConfiguration=_VsanFcConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,4))
class _FcTimerRatov_Type(CiscoMilliSeconds):defaultValue=10000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,100000))
_FcTimerRatov_Type.__name__=_F
_FcTimerRatov_Object=MibScalar
fcTimerRatov=_FcTimerRatov_Object((1,3,6,1,4,1,9,9,282,1,4,1),_FcTimerRatov_Type())
fcTimerRatov.setMaxAccess(_H)
if mibBuilder.loadTexts:fcTimerRatov.setStatus(_B)
if mibBuilder.loadTexts:fcTimerRatov.setUnits(_E)
class _FcTimerEdtov_Type(CiscoMilliSeconds):defaultValue=2000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,100000))
_FcTimerEdtov_Type.__name__=_F
_FcTimerEdtov_Object=MibScalar
fcTimerEdtov=_FcTimerEdtov_Object((1,3,6,1,4,1,9,9,282,1,4,2),_FcTimerEdtov_Type())
fcTimerEdtov.setMaxAccess(_H)
if mibBuilder.loadTexts:fcTimerEdtov.setStatus(_B)
if mibBuilder.loadTexts:fcTimerEdtov.setUnits(_E)
_FcTimerFstov_Type=CiscoMilliSeconds
_FcTimerFstov_Object=MibScalar
fcTimerFstov=_FcTimerFstov_Object((1,3,6,1,4,1,9,9,282,1,4,3),_FcTimerFstov_Type())
fcTimerFstov.setMaxAccess(_G)
if mibBuilder.loadTexts:fcTimerFstov.setStatus(_B)
if mibBuilder.loadTexts:fcTimerFstov.setUnits(_E)
class _FcTimerDstov_Type(CiscoMilliSeconds):defaultValue=5000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,100000))
_FcTimerDstov_Type.__name__=_F
_FcTimerDstov_Object=MibScalar
fcTimerDstov=_FcTimerDstov_Object((1,3,6,1,4,1,9,9,282,1,4,4),_FcTimerDstov_Type())
fcTimerDstov.setMaxAccess(_H)
if mibBuilder.loadTexts:fcTimerDstov.setStatus(_B)
if mibBuilder.loadTexts:fcTimerDstov.setUnits(_E)
class _FcNetworkDropLatency_Type(CiscoMilliSeconds):defaultValue=2000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,60000))
_FcNetworkDropLatency_Type.__name__=_F
_FcNetworkDropLatency_Object=MibScalar
fcNetworkDropLatency=_FcNetworkDropLatency_Object((1,3,6,1,4,1,9,9,282,1,4,5),_FcNetworkDropLatency_Type())
fcNetworkDropLatency.setMaxAccess(_H)
if mibBuilder.loadTexts:fcNetworkDropLatency.setStatus(_B)
if mibBuilder.loadTexts:fcNetworkDropLatency.setUnits(_E)
class _FcSwitchDropLatency_Type(CiscoMilliSeconds):defaultValue=500;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_FcSwitchDropLatency_Type.__name__=_F
_FcSwitchDropLatency_Object=MibScalar
fcSwitchDropLatency=_FcSwitchDropLatency_Object((1,3,6,1,4,1,9,9,282,1,4,6),_FcSwitchDropLatency_Type())
fcSwitchDropLatency.setMaxAccess(_H)
if mibBuilder.loadTexts:fcSwitchDropLatency.setStatus(_B)
if mibBuilder.loadTexts:fcSwitchDropLatency.setUnits(_E)
class _FcInorderDelivery_Type(TruthValue):defaultValue=2
_FcInorderDelivery_Type.__name__=_U
_FcInorderDelivery_Object=MibScalar
fcInorderDelivery=_FcInorderDelivery_Object((1,3,6,1,4,1,9,9,282,1,4,7),_FcInorderDelivery_Type())
fcInorderDelivery.setMaxAccess(_H)
if mibBuilder.loadTexts:fcInorderDelivery.setStatus(_B)
_VsanFcTimerTable_Object=MibTable
vsanFcTimerTable=_VsanFcTimerTable_Object((1,3,6,1,4,1,9,9,282,1,4,8))
if mibBuilder.loadTexts:vsanFcTimerTable.setStatus(_B)
_VsanFcTimerEntry_Object=MibTableRow
vsanFcTimerEntry=_VsanFcTimerEntry_Object((1,3,6,1,4,1,9,9,282,1,4,8,1))
if mibBuilder.loadTexts:vsanFcTimerEntry.setStatus(_B)
class _VsanFcTimerForceFlag_Type(Bits):namedValues=NamedValues(*(('ratov',0),('edtov',1),('dstov',2)))
_VsanFcTimerForceFlag_Type.__name__='Bits'
_VsanFcTimerForceFlag_Object=MibTableColumn
vsanFcTimerForceFlag=_VsanFcTimerForceFlag_Object((1,3,6,1,4,1,9,9,282,1,4,8,1,1),_VsanFcTimerForceFlag_Type())
vsanFcTimerForceFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanFcTimerForceFlag.setStatus(_B)
class _VsanFcTimerRatov_Type(CiscoMilliSeconds):defaultValue=10000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,100000))
_VsanFcTimerRatov_Type.__name__=_F
_VsanFcTimerRatov_Object=MibTableColumn
vsanFcTimerRatov=_VsanFcTimerRatov_Object((1,3,6,1,4,1,9,9,282,1,4,8,1,2),_VsanFcTimerRatov_Type())
vsanFcTimerRatov.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanFcTimerRatov.setStatus(_B)
if mibBuilder.loadTexts:vsanFcTimerRatov.setUnits(_E)
class _VsanFcTimerEdtov_Type(CiscoMilliSeconds):defaultValue=2000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,100000))
_VsanFcTimerEdtov_Type.__name__=_F
_VsanFcTimerEdtov_Object=MibTableColumn
vsanFcTimerEdtov=_VsanFcTimerEdtov_Object((1,3,6,1,4,1,9,9,282,1,4,8,1,3),_VsanFcTimerEdtov_Type())
vsanFcTimerEdtov.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanFcTimerEdtov.setStatus(_B)
if mibBuilder.loadTexts:vsanFcTimerEdtov.setUnits(_E)
class _VsanFcTimerDstov_Type(CiscoMilliSeconds):defaultValue=5000;subtypeSpec=CiscoMilliSeconds.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5000,100000))
_VsanFcTimerDstov_Type.__name__=_F
_VsanFcTimerDstov_Object=MibTableColumn
vsanFcTimerDstov=_VsanFcTimerDstov_Object((1,3,6,1,4,1,9,9,282,1,4,8,1,4),_VsanFcTimerDstov_Type())
vsanFcTimerDstov.setMaxAccess(_C)
if mibBuilder.loadTexts:vsanFcTimerDstov.setStatus(_B)
if mibBuilder.loadTexts:vsanFcTimerDstov.setUnits(_E)
_VsanFcTimerFstov_Type=CiscoMilliSeconds
_VsanFcTimerFstov_Object=MibTableColumn
vsanFcTimerFstov=_VsanFcTimerFstov_Object((1,3,6,1,4,1,9,9,282,1,4,8,1,5),_VsanFcTimerFstov_Type())
vsanFcTimerFstov.setMaxAccess(_G)
if mibBuilder.loadTexts:vsanFcTimerFstov.setStatus(_B)
if mibBuilder.loadTexts:vsanFcTimerFstov.setUnits(_E)
_VsanStats_ObjectIdentity=ObjectIdentity
vsanStats=_VsanStats_ObjectIdentity((1,3,6,1,4,1,9,9,282,1,5))
_VsanFcFeElementName_Type=FcNameId
_VsanFcFeElementName_Object=MibScalar
vsanFcFeElementName=_VsanFcFeElementName_Object((1,3,6,1,4,1,9,9,282,1,5,1),_VsanFcFeElementName_Type())
vsanFcFeElementName.setMaxAccess(_H)
if mibBuilder.loadTexts:vsanFcFeElementName.setStatus(_B)
_VsanMIBConformance_ObjectIdentity=ObjectIdentity
vsanMIBConformance=_VsanMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,282,3))
_VsanMIBCompliances_ObjectIdentity=ObjectIdentity
vsanMIBCompliances=_VsanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,282,3,1))
_VsanMIBGroups_ObjectIdentity=ObjectIdentity
vsanMIBGroups=_VsanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,282,3,2))
vsanEntry.registerAugmentions((_A,_A7))
vsanFcTimerEntry.setIndexNames(*vsanEntry.getIndexNames())
vsanGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,1))
vsanGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_R),(_A,_a),(_A,_A8),(_A,_S),(_A,_b),(_A,_P),(_A,_c)))
if mibBuilder.loadTexts:vsanGroup.setStatus(_D)
vsanMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,3))
vsanMembershipGroup.setObjects((_A,_A9))
if mibBuilder.loadTexts:vsanMembershipGroup.setStatus(_B)
vsanStaticMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,4))
vsanStaticMembershipGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:vsanStaticMembershipGroup.setStatus(_B)
vsanWWNListGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,5))
vsanWWNListGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:vsanWWNListGroup.setStatus(_B)
vsanDynamicMembershipGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,6))
vsanDynamicMembershipGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:vsanDynamicMembershipGroup.setStatus(_B)
vsanFcTimerGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,8))
vsanFcTimerGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:vsanFcTimerGroup.setStatus(_D)
vsanFcLatencyGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,9))
vsanFcLatencyGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:vsanFcLatencyGroup.setStatus(_B)
vsanVsanMembershipSummaryGroup=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,10))
vsanVsanMembershipSummaryGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:vsanVsanMembershipSummaryGroup.setStatus(_B)
vsanGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,11))
vsanGroupRev1.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_R),(_A,_a),(_A,_S),(_A,_b),(_A,_d),(_A,_P),(_A,_c)))
if mibBuilder.loadTexts:vsanGroupRev1.setStatus(_D)
vsanFcTimerGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,12))
vsanFcTimerGroupRev1.setObjects(*((_A,_p),(_A,_q),(_A,_s),(_A,_r),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP)))
if mibBuilder.loadTexts:vsanFcTimerGroupRev1.setStatus(_B)
vsanGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,13))
vsanGroupRev2.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_R),(_A,_a),(_A,_S),(_A,_b),(_A,_d),(_A,_P),(_A,_c),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:vsanGroupRev2.setStatus(_D)
vsanMembershipSummaryGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,14))
vsanMembershipSummaryGroupRev1.setObjects((_A,_AQ))
if mibBuilder.loadTexts:vsanMembershipSummaryGroupRev1.setStatus(_B)
vsanGroupRev3=ObjectGroup((1,3,6,1,4,1,9,9,282,3,2,16))
vsanGroupRev3.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_R),(_A,_a),(_A,_S),(_A,_b),(_A,_d),(_A,_P),(_A,_c),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:vsanGroupRev3.setStatus(_B)
vsanStatusChange=NotificationType((1,3,6,1,4,1,9,9,282,1,3,0,1))
vsanStatusChange.setObjects(*((_A,_P),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:vsanStatusChange.setStatus(_B)
vsanPortMembershipChange=NotificationType((1,3,6,1,4,1,9,9,282,1,3,0,2))
vsanPortMembershipChange.setObjects(*((_A,_v),(_i,_j),(_A,_P)))
if mibBuilder.loadTexts:vsanPortMembershipChange.setStatus(_B)
vsanNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,282,3,2,7))
vsanNotificationGroup.setObjects((_A,_w))
if mibBuilder.loadTexts:vsanNotificationGroup.setStatus(_D)
vsanNotificationGroupRev1=NotificationGroup((1,3,6,1,4,1,9,9,282,3,2,15))
vsanNotificationGroupRev1.setObjects(*((_A,_w),(_A,_AR)))
if mibBuilder.loadTexts:vsanNotificationGroupRev1.setStatus(_B)
vsanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,1))
vsanMIBCompliance.setObjects(*((_A,_x),(_A,_I),(_A,_J),(_A,_Q),(_A,_e),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance.setStatus(_D)
vsanMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,2))
vsanMIBCompliance1.setObjects(*((_A,_x),(_A,_I),(_A,_J),(_A,_Q),(_A,_e),(_A,_K),(_A,_N),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance1.setStatus(_D)
vsanMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,3))
vsanMIBCompliance2.setObjects(*((_A,_y),(_A,_I),(_A,_J),(_A,_Q),(_A,_e),(_A,_K),(_A,_N),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance2.setStatus(_D)
vsanMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,4))
vsanMIBCompliance3.setObjects(*((_A,_y),(_A,_I),(_A,_J),(_A,_Q),(_A,_T),(_A,_K),(_A,_N),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance3.setStatus(_D)
vsanMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,5))
vsanMIBCompliance4.setObjects(*((_A,_f),(_A,_I),(_A,_J),(_A,_Q),(_A,_T),(_A,_K),(_A,_N),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance4.setStatus(_D)
vsanMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,6))
vsanMIBCompliance5.setObjects(*((_A,_f),(_A,_I),(_A,_J),(_A,_Q),(_A,_T),(_A,_K),(_A,_N),(_A,_g),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance5.setStatus(_D)
vsanMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,7))
vsanMIBCompliance6.setObjects(*((_A,_f),(_A,_I),(_A,_J),(_A,_z),(_A,_T),(_A,_K),(_A,_N),(_A,_g),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance6.setStatus(_D)
vsanMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,282,3,1,8))
vsanMIBCompliance7.setObjects(*((_A,_AS),(_A,_I),(_A,_J),(_A,_z),(_A,_T),(_A,_K),(_A,_N),(_A,_g),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:vsanMIBCompliance7.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_A3:VsanMediaType,_A4:VsanAdminState,'VsanOperationalState':VsanOperationalState,_A5:VsanLoadBalancingType,'ciscoVsanMIB':ciscoVsanMIB,'ciscoVsanMIBObjects':ciscoVsanMIBObjects,'vsanConfiguration':vsanConfiguration,_V:vsanNumber,_W:vsanLastChange,'vsanTable':vsanTable,'vsanEntry':vsanEntry,_l:vsanIndex,_X:vsanName,_Y:vsanMediaType,_R:vsanAdminState,_Z:vsanMtu,_a:vsanLoadBalancingType,_A8:vsanInterOperMode,_S:vsanOperState,_b:vsanRowStatus,_d:vsanInterOperValue,_t:vsanInorderDelivery,_u:vsanNetworkDropLatency,_P:notifyVsanIndex,'vsanMembership':vsanMembership,_A9:vsanDenyUnknownWwn,_AD:vsanWwnListNumber,'vsanWwnListTable':vsanWwnListTable,'vsanWwnListEntry':vsanWwnListEntry,_n:vsanWwnListIndex,_A6:vsanWwnListWwnIndex,_AE:vsanWwnListWwn,_AF:vsanWwnListRowStatus,_AA:vsanIfNumber,'vsanIfTable':vsanIfTable,'vsanIfEntry':vsanIfEntry,_AB:vsanIfVsan,_AC:vsanIfDenyList,_AG:vsanDynamicListNumber,'vsanDynamicTable':vsanDynamicTable,'vsanDynamicEntry':vsanDynamicEntry,_AH:vsanDynamicVsan,_AI:vsanDynamicRowStatus,'vsanMembershipSummaryTable':vsanMembershipSummaryTable,'vsanMembershipSummaryEntry':vsanMembershipSummaryEntry,_o:vsanMembershipSummaryInterface,_AQ:vsanMembershipSummaryIntfType,'vsanNotification':vsanNotification,'vsanNotifications':vsanNotifications,_w:vsanStatusChange,_AR:vsanPortMembershipChange,'vsanFcConfiguration':vsanFcConfiguration,_p:fcTimerRatov,_q:fcTimerEdtov,_r:fcTimerFstov,_s:fcTimerDstov,_AJ:fcNetworkDropLatency,_AK:fcSwitchDropLatency,_c:fcInorderDelivery,'vsanFcTimerTable':vsanFcTimerTable,_A7:vsanFcTimerEntry,_AL:vsanFcTimerForceFlag,_AM:vsanFcTimerRatov,_AN:vsanFcTimerEdtov,_AO:vsanFcTimerDstov,_AP:vsanFcTimerFstov,'vsanStats':vsanStats,_v:vsanFcFeElementName,'vsanMIBConformance':vsanMIBConformance,'vsanMIBCompliances':vsanMIBCompliances,'vsanMIBCompliance':vsanMIBCompliance,'vsanMIBCompliance1':vsanMIBCompliance1,'vsanMIBCompliance2':vsanMIBCompliance2,'vsanMIBCompliance3':vsanMIBCompliance3,'vsanMIBCompliance4':vsanMIBCompliance4,'vsanMIBCompliance5':vsanMIBCompliance5,'vsanMIBCompliance6':vsanMIBCompliance6,'vsanMIBCompliance7':vsanMIBCompliance7,'vsanMIBGroups':vsanMIBGroups,_x:vsanGroup,_I:vsanMembershipGroup,_J:vsanStaticMembershipGroup,_M:vsanWWNListGroup,_L:vsanDynamicMembershipGroup,_Q:vsanNotificationGroup,_e:vsanFcTimerGroup,_K:vsanFcLatencyGroup,_N:vsanVsanMembershipSummaryGroup,_y:vsanGroupRev1,_T:vsanFcTimerGroupRev1,_f:vsanGroupRev2,_g:vsanMembershipSummaryGroupRev1,_z:vsanNotificationGroupRev1,_AS:vsanGroupRev3})