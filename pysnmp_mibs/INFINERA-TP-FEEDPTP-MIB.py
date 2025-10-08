#
# PySNMP MIB module INFINERA-TP-FEEDPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-FEEDPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
feedPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52))
feedPtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: feedPtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: feedPtpMIB.setOrganization('Infinera')
feedPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3))
feedPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 1))
feedPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 2))
feedPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1), )
if mibBuilder.loadTexts: feedPtpTable.setStatus('current')
feedPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: feedPtpEntry.setStatus('current')
feedPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: feedPtpPmHistStatsEnable.setStatus('current')
feedPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 1, 1)).setObjects(("INFINERA-TP-FEEDPTP-MIB", "feedPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    feedPtpCompliance = feedPtpCompliance.setStatus('current')
feedPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 2, 1)).setObjects(("INFINERA-TP-FEEDPTP-MIB", "feedPtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    feedPtpGroup = feedPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-FEEDPTP-MIB", feedPtpTable=feedPtpTable, feedPtpGroup=feedPtpGroup, feedPtpCompliance=feedPtpCompliance, feedPtpCompliances=feedPtpCompliances, feedPtpConformance=feedPtpConformance, feedPtpMIB=feedPtpMIB, PYSNMP_MODULE_ID=feedPtpMIB, feedPtpGroups=feedPtpGroups, feedPtpPmHistStatsEnable=feedPtpPmHistStatsEnable, feedPtpEntry=feedPtpEntry)
