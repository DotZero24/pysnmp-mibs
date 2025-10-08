#
# PySNMP MIB module SL-TRAP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/smartoptics/SL-TRAP-OPT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
slAlarmServiceAffect, slAlarmSeverity, slAlarmIfIndex, slAlarmActive, slAlarmType = mibBuilder.importSymbols("SL-ALARM-MIB", "slAlarmServiceAffect", "slAlarmSeverity", "slAlarmIfIndex", "slAlarmActive", "slAlarmType")
slEventIfIndex, slEventType, slEventUser, slEventVal = mibBuilder.importSymbols("SL-EVENT-MIB", "slEventIfIndex", "slEventType", "slEventUser", "slEventVal")
smartoptics, = mibBuilder.importSymbols("SL-NE-MIB", "smartoptics")
optApsConfigActiveConnectionRx, optApsConfigUserWorkingIndex = mibBuilder.importSymbols("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx", "optApsConfigUserWorkingIndex")
slTestsTrapsLoopbackActive, slTestsIfLoopIfIndex, slTestsIfLoopType = mibBuilder.importSymbols("SL-TESTS-MIB", "slTestsTrapsLoopbackActive", "slTestsIfLoopIfIndex", "slTestsIfLoopType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
slAlarmTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,101)).setObjects(("SL-ALARM-MIB", "slAlarmIfIndex"), ("SL-ALARM-MIB", "slAlarmType"), ("SL-ALARM-MIB", "slAlarmSeverity"), ("SL-ALARM-MIB", "slAlarmServiceAffect"), ("SL-ALARM-MIB", "slAlarmActive"))
optApsTrapSwitchoverV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,102)).setObjects(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"), ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
slTestsTrapsLoopbackTableChangedV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,103)).setObjects(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"), ("SL-TESTS-MIB", "slTestsIfLoopType"), ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
slEventTrapV1 = NotificationType((1, 3, 6, 1, 4, 1, 4515) + (0,104)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
mibBuilder.exportSymbols("SL-TRAP-OPT-MIB", slEventTrapV1=slEventTrapV1, optApsTrapSwitchoverV1=optApsTrapSwitchoverV1, slTestsTrapsLoopbackTableChangedV1=slTestsTrapsLoopbackTableChangedV1, slAlarmTrapV1=slAlarmTrapV1)
