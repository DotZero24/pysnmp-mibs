# SNMP MIB module (WR-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/white-rabbit/WR-SWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:28 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

wrSwitchMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100)
)
if mibBuilder.loadTexts:
    wrSwitchMIB.setRevisions(
        ("2023-03-26 00:00",
         "2021-08-31 00:00",
         "2020-05-22 00:00",
         "2018-07-18 14:00",
         "2016-02-17 16:00",
         "2015-08-12 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cern_ObjectIdentity = ObjectIdentity
cern = _Cern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96)
)
_WrsScalar_ObjectIdentity = ObjectIdentity
wrsScalar = _WrsScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1)
)
_WrsScalarOne_Type = Integer32
_WrsScalarOne_Object = MibScalar
wrsScalarOne = _WrsScalarOne_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 1, 1),
    _WrsScalarOne_Type()
)
wrsScalarOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrsScalarOne.setStatus("current")
_WrsStatus_ObjectIdentity = ObjectIdentity
wrsStatus = _WrsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6)
)
_WrsGeneralStatusGroup_ObjectIdentity = ObjectIdentity
wrsGeneralStatusGroup = _WrsGeneralStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 1)
)


class _WrsMainSystemStatus_Type(Integer32):
    """Custom type wrsMainSystemStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsMainSystemStatus_Type.__name__ = "Integer32"
_WrsMainSystemStatus_Object = MibScalar
wrsMainSystemStatus = _WrsMainSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 1, 1),
    _WrsMainSystemStatus_Type()
)
wrsMainSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMainSystemStatus.setStatus("current")


class _WrsOSStatus_Type(Integer32):
    """Custom type wrsOSStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsOSStatus_Type.__name__ = "Integer32"
_WrsOSStatus_Object = MibScalar
wrsOSStatus = _WrsOSStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 1, 2),
    _WrsOSStatus_Type()
)
wrsOSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsOSStatus.setStatus("current")


class _WrsTimingStatus_Type(Integer32):
    """Custom type wrsTimingStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsTimingStatus_Type.__name__ = "Integer32"
_WrsTimingStatus_Object = MibScalar
wrsTimingStatus = _WrsTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 1, 3),
    _WrsTimingStatus_Type()
)
wrsTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTimingStatus.setStatus("current")


class _WrsNetworkingStatus_Type(Integer32):
    """Custom type wrsNetworkingStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsNetworkingStatus_Type.__name__ = "Integer32"
_WrsNetworkingStatus_Object = MibScalar
wrsNetworkingStatus = _WrsNetworkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 1, 4),
    _WrsNetworkingStatus_Type()
)
wrsNetworkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsNetworkingStatus.setStatus("current")
_WrsDetailedStatusesGroup_ObjectIdentity = ObjectIdentity
wrsDetailedStatusesGroup = _WrsDetailedStatusesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2)
)
_WrsOSStatusGroup_ObjectIdentity = ObjectIdentity
wrsOSStatusGroup = _WrsOSStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1)
)


class _WrsBootSuccessful_Type(Integer32):
    """Custom type wrsBootSuccessful based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsBootSuccessful_Type.__name__ = "Integer32"
_WrsBootSuccessful_Object = MibScalar
wrsBootSuccessful = _WrsBootSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1, 1),
    _WrsBootSuccessful_Type()
)
wrsBootSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootSuccessful.setStatus("current")


class _WrsTemperatureWarning_Type(Integer32):
    """Custom type wrsTemperatureWarning based on Integer32"""
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
        *(("na", 0),
          ("thresholdNotSet", 1),
          ("temperatureOK", 2),
          ("temperatureTooHigh", 3))
    )


_WrsTemperatureWarning_Type.__name__ = "Integer32"
_WrsTemperatureWarning_Object = MibScalar
wrsTemperatureWarning = _WrsTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1, 2),
    _WrsTemperatureWarning_Type()
)
wrsTemperatureWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTemperatureWarning.setStatus("current")


class _WrsMemoryFreeLow_Type(Integer32):
    """Custom type wrsMemoryFreeLow based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4))
    )


_WrsMemoryFreeLow_Type.__name__ = "Integer32"
_WrsMemoryFreeLow_Object = MibScalar
wrsMemoryFreeLow = _WrsMemoryFreeLow_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1, 3),
    _WrsMemoryFreeLow_Type()
)
wrsMemoryFreeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMemoryFreeLow.setStatus("current")


class _WrsCpuLoadHigh_Type(Integer32):
    """Custom type wrsCpuLoadHigh based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3))
    )


_WrsCpuLoadHigh_Type.__name__ = "Integer32"
_WrsCpuLoadHigh_Object = MibScalar
wrsCpuLoadHigh = _WrsCpuLoadHigh_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1, 4),
    _WrsCpuLoadHigh_Type()
)
wrsCpuLoadHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCpuLoadHigh.setStatus("current")


class _WrsDiskSpaceLow_Type(Integer32):
    """Custom type wrsDiskSpaceLow based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4))
    )


_WrsDiskSpaceLow_Type.__name__ = "Integer32"
_WrsDiskSpaceLow_Object = MibScalar
wrsDiskSpaceLow = _WrsDiskSpaceLow_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 1, 5),
    _WrsDiskSpaceLow_Type()
)
wrsDiskSpaceLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskSpaceLow.setStatus("current")
_WrsTimingStatusGroup_ObjectIdentity = ObjectIdentity
wrsTimingStatusGroup = _WrsTimingStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2)
)


class _WrsPTPStatus_Type(Integer32):
    """Custom type wrsPTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("firstRead", 6))
    )


_WrsPTPStatus_Type.__name__ = "Integer32"
_WrsPTPStatus_Object = MibScalar
wrsPTPStatus = _WrsPTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2, 1),
    _WrsPTPStatus_Type()
)
wrsPTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPTPStatus.setStatus("current")


class _WrsSoftPLLStatus_Type(Integer32):
    """Custom type wrsSoftPLLStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsSoftPLLStatus_Type.__name__ = "Integer32"
_WrsSoftPLLStatus_Object = MibScalar
wrsSoftPLLStatus = _WrsSoftPLLStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2, 2),
    _WrsSoftPLLStatus_Type()
)
wrsSoftPLLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSoftPLLStatus.setStatus("current")


class _WrsSlaveLinksStatus_Type(Integer32):
    """Custom type wrsSlaveLinksStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warningNA", 4))
    )


_WrsSlaveLinksStatus_Type.__name__ = "Integer32"
_WrsSlaveLinksStatus_Object = MibScalar
wrsSlaveLinksStatus = _WrsSlaveLinksStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2, 3),
    _WrsSlaveLinksStatus_Type()
)
wrsSlaveLinksStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSlaveLinksStatus.setStatus("current")


class _WrsPTPFramesFlowing_Type(Integer32):
    """Custom type wrsPTPFramesFlowing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warningNA", 4),
          ("firstRead", 6))
    )


_WrsPTPFramesFlowing_Type.__name__ = "Integer32"
_WrsPTPFramesFlowing_Object = MibScalar
wrsPTPFramesFlowing = _WrsPTPFramesFlowing_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2, 4),
    _WrsPTPFramesFlowing_Type()
)
wrsPTPFramesFlowing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPTPFramesFlowing.setStatus("current")


class _WrsSystemClockStatus_Type(Integer32):
    """Custom type wrsSystemClockStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4))
    )


_WrsSystemClockStatus_Type.__name__ = "Integer32"
_WrsSystemClockStatus_Object = MibScalar
wrsSystemClockStatus = _WrsSystemClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 2, 5),
    _WrsSystemClockStatus_Type()
)
wrsSystemClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockStatus.setStatus("current")
_WrsNetworkingStatusGroup_ObjectIdentity = ObjectIdentity
wrsNetworkingStatusGroup = _WrsNetworkingStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 3)
)


class _WrsSFPsStatus_Type(Integer32):
    """Custom type wrsSFPsStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warning", 3),
          ("warningNA", 4),
          ("bug", 5))
    )


_WrsSFPsStatus_Type.__name__ = "Integer32"
_WrsSFPsStatus_Object = MibScalar
wrsSFPsStatus = _WrsSFPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 3, 1),
    _WrsSFPsStatus_Type()
)
wrsSFPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSFPsStatus.setStatus("current")


class _WrsEndpointStatus_Type(Integer32):
    """Custom type wrsEndpointStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("firstRead", 6))
    )


_WrsEndpointStatus_Type.__name__ = "Integer32"
_WrsEndpointStatus_Object = MibScalar
wrsEndpointStatus = _WrsEndpointStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 3, 2),
    _WrsEndpointStatus_Type()
)
wrsEndpointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsEndpointStatus.setStatus("current")


class _WrsSwcoreStatus_Type(Integer32):
    """Custom type wrsSwcoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("firstRead", 6))
    )


_WrsSwcoreStatus_Type.__name__ = "Integer32"
_WrsSwcoreStatus_Object = MibScalar
wrsSwcoreStatus = _WrsSwcoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 3, 3),
    _WrsSwcoreStatus_Type()
)
wrsSwcoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSwcoreStatus.setStatus("current")


class _WrsRTUStatus_Type(Integer32):
    """Custom type wrsRTUStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("firstRead", 6))
    )


_WrsRTUStatus_Type.__name__ = "Integer32"
_WrsRTUStatus_Object = MibScalar
wrsRTUStatus = _WrsRTUStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 2, 3, 4),
    _WrsRTUStatus_Type()
)
wrsRTUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsRTUStatus.setStatus("current")
_WrsVersionGroup_ObjectIdentity = ObjectIdentity
wrsVersionGroup = _WrsVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3)
)


class _WrsVersionSwVersion_Type(DisplayString):
    """Custom type wrsVersionSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionSwVersion_Type.__name__ = "DisplayString"
_WrsVersionSwVersion_Object = MibScalar
wrsVersionSwVersion = _WrsVersionSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 1),
    _WrsVersionSwVersion_Type()
)
wrsVersionSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionSwVersion.setStatus("current")


class _WrsVersionSwBuildBy_Type(DisplayString):
    """Custom type wrsVersionSwBuildBy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionSwBuildBy_Type.__name__ = "DisplayString"
_WrsVersionSwBuildBy_Object = MibScalar
wrsVersionSwBuildBy = _WrsVersionSwBuildBy_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 2),
    _WrsVersionSwBuildBy_Type()
)
wrsVersionSwBuildBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionSwBuildBy.setStatus("current")


class _WrsVersionSwBuildDate_Type(DisplayString):
    """Custom type wrsVersionSwBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionSwBuildDate_Type.__name__ = "DisplayString"
_WrsVersionSwBuildDate_Object = MibScalar
wrsVersionSwBuildDate = _WrsVersionSwBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 3),
    _WrsVersionSwBuildDate_Type()
)
wrsVersionSwBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionSwBuildDate.setStatus("current")


class _WrsVersionBackplaneVersion_Type(DisplayString):
    """Custom type wrsVersionBackplaneVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionBackplaneVersion_Type.__name__ = "DisplayString"
_WrsVersionBackplaneVersion_Object = MibScalar
wrsVersionBackplaneVersion = _WrsVersionBackplaneVersion_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 4),
    _WrsVersionBackplaneVersion_Type()
)
wrsVersionBackplaneVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionBackplaneVersion.setStatus("current")


class _WrsVersionFpgaType_Type(DisplayString):
    """Custom type wrsVersionFpgaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionFpgaType_Type.__name__ = "DisplayString"
_WrsVersionFpgaType_Object = MibScalar
wrsVersionFpgaType = _WrsVersionFpgaType_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 5),
    _WrsVersionFpgaType_Type()
)
wrsVersionFpgaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionFpgaType.setStatus("current")


class _WrsVersionManufacturer_Type(DisplayString):
    """Custom type wrsVersionManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionManufacturer_Type.__name__ = "DisplayString"
_WrsVersionManufacturer_Object = MibScalar
wrsVersionManufacturer = _WrsVersionManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 6),
    _WrsVersionManufacturer_Type()
)
wrsVersionManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionManufacturer.setStatus("current")


class _WrsVersionSwitchSerialNumber_Type(DisplayString):
    """Custom type wrsVersionSwitchSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionSwitchSerialNumber_Type.__name__ = "DisplayString"
_WrsVersionSwitchSerialNumber_Object = MibScalar
wrsVersionSwitchSerialNumber = _WrsVersionSwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 7),
    _WrsVersionSwitchSerialNumber_Type()
)
wrsVersionSwitchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionSwitchSerialNumber.setStatus("current")


class _WrsVersionScbVersion_Type(DisplayString):
    """Custom type wrsVersionScbVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionScbVersion_Type.__name__ = "DisplayString"
_WrsVersionScbVersion_Object = MibScalar
wrsVersionScbVersion = _WrsVersionScbVersion_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 8),
    _WrsVersionScbVersion_Type()
)
wrsVersionScbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionScbVersion.setStatus("current")


class _WrsVersionGwVersion_Type(DisplayString):
    """Custom type wrsVersionGwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionGwVersion_Type.__name__ = "DisplayString"
_WrsVersionGwVersion_Object = MibScalar
wrsVersionGwVersion = _WrsVersionGwVersion_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 9),
    _WrsVersionGwVersion_Type()
)
wrsVersionGwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionGwVersion.setStatus("current")


class _WrsVersionGwBuild_Type(DisplayString):
    """Custom type wrsVersionGwBuild based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionGwBuild_Type.__name__ = "DisplayString"
_WrsVersionGwBuild_Object = MibScalar
wrsVersionGwBuild = _WrsVersionGwBuild_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 10),
    _WrsVersionGwBuild_Type()
)
wrsVersionGwBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionGwBuild.setStatus("current")


class _WrsVersionSwitchHdlCommitId_Type(DisplayString):
    """Custom type wrsVersionSwitchHdlCommitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionSwitchHdlCommitId_Type.__name__ = "DisplayString"
_WrsVersionSwitchHdlCommitId_Object = MibScalar
wrsVersionSwitchHdlCommitId = _WrsVersionSwitchHdlCommitId_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 11),
    _WrsVersionSwitchHdlCommitId_Type()
)
wrsVersionSwitchHdlCommitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionSwitchHdlCommitId.setStatus("current")


class _WrsVersionGeneralCoresCommitId_Type(DisplayString):
    """Custom type wrsVersionGeneralCoresCommitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionGeneralCoresCommitId_Type.__name__ = "DisplayString"
_WrsVersionGeneralCoresCommitId_Object = MibScalar
wrsVersionGeneralCoresCommitId = _WrsVersionGeneralCoresCommitId_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 12),
    _WrsVersionGeneralCoresCommitId_Type()
)
wrsVersionGeneralCoresCommitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionGeneralCoresCommitId.setStatus("current")


class _WrsVersionWrCoresCommitId_Type(DisplayString):
    """Custom type wrsVersionWrCoresCommitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionWrCoresCommitId_Type.__name__ = "DisplayString"
_WrsVersionWrCoresCommitId_Object = MibScalar
wrsVersionWrCoresCommitId = _WrsVersionWrCoresCommitId_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 13),
    _WrsVersionWrCoresCommitId_Type()
)
wrsVersionWrCoresCommitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionWrCoresCommitId.setStatus("current")


class _WrsVersionLastUpdateDate_Type(DisplayString):
    """Custom type wrsVersionLastUpdateDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsVersionLastUpdateDate_Type.__name__ = "DisplayString"
_WrsVersionLastUpdateDate_Object = MibScalar
wrsVersionLastUpdateDate = _WrsVersionLastUpdateDate_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 14),
    _WrsVersionLastUpdateDate_Type()
)
wrsVersionLastUpdateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionLastUpdateDate.setStatus("current")
_WrsVersionFeatures_Type = DisplayString
_WrsVersionFeatures_Object = MibScalar
wrsVersionFeatures = _WrsVersionFeatures_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 6, 3, 15),
    _WrsVersionFeatures_Type()
)
wrsVersionFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVersionFeatures.setStatus("current")
_WrsExpertStatus_ObjectIdentity = ObjectIdentity
wrsExpertStatus = _WrsExpertStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7)
)
_WrsOperationStatus_ObjectIdentity = ObjectIdentity
wrsOperationStatus = _WrsOperationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1)
)
_WrsCurrentTimeGroup_ObjectIdentity = ObjectIdentity
wrsCurrentTimeGroup = _WrsCurrentTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1)
)
_WrsDateTAI_Type = Counter64
_WrsDateTAI_Object = MibScalar
wrsDateTAI = _WrsDateTAI_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 1),
    _WrsDateTAI_Type()
)
wrsDateTAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDateTAI.setStatus("current")


class _WrsDateTAIString_Type(DisplayString):
    """Custom type wrsDateTAIString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsDateTAIString_Type.__name__ = "DisplayString"
_WrsDateTAIString_Object = MibScalar
wrsDateTAIString = _WrsDateTAIString_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 2),
    _WrsDateTAIString_Type()
)
wrsDateTAIString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDateTAIString.setStatus("current")


