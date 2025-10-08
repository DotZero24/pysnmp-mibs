#
# PySNMP MIB module HP-ICF-RELOAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-ICF-RELOAD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpicfBasic, = mibBuilder.importSymbols("HP-ICF-BASIC", "hpicfBasic")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HP-ICF-RELOAD-MIB", hpicfReloadFullCompliance2=hpicfReloadFullCompliance2, hpicfReloadAfter=hpicfReloadAfter, hpicfReloadFullCompliance1=hpicfReloadFullCompliance1, hpicfReloadObjects=hpicfReloadObjects, hpicfReloadCompliances=hpicfReloadCompliances, hpicfReloadControl=hpicfReloadControl, hpicfReloadAt=hpicfReloadAt, hpicfReloadGroups=hpicfReloadGroups, hpicfEntityReload=hpicfEntityReload, hpicfReloadDateTime=hpicfReloadDateTime, PYSNMP_MODULE_ID=hpicfReloadMIB, ReloadControl=ReloadControl, hpicfReloadReadOnlyCompliance1=hpicfReloadReadOnlyCompliance1, hpicfReloadEntry=hpicfReloadEntry, hpicfReloadConformance=hpicfReloadConformance, hpicfReloadGroup=hpicfReloadGroup, hpicfReloadTable=hpicfReloadTable, hpicfReloadMIB=hpicfReloadMIB, hpicfReloadState=hpicfReloadState)
