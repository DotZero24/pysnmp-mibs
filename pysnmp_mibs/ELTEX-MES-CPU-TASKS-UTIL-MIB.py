#
# PySNMP MIB module ELTEX-MES-CPU-TASKS-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-CPU-TASKS-UTIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesCpuTasksUtilMIB, = mibBuilder.importSymbols("ELTEX-MES-MNG-MIB", "eltMesCpuTasksUtilMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-CPU-TASKS-UTIL-MIB", eltCpuTasksUtilEnable=eltCpuTasksUtilEnable, eltMesCpuTasksUtilObjects=eltMesCpuTasksUtilObjects, eltCpuTasksUtilStatisticsTable=eltCpuTasksUtilStatisticsTable, eltCpuTasksUtilStatisticsTaskName=eltCpuTasksUtilStatisticsTaskName, eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds=eltCpuTasksUtilStatisticsUtilizationDuringLast5Seconds, eltCpuTasksUtilStatisticsTaskIndex=eltCpuTasksUtilStatisticsTaskIndex, eltCpuTasksUtilStatisticsEntry=eltCpuTasksUtilStatisticsEntry, eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes=eltCpuTasksUtilStatisticsUtilizationDuringLast5Minutes, eltMesCpuTasksUtilStatistics=eltMesCpuTasksUtilStatistics, eltMesCpuTasksUtilConfig=eltMesCpuTasksUtilConfig, eltCpuTasksUtilStatisticsUtilizationDuringLastMinute=eltCpuTasksUtilStatisticsUtilizationDuringLastMinute)
