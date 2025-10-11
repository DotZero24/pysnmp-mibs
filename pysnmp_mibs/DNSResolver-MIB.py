# SNMP MIB module (DNSResolver-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DNSResolver-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:42 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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


# MODULE-IDENTITY

swDNSResolverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 85)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DnsName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class DnsTime(TextualConvention, Integer32):
    status = "current"
    displayHint = "4d"


# MIB Managed Objects in the order of their OIDs

_SwDNSResolverMIBObjects_ObjectIdentity = ObjectIdentity
swDNSResolverMIBObjects = _SwDNSResolverMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1)
)


class _SwDNSResState_Type(Integer32):
    """Custom type swDNSResState based on Integer32"""
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


_SwDNSResState_Type.__name__ = "Integer32"
_SwDNSResState_Object = MibScalar
swDNSResState = _SwDNSResState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 1),
    _SwDNSResState_Type()
)
swDNSResState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResState.setStatus("current")


class _SwDNSResNameSrvTimeOut_Type(Integer32):
    """Custom type swDNSResNameSrvTimeOut based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SwDNSResNameSrvTimeOut_Type.__name__ = "Integer32"
_SwDNSResNameSrvTimeOut_Object = MibScalar
swDNSResNameSrvTimeOut = _SwDNSResNameSrvTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 2),
    _SwDNSResNameSrvTimeOut_Type()
)
swDNSResNameSrvTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResNameSrvTimeOut.setStatus("current")
_SwDNSResNameSrv_ObjectIdentity = ObjectIdentity
swDNSResNameSrv = _SwDNSResNameSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3)
)
_SwDNSResStaticNameSrvTable_Object = MibTable
swDNSResStaticNameSrvTable = _SwDNSResStaticNameSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1)
)
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvTable.setStatus("current")
_SwDNSResStaticNameSrvEntry_Object = MibTableRow
swDNSResStaticNameSrvEntry = _SwDNSResStaticNameSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1, 1)
)
swDNSResStaticNameSrvEntry.setIndexNames(
    (0, "DNSResolver-MIB", "swDNSResStaticNameSrvIndex"),
)
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvEntry.setStatus("current")
_SwDNSResStaticNameSrvIndex_Type = Integer32
_SwDNSResStaticNameSrvIndex_Object = MibTableColumn
swDNSResStaticNameSrvIndex = _SwDNSResStaticNameSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1, 1, 1),
    _SwDNSResStaticNameSrvIndex_Type()
)
swDNSResStaticNameSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvIndex.setStatus("current")
_SwDNSResStaticNameSrvRowStatus_Type = RowStatus
_SwDNSResStaticNameSrvRowStatus_Object = MibTableColumn
swDNSResStaticNameSrvRowStatus = _SwDNSResStaticNameSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1, 1, 2),
    _SwDNSResStaticNameSrvRowStatus_Type()
)
swDNSResStaticNameSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvRowStatus.setStatus("current")
_SwDNSResStaticNameSrvIPaddr_Type = IpAddress
_SwDNSResStaticNameSrvIPaddr_Object = MibTableColumn
swDNSResStaticNameSrvIPaddr = _SwDNSResStaticNameSrvIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1, 1, 3),
    _SwDNSResStaticNameSrvIPaddr_Type()
)
swDNSResStaticNameSrvIPaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvIPaddr.setStatus("current")


class _SwDNSResStaticNameSrvPriority_Type(Integer32):
    """Custom type swDNSResStaticNameSrvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SwDNSResStaticNameSrvPriority_Type.__name__ = "Integer32"
_SwDNSResStaticNameSrvPriority_Object = MibTableColumn
swDNSResStaticNameSrvPriority = _SwDNSResStaticNameSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 1, 1, 4),
    _SwDNSResStaticNameSrvPriority_Type()
)
swDNSResStaticNameSrvPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticNameSrvPriority.setStatus("current")
_SwDNSResDynamicNameSrvTable_Object = MibTable
swDNSResDynamicNameSrvTable = _SwDNSResDynamicNameSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 2)
)
if mibBuilder.loadTexts:
    swDNSResDynamicNameSrvTable.setStatus("current")
