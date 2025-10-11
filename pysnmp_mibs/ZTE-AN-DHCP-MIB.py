# SNMP MIB module (ZTE-AN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:44 2025
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

(zxAnPortLocatingMib,) = mibBuilder.importSymbols(
    "ZTE-AN-PORT-LOCATING-MIB",
    "zxAnPortLocatingMib")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ZxAnDhcpV4L2RAEnable_Type(Integer32):
    """Custom type zxAnDhcpV4L2RAEnable based on Integer32"""
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


_ZxAnDhcpV4L2RAEnable_Type.__name__ = "Integer32"
_ZxAnDhcpV4L2RAEnable_Object = MibScalar
zxAnDhcpV4L2RAEnable = _ZxAnDhcpV4L2RAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 1),
    _ZxAnDhcpV4L2RAEnable_Type()
)
zxAnDhcpV4L2RAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV4L2RAEnable.setStatus("current")


class _ZxAnPortLocatingDhcp128Enable_Type(Integer32):
    """Custom type zxAnPortLocatingDhcp128Enable based on Integer32"""
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


_ZxAnPortLocatingDhcp128Enable_Type.__name__ = "Integer32"
_ZxAnPortLocatingDhcp128Enable_Object = MibScalar
zxAnPortLocatingDhcp128Enable = _ZxAnPortLocatingDhcp128Enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 2),
    _ZxAnPortLocatingDhcp128Enable_Type()
)
zxAnPortLocatingDhcp128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingDhcp128Enable.setStatus("current")


class _ZxAnDhcpV6L2RAEnable_Type(Integer32):
    """Custom type zxAnDhcpV6L2RAEnable based on Integer32"""
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


_ZxAnDhcpV6L2RAEnable_Type.__name__ = "Integer32"
_ZxAnDhcpV6L2RAEnable_Object = MibScalar
zxAnDhcpV6L2RAEnable = _ZxAnDhcpV6L2RAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 3),
    _ZxAnDhcpV6L2RAEnable_Type()
)
zxAnDhcpV6L2RAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV6L2RAEnable.setStatus("current")


class _ZxAnPortLocatingDhcpVmacEnable_Type(Integer32):
    """Custom type zxAnPortLocatingDhcpVmacEnable based on Integer32"""
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


_ZxAnPortLocatingDhcpVmacEnable_Type.__name__ = "Integer32"
_ZxAnPortLocatingDhcpVmacEnable_Object = MibScalar
zxAnPortLocatingDhcpVmacEnable = _ZxAnPortLocatingDhcpVmacEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 4),
    _ZxAnPortLocatingDhcpVmacEnable_Type()
)
zxAnPortLocatingDhcpVmacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingDhcpVmacEnable.setStatus("current")


class _ZxAnDhcpv6PortLocatingWorkMode_Type(Integer32):
    """Custom type zxAnDhcpv6PortLocatingWorkMode based on Integer32"""
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
        *(("tcMode", 1),
          ("layer2Mode", 2),
          ("layer3Mode", 3))
    )


_ZxAnDhcpv6PortLocatingWorkMode_Type.__name__ = "Integer32"
_ZxAnDhcpv6PortLocatingWorkMode_Object = MibScalar
zxAnDhcpv6PortLocatingWorkMode = _ZxAnDhcpv6PortLocatingWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 5),
    _ZxAnDhcpv6PortLocatingWorkMode_Type()
)
zxAnDhcpv6PortLocatingWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpv6PortLocatingWorkMode.setStatus("current")
_ZxAnPortLocatingDhcpTable_Object = MibTable
zxAnPortLocatingDhcpTable = _ZxAnPortLocatingDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20)
)
if mibBuilder.loadTexts:
    zxAnPortLocatingDhcpTable.setStatus("current")
_ZxAnPortLocatingDhcpEntry_Object = MibTableRow
zxAnPortLocatingDhcpEntry = _ZxAnPortLocatingDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1)
)
zxAnPortLocatingDhcpEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-MIB", "zxAnPortLocatingDhcpIndex"),
)
if mibBuilder.loadTexts:
    zxAnPortLocatingDhcpEntry.setStatus("current")