class _WrsSystemClockStatusDetails_Type(Integer32):
    """Custom type wrsSystemClockStatusDetails based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("thresholdExceeded", 2),
          ("ntpError", 3),
          ("error", 4),
          ("ioError", 5),
          ("unknownStatus", 6))
    )


_WrsSystemClockStatusDetails_Type.__name__ = "Integer32"
_WrsSystemClockStatusDetails_Object = MibScalar
wrsSystemClockStatusDetails = _WrsSystemClockStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 3),
    _WrsSystemClockStatusDetails_Type()
)
wrsSystemClockStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockStatusDetails.setStatus("current")
_WrsSystemClockDrift_Type = Integer32
_WrsSystemClockDrift_Object = MibScalar
wrsSystemClockDrift = _WrsSystemClockDrift_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 4),
    _WrsSystemClockDrift_Type()
)
wrsSystemClockDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockDrift.setStatus("current")
_WrsSystemClockDriftThreshold_Type = Integer32
_WrsSystemClockDriftThreshold_Object = MibScalar
wrsSystemClockDriftThreshold = _WrsSystemClockDriftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 5),
    _WrsSystemClockDriftThreshold_Type()
)
wrsSystemClockDriftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockDriftThreshold.setStatus("current")
_WrsSystemClockCheckInterval_Type = Integer32
_WrsSystemClockCheckInterval_Object = MibScalar
wrsSystemClockCheckInterval = _WrsSystemClockCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 6),
    _WrsSystemClockCheckInterval_Type()
)
wrsSystemClockCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockCheckInterval.setStatus("current")


class _WrsSystemClockCheckIntervalUnit_Type(Integer32):
    """Custom type wrsSystemClockCheckIntervalUnit based on Integer32"""
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
        *(("na", 0),
          ("error", 1),
          ("minutes", 2),
          ("hours", 3),
          ("days", 4))
    )


_WrsSystemClockCheckIntervalUnit_Type.__name__ = "Integer32"
_WrsSystemClockCheckIntervalUnit_Object = MibScalar
wrsSystemClockCheckIntervalUnit = _WrsSystemClockCheckIntervalUnit_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 7),
    _WrsSystemClockCheckIntervalUnit_Type()
)
wrsSystemClockCheckIntervalUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockCheckIntervalUnit.setStatus("current")


class _WrsLeapSecSource_Type(Integer32):
    """Custom type wrsLeapSecSource based on Integer32"""
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
        *(("na", 0),
          ("error", 1),
          ("errorMinor", 2),
          ("local", 3),
          ("tryRemote", 4),
          ("forceRemote", 5))
    )


_WrsLeapSecSource_Type.__name__ = "Integer32"
_WrsLeapSecSource_Object = MibScalar
wrsLeapSecSource = _WrsLeapSecSource_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 8),
    _WrsLeapSecSource_Type()
)
wrsLeapSecSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsLeapSecSource.setStatus("current")


class _WrsLeapSecStatusDetails_Type(Integer32):
    """Custom type wrsLeapSecStatusDetails based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("statusFileMissing", 2),
          ("unknownStatus", 3),
          ("leapSecFileExpired", 4),
          ("internalErrorDetected", 5),
          ("taiReadError", 6),
          ("leaSecInserted", 7),
          ("leapSecDeleted", 8))
    )


_WrsLeapSecStatusDetails_Type.__name__ = "Integer32"
_WrsLeapSecStatusDetails_Object = MibScalar
wrsLeapSecStatusDetails = _WrsLeapSecStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 9),
    _WrsLeapSecStatusDetails_Type()
)
wrsLeapSecStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsLeapSecStatusDetails.setStatus("current")


class _WrsLeapSecSourceStatusDetails_Type(Integer32):
    """Custom type wrsLeapSecSourceStatusDetails based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("statusFileMissing", 2),
          ("unknownStatus", 3),
          ("updated", 4),
          ("dhcpError", 5),
          ("invalidUrl", 6),
          ("invalidFile", 7),
          ("downloadError", 8))
    )


_WrsLeapSecSourceStatusDetails_Type.__name__ = "Integer32"
_WrsLeapSecSourceStatusDetails_Object = MibScalar
wrsLeapSecSourceStatusDetails = _WrsLeapSecSourceStatusDetails_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 10),
    _WrsLeapSecSourceStatusDetails_Type()
)
wrsLeapSecSourceStatusDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsLeapSecSourceStatusDetails.setStatus("current")


class _WrsLeapSecSourceURL_Type(DisplayString):
    """Custom type wrsLeapSecSourceURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WrsLeapSecSourceURL_Type.__name__ = "DisplayString"
_WrsLeapSecSourceURL_Object = MibScalar
wrsLeapSecSourceURL = _WrsLeapSecSourceURL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 11),
    _WrsLeapSecSourceURL_Type()
)
wrsLeapSecSourceURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsLeapSecSourceURL.setStatus("current")
_WrsSystemClockDriftUs_Type = Integer32
_WrsSystemClockDriftUs_Object = MibScalar
wrsSystemClockDriftUs = _WrsSystemClockDriftUs_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 1, 12),
    _WrsSystemClockDriftUs_Type()
)
wrsSystemClockDriftUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSystemClockDriftUs.setStatus("current")
_WrsBootStatusGroup_ObjectIdentity = ObjectIdentity
wrsBootStatusGroup = _WrsBootStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2)
)
_WrsBootCnt_Type = Counter32
_WrsBootCnt_Object = MibScalar
wrsBootCnt = _WrsBootCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 1),
    _WrsBootCnt_Type()
)
wrsBootCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootCnt.setStatus("current")
_WrsRebootCnt_Type = Counter32
_WrsRebootCnt_Object = MibScalar
wrsRebootCnt = _WrsRebootCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 2),
    _WrsRebootCnt_Type()
)
wrsRebootCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsRebootCnt.setStatus("current")


class _WrsRestartReason_Type(Integer32):
    """Custom type wrsRestartReason based on Integer32"""
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
        *(("na", 0),
          ("error", 1),
          ("generalReset", 2),
          ("wakeUpReset", 3),
          ("watchdogReset", 4),
          ("softwareReset", 5),
          ("userReset", 6),
          ("restartByMonit", 7))
    )


_WrsRestartReason_Type.__name__ = "Integer32"
_WrsRestartReason_Object = MibScalar
wrsRestartReason = _WrsRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 3),
    _WrsRestartReason_Type()
)
wrsRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsRestartReason.setStatus("current")


class _WrsFaultIP_Type(OctetString):
    """Custom type wrsFaultIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WrsFaultIP_Type.__name__ = "OctetString"
_WrsFaultIP_Object = MibScalar
wrsFaultIP = _WrsFaultIP_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 4),
    _WrsFaultIP_Type()
)
wrsFaultIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsFaultIP.setStatus("current")


class _WrsFaultLR_Type(OctetString):
    """Custom type wrsFaultLR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_WrsFaultLR_Type.__name__ = "OctetString"
_WrsFaultLR_Object = MibScalar
wrsFaultLR = _WrsFaultLR_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 5),
    _WrsFaultLR_Type()
)
wrsFaultLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsFaultLR.setStatus("current")


class _WrsConfigSource_Type(Integer32):
    """Custom type wrsConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("error", 1),
          ("errorMinor", 2),
          ("local", 3),
          ("remote", 4),
          ("tryDhcp", 5),
          ("forceDhcp", 6))
    )


_WrsConfigSource_Type.__name__ = "Integer32"
_WrsConfigSource_Object = MibScalar
wrsConfigSource = _WrsConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 6),
    _WrsConfigSource_Type()
)
wrsConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsConfigSource.setStatus("current")


class _WrsConfigSourceUrl_Type(DisplayString):
    """Custom type wrsConfigSourceUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WrsConfigSourceUrl_Type.__name__ = "DisplayString"
_WrsConfigSourceUrl_Object = MibScalar
wrsConfigSourceUrl = _WrsConfigSourceUrl_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 7),
    _WrsConfigSourceUrl_Type()
)
wrsConfigSourceUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsConfigSourceUrl.setStatus("current")


class _WrsRestartReasonMonit_Type(DisplayString):
    """Custom type wrsRestartReasonMonit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsRestartReasonMonit_Type.__name__ = "DisplayString"
_WrsRestartReasonMonit_Object = MibScalar
wrsRestartReasonMonit = _WrsRestartReasonMonit_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 8),
    _WrsRestartReasonMonit_Type()
)
wrsRestartReasonMonit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsRestartReasonMonit.setStatus("current")


class _WrsBootConfigStatus_Type(Integer32):
    """Custom type wrsBootConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("downloadError", 3),
          ("checkError", 4),
          ("errorMinor", 5),
          ("dhcpError", 6))
    )


_WrsBootConfigStatus_Type.__name__ = "Integer32"
_WrsBootConfigStatus_Object = MibScalar
wrsBootConfigStatus = _WrsBootConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 9),
    _WrsBootConfigStatus_Type()
)
wrsBootConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootConfigStatus.setStatus("current")


class _WrsBootHwinfoReadout_Type(Integer32):
    """Custom type wrsBootHwinfoReadout based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("errorMinor", 3),
          ("warning", 4))
    )


_WrsBootHwinfoReadout_Type.__name__ = "Integer32"
_WrsBootHwinfoReadout_Object = MibScalar
wrsBootHwinfoReadout = _WrsBootHwinfoReadout_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 10),
    _WrsBootHwinfoReadout_Type()
)
wrsBootHwinfoReadout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootHwinfoReadout.setStatus("current")


class _WrsBootLoadFPGA_Type(Integer32):
    """Custom type wrsBootLoadFPGA based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("errorMinor", 3),
          ("fileNotFound", 4))
    )


_WrsBootLoadFPGA_Type.__name__ = "Integer32"
_WrsBootLoadFPGA_Object = MibScalar
wrsBootLoadFPGA = _WrsBootLoadFPGA_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 11),
    _WrsBootLoadFPGA_Type()
)
wrsBootLoadFPGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootLoadFPGA.setStatus("current")


class _WrsBootLoadLM32_Type(Integer32):
    """Custom type wrsBootLoadLM32 based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("errorMinor", 3),
          ("fileNotFound", 4))
    )


_WrsBootLoadLM32_Type.__name__ = "Integer32"
_WrsBootLoadLM32_Object = MibScalar
wrsBootLoadLM32 = _WrsBootLoadLM32_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 12),
    _WrsBootLoadLM32_Type()
)
wrsBootLoadLM32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootLoadLM32.setStatus("current")


class _WrsBootKernelModulesMissing_Type(Integer32):
    """Custom type wrsBootKernelModulesMissing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("allKernelModulesPresent", 0)
    )


_WrsBootKernelModulesMissing_Type.__name__ = "Integer32"
_WrsBootKernelModulesMissing_Object = MibScalar
wrsBootKernelModulesMissing = _WrsBootKernelModulesMissing_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 13),
    _WrsBootKernelModulesMissing_Type()
)
wrsBootKernelModulesMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootKernelModulesMissing.setStatus("current")


class _WrsBootUserspaceDaemonsMissing_Type(Integer32):
    """Custom type wrsBootUserspaceDaemonsMissing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("allDaemonsPresent", 0)
    )


_WrsBootUserspaceDaemonsMissing_Type.__name__ = "Integer32"
_WrsBootUserspaceDaemonsMissing_Object = MibScalar
wrsBootUserspaceDaemonsMissing = _WrsBootUserspaceDaemonsMissing_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 14),
    _WrsBootUserspaceDaemonsMissing_Type()
)
wrsBootUserspaceDaemonsMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsBootUserspaceDaemonsMissing.setStatus("current")
_WrsGwWatchdogTimeouts_Type = Counter32
_WrsGwWatchdogTimeouts_Object = MibScalar
wrsGwWatchdogTimeouts = _WrsGwWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 15),
    _WrsGwWatchdogTimeouts_Type()
)
wrsGwWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsGwWatchdogTimeouts.setStatus("current")


class _WrsFwUpdateStatus_Type(Integer32):
    """Custom type wrsFwUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("ok", 1),
          ("checksumError", 2))
    )


_WrsFwUpdateStatus_Type.__name__ = "Integer32"
_WrsFwUpdateStatus_Object = MibScalar
wrsFwUpdateStatus = _WrsFwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 16),
    _WrsFwUpdateStatus_Type()
)
wrsFwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsFwUpdateStatus.setStatus("current")


class _WrsCustomBootScriptSource_Type(Integer32):
    """Custom type wrsCustomBootScriptSource based on Integer32"""
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
        *(("na", 0),
          ("error", 1),
          ("errorMinor", 2),
          ("local", 3),
          ("remote", 4),
          ("disabled", 5))
    )


_WrsCustomBootScriptSource_Type.__name__ = "Integer32"
_WrsCustomBootScriptSource_Object = MibScalar
wrsCustomBootScriptSource = _WrsCustomBootScriptSource_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 17),
    _WrsCustomBootScriptSource_Type()
)
wrsCustomBootScriptSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCustomBootScriptSource.setStatus("current")


class _WrsCustomBootScriptSourceUrl_Type(DisplayString):
    """Custom type wrsCustomBootScriptSourceUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WrsCustomBootScriptSourceUrl_Type.__name__ = "DisplayString"
_WrsCustomBootScriptSourceUrl_Object = MibScalar
wrsCustomBootScriptSourceUrl = _WrsCustomBootScriptSourceUrl_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 18),
    _WrsCustomBootScriptSourceUrl_Type()
)
wrsCustomBootScriptSourceUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCustomBootScriptSourceUrl.setStatus("current")


class _WrsCustomBootScriptStatus_Type(Integer32):
    """Custom type wrsCustomBootScriptStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("failed", 2),
          ("wrongSrc", 3),
          ("downloadError", 4),
          ("disabled", 5),
          ("error", 6),
          ("errorMinor", 7))
    )


_WrsCustomBootScriptStatus_Type.__name__ = "Integer32"
_WrsCustomBootScriptStatus_Object = MibScalar
wrsCustomBootScriptStatus = _WrsCustomBootScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 19),
    _WrsCustomBootScriptStatus_Type()
)
wrsCustomBootScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCustomBootScriptStatus.setStatus("current")


class _WrsAuxClkSetStatus_Type(Integer32):
    """Custom type wrsAuxClkSetStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("failed", 2),
          ("disabled", 3),
          ("error", 4),
          ("errorMinor", 5))
    )


_WrsAuxClkSetStatus_Type.__name__ = "Integer32"
_WrsAuxClkSetStatus_Object = MibScalar
wrsAuxClkSetStatus = _WrsAuxClkSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 20),
    _WrsAuxClkSetStatus_Type()
)
wrsAuxClkSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsAuxClkSetStatus.setStatus("current")


class _WrsThrottlingSetStatus_Type(Integer32):
    """Custom type wrsThrottlingSetStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("failed", 2),
          ("disabled", 3),
          ("error", 4),
          ("errorMinor", 5))
    )


_WrsThrottlingSetStatus_Type.__name__ = "Integer32"
_WrsThrottlingSetStatus_Object = MibScalar
wrsThrottlingSetStatus = _WrsThrottlingSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 21),
    _WrsThrottlingSetStatus_Type()
)
wrsThrottlingSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsThrottlingSetStatus.setStatus("current")


