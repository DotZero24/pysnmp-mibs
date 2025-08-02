_Z='ruckusWiredClientGroup'
_Y='ruckusDhcpClientModelName'
_X='ruckusDhcpClientOsVendorName'
_W='ruckusDhcpClientDeviceTypeName'
_V='ruckusDhcpClientHostName'
_U='ruckusWiredClientRxOctets'
_T='ruckusWiredClientTxOctets'
_S='ruckusWiredClientRxPkts'
_R='ruckusWiredClientTxPkts'
_Q='ruckusWiredClientUpTime'
_P='ruckusWiredClientV6Addr'
_O='ruckusWiredClientV4Addr'
_N='ruckusWiredClientUserName'
_M='ruckusWiredClientDescr'
_L='ruckusWiredClientStatus'
_K='ruckusWiredClientAuthType'
_J='ruckusWiredClientType'
_I='ruckusWiredClientVlan'
_H='DisplayString'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='ruckusWiredClientMac'
_C='read-only'
_B='RUCKUS-WIRED-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayString,=mibBuilder.importSymbols('FOUNDRY-SN-AGENT-MIB',_H)
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressIPv6')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','TextualConvention','TruthValue')
ruckusWiredClientMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,43))
if mibBuilder.loadTexts:ruckusWiredClientMIB.setRevisions(('2019-02-28 00:00','2023-05-24 00:00'))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RuckusWiredClientNotify_ObjectIdentity=ObjectIdentity
ruckusWiredClientNotify=_RuckusWiredClientNotify_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,0))
_RuckusWiredClientObjects_ObjectIdentity=ObjectIdentity
ruckusWiredClientObjects=_RuckusWiredClientObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,1))
_RuckusWiredClients_ObjectIdentity=ObjectIdentity
ruckusWiredClients=_RuckusWiredClients_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,1,1))
_RuckusWiredClientsTable_Object=MibTable
ruckusWiredClientsTable=_RuckusWiredClientsTable_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1))
if mibBuilder.loadTexts:ruckusWiredClientsTable.setStatus(_A)
_RuckusWiredClientEntry_Object=MibTableRow
ruckusWiredClientEntry=_RuckusWiredClientEntry_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1))
ruckusWiredClientEntry.setIndexNames((0,_E,_F),(0,_B,_D))
if mibBuilder.loadTexts:ruckusWiredClientEntry.setStatus(_A)
_RuckusWiredClientMac_Type=MacAddress
_RuckusWiredClientMac_Object=MibTableColumn
ruckusWiredClientMac=_RuckusWiredClientMac_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,1),_RuckusWiredClientMac_Type())
ruckusWiredClientMac.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientMac.setStatus(_A)
_RuckusWiredClientVlan_Type=VlanId
_RuckusWiredClientVlan_Object=MibTableColumn
ruckusWiredClientVlan=_RuckusWiredClientVlan_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,2),_RuckusWiredClientVlan_Type())
ruckusWiredClientVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientVlan.setStatus(_A)
class _RuckusWiredClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('phone',2),('wlanAP',3),('router',4),('bridge',5),('cableDevice',6)))
_RuckusWiredClientType_Type.__name__=_G
_RuckusWiredClientType_Object=MibTableColumn
ruckusWiredClientType=_RuckusWiredClientType_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,3),_RuckusWiredClientType_Type())
ruckusWiredClientType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientType.setStatus(_A)
class _RuckusWiredClientAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('dot1x',2),('macAuth',3),('webAuth',4)))
_RuckusWiredClientAuthType_Type.__name__=_G
_RuckusWiredClientAuthType_Object=MibTableColumn
ruckusWiredClientAuthType=_RuckusWiredClientAuthType_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,4),_RuckusWiredClientAuthType_Type())
ruckusWiredClientAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientAuthType.setStatus(_A)
class _RuckusWiredClientStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noAuth',1),('allowed',2),('blocked',3),('restricted',4),('critical',5),('guest',6)))
_RuckusWiredClientStatus_Type.__name__=_G
_RuckusWiredClientStatus_Object=MibTableColumn
ruckusWiredClientStatus=_RuckusWiredClientStatus_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,5),_RuckusWiredClientStatus_Type())
ruckusWiredClientStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientStatus.setStatus(_A)
_RuckusWiredClientDescr_Type=SnmpAdminString
_RuckusWiredClientDescr_Object=MibTableColumn
ruckusWiredClientDescr=_RuckusWiredClientDescr_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,6),_RuckusWiredClientDescr_Type())
ruckusWiredClientDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientDescr.setStatus(_A)
_RuckusWiredClientUserName_Type=SnmpAdminString
_RuckusWiredClientUserName_Object=MibTableColumn
ruckusWiredClientUserName=_RuckusWiredClientUserName_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,7),_RuckusWiredClientUserName_Type())
ruckusWiredClientUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientUserName.setStatus(_A)
_RuckusWiredClientV4Addr_Type=InetAddressIPv4
_RuckusWiredClientV4Addr_Object=MibTableColumn
ruckusWiredClientV4Addr=_RuckusWiredClientV4Addr_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,8),_RuckusWiredClientV4Addr_Type())
ruckusWiredClientV4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientV4Addr.setStatus(_A)
_RuckusWiredClientV6Addr_Type=InetAddressIPv6
_RuckusWiredClientV6Addr_Object=MibTableColumn
ruckusWiredClientV6Addr=_RuckusWiredClientV6Addr_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,9),_RuckusWiredClientV6Addr_Type())
ruckusWiredClientV6Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientV6Addr.setStatus(_A)
_RuckusWiredClientUpTime_Type=TimeTicks
_RuckusWiredClientUpTime_Object=MibTableColumn
ruckusWiredClientUpTime=_RuckusWiredClientUpTime_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,10),_RuckusWiredClientUpTime_Type())
ruckusWiredClientUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientUpTime.setStatus(_A)
if mibBuilder.loadTexts:ruckusWiredClientUpTime.setUnits('centi-seconds')
_RuckusWiredClientTxPkts_Type=Counter64
_RuckusWiredClientTxPkts_Object=MibTableColumn
ruckusWiredClientTxPkts=_RuckusWiredClientTxPkts_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,11),_RuckusWiredClientTxPkts_Type())
ruckusWiredClientTxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientTxPkts.setStatus(_A)
_RuckusWiredClientRxPkts_Type=Counter64
_RuckusWiredClientRxPkts_Object=MibTableColumn
ruckusWiredClientRxPkts=_RuckusWiredClientRxPkts_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,12),_RuckusWiredClientRxPkts_Type())
ruckusWiredClientRxPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientRxPkts.setStatus(_A)
_RuckusWiredClientTxOctets_Type=Counter64
_RuckusWiredClientTxOctets_Object=MibTableColumn
ruckusWiredClientTxOctets=_RuckusWiredClientTxOctets_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,13),_RuckusWiredClientTxOctets_Type())
ruckusWiredClientTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientTxOctets.setStatus(_A)
_RuckusWiredClientRxOctets_Type=Counter64
_RuckusWiredClientRxOctets_Object=MibTableColumn
ruckusWiredClientRxOctets=_RuckusWiredClientRxOctets_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,14),_RuckusWiredClientRxOctets_Type())
ruckusWiredClientRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusWiredClientRxOctets.setStatus(_A)
_RuckusDhcpClientHostName_Type=SnmpAdminString
_RuckusDhcpClientHostName_Object=MibTableColumn
ruckusDhcpClientHostName=_RuckusDhcpClientHostName_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,15),_RuckusDhcpClientHostName_Type())
ruckusDhcpClientHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpClientHostName.setStatus(_A)
_RuckusDhcpClientDeviceTypeName_Type=SnmpAdminString
_RuckusDhcpClientDeviceTypeName_Object=MibTableColumn
ruckusDhcpClientDeviceTypeName=_RuckusDhcpClientDeviceTypeName_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,16),_RuckusDhcpClientDeviceTypeName_Type())
ruckusDhcpClientDeviceTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpClientDeviceTypeName.setStatus(_A)
_RuckusDhcpClientOsVendorName_Type=SnmpAdminString
_RuckusDhcpClientOsVendorName_Object=MibTableColumn
ruckusDhcpClientOsVendorName=_RuckusDhcpClientOsVendorName_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,17),_RuckusDhcpClientOsVendorName_Type())
ruckusDhcpClientOsVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpClientOsVendorName.setStatus(_A)
_RuckusDhcpClientModelName_Type=SnmpAdminString
_RuckusDhcpClientModelName_Object=MibTableColumn
ruckusDhcpClientModelName=_RuckusDhcpClientModelName_Object((1,3,6,1,4,1,1991,1,1,3,43,1,1,1,1,18),_RuckusDhcpClientModelName_Type())
ruckusDhcpClientModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusDhcpClientModelName.setStatus(_A)
_RuckusWiredClientConformance_ObjectIdentity=ObjectIdentity
ruckusWiredClientConformance=_RuckusWiredClientConformance_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,2))
_RuckusWiredClientMIBCompliances_ObjectIdentity=ObjectIdentity
ruckusWiredClientMIBCompliances=_RuckusWiredClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,2,1))
_RuckusWiredClientMIBGroups_ObjectIdentity=ObjectIdentity
ruckusWiredClientMIBGroups=_RuckusWiredClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,43,2,2))
ruckusWiredClientGroup=ObjectGroup((1,3,6,1,4,1,1991,1,1,3,43,2,2,1))
ruckusWiredClientGroup.setObjects(*((_B,_D),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:ruckusWiredClientGroup.setStatus(_A)
ruckusWiredClientConnectedNotify=NotificationType((1,3,6,1,4,1,1991,1,1,3,43,0,1))
ruckusWiredClientConnectedNotify.setObjects(*((_E,_F),(_B,_D)))
if mibBuilder.loadTexts:ruckusWiredClientConnectedNotify.setStatus(_A)
ruckusWiredClientDisconnectedNotify=NotificationType((1,3,6,1,4,1,1991,1,1,3,43,0,2))
ruckusWiredClientDisconnectedNotify.setObjects(*((_E,_F),(_B,_D)))
if mibBuilder.loadTexts:ruckusWiredClientDisconnectedNotify.setStatus(_A)
ruckusWiredClientCompliance=ModuleCompliance((1,3,6,1,4,1,1991,1,1,3,43,2,1,1))
ruckusWiredClientCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:ruckusWiredClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanId':VlanId,'ruckusWiredClientMIB':ruckusWiredClientMIB,'ruckusWiredClientNotify':ruckusWiredClientNotify,'ruckusWiredClientConnectedNotify':ruckusWiredClientConnectedNotify,'ruckusWiredClientDisconnectedNotify':ruckusWiredClientDisconnectedNotify,'ruckusWiredClientObjects':ruckusWiredClientObjects,'ruckusWiredClients':ruckusWiredClients,'ruckusWiredClientsTable':ruckusWiredClientsTable,'ruckusWiredClientEntry':ruckusWiredClientEntry,_D:ruckusWiredClientMac,_I:ruckusWiredClientVlan,_J:ruckusWiredClientType,_K:ruckusWiredClientAuthType,_L:ruckusWiredClientStatus,_M:ruckusWiredClientDescr,_N:ruckusWiredClientUserName,_O:ruckusWiredClientV4Addr,_P:ruckusWiredClientV6Addr,_Q:ruckusWiredClientUpTime,_R:ruckusWiredClientTxPkts,_S:ruckusWiredClientRxPkts,_T:ruckusWiredClientTxOctets,_U:ruckusWiredClientRxOctets,_V:ruckusDhcpClientHostName,_W:ruckusDhcpClientDeviceTypeName,_X:ruckusDhcpClientOsVendorName,_Y:ruckusDhcpClientModelName,'ruckusWiredClientConformance':ruckusWiredClientConformance,'ruckusWiredClientMIBCompliances':ruckusWiredClientMIBCompliances,'ruckusWiredClientCompliance':ruckusWiredClientCompliance,'ruckusWiredClientMIBGroups':ruckusWiredClientMIBGroups,_Z:ruckusWiredClientGroup})