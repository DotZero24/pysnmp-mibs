_F='read-only'
_E='not-accessible'
_D='zyPathMtuDiscoveryDestinationIpAddress'
_C='zyPathMtuDiscoveryDestinationIpAddressType'
_B='ZYXEL-IPV6-PATH-MTU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6PathMtu=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,36))
_ZyxelPathMtuDiscoveryStatus_ObjectIdentity=ObjectIdentity
zyxelPathMtuDiscoveryStatus=_ZyxelPathMtuDiscoveryStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,36,1))
_ZyxelPathMtuDiscoveryTable_Object=MibTable
zyxelPathMtuDiscoveryTable=_ZyxelPathMtuDiscoveryTable_Object((1,3,6,1,4,1,890,1,15,3,36,1,1))
if mibBuilder.loadTexts:zyxelPathMtuDiscoveryTable.setStatus(_A)
_ZyxelPathMtuDiscoveryEntry_Object=MibTableRow
zyxelPathMtuDiscoveryEntry=_ZyxelPathMtuDiscoveryEntry_Object((1,3,6,1,4,1,890,1,15,3,36,1,1,1))
zyxelPathMtuDiscoveryEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:zyxelPathMtuDiscoveryEntry.setStatus(_A)
_ZyPathMtuDiscoveryDestinationIpAddressType_Type=InetAddressType
_ZyPathMtuDiscoveryDestinationIpAddressType_Object=MibTableColumn
zyPathMtuDiscoveryDestinationIpAddressType=_ZyPathMtuDiscoveryDestinationIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,36,1,1,1,1),_ZyPathMtuDiscoveryDestinationIpAddressType_Type())
zyPathMtuDiscoveryDestinationIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyPathMtuDiscoveryDestinationIpAddressType.setStatus(_A)
_ZyPathMtuDiscoveryDestinationIpAddress_Type=InetAddress
_ZyPathMtuDiscoveryDestinationIpAddress_Object=MibTableColumn
zyPathMtuDiscoveryDestinationIpAddress=_ZyPathMtuDiscoveryDestinationIpAddress_Object((1,3,6,1,4,1,890,1,15,3,36,1,1,1,2),_ZyPathMtuDiscoveryDestinationIpAddress_Type())
zyPathMtuDiscoveryDestinationIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyPathMtuDiscoveryDestinationIpAddress.setStatus(_A)
_ZyPathMtuDiscoveryMtu_Type=Integer32
_ZyPathMtuDiscoveryMtu_Object=MibTableColumn
zyPathMtuDiscoveryMtu=_ZyPathMtuDiscoveryMtu_Object((1,3,6,1,4,1,890,1,15,3,36,1,1,1,3),_ZyPathMtuDiscoveryMtu_Type())
zyPathMtuDiscoveryMtu.setMaxAccess(_F)
if mibBuilder.loadTexts:zyPathMtuDiscoveryMtu.setStatus(_A)
_ZyPathMtuDiscoveryExpiredTime_Type=Gauge32
_ZyPathMtuDiscoveryExpiredTime_Object=MibTableColumn
zyPathMtuDiscoveryExpiredTime=_ZyPathMtuDiscoveryExpiredTime_Object((1,3,6,1,4,1,890,1,15,3,36,1,1,1,4),_ZyPathMtuDiscoveryExpiredTime_Type())
zyPathMtuDiscoveryExpiredTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zyPathMtuDiscoveryExpiredTime.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIpv6PathMtu':zyxelIpv6PathMtu,'zyxelPathMtuDiscoveryStatus':zyxelPathMtuDiscoveryStatus,'zyxelPathMtuDiscoveryTable':zyxelPathMtuDiscoveryTable,'zyxelPathMtuDiscoveryEntry':zyxelPathMtuDiscoveryEntry,_C:zyPathMtuDiscoveryDestinationIpAddressType,_D:zyPathMtuDiscoveryDestinationIpAddress,'zyPathMtuDiscoveryMtu':zyPathMtuDiscoveryMtu,'zyPathMtuDiscoveryExpiredTime':zyPathMtuDiscoveryExpiredTime})