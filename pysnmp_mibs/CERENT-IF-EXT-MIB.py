#
# PySNMP MIB module CERENT-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CERENT-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cerentModules, cerentGeneric, cerentRequirements = mibBuilder.importSymbols("CERENT-GLOBAL-REGISTRY", "cerentModules", "cerentGeneric", "cerentRequirements")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
cerentIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3607, 1, 10, 140))
cerentIfExtMIB.setRevisions(('2005-11-14 00:00',))
if mibBuilder.loadTexts: cerentIfExtMIB.setLastUpdated('200511140000Z')
if mibBuilder.loadTexts: cerentIfExtMIB.setOrganization('Cisco Systems, Inc.')
cerentIfExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 2, 100))
cerentIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10), )
if mibBuilder.loadTexts: cerentIfExtTable.setStatus('current')
cerentIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cerentIfExtEntry.setStatus('current')
cerentIfExtPreServiceAlarmSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtPreServiceAlarmSuppression.setStatus('current')
cerentIfExtConfiguredSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20), Integer32().clone(480)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cerentIfExtConfiguredSoakTime.setStatus('current')
cerentIfExtCurrentSoakTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cerentIfExtCurrentSoakTime.setStatus('current')
cerentIfExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90))
cerentIfExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1))
cerentIfExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2))
cerentIfExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtMIBCompliance = cerentIfExtMIBCompliance.setStatus('current')
cerentIfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)).setObjects(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"), ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"), ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cerentIfExtGroup = cerentIfExtGroup.setStatus('current')
mibBuilder.exportSymbols("CERENT-IF-EXT-MIB", cerentIfExtGroup=cerentIfExtGroup, cerentIfExtMIBObjects=cerentIfExtMIBObjects, cerentIfExtMIBGroups=cerentIfExtMIBGroups, cerentIfExtEntry=cerentIfExtEntry, cerentIfExtCurrentSoakTime=cerentIfExtCurrentSoakTime, cerentIfExtMIBCompliance=cerentIfExtMIBCompliance, PYSNMP_MODULE_ID=cerentIfExtMIB, cerentIfExtMIB=cerentIfExtMIB, cerentIfExtMIBCompliances=cerentIfExtMIBCompliances, cerentIfExtConfiguredSoakTime=cerentIfExtConfiguredSoakTime, cerentIfExtMIBConformance=cerentIfExtMIBConformance, cerentIfExtTable=cerentIfExtTable, cerentIfExtPreServiceAlarmSuppression=cerentIfExtPreServiceAlarmSuppression)
