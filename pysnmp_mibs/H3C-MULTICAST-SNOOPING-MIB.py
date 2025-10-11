# SNMP MIB module (H3C-MULTICAST-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MULTICAST-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:27 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cMulticastSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123)
)
if mibBuilder.loadTexts:
    h3cMulticastSnoop.setRevisions(
        ("2017-09-26 09:50",
         "2014-05-14 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cVirtualUnitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("vsi", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cMulticastSnoopObject_ObjectIdentity = ObjectIdentity
h3cMulticastSnoopObject = _H3cMulticastSnoopObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1)
)
_H3cMcsGlobalConfigTable_Object = MibTable
h3cMcsGlobalConfigTable = _H3cMcsGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1)
)
if mibBuilder.loadTexts:
    h3cMcsGlobalConfigTable.setStatus("current")
_H3cMcsGlobalConfigEntry_Object = MibTableRow
h3cMcsGlobalConfigEntry = _H3cMcsGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1)
)
h3cMcsGlobalConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsGlbSnoopingType"),
)
if mibBuilder.loadTexts:
    h3cMcsGlobalConfigEntry.setStatus("current")
_H3cMcsGlbSnoopingType_Type = InetAddressType
_H3cMcsGlbSnoopingType_Object = MibTableColumn
h3cMcsGlbSnoopingType = _H3cMcsGlbSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 1),
    _H3cMcsGlbSnoopingType_Type()
)
h3cMcsGlbSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsGlbSnoopingType.setStatus("current")
_H3cMcsGlbRowStatus_Type = RowStatus
_H3cMcsGlbRowStatus_Object = MibTableColumn
h3cMcsGlbRowStatus = _H3cMcsGlbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 2),
    _H3cMcsGlbRowStatus_Type()
)
h3cMcsGlbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbRowStatus.setStatus("current")
_H3cMcsGlbEntryLimit_Type = Unsigned32
_H3cMcsGlbEntryLimit_Object = MibTableColumn
h3cMcsGlbEntryLimit = _H3cMcsGlbEntryLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 3),
    _H3cMcsGlbEntryLimit_Type()
)
h3cMcsGlbEntryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbEntryLimit.setStatus("current")


class _H3cMcsGlbHostAgingTime_Type(Unsigned32):
    """Custom type h3cMcsGlbHostAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_H3cMcsGlbHostAgingTime_Type.__name__ = "Unsigned32"
_H3cMcsGlbHostAgingTime_Object = MibTableColumn
h3cMcsGlbHostAgingTime = _H3cMcsGlbHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 4),
    _H3cMcsGlbHostAgingTime_Type()
)
h3cMcsGlbHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbHostAgingTime.setStatus("current")


class _H3cMcsGlbMaxResponseTime_Type(Unsigned32):
    """Custom type h3cMcsGlbMaxResponseTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3174),
    )


_H3cMcsGlbMaxResponseTime_Type.__name__ = "Unsigned32"
_H3cMcsGlbMaxResponseTime_Object = MibTableColumn
h3cMcsGlbMaxResponseTime = _H3cMcsGlbMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 5),
    _H3cMcsGlbMaxResponseTime_Type()
)
h3cMcsGlbMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbMaxResponseTime.setStatus("current")


class _H3cMcsGlbRouterAgingTime_Type(Unsigned32):
    """Custom type h3cMcsGlbRouterAgingTime based on Unsigned32"""
    defaultValue = 260

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8097894),
    )


_H3cMcsGlbRouterAgingTime_Type.__name__ = "Unsigned32"
_H3cMcsGlbRouterAgingTime_Object = MibTableColumn
h3cMcsGlbRouterAgingTime = _H3cMcsGlbRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 6),
    _H3cMcsGlbRouterAgingTime_Type()
)
h3cMcsGlbRouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbRouterAgingTime.setStatus("current")


class _H3cMcsGlbLastMemQryInterval_Type(Unsigned32):
    """Custom type h3cMcsGlbLastMemQryInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_H3cMcsGlbLastMemQryInterval_Type.__name__ = "Unsigned32"
_H3cMcsGlbLastMemQryInterval_Object = MibTableColumn
h3cMcsGlbLastMemQryInterval = _H3cMcsGlbLastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 7),
    _H3cMcsGlbLastMemQryInterval_Type()
)
h3cMcsGlbLastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbLastMemQryInterval.setStatus("current")


class _H3cMcsGlbDropUnknownEnabled_Type(TruthValue):
    """Custom type h3cMcsGlbDropUnknownEnabled based on TruthValue"""
    defaultValue = 2


_H3cMcsGlbDropUnknownEnabled_Type.__name__ = "TruthValue"
_H3cMcsGlbDropUnknownEnabled_Object = MibTableColumn
h3cMcsGlbDropUnknownEnabled = _H3cMcsGlbDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 1, 1, 8),
    _H3cMcsGlbDropUnknownEnabled_Type()
)
h3cMcsGlbDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsGlbDropUnknownEnabled.setStatus("current")
_H3cMcsVirtualUnitConfigTable_Object = MibTable
h3cMcsVirtualUnitConfigTable = _H3cMcsVirtualUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2)
)
if mibBuilder.loadTexts:
    h3cMcsVirtualUnitConfigTable.setStatus("current")
_H3cMcsVirtualUnitConfigEntry_Object = MibTableRow
h3cMcsVirtualUnitConfigEntry = _H3cMcsVirtualUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1)
)
h3cMcsVirtualUnitConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsVUType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsVUID"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsVUSnoopingType"),
)
if mibBuilder.loadTexts:
    h3cMcsVirtualUnitConfigEntry.setStatus("current")
_H3cMcsVUType_Type = H3cVirtualUnitType
_H3cMcsVUType_Object = MibTableColumn
h3cMcsVUType = _H3cMcsVUType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 1),
    _H3cMcsVUType_Type()
)
h3cMcsVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsVUType.setStatus("current")
_H3cMcsVUID_Type = Unsigned32
_H3cMcsVUID_Object = MibTableColumn
h3cMcsVUID = _H3cMcsVUID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 2),
    _H3cMcsVUID_Type()
)
h3cMcsVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsVUID.setStatus("current")
_H3cMcsVUSnoopingType_Type = InetAddressType
_H3cMcsVUSnoopingType_Object = MibTableColumn
h3cMcsVUSnoopingType = _H3cMcsVUSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 3),
    _H3cMcsVUSnoopingType_Type()
)
h3cMcsVUSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsVUSnoopingType.setStatus("current")
_H3cMcsVURowStatus_Type = RowStatus
_H3cMcsVURowStatus_Object = MibTableColumn
h3cMcsVURowStatus = _H3cMcsVURowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 4),
    _H3cMcsVURowStatus_Type()
)
h3cMcsVURowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVURowStatus.setStatus("current")


class _H3cMcsVUHostAgingTime_Type(Unsigned32):
    """Custom type h3cMcsVUHostAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_H3cMcsVUHostAgingTime_Type.__name__ = "Unsigned32"
