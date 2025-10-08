#
# PySNMP MIB module TPLINK-AUTOINSTALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-AUTOINSTALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkAutoInstallMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 97))
tplinkAutoInstallMIB.setRevisions(('2012-12-17 10:14',))
if mibBuilder.loadTexts: tplinkAutoInstallMIB.setLastUpdated('201212171014Z')
if mibBuilder.loadTexts: tplinkAutoInstallMIB.setOrganization('TPLINK')
tplinkAutoInstallMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1))
tplinkAutoInstallNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 97, 2))
autoInstallConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1))
autoInstallStartStop = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("stop", 0), ("start", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: autoInstallStartStop.setStatus('current')
autoInstallPersistentMode = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: autoInstallPersistentMode.setStatus('current')
autoInstallAutoSave = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: autoInstallAutoSave.setStatus('current')
autoInstallAutoReboot = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: autoInstallAutoReboot.setStatus('current')
autoInstallRetryCount = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: autoInstallRetryCount.setStatus('current')
autoInstallState = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 97, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: autoInstallState.setStatus('current')
mibBuilder.exportSymbols("TPLINK-AUTOINSTALL-MIB", autoInstallState=autoInstallState, PYSNMP_MODULE_ID=tplinkAutoInstallMIB, autoInstallRetryCount=autoInstallRetryCount, tplinkAutoInstallMIB=tplinkAutoInstallMIB, autoInstallStartStop=autoInstallStartStop, autoInstallAutoSave=autoInstallAutoSave, autoInstallPersistentMode=autoInstallPersistentMode, autoInstallAutoReboot=autoInstallAutoReboot, autoInstallConfig=autoInstallConfig, tplinkAutoInstallMIBObjects=tplinkAutoInstallMIBObjects, tplinkAutoInstallNotifications=tplinkAutoInstallNotifications)
