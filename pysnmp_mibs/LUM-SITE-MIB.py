# SNMP MIB module (LUM-SITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SITE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:45 2025
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

(AlarmPerceivedSeverity,) = mibBuilder.importSymbols(
    "LUM-ALARM-MIB",
    "AlarmPerceivedSeverity")

(lumModules,
 lumSiteMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSiteMIB")

(AdminStatusWithNA,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 OperStatusWithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "OperStatusWithNA")

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

lumSiteMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 42)
)
if mibBuilder.loadTexts:
    lumSiteMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-12-01 00:00",
         "2011-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSiteConfs_ObjectIdentity = ObjectIdentity
lumSiteConfs = _LumSiteConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1)
)
_LumSiteGroups_ObjectIdentity = ObjectIdentity
lumSiteGroups = _LumSiteGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1)
)
_LumSiteCompl_ObjectIdentity = ObjectIdentity
lumSiteCompl = _LumSiteCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 2)
)
_LumSiteMIBObjects_ObjectIdentity = ObjectIdentity
lumSiteMIBObjects = _LumSiteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2)
)
_SiteGeneral_ObjectIdentity = ObjectIdentity
siteGeneral = _SiteGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 1)
)
_SiteGeneralLastChangeTime_Type = DateAndTime
_SiteGeneralLastChangeTime_Object = MibScalar
siteGeneralLastChangeTime = _SiteGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 1, 1),
    _SiteGeneralLastChangeTime_Type()
)
siteGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGeneralLastChangeTime.setStatus("current")
_SiteGeneralStateLastChangeTime_Type = DateAndTime
_SiteGeneralStateLastChangeTime_Object = MibScalar
siteGeneralStateLastChangeTime = _SiteGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 1, 2),
    _SiteGeneralStateLastChangeTime_Type()
)
siteGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGeneralStateLastChangeTime.setStatus("current")
_SiteGeneralExtAlarmTableSize_Type = Unsigned32
_SiteGeneralExtAlarmTableSize_Object = MibScalar
siteGeneralExtAlarmTableSize = _SiteGeneralExtAlarmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 1, 3),
    _SiteGeneralExtAlarmTableSize_Type()
)
siteGeneralExtAlarmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGeneralExtAlarmTableSize.setStatus("current")
_SiteGeneralExtAlarmOutTableSize_Type = Unsigned32
_SiteGeneralExtAlarmOutTableSize_Object = MibScalar
siteGeneralExtAlarmOutTableSize = _SiteGeneralExtAlarmOutTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 1, 4),
    _SiteGeneralExtAlarmOutTableSize_Type()
)
siteGeneralExtAlarmOutTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGeneralExtAlarmOutTableSize.setStatus("current")
_SiteExtAlarmList_ObjectIdentity = ObjectIdentity
siteExtAlarmList = _SiteExtAlarmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2)
)
_SiteExtAlarmTable_Object = MibTable
siteExtAlarmTable = _SiteExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    siteExtAlarmTable.setStatus("current")
_SiteExtAlarmEntry_Object = MibTableRow
siteExtAlarmEntry = _SiteExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1)
)
siteExtAlarmEntry.setIndexNames(
    (0, "LUM-SITE-MIB", "siteExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    siteExtAlarmEntry.setStatus("current")


class _SiteExtAlarmIndex_Type(Unsigned32):
    """Custom type siteExtAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SiteExtAlarmIndex_Type.__name__ = "Unsigned32"
_SiteExtAlarmIndex_Object = MibTableColumn
siteExtAlarmIndex = _SiteExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 1),
    _SiteExtAlarmIndex_Type()
)
siteExtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmIndex.setStatus("current")


class _SiteExtAlarmName_Type(DisplayString):
    """Custom type siteExtAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SiteExtAlarmName_Type.__name__ = "DisplayString"
_SiteExtAlarmName_Object = MibTableColumn
siteExtAlarmName = _SiteExtAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 2),
    _SiteExtAlarmName_Type()
)
siteExtAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmName.setStatus("current")


