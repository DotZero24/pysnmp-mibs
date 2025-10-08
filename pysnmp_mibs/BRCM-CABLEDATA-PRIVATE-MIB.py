#
# PySNMP MIB module BRCM-CABLEDATA-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-CABLEDATA-PRIVATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataPrivate, = mibBuilder.importSymbols("BRCM-CABLEDATA-SMI", "cableDataPrivate")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("BRCM-CABLEDATA-PRIVATE-MIB", cdPvtMibEnableKeyValue=cdPvtMibEnableKeyValue, cdPrivateMibEnable=cdPrivateMibEnable, cdPrivateMibEnableKeyEntry=cdPrivateMibEnableKeyEntry, cableDataPrivateMIB=cableDataPrivateMIB, cdPrivateMibEnableKeyTable=cdPrivateMibEnableKeyTable, cdPvtMibEnableKeyIndex=cdPvtMibEnableKeyIndex, cdPvtMibEnableKeyStatus=cdPvtMibEnableKeyStatus, cableDataPrivateBase=cableDataPrivateBase, PYSNMP_MODULE_ID=cableDataPrivateMIB, cableDataPrivateMIBObjects=cableDataPrivateMIBObjects)
