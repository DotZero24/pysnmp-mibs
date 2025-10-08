#
# PySNMP MIB module INFINERA-TP-CMMOCGPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-CMMOCGPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:42 2025
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
cmmOcgPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28))
cmmOcgPtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: cmmOcgPtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: cmmOcgPtpMIB.setOrganization('Infinera')
cmmOcgPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1), )
if mibBuilder.loadTexts: cmmOcgPtpTable.setStatus('current')
cmmOcgPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmmOcgPtpEntry.setStatus('current')
cmmOcgPtpDiscoveredRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmOcgPtpDiscoveredRemoteTP.setStatus('current')
cmmOcgPtpAutoDiscoveryState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("inProgress", 1), ("completed", 2), ("unknown", 3), ("notValidOrShutdown", 4), ("failed", 5))).clone('notValidOrShutdown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmOcgPtpAutoDiscoveryState.setStatus('current')
cmmOcgPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmOcgPtpPmHistStatsEnable.setStatus('current')
cmmOcgPtpOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gen1", 1), ("gen2", 2))).clone('gen2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmmOcgPtpOperatingMode.setStatus('current')
cmmOcgPtpOcgPowerControlLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmmOcgPtpOcgPowerControlLoop.setStatus('current')
cmmOcgPtpProvisionedOcgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmmOcgPtpProvisionedOcgNumber.setStatus('current')
cmmOcgPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3))
cmmOcgPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 1))
cmmOcgPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 2))
cmmOcgPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 1, 1)).setObjects(("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmOcgPtpCompliance = cmmOcgPtpCompliance.setStatus('current')
cmmOcgPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 28, 3, 2, 1)).setObjects(("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpDiscoveredRemoteTP"), ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpAutoDiscoveryState"), ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpPmHistStatsEnable"), ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpOcgPowerControlLoop"), ("INFINERA-TP-CMMOCGPTP-MIB", "cmmOcgPtpProvisionedOcgNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmmOcgPtpGroup = cmmOcgPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-CMMOCGPTP-MIB", cmmOcgPtpProvisionedOcgNumber=cmmOcgPtpProvisionedOcgNumber, cmmOcgPtpEntry=cmmOcgPtpEntry, cmmOcgPtpPmHistStatsEnable=cmmOcgPtpPmHistStatsEnable, cmmOcgPtpDiscoveredRemoteTP=cmmOcgPtpDiscoveredRemoteTP, PYSNMP_MODULE_ID=cmmOcgPtpMIB, cmmOcgPtpTable=cmmOcgPtpTable, cmmOcgPtpCompliances=cmmOcgPtpCompliances, cmmOcgPtpGroup=cmmOcgPtpGroup, cmmOcgPtpConformance=cmmOcgPtpConformance, cmmOcgPtpOperatingMode=cmmOcgPtpOperatingMode, cmmOcgPtpGroups=cmmOcgPtpGroups, cmmOcgPtpCompliance=cmmOcgPtpCompliance, cmmOcgPtpOcgPowerControlLoop=cmmOcgPtpOcgPowerControlLoop, cmmOcgPtpAutoDiscoveryState=cmmOcgPtpAutoDiscoveryState, cmmOcgPtpMIB=cmmOcgPtpMIB)