_ZxAnPortLocatingDhcpIndex_Type = ZxAnIfindex
_ZxAnPortLocatingDhcpIndex_Object = MibTableColumn
zxAnPortLocatingDhcpIndex = _ZxAnPortLocatingDhcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 1),
    _ZxAnPortLocatingDhcpIndex_Type()
)
zxAnPortLocatingDhcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortLocatingDhcpIndex.setStatus("current")


class _ZxAnDhcpV4L2RAIfConfEnable_Type(Integer32):
    """Custom type zxAnDhcpV4L2RAIfConfEnable based on Integer32"""
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


_ZxAnDhcpV4L2RAIfConfEnable_Type.__name__ = "Integer32"
_ZxAnDhcpV4L2RAIfConfEnable_Object = MibTableColumn
zxAnDhcpV4L2RAIfConfEnable = _ZxAnDhcpV4L2RAIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 2),
    _ZxAnDhcpV4L2RAIfConfEnable_Type()
)
zxAnDhcpV4L2RAIfConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV4L2RAIfConfEnable.setStatus("current")


class _ZxAnPortLocatingPortDhcp128Enable_Type(Integer32):
    """Custom type zxAnPortLocatingPortDhcp128Enable based on Integer32"""
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


_ZxAnPortLocatingPortDhcp128Enable_Type.__name__ = "Integer32"
_ZxAnPortLocatingPortDhcp128Enable_Object = MibTableColumn
zxAnPortLocatingPortDhcp128Enable = _ZxAnPortLocatingPortDhcp128Enable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 3),
    _ZxAnPortLocatingPortDhcp128Enable_Type()
)
zxAnPortLocatingPortDhcp128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingPortDhcp128Enable.setStatus("current")


class _ZxAnDhcpV4L2RAIfConfTrust_Type(Integer32):
    """Custom type zxAnDhcpV4L2RAIfConfTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ZxAnDhcpV4L2RAIfConfTrust_Type.__name__ = "Integer32"
_ZxAnDhcpV4L2RAIfConfTrust_Object = MibTableColumn
zxAnDhcpV4L2RAIfConfTrust = _ZxAnDhcpV4L2RAIfConfTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 4),
    _ZxAnDhcpV4L2RAIfConfTrust_Type()
)
zxAnDhcpV4L2RAIfConfTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV4L2RAIfConfTrust.setStatus("current")


class _ZxAnDhcpV4L2RAIfConfPolicy_Type(Integer32):
    """Custom type zxAnDhcpV4L2RAIfConfPolicy based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("replace", 2),
          ("discard", 3),
          ("add", 4))
    )


_ZxAnDhcpV4L2RAIfConfPolicy_Type.__name__ = "Integer32"
_ZxAnDhcpV4L2RAIfConfPolicy_Object = MibTableColumn
zxAnDhcpV4L2RAIfConfPolicy = _ZxAnDhcpV4L2RAIfConfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 5),
    _ZxAnDhcpV4L2RAIfConfPolicy_Type()
)
zxAnDhcpV4L2RAIfConfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV4L2RAIfConfPolicy.setStatus("current")


class _ZxAnPortLocatingPortDhcpSnoopEnable_Type(Integer32):
    """Custom type zxAnPortLocatingPortDhcpSnoopEnable based on Integer32"""
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


_ZxAnPortLocatingPortDhcpSnoopEnable_Type.__name__ = "Integer32"
_ZxAnPortLocatingPortDhcpSnoopEnable_Object = MibTableColumn
zxAnPortLocatingPortDhcpSnoopEnable = _ZxAnPortLocatingPortDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 20, 1, 6),
    _ZxAnPortLocatingPortDhcpSnoopEnable_Type()
)
zxAnPortLocatingPortDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPortLocatingPortDhcpSnoopEnable.setStatus("current")
_ZxAnDhcpv6PortLocatingDhcpTable_Object = MibTable
zxAnDhcpv6PortLocatingDhcpTable = _ZxAnDhcpv6PortLocatingDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21)
)
if mibBuilder.loadTexts:
    zxAnDhcpv6PortLocatingDhcpTable.setStatus("current")
_ZxAnDhcpv6PortLocatingDhcpEntry_Object = MibTableRow
zxAnDhcpv6PortLocatingDhcpEntry = _ZxAnDhcpv6PortLocatingDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1)
)
zxAnDhcpv6PortLocatingDhcpEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-MIB", "zxAnDhcpv6PortLocatingDhcpIndex"),
)
if mibBuilder.loadTexts:
    zxAnDhcpv6PortLocatingDhcpEntry.setStatus("current")
