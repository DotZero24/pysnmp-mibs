# SNMP MIB module (LUM-SATELLITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SATELLITE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:22 2025
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

(lumModules,
 lumSatelliteMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSatelliteMIB")

(MgmtNameString,) = mibBuilder.importSymbols(
    "LUM-TC",
    "MgmtNameString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumSatelliteMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 36)
)
if mibBuilder.loadTexts:
    lumSatelliteMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2009-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSatelliteConfs_ObjectIdentity = ObjectIdentity
lumSatelliteConfs = _LumSatelliteConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1)
)
_LumSatelliteGroups_ObjectIdentity = ObjectIdentity
lumSatelliteGroups = _LumSatelliteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1)
)
_LumSatelliteCompl_ObjectIdentity = ObjectIdentity
lumSatelliteCompl = _LumSatelliteCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 2)
)
_LumSatelliteMIBObjects_ObjectIdentity = ObjectIdentity
lumSatelliteMIBObjects = _LumSatelliteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2)
)
_SatelliteGeneral_ObjectIdentity = ObjectIdentity
satelliteGeneral = _SatelliteGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1)
)
_SatelliteGeneralLastChangeTime_Type = DateAndTime
_SatelliteGeneralLastChangeTime_Object = MibScalar
satelliteGeneralLastChangeTime = _SatelliteGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 1),
    _SatelliteGeneralLastChangeTime_Type()
)
satelliteGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteGeneralLastChangeTime.setStatus("current")
_SatelliteGeneralStateLastChangeTime_Type = DateAndTime
_SatelliteGeneralStateLastChangeTime_Object = MibScalar
satelliteGeneralStateLastChangeTime = _SatelliteGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 2),
    _SatelliteGeneralStateLastChangeTime_Type()
)
satelliteGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteGeneralStateLastChangeTime.setStatus("current")
_SatelliteGeneralSatelliteTableSize_Type = Unsigned32
_SatelliteGeneralSatelliteTableSize_Object = MibScalar
satelliteGeneralSatelliteTableSize = _SatelliteGeneralSatelliteTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 1, 3),
    _SatelliteGeneralSatelliteTableSize_Type()
)
satelliteGeneralSatelliteTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteGeneralSatelliteTableSize.setStatus("current")
_SatelliteSatelliteList_ObjectIdentity = ObjectIdentity
satelliteSatelliteList = _SatelliteSatelliteList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2)
)
_SatelliteSatelliteTable_Object = MibTable
satelliteSatelliteTable = _SatelliteSatelliteTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1)
)
if mibBuilder.loadTexts:
    satelliteSatelliteTable.setStatus("current")
_SatelliteSatelliteEntry_Object = MibTableRow
satelliteSatelliteEntry = _SatelliteSatelliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1)
)
satelliteSatelliteEntry.setIndexNames(
    (0, "LUM-SATELLITE-MIB", "satelliteSatelliteIndex"),
)
if mibBuilder.loadTexts:
    satelliteSatelliteEntry.setStatus("current")


class _SatelliteSatelliteIndex_Type(Unsigned32):
    """Custom type satelliteSatelliteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SatelliteSatelliteIndex_Type.__name__ = "Unsigned32"
_SatelliteSatelliteIndex_Object = MibTableColumn
satelliteSatelliteIndex = _SatelliteSatelliteIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 1),
    _SatelliteSatelliteIndex_Type()
)
satelliteSatelliteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSatelliteIndex.setStatus("current")


class _SatelliteSatelliteName_Type(MgmtNameString):
    """Custom type satelliteSatelliteName based on MgmtNameString"""
    defaultValue = OctetString("")


_SatelliteSatelliteName_Type.__name__ = "MgmtNameString"
_SatelliteSatelliteName_Object = MibTableColumn
satelliteSatelliteName = _SatelliteSatelliteName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 2),
    _SatelliteSatelliteName_Type()
)
satelliteSatelliteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satelliteSatelliteName.setStatus("current")


class _SatelliteSatelliteDescr_Type(DisplayString):
    """Custom type satelliteSatelliteDescr based on DisplayString"""
    defaultValue = OctetString("")


_SatelliteSatelliteDescr_Type.__name__ = "DisplayString"
_SatelliteSatelliteDescr_Object = MibTableColumn
satelliteSatelliteDescr = _SatelliteSatelliteDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 3),
    _SatelliteSatelliteDescr_Type()
)
satelliteSatelliteDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satelliteSatelliteDescr.setStatus("current")


class _SatelliteSatelliteExpectedBoardType_Type(Integer32):
    """Custom type satelliteSatelliteExpectedBoardType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mba1", 1),
          ("mba2", 2))
    )