_H3cMcsVUHostAgingTime_Object = MibTableColumn
h3cMcsVUHostAgingTime = _H3cMcsVUHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 5),
    _H3cMcsVUHostAgingTime_Type()
)
h3cMcsVUHostAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUHostAgingTime.setStatus("current")


class _H3cMcsVUMaxResponseTime_Type(Unsigned32):
    """Custom type h3cMcsVUMaxResponseTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3174),
    )


_H3cMcsVUMaxResponseTime_Type.__name__ = "Unsigned32"
_H3cMcsVUMaxResponseTime_Object = MibTableColumn
h3cMcsVUMaxResponseTime = _H3cMcsVUMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 6),
    _H3cMcsVUMaxResponseTime_Type()
)
h3cMcsVUMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUMaxResponseTime.setStatus("current")


class _H3cMcsVURouterAgingTime_Type(Unsigned32):
    """Custom type h3cMcsVURouterAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8097894),
    )


_H3cMcsVURouterAgingTime_Type.__name__ = "Unsigned32"
_H3cMcsVURouterAgingTime_Object = MibTableColumn
h3cMcsVURouterAgingTime = _H3cMcsVURouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 7),
    _H3cMcsVURouterAgingTime_Type()
)
h3cMcsVURouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVURouterAgingTime.setStatus("current")


class _H3cMcsVULastMemQryInterval_Type(Unsigned32):
    """Custom type h3cMcsVULastMemQryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_H3cMcsVULastMemQryInterval_Type.__name__ = "Unsigned32"
_H3cMcsVULastMemQryInterval_Object = MibTableColumn
h3cMcsVULastMemQryInterval = _H3cMcsVULastMemQryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 8),
    _H3cMcsVULastMemQryInterval_Type()
)
h3cMcsVULastMemQryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVULastMemQryInterval.setStatus("current")


class _H3cMcsVUDropUnknownEnabled_Type(TruthValue):
    """Custom type h3cMcsVUDropUnknownEnabled based on TruthValue"""
    defaultValue = 2


_H3cMcsVUDropUnknownEnabled_Type.__name__ = "TruthValue"
_H3cMcsVUDropUnknownEnabled_Object = MibTableColumn
h3cMcsVUDropUnknownEnabled = _H3cMcsVUDropUnknownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 9),
    _H3cMcsVUDropUnknownEnabled_Type()
)
h3cMcsVUDropUnknownEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUDropUnknownEnabled.setStatus("current")


class _H3cMcsVUPimSnoopingEnabled_Type(TruthValue):
    """Custom type h3cMcsVUPimSnoopingEnabled based on TruthValue"""
    defaultValue = 2


_H3cMcsVUPimSnoopingEnabled_Type.__name__ = "TruthValue"
_H3cMcsVUPimSnoopingEnabled_Object = MibTableColumn
h3cMcsVUPimSnoopingEnabled = _H3cMcsVUPimSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 10),
    _H3cMcsVUPimSnoopingEnabled_Type()
)
h3cMcsVUPimSnoopingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUPimSnoopingEnabled.setStatus("current")


class _H3cMcsVUVersion_Type(Unsigned32):
    """Custom type h3cMcsVUVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
    )


_H3cMcsVUVersion_Type.__name__ = "Unsigned32"
_H3cMcsVUVersion_Object = MibTableColumn
h3cMcsVUVersion = _H3cMcsVUVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 11),
    _H3cMcsVUVersion_Type()
)
h3cMcsVUVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUVersion.setStatus("current")


class _H3cMcsVUQuerierEnabled_Type(TruthValue):
    """Custom type h3cMcsVUQuerierEnabled based on TruthValue"""
    defaultValue = 2


_H3cMcsVUQuerierEnabled_Type.__name__ = "TruthValue"
_H3cMcsVUQuerierEnabled_Object = MibTableColumn
h3cMcsVUQuerierEnabled = _H3cMcsVUQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 12),
    _H3cMcsVUQuerierEnabled_Type()
)
h3cMcsVUQuerierEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUQuerierEnabled.setStatus("current")


