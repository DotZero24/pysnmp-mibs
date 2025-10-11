# SNMP MIB module (ZTE-AN-IEEE1588-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-IEEE1588-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:59 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnIeee1588Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPtpMgmt_ObjectIdentity = ObjectIdentity
zxAnPtpMgmt = _ZxAnPtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1)
)
_ZxAnPtpTable_Object = MibTable
zxAnPtpTable = _ZxAnPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnPtpTable.setStatus("current")
_ZxAnPtpEntry_Object = MibTableRow
zxAnPtpEntry = _ZxAnPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1)
)
zxAnPtpEntry.setIndexNames(
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpRack"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpShelf"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpSlot"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpId"),
)
if mibBuilder.loadTexts:
    zxAnPtpEntry.setStatus("current")
_ZxAnPtpRack_Type = Integer32
_ZxAnPtpRack_Object = MibTableColumn
zxAnPtpRack = _ZxAnPtpRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 1),
    _ZxAnPtpRack_Type()
)
zxAnPtpRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpRack.setStatus("current")
_ZxAnPtpShelf_Type = Integer32
_ZxAnPtpShelf_Object = MibTableColumn
zxAnPtpShelf = _ZxAnPtpShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 2),
    _ZxAnPtpShelf_Type()
)
zxAnPtpShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpShelf.setStatus("current")
_ZxAnPtpSlot_Type = Integer32
_ZxAnPtpSlot_Object = MibTableColumn
zxAnPtpSlot = _ZxAnPtpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 3),
    _ZxAnPtpSlot_Type()
)
zxAnPtpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpSlot.setStatus("current")


class _ZxAnPtpId_Type(Integer32):
    """Custom type zxAnPtpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnPtpId_Type.__name__ = "Integer32"
_ZxAnPtpId_Object = MibTableColumn
zxAnPtpId = _ZxAnPtpId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 4),
    _ZxAnPtpId_Type()
)
zxAnPtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpId.setStatus("current")


class _ZxAnPtpClockType_Type(Integer32):
    """Custom type zxAnPtpClockType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordinary", 1),
          ("boundary", 2))
    )


_ZxAnPtpClockType_Type.__name__ = "Integer32"
_ZxAnPtpClockType_Object = MibTableColumn
zxAnPtpClockType = _ZxAnPtpClockType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 5),
    _ZxAnPtpClockType_Type()
)
zxAnPtpClockType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpClockType.setStatus("current")


class _ZxAnPtpSlaveOnly_Type(TruthValue):
    """Custom type zxAnPtpSlaveOnly based on TruthValue"""
    defaultValue = 1


_ZxAnPtpSlaveOnly_Type.__name__ = "TruthValue"
_ZxAnPtpSlaveOnly_Object = MibTableColumn
zxAnPtpSlaveOnly = _ZxAnPtpSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 6),
    _ZxAnPtpSlaveOnly_Type()
)
zxAnPtpSlaveOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpSlaveOnly.setStatus("current")


class _ZxAnPtpDomainNumber_Type(Integer32):
    """Custom type zxAnPtpDomainNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnPtpDomainNumber_Type.__name__ = "Integer32"
_ZxAnPtpDomainNumber_Object = MibTableColumn
zxAnPtpDomainNumber = _ZxAnPtpDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 7),
    _ZxAnPtpDomainNumber_Type()
)
zxAnPtpDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpDomainNumber.setStatus("current")


class _ZxAnPtpProtocolIpAddrType_Type(InetAddressType):
    """Custom type zxAnPtpProtocolIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnPtpProtocolIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnPtpProtocolIpAddrType_Object = MibTableColumn
zxAnPtpProtocolIpAddrType = _ZxAnPtpProtocolIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 8),
    _ZxAnPtpProtocolIpAddrType_Type()
)
zxAnPtpProtocolIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpProtocolIpAddrType.setStatus("current")
_ZxAnPtpProtocolIpAddress_Type = InetAddress
_ZxAnPtpProtocolIpAddress_Object = MibTableColumn
zxAnPtpProtocolIpAddress = _ZxAnPtpProtocolIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 9),
    _ZxAnPtpProtocolIpAddress_Type()
)
zxAnPtpProtocolIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpProtocolIpAddress.setStatus("current")


