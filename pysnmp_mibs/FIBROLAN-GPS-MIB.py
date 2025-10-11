# SNMP MIB module (FIBROLAN-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fibrolan/FIBROLAN-GPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:11 2025
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

(FlGeoCoordinateAxis,
 fibrolanGeneric) = mibBuilder.importSymbols(
    "FIBROLAN-COMMON-MIB",
    "FlGeoCoordinateAxis",
    "fibrolanGeneric")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

flGps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210)
)
if mibBuilder.loadTexts:
    flGps.setRevisions(
        ("2015-09-15 00:00",
         "2015-08-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlGpsNotifications_ObjectIdentity = ObjectIdentity
flGpsNotifications = _FlGpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 0)
)
_FlGpsMIBObjects_ObjectIdentity = ObjectIdentity
flGpsMIBObjects = _FlGpsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1)
)
_FlGpsTable_Object = MibTable
flGpsTable = _FlGpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10)
)
if mibBuilder.loadTexts:
    flGpsTable.setStatus("current")
_FlGpsEntry_Object = MibTableRow
flGpsEntry = _FlGpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1)
)
flGpsEntry.setIndexNames(
    (0, "FIBROLAN-GPS-MIB", "flGpsId"),
)
if mibBuilder.loadTexts:
    flGpsEntry.setStatus("current")


class _FlGpsId_Type(Integer32):
    """Custom type flGpsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlGpsId_Type.__name__ = "Integer32"
_FlGpsId_Object = MibTableColumn
flGpsId = _FlGpsId_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 1),
    _FlGpsId_Type()
)
flGpsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flGpsId.setStatus("current")


class _FlGpsModulePartNumber_Type(DisplayString):
    """Custom type flGpsModulePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlGpsModulePartNumber_Type.__name__ = "DisplayString"
_FlGpsModulePartNumber_Object = MibTableColumn
flGpsModulePartNumber = _FlGpsModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 2),
    _FlGpsModulePartNumber_Type()
)
flGpsModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsModulePartNumber.setStatus("current")


class _FlGpsModuleSerialNumber_Type(DisplayString):
    """Custom type flGpsModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlGpsModuleSerialNumber_Type.__name__ = "DisplayString"
_FlGpsModuleSerialNumber_Object = MibTableColumn
flGpsModuleSerialNumber = _FlGpsModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 3),
    _FlGpsModuleSerialNumber_Type()
)
flGpsModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsModuleSerialNumber.setStatus("current")


class _FlGpsHardwareId_Type(DisplayString):
    """Custom type flGpsHardwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlGpsHardwareId_Type.__name__ = "DisplayString"
_FlGpsHardwareId_Object = MibTableColumn
flGpsHardwareId = _FlGpsHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 4),
    _FlGpsHardwareId_Type()
)
flGpsHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsHardwareId.setStatus("current")


class _FlGpsFirmwareVersion_Type(DisplayString):
    """Custom type flGpsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlGpsFirmwareVersion_Type.__name__ = "DisplayString"
_FlGpsFirmwareVersion_Object = MibTableColumn
flGpsFirmwareVersion = _FlGpsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 5),
    _FlGpsFirmwareVersion_Type()
)
flGpsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsFirmwareVersion.setStatus("current")


class _FlGpsFirmwareDate_Type(DisplayString):
    """Custom type flGpsFirmwareDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FlGpsFirmwareDate_Type.__name__ = "DisplayString"
_FlGpsFirmwareDate_Object = MibTableColumn
flGpsFirmwareDate = _FlGpsFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 6),
    _FlGpsFirmwareDate_Type()
)
flGpsFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsFirmwareDate.setStatus("current")


