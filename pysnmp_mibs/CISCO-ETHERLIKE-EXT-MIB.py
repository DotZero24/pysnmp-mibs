#
# PySNMP MIB module CISCO-ETHERLIKE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-ETHERLIKE-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
dot3StatsIndex, = mibBuilder.importSymbols("EtherLike-MIB", "dot3StatsIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 645))
ciscoEtherExtMIB.setRevisions(('2010-06-04 00:00', '2008-10-15 00:00', '2008-01-09 00:00',))
if mibBuilder.loadTexts: ciscoEtherExtMIB.setLastUpdated('201006040000Z')
if mibBuilder.loadTexts: ciscoEtherExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoEtherExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 0))
ciscoEtherExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1))
ciscoEtherExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2))
ceeDot3PauseExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1))
ceeSubIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2))
ceeDot3PauseExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1), )
if mibBuilder.loadTexts: ceeDot3PauseExtTable.setStatus('current')
ceeDot3PauseExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1), ).setIndexNames((0, "EtherLike-MIB", "dot3StatsIndex"))
if mibBuilder.loadTexts: ceeDot3PauseExtEntry.setStatus('current')
ceeDot3PauseExtAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("txDesired", 0), ("rxDesired", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceeDot3PauseExtAdminMode.setStatus('current')
ceeDot3PauseExtOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("txDisagree", 0), ("rxDisagree", 1), ("txDesired", 2), ("rxDesired", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeDot3PauseExtOperMode.setStatus('current')
ceeSubInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1), )
if mibBuilder.loadTexts: ceeSubInterfaceTable.setStatus('current')
ceeSubInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ceeSubInterfaceEntry.setStatus('current')
ceeSubInterfaceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('subifs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ceeSubInterfaceCount.setStatus('current')
ceeEtherExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1))
ceeEtherExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2))
ceeEtherExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBCompliance = ceeEtherExtMIBCompliance.setStatus('deprecated')
ceeEtherExtMIBComplianceR01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtPauseGroup"), ("CISCO-ETHERLIKE-EXT-MIB", "ciscoEtherExtSubIfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceeEtherExtMIBComplianceR01 = ceeEtherExtMIBComplianceR01.setStatus('current')
ciscoEtherExtPauseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 1)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtAdminMode"), ("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtPauseGroup = ciscoEtherExtPauseGroup.setStatus('current')
ciscoEtherExtSubIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 2)).setObjects(("CISCO-ETHERLIKE-EXT-MIB", "ceeSubInterfaceCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherExtSubIfGroup = ciscoEtherExtSubIfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHERLIKE-EXT-MIB", ciscoEtherExtPauseGroup=ciscoEtherExtPauseGroup, ciscoEtherExtMIBConform=ciscoEtherExtMIBConform, ceeEtherExtMIBGroups=ceeEtherExtMIBGroups, ciscoEtherExtMIBObjects=ciscoEtherExtMIBObjects, ciscoEtherExtSubIfGroup=ciscoEtherExtSubIfGroup, ceeDot3PauseExt=ceeDot3PauseExt, ceeDot3PauseExtTable=ceeDot3PauseExtTable, ceeDot3PauseExtEntry=ceeDot3PauseExtEntry, ceeSubInterfaceTable=ceeSubInterfaceTable, ceeEtherExtMIBCompliances=ceeEtherExtMIBCompliances, ceeEtherExtMIBComplianceR01=ceeEtherExtMIBComplianceR01, ceeSubIf=ceeSubIf, ceeDot3PauseExtAdminMode=ceeDot3PauseExtAdminMode, ceeDot3PauseExtOperMode=ceeDot3PauseExtOperMode, ceeSubInterfaceEntry=ceeSubInterfaceEntry, ceeSubInterfaceCount=ceeSubInterfaceCount, PYSNMP_MODULE_ID=ciscoEtherExtMIB, ciscoEtherExtMIB=ciscoEtherExtMIB, ceeEtherExtMIBCompliance=ceeEtherExtMIBCompliance, ciscoEtherExtMIBNotifs=ciscoEtherExtMIBNotifs)
