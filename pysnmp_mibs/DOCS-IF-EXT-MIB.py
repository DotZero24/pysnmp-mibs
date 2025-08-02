_I='docsIfExtGroup'
_H='docsIfCmtsCmStatusDocsisMode'
_G='docsIfDocsisOperMode'
_F='docsIfDocsisCapability'
_E='docsIfCmtsCmStatusExtEntry'
_D='docsIfDocsisVersionGroup'
_C='read-only'
_B='DOCS-IF-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
docsIfCmtsCmStatusEntry,docsIfMib=mibBuilder.importSymbols('DOCS-IF-MIB','docsIfCmtsCmStatusEntry','docsIfMib')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
docsIfExtMib=ModuleIdentity((1,3,6,1,2,1,10,127,21))
if mibBuilder.loadTexts:docsIfExtMib.setRevisions(('2000-10-08 00:00',))
class DocsisVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('docsis10',1),('docsis11',2)))
_DocsIfDocsisCapability_Type=DocsisVersion
_DocsIfDocsisCapability_Object=MibScalar
docsIfDocsisCapability=_DocsIfDocsisCapability_Object((1,3,6,1,2,1,10,127,21,1),_DocsIfDocsisCapability_Type())
docsIfDocsisCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfDocsisCapability.setStatus(_A)
_DocsIfDocsisOperMode_Type=DocsisVersion
_DocsIfDocsisOperMode_Object=MibScalar
docsIfDocsisOperMode=_DocsIfDocsisOperMode_Object((1,3,6,1,2,1,10,127,21,2),_DocsIfDocsisOperMode_Type())
docsIfDocsisOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfDocsisOperMode.setStatus(_A)
_DocsIfCmtsCmStatusExtTable_Object=MibTable
docsIfCmtsCmStatusExtTable=_DocsIfCmtsCmStatusExtTable_Object((1,3,6,1,2,1,10,127,21,3))
if mibBuilder.loadTexts:docsIfCmtsCmStatusExtTable.setStatus(_A)
_DocsIfCmtsCmStatusExtEntry_Object=MibTableRow
docsIfCmtsCmStatusExtEntry=_DocsIfCmtsCmStatusExtEntry_Object((1,3,6,1,2,1,10,127,21,3,1))
if mibBuilder.loadTexts:docsIfCmtsCmStatusExtEntry.setStatus(_A)
_DocsIfCmtsCmStatusDocsisMode_Type=DocsisVersion
_DocsIfCmtsCmStatusDocsisMode_Object=MibTableColumn
docsIfCmtsCmStatusDocsisMode=_DocsIfCmtsCmStatusDocsisMode_Object((1,3,6,1,2,1,10,127,21,3,1,1),_DocsIfCmtsCmStatusDocsisMode_Type())
docsIfCmtsCmStatusDocsisMode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsIfCmtsCmStatusDocsisMode.setStatus(_A)
_DocsIfExtConformance_ObjectIdentity=ObjectIdentity
docsIfExtConformance=_DocsIfExtConformance_ObjectIdentity((1,3,6,1,2,1,10,127,21,4))
_DocsIfExtCompliances_ObjectIdentity=ObjectIdentity
docsIfExtCompliances=_DocsIfExtCompliances_ObjectIdentity((1,3,6,1,2,1,10,127,21,4,1))
_DocsIfExtGroups_ObjectIdentity=ObjectIdentity
docsIfExtGroups=_DocsIfExtGroups_ObjectIdentity((1,3,6,1,2,1,10,127,21,4,2))
docsIfCmtsCmStatusEntry.registerAugmentions((_B,_E))
docsIfCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
docsIfDocsisVersionGroup=ObjectGroup((1,3,6,1,2,1,10,127,21,4,2,1))
docsIfDocsisVersionGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:docsIfDocsisVersionGroup.setStatus(_A)
docsIfExtGroup=ObjectGroup((1,3,6,1,2,1,10,127,21,4,2,2))
docsIfExtGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:docsIfExtGroup.setStatus(_A)
docsIfExtCmCompliance=ModuleCompliance((1,3,6,1,2,1,10,127,21,4,1,1))
docsIfExtCmCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:docsIfExtCmCompliance.setStatus(_A)
docsIfExtCmtsCompliance=ModuleCompliance((1,3,6,1,2,1,10,127,21,4,1,2))
docsIfExtCmtsCompliance.setObjects(*((_B,_I),(_B,_D)))
if mibBuilder.loadTexts:docsIfExtCmtsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'DocsisVersion':DocsisVersion,'docsIfExtMib':docsIfExtMib,_F:docsIfDocsisCapability,_G:docsIfDocsisOperMode,'docsIfCmtsCmStatusExtTable':docsIfCmtsCmStatusExtTable,_E:docsIfCmtsCmStatusExtEntry,_H:docsIfCmtsCmStatusDocsisMode,'docsIfExtConformance':docsIfExtConformance,'docsIfExtCompliances':docsIfExtCompliances,'docsIfExtCmCompliance':docsIfExtCmCompliance,'docsIfExtCmtsCompliance':docsIfExtCmtsCompliance,'docsIfExtGroups':docsIfExtGroups,_D:docsIfDocsisVersionGroup,_I:docsIfExtGroup})