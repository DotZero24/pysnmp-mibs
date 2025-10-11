# SNMP MIB module (ENTERASYS-STATION-LOCATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-STATION-LOCATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:00 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysStationLocationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98)
)
if mibBuilder.loadTexts:
    etsysStationLocationMIB.setRevisions(
        ("2016-05-11 19:36",
         "2015-09-10 16:18",
         "2014-06-13 16:10",
         "2013-04-18 15:20")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FloorEnvironmentType(TextualConvention, Integer32):
    status = "current"
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
        *(("openSpace", 0),
          ("lightDivision", 1),
          ("dryWallsDivision", 2),
          ("hardDivision", 3),
          ("interiorWalls", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysStationLocationMIBObjects_ObjectIdentity = ObjectIdentity
etsysStationLocationMIBObjects = _EtsysStationLocationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1)
)
_EtsysLocationConfiguration_ObjectIdentity = ObjectIdentity
etsysLocationConfiguration = _EtsysLocationConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1)
)
_EtsysLocationEngineEnable_Type = TruthValue
_EtsysLocationEngineEnable_Object = MibScalar
etsysLocationEngineEnable = _EtsysLocationEngineEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 1),
    _EtsysLocationEngineEnable_Type()
)
etsysLocationEngineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineEnable.setStatus("current")
_EtsysLocationEngineAutoTrkEnable_Type = TruthValue
_EtsysLocationEngineAutoTrkEnable_Object = MibScalar
etsysLocationEngineAutoTrkEnable = _EtsysLocationEngineAutoTrkEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 2),
    _EtsysLocationEngineAutoTrkEnable_Type()
)
etsysLocationEngineAutoTrkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineAutoTrkEnable.setStatus("current")


class _EtsysLocationEngineGlblAPHeight_Type(Unsigned32):
    """Custom type etsysLocationEngineGlblAPHeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EtsysLocationEngineGlblAPHeight_Type.__name__ = "Unsigned32"
_EtsysLocationEngineGlblAPHeight_Object = MibScalar
etsysLocationEngineGlblAPHeight = _EtsysLocationEngineGlblAPHeight_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 3),
    _EtsysLocationEngineGlblAPHeight_Type()
)
etsysLocationEngineGlblAPHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineGlblAPHeight.setStatus("current")
if mibBuilder.loadTexts:
    etsysLocationEngineGlblAPHeight.setUnits("centimeters")
_EtsysLocationEngineGlobalEnv_Type = FloorEnvironmentType
_EtsysLocationEngineGlobalEnv_Object = MibScalar
etsysLocationEngineGlobalEnv = _EtsysLocationEngineGlobalEnv_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 4),
    _EtsysLocationEngineGlobalEnv_Type()
)
etsysLocationEngineGlobalEnv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineGlobalEnv.setStatus("current")
_EtsysLocationFloors_ObjectIdentity = ObjectIdentity
etsysLocationFloors = _EtsysLocationFloors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5)
)
_EtsysLocationMaxFloorLimit_Type = Unsigned32
_EtsysLocationMaxFloorLimit_Object = MibScalar
etsysLocationMaxFloorLimit = _EtsysLocationMaxFloorLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 1),
    _EtsysLocationMaxFloorLimit_Type()
)
etsysLocationMaxFloorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLocationMaxFloorLimit.setStatus("current")
_EtsysLocationFloorConfigured_Type = Unsigned32
_EtsysLocationFloorConfigured_Object = MibScalar
etsysLocationFloorConfigured = _EtsysLocationFloorConfigured_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 2),
    _EtsysLocationFloorConfigured_Type()
)
etsysLocationFloorConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysLocationFloorConfigured.setStatus("current")
_EtsysFloorTable_Object = MibTable
etsysFloorTable = _EtsysFloorTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    etsysFloorTable.setStatus("current")
_EtsysFloorEntry_Object = MibTableRow
etsysFloorEntry = _EtsysFloorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1)
)
etsysFloorEntry.setIndexNames(
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysFloorID"),
)
if mibBuilder.loadTexts:
    etsysFloorEntry.setStatus("current")
_EtsysFloorID_Type = Unsigned32
_EtsysFloorID_Object = MibTableColumn
etsysFloorID = _EtsysFloorID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 1),
    _EtsysFloorID_Type()
)
etsysFloorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFloorID.setStatus("current")
_EtsysFloorRowStatus_Type = RowStatus
_EtsysFloorRowStatus_Object = MibTableColumn
etsysFloorRowStatus = _EtsysFloorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 2),
    _EtsysFloorRowStatus_Type()
)
etsysFloorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorRowStatus.setStatus("current")


class _EtsysFloorName_Type(SnmpAdminString):
    """Custom type etsysFloorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysFloorName_Type.__name__ = "SnmpAdminString"
