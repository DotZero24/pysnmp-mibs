#
# PySNMP MIB module NEWTEC-TERMINAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-TERMINAL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:44 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-TERMINAL-MIB", ntcTermConfGroup=ntcTermConfGroup, PYSNMP_MODULE_ID=ntcTerminal, ntcTermId=ntcTermId, ntcTermConfCompliance=ntcTermConfCompliance, ntcTermConformance=ntcTermConformance, ntcTerminal=ntcTerminal, ntcTermConfCompV1Standard=ntcTermConfCompV1Standard, ntcTermConfGrpV1Standard=ntcTermConfGrpV1Standard, ntcTermObjects=ntcTermObjects)