_SwDNSResDynamicNameSrvEntry_Object = MibTableRow
swDNSResDynamicNameSrvEntry = _SwDNSResDynamicNameSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 2, 1)
)
swDNSResDynamicNameSrvEntry.setIndexNames(
    (0, "DNSResolver-MIB", "swDNSResDynamicNameSrvIndex"),
)
if mibBuilder.loadTexts:
    swDNSResDynamicNameSrvEntry.setStatus("current")
_SwDNSResDynamicNameSrvIndex_Type = Integer32
_SwDNSResDynamicNameSrvIndex_Object = MibTableColumn
swDNSResDynamicNameSrvIndex = _SwDNSResDynamicNameSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 2, 1, 1),
    _SwDNSResDynamicNameSrvIndex_Type()
)
swDNSResDynamicNameSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDNSResDynamicNameSrvIndex.setStatus("current")
_SwDNSResDynamicNameSrvIPaddr_Type = IpAddress
_SwDNSResDynamicNameSrvIPaddr_Object = MibTableColumn
swDNSResDynamicNameSrvIPaddr = _SwDNSResDynamicNameSrvIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 2, 1, 2),
    _SwDNSResDynamicNameSrvIPaddr_Type()
)
swDNSResDynamicNameSrvIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDNSResDynamicNameSrvIPaddr.setStatus("current")


class _SwDNSResDynamicNameSrvPriority_Type(Integer32):
    """Custom type swDNSResDynamicNameSrvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SwDNSResDynamicNameSrvPriority_Type.__name__ = "Integer32"
_SwDNSResDynamicNameSrvPriority_Object = MibTableColumn
swDNSResDynamicNameSrvPriority = _SwDNSResDynamicNameSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 2, 1, 3),
    _SwDNSResDynamicNameSrvPriority_Type()
)
swDNSResDynamicNameSrvPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDNSResDynamicNameSrvPriority.setStatus("current")
_SwDNSResStaticIPv6NameSrvTable_Object = MibTable
swDNSResStaticIPv6NameSrvTable = _SwDNSResStaticIPv6NameSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3)
)
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvTable.setStatus("current")
_SwDNSResStaticIPv6NameSrvEntry_Object = MibTableRow
swDNSResStaticIPv6NameSrvEntry = _SwDNSResStaticIPv6NameSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1)
)
swDNSResStaticIPv6NameSrvEntry.setIndexNames(
    (0, "DNSResolver-MIB", "swDNSResStaticIPv6NameSrvIndex"),
)
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvEntry.setStatus("current")
_SwDNSResStaticIPv6NameSrvIndex_Type = Integer32
_SwDNSResStaticIPv6NameSrvIndex_Object = MibTableColumn
swDNSResStaticIPv6NameSrvIndex = _SwDNSResStaticIPv6NameSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1, 1),
    _SwDNSResStaticIPv6NameSrvIndex_Type()
)
swDNSResStaticIPv6NameSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvIndex.setStatus("current")
_SwDNSResStaticIPv6NameSrvaddr_Type = Ipv6Address
_SwDNSResStaticIPv6NameSrvaddr_Object = MibTableColumn
swDNSResStaticIPv6NameSrvaddr = _SwDNSResStaticIPv6NameSrvaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1, 2),
    _SwDNSResStaticIPv6NameSrvaddr_Type()
)
swDNSResStaticIPv6NameSrvaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvaddr.setStatus("current")


class _SwDNSResStaticIPv6NameSrvIntfName_Type(DisplayString):
    """Custom type swDNSResStaticIPv6NameSrvIntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwDNSResStaticIPv6NameSrvIntfName_Type.__name__ = "DisplayString"
