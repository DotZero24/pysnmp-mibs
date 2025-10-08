#
# PySNMP MIB module MX-SIP-DEBUG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-SIP-DEBUG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:29 2025
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
mibBuilder.exportSymbols("MX-SIP-DEBUG-MIB", sipDebugMIB=sipDebugMIB, sipDebugGroups=sipDebugGroups, sipDebugGroupVer1=sipDebugGroupVer1, sipDebugConformance=sipDebugConformance, sipDebugContextSnapshotTime=sipDebugContextSnapshotTime, sipDebugMIBObjects=sipDebugMIBObjects, sipDebugCompliances=sipDebugCompliances, sipDebugBasicComplVer1=sipDebugBasicComplVer1, PYSNMP_MODULE_ID=sipDebugMIB)
