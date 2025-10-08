#
# PySNMP MIB module INFINERA-ENTITY-XMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XMM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:32 2025
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
xmmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36))
if mibBuilder.loadTexts: xmmMIB.setLastUpdated('200810200000Z')
if mibBuilder.loadTexts: xmmMIB.setOrganization('INFINERA')
xmmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3))
xmmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 1))
xmmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 2))
xmmTable = MibTable((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1), )
if mibBuilder.loadTexts: xmmTable.setStatus('current')
xmmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entLPPhysicalIndex"))
if mibBuilder.loadTexts: xmmEntry.setStatus('current')
xmmMoId = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 1), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xmmMoId.setStatus('current')
xmmProvType = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 2), InfnEqptType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xmmProvType.setStatus('current')
xmmBrandingFault = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xmmBrandingFault.setStatus('current')
xmmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: xmmRowStatus.setStatus('current')
xmmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 1, 1)).setObjects(("INFINERA-ENTITY-XMM-MIB", "xmmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xmmCompliance = xmmCompliance.setStatus('current')
xmmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 36, 3, 2, 1)).setObjects(("INFINERA-ENTITY-XMM-MIB", "xmmBrandingFault"), ("INFINERA-ENTITY-XMM-MIB", "xmmMoId"), ("INFINERA-ENTITY-XMM-MIB", "xmmProvType"), ("INFINERA-ENTITY-XMM-MIB", "xmmRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xmmGroup = xmmGroup.setStatus('current')
mibBuilder.exportSymbols("INFINERA-ENTITY-XMM-MIB", xmmProvType=xmmProvType, xmmBrandingFault=xmmBrandingFault, xmmRowStatus=xmmRowStatus, xmmGroups=xmmGroups, xmmEntry=xmmEntry, xmmConformance=xmmConformance, PYSNMP_MODULE_ID=xmmMIB, xmmCompliances=xmmCompliances, xmmGroup=xmmGroup, xmmMIB=xmmMIB, xmmCompliance=xmmCompliance, xmmTable=xmmTable, xmmMoId=xmmMoId)