class _FlGpsState_Type(Integer32):
    """Custom type flGpsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 1),
          ("searching", 2),
          ("acquiring", 3),
          ("locked", 4),
          ("fail", 5),
          ("other", 99))
    )


_FlGpsState_Type.__name__ = "Integer32"
_FlGpsState_Object = MibTableColumn
flGpsState = _FlGpsState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 7),
    _FlGpsState_Type()
)
flGpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsState.setStatus("current")
_FlGpsStateLastChange_Type = TimeTicks
_FlGpsStateLastChange_Object = MibTableColumn
flGpsStateLastChange = _FlGpsStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 8),
    _FlGpsStateLastChange_Type()
)
flGpsStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsStateLastChange.setStatus("current")
_FlGpsDateAndTime_Type = DateAndTime
_FlGpsDateAndTime_Object = MibTableColumn
flGpsDateAndTime = _FlGpsDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 9),
    _FlGpsDateAndTime_Type()
)
flGpsDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsDateAndTime.setStatus("current")
_FlGpsLatitude_Type = FlGeoCoordinateAxis
_FlGpsLatitude_Object = MibTableColumn
flGpsLatitude = _FlGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 10),
    _FlGpsLatitude_Type()
)
flGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsLatitude.setStatus("current")
_FlGpsLongitude_Type = FlGeoCoordinateAxis
_FlGpsLongitude_Object = MibTableColumn
flGpsLongitude = _FlGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 11),
    _FlGpsLongitude_Type()
)
flGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsLongitude.setStatus("current")


class _FlGpsAltitude_Type(Integer32):
    """Custom type flGpsAltitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 10000),
    )


_FlGpsAltitude_Type.__name__ = "Integer32"
_FlGpsAltitude_Object = MibTableColumn
flGpsAltitude = _FlGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 12),
    _FlGpsAltitude_Type()
)
flGpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsAltitude.setStatus("current")


class _FlGpsCableDelay_Type(Integer32):
    """Custom type flGpsCableDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlGpsCableDelay_Type.__name__ = "Integer32"
_FlGpsCableDelay_Object = MibTableColumn
flGpsCableDelay = _FlGpsCableDelay_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 13),
    _FlGpsCableDelay_Type()
)
flGpsCableDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsCableDelay.setStatus("current")


class _FlGpsAntennaState_Type(Integer32):
    """Custom type flGpsAntennaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("open", 2),
          ("shorted", 3),
          ("other", 99))
    )


_FlGpsAntennaState_Type.__name__ = "Integer32"
_FlGpsAntennaState_Object = MibTableColumn
flGpsAntennaState = _FlGpsAntennaState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 14),
    _FlGpsAntennaState_Type()
)
flGpsAntennaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsAntennaState.setStatus("current")


class _FlGps1PpsState_Type(Integer32):
    """Custom type flGps1PpsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("notGenerated", 2),
          ("other", 99))
    )


_FlGps1PpsState_Type.__name__ = "Integer32"
_FlGps1PpsState_Object = MibTableColumn
flGps1PpsState = _FlGps1PpsState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 15),
    _FlGps1PpsState_Type()
)
flGps1PpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGps1PpsState.setStatus("current")


class _FlGpsTrackedSatelliteCount_Type(Integer32):
    """Custom type flGpsTrackedSatelliteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FlGpsTrackedSatelliteCount_Type.__name__ = "Integer32"
_FlGpsTrackedSatelliteCount_Object = MibTableColumn
flGpsTrackedSatelliteCount = _FlGpsTrackedSatelliteCount_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 10, 1, 16),
    _FlGpsTrackedSatelliteCount_Type()
)
flGpsTrackedSatelliteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsTrackedSatelliteCount.setStatus("current")
_FlGpsSatelliteTable_Object = MibTable
flGpsSatelliteTable = _FlGpsSatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30)
)
if mibBuilder.loadTexts:
    flGpsSatelliteTable.setStatus("current")
_FlGpsSatelliteEntry_Object = MibTableRow
flGpsSatelliteEntry = _FlGpsSatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1)
)
flGpsSatelliteEntry.setIndexNames(
    (0, "FIBROLAN-GPS-MIB", "flGpsSatelliteId"),
)
if mibBuilder.loadTexts:
    flGpsSatelliteEntry.setStatus("current")


