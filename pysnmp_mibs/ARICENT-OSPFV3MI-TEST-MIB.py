_M='fsMIOspfv3ExtRouteNextHop'
_L='fsMIOspfv3ExtRouteNextHopType'
_K='fsMIOspfv3ExtRoutePfxLength'
_J='fsMIOspfv3ExtRouteDest'
_I='fsMIOspfv3ExtRouteDestType'
_H='fsMIOspfv3TestIfIndex'
_G='Integer32'
_F='fsMIStdOspfv3ContextId'
_E='ARICENT-MISTDOSPFV3-MIB'
_D='InetAddress'
_C='not-accessible'
_B='ARICENT-OSPFV3MI-TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMIStdOspfv3ContextId,=mibBuilder.importSymbols(_E,_F)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMIOspfv3TestGroup=ModuleIdentity((1,3,6,1,4,1,2076,2,24,100))
if mibBuilder.loadTexts:fsMIOspfv3TestGroup.setRevisions(('2012-09-05 00:00',))
_FsMIOspfv3TestIfTable_Object=MibTable
fsMIOspfv3TestIfTable=_FsMIOspfv3TestIfTable_Object((1,3,6,1,4,1,2076,2,24,100,1))
if mibBuilder.loadTexts:fsMIOspfv3TestIfTable.setStatus(_A)
_FsMIOspfv3TestIfEntry_Object=MibTableRow
fsMIOspfv3TestIfEntry=_FsMIOspfv3TestIfEntry_Object((1,3,6,1,4,1,2076,2,24,100,1,1))
fsMIOspfv3TestIfEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:fsMIOspfv3TestIfEntry.setStatus(_A)
_FsMIOspfv3TestIfIndex_Type=InterfaceIndex
_FsMIOspfv3TestIfIndex_Object=MibTableColumn
fsMIOspfv3TestIfIndex=_FsMIOspfv3TestIfIndex_Object((1,3,6,1,4,1,2076,2,24,100,1,1,1),_FsMIOspfv3TestIfIndex_Type())
fsMIOspfv3TestIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3TestIfIndex.setStatus(_A)
class _FsMIOspfv3TestDemandTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
_FsMIOspfv3TestDemandTraffic_Type.__name__=_G
_FsMIOspfv3TestDemandTraffic_Object=MibTableColumn
fsMIOspfv3TestDemandTraffic=_FsMIOspfv3TestDemandTraffic_Object((1,3,6,1,4,1,2076,2,24,100,1,1,2),_FsMIOspfv3TestDemandTraffic_Type())
fsMIOspfv3TestDemandTraffic.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsMIOspfv3TestDemandTraffic.setStatus(_A)
_FsMIOspfv3TestIfContextId_Type=Integer32
_FsMIOspfv3TestIfContextId_Object=MibTableColumn
fsMIOspfv3TestIfContextId=_FsMIOspfv3TestIfContextId_Object((1,3,6,1,4,1,2076,2,24,100,1,1,3),_FsMIOspfv3TestIfContextId_Type())
fsMIOspfv3TestIfContextId.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsMIOspfv3TestIfContextId.setStatus(_A)
_FsMIOspfv3ExtRouteTable_Object=MibTable
fsMIOspfv3ExtRouteTable=_FsMIOspfv3ExtRouteTable_Object((1,3,6,1,4,1,2076,2,24,100,2))
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteTable.setStatus(_A)
_FsMIOspfv3ExtRouteEntry_Object=MibTableRow
fsMIOspfv3ExtRouteEntry=_FsMIOspfv3ExtRouteEntry_Object((1,3,6,1,4,1,2076,2,24,100,2,1))
fsMIOspfv3ExtRouteEntry.setIndexNames((0,_E,_F),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteEntry.setStatus(_A)
_FsMIOspfv3ExtRouteDestType_Type=InetAddressType
_FsMIOspfv3ExtRouteDestType_Object=MibTableColumn
fsMIOspfv3ExtRouteDestType=_FsMIOspfv3ExtRouteDestType_Object((1,3,6,1,4,1,2076,2,24,100,2,1,1),_FsMIOspfv3ExtRouteDestType_Type())
fsMIOspfv3ExtRouteDestType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteDestType.setStatus(_A)
class _FsMIOspfv3ExtRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3ExtRouteDest_Type.__name__=_D
_FsMIOspfv3ExtRouteDest_Object=MibTableColumn
fsMIOspfv3ExtRouteDest=_FsMIOspfv3ExtRouteDest_Object((1,3,6,1,4,1,2076,2,24,100,2,1,2),_FsMIOspfv3ExtRouteDest_Type())
fsMIOspfv3ExtRouteDest.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteDest.setStatus(_A)
_FsMIOspfv3ExtRoutePfxLength_Type=InetAddressPrefixLength
_FsMIOspfv3ExtRoutePfxLength_Object=MibTableColumn
fsMIOspfv3ExtRoutePfxLength=_FsMIOspfv3ExtRoutePfxLength_Object((1,3,6,1,4,1,2076,2,24,100,2,1,3),_FsMIOspfv3ExtRoutePfxLength_Type())
fsMIOspfv3ExtRoutePfxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3ExtRoutePfxLength.setStatus(_A)
_FsMIOspfv3ExtRouteNextHopType_Type=InetAddressType
_FsMIOspfv3ExtRouteNextHopType_Object=MibTableColumn
fsMIOspfv3ExtRouteNextHopType=_FsMIOspfv3ExtRouteNextHopType_Object((1,3,6,1,4,1,2076,2,24,100,2,1,4),_FsMIOspfv3ExtRouteNextHopType_Type())
fsMIOspfv3ExtRouteNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteNextHopType.setStatus(_A)
class _FsMIOspfv3ExtRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIOspfv3ExtRouteNextHop_Type.__name__=_D
_FsMIOspfv3ExtRouteNextHop_Object=MibTableColumn
fsMIOspfv3ExtRouteNextHop=_FsMIOspfv3ExtRouteNextHop_Object((1,3,6,1,4,1,2076,2,24,100,2,1,5),_FsMIOspfv3ExtRouteNextHop_Type())
fsMIOspfv3ExtRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteNextHop.setStatus(_A)
_FsMIOspfv3ExtRouteStatus_Type=RowStatus
_FsMIOspfv3ExtRouteStatus_Object=MibTableColumn
fsMIOspfv3ExtRouteStatus=_FsMIOspfv3ExtRouteStatus_Object((1,3,6,1,4,1,2076,2,24,100,2,1,6),_FsMIOspfv3ExtRouteStatus_Type())
fsMIOspfv3ExtRouteStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMIOspfv3ExtRouteStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsMIOspfv3TestGroup':fsMIOspfv3TestGroup,'fsMIOspfv3TestIfTable':fsMIOspfv3TestIfTable,'fsMIOspfv3TestIfEntry':fsMIOspfv3TestIfEntry,_H:fsMIOspfv3TestIfIndex,'fsMIOspfv3TestDemandTraffic':fsMIOspfv3TestDemandTraffic,'fsMIOspfv3TestIfContextId':fsMIOspfv3TestIfContextId,'fsMIOspfv3ExtRouteTable':fsMIOspfv3ExtRouteTable,'fsMIOspfv3ExtRouteEntry':fsMIOspfv3ExtRouteEntry,_I:fsMIOspfv3ExtRouteDestType,_J:fsMIOspfv3ExtRouteDest,_K:fsMIOspfv3ExtRoutePfxLength,_L:fsMIOspfv3ExtRouteNextHopType,_M:fsMIOspfv3ExtRouteNextHop,'fsMIOspfv3ExtRouteStatus':fsMIOspfv3ExtRouteStatus})