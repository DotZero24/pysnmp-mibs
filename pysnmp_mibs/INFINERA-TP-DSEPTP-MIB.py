#
# PySNMP MIB module INFINERA-TP-DSEPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-DSEPTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:51 2025
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
dsePtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22))
dsePtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: dsePtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: dsePtpMIB.setOrganization('Infinera')
dsePtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3))
dsePtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 1))
dsePtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 2))
dsePtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1), )
if mibBuilder.loadTexts: dsePtpTable.setStatus('current')
dsePtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dsePtpEntry.setStatus('current')
dsePtpProvisionedRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsePtpProvisionedRemoteTP.setStatus('current')
dsePtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsePtpPmHistStatsEnable.setStatus('current')
dsePtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 1, 1)).setObjects(("INFINERA-TP-DSEPTP-MIB", "dsePtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsePtpCompliance = dsePtpCompliance.setStatus('current')
dsePtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 2, 1)).setObjects(("INFINERA-TP-DSEPTP-MIB", "dsePtpProvisionedRemoteTP"), ("INFINERA-TP-DSEPTP-MIB", "dsePtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsePtpGroup = dsePtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-DSEPTP-MIB", dsePtpGroups=dsePtpGroups, dsePtpPmHistStatsEnable=dsePtpPmHistStatsEnable, dsePtpEntry=dsePtpEntry, dsePtpProvisionedRemoteTP=dsePtpProvisionedRemoteTP, dsePtpCompliance=dsePtpCompliance, dsePtpTable=dsePtpTable, dsePtpGroup=dsePtpGroup, dsePtpConformance=dsePtpConformance, PYSNMP_MODULE_ID=dsePtpMIB, dsePtpMIB=dsePtpMIB, dsePtpCompliances=dsePtpCompliances)
