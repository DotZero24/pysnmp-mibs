# SNMP MIB module (MAIPU-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:14 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dnsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnsGlobal_ObjectIdentity = ObjectIdentity
dnsGlobal = _DnsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 1)
)


class _DnsDomainName_Type(DisplayString):
    """Custom type dnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsDomainName_Type.__name__ = "DisplayString"
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 1, 1),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")


class _DnsDomainOrder_Type(Integer32):
    """Custom type dnsDomainOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localfirst", 1),
          ("dnsfirst", 2),
          ("dnsonly", 3))
    )


_DnsDomainOrder_Type.__name__ = "Integer32"
_DnsDomainOrder_Object = MibScalar
dnsDomainOrder = _DnsDomainOrder_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 1, 2),
    _DnsDomainOrder_Type()
)
dnsDomainOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainOrder.setStatus("current")
_DnsNameServerTable_Object = MibTable
dnsNameServerTable = _DnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 2)
)
if mibBuilder.loadTexts:
    dnsNameServerTable.setStatus("current")
_DnsNameServerEntry_Object = MibTableRow
dnsNameServerEntry = _DnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 2, 1)
)
dnsNameServerEntry.setIndexNames(
    (0, "MAIPU-DNS-MIB", "dnsNameServerIPAddress"),
)
if mibBuilder.loadTexts:
    dnsNameServerEntry.setStatus("current")
_DnsNameServerIPAddress_Type = IpAddress
_DnsNameServerIPAddress_Object = MibTableColumn
dnsNameServerIPAddress = _DnsNameServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 2, 1, 1),
    _DnsNameServerIPAddress_Type()
)
dnsNameServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsNameServerIPAddress.setStatus("current")
_DnsNameServerRowStatus_Type = RowStatus
_DnsNameServerRowStatus_Object = MibTableColumn
dnsNameServerRowStatus = _DnsNameServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 2, 1, 2),
    _DnsNameServerRowStatus_Type()
)
dnsNameServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsNameServerRowStatus.setStatus("current")
_DnsHostNameTable_Object = MibTable
dnsHostNameTable = _DnsHostNameTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3)
)
if mibBuilder.loadTexts:
    dnsHostNameTable.setStatus("current")
_DnsHostNameEntry_Object = MibTableRow
dnsHostNameEntry = _DnsHostNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3, 1)
)
dnsHostNameEntry.setIndexNames(
    (0, "MAIPU-DNS-MIB", "dnsHostIPAddress"),
    (0, "MAIPU-DNS-MIB", "dnsHostName"),
)
if mibBuilder.loadTexts:
    dnsHostNameEntry.setStatus("current")
_DnsHostIPAddress_Type = IpAddress
_DnsHostIPAddress_Object = MibTableColumn
dnsHostIPAddress = _DnsHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3, 1, 1),
    _DnsHostIPAddress_Type()
)
dnsHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostIPAddress.setStatus("current")


class _DnsHostName_Type(DisplayString):
    """Custom type dnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DnsHostName_Type.__name__ = "DisplayString"
_DnsHostName_Object = MibTableColumn
dnsHostName = _DnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3, 1, 2),
    _DnsHostName_Type()
)
dnsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostName.setStatus("current")
_DnsHostAlias_Type = TruthValue
_DnsHostAlias_Object = MibTableColumn
dnsHostAlias = _DnsHostAlias_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3, 1, 3),
    _DnsHostAlias_Type()
)
dnsHostAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostAlias.setStatus("current")
_DnsHostRawStatus_Type = RowStatus
_DnsHostRawStatus_Object = MibTableColumn
dnsHostRawStatus = _DnsHostRawStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 3, 1, 4),
    _DnsHostRawStatus_Type()
)
dnsHostRawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsHostRawStatus.setStatus("current")
_DnsDomainNameTable_Object = MibTable
dnsDomainNameTable = _DnsDomainNameTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 4)
)
if mibBuilder.loadTexts:
    dnsDomainNameTable.setStatus("current")
_DnsDomainNameEntry_Object = MibTableRow
dnsDomainNameEntry = _DnsDomainNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 4, 1)
)
dnsDomainNameEntry.setIndexNames(
    (0, "MAIPU-DNS-MIB", "dnsDomainTblNameVrf"),
)
if mibBuilder.loadTexts:
    dnsDomainNameEntry.setStatus("current")


class _DnsDomainTblName_Type(DisplayString):
    """Custom type dnsDomainTblName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsDomainTblName_Type.__name__ = "DisplayString"
_DnsDomainTblName_Object = MibTableColumn
dnsDomainTblName = _DnsDomainTblName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 4, 1, 1),
    _DnsDomainTblName_Type()
)
dnsDomainTblName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainTblName.setStatus("current")


class _DnsDomainTblNameVrf_Type(DisplayString):
    """Custom type dnsDomainTblNameVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DnsDomainTblNameVrf_Type.__name__ = "DisplayString"
_DnsDomainTblNameVrf_Object = MibTableColumn
dnsDomainTblNameVrf = _DnsDomainTblNameVrf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 4, 1, 2),
    _DnsDomainTblNameVrf_Type()
)
dnsDomainTblNameVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsDomainTblNameVrf.setStatus("current")
_DnsNameServerXTable_Object = MibTable
dnsNameServerXTable = _DnsNameServerXTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 5)
)
if mibBuilder.loadTexts:
    dnsNameServerXTable.setStatus("current")
_DnsNameServerXEntry_Object = MibTableRow
dnsNameServerXEntry = _DnsNameServerXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 5, 1)
)
dnsNameServerXEntry.setIndexNames(
    (0, "MAIPU-DNS-MIB", "dnsNameServerXIPAddress"),
    (0, "MAIPU-DNS-MIB", "dnsNameServerXVrf"),
)
if mibBuilder.loadTexts:
    dnsNameServerXEntry.setStatus("current")
_DnsNameServerXIPAddress_Type = IpAddress
_DnsNameServerXIPAddress_Object = MibTableColumn
dnsNameServerXIPAddress = _DnsNameServerXIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 5, 1, 1),
    _DnsNameServerXIPAddress_Type()
)
dnsNameServerXIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsNameServerXIPAddress.setStatus("current")


class _DnsNameServerXVrf_Type(DisplayString):
    """Custom type dnsNameServerXVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DnsNameServerXVrf_Type.__name__ = "DisplayString"