class _ZxAnPtpEthWorkMode_Type(Integer32):
    """Custom type zxAnPtpEthWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncE", 1),
          ("notSyncE", 2))
    )


_ZxAnPtpEthWorkMode_Type.__name__ = "Integer32"
_ZxAnPtpEthWorkMode_Object = MibTableColumn
zxAnPtpEthWorkMode = _ZxAnPtpEthWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 10),
    _ZxAnPtpEthWorkMode_Type()
)
zxAnPtpEthWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpEthWorkMode.setStatus("current")


class _ZxAnPtpPacketsMode_Type(Integer32):
    """Custom type zxAnPtpPacketsMode based on Integer32"""
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
        *(("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_ZxAnPtpPacketsMode_Type.__name__ = "Integer32"
_ZxAnPtpPacketsMode_Object = MibTableColumn
zxAnPtpPacketsMode = _ZxAnPtpPacketsMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 11),
    _ZxAnPtpPacketsMode_Type()
)
zxAnPtpPacketsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpPacketsMode.setStatus("current")


class _ZxAnPtpTwoStepFlag_Type(TruthValue):
    """Custom type zxAnPtpTwoStepFlag based on TruthValue"""
    defaultValue = 2


_ZxAnPtpTwoStepFlag_Type.__name__ = "TruthValue"
_ZxAnPtpTwoStepFlag_Object = MibTableColumn
zxAnPtpTwoStepFlag = _ZxAnPtpTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 12),
    _ZxAnPtpTwoStepFlag_Type()
)
zxAnPtpTwoStepFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpTwoStepFlag.setStatus("current")


class _ZxAnPtpSendPacketsRate_Type(Integer32):
    """Custom type zxAnPtpSendPacketsRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_ZxAnPtpSendPacketsRate_Type.__name__ = "Integer32"
_ZxAnPtpSendPacketsRate_Object = MibTableColumn
zxAnPtpSendPacketsRate = _ZxAnPtpSendPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 13),
    _ZxAnPtpSendPacketsRate_Type()
)
zxAnPtpSendPacketsRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpSendPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPtpSendPacketsRate.setUnits("pps")


class _ZxAnPtpClockStatus_Type(Integer32):
    """Custom type zxAnPtpClockStatus based on Integer32"""
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
        *(("freeRun", 1),
          ("holdover", 2),
          ("acquisition", 3),
          ("locked", 4))
    )


_ZxAnPtpClockStatus_Type.__name__ = "Integer32"
_ZxAnPtpClockStatus_Object = MibTableColumn
zxAnPtpClockStatus = _ZxAnPtpClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 14),
    _ZxAnPtpClockStatus_Type()
)
zxAnPtpClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPtpClockStatus.setStatus("current")


class _ZxAnPtpUtcTime_Type(DisplayString):
    """Custom type zxAnPtpUtcTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_ZxAnPtpUtcTime_Type.__name__ = "DisplayString"
_ZxAnPtpUtcTime_Object = MibTableColumn
zxAnPtpUtcTime = _ZxAnPtpUtcTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 15),
    _ZxAnPtpUtcTime_Type()
)
zxAnPtpUtcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPtpUtcTime.setStatus("current")
_ZxAnPtpRowStatus_Type = RowStatus
_ZxAnPtpRowStatus_Object = MibTableColumn
zxAnPtpRowStatus = _ZxAnPtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 2, 1, 50),
    _ZxAnPtpRowStatus_Type()
)
zxAnPtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpRowStatus.setStatus("current")
_ZxAnPtpRemoteSrcTable_Object = MibTable
zxAnPtpRemoteSrcTable = _ZxAnPtpRemoteSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcTable.setStatus("current")
_ZxAnPtpRemoteSrcEntry_Object = MibTableRow
zxAnPtpRemoteSrcEntry = _ZxAnPtpRemoteSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1)
)
zxAnPtpRemoteSrcEntry.setIndexNames(
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpRack"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpShelf"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpSlot"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpId"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpRemoteSrcIpAddrType"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnPtpRemoteSrcIpAddress"),
)
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcEntry.setStatus("current")


class _ZxAnPtpRemoteSrcIpAddrType_Type(InetAddressType):
    """Custom type zxAnPtpRemoteSrcIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnPtpRemoteSrcIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnPtpRemoteSrcIpAddrType_Object = MibTableColumn