_EtsysFloorName_Object = MibTableColumn
etsysFloorName = _EtsysFloorName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 3),
    _EtsysFloorName_Type()
)
etsysFloorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorName.setStatus("current")
_EtsysFloorNumberOfAPs_Type = Unsigned32
_EtsysFloorNumberOfAPs_Object = MibTableColumn
etsysFloorNumberOfAPs = _EtsysFloorNumberOfAPs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 4),
    _EtsysFloorNumberOfAPs_Type()
)
etsysFloorNumberOfAPs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorNumberOfAPs.setStatus("current")
_EtsysFloorWidth_Type = Unsigned32
_EtsysFloorWidth_Object = MibTableColumn
etsysFloorWidth = _EtsysFloorWidth_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 5),
    _EtsysFloorWidth_Type()
)
etsysFloorWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorWidth.setStatus("current")
if mibBuilder.loadTexts:
    etsysFloorWidth.setUnits("centimeters")
_EtsysFloorLength_Type = Unsigned32
_EtsysFloorLength_Object = MibTableColumn
etsysFloorLength = _EtsysFloorLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 6),
    _EtsysFloorLength_Type()
)
etsysFloorLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorLength.setStatus("current")
if mibBuilder.loadTexts:
    etsysFloorLength.setUnits("centimeters")
_EtsysFloorNumberOfCells_Type = Unsigned32
_EtsysFloorNumberOfCells_Object = MibTableColumn
etsysFloorNumberOfCells = _EtsysFloorNumberOfCells_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 7),
    _EtsysFloorNumberOfCells_Type()
)
etsysFloorNumberOfCells.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorNumberOfCells.setStatus("current")
if mibBuilder.loadTexts:
    etsysFloorNumberOfCells.setUnits("centimeters")
_EtsysFloorCellWidth_Type = Unsigned32
_EtsysFloorCellWidth_Object = MibTableColumn
etsysFloorCellWidth = _EtsysFloorCellWidth_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 8),
    _EtsysFloorCellWidth_Type()
)
etsysFloorCellWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorCellWidth.setStatus("current")
if mibBuilder.loadTexts:
    etsysFloorCellWidth.setUnits("centimeters")
_EtsysFloorCellLength_Type = Unsigned32
_EtsysFloorCellLength_Object = MibTableColumn
etsysFloorCellLength = _EtsysFloorCellLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 9),
    _EtsysFloorCellLength_Type()
)
etsysFloorCellLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorCellLength.setStatus("current")
if mibBuilder.loadTexts:
    etsysFloorCellLength.setUnits("centimeters")
_EtsysFloorEnvironment_Type = FloorEnvironmentType
_EtsysFloorEnvironment_Object = MibTableColumn
etsysFloorEnvironment = _EtsysFloorEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 10),
    _EtsysFloorEnvironment_Type()
)
etsysFloorEnvironment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorEnvironment.setStatus("current")


