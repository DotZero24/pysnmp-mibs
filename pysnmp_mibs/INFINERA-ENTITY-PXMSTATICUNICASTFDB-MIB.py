#
# PySNMP MIB module INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pxmStaticUnicastFdbMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65))
if mibBuilder.loadTexts: pxmStaticUnicastFdbMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: pxmStaticUnicastFdbMIB.setOrganization('INFINERA')
pxmStaticUnicastFdbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3))
pxmStaticUnicastFdbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 1))
pxmStaticUnicastFdbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 2))
pxmStaticUnicastFdbTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1), )
if mibBuilder.loadTexts: pxmStaticUnicastFdbTable.setStatus('current')
pxmStaticUnicastFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pxmStaticUnicastFdbEntry.setStatus('current')
pxmStaticUnicastFdbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmStaticUnicastFdbMacAddress.setStatus('current')
pxmStaticUnicastFdbCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 1, 1)).setObjects(("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", "pxmStaticUnicastFdbGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmStaticUnicastFdbCompliance = pxmStaticUnicastFdbCompliance.setStatus('current')
pxmStaticUnicastFdbGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 65, 3, 2, 1)).setObjects(("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", "pxmStaticUnicastFdbMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmStaticUnicastFdbGroup = pxmStaticUnicastFdbGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", pxmStaticUnicastFdbGroups=pxmStaticUnicastFdbGroups, pxmStaticUnicastFdbEntry=pxmStaticUnicastFdbEntry, pxmStaticUnicastFdbMIB=pxmStaticUnicastFdbMIB, pxmStaticUnicastFdbGroup=pxmStaticUnicastFdbGroup, PYSNMP_MODULE_ID=pxmStaticUnicastFdbMIB, pxmStaticUnicastFdbConformance=pxmStaticUnicastFdbConformance, pxmStaticUnicastFdbCompliance=pxmStaticUnicastFdbCompliance, pxmStaticUnicastFdbMacAddress=pxmStaticUnicastFdbMacAddress, pxmStaticUnicastFdbCompliances=pxmStaticUnicastFdbCompliances, pxmStaticUnicastFdbTable=pxmStaticUnicastFdbTable)
