# SNMP MIB module (SAVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/SAVI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:24:46 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetVersion")

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

saviMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40)
)
if mibBuilder.loadTexts:
    saviMIB.setRevisions(
        ("2020-07-24 00:00",
         "2015-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SaviObjects_ObjectIdentity = ObjectIdentity
saviObjects = _SaviObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 1)
)
_SaviObjectsSystemTable_Object = MibTable
saviObjectsSystemTable = _SaviObjectsSystemTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1)
)
if mibBuilder.loadTexts:
    saviObjectsSystemTable.setStatus("current")
_SaviObjectsSystemEntry_Object = MibTableRow
saviObjectsSystemEntry = _SaviObjectsSystemEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1)
)
saviObjectsSystemEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsSystemIPVersion"),
)
if mibBuilder.loadTexts:
    saviObjectsSystemEntry.setStatus("current")
_SaviObjectsSystemIPVersion_Type = InetVersion
_SaviObjectsSystemIPVersion_Object = MibTableColumn
saviObjectsSystemIPVersion = _SaviObjectsSystemIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 1),
    _SaviObjectsSystemIPVersion_Type()
)
saviObjectsSystemIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsSystemIPVersion.setStatus("current")


class _SaviObjectsSystemMode_Type(Integer32):
    """Custom type saviObjectsSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("savi-disable", 1),
          ("savi-default", 2),
          ("savi-dhcp-only", 3),
          ("savi-slaac-only", 4),
          ("savi-dhcp-slaac-mix", 5),
          ("savi-send", 6))
    )


_SaviObjectsSystemMode_Type.__name__ = "Integer32"
_SaviObjectsSystemMode_Object = MibTableColumn
saviObjectsSystemMode = _SaviObjectsSystemMode_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 2),
    _SaviObjectsSystemMode_Type()
)
saviObjectsSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMode.setStatus("current")
_SaviObjectsSystemMaxDhcpResponseTime_Type = TimeInterval
_SaviObjectsSystemMaxDhcpResponseTime_Object = MibTableColumn
saviObjectsSystemMaxDhcpResponseTime = _SaviObjectsSystemMaxDhcpResponseTime_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 3),
    _SaviObjectsSystemMaxDhcpResponseTime_Type()
)
saviObjectsSystemMaxDhcpResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMaxDhcpResponseTime.setStatus("current")
_SaviObjectsSystemDataSnoopingInterval_Type = TimeInterval
_SaviObjectsSystemDataSnoopingInterval_Object = MibTableColumn
saviObjectsSystemDataSnoopingInterval = _SaviObjectsSystemDataSnoopingInterval_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 4),
    _SaviObjectsSystemDataSnoopingInterval_Type()
)
saviObjectsSystemDataSnoopingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemDataSnoopingInterval.setStatus("current")
_SaviObjectsSystemMaxLeaseQueryDelay_Type = TimeInterval
_SaviObjectsSystemMaxLeaseQueryDelay_Object = MibTableColumn
saviObjectsSystemMaxLeaseQueryDelay = _SaviObjectsSystemMaxLeaseQueryDelay_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 5),
    _SaviObjectsSystemMaxLeaseQueryDelay_Type()
)
saviObjectsSystemMaxLeaseQueryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMaxLeaseQueryDelay.setStatus("current")
_SaviObjectsSystemOffLinkDelay_Type = TimeInterval
_SaviObjectsSystemOffLinkDelay_Object = MibTableColumn
saviObjectsSystemOffLinkDelay = _SaviObjectsSystemOffLinkDelay_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 6),
    _SaviObjectsSystemOffLinkDelay_Type()
)
saviObjectsSystemOffLinkDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemOffLinkDelay.setStatus("current")
_SaviObjectsSystemDetectionTimeout_Type = TimeInterval
_SaviObjectsSystemDetectionTimeout_Object = MibTableColumn
saviObjectsSystemDetectionTimeout = _SaviObjectsSystemDetectionTimeout_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 7),
    _SaviObjectsSystemDetectionTimeout_Type()
)
saviObjectsSystemDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemDetectionTimeout.setStatus("current")
_SaviObjectsSystemTentLT_Type = TimeInterval
_SaviObjectsSystemTentLT_Object = MibTableColumn
saviObjectsSystemTentLT = _SaviObjectsSystemTentLT_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 8),
    _SaviObjectsSystemTentLT_Type()
)
saviObjectsSystemTentLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemTentLT.setStatus("current")
_SaviObjectsSystemDefaultLT_Type = TimeInterval
_SaviObjectsSystemDefaultLT_Object = MibTableColumn
saviObjectsSystemDefaultLT = _SaviObjectsSystemDefaultLT_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 9),
    _SaviObjectsSystemDefaultLT_Type()
)
saviObjectsSystemDefaultLT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemDefaultLT.setStatus("current")
_SaviObjectsSystemTWAIT_Type = TimeInterval
_SaviObjectsSystemTWAIT_Object = MibTableColumn
saviObjectsSystemTWAIT = _SaviObjectsSystemTWAIT_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 10),
    _SaviObjectsSystemTWAIT_Type()
)
saviObjectsSystemTWAIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemTWAIT.setStatus("current")


class _SaviObjectsSystemNotifySpoofing_Type(Integer32):
    """Custom type saviObjectsSystemNotifySpoofing based on Integer32"""
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


_SaviObjectsSystemNotifySpoofing_Type.__name__ = "Integer32"
_SaviObjectsSystemNotifySpoofing_Object = MibTableColumn
saviObjectsSystemNotifySpoofing = _SaviObjectsSystemNotifySpoofing_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 11),
    _SaviObjectsSystemNotifySpoofing_Type()
)
saviObjectsSystemNotifySpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemNotifySpoofing.setStatus("current")


class _SaviObjectsSystemNotifyFilter_Type(Integer32):
    """Custom type saviObjectsSystemNotifyFilter based on Integer32"""
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


_SaviObjectsSystemNotifyFilter_Type.__name__ = "Integer32"
_SaviObjectsSystemNotifyFilter_Object = MibTableColumn
saviObjectsSystemNotifyFilter = _SaviObjectsSystemNotifyFilter_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 12),
    _SaviObjectsSystemNotifyFilter_Type()
)
saviObjectsSystemNotifyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemNotifyFilter.setStatus("current")


class _SaviObjectsSystemNotifySpoofingInterval_Type(Unsigned32):
    """Custom type saviObjectsSystemNotifySpoofingInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 3600),
    )


