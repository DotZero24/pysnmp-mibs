_K='atiVlanProtocolVlanProtocolIndex'
_J='atiVlanProtocolVlanIfIndex'
_I='atiVlanProtocolIdIndex'
_H='atiVlanProtocolIndex'
_G='atiVlanEncapsIfIndex'
_F='atiVlanIfIndex'
_E='DisplayString'
_D='Integer32'
_C='CENTRECOM-VLAN-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extSwitchMIB,=mibBuilder.importSymbols('CENTRECOM-MIB','extSwitchMIB')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
atiVlan=ModuleIdentity((1,3,6,1,4,1,207,8,12,2,4))
class AtiSwitchVlanType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('vlanLayer2',1))
class AtiSwitchVlanEncapsType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('vlanEncaps8021q',2))
_AtiVlanGroup_ObjectIdentity=ObjectIdentity
atiVlanGroup=_AtiVlanGroup_ObjectIdentity((1,3,6,1,4,1,207,8,12,2,4,1))
_AtiVlanIfTable_Object=MibTable
atiVlanIfTable=_AtiVlanIfTable_Object((1,3,6,1,4,1,207,8,12,2,4,1,2))
if mibBuilder.loadTexts:atiVlanIfTable.setStatus(_A)
_AtiVlanIfEntry_Object=MibTableRow
atiVlanIfEntry=_AtiVlanIfEntry_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1))
atiVlanIfEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:atiVlanIfEntry.setStatus(_A)
_AtiVlanIfIndex_Type=Integer32
_AtiVlanIfIndex_Object=MibTableColumn
atiVlanIfIndex=_AtiVlanIfIndex_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1,1),_AtiVlanIfIndex_Type())
atiVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanIfIndex.setStatus(_A)
class _AtiVlanIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AtiVlanIfDescr_Type.__name__=_E
_AtiVlanIfDescr_Object=MibTableColumn
atiVlanIfDescr=_AtiVlanIfDescr_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1,2),_AtiVlanIfDescr_Type())
atiVlanIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanIfDescr.setStatus(_A)
_AtiVlanIfType_Type=AtiSwitchVlanType
_AtiVlanIfType_Object=MibTableColumn
atiVlanIfType=_AtiVlanIfType_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1,3),_AtiVlanIfType_Type())
atiVlanIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanIfType.setStatus(_A)
class _AtiVlanIfGlobalIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtiVlanIfGlobalIdentifier_Type.__name__=_D
_AtiVlanIfGlobalIdentifier_Object=MibTableColumn
atiVlanIfGlobalIdentifier=_AtiVlanIfGlobalIdentifier_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1,4),_AtiVlanIfGlobalIdentifier_Type())
atiVlanIfGlobalIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanIfGlobalIdentifier.setStatus(_A)
_AtiVlanIfStatus_Type=RowStatus
_AtiVlanIfStatus_Object=MibTableColumn
atiVlanIfStatus=_AtiVlanIfStatus_Object((1,3,6,1,4,1,207,8,12,2,4,1,2,1,6),_AtiVlanIfStatus_Type())
atiVlanIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanIfStatus.setStatus(_A)
_AtiVirtualGroup_ObjectIdentity=ObjectIdentity
atiVirtualGroup=_AtiVirtualGroup_ObjectIdentity((1,3,6,1,4,1,207,8,12,2,4,2))
_AtiNextAvailableVirtIfIndex_Type=Integer32
_AtiNextAvailableVirtIfIndex_Object=MibScalar
atiNextAvailableVirtIfIndex=_AtiNextAvailableVirtIfIndex_Object((1,3,6,1,4,1,207,8,12,2,4,2,1),_AtiNextAvailableVirtIfIndex_Type())
atiNextAvailableVirtIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:atiNextAvailableVirtIfIndex.setStatus(_A)
_AtiEncapsulationGroup_ObjectIdentity=ObjectIdentity
atiEncapsulationGroup=_AtiEncapsulationGroup_ObjectIdentity((1,3,6,1,4,1,207,8,12,2,4,3))
_AtiVlanEncapsIfTable_Object=MibTable
atiVlanEncapsIfTable=_AtiVlanEncapsIfTable_Object((1,3,6,1,4,1,207,8,12,2,4,3,1))
if mibBuilder.loadTexts:atiVlanEncapsIfTable.setStatus(_A)
_AtiVlanEncapsIfEntry_Object=MibTableRow
atiVlanEncapsIfEntry=_AtiVlanEncapsIfEntry_Object((1,3,6,1,4,1,207,8,12,2,4,3,1,1))
atiVlanEncapsIfEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:atiVlanEncapsIfEntry.setStatus(_A)
_AtiVlanEncapsIfIndex_Type=Integer32
_AtiVlanEncapsIfIndex_Object=MibTableColumn
atiVlanEncapsIfIndex=_AtiVlanEncapsIfIndex_Object((1,3,6,1,4,1,207,8,12,2,4,3,1,1,1),_AtiVlanEncapsIfIndex_Type())
atiVlanEncapsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanEncapsIfIndex.setStatus(_A)
_AtiVlanEncapsIfType_Type=AtiSwitchVlanEncapsType
_AtiVlanEncapsIfType_Object=MibTableColumn
atiVlanEncapsIfType=_AtiVlanEncapsIfType_Object((1,3,6,1,4,1,207,8,12,2,4,3,1,1,2),_AtiVlanEncapsIfType_Type())
atiVlanEncapsIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanEncapsIfType.setStatus(_A)
_AtiVlanEncapsIfTag_Type=Integer32
_AtiVlanEncapsIfTag_Object=MibTableColumn
atiVlanEncapsIfTag=_AtiVlanEncapsIfTag_Object((1,3,6,1,4,1,207,8,12,2,4,3,1,1,3),_AtiVlanEncapsIfTag_Type())
atiVlanEncapsIfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanEncapsIfTag.setStatus(_A)
_AtiVlanEncapsIfStatus_Type=RowStatus
_AtiVlanEncapsIfStatus_Object=MibTableColumn
atiVlanEncapsIfStatus=_AtiVlanEncapsIfStatus_Object((1,3,6,1,4,1,207,8,12,2,4,3,1,1,4),_AtiVlanEncapsIfStatus_Type())
atiVlanEncapsIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanEncapsIfStatus.setStatus(_A)
_AtiProtocolGroup_ObjectIdentity=ObjectIdentity
atiProtocolGroup=_AtiProtocolGroup_ObjectIdentity((1,3,6,1,4,1,207,8,12,2,4,5))
_AtiVlanProtocolTable_Object=MibTable
atiVlanProtocolTable=_AtiVlanProtocolTable_Object((1,3,6,1,4,1,207,8,12,2,4,5,1))
if mibBuilder.loadTexts:atiVlanProtocolTable.setStatus(_A)
_AtiVlanProtocolEntry_Object=MibTableRow
atiVlanProtocolEntry=_AtiVlanProtocolEntry_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1))
atiVlanProtocolEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:atiVlanProtocolEntry.setStatus(_A)
class _AtiVlanProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AtiVlanProtocolIndex_Type.__name__=_D
_AtiVlanProtocolIndex_Object=MibTableColumn
atiVlanProtocolIndex=_AtiVlanProtocolIndex_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,1),_AtiVlanProtocolIndex_Type())
atiVlanProtocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolIndex.setStatus(_A)
class _AtiVlanProtocolIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_AtiVlanProtocolIdIndex_Type.__name__=_D
_AtiVlanProtocolIdIndex_Object=MibTableColumn
atiVlanProtocolIdIndex=_AtiVlanProtocolIdIndex_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,2),_AtiVlanProtocolIdIndex_Type())
atiVlanProtocolIdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolIdIndex.setStatus(_A)
class _AtiVlanProtocolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AtiVlanProtocolName_Type.__name__=_E
_AtiVlanProtocolName_Object=MibTableColumn
atiVlanProtocolName=_AtiVlanProtocolName_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,3),_AtiVlanProtocolName_Type())
atiVlanProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolName.setStatus(_A)
class _AtiVlanProtocolDllEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('any',1),('ethertype',2),('llc',3),('llcSnapEthertype',4)))
_AtiVlanProtocolDllEncapsType_Type.__name__=_D
_AtiVlanProtocolDllEncapsType_Object=MibTableColumn
atiVlanProtocolDllEncapsType=_AtiVlanProtocolDllEncapsType_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,4),_AtiVlanProtocolDllEncapsType_Type())
atiVlanProtocolDllEncapsType.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolDllEncapsType.setStatus(_A)
class _AtiVlanProtocolId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtiVlanProtocolId_Type.__name__=_D
_AtiVlanProtocolId_Object=MibTableColumn
atiVlanProtocolId=_AtiVlanProtocolId_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,5),_AtiVlanProtocolId_Type())
atiVlanProtocolId.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolId.setStatus(_A)
_AtiVlanProtocolStatus_Type=RowStatus
_AtiVlanProtocolStatus_Object=MibTableColumn
atiVlanProtocolStatus=_AtiVlanProtocolStatus_Object((1,3,6,1,4,1,207,8,12,2,4,5,1,1,6),_AtiVlanProtocolStatus_Type())
atiVlanProtocolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolStatus.setStatus(_A)
_AtiVlanProtocolVlanTable_Object=MibTable
atiVlanProtocolVlanTable=_AtiVlanProtocolVlanTable_Object((1,3,6,1,4,1,207,8,12,2,4,5,2))
if mibBuilder.loadTexts:atiVlanProtocolVlanTable.setStatus(_A)
_AtiVlanProtocolVlanEntry_Object=MibTableRow
atiVlanProtocolVlanEntry=_AtiVlanProtocolVlanEntry_Object((1,3,6,1,4,1,207,8,12,2,4,5,2,1))
atiVlanProtocolVlanEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:atiVlanProtocolVlanEntry.setStatus(_A)
_AtiVlanProtocolVlanIfIndex_Type=Integer32
_AtiVlanProtocolVlanIfIndex_Object=MibTableColumn
atiVlanProtocolVlanIfIndex=_AtiVlanProtocolVlanIfIndex_Object((1,3,6,1,4,1,207,8,12,2,4,5,2,1,1),_AtiVlanProtocolVlanIfIndex_Type())
atiVlanProtocolVlanIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolVlanIfIndex.setStatus(_A)
_AtiVlanProtocolVlanProtocolIndex_Type=Integer32
_AtiVlanProtocolVlanProtocolIndex_Object=MibTableColumn
atiVlanProtocolVlanProtocolIndex=_AtiVlanProtocolVlanProtocolIndex_Object((1,3,6,1,4,1,207,8,12,2,4,5,2,1,2),_AtiVlanProtocolVlanProtocolIndex_Type())
atiVlanProtocolVlanProtocolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolVlanProtocolIndex.setStatus(_A)
_AtiVlanProtocolVlanStatus_Type=RowStatus
_AtiVlanProtocolVlanStatus_Object=MibTableColumn
atiVlanProtocolVlanStatus=_AtiVlanProtocolVlanStatus_Object((1,3,6,1,4,1,207,8,12,2,4,5,2,1,3),_AtiVlanProtocolVlanStatus_Type())
atiVlanProtocolVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiVlanProtocolVlanStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AtiSwitchVlanType':AtiSwitchVlanType,'AtiSwitchVlanEncapsType':AtiSwitchVlanEncapsType,'atiVlan':atiVlan,'atiVlanGroup':atiVlanGroup,'atiVlanIfTable':atiVlanIfTable,'atiVlanIfEntry':atiVlanIfEntry,_F:atiVlanIfIndex,'atiVlanIfDescr':atiVlanIfDescr,'atiVlanIfType':atiVlanIfType,'atiVlanIfGlobalIdentifier':atiVlanIfGlobalIdentifier,'atiVlanIfStatus':atiVlanIfStatus,'atiVirtualGroup':atiVirtualGroup,'atiNextAvailableVirtIfIndex':atiNextAvailableVirtIfIndex,'atiEncapsulationGroup':atiEncapsulationGroup,'atiVlanEncapsIfTable':atiVlanEncapsIfTable,'atiVlanEncapsIfEntry':atiVlanEncapsIfEntry,_G:atiVlanEncapsIfIndex,'atiVlanEncapsIfType':atiVlanEncapsIfType,'atiVlanEncapsIfTag':atiVlanEncapsIfTag,'atiVlanEncapsIfStatus':atiVlanEncapsIfStatus,'atiProtocolGroup':atiProtocolGroup,'atiVlanProtocolTable':atiVlanProtocolTable,'atiVlanProtocolEntry':atiVlanProtocolEntry,_H:atiVlanProtocolIndex,_I:atiVlanProtocolIdIndex,'atiVlanProtocolName':atiVlanProtocolName,'atiVlanProtocolDllEncapsType':atiVlanProtocolDllEncapsType,'atiVlanProtocolId':atiVlanProtocolId,'atiVlanProtocolStatus':atiVlanProtocolStatus,'atiVlanProtocolVlanTable':atiVlanProtocolVlanTable,'atiVlanProtocolVlanEntry':atiVlanProtocolVlanEntry,_J:atiVlanProtocolVlanIfIndex,_K:atiVlanProtocolVlanProtocolIndex,'atiVlanProtocolVlanStatus':atiVlanProtocolVlanStatus})