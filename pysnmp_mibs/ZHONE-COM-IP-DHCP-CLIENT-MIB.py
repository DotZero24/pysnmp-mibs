_Q='dhcpInterfacesEntry'
_P='routersIpAddress'
_O='dnsIpAddress'
_N='zhoneSlotIndex'
_M='zhoneShelfIndex'
_L='Integer32'
_K='SnmpAdminString'
_J='Zhone'
_I='ifIndex'
_H='IF-MIB'
_G='OctetString'
_F='ZHONE-COM-IP-DHCP-CLIENT-MIB'
_E='Unsigned32'
_D='read-write'
_C='seconds'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipInterfaceEntry,=mibBuilder.importSymbols('ZHONE-COM-IP-REC-MIB','ipInterfaceEntry')
zhoneIp,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_J,'zhoneIp','zhoneModules',_M,_N)
ZhoneAdminString,=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString')
comIpDhcpClient=ModuleIdentity((1,3,6,1,4,1,5504,6,51))
if mibBuilder.loadTexts:comIpDhcpClient.setRevisions(('2001-06-28 11:14','2000-09-28 17:00','2000-09-11 15:01'))
_DhcpClient_ObjectIdentity=ObjectIdentity
dhcpClient=_DhcpClient_ObjectIdentity((1,3,6,1,4,1,5504,4,1,1))
if mibBuilder.loadTexts:dhcpClient.setStatus(_A)
_DhcpClientResourceTable_Object=MibTable
dhcpClientResourceTable=_DhcpClientResourceTable_Object((1,3,6,1,4,1,5504,4,1,1,1))
if mibBuilder.loadTexts:dhcpClientResourceTable.setStatus(_A)
_DhcpClientResourceEntry_Object=MibTableRow
dhcpClientResourceEntry=_DhcpClientResourceEntry_Object((1,3,6,1,4,1,5504,4,1,1,1,1))
dhcpClientResourceEntry.setIndexNames((0,_J,_M),(0,_J,_N))
if mibBuilder.loadTexts:dhcpClientResourceEntry.setStatus(_A)
class _DhcpOfferTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DhcpOfferTimeout_Type.__name__=_E
_DhcpOfferTimeout_Object=MibTableColumn
dhcpOfferTimeout=_DhcpOfferTimeout_Object((1,3,6,1,4,1,5504,4,1,1,1,1,1),_DhcpOfferTimeout_Type())
dhcpOfferTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpOfferTimeout.setStatus(_A)
if mibBuilder.loadTexts:dhcpOfferTimeout.setUnits(_C)
class _DhcpDefaultLease_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,604800))
_DhcpDefaultLease_Type.__name__=_E
_DhcpDefaultLease_Object=MibTableColumn
dhcpDefaultLease=_DhcpDefaultLease_Object((1,3,6,1,4,1,5504,4,1,1,1,1,2),_DhcpDefaultLease_Type())
dhcpDefaultLease.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpDefaultLease.setStatus(_A)
if mibBuilder.loadTexts:dhcpDefaultLease.setUnits(_C)
class _DhcpMinLease_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_DhcpMinLease_Type.__name__=_E
_DhcpMinLease_Object=MibTableColumn
dhcpMinLease=_DhcpMinLease_Object((1,3,6,1,4,1,5504,4,1,1,1,1,3),_DhcpMinLease_Type())
dhcpMinLease.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpMinLease.setStatus(_A)
if mibBuilder.loadTexts:dhcpMinLease.setUnits(_C)
_DhcpClientErrors_Type=Counter32
_DhcpClientErrors_Object=MibTableColumn
dhcpClientErrors=_DhcpClientErrors_Object((1,3,6,1,4,1,5504,4,1,1,1,1,4),_DhcpClientErrors_Type())
dhcpClientErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientErrors.setStatus(_A)
_DhcpAvgTimeForLease_Type=Gauge32
_DhcpAvgTimeForLease_Object=MibTableColumn
dhcpAvgTimeForLease=_DhcpAvgTimeForLease_Object((1,3,6,1,4,1,5504,4,1,1,1,1,5),_DhcpAvgTimeForLease_Type())
dhcpAvgTimeForLease.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpAvgTimeForLease.setStatus(_A)
if mibBuilder.loadTexts:dhcpAvgTimeForLease.setUnits(_C)
_DhcpInterfacesTable_Object=MibTable
dhcpInterfacesTable=_DhcpInterfacesTable_Object((1,3,6,1,4,1,5504,4,1,1,2))
if mibBuilder.loadTexts:dhcpInterfacesTable.setStatus(_A)
_DhcpInterfacesEntry_Object=MibTableRow
dhcpInterfacesEntry=_DhcpInterfacesEntry_Object((1,3,6,1,4,1,5504,4,1,1,2,1))
if mibBuilder.loadTexts:dhcpInterfacesEntry.setStatus(_A)
_DhcpInterfaceServerName_Type=SnmpAdminString
_DhcpInterfaceServerName_Object=MibTableColumn
dhcpInterfaceServerName=_DhcpInterfaceServerName_Object((1,3,6,1,4,1,5504,4,1,1,2,1,1),_DhcpInterfaceServerName_Type())
dhcpInterfaceServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceServerName.setStatus(_A)
_DhcpInterfaceRenew_Type=Unsigned32
_DhcpInterfaceRenew_Object=MibTableColumn
dhcpInterfaceRenew=_DhcpInterfaceRenew_Object((1,3,6,1,4,1,5504,4,1,1,2,1,2),_DhcpInterfaceRenew_Type())
dhcpInterfaceRenew.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceRenew.setStatus(_A)
if mibBuilder.loadTexts:dhcpInterfaceRenew.setUnits(_C)
_DhcpInterfaceRebind_Type=Unsigned32
_DhcpInterfaceRebind_Object=MibTableColumn
dhcpInterfaceRebind=_DhcpInterfaceRebind_Object((1,3,6,1,4,1,5504,4,1,1,2,1,3),_DhcpInterfaceRebind_Type())
dhcpInterfaceRebind.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceRebind.setStatus(_A)
if mibBuilder.loadTexts:dhcpInterfaceRebind.setUnits(_C)
class _DhcpInterfaceBootFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DhcpInterfaceBootFile_Type.__name__=_K
_DhcpInterfaceBootFile_Object=MibTableColumn
dhcpInterfaceBootFile=_DhcpInterfaceBootFile_Object((1,3,6,1,4,1,5504,4,1,1,2,1,4),_DhcpInterfaceBootFile_Type())
dhcpInterfaceBootFile.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceBootFile.setStatus(_A)
_DhcpInterfaceTftp_Type=IpAddress
_DhcpInterfaceTftp_Object=MibTableColumn
dhcpInterfaceTftp=_DhcpInterfaceTftp_Object((1,3,6,1,4,1,5504,4,1,1,2,1,5),_DhcpInterfaceTftp_Type())
dhcpInterfaceTftp.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceTftp.setStatus(_A)
_DhcpInterfaceHostname_Type=ZhoneAdminString
_DhcpInterfaceHostname_Object=MibTableColumn
dhcpInterfaceHostname=_DhcpInterfaceHostname_Object((1,3,6,1,4,1,5504,4,1,1,2,1,6),_DhcpInterfaceHostname_Type())
dhcpInterfaceHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceHostname.setStatus(_A)
_DhcpInterfaceDomainName_Type=SnmpAdminString
_DhcpInterfaceDomainName_Object=MibTableColumn
dhcpInterfaceDomainName=_DhcpInterfaceDomainName_Object((1,3,6,1,4,1,5504,4,1,1,2,1,7),_DhcpInterfaceDomainName_Type())
dhcpInterfaceDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceDomainName.setStatus(_A)
class _DhcpInterfaceVendorClassId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DhcpInterfaceVendorClassId_Type.__name__=_G
_DhcpInterfaceVendorClassId_Object=MibTableColumn
dhcpInterfaceVendorClassId=_DhcpInterfaceVendorClassId_Object((1,3,6,1,4,1,5504,4,1,1,2,1,8),_DhcpInterfaceVendorClassId_Type())
dhcpInterfaceVendorClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpInterfaceVendorClassId.setStatus(_A)
class _DhcpInterfaceDhcpClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,255))
_DhcpInterfaceDhcpClientId_Type.__name__=_G
_DhcpInterfaceDhcpClientId_Object=MibTableColumn
dhcpInterfaceDhcpClientId=_DhcpInterfaceDhcpClientId_Object((1,3,6,1,4,1,5504,4,1,1,2,1,9),_DhcpInterfaceDhcpClientId_Type())
dhcpInterfaceDhcpClientId.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpInterfaceDhcpClientId.setStatus(_A)
class _DhcpInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('init',1),('reboot',2),('bound',3),('verify',4),('release',5),('invalid',6),('bind',7)))
_DhcpInterfaceState_Type.__name__=_L
_DhcpInterfaceState_Object=MibTableColumn
dhcpInterfaceState=_DhcpInterfaceState_Object((1,3,6,1,4,1,5504,4,1,1,2,1,10),_DhcpInterfaceState_Type())
dhcpInterfaceState.setMaxAccess(_D)
if mibBuilder.loadTexts:dhcpInterfaceState.setStatus(_A)
_DnsTable_Object=MibTable
dnsTable=_DnsTable_Object((1,3,6,1,4,1,5504,4,1,1,3))
if mibBuilder.loadTexts:dnsTable.setStatus(_A)
_DnsEntry_Object=MibTableRow
dnsEntry=_DnsEntry_Object((1,3,6,1,4,1,5504,4,1,1,3,1))
dnsEntry.setIndexNames((0,_H,_I),(0,_F,_O))
if mibBuilder.loadTexts:dnsEntry.setStatus(_A)
_DnsIpAddress_Type=IpAddress
_DnsIpAddress_Object=MibTableColumn
dnsIpAddress=_DnsIpAddress_Object((1,3,6,1,4,1,5504,4,1,1,3,1,1),_DnsIpAddress_Type())
dnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsIpAddress.setStatus(_A)
_RoutersTable_Object=MibTable
routersTable=_RoutersTable_Object((1,3,6,1,4,1,5504,4,1,1,4))
if mibBuilder.loadTexts:routersTable.setStatus(_A)
_RoutersEntry_Object=MibTableRow
routersEntry=_RoutersEntry_Object((1,3,6,1,4,1,5504,4,1,1,4,1))
routersEntry.setIndexNames((0,_H,_I),(0,_F,_P))
if mibBuilder.loadTexts:routersEntry.setStatus(_A)
_RoutersIpAddress_Type=IpAddress
_RoutersIpAddress_Object=MibTableColumn
routersIpAddress=_RoutersIpAddress_Object((1,3,6,1,4,1,5504,4,1,1,4,1,1),_RoutersIpAddress_Type())
routersIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:routersIpAddress.setStatus(_A)
ipInterfaceEntry.registerAugmentions((_F,_Q))
dhcpInterfacesEntry.setIndexNames(*ipInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'dhcpClient':dhcpClient,'dhcpClientResourceTable':dhcpClientResourceTable,'dhcpClientResourceEntry':dhcpClientResourceEntry,'dhcpOfferTimeout':dhcpOfferTimeout,'dhcpDefaultLease':dhcpDefaultLease,'dhcpMinLease':dhcpMinLease,'dhcpClientErrors':dhcpClientErrors,'dhcpAvgTimeForLease':dhcpAvgTimeForLease,'dhcpInterfacesTable':dhcpInterfacesTable,_Q:dhcpInterfacesEntry,'dhcpInterfaceServerName':dhcpInterfaceServerName,'dhcpInterfaceRenew':dhcpInterfaceRenew,'dhcpInterfaceRebind':dhcpInterfaceRebind,'dhcpInterfaceBootFile':dhcpInterfaceBootFile,'dhcpInterfaceTftp':dhcpInterfaceTftp,'dhcpInterfaceHostname':dhcpInterfaceHostname,'dhcpInterfaceDomainName':dhcpInterfaceDomainName,'dhcpInterfaceVendorClassId':dhcpInterfaceVendorClassId,'dhcpInterfaceDhcpClientId':dhcpInterfaceDhcpClientId,'dhcpInterfaceState':dhcpInterfaceState,'dnsTable':dnsTable,'dnsEntry':dnsEntry,_O:dnsIpAddress,'routersTable':routersTable,'routersEntry':routersEntry,_P:routersIpAddress,'comIpDhcpClient':comIpDhcpClient})