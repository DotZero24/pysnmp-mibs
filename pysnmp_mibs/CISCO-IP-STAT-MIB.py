_a='ciscoIpStatHCMIBGroup'
_Z='cipMacHCSwitchedBytes'
_Y='cipMacHCSwitchedPkts'
_X='cipPrecedenceHCSwitchedBytes'
_W='cipPrecedenceHCSwitchedPkts'
_V='cipMacFreeCount'
_U='cipMacSwitchedBytes'
_T='cipMacSwitchedPkts'
_S='cipPrecedenceSwitchedBytes'
_R='cipPrecedenceSwitchedPkts'
_Q='cipMacXEntry'
_P='cipPrecedenceXEntry'
_O='cipMacFreeDirection'
_N='cipMacAddress'
_M='cipMacDirection'
_L='cipPrecedenceIpPrecedence'
_K='cipPrecedenceDirection'
_J='Integer32'
_I='ciscoIpStatMIBGroup'
_H='bytes'
_G='packets'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='read-only'
_B='CISCO-IP-STAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoIpStatMIB=ModuleIdentity((1,3,6,1,4,1,9,9,84))
if mibBuilder.loadTexts:ciscoIpStatMIB.setRevisions(('2001-12-20 23:00','1997-07-18 00:00'))
class PacketSource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('input',1),('output',2)))
_CiscoIpStatMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpStatMIBObjects=_CiscoIpStatMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,84,1))
_CipPrecedence_ObjectIdentity=ObjectIdentity
cipPrecedence=_CipPrecedence_ObjectIdentity((1,3,6,1,4,1,9,9,84,1,1))
_CipPrecedenceTable_Object=MibTable
cipPrecedenceTable=_CipPrecedenceTable_Object((1,3,6,1,4,1,9,9,84,1,1,1))
if mibBuilder.loadTexts:cipPrecedenceTable.setStatus(_A)
_CipPrecedenceEntry_Object=MibTableRow
cipPrecedenceEntry=_CipPrecedenceEntry_Object((1,3,6,1,4,1,9,9,84,1,1,1,1))
cipPrecedenceEntry.setIndexNames((0,_E,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cipPrecedenceEntry.setStatus(_A)
_CipPrecedenceDirection_Type=PacketSource
_CipPrecedenceDirection_Object=MibTableColumn
cipPrecedenceDirection=_CipPrecedenceDirection_Object((1,3,6,1,4,1,9,9,84,1,1,1,1,1),_CipPrecedenceDirection_Type())
cipPrecedenceDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cipPrecedenceDirection.setStatus(_A)
class _CipPrecedenceIpPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CipPrecedenceIpPrecedence_Type.__name__=_J
_CipPrecedenceIpPrecedence_Object=MibTableColumn
cipPrecedenceIpPrecedence=_CipPrecedenceIpPrecedence_Object((1,3,6,1,4,1,9,9,84,1,1,1,1,2),_CipPrecedenceIpPrecedence_Type())
cipPrecedenceIpPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:cipPrecedenceIpPrecedence.setStatus(_A)
_CipPrecedenceSwitchedPkts_Type=Counter32
_CipPrecedenceSwitchedPkts_Object=MibTableColumn
cipPrecedenceSwitchedPkts=_CipPrecedenceSwitchedPkts_Object((1,3,6,1,4,1,9,9,84,1,1,1,1,3),_CipPrecedenceSwitchedPkts_Type())
cipPrecedenceSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipPrecedenceSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cipPrecedenceSwitchedPkts.setUnits(_G)
_CipPrecedenceSwitchedBytes_Type=Counter32
_CipPrecedenceSwitchedBytes_Object=MibTableColumn
cipPrecedenceSwitchedBytes=_CipPrecedenceSwitchedBytes_Object((1,3,6,1,4,1,9,9,84,1,1,1,1,4),_CipPrecedenceSwitchedBytes_Type())
cipPrecedenceSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipPrecedenceSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:cipPrecedenceSwitchedBytes.setUnits(_H)
_CipPrecedenceXTable_Object=MibTable
cipPrecedenceXTable=_CipPrecedenceXTable_Object((1,3,6,1,4,1,9,9,84,1,1,2))
if mibBuilder.loadTexts:cipPrecedenceXTable.setStatus(_A)
_CipPrecedenceXEntry_Object=MibTableRow
cipPrecedenceXEntry=_CipPrecedenceXEntry_Object((1,3,6,1,4,1,9,9,84,1,1,2,1))
if mibBuilder.loadTexts:cipPrecedenceXEntry.setStatus(_A)
_CipPrecedenceHCSwitchedPkts_Type=Counter64
_CipPrecedenceHCSwitchedPkts_Object=MibTableColumn
cipPrecedenceHCSwitchedPkts=_CipPrecedenceHCSwitchedPkts_Object((1,3,6,1,4,1,9,9,84,1,1,2,1,1),_CipPrecedenceHCSwitchedPkts_Type())
cipPrecedenceHCSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipPrecedenceHCSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cipPrecedenceHCSwitchedPkts.setUnits(_G)
_CipPrecedenceHCSwitchedBytes_Type=Counter64
_CipPrecedenceHCSwitchedBytes_Object=MibTableColumn
cipPrecedenceHCSwitchedBytes=_CipPrecedenceHCSwitchedBytes_Object((1,3,6,1,4,1,9,9,84,1,1,2,1,2),_CipPrecedenceHCSwitchedBytes_Type())
cipPrecedenceHCSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipPrecedenceHCSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:cipPrecedenceHCSwitchedBytes.setUnits(_H)
_CipMacIf_ObjectIdentity=ObjectIdentity
cipMacIf=_CipMacIf_ObjectIdentity((1,3,6,1,4,1,9,9,84,1,2))
_CipMacTable_Object=MibTable
cipMacTable=_CipMacTable_Object((1,3,6,1,4,1,9,9,84,1,2,1))
if mibBuilder.loadTexts:cipMacTable.setStatus(_A)
_CipMacEntry_Object=MibTableRow
cipMacEntry=_CipMacEntry_Object((1,3,6,1,4,1,9,9,84,1,2,1,1))
cipMacEntry.setIndexNames((0,_E,_F),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:cipMacEntry.setStatus(_A)
_CipMacDirection_Type=PacketSource
_CipMacDirection_Object=MibTableColumn
cipMacDirection=_CipMacDirection_Object((1,3,6,1,4,1,9,9,84,1,2,1,1,1),_CipMacDirection_Type())
cipMacDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cipMacDirection.setStatus(_A)
_CipMacAddress_Type=MacAddress
_CipMacAddress_Object=MibTableColumn
cipMacAddress=_CipMacAddress_Object((1,3,6,1,4,1,9,9,84,1,2,1,1,2),_CipMacAddress_Type())
cipMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cipMacAddress.setStatus(_A)
_CipMacSwitchedPkts_Type=Counter32
_CipMacSwitchedPkts_Object=MibTableColumn
cipMacSwitchedPkts=_CipMacSwitchedPkts_Object((1,3,6,1,4,1,9,9,84,1,2,1,1,3),_CipMacSwitchedPkts_Type())
cipMacSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipMacSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cipMacSwitchedPkts.setUnits(_G)
_CipMacSwitchedBytes_Type=Counter32
_CipMacSwitchedBytes_Object=MibTableColumn
cipMacSwitchedBytes=_CipMacSwitchedBytes_Object((1,3,6,1,4,1,9,9,84,1,2,1,1,4),_CipMacSwitchedBytes_Type())
cipMacSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipMacSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:cipMacSwitchedBytes.setUnits(_H)
_CipMacFreeTable_Object=MibTable
cipMacFreeTable=_CipMacFreeTable_Object((1,3,6,1,4,1,9,9,84,1,2,2))
if mibBuilder.loadTexts:cipMacFreeTable.setStatus(_A)
_CipMacFreeEntry_Object=MibTableRow
cipMacFreeEntry=_CipMacFreeEntry_Object((1,3,6,1,4,1,9,9,84,1,2,2,1))
cipMacFreeEntry.setIndexNames((0,_E,_F),(0,_B,_O))
if mibBuilder.loadTexts:cipMacFreeEntry.setStatus(_A)
_CipMacFreeDirection_Type=PacketSource
_CipMacFreeDirection_Object=MibTableColumn
cipMacFreeDirection=_CipMacFreeDirection_Object((1,3,6,1,4,1,9,9,84,1,2,2,1,1),_CipMacFreeDirection_Type())
cipMacFreeDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cipMacFreeDirection.setStatus(_A)
_CipMacFreeCount_Type=Gauge32
_CipMacFreeCount_Object=MibTableColumn
cipMacFreeCount=_CipMacFreeCount_Object((1,3,6,1,4,1,9,9,84,1,2,2,1,2),_CipMacFreeCount_Type())
cipMacFreeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cipMacFreeCount.setStatus(_A)
_CipMacXTable_Object=MibTable
cipMacXTable=_CipMacXTable_Object((1,3,6,1,4,1,9,9,84,1,2,3))
if mibBuilder.loadTexts:cipMacXTable.setStatus(_A)
_CipMacXEntry_Object=MibTableRow
cipMacXEntry=_CipMacXEntry_Object((1,3,6,1,4,1,9,9,84,1,2,3,1))
if mibBuilder.loadTexts:cipMacXEntry.setStatus(_A)
_CipMacHCSwitchedPkts_Type=Counter64
_CipMacHCSwitchedPkts_Object=MibTableColumn
cipMacHCSwitchedPkts=_CipMacHCSwitchedPkts_Object((1,3,6,1,4,1,9,9,84,1,2,3,1,1),_CipMacHCSwitchedPkts_Type())
cipMacHCSwitchedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipMacHCSwitchedPkts.setStatus(_A)
if mibBuilder.loadTexts:cipMacHCSwitchedPkts.setUnits(_G)
_CipMacHCSwitchedBytes_Type=Counter64
_CipMacHCSwitchedBytes_Object=MibTableColumn
cipMacHCSwitchedBytes=_CipMacHCSwitchedBytes_Object((1,3,6,1,4,1,9,9,84,1,2,3,1,2),_CipMacHCSwitchedBytes_Type())
cipMacHCSwitchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cipMacHCSwitchedBytes.setStatus(_A)
if mibBuilder.loadTexts:cipMacHCSwitchedBytes.setUnits(_H)
_CiscoIpStatMIBConformance_ObjectIdentity=ObjectIdentity
ciscoIpStatMIBConformance=_CiscoIpStatMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,84,3))
_CiscoIpStatMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpStatMIBCompliances=_CiscoIpStatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,84,3,1))
_CiscoIpStatMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpStatMIBGroups=_CiscoIpStatMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,84,3,2))
cipPrecedenceEntry.registerAugmentions((_B,_P))
cipPrecedenceXEntry.setIndexNames(*cipPrecedenceEntry.getIndexNames())
cipMacEntry.registerAugmentions((_B,_Q))
cipMacXEntry.setIndexNames(*cipMacEntry.getIndexNames())
ciscoIpStatMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,84,3,2,1))
ciscoIpStatMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ciscoIpStatMIBGroup.setStatus(_A)
ciscoIpStatHCMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,84,3,2,2))
ciscoIpStatHCMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:ciscoIpStatHCMIBGroup.setStatus(_A)
ciscoIpStatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,84,3,1,1))
ciscoIpStatMIBCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:ciscoIpStatMIBCompliance.setStatus('deprecated')
ciscoIpStatMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,84,3,1,2))
ciscoIpStatMIBComplianceRev2.setObjects(*((_B,_I),(_B,_a)))
if mibBuilder.loadTexts:ciscoIpStatMIBComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PacketSource':PacketSource,'ciscoIpStatMIB':ciscoIpStatMIB,'ciscoIpStatMIBObjects':ciscoIpStatMIBObjects,'cipPrecedence':cipPrecedence,'cipPrecedenceTable':cipPrecedenceTable,'cipPrecedenceEntry':cipPrecedenceEntry,_K:cipPrecedenceDirection,_L:cipPrecedenceIpPrecedence,_R:cipPrecedenceSwitchedPkts,_S:cipPrecedenceSwitchedBytes,'cipPrecedenceXTable':cipPrecedenceXTable,_P:cipPrecedenceXEntry,_W:cipPrecedenceHCSwitchedPkts,_X:cipPrecedenceHCSwitchedBytes,'cipMacIf':cipMacIf,'cipMacTable':cipMacTable,'cipMacEntry':cipMacEntry,_M:cipMacDirection,_N:cipMacAddress,_T:cipMacSwitchedPkts,_U:cipMacSwitchedBytes,'cipMacFreeTable':cipMacFreeTable,'cipMacFreeEntry':cipMacFreeEntry,_O:cipMacFreeDirection,_V:cipMacFreeCount,'cipMacXTable':cipMacXTable,_Q:cipMacXEntry,_Y:cipMacHCSwitchedPkts,_Z:cipMacHCSwitchedBytes,'ciscoIpStatMIBConformance':ciscoIpStatMIBConformance,'ciscoIpStatMIBCompliances':ciscoIpStatMIBCompliances,'ciscoIpStatMIBCompliance':ciscoIpStatMIBCompliance,'ciscoIpStatMIBComplianceRev2':ciscoIpStatMIBComplianceRev2,'ciscoIpStatMIBGroups':ciscoIpStatMIBGroups,_I:ciscoIpStatMIBGroup,_a:ciscoIpStatHCMIBGroup})