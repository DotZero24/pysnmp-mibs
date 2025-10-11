# SNMP MIB module (QTECH-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-RIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:03 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechRIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13)
)
if mibBuilder.loadTexts:
    qtechRIPMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechRIPMIBObjects_ObjectIdentity = ObjectIdentity
qtechRIPMIBObjects = _QtechRIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1)
)


class _QtechRipEnable_Type(EnabledStatus):
    """Custom type qtechRipEnable based on EnabledStatus"""
    defaultValue = 2


_QtechRipEnable_Type.__name__ = "EnabledStatus"
_QtechRipEnable_Object = MibScalar
qtechRipEnable = _QtechRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 1),
    _QtechRipEnable_Type()
)
qtechRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipEnable.setStatus("current")


class _QtechRipUpdateTime_Type(Integer32):
    """Custom type qtechRipUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechRipUpdateTime_Type.__name__ = "Integer32"
_QtechRipUpdateTime_Object = MibScalar
qtechRipUpdateTime = _QtechRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 2),
    _QtechRipUpdateTime_Type()
)
qtechRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipUpdateTime.setStatus("current")


class _QtechRipInvalidTime_Type(Integer32):
    """Custom type qtechRipInvalidTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechRipInvalidTime_Type.__name__ = "Integer32"
_QtechRipInvalidTime_Object = MibScalar
qtechRipInvalidTime = _QtechRipInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 3),
    _QtechRipInvalidTime_Type()
)
qtechRipInvalidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipInvalidTime.setStatus("current")


class _QtechRipHolddownTime_Type(Integer32):
    """Custom type qtechRipHolddownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechRipHolddownTime_Type.__name__ = "Integer32"
_QtechRipHolddownTime_Object = MibScalar
qtechRipHolddownTime = _QtechRipHolddownTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 4),
    _QtechRipHolddownTime_Type()
)
qtechRipHolddownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipHolddownTime.setStatus("current")


class _QtechRipRecommendSetting_Type(Integer32):
    """Custom type qtechRipRecommendSetting based on Integer32"""
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


_QtechRipRecommendSetting_Type.__name__ = "Integer32"
_QtechRipRecommendSetting_Object = MibScalar
qtechRipRecommendSetting = _QtechRipRecommendSetting_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 5),
    _QtechRipRecommendSetting_Type()
)
qtechRipRecommendSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipRecommendSetting.setStatus("current")
_QtechRipIfStatTable_Object = MibTable
qtechRipIfStatTable = _QtechRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6)
)
if mibBuilder.loadTexts:
    qtechRipIfStatTable.setStatus("current")
_QtechRipIfStatEntry_Object = MibTableRow
qtechRipIfStatEntry = _QtechRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6, 1)
)
qtechRipIfStatEntry.setIndexNames(
    (0, "QTECH-RIP-MIB", "qtechRipIfStatIfIndex"),
)
if mibBuilder.loadTexts:
    qtechRipIfStatEntry.setStatus("current")
_QtechRipIfStatIfIndex_Type = IfIndex
_QtechRipIfStatIfIndex_Object = MibTableColumn
qtechRipIfStatIfIndex = _QtechRipIfStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6, 1, 1),
    _QtechRipIfStatIfIndex_Type()
)
qtechRipIfStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfStatIfIndex.setStatus("current")
_QtechRipIfStatRcvBadPackets_Type = Counter32
_QtechRipIfStatRcvBadPackets_Object = MibTableColumn
qtechRipIfStatRcvBadPackets = _QtechRipIfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6, 1, 2),
    _QtechRipIfStatRcvBadPackets_Type()
)
qtechRipIfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfStatRcvBadPackets.setStatus("current")
_QtechRipIfStatRcvBadRoutes_Type = Counter32
_QtechRipIfStatRcvBadRoutes_Object = MibTableColumn
qtechRipIfStatRcvBadRoutes = _QtechRipIfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6, 1, 3),
    _QtechRipIfStatRcvBadRoutes_Type()
)
qtechRipIfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfStatRcvBadRoutes.setStatus("current")
_QtechRipIfStatSentUpdates_Type = Counter32
_QtechRipIfStatSentUpdates_Object = MibTableColumn
qtechRipIfStatSentUpdates = _QtechRipIfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 6, 1, 4),
    _QtechRipIfStatSentUpdates_Type()
)
qtechRipIfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfStatSentUpdates.setStatus("current")
_QtechRipIfConfTable_Object = MibTable
qtechRipIfConfTable = _QtechRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7)
)
if mibBuilder.loadTexts:
    qtechRipIfConfTable.setStatus("current")
_QtechRipIfConfEntry_Object = MibTableRow
qtechRipIfConfEntry = _QtechRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1)
)
qtechRipIfConfEntry.setIndexNames(
    (0, "QTECH-RIP-MIB", "qtechRipIfConfIfIndex"),
)
if mibBuilder.loadTexts:
    qtechRipIfConfEntry.setStatus("current")
_QtechRipIfConfIfIndex_Type = IfIndex
_QtechRipIfConfIfIndex_Object = MibTableColumn
qtechRipIfConfIfIndex = _QtechRipIfConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 1),
    _QtechRipIfConfIfIndex_Type()
)
qtechRipIfConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfConfIfIndex.setStatus("current")


class _QtechRipIfConfAuthType_Type(Integer32):
    """Custom type qtechRipIfConfAuthType based on Integer32"""
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


_QtechRipIfConfAuthType_Type.__name__ = "Integer32"
_QtechRipIfConfAuthType_Object = MibTableColumn
qtechRipIfConfAuthType = _QtechRipIfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 2),
    _QtechRipIfConfAuthType_Type()
)
qtechRipIfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfConfAuthType.setStatus("current")


class _QtechRipIfConfAuthKeyChain_Type(DisplayString):
    """Custom type qtechRipIfConfAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRipIfConfAuthKeyChain_Type.__name__ = "DisplayString"
