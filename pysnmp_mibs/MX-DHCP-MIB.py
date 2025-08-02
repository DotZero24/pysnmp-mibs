_i='subnetsStatsSubnetName'
_h='specificOption67SubnetName'
_g='specificOption66SubnetName'
_f='assignedLeasesInfoIpAddress'
_e='staticLeasesMacAddress'
_d='nbnsServersInfoSubnetName'
_c='specificNbnsServersSubnetName'
_b='defaultStaticNbnsServersPriority'
_a='ntpServersInfoSubnetName'
_Z='specificNtpServersSubnetName'
_Y='defaultStaticNtpServersPriority'
_X='dnsServersInfoSubnetName'
_W='specificDnsServersSubnetName'
_V='defaultStaticDnsServersPriority'
_U='defaultRoutersInfoSubnetName'
_T='specificDefaultRoutersSubnetName'
_S='leaseTimesInfoSubnetName'
_R='specificLeaseTimesSubnetName'
_Q='domainNamesInfoSubnetName'
_P='specificDomainNamesSubnetName'
_O='delete'
_N='subnetsNetworkInterfaceName'
_M='MxIpHostName'
_L='automatic'
_K='hostConfiguration'
_J='Unsigned32'
_I='OctetString'
_H='static'
_G='Integer32'
_F='MxEnableState'
_E='MxIpAddr'
_D='MX-DHCP-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_F,'MxIpAddress',_M,'MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32',_E,'MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dhcpMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900))
_DhcpMIBObjects_ObjectIdentity=ObjectIdentity
dhcpMIBObjects=_DhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1))
_SubnetsTable_Object=MibTable
subnetsTable=_SubnetsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100))
if mibBuilder.loadTexts:subnetsTable.setStatus(_A)
_SubnetsEntry_Object=MibTableRow
subnetsEntry=_SubnetsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1))
subnetsEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:subnetsEntry.setStatus(_A)
_SubnetsNetworkInterfaceName_Type=OctetString
_SubnetsNetworkInterfaceName_Object=MibTableColumn
subnetsNetworkInterfaceName=_SubnetsNetworkInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,100),_SubnetsNetworkInterfaceName_Type())
subnetsNetworkInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetsNetworkInterfaceName.setStatus(_A)
class _SubnetsEnableSubnet_Type(MxEnableState):defaultValue=0
_SubnetsEnableSubnet_Type.__name__=_F
_SubnetsEnableSubnet_Object=MibTableColumn
subnetsEnableSubnet=_SubnetsEnableSubnet_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,200),_SubnetsEnableSubnet_Type())
subnetsEnableSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetsEnableSubnet.setStatus(_A)
class _SubnetsStartAddress_Type(MxIpAddr):defaultValue=OctetString('')
_SubnetsStartAddress_Type.__name__=_E
_SubnetsStartAddress_Object=MibTableColumn
subnetsStartAddress=_SubnetsStartAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,300),_SubnetsStartAddress_Type())
subnetsStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetsStartAddress.setStatus(_A)
class _SubnetsEndAddress_Type(MxIpAddr):defaultValue=OctetString('')
_SubnetsEndAddress_Type.__name__=_E
_SubnetsEndAddress_Object=MibTableColumn
subnetsEndAddress=_SubnetsEndAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,400),_SubnetsEndAddress_Type())
subnetsEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetsEndAddress.setStatus(_A)
class _SubnetsAutomaticConfigurationInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_SubnetsAutomaticConfigurationInterface_Type.__name__=_I
_SubnetsAutomaticConfigurationInterface_Object=MibTableColumn
subnetsAutomaticConfigurationInterface=_SubnetsAutomaticConfigurationInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,450),_SubnetsAutomaticConfigurationInterface_Type())
subnetsAutomaticConfigurationInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetsAutomaticConfigurationInterface.setStatus(_A)
class _SubnetsConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('disabled',100),('invalidConfig',200),('ok',300)))
_SubnetsConfigStatus_Type.__name__=_G
_SubnetsConfigStatus_Object=MibTableColumn
subnetsConfigStatus=_SubnetsConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,500),_SubnetsConfigStatus_Type())
subnetsConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetsConfigStatus.setStatus(_A)
class _SubnetsDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_O,10)))
_SubnetsDelete_Type.__name__=_G
_SubnetsDelete_Object=MibTableColumn
subnetsDelete=_SubnetsDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,100,1,600),_SubnetsDelete_Type())
subnetsDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetsDelete.setStatus(_A)
_DomainNameGroup_ObjectIdentity=ObjectIdentity
domainNameGroup=_DomainNameGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200))
class _DefaultDomainNameConfigSource_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,400)));namedValues=NamedValues(*((_K,200),(_H,400)))
_DefaultDomainNameConfigSource_Type.__name__=_G
_DefaultDomainNameConfigSource_Object=MibScalar
defaultDomainNameConfigSource=_DefaultDomainNameConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,100),_DefaultDomainNameConfigSource_Type())
defaultDomainNameConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDomainNameConfigSource.setStatus(_A)
class _DefaultStaticDomainName_Type(MxIpHostName):defaultValue=OctetString('')
_DefaultStaticDomainName_Type.__name__=_M
_DefaultStaticDomainName_Object=MibScalar
defaultStaticDomainName=_DefaultStaticDomainName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,200),_DefaultStaticDomainName_Type())
defaultStaticDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticDomainName.setStatus(_A)
_SpecificDomainNamesTable_Object=MibTable
specificDomainNamesTable=_SpecificDomainNamesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300))
if mibBuilder.loadTexts:specificDomainNamesTable.setStatus(_A)
_SpecificDomainNamesEntry_Object=MibTableRow
specificDomainNamesEntry=_SpecificDomainNamesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1))
specificDomainNamesEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:specificDomainNamesEntry.setStatus(_A)
_SpecificDomainNamesSubnetName_Type=OctetString
_SpecificDomainNamesSubnetName_Object=MibTableColumn
specificDomainNamesSubnetName=_SpecificDomainNamesSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1,100),_SpecificDomainNamesSubnetName_Type())
specificDomainNamesSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificDomainNamesSubnetName.setStatus(_A)
class _SpecificDomainNamesEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificDomainNamesEnableConfig_Type.__name__=_F
_SpecificDomainNamesEnableConfig_Object=MibTableColumn
specificDomainNamesEnableConfig=_SpecificDomainNamesEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1,200),_SpecificDomainNamesEnableConfig_Type())
specificDomainNamesEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDomainNamesEnableConfig.setStatus(_A)
class _SpecificDomainNamesEnableOption_Type(MxEnableState):defaultValue=0
_SpecificDomainNamesEnableOption_Type.__name__=_F
_SpecificDomainNamesEnableOption_Object=MibTableColumn
specificDomainNamesEnableOption=_SpecificDomainNamesEnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1,300),_SpecificDomainNamesEnableOption_Type())
specificDomainNamesEnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDomainNamesEnableOption.setStatus(_A)
class _SpecificDomainNamesConfigSource_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,400)));namedValues=NamedValues(*((_K,200),(_H,400)))
_SpecificDomainNamesConfigSource_Type.__name__=_G
_SpecificDomainNamesConfigSource_Object=MibTableColumn
specificDomainNamesConfigSource=_SpecificDomainNamesConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1,400),_SpecificDomainNamesConfigSource_Type())
specificDomainNamesConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDomainNamesConfigSource.setStatus(_A)
class _SpecificDomainNamesStaticName_Type(MxIpHostName):defaultValue=OctetString('')
_SpecificDomainNamesStaticName_Type.__name__=_M
_SpecificDomainNamesStaticName_Object=MibTableColumn
specificDomainNamesStaticName=_SpecificDomainNamesStaticName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,300,1,500),_SpecificDomainNamesStaticName_Type())
specificDomainNamesStaticName.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDomainNamesStaticName.setStatus(_A)
_DomainNamesInfoTable_Object=MibTable
domainNamesInfoTable=_DomainNamesInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,400))
if mibBuilder.loadTexts:domainNamesInfoTable.setStatus(_A)
_DomainNamesInfoEntry_Object=MibTableRow
domainNamesInfoEntry=_DomainNamesInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,400,1))
domainNamesInfoEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:domainNamesInfoEntry.setStatus(_A)
_DomainNamesInfoSubnetName_Type=OctetString
_DomainNamesInfoSubnetName_Object=MibTableColumn
domainNamesInfoSubnetName=_DomainNamesInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,400,1,100),_DomainNamesInfoSubnetName_Type())
domainNamesInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:domainNamesInfoSubnetName.setStatus(_A)
_DomainNamesInfoDomainName_Type=OctetString
_DomainNamesInfoDomainName_Object=MibTableColumn
domainNamesInfoDomainName=_DomainNamesInfoDomainName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,200,400,1,200),_DomainNamesInfoDomainName_Type())
domainNamesInfoDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:domainNamesInfoDomainName.setStatus(_A)
_LeaseTimeGroup_ObjectIdentity=ObjectIdentity
leaseTimeGroup=_LeaseTimeGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300))
class _DefaultLeaseTime_Type(Unsigned32):defaultValue=86400
_DefaultLeaseTime_Type.__name__=_J
_DefaultLeaseTime_Object=MibScalar
defaultLeaseTime=_DefaultLeaseTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,100),_DefaultLeaseTime_Type())
defaultLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultLeaseTime.setStatus(_A)
_SpecificLeaseTimesTable_Object=MibTable
specificLeaseTimesTable=_SpecificLeaseTimesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,200))
if mibBuilder.loadTexts:specificLeaseTimesTable.setStatus(_A)
_SpecificLeaseTimesEntry_Object=MibTableRow
specificLeaseTimesEntry=_SpecificLeaseTimesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,200,1))
specificLeaseTimesEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:specificLeaseTimesEntry.setStatus(_A)
_SpecificLeaseTimesSubnetName_Type=OctetString
_SpecificLeaseTimesSubnetName_Object=MibTableColumn
specificLeaseTimesSubnetName=_SpecificLeaseTimesSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,200,1,100),_SpecificLeaseTimesSubnetName_Type())
specificLeaseTimesSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificLeaseTimesSubnetName.setStatus(_A)
class _SpecificLeaseTimesEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificLeaseTimesEnableConfig_Type.__name__=_F
_SpecificLeaseTimesEnableConfig_Object=MibTableColumn
specificLeaseTimesEnableConfig=_SpecificLeaseTimesEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,200,1,200),_SpecificLeaseTimesEnableConfig_Type())
specificLeaseTimesEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificLeaseTimesEnableConfig.setStatus(_A)
class _SpecificLeaseTimesLeaseTime_Type(Unsigned32):defaultValue=86400
_SpecificLeaseTimesLeaseTime_Type.__name__=_J
_SpecificLeaseTimesLeaseTime_Object=MibTableColumn
specificLeaseTimesLeaseTime=_SpecificLeaseTimesLeaseTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,200,1,300),_SpecificLeaseTimesLeaseTime_Type())
specificLeaseTimesLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:specificLeaseTimesLeaseTime.setStatus(_A)
_LeaseTimesInfoTable_Object=MibTable
leaseTimesInfoTable=_LeaseTimesInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,300))
if mibBuilder.loadTexts:leaseTimesInfoTable.setStatus(_A)
_LeaseTimesInfoEntry_Object=MibTableRow
leaseTimesInfoEntry=_LeaseTimesInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,300,1))
leaseTimesInfoEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:leaseTimesInfoEntry.setStatus(_A)
_LeaseTimesInfoSubnetName_Type=OctetString
_LeaseTimesInfoSubnetName_Object=MibTableColumn
leaseTimesInfoSubnetName=_LeaseTimesInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,300,1,100),_LeaseTimesInfoSubnetName_Type())
leaseTimesInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:leaseTimesInfoSubnetName.setStatus(_A)
_LeaseTimesInfoDefault_Type=Unsigned32
_LeaseTimesInfoDefault_Object=MibTableColumn
leaseTimesInfoDefault=_LeaseTimesInfoDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,300,300,1,200),_LeaseTimesInfoDefault_Type())
leaseTimesInfoDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:leaseTimesInfoDefault.setStatus(_A)
_DefaultRouterGroup_ObjectIdentity=ObjectIdentity
defaultRouterGroup=_DefaultRouterGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400))
_SpecificDefaultRoutersTable_Object=MibTable
specificDefaultRoutersTable=_SpecificDefaultRoutersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100))
if mibBuilder.loadTexts:specificDefaultRoutersTable.setStatus(_A)
_SpecificDefaultRoutersEntry_Object=MibTableRow
specificDefaultRoutersEntry=_SpecificDefaultRoutersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100,1))
specificDefaultRoutersEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:specificDefaultRoutersEntry.setStatus(_A)
_SpecificDefaultRoutersSubnetName_Type=OctetString
_SpecificDefaultRoutersSubnetName_Object=MibTableColumn
specificDefaultRoutersSubnetName=_SpecificDefaultRoutersSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100,1,100),_SpecificDefaultRoutersSubnetName_Type())
specificDefaultRoutersSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificDefaultRoutersSubnetName.setStatus(_A)
class _SpecificDefaultRoutersEnableOption_Type(MxEnableState):defaultValue=1
_SpecificDefaultRoutersEnableOption_Type.__name__=_F
_SpecificDefaultRoutersEnableOption_Object=MibTableColumn
specificDefaultRoutersEnableOption=_SpecificDefaultRoutersEnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100,1,200),_SpecificDefaultRoutersEnableOption_Type())
specificDefaultRoutersEnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDefaultRoutersEnableOption.setStatus(_A)
class _SpecificDefaultRoutersConfigSource_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,400)));namedValues=NamedValues(*(('hostInterface',100),(_H,400)))
_SpecificDefaultRoutersConfigSource_Type.__name__=_G
_SpecificDefaultRoutersConfigSource_Object=MibTableColumn
specificDefaultRoutersConfigSource=_SpecificDefaultRoutersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100,1,300),_SpecificDefaultRoutersConfigSource_Type())
specificDefaultRoutersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDefaultRoutersConfigSource.setStatus(_A)
class _SpecificDefaultRoutersStaticRouter_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificDefaultRoutersStaticRouter_Type.__name__=_E
_SpecificDefaultRoutersStaticRouter_Object=MibTableColumn
specificDefaultRoutersStaticRouter=_SpecificDefaultRoutersStaticRouter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,100,1,400),_SpecificDefaultRoutersStaticRouter_Type())
specificDefaultRoutersStaticRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDefaultRoutersStaticRouter.setStatus(_A)
_DefaultRoutersInfoTable_Object=MibTable
defaultRoutersInfoTable=_DefaultRoutersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,200))
if mibBuilder.loadTexts:defaultRoutersInfoTable.setStatus(_A)
_DefaultRoutersInfoEntry_Object=MibTableRow
defaultRoutersInfoEntry=_DefaultRoutersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,200,1))
defaultRoutersInfoEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:defaultRoutersInfoEntry.setStatus(_A)
_DefaultRoutersInfoSubnetName_Type=OctetString
_DefaultRoutersInfoSubnetName_Object=MibTableColumn
defaultRoutersInfoSubnetName=_DefaultRoutersInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,200,1,100),_DefaultRoutersInfoSubnetName_Type())
defaultRoutersInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultRoutersInfoSubnetName.setStatus(_A)
_DefaultRoutersInfoDefaultRouter_Type=MxIpAddr
_DefaultRoutersInfoDefaultRouter_Object=MibTableColumn
defaultRoutersInfoDefaultRouter=_DefaultRoutersInfoDefaultRouter_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,400,200,1,200),_DefaultRoutersInfoDefaultRouter_Type())
defaultRoutersInfoDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultRoutersInfoDefaultRouter.setStatus(_A)
_DnsServersGroup_ObjectIdentity=ObjectIdentity
dnsServersGroup=_DnsServersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500))
class _DefaultDnsServersConfigSource_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400)));namedValues=NamedValues(*((_K,200),(_L,300),(_H,400)))
_DefaultDnsServersConfigSource_Type.__name__=_G
_DefaultDnsServersConfigSource_Object=MibScalar
defaultDnsServersConfigSource=_DefaultDnsServersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,100),_DefaultDnsServersConfigSource_Type())
defaultDnsServersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultDnsServersConfigSource.setStatus(_A)
_DefaultStaticDnsServersTable_Object=MibTable
defaultStaticDnsServersTable=_DefaultStaticDnsServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,200))
if mibBuilder.loadTexts:defaultStaticDnsServersTable.setStatus(_A)
_DefaultStaticDnsServersEntry_Object=MibTableRow
defaultStaticDnsServersEntry=_DefaultStaticDnsServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,200,1))
defaultStaticDnsServersEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:defaultStaticDnsServersEntry.setStatus(_A)
class _DefaultStaticDnsServersPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_DefaultStaticDnsServersPriority_Type.__name__=_J
_DefaultStaticDnsServersPriority_Object=MibTableColumn
defaultStaticDnsServersPriority=_DefaultStaticDnsServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,200,1,100),_DefaultStaticDnsServersPriority_Type())
defaultStaticDnsServersPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultStaticDnsServersPriority.setStatus(_A)
_DefaultStaticDnsServersIpAddress_Type=MxIpAddr
_DefaultStaticDnsServersIpAddress_Object=MibTableColumn
defaultStaticDnsServersIpAddress=_DefaultStaticDnsServersIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,200,1,200),_DefaultStaticDnsServersIpAddress_Type())
defaultStaticDnsServersIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticDnsServersIpAddress.setStatus(_A)
_SpecificDnsServersTable_Object=MibTable
specificDnsServersTable=_SpecificDnsServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300))
if mibBuilder.loadTexts:specificDnsServersTable.setStatus(_A)
_SpecificDnsServersEntry_Object=MibTableRow
specificDnsServersEntry=_SpecificDnsServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1))
specificDnsServersEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:specificDnsServersEntry.setStatus(_A)
_SpecificDnsServersSubnetName_Type=OctetString
_SpecificDnsServersSubnetName_Object=MibTableColumn
specificDnsServersSubnetName=_SpecificDnsServersSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,100),_SpecificDnsServersSubnetName_Type())
specificDnsServersSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificDnsServersSubnetName.setStatus(_A)
class _SpecificDnsServersEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificDnsServersEnableConfig_Type.__name__=_F
_SpecificDnsServersEnableConfig_Object=MibTableColumn
specificDnsServersEnableConfig=_SpecificDnsServersEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,200),_SpecificDnsServersEnableConfig_Type())
specificDnsServersEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersEnableConfig.setStatus(_A)
class _SpecificDnsServersEnableOption_Type(MxEnableState):defaultValue=1
_SpecificDnsServersEnableOption_Type.__name__=_F
_SpecificDnsServersEnableOption_Object=MibTableColumn
specificDnsServersEnableOption=_SpecificDnsServersEnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,300),_SpecificDnsServersEnableOption_Type())
specificDnsServersEnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersEnableOption.setStatus(_A)
class _SpecificDnsServersConfigSource_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400)));namedValues=NamedValues(*((_K,200),(_L,300),(_H,400)))
_SpecificDnsServersConfigSource_Type.__name__=_G
_SpecificDnsServersConfigSource_Object=MibTableColumn
specificDnsServersConfigSource=_SpecificDnsServersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,400),_SpecificDnsServersConfigSource_Type())
specificDnsServersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersConfigSource.setStatus(_A)
class _SpecificDnsServersStaticDns1_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificDnsServersStaticDns1_Type.__name__=_E
_SpecificDnsServersStaticDns1_Object=MibTableColumn
specificDnsServersStaticDns1=_SpecificDnsServersStaticDns1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,500),_SpecificDnsServersStaticDns1_Type())
specificDnsServersStaticDns1.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersStaticDns1.setStatus(_A)
class _SpecificDnsServersStaticDns2_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificDnsServersStaticDns2_Type.__name__=_E
_SpecificDnsServersStaticDns2_Object=MibTableColumn
specificDnsServersStaticDns2=_SpecificDnsServersStaticDns2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,600),_SpecificDnsServersStaticDns2_Type())
specificDnsServersStaticDns2.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersStaticDns2.setStatus(_A)
class _SpecificDnsServersStaticDns3_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificDnsServersStaticDns3_Type.__name__=_E
_SpecificDnsServersStaticDns3_Object=MibTableColumn
specificDnsServersStaticDns3=_SpecificDnsServersStaticDns3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,700),_SpecificDnsServersStaticDns3_Type())
specificDnsServersStaticDns3.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersStaticDns3.setStatus(_A)
class _SpecificDnsServersStaticDns4_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificDnsServersStaticDns4_Type.__name__=_E
_SpecificDnsServersStaticDns4_Object=MibTableColumn
specificDnsServersStaticDns4=_SpecificDnsServersStaticDns4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,300,1,800),_SpecificDnsServersStaticDns4_Type())
specificDnsServersStaticDns4.setMaxAccess(_B)
if mibBuilder.loadTexts:specificDnsServersStaticDns4.setStatus(_A)
_DnsServersInfoTable_Object=MibTable
dnsServersInfoTable=_DnsServersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400))
if mibBuilder.loadTexts:dnsServersInfoTable.setStatus(_A)
_DnsServersInfoEntry_Object=MibTableRow
dnsServersInfoEntry=_DnsServersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1))
dnsServersInfoEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:dnsServersInfoEntry.setStatus(_A)
_DnsServersInfoSubnetName_Type=OctetString
_DnsServersInfoSubnetName_Object=MibTableColumn
dnsServersInfoSubnetName=_DnsServersInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1,100),_DnsServersInfoSubnetName_Type())
dnsServersInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoSubnetName.setStatus(_A)
_DnsServersInfoDns1_Type=MxIpAddr
_DnsServersInfoDns1_Object=MibTableColumn
dnsServersInfoDns1=_DnsServersInfoDns1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1,200),_DnsServersInfoDns1_Type())
dnsServersInfoDns1.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoDns1.setStatus(_A)
_DnsServersInfoDns2_Type=MxIpAddr
_DnsServersInfoDns2_Object=MibTableColumn
dnsServersInfoDns2=_DnsServersInfoDns2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1,300),_DnsServersInfoDns2_Type())
dnsServersInfoDns2.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoDns2.setStatus(_A)
_DnsServersInfoDns3_Type=MxIpAddr
_DnsServersInfoDns3_Object=MibTableColumn
dnsServersInfoDns3=_DnsServersInfoDns3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1,400),_DnsServersInfoDns3_Type())
dnsServersInfoDns3.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoDns3.setStatus(_A)
_DnsServersInfoDns4_Type=MxIpAddr
_DnsServersInfoDns4_Object=MibTableColumn
dnsServersInfoDns4=_DnsServersInfoDns4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,500,400,1,500),_DnsServersInfoDns4_Type())
dnsServersInfoDns4.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServersInfoDns4.setStatus(_A)
_NtpServersGroup_ObjectIdentity=ObjectIdentity
ntpServersGroup=_NtpServersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600))
class _DefaultNtpServersConfigSource_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400)));namedValues=NamedValues(*((_K,200),(_L,300),(_H,400)))
_DefaultNtpServersConfigSource_Type.__name__=_G
_DefaultNtpServersConfigSource_Object=MibScalar
defaultNtpServersConfigSource=_DefaultNtpServersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,100),_DefaultNtpServersConfigSource_Type())
defaultNtpServersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultNtpServersConfigSource.setStatus(_A)
_DefaultStaticNtpServersTable_Object=MibTable
defaultStaticNtpServersTable=_DefaultStaticNtpServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,200))
if mibBuilder.loadTexts:defaultStaticNtpServersTable.setStatus(_A)
_DefaultStaticNtpServersEntry_Object=MibTableRow
defaultStaticNtpServersEntry=_DefaultStaticNtpServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,200,1))
defaultStaticNtpServersEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:defaultStaticNtpServersEntry.setStatus(_A)
class _DefaultStaticNtpServersPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_DefaultStaticNtpServersPriority_Type.__name__=_J
_DefaultStaticNtpServersPriority_Object=MibTableColumn
defaultStaticNtpServersPriority=_DefaultStaticNtpServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,200,1,100),_DefaultStaticNtpServersPriority_Type())
defaultStaticNtpServersPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultStaticNtpServersPriority.setStatus(_A)
_DefaultStaticNtpServersIpAddress_Type=MxIpAddr
_DefaultStaticNtpServersIpAddress_Object=MibTableColumn
defaultStaticNtpServersIpAddress=_DefaultStaticNtpServersIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,200,1,200),_DefaultStaticNtpServersIpAddress_Type())
defaultStaticNtpServersIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticNtpServersIpAddress.setStatus(_A)
_SpecificNtpServersTable_Object=MibTable
specificNtpServersTable=_SpecificNtpServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300))
if mibBuilder.loadTexts:specificNtpServersTable.setStatus(_A)
_SpecificNtpServersEntry_Object=MibTableRow
specificNtpServersEntry=_SpecificNtpServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1))
specificNtpServersEntry.setIndexNames((0,_D,_Z))
if mibBuilder.loadTexts:specificNtpServersEntry.setStatus(_A)
_SpecificNtpServersSubnetName_Type=OctetString
_SpecificNtpServersSubnetName_Object=MibTableColumn
specificNtpServersSubnetName=_SpecificNtpServersSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,100),_SpecificNtpServersSubnetName_Type())
specificNtpServersSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificNtpServersSubnetName.setStatus(_A)
class _SpecificNtpServersEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificNtpServersEnableConfig_Type.__name__=_F
_SpecificNtpServersEnableConfig_Object=MibTableColumn
specificNtpServersEnableConfig=_SpecificNtpServersEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,200),_SpecificNtpServersEnableConfig_Type())
specificNtpServersEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersEnableConfig.setStatus(_A)
class _SpecificNtpServersEnableOption_Type(MxEnableState):defaultValue=0
_SpecificNtpServersEnableOption_Type.__name__=_F
_SpecificNtpServersEnableOption_Object=MibTableColumn
specificNtpServersEnableOption=_SpecificNtpServersEnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,300),_SpecificNtpServersEnableOption_Type())
specificNtpServersEnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersEnableOption.setStatus(_A)
class _SpecificNtpServersConfigSource_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,300,400)));namedValues=NamedValues(*((_K,200),(_L,300),(_H,400)))
_SpecificNtpServersConfigSource_Type.__name__=_G
_SpecificNtpServersConfigSource_Object=MibTableColumn
specificNtpServersConfigSource=_SpecificNtpServersConfigSource_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,400),_SpecificNtpServersConfigSource_Type())
specificNtpServersConfigSource.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersConfigSource.setStatus(_A)
class _SpecificNtpServersStaticNtp1_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNtpServersStaticNtp1_Type.__name__=_E
_SpecificNtpServersStaticNtp1_Object=MibTableColumn
specificNtpServersStaticNtp1=_SpecificNtpServersStaticNtp1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,500),_SpecificNtpServersStaticNtp1_Type())
specificNtpServersStaticNtp1.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersStaticNtp1.setStatus(_A)
class _SpecificNtpServersStaticNtp2_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNtpServersStaticNtp2_Type.__name__=_E
_SpecificNtpServersStaticNtp2_Object=MibTableColumn
specificNtpServersStaticNtp2=_SpecificNtpServersStaticNtp2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,600),_SpecificNtpServersStaticNtp2_Type())
specificNtpServersStaticNtp2.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersStaticNtp2.setStatus(_A)
class _SpecificNtpServersStaticNtp3_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNtpServersStaticNtp3_Type.__name__=_E
_SpecificNtpServersStaticNtp3_Object=MibTableColumn
specificNtpServersStaticNtp3=_SpecificNtpServersStaticNtp3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,700),_SpecificNtpServersStaticNtp3_Type())
specificNtpServersStaticNtp3.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersStaticNtp3.setStatus(_A)
class _SpecificNtpServersStaticNtp4_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNtpServersStaticNtp4_Type.__name__=_E
_SpecificNtpServersStaticNtp4_Object=MibTableColumn
specificNtpServersStaticNtp4=_SpecificNtpServersStaticNtp4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,300,1,800),_SpecificNtpServersStaticNtp4_Type())
specificNtpServersStaticNtp4.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNtpServersStaticNtp4.setStatus(_A)
_NtpServersInfoTable_Object=MibTable
ntpServersInfoTable=_NtpServersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400))
if mibBuilder.loadTexts:ntpServersInfoTable.setStatus(_A)
_NtpServersInfoEntry_Object=MibTableRow
ntpServersInfoEntry=_NtpServersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1))
ntpServersInfoEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:ntpServersInfoEntry.setStatus(_A)
_NtpServersInfoSubnetName_Type=OctetString
_NtpServersInfoSubnetName_Object=MibTableColumn
ntpServersInfoSubnetName=_NtpServersInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1,100),_NtpServersInfoSubnetName_Type())
ntpServersInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServersInfoSubnetName.setStatus(_A)
_NtpServersInfoNtp1_Type=MxIpAddr
_NtpServersInfoNtp1_Object=MibTableColumn
ntpServersInfoNtp1=_NtpServersInfoNtp1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1,200),_NtpServersInfoNtp1_Type())
ntpServersInfoNtp1.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServersInfoNtp1.setStatus(_A)
_NtpServersInfoNtp2_Type=MxIpAddr
_NtpServersInfoNtp2_Object=MibTableColumn
ntpServersInfoNtp2=_NtpServersInfoNtp2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1,300),_NtpServersInfoNtp2_Type())
ntpServersInfoNtp2.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServersInfoNtp2.setStatus(_A)
_NtpServersInfoNtp3_Type=MxIpAddr
_NtpServersInfoNtp3_Object=MibTableColumn
ntpServersInfoNtp3=_NtpServersInfoNtp3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1,400),_NtpServersInfoNtp3_Type())
ntpServersInfoNtp3.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServersInfoNtp3.setStatus(_A)
_NtpServersInfoNtp4_Type=MxIpAddr
_NtpServersInfoNtp4_Object=MibTableColumn
ntpServersInfoNtp4=_NtpServersInfoNtp4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,600,400,1,500),_NtpServersInfoNtp4_Type())
ntpServersInfoNtp4.setMaxAccess(_C)
if mibBuilder.loadTexts:ntpServersInfoNtp4.setStatus(_A)
_NbnsServersGroup_ObjectIdentity=ObjectIdentity
nbnsServersGroup=_NbnsServersGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700))
_DefaultStaticNbnsServersTable_Object=MibTable
defaultStaticNbnsServersTable=_DefaultStaticNbnsServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,100))
if mibBuilder.loadTexts:defaultStaticNbnsServersTable.setStatus(_A)
_DefaultStaticNbnsServersEntry_Object=MibTableRow
defaultStaticNbnsServersEntry=_DefaultStaticNbnsServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,100,1))
defaultStaticNbnsServersEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:defaultStaticNbnsServersEntry.setStatus(_A)
class _DefaultStaticNbnsServersPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_DefaultStaticNbnsServersPriority_Type.__name__=_J
_DefaultStaticNbnsServersPriority_Object=MibTableColumn
defaultStaticNbnsServersPriority=_DefaultStaticNbnsServersPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,100,1,100),_DefaultStaticNbnsServersPriority_Type())
defaultStaticNbnsServersPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:defaultStaticNbnsServersPriority.setStatus(_A)
_DefaultStaticNbnsServersIpAddress_Type=MxIpAddr
_DefaultStaticNbnsServersIpAddress_Object=MibTableColumn
defaultStaticNbnsServersIpAddress=_DefaultStaticNbnsServersIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,100,1,200),_DefaultStaticNbnsServersIpAddress_Type())
defaultStaticNbnsServersIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticNbnsServersIpAddress.setStatus(_A)
_SpecificNbnsServersTable_Object=MibTable
specificNbnsServersTable=_SpecificNbnsServersTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200))
if mibBuilder.loadTexts:specificNbnsServersTable.setStatus(_A)
_SpecificNbnsServersEntry_Object=MibTableRow
specificNbnsServersEntry=_SpecificNbnsServersEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1))
specificNbnsServersEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:specificNbnsServersEntry.setStatus(_A)
_SpecificNbnsServersSubnetName_Type=OctetString
_SpecificNbnsServersSubnetName_Object=MibTableColumn
specificNbnsServersSubnetName=_SpecificNbnsServersSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,100),_SpecificNbnsServersSubnetName_Type())
specificNbnsServersSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificNbnsServersSubnetName.setStatus(_A)
class _SpecificNbnsServersEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificNbnsServersEnableConfig_Type.__name__=_F
_SpecificNbnsServersEnableConfig_Object=MibTableColumn
specificNbnsServersEnableConfig=_SpecificNbnsServersEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,200),_SpecificNbnsServersEnableConfig_Type())
specificNbnsServersEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersEnableConfig.setStatus(_A)
class _SpecificNbnsServersEnableOption_Type(MxEnableState):defaultValue=0
_SpecificNbnsServersEnableOption_Type.__name__=_F
_SpecificNbnsServersEnableOption_Object=MibTableColumn
specificNbnsServersEnableOption=_SpecificNbnsServersEnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,300),_SpecificNbnsServersEnableOption_Type())
specificNbnsServersEnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersEnableOption.setStatus(_A)
class _SpecificNbnsServersStaticNbns1_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNbnsServersStaticNbns1_Type.__name__=_E
_SpecificNbnsServersStaticNbns1_Object=MibTableColumn
specificNbnsServersStaticNbns1=_SpecificNbnsServersStaticNbns1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,400),_SpecificNbnsServersStaticNbns1_Type())
specificNbnsServersStaticNbns1.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersStaticNbns1.setStatus(_A)
class _SpecificNbnsServersStaticNbns2_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNbnsServersStaticNbns2_Type.__name__=_E
_SpecificNbnsServersStaticNbns2_Object=MibTableColumn
specificNbnsServersStaticNbns2=_SpecificNbnsServersStaticNbns2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,500),_SpecificNbnsServersStaticNbns2_Type())
specificNbnsServersStaticNbns2.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersStaticNbns2.setStatus(_A)
class _SpecificNbnsServersStaticNbns3_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNbnsServersStaticNbns3_Type.__name__=_E
_SpecificNbnsServersStaticNbns3_Object=MibTableColumn
specificNbnsServersStaticNbns3=_SpecificNbnsServersStaticNbns3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,600),_SpecificNbnsServersStaticNbns3_Type())
specificNbnsServersStaticNbns3.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersStaticNbns3.setStatus(_A)
class _SpecificNbnsServersStaticNbns4_Type(MxIpAddr):defaultValue=OctetString('')
_SpecificNbnsServersStaticNbns4_Type.__name__=_E
_SpecificNbnsServersStaticNbns4_Object=MibTableColumn
specificNbnsServersStaticNbns4=_SpecificNbnsServersStaticNbns4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,200,1,700),_SpecificNbnsServersStaticNbns4_Type())
specificNbnsServersStaticNbns4.setMaxAccess(_B)
if mibBuilder.loadTexts:specificNbnsServersStaticNbns4.setStatus(_A)
_NbnsServersInfoTable_Object=MibTable
nbnsServersInfoTable=_NbnsServersInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300))
if mibBuilder.loadTexts:nbnsServersInfoTable.setStatus(_A)
_NbnsServersInfoEntry_Object=MibTableRow
nbnsServersInfoEntry=_NbnsServersInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1))
nbnsServersInfoEntry.setIndexNames((0,_D,_d))
if mibBuilder.loadTexts:nbnsServersInfoEntry.setStatus(_A)
_NbnsServersInfoSubnetName_Type=OctetString
_NbnsServersInfoSubnetName_Object=MibTableColumn
nbnsServersInfoSubnetName=_NbnsServersInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1,100),_NbnsServersInfoSubnetName_Type())
nbnsServersInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:nbnsServersInfoSubnetName.setStatus(_A)
_NbnsServersInfoNbns1_Type=MxIpAddr
_NbnsServersInfoNbns1_Object=MibTableColumn
nbnsServersInfoNbns1=_NbnsServersInfoNbns1_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1,200),_NbnsServersInfoNbns1_Type())
nbnsServersInfoNbns1.setMaxAccess(_C)
if mibBuilder.loadTexts:nbnsServersInfoNbns1.setStatus(_A)
_NbnsServersInfoNbns2_Type=MxIpAddr
_NbnsServersInfoNbns2_Object=MibTableColumn
nbnsServersInfoNbns2=_NbnsServersInfoNbns2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1,300),_NbnsServersInfoNbns2_Type())
nbnsServersInfoNbns2.setMaxAccess(_C)
if mibBuilder.loadTexts:nbnsServersInfoNbns2.setStatus(_A)
_NbnsServersInfoNbns3_Type=MxIpAddr
_NbnsServersInfoNbns3_Object=MibTableColumn
nbnsServersInfoNbns3=_NbnsServersInfoNbns3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1,400),_NbnsServersInfoNbns3_Type())
nbnsServersInfoNbns3.setMaxAccess(_C)
if mibBuilder.loadTexts:nbnsServersInfoNbns3.setStatus(_A)
_NbnsServersInfoNbns4_Type=MxIpAddr
_NbnsServersInfoNbns4_Object=MibTableColumn
nbnsServersInfoNbns4=_NbnsServersInfoNbns4_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,700,300,1,500),_NbnsServersInfoNbns4_Type())
nbnsServersInfoNbns4.setMaxAccess(_C)
if mibBuilder.loadTexts:nbnsServersInfoNbns4.setStatus(_A)
_StaticLeasesTable_Object=MibTable
staticLeasesTable=_StaticLeasesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,800))
if mibBuilder.loadTexts:staticLeasesTable.setStatus(_A)
_StaticLeasesEntry_Object=MibTableRow
staticLeasesEntry=_StaticLeasesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,800,1))
staticLeasesEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:staticLeasesEntry.setStatus(_A)
_StaticLeasesMacAddress_Type=OctetString
_StaticLeasesMacAddress_Object=MibTableColumn
staticLeasesMacAddress=_StaticLeasesMacAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,800,1,100),_StaticLeasesMacAddress_Type())
staticLeasesMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:staticLeasesMacAddress.setStatus(_A)
class _StaticLeasesIpAddress_Type(MxIpAddr):defaultValue=OctetString('')
_StaticLeasesIpAddress_Type.__name__=_E
_StaticLeasesIpAddress_Object=MibTableColumn
staticLeasesIpAddress=_StaticLeasesIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,800,1,200),_StaticLeasesIpAddress_Type())
staticLeasesIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:staticLeasesIpAddress.setStatus(_A)
class _StaticLeasesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),(_O,10)))
_StaticLeasesDelete_Type.__name__=_G
_StaticLeasesDelete_Object=MibTableColumn
staticLeasesDelete=_StaticLeasesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,800,1,300),_StaticLeasesDelete_Type())
staticLeasesDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:staticLeasesDelete.setStatus(_A)
_AssignedLeasesInfoTable_Object=MibTable
assignedLeasesInfoTable=_AssignedLeasesInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900))
if mibBuilder.loadTexts:assignedLeasesInfoTable.setStatus(_A)
_AssignedLeasesInfoEntry_Object=MibTableRow
assignedLeasesInfoEntry=_AssignedLeasesInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900,1))
assignedLeasesInfoEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:assignedLeasesInfoEntry.setStatus(_A)
_AssignedLeasesInfoIpAddress_Type=MxIpAddr
_AssignedLeasesInfoIpAddress_Object=MibTableColumn
assignedLeasesInfoIpAddress=_AssignedLeasesInfoIpAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900,1,100),_AssignedLeasesInfoIpAddress_Type())
assignedLeasesInfoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:assignedLeasesInfoIpAddress.setStatus(_A)
_AssignedLeasesInfoMacAddress_Type=OctetString
_AssignedLeasesInfoMacAddress_Object=MibTableColumn
assignedLeasesInfoMacAddress=_AssignedLeasesInfoMacAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900,1,200),_AssignedLeasesInfoMacAddress_Type())
assignedLeasesInfoMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:assignedLeasesInfoMacAddress.setStatus(_A)
_AssignedLeasesInfoSubnetName_Type=OctetString
_AssignedLeasesInfoSubnetName_Object=MibTableColumn
assignedLeasesInfoSubnetName=_AssignedLeasesInfoSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900,1,300),_AssignedLeasesInfoSubnetName_Type())
assignedLeasesInfoSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:assignedLeasesInfoSubnetName.setStatus(_A)
_AssignedLeasesInfoLeaseTimeLeft_Type=Unsigned32
_AssignedLeasesInfoLeaseTimeLeft_Object=MibTableColumn
assignedLeasesInfoLeaseTimeLeft=_AssignedLeasesInfoLeaseTimeLeft_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,900,1,400),_AssignedLeasesInfoLeaseTimeLeft_Type())
assignedLeasesInfoLeaseTimeLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:assignedLeasesInfoLeaseTimeLeft.setStatus(_A)
_ProvisioningGroup_ObjectIdentity=ObjectIdentity
provisioningGroup=_ProvisioningGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000))
class _DefaultStaticOption66_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_DefaultStaticOption66_Type.__name__=_I
_DefaultStaticOption66_Object=MibScalar
defaultStaticOption66=_DefaultStaticOption66_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,100),_DefaultStaticOption66_Type())
defaultStaticOption66.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticOption66.setStatus(_A)
class _DefaultStaticOption67_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_DefaultStaticOption67_Type.__name__=_I
_DefaultStaticOption67_Object=MibScalar
defaultStaticOption67=_DefaultStaticOption67_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,200),_DefaultStaticOption67_Type())
defaultStaticOption67.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultStaticOption67.setStatus(_A)
_SpecificOption66Table_Object=MibTable
specificOption66Table=_SpecificOption66Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000))
if mibBuilder.loadTexts:specificOption66Table.setStatus(_A)
_SpecificOption66Entry_Object=MibTableRow
specificOption66Entry=_SpecificOption66Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000,1))
specificOption66Entry.setIndexNames((0,_D,_g))
if mibBuilder.loadTexts:specificOption66Entry.setStatus(_A)
_SpecificOption66SubnetName_Type=OctetString
_SpecificOption66SubnetName_Object=MibTableColumn
specificOption66SubnetName=_SpecificOption66SubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000,1,100),_SpecificOption66SubnetName_Type())
specificOption66SubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificOption66SubnetName.setStatus(_A)
class _SpecificOption66EnableConfig_Type(MxEnableState):defaultValue=0
_SpecificOption66EnableConfig_Type.__name__=_F
_SpecificOption66EnableConfig_Object=MibTableColumn
specificOption66EnableConfig=_SpecificOption66EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000,1,200),_SpecificOption66EnableConfig_Type())
specificOption66EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption66EnableConfig.setStatus(_A)
class _SpecificOption66EnableOption_Type(MxEnableState):defaultValue=0
_SpecificOption66EnableOption_Type.__name__=_F
_SpecificOption66EnableOption_Object=MibTableColumn
specificOption66EnableOption=_SpecificOption66EnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000,1,300),_SpecificOption66EnableOption_Type())
specificOption66EnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption66EnableOption.setStatus(_A)
class _SpecificOption66Value_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_SpecificOption66Value_Type.__name__=_I
_SpecificOption66Value_Object=MibTableColumn
specificOption66Value=_SpecificOption66Value_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1000,1,400),_SpecificOption66Value_Type())
specificOption66Value.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption66Value.setStatus(_A)
_SpecificOption67Table_Object=MibTable
specificOption67Table=_SpecificOption67Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100))
if mibBuilder.loadTexts:specificOption67Table.setStatus(_A)
_SpecificOption67Entry_Object=MibTableRow
specificOption67Entry=_SpecificOption67Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100,1))
specificOption67Entry.setIndexNames((0,_D,_h))
if mibBuilder.loadTexts:specificOption67Entry.setStatus(_A)
_SpecificOption67SubnetName_Type=OctetString
_SpecificOption67SubnetName_Object=MibTableColumn
specificOption67SubnetName=_SpecificOption67SubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100,1,100),_SpecificOption67SubnetName_Type())
specificOption67SubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:specificOption67SubnetName.setStatus(_A)
class _SpecificOption67EnableConfig_Type(MxEnableState):defaultValue=0
_SpecificOption67EnableConfig_Type.__name__=_F
_SpecificOption67EnableConfig_Object=MibTableColumn
specificOption67EnableConfig=_SpecificOption67EnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100,1,200),_SpecificOption67EnableConfig_Type())
specificOption67EnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption67EnableConfig.setStatus(_A)
class _SpecificOption67EnableOption_Type(MxEnableState):defaultValue=0
_SpecificOption67EnableOption_Type.__name__=_F
_SpecificOption67EnableOption_Object=MibTableColumn
specificOption67EnableOption=_SpecificOption67EnableOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100,1,300),_SpecificOption67EnableOption_Type())
specificOption67EnableOption.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption67EnableOption.setStatus(_A)
class _SpecificOption67Value_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_SpecificOption67Value_Type.__name__=_I
_SpecificOption67Value_Object=MibTableColumn
specificOption67Value=_SpecificOption67Value_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,1000,1100,1,400),_SpecificOption67Value_Type())
specificOption67Value.setMaxAccess(_B)
if mibBuilder.loadTexts:specificOption67Value.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,10000))
_SubnetsStatsTable_Object=MibTable
subnetsStatsTable=_SubnetsStatsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,10000,100))
if mibBuilder.loadTexts:subnetsStatsTable.setStatus(_A)
_SubnetsStatsEntry_Object=MibTableRow
subnetsStatsEntry=_SubnetsStatsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,10000,100,1))
subnetsStatsEntry.setIndexNames((0,_D,_i))
if mibBuilder.loadTexts:subnetsStatsEntry.setStatus(_A)
_SubnetsStatsSubnetName_Type=OctetString
_SubnetsStatsSubnetName_Object=MibTableColumn
subnetsStatsSubnetName=_SubnetsStatsSubnetName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,10000,100,1,100),_SubnetsStatsSubnetName_Type())
subnetsStatsSubnetName.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetsStatsSubnetName.setStatus(_A)
_SubnetsStatsNumberOfLeases_Type=Unsigned32
_SubnetsStatsNumberOfLeases_Object=MibTableColumn
subnetsStatsNumberOfLeases=_SubnetsStatsNumberOfLeases_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,10000,100,1,200),_SubnetsStatsNumberOfLeases_Type())
subnetsStatsNumberOfLeases.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetsStatsNumberOfLeases.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_G
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_G
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1900,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'dhcpMIB':dhcpMIB,'dhcpMIBObjects':dhcpMIBObjects,'subnetsTable':subnetsTable,'subnetsEntry':subnetsEntry,_N:subnetsNetworkInterfaceName,'subnetsEnableSubnet':subnetsEnableSubnet,'subnetsStartAddress':subnetsStartAddress,'subnetsEndAddress':subnetsEndAddress,'subnetsAutomaticConfigurationInterface':subnetsAutomaticConfigurationInterface,'subnetsConfigStatus':subnetsConfigStatus,'subnetsDelete':subnetsDelete,'domainNameGroup':domainNameGroup,'defaultDomainNameConfigSource':defaultDomainNameConfigSource,'defaultStaticDomainName':defaultStaticDomainName,'specificDomainNamesTable':specificDomainNamesTable,'specificDomainNamesEntry':specificDomainNamesEntry,_P:specificDomainNamesSubnetName,'specificDomainNamesEnableConfig':specificDomainNamesEnableConfig,'specificDomainNamesEnableOption':specificDomainNamesEnableOption,'specificDomainNamesConfigSource':specificDomainNamesConfigSource,'specificDomainNamesStaticName':specificDomainNamesStaticName,'domainNamesInfoTable':domainNamesInfoTable,'domainNamesInfoEntry':domainNamesInfoEntry,_Q:domainNamesInfoSubnetName,'domainNamesInfoDomainName':domainNamesInfoDomainName,'leaseTimeGroup':leaseTimeGroup,'defaultLeaseTime':defaultLeaseTime,'specificLeaseTimesTable':specificLeaseTimesTable,'specificLeaseTimesEntry':specificLeaseTimesEntry,_R:specificLeaseTimesSubnetName,'specificLeaseTimesEnableConfig':specificLeaseTimesEnableConfig,'specificLeaseTimesLeaseTime':specificLeaseTimesLeaseTime,'leaseTimesInfoTable':leaseTimesInfoTable,'leaseTimesInfoEntry':leaseTimesInfoEntry,_S:leaseTimesInfoSubnetName,'leaseTimesInfoDefault':leaseTimesInfoDefault,'defaultRouterGroup':defaultRouterGroup,'specificDefaultRoutersTable':specificDefaultRoutersTable,'specificDefaultRoutersEntry':specificDefaultRoutersEntry,_T:specificDefaultRoutersSubnetName,'specificDefaultRoutersEnableOption':specificDefaultRoutersEnableOption,'specificDefaultRoutersConfigSource':specificDefaultRoutersConfigSource,'specificDefaultRoutersStaticRouter':specificDefaultRoutersStaticRouter,'defaultRoutersInfoTable':defaultRoutersInfoTable,'defaultRoutersInfoEntry':defaultRoutersInfoEntry,_U:defaultRoutersInfoSubnetName,'defaultRoutersInfoDefaultRouter':defaultRoutersInfoDefaultRouter,'dnsServersGroup':dnsServersGroup,'defaultDnsServersConfigSource':defaultDnsServersConfigSource,'defaultStaticDnsServersTable':defaultStaticDnsServersTable,'defaultStaticDnsServersEntry':defaultStaticDnsServersEntry,_V:defaultStaticDnsServersPriority,'defaultStaticDnsServersIpAddress':defaultStaticDnsServersIpAddress,'specificDnsServersTable':specificDnsServersTable,'specificDnsServersEntry':specificDnsServersEntry,_W:specificDnsServersSubnetName,'specificDnsServersEnableConfig':specificDnsServersEnableConfig,'specificDnsServersEnableOption':specificDnsServersEnableOption,'specificDnsServersConfigSource':specificDnsServersConfigSource,'specificDnsServersStaticDns1':specificDnsServersStaticDns1,'specificDnsServersStaticDns2':specificDnsServersStaticDns2,'specificDnsServersStaticDns3':specificDnsServersStaticDns3,'specificDnsServersStaticDns4':specificDnsServersStaticDns4,'dnsServersInfoTable':dnsServersInfoTable,'dnsServersInfoEntry':dnsServersInfoEntry,_X:dnsServersInfoSubnetName,'dnsServersInfoDns1':dnsServersInfoDns1,'dnsServersInfoDns2':dnsServersInfoDns2,'dnsServersInfoDns3':dnsServersInfoDns3,'dnsServersInfoDns4':dnsServersInfoDns4,'ntpServersGroup':ntpServersGroup,'defaultNtpServersConfigSource':defaultNtpServersConfigSource,'defaultStaticNtpServersTable':defaultStaticNtpServersTable,'defaultStaticNtpServersEntry':defaultStaticNtpServersEntry,_Y:defaultStaticNtpServersPriority,'defaultStaticNtpServersIpAddress':defaultStaticNtpServersIpAddress,'specificNtpServersTable':specificNtpServersTable,'specificNtpServersEntry':specificNtpServersEntry,_Z:specificNtpServersSubnetName,'specificNtpServersEnableConfig':specificNtpServersEnableConfig,'specificNtpServersEnableOption':specificNtpServersEnableOption,'specificNtpServersConfigSource':specificNtpServersConfigSource,'specificNtpServersStaticNtp1':specificNtpServersStaticNtp1,'specificNtpServersStaticNtp2':specificNtpServersStaticNtp2,'specificNtpServersStaticNtp3':specificNtpServersStaticNtp3,'specificNtpServersStaticNtp4':specificNtpServersStaticNtp4,'ntpServersInfoTable':ntpServersInfoTable,'ntpServersInfoEntry':ntpServersInfoEntry,_a:ntpServersInfoSubnetName,'ntpServersInfoNtp1':ntpServersInfoNtp1,'ntpServersInfoNtp2':ntpServersInfoNtp2,'ntpServersInfoNtp3':ntpServersInfoNtp3,'ntpServersInfoNtp4':ntpServersInfoNtp4,'nbnsServersGroup':nbnsServersGroup,'defaultStaticNbnsServersTable':defaultStaticNbnsServersTable,'defaultStaticNbnsServersEntry':defaultStaticNbnsServersEntry,_b:defaultStaticNbnsServersPriority,'defaultStaticNbnsServersIpAddress':defaultStaticNbnsServersIpAddress,'specificNbnsServersTable':specificNbnsServersTable,'specificNbnsServersEntry':specificNbnsServersEntry,_c:specificNbnsServersSubnetName,'specificNbnsServersEnableConfig':specificNbnsServersEnableConfig,'specificNbnsServersEnableOption':specificNbnsServersEnableOption,'specificNbnsServersStaticNbns1':specificNbnsServersStaticNbns1,'specificNbnsServersStaticNbns2':specificNbnsServersStaticNbns2,'specificNbnsServersStaticNbns3':specificNbnsServersStaticNbns3,'specificNbnsServersStaticNbns4':specificNbnsServersStaticNbns4,'nbnsServersInfoTable':nbnsServersInfoTable,'nbnsServersInfoEntry':nbnsServersInfoEntry,_d:nbnsServersInfoSubnetName,'nbnsServersInfoNbns1':nbnsServersInfoNbns1,'nbnsServersInfoNbns2':nbnsServersInfoNbns2,'nbnsServersInfoNbns3':nbnsServersInfoNbns3,'nbnsServersInfoNbns4':nbnsServersInfoNbns4,'staticLeasesTable':staticLeasesTable,'staticLeasesEntry':staticLeasesEntry,_e:staticLeasesMacAddress,'staticLeasesIpAddress':staticLeasesIpAddress,'staticLeasesDelete':staticLeasesDelete,'assignedLeasesInfoTable':assignedLeasesInfoTable,'assignedLeasesInfoEntry':assignedLeasesInfoEntry,_f:assignedLeasesInfoIpAddress,'assignedLeasesInfoMacAddress':assignedLeasesInfoMacAddress,'assignedLeasesInfoSubnetName':assignedLeasesInfoSubnetName,'assignedLeasesInfoLeaseTimeLeft':assignedLeasesInfoLeaseTimeLeft,'provisioningGroup':provisioningGroup,'defaultStaticOption66':defaultStaticOption66,'defaultStaticOption67':defaultStaticOption67,'specificOption66Table':specificOption66Table,'specificOption66Entry':specificOption66Entry,_g:specificOption66SubnetName,'specificOption66EnableConfig':specificOption66EnableConfig,'specificOption66EnableOption':specificOption66EnableOption,'specificOption66Value':specificOption66Value,'specificOption67Table':specificOption67Table,'specificOption67Entry':specificOption67Entry,_h:specificOption67SubnetName,'specificOption67EnableConfig':specificOption67EnableConfig,'specificOption67EnableOption':specificOption67EnableOption,'specificOption67Value':specificOption67Value,'statisticsGroup':statisticsGroup,'subnetsStatsTable':subnetsStatsTable,'subnetsStatsEntry':subnetsStatsEntry,_i:subnetsStatsSubnetName,'subnetsStatsNumberOfLeases':subnetsStatsNumberOfLeases,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})