_ZxAnDhcpv6PortLocatingDhcpIndex_Type = ZxAnIfindex
_ZxAnDhcpv6PortLocatingDhcpIndex_Object = MibTableColumn
zxAnDhcpv6PortLocatingDhcpIndex = _ZxAnDhcpv6PortLocatingDhcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1, 1),
    _ZxAnDhcpv6PortLocatingDhcpIndex_Type()
)
zxAnDhcpv6PortLocatingDhcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDhcpv6PortLocatingDhcpIndex.setStatus("current")


class _ZxAnDhcpV6L2RAIfConfEnable_Type(Integer32):
    """Custom type zxAnDhcpV6L2RAIfConfEnable based on Integer32"""
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


_ZxAnDhcpV6L2RAIfConfEnable_Type.__name__ = "Integer32"
_ZxAnDhcpV6L2RAIfConfEnable_Object = MibTableColumn
zxAnDhcpV6L2RAIfConfEnable = _ZxAnDhcpV6L2RAIfConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1, 2),
    _ZxAnDhcpV6L2RAIfConfEnable_Type()
)
zxAnDhcpV6L2RAIfConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV6L2RAIfConfEnable.setStatus("current")


class _ZxAnDhcpV6L2RAIfConfTrust_Type(Integer32):
    """Custom type zxAnDhcpV6L2RAIfConfTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_ZxAnDhcpV6L2RAIfConfTrust_Type.__name__ = "Integer32"
_ZxAnDhcpV6L2RAIfConfTrust_Object = MibTableColumn
zxAnDhcpV6L2RAIfConfTrust = _ZxAnDhcpV6L2RAIfConfTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1, 3),
    _ZxAnDhcpV6L2RAIfConfTrust_Type()
)
zxAnDhcpV6L2RAIfConfTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV6L2RAIfConfTrust.setStatus("current")


class _ZxAnDhcpV6L2RAIfConfPolicy_Type(Integer32):
    """Custom type zxAnDhcpV6L2RAIfConfPolicy based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("replace", 2),
          ("discard", 3),
          ("add", 4))
    )


_ZxAnDhcpV6L2RAIfConfPolicy_Type.__name__ = "Integer32"
_ZxAnDhcpV6L2RAIfConfPolicy_Object = MibTableColumn
zxAnDhcpV6L2RAIfConfPolicy = _ZxAnDhcpV6L2RAIfConfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1, 4),
    _ZxAnDhcpV6L2RAIfConfPolicy_Type()
)
zxAnDhcpV6L2RAIfConfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpV6L2RAIfConfPolicy.setStatus("current")


class _ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type(Integer32):
    """Custom type zxAnDhcpv6PortLocatingPortDhcpSnoopEnable based on Integer32"""
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


_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type.__name__ = "Integer32"
_ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Object = MibTableColumn
zxAnDhcpv6PortLocatingPortDhcpSnoopEnable = _ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 21, 1, 5),
    _ZxAnDhcpv6PortLocatingPortDhcpSnoopEnable_Type()
)
zxAnDhcpv6PortLocatingPortDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDhcpv6PortLocatingPortDhcpSnoopEnable.setStatus("current")
_ZxAnPortIdDhcpVmacTable_Object = MibTable
zxAnPortIdDhcpVmacTable = _ZxAnPortIdDhcpVmacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 22)
)
if mibBuilder.loadTexts:
    zxAnPortIdDhcpVmacTable.setStatus("current")
_ZxAnPortIdDhcpVmacEntry_Object = MibTableRow
zxAnPortIdDhcpVmacEntry = _ZxAnPortIdDhcpVmacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 22, 1)
)
zxAnPortIdDhcpVmacEntry.setIndexNames(
    (0, "ZTE-AN-DHCP-MIB", "zxAnPortIdDhcpVmacIfIndex"),
    (0, "ZTE-AN-DHCP-MIB", "zxAnPortIdDhcpVmacVid"),
)
if mibBuilder.loadTexts:
    zxAnPortIdDhcpVmacEntry.setStatus("current")