class _EtsysFloorHashString_Type(OctetString):
    """Custom type etsysFloorHashString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_EtsysFloorHashString_Type.__name__ = "OctetString"
_EtsysFloorHashString_Object = MibTableColumn
etsysFloorHashString = _EtsysFloorHashString_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 5, 3, 1, 11),
    _EtsysFloorHashString_Type()
)
etsysFloorHashString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFloorHashString.setStatus("current")
_EtsysLocationStations_ObjectIdentity = ObjectIdentity
etsysLocationStations = _EtsysLocationStations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6)
)
_EtsysMaxTrackedStationLimit_Type = Unsigned32
_EtsysMaxTrackedStationLimit_Object = MibScalar
etsysMaxTrackedStationLimit = _EtsysMaxTrackedStationLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 1),
    _EtsysMaxTrackedStationLimit_Type()
)
etsysMaxTrackedStationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMaxTrackedStationLimit.setStatus("current")


class _EtsysMaxOnDemandStationLimit_Type(Unsigned32):
    """Custom type etsysMaxOnDemandStationLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EtsysMaxOnDemandStationLimit_Type.__name__ = "Unsigned32"
_EtsysMaxOnDemandStationLimit_Object = MibScalar
etsysMaxOnDemandStationLimit = _EtsysMaxOnDemandStationLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 2),
    _EtsysMaxOnDemandStationLimit_Type()
)
etsysMaxOnDemandStationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMaxOnDemandStationLimit.setStatus("current")
_EtsysOnDemandStationTable_Object = MibTable
etsysOnDemandStationTable = _EtsysOnDemandStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    etsysOnDemandStationTable.setStatus("current")
_EtsysOnDemandStationEntry_Object = MibTableRow
etsysOnDemandStationEntry = _EtsysOnDemandStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 3, 1)
)
etsysOnDemandStationEntry.setIndexNames(
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysOnDemandStationMAC"),
)
if mibBuilder.loadTexts:
    etsysOnDemandStationEntry.setStatus("current")
_EtsysOnDemandStationMAC_Type = MacAddress
_EtsysOnDemandStationMAC_Object = MibTableColumn
etsysOnDemandStationMAC = _EtsysOnDemandStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 3, 1, 1),
    _EtsysOnDemandStationMAC_Type()
)
etsysOnDemandStationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysOnDemandStationMAC.setStatus("current")
_EtsysOnDemandStationRowStatus_Type = RowStatus
_EtsysOnDemandStationRowStatus_Object = MibTableColumn
etsysOnDemandStationRowStatus = _EtsysOnDemandStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 6, 3, 1, 2),
    _EtsysOnDemandStationRowStatus_Type()
)
etsysOnDemandStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOnDemandStationRowStatus.setStatus("current")


class _EtsysLocationEngineTrackAreaChange_Type(Integer32):
    """Custom type etsysLocationEngineTrackAreaChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EtsysLocationEngineTrackAreaChange_Type.__name__ = "Integer32"
_EtsysLocationEngineTrackAreaChange_Object = MibScalar
etsysLocationEngineTrackAreaChange = _EtsysLocationEngineTrackAreaChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 7),
    _EtsysLocationEngineTrackAreaChange_Type()
)
etsysLocationEngineTrackAreaChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineTrackAreaChange.setStatus("current")


class _EtsysLocationEngineTrackMode_Type(Integer32):
    """Custom type etsysLocationEngineTrackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trackClients", 1),
          ("trackAll", 2),
          ("trackNone", 3))
    )


_EtsysLocationEngineTrackMode_Type.__name__ = "Integer32"
_EtsysLocationEngineTrackMode_Object = MibScalar
etsysLocationEngineTrackMode = _EtsysLocationEngineTrackMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 1, 8),
    _EtsysLocationEngineTrackMode_Type()
)
etsysLocationEngineTrackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationEngineTrackMode.setStatus("current")
_EtsysLocationReports_ObjectIdentity = ObjectIdentity
etsysLocationReports = _EtsysLocationReports_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2)
)
_EtsysTrackedStationTable_Object = MibTable
etsysTrackedStationTable = _EtsysTrackedStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysTrackedStationTable.setStatus("current")
_EtsysTrackedStationEntry_Object = MibTableRow
etsysTrackedStationEntry = _EtsysTrackedStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1)
)
etsysTrackedStationEntry.setIndexNames(
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationMAC"),
)
if mibBuilder.loadTexts:
    etsysTrackedStationEntry.setStatus("current")
