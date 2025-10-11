# SNMP MIB module (ZTE-AN-BRG-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-BRG-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:03 2025
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus",
    "ifType")

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

(ZxAnIdList,
 ZxAnIfindex,
 ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIdList",
    "ZxAnIfindex",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnBrgPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnBrgPortObjects_ObjectIdentity = ObjectIdentity
zxAnBrgPortObjects = _ZxAnBrgPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1)
)
_ZxAnBrgUsrSidePortTable_Object = MibTable
zxAnBrgUsrSidePortTable = _ZxAnBrgUsrSidePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnBrgUsrSidePortTable.setStatus("current")
_ZxAnBrgUsrSidePortEntry_Object = MibTableRow
zxAnBrgUsrSidePortEntry = _ZxAnBrgUsrSidePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1)
)
zxAnBrgUsrSidePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
)
if mibBuilder.loadTexts:
    zxAnBrgUsrSidePortEntry.setStatus("current")
_ZxAnBrgUsrPortId_Type = Integer32
_ZxAnBrgUsrPortId_Object = MibTableColumn
zxAnBrgUsrPortId = _ZxAnBrgUsrPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 1),
    _ZxAnBrgUsrPortId_Type()
)
zxAnBrgUsrPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortId.setStatus("current")


class _ZxAnBrgUsrPortAdminStatus_Type(Integer32):
    """Custom type zxAnBrgUsrPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnBrgUsrPortAdminStatus_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortAdminStatus_Object = MibTableColumn
zxAnBrgUsrPortAdminStatus = _ZxAnBrgUsrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 2),
    _ZxAnBrgUsrPortAdminStatus_Type()
)
zxAnBrgUsrPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortAdminStatus.setStatus("current")
_ZxAnBrgUsrPortPvcVpi_Type = Integer32
_ZxAnBrgUsrPortPvcVpi_Object = MibTableColumn
zxAnBrgUsrPortPvcVpi = _ZxAnBrgUsrPortPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 3),
    _ZxAnBrgUsrPortPvcVpi_Type()
)
zxAnBrgUsrPortPvcVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortPvcVpi.setStatus("current")
_ZxAnBrgUsrPortPvcVci_Type = Integer32
_ZxAnBrgUsrPortPvcVci_Object = MibTableColumn
zxAnBrgUsrPortPvcVci = _ZxAnBrgUsrPortPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 4),
    _ZxAnBrgUsrPortPvcVci_Type()
)
zxAnBrgUsrPortPvcVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortPvcVci.setStatus("current")


class _ZxAnBrgUsrPortBindIpEnable_Type(Integer32):
    """Custom type zxAnBrgUsrPortBindIpEnable based on Integer32"""
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


_ZxAnBrgUsrPortBindIpEnable_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortBindIpEnable_Object = MibTableColumn
zxAnBrgUsrPortBindIpEnable = _ZxAnBrgUsrPortBindIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 5),
    _ZxAnBrgUsrPortBindIpEnable_Type()
)
zxAnBrgUsrPortBindIpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortBindIpEnable.setStatus("current")


class _ZxAnBrgUsrPortBindMacEnable_Type(Integer32):
    """Custom type zxAnBrgUsrPortBindMacEnable based on Integer32"""
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


_ZxAnBrgUsrPortBindMacEnable_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortBindMacEnable_Object = MibTableColumn
zxAnBrgUsrPortBindMacEnable = _ZxAnBrgUsrPortBindMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 6),
    _ZxAnBrgUsrPortBindMacEnable_Type()
)
zxAnBrgUsrPortBindMacEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortBindMacEnable.setStatus("current")


class _ZxAnBrgUsrPortMacLearnLimit_Type(Integer32):
    """Custom type zxAnBrgUsrPortMacLearnLimit based on Integer32"""
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


_ZxAnBrgUsrPortMacLearnLimit_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortMacLearnLimit_Object = MibTableColumn
zxAnBrgUsrPortMacLearnLimit = _ZxAnBrgUsrPortMacLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 7),
    _ZxAnBrgUsrPortMacLearnLimit_Type()
)
zxAnBrgUsrPortMacLearnLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMacLearnLimit.setStatus("current")
_ZxAnBrgUsrPortMaxMacLearn_Type = Integer32
_ZxAnBrgUsrPortMaxMacLearn_Object = MibTableColumn
zxAnBrgUsrPortMaxMacLearn = _ZxAnBrgUsrPortMaxMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 8),
    _ZxAnBrgUsrPortMaxMacLearn_Type()
)
zxAnBrgUsrPortMaxMacLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxMacLearn.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxMacLearn.setUnits("package")


class _ZxAnBrgUsrPortBrdcastRateLimit_Type(Integer32):
    """Custom type zxAnBrgUsrPortBrdcastRateLimit based on Integer32"""
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


_ZxAnBrgUsrPortBrdcastRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortBrdcastRateLimit_Object = MibTableColumn
zxAnBrgUsrPortBrdcastRateLimit = _ZxAnBrgUsrPortBrdcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 9),
    _ZxAnBrgUsrPortBrdcastRateLimit_Type()
)
zxAnBrgUsrPortBrdcastRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortBrdcastRateLimit.setStatus("current")
_ZxAnBrgUsrPortMaxBroadcastRate_Type = Integer32
_ZxAnBrgUsrPortMaxBroadcastRate_Object = MibTableColumn
zxAnBrgUsrPortMaxBroadcastRate = _ZxAnBrgUsrPortMaxBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 10),
    _ZxAnBrgUsrPortMaxBroadcastRate_Type()
)
zxAnBrgUsrPortMaxBroadcastRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxBroadcastRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxBroadcastRate.setUnits("pps")


class _ZxAnBrgUsrPortDhcpRateLimit_Type(Integer32):
    """Custom type zxAnBrgUsrPortDhcpRateLimit based on Integer32"""
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


_ZxAnBrgUsrPortDhcpRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortDhcpRateLimit_Object = MibTableColumn
zxAnBrgUsrPortDhcpRateLimit = _ZxAnBrgUsrPortDhcpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 11),
    _ZxAnBrgUsrPortDhcpRateLimit_Type()
)
zxAnBrgUsrPortDhcpRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortDhcpRateLimit.setStatus("current")
_ZxAnBrgUsrPortMaxDhcpRate_Type = Integer32
_ZxAnBrgUsrPortMaxDhcpRate_Object = MibTableColumn
zxAnBrgUsrPortMaxDhcpRate = _ZxAnBrgUsrPortMaxDhcpRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 12),
    _ZxAnBrgUsrPortMaxDhcpRate_Type()
)
zxAnBrgUsrPortMaxDhcpRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxDhcpRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxDhcpRate.setUnits("pps")


class _ZxAnBrgUsrPortIgmpRateLimit_Type(Integer32):
    """Custom type zxAnBrgUsrPortIgmpRateLimit based on Integer32"""
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


_ZxAnBrgUsrPortIgmpRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortIgmpRateLimit_Object = MibTableColumn
zxAnBrgUsrPortIgmpRateLimit = _ZxAnBrgUsrPortIgmpRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 13),
    _ZxAnBrgUsrPortIgmpRateLimit_Type()
)
zxAnBrgUsrPortIgmpRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortIgmpRateLimit.setStatus("current")
_ZxAnBrgUsrPortMaxIgmpRate_Type = Integer32
_ZxAnBrgUsrPortMaxIgmpRate_Object = MibTableColumn
zxAnBrgUsrPortMaxIgmpRate = _ZxAnBrgUsrPortMaxIgmpRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 14),
    _ZxAnBrgUsrPortMaxIgmpRate_Type()
)
zxAnBrgUsrPortMaxIgmpRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxIgmpRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxIgmpRate.setUnits("pps")


class _ZxAnBrgUsrPortEncapsType_Type(Integer32):
    """Custom type zxAnBrgUsrPortEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eoaLlc", 1),
          ("eoaVcmux", 2),
          ("pppoaLlc", 3),
          ("pppoaVcmux", 4),
          ("ipoaLlc", 5),
          ("ipoaVcmux", 6),
          ("aoe", 7),
          ("modemMgmt", 8),
          ("auto", 9),
          ("aoeAal0", 10))
    )


