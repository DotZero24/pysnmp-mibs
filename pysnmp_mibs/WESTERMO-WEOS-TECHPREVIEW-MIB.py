#
# PySNMP MIB module WESTERMO-WEOS-TECHPREVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/westermo/WESTERMO-WEOS-TECHPREVIEW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
otherNotificationPrefix, = mibBuilder.importSymbols("WESTERMO-WEOS-MIB", "otherNotificationPrefix")
remoteTriggerSet = NotificationType((1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7, 0, 1)).setObjects(("WESTERMO-WEOS-TECHPREVIEW-MIB", "remoteTriggerStatus"))
if mibBuilder.loadTexts: remoteTriggerSet.setStatus('current')
remoteTriggerTimeout = NotificationType((1, 3, 6, 1, 4, 1, 16177, 2, 1, 6, 7, 0, 2)).setObjects(("WESTERMO-WEOS-TECHPREVIEW-MIB", "remoteTriggerStatus"))
if mibBuilder.loadTexts: remoteTriggerTimeout.setStatus('current')
mibBuilder.exportSymbols("WESTERMO-WEOS-TECHPREVIEW-MIB", remoteTriggerSet=remoteTriggerSet, remoteTriggerTimeout=remoteTriggerTimeout)