_DnsNameServerXVrf_Object = MibTableColumn
dnsNameServerXVrf = _DnsNameServerXVrf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 5, 1, 2),
    _DnsNameServerXVrf_Type()
)
dnsNameServerXVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsNameServerXVrf.setStatus("current")
_DnsNameServerXRowStatus_Type = RowStatus
_DnsNameServerXRowStatus_Object = MibTableColumn
dnsNameServerXRowStatus = _DnsNameServerXRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 5, 1, 3),
    _DnsNameServerXRowStatus_Type()
)
dnsNameServerXRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsNameServerXRowStatus.setStatus("current")
_DnsHostNameXTable_Object = MibTable
dnsHostNameXTable = _DnsHostNameXTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6)
)
if mibBuilder.loadTexts:
    dnsHostNameXTable.setStatus("current")
_DnsHostNameXEntry_Object = MibTableRow
dnsHostNameXEntry = _DnsHostNameXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1)
)
dnsHostNameXEntry.setIndexNames(
    (0, "MAIPU-DNS-MIB", "dnsHostXIPAddress"),
    (0, "MAIPU-DNS-MIB", "dnsHostXName"),
    (0, "MAIPU-DNS-MIB", "dnsHostXVrf"),
)
if mibBuilder.loadTexts:
    dnsHostNameXEntry.setStatus("current")
_DnsHostXIPAddress_Type = IpAddress
_DnsHostXIPAddress_Object = MibTableColumn
dnsHostXIPAddress = _DnsHostXIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1, 1),
    _DnsHostXIPAddress_Type()
)
dnsHostXIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostXIPAddress.setStatus("current")


class _DnsHostXName_Type(DisplayString):
    """Custom type dnsHostXName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DnsHostXName_Type.__name__ = "DisplayString"
_DnsHostXName_Object = MibTableColumn
dnsHostXName = _DnsHostXName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1, 2),
    _DnsHostXName_Type()
)
dnsHostXName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostXName.setStatus("current")


class _DnsHostXVrf_Type(DisplayString):
    """Custom type dnsHostXVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DnsHostXVrf_Type.__name__ = "DisplayString"
_DnsHostXVrf_Object = MibTableColumn
dnsHostXVrf = _DnsHostXVrf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1, 3),
    _DnsHostXVrf_Type()
)
dnsHostXVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostXVrf.setStatus("current")
_DnsHostXAlias_Type = TruthValue
_DnsHostXAlias_Object = MibTableColumn
dnsHostXAlias = _DnsHostXAlias_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1, 4),
    _DnsHostXAlias_Type()
)
dnsHostXAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsHostXAlias.setStatus("current")
_DnsHostXRawStatus_Type = RowStatus
_DnsHostXRawStatus_Object = MibTableColumn
dnsHostXRawStatus = _DnsHostXRawStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 109, 6, 1, 5),
    _DnsHostXRawStatus_Type()
)
dnsHostXRawStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsHostXRawStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-DNS-MIB",
    **{"dnsMib": dnsMib,
       "dnsGlobal": dnsGlobal,
       "dnsDomainName": dnsDomainName,
       "dnsDomainOrder": dnsDomainOrder,
       "dnsNameServerTable": dnsNameServerTable,
       "dnsNameServerEntry": dnsNameServerEntry,
       "dnsNameServerIPAddress": dnsNameServerIPAddress,
       "dnsNameServerRowStatus": dnsNameServerRowStatus,
       "dnsHostNameTable": dnsHostNameTable,
       "dnsHostNameEntry": dnsHostNameEntry,
       "dnsHostIPAddress": dnsHostIPAddress,
       "dnsHostName": dnsHostName,
       "dnsHostAlias": dnsHostAlias,
       "dnsHostRawStatus": dnsHostRawStatus,
       "dnsDomainNameTable": dnsDomainNameTable,
       "dnsDomainNameEntry": dnsDomainNameEntry,
       "dnsDomainTblName": dnsDomainTblName,
       "dnsDomainTblNameVrf": dnsDomainTblNameVrf,
       "dnsNameServerXTable": dnsNameServerXTable,
       "dnsNameServerXEntry": dnsNameServerXEntry,
       "dnsNameServerXIPAddress": dnsNameServerXIPAddress,
       "dnsNameServerXVrf": dnsNameServerXVrf,
       "dnsNameServerXRowStatus": dnsNameServerXRowStatus,
       "dnsHostNameXTable": dnsHostNameXTable,
       "dnsHostNameXEntry": dnsHostNameXEntry,
       "dnsHostXIPAddress": dnsHostXIPAddress,
       "dnsHostXName": dnsHostXName,
       "dnsHostXVrf": dnsHostXVrf,
       "dnsHostXAlias": dnsHostXAlias,
       "dnsHostXRawStatus": dnsHostXRawStatus}
)
