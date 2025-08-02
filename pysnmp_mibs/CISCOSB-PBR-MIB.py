_L='read-write'
_K='not-accessible'
_J='active'
_I='rlRouteMapPbrRouteMapSectionId'
_H='rlRouteMapPbrRouteMapName'
_G='rlPBRInetType'
_F='rlPBRIfIndex'
_E='DisplayString'
_D='CISCOSB-ROUTEMAP-MIB'
_C='CISCOSB-PBR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
rlRouteMapPbrRouteMapName,rlRouteMapPbrRouteMapSectionId=mibBuilder.importSymbols(_D,_H,_I)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressIPv6,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
rlPolicyBasedRouting=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,228))
if mibBuilder.loadTexts:rlPolicyBasedRouting.setRevisions(('2015-06-08 00:00',))
class RlPBRInetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
class RlPBRStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('noIp',2),('interfaceDown',3)))
class RlPBRNexthopStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('notReachable',2),('notDirect',3)))
_RlPBRTable_Object=MibTable
rlPBRTable=_RlPBRTable_Object((1,3,6,1,4,1,9,6,1,101,228,1))
if mibBuilder.loadTexts:rlPBRTable.setStatus(_A)
_RlPBREntry_Object=MibTableRow
rlPBREntry=_RlPBREntry_Object((1,3,6,1,4,1,9,6,1,101,228,1,1))
rlPBREntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rlPBREntry.setStatus(_A)
_RlPBRIfIndex_Type=InterfaceIndex
_RlPBRIfIndex_Object=MibTableColumn
rlPBRIfIndex=_RlPBRIfIndex_Object((1,3,6,1,4,1,9,6,1,101,228,1,1,1),_RlPBRIfIndex_Type())
rlPBRIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rlPBRIfIndex.setStatus(_A)
_RlPBRInetType_Type=RlPBRInetType
_RlPBRInetType_Object=MibTableColumn
rlPBRInetType=_RlPBRInetType_Object((1,3,6,1,4,1,9,6,1,101,228,1,1,2),_RlPBRInetType_Type())
rlPBRInetType.setMaxAccess(_K)
if mibBuilder.loadTexts:rlPBRInetType.setStatus(_A)
class _RlPBRRouteMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlPBRRouteMapName_Type.__name__=_E
_RlPBRRouteMapName_Object=MibTableColumn
rlPBRRouteMapName=_RlPBRRouteMapName_Object((1,3,6,1,4,1,9,6,1,101,228,1,1,3),_RlPBRRouteMapName_Type())
rlPBRRouteMapName.setMaxAccess(_L)
if mibBuilder.loadTexts:rlPBRRouteMapName.setStatus(_A)
_RlPBRStatus_Type=RlPBRStatusType
_RlPBRStatus_Object=MibTableColumn
rlPBRStatus=_RlPBRStatus_Object((1,3,6,1,4,1,9,6,1,101,228,1,1,4),_RlPBRStatus_Type())
rlPBRStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRStatus.setStatus(_A)
_RlPBRRowStatus_Type=RowStatus
_RlPBRRowStatus_Object=MibTableColumn
rlPBRRowStatus=_RlPBRRowStatus_Object((1,3,6,1,4,1,9,6,1,101,228,1,1,5),_RlPBRRowStatus_Type())
rlPBRRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:rlPBRRowStatus.setStatus(_A)
_RlPBRInfoTable_Object=MibTable
rlPBRInfoTable=_RlPBRInfoTable_Object((1,3,6,1,4,1,9,6,1,101,228,2))
if mibBuilder.loadTexts:rlPBRInfoTable.setStatus(_A)
_RlPBRInfoEntry_Object=MibTableRow
rlPBRInfoEntry=_RlPBRInfoEntry_Object((1,3,6,1,4,1,9,6,1,101,228,2,1))
rlPBRInfoEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:rlPBRInfoEntry.setStatus(_A)
class _RlPBRInfoAccessListName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlPBRInfoAccessListName_Type.__name__=_E
_RlPBRInfoAccessListName_Object=MibTableColumn
rlPBRInfoAccessListName=_RlPBRInfoAccessListName_Object((1,3,6,1,4,1,9,6,1,101,228,2,1,1),_RlPBRInfoAccessListName_Type())
rlPBRInfoAccessListName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRInfoAccessListName.setStatus(_A)
_RlPBRInfoNexthopInetAddressType_Type=InetAddressType
_RlPBRInfoNexthopInetAddressType_Object=MibTableColumn
rlPBRInfoNexthopInetAddressType=_RlPBRInfoNexthopInetAddressType_Object((1,3,6,1,4,1,9,6,1,101,228,2,1,2),_RlPBRInfoNexthopInetAddressType_Type())
rlPBRInfoNexthopInetAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRInfoNexthopInetAddressType.setStatus(_A)
_RlPBRInfoNexthopInetAddress_Type=InetAddress
_RlPBRInfoNexthopInetAddress_Object=MibTableColumn
rlPBRInfoNexthopInetAddress=_RlPBRInfoNexthopInetAddress_Object((1,3,6,1,4,1,9,6,1,101,228,2,1,3),_RlPBRInfoNexthopInetAddress_Type())
rlPBRInfoNexthopInetAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRInfoNexthopInetAddress.setStatus(_A)
_RlPBRInfoNexthopIfIndex_Type=InterfaceIndexOrZero
_RlPBRInfoNexthopIfIndex_Object=MibTableColumn
rlPBRInfoNexthopIfIndex=_RlPBRInfoNexthopIfIndex_Object((1,3,6,1,4,1,9,6,1,101,228,2,1,4),_RlPBRInfoNexthopIfIndex_Type())
rlPBRInfoNexthopIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRInfoNexthopIfIndex.setStatus(_A)
_RlPBRInfoNexthopStatus_Type=RlPBRNexthopStatusType
_RlPBRInfoNexthopStatus_Object=MibTableColumn
rlPBRInfoNexthopStatus=_RlPBRInfoNexthopStatus_Object((1,3,6,1,4,1,9,6,1,101,228,2,1,5),_RlPBRInfoNexthopStatus_Type())
rlPBRInfoNexthopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPBRInfoNexthopStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'RlPBRInetType':RlPBRInetType,'RlPBRStatusType':RlPBRStatusType,'RlPBRNexthopStatusType':RlPBRNexthopStatusType,'rlPolicyBasedRouting':rlPolicyBasedRouting,'rlPBRTable':rlPBRTable,'rlPBREntry':rlPBREntry,_F:rlPBRIfIndex,_G:rlPBRInetType,'rlPBRRouteMapName':rlPBRRouteMapName,'rlPBRStatus':rlPBRStatus,'rlPBRRowStatus':rlPBRRowStatus,'rlPBRInfoTable':rlPBRInfoTable,'rlPBRInfoEntry':rlPBRInfoEntry,'rlPBRInfoAccessListName':rlPBRInfoAccessListName,'rlPBRInfoNexthopInetAddressType':rlPBRInfoNexthopInetAddressType,'rlPBRInfoNexthopInetAddress':rlPBRInfoNexthopInetAddress,'rlPBRInfoNexthopIfIndex':rlPBRInfoNexthopIfIndex,'rlPBRInfoNexthopStatus':rlPBRInfoNexthopStatus})