_EtsysTrackedStationMAC_Type = MacAddress
_EtsysTrackedStationMAC_Object = MibTableColumn
etsysTrackedStationMAC = _EtsysTrackedStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1, 1),
    _EtsysTrackedStationMAC_Type()
)
etsysTrackedStationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTrackedStationMAC.setStatus("current")
_EtsysTrackedStationFloorID_Type = Unsigned32
_EtsysTrackedStationFloorID_Object = MibTableColumn
etsysTrackedStationFloorID = _EtsysTrackedStationFloorID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1, 2),
    _EtsysTrackedStationFloorID_Type()
)
etsysTrackedStationFloorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedStationFloorID.setStatus("current")


class _EtsysTrackedStationLocationType_Type(Integer32):
    """Custom type etsysTrackedStationLocationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("rssBasedLocation", 1),
          ("cellOfOrigin", 2))
    )


_EtsysTrackedStationLocationType_Type.__name__ = "Integer32"
_EtsysTrackedStationLocationType_Object = MibTableColumn
etsysTrackedStationLocationType = _EtsysTrackedStationLocationType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1, 3),
    _EtsysTrackedStationLocationType_Type()
)
etsysTrackedStationLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedStationLocationType.setStatus("current")
_EtsysTrackedStationReportingAPSN_Type = SnmpAdminString
_EtsysTrackedStationReportingAPSN_Object = MibTableColumn
etsysTrackedStationReportingAPSN = _EtsysTrackedStationReportingAPSN_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1, 6),
    _EtsysTrackedStationReportingAPSN_Type()
)
etsysTrackedStationReportingAPSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedStationReportingAPSN.setStatus("current")
_EtsysTrackedStationAPDistance_Type = Integer32
_EtsysTrackedStationAPDistance_Object = MibTableColumn
etsysTrackedStationAPDistance = _EtsysTrackedStationAPDistance_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 1, 1, 7),
    _EtsysTrackedStationAPDistance_Type()
)
etsysTrackedStationAPDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTrackedStationAPDistance.setStatus("current")
if mibBuilder.loadTexts:
    etsysTrackedStationAPDistance.setUnits("meters")
_EtsysStationLocationGridTable_Object = MibTable
etsysStationLocationGridTable = _EtsysStationLocationGridTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysStationLocationGridTable.setStatus("current")
_EtsysStationLocationGridEntry_Object = MibTableRow
etsysStationLocationGridEntry = _EtsysStationLocationGridEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2, 1)
)
etsysStationLocationGridEntry.setIndexNames(
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationMAC"),
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysStationLocnGridIndex"),
)
if mibBuilder.loadTexts:
    etsysStationLocationGridEntry.setStatus("current")
_EtsysStationLocnGridIndex_Type = Unsigned32
_EtsysStationLocnGridIndex_Object = MibTableColumn
etsysStationLocnGridIndex = _EtsysStationLocnGridIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2, 1, 1),
    _EtsysStationLocnGridIndex_Type()
)
etsysStationLocnGridIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysStationLocnGridIndex.setStatus("current")
_EtsysStationLocnGridX_Type = Integer32
_EtsysStationLocnGridX_Object = MibTableColumn
etsysStationLocnGridX = _EtsysStationLocnGridX_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2, 1, 2),
    _EtsysStationLocnGridX_Type()
)
etsysStationLocnGridX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationLocnGridX.setStatus("current")
_EtsysStationLocnGridY_Type = Integer32
_EtsysStationLocnGridY_Object = MibTableColumn
etsysStationLocnGridY = _EtsysStationLocnGridY_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2, 1, 3),
    _EtsysStationLocnGridY_Type()
)
etsysStationLocnGridY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationLocnGridY.setStatus("current")


class _EtsysStationLocnGridProbability_Type(Integer32):
    """Custom type etsysStationLocnGridProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EtsysStationLocnGridProbability_Type.__name__ = "Integer32"
