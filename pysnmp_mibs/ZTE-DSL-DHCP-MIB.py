# SNMP MIB module (ZTE-DSL-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:18 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength")

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

zxDslDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslDhcpSnoopingTable_Object = MibTable
zxDslDhcpSnoopingTable = _ZxDslDhcpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1)
)
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingTable.setStatus("current")
_ZxDslDhcpSnoopingEntry_Object = MibTableRow
zxDslDhcpSnoopingEntry = _ZxDslDhcpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1)
)
zxDslDhcpSnoopingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpSnoopingBindMac"),
)
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingEntry.setStatus("current")
_ZxDslDhcpSnoopingBindMac_Type = MacAddress
_ZxDslDhcpSnoopingBindMac_Object = MibTableColumn
zxDslDhcpSnoopingBindMac = _ZxDslDhcpSnoopingBindMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 1),
    _ZxDslDhcpSnoopingBindMac_Type()
)
zxDslDhcpSnoopingBindMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingBindMac.setStatus("current")
_ZxDslDhcpSnoopingPvcNo_Type = Integer32
_ZxDslDhcpSnoopingPvcNo_Object = MibTableColumn
zxDslDhcpSnoopingPvcNo = _ZxDslDhcpSnoopingPvcNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 2),
    _ZxDslDhcpSnoopingPvcNo_Type()
)
zxDslDhcpSnoopingPvcNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingPvcNo.setStatus("current")
_ZxDslDhcpSnoopingBindIp_Type = IpAddress
_ZxDslDhcpSnoopingBindIp_Object = MibTableColumn
zxDslDhcpSnoopingBindIp = _ZxDslDhcpSnoopingBindIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 3),
    _ZxDslDhcpSnoopingBindIp_Type()
)
zxDslDhcpSnoopingBindIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingBindIp.setStatus("current")
_ZxDslDhcpSnoopingBindIpLeaseTime_Type = Integer32
_ZxDslDhcpSnoopingBindIpLeaseTime_Object = MibTableColumn
zxDslDhcpSnoopingBindIpLeaseTime = _ZxDslDhcpSnoopingBindIpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 4),
    _ZxDslDhcpSnoopingBindIpLeaseTime_Type()
)
zxDslDhcpSnoopingBindIpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingBindIpLeaseTime.setStatus("current")
_ZxDslDhcpSnoopingBindVlan_Type = Integer32
_ZxDslDhcpSnoopingBindVlan_Object = MibTableColumn
zxDslDhcpSnoopingBindVlan = _ZxDslDhcpSnoopingBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 5),
    _ZxDslDhcpSnoopingBindVlan_Type()
)
zxDslDhcpSnoopingBindVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingBindVlan.setStatus("current")


class _ZxDslDhcpSnoopingIpSourceGuard_Type(Integer32):
    """Custom type zxDslDhcpSnoopingIpSourceGuard based on Integer32"""
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


_ZxDslDhcpSnoopingIpSourceGuard_Type.__name__ = "Integer32"
_ZxDslDhcpSnoopingIpSourceGuard_Object = MibTableColumn
zxDslDhcpSnoopingIpSourceGuard = _ZxDslDhcpSnoopingIpSourceGuard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 1, 1, 6),
    _ZxDslDhcpSnoopingIpSourceGuard_Type()
)
zxDslDhcpSnoopingIpSourceGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpSnoopingIpSourceGuard.setStatus("current")
_ZxDslDhcpPvcIfTable_Object = MibTable
zxDslDhcpPvcIfTable = _ZxDslDhcpPvcIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2)
)
if mibBuilder.loadTexts:
    zxDslDhcpPvcIfTable.setStatus("current")
_ZxDslDhcpPvcIfEntry_Object = MibTableRow
zxDslDhcpPvcIfEntry = _ZxDslDhcpPvcIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2, 1)
)
zxDslDhcpPvcIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpPvcNo"),
)
if mibBuilder.loadTexts:
    zxDslDhcpPvcIfEntry.setStatus("current")
