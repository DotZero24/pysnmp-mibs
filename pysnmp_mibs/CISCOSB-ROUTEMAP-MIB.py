_I='not-accessible'
_H='rlRouteMapPbrInetType'
_G='rlRouteMapPbrRouteMapSectionId'
_F='rlRouteMapPbrRouteMapName'
_E='Unsigned32'
_D='DisplayString'
_C='CISCOSB-ROUTEMAP-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
rlRouteMap=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,227))
if mibBuilder.loadTexts:rlRouteMap.setRevisions(('2015-06-08 00:00',))
class RlRouteMapInetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_RlRouteMapPbrTable_Object=MibTable
rlRouteMapPbrTable=_RlRouteMapPbrTable_Object((1,3,6,1,4,1,9,6,1,101,227,1))
if mibBuilder.loadTexts:rlRouteMapPbrTable.setStatus(_A)
_RlRouteMapPbrEntry_Object=MibTableRow
rlRouteMapPbrEntry=_RlRouteMapPbrEntry_Object((1,3,6,1,4,1,9,6,1,101,227,1,1))
rlRouteMapPbrEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:rlRouteMapPbrEntry.setStatus(_A)
class _RlRouteMapPbrRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlRouteMapPbrRouteMapName_Type.__name__=_D
_RlRouteMapPbrRouteMapName_Object=MibTableColumn
rlRouteMapPbrRouteMapName=_RlRouteMapPbrRouteMapName_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,1),_RlRouteMapPbrRouteMapName_Type())
rlRouteMapPbrRouteMapName.setMaxAccess(_I)
if mibBuilder.loadTexts:rlRouteMapPbrRouteMapName.setStatus(_A)
class _RlRouteMapPbrRouteMapSectionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlRouteMapPbrRouteMapSectionId_Type.__name__=_E
_RlRouteMapPbrRouteMapSectionId_Object=MibTableColumn
rlRouteMapPbrRouteMapSectionId=_RlRouteMapPbrRouteMapSectionId_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,2),_RlRouteMapPbrRouteMapSectionId_Type())
rlRouteMapPbrRouteMapSectionId.setMaxAccess(_I)
if mibBuilder.loadTexts:rlRouteMapPbrRouteMapSectionId.setStatus(_A)
_RlRouteMapPbrInetType_Type=RlRouteMapInetType
_RlRouteMapPbrInetType_Object=MibTableColumn
rlRouteMapPbrInetType=_RlRouteMapPbrInetType_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,3),_RlRouteMapPbrInetType_Type())
rlRouteMapPbrInetType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrInetType.setStatus(_A)
class _RlRouteMapPbrMatchAccessListName_Type(DisplayString):defaultValue=OctetString('')
_RlRouteMapPbrMatchAccessListName_Type.__name__=_D
_RlRouteMapPbrMatchAccessListName_Object=MibTableColumn
rlRouteMapPbrMatchAccessListName=_RlRouteMapPbrMatchAccessListName_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,4),_RlRouteMapPbrMatchAccessListName_Type())
rlRouteMapPbrMatchAccessListName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrMatchAccessListName.setStatus(_A)
_RlRouteMapPbrActionNexthopInetAddressType_Type=InetAddressType
_RlRouteMapPbrActionNexthopInetAddressType_Object=MibTableColumn
rlRouteMapPbrActionNexthopInetAddressType=_RlRouteMapPbrActionNexthopInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,5),_RlRouteMapPbrActionNexthopInetAddressType_Type())
rlRouteMapPbrActionNexthopInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrActionNexthopInetAddressType.setStatus(_A)
_RlRouteMapPbrActionNexthopInetAddress_Type=InetAddress
_RlRouteMapPbrActionNexthopInetAddress_Object=MibTableColumn
rlRouteMapPbrActionNexthopInetAddress=_RlRouteMapPbrActionNexthopInetAddress_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,6),_RlRouteMapPbrActionNexthopInetAddress_Type())
rlRouteMapPbrActionNexthopInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrActionNexthopInetAddress.setStatus(_A)
_RlRouteMapPbrActionNexthopIfIndex_Type=InterfaceIndexOrZero
_RlRouteMapPbrActionNexthopIfIndex_Object=MibTableColumn
rlRouteMapPbrActionNexthopIfIndex=_RlRouteMapPbrActionNexthopIfIndex_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,7),_RlRouteMapPbrActionNexthopIfIndex_Type())
rlRouteMapPbrActionNexthopIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrActionNexthopIfIndex.setStatus(_A)
_RlRouteMapPbrRowStatus_Type=RowStatus
_RlRouteMapPbrRowStatus_Object=MibTableColumn
rlRouteMapPbrRowStatus=_RlRouteMapPbrRowStatus_Object((1,3,6,1,4,1,9,6,1,101,227,1,1,8),_RlRouteMapPbrRowStatus_Type())
rlRouteMapPbrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlRouteMapPbrRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlRouteMapInetType':RlRouteMapInetType,'rlRouteMap':rlRouteMap,'rlRouteMapPbrTable':rlRouteMapPbrTable,'rlRouteMapPbrEntry':rlRouteMapPbrEntry,_F:rlRouteMapPbrRouteMapName,_G:rlRouteMapPbrRouteMapSectionId,_H:rlRouteMapPbrInetType,'rlRouteMapPbrMatchAccessListName':rlRouteMapPbrMatchAccessListName,'rlRouteMapPbrActionNexthopInetAddressType':rlRouteMapPbrActionNexthopInetAddressType,'rlRouteMapPbrActionNexthopInetAddress':rlRouteMapPbrActionNexthopInetAddress,'rlRouteMapPbrActionNexthopIfIndex':rlRouteMapPbrActionNexthopIfIndex,'rlRouteMapPbrRowStatus':rlRouteMapPbrRowStatus})