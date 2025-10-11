# SNMP MIB module (MY-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-RIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:44 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

myRIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13)
)
if mibBuilder.loadTexts:
    myRIPMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyRIPMIBObjects_ObjectIdentity = ObjectIdentity
myRIPMIBObjects = _MyRIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1)
)


class _MyRipEnable_Type(EnabledStatus):
    """Custom type myRipEnable based on EnabledStatus"""
    defaultValue = 2


_MyRipEnable_Type.__name__ = "EnabledStatus"
_MyRipEnable_Object = MibScalar
myRipEnable = _MyRipEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 1),
    _MyRipEnable_Type()
)
myRipEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipEnable.setStatus("current")


class _MyRipUpdateTime_Type(Integer32):
    """Custom type myRipUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyRipUpdateTime_Type.__name__ = "Integer32"
_MyRipUpdateTime_Object = MibScalar
myRipUpdateTime = _MyRipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 2),
    _MyRipUpdateTime_Type()
)
myRipUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipUpdateTime.setStatus("current")


class _MyRipInvalidTime_Type(Integer32):
    """Custom type myRipInvalidTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MyRipInvalidTime_Type.__name__ = "Integer32"
_MyRipInvalidTime_Object = MibScalar
myRipInvalidTime = _MyRipInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 3),
    _MyRipInvalidTime_Type()
)
myRipInvalidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipInvalidTime.setStatus("current")


class _MyRipHolddownTime_Type(Integer32):
    """Custom type myRipHolddownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyRipHolddownTime_Type.__name__ = "Integer32"
_MyRipHolddownTime_Object = MibScalar
myRipHolddownTime = _MyRipHolddownTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 4),
    _MyRipHolddownTime_Type()
)
myRipHolddownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipHolddownTime.setStatus("current")


class _MyRipRecommendSetting_Type(Integer32):
    """Custom type myRipRecommendSetting based on Integer32"""
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


_MyRipRecommendSetting_Type.__name__ = "Integer32"
_MyRipRecommendSetting_Object = MibScalar
myRipRecommendSetting = _MyRipRecommendSetting_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 5),
    _MyRipRecommendSetting_Type()
)
myRipRecommendSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipRecommendSetting.setStatus("current")
_MyRipIfStatTable_Object = MibTable
myRipIfStatTable = _MyRipIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6)
)
if mibBuilder.loadTexts:
    myRipIfStatTable.setStatus("current")
_MyRipIfStatEntry_Object = MibTableRow
myRipIfStatEntry = _MyRipIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1)
)
myRipIfStatEntry.setIndexNames(
    (0, "MY-RIP-MIB", "myRipIfStatIfIndex"),
)
if mibBuilder.loadTexts:
    myRipIfStatEntry.setStatus("current")
_MyRipIfStatIfIndex_Type = IfIndex
_MyRipIfStatIfIndex_Object = MibTableColumn
myRipIfStatIfIndex = _MyRipIfStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 1),
    _MyRipIfStatIfIndex_Type()
)
myRipIfStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfStatIfIndex.setStatus("current")
_MyRipIfStatRcvBadPackets_Type = Counter32
_MyRipIfStatRcvBadPackets_Object = MibTableColumn
myRipIfStatRcvBadPackets = _MyRipIfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 2),
    _MyRipIfStatRcvBadPackets_Type()
)
myRipIfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfStatRcvBadPackets.setStatus("current")
_MyRipIfStatRcvBadRoutes_Type = Counter32
_MyRipIfStatRcvBadRoutes_Object = MibTableColumn
myRipIfStatRcvBadRoutes = _MyRipIfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 3),
    _MyRipIfStatRcvBadRoutes_Type()
)
myRipIfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfStatRcvBadRoutes.setStatus("current")
_MyRipIfStatSentUpdates_Type = Counter32
_MyRipIfStatSentUpdates_Object = MibTableColumn
myRipIfStatSentUpdates = _MyRipIfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 6, 1, 4),
    _MyRipIfStatSentUpdates_Type()
)
myRipIfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfStatSentUpdates.setStatus("current")
_MyRipIfConfTable_Object = MibTable
myRipIfConfTable = _MyRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7)
)
if mibBuilder.loadTexts:
    myRipIfConfTable.setStatus("current")
_MyRipIfConfEntry_Object = MibTableRow
myRipIfConfEntry = _MyRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1)
)
myRipIfConfEntry.setIndexNames(
    (0, "MY-RIP-MIB", "myRipIfConfIfIndex"),
)
if mibBuilder.loadTexts:
    myRipIfConfEntry.setStatus("current")
_MyRipIfConfIfIndex_Type = IfIndex
_MyRipIfConfIfIndex_Object = MibTableColumn
myRipIfConfIfIndex = _MyRipIfConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 1),
    _MyRipIfConfIfIndex_Type()
)
myRipIfConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfConfIfIndex.setStatus("current")


class _MyRipIfConfAuthType_Type(Integer32):
    """Custom type myRipIfConfAuthType based on Integer32"""
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


_MyRipIfConfAuthType_Type.__name__ = "Integer32"
_MyRipIfConfAuthType_Object = MibTableColumn
myRipIfConfAuthType = _MyRipIfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 2),
    _MyRipIfConfAuthType_Type()
)
myRipIfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfConfAuthType.setStatus("current")


class _MyRipIfConfAuthKeyChain_Type(DisplayString):
    """Custom type myRipIfConfAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyRipIfConfAuthKeyChain_Type.__name__ = "DisplayString"
