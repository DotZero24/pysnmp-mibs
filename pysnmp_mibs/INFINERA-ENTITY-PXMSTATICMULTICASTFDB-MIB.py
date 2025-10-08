#
# PySNMP MIB module INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:37 2025
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
pxmStaticMulticastFdbMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67))
if mibBuilder.loadTexts: pxmStaticMulticastFdbMIB.setLastUpdated('201605200000Z')
if mibBuilder.loadTexts: pxmStaticMulticastFdbMIB.setOrganization('INFINERA')
pxmStaticMulticastFdbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 3))
pxmStaticMulticastFdbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 3, 1))
pxmStaticMulticastFdbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 3, 2))
pxmStaticMulticastFdbTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 1), )
if mibBuilder.loadTexts: pxmStaticMulticastFdbTable.setStatus('current')
pxmStaticMulticastFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pxmStaticMulticastFdbEntry.setStatus('current')
pxmStaticMulticastFdbMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pxmStaticMulticastFdbMacAddress.setStatus('current')
pxmStaticMulticastFdbCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 3, 1, 1)).setObjects(("INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB", "pxmStaticMulticastFdbGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmStaticMulticastFdbCompliance = pxmStaticMulticastFdbCompliance.setStatus('current')
pxmStaticMulticastFdbGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 67, 3, 2, 1)).setObjects(("INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB", "pxmStaticMulticastFdbMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pxmStaticMulticastFdbGroup = pxmStaticMulticastFdbGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB", pxmStaticMulticastFdbConformance=pxmStaticMulticastFdbConformance, pxmStaticMulticastFdbMacAddress=pxmStaticMulticastFdbMacAddress, pxmStaticMulticastFdbEntry=pxmStaticMulticastFdbEntry, pxmStaticMulticastFdbTable=pxmStaticMulticastFdbTable, PYSNMP_MODULE_ID=pxmStaticMulticastFdbMIB, pxmStaticMulticastFdbCompliance=pxmStaticMulticastFdbCompliance, pxmStaticMulticastFdbGroup=pxmStaticMulticastFdbGroup, pxmStaticMulticastFdbCompliances=pxmStaticMulticastFdbCompliances, pxmStaticMulticastFdbMIB=pxmStaticMulticastFdbMIB, pxmStaticMulticastFdbGroups=pxmStaticMulticastFdbGroups)