_EtsysStationLocnGridProbability_Object = MibTableColumn
etsysStationLocnGridProbability = _EtsysStationLocnGridProbability_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 2, 2, 1, 4),
    _EtsysStationLocnGridProbability_Type()
)
etsysStationLocnGridProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysStationLocnGridProbability.setStatus("current")
_EtsysLocationBatchReport_ObjectIdentity = ObjectIdentity
etsysLocationBatchReport = _EtsysLocationBatchReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3)
)
_EtsysLocationBatchReportEnable_Type = TruthValue
_EtsysLocationBatchReportEnable_Object = MibScalar
etsysLocationBatchReportEnable = _EtsysLocationBatchReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 1),
    _EtsysLocationBatchReportEnable_Type()
)
etsysLocationBatchReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationBatchReportEnable.setStatus("current")


class _EtsysLocationBatchReportFrequency_Type(Unsigned32):
    """Custom type etsysLocationBatchReportFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 4294967295),
    )


_EtsysLocationBatchReportFrequency_Type.__name__ = "Unsigned32"
_EtsysLocationBatchReportFrequency_Object = MibScalar
etsysLocationBatchReportFrequency = _EtsysLocationBatchReportFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 2),
    _EtsysLocationBatchReportFrequency_Type()
)
etsysLocationBatchReportFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationBatchReportFrequency.setStatus("current")
_EtsysPublishLocationURLMaxEntries_Type = Unsigned32
_EtsysPublishLocationURLMaxEntries_Object = MibScalar
etsysPublishLocationURLMaxEntries = _EtsysPublishLocationURLMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 3),
    _EtsysPublishLocationURLMaxEntries_Type()
)
etsysPublishLocationURLMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPublishLocationURLMaxEntries.setStatus("current")
_EtsysPublishLocationURLNumEntries_Type = Unsigned32
_EtsysPublishLocationURLNumEntries_Object = MibScalar
etsysPublishLocationURLNumEntries = _EtsysPublishLocationURLNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 4),
    _EtsysPublishLocationURLNumEntries_Type()
)
etsysPublishLocationURLNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPublishLocationURLNumEntries.setStatus("current")
_EtsysPublishLocationURLTable_Object = MibTable
etsysPublishLocationURLTable = _EtsysPublishLocationURLTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5)
)
if mibBuilder.loadTexts:
    etsysPublishLocationURLTable.setStatus("current")
_EtsysPublishLocationURLEntry_Object = MibTableRow
etsysPublishLocationURLEntry = _EtsysPublishLocationURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1)
)
etsysPublishLocationURLEntry.setIndexNames(
    (0, "ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationIndex"),
)
if mibBuilder.loadTexts:
    etsysPublishLocationURLEntry.setStatus("current")


class _EtsysPublishLocationIndex_Type(Unsigned32):
    """Custom type etsysPublishLocationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysPublishLocationIndex_Type.__name__ = "Unsigned32"
_EtsysPublishLocationIndex_Object = MibTableColumn
etsysPublishLocationIndex = _EtsysPublishLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1, 1),
    _EtsysPublishLocationIndex_Type()
)
etsysPublishLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPublishLocationIndex.setStatus("current")