class _SiteExtAlarmAdminStatus_Type(Integer32):
    """Custom type siteExtAlarmAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_SiteExtAlarmAdminStatus_Type.__name__ = "Integer32"
_SiteExtAlarmAdminStatus_Object = MibTableColumn
siteExtAlarmAdminStatus = _SiteExtAlarmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 3),
    _SiteExtAlarmAdminStatus_Type()
)
siteExtAlarmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmAdminStatus.setStatus("current")


class _SiteExtAlarmLevel_Type(Integer32):
    """Custom type siteExtAlarmLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2))
    )


_SiteExtAlarmLevel_Type.__name__ = "Integer32"
_SiteExtAlarmLevel_Object = MibTableColumn
siteExtAlarmLevel = _SiteExtAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 4),
    _SiteExtAlarmLevel_Type()
)
siteExtAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmLevel.setStatus("current")


class _SiteExtAlarmSeverity_Type(AlarmPerceivedSeverity):
    """Custom type siteExtAlarmSeverity based on AlarmPerceivedSeverity"""
    defaultValue = 3


_SiteExtAlarmSeverity_Type.__name__ = "AlarmPerceivedSeverity"
_SiteExtAlarmSeverity_Object = MibTableColumn
siteExtAlarmSeverity = _SiteExtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 5),
    _SiteExtAlarmSeverity_Type()
)
siteExtAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmSeverity.setStatus("current")


class _SiteExtAlarmText_Type(DisplayString):
    """Custom type siteExtAlarmText based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SiteExtAlarmText_Type.__name__ = "DisplayString"
_SiteExtAlarmText_Object = MibTableColumn
siteExtAlarmText = _SiteExtAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 6),
    _SiteExtAlarmText_Type()
)
siteExtAlarmText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmText.setStatus("current")
_SiteExtAlarmActive_Type = FaultStatus
_SiteExtAlarmActive_Object = MibTableColumn
siteExtAlarmActive = _SiteExtAlarmActive_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 7),
    _SiteExtAlarmActive_Type()
)
siteExtAlarmActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmActive.setStatus("current")


class _SiteExtAlarmId_Type(Unsigned32):
    """Custom type siteExtAlarmId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SiteExtAlarmId_Type.__name__ = "Unsigned32"
_SiteExtAlarmId_Object = MibTableColumn
siteExtAlarmId = _SiteExtAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 8),
    _SiteExtAlarmId_Type()
)
siteExtAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmId.setStatus("current")
_SiteExtAlarmOperStatus_Type = BoardOrInterfaceOperStatus
_SiteExtAlarmOperStatus_Object = MibTableColumn
siteExtAlarmOperStatus = _SiteExtAlarmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 2, 1, 1, 9),
    _SiteExtAlarmOperStatus_Type()
)
siteExtAlarmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOperStatus.setStatus("current")
_SiteExtAlarmOutList_ObjectIdentity = ObjectIdentity
siteExtAlarmOutList = _SiteExtAlarmOutList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3)
)
_SiteExtAlarmOutTable_Object = MibTable
siteExtAlarmOutTable = _SiteExtAlarmOutTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1)
)
if mibBuilder.loadTexts:
    siteExtAlarmOutTable.setStatus("current")
_SiteExtAlarmOutEntry_Object = MibTableRow
siteExtAlarmOutEntry = _SiteExtAlarmOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1)
)
siteExtAlarmOutEntry.setIndexNames(
    (0, "LUM-SITE-MIB", "siteExtAlarmOutIndex"),
)
if mibBuilder.loadTexts:
    siteExtAlarmOutEntry.setStatus("current")


