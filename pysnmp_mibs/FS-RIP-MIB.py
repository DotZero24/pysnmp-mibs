# SNMP MIB module (FS-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-RIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:12 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsRIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13)
)
if mibBuilder.loadTexts:
    fsRIPMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRIPMIBObjects_ObjectIdentity = ObjectIdentity
fsRIPMIBObjects = _FsRIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1)
)


class _FsRipEnable_Type(EnabledStatus):
    """Custom type fsRipEnable based on EnabledStatus"""
    defaultValue = 2


_FsRipEnable_Type.__name__ = "EnabledStatus"
_FsRipEnable_Object = MibScalar
fsRipEnable = _FsRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 1),
    _FsRipEnable_Type()
)
fsRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipEnable.setStatus("current")


class _FsRipUpdateTime_Type(Integer32):
    """Custom type fsRipUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRipUpdateTime_Type.__name__ = "Integer32"
_FsRipUpdateTime_Object = MibScalar
fsRipUpdateTime = _FsRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 2),
    _FsRipUpdateTime_Type()
)
fsRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipUpdateTime.setStatus("current")


class _FsRipInvalidTime_Type(Integer32):
    """Custom type fsRipInvalidTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRipInvalidTime_Type.__name__ = "Integer32"
_FsRipInvalidTime_Object = MibScalar
fsRipInvalidTime = _FsRipInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 3),
    _FsRipInvalidTime_Type()
)
fsRipInvalidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipInvalidTime.setStatus("current")


class _FsRipHolddownTime_Type(Integer32):
    """Custom type fsRipHolddownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRipHolddownTime_Type.__name__ = "Integer32"
_FsRipHolddownTime_Object = MibScalar
fsRipHolddownTime = _FsRipHolddownTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 4),
    _FsRipHolddownTime_Type()
)
fsRipHolddownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipHolddownTime.setStatus("current")


class _FsRipRecommendSetting_Type(Integer32):
    """Custom type fsRipRecommendSetting based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ripv1", 1),
          ("ripv2", 2),
          ("compatible", 3))
    )


_FsRipRecommendSetting_Type.__name__ = "Integer32"
_FsRipRecommendSetting_Object = MibScalar
fsRipRecommendSetting = _FsRipRecommendSetting_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 5),
    _FsRipRecommendSetting_Type()
)
fsRipRecommendSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRecommendSetting.setStatus("current")
_FsRipIfStatTable_Object = MibTable
fsRipIfStatTable = _FsRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6)
)
if mibBuilder.loadTexts:
    fsRipIfStatTable.setStatus("current")
_FsRipIfStatEntry_Object = MibTableRow
fsRipIfStatEntry = _FsRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6, 1)
)
fsRipIfStatEntry.setIndexNames(
    (0, "FS-RIP-MIB", "fsRipIfStatIfIndex"),
)
if mibBuilder.loadTexts:
    fsRipIfStatEntry.setStatus("current")
_FsRipIfStatIfIndex_Type = IfIndex
_FsRipIfStatIfIndex_Object = MibTableColumn
fsRipIfStatIfIndex = _FsRipIfStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6, 1, 1),
    _FsRipIfStatIfIndex_Type()
)
fsRipIfStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfStatIfIndex.setStatus("current")
_FsRipIfStatRcvBadPackets_Type = Counter32
_FsRipIfStatRcvBadPackets_Object = MibTableColumn
fsRipIfStatRcvBadPackets = _FsRipIfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6, 1, 2),
    _FsRipIfStatRcvBadPackets_Type()
)
fsRipIfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfStatRcvBadPackets.setStatus("current")
_FsRipIfStatRcvBadRoutes_Type = Counter32
_FsRipIfStatRcvBadRoutes_Object = MibTableColumn
fsRipIfStatRcvBadRoutes = _FsRipIfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6, 1, 3),
    _FsRipIfStatRcvBadRoutes_Type()
)
fsRipIfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfStatRcvBadRoutes.setStatus("current")
_FsRipIfStatSentUpdates_Type = Counter32
_FsRipIfStatSentUpdates_Object = MibTableColumn
fsRipIfStatSentUpdates = _FsRipIfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 6, 1, 4),
    _FsRipIfStatSentUpdates_Type()
)
fsRipIfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfStatSentUpdates.setStatus("current")
_FsRipIfConfTable_Object = MibTable
fsRipIfConfTable = _FsRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7)
)
if mibBuilder.loadTexts:
    fsRipIfConfTable.setStatus("current")
