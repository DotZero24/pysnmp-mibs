# SNMP MIB module (ZTE-AN-ACCESS-CTRL-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ACCESS-CTRL-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:46 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnAccessCtrlRadiusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91)
)
if mibBuilder.loadTexts:
    zxAnAccessCtrlRadiusMib.setRevisions(
        ("2012-11-07 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnRadiusGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnRadiusGlobalObjects = _ZxAnRadiusGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 1)
)


class _ZxAnRadiusVendorIdEnable_Type(Integer32):
    """Custom type zxAnRadiusVendorIdEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnRadiusVendorIdEnable_Type.__name__ = "Integer32"
_ZxAnRadiusVendorIdEnable_Object = MibScalar
zxAnRadiusVendorIdEnable = _ZxAnRadiusVendorIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 1, 1),
    _ZxAnRadiusVendorIdEnable_Type()
)
zxAnRadiusVendorIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRadiusVendorIdEnable.setStatus("current")
_ZxAnRadiusAuthenticationObjects_ObjectIdentity = ObjectIdentity
zxAnRadiusAuthenticationObjects = _ZxAnRadiusAuthenticationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2)
)
_ZxAnRadiusAuthenGroup_ObjectIdentity = ObjectIdentity
zxAnRadiusAuthenGroup = _ZxAnRadiusAuthenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2)
)
_ZxAnRadiusAuthenGroupTable_Object = MibTable
zxAnRadiusAuthenGroupTable = _ZxAnRadiusAuthenGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupTable.setStatus("current")
_ZxAnRadiusAuthenGroupEntry_Object = MibTableRow
zxAnRadiusAuthenGroupEntry = _ZxAnRadiusAuthenGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1)
)
zxAnRadiusAuthenGroupEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAuthenGroupId"),
)
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupEntry.setStatus("current")


class _ZxAnRadiusAuthenGroupId_Type(Integer32):
    """Custom type zxAnRadiusAuthenGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnRadiusAuthenGroupId_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenGroupId_Object = MibTableColumn
zxAnRadiusAuthenGroupId = _ZxAnRadiusAuthenGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 1),
    _ZxAnRadiusAuthenGroupId_Type()
)
zxAnRadiusAuthenGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupId.setStatus("current")


class _ZxAnRadiusAuthenGroupAlgorithm_Type(Integer32):
    """Custom type zxAnRadiusAuthenGroupAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterBackup", 1),
          ("roundRobin", 2))
    )


_ZxAnRadiusAuthenGroupAlgorithm_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenGroupAlgorithm_Object = MibTableColumn
zxAnRadiusAuthenGroupAlgorithm = _ZxAnRadiusAuthenGroupAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 2),
    _ZxAnRadiusAuthenGroupAlgorithm_Type()
)
zxAnRadiusAuthenGroupAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupAlgorithm.setStatus("current")


class _ZxAnRadiusAuthenGroupDeadTime_Type(Integer32):
    """Custom type zxAnRadiusAuthenGroupDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnRadiusAuthenGroupDeadTime_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenGroupDeadTime_Object = MibTableColumn
zxAnRadiusAuthenGroupDeadTime = _ZxAnRadiusAuthenGroupDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 3),
    _ZxAnRadiusAuthenGroupDeadTime_Type()
)
zxAnRadiusAuthenGroupDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupDeadTime.setUnits("minutes")


class _ZxAnRadiusAuthenGroupRetries_Type(Integer32):
    """Custom type zxAnRadiusAuthenGroupRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnRadiusAuthenGroupRetries_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenGroupRetries_Object = MibTableColumn
zxAnRadiusAuthenGroupRetries = _ZxAnRadiusAuthenGroupRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 4),
    _ZxAnRadiusAuthenGroupRetries_Type()
)
zxAnRadiusAuthenGroupRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupRetries.setStatus("current")


class _ZxAnRadiusAuthenGroupTimeout_Type(Integer32):
    """Custom type zxAnRadiusAuthenGroupTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnRadiusAuthenGroupTimeout_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenGroupTimeout_Object = MibTableColumn