class _WrsVlansSetStatus_Type(Integer32):
    """Custom type wrsVlansSetStatus based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("failed", 2),
          ("disabled", 3),
          ("error", 4),
          ("errorMinor", 5))
    )


_WrsVlansSetStatus_Type.__name__ = "Integer32"
_WrsVlansSetStatus_Object = MibScalar
wrsVlansSetStatus = _WrsVlansSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 2, 22),
    _WrsVlansSetStatus_Type()
)
wrsVlansSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsVlansSetStatus.setStatus("current")
_WrsTemperatureGroup_ObjectIdentity = ObjectIdentity
wrsTemperatureGroup = _WrsTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3)
)
_WrsTempFPGA_Type = Integer32
_WrsTempFPGA_Object = MibScalar
wrsTempFPGA = _WrsTempFPGA_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 1),
    _WrsTempFPGA_Type()
)
wrsTempFPGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempFPGA.setStatus("current")
_WrsTempPLL_Type = Integer32
_WrsTempPLL_Object = MibScalar
wrsTempPLL = _WrsTempPLL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 2),
    _WrsTempPLL_Type()
)
wrsTempPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempPLL.setStatus("current")
_WrsTempPSL_Type = Integer32
_WrsTempPSL_Object = MibScalar
wrsTempPSL = _WrsTempPSL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 3),
    _WrsTempPSL_Type()
)
wrsTempPSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempPSL.setStatus("current")
_WrsTempPSR_Type = Integer32
_WrsTempPSR_Object = MibScalar
wrsTempPSR = _WrsTempPSR_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 4),
    _WrsTempPSR_Type()
)
wrsTempPSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempPSR.setStatus("current")
_WrsTempThresholdFPGA_Type = Integer32
_WrsTempThresholdFPGA_Object = MibScalar
wrsTempThresholdFPGA = _WrsTempThresholdFPGA_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 5),
    _WrsTempThresholdFPGA_Type()
)
wrsTempThresholdFPGA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempThresholdFPGA.setStatus("current")
_WrsTempThresholdPLL_Type = Integer32
_WrsTempThresholdPLL_Object = MibScalar
wrsTempThresholdPLL = _WrsTempThresholdPLL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 6),
    _WrsTempThresholdPLL_Type()
)
wrsTempThresholdPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempThresholdPLL.setStatus("current")
_WrsTempThresholdPSL_Type = Integer32
_WrsTempThresholdPSL_Object = MibScalar
wrsTempThresholdPSL = _WrsTempThresholdPSL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 7),
    _WrsTempThresholdPSL_Type()
)
wrsTempThresholdPSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempThresholdPSL.setStatus("current")
_WrsTempThresholdPSR_Type = Integer32
_WrsTempThresholdPSR_Object = MibScalar
wrsTempThresholdPSR = _WrsTempThresholdPSR_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 3, 8),
    _WrsTempThresholdPSR_Type()
)
wrsTempThresholdPSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsTempThresholdPSR.setStatus("current")
_WrsMemoryGroup_ObjectIdentity = ObjectIdentity
wrsMemoryGroup = _WrsMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 4)
)
_WrsMemoryTotal_Type = Integer32
_WrsMemoryTotal_Object = MibScalar
wrsMemoryTotal = _WrsMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 4, 1),
    _WrsMemoryTotal_Type()
)
wrsMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMemoryTotal.setStatus("current")
_WrsMemoryUsed_Type = Integer32
_WrsMemoryUsed_Object = MibScalar
wrsMemoryUsed = _WrsMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 4, 2),
    _WrsMemoryUsed_Type()
)
wrsMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMemoryUsed.setStatus("current")
_WrsMemoryUsedPerc_Type = Integer32
_WrsMemoryUsedPerc_Object = MibScalar
wrsMemoryUsedPerc = _WrsMemoryUsedPerc_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 4, 3),
    _WrsMemoryUsedPerc_Type()
)
wrsMemoryUsedPerc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMemoryUsedPerc.setStatus("current")
_WrsMemoryFree_Type = Integer32
_WrsMemoryFree_Object = MibScalar
wrsMemoryFree = _WrsMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 4, 4),
    _WrsMemoryFree_Type()
)
wrsMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsMemoryFree.setStatus("current")
_WrsCpuLoadGroup_ObjectIdentity = ObjectIdentity
wrsCpuLoadGroup = _WrsCpuLoadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 5)
)
_WrsCPULoadAvg1min_Type = Integer32
_WrsCPULoadAvg1min_Object = MibScalar
wrsCPULoadAvg1min = _WrsCPULoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 5, 1),
    _WrsCPULoadAvg1min_Type()
)
wrsCPULoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCPULoadAvg1min.setStatus("current")
_WrsCPULoadAvg5min_Type = Integer32
_WrsCPULoadAvg5min_Object = MibScalar
wrsCPULoadAvg5min = _WrsCPULoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 5, 2),
    _WrsCPULoadAvg5min_Type()
)
wrsCPULoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCPULoadAvg5min.setStatus("current")
_WrsCPULoadAvg15min_Type = Integer32
_WrsCPULoadAvg15min_Object = MibScalar
wrsCPULoadAvg15min = _WrsCPULoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 5, 3),
    _WrsCPULoadAvg15min_Type()
)
wrsCPULoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsCPULoadAvg15min.setStatus("current")
_WrsDiskTable_Object = MibTable
wrsDiskTable = _WrsDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6)
)
if mibBuilder.loadTexts:
    wrsDiskTable.setStatus("current")
_WrsDiskEntry_Object = MibTableRow
wrsDiskEntry = _WrsDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1)
)
wrsDiskEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsDiskIndex"),
)
if mibBuilder.loadTexts:
    wrsDiskEntry.setStatus("current")
_WrsDiskIndex_Type = Unsigned32
_WrsDiskIndex_Object = MibTableColumn
wrsDiskIndex = _WrsDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 1),
    _WrsDiskIndex_Type()
)
wrsDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsDiskIndex.setStatus("current")


class _WrsDiskMountPath_Type(DisplayString):
    """Custom type wrsDiskMountPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsDiskMountPath_Type.__name__ = "DisplayString"
_WrsDiskMountPath_Object = MibTableColumn
wrsDiskMountPath = _WrsDiskMountPath_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 2),
    _WrsDiskMountPath_Type()
)
wrsDiskMountPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskMountPath.setStatus("current")
_WrsDiskSize_Type = Integer32
_WrsDiskSize_Object = MibTableColumn
wrsDiskSize = _WrsDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 3),
    _WrsDiskSize_Type()
)
wrsDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskSize.setStatus("current")
_WrsDiskUsed_Type = Integer32
_WrsDiskUsed_Object = MibTableColumn
wrsDiskUsed = _WrsDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 4),
    _WrsDiskUsed_Type()
)
wrsDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskUsed.setStatus("current")
_WrsDiskFree_Type = Integer32
_WrsDiskFree_Object = MibTableColumn
wrsDiskFree = _WrsDiskFree_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 5),
    _WrsDiskFree_Type()
)
wrsDiskFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskFree.setStatus("current")
_WrsDiskUseRate_Type = Integer32
_WrsDiskUseRate_Object = MibTableColumn
wrsDiskUseRate = _WrsDiskUseRate_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 6),
    _WrsDiskUseRate_Type()
)
wrsDiskUseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskUseRate.setStatus("current")


class _WrsDiskFilesystem_Type(DisplayString):
    """Custom type wrsDiskFilesystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WrsDiskFilesystem_Type.__name__ = "DisplayString"
_WrsDiskFilesystem_Object = MibTableColumn
wrsDiskFilesystem = _WrsDiskFilesystem_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 1, 6, 1, 7),
    _WrsDiskFilesystem_Type()
)
wrsDiskFilesystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsDiskFilesystem.setStatus("current")
_WrsStartCntGroup_ObjectIdentity = ObjectIdentity
wrsStartCntGroup = _WrsStartCntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2)
)
_WrsStartCntHAL_Type = Counter32
_WrsStartCntHAL_Object = MibScalar
wrsStartCntHAL = _WrsStartCntHAL_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 1),
    _WrsStartCntHAL_Type()
)
wrsStartCntHAL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntHAL.setStatus("current")
_WrsStartCntPTP_Type = Counter32
_WrsStartCntPTP_Object = MibScalar
wrsStartCntPTP = _WrsStartCntPTP_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 2),
    _WrsStartCntPTP_Type()
)
wrsStartCntPTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntPTP.setStatus("current")
_WrsStartCntRTUd_Type = Counter32
_WrsStartCntRTUd_Object = MibScalar
wrsStartCntRTUd = _WrsStartCntRTUd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 3),
    _WrsStartCntRTUd_Type()
)
wrsStartCntRTUd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntRTUd.setStatus("current")
_WrsStartCntSshd_Type = Counter32
_WrsStartCntSshd_Object = MibScalar
wrsStartCntSshd = _WrsStartCntSshd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 4),
    _WrsStartCntSshd_Type()
)
wrsStartCntSshd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntSshd.setStatus("current")
_WrsStartCntHttpd_Type = Counter32
_WrsStartCntHttpd_Object = MibScalar
wrsStartCntHttpd = _WrsStartCntHttpd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 5),
    _WrsStartCntHttpd_Type()
)
wrsStartCntHttpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntHttpd.setStatus("current")
_WrsStartCntSnmpd_Type = Counter32
_WrsStartCntSnmpd_Object = MibScalar
wrsStartCntSnmpd = _WrsStartCntSnmpd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 6),
    _WrsStartCntSnmpd_Type()
)
wrsStartCntSnmpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntSnmpd.setStatus("current")
_WrsStartCntSyslogd_Type = Counter32
_WrsStartCntSyslogd_Object = MibScalar
wrsStartCntSyslogd = _WrsStartCntSyslogd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 7),
    _WrsStartCntSyslogd_Type()
)
wrsStartCntSyslogd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntSyslogd.setStatus("current")
_WrsStartCntWrsWatchdog_Type = Counter32
_WrsStartCntWrsWatchdog_Object = MibScalar
wrsStartCntWrsWatchdog = _WrsStartCntWrsWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 8),
    _WrsStartCntWrsWatchdog_Type()
)
wrsStartCntWrsWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntWrsWatchdog.setStatus("current")
_WrsStartCntLldpd_Type = Counter32
_WrsStartCntLldpd_Object = MibScalar
wrsStartCntLldpd = _WrsStartCntLldpd_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 9),
    _WrsStartCntLldpd_Type()
)
wrsStartCntLldpd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntLldpd.setStatus("current")
_WrsStartCntLdap_Type = Counter32
_WrsStartCntLdap_Object = MibScalar
wrsStartCntLdap = _WrsStartCntLdap_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 10),
    _WrsStartCntLdap_Type()
)
wrsStartCntLdap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntLdap.setStatus("current")
_WrsStartCntRvlan_Type = Counter32
_WrsStartCntRvlan_Object = MibScalar
wrsStartCntRvlan = _WrsStartCntRvlan_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 2, 11),
    _WrsStartCntRvlan_Type()
)
wrsStartCntRvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsStartCntRvlan.setStatus("current")
_WrsSpllState_ObjectIdentity = ObjectIdentity
wrsSpllState = _WrsSpllState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3)
)
_WrsSpllVersionGroup_ObjectIdentity = ObjectIdentity
wrsSpllVersionGroup = _WrsSpllVersionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 1)
)


class _WrsSpllVersion_Type(DisplayString):
    """Custom type wrsSpllVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsSpllVersion_Type.__name__ = "DisplayString"
_WrsSpllVersion_Object = MibScalar
wrsSpllVersion = _WrsSpllVersion_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 1, 1),
    _WrsSpllVersion_Type()
)
wrsSpllVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllVersion.setStatus("current")


class _WrsSpllBuildDate_Type(DisplayString):
    """Custom type wrsSpllBuildDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsSpllBuildDate_Type.__name__ = "DisplayString"
_WrsSpllBuildDate_Object = MibScalar
wrsSpllBuildDate = _WrsSpllBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 1, 2),
    _WrsSpllBuildDate_Type()
)
wrsSpllBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllBuildDate.setStatus("current")


class _WrsSpllBuildBy_Type(DisplayString):
    """Custom type wrsSpllBuildBy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsSpllBuildBy_Type.__name__ = "DisplayString"
_WrsSpllBuildBy_Object = MibScalar
wrsSpllBuildBy = _WrsSpllBuildBy_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 1, 3),
    _WrsSpllBuildBy_Type()
)
wrsSpllBuildBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllBuildBy.setStatus("current")
_WrsSpllStatusGroup_ObjectIdentity = ObjectIdentity
wrsSpllStatusGroup = _WrsSpllStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2)
)


class _WrsSpllMode_Type(Integer32):
    """Custom type wrsSpllMode based on Integer32"""
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
        *(("na", 0),
          ("grandmaster", 1),
          ("master", 2),
          ("slave", 3),
          ("disabled", 4))
    )


_WrsSpllMode_Type.__name__ = "Integer32"
_WrsSpllMode_Object = MibScalar
wrsSpllMode = _WrsSpllMode_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 1),
    _WrsSpllMode_Type()
)
wrsSpllMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllMode.setStatus("current")
_WrsSpllIrqCnt_Type = Counter32
_WrsSpllIrqCnt_Object = MibScalar
wrsSpllIrqCnt = _WrsSpllIrqCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 2),
    _WrsSpllIrqCnt_Type()
)
wrsSpllIrqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllIrqCnt.setStatus("current")


class _WrsSpllSeqState_Type(Integer32):
    """Custom type wrsSpllSeqState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("startExt", 1),
          ("waitExt", 2),
          ("startHelper", 3),
          ("waitHelper", 4),
          ("startMain", 5),
          ("waitMain", 6),
          ("disabled", 7),
          ("ready", 8),
          ("clearDacs", 9),
          ("waitClearDacs", 10))
    )


_WrsSpllSeqState_Type.__name__ = "Integer32"
_WrsSpllSeqState_Object = MibScalar
wrsSpllSeqState = _WrsSpllSeqState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 3),
    _WrsSpllSeqState_Type()
)
wrsSpllSeqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllSeqState.setStatus("current")


class _WrsSpllAlignState_Type(Integer32):
    """Custom type wrsSpllAlignState based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("extOff", 0),
          ("start", 1),
          ("initCsync", 2),
          ("waitCsync", 3),
          ("waitSample", 4),
          ("compensateDelay", 5),
          ("locked", 6),
          ("startAlignment", 7),
          ("startMain", 8),
          ("waitClkIn", 9),
          ("waitPlock", 10))
    )


_WrsSpllAlignState_Type.__name__ = "Integer32"
_WrsSpllAlignState_Object = MibScalar
wrsSpllAlignState = _WrsSpllAlignState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 4),
    _WrsSpllAlignState_Type()
)
wrsSpllAlignState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllAlignState.setStatus("current")
_WrsSpllHlock_Type = Counter32
_WrsSpllHlock_Object = MibScalar
wrsSpllHlock = _WrsSpllHlock_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 5),
    _WrsSpllHlock_Type()
)
wrsSpllHlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllHlock.setStatus("current")
_WrsSpllMlock_Type = Counter32
_WrsSpllMlock_Object = MibScalar
wrsSpllMlock = _WrsSpllMlock_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 6),
    _WrsSpllMlock_Type()
)
wrsSpllMlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllMlock.setStatus("current")
_WrsSpllHY_Type = Integer32
_WrsSpllHY_Object = MibScalar
wrsSpllHY = _WrsSpllHY_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 7),
    _WrsSpllHY_Type()
)
wrsSpllHY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllHY.setStatus("current")
_WrsSpllMY_Type = Integer32
_WrsSpllMY_Object = MibScalar
wrsSpllMY = _WrsSpllMY_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 8),
    _WrsSpllMY_Type()
)
wrsSpllMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllMY.setStatus("current")
_WrsSpllDelCnt_Type = Counter32
_WrsSpllDelCnt_Object = MibScalar
wrsSpllDelCnt = _WrsSpllDelCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 3, 2, 9),
    _WrsSpllDelCnt_Type()
)
wrsSpllDelCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsSpllDelCnt.setStatus("current")
_WrsPstatsTable_Object = MibTable
wrsPstatsTable = _WrsPstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4)
)
if mibBuilder.loadTexts:
    wrsPstatsTable.setStatus("deprecated")
_WrsPstatsEntry_Object = MibTableRow
wrsPstatsEntry = _WrsPstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1)
)
wrsPstatsEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsPstatsIndex"),
)
if mibBuilder.loadTexts:
    wrsPstatsEntry.setStatus("deprecated")
_WrsPstatsIndex_Type = Unsigned32
_WrsPstatsIndex_Object = MibTableColumn
wrsPstatsIndex = _WrsPstatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 1),
    _WrsPstatsIndex_Type()
)
wrsPstatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPstatsIndex.setStatus("deprecated")