_FsRipIfConfEntry_Object = MibTableRow
fsRipIfConfEntry = _FsRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1)
)
fsRipIfConfEntry.setIndexNames(
    (0, "FS-RIP-MIB", "fsRipIfConfIfIndex"),
)
if mibBuilder.loadTexts:
    fsRipIfConfEntry.setStatus("current")
_FsRipIfConfIfIndex_Type = IfIndex
_FsRipIfConfIfIndex_Object = MibTableColumn
fsRipIfConfIfIndex = _FsRipIfConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 1),
    _FsRipIfConfIfIndex_Type()
)
fsRipIfConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfConfIfIndex.setStatus("current")


class _FsRipIfConfAuthType_Type(Integer32):
    """Custom type fsRipIfConfAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3))
    )


_FsRipIfConfAuthType_Type.__name__ = "Integer32"
_FsRipIfConfAuthType_Object = MibTableColumn
fsRipIfConfAuthType = _FsRipIfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 2),
    _FsRipIfConfAuthType_Type()
)
fsRipIfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfConfAuthType.setStatus("current")


class _FsRipIfConfAuthKeyChain_Type(DisplayString):
    """Custom type fsRipIfConfAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRipIfConfAuthKeyChain_Type.__name__ = "DisplayString"
_FsRipIfConfAuthKeyChain_Object = MibTableColumn
fsRipIfConfAuthKeyChain = _FsRipIfConfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 3),
    _FsRipIfConfAuthKeyChain_Type()
)
fsRipIfConfAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfConfAuthKeyChain.setStatus("current")


class _FsRipIfConfSend_Type(Integer32):
    """Custom type fsRipIfConfSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ripVersion1", 1),
          ("rip1Compatible", 2),
          ("ripVersion2", 3))
    )


_FsRipIfConfSend_Type.__name__ = "Integer32"
_FsRipIfConfSend_Object = MibTableColumn
fsRipIfConfSend = _FsRipIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 4),
    _FsRipIfConfSend_Type()
)
fsRipIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfConfSend.setStatus("current")


class _FsRipIfConfReceive_Type(Integer32):
    """Custom type fsRipIfConfReceive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3))
    )


_FsRipIfConfReceive_Type.__name__ = "Integer32"
_FsRipIfConfReceive_Object = MibTableColumn
fsRipIfConfReceive = _FsRipIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 5),
    _FsRipIfConfReceive_Type()
)
fsRipIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfConfReceive.setStatus("current")


class _FsRipIfPassiveStatus_Type(EnabledStatus):
    """Custom type fsRipIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_FsRipIfPassiveStatus_Type.__name__ = "EnabledStatus"
_FsRipIfPassiveStatus_Object = MibTableColumn
fsRipIfPassiveStatus = _FsRipIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 6),
    _FsRipIfPassiveStatus_Type()
)
fsRipIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfPassiveStatus.setStatus("current")


class _FsRipIfBroadcastEnable_Type(EnabledStatus):
    """Custom type fsRipIfBroadcastEnable based on EnabledStatus"""
    defaultValue = 2


_FsRipIfBroadcastEnable_Type.__name__ = "EnabledStatus"
_FsRipIfBroadcastEnable_Object = MibTableColumn
fsRipIfBroadcastEnable = _FsRipIfBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 7),
    _FsRipIfBroadcastEnable_Type()
)
fsRipIfBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipIfBroadcastEnable.setStatus("current")
_FsRipIfAdminStat_Type = EnabledStatus
_FsRipIfAdminStat_Object = MibTableColumn
fsRipIfAdminStat = _FsRipIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 7, 1, 8),
    _FsRipIfAdminStat_Type()
)
fsRipIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfAdminStat.setStatus("current")


class _FsRipOffsetMetric_Type(Integer32):
    """Custom type fsRipOffsetMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsRipOffsetMetric_Type.__name__ = "Integer32"
_FsRipOffsetMetric_Object = MibScalar
fsRipOffsetMetric = _FsRipOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 8),
    _FsRipOffsetMetric_Type()
)
fsRipOffsetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipOffsetMetric.setStatus("current")