_ZxDslDhcpPvcNo_Type = Integer32
_ZxDslDhcpPvcNo_Object = MibTableColumn
zxDslDhcpPvcNo = _ZxDslDhcpPvcNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2, 1, 1),
    _ZxDslDhcpPvcNo_Type()
)
zxDslDhcpPvcNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpPvcNo.setStatus("current")


class _ZxDslDhcpPvcIfIpSourceGuardEnable_Type(Integer32):
    """Custom type zxDslDhcpPvcIfIpSourceGuardEnable based on Integer32"""
    defaultValue = 1

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


_ZxDslDhcpPvcIfIpSourceGuardEnable_Type.__name__ = "Integer32"
_ZxDslDhcpPvcIfIpSourceGuardEnable_Object = MibTableColumn
zxDslDhcpPvcIfIpSourceGuardEnable = _ZxDslDhcpPvcIfIpSourceGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2, 1, 2),
    _ZxDslDhcpPvcIfIpSourceGuardEnable_Type()
)
zxDslDhcpPvcIfIpSourceGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpPvcIfIpSourceGuardEnable.setStatus("current")


class _ZxDslDhcpPvcIfShortLeaseEnable_Type(Integer32):
    """Custom type zxDslDhcpPvcIfShortLeaseEnable based on Integer32"""
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


_ZxDslDhcpPvcIfShortLeaseEnable_Type.__name__ = "Integer32"
_ZxDslDhcpPvcIfShortLeaseEnable_Object = MibTableColumn
zxDslDhcpPvcIfShortLeaseEnable = _ZxDslDhcpPvcIfShortLeaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2, 1, 3),
    _ZxDslDhcpPvcIfShortLeaseEnable_Type()
)
zxDslDhcpPvcIfShortLeaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpPvcIfShortLeaseEnable.setStatus("current")


class _ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type(Integer32):
    """Custom type zxDslDhcpv6PvcIfIpSourceGuardEnable based on Integer32"""
    defaultValue = 1

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


_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type.__name__ = "Integer32"
_ZxDslDhcpv6PvcIfIpSourceGuardEnable_Object = MibTableColumn
zxDslDhcpv6PvcIfIpSourceGuardEnable = _ZxDslDhcpv6PvcIfIpSourceGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 2, 1, 4),
    _ZxDslDhcpv6PvcIfIpSourceGuardEnable_Type()
)
zxDslDhcpv6PvcIfIpSourceGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpv6PvcIfIpSourceGuardEnable.setStatus("current")
_ZxDslDhcpIfTable_Object = MibTable
zxDslDhcpIfTable = _ZxDslDhcpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3)
)
if mibBuilder.loadTexts:
    zxDslDhcpIfTable.setStatus("current")
_ZxDslDhcpIfEntry_Object = MibTableRow
zxDslDhcpIfEntry = _ZxDslDhcpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3, 1)
)
zxDslDhcpIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslDhcpIfEntry.setStatus("current")


class _ZxDslDhcpIfDhcpSnoopingEnable_Type(Integer32):
    """Custom type zxDslDhcpIfDhcpSnoopingEnable based on Integer32"""
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


_ZxDslDhcpIfDhcpSnoopingEnable_Type.__name__ = "Integer32"
_ZxDslDhcpIfDhcpSnoopingEnable_Object = MibTableColumn
zxDslDhcpIfDhcpSnoopingEnable = _ZxDslDhcpIfDhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3, 1, 1),
    _ZxDslDhcpIfDhcpSnoopingEnable_Type()
)
zxDslDhcpIfDhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpIfDhcpSnoopingEnable.setStatus("current")