_SaviObjectsSystemNotifySpoofingInterval_Type.__name__ = "Unsigned32"
_SaviObjectsSystemNotifySpoofingInterval_Object = MibTableColumn
saviObjectsSystemNotifySpoofingInterval = _SaviObjectsSystemNotifySpoofingInterval_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 13),
    _SaviObjectsSystemNotifySpoofingInterval_Type()
)
saviObjectsSystemNotifySpoofingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemNotifySpoofingInterval.setStatus("current")


class _SaviObjectsSystemNotifySpoofingNumber_Type(Unsigned32):
    """Custom type saviObjectsSystemNotifySpoofingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SaviObjectsSystemNotifySpoofingNumber_Type.__name__ = "Unsigned32"
_SaviObjectsSystemNotifySpoofingNumber_Object = MibTableColumn
saviObjectsSystemNotifySpoofingNumber = _SaviObjectsSystemNotifySpoofingNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 14),
    _SaviObjectsSystemNotifySpoofingNumber_Type()
)
saviObjectsSystemNotifySpoofingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemNotifySpoofingNumber.setStatus("current")
_SaviObjectsSystemBindingCount_Type = Unsigned32
_SaviObjectsSystemBindingCount_Object = MibTableColumn
saviObjectsSystemBindingCount = _SaviObjectsSystemBindingCount_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 15),
    _SaviObjectsSystemBindingCount_Type()
)
saviObjectsSystemBindingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsSystemBindingCount.setStatus("current")
_SaviObjectsSystemFilteringCount_Type = Unsigned32
_SaviObjectsSystemFilteringCount_Object = MibTableColumn
saviObjectsSystemFilteringCount = _SaviObjectsSystemFilteringCount_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 16),
    _SaviObjectsSystemFilteringCount_Type()
)
saviObjectsSystemFilteringCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsSystemFilteringCount.setStatus("current")
_SaviObjectsPortTable_Object = MibTable
saviObjectsPortTable = _SaviObjectsPortTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2)
)
if mibBuilder.loadTexts:
    saviObjectsPortTable.setStatus("current")
_SaviObjectsPortEntry_Object = MibTableRow
saviObjectsPortEntry = _SaviObjectsPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1)
)
saviObjectsPortEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsPortIPVersion"),
    (0, "SAVI-MIB", "saviObjectsPortIfIndex"),
)
if mibBuilder.loadTexts:
    saviObjectsPortEntry.setStatus("current")
_SaviObjectsPortIPVersion_Type = InetVersion
_SaviObjectsPortIPVersion_Object = MibTableColumn
saviObjectsPortIPVersion = _SaviObjectsPortIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 1),
    _SaviObjectsPortIPVersion_Type()
)
saviObjectsPortIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsPortIPVersion.setStatus("current")
_SaviObjectsPortIfIndex_Type = InterfaceIndex
_SaviObjectsPortIfIndex_Object = MibTableColumn
saviObjectsPortIfIndex = _SaviObjectsPortIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 2),
    _SaviObjectsPortIfIndex_Type()
)
saviObjectsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsPortIfIndex.setStatus("current")


class _SaviObjectsPortValidatingAttr_Type(Integer32):
    """Custom type saviObjectsPortValidatingAttr based on Integer32"""
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


_SaviObjectsPortValidatingAttr_Type.__name__ = "Integer32"
_SaviObjectsPortValidatingAttr_Object = MibTableColumn
saviObjectsPortValidatingAttr = _SaviObjectsPortValidatingAttr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 3),
    _SaviObjectsPortValidatingAttr_Type()
)
saviObjectsPortValidatingAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortValidatingAttr.setStatus("current")


class _SaviObjectsPortDhcpTrustAttr_Type(Integer32):
    """Custom type saviObjectsPortDhcpTrustAttr based on Integer32"""
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


_SaviObjectsPortDhcpTrustAttr_Type.__name__ = "Integer32"
_SaviObjectsPortDhcpTrustAttr_Object = MibTableColumn
saviObjectsPortDhcpTrustAttr = _SaviObjectsPortDhcpTrustAttr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 4),
    _SaviObjectsPortDhcpTrustAttr_Type()
)
saviObjectsPortDhcpTrustAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortDhcpTrustAttr.setStatus("current")


class _SaviObjectsPortTrustAttr_Type(Integer32):
    """Custom type saviObjectsPortTrustAttr based on Integer32"""
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


_SaviObjectsPortTrustAttr_Type.__name__ = "Integer32"
_SaviObjectsPortTrustAttr_Object = MibTableColumn
saviObjectsPortTrustAttr = _SaviObjectsPortTrustAttr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 5),
    _SaviObjectsPortTrustAttr_Type()
)
saviObjectsPortTrustAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortTrustAttr.setStatus("current")


class _SaviObjectsPortDhcpSnoopingAttr_Type(Integer32):
    """Custom type saviObjectsPortDhcpSnoopingAttr based on Integer32"""
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


_SaviObjectsPortDhcpSnoopingAttr_Type.__name__ = "Integer32"
_SaviObjectsPortDhcpSnoopingAttr_Object = MibTableColumn
saviObjectsPortDhcpSnoopingAttr = _SaviObjectsPortDhcpSnoopingAttr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 6),
    _SaviObjectsPortDhcpSnoopingAttr_Type()
)
saviObjectsPortDhcpSnoopingAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortDhcpSnoopingAttr.setStatus("current")


class _SaviObjectsPortDataSnoopingAttr_Type(Integer32):
    """Custom type saviObjectsPortDataSnoopingAttr based on Integer32"""
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


_SaviObjectsPortDataSnoopingAttr_Type.__name__ = "Integer32"
_SaviObjectsPortDataSnoopingAttr_Object = MibTableColumn
saviObjectsPortDataSnoopingAttr = _SaviObjectsPortDataSnoopingAttr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 7),
    _SaviObjectsPortDataSnoopingAttr_Type()
)
saviObjectsPortDataSnoopingAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortDataSnoopingAttr.setStatus("current")
_SaviObjectsPortFilteringNum_Type = Unsigned32
_SaviObjectsPortFilteringNum_Object = MibTableColumn
saviObjectsPortFilteringNum = _SaviObjectsPortFilteringNum_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 8),
    _SaviObjectsPortFilteringNum_Type()
)
saviObjectsPortFilteringNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsPortFilteringNum.setStatus("current")
_SaviObjectsBindingTable_Object = MibTable
saviObjectsBindingTable = _SaviObjectsBindingTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3)
)
if mibBuilder.loadTexts:
    saviObjectsBindingTable.setStatus("current")
_SaviObjectsBindingEntry_Object = MibTableRow
saviObjectsBindingEntry = _SaviObjectsBindingEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1)
)
saviObjectsBindingEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsBindingIpAddressType"),
    (0, "SAVI-MIB", "saviObjectsBindingType"),
    (0, "SAVI-MIB", "saviObjectsBindingIfIndex"),
    (0, "SAVI-MIB", "saviObjectsBindingIpAddress"),
)
if mibBuilder.loadTexts:
    saviObjectsBindingEntry.setStatus("current")
_SaviObjectsBindingIpAddressType_Type = InetAddressType
_SaviObjectsBindingIpAddressType_Object = MibTableColumn
saviObjectsBindingIpAddressType = _SaviObjectsBindingIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 1),
    _SaviObjectsBindingIpAddressType_Type()
)
saviObjectsBindingIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIpAddressType.setStatus("current")


class _SaviObjectsBindingType_Type(Integer32):
    """Custom type saviObjectsBindingType based on Integer32"""
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
        *(("manual", 1),
          ("slaac", 2),
          ("dhcp", 3),
          ("send", 4))
    )


_SaviObjectsBindingType_Type.__name__ = "Integer32"
_SaviObjectsBindingType_Object = MibTableColumn
saviObjectsBindingType = _SaviObjectsBindingType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 2),
    _SaviObjectsBindingType_Type()
)
saviObjectsBindingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingType.setStatus("current")
_SaviObjectsBindingIfIndex_Type = InterfaceIndex
_SaviObjectsBindingIfIndex_Object = MibTableColumn
saviObjectsBindingIfIndex = _SaviObjectsBindingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 3),
    _SaviObjectsBindingIfIndex_Type()
)
saviObjectsBindingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIfIndex.setStatus("current")
_SaviObjectsBindingIpAddress_Type = InetAddress
_SaviObjectsBindingIpAddress_Object = MibTableColumn
saviObjectsBindingIpAddress = _SaviObjectsBindingIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 4),
    _SaviObjectsBindingIpAddress_Type()
)
saviObjectsBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIpAddress.setStatus("current")
_SaviObjectsBindingMacAddr_Type = MacAddress
_SaviObjectsBindingMacAddr_Object = MibTableColumn
saviObjectsBindingMacAddr = _SaviObjectsBindingMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 5),
    _SaviObjectsBindingMacAddr_Type()
)
saviObjectsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingMacAddr.setStatus("current")


class _SaviObjectsBindingState_Type(Integer32):
    """Custom type saviObjectsBindingState based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("nO-BIND", 1),
          ("iNIT-BIND", 2),
          ("bOUND", 3),
          ("dETECTION", 4),
          ("rECOVERY", 5),
          ("vERIFY", 6),
          ("tENTATIVE", 7),
          ("vALID", 8),
          ("tESTING-TP-LT", 9),
          ("tESTING-VP", 10),
          ("tESTING-VPP", 11),
          ("tENTATIVE-NUD", 12),
          ("tENTATIVE-DAD", 13))
    )