class _WrsPstatsPortName_Type(DisplayString):
    """Custom type wrsPstatsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPstatsPortName_Type.__name__ = "DisplayString"
_WrsPstatsPortName_Object = MibTableColumn
wrsPstatsPortName = _WrsPstatsPortName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 2),
    _WrsPstatsPortName_Type()
)
wrsPstatsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsPortName.setStatus("deprecated")
_WrsPstatsTXUnderrun_Type = Counter32
_WrsPstatsTXUnderrun_Object = MibTableColumn
wrsPstatsTXUnderrun = _WrsPstatsTXUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 3),
    _WrsPstatsTXUnderrun_Type()
)
wrsPstatsTXUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsTXUnderrun.setStatus("deprecated")
_WrsPstatsRXOverrun_Type = Counter32
_WrsPstatsRXOverrun_Object = MibTableColumn
wrsPstatsRXOverrun = _WrsPstatsRXOverrun_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 4),
    _WrsPstatsRXOverrun_Type()
)
wrsPstatsRXOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXOverrun.setStatus("deprecated")
_WrsPstatsRXInvalidCode_Type = Counter32
_WrsPstatsRXInvalidCode_Object = MibTableColumn
wrsPstatsRXInvalidCode = _WrsPstatsRXInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 5),
    _WrsPstatsRXInvalidCode_Type()
)
wrsPstatsRXInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXInvalidCode.setStatus("deprecated")
_WrsPstatsRXSyncLost_Type = Counter32
_WrsPstatsRXSyncLost_Object = MibTableColumn
wrsPstatsRXSyncLost = _WrsPstatsRXSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 6),
    _WrsPstatsRXSyncLost_Type()
)
wrsPstatsRXSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXSyncLost.setStatus("deprecated")
_WrsPstatsRXPauseFrames_Type = Counter32
_WrsPstatsRXPauseFrames_Object = MibTableColumn
wrsPstatsRXPauseFrames = _WrsPstatsRXPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 7),
    _WrsPstatsRXPauseFrames_Type()
)
wrsPstatsRXPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPauseFrames.setStatus("deprecated")
_WrsPstatsRXPfilterDropped_Type = Counter32
_WrsPstatsRXPfilterDropped_Object = MibTableColumn
wrsPstatsRXPfilterDropped = _WrsPstatsRXPfilterDropped_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 8),
    _WrsPstatsRXPfilterDropped_Type()
)
wrsPstatsRXPfilterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPfilterDropped.setStatus("deprecated")
_WrsPstatsRXPCSErrors_Type = Counter32
_WrsPstatsRXPCSErrors_Object = MibTableColumn
wrsPstatsRXPCSErrors = _WrsPstatsRXPCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 9),
    _WrsPstatsRXPCSErrors_Type()
)
wrsPstatsRXPCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPCSErrors.setStatus("deprecated")
_WrsPstatsRXGiantFrames_Type = Counter32
_WrsPstatsRXGiantFrames_Object = MibTableColumn
wrsPstatsRXGiantFrames = _WrsPstatsRXGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 10),
    _WrsPstatsRXGiantFrames_Type()
)
wrsPstatsRXGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXGiantFrames.setStatus("deprecated")
_WrsPstatsRXRuntFrames_Type = Counter32
_WrsPstatsRXRuntFrames_Object = MibTableColumn
wrsPstatsRXRuntFrames = _WrsPstatsRXRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 11),
    _WrsPstatsRXRuntFrames_Type()
)
wrsPstatsRXRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXRuntFrames.setStatus("deprecated")
_WrsPstatsRXCRCErrors_Type = Counter32
_WrsPstatsRXCRCErrors_Object = MibTableColumn
wrsPstatsRXCRCErrors = _WrsPstatsRXCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 12),
    _WrsPstatsRXCRCErrors_Type()
)
wrsPstatsRXCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXCRCErrors.setStatus("deprecated")
_WrsPstatsRXPclass0_Type = Counter32
_WrsPstatsRXPclass0_Object = MibTableColumn
wrsPstatsRXPclass0 = _WrsPstatsRXPclass0_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 13),
    _WrsPstatsRXPclass0_Type()
)
wrsPstatsRXPclass0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass0.setStatus("deprecated")
_WrsPstatsRXPclass1_Type = Counter32
_WrsPstatsRXPclass1_Object = MibTableColumn
wrsPstatsRXPclass1 = _WrsPstatsRXPclass1_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 14),
    _WrsPstatsRXPclass1_Type()
)
wrsPstatsRXPclass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass1.setStatus("deprecated")
_WrsPstatsRXPclass2_Type = Counter32
_WrsPstatsRXPclass2_Object = MibTableColumn
wrsPstatsRXPclass2 = _WrsPstatsRXPclass2_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 15),
    _WrsPstatsRXPclass2_Type()
)
wrsPstatsRXPclass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass2.setStatus("deprecated")
_WrsPstatsRXPclass3_Type = Counter32
_WrsPstatsRXPclass3_Object = MibTableColumn
wrsPstatsRXPclass3 = _WrsPstatsRXPclass3_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 16),
    _WrsPstatsRXPclass3_Type()
)
wrsPstatsRXPclass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass3.setStatus("deprecated")
_WrsPstatsRXPclass4_Type = Counter32
_WrsPstatsRXPclass4_Object = MibTableColumn
wrsPstatsRXPclass4 = _WrsPstatsRXPclass4_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 17),
    _WrsPstatsRXPclass4_Type()
)
wrsPstatsRXPclass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass4.setStatus("deprecated")
_WrsPstatsRXPclass5_Type = Counter32
_WrsPstatsRXPclass5_Object = MibTableColumn
wrsPstatsRXPclass5 = _WrsPstatsRXPclass5_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 18),
    _WrsPstatsRXPclass5_Type()
)
wrsPstatsRXPclass5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass5.setStatus("deprecated")
_WrsPstatsRXPclass6_Type = Counter32
_WrsPstatsRXPclass6_Object = MibTableColumn
wrsPstatsRXPclass6 = _WrsPstatsRXPclass6_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 19),
    _WrsPstatsRXPclass6_Type()
)
wrsPstatsRXPclass6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass6.setStatus("deprecated")
_WrsPstatsRXPclass7_Type = Counter32
_WrsPstatsRXPclass7_Object = MibTableColumn
wrsPstatsRXPclass7 = _WrsPstatsRXPclass7_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 20),
    _WrsPstatsRXPclass7_Type()
)
wrsPstatsRXPclass7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPclass7.setStatus("deprecated")
_WrsPstatsTXFrames_Type = Counter32
_WrsPstatsTXFrames_Object = MibTableColumn
wrsPstatsTXFrames = _WrsPstatsTXFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 21),
    _WrsPstatsTXFrames_Type()
)
wrsPstatsTXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsTXFrames.setStatus("deprecated")
_WrsPstatsRXFrames_Type = Counter32
_WrsPstatsRXFrames_Object = MibTableColumn
wrsPstatsRXFrames = _WrsPstatsRXFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 22),
    _WrsPstatsRXFrames_Type()
)
wrsPstatsRXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXFrames.setStatus("deprecated")
_WrsPstatsRXDropRTUFull_Type = Counter32
_WrsPstatsRXDropRTUFull_Object = MibTableColumn
wrsPstatsRXDropRTUFull = _WrsPstatsRXDropRTUFull_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 23),
    _WrsPstatsRXDropRTUFull_Type()
)
wrsPstatsRXDropRTUFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXDropRTUFull.setStatus("deprecated")
_WrsPstatsRXPrio0_Type = Counter32
_WrsPstatsRXPrio0_Object = MibTableColumn
wrsPstatsRXPrio0 = _WrsPstatsRXPrio0_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 24),
    _WrsPstatsRXPrio0_Type()
)
wrsPstatsRXPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio0.setStatus("deprecated")
_WrsPstatsRXPrio1_Type = Counter32
_WrsPstatsRXPrio1_Object = MibTableColumn
wrsPstatsRXPrio1 = _WrsPstatsRXPrio1_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 25),
    _WrsPstatsRXPrio1_Type()
)
wrsPstatsRXPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio1.setStatus("deprecated")
_WrsPstatsRXPrio2_Type = Counter32
_WrsPstatsRXPrio2_Object = MibTableColumn
wrsPstatsRXPrio2 = _WrsPstatsRXPrio2_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 26),
    _WrsPstatsRXPrio2_Type()
)
wrsPstatsRXPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio2.setStatus("deprecated")
_WrsPstatsRXPrio3_Type = Counter32
_WrsPstatsRXPrio3_Object = MibTableColumn
wrsPstatsRXPrio3 = _WrsPstatsRXPrio3_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 27),
    _WrsPstatsRXPrio3_Type()
)
wrsPstatsRXPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio3.setStatus("deprecated")
_WrsPstatsRXPrio4_Type = Counter32
_WrsPstatsRXPrio4_Object = MibTableColumn
wrsPstatsRXPrio4 = _WrsPstatsRXPrio4_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 28),
    _WrsPstatsRXPrio4_Type()
)
wrsPstatsRXPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio4.setStatus("deprecated")
_WrsPstatsRXPrio5_Type = Counter32
_WrsPstatsRXPrio5_Object = MibTableColumn
wrsPstatsRXPrio5 = _WrsPstatsRXPrio5_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 29),
    _WrsPstatsRXPrio5_Type()
)
wrsPstatsRXPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio5.setStatus("deprecated")
_WrsPstatsRXPrio6_Type = Counter32
_WrsPstatsRXPrio6_Object = MibTableColumn
wrsPstatsRXPrio6 = _WrsPstatsRXPrio6_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 30),
    _WrsPstatsRXPrio6_Type()
)
wrsPstatsRXPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio6.setStatus("deprecated")
_WrsPstatsRXPrio7_Type = Counter32
_WrsPstatsRXPrio7_Object = MibTableColumn
wrsPstatsRXPrio7 = _WrsPstatsRXPrio7_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 31),
    _WrsPstatsRXPrio7_Type()
)
wrsPstatsRXPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRXPrio7.setStatus("deprecated")
_WrsPstatsRTUValid_Type = Counter32
_WrsPstatsRTUValid_Object = MibTableColumn
wrsPstatsRTUValid = _WrsPstatsRTUValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 32),
    _WrsPstatsRTUValid_Type()
)
wrsPstatsRTUValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRTUValid.setStatus("deprecated")
_WrsPstatsRTUResponses_Type = Counter32
_WrsPstatsRTUResponses_Object = MibTableColumn
wrsPstatsRTUResponses = _WrsPstatsRTUResponses_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 33),
    _WrsPstatsRTUResponses_Type()
)
wrsPstatsRTUResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRTUResponses.setStatus("deprecated")
_WrsPstatsRTUDropped_Type = Counter32
_WrsPstatsRTUDropped_Object = MibTableColumn
wrsPstatsRTUDropped = _WrsPstatsRTUDropped_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 34),
    _WrsPstatsRTUDropped_Type()
)
wrsPstatsRTUDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsRTUDropped.setStatus("deprecated")
_WrsPstatsFastMatchPriority_Type = Counter32
_WrsPstatsFastMatchPriority_Object = MibTableColumn
wrsPstatsFastMatchPriority = _WrsPstatsFastMatchPriority_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 35),
    _WrsPstatsFastMatchPriority_Type()
)
wrsPstatsFastMatchPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsFastMatchPriority.setStatus("deprecated")
_WrsPstatsFastMatchFastForward_Type = Counter32
_WrsPstatsFastMatchFastForward_Object = MibTableColumn
wrsPstatsFastMatchFastForward = _WrsPstatsFastMatchFastForward_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 36),
    _WrsPstatsFastMatchFastForward_Type()
)
wrsPstatsFastMatchFastForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsFastMatchFastForward.setStatus("deprecated")
_WrsPstatsFastMatchNonForward_Type = Counter32
_WrsPstatsFastMatchNonForward_Object = MibTableColumn
wrsPstatsFastMatchNonForward = _WrsPstatsFastMatchNonForward_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 37),
    _WrsPstatsFastMatchNonForward_Type()
)
wrsPstatsFastMatchNonForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsFastMatchNonForward.setStatus("deprecated")
_WrsPstatsFastMatchRespValid_Type = Counter32
_WrsPstatsFastMatchRespValid_Object = MibTableColumn
wrsPstatsFastMatchRespValid = _WrsPstatsFastMatchRespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 38),
    _WrsPstatsFastMatchRespValid_Type()
)
wrsPstatsFastMatchRespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsFastMatchRespValid.setStatus("deprecated")
_WrsPstatsFullMatchRespValid_Type = Counter32
_WrsPstatsFullMatchRespValid_Object = MibTableColumn
wrsPstatsFullMatchRespValid = _WrsPstatsFullMatchRespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 39),
    _WrsPstatsFullMatchRespValid_Type()
)
wrsPstatsFullMatchRespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsFullMatchRespValid.setStatus("deprecated")
_WrsPstatsForwarded_Type = Counter32
_WrsPstatsForwarded_Object = MibTableColumn
wrsPstatsForwarded = _WrsPstatsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 40),
    _WrsPstatsForwarded_Type()
)
wrsPstatsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsForwarded.setStatus("deprecated")
_WrsPstatsTRURespValid_Type = Counter32
_WrsPstatsTRURespValid_Object = MibTableColumn
wrsPstatsTRURespValid = _WrsPstatsTRURespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 4, 1, 41),
    _WrsPstatsTRURespValid_Type()
)
wrsPstatsTRURespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsTRURespValid.setStatus("deprecated")
_WrsPtpDataTable_Object = MibTable
wrsPtpDataTable = _WrsPtpDataTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5)
)
if mibBuilder.loadTexts:
    wrsPtpDataTable.setStatus("current")
_WrsPtpDataEntry_Object = MibTableRow
wrsPtpDataEntry = _WrsPtpDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1)
)
wrsPtpDataEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsPtpDataIndex"),
)
if mibBuilder.loadTexts:
    wrsPtpDataEntry.setStatus("current")
_WrsPtpDataIndex_Type = Unsigned32
_WrsPtpDataIndex_Object = MibTableColumn
wrsPtpDataIndex = _WrsPtpDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 1),
    _WrsPtpDataIndex_Type()
)
wrsPtpDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPtpDataIndex.setStatus("current")


class _WrsPtpPortName_Type(DisplayString):
    """Custom type wrsPtpPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPtpPortName_Type.__name__ = "DisplayString"
_WrsPtpPortName_Object = MibTableColumn
wrsPtpPortName = _WrsPtpPortName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 2),
    _WrsPtpPortName_Type()
)
wrsPtpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpPortName.setStatus("current")


class _WrsPtpGrandmasterID_Type(OctetString):
    """Custom type wrsPtpGrandmasterID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_WrsPtpGrandmasterID_Type.__name__ = "OctetString"
_WrsPtpGrandmasterID_Object = MibTableColumn
wrsPtpGrandmasterID = _WrsPtpGrandmasterID_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 3),
    _WrsPtpGrandmasterID_Type()
)
wrsPtpGrandmasterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpGrandmasterID.setStatus("current")


class _WrsPtpOwnID_Type(OctetString):
    """Custom type wrsPtpOwnID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_WrsPtpOwnID_Type.__name__ = "OctetString"
_WrsPtpOwnID_Object = MibTableColumn
wrsPtpOwnID = _WrsPtpOwnID_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 4),
    _WrsPtpOwnID_Type()
)
wrsPtpOwnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpOwnID.setStatus("current")


class _WrsPtpMode_Type(Integer32):
    """Custom type wrsPtpMode based on Integer32"""
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
        *(("unknown", 0),
          ("grandmaster", 1),
          ("master", 2),
          ("slave", 3))
    )


_WrsPtpMode_Type.__name__ = "Integer32"
_WrsPtpMode_Object = MibTableColumn
wrsPtpMode = _WrsPtpMode_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 5),
    _WrsPtpMode_Type()
)
wrsPtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpMode.setStatus("obsolete")


class _WrsPtpServoState_Type(DisplayString):
    """Custom type wrsPtpServoState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsPtpServoState_Type.__name__ = "DisplayString"
_WrsPtpServoState_Object = MibTableColumn
wrsPtpServoState = _WrsPtpServoState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 6),
    _WrsPtpServoState_Type()
)
wrsPtpServoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoState.setStatus("current")


class _WrsPtpServoStateN_Type(Integer32):
    """Custom type wrsPtpServoStateN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("uninitialized", 0),
          ("syncNsec", 1),
          ("syncSec", 2),
          ("syncPhase", 3),
          ("trackPhase", 4),
          ("waitOffsetStable", 5),
          ("standardPTP", 99))
    )


_WrsPtpServoStateN_Type.__name__ = "Integer32"
_WrsPtpServoStateN_Object = MibTableColumn
wrsPtpServoStateN = _WrsPtpServoStateN_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 7),
    _WrsPtpServoStateN_Type()
)
wrsPtpServoStateN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoStateN.setStatus("current")


class _WrsPtpPhaseTracking_Type(Integer32):
    """Custom type wrsPtpPhaseTracking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("notTracking", 1),
          ("tracking", 2))
    )


_WrsPtpPhaseTracking_Type.__name__ = "Integer32"
_WrsPtpPhaseTracking_Object = MibTableColumn
wrsPtpPhaseTracking = _WrsPtpPhaseTracking_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 8),
    _WrsPtpPhaseTracking_Type()
)
wrsPtpPhaseTracking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpPhaseTracking.setStatus("current")


class _WrsPtpSyncSource_Type(DisplayString):
    """Custom type wrsPtpSyncSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsPtpSyncSource_Type.__name__ = "DisplayString"
_WrsPtpSyncSource_Object = MibTableColumn
wrsPtpSyncSource = _WrsPtpSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 9),
    _WrsPtpSyncSource_Type()
)
wrsPtpSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpSyncSource.setStatus("current")
_WrsPtpClockOffsetPs_Type = Counter64
_WrsPtpClockOffsetPs_Object = MibTableColumn
wrsPtpClockOffsetPs = _WrsPtpClockOffsetPs_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 10),
    _WrsPtpClockOffsetPs_Type()
)
wrsPtpClockOffsetPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpClockOffsetPs.setStatus("current")
_WrsPtpClockOffsetPsHR_Type = Integer32
_WrsPtpClockOffsetPsHR_Object = MibTableColumn
wrsPtpClockOffsetPsHR = _WrsPtpClockOffsetPsHR_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 11),
    _WrsPtpClockOffsetPsHR_Type()
)
wrsPtpClockOffsetPsHR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpClockOffsetPsHR.setStatus("current")
_WrsPtpSkew_Type = Integer32
_WrsPtpSkew_Object = MibTableColumn
wrsPtpSkew = _WrsPtpSkew_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 12),
    _WrsPtpSkew_Type()
)
wrsPtpSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpSkew.setStatus("current")
_WrsPtpRTT_Type = Counter64
_WrsPtpRTT_Object = MibTableColumn
wrsPtpRTT = _WrsPtpRTT_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 13),
    _WrsPtpRTT_Type()
)
wrsPtpRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpRTT.setStatus("current")
_WrsPtpLinkLength_Type = Unsigned32
_WrsPtpLinkLength_Object = MibTableColumn
wrsPtpLinkLength = _WrsPtpLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 14),
    _WrsPtpLinkLength_Type()
)
wrsPtpLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpLinkLength.setStatus("current")
_WrsPtpServoUpdates_Type = Counter32
_WrsPtpServoUpdates_Object = MibTableColumn
wrsPtpServoUpdates = _WrsPtpServoUpdates_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 15),
    _WrsPtpServoUpdates_Type()
)
wrsPtpServoUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoUpdates.setStatus("current")
_WrsPtpDeltaTxM_Type = Integer32
_WrsPtpDeltaTxM_Object = MibTableColumn
wrsPtpDeltaTxM = _WrsPtpDeltaTxM_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 16),
    _WrsPtpDeltaTxM_Type()
)
wrsPtpDeltaTxM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpDeltaTxM.setStatus("current")
_WrsPtpDeltaRxM_Type = Integer32
_WrsPtpDeltaRxM_Object = MibTableColumn
wrsPtpDeltaRxM = _WrsPtpDeltaRxM_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 17),
    _WrsPtpDeltaRxM_Type()
)
wrsPtpDeltaRxM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpDeltaRxM.setStatus("current")
_WrsPtpDeltaTxS_Type = Integer32
_WrsPtpDeltaTxS_Object = MibTableColumn
wrsPtpDeltaTxS = _WrsPtpDeltaTxS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 18),
    _WrsPtpDeltaTxS_Type()
)
wrsPtpDeltaTxS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpDeltaTxS.setStatus("current")
_WrsPtpDeltaRxS_Type = Integer32
_WrsPtpDeltaRxS_Object = MibTableColumn
wrsPtpDeltaRxS = _WrsPtpDeltaRxS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 19),
    _WrsPtpDeltaRxS_Type()
)
wrsPtpDeltaRxS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpDeltaRxS.setStatus("current")
_WrsPtpServoStateErrCnt_Type = Counter32
_WrsPtpServoStateErrCnt_Object = MibTableColumn
wrsPtpServoStateErrCnt = _WrsPtpServoStateErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 20),
    _WrsPtpServoStateErrCnt_Type()
)
wrsPtpServoStateErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoStateErrCnt.setStatus("current")
_WrsPtpClockOffsetErrCnt_Type = Counter32
_WrsPtpClockOffsetErrCnt_Object = MibTableColumn
wrsPtpClockOffsetErrCnt = _WrsPtpClockOffsetErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 21),
    _WrsPtpClockOffsetErrCnt_Type()
)
wrsPtpClockOffsetErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpClockOffsetErrCnt.setStatus("current")
_WrsPtpRTTErrCnt_Type = Counter32
_WrsPtpRTTErrCnt_Object = MibTableColumn
wrsPtpRTTErrCnt = _WrsPtpRTTErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 22),
    _WrsPtpRTTErrCnt_Type()
)
wrsPtpRTTErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpRTTErrCnt.setStatus("current")
_WrsPtpServoUpdateTime_Type = Counter64
_WrsPtpServoUpdateTime_Object = MibTableColumn
wrsPtpServoUpdateTime = _WrsPtpServoUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 23),
    _WrsPtpServoUpdateTime_Type()
)
wrsPtpServoUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoUpdateTime.setStatus("current")


