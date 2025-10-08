#
# PySNMP MIB module QOSSLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/QOSSLA-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
nnqosSLAMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24))
nnqosSLAMib.setRevisions(('1900-08-18 00:00',))
if mibBuilder.loadTexts: nnqosSLAMib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: nnqosSLAMib.setOrganization('Nortel Networks')
nnqosSLANotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1))
nnqosSLANotificationsVars = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2))
nnqosSLATraps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1, 0))
nnqosSlaIndex = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnqosSlaIndex.setStatus('current')
nnqosSlaThresholdType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("average", 1), ("immediate", 2), ("consecutive", 3), ("xofy", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnqosSlaThresholdType.setStatus('current')
nnqosSlaEffectType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("jitterAvg", 1), ("jitterAvgSrcDest", 2), ("jitterAvgDestSrc", 3), ("jitterMaxPosSrcDest", 4), ("jitterMaxPosDestSrc", 5), ("jitterMaxNegSrcDest", 6), ("jitterMaxNegDestSrc", 7), ("delayAvg", 8), ("delayAvgSrcDest", 9), ("delayAvgDestSrc", 10), ("delayMaxSrcDest", 11), ("delayMaxDestSrc", 12), ("packetLoss", 13), ("packetOutOfOrder", 14), ("packetLateArrival", 15), ("responseTime", 16), ("timeout", 17)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnqosSlaEffectType.setStatus('current')
nnqosSlaThresholdValue1 = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 4), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnqosSlaThresholdValue1.setStatus('current')
nnqosSlaThresholdValue2 = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnqosSlaThresholdValue2.setStatus('current')
nnqosSLANotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1, 0, 1)).setObjects(("QOSSLA-MIB", "nnqosSlaIndex"), ("QOSSLA-MIB", "nnqosSlaThresholdType"), ("QOSSLA-MIB", "nnqosSlaEffectType"), ("QOSSLA-MIB", "nnqosSlaThresholdValue1"), ("QOSSLA-MIB", "nnqosSlaThresholdValue2"))
if mibBuilder.loadTexts: nnqosSLANotification.setStatus('current')
nnqosNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 3)).setObjects(("QOSSLA-MIB", "nnqosSLANotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nnqosNotificationGroup = nnqosNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("QOSSLA-MIB", nnqosSLATraps=nnqosSLATraps, nnqosSlaIndex=nnqosSlaIndex, nnqosSLANotifications=nnqosSLANotifications, nnqosSLANotificationsVars=nnqosSLANotificationsVars, nnqosSlaThresholdType=nnqosSlaThresholdType, nnqosSlaThresholdValue1=nnqosSlaThresholdValue1, nnqosSLAMib=nnqosSLAMib, nnqosSLANotification=nnqosSLANotification, nnqosNotificationGroup=nnqosNotificationGroup, PYSNMP_MODULE_ID=nnqosSLAMib, nnqosSlaEffectType=nnqosSlaEffectType, nnqosSlaThresholdValue2=nnqosSlaThresholdValue2)
