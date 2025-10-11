# SNMP MIB module (SL-SONET-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-SONET-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:26 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slSonetMib,) = mibBuilder.importSymbols(
    "SL-SONET-MIB",
    "slSonetMib")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slSonetAlarmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SonetAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("losSonetAlarm", 1),
          ("lofSonetAlarm", 2),
          ("lopSonetAlarm", 3),
          ("aisSonetAlarm", 4),
          ("rfiSonetAlarm", 5),
          ("uneqSonetAlarm", 6),
          ("tim", 7),
          ("slm", 8),
          ("sd", 9),
          ("sf", 10),
          ("hwfail", 11))
    )



# MIB Managed Objects in the order of their OIDs

_SlSonetAlarmConfig_ObjectIdentity = ObjectIdentity
slSonetAlarmConfig = _SlSonetAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1)
)
_SlSonetAlarmConfigTable_Object = MibTable
slSonetAlarmConfigTable = _SlSonetAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    slSonetAlarmConfigTable.setStatus("current")
_SlSonetAlarmConfigEntry_Object = MibTableRow
slSonetAlarmConfigEntry = _SlSonetAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1)
)
slSonetAlarmConfigEntry.setIndexNames(
    (0, "SL-SONET-ALARM-MIB", "slSonetAlarmIfIndex"),
    (0, "SL-SONET-ALARM-MIB", "slSonetAlarmType"),
)
if mibBuilder.loadTexts:
    slSonetAlarmConfigEntry.setStatus("current")
_SlSonetAlarmIfIndex_Type = InterfaceIndex
_SlSonetAlarmIfIndex_Object = MibTableColumn
slSonetAlarmIfIndex = _SlSonetAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 1),
    _SlSonetAlarmIfIndex_Type()
)
slSonetAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetAlarmIfIndex.setStatus("current")
_SlSonetAlarmType_Type = SonetAlarmType
_SlSonetAlarmType_Object = MibTableColumn
slSonetAlarmType = _SlSonetAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 2),
    _SlSonetAlarmType_Type()
)
slSonetAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetAlarmType.setStatus("current")
_SlSonetAlarmMask_Type = TruthValue
_SlSonetAlarmMask_Object = MibTableColumn
slSonetAlarmMask = _SlSonetAlarmMask_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 3),
    _SlSonetAlarmMask_Type()
)
slSonetAlarmMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetAlarmMask.setStatus("current")
_SlSonetAlarmStatus_Type = TruthValue
_SlSonetAlarmStatus_Object = MibTableColumn
slSonetAlarmStatus = _SlSonetAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 1, 1, 1, 4),
    _SlSonetAlarmStatus_Type()
)
slSonetAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetAlarmStatus.setStatus("current")
_SlSonetAlarmTraps_ObjectIdentity = ObjectIdentity
slSonetAlarmTraps = _SlSonetAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2)
)


class _SlSonetAlarmSeverity_Type(Integer32):
    """Custom type slSonetAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_SlSonetAlarmSeverity_Type.__name__ = "Integer32"
_SlSonetAlarmSeverity_Object = MibScalar
slSonetAlarmSeverity = _SlSonetAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 1),
    _SlSonetAlarmSeverity_Type()
)
slSonetAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetAlarmSeverity.setStatus("current")
_SlSonetAlarmServiceAffect_Type = TruthValue
_SlSonetAlarmServiceAffect_Object = MibScalar
slSonetAlarmServiceAffect = _SlSonetAlarmServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 2),
    _SlSonetAlarmServiceAffect_Type()
)
slSonetAlarmServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetAlarmServiceAffect.setStatus("current")

# Managed Objects groups


# Notification objects

slSonetAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 4, 2, 3)
)
slSonetAlarmTrap.setObjects(
      *(("SL-SONET-ALARM-MIB", "slSonetAlarmIfIndex"),
        ("SL-SONET-ALARM-MIB", "slSonetAlarmType"),
        ("SL-SONET-ALARM-MIB", "slSonetAlarmStatus"),
        ("SL-SONET-ALARM-MIB", "slSonetAlarmSeverity"),
        ("SL-SONET-ALARM-MIB", "slSonetAlarmServiceAffect"))
)
if mibBuilder.loadTexts:
    slSonetAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SONET-ALARM-MIB",
    **{"SonetAlarmType": SonetAlarmType,
       "slSonetAlarmMib": slSonetAlarmMib,
       "slSonetAlarmConfig": slSonetAlarmConfig,
       "slSonetAlarmConfigTable": slSonetAlarmConfigTable,
       "slSonetAlarmConfigEntry": slSonetAlarmConfigEntry,
       "slSonetAlarmIfIndex": slSonetAlarmIfIndex,
       "slSonetAlarmType": slSonetAlarmType,
       "slSonetAlarmMask": slSonetAlarmMask,
       "slSonetAlarmStatus": slSonetAlarmStatus,
       "slSonetAlarmTraps": slSonetAlarmTraps,
       "slSonetAlarmSeverity": slSonetAlarmSeverity,
       "slSonetAlarmServiceAffect": slSonetAlarmServiceAffect,
       "slSonetAlarmTrap": slSonetAlarmTrap}
)
