# SNMP MIB module (DC-L2VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-L2VPN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:11 2025
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

(AdminStatus,
 MjStatus,
 NpgOperStatus,
 NumericIndex,
 OperStatus,
 SjStatus) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "AdminStatus",
    "MjStatus",
    "NpgOperStatus",
    "NumericIndex",
    "OperStatus",
    "SjStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

l2vpnMib = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class L2vmMjIfId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(696844288,
              697761792,
              1921384448)
        )
    )
    namedValues = NamedValues(
        *(("ifAtgI3", 696844288),
          ("ifAtgBdpi", 697761792),
          ("ifAtgPvpi", 1921384448))
    )



class L2vmSjIfId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1031864320
        )
    )
    namedValues = NamedValues(
        ("ifAtgRpi", 1031864320)
    )



class L2vpnADType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("bgp", 2))
    )



class L2vpnSigType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ldp", 2),
          ("bgp", 3))
    )



class L2vpnPwBindType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwMibIndex", 1),
          ("lclRmtVeId", 2))
    )



class L2vpnType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("vpls", 1),
          ("vpws", 2))
    )



class L2vpnSiteId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class L2vpnVeIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class BgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class BgpExtendedCommunity(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class BgpRouteTargetType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )



# MIB Managed Objects in the order of their OIDs

_L2vpnObjects_ObjectIdentity = ObjectIdentity
l2vpnObjects = _L2vpnObjects_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1)
)
_L2vmEntityTable_Object = MibTable
l2vmEntityTable = _L2vmEntityTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    l2vmEntityTable.setStatus("current")
_L2vmEntityEntry_Object = MibTableRow
l2vmEntityEntry = _L2vmEntityEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1)
)
l2vmEntityEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
)
if mibBuilder.loadTexts:
    l2vmEntityEntry.setStatus("current")
_L2vmEntityIndex_Type = NumericIndex
_L2vmEntityIndex_Object = MibTableColumn
l2vmEntityIndex = _L2vmEntityIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 1),
    _L2vmEntityIndex_Type()
)
l2vmEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmEntityIndex.setStatus("current")
_L2vmEntityRowStatus_Type = RowStatus
_L2vmEntityRowStatus_Object = MibTableColumn
l2vmEntityRowStatus = _L2vmEntityRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 2),
    _L2vmEntityRowStatus_Type()
)
l2vmEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRowStatus.setStatus("current")


class _L2vmEntityAdminStatus_Type(AdminStatus):
    """Custom type l2vmEntityAdminStatus based on AdminStatus"""
    defaultValue = 1


_L2vmEntityAdminStatus_Type.__name__ = "AdminStatus"
_L2vmEntityAdminStatus_Object = MibTableColumn
l2vmEntityAdminStatus = _L2vmEntityAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 3),
    _L2vmEntityAdminStatus_Type()
)
l2vmEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityAdminStatus.setStatus("current")
_L2vmEntityOperStatus_Type = NpgOperStatus
_L2vmEntityOperStatus_Object = MibTableColumn
l2vmEntityOperStatus = _L2vmEntityOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 4),
    _L2vmEntityOperStatus_Type()
)
l2vmEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmEntityOperStatus.setStatus("current")
_L2vmEntityVplsIndexNext_Type = NumericIndex
_L2vmEntityVplsIndexNext_Object = MibTableColumn
l2vmEntityVplsIndexNext = _L2vmEntityVplsIndexNext_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 5),
    _L2vmEntityVplsIndexNext_Type()
)
l2vmEntityVplsIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmEntityVplsIndexNext.setStatus("current")
_L2vmEntityVpwsIndexNext_Type = NumericIndex
_L2vmEntityVpwsIndexNext_Object = MibTableColumn
l2vmEntityVpwsIndexNext = _L2vmEntityVpwsIndexNext_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 6),
    _L2vmEntityVpwsIndexNext_Type()
)
l2vmEntityVpwsIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmEntityVpwsIndexNext.setStatus("current")


