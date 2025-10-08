#
# PySNMP MIB module INFINERA-ENTITY-XTMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XTMM-MIB
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
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-XTMM-MIB", xtmmMoId=xtmmMoId, xtmmCompliances=xtmmCompliances, PYSNMP_MODULE_ID=xtmmMIB, xtmmProvType=xtmmProvType, xtmmBrandingFault=xtmmBrandingFault, xtmmCompliance=xtmmCompliance, xtmmGroup=xtmmGroup, xtmmGroups=xtmmGroups, xtmmConformance=xtmmConformance, xtmmEntry=xtmmEntry, xtmmMIB=xtmmMIB, xtmmRowStatus=xtmmRowStatus, xtmmTable=xtmmTable)