_SaviObjectsBindingState_Type.__name__ = "Integer32"
_SaviObjectsBindingState_Object = MibTableColumn
saviObjectsBindingState = _SaviObjectsBindingState_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 6),
    _SaviObjectsBindingState_Type()
)
saviObjectsBindingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingState.setStatus("current")
_SaviObjectsBindingLifetime_Type = TimeInterval
_SaviObjectsBindingLifetime_Object = MibTableColumn
saviObjectsBindingLifetime = _SaviObjectsBindingLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 7),
    _SaviObjectsBindingLifetime_Type()
)
saviObjectsBindingLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingLifetime.setStatus("current")
_SaviObjectsBindingCreationtime_Type = DateAndTime
_SaviObjectsBindingCreationtime_Object = MibTableColumn
saviObjectsBindingCreationtime = _SaviObjectsBindingCreationtime_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 8),
    _SaviObjectsBindingCreationtime_Type()
)
saviObjectsBindingCreationtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingCreationtime.setStatus("current")
_SaviObjectsBindingTID_Type = Integer32
_SaviObjectsBindingTID_Object = MibTableColumn
saviObjectsBindingTID = _SaviObjectsBindingTID_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 9),
    _SaviObjectsBindingTID_Type()
)
saviObjectsBindingTID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingTID.setStatus("current")
_SaviObjectsBindingRowStatus_Type = RowStatus
_SaviObjectsBindingRowStatus_Object = MibTableColumn
saviObjectsBindingRowStatus = _SaviObjectsBindingRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 10),
    _SaviObjectsBindingRowStatus_Type()
)
saviObjectsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingRowStatus.setStatus("current")
_SaviObjectsFilteringTable_Object = MibTable
saviObjectsFilteringTable = _SaviObjectsFilteringTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4)
)
if mibBuilder.loadTexts:
    saviObjectsFilteringTable.setStatus("current")
