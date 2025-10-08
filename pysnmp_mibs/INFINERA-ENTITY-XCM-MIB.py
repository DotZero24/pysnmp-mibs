#
# PySNMP MIB module INFINERA-ENTITY-XCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XCM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:49 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnXcmTimingSrcRedunState, InfnCorrelatedRedunStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnXcmTimingSrcRedunState", "InfnCorrelatedRedunStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
xcmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21))
if mibBuilder.loadTexts: xcmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: xcmMIB.setOrganization('INFINERA')
xcmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3))
xcmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 1))
xcmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 2))
xcmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1), )
if mibBuilder.loadTexts: xcmTable.setStatus('current')
xcmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: xcmEntry.setStatus('current')
xcmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmMoId.setStatus('current')
xcmProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmProvType.setStatus('current')
xcmRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 3), InfnCorrelatedRedunStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcmRedundancyStatus.setStatus('current')
xcmBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcmBrandingFault.setStatus('current')
xcmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmRowStatus.setStatus('current')
timingSrcRedunState = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 1, 1, 6), InfnXcmTimingSrcRedunState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSrcRedunState.setStatus('current')
xcmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 1, 1)).setObjects(("INFINERA-ENTITY-XCM-MIB", "xcmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xcmCompliance = xcmCompliance.setStatus('current')
xcmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 21, 3, 2, 1)).setObjects(("INFINERA-ENTITY-XCM-MIB", "xcmBrandingFault"), ("INFINERA-ENTITY-XCM-MIB", "xcmMoId"), ("INFINERA-ENTITY-XCM-MIB", "xcmProvType"), ("INFINERA-ENTITY-XCM-MIB", "xcmRedundancyStatus"), ("INFINERA-ENTITY-XCM-MIB", "xcmRowStatus"), ("INFINERA-ENTITY-XCM-MIB", "timingSrcRedunState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xcmGroup = xcmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-XCM-MIB", xcmEntry=xcmEntry, xcmMoId=xcmMoId, xcmRedundancyStatus=xcmRedundancyStatus, xcmCompliances=xcmCompliances, PYSNMP_MODULE_ID=xcmMIB, xcmBrandingFault=xcmBrandingFault, xcmProvType=xcmProvType, xcmMIB=xcmMIB, xcmCompliance=xcmCompliance, xcmGroup=xcmGroup, xcmConformance=xcmConformance, timingSrcRedunState=timingSrcRedunState, xcmTable=xcmTable, xcmRowStatus=xcmRowStatus, xcmGroups=xcmGroups)
