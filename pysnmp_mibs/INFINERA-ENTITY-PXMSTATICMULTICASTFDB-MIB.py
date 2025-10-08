#
# PySNMP MIB module INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:44 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-PXMSTATICMULTICASTFDB-MIB", PYSNMP_MODULE_ID=pxmStaticMulticastFdbMIB, pxmStaticMulticastFdbCompliance=pxmStaticMulticastFdbCompliance, pxmStaticMulticastFdbGroup=pxmStaticMulticastFdbGroup, pxmStaticMulticastFdbConformance=pxmStaticMulticastFdbConformance, pxmStaticMulticastFdbCompliances=pxmStaticMulticastFdbCompliances, pxmStaticMulticastFdbMacAddress=pxmStaticMulticastFdbMacAddress, pxmStaticMulticastFdbTable=pxmStaticMulticastFdbTable, pxmStaticMulticastFdbEntry=pxmStaticMulticastFdbEntry, pxmStaticMulticastFdbMIB=pxmStaticMulticastFdbMIB, pxmStaticMulticastFdbGroups=pxmStaticMulticastFdbGroups)
