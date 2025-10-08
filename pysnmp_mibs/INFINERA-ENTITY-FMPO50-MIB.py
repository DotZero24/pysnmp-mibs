#
# PySNMP MIB module INFINERA-ENTITY-FMPO50-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FMPO50-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-FMPO50-MIB", PYSNMP_MODULE_ID=fmpo50MIB, fmpo50Conformance=fmpo50Conformance, fmpo50Table=fmpo50Table, fmpo50Compliances=fmpo50Compliances, fmpo50Compliance=fmpo50Compliance, fmpo50MIB=fmpo50MIB, fmpo50Entry=fmpo50Entry, fmpo50Groups=fmpo50Groups, fmpo50ProvEqptType=fmpo50ProvEqptType, fmpo50Group=fmpo50Group, fmpo50MoId=fmpo50MoId, fmpo50ProvSerialNumber=fmpo50ProvSerialNumber)