class _WrsPtpServoExt_Type(Integer32):
    """Custom type wrsPtpServoExt based on Integer32"""
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
        *(("na", 0),
          ("none", 1),
          ("wr", 2),
          ("l1Sync", 3))
    )


_WrsPtpServoExt_Type.__name__ = "Integer32"
_WrsPtpServoExt_Object = MibTableColumn
wrsPtpServoExt = _WrsPtpServoExt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 5, 1, 24),
    _WrsPtpServoExt_Type()
)
wrsPtpServoExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpServoExt.setStatus("current")
_WrsPortStatusTable_Object = MibTable
wrsPortStatusTable = _WrsPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6)
)
if mibBuilder.loadTexts:
    wrsPortStatusTable.setStatus("current")
_WrsPortStatusEntry_Object = MibTableRow
wrsPortStatusEntry = _WrsPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1)
)
wrsPortStatusEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsPortStatusIndex"),
)
if mibBuilder.loadTexts:
    wrsPortStatusEntry.setStatus("current")
_WrsPortStatusIndex_Type = Unsigned32
_WrsPortStatusIndex_Object = MibTableColumn
wrsPortStatusIndex = _WrsPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 1),
    _WrsPortStatusIndex_Type()
)
wrsPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPortStatusIndex.setStatus("current")


class _WrsPortStatusPortName_Type(DisplayString):
    """Custom type wrsPortStatusPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPortStatusPortName_Type.__name__ = "DisplayString"
_WrsPortStatusPortName_Object = MibTableColumn
wrsPortStatusPortName = _WrsPortStatusPortName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 2),
    _WrsPortStatusPortName_Type()
)
wrsPortStatusPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusPortName.setStatus("current")


class _WrsPortStatusLink_Type(Integer32):
    """Custom type wrsPortStatusLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("down", 1),
          ("up", 2))
    )


_WrsPortStatusLink_Type.__name__ = "Integer32"
_WrsPortStatusLink_Object = MibTableColumn
wrsPortStatusLink = _WrsPortStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 3),
    _WrsPortStatusLink_Type()
)
wrsPortStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusLink.setStatus("current")


class _WrsPortStatusConfiguredMode_Type(Integer32):
    """Custom type wrsPortStatusConfiguredMode based on Integer32"""
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
        *(("unknown", 0),
          ("master", 1),
          ("slave", 2),
          ("nonWr", 3),
          ("auto", 4),
          ("none", 5))
    )


_WrsPortStatusConfiguredMode_Type.__name__ = "Integer32"
_WrsPortStatusConfiguredMode_Object = MibTableColumn
wrsPortStatusConfiguredMode = _WrsPortStatusConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 4),
    _WrsPortStatusConfiguredMode_Type()
)
wrsPortStatusConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusConfiguredMode.setStatus("current")


class _WrsPortStatusLocked_Type(Integer32):
    """Custom type wrsPortStatusLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("notLocked", 1),
          ("locked", 2))
    )


_WrsPortStatusLocked_Type.__name__ = "Integer32"
_WrsPortStatusLocked_Object = MibTableColumn
wrsPortStatusLocked = _WrsPortStatusLocked_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 5),
    _WrsPortStatusLocked_Type()
)
wrsPortStatusLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusLocked.setStatus("current")


class _WrsPortStatusPeer_Type(OctetString):
    """Custom type wrsPortStatusPeer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_WrsPortStatusPeer_Type.__name__ = "OctetString"
_WrsPortStatusPeer_Object = MibTableColumn
wrsPortStatusPeer = _WrsPortStatusPeer_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 6),
    _WrsPortStatusPeer_Type()
)
wrsPortStatusPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusPeer.setStatus("obsolete")


class _WrsPortStatusSfpVN_Type(DisplayString):
    """Custom type wrsPortStatusSfpVN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsPortStatusSfpVN_Type.__name__ = "DisplayString"
_WrsPortStatusSfpVN_Object = MibTableColumn
wrsPortStatusSfpVN = _WrsPortStatusSfpVN_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 7),
    _WrsPortStatusSfpVN_Type()
)
wrsPortStatusSfpVN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpVN.setStatus("current")


class _WrsPortStatusSfpPN_Type(DisplayString):
    """Custom type wrsPortStatusSfpPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsPortStatusSfpPN_Type.__name__ = "DisplayString"
_WrsPortStatusSfpPN_Object = MibTableColumn
wrsPortStatusSfpPN = _WrsPortStatusSfpPN_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 8),
    _WrsPortStatusSfpPN_Type()
)
wrsPortStatusSfpPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpPN.setStatus("current")


class _WrsPortStatusSfpVS_Type(DisplayString):
    """Custom type wrsPortStatusSfpVS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WrsPortStatusSfpVS_Type.__name__ = "DisplayString"
_WrsPortStatusSfpVS_Object = MibTableColumn
wrsPortStatusSfpVS = _WrsPortStatusSfpVS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 9),
    _WrsPortStatusSfpVS_Type()
)
wrsPortStatusSfpVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpVS.setStatus("current")


class _WrsPortStatusSfpInDB_Type(Integer32):
    """Custom type wrsPortStatusSfpInDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("notInDataBase", 1),
          ("inDataBase", 2))
    )


_WrsPortStatusSfpInDB_Type.__name__ = "Integer32"
_WrsPortStatusSfpInDB_Object = MibTableColumn
wrsPortStatusSfpInDB = _WrsPortStatusSfpInDB_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 10),
    _WrsPortStatusSfpInDB_Type()
)
wrsPortStatusSfpInDB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpInDB.setStatus("current")


class _WrsPortStatusSfpGbE_Type(Integer32):
    """Custom type wrsPortStatusSfpGbE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("linkNotGbE", 1),
          ("linkGbE", 2))
    )


_WrsPortStatusSfpGbE_Type.__name__ = "Integer32"
_WrsPortStatusSfpGbE_Object = MibTableColumn
wrsPortStatusSfpGbE = _WrsPortStatusSfpGbE_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 11),
    _WrsPortStatusSfpGbE_Type()
)
wrsPortStatusSfpGbE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpGbE.setStatus("current")


class _WrsPortStatusSfpError_Type(Integer32):
    """Custom type wrsPortStatusSfpError based on Integer32"""
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
        *(("na", 0),
          ("sfpOk", 1),
          ("sfpError", 2),
          ("portDown", 3))
    )


_WrsPortStatusSfpError_Type.__name__ = "Integer32"
_WrsPortStatusSfpError_Object = MibTableColumn
wrsPortStatusSfpError = _WrsPortStatusSfpError_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 12),
    _WrsPortStatusSfpError_Type()
)
wrsPortStatusSfpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpError.setStatus("current")
_WrsPortStatusPtpTxFrames_Type = Counter32
_WrsPortStatusPtpTxFrames_Object = MibTableColumn
wrsPortStatusPtpTxFrames = _WrsPortStatusPtpTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 13),
    _WrsPortStatusPtpTxFrames_Type()
)
wrsPortStatusPtpTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusPtpTxFrames.setStatus("current")
_WrsPortStatusPtpRxFrames_Type = Counter32
_WrsPortStatusPtpRxFrames_Object = MibTableColumn
wrsPortStatusPtpRxFrames = _WrsPortStatusPtpRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 14),
    _WrsPortStatusPtpRxFrames_Type()
)
wrsPortStatusPtpRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusPtpRxFrames.setStatus("current")


class _WrsPortStatusMonitor_Type(Integer32):
    """Custom type wrsPortStatusMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("enable", 1),
          ("disable", 2))
    )


_WrsPortStatusMonitor_Type.__name__ = "Integer32"
_WrsPortStatusMonitor_Object = MibTableColumn
wrsPortStatusMonitor = _WrsPortStatusMonitor_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 15),
    _WrsPortStatusMonitor_Type()
)
wrsPortStatusMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusMonitor.setStatus("current")


class _WrsPortStatusSfpDom_Type(Integer32):
    """Custom type wrsPortStatusSfpDom based on Integer32"""
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
        *(("na", 0),
          ("enable", 1),
          ("disable", 2),
          ("domNotSupported", 3))
    )


_WrsPortStatusSfpDom_Type.__name__ = "Integer32"
_WrsPortStatusSfpDom_Object = MibTableColumn
wrsPortStatusSfpDom = _WrsPortStatusSfpDom_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 16),
    _WrsPortStatusSfpDom_Type()
)
wrsPortStatusSfpDom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpDom.setStatus("current")
_WrsPortStatusSfpTemp_Type = Integer32
_WrsPortStatusSfpTemp_Object = MibTableColumn
wrsPortStatusSfpTemp = _WrsPortStatusSfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 17),
    _WrsPortStatusSfpTemp_Type()
)
wrsPortStatusSfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpTemp.setStatus("current")
_WrsPortStatusSfpVcc_Type = Integer32
_WrsPortStatusSfpVcc_Object = MibTableColumn
wrsPortStatusSfpVcc = _WrsPortStatusSfpVcc_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 18),
    _WrsPortStatusSfpVcc_Type()
)
wrsPortStatusSfpVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpVcc.setStatus("current")
_WrsPortStatusSfpTxBias_Type = Integer32
_WrsPortStatusSfpTxBias_Object = MibTableColumn
wrsPortStatusSfpTxBias = _WrsPortStatusSfpTxBias_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 19),
    _WrsPortStatusSfpTxBias_Type()
)
wrsPortStatusSfpTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpTxBias.setStatus("current")
_WrsPortStatusSfpTxPower_Type = Integer32
_WrsPortStatusSfpTxPower_Object = MibTableColumn
wrsPortStatusSfpTxPower = _WrsPortStatusSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 20),
    _WrsPortStatusSfpTxPower_Type()
)
wrsPortStatusSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpTxPower.setStatus("current")
_WrsPortStatusSfpRxPower_Type = Integer32
_WrsPortStatusSfpRxPower_Object = MibTableColumn
wrsPortStatusSfpRxPower = _WrsPortStatusSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 21),
    _WrsPortStatusSfpRxPower_Type()
)
wrsPortStatusSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusSfpRxPower.setStatus("current")
_WrsPortStatusT24p_Type = Integer32
_WrsPortStatusT24p_Object = MibTableColumn
wrsPortStatusT24p = _WrsPortStatusT24p_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 22),
    _WrsPortStatusT24p_Type()
)
wrsPortStatusT24p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusT24p.setStatus("current")


class _WrsPortStatusT24pValid_Type(Integer32):
    """Custom type wrsPortStatusT24pValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("readFromConfig", 1))
    )


_WrsPortStatusT24pValid_Type.__name__ = "Integer32"
_WrsPortStatusT24pValid_Object = MibTableColumn
wrsPortStatusT24pValid = _WrsPortStatusT24pValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 6, 1, 23),
    _WrsPortStatusT24pValid_Type()
)
wrsPortStatusT24pValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPortStatusT24pValid.setStatus("current")
_WrsPstatsHCTable_Object = MibTable
wrsPstatsHCTable = _WrsPstatsHCTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7)
)
if mibBuilder.loadTexts:
    wrsPstatsHCTable.setStatus("current")
_WrsPstatsHCEntry_Object = MibTableRow
wrsPstatsHCEntry = _WrsPstatsHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1)
)
wrsPstatsHCEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsPstatsHCIndex"),
)
if mibBuilder.loadTexts:
    wrsPstatsHCEntry.setStatus("current")
_WrsPstatsHCIndex_Type = Unsigned32
_WrsPstatsHCIndex_Object = MibTableColumn
wrsPstatsHCIndex = _WrsPstatsHCIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 1),
    _WrsPstatsHCIndex_Type()
)
wrsPstatsHCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPstatsHCIndex.setStatus("current")


class _WrsPstatsHCPortName_Type(DisplayString):
    """Custom type wrsPstatsHCPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPstatsHCPortName_Type.__name__ = "DisplayString"