class _FsRipAdministrativeDistance_Type(Integer32):
    """Custom type fsRipAdministrativeDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipAdministrativeDistance_Type.__name__ = "Integer32"
_FsRipAdministrativeDistance_Object = MibScalar
fsRipAdministrativeDistance = _FsRipAdministrativeDistance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 9),
    _FsRipAdministrativeDistance_Type()
)
fsRipAdministrativeDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipAdministrativeDistance.setStatus("current")


class _FsRipValidateUpdateSrcEnable_Type(EnabledStatus):
    """Custom type fsRipValidateUpdateSrcEnable based on EnabledStatus"""
    defaultValue = 1


_FsRipValidateUpdateSrcEnable_Type.__name__ = "EnabledStatus"
_FsRipValidateUpdateSrcEnable_Object = MibScalar
fsRipValidateUpdateSrcEnable = _FsRipValidateUpdateSrcEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 10),
    _FsRipValidateUpdateSrcEnable_Type()
)
fsRipValidateUpdateSrcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipValidateUpdateSrcEnable.setStatus("current")


class _FsRipPassiveStatus_Type(EnabledStatus):
    """Custom type fsRipPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_FsRipPassiveStatus_Type.__name__ = "EnabledStatus"
_FsRipPassiveStatus_Object = MibScalar
fsRipPassiveStatus = _FsRipPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 11),
    _FsRipPassiveStatus_Type()
)
fsRipPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipPassiveStatus.setStatus("current")
_FsRipNextDueIn_Type = TimeTicks
_FsRipNextDueIn_Object = MibScalar
fsRipNextDueIn = _FsRipNextDueIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 12),
    _FsRipNextDueIn_Type()
)
fsRipNextDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipNextDueIn.setStatus("current")
_FsRipIfOffsetTable_Object = MibTable
fsRipIfOffsetTable = _FsRipIfOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13)
)
if mibBuilder.loadTexts:
    fsRipIfOffsetTable.setStatus("current")
_FsRipIfOffsetEntry_Object = MibTableRow
fsRipIfOffsetEntry = _FsRipIfOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1)
)
fsRipIfOffsetEntry.setIndexNames(
    (0, "FS-RIP-MIB", "fsRipIfOffsetIfIndex"),
    (0, "FS-RIP-MIB", "fsRipIfOffsetMethod"),
)
if mibBuilder.loadTexts:
    fsRipIfOffsetEntry.setStatus("current")


class _FsRipIfOffsetIfIndex_Type(Integer32):
    """Custom type fsRipIfOffsetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRipIfOffsetIfIndex_Type.__name__ = "Integer32"
_FsRipIfOffsetIfIndex_Object = MibTableColumn
fsRipIfOffsetIfIndex = _FsRipIfOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1, 1),
    _FsRipIfOffsetIfIndex_Type()
)
fsRipIfOffsetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfOffsetIfIndex.setStatus("current")


class _FsRipIfOffsetMethod_Type(Integer32):
    """Custom type fsRipIfOffsetMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("out", 1),
          ("in", 2))
    )


_FsRipIfOffsetMethod_Type.__name__ = "Integer32"
_FsRipIfOffsetMethod_Object = MibTableColumn
fsRipIfOffsetMethod = _FsRipIfOffsetMethod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1, 2),
    _FsRipIfOffsetMethod_Type()
)
fsRipIfOffsetMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipIfOffsetMethod.setStatus("current")


class _FsRipIfOffsetAclName_Type(DisplayString):
    """Custom type fsRipIfOffsetAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsRipIfOffsetAclName_Type.__name__ = "DisplayString"
_FsRipIfOffsetAclName_Object = MibTableColumn
fsRipIfOffsetAclName = _FsRipIfOffsetAclName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1, 3),
    _FsRipIfOffsetAclName_Type()
)
fsRipIfOffsetAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRipIfOffsetAclName.setStatus("current")


class _FsRipIfOffsetMetric_Type(Unsigned32):
    """Custom type fsRipIfOffsetMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FsRipIfOffsetMetric_Type.__name__ = "Unsigned32"
_FsRipIfOffsetMetric_Object = MibTableColumn
fsRipIfOffsetMetric = _FsRipIfOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1, 4),
    _FsRipIfOffsetMetric_Type()
)
fsRipIfOffsetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRipIfOffsetMetric.setStatus("current")
_FsRipIfOffsetStatus_Type = RowStatus
_FsRipIfOffsetStatus_Object = MibTableColumn
fsRipIfOffsetStatus = _FsRipIfOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 13, 1, 5),
    _FsRipIfOffsetStatus_Type()
)
fsRipIfOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRipIfOffsetStatus.setStatus("current")
_FsRipNetworkTable_Object = MibTable
fsRipNetworkTable = _FsRipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 14)
)
if mibBuilder.loadTexts:
    fsRipNetworkTable.setStatus("current")
_FsRipNetworkEntry_Object = MibTableRow
fsRipNetworkEntry = _FsRipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 14, 1)
)
fsRipNetworkEntry.setIndexNames(
    (0, "FS-RIP-MIB", "fsRipNetworkAddr"),
)
if mibBuilder.loadTexts:
    fsRipNetworkEntry.setStatus("current")