_ZxAnBrgUsrPortEncapsType_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortEncapsType_Object = MibTableColumn
zxAnBrgUsrPortEncapsType = _ZxAnBrgUsrPortEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 15),
    _ZxAnBrgUsrPortEncapsType_Type()
)
zxAnBrgUsrPortEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortEncapsType.setStatus("current")


class _ZxAnBrgUserPortBrdcastEnable_Type(Integer32):
    """Custom type zxAnBrgUserPortBrdcastEnable based on Integer32"""
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


_ZxAnBrgUserPortBrdcastEnable_Type.__name__ = "Integer32"
_ZxAnBrgUserPortBrdcastEnable_Object = MibTableColumn
zxAnBrgUserPortBrdcastEnable = _ZxAnBrgUserPortBrdcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 16),
    _ZxAnBrgUserPortBrdcastEnable_Type()
)
zxAnBrgUserPortBrdcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUserPortBrdcastEnable.setStatus("current")


class _ZxAnBrgUserPortFloodEnable_Type(Integer32):
    """Custom type zxAnBrgUserPortFloodEnable based on Integer32"""
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


_ZxAnBrgUserPortFloodEnable_Type.__name__ = "Integer32"
_ZxAnBrgUserPortFloodEnable_Object = MibTableColumn
zxAnBrgUserPortFloodEnable = _ZxAnBrgUserPortFloodEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 17),
    _ZxAnBrgUserPortFloodEnable_Type()
)
zxAnBrgUserPortFloodEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUserPortFloodEnable.setStatus("current")


