#
# PySNMP MIB module ELTEX-MES-CPU-TASKS-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-CPU-TASKS-UTIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesCpuTasksUtilMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesCpuTasksUtilMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltMesCpuTasksUtilObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1))
eltMesCpuTasksUtilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 1))
eltMesCpuTasksUtilStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2))
eltCpuTasksUtilEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltCpuTasksUtilEnable.setStatus('current')
eltCpuTasksUtilStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1), )
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsTable.setStatus('current')
eltCpuTasksUtilStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1), ).setIndexNames((0, "ELTEX-MES-CPU-TASKS-UTIL-MIB", "eltCpuTasksUtilStatisticsTaskIndex"))
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsEntry.setStatus('current')
eltCpuTasksUtilStatisticsTaskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsTaskIndex.setStatus('current')
eltCpuTasksUtilStatisticsTaskName = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsTaskName.setStatus('current')
eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds.setStatus('current')
eltCpuTasksUtilStatisticsUtilizationDuringLastMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsUtilizationDuringLastMinute.setStatus('current')
eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-CPU-TASKS-UTIL-MIB", eltCpuTasksUtilStatisticsUtilizationDuringLastMinute=eltCpuTasksUtilStatisticsUtilizationDuringLastMinute, eltMesCpuTasksUtilStatistics=eltMesCpuTasksUtilStatistics, eltMesCpuTasksUtilObjects=eltMesCpuTasksUtilObjects, eltCpuTasksUtilStatisticsTaskIndex=eltCpuTasksUtilStatisticsTaskIndex, eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds=eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds, eltCpuTasksUtilStatisticsEntry=eltCpuTasksUtilStatisticsEntry, eltCpuTasksUtilStatisticsTaskName=eltCpuTasksUtilStatisticsTaskName, eltCpuTasksUtilStatisticsTable=eltCpuTasksUtilStatisticsTable, eltMesCpuTasksUtilConfig=eltMesCpuTasksUtilConfig, eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes=eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes, eltCpuTasksUtilEnable=eltCpuTasksUtilEnable)