zxAnPtpRemoteSrcIpAddrType = _ZxAnPtpRemoteSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 1),
    _ZxAnPtpRemoteSrcIpAddrType_Type()
)
zxAnPtpRemoteSrcIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcIpAddrType.setStatus("current")
_ZxAnPtpRemoteSrcIpAddress_Type = InetAddress
_ZxAnPtpRemoteSrcIpAddress_Object = MibTableColumn
zxAnPtpRemoteSrcIpAddress = _ZxAnPtpRemoteSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 2),
    _ZxAnPtpRemoteSrcIpAddress_Type()
)
zxAnPtpRemoteSrcIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcIpAddress.setStatus("current")


class _ZxAnPtpRemoteSrcDomainNumber_Type(Integer32):
    """Custom type zxAnPtpRemoteSrcDomainNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnPtpRemoteSrcDomainNumber_Type.__name__ = "Integer32"
_ZxAnPtpRemoteSrcDomainNumber_Object = MibTableColumn
zxAnPtpRemoteSrcDomainNumber = _ZxAnPtpRemoteSrcDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 3),
    _ZxAnPtpRemoteSrcDomainNumber_Type()
)
zxAnPtpRemoteSrcDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcDomainNumber.setStatus("current")


class _ZxAnPtpRemoteSrcPathDelayAdjust_Type(Integer32):
    """Custom type zxAnPtpRemoteSrcPathDelayAdjust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_ZxAnPtpRemoteSrcPathDelayAdjust_Type.__name__ = "Integer32"
_ZxAnPtpRemoteSrcPathDelayAdjust_Object = MibTableColumn
zxAnPtpRemoteSrcPathDelayAdjust = _ZxAnPtpRemoteSrcPathDelayAdjust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 4),
    _ZxAnPtpRemoteSrcPathDelayAdjust_Type()
)
zxAnPtpRemoteSrcPathDelayAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcPathDelayAdjust.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcPathDelayAdjust.setUnits("ns")


class _ZxAnPtpRemoteSrcWorkStatus_Type(Integer32):
    """Custom type zxAnPtpRemoteSrcWorkStatus based on Integer32"""
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
          ("active", 2),
          ("standby", 3))
    )