_QtechRipIfConfAuthKeyChain_Object = MibTableColumn
qtechRipIfConfAuthKeyChain = _QtechRipIfConfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 3),
    _QtechRipIfConfAuthKeyChain_Type()
)
qtechRipIfConfAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfConfAuthKeyChain.setStatus("current")


class _QtechRipIfConfSend_Type(Integer32):
    """Custom type qtechRipIfConfSend based on Integer32"""
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


_QtechRipIfConfSend_Type.__name__ = "Integer32"
_QtechRipIfConfSend_Object = MibTableColumn
qtechRipIfConfSend = _QtechRipIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 4),
    _QtechRipIfConfSend_Type()
)
qtechRipIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfConfSend.setStatus("current")


class _QtechRipIfConfReceive_Type(Integer32):
    """Custom type qtechRipIfConfReceive based on Integer32"""
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


_QtechRipIfConfReceive_Type.__name__ = "Integer32"
_QtechRipIfConfReceive_Object = MibTableColumn
qtechRipIfConfReceive = _QtechRipIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 5),
    _QtechRipIfConfReceive_Type()
)
qtechRipIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfConfReceive.setStatus("current")


class _QtechRipIfPassiveStatus_Type(EnabledStatus):
    """Custom type qtechRipIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_QtechRipIfPassiveStatus_Type.__name__ = "EnabledStatus"
_QtechRipIfPassiveStatus_Object = MibTableColumn
qtechRipIfPassiveStatus = _QtechRipIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 6),
    _QtechRipIfPassiveStatus_Type()
)
qtechRipIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfPassiveStatus.setStatus("current")


class _QtechRipIfBroadcastEnable_Type(EnabledStatus):
    """Custom type qtechRipIfBroadcastEnable based on EnabledStatus"""
    defaultValue = 2


_QtechRipIfBroadcastEnable_Type.__name__ = "EnabledStatus"
_QtechRipIfBroadcastEnable_Object = MibTableColumn
qtechRipIfBroadcastEnable = _QtechRipIfBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 7),
    _QtechRipIfBroadcastEnable_Type()
)
qtechRipIfBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipIfBroadcastEnable.setStatus("current")
_QtechRipIfAdminStat_Type = EnabledStatus
_QtechRipIfAdminStat_Object = MibTableColumn
qtechRipIfAdminStat = _QtechRipIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 7, 1, 8),
    _QtechRipIfAdminStat_Type()
)
qtechRipIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfAdminStat.setStatus("current")


class _QtechRipOffsetMetric_Type(Integer32):
    """Custom type qtechRipOffsetMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechRipOffsetMetric_Type.__name__ = "Integer32"
