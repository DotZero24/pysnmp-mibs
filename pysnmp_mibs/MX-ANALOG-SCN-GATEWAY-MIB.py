#
# PySNMP MIB module MX-ANALOG-SCN-GATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/media5/MX-ANALOG-SCN-GATEWAY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:34 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixConfig, = mibBuilder.importSymbols("MX-SMI", "mediatrixConfig")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MX-ANALOG-SCN-GATEWAY-MIB", analogScnGwInterDigitDialDelay=analogScnGwInterDigitDialDelay, analogScnGwComplVer1=analogScnGwComplVer1, analogScnGwPreDialDelay=analogScnGwPreDialDelay, analogScnGwConformance=analogScnGwConformance, analogScnGwMIBObjects=analogScnGwMIBObjects, analogScnGwDialEnable=analogScnGwDialEnable, analogScnGwMIB=analogScnGwMIB, analogScnGwDtmfDuration=analogScnGwDtmfDuration, PYSNMP_MODULE_ID=analogScnGwMIB, analogScnGwGroups=analogScnGwGroups, analogScnGwDialingVer1=analogScnGwDialingVer1, analogScnGwDialPrefix=analogScnGwDialPrefix, analogScnGwIfDialingEntry=analogScnGwIfDialingEntry, analogScnGwIfDialingTable=analogScnGwIfDialingTable, analogScnGwCompliances=analogScnGwCompliances)
