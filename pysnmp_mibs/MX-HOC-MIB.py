_V='staticHostsIndex'
_U='staticDnsServersPriority'
_T='dnsServersInfoPriority'
_S='staticSntpServersPriority'
_R='sntpServersInfoPriority'
_Q='EST5EDT4,M3.2.0/02:00:00,M11.1.0/02:00:00'
_P='MxIpAddr'
_O='MxIpAddress'
_N='MxEnableState'
_M='obsolete'
_L='MxIpHostName'
_K='automaticIpv6'
_J='automatic'
_I='MxIpHostNamePort'
_H='static'
_G='MX-HOC-MIB'
_F='Unsigned32'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_N,_O,_L,'MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32',_P,'MxIpAddrMask','MxIpAddrPort',_I,'MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hocMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700))
_HocMIBObjects_ObjectIdentity=ObjectIdentity
hocMIBObjects=_HocMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1))
class _ManagementInterface_Type(OctetString):defaultValue=OctetString('Lan1');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,50))
_ManagementInterface_Type.__name__=_D
_ManagementInterface_Object=MibScalar
managementInterface=_ManagementInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,100),_ManagementInterface_Type())
managementInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:managementInterface.setStatus(_A)
class _AutomaticConfigurationInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_AutomaticConfigurationInterface_Type.__name__=_D
_AutomaticConfigurationInterface_Object=MibScalar
automaticConfigurationInterface=_AutomaticConfigurationInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,150),_AutomaticConfigurationInterface_Type())
automaticConfigurationInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:automaticConfigurationInterface.setStatus(_A)
class _Ipv6AutomaticConfigurationInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_Ipv6AutomaticConfigurationInterface_Type.__name__=_D
_Ipv6AutomaticConfigurationInterface_Object=MibScalar
ipv6AutomaticConfigurationInterface=_Ipv6AutomaticConfigurationInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,175),_Ipv6AutomaticConfigurationInterface_Type())
ipv6AutomaticConfigurationInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:ipv6AutomaticConfigurationInterface.setStatus(_A)
class _HostName_Type(MxIpHostName):defaultValue=OctetString('')
_HostName_Type.__name__=_L
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,200),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_TimeGroup_ObjectIdentity=ObjectIdentity
timeGroup=_TimeGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,250))
_SystemTime_Type=OctetString
_SystemTime_Object=MibScalar
systemTime=_SystemTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,250,100),_SystemTime_Type())
systemTime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemTime.setStatus(_A)
_SystemUptime_Type=OctetString
_SystemUptime_Object=MibScalar
systemUptime=_SystemUptime_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,250,150),_SystemUptime_Type())
systemUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemUptime.setStatus(_A)
class _StaticTimeZone_Type(OctetString):defaultValue=OctetString(_Q);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_StaticTimeZone_Type.__name__=_D
_StaticTimeZone_Object=MibScalar
staticTimeZone=_StaticTimeZone_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,250,200),_StaticTimeZone_Type())
staticTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:staticTimeZone.setStatus(_A)
_DomainNameGroup_ObjectIdentity=ObjectIdentity
domainNameGroup=_DomainNameGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,300))
class _DomainNameConfigSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,150,200)));namedValues=NamedValues(*((_J,100),(_K,150),(_H,200)))
_DomainNameConfigSource_Type.__name__=_E
_DomainNameConfigSource_Object=MibScalar
domainNameConfigSource=_DomainNameConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,300,100),_DomainNameConfigSource_Type())
domainNameConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:domainNameConfigSource.setStatus(_A)
_DomainNameInfo_Type=MxIpHostName
_DomainNameInfo_Object=MibScalar
domainNameInfo=_DomainNameInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,300,200),_DomainNameInfo_Type())
domainNameInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:domainNameInfo.setStatus(_A)
class _StaticDomainName_Type(MxIpHostName):defaultValue=OctetString('')
_StaticDomainName_Type.__name__=_L
_StaticDomainName_Object=MibScalar
staticDomainName=_StaticDomainName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,300,300),_StaticDomainName_Type())
staticDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticDomainName.setStatus(_A)
_SntpGroup_ObjectIdentity=ObjectIdentity
sntpGroup=_SntpGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400))
class _SntpConfigSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,150,200,300)));namedValues=NamedValues(*((_J,100),(_K,150),(_H,200),('automaticWithFallback',300)))
_SntpConfigSource_Type.__name__=_E
_SntpConfigSource_Object=MibScalar
sntpConfigSource=_SntpConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,100),_SntpConfigSource_Type())
sntpConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpConfigSource.setStatus(_A)
class _SntpSynchronizationPeriod_Type(Unsigned32):defaultValue=1440;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_SntpSynchronizationPeriod_Type.__name__=_F
_SntpSynchronizationPeriod_Object=MibScalar
sntpSynchronizationPeriod=_SntpSynchronizationPeriod_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,200),_SntpSynchronizationPeriod_Type())
sntpSynchronizationPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpSynchronizationPeriod.setStatus(_A)
class _SntpSynchronizationPeriodOnError_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_SntpSynchronizationPeriodOnError_Type.__name__=_F
_SntpSynchronizationPeriodOnError_Object=MibScalar
sntpSynchronizationPeriodOnError=_SntpSynchronizationPeriodOnError_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,300),_SntpSynchronizationPeriodOnError_Type())
sntpSynchronizationPeriodOnError.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpSynchronizationPeriodOnError.setStatus(_A)
class _SntpTimeZone_Type(OctetString):defaultValue=OctetString(_Q);subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SntpTimeZone_Type.__name__=_D
_SntpTimeZone_Object=MibScalar
sntpTimeZone=_SntpTimeZone_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,400),_SntpTimeZone_Type())
sntpTimeZone.setMaxAccess(_B)
if mibBuilder.loadTexts:sntpTimeZone.setStatus(_M)
_SntpServerHostInfo_Type=MxIpHostNamePort
_SntpServerHostInfo_Object=MibScalar
sntpServerHostInfo=_SntpServerHostInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,500),_SntpServerHostInfo_Type())
sntpServerHostInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpServerHostInfo.setStatus(_M)
class _StaticSntpServerHost_Type(MxIpHostNamePort):defaultValue=OctetString('192.168.10.10:123')
_StaticSntpServerHost_Type.__name__=_I
_StaticSntpServerHost_Object=MibScalar
staticSntpServerHost=_StaticSntpServerHost_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,700),_StaticSntpServerHost_Type())
staticSntpServerHost.setMaxAccess(_B)
if mibBuilder.loadTexts:staticSntpServerHost.setStatus(_M)
_SntpCurrentSource_Type=MxIpHostNamePort
_SntpCurrentSource_Object=MibScalar
sntpCurrentSource=_SntpCurrentSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,750),_SntpCurrentSource_Type())
sntpCurrentSource.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpCurrentSource.setStatus(_A)
_SntpServersInfoTable_Object=MibTable
sntpServersInfoTable=_SntpServersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,800))
if mibBuilder.loadTexts:sntpServersInfoTable.setStatus(_A)
_SntpServersInfoEntry_Object=MibTableRow
sntpServersInfoEntry=_SntpServersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,800,1))
sntpServersInfoEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:sntpServersInfoEntry.setStatus(_A)
class _SntpServersInfoPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SntpServersInfoPriority_Type.__name__=_F
_SntpServersInfoPriority_Object=MibTableColumn
sntpServersInfoPriority=_SntpServersInfoPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,800,1,100),_SntpServersInfoPriority_Type())
sntpServersInfoPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpServersInfoPriority.setStatus(_A)
class _SntpServersInfoHostName_Type(MxIpHostNamePort):defaultValue=OctetString('')
_SntpServersInfoHostName_Type.__name__=_I
_SntpServersInfoHostName_Object=MibTableColumn
sntpServersInfoHostName=_SntpServersInfoHostName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,800,1,200),_SntpServersInfoHostName_Type())
sntpServersInfoHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:sntpServersInfoHostName.setStatus(_A)
_StaticSntpServersTable_Object=MibTable
staticSntpServersTable=_StaticSntpServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,900))
if mibBuilder.loadTexts:staticSntpServersTable.setStatus(_A)
_StaticSntpServersEntry_Object=MibTableRow
staticSntpServersEntry=_StaticSntpServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,900,1))
staticSntpServersEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:staticSntpServersEntry.setStatus(_A)
class _StaticSntpServersPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_StaticSntpServersPriority_Type.__name__=_F
_StaticSntpServersPriority_Object=MibTableColumn
staticSntpServersPriority=_StaticSntpServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,900,1,100),_StaticSntpServersPriority_Type())
staticSntpServersPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:staticSntpServersPriority.setStatus(_A)
class _StaticSntpServersHostName_Type(MxIpHostNamePort):defaultValue=OctetString('')
_StaticSntpServersHostName_Type.__name__=_I
_StaticSntpServersHostName_Object=MibTableColumn
staticSntpServersHostName=_StaticSntpServersHostName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,400,900,1,200),_StaticSntpServersHostName_Type())
staticSntpServersHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticSntpServersHostName.setStatus(_A)
_DefaultRouterGroup_ObjectIdentity=ObjectIdentity
defaultRouterGroup=_DefaultRouterGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500))
class _DefaultRouterConfigSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_J,100),(_H,200)))
_DefaultRouterConfigSource_Type.__name__=_E
_DefaultRouterConfigSource_Object=MibScalar
defaultRouterConfigSource=_DefaultRouterConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,100),_DefaultRouterConfigSource_Type())
defaultRouterConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultRouterConfigSource.setStatus(_A)
class _DefaultIpv6RouterConfigSource_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(150,200)));namedValues=NamedValues(*((_K,150),(_H,200)))
_DefaultIpv6RouterConfigSource_Type.__name__=_E
_DefaultIpv6RouterConfigSource_Object=MibScalar
defaultIpv6RouterConfigSource=_DefaultIpv6RouterConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,150),_DefaultIpv6RouterConfigSource_Type())
defaultIpv6RouterConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultIpv6RouterConfigSource.setStatus(_A)
_DefaultRouterInfo_Type=MxIpAddr
_DefaultRouterInfo_Object=MibScalar
defaultRouterInfo=_DefaultRouterInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,200),_DefaultRouterInfo_Type())
defaultRouterInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultRouterInfo.setStatus(_A)
_DefaultIpv6RouterInfo_Type=MxIpAddress
_DefaultIpv6RouterInfo_Object=MibScalar
defaultIpv6RouterInfo=_DefaultIpv6RouterInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,250),_DefaultIpv6RouterInfo_Type())
defaultIpv6RouterInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultIpv6RouterInfo.setStatus(_A)
class _StaticDefaultRouter_Type(MxIpAddr):defaultValue=OctetString('192.168.10.10')
_StaticDefaultRouter_Type.__name__=_P
_StaticDefaultRouter_Object=MibScalar
staticDefaultRouter=_StaticDefaultRouter_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,300),_StaticDefaultRouter_Type())
staticDefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:staticDefaultRouter.setStatus(_A)
class _StaticDefaultIpv6Router_Type(MxIpAddress):defaultValue=OctetString('')
_StaticDefaultIpv6Router_Type.__name__=_O
_StaticDefaultIpv6Router_Object=MibScalar
staticDefaultIpv6Router=_StaticDefaultIpv6Router_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,500,350),_StaticDefaultIpv6Router_Type())
staticDefaultIpv6Router.setMaxAccess(_B)
if mibBuilder.loadTexts:staticDefaultIpv6Router.setStatus(_A)
_DnsServersGroup_ObjectIdentity=ObjectIdentity
dnsServersGroup=_DnsServersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600))
class _DnsServersConfigSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,150,200)));namedValues=NamedValues(*((_J,100),(_K,150),(_H,200)))
_DnsServersConfigSource_Type.__name__=_E
_DnsServersConfigSource_Object=MibScalar
dnsServersConfigSource=_DnsServersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,100),_DnsServersConfigSource_Type())
dnsServersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServersConfigSource.setStatus(_A)
class _DnsCacheRandomization_Type(MxEnableState):defaultValue=0
_DnsCacheRandomization_Type.__name__=_N
_DnsCacheRandomization_Object=MibScalar
dnsCacheRandomization=_DnsCacheRandomization_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,150),_DnsCacheRandomization_Type())
dnsCacheRandomization.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsCacheRandomization.setStatus(_A)
_DnsServersInfoTable_Object=MibTable
dnsServersInfoTable=_DnsServersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,200))
if mibBuilder.loadTexts:dnsServersInfoTable.setStatus(_A)
_DnsServersInfoEntry_Object=MibTableRow
dnsServersInfoEntry=_DnsServersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,200,1))
dnsServersInfoEntry.setIndexNames((0,_G,_T))
if mibBuilder.loadTexts:dnsServersInfoEntry.setStatus(_A)
class _DnsServersInfoPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_DnsServersInfoPriority_Type.__name__=_F
_DnsServersInfoPriority_Object=MibTableColumn
dnsServersInfoPriority=_DnsServersInfoPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,200,1,100),_DnsServersInfoPriority_Type())
dnsServersInfoPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoPriority.setStatus(_A)
_DnsServersInfoIpAddress_Type=MxIpAddress
_DnsServersInfoIpAddress_Object=MibTableColumn
dnsServersInfoIpAddress=_DnsServersInfoIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,200,1,200),_DnsServersInfoIpAddress_Type())
dnsServersInfoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoIpAddress.setStatus(_A)
_StaticDnsServersTable_Object=MibTable
staticDnsServersTable=_StaticDnsServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,300))
if mibBuilder.loadTexts:staticDnsServersTable.setStatus(_A)
_StaticDnsServersEntry_Object=MibTableRow
staticDnsServersEntry=_StaticDnsServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,300,1))
staticDnsServersEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:staticDnsServersEntry.setStatus(_A)
class _StaticDnsServersPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_StaticDnsServersPriority_Type.__name__=_F
_StaticDnsServersPriority_Object=MibTableColumn
staticDnsServersPriority=_StaticDnsServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,300,1,100),_StaticDnsServersPriority_Type())
staticDnsServersPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:staticDnsServersPriority.setStatus(_A)
_StaticDnsServersIpAddress_Type=MxIpAddress
_StaticDnsServersIpAddress_Object=MibTableColumn
staticDnsServersIpAddress=_StaticDnsServersIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,600,300,1,200),_StaticDnsServersIpAddress_Type())
staticDnsServersIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:staticDnsServersIpAddress.setStatus(_A)
_HostsGroup_ObjectIdentity=ObjectIdentity
hostsGroup=_HostsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650))
_StaticHostsTable_Object=MibTable
staticHostsTable=_StaticHostsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100))
if mibBuilder.loadTexts:staticHostsTable.setStatus(_A)
_StaticHostsEntry_Object=MibTableRow
staticHostsEntry=_StaticHostsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100,1))
staticHostsEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:staticHostsEntry.setStatus(_A)
_StaticHostsIndex_Type=Unsigned32
_StaticHostsIndex_Object=MibTableColumn
staticHostsIndex=_StaticHostsIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100,1,100),_StaticHostsIndex_Type())
staticHostsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:staticHostsIndex.setStatus(_A)
class _StaticHostsName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_StaticHostsName_Type.__name__=_D
_StaticHostsName_Object=MibTableColumn
staticHostsName=_StaticHostsName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100,1,200),_StaticHostsName_Type())
staticHostsName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticHostsName.setStatus(_A)
class _StaticHostsIpAddresses_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_StaticHostsIpAddresses_Type.__name__=_D
_StaticHostsIpAddresses_Object=MibTableColumn
staticHostsIpAddresses=_StaticHostsIpAddresses_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100,1,300),_StaticHostsIpAddresses_Type())
staticHostsIpAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:staticHostsIpAddresses.setStatus(_A)
class _StaticHostsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_StaticHostsDelete_Type.__name__=_E
_StaticHostsDelete_Object=MibTableColumn
staticHostsDelete=_StaticHostsDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,650,100,1,1000),_StaticHostsDelete_Type())
staticHostsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:staticHostsDelete.setStatus(_A)
_SystemGroup_ObjectIdentity=ObjectIdentity
systemGroup=_SystemGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800))
class _SystemContact_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemContact_Type.__name__=_D
_SystemContact_Object=MibScalar
systemContact=_SystemContact_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800,100),_SystemContact_Type())
systemContact.setMaxAccess(_B)
if mibBuilder.loadTexts:systemContact.setStatus(_A)
class _SystemName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemName_Type.__name__=_D
_SystemName_Object=MibScalar
systemName=_SystemName_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800,200),_SystemName_Type())
systemName.setMaxAccess(_B)
if mibBuilder.loadTexts:systemName.setStatus(_A)
class _SystemLocation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SystemLocation_Type.__name__=_D
_SystemLocation_Object=MibScalar
systemLocation=_SystemLocation_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800,300),_SystemLocation_Type())
systemLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:systemLocation.setStatus(_A)
_HttpClientGroup_ObjectIdentity=ObjectIdentity
httpClientGroup=_HttpClientGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800,1000))
class _HttpUaHeaderFormat_Type(OctetString):defaultValue=OctetString('%product%/v%version% %profile%')
_HttpUaHeaderFormat_Type.__name__=_D
_HttpUaHeaderFormat_Object=MibScalar
httpUaHeaderFormat=_HttpUaHeaderFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,800,1000,100),_HttpUaHeaderFormat_Type())
httpUaHeaderFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:httpUaHeaderFormat.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_E
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,700,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_E
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,700,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hocMIB':hocMIB,'hocMIBObjects':hocMIBObjects,'managementInterface':managementInterface,'automaticConfigurationInterface':automaticConfigurationInterface,'ipv6AutomaticConfigurationInterface':ipv6AutomaticConfigurationInterface,'hostName':hostName,'timeGroup':timeGroup,'systemTime':systemTime,'systemUptime':systemUptime,'staticTimeZone':staticTimeZone,'domainNameGroup':domainNameGroup,'domainNameConfigSource':domainNameConfigSource,'domainNameInfo':domainNameInfo,'staticDomainName':staticDomainName,'sntpGroup':sntpGroup,'sntpConfigSource':sntpConfigSource,'sntpSynchronizationPeriod':sntpSynchronizationPeriod,'sntpSynchronizationPeriodOnError':sntpSynchronizationPeriodOnError,'sntpTimeZone':sntpTimeZone,'sntpServerHostInfo':sntpServerHostInfo,'staticSntpServerHost':staticSntpServerHost,'sntpCurrentSource':sntpCurrentSource,'sntpServersInfoTable':sntpServersInfoTable,'sntpServersInfoEntry':sntpServersInfoEntry,_R:sntpServersInfoPriority,'sntpServersInfoHostName':sntpServersInfoHostName,'staticSntpServersTable':staticSntpServersTable,'staticSntpServersEntry':staticSntpServersEntry,_S:staticSntpServersPriority,'staticSntpServersHostName':staticSntpServersHostName,'defaultRouterGroup':defaultRouterGroup,'defaultRouterConfigSource':defaultRouterConfigSource,'defaultIpv6RouterConfigSource':defaultIpv6RouterConfigSource,'defaultRouterInfo':defaultRouterInfo,'defaultIpv6RouterInfo':defaultIpv6RouterInfo,'staticDefaultRouter':staticDefaultRouter,'staticDefaultIpv6Router':staticDefaultIpv6Router,'dnsServersGroup':dnsServersGroup,'dnsServersConfigSource':dnsServersConfigSource,'dnsCacheRandomization':dnsCacheRandomization,'dnsServersInfoTable':dnsServersInfoTable,'dnsServersInfoEntry':dnsServersInfoEntry,_T:dnsServersInfoPriority,'dnsServersInfoIpAddress':dnsServersInfoIpAddress,'staticDnsServersTable':staticDnsServersTable,'staticDnsServersEntry':staticDnsServersEntry,_U:staticDnsServersPriority,'staticDnsServersIpAddress':staticDnsServersIpAddress,'hostsGroup':hostsGroup,'staticHostsTable':staticHostsTable,'staticHostsEntry':staticHostsEntry,_V:staticHostsIndex,'staticHostsName':staticHostsName,'staticHostsIpAddresses':staticHostsIpAddresses,'staticHostsDelete':staticHostsDelete,'systemGroup':systemGroup,'systemContact':systemContact,'systemName':systemName,'systemLocation':systemLocation,'httpClientGroup':httpClientGroup,'httpUaHeaderFormat':httpUaHeaderFormat,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})