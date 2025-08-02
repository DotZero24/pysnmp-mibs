_R='ciscoIfTopNExtCtrlVlanGroup'
_Q='ciscoIfTopNExtControlGroup'
_P='ciscoIfTopNExtCapsGroup'
_O='citneInterfaceTopNVlanNumber'
_N='citneInterfaceTopNInterfaceType'
_M='citneInterfaceTopNCounterType'
_L='citneInterfaceTopNCaps'
_K='citneInterfaceTopNControlEntry'
_J='overflow'
_I='multicast'
_H='broadcast'
_G='packets'
_F='utilization'
_E='VlanIndex'
_D='read-create'
_C='Integer32'
_B='CISCO-INTERFACETOPN-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
interfaceTopNControlEntry,=mibBuilder.importSymbols('INTERFACETOPN-MIB','interfaceTopNControlEntry')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoInterfaceTopNExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,482))
if mibBuilder.loadTexts:ciscoInterfaceTopNExtMIB.setRevisions(('2010-10-19 00:00','2008-01-15 00:00','2006-03-15 00:00'))
_CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoInterfaceTopNExtMIBNotifs=_CiscoInterfaceTopNExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,482,0))
_CiscoInterfaceTopNExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoInterfaceTopNExtMIBObjects=_CiscoInterfaceTopNExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,482,1))
class _CitneInterfaceTopNCaps_Type(Bits):namedValues=NamedValues(*((_F,0),('bytes',1),(_G,2),(_H,3),(_I,4),(_J,5)))
_CitneInterfaceTopNCaps_Type.__name__='Bits'
_CitneInterfaceTopNCaps_Object=MibScalar
citneInterfaceTopNCaps=_CitneInterfaceTopNCaps_Object((1,3,6,1,4,1,9,9,482,1,1),_CitneInterfaceTopNCaps_Type())
citneInterfaceTopNCaps.setMaxAccess('read-only')
if mibBuilder.loadTexts:citneInterfaceTopNCaps.setStatus(_A)
_CitneInterfaceTopNControlTable_Object=MibTable
citneInterfaceTopNControlTable=_CitneInterfaceTopNControlTable_Object((1,3,6,1,4,1,9,9,482,1,2))
if mibBuilder.loadTexts:citneInterfaceTopNControlTable.setStatus(_A)
_CitneInterfaceTopNControlEntry_Object=MibTableRow
citneInterfaceTopNControlEntry=_CitneInterfaceTopNControlEntry_Object((1,3,6,1,4,1,9,9,482,1,2,1))
if mibBuilder.loadTexts:citneInterfaceTopNControlEntry.setStatus(_A)
class _CitneInterfaceTopNCounterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),(_F,2),('bytes',3),(_G,4),(_H,5),(_I,6),(_J,7)))
_CitneInterfaceTopNCounterType_Type.__name__=_C
_CitneInterfaceTopNCounterType_Object=MibTableColumn
citneInterfaceTopNCounterType=_CitneInterfaceTopNCounterType_Object((1,3,6,1,4,1,9,9,482,1,2,1,1),_CitneInterfaceTopNCounterType_Type())
citneInterfaceTopNCounterType.setMaxAccess(_D)
if mibBuilder.loadTexts:citneInterfaceTopNCounterType.setStatus(_A)
class _CitneInterfaceTopNInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('all',1),('ethernet',2),('fastEthernet',3),('gigaEthernet',4),('tenGigaEthernet',5),('portChannel',6),('layer2',7),('layer3',8),('fortyGigaEthernet',9)))
_CitneInterfaceTopNInterfaceType_Type.__name__=_C
_CitneInterfaceTopNInterfaceType_Object=MibTableColumn
citneInterfaceTopNInterfaceType=_CitneInterfaceTopNInterfaceType_Object((1,3,6,1,4,1,9,9,482,1,2,1,2),_CitneInterfaceTopNInterfaceType_Type())
citneInterfaceTopNInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:citneInterfaceTopNInterfaceType.setStatus(_A)
class _CitneInterfaceTopNVlanNumber_Type(VlanIndex):defaultValue=0
_CitneInterfaceTopNVlanNumber_Type.__name__=_E
_CitneInterfaceTopNVlanNumber_Object=MibTableColumn
citneInterfaceTopNVlanNumber=_CitneInterfaceTopNVlanNumber_Object((1,3,6,1,4,1,9,9,482,1,2,1,3),_CitneInterfaceTopNVlanNumber_Type())
citneInterfaceTopNVlanNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:citneInterfaceTopNVlanNumber.setStatus(_A)
_CiscoInterfaceTopNExtMIBConform_ObjectIdentity=ObjectIdentity
ciscoInterfaceTopNExtMIBConform=_CiscoInterfaceTopNExtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,482,2))
_CiscoIfTopNExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIfTopNExtMIBCompliances=_CiscoIfTopNExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,482,2,1))
_CiscoIfTopNExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIfTopNExtMIBGroups=_CiscoIfTopNExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,482,2,2))
interfaceTopNControlEntry.registerAugmentions((_B,_K))
citneInterfaceTopNControlEntry.setIndexNames(*interfaceTopNControlEntry.getIndexNames())
ciscoIfTopNExtCapsGroup=ObjectGroup((1,3,6,1,4,1,9,9,482,2,2,1))
ciscoIfTopNExtCapsGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoIfTopNExtCapsGroup.setStatus(_A)
ciscoIfTopNExtControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,482,2,2,2))
ciscoIfTopNExtControlGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ciscoIfTopNExtControlGroup.setStatus(_A)
ciscoIfTopNExtCtrlVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,482,2,2,3))
ciscoIfTopNExtCtrlVlanGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ciscoIfTopNExtCtrlVlanGroup.setStatus(_A)
ciscoIfTopNExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,482,2,1,1))
ciscoIfTopNExtMIBCompliance.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ciscoIfTopNExtMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoInterfaceTopNExtMIB':ciscoInterfaceTopNExtMIB,'ciscoInterfaceTopNExtMIBNotifs':ciscoInterfaceTopNExtMIBNotifs,'ciscoInterfaceTopNExtMIBObjects':ciscoInterfaceTopNExtMIBObjects,_L:citneInterfaceTopNCaps,'citneInterfaceTopNControlTable':citneInterfaceTopNControlTable,_K:citneInterfaceTopNControlEntry,_M:citneInterfaceTopNCounterType,_N:citneInterfaceTopNInterfaceType,_O:citneInterfaceTopNVlanNumber,'ciscoInterfaceTopNExtMIBConform':ciscoInterfaceTopNExtMIBConform,'ciscoIfTopNExtMIBCompliances':ciscoIfTopNExtMIBCompliances,'ciscoIfTopNExtMIBCompliance':ciscoIfTopNExtMIBCompliance,'ciscoIfTopNExtMIBGroups':ciscoIfTopNExtMIBGroups,_P:ciscoIfTopNExtCapsGroup,_Q:ciscoIfTopNExtControlGroup,_R:ciscoIfTopNExtCtrlVlanGroup})