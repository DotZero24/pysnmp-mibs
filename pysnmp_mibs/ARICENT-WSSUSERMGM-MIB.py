# SNMP MIB module (ARICENT-WSSUSERMGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-WSSUSERMGM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:34 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsWssUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90)
)
if mibBuilder.loadTexts:
    fsWssUser.setRevisions(
        ("2014-09-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsWssUserStationMac(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )



class FsWssUserIdName(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_FsWssUserScalars_ObjectIdentity = ObjectIdentity
fsWssUserScalars = _FsWssUserScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1)
)


class _FsWssUserRoleStatus_Type(Integer32):
    """Custom type fsWssUserRoleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsWssUserRoleStatus_Type.__name__ = "Integer32"
_FsWssUserRoleStatus_Object = MibScalar
fsWssUserRoleStatus = _FsWssUserRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1, 1),
    _FsWssUserRoleStatus_Type()
)
fsWssUserRoleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserRoleStatus.setStatus("current")


class _FsWssUserBlockedCount_Type(Unsigned32):
    """Custom type fsWssUserBlockedCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserBlockedCount_Type.__name__ = "Unsigned32"
_FsWssUserBlockedCount_Object = MibScalar
fsWssUserBlockedCount = _FsWssUserBlockedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1, 2),
    _FsWssUserBlockedCount_Type()
)
fsWssUserBlockedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserBlockedCount.setStatus("current")


class _FsWssUserLoggedCount_Type(Unsigned32):
    """Custom type fsWssUserLoggedCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserLoggedCount_Type.__name__ = "Unsigned32"
_FsWssUserLoggedCount_Object = MibScalar
fsWssUserLoggedCount = _FsWssUserLoggedCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1, 3),
    _FsWssUserLoggedCount_Type()
)
fsWssUserLoggedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserLoggedCount.setStatus("current")


class _FsWssUserTraceOption_Type(Integer32):
    """Custom type fsWssUserTraceOption based on Integer32"""
    defaultValue = 0


_FsWssUserTraceOption_Type.__name__ = "Integer32"
_FsWssUserTraceOption_Object = MibScalar
fsWssUserTraceOption = _FsWssUserTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1, 4),
    _FsWssUserTraceOption_Type()
)
fsWssUserTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserTraceOption.setStatus("current")


class _FsWssUserRoleTrapStatus_Type(Integer32):
    """Custom type fsWssUserRoleTrapStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsWssUserRoleTrapStatus_Type.__name__ = "Integer32"
_FsWssUserRoleTrapStatus_Object = MibScalar
fsWssUserRoleTrapStatus = _FsWssUserRoleTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 1, 5),
    _FsWssUserRoleTrapStatus_Type()
)
fsWssUserRoleTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserRoleTrapStatus.setStatus("current")
_FsWssUserRole_ObjectIdentity = ObjectIdentity
fsWssUserRole = _FsWssUserRole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2)
)
_FsWssUserGroupTable_Object = MibTable
fsWssUserGroupTable = _FsWssUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1)
)
if mibBuilder.loadTexts:
    fsWssUserGroupTable.setStatus("current")
_FsWssUserGroupEntry_Object = MibTableRow
fsWssUserGroupEntry = _FsWssUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1)
)
fsWssUserGroupEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserGroupId"),
)
if mibBuilder.loadTexts:
    fsWssUserGroupEntry.setStatus("current")


class _FsWssUserGroupId_Type(Unsigned32):
    """Custom type fsWssUserGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsWssUserGroupId_Type.__name__ = "Unsigned32"
_FsWssUserGroupId_Object = MibTableColumn
fsWssUserGroupId = _FsWssUserGroupId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 1),
    _FsWssUserGroupId_Type()
)
fsWssUserGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserGroupId.setStatus("current")
_FsWssUserGroupName_Type = OctetString
_FsWssUserGroupName_Object = MibTableColumn
fsWssUserGroupName = _FsWssUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 2),
    _FsWssUserGroupName_Type()
)
fsWssUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupName.setStatus("current")


class _FsWssUserGroupBandWidth_Type(Unsigned32):
    """Custom type fsWssUserGroupBandWidth based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserGroupBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserGroupBandWidth_Object = MibTableColumn
