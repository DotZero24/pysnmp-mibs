#
# PySNMP MIB module MBG-SNMP-NTP-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/meinberg/MBG-SNMP-NTP-DISPLAY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:35 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mbgNtpDisp = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20))
mbgNtpDispInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20, 2))
mbgNtpDispTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 20, 3))
mbgNtpDispClockType = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispClockType.setStatus('mandatory')
mbgNtpDispClockTypeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispClockTypeVal.setStatus('mandatory')
mbgNtpDispMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispMode.setStatus('mandatory')
mbgNtpDispModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispModeVal.setStatus('mandatory')
mbgNtpDispState = MibScalar((1, 3, 6, 1, 4, 1, 5597, 20, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgNtpDispState.setStatus('mandatory')
mbgNtpDispTrapBoot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,1))
mbgNtpDispTrapSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,2))
mbgNtpDispTrapNotSync = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,3))
mbgNtpDispTrapTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 5597, 20, 3) + (0,4))
mibBuilder.exportSymbols("MBG-SNMP-NTP-DISPLAY-MIB", mbgNtpDispTrapTestNotification=mbgNtpDispTrapTestNotification, mbgNtpDispTrapBoot=mbgNtpDispTrapBoot, mbgNtpDispState=mbgNtpDispState, mbgNtpDispModeVal=mbgNtpDispModeVal, mbgNtpDispInfo=mbgNtpDispInfo, mbgNtpDispTraps=mbgNtpDispTraps, mbgNtpDispMode=mbgNtpDispMode, mbgNtpDispTrapSync=mbgNtpDispTrapSync, mbgNtpDispClockType=mbgNtpDispClockType, mbgNtpDisp=mbgNtpDisp, mbgNtpDispClockTypeVal=mbgNtpDispClockTypeVal, mbgNtpDispTrapNotSync=mbgNtpDispTrapNotSync)
