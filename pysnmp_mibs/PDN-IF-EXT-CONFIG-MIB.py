_M='pdnIfXLinkConfigOptionalGroup'
_L='pdnIfMultiprotocolEncapsulationOptionalGroup'
_K='pdnIfXLinkConfigRole'
_J='pdnIfMultiprotocolEncapConfigBridgedPDUs'
_I='pdnIfMultiprotocolEncapConfigIPRoutedPDUs'
_H='vcBasedMultiplexing'
_G='llcSnap'
_F='read-write'
_E='Integer32'
_D='ifIndex'
_C='IF-MIB'
_B='PDN-IF-EXT-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
pdnIfExt,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnIfExt')
pdnIfExtConfig,=mibBuilder.importSymbols('PDN-IFEXT-MIB','pdnIfExtConfig')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnIfExtEncapConfig=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,3))
if mibBuilder.loadTexts:pdnIfExtEncapConfig.setRevisions(('2003-12-16 09:00','2001-11-13 00:00','2001-11-12 00:00','2000-05-11 00:00','2000-05-03 00:00','2000-05-02 00:00'))
class PdnLinkRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uplink',1),('other',2)))
_PdnIfXLinkConfigTable_Object=MibTable
pdnIfXLinkConfigTable=_PdnIfXLinkConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,3))
if mibBuilder.loadTexts:pdnIfXLinkConfigTable.setStatus(_A)
_PdnIfXLinkConfigEntry_Object=MibTableRow
pdnIfXLinkConfigEntry=_PdnIfXLinkConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,3,1))
pdnIfXLinkConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pdnIfXLinkConfigEntry.setStatus(_A)
_PdnIfXLinkConfigRole_Type=PdnLinkRole
_PdnIfXLinkConfigRole_Object=MibTableColumn
pdnIfXLinkConfigRole=_PdnIfXLinkConfigRole_Object((1,3,6,1,4,1,1795,2,24,2,6,12,1,3,1,1),_PdnIfXLinkConfigRole_Type())
pdnIfXLinkConfigRole.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnIfXLinkConfigRole.setStatus(_A)
_PdnIfMultiprotocolEncapConfigTable_Object=MibTable
pdnIfMultiprotocolEncapConfigTable=_PdnIfMultiprotocolEncapConfigTable_Object((1,3,6,1,4,1,1795,2,24,2,6,12,3,1))
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapConfigTable.setStatus(_A)
_PdnIfMultiprotocolEncapConfigEntry_Object=MibTableRow
pdnIfMultiprotocolEncapConfigEntry=_PdnIfMultiprotocolEncapConfigEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,12,3,1,1))
pdnIfMultiprotocolEncapConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapConfigEntry.setStatus(_A)
class _PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_G,2),(_H,3)))
_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type.__name__=_E
_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Object=MibTableColumn
pdnIfMultiprotocolEncapConfigIPRoutedPDUs=_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Object((1,3,6,1,4,1,1795,2,24,2,6,12,3,1,1,1),_PdnIfMultiprotocolEncapConfigIPRoutedPDUs_Type())
pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapConfigIPRoutedPDUs.setStatus(_A)
class _PdnIfMultiprotocolEncapConfigBridgedPDUs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_G,2),(_H,3)))
_PdnIfMultiprotocolEncapConfigBridgedPDUs_Type.__name__=_E
_PdnIfMultiprotocolEncapConfigBridgedPDUs_Object=MibTableColumn
pdnIfMultiprotocolEncapConfigBridgedPDUs=_PdnIfMultiprotocolEncapConfigBridgedPDUs_Object((1,3,6,1,4,1,1795,2,24,2,6,12,3,1,1,2),_PdnIfMultiprotocolEncapConfigBridgedPDUs_Type())
pdnIfMultiprotocolEncapConfigBridgedPDUs.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapConfigBridgedPDUs.setStatus(_A)
_PdnIfMultiprotocolEncapMIBConformance_ObjectIdentity=ObjectIdentity
pdnIfMultiprotocolEncapMIBConformance=_PdnIfMultiprotocolEncapMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,3,2))
_PdnIfMultiprotocolEncapMIBGroups_ObjectIdentity=ObjectIdentity
pdnIfMultiprotocolEncapMIBGroups=_PdnIfMultiprotocolEncapMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,3,2,1))
_PdnIfMultiprotocolEncapCompliances_ObjectIdentity=ObjectIdentity
pdnIfMultiprotocolEncapCompliances=_PdnIfMultiprotocolEncapCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,3,2,2))
_PdnIfXConfigMIBConformance_ObjectIdentity=ObjectIdentity
pdnIfXConfigMIBConformance=_PdnIfXConfigMIBConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,4))
_PdnIfXConfigMIBGroups_ObjectIdentity=ObjectIdentity
pdnIfXConfigMIBGroups=_PdnIfXConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,12,4,1))
pdnIfMultiprotocolEncapsulationOptionalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,12,3,2,1,1))
pdnIfMultiprotocolEncapsulationOptionalGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapsulationOptionalGroup.setStatus(_A)
pdnIfXLinkConfigOptionalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,12,4,1,1))
pdnIfXLinkConfigOptionalGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:pdnIfXLinkConfigOptionalGroup.setStatus(_A)
pdnIfMultiprotocolEncapCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,12,3,2,2,1))
pdnIfMultiprotocolEncapCompliance.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:pdnIfMultiprotocolEncapCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnLinkRole':PdnLinkRole,'pdnIfXLinkConfigTable':pdnIfXLinkConfigTable,'pdnIfXLinkConfigEntry':pdnIfXLinkConfigEntry,_K:pdnIfXLinkConfigRole,'pdnIfExtEncapConfig':pdnIfExtEncapConfig,'pdnIfMultiprotocolEncapConfigTable':pdnIfMultiprotocolEncapConfigTable,'pdnIfMultiprotocolEncapConfigEntry':pdnIfMultiprotocolEncapConfigEntry,_I:pdnIfMultiprotocolEncapConfigIPRoutedPDUs,_J:pdnIfMultiprotocolEncapConfigBridgedPDUs,'pdnIfMultiprotocolEncapMIBConformance':pdnIfMultiprotocolEncapMIBConformance,'pdnIfMultiprotocolEncapMIBGroups':pdnIfMultiprotocolEncapMIBGroups,_L:pdnIfMultiprotocolEncapsulationOptionalGroup,'pdnIfMultiprotocolEncapCompliances':pdnIfMultiprotocolEncapCompliances,'pdnIfMultiprotocolEncapCompliance':pdnIfMultiprotocolEncapCompliance,'pdnIfXConfigMIBConformance':pdnIfXConfigMIBConformance,'pdnIfXConfigMIBGroups':pdnIfXConfigMIBGroups,_M:pdnIfXLinkConfigOptionalGroup})