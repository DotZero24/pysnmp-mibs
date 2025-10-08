#
# PySNMP MIB module INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:01 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
terminationPoint, = mibBuilder.importSymbols("INFINERA-REG-MIB", "terminationPoint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-PXMSTATICUNICASTFDB-MIB", pxmStaticUnicastFdbMIB=pxmStaticUnicastFdbMIB, pxmStaticUnicastFdbTable=pxmStaticUnicastFdbTable, pxmStaticUnicastFdbGroups=pxmStaticUnicastFdbGroups, pxmStaticUnicastFdbConformance=pxmStaticUnicastFdbConformance, PYSNMP_MODULE_ID=pxmStaticUnicastFdbMIB, pxmStaticUnicastFdbCompliance=pxmStaticUnicastFdbCompliance, pxmStaticUnicastFdbEntry=pxmStaticUnicastFdbEntry, pxmStaticUnicastFdbCompliances=pxmStaticUnicastFdbCompliances, pxmStaticUnicastFdbGroup=pxmStaticUnicastFdbGroup, pxmStaticUnicastFdbMacAddress=pxmStaticUnicastFdbMacAddress)
