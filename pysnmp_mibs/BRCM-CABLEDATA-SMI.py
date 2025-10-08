#
# PySNMP MIB module BRCM-CABLEDATA-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-SMI
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
broadcom, = mibBuilder.importSymbols("BRCM-SMI", "broadcom")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cableData = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2))
cableData.setRevisions(('2007-05-21 00:00', '2007-02-05 00:00', '2002-07-31 00:00',))
if mibBuilder.loadTexts: cableData.setLastUpdated('200705210000Z')
if mibBuilder.loadTexts: cableData.setOrganization('Broadcom Corporation')
cableDataProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 1))
if mibBuilder.loadTexts: cableDataProducts.setStatus('current')
cableDataMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2))
if mibBuilder.loadTexts: cableDataMgmt.setStatus('current')
cableDataAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 3))
if mibBuilder.loadTexts: cableDataAgentCapability.setStatus('current')
cableDataExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 4))
if mibBuilder.loadTexts: cableDataExperimental.setStatus('current')
cableDataPrivate = ObjectIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99))
if mibBuilder.loadTexts: cableDataPrivate.setStatus('current')
mibBuilder.exportSymbols("BRCM-CABLEDATA-SMI", cableDataMgmt=cableDataMgmt, cableDataExperimental=cableDataExperimental, cableDataProducts=cableDataProducts, cableData=cableData, PYSNMP_MODULE_ID=cableData, cableDataAgentCapability=cableDataAgentCapability, cableDataPrivate=cableDataPrivate)
