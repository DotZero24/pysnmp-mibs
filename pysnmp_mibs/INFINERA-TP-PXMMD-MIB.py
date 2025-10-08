#
# PySNMP MIB module INFINERA-TP-PXMMD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMMD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnMDNameFormat, InfnSenderIDTLV, InfnMHFCreationCriteria = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnMDNameFormat", "InfnSenderIDTLV", "InfnMHFCreationCriteria")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78))
if mibBuilder.loadTexts: mdMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: mdMIB.setOrganization('INFINERA')
mdTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1), )
if mibBuilder.loadTexts: mdTable.setStatus('current')
mdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mdEntry.setStatus('current')
mdName = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdName.setStatus('current')
mdLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdLevel.setStatus('current')
mdMDNameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 3), InfnMDNameFormat()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdMDNameFormat.setStatus('current')
mdMHFCreationCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 4), InfnMHFCreationCriteria()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdMHFCreationCriteria.setStatus('current')
mdSenderIDTLV = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 1, 1, 5), InfnSenderIDTLV()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdSenderIDTLV.setStatus('current')
mdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3))
mdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 1))
mdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 2))
mdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 1, 1)).setObjects(("INFINERA-TP-PXMMD-MIB", "mdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdCompliance = mdCompliance.setStatus('current')
mdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 78, 3, 2, 1)).setObjects(("INFINERA-TP-PXMMD-MIB", "mdName"), ("INFINERA-TP-PXMMD-MIB", "mdLevel"), ("INFINERA-TP-PXMMD-MIB", "mdMDNameFormat"), ("INFINERA-TP-PXMMD-MIB", "mdMHFCreationCriteria"), ("INFINERA-TP-PXMMD-MIB", "mdSenderIDTLV"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdGroup = mdGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-TP-PXMMD-MIB", mdCompliances=mdCompliances, mdGroup=mdGroup, mdCompliance=mdCompliance, mdGroups=mdGroups, mdName=mdName, mdMIB=mdMIB, mdMDNameFormat=mdMDNameFormat, mdSenderIDTLV=mdSenderIDTLV, mdLevel=mdLevel, mdEntry=mdEntry, PYSNMP_MODULE_ID=mdMIB, mdTable=mdTable, mdConformance=mdConformance, mdMHFCreationCriteria=mdMHFCreationCriteria)
