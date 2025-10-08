#
# PySNMP MIB module TPLINK-AUTOINSTALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-AUTOINSTALL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:08 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TPLINK-AUTOINSTALL-MIB", autoInstallRetryCount=autoInstallRetryCount, autoInstallAutoReboot=autoInstallAutoReboot, tplinkAutoInstallMIB=tplinkAutoInstallMIB, PYSNMP_MODULE_ID=tplinkAutoInstallMIB, autoInstallState=autoInstallState, tplinkAutoInstallNotifications=tplinkAutoInstallNotifications, autoInstallPersistentMode=autoInstallPersistentMode, autoInstallAutoSave=autoInstallAutoSave, autoInstallConfig=autoInstallConfig, autoInstallStartStop=autoInstallStartStop, tplinkAutoInstallMIBObjects=tplinkAutoInstallMIBObjects)
