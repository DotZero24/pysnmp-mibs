_G='hpicfLayer3VlanStatus'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='hpicfLayer3VlanConfigGroup'
_B='HP-ICF-LAYER3VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfLayer3VlanConfigMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,70))
if mibBuilder.loadTexts:hpicfLayer3VlanConfigMIB.setRevisions(('2010-03-23 00:00',))
_HpicfLayer3VlanConfig_ObjectIdentity=ObjectIdentity
hpicfLayer3VlanConfig=_HpicfLayer3VlanConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,70,1))
_HpicfLayer3VlanConfigTable_Object=MibTable
hpicfLayer3VlanConfigTable=_HpicfLayer3VlanConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,70,1,1))
if mibBuilder.loadTexts:hpicfLayer3VlanConfigTable.setStatus(_A)
_HpicfLayer3VlanConfigEntry_Object=MibTableRow
hpicfLayer3VlanConfigEntry=_HpicfLayer3VlanConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,70,1,1,1))
hpicfLayer3VlanConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpicfLayer3VlanConfigEntry.setStatus(_A)
class _HpicfLayer3VlanStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfLayer3VlanStatus_Type.__name__=_F
_HpicfLayer3VlanStatus_Object=MibTableColumn
hpicfLayer3VlanStatus=_HpicfLayer3VlanStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,70,1,1,1,1),_HpicfLayer3VlanStatus_Type())
hpicfLayer3VlanStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfLayer3VlanStatus.setStatus(_A)
_HpicfLayer3VlanConfigConformance_ObjectIdentity=ObjectIdentity
hpicfLayer3VlanConfigConformance=_HpicfLayer3VlanConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,70,2))
_HpicfL3VlanConfigMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfL3VlanConfigMIBCompliances=_HpicfL3VlanConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,70,2,1))
_HpicfLayer3VlanConfigMIBGroups_ObjectIdentity=ObjectIdentity
hpicfLayer3VlanConfigMIBGroups=_HpicfLayer3VlanConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,70,2,2))
hpicfLayer3VlanConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,70,2,2,1))
hpicfLayer3VlanConfigGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:hpicfLayer3VlanConfigGroup.setStatus(_A)
hpicfL3VlanConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,70,2,1,1))
hpicfL3VlanConfigMIBCompliance.setObjects(*((_B,_C),(_B,_C)))
if mibBuilder.loadTexts:hpicfL3VlanConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfLayer3VlanConfigMIB':hpicfLayer3VlanConfigMIB,'hpicfLayer3VlanConfig':hpicfLayer3VlanConfig,'hpicfLayer3VlanConfigTable':hpicfLayer3VlanConfigTable,'hpicfLayer3VlanConfigEntry':hpicfLayer3VlanConfigEntry,_G:hpicfLayer3VlanStatus,'hpicfLayer3VlanConfigConformance':hpicfLayer3VlanConfigConformance,'hpicfL3VlanConfigMIBCompliances':hpicfL3VlanConfigMIBCompliances,'hpicfL3VlanConfigMIBCompliance':hpicfL3VlanConfigMIBCompliance,'hpicfLayer3VlanConfigMIBGroups':hpicfLayer3VlanConfigMIBGroups,_C:hpicfLayer3VlanConfigGroup})