class _L2vmEntityNbasePriority_Type(Integer32):
    """Custom type l2vmEntityNbasePriority based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_L2vmEntityNbasePriority_Type.__name__ = "Integer32"
_L2vmEntityNbasePriority_Object = MibTableColumn
l2vmEntityNbasePriority = _L2vmEntityNbasePriority_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 7),
    _L2vmEntityNbasePriority_Type()
)
l2vmEntityNbasePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityNbasePriority.setStatus("current")


class _L2vmEntityTimerGranularity_Type(Integer32):
    """Custom type l2vmEntityTimerGranularity based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_L2vmEntityTimerGranularity_Type.__name__ = "Integer32"
_L2vmEntityTimerGranularity_Object = MibTableColumn
l2vmEntityTimerGranularity = _L2vmEntityTimerGranularity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 8),
    _L2vmEntityTimerGranularity_Type()
)
l2vmEntityTimerGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityTimerGranularity.setStatus("current")


class _L2vmEntityRestartDuration_Type(TimeTicks):
    """Custom type l2vmEntityRestartDuration based on TimeTicks"""
    defaultValue = 18000


_L2vmEntityRestartDuration_Type.__name__ = "TimeTicks"
_L2vmEntityRestartDuration_Object = MibTableColumn
l2vmEntityRestartDuration = _L2vmEntityRestartDuration_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 9),
    _L2vmEntityRestartDuration_Type()
)
l2vmEntityRestartDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRestartDuration.setStatus("current")


class _L2vmEntityRescheduleLimit_Type(Integer32):
    """Custom type l2vmEntityRescheduleLimit based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2vmEntityRescheduleLimit_Type.__name__ = "Integer32"
_L2vmEntityRescheduleLimit_Object = MibTableColumn
l2vmEntityRescheduleLimit = _L2vmEntityRescheduleLimit_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 10),
    _L2vmEntityRescheduleLimit_Type()
)
l2vmEntityRescheduleLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRescheduleLimit.setStatus("current")


class _L2vmEntityPvpiBufferPoolSize_Type(Integer32):
    """Custom type l2vmEntityPvpiBufferPoolSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_L2vmEntityPvpiBufferPoolSize_Type.__name__ = "Integer32"
_L2vmEntityPvpiBufferPoolSize_Object = MibTableColumn
l2vmEntityPvpiBufferPoolSize = _L2vmEntityPvpiBufferPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 11),
    _L2vmEntityPvpiBufferPoolSize_Type()
)
l2vmEntityPvpiBufferPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityPvpiBufferPoolSize.setStatus("current")


class _L2vmEntityRpiBufferPoolSize_Type(Integer32):
    """Custom type l2vmEntityRpiBufferPoolSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_L2vmEntityRpiBufferPoolSize_Type.__name__ = "Integer32"
_L2vmEntityRpiBufferPoolSize_Object = MibTableColumn
l2vmEntityRpiBufferPoolSize = _L2vmEntityRpiBufferPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 12),
    _L2vmEntityRpiBufferPoolSize_Type()
)
l2vmEntityRpiBufferPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRpiBufferPoolSize.setStatus("current")


class _L2vmEntityRpiFailTimeout_Type(TimeTicks):
    """Custom type l2vmEntityRpiFailTimeout based on TimeTicks"""
    defaultValue = 3000


_L2vmEntityRpiFailTimeout_Type.__name__ = "TimeTicks"
_L2vmEntityRpiFailTimeout_Object = MibTableColumn
l2vmEntityRpiFailTimeout = _L2vmEntityRpiFailTimeout_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 13),
    _L2vmEntityRpiFailTimeout_Type()
)
l2vmEntityRpiFailTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRpiFailTimeout.setStatus("current")


class _L2vmEntityRetryInterval_Type(TimeTicks):
    """Custom type l2vmEntityRetryInterval based on TimeTicks"""
    defaultValue = 1000


_L2vmEntityRetryInterval_Type.__name__ = "TimeTicks"
_L2vmEntityRetryInterval_Object = MibTableColumn
l2vmEntityRetryInterval = _L2vmEntityRetryInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 14),
    _L2vmEntityRetryInterval_Type()
)
l2vmEntityRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityRetryInterval.setStatus("current")


class _L2vmEntityVpnNotifEnable_Type(TruthValue):
    """Custom type l2vmEntityVpnNotifEnable based on TruthValue"""
    defaultValue = 2


_L2vmEntityVpnNotifEnable_Type.__name__ = "TruthValue"
_L2vmEntityVpnNotifEnable_Object = MibTableColumn
l2vmEntityVpnNotifEnable = _L2vmEntityVpnNotifEnable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 15),
    _L2vmEntityVpnNotifEnable_Type()
)
l2vmEntityVpnNotifEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityVpnNotifEnable.setStatus("current")


class _L2vmEntityVpnNotifBufferPoolSize_Type(Integer32):
    """Custom type l2vmEntityVpnNotifBufferPoolSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_L2vmEntityVpnNotifBufferPoolSize_Type.__name__ = "Integer32"