class _H3cMcsVUQuerierInterval_Type(Unsigned32):
    """Custom type h3cMcsVUQuerierInterval based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 31744),
    )


_H3cMcsVUQuerierInterval_Type.__name__ = "Unsigned32"
_H3cMcsVUQuerierInterval_Object = MibTableColumn
h3cMcsVUQuerierInterval = _H3cMcsVUQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 13),
    _H3cMcsVUQuerierInterval_Type()
)
h3cMcsVUQuerierInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUQuerierInterval.setStatus("current")
_H3cMcsVUGeneQuerierSourceAddress_Type = InetAddress
_H3cMcsVUGeneQuerierSourceAddress_Object = MibTableColumn
h3cMcsVUGeneQuerierSourceAddress = _H3cMcsVUGeneQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 14),
    _H3cMcsVUGeneQuerierSourceAddress_Type()
)
h3cMcsVUGeneQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUGeneQuerierSourceAddress.setStatus("current")
_H3cMcsVUSpecQuerierSourceAddress_Type = InetAddress
_H3cMcsVUSpecQuerierSourceAddress_Object = MibTableColumn
h3cMcsVUSpecQuerierSourceAddress = _H3cMcsVUSpecQuerierSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 15),
    _H3cMcsVUSpecQuerierSourceAddress_Type()
)
h3cMcsVUSpecQuerierSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUSpecQuerierSourceAddress.setStatus("current")
_H3cMcsVULeaveSourceAddress_Type = InetAddress
_H3cMcsVULeaveSourceAddress_Object = MibTableColumn
h3cMcsVULeaveSourceAddress = _H3cMcsVULeaveSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 16),
    _H3cMcsVULeaveSourceAddress_Type()
)
h3cMcsVULeaveSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVULeaveSourceAddress.setStatus("current")
_H3cMcsVUReportSourceAddress_Type = InetAddress
_H3cMcsVUReportSourceAddress_Object = MibTableColumn
h3cMcsVUReportSourceAddress = _H3cMcsVUReportSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 17),
    _H3cMcsVUReportSourceAddress_Type()
)
h3cMcsVUReportSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUReportSourceAddress.setStatus("current")


class _H3cMcsVUProxyEnabled_Type(TruthValue):
    """Custom type h3cMcsVUProxyEnabled based on TruthValue"""
    defaultValue = 2


_H3cMcsVUProxyEnabled_Type.__name__ = "TruthValue"
_H3cMcsVUProxyEnabled_Object = MibTableColumn
h3cMcsVUProxyEnabled = _H3cMcsVUProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 18),
    _H3cMcsVUProxyEnabled_Type()
)
h3cMcsVUProxyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUProxyEnabled.setStatus("current")


class _H3cMcsVUQuerierElection_Type(TruthValue):
    """Custom type h3cMcsVUQuerierElection based on TruthValue"""
    defaultValue = 2


_H3cMcsVUQuerierElection_Type.__name__ = "TruthValue"
_H3cMcsVUQuerierElection_Object = MibTableColumn
h3cMcsVUQuerierElection = _H3cMcsVUQuerierElection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 2, 1, 19),
    _H3cMcsVUQuerierElection_Type()
)
h3cMcsVUQuerierElection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsVUQuerierElection.setStatus("current")
_H3cMcsL2EntryTable_Object = MibTable
h3cMcsL2EntryTable = _H3cMcsL2EntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3)
)
if mibBuilder.loadTexts:
    h3cMcsL2EntryTable.setStatus("current")
_H3cMcsL2EntryEntry_Object = MibTableRow
h3cMcsL2EntryEntry = _H3cMcsL2EntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1)
)
h3cMcsL2EntryEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntryVUType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntryVUID"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntryAddressType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntryGroupAddress"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntrySourceAddress"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsL2EntryIfIndex"),
)
if mibBuilder.loadTexts:
    h3cMcsL2EntryEntry.setStatus("current")
_H3cMcsL2EntryVUType_Type = H3cVirtualUnitType
_H3cMcsL2EntryVUType_Object = MibTableColumn
h3cMcsL2EntryVUType = _H3cMcsL2EntryVUType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 1),
    _H3cMcsL2EntryVUType_Type()
)
h3cMcsL2EntryVUType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntryVUType.setStatus("current")
_H3cMcsL2EntryVUID_Type = Unsigned32
_H3cMcsL2EntryVUID_Object = MibTableColumn
h3cMcsL2EntryVUID = _H3cMcsL2EntryVUID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 2),
    _H3cMcsL2EntryVUID_Type()
)
h3cMcsL2EntryVUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntryVUID.setStatus("current")
_H3cMcsL2EntryAddressType_Type = InetAddressType
_H3cMcsL2EntryAddressType_Object = MibTableColumn
h3cMcsL2EntryAddressType = _H3cMcsL2EntryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 3),
    _H3cMcsL2EntryAddressType_Type()
)
h3cMcsL2EntryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntryAddressType.setStatus("current")
_H3cMcsL2EntryGroupAddress_Type = InetAddress
_H3cMcsL2EntryGroupAddress_Object = MibTableColumn
h3cMcsL2EntryGroupAddress = _H3cMcsL2EntryGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 4),
    _H3cMcsL2EntryGroupAddress_Type()
)
h3cMcsL2EntryGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntryGroupAddress.setStatus("current")
_H3cMcsL2EntrySourceAddress_Type = InetAddress
_H3cMcsL2EntrySourceAddress_Object = MibTableColumn
h3cMcsL2EntrySourceAddress = _H3cMcsL2EntrySourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 5),
    _H3cMcsL2EntrySourceAddress_Type()
)
h3cMcsL2EntrySourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntrySourceAddress.setStatus("current")
_H3cMcsL2EntryIfIndex_Type = InterfaceIndex
_H3cMcsL2EntryIfIndex_Object = MibTableColumn
h3cMcsL2EntryIfIndex = _H3cMcsL2EntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 6),
    _H3cMcsL2EntryIfIndex_Type()
)
h3cMcsL2EntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsL2EntryIfIndex.setStatus("current")


class _H3cMcsL2EntryPortType_Type(Integer32):
    """Custom type h3cMcsL2EntryPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("ac", 2),
          ("npw", 3),
          ("upw", 4),
          ("trill", 5),
          ("tunnel", 6),
          ("mtunnel", 7))
    )


_H3cMcsL2EntryPortType_Type.__name__ = "Integer32"
_H3cMcsL2EntryPortType_Object = MibTableColumn
h3cMcsL2EntryPortType = _H3cMcsL2EntryPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 7),
    _H3cMcsL2EntryPortType_Type()
)
h3cMcsL2EntryPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsL2EntryPortType.setStatus("current")