class _ZxAnBrgUserPortActualEncapsType_Type(Integer32):
    """Custom type zxAnBrgUserPortActualEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eoaLlc", 1),
          ("eoaVcmux", 2),
          ("pppoaLlc", 3),
          ("pppoaVcmux", 4),
          ("ipoaLlc", 5),
          ("ipoaVcmux", 6),
          ("aoe", 7),
          ("modemMgmt", 8),
          ("unknown", 9),
          ("aoeAal0", 10))
    )


_ZxAnBrgUserPortActualEncapsType_Type.__name__ = "Integer32"
_ZxAnBrgUserPortActualEncapsType_Object = MibTableColumn
zxAnBrgUserPortActualEncapsType = _ZxAnBrgUserPortActualEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 18),
    _ZxAnBrgUserPortActualEncapsType_Type()
)
zxAnBrgUserPortActualEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgUserPortActualEncapsType.setStatus("current")


class _ZxAnBrgUserPortVirtualMacEnable_Type(Integer32):
    """Custom type zxAnBrgUserPortVirtualMacEnable based on Integer32"""
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


_ZxAnBrgUserPortVirtualMacEnable_Type.__name__ = "Integer32"
_ZxAnBrgUserPortVirtualMacEnable_Object = MibTableColumn
zxAnBrgUserPortVirtualMacEnable = _ZxAnBrgUserPortVirtualMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 19),
    _ZxAnBrgUserPortVirtualMacEnable_Type()
)
zxAnBrgUserPortVirtualMacEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUserPortVirtualMacEnable.setStatus("current")
_ZxAnBrgUserPortTxNetDataRate_Type = Integer32
_ZxAnBrgUserPortTxNetDataRate_Object = MibTableColumn
zxAnBrgUserPortTxNetDataRate = _ZxAnBrgUserPortTxNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 20),
    _ZxAnBrgUserPortTxNetDataRate_Type()
)
zxAnBrgUserPortTxNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgUserPortTxNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUserPortTxNetDataRate.setUnits("kbps")
_ZxAnBrgUserPortRxNetDataRate_Type = Integer32
_ZxAnBrgUserPortRxNetDataRate_Object = MibTableColumn
zxAnBrgUserPortRxNetDataRate = _ZxAnBrgUserPortRxNetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 21),
    _ZxAnBrgUserPortRxNetDataRate_Type()
)
zxAnBrgUserPortRxNetDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgUserPortRxNetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUserPortRxNetDataRate.setUnits("kbps")


class _ZxAnBrgUsrPortPppoeRateLimit_Type(Integer32):
    """Custom type zxAnBrgUsrPortPppoeRateLimit based on Integer32"""
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


_ZxAnBrgUsrPortPppoeRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortPppoeRateLimit_Object = MibTableColumn
zxAnBrgUsrPortPppoeRateLimit = _ZxAnBrgUsrPortPppoeRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 22),
    _ZxAnBrgUsrPortPppoeRateLimit_Type()
)
zxAnBrgUsrPortPppoeRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortPppoeRateLimit.setStatus("current")


class _ZxAnBrgUsrPortMaxPppoeRate_Type(Integer32):
    """Custom type zxAnBrgUsrPortMaxPppoeRate based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnBrgUsrPortMaxPppoeRate_Type.__name__ = "Integer32"
_ZxAnBrgUsrPortMaxPppoeRate_Object = MibTableColumn
zxAnBrgUsrPortMaxPppoeRate = _ZxAnBrgUsrPortMaxPppoeRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 23),
    _ZxAnBrgUsrPortMaxPppoeRate_Type()
)
zxAnBrgUsrPortMaxPppoeRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxPppoeRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortMaxPppoeRate.setUnits("pps")
_ZxAnBrgUsrPortRowStatus_Type = RowStatus
_ZxAnBrgUsrPortRowStatus_Object = MibTableColumn
zxAnBrgUsrPortRowStatus = _ZxAnBrgUsrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 1, 1, 50),
    _ZxAnBrgUsrPortRowStatus_Type()
)
zxAnBrgUsrPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgUsrPortRowStatus.setStatus("current")
_ZxAnBrgPortStaticHostTable_Object = MibTable
zxAnBrgPortStaticHostTable = _ZxAnBrgPortStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnBrgPortStaticHostTable.setStatus("current")
_ZxAnBrgPortStaticHostEntry_Object = MibTableRow
zxAnBrgPortStaticHostEntry = _ZxAnBrgPortStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 2, 1)
)
zxAnBrgPortStaticHostEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgPortStaticHostIp"),
)
if mibBuilder.loadTexts:
    zxAnBrgPortStaticHostEntry.setStatus("current")
