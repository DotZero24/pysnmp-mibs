_A2='f10VirtualLinkDetailsTableGroup'
_A1='f10VirtualLinkNotificationGroup'
_A0='f10VirtualLinkStatisticsGroup'
_z='f10VirtualLinkTrunkGroup'
_y='f10VLTDomainConfigError'
_x='f10VLTIclBwUsageExceed'
_w='f10VLTHBeatStatusChange'
_v='f10VLTPeerStatusChange'
_u='f10VLTIclStatusChange'
_t='f10VLTRoleChange'
_s='f10VLTDetailPeerStatus'
_r='f10VLTDetailLocalStatus'
_q='f10VLTDetailPeerLagID'
_p='f10VLTStatNumVersionErrors'
_o='f10VLTStatNumDomainErrors'
_n='f10VLTStatNumHbeatRcvd'
_m='f10VLTStatNumHbeatSent'
_l='f10VLTStatNumHelloRcvd'
_k='f10VLTStatNumHelloSent'
_j='f10VLTRemotePeerRouting'
_i='f10VLTPeerRoutingTimeout'
_h='f10VLTPeerRouting'
_g='f10VLTCfgSysMacAddr'
_f='f10VLTRemoteVersionMinor'
_e='f10VLTRemoteVersionMajor'
_d='f10VLTRemoteUnitId'
_c='f10VLTVersionMinor'
_b='f10VLTVersionMajor'
_a='f10VLTUnitId'
_Z='f10VLTRemoteRolePriority'
_Y='f10VLTRemoteMacAddr'
_X='f10VLTBkUpInterval'
_W='f10VLTBkUpIpAddr'
_V='f10VLTBkUpIpAddrType'
_U='f10VLTPriority'
_T='f10VLTMacAddr'
_S='f10VirtualLinkStatsTableEntry'
_R='enabled'
_Q='disabled'
_P='linkDown'
_O='f10VLTErrorReason'
_N='f10VLTIclBwStatus'
_M='f10VLTHBeatStatus'
_L='f10VLTIclStatus'
_K='f10VLTPeerStatus'
_J='f10VLTRole'
_I='f10VLTIclIfIndex'
_H='f10VLTDetailLocalLagID'
_G='f10VLTDomainId'
_F='TimeInterval'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='current'
_A='F10-VIRTUAL-LINK-TRUNK-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
f10VirtualLinkTrunkMib=ModuleIdentity((1,3,6,1,4,1,6027,3,17))
if mibBuilder.loadTexts:f10VirtualLinkTrunkMib.setRevisions(('2012-11-28 00:00','2012-05-21 00:00','2012-05-14 00:00','2012-04-02 00:00','2011-05-06 00:00','2011-03-14 00:00'))
class F10VLTMemberLinkStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('linkNotEstablished',0),('linkUp',1),(_P,2),('linkError',3)))
_F10VirtualLinkTrunkObjects_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkObjects=_F10VirtualLinkTrunkObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,17,1))
_F10VirtualLinkTrunkTable_Object=MibTable
f10VirtualLinkTrunkTable=_F10VirtualLinkTrunkTable_Object((1,3,6,1,4,1,6027,3,17,1,1))
if mibBuilder.loadTexts:f10VirtualLinkTrunkTable.setStatus(_B)
_F10VirtualLinkTrunkTableEntry_Object=MibTableRow
f10VirtualLinkTrunkTableEntry=_F10VirtualLinkTrunkTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,1,1))
f10VirtualLinkTrunkTableEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:f10VirtualLinkTrunkTableEntry.setStatus(_B)
_F10VLTDomainId_Type=Unsigned32
_F10VLTDomainId_Object=MibTableColumn
f10VLTDomainId=_F10VLTDomainId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,1),_F10VLTDomainId_Type())
f10VLTDomainId.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTDomainId.setStatus(_B)
_F10VLTMacAddr_Type=MacAddress
_F10VLTMacAddr_Object=MibTableColumn
f10VLTMacAddr=_F10VLTMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,2),_F10VLTMacAddr_Type())
f10VLTMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTMacAddr.setStatus(_B)
class _F10VLTPriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F10VLTPriority_Type.__name__=_E
_F10VLTPriority_Object=MibTableColumn
f10VLTPriority=_F10VLTPriority_Object((1,3,6,1,4,1,6027,3,17,1,1,1,3),_F10VLTPriority_Type())
f10VLTPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTPriority.setStatus(_B)
_F10VLTIclIfIndex_Type=InterfaceIndex
_F10VLTIclIfIndex_Object=MibTableColumn
f10VLTIclIfIndex=_F10VLTIclIfIndex_Object((1,3,6,1,4,1,6027,3,17,1,1,1,4),_F10VLTIclIfIndex_Type())
f10VLTIclIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTIclIfIndex.setStatus(_B)
class _F10VLTRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('standAlone',0),('primary',1),('secondary',2)))
_F10VLTRole_Type.__name__=_D
_F10VLTRole_Object=MibTableColumn
f10VLTRole=_F10VLTRole_Object((1,3,6,1,4,1,6027,3,17,1,1,1,5),_F10VLTRole_Type())
f10VLTRole.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRole.setStatus(_B)
class _F10VLTPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notEstablished',0),('peerUp',1),('peerDown',2),(_P,3)))
_F10VLTPeerStatus_Type.__name__=_D
_F10VLTPeerStatus_Object=MibTableColumn
f10VLTPeerStatus=_F10VLTPeerStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,6),_F10VLTPeerStatus_Type())
f10VLTPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTPeerStatus.setStatus(_B)
_F10VLTIclStatus_Type=F10VLTMemberLinkStatus
_F10VLTIclStatus_Object=MibTableColumn
f10VLTIclStatus=_F10VLTIclStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,7),_F10VLTIclStatus_Type())
f10VLTIclStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTIclStatus.setStatus(_B)
_F10VLTHBeatStatus_Type=F10VLTMemberLinkStatus
_F10VLTHBeatStatus_Object=MibTableColumn
f10VLTHBeatStatus=_F10VLTHBeatStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,8),_F10VLTHBeatStatus_Type())
f10VLTHBeatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTHBeatStatus.setStatus(_B)
_F10VLTBkUpIpAddrType_Type=InetAddressType
_F10VLTBkUpIpAddrType_Object=MibTableColumn
f10VLTBkUpIpAddrType=_F10VLTBkUpIpAddrType_Object((1,3,6,1,4,1,6027,3,17,1,1,1,9),_F10VLTBkUpIpAddrType_Type())
f10VLTBkUpIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTBkUpIpAddrType.setStatus(_B)
_F10VLTBkUpIpAddr_Type=InetAddress
_F10VLTBkUpIpAddr_Object=MibTableColumn
f10VLTBkUpIpAddr=_F10VLTBkUpIpAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,10),_F10VLTBkUpIpAddr_Type())
f10VLTBkUpIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTBkUpIpAddr.setStatus(_B)
class _F10VLTBkUpInterval_Type(TimeInterval):defaultValue=100;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,500))
_F10VLTBkUpInterval_Type.__name__=_F
_F10VLTBkUpInterval_Object=MibTableColumn
f10VLTBkUpInterval=_F10VLTBkUpInterval_Object((1,3,6,1,4,1,6027,3,17,1,1,1,11),_F10VLTBkUpInterval_Type())
f10VLTBkUpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTBkUpInterval.setStatus(_B)
_F10VLTRemoteMacAddr_Type=MacAddress
_F10VLTRemoteMacAddr_Object=MibTableColumn
f10VLTRemoteMacAddr=_F10VLTRemoteMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,12),_F10VLTRemoteMacAddr_Type())
f10VLTRemoteMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemoteMacAddr.setStatus(_B)
class _F10VLTRemoteRolePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F10VLTRemoteRolePriority_Type.__name__=_E
_F10VLTRemoteRolePriority_Object=MibTableColumn
f10VLTRemoteRolePriority=_F10VLTRemoteRolePriority_Object((1,3,6,1,4,1,6027,3,17,1,1,1,13),_F10VLTRemoteRolePriority_Type())
f10VLTRemoteRolePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemoteRolePriority.setStatus(_B)
_F10VLTUnitId_Type=Unsigned32
_F10VLTUnitId_Object=MibTableColumn
f10VLTUnitId=_F10VLTUnitId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,14),_F10VLTUnitId_Type())
f10VLTUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTUnitId.setStatus(_B)
_F10VLTVersionMajor_Type=Unsigned32
_F10VLTVersionMajor_Object=MibTableColumn
f10VLTVersionMajor=_F10VLTVersionMajor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,15),_F10VLTVersionMajor_Type())
f10VLTVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTVersionMajor.setStatus(_B)
_F10VLTVersionMinor_Type=Unsigned32
_F10VLTVersionMinor_Object=MibTableColumn
f10VLTVersionMinor=_F10VLTVersionMinor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,16),_F10VLTVersionMinor_Type())
f10VLTVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTVersionMinor.setStatus(_B)
_F10VLTRemoteUnitId_Type=Unsigned32
_F10VLTRemoteUnitId_Object=MibTableColumn
f10VLTRemoteUnitId=_F10VLTRemoteUnitId_Object((1,3,6,1,4,1,6027,3,17,1,1,1,17),_F10VLTRemoteUnitId_Type())
f10VLTRemoteUnitId.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemoteUnitId.setStatus(_B)
_F10VLTRemoteVersionMajor_Type=Unsigned32
_F10VLTRemoteVersionMajor_Object=MibTableColumn
f10VLTRemoteVersionMajor=_F10VLTRemoteVersionMajor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,18),_F10VLTRemoteVersionMajor_Type())
f10VLTRemoteVersionMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemoteVersionMajor.setStatus(_B)
_F10VLTRemoteVersionMinor_Type=Unsigned32
_F10VLTRemoteVersionMinor_Object=MibTableColumn
f10VLTRemoteVersionMinor=_F10VLTRemoteVersionMinor_Object((1,3,6,1,4,1,6027,3,17,1,1,1,19),_F10VLTRemoteVersionMinor_Type())
f10VLTRemoteVersionMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemoteVersionMinor.setStatus(_B)
class _F10VLTIclBwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('belowthreshold',0),('abovethreshold',1)))
_F10VLTIclBwStatus_Type.__name__=_D
_F10VLTIclBwStatus_Object=MibTableColumn
f10VLTIclBwStatus=_F10VLTIclBwStatus_Object((1,3,6,1,4,1,6027,3,17,1,1,1,20),_F10VLTIclBwStatus_Type())
f10VLTIclBwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTIclBwStatus.setStatus(_B)
_F10VLTCfgSysMacAddr_Type=MacAddress
_F10VLTCfgSysMacAddr_Object=MibTableColumn
f10VLTCfgSysMacAddr=_F10VLTCfgSysMacAddr_Object((1,3,6,1,4,1,6027,3,17,1,1,1,21),_F10VLTCfgSysMacAddr_Type())
f10VLTCfgSysMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTCfgSysMacAddr.setStatus(_B)
class _F10VLTPeerRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_F10VLTPeerRouting_Type.__name__=_D
_F10VLTPeerRouting_Object=MibTableColumn
f10VLTPeerRouting=_F10VLTPeerRouting_Object((1,3,6,1,4,1,6027,3,17,1,1,1,22),_F10VLTPeerRouting_Type())
f10VLTPeerRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTPeerRouting.setStatus(_B)
class _F10VLTPeerRoutingTimeout_Type(TimeInterval):subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_F10VLTPeerRoutingTimeout_Type.__name__=_F
_F10VLTPeerRoutingTimeout_Object=MibTableColumn
f10VLTPeerRoutingTimeout=_F10VLTPeerRoutingTimeout_Object((1,3,6,1,4,1,6027,3,17,1,1,1,23),_F10VLTPeerRoutingTimeout_Type())
f10VLTPeerRoutingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTPeerRoutingTimeout.setStatus(_B)
class _F10VLTRemotePeerRouting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_F10VLTRemotePeerRouting_Type.__name__=_D
_F10VLTRemotePeerRouting_Object=MibTableColumn
f10VLTRemotePeerRouting=_F10VLTRemotePeerRouting_Object((1,3,6,1,4,1,6027,3,17,1,1,1,24),_F10VLTRemotePeerRouting_Type())
f10VLTRemotePeerRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTRemotePeerRouting.setStatus(_B)
_F10VirtualLinkStatsTable_Object=MibTable
f10VirtualLinkStatsTable=_F10VirtualLinkStatsTable_Object((1,3,6,1,4,1,6027,3,17,1,2))
if mibBuilder.loadTexts:f10VirtualLinkStatsTable.setStatus(_B)
_F10VirtualLinkStatsTableEntry_Object=MibTableRow
f10VirtualLinkStatsTableEntry=_F10VirtualLinkStatsTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,2,1))
if mibBuilder.loadTexts:f10VirtualLinkStatsTableEntry.setStatus(_B)
_F10VLTStatNumHelloSent_Type=Counter32
_F10VLTStatNumHelloSent_Object=MibTableColumn
f10VLTStatNumHelloSent=_F10VLTStatNumHelloSent_Object((1,3,6,1,4,1,6027,3,17,1,2,1,1),_F10VLTStatNumHelloSent_Type())
f10VLTStatNumHelloSent.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumHelloSent.setStatus(_B)
_F10VLTStatNumHelloRcvd_Type=Counter32
_F10VLTStatNumHelloRcvd_Object=MibTableColumn
f10VLTStatNumHelloRcvd=_F10VLTStatNumHelloRcvd_Object((1,3,6,1,4,1,6027,3,17,1,2,1,2),_F10VLTStatNumHelloRcvd_Type())
f10VLTStatNumHelloRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumHelloRcvd.setStatus(_B)
_F10VLTStatNumHbeatSent_Type=Counter32
_F10VLTStatNumHbeatSent_Object=MibTableColumn
f10VLTStatNumHbeatSent=_F10VLTStatNumHbeatSent_Object((1,3,6,1,4,1,6027,3,17,1,2,1,3),_F10VLTStatNumHbeatSent_Type())
f10VLTStatNumHbeatSent.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumHbeatSent.setStatus(_B)
_F10VLTStatNumHbeatRcvd_Type=Counter32
_F10VLTStatNumHbeatRcvd_Object=MibTableColumn
f10VLTStatNumHbeatRcvd=_F10VLTStatNumHbeatRcvd_Object((1,3,6,1,4,1,6027,3,17,1,2,1,4),_F10VLTStatNumHbeatRcvd_Type())
f10VLTStatNumHbeatRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumHbeatRcvd.setStatus(_B)
_F10VLTStatNumDomainErrors_Type=Counter32
_F10VLTStatNumDomainErrors_Object=MibTableColumn
f10VLTStatNumDomainErrors=_F10VLTStatNumDomainErrors_Object((1,3,6,1,4,1,6027,3,17,1,2,1,5),_F10VLTStatNumDomainErrors_Type())
f10VLTStatNumDomainErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumDomainErrors.setStatus(_B)
_F10VLTStatNumVersionErrors_Type=Counter32
_F10VLTStatNumVersionErrors_Object=MibTableColumn
f10VLTStatNumVersionErrors=_F10VLTStatNumVersionErrors_Object((1,3,6,1,4,1,6027,3,17,1,2,1,6),_F10VLTStatNumVersionErrors_Type())
f10VLTStatNumVersionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTStatNumVersionErrors.setStatus(_B)
_F10VirtualLinkDetailsTable_Object=MibTable
f10VirtualLinkDetailsTable=_F10VirtualLinkDetailsTable_Object((1,3,6,1,4,1,6027,3,17,1,3))
if mibBuilder.loadTexts:f10VirtualLinkDetailsTable.setStatus(_B)
_F10VirtualLinkDetailsTableEntry_Object=MibTableRow
f10VirtualLinkDetailsTableEntry=_F10VirtualLinkDetailsTableEntry_Object((1,3,6,1,4,1,6027,3,17,1,3,1))
f10VirtualLinkDetailsTableEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:f10VirtualLinkDetailsTableEntry.setStatus(_B)
class _F10VLTDetailLocalLagID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F10VLTDetailLocalLagID_Type.__name__=_E
_F10VLTDetailLocalLagID_Object=MibTableColumn
f10VLTDetailLocalLagID=_F10VLTDetailLocalLagID_Object((1,3,6,1,4,1,6027,3,17,1,3,1,1),_F10VLTDetailLocalLagID_Type())
f10VLTDetailLocalLagID.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTDetailLocalLagID.setStatus(_B)
class _F10VLTDetailPeerLagID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_F10VLTDetailPeerLagID_Type.__name__=_E
_F10VLTDetailPeerLagID_Object=MibTableColumn
f10VLTDetailPeerLagID=_F10VLTDetailPeerLagID_Object((1,3,6,1,4,1,6027,3,17,1,3,1,2),_F10VLTDetailPeerLagID_Type())
f10VLTDetailPeerLagID.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTDetailPeerLagID.setStatus(_B)
class _F10VLTDetailLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_F10VLTDetailLocalStatus_Type.__name__=_D
_F10VLTDetailLocalStatus_Object=MibTableColumn
f10VLTDetailLocalStatus=_F10VLTDetailLocalStatus_Object((1,3,6,1,4,1,6027,3,17,1,3,1,3),_F10VLTDetailLocalStatus_Type())
f10VLTDetailLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTDetailLocalStatus.setStatus(_B)
class _F10VLTDetailPeerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_F10VLTDetailPeerStatus_Type.__name__=_D
_F10VLTDetailPeerStatus_Object=MibTableColumn
f10VLTDetailPeerStatus=_F10VLTDetailPeerStatus_Object((1,3,6,1,4,1,6027,3,17,1,3,1,4),_F10VLTDetailPeerStatus_Type())
f10VLTDetailPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:f10VLTDetailPeerStatus.setStatus(_B)
class _F10VLTErrorReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noError',1),('domainIdMismatch',2),('unitIdMismatch',3),('versionMismatch',4),('sysMacMismatch',5),('peerRoutingMismatch',6)))
_F10VLTErrorReason_Type.__name__=_D
_F10VLTErrorReason_Object=MibScalar
f10VLTErrorReason=_F10VLTErrorReason_Object((1,3,6,1,4,1,6027,3,17,1,4),_F10VLTErrorReason_Type())
f10VLTErrorReason.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:f10VLTErrorReason.setStatus(_B)
_F10VirtualLinkTrunkNotifObjects_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkNotifObjects=_F10VirtualLinkTrunkNotifObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,17,2))
_F10VirtualLinkTrunkNotifications_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkNotifications=_F10VirtualLinkTrunkNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,17,2,0))
_F10VirtualLinkTrunkConformance_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkConformance=_F10VirtualLinkTrunkConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3))
_F10VirtualLinkTrunkCompliances_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkCompliances=_F10VirtualLinkTrunkCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3,1))
_F10VirtualLinkTrunkGroups_ObjectIdentity=ObjectIdentity
f10VirtualLinkTrunkGroups=_F10VirtualLinkTrunkGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,17,3,2))
f10VirtualLinkTrunkTableEntry.registerAugmentions((_A,_S))
f10VirtualLinkStatsTableEntry.setIndexNames(*f10VirtualLinkTrunkTableEntry.getIndexNames())
f10VirtualLinkTrunkGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,1))
f10VirtualLinkTrunkGroup.setObjects(*((_A,_G),(_A,_T),(_A,_U),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_N),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_O)))
if mibBuilder.loadTexts:f10VirtualLinkTrunkGroup.setStatus(_B)
f10VirtualLinkStatisticsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,2))
f10VirtualLinkStatisticsGroup.setObjects(*((_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:f10VirtualLinkStatisticsGroup.setStatus(_B)
f10VirtualLinkDetailsTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,17,3,2,4))
f10VirtualLinkDetailsTableGroup.setObjects(*((_A,_H),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:f10VirtualLinkDetailsTableGroup.setStatus(_B)
f10VLTRoleChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,1))
f10VLTRoleChange.setObjects((_A,_J))
if mibBuilder.loadTexts:f10VLTRoleChange.setStatus(_B)
f10VLTIclStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,2))
f10VLTIclStatusChange.setObjects((_A,_L))
if mibBuilder.loadTexts:f10VLTIclStatusChange.setStatus(_B)
f10VLTPeerStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,3))
f10VLTPeerStatusChange.setObjects((_A,_K))
if mibBuilder.loadTexts:f10VLTPeerStatusChange.setStatus(_B)
f10VLTHBeatStatusChange=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,4))
f10VLTHBeatStatusChange.setObjects((_A,_M))
if mibBuilder.loadTexts:f10VLTHBeatStatusChange.setStatus(_B)
f10VLTIclBwUsageExceed=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,5))
f10VLTIclBwUsageExceed.setObjects(*((_A,_I),(_A,_N)))
if mibBuilder.loadTexts:f10VLTIclBwUsageExceed.setStatus(_B)
f10VLTDomainConfigError=NotificationType((1,3,6,1,4,1,6027,3,17,2,0,6))
f10VLTDomainConfigError.setObjects((_A,_O))
if mibBuilder.loadTexts:f10VLTDomainConfigError.setStatus(_B)
f10VirtualLinkNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,17,3,2,3))
f10VirtualLinkNotificationGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:f10VirtualLinkNotificationGroup.setStatus(_B)
f10VirtualLinkTrunkCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,17,3,1,1))
f10VirtualLinkTrunkCompliance.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:f10VirtualLinkTrunkCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'F10VLTMemberLinkStatus':F10VLTMemberLinkStatus,'f10VirtualLinkTrunkMib':f10VirtualLinkTrunkMib,'f10VirtualLinkTrunkObjects':f10VirtualLinkTrunkObjects,'f10VirtualLinkTrunkTable':f10VirtualLinkTrunkTable,'f10VirtualLinkTrunkTableEntry':f10VirtualLinkTrunkTableEntry,_G:f10VLTDomainId,_T:f10VLTMacAddr,_U:f10VLTPriority,_I:f10VLTIclIfIndex,_J:f10VLTRole,_K:f10VLTPeerStatus,_L:f10VLTIclStatus,_M:f10VLTHBeatStatus,_V:f10VLTBkUpIpAddrType,_W:f10VLTBkUpIpAddr,_X:f10VLTBkUpInterval,_Y:f10VLTRemoteMacAddr,_Z:f10VLTRemoteRolePriority,_a:f10VLTUnitId,_b:f10VLTVersionMajor,_c:f10VLTVersionMinor,_d:f10VLTRemoteUnitId,_e:f10VLTRemoteVersionMajor,_f:f10VLTRemoteVersionMinor,_N:f10VLTIclBwStatus,_g:f10VLTCfgSysMacAddr,_h:f10VLTPeerRouting,_i:f10VLTPeerRoutingTimeout,_j:f10VLTRemotePeerRouting,'f10VirtualLinkStatsTable':f10VirtualLinkStatsTable,_S:f10VirtualLinkStatsTableEntry,_k:f10VLTStatNumHelloSent,_l:f10VLTStatNumHelloRcvd,_m:f10VLTStatNumHbeatSent,_n:f10VLTStatNumHbeatRcvd,_o:f10VLTStatNumDomainErrors,_p:f10VLTStatNumVersionErrors,'f10VirtualLinkDetailsTable':f10VirtualLinkDetailsTable,'f10VirtualLinkDetailsTableEntry':f10VirtualLinkDetailsTableEntry,_H:f10VLTDetailLocalLagID,_q:f10VLTDetailPeerLagID,_r:f10VLTDetailLocalStatus,_s:f10VLTDetailPeerStatus,_O:f10VLTErrorReason,'f10VirtualLinkTrunkNotifObjects':f10VirtualLinkTrunkNotifObjects,'f10VirtualLinkTrunkNotifications':f10VirtualLinkTrunkNotifications,_t:f10VLTRoleChange,_u:f10VLTIclStatusChange,_v:f10VLTPeerStatusChange,_w:f10VLTHBeatStatusChange,_x:f10VLTIclBwUsageExceed,_y:f10VLTDomainConfigError,'f10VirtualLinkTrunkConformance':f10VirtualLinkTrunkConformance,'f10VirtualLinkTrunkCompliances':f10VirtualLinkTrunkCompliances,'f10VirtualLinkTrunkCompliance':f10VirtualLinkTrunkCompliance,'f10VirtualLinkTrunkGroups':f10VirtualLinkTrunkGroups,_z:f10VirtualLinkTrunkGroup,_A0:f10VirtualLinkStatisticsGroup,_A1:f10VirtualLinkNotificationGroup,_A2:f10VirtualLinkDetailsTableGroup})