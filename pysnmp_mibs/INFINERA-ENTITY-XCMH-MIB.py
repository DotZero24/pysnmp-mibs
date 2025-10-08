#
# PySNMP MIB module INFINERA-ENTITY-XCMH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XCMH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnCorrelatedRedunStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnCorrelatedRedunStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
xcmhMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31))
if mibBuilder.loadTexts: xcmhMIB.setLastUpdated('201501200000Z')
if mibBuilder.loadTexts: xcmhMIB.setOrganization('INFINERA')
xcmhConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3))
xcmhCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 1))
xcmhGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 2))
xcmhTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1), )
if mibBuilder.loadTexts: xcmhTable.setStatus('current')
xcmhEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: xcmhEntry.setStatus('current')
xcmhMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmhMoId.setStatus('current')
xcmhProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmhProvType.setStatus('current')
xcmhRedundancyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 3), InfnCorrelatedRedunStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcmhRedundancyStatus.setStatus('current')
xcmhBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcmhBrandingFault.setStatus('current')
xcmhRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xcmhRowStatus.setStatus('current')
xcmhCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 1, 1)).setObjects(("INFINERA-ENTITY-XCMH-MIB", "xcmhGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xcmhCompliance = xcmhCompliance.setStatus('current')
xcmhGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 31, 3, 2, 1)).setObjects(("INFINERA-ENTITY-XCMH-MIB", "xcmhBrandingFault"), ("INFINERA-ENTITY-XCMH-MIB", "xcmhMoId"), ("INFINERA-ENTITY-XCMH-MIB", "xcmhProvType"), ("INFINERA-ENTITY-XCMH-MIB", "xcmhRedundancyStatus"), ("INFINERA-ENTITY-XCMH-MIB", "xcmhBrandingFault"), ("INFINERA-ENTITY-XCMH-MIB", "xcmhRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xcmhGroup = xcmhGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-XCMH-MIB", xcmhMIB=xcmhMIB, xcmhCompliance=xcmhCompliance, xcmhTable=xcmhTable, xcmhGroup=xcmhGroup, xcmhRedundancyStatus=xcmhRedundancyStatus, xcmhProvType=xcmhProvType, xcmhConformance=xcmhConformance, xcmhCompliances=xcmhCompliances, xcmhGroups=xcmhGroups, xcmhRowStatus=xcmhRowStatus, xcmhBrandingFault=xcmhBrandingFault, PYSNMP_MODULE_ID=xcmhMIB, xcmhEntry=xcmhEntry, xcmhMoId=xcmhMoId)