_WrsPstatsHCPortName_Object = MibTableColumn
wrsPstatsHCPortName = _WrsPstatsHCPortName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 2),
    _WrsPstatsHCPortName_Type()
)
wrsPstatsHCPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCPortName.setStatus("current")
_WrsPstatsHCTXUnderrun_Type = Counter64
_WrsPstatsHCTXUnderrun_Object = MibTableColumn
wrsPstatsHCTXUnderrun = _WrsPstatsHCTXUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 3),
    _WrsPstatsHCTXUnderrun_Type()
)
wrsPstatsHCTXUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCTXUnderrun.setStatus("current")
_WrsPstatsHCRXOverrun_Type = Counter64
_WrsPstatsHCRXOverrun_Object = MibTableColumn
wrsPstatsHCRXOverrun = _WrsPstatsHCRXOverrun_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 4),
    _WrsPstatsHCRXOverrun_Type()
)
wrsPstatsHCRXOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXOverrun.setStatus("current")
_WrsPstatsHCRXInvalidCode_Type = Counter64
_WrsPstatsHCRXInvalidCode_Object = MibTableColumn
wrsPstatsHCRXInvalidCode = _WrsPstatsHCRXInvalidCode_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 5),
    _WrsPstatsHCRXInvalidCode_Type()
)
wrsPstatsHCRXInvalidCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXInvalidCode.setStatus("current")
_WrsPstatsHCRXSyncLost_Type = Counter64
_WrsPstatsHCRXSyncLost_Object = MibTableColumn
wrsPstatsHCRXSyncLost = _WrsPstatsHCRXSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 6),
    _WrsPstatsHCRXSyncLost_Type()
)
wrsPstatsHCRXSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXSyncLost.setStatus("current")
_WrsPstatsHCRXPauseFrames_Type = Counter64
_WrsPstatsHCRXPauseFrames_Object = MibTableColumn
wrsPstatsHCRXPauseFrames = _WrsPstatsHCRXPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 7),
    _WrsPstatsHCRXPauseFrames_Type()
)
wrsPstatsHCRXPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPauseFrames.setStatus("current")
_WrsPstatsHCRXPfilterDropped_Type = Counter64
_WrsPstatsHCRXPfilterDropped_Object = MibTableColumn
wrsPstatsHCRXPfilterDropped = _WrsPstatsHCRXPfilterDropped_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 8),
    _WrsPstatsHCRXPfilterDropped_Type()
)
wrsPstatsHCRXPfilterDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPfilterDropped.setStatus("current")
_WrsPstatsHCRXPCSErrors_Type = Counter64
_WrsPstatsHCRXPCSErrors_Object = MibTableColumn
wrsPstatsHCRXPCSErrors = _WrsPstatsHCRXPCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 9),
    _WrsPstatsHCRXPCSErrors_Type()
)
wrsPstatsHCRXPCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPCSErrors.setStatus("current")
_WrsPstatsHCRXGiantFrames_Type = Counter64
_WrsPstatsHCRXGiantFrames_Object = MibTableColumn
wrsPstatsHCRXGiantFrames = _WrsPstatsHCRXGiantFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 10),
    _WrsPstatsHCRXGiantFrames_Type()
)
wrsPstatsHCRXGiantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXGiantFrames.setStatus("current")
_WrsPstatsHCRXRuntFrames_Type = Counter64
_WrsPstatsHCRXRuntFrames_Object = MibTableColumn
wrsPstatsHCRXRuntFrames = _WrsPstatsHCRXRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 11),
    _WrsPstatsHCRXRuntFrames_Type()
)
wrsPstatsHCRXRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXRuntFrames.setStatus("current")
_WrsPstatsHCRXCRCErrors_Type = Counter64
_WrsPstatsHCRXCRCErrors_Object = MibTableColumn
wrsPstatsHCRXCRCErrors = _WrsPstatsHCRXCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 12),
    _WrsPstatsHCRXCRCErrors_Type()
)
wrsPstatsHCRXCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXCRCErrors.setStatus("current")
_WrsPstatsHCRXPclass0_Type = Counter64
_WrsPstatsHCRXPclass0_Object = MibTableColumn
wrsPstatsHCRXPclass0 = _WrsPstatsHCRXPclass0_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 13),
    _WrsPstatsHCRXPclass0_Type()
)
wrsPstatsHCRXPclass0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass0.setStatus("current")
_WrsPstatsHCRXPclass1_Type = Counter64
_WrsPstatsHCRXPclass1_Object = MibTableColumn
wrsPstatsHCRXPclass1 = _WrsPstatsHCRXPclass1_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 14),
    _WrsPstatsHCRXPclass1_Type()
)
wrsPstatsHCRXPclass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass1.setStatus("current")
_WrsPstatsHCRXPclass2_Type = Counter64
_WrsPstatsHCRXPclass2_Object = MibTableColumn
wrsPstatsHCRXPclass2 = _WrsPstatsHCRXPclass2_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 15),
    _WrsPstatsHCRXPclass2_Type()
)
wrsPstatsHCRXPclass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass2.setStatus("current")
_WrsPstatsHCRXPclass3_Type = Counter64
_WrsPstatsHCRXPclass3_Object = MibTableColumn
wrsPstatsHCRXPclass3 = _WrsPstatsHCRXPclass3_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 16),
    _WrsPstatsHCRXPclass3_Type()
)
wrsPstatsHCRXPclass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass3.setStatus("current")
_WrsPstatsHCRXPclass4_Type = Counter64
_WrsPstatsHCRXPclass4_Object = MibTableColumn
wrsPstatsHCRXPclass4 = _WrsPstatsHCRXPclass4_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 17),
    _WrsPstatsHCRXPclass4_Type()
)
wrsPstatsHCRXPclass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass4.setStatus("current")
_WrsPstatsHCRXPclass5_Type = Counter64
_WrsPstatsHCRXPclass5_Object = MibTableColumn
wrsPstatsHCRXPclass5 = _WrsPstatsHCRXPclass5_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 18),
    _WrsPstatsHCRXPclass5_Type()
)
wrsPstatsHCRXPclass5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass5.setStatus("current")
_WrsPstatsHCRXPclass6_Type = Counter64
_WrsPstatsHCRXPclass6_Object = MibTableColumn
wrsPstatsHCRXPclass6 = _WrsPstatsHCRXPclass6_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 19),
    _WrsPstatsHCRXPclass6_Type()
)
wrsPstatsHCRXPclass6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass6.setStatus("current")
_WrsPstatsHCRXPclass7_Type = Counter64
_WrsPstatsHCRXPclass7_Object = MibTableColumn
wrsPstatsHCRXPclass7 = _WrsPstatsHCRXPclass7_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 20),
    _WrsPstatsHCRXPclass7_Type()
)
wrsPstatsHCRXPclass7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPclass7.setStatus("current")
_WrsPstatsHCTXFrames_Type = Counter64
_WrsPstatsHCTXFrames_Object = MibTableColumn
wrsPstatsHCTXFrames = _WrsPstatsHCTXFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 21),
    _WrsPstatsHCTXFrames_Type()
)
wrsPstatsHCTXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCTXFrames.setStatus("current")
_WrsPstatsHCRXFrames_Type = Counter64
_WrsPstatsHCRXFrames_Object = MibTableColumn
wrsPstatsHCRXFrames = _WrsPstatsHCRXFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 22),
    _WrsPstatsHCRXFrames_Type()
)
wrsPstatsHCRXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXFrames.setStatus("current")
_WrsPstatsHCRXDropRTUFull_Type = Counter64
_WrsPstatsHCRXDropRTUFull_Object = MibTableColumn
wrsPstatsHCRXDropRTUFull = _WrsPstatsHCRXDropRTUFull_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 23),
    _WrsPstatsHCRXDropRTUFull_Type()
)
wrsPstatsHCRXDropRTUFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXDropRTUFull.setStatus("current")
_WrsPstatsHCRXPrio0_Type = Counter64
_WrsPstatsHCRXPrio0_Object = MibTableColumn
wrsPstatsHCRXPrio0 = _WrsPstatsHCRXPrio0_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 24),
    _WrsPstatsHCRXPrio0_Type()
)
wrsPstatsHCRXPrio0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio0.setStatus("current")
_WrsPstatsHCRXPrio1_Type = Counter64
_WrsPstatsHCRXPrio1_Object = MibTableColumn
wrsPstatsHCRXPrio1 = _WrsPstatsHCRXPrio1_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 25),
    _WrsPstatsHCRXPrio1_Type()
)
wrsPstatsHCRXPrio1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio1.setStatus("current")
_WrsPstatsHCRXPrio2_Type = Counter64
_WrsPstatsHCRXPrio2_Object = MibTableColumn
wrsPstatsHCRXPrio2 = _WrsPstatsHCRXPrio2_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 26),
    _WrsPstatsHCRXPrio2_Type()
)
wrsPstatsHCRXPrio2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio2.setStatus("current")
_WrsPstatsHCRXPrio3_Type = Counter64
_WrsPstatsHCRXPrio3_Object = MibTableColumn
wrsPstatsHCRXPrio3 = _WrsPstatsHCRXPrio3_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 27),
    _WrsPstatsHCRXPrio3_Type()
)
wrsPstatsHCRXPrio3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio3.setStatus("current")
_WrsPstatsHCRXPrio4_Type = Counter64
_WrsPstatsHCRXPrio4_Object = MibTableColumn
wrsPstatsHCRXPrio4 = _WrsPstatsHCRXPrio4_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 28),
    _WrsPstatsHCRXPrio4_Type()
)
wrsPstatsHCRXPrio4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio4.setStatus("current")
_WrsPstatsHCRXPrio5_Type = Counter64
_WrsPstatsHCRXPrio5_Object = MibTableColumn
wrsPstatsHCRXPrio5 = _WrsPstatsHCRXPrio5_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 29),
    _WrsPstatsHCRXPrio5_Type()
)
wrsPstatsHCRXPrio5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio5.setStatus("current")
_WrsPstatsHCRXPrio6_Type = Counter64
_WrsPstatsHCRXPrio6_Object = MibTableColumn
wrsPstatsHCRXPrio6 = _WrsPstatsHCRXPrio6_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 30),
    _WrsPstatsHCRXPrio6_Type()
)
wrsPstatsHCRXPrio6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio6.setStatus("current")
_WrsPstatsHCRXPrio7_Type = Counter64
_WrsPstatsHCRXPrio7_Object = MibTableColumn
wrsPstatsHCRXPrio7 = _WrsPstatsHCRXPrio7_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 31),
    _WrsPstatsHCRXPrio7_Type()
)
wrsPstatsHCRXPrio7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRXPrio7.setStatus("current")
_WrsPstatsHCRTUValid_Type = Counter64
_WrsPstatsHCRTUValid_Object = MibTableColumn
wrsPstatsHCRTUValid = _WrsPstatsHCRTUValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 32),
    _WrsPstatsHCRTUValid_Type()
)
wrsPstatsHCRTUValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRTUValid.setStatus("current")
_WrsPstatsHCRTUResponses_Type = Counter64
_WrsPstatsHCRTUResponses_Object = MibTableColumn
wrsPstatsHCRTUResponses = _WrsPstatsHCRTUResponses_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 33),
    _WrsPstatsHCRTUResponses_Type()
)
wrsPstatsHCRTUResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRTUResponses.setStatus("current")
_WrsPstatsHCRTUDropped_Type = Counter64
_WrsPstatsHCRTUDropped_Object = MibTableColumn
wrsPstatsHCRTUDropped = _WrsPstatsHCRTUDropped_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 34),
    _WrsPstatsHCRTUDropped_Type()
)
wrsPstatsHCRTUDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCRTUDropped.setStatus("current")
_WrsPstatsHCFastMatchPriority_Type = Counter64
_WrsPstatsHCFastMatchPriority_Object = MibTableColumn
wrsPstatsHCFastMatchPriority = _WrsPstatsHCFastMatchPriority_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 35),
    _WrsPstatsHCFastMatchPriority_Type()
)
wrsPstatsHCFastMatchPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCFastMatchPriority.setStatus("current")
_WrsPstatsHCFastMatchFastForward_Type = Counter64
_WrsPstatsHCFastMatchFastForward_Object = MibTableColumn
wrsPstatsHCFastMatchFastForward = _WrsPstatsHCFastMatchFastForward_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 36),
    _WrsPstatsHCFastMatchFastForward_Type()
)
wrsPstatsHCFastMatchFastForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCFastMatchFastForward.setStatus("current")
_WrsPstatsHCFastMatchNonForward_Type = Counter64
_WrsPstatsHCFastMatchNonForward_Object = MibTableColumn
wrsPstatsHCFastMatchNonForward = _WrsPstatsHCFastMatchNonForward_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 37),
    _WrsPstatsHCFastMatchNonForward_Type()
)
wrsPstatsHCFastMatchNonForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCFastMatchNonForward.setStatus("current")
_WrsPstatsHCFastMatchRespValid_Type = Counter64
_WrsPstatsHCFastMatchRespValid_Object = MibTableColumn
wrsPstatsHCFastMatchRespValid = _WrsPstatsHCFastMatchRespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 38),
    _WrsPstatsHCFastMatchRespValid_Type()
)
wrsPstatsHCFastMatchRespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCFastMatchRespValid.setStatus("current")
_WrsPstatsHCFullMatchRespValid_Type = Counter64
_WrsPstatsHCFullMatchRespValid_Object = MibTableColumn
wrsPstatsHCFullMatchRespValid = _WrsPstatsHCFullMatchRespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 39),
    _WrsPstatsHCFullMatchRespValid_Type()
)
wrsPstatsHCFullMatchRespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCFullMatchRespValid.setStatus("current")
_WrsPstatsHCForwarded_Type = Counter64
_WrsPstatsHCForwarded_Object = MibTableColumn
wrsPstatsHCForwarded = _WrsPstatsHCForwarded_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 40),
    _WrsPstatsHCForwarded_Type()
)
wrsPstatsHCForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCForwarded.setStatus("current")
_WrsPstatsHCTRURespValid_Type = Counter64
_WrsPstatsHCTRURespValid_Object = MibTableColumn
wrsPstatsHCTRURespValid = _WrsPstatsHCTRURespValid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 41),
    _WrsPstatsHCTRURespValid_Type()
)
wrsPstatsHCTRURespValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCTRURespValid.setStatus("current")
_WrsPstatsHCNICTXFrames_Type = Counter64
_WrsPstatsHCNICTXFrames_Object = MibTableColumn
wrsPstatsHCNICTXFrames = _WrsPstatsHCNICTXFrames_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 7, 1, 42),
    _WrsPstatsHCNICTXFrames_Type()
)
wrsPstatsHCNICTXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPstatsHCNICTXFrames.setStatus("current")
_WrsPtpInstanceTable_Object = MibTable
wrsPtpInstanceTable = _WrsPtpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8)
)
if mibBuilder.loadTexts:
    wrsPtpInstanceTable.setStatus("current")
_WrsPtpInstanceEntry_Object = MibTableRow
wrsPtpInstanceEntry = _WrsPtpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1)
)
wrsPtpInstanceEntry.setIndexNames(
    (0, "WR-SWITCH-MIB", "wrsPtpInstancePortIndex"),
    (0, "WR-SWITCH-MIB", "wrsPtpInstanceOnPortIndex"),
)
if mibBuilder.loadTexts:
    wrsPtpInstanceEntry.setStatus("current")
_WrsPtpInstancePortIndex_Type = Unsigned32
_WrsPtpInstancePortIndex_Object = MibTableColumn
wrsPtpInstancePortIndex = _WrsPtpInstancePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 1),
    _WrsPtpInstancePortIndex_Type()
)
wrsPtpInstancePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPtpInstancePortIndex.setStatus("current")
_WrsPtpInstanceOnPortIndex_Type = Unsigned32
_WrsPtpInstanceOnPortIndex_Object = MibTableColumn
wrsPtpInstanceOnPortIndex = _WrsPtpInstanceOnPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 2),
    _WrsPtpInstanceOnPortIndex_Type()
)
wrsPtpInstanceOnPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wrsPtpInstanceOnPortIndex.setStatus("current")


class _WrsPtpInstanceName_Type(DisplayString):
    """Custom type wrsPtpInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPtpInstanceName_Type.__name__ = "DisplayString"
_WrsPtpInstanceName_Object = MibTableColumn
wrsPtpInstanceName = _WrsPtpInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 3),
    _WrsPtpInstanceName_Type()
)
wrsPtpInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceName.setStatus("current")
_WrsPtpInstancePort_Type = Integer32
_WrsPtpInstancePort_Object = MibTableColumn
wrsPtpInstancePort = _WrsPtpInstancePort_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 4),
    _WrsPtpInstancePort_Type()
)
wrsPtpInstancePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstancePort.setStatus("current")
_WrsPtpInstancePortInstance_Type = Integer32
_WrsPtpInstancePortInstance_Object = MibTableColumn
wrsPtpInstancePortInstance = _WrsPtpInstancePortInstance_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 5),
    _WrsPtpInstancePortInstance_Type()
)
wrsPtpInstancePortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstancePortInstance.setStatus("current")


class _WrsPtpInstancePortName_Type(DisplayString):
    """Custom type wrsPtpInstancePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WrsPtpInstancePortName_Type.__name__ = "DisplayString"
_WrsPtpInstancePortName_Object = MibTableColumn
wrsPtpInstancePortName = _WrsPtpInstancePortName_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 6),
    _WrsPtpInstancePortName_Type()
)
wrsPtpInstancePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstancePortName.setStatus("current")


class _WrsPtpInstanceState_Type(Integer32):
    """Custom type wrsPtpInstanceState based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )


_WrsPtpInstanceState_Type.__name__ = "Integer32"
_WrsPtpInstanceState_Object = MibTableColumn
wrsPtpInstanceState = _WrsPtpInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 7),
    _WrsPtpInstanceState_Type()
)
wrsPtpInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceState.setStatus("current")


class _WrsPtpInstanceMasterOnly_Type(Integer32):
    """Custom type wrsPtpInstanceMasterOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_WrsPtpInstanceMasterOnly_Type.__name__ = "Integer32"
_WrsPtpInstanceMasterOnly_Object = MibTableColumn
wrsPtpInstanceMasterOnly = _WrsPtpInstanceMasterOnly_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 8),
    _WrsPtpInstanceMasterOnly_Type()
)
wrsPtpInstanceMasterOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceMasterOnly.setStatus("current")


class _WrsPtpInstanceExtPortCfgDesSt_Type(Integer32):
    """Custom type wrsPtpInstanceExtPortCfgDesSt based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )


_WrsPtpInstanceExtPortCfgDesSt_Type.__name__ = "Integer32"
_WrsPtpInstanceExtPortCfgDesSt_Object = MibTableColumn
wrsPtpInstanceExtPortCfgDesSt = _WrsPtpInstanceExtPortCfgDesSt_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 9),
    _WrsPtpInstanceExtPortCfgDesSt_Type()
)
wrsPtpInstanceExtPortCfgDesSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceExtPortCfgDesSt.setStatus("current")


class _WrsPtpInstanceMechanism_Type(Integer32):
    """Custom type wrsPtpInstanceMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("e2e", 1),
          ("p2p", 2),
          ("commonP2P", 3),
          ("special", 4),
          ("noMechanism", 254))
    )


_WrsPtpInstanceMechanism_Type.__name__ = "Integer32"
_WrsPtpInstanceMechanism_Object = MibTableColumn
wrsPtpInstanceMechanism = _WrsPtpInstanceMechanism_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 10),
    _WrsPtpInstanceMechanism_Type()
)
wrsPtpInstanceMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceMechanism.setStatus("current")


class _WrsPtpInstanceProfile_Type(Integer32):
    """Custom type wrsPtpInstanceProfile based on Integer32"""
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
        *(("na", 0),
          ("defaultPTP", 1),
          ("whiteRabbit", 2),
          ("highAccuracy", 3),
          ("custom", 4))
    )


_WrsPtpInstanceProfile_Type.__name__ = "Integer32"
_WrsPtpInstanceProfile_Object = MibTableColumn
wrsPtpInstanceProfile = _WrsPtpInstanceProfile_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 11),
    _WrsPtpInstanceProfile_Type()
)
wrsPtpInstanceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceProfile.setStatus("current")


class _WrsPtpInstanceExtension_Type(Integer32):
    """Custom type wrsPtpInstanceExtension based on Integer32"""
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
        *(("na", 0),
          ("none", 1),
          ("whiteRabbit", 2),
          ("l1Sync", 3))
    )


_WrsPtpInstanceExtension_Type.__name__ = "Integer32"
_WrsPtpInstanceExtension_Object = MibTableColumn
wrsPtpInstanceExtension = _WrsPtpInstanceExtension_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 12),
    _WrsPtpInstanceExtension_Type()
)
wrsPtpInstanceExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceExtension.setStatus("current")