_L2vmEntityVpnNotifBufferPoolSize_Object = MibTableColumn
l2vmEntityVpnNotifBufferPoolSize = _L2vmEntityVpnNotifBufferPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 16),
    _L2vmEntityVpnNotifBufferPoolSize_Type()
)
l2vmEntityVpnNotifBufferPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityVpnNotifBufferPoolSize.setStatus("current")


class _L2vmEntitySupportVpls_Type(TruthValue):
    """Custom type l2vmEntitySupportVpls based on TruthValue"""
    defaultValue = 2


_L2vmEntitySupportVpls_Type.__name__ = "TruthValue"
_L2vmEntitySupportVpls_Object = MibTableColumn
l2vmEntitySupportVpls = _L2vmEntitySupportVpls_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 17),
    _L2vmEntitySupportVpls_Type()
)
l2vmEntitySupportVpls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntitySupportVpls.setStatus("current")


class _L2vmEntityBdpiBufferPoolSize_Type(Integer32):
    """Custom type l2vmEntityBdpiBufferPoolSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_L2vmEntityBdpiBufferPoolSize_Type.__name__ = "Integer32"
_L2vmEntityBdpiBufferPoolSize_Object = MibTableColumn
l2vmEntityBdpiBufferPoolSize = _L2vmEntityBdpiBufferPoolSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 1, 1, 18),
    _L2vmEntityBdpiBufferPoolSize_Type()
)
l2vmEntityBdpiBufferPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmEntityBdpiBufferPoolSize.setStatus("current")
_L2vmMjTable_Object = MibTable
l2vmMjTable = _L2vmMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    l2vmMjTable.setStatus("current")
_L2vmMjEntry_Object = MibTableRow
l2vmMjEntry = _L2vmMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1)
)
l2vmMjEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-L2VPN-MIB", "l2vmMjInterfaceId"),
    (0, "DC-L2VPN-MIB", "l2vmMjPartnerType"),
    (0, "DC-L2VPN-MIB", "l2vmMjPartnerIndex"),
    (0, "DC-L2VPN-MIB", "l2vmMjSubIndex"),
)
if mibBuilder.loadTexts:
    l2vmMjEntry.setStatus("current")
_L2vmMjInterfaceId_Type = L2vmMjIfId
_L2vmMjInterfaceId_Object = MibTableColumn
l2vmMjInterfaceId = _L2vmMjInterfaceId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 2),
    _L2vmMjInterfaceId_Type()
)
l2vmMjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmMjInterfaceId.setStatus("current")
_L2vmMjPartnerType_Type = Unsigned32
_L2vmMjPartnerType_Object = MibTableColumn
l2vmMjPartnerType = _L2vmMjPartnerType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 3),
    _L2vmMjPartnerType_Type()
)
l2vmMjPartnerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmMjPartnerType.setStatus("current")


class _L2vmMjPartnerIndex_Type(Unsigned32):
    """Custom type l2vmMjPartnerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2vmMjPartnerIndex_Type.__name__ = "Unsigned32"
_L2vmMjPartnerIndex_Object = MibTableColumn
l2vmMjPartnerIndex = _L2vmMjPartnerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 4),
    _L2vmMjPartnerIndex_Type()
)
l2vmMjPartnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmMjPartnerIndex.setStatus("current")
_L2vmMjSubIndex_Type = Unsigned32
_L2vmMjSubIndex_Object = MibTableColumn
l2vmMjSubIndex = _L2vmMjSubIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 5),
    _L2vmMjSubIndex_Type()
)
l2vmMjSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmMjSubIndex.setStatus("current")
_L2vmMjRowStatus_Type = RowStatus
_L2vmMjRowStatus_Object = MibTableColumn
l2vmMjRowStatus = _L2vmMjRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 6),
    _L2vmMjRowStatus_Type()
)
l2vmMjRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmMjRowStatus.setStatus("current")