_ZxAnBrgPortStaticHostIp_Type = IpAddress
_ZxAnBrgPortStaticHostIp_Object = MibTableColumn
zxAnBrgPortStaticHostIp = _ZxAnBrgPortStaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 2, 1, 1),
    _ZxAnBrgPortStaticHostIp_Type()
)
zxAnBrgPortStaticHostIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgPortStaticHostIp.setStatus("current")
_ZxAnBrgPortStaticHostRowStatus_Type = RowStatus
_ZxAnBrgPortStaticHostRowStatus_Object = MibTableColumn
zxAnBrgPortStaticHostRowStatus = _ZxAnBrgPortStaticHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 2, 1, 2),
    _ZxAnBrgPortStaticHostRowStatus_Type()
)
zxAnBrgPortStaticHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortStaticHostRowStatus.setStatus("current")
_ZxAnBrgPortStaticMacTable_Object = MibTable
zxAnBrgPortStaticMacTable = _ZxAnBrgPortStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnBrgPortStaticMacTable.setStatus("current")
_ZxAnBrgPortStaticMacEntry_Object = MibTableRow
zxAnBrgPortStaticMacEntry = _ZxAnBrgPortStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 3, 1)
)
zxAnBrgPortStaticMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgPortStaticMac"),
)
if mibBuilder.loadTexts:
    zxAnBrgPortStaticMacEntry.setStatus("current")
_ZxAnBrgPortStaticMac_Type = MacAddress
_ZxAnBrgPortStaticMac_Object = MibTableColumn
zxAnBrgPortStaticMac = _ZxAnBrgPortStaticMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 3, 1, 1),
    _ZxAnBrgPortStaticMac_Type()
)
zxAnBrgPortStaticMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgPortStaticMac.setStatus("current")
_ZxAnSecIfMacBindingRowStatus_Type = RowStatus
_ZxAnSecIfMacBindingRowStatus_Object = MibTableColumn
zxAnSecIfMacBindingRowStatus = _ZxAnSecIfMacBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 3, 1, 2),
    _ZxAnSecIfMacBindingRowStatus_Type()
)
zxAnSecIfMacBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecIfMacBindingRowStatus.setStatus("current")
_ZxAnBrgPortFilterMacTable_Object = MibTable
zxAnBrgPortFilterMacTable = _ZxAnBrgPortFilterMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnBrgPortFilterMacTable.setStatus("current")
_ZxAnBrgPortFilterMacEntry_Object = MibTableRow
zxAnBrgPortFilterMacEntry = _ZxAnBrgPortFilterMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 4, 1)
)
zxAnBrgPortFilterMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgPortFilterMac"),
)
if mibBuilder.loadTexts:
    zxAnBrgPortFilterMacEntry.setStatus("current")
_ZxAnBrgPortFilterMac_Type = MacAddress
_ZxAnBrgPortFilterMac_Object = MibTableColumn
zxAnBrgPortFilterMac = _ZxAnBrgPortFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 4, 1, 1),
    _ZxAnBrgPortFilterMac_Type()
)
zxAnBrgPortFilterMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgPortFilterMac.setStatus("current")
_ZxAnSecIfMacFilterRowStatus_Type = RowStatus
_ZxAnSecIfMacFilterRowStatus_Object = MibTableColumn
zxAnSecIfMacFilterRowStatus = _ZxAnSecIfMacFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 4, 1, 2),
    _ZxAnSecIfMacFilterRowStatus_Type()
)
zxAnSecIfMacFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSecIfMacFilterRowStatus.setStatus("current")
_ZxAnBrgPortIpv6Objects_ObjectIdentity = ObjectIdentity
zxAnBrgPortIpv6Objects = _ZxAnBrgPortIpv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10)
)
_ZxAnBrgPortIpv6IpBindTable_Object = MibTable
zxAnBrgPortIpv6IpBindTable = _ZxAnBrgPortIpv6IpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    zxAnBrgPortIpv6IpBindTable.setStatus("current")
_ZxAnBrgPortIpv6IpBindEntry_Object = MibTableRow
zxAnBrgPortIpv6IpBindEntry = _ZxAnBrgPortIpv6IpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10, 1, 1)
)
zxAnBrgPortIpv6IpBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgPortIpv6IpBindIp"),
)
if mibBuilder.loadTexts:
    zxAnBrgPortIpv6IpBindEntry.setStatus("current")
