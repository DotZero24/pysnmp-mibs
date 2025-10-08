#
# PySNMP MIB module INFINERA-TP-OSCPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-OSCPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:22 2025
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
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
oscPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36))
oscPtpMIB.setRevisions(('2012-10-20 00:00',))
if mibBuilder.loadTexts: oscPtpMIB.setLastUpdated('201210200000Z')
if mibBuilder.loadTexts: oscPtpMIB.setOrganization('Infinera')
oscPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3))
oscPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 1))
oscPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 2))
oscPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1), )
if mibBuilder.loadTexts: oscPtpTable.setStatus('current')
oscPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oscPtpEntry.setStatus('current')
oscPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: oscPtpPmHistStatsEnable.setStatus('current')
oscPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 1, 1)).setObjects(("INFINERA-TP-OSCPTP-MIB", "oscPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpCompliance = oscPtpCompliance.setStatus('current')
oscPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 2, 1)).setObjects(("INFINERA-TP-OSCPTP-MIB", "oscPtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oscPtpGroup = oscPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-OSCPTP-MIB", oscPtpCompliance=oscPtpCompliance, oscPtpCompliances=oscPtpCompliances, oscPtpPmHistStatsEnable=oscPtpPmHistStatsEnable, oscPtpGroups=oscPtpGroups, oscPtpMIB=oscPtpMIB, oscPtpTable=oscPtpTable, PYSNMP_MODULE_ID=oscPtpMIB, oscPtpEntry=oscPtpEntry, oscPtpGroup=oscPtpGroup, oscPtpConformance=oscPtpConformance)
