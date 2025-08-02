_M='ciscoAtmTrafficNmsGroup'
_L='atmTrafficDescriptorName'
_K='atmTrafficDerivedServCategory'
_J='atmTrafficExplicitServCategory'
_I='atmTrafficDescrParamExtEntry'
_H='read-create'
_G='vbrNrt'
_F='deprecated'
_E='SnmpAdminString'
_D='ciscoAtmTrafficTableExtMIBGroup'
_C='Integer32'
_B='CISCO-ATM-TRAFFIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmTrafficDescrParamEntry,=mibBuilder.importSymbols('ATM-MIB','atmTrafficDescrParamEntry')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAtmTrafficExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,11))
if mibBuilder.loadTexts:ciscoAtmTrafficExtMIB.setRevisions(('2002-08-26 00:00','2001-11-01 00:00','1997-05-29 00:00'))
_CiscoAtmTrafficExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficExtMIBObjects=_CiscoAtmTrafficExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,11,1))
_CiscoAtmTrafficTypeExt_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficTypeExt=_CiscoAtmTrafficTypeExt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1))
_AtmNoClpNoScrCdvt_ObjectIdentity=ObjectIdentity
atmNoClpNoScrCdvt=_AtmNoClpNoScrCdvt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1,1))
if mibBuilder.loadTexts:atmNoClpNoScrCdvt.setStatus(_F)
_AtmClpScrMbsCdvt_ObjectIdentity=ObjectIdentity
atmClpScrMbsCdvt=_AtmClpScrMbsCdvt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1,2))
if mibBuilder.loadTexts:atmClpScrMbsCdvt.setStatus(_A)
_AtmNoClpScrMbsCdvt_ObjectIdentity=ObjectIdentity
atmNoClpScrMbsCdvt=_AtmNoClpScrMbsCdvt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1,3))
if mibBuilder.loadTexts:atmNoClpScrMbsCdvt.setStatus(_A)
_AtmNoClpMcr_ObjectIdentity=ObjectIdentity
atmNoClpMcr=_AtmNoClpMcr_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1,4))
if mibBuilder.loadTexts:atmNoClpMcr.setStatus(_A)
_AtmNoClpMcrCdvt_ObjectIdentity=ObjectIdentity
atmNoClpMcrCdvt=_AtmNoClpMcrCdvt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,1,5))
if mibBuilder.loadTexts:atmNoClpMcrCdvt.setStatus(_A)
_CiscoAtmTrafficTableExt_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficTableExt=_CiscoAtmTrafficTableExt_ObjectIdentity((1,3,6,1,4,1,9,10,11,1,2))
_AtmTrafficDescrParamExtTable_Object=MibTable
atmTrafficDescrParamExtTable=_AtmTrafficDescrParamExtTable_Object((1,3,6,1,4,1,9,10,11,1,2,1))
if mibBuilder.loadTexts:atmTrafficDescrParamExtTable.setStatus(_A)
_AtmTrafficDescrParamExtEntry_Object=MibTableRow
atmTrafficDescrParamExtEntry=_AtmTrafficDescrParamExtEntry_Object((1,3,6,1,4,1,9,10,11,1,2,1,1))
if mibBuilder.loadTexts:atmTrafficDescrParamExtEntry.setStatus(_A)
class _AtmTrafficExplicitServCategory_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cbr',1),('vbrRt',2),(_G,3),('abr',4),('ubr',5),('notDef',6)))
_AtmTrafficExplicitServCategory_Type.__name__=_C
_AtmTrafficExplicitServCategory_Object=MibTableColumn
atmTrafficExplicitServCategory=_AtmTrafficExplicitServCategory_Object((1,3,6,1,4,1,9,10,11,1,2,1,1,1),_AtmTrafficExplicitServCategory_Type())
atmTrafficExplicitServCategory.setMaxAccess(_H)
if mibBuilder.loadTexts:atmTrafficExplicitServCategory.setStatus(_A)
class _AtmTrafficDerivedServCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cbr',1),('vbrRt',2),(_G,3),('abr',4),('ubr',5)))
_AtmTrafficDerivedServCategory_Type.__name__=_C
_AtmTrafficDerivedServCategory_Object=MibTableColumn
atmTrafficDerivedServCategory=_AtmTrafficDerivedServCategory_Object((1,3,6,1,4,1,9,10,11,1,2,1,1,2),_AtmTrafficDerivedServCategory_Type())
atmTrafficDerivedServCategory.setMaxAccess('read-only')
if mibBuilder.loadTexts:atmTrafficDerivedServCategory.setStatus(_A)
class _AtmTrafficDescriptorName_Type(SnmpAdminString):defaultValue=OctetString('')
_AtmTrafficDescriptorName_Type.__name__=_E
_AtmTrafficDescriptorName_Object=MibTableColumn
atmTrafficDescriptorName=_AtmTrafficDescriptorName_Object((1,3,6,1,4,1,9,10,11,1,2,1,1,3),_AtmTrafficDescriptorName_Type())
atmTrafficDescriptorName.setMaxAccess(_H)
if mibBuilder.loadTexts:atmTrafficDescriptorName.setStatus(_A)
_CiscoAtmTrafficExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficExtMIBConformance=_CiscoAtmTrafficExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,11,3))
_CiscoAtmTrafficExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficExtMIBCompliances=_CiscoAtmTrafficExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,11,3,1))
_CiscoAtmTrafficExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmTrafficExtMIBGroups=_CiscoAtmTrafficExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,11,3,2))
atmTrafficDescrParamEntry.registerAugmentions((_B,_I))
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
ciscoAtmTrafficTableExtMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,11,3,2,1))
ciscoAtmTrafficTableExtMIBGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoAtmTrafficTableExtMIBGroup.setStatus(_A)
ciscoAtmTrafficNmsGroup=ObjectGroup((1,3,6,1,4,1,9,10,11,3,2,2))
ciscoAtmTrafficNmsGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:ciscoAtmTrafficNmsGroup.setStatus(_A)
ciscoAtmTrafficExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,11,3,1,1))
ciscoAtmTrafficExtMIBCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:ciscoAtmTrafficExtMIBCompliance.setStatus(_F)
ciscoAtmTrafficExtMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,11,3,1,2))
ciscoAtmTrafficExtMIBComplianceRev1.setObjects(*((_B,_D),(_B,_M)))
if mibBuilder.loadTexts:ciscoAtmTrafficExtMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoAtmTrafficExtMIB':ciscoAtmTrafficExtMIB,'ciscoAtmTrafficExtMIBObjects':ciscoAtmTrafficExtMIBObjects,'ciscoAtmTrafficTypeExt':ciscoAtmTrafficTypeExt,'atmNoClpNoScrCdvt':atmNoClpNoScrCdvt,'atmClpScrMbsCdvt':atmClpScrMbsCdvt,'atmNoClpScrMbsCdvt':atmNoClpScrMbsCdvt,'atmNoClpMcr':atmNoClpMcr,'atmNoClpMcrCdvt':atmNoClpMcrCdvt,'ciscoAtmTrafficTableExt':ciscoAtmTrafficTableExt,'atmTrafficDescrParamExtTable':atmTrafficDescrParamExtTable,_I:atmTrafficDescrParamExtEntry,_J:atmTrafficExplicitServCategory,_K:atmTrafficDerivedServCategory,_L:atmTrafficDescriptorName,'ciscoAtmTrafficExtMIBConformance':ciscoAtmTrafficExtMIBConformance,'ciscoAtmTrafficExtMIBCompliances':ciscoAtmTrafficExtMIBCompliances,'ciscoAtmTrafficExtMIBCompliance':ciscoAtmTrafficExtMIBCompliance,'ciscoAtmTrafficExtMIBComplianceRev1':ciscoAtmTrafficExtMIBComplianceRev1,'ciscoAtmTrafficExtMIBGroups':ciscoAtmTrafficExtMIBGroups,_D:ciscoAtmTrafficTableExtMIBGroup,_M:ciscoAtmTrafficNmsGroup})