_MyRipIfConfAuthKeyChain_Object = MibTableColumn
myRipIfConfAuthKeyChain = _MyRipIfConfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 3),
    _MyRipIfConfAuthKeyChain_Type()
)
myRipIfConfAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfConfAuthKeyChain.setStatus("current")


class _MyRipIfConfSend_Type(Integer32):
    """Custom type myRipIfConfSend based on Integer32"""
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


_MyRipIfConfSend_Type.__name__ = "Integer32"
_MyRipIfConfSend_Object = MibTableColumn
myRipIfConfSend = _MyRipIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 4),
    _MyRipIfConfSend_Type()
)
myRipIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfConfSend.setStatus("current")


class _MyRipIfConfReceive_Type(Integer32):
    """Custom type myRipIfConfReceive based on Integer32"""
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


_MyRipIfConfReceive_Type.__name__ = "Integer32"
_MyRipIfConfReceive_Object = MibTableColumn
myRipIfConfReceive = _MyRipIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 5),
    _MyRipIfConfReceive_Type()
)
myRipIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfConfReceive.setStatus("current")


class _MyRipIfPassiveStatus_Type(EnabledStatus):
    """Custom type myRipIfPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_MyRipIfPassiveStatus_Type.__name__ = "EnabledStatus"
_MyRipIfPassiveStatus_Object = MibTableColumn
myRipIfPassiveStatus = _MyRipIfPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 6),
    _MyRipIfPassiveStatus_Type()
)
myRipIfPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfPassiveStatus.setStatus("current")


class _MyRipIfBroadcastEnable_Type(EnabledStatus):
    """Custom type myRipIfBroadcastEnable based on EnabledStatus"""
    defaultValue = 2


_MyRipIfBroadcastEnable_Type.__name__ = "EnabledStatus"
_MyRipIfBroadcastEnable_Object = MibTableColumn
myRipIfBroadcastEnable = _MyRipIfBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 7),
    _MyRipIfBroadcastEnable_Type()
)
myRipIfBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfBroadcastEnable.setStatus("current")
_MyRipIfAdminStat_Type = EnabledStatus
_MyRipIfAdminStat_Object = MibTableColumn
myRipIfAdminStat = _MyRipIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 7, 1, 8),
    _MyRipIfAdminStat_Type()
)
myRipIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfAdminStat.setStatus("current")


class _MyRipOffsetMetric_Type(Integer32):
    """Custom type myRipOffsetMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MyRipOffsetMetric_Type.__name__ = "Integer32"
_MyRipOffsetMetric_Object = MibScalar
myRipOffsetMetric = _MyRipOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 8),
    _MyRipOffsetMetric_Type()
)
myRipOffsetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipOffsetMetric.setStatus("current")


