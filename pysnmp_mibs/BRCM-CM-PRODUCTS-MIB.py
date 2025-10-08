#
# PySNMP MIB module BRCM-CM-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CM-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataProducts, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataProducts")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
brcmCmProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2))
brcmCmProducts.setRevisions(('2007-02-05 00:00', '2004-02-11 00:00',))
if mibBuilder.loadTexts: brcmCmProducts.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: brcmCmProducts.setOrganization('Broadcom Corporation')
cmReferenceDesigns = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1))
bcm93220 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3220))
bcm93300 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3300))
bcm93345 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3345))
bcm93348 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3348))
bcm93349 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3349))
bcm93350 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3350))
bcm93351 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3351))
bcm93352 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3352))
bcm93360 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3360))
bcm93367 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3367))
bcm93368 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3368))
bcm93380 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3380))
bcm93381 = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3381))
mibBuilder.exportSymbols("BRCM-CM-PRODUCTS-MIB", bcm93345=bcm93345, bcm93381=bcm93381, bcm93349=bcm93349, bcm93352=bcm93352, cmReferenceDesigns=cmReferenceDesigns, PYSNMP_MODULE_ID=brcmCmProducts, bcm93368=bcm93368, bcm93300=bcm93300, bcm93380=bcm93380, bcm93351=bcm93351, bcm93350=bcm93350, brcmCmProducts=brcmCmProducts, bcm93220=bcm93220, bcm93348=bcm93348, bcm93360=bcm93360, bcm93367=bcm93367)
