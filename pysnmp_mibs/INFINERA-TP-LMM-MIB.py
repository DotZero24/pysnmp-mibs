#
# PySNMP MIB module INFINERA-TP-LMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-LMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
FloatHundredths, InfnEnableDisable = mibBuilder.importSymbols("INFINERA-TC-MIB", "FloatHundredths", "InfnEnableDisable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-TP-LMM-MIB", PYSNMP_MODULE_ID=lmmPtpMIB, lmmPtpGroups=lmmPtpGroups, lmmPtpTable=lmmPtpTable, lmmPtpConformance=lmmPtpConformance, lmmPtpCompliances=lmmPtpCompliances, lmmPtpGroup=lmmPtpGroup, lmmPtpMIB=lmmPtpMIB, lmmPtpCompliance=lmmPtpCompliance, lmmPtpTxProvNbrTP=lmmPtpTxProvNbrTP, lmmPtpProvisionedOpenWaveRemoteTP=lmmPtpProvisionedOpenWaveRemoteTP, lmmPtpRxProvNbrTP=lmmPtpRxProvNbrTP, lmmPtpEntry=lmmPtpEntry)
