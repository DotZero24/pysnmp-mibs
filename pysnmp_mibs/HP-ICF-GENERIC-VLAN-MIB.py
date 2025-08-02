_K='hpicfGenericVlanFeaturesConfGrp1'
_J='hpicfGenericVlanFeaturesConfigGroup'
_I='hpicfDot1qTpFdbInstalledTime'
_H='deprecated'
_G='hpicfGenericVlanFeaturesEntry'
_F='read-only'
_E='Integer32'
_D='hpicfDot1qTpFdbVlanId'
_C='hpicfMacNotifyClearVlanControl'
_B='current'
_A='HP-ICF-GENERIC-VLAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VlanId,dot1qTpFdbEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','dot1qTpFdbEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfGenericVlanMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,67))
if mibBuilder.loadTexts:hpicfGenericVlanMIB.setRevisions(('2017-06-28 00:00','2010-02-08 00:00'))
_HpicfGenericVlanFeaturesObjects_ObjectIdentity=ObjectIdentity
hpicfGenericVlanFeaturesObjects=_HpicfGenericVlanFeaturesObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,67,1))
_HpicfGenericVlanFeaturesTable_Object=MibTable
hpicfGenericVlanFeaturesTable=_HpicfGenericVlanFeaturesTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,67,1,1))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesTable.setStatus(_B)
_HpicfGenericVlanFeaturesEntry_Object=MibTableRow
hpicfGenericVlanFeaturesEntry=_HpicfGenericVlanFeaturesEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,67,1,1,1))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesEntry.setStatus(_B)
class _HpicfMacNotifyClearVlanControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOperation',1),('macNotifyClearVlan',2)))
_HpicfMacNotifyClearVlanControl_Type.__name__=_E
_HpicfMacNotifyClearVlanControl_Object=MibTableColumn
hpicfMacNotifyClearVlanControl=_HpicfMacNotifyClearVlanControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,67,1,1,1,1),_HpicfMacNotifyClearVlanControl_Type())
hpicfMacNotifyClearVlanControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfMacNotifyClearVlanControl.setStatus(_B)
_HpicfDot1qTpFdbVlanId_Type=VlanId
_HpicfDot1qTpFdbVlanId_Object=MibTableColumn
hpicfDot1qTpFdbVlanId=_HpicfDot1qTpFdbVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,67,1,1,1,2),_HpicfDot1qTpFdbVlanId_Type())
hpicfDot1qTpFdbVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDot1qTpFdbVlanId.setStatus(_B)
_HpicfDot1qTpFdbInstalledTime_Type=TimeTicks
_HpicfDot1qTpFdbInstalledTime_Object=MibTableColumn
hpicfDot1qTpFdbInstalledTime=_HpicfDot1qTpFdbInstalledTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,67,1,1,1,3),_HpicfDot1qTpFdbInstalledTime_Type())
hpicfDot1qTpFdbInstalledTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDot1qTpFdbInstalledTime.setStatus(_B)
_HpicfGenericVlanFeaturesConformance_ObjectIdentity=ObjectIdentity
hpicfGenericVlanFeaturesConformance=_HpicfGenericVlanFeaturesConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,67,2))
_HpicfGenericVlanFeaturesCompliances_ObjectIdentity=ObjectIdentity
hpicfGenericVlanFeaturesCompliances=_HpicfGenericVlanFeaturesCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,67,2,1))
_HpicfGenericVlanFeaturesGroups_ObjectIdentity=ObjectIdentity
hpicfGenericVlanFeaturesGroups=_HpicfGenericVlanFeaturesGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,67,2,2))
dot1qTpFdbEntry.registerAugmentions((_A,_G))
hpicfGenericVlanFeaturesEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
hpicfGenericVlanFeaturesConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,67,2,2,2))
hpicfGenericVlanFeaturesConfigGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesConfigGroup.setStatus(_H)
hpicfGenericVlanFeaturesConfGrp1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,67,2,2,3))
hpicfGenericVlanFeaturesConfGrp1.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesConfGrp1.setStatus(_B)
hpicfGenericVlanFeaturesCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,67,2,1,1))
hpicfGenericVlanFeaturesCompliance.setObjects((_A,_J))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesCompliance.setStatus(_H)
hpicfGenericVlanFeaturesComp1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,67,2,1,2))
hpicfGenericVlanFeaturesComp1.setObjects((_A,_K))
if mibBuilder.loadTexts:hpicfGenericVlanFeaturesComp1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfGenericVlanMIB':hpicfGenericVlanMIB,'hpicfGenericVlanFeaturesObjects':hpicfGenericVlanFeaturesObjects,'hpicfGenericVlanFeaturesTable':hpicfGenericVlanFeaturesTable,_G:hpicfGenericVlanFeaturesEntry,_C:hpicfMacNotifyClearVlanControl,_D:hpicfDot1qTpFdbVlanId,_I:hpicfDot1qTpFdbInstalledTime,'hpicfGenericVlanFeaturesConformance':hpicfGenericVlanFeaturesConformance,'hpicfGenericVlanFeaturesCompliances':hpicfGenericVlanFeaturesCompliances,'hpicfGenericVlanFeaturesCompliance':hpicfGenericVlanFeaturesCompliance,'hpicfGenericVlanFeaturesComp1':hpicfGenericVlanFeaturesComp1,'hpicfGenericVlanFeaturesGroups':hpicfGenericVlanFeaturesGroups,_J:hpicfGenericVlanFeaturesConfigGroup,_K:hpicfGenericVlanFeaturesConfGrp1})