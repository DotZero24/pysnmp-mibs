#
# PySNMP MIB module INFINERA-ENTITY-DSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-DSE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:44 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnConvergenceStatus, InfnEqualizationCtrlLoop, FloatTenths = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnConvergenceStatus", "InfnEqualizationCtrlLoop", "FloatTenths")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-DSE-MIB", dseProvEqptType=dseProvEqptType, dseConvergenceStatus=dseConvergenceStatus, dseConformance=dseConformance, dseGroups=dseGroups, dseCompliances=dseCompliances, dseMIB=dseMIB, dseTable=dseTable, dseEqualizationCtrlLoop=dseEqualizationCtrlLoop, dseCtrlLoopTimer=dseCtrlLoopTimer, PYSNMP_MODULE_ID=dseMIB, dseGroup=dseGroup, dseMoId=dseMoId, dseEntry=dseEntry, dseRowStatus=dseRowStatus, dseCompliance=dseCompliance, dseSpectrumTiltOffset=dseSpectrumTiltOffset)