_ZxAnPortIdDhcpVmacIfIndex_Type = ZxAnIfindex
_ZxAnPortIdDhcpVmacIfIndex_Object = MibTableColumn
zxAnPortIdDhcpVmacIfIndex = _ZxAnPortIdDhcpVmacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 22, 1, 1),
    _ZxAnPortIdDhcpVmacIfIndex_Type()
)
zxAnPortIdDhcpVmacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortIdDhcpVmacIfIndex.setStatus("current")


class _ZxAnPortIdDhcpVmacVid_Type(Integer32):
    """Custom type zxAnPortIdDhcpVmacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnPortIdDhcpVmacVid_Type.__name__ = "Integer32"
_ZxAnPortIdDhcpVmacVid_Object = MibTableColumn
zxAnPortIdDhcpVmacVid = _ZxAnPortIdDhcpVmacVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 22, 1, 2),
    _ZxAnPortIdDhcpVmacVid_Type()
)
zxAnPortIdDhcpVmacVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPortIdDhcpVmacVid.setStatus("current")
_ZxAnPortIdDhcpVmacRowStatus_Type = RowStatus
_ZxAnPortIdDhcpVmacRowStatus_Object = MibTableColumn
zxAnPortIdDhcpVmacRowStatus = _ZxAnPortIdDhcpVmacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 32, 21, 22, 1, 50),
    _ZxAnPortIdDhcpVmacRowStatus_Type()
)
zxAnPortIdDhcpVmacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPortIdDhcpVmacRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-DHCP-MIB",
    **{"zxAnDhcpMib": zxAnDhcpMib,
       "zxAnDhcpV4L2RAEnable": zxAnDhcpV4L2RAEnable,
       "zxAnPortLocatingDhcp128Enable": zxAnPortLocatingDhcp128Enable,
       "zxAnDhcpV6L2RAEnable": zxAnDhcpV6L2RAEnable,
       "zxAnPortLocatingDhcpVmacEnable": zxAnPortLocatingDhcpVmacEnable,
       "zxAnDhcpv6PortLocatingWorkMode": zxAnDhcpv6PortLocatingWorkMode,
       "zxAnPortLocatingDhcpTable": zxAnPortLocatingDhcpTable,
       "zxAnPortLocatingDhcpEntry": zxAnPortLocatingDhcpEntry,
       "zxAnPortLocatingDhcpIndex": zxAnPortLocatingDhcpIndex,
       "zxAnDhcpV4L2RAIfConfEnable": zxAnDhcpV4L2RAIfConfEnable,
       "zxAnPortLocatingPortDhcp128Enable": zxAnPortLocatingPortDhcp128Enable,
       "zxAnDhcpV4L2RAIfConfTrust": zxAnDhcpV4L2RAIfConfTrust,
       "zxAnDhcpV4L2RAIfConfPolicy": zxAnDhcpV4L2RAIfConfPolicy,
       "zxAnPortLocatingPortDhcpSnoopEnable": zxAnPortLocatingPortDhcpSnoopEnable,
       "zxAnDhcpv6PortLocatingDhcpTable": zxAnDhcpv6PortLocatingDhcpTable,
       "zxAnDhcpv6PortLocatingDhcpEntry": zxAnDhcpv6PortLocatingDhcpEntry,
       "zxAnDhcpv6PortLocatingDhcpIndex": zxAnDhcpv6PortLocatingDhcpIndex,
       "zxAnDhcpV6L2RAIfConfEnable": zxAnDhcpV6L2RAIfConfEnable,
       "zxAnDhcpV6L2RAIfConfTrust": zxAnDhcpV6L2RAIfConfTrust,
       "zxAnDhcpV6L2RAIfConfPolicy": zxAnDhcpV6L2RAIfConfPolicy,
       "zxAnDhcpv6PortLocatingPortDhcpSnoopEnable": zxAnDhcpv6PortLocatingPortDhcpSnoopEnable,
       "zxAnPortIdDhcpVmacTable": zxAnPortIdDhcpVmacTable,
       "zxAnPortIdDhcpVmacEntry": zxAnPortIdDhcpVmacEntry,
       "zxAnPortIdDhcpVmacIfIndex": zxAnPortIdDhcpVmacIfIndex,
       "zxAnPortIdDhcpVmacVid": zxAnPortIdDhcpVmacVid,
       "zxAnPortIdDhcpVmacRowStatus": zxAnPortIdDhcpVmacRowStatus}
)
