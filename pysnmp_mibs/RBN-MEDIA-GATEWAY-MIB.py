#
# PySNMP MIB module RBN-MEDIA-GATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-MEDIA-GATEWAY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:54 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
IANAItuProbableCause, IANAItuEventType = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuProbableCause", "IANAItuEventType")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
rbnMediaGatewayMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 52))
rbnMediaGatewayMib.setRevisions(('2010-04-19 00:00', '2009-09-30 00:00',))
if mibBuilder.loadTexts: rbnMediaGatewayMib.setLastUpdated('201004190000Z')
if mibBuilder.loadTexts: rbnMediaGatewayMib.setOrganization('Ericsson Inc.')
rbnMediaGatewayNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 0))
rbnMediaGatewayObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1))
rbnMediaGatewayConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2))
rbnMediaGatewayNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1))
rbnMGEventDateAndTime = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 1), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventDateAndTime.setStatus('current')
rbnMGEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 2), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventSeverity.setStatus('current')
rbnMGEventSender = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventSender.setStatus('current')
rbnMGEventType = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 4), IANAItuEventType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventType.setStatus('current')
rbnMGEventProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 5), IANAItuProbableCause()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventProbableCause.setStatus('current')
rbnMGEventInformation = MibScalar((1, 3, 6, 1, 4, 1, 2352, 2, 52, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: rbnMGEventInformation.setStatus('current')
rbnH248LinkStatusAlarm = NotificationType((1, 3, 6, 1, 4, 1, 2352, 2, 52, 0, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
if mibBuilder.loadTexts: rbnH248LinkStatusAlarm.setStatus('current')
rbnMediaGatewayCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1))
rbnMediaGatewayGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2))
rbnMGCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 1, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGNotifyObjectGroup"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGLinkNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGCompliance = rbnMGCompliance.setStatus('current')
rbnMGNotifyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 1)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventDateAndTime"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSeverity"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventSender"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventType"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventProbableCause"), ("RBN-MEDIA-GATEWAY-MIB", "rbnMGEventInformation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGNotifyObjectGroup = rbnMGNotifyObjectGroup.setStatus('current')
rbnMGLinkNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2352, 2, 52, 2, 2, 2)).setObjects(("RBN-MEDIA-GATEWAY-MIB", "rbnH248LinkStatusAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnMGLinkNotifyGroup = rbnMGLinkNotifyGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-MEDIA-GATEWAY-MIB", rbnMediaGatewayConformance=rbnMediaGatewayConformance, PYSNMP_MODULE_ID=rbnMediaGatewayMib, rbnMGNotifyObjectGroup=rbnMGNotifyObjectGroup, rbnMediaGatewayMib=rbnMediaGatewayMib, rbnMediaGatewayNotify=rbnMediaGatewayNotify, rbnMGCompliance=rbnMGCompliance, rbnMGLinkNotifyGroup=rbnMGLinkNotifyGroup, rbnMediaGatewayNotifications=rbnMediaGatewayNotifications, rbnMGEventType=rbnMGEventType, rbnMediaGatewayObjects=rbnMediaGatewayObjects, rbnMGEventInformation=rbnMGEventInformation, rbnH248LinkStatusAlarm=rbnH248LinkStatusAlarm, rbnMediaGatewayGroups=rbnMediaGatewayGroups, rbnMGEventSender=rbnMGEventSender, rbnMGEventDateAndTime=rbnMGEventDateAndTime, rbnMGEventProbableCause=rbnMGEventProbableCause, rbnMGEventSeverity=rbnMGEventSeverity, rbnMediaGatewayCompliances=rbnMediaGatewayCompliances)