fsWssUserGroupBandWidth = _FsWssUserGroupBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 3),
    _FsWssUserGroupBandWidth_Type()
)
fsWssUserGroupBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupBandWidth.setStatus("current")


class _FsWssUserGroupVolume_Type(Unsigned32):
    """Custom type fsWssUserGroupVolume based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserGroupVolume_Type.__name__ = "Unsigned32"
_FsWssUserGroupVolume_Object = MibTableColumn
fsWssUserGroupVolume = _FsWssUserGroupVolume_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 4),
    _FsWssUserGroupVolume_Type()
)
fsWssUserGroupVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupVolume.setStatus("current")


class _FsWssUserGroupTime_Type(Unsigned32):
    """Custom type fsWssUserGroupTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_FsWssUserGroupTime_Type.__name__ = "Unsigned32"
_FsWssUserGroupTime_Object = MibTableColumn
fsWssUserGroupTime = _FsWssUserGroupTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 5),
    _FsWssUserGroupTime_Type()
)
fsWssUserGroupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupTime.setStatus("current")
_FsWssUserGroupRowStatus_Type = RowStatus
_FsWssUserGroupRowStatus_Object = MibTableColumn
fsWssUserGroupRowStatus = _FsWssUserGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 6),
    _FsWssUserGroupRowStatus_Type()
)
fsWssUserGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWssUserGroupRowStatus.setStatus("current")


class _FsWssUserGroupDLBandWidth_Type(Unsigned32):
    """Custom type fsWssUserGroupDLBandWidth based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserGroupDLBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserGroupDLBandWidth_Object = MibTableColumn
fsWssUserGroupDLBandWidth = _FsWssUserGroupDLBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 7),
    _FsWssUserGroupDLBandWidth_Type()
)
fsWssUserGroupDLBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupDLBandWidth.setStatus("current")


class _FsWssUserGroupULBandWidth_Type(Unsigned32):
    """Custom type fsWssUserGroupULBandWidth based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserGroupULBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserGroupULBandWidth_Object = MibTableColumn
fsWssUserGroupULBandWidth = _FsWssUserGroupULBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 1, 1, 8),
    _FsWssUserGroupULBandWidth_Type()
)
fsWssUserGroupULBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserGroupULBandWidth.setStatus("current")
_FsWssUserRoleTable_Object = MibTable
fsWssUserRoleTable = _FsWssUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2)
)
if mibBuilder.loadTexts:
    fsWssUserRoleTable.setStatus("current")
_FsWssUserRoleEntry_Object = MibTableRow
fsWssUserRoleEntry = _FsWssUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2, 1)
)
fsWssUserRoleEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserRoleName"),
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserRoleWlanIndex"),
)
if mibBuilder.loadTexts:
    fsWssUserRoleEntry.setStatus("current")


class _FsWssUserRoleName_Type(OctetString):
    """Custom type fsWssUserRoleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsWssUserRoleName_Type.__name__ = "OctetString"
_FsWssUserRoleName_Object = MibTableColumn
fsWssUserRoleName = _FsWssUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2, 1, 1),
    _FsWssUserRoleName_Type()
)
fsWssUserRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserRoleName.setStatus("current")


class _FsWssUserRoleWlanIndex_Type(Unsigned32):
    """Custom type fsWssUserRoleWlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_FsWssUserRoleWlanIndex_Type.__name__ = "Unsigned32"
_FsWssUserRoleWlanIndex_Object = MibTableColumn
fsWssUserRoleWlanIndex = _FsWssUserRoleWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2, 1, 2),
    _FsWssUserRoleWlanIndex_Type()
)
fsWssUserRoleWlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserRoleWlanIndex.setStatus("current")