class _SiteExtAlarmOutIndex_Type(Unsigned32):
    """Custom type siteExtAlarmOutIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SiteExtAlarmOutIndex_Type.__name__ = "Unsigned32"
_SiteExtAlarmOutIndex_Object = MibTableColumn
siteExtAlarmOutIndex = _SiteExtAlarmOutIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 1),
    _SiteExtAlarmOutIndex_Type()
)
siteExtAlarmOutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOutIndex.setStatus("current")


class _SiteExtAlarmOutName_Type(DisplayString):
    """Custom type siteExtAlarmOutName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SiteExtAlarmOutName_Type.__name__ = "DisplayString"
_SiteExtAlarmOutName_Object = MibTableColumn
siteExtAlarmOutName = _SiteExtAlarmOutName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 2),
    _SiteExtAlarmOutName_Type()
)
siteExtAlarmOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOutName.setStatus("current")


class _SiteExtAlarmOutAdminStatus_Type(AdminStatusWithNA):
    """Custom type siteExtAlarmOutAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_SiteExtAlarmOutAdminStatus_Type.__name__ = "AdminStatusWithNA"
_SiteExtAlarmOutAdminStatus_Object = MibTableColumn
siteExtAlarmOutAdminStatus = _SiteExtAlarmOutAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 3),
    _SiteExtAlarmOutAdminStatus_Type()
)
siteExtAlarmOutAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmOutAdminStatus.setStatus("current")
_SiteExtAlarmOutOperStatus_Type = OperStatusWithNA
_SiteExtAlarmOutOperStatus_Object = MibTableColumn
siteExtAlarmOutOperStatus = _SiteExtAlarmOutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 4),
    _SiteExtAlarmOutOperStatus_Type()
)
siteExtAlarmOutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOutOperStatus.setStatus("current")


class _SiteExtAlarmOutLevel_Type(Integer32):
    """Custom type siteExtAlarmOutLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2))
    )


_SiteExtAlarmOutLevel_Type.__name__ = "Integer32"
_SiteExtAlarmOutLevel_Object = MibTableColumn
siteExtAlarmOutLevel = _SiteExtAlarmOutLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 5),
    _SiteExtAlarmOutLevel_Type()
)
siteExtAlarmOutLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmOutLevel.setStatus("current")


class _SiteExtAlarmOutSeverity_Type(AlarmPerceivedSeverity):
    """Custom type siteExtAlarmOutSeverity based on AlarmPerceivedSeverity"""
    defaultValue = 3


_SiteExtAlarmOutSeverity_Type.__name__ = "AlarmPerceivedSeverity"
_SiteExtAlarmOutSeverity_Object = MibTableColumn
siteExtAlarmOutSeverity = _SiteExtAlarmOutSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 6),
    _SiteExtAlarmOutSeverity_Type()
)
siteExtAlarmOutSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmOutSeverity.setStatus("current")


class _SiteExtAlarmOutText_Type(DisplayString):
    """Custom type siteExtAlarmOutText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SiteExtAlarmOutText_Type.__name__ = "DisplayString"
_SiteExtAlarmOutText_Object = MibTableColumn
siteExtAlarmOutText = _SiteExtAlarmOutText_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 7),
    _SiteExtAlarmOutText_Type()
)
siteExtAlarmOutText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteExtAlarmOutText.setStatus("current")
_SiteExtAlarmOutActive_Type = FaultStatus
_SiteExtAlarmOutActive_Object = MibTableColumn
siteExtAlarmOutActive = _SiteExtAlarmOutActive_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 8),
    _SiteExtAlarmOutActive_Type()
)
siteExtAlarmOutActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOutActive.setStatus("current")


class _SiteExtAlarmOutId_Type(Unsigned32):
    """Custom type siteExtAlarmOutId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SiteExtAlarmOutId_Type.__name__ = "Unsigned32"
_SiteExtAlarmOutId_Object = MibTableColumn
siteExtAlarmOutId = _SiteExtAlarmOutId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 2, 3, 1, 1, 9),
    _SiteExtAlarmOutId_Type()
)
siteExtAlarmOutId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteExtAlarmOutId.setStatus("current")

