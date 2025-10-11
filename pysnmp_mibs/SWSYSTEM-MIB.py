# SNMP MIB module (SWSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/SWSYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:01:56 2025
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

(SwPortIndex,
 SwSensorIndex) = mibBuilder.importSymbols(
    "Brocade-TC",
    "SwPortIndex",
    "SwSensorIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sw,) = mibBuilder.importSymbols(
    "SWBASE-MIB",
    "sw")


# MODULE-IDENTITY

swSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    swSystem.setRevisions(
        ("2019-03-20 17:00",
         "2018-07-26 21:00",
         "1911-04-15 18:30",
         "1912-04-30 18:00",
         "1916-09-23 10:30")
    )


# Types definitions



class SwFwEvent(Integer32):
    """Custom type SwFwEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("started", 1),
          ("changed", 2),
          ("exceeded", 3),
          ("below", 4),
          ("above", 5),
          ("inBetween", 6),
          ("lowBufferCrsd", 7))
    )




# TEXTUAL-CONVENTIONS



class FcPortFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("physical", 0),
          ("virtual", 1))
    )


# MIB Managed Objects in the order of their OIDs

_SwTrapsV2_ObjectIdentity = ObjectIdentity
swTrapsV2 = _SwTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    swTrapsV2.setStatus("current")


class _SwCurrentDate_Type(DisplayString):
    """Custom type swCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwCurrentDate_Type.__name__ = "DisplayString"
_SwCurrentDate_Object = MibScalar
swCurrentDate = _SwCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 1),
    _SwCurrentDate_Type()
)
swCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentDate.setStatus("current")


class _SwBootDate_Type(DisplayString):
    """Custom type swBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootDate_Type.__name__ = "DisplayString"
_SwBootDate_Object = MibScalar
swBootDate = _SwBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 2),
    _SwBootDate_Type()
)
swBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootDate.setStatus("current")


class _SwFWLastUpdated_Type(DisplayString):
    """Custom type swFWLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFWLastUpdated_Type.__name__ = "DisplayString"
_SwFWLastUpdated_Object = MibScalar
swFWLastUpdated = _SwFWLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 3),
    _SwFWLastUpdated_Type()
)
swFWLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFWLastUpdated.setStatus("current")


class _SwFlashLastUpdated_Type(DisplayString):
    """Custom type swFlashLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashLastUpdated_Type.__name__ = "DisplayString"
_SwFlashLastUpdated_Object = MibScalar
swFlashLastUpdated = _SwFlashLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 4),
    _SwFlashLastUpdated_Type()
)
swFlashLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashLastUpdated.setStatus("current")


class _SwBootPromLastUpdated_Type(DisplayString):
    """Custom type swBootPromLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootPromLastUpdated_Type.__name__ = "DisplayString"
_SwBootPromLastUpdated_Object = MibScalar
swBootPromLastUpdated = _SwBootPromLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 5),
    _SwBootPromLastUpdated_Type()
)
swBootPromLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootPromLastUpdated.setStatus("current")


class _SwFirmwareVersion_Type(DisplayString):
    """Custom type swFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFirmwareVersion_Type.__name__ = "DisplayString"
_SwFirmwareVersion_Object = MibScalar
swFirmwareVersion = _SwFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 6),
    _SwFirmwareVersion_Type()
)
swFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVersion.setStatus("current")


class _SwOperStatus_Type(Integer32):
    """Custom type swOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_SwOperStatus_Type.__name__ = "Integer32"
_SwOperStatus_Object = MibScalar
swOperStatus = _SwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 7),
    _SwOperStatus_Type()
)
swOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOperStatus.setStatus("current")


class _SwSsn_Type(DisplayString):
    """Custom type swSsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSsn_Type.__name__ = "DisplayString"
_SwSsn_Object = MibScalar
swSsn = _SwSsn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 10),
    _SwSsn_Type()
)
swSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSsn.setStatus("current")


class _SwBeaconOperStatus_Type(Integer32):
    """Custom type swBeaconOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconOperStatus_Type.__name__ = "Integer32"
_SwBeaconOperStatus_Object = MibScalar
swBeaconOperStatus = _SwBeaconOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 18),
    _SwBeaconOperStatus_Type()
)
swBeaconOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconOperStatus.setStatus("current")


class _SwBeaconAdmStatus_Type(Integer32):
    """Custom type swBeaconAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconAdmStatus_Type.__name__ = "Integer32"
_SwBeaconAdmStatus_Object = MibScalar
swBeaconAdmStatus = _SwBeaconAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 19),
    _SwBeaconAdmStatus_Type()
)
swBeaconAdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconAdmStatus.setStatus("current")


class _SwDiagResult_Type(Integer32):
    """Custom type swDiagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sw-ok", 1),
          ("sw-faulty", 2),
          ("sw-embedded-port-fault", 3))
    )


