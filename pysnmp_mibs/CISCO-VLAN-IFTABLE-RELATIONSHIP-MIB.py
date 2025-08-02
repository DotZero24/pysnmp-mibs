_G='cviMIBGroup'
_F='cviRoutedVlanIfIndex'
_E='not-accessible'
_D='cviPhysicalIfIndex'
_C='cviVlanId'
_B='CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','InterfaceIndexOrZero')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVlanIfTableRelationshipMIB=ModuleIdentity((1,3,6,1,4,1,9,9,128))
if mibBuilder.loadTexts:ciscoVlanIfTableRelationshipMIB.setRevisions(('2013-07-15 00:00',))
_CviMIBObjects_ObjectIdentity=ObjectIdentity
cviMIBObjects=_CviMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,128,1))
_CviGlobals_ObjectIdentity=ObjectIdentity
cviGlobals=_CviGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,128,1,1))
_CviVlanInterfaceIndexTable_Object=MibTable
cviVlanInterfaceIndexTable=_CviVlanInterfaceIndexTable_Object((1,3,6,1,4,1,9,9,128,1,1,1))
if mibBuilder.loadTexts:cviVlanInterfaceIndexTable.setStatus(_A)
_CviVlanInterfaceIndexEntry_Object=MibTableRow
cviVlanInterfaceIndexEntry=_CviVlanInterfaceIndexEntry_Object((1,3,6,1,4,1,9,9,128,1,1,1,1))
cviVlanInterfaceIndexEntry.setIndexNames((0,_B,_C),(0,_B,_D))
if mibBuilder.loadTexts:cviVlanInterfaceIndexEntry.setStatus(_A)
_CviVlanId_Type=VlanIndex
_CviVlanId_Object=MibTableColumn
cviVlanId=_CviVlanId_Object((1,3,6,1,4,1,9,9,128,1,1,1,1,1),_CviVlanId_Type())
cviVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:cviVlanId.setStatus(_A)
_CviPhysicalIfIndex_Type=InterfaceIndexOrZero
_CviPhysicalIfIndex_Object=MibTableColumn
cviPhysicalIfIndex=_CviPhysicalIfIndex_Object((1,3,6,1,4,1,9,9,128,1,1,1,1,2),_CviPhysicalIfIndex_Type())
cviPhysicalIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cviPhysicalIfIndex.setStatus(_A)
_CviRoutedVlanIfIndex_Type=InterfaceIndex
_CviRoutedVlanIfIndex_Object=MibTableColumn
cviRoutedVlanIfIndex=_CviRoutedVlanIfIndex_Object((1,3,6,1,4,1,9,9,128,1,1,1,1,3),_CviRoutedVlanIfIndex_Type())
cviRoutedVlanIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:cviRoutedVlanIfIndex.setStatus(_A)
_CviMIBConformance_ObjectIdentity=ObjectIdentity
cviMIBConformance=_CviMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,128,1,3))
_CviMIBCompliances_ObjectIdentity=ObjectIdentity
cviMIBCompliances=_CviMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,128,1,3,1))
_CviMIBGroups_ObjectIdentity=ObjectIdentity
cviMIBGroups=_CviMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,128,1,3,2))
cviMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,128,1,3,2,1))
cviMIBGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:cviMIBGroup.setStatus(_A)
cviMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,128,1,3,1,1))
cviMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:cviMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVlanIfTableRelationshipMIB':ciscoVlanIfTableRelationshipMIB,'cviMIBObjects':cviMIBObjects,'cviGlobals':cviGlobals,'cviVlanInterfaceIndexTable':cviVlanInterfaceIndexTable,'cviVlanInterfaceIndexEntry':cviVlanInterfaceIndexEntry,_C:cviVlanId,_D:cviPhysicalIfIndex,_F:cviRoutedVlanIfIndex,'cviMIBConformance':cviMIBConformance,'cviMIBCompliances':cviMIBCompliances,'cviMIBCompliance':cviMIBCompliance,'cviMIBGroups':cviMIBGroups,_G:cviMIBGroup})