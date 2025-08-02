_O='juniBridgeGroup'
_N='juniBridgeDupMacCounter'
_M='juniBridgeAge'
_L='juniBridgeIfMaxLearnCount'
_K='juniBridgeSPolicyIndex'
_J='juniBridgeIfLowerIfIndex'
_I='juniBridgeIfRowStatus'
_H='juniBridgeIfNextIfIndex'
_G='juniBridgeMacAddress'
_F='not-accessible'
_E='juniBridgeIfIndex'
_D='read-only'
_C='read-create'
_B='Juniper-BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
juniBridgeMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,63))
if mibBuilder.loadTexts:juniBridgeMIB.setRevisions(('2003-11-04 20:39','2002-09-16 21:44'))
_JuniBridgeIfLayer_ObjectIdentity=ObjectIdentity
juniBridgeIfLayer=_JuniBridgeIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,1))
_JuniBridgeIfNextIfIndex_Type=JuniNextIfIndex
_JuniBridgeIfNextIfIndex_Object=MibScalar
juniBridgeIfNextIfIndex=_JuniBridgeIfNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,63,1,1),_JuniBridgeIfNextIfIndex_Type())
juniBridgeIfNextIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgeIfNextIfIndex.setStatus(_A)
_JuniBridgeIfTable_Object=MibTable
juniBridgeIfTable=_JuniBridgeIfTable_Object((1,3,6,1,4,1,4874,2,2,63,1,2))
if mibBuilder.loadTexts:juniBridgeIfTable.setStatus(_A)
_JuniBridgeIfEntry_Object=MibTableRow
juniBridgeIfEntry=_JuniBridgeIfEntry_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1))
juniBridgeIfEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:juniBridgeIfEntry.setStatus(_A)
_JuniBridgeIfIndex_Type=InterfaceIndex
_JuniBridgeIfIndex_Object=MibTableColumn
juniBridgeIfIndex=_JuniBridgeIfIndex_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1,1),_JuniBridgeIfIndex_Type())
juniBridgeIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniBridgeIfIndex.setStatus(_A)
_JuniBridgeIfRowStatus_Type=RowStatus
_JuniBridgeIfRowStatus_Object=MibTableColumn
juniBridgeIfRowStatus=_JuniBridgeIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1,2),_JuniBridgeIfRowStatus_Type())
juniBridgeIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgeIfRowStatus.setStatus(_A)
_JuniBridgeIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniBridgeIfLowerIfIndex_Object=MibTableColumn
juniBridgeIfLowerIfIndex=_JuniBridgeIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1,3),_JuniBridgeIfLowerIfIndex_Type())
juniBridgeIfLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgeIfLowerIfIndex.setStatus(_A)
_JuniBridgeSPolicyIndex_Type=Unsigned32
_JuniBridgeSPolicyIndex_Object=MibTableColumn
juniBridgeSPolicyIndex=_JuniBridgeSPolicyIndex_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1,4),_JuniBridgeSPolicyIndex_Type())
juniBridgeSPolicyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgeSPolicyIndex.setStatus(_A)
_JuniBridgeIfMaxLearnCount_Type=Unsigned32
_JuniBridgeIfMaxLearnCount_Object=MibTableColumn
juniBridgeIfMaxLearnCount=_JuniBridgeIfMaxLearnCount_Object((1,3,6,1,4,1,4874,2,2,63,1,2,1,5),_JuniBridgeIfMaxLearnCount_Type())
juniBridgeIfMaxLearnCount.setMaxAccess(_C)
if mibBuilder.loadTexts:juniBridgeIfMaxLearnCount.setStatus(_A)
_JuniBridgeAgeLayer_ObjectIdentity=ObjectIdentity
juniBridgeAgeLayer=_JuniBridgeAgeLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,2))
_JuniBridgeAgeTable_Object=MibTable
juniBridgeAgeTable=_JuniBridgeAgeTable_Object((1,3,6,1,4,1,4874,2,2,63,2,1))
if mibBuilder.loadTexts:juniBridgeAgeTable.setStatus(_A)
_JuniBridgeAgeEntry_Object=MibTableRow
juniBridgeAgeEntry=_JuniBridgeAgeEntry_Object((1,3,6,1,4,1,4874,2,2,63,2,1,1))
juniBridgeAgeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:juniBridgeAgeEntry.setStatus(_A)
_JuniBridgeMacAddress_Type=MacAddress
_JuniBridgeMacAddress_Object=MibTableColumn
juniBridgeMacAddress=_JuniBridgeMacAddress_Object((1,3,6,1,4,1,4874,2,2,63,2,1,1,1),_JuniBridgeMacAddress_Type())
juniBridgeMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:juniBridgeMacAddress.setStatus(_A)
_JuniBridgeAge_Type=Unsigned32
_JuniBridgeAge_Object=MibTableColumn
juniBridgeAge=_JuniBridgeAge_Object((1,3,6,1,4,1,4874,2,2,63,2,1,1,2),_JuniBridgeAge_Type())
juniBridgeAge.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgeAge.setStatus(_A)
_JuniBridgeMiscCounters_ObjectIdentity=ObjectIdentity
juniBridgeMiscCounters=_JuniBridgeMiscCounters_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,3))
_JuniBridgeDupMacCounter_Type=Counter32
_JuniBridgeDupMacCounter_Object=MibScalar
juniBridgeDupMacCounter=_JuniBridgeDupMacCounter_Object((1,3,6,1,4,1,4874,2,2,63,3,1),_JuniBridgeDupMacCounter_Type())
juniBridgeDupMacCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgeDupMacCounter.setStatus(_A)
_JuniBridgeConformance_ObjectIdentity=ObjectIdentity
juniBridgeConformance=_JuniBridgeConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,4))
_JuniBridgeCompliances_ObjectIdentity=ObjectIdentity
juniBridgeCompliances=_JuniBridgeCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,4,1))
_JuniBridgeGroups_ObjectIdentity=ObjectIdentity
juniBridgeGroups=_JuniBridgeGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,63,4,2))
juniBridgeGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,63,4,2,1))
juniBridgeGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:juniBridgeGroup.setStatus(_A)
juniBridgeCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,63,4,1,1))
juniBridgeCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:juniBridgeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'juniBridgeMIB':juniBridgeMIB,'juniBridgeIfLayer':juniBridgeIfLayer,_H:juniBridgeIfNextIfIndex,'juniBridgeIfTable':juniBridgeIfTable,'juniBridgeIfEntry':juniBridgeIfEntry,_E:juniBridgeIfIndex,_I:juniBridgeIfRowStatus,_J:juniBridgeIfLowerIfIndex,_K:juniBridgeSPolicyIndex,_L:juniBridgeIfMaxLearnCount,'juniBridgeAgeLayer':juniBridgeAgeLayer,'juniBridgeAgeTable':juniBridgeAgeTable,'juniBridgeAgeEntry':juniBridgeAgeEntry,_G:juniBridgeMacAddress,_M:juniBridgeAge,'juniBridgeMiscCounters':juniBridgeMiscCounters,_N:juniBridgeDupMacCounter,'juniBridgeConformance':juniBridgeConformance,'juniBridgeCompliances':juniBridgeCompliances,'juniBridgeCompliance':juniBridgeCompliance,'juniBridgeGroups':juniBridgeGroups,_O:juniBridgeGroup})