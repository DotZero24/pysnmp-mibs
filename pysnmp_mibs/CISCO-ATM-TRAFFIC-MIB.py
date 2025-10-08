#
# PySNMP MIB module CISCO-ATM-TRAFFIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ATM-TRAFFIC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-ATM-TRAFFIC-MIB", atmNoClpMcr=atmNoClpMcr, PYSNMP_MODULE_ID=ciscoAtmTrafficExtMIB, ciscoAtmTrafficExtMIBConformance=ciscoAtmTrafficExtMIBConformance, ciscoAtmTrafficExtMIBComplianceRev1=ciscoAtmTrafficExtMIBComplianceRev1, ciscoAtmTrafficExtMIBCompliances=ciscoAtmTrafficExtMIBCompliances, atmNoClpScrMbsCdvt=atmNoClpScrMbsCdvt, atmTrafficExplicitServCategory=atmTrafficExplicitServCategory, atmTrafficDescriptorName=atmTrafficDescriptorName, ciscoAtmTrafficTypeExt=ciscoAtmTrafficTypeExt, atmTrafficDescrParamExtTable=atmTrafficDescrParamExtTable, ciscoAtmTrafficExtMIBGroups=ciscoAtmTrafficExtMIBGroups, atmTrafficDescrParamExtEntry=atmTrafficDescrParamExtEntry, atmTrafficDerivedServCategory=atmTrafficDerivedServCategory, ciscoAtmTrafficTableExt=ciscoAtmTrafficTableExt, atmNoClpMcrCdvt=atmNoClpMcrCdvt, ciscoAtmTrafficTableExtMIBGroup=ciscoAtmTrafficTableExtMIBGroup, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, ciscoAtmTrafficExtMIB=ciscoAtmTrafficExtMIB, ciscoAtmTrafficExtMIBCompliance=ciscoAtmTrafficExtMIBCompliance, atmClpScrMbsCdvt=atmClpScrMbsCdvt, ciscoAtmTrafficNmsGroup=ciscoAtmTrafficNmsGroup, ciscoAtmTrafficExtMIBObjects=ciscoAtmTrafficExtMIBObjects)
