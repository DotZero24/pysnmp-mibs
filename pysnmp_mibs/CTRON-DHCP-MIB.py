_I='ctDhcpClientStatsID'
_H='ctDhcpIfIndex'
_G='CTRON-DHCP-MIB'
_F='enabled'
_E='disabled'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwIpClientServices,nwIpComponents,nwIpMibs,nwIpRouter=mibBuilder.importSymbols('CTRON-IP-ROUTER-MIB','nwIpClientServices','nwIpComponents','nwIpMibs','nwIpRouter')
nwRtrProtoSuites,=mibBuilder.importSymbols('ROUTER-OIDS','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtDhcp_ObjectIdentity=ObjectIdentity
ctDhcp=_CtDhcp_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2))
_CtDhcpServerStats_ObjectIdentity=ObjectIdentity
ctDhcpServerStats=_CtDhcpServerStats_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1))
class _CtDhcpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CtDhcpAdminStatus_Type.__name__=_D
_CtDhcpAdminStatus_Object=MibScalar
ctDhcpAdminStatus=_CtDhcpAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,1),_CtDhcpAdminStatus_Type())
ctDhcpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpAdminStatus.setStatus(_A)
class _CtDhcpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CtDhcpOperStatus_Type.__name__=_D
_CtDhcpOperStatus_Object=MibScalar
ctDhcpOperStatus=_CtDhcpOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,2),_CtDhcpOperStatus_Type())
ctDhcpOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpOperStatus.setStatus(_A)
_CtDhcpDiscovers_Type=Counter32
_CtDhcpDiscovers_Object=MibScalar
ctDhcpDiscovers=_CtDhcpDiscovers_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,3),_CtDhcpDiscovers_Type())
ctDhcpDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpDiscovers.setStatus(_A)
_CtDhcpOffers_Type=Counter32
_CtDhcpOffers_Object=MibScalar
ctDhcpOffers=_CtDhcpOffers_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,4),_CtDhcpOffers_Type())
ctDhcpOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpOffers.setStatus(_A)
_CtDhcpRequests_Type=Counter32
_CtDhcpRequests_Object=MibScalar
ctDhcpRequests=_CtDhcpRequests_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,5),_CtDhcpRequests_Type())
ctDhcpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpRequests.setStatus(_A)
_CtDhcpDeclines_Type=Counter32
_CtDhcpDeclines_Object=MibScalar
ctDhcpDeclines=_CtDhcpDeclines_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,6),_CtDhcpDeclines_Type())
ctDhcpDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpDeclines.setStatus(_A)
_CtDhcpReleases_Type=Counter32
_CtDhcpReleases_Object=MibScalar
ctDhcpReleases=_CtDhcpReleases_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,7),_CtDhcpReleases_Type())
ctDhcpReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpReleases.setStatus(_A)
_CtDhcpAcks_Type=Counter32
_CtDhcpAcks_Object=MibScalar
ctDhcpAcks=_CtDhcpAcks_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,8),_CtDhcpAcks_Type())
ctDhcpAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpAcks.setStatus(_A)
_CtDhcpNaks_Type=Counter32
_CtDhcpNaks_Object=MibScalar
ctDhcpNaks=_CtDhcpNaks_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,9),_CtDhcpNaks_Type())
ctDhcpNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpNaks.setStatus(_A)
_CtDhcpOtherServers_Type=Counter32
_CtDhcpOtherServers_Object=MibScalar
ctDhcpOtherServers=_CtDhcpOtherServers_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,10),_CtDhcpOtherServers_Type())
ctDhcpOtherServers.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpOtherServers.setStatus(_A)
_CtDhcpProtocolErrors_Type=Counter32
_CtDhcpProtocolErrors_Object=MibScalar
ctDhcpProtocolErrors=_CtDhcpProtocolErrors_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,11),_CtDhcpProtocolErrors_Type())
ctDhcpProtocolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpProtocolErrors.setStatus(_A)
_CtDhcpServerTime_Type=Integer32
_CtDhcpServerTime_Object=MibScalar
ctDhcpServerTime=_CtDhcpServerTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,12),_CtDhcpServerTime_Type())
ctDhcpServerTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpServerTime.setStatus(_A)
_CtDhcpNoOfActiveClients_Type=Integer32
_CtDhcpNoOfActiveClients_Object=MibScalar
ctDhcpNoOfActiveClients=_CtDhcpNoOfActiveClients_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,13),_CtDhcpNoOfActiveClients_Type())
ctDhcpNoOfActiveClients.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpNoOfActiveClients.setStatus(_A)
_CtDhcpReclaimIP_Type=IpAddress
_CtDhcpReclaimIP_Object=MibScalar
ctDhcpReclaimIP=_CtDhcpReclaimIP_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,1,14),_CtDhcpReclaimIP_Type())
ctDhcpReclaimIP.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpReclaimIP.setStatus(_A)
_CtDhcpInterfaceConfig_ObjectIdentity=ObjectIdentity
ctDhcpInterfaceConfig=_CtDhcpInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2))
_CtDhcpServerIfTable_Object=MibTable
ctDhcpServerIfTable=_CtDhcpServerIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1))
if mibBuilder.loadTexts:ctDhcpServerIfTable.setStatus(_A)
_CtDhcpServerIfEntry_Object=MibTableRow
ctDhcpServerIfEntry=_CtDhcpServerIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1))
ctDhcpServerIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ctDhcpServerIfEntry.setStatus(_A)
_CtDhcpIfIndex_Type=Integer32
_CtDhcpIfIndex_Object=MibTableColumn
ctDhcpIfIndex=_CtDhcpIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,1),_CtDhcpIfIndex_Type())
ctDhcpIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpIfIndex.setStatus(_A)
class _CtDhcpIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_CtDhcpIfAdminStatus_Type.__name__=_D
_CtDhcpIfAdminStatus_Object=MibTableColumn
ctDhcpIfAdminStatus=_CtDhcpIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,2),_CtDhcpIfAdminStatus_Type())
ctDhcpIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfAdminStatus.setStatus(_A)
class _CtDhcpIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),('invalid-config',3)))
_CtDhcpIfOperStatus_Type.__name__=_D
_CtDhcpIfOperStatus_Object=MibTableColumn
ctDhcpIfOperStatus=_CtDhcpIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,3),_CtDhcpIfOperStatus_Type())
ctDhcpIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpIfOperStatus.setStatus(_A)
_CtDhcpIfServerAddress_Type=IpAddress
_CtDhcpIfServerAddress_Object=MibTableColumn
ctDhcpIfServerAddress=_CtDhcpIfServerAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,4),_CtDhcpIfServerAddress_Type())
ctDhcpIfServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpIfServerAddress.setStatus(_A)
_CtDhcpIfNetworkAddress_Type=IpAddress
_CtDhcpIfNetworkAddress_Object=MibTableColumn
ctDhcpIfNetworkAddress=_CtDhcpIfNetworkAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,5),_CtDhcpIfNetworkAddress_Type())
ctDhcpIfNetworkAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfNetworkAddress.setStatus(_A)
_CtDhcpIfSubnetMask_Type=IpAddress
_CtDhcpIfSubnetMask_Object=MibTableColumn
ctDhcpIfSubnetMask=_CtDhcpIfSubnetMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,6),_CtDhcpIfSubnetMask_Type())
ctDhcpIfSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfSubnetMask.setStatus(_A)
_CtDhcpIfLowestaddress_Type=IpAddress
_CtDhcpIfLowestaddress_Object=MibTableColumn
ctDhcpIfLowestaddress=_CtDhcpIfLowestaddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,7),_CtDhcpIfLowestaddress_Type())
ctDhcpIfLowestaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfLowestaddress.setStatus(_A)
_CtDhcpIfHighestAddress_Type=IpAddress
_CtDhcpIfHighestAddress_Object=MibTableColumn
ctDhcpIfHighestAddress=_CtDhcpIfHighestAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,8),_CtDhcpIfHighestAddress_Type())
ctDhcpIfHighestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfHighestAddress.setStatus(_A)
_CtDhcpIfAddressesUsed_Type=Integer32
_CtDhcpIfAddressesUsed_Object=MibTableColumn
ctDhcpIfAddressesUsed=_CtDhcpIfAddressesUsed_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,9),_CtDhcpIfAddressesUsed_Type())
ctDhcpIfAddressesUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpIfAddressesUsed.setStatus(_A)
_CtDhcpIfAddressesFree_Type=Integer32
_CtDhcpIfAddressesFree_Object=MibTableColumn
ctDhcpIfAddressesFree=_CtDhcpIfAddressesFree_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,10),_CtDhcpIfAddressesFree_Type())
ctDhcpIfAddressesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpIfAddressesFree.setStatus(_A)
_CtDhcpIfLeasePeriod_Type=Integer32
_CtDhcpIfLeasePeriod_Object=MibTableColumn
ctDhcpIfLeasePeriod=_CtDhcpIfLeasePeriod_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,11),_CtDhcpIfLeasePeriod_Type())
ctDhcpIfLeasePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfLeasePeriod.setStatus(_A)
_CtDhcpIfDefaultGateway_Type=IpAddress
_CtDhcpIfDefaultGateway_Object=MibTableColumn
ctDhcpIfDefaultGateway=_CtDhcpIfDefaultGateway_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,12),_CtDhcpIfDefaultGateway_Type())
ctDhcpIfDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfDefaultGateway.setStatus(_A)
_CtDhcpIfDomainNameServer_Type=IpAddress
_CtDhcpIfDomainNameServer_Object=MibTableColumn
ctDhcpIfDomainNameServer=_CtDhcpIfDomainNameServer_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,13),_CtDhcpIfDomainNameServer_Type())
ctDhcpIfDomainNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfDomainNameServer.setStatus(_A)
_CtDhcpIfDomainName_Type=OctetString
_CtDhcpIfDomainName_Object=MibTableColumn
ctDhcpIfDomainName=_CtDhcpIfDomainName_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,14),_CtDhcpIfDomainName_Type())
ctDhcpIfDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfDomainName.setStatus(_A)
_CtDhcpIfWINServer_Type=IpAddress
_CtDhcpIfWINServer_Object=MibTableColumn
ctDhcpIfWINServer=_CtDhcpIfWINServer_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,2,1,1,15),_CtDhcpIfWINServer_Type())
ctDhcpIfWINServer.setMaxAccess(_C)
if mibBuilder.loadTexts:ctDhcpIfWINServer.setStatus(_A)
_CtDhcpClientStatusTable_ObjectIdentity=ObjectIdentity
ctDhcpClientStatusTable=_CtDhcpClientStatusTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3))
_CtDhcpClientStatsTable_Object=MibTable
ctDhcpClientStatsTable=_CtDhcpClientStatsTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1))
if mibBuilder.loadTexts:ctDhcpClientStatsTable.setStatus(_A)
_CtDhcpClientStatsEntry_Object=MibTableRow
ctDhcpClientStatsEntry=_CtDhcpClientStatsEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1))
ctDhcpClientStatsEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:ctDhcpClientStatsEntry.setStatus(_A)
_CtDhcpClientStatsID_Type=Integer32
_CtDhcpClientStatsID_Object=MibTableColumn
ctDhcpClientStatsID=_CtDhcpClientStatsID_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1,1),_CtDhcpClientStatsID_Type())
ctDhcpClientStatsID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpClientStatsID.setStatus(_A)
_CtDhcpClientName_Type=OctetString
_CtDhcpClientName_Object=MibTableColumn
ctDhcpClientName=_CtDhcpClientName_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1,2),_CtDhcpClientName_Type())
ctDhcpClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpClientName.setStatus(_A)
_CtDhcpClientIP_Type=IpAddress
_CtDhcpClientIP_Object=MibTableColumn
ctDhcpClientIP=_CtDhcpClientIP_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1,3),_CtDhcpClientIP_Type())
ctDhcpClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpClientIP.setStatus(_A)
_CtDhcpClientID_Type=OctetString
_CtDhcpClientID_Object=MibTableColumn
ctDhcpClientID=_CtDhcpClientID_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1,4),_CtDhcpClientID_Type())
ctDhcpClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpClientID.setStatus(_A)
_CtDhcpEndOfLease_Type=Integer32
_CtDhcpEndOfLease_Object=MibTableColumn
ctDhcpEndOfLease=_CtDhcpEndOfLease_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12,2,3,1,1,5),_CtDhcpEndOfLease_Type())
ctDhcpEndOfLease.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDhcpEndOfLease.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'ctDhcp':ctDhcp,'ctDhcpServerStats':ctDhcpServerStats,'ctDhcpAdminStatus':ctDhcpAdminStatus,'ctDhcpOperStatus':ctDhcpOperStatus,'ctDhcpDiscovers':ctDhcpDiscovers,'ctDhcpOffers':ctDhcpOffers,'ctDhcpRequests':ctDhcpRequests,'ctDhcpDeclines':ctDhcpDeclines,'ctDhcpReleases':ctDhcpReleases,'ctDhcpAcks':ctDhcpAcks,'ctDhcpNaks':ctDhcpNaks,'ctDhcpOtherServers':ctDhcpOtherServers,'ctDhcpProtocolErrors':ctDhcpProtocolErrors,'ctDhcpServerTime':ctDhcpServerTime,'ctDhcpNoOfActiveClients':ctDhcpNoOfActiveClients,'ctDhcpReclaimIP':ctDhcpReclaimIP,'ctDhcpInterfaceConfig':ctDhcpInterfaceConfig,'ctDhcpServerIfTable':ctDhcpServerIfTable,'ctDhcpServerIfEntry':ctDhcpServerIfEntry,_H:ctDhcpIfIndex,'ctDhcpIfAdminStatus':ctDhcpIfAdminStatus,'ctDhcpIfOperStatus':ctDhcpIfOperStatus,'ctDhcpIfServerAddress':ctDhcpIfServerAddress,'ctDhcpIfNetworkAddress':ctDhcpIfNetworkAddress,'ctDhcpIfSubnetMask':ctDhcpIfSubnetMask,'ctDhcpIfLowestaddress':ctDhcpIfLowestaddress,'ctDhcpIfHighestAddress':ctDhcpIfHighestAddress,'ctDhcpIfAddressesUsed':ctDhcpIfAddressesUsed,'ctDhcpIfAddressesFree':ctDhcpIfAddressesFree,'ctDhcpIfLeasePeriod':ctDhcpIfLeasePeriod,'ctDhcpIfDefaultGateway':ctDhcpIfDefaultGateway,'ctDhcpIfDomainNameServer':ctDhcpIfDomainNameServer,'ctDhcpIfDomainName':ctDhcpIfDomainName,'ctDhcpIfWINServer':ctDhcpIfWINServer,'ctDhcpClientStatusTable':ctDhcpClientStatusTable,'ctDhcpClientStatsTable':ctDhcpClientStatsTable,'ctDhcpClientStatsEntry':ctDhcpClientStatsEntry,_I:ctDhcpClientStatsID,'ctDhcpClientName':ctDhcpClientName,'ctDhcpClientIP':ctDhcpClientIP,'ctDhcpClientID':ctDhcpClientID,'ctDhcpEndOfLease':ctDhcpEndOfLease})