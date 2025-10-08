#
# PySNMP MIB module INFINERA-TP-BPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-BPP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:24 2025
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
bppPtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66))
bppPtpMIB.setRevisions(('2013-10-20 00:00',))
if mibBuilder.loadTexts: bppPtpMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: bppPtpMIB.setOrganization('Infinera')
bppPtpTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1), )
if mibBuilder.loadTexts: bppPtpTable.setStatus('current')
bppPtpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: bppPtpEntry.setStatus('current')
bppPtpProvNbrTP = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bppPtpProvNbrTP.setStatus('current')
bppPtpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3))
bppPtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 1))
bppPtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 2))
bppPtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 1, 1)).setObjects(("INFINERA-TP-BPP-MIB", "bppPtpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bppPtpCompliance = bppPtpCompliance.setStatus('current')
bppPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 66, 3, 2, 1)).setObjects(("INFINERA-TP-BPP-MIB", "bppPtpProvNbrTP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bppPtpGroup = bppPtpGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-BPP-MIB", bppPtpGroups=bppPtpGroups, bppPtpEntry=bppPtpEntry, PYSNMP_MODULE_ID=bppPtpMIB, bppPtpCompliances=bppPtpCompliances, bppPtpGroup=bppPtpGroup, bppPtpMIB=bppPtpMIB, bppPtpProvNbrTP=bppPtpProvNbrTP, bppPtpConformance=bppPtpConformance, bppPtpCompliance=bppPtpCompliance, bppPtpTable=bppPtpTable)