_SwDiagResult_Type.__name__ = "Integer32"
_SwDiagResult_Object = MibScalar
swDiagResult = _SwDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 20),
    _SwDiagResult_Type()
)
swDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDiagResult.setStatus("current")


class _SwNumSensors_Type(Integer32):
    """Custom type swNumSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumSensors_Type.__name__ = "Integer32"
_SwNumSensors_Object = MibScalar
swNumSensors = _SwNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 21),
    _SwNumSensors_Type()
)
swNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumSensors.setStatus("current")
_SwSensorTable_Object = MibTable
swSensorTable = _SwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swSensorTable.setStatus("current")
_SwSensorEntry_Object = MibTableRow
swSensorEntry = _SwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1)
)
swSensorEntry.setIndexNames(
    (0, "SWSYSTEM-MIB", "swSensorIndex"),
)
if mibBuilder.loadTexts:
    swSensorEntry.setStatus("current")
_SwSensorIndex_Type = SwSensorIndex
_SwSensorIndex_Object = MibTableColumn
swSensorIndex = _SwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 1),
    _SwSensorIndex_Type()
)
swSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorIndex.setStatus("current")


class _SwSensorType_Type(Integer32):
    """Custom type swSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("fan", 2),
          ("power-supply", 3))
    )


_SwSensorType_Type.__name__ = "Integer32"
_SwSensorType_Object = MibTableColumn
swSensorType = _SwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 2),
    _SwSensorType_Type()
)
swSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorType.setStatus("current")


class _SwSensorStatus_Type(Integer32):
    """Custom type swSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("faulty", 2),
          ("below-min", 3),
          ("nominal", 4),
          ("above-max", 5),
          ("absent", 6))
    )


_SwSensorStatus_Type.__name__ = "Integer32"
_SwSensorStatus_Object = MibTableColumn
swSensorStatus = _SwSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 3),
    _SwSensorStatus_Type()
)
swSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorStatus.setStatus("current")
_SwSensorValue_Type = Integer32
_SwSensorValue_Object = MibTableColumn
swSensorValue = _SwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 4),
    _SwSensorValue_Type()
)
swSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorValue.setStatus("current")


class _SwSensorInfo_Type(DisplayString):
    """Custom type swSensorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSensorInfo_Type.__name__ = "DisplayString"
_SwSensorInfo_Object = MibTableColumn
swSensorInfo = _SwSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 5),
    _SwSensorInfo_Type()
)
swSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorInfo.setStatus("current")
_SwID_Type = Integer32
_SwID_Object = MibScalar
swID = _SwID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 24),
    _SwID_Type()
)
swID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swID.setStatus("current")
_SwEtherIPAddress_Type = IpAddress
_SwEtherIPAddress_Object = MibScalar
swEtherIPAddress = _SwEtherIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 25),
    _SwEtherIPAddress_Type()
)
swEtherIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPAddress.setStatus("current")
_SwEtherIPMask_Type = IpAddress
_SwEtherIPMask_Object = MibScalar
swEtherIPMask = _SwEtherIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 26),
    _SwEtherIPMask_Type()
)
swEtherIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPMask.setStatus("current")
_SwIPv6Address_Type = DisplayString
_SwIPv6Address_Object = MibScalar
swIPv6Address = _SwIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 29),
    _SwIPv6Address_Type()
)
swIPv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Address.setStatus("current")


class _SwIPv6Status_Type(Integer32):
    """Custom type swIPv6Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("tentative", 1),
          ("preferred", 2),
          ("ipdeprecated", 3),
          ("inactive", 4))
    )


_SwIPv6Status_Type.__name__ = "Integer32"
_SwIPv6Status_Object = MibScalar
swIPv6Status = _SwIPv6Status_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 30),
    _SwIPv6Status_Type()
)
swIPv6Status.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIPv6Status.setStatus("current")
_SwEvent_ObjectIdentity = ObjectIdentity
swEvent = _SwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swEvent.setStatus("current")


class _SwEventTrapLevel_Type(Integer32):
    """Custom type swEventTrapLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SwEventTrapLevel_Type.__name__ = "Integer32"
_SwEventTrapLevel_Object = MibScalar
swEventTrapLevel = _SwEventTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 1),
    _SwEventTrapLevel_Type()
)
swEventTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEventTrapLevel.setStatus("deprecated")


