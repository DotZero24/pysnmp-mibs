_AG='telephonyDnsGroupVer1'
_AF='commonLocalHostGroupVer1'
_AE='sysConfigGroupVer1'
_AD='telephonyDnsSecondaryDns'
_AC='telephonyDnsPrimaryDns'
_AB='telephonyDnsStaticSecondaryDns'
_AA='telephonyDnsStaticPrimaryDns'
_A9='telephonyDnsOverrideEnable'
_A8='localHostStaticWanAddress'
_A7='localHostStaticFqdn'
_A6='localHostStaticSubnetMask'
_A5='localHostStaticSnmpPort'
_A4='localHostStaticDefaultRouter'
_A3='localHostStaticSecondaryDns'
_A2='localHostStaticPrimaryDns'
_A1='localHostStaticAddress'
_A0='localHostDnsOverrideEnable'
_z='localHostWanAddressSelectConfigSource'
_y='localHostFqdnSelectConfigSource'
_x='localHostSelectConfigSource'
_w='localHostWanAddress'
_v='localHostWanAddressConfigSource'
_u='localHostFqdn'
_t='localHostFqdnConfigSource'
_s='localHostSubnetMask'
_r='localHostSnmpPort'
_q='localHostDefaultRouter'
_p='localHostSecondaryDns'
_o='localHostPrimaryDns'
_n='localHostDhcpServer'
_m='localHostAddress'
_l='localHostConfigSource'
_k='sysConfigDownloadConfigMode'
_j='sysConfigDownloadConfigFile'
_i='sysConfigStatsBySyslogEnable'
_h='sysConfigStatsNumberPeriods'
_g='sysConfigStatsPeriodLength'
_f='sysConfigProductNamePadding'
_e='sysConfigBootpFlags'
_d='sysConfigDhcpWaitDelay'
_c='sysConfigDhcpWait'
_b='sysConfigMaxDynamicPort'
_a='sysConfigMinDynamicPort'
_Z='sysConfigComputerEthernetSpeed'
_Y='sysConfigNetworkEthernetSpeed'
_X='at-100Mbs-FullDuplex'
_W='at-10Mbs-FullDuplex'
_V='at-100Mbs-HalfDuplex'
_U='at-10Mbs-HalfDuplex'
_T='autoDetect'
_S='0.0.0.0'
_R='localAddress'
_Q='255.255.255.0'
_P='192.168.0.1'
_O='MxIpSelectConfigSource'
_N='MxIpConfigSource'
_M='MxIpSubnetMask'
_L='MxIpPort'
_K='static'
_J='OctetString'
_I='MxEnableState'
_H='Unsigned32'
_G='Integer32'
_F='192.168.0.10'
_E='read-only'
_D='MxIpAddress'
_C='read-write'
_B='MX-SYSTEM-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig','mediatrixMgmt')
MxEnableState,MxIpAddress,MxIpConfigSource,MxIpPort,MxIpSelectConfigSource,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC',_I,_D,_N,_L,_O,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sysConfigMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,3))
if mibBuilder.loadTexts:sysConfigMIB.setRevisions(('2008-08-25 00:00','2006-11-23 00:00','2006-07-12 00:00','2005-08-31 00:00','2005-05-09 00:00','2004-09-20 00:00','2004-02-12 00:00','2003-11-14 00:00','2003-11-13 00:00','2003-09-11 00:00','2003-07-16 00:00','2003-04-10 00:00','2003-04-07 00:00','2003-04-03 00:00','2003-03-11 00:00','2002-08-19 00:00','2002-07-10 00:00','2002-01-10 00:00','2001-08-22 00:00'))
_IpAddressStatusLocalHost_ObjectIdentity=ObjectIdentity
ipAddressStatusLocalHost=_IpAddressStatusLocalHost_ObjectIdentity((1,3,6,1,4,1,4935,10,1,1))
class _LocalHostConfigSource_Type(MxIpConfigSource):defaultValue=1
_LocalHostConfigSource_Type.__name__=_N
_LocalHostConfigSource_Object=MibScalar
localHostConfigSource=_LocalHostConfigSource_Object((1,3,6,1,4,1,4935,10,1,1,1),_LocalHostConfigSource_Type())
localHostConfigSource.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostConfigSource.setStatus(_A)
class _LocalHostAddress_Type(MxIpAddress):defaultValue=OctetString(_P)
_LocalHostAddress_Type.__name__=_D
_LocalHostAddress_Object=MibScalar
localHostAddress=_LocalHostAddress_Object((1,3,6,1,4,1,4935,10,1,1,2),_LocalHostAddress_Type())
localHostAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostAddress.setStatus(_A)
class _LocalHostDhcpServer_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostDhcpServer_Type.__name__=_D
_LocalHostDhcpServer_Object=MibScalar
localHostDhcpServer=_LocalHostDhcpServer_Object((1,3,6,1,4,1,4935,10,1,1,3),_LocalHostDhcpServer_Type())
localHostDhcpServer.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostDhcpServer.setStatus(_A)
class _LocalHostPrimaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostPrimaryDns_Type.__name__=_D
_LocalHostPrimaryDns_Object=MibScalar
localHostPrimaryDns=_LocalHostPrimaryDns_Object((1,3,6,1,4,1,4935,10,1,1,4),_LocalHostPrimaryDns_Type())
localHostPrimaryDns.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostPrimaryDns.setStatus(_A)
class _LocalHostSecondaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostSecondaryDns_Type.__name__=_D
_LocalHostSecondaryDns_Object=MibScalar
localHostSecondaryDns=_LocalHostSecondaryDns_Object((1,3,6,1,4,1,4935,10,1,1,5),_LocalHostSecondaryDns_Type())
localHostSecondaryDns.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostSecondaryDns.setStatus(_A)
class _LocalHostDefaultRouter_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostDefaultRouter_Type.__name__=_D
_LocalHostDefaultRouter_Object=MibScalar
localHostDefaultRouter=_LocalHostDefaultRouter_Object((1,3,6,1,4,1,4935,10,1,1,6),_LocalHostDefaultRouter_Type())
localHostDefaultRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostDefaultRouter.setStatus(_A)
class _LocalHostSnmpPort_Type(MxIpPort):defaultValue=161
_LocalHostSnmpPort_Type.__name__=_L
_LocalHostSnmpPort_Object=MibScalar
localHostSnmpPort=_LocalHostSnmpPort_Object((1,3,6,1,4,1,4935,10,1,1,7),_LocalHostSnmpPort_Type())
localHostSnmpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostSnmpPort.setStatus(_A)
class _LocalHostSubnetMask_Type(MxIpSubnetMask):defaultValue=OctetString(_Q)
_LocalHostSubnetMask_Type.__name__=_M
_LocalHostSubnetMask_Object=MibScalar
localHostSubnetMask=_LocalHostSubnetMask_Object((1,3,6,1,4,1,4935,10,1,1,8),_LocalHostSubnetMask_Type())
localHostSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostSubnetMask.setStatus(_A)
class _LocalHostFqdnConfigSource_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('dhcp',1),('dns',2),('none',3)))
_LocalHostFqdnConfigSource_Type.__name__=_G
_LocalHostFqdnConfigSource_Object=MibScalar
localHostFqdnConfigSource=_LocalHostFqdnConfigSource_Object((1,3,6,1,4,1,4935,10,1,1,9),_LocalHostFqdnConfigSource_Type())
localHostFqdnConfigSource.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostFqdnConfigSource.setStatus(_A)
class _LocalHostFqdn_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LocalHostFqdn_Type.__name__=_J
_LocalHostFqdn_Object=MibScalar
localHostFqdn=_LocalHostFqdn_Object((1,3,6,1,4,1,4935,10,1,1,10),_LocalHostFqdn_Type())
localHostFqdn.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostFqdn.setStatus(_A)
class _LocalHostWanAddressConfigSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_R,0),(_K,1),('pppoe',2),('pppoa',3)))
_LocalHostWanAddressConfigSource_Type.__name__=_G
_LocalHostWanAddressConfigSource_Object=MibScalar
localHostWanAddressConfigSource=_LocalHostWanAddressConfigSource_Object((1,3,6,1,4,1,4935,10,1,1,15),_LocalHostWanAddressConfigSource_Type())
localHostWanAddressConfigSource.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostWanAddressConfigSource.setStatus(_A)
class _LocalHostWanAddress_Type(MxIpAddress):defaultValue=OctetString(_S)
_LocalHostWanAddress_Type.__name__=_D
_LocalHostWanAddress_Object=MibScalar
localHostWanAddress=_LocalHostWanAddress_Object((1,3,6,1,4,1,4935,10,1,1,20),_LocalHostWanAddress_Type())
localHostWanAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:localHostWanAddress.setStatus(_A)
_IpAddressStatusTelephonyDns_ObjectIdentity=ObjectIdentity
ipAddressStatusTelephonyDns=_IpAddressStatusTelephonyDns_ObjectIdentity((1,3,6,1,4,1,4935,10,1,100))
class _TelephonyDnsPrimaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_TelephonyDnsPrimaryDns_Type.__name__=_D
_TelephonyDnsPrimaryDns_Object=MibScalar
telephonyDnsPrimaryDns=_TelephonyDnsPrimaryDns_Object((1,3,6,1,4,1,4935,10,1,100,10),_TelephonyDnsPrimaryDns_Type())
telephonyDnsPrimaryDns.setMaxAccess(_E)
if mibBuilder.loadTexts:telephonyDnsPrimaryDns.setStatus(_A)
class _TelephonyDnsSecondaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_TelephonyDnsSecondaryDns_Type.__name__=_D
_TelephonyDnsSecondaryDns_Object=MibScalar
telephonyDnsSecondaryDns=_TelephonyDnsSecondaryDns_Object((1,3,6,1,4,1,4935,10,1,100,15),_TelephonyDnsSecondaryDns_Type())
telephonyDnsSecondaryDns.setMaxAccess(_E)
if mibBuilder.loadTexts:telephonyDnsSecondaryDns.setStatus(_A)
_IpAddressConfigLocalHost_ObjectIdentity=ObjectIdentity
ipAddressConfigLocalHost=_IpAddressConfigLocalHost_ObjectIdentity((1,3,6,1,4,1,4935,15,1,1))
class _LocalHostSelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_LocalHostSelectConfigSource_Type.__name__=_O
_LocalHostSelectConfigSource_Object=MibScalar
localHostSelectConfigSource=_LocalHostSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,1,1),_LocalHostSelectConfigSource_Type())
localHostSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostSelectConfigSource.setStatus(_A)
class _LocalHostFqdnSelectConfigSource_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('dhcp',1),('dns',2),('none',3)))
_LocalHostFqdnSelectConfigSource_Type.__name__=_G
_LocalHostFqdnSelectConfigSource_Object=MibScalar
localHostFqdnSelectConfigSource=_LocalHostFqdnSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,1,2),_LocalHostFqdnSelectConfigSource_Type())
localHostFqdnSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostFqdnSelectConfigSource.setStatus(_A)
class _LocalHostWanAddressSelectConfigSource_Type(Integer32):defaultValue=9999;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,9999)));namedValues=NamedValues(*((_R,0),(_K,1),('pppoe',2),('pppoa',3),('automatic',9999)))
_LocalHostWanAddressSelectConfigSource_Type.__name__=_G
_LocalHostWanAddressSelectConfigSource_Object=MibScalar
localHostWanAddressSelectConfigSource=_LocalHostWanAddressSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,1,5),_LocalHostWanAddressSelectConfigSource_Type())
localHostWanAddressSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostWanAddressSelectConfigSource.setStatus(_A)
class _LocalHostDnsOverrideEnable_Type(MxEnableState):defaultValue=0
_LocalHostDnsOverrideEnable_Type.__name__=_I
_LocalHostDnsOverrideEnable_Object=MibScalar
localHostDnsOverrideEnable=_LocalHostDnsOverrideEnable_Object((1,3,6,1,4,1,4935,15,1,1,6),_LocalHostDnsOverrideEnable_Type())
localHostDnsOverrideEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostDnsOverrideEnable.setStatus(_A)
_IpAddressConfigLocalHostStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigLocalHostStatic=_IpAddressConfigLocalHostStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,1,10))
class _LocalHostStaticAddress_Type(MxIpAddress):defaultValue=OctetString(_P)
_LocalHostStaticAddress_Type.__name__=_D
_LocalHostStaticAddress_Object=MibScalar
localHostStaticAddress=_LocalHostStaticAddress_Object((1,3,6,1,4,1,4935,15,1,1,10,1),_LocalHostStaticAddress_Type())
localHostStaticAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticAddress.setStatus(_A)
class _LocalHostStaticPrimaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostStaticPrimaryDns_Type.__name__=_D
_LocalHostStaticPrimaryDns_Object=MibScalar
localHostStaticPrimaryDns=_LocalHostStaticPrimaryDns_Object((1,3,6,1,4,1,4935,15,1,1,10,2),_LocalHostStaticPrimaryDns_Type())
localHostStaticPrimaryDns.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticPrimaryDns.setStatus(_A)
class _LocalHostStaticSecondaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostStaticSecondaryDns_Type.__name__=_D
_LocalHostStaticSecondaryDns_Object=MibScalar
localHostStaticSecondaryDns=_LocalHostStaticSecondaryDns_Object((1,3,6,1,4,1,4935,15,1,1,10,3),_LocalHostStaticSecondaryDns_Type())
localHostStaticSecondaryDns.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticSecondaryDns.setStatus(_A)
class _LocalHostStaticDefaultRouter_Type(MxIpAddress):defaultValue=OctetString(_F)
_LocalHostStaticDefaultRouter_Type.__name__=_D
_LocalHostStaticDefaultRouter_Object=MibScalar
localHostStaticDefaultRouter=_LocalHostStaticDefaultRouter_Object((1,3,6,1,4,1,4935,15,1,1,10,4),_LocalHostStaticDefaultRouter_Type())
localHostStaticDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticDefaultRouter.setStatus(_A)
class _LocalHostStaticSnmpPort_Type(MxIpPort):defaultValue=161
_LocalHostStaticSnmpPort_Type.__name__=_L
_LocalHostStaticSnmpPort_Object=MibScalar
localHostStaticSnmpPort=_LocalHostStaticSnmpPort_Object((1,3,6,1,4,1,4935,15,1,1,10,5),_LocalHostStaticSnmpPort_Type())
localHostStaticSnmpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticSnmpPort.setStatus(_A)
class _LocalHostStaticSubnetMask_Type(MxIpSubnetMask):defaultValue=OctetString(_Q)
_LocalHostStaticSubnetMask_Type.__name__=_M
_LocalHostStaticSubnetMask_Object=MibScalar
localHostStaticSubnetMask=_LocalHostStaticSubnetMask_Object((1,3,6,1,4,1,4935,15,1,1,10,6),_LocalHostStaticSubnetMask_Type())
localHostStaticSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticSubnetMask.setStatus(_A)
class _LocalHostStaticFqdn_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LocalHostStaticFqdn_Type.__name__=_J
_LocalHostStaticFqdn_Object=MibScalar
localHostStaticFqdn=_LocalHostStaticFqdn_Object((1,3,6,1,4,1,4935,15,1,1,10,7),_LocalHostStaticFqdn_Type())
localHostStaticFqdn.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticFqdn.setStatus(_A)
class _LocalHostStaticWanAddress_Type(MxIpAddress):defaultValue=OctetString(_S)
_LocalHostStaticWanAddress_Type.__name__=_D
_LocalHostStaticWanAddress_Object=MibScalar
localHostStaticWanAddress=_LocalHostStaticWanAddress_Object((1,3,6,1,4,1,4935,15,1,1,10,10),_LocalHostStaticWanAddress_Type())
localHostStaticWanAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:localHostStaticWanAddress.setStatus(_A)
_IpAddressConfigTelephonyDns_ObjectIdentity=ObjectIdentity
ipAddressConfigTelephonyDns=_IpAddressConfigTelephonyDns_ObjectIdentity((1,3,6,1,4,1,4935,15,1,120))
class _TelephonyDnsOverrideEnable_Type(MxEnableState):defaultValue=0
_TelephonyDnsOverrideEnable_Type.__name__=_I
_TelephonyDnsOverrideEnable_Object=MibScalar
telephonyDnsOverrideEnable=_TelephonyDnsOverrideEnable_Object((1,3,6,1,4,1,4935,15,1,120,1),_TelephonyDnsOverrideEnable_Type())
telephonyDnsOverrideEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyDnsOverrideEnable.setStatus(_A)
_IpAddressConfigTelephonyDnsStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigTelephonyDnsStatic=_IpAddressConfigTelephonyDnsStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,120,50))
class _TelephonyDnsStaticPrimaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_TelephonyDnsStaticPrimaryDns_Type.__name__=_D
_TelephonyDnsStaticPrimaryDns_Object=MibScalar
telephonyDnsStaticPrimaryDns=_TelephonyDnsStaticPrimaryDns_Object((1,3,6,1,4,1,4935,15,1,120,50,10),_TelephonyDnsStaticPrimaryDns_Type())
telephonyDnsStaticPrimaryDns.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyDnsStaticPrimaryDns.setStatus(_A)
class _TelephonyDnsStaticSecondaryDns_Type(MxIpAddress):defaultValue=OctetString(_F)
_TelephonyDnsStaticSecondaryDns_Type.__name__=_D
_TelephonyDnsStaticSecondaryDns_Object=MibScalar
telephonyDnsStaticSecondaryDns=_TelephonyDnsStaticSecondaryDns_Object((1,3,6,1,4,1,4935,15,1,120,50,15),_TelephonyDnsStaticSecondaryDns_Type())
telephonyDnsStaticSecondaryDns.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyDnsStaticSecondaryDns.setStatus(_A)
_SysConfigMIBObjects_ObjectIdentity=ObjectIdentity
sysConfigMIBObjects=_SysConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,3,1))
class _SysConfigNetworkEthernetSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_W,3),(_X,4)))
_SysConfigNetworkEthernetSpeed_Type.__name__=_G
_SysConfigNetworkEthernetSpeed_Object=MibScalar
sysConfigNetworkEthernetSpeed=_SysConfigNetworkEthernetSpeed_Object((1,3,6,1,4,1,4935,15,3,1,10),_SysConfigNetworkEthernetSpeed_Type())
sysConfigNetworkEthernetSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigNetworkEthernetSpeed.setStatus(_A)
class _SysConfigComputerEthernetSpeed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_T,0),(_U,1),(_V,2),(_W,3),(_X,4)))
_SysConfigComputerEthernetSpeed_Type.__name__=_G
_SysConfigComputerEthernetSpeed_Object=MibScalar
sysConfigComputerEthernetSpeed=_SysConfigComputerEthernetSpeed_Object((1,3,6,1,4,1,4935,15,3,1,12),_SysConfigComputerEthernetSpeed_Type())
sysConfigComputerEthernetSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigComputerEthernetSpeed.setStatus(_A)
class _SysConfigMinDynamicPort_Type(Unsigned32):defaultValue=31001;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SysConfigMinDynamicPort_Type.__name__=_H
_SysConfigMinDynamicPort_Object=MibScalar
sysConfigMinDynamicPort=_SysConfigMinDynamicPort_Object((1,3,6,1,4,1,4935,15,3,1,14),_SysConfigMinDynamicPort_Type())
sysConfigMinDynamicPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigMinDynamicPort.setStatus(_A)
class _SysConfigMaxDynamicPort_Type(Unsigned32):defaultValue=32000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_SysConfigMaxDynamicPort_Type.__name__=_H
_SysConfigMaxDynamicPort_Object=MibScalar
sysConfigMaxDynamicPort=_SysConfigMaxDynamicPort_Object((1,3,6,1,4,1,4935,15,3,1,16),_SysConfigMaxDynamicPort_Type())
sysConfigMaxDynamicPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigMaxDynamicPort.setStatus(_A)
class _SysConfigDhcpWait_Type(MxEnableState):defaultValue=1
_SysConfigDhcpWait_Type.__name__=_I
_SysConfigDhcpWait_Object=MibScalar
sysConfigDhcpWait=_SysConfigDhcpWait_Object((1,3,6,1,4,1,4935,15,3,1,19),_SysConfigDhcpWait_Type())
sysConfigDhcpWait.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigDhcpWait.setStatus(_A)
class _SysConfigDhcpWaitDelay_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_SysConfigDhcpWaitDelay_Type.__name__=_H
_SysConfigDhcpWaitDelay_Object=MibScalar
sysConfigDhcpWaitDelay=_SysConfigDhcpWaitDelay_Object((1,3,6,1,4,1,4935,15,3,1,22),_SysConfigDhcpWaitDelay_Type())
sysConfigDhcpWaitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigDhcpWaitDelay.setStatus(_A)
class _SysConfigBootpFlags_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noFlags',0),('broadcastFlag',1)))
_SysConfigBootpFlags_Type.__name__=_G
_SysConfigBootpFlags_Object=MibScalar
sysConfigBootpFlags=_SysConfigBootpFlags_Object((1,3,6,1,4,1,4935,15,3,1,23),_SysConfigBootpFlags_Type())
sysConfigBootpFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigBootpFlags.setStatus(_A)
class _SysConfigProductNamePadding_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysConfigProductNamePadding_Type.__name__=_J
_SysConfigProductNamePadding_Object=MibScalar
sysConfigProductNamePadding=_SysConfigProductNamePadding_Object((1,3,6,1,4,1,4935,15,3,1,24),_SysConfigProductNamePadding_Type())
sysConfigProductNamePadding.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigProductNamePadding.setStatus(_A)
_SysConfigStats_ObjectIdentity=ObjectIdentity
sysConfigStats=_SysConfigStats_ObjectIdentity((1,3,6,1,4,1,4935,15,3,1,25))
class _SysConfigStatsPeriodLength_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,288))
_SysConfigStatsPeriodLength_Type.__name__=_H
_SysConfigStatsPeriodLength_Object=MibScalar
sysConfigStatsPeriodLength=_SysConfigStatsPeriodLength_Object((1,3,6,1,4,1,4935,15,3,1,25,1),_SysConfigStatsPeriodLength_Type())
sysConfigStatsPeriodLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigStatsPeriodLength.setStatus(_A)
class _SysConfigStatsNumberPeriods_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_SysConfigStatsNumberPeriods_Type.__name__=_H
_SysConfigStatsNumberPeriods_Object=MibScalar
sysConfigStatsNumberPeriods=_SysConfigStatsNumberPeriods_Object((1,3,6,1,4,1,4935,15,3,1,25,2),_SysConfigStatsNumberPeriods_Type())
sysConfigStatsNumberPeriods.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigStatsNumberPeriods.setStatus(_A)
class _SysConfigStatsBySyslogEnable_Type(MxEnableState):defaultValue=0
_SysConfigStatsBySyslogEnable_Type.__name__=_I
_SysConfigStatsBySyslogEnable_Object=MibScalar
sysConfigStatsBySyslogEnable=_SysConfigStatsBySyslogEnable_Object((1,3,6,1,4,1,4935,15,3,1,25,10),_SysConfigStatsBySyslogEnable_Type())
sysConfigStatsBySyslogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigStatsBySyslogEnable.setStatus(_A)
_SysConfigDownloadConfig_ObjectIdentity=ObjectIdentity
sysConfigDownloadConfig=_SysConfigDownloadConfig_ObjectIdentity((1,3,6,1,4,1,4935,15,3,1,30))
class _SysConfigDownloadConfigFile_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3)));namedValues=NamedValues(*(('noFileDownload',0),('requestFileDownload',1),('automaticInitiateFileDownload',3)))
_SysConfigDownloadConfigFile_Type.__name__=_G
_SysConfigDownloadConfigFile_Object=MibScalar
sysConfigDownloadConfigFile=_SysConfigDownloadConfigFile_Object((1,3,6,1,4,1,4935,15,3,1,30,1),_SysConfigDownloadConfigFile_Type())
sysConfigDownloadConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigDownloadConfigFile.setStatus(_A)
class _SysConfigDownloadConfigMode_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0,1,2)));namedValues=NamedValues(*(('request',-1),('record',0),('commit',1),('undo',2)))
_SysConfigDownloadConfigMode_Type.__name__=_G
_SysConfigDownloadConfigMode_Object=MibScalar
sysConfigDownloadConfigMode=_SysConfigDownloadConfigMode_Object((1,3,6,1,4,1,4935,15,3,1,30,2),_SysConfigDownloadConfigMode_Type())
sysConfigDownloadConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sysConfigDownloadConfigMode.setStatus(_A)
_SysConfigConformance_ObjectIdentity=ObjectIdentity
sysConfigConformance=_SysConfigConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,3,2))
_SysConfigCompliances_ObjectIdentity=ObjectIdentity
sysConfigCompliances=_SysConfigCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,3,2,1))
_SysConfigGroups_ObjectIdentity=ObjectIdentity
sysConfigGroups=_SysConfigGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,3,2,2))
sysConfigGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,3,2,2,1))
sysConfigGroupVer1.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:sysConfigGroupVer1.setStatus(_A)
commonLocalHostGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,3,2,2,2))
commonLocalHostGroupVer1.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:commonLocalHostGroupVer1.setStatus(_A)
telephonyDnsGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,3,2,2,5))
telephonyDnsGroupVer1.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:telephonyDnsGroupVer1.setStatus(_A)
sysConfigComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,3,2,1,1))
sysConfigComplVer1.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:sysConfigComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusLocalHost':ipAddressStatusLocalHost,_l:localHostConfigSource,_m:localHostAddress,_n:localHostDhcpServer,_o:localHostPrimaryDns,_p:localHostSecondaryDns,_q:localHostDefaultRouter,_r:localHostSnmpPort,_s:localHostSubnetMask,_t:localHostFqdnConfigSource,_u:localHostFqdn,_v:localHostWanAddressConfigSource,_w:localHostWanAddress,'ipAddressStatusTelephonyDns':ipAddressStatusTelephonyDns,_AC:telephonyDnsPrimaryDns,_AD:telephonyDnsSecondaryDns,'ipAddressConfigLocalHost':ipAddressConfigLocalHost,_x:localHostSelectConfigSource,_y:localHostFqdnSelectConfigSource,_z:localHostWanAddressSelectConfigSource,_A0:localHostDnsOverrideEnable,'ipAddressConfigLocalHostStatic':ipAddressConfigLocalHostStatic,_A1:localHostStaticAddress,_A2:localHostStaticPrimaryDns,_A3:localHostStaticSecondaryDns,_A4:localHostStaticDefaultRouter,_A5:localHostStaticSnmpPort,_A6:localHostStaticSubnetMask,_A7:localHostStaticFqdn,_A8:localHostStaticWanAddress,'ipAddressConfigTelephonyDns':ipAddressConfigTelephonyDns,_A9:telephonyDnsOverrideEnable,'ipAddressConfigTelephonyDnsStatic':ipAddressConfigTelephonyDnsStatic,_AA:telephonyDnsStaticPrimaryDns,_AB:telephonyDnsStaticSecondaryDns,'sysConfigMIB':sysConfigMIB,'sysConfigMIBObjects':sysConfigMIBObjects,_Y:sysConfigNetworkEthernetSpeed,_Z:sysConfigComputerEthernetSpeed,_a:sysConfigMinDynamicPort,_b:sysConfigMaxDynamicPort,_c:sysConfigDhcpWait,_d:sysConfigDhcpWaitDelay,_e:sysConfigBootpFlags,_f:sysConfigProductNamePadding,'sysConfigStats':sysConfigStats,_g:sysConfigStatsPeriodLength,_h:sysConfigStatsNumberPeriods,_i:sysConfigStatsBySyslogEnable,'sysConfigDownloadConfig':sysConfigDownloadConfig,_j:sysConfigDownloadConfigFile,_k:sysConfigDownloadConfigMode,'sysConfigConformance':sysConfigConformance,'sysConfigCompliances':sysConfigCompliances,'sysConfigComplVer1':sysConfigComplVer1,'sysConfigGroups':sysConfigGroups,_AE:sysConfigGroupVer1,_AF:commonLocalHostGroupVer1,_AG:telephonyDnsGroupVer1})