_ZxAnPtpRemoteSrcWorkStatus_Type.__name__ = "Integer32"
_ZxAnPtpRemoteSrcWorkStatus_Object = MibTableColumn
zxAnPtpRemoteSrcWorkStatus = _ZxAnPtpRemoteSrcWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 5),
    _ZxAnPtpRemoteSrcWorkStatus_Type()
)
zxAnPtpRemoteSrcWorkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcWorkStatus.setStatus("current")
_ZxAnPtpRemoteSrcRowStatus_Type = RowStatus
_ZxAnPtpRemoteSrcRowStatus_Object = MibTableColumn
zxAnPtpRemoteSrcRowStatus = _ZxAnPtpRemoteSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 1, 3, 1, 50),
    _ZxAnPtpRemoteSrcRowStatus_Type()
)
zxAnPtpRemoteSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPtpRemoteSrcRowStatus.setStatus("current")
_ZxAnSyncTimeClkSrcMgmt_ObjectIdentity = ObjectIdentity
zxAnSyncTimeClkSrcMgmt = _ZxAnSyncTimeClkSrcMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2)
)
_ZxAnSyncTime1ppsSrcTable_Object = MibTable
zxAnSyncTime1ppsSrcTable = _ZxAnSyncTime1ppsSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcTable.setStatus("current")
_ZxAnSyncTime1ppsSrcEntry_Object = MibTableRow
zxAnSyncTime1ppsSrcEntry = _ZxAnSyncTime1ppsSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1)
)
zxAnSyncTime1ppsSrcEntry.setIndexNames(
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTime1ppsSrcRack"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTime1ppsSrcShelf"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTime1ppsSrcSlot"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTime1ppsSrcId"),
)
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcEntry.setStatus("current")
_ZxAnSyncTime1ppsSrcRack_Type = Integer32
_ZxAnSyncTime1ppsSrcRack_Object = MibTableColumn
zxAnSyncTime1ppsSrcRack = _ZxAnSyncTime1ppsSrcRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 1),
    _ZxAnSyncTime1ppsSrcRack_Type()
)
zxAnSyncTime1ppsSrcRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcRack.setStatus("current")
_ZxAnSyncTime1ppsSrcShelf_Type = Integer32
_ZxAnSyncTime1ppsSrcShelf_Object = MibTableColumn
zxAnSyncTime1ppsSrcShelf = _ZxAnSyncTime1ppsSrcShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 2),
    _ZxAnSyncTime1ppsSrcShelf_Type()
)
zxAnSyncTime1ppsSrcShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcShelf.setStatus("current")
_ZxAnSyncTime1ppsSrcSlot_Type = Integer32
_ZxAnSyncTime1ppsSrcSlot_Object = MibTableColumn
zxAnSyncTime1ppsSrcSlot = _ZxAnSyncTime1ppsSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 3),
    _ZxAnSyncTime1ppsSrcSlot_Type()
)
zxAnSyncTime1ppsSrcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcSlot.setStatus("current")


class _ZxAnSyncTime1ppsSrcId_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnSyncTime1ppsSrcId_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcId_Object = MibTableColumn
zxAnSyncTime1ppsSrcId = _ZxAnSyncTime1ppsSrcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 4),
    _ZxAnSyncTime1ppsSrcId_Type()
)
zxAnSyncTime1ppsSrcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcId.setStatus("current")


class _ZxAnSyncTime1ppsSrcSignalType_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcSignalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptp", 1),
          ("onepps", 2))
    )


_ZxAnSyncTime1ppsSrcSignalType_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcSignalType_Object = MibTableColumn
zxAnSyncTime1ppsSrcSignalType = _ZxAnSyncTime1ppsSrcSignalType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 5),
    _ZxAnSyncTime1ppsSrcSignalType_Type()
)
zxAnSyncTime1ppsSrcSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcSignalType.setStatus("current")


class _ZxAnSyncTime1ppsSrcPriority_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSyncTime1ppsSrcPriority_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcPriority_Object = MibTableColumn
zxAnSyncTime1ppsSrcPriority = _ZxAnSyncTime1ppsSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 6),
    _ZxAnSyncTime1ppsSrcPriority_Type()
)
zxAnSyncTime1ppsSrcPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcPriority.setStatus("current")


class _ZxAnSyncTime1ppsSrcPortType_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("typeTtl", 1),
          ("type422", 2))
    )


_ZxAnSyncTime1ppsSrcPortType_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcPortType_Object = MibTableColumn
zxAnSyncTime1ppsSrcPortType = _ZxAnSyncTime1ppsSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 7),
    _ZxAnSyncTime1ppsSrcPortType_Type()
)
zxAnSyncTime1ppsSrcPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcPortType.setStatus("current")


class _ZxAnSyncTime1ppsSrcPort_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnSyncTime1ppsSrcPort_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcPort_Object = MibTableColumn
zxAnSyncTime1ppsSrcPort = _ZxAnSyncTime1ppsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 8),
    _ZxAnSyncTime1ppsSrcPort_Type()
)
zxAnSyncTime1ppsSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcPort.setStatus("current")


