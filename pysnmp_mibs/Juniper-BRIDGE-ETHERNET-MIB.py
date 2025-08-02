_O='juniBridgedEthernetGroup3'
_N='juniBridgedEthernetGroup2'
_M='juniBridgedEthernetIfMtu'
_L='deprecated'
_K='juniBridgedEthernetProxyArp'
_J='obsolete'
_I='read-only'
_H='Integer32'
_G='juniBridgedEthernetIfRowStatus'
_F='juniBridgedEthernetIfLowerIfIndex'
_E='juniBridgedEthernetNextIfIndex'
_D='read-create'
_C='juniBridgedEthernetIfIfIndex'
_B='current'
_A='Juniper-BRIDGE-ETHERNET-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniBridgeEthernetMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,31))
if mibBuilder.loadTexts:juniBridgeEthernetMIB.setRevisions(('2005-12-14 17:10','2002-09-16 21:44','2000-09-26 14:43','2000-03-27 23:45','1999-12-10 18:30'))
_JuniBridgedEthernetObjects_ObjectIdentity=ObjectIdentity
juniBridgedEthernetObjects=_JuniBridgedEthernetObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,31,1))
_JuniBridgedEthernetIfLayer_ObjectIdentity=ObjectIdentity
juniBridgedEthernetIfLayer=_JuniBridgedEthernetIfLayer_ObjectIdentity((1,3,6,1,4,1,4874,2,2,31,1,1))
_JuniBridgedEthernetNextIfIndex_Type=JuniNextIfIndex
_JuniBridgedEthernetNextIfIndex_Object=MibScalar
juniBridgedEthernetNextIfIndex=_JuniBridgedEthernetNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,31,1,1,1),_JuniBridgedEthernetNextIfIndex_Type())
juniBridgedEthernetNextIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniBridgedEthernetNextIfIndex.setStatus(_B)
_JuniBridgedEthernetIfTable_Object=MibTable
juniBridgedEthernetIfTable=_JuniBridgedEthernetIfTable_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2))
if mibBuilder.loadTexts:juniBridgedEthernetIfTable.setStatus(_B)
_JuniBridgedEthernetIfEntry_Object=MibTableRow
juniBridgedEthernetIfEntry=_JuniBridgedEthernetIfEntry_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1))
juniBridgedEthernetIfEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:juniBridgedEthernetIfEntry.setStatus(_B)
_JuniBridgedEthernetIfIfIndex_Type=InterfaceIndex
_JuniBridgedEthernetIfIfIndex_Object=MibTableColumn
juniBridgedEthernetIfIfIndex=_JuniBridgedEthernetIfIfIndex_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1,1),_JuniBridgedEthernetIfIfIndex_Type())
juniBridgedEthernetIfIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniBridgedEthernetIfIfIndex.setStatus(_B)
class _JuniBridgedEthernetProxyArp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enableRestricted',1),('enableUnrestricted',2),('disable',3)))
_JuniBridgedEthernetProxyArp_Type.__name__=_H
_JuniBridgedEthernetProxyArp_Object=MibTableColumn
juniBridgedEthernetProxyArp=_JuniBridgedEthernetProxyArp_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1,2),_JuniBridgedEthernetProxyArp_Type())
juniBridgedEthernetProxyArp.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgedEthernetProxyArp.setStatus(_J)
_JuniBridgedEthernetIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniBridgedEthernetIfLowerIfIndex_Object=MibTableColumn
juniBridgedEthernetIfLowerIfIndex=_JuniBridgedEthernetIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1,3),_JuniBridgedEthernetIfLowerIfIndex_Type())
juniBridgedEthernetIfLowerIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgedEthernetIfLowerIfIndex.setStatus(_B)
_JuniBridgedEthernetIfRowStatus_Type=RowStatus
_JuniBridgedEthernetIfRowStatus_Object=MibTableColumn
juniBridgedEthernetIfRowStatus=_JuniBridgedEthernetIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1,4),_JuniBridgedEthernetIfRowStatus_Type())
juniBridgedEthernetIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgedEthernetIfRowStatus.setStatus(_B)
class _JuniBridgedEthernetIfMtu_Type(Integer32):defaultValue=1518;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9180))
_JuniBridgedEthernetIfMtu_Type.__name__=_H
_JuniBridgedEthernetIfMtu_Object=MibTableColumn
juniBridgedEthernetIfMtu=_JuniBridgedEthernetIfMtu_Object((1,3,6,1,4,1,4874,2,2,31,1,1,2,1,5),_JuniBridgedEthernetIfMtu_Type())
juniBridgedEthernetIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:juniBridgedEthernetIfMtu.setStatus(_B)
_JuniBridgeEthernetConformance_ObjectIdentity=ObjectIdentity
juniBridgeEthernetConformance=_JuniBridgeEthernetConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,31,4))
_JuniBridgeEthernetCompliances_ObjectIdentity=ObjectIdentity
juniBridgeEthernetCompliances=_JuniBridgeEthernetCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,31,4,1))
_JuniBridgeEthernetGroups_ObjectIdentity=ObjectIdentity
juniBridgeEthernetGroups=_JuniBridgeEthernetGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,31,4,2))
juniBridgedEthernetGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,31,4,2,1))
juniBridgedEthernetGroup.setObjects(*((_A,_E),(_A,_C),(_A,_K),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniBridgedEthernetGroup.setStatus(_J)
juniBridgedEthernetGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,31,4,2,2))
juniBridgedEthernetGroup2.setObjects(*((_A,_E),(_A,_C),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:juniBridgedEthernetGroup2.setStatus(_L)
juniBridgedEthernetGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,31,4,2,3))
juniBridgedEthernetGroup3.setObjects(*((_A,_E),(_A,_C),(_A,_F),(_A,_G),(_A,_M)))
if mibBuilder.loadTexts:juniBridgedEthernetGroup3.setStatus(_B)
juniBridgedEthernetCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,31,4,1,1))
juniBridgedEthernetCompliance.setObjects((_A,_N))
if mibBuilder.loadTexts:juniBridgedEthernetCompliance.setStatus(_L)
juniBridgedEthernetCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,31,4,1,2))
juniBridgedEthernetCompliance2.setObjects((_A,_O))
if mibBuilder.loadTexts:juniBridgedEthernetCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniBridgeEthernetMIB':juniBridgeEthernetMIB,'juniBridgedEthernetObjects':juniBridgedEthernetObjects,'juniBridgedEthernetIfLayer':juniBridgedEthernetIfLayer,_E:juniBridgedEthernetNextIfIndex,'juniBridgedEthernetIfTable':juniBridgedEthernetIfTable,'juniBridgedEthernetIfEntry':juniBridgedEthernetIfEntry,_C:juniBridgedEthernetIfIfIndex,_K:juniBridgedEthernetProxyArp,_F:juniBridgedEthernetIfLowerIfIndex,_G:juniBridgedEthernetIfRowStatus,_M:juniBridgedEthernetIfMtu,'juniBridgeEthernetConformance':juniBridgeEthernetConformance,'juniBridgeEthernetCompliances':juniBridgeEthernetCompliances,'juniBridgedEthernetCompliance':juniBridgedEthernetCompliance,'juniBridgedEthernetCompliance2':juniBridgedEthernetCompliance2,'juniBridgeEthernetGroups':juniBridgeEthernetGroups,'juniBridgedEthernetGroup':juniBridgedEthernetGroup,_N:juniBridgedEthernetGroup2,_O:juniBridgedEthernetGroup3})