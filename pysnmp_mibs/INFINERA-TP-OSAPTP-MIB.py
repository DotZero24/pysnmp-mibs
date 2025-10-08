#
# PySNMP MIB module INFINERA-TP-OSAPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OSAPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnServiceType, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnServiceType", "FloatTenths")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-OSAPTP-MIB", osaPtpGroup=osaPtpGroup, osaPtpGroups=osaPtpGroups, osaPtpMIB=osaPtpMIB, osaPtpConformance=osaPtpConformance, osaPtpTable=osaPtpTable, osaPtpPmHistStatsEnable=osaPtpPmHistStatsEnable, osaPtpCompliances=osaPtpCompliances, PYSNMP_MODULE_ID=osaPtpMIB, osaPtpEntry=osaPtpEntry, osaPtpCompliance=osaPtpCompliance)