# Managed Objects groups

siteGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1, 1)
)
siteGeneralGroupV1.setObjects(
      *(("LUM-SITE-MIB", "siteGeneralLastChangeTime"),
        ("LUM-SITE-MIB", "siteGeneralStateLastChangeTime"),
        ("LUM-SITE-MIB", "siteGeneralExtAlarmTableSize"))
)
if mibBuilder.loadTexts:
    siteGeneralGroupV1.setStatus("deprecated")

siteGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1, 2)
)
siteGeneralGroupV2.setObjects(
      *(("LUM-SITE-MIB", "siteGeneralLastChangeTime"),
        ("LUM-SITE-MIB", "siteGeneralStateLastChangeTime"),
        ("LUM-SITE-MIB", "siteGeneralExtAlarmTableSize"),
        ("LUM-SITE-MIB", "siteGeneralExtAlarmOutTableSize"))
)
if mibBuilder.loadTexts:
    siteGeneralGroupV2.setStatus("current")

siteExtAlarmGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1, 3)
)
siteExtAlarmGroupV1.setObjects(
      *(("LUM-SITE-MIB", "siteExtAlarmIndex"),
        ("LUM-SITE-MIB", "siteExtAlarmName"),
        ("LUM-SITE-MIB", "siteExtAlarmAdminStatus"),
        ("LUM-SITE-MIB", "siteExtAlarmLevel"),
        ("LUM-SITE-MIB", "siteExtAlarmSeverity"),
        ("LUM-SITE-MIB", "siteExtAlarmText"),
        ("LUM-SITE-MIB", "siteExtAlarmActive"))
)
if mibBuilder.loadTexts:
    siteExtAlarmGroupV1.setStatus("deprecated")

siteExtAlarmGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1, 4)
)
siteExtAlarmGroupV2.setObjects(
      *(("LUM-SITE-MIB", "siteExtAlarmIndex"),
        ("LUM-SITE-MIB", "siteExtAlarmName"),
        ("LUM-SITE-MIB", "siteExtAlarmAdminStatus"),
        ("LUM-SITE-MIB", "siteExtAlarmLevel"),
        ("LUM-SITE-MIB", "siteExtAlarmSeverity"),
        ("LUM-SITE-MIB", "siteExtAlarmText"),
        ("LUM-SITE-MIB", "siteExtAlarmActive"),
        ("LUM-SITE-MIB", "siteExtAlarmId"),
        ("LUM-SITE-MIB", "siteExtAlarmOperStatus"))
)
if mibBuilder.loadTexts:
    siteExtAlarmGroupV2.setStatus("current")

siteExtAlarmOutGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 1, 5)
)
siteExtAlarmOutGroupV1.setObjects(
      *(("LUM-SITE-MIB", "siteExtAlarmIndex"),
        ("LUM-SITE-MIB", "siteExtAlarmName"),
        ("LUM-SITE-MIB", "siteExtAlarmAdminStatus"),
        ("LUM-SITE-MIB", "siteExtAlarmOperStatus"),
        ("LUM-SITE-MIB", "siteExtAlarmLevel"),
        ("LUM-SITE-MIB", "siteExtAlarmSeverity"),
        ("LUM-SITE-MIB", "siteExtAlarmText"),
        ("LUM-SITE-MIB", "siteExtAlarmActive"),
        ("LUM-SITE-MIB", "siteExtAlarmId"))
)
if mibBuilder.loadTexts:
    siteExtAlarmOutGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSiteBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 2, 1)
)
lumSiteBasicComplV1.setObjects(
      *(("LUM-SITE-MIB", "siteGeneralGroupV1"),
        ("LUM-SITE-MIB", "siteExtAlarmGroupV1"))
)
if mibBuilder.loadTexts:
    lumSiteBasicComplV1.setStatus(
        "deprecated"
    )

lumSiteBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 2, 2)
)
lumSiteBasicComplV2.setObjects(
      *(("LUM-SITE-MIB", "siteGeneralGroupV1"),
        ("LUM-SITE-MIB", "siteExtAlarmGroupV2"))
)
if mibBuilder.loadTexts:
    lumSiteBasicComplV2.setStatus(
        "deprecated"
    )

lumSiteBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 42, 1, 2, 3)
)
lumSiteBasicComplV3.setObjects(
      *(("LUM-SITE-MIB", "siteGeneralGroupV2"),
        ("LUM-SITE-MIB", "siteExtAlarmGroupV2"),
        ("LUM-SITE-MIB", "siteExtAlarmOutGroupV1"))
)
if mibBuilder.loadTexts:
    lumSiteBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SITE-MIB",
    **{"lumSiteMIBModule": lumSiteMIBModule,
       "lumSiteConfs": lumSiteConfs,
       "lumSiteGroups": lumSiteGroups,
       "siteGeneralGroupV1": siteGeneralGroupV1,
       "siteGeneralGroupV2": siteGeneralGroupV2,
       "siteExtAlarmGroupV1": siteExtAlarmGroupV1,
       "siteExtAlarmGroupV2": siteExtAlarmGroupV2,
       "siteExtAlarmOutGroupV1": siteExtAlarmOutGroupV1,
       "lumSiteCompl": lumSiteCompl,
       "lumSiteBasicComplV1": lumSiteBasicComplV1,
       "lumSiteBasicComplV2": lumSiteBasicComplV2,
       "lumSiteBasicComplV3": lumSiteBasicComplV3,
       "lumSiteMIBObjects": lumSiteMIBObjects,
       "siteGeneral": siteGeneral,
       "siteGeneralLastChangeTime": siteGeneralLastChangeTime,
       "siteGeneralStateLastChangeTime": siteGeneralStateLastChangeTime,
       "siteGeneralExtAlarmTableSize": siteGeneralExtAlarmTableSize,
       "siteGeneralExtAlarmOutTableSize": siteGeneralExtAlarmOutTableSize,
       "siteExtAlarmList": siteExtAlarmList,
       "siteExtAlarmTable": siteExtAlarmTable,
       "siteExtAlarmEntry": siteExtAlarmEntry,
       "siteExtAlarmIndex": siteExtAlarmIndex,
       "siteExtAlarmName": siteExtAlarmName,
       "siteExtAlarmAdminStatus": siteExtAlarmAdminStatus,
       "siteExtAlarmLevel": siteExtAlarmLevel,
       "siteExtAlarmSeverity": siteExtAlarmSeverity,
       "siteExtAlarmText": siteExtAlarmText,
       "siteExtAlarmActive": siteExtAlarmActive,
       "siteExtAlarmId": siteExtAlarmId,
       "siteExtAlarmOperStatus": siteExtAlarmOperStatus,
       "siteExtAlarmOutList": siteExtAlarmOutList,
       "siteExtAlarmOutTable": siteExtAlarmOutTable,
       "siteExtAlarmOutEntry": siteExtAlarmOutEntry,
       "siteExtAlarmOutIndex": siteExtAlarmOutIndex,
       "siteExtAlarmOutName": siteExtAlarmOutName,
       "siteExtAlarmOutAdminStatus": siteExtAlarmOutAdminStatus,
       "siteExtAlarmOutOperStatus": siteExtAlarmOutOperStatus,
       "siteExtAlarmOutLevel": siteExtAlarmOutLevel,
       "siteExtAlarmOutSeverity": siteExtAlarmOutSeverity,
       "siteExtAlarmOutText": siteExtAlarmOutText,
       "siteExtAlarmOutActive": siteExtAlarmOutActive,
       "siteExtAlarmOutId": siteExtAlarmOutId}
)
