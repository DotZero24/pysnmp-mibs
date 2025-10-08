#
# PySNMP MIB module INFINERA-TP-OSAPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OSAPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnServiceType, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnServiceType", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
osaPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21))
osaPtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: osaPtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: osaPtpMIB.setOrganization('Infinera')
osaPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3))
osaPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 1))
osaPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 2))
osaPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1), )
if mibBuilder.loadTexts: osaPtpTable.setStatus('current')
osaPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: osaPtpEntry.setStatus('current')
osaPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: osaPtpPmHistStatsEnable.setStatus('current')
osaPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 1, 1)).setObjects(("INFINERA-TP-OSAPTP-MIB", "osaPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpCompliance = osaPtpCompliance.setStatus('current')
osaPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 2, 1)).setObjects(("INFINERA-TP-OSAPTP-MIB", "osaPtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    osaPtpGroup = osaPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-OSAPTP-MIB", osaPtpPmHistStatsEnable=osaPtpPmHistStatsEnable, osaPtpTable=osaPtpTable, osaPtpCompliance=osaPtpCompliance, PYSNMP_MODULE_ID=osaPtpMIB, osaPtpEntry=osaPtpEntry, osaPtpGroup=osaPtpGroup, osaPtpCompliances=osaPtpCompliances, osaPtpGroups=osaPtpGroups, osaPtpConformance=osaPtpConformance, osaPtpMIB=osaPtpMIB)