_SwDNSResStaticIPv6NameSrvIntfName_Object = MibTableColumn
swDNSResStaticIPv6NameSrvIntfName = _SwDNSResStaticIPv6NameSrvIntfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1, 3),
    _SwDNSResStaticIPv6NameSrvIntfName_Type()
)
swDNSResStaticIPv6NameSrvIntfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvIntfName.setStatus("current")


class _SwDNSResStaticIPv6NameSrvPriority_Type(Integer32):
    """Custom type swDNSResStaticIPv6NameSrvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SwDNSResStaticIPv6NameSrvPriority_Type.__name__ = "Integer32"
_SwDNSResStaticIPv6NameSrvPriority_Object = MibTableColumn
swDNSResStaticIPv6NameSrvPriority = _SwDNSResStaticIPv6NameSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1, 4),
    _SwDNSResStaticIPv6NameSrvPriority_Type()
)
swDNSResStaticIPv6NameSrvPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvPriority.setStatus("current")
_SwDNSResStaticIPv6NameSrvRowStatus_Type = RowStatus
_SwDNSResStaticIPv6NameSrvRowStatus_Object = MibTableColumn
swDNSResStaticIPv6NameSrvRowStatus = _SwDNSResStaticIPv6NameSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 3, 3, 1, 100),
    _SwDNSResStaticIPv6NameSrvRowStatus_Type()
)
swDNSResStaticIPv6NameSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticIPv6NameSrvRowStatus.setStatus("current")
_SwDNSResHost_ObjectIdentity = ObjectIdentity
swDNSResHost = _SwDNSResHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4)
)
_SwDNSResStaticHostTable_Object = MibTable
swDNSResStaticHostTable = _SwDNSResStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1)
)
if mibBuilder.loadTexts:
    swDNSResStaticHostTable.setStatus("current")
_SwDNSResStaticHostEntry_Object = MibTableRow
swDNSResStaticHostEntry = _SwDNSResStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1)
)
swDNSResStaticHostEntry.setIndexNames(
    (0, "DNSResolver-MIB", "swDNSResStaticHostIndex"),
)
if mibBuilder.loadTexts:
    swDNSResStaticHostEntry.setStatus("current")
_SwDNSResStaticHostIndex_Type = Integer32
_SwDNSResStaticHostIndex_Object = MibTableColumn
swDNSResStaticHostIndex = _SwDNSResStaticHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 1),
    _SwDNSResStaticHostIndex_Type()
)
swDNSResStaticHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDNSResStaticHostIndex.setStatus("current")
_SwDNSResStaticHostRowStatus_Type = RowStatus
_SwDNSResStaticHostRowStatus_Object = MibTableColumn
swDNSResStaticHostRowStatus = _SwDNSResStaticHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 2),
    _SwDNSResStaticHostRowStatus_Type()
)
swDNSResStaticHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticHostRowStatus.setStatus("current")
_SwDNSResStaticHostName_Type = DnsName
_SwDNSResStaticHostName_Object = MibTableColumn
swDNSResStaticHostName = _SwDNSResStaticHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 3),
    _SwDNSResStaticHostName_Type()
)
swDNSResStaticHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticHostName.setStatus("current")
_SwDNSResStaticHostIPaddr_Type = IpAddress
_SwDNSResStaticHostIPaddr_Object = MibTableColumn
swDNSResStaticHostIPaddr = _SwDNSResStaticHostIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 4),
    _SwDNSResStaticHostIPaddr_Type()
)
swDNSResStaticHostIPaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticHostIPaddr.setStatus("current")
_SwDNSResStaticHostIPv6addr_Type = Ipv6Address
_SwDNSResStaticHostIPv6addr_Object = MibTableColumn
swDNSResStaticHostIPv6addr = _SwDNSResStaticHostIPv6addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 6),
    _SwDNSResStaticHostIPv6addr_Type()
)
swDNSResStaticHostIPv6addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResStaticHostIPv6addr.setStatus("current")


class _SwDNSResStaticHostIPv6IntfName_Type(DisplayString):
    """Custom type swDNSResStaticHostIPv6IntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwDNSResStaticHostIPv6IntfName_Type.__name__ = "DisplayString"
