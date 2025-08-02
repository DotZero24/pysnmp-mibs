_c='etsysDnsResolverQuaternaryGroup'
_b='etsysDnsResolverTertiaryGroup'
_a='etsysDnsResolverSecondaryGroup'
_Z='etsysDnsResolverPrimaryGroup'
_Y='etsysDnsResolverQuaternaryServerAddr'
_X='etsysDnsResolverQuaternaryServerAddrType'
_W='etsysDnsResolverTertiaryServerAddr'
_V='etsysDnsResolverTertiaryServerAddrType'
_U='etsysDnsResolverSecondaryServerAddr'
_T='etsysDnsResolverSecondaryServerAddrType'
_S='etsysDnsResolverEnableStatus'
_R='etsysDnsResolverQueryRetries'
_Q='etsysDnsResolverQueryTimeout'
_P='etsysDnsResolverServerPortNumber'
_O='etsysDnsResolverIpv6DnsZone'
_N='etsysDnsResolverIpv4DnsZone'
_M='etsysDnsResolverPrimaryServerAddr'
_L='etsysDnsResolverPrimaryServerAddrType'
_K='etsysDnsResolverDomainName'
_J='etsysDnsResolverServiceType'
_I='InetPortNumber'
_H='Unsigned32'
_G='Integer32'
_F='SnmpAdminString'
_E='InetAddressType'
_D='InetAddress'
_C='read-write'
_B='ENTERASYS-DNS-RESOLVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,_E,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysDnsResolverMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,63))
if mibBuilder.loadTexts:etsysDnsResolverMIB.setRevisions(('2008-08-11 15:48','2008-06-18 20:56'))
_EtsysDnsResolverObjects_ObjectIdentity=ObjectIdentity
etsysDnsResolverObjects=_EtsysDnsResolverObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,63,1))
_EtsysDnsResolverSystem_ObjectIdentity=ObjectIdentity
etsysDnsResolverSystem=_EtsysDnsResolverSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,63,1,1))
class _EtsysDnsResolverServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('recursiveOnly',1),('iterativeOnly',2),('recursiveAndIterative',3)))
_EtsysDnsResolverServiceType_Type.__name__=_G
_EtsysDnsResolverServiceType_Object=MibScalar
etsysDnsResolverServiceType=_EtsysDnsResolverServiceType_Object((1,3,6,1,4,1,5624,1,2,63,1,1,1),_EtsysDnsResolverServiceType_Type())
etsysDnsResolverServiceType.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysDnsResolverServiceType.setStatus(_A)
class _EtsysDnsResolverDomainName_Type(SnmpAdminString):defaultHexValue=''
_EtsysDnsResolverDomainName_Type.__name__=_F
_EtsysDnsResolverDomainName_Object=MibScalar
etsysDnsResolverDomainName=_EtsysDnsResolverDomainName_Object((1,3,6,1,4,1,5624,1,2,63,1,1,2),_EtsysDnsResolverDomainName_Type())
etsysDnsResolverDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverDomainName.setStatus(_A)
class _EtsysDnsResolverPrimaryServerAddrType_Type(InetAddressType):defaultValue=0
_EtsysDnsResolverPrimaryServerAddrType_Type.__name__=_E
_EtsysDnsResolverPrimaryServerAddrType_Object=MibScalar
etsysDnsResolverPrimaryServerAddrType=_EtsysDnsResolverPrimaryServerAddrType_Object((1,3,6,1,4,1,5624,1,2,63,1,1,3),_EtsysDnsResolverPrimaryServerAddrType_Type())
etsysDnsResolverPrimaryServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverPrimaryServerAddrType.setStatus(_A)
class _EtsysDnsResolverPrimaryServerAddr_Type(InetAddress):defaultHexValue=''
_EtsysDnsResolverPrimaryServerAddr_Type.__name__=_D
_EtsysDnsResolverPrimaryServerAddr_Object=MibScalar
etsysDnsResolverPrimaryServerAddr=_EtsysDnsResolverPrimaryServerAddr_Object((1,3,6,1,4,1,5624,1,2,63,1,1,4),_EtsysDnsResolverPrimaryServerAddr_Type())
etsysDnsResolverPrimaryServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverPrimaryServerAddr.setStatus(_A)
class _EtsysDnsResolverSecondaryServerAddrType_Type(InetAddressType):defaultValue=0
_EtsysDnsResolverSecondaryServerAddrType_Type.__name__=_E
_EtsysDnsResolverSecondaryServerAddrType_Object=MibScalar
etsysDnsResolverSecondaryServerAddrType=_EtsysDnsResolverSecondaryServerAddrType_Object((1,3,6,1,4,1,5624,1,2,63,1,1,5),_EtsysDnsResolverSecondaryServerAddrType_Type())
etsysDnsResolverSecondaryServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverSecondaryServerAddrType.setStatus(_A)
class _EtsysDnsResolverSecondaryServerAddr_Type(InetAddress):defaultHexValue=''
_EtsysDnsResolverSecondaryServerAddr_Type.__name__=_D
_EtsysDnsResolverSecondaryServerAddr_Object=MibScalar
etsysDnsResolverSecondaryServerAddr=_EtsysDnsResolverSecondaryServerAddr_Object((1,3,6,1,4,1,5624,1,2,63,1,1,6),_EtsysDnsResolverSecondaryServerAddr_Type())
etsysDnsResolverSecondaryServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverSecondaryServerAddr.setStatus(_A)
class _EtsysDnsResolverTertiaryServerAddrType_Type(InetAddressType):defaultValue=0
_EtsysDnsResolverTertiaryServerAddrType_Type.__name__=_E
_EtsysDnsResolverTertiaryServerAddrType_Object=MibScalar
etsysDnsResolverTertiaryServerAddrType=_EtsysDnsResolverTertiaryServerAddrType_Object((1,3,6,1,4,1,5624,1,2,63,1,1,7),_EtsysDnsResolverTertiaryServerAddrType_Type())
etsysDnsResolverTertiaryServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverTertiaryServerAddrType.setStatus(_A)
class _EtsysDnsResolverTertiaryServerAddr_Type(InetAddress):defaultHexValue=''
_EtsysDnsResolverTertiaryServerAddr_Type.__name__=_D
_EtsysDnsResolverTertiaryServerAddr_Object=MibScalar
etsysDnsResolverTertiaryServerAddr=_EtsysDnsResolverTertiaryServerAddr_Object((1,3,6,1,4,1,5624,1,2,63,1,1,8),_EtsysDnsResolverTertiaryServerAddr_Type())
etsysDnsResolverTertiaryServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverTertiaryServerAddr.setStatus(_A)
class _EtsysDnsResolverQuaternaryServerAddrType_Type(InetAddressType):defaultValue=0
_EtsysDnsResolverQuaternaryServerAddrType_Type.__name__=_E
_EtsysDnsResolverQuaternaryServerAddrType_Object=MibScalar
etsysDnsResolverQuaternaryServerAddrType=_EtsysDnsResolverQuaternaryServerAddrType_Object((1,3,6,1,4,1,5624,1,2,63,1,1,9),_EtsysDnsResolverQuaternaryServerAddrType_Type())
etsysDnsResolverQuaternaryServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverQuaternaryServerAddrType.setStatus(_A)
class _EtsysDnsResolverQuaternaryServerAddr_Type(InetAddress):defaultHexValue=''
_EtsysDnsResolverQuaternaryServerAddr_Type.__name__=_D
_EtsysDnsResolverQuaternaryServerAddr_Object=MibScalar
etsysDnsResolverQuaternaryServerAddr=_EtsysDnsResolverQuaternaryServerAddr_Object((1,3,6,1,4,1,5624,1,2,63,1,1,10),_EtsysDnsResolverQuaternaryServerAddr_Type())
etsysDnsResolverQuaternaryServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverQuaternaryServerAddr.setStatus(_A)
class _EtsysDnsResolverIpv4DnsZone_Type(SnmpAdminString):defaultValue=OctetString('in-addr.arpa')
_EtsysDnsResolverIpv4DnsZone_Type.__name__=_F
_EtsysDnsResolverIpv4DnsZone_Object=MibScalar
etsysDnsResolverIpv4DnsZone=_EtsysDnsResolverIpv4DnsZone_Object((1,3,6,1,4,1,5624,1,2,63,1,1,11),_EtsysDnsResolverIpv4DnsZone_Type())
etsysDnsResolverIpv4DnsZone.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverIpv4DnsZone.setStatus(_A)
class _EtsysDnsResolverIpv6DnsZone_Type(SnmpAdminString):defaultValue=OctetString('ip6.arpa')
_EtsysDnsResolverIpv6DnsZone_Type.__name__=_F
_EtsysDnsResolverIpv6DnsZone_Object=MibScalar
etsysDnsResolverIpv6DnsZone=_EtsysDnsResolverIpv6DnsZone_Object((1,3,6,1,4,1,5624,1,2,63,1,1,12),_EtsysDnsResolverIpv6DnsZone_Type())
etsysDnsResolverIpv6DnsZone.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverIpv6DnsZone.setStatus(_A)
class _EtsysDnsResolverServerPortNumber_Type(InetPortNumber):defaultValue=53
_EtsysDnsResolverServerPortNumber_Type.__name__=_I
_EtsysDnsResolverServerPortNumber_Object=MibScalar
etsysDnsResolverServerPortNumber=_EtsysDnsResolverServerPortNumber_Object((1,3,6,1,4,1,5624,1,2,63,1,1,13),_EtsysDnsResolverServerPortNumber_Type())
etsysDnsResolverServerPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverServerPortNumber.setStatus(_A)
class _EtsysDnsResolverQueryTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EtsysDnsResolverQueryTimeout_Type.__name__=_H
_EtsysDnsResolverQueryTimeout_Object=MibScalar
etsysDnsResolverQueryTimeout=_EtsysDnsResolverQueryTimeout_Object((1,3,6,1,4,1,5624,1,2,63,1,1,14),_EtsysDnsResolverQueryTimeout_Type())
etsysDnsResolverQueryTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverQueryTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysDnsResolverQueryTimeout.setUnits('seconds')
class _EtsysDnsResolverQueryRetries_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_EtsysDnsResolverQueryRetries_Type.__name__=_H
_EtsysDnsResolverQueryRetries_Object=MibScalar
etsysDnsResolverQueryRetries=_EtsysDnsResolverQueryRetries_Object((1,3,6,1,4,1,5624,1,2,63,1,1,15),_EtsysDnsResolverQueryRetries_Type())
etsysDnsResolverQueryRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverQueryRetries.setStatus(_A)
class _EtsysDnsResolverEnableStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EtsysDnsResolverEnableStatus_Type.__name__=_G
_EtsysDnsResolverEnableStatus_Object=MibScalar
etsysDnsResolverEnableStatus=_EtsysDnsResolverEnableStatus_Object((1,3,6,1,4,1,5624,1,2,63,1,1,16),_EtsysDnsResolverEnableStatus_Type())
etsysDnsResolverEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDnsResolverEnableStatus.setStatus(_A)
_EtsysDnsResolverConformance_ObjectIdentity=ObjectIdentity
etsysDnsResolverConformance=_EtsysDnsResolverConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,63,2))
_EtsysDnsResolverGroups_ObjectIdentity=ObjectIdentity
etsysDnsResolverGroups=_EtsysDnsResolverGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,63,2,1))
_EtsysDnsResolverCompliances_ObjectIdentity=ObjectIdentity
etsysDnsResolverCompliances=_EtsysDnsResolverCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,63,2,2))
etsysDnsResolverPrimaryGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,63,2,1,1))
etsysDnsResolverPrimaryGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:etsysDnsResolverPrimaryGroup.setStatus(_A)
etsysDnsResolverSecondaryGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,63,2,1,2))
etsysDnsResolverSecondaryGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:etsysDnsResolverSecondaryGroup.setStatus(_A)
etsysDnsResolverTertiaryGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,63,2,1,3))
etsysDnsResolverTertiaryGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:etsysDnsResolverTertiaryGroup.setStatus(_A)
etsysDnsResolverQuaternaryGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,63,2,1,4))
etsysDnsResolverQuaternaryGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:etsysDnsResolverQuaternaryGroup.setStatus(_A)
etsysDnsResolverCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,63,2,2,1))
etsysDnsResolverCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:etsysDnsResolverCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysDnsResolverMIB':etsysDnsResolverMIB,'etsysDnsResolverObjects':etsysDnsResolverObjects,'etsysDnsResolverSystem':etsysDnsResolverSystem,_J:etsysDnsResolverServiceType,_K:etsysDnsResolverDomainName,_L:etsysDnsResolverPrimaryServerAddrType,_M:etsysDnsResolverPrimaryServerAddr,_T:etsysDnsResolverSecondaryServerAddrType,_U:etsysDnsResolverSecondaryServerAddr,_V:etsysDnsResolverTertiaryServerAddrType,_W:etsysDnsResolverTertiaryServerAddr,_X:etsysDnsResolverQuaternaryServerAddrType,_Y:etsysDnsResolverQuaternaryServerAddr,_N:etsysDnsResolverIpv4DnsZone,_O:etsysDnsResolverIpv6DnsZone,_P:etsysDnsResolverServerPortNumber,_Q:etsysDnsResolverQueryTimeout,_R:etsysDnsResolverQueryRetries,_S:etsysDnsResolverEnableStatus,'etsysDnsResolverConformance':etsysDnsResolverConformance,'etsysDnsResolverGroups':etsysDnsResolverGroups,_Z:etsysDnsResolverPrimaryGroup,_a:etsysDnsResolverSecondaryGroup,_b:etsysDnsResolverTertiaryGroup,_c:etsysDnsResolverQuaternaryGroup,'etsysDnsResolverCompliances':etsysDnsResolverCompliances,'etsysDnsResolverCompliance':etsysDnsResolverCompliance})