class _ZxDslDhcpIfDhcpSnoopingLimit_Type(Integer32):
    """Custom type zxDslDhcpIfDhcpSnoopingLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxDslDhcpIfDhcpSnoopingLimit_Type.__name__ = "Integer32"
_ZxDslDhcpIfDhcpSnoopingLimit_Object = MibTableColumn
zxDslDhcpIfDhcpSnoopingLimit = _ZxDslDhcpIfDhcpSnoopingLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3, 1, 2),
    _ZxDslDhcpIfDhcpSnoopingLimit_Type()
)
zxDslDhcpIfDhcpSnoopingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpIfDhcpSnoopingLimit.setStatus("current")


class _ZxDslDhcpv6IfDhcpSnoopingEnable_Type(Integer32):
    """Custom type zxDslDhcpv6IfDhcpSnoopingEnable based on Integer32"""
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


_ZxDslDhcpv6IfDhcpSnoopingEnable_Type.__name__ = "Integer32"
_ZxDslDhcpv6IfDhcpSnoopingEnable_Object = MibTableColumn
zxDslDhcpv6IfDhcpSnoopingEnable = _ZxDslDhcpv6IfDhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3, 1, 3),
    _ZxDslDhcpv6IfDhcpSnoopingEnable_Type()
)
zxDslDhcpv6IfDhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpv6IfDhcpSnoopingEnable.setStatus("current")


class _ZxDslDhcpv6IfDhcpSnoopingLimit_Type(Integer32):
    """Custom type zxDslDhcpv6IfDhcpSnoopingLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxDslDhcpv6IfDhcpSnoopingLimit_Type.__name__ = "Integer32"
_ZxDslDhcpv6IfDhcpSnoopingLimit_Object = MibTableColumn
zxDslDhcpv6IfDhcpSnoopingLimit = _ZxDslDhcpv6IfDhcpSnoopingLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 3, 1, 4),
    _ZxDslDhcpv6IfDhcpSnoopingLimit_Type()
)
zxDslDhcpv6IfDhcpSnoopingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpv6IfDhcpSnoopingLimit.setStatus("current")
_ZxDslDhcpL3IfTable_Object = MibTable
zxDslDhcpL3IfTable = _ZxDslDhcpL3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4)
)
if mibBuilder.loadTexts:
    zxDslDhcpL3IfTable.setStatus("current")
_ZxDslDhcpL3IfEntry_Object = MibTableRow
zxDslDhcpL3IfEntry = _ZxDslDhcpL3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1)
)
zxDslDhcpL3IfEntry.setIndexNames(
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpL3IfIndex"),
)
if mibBuilder.loadTexts:
    zxDslDhcpL3IfEntry.setStatus("current")
_ZxDslDhcpL3IfIndex_Type = Integer32
_ZxDslDhcpL3IfIndex_Object = MibTableColumn
zxDslDhcpL3IfIndex = _ZxDslDhcpL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1, 1),
    _ZxDslDhcpL3IfIndex_Type()
)
zxDslDhcpL3IfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpL3IfIndex.setStatus("current")
_ZxDslDhcpL3IfIpAddress_Type = IpAddress
_ZxDslDhcpL3IfIpAddress_Object = MibTableColumn
zxDslDhcpL3IfIpAddress = _ZxDslDhcpL3IfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1, 2),
    _ZxDslDhcpL3IfIpAddress_Type()
)
zxDslDhcpL3IfIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpL3IfIpAddress.setStatus("current")
_ZxDslDhcpL3IfIpMask_Type = IpAddress
_ZxDslDhcpL3IfIpMask_Object = MibTableColumn
zxDslDhcpL3IfIpMask = _ZxDslDhcpL3IfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1, 3),
    _ZxDslDhcpL3IfIpMask_Type()
)
zxDslDhcpL3IfIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpL3IfIpMask.setStatus("current")
_ZxDslDhcpL3IfDhcpServerIp_Type = IpAddress
_ZxDslDhcpL3IfDhcpServerIp_Object = MibTableColumn
zxDslDhcpL3IfDhcpServerIp = _ZxDslDhcpL3IfDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1, 4),
    _ZxDslDhcpL3IfDhcpServerIp_Type()
)
zxDslDhcpL3IfDhcpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpL3IfDhcpServerIp.setStatus("current")
_ZxDslDhcpL3IfRowstatus_Type = RowStatus
_ZxDslDhcpL3IfRowstatus_Object = MibTableColumn
zxDslDhcpL3IfRowstatus = _ZxDslDhcpL3IfRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 4, 1, 5),
    _ZxDslDhcpL3IfRowstatus_Type()
)
zxDslDhcpL3IfRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpL3IfRowstatus.setStatus("current")
_ZxDslDhcpClientDomainTable_Object = MibTable
zxDslDhcpClientDomainTable = _ZxDslDhcpClientDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 5)
)
if mibBuilder.loadTexts:
    zxDslDhcpClientDomainTable.setStatus("current")