zxAnRadiusAuthenGroupTimeout = _ZxAnRadiusAuthenGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 5),
    _ZxAnRadiusAuthenGroupTimeout_Type()
)
zxAnRadiusAuthenGroupTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupTimeout.setUnits("seconds")
_ZxAnRadiusAuthenGroupRowStatus_Type = RowStatus
_ZxAnRadiusAuthenGroupRowStatus_Object = MibTableColumn
zxAnRadiusAuthenGroupRowStatus = _ZxAnRadiusAuthenGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 2, 1, 50),
    _ZxAnRadiusAuthenGroupRowStatus_Type()
)
zxAnRadiusAuthenGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenGroupRowStatus.setStatus("current")
_ZxAnRadiusAuthenSvrGroupTable_Object = MibTable
zxAnRadiusAuthenSvrGroupTable = _ZxAnRadiusAuthenSvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGroupTable.setStatus("current")
_ZxAnRadiusAuthenSvrGroupEntry_Object = MibTableRow
zxAnRadiusAuthenSvrGroupEntry = _ZxAnRadiusAuthenSvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1)
)
zxAnRadiusAuthenSvrGroupEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAuthenGroupId"),
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAuthenSvrGrpSvrId"),
)
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGroupEntry.setStatus("current")


class _ZxAnRadiusAuthenSvrGrpSvrId_Type(Integer32):
    """Custom type zxAnRadiusAuthenSvrGrpSvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnRadiusAuthenSvrGrpSvrId_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenSvrGrpSvrId_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpSvrId = _ZxAnRadiusAuthenSvrGrpSvrId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 1),
    _ZxAnRadiusAuthenSvrGrpSvrId_Type()
)
zxAnRadiusAuthenSvrGrpSvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpSvrId.setStatus("current")
_ZxAnRadiusAuthenSvrGrpSvrIpType_Type = InetAddressType
_ZxAnRadiusAuthenSvrGrpSvrIpType_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpSvrIpType = _ZxAnRadiusAuthenSvrGrpSvrIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 2),
    _ZxAnRadiusAuthenSvrGrpSvrIpType_Type()
)
zxAnRadiusAuthenSvrGrpSvrIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpSvrIpType.setStatus("current")
_ZxAnRadiusAuthenSvrGrpSvrIpAddr_Type = InetAddress
_ZxAnRadiusAuthenSvrGrpSvrIpAddr_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpSvrIpAddr = _ZxAnRadiusAuthenSvrGrpSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 3),
    _ZxAnRadiusAuthenSvrGrpSvrIpAddr_Type()
)
zxAnRadiusAuthenSvrGrpSvrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpSvrIpAddr.setStatus("current")


class _ZxAnRadiusAuthenSvrGrpSvrPort_Type(Integer32):
    """Custom type zxAnRadiusAuthenSvrGrpSvrPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_ZxAnRadiusAuthenSvrGrpSvrPort_Type.__name__ = "Integer32"
_ZxAnRadiusAuthenSvrGrpSvrPort_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpSvrPort = _ZxAnRadiusAuthenSvrGrpSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 4),
    _ZxAnRadiusAuthenSvrGrpSvrPort_Type()
)
zxAnRadiusAuthenSvrGrpSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpSvrPort.setStatus("current")


