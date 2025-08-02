_m='mitelDhcpClientLeaseExpiry'
_l='mitelDhcpClientObtainedIp'
_k='mitelDhcpClientServerIp'
_j='mitelDhcpClientIpAddress'
_i='mitelDhcpServerVendorInfoID'
_h='mitelDhcpServerLeaseAddr'
_g='octet-string'
_f='integer'
_e='ascii-string'
_d='ip-address'
_c='mitelDhcpServerStaticIpSubnet'
_b='mitelDhcpServerStaticIpAddr'
_a='mitelDhcpServerRangeSubnet'
_Z='mitelDhcpServerRangeEnd'
_Y='mitelDhcpServerRangeStart'
_X='mitelDhcpServerSubnetSharedNet'
_W='mitelDhcpServerSubnetAddr'
_V='mitelDhcpRelayAgentServerAddr'
_U='bootp-or-dhcp'
_T='mitelDhcpServerOptionNumber'
_S='mitelDhcpServerOptionAddr'
_R='dhcp'
_Q='bootp'
_P='mitelDhcpClientIndex'
_O='not-this-if'
_N='this-if-last'
_M='this-if-first'
_L='none'
_K='default'
_J='read-create'
_I='OctetString'
_H='disabled'
_G='enabled'
_F='DisplayString'
_E='Integer32'
_D='MITEL-DHCP-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
mitelRouterDhcpGroup=ModuleIdentity((1,3,6,1,4,1,1027,4,8,1,3))
if mibBuilder.loadTexts:mitelRouterDhcpGroup.setRevisions(('2005-11-07 12:00','2003-03-21 12:31','1999-03-01 00:00'))
class MitelDhcpServerProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3),(_U,4)))
class MitelDhcpServerOptionList(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76)));namedValues=NamedValues(*(('subnet-mask',1),('time-offset',2),('default-router',3),('time-server',4),('name-server',5),('dns-server',6),('log-server',7),('cookie-server',8),('lpr-server',9),('impress-server',10),('resource-location-server',11),('host-name',12),('boot-file-size',13),('merit-dump-file-name',14),('domain-name',15),('swap-server',16),('root-path',17),('extension-path',18),('ip-forwarding',19),('non-local-source-routing',20),('policy-filter',21),('max-datagram-reassembly',22),('default-ip-time-to-live',23),('path-MTU-aging-timeout',24),('path-MTU-plateau-table',25),('interface-MTU-value',26),('all-subnets-are-local',27),('broadcast-address',28),('perform-mask-discovery',29),('mask-supplier',30),('perform-router-discovery',31),('router-solicitation-address',32),('static-route',33),('trailer-encapsulation',34),('arp-cache-timeout',35),('ethernet-encapsulation',36),('tcp-default-ttl',37),('tcp-keepalive-interval',38),('tcp-keepalive-garbage',39),('nis-domain-name',40),('nis-server',41),('ntp-server',42),('vendor-specific-information',43),('netbios-ip-name-server',44),('netbios-ip-dgram-distrib-server',45),('netbios-ip-node-type',46),('netbios-ip-scope',47),('x-window-font-server',48),('x-window-display-manager',49),('requested-ip',50),('lease-time',51),('option-overload',52),('message-type',53),('server-identifier',54),('parameter-request-list',55),('message',56),('max-dhcp-message-size',57),('renewal-time-value-t1',58),('rebinding-time-value-t2',59),('vendor-class-identifier',60),('client-identifier',61),('nis-plus-domain',64),('nis-plus-server',65),('tftp-server-name',66),('bootfile-name',67),('mobile-ip-home-agent',68),('smtp-server',69),('pop3-server',70),('nntp-server',71),('www-server',72),('finger-server',73),('irc-server',74),('streettalk-server',75),('streettalk-directory-assistance-server',76)))
_Mitel_ObjectIdentity=ObjectIdentity
mitel=_Mitel_ObjectIdentity((1,3,6,1,4,1,1027))
_MitelIdentification_ObjectIdentity=ObjectIdentity
mitelIdentification=_MitelIdentification_ObjectIdentity((1,3,6,1,4,1,1027,1))
_MitelIdCallServers_ObjectIdentity=ObjectIdentity
mitelIdCallServers=_MitelIdCallServers_ObjectIdentity((1,3,6,1,4,1,1027,1,2))
_MitelIdCsIpera1000_ObjectIdentity=ObjectIdentity
mitelIdCsIpera1000=_MitelIdCsIpera1000_ObjectIdentity((1,3,6,1,4,1,1027,1,2,4))
_MitelProprietary_ObjectIdentity=ObjectIdentity
mitelProprietary=_MitelProprietary_ObjectIdentity((1,3,6,1,4,1,1027,4))
_MitelPropIpNetworking_ObjectIdentity=ObjectIdentity
mitelPropIpNetworking=_MitelPropIpNetworking_ObjectIdentity((1,3,6,1,4,1,1027,4,8))
_MitelIpNetRouter_ObjectIdentity=ObjectIdentity
mitelIpNetRouter=_MitelIpNetRouter_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1))
class _MitelDhcpRelayAgentEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpRelayAgentEnable_Type.__name__=_E
_MitelDhcpRelayAgentEnable_Object=MibScalar
mitelDhcpRelayAgentEnable=_MitelDhcpRelayAgentEnable_Object((1,3,6,1,4,1,1027,4,8,1,3,1),_MitelDhcpRelayAgentEnable_Type())
mitelDhcpRelayAgentEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpRelayAgentEnable.setStatus(_A)
class _MitelDhcpRelayAgentMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MitelDhcpRelayAgentMaxHops_Type.__name__=_E
_MitelDhcpRelayAgentMaxHops_Object=MibScalar
mitelDhcpRelayAgentMaxHops=_MitelDhcpRelayAgentMaxHops_Object((1,3,6,1,4,1,1027,4,8,1,3,2),_MitelDhcpRelayAgentMaxHops_Type())
mitelDhcpRelayAgentMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpRelayAgentMaxHops.setStatus(_A)
_MitelDhcpRelayAgentServerTable_Object=MibTable
mitelDhcpRelayAgentServerTable=_MitelDhcpRelayAgentServerTable_Object((1,3,6,1,4,1,1027,4,8,1,3,3))
if mibBuilder.loadTexts:mitelDhcpRelayAgentServerTable.setStatus(_A)
_MitelDhcpRelayAgentServerEntry_Object=MibTableRow
mitelDhcpRelayAgentServerEntry=_MitelDhcpRelayAgentServerEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,3,1))
mitelDhcpRelayAgentServerEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:mitelDhcpRelayAgentServerEntry.setStatus(_A)
_MitelDhcpRelayAgentServerAddr_Type=IpAddress
_MitelDhcpRelayAgentServerAddr_Object=MibTableColumn
mitelDhcpRelayAgentServerAddr=_MitelDhcpRelayAgentServerAddr_Object((1,3,6,1,4,1,1027,4,8,1,3,3,1,1),_MitelDhcpRelayAgentServerAddr_Type())
mitelDhcpRelayAgentServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpRelayAgentServerAddr.setStatus(_A)
class _MitelDhcpRelayAgentServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MitelDhcpRelayAgentServerName_Type.__name__=_F
_MitelDhcpRelayAgentServerName_Object=MibTableColumn
mitelDhcpRelayAgentServerName=_MitelDhcpRelayAgentServerName_Object((1,3,6,1,4,1,1027,4,8,1,3,3,1,2),_MitelDhcpRelayAgentServerName_Type())
mitelDhcpRelayAgentServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpRelayAgentServerName.setStatus(_A)
_MitelDhcpRelayAgentServerStatus_Type=RowStatus
_MitelDhcpRelayAgentServerStatus_Object=MibTableColumn
mitelDhcpRelayAgentServerStatus=_MitelDhcpRelayAgentServerStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,3,1,3),_MitelDhcpRelayAgentServerStatus_Type())
mitelDhcpRelayAgentServerStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpRelayAgentServerStatus.setStatus(_A)
class _MitelDhcpRelayAgentBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpRelayAgentBroadcast_Type.__name__=_E
_MitelDhcpRelayAgentBroadcast_Object=MibScalar
mitelDhcpRelayAgentBroadcast=_MitelDhcpRelayAgentBroadcast_Object((1,3,6,1,4,1,1027,4,8,1,3,4),_MitelDhcpRelayAgentBroadcast_Type())
mitelDhcpRelayAgentBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpRelayAgentBroadcast.setStatus(_A)
_MitelDhcpServerGroup_ObjectIdentity=ObjectIdentity
mitelDhcpServerGroup=_MitelDhcpServerGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,3,5))
_MitelDhcpServerGeneralGroup_ObjectIdentity=ObjectIdentity
mitelDhcpServerGeneralGroup=_MitelDhcpServerGeneralGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,3,5,1))
class _MitelDhcpServerGeneralEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),('autoconfig',3)))
_MitelDhcpServerGeneralEnable_Type.__name__=_E
_MitelDhcpServerGeneralEnable_Object=MibScalar
mitelDhcpServerGeneralEnable=_MitelDhcpServerGeneralEnable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,1,1),_MitelDhcpServerGeneralEnable_Type())
mitelDhcpServerGeneralEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerGeneralEnable.setStatus(_A)
class _MitelDhcpServerGeneralGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3)))
_MitelDhcpServerGeneralGateway_Type.__name__=_E
_MitelDhcpServerGeneralGateway_Object=MibScalar
mitelDhcpServerGeneralGateway=_MitelDhcpServerGeneralGateway_Object((1,3,6,1,4,1,1027,4,8,1,3,5,1,2),_MitelDhcpServerGeneralGateway_Type())
mitelDhcpServerGeneralGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerGeneralGateway.setStatus(_A)
_MitelDhcpServerGeneralRefDhcpServer_Type=IpAddress
_MitelDhcpServerGeneralRefDhcpServer_Object=MibScalar
mitelDhcpServerGeneralRefDhcpServer=_MitelDhcpServerGeneralRefDhcpServer_Object((1,3,6,1,4,1,1027,4,8,1,3,5,1,3),_MitelDhcpServerGeneralRefDhcpServer_Type())
mitelDhcpServerGeneralRefDhcpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerGeneralRefDhcpServer.setStatus(_A)
class _MitelDhcpServerGeneralPingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MitelDhcpServerGeneralPingStatus_Type.__name__=_E
_MitelDhcpServerGeneralPingStatus_Object=MibScalar
mitelDhcpServerGeneralPingStatus=_MitelDhcpServerGeneralPingStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,1,4),_MitelDhcpServerGeneralPingStatus_Type())
mitelDhcpServerGeneralPingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerGeneralPingStatus.setStatus(_A)
_MitelDhcpServerSubnetTable_Object=MibTable
mitelDhcpServerSubnetTable=_MitelDhcpServerSubnetTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2))
if mibBuilder.loadTexts:mitelDhcpServerSubnetTable.setStatus(_A)
_MitelDhcpServerSubnetEntry_Object=MibTableRow
mitelDhcpServerSubnetEntry=_MitelDhcpServerSubnetEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1))
mitelDhcpServerSubnetEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:mitelDhcpServerSubnetEntry.setStatus(_A)
_MitelDhcpServerSubnetAddr_Type=IpAddress
_MitelDhcpServerSubnetAddr_Object=MibTableColumn
mitelDhcpServerSubnetAddr=_MitelDhcpServerSubnetAddr_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,1),_MitelDhcpServerSubnetAddr_Type())
mitelDhcpServerSubnetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerSubnetAddr.setStatus(_A)
_MitelDhcpServerSubnetSharedNet_Type=IpAddress
_MitelDhcpServerSubnetSharedNet_Object=MibTableColumn
mitelDhcpServerSubnetSharedNet=_MitelDhcpServerSubnetSharedNet_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,2),_MitelDhcpServerSubnetSharedNet_Type())
mitelDhcpServerSubnetSharedNet.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerSubnetSharedNet.setStatus(_A)
_MitelDhcpServerSubnetMask_Type=IpAddress
_MitelDhcpServerSubnetMask_Object=MibTableColumn
mitelDhcpServerSubnetMask=_MitelDhcpServerSubnetMask_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,3),_MitelDhcpServerSubnetMask_Type())
mitelDhcpServerSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerSubnetMask.setStatus(_A)
class _MitelDhcpServerSubnetGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_K,4)))
_MitelDhcpServerSubnetGateway_Type.__name__=_E
_MitelDhcpServerSubnetGateway_Object=MibTableColumn
mitelDhcpServerSubnetGateway=_MitelDhcpServerSubnetGateway_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,4),_MitelDhcpServerSubnetGateway_Type())
mitelDhcpServerSubnetGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerSubnetGateway.setStatus(_A)
class _MitelDhcpServerSubnetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MitelDhcpServerSubnetName_Type.__name__=_F
_MitelDhcpServerSubnetName_Object=MibTableColumn
mitelDhcpServerSubnetName=_MitelDhcpServerSubnetName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,5),_MitelDhcpServerSubnetName_Type())
mitelDhcpServerSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerSubnetName.setStatus(_A)
class _MitelDhcpServerSubnetDeleteTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpServerSubnetDeleteTree_Type.__name__=_E
_MitelDhcpServerSubnetDeleteTree_Object=MibTableColumn
mitelDhcpServerSubnetDeleteTree=_MitelDhcpServerSubnetDeleteTree_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,6),_MitelDhcpServerSubnetDeleteTree_Type())
mitelDhcpServerSubnetDeleteTree.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerSubnetDeleteTree.setStatus(_A)
_MitelDhcpServerSubnetStatus_Type=RowStatus
_MitelDhcpServerSubnetStatus_Object=MibTableColumn
mitelDhcpServerSubnetStatus=_MitelDhcpServerSubnetStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,2,1,7),_MitelDhcpServerSubnetStatus_Type())
mitelDhcpServerSubnetStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerSubnetStatus.setStatus(_A)
_MitelDhcpServerRangeTable_Object=MibTable
mitelDhcpServerRangeTable=_MitelDhcpServerRangeTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3))
if mibBuilder.loadTexts:mitelDhcpServerRangeTable.setStatus(_A)
_MitelDhcpServerRangeEntry_Object=MibTableRow
mitelDhcpServerRangeEntry=_MitelDhcpServerRangeEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1))
mitelDhcpServerRangeEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:mitelDhcpServerRangeEntry.setStatus(_A)
_MitelDhcpServerRangeStart_Type=IpAddress
_MitelDhcpServerRangeStart_Object=MibTableColumn
mitelDhcpServerRangeStart=_MitelDhcpServerRangeStart_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,1),_MitelDhcpServerRangeStart_Type())
mitelDhcpServerRangeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerRangeStart.setStatus(_A)
_MitelDhcpServerRangeEnd_Type=IpAddress
_MitelDhcpServerRangeEnd_Object=MibTableColumn
mitelDhcpServerRangeEnd=_MitelDhcpServerRangeEnd_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,2),_MitelDhcpServerRangeEnd_Type())
mitelDhcpServerRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerRangeEnd.setStatus(_A)
_MitelDhcpServerRangeSubnet_Type=IpAddress
_MitelDhcpServerRangeSubnet_Object=MibTableColumn
mitelDhcpServerRangeSubnet=_MitelDhcpServerRangeSubnet_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,3),_MitelDhcpServerRangeSubnet_Type())
mitelDhcpServerRangeSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerRangeSubnet.setStatus(_A)
_MitelDhcpServerRangeProtocol_Type=MitelDhcpServerProtocol
_MitelDhcpServerRangeProtocol_Object=MibTableColumn
mitelDhcpServerRangeProtocol=_MitelDhcpServerRangeProtocol_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,4),_MitelDhcpServerRangeProtocol_Type())
mitelDhcpServerRangeProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeProtocol.setStatus(_A)
class _MitelDhcpServerRangeGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_K,4)))
_MitelDhcpServerRangeGateway_Type.__name__=_E
_MitelDhcpServerRangeGateway_Object=MibTableColumn
mitelDhcpServerRangeGateway=_MitelDhcpServerRangeGateway_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,5),_MitelDhcpServerRangeGateway_Type())
mitelDhcpServerRangeGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeGateway.setStatus(_A)
_MitelDhcpServerRangeLeaseTime_Type=Integer32
_MitelDhcpServerRangeLeaseTime_Object=MibTableColumn
mitelDhcpServerRangeLeaseTime=_MitelDhcpServerRangeLeaseTime_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,6),_MitelDhcpServerRangeLeaseTime_Type())
mitelDhcpServerRangeLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeLeaseTime.setStatus(_A)
class _MitelDhcpServerRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MitelDhcpServerRangeName_Type.__name__=_F
_MitelDhcpServerRangeName_Object=MibTableColumn
mitelDhcpServerRangeName=_MitelDhcpServerRangeName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,7),_MitelDhcpServerRangeName_Type())
mitelDhcpServerRangeName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeName.setStatus(_A)
class _MitelDhcpServerRangeMatchClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpServerRangeMatchClassId_Type.__name__=_E
_MitelDhcpServerRangeMatchClassId_Object=MibTableColumn
mitelDhcpServerRangeMatchClassId=_MitelDhcpServerRangeMatchClassId_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,8),_MitelDhcpServerRangeMatchClassId_Type())
mitelDhcpServerRangeMatchClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeMatchClassId.setStatus(_A)
class _MitelDhcpServerRangeDeleteTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpServerRangeDeleteTree_Type.__name__=_E
_MitelDhcpServerRangeDeleteTree_Object=MibTableColumn
mitelDhcpServerRangeDeleteTree=_MitelDhcpServerRangeDeleteTree_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,9),_MitelDhcpServerRangeDeleteTree_Type())
mitelDhcpServerRangeDeleteTree.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerRangeDeleteTree.setStatus(_A)
_MitelDhcpServerRangeStatus_Type=RowStatus
_MitelDhcpServerRangeStatus_Object=MibTableColumn
mitelDhcpServerRangeStatus=_MitelDhcpServerRangeStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,3,1,10),_MitelDhcpServerRangeStatus_Type())
mitelDhcpServerRangeStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerRangeStatus.setStatus(_A)
_MitelDhcpServerStaticIpTable_Object=MibTable
mitelDhcpServerStaticIpTable=_MitelDhcpServerStaticIpTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4))
if mibBuilder.loadTexts:mitelDhcpServerStaticIpTable.setStatus(_A)
_MitelDhcpServerStaticIpEntry_Object=MibTableRow
mitelDhcpServerStaticIpEntry=_MitelDhcpServerStaticIpEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1))
mitelDhcpServerStaticIpEntry.setIndexNames((0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:mitelDhcpServerStaticIpEntry.setStatus(_A)
_MitelDhcpServerStaticIpAddr_Type=IpAddress
_MitelDhcpServerStaticIpAddr_Object=MibTableColumn
mitelDhcpServerStaticIpAddr=_MitelDhcpServerStaticIpAddr_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,1),_MitelDhcpServerStaticIpAddr_Type())
mitelDhcpServerStaticIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpAddr.setStatus(_A)
_MitelDhcpServerStaticIpSubnet_Type=IpAddress
_MitelDhcpServerStaticIpSubnet_Object=MibTableColumn
mitelDhcpServerStaticIpSubnet=_MitelDhcpServerStaticIpSubnet_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,2),_MitelDhcpServerStaticIpSubnet_Type())
mitelDhcpServerStaticIpSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpSubnet.setStatus(_A)
_MitelDhcpServerStaticIpProtocol_Type=MitelDhcpServerProtocol
_MitelDhcpServerStaticIpProtocol_Object=MibTableColumn
mitelDhcpServerStaticIpProtocol=_MitelDhcpServerStaticIpProtocol_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,3),_MitelDhcpServerStaticIpProtocol_Type())
mitelDhcpServerStaticIpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpProtocol.setStatus(_A)
class _MitelDhcpServerStaticIpGateway_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_K,4)))
_MitelDhcpServerStaticIpGateway_Type.__name__=_E
_MitelDhcpServerStaticIpGateway_Object=MibTableColumn
mitelDhcpServerStaticIpGateway=_MitelDhcpServerStaticIpGateway_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,4),_MitelDhcpServerStaticIpGateway_Type())
mitelDhcpServerStaticIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpGateway.setStatus(_A)
class _MitelDhcpServerStaticIpMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MitelDhcpServerStaticIpMacAddress_Type.__name__=_I
_MitelDhcpServerStaticIpMacAddress_Object=MibTableColumn
mitelDhcpServerStaticIpMacAddress=_MitelDhcpServerStaticIpMacAddress_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,5),_MitelDhcpServerStaticIpMacAddress_Type())
mitelDhcpServerStaticIpMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpMacAddress.setStatus(_A)
class _MitelDhcpServerStaticIpClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelDhcpServerStaticIpClientId_Type.__name__=_I
_MitelDhcpServerStaticIpClientId_Object=MibTableColumn
mitelDhcpServerStaticIpClientId=_MitelDhcpServerStaticIpClientId_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,6),_MitelDhcpServerStaticIpClientId_Type())
mitelDhcpServerStaticIpClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpClientId.setStatus(_A)
class _MitelDhcpServerStaticIpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MitelDhcpServerStaticIpName_Type.__name__=_F
_MitelDhcpServerStaticIpName_Object=MibTableColumn
mitelDhcpServerStaticIpName=_MitelDhcpServerStaticIpName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,7),_MitelDhcpServerStaticIpName_Type())
mitelDhcpServerStaticIpName.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpName.setStatus(_A)
class _MitelDhcpServerStaticIpDeleteTree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpServerStaticIpDeleteTree_Type.__name__=_E
_MitelDhcpServerStaticIpDeleteTree_Object=MibTableColumn
mitelDhcpServerStaticIpDeleteTree=_MitelDhcpServerStaticIpDeleteTree_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,8),_MitelDhcpServerStaticIpDeleteTree_Type())
mitelDhcpServerStaticIpDeleteTree.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpDeleteTree.setStatus(_A)
_MitelDhcpServerStaticIpStatus_Type=RowStatus
_MitelDhcpServerStaticIpStatus_Object=MibTableColumn
mitelDhcpServerStaticIpStatus=_MitelDhcpServerStaticIpStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,4,1,9),_MitelDhcpServerStaticIpStatus_Type())
mitelDhcpServerStaticIpStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerStaticIpStatus.setStatus(_A)
_MitelDhcpServerOptionTable_Object=MibTable
mitelDhcpServerOptionTable=_MitelDhcpServerOptionTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5))
if mibBuilder.loadTexts:mitelDhcpServerOptionTable.setStatus(_A)
_MitelDhcpServerOptionEntry_Object=MibTableRow
mitelDhcpServerOptionEntry=_MitelDhcpServerOptionEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1))
mitelDhcpServerOptionEntry.setIndexNames((0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:mitelDhcpServerOptionEntry.setStatus(_A)
_MitelDhcpServerOptionAddr_Type=IpAddress
_MitelDhcpServerOptionAddr_Object=MibTableColumn
mitelDhcpServerOptionAddr=_MitelDhcpServerOptionAddr_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1,1),_MitelDhcpServerOptionAddr_Type())
mitelDhcpServerOptionAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerOptionAddr.setStatus(_A)
_MitelDhcpServerOptionNumber_Type=MitelDhcpServerOptionList
_MitelDhcpServerOptionNumber_Object=MibTableColumn
mitelDhcpServerOptionNumber=_MitelDhcpServerOptionNumber_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1,2),_MitelDhcpServerOptionNumber_Type())
mitelDhcpServerOptionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerOptionNumber.setStatus(_A)
class _MitelDhcpServerOptionDisplayFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_MitelDhcpServerOptionDisplayFormat_Type.__name__=_E
_MitelDhcpServerOptionDisplayFormat_Object=MibTableColumn
mitelDhcpServerOptionDisplayFormat=_MitelDhcpServerOptionDisplayFormat_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1,3),_MitelDhcpServerOptionDisplayFormat_Type())
mitelDhcpServerOptionDisplayFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerOptionDisplayFormat.setStatus(_A)
class _MitelDhcpServerOptionValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MitelDhcpServerOptionValue_Type.__name__=_I
_MitelDhcpServerOptionValue_Object=MibTableColumn
mitelDhcpServerOptionValue=_MitelDhcpServerOptionValue_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1,4),_MitelDhcpServerOptionValue_Type())
mitelDhcpServerOptionValue.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerOptionValue.setStatus(_A)
_MitelDhcpServerOptionStatus_Type=RowStatus
_MitelDhcpServerOptionStatus_Object=MibTableColumn
mitelDhcpServerOptionStatus=_MitelDhcpServerOptionStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,5,1,5),_MitelDhcpServerOptionStatus_Type())
mitelDhcpServerOptionStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerOptionStatus.setStatus(_A)
_MitelDhcpServerLeaseTable_Object=MibTable
mitelDhcpServerLeaseTable=_MitelDhcpServerLeaseTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6))
if mibBuilder.loadTexts:mitelDhcpServerLeaseTable.setStatus(_A)
_MitelDhcpServerLeaseEntry_Object=MibTableRow
mitelDhcpServerLeaseEntry=_MitelDhcpServerLeaseEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1))
mitelDhcpServerLeaseEntry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:mitelDhcpServerLeaseEntry.setStatus(_A)
_MitelDhcpServerLeaseAddr_Type=IpAddress
_MitelDhcpServerLeaseAddr_Object=MibTableColumn
mitelDhcpServerLeaseAddr=_MitelDhcpServerLeaseAddr_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,1),_MitelDhcpServerLeaseAddr_Type())
mitelDhcpServerLeaseAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseAddr.setStatus(_A)
_MitelDhcpServerLeaseSubnet_Type=IpAddress
_MitelDhcpServerLeaseSubnet_Object=MibTableColumn
mitelDhcpServerLeaseSubnet=_MitelDhcpServerLeaseSubnet_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,2),_MitelDhcpServerLeaseSubnet_Type())
mitelDhcpServerLeaseSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseSubnet.setStatus(_A)
_MitelDhcpServerLeaseRange_Type=IpAddress
_MitelDhcpServerLeaseRange_Object=MibTableColumn
mitelDhcpServerLeaseRange=_MitelDhcpServerLeaseRange_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,3),_MitelDhcpServerLeaseRange_Type())
mitelDhcpServerLeaseRange.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseRange.setStatus(_A)
class _MitelDhcpServerLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('static',1),('dynamic',2),('configuration-reserved',3),('server-reserved',4)))
_MitelDhcpServerLeaseType_Type.__name__=_E
_MitelDhcpServerLeaseType_Object=MibTableColumn
mitelDhcpServerLeaseType=_MitelDhcpServerLeaseType_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,4),_MitelDhcpServerLeaseType_Type())
mitelDhcpServerLeaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseType.setStatus(_A)
_MitelDhcpServerLeaseEndTime_Type=TimeTicks
_MitelDhcpServerLeaseEndTime_Object=MibTableColumn
mitelDhcpServerLeaseEndTime=_MitelDhcpServerLeaseEndTime_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,5),_MitelDhcpServerLeaseEndTime_Type())
mitelDhcpServerLeaseEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseEndTime.setStatus(_A)
class _MitelDhcpServerLeaseAllowedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3),(_U,4)))
_MitelDhcpServerLeaseAllowedProtocol_Type.__name__=_E
_MitelDhcpServerLeaseAllowedProtocol_Object=MibTableColumn
mitelDhcpServerLeaseAllowedProtocol=_MitelDhcpServerLeaseAllowedProtocol_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,6),_MitelDhcpServerLeaseAllowedProtocol_Type())
mitelDhcpServerLeaseAllowedProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseAllowedProtocol.setStatus(_A)
class _MitelDhcpServerLeaseServedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3)))
_MitelDhcpServerLeaseServedProtocol_Type.__name__=_E
_MitelDhcpServerLeaseServedProtocol_Object=MibTableColumn
mitelDhcpServerLeaseServedProtocol=_MitelDhcpServerLeaseServedProtocol_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,7),_MitelDhcpServerLeaseServedProtocol_Type())
mitelDhcpServerLeaseServedProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseServedProtocol.setStatus(_A)
class _MitelDhcpServerLeaseMacAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MitelDhcpServerLeaseMacAddress_Type.__name__=_I
_MitelDhcpServerLeaseMacAddress_Object=MibTableColumn
mitelDhcpServerLeaseMacAddress=_MitelDhcpServerLeaseMacAddress_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,8),_MitelDhcpServerLeaseMacAddress_Type())
mitelDhcpServerLeaseMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseMacAddress.setStatus(_A)
class _MitelDhcpServerLeaseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelDhcpServerLeaseClientId_Type.__name__=_I
_MitelDhcpServerLeaseClientId_Object=MibTableColumn
mitelDhcpServerLeaseClientId=_MitelDhcpServerLeaseClientId_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,9),_MitelDhcpServerLeaseClientId_Type())
mitelDhcpServerLeaseClientId.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseClientId.setStatus(_A)
class _MitelDhcpServerLeaseHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_MitelDhcpServerLeaseHostName_Type.__name__=_F
_MitelDhcpServerLeaseHostName_Object=MibTableColumn
mitelDhcpServerLeaseHostName=_MitelDhcpServerLeaseHostName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,10),_MitelDhcpServerLeaseHostName_Type())
mitelDhcpServerLeaseHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseHostName.setStatus(_A)
class _MitelDhcpServerLeaseDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelDhcpServerLeaseDomainName_Type.__name__=_F
_MitelDhcpServerLeaseDomainName_Object=MibTableColumn
mitelDhcpServerLeaseDomainName=_MitelDhcpServerLeaseDomainName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,11),_MitelDhcpServerLeaseDomainName_Type())
mitelDhcpServerLeaseDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseDomainName.setStatus(_A)
_MitelDhcpServerLeaseServedTime_Type=Integer32
_MitelDhcpServerLeaseServedTime_Object=MibTableColumn
mitelDhcpServerLeaseServedTime=_MitelDhcpServerLeaseServedTime_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,12),_MitelDhcpServerLeaseServedTime_Type())
mitelDhcpServerLeaseServedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerLeaseServedTime.setStatus(_A)
_MitelDhcpServerLeaseStatus_Type=RowStatus
_MitelDhcpServerLeaseStatus_Object=MibTableColumn
mitelDhcpServerLeaseStatus=_MitelDhcpServerLeaseStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,6,1,13),_MitelDhcpServerLeaseStatus_Type())
mitelDhcpServerLeaseStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerLeaseStatus.setStatus(_A)
_MitelDhcpServerStatsGroup_ObjectIdentity=ObjectIdentity
mitelDhcpServerStatsGroup=_MitelDhcpServerStatsGroup_ObjectIdentity((1,3,6,1,4,1,1027,4,8,1,3,5,7))
_MitelDhcpServerStatsNumServers_Type=Integer32
_MitelDhcpServerStatsNumServers_Object=MibScalar
mitelDhcpServerStatsNumServers=_MitelDhcpServerStatsNumServers_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,1),_MitelDhcpServerStatsNumServers_Type())
mitelDhcpServerStatsNumServers.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsNumServers.setStatus(_A)
_MitelDhcpServerStatsConfSubnets_Type=Integer32
_MitelDhcpServerStatsConfSubnets_Object=MibScalar
mitelDhcpServerStatsConfSubnets=_MitelDhcpServerStatsConfSubnets_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,2),_MitelDhcpServerStatsConfSubnets_Type())
mitelDhcpServerStatsConfSubnets.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsConfSubnets.setStatus(_A)
_MitelDhcpServerStatsConfRanges_Type=Integer32
_MitelDhcpServerStatsConfRanges_Object=MibScalar
mitelDhcpServerStatsConfRanges=_MitelDhcpServerStatsConfRanges_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,3),_MitelDhcpServerStatsConfRanges_Type())
mitelDhcpServerStatsConfRanges.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsConfRanges.setStatus(_A)
_MitelDhcpServerStatsConfStatic_Type=Integer32
_MitelDhcpServerStatsConfStatic_Object=MibScalar
mitelDhcpServerStatsConfStatic=_MitelDhcpServerStatsConfStatic_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,4),_MitelDhcpServerStatsConfStatic_Type())
mitelDhcpServerStatsConfStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsConfStatic.setStatus(_A)
_MitelDhcpServerStatsConfOptions_Type=Integer32
_MitelDhcpServerStatsConfOptions_Object=MibScalar
mitelDhcpServerStatsConfOptions=_MitelDhcpServerStatsConfOptions_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,5),_MitelDhcpServerStatsConfOptions_Type())
mitelDhcpServerStatsConfOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsConfOptions.setStatus(_A)
_MitelDhcpServerStatsConfLeases_Type=Integer32
_MitelDhcpServerStatsConfLeases_Object=MibScalar
mitelDhcpServerStatsConfLeases=_MitelDhcpServerStatsConfLeases_Object((1,3,6,1,4,1,1027,4,8,1,3,5,7,6),_MitelDhcpServerStatsConfLeases_Type())
mitelDhcpServerStatsConfLeases.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerStatsConfLeases.setStatus(_A)
_MitelDhcpServerVendorInfoTable_Object=MibTable
mitelDhcpServerVendorInfoTable=_MitelDhcpServerVendorInfoTable_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8))
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoTable.setStatus(_A)
_MitelDhcpServerVendorInfoEntry_Object=MibTableRow
mitelDhcpServerVendorInfoEntry=_MitelDhcpServerVendorInfoEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1))
mitelDhcpServerVendorInfoEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_i))
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoEntry.setStatus(_A)
class _MitelDhcpServerVendorInfoID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MitelDhcpServerVendorInfoID_Type.__name__=_F
_MitelDhcpServerVendorInfoID_Object=MibTableColumn
mitelDhcpServerVendorInfoID=_MitelDhcpServerVendorInfoID_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1,1),_MitelDhcpServerVendorInfoID_Type())
mitelDhcpServerVendorInfoID.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoID.setStatus(_A)
class _MitelDhcpServerVendorInfoName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MitelDhcpServerVendorInfoName_Type.__name__=_F
_MitelDhcpServerVendorInfoName_Object=MibTableColumn
mitelDhcpServerVendorInfoName=_MitelDhcpServerVendorInfoName_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1,2),_MitelDhcpServerVendorInfoName_Type())
mitelDhcpServerVendorInfoName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoName.setStatus(_A)
class _MitelDhcpServerVendorInfoOptionDisplayFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_d,2),(_e,3),(_f,4),(_g,5)))
_MitelDhcpServerVendorInfoOptionDisplayFormat_Type.__name__=_E
_MitelDhcpServerVendorInfoOptionDisplayFormat_Object=MibTableColumn
mitelDhcpServerVendorInfoOptionDisplayFormat=_MitelDhcpServerVendorInfoOptionDisplayFormat_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1,3),_MitelDhcpServerVendorInfoOptionDisplayFormat_Type())
mitelDhcpServerVendorInfoOptionDisplayFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoOptionDisplayFormat.setStatus(_A)
class _MitelDhcpServerVendorInfoOptionValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_MitelDhcpServerVendorInfoOptionValue_Type.__name__=_I
_MitelDhcpServerVendorInfoOptionValue_Object=MibScalar
mitelDhcpServerVendorInfoOptionValue=_MitelDhcpServerVendorInfoOptionValue_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1,4),_MitelDhcpServerVendorInfoOptionValue_Type())
mitelDhcpServerVendorInfoOptionValue.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoOptionValue.setStatus(_A)
_MitelDhcpServerVendorInfoStatus_Type=RowStatus
_MitelDhcpServerVendorInfoStatus_Object=MibTableColumn
mitelDhcpServerVendorInfoStatus=_MitelDhcpServerVendorInfoStatus_Object((1,3,6,1,4,1,1027,4,8,1,3,5,8,1,5),_MitelDhcpServerVendorInfoStatus_Type())
mitelDhcpServerVendorInfoStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:mitelDhcpServerVendorInfoStatus.setStatus(_A)
_MitelDhcpClientTable_Object=MibTable
mitelDhcpClientTable=_MitelDhcpClientTable_Object((1,3,6,1,4,1,1027,4,8,1,3,6))
if mibBuilder.loadTexts:mitelDhcpClientTable.setStatus(_A)
_MitelDhcpClientEntry_Object=MibTableRow
mitelDhcpClientEntry=_MitelDhcpClientEntry_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1))
mitelDhcpClientEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:mitelDhcpClientEntry.setStatus(_A)
_MitelDhcpClientIndex_Type=Integer32
_MitelDhcpClientIndex_Object=MibTableColumn
mitelDhcpClientIndex=_MitelDhcpClientIndex_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,1),_MitelDhcpClientIndex_Type())
mitelDhcpClientIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientIndex.setStatus(_A)
_MitelDhcpClientId_Type=OctetString
_MitelDhcpClientId_Object=MibTableColumn
mitelDhcpClientId=_MitelDhcpClientId_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,2),_MitelDhcpClientId_Type())
mitelDhcpClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelDhcpClientId.setStatus(_A)
class _MitelDhcpClientLeaseAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('release',2),('renew',3)))
_MitelDhcpClientLeaseAction_Type.__name__=_E
_MitelDhcpClientLeaseAction_Object=MibTableColumn
mitelDhcpClientLeaseAction=_MitelDhcpClientLeaseAction_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,3),_MitelDhcpClientLeaseAction_Type())
mitelDhcpClientLeaseAction.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientLeaseAction.setStatus(_A)
_MitelDhcpClientIpAddress_Type=IpAddress
_MitelDhcpClientIpAddress_Object=MibTableColumn
mitelDhcpClientIpAddress=_MitelDhcpClientIpAddress_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,4),_MitelDhcpClientIpAddress_Type())
mitelDhcpClientIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientIpAddress.setStatus(_A)
_MitelDhcpClientLeaseObtained_Type=TimeTicks
_MitelDhcpClientLeaseObtained_Object=MibTableColumn
mitelDhcpClientLeaseObtained=_MitelDhcpClientLeaseObtained_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,5),_MitelDhcpClientLeaseObtained_Type())
mitelDhcpClientLeaseObtained.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientLeaseObtained.setStatus(_A)
_MitelDhcpClientLeaseExpired_Type=TimeTicks
_MitelDhcpClientLeaseExpired_Object=MibTableColumn
mitelDhcpClientLeaseExpired=_MitelDhcpClientLeaseExpired_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,6),_MitelDhcpClientLeaseExpired_Type())
mitelDhcpClientLeaseExpired.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientLeaseExpired.setStatus(_A)
_MitelDhcpClientDefaultGateway_Type=IpAddress
_MitelDhcpClientDefaultGateway_Object=MibTableColumn
mitelDhcpClientDefaultGateway=_MitelDhcpClientDefaultGateway_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,7),_MitelDhcpClientDefaultGateway_Type())
mitelDhcpClientDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientDefaultGateway.setStatus(_A)
_MitelDhcpClientServerIp_Type=IpAddress
_MitelDhcpClientServerIp_Object=MibTableColumn
mitelDhcpClientServerIp=_MitelDhcpClientServerIp_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,8),_MitelDhcpClientServerIp_Type())
mitelDhcpClientServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientServerIp.setStatus(_A)
_MitelDhcpClientPrimaryDns_Type=IpAddress
_MitelDhcpClientPrimaryDns_Object=MibTableColumn
mitelDhcpClientPrimaryDns=_MitelDhcpClientPrimaryDns_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,9),_MitelDhcpClientPrimaryDns_Type())
mitelDhcpClientPrimaryDns.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientPrimaryDns.setStatus(_A)
_MitelDhcpClientSecondaryDns_Type=IpAddress
_MitelDhcpClientSecondaryDns_Object=MibTableColumn
mitelDhcpClientSecondaryDns=_MitelDhcpClientSecondaryDns_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,10),_MitelDhcpClientSecondaryDns_Type())
mitelDhcpClientSecondaryDns.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientSecondaryDns.setStatus(_A)
_MitelDhcpClientPrimaryWins_Type=IpAddress
_MitelDhcpClientPrimaryWins_Object=MibTableColumn
mitelDhcpClientPrimaryWins=_MitelDhcpClientPrimaryWins_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,11),_MitelDhcpClientPrimaryWins_Type())
mitelDhcpClientPrimaryWins.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientPrimaryWins.setStatus(_A)
_MitelDhcpClientSecondaryWins_Type=IpAddress
_MitelDhcpClientSecondaryWins_Object=MibTableColumn
mitelDhcpClientSecondaryWins=_MitelDhcpClientSecondaryWins_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,12),_MitelDhcpClientSecondaryWins_Type())
mitelDhcpClientSecondaryWins.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientSecondaryWins.setStatus(_A)
_MitelDhcpClientDomainName_Type=OctetString
_MitelDhcpClientDomainName_Object=MibTableColumn
mitelDhcpClientDomainName=_MitelDhcpClientDomainName_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,13),_MitelDhcpClientDomainName_Type())
mitelDhcpClientDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientDomainName.setStatus(_A)
_MitelDhcpClientName_Type=OctetString
_MitelDhcpClientName_Object=MibTableColumn
mitelDhcpClientName=_MitelDhcpClientName_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,14),_MitelDhcpClientName_Type())
mitelDhcpClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientName.setStatus(_A)
class _MitelDhcpClientAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MitelDhcpClientAdminState_Type.__name__=_E
_MitelDhcpClientAdminState_Object=MibTableColumn
mitelDhcpClientAdminState=_MitelDhcpClientAdminState_Object((1,3,6,1,4,1,1027,4,8,1,3,6,1,15),_MitelDhcpClientAdminState_Type())
mitelDhcpClientAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelDhcpClientAdminState.setStatus(_A)
mitelDhcpClientObtainedIp=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,404))
mitelDhcpClientObtainedIp.setObjects(*((_D,_P),(_D,_j),(_D,_k)))
if mibBuilder.loadTexts:mitelDhcpClientObtainedIp.setStatus(_A)
mitelDhcpClientLeaseExpiry=NotificationType((1,3,6,1,4,1,1027,1,2,4,0,405))
mitelDhcpClientLeaseExpiry.setObjects((_D,_P))
if mibBuilder.loadTexts:mitelDhcpClientLeaseExpiry.setStatus(_A)
mitelIpera1000Notifications=NotificationGroup((1,3,6,1,4,1,1027,1,2,4,0))
mitelIpera1000Notifications.setObjects(*((_D,_l),(_D,_m)))
if mibBuilder.loadTexts:mitelIpera1000Notifications.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MitelDhcpServerProtocol':MitelDhcpServerProtocol,'MitelDhcpServerOptionList':MitelDhcpServerOptionList,'mitel':mitel,'mitelIdentification':mitelIdentification,'mitelIdCallServers':mitelIdCallServers,'mitelIdCsIpera1000':mitelIdCsIpera1000,'mitelIpera1000Notifications':mitelIpera1000Notifications,_l:mitelDhcpClientObtainedIp,_m:mitelDhcpClientLeaseExpiry,'mitelProprietary':mitelProprietary,'mitelPropIpNetworking':mitelPropIpNetworking,'mitelIpNetRouter':mitelIpNetRouter,'mitelRouterDhcpGroup':mitelRouterDhcpGroup,'mitelDhcpRelayAgentEnable':mitelDhcpRelayAgentEnable,'mitelDhcpRelayAgentMaxHops':mitelDhcpRelayAgentMaxHops,'mitelDhcpRelayAgentServerTable':mitelDhcpRelayAgentServerTable,'mitelDhcpRelayAgentServerEntry':mitelDhcpRelayAgentServerEntry,_V:mitelDhcpRelayAgentServerAddr,'mitelDhcpRelayAgentServerName':mitelDhcpRelayAgentServerName,'mitelDhcpRelayAgentServerStatus':mitelDhcpRelayAgentServerStatus,'mitelDhcpRelayAgentBroadcast':mitelDhcpRelayAgentBroadcast,'mitelDhcpServerGroup':mitelDhcpServerGroup,'mitelDhcpServerGeneralGroup':mitelDhcpServerGeneralGroup,'mitelDhcpServerGeneralEnable':mitelDhcpServerGeneralEnable,'mitelDhcpServerGeneralGateway':mitelDhcpServerGeneralGateway,'mitelDhcpServerGeneralRefDhcpServer':mitelDhcpServerGeneralRefDhcpServer,'mitelDhcpServerGeneralPingStatus':mitelDhcpServerGeneralPingStatus,'mitelDhcpServerSubnetTable':mitelDhcpServerSubnetTable,'mitelDhcpServerSubnetEntry':mitelDhcpServerSubnetEntry,_W:mitelDhcpServerSubnetAddr,_X:mitelDhcpServerSubnetSharedNet,'mitelDhcpServerSubnetMask':mitelDhcpServerSubnetMask,'mitelDhcpServerSubnetGateway':mitelDhcpServerSubnetGateway,'mitelDhcpServerSubnetName':mitelDhcpServerSubnetName,'mitelDhcpServerSubnetDeleteTree':mitelDhcpServerSubnetDeleteTree,'mitelDhcpServerSubnetStatus':mitelDhcpServerSubnetStatus,'mitelDhcpServerRangeTable':mitelDhcpServerRangeTable,'mitelDhcpServerRangeEntry':mitelDhcpServerRangeEntry,_Y:mitelDhcpServerRangeStart,_Z:mitelDhcpServerRangeEnd,_a:mitelDhcpServerRangeSubnet,'mitelDhcpServerRangeProtocol':mitelDhcpServerRangeProtocol,'mitelDhcpServerRangeGateway':mitelDhcpServerRangeGateway,'mitelDhcpServerRangeLeaseTime':mitelDhcpServerRangeLeaseTime,'mitelDhcpServerRangeName':mitelDhcpServerRangeName,'mitelDhcpServerRangeMatchClassId':mitelDhcpServerRangeMatchClassId,'mitelDhcpServerRangeDeleteTree':mitelDhcpServerRangeDeleteTree,'mitelDhcpServerRangeStatus':mitelDhcpServerRangeStatus,'mitelDhcpServerStaticIpTable':mitelDhcpServerStaticIpTable,'mitelDhcpServerStaticIpEntry':mitelDhcpServerStaticIpEntry,_b:mitelDhcpServerStaticIpAddr,_c:mitelDhcpServerStaticIpSubnet,'mitelDhcpServerStaticIpProtocol':mitelDhcpServerStaticIpProtocol,'mitelDhcpServerStaticIpGateway':mitelDhcpServerStaticIpGateway,'mitelDhcpServerStaticIpMacAddress':mitelDhcpServerStaticIpMacAddress,'mitelDhcpServerStaticIpClientId':mitelDhcpServerStaticIpClientId,'mitelDhcpServerStaticIpName':mitelDhcpServerStaticIpName,'mitelDhcpServerStaticIpDeleteTree':mitelDhcpServerStaticIpDeleteTree,'mitelDhcpServerStaticIpStatus':mitelDhcpServerStaticIpStatus,'mitelDhcpServerOptionTable':mitelDhcpServerOptionTable,'mitelDhcpServerOptionEntry':mitelDhcpServerOptionEntry,_S:mitelDhcpServerOptionAddr,_T:mitelDhcpServerOptionNumber,'mitelDhcpServerOptionDisplayFormat':mitelDhcpServerOptionDisplayFormat,'mitelDhcpServerOptionValue':mitelDhcpServerOptionValue,'mitelDhcpServerOptionStatus':mitelDhcpServerOptionStatus,'mitelDhcpServerLeaseTable':mitelDhcpServerLeaseTable,'mitelDhcpServerLeaseEntry':mitelDhcpServerLeaseEntry,_h:mitelDhcpServerLeaseAddr,'mitelDhcpServerLeaseSubnet':mitelDhcpServerLeaseSubnet,'mitelDhcpServerLeaseRange':mitelDhcpServerLeaseRange,'mitelDhcpServerLeaseType':mitelDhcpServerLeaseType,'mitelDhcpServerLeaseEndTime':mitelDhcpServerLeaseEndTime,'mitelDhcpServerLeaseAllowedProtocol':mitelDhcpServerLeaseAllowedProtocol,'mitelDhcpServerLeaseServedProtocol':mitelDhcpServerLeaseServedProtocol,'mitelDhcpServerLeaseMacAddress':mitelDhcpServerLeaseMacAddress,'mitelDhcpServerLeaseClientId':mitelDhcpServerLeaseClientId,'mitelDhcpServerLeaseHostName':mitelDhcpServerLeaseHostName,'mitelDhcpServerLeaseDomainName':mitelDhcpServerLeaseDomainName,'mitelDhcpServerLeaseServedTime':mitelDhcpServerLeaseServedTime,'mitelDhcpServerLeaseStatus':mitelDhcpServerLeaseStatus,'mitelDhcpServerStatsGroup':mitelDhcpServerStatsGroup,'mitelDhcpServerStatsNumServers':mitelDhcpServerStatsNumServers,'mitelDhcpServerStatsConfSubnets':mitelDhcpServerStatsConfSubnets,'mitelDhcpServerStatsConfRanges':mitelDhcpServerStatsConfRanges,'mitelDhcpServerStatsConfStatic':mitelDhcpServerStatsConfStatic,'mitelDhcpServerStatsConfOptions':mitelDhcpServerStatsConfOptions,'mitelDhcpServerStatsConfLeases':mitelDhcpServerStatsConfLeases,'mitelDhcpServerVendorInfoTable':mitelDhcpServerVendorInfoTable,'mitelDhcpServerVendorInfoEntry':mitelDhcpServerVendorInfoEntry,_i:mitelDhcpServerVendorInfoID,'mitelDhcpServerVendorInfoName':mitelDhcpServerVendorInfoName,'mitelDhcpServerVendorInfoOptionDisplayFormat':mitelDhcpServerVendorInfoOptionDisplayFormat,'mitelDhcpServerVendorInfoOptionValue':mitelDhcpServerVendorInfoOptionValue,'mitelDhcpServerVendorInfoStatus':mitelDhcpServerVendorInfoStatus,'mitelDhcpClientTable':mitelDhcpClientTable,'mitelDhcpClientEntry':mitelDhcpClientEntry,_P:mitelDhcpClientIndex,'mitelDhcpClientId':mitelDhcpClientId,'mitelDhcpClientLeaseAction':mitelDhcpClientLeaseAction,_j:mitelDhcpClientIpAddress,'mitelDhcpClientLeaseObtained':mitelDhcpClientLeaseObtained,'mitelDhcpClientLeaseExpired':mitelDhcpClientLeaseExpired,'mitelDhcpClientDefaultGateway':mitelDhcpClientDefaultGateway,_k:mitelDhcpClientServerIp,'mitelDhcpClientPrimaryDns':mitelDhcpClientPrimaryDns,'mitelDhcpClientSecondaryDns':mitelDhcpClientSecondaryDns,'mitelDhcpClientPrimaryWins':mitelDhcpClientPrimaryWins,'mitelDhcpClientSecondaryWins':mitelDhcpClientSecondaryWins,'mitelDhcpClientDomainName':mitelDhcpClientDomainName,'mitelDhcpClientName':mitelDhcpClientName,'mitelDhcpClientAdminState':mitelDhcpClientAdminState})