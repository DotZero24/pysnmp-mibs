#
# PySNMP MIB module HP-ICF-RELOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-RELOAD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpicfBasic, = mibBuilder.importSymbols("HP-ICF-BASIC", "hpicfBasic")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
hpicfReloadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20))
hpicfReloadMIB.setRevisions(('2009-12-03 00:00', '2009-10-01 00:00',))
if mibBuilder.loadTexts: hpicfReloadMIB.setLastUpdated('200912030000Z')
if mibBuilder.loadTexts: hpicfReloadMIB.setOrganization('HP Networking')
hpicfReloadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1))
hpicfEntityReload = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2))
hpicfReloadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3))
class ReloadControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("reloadSlotNone", 1), ("fullPowerCycleReload", 2))

hpicfReloadState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notScheduled", 1), ("reloadAfter", 2), ("reloadAt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadState.setStatus('current')
hpicfReloadAfter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAfter.setStatus('current')
hpicfReloadAt = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 3), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadAt.setStatus('current')
hpicfReloadTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2), )
if mibBuilder.loadTexts: hpicfReloadTable.setStatus('current')
hpicfReloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfReloadEntry.setStatus('current')
hpicfReloadControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 1), ReloadControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfReloadControl.setStatus('current')
hpicfReloadDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfReloadDateTime.setStatus('current')
hpicfReloadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1))
hpicfReloadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2))
hpicfReloadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadState"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAfter"), ("HP-ICF-RELOAD-MIB", "hpicfReloadAt"), ("HP-ICF-RELOAD-MIB", "hpicfReloadControl"), ("HP-ICF-RELOAD-MIB", "hpicfReloadDateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadGroup = hpicfReloadGroup.setStatus('current')
hpicfReloadFullCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 1)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance1 = hpicfReloadFullCompliance1.setStatus('current')
hpicfReloadFullCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 2)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadFullCompliance2 = hpicfReloadFullCompliance2.setStatus('current')
hpicfReloadReadOnlyCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 3)).setObjects(("HP-ICF-RELOAD-MIB", "hpicfReloadGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfReloadReadOnlyCompliance1 = hpicfReloadReadOnlyCompliance1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-RELOAD-MIB", hpicfReloadCompliances=hpicfReloadCompliances, hpicfReloadFullCompliance2=hpicfReloadFullCompliance2, hpicfReloadGroup=hpicfReloadGroup, hpicfReloadConformance=hpicfReloadConformance, PYSNMP_MODULE_ID=hpicfReloadMIB, hpicfReloadMIB=hpicfReloadMIB, hpicfReloadControl=hpicfReloadControl, hpicfReloadAt=hpicfReloadAt, hpicfReloadAfter=hpicfReloadAfter, hpicfEntityReload=hpicfEntityReload, hpicfReloadTable=hpicfReloadTable, hpicfReloadDateTime=hpicfReloadDateTime, hpicfReloadGroups=hpicfReloadGroups, hpicfReloadEntry=hpicfReloadEntry, hpicfReloadReadOnlyCompliance1=hpicfReloadReadOnlyCompliance1, hpicfReloadState=hpicfReloadState, hpicfReloadFullCompliance1=hpicfReloadFullCompliance1, hpicfReloadObjects=hpicfReloadObjects, ReloadControl=ReloadControl)