class _SwEventNumEntries_Type(Integer32):
    """Custom type swEventNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventNumEntries_Type.__name__ = "Integer32"
_SwEventNumEntries_Object = MibScalar
swEventNumEntries = _SwEventNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 4),
    _SwEventNumEntries_Type()
)
swEventNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventNumEntries.setStatus("current")
_SwEventTable_Object = MibTable
swEventTable = _SwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    swEventTable.setStatus("current")
_SwEventEntry_Object = MibTableRow
swEventEntry = _SwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1)
)
swEventEntry.setIndexNames(
    (0, "SWSYSTEM-MIB", "swEventIndex"),
)
if mibBuilder.loadTexts:
    swEventEntry.setStatus("current")


class _SwEventIndex_Type(Integer32):
    """Custom type swEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventIndex_Type.__name__ = "Integer32"
_SwEventIndex_Object = MibTableColumn
swEventIndex = _SwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 1),
    _SwEventIndex_Type()
)
swEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventIndex.setStatus("current")


class _SwEventTimeInfo_Type(DisplayString):
    """Custom type swEventTimeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwEventTimeInfo_Type.__name__ = "DisplayString"
_SwEventTimeInfo_Object = MibTableColumn
swEventTimeInfo = _SwEventTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 2),
    _SwEventTimeInfo_Type()
)
swEventTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventTimeInfo.setStatus("current")


class _SwEventLevel_Type(Integer32):
    """Custom type swEventLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SwEventLevel_Type.__name__ = "Integer32"
_SwEventLevel_Object = MibTableColumn
swEventLevel = _SwEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 3),
    _SwEventLevel_Type()
)
swEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventLevel.setStatus("current")


class _SwEventRepeatCount_Type(Integer32):
    """Custom type swEventRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventRepeatCount_Type.__name__ = "Integer32"
_SwEventRepeatCount_Object = MibTableColumn
swEventRepeatCount = _SwEventRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 4),
    _SwEventRepeatCount_Type()
)
swEventRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventRepeatCount.setStatus("current")
_SwEventDescr_Type = DisplayString
_SwEventDescr_Object = MibTableColumn
swEventDescr = _SwEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 5),
    _SwEventDescr_Type()
)
swEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventDescr.setStatus("current")


class _SwEventVfId_Type(Integer32):
    """Custom type swEventVfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwEventVfId_Type.__name__ = "Integer32"
_SwEventVfId_Object = MibTableColumn
swEventVfId = _SwEventVfId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 6),
    _SwEventVfId_Type()
)
swEventVfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventVfId.setStatus("current")
_SwCpuOrMemoryUsage_ObjectIdentity = ObjectIdentity
swCpuOrMemoryUsage = _SwCpuOrMemoryUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    swCpuOrMemoryUsage.setStatus("current")


class _SwCpuUsage_Type(Integer32):
    """Custom type swCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwCpuUsage_Type.__name__ = "Integer32"
_SwCpuUsage_Object = MibScalar
swCpuUsage = _SwCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 1),
    _SwCpuUsage_Type()
)
swCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsage.setStatus("current")


class _SwCpuNoOfRetries_Type(Integer32):
    """Custom type swCpuNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuNoOfRetries_Type.__name__ = "Integer32"
_SwCpuNoOfRetries_Object = MibScalar
swCpuNoOfRetries = _SwCpuNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 2),
    _SwCpuNoOfRetries_Type()
)
swCpuNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuNoOfRetries.setStatus("current")


class _SwCpuUsageLimit_Type(Integer32):
    """Custom type swCpuUsageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwCpuUsageLimit_Type.__name__ = "Integer32"
_SwCpuUsageLimit_Object = MibScalar
swCpuUsageLimit = _SwCpuUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 3),
    _SwCpuUsageLimit_Type()
)
swCpuUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuUsageLimit.setStatus("current")


class _SwCpuPollingInterval_Type(Integer32):
    """Custom type swCpuPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwCpuPollingInterval_Type.__name__ = "Integer32"
_SwCpuPollingInterval_Object = MibScalar
swCpuPollingInterval = _SwCpuPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 4),
    _SwCpuPollingInterval_Type()
)
swCpuPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swCpuPollingInterval.setUnits("seconds")


class _SwCpuAction_Type(Integer32):
    """Custom type swCpuAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwCpuAction_Type.__name__ = "Integer32"
_SwCpuAction_Object = MibScalar
swCpuAction = _SwCpuAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 5),
    _SwCpuAction_Type()
)
swCpuAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCpuAction.setStatus("current")
if mibBuilder.loadTexts:
    swCpuAction.setUnits("seconds")
_SwMemUsage_Type = Integer32
_SwMemUsage_Object = MibScalar
swMemUsage = _SwMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 6),
    _SwMemUsage_Type()
)
swMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsage.setStatus("current")


class _SwMemNoOfRetries_Type(Integer32):
    """Custom type swMemNoOfRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SwMemNoOfRetries_Type.__name__ = "Integer32"
