#
# PySNMP MIB module INFINERA-ENTITY-XCMH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XCMH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:21:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
entLPPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entLPPhysicalIndex")
equipment, = mibBuilder.importSymbols("INFINERA-REG-MIB", "equipment")
InfnEqptType, InfnCorrelatedRedunStatus = mibBuilder.importSymbols("INFINERA-TC-MIB", "InfnEqptType", "InfnCorrelatedRedunStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("INFINERA-ENTITY-XCMH-MIB", xcmhEntry=xcmhEntry, xcmhTable=xcmhTable, xcmhMIB=xcmhMIB, xcmhCompliances=xcmhCompliances, xcmhGroups=xcmhGroups, xcmhGroup=xcmhGroup, PYSNMP_MODULE_ID=xcmhMIB, xcmhConformance=xcmhConformance, xcmhMoId=xcmhMoId, xcmhBrandingFault=xcmhBrandingFault, xcmhProvType=xcmhProvType, xcmhRedundancyStatus=xcmhRedundancyStatus, xcmhRowStatus=xcmhRowStatus, xcmhCompliance=xcmhCompliance)