_SatelliteSatelliteExpectedBoardType_Type.__name__ = "Integer32"
_SatelliteSatelliteExpectedBoardType_Object = MibTableColumn
satelliteSatelliteExpectedBoardType = _SatelliteSatelliteExpectedBoardType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 2, 2, 1, 1, 4),
    _SatelliteSatelliteExpectedBoardType_Type()
)
satelliteSatelliteExpectedBoardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    satelliteSatelliteExpectedBoardType.setStatus("current")

# Managed Objects groups

satelliteGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1, 1)
)
satelliteGeneralGroup.setObjects(
      *(("LUM-SATELLITE-MIB", "satelliteGeneralLastChangeTime"),
        ("LUM-SATELLITE-MIB", "satelliteGeneralStateLastChangeTime"),
        ("LUM-SATELLITE-MIB", "satelliteGeneralSatelliteTableSize"))
)
if mibBuilder.loadTexts:
    satelliteGeneralGroup.setStatus("current")

satelliteSatelliteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 1, 2)
)
satelliteSatelliteGroup.setObjects(
      *(("LUM-SATELLITE-MIB", "satelliteSatelliteIndex"),
        ("LUM-SATELLITE-MIB", "satelliteSatelliteName"),
        ("LUM-SATELLITE-MIB", "satelliteSatelliteDescr"),
        ("LUM-SATELLITE-MIB", "satelliteSatelliteExpectedBoardType"))
)
if mibBuilder.loadTexts:
    satelliteSatelliteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSatelliteBasicCompl1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 36, 1, 2, 1)
)
lumSatelliteBasicCompl1.setObjects(
      *(("LUM-SATELLITE-MIB", "satelliteGeneralGroup"),
        ("LUM-SATELLITE-MIB", "satelliteSatelliteGroup"))
)
if mibBuilder.loadTexts:
    lumSatelliteBasicCompl1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SATELLITE-MIB",
    **{"lumSatelliteMIBModule": lumSatelliteMIBModule,
       "lumSatelliteConfs": lumSatelliteConfs,
       "lumSatelliteGroups": lumSatelliteGroups,
       "satelliteGeneralGroup": satelliteGeneralGroup,
       "satelliteSatelliteGroup": satelliteSatelliteGroup,
       "lumSatelliteCompl": lumSatelliteCompl,
       "lumSatelliteBasicCompl1": lumSatelliteBasicCompl1,
       "lumSatelliteMIBObjects": lumSatelliteMIBObjects,
       "satelliteGeneral": satelliteGeneral,
       "satelliteGeneralLastChangeTime": satelliteGeneralLastChangeTime,
       "satelliteGeneralStateLastChangeTime": satelliteGeneralStateLastChangeTime,
       "satelliteGeneralSatelliteTableSize": satelliteGeneralSatelliteTableSize,
       "satelliteSatelliteList": satelliteSatelliteList,
       "satelliteSatelliteTable": satelliteSatelliteTable,
       "satelliteSatelliteEntry": satelliteSatelliteEntry,
       "satelliteSatelliteIndex": satelliteSatelliteIndex,
       "satelliteSatelliteName": satelliteSatelliteName,
       "satelliteSatelliteDescr": satelliteSatelliteDescr,
       "satelliteSatelliteExpectedBoardType": satelliteSatelliteExpectedBoardType}
)
