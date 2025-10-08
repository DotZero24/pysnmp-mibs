#
# PySNMP MIB module INFINERA-ENTITY-FSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FSP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fspMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35))
if mibBuilder.loadTexts: fspMIB.setLastUpdated('201310200000Z')
if mibBuilder.loadTexts: fspMIB.setOrganization('INFINERA')
fspConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3))
fspCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 1))
fspGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 2))
fspTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1), )
if mibBuilder.loadTexts: fspTable.setStatus('current')
fspEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: fspEntry.setStatus('current')
fspType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7805, 7806, 7807, 7808))).clone(namedValues=NamedValues(("fspE9D18MPO", 7805), ("fspS4D8MPO", 7806), ("fspC1D1MPO", 7807), ("fmpC8fourLcMPO", 7808)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fspType.setStatus('current')
fspProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fspProvSerialNumber.setStatus('current')
fspLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fspLabel.setStatus('current')
fspAid = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fspAid.setStatus('current')
fspCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FSP-MIB", "fspGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspCompliance = fspCompliance.setStatus('current')
fspGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FSP-MIB", "fspType"), ("INFINERA-ENTITY-FSP-MIB", "fspProvSerialNumber"), ("INFINERA-ENTITY-FSP-MIB", "fspLabel"), ("INFINERA-ENTITY-FSP-MIB", "fspAid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fspGroup = fspGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FSP-MIB", fspEntry=fspEntry, fspGroups=fspGroups, fspMIB=fspMIB, fspLabel=fspLabel, fspConformance=fspConformance, fspAid=fspAid, fspCompliances=fspCompliances, fspCompliance=fspCompliance, fspProvSerialNumber=fspProvSerialNumber, fspType=fspType, fspGroup=fspGroup, PYSNMP_MODULE_ID=fspMIB, fspTable=fspTable)
