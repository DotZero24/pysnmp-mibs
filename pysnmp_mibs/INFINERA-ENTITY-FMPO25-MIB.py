#
# PySNMP MIB module INFINERA-ENTITY-FMPO25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-FMPO25-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:50 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-FMPO25-MIB", fmpo25Compliances=fmpo25Compliances, fmpo25ProvEqptType=fmpo25ProvEqptType, fmpo25Groups=fmpo25Groups, fmpo25Table=fmpo25Table, fmpo25Group=fmpo25Group, fmpo25Entry=fmpo25Entry, fmpo25ProvSerialNumber=fmpo25ProvSerialNumber, fmpo25MoId=fmpo25MoId, PYSNMP_MODULE_ID=fmpo25MIB, fmpo25Compliance=fmpo25Compliance, fmpo25Conformance=fmpo25Conformance, fmpo25MIB=fmpo25MIB)
