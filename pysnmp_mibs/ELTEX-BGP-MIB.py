_A5='eltexBgpPathAttrClusterLocIndex'
_A4='EltexBgpSafi'
_A3='EltexBgpAfi'
_A2='eltexBgpNetworkPrfxLen'
_A1='eltexBgpNetworkPrfx'
_A0='eltexBgpNetworkPrfxType'
_z='eltexBgpNetworkSafi'
_y='eltexBgpNetworkAfi'
_x='eltexBgpAdjRibOutPathId'
_w='eltexBgpAdjRibOutPrfxLen'
_v='eltexBgpAdjRibOutPrfx'
_u='eltexBgpAdjRibOutPrfxType'
_t='eltexBgpAdjRibOutSafi'
_s='eltexBgpAdjRibOutAfi'
_r='eltexBgpPeerStatusPeerIndex'
_q='eltexBgpAdjRibInPathId'
_p='eltexBgpAdjRibInPrfxLen'
_o='eltexBgpAdjRibInPrfx'
_n='eltexBgpAdjRibInPrfxType'
_m='eltexBgpAdjRibInSafi'
_l='eltexBgpAdjRibInAfi'
_k='eltexBgpAdjRibInPeerIndex'
_j='eltexBgpLocRibPrfxType'
_i='eltexBgpPeerGroupName'
_h='EltexBgpCeaseErrorSubcode'
_g='eltexBgpProcessAddrFamilySafi'
_f='eltexBgpProcessAddrFamilyAfi'
_e='EltexBgpASNotation'
_d='active'
_c='eltexBgpLocRibPathId'
_b='eltexBgpLocRibPeerRibIndex'
_a='eltexBgpLocRibPeerOrRib'
_Z='eltexBgpLocRibPrfxLen'
_Y='eltexBgpLocRibPrfx'
_X='eltexBgpLocRibSafi'
_W='eltexBgpLocRibAfi'
_V='eltexBgpPeerAddrFamilySafi'
_U='eltexBgpPeerAddrFamilyAfi'
_T='00000000'
_S='EltexBgpAdminStatus'
_R='Integer32'
_Q='InterfaceIndexOrZero'
_P='EltexBgpPeerReflectorClientType'
_O='EltexBgpConfigDropOrWarn'
_N='EltexBgpIdentifier'
_M='read-create'
_L='eltexBgpPeerRemoteAddr'
_K='eltexBgpPeerRemoteAddrType'
_J='none'
_I='OctetString'
_H='eltexBgpProcessId'
_G='TruthValue'
_F='not-accessible'
_E='Unsigned32'
_D='ELTEX-BGP-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_Q)
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp',_G)
eltexBgpMIB=ModuleIdentity((1,3,6,1,4,1,35265,45))
class EltexBgpIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class EltexBgpAfi(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,25)));namedValues=NamedValues(*(('other',0),('ipv4',1),('ipv6',2),('l2vpn',25)))
class EltexBgpSafi(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,65,70,128,241)));namedValues=NamedValues(*((_J,0),('unicast',1),('multicast',2),('both',3),('labeled',4),('vpls',65),('evpn',70),('mplsBgpVpn',128),('private',241)))
class EltexBgpAutonomousSystemNumber(TextualConvention,Unsigned32):status=_A
class EltexBgpAsSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoOctet',1),('fourOctet',2)))
class EltexBgpAdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
class EltexBgpOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operStatusUp',1),('operStatusDown',2),('operStatusGoingUp',3),('operStatusGoingDown',4),('operStatusActFailed',5)))
class EltexBgpOriginCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('originIgp',0),('originEgp',1),('originIncomplete',2)))
class EltexBgpConfigDropOrWarn(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('drop',1),('warn',2)))
class EltexBgpPeerOrRib(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('peerIndex',1),('ribIndex',2)))
class EltexBgpPeerStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),('idle',1),('connect',2),(_d,3),('opensent',4),('openconfirm',5),('established',6)))
class EltexBgpPeerEvents(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('noEvent',0),('start',1),('stop',2),('transportOpen',3),('transportClosed',4),('transportOpenFailed',5),('transportFatalError',6),('connectRetryTimer',7),('holdTimer',8),('keepaliverTimer',9),('recvOpen',10),('recvKeepAlive',11),('recvUpdate',12),('recvNotification',13),('connParmsUpdate',14)))
class EltexBgpCapabilities(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('mpIpv4Unicast',0),('mpIpv4Multicast',1),('mpIpv4Vpn',2),('mpIpv4Label',3),('mpIpv6Unicast',4),('mpIpv6Multicast',5),('mpIpv6Vpn',6),('mpIpv6Label',7),('routeRefresh',8),('gracefulRestart',9),('routeRefreshCisco',10),('outboundRouteFilter',11),('outboundRouteFilterCisco',12),('fourOctetAs',13),('mpL2vpnVpls',14),('addPath',15),('mpL2vpnEvpn',16),('mpIpv4Private',17),('enhancedRouteRefresh',18)))
class EltexBgpCeaseErrorSubcode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,6,8)));namedValues=NamedValues(*((_J,0),('adminShutdown',2),('peerUnconfig',3),('adminReset',4),('configChange',6),('noResource',8)))
class EltexBgpNlriIsActiveFlag(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notTracked',1),('inactive',2),(_d,3)))
class EltexBgpPeerConfigStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stateUpToDate',1),('stateOutOfDateAdminDown',2),('stateOutOfDateRowInactive',3)))
class EltexBgpReasonNotBest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('notConsidered',0),('routeIsBest',1),('weight',2),('localPref',3),('localOrigPreferred',4),('asPathLen',5),('origin',6),('med',7),('localOrigTieBreaker',8),('ebgpVsibgp',9),('adminDistance',10),('pathCostToNextHop',11),('prefExisting',12),('identifier',13),('clusterLen',14),('peerType',15),('peerAddress',16),('peerPort',17),('pathId',18)))
class EltexBgpNlriPeerTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('iBGP',2),('eBGP',3)))
class EltexBgpASNotation(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('asplainASNumber',1),('asdotASnumber',2)))
class EltexBgpPeerReflectorClientType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nonClient',0),('client',1),('meshedClient',2)))
class EltexBgpRouteMapAsPathAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),('set',1)))
class EltexBgpAddPathSrCap(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('disable',0),('receive',1),('send',2),('both',3),('inherit',4),('unknown',5)))
class EltexBfdSessionStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('bfdSessNotRequired',0),('bfdSessInitial',1),('bfdSessActivating',2),('bfdSessActive',3),('bfdSessInactive',4),('bfdSessAdminDown',5),('bfdSessNoContact',6)))
_EltexBgpObjects_ObjectIdentity=ObjectIdentity
eltexBgpObjects=_EltexBgpObjects_ObjectIdentity((1,3,6,1,4,1,35265,45,1))
_EltexBgpProcess_ObjectIdentity=ObjectIdentity
eltexBgpProcess=_EltexBgpProcess_ObjectIdentity((1,3,6,1,4,1,35265,45,1,1))
_EltexBgpProcessTable_Object=MibTable
eltexBgpProcessTable=_EltexBgpProcessTable_Object((1,3,6,1,4,1,35265,45,1,1,1))
if mibBuilder.loadTexts:eltexBgpProcessTable.setStatus(_A)
_EltexBgpProcessEntry_Object=MibTableRow
eltexBgpProcessEntry=_EltexBgpProcessEntry_Object((1,3,6,1,4,1,35265,45,1,1,1,1))
eltexBgpProcessEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:eltexBgpProcessEntry.setStatus(_A)
_EltexBgpProcessId_Type=Unsigned32
_EltexBgpProcessId_Object=MibTableColumn
eltexBgpProcessId=_EltexBgpProcessId_Object((1,3,6,1,4,1,35265,45,1,1,1,1,1),_EltexBgpProcessId_Type())
eltexBgpProcessId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpProcessId.setStatus(_A)
_EltexBgpProcessRowStatus_Type=RowStatus
_EltexBgpProcessRowStatus_Object=MibTableColumn
eltexBgpProcessRowStatus=_EltexBgpProcessRowStatus_Object((1,3,6,1,4,1,35265,45,1,1,1,1,2),_EltexBgpProcessRowStatus_Type())
eltexBgpProcessRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:eltexBgpProcessRowStatus.setStatus(_A)
class _EltexBgpProcessAdminStatus_Type(EltexBgpAdminStatus):defaultValue=2
_EltexBgpProcessAdminStatus_Type.__name__=_S
_EltexBgpProcessAdminStatus_Object=MibTableColumn
eltexBgpProcessAdminStatus=_EltexBgpProcessAdminStatus_Object((1,3,6,1,4,1,35265,45,1,1,1,1,3),_EltexBgpProcessAdminStatus_Type())
eltexBgpProcessAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessAdminStatus.setStatus(_A)
_EltexBgpProcessOperStatus_Type=EltexBgpOperStatus
_EltexBgpProcessOperStatus_Object=MibTableColumn
eltexBgpProcessOperStatus=_EltexBgpProcessOperStatus_Object((1,3,6,1,4,1,35265,45,1,1,1,1,4),_EltexBgpProcessOperStatus_Type())
eltexBgpProcessOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpProcessOperStatus.setStatus(_A)
_EltexBgpProcessLocalAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpProcessLocalAs_Object=MibTableColumn
eltexBgpProcessLocalAs=_EltexBgpProcessLocalAs_Object((1,3,6,1,4,1,35265,45,1,1,1,1,5),_EltexBgpProcessLocalAs_Type())
eltexBgpProcessLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessLocalAs.setStatus(_A)
class _EltexBgpProcessLocalIdentifier_Type(EltexBgpIdentifier):defaultHexValue=_T
_EltexBgpProcessLocalIdentifier_Type.__name__=_N
_EltexBgpProcessLocalIdentifier_Object=MibTableColumn
eltexBgpProcessLocalIdentifier=_EltexBgpProcessLocalIdentifier_Object((1,3,6,1,4,1,35265,45,1,1,1,1,6),_EltexBgpProcessLocalIdentifier_Type())
eltexBgpProcessLocalIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessLocalIdentifier.setStatus(_A)
_EltexBgpProcessOperLocalIdentifier_Type=EltexBgpIdentifier
_EltexBgpProcessOperLocalIdentifier_Object=MibTableColumn
eltexBgpProcessOperLocalIdentifier=_EltexBgpProcessOperLocalIdentifier_Object((1,3,6,1,4,1,35265,45,1,1,1,1,7),_EltexBgpProcessOperLocalIdentifier_Type())
eltexBgpProcessOperLocalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpProcessOperLocalIdentifier.setStatus(_A)
class _EltexBgpProcessTableVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EltexBgpProcessTableVersion_Type.__name__=_E
_EltexBgpProcessTableVersion_Object=MibTableColumn
eltexBgpProcessTableVersion=_EltexBgpProcessTableVersion_Object((1,3,6,1,4,1,35265,45,1,1,1,1,8),_EltexBgpProcessTableVersion_Type())
eltexBgpProcessTableVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpProcessTableVersion.setStatus(_A)
class _EltexBgpProcessASNotation_Type(EltexBgpASNotation):defaultValue=1
_EltexBgpProcessASNotation_Type.__name__=_e
_EltexBgpProcessASNotation_Object=MibTableColumn
eltexBgpProcessASNotation=_EltexBgpProcessASNotation_Object((1,3,6,1,4,1,35265,45,1,1,1,1,9),_EltexBgpProcessASNotation_Type())
eltexBgpProcessASNotation.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessASNotation.setStatus(_A)
class _EltexBgpProcessClusterIdentifier_Type(EltexBgpIdentifier):defaultHexValue=_T
_EltexBgpProcessClusterIdentifier_Type.__name__=_N
_EltexBgpProcessClusterIdentifier_Object=MibTableColumn
eltexBgpProcessClusterIdentifier=_EltexBgpProcessClusterIdentifier_Object((1,3,6,1,4,1,35265,45,1,1,1,1,10),_EltexBgpProcessClusterIdentifier_Type())
eltexBgpProcessClusterIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessClusterIdentifier.setStatus(_A)
class _EltexBgpProcessOperClusterIdentifier_Type(EltexBgpIdentifier):defaultHexValue=_T
_EltexBgpProcessOperClusterIdentifier_Type.__name__=_N
_EltexBgpProcessOperClusterIdentifier_Object=MibTableColumn
eltexBgpProcessOperClusterIdentifier=_EltexBgpProcessOperClusterIdentifier_Object((1,3,6,1,4,1,35265,45,1,1,1,1,11),_EltexBgpProcessOperClusterIdentifier_Type())
eltexBgpProcessOperClusterIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpProcessOperClusterIdentifier.setStatus(_A)
class _EltexBgpProcessInterClientReflEnabled_Type(TruthValue):defaultValue=1
_EltexBgpProcessInterClientReflEnabled_Type.__name__=_G
_EltexBgpProcessInterClientReflEnabled_Object=MibTableColumn
eltexBgpProcessInterClientReflEnabled=_EltexBgpProcessInterClientReflEnabled_Object((1,3,6,1,4,1,35265,45,1,1,1,1,12),_EltexBgpProcessInterClientReflEnabled_Type())
eltexBgpProcessInterClientReflEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessInterClientReflEnabled.setStatus(_A)
class _EltexBgpProcessPathMtuDiscovery_Type(TruthValue):defaultValue=2
_EltexBgpProcessPathMtuDiscovery_Type.__name__=_G
_EltexBgpProcessPathMtuDiscovery_Object=MibTableColumn
eltexBgpProcessPathMtuDiscovery=_EltexBgpProcessPathMtuDiscovery_Object((1,3,6,1,4,1,35265,45,1,1,1,1,13),_EltexBgpProcessPathMtuDiscovery_Type())
eltexBgpProcessPathMtuDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessPathMtuDiscovery.setStatus(_A)
_EltexBgpProcessAddrFamilyTable_Object=MibTable
eltexBgpProcessAddrFamilyTable=_EltexBgpProcessAddrFamilyTable_Object((1,3,6,1,4,1,35265,45,1,1,2))
if mibBuilder.loadTexts:eltexBgpProcessAddrFamilyTable.setStatus(_A)
_EltexBgpProcessAddrFamilyEntry_Object=MibTableRow
eltexBgpProcessAddrFamilyEntry=_EltexBgpProcessAddrFamilyEntry_Object((1,3,6,1,4,1,35265,45,1,1,2,1))
eltexBgpProcessAddrFamilyEntry.setIndexNames((0,_D,_H),(0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:eltexBgpProcessAddrFamilyEntry.setStatus(_A)
_EltexBgpProcessAddrFamilyAfi_Type=EltexBgpAfi
_EltexBgpProcessAddrFamilyAfi_Object=MibTableColumn
eltexBgpProcessAddrFamilyAfi=_EltexBgpProcessAddrFamilyAfi_Object((1,3,6,1,4,1,35265,45,1,1,2,1,2),_EltexBgpProcessAddrFamilyAfi_Type())
eltexBgpProcessAddrFamilyAfi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpProcessAddrFamilyAfi.setStatus(_A)
_EltexBgpProcessAddrFamilySafi_Type=EltexBgpSafi
_EltexBgpProcessAddrFamilySafi_Object=MibTableColumn
eltexBgpProcessAddrFamilySafi=_EltexBgpProcessAddrFamilySafi_Object((1,3,6,1,4,1,35265,45,1,1,2,1,3),_EltexBgpProcessAddrFamilySafi_Type())
eltexBgpProcessAddrFamilySafi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpProcessAddrFamilySafi.setStatus(_A)
_EltexBgpProcessAddrFamilyRowStatus_Type=RowStatus
_EltexBgpProcessAddrFamilyRowStatus_Object=MibTableColumn
eltexBgpProcessAddrFamilyRowStatus=_EltexBgpProcessAddrFamilyRowStatus_Object((1,3,6,1,4,1,35265,45,1,1,2,1,4),_EltexBgpProcessAddrFamilyRowStatus_Type())
eltexBgpProcessAddrFamilyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpProcessAddrFamilyRowStatus.setStatus(_A)
_EltexBgpPeer_ObjectIdentity=ObjectIdentity
eltexBgpPeer=_EltexBgpPeer_ObjectIdentity((1,3,6,1,4,1,35265,45,1,2))
_EltexBgpPeerData_ObjectIdentity=ObjectIdentity
eltexBgpPeerData=_EltexBgpPeerData_ObjectIdentity((1,3,6,1,4,1,35265,45,1,2,1))
_EltexBgpPeerTable_Object=MibTable
eltexBgpPeerTable=_EltexBgpPeerTable_Object((1,3,6,1,4,1,35265,45,1,2,1,1))
if mibBuilder.loadTexts:eltexBgpPeerTable.setStatus(_A)
_EltexBgpPeerEntry_Object=MibTableRow
eltexBgpPeerEntry=_EltexBgpPeerEntry_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1))
eltexBgpPeerEntry.setIndexNames((0,_D,_H),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:eltexBgpPeerEntry.setStatus(_A)
_EltexBgpPeerRemoteAddrType_Type=InetAddressType
_EltexBgpPeerRemoteAddrType_Object=MibTableColumn
eltexBgpPeerRemoteAddrType=_EltexBgpPeerRemoteAddrType_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,1),_EltexBgpPeerRemoteAddrType_Type())
eltexBgpPeerRemoteAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPeerRemoteAddrType.setStatus(_A)
_EltexBgpPeerRemoteAddr_Type=InetAddress
_EltexBgpPeerRemoteAddr_Object=MibTableColumn
eltexBgpPeerRemoteAddr=_EltexBgpPeerRemoteAddr_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,2),_EltexBgpPeerRemoteAddr_Type())
eltexBgpPeerRemoteAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPeerRemoteAddr.setStatus(_A)
_EltexBgpPeerRowStatus_Type=RowStatus
_EltexBgpPeerRowStatus_Object=MibTableColumn
eltexBgpPeerRowStatus=_EltexBgpPeerRowStatus_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,3),_EltexBgpPeerRowStatus_Type())
eltexBgpPeerRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:eltexBgpPeerRowStatus.setStatus(_A)
class _EltexBgpPeerAdminStatus_Type(EltexBgpAdminStatus):defaultValue=2
_EltexBgpPeerAdminStatus_Type.__name__=_S
_EltexBgpPeerAdminStatus_Object=MibTableColumn
eltexBgpPeerAdminStatus=_EltexBgpPeerAdminStatus_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,4),_EltexBgpPeerAdminStatus_Type())
eltexBgpPeerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAdminStatus.setStatus(_A)
_EltexBgpPeerOperStatus_Type=EltexBgpOperStatus
_EltexBgpPeerOperStatus_Object=MibTableColumn
eltexBgpPeerOperStatus=_EltexBgpPeerOperStatus_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,5),_EltexBgpPeerOperStatus_Type())
eltexBgpPeerOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerOperStatus.setStatus(_A)
_EltexBgpPeerRemoteAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpPeerRemoteAs_Object=MibTableColumn
eltexBgpPeerRemoteAs=_EltexBgpPeerRemoteAs_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,6),_EltexBgpPeerRemoteAs_Type())
eltexBgpPeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerRemoteAs.setStatus(_A)
class _EltexBgpPeerSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_EltexBgpPeerSourceInterface_Type.__name__=_Q
_EltexBgpPeerSourceInterface_Object=MibTableColumn
eltexBgpPeerSourceInterface=_EltexBgpPeerSourceInterface_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,7),_EltexBgpPeerSourceInterface_Type())
eltexBgpPeerSourceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerSourceInterface.setStatus(_A)
class _EltexBgpPeerNxtHopSlf_Type(TruthValue):defaultValue=2
_EltexBgpPeerNxtHopSlf_Type.__name__=_G
_EltexBgpPeerNxtHopSlf_Object=MibTableColumn
eltexBgpPeerNxtHopSlf=_EltexBgpPeerNxtHopSlf_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,8),_EltexBgpPeerNxtHopSlf_Type())
eltexBgpPeerNxtHopSlf.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerNxtHopSlf.setStatus(_A)
class _EltexBgpPeerConfigMaxPrfx_Type(Unsigned32):defaultValue=0
_EltexBgpPeerConfigMaxPrfx_Type.__name__=_E
_EltexBgpPeerConfigMaxPrfx_Object=MibTableColumn
eltexBgpPeerConfigMaxPrfx=_EltexBgpPeerConfigMaxPrfx_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,9),_EltexBgpPeerConfigMaxPrfx_Type())
eltexBgpPeerConfigMaxPrfx.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigMaxPrfx.setStatus(_A)
class _EltexBgpPeerConfigDropWarn_Type(EltexBgpConfigDropOrWarn):defaultValue=2
_EltexBgpPeerConfigDropWarn_Type.__name__=_O
_EltexBgpPeerConfigDropWarn_Object=MibTableColumn
eltexBgpPeerConfigDropWarn=_EltexBgpPeerConfigDropWarn_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,10),_EltexBgpPeerConfigDropWarn_Type())
eltexBgpPeerConfigDropWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigDropWarn.setStatus(_A)
class _EltexBgpPeerMaxPrfxHold_Type(Unsigned32):defaultValue=90
_EltexBgpPeerMaxPrfxHold_Type.__name__=_E
_EltexBgpPeerMaxPrfxHold_Object=MibTableColumn
eltexBgpPeerMaxPrfxHold=_EltexBgpPeerMaxPrfxHold_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,11),_EltexBgpPeerMaxPrfxHold_Type())
eltexBgpPeerMaxPrfxHold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerMaxPrfxHold.setStatus(_A)
class _EltexBgpPeerConfigThreshold_Type(Unsigned32):defaultValue=75
_EltexBgpPeerConfigThreshold_Type.__name__=_E
_EltexBgpPeerConfigThreshold_Object=MibTableColumn
eltexBgpPeerConfigThreshold=_EltexBgpPeerConfigThreshold_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,12),_EltexBgpPeerConfigThreshold_Type())
eltexBgpPeerConfigThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigThreshold.setStatus(_A)
class _EltexBgpPeerConnectRetryInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexBgpPeerConnectRetryInterval_Type.__name__=_E
_EltexBgpPeerConnectRetryInterval_Object=MibTableColumn
eltexBgpPeerConnectRetryInterval=_EltexBgpPeerConnectRetryInterval_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,13),_EltexBgpPeerConnectRetryInterval_Type())
eltexBgpPeerConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConnectRetryInterval.setStatus(_A)
class _EltexBgpPeerHoldTimeConfigd_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerHoldTimeConfigd_Type.__name__=_E
_EltexBgpPeerHoldTimeConfigd_Object=MibTableColumn
eltexBgpPeerHoldTimeConfigd=_EltexBgpPeerHoldTimeConfigd_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,14),_EltexBgpPeerHoldTimeConfigd_Type())
eltexBgpPeerHoldTimeConfigd.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerHoldTimeConfigd.setStatus(_A)
class _EltexBgpPeerKeepAliveConfigd_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_EltexBgpPeerKeepAliveConfigd_Type.__name__=_E
_EltexBgpPeerKeepAliveConfigd_Object=MibTableColumn
eltexBgpPeerKeepAliveConfigd=_EltexBgpPeerKeepAliveConfigd_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,15),_EltexBgpPeerKeepAliveConfigd_Type())
eltexBgpPeerKeepAliveConfigd.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerKeepAliveConfigd.setStatus(_A)
class _EltexBgpPeerMinRouteAdvertiseInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerMinRouteAdvertiseInterval_Type.__name__=_E
_EltexBgpPeerMinRouteAdvertiseInterval_Object=MibTableColumn
eltexBgpPeerMinRouteAdvertiseInterval=_EltexBgpPeerMinRouteAdvertiseInterval_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,16),_EltexBgpPeerMinRouteAdvertiseInterval_Type())
eltexBgpPeerMinRouteAdvertiseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerMinRouteAdvertiseInterval.setStatus(_A)
class _EltexBgpPeerMinASOriginationInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerMinASOriginationInterval_Type.__name__=_E
_EltexBgpPeerMinASOriginationInterval_Object=MibTableColumn
eltexBgpPeerMinASOriginationInterval=_EltexBgpPeerMinASOriginationInterval_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,17),_EltexBgpPeerMinASOriginationInterval_Type())
eltexBgpPeerMinASOriginationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerMinASOriginationInterval.setStatus(_A)
class _EltexBgpPeerMinRouteWithdrawInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerMinRouteWithdrawInterval_Type.__name__=_E
_EltexBgpPeerMinRouteWithdrawInterval_Object=MibTableColumn
eltexBgpPeerMinRouteWithdrawInterval=_EltexBgpPeerMinRouteWithdrawInterval_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,18),_EltexBgpPeerMinRouteWithdrawInterval_Type())
eltexBgpPeerMinRouteWithdrawInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerMinRouteWithdrawInterval.setStatus(_A)
class _EltexBgpPeerConfigOpenDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_EltexBgpPeerConfigOpenDelay_Type.__name__=_E
_EltexBgpPeerConfigOpenDelay_Object=MibTableColumn
eltexBgpPeerConfigOpenDelay=_EltexBgpPeerConfigOpenDelay_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,19),_EltexBgpPeerConfigOpenDelay_Type())
eltexBgpPeerConfigOpenDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigOpenDelay.setStatus(_A)
class _EltexBgpPeerConfigIdleHold_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_EltexBgpPeerConfigIdleHold_Type.__name__=_E
_EltexBgpPeerConfigIdleHold_Object=MibTableColumn
eltexBgpPeerConfigIdleHold=_EltexBgpPeerConfigIdleHold_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,20),_EltexBgpPeerConfigIdleHold_Type())
eltexBgpPeerConfigIdleHold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigIdleHold.setStatus(_A)
_EltexBgpPeerDistListPlIn_Type=DisplayString
_EltexBgpPeerDistListPlIn_Object=MibTableColumn
eltexBgpPeerDistListPlIn=_EltexBgpPeerDistListPlIn_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,21),_EltexBgpPeerDistListPlIn_Type())
eltexBgpPeerDistListPlIn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerDistListPlIn.setStatus(_A)
_EltexBgpPeerDistListPlOut_Type=DisplayString
_EltexBgpPeerDistListPlOut_Object=MibTableColumn
eltexBgpPeerDistListPlOut=_EltexBgpPeerDistListPlOut_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,22),_EltexBgpPeerDistListPlOut_Type())
eltexBgpPeerDistListPlOut.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerDistListPlOut.setStatus(_A)
class _EltexBgpPeerReflectorClient_Type(EltexBgpPeerReflectorClientType):defaultValue=0
_EltexBgpPeerReflectorClient_Type.__name__=_P
_EltexBgpPeerReflectorClient_Object=MibTableColumn
eltexBgpPeerReflectorClient=_EltexBgpPeerReflectorClient_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,23),_EltexBgpPeerReflectorClient_Type())
eltexBgpPeerReflectorClient.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerReflectorClient.setStatus(_A)
class _EltexBgpPeerSoftResetWithStoredInfo_Type(TruthValue):defaultValue=2
_EltexBgpPeerSoftResetWithStoredInfo_Type.__name__=_G
_EltexBgpPeerSoftResetWithStoredInfo_Object=MibTableColumn
eltexBgpPeerSoftResetWithStoredInfo=_EltexBgpPeerSoftResetWithStoredInfo_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,24),_EltexBgpPeerSoftResetWithStoredInfo_Type())
eltexBgpPeerSoftResetWithStoredInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerSoftResetWithStoredInfo.setStatus(_A)
_EltexBgpPeerConfigPeerGroup_Type=DisplayString
_EltexBgpPeerConfigPeerGroup_Object=MibTableColumn
eltexBgpPeerConfigPeerGroup=_EltexBgpPeerConfigPeerGroup_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,25),_EltexBgpPeerConfigPeerGroup_Type())
eltexBgpPeerConfigPeerGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerConfigPeerGroup.setStatus(_A)
class _EltexBgpPeerPathMtuDiscovery_Type(TruthValue):defaultValue=2
_EltexBgpPeerPathMtuDiscovery_Type.__name__=_G
_EltexBgpPeerPathMtuDiscovery_Object=MibTableColumn
eltexBgpPeerPathMtuDiscovery=_EltexBgpPeerPathMtuDiscovery_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,26),_EltexBgpPeerPathMtuDiscovery_Type())
eltexBgpPeerPathMtuDiscovery.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerPathMtuDiscovery.setStatus(_A)
class _EltexBgpPeerBfdDesired_Type(TruthValue):defaultValue=2
_EltexBgpPeerBfdDesired_Type.__name__=_G
_EltexBgpPeerBfdDesired_Object=MibTableColumn
eltexBgpPeerBfdDesired=_EltexBgpPeerBfdDesired_Object((1,3,6,1,4,1,35265,45,1,2,1,1,1,27),_EltexBgpPeerBfdDesired_Type())
eltexBgpPeerBfdDesired.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerBfdDesired.setStatus(_A)
_EltexBgpPeerAddrFamilyTable_Object=MibTable
eltexBgpPeerAddrFamilyTable=_EltexBgpPeerAddrFamilyTable_Object((1,3,6,1,4,1,35265,45,1,2,1,2))
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyTable.setStatus(_A)
_EltexBgpPeerAddrFamilyEntry_Object=MibTableRow
eltexBgpPeerAddrFamilyEntry=_EltexBgpPeerAddrFamilyEntry_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1))
eltexBgpPeerAddrFamilyEntry.setIndexNames((0,_D,_H),(0,_D,_K),(0,_D,_L),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyEntry.setStatus(_A)
_EltexBgpPeerAddrFamilyAfi_Type=EltexBgpAfi
_EltexBgpPeerAddrFamilyAfi_Object=MibTableColumn
eltexBgpPeerAddrFamilyAfi=_EltexBgpPeerAddrFamilyAfi_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,1),_EltexBgpPeerAddrFamilyAfi_Type())
eltexBgpPeerAddrFamilyAfi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyAfi.setStatus(_A)
_EltexBgpPeerAddrFamilySafi_Type=EltexBgpSafi
_EltexBgpPeerAddrFamilySafi_Object=MibTableColumn
eltexBgpPeerAddrFamilySafi=_EltexBgpPeerAddrFamilySafi_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,2),_EltexBgpPeerAddrFamilySafi_Type())
eltexBgpPeerAddrFamilySafi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilySafi.setStatus(_A)
class _EltexBgpPeerAddrFamilyDisable_Type(TruthValue):defaultValue=1
_EltexBgpPeerAddrFamilyDisable_Type.__name__=_G
_EltexBgpPeerAddrFamilyDisable_Object=MibTableColumn
eltexBgpPeerAddrFamilyDisable=_EltexBgpPeerAddrFamilyDisable_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,3),_EltexBgpPeerAddrFamilyDisable_Type())
eltexBgpPeerAddrFamilyDisable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyDisable.setStatus(_A)
class _EltexBgpPeerAddrFamilyNxtHopSlf_Type(TruthValue):defaultValue=1
_EltexBgpPeerAddrFamilyNxtHopSlf_Type.__name__=_G
_EltexBgpPeerAddrFamilyNxtHopSlf_Object=MibTableColumn
eltexBgpPeerAddrFamilyNxtHopSlf=_EltexBgpPeerAddrFamilyNxtHopSlf_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,4),_EltexBgpPeerAddrFamilyNxtHopSlf_Type())
eltexBgpPeerAddrFamilyNxtHopSlf.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyNxtHopSlf.setStatus(_A)
class _EltexBgpPeerAddrFamilyConfigMaxPrfx_Type(Unsigned32):defaultValue=0
_EltexBgpPeerAddrFamilyConfigMaxPrfx_Type.__name__=_E
_EltexBgpPeerAddrFamilyConfigMaxPrfx_Object=MibTableColumn
eltexBgpPeerAddrFamilyConfigMaxPrfx=_EltexBgpPeerAddrFamilyConfigMaxPrfx_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,5),_EltexBgpPeerAddrFamilyConfigMaxPrfx_Type())
eltexBgpPeerAddrFamilyConfigMaxPrfx.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyConfigMaxPrfx.setStatus(_A)
class _EltexBgpPeerAddrFamilyConfigDropWarn_Type(EltexBgpConfigDropOrWarn):defaultValue=2
_EltexBgpPeerAddrFamilyConfigDropWarn_Type.__name__=_O
_EltexBgpPeerAddrFamilyConfigDropWarn_Object=MibTableColumn
eltexBgpPeerAddrFamilyConfigDropWarn=_EltexBgpPeerAddrFamilyConfigDropWarn_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,6),_EltexBgpPeerAddrFamilyConfigDropWarn_Type())
eltexBgpPeerAddrFamilyConfigDropWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyConfigDropWarn.setStatus(_A)
class _EltexBgpPeerAddrFamilyMaxPrfxHold_Type(Unsigned32):defaultValue=90
_EltexBgpPeerAddrFamilyMaxPrfxHold_Type.__name__=_E
_EltexBgpPeerAddrFamilyMaxPrfxHold_Object=MibTableColumn
eltexBgpPeerAddrFamilyMaxPrfxHold=_EltexBgpPeerAddrFamilyMaxPrfxHold_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,7),_EltexBgpPeerAddrFamilyMaxPrfxHold_Type())
eltexBgpPeerAddrFamilyMaxPrfxHold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyMaxPrfxHold.setStatus(_A)
class _EltexBgpPeerAddrFamilyConfigThreshold_Type(Unsigned32):defaultValue=75
_EltexBgpPeerAddrFamilyConfigThreshold_Type.__name__=_E
_EltexBgpPeerAddrFamilyConfigThreshold_Object=MibTableColumn
eltexBgpPeerAddrFamilyConfigThreshold=_EltexBgpPeerAddrFamilyConfigThreshold_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,8),_EltexBgpPeerAddrFamilyConfigThreshold_Type())
eltexBgpPeerAddrFamilyConfigThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyConfigThreshold.setStatus(_A)
class _EltexBgpPeerAddrFamilyMinRteAdvertInt_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerAddrFamilyMinRteAdvertInt_Type.__name__=_E
_EltexBgpPeerAddrFamilyMinRteAdvertInt_Object=MibTableColumn
eltexBgpPeerAddrFamilyMinRteAdvertInt=_EltexBgpPeerAddrFamilyMinRteAdvertInt_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,9),_EltexBgpPeerAddrFamilyMinRteAdvertInt_Type())
eltexBgpPeerAddrFamilyMinRteAdvertInt.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyMinRteAdvertInt.setStatus(_A)
class _EltexBgpPeerAddrFamilyMinASOrigInt_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexBgpPeerAddrFamilyMinASOrigInt_Type.__name__=_E
_EltexBgpPeerAddrFamilyMinASOrigInt_Object=MibTableColumn
eltexBgpPeerAddrFamilyMinASOrigInt=_EltexBgpPeerAddrFamilyMinASOrigInt_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,10),_EltexBgpPeerAddrFamilyMinASOrigInt_Type())
eltexBgpPeerAddrFamilyMinASOrigInt.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyMinASOrigInt.setStatus(_A)
class _EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type.__name__=_E
_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Object=MibTableColumn
eltexBgpPeerAddrFamilyMinRteWithdrawInt=_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,11),_EltexBgpPeerAddrFamilyMinRteWithdrawInt_Type())
eltexBgpPeerAddrFamilyMinRteWithdrawInt.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyMinRteWithdrawInt.setStatus(_A)
class _EltexBgpPeerAddrFamilyReflectorClient_Type(EltexBgpPeerReflectorClientType):defaultValue=0
_EltexBgpPeerAddrFamilyReflectorClient_Type.__name__=_P
_EltexBgpPeerAddrFamilyReflectorClient_Object=MibTableColumn
eltexBgpPeerAddrFamilyReflectorClient=_EltexBgpPeerAddrFamilyReflectorClient_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,12),_EltexBgpPeerAddrFamilyReflectorClient_Type())
eltexBgpPeerAddrFamilyReflectorClient.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyReflectorClient.setStatus(_A)
_EltexBgpPeerAddrFamilyRouteMapIn_Type=DisplayString
_EltexBgpPeerAddrFamilyRouteMapIn_Object=MibTableColumn
eltexBgpPeerAddrFamilyRouteMapIn=_EltexBgpPeerAddrFamilyRouteMapIn_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,13),_EltexBgpPeerAddrFamilyRouteMapIn_Type())
eltexBgpPeerAddrFamilyRouteMapIn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyRouteMapIn.setStatus(_A)
_EltexBgpPeerAddrFamilyRouteMapOut_Type=DisplayString
_EltexBgpPeerAddrFamilyRouteMapOut_Object=MibTableColumn
eltexBgpPeerAddrFamilyRouteMapOut=_EltexBgpPeerAddrFamilyRouteMapOut_Object((1,3,6,1,4,1,35265,45,1,2,1,2,1,14),_EltexBgpPeerAddrFamilyRouteMapOut_Type())
eltexBgpPeerAddrFamilyRouteMapOut.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyRouteMapOut.setStatus(_A)
_EltexBgpPeerStatusTable_Object=MibTable
eltexBgpPeerStatusTable=_EltexBgpPeerStatusTable_Object((1,3,6,1,4,1,35265,45,1,2,1,3))
if mibBuilder.loadTexts:eltexBgpPeerStatusTable.setStatus(_A)
_EltexBgpPeerStatusEntry_Object=MibTableRow
eltexBgpPeerStatusEntry=_EltexBgpPeerStatusEntry_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1))
eltexBgpPeerStatusEntry.setIndexNames((0,_D,_H),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:eltexBgpPeerStatusEntry.setStatus(_A)
_EltexBgpPeerStatusIdentifier_Type=EltexBgpIdentifier
_EltexBgpPeerStatusIdentifier_Object=MibTableColumn
eltexBgpPeerStatusIdentifier=_EltexBgpPeerStatusIdentifier_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,1),_EltexBgpPeerStatusIdentifier_Type())
eltexBgpPeerStatusIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusIdentifier.setStatus(_A)
_EltexBgpPeerStatusState_Type=EltexBgpPeerStates
_EltexBgpPeerStatusState_Object=MibTableColumn
eltexBgpPeerStatusState=_EltexBgpPeerStatusState_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,2),_EltexBgpPeerStatusState_Type())
eltexBgpPeerStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusState.setStatus(_A)
_EltexBgpPeerStatusDynamicPeer_Type=TruthValue
_EltexBgpPeerStatusDynamicPeer_Object=MibTableColumn
eltexBgpPeerStatusDynamicPeer=_EltexBgpPeerStatusDynamicPeer_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,3),_EltexBgpPeerStatusDynamicPeer_Type())
eltexBgpPeerStatusDynamicPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusDynamicPeer.setStatus(_A)
_EltexBgpPeerStatusRemoteAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusRemoteAs_Object=MibTableColumn
eltexBgpPeerStatusRemoteAs=_EltexBgpPeerStatusRemoteAs_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,4),_EltexBgpPeerStatusRemoteAs_Type())
eltexBgpPeerStatusRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusRemoteAs.setStatus(_A)
_EltexBgpPeerStatusPeerIndex_Type=Unsigned32
_EltexBgpPeerStatusPeerIndex_Object=MibTableColumn
eltexBgpPeerStatusPeerIndex=_EltexBgpPeerStatusPeerIndex_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,5),_EltexBgpPeerStatusPeerIndex_Type())
eltexBgpPeerStatusPeerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusPeerIndex.setStatus(_A)
_EltexBgpPeerStatusCapsSupport_Type=TruthValue
_EltexBgpPeerStatusCapsSupport_Object=MibTableColumn
eltexBgpPeerStatusCapsSupport=_EltexBgpPeerStatusCapsSupport_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,6),_EltexBgpPeerStatusCapsSupport_Type())
eltexBgpPeerStatusCapsSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusCapsSupport.setStatus(_A)
class _EltexBgpPeerStatusLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EltexBgpPeerStatusLastError_Type.__name__=_I
_EltexBgpPeerStatusLastError_Object=MibTableColumn
eltexBgpPeerStatusLastError=_EltexBgpPeerStatusLastError_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,7),_EltexBgpPeerStatusLastError_Type())
eltexBgpPeerStatusLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastError.setStatus(_A)
_EltexBgpPeerStatusLastErrorDataLen_Type=Unsigned32
_EltexBgpPeerStatusLastErrorDataLen_Object=MibTableColumn
eltexBgpPeerStatusLastErrorDataLen=_EltexBgpPeerStatusLastErrorDataLen_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,8),_EltexBgpPeerStatusLastErrorDataLen_Type())
eltexBgpPeerStatusLastErrorDataLen.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorDataLen.setStatus(_A)
class _EltexBgpPeerStatusLastErrorData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_EltexBgpPeerStatusLastErrorData_Type.__name__=_I
_EltexBgpPeerStatusLastErrorData_Object=MibTableColumn
eltexBgpPeerStatusLastErrorData=_EltexBgpPeerStatusLastErrorData_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,9),_EltexBgpPeerStatusLastErrorData_Type())
eltexBgpPeerStatusLastErrorData.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorData.setStatus(_A)
_EltexBgpPeerStatusFsmEstablishedTime_Type=Gauge32
_EltexBgpPeerStatusFsmEstablishedTime_Object=MibTableColumn
eltexBgpPeerStatusFsmEstablishedTime=_EltexBgpPeerStatusFsmEstablishedTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,10),_EltexBgpPeerStatusFsmEstablishedTime_Type())
eltexBgpPeerStatusFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusFsmEstablishedTime.setStatus(_A)
_EltexBgpPeerStatusInUpdatesElpsTime_Type=Gauge32
_EltexBgpPeerStatusInUpdatesElpsTime_Object=MibTableColumn
eltexBgpPeerStatusInUpdatesElpsTime=_EltexBgpPeerStatusInUpdatesElpsTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,11),_EltexBgpPeerStatusInUpdatesElpsTime_Type())
eltexBgpPeerStatusInUpdatesElpsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInUpdatesElpsTime.setStatus(_A)
_EltexBgpPeerStatusHoldTime_Type=Integer32
_EltexBgpPeerStatusHoldTime_Object=MibTableColumn
eltexBgpPeerStatusHoldTime=_EltexBgpPeerStatusHoldTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,12),_EltexBgpPeerStatusHoldTime_Type())
eltexBgpPeerStatusHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusHoldTime.setStatus(_A)
_EltexBgpPeerStatusKeepAlive_Type=Integer32
_EltexBgpPeerStatusKeepAlive_Object=MibTableColumn
eltexBgpPeerStatusKeepAlive=_EltexBgpPeerStatusKeepAlive_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,13),_EltexBgpPeerStatusKeepAlive_Type())
eltexBgpPeerStatusKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusKeepAlive.setStatus(_A)
_EltexBgpPeerStatusInOpens_Type=Counter32
_EltexBgpPeerStatusInOpens_Object=MibTableColumn
eltexBgpPeerStatusInOpens=_EltexBgpPeerStatusInOpens_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,14),_EltexBgpPeerStatusInOpens_Type())
eltexBgpPeerStatusInOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInOpens.setStatus(_A)
_EltexBgpPeerStatusOutOpens_Type=Counter32
_EltexBgpPeerStatusOutOpens_Object=MibTableColumn
eltexBgpPeerStatusOutOpens=_EltexBgpPeerStatusOutOpens_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,15),_EltexBgpPeerStatusOutOpens_Type())
eltexBgpPeerStatusOutOpens.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutOpens.setStatus(_A)
_EltexBgpPeerStatusInNotifications_Type=Counter32
_EltexBgpPeerStatusInNotifications_Object=MibTableColumn
eltexBgpPeerStatusInNotifications=_EltexBgpPeerStatusInNotifications_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,16),_EltexBgpPeerStatusInNotifications_Type())
eltexBgpPeerStatusInNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInNotifications.setStatus(_A)
_EltexBgpPeerStatusOutNotifications_Type=Counter32
_EltexBgpPeerStatusOutNotifications_Object=MibTableColumn
eltexBgpPeerStatusOutNotifications=_EltexBgpPeerStatusOutNotifications_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,17),_EltexBgpPeerStatusOutNotifications_Type())
eltexBgpPeerStatusOutNotifications.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutNotifications.setStatus(_A)
_EltexBgpPeerStatusInUpdates_Type=Counter32
_EltexBgpPeerStatusInUpdates_Object=MibTableColumn
eltexBgpPeerStatusInUpdates=_EltexBgpPeerStatusInUpdates_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,18),_EltexBgpPeerStatusInUpdates_Type())
eltexBgpPeerStatusInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInUpdates.setStatus(_A)
_EltexBgpPeerStatusOutUpdates_Type=Counter32
_EltexBgpPeerStatusOutUpdates_Object=MibTableColumn
eltexBgpPeerStatusOutUpdates=_EltexBgpPeerStatusOutUpdates_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,19),_EltexBgpPeerStatusOutUpdates_Type())
eltexBgpPeerStatusOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutUpdates.setStatus(_A)
_EltexBgpPeerStatusInKeepalives_Type=Counter32
_EltexBgpPeerStatusInKeepalives_Object=MibTableColumn
eltexBgpPeerStatusInKeepalives=_EltexBgpPeerStatusInKeepalives_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,20),_EltexBgpPeerStatusInKeepalives_Type())
eltexBgpPeerStatusInKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInKeepalives.setStatus(_A)
_EltexBgpPeerStatusOutKeepalives_Type=Counter32
_EltexBgpPeerStatusOutKeepalives_Object=MibTableColumn
eltexBgpPeerStatusOutKeepalives=_EltexBgpPeerStatusOutKeepalives_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,21),_EltexBgpPeerStatusOutKeepalives_Type())
eltexBgpPeerStatusOutKeepalives.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutKeepalives.setStatus(_A)
_EltexBgpPeerStatusInRefreshes_Type=Counter32
_EltexBgpPeerStatusInRefreshes_Object=MibTableColumn
eltexBgpPeerStatusInRefreshes=_EltexBgpPeerStatusInRefreshes_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,22),_EltexBgpPeerStatusInRefreshes_Type())
eltexBgpPeerStatusInRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInRefreshes.setStatus(_A)
_EltexBgpPeerStatusOutRefreshes_Type=Counter32
_EltexBgpPeerStatusOutRefreshes_Object=MibTableColumn
eltexBgpPeerStatusOutRefreshes=_EltexBgpPeerStatusOutRefreshes_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,23),_EltexBgpPeerStatusOutRefreshes_Type())
eltexBgpPeerStatusOutRefreshes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutRefreshes.setStatus(_A)
_EltexBgpPeerStatusInTotalMessages_Type=Counter32
_EltexBgpPeerStatusInTotalMessages_Object=MibTableColumn
eltexBgpPeerStatusInTotalMessages=_EltexBgpPeerStatusInTotalMessages_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,24),_EltexBgpPeerStatusInTotalMessages_Type())
eltexBgpPeerStatusInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInTotalMessages.setStatus(_A)
_EltexBgpPeerStatusOutTotalMessages_Type=Counter32
_EltexBgpPeerStatusOutTotalMessages_Object=MibTableColumn
eltexBgpPeerStatusOutTotalMessages=_EltexBgpPeerStatusOutTotalMessages_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,25),_EltexBgpPeerStatusOutTotalMessages_Type())
eltexBgpPeerStatusOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutTotalMessages.setStatus(_A)
_EltexBgpPeerStatusFsmEstTransitions_Type=Counter32
_EltexBgpPeerStatusFsmEstTransitions_Object=MibTableColumn
eltexBgpPeerStatusFsmEstTransitions=_EltexBgpPeerStatusFsmEstTransitions_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,26),_EltexBgpPeerStatusFsmEstTransitions_Type())
eltexBgpPeerStatusFsmEstTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusFsmEstTransitions.setStatus(_A)
_EltexBgpPeerStatusConnectRetryCount_Type=Counter32
_EltexBgpPeerStatusConnectRetryCount_Object=MibTableColumn
eltexBgpPeerStatusConnectRetryCount=_EltexBgpPeerStatusConnectRetryCount_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,27),_EltexBgpPeerStatusConnectRetryCount_Type())
eltexBgpPeerStatusConnectRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConnectRetryCount.setStatus(_A)
_EltexBgpPeerStatusClearCnts_Type=TruthValue
_EltexBgpPeerStatusClearCnts_Object=MibTableColumn
eltexBgpPeerStatusClearCnts=_EltexBgpPeerStatusClearCnts_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,28),_EltexBgpPeerStatusClearCnts_Type())
eltexBgpPeerStatusClearCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerStatusClearCnts.setStatus(_A)
_EltexBgpPeerStatusRtRefresh_Type=TruthValue
_EltexBgpPeerStatusRtRefresh_Object=MibTableColumn
eltexBgpPeerStatusRtRefresh=_EltexBgpPeerStatusRtRefresh_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,29),_EltexBgpPeerStatusRtRefresh_Type())
eltexBgpPeerStatusRtRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerStatusRtRefresh.setStatus(_A)
class _EltexBgpPeerStatusLastErrorRcvd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EltexBgpPeerStatusLastErrorRcvd_Type.__name__=_I
_EltexBgpPeerStatusLastErrorRcvd_Object=MibTableColumn
eltexBgpPeerStatusLastErrorRcvd=_EltexBgpPeerStatusLastErrorRcvd_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,30),_EltexBgpPeerStatusLastErrorRcvd_Type())
eltexBgpPeerStatusLastErrorRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorRcvd.setStatus(_A)
_EltexBgpPeerStatusLastErrorRcvdTime_Type=TimeStamp
_EltexBgpPeerStatusLastErrorRcvdTime_Object=MibTableColumn
eltexBgpPeerStatusLastErrorRcvdTime=_EltexBgpPeerStatusLastErrorRcvdTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,31),_EltexBgpPeerStatusLastErrorRcvdTime_Type())
eltexBgpPeerStatusLastErrorRcvdTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorRcvdTime.setStatus(_A)
class _EltexBgpPeerStatusLastErrorSent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EltexBgpPeerStatusLastErrorSent_Type.__name__=_I
_EltexBgpPeerStatusLastErrorSent_Object=MibTableColumn
eltexBgpPeerStatusLastErrorSent=_EltexBgpPeerStatusLastErrorSent_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,32),_EltexBgpPeerStatusLastErrorSent_Type())
eltexBgpPeerStatusLastErrorSent.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorSent.setStatus(_A)
_EltexBgpPeerStatusLastErrorSentTime_Type=TimeStamp
_EltexBgpPeerStatusLastErrorSentTime_Object=MibTableColumn
eltexBgpPeerStatusLastErrorSentTime=_EltexBgpPeerStatusLastErrorSentTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,33),_EltexBgpPeerStatusLastErrorSentTime_Type())
eltexBgpPeerStatusLastErrorSentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastErrorSentTime.setStatus(_A)
_EltexBgpPeerStatusLastState_Type=EltexBgpPeerStates
_EltexBgpPeerStatusLastState_Object=MibTableColumn
eltexBgpPeerStatusLastState=_EltexBgpPeerStatusLastState_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,34),_EltexBgpPeerStatusLastState_Type())
eltexBgpPeerStatusLastState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastState.setStatus(_A)
_EltexBgpPeerStatusLastEvent_Type=EltexBgpPeerEvents
_EltexBgpPeerStatusLastEvent_Object=MibTableColumn
eltexBgpPeerStatusLastEvent=_EltexBgpPeerStatusLastEvent_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,35),_EltexBgpPeerStatusLastEvent_Type())
eltexBgpPeerStatusLastEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusLastEvent.setStatus(_A)
_EltexBgpPeerStatusCapsSent_Type=EltexBgpCapabilities
_EltexBgpPeerStatusCapsSent_Object=MibTableColumn
eltexBgpPeerStatusCapsSent=_EltexBgpPeerStatusCapsSent_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,36),_EltexBgpPeerStatusCapsSent_Type())
eltexBgpPeerStatusCapsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusCapsSent.setStatus(_A)
_EltexBgpPeerStatusCapsRcvd_Type=EltexBgpCapabilities
_EltexBgpPeerStatusCapsRcvd_Object=MibTableColumn
eltexBgpPeerStatusCapsRcvd=_EltexBgpPeerStatusCapsRcvd_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,37),_EltexBgpPeerStatusCapsRcvd_Type())
eltexBgpPeerStatusCapsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusCapsRcvd.setStatus(_A)
_EltexBgpPeerStatusCapsNegotiated_Type=EltexBgpCapabilities
_EltexBgpPeerStatusCapsNegotiated_Object=MibTableColumn
eltexBgpPeerStatusCapsNegotiated=_EltexBgpPeerStatusCapsNegotiated_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,38),_EltexBgpPeerStatusCapsNegotiated_Type())
eltexBgpPeerStatusCapsNegotiated.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusCapsNegotiated.setStatus(_A)
_EltexBgpPeerStatusRcvdMsgElpsTime_Type=TimeInterval
_EltexBgpPeerStatusRcvdMsgElpsTime_Object=MibTableColumn
eltexBgpPeerStatusRcvdMsgElpsTime=_EltexBgpPeerStatusRcvdMsgElpsTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,39),_EltexBgpPeerStatusRcvdMsgElpsTime_Type())
eltexBgpPeerStatusRcvdMsgElpsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusRcvdMsgElpsTime.setStatus(_A)
_EltexBgpPeerStatusIdleHoldRemTime_Type=TimeInterval
_EltexBgpPeerStatusIdleHoldRemTime_Object=MibTableColumn
eltexBgpPeerStatusIdleHoldRemTime=_EltexBgpPeerStatusIdleHoldRemTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,40),_EltexBgpPeerStatusIdleHoldRemTime_Type())
eltexBgpPeerStatusIdleHoldRemTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusIdleHoldRemTime.setStatus(_A)
_EltexBgpPeerStatusRouteRefrSent_Type=Counter32
_EltexBgpPeerStatusRouteRefrSent_Object=MibTableColumn
eltexBgpPeerStatusRouteRefrSent=_EltexBgpPeerStatusRouteRefrSent_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,41),_EltexBgpPeerStatusRouteRefrSent_Type())
eltexBgpPeerStatusRouteRefrSent.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusRouteRefrSent.setStatus(_A)
_EltexBgpPeerStatusRouteRefrRcvd_Type=Counter32
_EltexBgpPeerStatusRouteRefrRcvd_Object=MibTableColumn
eltexBgpPeerStatusRouteRefrRcvd=_EltexBgpPeerStatusRouteRefrRcvd_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,42),_EltexBgpPeerStatusRouteRefrRcvd_Type())
eltexBgpPeerStatusRouteRefrRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusRouteRefrRcvd.setStatus(_A)
_EltexBgpPeerStatusSelLocalAddrType_Type=InetAddressType
_EltexBgpPeerStatusSelLocalAddrType_Object=MibTableColumn
eltexBgpPeerStatusSelLocalAddrType=_EltexBgpPeerStatusSelLocalAddrType_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,43),_EltexBgpPeerStatusSelLocalAddrType_Type())
eltexBgpPeerStatusSelLocalAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelLocalAddrType.setStatus(_A)
_EltexBgpPeerStatusSelLocalAddr_Type=InetAddress
_EltexBgpPeerStatusSelLocalAddr_Object=MibTableColumn
eltexBgpPeerStatusSelLocalAddr=_EltexBgpPeerStatusSelLocalAddr_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,44),_EltexBgpPeerStatusSelLocalAddr_Type())
eltexBgpPeerStatusSelLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelLocalAddr.setStatus(_A)
_EltexBgpPeerStatusSelLocalPort_Type=InetPortNumber
_EltexBgpPeerStatusSelLocalPort_Object=MibTableColumn
eltexBgpPeerStatusSelLocalPort=_EltexBgpPeerStatusSelLocalPort_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,45),_EltexBgpPeerStatusSelLocalPort_Type())
eltexBgpPeerStatusSelLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelLocalPort.setStatus(_A)
_EltexBgpPeerStatusSelRemotePort_Type=InetPortNumber
_EltexBgpPeerStatusSelRemotePort_Object=MibTableColumn
eltexBgpPeerStatusSelRemotePort=_EltexBgpPeerStatusSelRemotePort_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,46),_EltexBgpPeerStatusSelRemotePort_Type())
eltexBgpPeerStatusSelRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelRemotePort.setStatus(_A)
_EltexBgpPeerStatusSelLocalAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusSelLocalAs_Object=MibTableColumn
eltexBgpPeerStatusSelLocalAs=_EltexBgpPeerStatusSelLocalAs_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,47),_EltexBgpPeerStatusSelLocalAs_Type())
eltexBgpPeerStatusSelLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelLocalAs.setStatus(_A)
_EltexBgpPeerStatusSelRemoteAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpPeerStatusSelRemoteAs_Object=MibTableColumn
eltexBgpPeerStatusSelRemoteAs=_EltexBgpPeerStatusSelRemoteAs_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,48),_EltexBgpPeerStatusSelRemoteAs_Type())
eltexBgpPeerStatusSelRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusSelRemoteAs.setStatus(_A)
_EltexBgpPeerStatusInPrfxes_Type=Gauge32
_EltexBgpPeerStatusInPrfxes_Object=MibTableColumn
eltexBgpPeerStatusInPrfxes=_EltexBgpPeerStatusInPrfxes_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,49),_EltexBgpPeerStatusInPrfxes_Type())
eltexBgpPeerStatusInPrfxes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInPrfxes.setStatus(_A)
_EltexBgpPeerStatusOutPrfxes_Type=Gauge32
_EltexBgpPeerStatusOutPrfxes_Object=MibTableColumn
eltexBgpPeerStatusOutPrfxes=_EltexBgpPeerStatusOutPrfxes_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,50),_EltexBgpPeerStatusOutPrfxes_Type())
eltexBgpPeerStatusOutPrfxes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutPrfxes.setStatus(_A)
_EltexBgpPeerStatusOutPrfxesAdvertised_Type=Gauge32
_EltexBgpPeerStatusOutPrfxesAdvertised_Object=MibTableColumn
eltexBgpPeerStatusOutPrfxesAdvertised=_EltexBgpPeerStatusOutPrfxesAdvertised_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,51),_EltexBgpPeerStatusOutPrfxesAdvertised_Type())
eltexBgpPeerStatusOutPrfxesAdvertised.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutPrfxesAdvertised.setStatus(_A)
_EltexBgpPeerStatusConfigState_Type=EltexBgpPeerConfigStates
_EltexBgpPeerStatusConfigState_Object=MibTableColumn
eltexBgpPeerStatusConfigState=_EltexBgpPeerStatusConfigState_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,52),_EltexBgpPeerStatusConfigState_Type())
eltexBgpPeerStatusConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConfigState.setStatus(_A)
_EltexBgpPeerStatusConnectRetryInt_Type=Unsigned32
_EltexBgpPeerStatusConnectRetryInt_Object=MibTableColumn
eltexBgpPeerStatusConnectRetryInt=_EltexBgpPeerStatusConnectRetryInt_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,53),_EltexBgpPeerStatusConnectRetryInt_Type())
eltexBgpPeerStatusConnectRetryInt.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConnectRetryInt.setStatus(_A)
_EltexBgpPeerStatusConfigPassive_Type=TruthValue
_EltexBgpPeerStatusConfigPassive_Object=MibTableColumn
eltexBgpPeerStatusConfigPassive=_EltexBgpPeerStatusConfigPassive_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,54),_EltexBgpPeerStatusConfigPassive_Type())
eltexBgpPeerStatusConfigPassive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConfigPassive.setStatus(_A)
_EltexBgpPeerStatusConfigOpenDelay_Type=Unsigned32
_EltexBgpPeerStatusConfigOpenDelay_Object=MibTableColumn
eltexBgpPeerStatusConfigOpenDelay=_EltexBgpPeerStatusConfigOpenDelay_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,55),_EltexBgpPeerStatusConfigOpenDelay_Type())
eltexBgpPeerStatusConfigOpenDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConfigOpenDelay.setStatus(_A)
_EltexBgpPeerStatusConfigIdleHold_Type=Unsigned32
_EltexBgpPeerStatusConfigIdleHold_Object=MibTableColumn
eltexBgpPeerStatusConfigIdleHold=_EltexBgpPeerStatusConfigIdleHold_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,56),_EltexBgpPeerStatusConfigIdleHold_Type())
eltexBgpPeerStatusConfigIdleHold.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusConfigIdleHold.setStatus(_A)
_EltexBgpPeerStatusTtl_Type=Integer32
_EltexBgpPeerStatusTtl_Object=MibTableColumn
eltexBgpPeerStatusTtl=_EltexBgpPeerStatusTtl_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,57),_EltexBgpPeerStatusTtl_Type())
eltexBgpPeerStatusTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusTtl.setStatus(_A)
_EltexBgpPeerStatusHoldTimeConfigd_Type=Unsigned32
_EltexBgpPeerStatusHoldTimeConfigd_Object=MibTableColumn
eltexBgpPeerStatusHoldTimeConfigd=_EltexBgpPeerStatusHoldTimeConfigd_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,58),_EltexBgpPeerStatusHoldTimeConfigd_Type())
eltexBgpPeerStatusHoldTimeConfigd.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusHoldTimeConfigd.setStatus(_A)
_EltexBgpPeerStatusKeepAliveConfigd_Type=Unsigned32
_EltexBgpPeerStatusKeepAliveConfigd_Object=MibTableColumn
eltexBgpPeerStatusKeepAliveConfigd=_EltexBgpPeerStatusKeepAliveConfigd_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,59),_EltexBgpPeerStatusKeepAliveConfigd_Type())
eltexBgpPeerStatusKeepAliveConfigd.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusKeepAliveConfigd.setStatus(_A)
class _EltexBgpPeerStatusResendAllRoutes_Type(TruthValue):defaultValue=2
_EltexBgpPeerStatusResendAllRoutes_Type.__name__=_G
_EltexBgpPeerStatusResendAllRoutes_Object=MibTableColumn
eltexBgpPeerStatusResendAllRoutes=_EltexBgpPeerStatusResendAllRoutes_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,60),_EltexBgpPeerStatusResendAllRoutes_Type())
eltexBgpPeerStatusResendAllRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerStatusResendAllRoutes.setStatus(_A)
_EltexBgpPeerStatusOutUpdateElpsTime_Type=Gauge32
_EltexBgpPeerStatusOutUpdateElpsTime_Object=MibTableColumn
eltexBgpPeerStatusOutUpdateElpsTime=_EltexBgpPeerStatusOutUpdateElpsTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,61),_EltexBgpPeerStatusOutUpdateElpsTime_Type())
eltexBgpPeerStatusOutUpdateElpsTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutUpdateElpsTime.setStatus(_A)
_EltexBgpPeerStatusOutPrfxesDenied_Type=Counter32
_EltexBgpPeerStatusOutPrfxesDenied_Object=MibTableColumn
eltexBgpPeerStatusOutPrfxesDenied=_EltexBgpPeerStatusOutPrfxesDenied_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,62),_EltexBgpPeerStatusOutPrfxesDenied_Type())
eltexBgpPeerStatusOutPrfxesDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutPrfxesDenied.setStatus(_A)
_EltexBgpPeerStatusOutPrfxesImpWdr_Type=Counter32
_EltexBgpPeerStatusOutPrfxesImpWdr_Object=MibTableColumn
eltexBgpPeerStatusOutPrfxesImpWdr=_EltexBgpPeerStatusOutPrfxesImpWdr_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,63),_EltexBgpPeerStatusOutPrfxesImpWdr_Type())
eltexBgpPeerStatusOutPrfxesImpWdr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutPrfxesImpWdr.setStatus(_A)
_EltexBgpPeerStatusOutPrfxesExpWdr_Type=Counter32
_EltexBgpPeerStatusOutPrfxesExpWdr_Object=MibTableColumn
eltexBgpPeerStatusOutPrfxesExpWdr=_EltexBgpPeerStatusOutPrfxesExpWdr_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,64),_EltexBgpPeerStatusOutPrfxesExpWdr_Type())
eltexBgpPeerStatusOutPrfxesExpWdr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusOutPrfxesExpWdr.setStatus(_A)
_EltexBgpPeerStatusInPrfxesImpWdr_Type=Counter32
_EltexBgpPeerStatusInPrfxesImpWdr_Object=MibTableColumn
eltexBgpPeerStatusInPrfxesImpWdr=_EltexBgpPeerStatusInPrfxesImpWdr_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,65),_EltexBgpPeerStatusInPrfxesImpWdr_Type())
eltexBgpPeerStatusInPrfxesImpWdr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInPrfxesImpWdr.setStatus(_A)
_EltexBgpPeerStatusInPrfxesExpWdr_Type=Counter32
_EltexBgpPeerStatusInPrfxesExpWdr_Object=MibTableColumn
eltexBgpPeerStatusInPrfxesExpWdr=_EltexBgpPeerStatusInPrfxesExpWdr_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,66),_EltexBgpPeerStatusInPrfxesExpWdr_Type())
eltexBgpPeerStatusInPrfxesExpWdr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusInPrfxesExpWdr.setStatus(_A)
_EltexBgpPeerStatusReceivedHoldTime_Type=Integer32
_EltexBgpPeerStatusReceivedHoldTime_Object=MibTableColumn
eltexBgpPeerStatusReceivedHoldTime=_EltexBgpPeerStatusReceivedHoldTime_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,67),_EltexBgpPeerStatusReceivedHoldTime_Type())
eltexBgpPeerStatusReceivedHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusReceivedHoldTime.setStatus(_A)
_EltexBgpPeerStatusDropSession_Type=TruthValue
_EltexBgpPeerStatusDropSession_Object=MibTableColumn
eltexBgpPeerStatusDropSession=_EltexBgpPeerStatusDropSession_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,68),_EltexBgpPeerStatusDropSession_Type())
eltexBgpPeerStatusDropSession.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerStatusDropSession.setStatus(_A)
class _EltexBgpPeerStatusCeaseErrorSubcode_Type(EltexBgpCeaseErrorSubcode):defaultValue=0
_EltexBgpPeerStatusCeaseErrorSubcode_Type.__name__=_h
_EltexBgpPeerStatusCeaseErrorSubcode_Object=MibTableColumn
eltexBgpPeerStatusCeaseErrorSubcode=_EltexBgpPeerStatusCeaseErrorSubcode_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,69),_EltexBgpPeerStatusCeaseErrorSubcode_Type())
eltexBgpPeerStatusCeaseErrorSubcode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerStatusCeaseErrorSubcode.setStatus(_A)
_EltexBgpPeerStatusBfdStatus_Type=EltexBfdSessionStatus
_EltexBgpPeerStatusBfdStatus_Object=MibTableColumn
eltexBgpPeerStatusBfdStatus=_EltexBgpPeerStatusBfdStatus_Object((1,3,6,1,4,1,35265,45,1,2,1,3,1,70),_EltexBgpPeerStatusBfdStatus_Type())
eltexBgpPeerStatusBfdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerStatusBfdStatus.setStatus(_A)
_EltexBgpPeerAddrFamilyStatusTable_Object=MibTable
eltexBgpPeerAddrFamilyStatusTable=_EltexBgpPeerAddrFamilyStatusTable_Object((1,3,6,1,4,1,35265,45,1,2,1,4))
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusTable.setStatus(_A)
_EltexBgpPeerAddrFamilyStatusEntry_Object=MibTableRow
eltexBgpPeerAddrFamilyStatusEntry=_EltexBgpPeerAddrFamilyStatusEntry_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1))
eltexBgpPeerAddrFamilyStatusEntry.setIndexNames((0,_D,_H),(0,_D,_K),(0,_D,_L),(0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusEntry.setStatus(_A)
class _EltexBgpPeerAddrFamilyStatusRtRefresh_Type(TruthValue):defaultValue=2
_EltexBgpPeerAddrFamilyStatusRtRefresh_Type.__name__=_G
_EltexBgpPeerAddrFamilyStatusRtRefresh_Object=MibTableColumn
eltexBgpPeerAddrFamilyStatusRtRefresh=_EltexBgpPeerAddrFamilyStatusRtRefresh_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1,1),_EltexBgpPeerAddrFamilyStatusRtRefresh_Type())
eltexBgpPeerAddrFamilyStatusRtRefresh.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusRtRefresh.setStatus(_A)
_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Type=EltexBgpAddPathSrCap
_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Object=MibTableColumn
eltexBgpPeerAddrFamilyStatusAddPathCapNeg=_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1,2),_EltexBgpPeerAddrFamilyStatusAddPathCapNeg_Type())
eltexBgpPeerAddrFamilyStatusAddPathCapNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusAddPathCapNeg.setStatus(_A)
_EltexBgpPeerAddrFamilyStatusReflectorClient_Type=EltexBgpPeerReflectorClientType
_EltexBgpPeerAddrFamilyStatusReflectorClient_Object=MibTableColumn
eltexBgpPeerAddrFamilyStatusReflectorClient=_EltexBgpPeerAddrFamilyStatusReflectorClient_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1,3),_EltexBgpPeerAddrFamilyStatusReflectorClient_Type())
eltexBgpPeerAddrFamilyStatusReflectorClient.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusReflectorClient.setStatus(_A)
_EltexBgpPeerAddrFamilyStatusUpdateGroup_Type=Unsigned32
_EltexBgpPeerAddrFamilyStatusUpdateGroup_Object=MibTableColumn
eltexBgpPeerAddrFamilyStatusUpdateGroup=_EltexBgpPeerAddrFamilyStatusUpdateGroup_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1,4),_EltexBgpPeerAddrFamilyStatusUpdateGroup_Type())
eltexBgpPeerAddrFamilyStatusUpdateGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusUpdateGroup.setStatus(_A)
class _EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type(TruthValue):defaultValue=2
_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type.__name__=_G
_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Object=MibTableColumn
eltexBgpPeerAddrFamilyStatusResendAllRoutes=_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Object((1,3,6,1,4,1,35265,45,1,2,1,4,1,5),_EltexBgpPeerAddrFamilyStatusResendAllRoutes_Type())
eltexBgpPeerAddrFamilyStatusResendAllRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerAddrFamilyStatusResendAllRoutes.setStatus(_A)
_EltexBgpPeerGroup_ObjectIdentity=ObjectIdentity
eltexBgpPeerGroup=_EltexBgpPeerGroup_ObjectIdentity((1,3,6,1,4,1,35265,45,1,2,2))
_EltexBgpPeerGroupTable_Object=MibTable
eltexBgpPeerGroupTable=_EltexBgpPeerGroupTable_Object((1,3,6,1,4,1,35265,45,1,2,2,1))
if mibBuilder.loadTexts:eltexBgpPeerGroupTable.setStatus(_A)
_EltexBgpPeerGroupEntry_Object=MibTableRow
eltexBgpPeerGroupEntry=_EltexBgpPeerGroupEntry_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1))
eltexBgpPeerGroupEntry.setIndexNames((0,_D,_H),(0,_D,_i))
if mibBuilder.loadTexts:eltexBgpPeerGroupEntry.setStatus(_A)
_EltexBgpPeerGroupName_Type=DisplayString
_EltexBgpPeerGroupName_Object=MibTableColumn
eltexBgpPeerGroupName=_EltexBgpPeerGroupName_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,1),_EltexBgpPeerGroupName_Type())
eltexBgpPeerGroupName.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPeerGroupName.setStatus(_A)
_EltexBgpPeerGroupRowStatus_Type=RowStatus
_EltexBgpPeerGroupRowStatus_Object=MibTableColumn
eltexBgpPeerGroupRowStatus=_EltexBgpPeerGroupRowStatus_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,2),_EltexBgpPeerGroupRowStatus_Type())
eltexBgpPeerGroupRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:eltexBgpPeerGroupRowStatus.setStatus(_A)
_EltexBgpPeerGroupRemoteAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpPeerGroupRemoteAs_Object=MibTableColumn
eltexBgpPeerGroupRemoteAs=_EltexBgpPeerGroupRemoteAs_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,3),_EltexBgpPeerGroupRemoteAs_Type())
eltexBgpPeerGroupRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupRemoteAs.setStatus(_A)
class _EltexBgpPeerGroupSourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_EltexBgpPeerGroupSourceInterface_Type.__name__=_Q
_EltexBgpPeerGroupSourceInterface_Object=MibTableColumn
eltexBgpPeerGroupSourceInterface=_EltexBgpPeerGroupSourceInterface_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,4),_EltexBgpPeerGroupSourceInterface_Type())
eltexBgpPeerGroupSourceInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupSourceInterface.setStatus(_A)
class _EltexBgpPeerGroupNxtHopSlf_Type(TruthValue):defaultValue=2
_EltexBgpPeerGroupNxtHopSlf_Type.__name__=_G
_EltexBgpPeerGroupNxtHopSlf_Object=MibTableColumn
eltexBgpPeerGroupNxtHopSlf=_EltexBgpPeerGroupNxtHopSlf_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,5),_EltexBgpPeerGroupNxtHopSlf_Type())
eltexBgpPeerGroupNxtHopSlf.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupNxtHopSlf.setStatus(_A)
class _EltexBgpPeerGroupConfigMaxPrfx_Type(Unsigned32):defaultValue=0
_EltexBgpPeerGroupConfigMaxPrfx_Type.__name__=_E
_EltexBgpPeerGroupConfigMaxPrfx_Object=MibTableColumn
eltexBgpPeerGroupConfigMaxPrfx=_EltexBgpPeerGroupConfigMaxPrfx_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,6),_EltexBgpPeerGroupConfigMaxPrfx_Type())
eltexBgpPeerGroupConfigMaxPrfx.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConfigMaxPrfx.setStatus(_A)
class _EltexBgpPeerGroupConfigDropWarn_Type(EltexBgpConfigDropOrWarn):defaultValue=2
_EltexBgpPeerGroupConfigDropWarn_Type.__name__=_O
_EltexBgpPeerGroupConfigDropWarn_Object=MibTableColumn
eltexBgpPeerGroupConfigDropWarn=_EltexBgpPeerGroupConfigDropWarn_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,7),_EltexBgpPeerGroupConfigDropWarn_Type())
eltexBgpPeerGroupConfigDropWarn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConfigDropWarn.setStatus(_A)
class _EltexBgpPeerGroupMaxPrfxHold_Type(Unsigned32):defaultValue=90
_EltexBgpPeerGroupMaxPrfxHold_Type.__name__=_E
_EltexBgpPeerGroupMaxPrfxHold_Object=MibTableColumn
eltexBgpPeerGroupMaxPrfxHold=_EltexBgpPeerGroupMaxPrfxHold_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,8),_EltexBgpPeerGroupMaxPrfxHold_Type())
eltexBgpPeerGroupMaxPrfxHold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupMaxPrfxHold.setStatus(_A)
class _EltexBgpPeerGroupConfigThreshold_Type(Unsigned32):defaultValue=75
_EltexBgpPeerGroupConfigThreshold_Type.__name__=_E
_EltexBgpPeerGroupConfigThreshold_Object=MibTableColumn
eltexBgpPeerGroupConfigThreshold=_EltexBgpPeerGroupConfigThreshold_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,9),_EltexBgpPeerGroupConfigThreshold_Type())
eltexBgpPeerGroupConfigThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConfigThreshold.setStatus(_A)
class _EltexBgpPeerGroupConnectRetryInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexBgpPeerGroupConnectRetryInterval_Type.__name__=_E
_EltexBgpPeerGroupConnectRetryInterval_Object=MibTableColumn
eltexBgpPeerGroupConnectRetryInterval=_EltexBgpPeerGroupConnectRetryInterval_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,10),_EltexBgpPeerGroupConnectRetryInterval_Type())
eltexBgpPeerGroupConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConnectRetryInterval.setStatus(_A)
class _EltexBgpPeerGroupHoldTimeConfigd_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerGroupHoldTimeConfigd_Type.__name__=_E
_EltexBgpPeerGroupHoldTimeConfigd_Object=MibTableColumn
eltexBgpPeerGroupHoldTimeConfigd=_EltexBgpPeerGroupHoldTimeConfigd_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,11),_EltexBgpPeerGroupHoldTimeConfigd_Type())
eltexBgpPeerGroupHoldTimeConfigd.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupHoldTimeConfigd.setStatus(_A)
class _EltexBgpPeerGroupKeepAliveConfigd_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_EltexBgpPeerGroupKeepAliveConfigd_Type.__name__=_E
_EltexBgpPeerGroupKeepAliveConfigd_Object=MibTableColumn
eltexBgpPeerGroupKeepAliveConfigd=_EltexBgpPeerGroupKeepAliveConfigd_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,12),_EltexBgpPeerGroupKeepAliveConfigd_Type())
eltexBgpPeerGroupKeepAliveConfigd.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupKeepAliveConfigd.setStatus(_A)
class _EltexBgpPeerGroupMinRouteAdvertiseInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerGroupMinRouteAdvertiseInterval_Type.__name__=_E
_EltexBgpPeerGroupMinRouteAdvertiseInterval_Object=MibTableColumn
eltexBgpPeerGroupMinRouteAdvertiseInterval=_EltexBgpPeerGroupMinRouteAdvertiseInterval_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,13),_EltexBgpPeerGroupMinRouteAdvertiseInterval_Type())
eltexBgpPeerGroupMinRouteAdvertiseInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupMinRouteAdvertiseInterval.setStatus(_A)
class _EltexBgpPeerGroupMinASOriginationInterval_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerGroupMinASOriginationInterval_Type.__name__=_E
_EltexBgpPeerGroupMinASOriginationInterval_Object=MibTableColumn
eltexBgpPeerGroupMinASOriginationInterval=_EltexBgpPeerGroupMinASOriginationInterval_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,14),_EltexBgpPeerGroupMinASOriginationInterval_Type())
eltexBgpPeerGroupMinASOriginationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupMinASOriginationInterval.setStatus(_A)
class _EltexBgpPeerGroupMinRouteWithdrawInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltexBgpPeerGroupMinRouteWithdrawInterval_Type.__name__=_E
_EltexBgpPeerGroupMinRouteWithdrawInterval_Object=MibTableColumn
eltexBgpPeerGroupMinRouteWithdrawInterval=_EltexBgpPeerGroupMinRouteWithdrawInterval_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,15),_EltexBgpPeerGroupMinRouteWithdrawInterval_Type())
eltexBgpPeerGroupMinRouteWithdrawInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupMinRouteWithdrawInterval.setStatus(_A)
class _EltexBgpPeerGroupConfigOpenDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_EltexBgpPeerGroupConfigOpenDelay_Type.__name__=_E
_EltexBgpPeerGroupConfigOpenDelay_Object=MibTableColumn
eltexBgpPeerGroupConfigOpenDelay=_EltexBgpPeerGroupConfigOpenDelay_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,16),_EltexBgpPeerGroupConfigOpenDelay_Type())
eltexBgpPeerGroupConfigOpenDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConfigOpenDelay.setStatus(_A)
class _EltexBgpPeerGroupConfigIdleHold_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_EltexBgpPeerGroupConfigIdleHold_Type.__name__=_E
_EltexBgpPeerGroupConfigIdleHold_Object=MibTableColumn
eltexBgpPeerGroupConfigIdleHold=_EltexBgpPeerGroupConfigIdleHold_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,17),_EltexBgpPeerGroupConfigIdleHold_Type())
eltexBgpPeerGroupConfigIdleHold.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupConfigIdleHold.setStatus(_A)
_EltexBgpPeerGroupDistListPlIn_Type=DisplayString
_EltexBgpPeerGroupDistListPlIn_Object=MibTableColumn
eltexBgpPeerGroupDistListPlIn=_EltexBgpPeerGroupDistListPlIn_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,18),_EltexBgpPeerGroupDistListPlIn_Type())
eltexBgpPeerGroupDistListPlIn.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupDistListPlIn.setStatus(_A)
_EltexBgpPeerGroupDistListPlOut_Type=DisplayString
_EltexBgpPeerGroupDistListPlOut_Object=MibTableColumn
eltexBgpPeerGroupDistListPlOut=_EltexBgpPeerGroupDistListPlOut_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,19),_EltexBgpPeerGroupDistListPlOut_Type())
eltexBgpPeerGroupDistListPlOut.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupDistListPlOut.setStatus(_A)
class _EltexBgpPeerGroupReflectorClient_Type(EltexBgpPeerReflectorClientType):defaultValue=0
_EltexBgpPeerGroupReflectorClient_Type.__name__=_P
_EltexBgpPeerGroupReflectorClient_Object=MibTableColumn
eltexBgpPeerGroupReflectorClient=_EltexBgpPeerGroupReflectorClient_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,20),_EltexBgpPeerGroupReflectorClient_Type())
eltexBgpPeerGroupReflectorClient.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupReflectorClient.setStatus(_A)
class _EltexBgpPeerGroupSoftResetWithStoredInfo_Type(TruthValue):defaultValue=2
_EltexBgpPeerGroupSoftResetWithStoredInfo_Type.__name__=_G
_EltexBgpPeerGroupSoftResetWithStoredInfo_Object=MibTableColumn
eltexBgpPeerGroupSoftResetWithStoredInfo=_EltexBgpPeerGroupSoftResetWithStoredInfo_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,21),_EltexBgpPeerGroupSoftResetWithStoredInfo_Type())
eltexBgpPeerGroupSoftResetWithStoredInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupSoftResetWithStoredInfo.setStatus(_A)
class _EltexBgpPeerGroupBfdDesired_Type(TruthValue):defaultValue=2
_EltexBgpPeerGroupBfdDesired_Type.__name__=_G
_EltexBgpPeerGroupBfdDesired_Object=MibTableColumn
eltexBgpPeerGroupBfdDesired=_EltexBgpPeerGroupBfdDesired_Object((1,3,6,1,4,1,35265,45,1,2,2,1,1,22),_EltexBgpPeerGroupBfdDesired_Type())
eltexBgpPeerGroupBfdDesired.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpPeerGroupBfdDesired.setStatus(_A)
_EltexBgpRib_ObjectIdentity=ObjectIdentity
eltexBgpRib=_EltexBgpRib_ObjectIdentity((1,3,6,1,4,1,35265,45,1,3))
_EltexBgpLocRibTable_Object=MibTable
eltexBgpLocRibTable=_EltexBgpLocRibTable_Object((1,3,6,1,4,1,35265,45,1,3,1))
if mibBuilder.loadTexts:eltexBgpLocRibTable.setStatus(_A)
_EltexBgpLocRibEntry_Object=MibTableRow
eltexBgpLocRibEntry=_EltexBgpLocRibEntry_Object((1,3,6,1,4,1,35265,45,1,3,1,1))
eltexBgpLocRibEntry.setIndexNames((0,_D,_H),(0,_D,_W),(0,_D,_X),(0,_D,_j),(0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b),(0,_D,_c))
if mibBuilder.loadTexts:eltexBgpLocRibEntry.setStatus(_A)
_EltexBgpLocRibAfi_Type=EltexBgpAfi
_EltexBgpLocRibAfi_Object=MibTableColumn
eltexBgpLocRibAfi=_EltexBgpLocRibAfi_Object((1,3,6,1,4,1,35265,45,1,3,1,1,1),_EltexBgpLocRibAfi_Type())
eltexBgpLocRibAfi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibAfi.setStatus(_A)
_EltexBgpLocRibSafi_Type=EltexBgpSafi
_EltexBgpLocRibSafi_Object=MibTableColumn
eltexBgpLocRibSafi=_EltexBgpLocRibSafi_Object((1,3,6,1,4,1,35265,45,1,3,1,1,2),_EltexBgpLocRibSafi_Type())
eltexBgpLocRibSafi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibSafi.setStatus(_A)
_EltexBgpLocRibPrfxType_Type=InetAddressType
_EltexBgpLocRibPrfxType_Object=MibTableColumn
eltexBgpLocRibPrfxType=_EltexBgpLocRibPrfxType_Object((1,3,6,1,4,1,35265,45,1,3,1,1,3),_EltexBgpLocRibPrfxType_Type())
eltexBgpLocRibPrfxType.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPrfxType.setStatus(_A)
_EltexBgpLocRibPrfx_Type=InetAddress
_EltexBgpLocRibPrfx_Object=MibTableColumn
eltexBgpLocRibPrfx=_EltexBgpLocRibPrfx_Object((1,3,6,1,4,1,35265,45,1,3,1,1,4),_EltexBgpLocRibPrfx_Type())
eltexBgpLocRibPrfx.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPrfx.setStatus(_A)
_EltexBgpLocRibPrfxLen_Type=InetAddressPrefixLength
_EltexBgpLocRibPrfxLen_Object=MibTableColumn
eltexBgpLocRibPrfxLen=_EltexBgpLocRibPrfxLen_Object((1,3,6,1,4,1,35265,45,1,3,1,1,5),_EltexBgpLocRibPrfxLen_Type())
eltexBgpLocRibPrfxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPrfxLen.setStatus(_A)
_EltexBgpLocRibPeerOrRib_Type=EltexBgpPeerOrRib
_EltexBgpLocRibPeerOrRib_Object=MibTableColumn
eltexBgpLocRibPeerOrRib=_EltexBgpLocRibPeerOrRib_Object((1,3,6,1,4,1,35265,45,1,3,1,1,6),_EltexBgpLocRibPeerOrRib_Type())
eltexBgpLocRibPeerOrRib.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPeerOrRib.setStatus(_A)
_EltexBgpLocRibPeerRibIndex_Type=Unsigned32
_EltexBgpLocRibPeerRibIndex_Object=MibTableColumn
eltexBgpLocRibPeerRibIndex=_EltexBgpLocRibPeerRibIndex_Object((1,3,6,1,4,1,35265,45,1,3,1,1,7),_EltexBgpLocRibPeerRibIndex_Type())
eltexBgpLocRibPeerRibIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPeerRibIndex.setStatus(_A)
_EltexBgpLocRibPathId_Type=Unsigned32
_EltexBgpLocRibPathId_Object=MibTableColumn
eltexBgpLocRibPathId=_EltexBgpLocRibPathId_Object((1,3,6,1,4,1,35265,45,1,3,1,1,8),_EltexBgpLocRibPathId_Type())
eltexBgpLocRibPathId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpLocRibPathId.setStatus(_A)
_EltexBgpLocRibBest_Type=TruthValue
_EltexBgpLocRibBest_Object=MibTableColumn
eltexBgpLocRibBest=_EltexBgpLocRibBest_Object((1,3,6,1,4,1,35265,45,1,3,1,1,9),_EltexBgpLocRibBest_Type())
eltexBgpLocRibBest.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibBest.setStatus(_A)
_EltexBgpLocRibAsSize_Type=EltexBgpAsSize
_EltexBgpLocRibAsSize_Object=MibTableColumn
eltexBgpLocRibAsSize=_EltexBgpLocRibAsSize_Object((1,3,6,1,4,1,35265,45,1,3,1,1,10),_EltexBgpLocRibAsSize_Type())
eltexBgpLocRibAsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibAsSize.setStatus(_A)
class _EltexBgpLocRibASPathStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexBgpLocRibASPathStr_Type.__name__=_I
_EltexBgpLocRibASPathStr_Object=MibTableColumn
eltexBgpLocRibASPathStr=_EltexBgpLocRibASPathStr_Object((1,3,6,1,4,1,35265,45,1,3,1,1,11),_EltexBgpLocRibASPathStr_Type())
eltexBgpLocRibASPathStr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibASPathStr.setStatus(_A)
_EltexBgpLocRibPathAttrOrigin_Type=EltexBgpOriginCode
_EltexBgpLocRibPathAttrOrigin_Object=MibTableColumn
eltexBgpLocRibPathAttrOrigin=_EltexBgpLocRibPathAttrOrigin_Object((1,3,6,1,4,1,35265,45,1,3,1,1,12),_EltexBgpLocRibPathAttrOrigin_Type())
eltexBgpLocRibPathAttrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrOrigin.setStatus(_A)
_EltexBgpLocRibPathAttrNextHopType_Type=InetAddressType
_EltexBgpLocRibPathAttrNextHopType_Object=MibTableColumn
eltexBgpLocRibPathAttrNextHopType=_EltexBgpLocRibPathAttrNextHopType_Object((1,3,6,1,4,1,35265,45,1,3,1,1,13),_EltexBgpLocRibPathAttrNextHopType_Type())
eltexBgpLocRibPathAttrNextHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrNextHopType.setStatus(_A)
_EltexBgpLocRibPathAttrNextHop_Type=InetAddress
_EltexBgpLocRibPathAttrNextHop_Object=MibTableColumn
eltexBgpLocRibPathAttrNextHop=_EltexBgpLocRibPathAttrNextHop_Object((1,3,6,1,4,1,35265,45,1,3,1,1,14),_EltexBgpLocRibPathAttrNextHop_Type())
eltexBgpLocRibPathAttrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrNextHop.setStatus(_A)
_EltexBgpLocRibPathAttrMultExtDisc_Type=Unsigned32
_EltexBgpLocRibPathAttrMultExtDisc_Object=MibTableColumn
eltexBgpLocRibPathAttrMultExtDisc=_EltexBgpLocRibPathAttrMultExtDisc_Object((1,3,6,1,4,1,35265,45,1,3,1,1,15),_EltexBgpLocRibPathAttrMultExtDisc_Type())
eltexBgpLocRibPathAttrMultExtDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrMultExtDisc.setStatus(_A)
_EltexBgpLocRibPathAttrLocalPref_Type=Unsigned32
_EltexBgpLocRibPathAttrLocalPref_Object=MibTableColumn
eltexBgpLocRibPathAttrLocalPref=_EltexBgpLocRibPathAttrLocalPref_Object((1,3,6,1,4,1,35265,45,1,3,1,1,16),_EltexBgpLocRibPathAttrLocalPref_Type())
eltexBgpLocRibPathAttrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrLocalPref.setStatus(_A)
_EltexBgpLocRibPathAttrAtomicAgg_Type=TruthValue
_EltexBgpLocRibPathAttrAtomicAgg_Object=MibTableColumn
eltexBgpLocRibPathAttrAtomicAgg=_EltexBgpLocRibPathAttrAtomicAgg_Object((1,3,6,1,4,1,35265,45,1,3,1,1,17),_EltexBgpLocRibPathAttrAtomicAgg_Type())
eltexBgpLocRibPathAttrAtomicAgg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrAtomicAgg.setStatus(_A)
_EltexBgpLocRibPathAttrAggAS_Type=EltexBgpAutonomousSystemNumber
_EltexBgpLocRibPathAttrAggAS_Object=MibTableColumn
eltexBgpLocRibPathAttrAggAS=_EltexBgpLocRibPathAttrAggAS_Object((1,3,6,1,4,1,35265,45,1,3,1,1,18),_EltexBgpLocRibPathAttrAggAS_Type())
eltexBgpLocRibPathAttrAggAS.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrAggAS.setStatus(_A)
_EltexBgpLocRibPathAttrAggAddr_Type=EltexBgpIdentifier
_EltexBgpLocRibPathAttrAggAddr_Object=MibTableColumn
eltexBgpLocRibPathAttrAggAddr=_EltexBgpLocRibPathAttrAggAddr_Object((1,3,6,1,4,1,35265,45,1,3,1,1,19),_EltexBgpLocRibPathAttrAggAddr_Type())
eltexBgpLocRibPathAttrAggAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrAggAddr.setStatus(_A)
_EltexBgpLocRibPathAttrCalcLclPref_Type=Unsigned32
_EltexBgpLocRibPathAttrCalcLclPref_Object=MibTableColumn
eltexBgpLocRibPathAttrCalcLclPref=_EltexBgpLocRibPathAttrCalcLclPref_Object((1,3,6,1,4,1,35265,45,1,3,1,1,20),_EltexBgpLocRibPathAttrCalcLclPref_Type())
eltexBgpLocRibPathAttrCalcLclPref.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrCalcLclPref.setStatus(_A)
_EltexBgpLocRibPathAttrOrigId_Type=EltexBgpIdentifier
_EltexBgpLocRibPathAttrOrigId_Object=MibTableColumn
eltexBgpLocRibPathAttrOrigId=_EltexBgpLocRibPathAttrOrigId_Object((1,3,6,1,4,1,35265,45,1,3,1,1,21),_EltexBgpLocRibPathAttrOrigId_Type())
eltexBgpLocRibPathAttrOrigId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrOrigId.setStatus(_A)
_EltexBgpLocRibPathAttrWeight_Type=Unsigned32
_EltexBgpLocRibPathAttrWeight_Object=MibTableColumn
eltexBgpLocRibPathAttrWeight=_EltexBgpLocRibPathAttrWeight_Object((1,3,6,1,4,1,35265,45,1,3,1,1,22),_EltexBgpLocRibPathAttrWeight_Type())
eltexBgpLocRibPathAttrWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrWeight.setStatus(_A)
_EltexBgpLocRibEcmp_Type=TruthValue
_EltexBgpLocRibEcmp_Object=MibTableColumn
eltexBgpLocRibEcmp=_EltexBgpLocRibEcmp_Object((1,3,6,1,4,1,35265,45,1,3,1,1,23),_EltexBgpLocRibEcmp_Type())
eltexBgpLocRibEcmp.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibEcmp.setStatus(_A)
_EltexBgpLocRibPathAttrAsPathLimAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpLocRibPathAttrAsPathLimAs_Object=MibTableColumn
eltexBgpLocRibPathAttrAsPathLimAs=_EltexBgpLocRibPathAttrAsPathLimAs_Object((1,3,6,1,4,1,35265,45,1,3,1,1,24),_EltexBgpLocRibPathAttrAsPathLimAs_Type())
eltexBgpLocRibPathAttrAsPathLimAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrAsPathLimAs.setStatus(_A)
class _EltexBgpLocRibPthAttAsPthLimUpper_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexBgpLocRibPthAttAsPthLimUpper_Type.__name__=_E
_EltexBgpLocRibPthAttAsPthLimUpper_Object=MibTableColumn
eltexBgpLocRibPthAttAsPthLimUpper=_EltexBgpLocRibPthAttAsPthLimUpper_Object((1,3,6,1,4,1,35265,45,1,3,1,1,25),_EltexBgpLocRibPthAttAsPthLimUpper_Type())
eltexBgpLocRibPthAttAsPthLimUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPthAttAsPthLimUpper.setStatus(_A)
_EltexBgpLocRibIsActive_Type=EltexBgpNlriIsActiveFlag
_EltexBgpLocRibIsActive_Object=MibTableColumn
eltexBgpLocRibIsActive=_EltexBgpLocRibIsActive_Object((1,3,6,1,4,1,35265,45,1,3,1,1,26),_EltexBgpLocRibIsActive_Type())
eltexBgpLocRibIsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibIsActive.setStatus(_A)
_EltexBgpLocRibPathAttrMEDPrsnt_Type=TruthValue
_EltexBgpLocRibPathAttrMEDPrsnt_Object=MibTableColumn
eltexBgpLocRibPathAttrMEDPrsnt=_EltexBgpLocRibPathAttrMEDPrsnt_Object((1,3,6,1,4,1,35265,45,1,3,1,1,27),_EltexBgpLocRibPathAttrMEDPrsnt_Type())
eltexBgpLocRibPathAttrMEDPrsnt.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPathAttrMEDPrsnt.setStatus(_A)
_EltexBgpLocRibReasonNotBest_Type=EltexBgpReasonNotBest
_EltexBgpLocRibReasonNotBest_Object=MibTableColumn
eltexBgpLocRibReasonNotBest=_EltexBgpLocRibReasonNotBest_Object((1,3,6,1,4,1,35265,45,1,3,1,1,28),_EltexBgpLocRibReasonNotBest_Type())
eltexBgpLocRibReasonNotBest.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibReasonNotBest.setStatus(_A)
_EltexBgpLocRibPeerType_Type=EltexBgpNlriPeerTypes
_EltexBgpLocRibPeerType_Object=MibTableColumn
eltexBgpLocRibPeerType=_EltexBgpLocRibPeerType_Object((1,3,6,1,4,1,35265,45,1,3,1,1,29),_EltexBgpLocRibPeerType_Type())
eltexBgpLocRibPeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpLocRibPeerType.setStatus(_A)
_EltexBgpAdjRibInTable_Object=MibTable
eltexBgpAdjRibInTable=_EltexBgpAdjRibInTable_Object((1,3,6,1,4,1,35265,45,1,3,2))
if mibBuilder.loadTexts:eltexBgpAdjRibInTable.setStatus(_A)
_EltexBgpAdjRibInEntry_Object=MibTableRow
eltexBgpAdjRibInEntry=_EltexBgpAdjRibInEntry_Object((1,3,6,1,4,1,35265,45,1,3,2,1))
eltexBgpAdjRibInEntry.setIndexNames((0,_D,_H),(0,_D,_k),(0,_D,_l),(0,_D,_m),(0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:eltexBgpAdjRibInEntry.setStatus(_A)
_EltexBgpAdjRibInPeerIndex_Type=Unsigned32
_EltexBgpAdjRibInPeerIndex_Object=MibTableColumn
eltexBgpAdjRibInPeerIndex=_EltexBgpAdjRibInPeerIndex_Object((1,3,6,1,4,1,35265,45,1,3,2,1,1),_EltexBgpAdjRibInPeerIndex_Type())
eltexBgpAdjRibInPeerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInPeerIndex.setStatus(_A)
_EltexBgpAdjRibInAfi_Type=EltexBgpAfi
_EltexBgpAdjRibInAfi_Object=MibTableColumn
eltexBgpAdjRibInAfi=_EltexBgpAdjRibInAfi_Object((1,3,6,1,4,1,35265,45,1,3,2,1,2),_EltexBgpAdjRibInAfi_Type())
eltexBgpAdjRibInAfi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInAfi.setStatus(_A)
_EltexBgpAdjRibInSafi_Type=EltexBgpSafi
_EltexBgpAdjRibInSafi_Object=MibTableColumn
eltexBgpAdjRibInSafi=_EltexBgpAdjRibInSafi_Object((1,3,6,1,4,1,35265,45,1,3,2,1,3),_EltexBgpAdjRibInSafi_Type())
eltexBgpAdjRibInSafi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInSafi.setStatus(_A)
_EltexBgpAdjRibInPrfxType_Type=InetAddressType
_EltexBgpAdjRibInPrfxType_Object=MibTableColumn
eltexBgpAdjRibInPrfxType=_EltexBgpAdjRibInPrfxType_Object((1,3,6,1,4,1,35265,45,1,3,2,1,4),_EltexBgpAdjRibInPrfxType_Type())
eltexBgpAdjRibInPrfxType.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInPrfxType.setStatus(_A)
_EltexBgpAdjRibInPrfx_Type=InetAddress
_EltexBgpAdjRibInPrfx_Object=MibTableColumn
eltexBgpAdjRibInPrfx=_EltexBgpAdjRibInPrfx_Object((1,3,6,1,4,1,35265,45,1,3,2,1,5),_EltexBgpAdjRibInPrfx_Type())
eltexBgpAdjRibInPrfx.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInPrfx.setStatus(_A)
_EltexBgpAdjRibInPrfxLen_Type=InetAddressPrefixLength
_EltexBgpAdjRibInPrfxLen_Object=MibTableColumn
eltexBgpAdjRibInPrfxLen=_EltexBgpAdjRibInPrfxLen_Object((1,3,6,1,4,1,35265,45,1,3,2,1,6),_EltexBgpAdjRibInPrfxLen_Type())
eltexBgpAdjRibInPrfxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInPrfxLen.setStatus(_A)
_EltexBgpAdjRibInPathId_Type=Unsigned32
_EltexBgpAdjRibInPathId_Object=MibTableColumn
eltexBgpAdjRibInPathId=_EltexBgpAdjRibInPathId_Object((1,3,6,1,4,1,35265,45,1,3,2,1,7),_EltexBgpAdjRibInPathId_Type())
eltexBgpAdjRibInPathId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathId.setStatus(_A)
_EltexBgpAdjRibInAsSize_Type=EltexBgpAsSize
_EltexBgpAdjRibInAsSize_Object=MibTableColumn
eltexBgpAdjRibInAsSize=_EltexBgpAdjRibInAsSize_Object((1,3,6,1,4,1,35265,45,1,3,2,1,8),_EltexBgpAdjRibInAsSize_Type())
eltexBgpAdjRibInAsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInAsSize.setStatus(_A)
class _EltexBgpAdjRibInASPathStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexBgpAdjRibInASPathStr_Type.__name__=_I
_EltexBgpAdjRibInASPathStr_Object=MibTableColumn
eltexBgpAdjRibInASPathStr=_EltexBgpAdjRibInASPathStr_Object((1,3,6,1,4,1,35265,45,1,3,2,1,9),_EltexBgpAdjRibInASPathStr_Type())
eltexBgpAdjRibInASPathStr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInASPathStr.setStatus(_A)
_EltexBgpAdjRibInPathAttrOrigin_Type=EltexBgpOriginCode
_EltexBgpAdjRibInPathAttrOrigin_Object=MibTableColumn
eltexBgpAdjRibInPathAttrOrigin=_EltexBgpAdjRibInPathAttrOrigin_Object((1,3,6,1,4,1,35265,45,1,3,2,1,10),_EltexBgpAdjRibInPathAttrOrigin_Type())
eltexBgpAdjRibInPathAttrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrOrigin.setStatus(_A)
_EltexBgpAdjRibInPathAttrNextHopType_Type=InetAddressType
_EltexBgpAdjRibInPathAttrNextHopType_Object=MibTableColumn
eltexBgpAdjRibInPathAttrNextHopType=_EltexBgpAdjRibInPathAttrNextHopType_Object((1,3,6,1,4,1,35265,45,1,3,2,1,11),_EltexBgpAdjRibInPathAttrNextHopType_Type())
eltexBgpAdjRibInPathAttrNextHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrNextHopType.setStatus(_A)
_EltexBgpAdjRibInPathAttrNextHop_Type=InetAddress
_EltexBgpAdjRibInPathAttrNextHop_Object=MibTableColumn
eltexBgpAdjRibInPathAttrNextHop=_EltexBgpAdjRibInPathAttrNextHop_Object((1,3,6,1,4,1,35265,45,1,3,2,1,12),_EltexBgpAdjRibInPathAttrNextHop_Type())
eltexBgpAdjRibInPathAttrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrNextHop.setStatus(_A)
_EltexBgpAdjRibInPathAttrMultiExitDisc_Type=Unsigned32
_EltexBgpAdjRibInPathAttrMultiExitDisc_Object=MibTableColumn
eltexBgpAdjRibInPathAttrMultiExitDisc=_EltexBgpAdjRibInPathAttrMultiExitDisc_Object((1,3,6,1,4,1,35265,45,1,3,2,1,13),_EltexBgpAdjRibInPathAttrMultiExitDisc_Type())
eltexBgpAdjRibInPathAttrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrMultiExitDisc.setStatus(_A)
_EltexBgpAdjRibInPathAttrLocalPref_Type=Unsigned32
_EltexBgpAdjRibInPathAttrLocalPref_Object=MibTableColumn
eltexBgpAdjRibInPathAttrLocalPref=_EltexBgpAdjRibInPathAttrLocalPref_Object((1,3,6,1,4,1,35265,45,1,3,2,1,14),_EltexBgpAdjRibInPathAttrLocalPref_Type())
eltexBgpAdjRibInPathAttrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrLocalPref.setStatus(_A)
_EltexBgpAdjRibInPathAttrAtomicAggregate_Type=TruthValue
_EltexBgpAdjRibInPathAttrAtomicAggregate_Object=MibTableColumn
eltexBgpAdjRibInPathAttrAtomicAggregate=_EltexBgpAdjRibInPathAttrAtomicAggregate_Object((1,3,6,1,4,1,35265,45,1,3,2,1,15),_EltexBgpAdjRibInPathAttrAtomicAggregate_Type())
eltexBgpAdjRibInPathAttrAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrAtomicAggregate.setStatus(_A)
_EltexBgpAdjRibInPathAttrAggregatorAS_Type=EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibInPathAttrAggregatorAS_Object=MibTableColumn
eltexBgpAdjRibInPathAttrAggregatorAS=_EltexBgpAdjRibInPathAttrAggregatorAS_Object((1,3,6,1,4,1,35265,45,1,3,2,1,16),_EltexBgpAdjRibInPathAttrAggregatorAS_Type())
eltexBgpAdjRibInPathAttrAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrAggregatorAS.setStatus(_A)
_EltexBgpAdjRibInPathAttrAggregatorAddr_Type=EltexBgpIdentifier
_EltexBgpAdjRibInPathAttrAggregatorAddr_Object=MibTableColumn
eltexBgpAdjRibInPathAttrAggregatorAddr=_EltexBgpAdjRibInPathAttrAggregatorAddr_Object((1,3,6,1,4,1,35265,45,1,3,2,1,17),_EltexBgpAdjRibInPathAttrAggregatorAddr_Type())
eltexBgpAdjRibInPathAttrAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrAggregatorAddr.setStatus(_A)
_EltexBgpAdjRibInPathAttrOrigId_Type=EltexBgpIdentifier
_EltexBgpAdjRibInPathAttrOrigId_Object=MibTableColumn
eltexBgpAdjRibInPathAttrOrigId=_EltexBgpAdjRibInPathAttrOrigId_Object((1,3,6,1,4,1,35265,45,1,3,2,1,18),_EltexBgpAdjRibInPathAttrOrigId_Type())
eltexBgpAdjRibInPathAttrOrigId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrOrigId.setStatus(_A)
_EltexBgpAdjRibInPathAttrAsPathLimAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibInPathAttrAsPathLimAs_Object=MibTableColumn
eltexBgpAdjRibInPathAttrAsPathLimAs=_EltexBgpAdjRibInPathAttrAsPathLimAs_Object((1,3,6,1,4,1,35265,45,1,3,2,1,19),_EltexBgpAdjRibInPathAttrAsPathLimAs_Type())
eltexBgpAdjRibInPathAttrAsPathLimAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrAsPathLimAs.setStatus(_A)
class _EltexBgpAdjRibInPathAttrAsPathLimUpper_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexBgpAdjRibInPathAttrAsPathLimUpper_Type.__name__=_E
_EltexBgpAdjRibInPathAttrAsPathLimUpper_Object=MibTableColumn
eltexBgpAdjRibInPathAttrAsPathLimUpper=_EltexBgpAdjRibInPathAttrAsPathLimUpper_Object((1,3,6,1,4,1,35265,45,1,3,2,1,20),_EltexBgpAdjRibInPathAttrAsPathLimUpper_Type())
eltexBgpAdjRibInPathAttrAsPathLimUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrAsPathLimUpper.setStatus(_A)
_EltexBgpAdjRibInPathAttrMEDPrsnt_Type=TruthValue
_EltexBgpAdjRibInPathAttrMEDPrsnt_Object=MibTableColumn
eltexBgpAdjRibInPathAttrMEDPrsnt=_EltexBgpAdjRibInPathAttrMEDPrsnt_Object((1,3,6,1,4,1,35265,45,1,3,2,1,21),_EltexBgpAdjRibInPathAttrMEDPrsnt_Type())
eltexBgpAdjRibInPathAttrMEDPrsnt.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAttrMEDPrsnt.setStatus(_A)
_EltexBgpAdjRibInPathAccepted_Type=TruthValue
_EltexBgpAdjRibInPathAccepted_Object=MibTableColumn
eltexBgpAdjRibInPathAccepted=_EltexBgpAdjRibInPathAccepted_Object((1,3,6,1,4,1,35265,45,1,3,2,1,22),_EltexBgpAdjRibInPathAccepted_Type())
eltexBgpAdjRibInPathAccepted.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibInPathAccepted.setStatus(_A)
_EltexBgpAdjRibOutTable_Object=MibTable
eltexBgpAdjRibOutTable=_EltexBgpAdjRibOutTable_Object((1,3,6,1,4,1,35265,45,1,3,3))
if mibBuilder.loadTexts:eltexBgpAdjRibOutTable.setStatus(_A)
_EltexBgpAdjRibOutEntry_Object=MibTableRow
eltexBgpAdjRibOutEntry=_EltexBgpAdjRibOutEntry_Object((1,3,6,1,4,1,35265,45,1,3,3,1))
eltexBgpAdjRibOutEntry.setIndexNames((0,_D,_H),(0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u),(0,_D,_v),(0,_D,_w),(0,_D,_x))
if mibBuilder.loadTexts:eltexBgpAdjRibOutEntry.setStatus(_A)
_EltexBgpAdjRibOutAfi_Type=EltexBgpAfi
_EltexBgpAdjRibOutAfi_Object=MibTableColumn
eltexBgpAdjRibOutAfi=_EltexBgpAdjRibOutAfi_Object((1,3,6,1,4,1,35265,45,1,3,3,1,1),_EltexBgpAdjRibOutAfi_Type())
eltexBgpAdjRibOutAfi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAfi.setStatus(_A)
_EltexBgpAdjRibOutSafi_Type=EltexBgpSafi
_EltexBgpAdjRibOutSafi_Object=MibTableColumn
eltexBgpAdjRibOutSafi=_EltexBgpAdjRibOutSafi_Object((1,3,6,1,4,1,35265,45,1,3,3,1,2),_EltexBgpAdjRibOutSafi_Type())
eltexBgpAdjRibOutSafi.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutSafi.setStatus(_A)
_EltexBgpAdjRibOutPrfxType_Type=InetAddressType
_EltexBgpAdjRibOutPrfxType_Object=MibTableColumn
eltexBgpAdjRibOutPrfxType=_EltexBgpAdjRibOutPrfxType_Object((1,3,6,1,4,1,35265,45,1,3,3,1,3),_EltexBgpAdjRibOutPrfxType_Type())
eltexBgpAdjRibOutPrfxType.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutPrfxType.setStatus(_A)
_EltexBgpAdjRibOutPrfx_Type=InetAddress
_EltexBgpAdjRibOutPrfx_Object=MibTableColumn
eltexBgpAdjRibOutPrfx=_EltexBgpAdjRibOutPrfx_Object((1,3,6,1,4,1,35265,45,1,3,3,1,4),_EltexBgpAdjRibOutPrfx_Type())
eltexBgpAdjRibOutPrfx.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutPrfx.setStatus(_A)
_EltexBgpAdjRibOutPrfxLen_Type=InetAddressPrefixLength
_EltexBgpAdjRibOutPrfxLen_Object=MibTableColumn
eltexBgpAdjRibOutPrfxLen=_EltexBgpAdjRibOutPrfxLen_Object((1,3,6,1,4,1,35265,45,1,3,3,1,5),_EltexBgpAdjRibOutPrfxLen_Type())
eltexBgpAdjRibOutPrfxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutPrfxLen.setStatus(_A)
_EltexBgpAdjRibOutPathId_Type=Unsigned32
_EltexBgpAdjRibOutPathId_Object=MibTableColumn
eltexBgpAdjRibOutPathId=_EltexBgpAdjRibOutPathId_Object((1,3,6,1,4,1,35265,45,1,3,3,1,6),_EltexBgpAdjRibOutPathId_Type())
eltexBgpAdjRibOutPathId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpAdjRibOutPathId.setStatus(_A)
_EltexBgpAdjRibOutBest_Type=TruthValue
_EltexBgpAdjRibOutBest_Object=MibTableColumn
eltexBgpAdjRibOutBest=_EltexBgpAdjRibOutBest_Object((1,3,6,1,4,1,35265,45,1,3,3,1,7),_EltexBgpAdjRibOutBest_Type())
eltexBgpAdjRibOutBest.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutBest.setStatus(_A)
class _EltexBgpAdjRibOutAdvertStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertised',1),('suppressed',2),('pendingWithdrawal',3),('withdrawn',4)))
_EltexBgpAdjRibOutAdvertStatus_Type.__name__=_R
_EltexBgpAdjRibOutAdvertStatus_Object=MibTableColumn
eltexBgpAdjRibOutAdvertStatus=_EltexBgpAdjRibOutAdvertStatus_Object((1,3,6,1,4,1,35265,45,1,3,3,1,8),_EltexBgpAdjRibOutAdvertStatus_Type())
eltexBgpAdjRibOutAdvertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAdvertStatus.setStatus(_A)
class _EltexBgpAdjRibOutLocalAggrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noAggregation',1),('aggregateRoute',2),('unsuppAggregatedRoute',3),('suppressedAggregatedRoute',4)))
_EltexBgpAdjRibOutLocalAggrType_Type.__name__=_R
_EltexBgpAdjRibOutLocalAggrType_Object=MibTableColumn
eltexBgpAdjRibOutLocalAggrType=_EltexBgpAdjRibOutLocalAggrType_Object((1,3,6,1,4,1,35265,45,1,3,3,1,9),_EltexBgpAdjRibOutLocalAggrType_Type())
eltexBgpAdjRibOutLocalAggrType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutLocalAggrType.setStatus(_A)
_EltexBgpAdjRibOutAsSize_Type=EltexBgpAsSize
_EltexBgpAdjRibOutAsSize_Object=MibTableColumn
eltexBgpAdjRibOutAsSize=_EltexBgpAdjRibOutAsSize_Object((1,3,6,1,4,1,35265,45,1,3,3,1,10),_EltexBgpAdjRibOutAsSize_Type())
eltexBgpAdjRibOutAsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAsSize.setStatus(_A)
class _EltexBgpAdjRibOutASPathStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltexBgpAdjRibOutASPathStr_Type.__name__=_I
_EltexBgpAdjRibOutASPathStr_Object=MibTableColumn
eltexBgpAdjRibOutASPathStr=_EltexBgpAdjRibOutASPathStr_Object((1,3,6,1,4,1,35265,45,1,3,3,1,11),_EltexBgpAdjRibOutASPathStr_Type())
eltexBgpAdjRibOutASPathStr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutASPathStr.setStatus(_A)
_EltexBgpAdjRibOutOrigin_Type=EltexBgpOriginCode
_EltexBgpAdjRibOutOrigin_Object=MibTableColumn
eltexBgpAdjRibOutOrigin=_EltexBgpAdjRibOutOrigin_Object((1,3,6,1,4,1,35265,45,1,3,3,1,12),_EltexBgpAdjRibOutOrigin_Type())
eltexBgpAdjRibOutOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutOrigin.setStatus(_A)
_EltexBgpAdjRibOutNextHopType_Type=InetAddressType
_EltexBgpAdjRibOutNextHopType_Object=MibTableColumn
eltexBgpAdjRibOutNextHopType=_EltexBgpAdjRibOutNextHopType_Object((1,3,6,1,4,1,35265,45,1,3,3,1,13),_EltexBgpAdjRibOutNextHopType_Type())
eltexBgpAdjRibOutNextHopType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutNextHopType.setStatus(_A)
_EltexBgpAdjRibOutNextHop_Type=InetAddress
_EltexBgpAdjRibOutNextHop_Object=MibTableColumn
eltexBgpAdjRibOutNextHop=_EltexBgpAdjRibOutNextHop_Object((1,3,6,1,4,1,35265,45,1,3,3,1,14),_EltexBgpAdjRibOutNextHop_Type())
eltexBgpAdjRibOutNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutNextHop.setStatus(_A)
_EltexBgpAdjRibOutMultiExitDisc_Type=Unsigned32
_EltexBgpAdjRibOutMultiExitDisc_Object=MibTableColumn
eltexBgpAdjRibOutMultiExitDisc=_EltexBgpAdjRibOutMultiExitDisc_Object((1,3,6,1,4,1,35265,45,1,3,3,1,15),_EltexBgpAdjRibOutMultiExitDisc_Type())
eltexBgpAdjRibOutMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutMultiExitDisc.setStatus(_A)
_EltexBgpAdjRibOutLocalPref_Type=Unsigned32
_EltexBgpAdjRibOutLocalPref_Object=MibTableColumn
eltexBgpAdjRibOutLocalPref=_EltexBgpAdjRibOutLocalPref_Object((1,3,6,1,4,1,35265,45,1,3,3,1,16),_EltexBgpAdjRibOutLocalPref_Type())
eltexBgpAdjRibOutLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutLocalPref.setStatus(_A)
_EltexBgpAdjRibOutAtomicAggregate_Type=TruthValue
_EltexBgpAdjRibOutAtomicAggregate_Object=MibTableColumn
eltexBgpAdjRibOutAtomicAggregate=_EltexBgpAdjRibOutAtomicAggregate_Object((1,3,6,1,4,1,35265,45,1,3,3,1,17),_EltexBgpAdjRibOutAtomicAggregate_Type())
eltexBgpAdjRibOutAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAtomicAggregate.setStatus(_A)
_EltexBgpAdjRibOutAggregatorAS_Type=EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibOutAggregatorAS_Object=MibTableColumn
eltexBgpAdjRibOutAggregatorAS=_EltexBgpAdjRibOutAggregatorAS_Object((1,3,6,1,4,1,35265,45,1,3,3,1,18),_EltexBgpAdjRibOutAggregatorAS_Type())
eltexBgpAdjRibOutAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAggregatorAS.setStatus(_A)
_EltexBgpAdjRibOutAggregatorAddr_Type=EltexBgpIdentifier
_EltexBgpAdjRibOutAggregatorAddr_Object=MibTableColumn
eltexBgpAdjRibOutAggregatorAddr=_EltexBgpAdjRibOutAggregatorAddr_Object((1,3,6,1,4,1,35265,45,1,3,3,1,19),_EltexBgpAdjRibOutAggregatorAddr_Type())
eltexBgpAdjRibOutAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAggregatorAddr.setStatus(_A)
_EltexBgpAdjRibOutOrigId_Type=EltexBgpIdentifier
_EltexBgpAdjRibOutOrigId_Object=MibTableColumn
eltexBgpAdjRibOutOrigId=_EltexBgpAdjRibOutOrigId_Object((1,3,6,1,4,1,35265,45,1,3,3,1,20),_EltexBgpAdjRibOutOrigId_Type())
eltexBgpAdjRibOutOrigId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutOrigId.setStatus(_A)
_EltexBgpAdjRibOutEcmp_Type=TruthValue
_EltexBgpAdjRibOutEcmp_Object=MibTableColumn
eltexBgpAdjRibOutEcmp=_EltexBgpAdjRibOutEcmp_Object((1,3,6,1,4,1,35265,45,1,3,3,1,21),_EltexBgpAdjRibOutEcmp_Type())
eltexBgpAdjRibOutEcmp.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutEcmp.setStatus(_A)
_EltexBgpAdjRibOutAsLimAs_Type=EltexBgpAutonomousSystemNumber
_EltexBgpAdjRibOutAsLimAs_Object=MibTableColumn
eltexBgpAdjRibOutAsLimAs=_EltexBgpAdjRibOutAsLimAs_Object((1,3,6,1,4,1,35265,45,1,3,3,1,22),_EltexBgpAdjRibOutAsLimAs_Type())
eltexBgpAdjRibOutAsLimAs.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAsLimAs.setStatus(_A)
class _EltexBgpAdjRibOutAsLimUpper_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexBgpAdjRibOutAsLimUpper_Type.__name__=_E
_EltexBgpAdjRibOutAsLimUpper_Object=MibTableColumn
eltexBgpAdjRibOutAsLimUpper=_EltexBgpAdjRibOutAsLimUpper_Object((1,3,6,1,4,1,35265,45,1,3,3,1,23),_EltexBgpAdjRibOutAsLimUpper_Type())
eltexBgpAdjRibOutAsLimUpper.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutAsLimUpper.setStatus(_A)
_EltexBgpAdjRibOutIsActive_Type=EltexBgpNlriIsActiveFlag
_EltexBgpAdjRibOutIsActive_Object=MibTableColumn
eltexBgpAdjRibOutIsActive=_EltexBgpAdjRibOutIsActive_Object((1,3,6,1,4,1,35265,45,1,3,3,1,24),_EltexBgpAdjRibOutIsActive_Type())
eltexBgpAdjRibOutIsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutIsActive.setStatus(_A)
_EltexBgpAdjRibOutMEDPrsnt_Type=TruthValue
_EltexBgpAdjRibOutMEDPrsnt_Object=MibTableColumn
eltexBgpAdjRibOutMEDPrsnt=_EltexBgpAdjRibOutMEDPrsnt_Object((1,3,6,1,4,1,35265,45,1,3,3,1,25),_EltexBgpAdjRibOutMEDPrsnt_Type())
eltexBgpAdjRibOutMEDPrsnt.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutMEDPrsnt.setStatus(_A)
_EltexBgpAdjRibOutPeerType_Type=EltexBgpNlriPeerTypes
_EltexBgpAdjRibOutPeerType_Object=MibTableColumn
eltexBgpAdjRibOutPeerType=_EltexBgpAdjRibOutPeerType_Object((1,3,6,1,4,1,35265,45,1,3,3,1,26),_EltexBgpAdjRibOutPeerType_Type())
eltexBgpAdjRibOutPeerType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpAdjRibOutPeerType.setStatus(_A)
_EltexBgpNetworkTable_Object=MibTable
eltexBgpNetworkTable=_EltexBgpNetworkTable_Object((1,3,6,1,4,1,35265,45,1,3,4))
if mibBuilder.loadTexts:eltexBgpNetworkTable.setStatus(_A)
_EltexBgpNetworkEntry_Object=MibTableRow
eltexBgpNetworkEntry=_EltexBgpNetworkEntry_Object((1,3,6,1,4,1,35265,45,1,3,4,1))
eltexBgpNetworkEntry.setIndexNames((0,_D,_H),(0,_D,_y),(0,_D,_z),(0,_D,_A0),(0,_D,_A1),(0,_D,_A2))
if mibBuilder.loadTexts:eltexBgpNetworkEntry.setStatus(_A)
class _EltexBgpNetworkAfi_Type(EltexBgpAfi):defaultValue=1
_EltexBgpNetworkAfi_Type.__name__=_A3
_EltexBgpNetworkAfi_Object=MibTableColumn
eltexBgpNetworkAfi=_EltexBgpNetworkAfi_Object((1,3,6,1,4,1,35265,45,1,3,4,1,1),_EltexBgpNetworkAfi_Type())
eltexBgpNetworkAfi.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpNetworkAfi.setStatus(_A)
class _EltexBgpNetworkSafi_Type(EltexBgpSafi):defaultValue=1
_EltexBgpNetworkSafi_Type.__name__=_A4
_EltexBgpNetworkSafi_Object=MibTableColumn
eltexBgpNetworkSafi=_EltexBgpNetworkSafi_Object((1,3,6,1,4,1,35265,45,1,3,4,1,2),_EltexBgpNetworkSafi_Type())
eltexBgpNetworkSafi.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpNetworkSafi.setStatus(_A)
_EltexBgpNetworkPrfxType_Type=InetAddressType
_EltexBgpNetworkPrfxType_Object=MibTableColumn
eltexBgpNetworkPrfxType=_EltexBgpNetworkPrfxType_Object((1,3,6,1,4,1,35265,45,1,3,4,1,3),_EltexBgpNetworkPrfxType_Type())
eltexBgpNetworkPrfxType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpNetworkPrfxType.setStatus(_A)
_EltexBgpNetworkPrfx_Type=InetAddress
_EltexBgpNetworkPrfx_Object=MibTableColumn
eltexBgpNetworkPrfx=_EltexBgpNetworkPrfx_Object((1,3,6,1,4,1,35265,45,1,3,4,1,4),_EltexBgpNetworkPrfx_Type())
eltexBgpNetworkPrfx.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpNetworkPrfx.setStatus(_A)
_EltexBgpNetworkPrfxLen_Type=InetAddressPrefixLength
_EltexBgpNetworkPrfxLen_Object=MibTableColumn
eltexBgpNetworkPrfxLen=_EltexBgpNetworkPrfxLen_Object((1,3,6,1,4,1,35265,45,1,3,4,1,5),_EltexBgpNetworkPrfxLen_Type())
eltexBgpNetworkPrfxLen.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexBgpNetworkPrfxLen.setStatus(_A)
_EltexBgpNetworkRowStatus_Type=RowStatus
_EltexBgpNetworkRowStatus_Object=MibTableColumn
eltexBgpNetworkRowStatus=_EltexBgpNetworkRowStatus_Object((1,3,6,1,4,1,35265,45,1,3,4,1,6),_EltexBgpNetworkRowStatus_Type())
eltexBgpNetworkRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:eltexBgpNetworkRowStatus.setStatus(_A)
_EltexBgpPathAttrExtensions_ObjectIdentity=ObjectIdentity
eltexBgpPathAttrExtensions=_EltexBgpPathAttrExtensions_ObjectIdentity((1,3,6,1,4,1,35265,45,1,3,5))
_EltexBgpPathAttrRouteReflectionExts_ObjectIdentity=ObjectIdentity
eltexBgpPathAttrRouteReflectionExts=_EltexBgpPathAttrRouteReflectionExts_ObjectIdentity((1,3,6,1,4,1,35265,45,1,3,5,1))
_EltexBgpPathAttrClusterLocTable_Object=MibTable
eltexBgpPathAttrClusterLocTable=_EltexBgpPathAttrClusterLocTable_Object((1,3,6,1,4,1,35265,45,1,3,5,1,1))
if mibBuilder.loadTexts:eltexBgpPathAttrClusterLocTable.setStatus(_A)
_EltexBgpPathAttrClusterLocEntry_Object=MibTableRow
eltexBgpPathAttrClusterLocEntry=_EltexBgpPathAttrClusterLocEntry_Object((1,3,6,1,4,1,35265,45,1,3,5,1,1,1))
eltexBgpPathAttrClusterLocEntry.setIndexNames((0,_D,_H),(0,_D,_a),(0,_D,_b),(0,_D,_W),(0,_D,_X),(0,_D,_Y),(0,_D,_Z),(0,_D,_c),(0,_D,_A5))
if mibBuilder.loadTexts:eltexBgpPathAttrClusterLocEntry.setStatus(_A)
_EltexBgpPathAttrClusterLocIndex_Type=Unsigned32
_EltexBgpPathAttrClusterLocIndex_Object=MibTableColumn
eltexBgpPathAttrClusterLocIndex=_EltexBgpPathAttrClusterLocIndex_Object((1,3,6,1,4,1,35265,45,1,3,5,1,1,1,1),_EltexBgpPathAttrClusterLocIndex_Type())
eltexBgpPathAttrClusterLocIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexBgpPathAttrClusterLocIndex.setStatus(_A)
_EltexBgpPathAttrClusterLocValue_Type=Unsigned32
_EltexBgpPathAttrClusterLocValue_Object=MibTableColumn
eltexBgpPathAttrClusterLocValue=_EltexBgpPathAttrClusterLocValue_Object((1,3,6,1,4,1,35265,45,1,3,5,1,1,1,2),_EltexBgpPathAttrClusterLocValue_Type())
eltexBgpPathAttrClusterLocValue.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexBgpPathAttrClusterLocValue.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_N:EltexBgpIdentifier,_A3:EltexBgpAfi,_A4:EltexBgpSafi,'EltexBgpAutonomousSystemNumber':EltexBgpAutonomousSystemNumber,'EltexBgpAsSize':EltexBgpAsSize,_S:EltexBgpAdminStatus,'EltexBgpOperStatus':EltexBgpOperStatus,'EltexBgpOriginCode':EltexBgpOriginCode,_O:EltexBgpConfigDropOrWarn,'EltexBgpPeerOrRib':EltexBgpPeerOrRib,'EltexBgpPeerStates':EltexBgpPeerStates,'EltexBgpPeerEvents':EltexBgpPeerEvents,'EltexBgpCapabilities':EltexBgpCapabilities,_h:EltexBgpCeaseErrorSubcode,'EltexBgpNlriIsActiveFlag':EltexBgpNlriIsActiveFlag,'EltexBgpPeerConfigStates':EltexBgpPeerConfigStates,'EltexBgpReasonNotBest':EltexBgpReasonNotBest,'EltexBgpNlriPeerTypes':EltexBgpNlriPeerTypes,_e:EltexBgpASNotation,_P:EltexBgpPeerReflectorClientType,'EltexBgpRouteMapAsPathAction':EltexBgpRouteMapAsPathAction,'EltexBgpAddPathSrCap':EltexBgpAddPathSrCap,'EltexBfdSessionStatus':EltexBfdSessionStatus,'eltexBgpMIB':eltexBgpMIB,'eltexBgpObjects':eltexBgpObjects,'eltexBgpProcess':eltexBgpProcess,'eltexBgpProcessTable':eltexBgpProcessTable,'eltexBgpProcessEntry':eltexBgpProcessEntry,_H:eltexBgpProcessId,'eltexBgpProcessRowStatus':eltexBgpProcessRowStatus,'eltexBgpProcessAdminStatus':eltexBgpProcessAdminStatus,'eltexBgpProcessOperStatus':eltexBgpProcessOperStatus,'eltexBgpProcessLocalAs':eltexBgpProcessLocalAs,'eltexBgpProcessLocalIdentifier':eltexBgpProcessLocalIdentifier,'eltexBgpProcessOperLocalIdentifier':eltexBgpProcessOperLocalIdentifier,'eltexBgpProcessTableVersion':eltexBgpProcessTableVersion,'eltexBgpProcessASNotation':eltexBgpProcessASNotation,'eltexBgpProcessClusterIdentifier':eltexBgpProcessClusterIdentifier,'eltexBgpProcessOperClusterIdentifier':eltexBgpProcessOperClusterIdentifier,'eltexBgpProcessInterClientReflEnabled':eltexBgpProcessInterClientReflEnabled,'eltexBgpProcessPathMtuDiscovery':eltexBgpProcessPathMtuDiscovery,'eltexBgpProcessAddrFamilyTable':eltexBgpProcessAddrFamilyTable,'eltexBgpProcessAddrFamilyEntry':eltexBgpProcessAddrFamilyEntry,_f:eltexBgpProcessAddrFamilyAfi,_g:eltexBgpProcessAddrFamilySafi,'eltexBgpProcessAddrFamilyRowStatus':eltexBgpProcessAddrFamilyRowStatus,'eltexBgpPeer':eltexBgpPeer,'eltexBgpPeerData':eltexBgpPeerData,'eltexBgpPeerTable':eltexBgpPeerTable,'eltexBgpPeerEntry':eltexBgpPeerEntry,_K:eltexBgpPeerRemoteAddrType,_L:eltexBgpPeerRemoteAddr,'eltexBgpPeerRowStatus':eltexBgpPeerRowStatus,'eltexBgpPeerAdminStatus':eltexBgpPeerAdminStatus,'eltexBgpPeerOperStatus':eltexBgpPeerOperStatus,'eltexBgpPeerRemoteAs':eltexBgpPeerRemoteAs,'eltexBgpPeerSourceInterface':eltexBgpPeerSourceInterface,'eltexBgpPeerNxtHopSlf':eltexBgpPeerNxtHopSlf,'eltexBgpPeerConfigMaxPrfx':eltexBgpPeerConfigMaxPrfx,'eltexBgpPeerConfigDropWarn':eltexBgpPeerConfigDropWarn,'eltexBgpPeerMaxPrfxHold':eltexBgpPeerMaxPrfxHold,'eltexBgpPeerConfigThreshold':eltexBgpPeerConfigThreshold,'eltexBgpPeerConnectRetryInterval':eltexBgpPeerConnectRetryInterval,'eltexBgpPeerHoldTimeConfigd':eltexBgpPeerHoldTimeConfigd,'eltexBgpPeerKeepAliveConfigd':eltexBgpPeerKeepAliveConfigd,'eltexBgpPeerMinRouteAdvertiseInterval':eltexBgpPeerMinRouteAdvertiseInterval,'eltexBgpPeerMinASOriginationInterval':eltexBgpPeerMinASOriginationInterval,'eltexBgpPeerMinRouteWithdrawInterval':eltexBgpPeerMinRouteWithdrawInterval,'eltexBgpPeerConfigOpenDelay':eltexBgpPeerConfigOpenDelay,'eltexBgpPeerConfigIdleHold':eltexBgpPeerConfigIdleHold,'eltexBgpPeerDistListPlIn':eltexBgpPeerDistListPlIn,'eltexBgpPeerDistListPlOut':eltexBgpPeerDistListPlOut,'eltexBgpPeerReflectorClient':eltexBgpPeerReflectorClient,'eltexBgpPeerSoftResetWithStoredInfo':eltexBgpPeerSoftResetWithStoredInfo,'eltexBgpPeerConfigPeerGroup':eltexBgpPeerConfigPeerGroup,'eltexBgpPeerPathMtuDiscovery':eltexBgpPeerPathMtuDiscovery,'eltexBgpPeerBfdDesired':eltexBgpPeerBfdDesired,'eltexBgpPeerAddrFamilyTable':eltexBgpPeerAddrFamilyTable,'eltexBgpPeerAddrFamilyEntry':eltexBgpPeerAddrFamilyEntry,_U:eltexBgpPeerAddrFamilyAfi,_V:eltexBgpPeerAddrFamilySafi,'eltexBgpPeerAddrFamilyDisable':eltexBgpPeerAddrFamilyDisable,'eltexBgpPeerAddrFamilyNxtHopSlf':eltexBgpPeerAddrFamilyNxtHopSlf,'eltexBgpPeerAddrFamilyConfigMaxPrfx':eltexBgpPeerAddrFamilyConfigMaxPrfx,'eltexBgpPeerAddrFamilyConfigDropWarn':eltexBgpPeerAddrFamilyConfigDropWarn,'eltexBgpPeerAddrFamilyMaxPrfxHold':eltexBgpPeerAddrFamilyMaxPrfxHold,'eltexBgpPeerAddrFamilyConfigThreshold':eltexBgpPeerAddrFamilyConfigThreshold,'eltexBgpPeerAddrFamilyMinRteAdvertInt':eltexBgpPeerAddrFamilyMinRteAdvertInt,'eltexBgpPeerAddrFamilyMinASOrigInt':eltexBgpPeerAddrFamilyMinASOrigInt,'eltexBgpPeerAddrFamilyMinRteWithdrawInt':eltexBgpPeerAddrFamilyMinRteWithdrawInt,'eltexBgpPeerAddrFamilyReflectorClient':eltexBgpPeerAddrFamilyReflectorClient,'eltexBgpPeerAddrFamilyRouteMapIn':eltexBgpPeerAddrFamilyRouteMapIn,'eltexBgpPeerAddrFamilyRouteMapOut':eltexBgpPeerAddrFamilyRouteMapOut,'eltexBgpPeerStatusTable':eltexBgpPeerStatusTable,'eltexBgpPeerStatusEntry':eltexBgpPeerStatusEntry,'eltexBgpPeerStatusIdentifier':eltexBgpPeerStatusIdentifier,'eltexBgpPeerStatusState':eltexBgpPeerStatusState,'eltexBgpPeerStatusDynamicPeer':eltexBgpPeerStatusDynamicPeer,'eltexBgpPeerStatusRemoteAs':eltexBgpPeerStatusRemoteAs,_r:eltexBgpPeerStatusPeerIndex,'eltexBgpPeerStatusCapsSupport':eltexBgpPeerStatusCapsSupport,'eltexBgpPeerStatusLastError':eltexBgpPeerStatusLastError,'eltexBgpPeerStatusLastErrorDataLen':eltexBgpPeerStatusLastErrorDataLen,'eltexBgpPeerStatusLastErrorData':eltexBgpPeerStatusLastErrorData,'eltexBgpPeerStatusFsmEstablishedTime':eltexBgpPeerStatusFsmEstablishedTime,'eltexBgpPeerStatusInUpdatesElpsTime':eltexBgpPeerStatusInUpdatesElpsTime,'eltexBgpPeerStatusHoldTime':eltexBgpPeerStatusHoldTime,'eltexBgpPeerStatusKeepAlive':eltexBgpPeerStatusKeepAlive,'eltexBgpPeerStatusInOpens':eltexBgpPeerStatusInOpens,'eltexBgpPeerStatusOutOpens':eltexBgpPeerStatusOutOpens,'eltexBgpPeerStatusInNotifications':eltexBgpPeerStatusInNotifications,'eltexBgpPeerStatusOutNotifications':eltexBgpPeerStatusOutNotifications,'eltexBgpPeerStatusInUpdates':eltexBgpPeerStatusInUpdates,'eltexBgpPeerStatusOutUpdates':eltexBgpPeerStatusOutUpdates,'eltexBgpPeerStatusInKeepalives':eltexBgpPeerStatusInKeepalives,'eltexBgpPeerStatusOutKeepalives':eltexBgpPeerStatusOutKeepalives,'eltexBgpPeerStatusInRefreshes':eltexBgpPeerStatusInRefreshes,'eltexBgpPeerStatusOutRefreshes':eltexBgpPeerStatusOutRefreshes,'eltexBgpPeerStatusInTotalMessages':eltexBgpPeerStatusInTotalMessages,'eltexBgpPeerStatusOutTotalMessages':eltexBgpPeerStatusOutTotalMessages,'eltexBgpPeerStatusFsmEstTransitions':eltexBgpPeerStatusFsmEstTransitions,'eltexBgpPeerStatusConnectRetryCount':eltexBgpPeerStatusConnectRetryCount,'eltexBgpPeerStatusClearCnts':eltexBgpPeerStatusClearCnts,'eltexBgpPeerStatusRtRefresh':eltexBgpPeerStatusRtRefresh,'eltexBgpPeerStatusLastErrorRcvd':eltexBgpPeerStatusLastErrorRcvd,'eltexBgpPeerStatusLastErrorRcvdTime':eltexBgpPeerStatusLastErrorRcvdTime,'eltexBgpPeerStatusLastErrorSent':eltexBgpPeerStatusLastErrorSent,'eltexBgpPeerStatusLastErrorSentTime':eltexBgpPeerStatusLastErrorSentTime,'eltexBgpPeerStatusLastState':eltexBgpPeerStatusLastState,'eltexBgpPeerStatusLastEvent':eltexBgpPeerStatusLastEvent,'eltexBgpPeerStatusCapsSent':eltexBgpPeerStatusCapsSent,'eltexBgpPeerStatusCapsRcvd':eltexBgpPeerStatusCapsRcvd,'eltexBgpPeerStatusCapsNegotiated':eltexBgpPeerStatusCapsNegotiated,'eltexBgpPeerStatusRcvdMsgElpsTime':eltexBgpPeerStatusRcvdMsgElpsTime,'eltexBgpPeerStatusIdleHoldRemTime':eltexBgpPeerStatusIdleHoldRemTime,'eltexBgpPeerStatusRouteRefrSent':eltexBgpPeerStatusRouteRefrSent,'eltexBgpPeerStatusRouteRefrRcvd':eltexBgpPeerStatusRouteRefrRcvd,'eltexBgpPeerStatusSelLocalAddrType':eltexBgpPeerStatusSelLocalAddrType,'eltexBgpPeerStatusSelLocalAddr':eltexBgpPeerStatusSelLocalAddr,'eltexBgpPeerStatusSelLocalPort':eltexBgpPeerStatusSelLocalPort,'eltexBgpPeerStatusSelRemotePort':eltexBgpPeerStatusSelRemotePort,'eltexBgpPeerStatusSelLocalAs':eltexBgpPeerStatusSelLocalAs,'eltexBgpPeerStatusSelRemoteAs':eltexBgpPeerStatusSelRemoteAs,'eltexBgpPeerStatusInPrfxes':eltexBgpPeerStatusInPrfxes,'eltexBgpPeerStatusOutPrfxes':eltexBgpPeerStatusOutPrfxes,'eltexBgpPeerStatusOutPrfxesAdvertised':eltexBgpPeerStatusOutPrfxesAdvertised,'eltexBgpPeerStatusConfigState':eltexBgpPeerStatusConfigState,'eltexBgpPeerStatusConnectRetryInt':eltexBgpPeerStatusConnectRetryInt,'eltexBgpPeerStatusConfigPassive':eltexBgpPeerStatusConfigPassive,'eltexBgpPeerStatusConfigOpenDelay':eltexBgpPeerStatusConfigOpenDelay,'eltexBgpPeerStatusConfigIdleHold':eltexBgpPeerStatusConfigIdleHold,'eltexBgpPeerStatusTtl':eltexBgpPeerStatusTtl,'eltexBgpPeerStatusHoldTimeConfigd':eltexBgpPeerStatusHoldTimeConfigd,'eltexBgpPeerStatusKeepAliveConfigd':eltexBgpPeerStatusKeepAliveConfigd,'eltexBgpPeerStatusResendAllRoutes':eltexBgpPeerStatusResendAllRoutes,'eltexBgpPeerStatusOutUpdateElpsTime':eltexBgpPeerStatusOutUpdateElpsTime,'eltexBgpPeerStatusOutPrfxesDenied':eltexBgpPeerStatusOutPrfxesDenied,'eltexBgpPeerStatusOutPrfxesImpWdr':eltexBgpPeerStatusOutPrfxesImpWdr,'eltexBgpPeerStatusOutPrfxesExpWdr':eltexBgpPeerStatusOutPrfxesExpWdr,'eltexBgpPeerStatusInPrfxesImpWdr':eltexBgpPeerStatusInPrfxesImpWdr,'eltexBgpPeerStatusInPrfxesExpWdr':eltexBgpPeerStatusInPrfxesExpWdr,'eltexBgpPeerStatusReceivedHoldTime':eltexBgpPeerStatusReceivedHoldTime,'eltexBgpPeerStatusDropSession':eltexBgpPeerStatusDropSession,'eltexBgpPeerStatusCeaseErrorSubcode':eltexBgpPeerStatusCeaseErrorSubcode,'eltexBgpPeerStatusBfdStatus':eltexBgpPeerStatusBfdStatus,'eltexBgpPeerAddrFamilyStatusTable':eltexBgpPeerAddrFamilyStatusTable,'eltexBgpPeerAddrFamilyStatusEntry':eltexBgpPeerAddrFamilyStatusEntry,'eltexBgpPeerAddrFamilyStatusRtRefresh':eltexBgpPeerAddrFamilyStatusRtRefresh,'eltexBgpPeerAddrFamilyStatusAddPathCapNeg':eltexBgpPeerAddrFamilyStatusAddPathCapNeg,'eltexBgpPeerAddrFamilyStatusReflectorClient':eltexBgpPeerAddrFamilyStatusReflectorClient,'eltexBgpPeerAddrFamilyStatusUpdateGroup':eltexBgpPeerAddrFamilyStatusUpdateGroup,'eltexBgpPeerAddrFamilyStatusResendAllRoutes':eltexBgpPeerAddrFamilyStatusResendAllRoutes,'eltexBgpPeerGroup':eltexBgpPeerGroup,'eltexBgpPeerGroupTable':eltexBgpPeerGroupTable,'eltexBgpPeerGroupEntry':eltexBgpPeerGroupEntry,_i:eltexBgpPeerGroupName,'eltexBgpPeerGroupRowStatus':eltexBgpPeerGroupRowStatus,'eltexBgpPeerGroupRemoteAs':eltexBgpPeerGroupRemoteAs,'eltexBgpPeerGroupSourceInterface':eltexBgpPeerGroupSourceInterface,'eltexBgpPeerGroupNxtHopSlf':eltexBgpPeerGroupNxtHopSlf,'eltexBgpPeerGroupConfigMaxPrfx':eltexBgpPeerGroupConfigMaxPrfx,'eltexBgpPeerGroupConfigDropWarn':eltexBgpPeerGroupConfigDropWarn,'eltexBgpPeerGroupMaxPrfxHold':eltexBgpPeerGroupMaxPrfxHold,'eltexBgpPeerGroupConfigThreshold':eltexBgpPeerGroupConfigThreshold,'eltexBgpPeerGroupConnectRetryInterval':eltexBgpPeerGroupConnectRetryInterval,'eltexBgpPeerGroupHoldTimeConfigd':eltexBgpPeerGroupHoldTimeConfigd,'eltexBgpPeerGroupKeepAliveConfigd':eltexBgpPeerGroupKeepAliveConfigd,'eltexBgpPeerGroupMinRouteAdvertiseInterval':eltexBgpPeerGroupMinRouteAdvertiseInterval,'eltexBgpPeerGroupMinASOriginationInterval':eltexBgpPeerGroupMinASOriginationInterval,'eltexBgpPeerGroupMinRouteWithdrawInterval':eltexBgpPeerGroupMinRouteWithdrawInterval,'eltexBgpPeerGroupConfigOpenDelay':eltexBgpPeerGroupConfigOpenDelay,'eltexBgpPeerGroupConfigIdleHold':eltexBgpPeerGroupConfigIdleHold,'eltexBgpPeerGroupDistListPlIn':eltexBgpPeerGroupDistListPlIn,'eltexBgpPeerGroupDistListPlOut':eltexBgpPeerGroupDistListPlOut,'eltexBgpPeerGroupReflectorClient':eltexBgpPeerGroupReflectorClient,'eltexBgpPeerGroupSoftResetWithStoredInfo':eltexBgpPeerGroupSoftResetWithStoredInfo,'eltexBgpPeerGroupBfdDesired':eltexBgpPeerGroupBfdDesired,'eltexBgpRib':eltexBgpRib,'eltexBgpLocRibTable':eltexBgpLocRibTable,'eltexBgpLocRibEntry':eltexBgpLocRibEntry,_W:eltexBgpLocRibAfi,_X:eltexBgpLocRibSafi,_j:eltexBgpLocRibPrfxType,_Y:eltexBgpLocRibPrfx,_Z:eltexBgpLocRibPrfxLen,_a:eltexBgpLocRibPeerOrRib,_b:eltexBgpLocRibPeerRibIndex,_c:eltexBgpLocRibPathId,'eltexBgpLocRibBest':eltexBgpLocRibBest,'eltexBgpLocRibAsSize':eltexBgpLocRibAsSize,'eltexBgpLocRibASPathStr':eltexBgpLocRibASPathStr,'eltexBgpLocRibPathAttrOrigin':eltexBgpLocRibPathAttrOrigin,'eltexBgpLocRibPathAttrNextHopType':eltexBgpLocRibPathAttrNextHopType,'eltexBgpLocRibPathAttrNextHop':eltexBgpLocRibPathAttrNextHop,'eltexBgpLocRibPathAttrMultExtDisc':eltexBgpLocRibPathAttrMultExtDisc,'eltexBgpLocRibPathAttrLocalPref':eltexBgpLocRibPathAttrLocalPref,'eltexBgpLocRibPathAttrAtomicAgg':eltexBgpLocRibPathAttrAtomicAgg,'eltexBgpLocRibPathAttrAggAS':eltexBgpLocRibPathAttrAggAS,'eltexBgpLocRibPathAttrAggAddr':eltexBgpLocRibPathAttrAggAddr,'eltexBgpLocRibPathAttrCalcLclPref':eltexBgpLocRibPathAttrCalcLclPref,'eltexBgpLocRibPathAttrOrigId':eltexBgpLocRibPathAttrOrigId,'eltexBgpLocRibPathAttrWeight':eltexBgpLocRibPathAttrWeight,'eltexBgpLocRibEcmp':eltexBgpLocRibEcmp,'eltexBgpLocRibPathAttrAsPathLimAs':eltexBgpLocRibPathAttrAsPathLimAs,'eltexBgpLocRibPthAttAsPthLimUpper':eltexBgpLocRibPthAttAsPthLimUpper,'eltexBgpLocRibIsActive':eltexBgpLocRibIsActive,'eltexBgpLocRibPathAttrMEDPrsnt':eltexBgpLocRibPathAttrMEDPrsnt,'eltexBgpLocRibReasonNotBest':eltexBgpLocRibReasonNotBest,'eltexBgpLocRibPeerType':eltexBgpLocRibPeerType,'eltexBgpAdjRibInTable':eltexBgpAdjRibInTable,'eltexBgpAdjRibInEntry':eltexBgpAdjRibInEntry,_k:eltexBgpAdjRibInPeerIndex,_l:eltexBgpAdjRibInAfi,_m:eltexBgpAdjRibInSafi,_n:eltexBgpAdjRibInPrfxType,_o:eltexBgpAdjRibInPrfx,_p:eltexBgpAdjRibInPrfxLen,_q:eltexBgpAdjRibInPathId,'eltexBgpAdjRibInAsSize':eltexBgpAdjRibInAsSize,'eltexBgpAdjRibInASPathStr':eltexBgpAdjRibInASPathStr,'eltexBgpAdjRibInPathAttrOrigin':eltexBgpAdjRibInPathAttrOrigin,'eltexBgpAdjRibInPathAttrNextHopType':eltexBgpAdjRibInPathAttrNextHopType,'eltexBgpAdjRibInPathAttrNextHop':eltexBgpAdjRibInPathAttrNextHop,'eltexBgpAdjRibInPathAttrMultiExitDisc':eltexBgpAdjRibInPathAttrMultiExitDisc,'eltexBgpAdjRibInPathAttrLocalPref':eltexBgpAdjRibInPathAttrLocalPref,'eltexBgpAdjRibInPathAttrAtomicAggregate':eltexBgpAdjRibInPathAttrAtomicAggregate,'eltexBgpAdjRibInPathAttrAggregatorAS':eltexBgpAdjRibInPathAttrAggregatorAS,'eltexBgpAdjRibInPathAttrAggregatorAddr':eltexBgpAdjRibInPathAttrAggregatorAddr,'eltexBgpAdjRibInPathAttrOrigId':eltexBgpAdjRibInPathAttrOrigId,'eltexBgpAdjRibInPathAttrAsPathLimAs':eltexBgpAdjRibInPathAttrAsPathLimAs,'eltexBgpAdjRibInPathAttrAsPathLimUpper':eltexBgpAdjRibInPathAttrAsPathLimUpper,'eltexBgpAdjRibInPathAttrMEDPrsnt':eltexBgpAdjRibInPathAttrMEDPrsnt,'eltexBgpAdjRibInPathAccepted':eltexBgpAdjRibInPathAccepted,'eltexBgpAdjRibOutTable':eltexBgpAdjRibOutTable,'eltexBgpAdjRibOutEntry':eltexBgpAdjRibOutEntry,_s:eltexBgpAdjRibOutAfi,_t:eltexBgpAdjRibOutSafi,_u:eltexBgpAdjRibOutPrfxType,_v:eltexBgpAdjRibOutPrfx,_w:eltexBgpAdjRibOutPrfxLen,_x:eltexBgpAdjRibOutPathId,'eltexBgpAdjRibOutBest':eltexBgpAdjRibOutBest,'eltexBgpAdjRibOutAdvertStatus':eltexBgpAdjRibOutAdvertStatus,'eltexBgpAdjRibOutLocalAggrType':eltexBgpAdjRibOutLocalAggrType,'eltexBgpAdjRibOutAsSize':eltexBgpAdjRibOutAsSize,'eltexBgpAdjRibOutASPathStr':eltexBgpAdjRibOutASPathStr,'eltexBgpAdjRibOutOrigin':eltexBgpAdjRibOutOrigin,'eltexBgpAdjRibOutNextHopType':eltexBgpAdjRibOutNextHopType,'eltexBgpAdjRibOutNextHop':eltexBgpAdjRibOutNextHop,'eltexBgpAdjRibOutMultiExitDisc':eltexBgpAdjRibOutMultiExitDisc,'eltexBgpAdjRibOutLocalPref':eltexBgpAdjRibOutLocalPref,'eltexBgpAdjRibOutAtomicAggregate':eltexBgpAdjRibOutAtomicAggregate,'eltexBgpAdjRibOutAggregatorAS':eltexBgpAdjRibOutAggregatorAS,'eltexBgpAdjRibOutAggregatorAddr':eltexBgpAdjRibOutAggregatorAddr,'eltexBgpAdjRibOutOrigId':eltexBgpAdjRibOutOrigId,'eltexBgpAdjRibOutEcmp':eltexBgpAdjRibOutEcmp,'eltexBgpAdjRibOutAsLimAs':eltexBgpAdjRibOutAsLimAs,'eltexBgpAdjRibOutAsLimUpper':eltexBgpAdjRibOutAsLimUpper,'eltexBgpAdjRibOutIsActive':eltexBgpAdjRibOutIsActive,'eltexBgpAdjRibOutMEDPrsnt':eltexBgpAdjRibOutMEDPrsnt,'eltexBgpAdjRibOutPeerType':eltexBgpAdjRibOutPeerType,'eltexBgpNetworkTable':eltexBgpNetworkTable,'eltexBgpNetworkEntry':eltexBgpNetworkEntry,_y:eltexBgpNetworkAfi,_z:eltexBgpNetworkSafi,_A0:eltexBgpNetworkPrfxType,_A1:eltexBgpNetworkPrfx,_A2:eltexBgpNetworkPrfxLen,'eltexBgpNetworkRowStatus':eltexBgpNetworkRowStatus,'eltexBgpPathAttrExtensions':eltexBgpPathAttrExtensions,'eltexBgpPathAttrRouteReflectionExts':eltexBgpPathAttrRouteReflectionExts,'eltexBgpPathAttrClusterLocTable':eltexBgpPathAttrClusterLocTable,'eltexBgpPathAttrClusterLocEntry':eltexBgpPathAttrClusterLocEntry,_A5:eltexBgpPathAttrClusterLocIndex,'eltexBgpPathAttrClusterLocValue':eltexBgpPathAttrClusterLocValue})