class _H3cMcsL2EntryPortAttribute_Type(Bits):
    """Custom type h3cMcsL2EntryPortAttribute based on Bits"""
    namedValues = NamedValues(
        *(("d", 0),
          ("s", 1),
          ("p", 2),
          ("k", 3),
          ("r", 4),
          ("w", 5),
          ("b", 6),
          ("e", 7),
          ("de", 8),
          ("ee", 9),
          ("suc", 10),
          ("f", 11))
    )

_H3cMcsL2EntryPortAttribute_Type.__name__ = "Bits"
_H3cMcsL2EntryPortAttribute_Object = MibTableColumn
h3cMcsL2EntryPortAttribute = _H3cMcsL2EntryPortAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 3, 1, 8),
    _H3cMcsL2EntryPortAttribute_Type()
)
h3cMcsL2EntryPortAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsL2EntryPortAttribute.setStatus("current")
_H3cMcsPacketStatisticsTable_Object = MibTable
h3cMcsPacketStatisticsTable = _H3cMcsPacketStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4)
)
if mibBuilder.loadTexts:
    h3cMcsPacketStatisticsTable.setStatus("current")
_H3cMcsPacketStatisticsEntry_Object = MibTableRow
h3cMcsPacketStatisticsEntry = _H3cMcsPacketStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1)
)
h3cMcsPacketStatisticsEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsStatisticsSnoopingType"),
)
if mibBuilder.loadTexts:
    h3cMcsPacketStatisticsEntry.setStatus("current")
_H3cMcsStatisticsSnoopingType_Type = InetAddressType
_H3cMcsStatisticsSnoopingType_Object = MibTableColumn
h3cMcsStatisticsSnoopingType = _H3cMcsStatisticsSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 1),
    _H3cMcsStatisticsSnoopingType_Type()
)
h3cMcsStatisticsSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsStatisticsSnoopingType.setStatus("current")
_H3cMcsRxGeneryQueryNum_Type = Counter64
_H3cMcsRxGeneryQueryNum_Object = MibTableColumn
h3cMcsRxGeneryQueryNum = _H3cMcsRxGeneryQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 2),
    _H3cMcsRxGeneryQueryNum_Type()
)
h3cMcsRxGeneryQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxGeneryQueryNum.setStatus("current")
_H3cMcsRxV2SpecificQueryNum_Type = Counter64
_H3cMcsRxV2SpecificQueryNum_Object = MibTableColumn
h3cMcsRxV2SpecificQueryNum = _H3cMcsRxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 3),
    _H3cMcsRxV2SpecificQueryNum_Type()
)
h3cMcsRxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV2SpecificQueryNum.setStatus("current")
_H3cMcsRxV3SpecificQueryNum_Type = Counter64
_H3cMcsRxV3SpecificQueryNum_Object = MibTableColumn
h3cMcsRxV3SpecificQueryNum = _H3cMcsRxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 4),
    _H3cMcsRxV3SpecificQueryNum_Type()
)
h3cMcsRxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV3SpecificQueryNum.setStatus("current")
_H3cMcsRxV3SpecificSGQueryNum_Type = Counter64
_H3cMcsRxV3SpecificSGQueryNum_Object = MibTableColumn
h3cMcsRxV3SpecificSGQueryNum = _H3cMcsRxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 5),
    _H3cMcsRxV3SpecificSGQueryNum_Type()
)
h3cMcsRxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV3SpecificSGQueryNum.setStatus("current")
_H3cMcsRxV1ReportNum_Type = Counter64
_H3cMcsRxV1ReportNum_Object = MibTableColumn
h3cMcsRxV1ReportNum = _H3cMcsRxV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 6),
    _H3cMcsRxV1ReportNum_Type()
)
h3cMcsRxV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV1ReportNum.setStatus("current")
_H3cMcsRxV2ReportNum_Type = Counter64
_H3cMcsRxV2ReportNum_Object = MibTableColumn
h3cMcsRxV2ReportNum = _H3cMcsRxV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 7),
    _H3cMcsRxV2ReportNum_Type()
)
h3cMcsRxV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV2ReportNum.setStatus("current")
_H3cMcsRxV3ReportNum_Type = Counter64
_H3cMcsRxV3ReportNum_Object = MibTableColumn
h3cMcsRxV3ReportNum = _H3cMcsRxV3ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 8),
    _H3cMcsRxV3ReportNum_Type()
)
h3cMcsRxV3ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV3ReportNum.setStatus("current")
_H3cMcsRxV3ErrCorReportNum_Type = Counter64
_H3cMcsRxV3ErrCorReportNum_Object = MibTableColumn
h3cMcsRxV3ErrCorReportNum = _H3cMcsRxV3ErrCorReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 9),
    _H3cMcsRxV3ErrCorReportNum_Type()
)
h3cMcsRxV3ErrCorReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxV3ErrCorReportNum.setStatus("current")
_H3cMcsRxLeaveNum_Type = Counter64
_H3cMcsRxLeaveNum_Object = MibTableColumn
h3cMcsRxLeaveNum = _H3cMcsRxLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 10),
    _H3cMcsRxLeaveNum_Type()
)
h3cMcsRxLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxLeaveNum.setStatus("current")
_H3cMcsRxPimHelloNum_Type = Counter64
_H3cMcsRxPimHelloNum_Object = MibTableColumn
h3cMcsRxPimHelloNum = _H3cMcsRxPimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 11),
    _H3cMcsRxPimHelloNum_Type()
)
h3cMcsRxPimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxPimHelloNum.setStatus("current")
_H3cMcsRxErrorPacketNum_Type = Counter64
_H3cMcsRxErrorPacketNum_Object = MibTableColumn
h3cMcsRxErrorPacketNum = _H3cMcsRxErrorPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 12),
    _H3cMcsRxErrorPacketNum_Type()
)
h3cMcsRxErrorPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsRxErrorPacketNum.setStatus("current")
_H3cMcsTxV2SpecificQueryNum_Type = Counter64
_H3cMcsTxV2SpecificQueryNum_Object = MibTableColumn
h3cMcsTxV2SpecificQueryNum = _H3cMcsTxV2SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 13),
    _H3cMcsTxV2SpecificQueryNum_Type()
)
h3cMcsTxV2SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsTxV2SpecificQueryNum.setStatus("current")
_H3cMcsTxV3SpecificQueryNum_Type = Counter64
_H3cMcsTxV3SpecificQueryNum_Object = MibTableColumn
h3cMcsTxV3SpecificQueryNum = _H3cMcsTxV3SpecificQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 14),
    _H3cMcsTxV3SpecificQueryNum_Type()
)
h3cMcsTxV3SpecificQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsTxV3SpecificQueryNum.setStatus("current")
_H3cMcsTxV3SpecificSGQueryNum_Type = Counter64
_H3cMcsTxV3SpecificSGQueryNum_Object = MibTableColumn
h3cMcsTxV3SpecificSGQueryNum = _H3cMcsTxV3SpecificSGQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 4, 1, 15),
    _H3cMcsTxV3SpecificSGQueryNum_Type()
)
h3cMcsTxV3SpecificSGQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMcsTxV3SpecificSGQueryNum.setStatus("current")
_H3cMcsPortJoinGroupConfigTable_Object = MibTable
h3cMcsPortJoinGroupConfigTable = _H3cMcsPortJoinGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5)
)
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupConfigTable.setStatus("current")
_H3cMcsPortJoinGroupConfigEntry_Object = MibTableRow
h3cMcsPortJoinGroupConfigEntry = _H3cMcsPortJoinGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1)
)
h3cMcsPortJoinGroupConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortJoinGroupIfIndex"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortJoinGroupSnoopingType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortJoinGroupVlanID"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortJoinGroupGroupAddress"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortJoinGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupConfigEntry.setStatus("current")
_H3cMcsPortJoinGroupIfIndex_Type = InterfaceIndex
_H3cMcsPortJoinGroupIfIndex_Object = MibTableColumn
h3cMcsPortJoinGroupIfIndex = _H3cMcsPortJoinGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 1),
    _H3cMcsPortJoinGroupIfIndex_Type()
)
h3cMcsPortJoinGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupIfIndex.setStatus("current")
_H3cMcsPortJoinGroupSnoopingType_Type = InetAddressType
_H3cMcsPortJoinGroupSnoopingType_Object = MibTableColumn
h3cMcsPortJoinGroupSnoopingType = _H3cMcsPortJoinGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 2),
    _H3cMcsPortJoinGroupSnoopingType_Type()
)
h3cMcsPortJoinGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupSnoopingType.setStatus("current")