_SaviObjectsFilteringEntry_Object = MibTableRow
saviObjectsFilteringEntry = _SaviObjectsFilteringEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1)
)
saviObjectsFilteringEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsFilteringIpAddressType"),
    (0, "SAVI-MIB", "saviObjectsFilteringIfIndex"),
    (0, "SAVI-MIB", "saviObjectsFilteringIpAddress"),
)
if mibBuilder.loadTexts:
    saviObjectsFilteringEntry.setStatus("current")
_SaviObjectsFilteringIpAddressType_Type = InetAddressType
_SaviObjectsFilteringIpAddressType_Object = MibTableColumn
saviObjectsFilteringIpAddressType = _SaviObjectsFilteringIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 1),
    _SaviObjectsFilteringIpAddressType_Type()
)
saviObjectsFilteringIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIpAddressType.setStatus("current")
_SaviObjectsFilteringIfIndex_Type = InterfaceIndex
_SaviObjectsFilteringIfIndex_Object = MibTableColumn
saviObjectsFilteringIfIndex = _SaviObjectsFilteringIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 2),
    _SaviObjectsFilteringIfIndex_Type()
)
saviObjectsFilteringIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIfIndex.setStatus("current")
_SaviObjectsFilteringIpAddress_Type = InetAddress
_SaviObjectsFilteringIpAddress_Object = MibTableColumn
saviObjectsFilteringIpAddress = _SaviObjectsFilteringIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 3),
    _SaviObjectsFilteringIpAddress_Type()
)
saviObjectsFilteringIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIpAddress.setStatus("current")
_SaviObjectsFilteringMacAddr_Type = MacAddress
_SaviObjectsFilteringMacAddr_Object = MibTableColumn
saviObjectsFilteringMacAddr = _SaviObjectsFilteringMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 4),
    _SaviObjectsFilteringMacAddr_Type()
)
saviObjectsFilteringMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsFilteringMacAddr.setStatus("current")
_SaviObjectsCountTable_Object = MibTable
saviObjectsCountTable = _SaviObjectsCountTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5)
)
if mibBuilder.loadTexts:
    saviObjectsCountTable.setStatus("current")
