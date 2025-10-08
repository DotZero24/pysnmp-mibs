#
# PySNMP MIB module ARISTA-XCVR-DWDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arista/ARISTA-XCVR-DWDM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
aristaXcvrDwdmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 19))
aristaXcvrDwdmMIB.setRevisions(('2018-08-27 00:00', '2018-05-16 00:00', '2016-03-11 00:00',))
if mibBuilder.loadTexts: aristaXcvrDwdmMIB.setLastUpdated('201808270000Z')
if mibBuilder.loadTexts: aristaXcvrDwdmMIB.setOrganization('Arista Networks, Inc.')
class AristaDwdmGridSpacing(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(6250, 6250), ValueRangeConstraint(12500, 12500), ValueRangeConstraint(25000, 25000), ValueRangeConstraint(50000, 50000), ValueRangeConstraint(100000, 100000), )
class AristaModulationFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 0), ("none", 1), ("qpsk", 2), ("eightQam", 3), ("sixteenQam", 4))

aristaXcvrDwdmTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1), )
if mibBuilder.loadTexts: aristaXcvrDwdmTable.setStatus('current')
aristaXcvrDwdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: aristaXcvrDwdmEntry.setStatus('current')
aristaXcvrDwdmOperChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmOperChannel.setStatus('current')
aristaXcvrDwdmOperGrid = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 2), AristaDwdmGridSpacing()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmOperGrid.setStatus('current')
aristaXcvrDwdmOperFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmOperFrequency.setStatus('current')
aristaXcvrDwdmAdminChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aristaXcvrDwdmAdminChannel.setStatus('current')
aristaXcvrDwdmAdminGrid = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 7), AristaDwdmGridSpacing()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aristaXcvrDwdmAdminGrid.setStatus('current')
aristaXcvrDwdmTunable = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmTunable.setStatus('current')
aristaXcvrDwdmModulationFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 9), AristaModulationFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmModulationFormat.setStatus('current')
aristaXcvrDwdmAdminFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aristaXcvrDwdmAdminFrequency.setStatus('current')
aristaXcvrDwdmUncorrectedCodewords = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaXcvrDwdmUncorrectedCodewords.setStatus('current')
aristaXcvrDwdmMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 19, 2))
aristaXcvrDwdmMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 1))
aristaXcvrDwdmMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 2))
aristaXcvrDwdmMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 1, 1)).setObjects(("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaXcvrDwdmMibCompliance = aristaXcvrDwdmMibCompliance.setStatus('current')
aristaXcvrDwdmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 2, 1)).setObjects(("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperChannel"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperGrid"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperFrequency"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminChannel"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminGrid"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmTunable"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmModulationFormat"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminFrequency"), ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmUncorrectedCodewords"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaXcvrDwdmGroup = aristaXcvrDwdmGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-XCVR-DWDM-MIB", aristaXcvrDwdmAdminFrequency=aristaXcvrDwdmAdminFrequency, aristaXcvrDwdmOperGrid=aristaXcvrDwdmOperGrid, aristaXcvrDwdmModulationFormat=aristaXcvrDwdmModulationFormat, aristaXcvrDwdmMIB=aristaXcvrDwdmMIB, PYSNMP_MODULE_ID=aristaXcvrDwdmMIB, aristaXcvrDwdmUncorrectedCodewords=aristaXcvrDwdmUncorrectedCodewords, aristaXcvrDwdmTable=aristaXcvrDwdmTable, aristaXcvrDwdmMibConformance=aristaXcvrDwdmMibConformance, aristaXcvrDwdmGroup=aristaXcvrDwdmGroup, aristaXcvrDwdmAdminGrid=aristaXcvrDwdmAdminGrid, aristaXcvrDwdmOperFrequency=aristaXcvrDwdmOperFrequency, aristaXcvrDwdmEntry=aristaXcvrDwdmEntry, aristaXcvrDwdmTunable=aristaXcvrDwdmTunable, aristaXcvrDwdmAdminChannel=aristaXcvrDwdmAdminChannel, aristaXcvrDwdmMibGroups=aristaXcvrDwdmMibGroups, aristaXcvrDwdmMibCompliances=aristaXcvrDwdmMibCompliances, AristaModulationFormat=AristaModulationFormat, AristaDwdmGridSpacing=AristaDwdmGridSpacing, aristaXcvrDwdmOperChannel=aristaXcvrDwdmOperChannel, aristaXcvrDwdmMibCompliance=aristaXcvrDwdmMibCompliance)
