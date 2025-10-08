#
# PySNMP MIB module INFINERA-ENTITY-IMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-IMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnFlashStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnFlashStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
immMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27))
if mibBuilder.loadTexts: immMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: immMIB.setOrganization('INFINERA')
immConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3))
immCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 1))
immGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 2))
immTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1), )
if mibBuilder.loadTexts: immTable.setStatus('current')
immEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: immEntry.setStatus('current')
immMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: immMoId.setStatus('current')
immProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: immProvEqptType.setStatus('current')
immInterfaceTypeNCT = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copper", 1), ("fiber", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: immInterfaceTypeNCT.setStatus('current')
immFlashStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 1, 1, 4), InfnFlashStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: immFlashStatus.setStatus('current')
immCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 1, 1)).setObjects(("INFINERA-ENTITY-IMM-MIB", "immGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    immCompliance = immCompliance.setStatus('current')
immGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 27, 3, 2, 1)).setObjects(("INFINERA-ENTITY-IMM-MIB", "immMoId"), ("INFINERA-ENTITY-IMM-MIB", "immProvEqptType"), ("INFINERA-ENTITY-IMM-MIB", "immInterfaceTypeNCT"), ("INFINERA-ENTITY-IMM-MIB", "immFlashStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    immGroup = immGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-IMM-MIB", immInterfaceTypeNCT=immInterfaceTypeNCT, immFlashStatus=immFlashStatus, immMoId=immMoId, immCompliance=immCompliance, immMIB=immMIB, immGroup=immGroup, immEntry=immEntry, immConformance=immConformance, immProvEqptType=immProvEqptType, PYSNMP_MODULE_ID=immMIB, immGroups=immGroups, immCompliances=immCompliances, immTable=immTable)