class _ZxAnRadiusAuthenSvrGrpSvrKey_Type(DisplayString):
    """Custom type zxAnRadiusAuthenSvrGrpSvrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRadiusAuthenSvrGrpSvrKey_Type.__name__ = "DisplayString"
_ZxAnRadiusAuthenSvrGrpSvrKey_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpSvrKey = _ZxAnRadiusAuthenSvrGrpSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 5),
    _ZxAnRadiusAuthenSvrGrpSvrKey_Type()
)
zxAnRadiusAuthenSvrGrpSvrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpSvrKey.setStatus("current")
_ZxAnRadiusAuthenSvrGrpRowStatus_Type = RowStatus
_ZxAnRadiusAuthenSvrGrpRowStatus_Object = MibTableColumn
zxAnRadiusAuthenSvrGrpRowStatus = _ZxAnRadiusAuthenSvrGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 2, 2, 3, 1, 50),
    _ZxAnRadiusAuthenSvrGrpRowStatus_Type()
)
zxAnRadiusAuthenSvrGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAuthenSvrGrpRowStatus.setStatus("current")
_ZxAnRadiusAccountingObjects_ObjectIdentity = ObjectIdentity
zxAnRadiusAccountingObjects = _ZxAnRadiusAccountingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3)
)
_ZxAnRadiusAccountGroup_ObjectIdentity = ObjectIdentity
zxAnRadiusAccountGroup = _ZxAnRadiusAccountGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2)
)
_ZxAnRadiusAccountGroupTable_Object = MibTable
zxAnRadiusAccountGroupTable = _ZxAnRadiusAccountGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupTable.setStatus("current")
_ZxAnRadiusAccountGroupEntry_Object = MibTableRow
zxAnRadiusAccountGroupEntry = _ZxAnRadiusAccountGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1)
)
zxAnRadiusAccountGroupEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAccountGroupId"),
)
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupEntry.setStatus("current")


class _ZxAnRadiusAccountGroupId_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnRadiusAccountGroupId_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupId_Object = MibTableColumn
zxAnRadiusAccountGroupId = _ZxAnRadiusAccountGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 1),
    _ZxAnRadiusAccountGroupId_Type()
)
zxAnRadiusAccountGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupId.setStatus("current")


class _ZxAnRadiusAccountGroupAlgorithm_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterBackup", 1),
          ("roundrobin", 2))
    )


_ZxAnRadiusAccountGroupAlgorithm_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupAlgorithm_Object = MibTableColumn
zxAnRadiusAccountGroupAlgorithm = _ZxAnRadiusAccountGroupAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 2),
    _ZxAnRadiusAccountGroupAlgorithm_Type()
)
zxAnRadiusAccountGroupAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupAlgorithm.setStatus("current")


class _ZxAnRadiusAccountGroupDeadTime_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnRadiusAccountGroupDeadTime_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupDeadTime_Object = MibTableColumn
zxAnRadiusAccountGroupDeadTime = _ZxAnRadiusAccountGroupDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 3),
    _ZxAnRadiusAccountGroupDeadTime_Type()
)
zxAnRadiusAccountGroupDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupDeadTime.setUnits("minutes")


class _ZxAnRadiusAccountGroupBufferEn_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupBufferEn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnRadiusAccountGroupBufferEn_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupBufferEn_Object = MibTableColumn
zxAnRadiusAccountGroupBufferEn = _ZxAnRadiusAccountGroupBufferEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 4),
    _ZxAnRadiusAccountGroupBufferEn_Type()
)
zxAnRadiusAccountGroupBufferEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupBufferEn.setStatus("current")


class _ZxAnRadiusAccountGroupRetries_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnRadiusAccountGroupRetries_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupRetries_Object = MibTableColumn
zxAnRadiusAccountGroupRetries = _ZxAnRadiusAccountGroupRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 5),
    _ZxAnRadiusAccountGroupRetries_Type()
)
zxAnRadiusAccountGroupRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupRetries.setStatus("current")


class _ZxAnRadiusAccountGroupTimeout_Type(Integer32):
    """Custom type zxAnRadiusAccountGroupTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnRadiusAccountGroupTimeout_Type.__name__ = "Integer32"
_ZxAnRadiusAccountGroupTimeout_Object = MibTableColumn
zxAnRadiusAccountGroupTimeout = _ZxAnRadiusAccountGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 6),
    _ZxAnRadiusAccountGroupTimeout_Type()
)
zxAnRadiusAccountGroupTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupTimeout.setUnits("seconds")
_ZxAnRadiusAccountGroupRowStatus_Type = RowStatus
_ZxAnRadiusAccountGroupRowStatus_Object = MibTableColumn
zxAnRadiusAccountGroupRowStatus = _ZxAnRadiusAccountGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 2, 1, 50),
    _ZxAnRadiusAccountGroupRowStatus_Type()
)
zxAnRadiusAccountGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountGroupRowStatus.setStatus("current")
_ZxAnRadiusAccountSvrGroupTable_Object = MibTable
zxAnRadiusAccountSvrGroupTable = _ZxAnRadiusAccountSvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGroupTable.setStatus("current")
_ZxAnRadiusAccountSvrGroupEntry_Object = MibTableRow
zxAnRadiusAccountSvrGroupEntry = _ZxAnRadiusAccountSvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1)
)
zxAnRadiusAccountSvrGroupEntry.setIndexNames(
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAccountGroupId"),
    (0, "ZTE-AN-ACCESS-CTRL-RADIUS-MIB", "zxAnRadiusAccountSvrGrpSvrId"),
)
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGroupEntry.setStatus("current")