class _H3cMcsPortJoinGroupVlanID_Type(Unsigned32):
    """Custom type h3cMcsPortJoinGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMcsPortJoinGroupVlanID_Type.__name__ = "Unsigned32"
_H3cMcsPortJoinGroupVlanID_Object = MibTableColumn
h3cMcsPortJoinGroupVlanID = _H3cMcsPortJoinGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 3),
    _H3cMcsPortJoinGroupVlanID_Type()
)
h3cMcsPortJoinGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupVlanID.setStatus("current")
_H3cMcsPortJoinGroupGroupAddress_Type = InetAddress
_H3cMcsPortJoinGroupGroupAddress_Object = MibTableColumn
h3cMcsPortJoinGroupGroupAddress = _H3cMcsPortJoinGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 4),
    _H3cMcsPortJoinGroupGroupAddress_Type()
)
h3cMcsPortJoinGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupGroupAddress.setStatus("current")
_H3cMcsPortJoinGroupSourceAddress_Type = InetAddress
_H3cMcsPortJoinGroupSourceAddress_Object = MibTableColumn
h3cMcsPortJoinGroupSourceAddress = _H3cMcsPortJoinGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 5),
    _H3cMcsPortJoinGroupSourceAddress_Type()
)
h3cMcsPortJoinGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupSourceAddress.setStatus("current")
_H3cMcsPortJoinGroupStatus_Type = RowStatus
_H3cMcsPortJoinGroupStatus_Object = MibTableColumn
h3cMcsPortJoinGroupStatus = _H3cMcsPortJoinGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 5, 1, 6),
    _H3cMcsPortJoinGroupStatus_Type()
)
h3cMcsPortJoinGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortJoinGroupStatus.setStatus("current")
_H3cMcsPortStaticGroupConfigTable_Object = MibTable
h3cMcsPortStaticGroupConfigTable = _H3cMcsPortStaticGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6)
)
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupConfigTable.setStatus("current")
_H3cMcsPortStaticGroupConfigEntry_Object = MibTableRow
h3cMcsPortStaticGroupConfigEntry = _H3cMcsPortStaticGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1)
)
h3cMcsPortStaticGroupConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortStaticGroupIfIndex"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortStaticGroupSnoopingType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortStaticGroupVlanID"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortStaticGroupGroupAddress"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortStaticGroupSourceAddress"),
)
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupConfigEntry.setStatus("current")
_H3cMcsPortStaticGroupIfIndex_Type = InterfaceIndex
_H3cMcsPortStaticGroupIfIndex_Object = MibTableColumn
h3cMcsPortStaticGroupIfIndex = _H3cMcsPortStaticGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 1),
    _H3cMcsPortStaticGroupIfIndex_Type()
)
h3cMcsPortStaticGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupIfIndex.setStatus("current")
_H3cMcsPortStaticGroupSnoopingType_Type = InetAddressType
_H3cMcsPortStaticGroupSnoopingType_Object = MibTableColumn
h3cMcsPortStaticGroupSnoopingType = _H3cMcsPortStaticGroupSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 2),
    _H3cMcsPortStaticGroupSnoopingType_Type()
)
h3cMcsPortStaticGroupSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupSnoopingType.setStatus("current")


class _H3cMcsPortStaticGroupVlanID_Type(Unsigned32):
    """Custom type h3cMcsPortStaticGroupVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMcsPortStaticGroupVlanID_Type.__name__ = "Unsigned32"