_ZxAnBrgPortIpv6IpBindIp_Type = InetAddress
_ZxAnBrgPortIpv6IpBindIp_Object = MibTableColumn
zxAnBrgPortIpv6IpBindIp = _ZxAnBrgPortIpv6IpBindIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10, 1, 1, 1),
    _ZxAnBrgPortIpv6IpBindIp_Type()
)
zxAnBrgPortIpv6IpBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgPortIpv6IpBindIp.setStatus("current")
_ZxAnBrgPortIpv6IpBindIpPfxLen_Type = InetAddressPrefixLength
_ZxAnBrgPortIpv6IpBindIpPfxLen_Object = MibTableColumn
zxAnBrgPortIpv6IpBindIpPfxLen = _ZxAnBrgPortIpv6IpBindIpPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10, 1, 1, 2),
    _ZxAnBrgPortIpv6IpBindIpPfxLen_Type()
)
zxAnBrgPortIpv6IpBindIpPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortIpv6IpBindIpPfxLen.setStatus("current")
_ZxAnBrgPortIpv6IpBindRowStatus_Type = RowStatus
_ZxAnBrgPortIpv6IpBindRowStatus_Object = MibTableColumn
zxAnBrgPortIpv6IpBindRowStatus = _ZxAnBrgPortIpv6IpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 10, 1, 1, 10),
    _ZxAnBrgPortIpv6IpBindRowStatus_Type()
)
zxAnBrgPortIpv6IpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgPortIpv6IpBindRowStatus.setStatus("current")
_ZxAnBrgPortStatsObjects_ObjectIdentity = ObjectIdentity
zxAnBrgPortStatsObjects = _ZxAnBrgPortStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 11)
)
_ZxAnBrgPortStatsTable_Object = MibTable
zxAnBrgPortStatsTable = _ZxAnBrgPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 11, 2)
)
if mibBuilder.loadTexts:
    zxAnBrgPortStatsTable.setStatus("current")
_ZxAnBrgPortStatsEntry_Object = MibTableRow
zxAnBrgPortStatsEntry = _ZxAnBrgPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 11, 2, 1)
)
zxAnBrgPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgUsrPortId"),
)
if mibBuilder.loadTexts:
    zxAnBrgPortStatsEntry.setStatus("current")
_ZxAnBrgPortInDiscards_Type = Counter64
_ZxAnBrgPortInDiscards_Object = MibTableColumn
zxAnBrgPortInDiscards = _ZxAnBrgPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 11, 2, 1, 1),
    _ZxAnBrgPortInDiscards_Type()
)
zxAnBrgPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgPortInDiscards.setStatus("current")
_ZxAnBrgPortOutDiscards_Type = Counter64
_ZxAnBrgPortOutDiscards_Object = MibTableColumn
zxAnBrgPortOutDiscards = _ZxAnBrgPortOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 11, 2, 1, 2),
    _ZxAnBrgPortOutDiscards_Type()
)
zxAnBrgPortOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgPortOutDiscards.setStatus("current")
_ZxAnBrgVirtualMacObjects_ObjectIdentity = ObjectIdentity
zxAnBrgVirtualMacObjects = _ZxAnBrgVirtualMacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 12)
)
_ZxAnBrgVirtualMacVlanTable_Object = MibTable
zxAnBrgVirtualMacVlanTable = _ZxAnBrgVirtualMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 12, 2)
)
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacVlanTable.setStatus("current")
_ZxAnBrgVirtualMacVlanEntry_Object = MibTableRow
zxAnBrgVirtualMacVlanEntry = _ZxAnBrgVirtualMacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 12, 2, 1)
)
zxAnBrgVirtualMacVlanEntry.setIndexNames(
    (0, "ZTE-AN-BRG-PORT-MIB", "zxAnBrgVirtualMacVid"),
)
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacVlanEntry.setStatus("current")