class _FsWssUserRoleGroupId_Type(Unsigned32):
    """Custom type fsWssUserRoleGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_FsWssUserRoleGroupId_Type.__name__ = "Unsigned32"
_FsWssUserRoleGroupId_Object = MibTableColumn
fsWssUserRoleGroupId = _FsWssUserRoleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2, 1, 3),
    _FsWssUserRoleGroupId_Type()
)
fsWssUserRoleGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWssUserRoleGroupId.setStatus("current")
_FsWssUserRoleRowStatus_Type = RowStatus
_FsWssUserRoleRowStatus_Object = MibTableColumn
fsWssUserRoleRowStatus = _FsWssUserRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 2, 1, 4),
    _FsWssUserRoleRowStatus_Type()
)
fsWssUserRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWssUserRoleRowStatus.setStatus("current")
_FsWssUserNameAccessListTable_Object = MibTable
fsWssUserNameAccessListTable = _FsWssUserNameAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 3)
)
if mibBuilder.loadTexts:
    fsWssUserNameAccessListTable.setStatus("current")
_FsWssUserNameAccessListEntry_Object = MibTableRow
fsWssUserNameAccessListEntry = _FsWssUserNameAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 3, 1)
)
fsWssUserNameAccessListEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserNameAccessListUserName"),
)
if mibBuilder.loadTexts:
    fsWssUserNameAccessListEntry.setStatus("current")


class _FsWssUserNameAccessListUserName_Type(OctetString):
    """Custom type fsWssUserNameAccessListUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsWssUserNameAccessListUserName_Type.__name__ = "OctetString"
_FsWssUserNameAccessListUserName_Object = MibTableColumn
fsWssUserNameAccessListUserName = _FsWssUserNameAccessListUserName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 3, 1, 1),
    _FsWssUserNameAccessListUserName_Type()
)
fsWssUserNameAccessListUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserNameAccessListUserName.setStatus("current")
_FsWssUserNameAccessListRowStatus_Type = RowStatus
_FsWssUserNameAccessListRowStatus_Object = MibTableColumn
fsWssUserNameAccessListRowStatus = _FsWssUserNameAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 3, 1, 2),
    _FsWssUserNameAccessListRowStatus_Type()
)
fsWssUserNameAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWssUserNameAccessListRowStatus.setStatus("current")
_FsWssUserMacAccessListTable_Object = MibTable
fsWssUserMacAccessListTable = _FsWssUserMacAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 4)
)
if mibBuilder.loadTexts:
    fsWssUserMacAccessListTable.setStatus("current")
_FsWssUserMacAccessListEntry_Object = MibTableRow
fsWssUserMacAccessListEntry = _FsWssUserMacAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 4, 1)
)
fsWssUserMacAccessListEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserMacAccessListStaMac"),
)
if mibBuilder.loadTexts:
    fsWssUserMacAccessListEntry.setStatus("current")
_FsWssUserMacAccessListStaMac_Type = MacAddress
_FsWssUserMacAccessListStaMac_Object = MibTableColumn
fsWssUserMacAccessListStaMac = _FsWssUserMacAccessListStaMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 4, 1, 1),
    _FsWssUserMacAccessListStaMac_Type()
)
fsWssUserMacAccessListStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserMacAccessListStaMac.setStatus("current")
_FsWssUserMacAccessListRowStatus_Type = RowStatus
_FsWssUserMacAccessListRowStatus_Object = MibTableColumn
fsWssUserMacAccessListRowStatus = _FsWssUserMacAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 4, 1, 2),
    _FsWssUserMacAccessListRowStatus_Type()
)
fsWssUserMacAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWssUserMacAccessListRowStatus.setStatus("current")
_FsWssUserMappingTable_Object = MibTable
fsWssUserMappingTable = _FsWssUserMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 5)
)
if mibBuilder.loadTexts:
    fsWssUserMappingTable.setStatus("current")
_FsWssUserMappingEntry_Object = MibTableRow
fsWssUserMappingEntry = _FsWssUserMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 5, 1)
)
fsWssUserMappingEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserMappingName"),
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserMappingStaMac"),
)
if mibBuilder.loadTexts:
    fsWssUserMappingEntry.setStatus("current")


