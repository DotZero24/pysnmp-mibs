_A8='ciscoLwappInterfaceNotificationGroup'
_A7='ciscoLwappInterfaceInfoGroup'
_A6='ciscoLwappInterfaceGroupConfigSup1Rev01'
_A5='ciscoLwappInterfaceConfigGroupRev01'
_A4='ciscoLwappInterfaceGroupConfigSup1'
_A3='ciscoLwappInterfaceIpv6AddressStatus'
_A2='ciscoLwappInterfaceAddressChanged'
_A1='clInterfaceGroupFailDetectMode'
_A0='clInterfaceGroupMdnsProfileName'
_z='clInterfaceLinkLocalIpv6AddrStatus'
_y='clInterfaceVpnselectVrfName'
_x='clInterfaceVpnSelectVpnId'
_w='clInterfaceVpnSelectEnabled'
_v='clInterfaceLinkSelectRelaySrcIntf'
_u='clInterfaceLinkSelectEnabled'
_t='clInterfaceIPv6SLAAC'
_s='clInterfaceLinkLocalID'
_r='clInterfaceLinkLocalIDType'
_q='clInterfaceIPv6AclName'
_p='clInterfacePrimaryIPv6Gateway'
_o='clInterfacePrimaryIPv6GatewayType'
_n='clInterfacePrimaryPrefixLen'
_m='clInterfacePrimaryIPv6Addr'
_l='clInterfacePrimaryIPv6AddrType'
_k='clInterfaceMappingRedPort'
_j='clInterfaceNasId'
_i='clInterfaceMdnsProfileName'
_h='clInterfaceDhcpProxyMode'
_g='clInterfaceDhcpOpt82Enabled'
_f='unknown'
_e='reachable'
_d='verify'
_c='incomplete'
_b='tentative'
_a='creating'
_Z='not-accessible'
_Y='OctetString'
_X='ciscoLwappInterfaceConfigGroup'
_W='cLInterfacePreviousAddress'
_V='cLInterfacePreviousAddressType'
_U='clInterfacePrimaryIpv6AddrStatus'
_T='clInterfaceGroupMappingRowStatus'
_S='clInterfaceGroupRowStatus'
_R='clInterfaceGroupIsQuarantine'
_Q='clInterfaceGroupDescr'
_P='clInterfaceQuarantineVlanId'
_O='clInterfaceWired'
_N='clInterfaceGroupName'
_M='Unsigned32'
_L='SnmpAdminString'
_K='cLInterfaceCurrentAddress'
_J='cLInterfaceCurrentAddressType'
_I='deprecated'
_H='read-create'
_G='Integer32'
_F='clInterfaceName'
_E='TruthValue'
_D='read-only'
_C='read-write'
_B='current'
_A='CISCO-LWAPP-INTERFACE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
ciscoLwappInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,686))
if mibBuilder.loadTexts:ciscoLwappInterfaceMIB.setRevisions(('2017-04-27 00:00','2010-08-22 00:00','2009-01-09 00:00'))
_CiscoLwappInterfaceMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceMIBNotifs=_CiscoLwappInterfaceMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,686,0))
_CiscoLwappInterfaceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceMIBObjects=_CiscoLwappInterfaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,686,1))
_CiscoLwappInterfaceConfig_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceConfig=_CiscoLwappInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,686,1,1))
_ClInterfaceConfigTable_Object=MibTable
clInterfaceConfigTable=_ClInterfaceConfigTable_Object((1,3,6,1,4,1,9,9,686,1,1,1))
if mibBuilder.loadTexts:clInterfaceConfigTable.setStatus(_B)
_ClInterfaceConfigEntry_Object=MibTableRow
clInterfaceConfigEntry=_ClInterfaceConfigEntry_Object((1,3,6,1,4,1,9,9,686,1,1,1,1))
clInterfaceConfigEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:clInterfaceConfigEntry.setStatus(_B)
class _ClInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ClInterfaceName_Type.__name__=_Y
_ClInterfaceName_Object=MibTableColumn
clInterfaceName=_ClInterfaceName_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,1),_ClInterfaceName_Type())
clInterfaceName.setMaxAccess(_Z)
if mibBuilder.loadTexts:clInterfaceName.setStatus(_B)
class _ClInterfaceWired_Type(TruthValue):defaultValue=2
_ClInterfaceWired_Type.__name__=_E
_ClInterfaceWired_Object=MibTableColumn
clInterfaceWired=_ClInterfaceWired_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,2),_ClInterfaceWired_Type())
clInterfaceWired.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceWired.setStatus(_B)
class _ClInterfaceQuarantineVlanId_Type(Unsigned32):defaultValue=0
_ClInterfaceQuarantineVlanId_Type.__name__=_M
_ClInterfaceQuarantineVlanId_Object=MibTableColumn
clInterfaceQuarantineVlanId=_ClInterfaceQuarantineVlanId_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,3),_ClInterfaceQuarantineVlanId_Type())
clInterfaceQuarantineVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceQuarantineVlanId.setStatus(_B)
class _ClInterfaceDhcpOpt82Enabled_Type(TruthValue):defaultValue=2
_ClInterfaceDhcpOpt82Enabled_Type.__name__=_E
_ClInterfaceDhcpOpt82Enabled_Object=MibTableColumn
clInterfaceDhcpOpt82Enabled=_ClInterfaceDhcpOpt82Enabled_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,4),_ClInterfaceDhcpOpt82Enabled_Type())
clInterfaceDhcpOpt82Enabled.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceDhcpOpt82Enabled.setStatus(_B)
class _ClInterfaceDhcpProxyMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('global',0),('enabled',1),('disabled',2)))
_ClInterfaceDhcpProxyMode_Type.__name__=_G
_ClInterfaceDhcpProxyMode_Object=MibTableColumn
clInterfaceDhcpProxyMode=_ClInterfaceDhcpProxyMode_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,5),_ClInterfaceDhcpProxyMode_Type())
clInterfaceDhcpProxyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceDhcpProxyMode.setStatus(_B)
_ClInterfaceMdnsProfileName_Type=SnmpAdminString
_ClInterfaceMdnsProfileName_Object=MibTableColumn
clInterfaceMdnsProfileName=_ClInterfaceMdnsProfileName_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,6),_ClInterfaceMdnsProfileName_Type())
clInterfaceMdnsProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceMdnsProfileName.setStatus(_B)
class _ClInterfaceNasId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ClInterfaceNasId_Type.__name__=_L
_ClInterfaceNasId_Object=MibTableColumn
clInterfaceNasId=_ClInterfaceNasId_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,7),_ClInterfaceNasId_Type())
clInterfaceNasId.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceNasId.setStatus(_B)
class _ClInterfaceMappingRedPort_Type(TruthValue):defaultValue=2
_ClInterfaceMappingRedPort_Type.__name__=_E
_ClInterfaceMappingRedPort_Object=MibTableColumn
clInterfaceMappingRedPort=_ClInterfaceMappingRedPort_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,8),_ClInterfaceMappingRedPort_Type())
clInterfaceMappingRedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceMappingRedPort.setStatus(_B)
_ClInterfacePrimaryIPv6AddrType_Type=InetAddressType
_ClInterfacePrimaryIPv6AddrType_Object=MibTableColumn
clInterfacePrimaryIPv6AddrType=_ClInterfacePrimaryIPv6AddrType_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,9),_ClInterfacePrimaryIPv6AddrType_Type())
clInterfacePrimaryIPv6AddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfacePrimaryIPv6AddrType.setStatus(_B)
_ClInterfacePrimaryIPv6Addr_Type=InetAddress
_ClInterfacePrimaryIPv6Addr_Object=MibTableColumn
clInterfacePrimaryIPv6Addr=_ClInterfacePrimaryIPv6Addr_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,10),_ClInterfacePrimaryIPv6Addr_Type())
clInterfacePrimaryIPv6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfacePrimaryIPv6Addr.setStatus(_B)
class _ClInterfacePrimaryPrefixLen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_ClInterfacePrimaryPrefixLen_Type.__name__=_M
_ClInterfacePrimaryPrefixLen_Object=MibTableColumn
clInterfacePrimaryPrefixLen=_ClInterfacePrimaryPrefixLen_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,11),_ClInterfacePrimaryPrefixLen_Type())
clInterfacePrimaryPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfacePrimaryPrefixLen.setStatus(_B)
_ClInterfacePrimaryIPv6GatewayType_Type=InetAddressType
_ClInterfacePrimaryIPv6GatewayType_Object=MibTableColumn
clInterfacePrimaryIPv6GatewayType=_ClInterfacePrimaryIPv6GatewayType_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,12),_ClInterfacePrimaryIPv6GatewayType_Type())
clInterfacePrimaryIPv6GatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfacePrimaryIPv6GatewayType.setStatus(_B)
_ClInterfacePrimaryIPv6Gateway_Type=InetAddress
_ClInterfacePrimaryIPv6Gateway_Object=MibTableColumn
clInterfacePrimaryIPv6Gateway=_ClInterfacePrimaryIPv6Gateway_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,13),_ClInterfacePrimaryIPv6Gateway_Type())
clInterfacePrimaryIPv6Gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfacePrimaryIPv6Gateway.setStatus(_B)
class _ClInterfaceIPv6AclName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ClInterfaceIPv6AclName_Type.__name__=_L
_ClInterfaceIPv6AclName_Object=MibTableColumn
clInterfaceIPv6AclName=_ClInterfaceIPv6AclName_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,14),_ClInterfaceIPv6AclName_Type())
clInterfaceIPv6AclName.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceIPv6AclName.setStatus(_B)
_ClInterfaceLinkLocalIDType_Type=InetAddressType
_ClInterfaceLinkLocalIDType_Object=MibTableColumn
clInterfaceLinkLocalIDType=_ClInterfaceLinkLocalIDType_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,15),_ClInterfaceLinkLocalIDType_Type())
clInterfaceLinkLocalIDType.setMaxAccess(_D)
if mibBuilder.loadTexts:clInterfaceLinkLocalIDType.setStatus(_B)
_ClInterfaceLinkLocalID_Type=InetAddress
_ClInterfaceLinkLocalID_Object=MibTableColumn
clInterfaceLinkLocalID=_ClInterfaceLinkLocalID_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,16),_ClInterfaceLinkLocalID_Type())
clInterfaceLinkLocalID.setMaxAccess(_D)
if mibBuilder.loadTexts:clInterfaceLinkLocalID.setStatus(_B)
class _ClInterfaceIPv6SLAAC_Type(TruthValue):defaultValue=2
_ClInterfaceIPv6SLAAC_Type.__name__=_E
_ClInterfaceIPv6SLAAC_Object=MibTableColumn
clInterfaceIPv6SLAAC=_ClInterfaceIPv6SLAAC_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,17),_ClInterfaceIPv6SLAAC_Type())
clInterfaceIPv6SLAAC.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceIPv6SLAAC.setStatus(_B)
class _ClInterfaceLinkSelectEnabled_Type(TruthValue):defaultValue=2
_ClInterfaceLinkSelectEnabled_Type.__name__=_E
_ClInterfaceLinkSelectEnabled_Object=MibTableColumn
clInterfaceLinkSelectEnabled=_ClInterfaceLinkSelectEnabled_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,18),_ClInterfaceLinkSelectEnabled_Type())
clInterfaceLinkSelectEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceLinkSelectEnabled.setStatus(_B)
_ClInterfaceLinkSelectRelaySrcIntf_Type=SnmpAdminString
_ClInterfaceLinkSelectRelaySrcIntf_Object=MibTableColumn
clInterfaceLinkSelectRelaySrcIntf=_ClInterfaceLinkSelectRelaySrcIntf_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,19),_ClInterfaceLinkSelectRelaySrcIntf_Type())
clInterfaceLinkSelectRelaySrcIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceLinkSelectRelaySrcIntf.setStatus(_B)
class _ClInterfaceVpnSelectEnabled_Type(TruthValue):defaultValue=2
_ClInterfaceVpnSelectEnabled_Type.__name__=_E
_ClInterfaceVpnSelectEnabled_Object=MibTableColumn
clInterfaceVpnSelectEnabled=_ClInterfaceVpnSelectEnabled_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,20),_ClInterfaceVpnSelectEnabled_Type())
clInterfaceVpnSelectEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceVpnSelectEnabled.setStatus(_B)
_ClInterfaceVpnSelectVpnId_Type=SnmpAdminString
_ClInterfaceVpnSelectVpnId_Object=MibTableColumn
clInterfaceVpnSelectVpnId=_ClInterfaceVpnSelectVpnId_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,21),_ClInterfaceVpnSelectVpnId_Type())
clInterfaceVpnSelectVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceVpnSelectVpnId.setStatus(_B)
_ClInterfaceVpnselectVrfName_Type=SnmpAdminString
_ClInterfaceVpnselectVrfName_Object=MibTableColumn
clInterfaceVpnselectVrfName=_ClInterfaceVpnselectVrfName_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,22),_ClInterfaceVpnselectVrfName_Type())
clInterfaceVpnselectVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:clInterfaceVpnselectVrfName.setStatus(_B)
class _ClInterfacePrimaryIpv6AddrStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),('stale',7),('down',8),(_f,9),('dad',10)))
_ClInterfacePrimaryIpv6AddrStatus_Type.__name__=_G
_ClInterfacePrimaryIpv6AddrStatus_Object=MibTableColumn
clInterfacePrimaryIpv6AddrStatus=_ClInterfacePrimaryIpv6AddrStatus_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,23),_ClInterfacePrimaryIpv6AddrStatus_Type())
clInterfacePrimaryIpv6AddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clInterfacePrimaryIpv6AddrStatus.setStatus(_B)
class _ClInterfaceLinkLocalIpv6AddrStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',1),(_a,2),(_b,3),(_c,4),(_d,5),(_e,6),('stale',7),('down',8),(_f,9),('dad',10)))
_ClInterfaceLinkLocalIpv6AddrStatus_Type.__name__=_G
_ClInterfaceLinkLocalIpv6AddrStatus_Object=MibTableColumn
clInterfaceLinkLocalIpv6AddrStatus=_ClInterfaceLinkLocalIpv6AddrStatus_Object((1,3,6,1,4,1,9,9,686,1,1,1,1,24),_ClInterfaceLinkLocalIpv6AddrStatus_Type())
clInterfaceLinkLocalIpv6AddrStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clInterfaceLinkLocalIpv6AddrStatus.setStatus(_B)
_ClInterfaceGroupsConfigTable_Object=MibTable
clInterfaceGroupsConfigTable=_ClInterfaceGroupsConfigTable_Object((1,3,6,1,4,1,9,9,686,1,1,2))
if mibBuilder.loadTexts:clInterfaceGroupsConfigTable.setStatus(_B)
_ClInterfaceGroupsConfigEntry_Object=MibTableRow
clInterfaceGroupsConfigEntry=_ClInterfaceGroupsConfigEntry_Object((1,3,6,1,4,1,9,9,686,1,1,2,1))
clInterfaceGroupsConfigEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:clInterfaceGroupsConfigEntry.setStatus(_B)
_ClInterfaceGroupName_Type=SnmpAdminString
_ClInterfaceGroupName_Object=MibTableColumn
clInterfaceGroupName=_ClInterfaceGroupName_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,1),_ClInterfaceGroupName_Type())
clInterfaceGroupName.setMaxAccess(_Z)
if mibBuilder.loadTexts:clInterfaceGroupName.setStatus(_B)
_ClInterfaceGroupDescr_Type=SnmpAdminString
_ClInterfaceGroupDescr_Object=MibTableColumn
clInterfaceGroupDescr=_ClInterfaceGroupDescr_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,2),_ClInterfaceGroupDescr_Type())
clInterfaceGroupDescr.setMaxAccess(_H)
if mibBuilder.loadTexts:clInterfaceGroupDescr.setStatus(_B)
_ClInterfaceGroupIsQuarantine_Type=TruthValue
_ClInterfaceGroupIsQuarantine_Object=MibTableColumn
clInterfaceGroupIsQuarantine=_ClInterfaceGroupIsQuarantine_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,3),_ClInterfaceGroupIsQuarantine_Type())
clInterfaceGroupIsQuarantine.setMaxAccess(_D)
if mibBuilder.loadTexts:clInterfaceGroupIsQuarantine.setStatus(_B)
_ClInterfaceGroupRowStatus_Type=RowStatus
_ClInterfaceGroupRowStatus_Object=MibTableColumn
clInterfaceGroupRowStatus=_ClInterfaceGroupRowStatus_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,4),_ClInterfaceGroupRowStatus_Type())
clInterfaceGroupRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:clInterfaceGroupRowStatus.setStatus(_B)
_ClInterfaceGroupMdnsProfileName_Type=SnmpAdminString
_ClInterfaceGroupMdnsProfileName_Object=MibTableColumn
clInterfaceGroupMdnsProfileName=_ClInterfaceGroupMdnsProfileName_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,5),_ClInterfaceGroupMdnsProfileName_Type())
clInterfaceGroupMdnsProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:clInterfaceGroupMdnsProfileName.setStatus(_B)
class _ClInterfaceGroupFailDetectMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('aggressive',0),('nonaggressive',1)))
_ClInterfaceGroupFailDetectMode_Type.__name__=_G
_ClInterfaceGroupFailDetectMode_Object=MibTableColumn
clInterfaceGroupFailDetectMode=_ClInterfaceGroupFailDetectMode_Object((1,3,6,1,4,1,9,9,686,1,1,2,1,6),_ClInterfaceGroupFailDetectMode_Type())
clInterfaceGroupFailDetectMode.setMaxAccess(_H)
if mibBuilder.loadTexts:clInterfaceGroupFailDetectMode.setStatus(_B)
_ClInterfaceGroupsMappingTable_Object=MibTable
clInterfaceGroupsMappingTable=_ClInterfaceGroupsMappingTable_Object((1,3,6,1,4,1,9,9,686,1,1,3))
if mibBuilder.loadTexts:clInterfaceGroupsMappingTable.setStatus(_B)
_ClInterfaceGroupsMappingEntry_Object=MibTableRow
clInterfaceGroupsMappingEntry=_ClInterfaceGroupsMappingEntry_Object((1,3,6,1,4,1,9,9,686,1,1,3,1))
clInterfaceGroupsMappingEntry.setIndexNames((0,_A,_N),(0,_A,_F))
if mibBuilder.loadTexts:clInterfaceGroupsMappingEntry.setStatus(_B)
_ClInterfaceGroupMappingRowStatus_Type=RowStatus
_ClInterfaceGroupMappingRowStatus_Object=MibTableColumn
clInterfaceGroupMappingRowStatus=_ClInterfaceGroupMappingRowStatus_Object((1,3,6,1,4,1,9,9,686,1,1,3,1,1),_ClInterfaceGroupMappingRowStatus_Type())
clInterfaceGroupMappingRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:clInterfaceGroupMappingRowStatus.setStatus(_B)
_CiscoLwappInterfaceInfo_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceInfo=_CiscoLwappInterfaceInfo_ObjectIdentity((1,3,6,1,4,1,9,9,686,1,2))
_CLInterfaceTable_Object=MibTable
cLInterfaceTable=_CLInterfaceTable_Object((1,3,6,1,4,1,9,9,686,1,2,1))
if mibBuilder.loadTexts:cLInterfaceTable.setStatus(_B)
_CLInterfaceEntry_Object=MibTableRow
cLInterfaceEntry=_CLInterfaceEntry_Object((1,3,6,1,4,1,9,9,686,1,2,1,1))
cLInterfaceEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cLInterfaceEntry.setStatus(_B)
_CLInterfacePreviousAddressType_Type=InetAddressType
_CLInterfacePreviousAddressType_Object=MibTableColumn
cLInterfacePreviousAddressType=_CLInterfacePreviousAddressType_Object((1,3,6,1,4,1,9,9,686,1,2,1,1,1),_CLInterfacePreviousAddressType_Type())
cLInterfacePreviousAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLInterfacePreviousAddressType.setStatus(_B)
_CLInterfacePreviousAddress_Type=InetAddress
_CLInterfacePreviousAddress_Object=MibTableColumn
cLInterfacePreviousAddress=_CLInterfacePreviousAddress_Object((1,3,6,1,4,1,9,9,686,1,2,1,1,2),_CLInterfacePreviousAddress_Type())
cLInterfacePreviousAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cLInterfacePreviousAddress.setStatus(_B)
_CLInterfaceCurrentAddressType_Type=InetAddressType
_CLInterfaceCurrentAddressType_Object=MibTableColumn
cLInterfaceCurrentAddressType=_CLInterfaceCurrentAddressType_Object((1,3,6,1,4,1,9,9,686,1,2,1,1,3),_CLInterfaceCurrentAddressType_Type())
cLInterfaceCurrentAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cLInterfaceCurrentAddressType.setStatus(_B)
_CLInterfaceCurrentAddress_Type=InetAddress
_CLInterfaceCurrentAddress_Object=MibTableColumn
cLInterfaceCurrentAddress=_CLInterfaceCurrentAddress_Object((1,3,6,1,4,1,9,9,686,1,2,1,1,4),_CLInterfaceCurrentAddress_Type())
cLInterfaceCurrentAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cLInterfaceCurrentAddress.setStatus(_B)
_CiscoLwappInterfaceMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceMIBConform=_CiscoLwappInterfaceMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,686,2))
_CiscoLwappInterfaceMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceMIBCompliances=_CiscoLwappInterfaceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,686,2,1))
_CiscoLwappInterfaceMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappInterfaceMIBGroups=_CiscoLwappInterfaceMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,686,2,2))
ciscoLwappInterfaceConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,686,2,2,1))
ciscoLwappInterfaceConfigGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoLwappInterfaceConfigGroup.setStatus(_I)
ciscoLwappInterfaceGroupConfigSup1=ObjectGroup((1,3,6,1,4,1,9,9,686,2,2,2))
ciscoLwappInterfaceGroupConfigSup1.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:ciscoLwappInterfaceGroupConfigSup1.setStatus(_I)
ciscoLwappInterfaceConfigGroupRev01=ObjectGroup((1,3,6,1,4,1,9,9,686,2,2,3))
ciscoLwappInterfaceConfigGroupRev01.setObjects(*((_A,_O),(_A,_P),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_U),(_A,_z)))
if mibBuilder.loadTexts:ciscoLwappInterfaceConfigGroupRev01.setStatus(_B)
ciscoLwappInterfaceGroupConfigSup1Rev01=ObjectGroup((1,3,6,1,4,1,9,9,686,2,2,4))
ciscoLwappInterfaceGroupConfigSup1Rev01.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:ciscoLwappInterfaceGroupConfigSup1Rev01.setStatus(_B)
ciscoLwappInterfaceInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,686,2,2,5))
ciscoLwappInterfaceInfoGroup.setObjects(*((_A,_V),(_A,_W),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoLwappInterfaceInfoGroup.setStatus(_B)
ciscoLwappInterfaceAddressChanged=NotificationType((1,3,6,1,4,1,9,9,686,0,1))
ciscoLwappInterfaceAddressChanged.setObjects(*((_A,_F),(_A,_V),(_A,_W),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoLwappInterfaceAddressChanged.setStatus(_B)
ciscoLwappInterfaceIpv6AddressStatus=NotificationType((1,3,6,1,4,1,9,9,686,0,2))
ciscoLwappInterfaceIpv6AddressStatus.setObjects(*((_A,_F),(_A,_U),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ciscoLwappInterfaceIpv6AddressStatus.setStatus(_B)
ciscoLwappInterfaceNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,686,2,2,6))
ciscoLwappInterfaceNotificationGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:ciscoLwappInterfaceNotificationGroup.setStatus(_B)
ciscoLwappInterfaceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,686,2,1,1))
ciscoLwappInterfaceMIBCompliance.setObjects((_A,_X))
if mibBuilder.loadTexts:ciscoLwappInterfaceMIBCompliance.setStatus(_I)
ciscoLwappInterfaceMIBComplianceRev01=ModuleCompliance((1,3,6,1,4,1,9,9,686,2,1,2))
ciscoLwappInterfaceMIBComplianceRev01.setObjects(*((_A,_X),(_A,_A4)))
if mibBuilder.loadTexts:ciscoLwappInterfaceMIBComplianceRev01.setStatus(_I)
ciscoLwappInterfaceMIBComplianceRev02=ModuleCompliance((1,3,6,1,4,1,9,9,686,2,1,3))
ciscoLwappInterfaceMIBComplianceRev02.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoLwappInterfaceMIBComplianceRev02.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoLwappInterfaceMIB':ciscoLwappInterfaceMIB,'ciscoLwappInterfaceMIBNotifs':ciscoLwappInterfaceMIBNotifs,_A2:ciscoLwappInterfaceAddressChanged,_A3:ciscoLwappInterfaceIpv6AddressStatus,'ciscoLwappInterfaceMIBObjects':ciscoLwappInterfaceMIBObjects,'ciscoLwappInterfaceConfig':ciscoLwappInterfaceConfig,'clInterfaceConfigTable':clInterfaceConfigTable,'clInterfaceConfigEntry':clInterfaceConfigEntry,_F:clInterfaceName,_O:clInterfaceWired,_P:clInterfaceQuarantineVlanId,_g:clInterfaceDhcpOpt82Enabled,_h:clInterfaceDhcpProxyMode,_i:clInterfaceMdnsProfileName,_j:clInterfaceNasId,_k:clInterfaceMappingRedPort,_l:clInterfacePrimaryIPv6AddrType,_m:clInterfacePrimaryIPv6Addr,_n:clInterfacePrimaryPrefixLen,_o:clInterfacePrimaryIPv6GatewayType,_p:clInterfacePrimaryIPv6Gateway,_q:clInterfaceIPv6AclName,_r:clInterfaceLinkLocalIDType,_s:clInterfaceLinkLocalID,_t:clInterfaceIPv6SLAAC,_u:clInterfaceLinkSelectEnabled,_v:clInterfaceLinkSelectRelaySrcIntf,_w:clInterfaceVpnSelectEnabled,_x:clInterfaceVpnSelectVpnId,_y:clInterfaceVpnselectVrfName,_U:clInterfacePrimaryIpv6AddrStatus,_z:clInterfaceLinkLocalIpv6AddrStatus,'clInterfaceGroupsConfigTable':clInterfaceGroupsConfigTable,'clInterfaceGroupsConfigEntry':clInterfaceGroupsConfigEntry,_N:clInterfaceGroupName,_Q:clInterfaceGroupDescr,_R:clInterfaceGroupIsQuarantine,_S:clInterfaceGroupRowStatus,_A0:clInterfaceGroupMdnsProfileName,_A1:clInterfaceGroupFailDetectMode,'clInterfaceGroupsMappingTable':clInterfaceGroupsMappingTable,'clInterfaceGroupsMappingEntry':clInterfaceGroupsMappingEntry,_T:clInterfaceGroupMappingRowStatus,'ciscoLwappInterfaceInfo':ciscoLwappInterfaceInfo,'cLInterfaceTable':cLInterfaceTable,'cLInterfaceEntry':cLInterfaceEntry,_V:cLInterfacePreviousAddressType,_W:cLInterfacePreviousAddress,_J:cLInterfaceCurrentAddressType,_K:cLInterfaceCurrentAddress,'ciscoLwappInterfaceMIBConform':ciscoLwappInterfaceMIBConform,'ciscoLwappInterfaceMIBCompliances':ciscoLwappInterfaceMIBCompliances,'ciscoLwappInterfaceMIBCompliance':ciscoLwappInterfaceMIBCompliance,'ciscoLwappInterfaceMIBComplianceRev01':ciscoLwappInterfaceMIBComplianceRev01,'ciscoLwappInterfaceMIBComplianceRev02':ciscoLwappInterfaceMIBComplianceRev02,'ciscoLwappInterfaceMIBGroups':ciscoLwappInterfaceMIBGroups,_X:ciscoLwappInterfaceConfigGroup,_A4:ciscoLwappInterfaceGroupConfigSup1,_A5:ciscoLwappInterfaceConfigGroupRev01,_A6:ciscoLwappInterfaceGroupConfigSup1Rev01,_A7:ciscoLwappInterfaceInfoGroup,_A8:ciscoLwappInterfaceNotificationGroup})