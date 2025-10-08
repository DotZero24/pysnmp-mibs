#
# PySNMP MIB module BRCM-CABLEDATA-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
broadcom, = mibBuilder.importSymbols("BRCM-SMI", "broadcom")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BRCM-CABLEDATA-SMI", cableData=cableData, cableDataMgmt=cableDataMgmt, PYSNMP_MODULE_ID=cableData, cableDataExperimental=cableDataExperimental, cableDataPrivate=cableDataPrivate, cableDataAgentCapability=cableDataAgentCapability, cableDataProducts=cableDataProducts)
