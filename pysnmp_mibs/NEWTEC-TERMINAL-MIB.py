#
# PySNMP MIB module NEWTEC-TERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-TERMINAL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcTerminal = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900))
ntcTerminal.setRevisions(('2013-01-08 12:00',))
if mibBuilder.loadTexts: ntcTerminal.setLastUpdated('201301081200Z')
if mibBuilder.loadTexts: ntcTerminal.setOrganization('Newtec Cy')
ntcTermObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 1))
if mibBuilder.loadTexts: ntcTermObjects.setStatus('current')
ntcTermConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2))
if mibBuilder.loadTexts: ntcTermConformance.setStatus('current')
ntcTermConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 1))
if mibBuilder.loadTexts: ntcTermConfCompliance.setStatus('current')
ntcTermConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 2))
if mibBuilder.loadTexts: ntcTermConfGroup.setStatus('current')
ntcTermId = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65277))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcTermId.setStatus('current')
ntcTermConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 2, 1)).setObjects(("NEWTEC-TERMINAL-MIB", "ntcTermId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcTermConfGrpV1Standard = ntcTermConfGrpV1Standard.setStatus('current')
ntcTermConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 2900, 2, 1, 1)).setObjects(("NEWTEC-TERMINAL-MIB", "ntcTermConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcTermConfCompV1Standard = ntcTermConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-TERMINAL-MIB", ntcTermObjects=ntcTermObjects, ntcTermId=ntcTermId, ntcTermConfCompliance=ntcTermConfCompliance, PYSNMP_MODULE_ID=ntcTerminal, ntcTermConfCompV1Standard=ntcTermConfCompV1Standard, ntcTermConfGroup=ntcTermConfGroup, ntcTerminal=ntcTerminal, ntcTermConformance=ntcTermConformance, ntcTermConfGrpV1Standard=ntcTermConfGrpV1Standard)