_SwDNSResStaticHostIPv6IntfName_Object = MibTableColumn
swDNSResStaticHostIPv6IntfName = _SwDNSResStaticHostIPv6IntfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 1, 1, 7),
    _SwDNSResStaticHostIPv6IntfName_Type()
)
swDNSResStaticHostIPv6IntfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResStaticHostIPv6IntfName.setStatus("current")
_SwDNSResDynamicHostTable_Object = MibTable
swDNSResDynamicHostTable = _SwDNSResDynamicHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2)
)
if mibBuilder.loadTexts:
    swDNSResDynamicHostTable.setStatus("current")
_SwDNSResDynamicHostEntry_Object = MibTableRow
swDNSResDynamicHostEntry = _SwDNSResDynamicHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1)
)
swDNSResDynamicHostEntry.setIndexNames(
    (0, "DNSResolver-MIB", "swDNSResDynamicHostIndex"),
)
if mibBuilder.loadTexts:
    swDNSResDynamicHostEntry.setStatus("current")
_SwDNSResDynamicHostIndex_Type = Integer32
_SwDNSResDynamicHostIndex_Object = MibTableColumn
swDNSResDynamicHostIndex = _SwDNSResDynamicHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 1),
    _SwDNSResDynamicHostIndex_Type()
)
swDNSResDynamicHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDNSResDynamicHostIndex.setStatus("current")
_SwDNSResDynamicHostName_Type = DnsName
_SwDNSResDynamicHostName_Object = MibTableColumn
swDNSResDynamicHostName = _SwDNSResDynamicHostName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 2),
    _SwDNSResDynamicHostName_Type()
)
swDNSResDynamicHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDNSResDynamicHostName.setStatus("current")
_SwDNSResDynamicHostIPaddr_Type = IpAddress
_SwDNSResDynamicHostIPaddr_Object = MibTableColumn
swDNSResDynamicHostIPaddr = _SwDNSResDynamicHostIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 3),
    _SwDNSResDynamicHostIPaddr_Type()
)
swDNSResDynamicHostIPaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDNSResDynamicHostIPaddr.setStatus("current")
_SwDNSResDynamicHostTTL_Type = DnsTime
_SwDNSResDynamicHostTTL_Object = MibTableColumn
swDNSResDynamicHostTTL = _SwDNSResDynamicHostTTL_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 4),
    _SwDNSResDynamicHostTTL_Type()
)
swDNSResDynamicHostTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDNSResDynamicHostTTL.setStatus("current")


class _SwDNSResDynamicHostClearCtrl_Type(Integer32):
    """Custom type swDNSResDynamicHostClearCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwDNSResDynamicHostClearCtrl_Type.__name__ = "Integer32"
_SwDNSResDynamicHostClearCtrl_Object = MibTableColumn
swDNSResDynamicHostClearCtrl = _SwDNSResDynamicHostClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 5),
    _SwDNSResDynamicHostClearCtrl_Type()
)
swDNSResDynamicHostClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResDynamicHostClearCtrl.setStatus("current")
_SwDNSResDynamicHostIPv6addr_Type = Ipv6Address
_SwDNSResDynamicHostIPv6addr_Object = MibTableColumn
swDNSResDynamicHostIPv6addr = _SwDNSResDynamicHostIPv6addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 7),
    _SwDNSResDynamicHostIPv6addr_Type()
)
swDNSResDynamicHostIPv6addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDNSResDynamicHostIPv6addr.setStatus("current")


class _SwDNSResDynamicHostIPv6IntfName_Type(DisplayString):
    """Custom type swDNSResDynamicHostIPv6IntfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwDNSResDynamicHostIPv6IntfName_Type.__name__ = "DisplayString"
