#
# PySNMP MIB module ELECTROLINE-DHT-REMOTE-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-REMOTE-SWITCH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:43:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dhtExtensionsMibObjects, = mibBuilder.importSymbols("ELECTROLINE-DHT-EXTENSIONS-MIB", "dhtExtensionsMibObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
dhtRemoteSwitchMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11))
dhtRemoteSwitchMib.setRevisions(('2004-12-10 00:00',))
if mibBuilder.loadTexts: dhtRemoteSwitchMib.setLastUpdated('200412100000Z')
if mibBuilder.loadTexts: dhtRemoteSwitchMib.setOrganization('Electroline Equipment Inc')
dhtRemoteSwitchObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1))
dhtRemoteSwitchPresence = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtRemoteSwitchPresence.setStatus('current')
dhtRemoteSwitchManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11))
dhtRemoteSwitchControl = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtRemoteSwitchControl.setStatus('current')
dhtRemoteSwitchAutoStopTimer = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtRemoteSwitchAutoStopTimer.setStatus('current')
dhtRemoteSwitchStatus = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("mismatch", 3), ("timeout", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhtRemoteSwitchStatus.setStatus('current')
dhtRemoteSwitchOnTime = MibScalar((1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 11, 1, 11, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhtRemoteSwitchOnTime.setStatus('current')
mibBuilder.exportSymbols("ELECTROLINE-DHT-REMOTE-SWITCH-MIB", dhtRemoteSwitchObjects=dhtRemoteSwitchObjects, dhtRemoteSwitchPresence=dhtRemoteSwitchPresence, dhtRemoteSwitchControl=dhtRemoteSwitchControl, dhtRemoteSwitchOnTime=dhtRemoteSwitchOnTime, dhtRemoteSwitchMib=dhtRemoteSwitchMib, dhtRemoteSwitchStatus=dhtRemoteSwitchStatus, dhtRemoteSwitchAutoStopTimer=dhtRemoteSwitchAutoStopTimer, PYSNMP_MODULE_ID=dhtRemoteSwitchMib, dhtRemoteSwitchManagement=dhtRemoteSwitchManagement)
