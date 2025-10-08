#
# PySNMP MIB module WESTERMO-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/westermo/WESTERMO-TRAP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WESTERMO-TRAP-MIB", notifyWarning=notifyWarning, rtTrapCompliances=rtTrapCompliances, rtTrapGroups=rtTrapGroups, notifyCritical=notifyCritical, rtTrapConformance=rtTrapConformance, PYSNMP_MODULE_ID=notification, notifyEmergency=notifyEmergency, rttrapCompliance=rttrapCompliance, rtTrapMsgGroup=rtTrapMsgGroup, notification=notification, trapMsgString=trapMsgString, notifyAlert=notifyAlert, rtTraps=rtTraps, rtTrapMsg=rtTrapMsg, notifyNotice=notifyNotice, rtTrapGroup=rtTrapGroup, notifyError=notifyError, notifyInfo=notifyInfo)