_ZxDslDhcpClientDomainEntry_Object = MibTableRow
zxDslDhcpClientDomainEntry = _ZxDslDhcpClientDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 5, 1)
)
zxDslDhcpClientDomainEntry.setIndexNames(
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpClientDomainName"),
)
if mibBuilder.loadTexts:
    zxDslDhcpClientDomainEntry.setStatus("current")


class _ZxDslDhcpClientDomainName_Type(DisplayString):
    """Custom type zxDslDhcpClientDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxDslDhcpClientDomainName_Type.__name__ = "DisplayString"
_ZxDslDhcpClientDomainName_Object = MibTableColumn
zxDslDhcpClientDomainName = _ZxDslDhcpClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 5, 1, 1),
    _ZxDslDhcpClientDomainName_Type()
)
zxDslDhcpClientDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpClientDomainName.setStatus("current")
_ZxDslDhcpServerIp_Type = IpAddress
_ZxDslDhcpServerIp_Object = MibTableColumn
zxDslDhcpServerIp = _ZxDslDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 5, 1, 2),
    _ZxDslDhcpServerIp_Type()
)
zxDslDhcpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpServerIp.setStatus("current")
_ZxDslDhcpClientDomainRowstatus_Type = RowStatus
_ZxDslDhcpClientDomainRowstatus_Object = MibTableColumn
zxDslDhcpClientDomainRowstatus = _ZxDslDhcpClientDomainRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 5, 1, 3),
    _ZxDslDhcpClientDomainRowstatus_Type()
)
zxDslDhcpClientDomainRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslDhcpClientDomainRowstatus.setStatus("current")
_ZxDslDhcpGlobal_ObjectIdentity = ObjectIdentity
zxDslDhcpGlobal = _ZxDslDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 6)
)


class _ZxDslDhcpProxyShortLease_Type(Integer32):
    """Custom type zxDslDhcpProxyShortLease based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_ZxDslDhcpProxyShortLease_Type.__name__ = "Integer32"
_ZxDslDhcpProxyShortLease_Object = MibScalar
zxDslDhcpProxyShortLease = _ZxDslDhcpProxyShortLease_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 6, 1),
    _ZxDslDhcpProxyShortLease_Type()
)
zxDslDhcpProxyShortLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslDhcpProxyShortLease.setStatus("current")
if mibBuilder.loadTexts:
    zxDslDhcpProxyShortLease.setUnits("seconds")