class _FsWssUserMappingName_Type(OctetString):
    """Custom type fsWssUserMappingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsWssUserMappingName_Type.__name__ = "OctetString"
_FsWssUserMappingName_Object = MibTableColumn
fsWssUserMappingName = _FsWssUserMappingName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 5, 1, 1),
    _FsWssUserMappingName_Type()
)
fsWssUserMappingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserMappingName.setStatus("current")
_FsWssUserMappingStaMac_Type = MacAddress
_FsWssUserMappingStaMac_Object = MibTableColumn
fsWssUserMappingStaMac = _FsWssUserMappingStaMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 5, 1, 2),
    _FsWssUserMappingStaMac_Type()
)
fsWssUserMappingStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserMappingStaMac.setStatus("current")
_FsWssUserMappingRowStatus_Type = RowStatus
_FsWssUserMappingRowStatus_Object = MibTableColumn
fsWssUserMappingRowStatus = _FsWssUserMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 2, 5, 1, 3),
    _FsWssUserMappingRowStatus_Type()
)
fsWssUserMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWssUserMappingRowStatus.setStatus("current")
_FsWssUserStats_ObjectIdentity = ObjectIdentity
fsWssUserStats = _FsWssUserStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3)
)
_FsWssUserSessionTable_Object = MibTable
fsWssUserSessionTable = _FsWssUserSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1)
)
if mibBuilder.loadTexts:
    fsWssUserSessionTable.setStatus("current")
_FsWssUserSessionEntry_Object = MibTableRow
fsWssUserSessionEntry = _FsWssUserSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1)
)
fsWssUserSessionEntry.setIndexNames(
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserName"),
    (0, "ARICENT-WSSUSERMGM-MIB", "fsWssUserStaMac"),
)
if mibBuilder.loadTexts:
    fsWssUserSessionEntry.setStatus("current")
_FsWssUserName_Type = FsWssUserIdName
_FsWssUserName_Object = MibTableColumn
fsWssUserName = _FsWssUserName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 1),
    _FsWssUserName_Type()
)
fsWssUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserName.setStatus("current")
_FsWssUserStaMac_Type = FsWssUserStationMac
_FsWssUserStaMac_Object = MibTableColumn
fsWssUserStaMac = _FsWssUserStaMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 2),
    _FsWssUserStaMac_Type()
)
fsWssUserStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsWssUserStaMac.setStatus("current")


class _FsWssUserWlanIndex_Type(Unsigned32):
    """Custom type fsWssUserWlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_FsWssUserWlanIndex_Type.__name__ = "Unsigned32"
_FsWssUserWlanIndex_Object = MibTableColumn
fsWssUserWlanIndex = _FsWssUserWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 3),
    _FsWssUserWlanIndex_Type()
)
fsWssUserWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserWlanIndex.setStatus("current")


class _FsWssUserAllotedBandWidth_Type(Unsigned32):
    """Custom type fsWssUserAllotedBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserAllotedBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserAllotedBandWidth_Object = MibTableColumn
fsWssUserAllotedBandWidth = _FsWssUserAllotedBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 4),
    _FsWssUserAllotedBandWidth_Type()
)
fsWssUserAllotedBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserAllotedBandWidth.setStatus("current")


class _FsWssUserAllotedVolume_Type(Unsigned32):
    """Custom type fsWssUserAllotedVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserAllotedVolume_Type.__name__ = "Unsigned32"
_FsWssUserAllotedVolume_Object = MibTableColumn
fsWssUserAllotedVolume = _FsWssUserAllotedVolume_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 5),
    _FsWssUserAllotedVolume_Type()
)
fsWssUserAllotedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserAllotedVolume.setStatus("current")


class _FsWssUserAllotedTime_Type(Unsigned32):
    """Custom type fsWssUserAllotedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_FsWssUserAllotedTime_Type.__name__ = "Unsigned32"
_FsWssUserAllotedTime_Object = MibTableColumn
fsWssUserAllotedTime = _FsWssUserAllotedTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 6),
    _FsWssUserAllotedTime_Type()
)
fsWssUserAllotedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserAllotedTime.setStatus("current")


class _FsWssUserUsedVolume_Type(Unsigned32):
    """Custom type fsWssUserUsedVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserUsedVolume_Type.__name__ = "Unsigned32"
