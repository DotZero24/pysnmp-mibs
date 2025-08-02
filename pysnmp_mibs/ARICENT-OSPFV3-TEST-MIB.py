_K='futOspfv3ExtRouteNextHop'
_J='futOspfv3ExtRouteNextHopType'
_I='futOspfv3ExtRoutePfxLength'
_H='futOspfv3ExtRouteDest'
_G='futOspfv3ExtRouteDestType'
_F='futOspfv3TestIfIndex'
_E='Integer32'
_D='InetAddress'
_C='not-accessible'
_B='ARICENT-OSPFV3-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futOspfv3TestGroup=ModuleIdentity((1,3,6,1,4,1,2076,301))
if mibBuilder.loadTexts:futOspfv3TestGroup.setRevisions(('2012-09-05 00:00',))
_FutOspfv3TestIfTable_Object=MibTable
futOspfv3TestIfTable=_FutOspfv3TestIfTable_Object((1,3,6,1,4,1,2076,301,1))
if mibBuilder.loadTexts:futOspfv3TestIfTable.setStatus(_A)
_FutOspfv3TestIfEntry_Object=MibTableRow
futOspfv3TestIfEntry=_FutOspfv3TestIfEntry_Object((1,3,6,1,4,1,2076,301,1,1))
futOspfv3TestIfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:futOspfv3TestIfEntry.setStatus(_A)
_FutOspfv3TestIfIndex_Type=InterfaceIndex
_FutOspfv3TestIfIndex_Object=MibTableColumn
futOspfv3TestIfIndex=_FutOspfv3TestIfIndex_Object((1,3,6,1,4,1,2076,301,1,1,1),_FutOspfv3TestIfIndex_Type())
futOspfv3TestIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3TestIfIndex.setStatus(_A)
class _FutOspfv3TestDemandTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
_FutOspfv3TestDemandTraffic_Type.__name__=_E
_FutOspfv3TestDemandTraffic_Object=MibTableColumn
futOspfv3TestDemandTraffic=_FutOspfv3TestDemandTraffic_Object((1,3,6,1,4,1,2076,301,1,1,2),_FutOspfv3TestDemandTraffic_Type())
futOspfv3TestDemandTraffic.setMaxAccess('read-write')
if mibBuilder.loadTexts:futOspfv3TestDemandTraffic.setStatus(_A)
_FutOspfv3ExtRouteTable_Object=MibTable
futOspfv3ExtRouteTable=_FutOspfv3ExtRouteTable_Object((1,3,6,1,4,1,2076,301,2))
if mibBuilder.loadTexts:futOspfv3ExtRouteTable.setStatus(_A)
_FutOspfv3ExtRouteEntry_Object=MibTableRow
futOspfv3ExtRouteEntry=_FutOspfv3ExtRouteEntry_Object((1,3,6,1,4,1,2076,301,2,1))
futOspfv3ExtRouteEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:futOspfv3ExtRouteEntry.setStatus(_A)
_FutOspfv3ExtRouteDestType_Type=InetAddressType
_FutOspfv3ExtRouteDestType_Object=MibTableColumn
futOspfv3ExtRouteDestType=_FutOspfv3ExtRouteDestType_Object((1,3,6,1,4,1,2076,301,2,1,1),_FutOspfv3ExtRouteDestType_Type())
futOspfv3ExtRouteDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3ExtRouteDestType.setStatus(_A)
class _FutOspfv3ExtRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3ExtRouteDest_Type.__name__=_D
_FutOspfv3ExtRouteDest_Object=MibTableColumn
futOspfv3ExtRouteDest=_FutOspfv3ExtRouteDest_Object((1,3,6,1,4,1,2076,301,2,1,2),_FutOspfv3ExtRouteDest_Type())
futOspfv3ExtRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3ExtRouteDest.setStatus(_A)
_FutOspfv3ExtRoutePfxLength_Type=InetAddressPrefixLength
_FutOspfv3ExtRoutePfxLength_Object=MibTableColumn
futOspfv3ExtRoutePfxLength=_FutOspfv3ExtRoutePfxLength_Object((1,3,6,1,4,1,2076,301,2,1,3),_FutOspfv3ExtRoutePfxLength_Type())
futOspfv3ExtRoutePfxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3ExtRoutePfxLength.setStatus(_A)
_FutOspfv3ExtRouteNextHopType_Type=InetAddressType
_FutOspfv3ExtRouteNextHopType_Object=MibTableColumn
futOspfv3ExtRouteNextHopType=_FutOspfv3ExtRouteNextHopType_Object((1,3,6,1,4,1,2076,301,2,1,4),_FutOspfv3ExtRouteNextHopType_Type())
futOspfv3ExtRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3ExtRouteNextHopType.setStatus(_A)
class _FutOspfv3ExtRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FutOspfv3ExtRouteNextHop_Type.__name__=_D
_FutOspfv3ExtRouteNextHop_Object=MibTableColumn
futOspfv3ExtRouteNextHop=_FutOspfv3ExtRouteNextHop_Object((1,3,6,1,4,1,2076,301,2,1,5),_FutOspfv3ExtRouteNextHop_Type())
futOspfv3ExtRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:futOspfv3ExtRouteNextHop.setStatus(_A)
_FutOspfv3ExtRouteStatus_Type=RowStatus
_FutOspfv3ExtRouteStatus_Object=MibTableColumn
futOspfv3ExtRouteStatus=_FutOspfv3ExtRouteStatus_Object((1,3,6,1,4,1,2076,301,2,1,6),_FutOspfv3ExtRouteStatus_Type())
futOspfv3ExtRouteStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:futOspfv3ExtRouteStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'futOspfv3TestGroup':futOspfv3TestGroup,'futOspfv3TestIfTable':futOspfv3TestIfTable,'futOspfv3TestIfEntry':futOspfv3TestIfEntry,_F:futOspfv3TestIfIndex,'futOspfv3TestDemandTraffic':futOspfv3TestDemandTraffic,'futOspfv3ExtRouteTable':futOspfv3ExtRouteTable,'futOspfv3ExtRouteEntry':futOspfv3ExtRouteEntry,_G:futOspfv3ExtRouteDestType,_H:futOspfv3ExtRouteDest,_I:futOspfv3ExtRoutePfxLength,_J:futOspfv3ExtRouteNextHopType,_K:futOspfv3ExtRouteNextHop,'futOspfv3ExtRouteStatus':futOspfv3ExtRouteStatus})