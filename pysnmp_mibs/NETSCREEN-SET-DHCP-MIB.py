_F='nsSetDhcpIfIdx'
_E='NETSCREEN-SET-DHCP-MIB'
_D='DisplayString'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
netscreenSetDhcpMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,5))
if mibBuilder.loadTexts:netscreenSetDhcpMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-12-12 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetDHCP_ObjectIdentity=ObjectIdentity
nsSetDHCP=_NsSetDHCP_ObjectIdentity((1,3,6,1,4,1,3224,7,5))
_NsSetDhcpTable_Object=MibTable
nsSetDhcpTable=_NsSetDhcpTable_Object((1,3,6,1,4,1,3224,7,5,1))
if mibBuilder.loadTexts:nsSetDhcpTable.setStatus(_A)
_NsSetDhcpEntry_Object=MibTableRow
nsSetDhcpEntry=_NsSetDhcpEntry_Object((1,3,6,1,4,1,3224,7,5,1,1))
nsSetDhcpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsSetDhcpEntry.setStatus(_A)
class _NsSetDhcpIfIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSetDhcpIfIdx_Type.__name__=_B
_NsSetDhcpIfIdx_Object=MibTableColumn
nsSetDhcpIfIdx=_NsSetDhcpIfIdx_Object((1,3,6,1,4,1,3224,7,5,1,1,1),_NsSetDhcpIfIdx_Type())
nsSetDhcpIfIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSetDhcpIfIdx.setStatus(_A)
class _NsSetDHCPService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('dhcp-relay-agent',1),('dhcp-server',2)))
_NsSetDHCPService_Type.__name__=_B
_NsSetDHCPService_Object=MibTableColumn
nsSetDHCPService=_NsSetDHCPService_Object((1,3,6,1,4,1,3224,7,5,1,1,2),_NsSetDHCPService_Type())
nsSetDHCPService.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSetDHCPService.setStatus(_A)
class _NsSetDHCPRelayServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NsSetDHCPRelayServer_Type.__name__=_D
_NsSetDHCPRelayServer_Object=MibTableColumn
nsSetDHCPRelayServer=_NsSetDHCPRelayServer_Object((1,3,6,1,4,1,3224,7,5,1,1,3),_NsSetDHCPRelayServer_Type())
nsSetDHCPRelayServer.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSetDHCPRelayServer.setStatus(_A)
class _NsSetDHCPVpnEncryp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enabled',1)))
_NsSetDHCPVpnEncryp_Type.__name__=_B
_NsSetDHCPVpnEncryp_Object=MibTableColumn
nsSetDHCPVpnEncryp=_NsSetDHCPVpnEncryp_Object((1,3,6,1,4,1,3224,7,5,1,1,4),_NsSetDHCPVpnEncryp_Type())
nsSetDHCPVpnEncryp.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSetDHCPVpnEncryp.setStatus(_A)
class _NsSetDhcpIfInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSetDhcpIfInfo_Type.__name__=_B
_NsSetDhcpIfInfo_Object=MibTableColumn
nsSetDhcpIfInfo=_NsSetDhcpIfInfo_Object((1,3,6,1,4,1,3224,7,5,1,1,5),_NsSetDhcpIfInfo_Type())
nsSetDhcpIfInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSetDhcpIfInfo.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenSetDhcpMibModule':netscreenSetDhcpMibModule,'nsSetDHCP':nsSetDHCP,'nsSetDhcpTable':nsSetDhcpTable,'nsSetDhcpEntry':nsSetDhcpEntry,_F:nsSetDhcpIfIdx,'nsSetDHCPService':nsSetDHCPService,'nsSetDHCPRelayServer':nsSetDHCPRelayServer,'nsSetDHCPVpnEncryp':nsSetDHCPVpnEncryp,'nsSetDhcpIfInfo':nsSetDhcpIfInfo})