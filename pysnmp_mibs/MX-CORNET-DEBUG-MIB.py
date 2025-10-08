#
# PySNMP MIB module MX-CORNET-DEBUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-CORNET-DEBUG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-CORNET-DEBUG-MIB", corNetDebugGroupVer1=corNetDebugGroupVer1, corNetDebugBasicComplVer1=corNetDebugBasicComplVer1, corNetDebugConformance=corNetDebugConformance, corNetDebugCompliances=corNetDebugCompliances, corNetDebugMIB=corNetDebugMIB, corNetDebugMIBObjects=corNetDebugMIBObjects, corNetDebugGroups=corNetDebugGroups, PYSNMP_MODULE_ID=corNetDebugMIB, corNetDebugToMSecTraceLevel=corNetDebugToMSecTraceLevel)