_H3cMcsPortStaticGroupVlanID_Object = MibTableColumn
h3cMcsPortStaticGroupVlanID = _H3cMcsPortStaticGroupVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 3),
    _H3cMcsPortStaticGroupVlanID_Type()
)
h3cMcsPortStaticGroupVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupVlanID.setStatus("current")
_H3cMcsPortStaticGroupGroupAddress_Type = InetAddress
_H3cMcsPortStaticGroupGroupAddress_Object = MibTableColumn
h3cMcsPortStaticGroupGroupAddress = _H3cMcsPortStaticGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 4),
    _H3cMcsPortStaticGroupGroupAddress_Type()
)
h3cMcsPortStaticGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupGroupAddress.setStatus("current")
_H3cMcsPortStaticGroupSourceAddress_Type = InetAddress
_H3cMcsPortStaticGroupSourceAddress_Object = MibTableColumn
h3cMcsPortStaticGroupSourceAddress = _H3cMcsPortStaticGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 5),
    _H3cMcsPortStaticGroupSourceAddress_Type()
)
h3cMcsPortStaticGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupSourceAddress.setStatus("current")
_H3cMcsPortStaticGroupStatus_Type = RowStatus
_H3cMcsPortStaticGroupStatus_Object = MibTableColumn
h3cMcsPortStaticGroupStatus = _H3cMcsPortStaticGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 6, 1, 6),
    _H3cMcsPortStaticGroupStatus_Type()
)
h3cMcsPortStaticGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortStaticGroupStatus.setStatus("current")
_H3cMcsRouterPortConfigTable_Object = MibTable
h3cMcsRouterPortConfigTable = _H3cMcsRouterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7)
)
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigTable.setStatus("current")
_H3cMcsRouterPortConfigEntry_Object = MibTableRow
h3cMcsRouterPortConfigEntry = _H3cMcsRouterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7, 1)
)
h3cMcsRouterPortConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsRouterPortConfigIfIndex"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsRouterPortConfigSnoopingType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsRouterPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigEntry.setStatus("current")
_H3cMcsRouterPortConfigIfIndex_Type = InterfaceIndex
_H3cMcsRouterPortConfigIfIndex_Object = MibTableColumn
h3cMcsRouterPortConfigIfIndex = _H3cMcsRouterPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7, 1, 1),
    _H3cMcsRouterPortConfigIfIndex_Type()
)
h3cMcsRouterPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigIfIndex.setStatus("current")
_H3cMcsRouterPortConfigSnoopingType_Type = InetAddressType
_H3cMcsRouterPortConfigSnoopingType_Object = MibTableColumn
h3cMcsRouterPortConfigSnoopingType = _H3cMcsRouterPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7, 1, 2),
    _H3cMcsRouterPortConfigSnoopingType_Type()
)
h3cMcsRouterPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigSnoopingType.setStatus("current")


class _H3cMcsRouterPortConfigVlanID_Type(Unsigned32):
    """Custom type h3cMcsRouterPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMcsRouterPortConfigVlanID_Type.__name__ = "Unsigned32"
_H3cMcsRouterPortConfigVlanID_Object = MibTableColumn
h3cMcsRouterPortConfigVlanID = _H3cMcsRouterPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7, 1, 3),
    _H3cMcsRouterPortConfigVlanID_Type()
)
h3cMcsRouterPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigVlanID.setStatus("current")
_H3cMcsRouterPortConfigRowStatus_Type = RowStatus
_H3cMcsRouterPortConfigRowStatus_Object = MibTableColumn
h3cMcsRouterPortConfigRowStatus = _H3cMcsRouterPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 7, 1, 4),
    _H3cMcsRouterPortConfigRowStatus_Type()
)
h3cMcsRouterPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsRouterPortConfigRowStatus.setStatus("current")
_H3cMcsPortConfigTable_Object = MibTable
h3cMcsPortConfigTable = _H3cMcsPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8)
)
if mibBuilder.loadTexts:
    h3cMcsPortConfigTable.setStatus("current")
_H3cMcsPortConfigEntry_Object = MibTableRow
h3cMcsPortConfigEntry = _H3cMcsPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1)
)
h3cMcsPortConfigEntry.setIndexNames(
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortConfigIfIndex"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortConfigSnoopingType"),
    (0, "H3C-MULTICAST-SNOOPING-MIB", "h3cMcsPortConfigVlanID"),
)
if mibBuilder.loadTexts:
    h3cMcsPortConfigEntry.setStatus("current")
_H3cMcsPortConfigIfIndex_Type = InterfaceIndex
_H3cMcsPortConfigIfIndex_Object = MibTableColumn
h3cMcsPortConfigIfIndex = _H3cMcsPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 1),
    _H3cMcsPortConfigIfIndex_Type()
)
h3cMcsPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortConfigIfIndex.setStatus("current")
_H3cMcsPortConfigSnoopingType_Type = InetAddressType
_H3cMcsPortConfigSnoopingType_Object = MibTableColumn
h3cMcsPortConfigSnoopingType = _H3cMcsPortConfigSnoopingType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 2),
    _H3cMcsPortConfigSnoopingType_Type()
)
h3cMcsPortConfigSnoopingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortConfigSnoopingType.setStatus("current")


class _H3cMcsPortConfigVlanID_Type(Unsigned32):
    """Custom type h3cMcsPortConfigVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMcsPortConfigVlanID_Type.__name__ = "Unsigned32"
