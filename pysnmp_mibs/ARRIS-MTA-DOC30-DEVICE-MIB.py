#
# PySNMP MIB module ARRIS-MTA-DOC30-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/arris/ARRIS-MTA-DOC30-DEVICE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
arrisProdIdCM, = mibBuilder.importSymbols("ARRIS-MIB", "arrisProdIdCM")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DateAndTime, TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
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
mibBuilder.exportSymbols("ARRIS-MTA-DOC30-DEVICE-MIB", arrisMtaDoc30RootCertType=arrisMtaDoc30RootCertType, arrisMtaDoc30Base=arrisMtaDoc30Base, PYSNMP_MODULE_ID=arrisMtaDoc30Mib, arrisMtaDoc30AdjustCallpFeatureSwitch=arrisMtaDoc30AdjustCallpFeatureSwitch, arrisMtaDoc30InvalidateTickets=arrisMtaDoc30InvalidateTickets, arrisMtaDoc30EmergencyNumber=arrisMtaDoc30EmergencyNumber, arrisMtaDoc30Mib=arrisMtaDoc30Mib, arrisMtaDoc30Setup=arrisMtaDoc30Setup, arrisMtaDoc30MibObjects=arrisMtaDoc30MibObjects)