_ZxDslDhcpv6_ObjectIdentity = ObjectIdentity
zxDslDhcpv6 = _ZxDslDhcpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7)
)
_ZxDslDhcpv6SnoopingTable_Object = MibTable
zxDslDhcpv6SnoopingTable = _ZxDslDhcpv6SnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1)
)
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingTable.setStatus("current")
_ZxDslDhcpv6SnoopingEntry_Object = MibTableRow
zxDslDhcpv6SnoopingEntry = _ZxDslDhcpv6SnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1)
)
zxDslDhcpv6SnoopingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpv6SnoopingBindMac"),
    (0, "ZTE-DSL-DHCP-MIB", "zxDslDhcpv6SnoopingBindIp"),
)
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingEntry.setStatus("current")
_ZxDslDhcpv6SnoopingBindMac_Type = MacAddress
_ZxDslDhcpv6SnoopingBindMac_Object = MibTableColumn
zxDslDhcpv6SnoopingBindMac = _ZxDslDhcpv6SnoopingBindMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 1),
    _ZxDslDhcpv6SnoopingBindMac_Type()
)
zxDslDhcpv6SnoopingBindMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingBindMac.setStatus("current")
_ZxDslDhcpv6SnoopingBindIp_Type = InetAddress
_ZxDslDhcpv6SnoopingBindIp_Object = MibTableColumn
zxDslDhcpv6SnoopingBindIp = _ZxDslDhcpv6SnoopingBindIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 2),
    _ZxDslDhcpv6SnoopingBindIp_Type()
)
zxDslDhcpv6SnoopingBindIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingBindIp.setStatus("current")
_ZxDslDhcpv6SnoopingPvcNo_Type = Integer32
_ZxDslDhcpv6SnoopingPvcNo_Object = MibTableColumn
zxDslDhcpv6SnoopingPvcNo = _ZxDslDhcpv6SnoopingPvcNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 3),
    _ZxDslDhcpv6SnoopingPvcNo_Type()
)
zxDslDhcpv6SnoopingPvcNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingPvcNo.setStatus("current")
_ZxDslDhcpv6SnoopingBindIpLeaseTime_Type = Integer32
_ZxDslDhcpv6SnoopingBindIpLeaseTime_Object = MibTableColumn
zxDslDhcpv6SnoopingBindIpLeaseTime = _ZxDslDhcpv6SnoopingBindIpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 4),
    _ZxDslDhcpv6SnoopingBindIpLeaseTime_Type()
)
zxDslDhcpv6SnoopingBindIpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingBindIpLeaseTime.setStatus("current")
_ZxDslDhcpv6SnoopingBindVlan_Type = Integer32
_ZxDslDhcpv6SnoopingBindVlan_Object = MibTableColumn
zxDslDhcpv6SnoopingBindVlan = _ZxDslDhcpv6SnoopingBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 5),
    _ZxDslDhcpv6SnoopingBindVlan_Type()
)
zxDslDhcpv6SnoopingBindVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingBindVlan.setStatus("current")


class _ZxDslDhcpv6SnoopingIpSourceGuard_Type(Integer32):
    """Custom type zxDslDhcpv6SnoopingIpSourceGuard based on Integer32"""
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


