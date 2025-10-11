# SNMP MIB module (ADTRAN-GENCHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENCHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:50 2025
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

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(AdProductIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdProductIdentifier")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenericShelves = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenChassis_ObjectIdentity = ObjectIdentity
adGenChassis = _AdGenChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1)
)
_AdGenChassisScalars_ObjectIdentity = ObjectIdentity
adGenChassisScalars = _AdGenChassisScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1)
)
_AdGenChassisProduct_Type = AdProductIdentifier
_AdGenChassisProduct_Object = MibScalar
adGenChassisProduct = _AdGenChassisProduct_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 1),
    _AdGenChassisProduct_Type()
)
adGenChassisProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisProduct.setStatus("current")


class _AdGenChassisDate_Type(DisplayString):
    """Custom type adGenChassisDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_AdGenChassisDate_Type.__name__ = "DisplayString"
_AdGenChassisDate_Object = MibScalar
adGenChassisDate = _AdGenChassisDate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 5),
    _AdGenChassisDate_Type()
)
adGenChassisDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenChassisDate.setStatus("current")


class _AdGenChassisTime_Type(DisplayString):
    """Custom type adGenChassisTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdGenChassisTime_Type.__name__ = "DisplayString"
_AdGenChassisTime_Object = MibScalar
adGenChassisTime = _AdGenChassisTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 6),
    _AdGenChassisTime_Type()
)
adGenChassisTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenChassisTime.setStatus("current")
_AdGenChassisTftpAddr_Type = IpAddress
_AdGenChassisTftpAddr_Object = MibScalar
adGenChassisTftpAddr = _AdGenChassisTftpAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 7),
    _AdGenChassisTftpAddr_Type()
)
adGenChassisTftpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenChassisTftpAddr.setStatus("current")
_AdGenChassisAlarmStatus_Type = OctetString
_AdGenChassisAlarmStatus_Object = MibScalar
adGenChassisAlarmStatus = _AdGenChassisAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 9),
    _AdGenChassisAlarmStatus_Type()
)
adGenChassisAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisAlarmStatus.setStatus("current")
_AdGenChassisProvVersion_Type = Integer32
_AdGenChassisProvVersion_Object = MibScalar
adGenChassisProvVersion = _AdGenChassisProvVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 10),
    _AdGenChassisProvVersion_Type()
)
adGenChassisProvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisProvVersion.setStatus("current")


class _AdGenChassisActiveMux_Type(Integer32):
    """Custom type adGenChassisActiveMux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenChassisActiveMux_Type.__name__ = "Integer32"
_AdGenChassisActiveMux_Object = MibScalar
adGenChassisActiveMux = _AdGenChassisActiveMux_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 11),
    _AdGenChassisActiveMux_Type()
)
adGenChassisActiveMux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisActiveMux.setStatus("current")
_AdGenChassisViewAll_Type = OctetString
_AdGenChassisViewAll_Object = MibScalar
adGenChassisViewAll = _AdGenChassisViewAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 1, 12),
    _AdGenChassisViewAll_Type()
)
adGenChassisViewAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisViewAll.setStatus("current")
_AdGenChassisTables_ObjectIdentity = ObjectIdentity
adGenChassisTables = _AdGenChassisTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 2)
)
_AdGenChassisViewTable_Object = MibTable
adGenChassisViewTable = _AdGenChassisViewTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenChassisViewTable.setStatus("current")
_AdGenChassisViewEntry_Object = MibTableRow
adGenChassisViewEntry = _AdGenChassisViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 2, 1, 1)
)
adGenChassisViewEntry.setIndexNames(
    (0, "ADTRAN-GENCHASSIS-MIB", "adGenChassisViewIndex"),
)
if mibBuilder.loadTexts:
    adGenChassisViewEntry.setStatus("current")


class _AdGenChassisViewIndex_Type(Integer32):
    """Custom type adGenChassisViewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenChassisViewIndex_Type.__name__ = "Integer32"
_AdGenChassisViewIndex_Object = MibTableColumn
adGenChassisViewIndex = _AdGenChassisViewIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 2, 1, 1, 1),
    _AdGenChassisViewIndex_Type()
)
adGenChassisViewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisViewIndex.setStatus("current")
_AdGenChassisFaceplates_Type = OctetString
_AdGenChassisFaceplates_Object = MibTableColumn
adGenChassisFaceplates = _AdGenChassisFaceplates_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 1, 2, 1, 1, 2),
    _AdGenChassisFaceplates_Type()
)
adGenChassisFaceplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenChassisFaceplates.setStatus("current")
_AdGenChassisConformance_ObjectIdentity = ObjectIdentity
adGenChassisConformance = _AdGenChassisConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99)
)
_AdGenChassisCompliances_ObjectIdentity = ObjectIdentity
adGenChassisCompliances = _AdGenChassisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99, 1)
)
_AdGenChassisMIBGroups_ObjectIdentity = ObjectIdentity
adGenChassisMIBGroups = _AdGenChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99, 2)
)

# Managed Objects groups

adGenChassisBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99, 2, 1)
)
adGenChassisBaseGroup.setObjects(
      *(("ADTRAN-GENCHASSIS-MIB", "adGenChassisProduct"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisDate"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisTime"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisTftpAddr"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisAlarmStatus"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisProvVersion"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisActiveMux"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisViewIndex"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisFaceplates"))
)
if mibBuilder.loadTexts:
    adGenChassisBaseGroup.setStatus("current")

adGenChassisOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99, 2, 2)
)
adGenChassisOptionalGroup.setObjects(
    ("ADTRAN-GENCHASSIS-MIB", "adGenChassisViewAll")
)
if mibBuilder.loadTexts:
    adGenChassisOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenChassisCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 99, 1, 1)
)
adGenChassisCompliance.setObjects(
      *(("ADTRAN-GENCHASSIS-MIB", "adGenChassisBaseGroup"),
        ("ADTRAN-GENCHASSIS-MIB", "adGenChassisOptionalGroup"))
)
if mibBuilder.loadTexts:
    adGenChassisCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENCHASSIS-MIB",
    **{"adGenericShelves": adGenericShelves,
       "adGenChassis": adGenChassis,
       "adGenChassisScalars": adGenChassisScalars,
       "adGenChassisProduct": adGenChassisProduct,
       "adGenChassisDate": adGenChassisDate,
       "adGenChassisTime": adGenChassisTime,
       "adGenChassisTftpAddr": adGenChassisTftpAddr,
       "adGenChassisAlarmStatus": adGenChassisAlarmStatus,
       "adGenChassisProvVersion": adGenChassisProvVersion,
       "adGenChassisActiveMux": adGenChassisActiveMux,
       "adGenChassisViewAll": adGenChassisViewAll,
       "adGenChassisTables": adGenChassisTables,
       "adGenChassisViewTable": adGenChassisViewTable,
       "adGenChassisViewEntry": adGenChassisViewEntry,
       "adGenChassisViewIndex": adGenChassisViewIndex,
       "adGenChassisFaceplates": adGenChassisFaceplates,
       "adGenChassisConformance": adGenChassisConformance,
       "adGenChassisCompliances": adGenChassisCompliances,
       "adGenChassisCompliance": adGenChassisCompliance,
       "adGenChassisMIBGroups": adGenChassisMIBGroups,
       "adGenChassisBaseGroup": adGenChassisBaseGroup,
       "adGenChassisOptionalGroup": adGenChassisOptionalGroup}
)