_H3cMcsPortConfigVlanID_Object = MibTableColumn
h3cMcsPortConfigVlanID = _H3cMcsPortConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 3),
    _H3cMcsPortConfigVlanID_Type()
)
h3cMcsPortConfigVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMcsPortConfigVlanID.setStatus("current")
_H3cMcsPortConfigGroupLimitNumber_Type = Unsigned32
_H3cMcsPortConfigGroupLimitNumber_Object = MibTableColumn
h3cMcsPortConfigGroupLimitNumber = _H3cMcsPortConfigGroupLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 4),
    _H3cMcsPortConfigGroupLimitNumber_Type()
)
h3cMcsPortConfigGroupLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortConfigGroupLimitNumber.setStatus("current")


class _H3cMcsPortConfigFastLeaveStatus_Type(TruthValue):
    """Custom type h3cMcsPortConfigFastLeaveStatus based on TruthValue"""
    defaultValue = 2


_H3cMcsPortConfigFastLeaveStatus_Type.__name__ = "TruthValue"
_H3cMcsPortConfigFastLeaveStatus_Object = MibTableColumn
h3cMcsPortConfigFastLeaveStatus = _H3cMcsPortConfigFastLeaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 5),
    _H3cMcsPortConfigFastLeaveStatus_Type()
)
h3cMcsPortConfigFastLeaveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortConfigFastLeaveStatus.setStatus("current")


