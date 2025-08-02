_P='oacIpDnsConfigDomainName'
_O='ONEACCESS-IP-SERVICES-MIB'
_N='disabled'
_M='enabled'
_L='00000000'
_K='OctetString'
_J='read-only'
_I='IpAddress'
_H='ifIndex'
_G='IF-MIB'
_F='DisplayString'
_E='TruthValue'
_D='Integer32'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
oacExpIMIp,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIp','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_I,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention',_E)
oacIpServicesConfigMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,683))
if mibBuilder.loadTexts:oacIpServicesConfigMIB.setRevisions(('2011-07-29 00:00','2011-06-15 00:00'))
_OacIpServicesConfig_ObjectIdentity=ObjectIdentity
oacIpServicesConfig=_OacIpServicesConfig_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8))
_OacIpServicesConfigObjects_ObjectIdentity=ObjectIdentity
oacIpServicesConfigObjects=_OacIpServicesConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,1))
_OacIpServicesDnsConfigObjects_ObjectIdentity=ObjectIdentity
oacIpServicesDnsConfigObjects=_OacIpServicesDnsConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,1,1))
class _OacIpDnsConfigDomainName_Type(DisplayString):defaultValue=OctetString('')
_OacIpDnsConfigDomainName_Type.__name__=_F
_OacIpDnsConfigDomainName_Object=MibScalar
oacIpDnsConfigDomainName=_OacIpDnsConfigDomainName_Object((1,3,6,1,4,1,13191,10,3,1,8,1,1,1),_OacIpDnsConfigDomainName_Type())
oacIpDnsConfigDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpDnsConfigDomainName.setStatus(_A)
class _OacIpDnsConfigMainAdd_Type(IpAddress):defaultHexValue=_L
_OacIpDnsConfigMainAdd_Type.__name__=_I
_OacIpDnsConfigMainAdd_Object=MibScalar
oacIpDnsConfigMainAdd=_OacIpDnsConfigMainAdd_Object((1,3,6,1,4,1,13191,10,3,1,8,1,1,2),_OacIpDnsConfigMainAdd_Type())
oacIpDnsConfigMainAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpDnsConfigMainAdd.setStatus(_A)
class _OacIpDnsConfigSndAdd_Type(IpAddress):defaultHexValue=_L
_OacIpDnsConfigSndAdd_Type.__name__=_I
_OacIpDnsConfigSndAdd_Object=MibScalar
oacIpDnsConfigSndAdd=_OacIpDnsConfigSndAdd_Object((1,3,6,1,4,1,13191,10,3,1,8,1,1,3),_OacIpDnsConfigSndAdd_Type())
oacIpDnsConfigSndAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpDnsConfigSndAdd.setStatus(_A)
class _OacIpDnsConfigTimeout_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('timeoutValueDefault',1),('timeoutValue4',2),('timeoutValue12',3),('timeoutValue18',4),('timeoutValue42',5),('timeoutValue90',6),('timeoutValue120',7)))
_OacIpDnsConfigTimeout_Type.__name__=_D
_OacIpDnsConfigTimeout_Object=MibScalar
oacIpDnsConfigTimeout=_OacIpDnsConfigTimeout_Object((1,3,6,1,4,1,13191,10,3,1,8,1,1,4),_OacIpDnsConfigTimeout_Type())
oacIpDnsConfigTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpDnsConfigTimeout.setStatus(_A)
_OacIpServicesDHCPCConfigObjects_ObjectIdentity=ObjectIdentity
oacIpServicesDHCPCConfigObjects=_OacIpServicesDHCPCConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,1,2))
class _OacDhcpClientAutoRestartAtm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_OacDhcpClientAutoRestartAtm_Type.__name__=_D
_OacDhcpClientAutoRestartAtm_Object=MibScalar
oacDhcpClientAutoRestartAtm=_OacDhcpClientAutoRestartAtm_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,1),_OacDhcpClientAutoRestartAtm_Type())
oacDhcpClientAutoRestartAtm.setMaxAccess(_B)
if mibBuilder.loadTexts:oacDhcpClientAutoRestartAtm.setStatus(_A)
class _OacDhcpClientBroadcastFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_OacDhcpClientBroadcastFlag_Type.__name__=_D
_OacDhcpClientBroadcastFlag_Object=MibScalar
oacDhcpClientBroadcastFlag=_OacDhcpClientBroadcastFlag_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,2),_OacDhcpClientBroadcastFlag_Type())
oacDhcpClientBroadcastFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:oacDhcpClientBroadcastFlag.setStatus(_A)
class _OacDhcpVendorId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,199))
_OacDhcpVendorId_Type.__name__=_K
_OacDhcpVendorId_Object=MibScalar
oacDhcpVendorId=_OacDhcpVendorId_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,3),_OacDhcpVendorId_Type())
oacDhcpVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacDhcpVendorId.setStatus(_A)
_OacIpDhcpClientInterfaceTable_Object=MibTable
oacIpDhcpClientInterfaceTable=_OacIpDhcpClientInterfaceTable_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4))
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceTable.setStatus(_A)
_OacIpDhcpClientInterfaceEntry_Object=MibTableRow
oacIpDhcpClientInterfaceEntry=_OacIpDhcpClientInterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1))
oacIpDhcpClientInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceEntry.setStatus(_A)
_OacIpDhcpClientInterfaceIfName_Type=DisplayString
_OacIpDhcpClientInterfaceIfName_Object=MibTableColumn
oacIpDhcpClientInterfaceIfName=_OacIpDhcpClientInterfaceIfName_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1,1),_OacIpDhcpClientInterfaceIfName_Type())
oacIpDhcpClientInterfaceIfName.setMaxAccess(_J)
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceIfName.setStatus(_A)
class _OacIpDhcpClientInterfaceIgnoreDefRoute_Type(TruthValue):defaultValue=2
_OacIpDhcpClientInterfaceIgnoreDefRoute_Type.__name__=_E
_OacIpDhcpClientInterfaceIgnoreDefRoute_Object=MibTableColumn
oacIpDhcpClientInterfaceIgnoreDefRoute=_OacIpDhcpClientInterfaceIgnoreDefRoute_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1,2),_OacIpDhcpClientInterfaceIgnoreDefRoute_Type())
oacIpDhcpClientInterfaceIgnoreDefRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceIgnoreDefRoute.setStatus(_A)
class _OacIpDhcpClientInterfaceLeaseOptLess_Type(TruthValue):defaultValue=2
_OacIpDhcpClientInterfaceLeaseOptLess_Type.__name__=_E
_OacIpDhcpClientInterfaceLeaseOptLess_Object=MibTableColumn
oacIpDhcpClientInterfaceLeaseOptLess=_OacIpDhcpClientInterfaceLeaseOptLess_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1,3),_OacIpDhcpClientInterfaceLeaseOptLess_Type())
oacIpDhcpClientInterfaceLeaseOptLess.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceLeaseOptLess.setStatus(_A)
class _OacIpDhcpClientInterfaceUserClassId_Type(DisplayString):defaultValue=OctetString('')
_OacIpDhcpClientInterfaceUserClassId_Type.__name__=_F
_OacIpDhcpClientInterfaceUserClassId_Object=MibTableColumn
oacIpDhcpClientInterfaceUserClassId=_OacIpDhcpClientInterfaceUserClassId_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1,4),_OacIpDhcpClientInterfaceUserClassId_Type())
oacIpDhcpClientInterfaceUserClassId.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceUserClassId.setStatus(_A)
_OacIpDhcpClientInterfaceRowStatus_Type=RowStatus
_OacIpDhcpClientInterfaceRowStatus_Object=MibTableColumn
oacIpDhcpClientInterfaceRowStatus=_OacIpDhcpClientInterfaceRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,4,1,5),_OacIpDhcpClientInterfaceRowStatus_Type())
oacIpDhcpClientInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpClientInterfaceRowStatus.setStatus(_A)
_OacIpDhcpAddClientInterfaceTable_Object=MibTable
oacIpDhcpAddClientInterfaceTable=_OacIpDhcpAddClientInterfaceTable_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5))
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceTable.setStatus(_A)
_OacIpDhcpAddClientInterfaceEntry_Object=MibTableRow
oacIpDhcpAddClientInterfaceEntry=_OacIpDhcpAddClientInterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1))
oacIpDhcpAddClientInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceEntry.setStatus(_A)
class _OacIpDhcpAddClientInterfaceActivate_Type(TruthValue):defaultValue=2
_OacIpDhcpAddClientInterfaceActivate_Type.__name__=_E
_OacIpDhcpAddClientInterfaceActivate_Object=MibTableColumn
oacIpDhcpAddClientInterfaceActivate=_OacIpDhcpAddClientInterfaceActivate_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1,1),_OacIpDhcpAddClientInterfaceActivate_Type())
oacIpDhcpAddClientInterfaceActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceActivate.setStatus(_A)
_OacIpDhcpAddClientInterfaceIfName_Type=DisplayString
_OacIpDhcpAddClientInterfaceIfName_Object=MibTableColumn
oacIpDhcpAddClientInterfaceIfName=_OacIpDhcpAddClientInterfaceIfName_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1,2),_OacIpDhcpAddClientInterfaceIfName_Type())
oacIpDhcpAddClientInterfaceIfName.setMaxAccess(_J)
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceIfName.setStatus(_A)
class _OacIpDhcpAddClientInterfaceClientId_Type(DisplayString):defaultValue=OctetString('')
_OacIpDhcpAddClientInterfaceClientId_Type.__name__=_F
_OacIpDhcpAddClientInterfaceClientId_Object=MibTableColumn
oacIpDhcpAddClientInterfaceClientId=_OacIpDhcpAddClientInterfaceClientId_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1,3),_OacIpDhcpAddClientInterfaceClientId_Type())
oacIpDhcpAddClientInterfaceClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceClientId.setStatus(_A)
class _OacIpDhcpAddClientInterfaceHostname_Type(DisplayString):defaultValue=OctetString('')
_OacIpDhcpAddClientInterfaceHostname_Type.__name__=_F
_OacIpDhcpAddClientInterfaceHostname_Object=MibTableColumn
oacIpDhcpAddClientInterfaceHostname=_OacIpDhcpAddClientInterfaceHostname_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1,4),_OacIpDhcpAddClientInterfaceHostname_Type())
oacIpDhcpAddClientInterfaceHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceHostname.setStatus(_A)
_OacIpDhcpAddClientInterfaceRowStatus_Type=RowStatus
_OacIpDhcpAddClientInterfaceRowStatus_Object=MibTableColumn
oacIpDhcpAddClientInterfaceRowStatus=_OacIpDhcpAddClientInterfaceRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,8,1,2,5,1,5),_OacIpDhcpAddClientInterfaceRowStatus_Type())
oacIpDhcpAddClientInterfaceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpDhcpAddClientInterfaceRowStatus.setStatus(_A)
_OacIpServicesArpProxyConfigObjects_ObjectIdentity=ObjectIdentity
oacIpServicesArpProxyConfigObjects=_OacIpServicesArpProxyConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,1,3))
_OacIpProxyArpInterfaceConfigTable_Object=MibTable
oacIpProxyArpInterfaceConfigTable=_OacIpProxyArpInterfaceConfigTable_Object((1,3,6,1,4,1,13191,10,3,1,8,1,3,1))
if mibBuilder.loadTexts:oacIpProxyArpInterfaceConfigTable.setStatus(_A)
_OacIpProxyArpInterfaceConfigEntry_Object=MibTableRow
oacIpProxyArpInterfaceConfigEntry=_OacIpProxyArpInterfaceConfigEntry_Object((1,3,6,1,4,1,13191,10,3,1,8,1,3,1,1))
oacIpProxyArpInterfaceConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:oacIpProxyArpInterfaceConfigEntry.setStatus(_A)
class _OacIpProxyArpInterfaceConfigActivate_Type(TruthValue):defaultValue=1
_OacIpProxyArpInterfaceConfigActivate_Type.__name__=_E
_OacIpProxyArpInterfaceConfigActivate_Object=MibTableColumn
oacIpProxyArpInterfaceConfigActivate=_OacIpProxyArpInterfaceConfigActivate_Object((1,3,6,1,4,1,13191,10,3,1,8,1,3,1,1,1),_OacIpProxyArpInterfaceConfigActivate_Type())
oacIpProxyArpInterfaceConfigActivate.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpProxyArpInterfaceConfigActivate.setStatus(_A)
_OacIpProxyArpInterfaceConfigIfName_Type=DisplayString
_OacIpProxyArpInterfaceConfigIfName_Object=MibTableColumn
oacIpProxyArpInterfaceConfigIfName=_OacIpProxyArpInterfaceConfigIfName_Object((1,3,6,1,4,1,13191,10,3,1,8,1,3,1,1,2),_OacIpProxyArpInterfaceConfigIfName_Type())
oacIpProxyArpInterfaceConfigIfName.setMaxAccess(_J)
if mibBuilder.loadTexts:oacIpProxyArpInterfaceConfigIfName.setStatus(_A)
_OacIpProxyArpInterfaceConfigRowStatus_Type=RowStatus
_OacIpProxyArpInterfaceConfigRowStatus_Object=MibTableColumn
oacIpProxyArpInterfaceConfigRowStatus=_OacIpProxyArpInterfaceConfigRowStatus_Object((1,3,6,1,4,1,13191,10,3,1,8,1,3,1,1,3),_OacIpProxyArpInterfaceConfigRowStatus_Type())
oacIpProxyArpInterfaceConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oacIpProxyArpInterfaceConfigRowStatus.setStatus(_A)
_OacIpServicesIcmpRedirConfigObjects_ObjectIdentity=ObjectIdentity
oacIpServicesIcmpRedirConfigObjects=_OacIpServicesIcmpRedirConfigObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,1,4))
class _OacIpIcmpRedirConfigActivate_Type(TruthValue):defaultValue=1
_OacIpIcmpRedirConfigActivate_Type.__name__=_E
_OacIpIcmpRedirConfigActivate_Object=MibScalar
oacIpIcmpRedirConfigActivate=_OacIpIcmpRedirConfigActivate_Object((1,3,6,1,4,1,13191,10,3,1,8,1,4,1),_OacIpIcmpRedirConfigActivate_Type())
oacIpIcmpRedirConfigActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpIcmpRedirConfigActivate.setStatus(_A)
class _OacIpIcmpRedirConfigRedirRoutesActivate_Type(Integer32):defaultValue=0
_OacIpIcmpRedirConfigRedirRoutesActivate_Type.__name__=_D
_OacIpIcmpRedirConfigRedirRoutesActivate_Object=MibScalar
oacIpIcmpRedirConfigRedirRoutesActivate=_OacIpIcmpRedirConfigRedirRoutesActivate_Object((1,3,6,1,4,1,13191,10,3,1,8,1,4,2),_OacIpIcmpRedirConfigRedirRoutesActivate_Type())
oacIpIcmpRedirConfigRedirRoutesActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpIcmpRedirConfigRedirRoutesActivate.setStatus(_A)
class _OacIpIcmpRedirConfigRateLimitUnreach_Type(Integer32):defaultValue=0
_OacIpIcmpRedirConfigRateLimitUnreach_Type.__name__=_D
_OacIpIcmpRedirConfigRateLimitUnreach_Object=MibScalar
oacIpIcmpRedirConfigRateLimitUnreach=_OacIpIcmpRedirConfigRateLimitUnreach_Object((1,3,6,1,4,1,13191,10,3,1,8,1,4,3),_OacIpIcmpRedirConfigRateLimitUnreach_Type())
oacIpIcmpRedirConfigRateLimitUnreach.setMaxAccess(_B)
if mibBuilder.loadTexts:oacIpIcmpRedirConfigRateLimitUnreach.setStatus(_A)
_OacIpServicesConfigConformance_ObjectIdentity=ObjectIdentity
oacIpServicesConfigConformance=_OacIpServicesConfigConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,2))
_OacIpServicesGroups_ObjectIdentity=ObjectIdentity
oacIpServicesGroups=_OacIpServicesGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,2,1))
_OacIpServicesCompls_ObjectIdentity=ObjectIdentity
oacIpServicesCompls=_OacIpServicesCompls_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,8,2,2))
oacIpServicesConfigGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,1,8,2,1,1))
oacIpServicesConfigGroup.setObjects((_O,_P))
if mibBuilder.loadTexts:oacIpServicesConfigGroup.setStatus(_A)
mibBuilder.exportSymbols(_O,**{'oacIpServicesConfigMIB':oacIpServicesConfigMIB,'oacIpServicesConfig':oacIpServicesConfig,'oacIpServicesConfigObjects':oacIpServicesConfigObjects,'oacIpServicesDnsConfigObjects':oacIpServicesDnsConfigObjects,_P:oacIpDnsConfigDomainName,'oacIpDnsConfigMainAdd':oacIpDnsConfigMainAdd,'oacIpDnsConfigSndAdd':oacIpDnsConfigSndAdd,'oacIpDnsConfigTimeout':oacIpDnsConfigTimeout,'oacIpServicesDHCPCConfigObjects':oacIpServicesDHCPCConfigObjects,'oacDhcpClientAutoRestartAtm':oacDhcpClientAutoRestartAtm,'oacDhcpClientBroadcastFlag':oacDhcpClientBroadcastFlag,'oacDhcpVendorId':oacDhcpVendorId,'oacIpDhcpClientInterfaceTable':oacIpDhcpClientInterfaceTable,'oacIpDhcpClientInterfaceEntry':oacIpDhcpClientInterfaceEntry,'oacIpDhcpClientInterfaceIfName':oacIpDhcpClientInterfaceIfName,'oacIpDhcpClientInterfaceIgnoreDefRoute':oacIpDhcpClientInterfaceIgnoreDefRoute,'oacIpDhcpClientInterfaceLeaseOptLess':oacIpDhcpClientInterfaceLeaseOptLess,'oacIpDhcpClientInterfaceUserClassId':oacIpDhcpClientInterfaceUserClassId,'oacIpDhcpClientInterfaceRowStatus':oacIpDhcpClientInterfaceRowStatus,'oacIpDhcpAddClientInterfaceTable':oacIpDhcpAddClientInterfaceTable,'oacIpDhcpAddClientInterfaceEntry':oacIpDhcpAddClientInterfaceEntry,'oacIpDhcpAddClientInterfaceActivate':oacIpDhcpAddClientInterfaceActivate,'oacIpDhcpAddClientInterfaceIfName':oacIpDhcpAddClientInterfaceIfName,'oacIpDhcpAddClientInterfaceClientId':oacIpDhcpAddClientInterfaceClientId,'oacIpDhcpAddClientInterfaceHostname':oacIpDhcpAddClientInterfaceHostname,'oacIpDhcpAddClientInterfaceRowStatus':oacIpDhcpAddClientInterfaceRowStatus,'oacIpServicesArpProxyConfigObjects':oacIpServicesArpProxyConfigObjects,'oacIpProxyArpInterfaceConfigTable':oacIpProxyArpInterfaceConfigTable,'oacIpProxyArpInterfaceConfigEntry':oacIpProxyArpInterfaceConfigEntry,'oacIpProxyArpInterfaceConfigActivate':oacIpProxyArpInterfaceConfigActivate,'oacIpProxyArpInterfaceConfigIfName':oacIpProxyArpInterfaceConfigIfName,'oacIpProxyArpInterfaceConfigRowStatus':oacIpProxyArpInterfaceConfigRowStatus,'oacIpServicesIcmpRedirConfigObjects':oacIpServicesIcmpRedirConfigObjects,'oacIpIcmpRedirConfigActivate':oacIpIcmpRedirConfigActivate,'oacIpIcmpRedirConfigRedirRoutesActivate':oacIpIcmpRedirConfigRedirRoutesActivate,'oacIpIcmpRedirConfigRateLimitUnreach':oacIpIcmpRedirConfigRateLimitUnreach,'oacIpServicesConfigConformance':oacIpServicesConfigConformance,'oacIpServicesGroups':oacIpServicesGroups,'oacIpServicesConfigGroup':oacIpServicesConfigGroup,'oacIpServicesCompls':oacIpServicesCompls})