_FsWssUserUsedVolume_Object = MibTableColumn
fsWssUserUsedVolume = _FsWssUserUsedVolume_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 7),
    _FsWssUserUsedVolume_Type()
)
fsWssUserUsedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserUsedVolume.setStatus("current")


class _FsWssUserUsedTime_Type(Unsigned32):
    """Custom type fsWssUserUsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_FsWssUserUsedTime_Type.__name__ = "Unsigned32"
_FsWssUserUsedTime_Object = MibTableColumn
fsWssUserUsedTime = _FsWssUserUsedTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 8),
    _FsWssUserUsedTime_Type()
)
fsWssUserUsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserUsedTime.setStatus("current")


class _FsWssUserAllotedDLBandWidth_Type(Unsigned32):
    """Custom type fsWssUserAllotedDLBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserAllotedDLBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserAllotedDLBandWidth_Object = MibTableColumn
fsWssUserAllotedDLBandWidth = _FsWssUserAllotedDLBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 9),
    _FsWssUserAllotedDLBandWidth_Type()
)
fsWssUserAllotedDLBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserAllotedDLBandWidth.setStatus("current")


class _FsWssUserAllotedULBandWidth_Type(Unsigned32):
    """Custom type fsWssUserAllotedULBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsWssUserAllotedULBandWidth_Type.__name__ = "Unsigned32"
_FsWssUserAllotedULBandWidth_Object = MibTableColumn
fsWssUserAllotedULBandWidth = _FsWssUserAllotedULBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 3, 1, 1, 10),
    _FsWssUserAllotedULBandWidth_Type()
)
fsWssUserAllotedULBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWssUserAllotedULBandWidth.setStatus("current")
_FsWssUserNotifyObjects_ObjectIdentity = ObjectIdentity
fsWssUserNotifyObjects = _FsWssUserNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 4)
)
_FsWssUserTrapObjects_ObjectIdentity = ObjectIdentity
fsWssUserTrapObjects = _FsWssUserTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 4, 1)
)
_FsWssUserStationMacAddress_Type = FsWssUserStationMac
_FsWssUserStationMacAddress_Object = MibScalar
fsWssUserStationMacAddress = _FsWssUserStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 4, 1, 1),
    _FsWssUserStationMacAddress_Type()
)
fsWssUserStationMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWssUserStationMacAddress.setStatus("current")
_FsWssNtfUserName_Type = FsWssUserIdName
_FsWssNtfUserName_Object = MibScalar
fsWssNtfUserName = _FsWssNtfUserName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 4, 1, 2),
    _FsWssNtfUserName_Type()
)
fsWssNtfUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWssNtfUserName.setStatus("current")
_FsWssUserNotifications_ObjectIdentity = ObjectIdentity
fsWssUserNotifications = _FsWssUserNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 5)
)
_FsWssUserTraps_ObjectIdentity = ObjectIdentity
fsWssUserTraps = _FsWssUserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 5, 0)
)

# Managed Objects groups


# Notification objects

fsWssUserVolumeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 5, 0, 1)
)
fsWssUserVolumeExceeded.setObjects(
      *(("ARICENT-WSSUSERMGM-MIB", "fsWssUserWlanIndex"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssNtfUserName"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssUserStationMacAddress"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssUserUsedVolume"))
)
if mibBuilder.loadTexts:
    fsWssUserVolumeExceeded.setStatus(
        "current"
    )

fsWssUserTimeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 90, 5, 0, 2)
)
fsWssUserTimeExceeded.setObjects(
      *(("ARICENT-WSSUSERMGM-MIB", "fsWssUserWlanIndex"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssNtfUserName"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssUserStationMacAddress"),
        ("ARICENT-WSSUSERMGM-MIB", "fsWssUserUsedTime"))
)
if mibBuilder.loadTexts:
    fsWssUserTimeExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-WSSUSERMGM-MIB",
    **{"FsWssUserStationMac": FsWssUserStationMac,
       "FsWssUserIdName": FsWssUserIdName,
       "fsWssUser": fsWssUser,
       "fsWssUserScalars": fsWssUserScalars,
       "fsWssUserRoleStatus": fsWssUserRoleStatus,
       "fsWssUserBlockedCount": fsWssUserBlockedCount,
       "fsWssUserLoggedCount": fsWssUserLoggedCount,
       "fsWssUserTraceOption": fsWssUserTraceOption,
       "fsWssUserRoleTrapStatus": fsWssUserRoleTrapStatus,
       "fsWssUserRole": fsWssUserRole,
       "fsWssUserGroupTable": fsWssUserGroupTable,
       "fsWssUserGroupEntry": fsWssUserGroupEntry,
       "fsWssUserGroupId": fsWssUserGroupId,
       "fsWssUserGroupName": fsWssUserGroupName,
       "fsWssUserGroupBandWidth": fsWssUserGroupBandWidth,
       "fsWssUserGroupVolume": fsWssUserGroupVolume,
       "fsWssUserGroupTime": fsWssUserGroupTime,
       "fsWssUserGroupRowStatus": fsWssUserGroupRowStatus,
       "fsWssUserGroupDLBandWidth": fsWssUserGroupDLBandWidth,
       "fsWssUserGroupULBandWidth": fsWssUserGroupULBandWidth,
       "fsWssUserRoleTable": fsWssUserRoleTable,
       "fsWssUserRoleEntry": fsWssUserRoleEntry,
       "fsWssUserRoleName": fsWssUserRoleName,
       "fsWssUserRoleWlanIndex": fsWssUserRoleWlanIndex,
       "fsWssUserRoleGroupId": fsWssUserRoleGroupId,
       "fsWssUserRoleRowStatus": fsWssUserRoleRowStatus,
       "fsWssUserNameAccessListTable": fsWssUserNameAccessListTable,
       "fsWssUserNameAccessListEntry": fsWssUserNameAccessListEntry,
       "fsWssUserNameAccessListUserName": fsWssUserNameAccessListUserName,
       "fsWssUserNameAccessListRowStatus": fsWssUserNameAccessListRowStatus,
       "fsWssUserMacAccessListTable": fsWssUserMacAccessListTable,
       "fsWssUserMacAccessListEntry": fsWssUserMacAccessListEntry,
       "fsWssUserMacAccessListStaMac": fsWssUserMacAccessListStaMac,
       "fsWssUserMacAccessListRowStatus": fsWssUserMacAccessListRowStatus,
       "fsWssUserMappingTable": fsWssUserMappingTable,
       "fsWssUserMappingEntry": fsWssUserMappingEntry,
       "fsWssUserMappingName": fsWssUserMappingName,
       "fsWssUserMappingStaMac": fsWssUserMappingStaMac,
       "fsWssUserMappingRowStatus": fsWssUserMappingRowStatus,
       "fsWssUserStats": fsWssUserStats,
       "fsWssUserSessionTable": fsWssUserSessionTable,
       "fsWssUserSessionEntry": fsWssUserSessionEntry,
       "fsWssUserName": fsWssUserName,
       "fsWssUserStaMac": fsWssUserStaMac,
       "fsWssUserWlanIndex": fsWssUserWlanIndex,
       "fsWssUserAllotedBandWidth": fsWssUserAllotedBandWidth,
       "fsWssUserAllotedVolume": fsWssUserAllotedVolume,
       "fsWssUserAllotedTime": fsWssUserAllotedTime,
       "fsWssUserUsedVolume": fsWssUserUsedVolume,
       "fsWssUserUsedTime": fsWssUserUsedTime,
       "fsWssUserAllotedDLBandWidth": fsWssUserAllotedDLBandWidth,
       "fsWssUserAllotedULBandWidth": fsWssUserAllotedULBandWidth,
       "fsWssUserNotifyObjects": fsWssUserNotifyObjects,
       "fsWssUserTrapObjects": fsWssUserTrapObjects,
       "fsWssUserStationMacAddress": fsWssUserStationMacAddress,
       "fsWssNtfUserName": fsWssNtfUserName,
       "fsWssUserNotifications": fsWssUserNotifications,
       "fsWssUserTraps": fsWssUserTraps,
       "fsWssUserVolumeExceeded": fsWssUserVolumeExceeded,
       "fsWssUserTimeExceeded": fsWssUserTimeExceeded}
)
