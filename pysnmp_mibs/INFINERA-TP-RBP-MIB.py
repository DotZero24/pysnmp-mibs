#
# PySNMP MIB module INFINERA-TP-RBP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-RBP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:37 2025
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
mibBuilder.exportSymbols("INFINERA-TP-RBP-MIB", rbpPtpEntry=rbpPtpEntry, rbpPtpTable=rbpPtpTable, rbpPtpProvNbrTP=rbpPtpProvNbrTP, PYSNMP_MODULE_ID=rbpPtpMIB, rbpPtpCompliances=rbpPtpCompliances, rbpPtpMIB=rbpPtpMIB, rbpPtpConformance=rbpPtpConformance, rbpPtpCompliance=rbpPtpCompliance, rbpPtpGroup=rbpPtpGroup, rbpPtpGroups=rbpPtpGroups)
