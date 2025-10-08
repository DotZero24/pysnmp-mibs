#
# PySNMP MIB module BRCM-CM-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CM-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataProducts, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataProducts")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-CM-PRODUCTS-MIB", bcm93300=bcm93300, bcm93345=bcm93345, bcm93349=bcm93349, bcm93351=bcm93351, bcm93348=bcm93348, bcm93360=bcm93360, cmReferenceDesigns=cmReferenceDesigns, brcmCmProducts=brcmCmProducts, bcm93368=bcm93368, bcm93352=bcm93352, bcm93381=bcm93381, bcm93350=bcm93350, bcm93220=bcm93220, PYSNMP_MODULE_ID=brcmCmProducts, bcm93367=bcm93367, bcm93380=bcm93380)
