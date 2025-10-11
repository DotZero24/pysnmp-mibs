# SNMP MIB module (ARRIS-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-GPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:21 2025
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

(arris,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arris")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisGpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 12)
)
if mibBuilder.loadTexts:
    arrisGpsMib.setRevisions(
        ("2014-08-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ArrisGpsScanOnBoot_Type(TruthValue):
    """Custom type arrisGpsScanOnBoot based on TruthValue"""
    defaultValue = 1


_ArrisGpsScanOnBoot_Type.__name__ = "TruthValue"
_ArrisGpsScanOnBoot_Object = MibScalar
arrisGpsScanOnBoot = _ArrisGpsScanOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 1),
    _ArrisGpsScanOnBoot_Type()
)
arrisGpsScanOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsScanOnBoot.setStatus("current")


class _ArrisGpsScanPeriodically_Type(TruthValue):
    """Custom type arrisGpsScanPeriodically based on TruthValue"""
    defaultValue = 2


_ArrisGpsScanPeriodically_Type.__name__ = "TruthValue"
_ArrisGpsScanPeriodically_Object = MibScalar
arrisGpsScanPeriodically = _ArrisGpsScanPeriodically_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 2),
    _ArrisGpsScanPeriodically_Type()
)
arrisGpsScanPeriodically.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsScanPeriodically.setStatus("current")


class _ArrisGpsPeriodicInterval_Type(Unsigned32):
    """Custom type arrisGpsPeriodicInterval based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_ArrisGpsPeriodicInterval_Type.__name__ = "Unsigned32"
_ArrisGpsPeriodicInterval_Object = MibScalar
arrisGpsPeriodicInterval = _ArrisGpsPeriodicInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 3),
    _ArrisGpsPeriodicInterval_Type()
)
arrisGpsPeriodicInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsPeriodicInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisGpsPeriodicInterval.setUnits("seconds")


class _ArrisGpsPeriodicTime_Type(DisplayString):
    """Custom type arrisGpsPeriodicTime based on DisplayString"""
    defaultValue = OctetString("Unknown Time")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisGpsPeriodicTime_Type.__name__ = "DisplayString"
_ArrisGpsPeriodicTime_Object = MibScalar
arrisGpsPeriodicTime = _ArrisGpsPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 4),
    _ArrisGpsPeriodicTime_Type()
)
arrisGpsPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsPeriodicTime.setStatus("current")


class _ArrisGpsPowerDownAfterSuccessfulScan_Type(TruthValue):
    """Custom type arrisGpsPowerDownAfterSuccessfulScan based on TruthValue"""
    defaultValue = 1


_ArrisGpsPowerDownAfterSuccessfulScan_Type.__name__ = "TruthValue"
_ArrisGpsPowerDownAfterSuccessfulScan_Object = MibScalar
arrisGpsPowerDownAfterSuccessfulScan = _ArrisGpsPowerDownAfterSuccessfulScan_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 5),
    _ArrisGpsPowerDownAfterSuccessfulScan_Type()
)
arrisGpsPowerDownAfterSuccessfulScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsPowerDownAfterSuccessfulScan.setStatus("current")


class _ArrisGpsScanTimeout_Type(Unsigned32):
    """Custom type arrisGpsScanTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_ArrisGpsScanTimeout_Type.__name__ = "Unsigned32"
_ArrisGpsScanTimeout_Object = MibScalar
arrisGpsScanTimeout = _ArrisGpsScanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 6),
    _ArrisGpsScanTimeout_Type()
)
arrisGpsScanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsScanTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisGpsScanTimeout.setUnits("seconds")


class _ArrisGpsScanStatus_Type(Integer32):
    """Custom type arrisGpsScanStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 0),
          ("inprogress", 1),
          ("success", 2),
          ("error", 3),
          ("errorTimeout", 4))
    )


_ArrisGpsScanStatus_Type.__name__ = "Integer32"
_ArrisGpsScanStatus_Object = MibScalar
arrisGpsScanStatus = _ArrisGpsScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 7),
    _ArrisGpsScanStatus_Type()
)
arrisGpsScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsScanStatus.setStatus("current")


class _ArrisGpsErrorDetails_Type(DisplayString):
    """Custom type arrisGpsErrorDetails based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisGpsErrorDetails_Type.__name__ = "DisplayString"
_ArrisGpsErrorDetails_Object = MibScalar
arrisGpsErrorDetails = _ArrisGpsErrorDetails_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 8),
    _ArrisGpsErrorDetails_Type()
)
arrisGpsErrorDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsErrorDetails.setStatus("current")


class _ArrisGpsLastScanTime_Type(DisplayString):
    """Custom type arrisGpsLastScanTime based on DisplayString"""
    defaultValue = OctetString("Unknown Time")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisGpsLastScanTime_Type.__name__ = "DisplayString"
