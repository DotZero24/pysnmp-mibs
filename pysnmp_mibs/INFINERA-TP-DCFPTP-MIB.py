#
# PySNMP MIB module INFINERA-TP-DCFPTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-DCFPTP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnDcmType, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnDcmType", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dcfPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5))
dcfPtpMIB.setRevisions(('2008-10-20 00:00',))
if mibBuilder.loadTexts: dcfPtpMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: dcfPtpMIB.setOrganization('Infinera')
dcfPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: dcfPtpTable.setStatus('current')
dcfPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dcfPtpEntry.setStatus('current')
dcfPtpDcmType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 1), InfnDcmType().clone('unspecified')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcfPtpDcmType.setStatus('current')
dcfPtpExpectedDcfLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 2), FloatTenths()).setUnits('0.1 dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: dcfPtpExpectedDcfLoss.setStatus('current')
dcfPtpExpectedDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 3), Integer32()).setUnits('100 ps/nm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dcfPtpExpectedDispersion.setStatus('current')
dcfPtpDcfLossReporting = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcfPtpDcfLossReporting.setStatus('current')
dcfPtpPmHistStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcfPtpPmHistStatsEnable.setStatus('current')
dcfPtpProvisionedRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcfPtpProvisionedRemoteTP.setStatus('current')
dcfPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3))
dcfPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 1))
dcfPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 2))
dcfPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 1, 1)).setObjects(("INFINERA-TP-DCFPTP-MIB", "dcfPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcfPtpCompliance = dcfPtpCompliance.setStatus('current')
dcfPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 2, 1)).setObjects(("INFINERA-TP-DCFPTP-MIB", "dcfPtpDcmType"), ("INFINERA-TP-DCFPTP-MIB", "dcfPtpExpectedDcfLoss"), ("INFINERA-TP-DCFPTP-MIB", "dcfPtpExpectedDispersion"), ("INFINERA-TP-DCFPTP-MIB", "dcfPtpDcfLossReporting"), ("INFINERA-TP-DCFPTP-MIB", "dcfPtpPmHistStatsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dcfPtpGroup = dcfPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-DCFPTP-MIB", dcfPtpCompliance=dcfPtpCompliance, dcfPtpCompliances=dcfPtpCompliances, dcfPtpConformance=dcfPtpConformance, PYSNMP_MODULE_ID=dcfPtpMIB, dcfPtpDcmType=dcfPtpDcmType, dcfPtpExpectedDispersion=dcfPtpExpectedDispersion, dcfPtpProvisionedRemoteTP=dcfPtpProvisionedRemoteTP, dcfPtpEntry=dcfPtpEntry, dcfPtpPmHistStatsEnable=dcfPtpPmHistStatsEnable, dcfPtpMIB=dcfPtpMIB, dcfPtpGroups=dcfPtpGroups, dcfPtpGroup=dcfPtpGroup, dcfPtpExpectedDcfLoss=dcfPtpExpectedDcfLoss, dcfPtpTable=dcfPtpTable, dcfPtpDcfLossReporting=dcfPtpDcfLossReporting)