class _ZxAnBrgVirtualMacVid_Type(Integer32):
    """Custom type zxAnBrgVirtualMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnBrgVirtualMacVid_Type.__name__ = "Integer32"
_ZxAnBrgVirtualMacVid_Object = MibTableColumn
zxAnBrgVirtualMacVid = _ZxAnBrgVirtualMacVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 12, 2, 1, 1),
    _ZxAnBrgVirtualMacVid_Type()
)
zxAnBrgVirtualMacVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacVid.setStatus("current")
_ZxAnBrgVirtualMacVlanRowStatus_Type = RowStatus
_ZxAnBrgVirtualMacVlanRowStatus_Object = MibTableColumn
zxAnBrgVirtualMacVlanRowStatus = _ZxAnBrgVirtualMacVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 1, 12, 2, 1, 50),
    _ZxAnBrgVirtualMacVlanRowStatus_Type()
)
zxAnBrgVirtualMacVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacVlanRowStatus.setStatus("current")
_ZxAnBrgPortGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnBrgPortGlobalObjects = _ZxAnBrgPortGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2)
)
_ZxAnBrgPktRateLimit_ObjectIdentity = ObjectIdentity
zxAnBrgPktRateLimit = _ZxAnBrgPktRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1)
)


class _ZxAnBrgBroadcastRateLimit_Type(Integer32):
    """Custom type zxAnBrgBroadcastRateLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnBrgBroadcastRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgBroadcastRateLimit_Object = MibScalar
zxAnBrgBroadcastRateLimit = _ZxAnBrgBroadcastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 1),
    _ZxAnBrgBroadcastRateLimit_Type()
)
zxAnBrgBroadcastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgBroadcastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgBroadcastRateLimit.setUnits("pps")


class _ZxAnBrgMulticastRateLimit_Type(Integer32):
    """Custom type zxAnBrgMulticastRateLimit based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnBrgMulticastRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgMulticastRateLimit_Object = MibScalar
zxAnBrgMulticastRateLimit = _ZxAnBrgMulticastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 2),
    _ZxAnBrgMulticastRateLimit_Type()
)
zxAnBrgMulticastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgMulticastRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgMulticastRateLimit.setUnits("pps")


class _ZxAnBrgFloodingRateLimit_Type(Integer32):
    """Custom type zxAnBrgFloodingRateLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnBrgFloodingRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgFloodingRateLimit_Object = MibScalar
zxAnBrgFloodingRateLimit = _ZxAnBrgFloodingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 3),
    _ZxAnBrgFloodingRateLimit_Type()
)
zxAnBrgFloodingRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgFloodingRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgFloodingRateLimit.setUnits("pps")


class _ZxAnBrgBpduFloodingRateLimit_Type(Integer32):
    """Custom type zxAnBrgBpduFloodingRateLimit based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnBrgBpduFloodingRateLimit_Type.__name__ = "Integer32"
_ZxAnBrgBpduFloodingRateLimit_Object = MibScalar
zxAnBrgBpduFloodingRateLimit = _ZxAnBrgBpduFloodingRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 4),
    _ZxAnBrgBpduFloodingRateLimit_Type()
)
zxAnBrgBpduFloodingRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgBpduFloodingRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnBrgBpduFloodingRateLimit.setUnits("pps")


class _ZxAnBrgUnknownUcastFloodingEn_Type(Integer32):
    """Custom type zxAnBrgUnknownUcastFloodingEn based on Integer32"""
    defaultValue = 1

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


_ZxAnBrgUnknownUcastFloodingEn_Type.__name__ = "Integer32"
_ZxAnBrgUnknownUcastFloodingEn_Object = MibScalar
zxAnBrgUnknownUcastFloodingEn = _ZxAnBrgUnknownUcastFloodingEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 5),
    _ZxAnBrgUnknownUcastFloodingEn_Type()
)
zxAnBrgUnknownUcastFloodingEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgUnknownUcastFloodingEn.setStatus("current")


class _ZxAnBrgUnknownMcastFloodingEn_Type(Integer32):
    """Custom type zxAnBrgUnknownMcastFloodingEn based on Integer32"""
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


_ZxAnBrgUnknownMcastFloodingEn_Type.__name__ = "Integer32"
_ZxAnBrgUnknownMcastFloodingEn_Object = MibScalar
zxAnBrgUnknownMcastFloodingEn = _ZxAnBrgUnknownMcastFloodingEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 1, 6),
    _ZxAnBrgUnknownMcastFloodingEn_Type()
)
zxAnBrgUnknownMcastFloodingEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnBrgUnknownMcastFloodingEn.setStatus("current")
_ZxAnBrgVirtualMac_ObjectIdentity = ObjectIdentity
zxAnBrgVirtualMac = _ZxAnBrgVirtualMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 2)
)


class _ZxAnBrgVirtualMacKey_Type(Integer32):
    """Custom type zxAnBrgVirtualMacKey based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnBrgVirtualMacKey_Type.__name__ = "Integer32"