class _L2vmMjAdminStatus_Type(AdminStatus):
    """Custom type l2vmMjAdminStatus based on AdminStatus"""
    defaultValue = 1


_L2vmMjAdminStatus_Type.__name__ = "AdminStatus"
_L2vmMjAdminStatus_Object = MibTableColumn
l2vmMjAdminStatus = _L2vmMjAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 7),
    _L2vmMjAdminStatus_Type()
)
l2vmMjAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmMjAdminStatus.setStatus("current")
_L2vmMjOperStatus_Type = OperStatus
_L2vmMjOperStatus_Object = MibTableColumn
l2vmMjOperStatus = _L2vmMjOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 8),
    _L2vmMjOperStatus_Type()
)
l2vmMjOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmMjOperStatus.setStatus("current")
_L2vmMjJoinStatus_Type = MjStatus
_L2vmMjJoinStatus_Object = MibTableColumn
l2vmMjJoinStatus = _L2vmMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 2, 1, 9),
    _L2vmMjJoinStatus_Type()
)
l2vmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmMjJoinStatus.setStatus("current")
_L2vmSjTable_Object = MibTable
l2vmSjTable = _L2vmSjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    l2vmSjTable.setStatus("current")
_L2vmSjEntry_Object = MibTableRow
l2vmSjEntry = _L2vmSjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1)
)
l2vmSjEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-L2VPN-MIB", "l2vmSjInterfaceId"),
    (0, "DC-L2VPN-MIB", "l2vmSjPartnerType"),
    (0, "DC-L2VPN-MIB", "l2vmSjPartnerIndex"),
    (0, "DC-L2VPN-MIB", "l2vmSjSubIndex"),
)
if mibBuilder.loadTexts:
    l2vmSjEntry.setStatus("current")
_L2vmSjInterfaceId_Type = L2vmSjIfId
_L2vmSjInterfaceId_Object = MibTableColumn
l2vmSjInterfaceId = _L2vmSjInterfaceId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 2),
    _L2vmSjInterfaceId_Type()
)
l2vmSjInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmSjInterfaceId.setStatus("current")
_L2vmSjPartnerType_Type = Unsigned32
_L2vmSjPartnerType_Object = MibTableColumn
l2vmSjPartnerType = _L2vmSjPartnerType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 3),
    _L2vmSjPartnerType_Type()
)
l2vmSjPartnerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmSjPartnerType.setStatus("current")


