# SNMP MIB module (ARICENT-CLKIWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/ARICENT-CLKIWF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:48 2025
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
 enterprises,
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
    "enterprises",
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

fsClkIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46)
)
if mibBuilder.loadTexts:
    fsClkIwfMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsClkIwfTimeInterval(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_FsClkIwfObjects_ObjectIdentity = ObjectIdentity
fsClkIwfObjects = _FsClkIwfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1)
)
_FsClkIwfGeneralGroup_ObjectIdentity = ObjectIdentity
fsClkIwfGeneralGroup = _FsClkIwfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1)
)


class _FsClkIwfClockVariance_Type(Integer32):
    """Custom type fsClkIwfClockVariance based on Integer32"""
    defaultValue = 0


_FsClkIwfClockVariance_Type.__name__ = "Integer32"
_FsClkIwfClockVariance_Object = MibScalar
fsClkIwfClockVariance = _FsClkIwfClockVariance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 1),
    _FsClkIwfClockVariance_Type()
)
fsClkIwfClockVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfClockVariance.setStatus("current")


class _FsClkIwfClockClass_Type(Integer32):
    """Custom type fsClkIwfClockClass based on Integer32"""
    defaultValue = 248


_FsClkIwfClockClass_Type.__name__ = "Integer32"
_FsClkIwfClockClass_Object = MibScalar
fsClkIwfClockClass = _FsClkIwfClockClass_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 2),
    _FsClkIwfClockClass_Type()
)
fsClkIwfClockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfClockClass.setStatus("current")


class _FsClkIwfClockAccuracy_Type(Integer32):
    """Custom type fsClkIwfClockAccuracy based on Integer32"""
    defaultValue = 254


_FsClkIwfClockAccuracy_Type.__name__ = "Integer32"
_FsClkIwfClockAccuracy_Object = MibScalar
fsClkIwfClockAccuracy = _FsClkIwfClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 3),
    _FsClkIwfClockAccuracy_Type()
)
fsClkIwfClockAccuracy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfClockAccuracy.setStatus("current")


class _FsClkIwfClockTimeSource_Type(Integer32):
    """Custom type fsClkIwfClockTimeSource based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              80,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("ptp", 64),
          ("ntp", 80),
          ("internalOscillator", 160))
    )


_FsClkIwfClockTimeSource_Type.__name__ = "Integer32"
_FsClkIwfClockTimeSource_Object = MibScalar
fsClkIwfClockTimeSource = _FsClkIwfClockTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 4),
    _FsClkIwfClockTimeSource_Type()
)
fsClkIwfClockTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfClockTimeSource.setStatus("current")
_FsClkIwfCurrentUtcOffset_Type = FsClkIwfTimeInterval
_FsClkIwfCurrentUtcOffset_Object = MibScalar
fsClkIwfCurrentUtcOffset = _FsClkIwfCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 5),
    _FsClkIwfCurrentUtcOffset_Type()
)
fsClkIwfCurrentUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfCurrentUtcOffset.setStatus("deprecated")
_FsClkIwfARBTime_Type = DisplayString
_FsClkIwfARBTime_Object = MibScalar
fsClkIwfARBTime = _FsClkIwfARBTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 6),
    _FsClkIwfARBTime_Type()
)
fsClkIwfARBTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfARBTime.setStatus("current")


class _FsClkIwfHoldoverSpecification_Type(TruthValue):
    """Custom type fsClkIwfHoldoverSpecification based on TruthValue"""
    defaultValue = 1


_FsClkIwfHoldoverSpecification_Type.__name__ = "TruthValue"
_FsClkIwfHoldoverSpecification_Object = MibScalar
fsClkIwfHoldoverSpecification = _FsClkIwfHoldoverSpecification_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 7),
    _FsClkIwfHoldoverSpecification_Type()
)
fsClkIwfHoldoverSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfHoldoverSpecification.setStatus("current")


class _FsClkIwfLostSync_Type(TruthValue):
    """Custom type fsClkIwfLostSync based on TruthValue"""
    defaultValue = 2


_FsClkIwfLostSync_Type.__name__ = "TruthValue"
_FsClkIwfLostSync_Object = MibScalar
fsClkIwfLostSync = _FsClkIwfLostSync_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 8),
    _FsClkIwfLostSync_Type()
)
fsClkIwfLostSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClkIwfLostSync.setStatus("current")
_FsClkIwfUtcOffset_Type = DisplayString
_FsClkIwfUtcOffset_Object = MibScalar
fsClkIwfUtcOffset = _FsClkIwfUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 1, 1, 9),
    _FsClkIwfUtcOffset_Type()
)
fsClkIwfUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfUtcOffset.setStatus("current")
_FsClkIwfNotifications_ObjectIdentity = ObjectIdentity
fsClkIwfNotifications = _FsClkIwfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 2)
)
_FsClkIwfTrap_ObjectIdentity = ObjectIdentity
fsClkIwfTrap = _FsClkIwfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 2, 0)
)


class _FsClkIwfGlobalErrTrapType_Type(Integer32):
    """Custom type fsClkIwfGlobalErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("memfail", 1),
          ("bufffail", 2),
          ("timesourcechange", 3),
          ("clockclasschange", 4),
          ("clockaccuracychange", 5),
          ("clockvariancechange", 6),
          ("holdovermodechange", 7))
    )