_ZxAnBrgVirtualMacKey_Object = MibScalar
zxAnBrgVirtualMacKey = _ZxAnBrgVirtualMacKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 2, 1),
    _ZxAnBrgVirtualMacKey_Type()
)
zxAnBrgVirtualMacKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacKey.setStatus("current")


class _ZxAnBrgVirtualMacFormat_Type(Integer32):
    """Custom type zxAnBrgVirtualMacFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tpsa", 1),
          ("magyarTel", 2))
    )


_ZxAnBrgVirtualMacFormat_Type.__name__ = "Integer32"
_ZxAnBrgVirtualMacFormat_Object = MibScalar
zxAnBrgVirtualMacFormat = _ZxAnBrgVirtualMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 2, 2),
    _ZxAnBrgVirtualMacFormat_Type()
)
zxAnBrgVirtualMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacFormat.setStatus("current")


class _ZxAnBrgVirtualMacUserDefined_Type(Integer32):
    """Custom type zxAnBrgVirtualMacUserDefined based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnBrgVirtualMacUserDefined_Type.__name__ = "Integer32"
_ZxAnBrgVirtualMacUserDefined_Object = MibScalar
zxAnBrgVirtualMacUserDefined = _ZxAnBrgVirtualMacUserDefined_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 2, 3),
    _ZxAnBrgVirtualMacUserDefined_Type()
)
zxAnBrgVirtualMacUserDefined.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnBrgVirtualMacUserDefined.setStatus("current")


