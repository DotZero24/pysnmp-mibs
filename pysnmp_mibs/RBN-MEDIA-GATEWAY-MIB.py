#
# PySNMP MIB module RBN-MEDIA-GATEWAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-MEDIA-GATEWAY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
IANAItuEventType, IANAItuProbableCause = mibBuilder.importSymbols("IANA-ITU-ALARM-TC-MIB", "IANAItuEventType", "IANAItuProbableCause")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-MEDIA-GATEWAY-MIB", rbnH248LinkStatusAlarm=rbnH248LinkStatusAlarm, rbnMediaGatewayCompliances=rbnMediaGatewayCompliances, rbnMGCompliance=rbnMGCompliance, rbnMGLinkNotifyGroup=rbnMGLinkNotifyGroup, rbnMGEventDateAndTime=rbnMGEventDateAndTime, rbnMGEventProbableCause=rbnMGEventProbableCause, rbnMediaGatewayNotifications=rbnMediaGatewayNotifications, rbnMediaGatewayGroups=rbnMediaGatewayGroups, rbnMediaGatewayConformance=rbnMediaGatewayConformance, rbnMediaGatewayObjects=rbnMediaGatewayObjects, rbnMediaGatewayNotify=rbnMediaGatewayNotify, rbnMGEventSeverity=rbnMGEventSeverity, rbnMediaGatewayMib=rbnMediaGatewayMib, rbnMGEventInformation=rbnMGEventInformation, rbnMGEventSender=rbnMGEventSender, PYSNMP_MODULE_ID=rbnMediaGatewayMib, rbnMGNotifyObjectGroup=rbnMGNotifyObjectGroup, rbnMGEventType=rbnMGEventType)