class _ZxAnSyncTime1ppsSrcWorkStatus_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcWorkStatus based on Integer32"""
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
          ("active", 2),
          ("standby", 3))
    )


_ZxAnSyncTime1ppsSrcWorkStatus_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcWorkStatus_Object = MibTableColumn
zxAnSyncTime1ppsSrcWorkStatus = _ZxAnSyncTime1ppsSrcWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 9),
    _ZxAnSyncTime1ppsSrcWorkStatus_Type()
)
zxAnSyncTime1ppsSrcWorkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcWorkStatus.setStatus("current")


class _ZxAnSyncTime1ppsSrcValidStatus_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcValidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_ZxAnSyncTime1ppsSrcValidStatus_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcValidStatus_Object = MibTableColumn
zxAnSyncTime1ppsSrcValidStatus = _ZxAnSyncTime1ppsSrcValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 10),
    _ZxAnSyncTime1ppsSrcValidStatus_Type()
)
zxAnSyncTime1ppsSrcValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcValidStatus.setStatus("current")


class _ZxAnSyncTime1ppsSrcPortStatus_Type(Integer32):
    """Custom type zxAnSyncTime1ppsSrcPortStatus based on Integer32"""
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
          ("normal", 2),
          ("signalLos", 3))
    )


_ZxAnSyncTime1ppsSrcPortStatus_Type.__name__ = "Integer32"
_ZxAnSyncTime1ppsSrcPortStatus_Object = MibTableColumn
zxAnSyncTime1ppsSrcPortStatus = _ZxAnSyncTime1ppsSrcPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 11),
    _ZxAnSyncTime1ppsSrcPortStatus_Type()
)
zxAnSyncTime1ppsSrcPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcPortStatus.setStatus("current")
_ZxAnSyncTime1ppsSrcRowStatus_Type = RowStatus
_ZxAnSyncTime1ppsSrcRowStatus_Object = MibTableColumn
zxAnSyncTime1ppsSrcRowStatus = _ZxAnSyncTime1ppsSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 3, 1, 30),
    _ZxAnSyncTime1ppsSrcRowStatus_Type()
)
zxAnSyncTime1ppsSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTime1ppsSrcRowStatus.setStatus("current")
_ZxAnSyncTimeTodSrcTable_Object = MibTable
zxAnSyncTimeTodSrcTable = _ZxAnSyncTimeTodSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcTable.setStatus("current")
_ZxAnSyncTimeTodSrcEntry_Object = MibTableRow
zxAnSyncTimeTodSrcEntry = _ZxAnSyncTimeTodSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1)
)
zxAnSyncTimeTodSrcEntry.setIndexNames(
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeTodSrcRack"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeTodSrcShelf"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeTodSrcSlot"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeTodSrcPort"),
)
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcEntry.setStatus("current")
_ZxAnSyncTimeTodSrcRack_Type = Integer32
_ZxAnSyncTimeTodSrcRack_Object = MibTableColumn
zxAnSyncTimeTodSrcRack = _ZxAnSyncTimeTodSrcRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 1),
    _ZxAnSyncTimeTodSrcRack_Type()
)
zxAnSyncTimeTodSrcRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcRack.setStatus("current")
_ZxAnSyncTimeTodSrcShelf_Type = Integer32
_ZxAnSyncTimeTodSrcShelf_Object = MibTableColumn
zxAnSyncTimeTodSrcShelf = _ZxAnSyncTimeTodSrcShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 2),
    _ZxAnSyncTimeTodSrcShelf_Type()
)
zxAnSyncTimeTodSrcShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcShelf.setStatus("current")
_ZxAnSyncTimeTodSrcSlot_Type = Integer32
_ZxAnSyncTimeTodSrcSlot_Object = MibTableColumn
zxAnSyncTimeTodSrcSlot = _ZxAnSyncTimeTodSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 3),
    _ZxAnSyncTimeTodSrcSlot_Type()
)
zxAnSyncTimeTodSrcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcSlot.setStatus("current")
_ZxAnSyncTimeTodSrcPort_Type = Integer32
_ZxAnSyncTimeTodSrcPort_Object = MibTableColumn
zxAnSyncTimeTodSrcPort = _ZxAnSyncTimeTodSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 4),
    _ZxAnSyncTimeTodSrcPort_Type()
)
zxAnSyncTimeTodSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcPort.setStatus("current")


class _ZxAnSyncTimeTodSrcSignalType_Type(Integer32):
    """Custom type zxAnSyncTimeTodSrcSignalType based on Integer32"""
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
        *(("gps", 1),
          ("chinaMobile", 2),
          ("chinaUnicom", 3),
          ("chinaTelecom", 4))
    )


_ZxAnSyncTimeTodSrcSignalType_Type.__name__ = "Integer32"
_ZxAnSyncTimeTodSrcSignalType_Object = MibTableColumn
zxAnSyncTimeTodSrcSignalType = _ZxAnSyncTimeTodSrcSignalType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 5),
    _ZxAnSyncTimeTodSrcSignalType_Type()
)
zxAnSyncTimeTodSrcSignalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcSignalType.setStatus("current")


class _ZxAnSyncTimeTodSrcYearAdjust_Type(Integer32):
    """Custom type zxAnSyncTimeTodSrcYearAdjust based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2050),
    )


