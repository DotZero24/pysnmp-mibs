_H='read-write'
_G='zyIpv6StaticRouteDestinationAddressPrefixLength'
_F='zyIpv6StaticRouteDestinationIpAddress'
_E='zyIpv6StaticRouteDestinationIpAddressType'
_D='read-only'
_C='not-accessible'
_B='ZYXEL-IPV6-STATIC-ROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpv6StaticRoute=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,37))
_ZyxelIpv6StaticRouteSetup_ObjectIdentity=ObjectIdentity
zyxelIpv6StaticRouteSetup=_ZyxelIpv6StaticRouteSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,37,1))
_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Type=Integer32
_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Object=MibScalar
zyIpv6StaticRouteMaxNumberOfStaticRoutes=_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Object((1,3,6,1,4,1,890,1,15,3,37,1,1),_ZyIpv6StaticRouteMaxNumberOfStaticRoutes_Type())
zyIpv6StaticRouteMaxNumberOfStaticRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6StaticRouteMaxNumberOfStaticRoutes.setStatus(_A)
_ZyxelIpv6StaticRouteTable_Object=MibTable
zyxelIpv6StaticRouteTable=_ZyxelIpv6StaticRouteTable_Object((1,3,6,1,4,1,890,1,15,3,37,1,2))
if mibBuilder.loadTexts:zyxelIpv6StaticRouteTable.setStatus(_A)
_ZyxelIpv6StaticRouteEntry_Object=MibTableRow
zyxelIpv6StaticRouteEntry=_ZyxelIpv6StaticRouteEntry_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1))
zyxelIpv6StaticRouteEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:zyxelIpv6StaticRouteEntry.setStatus(_A)
_ZyIpv6StaticRouteDestinationIpAddressType_Type=InetAddressType
_ZyIpv6StaticRouteDestinationIpAddressType_Object=MibTableColumn
zyIpv6StaticRouteDestinationIpAddressType=_ZyIpv6StaticRouteDestinationIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,1),_ZyIpv6StaticRouteDestinationIpAddressType_Type())
zyIpv6StaticRouteDestinationIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpv6StaticRouteDestinationIpAddressType.setStatus(_A)
_ZyIpv6StaticRouteDestinationIpAddress_Type=InetAddress
_ZyIpv6StaticRouteDestinationIpAddress_Object=MibTableColumn
zyIpv6StaticRouteDestinationIpAddress=_ZyIpv6StaticRouteDestinationIpAddress_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,2),_ZyIpv6StaticRouteDestinationIpAddress_Type())
zyIpv6StaticRouteDestinationIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpv6StaticRouteDestinationIpAddress.setStatus(_A)
_ZyIpv6StaticRouteDestinationAddressPrefixLength_Type=Integer32
_ZyIpv6StaticRouteDestinationAddressPrefixLength_Object=MibTableColumn
zyIpv6StaticRouteDestinationAddressPrefixLength=_ZyIpv6StaticRouteDestinationAddressPrefixLength_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,3),_ZyIpv6StaticRouteDestinationAddressPrefixLength_Type())
zyIpv6StaticRouteDestinationAddressPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpv6StaticRouteDestinationAddressPrefixLength.setStatus(_A)
_ZyIpv6StaticRouteNextHopIpAddressType_Type=InetAddressType
_ZyIpv6StaticRouteNextHopIpAddressType_Object=MibTableColumn
zyIpv6StaticRouteNextHopIpAddressType=_ZyIpv6StaticRouteNextHopIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,4),_ZyIpv6StaticRouteNextHopIpAddressType_Type())
zyIpv6StaticRouteNextHopIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyIpv6StaticRouteNextHopIpAddressType.setStatus(_A)
_ZyIpv6StaticRouteNextHopIpAddress_Type=InetAddress
_ZyIpv6StaticRouteNextHopIpAddress_Object=MibTableColumn
zyIpv6StaticRouteNextHopIpAddress=_ZyIpv6StaticRouteNextHopIpAddress_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,5),_ZyIpv6StaticRouteNextHopIpAddress_Type())
zyIpv6StaticRouteNextHopIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zyIpv6StaticRouteNextHopIpAddress.setStatus(_A)
_ZyIpv6StaticRouteIfIndex_Type=Integer32
_ZyIpv6StaticRouteIfIndex_Object=MibTableColumn
zyIpv6StaticRouteIfIndex=_ZyIpv6StaticRouteIfIndex_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,6),_ZyIpv6StaticRouteIfIndex_Type())
zyIpv6StaticRouteIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:zyIpv6StaticRouteIfIndex.setStatus(_A)
_ZyIpv6StaticRouteRowStatus_Type=RowStatus
_ZyIpv6StaticRouteRowStatus_Object=MibTableColumn
zyIpv6StaticRouteRowStatus=_ZyIpv6StaticRouteRowStatus_Object((1,3,6,1,4,1,890,1,15,3,37,1,2,1,7),_ZyIpv6StaticRouteRowStatus_Type())
zyIpv6StaticRouteRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyIpv6StaticRouteRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIpv6StaticRoute':zyxelIpv6StaticRoute,'zyxelIpv6StaticRouteSetup':zyxelIpv6StaticRouteSetup,'zyIpv6StaticRouteMaxNumberOfStaticRoutes':zyIpv6StaticRouteMaxNumberOfStaticRoutes,'zyxelIpv6StaticRouteTable':zyxelIpv6StaticRouteTable,'zyxelIpv6StaticRouteEntry':zyxelIpv6StaticRouteEntry,_E:zyIpv6StaticRouteDestinationIpAddressType,_F:zyIpv6StaticRouteDestinationIpAddress,_G:zyIpv6StaticRouteDestinationAddressPrefixLength,'zyIpv6StaticRouteNextHopIpAddressType':zyIpv6StaticRouteNextHopIpAddressType,'zyIpv6StaticRouteNextHopIpAddress':zyIpv6StaticRouteNextHopIpAddress,'zyIpv6StaticRouteIfIndex':zyIpv6StaticRouteIfIndex,'zyIpv6StaticRouteRowStatus':zyIpv6StaticRouteRowStatus})