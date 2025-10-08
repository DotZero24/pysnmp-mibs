#
# PySNMP MIB module INFINERA-TP-LMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-LMM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lmmPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55))
lmmPtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: lmmPtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: lmmPtpMIB.setOrganization('Infinera')
lmmPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1), )
if mibBuilder.loadTexts: lmmPtpTable.setStatus('current')
lmmPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: lmmPtpEntry.setStatus('current')
lmmPtpRxProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lmmPtpRxProvNbrTP.setStatus('current')
lmmPtpTxProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lmmPtpTxProvNbrTP.setStatus('current')
lmmPtpProvisionedOpenWaveRemoteTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lmmPtpProvisionedOpenWaveRemoteTP.setStatus('current')
lmmPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3))
lmmPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 1))
lmmPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 2))
lmmPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 1, 1)).setObjects(("INFINERA-TP-LMM-MIB", "lmmPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lmmPtpCompliance = lmmPtpCompliance.setStatus('current')
lmmPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 2, 1)).setObjects(("INFINERA-TP-LMM-MIB", "lmmPtpRxProvNbrTP"), ("INFINERA-TP-LMM-MIB", "lmmPtpTxProvNbrTP"), ("INFINERA-TP-LMM-MIB", "lmmPtpProvisionedOpenWaveRemoteTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lmmPtpGroup = lmmPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-LMM-MIB", lmmPtpMIB=lmmPtpMIB, lmmPtpCompliances=lmmPtpCompliances, lmmPtpRxProvNbrTP=lmmPtpRxProvNbrTP, lmmPtpTable=lmmPtpTable, PYSNMP_MODULE_ID=lmmPtpMIB, lmmPtpGroup=lmmPtpGroup, lmmPtpCompliance=lmmPtpCompliance, lmmPtpTxProvNbrTP=lmmPtpTxProvNbrTP, lmmPtpConformance=lmmPtpConformance, lmmPtpEntry=lmmPtpEntry, lmmPtpProvisionedOpenWaveRemoteTP=lmmPtpProvisionedOpenWaveRemoteTP, lmmPtpGroups=lmmPtpGroups)