_ZxDslDhcpv6SnoopingIpSourceGuard_Type.__name__ = "Integer32"
_ZxDslDhcpv6SnoopingIpSourceGuard_Object = MibTableColumn
zxDslDhcpv6SnoopingIpSourceGuard = _ZxDslDhcpv6SnoopingIpSourceGuard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 6),
    _ZxDslDhcpv6SnoopingIpSourceGuard_Type()
)
zxDslDhcpv6SnoopingIpSourceGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingIpSourceGuard.setStatus("current")
_ZxDslDhcpv6SnoopingBindIpPrefixLength_Type = InetAddressPrefixLength
_ZxDslDhcpv6SnoopingBindIpPrefixLength_Object = MibTableColumn
zxDslDhcpv6SnoopingBindIpPrefixLength = _ZxDslDhcpv6SnoopingBindIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 28, 7, 1, 1, 7),
    _ZxDslDhcpv6SnoopingBindIpPrefixLength_Type()
)
zxDslDhcpv6SnoopingBindIpPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslDhcpv6SnoopingBindIpPrefixLength.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-DHCP-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslDhcpMib": zxDslDhcpMib,
       "zxDslDhcpSnoopingTable": zxDslDhcpSnoopingTable,
       "zxDslDhcpSnoopingEntry": zxDslDhcpSnoopingEntry,
       "zxDslDhcpSnoopingBindMac": zxDslDhcpSnoopingBindMac,
       "zxDslDhcpSnoopingPvcNo": zxDslDhcpSnoopingPvcNo,
       "zxDslDhcpSnoopingBindIp": zxDslDhcpSnoopingBindIp,
       "zxDslDhcpSnoopingBindIpLeaseTime": zxDslDhcpSnoopingBindIpLeaseTime,
       "zxDslDhcpSnoopingBindVlan": zxDslDhcpSnoopingBindVlan,
       "zxDslDhcpSnoopingIpSourceGuard": zxDslDhcpSnoopingIpSourceGuard,
       "zxDslDhcpPvcIfTable": zxDslDhcpPvcIfTable,
       "zxDslDhcpPvcIfEntry": zxDslDhcpPvcIfEntry,
       "zxDslDhcpPvcNo": zxDslDhcpPvcNo,
       "zxDslDhcpPvcIfIpSourceGuardEnable": zxDslDhcpPvcIfIpSourceGuardEnable,
       "zxDslDhcpPvcIfShortLeaseEnable": zxDslDhcpPvcIfShortLeaseEnable,
       "zxDslDhcpv6PvcIfIpSourceGuardEnable": zxDslDhcpv6PvcIfIpSourceGuardEnable,
       "zxDslDhcpIfTable": zxDslDhcpIfTable,
       "zxDslDhcpIfEntry": zxDslDhcpIfEntry,
       "zxDslDhcpIfDhcpSnoopingEnable": zxDslDhcpIfDhcpSnoopingEnable,
       "zxDslDhcpIfDhcpSnoopingLimit": zxDslDhcpIfDhcpSnoopingLimit,
       "zxDslDhcpv6IfDhcpSnoopingEnable": zxDslDhcpv6IfDhcpSnoopingEnable,
       "zxDslDhcpv6IfDhcpSnoopingLimit": zxDslDhcpv6IfDhcpSnoopingLimit,
       "zxDslDhcpL3IfTable": zxDslDhcpL3IfTable,
       "zxDslDhcpL3IfEntry": zxDslDhcpL3IfEntry,
       "zxDslDhcpL3IfIndex": zxDslDhcpL3IfIndex,
       "zxDslDhcpL3IfIpAddress": zxDslDhcpL3IfIpAddress,
       "zxDslDhcpL3IfIpMask": zxDslDhcpL3IfIpMask,
       "zxDslDhcpL3IfDhcpServerIp": zxDslDhcpL3IfDhcpServerIp,
       "zxDslDhcpL3IfRowstatus": zxDslDhcpL3IfRowstatus,
       "zxDslDhcpClientDomainTable": zxDslDhcpClientDomainTable,
       "zxDslDhcpClientDomainEntry": zxDslDhcpClientDomainEntry,
       "zxDslDhcpClientDomainName": zxDslDhcpClientDomainName,
       "zxDslDhcpServerIp": zxDslDhcpServerIp,
       "zxDslDhcpClientDomainRowstatus": zxDslDhcpClientDomainRowstatus,
       "zxDslDhcpGlobal": zxDslDhcpGlobal,
       "zxDslDhcpProxyShortLease": zxDslDhcpProxyShortLease,
       "zxDslDhcpv6": zxDslDhcpv6,
       "zxDslDhcpv6SnoopingTable": zxDslDhcpv6SnoopingTable,
       "zxDslDhcpv6SnoopingEntry": zxDslDhcpv6SnoopingEntry,
       "zxDslDhcpv6SnoopingBindMac": zxDslDhcpv6SnoopingBindMac,
       "zxDslDhcpv6SnoopingBindIp": zxDslDhcpv6SnoopingBindIp,
       "zxDslDhcpv6SnoopingPvcNo": zxDslDhcpv6SnoopingPvcNo,
       "zxDslDhcpv6SnoopingBindIpLeaseTime": zxDslDhcpv6SnoopingBindIpLeaseTime,
       "zxDslDhcpv6SnoopingBindVlan": zxDslDhcpv6SnoopingBindVlan,
       "zxDslDhcpv6SnoopingIpSourceGuard": zxDslDhcpv6SnoopingIpSourceGuard,
       "zxDslDhcpv6SnoopingBindIpPrefixLength": zxDslDhcpv6SnoopingBindIpPrefixLength}
)
