_A2='dellNetVirtualLinkDetailsTableGroup'
_A1='dellNetVirtualLinkNotificationGroup'
_A0='dellNetVirtualLinkStatisticsGroup'
_z='dellNetVirtualLinkTrunkGroup'
_y='dellNetVLTDomainConfigError'
_x='dellNetVLTIclBwUsageExceed'
_w='dellNetVLTHBeatStatusChange'
_v='dellNetVLTPeerStatusChange'
_u='dellNetVLTIclStatusChange'
_t='dellNetVLTRoleChange'
_s='dellNetVLTDetailPeerStatus'
_r='dellNetVLTDetailLocalStatus'
_q='dellNetVLTDetailPeerLagID'
_p='dellNetVLTStatNumVersionErrors'
_o='dellNetVLTStatNumDomainErrors'
_n='dellNetVLTStatNumHbeatRcvd'
_m='dellNetVLTStatNumHbeatSent'
_l='dellNetVLTStatNumHelloRcvd'
_k='dellNetVLTStatNumHelloSent'
_j='dellNetVLTRemotePeerRouting'
_i='dellNetVLTPeerRoutingTimeout'
_h='dellNetVLTPeerRouting'
_g='dellNetVLTCfgSysMacAddr'
_f='dellNetVLTRemoteVersionMinor'
_e='dellNetVLTRemoteVersionMajor'
_d='dellNetVLTRemoteUnitId'
_c='dellNetVLTVersionMinor'
_b='dellNetVLTVersionMajor'
_a='dellNetVLTUnitId'
_Z='dellNetVLTRemoteRolePriority'
_Y='dellNetVLTRemoteMacAddr'
_X='dellNetVLTBkUpInterval'
_W='dellNetVLTBkUpIpAddr'
_V='dellNetVLTBkUpIpAddrType'
_U='dellNetVLTPriority'
_T='dellNetVLTMacAddr'
_S='dellNetVirtualLinkStatsTableEntry'
_R='enabled'
_Q='disabled'
_P='linkDown'
_O='dellNetVLTErrorReason'
_N='dellNetVLTIclBwStatus'
_M='dellNetVLTHBeatStatus'
_L='dellNetVLTIclStatus'
_K='dellNetVLTPeerStatus'
_J='dellNetVLTRole'
_I='dellNetVLTIclIfIndex'
_H='dellNetVLTDetailLocalLagID'
_G='dellNetVLTDomainId'
_F='TimeInterval'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='current'
_A='DELL-NETWORKING-VIRTUAL-LINK-TRUNK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
dellNetVirtualLinkTrunkMib=ModuleIdentity((1,3,6,1,4,1,6027,3,17))
if mibBuilder.loadTexts:dellNetVirtualLinkTrunkMib.setRevisions(('2012-11-28 00:00','2012-05-21 00:00','2012-05-14 00:00','2012-04-02 00:00','2011-05-06 00:00','2011-03-14 00:00'))
class DellNetVLTMemberLinkStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('linkNotEstablished',0),('linkUp',1),(_P,2),('linkError',3)))
_DellNetVirtualLinkTrunkObjects_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkObjects=_DellNetVirtualLinkTrunkObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,17,1))
_DellNetVirtualLinkTrunkTable_Object=MibTable
dellNetVirtualLinkTrunkTable=_DellNetVirtualLinkTrunkTable_Object((1,3,6,1,4,1,6027,3,17,1,1))
if mibBuilder.loadTexts:dellNetVirtualLinkTrunkTable.setStatus(_B)
_DellNetVirtualLinkTrunkTableEntry_Object=MibTableRow
dellNetVirtualLinkTrunkTableEntry=_DellNetVirtualLinkTrunkTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,1,1))
dellNetVirtualLinkTrunkTableEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:dellNetVirtualLinkTrunkTableEntry.setStatus(_B)
_DellNetVLTDomainId_Type=Unsigned32
_DellNetVLTDomainId_Object=MibTableColumn
dellNetVLTDomainId=_DellNetVLTDomainId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,1),_DellNetVLTDomainId_Type())
dellNetVLTDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTDomainId.setStatus(_B)
_DellNetVLTMacAddr_Type=MacAddress
_DellNetVLTMacAddr_Object=MibTableColumn
dellNetVLTMacAddr=_DellNetVLTMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,2),_DellNetVLTMacAddr_Type())
dellNetVLTMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTMacAddr.setStatus(_B)
class _DellNetVLTPriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetVLTPriority_Type.__name__=_E
_DellNetVLTPriority_Object=MibTableColumn
dellNetVLTPriority=_DellNetVLTPriority_Object((1,3,6,1,4,1,6027,3,17,1,1,1,3),_DellNetVLTPriority_Type())
dellNetVLTPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTPriority.setStatus(_B)
_DellNetVLTIclIfIndex_Type=InterfaceIndex
_DellNetVLTIclIfIndex_Object=MibTableColumn
dellNetVLTIclIfIndex=_DellNetVLTIclIfIndex_Object((1,3,6,1,4,1,6027,3,17,1,1,1,4),_DellNetVLTIclIfIndex_Type())
dellNetVLTIclIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTIclIfIndex.setStatus(_B)
class _DellNetVLTRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('standAlone',0),('primary',1),('secondary',2)))
_DellNetVLTRole_Type.__name__=_D
_DellNetVLTRole_Object=MibTableColumn
dellNetVLTRole=_DellNetVLTRole_Object((1,3,6,1,4,1,6027,3,17,1,1,1,5),_DellNetVLTRole_Type())
dellNetVLTRole.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRole.setStatus(_B)
class _DellNetVLTPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notEstablished',0),('peerUp',1),('peerDown',2),(_P,3)))
_DellNetVLTPeerStatus_Type.__name__=_D
_DellNetVLTPeerStatus_Object=MibTableColumn
dellNetVLTPeerStatus=_DellNetVLTPeerStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,6),_DellNetVLTPeerStatus_Type())
dellNetVLTPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTPeerStatus.setStatus(_B)
_DellNetVLTIclStatus_Type=DellNetVLTMemberLinkStatus
_DellNetVLTIclStatus_Object=MibTableColumn
dellNetVLTIclStatus=_DellNetVLTIclStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,7),_DellNetVLTIclStatus_Type())
dellNetVLTIclStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTIclStatus.setStatus(_B)
_DellNetVLTHBeatStatus_Type=DellNetVLTMemberLinkStatus
_DellNetVLTHBeatStatus_Object=MibTableColumn
dellNetVLTHBeatStatus=_DellNetVLTHBeatStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,8),_DellNetVLTHBeatStatus_Type())
dellNetVLTHBeatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTHBeatStatus.setStatus(_B)
_DellNetVLTBkUpIpAddrType_Type=InetAddressType
_DellNetVLTBkUpIpAddrType_Object=MibTableColumn
dellNetVLTBkUpIpAddrType=_DellNetVLTBkUpIpAddrType_Object((1,3,6,1,4,1,6027,3,17,1,1,1,9),_DellNetVLTBkUpIpAddrType_Type())
dellNetVLTBkUpIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTBkUpIpAddrType.setStatus(_B)
_DellNetVLTBkUpIpAddr_Type=InetAddress
_DellNetVLTBkUpIpAddr_Object=MibTableColumn
dellNetVLTBkUpIpAddr=_DellNetVLTBkUpIpAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,10),_DellNetVLTBkUpIpAddr_Type())
dellNetVLTBkUpIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTBkUpIpAddr.setStatus(_B)
class _DellNetVLTBkUpInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,500))
_DellNetVLTBkUpInterval_Type.__name__=_F
_DellNetVLTBkUpInterval_Object=MibTableColumn
dellNetVLTBkUpInterval=_DellNetVLTBkUpInterval_Object((1,3,6,1,4,1,6027,3,17,1,1,1,11),_DellNetVLTBkUpInterval_Type())
dellNetVLTBkUpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTBkUpInterval.setStatus(_B)
_DellNetVLTRemoteMacAddr_Type=MacAddress
_DellNetVLTRemoteMacAddr_Object=MibTableColumn
dellNetVLTRemoteMacAddr=_DellNetVLTRemoteMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,12),_DellNetVLTRemoteMacAddr_Type())
dellNetVLTRemoteMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemoteMacAddr.setStatus(_B)
class _DellNetVLTRemoteRolePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetVLTRemoteRolePriority_Type.__name__=_E
_DellNetVLTRemoteRolePriority_Object=MibTableColumn
dellNetVLTRemoteRolePriority=_DellNetVLTRemoteRolePriority_Object((1,3,6,1,4,1,6027,3,17,1,1,1,13),_DellNetVLTRemoteRolePriority_Type())
dellNetVLTRemoteRolePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemoteRolePriority.setStatus(_B)
_DellNetVLTUnitId_Type=Unsigned32
_DellNetVLTUnitId_Object=MibTableColumn
dellNetVLTUnitId=_DellNetVLTUnitId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,14),_DellNetVLTUnitId_Type())
dellNetVLTUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTUnitId.setStatus(_B)
_DellNetVLTVersionMajor_Type=Unsigned32
_DellNetVLTVersionMajor_Object=MibTableColumn
dellNetVLTVersionMajor=_DellNetVLTVersionMajor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,15),_DellNetVLTVersionMajor_Type())
dellNetVLTVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTVersionMajor.setStatus(_B)
_DellNetVLTVersionMinor_Type=Unsigned32
_DellNetVLTVersionMinor_Object=MibTableColumn
dellNetVLTVersionMinor=_DellNetVLTVersionMinor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,16),_DellNetVLTVersionMinor_Type())
dellNetVLTVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTVersionMinor.setStatus(_B)
_DellNetVLTRemoteUnitId_Type=Unsigned32
_DellNetVLTRemoteUnitId_Object=MibTableColumn
dellNetVLTRemoteUnitId=_DellNetVLTRemoteUnitId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,17),_DellNetVLTRemoteUnitId_Type())
dellNetVLTRemoteUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemoteUnitId.setStatus(_B)
_DellNetVLTRemoteVersionMajor_Type=Unsigned32
_DellNetVLTRemoteVersionMajor_Object=MibTableColumn
dellNetVLTRemoteVersionMajor=_DellNetVLTRemoteVersionMajor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,18),_DellNetVLTRemoteVersionMajor_Type())
dellNetVLTRemoteVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemoteVersionMajor.setStatus(_B)
_DellNetVLTRemoteVersionMinor_Type=Unsigned32
_DellNetVLTRemoteVersionMinor_Object=MibTableColumn
dellNetVLTRemoteVersionMinor=_DellNetVLTRemoteVersionMinor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,19),_DellNetVLTRemoteVersionMinor_Type())
dellNetVLTRemoteVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemoteVersionMinor.setStatus(_B)
class _DellNetVLTIclBwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('belowthreshold',0),('abovethreshold',1)))
_DellNetVLTIclBwStatus_Type.__name__=_D
_DellNetVLTIclBwStatus_Object=MibTableColumn
dellNetVLTIclBwStatus=_DellNetVLTIclBwStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,20),_DellNetVLTIclBwStatus_Type())
dellNetVLTIclBwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTIclBwStatus.setStatus(_B)
_DellNetVLTCfgSysMacAddr_Type=MacAddress
_DellNetVLTCfgSysMacAddr_Object=MibTableColumn
dellNetVLTCfgSysMacAddr=_DellNetVLTCfgSysMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,21),_DellNetVLTCfgSysMacAddr_Type())
dellNetVLTCfgSysMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTCfgSysMacAddr.setStatus(_B)
class _DellNetVLTPeerRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DellNetVLTPeerRouting_Type.__name__=_D
_DellNetVLTPeerRouting_Object=MibTableColumn
dellNetVLTPeerRouting=_DellNetVLTPeerRouting_Object((1,3,6,1,4,1,6027,3,17,1,1,1,22),_DellNetVLTPeerRouting_Type())
dellNetVLTPeerRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTPeerRouting.setStatus(_B)
class _DellNetVLTPeerRoutingTimeout_Type(TimeInterval):subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DellNetVLTPeerRoutingTimeout_Type.__name__=_F
_DellNetVLTPeerRoutingTimeout_Object=MibTableColumn
dellNetVLTPeerRoutingTimeout=_DellNetVLTPeerRoutingTimeout_Object((1,3,6,1,4,1,6027,3,17,1,1,1,23),_DellNetVLTPeerRoutingTimeout_Type())
dellNetVLTPeerRoutingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTPeerRoutingTimeout.setStatus(_B)
class _DellNetVLTRemotePeerRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DellNetVLTRemotePeerRouting_Type.__name__=_D
_DellNetVLTRemotePeerRouting_Object=MibTableColumn
dellNetVLTRemotePeerRouting=_DellNetVLTRemotePeerRouting_Object((1,3,6,1,4,1,6027,3,17,1,1,1,24),_DellNetVLTRemotePeerRouting_Type())
dellNetVLTRemotePeerRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTRemotePeerRouting.setStatus(_B)
_DellNetVirtualLinkStatsTable_Object=MibTable
dellNetVirtualLinkStatsTable=_DellNetVirtualLinkStatsTable_Object((1,3,6,1,4,1,6027,3,17,1,2))
if mibBuilder.loadTexts:dellNetVirtualLinkStatsTable.setStatus(_B)
_DellNetVirtualLinkStatsTableEntry_Object=MibTableRow
dellNetVirtualLinkStatsTableEntry=_DellNetVirtualLinkStatsTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,2,1))
if mibBuilder.loadTexts:dellNetVirtualLinkStatsTableEntry.setStatus(_B)
_DellNetVLTStatNumHelloSent_Type=Counter32
_DellNetVLTStatNumHelloSent_Object=MibTableColumn
dellNetVLTStatNumHelloSent=_DellNetVLTStatNumHelloSent_Object((1,3,6,1,4,1,6027,3,17,1,2,1,1),_DellNetVLTStatNumHelloSent_Type())
dellNetVLTStatNumHelloSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumHelloSent.setStatus(_B)
_DellNetVLTStatNumHelloRcvd_Type=Counter32
_DellNetVLTStatNumHelloRcvd_Object=MibTableColumn
dellNetVLTStatNumHelloRcvd=_DellNetVLTStatNumHelloRcvd_Object((1,3,6,1,4,1,6027,3,17,1,2,1,2),_DellNetVLTStatNumHelloRcvd_Type())
dellNetVLTStatNumHelloRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumHelloRcvd.setStatus(_B)
_DellNetVLTStatNumHbeatSent_Type=Counter32
_DellNetVLTStatNumHbeatSent_Object=MibTableColumn
dellNetVLTStatNumHbeatSent=_DellNetVLTStatNumHbeatSent_Object((1,3,6,1,4,1,6027,3,17,1,2,1,3),_DellNetVLTStatNumHbeatSent_Type())
dellNetVLTStatNumHbeatSent.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumHbeatSent.setStatus(_B)
_DellNetVLTStatNumHbeatRcvd_Type=Counter32
_DellNetVLTStatNumHbeatRcvd_Object=MibTableColumn
dellNetVLTStatNumHbeatRcvd=_DellNetVLTStatNumHbeatRcvd_Object((1,3,6,1,4,1,6027,3,17,1,2,1,4),_DellNetVLTStatNumHbeatRcvd_Type())
dellNetVLTStatNumHbeatRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumHbeatRcvd.setStatus(_B)
_DellNetVLTStatNumDomainErrors_Type=Counter32
_DellNetVLTStatNumDomainErrors_Object=MibTableColumn
dellNetVLTStatNumDomainErrors=_DellNetVLTStatNumDomainErrors_Object((1,3,6,1,4,1,6027,3,17,1,2,1,5),_DellNetVLTStatNumDomainErrors_Type())
dellNetVLTStatNumDomainErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumDomainErrors.setStatus(_B)
_DellNetVLTStatNumVersionErrors_Type=Counter32
_DellNetVLTStatNumVersionErrors_Object=MibTableColumn
dellNetVLTStatNumVersionErrors=_DellNetVLTStatNumVersionErrors_Object((1,3,6,1,4,1,6027,3,17,1,2,1,6),_DellNetVLTStatNumVersionErrors_Type())
dellNetVLTStatNumVersionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTStatNumVersionErrors.setStatus(_B)
_DellNetVirtualLinkDetailsTable_Object=MibTable
dellNetVirtualLinkDetailsTable=_DellNetVirtualLinkDetailsTable_Object((1,3,6,1,4,1,6027,3,17,1,3))
if mibBuilder.loadTexts:dellNetVirtualLinkDetailsTable.setStatus(_B)
_DellNetVirtualLinkDetailsTableEntry_Object=MibTableRow
dellNetVirtualLinkDetailsTableEntry=_DellNetVirtualLinkDetailsTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,3,1))
dellNetVirtualLinkDetailsTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:dellNetVirtualLinkDetailsTableEntry.setStatus(_B)
class _DellNetVLTDetailLocalLagID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetVLTDetailLocalLagID_Type.__name__=_E
_DellNetVLTDetailLocalLagID_Object=MibTableColumn
dellNetVLTDetailLocalLagID=_DellNetVLTDetailLocalLagID_Object((1,3,6,1,4,1,6027,3,17,1,3,1,1),_DellNetVLTDetailLocalLagID_Type())
dellNetVLTDetailLocalLagID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTDetailLocalLagID.setStatus(_B)
class _DellNetVLTDetailPeerLagID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetVLTDetailPeerLagID_Type.__name__=_E
_DellNetVLTDetailPeerLagID_Object=MibTableColumn
dellNetVLTDetailPeerLagID=_DellNetVLTDetailPeerLagID_Object((1,3,6,1,4,1,6027,3,17,1,3,1,2),_DellNetVLTDetailPeerLagID_Type())
dellNetVLTDetailPeerLagID.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTDetailPeerLagID.setStatus(_B)
class _DellNetVLTDetailLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_DellNetVLTDetailLocalStatus_Type.__name__=_D
_DellNetVLTDetailLocalStatus_Object=MibTableColumn
dellNetVLTDetailLocalStatus=_DellNetVLTDetailLocalStatus_Object((1,3,6,1,4,1,6027,3,17,1,3,1,3),_DellNetVLTDetailLocalStatus_Type())
dellNetVLTDetailLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTDetailLocalStatus.setStatus(_B)
class _DellNetVLTDetailPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_DellNetVLTDetailPeerStatus_Type.__name__=_D
_DellNetVLTDetailPeerStatus_Object=MibTableColumn
dellNetVLTDetailPeerStatus=_DellNetVLTDetailPeerStatus_Object((1,3,6,1,4,1,6027,3,17,1,3,1,4),_DellNetVLTDetailPeerStatus_Type())
dellNetVLTDetailPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetVLTDetailPeerStatus.setStatus(_B)
class _DellNetVLTErrorReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noError',1),('domainIdMismatch',2),('unitIdMismatch',3),('versionMismatch',4),('sysMacMismatch',5),('peerRoutingMismatch',6)))
_DellNetVLTErrorReason_Type.__name__=_D
_DellNetVLTErrorReason_Object=MibScalar
dellNetVLTErrorReason=_DellNetVLTErrorReason_Object((1,3,6,1,4,1,6027,3,17,1,4),_DellNetVLTErrorReason_Type())
dellNetVLTErrorReason.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:dellNetVLTErrorReason.setStatus(_B)
_DellNetVirtualLinkTrunkNotifObjects_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkNotifObjects=_DellNetVirtualLinkTrunkNotifObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,17,2))
_DellNetVirtualLinkTrunkNotifications_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkNotifications=_DellNetVirtualLinkTrunkNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,17,2,0))
_DellNetVirtualLinkTrunkConformance_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkConformance=_DellNetVirtualLinkTrunkConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3))
_DellNetVirtualLinkTrunkCompliances_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkCompliances=_DellNetVirtualLinkTrunkCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3,1))
_DellNetVirtualLinkTrunkGroups_ObjectIdentity=ObjectIdentity
dellNetVirtualLinkTrunkGroups=_DellNetVirtualLinkTrunkGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3,2))
dellNetVirtualLinkTrunkTableEntry.registerAugmentions((_A,_S))
dellNetVirtualLinkStatsTableEntry.setIndexNames(*dellNetVirtualLinkTrunkTableEntry.getIndexNames())
dellNetVirtualLinkTrunkGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,1))
dellNetVirtualLinkTrunkGroup.setObjects(*((_A,_G),(_A,_T),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_N),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_O)))
if mibBuilder.loadTexts:dellNetVirtualLinkTrunkGroup.setStatus(_B)
dellNetVirtualLinkStatisticsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,2))
dellNetVirtualLinkStatisticsGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:dellNetVirtualLinkStatisticsGroup.setStatus(_B)
dellNetVirtualLinkDetailsTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,4))
dellNetVirtualLinkDetailsTableGroup.setObjects(*((_A,_H),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:dellNetVirtualLinkDetailsTableGroup.setStatus(_B)
dellNetVLTRoleChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,1))
dellNetVLTRoleChange.setObjects((_A,_J))
if mibBuilder.loadTexts:dellNetVLTRoleChange.setStatus(_B)
dellNetVLTIclStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,2))
dellNetVLTIclStatusChange.setObjects((_A,_L))
if mibBuilder.loadTexts:dellNetVLTIclStatusChange.setStatus(_B)
dellNetVLTPeerStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,3))
dellNetVLTPeerStatusChange.setObjects((_A,_K))
if mibBuilder.loadTexts:dellNetVLTPeerStatusChange.setStatus(_B)
dellNetVLTHBeatStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,4))
dellNetVLTHBeatStatusChange.setObjects((_A,_M))
if mibBuilder.loadTexts:dellNetVLTHBeatStatusChange.setStatus(_B)
dellNetVLTIclBwUsageExceed=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,5))
dellNetVLTIclBwUsageExceed.setObjects(*((_A,_I),(_A,_N)))
if mibBuilder.loadTexts:dellNetVLTIclBwUsageExceed.setStatus(_B)
dellNetVLTDomainConfigError=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,6))
dellNetVLTDomainConfigError.setObjects((_A,_O))
if mibBuilder.loadTexts:dellNetVLTDomainConfigError.setStatus(_B)
dellNetVirtualLinkNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,17,3,2,3))
dellNetVirtualLinkNotificationGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:dellNetVirtualLinkNotificationGroup.setStatus(_B)
dellNetVirtualLinkTrunkCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,17,3,1,1))
dellNetVirtualLinkTrunkCompliance.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:dellNetVirtualLinkTrunkCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'DellNetVLTMemberLinkStatus':DellNetVLTMemberLinkStatus,'dellNetVirtualLinkTrunkMib':dellNetVirtualLinkTrunkMib,'dellNetVirtualLinkTrunkObjects':dellNetVirtualLinkTrunkObjects,'dellNetVirtualLinkTrunkTable':dellNetVirtualLinkTrunkTable,'dellNetVirtualLinkTrunkTableEntry':dellNetVirtualLinkTrunkTableEntry,_G:dellNetVLTDomainId,_T:dellNetVLTMacAddr,_U:dellNetVLTPriority,_I:dellNetVLTIclIfIndex,_J:dellNetVLTRole,_K:dellNetVLTPeerStatus,_L:dellNetVLTIclStatus,_M:dellNetVLTHBeatStatus,_V:dellNetVLTBkUpIpAddrType,_W:dellNetVLTBkUpIpAddr,_X:dellNetVLTBkUpInterval,_Y:dellNetVLTRemoteMacAddr,_Z:dellNetVLTRemoteRolePriority,_a:dellNetVLTUnitId,_b:dellNetVLTVersionMajor,_c:dellNetVLTVersionMinor,_d:dellNetVLTRemoteUnitId,_e:dellNetVLTRemoteVersionMajor,_f:dellNetVLTRemoteVersionMinor,_N:dellNetVLTIclBwStatus,_g:dellNetVLTCfgSysMacAddr,_h:dellNetVLTPeerRouting,_i:dellNetVLTPeerRoutingTimeout,_j:dellNetVLTRemotePeerRouting,'dellNetVirtualLinkStatsTable':dellNetVirtualLinkStatsTable,_S:dellNetVirtualLinkStatsTableEntry,_k:dellNetVLTStatNumHelloSent,_l:dellNetVLTStatNumHelloRcvd,_m:dellNetVLTStatNumHbeatSent,_n:dellNetVLTStatNumHbeatRcvd,_o:dellNetVLTStatNumDomainErrors,_p:dellNetVLTStatNumVersionErrors,'dellNetVirtualLinkDetailsTable':dellNetVirtualLinkDetailsTable,'dellNetVirtualLinkDetailsTableEntry':dellNetVirtualLinkDetailsTableEntry,_H:dellNetVLTDetailLocalLagID,_q:dellNetVLTDetailPeerLagID,_r:dellNetVLTDetailLocalStatus,_s:dellNetVLTDetailPeerStatus,_O:dellNetVLTErrorReason,'dellNetVirtualLinkTrunkNotifObjects':dellNetVirtualLinkTrunkNotifObjects,'dellNetVirtualLinkTrunkNotifications':dellNetVirtualLinkTrunkNotifications,_t:dellNetVLTRoleChange,_u:dellNetVLTIclStatusChange,_v:dellNetVLTPeerStatusChange,_w:dellNetVLTHBeatStatusChange,_x:dellNetVLTIclBwUsageExceed,_y:dellNetVLTDomainConfigError,'dellNetVirtualLinkTrunkConformance':dellNetVirtualLinkTrunkConformance,'dellNetVirtualLinkTrunkCompliances':dellNetVirtualLinkTrunkCompliances,'dellNetVirtualLinkTrunkCompliance':dellNetVirtualLinkTrunkCompliance,'dellNetVirtualLinkTrunkGroups':dellNetVirtualLinkTrunkGroups,_z:dellNetVirtualLinkTrunkGroup,_A0:dellNetVirtualLinkStatisticsGroup,_A1:dellNetVirtualLinkNotificationGroup,_A2:dellNetVirtualLinkDetailsTableGroup})