#
# PySNMP MIB module MX-CORNET-DEBUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-CORNET-DEBUG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corNetDebugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 110))
corNetDebugMIB.setRevisions(('2005-05-18 00:00',))
if mibBuilder.loadTexts: corNetDebugMIB.setLastUpdated('200505180000Z')
if mibBuilder.loadTexts: corNetDebugMIB.setOrganization('Mediatrix Telecom, Inc.')
corNetDebugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 110, 1))
corNetDebugConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 110, 2))
corNetDebugToMSecTraceLevel = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 110, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 10, 20, 30, 40, 50, 1000))).clone(namedValues=NamedValues(("disabled", 0), ("error", 10), ("warning", 20), ("highPriorityInfo", 30), ("mediumPriorityInfo", 40), ("lowPriorityInfo", 50), ("all", 1000))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: corNetDebugToMSecTraceLevel.setStatus('current')
corNetDebugCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 1))
corNetDebugBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 1, 5)).setObjects(("MX-CORNET-DEBUG-MIB", "corNetDebugGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    corNetDebugBasicComplVer1 = corNetDebugBasicComplVer1.setStatus('current')
corNetDebugGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 2))
corNetDebugGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 2, 5)).setObjects(("MX-CORNET-DEBUG-MIB", "corNetDebugToMSecTraceLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    corNetDebugGroupVer1 = corNetDebugGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-CORNET-DEBUG-MIB", corNetDebugMIBObjects=corNetDebugMIBObjects, corNetDebugGroupVer1=corNetDebugGroupVer1, corNetDebugMIB=corNetDebugMIB, corNetDebugCompliances=corNetDebugCompliances, corNetDebugBasicComplVer1=corNetDebugBasicComplVer1, corNetDebugGroups=corNetDebugGroups, corNetDebugConformance=corNetDebugConformance, PYSNMP_MODULE_ID=corNetDebugMIB, corNetDebugToMSecTraceLevel=corNetDebugToMSecTraceLevel)