class _WrsPtpInstanceAsymEnabled_Type(Integer32):
    """Custom type wrsPtpInstanceAsymEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_WrsPtpInstanceAsymEnabled_Type.__name__ = "Integer32"
_WrsPtpInstanceAsymEnabled_Object = MibTableColumn
wrsPtpInstanceAsymEnabled = _WrsPtpInstanceAsymEnabled_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 13),
    _WrsPtpInstanceAsymEnabled_Type()
)
wrsPtpInstanceAsymEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceAsymEnabled.setStatus("current")
_WrsPtpInstanceAsymConstAsymPS_Type = Counter64
_WrsPtpInstanceAsymConstAsymPS_Object = MibTableColumn
wrsPtpInstanceAsymConstAsymPS = _WrsPtpInstanceAsymConstAsymPS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 14),
    _WrsPtpInstanceAsymConstAsymPS_Type()
)
wrsPtpInstanceAsymConstAsymPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceAsymConstAsymPS.setStatus("current")
_WrsPtpInstanceAsymScDelayCoef_Type = Counter64
_WrsPtpInstanceAsymScDelayCoef_Object = MibTableColumn
wrsPtpInstanceAsymScDelayCoef = _WrsPtpInstanceAsymScDelayCoef_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 15),
    _WrsPtpInstanceAsymScDelayCoef_Type()
)
wrsPtpInstanceAsymScDelayCoef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceAsymScDelayCoef.setStatus("current")


class _WrsPtpInstanceAsymScDelayCoefHR_Type(DisplayString):
    """Custom type wrsPtpInstanceAsymScDelayCoefHR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WrsPtpInstanceAsymScDelayCoefHR_Type.__name__ = "DisplayString"
_WrsPtpInstanceAsymScDelayCoefHR_Object = MibTableColumn
wrsPtpInstanceAsymScDelayCoefHR = _WrsPtpInstanceAsymScDelayCoefHR_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 16),
    _WrsPtpInstanceAsymScDelayCoefHR_Type()
)
wrsPtpInstanceAsymScDelayCoefHR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceAsymScDelayCoefHR.setStatus("current")
_WrsPtpInstanceTSCorrEgressLatPS_Type = Counter64
_WrsPtpInstanceTSCorrEgressLatPS_Object = MibTableColumn
wrsPtpInstanceTSCorrEgressLatPS = _WrsPtpInstanceTSCorrEgressLatPS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 17),
    _WrsPtpInstanceTSCorrEgressLatPS_Type()
)
wrsPtpInstanceTSCorrEgressLatPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceTSCorrEgressLatPS.setStatus("current")
_WrsPtpInstanceTSCorrIngLatPS_Type = Counter64
_WrsPtpInstanceTSCorrIngLatPS_Object = MibTableColumn
wrsPtpInstanceTSCorrIngLatPS = _WrsPtpInstanceTSCorrIngLatPS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 18),
    _WrsPtpInstanceTSCorrIngLatPS_Type()
)
wrsPtpInstanceTSCorrIngLatPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceTSCorrIngLatPS.setStatus("current")
_WrsPtpInstanceTSCorrSemistLatPS_Type = Counter64
_WrsPtpInstanceTSCorrSemistLatPS_Object = MibTableColumn
wrsPtpInstanceTSCorrSemistLatPS = _WrsPtpInstanceTSCorrSemistLatPS_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 19),
    _WrsPtpInstanceTSCorrSemistLatPS_Type()
)
wrsPtpInstanceTSCorrSemistLatPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceTSCorrSemistLatPS.setStatus("current")


class _WrsPtpInstanceProtoDetectState_Type(Integer32):
    """Custom type wrsPtpInstanceProtoDetectState based on Integer32"""
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
        *(("na", 0),
          ("none", 1),
          ("pWaitMsg", 2),
          ("pDetection", 3),
          ("pDetected", 4),
          ("pFailure", 5))
    )


_WrsPtpInstanceProtoDetectState_Type.__name__ = "Integer32"
_WrsPtpInstanceProtoDetectState_Object = MibTableColumn
wrsPtpInstanceProtoDetectState = _WrsPtpInstanceProtoDetectState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 20),
    _WrsPtpInstanceProtoDetectState_Type()
)
wrsPtpInstanceProtoDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceProtoDetectState.setStatus("current")


class _WrsPtpInstanceExtState_Type(Integer32):
    """Custom type wrsPtpInstanceExtState based on Integer32"""
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
        *(("na", 0),
          ("disabled", 1),
          ("active", 2),
          ("ptp", 3))
    )


_WrsPtpInstanceExtState_Type.__name__ = "Integer32"
_WrsPtpInstanceExtState_Object = MibTableColumn
wrsPtpInstanceExtState = _WrsPtpInstanceExtState_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 21),
    _WrsPtpInstanceExtState_Type()
)
wrsPtpInstanceExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceExtState.setStatus("current")
_WrsPtpInstancePeerMac_Type = PhysAddress
_WrsPtpInstancePeerMac_Object = MibTableColumn
wrsPtpInstancePeerMac = _WrsPtpInstancePeerMac_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 22),
    _WrsPtpInstancePeerMac_Type()
)
wrsPtpInstancePeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstancePeerMac.setStatus("current")
_WrsPtpInstancePeerVid_Type = Integer32
_WrsPtpInstancePeerVid_Object = MibTableColumn
wrsPtpInstancePeerVid = _WrsPtpInstancePeerVid_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 23),
    _WrsPtpInstancePeerVid_Type()
)
wrsPtpInstancePeerVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstancePeerVid.setStatus("current")
_WrsPtpInstanceVlanNum_Type = Integer32
_WrsPtpInstanceVlanNum_Object = MibTableColumn
wrsPtpInstanceVlanNum = _WrsPtpInstanceVlanNum_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 24),
    _WrsPtpInstanceVlanNum_Type()
)
wrsPtpInstanceVlanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceVlanNum.setStatus("current")