_ZxAnSyncTimeTodSrcYearAdjust_Type.__name__ = "Integer32"
_ZxAnSyncTimeTodSrcYearAdjust_Object = MibTableColumn
zxAnSyncTimeTodSrcYearAdjust = _ZxAnSyncTimeTodSrcYearAdjust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 6),
    _ZxAnSyncTimeTodSrcYearAdjust_Type()
)
zxAnSyncTimeTodSrcYearAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcYearAdjust.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcYearAdjust.setUnits("year")


class _ZxAnSyncTimeTodSrcPortStatus_Type(Integer32):
    """Custom type zxAnSyncTimeTodSrcPortStatus based on Integer32"""
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
          ("normal", 2),
          ("signalLos", 3))
    )


_ZxAnSyncTimeTodSrcPortStatus_Type.__name__ = "Integer32"
_ZxAnSyncTimeTodSrcPortStatus_Object = MibTableColumn
zxAnSyncTimeTodSrcPortStatus = _ZxAnSyncTimeTodSrcPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 7),
    _ZxAnSyncTimeTodSrcPortStatus_Type()
)
zxAnSyncTimeTodSrcPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcPortStatus.setStatus("current")
_ZxAnSyncTimeTodSrcRowStatus_Type = RowStatus
_ZxAnSyncTimeTodSrcRowStatus_Object = MibTableColumn
zxAnSyncTimeTodSrcRowStatus = _ZxAnSyncTimeTodSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 4, 1, 30),
    _ZxAnSyncTimeTodSrcRowStatus_Type()
)
zxAnSyncTimeTodSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeTodSrcRowStatus.setStatus("current")
_ZxAnSyncTimeOutputPortTable_Object = MibTable
zxAnSyncTimeOutputPortTable = _ZxAnSyncTimeOutputPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortTable.setStatus("current")
_ZxAnSyncTimeOutputPortEntry_Object = MibTableRow
zxAnSyncTimeOutputPortEntry = _ZxAnSyncTimeOutputPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1)
)
zxAnSyncTimeOutputPortEntry.setIndexNames(
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeOutputRack"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeOutputShelf"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeOutputSlot"),
    (0, "ZTE-AN-IEEE1588-MIB", "zxAnSyncTimeOutputPort"),
)
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortEntry.setStatus("current")
_ZxAnSyncTimeOutputRack_Type = Integer32
_ZxAnSyncTimeOutputRack_Object = MibTableColumn
zxAnSyncTimeOutputRack = _ZxAnSyncTimeOutputRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 1),
    _ZxAnSyncTimeOutputRack_Type()
)
zxAnSyncTimeOutputRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputRack.setStatus("current")
_ZxAnSyncTimeOutputShelf_Type = Integer32
_ZxAnSyncTimeOutputShelf_Object = MibTableColumn
zxAnSyncTimeOutputShelf = _ZxAnSyncTimeOutputShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 2),
    _ZxAnSyncTimeOutputShelf_Type()
)
zxAnSyncTimeOutputShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputShelf.setStatus("current")
_ZxAnSyncTimeOutputSlot_Type = Integer32
_ZxAnSyncTimeOutputSlot_Object = MibTableColumn
zxAnSyncTimeOutputSlot = _ZxAnSyncTimeOutputSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 3),
    _ZxAnSyncTimeOutputSlot_Type()
)
zxAnSyncTimeOutputSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputSlot.setStatus("current")
_ZxAnSyncTimeOutputPort_Type = Integer32
_ZxAnSyncTimeOutputPort_Object = MibTableColumn
zxAnSyncTimeOutputPort = _ZxAnSyncTimeOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 4),
    _ZxAnSyncTimeOutputPort_Type()
)
zxAnSyncTimeOutputPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPort.setStatus("current")


