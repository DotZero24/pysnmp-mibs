_M='hpicfPrivateVlanMappingRowStatus'
_L='hpicfPrivateVlanCommunity'
_K='hpicfPrivateVlanIsolated'
_J='hpicfPrivateVlanType'
_I='hpicfPrivateVlanEntry'
_H='hpicfPrivateVlanPrimary'
_G='PrivateVlanType'
_F='Integer32'
_E='hpicfPVlanMappingTableGroup'
_D='hpicfPrivateVlanTableGroup'
_C='read-create'
_B='HP-ICF-PRIVATEVLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
VlanId,dot1qVlanStaticEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','dot1qVlanStaticEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpicfPrivateVlan=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114))
if mibBuilder.loadTexts:hpicfPrivateVlan.setRevisions(('2015-04-22 00:00',))
class PrivateVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notAPrivateVLAN',1),('primary',2),('isolated',3),('community',4)))
_HpicfPrivateVlanObjects_ObjectIdentity=ObjectIdentity
hpicfPrivateVlanObjects=_HpicfPrivateVlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114,1))
_HpicfPrivateVlanConfig_ObjectIdentity=ObjectIdentity
hpicfPrivateVlanConfig=_HpicfPrivateVlanConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1))
_HpicfPrivateVlanTable_Object=MibTable
hpicfPrivateVlanTable=_HpicfPrivateVlanTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,1))
if mibBuilder.loadTexts:hpicfPrivateVlanTable.setStatus(_A)
_HpicfPrivateVlanEntry_Object=MibTableRow
hpicfPrivateVlanEntry=_HpicfPrivateVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,1,1))
if mibBuilder.loadTexts:hpicfPrivateVlanEntry.setStatus(_A)
class _HpicfPrivateVlanType_Type(PrivateVlanType):defaultValue=1
_HpicfPrivateVlanType_Type.__name__=_G
_HpicfPrivateVlanType_Object=MibTableColumn
hpicfPrivateVlanType=_HpicfPrivateVlanType_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,1,1,1),_HpicfPrivateVlanType_Type())
hpicfPrivateVlanType.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpicfPrivateVlanType.setStatus(_A)
_HpicfPrivateVlanMappingTable_Object=MibTable
hpicfPrivateVlanMappingTable=_HpicfPrivateVlanMappingTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2))
if mibBuilder.loadTexts:hpicfPrivateVlanMappingTable.setStatus(_A)
_HpicfPrivateVlanMappingEntry_Object=MibTableRow
hpicfPrivateVlanMappingEntry=_HpicfPrivateVlanMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2,1))
hpicfPrivateVlanMappingEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpicfPrivateVlanMappingEntry.setStatus(_A)
_HpicfPrivateVlanPrimary_Type=VlanId
_HpicfPrivateVlanPrimary_Object=MibTableColumn
hpicfPrivateVlanPrimary=_HpicfPrivateVlanPrimary_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2,1,1),_HpicfPrivateVlanPrimary_Type())
hpicfPrivateVlanPrimary.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfPrivateVlanPrimary.setStatus(_A)
class _HpicfPrivateVlanIsolated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpicfPrivateVlanIsolated_Type.__name__=_F
_HpicfPrivateVlanIsolated_Object=MibTableColumn
hpicfPrivateVlanIsolated=_HpicfPrivateVlanIsolated_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2,1,2),_HpicfPrivateVlanIsolated_Type())
hpicfPrivateVlanIsolated.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPrivateVlanIsolated.setStatus(_A)
_HpicfPrivateVlanCommunity_Type=VidList
_HpicfPrivateVlanCommunity_Object=MibTableColumn
hpicfPrivateVlanCommunity=_HpicfPrivateVlanCommunity_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2,1,3),_HpicfPrivateVlanCommunity_Type())
hpicfPrivateVlanCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPrivateVlanCommunity.setStatus(_A)
_HpicfPrivateVlanMappingRowStatus_Type=RowStatus
_HpicfPrivateVlanMappingRowStatus_Object=MibTableColumn
hpicfPrivateVlanMappingRowStatus=_HpicfPrivateVlanMappingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,114,1,1,2,1,4),_HpicfPrivateVlanMappingRowStatus_Type())
hpicfPrivateVlanMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfPrivateVlanMappingRowStatus.setStatus(_A)
_HpicfPrivateVlanConformance_ObjectIdentity=ObjectIdentity
hpicfPrivateVlanConformance=_HpicfPrivateVlanConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114,2))
_HpicfPrivateVlanCompliances_ObjectIdentity=ObjectIdentity
hpicfPrivateVlanCompliances=_HpicfPrivateVlanCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114,2,1))
_HpicfPrivateVlanGroup_ObjectIdentity=ObjectIdentity
hpicfPrivateVlanGroup=_HpicfPrivateVlanGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,114,2,2))
dot1qVlanStaticEntry.registerAugmentions((_B,_I))
hpicfPrivateVlanEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())
hpicfPrivateVlanTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,114,2,2,1))
hpicfPrivateVlanTableGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:hpicfPrivateVlanTableGroup.setStatus(_A)
hpicfPVlanMappingTableGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,114,2,2,2))
hpicfPVlanMappingTableGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpicfPVlanMappingTableGroup.setStatus(_A)
hpicfPVlanTableCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,114,2,1,1))
hpicfPVlanTableCompliance.setObjects(*((_B,_D),(_B,_D)))
if mibBuilder.loadTexts:hpicfPVlanTableCompliance.setStatus(_A)
hpicfPVlanMappingTblCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,114,2,1,2))
hpicfPVlanMappingTblCompliance.setObjects(*((_B,_E),(_B,_E)))
if mibBuilder.loadTexts:hpicfPVlanMappingTblCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:PrivateVlanType,'hpicfPrivateVlan':hpicfPrivateVlan,'hpicfPrivateVlanObjects':hpicfPrivateVlanObjects,'hpicfPrivateVlanConfig':hpicfPrivateVlanConfig,'hpicfPrivateVlanTable':hpicfPrivateVlanTable,_I:hpicfPrivateVlanEntry,_J:hpicfPrivateVlanType,'hpicfPrivateVlanMappingTable':hpicfPrivateVlanMappingTable,'hpicfPrivateVlanMappingEntry':hpicfPrivateVlanMappingEntry,_H:hpicfPrivateVlanPrimary,_K:hpicfPrivateVlanIsolated,_L:hpicfPrivateVlanCommunity,_M:hpicfPrivateVlanMappingRowStatus,'hpicfPrivateVlanConformance':hpicfPrivateVlanConformance,'hpicfPrivateVlanCompliances':hpicfPrivateVlanCompliances,'hpicfPVlanTableCompliance':hpicfPVlanTableCompliance,'hpicfPVlanMappingTblCompliance':hpicfPVlanMappingTblCompliance,'hpicfPrivateVlanGroup':hpicfPrivateVlanGroup,_D:hpicfPrivateVlanTableGroup,_E:hpicfPVlanMappingTableGroup})