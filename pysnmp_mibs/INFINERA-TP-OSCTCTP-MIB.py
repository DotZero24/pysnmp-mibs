#
# PySNMP MIB module INFINERA-TP-OSCTCTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OSCTCTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
osctCtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11))
osctCtpMIB.setRevisions(('2009-03-25 00:00',))
if mibBuilder.loadTexts: osctCtpMIB.setLastUpdated('200903250000Z')
if mibBuilder.loadTexts: osctCtpMIB.setOrganization('Infinera')
osctCtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3))
osctCtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 1))
osctCtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 2))
osctCtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1), )
if mibBuilder.loadTexts: osctCtpTable.setStatus('current')
osctCtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: osctCtpEntry.setStatus('current')
osctCtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osctCtpPmHistStatsEnable.setStatus('current')
osctCtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 2, 1)).setObjects(("INFINERA-TP-OSCTCTP-MIB", "osctCtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osctCtpGroup = osctCtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-OSCTCTP-MIB", osctCtpCompliances=osctCtpCompliances, osctCtpEntry=osctCtpEntry, osctCtpConformance=osctCtpConformance, osctCtpTable=osctCtpTable, osctCtpPmHistStatsEnable=osctCtpPmHistStatsEnable, PYSNMP_MODULE_ID=osctCtpMIB, osctCtpGroups=osctCtpGroups, osctCtpMIB=osctCtpMIB, osctCtpGroup=osctCtpGroup)
