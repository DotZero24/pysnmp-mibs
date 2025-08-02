_AL='vRtrIfBfdSessForwardInfoEntry'
_AK='vRtrIfQosEntry'
_AJ='vRtrIfStatsExtEntry'
_AI='vRtrIfExtEntry'
_AH='vRtrStatEntry'
_AG='rvConPathDown'
_AF='conPathDown'
_AE='fwdPlnRst'
_AD='nbSigSessDown'
_AC='echoFuncFail'
_AB='detTimeExp'
_AA='vRtrIfBfdSessExtRemAddr'
_A9='vRtrIfBfdSessExtRemAddrType'
_A8='vRtrIfBfdSessExtLclAddr'
_A7='vRtrIfBfdSessExtLclAddrType'
_A6='vRtrIfBfdSessExtRxInfoId'
_A5='vRtrIfBfdSessExtLinkType'
_A4='vRtrIfBfdExtAddressType'
_A3='destination'
_A2='vRtrIfGlobalIndex'
_A1='vRiaIndex'
_A0='vRtrIfName'
_z='TmnxVPNId'
_y='accessible-for-notify'
_x='regular'
_w='notApplicable'
_v='TmnxVPNRouteDistinguisher'
_u='TNamedItem'
_t='TItemLongDescription'
_s='TItemDescription'
_r='InterfaceIndexOrZero'
_q='OctetString'
_p='pathDown'
_o='init'
_n='down'
_m='isis'
_l='pim'
_k='TmnxEnabledDisabled'
_j='TmnxBgpAutonomousSystem'
_i='TmnxAdminState'
_h='TNetworkPolicyID'
_g='DisplayString'
_f='IpAddress'
_e='InetAutonomousSystemNumber'
_d='rsvp'
_c='ldp'
_b='bgp'
_a='TmnxServId'
_Z='InetAddressType'
_Y='adminDown'
_X='none'
_W='percent'
_V='TIPFilterID'
_U='vRtrIfIndex'
_T='unknown'
_S='Bits'
_R='TNamedItemOrEmpty'
_Q='not-accessible'
_P='vRtrID'
_O='InetAddress'
_N='read-write'
_M='obsolete'
_L='tnSysSwitchId'
_K='TROPIC-SYSTEM-MIB'
_J='milliseconds'
_I='seconds'
_H='TmnxStatus'
_G='TN-VRTR-MIB'
_F='Integer32'
_E='TruthValue'
_D='Unsigned32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_r)
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressPrefixLength',_Z,_e)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_S,'Counter32','Counter64','Gauge32',_F,_f,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_g,'MacAddress','PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp',_E)
TCpmProtPolicyID,TIPFilterID,TItemDescription,TItemLongDescription,TNamedItem,TNamedItemOrEmpty,TNetworkPolicyID,TmnxAdminState,TmnxBgpAutonomousSystem,TmnxCustId,TmnxEnabledDisabled,TmnxEncapVal,TmnxMplsTpGlobalID,TmnxMplsTpNodeID,TmnxOperState,TmnxPortID,TmnxServId,TmnxStatus,TmnxVPNRouteDistinguisher,TmnxVRtrID,TmnxVRtrIDOrZero=mibBuilder.importSymbols('TN-TC-MIB','TCpmProtPolicyID',_V,_s,_t,_u,_R,_h,_i,_j,'TmnxCustId',_k,'TmnxEncapVal','TmnxMplsTpGlobalID','TmnxMplsTpNodeID','TmnxOperState','TmnxPortID',_a,_H,_v,'TmnxVRtrID','TmnxVRtrIDOrZero')
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_K,_L)
tnVRtrMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,3))
if mibBuilder.loadTexts:tnVRtrMIBModule.setRevisions(('2015-09-14 00:00','2015-04-21 00:00','2015-04-06 00:00','2015-03-24 00:00','2015-03-02 00:00','2015-01-30 00:00','2011-02-01 00:00','2009-02-28 00:00','2008-07-01 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-02-28 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2000-08-14 00:00'))
class TmnxVPNId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
class TmnxInetAddrState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_T,0),('tentative',1),('duplicated',2),('inaccessible',3),('deprecated',4),('preferred',5)))
class TDSCPAppId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)));namedValues=NamedValues(*((_b,1),('cflowd',2),('dhcp',3),('dns',4),('ftp',5),('icmp',6),('igmp',7),('l2tp',8),(_c,9),('mld',10),('msdp',11),('ndis',12),('ntp',13),('ospf',14),(_l,15),('radius',16),('rip',17),(_d,18),('snmp',19),('snmp-notification',20),('srrp',21),('ssh',22),('syslog',23),('tacplus',24),('telnet',25),('tftp',26),('traceroute',27),('vrrp',28),('ptp',29),('igmp-reporter',30),('gtp',31)))
class TDot1pAppId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('arp',1),(_m,2),('pppoe',3)))
class TmnxVrtrSingleSfmOverloadState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_w,0),('normal',1),('overload',2)))
class TmnxInetCidrNextHopType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_x,1),('tunneled',2),('sixOverMPLS',3),('sixOverFour',4)))
class TmnxInetCidrNextHopOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_T,0),(_d,1),(_c,2),('ldpOverRsvp',3)))
class TmnxL3RouteOwner(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5,16)));namedValues=NamedValues(*((_T,0),('local',1),('host',2),('static',5),(_b,16)))
_TnVRtrObjs_ObjectIdentity=ObjectIdentity
tnVRtrObjs=_TnVRtrObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,3))
_VRtrConfTable_Object=MibTable
vRtrConfTable=_VRtrConfTable_Object((1,3,6,1,4,1,7483,6,1,2,3,1))
if mibBuilder.loadTexts:vRtrConfTable.setStatus(_A)
_VRtrConfEntry_Object=MibTableRow
vRtrConfEntry=_VRtrConfEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1))
vRtrConfEntry.setIndexNames((0,_K,_L),(0,_G,_P))
if mibBuilder.loadTexts:vRtrConfEntry.setStatus(_A)
_VRtrID_Type=TmnxVRtrID
_VRtrID_Object=MibTableColumn
vRtrID=_VRtrID_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,1),_VRtrID_Type())
vRtrID.setMaxAccess(_y)
if mibBuilder.loadTexts:vRtrID.setStatus(_A)
_VRtrRowStatus_Type=RowStatus
_VRtrRowStatus_Object=MibTableColumn
vRtrRowStatus=_VRtrRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,2),_VRtrRowStatus_Type())
vRtrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRowStatus.setStatus(_A)
class _VRtrAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrAdminState_Type.__name__=_i
_VRtrAdminState_Object=MibTableColumn
vRtrAdminState=_VRtrAdminState_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,3),_VRtrAdminState_Type())
vRtrAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrAdminState.setStatus(_A)
_VRtrName_Type=TNamedItemOrEmpty
_VRtrName_Object=MibTableColumn
vRtrName=_VRtrName_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,4),_VRtrName_Type())
vRtrName.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrName.setStatus(_A)
class _VRtrMaxNumRoutes_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_VRtrMaxNumRoutes_Type.__name__=_F
_VRtrMaxNumRoutes_Object=MibTableColumn
vRtrMaxNumRoutes=_VRtrMaxNumRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,5),_VRtrMaxNumRoutes_Type())
vRtrMaxNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMaxNumRoutes.setStatus(_A)
class _VRtrBgpStatus_Type(TmnxStatus):defaultValue=2
_VRtrBgpStatus_Type.__name__=_H
_VRtrBgpStatus_Object=MibTableColumn
vRtrBgpStatus=_VRtrBgpStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,6),_VRtrBgpStatus_Type())
vRtrBgpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBgpStatus.setStatus(_A)
class _VRtrMplsStatus_Type(TmnxStatus):defaultValue=2
_VRtrMplsStatus_Type.__name__=_H
_VRtrMplsStatus_Object=MibTableColumn
vRtrMplsStatus=_VRtrMplsStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,7),_VRtrMplsStatus_Type())
vRtrMplsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMplsStatus.setStatus(_A)
class _VRtrOspfStatus_Type(TmnxStatus):defaultValue=2
_VRtrOspfStatus_Type.__name__=_H
_VRtrOspfStatus_Object=MibTableColumn
vRtrOspfStatus=_VRtrOspfStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,8),_VRtrOspfStatus_Type())
vRtrOspfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOspfStatus.setStatus(_M)
class _VRtrRipStatus_Type(TmnxStatus):defaultValue=2
_VRtrRipStatus_Type.__name__=_H
_VRtrRipStatus_Object=MibTableColumn
vRtrRipStatus=_VRtrRipStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,9),_VRtrRipStatus_Type())
vRtrRipStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRipStatus.setStatus(_A)
class _VRtrRsvpStatus_Type(TmnxStatus):defaultValue=2
_VRtrRsvpStatus_Type.__name__=_H
_VRtrRsvpStatus_Object=MibTableColumn
vRtrRsvpStatus=_VRtrRsvpStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,10),_VRtrRsvpStatus_Type())
vRtrRsvpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRsvpStatus.setStatus(_A)
class _VRtrEcmpMaxRoutes_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_VRtrEcmpMaxRoutes_Type.__name__=_D
_VRtrEcmpMaxRoutes_Object=MibTableColumn
vRtrEcmpMaxRoutes=_VRtrEcmpMaxRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,11),_VRtrEcmpMaxRoutes_Type())
vRtrEcmpMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrEcmpMaxRoutes.setStatus(_A)
class _VRtrAS_Type(TmnxBgpAutonomousSystem):defaultValue=0
_VRtrAS_Type.__name__=_j
_VRtrAS_Object=MibTableColumn
vRtrAS=_VRtrAS_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,12),_VRtrAS_Type())
vRtrAS.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrAS.setStatus(_M)
_VRtrNewIfIndex_Type=TestAndIncr
_VRtrNewIfIndex_Object=MibTableColumn
vRtrNewIfIndex=_VRtrNewIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,13),_VRtrNewIfIndex_Type())
vRtrNewIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrNewIfIndex.setStatus(_A)
class _VRtrLdpStatus_Type(TmnxStatus):defaultValue=2
_VRtrLdpStatus_Type.__name__=_H
_VRtrLdpStatus_Object=MibTableColumn
vRtrLdpStatus=_VRtrLdpStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,14),_VRtrLdpStatus_Type())
vRtrLdpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrLdpStatus.setStatus(_A)
class _VRtrIsIsStatus_Type(TmnxStatus):defaultValue=2
_VRtrIsIsStatus_Type.__name__=_H
_VRtrIsIsStatus_Object=MibTableColumn
vRtrIsIsStatus=_VRtrIsIsStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,15),_VRtrIsIsStatus_Type())
vRtrIsIsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIsIsStatus.setStatus(_M)
_VRtrRouterId_Type=IpAddress
_VRtrRouterId_Object=MibTableColumn
vRtrRouterId=_VRtrRouterId_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,16),_VRtrRouterId_Type())
vRtrRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRouterId.setStatus(_A)
class _VRtrTriggeredPolicy_Type(TruthValue):defaultValue=2
_VRtrTriggeredPolicy_Type.__name__=_E
_VRtrTriggeredPolicy_Object=MibTableColumn
vRtrTriggeredPolicy=_VRtrTriggeredPolicy_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,17),_VRtrTriggeredPolicy_Type())
vRtrTriggeredPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrTriggeredPolicy.setStatus(_A)
class _VRtrConfederationAS_Type(TmnxBgpAutonomousSystem):defaultValue=0
_VRtrConfederationAS_Type.__name__=_j
_VRtrConfederationAS_Object=MibTableColumn
vRtrConfederationAS=_VRtrConfederationAS_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,18),_VRtrConfederationAS_Type())
vRtrConfederationAS.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrConfederationAS.setStatus(_M)
class _VRtrRouteDistinguisher_Type(TmnxVPNRouteDistinguisher):defaultHexValue='0000000000000000'
_VRtrRouteDistinguisher_Type.__name__=_v
_VRtrRouteDistinguisher_Object=MibTableColumn
vRtrRouteDistinguisher=_VRtrRouteDistinguisher_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,19),_VRtrRouteDistinguisher_Type())
vRtrRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRouteDistinguisher.setStatus(_A)
class _VRtrMidRouteThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VRtrMidRouteThreshold_Type.__name__=_D
_VRtrMidRouteThreshold_Object=MibTableColumn
vRtrMidRouteThreshold=_VRtrMidRouteThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,20),_VRtrMidRouteThreshold_Type())
vRtrMidRouteThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMidRouteThreshold.setStatus(_A)
if mibBuilder.loadTexts:vRtrMidRouteThreshold.setUnits(_W)
class _VRtrHighRouteThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VRtrHighRouteThreshold_Type.__name__=_D
_VRtrHighRouteThreshold_Object=MibTableColumn
vRtrHighRouteThreshold=_VRtrHighRouteThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,21),_VRtrHighRouteThreshold_Type())
vRtrHighRouteThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrHighRouteThreshold.setStatus(_A)
if mibBuilder.loadTexts:vRtrHighRouteThreshold.setUnits(_W)
class _VRtrIllegalLabelThreshold_Type(Unsigned32):defaultValue=0
_VRtrIllegalLabelThreshold_Type.__name__=_D
_VRtrIllegalLabelThreshold_Object=MibTableColumn
vRtrIllegalLabelThreshold=_VRtrIllegalLabelThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,22),_VRtrIllegalLabelThreshold_Type())
vRtrIllegalLabelThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIllegalLabelThreshold.setStatus(_A)
class _VRtrVpnId_Type(TmnxVPNId):defaultHexValue=''
_VRtrVpnId_Type.__name__=_z
_VRtrVpnId_Object=MibTableColumn
vRtrVpnId=_VRtrVpnId_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,23),_VRtrVpnId_Type())
vRtrVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrVpnId.setStatus(_A)
class _VRtrDescription_Type(TItemDescription):defaultHexValue=''
_VRtrDescription_Type.__name__=_s
_VRtrDescription_Object=MibTableColumn
vRtrDescription=_VRtrDescription_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,25),_VRtrDescription_Type())
vRtrDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrDescription.setStatus(_A)
class _VRtrGracefulRestart_Type(TruthValue):defaultValue=2
_VRtrGracefulRestart_Type.__name__=_E
_VRtrGracefulRestart_Object=MibTableColumn
vRtrGracefulRestart=_VRtrGracefulRestart_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,26),_VRtrGracefulRestart_Type())
vRtrGracefulRestart.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrGracefulRestart.setStatus(_A)
class _VRtrGracefulRestartType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('never',0),('manual',1),('automatic',2)))
_VRtrGracefulRestartType_Type.__name__=_F
_VRtrGracefulRestartType_Object=MibTableColumn
vRtrGracefulRestartType=_VRtrGracefulRestartType_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,27),_VRtrGracefulRestartType_Type())
vRtrGracefulRestartType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrGracefulRestartType.setStatus(_A)
class _VRtrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_T,0),('baseRouter',1),('vprn',2),('vr',3)))
_VRtrType_Type.__name__=_F
_VRtrType_Object=MibTableColumn
vRtrType=_VRtrType_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,28),_VRtrType_Type())
vRtrType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrType.setStatus(_A)
_VRtrServiceId_Type=TmnxServId
_VRtrServiceId_Object=MibTableColumn
vRtrServiceId=_VRtrServiceId_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,29),_VRtrServiceId_Type())
vRtrServiceId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrServiceId.setStatus(_A)
_VRtrCustId_Type=TmnxCustId
_VRtrCustId_Object=MibTableColumn
vRtrCustId=_VRtrCustId_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,30),_VRtrCustId_Type())
vRtrCustId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrCustId.setStatus(_A)
class _VRtrIgmpStatus_Type(TmnxStatus):defaultValue=2
_VRtrIgmpStatus_Type.__name__=_H
_VRtrIgmpStatus_Object=MibTableColumn
vRtrIgmpStatus=_VRtrIgmpStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,31),_VRtrIgmpStatus_Type())
vRtrIgmpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIgmpStatus.setStatus(_A)
class _VRtrMaxNumRoutesLogOnly_Type(TruthValue):defaultValue=2
_VRtrMaxNumRoutesLogOnly_Type.__name__=_E
_VRtrMaxNumRoutesLogOnly_Object=MibTableColumn
vRtrMaxNumRoutesLogOnly=_VRtrMaxNumRoutesLogOnly_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,32),_VRtrMaxNumRoutesLogOnly_Type())
vRtrMaxNumRoutesLogOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMaxNumRoutesLogOnly.setStatus(_A)
_VRtrVrfTarget_Type=TNamedItemOrEmpty
_VRtrVrfTarget_Object=MibTableColumn
vRtrVrfTarget=_VRtrVrfTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,33),_VRtrVrfTarget_Type())
vRtrVrfTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrVrfTarget.setStatus(_A)
_VRtrVrfExportTarget_Type=TNamedItemOrEmpty
_VRtrVrfExportTarget_Object=MibTableColumn
vRtrVrfExportTarget=_VRtrVrfExportTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,34),_VRtrVrfExportTarget_Type())
vRtrVrfExportTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrVrfExportTarget.setStatus(_A)
_VRtrVrfImportTarget_Type=TNamedItemOrEmpty
_VRtrVrfImportTarget_Object=MibTableColumn
vRtrVrfImportTarget=_VRtrVrfImportTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,35),_VRtrVrfImportTarget_Type())
vRtrVrfImportTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrVrfImportTarget.setStatus(_A)
class _VRtrPimStatus_Type(TmnxStatus):defaultValue=2
_VRtrPimStatus_Type.__name__=_H
_VRtrPimStatus_Object=MibTableColumn
vRtrPimStatus=_VRtrPimStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,36),_VRtrPimStatus_Type())
vRtrPimStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrPimStatus.setStatus(_A)
class _VRtrMaxMcastNumRoutes_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_VRtrMaxMcastNumRoutes_Type.__name__=_F
_VRtrMaxMcastNumRoutes_Object=MibTableColumn
vRtrMaxMcastNumRoutes=_VRtrMaxMcastNumRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,37),_VRtrMaxMcastNumRoutes_Type())
vRtrMaxMcastNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMaxMcastNumRoutes.setStatus(_A)
class _VRtrMaxMcastNumRoutesLogOnly_Type(TruthValue):defaultValue=2
_VRtrMaxMcastNumRoutesLogOnly_Type.__name__=_E
_VRtrMaxMcastNumRoutesLogOnly_Object=MibTableColumn
vRtrMaxMcastNumRoutesLogOnly=_VRtrMaxMcastNumRoutesLogOnly_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,38),_VRtrMaxMcastNumRoutesLogOnly_Type())
vRtrMaxMcastNumRoutesLogOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMaxMcastNumRoutesLogOnly.setStatus(_A)
class _VRtrMcastMidRouteThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VRtrMcastMidRouteThreshold_Type.__name__=_D
_VRtrMcastMidRouteThreshold_Object=MibTableColumn
vRtrMcastMidRouteThreshold=_VRtrMcastMidRouteThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,39),_VRtrMcastMidRouteThreshold_Type())
vRtrMcastMidRouteThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMcastMidRouteThreshold.setStatus(_A)
if mibBuilder.loadTexts:vRtrMcastMidRouteThreshold.setUnits(_W)
class _VRtrIgnoreIcmpRedirect_Type(TruthValue):defaultValue=1
_VRtrIgnoreIcmpRedirect_Type.__name__=_E
_VRtrIgnoreIcmpRedirect_Object=MibTableColumn
vRtrIgnoreIcmpRedirect=_VRtrIgnoreIcmpRedirect_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,40),_VRtrIgnoreIcmpRedirect_Type())
vRtrIgnoreIcmpRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIgnoreIcmpRedirect.setStatus(_A)
class _VRtrOspfv3Status_Type(TmnxStatus):defaultValue=2
_VRtrOspfv3Status_Type.__name__=_H
_VRtrOspfv3Status_Object=MibTableColumn
vRtrOspfv3Status=_VRtrOspfv3Status_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,41),_VRtrOspfv3Status_Type())
vRtrOspfv3Status.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOspfv3Status.setStatus(_M)
class _VRtrMsdpStatus_Type(TmnxStatus):defaultValue=2
_VRtrMsdpStatus_Type.__name__=_H
_VRtrMsdpStatus_Object=MibTableColumn
vRtrMsdpStatus=_VRtrMsdpStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,42),_VRtrMsdpStatus_Type())
vRtrMsdpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMsdpStatus.setStatus(_A)
class _VRtrVprnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_x,1),('hub',2),('spoke',3),('subscriberSplitHorizon',4)))
_VRtrVprnType_Type.__name__=_F
_VRtrVprnType_Object=MibTableColumn
vRtrVprnType=_VRtrVprnType_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,43),_VRtrVprnType_Type())
vRtrVprnType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrVprnType.setStatus(_A)
_VRtrSecondaryVrfId_Type=TmnxVRtrIDOrZero
_VRtrSecondaryVrfId_Object=MibTableColumn
vRtrSecondaryVrfId=_VRtrSecondaryVrfId_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,44),_VRtrSecondaryVrfId_Type())
vRtrSecondaryVrfId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrSecondaryVrfId.setStatus(_A)
class _VRtrMldStatus_Type(TmnxStatus):defaultValue=2
_VRtrMldStatus_Type.__name__=_H
_VRtrMldStatus_Object=MibTableColumn
vRtrMldStatus=_VRtrMldStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,45),_VRtrMldStatus_Type())
vRtrMldStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMldStatus.setStatus(_A)
class _VRtrIPv6MaxNumRoutes_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_VRtrIPv6MaxNumRoutes_Type.__name__=_F
_VRtrIPv6MaxNumRoutes_Object=MibTableColumn
vRtrIPv6MaxNumRoutes=_VRtrIPv6MaxNumRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,46),_VRtrIPv6MaxNumRoutes_Type())
vRtrIPv6MaxNumRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIPv6MaxNumRoutes.setStatus(_A)
class _VRtrIPv6MidRouteThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VRtrIPv6MidRouteThreshold_Type.__name__=_D
_VRtrIPv6MidRouteThreshold_Object=MibTableColumn
vRtrIPv6MidRouteThreshold=_VRtrIPv6MidRouteThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,47),_VRtrIPv6MidRouteThreshold_Type())
vRtrIPv6MidRouteThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIPv6MidRouteThreshold.setStatus(_A)
if mibBuilder.loadTexts:vRtrIPv6MidRouteThreshold.setUnits(_W)
class _VRtrIPv6HighRouteThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VRtrIPv6HighRouteThreshold_Type.__name__=_D
_VRtrIPv6HighRouteThreshold_Object=MibTableColumn
vRtrIPv6HighRouteThreshold=_VRtrIPv6HighRouteThreshold_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,48),_VRtrIPv6HighRouteThreshold_Type())
vRtrIPv6HighRouteThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIPv6HighRouteThreshold.setStatus(_A)
if mibBuilder.loadTexts:vRtrIPv6HighRouteThreshold.setUnits(_W)
class _VRtrIPv6MaxNumRoutesLogOnly_Type(TruthValue):defaultValue=2
_VRtrIPv6MaxNumRoutesLogOnly_Type.__name__=_E
_VRtrIPv6MaxNumRoutesLogOnly_Object=MibTableColumn
vRtrIPv6MaxNumRoutesLogOnly=_VRtrIPv6MaxNumRoutesLogOnly_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,49),_VRtrIPv6MaxNumRoutesLogOnly_Type())
vRtrIPv6MaxNumRoutesLogOnly.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIPv6MaxNumRoutesLogOnly.setStatus(_A)
class _VRtrIPv6IgnoreIcmpRedirect_Type(TruthValue):defaultValue=1
_VRtrIPv6IgnoreIcmpRedirect_Type.__name__=_E
_VRtrIPv6IgnoreIcmpRedirect_Object=MibTableColumn
vRtrIPv6IgnoreIcmpRedirect=_VRtrIPv6IgnoreIcmpRedirect_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,50),_VRtrIPv6IgnoreIcmpRedirect_Type())
vRtrIPv6IgnoreIcmpRedirect.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIPv6IgnoreIcmpRedirect.setStatus(_A)
class _VRtrMcPathMgmtPlcyName_Type(TNamedItem):defaultValue=OctetString('default')
_VRtrMcPathMgmtPlcyName_Type.__name__=_u
_VRtrMcPathMgmtPlcyName_Object=MibTableColumn
vRtrMcPathMgmtPlcyName=_VRtrMcPathMgmtPlcyName_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,51),_VRtrMcPathMgmtPlcyName_Type())
vRtrMcPathMgmtPlcyName.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMcPathMgmtPlcyName.setStatus(_A)
class _VRtrIgnoreNextHopMetric_Type(TruthValue):defaultValue=2
_VRtrIgnoreNextHopMetric_Type.__name__=_E
_VRtrIgnoreNextHopMetric_Object=MibTableColumn
vRtrIgnoreNextHopMetric=_VRtrIgnoreNextHopMetric_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,52),_VRtrIgnoreNextHopMetric_Type())
vRtrIgnoreNextHopMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIgnoreNextHopMetric.setStatus(_A)
class _VRtrMvpnVrfTarget_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrMvpnVrfTarget_Type.__name__=_R
_VRtrMvpnVrfTarget_Object=MibTableColumn
vRtrMvpnVrfTarget=_VRtrMvpnVrfTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,53),_VRtrMvpnVrfTarget_Type())
vRtrMvpnVrfTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfTarget.setStatus(_A)
class _VRtrMvpnVrfExportTarget_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrMvpnVrfExportTarget_Type.__name__=_R
_VRtrMvpnVrfExportTarget_Object=MibTableColumn
vRtrMvpnVrfExportTarget=_VRtrMvpnVrfExportTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,54),_VRtrMvpnVrfExportTarget_Type())
vRtrMvpnVrfExportTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfExportTarget.setStatus(_A)
class _VRtrMvpnVrfImportTarget_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrMvpnVrfImportTarget_Type.__name__=_R
_VRtrMvpnVrfImportTarget_Object=MibTableColumn
vRtrMvpnVrfImportTarget=_VRtrMvpnVrfImportTarget_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,55),_VRtrMvpnVrfImportTarget_Type())
vRtrMvpnVrfImportTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfImportTarget.setStatus(_A)
class _VRtrMvpnVrfTargetUnicast_Type(TruthValue):defaultValue=2
_VRtrMvpnVrfTargetUnicast_Type.__name__=_E
_VRtrMvpnVrfTargetUnicast_Object=MibTableColumn
vRtrMvpnVrfTargetUnicast=_VRtrMvpnVrfTargetUnicast_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,56),_VRtrMvpnVrfTargetUnicast_Type())
vRtrMvpnVrfTargetUnicast.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfTargetUnicast.setStatus(_A)
class _VRtrMvpnVrfExportTargetUnicast_Type(TruthValue):defaultValue=2
_VRtrMvpnVrfExportTargetUnicast_Type.__name__=_E
_VRtrMvpnVrfExportTargetUnicast_Object=MibTableColumn
vRtrMvpnVrfExportTargetUnicast=_VRtrMvpnVrfExportTargetUnicast_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,57),_VRtrMvpnVrfExportTargetUnicast_Type())
vRtrMvpnVrfExportTargetUnicast.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfExportTargetUnicast.setStatus(_A)
class _VRtrMvpnVrfImportTargetUnicast_Type(TruthValue):defaultValue=2
_VRtrMvpnVrfImportTargetUnicast_Type.__name__=_E
_VRtrMvpnVrfImportTargetUnicast_Object=MibTableColumn
vRtrMvpnVrfImportTargetUnicast=_VRtrMvpnVrfImportTargetUnicast_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,58),_VRtrMvpnVrfImportTargetUnicast_Type())
vRtrMvpnVrfImportTargetUnicast.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrMvpnVrfImportTargetUnicast.setStatus(_A)
class _VRtrAS4Byte_Type(InetAutonomousSystemNumber):defaultValue=0
_VRtrAS4Byte_Type.__name__=_e
_VRtrAS4Byte_Object=MibTableColumn
vRtrAS4Byte=_VRtrAS4Byte_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,59),_VRtrAS4Byte_Type())
vRtrAS4Byte.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrAS4Byte.setStatus(_A)
class _VRtrConfederationAS4Byte_Type(InetAutonomousSystemNumber):defaultValue=0
_VRtrConfederationAS4Byte_Type.__name__=_e
_VRtrConfederationAS4Byte_Object=MibTableColumn
vRtrConfederationAS4Byte=_VRtrConfederationAS4Byte_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,60),_VRtrConfederationAS4Byte_Type())
vRtrConfederationAS4Byte.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrConfederationAS4Byte.setStatus(_A)
class _VRtrMvpnCMcastImportRT_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrMvpnCMcastImportRT_Type.__name__=_R
_VRtrMvpnCMcastImportRT_Object=MibTableColumn
vRtrMvpnCMcastImportRT=_VRtrMvpnCMcastImportRT_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,61),_VRtrMvpnCMcastImportRT_Type())
vRtrMvpnCMcastImportRT.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMvpnCMcastImportRT.setStatus(_A)
_VRtrInterASMvpn_Type=TruthValue
_VRtrInterASMvpn_Object=MibTableColumn
vRtrInterASMvpn=_VRtrInterASMvpn_Object((1,3,6,1,4,1,7483,6,1,2,3,1,1,64),_VRtrInterASMvpn_Type())
vRtrInterASMvpn.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrInterASMvpn.setStatus(_A)
_VRtrStatTable_Object=MibTable
vRtrStatTable=_VRtrStatTable_Object((1,3,6,1,4,1,7483,6,1,2,3,2))
if mibBuilder.loadTexts:vRtrStatTable.setStatus(_A)
_VRtrStatEntry_Object=MibTableRow
vRtrStatEntry=_VRtrStatEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1))
if mibBuilder.loadTexts:vRtrStatEntry.setStatus(_A)
_VRtrOperState_Type=TmnxOperState
_VRtrOperState_Object=MibTableColumn
vRtrOperState=_VRtrOperState_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,1),_VRtrOperState_Type())
vRtrOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrOperState.setStatus(_A)
_VRtrDirectRoutes_Type=Gauge32
_VRtrDirectRoutes_Object=MibTableColumn
vRtrDirectRoutes=_VRtrDirectRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,2),_VRtrDirectRoutes_Type())
vRtrDirectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrDirectRoutes.setStatus(_A)
_VRtrDirectActiveRoutes_Type=Gauge32
_VRtrDirectActiveRoutes_Object=MibTableColumn
vRtrDirectActiveRoutes=_VRtrDirectActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,3),_VRtrDirectActiveRoutes_Type())
vRtrDirectActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrDirectActiveRoutes.setStatus(_A)
_VRtrStaticRoutes_Type=Gauge32
_VRtrStaticRoutes_Object=MibTableColumn
vRtrStaticRoutes=_VRtrStaticRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,4),_VRtrStaticRoutes_Type())
vRtrStaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStaticRoutes.setStatus(_A)
_VRtrStaticActiveRoutes_Type=Gauge32
_VRtrStaticActiveRoutes_Object=MibTableColumn
vRtrStaticActiveRoutes=_VRtrStaticActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,5),_VRtrStaticActiveRoutes_Type())
vRtrStaticActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStaticActiveRoutes.setStatus(_A)
_VRtrOSPFRoutes_Type=Gauge32
_VRtrOSPFRoutes_Object=MibTableColumn
vRtrOSPFRoutes=_VRtrOSPFRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,6),_VRtrOSPFRoutes_Type())
vRtrOSPFRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrOSPFRoutes.setStatus(_A)
_VRtrOSPFActiveRoutes_Type=Gauge32
_VRtrOSPFActiveRoutes_Object=MibTableColumn
vRtrOSPFActiveRoutes=_VRtrOSPFActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,7),_VRtrOSPFActiveRoutes_Type())
vRtrOSPFActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrOSPFActiveRoutes.setStatus(_A)
_VRtrBGPRoutes_Type=Gauge32
_VRtrBGPRoutes_Object=MibTableColumn
vRtrBGPRoutes=_VRtrBGPRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,8),_VRtrBGPRoutes_Type())
vRtrBGPRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrBGPRoutes.setStatus(_A)
_VRtrBGPActiveRoutes_Type=Gauge32
_VRtrBGPActiveRoutes_Object=MibTableColumn
vRtrBGPActiveRoutes=_VRtrBGPActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,9),_VRtrBGPActiveRoutes_Type())
vRtrBGPActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrBGPActiveRoutes.setStatus(_A)
_VRtrISISRoutes_Type=Gauge32
_VRtrISISRoutes_Object=MibTableColumn
vRtrISISRoutes=_VRtrISISRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,10),_VRtrISISRoutes_Type())
vRtrISISRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrISISRoutes.setStatus(_A)
_VRtrISISActiveRoutes_Type=Gauge32
_VRtrISISActiveRoutes_Object=MibTableColumn
vRtrISISActiveRoutes=_VRtrISISActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,11),_VRtrISISActiveRoutes_Type())
vRtrISISActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrISISActiveRoutes.setStatus(_A)
_VRtrRIPRoutes_Type=Gauge32
_VRtrRIPRoutes_Object=MibTableColumn
vRtrRIPRoutes=_VRtrRIPRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,12),_VRtrRIPRoutes_Type())
vRtrRIPRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrRIPRoutes.setStatus(_A)
_VRtrRIPActiveRoutes_Type=Gauge32
_VRtrRIPActiveRoutes_Object=MibTableColumn
vRtrRIPActiveRoutes=_VRtrRIPActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,13),_VRtrRIPActiveRoutes_Type())
vRtrRIPActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrRIPActiveRoutes.setStatus(_A)
_VRtrAggregateRoutes_Type=Gauge32
_VRtrAggregateRoutes_Object=MibTableColumn
vRtrAggregateRoutes=_VRtrAggregateRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,14),_VRtrAggregateRoutes_Type())
vRtrAggregateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrAggregateRoutes.setStatus(_A)
_VRtrAggregateActiveRoutes_Type=Gauge32
_VRtrAggregateActiveRoutes_Object=MibTableColumn
vRtrAggregateActiveRoutes=_VRtrAggregateActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,15),_VRtrAggregateActiveRoutes_Type())
vRtrAggregateActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrAggregateActiveRoutes.setStatus(_A)
_VRtrStatConfiguredIfs_Type=Gauge32
_VRtrStatConfiguredIfs_Object=MibTableColumn
vRtrStatConfiguredIfs=_VRtrStatConfiguredIfs_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,16),_VRtrStatConfiguredIfs_Type())
vRtrStatConfiguredIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatConfiguredIfs.setStatus(_A)
_VRtrStatActiveIfs_Type=Gauge32
_VRtrStatActiveIfs_Object=MibTableColumn
vRtrStatActiveIfs=_VRtrStatActiveIfs_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,17),_VRtrStatActiveIfs_Type())
vRtrStatActiveIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveIfs.setStatus(_A)
_VRtrStatIllegalLabels_Type=Counter32
_VRtrStatIllegalLabels_Object=MibTableColumn
vRtrStatIllegalLabels=_VRtrStatIllegalLabels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,18),_VRtrStatIllegalLabels_Type())
vRtrStatIllegalLabels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatIllegalLabels.setStatus(_A)
_VRtrStatCurrNumRoutes_Type=Gauge32
_VRtrStatCurrNumRoutes_Object=MibTableColumn
vRtrStatCurrNumRoutes=_VRtrStatCurrNumRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,19),_VRtrStatCurrNumRoutes_Type())
vRtrStatCurrNumRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatCurrNumRoutes.setStatus(_A)
_VRtrStatBGPVpnRoutes_Type=Gauge32
_VRtrStatBGPVpnRoutes_Object=MibTableColumn
vRtrStatBGPVpnRoutes=_VRtrStatBGPVpnRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,20),_VRtrStatBGPVpnRoutes_Type())
vRtrStatBGPVpnRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatBGPVpnRoutes.setStatus(_A)
_VRtrStatBGPVpnActiveRoutes_Type=Gauge32
_VRtrStatBGPVpnActiveRoutes_Object=MibTableColumn
vRtrStatBGPVpnActiveRoutes=_VRtrStatBGPVpnActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,21),_VRtrStatBGPVpnActiveRoutes_Type())
vRtrStatBGPVpnActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatBGPVpnActiveRoutes.setStatus(_A)
_VRtrStatTotalLdpTunnels_Type=Gauge32
_VRtrStatTotalLdpTunnels_Object=MibTableColumn
vRtrStatTotalLdpTunnels=_VRtrStatTotalLdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,22),_VRtrStatTotalLdpTunnels_Type())
vRtrStatTotalLdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalLdpTunnels.setStatus(_A)
_VRtrStatTotalSdpTunnels_Type=Gauge32
_VRtrStatTotalSdpTunnels_Object=MibTableColumn
vRtrStatTotalSdpTunnels=_VRtrStatTotalSdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,23),_VRtrStatTotalSdpTunnels_Type())
vRtrStatTotalSdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalSdpTunnels.setStatus(_A)
_VRtrStatActiveLdpTunnels_Type=Gauge32
_VRtrStatActiveLdpTunnels_Object=MibTableColumn
vRtrStatActiveLdpTunnels=_VRtrStatActiveLdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,24),_VRtrStatActiveLdpTunnels_Type())
vRtrStatActiveLdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveLdpTunnels.setStatus(_A)
_VRtrStatActiveSdpTunnels_Type=Gauge32
_VRtrStatActiveSdpTunnels_Object=MibTableColumn
vRtrStatActiveSdpTunnels=_VRtrStatActiveSdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,25),_VRtrStatActiveSdpTunnels_Type())
vRtrStatActiveSdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveSdpTunnels.setStatus(_A)
_VRtrMulticastRoutes_Type=Gauge32
_VRtrMulticastRoutes_Object=MibTableColumn
vRtrMulticastRoutes=_VRtrMulticastRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,26),_VRtrMulticastRoutes_Type())
vRtrMulticastRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMulticastRoutes.setStatus(_A)
_VRtrStatActiveARPEntries_Type=Gauge32
_VRtrStatActiveARPEntries_Object=MibTableColumn
vRtrStatActiveARPEntries=_VRtrStatActiveARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,27),_VRtrStatActiveARPEntries_Type())
vRtrStatActiveARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveARPEntries.setStatus(_A)
_VRtrStatTotalARPEntries_Type=Gauge32
_VRtrStatTotalARPEntries_Object=MibTableColumn
vRtrStatTotalARPEntries=_VRtrStatTotalARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,28),_VRtrStatTotalARPEntries_Type())
vRtrStatTotalARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalARPEntries.setStatus(_A)
_VRtrV6DirectRoutes_Type=Gauge32
_VRtrV6DirectRoutes_Object=MibTableColumn
vRtrV6DirectRoutes=_VRtrV6DirectRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,29),_VRtrV6DirectRoutes_Type())
vRtrV6DirectRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6DirectRoutes.setStatus(_A)
_VRtrV6DirectActiveRoutes_Type=Gauge32
_VRtrV6DirectActiveRoutes_Object=MibTableColumn
vRtrV6DirectActiveRoutes=_VRtrV6DirectActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,30),_VRtrV6DirectActiveRoutes_Type())
vRtrV6DirectActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6DirectActiveRoutes.setStatus(_A)
_VRtrV6StaticRoutes_Type=Gauge32
_VRtrV6StaticRoutes_Object=MibTableColumn
vRtrV6StaticRoutes=_VRtrV6StaticRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,31),_VRtrV6StaticRoutes_Type())
vRtrV6StaticRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StaticRoutes.setStatus(_A)
_VRtrV6StaticActiveRoutes_Type=Gauge32
_VRtrV6StaticActiveRoutes_Object=MibTableColumn
vRtrV6StaticActiveRoutes=_VRtrV6StaticActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,32),_VRtrV6StaticActiveRoutes_Type())
vRtrV6StaticActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StaticActiveRoutes.setStatus(_A)
_VRtrV6OSPFRoutes_Type=Gauge32
_VRtrV6OSPFRoutes_Object=MibTableColumn
vRtrV6OSPFRoutes=_VRtrV6OSPFRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,33),_VRtrV6OSPFRoutes_Type())
vRtrV6OSPFRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6OSPFRoutes.setStatus(_A)
_VRtrV6OSPFActiveRoutes_Type=Gauge32
_VRtrV6OSPFActiveRoutes_Object=MibTableColumn
vRtrV6OSPFActiveRoutes=_VRtrV6OSPFActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,34),_VRtrV6OSPFActiveRoutes_Type())
vRtrV6OSPFActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6OSPFActiveRoutes.setStatus(_A)
_VRtrV6BGPRoutes_Type=Gauge32
_VRtrV6BGPRoutes_Object=MibTableColumn
vRtrV6BGPRoutes=_VRtrV6BGPRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,35),_VRtrV6BGPRoutes_Type())
vRtrV6BGPRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6BGPRoutes.setStatus(_A)
_VRtrV6BGPActiveRoutes_Type=Gauge32
_VRtrV6BGPActiveRoutes_Object=MibTableColumn
vRtrV6BGPActiveRoutes=_VRtrV6BGPActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,36),_VRtrV6BGPActiveRoutes_Type())
vRtrV6BGPActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6BGPActiveRoutes.setStatus(_A)
_VRtrV6ISISRoutes_Type=Gauge32
_VRtrV6ISISRoutes_Object=MibTableColumn
vRtrV6ISISRoutes=_VRtrV6ISISRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,37),_VRtrV6ISISRoutes_Type())
vRtrV6ISISRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6ISISRoutes.setStatus(_A)
_VRtrV6ISISActiveRoutes_Type=Gauge32
_VRtrV6ISISActiveRoutes_Object=MibTableColumn
vRtrV6ISISActiveRoutes=_VRtrV6ISISActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,38),_VRtrV6ISISActiveRoutes_Type())
vRtrV6ISISActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6ISISActiveRoutes.setStatus(_A)
_VRtrV6RIPRoutes_Type=Gauge32
_VRtrV6RIPRoutes_Object=MibTableColumn
vRtrV6RIPRoutes=_VRtrV6RIPRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,39),_VRtrV6RIPRoutes_Type())
vRtrV6RIPRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6RIPRoutes.setStatus(_A)
_VRtrV6RIPActiveRoutes_Type=Gauge32
_VRtrV6RIPActiveRoutes_Object=MibTableColumn
vRtrV6RIPActiveRoutes=_VRtrV6RIPActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,40),_VRtrV6RIPActiveRoutes_Type())
vRtrV6RIPActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6RIPActiveRoutes.setStatus(_A)
_VRtrV6AggregateRoutes_Type=Gauge32
_VRtrV6AggregateRoutes_Object=MibTableColumn
vRtrV6AggregateRoutes=_VRtrV6AggregateRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,41),_VRtrV6AggregateRoutes_Type())
vRtrV6AggregateRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6AggregateRoutes.setStatus(_A)
_VRtrV6AggregateActiveRoutes_Type=Gauge32
_VRtrV6AggregateActiveRoutes_Object=MibTableColumn
vRtrV6AggregateActiveRoutes=_VRtrV6AggregateActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,42),_VRtrV6AggregateActiveRoutes_Type())
vRtrV6AggregateActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6AggregateActiveRoutes.setStatus(_A)
_VRtrV6StatConfiguredIfs_Type=Gauge32
_VRtrV6StatConfiguredIfs_Object=MibTableColumn
vRtrV6StatConfiguredIfs=_VRtrV6StatConfiguredIfs_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,43),_VRtrV6StatConfiguredIfs_Type())
vRtrV6StatConfiguredIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatConfiguredIfs.setStatus(_A)
_VRtrV6StatActiveIfs_Type=Gauge32
_VRtrV6StatActiveIfs_Object=MibTableColumn
vRtrV6StatActiveIfs=_VRtrV6StatActiveIfs_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,44),_VRtrV6StatActiveIfs_Type())
vRtrV6StatActiveIfs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatActiveIfs.setStatus(_A)
_VRtrV6StatIllegalLabels_Type=Counter32
_VRtrV6StatIllegalLabels_Object=MibTableColumn
vRtrV6StatIllegalLabels=_VRtrV6StatIllegalLabels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,45),_VRtrV6StatIllegalLabels_Type())
vRtrV6StatIllegalLabels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatIllegalLabels.setStatus(_A)
_VRtrV6StatCurrNumRoutes_Type=Gauge32
_VRtrV6StatCurrNumRoutes_Object=MibTableColumn
vRtrV6StatCurrNumRoutes=_VRtrV6StatCurrNumRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,46),_VRtrV6StatCurrNumRoutes_Type())
vRtrV6StatCurrNumRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatCurrNumRoutes.setStatus(_A)
_VRtrV6StatBGPVpnRoutes_Type=Gauge32
_VRtrV6StatBGPVpnRoutes_Object=MibTableColumn
vRtrV6StatBGPVpnRoutes=_VRtrV6StatBGPVpnRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,47),_VRtrV6StatBGPVpnRoutes_Type())
vRtrV6StatBGPVpnRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatBGPVpnRoutes.setStatus(_A)
_VRtrV6StatBGPVpnActiveRoutes_Type=Gauge32
_VRtrV6StatBGPVpnActiveRoutes_Object=MibTableColumn
vRtrV6StatBGPVpnActiveRoutes=_VRtrV6StatBGPVpnActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,48),_VRtrV6StatBGPVpnActiveRoutes_Type())
vRtrV6StatBGPVpnActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatBGPVpnActiveRoutes.setStatus(_A)
_VRtrV6StatTotalLdpTunnels_Type=Gauge32
_VRtrV6StatTotalLdpTunnels_Object=MibTableColumn
vRtrV6StatTotalLdpTunnels=_VRtrV6StatTotalLdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,49),_VRtrV6StatTotalLdpTunnels_Type())
vRtrV6StatTotalLdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatTotalLdpTunnels.setStatus(_A)
_VRtrV6StatTotalSdpTunnels_Type=Gauge32
_VRtrV6StatTotalSdpTunnels_Object=MibTableColumn
vRtrV6StatTotalSdpTunnels=_VRtrV6StatTotalSdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,50),_VRtrV6StatTotalSdpTunnels_Type())
vRtrV6StatTotalSdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatTotalSdpTunnels.setStatus(_A)
_VRtrV6StatActiveLdpTunnels_Type=Gauge32
_VRtrV6StatActiveLdpTunnels_Object=MibTableColumn
vRtrV6StatActiveLdpTunnels=_VRtrV6StatActiveLdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,51),_VRtrV6StatActiveLdpTunnels_Type())
vRtrV6StatActiveLdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatActiveLdpTunnels.setStatus(_A)
_VRtrV6StatActiveSdpTunnels_Type=Gauge32
_VRtrV6StatActiveSdpTunnels_Object=MibTableColumn
vRtrV6StatActiveSdpTunnels=_VRtrV6StatActiveSdpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,52),_VRtrV6StatActiveSdpTunnels_Type())
vRtrV6StatActiveSdpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatActiveSdpTunnels.setStatus(_A)
_VRtrV6MulticastRoutes_Type=Gauge32
_VRtrV6MulticastRoutes_Object=MibTableColumn
vRtrV6MulticastRoutes=_VRtrV6MulticastRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,53),_VRtrV6MulticastRoutes_Type())
vRtrV6MulticastRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6MulticastRoutes.setStatus(_A)
_VRtrV6StatActiveNbrEntries_Type=Gauge32
_VRtrV6StatActiveNbrEntries_Object=MibTableColumn
vRtrV6StatActiveNbrEntries=_VRtrV6StatActiveNbrEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,54),_VRtrV6StatActiveNbrEntries_Type())
vRtrV6StatActiveNbrEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatActiveNbrEntries.setStatus(_A)
_VRtrV6StatTotalNbrEntries_Type=Gauge32
_VRtrV6StatTotalNbrEntries_Object=MibTableColumn
vRtrV6StatTotalNbrEntries=_VRtrV6StatTotalNbrEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,55),_VRtrV6StatTotalNbrEntries_Type())
vRtrV6StatTotalNbrEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatTotalNbrEntries.setStatus(_A)
_VRtrSubMgmtRoutes_Type=Gauge32
_VRtrSubMgmtRoutes_Object=MibTableColumn
vRtrSubMgmtRoutes=_VRtrSubMgmtRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,56),_VRtrSubMgmtRoutes_Type())
vRtrSubMgmtRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrSubMgmtRoutes.setStatus(_A)
_VRtrSubMgmtActiveRoutes_Type=Gauge32
_VRtrSubMgmtActiveRoutes_Object=MibTableColumn
vRtrSubMgmtActiveRoutes=_VRtrSubMgmtActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,57),_VRtrSubMgmtActiveRoutes_Type())
vRtrSubMgmtActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrSubMgmtActiveRoutes.setStatus(_A)
_VRtrStatTotalRsvpTunnels_Type=Gauge32
_VRtrStatTotalRsvpTunnels_Object=MibTableColumn
vRtrStatTotalRsvpTunnels=_VRtrStatTotalRsvpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,58),_VRtrStatTotalRsvpTunnels_Type())
vRtrStatTotalRsvpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalRsvpTunnels.setStatus(_A)
_VRtrStatActiveRsvpTunnels_Type=Gauge32
_VRtrStatActiveRsvpTunnels_Object=MibTableColumn
vRtrStatActiveRsvpTunnels=_VRtrStatActiveRsvpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,59),_VRtrStatActiveRsvpTunnels_Type())
vRtrStatActiveRsvpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveRsvpTunnels.setStatus(_A)
_VRtrV6StatTotalRsvpTunnels_Type=Gauge32
_VRtrV6StatTotalRsvpTunnels_Object=MibTableColumn
vRtrV6StatTotalRsvpTunnels=_VRtrV6StatTotalRsvpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,60),_VRtrV6StatTotalRsvpTunnels_Type())
vRtrV6StatTotalRsvpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatTotalRsvpTunnels.setStatus(_A)
_VRtrV6StatActiveRsvpTunnels_Type=Gauge32
_VRtrV6StatActiveRsvpTunnels_Object=MibTableColumn
vRtrV6StatActiveRsvpTunnels=_VRtrV6StatActiveRsvpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,61),_VRtrV6StatActiveRsvpTunnels_Type())
vRtrV6StatActiveRsvpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6StatActiveRsvpTunnels.setStatus(_A)
_VRtrHostRoutes_Type=Gauge32
_VRtrHostRoutes_Object=MibTableColumn
vRtrHostRoutes=_VRtrHostRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,62),_VRtrHostRoutes_Type())
vRtrHostRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrHostRoutes.setStatus(_A)
_VRtrHostActiveRoutes_Type=Gauge32
_VRtrHostActiveRoutes_Object=MibTableColumn
vRtrHostActiveRoutes=_VRtrHostActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,63),_VRtrHostActiveRoutes_Type())
vRtrHostActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrHostActiveRoutes.setStatus(_A)
_VRtrV6HostRoutes_Type=Gauge32
_VRtrV6HostRoutes_Object=MibTableColumn
vRtrV6HostRoutes=_VRtrV6HostRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,64),_VRtrV6HostRoutes_Type())
vRtrV6HostRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6HostRoutes.setStatus(_A)
_VRtrV6HostActiveRoutes_Type=Gauge32
_VRtrV6HostActiveRoutes_Object=MibTableColumn
vRtrV6HostActiveRoutes=_VRtrV6HostActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,65),_VRtrV6HostActiveRoutes_Type())
vRtrV6HostActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6HostActiveRoutes.setStatus(_A)
_VRtrStatLocalARPEntries_Type=Gauge32
_VRtrStatLocalARPEntries_Object=MibTableColumn
vRtrStatLocalARPEntries=_VRtrStatLocalARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,66),_VRtrStatLocalARPEntries_Type())
vRtrStatLocalARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatLocalARPEntries.setStatus(_A)
_VRtrStatStaticARPEntries_Type=Gauge32
_VRtrStatStaticARPEntries_Object=MibTableColumn
vRtrStatStaticARPEntries=_VRtrStatStaticARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,67),_VRtrStatStaticARPEntries_Type())
vRtrStatStaticARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatStaticARPEntries.setStatus(_A)
_VRtrStatDynamicARPEntries_Type=Gauge32
_VRtrStatDynamicARPEntries_Object=MibTableColumn
vRtrStatDynamicARPEntries=_VRtrStatDynamicARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,68),_VRtrStatDynamicARPEntries_Type())
vRtrStatDynamicARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatDynamicARPEntries.setStatus(_A)
_VRtrStatManagedARPEntries_Type=Gauge32
_VRtrStatManagedARPEntries_Object=MibTableColumn
vRtrStatManagedARPEntries=_VRtrStatManagedARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,69),_VRtrStatManagedARPEntries_Type())
vRtrStatManagedARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatManagedARPEntries.setStatus(_A)
_VRtrStatInternalARPEntries_Type=Gauge32
_VRtrStatInternalARPEntries_Object=MibTableColumn
vRtrStatInternalARPEntries=_VRtrStatInternalARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,70),_VRtrStatInternalARPEntries_Type())
vRtrStatInternalARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatInternalARPEntries.setStatus(_A)
_VRtrManagedRoutes_Type=Gauge32
_VRtrManagedRoutes_Object=MibTableColumn
vRtrManagedRoutes=_VRtrManagedRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,71),_VRtrManagedRoutes_Type())
vRtrManagedRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrManagedRoutes.setStatus(_A)
_VRtrManagedActiveRoutes_Type=Gauge32
_VRtrManagedActiveRoutes_Object=MibTableColumn
vRtrManagedActiveRoutes=_VRtrManagedActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,72),_VRtrManagedActiveRoutes_Type())
vRtrManagedActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrManagedActiveRoutes.setStatus(_A)
_VRtrLDPRoutes_Type=Gauge32
_VRtrLDPRoutes_Object=MibTableColumn
vRtrLDPRoutes=_VRtrLDPRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,73),_VRtrLDPRoutes_Type())
vRtrLDPRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrLDPRoutes.setStatus(_A)
_VRtrLDPActiveRoutes_Type=Gauge32
_VRtrLDPActiveRoutes_Object=MibTableColumn
vRtrLDPActiveRoutes=_VRtrLDPActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,74),_VRtrLDPActiveRoutes_Type())
vRtrLDPActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrLDPActiveRoutes.setStatus(_A)
_VRtrVPNLeakRoutes_Type=Gauge32
_VRtrVPNLeakRoutes_Object=MibTableColumn
vRtrVPNLeakRoutes=_VRtrVPNLeakRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,75),_VRtrVPNLeakRoutes_Type())
vRtrVPNLeakRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrVPNLeakRoutes.setStatus(_A)
_VRtrVPNLeakActiveRoutes_Type=Gauge32
_VRtrVPNLeakActiveRoutes_Object=MibTableColumn
vRtrVPNLeakActiveRoutes=_VRtrVPNLeakActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,76),_VRtrVPNLeakActiveRoutes_Type())
vRtrVPNLeakActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrVPNLeakActiveRoutes.setStatus(_A)
_VRtrV6VPNLeakRoutes_Type=Gauge32
_VRtrV6VPNLeakRoutes_Object=MibTableColumn
vRtrV6VPNLeakRoutes=_VRtrV6VPNLeakRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,77),_VRtrV6VPNLeakRoutes_Type())
vRtrV6VPNLeakRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6VPNLeakRoutes.setStatus(_A)
_VRtrV6VPNLeakActiveRoutes_Type=Gauge32
_VRtrV6VPNLeakActiveRoutes_Object=MibTableColumn
vRtrV6VPNLeakActiveRoutes=_VRtrV6VPNLeakActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,78),_VRtrV6VPNLeakActiveRoutes_Type())
vRtrV6VPNLeakActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6VPNLeakActiveRoutes.setStatus(_A)
_VRtrV6SubMgmtRoutes_Type=Gauge32
_VRtrV6SubMgmtRoutes_Object=MibTableColumn
vRtrV6SubMgmtRoutes=_VRtrV6SubMgmtRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,79),_VRtrV6SubMgmtRoutes_Type())
vRtrV6SubMgmtRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6SubMgmtRoutes.setStatus(_A)
_VRtrV6SubMgmtActiveRoutes_Type=Gauge32
_VRtrV6SubMgmtActiveRoutes_Object=MibTableColumn
vRtrV6SubMgmtActiveRoutes=_VRtrV6SubMgmtActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,80),_VRtrV6SubMgmtActiveRoutes_Type())
vRtrV6SubMgmtActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6SubMgmtActiveRoutes.setStatus(_A)
_VRtrMobileHostRoutes_Type=Gauge32
_VRtrMobileHostRoutes_Object=MibTableColumn
vRtrMobileHostRoutes=_VRtrMobileHostRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,81),_VRtrMobileHostRoutes_Type())
vRtrMobileHostRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMobileHostRoutes.setStatus(_A)
_VRtrMobileHostActiveRoutes_Type=Gauge32
_VRtrMobileHostActiveRoutes_Object=MibTableColumn
vRtrMobileHostActiveRoutes=_VRtrMobileHostActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,82),_VRtrMobileHostActiveRoutes_Type())
vRtrMobileHostActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMobileHostActiveRoutes.setStatus(_A)
_VRtrV6MobileHostRoutes_Type=Gauge32
_VRtrV6MobileHostRoutes_Object=MibTableColumn
vRtrV6MobileHostRoutes=_VRtrV6MobileHostRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,83),_VRtrV6MobileHostRoutes_Type())
vRtrV6MobileHostRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6MobileHostRoutes.setStatus(_A)
_VRtrV6MobileHostActiveRoutes_Type=Gauge32
_VRtrV6MobileHostActiveRoutes_Object=MibTableColumn
vRtrV6MobileHostActiveRoutes=_VRtrV6MobileHostActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,84),_VRtrV6MobileHostActiveRoutes_Type())
vRtrV6MobileHostActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6MobileHostActiveRoutes.setStatus(_A)
_VRtrStatTotalBgpTunnels_Type=Gauge32
_VRtrStatTotalBgpTunnels_Object=MibTableColumn
vRtrStatTotalBgpTunnels=_VRtrStatTotalBgpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,85),_VRtrStatTotalBgpTunnels_Type())
vRtrStatTotalBgpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalBgpTunnels.setStatus(_A)
_VRtrStatActiveBgpTunnels_Type=Gauge32
_VRtrStatActiveBgpTunnels_Object=MibTableColumn
vRtrStatActiveBgpTunnels=_VRtrStatActiveBgpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,86),_VRtrStatActiveBgpTunnels_Type())
vRtrStatActiveBgpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveBgpTunnels.setStatus(_A)
_VRtrNatRoutes_Type=Gauge32
_VRtrNatRoutes_Object=MibTableColumn
vRtrNatRoutes=_VRtrNatRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,87),_VRtrNatRoutes_Type())
vRtrNatRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrNatRoutes.setStatus(_A)
_VRtrNatActiveRoutes_Type=Gauge32
_VRtrNatActiveRoutes_Object=MibTableColumn
vRtrNatActiveRoutes=_VRtrNatActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,88),_VRtrNatActiveRoutes_Type())
vRtrNatActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrNatActiveRoutes.setStatus(_A)
_VRtrV6NatRoutes_Type=Gauge32
_VRtrV6NatRoutes_Object=MibTableColumn
vRtrV6NatRoutes=_VRtrV6NatRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,89),_VRtrV6NatRoutes_Type())
vRtrV6NatRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6NatRoutes.setStatus(_A)
_VRtrV6NatActiveRoutes_Type=Gauge32
_VRtrV6NatActiveRoutes_Object=MibTableColumn
vRtrV6NatActiveRoutes=_VRtrV6NatActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,90),_VRtrV6NatActiveRoutes_Type())
vRtrV6NatActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6NatActiveRoutes.setStatus(_A)
_VRtrPeriodicRoutes_Type=Gauge32
_VRtrPeriodicRoutes_Object=MibTableColumn
vRtrPeriodicRoutes=_VRtrPeriodicRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,91),_VRtrPeriodicRoutes_Type())
vRtrPeriodicRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrPeriodicRoutes.setStatus(_A)
_VRtrPeriodicActiveRoutes_Type=Gauge32
_VRtrPeriodicActiveRoutes_Object=MibTableColumn
vRtrPeriodicActiveRoutes=_VRtrPeriodicActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,92),_VRtrPeriodicActiveRoutes_Type())
vRtrPeriodicActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrPeriodicActiveRoutes.setStatus(_A)
_VRtrV6PeriodicRoutes_Type=Gauge32
_VRtrV6PeriodicRoutes_Object=MibTableColumn
vRtrV6PeriodicRoutes=_VRtrV6PeriodicRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,93),_VRtrV6PeriodicRoutes_Type())
vRtrV6PeriodicRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6PeriodicRoutes.setStatus(_A)
_VRtrV6PeriodicActiveRoutes_Type=Gauge32
_VRtrV6PeriodicActiveRoutes_Object=MibTableColumn
vRtrV6PeriodicActiveRoutes=_VRtrV6PeriodicActiveRoutes_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,94),_VRtrV6PeriodicActiveRoutes_Type())
vRtrV6PeriodicActiveRoutes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrV6PeriodicActiveRoutes.setStatus(_A)
_VRtrStatTotalMplsTpTunnels_Type=Gauge32
_VRtrStatTotalMplsTpTunnels_Object=MibTableColumn
vRtrStatTotalMplsTpTunnels=_VRtrStatTotalMplsTpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,97),_VRtrStatTotalMplsTpTunnels_Type())
vRtrStatTotalMplsTpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatTotalMplsTpTunnels.setStatus(_A)
_VRtrStatActiveMplsTpTunnels_Type=Gauge32
_VRtrStatActiveMplsTpTunnels_Object=MibTableColumn
vRtrStatActiveMplsTpTunnels=_VRtrStatActiveMplsTpTunnels_Object((1,3,6,1,4,1,7483,6,1,2,3,2,1,98),_VRtrStatActiveMplsTpTunnels_Type())
vRtrStatActiveMplsTpTunnels.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrStatActiveMplsTpTunnels.setStatus(_A)
class _VRtrIfTotalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrIfTotalNumber_Type.__name__=_F
_VRtrIfTotalNumber_Object=MibScalar
vRtrIfTotalNumber=_VRtrIfTotalNumber_Object((1,3,6,1,4,1,7483,6,1,2,3,3),_VRtrIfTotalNumber_Type())
vRtrIfTotalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTotalNumber.setStatus(_A)
_VRtrIfTable_Object=MibTable
vRtrIfTable=_VRtrIfTable_Object((1,3,6,1,4,1,7483,6,1,2,3,4))
if mibBuilder.loadTexts:vRtrIfTable.setStatus(_A)
_VRtrIfEntry_Object=MibTableRow
vRtrIfEntry=_VRtrIfEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1))
vRtrIfEntry.setIndexNames((0,_K,_L),(0,_G,_P),(0,_G,_U))
if mibBuilder.loadTexts:vRtrIfEntry.setStatus(_A)
_VRtrIfIndex_Type=InterfaceIndex
_VRtrIfIndex_Object=MibTableColumn
vRtrIfIndex=_VRtrIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,1),_VRtrIfIndex_Type())
vRtrIfIndex.setMaxAccess(_y)
if mibBuilder.loadTexts:vRtrIfIndex.setStatus(_A)
_VRtrIfRowStatus_Type=RowStatus
_VRtrIfRowStatus_Object=MibTableColumn
vRtrIfRowStatus=_VRtrIfRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,2),_VRtrIfRowStatus_Type())
vRtrIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfRowStatus.setStatus(_A)
class _VRtrIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*(('network',1),('service',2),('serviceIes',3),('serviceRtdVpls',4),('serviceVprn',5),('serviceIesSubscriber',6),('serviceIesGroup',7),('serviceVprnSubscriber',8),('serviceVprnGroup',9),('serviceIesRedundant',10),('serviceVprnRedundant',11),('serviceVpls',12),('serviceIesCem',13),('serviceVprnCem',14),('serviceVprnIPsec',15),('serviceVprnIPMirror',16),('serviceVideo',17),('serviceVplsVideo',18),('multiHomingPrimary',19),('multiHomingSecondary',20),('serviceIesTunnel',21),('serviceIpReas',22),('networkIpReas',23),('networkVprn',24),('tmsService',25),('serviceIesAarp',26),('serviceVprnAarp',27),('serviceIesAa',28),('serviceVprnAa',29),('unnumMplsTp',30)))
_VRtrIfType_Type.__name__=_F
_VRtrIfType_Object=MibTableColumn
vRtrIfType=_VRtrIfType_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,3),_VRtrIfType_Type())
vRtrIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfType.setStatus(_A)
_VRtrIfName_Type=TNamedItem
_VRtrIfName_Object=MibTableColumn
vRtrIfName=_VRtrIfName_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,4),_VRtrIfName_Type())
vRtrIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfName.setStatus(_A)
class _VRtrIfPortID_Type(InterfaceIndexOrZero):defaultValue=0
_VRtrIfPortID_Type.__name__=_r
_VRtrIfPortID_Object=MibTableColumn
vRtrIfPortID=_VRtrIfPortID_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,5),_VRtrIfPortID_Type())
vRtrIfPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfPortID.setStatus(_A)
class _VRtrIfChannelID_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_VRtrIfChannelID_Type.__name__=_D
_VRtrIfChannelID_Object=MibTableColumn
vRtrIfChannelID=_VRtrIfChannelID_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,6),_VRtrIfChannelID_Type())
vRtrIfChannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfChannelID.setStatus(_M)
_VRtrIfEncapValue_Type=TmnxEncapVal
_VRtrIfEncapValue_Object=MibTableColumn
vRtrIfEncapValue=_VRtrIfEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,7),_VRtrIfEncapValue_Type())
vRtrIfEncapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfEncapValue.setStatus(_A)
class _VRtrIfAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrIfAdminState_Type.__name__=_i
_VRtrIfAdminState_Object=MibTableColumn
vRtrIfAdminState=_VRtrIfAdminState_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,8),_VRtrIfAdminState_Type())
vRtrIfAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfAdminState.setStatus(_A)
_VRtrIfOperState_Type=TmnxOperState
_VRtrIfOperState_Object=MibTableColumn
vRtrIfOperState=_VRtrIfOperState_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,9),_VRtrIfOperState_Type())
vRtrIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfOperState.setStatus(_A)
class _VRtrIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VRtrIfAlias_Type.__name__=_g
_VRtrIfAlias_Object=MibTableColumn
vRtrIfAlias=_VRtrIfAlias_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,10),_VRtrIfAlias_Type())
vRtrIfAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfAlias.setStatus(_A)
_VRtrIfPhysicalAddress_Type=MacAddress
_VRtrIfPhysicalAddress_Object=MibTableColumn
vRtrIfPhysicalAddress=_VRtrIfPhysicalAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,11),_VRtrIfPhysicalAddress_Type())
vRtrIfPhysicalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfPhysicalAddress.setStatus(_A)
class _VRtrIfArpTimeout_Type(Unsigned32):defaultValue=14400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrIfArpTimeout_Type.__name__=_D
_VRtrIfArpTimeout_Object=MibTableColumn
vRtrIfArpTimeout=_VRtrIfArpTimeout_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,12),_VRtrIfArpTimeout_Type())
vRtrIfArpTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfArpTimeout.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfArpTimeout.setUnits(_I)
class _VRtrIfIcmpMaskReply_Type(TruthValue):defaultValue=1
_VRtrIfIcmpMaskReply_Type.__name__=_E
_VRtrIfIcmpMaskReply_Object=MibTableColumn
vRtrIfIcmpMaskReply=_VRtrIfIcmpMaskReply_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,13),_VRtrIfIcmpMaskReply_Type())
vRtrIfIcmpMaskReply.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpMaskReply.setStatus(_A)
class _VRtrIfIcmpRedirects_Type(TruthValue):defaultValue=1
_VRtrIfIcmpRedirects_Type.__name__=_E
_VRtrIfIcmpRedirects_Object=MibTableColumn
vRtrIfIcmpRedirects=_VRtrIfIcmpRedirects_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,14),_VRtrIfIcmpRedirects_Type())
vRtrIfIcmpRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpRedirects.setStatus(_A)
class _VRtrIfIcmpNumRedirects_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpNumRedirects_Type.__name__=_D
_VRtrIfIcmpNumRedirects_Object=MibTableColumn
vRtrIfIcmpNumRedirects=_VRtrIfIcmpNumRedirects_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,15),_VRtrIfIcmpNumRedirects_Type())
vRtrIfIcmpNumRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpNumRedirects.setStatus(_A)
class _VRtrIfIcmpRedirectsTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpRedirectsTime_Type.__name__=_D
_VRtrIfIcmpRedirectsTime_Object=MibTableColumn
vRtrIfIcmpRedirectsTime=_VRtrIfIcmpRedirectsTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,16),_VRtrIfIcmpRedirectsTime_Type())
vRtrIfIcmpRedirectsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpRedirectsTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpRedirectsTime.setUnits(_I)
class _VRtrIfIcmpUnreachables_Type(TruthValue):defaultValue=1
_VRtrIfIcmpUnreachables_Type.__name__=_E
_VRtrIfIcmpUnreachables_Object=MibTableColumn
vRtrIfIcmpUnreachables=_VRtrIfIcmpUnreachables_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,17),_VRtrIfIcmpUnreachables_Type())
vRtrIfIcmpUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpUnreachables.setStatus(_A)
class _VRtrIfIcmpNumUnreachables_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpNumUnreachables_Type.__name__=_D
_VRtrIfIcmpNumUnreachables_Object=MibTableColumn
vRtrIfIcmpNumUnreachables=_VRtrIfIcmpNumUnreachables_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,18),_VRtrIfIcmpNumUnreachables_Type())
vRtrIfIcmpNumUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpNumUnreachables.setStatus(_A)
class _VRtrIfIcmpUnreachablesTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpUnreachablesTime_Type.__name__=_D
_VRtrIfIcmpUnreachablesTime_Object=MibTableColumn
vRtrIfIcmpUnreachablesTime=_VRtrIfIcmpUnreachablesTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,19),_VRtrIfIcmpUnreachablesTime_Type())
vRtrIfIcmpUnreachablesTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpUnreachablesTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpUnreachablesTime.setUnits(_I)
class _VRtrIfIcmpTtlExpired_Type(TruthValue):defaultValue=1
_VRtrIfIcmpTtlExpired_Type.__name__=_E
_VRtrIfIcmpTtlExpired_Object=MibTableColumn
vRtrIfIcmpTtlExpired=_VRtrIfIcmpTtlExpired_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,20),_VRtrIfIcmpTtlExpired_Type())
vRtrIfIcmpTtlExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpTtlExpired.setStatus(_A)
class _VRtrIfIcmpNumTtlExpired_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpNumTtlExpired_Type.__name__=_D
_VRtrIfIcmpNumTtlExpired_Object=MibTableColumn
vRtrIfIcmpNumTtlExpired=_VRtrIfIcmpNumTtlExpired_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,21),_VRtrIfIcmpNumTtlExpired_Type())
vRtrIfIcmpNumTtlExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpNumTtlExpired.setStatus(_A)
class _VRtrIfIcmpTtlExpiredTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpTtlExpiredTime_Type.__name__=_D
_VRtrIfIcmpTtlExpiredTime_Object=MibTableColumn
vRtrIfIcmpTtlExpiredTime=_VRtrIfIcmpTtlExpiredTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,22),_VRtrIfIcmpTtlExpiredTime_Type())
vRtrIfIcmpTtlExpiredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpTtlExpiredTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpTtlExpiredTime.setUnits(_I)
class _VRtrIfNtpBroadcast_Type(TruthValue):defaultValue=2
_VRtrIfNtpBroadcast_Type.__name__=_E
_VRtrIfNtpBroadcast_Object=MibTableColumn
vRtrIfNtpBroadcast=_VRtrIfNtpBroadcast_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,23),_VRtrIfNtpBroadcast_Type())
vRtrIfNtpBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfNtpBroadcast.setStatus(_A)
class _VRtrIfUnnumbered_Type(IpAddress):defaultHexValue='00000000'
_VRtrIfUnnumbered_Type.__name__=_f
_VRtrIfUnnumbered_Object=MibTableColumn
vRtrIfUnnumbered=_VRtrIfUnnumbered_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,24),_VRtrIfUnnumbered_Type())
vRtrIfUnnumbered.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfUnnumbered.setStatus(_A)
class _VRtrIfMtu_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(512,9000))
_VRtrIfMtu_Type.__name__=_D
_VRtrIfMtu_Object=MibTableColumn
vRtrIfMtu=_VRtrIfMtu_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,25),_VRtrIfMtu_Type())
vRtrIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfMtu.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfMtu.setUnits('bytes')
class _VRtrIfQosPolicyId_Type(TNetworkPolicyID):defaultValue=1
_VRtrIfQosPolicyId_Type.__name__=_h
_VRtrIfQosPolicyId_Object=MibTableColumn
vRtrIfQosPolicyId=_VRtrIfQosPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,26),_VRtrIfQosPolicyId_Type())
vRtrIfQosPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfQosPolicyId.setStatus(_M)
class _VRtrIfIngressFilterId_Type(TIPFilterID):defaultValue=0
_VRtrIfIngressFilterId_Type.__name__=_V
_VRtrIfIngressFilterId_Object=MibTableColumn
vRtrIfIngressFilterId=_VRtrIfIngressFilterId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,27),_VRtrIfIngressFilterId_Type())
vRtrIfIngressFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIngressFilterId.setStatus(_A)
class _VRtrIfEgressFilterId_Type(TIPFilterID):defaultValue=0
_VRtrIfEgressFilterId_Type.__name__=_V
_VRtrIfEgressFilterId_Object=MibTableColumn
vRtrIfEgressFilterId=_VRtrIfEgressFilterId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,28),_VRtrIfEgressFilterId_Type())
vRtrIfEgressFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfEgressFilterId.setStatus(_A)
class _VRtrIfDirectedBroadcast_Type(TruthValue):defaultValue=2
_VRtrIfDirectedBroadcast_Type.__name__=_E
_VRtrIfDirectedBroadcast_Object=MibTableColumn
vRtrIfDirectedBroadcast=_VRtrIfDirectedBroadcast_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,29),_VRtrIfDirectedBroadcast_Type())
vRtrIfDirectedBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfDirectedBroadcast.setStatus(_A)
class _VRtrIfMplsStatus_Type(TmnxStatus):defaultValue=2
_VRtrIfMplsStatus_Type.__name__=_H
_VRtrIfMplsStatus_Object=MibTableColumn
vRtrIfMplsStatus=_VRtrIfMplsStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,30),_VRtrIfMplsStatus_Type())
vRtrIfMplsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfMplsStatus.setStatus(_A)
class _VRtrIfUnnumberedIf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_VRtrIfUnnumberedIf_Type.__name__=_g
_VRtrIfUnnumberedIf_Object=MibTableColumn
vRtrIfUnnumberedIf=_VRtrIfUnnumberedIf_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,31),_VRtrIfUnnumberedIf_Type())
vRtrIfUnnumberedIf.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfUnnumberedIf.setStatus(_A)
class _VRtrIfCflowd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_X,1),('aclIngressOnly',2),('interfaceIngressOnly',3),('aclEgressOnly',4),('interfaceEgressOnly',5),('aclIngressEgress',6),('interfaceIngressEgress',7)))
_VRtrIfCflowd_Type.__name__=_F
_VRtrIfCflowd_Object=MibTableColumn
vRtrIfCflowd=_VRtrIfCflowd_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,32),_VRtrIfCflowd_Type())
vRtrIfCflowd.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfCflowd.setStatus(_A)
class _VRtrIfVPNClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_T,0),('carrierOfCarrier',1),('enterprise',2),('interProvider',3)))
_VRtrIfVPNClass_Type.__name__=_F
_VRtrIfVPNClass_Object=MibTableColumn
vRtrIfVPNClass=_VRtrIfVPNClass_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,33),_VRtrIfVPNClass_Type())
vRtrIfVPNClass.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfVPNClass.setStatus(_A)
class _VRtrIfDescription_Type(TItemLongDescription):defaultHexValue=''
_VRtrIfDescription_Type.__name__=_t
_VRtrIfDescription_Object=MibTableColumn
vRtrIfDescription=_VRtrIfDescription_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,34),_VRtrIfDescription_Type())
vRtrIfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfDescription.setStatus(_A)
class _VRtrIfProtocol_Type(Bits):namedValues=NamedValues(*(('ospfv2',0),('rip',1),(_m,2),(_b,3),('mpls',4),(_d,5),(_c,6),('igmp',7),(_l,8),('ospf3',9),('mld',10)))
_VRtrIfProtocol_Type.__name__=_S
_VRtrIfProtocol_Object=MibTableColumn
vRtrIfProtocol=_VRtrIfProtocol_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,35),_VRtrIfProtocol_Type())
vRtrIfProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfProtocol.setStatus(_A)
class _VRtrIfTosMarkingTrusted_Type(TruthValue):defaultValue=1
_VRtrIfTosMarkingTrusted_Type.__name__=_E
_VRtrIfTosMarkingTrusted_Object=MibTableColumn
vRtrIfTosMarkingTrusted=_VRtrIfTosMarkingTrusted_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,36),_VRtrIfTosMarkingTrusted_Type())
vRtrIfTosMarkingTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfTosMarkingTrusted.setStatus(_A)
class _VRtrIfServiceId_Type(TmnxServId):defaultValue=0
_VRtrIfServiceId_Type.__name__=_a
_VRtrIfServiceId_Object=MibTableColumn
vRtrIfServiceId=_VRtrIfServiceId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,37),_VRtrIfServiceId_Type())
vRtrIfServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfServiceId.setStatus(_A)
class _VRtrIfArpPopulate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_VRtrIfArpPopulate_Type.__name__=_F
_VRtrIfArpPopulate_Object=MibTableColumn
vRtrIfArpPopulate=_VRtrIfArpPopulate_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,38),_VRtrIfArpPopulate_Type())
vRtrIfArpPopulate.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfArpPopulate.setStatus(_A)
class _VRtrIfIPv6ConfigAllowed_Type(TruthValue):defaultValue=2
_VRtrIfIPv6ConfigAllowed_Type.__name__=_E
_VRtrIfIPv6ConfigAllowed_Object=MibTableColumn
vRtrIfIPv6ConfigAllowed=_VRtrIfIPv6ConfigAllowed_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,39),_VRtrIfIPv6ConfigAllowed_Type())
vRtrIfIPv6ConfigAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIPv6ConfigAllowed.setStatus(_A)
_VRtrIfIPv6OperState_Type=TmnxOperState
_VRtrIfIPv6OperState_Object=MibTableColumn
vRtrIfIPv6OperState=_VRtrIfIPv6OperState_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,40),_VRtrIfIPv6OperState_Type())
vRtrIfIPv6OperState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIPv6OperState.setStatus(_A)
class _VRtrIfIPv6IngressFilterId_Type(TIPFilterID):defaultValue=0
_VRtrIfIPv6IngressFilterId_Type.__name__=_V
_VRtrIfIPv6IngressFilterId_Object=MibTableColumn
vRtrIfIPv6IngressFilterId=_VRtrIfIPv6IngressFilterId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,41),_VRtrIfIPv6IngressFilterId_Type())
vRtrIfIPv6IngressFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIPv6IngressFilterId.setStatus(_A)
class _VRtrIfIPv6EgressFilterId_Type(TIPFilterID):defaultValue=0
_VRtrIfIPv6EgressFilterId_Type.__name__=_V
_VRtrIfIPv6EgressFilterId_Object=MibTableColumn
vRtrIfIPv6EgressFilterId=_VRtrIfIPv6EgressFilterId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,42),_VRtrIfIPv6EgressFilterId_Type())
vRtrIfIPv6EgressFilterId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIPv6EgressFilterId.setStatus(_A)
class _VRtrIfIcmpV6Redirects_Type(TruthValue):defaultValue=1
_VRtrIfIcmpV6Redirects_Type.__name__=_E
_VRtrIfIcmpV6Redirects_Object=MibTableColumn
vRtrIfIcmpV6Redirects=_VRtrIfIcmpV6Redirects_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,43),_VRtrIfIcmpV6Redirects_Type())
vRtrIfIcmpV6Redirects.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6Redirects.setStatus(_A)
class _VRtrIfIcmpV6NumRedirects_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpV6NumRedirects_Type.__name__=_D
_VRtrIfIcmpV6NumRedirects_Object=MibTableColumn
vRtrIfIcmpV6NumRedirects=_VRtrIfIcmpV6NumRedirects_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,44),_VRtrIfIcmpV6NumRedirects_Type())
vRtrIfIcmpV6NumRedirects.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6NumRedirects.setStatus(_A)
class _VRtrIfIcmpV6RedirectsTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpV6RedirectsTime_Type.__name__=_D
_VRtrIfIcmpV6RedirectsTime_Object=MibTableColumn
vRtrIfIcmpV6RedirectsTime=_VRtrIfIcmpV6RedirectsTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,45),_VRtrIfIcmpV6RedirectsTime_Type())
vRtrIfIcmpV6RedirectsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6RedirectsTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpV6RedirectsTime.setUnits(_I)
class _VRtrIfIcmpV6Unreachables_Type(TruthValue):defaultValue=1
_VRtrIfIcmpV6Unreachables_Type.__name__=_E
_VRtrIfIcmpV6Unreachables_Object=MibTableColumn
vRtrIfIcmpV6Unreachables=_VRtrIfIcmpV6Unreachables_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,46),_VRtrIfIcmpV6Unreachables_Type())
vRtrIfIcmpV6Unreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6Unreachables.setStatus(_A)
class _VRtrIfIcmpV6NumUnreachables_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpV6NumUnreachables_Type.__name__=_D
_VRtrIfIcmpV6NumUnreachables_Object=MibTableColumn
vRtrIfIcmpV6NumUnreachables=_VRtrIfIcmpV6NumUnreachables_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,47),_VRtrIfIcmpV6NumUnreachables_Type())
vRtrIfIcmpV6NumUnreachables.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6NumUnreachables.setStatus(_A)
class _VRtrIfIcmpV6UnreachablesTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpV6UnreachablesTime_Type.__name__=_D
_VRtrIfIcmpV6UnreachablesTime_Object=MibTableColumn
vRtrIfIcmpV6UnreachablesTime=_VRtrIfIcmpV6UnreachablesTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,48),_VRtrIfIcmpV6UnreachablesTime_Type())
vRtrIfIcmpV6UnreachablesTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6UnreachablesTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpV6UnreachablesTime.setUnits(_I)
class _VRtrIfIcmpV6TimeExceeded_Type(TruthValue):defaultValue=1
_VRtrIfIcmpV6TimeExceeded_Type.__name__=_E
_VRtrIfIcmpV6TimeExceeded_Object=MibTableColumn
vRtrIfIcmpV6TimeExceeded=_VRtrIfIcmpV6TimeExceeded_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,49),_VRtrIfIcmpV6TimeExceeded_Type())
vRtrIfIcmpV6TimeExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6TimeExceeded.setStatus(_A)
class _VRtrIfIcmpV6NumTimeExceeded_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpV6NumTimeExceeded_Type.__name__=_D
_VRtrIfIcmpV6NumTimeExceeded_Object=MibTableColumn
vRtrIfIcmpV6NumTimeExceeded=_VRtrIfIcmpV6NumTimeExceeded_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,50),_VRtrIfIcmpV6NumTimeExceeded_Type())
vRtrIfIcmpV6NumTimeExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6NumTimeExceeded.setStatus(_A)
class _VRtrIfIcmpV6TimeExceededTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpV6TimeExceededTime_Type.__name__=_D
_VRtrIfIcmpV6TimeExceededTime_Object=MibTableColumn
vRtrIfIcmpV6TimeExceededTime=_VRtrIfIcmpV6TimeExceededTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,51),_VRtrIfIcmpV6TimeExceededTime_Type())
vRtrIfIcmpV6TimeExceededTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6TimeExceededTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpV6TimeExceededTime.setUnits(_I)
class _VRtrIfIcmpV6PktTooBig_Type(TruthValue):defaultValue=1
_VRtrIfIcmpV6PktTooBig_Type.__name__=_E
_VRtrIfIcmpV6PktTooBig_Object=MibTableColumn
vRtrIfIcmpV6PktTooBig=_VRtrIfIcmpV6PktTooBig_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,52),_VRtrIfIcmpV6PktTooBig_Type())
vRtrIfIcmpV6PktTooBig.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6PktTooBig.setStatus(_A)
class _VRtrIfIcmpV6NumPktTooBig_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpV6NumPktTooBig_Type.__name__=_D
_VRtrIfIcmpV6NumPktTooBig_Object=MibTableColumn
vRtrIfIcmpV6NumPktTooBig=_VRtrIfIcmpV6NumPktTooBig_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,53),_VRtrIfIcmpV6NumPktTooBig_Type())
vRtrIfIcmpV6NumPktTooBig.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6NumPktTooBig.setStatus(_A)
class _VRtrIfIcmpV6PktTooBigTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpV6PktTooBigTime_Type.__name__=_D
_VRtrIfIcmpV6PktTooBigTime_Object=MibTableColumn
vRtrIfIcmpV6PktTooBigTime=_VRtrIfIcmpV6PktTooBigTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,54),_VRtrIfIcmpV6PktTooBigTime_Type())
vRtrIfIcmpV6PktTooBigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6PktTooBigTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpV6PktTooBigTime.setUnits(_I)
class _VRtrIfIcmpV6ParamProblem_Type(TruthValue):defaultValue=1
_VRtrIfIcmpV6ParamProblem_Type.__name__=_E
_VRtrIfIcmpV6ParamProblem_Object=MibTableColumn
vRtrIfIcmpV6ParamProblem=_VRtrIfIcmpV6ParamProblem_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,55),_VRtrIfIcmpV6ParamProblem_Type())
vRtrIfIcmpV6ParamProblem.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6ParamProblem.setStatus(_A)
class _VRtrIfIcmpV6NumParamProblem_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1000))
_VRtrIfIcmpV6NumParamProblem_Type.__name__=_D
_VRtrIfIcmpV6NumParamProblem_Object=MibTableColumn
vRtrIfIcmpV6NumParamProblem=_VRtrIfIcmpV6NumParamProblem_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,56),_VRtrIfIcmpV6NumParamProblem_Type())
vRtrIfIcmpV6NumParamProblem.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6NumParamProblem.setStatus(_A)
class _VRtrIfIcmpV6ParamProblemTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VRtrIfIcmpV6ParamProblemTime_Type.__name__=_D
_VRtrIfIcmpV6ParamProblemTime_Object=MibTableColumn
vRtrIfIcmpV6ParamProblemTime=_VRtrIfIcmpV6ParamProblemTime_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,57),_VRtrIfIcmpV6ParamProblemTime_Type())
vRtrIfIcmpV6ParamProblemTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIcmpV6ParamProblemTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfIcmpV6ParamProblemTime.setUnits(_I)
_VRtrIfLinkLocalAddressType_Type=InetAddressType
_VRtrIfLinkLocalAddressType_Object=MibTableColumn
vRtrIfLinkLocalAddressType=_VRtrIfLinkLocalAddressType_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,58),_VRtrIfLinkLocalAddressType_Type())
vRtrIfLinkLocalAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfLinkLocalAddressType.setStatus(_A)
class _VRtrIfLinkLocalAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_VRtrIfLinkLocalAddress_Type.__name__=_O
_VRtrIfLinkLocalAddress_Object=MibTableColumn
vRtrIfLinkLocalAddress=_VRtrIfLinkLocalAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,59),_VRtrIfLinkLocalAddress_Type())
vRtrIfLinkLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfLinkLocalAddress.setStatus(_A)
_VRtrIfLinkLocalAddressState_Type=TmnxInetAddrState
_VRtrIfLinkLocalAddressState_Object=MibTableColumn
vRtrIfLinkLocalAddressState=_VRtrIfLinkLocalAddressState_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,60),_VRtrIfLinkLocalAddressState_Type())
vRtrIfLinkLocalAddressState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfLinkLocalAddressState.setStatus(_A)
_VRtrIfLastOperStateChange_Type=TimeStamp
_VRtrIfLastOperStateChange_Object=MibTableColumn
vRtrIfLastOperStateChange=_VRtrIfLastOperStateChange_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,61),_VRtrIfLastOperStateChange_Type())
vRtrIfLastOperStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfLastOperStateChange.setStatus(_A)
_VRtrIfOperMtu_Type=Unsigned32
_VRtrIfOperMtu_Object=MibTableColumn
vRtrIfOperMtu=_VRtrIfOperMtu_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,62),_VRtrIfOperMtu_Type())
vRtrIfOperMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfOperMtu.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfOperMtu.setUnits('bytes')
class _VRtrIfGlobalIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262144))
_VRtrIfGlobalIndex_Type.__name__=_D
_VRtrIfGlobalIndex_Object=MibTableColumn
vRtrIfGlobalIndex=_VRtrIfGlobalIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,63),_VRtrIfGlobalIndex_Type())
vRtrIfGlobalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfGlobalIndex.setStatus(_A)
class _VRtrIfDelaySeconds_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrIfDelaySeconds_Type.__name__=_D
_VRtrIfDelaySeconds_Object=MibTableColumn
vRtrIfDelaySeconds=_VRtrIfDelaySeconds_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,64),_VRtrIfDelaySeconds_Type())
vRtrIfDelaySeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfDelaySeconds.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfDelaySeconds.setUnits(_I)
_VRtrIfDelayUpTimer_Type=Integer32
_VRtrIfDelayUpTimer_Object=MibTableColumn
vRtrIfDelayUpTimer=_VRtrIfDelayUpTimer_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,65),_VRtrIfDelayUpTimer_Type())
vRtrIfDelayUpTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfDelayUpTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfDelayUpTimer.setUnits(_I)
class _VRtrIfLocalDhcpServerName_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrIfLocalDhcpServerName_Type.__name__=_R
_VRtrIfLocalDhcpServerName_Object=MibTableColumn
vRtrIfLocalDhcpServerName=_VRtrIfLocalDhcpServerName_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,66),_VRtrIfLocalDhcpServerName_Type())
vRtrIfLocalDhcpServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfLocalDhcpServerName.setStatus(_A)
class _VRtrIfInitDelayEnable_Type(TruthValue):defaultValue=2
_VRtrIfInitDelayEnable_Type.__name__=_E
_VRtrIfInitDelayEnable_Object=MibTableColumn
vRtrIfInitDelayEnable=_VRtrIfInitDelayEnable_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,67),_VRtrIfInitDelayEnable_Type())
vRtrIfInitDelayEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfInitDelayEnable.setStatus(_A)
_VRtrIfCpmProtPolicyId_Type=TCpmProtPolicyID
_VRtrIfCpmProtPolicyId_Object=MibTableColumn
vRtrIfCpmProtPolicyId=_VRtrIfCpmProtPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,68),_VRtrIfCpmProtPolicyId_Type())
vRtrIfCpmProtPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfCpmProtPolicyId.setStatus(_A)
_VRtrIfCpmProtUncfgdProtoDropCnt_Type=Gauge32
_VRtrIfCpmProtUncfgdProtoDropCnt_Object=MibTableColumn
vRtrIfCpmProtUncfgdProtoDropCnt=_VRtrIfCpmProtUncfgdProtoDropCnt_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,69),_VRtrIfCpmProtUncfgdProtoDropCnt_Type())
vRtrIfCpmProtUncfgdProtoDropCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfCpmProtUncfgdProtoDropCnt.setStatus(_A)
class _VRtrIfLdpSyncTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1800))
_VRtrIfLdpSyncTimer_Type.__name__=_D
_VRtrIfLdpSyncTimer_Object=MibTableColumn
vRtrIfLdpSyncTimer=_VRtrIfLdpSyncTimer_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,70),_VRtrIfLdpSyncTimer_Type())
vRtrIfLdpSyncTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfLdpSyncTimer.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfLdpSyncTimer.setUnits(_I)
class _VRtrIfStripLabel_Type(TruthValue):defaultValue=2
_VRtrIfStripLabel_Type.__name__=_E
_VRtrIfStripLabel_Object=MibTableColumn
vRtrIfStripLabel=_VRtrIfStripLabel_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,71),_VRtrIfStripLabel_Type())
vRtrIfStripLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfStripLabel.setStatus(_A)
class _VRtrIfuRPFCheckState_Type(TmnxEnabledDisabled):defaultValue=2
_VRtrIfuRPFCheckState_Type.__name__=_k
_VRtrIfuRPFCheckState_Object=MibTableColumn
vRtrIfuRPFCheckState=_VRtrIfuRPFCheckState_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,72),_VRtrIfuRPFCheckState_Type())
vRtrIfuRPFCheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfuRPFCheckState.setStatus(_A)
class _VRtrIfuRPFCheckMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_VRtrIfuRPFCheckMode_Type.__name__=_F
_VRtrIfuRPFCheckMode_Object=MibTableColumn
vRtrIfuRPFCheckMode=_VRtrIfuRPFCheckMode_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,73),_VRtrIfuRPFCheckMode_Type())
vRtrIfuRPFCheckMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfuRPFCheckMode.setStatus(_A)
class _VRtrIfQosQGrp_Type(TNamedItemOrEmpty):defaultHexValue=''
_VRtrIfQosQGrp_Type.__name__=_R
_VRtrIfQosQGrp_Object=MibTableColumn
vRtrIfQosQGrp=_VRtrIfQosQGrp_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,74),_VRtrIfQosQGrp_Type())
vRtrIfQosQGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfQosQGrp.setStatus(_M)
class _VRtrIfAdminLinkLocalAddrType_Type(InetAddressType):defaultValue=0
_VRtrIfAdminLinkLocalAddrType_Type.__name__=_Z
_VRtrIfAdminLinkLocalAddrType_Object=MibTableColumn
vRtrIfAdminLinkLocalAddrType=_VRtrIfAdminLinkLocalAddrType_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,75),_VRtrIfAdminLinkLocalAddrType_Type())
vRtrIfAdminLinkLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfAdminLinkLocalAddrType.setStatus(_A)
class _VRtrIfAdminLinkLocalAddr_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(20,20))
_VRtrIfAdminLinkLocalAddr_Type.__name__=_O
_VRtrIfAdminLinkLocalAddr_Object=MibTableColumn
vRtrIfAdminLinkLocalAddr=_VRtrIfAdminLinkLocalAddr_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,76),_VRtrIfAdminLinkLocalAddr_Type())
vRtrIfAdminLinkLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfAdminLinkLocalAddr.setStatus(_A)
class _VRtrIfAdmLnkLclAddrPreferred_Type(TruthValue):defaultValue=2
_VRtrIfAdmLnkLclAddrPreferred_Type.__name__=_E
_VRtrIfAdmLnkLclAddrPreferred_Object=MibTableColumn
vRtrIfAdmLnkLclAddrPreferred=_VRtrIfAdmLnkLclAddrPreferred_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,77),_VRtrIfAdmLnkLclAddrPreferred_Type())
vRtrIfAdmLnkLclAddrPreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfAdmLnkLclAddrPreferred.setStatus(_A)
class _VRtrIfOperDownReason_Type(Bits):namedValues=NamedValues(*(('ifAdminDown',0),('svcAdminDown',1),('portOperDown',2),('addrOrIfNotReady',3),('assocObjNotReady',4),('rvplsDown',5),('operGrpDown',6),('ifAdminDestroy',7),('noIfAddress',8),('noIfInfo',9),('delayedStartEnabled',10),('ifProtoOperDown',11),('invalidPortCfg',12),(_T,13),('ipv6Misconfig',14)))
_VRtrIfOperDownReason_Type.__name__=_S
_VRtrIfOperDownReason_Object=MibTableColumn
vRtrIfOperDownReason=_VRtrIfOperDownReason_Object((1,3,6,1,4,1,7483,6,1,2,3,4,1,78),_VRtrIfOperDownReason_Type())
vRtrIfOperDownReason.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfOperDownReason.setStatus(_A)
_VRtrIfNameTable_Object=MibTable
vRtrIfNameTable=_VRtrIfNameTable_Object((1,3,6,1,4,1,7483,6,1,2,3,5))
if mibBuilder.loadTexts:vRtrIfNameTable.setStatus(_A)
_VRtrIfNameEntry_Object=MibTableRow
vRtrIfNameEntry=_VRtrIfNameEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,5,1))
vRtrIfNameEntry.setIndexNames((0,_K,_L),(0,_G,_P),(1,_G,_A0))
if mibBuilder.loadTexts:vRtrIfNameEntry.setStatus(_A)
_VRtrIfNameIndex_Type=InterfaceIndex
_VRtrIfNameIndex_Object=MibTableColumn
vRtrIfNameIndex=_VRtrIfNameIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,5,1,1),_VRtrIfNameIndex_Type())
vRtrIfNameIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfNameIndex.setStatus(_A)
_VRtrIpAddrTable_Object=MibTable
vRtrIpAddrTable=_VRtrIpAddrTable_Object((1,3,6,1,4,1,7483,6,1,2,3,6))
if mibBuilder.loadTexts:vRtrIpAddrTable.setStatus(_A)
_VRtrIpAddrEntry_Object=MibTableRow
vRtrIpAddrEntry=_VRtrIpAddrEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1))
vRtrIpAddrEntry.setIndexNames((0,_K,_L),(0,_G,_P),(0,_G,_U),(0,_G,_A1))
if mibBuilder.loadTexts:vRtrIpAddrEntry.setStatus(_A)
class _VRiaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_VRiaIndex_Type.__name__=_F
_VRiaIndex_Object=MibTableColumn
vRiaIndex=_VRiaIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,1),_VRiaIndex_Type())
vRiaIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRiaIndex.setStatus(_A)
_VRiaRowStatus_Type=RowStatus
_VRiaRowStatus_Object=MibTableColumn
vRiaRowStatus=_VRiaRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,2),_VRiaRowStatus_Type())
vRiaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaRowStatus.setStatus(_A)
_VRiaIpAddress_Type=IpAddress
_VRiaIpAddress_Object=MibTableColumn
vRiaIpAddress=_VRiaIpAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,3),_VRiaIpAddress_Type())
vRiaIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaIpAddress.setStatus(_A)
class _VRiaNetMask_Type(IpAddress):defaultHexValue='FFFFFF00'
_VRiaNetMask_Type.__name__=_f
_VRiaNetMask_Object=MibTableColumn
vRiaNetMask=_VRiaNetMask_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,4),_VRiaNetMask_Type())
vRiaNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaNetMask.setStatus(_A)
class _VRiaBcastAddrFormat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allOnes',1),('hostOnes',2)))
_VRiaBcastAddrFormat_Type.__name__=_F
_VRiaBcastAddrFormat_Object=MibTableColumn
vRiaBcastAddrFormat=_VRiaBcastAddrFormat_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,5),_VRiaBcastAddrFormat_Type())
vRiaBcastAddrFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaBcastAddrFormat.setStatus(_A)
class _VRiaReasmMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRiaReasmMaxSize_Type.__name__=_F
_VRiaReasmMaxSize_Object=MibTableColumn
vRiaReasmMaxSize=_VRiaReasmMaxSize_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,6),_VRiaReasmMaxSize_Type())
vRiaReasmMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaReasmMaxSize.setStatus(_A)
_VRiaIgpInhibit_Type=TruthValue
_VRiaIgpInhibit_Object=MibTableColumn
vRiaIgpInhibit=_VRiaIgpInhibit_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,7),_VRiaIgpInhibit_Type())
vRiaIgpInhibit.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaIgpInhibit.setStatus(_A)
_VRiaInetAddressType_Type=InetAddressType
_VRiaInetAddressType_Object=MibTableColumn
vRiaInetAddressType=_VRiaInetAddressType_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,8),_VRiaInetAddressType_Type())
vRiaInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetAddressType.setStatus(_A)
class _VRiaInetAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRiaInetAddress_Type.__name__=_O
_VRiaInetAddress_Object=MibTableColumn
vRiaInetAddress=_VRiaInetAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,9),_VRiaInetAddress_Type())
vRiaInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetAddress.setStatus(_A)
_VRiaInetPrefixLen_Type=InetAddressPrefixLength
_VRiaInetPrefixLen_Object=MibTableColumn
vRiaInetPrefixLen=_VRiaInetPrefixLen_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,10),_VRiaInetPrefixLen_Type())
vRiaInetPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetPrefixLen.setStatus(_A)
_VRiaInetAddrState_Type=TmnxInetAddrState
_VRiaInetAddrState_Object=MibTableColumn
vRiaInetAddrState=_VRiaInetAddrState_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,11),_VRiaInetAddrState_Type())
vRiaInetAddrState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRiaInetAddrState.setStatus(_A)
class _VRiaInetEui64_Type(TruthValue):defaultValue=2
_VRiaInetEui64_Type.__name__=_E
_VRiaInetEui64_Object=MibTableColumn
vRiaInetEui64=_VRiaInetEui64_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,12),_VRiaInetEui64_Type())
vRiaInetEui64.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetEui64.setStatus(_A)
_VRiaInetOperAddress_Type=InetAddress
_VRiaInetOperAddress_Object=MibTableColumn
vRiaInetOperAddress=_VRiaInetOperAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,13),_VRiaInetOperAddress_Type())
vRiaInetOperAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:vRiaInetOperAddress.setStatus(_A)
class _VRiaInetGwAddressType_Type(InetAddressType):defaultValue=0
_VRiaInetGwAddressType_Type.__name__=_Z
_VRiaInetGwAddressType_Object=MibTableColumn
vRiaInetGwAddressType=_VRiaInetGwAddressType_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,14),_VRiaInetGwAddressType_Type())
vRiaInetGwAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetGwAddressType.setStatus(_A)
class _VRiaInetGwAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRiaInetGwAddress_Type.__name__=_O
_VRiaInetGwAddress_Object=MibTableColumn
vRiaInetGwAddress=_VRiaInetGwAddress_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,15),_VRiaInetGwAddress_Type())
vRiaInetGwAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetGwAddress.setStatus(_A)
class _VRiaInetRemoteIpType_Type(InetAddressType):defaultValue=0
_VRiaInetRemoteIpType_Type.__name__=_Z
_VRiaInetRemoteIpType_Object=MibTableColumn
vRiaInetRemoteIpType=_VRiaInetRemoteIpType_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,16),_VRiaInetRemoteIpType_Type())
vRiaInetRemoteIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetRemoteIpType.setStatus(_A)
class _VRiaInetRemoteIp_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRiaInetRemoteIp_Type.__name__=_O
_VRiaInetRemoteIp_Object=MibTableColumn
vRiaInetRemoteIp=_VRiaInetRemoteIp_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,17),_VRiaInetRemoteIp_Type())
vRiaInetRemoteIp.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetRemoteIp.setStatus(_A)
class _VRiaInetAddrPreferred_Type(TruthValue):defaultValue=2
_VRiaInetAddrPreferred_Type.__name__=_E
_VRiaInetAddrPreferred_Object=MibTableColumn
vRiaInetAddrPreferred=_VRiaInetAddrPreferred_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,18),_VRiaInetAddrPreferred_Type())
vRiaInetAddrPreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaInetAddrPreferred.setStatus(_A)
class _VRiaSubscrPrefix_Type(TruthValue):defaultValue=2
_VRiaSubscrPrefix_Type.__name__=_E
_VRiaSubscrPrefix_Object=MibTableColumn
vRiaSubscrPrefix=_VRiaSubscrPrefix_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,19),_VRiaSubscrPrefix_Type())
vRiaSubscrPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaSubscrPrefix.setStatus(_A)
class _VRiaSubscrPrefixType_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('pd',0),('wan-host',1)))
_VRiaSubscrPrefixType_Type.__name__=_S
_VRiaSubscrPrefixType_Object=MibTableColumn
vRiaSubscrPrefixType=_VRiaSubscrPrefixType_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,20),_VRiaSubscrPrefixType_Type())
vRiaSubscrPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaSubscrPrefixType.setStatus(_A)
class _VRiaSubscrHostRoutePopulate_Type(TruthValue):defaultValue=2
_VRiaSubscrHostRoutePopulate_Type.__name__=_E
_VRiaSubscrHostRoutePopulate_Object=MibTableColumn
vRiaSubscrHostRoutePopulate=_VRiaSubscrHostRoutePopulate_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,21),_VRiaSubscrHostRoutePopulate_Type())
vRiaSubscrHostRoutePopulate.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaSubscrHostRoutePopulate.setStatus(_A)
class _VRiaTrackSrrpInstance_Type(Unsigned32):defaultValue=0
_VRiaTrackSrrpInstance_Type.__name__=_D
_VRiaTrackSrrpInstance_Object=MibTableColumn
vRiaTrackSrrpInstance=_VRiaTrackSrrpInstance_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,22),_VRiaTrackSrrpInstance_Type())
vRiaTrackSrrpInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaTrackSrrpInstance.setStatus(_A)
class _VRiaHoldUpTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,5000))
_VRiaHoldUpTime_Type.__name__=_D
_VRiaHoldUpTime_Object=MibTableColumn
vRiaHoldUpTime=_VRiaHoldUpTime_Object((1,3,6,1,4,1,7483,6,1,2,3,6,1,23),_VRiaHoldUpTime_Type())
vRiaHoldUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vRiaHoldUpTime.setStatus(_A)
if mibBuilder.loadTexts:vRiaHoldUpTime.setUnits('milli-seconds')
_TnVRtrGlobalObjs_ObjectIdentity=ObjectIdentity
tnVRtrGlobalObjs=_TnVRtrGlobalObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,3,15))
_VRtrNextVRtrID_Type=TestAndIncr
_VRtrNextVRtrID_Object=MibScalar
vRtrNextVRtrID=_VRtrNextVRtrID_Object((1,3,6,1,4,1,7483,6,1,2,3,15,1),_VRtrNextVRtrID_Type())
vRtrNextVRtrID.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrNextVRtrID.setStatus(_A)
_VRtrConfiguredVRtrs_Type=Gauge32
_VRtrConfiguredVRtrs_Object=MibScalar
vRtrConfiguredVRtrs=_VRtrConfiguredVRtrs_Object((1,3,6,1,4,1,7483,6,1,2,3,15,2),_VRtrConfiguredVRtrs_Type())
vRtrConfiguredVRtrs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrConfiguredVRtrs.setStatus(_A)
_VRtrActiveVRtrs_Type=Gauge32
_VRtrActiveVRtrs_Object=MibScalar
vRtrActiveVRtrs=_VRtrActiveVRtrs_Object((1,3,6,1,4,1,7483,6,1,2,3,15,3),_VRtrActiveVRtrs_Type())
vRtrActiveVRtrs.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrActiveVRtrs.setStatus(_A)
class _VRtrRouteThresholdSoakTime_Type(Unsigned32):defaultValue=600
_VRtrRouteThresholdSoakTime_Type.__name__=_D
_VRtrRouteThresholdSoakTime_Object=MibScalar
vRtrRouteThresholdSoakTime=_VRtrRouteThresholdSoakTime_Object((1,3,6,1,4,1,7483,6,1,2,3,15,4),_VRtrRouteThresholdSoakTime_Type())
vRtrRouteThresholdSoakTime.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrRouteThresholdSoakTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrRouteThresholdSoakTime.setUnits(_I)
_VRtrMaxARPEntries_Type=Unsigned32
_VRtrMaxARPEntries_Object=MibScalar
vRtrMaxARPEntries=_VRtrMaxARPEntries_Object((1,3,6,1,4,1,7483,6,1,2,3,15,5),_VRtrMaxARPEntries_Type())
vRtrMaxARPEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrMaxARPEntries.setStatus(_A)
class _VRtrIPv6RouteThresholdSoakTime_Type(Unsigned32):defaultValue=600
_VRtrIPv6RouteThresholdSoakTime_Type.__name__=_D
_VRtrIPv6RouteThresholdSoakTime_Object=MibScalar
vRtrIPv6RouteThresholdSoakTime=_VRtrIPv6RouteThresholdSoakTime_Object((1,3,6,1,4,1,7483,6,1,2,3,15,6),_VRtrIPv6RouteThresholdSoakTime_Type())
vRtrIPv6RouteThresholdSoakTime.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIPv6RouteThresholdSoakTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrIPv6RouteThresholdSoakTime.setUnits(_I)
_VRtrIfGlobalIndexTable_Object=MibTable
vRtrIfGlobalIndexTable=_VRtrIfGlobalIndexTable_Object((1,3,6,1,4,1,7483,6,1,2,3,37))
if mibBuilder.loadTexts:vRtrIfGlobalIndexTable.setStatus(_A)
_VRtrIfGlobalIndexEntry_Object=MibTableRow
vRtrIfGlobalIndexEntry=_VRtrIfGlobalIndexEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,37,1))
vRtrIfGlobalIndexEntry.setIndexNames((0,_K,_L),(0,_G,_A2))
if mibBuilder.loadTexts:vRtrIfGlobalIndexEntry.setStatus(_A)
_VRtrIfGlobalIndexvRtrID_Type=TmnxVRtrID
_VRtrIfGlobalIndexvRtrID_Object=MibTableColumn
vRtrIfGlobalIndexvRtrID=_VRtrIfGlobalIndexvRtrID_Object((1,3,6,1,4,1,7483,6,1,2,3,37,1,1),_VRtrIfGlobalIndexvRtrID_Type())
vRtrIfGlobalIndexvRtrID.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfGlobalIndexvRtrID.setStatus(_A)
_VRtrIfGlobalIndexvRtrIfIndex_Type=InterfaceIndex
_VRtrIfGlobalIndexvRtrIfIndex_Object=MibTableColumn
vRtrIfGlobalIndexvRtrIfIndex=_VRtrIfGlobalIndexvRtrIfIndex_Object((1,3,6,1,4,1,7483,6,1,2,3,37,1,2),_VRtrIfGlobalIndexvRtrIfIndex_Type())
vRtrIfGlobalIndexvRtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfGlobalIndexvRtrIfIndex.setStatus(_A)
_VRtrIfStatsTable_Object=MibTable
vRtrIfStatsTable=_VRtrIfStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,3,54))
if mibBuilder.loadTexts:vRtrIfStatsTable.setStatus(_A)
_VRtrIfStatsEntry_Object=MibTableRow
vRtrIfStatsEntry=_VRtrIfStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1))
vRtrIfStatsEntry.setIndexNames((0,_K,_L),(0,_G,_P),(0,_G,_U))
if mibBuilder.loadTexts:vRtrIfStatsEntry.setStatus(_A)
_VRtrIfuRPFCheckFailPkts_Type=Counter64
_VRtrIfuRPFCheckFailPkts_Object=MibTableColumn
vRtrIfuRPFCheckFailPkts=_VRtrIfuRPFCheckFailPkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,1),_VRtrIfuRPFCheckFailPkts_Type())
vRtrIfuRPFCheckFailPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailPkts.setStatus(_A)
_VRtrIfuRPFCheckFailPktsLow32_Type=Counter32
_VRtrIfuRPFCheckFailPktsLow32_Object=MibTableColumn
vRtrIfuRPFCheckFailPktsLow32=_VRtrIfuRPFCheckFailPktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,2),_VRtrIfuRPFCheckFailPktsLow32_Type())
vRtrIfuRPFCheckFailPktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailPktsLow32.setStatus(_A)
_VRtrIfuRPFCheckFailPktsHigh32_Type=Counter32
_VRtrIfuRPFCheckFailPktsHigh32_Object=MibTableColumn
vRtrIfuRPFCheckFailPktsHigh32=_VRtrIfuRPFCheckFailPktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,3),_VRtrIfuRPFCheckFailPktsHigh32_Type())
vRtrIfuRPFCheckFailPktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailPktsHigh32.setStatus(_A)
_VRtrIfuRPFCheckFailBytes_Type=Counter64
_VRtrIfuRPFCheckFailBytes_Object=MibTableColumn
vRtrIfuRPFCheckFailBytes=_VRtrIfuRPFCheckFailBytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,4),_VRtrIfuRPFCheckFailBytes_Type())
vRtrIfuRPFCheckFailBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailBytes.setStatus(_A)
_VRtrIfuRPFCheckFailBytesLow32_Type=Counter32
_VRtrIfuRPFCheckFailBytesLow32_Object=MibTableColumn
vRtrIfuRPFCheckFailBytesLow32=_VRtrIfuRPFCheckFailBytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,5),_VRtrIfuRPFCheckFailBytesLow32_Type())
vRtrIfuRPFCheckFailBytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailBytesLow32.setStatus(_A)
_VRtrIfuRPFCheckFailBytesHigh32_Type=Counter32
_VRtrIfuRPFCheckFailBytesHigh32_Object=MibTableColumn
vRtrIfuRPFCheckFailBytesHigh32=_VRtrIfuRPFCheckFailBytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,6),_VRtrIfuRPFCheckFailBytesHigh32_Type())
vRtrIfuRPFCheckFailBytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfuRPFCheckFailBytesHigh32.setStatus(_A)
_VRtrIfIpReasFragPktsRcvd_Type=Counter64
_VRtrIfIpReasFragPktsRcvd_Object=MibTableColumn
vRtrIfIpReasFragPktsRcvd=_VRtrIfIpReasFragPktsRcvd_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,7),_VRtrIfIpReasFragPktsRcvd_Type())
vRtrIfIpReasFragPktsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsRcvd.setStatus(_A)
_VRtrIfIpReasFragPktsRcvdLow32_Type=Counter32
_VRtrIfIpReasFragPktsRcvdLow32_Object=MibTableColumn
vRtrIfIpReasFragPktsRcvdLow32=_VRtrIfIpReasFragPktsRcvdLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,8),_VRtrIfIpReasFragPktsRcvdLow32_Type())
vRtrIfIpReasFragPktsRcvdLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsRcvdLow32.setStatus(_A)
_VRtrIfIpReasFragPktsRcvdHigh32_Type=Counter32
_VRtrIfIpReasFragPktsRcvdHigh32_Object=MibTableColumn
vRtrIfIpReasFragPktsRcvdHigh32=_VRtrIfIpReasFragPktsRcvdHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,9),_VRtrIfIpReasFragPktsRcvdHigh32_Type())
vRtrIfIpReasFragPktsRcvdHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsRcvdHigh32.setStatus(_A)
_VRtrIfIpReasFragBytesRcvd_Type=Counter64
_VRtrIfIpReasFragBytesRcvd_Object=MibTableColumn
vRtrIfIpReasFragBytesRcvd=_VRtrIfIpReasFragBytesRcvd_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,10),_VRtrIfIpReasFragBytesRcvd_Type())
vRtrIfIpReasFragBytesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesRcvd.setStatus(_A)
_VRtrIfIpReasFragBytesRcvdLow32_Type=Counter32
_VRtrIfIpReasFragBytesRcvdLow32_Object=MibTableColumn
vRtrIfIpReasFragBytesRcvdLow32=_VRtrIfIpReasFragBytesRcvdLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,11),_VRtrIfIpReasFragBytesRcvdLow32_Type())
vRtrIfIpReasFragBytesRcvdLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesRcvdLow32.setStatus(_A)
_VRtrIfIpReasFragBytesRcvdHigh32_Type=Counter32
_VRtrIfIpReasFragBytesRcvdHigh32_Object=MibTableColumn
vRtrIfIpReasFragBytesRcvdHigh32=_VRtrIfIpReasFragBytesRcvdHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,12),_VRtrIfIpReasFragBytesRcvdHigh32_Type())
vRtrIfIpReasFragBytesRcvdHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesRcvdHigh32.setStatus(_A)
_VRtrIfIpReasFragPktsReas_Type=Counter64
_VRtrIfIpReasFragPktsReas_Object=MibTableColumn
vRtrIfIpReasFragPktsReas=_VRtrIfIpReasFragPktsReas_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,13),_VRtrIfIpReasFragPktsReas_Type())
vRtrIfIpReasFragPktsReas.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsReas.setStatus(_A)
_VRtrIfIpReasFragPktsReasLow32_Type=Counter32
_VRtrIfIpReasFragPktsReasLow32_Object=MibTableColumn
vRtrIfIpReasFragPktsReasLow32=_VRtrIfIpReasFragPktsReasLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,14),_VRtrIfIpReasFragPktsReasLow32_Type())
vRtrIfIpReasFragPktsReasLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsReasLow32.setStatus(_A)
_VRtrIfIpReasFragPktsReasHigh32_Type=Counter32
_VRtrIfIpReasFragPktsReasHigh32_Object=MibTableColumn
vRtrIfIpReasFragPktsReasHigh32=_VRtrIfIpReasFragPktsReasHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,15),_VRtrIfIpReasFragPktsReasHigh32_Type())
vRtrIfIpReasFragPktsReasHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragPktsReasHigh32.setStatus(_A)
_VRtrIfIpReasFragBytesReas_Type=Counter64
_VRtrIfIpReasFragBytesReas_Object=MibTableColumn
vRtrIfIpReasFragBytesReas=_VRtrIfIpReasFragBytesReas_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,16),_VRtrIfIpReasFragBytesReas_Type())
vRtrIfIpReasFragBytesReas.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesReas.setStatus(_A)
_VRtrIfIpReasFragBytesReasLow32_Type=Counter32
_VRtrIfIpReasFragBytesReasLow32_Object=MibTableColumn
vRtrIfIpReasFragBytesReasLow32=_VRtrIfIpReasFragBytesReasLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,17),_VRtrIfIpReasFragBytesReasLow32_Type())
vRtrIfIpReasFragBytesReasLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesReasLow32.setStatus(_A)
_VRtrIfIpReasFragBytesReasHigh32_Type=Counter32
_VRtrIfIpReasFragBytesReasHigh32_Object=MibTableColumn
vRtrIfIpReasFragBytesReasHigh32=_VRtrIfIpReasFragBytesReasHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,18),_VRtrIfIpReasFragBytesReasHigh32_Type())
vRtrIfIpReasFragBytesReasHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragBytesReasHigh32.setStatus(_A)
_VRtrIfIpReasFragReasErrors_Type=Counter64
_VRtrIfIpReasFragReasErrors_Object=MibTableColumn
vRtrIfIpReasFragReasErrors=_VRtrIfIpReasFragReasErrors_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,19),_VRtrIfIpReasFragReasErrors_Type())
vRtrIfIpReasFragReasErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragReasErrors.setStatus(_A)
_VRtrIfIpReasFragReasErrorsLow32_Type=Counter32
_VRtrIfIpReasFragReasErrorsLow32_Object=MibTableColumn
vRtrIfIpReasFragReasErrorsLow32=_VRtrIfIpReasFragReasErrorsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,20),_VRtrIfIpReasFragReasErrorsLow32_Type())
vRtrIfIpReasFragReasErrorsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragReasErrorsLow32.setStatus(_A)
_VRtrIfIpReasFragReasErrorsHigh32_Type=Counter32
_VRtrIfIpReasFragReasErrorsHigh32_Object=MibTableColumn
vRtrIfIpReasFragReasErrorsHigh32=_VRtrIfIpReasFragReasErrorsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,21),_VRtrIfIpReasFragReasErrorsHigh32_Type())
vRtrIfIpReasFragReasErrorsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragReasErrorsHigh32.setStatus(_A)
_VRtrIfIpReasFragDisc_Type=Counter64
_VRtrIfIpReasFragDisc_Object=MibTableColumn
vRtrIfIpReasFragDisc=_VRtrIfIpReasFragDisc_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,22),_VRtrIfIpReasFragDisc_Type())
vRtrIfIpReasFragDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragDisc.setStatus(_A)
_VRtrIfIpReasFragDiscLow32_Type=Counter32
_VRtrIfIpReasFragDiscLow32_Object=MibTableColumn
vRtrIfIpReasFragDiscLow32=_VRtrIfIpReasFragDiscLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,23),_VRtrIfIpReasFragDiscLow32_Type())
vRtrIfIpReasFragDiscLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragDiscLow32.setStatus(_A)
_VRtrIfIpReasFragDiscHigh32_Type=Counter32
_VRtrIfIpReasFragDiscHigh32_Object=MibTableColumn
vRtrIfIpReasFragDiscHigh32=_VRtrIfIpReasFragDiscHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,24),_VRtrIfIpReasFragDiscHigh32_Type())
vRtrIfIpReasFragDiscHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasFragDiscHigh32.setStatus(_A)
_VRtrIfIpReasOutBufRes_Type=Counter64
_VRtrIfIpReasOutBufRes_Object=MibTableColumn
vRtrIfIpReasOutBufRes=_VRtrIfIpReasOutBufRes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,25),_VRtrIfIpReasOutBufRes_Type())
vRtrIfIpReasOutBufRes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasOutBufRes.setStatus(_A)
_VRtrIfIpReasOutBufResLow32_Type=Counter32
_VRtrIfIpReasOutBufResLow32_Object=MibTableColumn
vRtrIfIpReasOutBufResLow32=_VRtrIfIpReasOutBufResLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,26),_VRtrIfIpReasOutBufResLow32_Type())
vRtrIfIpReasOutBufResLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasOutBufResLow32.setStatus(_A)
_VRtrIfIpReasOutBufResHigh32_Type=Counter32
_VRtrIfIpReasOutBufResHigh32_Object=MibTableColumn
vRtrIfIpReasOutBufResHigh32=_VRtrIfIpReasOutBufResHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,27),_VRtrIfIpReasOutBufResHigh32_Type())
vRtrIfIpReasOutBufResHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasOutBufResHigh32.setStatus(_A)
_VRtrIfIpReasPktsRx_Type=Counter64
_VRtrIfIpReasPktsRx_Object=MibTableColumn
vRtrIfIpReasPktsRx=_VRtrIfIpReasPktsRx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,28),_VRtrIfIpReasPktsRx_Type())
vRtrIfIpReasPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsRx.setStatus(_A)
_VRtrIfIpReasPktsRxLow32_Type=Counter32
_VRtrIfIpReasPktsRxLow32_Object=MibTableColumn
vRtrIfIpReasPktsRxLow32=_VRtrIfIpReasPktsRxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,29),_VRtrIfIpReasPktsRxLow32_Type())
vRtrIfIpReasPktsRxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsRxLow32.setStatus(_A)
_VRtrIfIpReasPktsRxHigh32_Type=Counter32
_VRtrIfIpReasPktsRxHigh32_Object=MibTableColumn
vRtrIfIpReasPktsRxHigh32=_VRtrIfIpReasPktsRxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,30),_VRtrIfIpReasPktsRxHigh32_Type())
vRtrIfIpReasPktsRxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsRxHigh32.setStatus(_A)
_VRtrIfIpReasBytesRx_Type=Counter64
_VRtrIfIpReasBytesRx_Object=MibTableColumn
vRtrIfIpReasBytesRx=_VRtrIfIpReasBytesRx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,31),_VRtrIfIpReasBytesRx_Type())
vRtrIfIpReasBytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesRx.setStatus(_A)
_VRtrIfIpReasBytesRxLow32_Type=Counter32
_VRtrIfIpReasBytesRxLow32_Object=MibTableColumn
vRtrIfIpReasBytesRxLow32=_VRtrIfIpReasBytesRxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,32),_VRtrIfIpReasBytesRxLow32_Type())
vRtrIfIpReasBytesRxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesRxLow32.setStatus(_A)
_VRtrIfIpReasBytesRxHigh32_Type=Counter32
_VRtrIfIpReasBytesRxHigh32_Object=MibTableColumn
vRtrIfIpReasBytesRxHigh32=_VRtrIfIpReasBytesRxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,33),_VRtrIfIpReasBytesRxHigh32_Type())
vRtrIfIpReasBytesRxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesRxHigh32.setStatus(_A)
_VRtrIfIpReasPktsTx_Type=Counter64
_VRtrIfIpReasPktsTx_Object=MibTableColumn
vRtrIfIpReasPktsTx=_VRtrIfIpReasPktsTx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,34),_VRtrIfIpReasPktsTx_Type())
vRtrIfIpReasPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsTx.setStatus(_A)
_VRtrIfIpReasPktsTxLow32_Type=Counter32
_VRtrIfIpReasPktsTxLow32_Object=MibTableColumn
vRtrIfIpReasPktsTxLow32=_VRtrIfIpReasPktsTxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,35),_VRtrIfIpReasPktsTxLow32_Type())
vRtrIfIpReasPktsTxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsTxLow32.setStatus(_A)
_VRtrIfIpReasPktsTxHigh32_Type=Counter32
_VRtrIfIpReasPktsTxHigh32_Object=MibTableColumn
vRtrIfIpReasPktsTxHigh32=_VRtrIfIpReasPktsTxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,36),_VRtrIfIpReasPktsTxHigh32_Type())
vRtrIfIpReasPktsTxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasPktsTxHigh32.setStatus(_A)
_VRtrIfIpReasBytesTx_Type=Counter64
_VRtrIfIpReasBytesTx_Object=MibTableColumn
vRtrIfIpReasBytesTx=_VRtrIfIpReasBytesTx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,37),_VRtrIfIpReasBytesTx_Type())
vRtrIfIpReasBytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesTx.setStatus(_A)
_VRtrIfIpReasBytesTxLow32_Type=Counter32
_VRtrIfIpReasBytesTxLow32_Object=MibTableColumn
vRtrIfIpReasBytesTxLow32=_VRtrIfIpReasBytesTxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,38),_VRtrIfIpReasBytesTxLow32_Type())
vRtrIfIpReasBytesTxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesTxLow32.setStatus(_A)
_VRtrIfIpReasBytesTxHigh32_Type=Counter32
_VRtrIfIpReasBytesTxHigh32_Object=MibTableColumn
vRtrIfIpReasBytesTxHigh32=_VRtrIfIpReasBytesTxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,39),_VRtrIfIpReasBytesTxHigh32_Type())
vRtrIfIpReasBytesTxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasBytesTxHigh32.setStatus(_A)
_VRtrIfRxPkts_Type=Counter64
_VRtrIfRxPkts_Object=MibTableColumn
vRtrIfRxPkts=_VRtrIfRxPkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,40),_VRtrIfRxPkts_Type())
vRtrIfRxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxPkts.setStatus(_A)
_VRtrIfRxPktsLow32_Type=Counter32
_VRtrIfRxPktsLow32_Object=MibTableColumn
vRtrIfRxPktsLow32=_VRtrIfRxPktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,41),_VRtrIfRxPktsLow32_Type())
vRtrIfRxPktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxPktsLow32.setStatus(_A)
_VRtrIfRxPktsHigh32_Type=Counter32
_VRtrIfRxPktsHigh32_Object=MibTableColumn
vRtrIfRxPktsHigh32=_VRtrIfRxPktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,42),_VRtrIfRxPktsHigh32_Type())
vRtrIfRxPktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxPktsHigh32.setStatus(_A)
_VRtrIfRxBytes_Type=Counter64
_VRtrIfRxBytes_Object=MibTableColumn
vRtrIfRxBytes=_VRtrIfRxBytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,43),_VRtrIfRxBytes_Type())
vRtrIfRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxBytes.setStatus(_A)
_VRtrIfRxBytesLow32_Type=Counter32
_VRtrIfRxBytesLow32_Object=MibTableColumn
vRtrIfRxBytesLow32=_VRtrIfRxBytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,44),_VRtrIfRxBytesLow32_Type())
vRtrIfRxBytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxBytesLow32.setStatus(_A)
_VRtrIfRxBytesHigh32_Type=Counter32
_VRtrIfRxBytesHigh32_Object=MibTableColumn
vRtrIfRxBytesHigh32=_VRtrIfRxBytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,45),_VRtrIfRxBytesHigh32_Type())
vRtrIfRxBytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfRxBytesHigh32.setStatus(_A)
_VRtrIfTxV4Pkts_Type=Counter64
_VRtrIfTxV4Pkts_Object=MibTableColumn
vRtrIfTxV4Pkts=_VRtrIfTxV4Pkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,46),_VRtrIfTxV4Pkts_Type())
vRtrIfTxV4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4Pkts.setStatus(_A)
_VRtrIfTxV4PktsLow32_Type=Counter32
_VRtrIfTxV4PktsLow32_Object=MibTableColumn
vRtrIfTxV4PktsLow32=_VRtrIfTxV4PktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,47),_VRtrIfTxV4PktsLow32_Type())
vRtrIfTxV4PktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4PktsLow32.setStatus(_A)
_VRtrIfTxV4PktsHigh32_Type=Counter32
_VRtrIfTxV4PktsHigh32_Object=MibTableColumn
vRtrIfTxV4PktsHigh32=_VRtrIfTxV4PktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,48),_VRtrIfTxV4PktsHigh32_Type())
vRtrIfTxV4PktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4PktsHigh32.setStatus(_A)
_VRtrIfTxV4Bytes_Type=Counter64
_VRtrIfTxV4Bytes_Object=MibTableColumn
vRtrIfTxV4Bytes=_VRtrIfTxV4Bytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,49),_VRtrIfTxV4Bytes_Type())
vRtrIfTxV4Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4Bytes.setStatus(_A)
_VRtrIfTxV4BytesLow32_Type=Counter32
_VRtrIfTxV4BytesLow32_Object=MibTableColumn
vRtrIfTxV4BytesLow32=_VRtrIfTxV4BytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,50),_VRtrIfTxV4BytesLow32_Type())
vRtrIfTxV4BytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4BytesLow32.setStatus(_A)
_VRtrIfTxV4BytesHigh32_Type=Counter32
_VRtrIfTxV4BytesHigh32_Object=MibTableColumn
vRtrIfTxV4BytesHigh32=_VRtrIfTxV4BytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,51),_VRtrIfTxV4BytesHigh32_Type())
vRtrIfTxV4BytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4BytesHigh32.setStatus(_A)
_VRtrIfTxV6Pkts_Type=Counter64
_VRtrIfTxV6Pkts_Object=MibTableColumn
vRtrIfTxV6Pkts=_VRtrIfTxV6Pkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,52),_VRtrIfTxV6Pkts_Type())
vRtrIfTxV6Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6Pkts.setStatus(_A)
_VRtrIfTxV6PktsLow32_Type=Counter32
_VRtrIfTxV6PktsLow32_Object=MibTableColumn
vRtrIfTxV6PktsLow32=_VRtrIfTxV6PktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,53),_VRtrIfTxV6PktsLow32_Type())
vRtrIfTxV6PktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6PktsLow32.setStatus(_A)
_VRtrIfTxV6PktsHigh32_Type=Counter32
_VRtrIfTxV6PktsHigh32_Object=MibTableColumn
vRtrIfTxV6PktsHigh32=_VRtrIfTxV6PktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,54),_VRtrIfTxV6PktsHigh32_Type())
vRtrIfTxV6PktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6PktsHigh32.setStatus(_A)
_VRtrIfTxV6Bytes_Type=Counter64
_VRtrIfTxV6Bytes_Object=MibTableColumn
vRtrIfTxV6Bytes=_VRtrIfTxV6Bytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,55),_VRtrIfTxV6Bytes_Type())
vRtrIfTxV6Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6Bytes.setStatus(_A)
_VRtrIfTxV6BytesLow32_Type=Counter32
_VRtrIfTxV6BytesLow32_Object=MibTableColumn
vRtrIfTxV6BytesLow32=_VRtrIfTxV6BytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,56),_VRtrIfTxV6BytesLow32_Type())
vRtrIfTxV6BytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6BytesLow32.setStatus(_A)
_VRtrIfTxV6BytesHigh32_Type=Counter32
_VRtrIfTxV6BytesHigh32_Object=MibTableColumn
vRtrIfTxV6BytesHigh32=_VRtrIfTxV6BytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,57),_VRtrIfTxV6BytesHigh32_Type())
vRtrIfTxV6BytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6BytesHigh32.setStatus(_A)
_VRtrIfTxV4DiscardPkts_Type=Counter64
_VRtrIfTxV4DiscardPkts_Object=MibTableColumn
vRtrIfTxV4DiscardPkts=_VRtrIfTxV4DiscardPkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,58),_VRtrIfTxV4DiscardPkts_Type())
vRtrIfTxV4DiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardPkts.setStatus(_A)
_VRtrIfTxV4DiscardPktsLow32_Type=Counter32
_VRtrIfTxV4DiscardPktsLow32_Object=MibTableColumn
vRtrIfTxV4DiscardPktsLow32=_VRtrIfTxV4DiscardPktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,59),_VRtrIfTxV4DiscardPktsLow32_Type())
vRtrIfTxV4DiscardPktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardPktsLow32.setStatus(_A)
_VRtrIfTxV4DiscardPktsHigh32_Type=Counter32
_VRtrIfTxV4DiscardPktsHigh32_Object=MibTableColumn
vRtrIfTxV4DiscardPktsHigh32=_VRtrIfTxV4DiscardPktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,60),_VRtrIfTxV4DiscardPktsHigh32_Type())
vRtrIfTxV4DiscardPktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardPktsHigh32.setStatus(_A)
_VRtrIfTxV4DiscardBytes_Type=Counter64
_VRtrIfTxV4DiscardBytes_Object=MibTableColumn
vRtrIfTxV4DiscardBytes=_VRtrIfTxV4DiscardBytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,61),_VRtrIfTxV4DiscardBytes_Type())
vRtrIfTxV4DiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardBytes.setStatus(_A)
_VRtrIfTxV4DiscardBytesLow32_Type=Counter32
_VRtrIfTxV4DiscardBytesLow32_Object=MibTableColumn
vRtrIfTxV4DiscardBytesLow32=_VRtrIfTxV4DiscardBytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,62),_VRtrIfTxV4DiscardBytesLow32_Type())
vRtrIfTxV4DiscardBytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardBytesLow32.setStatus(_A)
_VRtrIfTxV4DiscardBytesHigh32_Type=Counter32
_VRtrIfTxV4DiscardBytesHigh32_Object=MibTableColumn
vRtrIfTxV4DiscardBytesHigh32=_VRtrIfTxV4DiscardBytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,63),_VRtrIfTxV4DiscardBytesHigh32_Type())
vRtrIfTxV4DiscardBytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV4DiscardBytesHigh32.setStatus(_A)
_VRtrIfTxV6DiscardPkts_Type=Counter64
_VRtrIfTxV6DiscardPkts_Object=MibTableColumn
vRtrIfTxV6DiscardPkts=_VRtrIfTxV6DiscardPkts_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,64),_VRtrIfTxV6DiscardPkts_Type())
vRtrIfTxV6DiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardPkts.setStatus(_A)
_VRtrIfTxV6DiscardPktsLow32_Type=Counter32
_VRtrIfTxV6DiscardPktsLow32_Object=MibTableColumn
vRtrIfTxV6DiscardPktsLow32=_VRtrIfTxV6DiscardPktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,65),_VRtrIfTxV6DiscardPktsLow32_Type())
vRtrIfTxV6DiscardPktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardPktsLow32.setStatus(_A)
_VRtrIfTxV6DiscardPktsHigh32_Type=Counter32
_VRtrIfTxV6DiscardPktsHigh32_Object=MibTableColumn
vRtrIfTxV6DiscardPktsHigh32=_VRtrIfTxV6DiscardPktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,66),_VRtrIfTxV6DiscardPktsHigh32_Type())
vRtrIfTxV6DiscardPktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardPktsHigh32.setStatus(_A)
_VRtrIfTxV6DiscardBytes_Type=Counter64
_VRtrIfTxV6DiscardBytes_Object=MibTableColumn
vRtrIfTxV6DiscardBytes=_VRtrIfTxV6DiscardBytes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,67),_VRtrIfTxV6DiscardBytes_Type())
vRtrIfTxV6DiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardBytes.setStatus(_A)
_VRtrIfTxV6DiscardBytesLow32_Type=Counter32
_VRtrIfTxV6DiscardBytesLow32_Object=MibTableColumn
vRtrIfTxV6DiscardBytesLow32=_VRtrIfTxV6DiscardBytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,68),_VRtrIfTxV6DiscardBytesLow32_Type())
vRtrIfTxV6DiscardBytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardBytesLow32.setStatus(_A)
_VRtrIfTxV6DiscardBytesHigh32_Type=Counter32
_VRtrIfTxV6DiscardBytesHigh32_Object=MibTableColumn
vRtrIfTxV6DiscardBytesHigh32=_VRtrIfTxV6DiscardBytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,69),_VRtrIfTxV6DiscardBytesHigh32_Type())
vRtrIfTxV6DiscardBytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxV6DiscardBytesHigh32.setStatus(_A)
_VRtrIfIpReasV6FragPktsRcvd_Type=Counter64
_VRtrIfIpReasV6FragPktsRcvd_Object=MibTableColumn
vRtrIfIpReasV6FragPktsRcvd=_VRtrIfIpReasV6FragPktsRcvd_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,70),_VRtrIfIpReasV6FragPktsRcvd_Type())
vRtrIfIpReasV6FragPktsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsRcvd.setStatus(_A)
_VRtrIfIpReasV6FragPktsRcvdLow32_Type=Counter32
_VRtrIfIpReasV6FragPktsRcvdLow32_Object=MibTableColumn
vRtrIfIpReasV6FragPktsRcvdLow32=_VRtrIfIpReasV6FragPktsRcvdLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,71),_VRtrIfIpReasV6FragPktsRcvdLow32_Type())
vRtrIfIpReasV6FragPktsRcvdLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsRcvdLow32.setStatus(_A)
_VRtrIfIpReasV6FragPktsRcvdHigh32_Type=Counter32
_VRtrIfIpReasV6FragPktsRcvdHigh32_Object=MibTableColumn
vRtrIfIpReasV6FragPktsRcvdHigh32=_VRtrIfIpReasV6FragPktsRcvdHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,72),_VRtrIfIpReasV6FragPktsRcvdHigh32_Type())
vRtrIfIpReasV6FragPktsRcvdHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsRcvdHigh32.setStatus(_A)
_VRtrIfIpReasV6FragBytesRcvd_Type=Counter64
_VRtrIfIpReasV6FragBytesRcvd_Object=MibTableColumn
vRtrIfIpReasV6FragBytesRcvd=_VRtrIfIpReasV6FragBytesRcvd_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,73),_VRtrIfIpReasV6FragBytesRcvd_Type())
vRtrIfIpReasV6FragBytesRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesRcvd.setStatus(_A)
_VRtrIfIpReasV6FragBytesRcvdL32_Type=Counter32
_VRtrIfIpReasV6FragBytesRcvdL32_Object=MibTableColumn
vRtrIfIpReasV6FragBytesRcvdL32=_VRtrIfIpReasV6FragBytesRcvdL32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,74),_VRtrIfIpReasV6FragBytesRcvdL32_Type())
vRtrIfIpReasV6FragBytesRcvdL32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesRcvdL32.setStatus(_A)
_VRtrIfIpReasV6FragBytesRcvdH32_Type=Counter32
_VRtrIfIpReasV6FragBytesRcvdH32_Object=MibTableColumn
vRtrIfIpReasV6FragBytesRcvdH32=_VRtrIfIpReasV6FragBytesRcvdH32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,75),_VRtrIfIpReasV6FragBytesRcvdH32_Type())
vRtrIfIpReasV6FragBytesRcvdH32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesRcvdH32.setStatus(_A)
_VRtrIfIpReasV6FragPktsReas_Type=Counter64
_VRtrIfIpReasV6FragPktsReas_Object=MibTableColumn
vRtrIfIpReasV6FragPktsReas=_VRtrIfIpReasV6FragPktsReas_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,76),_VRtrIfIpReasV6FragPktsReas_Type())
vRtrIfIpReasV6FragPktsReas.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsReas.setStatus(_A)
_VRtrIfIpReasV6FragPktsReasLow32_Type=Counter32
_VRtrIfIpReasV6FragPktsReasLow32_Object=MibTableColumn
vRtrIfIpReasV6FragPktsReasLow32=_VRtrIfIpReasV6FragPktsReasLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,77),_VRtrIfIpReasV6FragPktsReasLow32_Type())
vRtrIfIpReasV6FragPktsReasLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsReasLow32.setStatus(_A)
_VRtrIfIpReasV6FragPktsReasHigh32_Type=Counter32
_VRtrIfIpReasV6FragPktsReasHigh32_Object=MibTableColumn
vRtrIfIpReasV6FragPktsReasHigh32=_VRtrIfIpReasV6FragPktsReasHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,78),_VRtrIfIpReasV6FragPktsReasHigh32_Type())
vRtrIfIpReasV6FragPktsReasHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragPktsReasHigh32.setStatus(_A)
_VRtrIfIpReasV6FragBytesReas_Type=Counter64
_VRtrIfIpReasV6FragBytesReas_Object=MibTableColumn
vRtrIfIpReasV6FragBytesReas=_VRtrIfIpReasV6FragBytesReas_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,79),_VRtrIfIpReasV6FragBytesReas_Type())
vRtrIfIpReasV6FragBytesReas.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesReas.setStatus(_A)
_VRtrIfIpReasV6FragBytesReasL32_Type=Counter32
_VRtrIfIpReasV6FragBytesReasL32_Object=MibTableColumn
vRtrIfIpReasV6FragBytesReasL32=_VRtrIfIpReasV6FragBytesReasL32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,80),_VRtrIfIpReasV6FragBytesReasL32_Type())
vRtrIfIpReasV6FragBytesReasL32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesReasL32.setStatus(_A)
_VRtrIfIpReasV6FragBytesReasH32_Type=Counter32
_VRtrIfIpReasV6FragBytesReasH32_Object=MibTableColumn
vRtrIfIpReasV6FragBytesReasH32=_VRtrIfIpReasV6FragBytesReasH32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,81),_VRtrIfIpReasV6FragBytesReasH32_Type())
vRtrIfIpReasV6FragBytesReasH32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragBytesReasH32.setStatus(_A)
_VRtrIfIpReasV6FragReasErrors_Type=Counter64
_VRtrIfIpReasV6FragReasErrors_Object=MibTableColumn
vRtrIfIpReasV6FragReasErrors=_VRtrIfIpReasV6FragReasErrors_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,82),_VRtrIfIpReasV6FragReasErrors_Type())
vRtrIfIpReasV6FragReasErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragReasErrors.setStatus(_A)
_VRtrIfIpReasV6FragReasErrorsL32_Type=Counter32
_VRtrIfIpReasV6FragReasErrorsL32_Object=MibTableColumn
vRtrIfIpReasV6FragReasErrorsL32=_VRtrIfIpReasV6FragReasErrorsL32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,83),_VRtrIfIpReasV6FragReasErrorsL32_Type())
vRtrIfIpReasV6FragReasErrorsL32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragReasErrorsL32.setStatus(_A)
_VRtrIfIpReasV6FragReasErrorsH32_Type=Counter32
_VRtrIfIpReasV6FragReasErrorsH32_Object=MibTableColumn
vRtrIfIpReasV6FragReasErrorsH32=_VRtrIfIpReasV6FragReasErrorsH32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,84),_VRtrIfIpReasV6FragReasErrorsH32_Type())
vRtrIfIpReasV6FragReasErrorsH32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragReasErrorsH32.setStatus(_A)
_VRtrIfIpReasV6FragDisc_Type=Counter64
_VRtrIfIpReasV6FragDisc_Object=MibTableColumn
vRtrIfIpReasV6FragDisc=_VRtrIfIpReasV6FragDisc_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,85),_VRtrIfIpReasV6FragDisc_Type())
vRtrIfIpReasV6FragDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragDisc.setStatus(_A)
_VRtrIfIpReasV6FragDiscLow32_Type=Counter32
_VRtrIfIpReasV6FragDiscLow32_Object=MibTableColumn
vRtrIfIpReasV6FragDiscLow32=_VRtrIfIpReasV6FragDiscLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,86),_VRtrIfIpReasV6FragDiscLow32_Type())
vRtrIfIpReasV6FragDiscLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragDiscLow32.setStatus(_A)
_VRtrIfIpReasV6FragDiscHigh32_Type=Counter32
_VRtrIfIpReasV6FragDiscHigh32_Object=MibTableColumn
vRtrIfIpReasV6FragDiscHigh32=_VRtrIfIpReasV6FragDiscHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,87),_VRtrIfIpReasV6FragDiscHigh32_Type())
vRtrIfIpReasV6FragDiscHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6FragDiscHigh32.setStatus(_A)
_VRtrIfIpReasV6OutBufRes_Type=Counter64
_VRtrIfIpReasV6OutBufRes_Object=MibTableColumn
vRtrIfIpReasV6OutBufRes=_VRtrIfIpReasV6OutBufRes_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,88),_VRtrIfIpReasV6OutBufRes_Type())
vRtrIfIpReasV6OutBufRes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6OutBufRes.setStatus(_A)
_VRtrIfIpReasV6OutBufResLow32_Type=Counter32
_VRtrIfIpReasV6OutBufResLow32_Object=MibTableColumn
vRtrIfIpReasV6OutBufResLow32=_VRtrIfIpReasV6OutBufResLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,89),_VRtrIfIpReasV6OutBufResLow32_Type())
vRtrIfIpReasV6OutBufResLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6OutBufResLow32.setStatus(_A)
_VRtrIfIpReasV6OutBufResHigh32_Type=Counter32
_VRtrIfIpReasV6OutBufResHigh32_Object=MibTableColumn
vRtrIfIpReasV6OutBufResHigh32=_VRtrIfIpReasV6OutBufResHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,90),_VRtrIfIpReasV6OutBufResHigh32_Type())
vRtrIfIpReasV6OutBufResHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6OutBufResHigh32.setStatus(_A)
_VRtrIfIpReasV6PktsRx_Type=Counter64
_VRtrIfIpReasV6PktsRx_Object=MibTableColumn
vRtrIfIpReasV6PktsRx=_VRtrIfIpReasV6PktsRx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,91),_VRtrIfIpReasV6PktsRx_Type())
vRtrIfIpReasV6PktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsRx.setStatus(_A)
_VRtrIfIpReasV6PktsRxLow32_Type=Counter32
_VRtrIfIpReasV6PktsRxLow32_Object=MibTableColumn
vRtrIfIpReasV6PktsRxLow32=_VRtrIfIpReasV6PktsRxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,92),_VRtrIfIpReasV6PktsRxLow32_Type())
vRtrIfIpReasV6PktsRxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsRxLow32.setStatus(_A)
_VRtrIfIpReasV6PktsRxHigh32_Type=Counter32
_VRtrIfIpReasV6PktsRxHigh32_Object=MibTableColumn
vRtrIfIpReasV6PktsRxHigh32=_VRtrIfIpReasV6PktsRxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,93),_VRtrIfIpReasV6PktsRxHigh32_Type())
vRtrIfIpReasV6PktsRxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsRxHigh32.setStatus(_A)
_VRtrIfIpReasV6BytesRx_Type=Counter64
_VRtrIfIpReasV6BytesRx_Object=MibTableColumn
vRtrIfIpReasV6BytesRx=_VRtrIfIpReasV6BytesRx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,94),_VRtrIfIpReasV6BytesRx_Type())
vRtrIfIpReasV6BytesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesRx.setStatus(_A)
_VRtrIfIpReasV6BytesRxLow32_Type=Counter32
_VRtrIfIpReasV6BytesRxLow32_Object=MibTableColumn
vRtrIfIpReasV6BytesRxLow32=_VRtrIfIpReasV6BytesRxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,95),_VRtrIfIpReasV6BytesRxLow32_Type())
vRtrIfIpReasV6BytesRxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesRxLow32.setStatus(_A)
_VRtrIfIpReasV6BytesRxHigh32_Type=Counter32
_VRtrIfIpReasV6BytesRxHigh32_Object=MibTableColumn
vRtrIfIpReasV6BytesRxHigh32=_VRtrIfIpReasV6BytesRxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,96),_VRtrIfIpReasV6BytesRxHigh32_Type())
vRtrIfIpReasV6BytesRxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesRxHigh32.setStatus(_A)
_VRtrIfIpReasV6PktsTx_Type=Counter64
_VRtrIfIpReasV6PktsTx_Object=MibTableColumn
vRtrIfIpReasV6PktsTx=_VRtrIfIpReasV6PktsTx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,97),_VRtrIfIpReasV6PktsTx_Type())
vRtrIfIpReasV6PktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsTx.setStatus(_A)
_VRtrIfIpReasV6PktsTxLow32_Type=Counter32
_VRtrIfIpReasV6PktsTxLow32_Object=MibTableColumn
vRtrIfIpReasV6PktsTxLow32=_VRtrIfIpReasV6PktsTxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,98),_VRtrIfIpReasV6PktsTxLow32_Type())
vRtrIfIpReasV6PktsTxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsTxLow32.setStatus(_A)
_VRtrIfIpReasV6PktsTxHigh32_Type=Counter32
_VRtrIfIpReasV6PktsTxHigh32_Object=MibTableColumn
vRtrIfIpReasV6PktsTxHigh32=_VRtrIfIpReasV6PktsTxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,99),_VRtrIfIpReasV6PktsTxHigh32_Type())
vRtrIfIpReasV6PktsTxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6PktsTxHigh32.setStatus(_A)
_VRtrIfIpReasV6BytesTx_Type=Counter64
_VRtrIfIpReasV6BytesTx_Object=MibTableColumn
vRtrIfIpReasV6BytesTx=_VRtrIfIpReasV6BytesTx_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,100),_VRtrIfIpReasV6BytesTx_Type())
vRtrIfIpReasV6BytesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesTx.setStatus(_A)
_VRtrIfIpReasV6BytesTxLow32_Type=Counter32
_VRtrIfIpReasV6BytesTxLow32_Object=MibTableColumn
vRtrIfIpReasV6BytesTxLow32=_VRtrIfIpReasV6BytesTxLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,101),_VRtrIfIpReasV6BytesTxLow32_Type())
vRtrIfIpReasV6BytesTxLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesTxLow32.setStatus(_A)
_VRtrIfIpReasV6BytesTxHigh32_Type=Counter32
_VRtrIfIpReasV6BytesTxHigh32_Object=MibTableColumn
vRtrIfIpReasV6BytesTxHigh32=_VRtrIfIpReasV6BytesTxHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,102),_VRtrIfIpReasV6BytesTxHigh32_Type())
vRtrIfIpReasV6BytesTxHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfIpReasV6BytesTxHigh32.setStatus(_A)
_VRtrIfSpeed_Type=Counter64
_VRtrIfSpeed_Object=MibTableColumn
vRtrIfSpeed=_VRtrIfSpeed_Object((1,3,6,1,4,1,7483,6,1,2,3,54,1,103),_VRtrIfSpeed_Type())
vRtrIfSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfSpeed.setStatus(_A)
_VRtrIfExtTable_Object=MibTable
vRtrIfExtTable=_VRtrIfExtTable_Object((1,3,6,1,4,1,7483,6,1,2,3,61))
if mibBuilder.loadTexts:vRtrIfExtTable.setStatus(_A)
_VRtrIfExtEntry_Object=MibTableRow
vRtrIfExtEntry=_VRtrIfExtEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1))
if mibBuilder.loadTexts:vRtrIfExtEntry.setStatus(_A)
class _VRtrIfLsrIpLoadBalancing_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('system',0),('label-only',1),('label-ip',2),('ip-only',3)))
_VRtrIfLsrIpLoadBalancing_Type.__name__=_F
_VRtrIfLsrIpLoadBalancing_Object=MibTableColumn
vRtrIfLsrIpLoadBalancing=_VRtrIfLsrIpLoadBalancing_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,1),_VRtrIfLsrIpLoadBalancing_Type())
vRtrIfLsrIpLoadBalancing.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfLsrIpLoadBalancing.setStatus(_A)
class _VRtrIfIngressIpv4Flowspec_Type(TruthValue):defaultValue=2
_VRtrIfIngressIpv4Flowspec_Type.__name__=_E
_VRtrIfIngressIpv4Flowspec_Object=MibTableColumn
vRtrIfIngressIpv4Flowspec=_VRtrIfIngressIpv4Flowspec_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,2),_VRtrIfIngressIpv4Flowspec_Type())
vRtrIfIngressIpv4Flowspec.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIngressIpv4Flowspec.setStatus(_A)
class _VRtrIfInfo_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,257))
_VRtrIfInfo_Type.__name__=_q
_VRtrIfInfo_Object=MibTableColumn
vRtrIfInfo=_VRtrIfInfo_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,3),_VRtrIfInfo_Type())
vRtrIfInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfInfo.setStatus(_A)
class _VRtrIfInfoEncrypted_Type(TruthValue):defaultValue=1
_VRtrIfInfoEncrypted_Type.__name__=_E
_VRtrIfInfoEncrypted_Object=MibTableColumn
vRtrIfInfoEncrypted=_VRtrIfInfoEncrypted_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,4),_VRtrIfInfoEncrypted_Type())
vRtrIfInfoEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfInfoEncrypted.setStatus(_M)
class _VRtrIfQosRouteLookup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_X,0),(_A3,1),('source',2)))
_VRtrIfQosRouteLookup_Type.__name__=_F
_VRtrIfQosRouteLookup_Object=MibTableColumn
vRtrIfQosRouteLookup=_VRtrIfQosRouteLookup_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,5),_VRtrIfQosRouteLookup_Type())
vRtrIfQosRouteLookup.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfQosRouteLookup.setStatus(_A)
class _VRtrIfIpv6QosRouteLookup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_A3,1)))
_VRtrIfIpv6QosRouteLookup_Type.__name__=_F
_VRtrIfIpv6QosRouteLookup_Object=MibTableColumn
vRtrIfIpv6QosRouteLookup=_VRtrIfIpv6QosRouteLookup_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,6),_VRtrIfIpv6QosRouteLookup_Type())
vRtrIfIpv6QosRouteLookup.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIpv6QosRouteLookup.setStatus(_A)
_VRtrIfStatusString_Type=DisplayString
_VRtrIfStatusString_Object=MibTableColumn
vRtrIfStatusString=_VRtrIfStatusString_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,7),_VRtrIfStatusString_Type())
vRtrIfStatusString.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfStatusString.setStatus(_A)
class _VRtrIfIpv6uRPFCheckState_Type(TmnxEnabledDisabled):defaultValue=2
_VRtrIfIpv6uRPFCheckState_Type.__name__=_k
_VRtrIfIpv6uRPFCheckState_Object=MibTableColumn
vRtrIfIpv6uRPFCheckState=_VRtrIfIpv6uRPFCheckState_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,8),_VRtrIfIpv6uRPFCheckState_Type())
vRtrIfIpv6uRPFCheckState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIpv6uRPFCheckState.setStatus(_A)
class _VRtrIfIpv6uRPFCheckMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_VRtrIfIpv6uRPFCheckMode_Type.__name__=_F
_VRtrIfIpv6uRPFCheckMode_Object=MibTableColumn
vRtrIfIpv6uRPFCheckMode=_VRtrIfIpv6uRPFCheckMode_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,9),_VRtrIfIpv6uRPFCheckMode_Type())
vRtrIfIpv6uRPFCheckMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfIpv6uRPFCheckMode.setStatus(_A)
class _VRtrIfTmsOffRampVprn_Type(TmnxServId):defaultValue=0
_VRtrIfTmsOffRampVprn_Type.__name__=_a
_VRtrIfTmsOffRampVprn_Object=MibTableColumn
vRtrIfTmsOffRampVprn=_VRtrIfTmsOffRampVprn_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,10),_VRtrIfTmsOffRampVprn_Type())
vRtrIfTmsOffRampVprn.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfTmsOffRampVprn.setStatus(_A)
class _VRtrIfTmsMgmtVprn_Type(TmnxServId):defaultValue=0
_VRtrIfTmsMgmtVprn_Type.__name__=_a
_VRtrIfTmsMgmtVprn_Object=MibTableColumn
vRtrIfTmsMgmtVprn=_VRtrIfTmsMgmtVprn_Object((1,3,6,1,4,1,7483,6,1,2,3,61,1,11),_VRtrIfTmsMgmtVprn_Type())
vRtrIfTmsMgmtVprn.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfTmsMgmtVprn.setStatus(_A)
_TnVRtrMobGatewayObjs_ObjectIdentity=ObjectIdentity
tnVRtrMobGatewayObjs=_TnVRtrMobGatewayObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,3,69))
_VRtrIfBfdExtTableLastChanged_Type=TimeStamp
_VRtrIfBfdExtTableLastChanged_Object=MibScalar
vRtrIfBfdExtTableLastChanged=_VRtrIfBfdExtTableLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,3,70),_VRtrIfBfdExtTableLastChanged_Type())
vRtrIfBfdExtTableLastChanged.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdExtTableLastChanged.setStatus(_A)
_VRtrIfBfdExtTable_Object=MibTable
vRtrIfBfdExtTable=_VRtrIfBfdExtTable_Object((1,3,6,1,4,1,7483,6,1,2,3,71))
if mibBuilder.loadTexts:vRtrIfBfdExtTable.setStatus(_A)
_VRtrIfBfdExtEntry_Object=MibTableRow
vRtrIfBfdExtEntry=_VRtrIfBfdExtEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1))
vRtrIfBfdExtEntry.setIndexNames((0,_K,_L),(0,_G,_P),(0,_G,_U),(0,_G,_A4))
if mibBuilder.loadTexts:vRtrIfBfdExtEntry.setStatus(_A)
_VRtrIfBfdExtAddressType_Type=InetAddressType
_VRtrIfBfdExtAddressType_Object=MibTableColumn
vRtrIfBfdExtAddressType=_VRtrIfBfdExtAddressType_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,1),_VRtrIfBfdExtAddressType_Type())
vRtrIfBfdExtAddressType.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdExtAddressType.setStatus(_A)
_VRtrIfBfdExtAdminState_Type=TmnxAdminState
_VRtrIfBfdExtAdminState_Object=MibTableColumn
vRtrIfBfdExtAdminState=_VRtrIfBfdExtAdminState_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,2),_VRtrIfBfdExtAdminState_Type())
vRtrIfBfdExtAdminState.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtAdminState.setStatus(_A)
class _VRtrIfBfdExtTransmitInterval_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_VRtrIfBfdExtTransmitInterval_Type.__name__=_D
_VRtrIfBfdExtTransmitInterval_Object=MibTableColumn
vRtrIfBfdExtTransmitInterval=_VRtrIfBfdExtTransmitInterval_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,3),_VRtrIfBfdExtTransmitInterval_Type())
vRtrIfBfdExtTransmitInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtTransmitInterval.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdExtTransmitInterval.setUnits(_J)
class _VRtrIfBfdExtReceiveInterval_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100000))
_VRtrIfBfdExtReceiveInterval_Type.__name__=_D
_VRtrIfBfdExtReceiveInterval_Object=MibTableColumn
vRtrIfBfdExtReceiveInterval=_VRtrIfBfdExtReceiveInterval_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,4),_VRtrIfBfdExtReceiveInterval_Type())
vRtrIfBfdExtReceiveInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtReceiveInterval.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdExtReceiveInterval.setUnits(_J)
class _VRtrIfBfdExtMultiplier_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,20))
_VRtrIfBfdExtMultiplier_Type.__name__=_D
_VRtrIfBfdExtMultiplier_Object=MibTableColumn
vRtrIfBfdExtMultiplier=_VRtrIfBfdExtMultiplier_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,5),_VRtrIfBfdExtMultiplier_Type())
vRtrIfBfdExtMultiplier.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtMultiplier.setStatus(_A)
class _VRtrIfBfdExtEchoInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(100,100000))
_VRtrIfBfdExtEchoInterval_Type.__name__=_D
_VRtrIfBfdExtEchoInterval_Object=MibTableColumn
vRtrIfBfdExtEchoInterval=_VRtrIfBfdExtEchoInterval_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,6),_VRtrIfBfdExtEchoInterval_Type())
vRtrIfBfdExtEchoInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtEchoInterval.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdExtEchoInterval.setUnits(_J)
class _VRtrIfBfdExtType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cpmNp',1),('auto',2),('iomHw',3)))
_VRtrIfBfdExtType_Type.__name__=_F
_VRtrIfBfdExtType_Object=MibTableColumn
vRtrIfBfdExtType=_VRtrIfBfdExtType_Object((1,3,6,1,4,1,7483,6,1,2,3,71,1,7),_VRtrIfBfdExtType_Type())
vRtrIfBfdExtType.setMaxAccess(_N)
if mibBuilder.loadTexts:vRtrIfBfdExtType.setStatus(_A)
_VRtrIfStatsExtTable_Object=MibTable
vRtrIfStatsExtTable=_VRtrIfStatsExtTable_Object((1,3,6,1,4,1,7483,6,1,2,3,74))
if mibBuilder.loadTexts:vRtrIfStatsExtTable.setStatus(_A)
_VRtrIfStatsExtEntry_Object=MibTableRow
vRtrIfStatsExtEntry=_VRtrIfStatsExtEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1))
if mibBuilder.loadTexts:vRtrIfStatsExtEntry.setStatus(_A)
_VRtrIfTxPkts_Type=Counter64
_VRtrIfTxPkts_Object=MibTableColumn
vRtrIfTxPkts=_VRtrIfTxPkts_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,1),_VRtrIfTxPkts_Type())
vRtrIfTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxPkts.setStatus(_A)
_VRtrIfTxPktsLow32_Type=Counter32
_VRtrIfTxPktsLow32_Object=MibTableColumn
vRtrIfTxPktsLow32=_VRtrIfTxPktsLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,2),_VRtrIfTxPktsLow32_Type())
vRtrIfTxPktsLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxPktsLow32.setStatus(_A)
_VRtrIfTxPktsHigh32_Type=Counter32
_VRtrIfTxPktsHigh32_Object=MibTableColumn
vRtrIfTxPktsHigh32=_VRtrIfTxPktsHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,3),_VRtrIfTxPktsHigh32_Type())
vRtrIfTxPktsHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxPktsHigh32.setStatus(_A)
_VRtrIfTxBytes_Type=Counter64
_VRtrIfTxBytes_Object=MibTableColumn
vRtrIfTxBytes=_VRtrIfTxBytes_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,4),_VRtrIfTxBytes_Type())
vRtrIfTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxBytes.setStatus(_A)
_VRtrIfTxBytesLow32_Type=Counter32
_VRtrIfTxBytesLow32_Object=MibTableColumn
vRtrIfTxBytesLow32=_VRtrIfTxBytesLow32_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,5),_VRtrIfTxBytesLow32_Type())
vRtrIfTxBytesLow32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxBytesLow32.setStatus(_A)
_VRtrIfTxBytesHigh32_Type=Counter32
_VRtrIfTxBytesHigh32_Object=MibTableColumn
vRtrIfTxBytesHigh32=_VRtrIfTxBytesHigh32_Object((1,3,6,1,4,1,7483,6,1,2,3,74,1,6),_VRtrIfTxBytesHigh32_Type())
vRtrIfTxBytesHigh32.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfTxBytesHigh32.setStatus(_A)
_VRtrIfQosTable_Object=MibTable
vRtrIfQosTable=_VRtrIfQosTable_Object((1,3,6,1,4,1,7483,6,1,2,3,78))
if mibBuilder.loadTexts:vRtrIfQosTable.setStatus(_A)
_VRtrIfQosEntry_Object=MibTableRow
vRtrIfQosEntry=_VRtrIfQosEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,78,1))
if mibBuilder.loadTexts:vRtrIfQosEntry.setStatus(_A)
class _VRtrIfQosNetworkPolicyId_Type(TNetworkPolicyID):defaultValue=1
_VRtrIfQosNetworkPolicyId_Type.__name__=_h
_VRtrIfQosNetworkPolicyId_Object=MibTableColumn
vRtrIfQosNetworkPolicyId=_VRtrIfQosNetworkPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,3,78,1,1),_VRtrIfQosNetworkPolicyId_Type())
vRtrIfQosNetworkPolicyId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrIfQosNetworkPolicyId.setStatus(_A)
_VRtrIfBfdSessExtTable_Object=MibTable
vRtrIfBfdSessExtTable=_VRtrIfBfdSessExtTable_Object((1,3,6,1,4,1,7483,6,1,2,3,92))
if mibBuilder.loadTexts:vRtrIfBfdSessExtTable.setStatus(_A)
_VRtrIfBfdSessExtEntry_Object=MibTableRow
vRtrIfBfdSessExtEntry=_VRtrIfBfdSessExtEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1))
vRtrIfBfdSessExtEntry.setIndexNames((0,_K,_L),(0,_G,_A5),(0,_G,_A6),(0,_G,_P),(0,_G,_U),(0,_G,_A7),(0,_G,_A8),(0,_G,_A9),(0,_G,_AA))
if mibBuilder.loadTexts:vRtrIfBfdSessExtEntry.setStatus(_A)
class _VRtrIfBfdSessExtLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('pointToPoint',0),('head',1),('tail',2),('client',3),('ccOnly',4),('ccWithCv',5),('microBfd',6)))
_VRtrIfBfdSessExtLinkType_Type.__name__=_F
_VRtrIfBfdSessExtLinkType_Object=MibTableColumn
vRtrIfBfdSessExtLinkType=_VRtrIfBfdSessExtLinkType_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,1),_VRtrIfBfdSessExtLinkType_Type())
vRtrIfBfdSessExtLinkType.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLinkType.setStatus(_A)
_VRtrIfBfdSessExtRxInfoId_Type=Unsigned32
_VRtrIfBfdSessExtRxInfoId_Object=MibTableColumn
vRtrIfBfdSessExtRxInfoId=_VRtrIfBfdSessExtRxInfoId_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,2),_VRtrIfBfdSessExtRxInfoId_Type())
vRtrIfBfdSessExtRxInfoId.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRxInfoId.setStatus(_A)
_VRtrIfBfdSessExtLclAddrType_Type=InetAddressType
_VRtrIfBfdSessExtLclAddrType_Object=MibTableColumn
vRtrIfBfdSessExtLclAddrType=_VRtrIfBfdSessExtLclAddrType_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,3),_VRtrIfBfdSessExtLclAddrType_Type())
vRtrIfBfdSessExtLclAddrType.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclAddrType.setStatus(_A)
class _VRtrIfBfdSessExtLclAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_VRtrIfBfdSessExtLclAddr_Type.__name__=_O
_VRtrIfBfdSessExtLclAddr_Object=MibTableColumn
vRtrIfBfdSessExtLclAddr=_VRtrIfBfdSessExtLclAddr_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,4),_VRtrIfBfdSessExtLclAddr_Type())
vRtrIfBfdSessExtLclAddr.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclAddr.setStatus(_A)
_VRtrIfBfdSessExtRemAddrType_Type=InetAddressType
_VRtrIfBfdSessExtRemAddrType_Object=MibTableColumn
vRtrIfBfdSessExtRemAddrType=_VRtrIfBfdSessExtRemAddrType_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,5),_VRtrIfBfdSessExtRemAddrType_Type())
vRtrIfBfdSessExtRemAddrType.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemAddrType.setStatus(_A)
class _VRtrIfBfdSessExtRemAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_VRtrIfBfdSessExtRemAddr_Type.__name__=_O
_VRtrIfBfdSessExtRemAddr_Object=MibTableColumn
vRtrIfBfdSessExtRemAddr=_VRtrIfBfdSessExtRemAddr_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,6),_VRtrIfBfdSessExtRemAddr_Type())
vRtrIfBfdSessExtRemAddr.setMaxAccess(_Q)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemAddr.setStatus(_A)
_VRtrIfBfdSessExtOperState_Type=TmnxOperState
_VRtrIfBfdSessExtOperState_Object=MibTableColumn
vRtrIfBfdSessExtOperState=_VRtrIfBfdSessExtOperState_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,7),_VRtrIfBfdSessExtOperState_Type())
vRtrIfBfdSessExtOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtOperState.setStatus(_A)
class _VRtrIfBfdSessExtState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Y,0),(_n,1),(_o,2),('up',3)))
_VRtrIfBfdSessExtState_Type.__name__=_F
_VRtrIfBfdSessExtState_Object=MibTableColumn
vRtrIfBfdSessExtState=_VRtrIfBfdSessExtState_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,8),_VRtrIfBfdSessExtState_Type())
vRtrIfBfdSessExtState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtState.setStatus(_A)
class _VRtrIfBfdSessExtOperFlags_Type(Bits):namedValues=NamedValues(*(('noProtocols',0),('noHeartBeat',1),('echoFailed',2),('nbrSignalDown',3),('fwdPlaneReset',4),(_p,5),('nbrAdminDown',6),('adminClear',7),('misConnDefect',8)))
_VRtrIfBfdSessExtOperFlags_Type.__name__=_S
_VRtrIfBfdSessExtOperFlags_Object=MibTableColumn
vRtrIfBfdSessExtOperFlags=_VRtrIfBfdSessExtOperFlags_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,9),_VRtrIfBfdSessExtOperFlags_Type())
vRtrIfBfdSessExtOperFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtOperFlags.setStatus(_A)
_VRtrIfBfdSessExtMesgRecv_Type=Counter32
_VRtrIfBfdSessExtMesgRecv_Object=MibTableColumn
vRtrIfBfdSessExtMesgRecv=_VRtrIfBfdSessExtMesgRecv_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,10),_VRtrIfBfdSessExtMesgRecv_Type())
vRtrIfBfdSessExtMesgRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtMesgRecv.setStatus(_A)
_VRtrIfBfdSessExtMesgSent_Type=Counter32
_VRtrIfBfdSessExtMesgSent_Object=MibTableColumn
vRtrIfBfdSessExtMesgSent=_VRtrIfBfdSessExtMesgSent_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,11),_VRtrIfBfdSessExtMesgSent_Type())
vRtrIfBfdSessExtMesgSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtMesgSent.setStatus(_A)
_VRtrIfBfdSessExtLastDownTime_Type=TimeStamp
_VRtrIfBfdSessExtLastDownTime_Object=MibTableColumn
vRtrIfBfdSessExtLastDownTime=_VRtrIfBfdSessExtLastDownTime_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,12),_VRtrIfBfdSessExtLastDownTime_Type())
vRtrIfBfdSessExtLastDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLastDownTime.setStatus(_A)
_VRtrIfBfdSessExtLastUpTime_Type=TimeStamp
_VRtrIfBfdSessExtLastUpTime_Object=MibTableColumn
vRtrIfBfdSessExtLastUpTime=_VRtrIfBfdSessExtLastUpTime_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,13),_VRtrIfBfdSessExtLastUpTime_Type())
vRtrIfBfdSessExtLastUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLastUpTime.setStatus(_A)
_VRtrIfBfdSessExtUpCount_Type=Counter32
_VRtrIfBfdSessExtUpCount_Object=MibTableColumn
vRtrIfBfdSessExtUpCount=_VRtrIfBfdSessExtUpCount_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,14),_VRtrIfBfdSessExtUpCount_Type())
vRtrIfBfdSessExtUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtUpCount.setStatus(_A)
_VRtrIfBfdSessExtDownCount_Type=Counter32
_VRtrIfBfdSessExtDownCount_Object=MibTableColumn
vRtrIfBfdSessExtDownCount=_VRtrIfBfdSessExtDownCount_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,15),_VRtrIfBfdSessExtDownCount_Type())
vRtrIfBfdSessExtDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtDownCount.setStatus(_A)
_VRtrIfBfdSessExtLclDisc_Type=Unsigned32
_VRtrIfBfdSessExtLclDisc_Object=MibTableColumn
vRtrIfBfdSessExtLclDisc=_VRtrIfBfdSessExtLclDisc_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,16),_VRtrIfBfdSessExtLclDisc_Type())
vRtrIfBfdSessExtLclDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclDisc.setStatus(_A)
_VRtrIfBfdSessExtRemDisc_Type=Unsigned32
_VRtrIfBfdSessExtRemDisc_Object=MibTableColumn
vRtrIfBfdSessExtRemDisc=_VRtrIfBfdSessExtRemDisc_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,17),_VRtrIfBfdSessExtRemDisc_Type())
vRtrIfBfdSessExtRemDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemDisc.setStatus(_A)
class _VRtrIfBfdSessExtProtocols_Type(Bits):namedValues=NamedValues(*(('ospfv2',0),(_l,1),(_m,2),('staticRoute',3),('mcRing',4),(_d,5),(_b,6),('vrrp',7),('srrp',8),('mcep',9),(_c,10),('ipsecTunnel',11),('ospfv3',12),('mcIpsec',13),('mcMobile',14),('mplsTp',15),('lag',16)))
_VRtrIfBfdSessExtProtocols_Type.__name__=_S
_VRtrIfBfdSessExtProtocols_Object=MibTableColumn
vRtrIfBfdSessExtProtocols=_VRtrIfBfdSessExtProtocols_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,18),_VRtrIfBfdSessExtProtocols_Type())
vRtrIfBfdSessExtProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtProtocols.setStatus(_A)
_VRtrIfBfdSessExtTxInterval_Type=Unsigned32
_VRtrIfBfdSessExtTxInterval_Object=MibTableColumn
vRtrIfBfdSessExtTxInterval=_VRtrIfBfdSessExtTxInterval_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,19),_VRtrIfBfdSessExtTxInterval_Type())
vRtrIfBfdSessExtTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTxInterval.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTxInterval.setUnits(_J)
_VRtrIfBfdSessExtRxInterval_Type=Unsigned32
_VRtrIfBfdSessExtRxInterval_Object=MibTableColumn
vRtrIfBfdSessExtRxInterval=_VRtrIfBfdSessExtRxInterval_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,20),_VRtrIfBfdSessExtRxInterval_Type())
vRtrIfBfdSessExtRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRxInterval.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRxInterval.setUnits(_J)
class _VRtrIfBfdSessExtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('iom',1),('cpm',2),('cpmNp',3),('iomHw',4)))
_VRtrIfBfdSessExtType_Type.__name__=_F
_VRtrIfBfdSessExtType_Object=MibTableColumn
vRtrIfBfdSessExtType=_VRtrIfBfdSessExtType_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,21),_VRtrIfBfdSessExtType_Type())
vRtrIfBfdSessExtType.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtType.setStatus(_A)
_VRtrIfBfdSessExtVerMismatch_Type=Counter32
_VRtrIfBfdSessExtVerMismatch_Object=MibTableColumn
vRtrIfBfdSessExtVerMismatch=_VRtrIfBfdSessExtVerMismatch_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,22),_VRtrIfBfdSessExtVerMismatch_Type())
vRtrIfBfdSessExtVerMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtVerMismatch.setStatus(_A)
_VRtrIfBfdSessExtTimeSinceLastRx_Type=Unsigned32
_VRtrIfBfdSessExtTimeSinceLastRx_Object=MibTableColumn
vRtrIfBfdSessExtTimeSinceLastRx=_VRtrIfBfdSessExtTimeSinceLastRx_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,23),_VRtrIfBfdSessExtTimeSinceLastRx_Type())
vRtrIfBfdSessExtTimeSinceLastRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTimeSinceLastRx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTimeSinceLastRx.setUnits(_J)
_VRtrIfBfdSessExtTimeSinceLastTx_Type=Unsigned32
_VRtrIfBfdSessExtTimeSinceLastTx_Object=MibTableColumn
vRtrIfBfdSessExtTimeSinceLastTx=_VRtrIfBfdSessExtTimeSinceLastTx_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,24),_VRtrIfBfdSessExtTimeSinceLastTx_Type())
vRtrIfBfdSessExtTimeSinceLastTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTimeSinceLastTx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtTimeSinceLastTx.setUnits(_J)
_VRtrIfBfdSessExtRemoteLspNum_Type=Unsigned32
_VRtrIfBfdSessExtRemoteLspNum_Object=MibTableColumn
vRtrIfBfdSessExtRemoteLspNum=_VRtrIfBfdSessExtRemoteLspNum_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,25),_VRtrIfBfdSessExtRemoteLspNum_Type())
vRtrIfBfdSessExtRemoteLspNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemoteLspNum.setStatus(_A)
_VRtrIfBfdSessExtRemoteTunnelNum_Type=Unsigned32
_VRtrIfBfdSessExtRemoteTunnelNum_Object=MibTableColumn
vRtrIfBfdSessExtRemoteTunnelNum=_VRtrIfBfdSessExtRemoteTunnelNum_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,26),_VRtrIfBfdSessExtRemoteTunnelNum_Type())
vRtrIfBfdSessExtRemoteTunnelNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemoteTunnelNum.setStatus(_A)
_VRtrIfBfdSessExtRemoteNodeId_Type=TmnxMplsTpNodeID
_VRtrIfBfdSessExtRemoteNodeId_Object=MibTableColumn
vRtrIfBfdSessExtRemoteNodeId=_VRtrIfBfdSessExtRemoteNodeId_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,27),_VRtrIfBfdSessExtRemoteNodeId_Type())
vRtrIfBfdSessExtRemoteNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemoteNodeId.setStatus(_A)
_VRtrIfBfdSessExtRemoteGlobalId_Type=TmnxMplsTpGlobalID
_VRtrIfBfdSessExtRemoteGlobalId_Object=MibTableColumn
vRtrIfBfdSessExtRemoteGlobalId=_VRtrIfBfdSessExtRemoteGlobalId_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,28),_VRtrIfBfdSessExtRemoteGlobalId_Type())
vRtrIfBfdSessExtRemoteGlobalId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemoteGlobalId.setStatus(_A)
_VRtrIfBfdSessExtLspPathTunnelId_Type=Unsigned32
_VRtrIfBfdSessExtLspPathTunnelId_Object=MibTableColumn
vRtrIfBfdSessExtLspPathTunnelId=_VRtrIfBfdSessExtLspPathTunnelId_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,29),_VRtrIfBfdSessExtLspPathTunnelId_Type())
vRtrIfBfdSessExtLspPathTunnelId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLspPathTunnelId.setStatus(_A)
class _VRtrIfBfdSessExtLspPathId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_w,0),('working',1),('protecting',2)))
_VRtrIfBfdSessExtLspPathId_Type.__name__=_F
_VRtrIfBfdSessExtLspPathId_Object=MibTableColumn
vRtrIfBfdSessExtLspPathId=_VRtrIfBfdSessExtLspPathId_Object((1,3,6,1,4,1,7483,6,1,2,3,92,1,30),_VRtrIfBfdSessExtLspPathId_Type())
vRtrIfBfdSessExtLspPathId.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLspPathId.setStatus(_A)
_VRtrIfBfdSessForwardInfoTable_Object=MibTable
vRtrIfBfdSessForwardInfoTable=_VRtrIfBfdSessForwardInfoTable_Object((1,3,6,1,4,1,7483,6,1,2,3,95))
if mibBuilder.loadTexts:vRtrIfBfdSessForwardInfoTable.setStatus(_A)
_VRtrIfBfdSessForwardInfoEntry_Object=MibTableRow
vRtrIfBfdSessForwardInfoEntry=_VRtrIfBfdSessForwardInfoEntry_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1))
if mibBuilder.loadTexts:vRtrIfBfdSessForwardInfoEntry.setStatus(_A)
class _VRtrIfBfdSessExtLclState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Y,0),(_n,1),(_o,2),('up',3)))
_VRtrIfBfdSessExtLclState_Type.__name__=_F
_VRtrIfBfdSessExtLclState_Object=MibTableColumn
vRtrIfBfdSessExtLclState=_VRtrIfBfdSessExtLclState_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,1),_VRtrIfBfdSessExtLclState_Type())
vRtrIfBfdSessExtLclState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclState.setStatus(_A)
class _VRtrIfBfdSessExtLclMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('async',0),('demand',1)))
_VRtrIfBfdSessExtLclMode_Type.__name__=_F
_VRtrIfBfdSessExtLclMode_Object=MibTableColumn
vRtrIfBfdSessExtLclMode=_VRtrIfBfdSessExtLclMode_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,2),_VRtrIfBfdSessExtLclMode_Type())
vRtrIfBfdSessExtLclMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMode.setStatus(_A)
class _VRtrIfBfdSessExtLclDiag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,0),(_AB,1),(_AC,2),(_AD,3),(_AE,4),(_p,5),(_AF,6),(_Y,7),(_AG,8)))
_VRtrIfBfdSessExtLclDiag_Type.__name__=_F
_VRtrIfBfdSessExtLclDiag_Object=MibTableColumn
vRtrIfBfdSessExtLclDiag=_VRtrIfBfdSessExtLclDiag_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,3),_VRtrIfBfdSessExtLclDiag_Type())
vRtrIfBfdSessExtLclDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclDiag.setStatus(_A)
_VRtrIfBfdSessExtLclMinTx_Type=Unsigned32
_VRtrIfBfdSessExtLclMinTx_Object=MibTableColumn
vRtrIfBfdSessExtLclMinTx=_VRtrIfBfdSessExtLclMinTx_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,4),_VRtrIfBfdSessExtLclMinTx_Type())
vRtrIfBfdSessExtLclMinTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMinTx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMinTx.setUnits(_J)
_VRtrIfBfdSessExtLclMinRx_Type=Unsigned32
_VRtrIfBfdSessExtLclMinRx_Object=MibTableColumn
vRtrIfBfdSessExtLclMinRx=_VRtrIfBfdSessExtLclMinRx_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,5),_VRtrIfBfdSessExtLclMinRx_Type())
vRtrIfBfdSessExtLclMinRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMinRx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMinRx.setUnits(_J)
_VRtrIfBfdSessExtLclMult_Type=Unsigned32
_VRtrIfBfdSessExtLclMult_Object=MibTableColumn
vRtrIfBfdSessExtLclMult=_VRtrIfBfdSessExtLclMult_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,6),_VRtrIfBfdSessExtLclMult_Type())
vRtrIfBfdSessExtLclMult.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLclMult.setStatus(_A)
class _VRtrIfBfdSessExtRemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_Y,0),(_n,1),(_o,2),('up',3)))
_VRtrIfBfdSessExtRemState_Type.__name__=_F
_VRtrIfBfdSessExtRemState_Object=MibTableColumn
vRtrIfBfdSessExtRemState=_VRtrIfBfdSessExtRemState_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,7),_VRtrIfBfdSessExtRemState_Type())
vRtrIfBfdSessExtRemState.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemState.setStatus(_A)
class _VRtrIfBfdSessExtRemMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('async',0),('demand',1)))
_VRtrIfBfdSessExtRemMode_Type.__name__=_F
_VRtrIfBfdSessExtRemMode_Object=MibTableColumn
vRtrIfBfdSessExtRemMode=_VRtrIfBfdSessExtRemMode_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,8),_VRtrIfBfdSessExtRemMode_Type())
vRtrIfBfdSessExtRemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMode.setStatus(_A)
class _VRtrIfBfdSessExtRemDiag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,0),(_AB,1),(_AC,2),(_AD,3),(_AE,4),(_p,5),(_AF,6),(_Y,7),(_AG,8)))
_VRtrIfBfdSessExtRemDiag_Type.__name__=_F
_VRtrIfBfdSessExtRemDiag_Object=MibTableColumn
vRtrIfBfdSessExtRemDiag=_VRtrIfBfdSessExtRemDiag_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,9),_VRtrIfBfdSessExtRemDiag_Type())
vRtrIfBfdSessExtRemDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemDiag.setStatus(_A)
_VRtrIfBfdSessExtRemMinTx_Type=Unsigned32
_VRtrIfBfdSessExtRemMinTx_Object=MibTableColumn
vRtrIfBfdSessExtRemMinTx=_VRtrIfBfdSessExtRemMinTx_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,10),_VRtrIfBfdSessExtRemMinTx_Type())
vRtrIfBfdSessExtRemMinTx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMinTx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMinTx.setUnits(_J)
_VRtrIfBfdSessExtRemMinRx_Type=Unsigned32
_VRtrIfBfdSessExtRemMinRx_Object=MibTableColumn
vRtrIfBfdSessExtRemMinRx=_VRtrIfBfdSessExtRemMinRx_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,11),_VRtrIfBfdSessExtRemMinRx_Type())
vRtrIfBfdSessExtRemMinRx.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMinRx.setStatus(_A)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMinRx.setUnits(_J)
_VRtrIfBfdSessExtRemMult_Type=Unsigned32
_VRtrIfBfdSessExtRemMult_Object=MibTableColumn
vRtrIfBfdSessExtRemMult=_VRtrIfBfdSessExtRemMult_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,12),_VRtrIfBfdSessExtRemMult_Type())
vRtrIfBfdSessExtRemMult.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtRemMult.setStatus(_A)
_VRtrIfBfdSessExtLastRecv_Type=TimeStamp
_VRtrIfBfdSessExtLastRecv_Object=MibTableColumn
vRtrIfBfdSessExtLastRecv=_VRtrIfBfdSessExtLastRecv_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,13),_VRtrIfBfdSessExtLastRecv_Type())
vRtrIfBfdSessExtLastRecv.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLastRecv.setStatus(_A)
_VRtrIfBfdSessExtLastSent_Type=TimeStamp
_VRtrIfBfdSessExtLastSent_Object=MibTableColumn
vRtrIfBfdSessExtLastSent=_VRtrIfBfdSessExtLastSent_Object((1,3,6,1,4,1,7483,6,1,2,3,95,1,14),_VRtrIfBfdSessExtLastSent_Type())
vRtrIfBfdSessExtLastSent.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrIfBfdSessExtLastSent.setStatus(_A)
_VRtrConfScalar1_Type=Unsigned32
_VRtrConfScalar1_Object=MibScalar
vRtrConfScalar1=_VRtrConfScalar1_Object((1,3,6,1,4,1,7483,6,1,2,3,101),_VRtrConfScalar1_Type())
vRtrConfScalar1.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrConfScalar1.setStatus(_A)
_VRtrConfScalar2_Type=Unsigned32
_VRtrConfScalar2_Object=MibScalar
vRtrConfScalar2=_VRtrConfScalar2_Object((1,3,6,1,4,1,7483,6,1,2,3,102),_VRtrConfScalar2_Type())
vRtrConfScalar2.setMaxAccess(_B)
if mibBuilder.loadTexts:vRtrConfScalar2.setStatus(_A)
vRtrConfEntry.registerAugmentions((_G,_AH))
vRtrStatEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions((_G,_AI))
vRtrIfExtEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfStatsEntry.registerAugmentions((_G,_AJ))
vRtrIfStatsExtEntry.setIndexNames(*vRtrIfStatsEntry.getIndexNames())
vRtrIfEntry.registerAugmentions((_G,_AK))
vRtrIfQosEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfBfdSessExtEntry.registerAugmentions((_G,_AL))
vRtrIfBfdSessForwardInfoEntry.setIndexNames(*vRtrIfBfdSessExtEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{_z:TmnxVPNId,'TmnxInetAddrState':TmnxInetAddrState,'TDSCPAppId':TDSCPAppId,'TDot1pAppId':TDot1pAppId,'TmnxVrtrSingleSfmOverloadState':TmnxVrtrSingleSfmOverloadState,'TmnxInetCidrNextHopType':TmnxInetCidrNextHopType,'TmnxInetCidrNextHopOwner':TmnxInetCidrNextHopOwner,'TmnxL3RouteOwner':TmnxL3RouteOwner,'tnVRtrMIBModule':tnVRtrMIBModule,'tnVRtrObjs':tnVRtrObjs,'vRtrConfTable':vRtrConfTable,'vRtrConfEntry':vRtrConfEntry,_P:vRtrID,'vRtrRowStatus':vRtrRowStatus,'vRtrAdminState':vRtrAdminState,'vRtrName':vRtrName,'vRtrMaxNumRoutes':vRtrMaxNumRoutes,'vRtrBgpStatus':vRtrBgpStatus,'vRtrMplsStatus':vRtrMplsStatus,'vRtrOspfStatus':vRtrOspfStatus,'vRtrRipStatus':vRtrRipStatus,'vRtrRsvpStatus':vRtrRsvpStatus,'vRtrEcmpMaxRoutes':vRtrEcmpMaxRoutes,'vRtrAS':vRtrAS,'vRtrNewIfIndex':vRtrNewIfIndex,'vRtrLdpStatus':vRtrLdpStatus,'vRtrIsIsStatus':vRtrIsIsStatus,'vRtrRouterId':vRtrRouterId,'vRtrTriggeredPolicy':vRtrTriggeredPolicy,'vRtrConfederationAS':vRtrConfederationAS,'vRtrRouteDistinguisher':vRtrRouteDistinguisher,'vRtrMidRouteThreshold':vRtrMidRouteThreshold,'vRtrHighRouteThreshold':vRtrHighRouteThreshold,'vRtrIllegalLabelThreshold':vRtrIllegalLabelThreshold,'vRtrVpnId':vRtrVpnId,'vRtrDescription':vRtrDescription,'vRtrGracefulRestart':vRtrGracefulRestart,'vRtrGracefulRestartType':vRtrGracefulRestartType,'vRtrType':vRtrType,'vRtrServiceId':vRtrServiceId,'vRtrCustId':vRtrCustId,'vRtrIgmpStatus':vRtrIgmpStatus,'vRtrMaxNumRoutesLogOnly':vRtrMaxNumRoutesLogOnly,'vRtrVrfTarget':vRtrVrfTarget,'vRtrVrfExportTarget':vRtrVrfExportTarget,'vRtrVrfImportTarget':vRtrVrfImportTarget,'vRtrPimStatus':vRtrPimStatus,'vRtrMaxMcastNumRoutes':vRtrMaxMcastNumRoutes,'vRtrMaxMcastNumRoutesLogOnly':vRtrMaxMcastNumRoutesLogOnly,'vRtrMcastMidRouteThreshold':vRtrMcastMidRouteThreshold,'vRtrIgnoreIcmpRedirect':vRtrIgnoreIcmpRedirect,'vRtrOspfv3Status':vRtrOspfv3Status,'vRtrMsdpStatus':vRtrMsdpStatus,'vRtrVprnType':vRtrVprnType,'vRtrSecondaryVrfId':vRtrSecondaryVrfId,'vRtrMldStatus':vRtrMldStatus,'vRtrIPv6MaxNumRoutes':vRtrIPv6MaxNumRoutes,'vRtrIPv6MidRouteThreshold':vRtrIPv6MidRouteThreshold,'vRtrIPv6HighRouteThreshold':vRtrIPv6HighRouteThreshold,'vRtrIPv6MaxNumRoutesLogOnly':vRtrIPv6MaxNumRoutesLogOnly,'vRtrIPv6IgnoreIcmpRedirect':vRtrIPv6IgnoreIcmpRedirect,'vRtrMcPathMgmtPlcyName':vRtrMcPathMgmtPlcyName,'vRtrIgnoreNextHopMetric':vRtrIgnoreNextHopMetric,'vRtrMvpnVrfTarget':vRtrMvpnVrfTarget,'vRtrMvpnVrfExportTarget':vRtrMvpnVrfExportTarget,'vRtrMvpnVrfImportTarget':vRtrMvpnVrfImportTarget,'vRtrMvpnVrfTargetUnicast':vRtrMvpnVrfTargetUnicast,'vRtrMvpnVrfExportTargetUnicast':vRtrMvpnVrfExportTargetUnicast,'vRtrMvpnVrfImportTargetUnicast':vRtrMvpnVrfImportTargetUnicast,'vRtrAS4Byte':vRtrAS4Byte,'vRtrConfederationAS4Byte':vRtrConfederationAS4Byte,'vRtrMvpnCMcastImportRT':vRtrMvpnCMcastImportRT,'vRtrInterASMvpn':vRtrInterASMvpn,'vRtrStatTable':vRtrStatTable,_AH:vRtrStatEntry,'vRtrOperState':vRtrOperState,'vRtrDirectRoutes':vRtrDirectRoutes,'vRtrDirectActiveRoutes':vRtrDirectActiveRoutes,'vRtrStaticRoutes':vRtrStaticRoutes,'vRtrStaticActiveRoutes':vRtrStaticActiveRoutes,'vRtrOSPFRoutes':vRtrOSPFRoutes,'vRtrOSPFActiveRoutes':vRtrOSPFActiveRoutes,'vRtrBGPRoutes':vRtrBGPRoutes,'vRtrBGPActiveRoutes':vRtrBGPActiveRoutes,'vRtrISISRoutes':vRtrISISRoutes,'vRtrISISActiveRoutes':vRtrISISActiveRoutes,'vRtrRIPRoutes':vRtrRIPRoutes,'vRtrRIPActiveRoutes':vRtrRIPActiveRoutes,'vRtrAggregateRoutes':vRtrAggregateRoutes,'vRtrAggregateActiveRoutes':vRtrAggregateActiveRoutes,'vRtrStatConfiguredIfs':vRtrStatConfiguredIfs,'vRtrStatActiveIfs':vRtrStatActiveIfs,'vRtrStatIllegalLabels':vRtrStatIllegalLabels,'vRtrStatCurrNumRoutes':vRtrStatCurrNumRoutes,'vRtrStatBGPVpnRoutes':vRtrStatBGPVpnRoutes,'vRtrStatBGPVpnActiveRoutes':vRtrStatBGPVpnActiveRoutes,'vRtrStatTotalLdpTunnels':vRtrStatTotalLdpTunnels,'vRtrStatTotalSdpTunnels':vRtrStatTotalSdpTunnels,'vRtrStatActiveLdpTunnels':vRtrStatActiveLdpTunnels,'vRtrStatActiveSdpTunnels':vRtrStatActiveSdpTunnels,'vRtrMulticastRoutes':vRtrMulticastRoutes,'vRtrStatActiveARPEntries':vRtrStatActiveARPEntries,'vRtrStatTotalARPEntries':vRtrStatTotalARPEntries,'vRtrV6DirectRoutes':vRtrV6DirectRoutes,'vRtrV6DirectActiveRoutes':vRtrV6DirectActiveRoutes,'vRtrV6StaticRoutes':vRtrV6StaticRoutes,'vRtrV6StaticActiveRoutes':vRtrV6StaticActiveRoutes,'vRtrV6OSPFRoutes':vRtrV6OSPFRoutes,'vRtrV6OSPFActiveRoutes':vRtrV6OSPFActiveRoutes,'vRtrV6BGPRoutes':vRtrV6BGPRoutes,'vRtrV6BGPActiveRoutes':vRtrV6BGPActiveRoutes,'vRtrV6ISISRoutes':vRtrV6ISISRoutes,'vRtrV6ISISActiveRoutes':vRtrV6ISISActiveRoutes,'vRtrV6RIPRoutes':vRtrV6RIPRoutes,'vRtrV6RIPActiveRoutes':vRtrV6RIPActiveRoutes,'vRtrV6AggregateRoutes':vRtrV6AggregateRoutes,'vRtrV6AggregateActiveRoutes':vRtrV6AggregateActiveRoutes,'vRtrV6StatConfiguredIfs':vRtrV6StatConfiguredIfs,'vRtrV6StatActiveIfs':vRtrV6StatActiveIfs,'vRtrV6StatIllegalLabels':vRtrV6StatIllegalLabels,'vRtrV6StatCurrNumRoutes':vRtrV6StatCurrNumRoutes,'vRtrV6StatBGPVpnRoutes':vRtrV6StatBGPVpnRoutes,'vRtrV6StatBGPVpnActiveRoutes':vRtrV6StatBGPVpnActiveRoutes,'vRtrV6StatTotalLdpTunnels':vRtrV6StatTotalLdpTunnels,'vRtrV6StatTotalSdpTunnels':vRtrV6StatTotalSdpTunnels,'vRtrV6StatActiveLdpTunnels':vRtrV6StatActiveLdpTunnels,'vRtrV6StatActiveSdpTunnels':vRtrV6StatActiveSdpTunnels,'vRtrV6MulticastRoutes':vRtrV6MulticastRoutes,'vRtrV6StatActiveNbrEntries':vRtrV6StatActiveNbrEntries,'vRtrV6StatTotalNbrEntries':vRtrV6StatTotalNbrEntries,'vRtrSubMgmtRoutes':vRtrSubMgmtRoutes,'vRtrSubMgmtActiveRoutes':vRtrSubMgmtActiveRoutes,'vRtrStatTotalRsvpTunnels':vRtrStatTotalRsvpTunnels,'vRtrStatActiveRsvpTunnels':vRtrStatActiveRsvpTunnels,'vRtrV6StatTotalRsvpTunnels':vRtrV6StatTotalRsvpTunnels,'vRtrV6StatActiveRsvpTunnels':vRtrV6StatActiveRsvpTunnels,'vRtrHostRoutes':vRtrHostRoutes,'vRtrHostActiveRoutes':vRtrHostActiveRoutes,'vRtrV6HostRoutes':vRtrV6HostRoutes,'vRtrV6HostActiveRoutes':vRtrV6HostActiveRoutes,'vRtrStatLocalARPEntries':vRtrStatLocalARPEntries,'vRtrStatStaticARPEntries':vRtrStatStaticARPEntries,'vRtrStatDynamicARPEntries':vRtrStatDynamicARPEntries,'vRtrStatManagedARPEntries':vRtrStatManagedARPEntries,'vRtrStatInternalARPEntries':vRtrStatInternalARPEntries,'vRtrManagedRoutes':vRtrManagedRoutes,'vRtrManagedActiveRoutes':vRtrManagedActiveRoutes,'vRtrLDPRoutes':vRtrLDPRoutes,'vRtrLDPActiveRoutes':vRtrLDPActiveRoutes,'vRtrVPNLeakRoutes':vRtrVPNLeakRoutes,'vRtrVPNLeakActiveRoutes':vRtrVPNLeakActiveRoutes,'vRtrV6VPNLeakRoutes':vRtrV6VPNLeakRoutes,'vRtrV6VPNLeakActiveRoutes':vRtrV6VPNLeakActiveRoutes,'vRtrV6SubMgmtRoutes':vRtrV6SubMgmtRoutes,'vRtrV6SubMgmtActiveRoutes':vRtrV6SubMgmtActiveRoutes,'vRtrMobileHostRoutes':vRtrMobileHostRoutes,'vRtrMobileHostActiveRoutes':vRtrMobileHostActiveRoutes,'vRtrV6MobileHostRoutes':vRtrV6MobileHostRoutes,'vRtrV6MobileHostActiveRoutes':vRtrV6MobileHostActiveRoutes,'vRtrStatTotalBgpTunnels':vRtrStatTotalBgpTunnels,'vRtrStatActiveBgpTunnels':vRtrStatActiveBgpTunnels,'vRtrNatRoutes':vRtrNatRoutes,'vRtrNatActiveRoutes':vRtrNatActiveRoutes,'vRtrV6NatRoutes':vRtrV6NatRoutes,'vRtrV6NatActiveRoutes':vRtrV6NatActiveRoutes,'vRtrPeriodicRoutes':vRtrPeriodicRoutes,'vRtrPeriodicActiveRoutes':vRtrPeriodicActiveRoutes,'vRtrV6PeriodicRoutes':vRtrV6PeriodicRoutes,'vRtrV6PeriodicActiveRoutes':vRtrV6PeriodicActiveRoutes,'vRtrStatTotalMplsTpTunnels':vRtrStatTotalMplsTpTunnels,'vRtrStatActiveMplsTpTunnels':vRtrStatActiveMplsTpTunnels,'vRtrIfTotalNumber':vRtrIfTotalNumber,'vRtrIfTable':vRtrIfTable,'vRtrIfEntry':vRtrIfEntry,_U:vRtrIfIndex,'vRtrIfRowStatus':vRtrIfRowStatus,'vRtrIfType':vRtrIfType,_A0:vRtrIfName,'vRtrIfPortID':vRtrIfPortID,'vRtrIfChannelID':vRtrIfChannelID,'vRtrIfEncapValue':vRtrIfEncapValue,'vRtrIfAdminState':vRtrIfAdminState,'vRtrIfOperState':vRtrIfOperState,'vRtrIfAlias':vRtrIfAlias,'vRtrIfPhysicalAddress':vRtrIfPhysicalAddress,'vRtrIfArpTimeout':vRtrIfArpTimeout,'vRtrIfIcmpMaskReply':vRtrIfIcmpMaskReply,'vRtrIfIcmpRedirects':vRtrIfIcmpRedirects,'vRtrIfIcmpNumRedirects':vRtrIfIcmpNumRedirects,'vRtrIfIcmpRedirectsTime':vRtrIfIcmpRedirectsTime,'vRtrIfIcmpUnreachables':vRtrIfIcmpUnreachables,'vRtrIfIcmpNumUnreachables':vRtrIfIcmpNumUnreachables,'vRtrIfIcmpUnreachablesTime':vRtrIfIcmpUnreachablesTime,'vRtrIfIcmpTtlExpired':vRtrIfIcmpTtlExpired,'vRtrIfIcmpNumTtlExpired':vRtrIfIcmpNumTtlExpired,'vRtrIfIcmpTtlExpiredTime':vRtrIfIcmpTtlExpiredTime,'vRtrIfNtpBroadcast':vRtrIfNtpBroadcast,'vRtrIfUnnumbered':vRtrIfUnnumbered,'vRtrIfMtu':vRtrIfMtu,'vRtrIfQosPolicyId':vRtrIfQosPolicyId,'vRtrIfIngressFilterId':vRtrIfIngressFilterId,'vRtrIfEgressFilterId':vRtrIfEgressFilterId,'vRtrIfDirectedBroadcast':vRtrIfDirectedBroadcast,'vRtrIfMplsStatus':vRtrIfMplsStatus,'vRtrIfUnnumberedIf':vRtrIfUnnumberedIf,'vRtrIfCflowd':vRtrIfCflowd,'vRtrIfVPNClass':vRtrIfVPNClass,'vRtrIfDescription':vRtrIfDescription,'vRtrIfProtocol':vRtrIfProtocol,'vRtrIfTosMarkingTrusted':vRtrIfTosMarkingTrusted,'vRtrIfServiceId':vRtrIfServiceId,'vRtrIfArpPopulate':vRtrIfArpPopulate,'vRtrIfIPv6ConfigAllowed':vRtrIfIPv6ConfigAllowed,'vRtrIfIPv6OperState':vRtrIfIPv6OperState,'vRtrIfIPv6IngressFilterId':vRtrIfIPv6IngressFilterId,'vRtrIfIPv6EgressFilterId':vRtrIfIPv6EgressFilterId,'vRtrIfIcmpV6Redirects':vRtrIfIcmpV6Redirects,'vRtrIfIcmpV6NumRedirects':vRtrIfIcmpV6NumRedirects,'vRtrIfIcmpV6RedirectsTime':vRtrIfIcmpV6RedirectsTime,'vRtrIfIcmpV6Unreachables':vRtrIfIcmpV6Unreachables,'vRtrIfIcmpV6NumUnreachables':vRtrIfIcmpV6NumUnreachables,'vRtrIfIcmpV6UnreachablesTime':vRtrIfIcmpV6UnreachablesTime,'vRtrIfIcmpV6TimeExceeded':vRtrIfIcmpV6TimeExceeded,'vRtrIfIcmpV6NumTimeExceeded':vRtrIfIcmpV6NumTimeExceeded,'vRtrIfIcmpV6TimeExceededTime':vRtrIfIcmpV6TimeExceededTime,'vRtrIfIcmpV6PktTooBig':vRtrIfIcmpV6PktTooBig,'vRtrIfIcmpV6NumPktTooBig':vRtrIfIcmpV6NumPktTooBig,'vRtrIfIcmpV6PktTooBigTime':vRtrIfIcmpV6PktTooBigTime,'vRtrIfIcmpV6ParamProblem':vRtrIfIcmpV6ParamProblem,'vRtrIfIcmpV6NumParamProblem':vRtrIfIcmpV6NumParamProblem,'vRtrIfIcmpV6ParamProblemTime':vRtrIfIcmpV6ParamProblemTime,'vRtrIfLinkLocalAddressType':vRtrIfLinkLocalAddressType,'vRtrIfLinkLocalAddress':vRtrIfLinkLocalAddress,'vRtrIfLinkLocalAddressState':vRtrIfLinkLocalAddressState,'vRtrIfLastOperStateChange':vRtrIfLastOperStateChange,'vRtrIfOperMtu':vRtrIfOperMtu,_A2:vRtrIfGlobalIndex,'vRtrIfDelaySeconds':vRtrIfDelaySeconds,'vRtrIfDelayUpTimer':vRtrIfDelayUpTimer,'vRtrIfLocalDhcpServerName':vRtrIfLocalDhcpServerName,'vRtrIfInitDelayEnable':vRtrIfInitDelayEnable,'vRtrIfCpmProtPolicyId':vRtrIfCpmProtPolicyId,'vRtrIfCpmProtUncfgdProtoDropCnt':vRtrIfCpmProtUncfgdProtoDropCnt,'vRtrIfLdpSyncTimer':vRtrIfLdpSyncTimer,'vRtrIfStripLabel':vRtrIfStripLabel,'vRtrIfuRPFCheckState':vRtrIfuRPFCheckState,'vRtrIfuRPFCheckMode':vRtrIfuRPFCheckMode,'vRtrIfQosQGrp':vRtrIfQosQGrp,'vRtrIfAdminLinkLocalAddrType':vRtrIfAdminLinkLocalAddrType,'vRtrIfAdminLinkLocalAddr':vRtrIfAdminLinkLocalAddr,'vRtrIfAdmLnkLclAddrPreferred':vRtrIfAdmLnkLclAddrPreferred,'vRtrIfOperDownReason':vRtrIfOperDownReason,'vRtrIfNameTable':vRtrIfNameTable,'vRtrIfNameEntry':vRtrIfNameEntry,'vRtrIfNameIndex':vRtrIfNameIndex,'vRtrIpAddrTable':vRtrIpAddrTable,'vRtrIpAddrEntry':vRtrIpAddrEntry,_A1:vRiaIndex,'vRiaRowStatus':vRiaRowStatus,'vRiaIpAddress':vRiaIpAddress,'vRiaNetMask':vRiaNetMask,'vRiaBcastAddrFormat':vRiaBcastAddrFormat,'vRiaReasmMaxSize':vRiaReasmMaxSize,'vRiaIgpInhibit':vRiaIgpInhibit,'vRiaInetAddressType':vRiaInetAddressType,'vRiaInetAddress':vRiaInetAddress,'vRiaInetPrefixLen':vRiaInetPrefixLen,'vRiaInetAddrState':vRiaInetAddrState,'vRiaInetEui64':vRiaInetEui64,'vRiaInetOperAddress':vRiaInetOperAddress,'vRiaInetGwAddressType':vRiaInetGwAddressType,'vRiaInetGwAddress':vRiaInetGwAddress,'vRiaInetRemoteIpType':vRiaInetRemoteIpType,'vRiaInetRemoteIp':vRiaInetRemoteIp,'vRiaInetAddrPreferred':vRiaInetAddrPreferred,'vRiaSubscrPrefix':vRiaSubscrPrefix,'vRiaSubscrPrefixType':vRiaSubscrPrefixType,'vRiaSubscrHostRoutePopulate':vRiaSubscrHostRoutePopulate,'vRiaTrackSrrpInstance':vRiaTrackSrrpInstance,'vRiaHoldUpTime':vRiaHoldUpTime,'tnVRtrGlobalObjs':tnVRtrGlobalObjs,'vRtrNextVRtrID':vRtrNextVRtrID,'vRtrConfiguredVRtrs':vRtrConfiguredVRtrs,'vRtrActiveVRtrs':vRtrActiveVRtrs,'vRtrRouteThresholdSoakTime':vRtrRouteThresholdSoakTime,'vRtrMaxARPEntries':vRtrMaxARPEntries,'vRtrIPv6RouteThresholdSoakTime':vRtrIPv6RouteThresholdSoakTime,'vRtrIfGlobalIndexTable':vRtrIfGlobalIndexTable,'vRtrIfGlobalIndexEntry':vRtrIfGlobalIndexEntry,'vRtrIfGlobalIndexvRtrID':vRtrIfGlobalIndexvRtrID,'vRtrIfGlobalIndexvRtrIfIndex':vRtrIfGlobalIndexvRtrIfIndex,'vRtrIfStatsTable':vRtrIfStatsTable,'vRtrIfStatsEntry':vRtrIfStatsEntry,'vRtrIfuRPFCheckFailPkts':vRtrIfuRPFCheckFailPkts,'vRtrIfuRPFCheckFailPktsLow32':vRtrIfuRPFCheckFailPktsLow32,'vRtrIfuRPFCheckFailPktsHigh32':vRtrIfuRPFCheckFailPktsHigh32,'vRtrIfuRPFCheckFailBytes':vRtrIfuRPFCheckFailBytes,'vRtrIfuRPFCheckFailBytesLow32':vRtrIfuRPFCheckFailBytesLow32,'vRtrIfuRPFCheckFailBytesHigh32':vRtrIfuRPFCheckFailBytesHigh32,'vRtrIfIpReasFragPktsRcvd':vRtrIfIpReasFragPktsRcvd,'vRtrIfIpReasFragPktsRcvdLow32':vRtrIfIpReasFragPktsRcvdLow32,'vRtrIfIpReasFragPktsRcvdHigh32':vRtrIfIpReasFragPktsRcvdHigh32,'vRtrIfIpReasFragBytesRcvd':vRtrIfIpReasFragBytesRcvd,'vRtrIfIpReasFragBytesRcvdLow32':vRtrIfIpReasFragBytesRcvdLow32,'vRtrIfIpReasFragBytesRcvdHigh32':vRtrIfIpReasFragBytesRcvdHigh32,'vRtrIfIpReasFragPktsReas':vRtrIfIpReasFragPktsReas,'vRtrIfIpReasFragPktsReasLow32':vRtrIfIpReasFragPktsReasLow32,'vRtrIfIpReasFragPktsReasHigh32':vRtrIfIpReasFragPktsReasHigh32,'vRtrIfIpReasFragBytesReas':vRtrIfIpReasFragBytesReas,'vRtrIfIpReasFragBytesReasLow32':vRtrIfIpReasFragBytesReasLow32,'vRtrIfIpReasFragBytesReasHigh32':vRtrIfIpReasFragBytesReasHigh32,'vRtrIfIpReasFragReasErrors':vRtrIfIpReasFragReasErrors,'vRtrIfIpReasFragReasErrorsLow32':vRtrIfIpReasFragReasErrorsLow32,'vRtrIfIpReasFragReasErrorsHigh32':vRtrIfIpReasFragReasErrorsHigh32,'vRtrIfIpReasFragDisc':vRtrIfIpReasFragDisc,'vRtrIfIpReasFragDiscLow32':vRtrIfIpReasFragDiscLow32,'vRtrIfIpReasFragDiscHigh32':vRtrIfIpReasFragDiscHigh32,'vRtrIfIpReasOutBufRes':vRtrIfIpReasOutBufRes,'vRtrIfIpReasOutBufResLow32':vRtrIfIpReasOutBufResLow32,'vRtrIfIpReasOutBufResHigh32':vRtrIfIpReasOutBufResHigh32,'vRtrIfIpReasPktsRx':vRtrIfIpReasPktsRx,'vRtrIfIpReasPktsRxLow32':vRtrIfIpReasPktsRxLow32,'vRtrIfIpReasPktsRxHigh32':vRtrIfIpReasPktsRxHigh32,'vRtrIfIpReasBytesRx':vRtrIfIpReasBytesRx,'vRtrIfIpReasBytesRxLow32':vRtrIfIpReasBytesRxLow32,'vRtrIfIpReasBytesRxHigh32':vRtrIfIpReasBytesRxHigh32,'vRtrIfIpReasPktsTx':vRtrIfIpReasPktsTx,'vRtrIfIpReasPktsTxLow32':vRtrIfIpReasPktsTxLow32,'vRtrIfIpReasPktsTxHigh32':vRtrIfIpReasPktsTxHigh32,'vRtrIfIpReasBytesTx':vRtrIfIpReasBytesTx,'vRtrIfIpReasBytesTxLow32':vRtrIfIpReasBytesTxLow32,'vRtrIfIpReasBytesTxHigh32':vRtrIfIpReasBytesTxHigh32,'vRtrIfRxPkts':vRtrIfRxPkts,'vRtrIfRxPktsLow32':vRtrIfRxPktsLow32,'vRtrIfRxPktsHigh32':vRtrIfRxPktsHigh32,'vRtrIfRxBytes':vRtrIfRxBytes,'vRtrIfRxBytesLow32':vRtrIfRxBytesLow32,'vRtrIfRxBytesHigh32':vRtrIfRxBytesHigh32,'vRtrIfTxV4Pkts':vRtrIfTxV4Pkts,'vRtrIfTxV4PktsLow32':vRtrIfTxV4PktsLow32,'vRtrIfTxV4PktsHigh32':vRtrIfTxV4PktsHigh32,'vRtrIfTxV4Bytes':vRtrIfTxV4Bytes,'vRtrIfTxV4BytesLow32':vRtrIfTxV4BytesLow32,'vRtrIfTxV4BytesHigh32':vRtrIfTxV4BytesHigh32,'vRtrIfTxV6Pkts':vRtrIfTxV6Pkts,'vRtrIfTxV6PktsLow32':vRtrIfTxV6PktsLow32,'vRtrIfTxV6PktsHigh32':vRtrIfTxV6PktsHigh32,'vRtrIfTxV6Bytes':vRtrIfTxV6Bytes,'vRtrIfTxV6BytesLow32':vRtrIfTxV6BytesLow32,'vRtrIfTxV6BytesHigh32':vRtrIfTxV6BytesHigh32,'vRtrIfTxV4DiscardPkts':vRtrIfTxV4DiscardPkts,'vRtrIfTxV4DiscardPktsLow32':vRtrIfTxV4DiscardPktsLow32,'vRtrIfTxV4DiscardPktsHigh32':vRtrIfTxV4DiscardPktsHigh32,'vRtrIfTxV4DiscardBytes':vRtrIfTxV4DiscardBytes,'vRtrIfTxV4DiscardBytesLow32':vRtrIfTxV4DiscardBytesLow32,'vRtrIfTxV4DiscardBytesHigh32':vRtrIfTxV4DiscardBytesHigh32,'vRtrIfTxV6DiscardPkts':vRtrIfTxV6DiscardPkts,'vRtrIfTxV6DiscardPktsLow32':vRtrIfTxV6DiscardPktsLow32,'vRtrIfTxV6DiscardPktsHigh32':vRtrIfTxV6DiscardPktsHigh32,'vRtrIfTxV6DiscardBytes':vRtrIfTxV6DiscardBytes,'vRtrIfTxV6DiscardBytesLow32':vRtrIfTxV6DiscardBytesLow32,'vRtrIfTxV6DiscardBytesHigh32':vRtrIfTxV6DiscardBytesHigh32,'vRtrIfIpReasV6FragPktsRcvd':vRtrIfIpReasV6FragPktsRcvd,'vRtrIfIpReasV6FragPktsRcvdLow32':vRtrIfIpReasV6FragPktsRcvdLow32,'vRtrIfIpReasV6FragPktsRcvdHigh32':vRtrIfIpReasV6FragPktsRcvdHigh32,'vRtrIfIpReasV6FragBytesRcvd':vRtrIfIpReasV6FragBytesRcvd,'vRtrIfIpReasV6FragBytesRcvdL32':vRtrIfIpReasV6FragBytesRcvdL32,'vRtrIfIpReasV6FragBytesRcvdH32':vRtrIfIpReasV6FragBytesRcvdH32,'vRtrIfIpReasV6FragPktsReas':vRtrIfIpReasV6FragPktsReas,'vRtrIfIpReasV6FragPktsReasLow32':vRtrIfIpReasV6FragPktsReasLow32,'vRtrIfIpReasV6FragPktsReasHigh32':vRtrIfIpReasV6FragPktsReasHigh32,'vRtrIfIpReasV6FragBytesReas':vRtrIfIpReasV6FragBytesReas,'vRtrIfIpReasV6FragBytesReasL32':vRtrIfIpReasV6FragBytesReasL32,'vRtrIfIpReasV6FragBytesReasH32':vRtrIfIpReasV6FragBytesReasH32,'vRtrIfIpReasV6FragReasErrors':vRtrIfIpReasV6FragReasErrors,'vRtrIfIpReasV6FragReasErrorsL32':vRtrIfIpReasV6FragReasErrorsL32,'vRtrIfIpReasV6FragReasErrorsH32':vRtrIfIpReasV6FragReasErrorsH32,'vRtrIfIpReasV6FragDisc':vRtrIfIpReasV6FragDisc,'vRtrIfIpReasV6FragDiscLow32':vRtrIfIpReasV6FragDiscLow32,'vRtrIfIpReasV6FragDiscHigh32':vRtrIfIpReasV6FragDiscHigh32,'vRtrIfIpReasV6OutBufRes':vRtrIfIpReasV6OutBufRes,'vRtrIfIpReasV6OutBufResLow32':vRtrIfIpReasV6OutBufResLow32,'vRtrIfIpReasV6OutBufResHigh32':vRtrIfIpReasV6OutBufResHigh32,'vRtrIfIpReasV6PktsRx':vRtrIfIpReasV6PktsRx,'vRtrIfIpReasV6PktsRxLow32':vRtrIfIpReasV6PktsRxLow32,'vRtrIfIpReasV6PktsRxHigh32':vRtrIfIpReasV6PktsRxHigh32,'vRtrIfIpReasV6BytesRx':vRtrIfIpReasV6BytesRx,'vRtrIfIpReasV6BytesRxLow32':vRtrIfIpReasV6BytesRxLow32,'vRtrIfIpReasV6BytesRxHigh32':vRtrIfIpReasV6BytesRxHigh32,'vRtrIfIpReasV6PktsTx':vRtrIfIpReasV6PktsTx,'vRtrIfIpReasV6PktsTxLow32':vRtrIfIpReasV6PktsTxLow32,'vRtrIfIpReasV6PktsTxHigh32':vRtrIfIpReasV6PktsTxHigh32,'vRtrIfIpReasV6BytesTx':vRtrIfIpReasV6BytesTx,'vRtrIfIpReasV6BytesTxLow32':vRtrIfIpReasV6BytesTxLow32,'vRtrIfIpReasV6BytesTxHigh32':vRtrIfIpReasV6BytesTxHigh32,'vRtrIfSpeed':vRtrIfSpeed,'vRtrIfExtTable':vRtrIfExtTable,_AI:vRtrIfExtEntry,'vRtrIfLsrIpLoadBalancing':vRtrIfLsrIpLoadBalancing,'vRtrIfIngressIpv4Flowspec':vRtrIfIngressIpv4Flowspec,'vRtrIfInfo':vRtrIfInfo,'vRtrIfInfoEncrypted':vRtrIfInfoEncrypted,'vRtrIfQosRouteLookup':vRtrIfQosRouteLookup,'vRtrIfIpv6QosRouteLookup':vRtrIfIpv6QosRouteLookup,'vRtrIfStatusString':vRtrIfStatusString,'vRtrIfIpv6uRPFCheckState':vRtrIfIpv6uRPFCheckState,'vRtrIfIpv6uRPFCheckMode':vRtrIfIpv6uRPFCheckMode,'vRtrIfTmsOffRampVprn':vRtrIfTmsOffRampVprn,'vRtrIfTmsMgmtVprn':vRtrIfTmsMgmtVprn,'tnVRtrMobGatewayObjs':tnVRtrMobGatewayObjs,'vRtrIfBfdExtTableLastChanged':vRtrIfBfdExtTableLastChanged,'vRtrIfBfdExtTable':vRtrIfBfdExtTable,'vRtrIfBfdExtEntry':vRtrIfBfdExtEntry,_A4:vRtrIfBfdExtAddressType,'vRtrIfBfdExtAdminState':vRtrIfBfdExtAdminState,'vRtrIfBfdExtTransmitInterval':vRtrIfBfdExtTransmitInterval,'vRtrIfBfdExtReceiveInterval':vRtrIfBfdExtReceiveInterval,'vRtrIfBfdExtMultiplier':vRtrIfBfdExtMultiplier,'vRtrIfBfdExtEchoInterval':vRtrIfBfdExtEchoInterval,'vRtrIfBfdExtType':vRtrIfBfdExtType,'vRtrIfStatsExtTable':vRtrIfStatsExtTable,_AJ:vRtrIfStatsExtEntry,'vRtrIfTxPkts':vRtrIfTxPkts,'vRtrIfTxPktsLow32':vRtrIfTxPktsLow32,'vRtrIfTxPktsHigh32':vRtrIfTxPktsHigh32,'vRtrIfTxBytes':vRtrIfTxBytes,'vRtrIfTxBytesLow32':vRtrIfTxBytesLow32,'vRtrIfTxBytesHigh32':vRtrIfTxBytesHigh32,'vRtrIfQosTable':vRtrIfQosTable,_AK:vRtrIfQosEntry,'vRtrIfQosNetworkPolicyId':vRtrIfQosNetworkPolicyId,'vRtrIfBfdSessExtTable':vRtrIfBfdSessExtTable,'vRtrIfBfdSessExtEntry':vRtrIfBfdSessExtEntry,_A5:vRtrIfBfdSessExtLinkType,_A6:vRtrIfBfdSessExtRxInfoId,_A7:vRtrIfBfdSessExtLclAddrType,_A8:vRtrIfBfdSessExtLclAddr,_A9:vRtrIfBfdSessExtRemAddrType,_AA:vRtrIfBfdSessExtRemAddr,'vRtrIfBfdSessExtOperState':vRtrIfBfdSessExtOperState,'vRtrIfBfdSessExtState':vRtrIfBfdSessExtState,'vRtrIfBfdSessExtOperFlags':vRtrIfBfdSessExtOperFlags,'vRtrIfBfdSessExtMesgRecv':vRtrIfBfdSessExtMesgRecv,'vRtrIfBfdSessExtMesgSent':vRtrIfBfdSessExtMesgSent,'vRtrIfBfdSessExtLastDownTime':vRtrIfBfdSessExtLastDownTime,'vRtrIfBfdSessExtLastUpTime':vRtrIfBfdSessExtLastUpTime,'vRtrIfBfdSessExtUpCount':vRtrIfBfdSessExtUpCount,'vRtrIfBfdSessExtDownCount':vRtrIfBfdSessExtDownCount,'vRtrIfBfdSessExtLclDisc':vRtrIfBfdSessExtLclDisc,'vRtrIfBfdSessExtRemDisc':vRtrIfBfdSessExtRemDisc,'vRtrIfBfdSessExtProtocols':vRtrIfBfdSessExtProtocols,'vRtrIfBfdSessExtTxInterval':vRtrIfBfdSessExtTxInterval,'vRtrIfBfdSessExtRxInterval':vRtrIfBfdSessExtRxInterval,'vRtrIfBfdSessExtType':vRtrIfBfdSessExtType,'vRtrIfBfdSessExtVerMismatch':vRtrIfBfdSessExtVerMismatch,'vRtrIfBfdSessExtTimeSinceLastRx':vRtrIfBfdSessExtTimeSinceLastRx,'vRtrIfBfdSessExtTimeSinceLastTx':vRtrIfBfdSessExtTimeSinceLastTx,'vRtrIfBfdSessExtRemoteLspNum':vRtrIfBfdSessExtRemoteLspNum,'vRtrIfBfdSessExtRemoteTunnelNum':vRtrIfBfdSessExtRemoteTunnelNum,'vRtrIfBfdSessExtRemoteNodeId':vRtrIfBfdSessExtRemoteNodeId,'vRtrIfBfdSessExtRemoteGlobalId':vRtrIfBfdSessExtRemoteGlobalId,'vRtrIfBfdSessExtLspPathTunnelId':vRtrIfBfdSessExtLspPathTunnelId,'vRtrIfBfdSessExtLspPathId':vRtrIfBfdSessExtLspPathId,'vRtrIfBfdSessForwardInfoTable':vRtrIfBfdSessForwardInfoTable,_AL:vRtrIfBfdSessForwardInfoEntry,'vRtrIfBfdSessExtLclState':vRtrIfBfdSessExtLclState,'vRtrIfBfdSessExtLclMode':vRtrIfBfdSessExtLclMode,'vRtrIfBfdSessExtLclDiag':vRtrIfBfdSessExtLclDiag,'vRtrIfBfdSessExtLclMinTx':vRtrIfBfdSessExtLclMinTx,'vRtrIfBfdSessExtLclMinRx':vRtrIfBfdSessExtLclMinRx,'vRtrIfBfdSessExtLclMult':vRtrIfBfdSessExtLclMult,'vRtrIfBfdSessExtRemState':vRtrIfBfdSessExtRemState,'vRtrIfBfdSessExtRemMode':vRtrIfBfdSessExtRemMode,'vRtrIfBfdSessExtRemDiag':vRtrIfBfdSessExtRemDiag,'vRtrIfBfdSessExtRemMinTx':vRtrIfBfdSessExtRemMinTx,'vRtrIfBfdSessExtRemMinRx':vRtrIfBfdSessExtRemMinRx,'vRtrIfBfdSessExtRemMult':vRtrIfBfdSessExtRemMult,'vRtrIfBfdSessExtLastRecv':vRtrIfBfdSessExtLastRecv,'vRtrIfBfdSessExtLastSent':vRtrIfBfdSessExtLastSent,'vRtrConfScalar1':vRtrConfScalar1,'vRtrConfScalar2':vRtrConfScalar2})