class _ZxAnSyncTimeOutputPortEnable_Type(Integer32):
    """Custom type zxAnSyncTimeOutputPortEnable based on Integer32"""
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


_ZxAnSyncTimeOutputPortEnable_Type.__name__ = "Integer32"
_ZxAnSyncTimeOutputPortEnable_Object = MibTableColumn
zxAnSyncTimeOutputPortEnable = _ZxAnSyncTimeOutputPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 5),
    _ZxAnSyncTimeOutputPortEnable_Type()
)
zxAnSyncTimeOutputPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortEnable.setStatus("current")


class _ZxAnSyncTimeOutputPortPhaseAdjus_Type(Integer32):
    """Custom type zxAnSyncTimeOutputPortPhaseAdjus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_ZxAnSyncTimeOutputPortPhaseAdjus_Type.__name__ = "Integer32"
_ZxAnSyncTimeOutputPortPhaseAdjus_Object = MibTableColumn
zxAnSyncTimeOutputPortPhaseAdjus = _ZxAnSyncTimeOutputPortPhaseAdjus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 6),
    _ZxAnSyncTimeOutputPortPhaseAdjus_Type()
)
zxAnSyncTimeOutputPortPhaseAdjus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortPhaseAdjus.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortPhaseAdjus.setUnits("ns")
_ZxAnSyncTimeOutputPortRowStatus_Type = RowStatus
_ZxAnSyncTimeOutputPortRowStatus_Object = MibTableColumn
zxAnSyncTimeOutputPortRowStatus = _ZxAnSyncTimeOutputPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 66, 2, 5, 1, 30),
    _ZxAnSyncTimeOutputPortRowStatus_Type()
)
zxAnSyncTimeOutputPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSyncTimeOutputPortRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-IEEE1588-MIB",
    **{"zxAnIeee1588Mib": zxAnIeee1588Mib,
       "zxAnPtpMgmt": zxAnPtpMgmt,
       "zxAnPtpTable": zxAnPtpTable,
       "zxAnPtpEntry": zxAnPtpEntry,
       "zxAnPtpRack": zxAnPtpRack,
       "zxAnPtpShelf": zxAnPtpShelf,
       "zxAnPtpSlot": zxAnPtpSlot,
       "zxAnPtpId": zxAnPtpId,
       "zxAnPtpClockType": zxAnPtpClockType,
       "zxAnPtpSlaveOnly": zxAnPtpSlaveOnly,
       "zxAnPtpDomainNumber": zxAnPtpDomainNumber,
       "zxAnPtpProtocolIpAddrType": zxAnPtpProtocolIpAddrType,
       "zxAnPtpProtocolIpAddress": zxAnPtpProtocolIpAddress,
       "zxAnPtpEthWorkMode": zxAnPtpEthWorkMode,
       "zxAnPtpPacketsMode": zxAnPtpPacketsMode,
       "zxAnPtpTwoStepFlag": zxAnPtpTwoStepFlag,
       "zxAnPtpSendPacketsRate": zxAnPtpSendPacketsRate,
       "zxAnPtpClockStatus": zxAnPtpClockStatus,
       "zxAnPtpUtcTime": zxAnPtpUtcTime,
       "zxAnPtpRowStatus": zxAnPtpRowStatus,
       "zxAnPtpRemoteSrcTable": zxAnPtpRemoteSrcTable,
       "zxAnPtpRemoteSrcEntry": zxAnPtpRemoteSrcEntry,
       "zxAnPtpRemoteSrcIpAddrType": zxAnPtpRemoteSrcIpAddrType,
       "zxAnPtpRemoteSrcIpAddress": zxAnPtpRemoteSrcIpAddress,
       "zxAnPtpRemoteSrcDomainNumber": zxAnPtpRemoteSrcDomainNumber,
       "zxAnPtpRemoteSrcPathDelayAdjust": zxAnPtpRemoteSrcPathDelayAdjust,
       "zxAnPtpRemoteSrcWorkStatus": zxAnPtpRemoteSrcWorkStatus,
       "zxAnPtpRemoteSrcRowStatus": zxAnPtpRemoteSrcRowStatus,
       "zxAnSyncTimeClkSrcMgmt": zxAnSyncTimeClkSrcMgmt,
       "zxAnSyncTime1ppsSrcTable": zxAnSyncTime1ppsSrcTable,
       "zxAnSyncTime1ppsSrcEntry": zxAnSyncTime1ppsSrcEntry,
       "zxAnSyncTime1ppsSrcRack": zxAnSyncTime1ppsSrcRack,
       "zxAnSyncTime1ppsSrcShelf": zxAnSyncTime1ppsSrcShelf,
       "zxAnSyncTime1ppsSrcSlot": zxAnSyncTime1ppsSrcSlot,
       "zxAnSyncTime1ppsSrcId": zxAnSyncTime1ppsSrcId,
       "zxAnSyncTime1ppsSrcSignalType": zxAnSyncTime1ppsSrcSignalType,
       "zxAnSyncTime1ppsSrcPriority": zxAnSyncTime1ppsSrcPriority,
       "zxAnSyncTime1ppsSrcPortType": zxAnSyncTime1ppsSrcPortType,
       "zxAnSyncTime1ppsSrcPort": zxAnSyncTime1ppsSrcPort,
       "zxAnSyncTime1ppsSrcWorkStatus": zxAnSyncTime1ppsSrcWorkStatus,
       "zxAnSyncTime1ppsSrcValidStatus": zxAnSyncTime1ppsSrcValidStatus,
       "zxAnSyncTime1ppsSrcPortStatus": zxAnSyncTime1ppsSrcPortStatus,
       "zxAnSyncTime1ppsSrcRowStatus": zxAnSyncTime1ppsSrcRowStatus,
       "zxAnSyncTimeTodSrcTable": zxAnSyncTimeTodSrcTable,
       "zxAnSyncTimeTodSrcEntry": zxAnSyncTimeTodSrcEntry,
       "zxAnSyncTimeTodSrcRack": zxAnSyncTimeTodSrcRack,
       "zxAnSyncTimeTodSrcShelf": zxAnSyncTimeTodSrcShelf,
       "zxAnSyncTimeTodSrcSlot": zxAnSyncTimeTodSrcSlot,
       "zxAnSyncTimeTodSrcPort": zxAnSyncTimeTodSrcPort,
       "zxAnSyncTimeTodSrcSignalType": zxAnSyncTimeTodSrcSignalType,
       "zxAnSyncTimeTodSrcYearAdjust": zxAnSyncTimeTodSrcYearAdjust,
       "zxAnSyncTimeTodSrcPortStatus": zxAnSyncTimeTodSrcPortStatus,
       "zxAnSyncTimeTodSrcRowStatus": zxAnSyncTimeTodSrcRowStatus,
       "zxAnSyncTimeOutputPortTable": zxAnSyncTimeOutputPortTable,
       "zxAnSyncTimeOutputPortEntry": zxAnSyncTimeOutputPortEntry,
       "zxAnSyncTimeOutputRack": zxAnSyncTimeOutputRack,
       "zxAnSyncTimeOutputShelf": zxAnSyncTimeOutputShelf,
       "zxAnSyncTimeOutputSlot": zxAnSyncTimeOutputSlot,
       "zxAnSyncTimeOutputPort": zxAnSyncTimeOutputPort,
       "zxAnSyncTimeOutputPortEnable": zxAnSyncTimeOutputPortEnable,
       "zxAnSyncTimeOutputPortPhaseAdjus": zxAnSyncTimeOutputPortPhaseAdjus,
       "zxAnSyncTimeOutputPortRowStatus": zxAnSyncTimeOutputPortRowStatus}
)