_QtechRipOffsetMetric_Object = MibScalar
qtechRipOffsetMetric = _QtechRipOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 8),
    _QtechRipOffsetMetric_Type()
)
qtechRipOffsetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipOffsetMetric.setStatus("current")


class _QtechRipAdministrativeDistance_Type(Integer32):
    """Custom type qtechRipAdministrativeDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechRipAdministrativeDistance_Type.__name__ = "Integer32"
_QtechRipAdministrativeDistance_Object = MibScalar
qtechRipAdministrativeDistance = _QtechRipAdministrativeDistance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 9),
    _QtechRipAdministrativeDistance_Type()
)
qtechRipAdministrativeDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipAdministrativeDistance.setStatus("current")


class _QtechRipValidateUpdateSrcEnable_Type(EnabledStatus):
    """Custom type qtechRipValidateUpdateSrcEnable based on EnabledStatus"""
    defaultValue = 1


_QtechRipValidateUpdateSrcEnable_Type.__name__ = "EnabledStatus"
_QtechRipValidateUpdateSrcEnable_Object = MibScalar
qtechRipValidateUpdateSrcEnable = _QtechRipValidateUpdateSrcEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 10),
    _QtechRipValidateUpdateSrcEnable_Type()
)
qtechRipValidateUpdateSrcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipValidateUpdateSrcEnable.setStatus("current")


class _QtechRipPassiveStatus_Type(EnabledStatus):
    """Custom type qtechRipPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_QtechRipPassiveStatus_Type.__name__ = "EnabledStatus"
_QtechRipPassiveStatus_Object = MibScalar
qtechRipPassiveStatus = _QtechRipPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 11),
    _QtechRipPassiveStatus_Type()
)
qtechRipPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRipPassiveStatus.setStatus("current")
_QtechRipNextDueIn_Type = TimeTicks
_QtechRipNextDueIn_Object = MibScalar
qtechRipNextDueIn = _QtechRipNextDueIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 12),
    _QtechRipNextDueIn_Type()
)
qtechRipNextDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipNextDueIn.setStatus("current")
_QtechRipIfOffsetTable_Object = MibTable
qtechRipIfOffsetTable = _QtechRipIfOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13)
)
if mibBuilder.loadTexts:
    qtechRipIfOffsetTable.setStatus("current")
_QtechRipIfOffsetEntry_Object = MibTableRow
qtechRipIfOffsetEntry = _QtechRipIfOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1)
)
qtechRipIfOffsetEntry.setIndexNames(
    (0, "QTECH-RIP-MIB", "qtechRipIfOffsetIfIndex"),
    (0, "QTECH-RIP-MIB", "qtechRipIfOffsetMethod"),
)
if mibBuilder.loadTexts:
    qtechRipIfOffsetEntry.setStatus("current")


class _QtechRipIfOffsetIfIndex_Type(Integer32):
    """Custom type qtechRipIfOffsetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechRipIfOffsetIfIndex_Type.__name__ = "Integer32"
_QtechRipIfOffsetIfIndex_Object = MibTableColumn
qtechRipIfOffsetIfIndex = _QtechRipIfOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1, 1),
    _QtechRipIfOffsetIfIndex_Type()
)
qtechRipIfOffsetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfOffsetIfIndex.setStatus("current")


class _QtechRipIfOffsetMethod_Type(Integer32):
    """Custom type qtechRipIfOffsetMethod based on Integer32"""
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


_QtechRipIfOffsetMethod_Type.__name__ = "Integer32"
_QtechRipIfOffsetMethod_Object = MibTableColumn
qtechRipIfOffsetMethod = _QtechRipIfOffsetMethod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1, 2),
    _QtechRipIfOffsetMethod_Type()
)
qtechRipIfOffsetMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipIfOffsetMethod.setStatus("current")


class _QtechRipIfOffsetAclName_Type(DisplayString):
    """Custom type qtechRipIfOffsetAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechRipIfOffsetAclName_Type.__name__ = "DisplayString"