class _MyRipAdministrativeDistance_Type(Integer32):
    """Custom type myRipAdministrativeDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyRipAdministrativeDistance_Type.__name__ = "Integer32"
_MyRipAdministrativeDistance_Object = MibScalar
myRipAdministrativeDistance = _MyRipAdministrativeDistance_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 9),
    _MyRipAdministrativeDistance_Type()
)
myRipAdministrativeDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipAdministrativeDistance.setStatus("current")


class _MyRipValidateUpdateSrcEnable_Type(EnabledStatus):
    """Custom type myRipValidateUpdateSrcEnable based on EnabledStatus"""
    defaultValue = 1


_MyRipValidateUpdateSrcEnable_Type.__name__ = "EnabledStatus"
_MyRipValidateUpdateSrcEnable_Object = MibScalar
myRipValidateUpdateSrcEnable = _MyRipValidateUpdateSrcEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 10),
    _MyRipValidateUpdateSrcEnable_Type()
)
myRipValidateUpdateSrcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipValidateUpdateSrcEnable.setStatus("current")


class _MyRipPassiveStatus_Type(EnabledStatus):
    """Custom type myRipPassiveStatus based on EnabledStatus"""
    defaultValue = 2


_MyRipPassiveStatus_Type.__name__ = "EnabledStatus"
_MyRipPassiveStatus_Object = MibScalar
myRipPassiveStatus = _MyRipPassiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 11),
    _MyRipPassiveStatus_Type()
)
myRipPassiveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipPassiveStatus.setStatus("current")
_MyRipNextDueIn_Type = TimeTicks
_MyRipNextDueIn_Object = MibScalar
myRipNextDueIn = _MyRipNextDueIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 12),
    _MyRipNextDueIn_Type()
)
myRipNextDueIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipNextDueIn.setStatus("current")
_MyRipIfOffsetTable_Object = MibTable
myRipIfOffsetTable = _MyRipIfOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13)
)
if mibBuilder.loadTexts:
    myRipIfOffsetTable.setStatus("current")
_MyRipIfOffsetEntry_Object = MibTableRow
myRipIfOffsetEntry = _MyRipIfOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1)
)
myRipIfOffsetEntry.setIndexNames(
    (0, "MY-RIP-MIB", "myRipIfOffsetIfIndex"),
    (0, "MY-RIP-MIB", "myRipIfOffsetMethod"),
)
if mibBuilder.loadTexts:
    myRipIfOffsetEntry.setStatus("current")


class _MyRipIfOffsetIfIndex_Type(Integer32):
    """Custom type myRipIfOffsetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyRipIfOffsetIfIndex_Type.__name__ = "Integer32"
_MyRipIfOffsetIfIndex_Object = MibTableColumn
myRipIfOffsetIfIndex = _MyRipIfOffsetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 1),
    _MyRipIfOffsetIfIndex_Type()
)
myRipIfOffsetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfOffsetIfIndex.setStatus("current")


class _MyRipIfOffsetMethod_Type(Integer32):
    """Custom type myRipIfOffsetMethod based on Integer32"""
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


_MyRipIfOffsetMethod_Type.__name__ = "Integer32"
_MyRipIfOffsetMethod_Object = MibTableColumn
myRipIfOffsetMethod = _MyRipIfOffsetMethod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 2),
    _MyRipIfOffsetMethod_Type()
)
myRipIfOffsetMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipIfOffsetMethod.setStatus("current")


class _MyRipIfOffsetAclName_Type(DisplayString):
    """Custom type myRipIfOffsetAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyRipIfOffsetAclName_Type.__name__ = "DisplayString"
_MyRipIfOffsetAclName_Object = MibTableColumn
myRipIfOffsetAclName = _MyRipIfOffsetAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 3),
    _MyRipIfOffsetAclName_Type()
)
myRipIfOffsetAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfOffsetAclName.setStatus("current")


class _MyRipIfOffsetMetric_Type(Unsigned32):
    """Custom type myRipIfOffsetMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MyRipIfOffsetMetric_Type.__name__ = "Unsigned32"
_MyRipIfOffsetMetric_Object = MibTableColumn
myRipIfOffsetMetric = _MyRipIfOffsetMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 4),
    _MyRipIfOffsetMetric_Type()
)
myRipIfOffsetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myRipIfOffsetMetric.setStatus("current")
_MyRipIfOffsetStatus_Type = RowStatus
_MyRipIfOffsetStatus_Object = MibTableColumn
myRipIfOffsetStatus = _MyRipIfOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 13, 1, 5),
    _MyRipIfOffsetStatus_Type()
)
myRipIfOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRipIfOffsetStatus.setStatus("current")
_MyRipNetworkTable_Object = MibTable
myRipNetworkTable = _MyRipNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14)
)
if mibBuilder.loadTexts:
    myRipNetworkTable.setStatus("current")
_MyRipNetworkEntry_Object = MibTableRow
myRipNetworkEntry = _MyRipNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1)
)
myRipNetworkEntry.setIndexNames(
    (0, "MY-RIP-MIB", "myRipNetworkAddr"),
)
if mibBuilder.loadTexts:
    myRipNetworkEntry.setStatus("current")
