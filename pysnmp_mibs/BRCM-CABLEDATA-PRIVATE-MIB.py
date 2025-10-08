#
# PySNMP MIB module BRCM-CABLEDATA-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataPrivate, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataPrivate")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
cableDataPrivateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1))
cableDataPrivateMIB.setRevisions(('2007-02-05 00:00', '2002-06-04 00:00',))
if mibBuilder.loadTexts: cableDataPrivateMIB.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: cableDataPrivateMIB.setOrganization('Broadcom Corporation')
cableDataPrivateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1))
cableDataPrivateBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1))
cdPrivateMibEnable = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("factory", 1), ("engineering", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdPrivateMibEnable.setStatus('current')
cdPrivateMibEnableKeyTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2), )
if mibBuilder.loadTexts: cdPrivateMibEnableKeyTable.setStatus('current')
cdPrivateMibEnableKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1), ).setIndexNames((0, "BRCM-CABLEDATA-PRIVATE-MIB", "cdPvtMibEnableKeyIndex"))
if mibBuilder.loadTexts: cdPrivateMibEnableKeyEntry.setStatus('current')
cdPvtMibEnableKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: cdPvtMibEnableKeyIndex.setStatus('current')
cdPvtMibEnableKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 2), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdPvtMibEnableKeyValue.setStatus('current')
cdPvtMibEnableKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdPvtMibEnableKeyStatus.setStatus('current')
mibBuilder.exportSymbols("BRCM-CABLEDATA-PRIVATE-MIB", cdPvtMibEnableKeyStatus=cdPvtMibEnableKeyStatus, cdPrivateMibEnableKeyEntry=cdPrivateMibEnableKeyEntry, cdPvtMibEnableKeyValue=cdPvtMibEnableKeyValue, cdPrivateMibEnable=cdPrivateMibEnable, cableDataPrivateMIB=cableDataPrivateMIB, cdPrivateMibEnableKeyTable=cdPrivateMibEnableKeyTable, PYSNMP_MODULE_ID=cableDataPrivateMIB, cableDataPrivateBase=cableDataPrivateBase, cableDataPrivateMIBObjects=cableDataPrivateMIBObjects, cdPvtMibEnableKeyIndex=cdPvtMibEnableKeyIndex)