class _EtsysPublishLocationURL_Type(OctetString):
    """Custom type etsysPublishLocationURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EtsysPublishLocationURL_Type.__name__ = "OctetString"
_EtsysPublishLocationURL_Object = MibTableColumn
etsysPublishLocationURL = _EtsysPublishLocationURL_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1, 2),
    _EtsysPublishLocationURL_Type()
)
etsysPublishLocationURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPublishLocationURL.setStatus("current")
_EtsysPublishLocationRowStatus_Type = RowStatus
_EtsysPublishLocationRowStatus_Object = MibTableColumn
etsysPublishLocationRowStatus = _EtsysPublishLocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1, 3),
    _EtsysPublishLocationRowStatus_Type()
)
etsysPublishLocationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPublishLocationRowStatus.setStatus("current")
_EtsysPublishLocationUserId_Type = SnmpAdminString
_EtsysPublishLocationUserId_Object = MibTableColumn
etsysPublishLocationUserId = _EtsysPublishLocationUserId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1, 4),
    _EtsysPublishLocationUserId_Type()
)
etsysPublishLocationUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPublishLocationUserId.setStatus("current")
_EtsysPublishLocationPassword_Type = SnmpAdminString
_EtsysPublishLocationPassword_Object = MibTableColumn
etsysPublishLocationPassword = _EtsysPublishLocationPassword_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 5, 1, 5),
    _EtsysPublishLocationPassword_Type()
)
etsysPublishLocationPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysPublishLocationPassword.setStatus("current")


class _EtsysLocationBatchReportDimensionUnit_Type(Integer32):
    """Custom type etsysLocationBatchReportDimensionUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("meter", 0),
          ("feet", 1))
    )


_EtsysLocationBatchReportDimensionUnit_Type.__name__ = "Integer32"
_EtsysLocationBatchReportDimensionUnit_Object = MibScalar
etsysLocationBatchReportDimensionUnit = _EtsysLocationBatchReportDimensionUnit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 1, 3, 6),
    _EtsysLocationBatchReportDimensionUnit_Type()
)
etsysLocationBatchReportDimensionUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysLocationBatchReportDimensionUnit.setStatus("current")
_EtsysStationLocationConformance_ObjectIdentity = ObjectIdentity
etsysStationLocationConformance = _EtsysStationLocationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2)
)
_EtsysStationLocationGroups_ObjectIdentity = ObjectIdentity
etsysStationLocationGroups = _EtsysStationLocationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1)
)
_EtsysStationLocationCompliances_ObjectIdentity = ObjectIdentity
etsysStationLocationCompliances = _EtsysStationLocationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 2)
)

# Managed Objects groups

etsysLocationEngineGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 1)
)
etsysLocationEngineGlobalGroup.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineAutoTrkEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlblAPHeight"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalEnv"))
)
if mibBuilder.loadTexts:
    etsysLocationEngineGlobalGroup.setStatus("deprecated")

etsysFloorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 2)
)
etsysFloorGroup.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorRowStatus"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorName"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorNumberOfAPs"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorWidth"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorLength"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorNumberOfCells"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorCellWidth"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorCellLength"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorHashString"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorEnvironment"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationMaxFloorLimit"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationFloorConfigured"))
)
if mibBuilder.loadTexts:
    etsysFloorGroup.setStatus("current")

etsysOnDemandStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 3)
)
etsysOnDemandStationsGroup.setObjects(
    ("ENTERASYS-STATION-LOCATION-MIB", "etsysOnDemandStationRowStatus")
)
if mibBuilder.loadTexts:
    etsysOnDemandStationsGroup.setStatus("current")

etsysTrackedStationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 4)
)
etsysTrackedStationsGroup.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationFloorID"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationLocationType"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationReportingAPSN"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationAPDistance"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysStationLocnGridX"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysStationLocnGridY"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysStationLocnGridProbability"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysMaxOnDemandStationLimit"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysMaxTrackedStationLimit"))
)
if mibBuilder.loadTexts:
    etsysTrackedStationsGroup.setStatus("current")

etsysLocationBatchReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 5)
)
etsysLocationBatchReportGroup.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportFrequency"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportDimensionUnit"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURLMaxEntries"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURLNumEntries"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURL"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationRowStatus"))
)
if mibBuilder.loadTexts:
    etsysLocationBatchReportGroup.setStatus("deprecated")

etsysLocationEngineGlobalGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 6)
)
etsysLocationEngineGlobalGroup2.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineAutoTrkEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlblAPHeight"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalEnv"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineTrackAreaChange"))
)
if mibBuilder.loadTexts:
    etsysLocationEngineGlobalGroup2.setStatus("deprecated")

etsysLocationEngineGlobalGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 7)
)
etsysLocationEngineGlobalGroup3.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineAutoTrkEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlblAPHeight"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalEnv"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineTrackAreaChange"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineTrackMode"))
)
if mibBuilder.loadTexts:
    etsysLocationEngineGlobalGroup3.setStatus("current")

etsysLocationBatchReportGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 1, 8)
)
etsysLocationBatchReportGroup2.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportEnable"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportFrequency"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportDimensionUnit"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURLMaxEntries"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURLNumEntries"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationURL"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationRowStatus"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationUserId"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysPublishLocationPassword"))
)
if mibBuilder.loadTexts:
    etsysLocationBatchReportGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysStationLocationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 2, 1)
)
etsysStationLocationCompliance.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysOnDemandStationsGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationsGroup"))
)
if mibBuilder.loadTexts:
    etsysStationLocationCompliance.setStatus(
        "deprecated"
    )

etsysStationLocationCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 2, 2)
)
etsysStationLocationCompliance2.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalGroup2"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysOnDemandStationsGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationsGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportGroup"))
)
if mibBuilder.loadTexts:
    etsysStationLocationCompliance2.setStatus(
        "deprecated"
    )

etsysStationLocationCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 98, 2, 2, 3)
)
etsysStationLocationCompliance3.setObjects(
      *(("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationEngineGlobalGroup3"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysFloorGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysOnDemandStationsGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysTrackedStationsGroup"),
        ("ENTERASYS-STATION-LOCATION-MIB", "etsysLocationBatchReportGroup2"))
)
if mibBuilder.loadTexts:
    etsysStationLocationCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-STATION-LOCATION-MIB",
    **{"FloorEnvironmentType": FloorEnvironmentType,
       "etsysStationLocationMIB": etsysStationLocationMIB,
       "etsysStationLocationMIBObjects": etsysStationLocationMIBObjects,
       "etsysLocationConfiguration": etsysLocationConfiguration,
       "etsysLocationEngineEnable": etsysLocationEngineEnable,
       "etsysLocationEngineAutoTrkEnable": etsysLocationEngineAutoTrkEnable,
       "etsysLocationEngineGlblAPHeight": etsysLocationEngineGlblAPHeight,
       "etsysLocationEngineGlobalEnv": etsysLocationEngineGlobalEnv,
       "etsysLocationFloors": etsysLocationFloors,
       "etsysLocationMaxFloorLimit": etsysLocationMaxFloorLimit,
       "etsysLocationFloorConfigured": etsysLocationFloorConfigured,
       "etsysFloorTable": etsysFloorTable,
       "etsysFloorEntry": etsysFloorEntry,
       "etsysFloorID": etsysFloorID,
       "etsysFloorRowStatus": etsysFloorRowStatus,
       "etsysFloorName": etsysFloorName,
       "etsysFloorNumberOfAPs": etsysFloorNumberOfAPs,
       "etsysFloorWidth": etsysFloorWidth,
       "etsysFloorLength": etsysFloorLength,
       "etsysFloorNumberOfCells": etsysFloorNumberOfCells,
       "etsysFloorCellWidth": etsysFloorCellWidth,
       "etsysFloorCellLength": etsysFloorCellLength,
       "etsysFloorEnvironment": etsysFloorEnvironment,
       "etsysFloorHashString": etsysFloorHashString,
       "etsysLocationStations": etsysLocationStations,
       "etsysMaxTrackedStationLimit": etsysMaxTrackedStationLimit,
       "etsysMaxOnDemandStationLimit": etsysMaxOnDemandStationLimit,
       "etsysOnDemandStationTable": etsysOnDemandStationTable,
       "etsysOnDemandStationEntry": etsysOnDemandStationEntry,
       "etsysOnDemandStationMAC": etsysOnDemandStationMAC,
       "etsysOnDemandStationRowStatus": etsysOnDemandStationRowStatus,
       "etsysLocationEngineTrackAreaChange": etsysLocationEngineTrackAreaChange,
       "etsysLocationEngineTrackMode": etsysLocationEngineTrackMode,
       "etsysLocationReports": etsysLocationReports,
       "etsysTrackedStationTable": etsysTrackedStationTable,
       "etsysTrackedStationEntry": etsysTrackedStationEntry,
       "etsysTrackedStationMAC": etsysTrackedStationMAC,
       "etsysTrackedStationFloorID": etsysTrackedStationFloorID,
       "etsysTrackedStationLocationType": etsysTrackedStationLocationType,
       "etsysTrackedStationReportingAPSN": etsysTrackedStationReportingAPSN,
       "etsysTrackedStationAPDistance": etsysTrackedStationAPDistance,
       "etsysStationLocationGridTable": etsysStationLocationGridTable,
       "etsysStationLocationGridEntry": etsysStationLocationGridEntry,
       "etsysStationLocnGridIndex": etsysStationLocnGridIndex,
       "etsysStationLocnGridX": etsysStationLocnGridX,
       "etsysStationLocnGridY": etsysStationLocnGridY,
       "etsysStationLocnGridProbability": etsysStationLocnGridProbability,
       "etsysLocationBatchReport": etsysLocationBatchReport,
       "etsysLocationBatchReportEnable": etsysLocationBatchReportEnable,
       "etsysLocationBatchReportFrequency": etsysLocationBatchReportFrequency,
       "etsysPublishLocationURLMaxEntries": etsysPublishLocationURLMaxEntries,
       "etsysPublishLocationURLNumEntries": etsysPublishLocationURLNumEntries,
       "etsysPublishLocationURLTable": etsysPublishLocationURLTable,
       "etsysPublishLocationURLEntry": etsysPublishLocationURLEntry,
       "etsysPublishLocationIndex": etsysPublishLocationIndex,
       "etsysPublishLocationURL": etsysPublishLocationURL,
       "etsysPublishLocationRowStatus": etsysPublishLocationRowStatus,
       "etsysPublishLocationUserId": etsysPublishLocationUserId,
       "etsysPublishLocationPassword": etsysPublishLocationPassword,
       "etsysLocationBatchReportDimensionUnit": etsysLocationBatchReportDimensionUnit,
       "etsysStationLocationConformance": etsysStationLocationConformance,
       "etsysStationLocationGroups": etsysStationLocationGroups,
       "etsysLocationEngineGlobalGroup": etsysLocationEngineGlobalGroup,
       "etsysFloorGroup": etsysFloorGroup,
       "etsysOnDemandStationsGroup": etsysOnDemandStationsGroup,
       "etsysTrackedStationsGroup": etsysTrackedStationsGroup,
       "etsysLocationBatchReportGroup": etsysLocationBatchReportGroup,
       "etsysLocationEngineGlobalGroup2": etsysLocationEngineGlobalGroup2,
       "etsysLocationEngineGlobalGroup3": etsysLocationEngineGlobalGroup3,
       "etsysLocationBatchReportGroup2": etsysLocationBatchReportGroup2,
       "etsysStationLocationCompliances": etsysStationLocationCompliances,
       "etsysStationLocationCompliance": etsysStationLocationCompliance,
       "etsysStationLocationCompliance2": etsysStationLocationCompliance2,
       "etsysStationLocationCompliance3": etsysStationLocationCompliance3}
)