class _FlGpsSatelliteId_Type(Integer32):
    """Custom type flGpsSatelliteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlGpsSatelliteId_Type.__name__ = "Integer32"
_FlGpsSatelliteId_Object = MibTableColumn
flGpsSatelliteId = _FlGpsSatelliteId_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 2),
    _FlGpsSatelliteId_Type()
)
flGpsSatelliteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flGpsSatelliteId.setStatus("current")


class _FlGpsSatellitePrn_Type(Integer32):
    """Custom type flGpsSatellitePrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlGpsSatellitePrn_Type.__name__ = "Integer32"
_FlGpsSatellitePrn_Object = MibTableColumn
flGpsSatellitePrn = _FlGpsSatellitePrn_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 3),
    _FlGpsSatellitePrn_Type()
)
flGpsSatellitePrn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flGpsSatellitePrn.setStatus("current")


class _FlGpsSatelliteType_Type(Integer32):
    """Custom type flGpsSatelliteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("gps", 1),
          ("glonass", 2),
          ("galileo", 3),
          ("beidou", 4),
          ("qzss", 5),
          ("other", 99))
    )


_FlGpsSatelliteType_Type.__name__ = "Integer32"
_FlGpsSatelliteType_Object = MibTableColumn
flGpsSatelliteType = _FlGpsSatelliteType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 4),
    _FlGpsSatelliteType_Type()
)
flGpsSatelliteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteType.setStatus("current")


class _FlGpsSatelliteChannel_Type(Integer32):
    """Custom type flGpsSatelliteChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FlGpsSatelliteChannel_Type.__name__ = "Integer32"
_FlGpsSatelliteChannel_Object = MibTableColumn
flGpsSatelliteChannel = _FlGpsSatelliteChannel_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 5),
    _FlGpsSatelliteChannel_Type()
)
flGpsSatelliteChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteChannel.setStatus("current")


class _FlGpsSatelliteAcquisitionState_Type(Integer32):
    """Custom type flGpsSatelliteAcquisitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("acquired", 1),
          ("neverAcquired", 2),
          ("reopenSearch", 3),
          ("other", 99))
    )


_FlGpsSatelliteAcquisitionState_Type.__name__ = "Integer32"
_FlGpsSatelliteAcquisitionState_Object = MibTableColumn
flGpsSatelliteAcquisitionState = _FlGpsSatelliteAcquisitionState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 6),
    _FlGpsSatelliteAcquisitionState_Type()
)
flGpsSatelliteAcquisitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteAcquisitionState.setStatus("current")


class _FlGpsSatelliteSignalLevel_Type(Integer32):
    """Custom type flGpsSatelliteSignalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FlGpsSatelliteSignalLevel_Type.__name__ = "Integer32"
_FlGpsSatelliteSignalLevel_Object = MibTableColumn
flGpsSatelliteSignalLevel = _FlGpsSatelliteSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 7),
    _FlGpsSatelliteSignalLevel_Type()
)
flGpsSatelliteSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteSignalLevel.setStatus("current")


class _FlGpsSatelliteElevationAngle_Type(Integer32):
    """Custom type flGpsSatelliteElevationAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_FlGpsSatelliteElevationAngle_Type.__name__ = "Integer32"
_FlGpsSatelliteElevationAngle_Object = MibTableColumn
flGpsSatelliteElevationAngle = _FlGpsSatelliteElevationAngle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 8),
    _FlGpsSatelliteElevationAngle_Type()
)
flGpsSatelliteElevationAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteElevationAngle.setStatus("current")


class _FlGpsSatelliteAzimuthAngle_Type(Integer32):
    """Custom type flGpsSatelliteAzimuthAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_FlGpsSatelliteAzimuthAngle_Type.__name__ = "Integer32"
_FlGpsSatelliteAzimuthAngle_Object = MibTableColumn
flGpsSatelliteAzimuthAngle = _FlGpsSatelliteAzimuthAngle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 9),
    _FlGpsSatelliteAzimuthAngle_Type()
)
flGpsSatelliteAzimuthAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteAzimuthAngle.setStatus("current")