class _L2vmSjPartnerIndex_Type(Unsigned32):
    """Custom type l2vmSjPartnerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_L2vmSjPartnerIndex_Type.__name__ = "Unsigned32"
_L2vmSjPartnerIndex_Object = MibTableColumn
l2vmSjPartnerIndex = _L2vmSjPartnerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 4),
    _L2vmSjPartnerIndex_Type()
)
l2vmSjPartnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmSjPartnerIndex.setStatus("current")
_L2vmSjSubIndex_Type = Unsigned32
_L2vmSjSubIndex_Object = MibTableColumn
l2vmSjSubIndex = _L2vmSjSubIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 5),
    _L2vmSjSubIndex_Type()
)
l2vmSjSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmSjSubIndex.setStatus("current")
_L2vmSjJoinStatus_Type = SjStatus
_L2vmSjJoinStatus_Object = MibTableColumn
l2vmSjJoinStatus = _L2vmSjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 3, 1, 6),
    _L2vmSjJoinStatus_Type()
)
l2vmSjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmSjJoinStatus.setStatus("current")
_L2vmBgpRTCfgTable_Object = MibTable
l2vmBgpRTCfgTable = _L2vmBgpRTCfgTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    l2vmBgpRTCfgTable.setStatus("current")
_L2vmBgpRTCfgEntry_Object = MibTableRow
l2vmBgpRTCfgEntry = _L2vmBgpRTCfgEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1)
)
l2vmBgpRTCfgEntry.setIndexNames(
    (0, "DC-L2VPN-MIB", "l2vmEntityIndex"),
    (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgVpnType"),
    (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgVpnIndex"),
    (0, "DC-L2VPN-MIB", "l2vmBgpRTCfgIndex"),
)
if mibBuilder.loadTexts:
    l2vmBgpRTCfgEntry.setStatus("current")
_L2vmBgpRTCfgVpnType_Type = L2vpnType
_L2vmBgpRTCfgVpnType_Object = MibTableColumn
l2vmBgpRTCfgVpnType = _L2vmBgpRTCfgVpnType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 2),
    _L2vmBgpRTCfgVpnType_Type()
)
l2vmBgpRTCfgVpnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgVpnType.setStatus("current")
_L2vmBgpRTCfgVpnIndex_Type = NumericIndex
_L2vmBgpRTCfgVpnIndex_Object = MibTableColumn
l2vmBgpRTCfgVpnIndex = _L2vmBgpRTCfgVpnIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 3),
    _L2vmBgpRTCfgVpnIndex_Type()
)
l2vmBgpRTCfgVpnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgVpnIndex.setStatus("current")
_L2vmBgpRTCfgIndex_Type = NumericIndex
_L2vmBgpRTCfgIndex_Object = MibTableColumn
l2vmBgpRTCfgIndex = _L2vmBgpRTCfgIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 4),
    _L2vmBgpRTCfgIndex_Type()
)
l2vmBgpRTCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgIndex.setStatus("current")
_L2vmBgpRTCfgRowStatus_Type = RowStatus
_L2vmBgpRTCfgRowStatus_Object = MibTableColumn
l2vmBgpRTCfgRowStatus = _L2vmBgpRTCfgRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 5),
    _L2vmBgpRTCfgRowStatus_Type()
)
l2vmBgpRTCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgRowStatus.setStatus("current")


class _L2vmBgpRTCfgAdminStatus_Type(AdminStatus):
    """Custom type l2vmBgpRTCfgAdminStatus based on AdminStatus"""
    defaultValue = 1


_L2vmBgpRTCfgAdminStatus_Type.__name__ = "AdminStatus"
_L2vmBgpRTCfgAdminStatus_Object = MibTableColumn
l2vmBgpRTCfgAdminStatus = _L2vmBgpRTCfgAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 6),
    _L2vmBgpRTCfgAdminStatus_Type()
)
l2vmBgpRTCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgAdminStatus.setStatus("current")
_L2vmBgpRTCfgOperStatus_Type = NpgOperStatus
_L2vmBgpRTCfgOperStatus_Object = MibTableColumn
l2vmBgpRTCfgOperStatus = _L2vmBgpRTCfgOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 7),
    _L2vmBgpRTCfgOperStatus_Type()
)
l2vmBgpRTCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgOperStatus.setStatus("current")


class _L2vmBgpRTCfgType_Type(BgpRouteTargetType):
    """Custom type l2vmBgpRTCfgType based on BgpRouteTargetType"""
    defaultValue = 3


_L2vmBgpRTCfgType_Type.__name__ = "BgpRouteTargetType"
_L2vmBgpRTCfgType_Object = MibTableColumn
l2vmBgpRTCfgType = _L2vmBgpRTCfgType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 8),
    _L2vmBgpRTCfgType_Type()
)
l2vmBgpRTCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgType.setStatus("current")


class _L2vmBgpRTCfgRT_Type(BgpExtendedCommunity):
    """Custom type l2vmBgpRTCfgRT based on BgpExtendedCommunity"""
    defaultHexValue = "0000000000000000"


_L2vmBgpRTCfgRT_Type.__name__ = "BgpExtendedCommunity"
_L2vmBgpRTCfgRT_Object = MibTableColumn
l2vmBgpRTCfgRT = _L2vmBgpRTCfgRT_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 1, 4, 1, 9),
    _L2vmBgpRTCfgRT_Type()
)
l2vmBgpRTCfgRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2vmBgpRTCfgRT.setStatus("current")
_L2vpnConformance_ObjectIdentity = ObjectIdentity
l2vpnConformance = _L2vpnConformance_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2)
)
_L2vpnCompliances_ObjectIdentity = ObjectIdentity
l2vpnCompliances = _L2vpnCompliances_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1)
)
_L2vpnGroups_ObjectIdentity = ObjectIdentity
l2vpnGroups = _L2vpnGroups_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2)
)

# Managed Objects groups

l2vpnFrameworkGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2, 1)
)
l2vpnFrameworkGroup.setObjects(
      *(("DC-L2VPN-MIB", "l2vmEntityRowStatus"),
        ("DC-L2VPN-MIB", "l2vmEntityAdminStatus"),
        ("DC-L2VPN-MIB", "l2vmEntityOperStatus"),
        ("DC-L2VPN-MIB", "l2vmEntityVplsIndexNext"),
        ("DC-L2VPN-MIB", "l2vmEntityVpwsIndexNext"),
        ("DC-L2VPN-MIB", "l2vmEntityNbasePriority"),
        ("DC-L2VPN-MIB", "l2vmEntityTimerGranularity"),
        ("DC-L2VPN-MIB", "l2vmEntityRestartDuration"),
        ("DC-L2VPN-MIB", "l2vmEntityRescheduleLimit"),
        ("DC-L2VPN-MIB", "l2vmEntityPvpiBufferPoolSize"),
        ("DC-L2VPN-MIB", "l2vmEntityRpiBufferPoolSize"),
        ("DC-L2VPN-MIB", "l2vmEntityRpiFailTimeout"),
        ("DC-L2VPN-MIB", "l2vmEntityRetryInterval"),
        ("DC-L2VPN-MIB", "l2vmEntityVpnNotifEnable"),
        ("DC-L2VPN-MIB", "l2vmEntityVpnNotifBufferPoolSize"),
        ("DC-L2VPN-MIB", "l2vmEntitySupportVpls"),
        ("DC-L2VPN-MIB", "l2vmEntityBdpiBufferPoolSize"),
        ("DC-L2VPN-MIB", "l2vmMjRowStatus"),
        ("DC-L2VPN-MIB", "l2vmMjAdminStatus"),
        ("DC-L2VPN-MIB", "l2vmMjOperStatus"),
        ("DC-L2VPN-MIB", "l2vmMjJoinStatus"),
        ("DC-L2VPN-MIB", "l2vmSjJoinStatus"))
)
if mibBuilder.loadTexts:
    l2vpnFrameworkGroup.setStatus("current")

l2vmBgpADGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 2, 2)
)
l2vmBgpADGroup.setObjects(
      *(("DC-L2VPN-MIB", "l2vmBgpRTCfgRowStatus"),
        ("DC-L2VPN-MIB", "l2vmBgpRTCfgAdminStatus"),
        ("DC-L2VPN-MIB", "l2vmBgpRTCfgOperStatus"),
        ("DC-L2VPN-MIB", "l2vmBgpRTCfgType"),
        ("DC-L2VPN-MIB", "l2vmBgpRTCfgRT"))
)
if mibBuilder.loadTexts:
    l2vmBgpADGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

l2vpnFrameworkCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1, 1)
)
l2vpnFrameworkCompliance.setObjects(
    ("DC-L2VPN-MIB", "l2vpnFrameworkGroup")
)
if mibBuilder.loadTexts:
    l2vpnFrameworkCompliance.setStatus(
        "current"
    )

l2vmBgpADCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 94, 2, 1, 2, 1, 2)
)
l2vmBgpADCompliance.setObjects(
      *(("DC-L2VPN-MIB", "l2vpnFrameworkGroup"),
        ("DC-L2VPN-MIB", "l2vmBgpADGroup"))
)
if mibBuilder.loadTexts:
    l2vmBgpADCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-L2VPN-MIB",
    **{"L2vmMjIfId": L2vmMjIfId,
       "L2vmSjIfId": L2vmSjIfId,
       "L2vpnADType": L2vpnADType,
       "L2vpnSigType": L2vpnSigType,
       "L2vpnPwBindType": L2vpnPwBindType,
       "L2vpnType": L2vpnType,
       "L2vpnSiteId": L2vpnSiteId,
       "L2vpnVeIdOrZero": L2vpnVeIdOrZero,
       "BgpRouteDistinguisher": BgpRouteDistinguisher,
       "BgpExtendedCommunity": BgpExtendedCommunity,
       "BgpRouteTargetType": BgpRouteTargetType,
       "l2vpnMib": l2vpnMib,
       "l2vpnObjects": l2vpnObjects,
       "l2vmEntityTable": l2vmEntityTable,
       "l2vmEntityEntry": l2vmEntityEntry,
       "l2vmEntityIndex": l2vmEntityIndex,
       "l2vmEntityRowStatus": l2vmEntityRowStatus,
       "l2vmEntityAdminStatus": l2vmEntityAdminStatus,
       "l2vmEntityOperStatus": l2vmEntityOperStatus,
       "l2vmEntityVplsIndexNext": l2vmEntityVplsIndexNext,
       "l2vmEntityVpwsIndexNext": l2vmEntityVpwsIndexNext,
       "l2vmEntityNbasePriority": l2vmEntityNbasePriority,
       "l2vmEntityTimerGranularity": l2vmEntityTimerGranularity,
       "l2vmEntityRestartDuration": l2vmEntityRestartDuration,
       "l2vmEntityRescheduleLimit": l2vmEntityRescheduleLimit,
       "l2vmEntityPvpiBufferPoolSize": l2vmEntityPvpiBufferPoolSize,
       "l2vmEntityRpiBufferPoolSize": l2vmEntityRpiBufferPoolSize,
       "l2vmEntityRpiFailTimeout": l2vmEntityRpiFailTimeout,
       "l2vmEntityRetryInterval": l2vmEntityRetryInterval,
       "l2vmEntityVpnNotifEnable": l2vmEntityVpnNotifEnable,
       "l2vmEntityVpnNotifBufferPoolSize": l2vmEntityVpnNotifBufferPoolSize,
       "l2vmEntitySupportVpls": l2vmEntitySupportVpls,
       "l2vmEntityBdpiBufferPoolSize": l2vmEntityBdpiBufferPoolSize,
       "l2vmMjTable": l2vmMjTable,
       "l2vmMjEntry": l2vmMjEntry,
       "l2vmMjInterfaceId": l2vmMjInterfaceId,
       "l2vmMjPartnerType": l2vmMjPartnerType,
       "l2vmMjPartnerIndex": l2vmMjPartnerIndex,
       "l2vmMjSubIndex": l2vmMjSubIndex,
       "l2vmMjRowStatus": l2vmMjRowStatus,
       "l2vmMjAdminStatus": l2vmMjAdminStatus,
       "l2vmMjOperStatus": l2vmMjOperStatus,
       "l2vmMjJoinStatus": l2vmMjJoinStatus,
       "l2vmSjTable": l2vmSjTable,
       "l2vmSjEntry": l2vmSjEntry,
       "l2vmSjInterfaceId": l2vmSjInterfaceId,
       "l2vmSjPartnerType": l2vmSjPartnerType,
       "l2vmSjPartnerIndex": l2vmSjPartnerIndex,
       "l2vmSjSubIndex": l2vmSjSubIndex,
       "l2vmSjJoinStatus": l2vmSjJoinStatus,
       "l2vmBgpRTCfgTable": l2vmBgpRTCfgTable,
       "l2vmBgpRTCfgEntry": l2vmBgpRTCfgEntry,
       "l2vmBgpRTCfgVpnType": l2vmBgpRTCfgVpnType,
       "l2vmBgpRTCfgVpnIndex": l2vmBgpRTCfgVpnIndex,
       "l2vmBgpRTCfgIndex": l2vmBgpRTCfgIndex,
       "l2vmBgpRTCfgRowStatus": l2vmBgpRTCfgRowStatus,
       "l2vmBgpRTCfgAdminStatus": l2vmBgpRTCfgAdminStatus,
       "l2vmBgpRTCfgOperStatus": l2vmBgpRTCfgOperStatus,
       "l2vmBgpRTCfgType": l2vmBgpRTCfgType,
       "l2vmBgpRTCfgRT": l2vmBgpRTCfgRT,
       "l2vpnConformance": l2vpnConformance,
       "l2vpnCompliances": l2vpnCompliances,
       "l2vpnFrameworkCompliance": l2vpnFrameworkCompliance,
       "l2vmBgpADCompliance": l2vmBgpADCompliance,
       "l2vpnGroups": l2vpnGroups,
       "l2vpnFrameworkGroup": l2vpnFrameworkGroup,
       "l2vmBgpADGroup": l2vmBgpADGroup}
)