class _H3cMcsPortConfigGroupPolicyParameter_Type(Unsigned32):
    """Custom type h3cMcsPortConfigGroupPolicyParameter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_H3cMcsPortConfigGroupPolicyParameter_Type.__name__ = "Unsigned32"
_H3cMcsPortConfigGroupPolicyParameter_Object = MibTableColumn
h3cMcsPortConfigGroupPolicyParameter = _H3cMcsPortConfigGroupPolicyParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 6),
    _H3cMcsPortConfigGroupPolicyParameter_Type()
)
h3cMcsPortConfigGroupPolicyParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortConfigGroupPolicyParameter.setStatus("current")


class _H3cMcsPortConfigOverflowReplace_Type(TruthValue):
    """Custom type h3cMcsPortConfigOverflowReplace based on TruthValue"""
    defaultValue = 2


_H3cMcsPortConfigOverflowReplace_Type.__name__ = "TruthValue"
_H3cMcsPortConfigOverflowReplace_Object = MibTableColumn
h3cMcsPortConfigOverflowReplace = _H3cMcsPortConfigOverflowReplace_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 7),
    _H3cMcsPortConfigOverflowReplace_Type()
)
h3cMcsPortConfigOverflowReplace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortConfigOverflowReplace.setStatus("current")
_H3cMcsPortConfigRowStatus_Type = RowStatus
_H3cMcsPortConfigRowStatus_Object = MibTableColumn
h3cMcsPortConfigRowStatus = _H3cMcsPortConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 123, 1, 8, 1, 8),
    _H3cMcsPortConfigRowStatus_Type()
)
h3cMcsPortConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMcsPortConfigRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MULTICAST-SNOOPING-MIB",
    **{"H3cVirtualUnitType": H3cVirtualUnitType,
       "h3cMulticastSnoop": h3cMulticastSnoop,
       "h3cMulticastSnoopObject": h3cMulticastSnoopObject,
       "h3cMcsGlobalConfigTable": h3cMcsGlobalConfigTable,
       "h3cMcsGlobalConfigEntry": h3cMcsGlobalConfigEntry,
       "h3cMcsGlbSnoopingType": h3cMcsGlbSnoopingType,
       "h3cMcsGlbRowStatus": h3cMcsGlbRowStatus,
       "h3cMcsGlbEntryLimit": h3cMcsGlbEntryLimit,
       "h3cMcsGlbHostAgingTime": h3cMcsGlbHostAgingTime,
       "h3cMcsGlbMaxResponseTime": h3cMcsGlbMaxResponseTime,
       "h3cMcsGlbRouterAgingTime": h3cMcsGlbRouterAgingTime,
       "h3cMcsGlbLastMemQryInterval": h3cMcsGlbLastMemQryInterval,
       "h3cMcsGlbDropUnknownEnabled": h3cMcsGlbDropUnknownEnabled,
       "h3cMcsVirtualUnitConfigTable": h3cMcsVirtualUnitConfigTable,
       "h3cMcsVirtualUnitConfigEntry": h3cMcsVirtualUnitConfigEntry,
       "h3cMcsVUType": h3cMcsVUType,
       "h3cMcsVUID": h3cMcsVUID,
       "h3cMcsVUSnoopingType": h3cMcsVUSnoopingType,
       "h3cMcsVURowStatus": h3cMcsVURowStatus,
       "h3cMcsVUHostAgingTime": h3cMcsVUHostAgingTime,
       "h3cMcsVUMaxResponseTime": h3cMcsVUMaxResponseTime,
       "h3cMcsVURouterAgingTime": h3cMcsVURouterAgingTime,
       "h3cMcsVULastMemQryInterval": h3cMcsVULastMemQryInterval,
       "h3cMcsVUDropUnknownEnabled": h3cMcsVUDropUnknownEnabled,
       "h3cMcsVUPimSnoopingEnabled": h3cMcsVUPimSnoopingEnabled,
       "h3cMcsVUVersion": h3cMcsVUVersion,
       "h3cMcsVUQuerierEnabled": h3cMcsVUQuerierEnabled,
       "h3cMcsVUQuerierInterval": h3cMcsVUQuerierInterval,
       "h3cMcsVUGeneQuerierSourceAddress": h3cMcsVUGeneQuerierSourceAddress,
       "h3cMcsVUSpecQuerierSourceAddress": h3cMcsVUSpecQuerierSourceAddress,
       "h3cMcsVULeaveSourceAddress": h3cMcsVULeaveSourceAddress,
       "h3cMcsVUReportSourceAddress": h3cMcsVUReportSourceAddress,
       "h3cMcsVUProxyEnabled": h3cMcsVUProxyEnabled,
       "h3cMcsVUQuerierElection": h3cMcsVUQuerierElection,
       "h3cMcsL2EntryTable": h3cMcsL2EntryTable,
       "h3cMcsL2EntryEntry": h3cMcsL2EntryEntry,
       "h3cMcsL2EntryVUType": h3cMcsL2EntryVUType,
       "h3cMcsL2EntryVUID": h3cMcsL2EntryVUID,
       "h3cMcsL2EntryAddressType": h3cMcsL2EntryAddressType,
       "h3cMcsL2EntryGroupAddress": h3cMcsL2EntryGroupAddress,
       "h3cMcsL2EntrySourceAddress": h3cMcsL2EntrySourceAddress,
       "h3cMcsL2EntryIfIndex": h3cMcsL2EntryIfIndex,
       "h3cMcsL2EntryPortType": h3cMcsL2EntryPortType,
       "h3cMcsL2EntryPortAttribute": h3cMcsL2EntryPortAttribute,
       "h3cMcsPacketStatisticsTable": h3cMcsPacketStatisticsTable,
       "h3cMcsPacketStatisticsEntry": h3cMcsPacketStatisticsEntry,
       "h3cMcsStatisticsSnoopingType": h3cMcsStatisticsSnoopingType,
       "h3cMcsRxGeneryQueryNum": h3cMcsRxGeneryQueryNum,
       "h3cMcsRxV2SpecificQueryNum": h3cMcsRxV2SpecificQueryNum,
       "h3cMcsRxV3SpecificQueryNum": h3cMcsRxV3SpecificQueryNum,
       "h3cMcsRxV3SpecificSGQueryNum": h3cMcsRxV3SpecificSGQueryNum,
       "h3cMcsRxV1ReportNum": h3cMcsRxV1ReportNum,
       "h3cMcsRxV2ReportNum": h3cMcsRxV2ReportNum,
       "h3cMcsRxV3ReportNum": h3cMcsRxV3ReportNum,
       "h3cMcsRxV3ErrCorReportNum": h3cMcsRxV3ErrCorReportNum,
       "h3cMcsRxLeaveNum": h3cMcsRxLeaveNum,
       "h3cMcsRxPimHelloNum": h3cMcsRxPimHelloNum,
       "h3cMcsRxErrorPacketNum": h3cMcsRxErrorPacketNum,
       "h3cMcsTxV2SpecificQueryNum": h3cMcsTxV2SpecificQueryNum,
       "h3cMcsTxV3SpecificQueryNum": h3cMcsTxV3SpecificQueryNum,
       "h3cMcsTxV3SpecificSGQueryNum": h3cMcsTxV3SpecificSGQueryNum,
       "h3cMcsPortJoinGroupConfigTable": h3cMcsPortJoinGroupConfigTable,
       "h3cMcsPortJoinGroupConfigEntry": h3cMcsPortJoinGroupConfigEntry,
       "h3cMcsPortJoinGroupIfIndex": h3cMcsPortJoinGroupIfIndex,
       "h3cMcsPortJoinGroupSnoopingType": h3cMcsPortJoinGroupSnoopingType,
       "h3cMcsPortJoinGroupVlanID": h3cMcsPortJoinGroupVlanID,
       "h3cMcsPortJoinGroupGroupAddress": h3cMcsPortJoinGroupGroupAddress,
       "h3cMcsPortJoinGroupSourceAddress": h3cMcsPortJoinGroupSourceAddress,
       "h3cMcsPortJoinGroupStatus": h3cMcsPortJoinGroupStatus,
       "h3cMcsPortStaticGroupConfigTable": h3cMcsPortStaticGroupConfigTable,
       "h3cMcsPortStaticGroupConfigEntry": h3cMcsPortStaticGroupConfigEntry,
       "h3cMcsPortStaticGroupIfIndex": h3cMcsPortStaticGroupIfIndex,
       "h3cMcsPortStaticGroupSnoopingType": h3cMcsPortStaticGroupSnoopingType,
       "h3cMcsPortStaticGroupVlanID": h3cMcsPortStaticGroupVlanID,
       "h3cMcsPortStaticGroupGroupAddress": h3cMcsPortStaticGroupGroupAddress,
       "h3cMcsPortStaticGroupSourceAddress": h3cMcsPortStaticGroupSourceAddress,
       "h3cMcsPortStaticGroupStatus": h3cMcsPortStaticGroupStatus,
       "h3cMcsRouterPortConfigTable": h3cMcsRouterPortConfigTable,
       "h3cMcsRouterPortConfigEntry": h3cMcsRouterPortConfigEntry,
       "h3cMcsRouterPortConfigIfIndex": h3cMcsRouterPortConfigIfIndex,
       "h3cMcsRouterPortConfigSnoopingType": h3cMcsRouterPortConfigSnoopingType,
       "h3cMcsRouterPortConfigVlanID": h3cMcsRouterPortConfigVlanID,
       "h3cMcsRouterPortConfigRowStatus": h3cMcsRouterPortConfigRowStatus,
       "h3cMcsPortConfigTable": h3cMcsPortConfigTable,
       "h3cMcsPortConfigEntry": h3cMcsPortConfigEntry,
       "h3cMcsPortConfigIfIndex": h3cMcsPortConfigIfIndex,
       "h3cMcsPortConfigSnoopingType": h3cMcsPortConfigSnoopingType,
       "h3cMcsPortConfigVlanID": h3cMcsPortConfigVlanID,
       "h3cMcsPortConfigGroupLimitNumber": h3cMcsPortConfigGroupLimitNumber,
       "h3cMcsPortConfigFastLeaveStatus": h3cMcsPortConfigFastLeaveStatus,
       "h3cMcsPortConfigGroupPolicyParameter": h3cMcsPortConfigGroupPolicyParameter,
       "h3cMcsPortConfigOverflowReplace": h3cMcsPortConfigOverflowReplace,
       "h3cMcsPortConfigRowStatus": h3cMcsPortConfigRowStatus}
)
