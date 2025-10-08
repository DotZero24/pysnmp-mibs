#
# PySNMP MIB module ARRIS-MTA-DOC30-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/arris/ARRIS-MTA-DOC30-DEVICE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "DateAndTime", "TruthValue", "TextualConvention")
arrisMtaDoc30Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5))
arrisMtaDoc30Mib.setRevisions(('1910-10-20 00:00',))
if mibBuilder.loadTexts: arrisMtaDoc30Mib.setLastUpdated('1010200000Z')
if mibBuilder.loadTexts: arrisMtaDoc30Mib.setOrganization('ARRIS Broadband')
arrisMtaDoc30MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1))
arrisMtaDoc30Base = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 1))
arrisMtaDoc30Setup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2))
arrisMtaDoc30EmergencyNumber = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMtaDoc30EmergencyNumber.setStatus('current')
arrisMtaDoc30RootCertType = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("testRoot", 1), ("realRoot", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMtaDoc30RootCertType.setStatus('current')
arrisMtaDoc30AdjustCallpFeatureSwitch = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMtaDoc30AdjustCallpFeatureSwitch.setStatus('current')
arrisMtaDoc30InvalidateTickets = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 3, 5, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: arrisMtaDoc30InvalidateTickets.setStatus('current')
mibBuilder.exportSymbols("ARRIS-MTA-DOC30-DEVICE-MIB", arrisMtaDoc30MibObjects=arrisMtaDoc30MibObjects, arrisMtaDoc30EmergencyNumber=arrisMtaDoc30EmergencyNumber, arrisMtaDoc30AdjustCallpFeatureSwitch=arrisMtaDoc30AdjustCallpFeatureSwitch, arrisMtaDoc30RootCertType=arrisMtaDoc30RootCertType, arrisMtaDoc30Base=arrisMtaDoc30Base, PYSNMP_MODULE_ID=arrisMtaDoc30Mib, arrisMtaDoc30Mib=arrisMtaDoc30Mib, arrisMtaDoc30Setup=arrisMtaDoc30Setup, arrisMtaDoc30InvalidateTickets=arrisMtaDoc30InvalidateTickets)
