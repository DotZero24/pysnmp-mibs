#
# PySNMP MIB module MX-SIP-DEBUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SIP-DEBUG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:03 2025
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
sipDebugMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 23))
sipDebugMIB.setRevisions(('1903-11-13 00:00',))
if mibBuilder.loadTexts: sipDebugMIB.setLastUpdated('0311130000Z')
if mibBuilder.loadTexts: sipDebugMIB.setOrganization('Mediatrix Telecom, Inc.')
sipDebugMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 23, 1))
sipDebugConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 23, 2))
sipDebugContextSnapshotTime = MibScalar((1, 3, 6, 1, 4, 1, 4935, 99, 23, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10080))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sipDebugContextSnapshotTime.setStatus('current')
sipDebugCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 1))
sipDebugBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 1, 1)).setObjects(("MX-SIP-DEBUG-MIB", "sipDebugGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipDebugBasicComplVer1 = sipDebugBasicComplVer1.setStatus('current')
sipDebugGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 2))
sipDebugGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 23, 2, 2, 5)).setObjects(("MX-SIP-DEBUG-MIB", "sipDebugContextSnapshotTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sipDebugGroupVer1 = sipDebugGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-SIP-DEBUG-MIB", sipDebugConformance=sipDebugConformance, sipDebugBasicComplVer1=sipDebugBasicComplVer1, sipDebugGroupVer1=sipDebugGroupVer1, sipDebugMIB=sipDebugMIB, sipDebugCompliances=sipDebugCompliances, sipDebugMIBObjects=sipDebugMIBObjects, PYSNMP_MODULE_ID=sipDebugMIB, sipDebugGroups=sipDebugGroups, sipDebugContextSnapshotTime=sipDebugContextSnapshotTime)
