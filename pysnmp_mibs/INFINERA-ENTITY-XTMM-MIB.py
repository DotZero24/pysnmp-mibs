#
# PySNMP MIB module INFINERA-ENTITY-XTMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XTMM-MIB
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
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
xtmmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54))
if mibBuilder.loadTexts: xtmmMIB.setLastUpdated('201608020000Z')
if mibBuilder.loadTexts: xtmmMIB.setOrganization('INFINERA')
xtmmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3))
xtmmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 1))
xtmmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 2))
xtmmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1), )
if mibBuilder.loadTexts: xtmmTable.setStatus('current')
xtmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: xtmmEntry.setStatus('current')
xtmmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmmMoId.setStatus('current')
xtmmProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmmProvType.setStatus('current')
xtmmBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xtmmBrandingFault.setStatus('current')
xtmmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xtmmRowStatus.setStatus('current')
xtmmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 1, 1)).setObjects(("INFINERA-ENTITY-XTMM-MIB", "xtmmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xtmmCompliance = xtmmCompliance.setStatus('current')
xtmmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 54, 3, 2, 1)).setObjects(("INFINERA-ENTITY-XTMM-MIB", "xtmmBrandingFault"), ("INFINERA-ENTITY-XTMM-MIB", "xtmmMoId"), ("INFINERA-ENTITY-XTMM-MIB", "xtmmProvType"), ("INFINERA-ENTITY-XTMM-MIB", "xtmmRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xtmmGroup = xtmmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-XTMM-MIB", xtmmGroup=xtmmGroup, xtmmBrandingFault=xtmmBrandingFault, xtmmTable=xtmmTable, xtmmEntry=xtmmEntry, xtmmMoId=xtmmMoId, PYSNMP_MODULE_ID=xtmmMIB, xtmmProvType=xtmmProvType, xtmmCompliance=xtmmCompliance, xtmmCompliances=xtmmCompliances, xtmmRowStatus=xtmmRowStatus, xtmmGroups=xtmmGroups, xtmmConformance=xtmmConformance, xtmmMIB=xtmmMIB)
