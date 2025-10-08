#
# PySNMP MIB module INFINERA-TP-PXMMD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-TP-PXMMD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
InfnSenderIDTLV, InfnMHFCreationCriteria, InfnMDNameFormat = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnSenderIDTLV", "InfnMHFCreationCriteria", "InfnMDNameFormat")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("INFINERA-TP-PXMMD-MIB", mdName=mdName, mdMHFCreationCriteria=mdMHFCreationCriteria, mdEntry=mdEntry, mdLevel=mdLevel, mdMDNameFormat=mdMDNameFormat, mdSenderIDTLV=mdSenderIDTLV, mdCompliances=mdCompliances, mdCompliance=mdCompliance, mdTable=mdTable, PYSNMP_MODULE_ID=mdMIB, mdConformance=mdConformance, mdGroup=mdGroup, mdMIB=mdMIB, mdGroups=mdGroups)
