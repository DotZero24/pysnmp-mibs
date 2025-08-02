_M='interfaceStatisticsLinkName'
_L='networkInterfacesStatusIdx'
_K='networkInterfacesIdx'
_J='MxIpAddrMask'
_I='MxIpAddress'
_H='MxEnableState'
_G='MX-BNI-MIB'
_F='Unsigned32'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_H,_I,'MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr',_J,'MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bniMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200))
_BniMIBObjects_ObjectIdentity=ObjectIdentity
bniMIBObjects=_BniMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1))
_DhcpClientGroup_ObjectIdentity=ObjectIdentity
dhcpClientGroup=_DhcpClientGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,200))
class _DhcpClientIdentifierPresentation_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('disabled',100),('macAscii',200),('macBinary',300)))
_DhcpClientIdentifierPresentation_Type.__name__=_D
_DhcpClientIdentifierPresentation_Object=MibScalar
dhcpClientIdentifierPresentation=_DhcpClientIdentifierPresentation_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,200,100),_DhcpClientIdentifierPresentation_Type())
dhcpClientIdentifierPresentation.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientIdentifierPresentation.setStatus(_A)
class _DhcpClientDuplicateIpAddressDetectionEnable_Type(MxEnableState):defaultValue=0
_DhcpClientDuplicateIpAddressDetectionEnable_Type.__name__=_H
_DhcpClientDuplicateIpAddressDetectionEnable_Object=MibScalar
dhcpClientDuplicateIpAddressDetectionEnable=_DhcpClientDuplicateIpAddressDetectionEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,200,200),_DhcpClientDuplicateIpAddressDetectionEnable_Type())
dhcpClientDuplicateIpAddressDetectionEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientDuplicateIpAddressDetectionEnable.setStatus(_A)
class _DhcpClientClasslessStaticRouteOption_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('none',100),('request',200)))
_DhcpClientClasslessStaticRouteOption_Type.__name__=_D
_DhcpClientClasslessStaticRouteOption_Object=MibScalar
dhcpClientClasslessStaticRouteOption=_DhcpClientClasslessStaticRouteOption_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,200,300),_DhcpClientClasslessStaticRouteOption_Type())
dhcpClientClasslessStaticRouteOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientClasslessStaticRouteOption.setStatus(_A)
class _DhcpClientUserClass_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_DhcpClientUserClass_Type.__name__=_E
_DhcpClientUserClass_Object=MibScalar
dhcpClientUserClass=_DhcpClientUserClass_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,200,400),_DhcpClientUserClass_Type())
dhcpClientUserClass.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpClientUserClass.setStatus(_A)
_PppIpcpGroup_ObjectIdentity=ObjectIdentity
pppIpcpGroup=_PppIpcpGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400))
class _PppServiceName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PppServiceName_Type.__name__=_E
_PppServiceName_Object=MibScalar
pppServiceName=_PppServiceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400,100),_PppServiceName_Type())
pppServiceName.setMaxAccess(_B)
if mibBuilder.loadTexts:pppServiceName.setStatus(_A)
class _PppRetryInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_PppRetryInterval_Type.__name__=_F
_PppRetryInterval_Object=MibScalar
pppRetryInterval=_PppRetryInterval_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400,200),_PppRetryInterval_Type())
pppRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:pppRetryInterval.setStatus(_A)
class _PppAuthenticationProtocol_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('pap',100),('chap',200)))
_PppAuthenticationProtocol_Type.__name__=_D
_PppAuthenticationProtocol_Object=MibScalar
pppAuthenticationProtocol=_PppAuthenticationProtocol_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400,300),_PppAuthenticationProtocol_Type())
pppAuthenticationProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pppAuthenticationProtocol.setStatus(_A)
class _PppIdentity_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PppIdentity_Type.__name__=_E
_PppIdentity_Object=MibScalar
pppIdentity=_PppIdentity_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400,400),_PppIdentity_Type())
pppIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:pppIdentity.setStatus(_A)
class _PppSecret_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_PppSecret_Type.__name__=_E
_PppSecret_Object=MibScalar
pppSecret=_PppSecret_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,400,500),_PppSecret_Type())
pppSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:pppSecret.setStatus(_A)
_IcmpGroup_ObjectIdentity=ObjectIdentity
icmpGroup=_IcmpGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,500))
class _IcmpRedirect_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('acceptIpv4AndIpv6',100),('acceptIpv4Only',200)))
_IcmpRedirect_Type.__name__=_D
_IcmpRedirect_Object=MibScalar
icmpRedirect=_IcmpRedirect_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,500,100),_IcmpRedirect_Type())
icmpRedirect.setMaxAccess(_B)
if mibBuilder.loadTexts:icmpRedirect.setStatus(_A)
_IpGroup_ObjectIdentity=ObjectIdentity
ipGroup=_IpGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,600))
class _IpTtlValue_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,255))
_IpTtlValue_Type.__name__=_F
_IpTtlValue_Object=MibScalar
ipTtlValue=_IpTtlValue_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,600,100),_IpTtlValue_Type())
ipTtlValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ipTtlValue.setStatus(_A)
_NetworkInterfacesTable_Object=MibTable
networkInterfacesTable=_NetworkInterfacesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000))
if mibBuilder.loadTexts:networkInterfacesTable.setStatus(_A)
_NetworkInterfacesEntry_Object=MibTableRow
networkInterfacesEntry=_NetworkInterfacesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1))
networkInterfacesEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:networkInterfacesEntry.setStatus(_A)
_NetworkInterfacesIdx_Type=Unsigned32
_NetworkInterfacesIdx_Object=MibTableColumn
networkInterfacesIdx=_NetworkInterfacesIdx_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,50),_NetworkInterfacesIdx_Type())
networkInterfacesIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesIdx.setStatus(_A)
class _NetworkInterfacesInterfaceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NetworkInterfacesInterfaceName_Type.__name__=_E
_NetworkInterfacesInterfaceName_Object=MibTableColumn
networkInterfacesInterfaceName=_NetworkInterfacesInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,100),_NetworkInterfacesInterfaceName_Type())
networkInterfacesInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesInterfaceName.setStatus(_A)
class _NetworkInterfacesLinkName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NetworkInterfacesLinkName_Type.__name__=_E
_NetworkInterfacesLinkName_Object=MibTableColumn
networkInterfacesLinkName=_NetworkInterfacesLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,200),_NetworkInterfacesLinkName_Type())
networkInterfacesLinkName.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesLinkName.setStatus(_A)
class _NetworkInterfacesConnectionType_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,225,250,300)));namedValues=NamedValues(*(('ipDhcp',100),('ipStatic',200),('ip6AutoConf',225),('ip6Static',250),('pppIpcp',300)))
_NetworkInterfacesConnectionType_Type.__name__=_D
_NetworkInterfacesConnectionType_Object=MibTableColumn
networkInterfacesConnectionType=_NetworkInterfacesConnectionType_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,250),_NetworkInterfacesConnectionType_Type())
networkInterfacesConnectionType.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesConnectionType.setStatus(_A)
class _NetworkInterfacesStaticIpAddr_Type(MxIpAddrMask):defaultValue=OctetString('192.168.0.10/24')
_NetworkInterfacesStaticIpAddr_Type.__name__=_J
_NetworkInterfacesStaticIpAddr_Object=MibTableColumn
networkInterfacesStaticIpAddr=_NetworkInterfacesStaticIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,300),_NetworkInterfacesStaticIpAddr_Type())
networkInterfacesStaticIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesStaticIpAddr.setStatus(_A)
class _NetworkInterfacesStaticDefaultRouter_Type(MxIpAddress):defaultValue=OctetString('')
_NetworkInterfacesStaticDefaultRouter_Type.__name__=_I
_NetworkInterfacesStaticDefaultRouter_Object=MibTableColumn
networkInterfacesStaticDefaultRouter=_NetworkInterfacesStaticDefaultRouter_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,350),_NetworkInterfacesStaticDefaultRouter_Type())
networkInterfacesStaticDefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesStaticDefaultRouter.setStatus(_A)
class _NetworkInterfacesActivation_Type(MxEnableState):defaultValue=0
_NetworkInterfacesActivation_Type.__name__=_H
_NetworkInterfacesActivation_Object=MibTableColumn
networkInterfacesActivation=_NetworkInterfacesActivation_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,400),_NetworkInterfacesActivation_Type())
networkInterfacesActivation.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesActivation.setStatus(_A)
class _NetworkInterfacesPriority_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NetworkInterfacesPriority_Type.__name__=_F
_NetworkInterfacesPriority_Object=MibTableColumn
networkInterfacesPriority=_NetworkInterfacesPriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,450),_NetworkInterfacesPriority_Type())
networkInterfacesPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesPriority.setStatus(_A)
class _NetworkInterfacesConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600)));namedValues=NamedValues(*(('validConfig',100),('emptyInterfaceName',200),('duplicateInterfaceName',300),('invalidLinkName',400),('invalidStaticIpAddr',500),('multipleDynamicOnSameLink',600)))
_NetworkInterfacesConfigStatus_Type.__name__=_D
_NetworkInterfacesConfigStatus_Object=MibTableColumn
networkInterfacesConfigStatus=_NetworkInterfacesConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,480),_NetworkInterfacesConfigStatus_Type())
networkInterfacesConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesConfigStatus.setStatus(_A)
class _NetworkInterfacesDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('delete',10)))
_NetworkInterfacesDelete_Type.__name__=_D
_NetworkInterfacesDelete_Object=MibTableColumn
networkInterfacesDelete=_NetworkInterfacesDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,1000,1,500),_NetworkInterfacesDelete_Type())
networkInterfacesDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:networkInterfacesDelete.setStatus(_A)
_NetworkInterfacesStatusTable_Object=MibTable
networkInterfacesStatusTable=_NetworkInterfacesStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000))
if mibBuilder.loadTexts:networkInterfacesStatusTable.setStatus(_A)
_NetworkInterfacesStatusEntry_Object=MibTableRow
networkInterfacesStatusEntry=_NetworkInterfacesStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1))
networkInterfacesStatusEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:networkInterfacesStatusEntry.setStatus(_A)
_NetworkInterfacesStatusIdx_Type=Unsigned32
_NetworkInterfacesStatusIdx_Object=MibTableColumn
networkInterfacesStatusIdx=_NetworkInterfacesStatusIdx_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,50),_NetworkInterfacesStatusIdx_Type())
networkInterfacesStatusIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusIdx.setStatus(_A)
_NetworkInterfacesStatusInterfaceName_Type=OctetString
_NetworkInterfacesStatusInterfaceName_Object=MibTableColumn
networkInterfacesStatusInterfaceName=_NetworkInterfacesStatusInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,100),_NetworkInterfacesStatusInterfaceName_Type())
networkInterfacesStatusInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusInterfaceName.setStatus(_A)
class _NetworkInterfacesStatusInterfaceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,225,250,300,400)));namedValues=NamedValues(*(('invalidConfig',200),('networkConflict',225),('linkDown',250),('waitingResponse',300),('active',400)))
_NetworkInterfacesStatusInterfaceStatus_Type.__name__=_D
_NetworkInterfacesStatusInterfaceStatus_Object=MibTableColumn
networkInterfacesStatusInterfaceStatus=_NetworkInterfacesStatusInterfaceStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,150),_NetworkInterfacesStatusInterfaceStatus_Type())
networkInterfacesStatusInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusInterfaceStatus.setStatus(_A)
_NetworkInterfacesStatusLinkName_Type=OctetString
_NetworkInterfacesStatusLinkName_Object=MibTableColumn
networkInterfacesStatusLinkName=_NetworkInterfacesStatusLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,200),_NetworkInterfacesStatusLinkName_Type())
networkInterfacesStatusLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusLinkName.setStatus(_A)
_NetworkInterfacesStatusIpAddr_Type=MxIpAddrMask
_NetworkInterfacesStatusIpAddr_Object=MibTableColumn
networkInterfacesStatusIpAddr=_NetworkInterfacesStatusIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,300),_NetworkInterfacesStatusIpAddr_Type())
networkInterfacesStatusIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusIpAddr.setStatus(_A)
_NetworkInterfacesStatusDefaultRouter_Type=OctetString
_NetworkInterfacesStatusDefaultRouter_Object=MibTableColumn
networkInterfacesStatusDefaultRouter=_NetworkInterfacesStatusDefaultRouter_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,400),_NetworkInterfacesStatusDefaultRouter_Type())
networkInterfacesStatusDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusDefaultRouter.setStatus(_A)
_NetworkInterfacesStatusConnectionUptime_Type=Unsigned32
_NetworkInterfacesStatusConnectionUptime_Object=MibTableColumn
networkInterfacesStatusConnectionUptime=_NetworkInterfacesStatusConnectionUptime_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,500),_NetworkInterfacesStatusConnectionUptime_Type())
networkInterfacesStatusConnectionUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusConnectionUptime.setStatus(_A)
_NetworkInterfacesStatusVlanOverrideEnable_Type=MxEnableState
_NetworkInterfacesStatusVlanOverrideEnable_Object=MibTableColumn
networkInterfacesStatusVlanOverrideEnable=_NetworkInterfacesStatusVlanOverrideEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,2000,1,600),_NetworkInterfacesStatusVlanOverrideEnable_Type())
networkInterfacesStatusVlanOverrideEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:networkInterfacesStatusVlanOverrideEnable.setStatus(_A)
_StatisticsGroup_ObjectIdentity=ObjectIdentity
statisticsGroup=_StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000))
_InterfaceStatisticsTable_Object=MibTable
interfaceStatisticsTable=_InterfaceStatisticsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100))
if mibBuilder.loadTexts:interfaceStatisticsTable.setStatus(_A)
_InterfaceStatisticsEntry_Object=MibTableRow
interfaceStatisticsEntry=_InterfaceStatisticsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1))
interfaceStatisticsEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:interfaceStatisticsEntry.setStatus(_A)
_InterfaceStatisticsLinkName_Type=OctetString
_InterfaceStatisticsLinkName_Object=MibTableColumn
interfaceStatisticsLinkName=_InterfaceStatisticsLinkName_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,100),_InterfaceStatisticsLinkName_Type())
interfaceStatisticsLinkName.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsLinkName.setStatus(_A)
_InterfaceStatisticsTxBytes_Type=MxUInt64
_InterfaceStatisticsTxBytes_Object=MibTableColumn
interfaceStatisticsTxBytes=_InterfaceStatisticsTxBytes_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,200),_InterfaceStatisticsTxBytes_Type())
interfaceStatisticsTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsTxBytes.setStatus(_A)
_InterfaceStatisticsRxBytes_Type=MxUInt64
_InterfaceStatisticsRxBytes_Object=MibTableColumn
interfaceStatisticsRxBytes=_InterfaceStatisticsRxBytes_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,300),_InterfaceStatisticsRxBytes_Type())
interfaceStatisticsRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsRxBytes.setStatus(_A)
_InterfaceStatisticsTxPackets_Type=MxUInt64
_InterfaceStatisticsTxPackets_Object=MibTableColumn
interfaceStatisticsTxPackets=_InterfaceStatisticsTxPackets_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,400),_InterfaceStatisticsTxPackets_Type())
interfaceStatisticsTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsTxPackets.setStatus(_A)
_InterfaceStatisticsRxPackets_Type=MxUInt64
_InterfaceStatisticsRxPackets_Object=MibTableColumn
interfaceStatisticsRxPackets=_InterfaceStatisticsRxPackets_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,500),_InterfaceStatisticsRxPackets_Type())
interfaceStatisticsRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsRxPackets.setStatus(_A)
_InterfaceStatisticsRxErrors_Type=MxUInt64
_InterfaceStatisticsRxErrors_Object=MibTableColumn
interfaceStatisticsRxErrors=_InterfaceStatisticsRxErrors_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,600),_InterfaceStatisticsRxErrors_Type())
interfaceStatisticsRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsRxErrors.setStatus(_A)
_InterfaceStatisticsCollectTime_Type=Unsigned32
_InterfaceStatisticsCollectTime_Object=MibTableColumn
interfaceStatisticsCollectTime=_InterfaceStatisticsCollectTime_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,10000),_InterfaceStatisticsCollectTime_Type())
interfaceStatisticsCollectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceStatisticsCollectTime.setStatus(_A)
class _InterfaceStatisticsResetStat_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*(('noOp',0),('resetStat',10)))
_InterfaceStatisticsResetStat_Type.__name__=_D
_InterfaceStatisticsResetStat_Object=MibTableColumn
interfaceStatisticsResetStat=_InterfaceStatisticsResetStat_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,10000,100,1,11000),_InterfaceStatisticsResetStat_Type())
interfaceStatisticsResetStat.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceStatisticsResetStat.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_D
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,200,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_D
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,200,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'bniMIB':bniMIB,'bniMIBObjects':bniMIBObjects,'dhcpClientGroup':dhcpClientGroup,'dhcpClientIdentifierPresentation':dhcpClientIdentifierPresentation,'dhcpClientDuplicateIpAddressDetectionEnable':dhcpClientDuplicateIpAddressDetectionEnable,'dhcpClientClasslessStaticRouteOption':dhcpClientClasslessStaticRouteOption,'dhcpClientUserClass':dhcpClientUserClass,'pppIpcpGroup':pppIpcpGroup,'pppServiceName':pppServiceName,'pppRetryInterval':pppRetryInterval,'pppAuthenticationProtocol':pppAuthenticationProtocol,'pppIdentity':pppIdentity,'pppSecret':pppSecret,'icmpGroup':icmpGroup,'icmpRedirect':icmpRedirect,'ipGroup':ipGroup,'ipTtlValue':ipTtlValue,'networkInterfacesTable':networkInterfacesTable,'networkInterfacesEntry':networkInterfacesEntry,_K:networkInterfacesIdx,'networkInterfacesInterfaceName':networkInterfacesInterfaceName,'networkInterfacesLinkName':networkInterfacesLinkName,'networkInterfacesConnectionType':networkInterfacesConnectionType,'networkInterfacesStaticIpAddr':networkInterfacesStaticIpAddr,'networkInterfacesStaticDefaultRouter':networkInterfacesStaticDefaultRouter,'networkInterfacesActivation':networkInterfacesActivation,'networkInterfacesPriority':networkInterfacesPriority,'networkInterfacesConfigStatus':networkInterfacesConfigStatus,'networkInterfacesDelete':networkInterfacesDelete,'networkInterfacesStatusTable':networkInterfacesStatusTable,'networkInterfacesStatusEntry':networkInterfacesStatusEntry,_L:networkInterfacesStatusIdx,'networkInterfacesStatusInterfaceName':networkInterfacesStatusInterfaceName,'networkInterfacesStatusInterfaceStatus':networkInterfacesStatusInterfaceStatus,'networkInterfacesStatusLinkName':networkInterfacesStatusLinkName,'networkInterfacesStatusIpAddr':networkInterfacesStatusIpAddr,'networkInterfacesStatusDefaultRouter':networkInterfacesStatusDefaultRouter,'networkInterfacesStatusConnectionUptime':networkInterfacesStatusConnectionUptime,'networkInterfacesStatusVlanOverrideEnable':networkInterfacesStatusVlanOverrideEnable,'statisticsGroup':statisticsGroup,'interfaceStatisticsTable':interfaceStatisticsTable,'interfaceStatisticsEntry':interfaceStatisticsEntry,_M:interfaceStatisticsLinkName,'interfaceStatisticsTxBytes':interfaceStatisticsTxBytes,'interfaceStatisticsRxBytes':interfaceStatisticsRxBytes,'interfaceStatisticsTxPackets':interfaceStatisticsTxPackets,'interfaceStatisticsRxPackets':interfaceStatisticsRxPackets,'interfaceStatisticsRxErrors':interfaceStatisticsRxErrors,'interfaceStatisticsCollectTime':interfaceStatisticsCollectTime,'interfaceStatisticsResetStat':interfaceStatisticsResetStat,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})