_ArrisGpsLastScanTime_Object = MibScalar
arrisGpsLastScanTime = _ArrisGpsLastScanTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 9),
    _ArrisGpsLastScanTime_Type()
)
arrisGpsLastScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsLastScanTime.setStatus("current")


class _ArrisGpsLastSuccessfulScanTime_Type(DisplayString):
    """Custom type arrisGpsLastSuccessfulScanTime based on DisplayString"""
    defaultValue = OctetString("Unknown Time")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisGpsLastSuccessfulScanTime_Type.__name__ = "DisplayString"
_ArrisGpsLastSuccessfulScanTime_Object = MibScalar
arrisGpsLastSuccessfulScanTime = _ArrisGpsLastSuccessfulScanTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 10),
    _ArrisGpsLastSuccessfulScanTime_Type()
)
arrisGpsLastSuccessfulScanTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsLastSuccessfulScanTime.setStatus("current")


class _ArrisGpsLockedLatitude_Type(DisplayString):
    """Custom type arrisGpsLockedLatitude based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisGpsLockedLatitude_Type.__name__ = "DisplayString"
_ArrisGpsLockedLatitude_Object = MibScalar
arrisGpsLockedLatitude = _ArrisGpsLockedLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 11),
    _ArrisGpsLockedLatitude_Type()
)
arrisGpsLockedLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsLockedLatitude.setStatus("current")


class _ArrisGpsLockedLongitude_Type(DisplayString):
    """Custom type arrisGpsLockedLongitude based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisGpsLockedLongitude_Type.__name__ = "DisplayString"
_ArrisGpsLockedLongitude_Object = MibScalar
arrisGpsLockedLongitude = _ArrisGpsLockedLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 12),
    _ArrisGpsLockedLongitude_Type()
)
arrisGpsLockedLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsLockedLongitude.setStatus("current")


class _ArrisGpsNumberOfSatellites_Type(Unsigned32):
    """Custom type arrisGpsNumberOfSatellites based on Unsigned32"""
    defaultValue = 0


_ArrisGpsNumberOfSatellites_Type.__name__ = "Unsigned32"
_ArrisGpsNumberOfSatellites_Object = MibScalar
arrisGpsNumberOfSatellites = _ArrisGpsNumberOfSatellites_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 13),
    _ArrisGpsNumberOfSatellites_Type()
)
arrisGpsNumberOfSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsNumberOfSatellites.setStatus("current")


class _ArrisGpsReset_Type(TruthValue):
    """Custom type arrisGpsReset based on TruthValue"""
    defaultValue = 2


_ArrisGpsReset_Type.__name__ = "TruthValue"
_ArrisGpsReset_Object = MibScalar
arrisGpsReset = _ArrisGpsReset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 14),
    _ArrisGpsReset_Type()
)
arrisGpsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisGpsReset.setStatus("current")


class _ArrisGpsSuccessfulScanSinceBootup_Type(TruthValue):
    """Custom type arrisGpsSuccessfulScanSinceBootup based on TruthValue"""
    defaultValue = 2


_ArrisGpsSuccessfulScanSinceBootup_Type.__name__ = "TruthValue"
_ArrisGpsSuccessfulScanSinceBootup_Object = MibScalar
arrisGpsSuccessfulScanSinceBootup = _ArrisGpsSuccessfulScanSinceBootup_Object(
    (1, 3, 6, 1, 4, 1, 4115, 12, 15),
    _ArrisGpsSuccessfulScanSinceBootup_Type()
)
arrisGpsSuccessfulScanSinceBootup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisGpsSuccessfulScanSinceBootup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-GPS-MIB",
    **{"arrisGpsMib": arrisGpsMib,
       "arrisGpsScanOnBoot": arrisGpsScanOnBoot,
       "arrisGpsScanPeriodically": arrisGpsScanPeriodically,
       "arrisGpsPeriodicInterval": arrisGpsPeriodicInterval,
       "arrisGpsPeriodicTime": arrisGpsPeriodicTime,
       "arrisGpsPowerDownAfterSuccessfulScan": arrisGpsPowerDownAfterSuccessfulScan,
       "arrisGpsScanTimeout": arrisGpsScanTimeout,
       "arrisGpsScanStatus": arrisGpsScanStatus,
       "arrisGpsErrorDetails": arrisGpsErrorDetails,
       "arrisGpsLastScanTime": arrisGpsLastScanTime,
       "arrisGpsLastSuccessfulScanTime": arrisGpsLastSuccessfulScanTime,
       "arrisGpsLockedLatitude": arrisGpsLockedLatitude,
       "arrisGpsLockedLongitude": arrisGpsLockedLongitude,
       "arrisGpsNumberOfSatellites": arrisGpsNumberOfSatellites,
       "arrisGpsReset": arrisGpsReset,
       "arrisGpsSuccessfulScanSinceBootup": arrisGpsSuccessfulScanSinceBootup}
)