_MyRipNetworkAddr_Type = IpAddress
_MyRipNetworkAddr_Object = MibTableColumn
myRipNetworkAddr = _MyRipNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 1),
    _MyRipNetworkAddr_Type()
)
myRipNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipNetworkAddr.setStatus("current")
_MyRipNetworkMask_Type = IpAddress
_MyRipNetworkMask_Object = MibTableColumn
myRipNetworkMask = _MyRipNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 2),
    _MyRipNetworkMask_Type()
)
myRipNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipNetworkMask.setStatus("current")
_MyRipNetworkStatus_Type = RowStatus
_MyRipNetworkStatus_Object = MibTableColumn
myRipNetworkStatus = _MyRipNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 14, 1, 3),
    _MyRipNetworkStatus_Type()
)
myRipNetworkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRipNetworkStatus.setStatus("current")
_MyRipNeighborTable_Object = MibTable
myRipNeighborTable = _MyRipNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15)
)
if mibBuilder.loadTexts:
    myRipNeighborTable.setStatus("current")
_MyRipNeighborEntry_Object = MibTableRow
myRipNeighborEntry = _MyRipNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1)
)
myRipNeighborEntry.setIndexNames(
    (0, "MY-RIP-MIB", "myRipNeighborIndex"),
)
if mibBuilder.loadTexts:
    myRipNeighborEntry.setStatus("current")
_MyRipNeighborIndex_Type = IpAddress
_MyRipNeighborIndex_Object = MibTableColumn
myRipNeighborIndex = _MyRipNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1, 1),
    _MyRipNeighborIndex_Type()
)
myRipNeighborIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myRipNeighborIndex.setStatus("current")
_MyRipNeighborStatus_Type = RowStatus
_MyRipNeighborStatus_Object = MibTableColumn
myRipNeighborStatus = _MyRipNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 1, 15, 1, 2),
    _MyRipNeighborStatus_Type()
)
myRipNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myRipNeighborStatus.setStatus("current")
_MyRIPMIBConformance_ObjectIdentity = ObjectIdentity
myRIPMIBConformance = _MyRIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2)
)
_MyRIPMIBCompliances_ObjectIdentity = ObjectIdentity
myRIPMIBCompliances = _MyRIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 1)
)
_MyRIPMIBGroups_ObjectIdentity = ObjectIdentity
myRIPMIBGroups = _MyRIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2)
)

# Managed Objects groups

myRipMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2, 1)
)
myRipMIBGroup.setObjects(
      *(("MY-RIP-MIB", "myRipEnable"),
        ("MY-RIP-MIB", "myRipUpdateTime"),
        ("MY-RIP-MIB", "myRipInvalidTime"),
        ("MY-RIP-MIB", "myRipHolddownTime"),
        ("MY-RIP-MIB", "myRipRecommendSetting"),
        ("MY-RIP-MIB", "myRipIfStatIfIndex"),
        ("MY-RIP-MIB", "myRipIfStatRcvBadPackets"),
        ("MY-RIP-MIB", "myRipIfStatRcvBadRoutes"),
        ("MY-RIP-MIB", "myRipIfStatSentUpdates"),
        ("MY-RIP-MIB", "myRipIfConfIfIndex"),
        ("MY-RIP-MIB", "myRipIfConfAuthType"),
        ("MY-RIP-MIB", "myRipIfConfAuthKeyChain"),
        ("MY-RIP-MIB", "myRipIfConfSend"),
        ("MY-RIP-MIB", "myRipIfConfReceive"),
        ("MY-RIP-MIB", "myRipIfPassiveStatus"),
        ("MY-RIP-MIB", "myRipIfBroadcastEnable"),
        ("MY-RIP-MIB", "myRipIfAdminStat"),
        ("MY-RIP-MIB", "myRipOffsetMetric"),
        ("MY-RIP-MIB", "myRipAdministrativeDistance"),
        ("MY-RIP-MIB", "myRipValidateUpdateSrcEnable"))
)
if mibBuilder.loadTexts:
    myRipMIBGroup.setStatus("current")

myRIPExtendMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 2, 2)
)
myRIPExtendMIBGroup.setObjects(
      *(("MY-RIP-MIB", "myRipNextDueIn"),
        ("MY-RIP-MIB", "myRipIfOffsetIfIndex"),
        ("MY-RIP-MIB", "myRipIfOffsetMethod"),
        ("MY-RIP-MIB", "myRipIfOffsetAclName"),
        ("MY-RIP-MIB", "myRipIfOffsetMetric"),
        ("MY-RIP-MIB", "myRipIfOffsetStatus"),
        ("MY-RIP-MIB", "myRipNetworkAddr"),
        ("MY-RIP-MIB", "myRipNetworkMask"),
        ("MY-RIP-MIB", "myRipNetworkStatus"),
        ("MY-RIP-MIB", "myRipNeighborIndex"),
        ("MY-RIP-MIB", "myRipNeighborStatus"))
)
if mibBuilder.loadTexts:
    myRIPExtendMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myRIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 13, 2, 1, 1)
)
myRIPMIBCompliance.setObjects(
      *(("MY-RIP-MIB", "myRipMIBGroup"),
        ("MY-RIP-MIB", "myRIPExtendMIBGroup"))
)
if mibBuilder.loadTexts:
    myRIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-RIP-MIB",
    **{"myRIPMIB": myRIPMIB,
       "myRIPMIBObjects": myRIPMIBObjects,
       "myRipEnable": myRipEnable,
       "myRipUpdateTime": myRipUpdateTime,
       "myRipInvalidTime": myRipInvalidTime,
       "myRipHolddownTime": myRipHolddownTime,
       "myRipRecommendSetting": myRipRecommendSetting,
       "myRipIfStatTable": myRipIfStatTable,
       "myRipIfStatEntry": myRipIfStatEntry,
       "myRipIfStatIfIndex": myRipIfStatIfIndex,
       "myRipIfStatRcvBadPackets": myRipIfStatRcvBadPackets,
       "myRipIfStatRcvBadRoutes": myRipIfStatRcvBadRoutes,
       "myRipIfStatSentUpdates": myRipIfStatSentUpdates,
       "myRipIfConfTable": myRipIfConfTable,
       "myRipIfConfEntry": myRipIfConfEntry,
       "myRipIfConfIfIndex": myRipIfConfIfIndex,
       "myRipIfConfAuthType": myRipIfConfAuthType,
       "myRipIfConfAuthKeyChain": myRipIfConfAuthKeyChain,
       "myRipIfConfSend": myRipIfConfSend,
       "myRipIfConfReceive": myRipIfConfReceive,
       "myRipIfPassiveStatus": myRipIfPassiveStatus,
       "myRipIfBroadcastEnable": myRipIfBroadcastEnable,
       "myRipIfAdminStat": myRipIfAdminStat,
       "myRipOffsetMetric": myRipOffsetMetric,
       "myRipAdministrativeDistance": myRipAdministrativeDistance,
       "myRipValidateUpdateSrcEnable": myRipValidateUpdateSrcEnable,
       "myRipPassiveStatus": myRipPassiveStatus,
       "myRipNextDueIn": myRipNextDueIn,
       "myRipIfOffsetTable": myRipIfOffsetTable,
       "myRipIfOffsetEntry": myRipIfOffsetEntry,
       "myRipIfOffsetIfIndex": myRipIfOffsetIfIndex,
       "myRipIfOffsetMethod": myRipIfOffsetMethod,
       "myRipIfOffsetAclName": myRipIfOffsetAclName,
       "myRipIfOffsetMetric": myRipIfOffsetMetric,
       "myRipIfOffsetStatus": myRipIfOffsetStatus,
       "myRipNetworkTable": myRipNetworkTable,
       "myRipNetworkEntry": myRipNetworkEntry,
       "myRipNetworkAddr": myRipNetworkAddr,
       "myRipNetworkMask": myRipNetworkMask,
       "myRipNetworkStatus": myRipNetworkStatus,
       "myRipNeighborTable": myRipNeighborTable,
       "myRipNeighborEntry": myRipNeighborEntry,
       "myRipNeighborIndex": myRipNeighborIndex,
       "myRipNeighborStatus": myRipNeighborStatus,
       "myRIPMIBConformance": myRIPMIBConformance,
       "myRIPMIBCompliances": myRIPMIBCompliances,
       "myRIPMIBCompliance": myRIPMIBCompliance,
       "myRIPMIBGroups": myRIPMIBGroups,
       "myRipMIBGroup": myRipMIBGroup,
       "myRIPExtendMIBGroup": myRIPExtendMIBGroup}
)
