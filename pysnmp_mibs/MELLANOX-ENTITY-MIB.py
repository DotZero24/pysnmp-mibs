#
# PySNMP MIB module MELLANOX-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mellanox/MELLANOX-ENTITY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mellanoxEntity, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxEntity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mellanoxEntityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 33049, 5, 1))
mellanoxEntityMib.setRevisions(('2013-06-30 00:00',))
if mibBuilder.loadTexts: mellanoxEntityMib.setLastUpdated('201306300000Z')
if mibBuilder.loadTexts: mellanoxEntityMib.setOrganization('Mellanox Technologies, Inc.')
mellanoxPhysicalEntityTable = MibTable((1, 3, 6, 1, 4, 1, 33049, 5, 1, 1), )
if mibBuilder.loadTexts: mellanoxPhysicalEntityTable.setStatus('current')
mellanoxPhysicalEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33049, 5, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mellanoxPhysicalEntityEntry.setStatus('current')
mellanoxPhysicalEntityGUID = MibTableColumn((1, 3, 6, 1, 4, 1, 33049, 5, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxPhysicalEntityGUID.setStatus('current')
mellanoxPhysicalEntityAsicRev = MibTableColumn((1, 3, 6, 1, 4, 1, 33049, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxPhysicalEntityAsicRev.setStatus('current')
mibBuilder.exportSymbols("MELLANOX-ENTITY-MIB", PYSNMP_MODULE_ID=mellanoxEntityMib, mellanoxPhysicalEntityTable=mellanoxPhysicalEntityTable, mellanoxEntityMib=mellanoxEntityMib, mellanoxPhysicalEntityGUID=mellanoxPhysicalEntityGUID, mellanoxPhysicalEntityAsicRev=mellanoxPhysicalEntityAsicRev, mellanoxPhysicalEntityEntry=mellanoxPhysicalEntityEntry)