_SaviObjectsCountEntry_Object = MibTableRow
saviObjectsCountEntry = _SaviObjectsCountEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5, 1)
)
saviObjectsCountEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsCountIPVersion"),
    (0, "SAVI-MIB", "saviObjectsCountIfIndex"),
)
if mibBuilder.loadTexts:
    saviObjectsCountEntry.setStatus("current")
_SaviObjectsCountIPVersion_Type = InetVersion
_SaviObjectsCountIPVersion_Object = MibTableColumn
saviObjectsCountIPVersion = _SaviObjectsCountIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5, 1, 1),
    _SaviObjectsCountIPVersion_Type()
)
saviObjectsCountIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsCountIPVersion.setStatus("current")
_SaviObjectsCountIfIndex_Type = InterfaceIndex
_SaviObjectsCountIfIndex_Object = MibTableColumn
saviObjectsCountIfIndex = _SaviObjectsCountIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5, 1, 2),
    _SaviObjectsCountIfIndex_Type()
)
saviObjectsCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsCountIfIndex.setStatus("current")
_SaviObjectsCountFilterPkts_Type = Counter64
_SaviObjectsCountFilterPkts_Object = MibTableColumn
saviObjectsCountFilterPkts = _SaviObjectsCountFilterPkts_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5, 1, 3),
    _SaviObjectsCountFilterPkts_Type()
)
saviObjectsCountFilterPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsCountFilterPkts.setStatus("current")
_SaviObjectsCountFilterOctets_Type = Counter64
_SaviObjectsCountFilterOctets_Object = MibTableColumn
saviObjectsCountFilterOctets = _SaviObjectsCountFilterOctets_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 5, 1, 4),
    _SaviObjectsCountFilterOctets_Type()
)
saviObjectsCountFilterOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsCountFilterOctets.setStatus("current")
_SaviConformance_ObjectIdentity = ObjectIdentity
saviConformance = _SaviConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2)
)
_SaviCompliances_ObjectIdentity = ObjectIdentity
saviCompliances = _SaviCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 1)
)
_SaviGroups_ObjectIdentity = ObjectIdentity
saviGroups = _SaviGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2)
)

