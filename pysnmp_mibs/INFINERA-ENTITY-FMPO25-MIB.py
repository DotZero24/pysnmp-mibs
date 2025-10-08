#
# PySNMP MIB module INFINERA-ENTITY-FMPO25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FMPO25-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:41 2025
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
fmpo25MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51))
if mibBuilder.loadTexts: fmpo25MIB.setLastUpdated('201604220000Z')
if mibBuilder.loadTexts: fmpo25MIB.setOrganization('INFINERA')
fmpo25Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3))
fmpo25Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 1))
fmpo25Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 2))
fmpo25Table = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1), )
if mibBuilder.loadTexts: fmpo25Table.setStatus('current')
fmpo25Entry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: fmpo25Entry.setStatus('current')
fmpo25MoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fmpo25MoId.setStatus('current')
fmpo25ProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fmpo25ProvEqptType.setStatus('current')
fmpo25ProvSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fmpo25ProvSerialNumber.setStatus('current')
fmpo25Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 1, 1)).setObjects(("INFINERA-ENTITY-FMPO25-MIB", "fmpo25Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo25Compliance = fmpo25Compliance.setStatus('current')
fmpo25Group = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 2, 1)).setObjects(("INFINERA-ENTITY-FMPO25-MIB", "fmpo25MoId"), ("INFINERA-ENTITY-FMPO25-MIB", "fmpo25ProvEqptType"), ("INFINERA-ENTITY-FMPO25-MIB", "fmpo25ProvSerialNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fmpo25Group = fmpo25Group.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-FMPO25-MIB", PYSNMP_MODULE_ID=fmpo25MIB, fmpo25Compliances=fmpo25Compliances, fmpo25Table=fmpo25Table, fmpo25Conformance=fmpo25Conformance, fmpo25ProvSerialNumber=fmpo25ProvSerialNumber, fmpo25Compliance=fmpo25Compliance, fmpo25Entry=fmpo25Entry, fmpo25Groups=fmpo25Groups, fmpo25MIB=fmpo25MIB, fmpo25Group=fmpo25Group, fmpo25MoId=fmpo25MoId, fmpo25ProvEqptType=fmpo25ProvEqptType)