_FsClkIwfGlobalErrTrapType_Type.__name__ = "Integer32"
_FsClkIwfGlobalErrTrapType_Object = MibScalar
fsClkIwfGlobalErrTrapType = _FsClkIwfGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 2, 1),
    _FsClkIwfGlobalErrTrapType_Type()
)
fsClkIwfGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsClkIwfGlobalErrTrapType.setStatus("current")
_FsClkIwfNotification_Type = OctetString
_FsClkIwfNotification_Object = MibScalar
fsClkIwfNotification = _FsClkIwfNotification_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 2, 2),
    _FsClkIwfNotification_Type()
)
fsClkIwfNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClkIwfNotification.setStatus("current")

# Managed Objects groups


# Notification objects

fsClkIwfGlobalErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 46, 2, 0, 1)
)
fsClkIwfGlobalErrorTrap.setObjects(
    ("ARICENT-CLKIWF-MIB", "fsClkIwfGlobalErrTrapType")
)
if mibBuilder.loadTexts:
    fsClkIwfGlobalErrorTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-CLKIWF-MIB",
    **{"FsClkIwfTimeInterval": FsClkIwfTimeInterval,
       "fsClkIwfMIB": fsClkIwfMIB,
       "fsClkIwfObjects": fsClkIwfObjects,
       "fsClkIwfGeneralGroup": fsClkIwfGeneralGroup,
       "fsClkIwfClockVariance": fsClkIwfClockVariance,
       "fsClkIwfClockClass": fsClkIwfClockClass,
       "fsClkIwfClockAccuracy": fsClkIwfClockAccuracy,
       "fsClkIwfClockTimeSource": fsClkIwfClockTimeSource,
       "fsClkIwfCurrentUtcOffset": fsClkIwfCurrentUtcOffset,
       "fsClkIwfARBTime": fsClkIwfARBTime,
       "fsClkIwfHoldoverSpecification": fsClkIwfHoldoverSpecification,
       "fsClkIwfLostSync": fsClkIwfLostSync,
       "fsClkIwfUtcOffset": fsClkIwfUtcOffset,
       "fsClkIwfNotifications": fsClkIwfNotifications,
       "fsClkIwfTrap": fsClkIwfTrap,
       "fsClkIwfGlobalErrorTrap": fsClkIwfGlobalErrorTrap,
       "fsClkIwfGlobalErrTrapType": fsClkIwfGlobalErrTrapType,
       "fsClkIwfNotification": fsClkIwfNotification}
)
