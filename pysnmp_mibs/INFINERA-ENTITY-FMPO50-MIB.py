#
# PySNMP MIB module INFINERA-ENTITY-FMPO50-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FMPO50-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fmpo50MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52))
if mibBuilder.loadTexts: fmpo50MIB.setLastUpdated('201501080000Z')
if mibBuilder.loadTexts: fmpo50MIB.setOrganization('INFINERA')
fmpo50Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3))
fmpo50Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 1))
fmpo50Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 2))
fmpo50Table = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1), )
if mibBuilder.loadTexts: fmpo50Table.setStatus('current')
fmpo50Entry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: fmpo50Entry.setStatus('current')
fmpo50MoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fmpo50MoId.setStatus('current')
fmpo50ProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fmpo50ProvEqptType.setStatus('current')
fmpo50ProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpo50ProvSerialNumber.setStatus('current')
fmpo50Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FMPO50-MIB", "fmpo50Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo50Compliance = fmpo50Compliance.setStatus('current')
fmpo50Group = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FMPO50-MIB", "fmpo50MoId"), ("INFINERA-ENTITY-FMPO50-MIB", "fmpo50ProvEqptType"), ("INFINERA-ENTITY-FMPO50-MIB", "fmpo50ProvSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo50Group = fmpo50Group.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FMPO50-MIB", fmpo50Table=fmpo50Table, fmpo50Conformance=fmpo50Conformance, fmpo50ProvSerialNumber=fmpo50ProvSerialNumber, fmpo50MIB=fmpo50MIB, fmpo50Groups=fmpo50Groups, fmpo50Compliance=fmpo50Compliance, fmpo50Group=fmpo50Group, PYSNMP_MODULE_ID=fmpo50MIB, fmpo50Compliances=fmpo50Compliances, fmpo50ProvEqptType=fmpo50ProvEqptType, fmpo50MoId=fmpo50MoId, fmpo50Entry=fmpo50Entry)
