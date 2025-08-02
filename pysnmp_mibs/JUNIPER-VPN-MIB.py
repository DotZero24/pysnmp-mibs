_Z='jnxVpnRTIndex'
_Y='jnxVpnRTVpnName'
_X='jnxVpnRTVpnType'
_W='static'
_V='jnxVpnName'
_U='jnxVpnType'
_T='2x-4d:2d'
_S='2x-1d.1d.1d.1d:2d'
_R='2x-2d:4d'
_Q='1x:1x:1x:1x:1x:1x:1x:1x'
_P='other'
_O='jnxVpnPwIndex'
_N='jnxVpnPwVpnName'
_M='jnxVpnPwVpnType'
_L='up'
_K='down'
_J='unknown'
_I='jnxVpnIfIndex'
_H='jnxVpnIfVpnName'
_G='jnxVpnIfVpnType'
_F='not-accessible'
_E='accessible-for-notify'
_D='Integer32'
_C='JUNIPER-VPN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
jnxVpnMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,26))
if mibBuilder.loadTexts:jnxVpnMIB.setRevisions(('2010-10-15 00:00','2010-08-27 00:00','2002-04-21 21:28'))
class JnxVpnName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
class JnxVpnType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,1),('bgpIpVpn',2),('bgpL2Vpn',3),('bgpVpls',4),('l2Circuit',5),('ldpVpls',6),('opticalVpn',7),('vpOxc',8),('ccc',9),('bgpAtmVpn',10)))
class JnxVpnIdentifierType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',0),(_P,1),('routeDistinguisher',2),('routeDistinguisher0',3),('routeDistinguisher1',4),('routeDistinguisher2',5),('routeTarget',6),('routeTarget0',7),('routeTarget1',8),('routeTarget2',9),('vcId',10),('localSwitch',11)))
class JnxVpnIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class JnxVpnRouteDistinguisher(TextualConvention,OctetString):status=_A;displayHint=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteDistinguisher0(TextualConvention,OctetString):status=_A;displayHint=_R;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteDistinguisher1(TextualConvention,OctetString):status=_A;displayHint=_S;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteDistinguisher2(TextualConvention,OctetString):status=_A;displayHint=_T;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteTarget(TextualConvention,OctetString):status=_A;displayHint=_Q;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteTarget0(TextualConvention,OctetString):status=_A;displayHint=_T;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteTarget1(TextualConvention,OctetString):status=_A;displayHint=_S;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnRouteTarget2(TextualConvention,OctetString):status=_A;displayHint=_R;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnVCIdentifier(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d.1d:4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class JnxVpnMultiplexor(TextualConvention,Unsigned32):status=_A
class JnxVpnLocalSwitchIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,256))
_JnxVpnMIBNotifications_ObjectIdentity=ObjectIdentity
jnxVpnMIBNotifications=_JnxVpnMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,26,0))
_JnxVpnMibObjects_ObjectIdentity=ObjectIdentity
jnxVpnMibObjects=_JnxVpnMibObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,26,1))
_JnxVpnInfo_ObjectIdentity=ObjectIdentity
jnxVpnInfo=_JnxVpnInfo_ObjectIdentity((1,3,6,1,4,1,2636,3,26,1,1))
_JnxVpnConfiguredVpns_Type=Gauge32
_JnxVpnConfiguredVpns_Object=MibScalar
jnxVpnConfiguredVpns=_JnxVpnConfiguredVpns_Object((1,3,6,1,4,1,2636,3,26,1,1,1),_JnxVpnConfiguredVpns_Type())
jnxVpnConfiguredVpns.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnConfiguredVpns.setStatus(_A)
_JnxVpnActiveVpns_Type=Gauge32
_JnxVpnActiveVpns_Object=MibScalar
jnxVpnActiveVpns=_JnxVpnActiveVpns_Object((1,3,6,1,4,1,2636,3,26,1,1,2),_JnxVpnActiveVpns_Type())
jnxVpnActiveVpns.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnActiveVpns.setStatus(_A)
_JnxVpnNextIfIndex_Type=Unsigned32
_JnxVpnNextIfIndex_Object=MibScalar
jnxVpnNextIfIndex=_JnxVpnNextIfIndex_Object((1,3,6,1,4,1,2636,3,26,1,1,3),_JnxVpnNextIfIndex_Type())
jnxVpnNextIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnNextIfIndex.setStatus(_A)
_JnxVpnNextPwIndex_Type=Unsigned32
_JnxVpnNextPwIndex_Object=MibScalar
jnxVpnNextPwIndex=_JnxVpnNextPwIndex_Object((1,3,6,1,4,1,2636,3,26,1,1,4),_JnxVpnNextPwIndex_Type())
jnxVpnNextPwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnNextPwIndex.setStatus(_A)
_JnxVpnNextRTIndex_Type=Unsigned32
_JnxVpnNextRTIndex_Object=MibScalar
jnxVpnNextRTIndex=_JnxVpnNextRTIndex_Object((1,3,6,1,4,1,2636,3,26,1,1,5),_JnxVpnNextRTIndex_Type())
jnxVpnNextRTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnNextRTIndex.setStatus(_A)
_JnxVpnTable_Object=MibTable
jnxVpnTable=_JnxVpnTable_Object((1,3,6,1,4,1,2636,3,26,1,2))
if mibBuilder.loadTexts:jnxVpnTable.setStatus(_A)
_JnxVpnEntry_Object=MibTableRow
jnxVpnEntry=_JnxVpnEntry_Object((1,3,6,1,4,1,2636,3,26,1,2,1))
jnxVpnEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:jnxVpnEntry.setStatus(_A)
_JnxVpnType_Type=JnxVpnType
_JnxVpnType_Object=MibTableColumn
jnxVpnType=_JnxVpnType_Object((1,3,6,1,4,1,2636,3,26,1,2,1,1),_JnxVpnType_Type())
jnxVpnType.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxVpnType.setStatus(_A)
_JnxVpnName_Type=JnxVpnName
_JnxVpnName_Object=MibTableColumn
jnxVpnName=_JnxVpnName_Object((1,3,6,1,4,1,2636,3,26,1,2,1,2),_JnxVpnName_Type())
jnxVpnName.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxVpnName.setStatus(_A)
_JnxVpnRowStatus_Type=RowStatus
_JnxVpnRowStatus_Object=MibTableColumn
jnxVpnRowStatus=_JnxVpnRowStatus_Object((1,3,6,1,4,1,2636,3,26,1,2,1,3),_JnxVpnRowStatus_Type())
jnxVpnRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRowStatus.setStatus(_A)
_JnxVpnStorageType_Type=StorageType
_JnxVpnStorageType_Object=MibTableColumn
jnxVpnStorageType=_JnxVpnStorageType_Object((1,3,6,1,4,1,2636,3,26,1,2,1,4),_JnxVpnStorageType_Type())
jnxVpnStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnStorageType.setStatus(_A)
_JnxVpnDescription_Type=SnmpAdminString
_JnxVpnDescription_Object=MibTableColumn
jnxVpnDescription=_JnxVpnDescription_Object((1,3,6,1,4,1,2636,3,26,1,2,1,5),_JnxVpnDescription_Type())
jnxVpnDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnDescription.setStatus(_A)
_JnxVpnIdentifierType_Type=JnxVpnIdentifierType
_JnxVpnIdentifierType_Object=MibTableColumn
jnxVpnIdentifierType=_JnxVpnIdentifierType_Object((1,3,6,1,4,1,2636,3,26,1,2,1,6),_JnxVpnIdentifierType_Type())
jnxVpnIdentifierType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIdentifierType.setStatus(_A)
_JnxVpnIdentifier_Type=JnxVpnIdentifier
_JnxVpnIdentifier_Object=MibTableColumn
jnxVpnIdentifier=_JnxVpnIdentifier_Object((1,3,6,1,4,1,2636,3,26,1,2,1,7),_JnxVpnIdentifier_Type())
jnxVpnIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIdentifier.setStatus(_A)
_JnxVpnConfiguredSites_Type=Gauge32
_JnxVpnConfiguredSites_Object=MibTableColumn
jnxVpnConfiguredSites=_JnxVpnConfiguredSites_Object((1,3,6,1,4,1,2636,3,26,1,2,1,8),_JnxVpnConfiguredSites_Type())
jnxVpnConfiguredSites.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnConfiguredSites.setStatus(_A)
_JnxVpnActiveSites_Type=Gauge32
_JnxVpnActiveSites_Object=MibTableColumn
jnxVpnActiveSites=_JnxVpnActiveSites_Object((1,3,6,1,4,1,2636,3,26,1,2,1,9),_JnxVpnActiveSites_Type())
jnxVpnActiveSites.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnActiveSites.setStatus(_A)
_JnxVpnLocalAddresses_Type=Gauge32
_JnxVpnLocalAddresses_Object=MibTableColumn
jnxVpnLocalAddresses=_JnxVpnLocalAddresses_Object((1,3,6,1,4,1,2636,3,26,1,2,1,10),_JnxVpnLocalAddresses_Type())
jnxVpnLocalAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnLocalAddresses.setStatus(_A)
_JnxVpnTotalAddresses_Type=Gauge32
_JnxVpnTotalAddresses_Object=MibTableColumn
jnxVpnTotalAddresses=_JnxVpnTotalAddresses_Object((1,3,6,1,4,1,2636,3,26,1,2,1,11),_JnxVpnTotalAddresses_Type())
jnxVpnTotalAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnTotalAddresses.setStatus(_A)
_JnxVpnAge_Type=TimeTicks
_JnxVpnAge_Object=MibTableColumn
jnxVpnAge=_JnxVpnAge_Object((1,3,6,1,4,1,2636,3,26,1,2,1,12),_JnxVpnAge_Type())
jnxVpnAge.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnAge.setStatus(_A)
_JnxVpnIfTable_Object=MibTable
jnxVpnIfTable=_JnxVpnIfTable_Object((1,3,6,1,4,1,2636,3,26,1,3))
if mibBuilder.loadTexts:jnxVpnIfTable.setStatus(_A)
_JnxVpnIfEntry_Object=MibTableRow
jnxVpnIfEntry=_JnxVpnIfEntry_Object((1,3,6,1,4,1,2636,3,26,1,3,1))
jnxVpnIfEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:jnxVpnIfEntry.setStatus(_A)
_JnxVpnIfVpnType_Type=JnxVpnType
_JnxVpnIfVpnType_Object=MibTableColumn
jnxVpnIfVpnType=_JnxVpnIfVpnType_Object((1,3,6,1,4,1,2636,3,26,1,3,1,1),_JnxVpnIfVpnType_Type())
jnxVpnIfVpnType.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnIfVpnType.setStatus(_A)
_JnxVpnIfVpnName_Type=JnxVpnName
_JnxVpnIfVpnName_Object=MibTableColumn
jnxVpnIfVpnName=_JnxVpnIfVpnName_Object((1,3,6,1,4,1,2636,3,26,1,3,1,2),_JnxVpnIfVpnName_Type())
jnxVpnIfVpnName.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnIfVpnName.setStatus(_A)
_JnxVpnIfIndex_Type=Unsigned32
_JnxVpnIfIndex_Object=MibTableColumn
jnxVpnIfIndex=_JnxVpnIfIndex_Object((1,3,6,1,4,1,2636,3,26,1,3,1,3),_JnxVpnIfIndex_Type())
jnxVpnIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnIfIndex.setStatus(_A)
_JnxVpnIfRowStatus_Type=RowStatus
_JnxVpnIfRowStatus_Object=MibTableColumn
jnxVpnIfRowStatus=_JnxVpnIfRowStatus_Object((1,3,6,1,4,1,2636,3,26,1,3,1,4),_JnxVpnIfRowStatus_Type())
jnxVpnIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfRowStatus.setStatus(_A)
_JnxVpnIfStorageType_Type=StorageType
_JnxVpnIfStorageType_Object=MibTableColumn
jnxVpnIfStorageType=_JnxVpnIfStorageType_Object((1,3,6,1,4,1,2636,3,26,1,3,1,5),_JnxVpnIfStorageType_Type())
jnxVpnIfStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfStorageType.setStatus(_A)
_JnxVpnIfAssociatedPw_Type=Unsigned32
_JnxVpnIfAssociatedPw_Object=MibTableColumn
jnxVpnIfAssociatedPw=_JnxVpnIfAssociatedPw_Object((1,3,6,1,4,1,2636,3,26,1,3,1,6),_JnxVpnIfAssociatedPw_Type())
jnxVpnIfAssociatedPw.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfAssociatedPw.setStatus(_A)
class _JnxVpnIfProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,18,20,21,22,23,24,25,26,129,130)));namedValues=NamedValues(*((_P,0),('frameRelay',1),('atmAal5',2),('atmCell',3),('ethernetVlan',4),('ethernet',5),('ciscoHdlc',6),('ppp',7),('cem',8),('atmVcc',9),('atmVpc',10),('vpls',11),('ipInterworking',12),('snapInterworking',13),('frameRelayPort',15),('satope1',17),('satopt1',18),(_W,20),('rip',21),('ospf',22),('bgp',23),('satope3',24),('satopt3',25),('cesop',26),('atmTrunkNNI',129),('atmTrunkUNI',130)))
_JnxVpnIfProtocol_Type.__name__=_D
_JnxVpnIfProtocol_Object=MibTableColumn
jnxVpnIfProtocol=_JnxVpnIfProtocol_Object((1,3,6,1,4,1,2636,3,26,1,3,1,7),_JnxVpnIfProtocol_Type())
jnxVpnIfProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfProtocol.setStatus(_A)
_JnxVpnIfInBandwidth_Type=Unsigned32
_JnxVpnIfInBandwidth_Object=MibTableColumn
jnxVpnIfInBandwidth=_JnxVpnIfInBandwidth_Object((1,3,6,1,4,1,2636,3,26,1,3,1,8),_JnxVpnIfInBandwidth_Type())
jnxVpnIfInBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfInBandwidth.setStatus(_A)
_JnxVpnIfOutBandwidth_Type=Unsigned32
_JnxVpnIfOutBandwidth_Object=MibTableColumn
jnxVpnIfOutBandwidth=_JnxVpnIfOutBandwidth_Object((1,3,6,1,4,1,2636,3,26,1,3,1,9),_JnxVpnIfOutBandwidth_Type())
jnxVpnIfOutBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfOutBandwidth.setStatus(_A)
class _JnxVpnIfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_J,0),('noLocalInterface',1),('disabled',2),('encapsulationMismatch',3),(_K,4),(_L,5)))
_JnxVpnIfStatus_Type.__name__=_D
_JnxVpnIfStatus_Object=MibTableColumn
jnxVpnIfStatus=_JnxVpnIfStatus_Object((1,3,6,1,4,1,2636,3,26,1,3,1,10),_JnxVpnIfStatus_Type())
jnxVpnIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnIfStatus.setStatus(_A)
_JnxVpnPwTable_Object=MibTable
jnxVpnPwTable=_JnxVpnPwTable_Object((1,3,6,1,4,1,2636,3,26,1,4))
if mibBuilder.loadTexts:jnxVpnPwTable.setStatus(_A)
_JnxVpnPwEntry_Object=MibTableRow
jnxVpnPwEntry=_JnxVpnPwEntry_Object((1,3,6,1,4,1,2636,3,26,1,4,1))
jnxVpnPwEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:jnxVpnPwEntry.setStatus(_A)
_JnxVpnPwVpnType_Type=JnxVpnType
_JnxVpnPwVpnType_Object=MibTableColumn
jnxVpnPwVpnType=_JnxVpnPwVpnType_Object((1,3,6,1,4,1,2636,3,26,1,4,1,1),_JnxVpnPwVpnType_Type())
jnxVpnPwVpnType.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnPwVpnType.setStatus(_A)
_JnxVpnPwVpnName_Type=JnxVpnName
_JnxVpnPwVpnName_Object=MibTableColumn
jnxVpnPwVpnName=_JnxVpnPwVpnName_Object((1,3,6,1,4,1,2636,3,26,1,4,1,2),_JnxVpnPwVpnName_Type())
jnxVpnPwVpnName.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnPwVpnName.setStatus(_A)
_JnxVpnPwIndex_Type=Unsigned32
_JnxVpnPwIndex_Object=MibTableColumn
jnxVpnPwIndex=_JnxVpnPwIndex_Object((1,3,6,1,4,1,2636,3,26,1,4,1,3),_JnxVpnPwIndex_Type())
jnxVpnPwIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxVpnPwIndex.setStatus(_A)
_JnxVpnPwRowStatus_Type=RowStatus
_JnxVpnPwRowStatus_Object=MibTableColumn
jnxVpnPwRowStatus=_JnxVpnPwRowStatus_Object((1,3,6,1,4,1,2636,3,26,1,4,1,4),_JnxVpnPwRowStatus_Type())
jnxVpnPwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwRowStatus.setStatus(_A)
_JnxVpnPwStorageType_Type=StorageType
_JnxVpnPwStorageType_Object=MibTableColumn
jnxVpnPwStorageType=_JnxVpnPwStorageType_Object((1,3,6,1,4,1,2636,3,26,1,4,1,5),_JnxVpnPwStorageType_Type())
jnxVpnPwStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwStorageType.setStatus(_A)
_JnxVpnPwAssociatedInterface_Type=Unsigned32
_JnxVpnPwAssociatedInterface_Object=MibTableColumn
jnxVpnPwAssociatedInterface=_JnxVpnPwAssociatedInterface_Object((1,3,6,1,4,1,2636,3,26,1,4,1,6),_JnxVpnPwAssociatedInterface_Type())
jnxVpnPwAssociatedInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwAssociatedInterface.setStatus(_A)
_JnxVpnPwLocalSiteId_Type=Unsigned32
_JnxVpnPwLocalSiteId_Object=MibTableColumn
jnxVpnPwLocalSiteId=_JnxVpnPwLocalSiteId_Object((1,3,6,1,4,1,2636,3,26,1,4,1,7),_JnxVpnPwLocalSiteId_Type())
jnxVpnPwLocalSiteId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLocalSiteId.setStatus(_A)
_JnxVpnPwRemoteSiteId_Type=Unsigned32
_JnxVpnPwRemoteSiteId_Object=MibTableColumn
jnxVpnPwRemoteSiteId=_JnxVpnPwRemoteSiteId_Object((1,3,6,1,4,1,2636,3,26,1,4,1,8),_JnxVpnPwRemoteSiteId_Type())
jnxVpnPwRemoteSiteId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwRemoteSiteId.setStatus(_A)
_JnxVpnRemotePeIdAddrType_Type=InetAddressType
_JnxVpnRemotePeIdAddrType_Object=MibTableColumn
jnxVpnRemotePeIdAddrType=_JnxVpnRemotePeIdAddrType_Object((1,3,6,1,4,1,2636,3,26,1,4,1,9),_JnxVpnRemotePeIdAddrType_Type())
jnxVpnRemotePeIdAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRemotePeIdAddrType.setStatus(_A)
_JnxVpnRemotePeIdAddress_Type=InetAddress
_JnxVpnRemotePeIdAddress_Object=MibTableColumn
jnxVpnRemotePeIdAddress=_JnxVpnRemotePeIdAddress_Object((1,3,6,1,4,1,2636,3,26,1,4,1,10),_JnxVpnRemotePeIdAddress_Type())
jnxVpnRemotePeIdAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRemotePeIdAddress.setStatus(_A)
class _JnxVpnPwTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,1),('gre',2),('l2tpv3',3),('ipSec',4),('ldp',5),('rsvpTe',6),('crLdp',7)))
_JnxVpnPwTunnelType_Type.__name__=_D
_JnxVpnPwTunnelType_Object=MibTableColumn
jnxVpnPwTunnelType=_JnxVpnPwTunnelType_Object((1,3,6,1,4,1,2636,3,26,1,4,1,11),_JnxVpnPwTunnelType_Type())
jnxVpnPwTunnelType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTunnelType.setStatus(_A)
_JnxVpnPwTunnelName_Type=SnmpAdminString
_JnxVpnPwTunnelName_Object=MibTableColumn
jnxVpnPwTunnelName=_JnxVpnPwTunnelName_Object((1,3,6,1,4,1,2636,3,26,1,4,1,12),_JnxVpnPwTunnelName_Type())
jnxVpnPwTunnelName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTunnelName.setStatus(_A)
_JnxVpnPwReceiveDemux_Type=JnxVpnMultiplexor
_JnxVpnPwReceiveDemux_Object=MibTableColumn
jnxVpnPwReceiveDemux=_JnxVpnPwReceiveDemux_Object((1,3,6,1,4,1,2636,3,26,1,4,1,13),_JnxVpnPwReceiveDemux_Type())
jnxVpnPwReceiveDemux.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwReceiveDemux.setStatus(_A)
_JnxVpnPwTransmitDemux_Type=JnxVpnMultiplexor
_JnxVpnPwTransmitDemux_Object=MibTableColumn
jnxVpnPwTransmitDemux=_JnxVpnPwTransmitDemux_Object((1,3,6,1,4,1,2636,3,26,1,4,1,14),_JnxVpnPwTransmitDemux_Type())
jnxVpnPwTransmitDemux.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTransmitDemux.setStatus(_A)
class _JnxVpnPwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_JnxVpnPwStatus_Type.__name__=_D
_JnxVpnPwStatus_Object=MibTableColumn
jnxVpnPwStatus=_JnxVpnPwStatus_Object((1,3,6,1,4,1,2636,3,26,1,4,1,15),_JnxVpnPwStatus_Type())
jnxVpnPwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwStatus.setStatus(_A)
class _JnxVpnPwTunnelStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),(_K,1),('testing',2),(_L,3)))
_JnxVpnPwTunnelStatus_Type.__name__=_D
_JnxVpnPwTunnelStatus_Object=MibTableColumn
jnxVpnPwTunnelStatus=_JnxVpnPwTunnelStatus_Object((1,3,6,1,4,1,2636,3,26,1,4,1,16),_JnxVpnPwTunnelStatus_Type())
jnxVpnPwTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTunnelStatus.setStatus(_A)
class _JnxVpnPwRemoteSiteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_J,0),('outOfRange',1),(_K,2),(_L,3)))
_JnxVpnPwRemoteSiteStatus_Type.__name__=_D
_JnxVpnPwRemoteSiteStatus_Object=MibTableColumn
jnxVpnPwRemoteSiteStatus=_JnxVpnPwRemoteSiteStatus_Object((1,3,6,1,4,1,2636,3,26,1,4,1,17),_JnxVpnPwRemoteSiteStatus_Type())
jnxVpnPwRemoteSiteStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwRemoteSiteStatus.setStatus(_A)
_JnxVpnPwTimeUp_Type=TimeTicks
_JnxVpnPwTimeUp_Object=MibTableColumn
jnxVpnPwTimeUp=_JnxVpnPwTimeUp_Object((1,3,6,1,4,1,2636,3,26,1,4,1,18),_JnxVpnPwTimeUp_Type())
jnxVpnPwTimeUp.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTimeUp.setStatus(_A)
_JnxVpnPwTransitions_Type=Gauge32
_JnxVpnPwTransitions_Object=MibTableColumn
jnxVpnPwTransitions=_JnxVpnPwTransitions_Object((1,3,6,1,4,1,2636,3,26,1,4,1,19),_JnxVpnPwTransitions_Type())
jnxVpnPwTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwTransitions.setStatus(_A)
_JnxVpnPwLastTransition_Type=TimeTicks
_JnxVpnPwLastTransition_Object=MibTableColumn
jnxVpnPwLastTransition=_JnxVpnPwLastTransition_Object((1,3,6,1,4,1,2636,3,26,1,4,1,20),_JnxVpnPwLastTransition_Type())
jnxVpnPwLastTransition.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLastTransition.setStatus(_A)
_JnxVpnPwPacketsSent_Type=Counter64
_JnxVpnPwPacketsSent_Object=MibTableColumn
jnxVpnPwPacketsSent=_JnxVpnPwPacketsSent_Object((1,3,6,1,4,1,2636,3,26,1,4,1,21),_JnxVpnPwPacketsSent_Type())
jnxVpnPwPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwPacketsSent.setStatus(_A)
_JnxVpnPwOctetsSent_Type=Counter64
_JnxVpnPwOctetsSent_Object=MibTableColumn
jnxVpnPwOctetsSent=_JnxVpnPwOctetsSent_Object((1,3,6,1,4,1,2636,3,26,1,4,1,22),_JnxVpnPwOctetsSent_Type())
jnxVpnPwOctetsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwOctetsSent.setStatus(_A)
_JnxVpnPwPacketsReceived_Type=Counter64
_JnxVpnPwPacketsReceived_Object=MibTableColumn
jnxVpnPwPacketsReceived=_JnxVpnPwPacketsReceived_Object((1,3,6,1,4,1,2636,3,26,1,4,1,23),_JnxVpnPwPacketsReceived_Type())
jnxVpnPwPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwPacketsReceived.setStatus(_A)
_JnxVpnPwOctetsReceived_Type=Counter64
_JnxVpnPwOctetsReceived_Object=MibTableColumn
jnxVpnPwOctetsReceived=_JnxVpnPwOctetsReceived_Object((1,3,6,1,4,1,2636,3,26,1,4,1,24),_JnxVpnPwOctetsReceived_Type())
jnxVpnPwOctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwOctetsReceived.setStatus(_A)
_JnxVpnPwLRPacketsSent_Type=Counter32
_JnxVpnPwLRPacketsSent_Object=MibTableColumn
jnxVpnPwLRPacketsSent=_JnxVpnPwLRPacketsSent_Object((1,3,6,1,4,1,2636,3,26,1,4,1,25),_JnxVpnPwLRPacketsSent_Type())
jnxVpnPwLRPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLRPacketsSent.setStatus(_A)
_JnxVpnPwLROctetsSent_Type=Counter32
_JnxVpnPwLROctetsSent_Object=MibTableColumn
jnxVpnPwLROctetsSent=_JnxVpnPwLROctetsSent_Object((1,3,6,1,4,1,2636,3,26,1,4,1,26),_JnxVpnPwLROctetsSent_Type())
jnxVpnPwLROctetsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLROctetsSent.setStatus(_A)
_JnxVpnPwLRPacketsReceived_Type=Counter32
_JnxVpnPwLRPacketsReceived_Object=MibTableColumn
jnxVpnPwLRPacketsReceived=_JnxVpnPwLRPacketsReceived_Object((1,3,6,1,4,1,2636,3,26,1,4,1,27),_JnxVpnPwLRPacketsReceived_Type())
jnxVpnPwLRPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLRPacketsReceived.setStatus(_A)
_JnxVpnPwLROctetsReceived_Type=Counter32
_JnxVpnPwLROctetsReceived_Object=MibTableColumn
jnxVpnPwLROctetsReceived=_JnxVpnPwLROctetsReceived_Object((1,3,6,1,4,1,2636,3,26,1,4,1,28),_JnxVpnPwLROctetsReceived_Type())
jnxVpnPwLROctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnPwLROctetsReceived.setStatus(_A)
_JnxVpnRTTable_Object=MibTable
jnxVpnRTTable=_JnxVpnRTTable_Object((1,3,6,1,4,1,2636,3,26,1,5))
if mibBuilder.loadTexts:jnxVpnRTTable.setStatus(_A)
_JnxVpnRTEntry_Object=MibTableRow
jnxVpnRTEntry=_JnxVpnRTEntry_Object((1,3,6,1,4,1,2636,3,26,1,5,1))
jnxVpnRTEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:jnxVpnRTEntry.setStatus(_A)
_JnxVpnRTVpnType_Type=JnxVpnType
_JnxVpnRTVpnType_Object=MibTableColumn
jnxVpnRTVpnType=_JnxVpnRTVpnType_Object((1,3,6,1,4,1,2636,3,26,1,5,1,1),_JnxVpnRTVpnType_Type())
jnxVpnRTVpnType.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxVpnRTVpnType.setStatus(_A)
_JnxVpnRTVpnName_Type=JnxVpnName
_JnxVpnRTVpnName_Object=MibTableColumn
jnxVpnRTVpnName=_JnxVpnRTVpnName_Object((1,3,6,1,4,1,2636,3,26,1,5,1,2),_JnxVpnRTVpnName_Type())
jnxVpnRTVpnName.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxVpnRTVpnName.setStatus(_A)
_JnxVpnRTIndex_Type=Unsigned32
_JnxVpnRTIndex_Object=MibTableColumn
jnxVpnRTIndex=_JnxVpnRTIndex_Object((1,3,6,1,4,1,2636,3,26,1,5,1,3),_JnxVpnRTIndex_Type())
jnxVpnRTIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxVpnRTIndex.setStatus(_A)
_JnxVpnRTRowStatus_Type=RowStatus
_JnxVpnRTRowStatus_Object=MibTableColumn
jnxVpnRTRowStatus=_JnxVpnRTRowStatus_Object((1,3,6,1,4,1,2636,3,26,1,5,1,4),_JnxVpnRTRowStatus_Type())
jnxVpnRTRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRTRowStatus.setStatus(_A)
_JnxVpnRTStorageType_Type=StorageType
_JnxVpnRTStorageType_Object=MibTableColumn
jnxVpnRTStorageType=_JnxVpnRTStorageType_Object((1,3,6,1,4,1,2636,3,26,1,5,1,5),_JnxVpnRTStorageType_Type())
jnxVpnRTStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRTStorageType.setStatus(_A)
_JnxVpnRTType_Type=JnxVpnIdentifierType
_JnxVpnRTType_Object=MibTableColumn
jnxVpnRTType=_JnxVpnRTType_Object((1,3,6,1,4,1,2636,3,26,1,5,1,6),_JnxVpnRTType_Type())
jnxVpnRTType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRTType.setStatus(_A)
_JnxVpnRT_Type=JnxVpnIdentifier
_JnxVpnRT_Object=MibTableColumn
jnxVpnRT=_JnxVpnRT_Object((1,3,6,1,4,1,2636,3,26,1,5,1,7),_JnxVpnRT_Type())
jnxVpnRT.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRT.setStatus(_A)
class _JnxVpnRTFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_JnxVpnRTFunction_Type.__name__=_D
_JnxVpnRTFunction_Object=MibTableColumn
jnxVpnRTFunction=_JnxVpnRTFunction_Object((1,3,6,1,4,1,2636,3,26,1,5,1,8),_JnxVpnRTFunction_Type())
jnxVpnRTFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxVpnRTFunction.setStatus(_A)
_JnxVpnMIBConformance_ObjectIdentity=ObjectIdentity
jnxVpnMIBConformance=_JnxVpnMIBConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,26,2))
jnxVpnIfUp=NotificationType((1,3,6,1,4,1,2636,3,26,0,1))
jnxVpnIfUp.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxVpnIfUp.setStatus(_A)
jnxVpnIfDown=NotificationType((1,3,6,1,4,1,2636,3,26,0,2))
jnxVpnIfDown.setObjects(*((_C,_G),(_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxVpnIfDown.setStatus(_A)
jnxVpnPwUp=NotificationType((1,3,6,1,4,1,2636,3,26,0,3))
jnxVpnPwUp.setObjects(*((_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:jnxVpnPwUp.setStatus(_A)
jnxVpnPwDown=NotificationType((1,3,6,1,4,1,2636,3,26,0,4))
jnxVpnPwDown.setObjects(*((_C,_M),(_C,_N),(_C,_O)))
if mibBuilder.loadTexts:jnxVpnPwDown.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'JnxVpnName':JnxVpnName,'JnxVpnType':JnxVpnType,'JnxVpnIdentifierType':JnxVpnIdentifierType,'JnxVpnIdentifier':JnxVpnIdentifier,'JnxVpnRouteDistinguisher':JnxVpnRouteDistinguisher,'JnxVpnRouteDistinguisher0':JnxVpnRouteDistinguisher0,'JnxVpnRouteDistinguisher1':JnxVpnRouteDistinguisher1,'JnxVpnRouteDistinguisher2':JnxVpnRouteDistinguisher2,'JnxVpnRouteTarget':JnxVpnRouteTarget,'JnxVpnRouteTarget0':JnxVpnRouteTarget0,'JnxVpnRouteTarget1':JnxVpnRouteTarget1,'JnxVpnRouteTarget2':JnxVpnRouteTarget2,'JnxVpnVCIdentifier':JnxVpnVCIdentifier,'JnxVpnMultiplexor':JnxVpnMultiplexor,'JnxVpnLocalSwitchIdentifier':JnxVpnLocalSwitchIdentifier,'jnxVpnMIB':jnxVpnMIB,'jnxVpnMIBNotifications':jnxVpnMIBNotifications,'jnxVpnIfUp':jnxVpnIfUp,'jnxVpnIfDown':jnxVpnIfDown,'jnxVpnPwUp':jnxVpnPwUp,'jnxVpnPwDown':jnxVpnPwDown,'jnxVpnMibObjects':jnxVpnMibObjects,'jnxVpnInfo':jnxVpnInfo,'jnxVpnConfiguredVpns':jnxVpnConfiguredVpns,'jnxVpnActiveVpns':jnxVpnActiveVpns,'jnxVpnNextIfIndex':jnxVpnNextIfIndex,'jnxVpnNextPwIndex':jnxVpnNextPwIndex,'jnxVpnNextRTIndex':jnxVpnNextRTIndex,'jnxVpnTable':jnxVpnTable,'jnxVpnEntry':jnxVpnEntry,_U:jnxVpnType,_V:jnxVpnName,'jnxVpnRowStatus':jnxVpnRowStatus,'jnxVpnStorageType':jnxVpnStorageType,'jnxVpnDescription':jnxVpnDescription,'jnxVpnIdentifierType':jnxVpnIdentifierType,'jnxVpnIdentifier':jnxVpnIdentifier,'jnxVpnConfiguredSites':jnxVpnConfiguredSites,'jnxVpnActiveSites':jnxVpnActiveSites,'jnxVpnLocalAddresses':jnxVpnLocalAddresses,'jnxVpnTotalAddresses':jnxVpnTotalAddresses,'jnxVpnAge':jnxVpnAge,'jnxVpnIfTable':jnxVpnIfTable,'jnxVpnIfEntry':jnxVpnIfEntry,_G:jnxVpnIfVpnType,_H:jnxVpnIfVpnName,_I:jnxVpnIfIndex,'jnxVpnIfRowStatus':jnxVpnIfRowStatus,'jnxVpnIfStorageType':jnxVpnIfStorageType,'jnxVpnIfAssociatedPw':jnxVpnIfAssociatedPw,'jnxVpnIfProtocol':jnxVpnIfProtocol,'jnxVpnIfInBandwidth':jnxVpnIfInBandwidth,'jnxVpnIfOutBandwidth':jnxVpnIfOutBandwidth,'jnxVpnIfStatus':jnxVpnIfStatus,'jnxVpnPwTable':jnxVpnPwTable,'jnxVpnPwEntry':jnxVpnPwEntry,_M:jnxVpnPwVpnType,_N:jnxVpnPwVpnName,_O:jnxVpnPwIndex,'jnxVpnPwRowStatus':jnxVpnPwRowStatus,'jnxVpnPwStorageType':jnxVpnPwStorageType,'jnxVpnPwAssociatedInterface':jnxVpnPwAssociatedInterface,'jnxVpnPwLocalSiteId':jnxVpnPwLocalSiteId,'jnxVpnPwRemoteSiteId':jnxVpnPwRemoteSiteId,'jnxVpnRemotePeIdAddrType':jnxVpnRemotePeIdAddrType,'jnxVpnRemotePeIdAddress':jnxVpnRemotePeIdAddress,'jnxVpnPwTunnelType':jnxVpnPwTunnelType,'jnxVpnPwTunnelName':jnxVpnPwTunnelName,'jnxVpnPwReceiveDemux':jnxVpnPwReceiveDemux,'jnxVpnPwTransmitDemux':jnxVpnPwTransmitDemux,'jnxVpnPwStatus':jnxVpnPwStatus,'jnxVpnPwTunnelStatus':jnxVpnPwTunnelStatus,'jnxVpnPwRemoteSiteStatus':jnxVpnPwRemoteSiteStatus,'jnxVpnPwTimeUp':jnxVpnPwTimeUp,'jnxVpnPwTransitions':jnxVpnPwTransitions,'jnxVpnPwLastTransition':jnxVpnPwLastTransition,'jnxVpnPwPacketsSent':jnxVpnPwPacketsSent,'jnxVpnPwOctetsSent':jnxVpnPwOctetsSent,'jnxVpnPwPacketsReceived':jnxVpnPwPacketsReceived,'jnxVpnPwOctetsReceived':jnxVpnPwOctetsReceived,'jnxVpnPwLRPacketsSent':jnxVpnPwLRPacketsSent,'jnxVpnPwLROctetsSent':jnxVpnPwLROctetsSent,'jnxVpnPwLRPacketsReceived':jnxVpnPwLRPacketsReceived,'jnxVpnPwLROctetsReceived':jnxVpnPwLROctetsReceived,'jnxVpnRTTable':jnxVpnRTTable,'jnxVpnRTEntry':jnxVpnRTEntry,_X:jnxVpnRTVpnType,_Y:jnxVpnRTVpnName,_Z:jnxVpnRTIndex,'jnxVpnRTRowStatus':jnxVpnRTRowStatus,'jnxVpnRTStorageType':jnxVpnRTStorageType,'jnxVpnRTType':jnxVpnRTType,'jnxVpnRT':jnxVpnRT,'jnxVpnRTFunction':jnxVpnRTFunction,'jnxVpnMIBConformance':jnxVpnMIBConformance})