_QtechRipIfOffsetAclName_Object = MibTableColumn
qtechRipIfOffsetAclName = _QtechRipIfOffsetAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1, 3),
    _QtechRipIfOffsetAclName_Type()
)
qtechRipIfOffsetAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRipIfOffsetAclName.setStatus("current")


class _QtechRipIfOffsetMetric_Type(Unsigned32):
    """Custom type qtechRipIfOffsetMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QtechRipIfOffsetMetric_Type.__name__ = "Unsigned32"
_QtechRipIfOffsetMetric_Object = MibTableColumn
qtechRipIfOffsetMetric = _QtechRipIfOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1, 4),
    _QtechRipIfOffsetMetric_Type()
)
qtechRipIfOffsetMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRipIfOffsetMetric.setStatus("current")
_QtechRipIfOffsetStatus_Type = RowStatus
_QtechRipIfOffsetStatus_Object = MibTableColumn
qtechRipIfOffsetStatus = _QtechRipIfOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 13, 1, 5),
    _QtechRipIfOffsetStatus_Type()
)
qtechRipIfOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRipIfOffsetStatus.setStatus("current")
_QtechRipNetworkTable_Object = MibTable
qtechRipNetworkTable = _QtechRipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 14)
)
if mibBuilder.loadTexts:
    qtechRipNetworkTable.setStatus("current")
_QtechRipNetworkEntry_Object = MibTableRow
qtechRipNetworkEntry = _QtechRipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 14, 1)
)
qtechRipNetworkEntry.setIndexNames(
    (0, "QTECH-RIP-MIB", "qtechRipNetworkAddr"),
)
if mibBuilder.loadTexts:
    qtechRipNetworkEntry.setStatus("current")
_QtechRipNetworkAddr_Type = IpAddress
_QtechRipNetworkAddr_Object = MibTableColumn
qtechRipNetworkAddr = _QtechRipNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 14, 1, 1),
    _QtechRipNetworkAddr_Type()
)
qtechRipNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipNetworkAddr.setStatus("current")
_QtechRipNetworkMask_Type = IpAddress
_QtechRipNetworkMask_Object = MibTableColumn
qtechRipNetworkMask = _QtechRipNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 14, 1, 2),
    _QtechRipNetworkMask_Type()
)
qtechRipNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipNetworkMask.setStatus("current")
_QtechRipNetworkStatus_Type = RowStatus
_QtechRipNetworkStatus_Object = MibTableColumn
qtechRipNetworkStatus = _QtechRipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 14, 1, 3),
    _QtechRipNetworkStatus_Type()
)
qtechRipNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRipNetworkStatus.setStatus("current")
_QtechRipNeighborTable_Object = MibTable
qtechRipNeighborTable = _QtechRipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 15)
)
if mibBuilder.loadTexts:
    qtechRipNeighborTable.setStatus("current")
_QtechRipNeighborEntry_Object = MibTableRow
qtechRipNeighborEntry = _QtechRipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 15, 1)
)
qtechRipNeighborEntry.setIndexNames(
    (0, "QTECH-RIP-MIB", "qtechRipNeighborIndex"),
)
if mibBuilder.loadTexts:
    qtechRipNeighborEntry.setStatus("current")
_QtechRipNeighborIndex_Type = IpAddress
_QtechRipNeighborIndex_Object = MibTableColumn
qtechRipNeighborIndex = _QtechRipNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 15, 1, 1),
    _QtechRipNeighborIndex_Type()
)
qtechRipNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRipNeighborIndex.setStatus("current")
_QtechRipNeighborStatus_Type = RowStatus
_QtechRipNeighborStatus_Object = MibTableColumn
qtechRipNeighborStatus = _QtechRipNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 1, 15, 1, 2),
    _QtechRipNeighborStatus_Type()
)
qtechRipNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRipNeighborStatus.setStatus("current")
_QtechRIPMIBConformance_ObjectIdentity = ObjectIdentity
qtechRIPMIBConformance = _QtechRIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2)
)
_QtechRIPMIBCompliances_ObjectIdentity = ObjectIdentity
qtechRIPMIBCompliances = _QtechRIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2, 1)
)
_QtechRIPMIBGroups_ObjectIdentity = ObjectIdentity
qtechRIPMIBGroups = _QtechRIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2, 2)
)

# Managed Objects groups

qtechRipMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2, 2, 1)
)
qtechRipMIBGroup.setObjects(
      *(("QTECH-RIP-MIB", "qtechRipEnable"),
        ("QTECH-RIP-MIB", "qtechRipUpdateTime"),
        ("QTECH-RIP-MIB", "qtechRipInvalidTime"),
        ("QTECH-RIP-MIB", "qtechRipHolddownTime"),
        ("QTECH-RIP-MIB", "qtechRipRecommendSetting"),
        ("QTECH-RIP-MIB", "qtechRipIfStatIfIndex"),
        ("QTECH-RIP-MIB", "qtechRipIfStatRcvBadPackets"),
        ("QTECH-RIP-MIB", "qtechRipIfStatRcvBadRoutes"),
        ("QTECH-RIP-MIB", "qtechRipIfStatSentUpdates"),
        ("QTECH-RIP-MIB", "qtechRipIfConfIfIndex"),
        ("QTECH-RIP-MIB", "qtechRipIfConfAuthType"),
        ("QTECH-RIP-MIB", "qtechRipIfConfAuthKeyChain"),
        ("QTECH-RIP-MIB", "qtechRipIfConfSend"),
        ("QTECH-RIP-MIB", "qtechRipIfConfReceive"),
        ("QTECH-RIP-MIB", "qtechRipIfPassiveStatus"),
        ("QTECH-RIP-MIB", "qtechRipIfBroadcastEnable"),
        ("QTECH-RIP-MIB", "qtechRipIfAdminStat"),
        ("QTECH-RIP-MIB", "qtechRipOffsetMetric"),
        ("QTECH-RIP-MIB", "qtechRipAdministrativeDistance"),
        ("QTECH-RIP-MIB", "qtechRipValidateUpdateSrcEnable"))
)
if mibBuilder.loadTexts:
    qtechRipMIBGroup.setStatus("current")

qtechRIPExtendMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2, 2, 2)
)
qtechRIPExtendMIBGroup.setObjects(
      *(("QTECH-RIP-MIB", "qtechRipNextDueIn"),
        ("QTECH-RIP-MIB", "qtechRipIfOffsetIfIndex"),
        ("QTECH-RIP-MIB", "qtechRipIfOffsetMethod"),
        ("QTECH-RIP-MIB", "qtechRipIfOffsetAclName"),
        ("QTECH-RIP-MIB", "qtechRipIfOffsetMetric"),
        ("QTECH-RIP-MIB", "qtechRipIfOffsetStatus"),
        ("QTECH-RIP-MIB", "qtechRipNetworkAddr"),
        ("QTECH-RIP-MIB", "qtechRipNetworkMask"),
        ("QTECH-RIP-MIB", "qtechRipNetworkStatus"),
        ("QTECH-RIP-MIB", "qtechRipNeighborIndex"),
        ("QTECH-RIP-MIB", "qtechRipNeighborStatus"))
)
if mibBuilder.loadTexts:
    qtechRIPExtendMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechRIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 13, 2, 1, 1)
)
qtechRIPMIBCompliance.setObjects(
      *(("QTECH-RIP-MIB", "qtechRipMIBGroup"),
        ("QTECH-RIP-MIB", "qtechRIPExtendMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechRIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-RIP-MIB",
    **{"qtechRIPMIB": qtechRIPMIB,
       "qtechRIPMIBObjects": qtechRIPMIBObjects,
       "qtechRipEnable": qtechRipEnable,
       "qtechRipUpdateTime": qtechRipUpdateTime,
       "qtechRipInvalidTime": qtechRipInvalidTime,
       "qtechRipHolddownTime": qtechRipHolddownTime,
       "qtechRipRecommendSetting": qtechRipRecommendSetting,
       "qtechRipIfStatTable": qtechRipIfStatTable,
       "qtechRipIfStatEntry": qtechRipIfStatEntry,
       "qtechRipIfStatIfIndex": qtechRipIfStatIfIndex,
       "qtechRipIfStatRcvBadPackets": qtechRipIfStatRcvBadPackets,
       "qtechRipIfStatRcvBadRoutes": qtechRipIfStatRcvBadRoutes,
       "qtechRipIfStatSentUpdates": qtechRipIfStatSentUpdates,
       "qtechRipIfConfTable": qtechRipIfConfTable,
       "qtechRipIfConfEntry": qtechRipIfConfEntry,
       "qtechRipIfConfIfIndex": qtechRipIfConfIfIndex,
       "qtechRipIfConfAuthType": qtechRipIfConfAuthType,
       "qtechRipIfConfAuthKeyChain": qtechRipIfConfAuthKeyChain,
       "qtechRipIfConfSend": qtechRipIfConfSend,
       "qtechRipIfConfReceive": qtechRipIfConfReceive,
       "qtechRipIfPassiveStatus": qtechRipIfPassiveStatus,
       "qtechRipIfBroadcastEnable": qtechRipIfBroadcastEnable,
       "qtechRipIfAdminStat": qtechRipIfAdminStat,
       "qtechRipOffsetMetric": qtechRipOffsetMetric,
       "qtechRipAdministrativeDistance": qtechRipAdministrativeDistance,
       "qtechRipValidateUpdateSrcEnable": qtechRipValidateUpdateSrcEnable,
       "qtechRipPassiveStatus": qtechRipPassiveStatus,
       "qtechRipNextDueIn": qtechRipNextDueIn,
       "qtechRipIfOffsetTable": qtechRipIfOffsetTable,
       "qtechRipIfOffsetEntry": qtechRipIfOffsetEntry,
       "qtechRipIfOffsetIfIndex": qtechRipIfOffsetIfIndex,
       "qtechRipIfOffsetMethod": qtechRipIfOffsetMethod,
       "qtechRipIfOffsetAclName": qtechRipIfOffsetAclName,
       "qtechRipIfOffsetMetric": qtechRipIfOffsetMetric,
       "qtechRipIfOffsetStatus": qtechRipIfOffsetStatus,
       "qtechRipNetworkTable": qtechRipNetworkTable,
       "qtechRipNetworkEntry": qtechRipNetworkEntry,
       "qtechRipNetworkAddr": qtechRipNetworkAddr,
       "qtechRipNetworkMask": qtechRipNetworkMask,
       "qtechRipNetworkStatus": qtechRipNetworkStatus,
       "qtechRipNeighborTable": qtechRipNeighborTable,
       "qtechRipNeighborEntry": qtechRipNeighborEntry,
       "qtechRipNeighborIndex": qtechRipNeighborIndex,
       "qtechRipNeighborStatus": qtechRipNeighborStatus,
       "qtechRIPMIBConformance": qtechRIPMIBConformance,
       "qtechRIPMIBCompliances": qtechRIPMIBCompliances,
       "qtechRIPMIBCompliance": qtechRIPMIBCompliance,
       "qtechRIPMIBGroups": qtechRIPMIBGroups,
       "qtechRipMIBGroup": qtechRipMIBGroup,
       "qtechRIPExtendMIBGroup": qtechRIPExtendMIBGroup}
)
