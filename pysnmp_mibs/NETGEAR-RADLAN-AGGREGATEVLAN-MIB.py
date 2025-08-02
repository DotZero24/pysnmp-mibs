_H='rlAggregateSubVlanIfIndex'
_G='read-only'
_F='DisplayString'
_E='rlAggregateVlanIndex'
_D='Integer32'
_C='read-create'
_B='NETGEAR-RADLAN-AGGREGATEVLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
rlAggregateVlan=ModuleIdentity((1,3,6,1,4,1,4526,17,73))
if mibBuilder.loadTexts:rlAggregateVlan.setRevisions(('2007-01-02 00:00',))
_RlAggregateVlanMibVersion_Type=Integer32
_RlAggregateVlanMibVersion_Object=MibScalar
rlAggregateVlanMibVersion=_RlAggregateVlanMibVersion_Object((1,3,6,1,4,1,4526,17,73,1),_RlAggregateVlanMibVersion_Type())
rlAggregateVlanMibVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:rlAggregateVlanMibVersion.setStatus(_A)
_RlAggregateVlanTable_Object=MibTable
rlAggregateVlanTable=_RlAggregateVlanTable_Object((1,3,6,1,4,1,4526,17,73,2))
if mibBuilder.loadTexts:rlAggregateVlanTable.setStatus(_A)
_RlAggregateVlanEntry_Object=MibTableRow
rlAggregateVlanEntry=_RlAggregateVlanEntry_Object((1,3,6,1,4,1,4526,17,73,2,1))
rlAggregateVlanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:rlAggregateVlanEntry.setStatus(_A)
_RlAggregateVlanIndex_Type=InterfaceIndex
_RlAggregateVlanIndex_Object=MibTableColumn
rlAggregateVlanIndex=_RlAggregateVlanIndex_Object((1,3,6,1,4,1,4526,17,73,2,1,1),_RlAggregateVlanIndex_Type())
rlAggregateVlanIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rlAggregateVlanIndex.setStatus(_A)
class _RlAggregateVlanName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlAggregateVlanName_Type.__name__=_F
_RlAggregateVlanName_Object=MibTableColumn
rlAggregateVlanName=_RlAggregateVlanName_Object((1,3,6,1,4,1,4526,17,73,2,1,2),_RlAggregateVlanName_Type())
rlAggregateVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlAggregateVlanName.setStatus(_A)
class _RlAggregateVlanPhysAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('default',1),('reserve',2)))
_RlAggregateVlanPhysAddressType_Type.__name__=_D
_RlAggregateVlanPhysAddressType_Object=MibTableColumn
rlAggregateVlanPhysAddressType=_RlAggregateVlanPhysAddressType_Object((1,3,6,1,4,1,4526,17,73,2,1,3),_RlAggregateVlanPhysAddressType_Type())
rlAggregateVlanPhysAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlAggregateVlanPhysAddressType.setStatus(_A)
_RlAggregateVlanStatus_Type=RowStatus
_RlAggregateVlanStatus_Object=MibTableColumn
rlAggregateVlanStatus=_RlAggregateVlanStatus_Object((1,3,6,1,4,1,4526,17,73,2,1,4),_RlAggregateVlanStatus_Type())
rlAggregateVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlAggregateVlanStatus.setStatus(_A)
_RlAggregateSubVlanTable_Object=MibTable
rlAggregateSubVlanTable=_RlAggregateSubVlanTable_Object((1,3,6,1,4,1,4526,17,73,3))
if mibBuilder.loadTexts:rlAggregateSubVlanTable.setStatus(_A)
_RlAggregateSubVlanEntry_Object=MibTableRow
rlAggregateSubVlanEntry=_RlAggregateSubVlanEntry_Object((1,3,6,1,4,1,4526,17,73,3,1))
rlAggregateSubVlanEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:rlAggregateSubVlanEntry.setStatus(_A)
_RlAggregateSubVlanIfIndex_Type=InterfaceIndex
_RlAggregateSubVlanIfIndex_Object=MibTableColumn
rlAggregateSubVlanIfIndex=_RlAggregateSubVlanIfIndex_Object((1,3,6,1,4,1,4526,17,73,3,1,1),_RlAggregateSubVlanIfIndex_Type())
rlAggregateSubVlanIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlAggregateSubVlanIfIndex.setStatus(_A)
_RlAggregateSubVlanStatus_Type=RowStatus
_RlAggregateSubVlanStatus_Object=MibTableColumn
rlAggregateSubVlanStatus=_RlAggregateSubVlanStatus_Object((1,3,6,1,4,1,4526,17,73,3,1,2),_RlAggregateSubVlanStatus_Type())
rlAggregateSubVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlAggregateSubVlanStatus.setStatus(_A)
class _RlAggregateVlanArpProxy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_RlAggregateVlanArpProxy_Type.__name__=_D
_RlAggregateVlanArpProxy_Object=MibScalar
rlAggregateVlanArpProxy=_RlAggregateVlanArpProxy_Object((1,3,6,1,4,1,4526,17,73,4),_RlAggregateVlanArpProxy_Type())
rlAggregateVlanArpProxy.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlAggregateVlanArpProxy.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rlAggregateVlan':rlAggregateVlan,'rlAggregateVlanMibVersion':rlAggregateVlanMibVersion,'rlAggregateVlanTable':rlAggregateVlanTable,'rlAggregateVlanEntry':rlAggregateVlanEntry,_E:rlAggregateVlanIndex,'rlAggregateVlanName':rlAggregateVlanName,'rlAggregateVlanPhysAddressType':rlAggregateVlanPhysAddressType,'rlAggregateVlanStatus':rlAggregateVlanStatus,'rlAggregateSubVlanTable':rlAggregateSubVlanTable,'rlAggregateSubVlanEntry':rlAggregateSubVlanEntry,_H:rlAggregateSubVlanIfIndex,'rlAggregateSubVlanStatus':rlAggregateSubVlanStatus,'rlAggregateVlanArpProxy':rlAggregateVlanArpProxy})