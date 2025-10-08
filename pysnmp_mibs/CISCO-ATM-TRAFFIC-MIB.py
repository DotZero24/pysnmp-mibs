#
# PySNMP MIB module CISCO-ATM-TRAFFIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ATM-TRAFFIC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmTrafficExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11))
ciscoAtmTrafficExtMIB.setRevisions(('2002-08-26 00:00', '2001-11-01 00:00', '1997-05-29 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setLastUpdated('200208260000Z')
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setOrganization('Cisco System Inc.')
ciscoAtmTrafficExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1))
ciscoAtmTrafficTypeExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1))
ciscoAtmTrafficTableExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2))
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('deprecated')
atmClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2))
if mibBuilder.loadTexts: atmClpScrMbsCdvt.setStatus('current')
atmNoClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3))
if mibBuilder.loadTexts: atmNoClpScrMbsCdvt.setStatus('current')
atmNoClpMcr = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4))
if mibBuilder.loadTexts: atmNoClpMcr.setStatus('current')
atmNoClpMcrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpMcrCdvt.setStatus('current')
atmTrafficDescrParamExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1), )
if mibBuilder.loadTexts: atmTrafficDescrParamExtTable.setStatus('current')
atmTrafficDescrParamExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescrParamExtEntry"))
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: atmTrafficDescrParamExtEntry.setStatus('current')
atmTrafficExplicitServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5), ("notDef", 6))).clone('notDef')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficExplicitServCategory.setStatus('current')
atmTrafficDerivedServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTrafficDerivedServCategory.setStatus('current')
atmTrafficDescriptorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficDescriptorName.setStatus('current')
ciscoAtmTrafficExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3))
ciscoAtmTrafficExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1))
ciscoAtmTrafficExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2))
ciscoAtmTrafficExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBCompliance = ciscoAtmTrafficExtMIBCompliance.setStatus('deprecated')
ciscoAtmTrafficExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"), ("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficNmsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBComplianceRev1 = ciscoAtmTrafficExtMIBComplianceRev1.setStatus('current')
ciscoAtmTrafficTableExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficExplicitServCategory"), ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDerivedServCategory"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficTableExtMIBGroup = ciscoAtmTrafficTableExtMIBGroup.setStatus('current')
ciscoAtmTrafficNmsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescriptorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficNmsGroup = ciscoAtmTrafficNmsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRAFFIC-MIB", atmTrafficDescriptorName=atmTrafficDescriptorName, ciscoAtmTrafficExtMIBCompliance=ciscoAtmTrafficExtMIBCompliance, atmNoClpScrMbsCdvt=atmNoClpScrMbsCdvt, ciscoAtmTrafficExtMIBComplianceRev1=ciscoAtmTrafficExtMIBComplianceRev1, ciscoAtmTrafficTableExtMIBGroup=ciscoAtmTrafficTableExtMIBGroup, ciscoAtmTrafficExtMIBGroups=ciscoAtmTrafficExtMIBGroups, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, atmTrafficExplicitServCategory=atmTrafficExplicitServCategory, ciscoAtmTrafficNmsGroup=ciscoAtmTrafficNmsGroup, ciscoAtmTrafficTableExt=ciscoAtmTrafficTableExt, ciscoAtmTrafficExtMIBObjects=ciscoAtmTrafficExtMIBObjects, ciscoAtmTrafficExtMIBCompliances=ciscoAtmTrafficExtMIBCompliances, ciscoAtmTrafficExtMIB=ciscoAtmTrafficExtMIB, atmTrafficDescrParamExtTable=atmTrafficDescrParamExtTable, ciscoAtmTrafficExtMIBConformance=ciscoAtmTrafficExtMIBConformance, atmClpScrMbsCdvt=atmClpScrMbsCdvt, ciscoAtmTrafficTypeExt=ciscoAtmTrafficTypeExt, atmNoClpMcrCdvt=atmNoClpMcrCdvt, PYSNMP_MODULE_ID=ciscoAtmTrafficExtMIB, atmTrafficDerivedServCategory=atmTrafficDerivedServCategory, atmNoClpMcr=atmNoClpMcr, atmTrafficDescrParamExtEntry=atmTrafficDescrParamExtEntry)
