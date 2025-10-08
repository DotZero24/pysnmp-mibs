#
# PySNMP MIB module WESTERMO-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/westermo/WESTERMO-TRAP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
notification = ModuleIdentity((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200))
notification.setRevisions(('2019-09-06 00:00',))
if mibBuilder.loadTexts: notification.setLastUpdated('201909060000Z')
if mibBuilder.loadTexts: notification.setOrganization('Westermo Teleindustri AB')
rtTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0))
rtTrapMsg = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 1))
rtTrapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3))
rtTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1))
rtTrapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 2))
trapMsgString = MibScalar((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: trapMsgString.setStatus('current')
notifyEmergency = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 1)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyEmergency.setStatus('current')
notifyAlert = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 2)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyAlert.setStatus('current')
notifyCritical = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 3)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyCritical.setStatus('current')
notifyError = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 4)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyError.setStatus('current')
notifyWarning = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 5)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyWarning.setStatus('current')
notifyNotice = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 6)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyNotice.setStatus('current')
notifyInfo = NotificationType((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 0, 7)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if mibBuilder.loadTexts: notifyInfo.setStatus('current')
rtTrapMsgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1, 1)).setObjects(("WESTERMO-TRAP-MIB", "trapMsgString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtTrapMsgGroup = rtTrapMsgGroup.setStatus('current')
rtTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 1, 2)).setObjects(("WESTERMO-TRAP-MIB", "notifyEmergency"), ("WESTERMO-TRAP-MIB", "notifyAlert"), ("WESTERMO-TRAP-MIB", "notifyCritical"), ("WESTERMO-TRAP-MIB", "notifyError"), ("WESTERMO-TRAP-MIB", "notifyWarning"), ("WESTERMO-TRAP-MIB", "notifyNotice"), ("WESTERMO-TRAP-MIB", "notifyInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rtTrapGroup = rtTrapGroup.setStatus('current')
rttrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 16177, 1, 400, 200, 3, 2, 1)).setObjects(("WESTERMO-TRAP-MIB", "rtTrapMsgGroup"), ("WESTERMO-TRAP-MIB", "rtTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rttrapCompliance = rttrapCompliance.setStatus('current')
mibBuilder.exportSymbols("WESTERMO-TRAP-MIB", notifyError=notifyError, notifyWarning=notifyWarning, rtTrapGroup=rtTrapGroup, notifyAlert=notifyAlert, rtTrapMsgGroup=rtTrapMsgGroup, rtTrapCompliances=rtTrapCompliances, PYSNMP_MODULE_ID=notification, rtTrapMsg=rtTrapMsg, notifyEmergency=notifyEmergency, rtTrapConformance=rtTrapConformance, rttrapCompliance=rttrapCompliance, notifyNotice=notifyNotice, rtTrapGroups=rtTrapGroups, notification=notification, trapMsgString=trapMsgString, rtTraps=rtTraps, notifyCritical=notifyCritical, notifyInfo=notifyInfo)