class _ZxAnBrgPortCapabilities_Type(Bits):
    """Custom type zxAnBrgPortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("vdslAtmPtmCoexist", 0),
          ("shdslAtmEfmCoexist", 1),
          ("supportPppoeRateLimit", 2))
    )

_ZxAnBrgPortCapabilities_Type.__name__ = "Bits"
_ZxAnBrgPortCapabilities_Object = MibScalar
zxAnBrgPortCapabilities = _ZxAnBrgPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 2, 50),
    _ZxAnBrgPortCapabilities_Type()
)
zxAnBrgPortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnBrgPortCapabilities.setStatus("current")
_ZxAnBrgPortTrapObjects_ObjectIdentity = ObjectIdentity
zxAnBrgPortTrapObjects = _ZxAnBrgPortTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-BRG-PORT-MIB",
    **{"zxAnBrgPortMib": zxAnBrgPortMib,
       "zxAnBrgPortObjects": zxAnBrgPortObjects,
       "zxAnBrgUsrSidePortTable": zxAnBrgUsrSidePortTable,
       "zxAnBrgUsrSidePortEntry": zxAnBrgUsrSidePortEntry,
       "zxAnBrgUsrPortId": zxAnBrgUsrPortId,
       "zxAnBrgUsrPortAdminStatus": zxAnBrgUsrPortAdminStatus,
       "zxAnBrgUsrPortPvcVpi": zxAnBrgUsrPortPvcVpi,
       "zxAnBrgUsrPortPvcVci": zxAnBrgUsrPortPvcVci,
       "zxAnBrgUsrPortBindIpEnable": zxAnBrgUsrPortBindIpEnable,
       "zxAnBrgUsrPortBindMacEnable": zxAnBrgUsrPortBindMacEnable,
       "zxAnBrgUsrPortMacLearnLimit": zxAnBrgUsrPortMacLearnLimit,
       "zxAnBrgUsrPortMaxMacLearn": zxAnBrgUsrPortMaxMacLearn,
       "zxAnBrgUsrPortBrdcastRateLimit": zxAnBrgUsrPortBrdcastRateLimit,
       "zxAnBrgUsrPortMaxBroadcastRate": zxAnBrgUsrPortMaxBroadcastRate,
       "zxAnBrgUsrPortDhcpRateLimit": zxAnBrgUsrPortDhcpRateLimit,
       "zxAnBrgUsrPortMaxDhcpRate": zxAnBrgUsrPortMaxDhcpRate,
       "zxAnBrgUsrPortIgmpRateLimit": zxAnBrgUsrPortIgmpRateLimit,
       "zxAnBrgUsrPortMaxIgmpRate": zxAnBrgUsrPortMaxIgmpRate,
       "zxAnBrgUsrPortEncapsType": zxAnBrgUsrPortEncapsType,
       "zxAnBrgUserPortBrdcastEnable": zxAnBrgUserPortBrdcastEnable,
       "zxAnBrgUserPortFloodEnable": zxAnBrgUserPortFloodEnable,
       "zxAnBrgUserPortActualEncapsType": zxAnBrgUserPortActualEncapsType,
       "zxAnBrgUserPortVirtualMacEnable": zxAnBrgUserPortVirtualMacEnable,
       "zxAnBrgUserPortTxNetDataRate": zxAnBrgUserPortTxNetDataRate,
       "zxAnBrgUserPortRxNetDataRate": zxAnBrgUserPortRxNetDataRate,
       "zxAnBrgUsrPortPppoeRateLimit": zxAnBrgUsrPortPppoeRateLimit,
       "zxAnBrgUsrPortMaxPppoeRate": zxAnBrgUsrPortMaxPppoeRate,
       "zxAnBrgUsrPortRowStatus": zxAnBrgUsrPortRowStatus,
       "zxAnBrgPortStaticHostTable": zxAnBrgPortStaticHostTable,
       "zxAnBrgPortStaticHostEntry": zxAnBrgPortStaticHostEntry,
       "zxAnBrgPortStaticHostIp": zxAnBrgPortStaticHostIp,
       "zxAnBrgPortStaticHostRowStatus": zxAnBrgPortStaticHostRowStatus,
       "zxAnBrgPortStaticMacTable": zxAnBrgPortStaticMacTable,
       "zxAnBrgPortStaticMacEntry": zxAnBrgPortStaticMacEntry,
       "zxAnBrgPortStaticMac": zxAnBrgPortStaticMac,
       "zxAnSecIfMacBindingRowStatus": zxAnSecIfMacBindingRowStatus,
       "zxAnBrgPortFilterMacTable": zxAnBrgPortFilterMacTable,
       "zxAnBrgPortFilterMacEntry": zxAnBrgPortFilterMacEntry,
       "zxAnBrgPortFilterMac": zxAnBrgPortFilterMac,
       "zxAnSecIfMacFilterRowStatus": zxAnSecIfMacFilterRowStatus,
       "zxAnBrgPortIpv6Objects": zxAnBrgPortIpv6Objects,
       "zxAnBrgPortIpv6IpBindTable": zxAnBrgPortIpv6IpBindTable,
       "zxAnBrgPortIpv6IpBindEntry": zxAnBrgPortIpv6IpBindEntry,
       "zxAnBrgPortIpv6IpBindIp": zxAnBrgPortIpv6IpBindIp,
       "zxAnBrgPortIpv6IpBindIpPfxLen": zxAnBrgPortIpv6IpBindIpPfxLen,
       "zxAnBrgPortIpv6IpBindRowStatus": zxAnBrgPortIpv6IpBindRowStatus,
       "zxAnBrgPortStatsObjects": zxAnBrgPortStatsObjects,
       "zxAnBrgPortStatsTable": zxAnBrgPortStatsTable,
       "zxAnBrgPortStatsEntry": zxAnBrgPortStatsEntry,
       "zxAnBrgPortInDiscards": zxAnBrgPortInDiscards,
       "zxAnBrgPortOutDiscards": zxAnBrgPortOutDiscards,
       "zxAnBrgVirtualMacObjects": zxAnBrgVirtualMacObjects,
       "zxAnBrgVirtualMacVlanTable": zxAnBrgVirtualMacVlanTable,
       "zxAnBrgVirtualMacVlanEntry": zxAnBrgVirtualMacVlanEntry,
       "zxAnBrgVirtualMacVid": zxAnBrgVirtualMacVid,
       "zxAnBrgVirtualMacVlanRowStatus": zxAnBrgVirtualMacVlanRowStatus,
       "zxAnBrgPortGlobalObjects": zxAnBrgPortGlobalObjects,
       "zxAnBrgPktRateLimit": zxAnBrgPktRateLimit,
       "zxAnBrgBroadcastRateLimit": zxAnBrgBroadcastRateLimit,
       "zxAnBrgMulticastRateLimit": zxAnBrgMulticastRateLimit,
       "zxAnBrgFloodingRateLimit": zxAnBrgFloodingRateLimit,
       "zxAnBrgBpduFloodingRateLimit": zxAnBrgBpduFloodingRateLimit,
       "zxAnBrgUnknownUcastFloodingEn": zxAnBrgUnknownUcastFloodingEn,
       "zxAnBrgUnknownMcastFloodingEn": zxAnBrgUnknownMcastFloodingEn,
       "zxAnBrgVirtualMac": zxAnBrgVirtualMac,
       "zxAnBrgVirtualMacKey": zxAnBrgVirtualMacKey,
       "zxAnBrgVirtualMacFormat": zxAnBrgVirtualMacFormat,
       "zxAnBrgVirtualMacUserDefined": zxAnBrgVirtualMacUserDefined,
       "zxAnBrgPortCapabilities": zxAnBrgPortCapabilities,
       "zxAnBrgPortTrapObjects": zxAnBrgPortTrapObjects}
)