_SwMemNoOfRetries_Object = MibScalar
swMemNoOfRetries = _SwMemNoOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 7),
    _SwMemNoOfRetries_Type()
)
swMemNoOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemNoOfRetries.setStatus("current")
_SwMemUsageLimit_Type = Integer32
_SwMemUsageLimit_Object = MibScalar
swMemUsageLimit = _SwMemUsageLimit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 8),
    _SwMemUsageLimit_Type()
)
swMemUsageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemUsageLimit.setStatus("current")


class _SwMemPollingInterval_Type(Integer32):
    """Custom type swMemPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_SwMemPollingInterval_Type.__name__ = "Integer32"
_SwMemPollingInterval_Object = MibScalar
swMemPollingInterval = _SwMemPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 9),
    _SwMemPollingInterval_Type()
)
swMemPollingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    swMemPollingInterval.setUnits("seconds")


class _SwMemAction_Type(Integer32):
    """Custom type swMemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwMemAction_Type.__name__ = "Integer32"
_SwMemAction_Object = MibScalar
swMemAction = _SwMemAction_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 26, 10),
    _SwMemAction_Type()
)
swMemAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMemAction.setStatus("current")
if mibBuilder.loadTexts:
    swMemAction.setUnits("seconds")

# Managed Objects groups


# Notification objects

swEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 4)
)
swEventTrap.setObjects(
      *(("SWSYSTEM-MIB", "swEventIndex"),
        ("SWSYSTEM-MIB", "swEventTimeInfo"),
        ("SWSYSTEM-MIB", "swEventLevel"),
        ("SWSYSTEM-MIB", "swEventRepeatCount"),
        ("SWSYSTEM-MIB", "swEventDescr"),
        ("SWSYSTEM-MIB", "swSsn"))
)
if mibBuilder.loadTexts:
    swEventTrap.setStatus(
        "current"
    )

swStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 12)
)
swStateChangeTrap.setObjects(
    ("SWSYSTEM-MIB", "swOperStatus")
)
if mibBuilder.loadTexts:
    swStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWSYSTEM-MIB",
    **{"FcPortFlag": FcPortFlag,
       "SwFwEvent": SwFwEvent,
       "swTrapsV2": swTrapsV2,
       "swEventTrap": swEventTrap,
       "swStateChangeTrap": swStateChangeTrap,
       "swSystem": swSystem,
       "swCurrentDate": swCurrentDate,
       "swBootDate": swBootDate,
       "swFWLastUpdated": swFWLastUpdated,
       "swFlashLastUpdated": swFlashLastUpdated,
       "swBootPromLastUpdated": swBootPromLastUpdated,
       "swFirmwareVersion": swFirmwareVersion,
       "swOperStatus": swOperStatus,
       "swSsn": swSsn,
       "swBeaconOperStatus": swBeaconOperStatus,
       "swBeaconAdmStatus": swBeaconAdmStatus,
       "swDiagResult": swDiagResult,
       "swNumSensors": swNumSensors,
       "swSensorTable": swSensorTable,
       "swSensorEntry": swSensorEntry,
       "swSensorIndex": swSensorIndex,
       "swSensorType": swSensorType,
       "swSensorStatus": swSensorStatus,
       "swSensorValue": swSensorValue,
       "swSensorInfo": swSensorInfo,
       "swID": swID,
       "swEtherIPAddress": swEtherIPAddress,
       "swEtherIPMask": swEtherIPMask,
       "swIPv6Address": swIPv6Address,
       "swIPv6Status": swIPv6Status,
       "swEvent": swEvent,
       "swEventTrapLevel": swEventTrapLevel,
       "swEventNumEntries": swEventNumEntries,
       "swEventTable": swEventTable,
       "swEventEntry": swEventEntry,
       "swEventIndex": swEventIndex,
       "swEventTimeInfo": swEventTimeInfo,
       "swEventLevel": swEventLevel,
       "swEventRepeatCount": swEventRepeatCount,
       "swEventDescr": swEventDescr,
       "swEventVfId": swEventVfId,
       "swCpuOrMemoryUsage": swCpuOrMemoryUsage,
       "swCpuUsage": swCpuUsage,
       "swCpuNoOfRetries": swCpuNoOfRetries,
       "swCpuUsageLimit": swCpuUsageLimit,
       "swCpuPollingInterval": swCpuPollingInterval,
       "swCpuAction": swCpuAction,
       "swMemUsage": swMemUsage,
       "swMemNoOfRetries": swMemNoOfRetries,
       "swMemUsageLimit": swMemUsageLimit,
       "swMemPollingInterval": swMemPollingInterval,
       "swMemAction": swMemAction}
)
