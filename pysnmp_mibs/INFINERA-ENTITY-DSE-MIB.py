#
# PySNMP MIB module INFINERA-ENTITY-DSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-DSE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:56 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, FloatTenths, InfnConvergenceStatus, InfnEqualizationCtrlLoop = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "FloatTenths", "InfnConvergenceStatus", "InfnEqualizationCtrlLoop")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
dseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17))
if mibBuilder.loadTexts: dseMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: dseMIB.setOrganization('INFINERA')
dseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3))
dseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 1))
dseGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 2))
dseTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1), )
if mibBuilder.loadTexts: dseTable.setStatus('current')
dseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: dseEntry.setStatus('current')
dseMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dseMoId.setStatus('current')
dseProvEqptType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dseProvEqptType.setStatus('current')
dseSpectrumTiltOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 3), FloatTenths()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dseSpectrumTiltOffset.setStatus('current')
dseEqualizationCtrlLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 4), InfnEqualizationCtrlLoop()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dseEqualizationCtrlLoop.setStatus('current')
dseConvergenceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 5), InfnConvergenceStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dseConvergenceStatus.setStatus('current')
dseRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dseRowStatus.setStatus('current')
dseCtrlLoopTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dseCtrlLoopTimer.setStatus('current')
dseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 1, 1)).setObjects(("INFINERA-ENTITY-DSE-MIB", "dseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dseCompliance = dseCompliance.setStatus('current')
dseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 17, 3, 2, 1)).setObjects(("INFINERA-ENTITY-DSE-MIB", "dseMoId"), ("INFINERA-ENTITY-DSE-MIB", "dseProvEqptType"), ("INFINERA-ENTITY-DSE-MIB", "dseSpectrumTiltOffset"), ("INFINERA-ENTITY-DSE-MIB", "dseEqualizationCtrlLoop"), ("INFINERA-ENTITY-DSE-MIB", "dseConvergenceStatus"), ("INFINERA-ENTITY-DSE-MIB", "dseRowStatus"), ("INFINERA-ENTITY-DSE-MIB", "dseCtrlLoopTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dseGroup = dseGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-DSE-MIB", dseTable=dseTable, dseGroups=dseGroups, dseRowStatus=dseRowStatus, dseGroup=dseGroup, dseConformance=dseConformance, dseSpectrumTiltOffset=dseSpectrumTiltOffset, PYSNMP_MODULE_ID=dseMIB, dseCtrlLoopTimer=dseCtrlLoopTimer, dseMIB=dseMIB, dseProvEqptType=dseProvEqptType, dseCompliance=dseCompliance, dseMoId=dseMoId, dseEntry=dseEntry, dseConvergenceStatus=dseConvergenceStatus, dseCompliances=dseCompliances, dseEqualizationCtrlLoop=dseEqualizationCtrlLoop)