class _FlGpsSatelliteUsedForTiming_Type(Integer32):
    """Custom type flGpsSatelliteUsedForTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("other", 99))
    )


_FlGpsSatelliteUsedForTiming_Type.__name__ = "Integer32"
_FlGpsSatelliteUsedForTiming_Object = MibTableColumn
flGpsSatelliteUsedForTiming = _FlGpsSatelliteUsedForTiming_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 10),
    _FlGpsSatelliteUsedForTiming_Type()
)
flGpsSatelliteUsedForTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteUsedForTiming.setStatus("current")


class _FlGpsSatelliteUsedForPosition_Type(Integer32):
    """Custom type flGpsSatelliteUsedForPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("other", 99))
    )


_FlGpsSatelliteUsedForPosition_Type.__name__ = "Integer32"
_FlGpsSatelliteUsedForPosition_Object = MibTableColumn
flGpsSatelliteUsedForPosition = _FlGpsSatelliteUsedForPosition_Object(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 1, 30, 1, 11),
    _FlGpsSatelliteUsedForPosition_Type()
)
flGpsSatelliteUsedForPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flGpsSatelliteUsedForPosition.setStatus("current")

# Managed Objects groups


# Notification objects

flGpsStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 0, 10)
)
flGpsStateChanged.setObjects(
    ("FIBROLAN-GPS-MIB", "flGpsState")
)
if mibBuilder.loadTexts:
    flGpsStateChanged.setStatus(
        "current"
    )

flGpsAntennaStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4467, 1000, 210, 0, 20)
)
flGpsAntennaStateChanged.setObjects(
    ("FIBROLAN-GPS-MIB", "flGpsAntennaState")
)
if mibBuilder.loadTexts:
    flGpsAntennaStateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-GPS-MIB",
    **{"flGps": flGps,
       "flGpsNotifications": flGpsNotifications,
       "flGpsStateChanged": flGpsStateChanged,
       "flGpsAntennaStateChanged": flGpsAntennaStateChanged,
       "flGpsMIBObjects": flGpsMIBObjects,
       "flGpsTable": flGpsTable,
       "flGpsEntry": flGpsEntry,
       "flGpsId": flGpsId,
       "flGpsModulePartNumber": flGpsModulePartNumber,
       "flGpsModuleSerialNumber": flGpsModuleSerialNumber,
       "flGpsHardwareId": flGpsHardwareId,
       "flGpsFirmwareVersion": flGpsFirmwareVersion,
       "flGpsFirmwareDate": flGpsFirmwareDate,
       "flGpsState": flGpsState,
       "flGpsStateLastChange": flGpsStateLastChange,
       "flGpsDateAndTime": flGpsDateAndTime,
       "flGpsLatitude": flGpsLatitude,
       "flGpsLongitude": flGpsLongitude,
       "flGpsAltitude": flGpsAltitude,
       "flGpsCableDelay": flGpsCableDelay,
       "flGpsAntennaState": flGpsAntennaState,
       "flGps1PpsState": flGps1PpsState,
       "flGpsTrackedSatelliteCount": flGpsTrackedSatelliteCount,
       "flGpsSatelliteTable": flGpsSatelliteTable,
       "flGpsSatelliteEntry": flGpsSatelliteEntry,
       "flGpsSatelliteId": flGpsSatelliteId,
       "flGpsSatellitePrn": flGpsSatellitePrn,
       "flGpsSatelliteType": flGpsSatelliteType,
       "flGpsSatelliteChannel": flGpsSatelliteChannel,
       "flGpsSatelliteAcquisitionState": flGpsSatelliteAcquisitionState,
       "flGpsSatelliteSignalLevel": flGpsSatelliteSignalLevel,
       "flGpsSatelliteElevationAngle": flGpsSatelliteElevationAngle,
       "flGpsSatelliteAzimuthAngle": flGpsSatelliteAzimuthAngle,
       "flGpsSatelliteUsedForTiming": flGpsSatelliteUsedForTiming,
       "flGpsSatelliteUsedForPosition": flGpsSatelliteUsedForPosition}
)
