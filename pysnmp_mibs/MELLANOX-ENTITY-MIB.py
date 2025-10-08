#
# PySNMP MIB module MELLANOX-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mellanox/MELLANOX-ENTITY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mellanoxEntity, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxEntity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MELLANOX-ENTITY-MIB", mellanoxPhysicalEntityAsicRev=mellanoxPhysicalEntityAsicRev, mellanoxPhysicalEntityTable=mellanoxPhysicalEntityTable, PYSNMP_MODULE_ID=mellanoxEntityMib, mellanoxPhysicalEntityGUID=mellanoxPhysicalEntityGUID, mellanoxEntityMib=mellanoxEntityMib, mellanoxPhysicalEntityEntry=mellanoxPhysicalEntityEntry)
