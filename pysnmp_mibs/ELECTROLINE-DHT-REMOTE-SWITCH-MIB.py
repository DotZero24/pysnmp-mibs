#
# PySNMP MIB module ELECTROLINE-DHT-REMOTE-SWITCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/electroline/ELECTROLINE-DHT-REMOTE-SWITCH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dhtExtensionsMibObjects, = mibBuilder.importSymbols("ELECTROLINE-DHT-EXTENSIONS-MIB", "dhtExtensionsMibObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("ELECTROLINE-DHT-REMOTE-SWITCH-MIB", dhtRemoteSwitchOnTime=dhtRemoteSwitchOnTime, dhtRemoteSwitchObjects=dhtRemoteSwitchObjects, dhtRemoteSwitchAutoStopTimer=dhtRemoteSwitchAutoStopTimer, dhtRemoteSwitchMib=dhtRemoteSwitchMib, dhtRemoteSwitchPresence=dhtRemoteSwitchPresence, dhtRemoteSwitchManagement=dhtRemoteSwitchManagement, dhtRemoteSwitchControl=dhtRemoteSwitchControl, PYSNMP_MODULE_ID=dhtRemoteSwitchMib, dhtRemoteSwitchStatus=dhtRemoteSwitchStatus)