# Managed Objects groups

systemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 1)
)
systemGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsSystemMode"),
        ("SAVI-MIB", "saviObjectsSystemMaxDhcpResponseTime"),
        ("SAVI-MIB", "saviObjectsSystemDataSnoopingInterval"),
        ("SAVI-MIB", "saviObjectsSystemMaxLeaseQueryDelay"),
        ("SAVI-MIB", "saviObjectsSystemOffLinkDelay"),
        ("SAVI-MIB", "saviObjectsSystemDetectionTimeout"),
        ("SAVI-MIB", "saviObjectsSystemTentLT"),
        ("SAVI-MIB", "saviObjectsSystemDefaultLT"),
        ("SAVI-MIB", "saviObjectsSystemTWAIT"),
        ("SAVI-MIB", "saviObjectsSystemNotifySpoofing"),
        ("SAVI-MIB", "saviObjectsSystemNotifyFilter"),
        ("SAVI-MIB", "saviObjectsSystemNotifySpoofingInterval"),
        ("SAVI-MIB", "saviObjectsSystemNotifySpoofingNumber"),
        ("SAVI-MIB", "saviObjectsSystemBindingCount"),
        ("SAVI-MIB", "saviObjectsSystemFilteringCount"))
)
if mibBuilder.loadTexts:
    systemGroup.setStatus("current")

portGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 2)
)
portGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsPortValidatingAttr"),
        ("SAVI-MIB", "saviObjectsPortDhcpTrustAttr"),
        ("SAVI-MIB", "saviObjectsPortTrustAttr"),
        ("SAVI-MIB", "saviObjectsPortDhcpSnoopingAttr"),
        ("SAVI-MIB", "saviObjectsPortDataSnoopingAttr"),
        ("SAVI-MIB", "saviObjectsPortFilteringNum"))
)
if mibBuilder.loadTexts:
    portGroup.setStatus("current")

bindingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 3)
)
bindingGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsBindingMacAddr"),
        ("SAVI-MIB", "saviObjectsBindingState"),
        ("SAVI-MIB", "saviObjectsBindingLifetime"),
        ("SAVI-MIB", "saviObjectsBindingCreationtime"),
        ("SAVI-MIB", "saviObjectsBindingTID"),
        ("SAVI-MIB", "saviObjectsBindingRowStatus"))
)
if mibBuilder.loadTexts:
    bindingGroup.setStatus("current")

filteringGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 4)
)
filteringGroup.setObjects(
    ("SAVI-MIB", "saviObjectsFilteringMacAddr")
)
if mibBuilder.loadTexts:
    filteringGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

saviCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 1, 1)
)
saviCompliance.setObjects(
      *(("SAVI-MIB", "systemGroup"),
        ("SAVI-MIB", "portGroup"),
        ("SAVI-MIB", "bindingGroup"),
        ("SAVI-MIB", "filteringGroup"))
)
if mibBuilder.loadTexts:
    saviCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAVI-MIB",
    **{"saviMIB": saviMIB,
       "saviObjects": saviObjects,
       "saviObjectsSystemTable": saviObjectsSystemTable,
       "saviObjectsSystemEntry": saviObjectsSystemEntry,
       "saviObjectsSystemIPVersion": saviObjectsSystemIPVersion,
       "saviObjectsSystemMode": saviObjectsSystemMode,
       "saviObjectsSystemMaxDhcpResponseTime": saviObjectsSystemMaxDhcpResponseTime,
       "saviObjectsSystemDataSnoopingInterval": saviObjectsSystemDataSnoopingInterval,
       "saviObjectsSystemMaxLeaseQueryDelay": saviObjectsSystemMaxLeaseQueryDelay,
       "saviObjectsSystemOffLinkDelay": saviObjectsSystemOffLinkDelay,
       "saviObjectsSystemDetectionTimeout": saviObjectsSystemDetectionTimeout,
       "saviObjectsSystemTentLT": saviObjectsSystemTentLT,
       "saviObjectsSystemDefaultLT": saviObjectsSystemDefaultLT,
       "saviObjectsSystemTWAIT": saviObjectsSystemTWAIT,
       "saviObjectsSystemNotifySpoofing": saviObjectsSystemNotifySpoofing,
       "saviObjectsSystemNotifyFilter": saviObjectsSystemNotifyFilter,
       "saviObjectsSystemNotifySpoofingInterval": saviObjectsSystemNotifySpoofingInterval,
       "saviObjectsSystemNotifySpoofingNumber": saviObjectsSystemNotifySpoofingNumber,
       "saviObjectsSystemBindingCount": saviObjectsSystemBindingCount,
       "saviObjectsSystemFilteringCount": saviObjectsSystemFilteringCount,
       "saviObjectsPortTable": saviObjectsPortTable,
       "saviObjectsPortEntry": saviObjectsPortEntry,
       "saviObjectsPortIPVersion": saviObjectsPortIPVersion,
       "saviObjectsPortIfIndex": saviObjectsPortIfIndex,
       "saviObjectsPortValidatingAttr": saviObjectsPortValidatingAttr,
       "saviObjectsPortDhcpTrustAttr": saviObjectsPortDhcpTrustAttr,
       "saviObjectsPortTrustAttr": saviObjectsPortTrustAttr,
       "saviObjectsPortDhcpSnoopingAttr": saviObjectsPortDhcpSnoopingAttr,
       "saviObjectsPortDataSnoopingAttr": saviObjectsPortDataSnoopingAttr,
       "saviObjectsPortFilteringNum": saviObjectsPortFilteringNum,
       "saviObjectsBindingTable": saviObjectsBindingTable,
       "saviObjectsBindingEntry": saviObjectsBindingEntry,
       "saviObjectsBindingIpAddressType": saviObjectsBindingIpAddressType,
       "saviObjectsBindingType": saviObjectsBindingType,
       "saviObjectsBindingIfIndex": saviObjectsBindingIfIndex,
       "saviObjectsBindingIpAddress": saviObjectsBindingIpAddress,
       "saviObjectsBindingMacAddr": saviObjectsBindingMacAddr,
       "saviObjectsBindingState": saviObjectsBindingState,
       "saviObjectsBindingLifetime": saviObjectsBindingLifetime,
       "saviObjectsBindingCreationtime": saviObjectsBindingCreationtime,
       "saviObjectsBindingTID": saviObjectsBindingTID,
       "saviObjectsBindingRowStatus": saviObjectsBindingRowStatus,
       "saviObjectsFilteringTable": saviObjectsFilteringTable,
       "saviObjectsFilteringEntry": saviObjectsFilteringEntry,
       "saviObjectsFilteringIpAddressType": saviObjectsFilteringIpAddressType,
       "saviObjectsFilteringIfIndex": saviObjectsFilteringIfIndex,
       "saviObjectsFilteringIpAddress": saviObjectsFilteringIpAddress,
       "saviObjectsFilteringMacAddr": saviObjectsFilteringMacAddr,
       "saviObjectsCountTable": saviObjectsCountTable,
       "saviObjectsCountEntry": saviObjectsCountEntry,
       "saviObjectsCountIPVersion": saviObjectsCountIPVersion,
       "saviObjectsCountIfIndex": saviObjectsCountIfIndex,
       "saviObjectsCountFilterPkts": saviObjectsCountFilterPkts,
       "saviObjectsCountFilterOctets": saviObjectsCountFilterOctets,
       "saviConformance": saviConformance,
       "saviCompliances": saviCompliances,
       "saviCompliance": saviCompliance,
       "saviGroups": saviGroups,
       "systemGroup": systemGroup,
       "portGroup": portGroup,
       "bindingGroup": bindingGroup,
       "filteringGroup": filteringGroup}
)