class _ZxAnRadiusAccountSvrGrpSvrId_Type(Integer32):
    """Custom type zxAnRadiusAccountSvrGrpSvrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnRadiusAccountSvrGrpSvrId_Type.__name__ = "Integer32"
_ZxAnRadiusAccountSvrGrpSvrId_Object = MibTableColumn
zxAnRadiusAccountSvrGrpSvrId = _ZxAnRadiusAccountSvrGrpSvrId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 1),
    _ZxAnRadiusAccountSvrGrpSvrId_Type()
)
zxAnRadiusAccountSvrGrpSvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpSvrId.setStatus("current")
_ZxAnRadiusAccountSvrGrpSvrIpType_Type = InetAddressType
_ZxAnRadiusAccountSvrGrpSvrIpType_Object = MibTableColumn
zxAnRadiusAccountSvrGrpSvrIpType = _ZxAnRadiusAccountSvrGrpSvrIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 2),
    _ZxAnRadiusAccountSvrGrpSvrIpType_Type()
)
zxAnRadiusAccountSvrGrpSvrIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpSvrIpType.setStatus("current")
_ZxAnRadiusAccountSvrGrpSvrIpAddr_Type = InetAddress
_ZxAnRadiusAccountSvrGrpSvrIpAddr_Object = MibTableColumn
zxAnRadiusAccountSvrGrpSvrIpAddr = _ZxAnRadiusAccountSvrGrpSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 3),
    _ZxAnRadiusAccountSvrGrpSvrIpAddr_Type()
)
zxAnRadiusAccountSvrGrpSvrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpSvrIpAddr.setStatus("current")


class _ZxAnRadiusAccountSvrGrpSvrPort_Type(Integer32):
    """Custom type zxAnRadiusAccountSvrGrpSvrPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_ZxAnRadiusAccountSvrGrpSvrPort_Type.__name__ = "Integer32"
_ZxAnRadiusAccountSvrGrpSvrPort_Object = MibTableColumn
zxAnRadiusAccountSvrGrpSvrPort = _ZxAnRadiusAccountSvrGrpSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 4),
    _ZxAnRadiusAccountSvrGrpSvrPort_Type()
)
zxAnRadiusAccountSvrGrpSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpSvrPort.setStatus("current")


