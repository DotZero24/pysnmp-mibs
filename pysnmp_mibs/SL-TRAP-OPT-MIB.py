# SNMP MIB module (SL-TRAP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-TRAP-OPT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:09 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(slAlarmActive,
 slAlarmIfIndex,
 slAlarmServiceAffect,
 slAlarmSeverity,
 slAlarmType) = mibBuilder.importSymbols(
    "SL-ALARM-MIB",
    "slAlarmActive",
    "slAlarmIfIndex",
    "slAlarmServiceAffect",
    "slAlarmSeverity",
    "slAlarmType")

(slEventIfIndex,
 slEventType,
 slEventUser,
 slEventVal) = mibBuilder.importSymbols(
    "SL-EVENT-MIB",
    "slEventIfIndex",
    "slEventType",
    "slEventUser",
    "slEventVal")

(smartoptics,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "smartoptics")

(optApsConfigActiveConnectionRx,
 optApsConfigUserWorkingIndex) = mibBuilder.importSymbols(
    "SL-OPT-APS-MIB",
    "optApsConfigActiveConnectionRx",
    "optApsConfigUserWorkingIndex")

(slTestsIfLoopIfIndex,
 slTestsIfLoopType,
 slTestsTrapsLoopbackActive) = mibBuilder.importSymbols(
    "SL-TESTS-MIB",
    "slTestsIfLoopIfIndex",
    "slTestsIfLoopType",
    "slTestsTrapsLoopbackActive")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

slAlarmTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 101)
)
slAlarmTrapV1.setObjects(
      *(("SL-ALARM-MIB", "slAlarmIfIndex"),
        ("SL-ALARM-MIB", "slAlarmType"),
        ("SL-ALARM-MIB", "slAlarmSeverity"),
        ("SL-ALARM-MIB", "slAlarmServiceAffect"),
        ("SL-ALARM-MIB", "slAlarmActive"))
)
if mibBuilder.loadTexts:
    slAlarmTrapV1.setStatus(
        ""
    )

optApsTrapSwitchoverV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 102)
)
optApsTrapSwitchoverV1.setObjects(
      *(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
        ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
)
if mibBuilder.loadTexts:
    optApsTrapSwitchoverV1.setStatus(
        ""
    )

slTestsTrapsLoopbackTableChangedV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 103)
)
slTestsTrapsLoopbackTableChangedV1.setObjects(
      *(("SL-TESTS-MIB", "slTestsIfLoopIfIndex"),
        ("SL-TESTS-MIB", "slTestsIfLoopType"),
        ("SL-TESTS-MIB", "slTestsTrapsLoopbackActive"))
)
if mibBuilder.loadTexts:
    slTestsTrapsLoopbackTableChangedV1.setStatus(
        ""
    )

slEventTrapV1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 0, 104)
)
slEventTrapV1.setObjects(
      *(("SL-EVENT-MIB", "slEventIfIndex"),
        ("SL-EVENT-MIB", "slEventType"),
        ("SL-EVENT-MIB", "slEventVal"),
        ("SL-EVENT-MIB", "slEventUser"))
)
if mibBuilder.loadTexts:
    slEventTrapV1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-TRAP-OPT-MIB",
    **{"slAlarmTrapV1": slAlarmTrapV1,
       "optApsTrapSwitchoverV1": optApsTrapSwitchoverV1,
       "slTestsTrapsLoopbackTableChangedV1": slTestsTrapsLoopbackTableChangedV1,
       "slEventTrapV1": slEventTrapV1}
)
