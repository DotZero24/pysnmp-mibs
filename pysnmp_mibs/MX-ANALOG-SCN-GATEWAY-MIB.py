#
# PySNMP MIB module MX-ANALOG-SCN-GATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-ANALOG-SCN-GATEWAY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:07 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
analogScnGwMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 15, 85))
analogScnGwMIB.setRevisions(('2005-10-27 00:00', '2003-08-12 00:00', '2003-03-25 00:00', '2003-02-25 00:00',))
if mibBuilder.loadTexts: analogScnGwMIB.setLastUpdated('200510270000Z')
if mibBuilder.loadTexts: analogScnGwMIB.setOrganization('Mediatrix Telecom, Inc.')
analogScnGwMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1))
analogScnGwConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 85, 5))
analogScnGwIfDialingTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10), )
if mibBuilder.loadTexts: analogScnGwIfDialingTable.setStatus('current')
analogScnGwIfDialingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: analogScnGwIfDialingEntry.setStatus('current')
analogScnGwDialPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogScnGwDialPrefix.setStatus('current')
analogScnGwPreDialDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogScnGwPreDialDelay.setStatus('current')
analogScnGwInterDigitDialDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(50, 600)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogScnGwInterDigitDialDelay.setStatus('current')
analogScnGwDtmfDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 25), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(50, 600)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogScnGwDtmfDuration.setStatus('current')
analogScnGwDialEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 15, 85, 1, 10, 5, 75), MxEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: analogScnGwDialEnable.setStatus('current')
analogScnGwCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 1))
analogScnGwComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 1, 1)).setObjects(("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialingVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    analogScnGwComplVer1 = analogScnGwComplVer1.setStatus('current')
analogScnGwGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 5))
analogScnGwDialingVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 15, 85, 5, 5, 10)).setObjects(("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialPrefix"), ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwPreDialDelay"), ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwInterDigitDialDelay"), ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDtmfDuration"), ("MX-ANALOG-SCN-GATEWAY-MIB", "analogScnGwDialEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    analogScnGwDialingVer1 = analogScnGwDialingVer1.setStatus('current')
mibBuilder.exportSymbols("MX-ANALOG-SCN-GATEWAY-MIB", analogScnGwIfDialingEntry=analogScnGwIfDialingEntry, analogScnGwMIB=analogScnGwMIB, PYSNMP_MODULE_ID=analogScnGwMIB, analogScnGwInterDigitDialDelay=analogScnGwInterDigitDialDelay, analogScnGwMIBObjects=analogScnGwMIBObjects, analogScnGwDtmfDuration=analogScnGwDtmfDuration, analogScnGwComplVer1=analogScnGwComplVer1, analogScnGwDialEnable=analogScnGwDialEnable, analogScnGwCompliances=analogScnGwCompliances, analogScnGwDialingVer1=analogScnGwDialingVer1, analogScnGwDialPrefix=analogScnGwDialPrefix, analogScnGwGroups=analogScnGwGroups, analogScnGwPreDialDelay=analogScnGwPreDialDelay, analogScnGwIfDialingTable=analogScnGwIfDialingTable, analogScnGwConformance=analogScnGwConformance)
