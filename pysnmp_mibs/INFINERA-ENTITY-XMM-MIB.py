#
# PySNMP MIB module INFINERA-ENTITY-XMM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/infinera/INFINERA-ENTITY-XMM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:20:36 2025
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
mibBuilder.exportSymbols("INFINERA-ENTITY-XMM-MIB", xmmEntry=xmmEntry, xmmCompliance=xmmCompliance, xmmCompliances=xmmCompliances, xmmConformance=xmmConformance, xmmRowStatus=xmmRowStatus, xmmGroup=xmmGroup, xmmMoId=xmmMoId, xmmTable=xmmTable, xmmMIB=xmmMIB, xmmBrandingFault=xmmBrandingFault, xmmProvType=xmmProvType, xmmGroups=xmmGroups, PYSNMP_MODULE_ID=xmmMIB)
