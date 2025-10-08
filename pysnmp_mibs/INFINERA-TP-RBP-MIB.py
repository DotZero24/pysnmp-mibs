#
# PySNMP MIB module INFINERA-TP-RBP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-RBP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:32 2025
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
rbpPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54))
rbpPtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: rbpPtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: rbpPtpMIB.setOrganization('Infinera')
rbpPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1), )
if mibBuilder.loadTexts: rbpPtpTable.setStatus('current')
rbpPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rbpPtpEntry.setStatus('current')
rbpPtpProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rbpPtpProvNbrTP.setStatus('current')
rbpPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3))
rbpPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 1))
rbpPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 2))
rbpPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 1, 1)).setObjects(("INFINERA-TP-RBP-MIB", "rbpPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbpPtpCompliance = rbpPtpCompliance.setStatus('current')
rbpPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 54, 3, 2, 1)).setObjects(("INFINERA-TP-RBP-MIB", "rbpPtpProvNbrTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbpPtpGroup = rbpPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-RBP-MIB", rbpPtpEntry=rbpPtpEntry, rbpPtpCompliances=rbpPtpCompliances, PYSNMP_MODULE_ID=rbpPtpMIB, rbpPtpProvNbrTP=rbpPtpProvNbrTP, rbpPtpGroups=rbpPtpGroups, rbpPtpCompliance=rbpPtpCompliance, rbpPtpConformance=rbpPtpConformance, rbpPtpGroup=rbpPtpGroup, rbpPtpTable=rbpPtpTable, rbpPtpMIB=rbpPtpMIB)
