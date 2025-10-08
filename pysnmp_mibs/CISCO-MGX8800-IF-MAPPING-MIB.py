#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-MGX8800-IF-MAPPING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMGX8800IfMappingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 7))
ciscoMGX8800IfMappingMIB.setRevisions(('2004-05-25 00:00', '2004-04-30 00:00', '2003-12-04 00:00', '2003-03-20 00:00', '2002-10-21 00:00', '2002-10-16 00:00', '2002-05-21 00:00', '2002-02-17 00:00', '2001-10-16 00:00', '2001-07-08 00:00', '2000-02-12 00:00',))
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setLastUpdated('200405250000Z')
if mibBuilder.loadTexts: ciscoMGX8800IfMappingMIB.setOrganization('Cisco Systems, Inc.')
class CmimIfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("physicalLine", 1), ("atmIma", 2), ("atm", 3), ("atmVirtual", 4), ("ds1Inds3", 5), ("adjCardApsLine", 6), ("propAtm", 7), ("sonetVT", 8), ("imaGrpAtmPhy", 9), ("srmBertLine", 10), ("srmBertPort", 11), ("sonetPath", 12), ("ds3SonetPath", 13), ("atmSonetPath", 14), ("atmDs3SonetPath", 15), ("frameRelayPort", 16), ("ces", 17), ("ds1VTPath", 18), ("ds1Ds3SonetPath", 19), ("atmVciEndPt", 20), ("mfrBundle", 21), ("ppplink", 22), ("pppMpbundle", 23), ("lapd", 24))

cmimMappingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1))
cmimPhysToIf = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1))
cmimPhysToIfTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1), )
if mibBuilder.loadTexts: cmimPhysToIfTable.setStatus('current')
cmimPhysToIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimModuleIndex"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfNumber"), (0, "CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfType"))
if mibBuilder.loadTexts: cmimPhysToIfEntry.setStatus('current')
cmimModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cmimModuleIndex.setStatus('current')
cmimIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cmimIfNumber.setStatus('current')
cmimIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 3), CmimIfType())
if mibBuilder.loadTexts: cmimIfType.setStatus('current')
cmimIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 7, 1, 1, 1, 1, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmimIfIndex.setStatus('current')
cmimPhysToIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3))
cmimPhysToIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1))
cmimPhysToIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2))
cmimPhysToIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 1, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimPhysToIfMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBCompliance = cmimPhysToIfMIBCompliance.setStatus('current')
cmimPhysToIfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 7, 3, 2, 1)).setObjects(("CISCO-MGX8800-IF-MAPPING-MIB", "cmimIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmimPhysToIfMIBGroup = cmimPhysToIfMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-MIB", PYSNMP_MODULE_ID=ciscoMGX8800IfMappingMIB, cmimPhysToIfTable=cmimPhysToIfTable, cmimIfType=cmimIfType, cmimIfIndex=cmimIfIndex, cmimPhysToIfMIBGroup=cmimPhysToIfMIBGroup, cmimPhysToIfMIBCompliances=cmimPhysToIfMIBCompliances, cmimPhysToIfMIBConformance=cmimPhysToIfMIBConformance, cmimPhysToIfMIBGroups=cmimPhysToIfMIBGroups, cmimMappingObjects=cmimMappingObjects, cmimPhysToIfEntry=cmimPhysToIfEntry, CmimIfType=CmimIfType, cmimPhysToIf=cmimPhysToIf, cmimModuleIndex=cmimModuleIndex, cmimIfNumber=cmimIfNumber, cmimPhysToIfMIBCompliance=cmimPhysToIfMIBCompliance, ciscoMGX8800IfMappingMIB=ciscoMGX8800IfMappingMIB)
