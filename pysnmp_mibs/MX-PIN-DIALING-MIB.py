#
# PySNMP MIB module MX-PIN-DIALING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-PIN-DIALING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixExperimental, = mibBuilder.importSymbols("MX-SMI", "mediatrixExperimental")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pinDialingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 99, 90))
pinDialingMIB.setRevisions(('2006-03-06 00:00', '2004-08-19 00:00',))
if mibBuilder.loadTexts: pinDialingMIB.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: pinDialingMIB.setOrganization('Mediatrix Telecom, Inc.')
pinDialingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1))
pinDialingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 90, 2))
pinDialingIfTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10), )
if mibBuilder.loadTexts: pinDialingIfTable.setStatus('current')
pinDialingIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pinDialingIfEntry.setStatus('current')
pinDialingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 10), MxEnableState().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pinDialingEnable.setStatus('current')
pinDialingPin = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pinDialingPin.setStatus('current')
pinDialingDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 99, 90, 1, 10, 1, 30), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pinDialingDelay.setStatus('current')
pinDialingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 1))
pinDialingBasicComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 1, 1)).setObjects(("MX-PIN-DIALING-MIB", "pinDialingGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pinDialingBasicComplVer1 = pinDialingBasicComplVer1.setStatus('current')
pinDialingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 2))
pinDialingGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 99, 90, 2, 2, 1)).setObjects(("MX-PIN-DIALING-MIB", "pinDialingEnable"), ("MX-PIN-DIALING-MIB", "pinDialingPin"), ("MX-PIN-DIALING-MIB", "pinDialingDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pinDialingGroupVer1 = pinDialingGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-PIN-DIALING-MIB", pinDialingEnable=pinDialingEnable, pinDialingIfTable=pinDialingIfTable, pinDialingIfEntry=pinDialingIfEntry, pinDialingDelay=pinDialingDelay, pinDialingPin=pinDialingPin, pinDialingGroups=pinDialingGroups, pinDialingMIBObjects=pinDialingMIBObjects, pinDialingMIB=pinDialingMIB, pinDialingConformance=pinDialingConformance, pinDialingGroupVer1=pinDialingGroupVer1, pinDialingCompliances=pinDialingCompliances, pinDialingBasicComplVer1=pinDialingBasicComplVer1, PYSNMP_MODULE_ID=pinDialingMIB)