_FsRipNetworkAddr_Type = IpAddress
_FsRipNetworkAddr_Object = MibTableColumn
fsRipNetworkAddr = _FsRipNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 14, 1, 1),
    _FsRipNetworkAddr_Type()
)
fsRipNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipNetworkAddr.setStatus("current")
_FsRipNetworkMask_Type = IpAddress
_FsRipNetworkMask_Object = MibTableColumn
fsRipNetworkMask = _FsRipNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 14, 1, 2),
    _FsRipNetworkMask_Type()
)
fsRipNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipNetworkMask.setStatus("current")
_FsRipNetworkStatus_Type = RowStatus
_FsRipNetworkStatus_Object = MibTableColumn
fsRipNetworkStatus = _FsRipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 14, 1, 3),
    _FsRipNetworkStatus_Type()
)
fsRipNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRipNetworkStatus.setStatus("current")
_FsRipNeighborTable_Object = MibTable
fsRipNeighborTable = _FsRipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 15)
)
if mibBuilder.loadTexts:
    fsRipNeighborTable.setStatus("current")
_FsRipNeighborEntry_Object = MibTableRow
fsRipNeighborEntry = _FsRipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 15, 1)
)
fsRipNeighborEntry.setIndexNames(
    (0, "FS-RIP-MIB", "fsRipNeighborIndex"),
)
if mibBuilder.loadTexts:
    fsRipNeighborEntry.setStatus("current")
_FsRipNeighborIndex_Type = IpAddress
_FsRipNeighborIndex_Object = MibTableColumn
fsRipNeighborIndex = _FsRipNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 15, 1, 1),
    _FsRipNeighborIndex_Type()
)
fsRipNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipNeighborIndex.setStatus("current")
_FsRipNeighborStatus_Type = RowStatus
_FsRipNeighborStatus_Object = MibTableColumn
fsRipNeighborStatus = _FsRipNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 1, 15, 1, 2),
    _FsRipNeighborStatus_Type()
)
fsRipNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRipNeighborStatus.setStatus("current")
_FsRIPMIBConformance_ObjectIdentity = ObjectIdentity
fsRIPMIBConformance = _FsRIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2)
)
_FsRIPMIBCompliances_ObjectIdentity = ObjectIdentity
fsRIPMIBCompliances = _FsRIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2, 1)
)
_FsRIPMIBGroups_ObjectIdentity = ObjectIdentity
fsRIPMIBGroups = _FsRIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2, 2)
)

# Managed Objects groups

fsRipMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2, 2, 1)
)
fsRipMIBGroup.setObjects(
      *(("FS-RIP-MIB", "fsRipEnable"),
        ("FS-RIP-MIB", "fsRipUpdateTime"),
        ("FS-RIP-MIB", "fsRipInvalidTime"),
        ("FS-RIP-MIB", "fsRipHolddownTime"),
        ("FS-RIP-MIB", "fsRipRecommendSetting"),
        ("FS-RIP-MIB", "fsRipIfStatIfIndex"),
        ("FS-RIP-MIB", "fsRipIfStatRcvBadPackets"),
        ("FS-RIP-MIB", "fsRipIfStatRcvBadRoutes"),
        ("FS-RIP-MIB", "fsRipIfStatSentUpdates"),
        ("FS-RIP-MIB", "fsRipIfConfIfIndex"),
        ("FS-RIP-MIB", "fsRipIfConfAuthType"),
        ("FS-RIP-MIB", "fsRipIfConfAuthKeyChain"),
        ("FS-RIP-MIB", "fsRipIfConfSend"),
        ("FS-RIP-MIB", "fsRipIfConfReceive"),
        ("FS-RIP-MIB", "fsRipIfPassiveStatus"),
        ("FS-RIP-MIB", "fsRipIfBroadcastEnable"),
        ("FS-RIP-MIB", "fsRipIfAdminStat"),
        ("FS-RIP-MIB", "fsRipOffsetMetric"),
        ("FS-RIP-MIB", "fsRipAdministrativeDistance"),
        ("FS-RIP-MIB", "fsRipValidateUpdateSrcEnable"))
)
if mibBuilder.loadTexts:
    fsRipMIBGroup.setStatus("current")

fsRIPExtendMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2, 2, 2)
)
fsRIPExtendMIBGroup.setObjects(
      *(("FS-RIP-MIB", "fsRipNextDueIn"),
        ("FS-RIP-MIB", "fsRipIfOffsetIfIndex"),
        ("FS-RIP-MIB", "fsRipIfOffsetMethod"),
        ("FS-RIP-MIB", "fsRipIfOffsetAclName"),
        ("FS-RIP-MIB", "fsRipIfOffsetMetric"),
        ("FS-RIP-MIB", "fsRipIfOffsetStatus"),
        ("FS-RIP-MIB", "fsRipNetworkAddr"),
        ("FS-RIP-MIB", "fsRipNetworkMask"),
        ("FS-RIP-MIB", "fsRipNetworkStatus"),
        ("FS-RIP-MIB", "fsRipNeighborIndex"),
        ("FS-RIP-MIB", "fsRipNeighborStatus"))
)
if mibBuilder.loadTexts:
    fsRIPExtendMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsRIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 13, 2, 1, 1)
)
fsRIPMIBCompliance.setObjects(
      *(("FS-RIP-MIB", "fsRipMIBGroup"),
        ("FS-RIP-MIB", "fsRIPExtendMIBGroup"))
)
if mibBuilder.loadTexts:
    fsRIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-RIP-MIB",
    **{"fsRIPMIB": fsRIPMIB,
       "fsRIPMIBObjects": fsRIPMIBObjects,
       "fsRipEnable": fsRipEnable,
       "fsRipUpdateTime": fsRipUpdateTime,
       "fsRipInvalidTime": fsRipInvalidTime,
       "fsRipHolddownTime": fsRipHolddownTime,
       "fsRipRecommendSetting": fsRipRecommendSetting,
       "fsRipIfStatTable": fsRipIfStatTable,
       "fsRipIfStatEntry": fsRipIfStatEntry,
       "fsRipIfStatIfIndex": fsRipIfStatIfIndex,
       "fsRipIfStatRcvBadPackets": fsRipIfStatRcvBadPackets,
       "fsRipIfStatRcvBadRoutes": fsRipIfStatRcvBadRoutes,
       "fsRipIfStatSentUpdates": fsRipIfStatSentUpdates,
       "fsRipIfConfTable": fsRipIfConfTable,
       "fsRipIfConfEntry": fsRipIfConfEntry,
       "fsRipIfConfIfIndex": fsRipIfConfIfIndex,
       "fsRipIfConfAuthType": fsRipIfConfAuthType,
       "fsRipIfConfAuthKeyChain": fsRipIfConfAuthKeyChain,
       "fsRipIfConfSend": fsRipIfConfSend,
       "fsRipIfConfReceive": fsRipIfConfReceive,
       "fsRipIfPassiveStatus": fsRipIfPassiveStatus,
       "fsRipIfBroadcastEnable": fsRipIfBroadcastEnable,
       "fsRipIfAdminStat": fsRipIfAdminStat,
       "fsRipOffsetMetric": fsRipOffsetMetric,
       "fsRipAdministrativeDistance": fsRipAdministrativeDistance,
       "fsRipValidateUpdateSrcEnable": fsRipValidateUpdateSrcEnable,
       "fsRipPassiveStatus": fsRipPassiveStatus,
       "fsRipNextDueIn": fsRipNextDueIn,
       "fsRipIfOffsetTable": fsRipIfOffsetTable,
       "fsRipIfOffsetEntry": fsRipIfOffsetEntry,
       "fsRipIfOffsetIfIndex": fsRipIfOffsetIfIndex,
       "fsRipIfOffsetMethod": fsRipIfOffsetMethod,
       "fsRipIfOffsetAclName": fsRipIfOffsetAclName,
       "fsRipIfOffsetMetric": fsRipIfOffsetMetric,
       "fsRipIfOffsetStatus": fsRipIfOffsetStatus,
       "fsRipNetworkTable": fsRipNetworkTable,
       "fsRipNetworkEntry": fsRipNetworkEntry,
       "fsRipNetworkAddr": fsRipNetworkAddr,
       "fsRipNetworkMask": fsRipNetworkMask,
       "fsRipNetworkStatus": fsRipNetworkStatus,
       "fsRipNeighborTable": fsRipNeighborTable,
       "fsRipNeighborEntry": fsRipNeighborEntry,
       "fsRipNeighborIndex": fsRipNeighborIndex,
       "fsRipNeighborStatus": fsRipNeighborStatus,
       "fsRIPMIBConformance": fsRIPMIBConformance,
       "fsRIPMIBCompliances": fsRIPMIBCompliances,
       "fsRIPMIBCompliance": fsRIPMIBCompliance,
       "fsRIPMIBGroups": fsRIPMIBGroups,
       "fsRipMIBGroup": fsRipMIBGroup,
       "fsRIPExtendMIBGroup": fsRIPExtendMIBGroup}
)