class _ZxAnRadiusAccountSvrGrpSvrKey_Type(DisplayString):
    """Custom type zxAnRadiusAccountSvrGrpSvrKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRadiusAccountSvrGrpSvrKey_Type.__name__ = "DisplayString"
_ZxAnRadiusAccountSvrGrpSvrKey_Object = MibTableColumn
zxAnRadiusAccountSvrGrpSvrKey = _ZxAnRadiusAccountSvrGrpSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 5),
    _ZxAnRadiusAccountSvrGrpSvrKey_Type()
)
zxAnRadiusAccountSvrGrpSvrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpSvrKey.setStatus("current")
_ZxAnRadiusAccountSvrGrpRowStatus_Type = RowStatus
_ZxAnRadiusAccountSvrGrpRowStatus_Object = MibTableColumn
zxAnRadiusAccountSvrGrpRowStatus = _ZxAnRadiusAccountSvrGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 91, 3, 2, 3, 1, 50),
    _ZxAnRadiusAccountSvrGrpRowStatus_Type()
)
zxAnRadiusAccountSvrGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRadiusAccountSvrGrpRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ACCESS-CTRL-RADIUS-MIB",
    **{"zxAnAccessCtrlRadiusMib": zxAnAccessCtrlRadiusMib,
       "zxAnRadiusGlobalObjects": zxAnRadiusGlobalObjects,
       "zxAnRadiusVendorIdEnable": zxAnRadiusVendorIdEnable,
       "zxAnRadiusAuthenticationObjects": zxAnRadiusAuthenticationObjects,
       "zxAnRadiusAuthenGroup": zxAnRadiusAuthenGroup,
       "zxAnRadiusAuthenGroupTable": zxAnRadiusAuthenGroupTable,
       "zxAnRadiusAuthenGroupEntry": zxAnRadiusAuthenGroupEntry,
       "zxAnRadiusAuthenGroupId": zxAnRadiusAuthenGroupId,
       "zxAnRadiusAuthenGroupAlgorithm": zxAnRadiusAuthenGroupAlgorithm,
       "zxAnRadiusAuthenGroupDeadTime": zxAnRadiusAuthenGroupDeadTime,
       "zxAnRadiusAuthenGroupRetries": zxAnRadiusAuthenGroupRetries,
       "zxAnRadiusAuthenGroupTimeout": zxAnRadiusAuthenGroupTimeout,
       "zxAnRadiusAuthenGroupRowStatus": zxAnRadiusAuthenGroupRowStatus,
       "zxAnRadiusAuthenSvrGroupTable": zxAnRadiusAuthenSvrGroupTable,
       "zxAnRadiusAuthenSvrGroupEntry": zxAnRadiusAuthenSvrGroupEntry,
       "zxAnRadiusAuthenSvrGrpSvrId": zxAnRadiusAuthenSvrGrpSvrId,
       "zxAnRadiusAuthenSvrGrpSvrIpType": zxAnRadiusAuthenSvrGrpSvrIpType,
       "zxAnRadiusAuthenSvrGrpSvrIpAddr": zxAnRadiusAuthenSvrGrpSvrIpAddr,
       "zxAnRadiusAuthenSvrGrpSvrPort": zxAnRadiusAuthenSvrGrpSvrPort,
       "zxAnRadiusAuthenSvrGrpSvrKey": zxAnRadiusAuthenSvrGrpSvrKey,
       "zxAnRadiusAuthenSvrGrpRowStatus": zxAnRadiusAuthenSvrGrpRowStatus,
       "zxAnRadiusAccountingObjects": zxAnRadiusAccountingObjects,
       "zxAnRadiusAccountGroup": zxAnRadiusAccountGroup,
       "zxAnRadiusAccountGroupTable": zxAnRadiusAccountGroupTable,
       "zxAnRadiusAccountGroupEntry": zxAnRadiusAccountGroupEntry,
       "zxAnRadiusAccountGroupId": zxAnRadiusAccountGroupId,
       "zxAnRadiusAccountGroupAlgorithm": zxAnRadiusAccountGroupAlgorithm,
       "zxAnRadiusAccountGroupDeadTime": zxAnRadiusAccountGroupDeadTime,
       "zxAnRadiusAccountGroupBufferEn": zxAnRadiusAccountGroupBufferEn,
       "zxAnRadiusAccountGroupRetries": zxAnRadiusAccountGroupRetries,
       "zxAnRadiusAccountGroupTimeout": zxAnRadiusAccountGroupTimeout,
       "zxAnRadiusAccountGroupRowStatus": zxAnRadiusAccountGroupRowStatus,
       "zxAnRadiusAccountSvrGroupTable": zxAnRadiusAccountSvrGroupTable,
       "zxAnRadiusAccountSvrGroupEntry": zxAnRadiusAccountSvrGroupEntry,
       "zxAnRadiusAccountSvrGrpSvrId": zxAnRadiusAccountSvrGrpSvrId,
       "zxAnRadiusAccountSvrGrpSvrIpType": zxAnRadiusAccountSvrGrpSvrIpType,
       "zxAnRadiusAccountSvrGrpSvrIpAddr": zxAnRadiusAccountSvrGrpSvrIpAddr,
       "zxAnRadiusAccountSvrGrpSvrPort": zxAnRadiusAccountSvrGrpSvrPort,
       "zxAnRadiusAccountSvrGrpSvrKey": zxAnRadiusAccountSvrGrpSvrKey,
       "zxAnRadiusAccountSvrGrpRowStatus": zxAnRadiusAccountSvrGrpRowStatus}
)
