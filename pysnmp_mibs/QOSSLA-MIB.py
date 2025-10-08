#
# PySNMP MIB module QOSSLA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/QOSSLA-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("QOSSLA-MIB", nnqosSLAMib=nnqosSLAMib, nnqosSlaEffectType=nnqosSlaEffectType, nnqosSLANotification=nnqosSLANotification, nnqosSLANotificationsVars=nnqosSLANotificationsVars, nnqosSlaThresholdType=nnqosSlaThresholdType, PYSNMP_MODULE_ID=nnqosSLAMib, nnqosSlaThresholdValue2=nnqosSlaThresholdValue2, nnqosSLATraps=nnqosSLATraps, nnqosNotificationGroup=nnqosNotificationGroup, nnqosSlaThresholdValue1=nnqosSlaThresholdValue1, nnqosSLANotifications=nnqosSLANotifications, nnqosSlaIndex=nnqosSlaIndex)
