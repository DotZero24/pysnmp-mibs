#
# PySNMP MIB module INFINERA-TP-DSEPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-DSEPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:41 2025
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
mibBuilder.exportSymbols("INFINERA-TP-DSEPTP-MIB", dsePtpConformance=dsePtpConformance, dsePtpCompliance=dsePtpCompliance, dsePtpGroup=dsePtpGroup, dsePtpCompliances=dsePtpCompliances, dsePtpEntry=dsePtpEntry, dsePtpTable=dsePtpTable, dsePtpPmHistStatsEnable=dsePtpPmHistStatsEnable, PYSNMP_MODULE_ID=dsePtpMIB, dsePtpProvisionedRemoteTP=dsePtpProvisionedRemoteTP, dsePtpGroups=dsePtpGroups, dsePtpMIB=dsePtpMIB)