_SwDNSResDynamicHostIPv6IntfName_Object = MibTableColumn
swDNSResDynamicHostIPv6IntfName = _SwDNSResDynamicHostIPv6IntfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 85, 1, 4, 2, 1, 8),
    _SwDNSResDynamicHostIPv6IntfName_Type()
)
swDNSResDynamicHostIPv6IntfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDNSResDynamicHostIPv6IntfName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNSResolver-MIB",
    **{"DnsName": DnsName,
       "DnsTime": DnsTime,
       "swDNSResolverMIB": swDNSResolverMIB,
       "swDNSResolverMIBObjects": swDNSResolverMIBObjects,
       "swDNSResState": swDNSResState,
       "swDNSResNameSrvTimeOut": swDNSResNameSrvTimeOut,
       "swDNSResNameSrv": swDNSResNameSrv,
       "swDNSResStaticNameSrvTable": swDNSResStaticNameSrvTable,
       "swDNSResStaticNameSrvEntry": swDNSResStaticNameSrvEntry,
       "swDNSResStaticNameSrvIndex": swDNSResStaticNameSrvIndex,
       "swDNSResStaticNameSrvRowStatus": swDNSResStaticNameSrvRowStatus,
       "swDNSResStaticNameSrvIPaddr": swDNSResStaticNameSrvIPaddr,
       "swDNSResStaticNameSrvPriority": swDNSResStaticNameSrvPriority,
       "swDNSResDynamicNameSrvTable": swDNSResDynamicNameSrvTable,
       "swDNSResDynamicNameSrvEntry": swDNSResDynamicNameSrvEntry,
       "swDNSResDynamicNameSrvIndex": swDNSResDynamicNameSrvIndex,
       "swDNSResDynamicNameSrvIPaddr": swDNSResDynamicNameSrvIPaddr,
       "swDNSResDynamicNameSrvPriority": swDNSResDynamicNameSrvPriority,
       "swDNSResStaticIPv6NameSrvTable": swDNSResStaticIPv6NameSrvTable,
       "swDNSResStaticIPv6NameSrvEntry": swDNSResStaticIPv6NameSrvEntry,
       "swDNSResStaticIPv6NameSrvIndex": swDNSResStaticIPv6NameSrvIndex,
       "swDNSResStaticIPv6NameSrvaddr": swDNSResStaticIPv6NameSrvaddr,
       "swDNSResStaticIPv6NameSrvIntfName": swDNSResStaticIPv6NameSrvIntfName,
       "swDNSResStaticIPv6NameSrvPriority": swDNSResStaticIPv6NameSrvPriority,
       "swDNSResStaticIPv6NameSrvRowStatus": swDNSResStaticIPv6NameSrvRowStatus,
       "swDNSResHost": swDNSResHost,
       "swDNSResStaticHostTable": swDNSResStaticHostTable,
       "swDNSResStaticHostEntry": swDNSResStaticHostEntry,
       "swDNSResStaticHostIndex": swDNSResStaticHostIndex,
       "swDNSResStaticHostRowStatus": swDNSResStaticHostRowStatus,
       "swDNSResStaticHostName": swDNSResStaticHostName,
       "swDNSResStaticHostIPaddr": swDNSResStaticHostIPaddr,
       "swDNSResStaticHostIPv6addr": swDNSResStaticHostIPv6addr,
       "swDNSResStaticHostIPv6IntfName": swDNSResStaticHostIPv6IntfName,
       "swDNSResDynamicHostTable": swDNSResDynamicHostTable,
       "swDNSResDynamicHostEntry": swDNSResDynamicHostEntry,
       "swDNSResDynamicHostIndex": swDNSResDynamicHostIndex,
       "swDNSResDynamicHostName": swDNSResDynamicHostName,
       "swDNSResDynamicHostIPaddr": swDNSResDynamicHostIPaddr,
       "swDNSResDynamicHostTTL": swDNSResDynamicHostTTL,
       "swDNSResDynamicHostClearCtrl": swDNSResDynamicHostClearCtrl,
       "swDNSResDynamicHostIPv6addr": swDNSResDynamicHostIPv6addr,
       "swDNSResDynamicHostIPv6IntfName": swDNSResDynamicHostIPv6IntfName}
)