class _WrsPtpInstanceVlanListStr_Type(DisplayString):
    """Custom type wrsPtpInstanceVlanListStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_WrsPtpInstanceVlanListStr_Type.__name__ = "DisplayString"
_WrsPtpInstanceVlanListStr_Object = MibTableColumn
wrsPtpInstanceVlanListStr = _WrsPtpInstanceVlanListStr_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 25),
    _WrsPtpInstanceVlanListStr_Type()
)
wrsPtpInstanceVlanListStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceVlanListStr.setStatus("current")


class _WrsPtpInstanceStatusError_Type(Integer32):
    """Custom type wrsPtpInstanceStatusError based on Integer32"""
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
        *(("na", 0),
          ("ok", 1),
          ("error", 2),
          ("warningNA", 3))
    )


_WrsPtpInstanceStatusError_Type.__name__ = "Integer32"
_WrsPtpInstanceStatusError_Object = MibTableColumn
wrsPtpInstanceStatusError = _WrsPtpInstanceStatusError_Object(
    (1, 3, 6, 1, 4, 1, 96, 100, 7, 8, 1, 26),
    _WrsPtpInstanceStatusError_Type()
)
wrsPtpInstanceStatusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wrsPtpInstanceStatusError.setStatus("current")
_WrsId_ObjectIdentity = ObjectIdentity
wrsId = _WrsId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000)
)
_WrsIdUnkn_ObjectIdentity = ObjectIdentity
wrsIdUnkn = _WrsIdUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 1)
)
_WrsIdUnknUnkn_ObjectIdentity = ObjectIdentity
wrsIdUnknUnkn = _WrsIdUnknUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 1, 1)
)
_WrsIdOther_ObjectIdentity = ObjectIdentity
wrsIdOther = _WrsIdOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 2)
)
_WrsId3_ObjectIdentity = ObjectIdentity
wrsId3 = _WrsId3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3)
)
_WrsId3Unkn_ObjectIdentity = ObjectIdentity
wrsId3Unkn = _WrsId3Unkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 1)
)
_WrsId3UnknUnkn_ObjectIdentity = ObjectIdentity
wrsId3UnknUnkn = _WrsId3UnknUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 1, 1)
)
_WrsId3Unkn3_ObjectIdentity = ObjectIdentity
wrsId3Unkn3 = _WrsId3Unkn3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 1, 3)
)
_WrsId3Unkn4_ObjectIdentity = ObjectIdentity
wrsId3Unkn4 = _WrsId3Unkn4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 1, 4)
)
_WrsId3UnknFL_ObjectIdentity = ObjectIdentity
wrsId3UnknFL = _WrsId3UnknFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 1, 5)
)
_WrsId3Ssol_ObjectIdentity = ObjectIdentity
wrsId3Ssol = _WrsId3Ssol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 2)
)
_WrsId3SsolUnkn_ObjectIdentity = ObjectIdentity
wrsId3SsolUnkn = _WrsId3SsolUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 2, 1)
)
_WrsId3Ssol3_ObjectIdentity = ObjectIdentity
wrsId3Ssol3 = _WrsId3Ssol3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 2, 3)
)
_WrsId3Ssol4_ObjectIdentity = ObjectIdentity
wrsId3Ssol4 = _WrsId3Ssol4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 2, 4)
)
_WrsId3Cti_ObjectIdentity = ObjectIdentity
wrsId3Cti = _WrsId3Cti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 3)
)
_WrsId3CtiUnkn_ObjectIdentity = ObjectIdentity
wrsId3CtiUnkn = _WrsId3CtiUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 3, 1)
)
_WrsId3Cti3_ObjectIdentity = ObjectIdentity
wrsId3Cti3 = _WrsId3Cti3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 3, 3)
)
_WrsId3Cti4_ObjectIdentity = ObjectIdentity
wrsId3Cti4 = _WrsId3Cti4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 3, 4)
)
_WrsId3St_ObjectIdentity = ObjectIdentity
wrsId3St = _WrsId3St_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 4)
)
_WrsId3StUnkn_ObjectIdentity = ObjectIdentity
wrsId3StUnkn = _WrsId3StUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 4, 1)
)
_WrsId3St3_ObjectIdentity = ObjectIdentity
wrsId3St3 = _WrsId3St3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 4, 3)
)
_WrsId3St4_ObjectIdentity = ObjectIdentity
wrsId3St4 = _WrsId3St4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 4, 4)
)
_WrsId3StFL_ObjectIdentity = ObjectIdentity
wrsId3StFL = _WrsId3StFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 4, 5)
)
_WrsId3Opnt_ObjectIdentity = ObjectIdentity
wrsId3Opnt = _WrsId3Opnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 5)
)
_WrsId3OpntUnkn_ObjectIdentity = ObjectIdentity
wrsId3OpntUnkn = _WrsId3OpntUnkn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 5, 1)
)
_WrsId3Opnt3_ObjectIdentity = ObjectIdentity
wrsId3Opnt3 = _WrsId3Opnt3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 5, 3)
)
_WrsId3Opnt4_ObjectIdentity = ObjectIdentity
wrsId3Opnt4 = _WrsId3Opnt4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 96, 100, 1000, 3, 5, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WR-SWITCH-MIB",
    **{"cern": cern,
       "wrSwitchMIB": wrSwitchMIB,
       "wrsScalar": wrsScalar,
       "wrsScalarOne": wrsScalarOne,
       "wrsStatus": wrsStatus,
       "wrsGeneralStatusGroup": wrsGeneralStatusGroup,
       "wrsMainSystemStatus": wrsMainSystemStatus,
       "wrsOSStatus": wrsOSStatus,
       "wrsTimingStatus": wrsTimingStatus,
       "wrsNetworkingStatus": wrsNetworkingStatus,
       "wrsDetailedStatusesGroup": wrsDetailedStatusesGroup,
       "wrsOSStatusGroup": wrsOSStatusGroup,
       "wrsBootSuccessful": wrsBootSuccessful,
       "wrsTemperatureWarning": wrsTemperatureWarning,
       "wrsMemoryFreeLow": wrsMemoryFreeLow,
       "wrsCpuLoadHigh": wrsCpuLoadHigh,
       "wrsDiskSpaceLow": wrsDiskSpaceLow,
       "wrsTimingStatusGroup": wrsTimingStatusGroup,
       "wrsPTPStatus": wrsPTPStatus,
       "wrsSoftPLLStatus": wrsSoftPLLStatus,
       "wrsSlaveLinksStatus": wrsSlaveLinksStatus,
       "wrsPTPFramesFlowing": wrsPTPFramesFlowing,
       "wrsSystemClockStatus": wrsSystemClockStatus,
       "wrsNetworkingStatusGroup": wrsNetworkingStatusGroup,
       "wrsSFPsStatus": wrsSFPsStatus,
       "wrsEndpointStatus": wrsEndpointStatus,
       "wrsSwcoreStatus": wrsSwcoreStatus,
       "wrsRTUStatus": wrsRTUStatus,
       "wrsVersionGroup": wrsVersionGroup,
       "wrsVersionSwVersion": wrsVersionSwVersion,
       "wrsVersionSwBuildBy": wrsVersionSwBuildBy,
       "wrsVersionSwBuildDate": wrsVersionSwBuildDate,
       "wrsVersionBackplaneVersion": wrsVersionBackplaneVersion,
       "wrsVersionFpgaType": wrsVersionFpgaType,
       "wrsVersionManufacturer": wrsVersionManufacturer,
       "wrsVersionSwitchSerialNumber": wrsVersionSwitchSerialNumber,
       "wrsVersionScbVersion": wrsVersionScbVersion,
       "wrsVersionGwVersion": wrsVersionGwVersion,
       "wrsVersionGwBuild": wrsVersionGwBuild,
       "wrsVersionSwitchHdlCommitId": wrsVersionSwitchHdlCommitId,
       "wrsVersionGeneralCoresCommitId": wrsVersionGeneralCoresCommitId,
       "wrsVersionWrCoresCommitId": wrsVersionWrCoresCommitId,
       "wrsVersionLastUpdateDate": wrsVersionLastUpdateDate,
       "wrsVersionFeatures": wrsVersionFeatures,
       "wrsExpertStatus": wrsExpertStatus,
       "wrsOperationStatus": wrsOperationStatus,
       "wrsCurrentTimeGroup": wrsCurrentTimeGroup,
       "wrsDateTAI": wrsDateTAI,
       "wrsDateTAIString": wrsDateTAIString,
       "wrsSystemClockStatusDetails": wrsSystemClockStatusDetails,
       "wrsSystemClockDrift": wrsSystemClockDrift,
       "wrsSystemClockDriftThreshold": wrsSystemClockDriftThreshold,
       "wrsSystemClockCheckInterval": wrsSystemClockCheckInterval,
       "wrsSystemClockCheckIntervalUnit": wrsSystemClockCheckIntervalUnit,
       "wrsLeapSecSource": wrsLeapSecSource,
       "wrsLeapSecStatusDetails": wrsLeapSecStatusDetails,
       "wrsLeapSecSourceStatusDetails": wrsLeapSecSourceStatusDetails,
       "wrsLeapSecSourceURL": wrsLeapSecSourceURL,
       "wrsSystemClockDriftUs": wrsSystemClockDriftUs,
       "wrsBootStatusGroup": wrsBootStatusGroup,
       "wrsBootCnt": wrsBootCnt,
       "wrsRebootCnt": wrsRebootCnt,
       "wrsRestartReason": wrsRestartReason,
       "wrsFaultIP": wrsFaultIP,
       "wrsFaultLR": wrsFaultLR,
       "wrsConfigSource": wrsConfigSource,
       "wrsConfigSourceUrl": wrsConfigSourceUrl,
       "wrsRestartReasonMonit": wrsRestartReasonMonit,
       "wrsBootConfigStatus": wrsBootConfigStatus,
       "wrsBootHwinfoReadout": wrsBootHwinfoReadout,
       "wrsBootLoadFPGA": wrsBootLoadFPGA,
       "wrsBootLoadLM32": wrsBootLoadLM32,
       "wrsBootKernelModulesMissing": wrsBootKernelModulesMissing,
       "wrsBootUserspaceDaemonsMissing": wrsBootUserspaceDaemonsMissing,
       "wrsGwWatchdogTimeouts": wrsGwWatchdogTimeouts,
       "wrsFwUpdateStatus": wrsFwUpdateStatus,
       "wrsCustomBootScriptSource": wrsCustomBootScriptSource,
       "wrsCustomBootScriptSourceUrl": wrsCustomBootScriptSourceUrl,
       "wrsCustomBootScriptStatus": wrsCustomBootScriptStatus,
       "wrsAuxClkSetStatus": wrsAuxClkSetStatus,
       "wrsThrottlingSetStatus": wrsThrottlingSetStatus,
       "wrsVlansSetStatus": wrsVlansSetStatus,
       "wrsTemperatureGroup": wrsTemperatureGroup,
       "wrsTempFPGA": wrsTempFPGA,
       "wrsTempPLL": wrsTempPLL,
       "wrsTempPSL": wrsTempPSL,
       "wrsTempPSR": wrsTempPSR,
       "wrsTempThresholdFPGA": wrsTempThresholdFPGA,
       "wrsTempThresholdPLL": wrsTempThresholdPLL,
       "wrsTempThresholdPSL": wrsTempThresholdPSL,
       "wrsTempThresholdPSR": wrsTempThresholdPSR,
       "wrsMemoryGroup": wrsMemoryGroup,
       "wrsMemoryTotal": wrsMemoryTotal,
       "wrsMemoryUsed": wrsMemoryUsed,
       "wrsMemoryUsedPerc": wrsMemoryUsedPerc,
       "wrsMemoryFree": wrsMemoryFree,
       "wrsCpuLoadGroup": wrsCpuLoadGroup,
       "wrsCPULoadAvg1min": wrsCPULoadAvg1min,
       "wrsCPULoadAvg5min": wrsCPULoadAvg5min,
       "wrsCPULoadAvg15min": wrsCPULoadAvg15min,
       "wrsDiskTable": wrsDiskTable,
       "wrsDiskEntry": wrsDiskEntry,
       "wrsDiskIndex": wrsDiskIndex,
       "wrsDiskMountPath": wrsDiskMountPath,
       "wrsDiskSize": wrsDiskSize,
       "wrsDiskUsed": wrsDiskUsed,
       "wrsDiskFree": wrsDiskFree,
       "wrsDiskUseRate": wrsDiskUseRate,
       "wrsDiskFilesystem": wrsDiskFilesystem,
       "wrsStartCntGroup": wrsStartCntGroup,
       "wrsStartCntHAL": wrsStartCntHAL,
       "wrsStartCntPTP": wrsStartCntPTP,
       "wrsStartCntRTUd": wrsStartCntRTUd,
       "wrsStartCntSshd": wrsStartCntSshd,
       "wrsStartCntHttpd": wrsStartCntHttpd,
       "wrsStartCntSnmpd": wrsStartCntSnmpd,
       "wrsStartCntSyslogd": wrsStartCntSyslogd,
       "wrsStartCntWrsWatchdog": wrsStartCntWrsWatchdog,
       "wrsStartCntLldpd": wrsStartCntLldpd,
       "wrsStartCntLdap": wrsStartCntLdap,
       "wrsStartCntRvlan": wrsStartCntRvlan,
       "wrsSpllState": wrsSpllState,
       "wrsSpllVersionGroup": wrsSpllVersionGroup,
       "wrsSpllVersion": wrsSpllVersion,
       "wrsSpllBuildDate": wrsSpllBuildDate,
       "wrsSpllBuildBy": wrsSpllBuildBy,
       "wrsSpllStatusGroup": wrsSpllStatusGroup,
       "wrsSpllMode": wrsSpllMode,
       "wrsSpllIrqCnt": wrsSpllIrqCnt,
       "wrsSpllSeqState": wrsSpllSeqState,
       "wrsSpllAlignState": wrsSpllAlignState,
       "wrsSpllHlock": wrsSpllHlock,
       "wrsSpllMlock": wrsSpllMlock,
       "wrsSpllHY": wrsSpllHY,
       "wrsSpllMY": wrsSpllMY,
       "wrsSpllDelCnt": wrsSpllDelCnt,
       "wrsPstatsTable": wrsPstatsTable,
       "wrsPstatsEntry": wrsPstatsEntry,
       "wrsPstatsIndex": wrsPstatsIndex,
       "wrsPstatsPortName": wrsPstatsPortName,
       "wrsPstatsTXUnderrun": wrsPstatsTXUnderrun,
       "wrsPstatsRXOverrun": wrsPstatsRXOverrun,
       "wrsPstatsRXInvalidCode": wrsPstatsRXInvalidCode,
       "wrsPstatsRXSyncLost": wrsPstatsRXSyncLost,
       "wrsPstatsRXPauseFrames": wrsPstatsRXPauseFrames,
       "wrsPstatsRXPfilterDropped": wrsPstatsRXPfilterDropped,
       "wrsPstatsRXPCSErrors": wrsPstatsRXPCSErrors,
       "wrsPstatsRXGiantFrames": wrsPstatsRXGiantFrames,
       "wrsPstatsRXRuntFrames": wrsPstatsRXRuntFrames,
       "wrsPstatsRXCRCErrors": wrsPstatsRXCRCErrors,
       "wrsPstatsRXPclass0": wrsPstatsRXPclass0,
       "wrsPstatsRXPclass1": wrsPstatsRXPclass1,
       "wrsPstatsRXPclass2": wrsPstatsRXPclass2,
       "wrsPstatsRXPclass3": wrsPstatsRXPclass3,
       "wrsPstatsRXPclass4": wrsPstatsRXPclass4,
       "wrsPstatsRXPclass5": wrsPstatsRXPclass5,
       "wrsPstatsRXPclass6": wrsPstatsRXPclass6,
       "wrsPstatsRXPclass7": wrsPstatsRXPclass7,
       "wrsPstatsTXFrames": wrsPstatsTXFrames,
       "wrsPstatsRXFrames": wrsPstatsRXFrames,
       "wrsPstatsRXDropRTUFull": wrsPstatsRXDropRTUFull,
       "wrsPstatsRXPrio0": wrsPstatsRXPrio0,
       "wrsPstatsRXPrio1": wrsPstatsRXPrio1,
       "wrsPstatsRXPrio2": wrsPstatsRXPrio2,
       "wrsPstatsRXPrio3": wrsPstatsRXPrio3,
       "wrsPstatsRXPrio4": wrsPstatsRXPrio4,
       "wrsPstatsRXPrio5": wrsPstatsRXPrio5,
       "wrsPstatsRXPrio6": wrsPstatsRXPrio6,
       "wrsPstatsRXPrio7": wrsPstatsRXPrio7,
       "wrsPstatsRTUValid": wrsPstatsRTUValid,
       "wrsPstatsRTUResponses": wrsPstatsRTUResponses,
       "wrsPstatsRTUDropped": wrsPstatsRTUDropped,
       "wrsPstatsFastMatchPriority": wrsPstatsFastMatchPriority,
       "wrsPstatsFastMatchFastForward": wrsPstatsFastMatchFastForward,
       "wrsPstatsFastMatchNonForward": wrsPstatsFastMatchNonForward,
       "wrsPstatsFastMatchRespValid": wrsPstatsFastMatchRespValid,
       "wrsPstatsFullMatchRespValid": wrsPstatsFullMatchRespValid,
       "wrsPstatsForwarded": wrsPstatsForwarded,
       "wrsPstatsTRURespValid": wrsPstatsTRURespValid,
       "wrsPtpDataTable": wrsPtpDataTable,
       "wrsPtpDataEntry": wrsPtpDataEntry,
       "wrsPtpDataIndex": wrsPtpDataIndex,
       "wrsPtpPortName": wrsPtpPortName,
       "wrsPtpGrandmasterID": wrsPtpGrandmasterID,
       "wrsPtpOwnID": wrsPtpOwnID,
       "wrsPtpMode": wrsPtpMode,
       "wrsPtpServoState": wrsPtpServoState,
       "wrsPtpServoStateN": wrsPtpServoStateN,
       "wrsPtpPhaseTracking": wrsPtpPhaseTracking,
       "wrsPtpSyncSource": wrsPtpSyncSource,
       "wrsPtpClockOffsetPs": wrsPtpClockOffsetPs,
       "wrsPtpClockOffsetPsHR": wrsPtpClockOffsetPsHR,
       "wrsPtpSkew": wrsPtpSkew,
       "wrsPtpRTT": wrsPtpRTT,
       "wrsPtpLinkLength": wrsPtpLinkLength,
       "wrsPtpServoUpdates": wrsPtpServoUpdates,
       "wrsPtpDeltaTxM": wrsPtpDeltaTxM,
       "wrsPtpDeltaRxM": wrsPtpDeltaRxM,
       "wrsPtpDeltaTxS": wrsPtpDeltaTxS,
       "wrsPtpDeltaRxS": wrsPtpDeltaRxS,
       "wrsPtpServoStateErrCnt": wrsPtpServoStateErrCnt,
       "wrsPtpClockOffsetErrCnt": wrsPtpClockOffsetErrCnt,
       "wrsPtpRTTErrCnt": wrsPtpRTTErrCnt,
       "wrsPtpServoUpdateTime": wrsPtpServoUpdateTime,
       "wrsPtpServoExt": wrsPtpServoExt,
       "wrsPortStatusTable": wrsPortStatusTable,
       "wrsPortStatusEntry": wrsPortStatusEntry,
       "wrsPortStatusIndex": wrsPortStatusIndex,
       "wrsPortStatusPortName": wrsPortStatusPortName,
       "wrsPortStatusLink": wrsPortStatusLink,
       "wrsPortStatusConfiguredMode": wrsPortStatusConfiguredMode,
       "wrsPortStatusLocked": wrsPortStatusLocked,
       "wrsPortStatusPeer": wrsPortStatusPeer,
       "wrsPortStatusSfpVN": wrsPortStatusSfpVN,
       "wrsPortStatusSfpPN": wrsPortStatusSfpPN,
       "wrsPortStatusSfpVS": wrsPortStatusSfpVS,
       "wrsPortStatusSfpInDB": wrsPortStatusSfpInDB,
       "wrsPortStatusSfpGbE": wrsPortStatusSfpGbE,
       "wrsPortStatusSfpError": wrsPortStatusSfpError,
       "wrsPortStatusPtpTxFrames": wrsPortStatusPtpTxFrames,
       "wrsPortStatusPtpRxFrames": wrsPortStatusPtpRxFrames,
       "wrsPortStatusMonitor": wrsPortStatusMonitor,
       "wrsPortStatusSfpDom": wrsPortStatusSfpDom,
       "wrsPortStatusSfpTemp": wrsPortStatusSfpTemp,
       "wrsPortStatusSfpVcc": wrsPortStatusSfpVcc,
       "wrsPortStatusSfpTxBias": wrsPortStatusSfpTxBias,
       "wrsPortStatusSfpTxPower": wrsPortStatusSfpTxPower,
       "wrsPortStatusSfpRxPower": wrsPortStatusSfpRxPower,
       "wrsPortStatusT24p": wrsPortStatusT24p,
       "wrsPortStatusT24pValid": wrsPortStatusT24pValid,
       "wrsPstatsHCTable": wrsPstatsHCTable,
       "wrsPstatsHCEntry": wrsPstatsHCEntry,
       "wrsPstatsHCIndex": wrsPstatsHCIndex,
       "wrsPstatsHCPortName": wrsPstatsHCPortName,
       "wrsPstatsHCTXUnderrun": wrsPstatsHCTXUnderrun,
       "wrsPstatsHCRXOverrun": wrsPstatsHCRXOverrun,
       "wrsPstatsHCRXInvalidCode": wrsPstatsHCRXInvalidCode,
       "wrsPstatsHCRXSyncLost": wrsPstatsHCRXSyncLost,
       "wrsPstatsHCRXPauseFrames": wrsPstatsHCRXPauseFrames,
       "wrsPstatsHCRXPfilterDropped": wrsPstatsHCRXPfilterDropped,
       "wrsPstatsHCRXPCSErrors": wrsPstatsHCRXPCSErrors,
       "wrsPstatsHCRXGiantFrames": wrsPstatsHCRXGiantFrames,
       "wrsPstatsHCRXRuntFrames": wrsPstatsHCRXRuntFrames,
       "wrsPstatsHCRXCRCErrors": wrsPstatsHCRXCRCErrors,
       "wrsPstatsHCRXPclass0": wrsPstatsHCRXPclass0,
       "wrsPstatsHCRXPclass1": wrsPstatsHCRXPclass1,
       "wrsPstatsHCRXPclass2": wrsPstatsHCRXPclass2,
       "wrsPstatsHCRXPclass3": wrsPstatsHCRXPclass3,
       "wrsPstatsHCRXPclass4": wrsPstatsHCRXPclass4,
       "wrsPstatsHCRXPclass5": wrsPstatsHCRXPclass5,
       "wrsPstatsHCRXPclass6": wrsPstatsHCRXPclass6,
       "wrsPstatsHCRXPclass7": wrsPstatsHCRXPclass7,
       "wrsPstatsHCTXFrames": wrsPstatsHCTXFrames,
       "wrsPstatsHCRXFrames": wrsPstatsHCRXFrames,
       "wrsPstatsHCRXDropRTUFull": wrsPstatsHCRXDropRTUFull,
       "wrsPstatsHCRXPrio0": wrsPstatsHCRXPrio0,
       "wrsPstatsHCRXPrio1": wrsPstatsHCRXPrio1,
       "wrsPstatsHCRXPrio2": wrsPstatsHCRXPrio2,
       "wrsPstatsHCRXPrio3": wrsPstatsHCRXPrio3,
       "wrsPstatsHCRXPrio4": wrsPstatsHCRXPrio4,
       "wrsPstatsHCRXPrio5": wrsPstatsHCRXPrio5,
       "wrsPstatsHCRXPrio6": wrsPstatsHCRXPrio6,
       "wrsPstatsHCRXPrio7": wrsPstatsHCRXPrio7,
       "wrsPstatsHCRTUValid": wrsPstatsHCRTUValid,
       "wrsPstatsHCRTUResponses": wrsPstatsHCRTUResponses,
       "wrsPstatsHCRTUDropped": wrsPstatsHCRTUDropped,
       "wrsPstatsHCFastMatchPriority": wrsPstatsHCFastMatchPriority,
       "wrsPstatsHCFastMatchFastForward": wrsPstatsHCFastMatchFastForward,
       "wrsPstatsHCFastMatchNonForward": wrsPstatsHCFastMatchNonForward,
       "wrsPstatsHCFastMatchRespValid": wrsPstatsHCFastMatchRespValid,
       "wrsPstatsHCFullMatchRespValid": wrsPstatsHCFullMatchRespValid,
       "wrsPstatsHCForwarded": wrsPstatsHCForwarded,
       "wrsPstatsHCTRURespValid": wrsPstatsHCTRURespValid,
       "wrsPstatsHCNICTXFrames": wrsPstatsHCNICTXFrames,
       "wrsPtpInstanceTable": wrsPtpInstanceTable,
       "wrsPtpInstanceEntry": wrsPtpInstanceEntry,
       "wrsPtpInstancePortIndex": wrsPtpInstancePortIndex,
       "wrsPtpInstanceOnPortIndex": wrsPtpInstanceOnPortIndex,
       "wrsPtpInstanceName": wrsPtpInstanceName,
       "wrsPtpInstancePort": wrsPtpInstancePort,
       "wrsPtpInstancePortInstance": wrsPtpInstancePortInstance,
       "wrsPtpInstancePortName": wrsPtpInstancePortName,
       "wrsPtpInstanceState": wrsPtpInstanceState,
       "wrsPtpInstanceMasterOnly": wrsPtpInstanceMasterOnly,
       "wrsPtpInstanceExtPortCfgDesSt": wrsPtpInstanceExtPortCfgDesSt,
       "wrsPtpInstanceMechanism": wrsPtpInstanceMechanism,
       "wrsPtpInstanceProfile": wrsPtpInstanceProfile,
       "wrsPtpInstanceExtension": wrsPtpInstanceExtension,
       "wrsPtpInstanceAsymEnabled": wrsPtpInstanceAsymEnabled,
       "wrsPtpInstanceAsymConstAsymPS": wrsPtpInstanceAsymConstAsymPS,
       "wrsPtpInstanceAsymScDelayCoef": wrsPtpInstanceAsymScDelayCoef,
       "wrsPtpInstanceAsymScDelayCoefHR": wrsPtpInstanceAsymScDelayCoefHR,
       "wrsPtpInstanceTSCorrEgressLatPS": wrsPtpInstanceTSCorrEgressLatPS,
       "wrsPtpInstanceTSCorrIngLatPS": wrsPtpInstanceTSCorrIngLatPS,
       "wrsPtpInstanceTSCorrSemistLatPS": wrsPtpInstanceTSCorrSemistLatPS,
       "wrsPtpInstanceProtoDetectState": wrsPtpInstanceProtoDetectState,
       "wrsPtpInstanceExtState": wrsPtpInstanceExtState,
       "wrsPtpInstancePeerMac": wrsPtpInstancePeerMac,
       "wrsPtpInstancePeerVid": wrsPtpInstancePeerVid,
       "wrsPtpInstanceVlanNum": wrsPtpInstanceVlanNum,
       "wrsPtpInstanceVlanListStr": wrsPtpInstanceVlanListStr,
       "wrsPtpInstanceStatusError": wrsPtpInstanceStatusError,
       "wrsId": wrsId,
       "wrsIdUnkn": wrsIdUnkn,
       "wrsIdUnknUnkn": wrsIdUnknUnkn,
       "wrsIdOther": wrsIdOther,
       "wrsId3": wrsId3,
       "wrsId3Unkn": wrsId3Unkn,
       "wrsId3UnknUnkn": wrsId3UnknUnkn,
       "wrsId3Unkn3": wrsId3Unkn3,
       "wrsId3Unkn4": wrsId3Unkn4,
       "wrsId3UnknFL": wrsId3UnknFL,
       "wrsId3Ssol": wrsId3Ssol,
       "wrsId3SsolUnkn": wrsId3SsolUnkn,
       "wrsId3Ssol3": wrsId3Ssol3,
       "wrsId3Ssol4": wrsId3Ssol4,
       "wrsId3Cti": wrsId3Cti,
       "wrsId3CtiUnkn": wrsId3CtiUnkn,
       "wrsId3Cti3": wrsId3Cti3,
       "wrsId3Cti4": wrsId3Cti4,
       "wrsId3St": wrsId3St,
       "wrsId3StUnkn": wrsId3StUnkn,
       "wrsId3St3": wrsId3St3,
       "wrsId3St4": wrsId3St4,
       "wrsId3StFL": wrsId3StFL,
       "wrsId3Opnt": wrsId3Opnt,
       "wrsId3OpntUnkn": wrsId3OpntUnkn,
       "wrsId3Opnt3": wrsId3Opnt3,
       "wrsId3Opnt4": wrsId3Opnt4}
)
