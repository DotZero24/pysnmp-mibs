# SNMP MIB module (ARRIS-ROUTER-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-ROUTER-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:10 2025
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

(arrisProdIdRouter,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdRouter")

(DscpOrAny,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "DscpOrAny")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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

arrisRouterMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1)
)
if mibBuilder.loadTexts:
    arrisRouterMib.setRevisions(
        ("2015-07-15 00:00",
         "2015-07-08 00:00",
         "2015-06-26 00:00",
         "2015-06-04 00:00",
         "2015-05-26 00:00",
         "2015-05-25 00:00",
         "2015-05-15 00:00",
         "2015-05-13 00:00",
         "2015-04-28 00:00",
         "2015-04-27 00:00",
         "2015-04-24 00:00",
         "2015-04-10 00:00",
         "2015-04-10 00:00",
         "2015-04-01 00:00",
         "2015-03-31 00:00",
         "2015-01-04 00:00",
         "2015-03-26 00:00",
         "2015-02-27 00:00",
         "2015-01-04 00:00",
         "2015-02-17 00:00",
         "2015-02-12 00:00",
         "2015-02-06 00:00",
         "2015-01-30 00:00",
         "2015-02-10 00:00",
         "2015-01-15 00:00",
         "2015-01-08 00:00",
         "2015-01-04 00:00",
         "2014-12-12 00:00",
         "2014-12-24 00:00",
         "2014-12-23 00:00",
         "2014-12-09 00:00",
         "2014-12-12 00:00",
         "2014-12-11 00:00",
         "2014-12-09 00:00",
         "2014-12-09 00:00",
         "2014-11-27 00:00",
         "2014-11-25 00:00",
         "2014-11-27 00:00",
         "2014-11-27 00:00",
         "2014-11-26 00:00",
         "2014-11-26 00:00",
         "2014-11-21 00:00",
         "2014-11-20 00:00",
         "2014-11-14 00:00",
         "2014-11-13 00:00",
         "2014-11-01 00:00",
         "2014-10-27 00:00",
         "2014-10-23 00:00",
         "2014-10-01 00:00",
         "2014-10-17 00:00",
         "2014-10-14 00:00",
         "2014-10-13 00:00",
         "2014-10-11 00:00",
         "2014-09-15 00:00",
         "2014-07-11 00:00",
         "2014-06-16 00:00",
         "2014-06-04 00:00",
         "2014-05-15 00:00",
         "2014-04-28 00:00",
         "2014-03-27 00:00",
         "2014-03-25 00:00",
         "2014-03-19 00:00",
         "2014-03-06 00:00",
         "2014-02-24 00:00",
         "2014-01-28 00:00",
         "2014-01-27 00:00",
         "2014-01-16 00:00",
         "2014-01-10 00:00",
         "2013-11-28 00:00",
         "2013-11-25 00:00",
         "2013-11-20 00:00",
         "2013-10-17 00:00",
         "2013-10-15 00:00",
         "2013-09-19 00:00",
         "2013-09-04 00:00",
         "2013-08-26 00:00",
         "2013-08-20 00:00",
         "2013-08-13 00:00",
         "2013-08-13 00:00",
         "2013-08-07 00:00",
         "2013-08-02 00:00",
         "2013-07-30 00:00",
         "2013-07-26 00:00",
         "2013-07-24 00:00",
         "2013-07-22 00:01",
         "2013-07-17 00:01",
         "2013-07-17 00:00",
         "2013-07-16 00:00",
         "2013-06-26 00:00",
         "2013-06-20 00:00",
         "2013-06-05 00:00",
         "2013-06-03 00:00",
         "2013-05-31 00:00",
         "2013-05-29 00:00",
         "2013-05-22 00:00",
         "2013-01-31 00:00",
         "2013-05-09 00:00",
         "2013-04-27 00:00",
         "2013-04-24 00:00",
         "2013-04-17 00:00",
         "2013-04-15 00:00",
         "2013-04-03 00:00",
         "2013-04-08 00:00",
         "2013-03-19 00:00",
         "2013-03-29 00:00",
         "2013-03-15 00:00",
         "2013-03-13 00:00",
         "2013-03-07 00:00",
         "2013-03-06 00:00",
         "2013-02-08 00:00",
         "2013-01-31 00:00",
         "2013-01-10 00:00",
         "2012-12-27 00:00",
         "2012-12-19 00:00",
         "2012-12-17 00:00",
         "2012-12-11 00:00",
         "2012-12-04 00:00",
         "2012-11-02 00:00",
         "2012-11-01 00:00",
         "2012-10-31 00:00",
         "2012-10-26 00:00",
         "2012-10-26 00:00",
         "2012-10-15 00:00",
         "2012-10-15 00:00",
         "2012-08-29 00:00",
         "2012-06-12 00:00",
         "2012-05-30 00:00",
         "2012-05-22 00:00",
         "2012-05-21 00:00",
         "2012-04-02 00:00",
         "2012-03-21 00:00",
         "2012-02-15 00:00",
         "2012-02-15 00:00",
         "2011-12-09 00:00",
         "2011-10-06 00:00",
         "2011-09-06 00:00",
         "2011-08-30 00:00",
         "2011-08-18 00:00",
         "2011-05-05 00:00",
         "2011-04-28 00:00",
         "2011-02-09 00:00",
         "2011-02-04 00:00",
         "2011-01-18 00:00",
         "2011-01-10 00:00",
         "2011-01-09 00:00",
         "2010-12-22 00:00",
         "2010-12-17 00:00",
         "2010-12-15 00:00",
         "2010-12-06 00:00",
         "2010-11-29 00:00",
         "2010-11-26 00:00",
         "2010-11-23 00:00",
         "2010-11-08 00:00",
         "2010-10-26 00:00",
         "2010-10-25 00:00",
         "2010-10-21 00:00",
         "2010-10-20 00:00",
         "2010-10-15 00:00",
         "2010-10-12 00:00",
         "2010-09-30 00:00",
         "2010-09-24 00:00",
         "2010-09-21 00:00",
         "2010-09-16 00:00",
         "2010-09-01 00:00",
         "2010-08-17 00:00",
         "2010-07-23 00:00",
         "2010-07-22 00:00",
         "2010-07-14 00:00",
         "2010-07-12 00:00",
         "2010-06-30 00:00",
         "2010-06-28 00:00",
         "2010-06-20 00:00",
         "2010-06-17 00:00",
         "2010-05-27 00:00",
         "2010-05-26 00:00",
         "2010-05-11 00:00",
         "2010-05-07 00:00",
         "2010-05-03 00:00",
         "2010-04-29 00:00",
         "2010-04-27 00:00",
         "2010-04-25 00:00",
         "2010-04-22 00:00",
         "2010-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisRouterMibObjects_ObjectIdentity = ObjectIdentity
arrisRouterMibObjects = _ArrisRouterMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1)
)
_ArrisRouterWanConfig_ObjectIdentity = ObjectIdentity
arrisRouterWanConfig = _ArrisRouterWanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1)
)


class _ArrisRouterWanConnType_Type(Integer32):
    """Custom type arrisRouterWanConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dynamic", 1),
          ("static", 2),
          ("l2tpStatic", 5),
          ("l2tpDynamic", 6))
    )


_ArrisRouterWanConnType_Type.__name__ = "Integer32"
_ArrisRouterWanConnType_Object = MibScalar
arrisRouterWanConnType = _ArrisRouterWanConnType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 1),
    _ArrisRouterWanConnType_Type()
)
arrisRouterWanConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanConnType.setStatus("current")


class _ArrisRouterWanConnHostName_Type(DisplayString):
    """Custom type arrisRouterWanConnHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterWanConnHostName_Type.__name__ = "DisplayString"
_ArrisRouterWanConnHostName_Object = MibScalar
arrisRouterWanConnHostName = _ArrisRouterWanConnHostName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 2),
    _ArrisRouterWanConnHostName_Type()
)
arrisRouterWanConnHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanConnHostName.setStatus("current")


class _ArrisRouterWanConnDomainName_Type(DisplayString):
    """Custom type arrisRouterWanConnDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterWanConnDomainName_Type.__name__ = "DisplayString"
_ArrisRouterWanConnDomainName_Object = MibScalar
arrisRouterWanConnDomainName = _ArrisRouterWanConnDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 3),
    _ArrisRouterWanConnDomainName_Type()
)
arrisRouterWanConnDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanConnDomainName.setStatus("current")


class _ArrisRouterWanMTUSize_Type(Unsigned32):
    """Custom type arrisRouterWanMTUSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_ArrisRouterWanMTUSize_Type.__name__ = "Unsigned32"
_ArrisRouterWanMTUSize_Object = MibScalar
arrisRouterWanMTUSize = _ArrisRouterWanMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 4),
    _ArrisRouterWanMTUSize_Type()
)
arrisRouterWanMTUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanMTUSize.setStatus("current")
_ArrisRouterWanCurrentTable_Object = MibTable
arrisRouterWanCurrentTable = _ArrisRouterWanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    arrisRouterWanCurrentTable.setStatus("current")
_ArrisRouterWanCurrentEntry_Object = MibTableRow
arrisRouterWanCurrentEntry = _ArrisRouterWanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1)
)
arrisRouterWanCurrentEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWanCurrentIPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWanCurrentEntry.setStatus("current")
_ArrisRouterWanCurrentIPIndex_Type = Unsigned32
_ArrisRouterWanCurrentIPIndex_Object = MibTableColumn
arrisRouterWanCurrentIPIndex = _ArrisRouterWanCurrentIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 1),
    _ArrisRouterWanCurrentIPIndex_Type()
)
arrisRouterWanCurrentIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentIPIndex.setStatus("current")
_ArrisRouterWanCurrentIPAddrType_Type = InetAddressType
_ArrisRouterWanCurrentIPAddrType_Object = MibTableColumn
arrisRouterWanCurrentIPAddrType = _ArrisRouterWanCurrentIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 2),
    _ArrisRouterWanCurrentIPAddrType_Type()
)
arrisRouterWanCurrentIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentIPAddrType.setStatus("current")
_ArrisRouterWanCurrentIPAddr_Type = InetAddress
_ArrisRouterWanCurrentIPAddr_Object = MibTableColumn
arrisRouterWanCurrentIPAddr = _ArrisRouterWanCurrentIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 3),
    _ArrisRouterWanCurrentIPAddr_Type()
)
arrisRouterWanCurrentIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentIPAddr.setStatus("current")
_ArrisRouterWanCurrentPrefix_Type = InetAddressPrefixLength
_ArrisRouterWanCurrentPrefix_Object = MibTableColumn
arrisRouterWanCurrentPrefix = _ArrisRouterWanCurrentPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 4),
    _ArrisRouterWanCurrentPrefix_Type()
)
arrisRouterWanCurrentPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentPrefix.setStatus("current")
_ArrisRouterWanCurrentGWType_Type = InetAddressType
_ArrisRouterWanCurrentGWType_Object = MibTableColumn
arrisRouterWanCurrentGWType = _ArrisRouterWanCurrentGWType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 5),
    _ArrisRouterWanCurrentGWType_Type()
)
arrisRouterWanCurrentGWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentGWType.setStatus("current")
_ArrisRouterWanCurrentGW_Type = InetAddress
_ArrisRouterWanCurrentGW_Object = MibTableColumn
arrisRouterWanCurrentGW = _ArrisRouterWanCurrentGW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 6),
    _ArrisRouterWanCurrentGW_Type()
)
arrisRouterWanCurrentGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentGW.setStatus("current")


class _ArrisRouterWanCurrentIPType_Type(Integer32):
    """Custom type arrisRouterWanCurrentIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_ArrisRouterWanCurrentIPType_Type.__name__ = "Integer32"
_ArrisRouterWanCurrentIPType_Object = MibTableColumn
arrisRouterWanCurrentIPType = _ArrisRouterWanCurrentIPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 7),
    _ArrisRouterWanCurrentIPType_Type()
)
arrisRouterWanCurrentIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentIPType.setStatus("current")
_ArrisRouterWanCurrentNetMask_Type = InetAddress
_ArrisRouterWanCurrentNetMask_Object = MibTableColumn
arrisRouterWanCurrentNetMask = _ArrisRouterWanCurrentNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 8),
    _ArrisRouterWanCurrentNetMask_Type()
)
arrisRouterWanCurrentNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentNetMask.setStatus("current")
_ArrisRouterWanCurrentPrefixDelegationV6_Type = InetAddressIPv6
_ArrisRouterWanCurrentPrefixDelegationV6_Object = MibTableColumn
arrisRouterWanCurrentPrefixDelegationV6 = _ArrisRouterWanCurrentPrefixDelegationV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 9),
    _ArrisRouterWanCurrentPrefixDelegationV6_Type()
)
arrisRouterWanCurrentPrefixDelegationV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentPrefixDelegationV6.setStatus("current")
_ArrisRouterWanCurrentPrefixDelegationV6Len_Type = InetAddressPrefixLength
_ArrisRouterWanCurrentPrefixDelegationV6Len_Object = MibTableColumn
arrisRouterWanCurrentPrefixDelegationV6Len = _ArrisRouterWanCurrentPrefixDelegationV6Len_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 10),
    _ArrisRouterWanCurrentPrefixDelegationV6Len_Type()
)
arrisRouterWanCurrentPrefixDelegationV6Len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentPrefixDelegationV6Len.setStatus("current")
_ArrisRouterWanCurrentPreferredLifetimeV6_Type = Integer32
_ArrisRouterWanCurrentPreferredLifetimeV6_Object = MibTableColumn
arrisRouterWanCurrentPreferredLifetimeV6 = _ArrisRouterWanCurrentPreferredLifetimeV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 11),
    _ArrisRouterWanCurrentPreferredLifetimeV6_Type()
)
arrisRouterWanCurrentPreferredLifetimeV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentPreferredLifetimeV6.setStatus("current")
_ArrisRouterWanCurrentValidLifetimeV6_Type = Integer32
_ArrisRouterWanCurrentValidLifetimeV6_Object = MibTableColumn
arrisRouterWanCurrentValidLifetimeV6 = _ArrisRouterWanCurrentValidLifetimeV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 7, 1, 12),
    _ArrisRouterWanCurrentValidLifetimeV6_Type()
)
arrisRouterWanCurrentValidLifetimeV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentValidLifetimeV6.setStatus("current")


class _ArrisRouterWanStaticFreeIdx_Type(Unsigned32):
    """Custom type arrisRouterWanStaticFreeIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ArrisRouterWanStaticFreeIdx_Type.__name__ = "Unsigned32"
_ArrisRouterWanStaticFreeIdx_Object = MibScalar
arrisRouterWanStaticFreeIdx = _ArrisRouterWanStaticFreeIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 8),
    _ArrisRouterWanStaticFreeIdx_Type()
)
arrisRouterWanStaticFreeIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanStaticFreeIdx.setStatus("current")
_ArrisRouterWanStaticTable_Object = MibTable
arrisRouterWanStaticTable = _ArrisRouterWanStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    arrisRouterWanStaticTable.setStatus("current")
_ArrisRouterWanStaticEntry_Object = MibTableRow
arrisRouterWanStaticEntry = _ArrisRouterWanStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1)
)
arrisRouterWanStaticEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWanStaticIPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWanStaticEntry.setStatus("current")
_ArrisRouterWanStaticIPIndex_Type = Unsigned32
_ArrisRouterWanStaticIPIndex_Object = MibTableColumn
arrisRouterWanStaticIPIndex = _ArrisRouterWanStaticIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 1),
    _ArrisRouterWanStaticIPIndex_Type()
)
arrisRouterWanStaticIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWanStaticIPIndex.setStatus("current")
_ArrisRouterWanStaticIPAddrType_Type = InetAddressType
_ArrisRouterWanStaticIPAddrType_Object = MibTableColumn
arrisRouterWanStaticIPAddrType = _ArrisRouterWanStaticIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 2),
    _ArrisRouterWanStaticIPAddrType_Type()
)
arrisRouterWanStaticIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticIPAddrType.setStatus("current")
_ArrisRouterWanStaticIPAddr_Type = InetAddress
_ArrisRouterWanStaticIPAddr_Object = MibTableColumn
arrisRouterWanStaticIPAddr = _ArrisRouterWanStaticIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 3),
    _ArrisRouterWanStaticIPAddr_Type()
)
arrisRouterWanStaticIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticIPAddr.setStatus("current")
_ArrisRouterWanStaticPrefix_Type = InetAddressPrefixLength
_ArrisRouterWanStaticPrefix_Object = MibTableColumn
arrisRouterWanStaticPrefix = _ArrisRouterWanStaticPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 4),
    _ArrisRouterWanStaticPrefix_Type()
)
arrisRouterWanStaticPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticPrefix.setStatus("current")
_ArrisRouterWanStaticGatewayType_Type = InetAddressType
_ArrisRouterWanStaticGatewayType_Object = MibTableColumn
arrisRouterWanStaticGatewayType = _ArrisRouterWanStaticGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 5),
    _ArrisRouterWanStaticGatewayType_Type()
)
arrisRouterWanStaticGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticGatewayType.setStatus("current")
_ArrisRouterWanStaticGateway_Type = InetAddress
_ArrisRouterWanStaticGateway_Object = MibTableColumn
arrisRouterWanStaticGateway = _ArrisRouterWanStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 6),
    _ArrisRouterWanStaticGateway_Type()
)
arrisRouterWanStaticGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticGateway.setStatus("current")
_ArrisRouterWanStaticRowStatus_Type = RowStatus
_ArrisRouterWanStaticRowStatus_Object = MibTableColumn
arrisRouterWanStaticRowStatus = _ArrisRouterWanStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 7),
    _ArrisRouterWanStaticRowStatus_Type()
)
arrisRouterWanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticRowStatus.setStatus("current")
_ArrisRouterWanDelegatedPrefixLength_Type = InetAddressPrefixLength
_ArrisRouterWanDelegatedPrefixLength_Object = MibTableColumn
arrisRouterWanDelegatedPrefixLength = _ArrisRouterWanDelegatedPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 8),
    _ArrisRouterWanDelegatedPrefixLength_Type()
)
arrisRouterWanDelegatedPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanDelegatedPrefixLength.setStatus("current")
_ArrisRouterWanDelegatedPrefix_Type = InetAddressIPv6
_ArrisRouterWanDelegatedPrefix_Object = MibTableColumn
arrisRouterWanDelegatedPrefix = _ArrisRouterWanDelegatedPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 9, 1, 9),
    _ArrisRouterWanDelegatedPrefix_Type()
)
arrisRouterWanDelegatedPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanDelegatedPrefix.setStatus("current")
_ArrisRouterWanTunnelObjects_ObjectIdentity = ObjectIdentity
arrisRouterWanTunnelObjects = _ArrisRouterWanTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10)
)


class _ArrisRouterWanUserName_Type(DisplayString):
    """Custom type arrisRouterWanUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWanUserName_Type.__name__ = "DisplayString"
_ArrisRouterWanUserName_Object = MibScalar
arrisRouterWanUserName = _ArrisRouterWanUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 1),
    _ArrisRouterWanUserName_Type()
)
arrisRouterWanUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanUserName.setStatus("current")


class _ArrisRouterWanPassword_Type(DisplayString):
    """Custom type arrisRouterWanPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWanPassword_Type.__name__ = "DisplayString"
_ArrisRouterWanPassword_Object = MibScalar
arrisRouterWanPassword = _ArrisRouterWanPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 2),
    _ArrisRouterWanPassword_Type()
)
arrisRouterWanPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanPassword.setStatus("current")
_ArrisRouterWanEnableIdleTimeout_Type = TruthValue
_ArrisRouterWanEnableIdleTimeout_Object = MibScalar
arrisRouterWanEnableIdleTimeout = _ArrisRouterWanEnableIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 3),
    _ArrisRouterWanEnableIdleTimeout_Type()
)
arrisRouterWanEnableIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanEnableIdleTimeout.setStatus("current")


class _ArrisRouterWanIdleTimeout_Type(Unsigned32):
    """Custom type arrisRouterWanIdleTimeout based on Unsigned32"""
    defaultValue = 300


_ArrisRouterWanIdleTimeout_Type.__name__ = "Unsigned32"
_ArrisRouterWanIdleTimeout_Object = MibScalar
arrisRouterWanIdleTimeout = _ArrisRouterWanIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 4),
    _ArrisRouterWanIdleTimeout_Type()
)
arrisRouterWanIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWanIdleTimeout.setUnits("seconds")
_ArrisRouterWanTunnelAddrType_Type = InetAddressType
_ArrisRouterWanTunnelAddrType_Object = MibScalar
arrisRouterWanTunnelAddrType = _ArrisRouterWanTunnelAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 5),
    _ArrisRouterWanTunnelAddrType_Type()
)
arrisRouterWanTunnelAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanTunnelAddrType.setStatus("current")
_ArrisRouterWanTunnelAddr_Type = InetAddress
_ArrisRouterWanTunnelAddr_Object = MibScalar
arrisRouterWanTunnelAddr = _ArrisRouterWanTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 6),
    _ArrisRouterWanTunnelAddr_Type()
)
arrisRouterWanTunnelAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanTunnelAddr.setStatus("current")


class _ArrisRouterWanTunnelHostName_Type(DisplayString):
    """Custom type arrisRouterWanTunnelHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterWanTunnelHostName_Type.__name__ = "DisplayString"
_ArrisRouterWanTunnelHostName_Object = MibScalar
arrisRouterWanTunnelHostName = _ArrisRouterWanTunnelHostName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 7),
    _ArrisRouterWanTunnelHostName_Type()
)
arrisRouterWanTunnelHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanTunnelHostName.setStatus("current")
_ArrisRouterWanEnableKeepAlive_Type = TruthValue
_ArrisRouterWanEnableKeepAlive_Object = MibScalar
arrisRouterWanEnableKeepAlive = _ArrisRouterWanEnableKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 8),
    _ArrisRouterWanEnableKeepAlive_Type()
)
arrisRouterWanEnableKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanEnableKeepAlive.setStatus("current")


class _ArrisRouterWanKeepAliveTimeout_Type(Unsigned32):
    """Custom type arrisRouterWanKeepAliveTimeout based on Unsigned32"""
    defaultValue = 30


_ArrisRouterWanKeepAliveTimeout_Type.__name__ = "Unsigned32"
_ArrisRouterWanKeepAliveTimeout_Object = MibScalar
arrisRouterWanKeepAliveTimeout = _ArrisRouterWanKeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 10, 9),
    _ArrisRouterWanKeepAliveTimeout_Type()
)
arrisRouterWanKeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanKeepAliveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWanKeepAliveTimeout.setUnits("seconds")
_ArrisRouterWanDNSObjects_ObjectIdentity = ObjectIdentity
arrisRouterWanDNSObjects = _ArrisRouterWanDNSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11)
)
_ArrisRouterWanUseAutoDNS_Type = TruthValue
_ArrisRouterWanUseAutoDNS_Object = MibScalar
arrisRouterWanUseAutoDNS = _ArrisRouterWanUseAutoDNS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 1),
    _ArrisRouterWanUseAutoDNS_Type()
)
arrisRouterWanUseAutoDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanUseAutoDNS.setStatus("current")
_ArrisRouterWanCurrentDNSTable_Object = MibTable
arrisRouterWanCurrentDNSTable = _ArrisRouterWanCurrentDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    arrisRouterWanCurrentDNSTable.setStatus("current")
_ArrisRouterWanCurrentDNSEntry_Object = MibTableRow
arrisRouterWanCurrentDNSEntry = _ArrisRouterWanCurrentDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 2, 1)
)
arrisRouterWanCurrentDNSEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWanCurrentDNSIPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWanCurrentDNSEntry.setStatus("current")


class _ArrisRouterWanCurrentDNSIPIndex_Type(Unsigned32):
    """Custom type arrisRouterWanCurrentDNSIPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ArrisRouterWanCurrentDNSIPIndex_Type.__name__ = "Unsigned32"
_ArrisRouterWanCurrentDNSIPIndex_Object = MibTableColumn
arrisRouterWanCurrentDNSIPIndex = _ArrisRouterWanCurrentDNSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 2, 1, 1),
    _ArrisRouterWanCurrentDNSIPIndex_Type()
)
arrisRouterWanCurrentDNSIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentDNSIPIndex.setStatus("current")
_ArrisRouterWanCurrentDNSIPAddrType_Type = InetAddressType
_ArrisRouterWanCurrentDNSIPAddrType_Object = MibTableColumn
arrisRouterWanCurrentDNSIPAddrType = _ArrisRouterWanCurrentDNSIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 2, 1, 2),
    _ArrisRouterWanCurrentDNSIPAddrType_Type()
)
arrisRouterWanCurrentDNSIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentDNSIPAddrType.setStatus("current")
_ArrisRouterWanCurrentDNSIPAddr_Type = InetAddress
_ArrisRouterWanCurrentDNSIPAddr_Object = MibTableColumn
arrisRouterWanCurrentDNSIPAddr = _ArrisRouterWanCurrentDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 2, 1, 3),
    _ArrisRouterWanCurrentDNSIPAddr_Type()
)
arrisRouterWanCurrentDNSIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanCurrentDNSIPAddr.setStatus("current")
_ArrisRouterWanStaticDNSTable_Object = MibTable
arrisRouterWanStaticDNSTable = _ArrisRouterWanStaticDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSTable.setStatus("current")
_ArrisRouterWanStaticDNSEntry_Object = MibTableRow
arrisRouterWanStaticDNSEntry = _ArrisRouterWanStaticDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4, 1)
)
arrisRouterWanStaticDNSEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWanStaticDNSIPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSEntry.setStatus("current")


class _ArrisRouterWanStaticDNSIPIndex_Type(Unsigned32):
    """Custom type arrisRouterWanStaticDNSIPIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ArrisRouterWanStaticDNSIPIndex_Type.__name__ = "Unsigned32"
_ArrisRouterWanStaticDNSIPIndex_Object = MibTableColumn
arrisRouterWanStaticDNSIPIndex = _ArrisRouterWanStaticDNSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4, 1, 1),
    _ArrisRouterWanStaticDNSIPIndex_Type()
)
arrisRouterWanStaticDNSIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSIPIndex.setStatus("current")
_ArrisRouterWanStaticDNSIPAddrType_Type = InetAddressType
_ArrisRouterWanStaticDNSIPAddrType_Object = MibTableColumn
arrisRouterWanStaticDNSIPAddrType = _ArrisRouterWanStaticDNSIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4, 1, 2),
    _ArrisRouterWanStaticDNSIPAddrType_Type()
)
arrisRouterWanStaticDNSIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSIPAddrType.setStatus("current")
_ArrisRouterWanStaticDNSIPAddr_Type = InetAddress
_ArrisRouterWanStaticDNSIPAddr_Object = MibTableColumn
arrisRouterWanStaticDNSIPAddr = _ArrisRouterWanStaticDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4, 1, 3),
    _ArrisRouterWanStaticDNSIPAddr_Type()
)
arrisRouterWanStaticDNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSIPAddr.setStatus("current")
_ArrisRouterWanStaticDNSRowStatus_Type = RowStatus
_ArrisRouterWanStaticDNSRowStatus_Object = MibTableColumn
arrisRouterWanStaticDNSRowStatus = _ArrisRouterWanStaticDNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 11, 4, 1, 4),
    _ArrisRouterWanStaticDNSRowStatus_Type()
)
arrisRouterWanStaticDNSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWanStaticDNSRowStatus.setStatus("current")
_ArrisRouterWanDHCPObjects_ObjectIdentity = ObjectIdentity
arrisRouterWanDHCPObjects = _ArrisRouterWanDHCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12)
)


class _ArrisRouterWanRenewLease_Type(Integer32):
    """Custom type arrisRouterWanRenewLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noApply", 0),
          ("apply", 1))
    )


_ArrisRouterWanRenewLease_Type.__name__ = "Integer32"
_ArrisRouterWanRenewLease_Object = MibScalar
arrisRouterWanRenewLease = _ArrisRouterWanRenewLease_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 1),
    _ArrisRouterWanRenewLease_Type()
)
arrisRouterWanRenewLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanRenewLease.setStatus("current")


class _ArrisRouterWanReleaseLease_Type(Integer32):
    """Custom type arrisRouterWanReleaseLease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noApply", 0),
          ("apply", 1))
    )


_ArrisRouterWanReleaseLease_Type.__name__ = "Integer32"
_ArrisRouterWanReleaseLease_Object = MibScalar
arrisRouterWanReleaseLease = _ArrisRouterWanReleaseLease_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 2),
    _ArrisRouterWanReleaseLease_Type()
)
arrisRouterWanReleaseLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanReleaseLease.setStatus("current")
_ArrisRouterWanDHCPDuration_Type = Unsigned32
_ArrisRouterWanDHCPDuration_Object = MibScalar
arrisRouterWanDHCPDuration = _ArrisRouterWanDHCPDuration_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 3),
    _ArrisRouterWanDHCPDuration_Type()
)
arrisRouterWanDHCPDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPDuration.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPDuration.setUnits("seconds")
_ArrisRouterWanDHCPExpire_Type = DateAndTime
_ArrisRouterWanDHCPExpire_Object = MibScalar
arrisRouterWanDHCPExpire = _ArrisRouterWanDHCPExpire_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 4),
    _ArrisRouterWanDHCPExpire_Type()
)
arrisRouterWanDHCPExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPExpire.setStatus("current")


class _ArrisRouterWanRenewLeaseV6_Type(Integer32):
    """Custom type arrisRouterWanRenewLeaseV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noApply", 0),
          ("apply", 1))
    )


_ArrisRouterWanRenewLeaseV6_Type.__name__ = "Integer32"
_ArrisRouterWanRenewLeaseV6_Object = MibScalar
arrisRouterWanRenewLeaseV6 = _ArrisRouterWanRenewLeaseV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 5),
    _ArrisRouterWanRenewLeaseV6_Type()
)
arrisRouterWanRenewLeaseV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanRenewLeaseV6.setStatus("current")


class _ArrisRouterWanReleaseLeaseV6_Type(Integer32):
    """Custom type arrisRouterWanReleaseLeaseV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noApply", 0),
          ("apply", 1))
    )


_ArrisRouterWanReleaseLeaseV6_Type.__name__ = "Integer32"
_ArrisRouterWanReleaseLeaseV6_Object = MibScalar
arrisRouterWanReleaseLeaseV6 = _ArrisRouterWanReleaseLeaseV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 6),
    _ArrisRouterWanReleaseLeaseV6_Type()
)
arrisRouterWanReleaseLeaseV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanReleaseLeaseV6.setStatus("current")
_ArrisRouterWanDHCPDurationV6_Type = Unsigned32
_ArrisRouterWanDHCPDurationV6_Object = MibScalar
arrisRouterWanDHCPDurationV6 = _ArrisRouterWanDHCPDurationV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 7),
    _ArrisRouterWanDHCPDurationV6_Type()
)
arrisRouterWanDHCPDurationV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPDurationV6.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPDurationV6.setUnits("seconds")
_ArrisRouterWanDHCPExpireV6_Type = DateAndTime
_ArrisRouterWanDHCPExpireV6_Object = MibScalar
arrisRouterWanDHCPExpireV6 = _ArrisRouterWanDHCPExpireV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 8),
    _ArrisRouterWanDHCPExpireV6_Type()
)
arrisRouterWanDHCPExpireV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPExpireV6.setStatus("current")
_ArrisRouterWanDhcpSrvIPAddr_Type = InetAddress
_ArrisRouterWanDhcpSrvIPAddr_Object = MibScalar
arrisRouterWanDhcpSrvIPAddr = _ArrisRouterWanDhcpSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 9),
    _ArrisRouterWanDhcpSrvIPAddr_Type()
)
arrisRouterWanDhcpSrvIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDhcpSrvIPAddr.setStatus("current")


class _ArrisRouterWanDhcpOpt43Sub02_Type(Integer32):
    """Custom type arrisRouterWanDhcpOpt43Sub02 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("erouter", 0),
          ("ecm", 1))
    )


_ArrisRouterWanDhcpOpt43Sub02_Type.__name__ = "Integer32"
_ArrisRouterWanDhcpOpt43Sub02_Object = MibScalar
arrisRouterWanDhcpOpt43Sub02 = _ArrisRouterWanDhcpOpt43Sub02_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 10),
    _ArrisRouterWanDhcpOpt43Sub02_Type()
)
arrisRouterWanDhcpOpt43Sub02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanDhcpOpt43Sub02.setStatus("current")


class _ArrisRouterWanDHCPDUIDV6_Type(DisplayString):
    """Custom type arrisRouterWanDHCPDUIDV6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_ArrisRouterWanDHCPDUIDV6_Type.__name__ = "DisplayString"
_ArrisRouterWanDHCPDUIDV6_Object = MibScalar
arrisRouterWanDHCPDUIDV6 = _ArrisRouterWanDHCPDUIDV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 11),
    _ArrisRouterWanDHCPDUIDV6_Type()
)
arrisRouterWanDHCPDUIDV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPDUIDV6.setStatus("current")
_ArrisRouterWanDHCPSrvAddrV6_Type = InetAddressIPv6
_ArrisRouterWanDHCPSrvAddrV6_Object = MibScalar
arrisRouterWanDHCPSrvAddrV6 = _ArrisRouterWanDHCPSrvAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 12),
    _ArrisRouterWanDHCPSrvAddrV6_Type()
)
arrisRouterWanDHCPSrvAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPSrvAddrV6.setStatus("current")


class _ArrisRouterWanDHCPSrvDUIDV6_Type(DisplayString):
    """Custom type arrisRouterWanDHCPSrvDUIDV6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_ArrisRouterWanDHCPSrvDUIDV6_Type.__name__ = "DisplayString"
_ArrisRouterWanDHCPSrvDUIDV6_Object = MibScalar
arrisRouterWanDHCPSrvDUIDV6 = _ArrisRouterWanDHCPSrvDUIDV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 12, 13),
    _ArrisRouterWanDHCPSrvDUIDV6_Type()
)
arrisRouterWanDHCPSrvDUIDV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanDHCPSrvDUIDV6.setStatus("current")
_ArrisRouterWanIFMacAddr_Type = MacAddress
_ArrisRouterWanIFMacAddr_Object = MibScalar
arrisRouterWanIFMacAddr = _ArrisRouterWanIFMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 13),
    _ArrisRouterWanIFMacAddr_Type()
)
arrisRouterWanIFMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWanIFMacAddr.setStatus("current")


class _ArrisRouterWanConnTypeV6_Type(Integer32):
    """Custom type arrisRouterWanConnTypeV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dynamic", 1),
          ("static", 2))
    )


_ArrisRouterWanConnTypeV6_Type.__name__ = "Integer32"
_ArrisRouterWanConnTypeV6_Object = MibScalar
arrisRouterWanConnTypeV6 = _ArrisRouterWanConnTypeV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 16),
    _ArrisRouterWanConnTypeV6_Type()
)
arrisRouterWanConnTypeV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanConnTypeV6.setStatus("current")


class _ArrisRouterWanIPProvMode_Type(Integer32):
    """Custom type arrisRouterWanIPProvMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabledBridge", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("dualStack", 3))
    )


_ArrisRouterWanIPProvMode_Type.__name__ = "Integer32"
_ArrisRouterWanIPProvMode_Object = MibScalar
arrisRouterWanIPProvMode = _ArrisRouterWanIPProvMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 17),
    _ArrisRouterWanIPProvMode_Type()
)
arrisRouterWanIPProvMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanIPProvMode.setStatus("current")
_ArrisRouterDSLiteWanObjects_ObjectIdentity = ObjectIdentity
arrisRouterDSLiteWanObjects = _ArrisRouterDSLiteWanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18)
)


class _ArrisRouterDSLiteWanEnable_Type(TruthValue):
    """Custom type arrisRouterDSLiteWanEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterDSLiteWanEnable_Type.__name__ = "TruthValue"
_ArrisRouterDSLiteWanEnable_Object = MibScalar
arrisRouterDSLiteWanEnable = _ArrisRouterDSLiteWanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 1),
    _ArrisRouterDSLiteWanEnable_Type()
)
arrisRouterDSLiteWanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDSLiteWanEnable.setStatus("current")
_ArrisRouterDSLiteWanLSNATAddrType_Type = InetAddressType
_ArrisRouterDSLiteWanLSNATAddrType_Object = MibScalar
arrisRouterDSLiteWanLSNATAddrType = _ArrisRouterDSLiteWanLSNATAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 2),
    _ArrisRouterDSLiteWanLSNATAddrType_Type()
)
arrisRouterDSLiteWanLSNATAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDSLiteWanLSNATAddrType.setStatus("current")
_ArrisRouterDSLiteWanLSNATAddr_Type = InetAddressIPv6
_ArrisRouterDSLiteWanLSNATAddr_Object = MibScalar
arrisRouterDSLiteWanLSNATAddr = _ArrisRouterDSLiteWanLSNATAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 3),
    _ArrisRouterDSLiteWanLSNATAddr_Type()
)
arrisRouterDSLiteWanLSNATAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDSLiteWanLSNATAddr.setStatus("current")


class _ArrisRouterDSLiteTcpMssClamping_Type(TruthValue):
    """Custom type arrisRouterDSLiteTcpMssClamping based on TruthValue"""
    defaultValue = 1


_ArrisRouterDSLiteTcpMssClamping_Type.__name__ = "TruthValue"
_ArrisRouterDSLiteTcpMssClamping_Object = MibScalar
arrisRouterDSLiteTcpMssClamping = _ArrisRouterDSLiteTcpMssClamping_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 4),
    _ArrisRouterDSLiteTcpMssClamping_Type()
)
arrisRouterDSLiteTcpMssClamping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDSLiteTcpMssClamping.setStatus("current")
_ArrisRouterDSLiteTcpMssValue_Type = Unsigned32
_ArrisRouterDSLiteTcpMssValue_Object = MibScalar
arrisRouterDSLiteTcpMssValue = _ArrisRouterDSLiteTcpMssValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 5),
    _ArrisRouterDSLiteTcpMssValue_Type()
)
arrisRouterDSLiteTcpMssValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDSLiteTcpMssValue.setStatus("current")
_ArrisRouterDSLiteWanResolvedAddr_Type = InetAddressIPv6
_ArrisRouterDSLiteWanResolvedAddr_Object = MibScalar
arrisRouterDSLiteWanResolvedAddr = _ArrisRouterDSLiteWanResolvedAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 18, 6),
    _ArrisRouterDSLiteWanResolvedAddr_Type()
)
arrisRouterDSLiteWanResolvedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDSLiteWanResolvedAddr.setStatus("current")
_ArrisRouterSoftGreWanObjects_ObjectIdentity = ObjectIdentity
arrisRouterSoftGreWanObjects = _ArrisRouterSoftGreWanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19)
)
_ArrisRouterSoftGreWanTable_Object = MibTable
arrisRouterSoftGreWanTable = _ArrisRouterSoftGreWanTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanTable.setStatus("current")
_ArrisRouterSoftGreWanEntry_Object = MibTableRow
arrisRouterSoftGreWanEntry = _ArrisRouterSoftGreWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1)
)
arrisRouterSoftGreWanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanEntry.setStatus("current")


class _ArrisRouterSoftGreWanEnable_Type(TruthValue):
    """Custom type arrisRouterSoftGreWanEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterSoftGreWanEnable_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreWanEnable_Object = MibTableColumn
arrisRouterSoftGreWanEnable = _ArrisRouterSoftGreWanEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 1),
    _ArrisRouterSoftGreWanEnable_Type()
)
arrisRouterSoftGreWanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanEnable.setStatus("current")
_ArrisRouterSoftGreMappedInterface_Type = Unsigned32
_ArrisRouterSoftGreMappedInterface_Object = MibTableColumn
arrisRouterSoftGreMappedInterface = _ArrisRouterSoftGreMappedInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 2),
    _ArrisRouterSoftGreMappedInterface_Type()
)
arrisRouterSoftGreMappedInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreMappedInterface.setStatus("current")


class _ArrisRouterSoftGreMaxSessions_Type(Integer32):
    """Custom type arrisRouterSoftGreMaxSessions based on Integer32"""
    defaultValue = 5


_ArrisRouterSoftGreMaxSessions_Type.__name__ = "Integer32"
_ArrisRouterSoftGreMaxSessions_Object = MibTableColumn
arrisRouterSoftGreMaxSessions = _ArrisRouterSoftGreMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 3),
    _ArrisRouterSoftGreMaxSessions_Type()
)
arrisRouterSoftGreMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreMaxSessions.setStatus("current")


class _ArrisRouterSoftGreWanControllerFqdn_Type(DisplayString):
    """Custom type arrisRouterSoftGreWanControllerFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterSoftGreWanControllerFqdn_Type.__name__ = "DisplayString"
_ArrisRouterSoftGreWanControllerFqdn_Object = MibTableColumn
arrisRouterSoftGreWanControllerFqdn = _ArrisRouterSoftGreWanControllerFqdn_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 4),
    _ArrisRouterSoftGreWanControllerFqdn_Type()
)
arrisRouterSoftGreWanControllerFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanControllerFqdn.setStatus("current")
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Type = InetAddressType
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Object = MibTableColumn
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType = _ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 5),
    _ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType_Type()
)
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType.setStatus("current")
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Type = InetAddress
_ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Object = MibTableColumn
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress = _ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 6),
    _ArrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress_Type()
)
arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress.setStatus("current")


class _ArrisRouterSoftGreWanFailoverPingCount_Type(Integer32):
    """Custom type arrisRouterSoftGreWanFailoverPingCount based on Integer32"""
    defaultValue = 3


_ArrisRouterSoftGreWanFailoverPingCount_Type.__name__ = "Integer32"
_ArrisRouterSoftGreWanFailoverPingCount_Object = MibTableColumn
arrisRouterSoftGreWanFailoverPingCount = _ArrisRouterSoftGreWanFailoverPingCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 7),
    _ArrisRouterSoftGreWanFailoverPingCount_Type()
)
arrisRouterSoftGreWanFailoverPingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanFailoverPingCount.setStatus("current")


class _ArrisRouterSoftGreWanFailoverPingInterval_Type(Integer32):
    """Custom type arrisRouterSoftGreWanFailoverPingInterval based on Integer32"""
    defaultValue = 60


_ArrisRouterSoftGreWanFailoverPingInterval_Type.__name__ = "Integer32"
_ArrisRouterSoftGreWanFailoverPingInterval_Object = MibTableColumn
arrisRouterSoftGreWanFailoverPingInterval = _ArrisRouterSoftGreWanFailoverPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 8),
    _ArrisRouterSoftGreWanFailoverPingInterval_Type()
)
arrisRouterSoftGreWanFailoverPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanFailoverPingInterval.setStatus("current")


class _ArrisRouterSoftGreWanFailoverThreshold_Type(Integer32):
    """Custom type arrisRouterSoftGreWanFailoverThreshold based on Integer32"""
    defaultValue = 3


_ArrisRouterSoftGreWanFailoverThreshold_Type.__name__ = "Integer32"
_ArrisRouterSoftGreWanFailoverThreshold_Object = MibTableColumn
arrisRouterSoftGreWanFailoverThreshold = _ArrisRouterSoftGreWanFailoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 9),
    _ArrisRouterSoftGreWanFailoverThreshold_Type()
)
arrisRouterSoftGreWanFailoverThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanFailoverThreshold.setStatus("current")


class _ArrisRouterSoftGreCircuitIdEnabled_Type(TruthValue):
    """Custom type arrisRouterSoftGreCircuitIdEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterSoftGreCircuitIdEnabled_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreCircuitIdEnabled_Object = MibTableColumn
arrisRouterSoftGreCircuitIdEnabled = _ArrisRouterSoftGreCircuitIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 10),
    _ArrisRouterSoftGreCircuitIdEnabled_Type()
)
arrisRouterSoftGreCircuitIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreCircuitIdEnabled.setStatus("current")


class _ArrisRouterSoftGreRemoteIdEnabled_Type(TruthValue):
    """Custom type arrisRouterSoftGreRemoteIdEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterSoftGreRemoteIdEnabled_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreRemoteIdEnabled_Object = MibTableColumn
arrisRouterSoftGreRemoteIdEnabled = _ArrisRouterSoftGreRemoteIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 11),
    _ArrisRouterSoftGreRemoteIdEnabled_Type()
)
arrisRouterSoftGreRemoteIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRemoteIdEnabled.setStatus("current")


class _ArrisRouterSoftGreRadiusEnabled_Type(TruthValue):
    """Custom type arrisRouterSoftGreRadiusEnabled based on TruthValue"""
    defaultValue = 2


_ArrisRouterSoftGreRadiusEnabled_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreRadiusEnabled_Object = MibTableColumn
arrisRouterSoftGreRadiusEnabled = _ArrisRouterSoftGreRadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 12),
    _ArrisRouterSoftGreRadiusEnabled_Type()
)
arrisRouterSoftGreRadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusEnabled.setStatus("current")
_ArrisRouterSoftGreRadiusServerAddressType_Type = InetAddressType
_ArrisRouterSoftGreRadiusServerAddressType_Object = MibTableColumn
arrisRouterSoftGreRadiusServerAddressType = _ArrisRouterSoftGreRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 13),
    _ArrisRouterSoftGreRadiusServerAddressType_Type()
)
arrisRouterSoftGreRadiusServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusServerAddressType.setStatus("current")
_ArrisRouterSoftGreRadiusServerAddress_Type = InetAddress
_ArrisRouterSoftGreRadiusServerAddress_Object = MibTableColumn
arrisRouterSoftGreRadiusServerAddress = _ArrisRouterSoftGreRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 14),
    _ArrisRouterSoftGreRadiusServerAddress_Type()
)
arrisRouterSoftGreRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusServerAddress.setStatus("current")


class _ArrisRouterSoftGreRadiusServerPort_Type(Unsigned32):
    """Custom type arrisRouterSoftGreRadiusServerPort based on Unsigned32"""
    defaultValue = 1812


_ArrisRouterSoftGreRadiusServerPort_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreRadiusServerPort_Object = MibTableColumn
arrisRouterSoftGreRadiusServerPort = _ArrisRouterSoftGreRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 15),
    _ArrisRouterSoftGreRadiusServerPort_Type()
)
arrisRouterSoftGreRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusServerPort.setStatus("current")


class _ArrisRouterSoftGreRadiusKey_Type(DisplayString):
    """Custom type arrisRouterSoftGreRadiusKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrisRouterSoftGreRadiusKey_Type.__name__ = "DisplayString"
_ArrisRouterSoftGreRadiusKey_Object = MibTableColumn
arrisRouterSoftGreRadiusKey = _ArrisRouterSoftGreRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 16),
    _ArrisRouterSoftGreRadiusKey_Type()
)
arrisRouterSoftGreRadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusKey.setStatus("current")
_ArrisRouterSoftGreRadiusReAuthInterval_Type = Unsigned32
_ArrisRouterSoftGreRadiusReAuthInterval_Object = MibTableColumn
arrisRouterSoftGreRadiusReAuthInterval = _ArrisRouterSoftGreRadiusReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 17),
    _ArrisRouterSoftGreRadiusReAuthInterval_Type()
)
arrisRouterSoftGreRadiusReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusReAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusReAuthInterval.setUnits("seconds")


class _ArrisRouterSoftGreVlanQEnable_Type(TruthValue):
    """Custom type arrisRouterSoftGreVlanQEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterSoftGreVlanQEnable_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreVlanQEnable_Object = MibTableColumn
arrisRouterSoftGreVlanQEnable = _ArrisRouterSoftGreVlanQEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 18),
    _ArrisRouterSoftGreVlanQEnable_Type()
)
arrisRouterSoftGreVlanQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreVlanQEnable.setStatus("current")


class _ArrisRouterSoftGreWanDscp_Type(DscpOrAny):
    """Custom type arrisRouterSoftGreWanDscp based on DscpOrAny"""
    defaultValue = 0


_ArrisRouterSoftGreWanDscp_Type.__name__ = "DscpOrAny"
_ArrisRouterSoftGreWanDscp_Object = MibTableColumn
arrisRouterSoftGreWanDscp = _ArrisRouterSoftGreWanDscp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 19),
    _ArrisRouterSoftGreWanDscp_Type()
)
arrisRouterSoftGreWanDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanDscp.setStatus("current")


class _ArrisRouterSoftGreWanDNSRetryTimer_Type(Unsigned32):
    """Custom type arrisRouterSoftGreWanDNSRetryTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_ArrisRouterSoftGreWanDNSRetryTimer_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreWanDNSRetryTimer_Object = MibTableColumn
arrisRouterSoftGreWanDNSRetryTimer = _ArrisRouterSoftGreWanDNSRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 20),
    _ArrisRouterSoftGreWanDNSRetryTimer_Type()
)
arrisRouterSoftGreWanDNSRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanDNSRetryTimer.setStatus("current")
_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Type = InetAddressType
_ArrisRouterSoftGreWanCurrentControllerIPAddressType_Object = MibTableColumn
arrisRouterSoftGreWanCurrentControllerIPAddressType = _ArrisRouterSoftGreWanCurrentControllerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 21),
    _ArrisRouterSoftGreWanCurrentControllerIPAddressType_Type()
)
arrisRouterSoftGreWanCurrentControllerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanCurrentControllerIPAddressType.setStatus("current")
_ArrisRouterSoftGreWanCurrentControllerIPAddress_Type = InetAddress
_ArrisRouterSoftGreWanCurrentControllerIPAddress_Object = MibTableColumn
arrisRouterSoftGreWanCurrentControllerIPAddress = _ArrisRouterSoftGreWanCurrentControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 22),
    _ArrisRouterSoftGreWanCurrentControllerIPAddress_Type()
)
arrisRouterSoftGreWanCurrentControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanCurrentControllerIPAddress.setStatus("current")
_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Type = InetAddressType
_ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Object = MibTableColumn
arrisRouterSoftGreWanPrimaryControllerIPAddressType = _ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 23),
    _ArrisRouterSoftGreWanPrimaryControllerIPAddressType_Type()
)
arrisRouterSoftGreWanPrimaryControllerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanPrimaryControllerIPAddressType.setStatus("current")
_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Type = InetAddress
_ArrisRouterSoftGreWanPrimaryControllerIPAddress_Object = MibTableColumn
arrisRouterSoftGreWanPrimaryControllerIPAddress = _ArrisRouterSoftGreWanPrimaryControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 24),
    _ArrisRouterSoftGreWanPrimaryControllerIPAddress_Type()
)
arrisRouterSoftGreWanPrimaryControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanPrimaryControllerIPAddress.setStatus("current")
_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Type = InetAddressType
_ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Object = MibTableColumn
arrisRouterSoftGreWanSecondaryControllerIPAddressType = _ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 25),
    _ArrisRouterSoftGreWanSecondaryControllerIPAddressType_Type()
)
arrisRouterSoftGreWanSecondaryControllerIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanSecondaryControllerIPAddressType.setStatus("current")
_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Type = InetAddress
_ArrisRouterSoftGreWanSecondaryControllerIPAddress_Object = MibTableColumn
arrisRouterSoftGreWanSecondaryControllerIPAddress = _ArrisRouterSoftGreWanSecondaryControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 26),
    _ArrisRouterSoftGreWanSecondaryControllerIPAddress_Type()
)
arrisRouterSoftGreWanSecondaryControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanSecondaryControllerIPAddress.setStatus("current")


class _ArrisRouterSoftGreWanStatus_Type(Integer32):
    """Custom type arrisRouterSoftGreWanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("error", 2))
    )


_ArrisRouterSoftGreWanStatus_Type.__name__ = "Integer32"
_ArrisRouterSoftGreWanStatus_Object = MibTableColumn
arrisRouterSoftGreWanStatus = _ArrisRouterSoftGreWanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 27),
    _ArrisRouterSoftGreWanStatus_Type()
)
arrisRouterSoftGreWanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreWanStatus.setStatus("current")


class _ArrisRouterSoftGreTransportInterface_Type(Integer32):
    """Custom type arrisRouterSoftGreTransportInterface based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gwip", 0),
          ("cmip", 1))
    )


_ArrisRouterSoftGreTransportInterface_Type.__name__ = "Integer32"
_ArrisRouterSoftGreTransportInterface_Object = MibTableColumn
arrisRouterSoftGreTransportInterface = _ArrisRouterSoftGreTransportInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 29),
    _ArrisRouterSoftGreTransportInterface_Type()
)
arrisRouterSoftGreTransportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreTransportInterface.setStatus("current")


class _ArrisRouterSoftGreRadiusTransportInterface_Type(Integer32):
    """Custom type arrisRouterSoftGreRadiusTransportInterface based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gwip", 0),
          ("cmip", 1))
    )


_ArrisRouterSoftGreRadiusTransportInterface_Type.__name__ = "Integer32"
_ArrisRouterSoftGreRadiusTransportInterface_Object = MibTableColumn
arrisRouterSoftGreRadiusTransportInterface = _ArrisRouterSoftGreRadiusTransportInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 30),
    _ArrisRouterSoftGreRadiusTransportInterface_Type()
)
arrisRouterSoftGreRadiusTransportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusTransportInterface.setStatus("current")
_ArrisRouterSoftGreAcctServerAddressType_Type = InetAddressType
_ArrisRouterSoftGreAcctServerAddressType_Object = MibTableColumn
arrisRouterSoftGreAcctServerAddressType = _ArrisRouterSoftGreAcctServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 31),
    _ArrisRouterSoftGreAcctServerAddressType_Type()
)
arrisRouterSoftGreAcctServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctServerAddressType.setStatus("current")
_ArrisRouterSoftGreAcctServerAddress_Type = InetAddress
_ArrisRouterSoftGreAcctServerAddress_Object = MibTableColumn
arrisRouterSoftGreAcctServerAddress = _ArrisRouterSoftGreAcctServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 32),
    _ArrisRouterSoftGreAcctServerAddress_Type()
)
arrisRouterSoftGreAcctServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctServerAddress.setStatus("current")


class _ArrisRouterSoftGreAcctServerPort_Type(Unsigned32):
    """Custom type arrisRouterSoftGreAcctServerPort based on Unsigned32"""
    defaultValue = 1813


_ArrisRouterSoftGreAcctServerPort_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreAcctServerPort_Object = MibTableColumn
arrisRouterSoftGreAcctServerPort = _ArrisRouterSoftGreAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 33),
    _ArrisRouterSoftGreAcctServerPort_Type()
)
arrisRouterSoftGreAcctServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctServerPort.setStatus("current")


class _ArrisRouterSoftGreAcctKey_Type(DisplayString):
    """Custom type arrisRouterSoftGreAcctKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrisRouterSoftGreAcctKey_Type.__name__ = "DisplayString"
_ArrisRouterSoftGreAcctKey_Object = MibTableColumn
arrisRouterSoftGreAcctKey = _ArrisRouterSoftGreAcctKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 34),
    _ArrisRouterSoftGreAcctKey_Type()
)
arrisRouterSoftGreAcctKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctKey.setStatus("current")
_ArrisRouterSoftGreAcctInterval_Type = Unsigned32
_ArrisRouterSoftGreAcctInterval_Object = MibTableColumn
arrisRouterSoftGreAcctInterval = _ArrisRouterSoftGreAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 35),
    _ArrisRouterSoftGreAcctInterval_Type()
)
arrisRouterSoftGreAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterSoftGreAcctInterval.setUnits("seconds")
_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Type = InetAddressType
_ArrisRouterSoftGreRadiusSecondaryServerAddressType_Object = MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerAddressType = _ArrisRouterSoftGreRadiusSecondaryServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 36),
    _ArrisRouterSoftGreRadiusSecondaryServerAddressType_Type()
)
arrisRouterSoftGreRadiusSecondaryServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryServerAddressType.setStatus("current")
_ArrisRouterSoftGreRadiusSecondaryServerAddress_Type = InetAddress
_ArrisRouterSoftGreRadiusSecondaryServerAddress_Object = MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerAddress = _ArrisRouterSoftGreRadiusSecondaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 37),
    _ArrisRouterSoftGreRadiusSecondaryServerAddress_Type()
)
arrisRouterSoftGreRadiusSecondaryServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryServerAddress.setStatus("current")


class _ArrisRouterSoftGreRadiusSecondaryServerPort_Type(Unsigned32):
    """Custom type arrisRouterSoftGreRadiusSecondaryServerPort based on Unsigned32"""
    defaultValue = 1812


_ArrisRouterSoftGreRadiusSecondaryServerPort_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreRadiusSecondaryServerPort_Object = MibTableColumn
arrisRouterSoftGreRadiusSecondaryServerPort = _ArrisRouterSoftGreRadiusSecondaryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 38),
    _ArrisRouterSoftGreRadiusSecondaryServerPort_Type()
)
arrisRouterSoftGreRadiusSecondaryServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryServerPort.setStatus("current")


class _ArrisRouterSoftGreRadiusSecondaryKey_Type(DisplayString):
    """Custom type arrisRouterSoftGreRadiusSecondaryKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrisRouterSoftGreRadiusSecondaryKey_Type.__name__ = "DisplayString"
_ArrisRouterSoftGreRadiusSecondaryKey_Object = MibTableColumn
arrisRouterSoftGreRadiusSecondaryKey = _ArrisRouterSoftGreRadiusSecondaryKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 39),
    _ArrisRouterSoftGreRadiusSecondaryKey_Type()
)
arrisRouterSoftGreRadiusSecondaryKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryKey.setStatus("current")
_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Type = Unsigned32
_ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Object = MibTableColumn
arrisRouterSoftGreRadiusSecondaryReAuthInterval = _ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 1, 1, 40),
    _ArrisRouterSoftGreRadiusSecondaryReAuthInterval_Type()
)
arrisRouterSoftGreRadiusSecondaryReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryReAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterSoftGreRadiusSecondaryReAuthInterval.setUnits("seconds")
_ArrisRouterSoftGreSSIDTable_Object = MibTable
arrisRouterSoftGreSSIDTable = _ArrisRouterSoftGreSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    arrisRouterSoftGreSSIDTable.setStatus("current")
_ArrisRouterSoftGreSSIDEntry_Object = MibTableRow
arrisRouterSoftGreSSIDEntry = _ArrisRouterSoftGreSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 2, 1)
)
arrisRouterSoftGreSSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterSoftGreSSIDEntry.setStatus("current")


class _ArrisRouterSoftGreVLanId_Type(Unsigned32):
    """Custom type arrisRouterSoftGreVLanId based on Unsigned32"""
    defaultValue = 0


_ArrisRouterSoftGreVLanId_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreVLanId_Object = MibTableColumn
arrisRouterSoftGreVLanId = _ArrisRouterSoftGreVLanId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 2, 1, 1),
    _ArrisRouterSoftGreVLanId_Type()
)
arrisRouterSoftGreVLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreVLanId.setStatus("current")


class _ArrisRouterSoftGreVLanPriority_Type(Unsigned32):
    """Custom type arrisRouterSoftGreVLanPriority based on Unsigned32"""
    defaultValue = 0


_ArrisRouterSoftGreVLanPriority_Type.__name__ = "Unsigned32"
_ArrisRouterSoftGreVLanPriority_Object = MibTableColumn
arrisRouterSoftGreVLanPriority = _ArrisRouterSoftGreVLanPriority_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 2, 1, 2),
    _ArrisRouterSoftGreVLanPriority_Type()
)
arrisRouterSoftGreVLanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreVLanPriority.setStatus("current")


class _ArrisRouterSoftGreCustomerOptOut_Type(TruthValue):
    """Custom type arrisRouterSoftGreCustomerOptOut based on TruthValue"""
    defaultValue = 2


_ArrisRouterSoftGreCustomerOptOut_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreCustomerOptOut_Object = MibScalar
arrisRouterSoftGreCustomerOptOut = _ArrisRouterSoftGreCustomerOptOut_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 3),
    _ArrisRouterSoftGreCustomerOptOut_Type()
)
arrisRouterSoftGreCustomerOptOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSoftGreCustomerOptOut.setStatus("current")


class _ArrisRouterSoftGreCapable_Type(TruthValue):
    """Custom type arrisRouterSoftGreCapable based on TruthValue"""
    defaultValue = 1


_ArrisRouterSoftGreCapable_Type.__name__ = "TruthValue"
_ArrisRouterSoftGreCapable_Object = MibScalar
arrisRouterSoftGreCapable = _ArrisRouterSoftGreCapable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 19, 5),
    _ArrisRouterSoftGreCapable_Type()
)
arrisRouterSoftGreCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSoftGreCapable.setStatus("current")
_ArrisRouterDHCPRelayAgentWanObjects_ObjectIdentity = ObjectIdentity
arrisRouterDHCPRelayAgentWanObjects = _ArrisRouterDHCPRelayAgentWanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20)
)
_ArrisRouterDHCPRelayAgentSSIDTable_Object = MibTable
arrisRouterDHCPRelayAgentSSIDTable = _ArrisRouterDHCPRelayAgentSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentSSIDTable.setStatus("current")
_ArrisRouterDHCPRelayAgentSSIDEntry_Object = MibTableRow
arrisRouterDHCPRelayAgentSSIDEntry = _ArrisRouterDHCPRelayAgentSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1, 1)
)
arrisRouterDHCPRelayAgentSSIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentSSIDEntry.setStatus("current")


class _ArrisRouterDHCPRelayAgentEnable_Type(TruthValue):
    """Custom type arrisRouterDHCPRelayAgentEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterDHCPRelayAgentEnable_Type.__name__ = "TruthValue"
_ArrisRouterDHCPRelayAgentEnable_Object = MibTableColumn
arrisRouterDHCPRelayAgentEnable = _ArrisRouterDHCPRelayAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1, 1, 1),
    _ArrisRouterDHCPRelayAgentEnable_Type()
)
arrisRouterDHCPRelayAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentEnable.setStatus("current")


class _ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type(TruthValue):
    """Custom type arrisRouterDHCPRelayAgentCircuitIdEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type.__name__ = "TruthValue"
_ArrisRouterDHCPRelayAgentCircuitIdEnabled_Object = MibTableColumn
arrisRouterDHCPRelayAgentCircuitIdEnabled = _ArrisRouterDHCPRelayAgentCircuitIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1, 1, 2),
    _ArrisRouterDHCPRelayAgentCircuitIdEnabled_Type()
)
arrisRouterDHCPRelayAgentCircuitIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentCircuitIdEnabled.setStatus("current")


class _ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type(TruthValue):
    """Custom type arrisRouterDHCPRelayAgentRemoteIdEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type.__name__ = "TruthValue"
_ArrisRouterDHCPRelayAgentRemoteIdEnabled_Object = MibTableColumn
arrisRouterDHCPRelayAgentRemoteIdEnabled = _ArrisRouterDHCPRelayAgentRemoteIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1, 1, 3),
    _ArrisRouterDHCPRelayAgentRemoteIdEnabled_Type()
)
arrisRouterDHCPRelayAgentRemoteIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentRemoteIdEnabled.setStatus("current")


class _ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type(TruthValue):
    """Custom type arrisRouterDHCPRelayAgentOption60SSIDEnabled based on TruthValue"""
    defaultValue = 2


_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type.__name__ = "TruthValue"
_ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Object = MibTableColumn
arrisRouterDHCPRelayAgentOption60SSIDEnabled = _ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 20, 1, 1, 4),
    _ArrisRouterDHCPRelayAgentOption60SSIDEnabled_Type()
)
arrisRouterDHCPRelayAgentOption60SSIDEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDHCPRelayAgentOption60SSIDEnabled.setStatus("current")
_ArrisRouterWanTR181GatewayInfoObjects_ObjectIdentity = ObjectIdentity
arrisRouterWanTR181GatewayInfoObjects = _ArrisRouterWanTR181GatewayInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 21)
)


class _ArrisRouterTR181GatewayManufacturerOUI_Type(DisplayString):
    """Custom type arrisRouterTR181GatewayManufacturerOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_ArrisRouterTR181GatewayManufacturerOUI_Type.__name__ = "DisplayString"
_ArrisRouterTR181GatewayManufacturerOUI_Object = MibScalar
arrisRouterTR181GatewayManufacturerOUI = _ArrisRouterTR181GatewayManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 21, 1),
    _ArrisRouterTR181GatewayManufacturerOUI_Type()
)
arrisRouterTR181GatewayManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterTR181GatewayManufacturerOUI.setStatus("current")


class _ArrisRouterTR181GatewayProductClass_Type(DisplayString):
    """Custom type arrisRouterTR181GatewayProductClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterTR181GatewayProductClass_Type.__name__ = "DisplayString"
_ArrisRouterTR181GatewayProductClass_Object = MibScalar
arrisRouterTR181GatewayProductClass = _ArrisRouterTR181GatewayProductClass_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 21, 2),
    _ArrisRouterTR181GatewayProductClass_Type()
)
arrisRouterTR181GatewayProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterTR181GatewayProductClass.setStatus("current")


class _ArrisRouterTR181GatewaySerialNumber_Type(DisplayString):
    """Custom type arrisRouterTR181GatewaySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterTR181GatewaySerialNumber_Type.__name__ = "DisplayString"
_ArrisRouterTR181GatewaySerialNumber_Object = MibScalar
arrisRouterTR181GatewaySerialNumber = _ArrisRouterTR181GatewaySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 21, 3),
    _ArrisRouterTR181GatewaySerialNumber_Type()
)
arrisRouterTR181GatewaySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterTR181GatewaySerialNumber.setStatus("current")


class _ArrisRouterWanForceIGMPVersion_Type(Integer32):
    """Custom type arrisRouterWanForceIGMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("igmpv1", 1),
          ("igmpv2", 2),
          ("igmpv3", 3))
    )


_ArrisRouterWanForceIGMPVersion_Type.__name__ = "Integer32"
_ArrisRouterWanForceIGMPVersion_Object = MibScalar
arrisRouterWanForceIGMPVersion = _ArrisRouterWanForceIGMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 1, 22),
    _ArrisRouterWanForceIGMPVersion_Type()
)
arrisRouterWanForceIGMPVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWanForceIGMPVersion.setStatus("current")
_ArrisRouterLanConfig_ObjectIdentity = ObjectIdentity
arrisRouterLanConfig = _ArrisRouterLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2)
)
_ArrisRouterLanSrvTable_Object = MibTable
arrisRouterLanSrvTable = _ArrisRouterLanSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    arrisRouterLanSrvTable.setStatus("current")
_ArrisRouterLanSrvEntry_Object = MibTableRow
arrisRouterLanSrvEntry = _ArrisRouterLanSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1)
)
arrisRouterLanSrvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterLanSrvEntry.setStatus("current")


class _ArrisRouterLanName_Type(DisplayString):
    """Custom type arrisRouterLanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanName_Type.__name__ = "DisplayString"
_ArrisRouterLanName_Object = MibTableColumn
arrisRouterLanName = _ArrisRouterLanName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 1),
    _ArrisRouterLanName_Type()
)
arrisRouterLanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanName.setStatus("current")


class _ArrisRouterLanSubnetMaskType_Type(InetAddressType):
    """Custom type arrisRouterLanSubnetMaskType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterLanSubnetMaskType_Type.__name__ = "InetAddressType"
_ArrisRouterLanSubnetMaskType_Object = MibTableColumn
arrisRouterLanSubnetMaskType = _ArrisRouterLanSubnetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 2),
    _ArrisRouterLanSubnetMaskType_Type()
)
arrisRouterLanSubnetMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanSubnetMaskType.setStatus("current")
_ArrisRouterLanSubnetMask_Type = InetAddress
_ArrisRouterLanSubnetMask_Object = MibTableColumn
arrisRouterLanSubnetMask = _ArrisRouterLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 3),
    _ArrisRouterLanSubnetMask_Type()
)
arrisRouterLanSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanSubnetMask.setStatus("current")


class _ArrisRouterLanGatewayIpType_Type(InetAddressType):
    """Custom type arrisRouterLanGatewayIpType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterLanGatewayIpType_Type.__name__ = "InetAddressType"
_ArrisRouterLanGatewayIpType_Object = MibTableColumn
arrisRouterLanGatewayIpType = _ArrisRouterLanGatewayIpType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 4),
    _ArrisRouterLanGatewayIpType_Type()
)
arrisRouterLanGatewayIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanGatewayIpType.setStatus("current")
_ArrisRouterLanGatewayIp_Type = InetAddress
_ArrisRouterLanGatewayIp_Object = MibTableColumn
arrisRouterLanGatewayIp = _ArrisRouterLanGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 5),
    _ArrisRouterLanGatewayIp_Type()
)
arrisRouterLanGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanGatewayIp.setStatus("current")


class _ArrisRouterLanGatewayIp2Type_Type(InetAddressType):
    """Custom type arrisRouterLanGatewayIp2Type based on InetAddressType"""
    defaultValue = 1


_ArrisRouterLanGatewayIp2Type_Type.__name__ = "InetAddressType"
_ArrisRouterLanGatewayIp2Type_Object = MibTableColumn
arrisRouterLanGatewayIp2Type = _ArrisRouterLanGatewayIp2Type_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 6),
    _ArrisRouterLanGatewayIp2Type_Type()
)
arrisRouterLanGatewayIp2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanGatewayIp2Type.setStatus("current")
_ArrisRouterLanGatewayIp2_Type = InetAddress
_ArrisRouterLanGatewayIp2_Object = MibTableColumn
arrisRouterLanGatewayIp2 = _ArrisRouterLanGatewayIp2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 7),
    _ArrisRouterLanGatewayIp2_Type()
)
arrisRouterLanGatewayIp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanGatewayIp2.setStatus("current")


class _ArrisRouterLanVLanID_Type(Unsigned32):
    """Custom type arrisRouterLanVLanID based on Unsigned32"""
    defaultValue = 0


_ArrisRouterLanVLanID_Type.__name__ = "Unsigned32"
_ArrisRouterLanVLanID_Object = MibTableColumn
arrisRouterLanVLanID = _ArrisRouterLanVLanID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 8),
    _ArrisRouterLanVLanID_Type()
)
arrisRouterLanVLanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanVLanID.setStatus("current")


class _ArrisRouterLanUseDHCP_Type(TruthValue):
    """Custom type arrisRouterLanUseDHCP based on TruthValue"""
    defaultValue = 1


_ArrisRouterLanUseDHCP_Type.__name__ = "TruthValue"
_ArrisRouterLanUseDHCP_Object = MibTableColumn
arrisRouterLanUseDHCP = _ArrisRouterLanUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 9),
    _ArrisRouterLanUseDHCP_Type()
)
arrisRouterLanUseDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanUseDHCP.setStatus("current")
_ArrisRouterLanStartDHCPType_Type = InetAddressType
_ArrisRouterLanStartDHCPType_Object = MibTableColumn
arrisRouterLanStartDHCPType = _ArrisRouterLanStartDHCPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 10),
    _ArrisRouterLanStartDHCPType_Type()
)
arrisRouterLanStartDHCPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanStartDHCPType.setStatus("current")
_ArrisRouterLanStartDHCP_Type = InetAddress
_ArrisRouterLanStartDHCP_Object = MibTableColumn
arrisRouterLanStartDHCP = _ArrisRouterLanStartDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 11),
    _ArrisRouterLanStartDHCP_Type()
)
arrisRouterLanStartDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanStartDHCP.setStatus("current")
_ArrisRouterLanEndDHCPType_Type = InetAddressType
_ArrisRouterLanEndDHCPType_Object = MibTableColumn
arrisRouterLanEndDHCPType = _ArrisRouterLanEndDHCPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 12),
    _ArrisRouterLanEndDHCPType_Type()
)
arrisRouterLanEndDHCPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEndDHCPType.setStatus("current")
_ArrisRouterLanEndDHCP_Type = InetAddress
_ArrisRouterLanEndDHCP_Object = MibTableColumn
arrisRouterLanEndDHCP = _ArrisRouterLanEndDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 13),
    _ArrisRouterLanEndDHCP_Type()
)
arrisRouterLanEndDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEndDHCP.setStatus("current")
_ArrisRouterLanLeaseTime_Type = Unsigned32
_ArrisRouterLanLeaseTime_Object = MibTableColumn
arrisRouterLanLeaseTime = _ArrisRouterLanLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 14),
    _ArrisRouterLanLeaseTime_Type()
)
arrisRouterLanLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanLeaseTime.setUnits("seconds")


class _ArrisRouterLanDomainName_Type(DisplayString):
    """Custom type arrisRouterLanDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanDomainName_Type.__name__ = "DisplayString"
_ArrisRouterLanDomainName_Object = MibTableColumn
arrisRouterLanDomainName = _ArrisRouterLanDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 15),
    _ArrisRouterLanDomainName_Type()
)
arrisRouterLanDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanDomainName.setStatus("current")


class _ArrisRouterLanRelayDNS_Type(TruthValue):
    """Custom type arrisRouterLanRelayDNS based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanRelayDNS_Type.__name__ = "TruthValue"
_ArrisRouterLanRelayDNS_Object = MibTableColumn
arrisRouterLanRelayDNS = _ArrisRouterLanRelayDNS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 19),
    _ArrisRouterLanRelayDNS_Type()
)
arrisRouterLanRelayDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanRelayDNS.setStatus("current")


class _ArrisRouterLanPassThru_Type(Integer32):
    """Custom type arrisRouterLanPassThru based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("passThru", 1),
          ("routedNAT", 2),
          ("routedNoNAT", 3))
    )


_ArrisRouterLanPassThru_Type.__name__ = "Integer32"
_ArrisRouterLanPassThru_Object = MibTableColumn
arrisRouterLanPassThru = _ArrisRouterLanPassThru_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 21),
    _ArrisRouterLanPassThru_Type()
)
arrisRouterLanPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanPassThru.setStatus("current")
_ArrisRouterLanFirewallOn_Type = TruthValue
_ArrisRouterLanFirewallOn_Object = MibTableColumn
arrisRouterLanFirewallOn = _ArrisRouterLanFirewallOn_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 22),
    _ArrisRouterLanFirewallOn_Type()
)
arrisRouterLanFirewallOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanFirewallOn.setStatus("current")
_ArrisRouterLanUPnPEnable_Type = TruthValue
_ArrisRouterLanUPnPEnable_Object = MibTableColumn
arrisRouterLanUPnPEnable = _ArrisRouterLanUPnPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 23),
    _ArrisRouterLanUPnPEnable_Type()
)
arrisRouterLanUPnPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanUPnPEnable.setStatus("current")
_ArrisRouterLanCPEAging_Type = Integer32
_ArrisRouterLanCPEAging_Object = MibTableColumn
arrisRouterLanCPEAging = _ArrisRouterLanCPEAging_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 24),
    _ArrisRouterLanCPEAging_Type()
)
arrisRouterLanCPEAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanCPEAging.setStatus("current")


class _ArrisRouterLanOverrideDNS_Type(TruthValue):
    """Custom type arrisRouterLanOverrideDNS based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanOverrideDNS_Type.__name__ = "TruthValue"
_ArrisRouterLanOverrideDNS_Object = MibTableColumn
arrisRouterLanOverrideDNS = _ArrisRouterLanOverrideDNS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 25),
    _ArrisRouterLanOverrideDNS_Type()
)
arrisRouterLanOverrideDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanOverrideDNS.setStatus("current")


class _ArrisRouterLanNatAlgsEnabled_Type(Bits):
    """Custom type arrisRouterLanNatAlgsEnabled based on Bits"""
    namedValues = NamedValues(
        *(("rsvp", 0),
          ("ftp", 1),
          ("tftp", 2),
          ("kerb88", 3),
          ("netBiosDgm", 4),
          ("ike", 5),
          ("rtsp", 6),
          ("kerb1293", 7),
          ("h225", 8),
          ("pptp", 9),
          ("msn", 10),
          ("sip", 11),
          ("icq", 12),
          ("irc6667", 13),
          ("icqTalk", 14),
          ("net2Phone", 15),
          ("irc7000", 16),
          ("irc8000", 17))
    )

_ArrisRouterLanNatAlgsEnabled_Type.__name__ = "Bits"
_ArrisRouterLanNatAlgsEnabled_Object = MibTableColumn
arrisRouterLanNatAlgsEnabled = _ArrisRouterLanNatAlgsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 26),
    _ArrisRouterLanNatAlgsEnabled_Type()
)
arrisRouterLanNatAlgsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanNatAlgsEnabled.setStatus("current")
_ArrisRouterLanMappedInterface_Type = Unsigned32
_ArrisRouterLanMappedInterface_Object = MibTableColumn
arrisRouterLanMappedInterface = _ArrisRouterLanMappedInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 27),
    _ArrisRouterLanMappedInterface_Type()
)
arrisRouterLanMappedInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanMappedInterface.setStatus("current")


class _ArrisRouterLanEnvironmentControl_Type(Integer32):
    """Custom type arrisRouterLanEnvironmentControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 0),
          ("locked", 1))
    )


_ArrisRouterLanEnvironmentControl_Type.__name__ = "Integer32"
_ArrisRouterLanEnvironmentControl_Object = MibTableColumn
arrisRouterLanEnvironmentControl = _ArrisRouterLanEnvironmentControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 28),
    _ArrisRouterLanEnvironmentControl_Type()
)
arrisRouterLanEnvironmentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEnvironmentControl.setStatus("current")
_ArrisRouterLanPrefixLengthV6_Type = InetAddressPrefixLength
_ArrisRouterLanPrefixLengthV6_Object = MibTableColumn
arrisRouterLanPrefixLengthV6 = _ArrisRouterLanPrefixLengthV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 29),
    _ArrisRouterLanPrefixLengthV6_Type()
)
arrisRouterLanPrefixLengthV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanPrefixLengthV6.setStatus("current")


class _ArrisRouterLanUseDHCPV6_Type(TruthValue):
    """Custom type arrisRouterLanUseDHCPV6 based on TruthValue"""
    defaultValue = 1


_ArrisRouterLanUseDHCPV6_Type.__name__ = "TruthValue"
_ArrisRouterLanUseDHCPV6_Object = MibTableColumn
arrisRouterLanUseDHCPV6 = _ArrisRouterLanUseDHCPV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 30),
    _ArrisRouterLanUseDHCPV6_Type()
)
arrisRouterLanUseDHCPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanUseDHCPV6.setStatus("current")
_ArrisRouterLanStartDHCPV6_Type = InetAddressIPv6
_ArrisRouterLanStartDHCPV6_Object = MibTableColumn
arrisRouterLanStartDHCPV6 = _ArrisRouterLanStartDHCPV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 31),
    _ArrisRouterLanStartDHCPV6_Type()
)
arrisRouterLanStartDHCPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanStartDHCPV6.setStatus("current")
_ArrisRouterLanEndDHCPV6_Type = InetAddressIPv6
_ArrisRouterLanEndDHCPV6_Object = MibTableColumn
arrisRouterLanEndDHCPV6 = _ArrisRouterLanEndDHCPV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 32),
    _ArrisRouterLanEndDHCPV6_Type()
)
arrisRouterLanEndDHCPV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEndDHCPV6.setStatus("current")
_ArrisRouterLanLeaseTimeV6_Type = Unsigned32
_ArrisRouterLanLeaseTimeV6_Object = MibTableColumn
arrisRouterLanLeaseTimeV6 = _ArrisRouterLanLeaseTimeV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 33),
    _ArrisRouterLanLeaseTimeV6_Type()
)
arrisRouterLanLeaseTimeV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanLeaseTimeV6.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanLeaseTimeV6.setUnits("seconds")
_ArrisRouterLanLinkLocalAddressV6_Type = InetAddressIPv6
_ArrisRouterLanLinkLocalAddressV6_Object = MibTableColumn
arrisRouterLanLinkLocalAddressV6 = _ArrisRouterLanLinkLocalAddressV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 34),
    _ArrisRouterLanLinkLocalAddressV6_Type()
)
arrisRouterLanLinkLocalAddressV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanLinkLocalAddressV6.setStatus("current")


class _ArrisRouterLanDNSRelayV6_Type(TruthValue):
    """Custom type arrisRouterLanDNSRelayV6 based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanDNSRelayV6_Type.__name__ = "TruthValue"
_ArrisRouterLanDNSRelayV6_Object = MibTableColumn
arrisRouterLanDNSRelayV6 = _ArrisRouterLanDNSRelayV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 35),
    _ArrisRouterLanDNSRelayV6_Type()
)
arrisRouterLanDNSRelayV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanDNSRelayV6.setStatus("current")


class _ArrisRouterLanDNSOverrideV6_Type(TruthValue):
    """Custom type arrisRouterLanDNSOverrideV6 based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanDNSOverrideV6_Type.__name__ = "TruthValue"
_ArrisRouterLanDNSOverrideV6_Object = MibTableColumn
arrisRouterLanDNSOverrideV6 = _ArrisRouterLanDNSOverrideV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 36),
    _ArrisRouterLanDNSOverrideV6_Type()
)
arrisRouterLanDNSOverrideV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanDNSOverrideV6.setStatus("current")
_ArrisRouterLanPreProvLeaseTime_Type = Unsigned32
_ArrisRouterLanPreProvLeaseTime_Object = MibTableColumn
arrisRouterLanPreProvLeaseTime = _ArrisRouterLanPreProvLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 37),
    _ArrisRouterLanPreProvLeaseTime_Type()
)
arrisRouterLanPreProvLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanPreProvLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanPreProvLeaseTime.setUnits("seconds")


class _ArrisRouterLanParentalControlsEnable_Type(TruthValue):
    """Custom type arrisRouterLanParentalControlsEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanParentalControlsEnable_Type.__name__ = "TruthValue"
_ArrisRouterLanParentalControlsEnable_Object = MibTableColumn
arrisRouterLanParentalControlsEnable = _ArrisRouterLanParentalControlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 2, 1, 39),
    _ArrisRouterLanParentalControlsEnable_Type()
)
arrisRouterLanParentalControlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanParentalControlsEnable.setStatus("current")
_ArrisRouterLanDNSTable_Object = MibTable
arrisRouterLanDNSTable = _ArrisRouterLanDNSTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    arrisRouterLanDNSTable.setStatus("current")
_ArrisRouterLanDNSEntry_Object = MibTableRow
arrisRouterLanDNSEntry = _ArrisRouterLanDNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3, 1)
)
arrisRouterLanDNSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanDNSIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanDNSEntry.setStatus("current")


class _ArrisRouterLanDNSIdx_Type(Unsigned32):
    """Custom type arrisRouterLanDNSIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ArrisRouterLanDNSIdx_Type.__name__ = "Unsigned32"
_ArrisRouterLanDNSIdx_Object = MibTableColumn
arrisRouterLanDNSIdx = _ArrisRouterLanDNSIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3, 1, 1),
    _ArrisRouterLanDNSIdx_Type()
)
arrisRouterLanDNSIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanDNSIdx.setStatus("current")
_ArrisRouterLanDNSIPAddrType_Type = InetAddressType
_ArrisRouterLanDNSIPAddrType_Object = MibTableColumn
arrisRouterLanDNSIPAddrType = _ArrisRouterLanDNSIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3, 1, 2),
    _ArrisRouterLanDNSIPAddrType_Type()
)
arrisRouterLanDNSIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanDNSIPAddrType.setStatus("current")
_ArrisRouterLanDNSIPAddr_Type = InetAddress
_ArrisRouterLanDNSIPAddr_Object = MibTableColumn
arrisRouterLanDNSIPAddr = _ArrisRouterLanDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3, 1, 3),
    _ArrisRouterLanDNSIPAddr_Type()
)
arrisRouterLanDNSIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanDNSIPAddr.setStatus("current")
_ArrisRouterLanDNSRowStatus_Type = RowStatus
_ArrisRouterLanDNSRowStatus_Object = MibTableColumn
arrisRouterLanDNSRowStatus = _ArrisRouterLanDNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 3, 1, 4),
    _ArrisRouterLanDNSRowStatus_Type()
)
arrisRouterLanDNSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanDNSRowStatus.setStatus("current")
_ArrisRouterClientObjects_ObjectIdentity = ObjectIdentity
arrisRouterClientObjects = _ArrisRouterClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4)
)
_ArrisRouterLanClientCount_Type = Unsigned32
_ArrisRouterLanClientCount_Object = MibScalar
arrisRouterLanClientCount = _ArrisRouterLanClientCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 1),
    _ArrisRouterLanClientCount_Type()
)
arrisRouterLanClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientCount.setStatus("current")
_ArrisRouterLanClientTable_Object = MibTable
arrisRouterLanClientTable = _ArrisRouterLanClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    arrisRouterLanClientTable.setStatus("current")
_ArrisRouterLanClientEntry_Object = MibTableRow
arrisRouterLanClientEntry = _ArrisRouterLanClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1)
)
arrisRouterLanClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanClientIPAddrType"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanClientIPAddr"),
)
if mibBuilder.loadTexts:
    arrisRouterLanClientEntry.setStatus("current")
_ArrisRouterLanClientIPAddrType_Type = InetAddressType
_ArrisRouterLanClientIPAddrType_Object = MibTableColumn
arrisRouterLanClientIPAddrType = _ArrisRouterLanClientIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 1),
    _ArrisRouterLanClientIPAddrType_Type()
)
arrisRouterLanClientIPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanClientIPAddrType.setStatus("current")
_ArrisRouterLanClientIPAddr_Type = InetAddress
_ArrisRouterLanClientIPAddr_Object = MibTableColumn
arrisRouterLanClientIPAddr = _ArrisRouterLanClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 2),
    _ArrisRouterLanClientIPAddr_Type()
)
arrisRouterLanClientIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanClientIPAddr.setStatus("current")


class _ArrisRouterLanClientHostName_Type(DisplayString):
    """Custom type arrisRouterLanClientHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanClientHostName_Type.__name__ = "DisplayString"
_ArrisRouterLanClientHostName_Object = MibTableColumn
arrisRouterLanClientHostName = _ArrisRouterLanClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 3),
    _ArrisRouterLanClientHostName_Type()
)
arrisRouterLanClientHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanClientHostName.setStatus("current")
_ArrisRouterLanClientMAC_Type = MacAddress
_ArrisRouterLanClientMAC_Object = MibTableColumn
arrisRouterLanClientMAC = _ArrisRouterLanClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 4),
    _ArrisRouterLanClientMAC_Type()
)
arrisRouterLanClientMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanClientMAC.setStatus("current")


class _ArrisRouterLanClientAdapterType_Type(Integer32):
    """Custom type arrisRouterLanClientAdapterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ethernet", 1),
          ("usb", 2),
          ("moca", 3),
          ("dsg", 4),
          ("wireless1", 5),
          ("wireless2", 6),
          ("wireless3", 7),
          ("wireless4", 8),
          ("wireless5", 9),
          ("wireless6", 10),
          ("wireless7", 11),
          ("wireless8", 12),
          ("wireless9", 13),
          ("wireless10", 14),
          ("wireless11", 15),
          ("wireless12", 16),
          ("wireless13", 17),
          ("wireless14", 18),
          ("wireless15", 19),
          ("wireless16", 20),
          ("ethernet2", 21),
          ("ethernet3", 22),
          ("ethernet4", 23))
    )


_ArrisRouterLanClientAdapterType_Type.__name__ = "Integer32"
_ArrisRouterLanClientAdapterType_Object = MibTableColumn
arrisRouterLanClientAdapterType = _ArrisRouterLanClientAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 6),
    _ArrisRouterLanClientAdapterType_Type()
)
arrisRouterLanClientAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientAdapterType.setStatus("current")


class _ArrisRouterLanClientType_Type(Integer32):
    """Custom type arrisRouterLanClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dynamic", 1),
          ("static", 5),
          ("dynamicReserved", 6))
    )


_ArrisRouterLanClientType_Type.__name__ = "Integer32"
_ArrisRouterLanClientType_Object = MibTableColumn
arrisRouterLanClientType = _ArrisRouterLanClientType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 7),
    _ArrisRouterLanClientType_Type()
)
arrisRouterLanClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientType.setStatus("current")
_ArrisRouterLanClientLeaseEnd_Type = DateAndTime
_ArrisRouterLanClientLeaseEnd_Object = MibTableColumn
arrisRouterLanClientLeaseEnd = _ArrisRouterLanClientLeaseEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 9),
    _ArrisRouterLanClientLeaseEnd_Type()
)
arrisRouterLanClientLeaseEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientLeaseEnd.setStatus("current")
_ArrisRouterLanClientRowStatus_Type = RowStatus
_ArrisRouterLanClientRowStatus_Object = MibTableColumn
arrisRouterLanClientRowStatus = _ArrisRouterLanClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 13),
    _ArrisRouterLanClientRowStatus_Type()
)
arrisRouterLanClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanClientRowStatus.setStatus("current")


class _ArrisRouterLanClientOnline_Type(Integer32):
    """Custom type arrisRouterLanClientOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1))
    )


_ArrisRouterLanClientOnline_Type.__name__ = "Integer32"
_ArrisRouterLanClientOnline_Object = MibTableColumn
arrisRouterLanClientOnline = _ArrisRouterLanClientOnline_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 14),
    _ArrisRouterLanClientOnline_Type()
)
arrisRouterLanClientOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientOnline.setStatus("current")
_ArrisRouterLanClientComment_Type = DisplayString
_ArrisRouterLanClientComment_Object = MibTableColumn
arrisRouterLanClientComment = _ArrisRouterLanClientComment_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 15),
    _ArrisRouterLanClientComment_Type()
)
arrisRouterLanClientComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanClientComment.setStatus("deprecated")


class _ArrisRouterLanClientManufacturerOUI_Type(DisplayString):
    """Custom type arrisRouterLanClientManufacturerOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_ArrisRouterLanClientManufacturerOUI_Type.__name__ = "DisplayString"
_ArrisRouterLanClientManufacturerOUI_Object = MibTableColumn
arrisRouterLanClientManufacturerOUI = _ArrisRouterLanClientManufacturerOUI_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 17),
    _ArrisRouterLanClientManufacturerOUI_Type()
)
arrisRouterLanClientManufacturerOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientManufacturerOUI.setStatus("current")


class _ArrisRouterLanClientSerialNumber_Type(DisplayString):
    """Custom type arrisRouterLanClientSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanClientSerialNumber_Type.__name__ = "DisplayString"
_ArrisRouterLanClientSerialNumber_Object = MibTableColumn
arrisRouterLanClientSerialNumber = _ArrisRouterLanClientSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 18),
    _ArrisRouterLanClientSerialNumber_Type()
)
arrisRouterLanClientSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientSerialNumber.setStatus("current")


class _ArrisRouterLanClientProductClass_Type(DisplayString):
    """Custom type arrisRouterLanClientProductClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanClientProductClass_Type.__name__ = "DisplayString"
_ArrisRouterLanClientProductClass_Object = MibTableColumn
arrisRouterLanClientProductClass = _ArrisRouterLanClientProductClass_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 19),
    _ArrisRouterLanClientProductClass_Type()
)
arrisRouterLanClientProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientProductClass.setStatus("current")


class _ArrisRouterLanClientDeviceName_Type(DisplayString):
    """Custom type arrisRouterLanClientDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanClientDeviceName_Type.__name__ = "DisplayString"
_ArrisRouterLanClientDeviceName_Object = MibTableColumn
arrisRouterLanClientDeviceName = _ArrisRouterLanClientDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 20),
    _ArrisRouterLanClientDeviceName_Type()
)
arrisRouterLanClientDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientDeviceName.setStatus("current")
_ArrisRouterLanClientLastChange_Type = Integer32
_ArrisRouterLanClientLastChange_Object = MibTableColumn
arrisRouterLanClientLastChange = _ArrisRouterLanClientLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 24),
    _ArrisRouterLanClientLastChange_Type()
)
arrisRouterLanClientLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientLastChange.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanClientLastChange.setUnits("seconds")
_ArrisRouterLanClientTimeConnected_Type = Integer32
_ArrisRouterLanClientTimeConnected_Object = MibTableColumn
arrisRouterLanClientTimeConnected = _ArrisRouterLanClientTimeConnected_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 2, 1, 25),
    _ArrisRouterLanClientTimeConnected_Type()
)
arrisRouterLanClientTimeConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientTimeConnected.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanClientTimeConnected.setUnits("seconds")
_ArrisRouterDeviceUpDownTable_Object = MibTable
arrisRouterDeviceUpDownTable = _ArrisRouterDeviceUpDownTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownTable.setStatus("current")
_ArrisRouterDeviceUpDownEntry_Object = MibTableRow
arrisRouterDeviceUpDownEntry = _ArrisRouterDeviceUpDownEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3, 1)
)
arrisRouterDeviceUpDownEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterDeviceUpDownIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownEntry.setStatus("current")


class _ArrisRouterDeviceUpDownIndex_Type(Integer32):
    """Custom type arrisRouterDeviceUpDownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisRouterDeviceUpDownIndex_Type.__name__ = "Integer32"
_ArrisRouterDeviceUpDownIndex_Object = MibTableColumn
arrisRouterDeviceUpDownIndex = _ArrisRouterDeviceUpDownIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3, 1, 1),
    _ArrisRouterDeviceUpDownIndex_Type()
)
arrisRouterDeviceUpDownIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownIndex.setStatus("current")
_ArrisRouterDeviceUpDownMAC_Type = MacAddress
_ArrisRouterDeviceUpDownMAC_Object = MibTableColumn
arrisRouterDeviceUpDownMAC = _ArrisRouterDeviceUpDownMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3, 1, 2),
    _ArrisRouterDeviceUpDownMAC_Type()
)
arrisRouterDeviceUpDownMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownMAC.setStatus("current")
_ArrisRouterDeviceUpDownIPType_Type = InetAddressType
_ArrisRouterDeviceUpDownIPType_Object = MibTableColumn
arrisRouterDeviceUpDownIPType = _ArrisRouterDeviceUpDownIPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3, 1, 3),
    _ArrisRouterDeviceUpDownIPType_Type()
)
arrisRouterDeviceUpDownIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownIPType.setStatus("current")
_ArrisRouterDeviceUpDownStatus_Type = RowStatus
_ArrisRouterDeviceUpDownStatus_Object = MibTableColumn
arrisRouterDeviceUpDownStatus = _ArrisRouterDeviceUpDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 3, 1, 7),
    _ArrisRouterDeviceUpDownStatus_Type()
)
arrisRouterDeviceUpDownStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterDeviceUpDownStatus.setStatus("current")
_ArrisRouterLanCustomCount_Type = Unsigned32
_ArrisRouterLanCustomCount_Object = MibScalar
arrisRouterLanCustomCount = _ArrisRouterLanCustomCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 4),
    _ArrisRouterLanCustomCount_Type()
)
arrisRouterLanCustomCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanCustomCount.setStatus("current")
_ArrisRouterLanCustomTable_Object = MibTable
arrisRouterLanCustomTable = _ArrisRouterLanCustomTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    arrisRouterLanCustomTable.setStatus("current")
_ArrisRouterLanCustomEntry_Object = MibTableRow
arrisRouterLanCustomEntry = _ArrisRouterLanCustomEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1)
)
arrisRouterLanCustomEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanCustomIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanCustomEntry.setStatus("current")
_ArrisRouterLanCustomIdx_Type = Unsigned32
_ArrisRouterLanCustomIdx_Object = MibTableColumn
arrisRouterLanCustomIdx = _ArrisRouterLanCustomIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 1),
    _ArrisRouterLanCustomIdx_Type()
)
arrisRouterLanCustomIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanCustomIdx.setStatus("current")
_ArrisRouterLanCustomMAC_Type = MacAddress
_ArrisRouterLanCustomMAC_Object = MibTableColumn
arrisRouterLanCustomMAC = _ArrisRouterLanCustomMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 2),
    _ArrisRouterLanCustomMAC_Type()
)
arrisRouterLanCustomMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomMAC.setStatus("current")
_ArrisRouterLanCustomIPAddrType_Type = InetAddressType
_ArrisRouterLanCustomIPAddrType_Object = MibTableColumn
arrisRouterLanCustomIPAddrType = _ArrisRouterLanCustomIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 3),
    _ArrisRouterLanCustomIPAddrType_Type()
)
arrisRouterLanCustomIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomIPAddrType.setStatus("current")
_ArrisRouterLanCustomIPAddr_Type = InetAddress
_ArrisRouterLanCustomIPAddr_Object = MibTableColumn
arrisRouterLanCustomIPAddr = _ArrisRouterLanCustomIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 4),
    _ArrisRouterLanCustomIPAddr_Type()
)
arrisRouterLanCustomIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomIPAddr.setStatus("current")


class _ArrisRouterLanCustomFriendName_Type(DisplayString):
    """Custom type arrisRouterLanCustomFriendName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanCustomFriendName_Type.__name__ = "DisplayString"
_ArrisRouterLanCustomFriendName_Object = MibTableColumn
arrisRouterLanCustomFriendName = _ArrisRouterLanCustomFriendName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 5),
    _ArrisRouterLanCustomFriendName_Type()
)
arrisRouterLanCustomFriendName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomFriendName.setStatus("current")


class _ArrisRouterLanCustomHostName_Type(DisplayString):
    """Custom type arrisRouterLanCustomHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanCustomHostName_Type.__name__ = "DisplayString"
_ArrisRouterLanCustomHostName_Object = MibTableColumn
arrisRouterLanCustomHostName = _ArrisRouterLanCustomHostName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 6),
    _ArrisRouterLanCustomHostName_Type()
)
arrisRouterLanCustomHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomHostName.setStatus("current")


class _ArrisRouterLanCustomMACMfg_Type(DisplayString):
    """Custom type arrisRouterLanCustomMACMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanCustomMACMfg_Type.__name__ = "DisplayString"
_ArrisRouterLanCustomMACMfg_Object = MibTableColumn
arrisRouterLanCustomMACMfg = _ArrisRouterLanCustomMACMfg_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 7),
    _ArrisRouterLanCustomMACMfg_Type()
)
arrisRouterLanCustomMACMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanCustomMACMfg.setStatus("current")
_ArrisRouterLanCustomComments_Type = DisplayString
_ArrisRouterLanCustomComments_Object = MibTableColumn
arrisRouterLanCustomComments = _ArrisRouterLanCustomComments_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 8),
    _ArrisRouterLanCustomComments_Type()
)
arrisRouterLanCustomComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomComments.setStatus("current")
_ArrisRouterLanCustomRowStatus_Type = RowStatus
_ArrisRouterLanCustomRowStatus_Object = MibTableColumn
arrisRouterLanCustomRowStatus = _ArrisRouterLanCustomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 5, 1, 9),
    _ArrisRouterLanCustomRowStatus_Type()
)
arrisRouterLanCustomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanCustomRowStatus.setStatus("current")
_ArrisRouterLanClientDHCPOptionsTable_Object = MibTable
arrisRouterLanClientDHCPOptionsTable = _ArrisRouterLanClientDHCPOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8)
)
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsTable.setStatus("current")
_ArrisRouterLanClientDHCPOptionsEntry_Object = MibTableRow
arrisRouterLanClientDHCPOptionsEntry = _ArrisRouterLanClientDHCPOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8, 1)
)
arrisRouterLanClientDHCPOptionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanClientIPAddrType"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanClientIPAddr"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanClientDHCPOptionsIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsEntry.setStatus("current")


class _ArrisRouterLanClientDHCPOptionsIdx_Type(Unsigned32):
    """Custom type arrisRouterLanClientDHCPOptionsIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ArrisRouterLanClientDHCPOptionsIdx_Type.__name__ = "Unsigned32"
_ArrisRouterLanClientDHCPOptionsIdx_Object = MibTableColumn
arrisRouterLanClientDHCPOptionsIdx = _ArrisRouterLanClientDHCPOptionsIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8, 1, 1),
    _ArrisRouterLanClientDHCPOptionsIdx_Type()
)
arrisRouterLanClientDHCPOptionsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsIdx.setStatus("current")


class _ArrisRouterLanClientDHCPOptionsTag_Type(Unsigned32):
    """Custom type arrisRouterLanClientDHCPOptionsTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ArrisRouterLanClientDHCPOptionsTag_Type.__name__ = "Unsigned32"
_ArrisRouterLanClientDHCPOptionsTag_Object = MibTableColumn
arrisRouterLanClientDHCPOptionsTag = _ArrisRouterLanClientDHCPOptionsTag_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8, 1, 2),
    _ArrisRouterLanClientDHCPOptionsTag_Type()
)
arrisRouterLanClientDHCPOptionsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsTag.setStatus("current")


class _ArrisRouterLanClientDHCPOptionsValue_Type(DisplayString):
    """Custom type arrisRouterLanClientDHCPOptionsValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanClientDHCPOptionsValue_Type.__name__ = "DisplayString"
_ArrisRouterLanClientDHCPOptionsValue_Object = MibTableColumn
arrisRouterLanClientDHCPOptionsValue = _ArrisRouterLanClientDHCPOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8, 1, 3),
    _ArrisRouterLanClientDHCPOptionsValue_Type()
)
arrisRouterLanClientDHCPOptionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsValue.setStatus("current")
_ArrisRouterLanClientDHCPOptionsRowStatus_Type = RowStatus
_ArrisRouterLanClientDHCPOptionsRowStatus_Object = MibTableColumn
arrisRouterLanClientDHCPOptionsRowStatus = _ArrisRouterLanClientDHCPOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 4, 8, 1, 4),
    _ArrisRouterLanClientDHCPOptionsRowStatus_Type()
)
arrisRouterLanClientDHCPOptionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanClientDHCPOptionsRowStatus.setStatus("current")
_ArrisRouterRIPObjects_ObjectIdentity = ObjectIdentity
arrisRouterRIPObjects = _ArrisRouterRIPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5)
)
_ArrisRouterRIPEnable_Type = TruthValue
_ArrisRouterRIPEnable_Object = MibScalar
arrisRouterRIPEnable = _ArrisRouterRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 1),
    _ArrisRouterRIPEnable_Type()
)
arrisRouterRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPEnable.setStatus("current")


class _ArrisRouterRIPAuthEnable_Type(Integer32):
    """Custom type arrisRouterRIPAuthEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("disable", 0),
          ("textAuth", 1),
          ("md5Auth", 2))
    )


_ArrisRouterRIPAuthEnable_Type.__name__ = "Integer32"
_ArrisRouterRIPAuthEnable_Object = MibScalar
arrisRouterRIPAuthEnable = _ArrisRouterRIPAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 2),
    _ArrisRouterRIPAuthEnable_Type()
)
arrisRouterRIPAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPAuthEnable.setStatus("current")


class _ArrisRouterRIPReportTime_Type(Unsigned32):
    """Custom type arrisRouterRIPReportTime based on Unsigned32"""
    defaultValue = 30


_ArrisRouterRIPReportTime_Type.__name__ = "Unsigned32"
_ArrisRouterRIPReportTime_Object = MibScalar
arrisRouterRIPReportTime = _ArrisRouterRIPReportTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 3),
    _ArrisRouterRIPReportTime_Type()
)
arrisRouterRIPReportTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPReportTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterRIPReportTime.setUnits("seconds")


class _ArrisRouterRIPAuthKeyString_Type(DisplayString):
    """Custom type arrisRouterRIPAuthKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrisRouterRIPAuthKeyString_Type.__name__ = "DisplayString"
_ArrisRouterRIPAuthKeyString_Object = MibScalar
arrisRouterRIPAuthKeyString = _ArrisRouterRIPAuthKeyString_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 4),
    _ArrisRouterRIPAuthKeyString_Type()
)
arrisRouterRIPAuthKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPAuthKeyString.setStatus("current")


class _ArrisRouterRIPAuthKeyID_Type(Integer32):
    """Custom type arrisRouterRIPAuthKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterRIPAuthKeyID_Type.__name__ = "Integer32"
_ArrisRouterRIPAuthKeyID_Object = MibScalar
arrisRouterRIPAuthKeyID = _ArrisRouterRIPAuthKeyID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 5),
    _ArrisRouterRIPAuthKeyID_Type()
)
arrisRouterRIPAuthKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPAuthKeyID.setStatus("current")
_ArrisRouterRIPIPAddrType_Type = InetAddressType
_ArrisRouterRIPIPAddrType_Object = MibScalar
arrisRouterRIPIPAddrType = _ArrisRouterRIPIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 6),
    _ArrisRouterRIPIPAddrType_Type()
)
arrisRouterRIPIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPIPAddrType.setStatus("current")
_ArrisRouterRIPIPAddr_Type = InetAddress
_ArrisRouterRIPIPAddr_Object = MibScalar
arrisRouterRIPIPAddr = _ArrisRouterRIPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 7),
    _ArrisRouterRIPIPAddr_Type()
)
arrisRouterRIPIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPIPAddr.setStatus("current")
_ArrisRouterRIPPrefixLen_Type = InetAddressPrefixLength
_ArrisRouterRIPPrefixLen_Object = MibScalar
arrisRouterRIPPrefixLen = _ArrisRouterRIPPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 8),
    _ArrisRouterRIPPrefixLen_Type()
)
arrisRouterRIPPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPPrefixLen.setStatus("current")


class _ArrisRouterRIPAuthKeyChain_Type(DisplayString):
    """Custom type arrisRouterRIPAuthKeyChain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterRIPAuthKeyChain_Type.__name__ = "DisplayString"
_ArrisRouterRIPAuthKeyChain_Object = MibScalar
arrisRouterRIPAuthKeyChain = _ArrisRouterRIPAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 9),
    _ArrisRouterRIPAuthKeyChain_Type()
)
arrisRouterRIPAuthKeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPAuthKeyChain.setStatus("current")
_ArrisRouterRIPRoutedSubnetIPType_Type = InetAddressType
_ArrisRouterRIPRoutedSubnetIPType_Object = MibScalar
arrisRouterRIPRoutedSubnetIPType = _ArrisRouterRIPRoutedSubnetIPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 10),
    _ArrisRouterRIPRoutedSubnetIPType_Type()
)
arrisRouterRIPRoutedSubnetIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetIPType.setStatus("current")
_ArrisRouterRIPRoutedSubnetIP_Type = InetAddress
_ArrisRouterRIPRoutedSubnetIP_Object = MibScalar
arrisRouterRIPRoutedSubnetIP = _ArrisRouterRIPRoutedSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 11),
    _ArrisRouterRIPRoutedSubnetIP_Type()
)
arrisRouterRIPRoutedSubnetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetIP.setStatus("current")


class _ArrisRouterRIPRoutedSubnetGWNetIPType_Type(InetAddressType):
    """Custom type arrisRouterRIPRoutedSubnetGWNetIPType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterRIPRoutedSubnetGWNetIPType_Type.__name__ = "InetAddressType"
_ArrisRouterRIPRoutedSubnetGWNetIPType_Object = MibScalar
arrisRouterRIPRoutedSubnetGWNetIPType = _ArrisRouterRIPRoutedSubnetGWNetIPType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 12),
    _ArrisRouterRIPRoutedSubnetGWNetIPType_Type()
)
arrisRouterRIPRoutedSubnetGWNetIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetGWNetIPType.setStatus("current")
_ArrisRouterRIPRoutedSubnetGWNetIP_Type = InetAddress
_ArrisRouterRIPRoutedSubnetGWNetIP_Object = MibScalar
arrisRouterRIPRoutedSubnetGWNetIP = _ArrisRouterRIPRoutedSubnetGWNetIP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 13),
    _ArrisRouterRIPRoutedSubnetGWNetIP_Type()
)
arrisRouterRIPRoutedSubnetGWNetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetGWNetIP.setStatus("current")
_ArrisRouterRIPRoutedSubnetMask_Type = InetAddress
_ArrisRouterRIPRoutedSubnetMask_Object = MibScalar
arrisRouterRIPRoutedSubnetMask = _ArrisRouterRIPRoutedSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 14),
    _ArrisRouterRIPRoutedSubnetMask_Type()
)
arrisRouterRIPRoutedSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetMask.setStatus("current")
_ArrisRouterRIPRoutedSubnetEnabled_Type = TruthValue
_ArrisRouterRIPRoutedSubnetEnabled_Object = MibScalar
arrisRouterRIPRoutedSubnetEnabled = _ArrisRouterRIPRoutedSubnetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 15),
    _ArrisRouterRIPRoutedSubnetEnabled_Type()
)
arrisRouterRIPRoutedSubnetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetEnabled.setStatus("current")


class _ArrisRouterRIPSendCMInterface_Type(TruthValue):
    """Custom type arrisRouterRIPSendCMInterface based on TruthValue"""
    defaultValue = 2


_ArrisRouterRIPSendCMInterface_Type.__name__ = "TruthValue"
_ArrisRouterRIPSendCMInterface_Object = MibScalar
arrisRouterRIPSendCMInterface = _ArrisRouterRIPSendCMInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 16),
    _ArrisRouterRIPSendCMInterface_Type()
)
arrisRouterRIPSendCMInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPSendCMInterface.setStatus("current")


class _ArrisRouterRIPRoutedSubnetDHCP_Type(TruthValue):
    """Custom type arrisRouterRIPRoutedSubnetDHCP based on TruthValue"""
    defaultValue = 2


_ArrisRouterRIPRoutedSubnetDHCP_Type.__name__ = "TruthValue"
_ArrisRouterRIPRoutedSubnetDHCP_Object = MibScalar
arrisRouterRIPRoutedSubnetDHCP = _ArrisRouterRIPRoutedSubnetDHCP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 17),
    _ArrisRouterRIPRoutedSubnetDHCP_Type()
)
arrisRouterRIPRoutedSubnetDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetDHCP.setStatus("current")


class _ArrisRouterRIPRoutedSubnetNAT_Type(TruthValue):
    """Custom type arrisRouterRIPRoutedSubnetNAT based on TruthValue"""
    defaultValue = 2


_ArrisRouterRIPRoutedSubnetNAT_Type.__name__ = "TruthValue"
_ArrisRouterRIPRoutedSubnetNAT_Object = MibScalar
arrisRouterRIPRoutedSubnetNAT = _ArrisRouterRIPRoutedSubnetNAT_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 5, 18),
    _ArrisRouterRIPRoutedSubnetNAT_Type()
)
arrisRouterRIPRoutedSubnetNAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPRoutedSubnetNAT.setStatus("current")


class _ArrisRouterLanSettings_Type(Integer32):
    """Custom type arrisRouterLanSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("applyPrimaryLan", 1),
          ("applyGuestLans", 2),
          ("applyAllLans", 3),
          ("revertSettings", 10),
          ("resetDefaults", 11),
          ("restartWLAN", 12))
    )


_ArrisRouterLanSettings_Type.__name__ = "Integer32"
_ArrisRouterLanSettings_Object = MibScalar
arrisRouterLanSettings = _ArrisRouterLanSettings_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 6),
    _ArrisRouterLanSettings_Type()
)
arrisRouterLanSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanSettings.setStatus("current")
_ArrisRouterLanEtherPortTable_Object = MibTable
arrisRouterLanEtherPortTable = _ArrisRouterLanEtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortTable.setStatus("current")
_ArrisRouterLanEtherPortEntry_Object = MibTableRow
arrisRouterLanEtherPortEntry = _ArrisRouterLanEtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1)
)
arrisRouterLanEtherPortEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanEtherPortIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortEntry.setStatus("current")
_ArrisRouterLanEtherPortIdx_Type = Unsigned32
_ArrisRouterLanEtherPortIdx_Object = MibTableColumn
arrisRouterLanEtherPortIdx = _ArrisRouterLanEtherPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 1),
    _ArrisRouterLanEtherPortIdx_Type()
)
arrisRouterLanEtherPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortIdx.setStatus("current")
_ArrisRouterLanEtherPortIFIndex_Type = Integer32
_ArrisRouterLanEtherPortIFIndex_Object = MibTableColumn
arrisRouterLanEtherPortIFIndex = _ArrisRouterLanEtherPortIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 2),
    _ArrisRouterLanEtherPortIFIndex_Type()
)
arrisRouterLanEtherPortIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortIFIndex.setStatus("current")


class _ArrisRouterLanEtherPortEnabled_Type(Integer32):
    """Custom type arrisRouterLanEtherPortEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterLanEtherPortEnabled_Type.__name__ = "Integer32"
_ArrisRouterLanEtherPortEnabled_Object = MibTableColumn
arrisRouterLanEtherPortEnabled = _ArrisRouterLanEtherPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 3),
    _ArrisRouterLanEtherPortEnabled_Type()
)
arrisRouterLanEtherPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortEnabled.setStatus("current")


class _ArrisRouterLanEtherPortDuplex_Type(Integer32):
    """Custom type arrisRouterLanEtherPortDuplex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1))
    )


_ArrisRouterLanEtherPortDuplex_Type.__name__ = "Integer32"
_ArrisRouterLanEtherPortDuplex_Object = MibTableColumn
arrisRouterLanEtherPortDuplex = _ArrisRouterLanEtherPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 4),
    _ArrisRouterLanEtherPortDuplex_Type()
)
arrisRouterLanEtherPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortDuplex.setStatus("current")
_ArrisRouterLanEtherPortSpeed_Type = Integer32
_ArrisRouterLanEtherPortSpeed_Object = MibTableColumn
arrisRouterLanEtherPortSpeed = _ArrisRouterLanEtherPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 5),
    _ArrisRouterLanEtherPortSpeed_Type()
)
arrisRouterLanEtherPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortSpeed.setStatus("current")


class _ArrisRouterLanEtherPortAuto_Type(Integer32):
    """Custom type arrisRouterLanEtherPortAuto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manualConfigure", 0),
          ("autoNegotiate", 1))
    )


_ArrisRouterLanEtherPortAuto_Type.__name__ = "Integer32"
_ArrisRouterLanEtherPortAuto_Object = MibTableColumn
arrisRouterLanEtherPortAuto = _ArrisRouterLanEtherPortAuto_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 6),
    _ArrisRouterLanEtherPortAuto_Type()
)
arrisRouterLanEtherPortAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortAuto.setStatus("current")
_ArrisRouterLanEtherPortHasLink_Type = TruthValue
_ArrisRouterLanEtherPortHasLink_Object = MibTableColumn
arrisRouterLanEtherPortHasLink = _ArrisRouterLanEtherPortHasLink_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 8, 1, 7),
    _ArrisRouterLanEtherPortHasLink_Type()
)
arrisRouterLanEtherPortHasLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanEtherPortHasLink.setStatus("current")
_ArrisRouterRIPngObjects_ObjectIdentity = ObjectIdentity
arrisRouterRIPngObjects = _ArrisRouterRIPngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9)
)
_ArrisRouterRIPngEnable_Type = TruthValue
_ArrisRouterRIPngEnable_Object = MibScalar
arrisRouterRIPngEnable = _ArrisRouterRIPngEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 1),
    _ArrisRouterRIPngEnable_Type()
)
arrisRouterRIPngEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngEnable.setStatus("current")
_ArrisRouterRIPngAddr_Type = InetAddressIPv6
_ArrisRouterRIPngAddr_Object = MibScalar
arrisRouterRIPngAddr = _ArrisRouterRIPngAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 2),
    _ArrisRouterRIPngAddr_Type()
)
arrisRouterRIPngAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngAddr.setStatus("current")
_ArrisRouterRIPngSubnetEnable_Type = TruthValue
_ArrisRouterRIPngSubnetEnable_Object = MibScalar
arrisRouterRIPngSubnetEnable = _ArrisRouterRIPngSubnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 3),
    _ArrisRouterRIPngSubnetEnable_Type()
)
arrisRouterRIPngSubnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngSubnetEnable.setStatus("current")
_ArrisRouterRIPngRoutedSubnetAddr_Type = InetAddressIPv6
_ArrisRouterRIPngRoutedSubnetAddr_Object = MibScalar
arrisRouterRIPngRoutedSubnetAddr = _ArrisRouterRIPngRoutedSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 4),
    _ArrisRouterRIPngRoutedSubnetAddr_Type()
)
arrisRouterRIPngRoutedSubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngRoutedSubnetAddr.setStatus("current")


class _ArrisRouterRIPngRoutedSubnetPrefixLength_Type(Integer32):
    """Custom type arrisRouterRIPngRoutedSubnetPrefixLength based on Integer32"""
    defaultValue = 64


_ArrisRouterRIPngRoutedSubnetPrefixLength_Type.__name__ = "Integer32"
_ArrisRouterRIPngRoutedSubnetPrefixLength_Object = MibScalar
arrisRouterRIPngRoutedSubnetPrefixLength = _ArrisRouterRIPngRoutedSubnetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 5),
    _ArrisRouterRIPngRoutedSubnetPrefixLength_Type()
)
arrisRouterRIPngRoutedSubnetPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngRoutedSubnetPrefixLength.setStatus("current")


class _ArrisRouterRIPngSendCMInterface_Type(TruthValue):
    """Custom type arrisRouterRIPngSendCMInterface based on TruthValue"""
    defaultValue = 2


_ArrisRouterRIPngSendCMInterface_Type.__name__ = "TruthValue"
_ArrisRouterRIPngSendCMInterface_Object = MibScalar
arrisRouterRIPngSendCMInterface = _ArrisRouterRIPngSendCMInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 9, 6),
    _ArrisRouterRIPngSendCMInterface_Type()
)
arrisRouterRIPngSendCMInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRIPngSendCMInterface.setStatus("current")
_ArrisRouterLanSrvDHCPOptionsTable_Object = MibTable
arrisRouterLanSrvDHCPOptionsTable = _ArrisRouterLanSrvDHCPOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11)
)
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsTable.setStatus("current")
_ArrisRouterLanSrvDHCPOptionsEntry_Object = MibTableRow
arrisRouterLanSrvDHCPOptionsEntry = _ArrisRouterLanSrvDHCPOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1)
)
arrisRouterLanSrvDHCPOptionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanSrvDHCPOptionsIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsEntry.setStatus("current")
_ArrisRouterLanSrvDHCPOptionsIdx_Type = Unsigned32
_ArrisRouterLanSrvDHCPOptionsIdx_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsIdx = _ArrisRouterLanSrvDHCPOptionsIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 1),
    _ArrisRouterLanSrvDHCPOptionsIdx_Type()
)
arrisRouterLanSrvDHCPOptionsIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsIdx.setStatus("current")


class _ArrisRouterLanSrvDHCPOptionsEnable_Type(TruthValue):
    """Custom type arrisRouterLanSrvDHCPOptionsEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterLanSrvDHCPOptionsEnable_Type.__name__ = "TruthValue"
_ArrisRouterLanSrvDHCPOptionsEnable_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsEnable = _ArrisRouterLanSrvDHCPOptionsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 2),
    _ArrisRouterLanSrvDHCPOptionsEnable_Type()
)
arrisRouterLanSrvDHCPOptionsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsEnable.setStatus("current")
_ArrisRouterLanSrvDHCPOptionsIPAddrType_Type = InetAddressType
_ArrisRouterLanSrvDHCPOptionsIPAddrType_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsIPAddrType = _ArrisRouterLanSrvDHCPOptionsIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 3),
    _ArrisRouterLanSrvDHCPOptionsIPAddrType_Type()
)
arrisRouterLanSrvDHCPOptionsIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsIPAddrType.setStatus("current")


class _ArrisRouterLanSrvDHCPOptionsTag_Type(Unsigned32):
    """Custom type arrisRouterLanSrvDHCPOptionsTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ArrisRouterLanSrvDHCPOptionsTag_Type.__name__ = "Unsigned32"
_ArrisRouterLanSrvDHCPOptionsTag_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsTag = _ArrisRouterLanSrvDHCPOptionsTag_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 4),
    _ArrisRouterLanSrvDHCPOptionsTag_Type()
)
arrisRouterLanSrvDHCPOptionsTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsTag.setStatus("current")


class _ArrisRouterLanSrvDHCPOptionsValue_Type(DisplayString):
    """Custom type arrisRouterLanSrvDHCPOptionsValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanSrvDHCPOptionsValue_Type.__name__ = "DisplayString"
_ArrisRouterLanSrvDHCPOptionsValue_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsValue = _ArrisRouterLanSrvDHCPOptionsValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 5),
    _ArrisRouterLanSrvDHCPOptionsValue_Type()
)
arrisRouterLanSrvDHCPOptionsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsValue.setStatus("current")
_ArrisRouterLanSrvDHCPOptionsRowStatus_Type = RowStatus
_ArrisRouterLanSrvDHCPOptionsRowStatus_Object = MibTableColumn
arrisRouterLanSrvDHCPOptionsRowStatus = _ArrisRouterLanSrvDHCPOptionsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 11, 1, 6),
    _ArrisRouterLanSrvDHCPOptionsRowStatus_Type()
)
arrisRouterLanSrvDHCPOptionsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanSrvDHCPOptionsRowStatus.setStatus("current")


class _ArrisRouterLanMaxIPv6RAInterval_Type(Unsigned32):
    """Custom type arrisRouterLanMaxIPv6RAInterval based on Unsigned32"""
    defaultValue = 3


_ArrisRouterLanMaxIPv6RAInterval_Type.__name__ = "Unsigned32"
_ArrisRouterLanMaxIPv6RAInterval_Object = MibScalar
arrisRouterLanMaxIPv6RAInterval = _ArrisRouterLanMaxIPv6RAInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 13),
    _ArrisRouterLanMaxIPv6RAInterval_Type()
)
arrisRouterLanMaxIPv6RAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanMaxIPv6RAInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanMaxIPv6RAInterval.setUnits("seconds")


class _ArrisRouterLanMinIPv6RAInterval_Type(Unsigned32):
    """Custom type arrisRouterLanMinIPv6RAInterval based on Unsigned32"""
    defaultValue = 3


_ArrisRouterLanMinIPv6RAInterval_Type.__name__ = "Unsigned32"
_ArrisRouterLanMinIPv6RAInterval_Object = MibScalar
arrisRouterLanMinIPv6RAInterval = _ArrisRouterLanMinIPv6RAInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 14),
    _ArrisRouterLanMinIPv6RAInterval_Type()
)
arrisRouterLanMinIPv6RAInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanMinIPv6RAInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanMinIPv6RAInterval.setUnits("seconds")


class _ArrisRouterLanBridgeType_Type(Integer32):
    """Custom type arrisRouterLanBridgeType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("subnetBridge", 0),
          ("fullBridge", 1))
    )


_ArrisRouterLanBridgeType_Type.__name__ = "Integer32"
_ArrisRouterLanBridgeType_Object = MibScalar
arrisRouterLanBridgeType = _ArrisRouterLanBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 15),
    _ArrisRouterLanBridgeType_Type()
)
arrisRouterLanBridgeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanBridgeType.setStatus("current")
_ArrisRouterLanUSBPortTable_Object = MibTable
arrisRouterLanUSBPortTable = _ArrisRouterLanUSBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16)
)
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortTable.setStatus("current")
_ArrisRouterLanUSBPortEntry_Object = MibTableRow
arrisRouterLanUSBPortEntry = _ArrisRouterLanUSBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1)
)
arrisRouterLanUSBPortEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanUSBPortIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortEntry.setStatus("current")


class _ArrisRouterLanUSBPortIdx_Type(Unsigned32):
    """Custom type arrisRouterLanUSBPortIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ArrisRouterLanUSBPortIdx_Type.__name__ = "Unsigned32"
_ArrisRouterLanUSBPortIdx_Object = MibTableColumn
arrisRouterLanUSBPortIdx = _ArrisRouterLanUSBPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 1),
    _ArrisRouterLanUSBPortIdx_Type()
)
arrisRouterLanUSBPortIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortIdx.setStatus("current")
_ArrisRouterLanUSBPortHasLink_Type = TruthValue
_ArrisRouterLanUSBPortHasLink_Object = MibTableColumn
arrisRouterLanUSBPortHasLink = _ArrisRouterLanUSBPortHasLink_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 2),
    _ArrisRouterLanUSBPortHasLink_Type()
)
arrisRouterLanUSBPortHasLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortHasLink.setStatus("current")


class _ArrisRouterLanUSBPortDescr_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanUSBPortDescr_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortDescr_Object = MibTableColumn
arrisRouterLanUSBPortDescr = _ArrisRouterLanUSBPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 3),
    _ArrisRouterLanUSBPortDescr_Type()
)
arrisRouterLanUSBPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortDescr.setStatus("current")


class _ArrisRouterLanUSBPortSerialNum_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanUSBPortSerialNum_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortSerialNum_Object = MibTableColumn
arrisRouterLanUSBPortSerialNum = _ArrisRouterLanUSBPortSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 4),
    _ArrisRouterLanUSBPortSerialNum_Type()
)
arrisRouterLanUSBPortSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortSerialNum.setStatus("current")
_ArrisRouterLanUSBPortSpeed_Type = Integer32
_ArrisRouterLanUSBPortSpeed_Object = MibTableColumn
arrisRouterLanUSBPortSpeed = _ArrisRouterLanUSBPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 5),
    _ArrisRouterLanUSBPortSpeed_Type()
)
arrisRouterLanUSBPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortSpeed.setUnits("Mbps")


class _ArrisRouterLanUSBPortManuf_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortManuf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterLanUSBPortManuf_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortManuf_Object = MibTableColumn
arrisRouterLanUSBPortManuf = _ArrisRouterLanUSBPortManuf_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 6),
    _ArrisRouterLanUSBPortManuf_Type()
)
arrisRouterLanUSBPortManuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortManuf.setStatus("current")


class _ArrisRouterLanUSBPortStorageNam_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortStorageNam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanUSBPortStorageNam_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortStorageNam_Object = MibTableColumn
arrisRouterLanUSBPortStorageNam = _ArrisRouterLanUSBPortStorageNam_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 7),
    _ArrisRouterLanUSBPortStorageNam_Type()
)
arrisRouterLanUSBPortStorageNam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortStorageNam.setStatus("current")


class _ArrisRouterLanUSBPortFileSys_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortFileSys based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanUSBPortFileSys_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortFileSys_Object = MibTableColumn
arrisRouterLanUSBPortFileSys = _ArrisRouterLanUSBPortFileSys_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 8),
    _ArrisRouterLanUSBPortFileSys_Type()
)
arrisRouterLanUSBPortFileSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortFileSys.setStatus("current")


class _ArrisRouterLanUSBPortSpaceAvail_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortSpaceAvail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanUSBPortSpaceAvail_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortSpaceAvail_Object = MibTableColumn
arrisRouterLanUSBPortSpaceAvail = _ArrisRouterLanUSBPortSpaceAvail_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 9),
    _ArrisRouterLanUSBPortSpaceAvail_Type()
)
arrisRouterLanUSBPortSpaceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortSpaceAvail.setStatus("current")


class _ArrisRouterLanUSBPortTotalSpace_Type(DisplayString):
    """Custom type arrisRouterLanUSBPortTotalSpace based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanUSBPortTotalSpace_Type.__name__ = "DisplayString"
_ArrisRouterLanUSBPortTotalSpace_Object = MibTableColumn
arrisRouterLanUSBPortTotalSpace = _ArrisRouterLanUSBPortTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 10),
    _ArrisRouterLanUSBPortTotalSpace_Type()
)
arrisRouterLanUSBPortTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortTotalSpace.setStatus("current")


class _ArrisRouterLanUsbPortFoldersFile_Type(DisplayString):
    """Custom type arrisRouterLanUsbPortFoldersFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterLanUsbPortFoldersFile_Type.__name__ = "DisplayString"
_ArrisRouterLanUsbPortFoldersFile_Object = MibTableColumn
arrisRouterLanUsbPortFoldersFile = _ArrisRouterLanUsbPortFoldersFile_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 11),
    _ArrisRouterLanUsbPortFoldersFile_Type()
)
arrisRouterLanUsbPortFoldersFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterLanUsbPortFoldersFile.setStatus("current")
_ArrisRouterLanUSBPortDelStorage_Type = TruthValue
_ArrisRouterLanUSBPortDelStorage_Object = MibTableColumn
arrisRouterLanUSBPortDelStorage = _ArrisRouterLanUSBPortDelStorage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 16, 1, 12),
    _ArrisRouterLanUSBPortDelStorage_Type()
)
arrisRouterLanUSBPortDelStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanUSBPortDelStorage.setStatus("current")
_ArrisRouterLanFileSharingObjs_ObjectIdentity = ObjectIdentity
arrisRouterLanFileSharingObjs = _ArrisRouterLanFileSharingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17)
)


class _ArrisRouterLanFilesharingEnable_Type(TruthValue):
    """Custom type arrisRouterLanFilesharingEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterLanFilesharingEnable_Type.__name__ = "TruthValue"
_ArrisRouterLanFilesharingEnable_Object = MibScalar
arrisRouterLanFilesharingEnable = _ArrisRouterLanFilesharingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 1),
    _ArrisRouterLanFilesharingEnable_Type()
)
arrisRouterLanFilesharingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingEnable.setStatus("current")


class _ArrisRouterLanFilesharingDevName_Type(DisplayString):
    """Custom type arrisRouterLanFilesharingDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanFilesharingDevName_Type.__name__ = "DisplayString"
_ArrisRouterLanFilesharingDevName_Object = MibScalar
arrisRouterLanFilesharingDevName = _ArrisRouterLanFilesharingDevName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 2),
    _ArrisRouterLanFilesharingDevName_Type()
)
arrisRouterLanFilesharingDevName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingDevName.setStatus("current")
_ArrisRouterLanFileSharingTable_Object = MibTable
arrisRouterLanFileSharingTable = _ArrisRouterLanFileSharingTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3)
)
if mibBuilder.loadTexts:
    arrisRouterLanFileSharingTable.setStatus("current")
_ArrisRouterLanFileSharingEntry_Object = MibTableRow
arrisRouterLanFileSharingEntry = _ArrisRouterLanFileSharingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1)
)
arrisRouterLanFileSharingEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanFilesharingIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanFileSharingEntry.setStatus("current")


class _ArrisRouterLanFilesharingIdx_Type(Unsigned32):
    """Custom type arrisRouterLanFilesharingIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ArrisRouterLanFilesharingIdx_Type.__name__ = "Unsigned32"
_ArrisRouterLanFilesharingIdx_Object = MibTableColumn
arrisRouterLanFilesharingIdx = _ArrisRouterLanFilesharingIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 1),
    _ArrisRouterLanFilesharingIdx_Type()
)
arrisRouterLanFilesharingIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingIdx.setStatus("current")
_ArrisRouterLanFilesharingRowStatus_Type = RowStatus
_ArrisRouterLanFilesharingRowStatus_Object = MibTableColumn
arrisRouterLanFilesharingRowStatus = _ArrisRouterLanFilesharingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 2),
    _ArrisRouterLanFilesharingRowStatus_Type()
)
arrisRouterLanFilesharingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingRowStatus.setStatus("current")


class _ArrisRouterLanFilesharingUsbPort_Type(Unsigned32):
    """Custom type arrisRouterLanFilesharingUsbPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ArrisRouterLanFilesharingUsbPort_Type.__name__ = "Unsigned32"
_ArrisRouterLanFilesharingUsbPort_Object = MibTableColumn
arrisRouterLanFilesharingUsbPort = _ArrisRouterLanFilesharingUsbPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 3),
    _ArrisRouterLanFilesharingUsbPort_Type()
)
arrisRouterLanFilesharingUsbPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingUsbPort.setStatus("current")


class _ArrisRouterLanFilesharingDirectory_Type(DisplayString):
    """Custom type arrisRouterLanFilesharingDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterLanFilesharingDirectory_Type.__name__ = "DisplayString"
_ArrisRouterLanFilesharingDirectory_Object = MibTableColumn
arrisRouterLanFilesharingDirectory = _ArrisRouterLanFilesharingDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 4),
    _ArrisRouterLanFilesharingDirectory_Type()
)
arrisRouterLanFilesharingDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingDirectory.setStatus("current")


class _ArrisRouterLanFilesharingName_Type(DisplayString):
    """Custom type arrisRouterLanFilesharingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanFilesharingName_Type.__name__ = "DisplayString"
_ArrisRouterLanFilesharingName_Object = MibTableColumn
arrisRouterLanFilesharingName = _ArrisRouterLanFilesharingName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 5),
    _ArrisRouterLanFilesharingName_Type()
)
arrisRouterLanFilesharingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingName.setStatus("current")


class _ArrisRouterLanFilesharingEnableHttp_Type(TruthValue):
    """Custom type arrisRouterLanFilesharingEnableHttp based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanFilesharingEnableHttp_Type.__name__ = "TruthValue"
_ArrisRouterLanFilesharingEnableHttp_Object = MibTableColumn
arrisRouterLanFilesharingEnableHttp = _ArrisRouterLanFilesharingEnableHttp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 6),
    _ArrisRouterLanFilesharingEnableHttp_Type()
)
arrisRouterLanFilesharingEnableHttp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingEnableHttp.setStatus("current")


class _ArrisRouterLanFilesharingEnableFtp_Type(TruthValue):
    """Custom type arrisRouterLanFilesharingEnableFtp based on TruthValue"""
    defaultValue = 2


_ArrisRouterLanFilesharingEnableFtp_Type.__name__ = "TruthValue"
_ArrisRouterLanFilesharingEnableFtp_Object = MibTableColumn
arrisRouterLanFilesharingEnableFtp = _ArrisRouterLanFilesharingEnableFtp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 7),
    _ArrisRouterLanFilesharingEnableFtp_Type()
)
arrisRouterLanFilesharingEnableFtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingEnableFtp.setStatus("current")


class _ArrisRouterLanFilesharingVisibility_Type(TruthValue):
    """Custom type arrisRouterLanFilesharingVisibility based on TruthValue"""
    defaultValue = 1


_ArrisRouterLanFilesharingVisibility_Type.__name__ = "TruthValue"
_ArrisRouterLanFilesharingVisibility_Object = MibTableColumn
arrisRouterLanFilesharingVisibility = _ArrisRouterLanFilesharingVisibility_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 8),
    _ArrisRouterLanFilesharingVisibility_Type()
)
arrisRouterLanFilesharingVisibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingVisibility.setStatus("current")


class _ArrisRouterLanFilesharingEveryOnePerm_Type(Integer32):
    """Custom type arrisRouterLanFilesharingEveryOnePerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 0),
          ("readOnly", 1),
          ("writeOnly", 2),
          ("readandWrite", 3))
    )


_ArrisRouterLanFilesharingEveryOnePerm_Type.__name__ = "Integer32"
_ArrisRouterLanFilesharingEveryOnePerm_Object = MibTableColumn
arrisRouterLanFilesharingEveryOnePerm = _ArrisRouterLanFilesharingEveryOnePerm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 9),
    _ArrisRouterLanFilesharingEveryOnePerm_Type()
)
arrisRouterLanFilesharingEveryOnePerm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingEveryOnePerm.setStatus("current")


class _ArrisRouterLanFilesharingDesc_Type(DisplayString):
    """Custom type arrisRouterLanFilesharingDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisRouterLanFilesharingDesc_Type.__name__ = "DisplayString"
_ArrisRouterLanFilesharingDesc_Object = MibTableColumn
arrisRouterLanFilesharingDesc = _ArrisRouterLanFilesharingDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 3, 1, 10),
    _ArrisRouterLanFilesharingDesc_Type()
)
arrisRouterLanFilesharingDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingDesc.setStatus("current")
_ArrisRouterLanLocalUserTable_Object = MibTable
arrisRouterLanLocalUserTable = _ArrisRouterLanLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4)
)
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserTable.setStatus("current")
_ArrisRouterLanLocalUserEntry_Object = MibTableRow
arrisRouterLanLocalUserEntry = _ArrisRouterLanLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4, 1)
)
arrisRouterLanLocalUserEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanLocalUserIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserEntry.setStatus("current")


class _ArrisRouterLanLocalUserIdx_Type(Unsigned32):
    """Custom type arrisRouterLanLocalUserIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ArrisRouterLanLocalUserIdx_Type.__name__ = "Unsigned32"
_ArrisRouterLanLocalUserIdx_Object = MibTableColumn
arrisRouterLanLocalUserIdx = _ArrisRouterLanLocalUserIdx_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4, 1, 1),
    _ArrisRouterLanLocalUserIdx_Type()
)
arrisRouterLanLocalUserIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserIdx.setStatus("current")
_ArrisRouterLanLocalUserRowStatus_Type = RowStatus
_ArrisRouterLanLocalUserRowStatus_Object = MibTableColumn
arrisRouterLanLocalUserRowStatus = _ArrisRouterLanLocalUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4, 1, 2),
    _ArrisRouterLanLocalUserRowStatus_Type()
)
arrisRouterLanLocalUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserRowStatus.setStatus("current")


class _ArrisRouterLanLocalUserName_Type(DisplayString):
    """Custom type arrisRouterLanLocalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanLocalUserName_Type.__name__ = "DisplayString"
_ArrisRouterLanLocalUserName_Object = MibTableColumn
arrisRouterLanLocalUserName = _ArrisRouterLanLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4, 1, 3),
    _ArrisRouterLanLocalUserName_Type()
)
arrisRouterLanLocalUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserName.setStatus("current")


class _ArrisRouterLanLocalUserPasswd_Type(DisplayString):
    """Custom type arrisRouterLanLocalUserPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanLocalUserPasswd_Type.__name__ = "DisplayString"
_ArrisRouterLanLocalUserPasswd_Object = MibTableColumn
arrisRouterLanLocalUserPasswd = _ArrisRouterLanLocalUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 4, 1, 4),
    _ArrisRouterLanLocalUserPasswd_Type()
)
arrisRouterLanLocalUserPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanLocalUserPasswd.setStatus("current")
_ArrisRouterLanFilesharingPermitTable_Object = MibTable
arrisRouterLanFilesharingPermitTable = _ArrisRouterLanFilesharingPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 5)
)
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingPermitTable.setStatus("current")
_ArrisRouterLanFilesharingPermitEntry_Object = MibTableRow
arrisRouterLanFilesharingPermitEntry = _ArrisRouterLanFilesharingPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 5, 1)
)
arrisRouterLanFilesharingPermitEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanFilesharingIdx"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterLanLocalUserIdx"),
)
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingPermitEntry.setStatus("current")


class _ArrisRouterLanFilesharingPermitvalue_Type(Integer32):
    """Custom type arrisRouterLanFilesharingPermitvalue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 0),
          ("readOnly", 1),
          ("writeOnly", 2),
          ("readandWrite", 3))
    )


_ArrisRouterLanFilesharingPermitvalue_Type.__name__ = "Integer32"
_ArrisRouterLanFilesharingPermitvalue_Object = MibTableColumn
arrisRouterLanFilesharingPermitvalue = _ArrisRouterLanFilesharingPermitvalue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 17, 5, 1, 1),
    _ArrisRouterLanFilesharingPermitvalue_Type()
)
arrisRouterLanFilesharingPermitvalue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterLanFilesharingPermitvalue.setStatus("current")


class _ArrisRouterLanIPv6RALifetime_Type(Unsigned32):
    """Custom type arrisRouterLanIPv6RALifetime based on Unsigned32"""
    defaultValue = 1800


_ArrisRouterLanIPv6RALifetime_Type.__name__ = "Unsigned32"
_ArrisRouterLanIPv6RALifetime_Object = MibScalar
arrisRouterLanIPv6RALifetime = _ArrisRouterLanIPv6RALifetime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 2, 19),
    _ArrisRouterLanIPv6RALifetime_Type()
)
arrisRouterLanIPv6RALifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanIPv6RALifetime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterLanIPv6RALifetime.setUnits("seconds")
_ArrisRouterWirelessCfg_ObjectIdentity = ObjectIdentity
arrisRouterWirelessCfg = _ArrisRouterWirelessCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3)
)


class _ArrisRouterWiFiCountry_Type(DisplayString):
    """Custom type arrisRouterWiFiCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ArrisRouterWiFiCountry_Type.__name__ = "DisplayString"
_ArrisRouterWiFiCountry_Object = MibScalar
arrisRouterWiFiCountry = _ArrisRouterWiFiCountry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 1),
    _ArrisRouterWiFiCountry_Type()
)
arrisRouterWiFiCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiCountry.setStatus("current")


class _ArrisRouterWiFiChannel_Type(Unsigned32):
    """Custom type arrisRouterWiFiChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
    )


_ArrisRouterWiFiChannel_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiChannel_Object = MibScalar
arrisRouterWiFiChannel = _ArrisRouterWiFiChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 2),
    _ArrisRouterWiFiChannel_Type()
)
arrisRouterWiFiChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiChannel.setStatus("current")


class _ArrisRouterWiFiMode_Type(Integer32):
    """Custom type arrisRouterWiFiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              4,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("mixBG", 0),
          ("bOnly", 1),
          ("gOnly", 4),
          ("nOnly", 6),
          ("mixGN", 7),
          ("mixBGN", 9))
    )


_ArrisRouterWiFiMode_Type.__name__ = "Integer32"
_ArrisRouterWiFiMode_Object = MibScalar
arrisRouterWiFiMode = _ArrisRouterWiFiMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 3),
    _ArrisRouterWiFiMode_Type()
)
arrisRouterWiFiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiMode.setStatus("current")


class _ArrisRouterWiFiBGProtect_Type(TruthValue):
    """Custom type arrisRouterWiFiBGProtect based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiBGProtect_Type.__name__ = "TruthValue"
_ArrisRouterWiFiBGProtect_Object = MibScalar
arrisRouterWiFiBGProtect = _ArrisRouterWiFiBGProtect_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 4),
    _ArrisRouterWiFiBGProtect_Type()
)
arrisRouterWiFiBGProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBGProtect.setStatus("current")


class _ArrisRouterWiFiBeaconInterval_Type(Unsigned32):
    """Custom type arrisRouterWiFiBeaconInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterWiFiBeaconInterval_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiBeaconInterval_Object = MibScalar
arrisRouterWiFiBeaconInterval = _ArrisRouterWiFiBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 5),
    _ArrisRouterWiFiBeaconInterval_Type()
)
arrisRouterWiFiBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiBeaconInterval.setUnits("milliseconds")


class _ArrisRouterWiFiDTIMInterval_Type(Unsigned32):
    """Custom type arrisRouterWiFiDTIMInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFiDTIMInterval_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiDTIMInterval_Object = MibScalar
arrisRouterWiFiDTIMInterval = _ArrisRouterWiFiDTIMInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 6),
    _ArrisRouterWiFiDTIMInterval_Type()
)
arrisRouterWiFiDTIMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiDTIMInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiDTIMInterval.setUnits("milliseconds")


class _ArrisRouterWiFiTxPreamble_Type(Integer32):
    """Custom type arrisRouterWiFiTxPreamble based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("long", 0),
          ("short", 1))
    )


_ArrisRouterWiFiTxPreamble_Type.__name__ = "Integer32"
_ArrisRouterWiFiTxPreamble_Object = MibScalar
arrisRouterWiFiTxPreamble = _ArrisRouterWiFiTxPreamble_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 7),
    _ArrisRouterWiFiTxPreamble_Type()
)
arrisRouterWiFiTxPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiTxPreamble.setStatus("current")


class _ArrisRouterWiFiRTSThreshold_Type(Unsigned32):
    """Custom type arrisRouterWiFiRTSThreshold based on Unsigned32"""
    defaultValue = 2347

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_ArrisRouterWiFiRTSThreshold_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiRTSThreshold_Object = MibScalar
arrisRouterWiFiRTSThreshold = _ArrisRouterWiFiRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 8),
    _ArrisRouterWiFiRTSThreshold_Type()
)
arrisRouterWiFiRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiRTSThreshold.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiRTSThreshold.setUnits("bytes")


class _ArrisRouterWiFiFragmentThresh_Type(Unsigned32):
    """Custom type arrisRouterWiFiFragmentThresh based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_ArrisRouterWiFiFragmentThresh_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiFragmentThresh_Object = MibScalar
arrisRouterWiFiFragmentThresh = _ArrisRouterWiFiFragmentThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 9),
    _ArrisRouterWiFiFragmentThresh_Type()
)
arrisRouterWiFiFragmentThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiFragmentThresh.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiFragmentThresh.setUnits("bytes")


class _ArrisRouterWiFiShortSlot_Type(TruthValue):
    """Custom type arrisRouterWiFiShortSlot based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFiShortSlot_Type.__name__ = "TruthValue"
_ArrisRouterWiFiShortSlot_Object = MibScalar
arrisRouterWiFiShortSlot = _ArrisRouterWiFiShortSlot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 10),
    _ArrisRouterWiFiShortSlot_Type()
)
arrisRouterWiFiShortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiShortSlot.setStatus("current")


class _ArrisRouterWiFiFrameBurst_Type(TruthValue):
    """Custom type arrisRouterWiFiFrameBurst based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFiFrameBurst_Type.__name__ = "TruthValue"
_ArrisRouterWiFiFrameBurst_Object = MibScalar
arrisRouterWiFiFrameBurst = _ArrisRouterWiFiFrameBurst_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 11),
    _ArrisRouterWiFiFrameBurst_Type()
)
arrisRouterWiFiFrameBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiFrameBurst.setStatus("current")


class _ArrisRouterWiFiEnableRadio_Type(TruthValue):
    """Custom type arrisRouterWiFiEnableRadio based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFiEnableRadio_Type.__name__ = "TruthValue"
_ArrisRouterWiFiEnableRadio_Object = MibScalar
arrisRouterWiFiEnableRadio = _ArrisRouterWiFiEnableRadio_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 12),
    _ArrisRouterWiFiEnableRadio_Type()
)
arrisRouterWiFiEnableRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiEnableRadio.setStatus("current")


class _ArrisRouterWiFiShortRetryLimit_Type(Integer32):
    """Custom type arrisRouterWiFiShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFiShortRetryLimit_Type.__name__ = "Integer32"
_ArrisRouterWiFiShortRetryLimit_Object = MibScalar
arrisRouterWiFiShortRetryLimit = _ArrisRouterWiFiShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 14),
    _ArrisRouterWiFiShortRetryLimit_Type()
)
arrisRouterWiFiShortRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiShortRetryLimit.setStatus("current")


class _ArrisRouterWiFiLongRetryLimit_Type(Integer32):
    """Custom type arrisRouterWiFiLongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFiLongRetryLimit_Type.__name__ = "Integer32"
_ArrisRouterWiFiLongRetryLimit_Object = MibScalar
arrisRouterWiFiLongRetryLimit = _ArrisRouterWiFiLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 15),
    _ArrisRouterWiFiLongRetryLimit_Type()
)
arrisRouterWiFiLongRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiLongRetryLimit.setStatus("current")


class _ArrisRouterWiFiOutputPower_Type(Integer32):
    """Custom type arrisRouterWiFiOutputPower based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("percent12", 12),
          ("percent25", 25),
          ("percent50", 50),
          ("percent75", 75),
          ("percent100", 100))
    )


_ArrisRouterWiFiOutputPower_Type.__name__ = "Integer32"
_ArrisRouterWiFiOutputPower_Object = MibScalar
arrisRouterWiFiOutputPower = _ArrisRouterWiFiOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 16),
    _ArrisRouterWiFiOutputPower_Type()
)
arrisRouterWiFiOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiOutputPower.setStatus("current")
_ArrisRouterWiFi80211NSettings_ObjectIdentity = ObjectIdentity
arrisRouterWiFi80211NSettings = _ArrisRouterWiFi80211NSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21)
)


class _ArrisRouterWiFi80211NBand_Type(Integer32):
    """Custom type arrisRouterWiFi80211NBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("band24G", 1),
          ("band5G", 2))
    )


_ArrisRouterWiFi80211NBand_Type.__name__ = "Integer32"
_ArrisRouterWiFi80211NBand_Object = MibScalar
arrisRouterWiFi80211NBand = _ArrisRouterWiFi80211NBand_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 1),
    _ArrisRouterWiFi80211NBand_Type()
)
arrisRouterWiFi80211NBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi80211NBand.setStatus("current")


class _ArrisRouterWiFiHTMCS_Type(Integer32):
    """Custom type arrisRouterWiFiHTMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("legacy", 1),
          ("mcs0", 2),
          ("mcs1", 3),
          ("mcs2", 4),
          ("mcs3", 5),
          ("mcs4", 6),
          ("mcs5", 7),
          ("mcs6", 8),
          ("mcs7", 9),
          ("mcs8", 10),
          ("mcs9", 11),
          ("mcs10", 12),
          ("mcs11", 13),
          ("mcs12", 14),
          ("mcs13", 15),
          ("mcs14", 16),
          ("mcs15", 17),
          ("mcs16", 18),
          ("mcs17", 19),
          ("mcs18", 20),
          ("mcs19", 21),
          ("mcs20", 22),
          ("mcs21", 23),
          ("mcs22", 24),
          ("mcs23", 25))
    )


_ArrisRouterWiFiHTMCS_Type.__name__ = "Integer32"
_ArrisRouterWiFiHTMCS_Object = MibScalar
arrisRouterWiFiHTMCS = _ArrisRouterWiFiHTMCS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 2),
    _ArrisRouterWiFiHTMCS_Type()
)
arrisRouterWiFiHTMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiHTMCS.setStatus("current")


class _ArrisRouterWiFiChannelBW_Type(Integer32):
    """Custom type arrisRouterWiFiChannelBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("width20MHz", 0),
          ("width40MHz", 1),
          ("width20and40Mhz", 2))
    )


_ArrisRouterWiFiChannelBW_Type.__name__ = "Integer32"
_ArrisRouterWiFiChannelBW_Object = MibScalar
arrisRouterWiFiChannelBW = _ArrisRouterWiFiChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 3),
    _ArrisRouterWiFiChannelBW_Type()
)
arrisRouterWiFiChannelBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiChannelBW.setStatus("current")


class _ArrisRouterWiFi80211NSideBand_Type(Integer32):
    """Custom type arrisRouterWiFi80211NSideBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("upper", 1),
          ("lower", 2))
    )


_ArrisRouterWiFi80211NSideBand_Type.__name__ = "Integer32"
_ArrisRouterWiFi80211NSideBand_Object = MibScalar
arrisRouterWiFi80211NSideBand = _ArrisRouterWiFi80211NSideBand_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 4),
    _ArrisRouterWiFi80211NSideBand_Type()
)
arrisRouterWiFi80211NSideBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi80211NSideBand.setStatus("current")


class _ArrisRouterWiFiHTMode_Type(Integer32):
    """Custom type arrisRouterWiFiHTMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 0),
          ("greenField", 1))
    )


_ArrisRouterWiFiHTMode_Type.__name__ = "Integer32"
_ArrisRouterWiFiHTMode_Object = MibScalar
arrisRouterWiFiHTMode = _ArrisRouterWiFiHTMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 5),
    _ArrisRouterWiFiHTMode_Type()
)
arrisRouterWiFiHTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiHTMode.setStatus("current")


class _ArrisRouterWiFiGuardInterval_Type(Integer32):
    """Custom type arrisRouterWiFiGuardInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gi400", 0),
          ("gi800", 1),
          ("auto", 2))
    )


_ArrisRouterWiFiGuardInterval_Type.__name__ = "Integer32"
_ArrisRouterWiFiGuardInterval_Object = MibScalar
arrisRouterWiFiGuardInterval = _ArrisRouterWiFiGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 6),
    _ArrisRouterWiFiGuardInterval_Type()
)
arrisRouterWiFiGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiGuardInterval.setStatus("current")


class _ArrisRouterWiFiDeclinePeerBA_Type(TruthValue):
    """Custom type arrisRouterWiFiDeclinePeerBA based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiDeclinePeerBA_Type.__name__ = "TruthValue"
_ArrisRouterWiFiDeclinePeerBA_Object = MibScalar
arrisRouterWiFiDeclinePeerBA = _ArrisRouterWiFiDeclinePeerBA_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 8),
    _ArrisRouterWiFiDeclinePeerBA_Type()
)
arrisRouterWiFiDeclinePeerBA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiDeclinePeerBA.setStatus("current")


class _ArrisRouterWiFiBlockAck_Type(TruthValue):
    """Custom type arrisRouterWiFiBlockAck based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiBlockAck_Type.__name__ = "TruthValue"
_ArrisRouterWiFiBlockAck_Object = MibScalar
arrisRouterWiFiBlockAck = _ArrisRouterWiFiBlockAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 9),
    _ArrisRouterWiFiBlockAck_Type()
)
arrisRouterWiFiBlockAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBlockAck.setStatus("current")


class _ArrisRouterWiFiNProtection_Type(Integer32):
    """Custom type arrisRouterWiFiNProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("auto", 1))
    )


_ArrisRouterWiFiNProtection_Type.__name__ = "Integer32"
_ArrisRouterWiFiNProtection_Object = MibScalar
arrisRouterWiFiNProtection = _ArrisRouterWiFiNProtection_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 10),
    _ArrisRouterWiFiNProtection_Type()
)
arrisRouterWiFiNProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiNProtection.setStatus("current")


class _ArrisRouterWiFiAllow40MHzOnlyOperation_Type(TruthValue):
    """Custom type arrisRouterWiFiAllow40MHzOnlyOperation based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiAllow40MHzOnlyOperation_Type.__name__ = "TruthValue"
_ArrisRouterWiFiAllow40MHzOnlyOperation_Object = MibScalar
arrisRouterWiFiAllow40MHzOnlyOperation = _ArrisRouterWiFiAllow40MHzOnlyOperation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 21, 11),
    _ArrisRouterWiFiAllow40MHzOnlyOperation_Type()
)
arrisRouterWiFiAllow40MHzOnlyOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiAllow40MHzOnlyOperation.setStatus("current")
_ArrisRouterBSSTable_Object = MibTable
arrisRouterBSSTable = _ArrisRouterBSSTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22)
)
if mibBuilder.loadTexts:
    arrisRouterBSSTable.setStatus("current")
_ArrisRouterBSSEntry_Object = MibTableRow
arrisRouterBSSEntry = _ArrisRouterBSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1)
)
arrisRouterBSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterBSSEntry.setStatus("current")
_ArrisRouterBssID_Type = PhysAddress
_ArrisRouterBssID_Object = MibTableColumn
arrisRouterBssID = _ArrisRouterBssID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 1),
    _ArrisRouterBssID_Type()
)
arrisRouterBssID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBssID.setStatus("current")


class _ArrisRouterBssSSID_Type(DisplayString):
    """Custom type arrisRouterBssSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrisRouterBssSSID_Type.__name__ = "DisplayString"
_ArrisRouterBssSSID_Object = MibTableColumn
arrisRouterBssSSID = _ArrisRouterBssSSID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 2),
    _ArrisRouterBssSSID_Type()
)
arrisRouterBssSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssSSID.setStatus("current")


class _ArrisRouterBssActive_Type(TruthValue):
    """Custom type arrisRouterBssActive based on TruthValue"""
    defaultValue = 2


_ArrisRouterBssActive_Type.__name__ = "TruthValue"
_ArrisRouterBssActive_Object = MibTableColumn
arrisRouterBssActive = _ArrisRouterBssActive_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 3),
    _ArrisRouterBssActive_Type()
)
arrisRouterBssActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssActive.setStatus("current")


class _ArrisRouterBssSSIDBroadcast_Type(TruthValue):
    """Custom type arrisRouterBssSSIDBroadcast based on TruthValue"""
    defaultValue = 1


_ArrisRouterBssSSIDBroadcast_Type.__name__ = "TruthValue"
_ArrisRouterBssSSIDBroadcast_Object = MibTableColumn
arrisRouterBssSSIDBroadcast = _ArrisRouterBssSSIDBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 4),
    _ArrisRouterBssSSIDBroadcast_Type()
)
arrisRouterBssSSIDBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssSSIDBroadcast.setStatus("current")


class _ArrisRouterBssSecurityMode_Type(Integer32):
    """Custom type arrisRouterBssSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("wep", 1),
          ("wpaPsk", 2),
          ("wpa2Psk", 3),
          ("wpaEnterprise", 4),
          ("wpa2Enterprise", 5),
          ("wepEnterprise", 6),
          ("wpaWpa2Psk", 7),
          ("wpaWpa2Enterprise", 8))
    )


_ArrisRouterBssSecurityMode_Type.__name__ = "Integer32"
_ArrisRouterBssSecurityMode_Object = MibTableColumn
arrisRouterBssSecurityMode = _ArrisRouterBssSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 5),
    _ArrisRouterBssSecurityMode_Type()
)
arrisRouterBssSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssSecurityMode.setStatus("current")


class _ArrisRouterBssAccessMode_Type(Integer32):
    """Custom type arrisRouterBssAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allowAny", 1),
          ("allowList", 2),
          ("denyList", 3))
    )


_ArrisRouterBssAccessMode_Type.__name__ = "Integer32"
_ArrisRouterBssAccessMode_Object = MibTableColumn
arrisRouterBssAccessMode = _ArrisRouterBssAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 6),
    _ArrisRouterBssAccessMode_Type()
)
arrisRouterBssAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssAccessMode.setStatus("current")


class _ArrisRouterBssNetworkIsolate_Type(TruthValue):
    """Custom type arrisRouterBssNetworkIsolate based on TruthValue"""
    defaultValue = 2


_ArrisRouterBssNetworkIsolate_Type.__name__ = "TruthValue"
_ArrisRouterBssNetworkIsolate_Object = MibTableColumn
arrisRouterBssNetworkIsolate = _ArrisRouterBssNetworkIsolate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 7),
    _ArrisRouterBssNetworkIsolate_Type()
)
arrisRouterBssNetworkIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssNetworkIsolate.setStatus("current")
_ArrisRouterBssMACAccessCount_Type = Unsigned32
_ArrisRouterBssMACAccessCount_Object = MibTableColumn
arrisRouterBssMACAccessCount = _ArrisRouterBssMACAccessCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 8),
    _ArrisRouterBssMACAccessCount_Type()
)
arrisRouterBssMACAccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBssMACAccessCount.setStatus("current")


class _ArrisRouterBssMACAccessClear_Type(Integer32):
    """Custom type arrisRouterBssMACAccessClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ArrisRouterBssMACAccessClear_Type.__name__ = "Integer32"
_ArrisRouterBssMACAccessClear_Object = MibTableColumn
arrisRouterBssMACAccessClear = _ArrisRouterBssMACAccessClear_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 9),
    _ArrisRouterBssMACAccessClear_Type()
)
arrisRouterBssMACAccessClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssMACAccessClear.setStatus("current")
_ArrisRouterBSSArpAuditInterval_Type = Unsigned32
_ArrisRouterBSSArpAuditInterval_Object = MibTableColumn
arrisRouterBSSArpAuditInterval = _ArrisRouterBSSArpAuditInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 10),
    _ArrisRouterBSSArpAuditInterval_Type()
)
arrisRouterBSSArpAuditInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBSSArpAuditInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterBSSArpAuditInterval.setUnits("seconds")


class _ArrisRouterBssMaxWifiClients_Type(Integer32):
    """Custom type arrisRouterBssMaxWifiClients based on Integer32"""
    defaultValue = 0


_ArrisRouterBssMaxWifiClients_Type.__name__ = "Integer32"
_ArrisRouterBssMaxWifiClients_Object = MibTableColumn
arrisRouterBssMaxWifiClients = _ArrisRouterBssMaxWifiClients_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 11),
    _ArrisRouterBssMaxWifiClients_Type()
)
arrisRouterBssMaxWifiClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssMaxWifiClients.setStatus("current")


class _ArrisRouterBssWmmEnable_Type(TruthValue):
    """Custom type arrisRouterBssWmmEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterBssWmmEnable_Type.__name__ = "TruthValue"
_ArrisRouterBssWmmEnable_Object = MibTableColumn
arrisRouterBssWmmEnable = _ArrisRouterBssWmmEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 12),
    _ArrisRouterBssWmmEnable_Type()
)
arrisRouterBssWmmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssWmmEnable.setStatus("current")


class _ArrisRouterBssWmmAPSD_Type(TruthValue):
    """Custom type arrisRouterBssWmmAPSD based on TruthValue"""
    defaultValue = 1


_ArrisRouterBssWmmAPSD_Type.__name__ = "TruthValue"
_ArrisRouterBssWmmAPSD_Object = MibTableColumn
arrisRouterBssWmmAPSD = _ArrisRouterBssWmmAPSD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 13),
    _ArrisRouterBssWmmAPSD_Type()
)
arrisRouterBssWmmAPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssWmmAPSD.setStatus("current")


class _ArrisRouterBssActiveTimeout_Type(OctetString):
    """Custom type arrisRouterBssActiveTimeout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ArrisRouterBssActiveTimeout_Type.__name__ = "OctetString"
_ArrisRouterBssActiveTimeout_Object = MibTableColumn
arrisRouterBssActiveTimeout = _ArrisRouterBssActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 14),
    _ArrisRouterBssActiveTimeout_Type()
)
arrisRouterBssActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssActiveTimeout.setStatus("current")


class _ArrisRouterDefaultBssSSID_Type(DisplayString):
    """Custom type arrisRouterDefaultBssSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrisRouterDefaultBssSSID_Type.__name__ = "DisplayString"
_ArrisRouterDefaultBssSSID_Object = MibTableColumn
arrisRouterDefaultBssSSID = _ArrisRouterDefaultBssSSID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 15),
    _ArrisRouterDefaultBssSSID_Type()
)
arrisRouterDefaultBssSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDefaultBssSSID.setStatus("current")


class _ArrisRouterBssStaSteeringEnable_Type(TruthValue):
    """Custom type arrisRouterBssStaSteeringEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterBssStaSteeringEnable_Type.__name__ = "TruthValue"
_ArrisRouterBssStaSteeringEnable_Object = MibTableColumn
arrisRouterBssStaSteeringEnable = _ArrisRouterBssStaSteeringEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 22, 1, 16),
    _ArrisRouterBssStaSteeringEnable_Type()
)
arrisRouterBssStaSteeringEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringEnable.setStatus("current")
_ArrisRouterWEPTable_Object = MibTable
arrisRouterWEPTable = _ArrisRouterWEPTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 23)
)
if mibBuilder.loadTexts:
    arrisRouterWEPTable.setStatus("current")
_ArrisRouterWEPEntry_Object = MibTableRow
arrisRouterWEPEntry = _ArrisRouterWEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 23, 1)
)
arrisRouterWEPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWEPEntry.setStatus("current")
_ArrisRouterWEPCurrentKey_Type = Unsigned32
_ArrisRouterWEPCurrentKey_Object = MibTableColumn
arrisRouterWEPCurrentKey = _ArrisRouterWEPCurrentKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 23, 1, 1),
    _ArrisRouterWEPCurrentKey_Type()
)
arrisRouterWEPCurrentKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWEPCurrentKey.setStatus("current")


class _ArrisRouterWEPEncryptionMode_Type(Integer32):
    """Custom type arrisRouterWEPEncryptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wep64", 1),
          ("wep128", 2))
    )


_ArrisRouterWEPEncryptionMode_Type.__name__ = "Integer32"
_ArrisRouterWEPEncryptionMode_Object = MibTableColumn
arrisRouterWEPEncryptionMode = _ArrisRouterWEPEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 23, 1, 2),
    _ArrisRouterWEPEncryptionMode_Type()
)
arrisRouterWEPEncryptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWEPEncryptionMode.setStatus("current")
_ArrisRouterWEP64BitKeyTable_Object = MibTable
arrisRouterWEP64BitKeyTable = _ArrisRouterWEP64BitKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 24)
)
if mibBuilder.loadTexts:
    arrisRouterWEP64BitKeyTable.setStatus("current")
_ArrisRouterWEP64BitKeyEntry_Object = MibTableRow
arrisRouterWEP64BitKeyEntry = _ArrisRouterWEP64BitKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 24, 1)
)
arrisRouterWEP64BitKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWEP64BitKeyIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWEP64BitKeyEntry.setStatus("current")


class _ArrisRouterWEP64BitKeyIndex_Type(Integer32):
    """Custom type arrisRouterWEP64BitKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ArrisRouterWEP64BitKeyIndex_Type.__name__ = "Integer32"
_ArrisRouterWEP64BitKeyIndex_Object = MibTableColumn
arrisRouterWEP64BitKeyIndex = _ArrisRouterWEP64BitKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 24, 1, 1),
    _ArrisRouterWEP64BitKeyIndex_Type()
)
arrisRouterWEP64BitKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWEP64BitKeyIndex.setStatus("current")
_ArrisRouterWEP64BitKeyValue_Type = DisplayString
_ArrisRouterWEP64BitKeyValue_Object = MibTableColumn
arrisRouterWEP64BitKeyValue = _ArrisRouterWEP64BitKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 24, 1, 2),
    _ArrisRouterWEP64BitKeyValue_Type()
)
arrisRouterWEP64BitKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWEP64BitKeyValue.setStatus("current")
_ArrisRouterWEP64BitKeyStatus_Type = RowStatus
_ArrisRouterWEP64BitKeyStatus_Object = MibTableColumn
arrisRouterWEP64BitKeyStatus = _ArrisRouterWEP64BitKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 24, 1, 3),
    _ArrisRouterWEP64BitKeyStatus_Type()
)
arrisRouterWEP64BitKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWEP64BitKeyStatus.setStatus("current")
_ArrisRouterWEP128BitKeyTable_Object = MibTable
arrisRouterWEP128BitKeyTable = _ArrisRouterWEP128BitKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 25)
)
if mibBuilder.loadTexts:
    arrisRouterWEP128BitKeyTable.setStatus("current")
_ArrisRouterWEP128BitKeyEntry_Object = MibTableRow
arrisRouterWEP128BitKeyEntry = _ArrisRouterWEP128BitKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 25, 1)
)
arrisRouterWEP128BitKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWEP128BitKeyIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWEP128BitKeyEntry.setStatus("current")


class _ArrisRouterWEP128BitKeyIndex_Type(Integer32):
    """Custom type arrisRouterWEP128BitKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ArrisRouterWEP128BitKeyIndex_Type.__name__ = "Integer32"
_ArrisRouterWEP128BitKeyIndex_Object = MibTableColumn
arrisRouterWEP128BitKeyIndex = _ArrisRouterWEP128BitKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 25, 1, 1),
    _ArrisRouterWEP128BitKeyIndex_Type()
)
arrisRouterWEP128BitKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWEP128BitKeyIndex.setStatus("current")
_ArrisRouterWEP128BitKeyValue_Type = DisplayString
_ArrisRouterWEP128BitKeyValue_Object = MibTableColumn
arrisRouterWEP128BitKeyValue = _ArrisRouterWEP128BitKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 25, 1, 2),
    _ArrisRouterWEP128BitKeyValue_Type()
)
arrisRouterWEP128BitKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWEP128BitKeyValue.setStatus("current")
_ArrisRouterWEP128BitKeyStatus_Type = RowStatus
_ArrisRouterWEP128BitKeyStatus_Object = MibTableColumn
arrisRouterWEP128BitKeyStatus = _ArrisRouterWEP128BitKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 25, 1, 3),
    _ArrisRouterWEP128BitKeyStatus_Type()
)
arrisRouterWEP128BitKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWEP128BitKeyStatus.setStatus("current")
_ArrisRouterWPATable_Object = MibTable
arrisRouterWPATable = _ArrisRouterWPATable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26)
)
if mibBuilder.loadTexts:
    arrisRouterWPATable.setStatus("current")
_ArrisRouterWPAEntry_Object = MibTableRow
arrisRouterWPAEntry = _ArrisRouterWPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1)
)
arrisRouterWPAEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWPAEntry.setStatus("current")


class _ArrisRouterWPAAlgorithm_Type(Integer32):
    """Custom type arrisRouterWPAAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tkip", 1),
          ("aes", 2),
          ("tkipPlusAes", 3))
    )


_ArrisRouterWPAAlgorithm_Type.__name__ = "Integer32"
_ArrisRouterWPAAlgorithm_Object = MibTableColumn
arrisRouterWPAAlgorithm = _ArrisRouterWPAAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1, 1),
    _ArrisRouterWPAAlgorithm_Type()
)
arrisRouterWPAAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPAAlgorithm.setStatus("current")


class _ArrisRouterWPAPreSharedKey_Type(OctetString):
    """Custom type arrisRouterWPAPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_ArrisRouterWPAPreSharedKey_Type.__name__ = "OctetString"
_ArrisRouterWPAPreSharedKey_Object = MibTableColumn
arrisRouterWPAPreSharedKey = _ArrisRouterWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1, 2),
    _ArrisRouterWPAPreSharedKey_Type()
)
arrisRouterWPAPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPAPreSharedKey.setStatus("current")
_ArrisRouterWPAReAuthInterval_Type = Unsigned32
_ArrisRouterWPAReAuthInterval_Object = MibTableColumn
arrisRouterWPAReAuthInterval = _ArrisRouterWPAReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1, 4),
    _ArrisRouterWPAReAuthInterval_Type()
)
arrisRouterWPAReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPAReAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWPAReAuthInterval.setUnits("seconds")


class _ArrisRouterWPAPreAuthEnable_Type(TruthValue):
    """Custom type arrisRouterWPAPreAuthEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterWPAPreAuthEnable_Type.__name__ = "TruthValue"
_ArrisRouterWPAPreAuthEnable_Object = MibTableColumn
arrisRouterWPAPreAuthEnable = _ArrisRouterWPAPreAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1, 5),
    _ArrisRouterWPAPreAuthEnable_Type()
)
arrisRouterWPAPreAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPAPreAuthEnable.setStatus("current")


class _ArrisRouterDefaultWPAPreSharedKey_Type(OctetString):
    """Custom type arrisRouterDefaultWPAPreSharedKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_ArrisRouterDefaultWPAPreSharedKey_Type.__name__ = "OctetString"
_ArrisRouterDefaultWPAPreSharedKey_Object = MibTableColumn
arrisRouterDefaultWPAPreSharedKey = _ArrisRouterDefaultWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 26, 1, 6),
    _ArrisRouterDefaultWPAPreSharedKey_Type()
)
arrisRouterDefaultWPAPreSharedKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDefaultWPAPreSharedKey.setStatus("current")
_ArrisRouterRadiusTable_Object = MibTable
arrisRouterRadiusTable = _ArrisRouterRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27)
)
if mibBuilder.loadTexts:
    arrisRouterRadiusTable.setStatus("current")
_ArrisRouterRadiusEntry_Object = MibTableRow
arrisRouterRadiusEntry = _ArrisRouterRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1)
)
arrisRouterRadiusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterRadiusEntry.setStatus("current")
_ArrisRouterRadiusAddressType_Type = InetAddressType
_ArrisRouterRadiusAddressType_Object = MibTableColumn
arrisRouterRadiusAddressType = _ArrisRouterRadiusAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1, 1),
    _ArrisRouterRadiusAddressType_Type()
)
arrisRouterRadiusAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRadiusAddressType.setStatus("current")
_ArrisRouterRadiusAddress_Type = InetAddress
_ArrisRouterRadiusAddress_Object = MibTableColumn
arrisRouterRadiusAddress = _ArrisRouterRadiusAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1, 2),
    _ArrisRouterRadiusAddress_Type()
)
arrisRouterRadiusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRadiusAddress.setStatus("current")
_ArrisRouterRadiusPort_Type = Unsigned32
_ArrisRouterRadiusPort_Object = MibTableColumn
arrisRouterRadiusPort = _ArrisRouterRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1, 3),
    _ArrisRouterRadiusPort_Type()
)
arrisRouterRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRadiusPort.setStatus("current")


class _ArrisRouterRadiusKey_Type(DisplayString):
    """Custom type arrisRouterRadiusKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ArrisRouterRadiusKey_Type.__name__ = "DisplayString"
_ArrisRouterRadiusKey_Object = MibTableColumn
arrisRouterRadiusKey = _ArrisRouterRadiusKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1, 4),
    _ArrisRouterRadiusKey_Type()
)
arrisRouterRadiusKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRadiusKey.setStatus("current")
_ArrisRouterRadiusReAuthInterval_Type = Unsigned32
_ArrisRouterRadiusReAuthInterval_Object = MibTableColumn
arrisRouterRadiusReAuthInterval = _ArrisRouterRadiusReAuthInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 27, 1, 5),
    _ArrisRouterRadiusReAuthInterval_Type()
)
arrisRouterRadiusReAuthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRadiusReAuthInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterRadiusReAuthInterval.setUnits("seconds")
_ArrisRouterMACAccessTable_Object = MibTable
arrisRouterMACAccessTable = _ArrisRouterMACAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28)
)
if mibBuilder.loadTexts:
    arrisRouterMACAccessTable.setStatus("current")
_ArrisRouterMACAccessEntry_Object = MibTableRow
arrisRouterMACAccessEntry = _ArrisRouterMACAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28, 1)
)
arrisRouterMACAccessEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterMACAccessIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterMACAccessEntry.setStatus("current")


class _ArrisRouterMACAccessIndex_Type(Integer32):
    """Custom type arrisRouterMACAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ArrisRouterMACAccessIndex_Type.__name__ = "Integer32"
_ArrisRouterMACAccessIndex_Object = MibTableColumn
arrisRouterMACAccessIndex = _ArrisRouterMACAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28, 1, 1),
    _ArrisRouterMACAccessIndex_Type()
)
arrisRouterMACAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterMACAccessIndex.setStatus("current")
_ArrisRouterMACAccessAddr_Type = MacAddress
_ArrisRouterMACAccessAddr_Object = MibTableColumn
arrisRouterMACAccessAddr = _ArrisRouterMACAccessAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28, 1, 2),
    _ArrisRouterMACAccessAddr_Type()
)
arrisRouterMACAccessAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterMACAccessAddr.setStatus("current")
_ArrisRouterMACAccessStatus_Type = RowStatus
_ArrisRouterMACAccessStatus_Object = MibTableColumn
arrisRouterMACAccessStatus = _ArrisRouterMACAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28, 1, 3),
    _ArrisRouterMACAccessStatus_Type()
)
arrisRouterMACAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterMACAccessStatus.setStatus("current")
_ArrisRouterMACAccessDeviceName_Type = DisplayString
_ArrisRouterMACAccessDeviceName_Object = MibTableColumn
arrisRouterMACAccessDeviceName = _ArrisRouterMACAccessDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 28, 1, 4),
    _ArrisRouterMACAccessDeviceName_Type()
)
arrisRouterMACAccessDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterMACAccessDeviceName.setStatus("current")
_ArrisRouterWMMCfg_ObjectIdentity = ObjectIdentity
arrisRouterWMMCfg = _ArrisRouterWMMCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29)
)


class _ArrisRouterWMMEnable_Type(TruthValue):
    """Custom type arrisRouterWMMEnable based on TruthValue"""
    defaultValue = 1


_ArrisRouterWMMEnable_Type.__name__ = "TruthValue"
_ArrisRouterWMMEnable_Object = MibScalar
arrisRouterWMMEnable = _ArrisRouterWMMEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 1),
    _ArrisRouterWMMEnable_Type()
)
arrisRouterWMMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEnable.setStatus("current")


class _ArrisRouterWMMNoAck_Type(TruthValue):
    """Custom type arrisRouterWMMNoAck based on TruthValue"""
    defaultValue = 2


_ArrisRouterWMMNoAck_Type.__name__ = "TruthValue"
_ArrisRouterWMMNoAck_Object = MibScalar
arrisRouterWMMNoAck = _ArrisRouterWMMNoAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 2),
    _ArrisRouterWMMNoAck_Type()
)
arrisRouterWMMNoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMNoAck.setStatus("current")


class _ArrisRouterWMMAPSD_Type(TruthValue):
    """Custom type arrisRouterWMMAPSD based on TruthValue"""
    defaultValue = 1


_ArrisRouterWMMAPSD_Type.__name__ = "TruthValue"
_ArrisRouterWMMAPSD_Object = MibScalar
arrisRouterWMMAPSD = _ArrisRouterWMMAPSD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 3),
    _ArrisRouterWMMAPSD_Type()
)
arrisRouterWMMAPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMAPSD.setStatus("current")
_ArrisRouterWMMEDCAAPTable_Object = MibTable
arrisRouterWMMEDCAAPTable = _ArrisRouterWMMEDCAAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4)
)
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPTable.setStatus("current")
_ArrisRouterWMMEDCAAPEntry_Object = MibTableRow
arrisRouterWMMEDCAAPEntry = _ArrisRouterWMMEDCAAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1)
)
arrisRouterWMMEDCAAPEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWMMEDCAAPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPEntry.setStatus("current")


class _ArrisRouterWMMEDCAAPIndex_Type(Integer32):
    """Custom type arrisRouterWMMEDCAAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ArrisRouterWMMEDCAAPIndex_Type.__name__ = "Integer32"
_ArrisRouterWMMEDCAAPIndex_Object = MibTableColumn
arrisRouterWMMEDCAAPIndex = _ArrisRouterWMMEDCAAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 1),
    _ArrisRouterWMMEDCAAPIndex_Type()
)
arrisRouterWMMEDCAAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPIndex.setStatus("current")
_ArrisRouterWMMEDCAAPCWmin_Type = Unsigned32
_ArrisRouterWMMEDCAAPCWmin_Object = MibTableColumn
arrisRouterWMMEDCAAPCWmin = _ArrisRouterWMMEDCAAPCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 2),
    _ArrisRouterWMMEDCAAPCWmin_Type()
)
arrisRouterWMMEDCAAPCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPCWmin.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPCWmin.setUnits("milliseconds")
_ArrisRouterWMMEDCAAPCWmax_Type = Unsigned32
_ArrisRouterWMMEDCAAPCWmax_Object = MibTableColumn
arrisRouterWMMEDCAAPCWmax = _ArrisRouterWMMEDCAAPCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 3),
    _ArrisRouterWMMEDCAAPCWmax_Type()
)
arrisRouterWMMEDCAAPCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPCWmax.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPCWmax.setUnits("milliseconds")
_ArrisRouterWMMEDCAAPAIFSN_Type = Unsigned32
_ArrisRouterWMMEDCAAPAIFSN_Object = MibTableColumn
arrisRouterWMMEDCAAPAIFSN = _ArrisRouterWMMEDCAAPAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 4),
    _ArrisRouterWMMEDCAAPAIFSN_Type()
)
arrisRouterWMMEDCAAPAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPAIFSN.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPAIFSN.setUnits("milliseconds")


class _ArrisRouterWMMEDCAAPTxOpBLimit_Type(Unsigned32):
    """Custom type arrisRouterWMMEDCAAPTxOpBLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterWMMEDCAAPTxOpBLimit_Type.__name__ = "Unsigned32"
_ArrisRouterWMMEDCAAPTxOpBLimit_Object = MibTableColumn
arrisRouterWMMEDCAAPTxOpBLimit = _ArrisRouterWMMEDCAAPTxOpBLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 5),
    _ArrisRouterWMMEDCAAPTxOpBLimit_Type()
)
arrisRouterWMMEDCAAPTxOpBLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPTxOpBLimit.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPTxOpBLimit.setUnits("microseconds")


class _ArrisRouterWMMEDCAAPTxOpAGLimit_Type(Unsigned32):
    """Custom type arrisRouterWMMEDCAAPTxOpAGLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterWMMEDCAAPTxOpAGLimit_Type.__name__ = "Unsigned32"
_ArrisRouterWMMEDCAAPTxOpAGLimit_Object = MibTableColumn
arrisRouterWMMEDCAAPTxOpAGLimit = _ArrisRouterWMMEDCAAPTxOpAGLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 6),
    _ArrisRouterWMMEDCAAPTxOpAGLimit_Type()
)
arrisRouterWMMEDCAAPTxOpAGLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPTxOpAGLimit.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPTxOpAGLimit.setUnits("microseconds")
_ArrisRouterWMMEDCAAPAdmitCont_Type = TruthValue
_ArrisRouterWMMEDCAAPAdmitCont_Object = MibTableColumn
arrisRouterWMMEDCAAPAdmitCont = _ArrisRouterWMMEDCAAPAdmitCont_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 7),
    _ArrisRouterWMMEDCAAPAdmitCont_Type()
)
arrisRouterWMMEDCAAPAdmitCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPAdmitCont.setStatus("current")
_ArrisRouterWMMEDCAAPDiscardOld_Type = TruthValue
_ArrisRouterWMMEDCAAPDiscardOld_Object = MibTableColumn
arrisRouterWMMEDCAAPDiscardOld = _ArrisRouterWMMEDCAAPDiscardOld_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 29, 4, 1, 8),
    _ArrisRouterWMMEDCAAPDiscardOld_Type()
)
arrisRouterWMMEDCAAPDiscardOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMMEDCAAPDiscardOld.setStatus("current")
_ArrisRouterWPSCfg_ObjectIdentity = ObjectIdentity
arrisRouterWPSCfg = _ArrisRouterWPSCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30)
)


class _ArrisRouterWpsMode_Type(Integer32):
    """Custom type arrisRouterWpsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWpsMode_Type.__name__ = "Integer32"
_ArrisRouterWpsMode_Object = MibScalar
arrisRouterWpsMode = _ArrisRouterWpsMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 1),
    _ArrisRouterWpsMode_Type()
)
arrisRouterWpsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsMode.setStatus("current")


class _ArrisRouterWpsConfigState_Type(Integer32):
    """Custom type arrisRouterWpsConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWpsConfigState_Type.__name__ = "Integer32"
_ArrisRouterWpsConfigState_Object = MibScalar
arrisRouterWpsConfigState = _ArrisRouterWpsConfigState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 2),
    _ArrisRouterWpsConfigState_Type()
)
arrisRouterWpsConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsConfigState.setStatus("current")


class _ArrisRouterWpsDevicePIN_Type(DisplayString):
    """Custom type arrisRouterWpsDevicePIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ArrisRouterWpsDevicePIN_Type.__name__ = "DisplayString"
_ArrisRouterWpsDevicePIN_Object = MibScalar
arrisRouterWpsDevicePIN = _ArrisRouterWpsDevicePIN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 3),
    _ArrisRouterWpsDevicePIN_Type()
)
arrisRouterWpsDevicePIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsDevicePIN.setStatus("current")


class _ArrisRouterWpsDeviceName_Type(DisplayString):
    """Custom type arrisRouterWpsDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterWpsDeviceName_Type.__name__ = "DisplayString"
_ArrisRouterWpsDeviceName_Object = MibScalar
arrisRouterWpsDeviceName = _ArrisRouterWpsDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 4),
    _ArrisRouterWpsDeviceName_Type()
)
arrisRouterWpsDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWpsDeviceName.setStatus("current")


class _ArrisRouterWpsModelName_Type(DisplayString):
    """Custom type arrisRouterWpsModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterWpsModelName_Type.__name__ = "DisplayString"
_ArrisRouterWpsModelName_Object = MibScalar
arrisRouterWpsModelName = _ArrisRouterWpsModelName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 5),
    _ArrisRouterWpsModelName_Type()
)
arrisRouterWpsModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWpsModelName.setStatus("current")


class _ArrisRouterWpsMfg_Type(DisplayString):
    """Custom type arrisRouterWpsMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWpsMfg_Type.__name__ = "DisplayString"
_ArrisRouterWpsMfg_Object = MibScalar
arrisRouterWpsMfg = _ArrisRouterWpsMfg_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 6),
    _ArrisRouterWpsMfg_Type()
)
arrisRouterWpsMfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsMfg.setStatus("current")


class _ArrisRouterWpsResultStatus_Type(Integer32):
    """Custom type arrisRouterWpsResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("wpsResultUnknown", -1),
          ("wpsResultNoneIssued", 0),
          ("wpsResultAddClientSuccess", 1),
          ("wpsResultAddClientFail", 2),
          ("wpsResultAddClientAbort", 3),
          ("wpsResultConfigApSuccess", 4),
          ("wpsResultConfigApFail", 5),
          ("wpsResultConfigApAbort", 6))
    )


_ArrisRouterWpsResultStatus_Type.__name__ = "Integer32"
_ArrisRouterWpsResultStatus_Object = MibScalar
arrisRouterWpsResultStatus = _ArrisRouterWpsResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 7),
    _ArrisRouterWpsResultStatus_Type()
)
arrisRouterWpsResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWpsResultStatus.setStatus("current")


class _ArrisRouterWpsStatus_Type(Integer32):
    """Custom type arrisRouterWpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
        *(("wpsUnknown", -1),
          ("wpsInitialState", 0),
          ("wpsAssociatedStarted", 1),
          ("wpsM2Sent", 2),
          ("wpsM7Sent", 3),
          ("wpsTimedOut", 4),
          ("wpsMsgDone", 5),
          ("wpsSuccessful", 6),
          ("wpsMsgExchangeErr", 7),
          ("wpsPushButtonOverlap", 8),
          ("wpsAssociating", 9),
          ("wpsPushButtonFindAP", 10))
    )


_ArrisRouterWpsStatus_Type.__name__ = "Integer32"
_ArrisRouterWpsStatus_Object = MibScalar
arrisRouterWpsStatus = _ArrisRouterWpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 8),
    _ArrisRouterWpsStatus_Type()
)
arrisRouterWpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWpsStatus.setStatus("current")


class _ArrisRouterWpsConfigTimeout_Type(Integer32):
    """Custom type arrisRouterWpsConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWpsConfigTimeout_Type.__name__ = "Integer32"
_ArrisRouterWpsConfigTimeout_Object = MibScalar
arrisRouterWpsConfigTimeout = _ArrisRouterWpsConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 9),
    _ArrisRouterWpsConfigTimeout_Type()
)
arrisRouterWpsConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsConfigTimeout.setStatus("current")


class _ArrisRouterWpsSTAPin_Type(DisplayString):
    """Custom type arrisRouterWpsSTAPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ArrisRouterWpsSTAPin_Type.__name__ = "DisplayString"
_ArrisRouterWpsSTAPin_Object = MibScalar
arrisRouterWpsSTAPin = _ArrisRouterWpsSTAPin_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 10),
    _ArrisRouterWpsSTAPin_Type()
)
arrisRouterWpsSTAPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsSTAPin.setStatus("current")


class _ArrisRouterWpsPushButton_Type(Integer32):
    """Custom type arrisRouterWpsPushButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("activatePushButton", 1),
          ("activatePINCfg", 2),
          ("cancelWPS", 3))
    )


_ArrisRouterWpsPushButton_Type.__name__ = "Integer32"
_ArrisRouterWpsPushButton_Object = MibScalar
arrisRouterWpsPushButton = _ArrisRouterWpsPushButton_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 11),
    _ArrisRouterWpsPushButton_Type()
)
arrisRouterWpsPushButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsPushButton.setStatus("current")


class _ArrisRouterWpsUUID_Type(DisplayString):
    """Custom type arrisRouterWpsUUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrisRouterWpsUUID_Type.__name__ = "DisplayString"
_ArrisRouterWpsUUID_Object = MibScalar
arrisRouterWpsUUID = _ArrisRouterWpsUUID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 14),
    _ArrisRouterWpsUUID_Type()
)
arrisRouterWpsUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWpsUUID.setStatus("current")
_ArrisRouterWPSMethodCfg_ObjectIdentity = ObjectIdentity
arrisRouterWPSMethodCfg = _ArrisRouterWPSMethodCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 15)
)


class _ArrisRouterWPSMethodLabel_Type(Integer32):
    """Custom type arrisRouterWPSMethodLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWPSMethodLabel_Type.__name__ = "Integer32"
_ArrisRouterWPSMethodLabel_Object = MibScalar
arrisRouterWPSMethodLabel = _ArrisRouterWPSMethodLabel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 15, 1),
    _ArrisRouterWPSMethodLabel_Type()
)
arrisRouterWPSMethodLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPSMethodLabel.setStatus("current")


class _ArrisRouterWPSMethodPIN_Type(Integer32):
    """Custom type arrisRouterWPSMethodPIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWPSMethodPIN_Type.__name__ = "Integer32"
_ArrisRouterWPSMethodPIN_Object = MibScalar
arrisRouterWPSMethodPIN = _ArrisRouterWPSMethodPIN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 15, 2),
    _ArrisRouterWPSMethodPIN_Type()
)
arrisRouterWPSMethodPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPSMethodPIN.setStatus("current")


class _ArrisRouterWPSMethodPushButton_Type(Integer32):
    """Custom type arrisRouterWPSMethodPushButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWPSMethodPushButton_Type.__name__ = "Integer32"
_ArrisRouterWPSMethodPushButton_Object = MibScalar
arrisRouterWPSMethodPushButton = _ArrisRouterWPSMethodPushButton_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 15, 3),
    _ArrisRouterWPSMethodPushButton_Type()
)
arrisRouterWPSMethodPushButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPSMethodPushButton.setStatus("current")


class _ArrisRouterWPSMethodKeypad_Type(Integer32):
    """Custom type arrisRouterWPSMethodKeypad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWPSMethodKeypad_Type.__name__ = "Integer32"
_ArrisRouterWPSMethodKeypad_Object = MibScalar
arrisRouterWPSMethodKeypad = _ArrisRouterWPSMethodKeypad_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 30, 15, 4),
    _ArrisRouterWPSMethodKeypad_Type()
)
arrisRouterWPSMethodKeypad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWPSMethodKeypad.setStatus("current")


class _ArrisRouterWiFiResetDefaults_Type(Integer32):
    """Custom type arrisRouterWiFiResetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothingToReset", 0),
          ("resetWifiDefaults", 1))
    )


_ArrisRouterWiFiResetDefaults_Type.__name__ = "Integer32"
_ArrisRouterWiFiResetDefaults_Object = MibScalar
arrisRouterWiFiResetDefaults = _ArrisRouterWiFiResetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 32),
    _ArrisRouterWiFiResetDefaults_Type()
)
arrisRouterWiFiResetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiResetDefaults.setStatus("current")
_ArrisRouterWiFiCustomSSIDStr_Type = DisplayString
_ArrisRouterWiFiCustomSSIDStr_Object = MibScalar
arrisRouterWiFiCustomSSIDStr = _ArrisRouterWiFiCustomSSIDStr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 34),
    _ArrisRouterWiFiCustomSSIDStr_Type()
)
arrisRouterWiFiCustomSSIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiCustomSSIDStr.setStatus("current")


class _ArrisRouterWiFiRadioControlMode_Type(Integer32):
    """Custom type arrisRouterWiFiRadioControlMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userControlled", 0),
          ("msoControlled24bgnMode", 1),
          ("msoControlled24nMode", 2),
          ("msoControlled50nMode", 3))
    )


_ArrisRouterWiFiRadioControlMode_Type.__name__ = "Integer32"
_ArrisRouterWiFiRadioControlMode_Object = MibScalar
arrisRouterWiFiRadioControlMode = _ArrisRouterWiFiRadioControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 37),
    _ArrisRouterWiFiRadioControlMode_Type()
)
arrisRouterWiFiRadioControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiRadioControlMode.setStatus("current")
_ArrisRouterWiFiScan_ObjectIdentity = ObjectIdentity
arrisRouterWiFiScan = _ArrisRouterWiFiScan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39)
)


class _ArrisRouterWiFiStartScan_Type(Integer32):
    """Custom type arrisRouterWiFiStartScan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startRadio0", 1),
          ("startRadio1", 2))
    )


_ArrisRouterWiFiStartScan_Type.__name__ = "Integer32"
_ArrisRouterWiFiStartScan_Object = MibScalar
arrisRouterWiFiStartScan = _ArrisRouterWiFiStartScan_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 1),
    _ArrisRouterWiFiStartScan_Type()
)
arrisRouterWiFiStartScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiStartScan.setStatus("current")


class _ArrisRouterWiFiScanResult_Type(Integer32):
    """Custom type arrisRouterWiFiScanResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uninit", 0),
          ("running", 1),
          ("completeError", 2),
          ("completeSuccess", 3))
    )


_ArrisRouterWiFiScanResult_Type.__name__ = "Integer32"
_ArrisRouterWiFiScanResult_Object = MibScalar
arrisRouterWiFiScanResult = _ArrisRouterWiFiScanResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 2),
    _ArrisRouterWiFiScanResult_Type()
)
arrisRouterWiFiScanResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanResult.setStatus("current")
_ArrisRouterWiFiScanResultTable_Object = MibTable
arrisRouterWiFiScanResultTable = _ArrisRouterWiFiScanResultTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3)
)
if mibBuilder.loadTexts:
    arrisRouterWiFiScanResultTable.setStatus("current")
_ArrisRouterWiFiScanResultEntry_Object = MibTableRow
arrisRouterWiFiScanResultEntry = _ArrisRouterWiFiScanResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1)
)
arrisRouterWiFiScanResultEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWiFiScanIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWiFiScanResultEntry.setStatus("current")
_ArrisRouterWiFiScanIndex_Type = Unsigned32
_ArrisRouterWiFiScanIndex_Object = MibTableColumn
arrisRouterWiFiScanIndex = _ArrisRouterWiFiScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 1),
    _ArrisRouterWiFiScanIndex_Type()
)
arrisRouterWiFiScanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanIndex.setStatus("current")
_ArrisRouterWiFiScanSSID_Type = DisplayString
_ArrisRouterWiFiScanSSID_Object = MibTableColumn
arrisRouterWiFiScanSSID = _ArrisRouterWiFiScanSSID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 2),
    _ArrisRouterWiFiScanSSID_Type()
)
arrisRouterWiFiScanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanSSID.setStatus("current")
_ArrisRouterWiFiScanChannel_Type = Unsigned32
_ArrisRouterWiFiScanChannel_Object = MibTableColumn
arrisRouterWiFiScanChannel = _ArrisRouterWiFiScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 3),
    _ArrisRouterWiFiScanChannel_Type()
)
arrisRouterWiFiScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanChannel.setStatus("current")
_ArrisRouterWiFiScanChannel2_Type = Unsigned32
_ArrisRouterWiFiScanChannel2_Object = MibTableColumn
arrisRouterWiFiScanChannel2 = _ArrisRouterWiFiScanChannel2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 4),
    _ArrisRouterWiFiScanChannel2_Type()
)
arrisRouterWiFiScanChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanChannel2.setStatus("current")
_ArrisRouterWiFiScanRSSI_Type = Integer32
_ArrisRouterWiFiScanRSSI_Object = MibTableColumn
arrisRouterWiFiScanRSSI = _ArrisRouterWiFiScanRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 5),
    _ArrisRouterWiFiScanRSSI_Type()
)
arrisRouterWiFiScanRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanRSSI.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanRSSI.setUnits("dBm")
_ArrisRouterWiFiScanNoise_Type = Integer32
_ArrisRouterWiFiScanNoise_Object = MibTableColumn
arrisRouterWiFiScanNoise = _ArrisRouterWiFiScanNoise_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 6),
    _ArrisRouterWiFiScanNoise_Type()
)
arrisRouterWiFiScanNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanNoise.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanNoise.setUnits("dBm")
_ArrisRouterWiFiScanMAC_Type = DisplayString
_ArrisRouterWiFiScanMAC_Object = MibTableColumn
arrisRouterWiFiScanMAC = _ArrisRouterWiFiScanMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 7),
    _ArrisRouterWiFiScanMAC_Type()
)
arrisRouterWiFiScanMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanMAC.setStatus("current")
_ArrisRouterWiFiScanMfg_Type = DisplayString
_ArrisRouterWiFiScanMfg_Object = MibTableColumn
arrisRouterWiFiScanMfg = _ArrisRouterWiFiScanMfg_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 8),
    _ArrisRouterWiFiScanMfg_Type()
)
arrisRouterWiFiScanMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanMfg.setStatus("current")
_ArrisRouterWiFiScanSupportedRates_Type = DisplayString
_ArrisRouterWiFiScanSupportedRates_Object = MibTableColumn
arrisRouterWiFiScanSupportedRates = _ArrisRouterWiFiScanSupportedRates_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 9),
    _ArrisRouterWiFiScanSupportedRates_Type()
)
arrisRouterWiFiScanSupportedRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanSupportedRates.setStatus("current")
_ArrisRouterWiFiScanOperatingStandards_Type = DisplayString
_ArrisRouterWiFiScanOperatingStandards_Object = MibTableColumn
arrisRouterWiFiScanOperatingStandards = _ArrisRouterWiFiScanOperatingStandards_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 10),
    _ArrisRouterWiFiScanOperatingStandards_Type()
)
arrisRouterWiFiScanOperatingStandards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanOperatingStandards.setStatus("current")


class _ArrisRouterWiFiScanSecurityModeEnabled_Type(Integer32):
    """Custom type arrisRouterWiFiScanSecurityModeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknow", 0),
          ("disabled", 1),
          ("wep", 2),
          ("wpa", 3),
          ("wpa2", 4),
          ("wpaWpa2", 5),
          ("wpaEnterprise", 6),
          ("wpa2Enterprise", 7),
          ("wpaWpa2Enterprise", 8))
    )


_ArrisRouterWiFiScanSecurityModeEnabled_Type.__name__ = "Integer32"
_ArrisRouterWiFiScanSecurityModeEnabled_Object = MibTableColumn
arrisRouterWiFiScanSecurityModeEnabled = _ArrisRouterWiFiScanSecurityModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 11),
    _ArrisRouterWiFiScanSecurityModeEnabled_Type()
)
arrisRouterWiFiScanSecurityModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanSecurityModeEnabled.setStatus("current")


class _ArrisRouterWiFiScanOperatingChannelBandwidth_Type(Integer32):
    """Custom type arrisRouterWiFiScanOperatingChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("n20Mhz", 1),
          ("n40Mhz", 2),
          ("ac80Mhz", 3),
          ("ac160Mhz", 4))
    )


_ArrisRouterWiFiScanOperatingChannelBandwidth_Type.__name__ = "Integer32"
_ArrisRouterWiFiScanOperatingChannelBandwidth_Object = MibTableColumn
arrisRouterWiFiScanOperatingChannelBandwidth = _ArrisRouterWiFiScanOperatingChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 39, 3, 1, 12),
    _ArrisRouterWiFiScanOperatingChannelBandwidth_Type()
)
arrisRouterWiFiScanOperatingChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiScanOperatingChannelBandwidth.setStatus("current")
_ArrisRouterWiFiClientInfoTable_Object = MibTable
arrisRouterWiFiClientInfoTable = _ArrisRouterWiFiClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42)
)
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoTable.setStatus("current")
_ArrisRouterWiFiClientInfoEntry_Object = MibTableRow
arrisRouterWiFiClientInfoEntry = _ArrisRouterWiFiClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1)
)
arrisRouterWiFiClientInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWiFiClientInfoIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoEntry.setStatus("current")


class _ArrisRouterWiFiClientInfoIndex_Type(Integer32):
    """Custom type arrisRouterWiFiClientInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ArrisRouterWiFiClientInfoIndex_Type.__name__ = "Integer32"
_ArrisRouterWiFiClientInfoIndex_Object = MibTableColumn
arrisRouterWiFiClientInfoIndex = _ArrisRouterWiFiClientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 1),
    _ArrisRouterWiFiClientInfoIndex_Type()
)
arrisRouterWiFiClientInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIndex.setStatus("current")
_ArrisRouterWiFiClientInfoIPAddrType_Type = InetAddressType
_ArrisRouterWiFiClientInfoIPAddrType_Object = MibTableColumn
arrisRouterWiFiClientInfoIPAddrType = _ArrisRouterWiFiClientInfoIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 2),
    _ArrisRouterWiFiClientInfoIPAddrType_Type()
)
arrisRouterWiFiClientInfoIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIPAddrType.setStatus("current")
_ArrisRouterWiFiClientInfoIPAddr_Type = InetAddress
_ArrisRouterWiFiClientInfoIPAddr_Object = MibTableColumn
arrisRouterWiFiClientInfoIPAddr = _ArrisRouterWiFiClientInfoIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 3),
    _ArrisRouterWiFiClientInfoIPAddr_Type()
)
arrisRouterWiFiClientInfoIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIPAddr.setStatus("current")
_ArrisRouterWiFiClientInfoIPAddrTextual_Type = DisplayString
_ArrisRouterWiFiClientInfoIPAddrTextual_Object = MibTableColumn
arrisRouterWiFiClientInfoIPAddrTextual = _ArrisRouterWiFiClientInfoIPAddrTextual_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 4),
    _ArrisRouterWiFiClientInfoIPAddrTextual_Type()
)
arrisRouterWiFiClientInfoIPAddrTextual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIPAddrTextual.setStatus("current")


class _ArrisRouterWiFiClientInfoHostName_Type(DisplayString):
    """Custom type arrisRouterWiFiClientInfoHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWiFiClientInfoHostName_Type.__name__ = "DisplayString"
_ArrisRouterWiFiClientInfoHostName_Object = MibTableColumn
arrisRouterWiFiClientInfoHostName = _ArrisRouterWiFiClientInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 5),
    _ArrisRouterWiFiClientInfoHostName_Type()
)
arrisRouterWiFiClientInfoHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoHostName.setStatus("current")
_ArrisRouterWiFiClientInfoMAC_Type = MacAddress
_ArrisRouterWiFiClientInfoMAC_Object = MibTableColumn
arrisRouterWiFiClientInfoMAC = _ArrisRouterWiFiClientInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 6),
    _ArrisRouterWiFiClientInfoMAC_Type()
)
arrisRouterWiFiClientInfoMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoMAC.setStatus("current")


class _ArrisRouterWiFiClientInfoMACMfg_Type(DisplayString):
    """Custom type arrisRouterWiFiClientInfoMACMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWiFiClientInfoMACMfg_Type.__name__ = "DisplayString"
_ArrisRouterWiFiClientInfoMACMfg_Object = MibTableColumn
arrisRouterWiFiClientInfoMACMfg = _ArrisRouterWiFiClientInfoMACMfg_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 7),
    _ArrisRouterWiFiClientInfoMACMfg_Type()
)
arrisRouterWiFiClientInfoMACMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoMACMfg.setStatus("current")


class _ArrisRouterWiFiClientInfoStatus_Type(Integer32):
    """Custom type arrisRouterWiFiClientInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_ArrisRouterWiFiClientInfoStatus_Type.__name__ = "Integer32"
_ArrisRouterWiFiClientInfoStatus_Object = MibTableColumn
arrisRouterWiFiClientInfoStatus = _ArrisRouterWiFiClientInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 8),
    _ArrisRouterWiFiClientInfoStatus_Type()
)
arrisRouterWiFiClientInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoStatus.setStatus("current")
_ArrisRouterWiFiClientInfoFirstSeen_Type = DateAndTime
_ArrisRouterWiFiClientInfoFirstSeen_Object = MibTableColumn
arrisRouterWiFiClientInfoFirstSeen = _ArrisRouterWiFiClientInfoFirstSeen_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 9),
    _ArrisRouterWiFiClientInfoFirstSeen_Type()
)
arrisRouterWiFiClientInfoFirstSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoFirstSeen.setStatus("current")
_ArrisRouterWiFiClientInfoLastSeen_Type = DateAndTime
_ArrisRouterWiFiClientInfoLastSeen_Object = MibTableColumn
arrisRouterWiFiClientInfoLastSeen = _ArrisRouterWiFiClientInfoLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 10),
    _ArrisRouterWiFiClientInfoLastSeen_Type()
)
arrisRouterWiFiClientInfoLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoLastSeen.setStatus("current")
_ArrisRouterWiFiClientInfoIdleTime_Type = Integer32
_ArrisRouterWiFiClientInfoIdleTime_Object = MibTableColumn
arrisRouterWiFiClientInfoIdleTime = _ArrisRouterWiFiClientInfoIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 11),
    _ArrisRouterWiFiClientInfoIdleTime_Type()
)
arrisRouterWiFiClientInfoIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoIdleTime.setUnits("seconds")
_ArrisRouterWiFiClientInfoInNetworkTime_Type = Integer32
_ArrisRouterWiFiClientInfoInNetworkTime_Object = MibTableColumn
arrisRouterWiFiClientInfoInNetworkTime = _ArrisRouterWiFiClientInfoInNetworkTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 12),
    _ArrisRouterWiFiClientInfoInNetworkTime_Type()
)
arrisRouterWiFiClientInfoInNetworkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoInNetworkTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoInNetworkTime.setUnits("seconds")
_ArrisRouterWiFiClientInfoState_Type = DisplayString
_ArrisRouterWiFiClientInfoState_Object = MibTableColumn
arrisRouterWiFiClientInfoState = _ArrisRouterWiFiClientInfoState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 13),
    _ArrisRouterWiFiClientInfoState_Type()
)
arrisRouterWiFiClientInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoState.setStatus("current")
_ArrisRouterWiFiClientInfoFlags_Type = DisplayString
_ArrisRouterWiFiClientInfoFlags_Object = MibTableColumn
arrisRouterWiFiClientInfoFlags = _ArrisRouterWiFiClientInfoFlags_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 14),
    _ArrisRouterWiFiClientInfoFlags_Type()
)
arrisRouterWiFiClientInfoFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoFlags.setStatus("current")
_ArrisRouterWiFiClientInfoTxPkts_Type = Integer32
_ArrisRouterWiFiClientInfoTxPkts_Object = MibTableColumn
arrisRouterWiFiClientInfoTxPkts = _ArrisRouterWiFiClientInfoTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 15),
    _ArrisRouterWiFiClientInfoTxPkts_Type()
)
arrisRouterWiFiClientInfoTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoTxPkts.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoTxPkts.setUnits("packets")
_ArrisRouterWiFiClientInfoTxFailures_Type = Integer32
_ArrisRouterWiFiClientInfoTxFailures_Object = MibTableColumn
arrisRouterWiFiClientInfoTxFailures = _ArrisRouterWiFiClientInfoTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 16),
    _ArrisRouterWiFiClientInfoTxFailures_Type()
)
arrisRouterWiFiClientInfoTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoTxFailures.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoTxFailures.setUnits("packets")
_ArrisRouterWiFiClientInfoRxUnicastPkts_Type = Integer32
_ArrisRouterWiFiClientInfoRxUnicastPkts_Object = MibTableColumn
arrisRouterWiFiClientInfoRxUnicastPkts = _ArrisRouterWiFiClientInfoRxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 17),
    _ArrisRouterWiFiClientInfoRxUnicastPkts_Type()
)
arrisRouterWiFiClientInfoRxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRxUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRxUnicastPkts.setUnits("packets")
_ArrisRouterWiFiClientInfoRxMulticastPkts_Type = Integer32
_ArrisRouterWiFiClientInfoRxMulticastPkts_Object = MibTableColumn
arrisRouterWiFiClientInfoRxMulticastPkts = _ArrisRouterWiFiClientInfoRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 18),
    _ArrisRouterWiFiClientInfoRxMulticastPkts_Type()
)
arrisRouterWiFiClientInfoRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRxMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRxMulticastPkts.setUnits("packets")
_ArrisRouterWiFiClientInfoLastTxPktRate_Type = Integer32
_ArrisRouterWiFiClientInfoLastTxPktRate_Object = MibTableColumn
arrisRouterWiFiClientInfoLastTxPktRate = _ArrisRouterWiFiClientInfoLastTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 19),
    _ArrisRouterWiFiClientInfoLastTxPktRate_Type()
)
arrisRouterWiFiClientInfoLastTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoLastTxPktRate.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoLastTxPktRate.setUnits("kbps")
_ArrisRouterWiFiClientInfoLastRxPktRate_Type = Integer32
_ArrisRouterWiFiClientInfoLastRxPktRate_Object = MibTableColumn
arrisRouterWiFiClientInfoLastRxPktRate = _ArrisRouterWiFiClientInfoLastRxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 20),
    _ArrisRouterWiFiClientInfoLastRxPktRate_Type()
)
arrisRouterWiFiClientInfoLastRxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoLastRxPktRate.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoLastRxPktRate.setUnits("kbps")
_ArrisRouterWiFiClientInfoRateSet_Type = DisplayString
_ArrisRouterWiFiClientInfoRateSet_Object = MibTableColumn
arrisRouterWiFiClientInfoRateSet = _ArrisRouterWiFiClientInfoRateSet_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 21),
    _ArrisRouterWiFiClientInfoRateSet_Type()
)
arrisRouterWiFiClientInfoRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRateSet.setStatus("current")
_ArrisRouterWiFiClientInfoRSSI_Type = Integer32
_ArrisRouterWiFiClientInfoRSSI_Object = MibTableColumn
arrisRouterWiFiClientInfoRSSI = _ArrisRouterWiFiClientInfoRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 42, 1, 22),
    _ArrisRouterWiFiClientInfoRSSI_Type()
)
arrisRouterWiFiClientInfoRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiClientInfoRSSI.setStatus("current")
_ArrisRouterWiFiPhysicalChannel_Type = Integer32
_ArrisRouterWiFiPhysicalChannel_Object = MibScalar
arrisRouterWiFiPhysicalChannel = _ArrisRouterWiFiPhysicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 43),
    _ArrisRouterWiFiPhysicalChannel_Type()
)
arrisRouterWiFiPhysicalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiPhysicalChannel.setStatus("current")
_ArrisRouterWiFi50RadioSettings_ObjectIdentity = ObjectIdentity
arrisRouterWiFi50RadioSettings = _ArrisRouterWiFi50RadioSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50)
)


class _ArrisRouterWiFi50Channel_Type(Unsigned32):
    """Custom type arrisRouterWiFi50Channel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
    )


_ArrisRouterWiFi50Channel_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50Channel_Object = MibScalar
arrisRouterWiFi50Channel = _ArrisRouterWiFi50Channel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 1),
    _ArrisRouterWiFi50Channel_Type()
)
arrisRouterWiFi50Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50Channel.setStatus("current")


class _ArrisRouterWiFi50Mode_Type(Integer32):
    """Custom type arrisRouterWiFi50Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("anMix", 0),
          ("aOnly", 1),
          ("nOnly", 4),
          ("acOnly", 5),
          ("nacMix", 6),
          ("anacMix", 7))
    )


_ArrisRouterWiFi50Mode_Type.__name__ = "Integer32"
_ArrisRouterWiFi50Mode_Object = MibScalar
arrisRouterWiFi50Mode = _ArrisRouterWiFi50Mode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 2),
    _ArrisRouterWiFi50Mode_Type()
)
arrisRouterWiFi50Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50Mode.setStatus("current")


class _ArrisRouterWiFi50BeaconInterval_Type(Unsigned32):
    """Custom type arrisRouterWiFi50BeaconInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterWiFi50BeaconInterval_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50BeaconInterval_Object = MibScalar
arrisRouterWiFi50BeaconInterval = _ArrisRouterWiFi50BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 3),
    _ArrisRouterWiFi50BeaconInterval_Type()
)
arrisRouterWiFi50BeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50BeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFi50BeaconInterval.setUnits("milliseconds")


class _ArrisRouterWiFi50DTIMInterval_Type(Unsigned32):
    """Custom type arrisRouterWiFi50DTIMInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFi50DTIMInterval_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50DTIMInterval_Object = MibScalar
arrisRouterWiFi50DTIMInterval = _ArrisRouterWiFi50DTIMInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 4),
    _ArrisRouterWiFi50DTIMInterval_Type()
)
arrisRouterWiFi50DTIMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50DTIMInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFi50DTIMInterval.setUnits("milliseconds")


class _ArrisRouterWiFi50TxPreamble_Type(Integer32):
    """Custom type arrisRouterWiFi50TxPreamble based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("long", 0),
          ("short", 1))
    )


_ArrisRouterWiFi50TxPreamble_Type.__name__ = "Integer32"
_ArrisRouterWiFi50TxPreamble_Object = MibScalar
arrisRouterWiFi50TxPreamble = _ArrisRouterWiFi50TxPreamble_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 5),
    _ArrisRouterWiFi50TxPreamble_Type()
)
arrisRouterWiFi50TxPreamble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50TxPreamble.setStatus("current")


class _ArrisRouterWiFi50RTSThreshold_Type(Unsigned32):
    """Custom type arrisRouterWiFi50RTSThreshold based on Unsigned32"""
    defaultValue = 2347

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2347),
    )


_ArrisRouterWiFi50RTSThreshold_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50RTSThreshold_Object = MibScalar
arrisRouterWiFi50RTSThreshold = _ArrisRouterWiFi50RTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 6),
    _ArrisRouterWiFi50RTSThreshold_Type()
)
arrisRouterWiFi50RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50RTSThreshold.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFi50RTSThreshold.setUnits("bytes")


class _ArrisRouterWiFi50FragmentThresh_Type(Unsigned32):
    """Custom type arrisRouterWiFi50FragmentThresh based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_ArrisRouterWiFi50FragmentThresh_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50FragmentThresh_Object = MibScalar
arrisRouterWiFi50FragmentThresh = _ArrisRouterWiFi50FragmentThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 7),
    _ArrisRouterWiFi50FragmentThresh_Type()
)
arrisRouterWiFi50FragmentThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50FragmentThresh.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWiFi50FragmentThresh.setUnits("bytes")


class _ArrisRouterWiFi50ShortSlot_Type(TruthValue):
    """Custom type arrisRouterWiFi50ShortSlot based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFi50ShortSlot_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50ShortSlot_Object = MibScalar
arrisRouterWiFi50ShortSlot = _ArrisRouterWiFi50ShortSlot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 8),
    _ArrisRouterWiFi50ShortSlot_Type()
)
arrisRouterWiFi50ShortSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50ShortSlot.setStatus("current")


class _ArrisRouterWiFi50FrameBurst_Type(TruthValue):
    """Custom type arrisRouterWiFi50FrameBurst based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50FrameBurst_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50FrameBurst_Object = MibScalar
arrisRouterWiFi50FrameBurst = _ArrisRouterWiFi50FrameBurst_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 9),
    _ArrisRouterWiFi50FrameBurst_Type()
)
arrisRouterWiFi50FrameBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50FrameBurst.setStatus("current")


class _ArrisRouterWiFi50EnableRadio_Type(TruthValue):
    """Custom type arrisRouterWiFi50EnableRadio based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFi50EnableRadio_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50EnableRadio_Object = MibScalar
arrisRouterWiFi50EnableRadio = _ArrisRouterWiFi50EnableRadio_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 10),
    _ArrisRouterWiFi50EnableRadio_Type()
)
arrisRouterWiFi50EnableRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50EnableRadio.setStatus("current")


class _ArrisRouterWiFi50ShortRetryLimit_Type(Integer32):
    """Custom type arrisRouterWiFi50ShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFi50ShortRetryLimit_Type.__name__ = "Integer32"
_ArrisRouterWiFi50ShortRetryLimit_Object = MibScalar
arrisRouterWiFi50ShortRetryLimit = _ArrisRouterWiFi50ShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 12),
    _ArrisRouterWiFi50ShortRetryLimit_Type()
)
arrisRouterWiFi50ShortRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50ShortRetryLimit.setStatus("current")


class _ArrisRouterWiFi50LongRetryLimit_Type(Integer32):
    """Custom type arrisRouterWiFi50LongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterWiFi50LongRetryLimit_Type.__name__ = "Integer32"
_ArrisRouterWiFi50LongRetryLimit_Object = MibScalar
arrisRouterWiFi50LongRetryLimit = _ArrisRouterWiFi50LongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 13),
    _ArrisRouterWiFi50LongRetryLimit_Type()
)
arrisRouterWiFi50LongRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50LongRetryLimit.setStatus("current")


class _ArrisRouterWiFi50OutputPower_Type(Integer32):
    """Custom type arrisRouterWiFi50OutputPower based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("percent12", 12),
          ("percent25", 25),
          ("percent50", 50),
          ("percent75", 75),
          ("percent100", 100))
    )


_ArrisRouterWiFi50OutputPower_Type.__name__ = "Integer32"
_ArrisRouterWiFi50OutputPower_Object = MibScalar
arrisRouterWiFi50OutputPower = _ArrisRouterWiFi50OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 14),
    _ArrisRouterWiFi50OutputPower_Type()
)
arrisRouterWiFi50OutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50OutputPower.setStatus("current")


class _ArrisRouterWiFi50MulticastA_Type(Integer32):
    """Custom type arrisRouterWiFi50MulticastA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              12,
              18,
              24,
              36,
              48,
              72,
              96,
              108)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("rate12mbps", 12),
          ("rate18mbps", 18),
          ("rate24mbps", 24),
          ("rate36mbps", 36),
          ("rate48mbps", 48),
          ("rate72mbps", 72),
          ("rate96mbps", 96),
          ("rate108mbps", 108))
    )


_ArrisRouterWiFi50MulticastA_Type.__name__ = "Integer32"
_ArrisRouterWiFi50MulticastA_Object = MibScalar
arrisRouterWiFi50MulticastA = _ArrisRouterWiFi50MulticastA_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 15),
    _ArrisRouterWiFi50MulticastA_Type()
)
arrisRouterWiFi50MulticastA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50MulticastA.setStatus("current")
_ArrisRouterWiFi50PhysicalChannel_Type = Integer32
_ArrisRouterWiFi50PhysicalChannel_Object = MibScalar
arrisRouterWiFi50PhysicalChannel = _ArrisRouterWiFi50PhysicalChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 16),
    _ArrisRouterWiFi50PhysicalChannel_Type()
)
arrisRouterWiFi50PhysicalChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFi50PhysicalChannel.setStatus("current")
_ArrisRouterWiFi50NSettings_ObjectIdentity = ObjectIdentity
arrisRouterWiFi50NSettings = _ArrisRouterWiFi50NSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20)
)


class _ArrisRouterWiFi50HTMCS_Type(Integer32):
    """Custom type arrisRouterWiFi50HTMCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("legacy", 1),
          ("mcs0", 2),
          ("mcs1", 3),
          ("mcs2", 4),
          ("mcs3", 5),
          ("mcs4", 6),
          ("mcs5", 7),
          ("mcs6", 8),
          ("mcs7", 9),
          ("mcs8", 10),
          ("mcs9", 11),
          ("mcs10", 12),
          ("mcs11", 13),
          ("mcs12", 14),
          ("mcs13", 15),
          ("mcs14", 16),
          ("mcs15", 17),
          ("mcs16", 18),
          ("mcs17", 19),
          ("mcs18", 20),
          ("mcs19", 21),
          ("mcs20", 22),
          ("mcs21", 23),
          ("mcs22", 24),
          ("mcs23", 25))
    )


_ArrisRouterWiFi50HTMCS_Type.__name__ = "Integer32"
_ArrisRouterWiFi50HTMCS_Object = MibScalar
arrisRouterWiFi50HTMCS = _ArrisRouterWiFi50HTMCS_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 1),
    _ArrisRouterWiFi50HTMCS_Type()
)
arrisRouterWiFi50HTMCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50HTMCS.setStatus("current")


class _ArrisRouterWiFi50ChannelBW_Type(Integer32):
    """Custom type arrisRouterWiFi50ChannelBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("width20MHz", 0),
          ("width20and40Mhz", 2),
          ("width20and40and80Mhz", 3))
    )


_ArrisRouterWiFi50ChannelBW_Type.__name__ = "Integer32"
_ArrisRouterWiFi50ChannelBW_Object = MibScalar
arrisRouterWiFi50ChannelBW = _ArrisRouterWiFi50ChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 2),
    _ArrisRouterWiFi50ChannelBW_Type()
)
arrisRouterWiFi50ChannelBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50ChannelBW.setStatus("current")


class _ArrisRouterWiFi50NSideBand_Type(Integer32):
    """Custom type arrisRouterWiFi50NSideBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("upper", 1),
          ("lower", 2))
    )


_ArrisRouterWiFi50NSideBand_Type.__name__ = "Integer32"
_ArrisRouterWiFi50NSideBand_Object = MibScalar
arrisRouterWiFi50NSideBand = _ArrisRouterWiFi50NSideBand_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 3),
    _ArrisRouterWiFi50NSideBand_Type()
)
arrisRouterWiFi50NSideBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50NSideBand.setStatus("current")


class _ArrisRouterWiFi50HTMode_Type(Integer32):
    """Custom type arrisRouterWiFi50HTMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 0),
          ("greenField", 1))
    )


_ArrisRouterWiFi50HTMode_Type.__name__ = "Integer32"
_ArrisRouterWiFi50HTMode_Object = MibScalar
arrisRouterWiFi50HTMode = _ArrisRouterWiFi50HTMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 4),
    _ArrisRouterWiFi50HTMode_Type()
)
arrisRouterWiFi50HTMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50HTMode.setStatus("current")


class _ArrisRouterWiFi50GuardInterval_Type(Integer32):
    """Custom type arrisRouterWiFi50GuardInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gi400", 0),
          ("gi800", 1),
          ("auto", 2))
    )


_ArrisRouterWiFi50GuardInterval_Type.__name__ = "Integer32"
_ArrisRouterWiFi50GuardInterval_Object = MibScalar
arrisRouterWiFi50GuardInterval = _ArrisRouterWiFi50GuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 5),
    _ArrisRouterWiFi50GuardInterval_Type()
)
arrisRouterWiFi50GuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50GuardInterval.setStatus("current")


class _ArrisRouterWiFi50AMSDUEnable_Type(TruthValue):
    """Custom type arrisRouterWiFi50AMSDUEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50AMSDUEnable_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50AMSDUEnable_Object = MibScalar
arrisRouterWiFi50AMSDUEnable = _ArrisRouterWiFi50AMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 6),
    _ArrisRouterWiFi50AMSDUEnable_Type()
)
arrisRouterWiFi50AMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50AMSDUEnable.setStatus("current")


class _ArrisRouterWiFi50DeclinePeerBA_Type(TruthValue):
    """Custom type arrisRouterWiFi50DeclinePeerBA based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50DeclinePeerBA_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50DeclinePeerBA_Object = MibScalar
arrisRouterWiFi50DeclinePeerBA = _ArrisRouterWiFi50DeclinePeerBA_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 7),
    _ArrisRouterWiFi50DeclinePeerBA_Type()
)
arrisRouterWiFi50DeclinePeerBA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50DeclinePeerBA.setStatus("current")


class _ArrisRouterWiFi50BlockAck_Type(TruthValue):
    """Custom type arrisRouterWiFi50BlockAck based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50BlockAck_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50BlockAck_Object = MibScalar
arrisRouterWiFi50BlockAck = _ArrisRouterWiFi50BlockAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 8),
    _ArrisRouterWiFi50BlockAck_Type()
)
arrisRouterWiFi50BlockAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50BlockAck.setStatus("current")


class _ArrisRouterWiFi50NProtection_Type(Integer32):
    """Custom type arrisRouterWiFi50NProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("auto", 1))
    )


_ArrisRouterWiFi50NProtection_Type.__name__ = "Integer32"
_ArrisRouterWiFi50NProtection_Object = MibScalar
arrisRouterWiFi50NProtection = _ArrisRouterWiFi50NProtection_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 20, 9),
    _ArrisRouterWiFi50NProtection_Type()
)
arrisRouterWiFi50NProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50NProtection.setStatus("current")


class _ArrisRouterWiFi50HTTxStream_Type(Unsigned32):
    """Custom type arrisRouterWiFi50HTTxStream based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisRouterWiFi50HTTxStream_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50HTTxStream_Object = MibScalar
arrisRouterWiFi50HTTxStream = _ArrisRouterWiFi50HTTxStream_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 21),
    _ArrisRouterWiFi50HTTxStream_Type()
)
arrisRouterWiFi50HTTxStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50HTTxStream.setStatus("current")


class _ArrisRouterWiFi50HTRxStream_Type(Unsigned32):
    """Custom type arrisRouterWiFi50HTRxStream based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisRouterWiFi50HTRxStream_Type.__name__ = "Unsigned32"
_ArrisRouterWiFi50HTRxStream_Object = MibScalar
arrisRouterWiFi50HTRxStream = _ArrisRouterWiFi50HTRxStream_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 22),
    _ArrisRouterWiFi50HTRxStream_Type()
)
arrisRouterWiFi50HTRxStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50HTRxStream.setStatus("current")


class _ArrisRouterWiFi50EnableSTBC_Type(TruthValue):
    """Custom type arrisRouterWiFi50EnableSTBC based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50EnableSTBC_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50EnableSTBC_Object = MibScalar
arrisRouterWiFi50EnableSTBC = _ArrisRouterWiFi50EnableSTBC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 23),
    _ArrisRouterWiFi50EnableSTBC_Type()
)
arrisRouterWiFi50EnableSTBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50EnableSTBC.setStatus("current")


class _ArrisRouterWiFi50EnableRDG_Type(TruthValue):
    """Custom type arrisRouterWiFi50EnableRDG based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50EnableRDG_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50EnableRDG_Object = MibScalar
arrisRouterWiFi50EnableRDG = _ArrisRouterWiFi50EnableRDG_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 24),
    _ArrisRouterWiFi50EnableRDG_Type()
)
arrisRouterWiFi50EnableRDG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50EnableRDG.setStatus("current")


class _ArrisRouterWiFi50IGMPSnooping_Type(TruthValue):
    """Custom type arrisRouterWiFi50IGMPSnooping based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFi50IGMPSnooping_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50IGMPSnooping_Object = MibScalar
arrisRouterWiFi50IGMPSnooping = _ArrisRouterWiFi50IGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 25),
    _ArrisRouterWiFi50IGMPSnooping_Type()
)
arrisRouterWiFi50IGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50IGMPSnooping.setStatus("current")


class _ArrisRouterWiFi50BlockDFSChan_Type(TruthValue):
    """Custom type arrisRouterWiFi50BlockDFSChan based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFi50BlockDFSChan_Type.__name__ = "TruthValue"
_ArrisRouterWiFi50BlockDFSChan_Object = MibScalar
arrisRouterWiFi50BlockDFSChan = _ArrisRouterWiFi50BlockDFSChan_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 26),
    _ArrisRouterWiFi50BlockDFSChan_Type()
)
arrisRouterWiFi50BlockDFSChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50BlockDFSChan.setStatus("current")


class _ArrisRouterWiFi50RTSRetry_Type(Integer32):
    """Custom type arrisRouterWiFi50RTSRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterWiFi50RTSRetry_Type.__name__ = "Integer32"
_ArrisRouterWiFi50RTSRetry_Object = MibScalar
arrisRouterWiFi50RTSRetry = _ArrisRouterWiFi50RTSRetry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 27),
    _ArrisRouterWiFi50RTSRetry_Type()
)
arrisRouterWiFi50RTSRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50RTSRetry.setStatus("current")


class _ArrisRouterWiFi50TxRetry_Type(Integer32):
    """Custom type arrisRouterWiFi50TxRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterWiFi50TxRetry_Type.__name__ = "Integer32"
_ArrisRouterWiFi50TxRetry_Object = MibScalar
arrisRouterWiFi50TxRetry = _ArrisRouterWiFi50TxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 50, 28),
    _ArrisRouterWiFi50TxRetry_Type()
)
arrisRouterWiFi50TxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFi50TxRetry.setStatus("current")
_ArrisRouterWiFiNumSSIDSupported_Type = Unsigned32
_ArrisRouterWiFiNumSSIDSupported_Object = MibScalar
arrisRouterWiFiNumSSIDSupported = _ArrisRouterWiFiNumSSIDSupported_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 51),
    _ArrisRouterWiFiNumSSIDSupported_Type()
)
arrisRouterWiFiNumSSIDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWiFiNumSSIDSupported.setStatus("current")


class _ArrisRouterWiFiHTTxStream_Type(Unsigned32):
    """Custom type arrisRouterWiFiHTTxStream based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisRouterWiFiHTTxStream_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiHTTxStream_Object = MibScalar
arrisRouterWiFiHTTxStream = _ArrisRouterWiFiHTTxStream_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 55),
    _ArrisRouterWiFiHTTxStream_Type()
)
arrisRouterWiFiHTTxStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiHTTxStream.setStatus("current")


class _ArrisRouterWiFiHTRxStream_Type(Unsigned32):
    """Custom type arrisRouterWiFiHTRxStream based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisRouterWiFiHTRxStream_Type.__name__ = "Unsigned32"
_ArrisRouterWiFiHTRxStream_Object = MibScalar
arrisRouterWiFiHTRxStream = _ArrisRouterWiFiHTRxStream_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 56),
    _ArrisRouterWiFiHTRxStream_Type()
)
arrisRouterWiFiHTRxStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiHTRxStream.setStatus("current")


class _ArrisRouterWiFiEnableSTBC_Type(TruthValue):
    """Custom type arrisRouterWiFiEnableSTBC based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiEnableSTBC_Type.__name__ = "TruthValue"
_ArrisRouterWiFiEnableSTBC_Object = MibScalar
arrisRouterWiFiEnableSTBC = _ArrisRouterWiFiEnableSTBC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 57),
    _ArrisRouterWiFiEnableSTBC_Type()
)
arrisRouterWiFiEnableSTBC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiEnableSTBC.setStatus("current")


class _ArrisRouterWiFiEnableRDG_Type(TruthValue):
    """Custom type arrisRouterWiFiEnableRDG based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiEnableRDG_Type.__name__ = "TruthValue"
_ArrisRouterWiFiEnableRDG_Object = MibScalar
arrisRouterWiFiEnableRDG = _ArrisRouterWiFiEnableRDG_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 58),
    _ArrisRouterWiFiEnableRDG_Type()
)
arrisRouterWiFiEnableRDG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiEnableRDG.setStatus("current")


class _ArrisRouterWiFiIGMPSnooping_Type(TruthValue):
    """Custom type arrisRouterWiFiIGMPSnooping based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiIGMPSnooping_Type.__name__ = "TruthValue"
_ArrisRouterWiFiIGMPSnooping_Object = MibScalar
arrisRouterWiFiIGMPSnooping = _ArrisRouterWiFiIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 59),
    _ArrisRouterWiFiIGMPSnooping_Type()
)
arrisRouterWiFiIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiIGMPSnooping.setStatus("current")


class _ArrisRouterWiFiRTSRetry_Type(Integer32):
    """Custom type arrisRouterWiFiRTSRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterWiFiRTSRetry_Type.__name__ = "Integer32"
_ArrisRouterWiFiRTSRetry_Object = MibScalar
arrisRouterWiFiRTSRetry = _ArrisRouterWiFiRTSRetry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 60),
    _ArrisRouterWiFiRTSRetry_Type()
)
arrisRouterWiFiRTSRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiRTSRetry.setStatus("current")


class _ArrisRouterWiFiTxRetry_Type(Integer32):
    """Custom type arrisRouterWiFiTxRetry based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterWiFiTxRetry_Type.__name__ = "Integer32"
_ArrisRouterWiFiTxRetry_Object = MibScalar
arrisRouterWiFiTxRetry = _ArrisRouterWiFiTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 61),
    _ArrisRouterWiFiTxRetry_Type()
)
arrisRouterWiFiTxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiTxRetry.setStatus("current")
_ArrisRouterWiFiPhysicalChannelStats_ObjectIdentity = ObjectIdentity
arrisRouterWiFiPhysicalChannelStats = _ArrisRouterWiFiPhysicalChannelStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62)
)


class _ArrisRouterWiFiPhysicalChannelStatsEnable_Type(Integer32):
    """Custom type arrisRouterWiFiPhysicalChannelStatsEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enable-2-4", 1),
          ("enable-5", 2),
          ("enable-all", 3))
    )


_ArrisRouterWiFiPhysicalChannelStatsEnable_Type.__name__ = "Integer32"
_ArrisRouterWiFiPhysicalChannelStatsEnable_Object = MibScalar
arrisRouterWiFiPhysicalChannelStatsEnable = _ArrisRouterWiFiPhysicalChannelStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 1),
    _ArrisRouterWiFiPhysicalChannelStatsEnable_Type()
)
arrisRouterWiFiPhysicalChannelStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiPhysicalChannelStatsEnable.setStatus("current")


class _ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type(Integer32):
    """Custom type arrisRouterWiFiPhysicalChannelStatsMeasurementRate based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type.__name__ = "Integer32"
_ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Object = MibScalar
arrisRouterWiFiPhysicalChannelStatsMeasurementRate = _ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 2),
    _ArrisRouterWiFiPhysicalChannelStatsMeasurementRate_Type()
)
arrisRouterWiFiPhysicalChannelStatsMeasurementRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiPhysicalChannelStatsMeasurementRate.setStatus("current")


class _ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type(Integer32):
    """Custom type arrisRouterWiFiPhysicalChannelStatsMeasurementInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type.__name__ = "Integer32"
_ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Object = MibScalar
arrisRouterWiFiPhysicalChannelStatsMeasurementInterval = _ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 3),
    _ArrisRouterWiFiPhysicalChannelStatsMeasurementInterval_Type()
)
arrisRouterWiFiPhysicalChannelStatsMeasurementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiPhysicalChannelStatsMeasurementInterval.setStatus("current")
_ArrisRouterChannelStatsMeasurementTable_Object = MibTable
arrisRouterChannelStatsMeasurementTable = _ArrisRouterChannelStatsMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4)
)
if mibBuilder.loadTexts:
    arrisRouterChannelStatsMeasurementTable.setStatus("current")
_ArrisRouterChannelStatsMeasurementEntry_Object = MibTableRow
arrisRouterChannelStatsMeasurementEntry = _ArrisRouterChannelStatsMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1)
)
arrisRouterChannelStatsMeasurementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterChannelStatsMeasurementEntry.setStatus("current")


class _ArrisRouterChannelStatsMinNoiseFloor_Type(Integer32):
    """Custom type arrisRouterChannelStatsMinNoiseFloor based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsMinNoiseFloor_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsMinNoiseFloor_Object = MibTableColumn
arrisRouterChannelStatsMinNoiseFloor = _ArrisRouterChannelStatsMinNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 1),
    _ArrisRouterChannelStatsMinNoiseFloor_Type()
)
arrisRouterChannelStatsMinNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsMinNoiseFloor.setStatus("current")


class _ArrisRouterChannelStatsMaxNoiseFloor_Type(Integer32):
    """Custom type arrisRouterChannelStatsMaxNoiseFloor based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsMaxNoiseFloor_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsMaxNoiseFloor_Object = MibTableColumn
arrisRouterChannelStatsMaxNoiseFloor = _ArrisRouterChannelStatsMaxNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 2),
    _ArrisRouterChannelStatsMaxNoiseFloor_Type()
)
arrisRouterChannelStatsMaxNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsMaxNoiseFloor.setStatus("current")


class _ArrisRouterChannelStatsMedianNoiseFloor_Type(Integer32):
    """Custom type arrisRouterChannelStatsMedianNoiseFloor based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsMedianNoiseFloor_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsMedianNoiseFloor_Object = MibTableColumn
arrisRouterChannelStatsMedianNoiseFloor = _ArrisRouterChannelStatsMedianNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 3),
    _ArrisRouterChannelStatsMedianNoiseFloor_Type()
)
arrisRouterChannelStatsMedianNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsMedianNoiseFloor.setStatus("current")


class _ArrisRouterChannelStatsPacketsSent_Type(Counter64):
    """Custom type arrisRouterChannelStatsPacketsSent based on Counter64"""
    defaultValue = 0


_ArrisRouterChannelStatsPacketsSent_Type.__name__ = "Counter64"
_ArrisRouterChannelStatsPacketsSent_Object = MibTableColumn
arrisRouterChannelStatsPacketsSent = _ArrisRouterChannelStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 4),
    _ArrisRouterChannelStatsPacketsSent_Type()
)
arrisRouterChannelStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsPacketsSent.setStatus("current")


class _ArrisRouterChannelStatsPacketsReceived_Type(Counter64):
    """Custom type arrisRouterChannelStatsPacketsReceived based on Counter64"""
    defaultValue = 0


_ArrisRouterChannelStatsPacketsReceived_Type.__name__ = "Counter64"
_ArrisRouterChannelStatsPacketsReceived_Object = MibTableColumn
arrisRouterChannelStatsPacketsReceived = _ArrisRouterChannelStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 5),
    _ArrisRouterChannelStatsPacketsReceived_Type()
)
arrisRouterChannelStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsPacketsReceived.setStatus("current")


class _ArrisRouterChannelStatsCSTExceedPercent_Type(Integer32):
    """Custom type arrisRouterChannelStatsCSTExceedPercent based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsCSTExceedPercent_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsCSTExceedPercent_Object = MibTableColumn
arrisRouterChannelStatsCSTExceedPercent = _ArrisRouterChannelStatsCSTExceedPercent_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 6),
    _ArrisRouterChannelStatsCSTExceedPercent_Type()
)
arrisRouterChannelStatsCSTExceedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsCSTExceedPercent.setStatus("current")


class _ArrisRouterChannelStatsActivityFactor_Type(Integer32):
    """Custom type arrisRouterChannelStatsActivityFactor based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsActivityFactor_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsActivityFactor_Object = MibTableColumn
arrisRouterChannelStatsActivityFactor = _ArrisRouterChannelStatsActivityFactor_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 7),
    _ArrisRouterChannelStatsActivityFactor_Type()
)
arrisRouterChannelStatsActivityFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsActivityFactor.setStatus("current")


class _ArrisRouterChannelStatsChannelUtilization_Type(Integer32):
    """Custom type arrisRouterChannelStatsChannelUtilization based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsChannelUtilization_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsChannelUtilization_Object = MibTableColumn
arrisRouterChannelStatsChannelUtilization = _ArrisRouterChannelStatsChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 8),
    _ArrisRouterChannelStatsChannelUtilization_Type()
)
arrisRouterChannelStatsChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsChannelUtilization.setStatus("current")


class _ArrisRouterChannelStatsRetransmissionsMetric_Type(Integer32):
    """Custom type arrisRouterChannelStatsRetransmissionsMetric based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsRetransmissionsMetric_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsRetransmissionsMetric_Object = MibTableColumn
arrisRouterChannelStatsRetransmissionsMetric = _ArrisRouterChannelStatsRetransmissionsMetric_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 4, 1, 9),
    _ArrisRouterChannelStatsRetransmissionsMetric_Type()
)
arrisRouterChannelStatsRetransmissionsMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsRetransmissionsMetric.setStatus("current")
_ArrisRouterChannelStatsRSSITable_Object = MibTable
arrisRouterChannelStatsRSSITable = _ArrisRouterChannelStatsRSSITable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 5)
)
if mibBuilder.loadTexts:
    arrisRouterChannelStatsRSSITable.setStatus("current")
_ArrisRouterChannelStatsRSSITableEntry_Object = MibTableRow
arrisRouterChannelStatsRSSITableEntry = _ArrisRouterChannelStatsRSSITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 5, 1)
)
arrisRouterChannelStatsRSSITableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterChannelStatsRSSITableIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterChannelStatsRSSITableEntry.setStatus("current")


class _ArrisRouterChannelStatsRSSITableIndex_Type(Integer32):
    """Custom type arrisRouterChannelStatsRSSITableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ArrisRouterChannelStatsRSSITableIndex_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsRSSITableIndex_Object = MibTableColumn
arrisRouterChannelStatsRSSITableIndex = _ArrisRouterChannelStatsRSSITableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 5, 1, 1),
    _ArrisRouterChannelStatsRSSITableIndex_Type()
)
arrisRouterChannelStatsRSSITableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsRSSITableIndex.setStatus("current")


class _ArrisRouterChannelStatsRSSICount_Type(Integer32):
    """Custom type arrisRouterChannelStatsRSSICount based on Integer32"""
    defaultValue = -1


_ArrisRouterChannelStatsRSSICount_Type.__name__ = "Integer32"
_ArrisRouterChannelStatsRSSICount_Object = MibTableColumn
arrisRouterChannelStatsRSSICount = _ArrisRouterChannelStatsRSSICount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 62, 5, 1, 2),
    _ArrisRouterChannelStatsRSSICount_Type()
)
arrisRouterChannelStatsRSSICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChannelStatsRSSICount.setStatus("current")
_ArrisRouterWMM50Cfg_ObjectIdentity = ObjectIdentity
arrisRouterWMM50Cfg = _ArrisRouterWMM50Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63)
)


class _ArrisRouterWMM50Enable_Type(TruthValue):
    """Custom type arrisRouterWMM50Enable based on TruthValue"""
    defaultValue = 1


_ArrisRouterWMM50Enable_Type.__name__ = "TruthValue"
_ArrisRouterWMM50Enable_Object = MibScalar
arrisRouterWMM50Enable = _ArrisRouterWMM50Enable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 1),
    _ArrisRouterWMM50Enable_Type()
)
arrisRouterWMM50Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50Enable.setStatus("current")


class _ArrisRouterWMM50NoAck_Type(TruthValue):
    """Custom type arrisRouterWMM50NoAck based on TruthValue"""
    defaultValue = 2


_ArrisRouterWMM50NoAck_Type.__name__ = "TruthValue"
_ArrisRouterWMM50NoAck_Object = MibScalar
arrisRouterWMM50NoAck = _ArrisRouterWMM50NoAck_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 2),
    _ArrisRouterWMM50NoAck_Type()
)
arrisRouterWMM50NoAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50NoAck.setStatus("current")


class _ArrisRouterWMM50APSD_Type(TruthValue):
    """Custom type arrisRouterWMM50APSD based on TruthValue"""
    defaultValue = 1


_ArrisRouterWMM50APSD_Type.__name__ = "TruthValue"
_ArrisRouterWMM50APSD_Object = MibScalar
arrisRouterWMM50APSD = _ArrisRouterWMM50APSD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 3),
    _ArrisRouterWMM50APSD_Type()
)
arrisRouterWMM50APSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50APSD.setStatus("current")
_ArrisRouterWMM50EDCAAPTable_Object = MibTable
arrisRouterWMM50EDCAAPTable = _ArrisRouterWMM50EDCAAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4)
)
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPTable.setStatus("current")
_ArrisRouterWMM50EDCAAPEntry_Object = MibTableRow
arrisRouterWMM50EDCAAPEntry = _ArrisRouterWMM50EDCAAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1)
)
arrisRouterWMM50EDCAAPEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWMM50EDCAAPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPEntry.setStatus("current")


class _ArrisRouterWMM50EDCAAPIndex_Type(Integer32):
    """Custom type arrisRouterWMM50EDCAAPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ArrisRouterWMM50EDCAAPIndex_Type.__name__ = "Integer32"
_ArrisRouterWMM50EDCAAPIndex_Object = MibTableColumn
arrisRouterWMM50EDCAAPIndex = _ArrisRouterWMM50EDCAAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 1),
    _ArrisRouterWMM50EDCAAPIndex_Type()
)
arrisRouterWMM50EDCAAPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPIndex.setStatus("current")
_ArrisRouterWMM50EDCAAPCWmin_Type = Unsigned32
_ArrisRouterWMM50EDCAAPCWmin_Object = MibTableColumn
arrisRouterWMM50EDCAAPCWmin = _ArrisRouterWMM50EDCAAPCWmin_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 2),
    _ArrisRouterWMM50EDCAAPCWmin_Type()
)
arrisRouterWMM50EDCAAPCWmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPCWmin.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPCWmin.setUnits("milliseconds")
_ArrisRouterWMM50EDCAAPCWmax_Type = Unsigned32
_ArrisRouterWMM50EDCAAPCWmax_Object = MibTableColumn
arrisRouterWMM50EDCAAPCWmax = _ArrisRouterWMM50EDCAAPCWmax_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 3),
    _ArrisRouterWMM50EDCAAPCWmax_Type()
)
arrisRouterWMM50EDCAAPCWmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPCWmax.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPCWmax.setUnits("milliseconds")
_ArrisRouterWMM50EDCAAPAIFSN_Type = Unsigned32
_ArrisRouterWMM50EDCAAPAIFSN_Object = MibTableColumn
arrisRouterWMM50EDCAAPAIFSN = _ArrisRouterWMM50EDCAAPAIFSN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 4),
    _ArrisRouterWMM50EDCAAPAIFSN_Type()
)
arrisRouterWMM50EDCAAPAIFSN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPAIFSN.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPAIFSN.setUnits("milliseconds")


class _ArrisRouterWMM50EDCAAPTxOpBLimit_Type(Unsigned32):
    """Custom type arrisRouterWMM50EDCAAPTxOpBLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterWMM50EDCAAPTxOpBLimit_Type.__name__ = "Unsigned32"
_ArrisRouterWMM50EDCAAPTxOpBLimit_Object = MibTableColumn
arrisRouterWMM50EDCAAPTxOpBLimit = _ArrisRouterWMM50EDCAAPTxOpBLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 5),
    _ArrisRouterWMM50EDCAAPTxOpBLimit_Type()
)
arrisRouterWMM50EDCAAPTxOpBLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPTxOpBLimit.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPTxOpBLimit.setUnits("microseconds")


class _ArrisRouterWMM50EDCAAPTxOpAGLimit_Type(Unsigned32):
    """Custom type arrisRouterWMM50EDCAAPTxOpAGLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterWMM50EDCAAPTxOpAGLimit_Type.__name__ = "Unsigned32"
_ArrisRouterWMM50EDCAAPTxOpAGLimit_Object = MibTableColumn
arrisRouterWMM50EDCAAPTxOpAGLimit = _ArrisRouterWMM50EDCAAPTxOpAGLimit_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 6),
    _ArrisRouterWMM50EDCAAPTxOpAGLimit_Type()
)
arrisRouterWMM50EDCAAPTxOpAGLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPTxOpAGLimit.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPTxOpAGLimit.setUnits("microseconds")
_ArrisRouterWMM50EDCAAPAdmitCont_Type = TruthValue
_ArrisRouterWMM50EDCAAPAdmitCont_Object = MibTableColumn
arrisRouterWMM50EDCAAPAdmitCont = _ArrisRouterWMM50EDCAAPAdmitCont_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 7),
    _ArrisRouterWMM50EDCAAPAdmitCont_Type()
)
arrisRouterWMM50EDCAAPAdmitCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPAdmitCont.setStatus("current")
_ArrisRouterWMM50EDCAAPDiscardOld_Type = TruthValue
_ArrisRouterWMM50EDCAAPDiscardOld_Object = MibTableColumn
arrisRouterWMM50EDCAAPDiscardOld = _ArrisRouterWMM50EDCAAPDiscardOld_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 63, 4, 1, 8),
    _ArrisRouterWMM50EDCAAPDiscardOld_Type()
)
arrisRouterWMM50EDCAAPDiscardOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWMM50EDCAAPDiscardOld.setStatus("current")


class _ArrisRouterWiFiExtensionChannel_Type(Integer32):
    """Custom type arrisRouterWiFiExtensionChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("belowControlChannel", 0),
          ("aboveControlChannel", 1),
          ("auto", 2))
    )


_ArrisRouterWiFiExtensionChannel_Type.__name__ = "Integer32"
_ArrisRouterWiFiExtensionChannel_Object = MibScalar
arrisRouterWiFiExtensionChannel = _ArrisRouterWiFiExtensionChannel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 64),
    _ArrisRouterWiFiExtensionChannel_Type()
)
arrisRouterWiFiExtensionChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiExtensionChannel.setStatus("current")
_ArrisRouterWPS50Cfg_ObjectIdentity = ObjectIdentity
arrisRouterWPS50Cfg = _ArrisRouterWPS50Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65)
)


class _ArrisRouterWps50Mode_Type(Integer32):
    """Custom type arrisRouterWps50Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWps50Mode_Type.__name__ = "Integer32"
_ArrisRouterWps50Mode_Object = MibScalar
arrisRouterWps50Mode = _ArrisRouterWps50Mode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 1),
    _ArrisRouterWps50Mode_Type()
)
arrisRouterWps50Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50Mode.setStatus("current")


class _ArrisRouterWps50ConfigState_Type(Integer32):
    """Custom type arrisRouterWps50ConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWps50ConfigState_Type.__name__ = "Integer32"
_ArrisRouterWps50ConfigState_Object = MibScalar
arrisRouterWps50ConfigState = _ArrisRouterWps50ConfigState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 2),
    _ArrisRouterWps50ConfigState_Type()
)
arrisRouterWps50ConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50ConfigState.setStatus("current")


class _ArrisRouterWps50DevicePIN_Type(DisplayString):
    """Custom type arrisRouterWps50DevicePIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ArrisRouterWps50DevicePIN_Type.__name__ = "DisplayString"
_ArrisRouterWps50DevicePIN_Object = MibScalar
arrisRouterWps50DevicePIN = _ArrisRouterWps50DevicePIN_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 3),
    _ArrisRouterWps50DevicePIN_Type()
)
arrisRouterWps50DevicePIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50DevicePIN.setStatus("current")


class _ArrisRouterWps50DeviceName_Type(DisplayString):
    """Custom type arrisRouterWps50DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterWps50DeviceName_Type.__name__ = "DisplayString"
_ArrisRouterWps50DeviceName_Object = MibScalar
arrisRouterWps50DeviceName = _ArrisRouterWps50DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 4),
    _ArrisRouterWps50DeviceName_Type()
)
arrisRouterWps50DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWps50DeviceName.setStatus("current")


class _ArrisRouterWps50ModelName_Type(DisplayString):
    """Custom type arrisRouterWps50ModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterWps50ModelName_Type.__name__ = "DisplayString"
_ArrisRouterWps50ModelName_Object = MibScalar
arrisRouterWps50ModelName = _ArrisRouterWps50ModelName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 5),
    _ArrisRouterWps50ModelName_Type()
)
arrisRouterWps50ModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWps50ModelName.setStatus("current")


class _ArrisRouterWps50Mfg_Type(DisplayString):
    """Custom type arrisRouterWps50Mfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWps50Mfg_Type.__name__ = "DisplayString"
_ArrisRouterWps50Mfg_Object = MibScalar
arrisRouterWps50Mfg = _ArrisRouterWps50Mfg_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 6),
    _ArrisRouterWps50Mfg_Type()
)
arrisRouterWps50Mfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50Mfg.setStatus("current")


class _ArrisRouterWps50ResultStatus_Type(Integer32):
    """Custom type arrisRouterWps50ResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("wpsResultUnknown", -1),
          ("wpsResultNoneIssued", 0),
          ("wpsResultAddClientSuccess", 1),
          ("wpsResultAddClientFail", 2),
          ("wpsResultAddClientAbort", 3),
          ("wpsResultConfigApSuccess", 4),
          ("wpsResultConfigApFail", 5),
          ("wpsResultConfigApAbort", 6))
    )


_ArrisRouterWps50ResultStatus_Type.__name__ = "Integer32"
_ArrisRouterWps50ResultStatus_Object = MibScalar
arrisRouterWps50ResultStatus = _ArrisRouterWps50ResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 7),
    _ArrisRouterWps50ResultStatus_Type()
)
arrisRouterWps50ResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWps50ResultStatus.setStatus("current")


class _ArrisRouterWps50Status_Type(Integer32):
    """Custom type arrisRouterWps50Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
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
        *(("wpsUnknown", -1),
          ("wpsInitialState", 0),
          ("wpsAssociatedStarted", 1),
          ("wpsM2Sent", 2),
          ("wpsM7Sent", 3),
          ("wpsTimedOut", 4),
          ("wpsMsgDone", 5),
          ("wpsSuccessful", 6),
          ("wpsMsgExchangeErr", 7),
          ("wpsPushButtonOverlap", 8),
          ("wpsAssociating", 9),
          ("wpsPushButtonFindAP", 10))
    )


_ArrisRouterWps50Status_Type.__name__ = "Integer32"
_ArrisRouterWps50Status_Object = MibScalar
arrisRouterWps50Status = _ArrisRouterWps50Status_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 8),
    _ArrisRouterWps50Status_Type()
)
arrisRouterWps50Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWps50Status.setStatus("current")


class _ArrisRouterWps50ConfigTimeout_Type(Integer32):
    """Custom type arrisRouterWps50ConfigTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterWps50ConfigTimeout_Type.__name__ = "Integer32"
_ArrisRouterWps50ConfigTimeout_Object = MibScalar
arrisRouterWps50ConfigTimeout = _ArrisRouterWps50ConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 9),
    _ArrisRouterWps50ConfigTimeout_Type()
)
arrisRouterWps50ConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50ConfigTimeout.setStatus("current")


class _ArrisRouterWps50STAPin_Type(DisplayString):
    """Custom type arrisRouterWps50STAPin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ArrisRouterWps50STAPin_Type.__name__ = "DisplayString"
_ArrisRouterWps50STAPin_Object = MibScalar
arrisRouterWps50STAPin = _ArrisRouterWps50STAPin_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 10),
    _ArrisRouterWps50STAPin_Type()
)
arrisRouterWps50STAPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50STAPin.setStatus("current")


class _ArrisRouterWps50PushButton_Type(Integer32):
    """Custom type arrisRouterWps50PushButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("activatePushButton", 1),
          ("activatePINCfg", 2),
          ("cancelWPS", 3))
    )


_ArrisRouterWps50PushButton_Type.__name__ = "Integer32"
_ArrisRouterWps50PushButton_Object = MibScalar
arrisRouterWps50PushButton = _ArrisRouterWps50PushButton_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 11),
    _ArrisRouterWps50PushButton_Type()
)
arrisRouterWps50PushButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50PushButton.setStatus("current")


class _ArrisRouterWps50UUID_Type(DisplayString):
    """Custom type arrisRouterWps50UUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrisRouterWps50UUID_Type.__name__ = "DisplayString"
_ArrisRouterWps50UUID_Object = MibScalar
arrisRouterWps50UUID = _ArrisRouterWps50UUID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 65, 14),
    _ArrisRouterWps50UUID_Type()
)
arrisRouterWps50UUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWps50UUID.setStatus("current")


class _ArrisRouterWifiLowInitRate_Type(TruthValue):
    """Custom type arrisRouterWifiLowInitRate based on TruthValue"""
    defaultValue = 2


_ArrisRouterWifiLowInitRate_Type.__name__ = "TruthValue"
_ArrisRouterWifiLowInitRate_Object = MibScalar
arrisRouterWifiLowInitRate = _ArrisRouterWifiLowInitRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 66),
    _ArrisRouterWifiLowInitRate_Type()
)
arrisRouterWifiLowInitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWifiLowInitRate.setStatus("current")
_ArrisRouterWiFiBssStaSteering_ObjectIdentity = ObjectIdentity
arrisRouterWiFiBssStaSteering = _ArrisRouterWiFiBssStaSteering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69)
)


class _ArrisRouterWiFiBssStaSteeringReset_Type(TruthValue):
    """Custom type arrisRouterWiFiBssStaSteeringReset based on TruthValue"""
    defaultValue = 2


_ArrisRouterWiFiBssStaSteeringReset_Type.__name__ = "TruthValue"
_ArrisRouterWiFiBssStaSteeringReset_Object = MibScalar
arrisRouterWiFiBssStaSteeringReset = _ArrisRouterWiFiBssStaSteeringReset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 1),
    _ArrisRouterWiFiBssStaSteeringReset_Type()
)
arrisRouterWiFiBssStaSteeringReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBssStaSteeringReset.setStatus("current")


class _ArrisRouterWiFiBssStaSteeringDenyCount_Type(Integer32):
    """Custom type arrisRouterWiFiBssStaSteeringDenyCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArrisRouterWiFiBssStaSteeringDenyCount_Type.__name__ = "Integer32"
_ArrisRouterWiFiBssStaSteeringDenyCount_Object = MibScalar
arrisRouterWiFiBssStaSteeringDenyCount = _ArrisRouterWiFiBssStaSteeringDenyCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 2),
    _ArrisRouterWiFiBssStaSteeringDenyCount_Type()
)
arrisRouterWiFiBssStaSteeringDenyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBssStaSteeringDenyCount.setStatus("current")


class _ArrisRouterWiFiBssStaSteeringDenyWindow_Type(Integer32):
    """Custom type arrisRouterWiFiBssStaSteeringDenyWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_ArrisRouterWiFiBssStaSteeringDenyWindow_Type.__name__ = "Integer32"
_ArrisRouterWiFiBssStaSteeringDenyWindow_Object = MibScalar
arrisRouterWiFiBssStaSteeringDenyWindow = _ArrisRouterWiFiBssStaSteeringDenyWindow_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 3),
    _ArrisRouterWiFiBssStaSteeringDenyWindow_Type()
)
arrisRouterWiFiBssStaSteeringDenyWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiBssStaSteeringDenyWindow.setStatus("current")
_ArrisRouterBssStaSteeringTable_Object = MibTable
arrisRouterBssStaSteeringTable = _ArrisRouterBssStaSteeringTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4)
)
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringTable.setStatus("current")
_ArrisRouterBssStaSteeringEntry_Object = MibTableRow
arrisRouterBssStaSteeringEntry = _ArrisRouterBssStaSteeringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1)
)
arrisRouterBssStaSteeringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringEntry.setStatus("current")


class _ArrisRouterBssStaSteeringIndex_Type(Integer32):
    """Custom type arrisRouterBssStaSteeringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArrisRouterBssStaSteeringIndex_Type.__name__ = "Integer32"
_ArrisRouterBssStaSteeringIndex_Object = MibTableColumn
arrisRouterBssStaSteeringIndex = _ArrisRouterBssStaSteeringIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1, 1),
    _ArrisRouterBssStaSteeringIndex_Type()
)
arrisRouterBssStaSteeringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringIndex.setStatus("current")


class _ArrisRouterBssStaSteeringTableClear_Type(Integer32):
    """Custom type arrisRouterBssStaSteeringTableClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ArrisRouterBssStaSteeringTableClear_Type.__name__ = "Integer32"
_ArrisRouterBssStaSteeringTableClear_Object = MibTableColumn
arrisRouterBssStaSteeringTableClear = _ArrisRouterBssStaSteeringTableClear_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1, 2),
    _ArrisRouterBssStaSteeringTableClear_Type()
)
arrisRouterBssStaSteeringTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringTableClear.setStatus("current")


class _ArrisRouterBssStaSteeringTableDenyCount_Type(Integer32):
    """Custom type arrisRouterBssStaSteeringTableDenyCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ArrisRouterBssStaSteeringTableDenyCount_Type.__name__ = "Integer32"
_ArrisRouterBssStaSteeringTableDenyCount_Object = MibTableColumn
arrisRouterBssStaSteeringTableDenyCount = _ArrisRouterBssStaSteeringTableDenyCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1, 3),
    _ArrisRouterBssStaSteeringTableDenyCount_Type()
)
arrisRouterBssStaSteeringTableDenyCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringTableDenyCount.setStatus("current")


class _ArrisRouterBssStaSteeringTableDenyWindow_Type(Integer32):
    """Custom type arrisRouterBssStaSteeringTableDenyWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_ArrisRouterBssStaSteeringTableDenyWindow_Type.__name__ = "Integer32"
_ArrisRouterBssStaSteeringTableDenyWindow_Object = MibTableColumn
arrisRouterBssStaSteeringTableDenyWindow = _ArrisRouterBssStaSteeringTableDenyWindow_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1, 4),
    _ArrisRouterBssStaSteeringTableDenyWindow_Type()
)
arrisRouterBssStaSteeringTableDenyWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringTableDenyWindow.setStatus("current")
_ArrisRouterBssStaSteeringTableStatus_Type = RowStatus
_ArrisRouterBssStaSteeringTableStatus_Object = MibTableColumn
arrisRouterBssStaSteeringTableStatus = _ArrisRouterBssStaSteeringTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 4, 1, 5),
    _ArrisRouterBssStaSteeringTableStatus_Type()
)
arrisRouterBssStaSteeringTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringTableStatus.setStatus("current")
_ArrisRouterBssStaSteeringClientTable_Object = MibTable
arrisRouterBssStaSteeringClientTable = _ArrisRouterBssStaSteeringClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5)
)
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientTable.setStatus("current")
_ArrisRouterBssStaSteeringClientEntry_Object = MibTableRow
arrisRouterBssStaSteeringClientEntry = _ArrisRouterBssStaSteeringClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5, 1)
)
arrisRouterBssStaSteeringClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterBssStaSteeringClientIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientEntry.setStatus("current")


class _ArrisRouterBssStaSteeringClientIndex_Type(Integer32):
    """Custom type arrisRouterBssStaSteeringClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ArrisRouterBssStaSteeringClientIndex_Type.__name__ = "Integer32"
_ArrisRouterBssStaSteeringClientIndex_Object = MibTableColumn
arrisRouterBssStaSteeringClientIndex = _ArrisRouterBssStaSteeringClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5, 1, 1),
    _ArrisRouterBssStaSteeringClientIndex_Type()
)
arrisRouterBssStaSteeringClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientIndex.setStatus("current")
_ArrisRouterBssStaSteeringClientMacAddress_Type = MacAddress
_ArrisRouterBssStaSteeringClientMacAddress_Object = MibTableColumn
arrisRouterBssStaSteeringClientMacAddress = _ArrisRouterBssStaSteeringClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5, 1, 2),
    _ArrisRouterBssStaSteeringClientMacAddress_Type()
)
arrisRouterBssStaSteeringClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientMacAddress.setStatus("current")
_ArrisRouterBssStaSteeringClientLastAssocTime_Type = DateAndTime
_ArrisRouterBssStaSteeringClientLastAssocTime_Object = MibTableColumn
arrisRouterBssStaSteeringClientLastAssocTime = _ArrisRouterBssStaSteeringClientLastAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5, 1, 3),
    _ArrisRouterBssStaSteeringClientLastAssocTime_Type()
)
arrisRouterBssStaSteeringClientLastAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientLastAssocTime.setStatus("current")
_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Type = Integer32
_ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Object = MibTableColumn
arrisRouterBssStaSteeringClientOtherBssJoinedCount = _ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 69, 5, 1, 4),
    _ArrisRouterBssStaSteeringClientOtherBssJoinedCount_Type()
)
arrisRouterBssStaSteeringClientOtherBssJoinedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBssStaSteeringClientOtherBssJoinedCount.setStatus("current")


class _ArrisRouterWiFiInterworkingIE_Type(TruthValue):
    """Custom type arrisRouterWiFiInterworkingIE based on TruthValue"""
    defaultValue = 1


_ArrisRouterWiFiInterworkingIE_Type.__name__ = "TruthValue"
_ArrisRouterWiFiInterworkingIE_Object = MibScalar
arrisRouterWiFiInterworkingIE = _ArrisRouterWiFiInterworkingIE_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 70),
    _ArrisRouterWiFiInterworkingIE_Type()
)
arrisRouterWiFiInterworkingIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWiFiInterworkingIE.setStatus("current")
_ArrisRouterAirtimeCtrlCfg_ObjectIdentity = ObjectIdentity
arrisRouterAirtimeCtrlCfg = _ArrisRouterAirtimeCtrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99)
)


class _ArrisRouterAirtimeCtrlBSSIDEnable_Type(TruthValue):
    """Custom type arrisRouterAirtimeCtrlBSSIDEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterAirtimeCtrlBSSIDEnable_Type.__name__ = "TruthValue"
_ArrisRouterAirtimeCtrlBSSIDEnable_Object = MibScalar
arrisRouterAirtimeCtrlBSSIDEnable = _ArrisRouterAirtimeCtrlBSSIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99, 1),
    _ArrisRouterAirtimeCtrlBSSIDEnable_Type()
)
arrisRouterAirtimeCtrlBSSIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterAirtimeCtrlBSSIDEnable.setStatus("current")
_ArrisRouterAirtimeCtrlBSSIDWeightTable_Object = MibTable
arrisRouterAirtimeCtrlBSSIDWeightTable = _ArrisRouterAirtimeCtrlBSSIDWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99, 2)
)
if mibBuilder.loadTexts:
    arrisRouterAirtimeCtrlBSSIDWeightTable.setStatus("current")
_ArrisRouterAirtimeCtrlBSSIDWeightEntry_Object = MibTableRow
arrisRouterAirtimeCtrlBSSIDWeightEntry = _ArrisRouterAirtimeCtrlBSSIDWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99, 2, 1)
)
arrisRouterAirtimeCtrlBSSIDWeightEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterAirtimeCtrlBSSIDWeightEntry.setStatus("current")


class _ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type(Unsigned32):
    """Custom type arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type.__name__ = "Unsigned32"
_ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Object = MibTableColumn
arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage = _ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99, 2, 1, 1),
    _ArrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage_Type()
)
arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage.setStatus("current")


class _ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type(Unsigned32):
    """Custom type arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type.__name__ = "Unsigned32"
_ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Object = MibTableColumn
arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage = _ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 3, 99, 2, 1, 2),
    _ArrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage_Type()
)
arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage.setStatus("current")
_ArrisRouterFWCfg_ObjectIdentity = ObjectIdentity
arrisRouterFWCfg = _ArrisRouterFWCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4)
)


class _ArrisRouterFWEnabled_Type(TruthValue):
    """Custom type arrisRouterFWEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWEnabled_Type.__name__ = "TruthValue"
_ArrisRouterFWEnabled_Object = MibScalar
arrisRouterFWEnabled = _ArrisRouterFWEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 1),
    _ArrisRouterFWEnabled_Type()
)
arrisRouterFWEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWEnabled.setStatus("current")
_ArrisRouterFWEnableDMZ_Type = TruthValue
_ArrisRouterFWEnableDMZ_Object = MibScalar
arrisRouterFWEnableDMZ = _ArrisRouterFWEnableDMZ_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 6),
    _ArrisRouterFWEnableDMZ_Type()
)
arrisRouterFWEnableDMZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWEnableDMZ.setStatus("current")
_ArrisRouterFWIPAddrTypeDMZ_Type = InetAddressType
_ArrisRouterFWIPAddrTypeDMZ_Object = MibScalar
arrisRouterFWIPAddrTypeDMZ = _ArrisRouterFWIPAddrTypeDMZ_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 7),
    _ArrisRouterFWIPAddrTypeDMZ_Type()
)
arrisRouterFWIPAddrTypeDMZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPAddrTypeDMZ.setStatus("current")
_ArrisRouterFWIPAddrDMZ_Type = InetAddress
_ArrisRouterFWIPAddrDMZ_Object = MibScalar
arrisRouterFWIPAddrDMZ = _ArrisRouterFWIPAddrDMZ_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 8),
    _ArrisRouterFWIPAddrDMZ_Type()
)
arrisRouterFWIPAddrDMZ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPAddrDMZ.setStatus("current")


class _ArrisRouterFWSecurityLevel_Type(Integer32):
    """Custom type arrisRouterFWSecurityLevel based on Integer32"""
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
        *(("minimum", 1),
          ("medium", 2),
          ("maximum", 3),
          ("custom", 4))
    )


_ArrisRouterFWSecurityLevel_Type.__name__ = "Integer32"
_ArrisRouterFWSecurityLevel_Object = MibScalar
arrisRouterFWSecurityLevel = _ArrisRouterFWSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 9),
    _ArrisRouterFWSecurityLevel_Type()
)
arrisRouterFWSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWSecurityLevel.setStatus("current")
_ArrisRouterFWVirtSrvTable_Object = MibTable
arrisRouterFWVirtSrvTable = _ArrisRouterFWVirtSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12)
)
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvTable.setStatus("current")
_ArrisRouterFWVirtSrvEntry_Object = MibTableRow
arrisRouterFWVirtSrvEntry = _ArrisRouterFWVirtSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1)
)
arrisRouterFWVirtSrvEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWVirtSrvIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvEntry.setStatus("current")
_ArrisRouterFWVirtSrvIndex_Type = Unsigned32
_ArrisRouterFWVirtSrvIndex_Object = MibTableColumn
arrisRouterFWVirtSrvIndex = _ArrisRouterFWVirtSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 1),
    _ArrisRouterFWVirtSrvIndex_Type()
)
arrisRouterFWVirtSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvIndex.setStatus("current")


class _ArrisRouterFWVirtSrvDesc_Type(DisplayString):
    """Custom type arrisRouterFWVirtSrvDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrisRouterFWVirtSrvDesc_Type.__name__ = "DisplayString"
_ArrisRouterFWVirtSrvDesc_Object = MibTableColumn
arrisRouterFWVirtSrvDesc = _ArrisRouterFWVirtSrvDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 2),
    _ArrisRouterFWVirtSrvDesc_Type()
)
arrisRouterFWVirtSrvDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvDesc.setStatus("current")


class _ArrisRouterFWVirtSrvPortStart_Type(Unsigned32):
    """Custom type arrisRouterFWVirtSrvPortStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWVirtSrvPortStart_Type.__name__ = "Unsigned32"
_ArrisRouterFWVirtSrvPortStart_Object = MibTableColumn
arrisRouterFWVirtSrvPortStart = _ArrisRouterFWVirtSrvPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 3),
    _ArrisRouterFWVirtSrvPortStart_Type()
)
arrisRouterFWVirtSrvPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvPortStart.setStatus("current")


class _ArrisRouterFWVirtSrvPortEnd_Type(Unsigned32):
    """Custom type arrisRouterFWVirtSrvPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWVirtSrvPortEnd_Type.__name__ = "Unsigned32"
_ArrisRouterFWVirtSrvPortEnd_Object = MibTableColumn
arrisRouterFWVirtSrvPortEnd = _ArrisRouterFWVirtSrvPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 4),
    _ArrisRouterFWVirtSrvPortEnd_Type()
)
arrisRouterFWVirtSrvPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvPortEnd.setStatus("current")


class _ArrisRouterFWVirtSrvProtoType_Type(Integer32):
    """Custom type arrisRouterFWVirtSrvProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1),
          ("both", 2))
    )


_ArrisRouterFWVirtSrvProtoType_Type.__name__ = "Integer32"
_ArrisRouterFWVirtSrvProtoType_Object = MibTableColumn
arrisRouterFWVirtSrvProtoType = _ArrisRouterFWVirtSrvProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 5),
    _ArrisRouterFWVirtSrvProtoType_Type()
)
arrisRouterFWVirtSrvProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvProtoType.setStatus("current")
_ArrisRouterFWVirtSrvIPAddrType_Type = InetAddressType
_ArrisRouterFWVirtSrvIPAddrType_Object = MibTableColumn
arrisRouterFWVirtSrvIPAddrType = _ArrisRouterFWVirtSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 6),
    _ArrisRouterFWVirtSrvIPAddrType_Type()
)
arrisRouterFWVirtSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvIPAddrType.setStatus("current")
_ArrisRouterFWVirtSrvIPAddr_Type = InetAddress
_ArrisRouterFWVirtSrvIPAddr_Object = MibTableColumn
arrisRouterFWVirtSrvIPAddr = _ArrisRouterFWVirtSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 7),
    _ArrisRouterFWVirtSrvIPAddr_Type()
)
arrisRouterFWVirtSrvIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvIPAddr.setStatus("current")


class _ArrisRouterFWVirtSrvLocalPortStart_Type(Unsigned32):
    """Custom type arrisRouterFWVirtSrvLocalPortStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWVirtSrvLocalPortStart_Type.__name__ = "Unsigned32"
_ArrisRouterFWVirtSrvLocalPortStart_Object = MibTableColumn
arrisRouterFWVirtSrvLocalPortStart = _ArrisRouterFWVirtSrvLocalPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 9),
    _ArrisRouterFWVirtSrvLocalPortStart_Type()
)
arrisRouterFWVirtSrvLocalPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvLocalPortStart.setStatus("current")


class _ArrisRouterFWVirtSrvLocalPortEnd_Type(Unsigned32):
    """Custom type arrisRouterFWVirtSrvLocalPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWVirtSrvLocalPortEnd_Type.__name__ = "Unsigned32"
_ArrisRouterFWVirtSrvLocalPortEnd_Object = MibTableColumn
arrisRouterFWVirtSrvLocalPortEnd = _ArrisRouterFWVirtSrvLocalPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 10),
    _ArrisRouterFWVirtSrvLocalPortEnd_Type()
)
arrisRouterFWVirtSrvLocalPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvLocalPortEnd.setStatus("current")
_ArrisRouterFWVirtSrvRowStatus_Type = RowStatus
_ArrisRouterFWVirtSrvRowStatus_Object = MibTableColumn
arrisRouterFWVirtSrvRowStatus = _ArrisRouterFWVirtSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 11),
    _ArrisRouterFWVirtSrvRowStatus_Type()
)
arrisRouterFWVirtSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvRowStatus.setStatus("current")


class _ArrisRouterFWSrvTr69InstanceID_Type(Unsigned32):
    """Custom type arrisRouterFWSrvTr69InstanceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWSrvTr69InstanceID_Type.__name__ = "Unsigned32"
_ArrisRouterFWSrvTr69InstanceID_Object = MibTableColumn
arrisRouterFWSrvTr69InstanceID = _ArrisRouterFWSrvTr69InstanceID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 12, 1, 14),
    _ArrisRouterFWSrvTr69InstanceID_Type()
)
arrisRouterFWSrvTr69InstanceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWSrvTr69InstanceID.setStatus("current")
_ArrisRouterFWIPFilterTable_Object = MibTable
arrisRouterFWIPFilterTable = _ArrisRouterFWIPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13)
)
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterTable.setStatus("current")
_ArrisRouterFWIPFilterEntry_Object = MibTableRow
arrisRouterFWIPFilterEntry = _ArrisRouterFWIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1)
)
arrisRouterFWIPFilterEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWIPFilterIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterEntry.setStatus("current")
_ArrisRouterFWIPFilterIndex_Type = Unsigned32
_ArrisRouterFWIPFilterIndex_Object = MibTableColumn
arrisRouterFWIPFilterIndex = _ArrisRouterFWIPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 1),
    _ArrisRouterFWIPFilterIndex_Type()
)
arrisRouterFWIPFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterIndex.setStatus("current")


class _ArrisRouterFWIPFilterDesc_Type(DisplayString):
    """Custom type arrisRouterFWIPFilterDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterFWIPFilterDesc_Type.__name__ = "DisplayString"
_ArrisRouterFWIPFilterDesc_Object = MibTableColumn
arrisRouterFWIPFilterDesc = _ArrisRouterFWIPFilterDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 2),
    _ArrisRouterFWIPFilterDesc_Type()
)
arrisRouterFWIPFilterDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterDesc.setStatus("current")
_ArrisRouterFWIPFilterStartType_Type = InetAddressType
_ArrisRouterFWIPFilterStartType_Object = MibTableColumn
arrisRouterFWIPFilterStartType = _ArrisRouterFWIPFilterStartType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 3),
    _ArrisRouterFWIPFilterStartType_Type()
)
arrisRouterFWIPFilterStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterStartType.setStatus("current")
_ArrisRouterFWIPFilterStartAddr_Type = InetAddress
_ArrisRouterFWIPFilterStartAddr_Object = MibTableColumn
arrisRouterFWIPFilterStartAddr = _ArrisRouterFWIPFilterStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 4),
    _ArrisRouterFWIPFilterStartAddr_Type()
)
arrisRouterFWIPFilterStartAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterStartAddr.setStatus("current")
_ArrisRouterFWIPFilterEndType_Type = InetAddressType
_ArrisRouterFWIPFilterEndType_Object = MibTableColumn
arrisRouterFWIPFilterEndType = _ArrisRouterFWIPFilterEndType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 5),
    _ArrisRouterFWIPFilterEndType_Type()
)
arrisRouterFWIPFilterEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterEndType.setStatus("current")
_ArrisRouterFWIPFilterEndAddr_Type = InetAddress
_ArrisRouterFWIPFilterEndAddr_Object = MibTableColumn
arrisRouterFWIPFilterEndAddr = _ArrisRouterFWIPFilterEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 6),
    _ArrisRouterFWIPFilterEndAddr_Type()
)
arrisRouterFWIPFilterEndAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterEndAddr.setStatus("current")


class _ArrisRouterFWIPFilterPortStart_Type(Unsigned32):
    """Custom type arrisRouterFWIPFilterPortStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWIPFilterPortStart_Type.__name__ = "Unsigned32"
_ArrisRouterFWIPFilterPortStart_Object = MibTableColumn
arrisRouterFWIPFilterPortStart = _ArrisRouterFWIPFilterPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 7),
    _ArrisRouterFWIPFilterPortStart_Type()
)
arrisRouterFWIPFilterPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterPortStart.setStatus("current")


class _ArrisRouterFWIPFilterPortEnd_Type(Unsigned32):
    """Custom type arrisRouterFWIPFilterPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWIPFilterPortEnd_Type.__name__ = "Unsigned32"
_ArrisRouterFWIPFilterPortEnd_Object = MibTableColumn
arrisRouterFWIPFilterPortEnd = _ArrisRouterFWIPFilterPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 8),
    _ArrisRouterFWIPFilterPortEnd_Type()
)
arrisRouterFWIPFilterPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterPortEnd.setStatus("current")


class _ArrisRouterFWIPFilterProtoType_Type(Integer32):
    """Custom type arrisRouterFWIPFilterProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1),
          ("both", 2))
    )


_ArrisRouterFWIPFilterProtoType_Type.__name__ = "Integer32"
_ArrisRouterFWIPFilterProtoType_Object = MibTableColumn
arrisRouterFWIPFilterProtoType = _ArrisRouterFWIPFilterProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 9),
    _ArrisRouterFWIPFilterProtoType_Type()
)
arrisRouterFWIPFilterProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterProtoType.setStatus("current")
_ArrisRouterFWIPFilterTOD_Type = Integer32
_ArrisRouterFWIPFilterTOD_Object = MibTableColumn
arrisRouterFWIPFilterTOD = _ArrisRouterFWIPFilterTOD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 10),
    _ArrisRouterFWIPFilterTOD_Type()
)
arrisRouterFWIPFilterTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterTOD.setStatus("current")
_ArrisRouterFWIPFilterRowStatus_Type = RowStatus
_ArrisRouterFWIPFilterRowStatus_Object = MibTableColumn
arrisRouterFWIPFilterRowStatus = _ArrisRouterFWIPFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 11),
    _ArrisRouterFWIPFilterRowStatus_Type()
)
arrisRouterFWIPFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterRowStatus.setStatus("current")


class _ArrisRouterFWIPFilterAction_Type(Integer32):
    """Custom type arrisRouterFWIPFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("deny", 1))
    )


_ArrisRouterFWIPFilterAction_Type.__name__ = "Integer32"
_ArrisRouterFWIPFilterAction_Object = MibTableColumn
arrisRouterFWIPFilterAction = _ArrisRouterFWIPFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 12),
    _ArrisRouterFWIPFilterAction_Type()
)
arrisRouterFWIPFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterAction.setStatus("current")


class _ArrisRouterFWIPFilterDirection_Type(Integer32):
    """Custom type arrisRouterFWIPFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 0),
          ("outgoing", 1))
    )


_ArrisRouterFWIPFilterDirection_Type.__name__ = "Integer32"
_ArrisRouterFWIPFilterDirection_Object = MibTableColumn
arrisRouterFWIPFilterDirection = _ArrisRouterFWIPFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 13, 1, 13),
    _ArrisRouterFWIPFilterDirection_Type()
)
arrisRouterFWIPFilterDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWIPFilterDirection.setStatus("current")
_ArrisRouterFWAllowAll_Type = TruthValue
_ArrisRouterFWAllowAll_Object = MibScalar
arrisRouterFWAllowAll = _ArrisRouterFWAllowAll_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 14),
    _ArrisRouterFWAllowAll_Type()
)
arrisRouterFWAllowAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWAllowAll.setStatus("current")
_ArrisRouterFWMACFilterTable_Object = MibTable
arrisRouterFWMACFilterTable = _ArrisRouterFWMACFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15)
)
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterTable.setStatus("current")
_ArrisRouterFWMACFilterEntry_Object = MibTableRow
arrisRouterFWMACFilterEntry = _ArrisRouterFWMACFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15, 1)
)
arrisRouterFWMACFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWMACFilterIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterEntry.setStatus("current")
_ArrisRouterFWMACFilterIndex_Type = Unsigned32
_ArrisRouterFWMACFilterIndex_Object = MibTableColumn
arrisRouterFWMACFilterIndex = _ArrisRouterFWMACFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15, 1, 1),
    _ArrisRouterFWMACFilterIndex_Type()
)
arrisRouterFWMACFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterIndex.setStatus("current")
_ArrisRouterFWMACFilterAddr_Type = MacAddress
_ArrisRouterFWMACFilterAddr_Object = MibTableColumn
arrisRouterFWMACFilterAddr = _ArrisRouterFWMACFilterAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15, 1, 2),
    _ArrisRouterFWMACFilterAddr_Type()
)
arrisRouterFWMACFilterAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterAddr.setStatus("current")
_ArrisRouterFWMACFilterTOD_Type = Integer32
_ArrisRouterFWMACFilterTOD_Object = MibTableColumn
arrisRouterFWMACFilterTOD = _ArrisRouterFWMACFilterTOD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15, 1, 3),
    _ArrisRouterFWMACFilterTOD_Type()
)
arrisRouterFWMACFilterTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterTOD.setStatus("current")
_ArrisRouterFWMACFilterRowStatus_Type = RowStatus
_ArrisRouterFWMACFilterRowStatus_Object = MibTableColumn
arrisRouterFWMACFilterRowStatus = _ArrisRouterFWMACFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 15, 1, 4),
    _ArrisRouterFWMACFilterRowStatus_Type()
)
arrisRouterFWMACFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMACFilterRowStatus.setStatus("current")
_ArrisRouterFWPortTrigTable_Object = MibTable
arrisRouterFWPortTrigTable = _ArrisRouterFWPortTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16)
)
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigTable.setStatus("current")
_ArrisRouterFWPortTrigEntry_Object = MibTableRow
arrisRouterFWPortTrigEntry = _ArrisRouterFWPortTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1)
)
arrisRouterFWPortTrigEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWPortTrigIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigEntry.setStatus("current")
_ArrisRouterFWPortTrigIndex_Type = Unsigned32
_ArrisRouterFWPortTrigIndex_Object = MibTableColumn
arrisRouterFWPortTrigIndex = _ArrisRouterFWPortTrigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 1),
    _ArrisRouterFWPortTrigIndex_Type()
)
arrisRouterFWPortTrigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigIndex.setStatus("current")


class _ArrisRouterFWPortTrigDesc_Type(DisplayString):
    """Custom type arrisRouterFWPortTrigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ArrisRouterFWPortTrigDesc_Type.__name__ = "DisplayString"
_ArrisRouterFWPortTrigDesc_Object = MibTableColumn
arrisRouterFWPortTrigDesc = _ArrisRouterFWPortTrigDesc_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 2),
    _ArrisRouterFWPortTrigDesc_Type()
)
arrisRouterFWPortTrigDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigDesc.setStatus("current")


class _ArrisRouterFWPortTrigPortStart_Type(Unsigned32):
    """Custom type arrisRouterFWPortTrigPortStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWPortTrigPortStart_Type.__name__ = "Unsigned32"
_ArrisRouterFWPortTrigPortStart_Object = MibTableColumn
arrisRouterFWPortTrigPortStart = _ArrisRouterFWPortTrigPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 3),
    _ArrisRouterFWPortTrigPortStart_Type()
)
arrisRouterFWPortTrigPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigPortStart.setStatus("current")


class _ArrisRouterFWPortTrigPortEnd_Type(Unsigned32):
    """Custom type arrisRouterFWPortTrigPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWPortTrigPortEnd_Type.__name__ = "Unsigned32"
_ArrisRouterFWPortTrigPortEnd_Object = MibTableColumn
arrisRouterFWPortTrigPortEnd = _ArrisRouterFWPortTrigPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 4),
    _ArrisRouterFWPortTrigPortEnd_Type()
)
arrisRouterFWPortTrigPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigPortEnd.setStatus("current")


class _ArrisRouterFWPortTargPortStart_Type(Unsigned32):
    """Custom type arrisRouterFWPortTargPortStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWPortTargPortStart_Type.__name__ = "Unsigned32"
_ArrisRouterFWPortTargPortStart_Object = MibTableColumn
arrisRouterFWPortTargPortStart = _ArrisRouterFWPortTargPortStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 5),
    _ArrisRouterFWPortTargPortStart_Type()
)
arrisRouterFWPortTargPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTargPortStart.setStatus("current")


class _ArrisRouterFWPortTargPortEnd_Type(Unsigned32):
    """Custom type arrisRouterFWPortTargPortEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWPortTargPortEnd_Type.__name__ = "Unsigned32"
_ArrisRouterFWPortTargPortEnd_Object = MibTableColumn
arrisRouterFWPortTargPortEnd = _ArrisRouterFWPortTargPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 6),
    _ArrisRouterFWPortTargPortEnd_Type()
)
arrisRouterFWPortTargPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTargPortEnd.setStatus("current")


class _ArrisRouterFWPortTrigProtoType_Type(Integer32):
    """Custom type arrisRouterFWPortTrigProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("tcp", 1),
          ("both", 2))
    )


_ArrisRouterFWPortTrigProtoType_Type.__name__ = "Integer32"
_ArrisRouterFWPortTrigProtoType_Object = MibTableColumn
arrisRouterFWPortTrigProtoType = _ArrisRouterFWPortTrigProtoType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 7),
    _ArrisRouterFWPortTrigProtoType_Type()
)
arrisRouterFWPortTrigProtoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigProtoType.setStatus("current")
_ArrisRouterFWPortTrigRowStatus_Type = RowStatus
_ArrisRouterFWPortTrigRowStatus_Object = MibTableColumn
arrisRouterFWPortTrigRowStatus = _ArrisRouterFWPortTrigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 16, 1, 9),
    _ArrisRouterFWPortTrigRowStatus_Type()
)
arrisRouterFWPortTrigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigRowStatus.setStatus("current")
_ArrisRouterFWFilterRules_ObjectIdentity = ObjectIdentity
arrisRouterFWFilterRules = _ArrisRouterFWFilterRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17)
)


class _ArrisRouterFWBlockFragIPPkts_Type(TruthValue):
    """Custom type arrisRouterFWBlockFragIPPkts based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWBlockFragIPPkts_Type.__name__ = "TruthValue"
_ArrisRouterFWBlockFragIPPkts_Object = MibScalar
arrisRouterFWBlockFragIPPkts = _ArrisRouterFWBlockFragIPPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 6),
    _ArrisRouterFWBlockFragIPPkts_Type()
)
arrisRouterFWBlockFragIPPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWBlockFragIPPkts.setStatus("current")


class _ArrisRouterFWPortScanProtect_Type(TruthValue):
    """Custom type arrisRouterFWPortScanProtect based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWPortScanProtect_Type.__name__ = "TruthValue"
_ArrisRouterFWPortScanProtect_Object = MibScalar
arrisRouterFWPortScanProtect = _ArrisRouterFWPortScanProtect_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 7),
    _ArrisRouterFWPortScanProtect_Type()
)
arrisRouterFWPortScanProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPortScanProtect.setStatus("current")


class _ArrisRouterFWIPFloodDetect_Type(TruthValue):
    """Custom type arrisRouterFWIPFloodDetect based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWIPFloodDetect_Type.__name__ = "TruthValue"
_ArrisRouterFWIPFloodDetect_Object = MibScalar
arrisRouterFWIPFloodDetect = _ArrisRouterFWIPFloodDetect_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 8),
    _ArrisRouterFWIPFloodDetect_Type()
)
arrisRouterFWIPFloodDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPFloodDetect.setStatus("current")


class _ArrisRouterFWBlockFragIPPktsV4_Type(TruthValue):
    """Custom type arrisRouterFWBlockFragIPPktsV4 based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWBlockFragIPPktsV4_Type.__name__ = "TruthValue"
_ArrisRouterFWBlockFragIPPktsV4_Object = MibScalar
arrisRouterFWBlockFragIPPktsV4 = _ArrisRouterFWBlockFragIPPktsV4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 9),
    _ArrisRouterFWBlockFragIPPktsV4_Type()
)
arrisRouterFWBlockFragIPPktsV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWBlockFragIPPktsV4.setStatus("current")


class _ArrisRouterFWPortScanProtectV4_Type(TruthValue):
    """Custom type arrisRouterFWPortScanProtectV4 based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWPortScanProtectV4_Type.__name__ = "TruthValue"
_ArrisRouterFWPortScanProtectV4_Object = MibScalar
arrisRouterFWPortScanProtectV4 = _ArrisRouterFWPortScanProtectV4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 10),
    _ArrisRouterFWPortScanProtectV4_Type()
)
arrisRouterFWPortScanProtectV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPortScanProtectV4.setStatus("current")


class _ArrisRouterFWIPFloodDetectV4_Type(TruthValue):
    """Custom type arrisRouterFWIPFloodDetectV4 based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWIPFloodDetectV4_Type.__name__ = "TruthValue"
_ArrisRouterFWIPFloodDetectV4_Object = MibScalar
arrisRouterFWIPFloodDetectV4 = _ArrisRouterFWIPFloodDetectV4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 11),
    _ArrisRouterFWIPFloodDetectV4_Type()
)
arrisRouterFWIPFloodDetectV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPFloodDetectV4.setStatus("current")


class _ArrisRouterFWBlockFragIPPktsV6_Type(TruthValue):
    """Custom type arrisRouterFWBlockFragIPPktsV6 based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWBlockFragIPPktsV6_Type.__name__ = "TruthValue"
_ArrisRouterFWBlockFragIPPktsV6_Object = MibScalar
arrisRouterFWBlockFragIPPktsV6 = _ArrisRouterFWBlockFragIPPktsV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 12),
    _ArrisRouterFWBlockFragIPPktsV6_Type()
)
arrisRouterFWBlockFragIPPktsV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWBlockFragIPPktsV6.setStatus("current")


class _ArrisRouterFWPortScanProtectV6_Type(TruthValue):
    """Custom type arrisRouterFWPortScanProtectV6 based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWPortScanProtectV6_Type.__name__ = "TruthValue"
_ArrisRouterFWPortScanProtectV6_Object = MibScalar
arrisRouterFWPortScanProtectV6 = _ArrisRouterFWPortScanProtectV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 13),
    _ArrisRouterFWPortScanProtectV6_Type()
)
arrisRouterFWPortScanProtectV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPortScanProtectV6.setStatus("current")


class _ArrisRouterFWIPFloodDetectV6_Type(TruthValue):
    """Custom type arrisRouterFWIPFloodDetectV6 based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWIPFloodDetectV6_Type.__name__ = "TruthValue"
_ArrisRouterFWIPFloodDetectV6_Object = MibScalar
arrisRouterFWIPFloodDetectV6 = _ArrisRouterFWIPFloodDetectV6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 17, 14),
    _ArrisRouterFWIPFloodDetectV6_Type()
)
arrisRouterFWIPFloodDetectV6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPFloodDetectV6.setStatus("current")
_ArrisRouterFWDDNSObjs_ObjectIdentity = ObjectIdentity
arrisRouterFWDDNSObjs = _ArrisRouterFWDDNSObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18)
)


class _ArrisRouterFWDDNSEnable_Type(TruthValue):
    """Custom type arrisRouterFWDDNSEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWDDNSEnable_Type.__name__ = "TruthValue"
_ArrisRouterFWDDNSEnable_Object = MibScalar
arrisRouterFWDDNSEnable = _ArrisRouterFWDDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 1),
    _ArrisRouterFWDDNSEnable_Type()
)
arrisRouterFWDDNSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSEnable.setStatus("current")


class _ArrisRouterFWDDNSType_Type(Integer32):
    """Custom type arrisRouterFWDDNSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dynDNS", 1),
          ("tzo", 2),
          ("freeDNS", 3),
          ("zoneEdit", 4),
          ("noIP", 5),
          ("easyDNS", 6),
          ("domainsGoogle", 7))
    )


_ArrisRouterFWDDNSType_Type.__name__ = "Integer32"
_ArrisRouterFWDDNSType_Object = MibScalar
arrisRouterFWDDNSType = _ArrisRouterFWDDNSType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 2),
    _ArrisRouterFWDDNSType_Type()
)
arrisRouterFWDDNSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSType.setStatus("current")


class _ArrisRouterFWDDNSUserName_Type(DisplayString):
    """Custom type arrisRouterFWDDNSUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterFWDDNSUserName_Type.__name__ = "DisplayString"
_ArrisRouterFWDDNSUserName_Object = MibScalar
arrisRouterFWDDNSUserName = _ArrisRouterFWDDNSUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 3),
    _ArrisRouterFWDDNSUserName_Type()
)
arrisRouterFWDDNSUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSUserName.setStatus("current")


class _ArrisRouterFWDDNSPassword_Type(DisplayString):
    """Custom type arrisRouterFWDDNSPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterFWDDNSPassword_Type.__name__ = "DisplayString"
_ArrisRouterFWDDNSPassword_Object = MibScalar
arrisRouterFWDDNSPassword = _ArrisRouterFWDDNSPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 4),
    _ArrisRouterFWDDNSPassword_Type()
)
arrisRouterFWDDNSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSPassword.setStatus("current")


class _ArrisRouterFWDDNSDomainName_Type(DisplayString):
    """Custom type arrisRouterFWDDNSDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterFWDDNSDomainName_Type.__name__ = "DisplayString"
_ArrisRouterFWDDNSDomainName_Object = MibScalar
arrisRouterFWDDNSDomainName = _ArrisRouterFWDDNSDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 5),
    _ArrisRouterFWDDNSDomainName_Type()
)
arrisRouterFWDDNSDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSDomainName.setStatus("current")
_ArrisRouterFWDDNSIPAddrType_Type = InetAddressType
_ArrisRouterFWDDNSIPAddrType_Object = MibScalar
arrisRouterFWDDNSIPAddrType = _ArrisRouterFWDDNSIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 6),
    _ArrisRouterFWDDNSIPAddrType_Type()
)
arrisRouterFWDDNSIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSIPAddrType.setStatus("current")
_ArrisRouterFWDDNSIPAddr_Type = InetAddress
_ArrisRouterFWDDNSIPAddr_Object = MibScalar
arrisRouterFWDDNSIPAddr = _ArrisRouterFWDDNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 7),
    _ArrisRouterFWDDNSIPAddr_Type()
)
arrisRouterFWDDNSIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSIPAddr.setStatus("current")


class _ArrisRouterFWDDNSStatus_Type(DisplayString):
    """Custom type arrisRouterFWDDNSStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterFWDDNSStatus_Type.__name__ = "DisplayString"
_ArrisRouterFWDDNSStatus_Object = MibScalar
arrisRouterFWDDNSStatus = _ArrisRouterFWDDNSStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 18, 8),
    _ArrisRouterFWDDNSStatus_Type()
)
arrisRouterFWDDNSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWDDNSStatus.setStatus("current")
_ArrisRouterFWFeatures_ObjectIdentity = ObjectIdentity
arrisRouterFWFeatures = _ArrisRouterFWFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19)
)


class _ArrisRouterFWIPSecPassThru_Type(TruthValue):
    """Custom type arrisRouterFWIPSecPassThru based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWIPSecPassThru_Type.__name__ = "TruthValue"
_ArrisRouterFWIPSecPassThru_Object = MibScalar
arrisRouterFWIPSecPassThru = _ArrisRouterFWIPSecPassThru_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 2),
    _ArrisRouterFWIPSecPassThru_Type()
)
arrisRouterFWIPSecPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPSecPassThru.setStatus("current")


class _ArrisRouterFWPPTPPassThru_Type(TruthValue):
    """Custom type arrisRouterFWPPTPPassThru based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWPPTPPassThru_Type.__name__ = "TruthValue"
_ArrisRouterFWPPTPPassThru_Object = MibScalar
arrisRouterFWPPTPPassThru = _ArrisRouterFWPPTPPassThru_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 3),
    _ArrisRouterFWPPTPPassThru_Type()
)
arrisRouterFWPPTPPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPPTPPassThru.setStatus("current")


class _ArrisRouterFWEnableMulticast_Type(TruthValue):
    """Custom type arrisRouterFWEnableMulticast based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWEnableMulticast_Type.__name__ = "TruthValue"
_ArrisRouterFWEnableMulticast_Object = MibScalar
arrisRouterFWEnableMulticast = _ArrisRouterFWEnableMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 4),
    _ArrisRouterFWEnableMulticast_Type()
)
arrisRouterFWEnableMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWEnableMulticast.setStatus("current")


class _ArrisRouterFWEnableRemoteMgmt_Type(TruthValue):
    """Custom type arrisRouterFWEnableRemoteMgmt based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWEnableRemoteMgmt_Type.__name__ = "TruthValue"
_ArrisRouterFWEnableRemoteMgmt_Object = MibScalar
arrisRouterFWEnableRemoteMgmt = _ArrisRouterFWEnableRemoteMgmt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 5),
    _ArrisRouterFWEnableRemoteMgmt_Type()
)
arrisRouterFWEnableRemoteMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWEnableRemoteMgmt.setStatus("current")


class _ArrisRouterFWL2TPPassThru_Type(TruthValue):
    """Custom type arrisRouterFWL2TPPassThru based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWL2TPPassThru_Type.__name__ = "TruthValue"
_ArrisRouterFWL2TPPassThru_Object = MibScalar
arrisRouterFWL2TPPassThru = _ArrisRouterFWL2TPPassThru_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 7),
    _ArrisRouterFWL2TPPassThru_Type()
)
arrisRouterFWL2TPPassThru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWL2TPPassThru.setStatus("current")
_ArrisRouterFWRemoteMgmt_ObjectIdentity = ObjectIdentity
arrisRouterFWRemoteMgmt = _ArrisRouterFWRemoteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12)
)


class _ArrisRouterFWRemoteMgmtHttp_Type(TruthValue):
    """Custom type arrisRouterFWRemoteMgmtHttp based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWRemoteMgmtHttp_Type.__name__ = "TruthValue"
_ArrisRouterFWRemoteMgmtHttp_Object = MibScalar
arrisRouterFWRemoteMgmtHttp = _ArrisRouterFWRemoteMgmtHttp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 1),
    _ArrisRouterFWRemoteMgmtHttp_Type()
)
arrisRouterFWRemoteMgmtHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtHttp.setStatus("current")


class _ArrisRouterFWRemoteMgmtHttps_Type(TruthValue):
    """Custom type arrisRouterFWRemoteMgmtHttps based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWRemoteMgmtHttps_Type.__name__ = "TruthValue"
_ArrisRouterFWRemoteMgmtHttps_Object = MibScalar
arrisRouterFWRemoteMgmtHttps = _ArrisRouterFWRemoteMgmtHttps_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 2),
    _ArrisRouterFWRemoteMgmtHttps_Type()
)
arrisRouterFWRemoteMgmtHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtHttps.setStatus("current")


class _ArrisRouterFWRemoteMgmtHttpPort_Type(Integer32):
    """Custom type arrisRouterFWRemoteMgmtHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterFWRemoteMgmtHttpPort_Type.__name__ = "Integer32"
_ArrisRouterFWRemoteMgmtHttpPort_Object = MibScalar
arrisRouterFWRemoteMgmtHttpPort = _ArrisRouterFWRemoteMgmtHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 3),
    _ArrisRouterFWRemoteMgmtHttpPort_Type()
)
arrisRouterFWRemoteMgmtHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtHttpPort.setStatus("current")


class _ArrisRouterFWRemoteMgmtHttpsPort_Type(Integer32):
    """Custom type arrisRouterFWRemoteMgmtHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterFWRemoteMgmtHttpsPort_Type.__name__ = "Integer32"
_ArrisRouterFWRemoteMgmtHttpsPort_Object = MibScalar
arrisRouterFWRemoteMgmtHttpsPort = _ArrisRouterFWRemoteMgmtHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 4),
    _ArrisRouterFWRemoteMgmtHttpsPort_Type()
)
arrisRouterFWRemoteMgmtHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtHttpsPort.setStatus("current")


class _ArrisRouterFWRemoteMgmtAllowedType_Type(Integer32):
    """Custom type arrisRouterFWRemoteMgmtAllowedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleComputer", 1),
          ("rangeOfIP", 2),
          ("anyComputer", 3))
    )


_ArrisRouterFWRemoteMgmtAllowedType_Type.__name__ = "Integer32"
_ArrisRouterFWRemoteMgmtAllowedType_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedType = _ArrisRouterFWRemoteMgmtAllowedType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 5),
    _ArrisRouterFWRemoteMgmtAllowedType_Type()
)
arrisRouterFWRemoteMgmtAllowedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedType.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedIPv4_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedIPv4_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedIPv4 = _ArrisRouterFWRemoteMgmtAllowedIPv4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 6),
    _ArrisRouterFWRemoteMgmtAllowedIPv4_Type()
)
arrisRouterFWRemoteMgmtAllowedIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedIPv4.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedIPv6_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedIPv6_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedIPv6 = _ArrisRouterFWRemoteMgmtAllowedIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 7),
    _ArrisRouterFWRemoteMgmtAllowedIPv6_Type()
)
arrisRouterFWRemoteMgmtAllowedIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedIPv6.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedStartIPv4_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedStartIPv4 = _ArrisRouterFWRemoteMgmtAllowedStartIPv4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 8),
    _ArrisRouterFWRemoteMgmtAllowedStartIPv4_Type()
)
arrisRouterFWRemoteMgmtAllowedStartIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedStartIPv4.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedEndIPv4_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedEndIPv4 = _ArrisRouterFWRemoteMgmtAllowedEndIPv4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 9),
    _ArrisRouterFWRemoteMgmtAllowedEndIPv4_Type()
)
arrisRouterFWRemoteMgmtAllowedEndIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedEndIPv4.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedStartIPv6_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedStartIPv6 = _ArrisRouterFWRemoteMgmtAllowedStartIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 10),
    _ArrisRouterFWRemoteMgmtAllowedStartIPv6_Type()
)
arrisRouterFWRemoteMgmtAllowedStartIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedStartIPv6.setStatus("current")
_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Type = InetAddress
_ArrisRouterFWRemoteMgmtAllowedEndIPv6_Object = MibScalar
arrisRouterFWRemoteMgmtAllowedEndIPv6 = _ArrisRouterFWRemoteMgmtAllowedEndIPv6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 11),
    _ArrisRouterFWRemoteMgmtAllowedEndIPv6_Type()
)
arrisRouterFWRemoteMgmtAllowedEndIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtAllowedEndIPv6.setStatus("current")


class _ArrisRouterFWRemoteMgmtTelnet_Type(TruthValue):
    """Custom type arrisRouterFWRemoteMgmtTelnet based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWRemoteMgmtTelnet_Type.__name__ = "TruthValue"
_ArrisRouterFWRemoteMgmtTelnet_Object = MibScalar
arrisRouterFWRemoteMgmtTelnet = _ArrisRouterFWRemoteMgmtTelnet_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 12, 12),
    _ArrisRouterFWRemoteMgmtTelnet_Type()
)
arrisRouterFWRemoteMgmtTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWRemoteMgmtTelnet.setStatus("current")
_ArrisRouterFWSelectRemoteMgmt_Type = TruthValue
_ArrisRouterFWSelectRemoteMgmt_Object = MibScalar
arrisRouterFWSelectRemoteMgmt = _ArrisRouterFWSelectRemoteMgmt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 19, 13),
    _ArrisRouterFWSelectRemoteMgmt_Type()
)
arrisRouterFWSelectRemoteMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWSelectRemoteMgmt.setStatus("current")
_ArrisRouterFWParentalControls_ObjectIdentity = ObjectIdentity
arrisRouterFWParentalControls = _ArrisRouterFWParentalControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20)
)
_ArrisRouterKeywordCount_Type = Integer32
_ArrisRouterKeywordCount_Object = MibScalar
arrisRouterKeywordCount = _ArrisRouterKeywordCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 1),
    _ArrisRouterKeywordCount_Type()
)
arrisRouterKeywordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterKeywordCount.setStatus("current")
_ArrisRouterBlackListCount_Type = Integer32
_ArrisRouterBlackListCount_Object = MibScalar
arrisRouterBlackListCount = _ArrisRouterBlackListCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 3),
    _ArrisRouterBlackListCount_Type()
)
arrisRouterBlackListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBlackListCount.setStatus("current")
_ArrisRouterWhiteListCount_Type = Integer32
_ArrisRouterWhiteListCount_Object = MibScalar
arrisRouterWhiteListCount = _ArrisRouterWhiteListCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 5),
    _ArrisRouterWhiteListCount_Type()
)
arrisRouterWhiteListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWhiteListCount.setStatus("current")
_ArrisRouterKeywordBlkTable_Object = MibTable
arrisRouterKeywordBlkTable = _ArrisRouterKeywordBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10)
)
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkTable.setStatus("current")
_ArrisRouterKeywordBlkEntry_Object = MibTableRow
arrisRouterKeywordBlkEntry = _ArrisRouterKeywordBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10, 1)
)
arrisRouterKeywordBlkEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterKeywordBlkIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkEntry.setStatus("current")


class _ArrisRouterKeywordBlkIndex_Type(Integer32):
    """Custom type arrisRouterKeywordBlkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ArrisRouterKeywordBlkIndex_Type.__name__ = "Integer32"
_ArrisRouterKeywordBlkIndex_Object = MibTableColumn
arrisRouterKeywordBlkIndex = _ArrisRouterKeywordBlkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10, 1, 1),
    _ArrisRouterKeywordBlkIndex_Type()
)
arrisRouterKeywordBlkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkIndex.setStatus("current")


class _ArrisRouterKeywordBlkWord_Type(DisplayString):
    """Custom type arrisRouterKeywordBlkWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ArrisRouterKeywordBlkWord_Type.__name__ = "DisplayString"
_ArrisRouterKeywordBlkWord_Object = MibTableColumn
arrisRouterKeywordBlkWord = _ArrisRouterKeywordBlkWord_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10, 1, 2),
    _ArrisRouterKeywordBlkWord_Type()
)
arrisRouterKeywordBlkWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkWord.setStatus("current")
_ArrisRouterKeywordBlkTOD_Type = Integer32
_ArrisRouterKeywordBlkTOD_Object = MibTableColumn
arrisRouterKeywordBlkTOD = _ArrisRouterKeywordBlkTOD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10, 1, 3),
    _ArrisRouterKeywordBlkTOD_Type()
)
arrisRouterKeywordBlkTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkTOD.setStatus("current")
_ArrisRouterKeywordBlkStatus_Type = RowStatus
_ArrisRouterKeywordBlkStatus_Object = MibTableColumn
arrisRouterKeywordBlkStatus = _ArrisRouterKeywordBlkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 10, 1, 4),
    _ArrisRouterKeywordBlkStatus_Type()
)
arrisRouterKeywordBlkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterKeywordBlkStatus.setStatus("current")
_ArrisRouterBlackListTable_Object = MibTable
arrisRouterBlackListTable = _ArrisRouterBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12)
)
if mibBuilder.loadTexts:
    arrisRouterBlackListTable.setStatus("current")
_ArrisRouterBlackListEntry_Object = MibTableRow
arrisRouterBlackListEntry = _ArrisRouterBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12, 1)
)
arrisRouterBlackListEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterBlackListIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterBlackListEntry.setStatus("current")


class _ArrisRouterBlackListIndex_Type(Integer32):
    """Custom type arrisRouterBlackListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArrisRouterBlackListIndex_Type.__name__ = "Integer32"
_ArrisRouterBlackListIndex_Object = MibTableColumn
arrisRouterBlackListIndex = _ArrisRouterBlackListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12, 1, 1),
    _ArrisRouterBlackListIndex_Type()
)
arrisRouterBlackListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterBlackListIndex.setStatus("current")


class _ArrisRouterBlackListDomain_Type(DisplayString):
    """Custom type arrisRouterBlackListDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterBlackListDomain_Type.__name__ = "DisplayString"
_ArrisRouterBlackListDomain_Object = MibTableColumn
arrisRouterBlackListDomain = _ArrisRouterBlackListDomain_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12, 1, 2),
    _ArrisRouterBlackListDomain_Type()
)
arrisRouterBlackListDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBlackListDomain.setStatus("current")
_ArrisRouterBlackListTOD_Type = Integer32
_ArrisRouterBlackListTOD_Object = MibTableColumn
arrisRouterBlackListTOD = _ArrisRouterBlackListTOD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12, 1, 3),
    _ArrisRouterBlackListTOD_Type()
)
arrisRouterBlackListTOD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBlackListTOD.setStatus("current")
_ArrisRouterBlackListStatus_Type = RowStatus
_ArrisRouterBlackListStatus_Object = MibTableColumn
arrisRouterBlackListStatus = _ArrisRouterBlackListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 12, 1, 4),
    _ArrisRouterBlackListStatus_Type()
)
arrisRouterBlackListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterBlackListStatus.setStatus("current")
_ArrisRouterWhiteListTable_Object = MibTable
arrisRouterWhiteListTable = _ArrisRouterWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14)
)
if mibBuilder.loadTexts:
    arrisRouterWhiteListTable.setStatus("current")
_ArrisRouterWhiteListEntry_Object = MibTableRow
arrisRouterWhiteListEntry = _ArrisRouterWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14, 1)
)
arrisRouterWhiteListEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWhiteListIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWhiteListEntry.setStatus("current")


class _ArrisRouterWhiteListIndex_Type(Integer32):
    """Custom type arrisRouterWhiteListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArrisRouterWhiteListIndex_Type.__name__ = "Integer32"
_ArrisRouterWhiteListIndex_Object = MibTableColumn
arrisRouterWhiteListIndex = _ArrisRouterWhiteListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14, 1, 1),
    _ArrisRouterWhiteListIndex_Type()
)
arrisRouterWhiteListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWhiteListIndex.setStatus("current")


class _ArrisRouterWhiteListDomain_Type(DisplayString):
    """Custom type arrisRouterWhiteListDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterWhiteListDomain_Type.__name__ = "DisplayString"
_ArrisRouterWhiteListDomain_Object = MibTableColumn
arrisRouterWhiteListDomain = _ArrisRouterWhiteListDomain_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14, 1, 2),
    _ArrisRouterWhiteListDomain_Type()
)
arrisRouterWhiteListDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWhiteListDomain.setStatus("current")
_ArrisRouterWhiteListTOD_Type = Integer32
_ArrisRouterWhiteListTOD_Object = MibTableColumn
arrisRouterWhiteListTOD = _ArrisRouterWhiteListTOD_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14, 1, 3),
    _ArrisRouterWhiteListTOD_Type()
)
arrisRouterWhiteListTOD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWhiteListTOD.setStatus("current")
_ArrisRouterWhiteListStatus_Type = RowStatus
_ArrisRouterWhiteListStatus_Object = MibTableColumn
arrisRouterWhiteListStatus = _ArrisRouterWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 14, 1, 4),
    _ArrisRouterWhiteListStatus_Type()
)
arrisRouterWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWhiteListStatus.setStatus("current")
_ArrisRouterTrustedDeviceTable_Object = MibTable
arrisRouterTrustedDeviceTable = _ArrisRouterTrustedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16)
)
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceTable.setStatus("current")
_ArrisRouterTrustedDeviceEntry_Object = MibTableRow
arrisRouterTrustedDeviceEntry = _ArrisRouterTrustedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1)
)
arrisRouterTrustedDeviceEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterTrustedDeviceIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceEntry.setStatus("current")


class _ArrisRouterTrustedDeviceIndex_Type(Integer32):
    """Custom type arrisRouterTrustedDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisRouterTrustedDeviceIndex_Type.__name__ = "Integer32"
_ArrisRouterTrustedDeviceIndex_Object = MibTableColumn
arrisRouterTrustedDeviceIndex = _ArrisRouterTrustedDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 1),
    _ArrisRouterTrustedDeviceIndex_Type()
)
arrisRouterTrustedDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceIndex.setStatus("current")
_ArrisRouterTrustedDeviceMAC_Type = MacAddress
_ArrisRouterTrustedDeviceMAC_Object = MibTableColumn
arrisRouterTrustedDeviceMAC = _ArrisRouterTrustedDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 2),
    _ArrisRouterTrustedDeviceMAC_Type()
)
arrisRouterTrustedDeviceMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceMAC.setStatus("current")
_ArrisRouterTrustedDeviceStatus_Type = RowStatus
_ArrisRouterTrustedDeviceStatus_Object = MibTableColumn
arrisRouterTrustedDeviceStatus = _ArrisRouterTrustedDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 3),
    _ArrisRouterTrustedDeviceStatus_Type()
)
arrisRouterTrustedDeviceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceStatus.setStatus("current")
_ArrisRouterTrustedDeviceName_Type = DisplayString
_ArrisRouterTrustedDeviceName_Object = MibTableColumn
arrisRouterTrustedDeviceName = _ArrisRouterTrustedDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 4),
    _ArrisRouterTrustedDeviceName_Type()
)
arrisRouterTrustedDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceName.setStatus("current")
_ArrisRouterTrustedDeviceAddrType_Type = InetAddressType
_ArrisRouterTrustedDeviceAddrType_Object = MibTableColumn
arrisRouterTrustedDeviceAddrType = _ArrisRouterTrustedDeviceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 5),
    _ArrisRouterTrustedDeviceAddrType_Type()
)
arrisRouterTrustedDeviceAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceAddrType.setStatus("current")
_ArrisRouterTrustedDeviceAddr_Type = InetAddress
_ArrisRouterTrustedDeviceAddr_Object = MibTableColumn
arrisRouterTrustedDeviceAddr = _ArrisRouterTrustedDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 16, 1, 6),
    _ArrisRouterTrustedDeviceAddr_Type()
)
arrisRouterTrustedDeviceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterTrustedDeviceAddr.setStatus("current")


class _ArrisRouterEnableParentalCont_Type(TruthValue):
    """Custom type arrisRouterEnableParentalCont based on TruthValue"""
    defaultValue = 2


_ArrisRouterEnableParentalCont_Type.__name__ = "TruthValue"
_ArrisRouterEnableParentalCont_Object = MibScalar
arrisRouterEnableParentalCont = _ArrisRouterEnableParentalCont_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 17),
    _ArrisRouterEnableParentalCont_Type()
)
arrisRouterEnableParentalCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEnableParentalCont.setStatus("current")


class _ArrisRouterListActiveType_Type(Integer32):
    """Custom type arrisRouterListActiveType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blackList", 1),
          ("whiteList", 2))
    )


_ArrisRouterListActiveType_Type.__name__ = "Integer32"
_ArrisRouterListActiveType_Object = MibScalar
arrisRouterListActiveType = _ArrisRouterListActiveType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 22),
    _ArrisRouterListActiveType_Type()
)
arrisRouterListActiveType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterListActiveType.setStatus("current")
_ArrisRouterExceptionListCount_Type = Integer32
_ArrisRouterExceptionListCount_Object = MibScalar
arrisRouterExceptionListCount = _ArrisRouterExceptionListCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 24),
    _ArrisRouterExceptionListCount_Type()
)
arrisRouterExceptionListCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterExceptionListCount.setStatus("current")
_ArrisRouterExceptionListTable_Object = MibTable
arrisRouterExceptionListTable = _ArrisRouterExceptionListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 25)
)
if mibBuilder.loadTexts:
    arrisRouterExceptionListTable.setStatus("current")
_ArrisRouterExceptionListEntry_Object = MibTableRow
arrisRouterExceptionListEntry = _ArrisRouterExceptionListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 25, 1)
)
arrisRouterExceptionListEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterExceptionListIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterExceptionListEntry.setStatus("current")


class _ArrisRouterExceptionListIndex_Type(Integer32):
    """Custom type arrisRouterExceptionListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ArrisRouterExceptionListIndex_Type.__name__ = "Integer32"
_ArrisRouterExceptionListIndex_Object = MibTableColumn
arrisRouterExceptionListIndex = _ArrisRouterExceptionListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 25, 1, 1),
    _ArrisRouterExceptionListIndex_Type()
)
arrisRouterExceptionListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterExceptionListIndex.setStatus("current")


class _ArrisRouterExceptionListDomain_Type(DisplayString):
    """Custom type arrisRouterExceptionListDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterExceptionListDomain_Type.__name__ = "DisplayString"
_ArrisRouterExceptionListDomain_Object = MibTableColumn
arrisRouterExceptionListDomain = _ArrisRouterExceptionListDomain_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 25, 1, 2),
    _ArrisRouterExceptionListDomain_Type()
)
arrisRouterExceptionListDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterExceptionListDomain.setStatus("current")
_ArrisRouterExceptionListStatus_Type = RowStatus
_ArrisRouterExceptionListStatus_Object = MibTableColumn
arrisRouterExceptionListStatus = _ArrisRouterExceptionListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 20, 25, 1, 3),
    _ArrisRouterExceptionListStatus_Type()
)
arrisRouterExceptionListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterExceptionListStatus.setStatus("current")


class _ArrisRouterFWAllowICMP_Type(TruthValue):
    """Custom type arrisRouterFWAllowICMP based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWAllowICMP_Type.__name__ = "TruthValue"
_ArrisRouterFWAllowICMP_Object = MibScalar
arrisRouterFWAllowICMP = _ArrisRouterFWAllowICMP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 21),
    _ArrisRouterFWAllowICMP_Type()
)
arrisRouterFWAllowICMP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWAllowICMP.setStatus("current")


class _ArrisRouterFWVirtSrvTableEnabled_Type(TruthValue):
    """Custom type arrisRouterFWVirtSrvTableEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWVirtSrvTableEnabled_Type.__name__ = "TruthValue"
_ArrisRouterFWVirtSrvTableEnabled_Object = MibScalar
arrisRouterFWVirtSrvTableEnabled = _ArrisRouterFWVirtSrvTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 32),
    _ArrisRouterFWVirtSrvTableEnabled_Type()
)
arrisRouterFWVirtSrvTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWVirtSrvTableEnabled.setStatus("current")


class _ArrisRouterFWPortTrigTableEnabled_Type(TruthValue):
    """Custom type arrisRouterFWPortTrigTableEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWPortTrigTableEnabled_Type.__name__ = "TruthValue"
_ArrisRouterFWPortTrigTableEnabled_Object = MibScalar
arrisRouterFWPortTrigTableEnabled = _ArrisRouterFWPortTrigTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 33),
    _ArrisRouterFWPortTrigTableEnabled_Type()
)
arrisRouterFWPortTrigTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPortTrigTableEnabled.setStatus("current")
_ArrisRouterFWIPv6Security_ObjectIdentity = ObjectIdentity
arrisRouterFWIPv6Security = _ArrisRouterFWIPv6Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 40)
)


class _ArrisRouterFWIPv6Enable_Type(TruthValue):
    """Custom type arrisRouterFWIPv6Enable based on TruthValue"""
    defaultValue = 1


_ArrisRouterFWIPv6Enable_Type.__name__ = "TruthValue"
_ArrisRouterFWIPv6Enable_Object = MibScalar
arrisRouterFWIPv6Enable = _ArrisRouterFWIPv6Enable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 40, 7),
    _ArrisRouterFWIPv6Enable_Type()
)
arrisRouterFWIPv6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWIPv6Enable.setStatus("current")


class _ArrisRouterFWMacBridgingWebPageEnabled_Type(TruthValue):
    """Custom type arrisRouterFWMacBridgingWebPageEnabled based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWMacBridgingWebPageEnabled_Type.__name__ = "TruthValue"
_ArrisRouterFWMacBridgingWebPageEnabled_Object = MibScalar
arrisRouterFWMacBridgingWebPageEnabled = _ArrisRouterFWMacBridgingWebPageEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 41),
    _ArrisRouterFWMacBridgingWebPageEnabled_Type()
)
arrisRouterFWMacBridgingWebPageEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingWebPageEnabled.setStatus("current")


class _ArrisRouterFWMacBridgingFunctionEnabled_Type(TruthValue):
    """Custom type arrisRouterFWMacBridgingFunctionEnabled based on TruthValue"""
    defaultValue = 2


_ArrisRouterFWMacBridgingFunctionEnabled_Type.__name__ = "TruthValue"
_ArrisRouterFWMacBridgingFunctionEnabled_Object = MibScalar
arrisRouterFWMacBridgingFunctionEnabled = _ArrisRouterFWMacBridgingFunctionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 42),
    _ArrisRouterFWMacBridgingFunctionEnabled_Type()
)
arrisRouterFWMacBridgingFunctionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingFunctionEnabled.setStatus("current")
_ArrisRouterFWMacBridgingTable_Object = MibTable
arrisRouterFWMacBridgingTable = _ArrisRouterFWMacBridgingTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43)
)
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingTable.setStatus("current")
_ArrisRouterFWMacBridgingEntry_Object = MibTableRow
arrisRouterFWMacBridgingEntry = _ArrisRouterFWMacBridgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43, 1)
)
arrisRouterFWMacBridgingEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWMacBridgingIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingEntry.setStatus("current")


class _ArrisRouterFWMacBridgingIndex_Type(Integer32):
    """Custom type arrisRouterFWMacBridgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ArrisRouterFWMacBridgingIndex_Type.__name__ = "Integer32"
_ArrisRouterFWMacBridgingIndex_Object = MibTableColumn
arrisRouterFWMacBridgingIndex = _ArrisRouterFWMacBridgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43, 1, 1),
    _ArrisRouterFWMacBridgingIndex_Type()
)
arrisRouterFWMacBridgingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingIndex.setStatus("current")


class _ArrisRouterFWMacBridgingName_Type(DisplayString):
    """Custom type arrisRouterFWMacBridgingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterFWMacBridgingName_Type.__name__ = "DisplayString"
_ArrisRouterFWMacBridgingName_Object = MibTableColumn
arrisRouterFWMacBridgingName = _ArrisRouterFWMacBridgingName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43, 1, 2),
    _ArrisRouterFWMacBridgingName_Type()
)
arrisRouterFWMacBridgingName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingName.setStatus("current")
_ArrisRouterFWMacBridgingMACAddr_Type = MacAddress
_ArrisRouterFWMacBridgingMACAddr_Object = MibTableColumn
arrisRouterFWMacBridgingMACAddr = _ArrisRouterFWMacBridgingMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43, 1, 3),
    _ArrisRouterFWMacBridgingMACAddr_Type()
)
arrisRouterFWMacBridgingMACAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingMACAddr.setStatus("current")
_ArrisRouterFWMacBridgingRowStatus_Type = RowStatus
_ArrisRouterFWMacBridgingRowStatus_Object = MibTableColumn
arrisRouterFWMacBridgingRowStatus = _ArrisRouterFWMacBridgingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 43, 1, 4),
    _ArrisRouterFWMacBridgingRowStatus_Type()
)
arrisRouterFWMacBridgingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWMacBridgingRowStatus.setStatus("current")
_ArrisRouterFWPortAllowTable_Object = MibTable
arrisRouterFWPortAllowTable = _ArrisRouterFWPortAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 44)
)
if mibBuilder.loadTexts:
    arrisRouterFWPortAllowTable.setStatus("current")
_ArrisRouterFWPortAllowEntry_Object = MibTableRow
arrisRouterFWPortAllowEntry = _ArrisRouterFWPortAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 44, 1)
)
arrisRouterFWPortAllowEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWPortAllowIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFWPortAllowEntry.setStatus("current")
_ArrisRouterFWPortAllowIndex_Type = Unsigned32
_ArrisRouterFWPortAllowIndex_Object = MibTableColumn
arrisRouterFWPortAllowIndex = _ArrisRouterFWPortAllowIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 44, 1, 1),
    _ArrisRouterFWPortAllowIndex_Type()
)
arrisRouterFWPortAllowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWPortAllowIndex.setStatus("current")


class _ArrisRouterFWPortAllowInboundPort_Type(Unsigned32):
    """Custom type arrisRouterFWPortAllowInboundPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWPortAllowInboundPort_Type.__name__ = "Unsigned32"
_ArrisRouterFWPortAllowInboundPort_Object = MibTableColumn
arrisRouterFWPortAllowInboundPort = _ArrisRouterFWPortAllowInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 44, 1, 2),
    _ArrisRouterFWPortAllowInboundPort_Type()
)
arrisRouterFWPortAllowInboundPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWPortAllowInboundPort.setStatus("current")
_ArrisRouterFWPortAllowRowStatus_Type = RowStatus
_ArrisRouterFWPortAllowRowStatus_Object = MibTableColumn
arrisRouterFWPortAllowRowStatus = _ArrisRouterFWPortAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 44, 1, 3),
    _ArrisRouterFWPortAllowRowStatus_Type()
)
arrisRouterFWPortAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterFWPortAllowRowStatus.setStatus("current")


class _ArrisRouterFWSrvTr69LastInstance_Type(Unsigned32):
    """Custom type arrisRouterFWSrvTr69LastInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ArrisRouterFWSrvTr69LastInstance_Type.__name__ = "Unsigned32"
_ArrisRouterFWSrvTr69LastInstance_Object = MibScalar
arrisRouterFWSrvTr69LastInstance = _ArrisRouterFWSrvTr69LastInstance_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 4, 46),
    _ArrisRouterFWSrvTr69LastInstance_Type()
)
arrisRouterFWSrvTr69LastInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFWSrvTr69LastInstance.setStatus("current")
_ArrisRouterSysCfg_ObjectIdentity = ObjectIdentity
arrisRouterSysCfg = _ArrisRouterSysCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5)
)


class _ArrisRouterAdminPassword_Type(DisplayString):
    """Custom type arrisRouterAdminPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterAdminPassword_Type.__name__ = "DisplayString"
_ArrisRouterAdminPassword_Object = MibScalar
arrisRouterAdminPassword = _ArrisRouterAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 1),
    _ArrisRouterAdminPassword_Type()
)
arrisRouterAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterAdminPassword.setStatus("current")


class _ArrisRouterAdminTimeout_Type(Unsigned32):
    """Custom type arrisRouterAdminTimeout based on Unsigned32"""
    defaultValue = 600


_ArrisRouterAdminTimeout_Type.__name__ = "Unsigned32"
_ArrisRouterAdminTimeout_Object = MibScalar
arrisRouterAdminTimeout = _ArrisRouterAdminTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 2),
    _ArrisRouterAdminTimeout_Type()
)
arrisRouterAdminTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterAdminTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterAdminTimeout.setUnits("seconds")
_ArrisRouterTimeZoneUTCOffset_Type = Integer32
_ArrisRouterTimeZoneUTCOffset_Object = MibScalar
arrisRouterTimeZoneUTCOffset = _ArrisRouterTimeZoneUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 3),
    _ArrisRouterTimeZoneUTCOffset_Type()
)
arrisRouterTimeZoneUTCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTimeZoneUTCOffset.setStatus("current")


class _ArrisRouterReboot_Type(Integer32):
    """Custom type arrisRouterReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_ArrisRouterReboot_Type.__name__ = "Integer32"
_ArrisRouterReboot_Object = MibScalar
arrisRouterReboot = _ArrisRouterReboot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 4),
    _ArrisRouterReboot_Type()
)
arrisRouterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterReboot.setStatus("current")


class _ArrisRouterDefaults_Type(Integer32):
    """Custom type arrisRouterDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("restoreAll", 3),
          ("restoreAllNoReboot", 6))
    )


_ArrisRouterDefaults_Type.__name__ = "Integer32"
_ArrisRouterDefaults_Object = MibScalar
arrisRouterDefaults = _ArrisRouterDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 5),
    _ArrisRouterDefaults_Type()
)
arrisRouterDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterDefaults.setStatus("current")


class _ArrisRouterLanguage_Type(DisplayString):
    """Custom type arrisRouterLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterLanguage_Type.__name__ = "DisplayString"
_ArrisRouterLanguage_Object = MibScalar
arrisRouterLanguage = _ArrisRouterLanguage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 6),
    _ArrisRouterLanguage_Type()
)
arrisRouterLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLanguage.setStatus("current")


class _ArrisRouterName_Type(DisplayString):
    """Custom type arrisRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterName_Type.__name__ = "DisplayString"
_ArrisRouterName_Object = MibScalar
arrisRouterName = _ArrisRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 7),
    _ArrisRouterName_Type()
)
arrisRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterName.setStatus("current")


class _ArrisRouterSerialNumber_Type(DisplayString):
    """Custom type arrisRouterSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterSerialNumber_Type.__name__ = "DisplayString"
_ArrisRouterSerialNumber_Object = MibScalar
arrisRouterSerialNumber = _ArrisRouterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 8),
    _ArrisRouterSerialNumber_Type()
)
arrisRouterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterSerialNumber.setStatus("current")


class _ArrisRouterBootCodeVersion_Type(DisplayString):
    """Custom type arrisRouterBootCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterBootCodeVersion_Type.__name__ = "DisplayString"
_ArrisRouterBootCodeVersion_Object = MibScalar
arrisRouterBootCodeVersion = _ArrisRouterBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 9),
    _ArrisRouterBootCodeVersion_Type()
)
arrisRouterBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterBootCodeVersion.setStatus("current")


class _ArrisRouterHardwareVersion_Type(DisplayString):
    """Custom type arrisRouterHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterHardwareVersion_Type.__name__ = "DisplayString"
_ArrisRouterHardwareVersion_Object = MibScalar
arrisRouterHardwareVersion = _ArrisRouterHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 10),
    _ArrisRouterHardwareVersion_Type()
)
arrisRouterHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterHardwareVersion.setStatus("current")


class _ArrisRouterFirmwareVersion_Type(DisplayString):
    """Custom type arrisRouterFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterFirmwareVersion_Type.__name__ = "DisplayString"
_ArrisRouterFirmwareVersion_Object = MibScalar
arrisRouterFirmwareVersion = _ArrisRouterFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 11),
    _ArrisRouterFirmwareVersion_Type()
)
arrisRouterFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFirmwareVersion.setStatus("current")


class _ArrisRouterLogLevel_Type(Integer32):
    """Custom type arrisRouterLogLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLogging", 0),
          ("logError", 1),
          ("logWarn", 2),
          ("logInfo", 3))
    )


_ArrisRouterLogLevel_Type.__name__ = "Integer32"
_ArrisRouterLogLevel_Object = MibScalar
arrisRouterLogLevel = _ArrisRouterLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 12),
    _ArrisRouterLogLevel_Type()
)
arrisRouterLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLogLevel.setStatus("current")
_ArrisRouterCustomSettings_Type = DisplayString
_ArrisRouterCustomSettings_Object = MibScalar
arrisRouterCustomSettings = _ArrisRouterCustomSettings_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 13),
    _ArrisRouterCustomSettings_Type()
)
arrisRouterCustomSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterCustomSettings.setStatus("current")
_ArrisRouterCustomID_Type = Integer32
_ArrisRouterCustomID_Object = MibScalar
arrisRouterCustomID = _ArrisRouterCustomID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 14),
    _ArrisRouterCustomID_Type()
)
arrisRouterCustomID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterCustomID.setStatus("current")
_ArrisRouterCurrentTime_Type = DateAndTime
_ArrisRouterCurrentTime_Object = MibScalar
arrisRouterCurrentTime = _ArrisRouterCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 15),
    _ArrisRouterCurrentTime_Type()
)
arrisRouterCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterCurrentTime.setStatus("current")
_ArrisRouterAuthTable_Object = MibTable
arrisRouterAuthTable = _ArrisRouterAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16)
)
if mibBuilder.loadTexts:
    arrisRouterAuthTable.setStatus("current")
_ArrisRouterAuthEntry_Object = MibTableRow
arrisRouterAuthEntry = _ArrisRouterAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1)
)
arrisRouterAuthEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWanCurrentIPIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterAuthEntry.setStatus("current")
_ArrisRouterAuthIndex_Type = Unsigned32
_ArrisRouterAuthIndex_Object = MibTableColumn
arrisRouterAuthIndex = _ArrisRouterAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1, 1),
    _ArrisRouterAuthIndex_Type()
)
arrisRouterAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterAuthIndex.setStatus("current")


class _ArrisRouterAuthUserName_Type(DisplayString):
    """Custom type arrisRouterAuthUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterAuthUserName_Type.__name__ = "DisplayString"
_ArrisRouterAuthUserName_Object = MibTableColumn
arrisRouterAuthUserName = _ArrisRouterAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1, 2),
    _ArrisRouterAuthUserName_Type()
)
arrisRouterAuthUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterAuthUserName.setStatus("current")


class _ArrisRouterAuthPassword_Type(DisplayString):
    """Custom type arrisRouterAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterAuthPassword_Type.__name__ = "DisplayString"
_ArrisRouterAuthPassword_Object = MibTableColumn
arrisRouterAuthPassword = _ArrisRouterAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1, 3),
    _ArrisRouterAuthPassword_Type()
)
arrisRouterAuthPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterAuthPassword.setStatus("current")


class _ArrisRouterAuthType_Type(DisplayString):
    """Custom type arrisRouterAuthType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterAuthType_Type.__name__ = "DisplayString"
_ArrisRouterAuthType_Object = MibTableColumn
arrisRouterAuthType = _ArrisRouterAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1, 4),
    _ArrisRouterAuthType_Type()
)
arrisRouterAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterAuthType.setStatus("current")
_ArrisRouterAuthAccountEnabled_Type = TruthValue
_ArrisRouterAuthAccountEnabled_Object = MibTableColumn
arrisRouterAuthAccountEnabled = _ArrisRouterAuthAccountEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 16, 1, 6),
    _ArrisRouterAuthAccountEnabled_Type()
)
arrisRouterAuthAccountEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterAuthAccountEnabled.setStatus("current")
_ArrisRouterSNTPSettings_ObjectIdentity = ObjectIdentity
arrisRouterSNTPSettings = _ArrisRouterSNTPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17)
)


class _ArrisRouterEnableSNTP_Type(Integer32):
    """Custom type arrisRouterEnableSNTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisRouterEnableSNTP_Type.__name__ = "Integer32"
_ArrisRouterEnableSNTP_Object = MibScalar
arrisRouterEnableSNTP = _ArrisRouterEnableSNTP_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 1),
    _ArrisRouterEnableSNTP_Type()
)
arrisRouterEnableSNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEnableSNTP.setStatus("current")
_ArrisRouterSNTPServerTable_Object = MibTable
arrisRouterSNTPServerTable = _ArrisRouterSNTPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4)
)
if mibBuilder.loadTexts:
    arrisRouterSNTPServerTable.setStatus("current")
_ArrisRouterSNTPServerEntry_Object = MibTableRow
arrisRouterSNTPServerEntry = _ArrisRouterSNTPServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1)
)
arrisRouterSNTPServerEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterSNTPServerIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterSNTPServerEntry.setStatus("current")


class _ArrisRouterSNTPServerIndex_Type(Integer32):
    """Custom type arrisRouterSNTPServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisRouterSNTPServerIndex_Type.__name__ = "Integer32"
_ArrisRouterSNTPServerIndex_Object = MibTableColumn
arrisRouterSNTPServerIndex = _ArrisRouterSNTPServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1, 1),
    _ArrisRouterSNTPServerIndex_Type()
)
arrisRouterSNTPServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterSNTPServerIndex.setStatus("current")
_ArrisRouterSNTPServerAddrType_Type = InetAddressType
_ArrisRouterSNTPServerAddrType_Object = MibTableColumn
arrisRouterSNTPServerAddrType = _ArrisRouterSNTPServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1, 2),
    _ArrisRouterSNTPServerAddrType_Type()
)
arrisRouterSNTPServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterSNTPServerAddrType.setStatus("current")
_ArrisRouterSNTPServerAddr_Type = InetAddress
_ArrisRouterSNTPServerAddr_Object = MibTableColumn
arrisRouterSNTPServerAddr = _ArrisRouterSNTPServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1, 3),
    _ArrisRouterSNTPServerAddr_Type()
)
arrisRouterSNTPServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterSNTPServerAddr.setStatus("current")


class _ArrisRouterSNTPServerName_Type(DisplayString):
    """Custom type arrisRouterSNTPServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ArrisRouterSNTPServerName_Type.__name__ = "DisplayString"
_ArrisRouterSNTPServerName_Object = MibTableColumn
arrisRouterSNTPServerName = _ArrisRouterSNTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1, 4),
    _ArrisRouterSNTPServerName_Type()
)
arrisRouterSNTPServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterSNTPServerName.setStatus("current")
_ArrisRouterSNTPServerStatus_Type = RowStatus
_ArrisRouterSNTPServerStatus_Object = MibTableColumn
arrisRouterSNTPServerStatus = _ArrisRouterSNTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 17, 4, 1, 5),
    _ArrisRouterSNTPServerStatus_Type()
)
arrisRouterSNTPServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterSNTPServerStatus.setStatus("current")
_ArrisRouterEmailSettings_ObjectIdentity = ObjectIdentity
arrisRouterEmailSettings = _ArrisRouterEmailSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18)
)
_ArrisRouterEmailServerName_Type = DisplayString
_ArrisRouterEmailServerName_Object = MibScalar
arrisRouterEmailServerName = _ArrisRouterEmailServerName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 1),
    _ArrisRouterEmailServerName_Type()
)
arrisRouterEmailServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailServerName.setStatus("current")
_ArrisRouterEmailServerUser_Type = DisplayString
_ArrisRouterEmailServerUser_Object = MibScalar
arrisRouterEmailServerUser = _ArrisRouterEmailServerUser_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 2),
    _ArrisRouterEmailServerUser_Type()
)
arrisRouterEmailServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailServerUser.setStatus("current")
_ArrisRouterEmailServerPW_Type = DisplayString
_ArrisRouterEmailServerPW_Object = MibScalar
arrisRouterEmailServerPW = _ArrisRouterEmailServerPW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 3),
    _ArrisRouterEmailServerPW_Type()
)
arrisRouterEmailServerPW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailServerPW.setStatus("current")
_ArrisRouterEmailAddress_Type = DisplayString
_ArrisRouterEmailAddress_Object = MibScalar
arrisRouterEmailAddress = _ArrisRouterEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 4),
    _ArrisRouterEmailAddress_Type()
)
arrisRouterEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailAddress.setStatus("current")


class _ArrisRouterEnableLogEmail_Type(TruthValue):
    """Custom type arrisRouterEnableLogEmail based on TruthValue"""
    defaultValue = 2


_ArrisRouterEnableLogEmail_Type.__name__ = "TruthValue"
_ArrisRouterEnableLogEmail_Object = MibScalar
arrisRouterEnableLogEmail = _ArrisRouterEnableLogEmail_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 5),
    _ArrisRouterEnableLogEmail_Type()
)
arrisRouterEnableLogEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEnableLogEmail.setStatus("current")


class _ArrisRouterEmailApplySettings_Type(Integer32):
    """Custom type arrisRouterEmailApplySettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("applySettings", 1)
    )


_ArrisRouterEmailApplySettings_Type.__name__ = "Integer32"
_ArrisRouterEmailApplySettings_Object = MibScalar
arrisRouterEmailApplySettings = _ArrisRouterEmailApplySettings_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 6),
    _ArrisRouterEmailApplySettings_Type()
)
arrisRouterEmailApplySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailApplySettings.setStatus("current")
_ArrisRouterEmailSenderAddress_Type = DisplayString
_ArrisRouterEmailSenderAddress_Object = MibScalar
arrisRouterEmailSenderAddress = _ArrisRouterEmailSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 8),
    _ArrisRouterEmailSenderAddress_Type()
)
arrisRouterEmailSenderAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailSenderAddress.setStatus("current")


class _ArrisRouterEmailSend_Type(Integer32):
    """Custom type arrisRouterEmailSend based on Integer32"""
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
          ("networkCredential", 1),
          ("modemCredential", 2))
    )


_ArrisRouterEmailSend_Type.__name__ = "Integer32"
_ArrisRouterEmailSend_Object = MibScalar
arrisRouterEmailSend = _ArrisRouterEmailSend_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 18, 9),
    _ArrisRouterEmailSend_Type()
)
arrisRouterEmailSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterEmailSend.setStatus("current")
_ArrisRouterLogSettings_ObjectIdentity = ObjectIdentity
arrisRouterLogSettings = _ArrisRouterLogSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19)
)
_ArrisRouterUserLogs_ObjectIdentity = ObjectIdentity
arrisRouterUserLogs = _ArrisRouterUserLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1)
)
_ArrisRouterFirewallLogTable_Object = MibTable
arrisRouterFirewallLogTable = _ArrisRouterFirewallLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 1)
)
if mibBuilder.loadTexts:
    arrisRouterFirewallLogTable.setStatus("current")
_ArrisRouterFirewallLogEntry_Object = MibTableRow
arrisRouterFirewallLogEntry = _ArrisRouterFirewallLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 1, 1)
)
arrisRouterFirewallLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFirewallLogEntry.setStatus("current")


class _ArrisRouterFWLogIndex_Type(Integer32):
    """Custom type arrisRouterFWLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisRouterFWLogIndex_Type.__name__ = "Integer32"
_ArrisRouterFWLogIndex_Object = MibTableColumn
arrisRouterFWLogIndex = _ArrisRouterFWLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 1, 1, 1),
    _ArrisRouterFWLogIndex_Type()
)
arrisRouterFWLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWLogIndex.setStatus("current")
_ArrisRouterFWLogTime_Type = DateAndTime
_ArrisRouterFWLogTime_Object = MibTableColumn
arrisRouterFWLogTime = _ArrisRouterFWLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 1, 1, 2),
    _ArrisRouterFWLogTime_Type()
)
arrisRouterFWLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWLogTime.setStatus("current")
_ArrisRouterFWLogInfo_Type = DisplayString
_ArrisRouterFWLogInfo_Object = MibTableColumn
arrisRouterFWLogInfo = _ArrisRouterFWLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 1, 1, 3),
    _ArrisRouterFWLogInfo_Type()
)
arrisRouterFWLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWLogInfo.setStatus("current")
_ArrisRouterParentalContLogTable_Object = MibTable
arrisRouterParentalContLogTable = _ArrisRouterParentalContLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2)
)
if mibBuilder.loadTexts:
    arrisRouterParentalContLogTable.setStatus("current")
_ArrisRouterParentalContLogEntry_Object = MibTableRow
arrisRouterParentalContLogEntry = _ArrisRouterParentalContLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2, 1)
)
arrisRouterParentalContLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterPCLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterParentalContLogEntry.setStatus("current")


class _ArrisRouterPCLogIndex_Type(Integer32):
    """Custom type arrisRouterPCLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisRouterPCLogIndex_Type.__name__ = "Integer32"
_ArrisRouterPCLogIndex_Object = MibTableColumn
arrisRouterPCLogIndex = _ArrisRouterPCLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2, 1, 1),
    _ArrisRouterPCLogIndex_Type()
)
arrisRouterPCLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterPCLogIndex.setStatus("current")
_ArrisRouterPCLogTime_Type = DateAndTime
_ArrisRouterPCLogTime_Object = MibTableColumn
arrisRouterPCLogTime = _ArrisRouterPCLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2, 1, 2),
    _ArrisRouterPCLogTime_Type()
)
arrisRouterPCLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPCLogTime.setStatus("current")
_ArrisRouterPCLogInfo_Type = DisplayString
_ArrisRouterPCLogInfo_Object = MibTableColumn
arrisRouterPCLogInfo = _ArrisRouterPCLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2, 1, 3),
    _ArrisRouterPCLogInfo_Type()
)
arrisRouterPCLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPCLogInfo.setStatus("current")


class _ArrisRouterPCLogType_Type(Integer32):
    """Custom type arrisRouterPCLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ArrisRouterPCLogType_Type.__name__ = "Integer32"
_ArrisRouterPCLogType_Object = MibTableColumn
arrisRouterPCLogType = _ArrisRouterPCLogType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 2, 1, 4),
    _ArrisRouterPCLogType_Type()
)
arrisRouterPCLogType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPCLogType.setStatus("current")
_ArrisRouterChangeLogTable_Object = MibTable
arrisRouterChangeLogTable = _ArrisRouterChangeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 3)
)
if mibBuilder.loadTexts:
    arrisRouterChangeLogTable.setStatus("current")
_ArrisRouterChangeLogEntry_Object = MibTableRow
arrisRouterChangeLogEntry = _ArrisRouterChangeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 3, 1)
)
arrisRouterChangeLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterChangeLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterChangeLogEntry.setStatus("current")


class _ArrisRouterChangeLogIndex_Type(Integer32):
    """Custom type arrisRouterChangeLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ArrisRouterChangeLogIndex_Type.__name__ = "Integer32"
_ArrisRouterChangeLogIndex_Object = MibTableColumn
arrisRouterChangeLogIndex = _ArrisRouterChangeLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 3, 1, 1),
    _ArrisRouterChangeLogIndex_Type()
)
arrisRouterChangeLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterChangeLogIndex.setStatus("current")
_ArrisRouterChangeLogTime_Type = DateAndTime
_ArrisRouterChangeLogTime_Object = MibTableColumn
arrisRouterChangeLogTime = _ArrisRouterChangeLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 3, 1, 2),
    _ArrisRouterChangeLogTime_Type()
)
arrisRouterChangeLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChangeLogTime.setStatus("current")
_ArrisRouterChangeLogInfo_Type = DisplayString
_ArrisRouterChangeLogInfo_Object = MibTableColumn
arrisRouterChangeLogInfo = _ArrisRouterChangeLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 3, 1, 3),
    _ArrisRouterChangeLogInfo_Type()
)
arrisRouterChangeLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterChangeLogInfo.setStatus("current")
_ArrisRouterDebugLogTable_Object = MibTable
arrisRouterDebugLogTable = _ArrisRouterDebugLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 4)
)
if mibBuilder.loadTexts:
    arrisRouterDebugLogTable.setStatus("current")
_ArrisRouterDebugLogEntry_Object = MibTableRow
arrisRouterDebugLogEntry = _ArrisRouterDebugLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 4, 1)
)
arrisRouterDebugLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterDebugLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterDebugLogEntry.setStatus("current")


class _ArrisRouterDebugLogIndex_Type(Integer32):
    """Custom type arrisRouterDebugLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ArrisRouterDebugLogIndex_Type.__name__ = "Integer32"
_ArrisRouterDebugLogIndex_Object = MibTableColumn
arrisRouterDebugLogIndex = _ArrisRouterDebugLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 4, 1, 1),
    _ArrisRouterDebugLogIndex_Type()
)
arrisRouterDebugLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterDebugLogIndex.setStatus("current")
_ArrisRouterDebugLogTime_Type = DateAndTime
_ArrisRouterDebugLogTime_Object = MibTableColumn
arrisRouterDebugLogTime = _ArrisRouterDebugLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 4, 1, 2),
    _ArrisRouterDebugLogTime_Type()
)
arrisRouterDebugLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDebugLogTime.setStatus("current")
_ArrisRouterDebugLogInfo_Type = DisplayString
_ArrisRouterDebugLogInfo_Object = MibTableColumn
arrisRouterDebugLogInfo = _ArrisRouterDebugLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 4, 1, 3),
    _ArrisRouterDebugLogInfo_Type()
)
arrisRouterDebugLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterDebugLogInfo.setStatus("current")
_ArrisRouterFirewallLogExtTable_Object = MibTable
arrisRouterFirewallLogExtTable = _ArrisRouterFirewallLogExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7)
)
if mibBuilder.loadTexts:
    arrisRouterFirewallLogExtTable.setStatus("current")
_ArrisRouterFirewallLogExtEntry_Object = MibTableRow
arrisRouterFirewallLogExtEntry = _ArrisRouterFirewallLogExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7, 1)
)
arrisRouterFirewallLogExtEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFWLogExtIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFirewallLogExtEntry.setStatus("current")


class _ArrisRouterFWLogExtIndex_Type(Integer32):
    """Custom type arrisRouterFWLogExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArrisRouterFWLogExtIndex_Type.__name__ = "Integer32"
_ArrisRouterFWLogExtIndex_Object = MibTableColumn
arrisRouterFWLogExtIndex = _ArrisRouterFWLogExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7, 1, 1),
    _ArrisRouterFWLogExtIndex_Type()
)
arrisRouterFWLogExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFWLogExtIndex.setStatus("current")
_ArrisRouterFWLogLatestEventTime_Type = DateAndTime
_ArrisRouterFWLogLatestEventTime_Object = MibTableColumn
arrisRouterFWLogLatestEventTime = _ArrisRouterFWLogLatestEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7, 1, 2),
    _ArrisRouterFWLogLatestEventTime_Type()
)
arrisRouterFWLogLatestEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWLogLatestEventTime.setStatus("current")
_ArrisRouterFWLogLatestEventInfo_Type = DisplayString
_ArrisRouterFWLogLatestEventInfo_Object = MibTableColumn
arrisRouterFWLogLatestEventInfo = _ArrisRouterFWLogLatestEventInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7, 1, 3),
    _ArrisRouterFWLogLatestEventInfo_Type()
)
arrisRouterFWLogLatestEventInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWLogLatestEventInfo.setStatus("current")
_ArrisRouterFWLogEventCount_Type = Integer32
_ArrisRouterFWLogEventCount_Object = MibTableColumn
arrisRouterFWLogEventCount = _ArrisRouterFWLogEventCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 1, 7, 1, 4),
    _ArrisRouterFWLogEventCount_Type()
)
arrisRouterFWLogEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFWLogEventCount.setStatus("current")
_ArrisRouterMSOLogs_ObjectIdentity = ObjectIdentity
arrisRouterMSOLogs = _ArrisRouterMSOLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2)
)
_ArrisRouterMSOChgLogTable_Object = MibTable
arrisRouterMSOChgLogTable = _ArrisRouterMSOChgLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 1)
)
if mibBuilder.loadTexts:
    arrisRouterMSOChgLogTable.setStatus("current")
_ArrisRouterMSOChgLogEntry_Object = MibTableRow
arrisRouterMSOChgLogEntry = _ArrisRouterMSOChgLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 1, 1)
)
arrisRouterMSOChgLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterMSOChgLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterMSOChgLogEntry.setStatus("current")


class _ArrisRouterMSOChgLogIndex_Type(Integer32):
    """Custom type arrisRouterMSOChgLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_ArrisRouterMSOChgLogIndex_Type.__name__ = "Integer32"
_ArrisRouterMSOChgLogIndex_Object = MibTableColumn
arrisRouterMSOChgLogIndex = _ArrisRouterMSOChgLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 1, 1, 1),
    _ArrisRouterMSOChgLogIndex_Type()
)
arrisRouterMSOChgLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterMSOChgLogIndex.setStatus("current")
_ArrisRouterMSOChgLogTime_Type = DateAndTime
_ArrisRouterMSOChgLogTime_Object = MibTableColumn
arrisRouterMSOChgLogTime = _ArrisRouterMSOChgLogTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 1, 1, 2),
    _ArrisRouterMSOChgLogTime_Type()
)
arrisRouterMSOChgLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterMSOChgLogTime.setStatus("current")
_ArrisRouterMSOChgLogInfo_Type = DisplayString
_ArrisRouterMSOChgLogInfo_Object = MibTableColumn
arrisRouterMSOChgLogInfo = _ArrisRouterMSOChgLogInfo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 1, 1, 3),
    _ArrisRouterMSOChgLogInfo_Type()
)
arrisRouterMSOChgLogInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterMSOChgLogInfo.setStatus("current")


class _ArrisRouterClearMSOLogs_Type(Integer32):
    """Custom type arrisRouterClearMSOLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("clearLogs", 1))
    )


_ArrisRouterClearMSOLogs_Type.__name__ = "Integer32"
_ArrisRouterClearMSOLogs_Object = MibScalar
arrisRouterClearMSOLogs = _ArrisRouterClearMSOLogs_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 2, 2),
    _ArrisRouterClearMSOLogs_Type()
)
arrisRouterClearMSOLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterClearMSOLogs.setStatus("current")


class _ArrisRouterClearLogs_Type(Integer32):
    """Custom type arrisRouterClearLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("clearUserLogs", 1),
          ("clearMSOLogs", 2),
          ("clearAllLogs", 3))
    )


_ArrisRouterClearLogs_Type.__name__ = "Integer32"
_ArrisRouterClearLogs_Object = MibScalar
arrisRouterClearLogs = _ArrisRouterClearLogs_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 19, 3),
    _ArrisRouterClearLogs_Type()
)
arrisRouterClearLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterClearLogs.setStatus("current")


class _ArrisRouterTACACSAddr_Type(DisplayString):
    """Custom type arrisRouterTACACSAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterTACACSAddr_Type.__name__ = "DisplayString"
_ArrisRouterTACACSAddr_Object = MibScalar
arrisRouterTACACSAddr = _ArrisRouterTACACSAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 20),
    _ArrisRouterTACACSAddr_Type()
)
arrisRouterTACACSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTACACSAddr.setStatus("current")


class _ArrisRouterTACACSPort_Type(Integer32):
    """Custom type arrisRouterTACACSPort based on Integer32"""
    defaultValue = 49


_ArrisRouterTACACSPort_Type.__name__ = "Integer32"
_ArrisRouterTACACSPort_Object = MibScalar
arrisRouterTACACSPort = _ArrisRouterTACACSPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 21),
    _ArrisRouterTACACSPort_Type()
)
arrisRouterTACACSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTACACSPort.setStatus("current")


class _ArrisRouterTACACSSecretKey_Type(DisplayString):
    """Custom type arrisRouterTACACSSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArrisRouterTACACSSecretKey_Type.__name__ = "DisplayString"
_ArrisRouterTACACSSecretKey_Object = MibScalar
arrisRouterTACACSSecretKey = _ArrisRouterTACACSSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 22),
    _ArrisRouterTACACSSecretKey_Type()
)
arrisRouterTACACSSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTACACSSecretKey.setStatus("current")


class _ArrisRouterXmlProvisioningFile_Type(DisplayString):
    """Custom type arrisRouterXmlProvisioningFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterXmlProvisioningFile_Type.__name__ = "DisplayString"
_ArrisRouterXmlProvisioningFile_Object = MibScalar
arrisRouterXmlProvisioningFile = _ArrisRouterXmlProvisioningFile_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 23),
    _ArrisRouterXmlProvisioningFile_Type()
)
arrisRouterXmlProvisioningFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterXmlProvisioningFile.setStatus("current")


class _ArrisRouterXmlProvisioningStatus_Type(Integer32):
    """Custom type arrisRouterXmlProvisioningStatus based on Integer32"""
    defaultValue = 1

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
        *(("notSpecified", 1),
          ("inProgress", 2),
          ("downloadSuccess", 3),
          ("serverError", 4),
          ("fileNotFound", 5),
          ("fileFormatError", 6),
          ("downloadFromMgt", 7))
    )


_ArrisRouterXmlProvisioningStatus_Type.__name__ = "Integer32"
_ArrisRouterXmlProvisioningStatus_Object = MibScalar
arrisRouterXmlProvisioningStatus = _ArrisRouterXmlProvisioningStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 24),
    _ArrisRouterXmlProvisioningStatus_Type()
)
arrisRouterXmlProvisioningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterXmlProvisioningStatus.setStatus("current")


class _ArrisRouterInboundTrafficLogEnable_Type(TruthValue):
    """Custom type arrisRouterInboundTrafficLogEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterInboundTrafficLogEnable_Type.__name__ = "TruthValue"
_ArrisRouterInboundTrafficLogEnable_Object = MibScalar
arrisRouterInboundTrafficLogEnable = _ArrisRouterInboundTrafficLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 34),
    _ArrisRouterInboundTrafficLogEnable_Type()
)
arrisRouterInboundTrafficLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterInboundTrafficLogEnable.setStatus("current")
_ArrisRouterInboundTrafficLogTable_Object = MibTable
arrisRouterInboundTrafficLogTable = _ArrisRouterInboundTrafficLogTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 42)
)
if mibBuilder.loadTexts:
    arrisRouterInboundTrafficLogTable.setStatus("current")
_ArrisRouterInboundTrafficLogEntry_Object = MibTableRow
arrisRouterInboundTrafficLogEntry = _ArrisRouterInboundTrafficLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 42, 1)
)
arrisRouterInboundTrafficLogEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterInboundTrafficLogIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterInboundTrafficLogEntry.setStatus("current")
_ArrisRouterInboundTrafficLogIndex_Type = Unsigned32
_ArrisRouterInboundTrafficLogIndex_Object = MibTableColumn
arrisRouterInboundTrafficLogIndex = _ArrisRouterInboundTrafficLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 42, 1, 1),
    _ArrisRouterInboundTrafficLogIndex_Type()
)
arrisRouterInboundTrafficLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterInboundTrafficLogIndex.setStatus("current")
_ArrisRouterInboundTrafficLogData_Type = OctetString
_ArrisRouterInboundTrafficLogData_Object = MibTableColumn
arrisRouterInboundTrafficLogData = _ArrisRouterInboundTrafficLogData_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 42, 1, 2),
    _ArrisRouterInboundTrafficLogData_Type()
)
arrisRouterInboundTrafficLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterInboundTrafficLogData.setStatus("current")


class _ArrisRouterWirelessBand_Type(Integer32):
    """Custom type arrisRouterWirelessBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("band24GHz", 0),
          ("band5GHz", 1),
          ("band24GHzand5GHz", 2))
    )


_ArrisRouterWirelessBand_Type.__name__ = "Integer32"
_ArrisRouterWirelessBand_Object = MibScalar
arrisRouterWirelessBand = _ArrisRouterWirelessBand_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 55),
    _ArrisRouterWirelessBand_Type()
)
arrisRouterWirelessBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterWirelessBand.setStatus("current")


class _ArrisRouterSaveCurrentConfigFile_Type(Integer32):
    """Custom type arrisRouterSaveCurrentConfigFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_ArrisRouterSaveCurrentConfigFile_Type.__name__ = "Integer32"
_ArrisRouterSaveCurrentConfigFile_Object = MibScalar
arrisRouterSaveCurrentConfigFile = _ArrisRouterSaveCurrentConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 57),
    _ArrisRouterSaveCurrentConfigFile_Type()
)
arrisRouterSaveCurrentConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterSaveCurrentConfigFile.setStatus("current")


class _ArrisRouterRestoreCurrentConfigFile_Type(Integer32):
    """Custom type arrisRouterRestoreCurrentConfigFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_ArrisRouterRestoreCurrentConfigFile_Type.__name__ = "Integer32"
_ArrisRouterRestoreCurrentConfigFile_Object = MibScalar
arrisRouterRestoreCurrentConfigFile = _ArrisRouterRestoreCurrentConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 58),
    _ArrisRouterRestoreCurrentConfigFile_Type()
)
arrisRouterRestoreCurrentConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterRestoreCurrentConfigFile.setStatus("current")


class _ArrisRouterLocalPosixTimeZone_Type(DisplayString):
    """Custom type arrisRouterLocalPosixTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisRouterLocalPosixTimeZone_Type.__name__ = "DisplayString"
_ArrisRouterLocalPosixTimeZone_Object = MibScalar
arrisRouterLocalPosixTimeZone = _ArrisRouterLocalPosixTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 59),
    _ArrisRouterLocalPosixTimeZone_Type()
)
arrisRouterLocalPosixTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterLocalPosixTimeZone.setStatus("current")
_ArrisRouterFirstInstallWizardCompletionStatus_Type = TruthValue
_ArrisRouterFirstInstallWizardCompletionStatus_Object = MibScalar
arrisRouterFirstInstallWizardCompletionStatus = _ArrisRouterFirstInstallWizardCompletionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 62),
    _ArrisRouterFirstInstallWizardCompletionStatus_Type()
)
arrisRouterFirstInstallWizardCompletionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFirstInstallWizardCompletionStatus.setStatus("current")
_ArrisRouterTroubleshooterEnable_Type = TruthValue
_ArrisRouterTroubleshooterEnable_Object = MibScalar
arrisRouterTroubleshooterEnable = _ArrisRouterTroubleshooterEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 63),
    _ArrisRouterTroubleshooterEnable_Type()
)
arrisRouterTroubleshooterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTroubleshooterEnable.setStatus("current")
_ArrisRouterCSRActiveTimeout_Type = Unsigned32
_ArrisRouterCSRActiveTimeout_Object = MibScalar
arrisRouterCSRActiveTimeout = _ArrisRouterCSRActiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 5, 65),
    _ArrisRouterCSRActiveTimeout_Type()
)
arrisRouterCSRActiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterCSRActiveTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterCSRActiveTimeout.setUnits("seconds")
_ArrisRouterHostAccess_ObjectIdentity = ObjectIdentity
arrisRouterHostAccess = _ArrisRouterHostAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6)
)
_ArrisRouterWebAccessTable_Object = MibTable
arrisRouterWebAccessTable = _ArrisRouterWebAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    arrisRouterWebAccessTable.setStatus("current")
_ArrisRouterWebAccessEntry_Object = MibTableRow
arrisRouterWebAccessEntry = _ArrisRouterWebAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7, 1)
)
arrisRouterWebAccessEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterWebAccessIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterWebAccessEntry.setStatus("current")


class _ArrisRouterWebAccessIndex_Type(Integer32):
    """Custom type arrisRouterWebAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ArrisRouterWebAccessIndex_Type.__name__ = "Integer32"
_ArrisRouterWebAccessIndex_Object = MibTableColumn
arrisRouterWebAccessIndex = _ArrisRouterWebAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7, 1, 1),
    _ArrisRouterWebAccessIndex_Type()
)
arrisRouterWebAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterWebAccessIndex.setStatus("current")
_ArrisRouterWebAccessPage_Type = DisplayString
_ArrisRouterWebAccessPage_Object = MibTableColumn
arrisRouterWebAccessPage = _ArrisRouterWebAccessPage_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7, 1, 2),
    _ArrisRouterWebAccessPage_Type()
)
arrisRouterWebAccessPage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWebAccessPage.setStatus("current")


class _ArrisRouterWebAccessLevel_Type(Integer32):
    """Custom type arrisRouterWebAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccessAll", 0),
          ("accessTech", 1),
          ("accessUser", 2),
          ("accessAll", 3))
    )


_ArrisRouterWebAccessLevel_Type.__name__ = "Integer32"
_ArrisRouterWebAccessLevel_Object = MibTableColumn
arrisRouterWebAccessLevel = _ArrisRouterWebAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7, 1, 3),
    _ArrisRouterWebAccessLevel_Type()
)
arrisRouterWebAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWebAccessLevel.setStatus("current")
_ArrisRouterWebAccessRowStatus_Type = RowStatus
_ArrisRouterWebAccessRowStatus_Object = MibTableColumn
arrisRouterWebAccessRowStatus = _ArrisRouterWebAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 7, 1, 4),
    _ArrisRouterWebAccessRowStatus_Type()
)
arrisRouterWebAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterWebAccessRowStatus.setStatus("current")
_ArrisRouterWebAccessWANACL_Type = DisplayString
_ArrisRouterWebAccessWANACL_Object = MibScalar
arrisRouterWebAccessWANACL = _ArrisRouterWebAccessWANACL_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 6, 8),
    _ArrisRouterWebAccessWANACL_Type()
)
arrisRouterWebAccessWANACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterWebAccessWANACL.setStatus("current")
_ArrisRouterPingMgmt_ObjectIdentity = ObjectIdentity
arrisRouterPingMgmt = _ArrisRouterPingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7)
)


class _ArrisRouterPingTargetAddrType_Type(InetAddressType):
    """Custom type arrisRouterPingTargetAddrType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterPingTargetAddrType_Type.__name__ = "InetAddressType"
_ArrisRouterPingTargetAddrType_Object = MibScalar
arrisRouterPingTargetAddrType = _ArrisRouterPingTargetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 1),
    _ArrisRouterPingTargetAddrType_Type()
)
arrisRouterPingTargetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingTargetAddrType.setStatus("current")
_ArrisRouterPingTargetAddress_Type = InetAddress
_ArrisRouterPingTargetAddress_Object = MibScalar
arrisRouterPingTargetAddress = _ArrisRouterPingTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 2),
    _ArrisRouterPingTargetAddress_Type()
)
arrisRouterPingTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingTargetAddress.setStatus("current")


class _ArrisRouterPingNumPkts_Type(Unsigned32):
    """Custom type arrisRouterPingNumPkts based on Unsigned32"""
    defaultValue = 3


_ArrisRouterPingNumPkts_Type.__name__ = "Unsigned32"
_ArrisRouterPingNumPkts_Object = MibScalar
arrisRouterPingNumPkts = _ArrisRouterPingNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 3),
    _ArrisRouterPingNumPkts_Type()
)
arrisRouterPingNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingNumPkts.setStatus("current")


class _ArrisRouterPingPktSize_Type(Unsigned32):
    """Custom type arrisRouterPingPktSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_ArrisRouterPingPktSize_Type.__name__ = "Unsigned32"
_ArrisRouterPingPktSize_Object = MibScalar
arrisRouterPingPktSize = _ArrisRouterPingPktSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 4),
    _ArrisRouterPingPktSize_Type()
)
arrisRouterPingPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingPktSize.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingPktSize.setUnits("bytes")


class _ArrisRouterPingInterval_Type(Unsigned32):
    """Custom type arrisRouterPingInterval based on Unsigned32"""
    defaultValue = 0


_ArrisRouterPingInterval_Type.__name__ = "Unsigned32"
_ArrisRouterPingInterval_Object = MibScalar
arrisRouterPingInterval = _ArrisRouterPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 5),
    _ArrisRouterPingInterval_Type()
)
arrisRouterPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingInterval.setUnits("milliseconds")


class _ArrisRouterPingTimeout_Type(Integer32):
    """Custom type arrisRouterPingTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_ArrisRouterPingTimeout_Type.__name__ = "Integer32"
_ArrisRouterPingTimeout_Object = MibScalar
arrisRouterPingTimeout = _ArrisRouterPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 6),
    _ArrisRouterPingTimeout_Type()
)
arrisRouterPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingTimeout.setUnits("milliseconds")


class _ArrisRouterPingVerifyReply_Type(TruthValue):
    """Custom type arrisRouterPingVerifyReply based on TruthValue"""
    defaultValue = 1


_ArrisRouterPingVerifyReply_Type.__name__ = "TruthValue"
_ArrisRouterPingVerifyReply_Object = MibScalar
arrisRouterPingVerifyReply = _ArrisRouterPingVerifyReply_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 7),
    _ArrisRouterPingVerifyReply_Type()
)
arrisRouterPingVerifyReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingVerifyReply.setStatus("current")


class _ArrisRouterPingIpStackNumber_Type(Integer32):
    """Custom type arrisRouterPingIpStackNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ArrisRouterPingIpStackNumber_Type.__name__ = "Integer32"
_ArrisRouterPingIpStackNumber_Object = MibScalar
arrisRouterPingIpStackNumber = _ArrisRouterPingIpStackNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 8),
    _ArrisRouterPingIpStackNumber_Type()
)
arrisRouterPingIpStackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingIpStackNumber.setStatus("current")


class _ArrisRouterPingStartStop_Type(TruthValue):
    """Custom type arrisRouterPingStartStop based on TruthValue"""
    defaultValue = 1


_ArrisRouterPingStartStop_Type.__name__ = "TruthValue"
_ArrisRouterPingStartStop_Object = MibScalar
arrisRouterPingStartStop = _ArrisRouterPingStartStop_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 9),
    _ArrisRouterPingStartStop_Type()
)
arrisRouterPingStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingStartStop.setStatus("current")
_ArrisRouterPingPktsSent_Type = Counter32
_ArrisRouterPingPktsSent_Object = MibScalar
arrisRouterPingPktsSent = _ArrisRouterPingPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 10),
    _ArrisRouterPingPktsSent_Type()
)
arrisRouterPingPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingPktsSent.setStatus("current")
_ArrisRouterPingRepliesReceived_Type = Counter32
_ArrisRouterPingRepliesReceived_Object = MibScalar
arrisRouterPingRepliesReceived = _ArrisRouterPingRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 11),
    _ArrisRouterPingRepliesReceived_Type()
)
arrisRouterPingRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingRepliesReceived.setStatus("current")
_ArrisRouterPingRepliesVerified_Type = Counter32
_ArrisRouterPingRepliesVerified_Object = MibScalar
arrisRouterPingRepliesVerified = _ArrisRouterPingRepliesVerified_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 12),
    _ArrisRouterPingRepliesVerified_Type()
)
arrisRouterPingRepliesVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingRepliesVerified.setStatus("current")
_ArrisRouterPingOctetsSent_Type = Counter32
_ArrisRouterPingOctetsSent_Object = MibScalar
arrisRouterPingOctetsSent = _ArrisRouterPingOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 13),
    _ArrisRouterPingOctetsSent_Type()
)
arrisRouterPingOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingOctetsSent.setStatus("current")
_ArrisRouterPingOctetsReceived_Type = Counter32
_ArrisRouterPingOctetsReceived_Object = MibScalar
arrisRouterPingOctetsReceived = _ArrisRouterPingOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 14),
    _ArrisRouterPingOctetsReceived_Type()
)
arrisRouterPingOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingOctetsReceived.setStatus("current")
_ArrisRouterPingIcmpErrors_Type = Counter32
_ArrisRouterPingIcmpErrors_Object = MibScalar
arrisRouterPingIcmpErrors = _ArrisRouterPingIcmpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 15),
    _ArrisRouterPingIcmpErrors_Type()
)
arrisRouterPingIcmpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingIcmpErrors.setStatus("current")
_ArrisRouterPingLastIcmpError_Type = Unsigned32
_ArrisRouterPingLastIcmpError_Object = MibScalar
arrisRouterPingLastIcmpError = _ArrisRouterPingLastIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 16),
    _ArrisRouterPingLastIcmpError_Type()
)
arrisRouterPingLastIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingLastIcmpError.setStatus("current")
_ArrisRouterPingAverageRtt_Type = Unsigned32
_ArrisRouterPingAverageRtt_Object = MibScalar
arrisRouterPingAverageRtt = _ArrisRouterPingAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 17),
    _ArrisRouterPingAverageRtt_Type()
)
arrisRouterPingAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingAverageRtt.setUnits("milliseconds")
_ArrisRouterPingMinRtt_Type = Unsigned32
_ArrisRouterPingMinRtt_Object = MibScalar
arrisRouterPingMinRtt = _ArrisRouterPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 18),
    _ArrisRouterPingMinRtt_Type()
)
arrisRouterPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingMinRtt.setUnits("milliseconds")
_ArrisRouterPingMaxRtt_Type = Unsigned32
_ArrisRouterPingMaxRtt_Object = MibScalar
arrisRouterPingMaxRtt = _ArrisRouterPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 19),
    _ArrisRouterPingMaxRtt_Type()
)
arrisRouterPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterPingMaxRtt.setUnits("milliseconds")


class _ArrisRouterPingTargetDNSQueryIPAddrType_Type(InetAddressType):
    """Custom type arrisRouterPingTargetDNSQueryIPAddrType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterPingTargetDNSQueryIPAddrType_Type.__name__ = "InetAddressType"
_ArrisRouterPingTargetDNSQueryIPAddrType_Object = MibScalar
arrisRouterPingTargetDNSQueryIPAddrType = _ArrisRouterPingTargetDNSQueryIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 20),
    _ArrisRouterPingTargetDNSQueryIPAddrType_Type()
)
arrisRouterPingTargetDNSQueryIPAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterPingTargetDNSQueryIPAddrType.setStatus("current")


class _ArrisRouterPingLog_Type(DisplayString):
    """Custom type arrisRouterPingLog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ArrisRouterPingLog_Type.__name__ = "DisplayString"
_ArrisRouterPingLog_Object = MibScalar
arrisRouterPingLog = _ArrisRouterPingLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 7, 21),
    _ArrisRouterPingLog_Type()
)
arrisRouterPingLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterPingLog.setStatus("current")
_ArrisRouterTraceRtMgmt_ObjectIdentity = ObjectIdentity
arrisRouterTraceRtMgmt = _ArrisRouterTraceRtMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8)
)


class _ArrisRouterTraceRtTargAddrType_Type(InetAddressType):
    """Custom type arrisRouterTraceRtTargAddrType based on InetAddressType"""
    defaultValue = 1


_ArrisRouterTraceRtTargAddrType_Type.__name__ = "InetAddressType"
_ArrisRouterTraceRtTargAddrType_Object = MibScalar
arrisRouterTraceRtTargAddrType = _ArrisRouterTraceRtTargAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 1),
    _ArrisRouterTraceRtTargAddrType_Type()
)
arrisRouterTraceRtTargAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtTargAddrType.setStatus("current")
_ArrisRouterTraceRtTargetAddr_Type = InetAddress
_ArrisRouterTraceRtTargetAddr_Object = MibScalar
arrisRouterTraceRtTargetAddr = _ArrisRouterTraceRtTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 2),
    _ArrisRouterTraceRtTargetAddr_Type()
)
arrisRouterTraceRtTargetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtTargetAddr.setStatus("current")


class _ArrisRouterTraceRtMaxHops_Type(Integer32):
    """Custom type arrisRouterTraceRtMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterTraceRtMaxHops_Type.__name__ = "Integer32"
_ArrisRouterTraceRtMaxHops_Object = MibScalar
arrisRouterTraceRtMaxHops = _ArrisRouterTraceRtMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 3),
    _ArrisRouterTraceRtMaxHops_Type()
)
arrisRouterTraceRtMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtMaxHops.setStatus("current")


class _ArrisRouterTraceRtDataSize_Type(Integer32):
    """Custom type arrisRouterTraceRtDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterTraceRtDataSize_Type.__name__ = "Integer32"
_ArrisRouterTraceRtDataSize_Object = MibScalar
arrisRouterTraceRtDataSize = _ArrisRouterTraceRtDataSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 4),
    _ArrisRouterTraceRtDataSize_Type()
)
arrisRouterTraceRtDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtDataSize.setStatus("current")


class _ArrisRouterTraceRtResolveHosts_Type(Integer32):
    """Custom type arrisRouterTraceRtResolveHosts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noResolve", 0),
          ("resolve", 1))
    )


_ArrisRouterTraceRtResolveHosts_Type.__name__ = "Integer32"
_ArrisRouterTraceRtResolveHosts_Object = MibScalar
arrisRouterTraceRtResolveHosts = _ArrisRouterTraceRtResolveHosts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 5),
    _ArrisRouterTraceRtResolveHosts_Type()
)
arrisRouterTraceRtResolveHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtResolveHosts.setStatus("current")


class _ArrisRouterTraceRtBasePort_Type(Integer32):
    """Custom type arrisRouterTraceRtBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ArrisRouterTraceRtBasePort_Type.__name__ = "Integer32"
_ArrisRouterTraceRtBasePort_Object = MibScalar
arrisRouterTraceRtBasePort = _ArrisRouterTraceRtBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 6),
    _ArrisRouterTraceRtBasePort_Type()
)
arrisRouterTraceRtBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtBasePort.setStatus("current")


class _ArrisRouterTraceRtStart_Type(Integer32):
    """Custom type arrisRouterTraceRtStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("traceRouteNotRunning", 0),
          ("traceRouteRunning", 1),
          ("startTrace", 10),
          ("stopTrace", 11))
    )


_ArrisRouterTraceRtStart_Type.__name__ = "Integer32"
_ArrisRouterTraceRtStart_Object = MibScalar
arrisRouterTraceRtStart = _ArrisRouterTraceRtStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 7),
    _ArrisRouterTraceRtStart_Type()
)
arrisRouterTraceRtStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtStart.setStatus("current")


class _ArrisRouterTraceRtLog_Type(DisplayString):
    """Custom type arrisRouterTraceRtLog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ArrisRouterTraceRtLog_Type.__name__ = "DisplayString"
_ArrisRouterTraceRtLog_Object = MibScalar
arrisRouterTraceRtLog = _ArrisRouterTraceRtLog_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 8),
    _ArrisRouterTraceRtLog_Type()
)
arrisRouterTraceRtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterTraceRtLog.setStatus("current")


class _ArrisRouterTraceRtTimeout_Type(Unsigned32):
    """Custom type arrisRouterTraceRtTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ArrisRouterTraceRtTimeout_Type.__name__ = "Unsigned32"
_ArrisRouterTraceRtTimeout_Object = MibScalar
arrisRouterTraceRtTimeout = _ArrisRouterTraceRtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 9),
    _ArrisRouterTraceRtTimeout_Type()
)
arrisRouterTraceRtTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisRouterTraceRtTimeout.setUnits("seconds")


class _ArrisRouterTraceRtDiffServ_Type(Unsigned32):
    """Custom type arrisRouterTraceRtDiffServ based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterTraceRtDiffServ_Type.__name__ = "Unsigned32"
_ArrisRouterTraceRtDiffServ_Object = MibScalar
arrisRouterTraceRtDiffServ = _ArrisRouterTraceRtDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 8, 10),
    _ArrisRouterTraceRtDiffServ_Type()
)
arrisRouterTraceRtDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterTraceRtDiffServ.setStatus("current")


class _ArrisRouterApplyAllSettings_Type(Integer32):
    """Custom type arrisRouterApplyAllSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("applySettings", 1))
    )


_ArrisRouterApplyAllSettings_Type.__name__ = "Integer32"
_ArrisRouterApplyAllSettings_Object = MibScalar
arrisRouterApplyAllSettings = _ArrisRouterApplyAllSettings_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 9),
    _ArrisRouterApplyAllSettings_Type()
)
arrisRouterApplyAllSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterApplyAllSettings.setStatus("current")
_ArrisRouterICtrl_ObjectIdentity = ObjectIdentity
arrisRouterICtrl = _ArrisRouterICtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10)
)
_ArrisRouterICtrlPortMapCount_Type = Integer32
_ArrisRouterICtrlPortMapCount_Object = MibScalar
arrisRouterICtrlPortMapCount = _ArrisRouterICtrlPortMapCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 1),
    _ArrisRouterICtrlPortMapCount_Type()
)
arrisRouterICtrlPortMapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterICtrlPortMapCount.setStatus("current")
_ArrisRouterICtrlPortMapTable_Object = MibTable
arrisRouterICtrlPortMapTable = _ArrisRouterICtrlPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    arrisRouterICtrlPortMapTable.setStatus("current")
_ArrisRouterICtrlPortMapEntry_Object = MibTableRow
arrisRouterICtrlPortMapEntry = _ArrisRouterICtrlPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1)
)
arrisRouterICtrlPortMapEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterICtrlPortMapIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterICtrlPortMapEntry.setStatus("current")


class _ArrisRouterICtrlPortMapIndex_Type(Integer32):
    """Custom type arrisRouterICtrlPortMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArrisRouterICtrlPortMapIndex_Type.__name__ = "Integer32"
_ArrisRouterICtrlPortMapIndex_Object = MibTableColumn
arrisRouterICtrlPortMapIndex = _ArrisRouterICtrlPortMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 1),
    _ArrisRouterICtrlPortMapIndex_Type()
)
arrisRouterICtrlPortMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterICtrlPortMapIndex.setStatus("current")
_ArrisRouterPortMapDescription_Type = DisplayString
_ArrisRouterPortMapDescription_Object = MibTableColumn
arrisRouterPortMapDescription = _ArrisRouterPortMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 2),
    _ArrisRouterPortMapDescription_Type()
)
arrisRouterPortMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapDescription.setStatus("current")
_ArrisRouterPortMapInternalClientAddrType_Type = InetAddressType
_ArrisRouterPortMapInternalClientAddrType_Object = MibTableColumn
arrisRouterPortMapInternalClientAddrType = _ArrisRouterPortMapInternalClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 3),
    _ArrisRouterPortMapInternalClientAddrType_Type()
)
arrisRouterPortMapInternalClientAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapInternalClientAddrType.setStatus("current")
_ArrisRouterPortMapInternalClientAddr_Type = InetAddress
_ArrisRouterPortMapInternalClientAddr_Object = MibTableColumn
arrisRouterPortMapInternalClientAddr = _ArrisRouterPortMapInternalClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 4),
    _ArrisRouterPortMapInternalClientAddr_Type()
)
arrisRouterPortMapInternalClientAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapInternalClientAddr.setStatus("current")


class _ArrisRouterPortMapProtocol_Type(Integer32):
    """Custom type arrisRouterPortMapProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_ArrisRouterPortMapProtocol_Type.__name__ = "Integer32"
_ArrisRouterPortMapProtocol_Object = MibTableColumn
arrisRouterPortMapProtocol = _ArrisRouterPortMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 5),
    _ArrisRouterPortMapProtocol_Type()
)
arrisRouterPortMapProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapProtocol.setStatus("current")
_ArrisRouterPortMapExternalPort_Type = Unsigned32
_ArrisRouterPortMapExternalPort_Object = MibTableColumn
arrisRouterPortMapExternalPort = _ArrisRouterPortMapExternalPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 6),
    _ArrisRouterPortMapExternalPort_Type()
)
arrisRouterPortMapExternalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapExternalPort.setStatus("current")
_ArrisRouterPortMapInternalPort_Type = Unsigned32
_ArrisRouterPortMapInternalPort_Object = MibTableColumn
arrisRouterPortMapInternalPort = _ArrisRouterPortMapInternalPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 7),
    _ArrisRouterPortMapInternalPort_Type()
)
arrisRouterPortMapInternalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapInternalPort.setStatus("current")
_ArrisRouterPortMapRowStatus_Type = RowStatus
_ArrisRouterPortMapRowStatus_Object = MibTableColumn
arrisRouterPortMapRowStatus = _ArrisRouterPortMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 8),
    _ArrisRouterPortMapRowStatus_Type()
)
arrisRouterPortMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapRowStatus.setStatus("current")
_ArrisRouterPortMapInternalStartPort_Type = Unsigned32
_ArrisRouterPortMapInternalStartPort_Object = MibTableColumn
arrisRouterPortMapInternalStartPort = _ArrisRouterPortMapInternalStartPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 9),
    _ArrisRouterPortMapInternalStartPort_Type()
)
arrisRouterPortMapInternalStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapInternalStartPort.setStatus("current")
_ArrisRouterPortMapInternalEndPort_Type = Unsigned32
_ArrisRouterPortMapInternalEndPort_Object = MibTableColumn
arrisRouterPortMapInternalEndPort = _ArrisRouterPortMapInternalEndPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 10),
    _ArrisRouterPortMapInternalEndPort_Type()
)
arrisRouterPortMapInternalEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapInternalEndPort.setStatus("current")
_ArrisRouterPortMapExternalStartPort_Type = Unsigned32
_ArrisRouterPortMapExternalStartPort_Object = MibTableColumn
arrisRouterPortMapExternalStartPort = _ArrisRouterPortMapExternalStartPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 11),
    _ArrisRouterPortMapExternalStartPort_Type()
)
arrisRouterPortMapExternalStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapExternalStartPort.setStatus("current")
_ArrisRouterPortMapExternalEndPort_Type = Unsigned32
_ArrisRouterPortMapExternalEndPort_Object = MibTableColumn
arrisRouterPortMapExternalEndPort = _ArrisRouterPortMapExternalEndPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 2, 1, 12),
    _ArrisRouterPortMapExternalEndPort_Type()
)
arrisRouterPortMapExternalEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisRouterPortMapExternalEndPort.setStatus("current")
_ArrisRouterICtrlGetDeviceSettings_ObjectIdentity = ObjectIdentity
arrisRouterICtrlGetDeviceSettings = _ArrisRouterICtrlGetDeviceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 3)
)
_ArrisRouterICtrlDeviceSettingsFWversion_Type = DisplayString
_ArrisRouterICtrlDeviceSettingsFWversion_Object = MibScalar
arrisRouterICtrlDeviceSettingsFWversion = _ArrisRouterICtrlDeviceSettingsFWversion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 3, 1),
    _ArrisRouterICtrlDeviceSettingsFWversion_Type()
)
arrisRouterICtrlDeviceSettingsFWversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterICtrlDeviceSettingsFWversion.setStatus("current")
_ArrisRouterICtrlIsDeviceReady_ObjectIdentity = ObjectIdentity
arrisRouterICtrlIsDeviceReady = _ArrisRouterICtrlIsDeviceReady_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 4)
)


class _ArrisRouterICtrlDeviceStatus_Type(Integer32):
    """Custom type arrisRouterICtrlDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_ArrisRouterICtrlDeviceStatus_Type.__name__ = "Integer32"
_ArrisRouterICtrlDeviceStatus_Object = MibScalar
arrisRouterICtrlDeviceStatus = _ArrisRouterICtrlDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 4, 1),
    _ArrisRouterICtrlDeviceStatus_Type()
)
arrisRouterICtrlDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterICtrlDeviceStatus.setStatus("current")
_ArrisRouterICtrlReboot_ObjectIdentity = ObjectIdentity
arrisRouterICtrlReboot = _ArrisRouterICtrlReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 5)
)


class _ArrisRouterICtrlInitiateReboot_Type(Integer32):
    """Custom type arrisRouterICtrlInitiateReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_ArrisRouterICtrlInitiateReboot_Type.__name__ = "Integer32"
_ArrisRouterICtrlInitiateReboot_Object = MibScalar
arrisRouterICtrlInitiateReboot = _ArrisRouterICtrlInitiateReboot_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 5, 1),
    _ArrisRouterICtrlInitiateReboot_Type()
)
arrisRouterICtrlInitiateReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlInitiateReboot.setStatus("current")
_ArrisRouterICtrlSetDeviceSettings_ObjectIdentity = ObjectIdentity
arrisRouterICtrlSetDeviceSettings = _ArrisRouterICtrlSetDeviceSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 6)
)
_ArrisRouterICtrlSetDeviceName_Type = DisplayString
_ArrisRouterICtrlSetDeviceName_Object = MibScalar
arrisRouterICtrlSetDeviceName = _ArrisRouterICtrlSetDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 6, 1),
    _ArrisRouterICtrlSetDeviceName_Type()
)
arrisRouterICtrlSetDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlSetDeviceName.setStatus("current")
_ArrisRouterICtrlSetAdminPassword_Type = DisplayString
_ArrisRouterICtrlSetAdminPassword_Object = MibScalar
arrisRouterICtrlSetAdminPassword = _ArrisRouterICtrlSetAdminPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 6, 2),
    _ArrisRouterICtrlSetAdminPassword_Type()
)
arrisRouterICtrlSetAdminPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlSetAdminPassword.setStatus("current")
_ArrisRouterICtrlRouterSettings_ObjectIdentity = ObjectIdentity
arrisRouterICtrlRouterSettings = _ArrisRouterICtrlRouterSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 7)
)
_ArrisRouterICtrlRouterManageRemote_Type = TruthValue
_ArrisRouterICtrlRouterManageRemote_Object = MibScalar
arrisRouterICtrlRouterManageRemote = _ArrisRouterICtrlRouterManageRemote_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 7, 1),
    _ArrisRouterICtrlRouterManageRemote_Type()
)
arrisRouterICtrlRouterManageRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlRouterManageRemote.setStatus("current")
_ArrisRouterICtrlRouterRemotePort_Type = Unsigned32
_ArrisRouterICtrlRouterRemotePort_Object = MibScalar
arrisRouterICtrlRouterRemotePort = _ArrisRouterICtrlRouterRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 7, 2),
    _ArrisRouterICtrlRouterRemotePort_Type()
)
arrisRouterICtrlRouterRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlRouterRemotePort.setStatus("current")
_ArrisRouterICtrlRouterRemoteSSL_Type = TruthValue
_ArrisRouterICtrlRouterRemoteSSL_Object = MibScalar
arrisRouterICtrlRouterRemoteSSL = _ArrisRouterICtrlRouterRemoteSSL_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 7, 3),
    _ArrisRouterICtrlRouterRemoteSSL_Type()
)
arrisRouterICtrlRouterRemoteSSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlRouterRemoteSSL.setStatus("current")
_ArrisRouterICtrlWLanRadioSettings_ObjectIdentity = ObjectIdentity
arrisRouterICtrlWLanRadioSettings = _ArrisRouterICtrlWLanRadioSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 8)
)
_ArrisRouterICtrlWLanRadioMacAddress_Type = MacAddress
_ArrisRouterICtrlWLanRadioMacAddress_Object = MibScalar
arrisRouterICtrlWLanRadioMacAddress = _ArrisRouterICtrlWLanRadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 8, 1),
    _ArrisRouterICtrlWLanRadioMacAddress_Type()
)
arrisRouterICtrlWLanRadioMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlWLanRadioMacAddress.setStatus("current")
_ArrisRouterICtrlWLanRadioChannelWidth_Type = Unsigned32
_ArrisRouterICtrlWLanRadioChannelWidth_Object = MibScalar
arrisRouterICtrlWLanRadioChannelWidth = _ArrisRouterICtrlWLanRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 8, 2),
    _ArrisRouterICtrlWLanRadioChannelWidth_Type()
)
arrisRouterICtrlWLanRadioChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlWLanRadioChannelWidth.setStatus("current")
_ArrisRouterICtrlSetBridgeConnect_ObjectIdentity = ObjectIdentity
arrisRouterICtrlSetBridgeConnect = _ArrisRouterICtrlSetBridgeConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 9)
)
_ArrisRouterICtrlSetBridgeEthernetPort_Type = Unsigned32
_ArrisRouterICtrlSetBridgeEthernetPort_Object = MibScalar
arrisRouterICtrlSetBridgeEthernetPort = _ArrisRouterICtrlSetBridgeEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 9, 1),
    _ArrisRouterICtrlSetBridgeEthernetPort_Type()
)
arrisRouterICtrlSetBridgeEthernetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlSetBridgeEthernetPort.setStatus("current")
_ArrisRouterICtrlSetBridgeMinutes_Type = Unsigned32
_ArrisRouterICtrlSetBridgeMinutes_Object = MibScalar
arrisRouterICtrlSetBridgeMinutes = _ArrisRouterICtrlSetBridgeMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 9, 2),
    _ArrisRouterICtrlSetBridgeMinutes_Type()
)
arrisRouterICtrlSetBridgeMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlSetBridgeMinutes.setStatus("current")


class _ArrisRouterICtrlSetBridgePermanentPort4Enable_Type(TruthValue):
    """Custom type arrisRouterICtrlSetBridgePermanentPort4Enable based on TruthValue"""
    defaultValue = 2


_ArrisRouterICtrlSetBridgePermanentPort4Enable_Type.__name__ = "TruthValue"
_ArrisRouterICtrlSetBridgePermanentPort4Enable_Object = MibScalar
arrisRouterICtrlSetBridgePermanentPort4Enable = _ArrisRouterICtrlSetBridgePermanentPort4Enable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 9, 3),
    _ArrisRouterICtrlSetBridgePermanentPort4Enable_Type()
)
arrisRouterICtrlSetBridgePermanentPort4Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlSetBridgePermanentPort4Enable.setStatus("current")
_ArrisRouterICtrlGetWanSettings_ObjectIdentity = ObjectIdentity
arrisRouterICtrlGetWanSettings = _ArrisRouterICtrlGetWanSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10)
)


class _ArrisRouterICtrlGetWanType_Type(DisplayString):
    """Custom type arrisRouterICtrlGetWanType based on DisplayString"""
    defaultValue = OctetString("DHCP")


_ArrisRouterICtrlGetWanType_Type.__name__ = "DisplayString"
_ArrisRouterICtrlGetWanType_Object = MibScalar
arrisRouterICtrlGetWanType = _ArrisRouterICtrlGetWanType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 2),
    _ArrisRouterICtrlGetWanType_Type()
)
arrisRouterICtrlGetWanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanType.setStatus("current")
_ArrisRouterICtrlGetWanMTU_Type = Unsigned32
_ArrisRouterICtrlGetWanMTU_Object = MibScalar
arrisRouterICtrlGetWanMTU = _ArrisRouterICtrlGetWanMTU_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 3),
    _ArrisRouterICtrlGetWanMTU_Type()
)
arrisRouterICtrlGetWanMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanMTU.setStatus("current")
_ArrisRouterICtrlGetWanPrefixLen_Type = InetAddressPrefixLength
_ArrisRouterICtrlGetWanPrefixLen_Object = MibScalar
arrisRouterICtrlGetWanPrefixLen = _ArrisRouterICtrlGetWanPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 4),
    _ArrisRouterICtrlGetWanPrefixLen_Type()
)
arrisRouterICtrlGetWanPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanPrefixLen.setStatus("current")
_ArrisRouterICtrlGetWanGatewayAddrType_Type = InetAddressType
_ArrisRouterICtrlGetWanGatewayAddrType_Object = MibScalar
arrisRouterICtrlGetWanGatewayAddrType = _ArrisRouterICtrlGetWanGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 5),
    _ArrisRouterICtrlGetWanGatewayAddrType_Type()
)
arrisRouterICtrlGetWanGatewayAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanGatewayAddrType.setStatus("current")
_ArrisRouterICtrlGetWanGatewayAddr_Type = InetAddress
_ArrisRouterICtrlGetWanGatewayAddr_Object = MibScalar
arrisRouterICtrlGetWanGatewayAddr = _ArrisRouterICtrlGetWanGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 6),
    _ArrisRouterICtrlGetWanGatewayAddr_Type()
)
arrisRouterICtrlGetWanGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanGatewayAddr.setStatus("current")
_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Type = InetAddressType
_ArrisRouterICtrlGetWanDNSPrimaryAddrType_Object = MibScalar
arrisRouterICtrlGetWanDNSPrimaryAddrType = _ArrisRouterICtrlGetWanDNSPrimaryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 7),
    _ArrisRouterICtrlGetWanDNSPrimaryAddrType_Type()
)
arrisRouterICtrlGetWanDNSPrimaryAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanDNSPrimaryAddrType.setStatus("current")
_ArrisRouterICtrlGetWanDNSPrimaryAddr_Type = InetAddress
_ArrisRouterICtrlGetWanDNSPrimaryAddr_Object = MibScalar
arrisRouterICtrlGetWanDNSPrimaryAddr = _ArrisRouterICtrlGetWanDNSPrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 8),
    _ArrisRouterICtrlGetWanDNSPrimaryAddr_Type()
)
arrisRouterICtrlGetWanDNSPrimaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanDNSPrimaryAddr.setStatus("current")
_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Type = InetAddressType
_ArrisRouterICtrlGetWanDNSSecondaryAddrType_Object = MibScalar
arrisRouterICtrlGetWanDNSSecondaryAddrType = _ArrisRouterICtrlGetWanDNSSecondaryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 9),
    _ArrisRouterICtrlGetWanDNSSecondaryAddrType_Type()
)
arrisRouterICtrlGetWanDNSSecondaryAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanDNSSecondaryAddrType.setStatus("current")
_ArrisRouterICtrlGetWanDNSSecondaryAddr_Type = InetAddress
_ArrisRouterICtrlGetWanDNSSecondaryAddr_Object = MibScalar
arrisRouterICtrlGetWanDNSSecondaryAddr = _ArrisRouterICtrlGetWanDNSSecondaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 10),
    _ArrisRouterICtrlGetWanDNSSecondaryAddr_Type()
)
arrisRouterICtrlGetWanDNSSecondaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanDNSSecondaryAddr.setStatus("current")
_ArrisRouterICtrlGetWanMacAddress_Type = MacAddress
_ArrisRouterICtrlGetWanMacAddress_Object = MibScalar
arrisRouterICtrlGetWanMacAddress = _ArrisRouterICtrlGetWanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 10, 11),
    _ArrisRouterICtrlGetWanMacAddress_Type()
)
arrisRouterICtrlGetWanMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlGetWanMacAddress.setStatus("current")


class _ArrisRouterICtrlHNAPServerPort_Type(Unsigned32):
    """Custom type arrisRouterICtrlHNAPServerPort based on Unsigned32"""
    defaultValue = 8081


_ArrisRouterICtrlHNAPServerPort_Type.__name__ = "Unsigned32"
_ArrisRouterICtrlHNAPServerPort_Object = MibScalar
arrisRouterICtrlHNAPServerPort = _ArrisRouterICtrlHNAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 11),
    _ArrisRouterICtrlHNAPServerPort_Type()
)
arrisRouterICtrlHNAPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlHNAPServerPort.setStatus("current")


class _ArrisRouterICtrlEnable_Type(Integer32):
    """Custom type arrisRouterICtrlEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ArrisRouterICtrlEnable_Type.__name__ = "Integer32"
_ArrisRouterICtrlEnable_Object = MibScalar
arrisRouterICtrlEnable = _ArrisRouterICtrlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 12),
    _ArrisRouterICtrlEnable_Type()
)
arrisRouterICtrlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlEnable.setStatus("current")


class _ArrisRouterICtrlHashingKey_Type(DisplayString):
    """Custom type arrisRouterICtrlHashingKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_ArrisRouterICtrlHashingKey_Type.__name__ = "DisplayString"
_ArrisRouterICtrlHashingKey_Object = MibScalar
arrisRouterICtrlHashingKey = _ArrisRouterICtrlHashingKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 13),
    _ArrisRouterICtrlHashingKey_Type()
)
arrisRouterICtrlHashingKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlHashingKey.setStatus("current")


class _ArrisRouterICtrlPortMapTableEnabled_Type(TruthValue):
    """Custom type arrisRouterICtrlPortMapTableEnabled based on TruthValue"""
    defaultValue = 1


_ArrisRouterICtrlPortMapTableEnabled_Type.__name__ = "TruthValue"
_ArrisRouterICtrlPortMapTableEnabled_Object = MibScalar
arrisRouterICtrlPortMapTableEnabled = _ArrisRouterICtrlPortMapTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 10, 14),
    _ArrisRouterICtrlPortMapTableEnabled_Type()
)
arrisRouterICtrlPortMapTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterICtrlPortMapTableEnabled.setStatus("current")
_ArrisRouterFlapListCfg_ObjectIdentity = ObjectIdentity
arrisRouterFlapListCfg = _ArrisRouterFlapListCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11)
)


class _ArrisRouterFlapListEnable_Type(TruthValue):
    """Custom type arrisRouterFlapListEnable based on TruthValue"""
    defaultValue = 2


_ArrisRouterFlapListEnable_Type.__name__ = "TruthValue"
_ArrisRouterFlapListEnable_Object = MibScalar
arrisRouterFlapListEnable = _ArrisRouterFlapListEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 1),
    _ArrisRouterFlapListEnable_Type()
)
arrisRouterFlapListEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFlapListEnable.setStatus("current")


class _ArrisRouterFlapListWLANInterval_Type(Integer32):
    """Custom type arrisRouterFlapListWLANInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ArrisRouterFlapListWLANInterval_Type.__name__ = "Integer32"
_ArrisRouterFlapListWLANInterval_Object = MibScalar
arrisRouterFlapListWLANInterval = _ArrisRouterFlapListWLANInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 2),
    _ArrisRouterFlapListWLANInterval_Type()
)
arrisRouterFlapListWLANInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANInterval.setStatus("current")


class _ArrisRouterFlapListDHCPInterval_Type(Integer32):
    """Custom type arrisRouterFlapListDHCPInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ArrisRouterFlapListDHCPInterval_Type.__name__ = "Integer32"
_ArrisRouterFlapListDHCPInterval_Object = MibScalar
arrisRouterFlapListDHCPInterval = _ArrisRouterFlapListDHCPInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 3),
    _ArrisRouterFlapListDHCPInterval_Type()
)
arrisRouterFlapListDHCPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFlapListDHCPInterval.setStatus("current")


class _ArrisRouterFlapListReportPeroid_Type(Integer32):
    """Custom type arrisRouterFlapListReportPeroid based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_ArrisRouterFlapListReportPeroid_Type.__name__ = "Integer32"
_ArrisRouterFlapListReportPeroid_Object = MibScalar
arrisRouterFlapListReportPeroid = _ArrisRouterFlapListReportPeroid_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 4),
    _ArrisRouterFlapListReportPeroid_Type()
)
arrisRouterFlapListReportPeroid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFlapListReportPeroid.setStatus("current")
_ArrisRouterFlapListWLANCount_Type = Integer32
_ArrisRouterFlapListWLANCount_Object = MibScalar
arrisRouterFlapListWLANCount = _ArrisRouterFlapListWLANCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 5),
    _ArrisRouterFlapListWLANCount_Type()
)
arrisRouterFlapListWLANCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANCount.setStatus("current")
_ArrisRouterFlapListLANCount_Type = Integer32
_ArrisRouterFlapListLANCount_Object = MibScalar
arrisRouterFlapListLANCount = _ArrisRouterFlapListLANCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 6),
    _ArrisRouterFlapListLANCount_Type()
)
arrisRouterFlapListLANCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListLANCount.setStatus("current")


class _ArrisRouterFlapListReqFreqThreshold_Type(Integer32):
    """Custom type arrisRouterFlapListReqFreqThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArrisRouterFlapListReqFreqThreshold_Type.__name__ = "Integer32"
_ArrisRouterFlapListReqFreqThreshold_Object = MibScalar
arrisRouterFlapListReqFreqThreshold = _ArrisRouterFlapListReqFreqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 7),
    _ArrisRouterFlapListReqFreqThreshold_Type()
)
arrisRouterFlapListReqFreqThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisRouterFlapListReqFreqThreshold.setStatus("current")
_ArrisRouterFlapListWLANTable_Object = MibTable
arrisRouterFlapListWLANTable = _ArrisRouterFlapListWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10)
)
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANTable.setStatus("current")
_ArrisRouterFlapListWLANEntry_Object = MibTableRow
arrisRouterFlapListWLANEntry = _ArrisRouterFlapListWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10, 1)
)
arrisRouterFlapListWLANEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFlapListWLANIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANEntry.setStatus("current")


class _ArrisRouterFlapListWLANIndex_Type(Unsigned32):
    """Custom type arrisRouterFlapListWLANIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ArrisRouterFlapListWLANIndex_Type.__name__ = "Unsigned32"
_ArrisRouterFlapListWLANIndex_Object = MibTableColumn
arrisRouterFlapListWLANIndex = _ArrisRouterFlapListWLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10, 1, 1),
    _ArrisRouterFlapListWLANIndex_Type()
)
arrisRouterFlapListWLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANIndex.setStatus("current")
_ArrisRouterFlapListWLANMacAddress_Type = MacAddress
_ArrisRouterFlapListWLANMacAddress_Object = MibTableColumn
arrisRouterFlapListWLANMacAddress = _ArrisRouterFlapListWLANMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10, 1, 2),
    _ArrisRouterFlapListWLANMacAddress_Type()
)
arrisRouterFlapListWLANMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANMacAddress.setStatus("current")
_ArrisRouterFlapListWLANRemoveTime_Type = DateAndTime
_ArrisRouterFlapListWLANRemoveTime_Object = MibTableColumn
arrisRouterFlapListWLANRemoveTime = _ArrisRouterFlapListWLANRemoveTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10, 1, 3),
    _ArrisRouterFlapListWLANRemoveTime_Type()
)
arrisRouterFlapListWLANRemoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANRemoveTime.setStatus("current")
_ArrisRouterFlapListWLANFlapTime_Type = DateAndTime
_ArrisRouterFlapListWLANFlapTime_Object = MibTableColumn
arrisRouterFlapListWLANFlapTime = _ArrisRouterFlapListWLANFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 10, 1, 4),
    _ArrisRouterFlapListWLANFlapTime_Type()
)
arrisRouterFlapListWLANFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListWLANFlapTime.setStatus("current")
_ArrisRouterFlapListLANTable_Object = MibTable
arrisRouterFlapListLANTable = _ArrisRouterFlapListLANTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11)
)
if mibBuilder.loadTexts:
    arrisRouterFlapListLANTable.setStatus("current")
_ArrisRouterFlapListLANEntry_Object = MibTableRow
arrisRouterFlapListLANEntry = _ArrisRouterFlapListLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11, 1)
)
arrisRouterFlapListLANEntry.setIndexNames(
    (0, "ARRIS-ROUTER-DEVICE-MIB", "arrisRouterFlapListLANIndex"),
)
if mibBuilder.loadTexts:
    arrisRouterFlapListLANEntry.setStatus("current")


class _ArrisRouterFlapListLANIndex_Type(Unsigned32):
    """Custom type arrisRouterFlapListLANIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ArrisRouterFlapListLANIndex_Type.__name__ = "Unsigned32"
_ArrisRouterFlapListLANIndex_Object = MibTableColumn
arrisRouterFlapListLANIndex = _ArrisRouterFlapListLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11, 1, 1),
    _ArrisRouterFlapListLANIndex_Type()
)
arrisRouterFlapListLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisRouterFlapListLANIndex.setStatus("current")
_ArrisRouterFlapListLANMacAddress_Type = MacAddress
_ArrisRouterFlapListLANMacAddress_Object = MibTableColumn
arrisRouterFlapListLANMacAddress = _ArrisRouterFlapListLANMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11, 1, 2),
    _ArrisRouterFlapListLANMacAddress_Type()
)
arrisRouterFlapListLANMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListLANMacAddress.setStatus("current")
_ArrisRouterFlapListLANRemoveTime_Type = DateAndTime
_ArrisRouterFlapListLANRemoveTime_Object = MibTableColumn
arrisRouterFlapListLANRemoveTime = _ArrisRouterFlapListLANRemoveTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11, 1, 3),
    _ArrisRouterFlapListLANRemoveTime_Type()
)
arrisRouterFlapListLANRemoveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListLANRemoveTime.setStatus("current")
_ArrisRouterFlapListLANFlapTime_Type = DateAndTime
_ArrisRouterFlapListLANFlapTime_Object = MibTableColumn
arrisRouterFlapListLANFlapTime = _ArrisRouterFlapListLANFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 1, 1, 11, 11, 1, 4),
    _ArrisRouterFlapListLANFlapTime_Type()
)
arrisRouterFlapListLANFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisRouterFlapListLANFlapTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-ROUTER-DEVICE-MIB",
    **{"arrisRouterMib": arrisRouterMib,
       "arrisRouterMibObjects": arrisRouterMibObjects,
       "arrisRouterWanConfig": arrisRouterWanConfig,
       "arrisRouterWanConnType": arrisRouterWanConnType,
       "arrisRouterWanConnHostName": arrisRouterWanConnHostName,
       "arrisRouterWanConnDomainName": arrisRouterWanConnDomainName,
       "arrisRouterWanMTUSize": arrisRouterWanMTUSize,
       "arrisRouterWanCurrentTable": arrisRouterWanCurrentTable,
       "arrisRouterWanCurrentEntry": arrisRouterWanCurrentEntry,
       "arrisRouterWanCurrentIPIndex": arrisRouterWanCurrentIPIndex,
       "arrisRouterWanCurrentIPAddrType": arrisRouterWanCurrentIPAddrType,
       "arrisRouterWanCurrentIPAddr": arrisRouterWanCurrentIPAddr,
       "arrisRouterWanCurrentPrefix": arrisRouterWanCurrentPrefix,
       "arrisRouterWanCurrentGWType": arrisRouterWanCurrentGWType,
       "arrisRouterWanCurrentGW": arrisRouterWanCurrentGW,
       "arrisRouterWanCurrentIPType": arrisRouterWanCurrentIPType,
       "arrisRouterWanCurrentNetMask": arrisRouterWanCurrentNetMask,
       "arrisRouterWanCurrentPrefixDelegationV6": arrisRouterWanCurrentPrefixDelegationV6,
       "arrisRouterWanCurrentPrefixDelegationV6Len": arrisRouterWanCurrentPrefixDelegationV6Len,
       "arrisRouterWanCurrentPreferredLifetimeV6": arrisRouterWanCurrentPreferredLifetimeV6,
       "arrisRouterWanCurrentValidLifetimeV6": arrisRouterWanCurrentValidLifetimeV6,
       "arrisRouterWanStaticFreeIdx": arrisRouterWanStaticFreeIdx,
       "arrisRouterWanStaticTable": arrisRouterWanStaticTable,
       "arrisRouterWanStaticEntry": arrisRouterWanStaticEntry,
       "arrisRouterWanStaticIPIndex": arrisRouterWanStaticIPIndex,
       "arrisRouterWanStaticIPAddrType": arrisRouterWanStaticIPAddrType,
       "arrisRouterWanStaticIPAddr": arrisRouterWanStaticIPAddr,
       "arrisRouterWanStaticPrefix": arrisRouterWanStaticPrefix,
       "arrisRouterWanStaticGatewayType": arrisRouterWanStaticGatewayType,
       "arrisRouterWanStaticGateway": arrisRouterWanStaticGateway,
       "arrisRouterWanStaticRowStatus": arrisRouterWanStaticRowStatus,
       "arrisRouterWanDelegatedPrefixLength": arrisRouterWanDelegatedPrefixLength,
       "arrisRouterWanDelegatedPrefix": arrisRouterWanDelegatedPrefix,
       "arrisRouterWanTunnelObjects": arrisRouterWanTunnelObjects,
       "arrisRouterWanUserName": arrisRouterWanUserName,
       "arrisRouterWanPassword": arrisRouterWanPassword,
       "arrisRouterWanEnableIdleTimeout": arrisRouterWanEnableIdleTimeout,
       "arrisRouterWanIdleTimeout": arrisRouterWanIdleTimeout,
       "arrisRouterWanTunnelAddrType": arrisRouterWanTunnelAddrType,
       "arrisRouterWanTunnelAddr": arrisRouterWanTunnelAddr,
       "arrisRouterWanTunnelHostName": arrisRouterWanTunnelHostName,
       "arrisRouterWanEnableKeepAlive": arrisRouterWanEnableKeepAlive,
       "arrisRouterWanKeepAliveTimeout": arrisRouterWanKeepAliveTimeout,
       "arrisRouterWanDNSObjects": arrisRouterWanDNSObjects,
       "arrisRouterWanUseAutoDNS": arrisRouterWanUseAutoDNS,
       "arrisRouterWanCurrentDNSTable": arrisRouterWanCurrentDNSTable,
       "arrisRouterWanCurrentDNSEntry": arrisRouterWanCurrentDNSEntry,
       "arrisRouterWanCurrentDNSIPIndex": arrisRouterWanCurrentDNSIPIndex,
       "arrisRouterWanCurrentDNSIPAddrType": arrisRouterWanCurrentDNSIPAddrType,
       "arrisRouterWanCurrentDNSIPAddr": arrisRouterWanCurrentDNSIPAddr,
       "arrisRouterWanStaticDNSTable": arrisRouterWanStaticDNSTable,
       "arrisRouterWanStaticDNSEntry": arrisRouterWanStaticDNSEntry,
       "arrisRouterWanStaticDNSIPIndex": arrisRouterWanStaticDNSIPIndex,
       "arrisRouterWanStaticDNSIPAddrType": arrisRouterWanStaticDNSIPAddrType,
       "arrisRouterWanStaticDNSIPAddr": arrisRouterWanStaticDNSIPAddr,
       "arrisRouterWanStaticDNSRowStatus": arrisRouterWanStaticDNSRowStatus,
       "arrisRouterWanDHCPObjects": arrisRouterWanDHCPObjects,
       "arrisRouterWanRenewLease": arrisRouterWanRenewLease,
       "arrisRouterWanReleaseLease": arrisRouterWanReleaseLease,
       "arrisRouterWanDHCPDuration": arrisRouterWanDHCPDuration,
       "arrisRouterWanDHCPExpire": arrisRouterWanDHCPExpire,
       "arrisRouterWanRenewLeaseV6": arrisRouterWanRenewLeaseV6,
       "arrisRouterWanReleaseLeaseV6": arrisRouterWanReleaseLeaseV6,
       "arrisRouterWanDHCPDurationV6": arrisRouterWanDHCPDurationV6,
       "arrisRouterWanDHCPExpireV6": arrisRouterWanDHCPExpireV6,
       "arrisRouterWanDhcpSrvIPAddr": arrisRouterWanDhcpSrvIPAddr,
       "arrisRouterWanDhcpOpt43Sub02": arrisRouterWanDhcpOpt43Sub02,
       "arrisRouterWanDHCPDUIDV6": arrisRouterWanDHCPDUIDV6,
       "arrisRouterWanDHCPSrvAddrV6": arrisRouterWanDHCPSrvAddrV6,
       "arrisRouterWanDHCPSrvDUIDV6": arrisRouterWanDHCPSrvDUIDV6,
       "arrisRouterWanIFMacAddr": arrisRouterWanIFMacAddr,
       "arrisRouterWanConnTypeV6": arrisRouterWanConnTypeV6,
       "arrisRouterWanIPProvMode": arrisRouterWanIPProvMode,
       "arrisRouterDSLiteWanObjects": arrisRouterDSLiteWanObjects,
       "arrisRouterDSLiteWanEnable": arrisRouterDSLiteWanEnable,
       "arrisRouterDSLiteWanLSNATAddrType": arrisRouterDSLiteWanLSNATAddrType,
       "arrisRouterDSLiteWanLSNATAddr": arrisRouterDSLiteWanLSNATAddr,
       "arrisRouterDSLiteTcpMssClamping": arrisRouterDSLiteTcpMssClamping,
       "arrisRouterDSLiteTcpMssValue": arrisRouterDSLiteTcpMssValue,
       "arrisRouterDSLiteWanResolvedAddr": arrisRouterDSLiteWanResolvedAddr,
       "arrisRouterSoftGreWanObjects": arrisRouterSoftGreWanObjects,
       "arrisRouterSoftGreWanTable": arrisRouterSoftGreWanTable,
       "arrisRouterSoftGreWanEntry": arrisRouterSoftGreWanEntry,
       "arrisRouterSoftGreWanEnable": arrisRouterSoftGreWanEnable,
       "arrisRouterSoftGreMappedInterface": arrisRouterSoftGreMappedInterface,
       "arrisRouterSoftGreMaxSessions": arrisRouterSoftGreMaxSessions,
       "arrisRouterSoftGreWanControllerFqdn": arrisRouterSoftGreWanControllerFqdn,
       "arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType": arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddressType,
       "arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress": arrisRouterSoftGreWanControllerProvisionedSecondaryIpAddress,
       "arrisRouterSoftGreWanFailoverPingCount": arrisRouterSoftGreWanFailoverPingCount,
       "arrisRouterSoftGreWanFailoverPingInterval": arrisRouterSoftGreWanFailoverPingInterval,
       "arrisRouterSoftGreWanFailoverThreshold": arrisRouterSoftGreWanFailoverThreshold,
       "arrisRouterSoftGreCircuitIdEnabled": arrisRouterSoftGreCircuitIdEnabled,
       "arrisRouterSoftGreRemoteIdEnabled": arrisRouterSoftGreRemoteIdEnabled,
       "arrisRouterSoftGreRadiusEnabled": arrisRouterSoftGreRadiusEnabled,
       "arrisRouterSoftGreRadiusServerAddressType": arrisRouterSoftGreRadiusServerAddressType,
       "arrisRouterSoftGreRadiusServerAddress": arrisRouterSoftGreRadiusServerAddress,
       "arrisRouterSoftGreRadiusServerPort": arrisRouterSoftGreRadiusServerPort,
       "arrisRouterSoftGreRadiusKey": arrisRouterSoftGreRadiusKey,
       "arrisRouterSoftGreRadiusReAuthInterval": arrisRouterSoftGreRadiusReAuthInterval,
       "arrisRouterSoftGreVlanQEnable": arrisRouterSoftGreVlanQEnable,
       "arrisRouterSoftGreWanDscp": arrisRouterSoftGreWanDscp,
       "arrisRouterSoftGreWanDNSRetryTimer": arrisRouterSoftGreWanDNSRetryTimer,
       "arrisRouterSoftGreWanCurrentControllerIPAddressType": arrisRouterSoftGreWanCurrentControllerIPAddressType,
       "arrisRouterSoftGreWanCurrentControllerIPAddress": arrisRouterSoftGreWanCurrentControllerIPAddress,
       "arrisRouterSoftGreWanPrimaryControllerIPAddressType": arrisRouterSoftGreWanPrimaryControllerIPAddressType,
       "arrisRouterSoftGreWanPrimaryControllerIPAddress": arrisRouterSoftGreWanPrimaryControllerIPAddress,
       "arrisRouterSoftGreWanSecondaryControllerIPAddressType": arrisRouterSoftGreWanSecondaryControllerIPAddressType,
       "arrisRouterSoftGreWanSecondaryControllerIPAddress": arrisRouterSoftGreWanSecondaryControllerIPAddress,
       "arrisRouterSoftGreWanStatus": arrisRouterSoftGreWanStatus,
       "arrisRouterSoftGreTransportInterface": arrisRouterSoftGreTransportInterface,
       "arrisRouterSoftGreRadiusTransportInterface": arrisRouterSoftGreRadiusTransportInterface,
       "arrisRouterSoftGreAcctServerAddressType": arrisRouterSoftGreAcctServerAddressType,
       "arrisRouterSoftGreAcctServerAddress": arrisRouterSoftGreAcctServerAddress,
       "arrisRouterSoftGreAcctServerPort": arrisRouterSoftGreAcctServerPort,
       "arrisRouterSoftGreAcctKey": arrisRouterSoftGreAcctKey,
       "arrisRouterSoftGreAcctInterval": arrisRouterSoftGreAcctInterval,
       "arrisRouterSoftGreRadiusSecondaryServerAddressType": arrisRouterSoftGreRadiusSecondaryServerAddressType,
       "arrisRouterSoftGreRadiusSecondaryServerAddress": arrisRouterSoftGreRadiusSecondaryServerAddress,
       "arrisRouterSoftGreRadiusSecondaryServerPort": arrisRouterSoftGreRadiusSecondaryServerPort,
       "arrisRouterSoftGreRadiusSecondaryKey": arrisRouterSoftGreRadiusSecondaryKey,
       "arrisRouterSoftGreRadiusSecondaryReAuthInterval": arrisRouterSoftGreRadiusSecondaryReAuthInterval,
       "arrisRouterSoftGreSSIDTable": arrisRouterSoftGreSSIDTable,
       "arrisRouterSoftGreSSIDEntry": arrisRouterSoftGreSSIDEntry,
       "arrisRouterSoftGreVLanId": arrisRouterSoftGreVLanId,
       "arrisRouterSoftGreVLanPriority": arrisRouterSoftGreVLanPriority,
       "arrisRouterSoftGreCustomerOptOut": arrisRouterSoftGreCustomerOptOut,
       "arrisRouterSoftGreCapable": arrisRouterSoftGreCapable,
       "arrisRouterDHCPRelayAgentWanObjects": arrisRouterDHCPRelayAgentWanObjects,
       "arrisRouterDHCPRelayAgentSSIDTable": arrisRouterDHCPRelayAgentSSIDTable,
       "arrisRouterDHCPRelayAgentSSIDEntry": arrisRouterDHCPRelayAgentSSIDEntry,
       "arrisRouterDHCPRelayAgentEnable": arrisRouterDHCPRelayAgentEnable,
       "arrisRouterDHCPRelayAgentCircuitIdEnabled": arrisRouterDHCPRelayAgentCircuitIdEnabled,
       "arrisRouterDHCPRelayAgentRemoteIdEnabled": arrisRouterDHCPRelayAgentRemoteIdEnabled,
       "arrisRouterDHCPRelayAgentOption60SSIDEnabled": arrisRouterDHCPRelayAgentOption60SSIDEnabled,
       "arrisRouterWanTR181GatewayInfoObjects": arrisRouterWanTR181GatewayInfoObjects,
       "arrisRouterTR181GatewayManufacturerOUI": arrisRouterTR181GatewayManufacturerOUI,
       "arrisRouterTR181GatewayProductClass": arrisRouterTR181GatewayProductClass,
       "arrisRouterTR181GatewaySerialNumber": arrisRouterTR181GatewaySerialNumber,
       "arrisRouterWanForceIGMPVersion": arrisRouterWanForceIGMPVersion,
       "arrisRouterLanConfig": arrisRouterLanConfig,
       "arrisRouterLanSrvTable": arrisRouterLanSrvTable,
       "arrisRouterLanSrvEntry": arrisRouterLanSrvEntry,
       "arrisRouterLanName": arrisRouterLanName,
       "arrisRouterLanSubnetMaskType": arrisRouterLanSubnetMaskType,
       "arrisRouterLanSubnetMask": arrisRouterLanSubnetMask,
       "arrisRouterLanGatewayIpType": arrisRouterLanGatewayIpType,
       "arrisRouterLanGatewayIp": arrisRouterLanGatewayIp,
       "arrisRouterLanGatewayIp2Type": arrisRouterLanGatewayIp2Type,
       "arrisRouterLanGatewayIp2": arrisRouterLanGatewayIp2,
       "arrisRouterLanVLanID": arrisRouterLanVLanID,
       "arrisRouterLanUseDHCP": arrisRouterLanUseDHCP,
       "arrisRouterLanStartDHCPType": arrisRouterLanStartDHCPType,
       "arrisRouterLanStartDHCP": arrisRouterLanStartDHCP,
       "arrisRouterLanEndDHCPType": arrisRouterLanEndDHCPType,
       "arrisRouterLanEndDHCP": arrisRouterLanEndDHCP,
       "arrisRouterLanLeaseTime": arrisRouterLanLeaseTime,
       "arrisRouterLanDomainName": arrisRouterLanDomainName,
       "arrisRouterLanRelayDNS": arrisRouterLanRelayDNS,
       "arrisRouterLanPassThru": arrisRouterLanPassThru,
       "arrisRouterLanFirewallOn": arrisRouterLanFirewallOn,
       "arrisRouterLanUPnPEnable": arrisRouterLanUPnPEnable,
       "arrisRouterLanCPEAging": arrisRouterLanCPEAging,
       "arrisRouterLanOverrideDNS": arrisRouterLanOverrideDNS,
       "arrisRouterLanNatAlgsEnabled": arrisRouterLanNatAlgsEnabled,
       "arrisRouterLanMappedInterface": arrisRouterLanMappedInterface,
       "arrisRouterLanEnvironmentControl": arrisRouterLanEnvironmentControl,
       "arrisRouterLanPrefixLengthV6": arrisRouterLanPrefixLengthV6,
       "arrisRouterLanUseDHCPV6": arrisRouterLanUseDHCPV6,
       "arrisRouterLanStartDHCPV6": arrisRouterLanStartDHCPV6,
       "arrisRouterLanEndDHCPV6": arrisRouterLanEndDHCPV6,
       "arrisRouterLanLeaseTimeV6": arrisRouterLanLeaseTimeV6,
       "arrisRouterLanLinkLocalAddressV6": arrisRouterLanLinkLocalAddressV6,
       "arrisRouterLanDNSRelayV6": arrisRouterLanDNSRelayV6,
       "arrisRouterLanDNSOverrideV6": arrisRouterLanDNSOverrideV6,
       "arrisRouterLanPreProvLeaseTime": arrisRouterLanPreProvLeaseTime,
       "arrisRouterLanParentalControlsEnable": arrisRouterLanParentalControlsEnable,
       "arrisRouterLanDNSTable": arrisRouterLanDNSTable,
       "arrisRouterLanDNSEntry": arrisRouterLanDNSEntry,
       "arrisRouterLanDNSIdx": arrisRouterLanDNSIdx,
       "arrisRouterLanDNSIPAddrType": arrisRouterLanDNSIPAddrType,
       "arrisRouterLanDNSIPAddr": arrisRouterLanDNSIPAddr,
       "arrisRouterLanDNSRowStatus": arrisRouterLanDNSRowStatus,
       "arrisRouterClientObjects": arrisRouterClientObjects,
       "arrisRouterLanClientCount": arrisRouterLanClientCount,
       "arrisRouterLanClientTable": arrisRouterLanClientTable,
       "arrisRouterLanClientEntry": arrisRouterLanClientEntry,
       "arrisRouterLanClientIPAddrType": arrisRouterLanClientIPAddrType,
       "arrisRouterLanClientIPAddr": arrisRouterLanClientIPAddr,
       "arrisRouterLanClientHostName": arrisRouterLanClientHostName,
       "arrisRouterLanClientMAC": arrisRouterLanClientMAC,
       "arrisRouterLanClientAdapterType": arrisRouterLanClientAdapterType,
       "arrisRouterLanClientType": arrisRouterLanClientType,
       "arrisRouterLanClientLeaseEnd": arrisRouterLanClientLeaseEnd,
       "arrisRouterLanClientRowStatus": arrisRouterLanClientRowStatus,
       "arrisRouterLanClientOnline": arrisRouterLanClientOnline,
       "arrisRouterLanClientComment": arrisRouterLanClientComment,
       "arrisRouterLanClientManufacturerOUI": arrisRouterLanClientManufacturerOUI,
       "arrisRouterLanClientSerialNumber": arrisRouterLanClientSerialNumber,
       "arrisRouterLanClientProductClass": arrisRouterLanClientProductClass,
       "arrisRouterLanClientDeviceName": arrisRouterLanClientDeviceName,
       "arrisRouterLanClientLastChange": arrisRouterLanClientLastChange,
       "arrisRouterLanClientTimeConnected": arrisRouterLanClientTimeConnected,
       "arrisRouterDeviceUpDownTable": arrisRouterDeviceUpDownTable,
       "arrisRouterDeviceUpDownEntry": arrisRouterDeviceUpDownEntry,
       "arrisRouterDeviceUpDownIndex": arrisRouterDeviceUpDownIndex,
       "arrisRouterDeviceUpDownMAC": arrisRouterDeviceUpDownMAC,
       "arrisRouterDeviceUpDownIPType": arrisRouterDeviceUpDownIPType,
       "arrisRouterDeviceUpDownStatus": arrisRouterDeviceUpDownStatus,
       "arrisRouterLanCustomCount": arrisRouterLanCustomCount,
       "arrisRouterLanCustomTable": arrisRouterLanCustomTable,
       "arrisRouterLanCustomEntry": arrisRouterLanCustomEntry,
       "arrisRouterLanCustomIdx": arrisRouterLanCustomIdx,
       "arrisRouterLanCustomMAC": arrisRouterLanCustomMAC,
       "arrisRouterLanCustomIPAddrType": arrisRouterLanCustomIPAddrType,
       "arrisRouterLanCustomIPAddr": arrisRouterLanCustomIPAddr,
       "arrisRouterLanCustomFriendName": arrisRouterLanCustomFriendName,
       "arrisRouterLanCustomHostName": arrisRouterLanCustomHostName,
       "arrisRouterLanCustomMACMfg": arrisRouterLanCustomMACMfg,
       "arrisRouterLanCustomComments": arrisRouterLanCustomComments,
       "arrisRouterLanCustomRowStatus": arrisRouterLanCustomRowStatus,
       "arrisRouterLanClientDHCPOptionsTable": arrisRouterLanClientDHCPOptionsTable,
       "arrisRouterLanClientDHCPOptionsEntry": arrisRouterLanClientDHCPOptionsEntry,
       "arrisRouterLanClientDHCPOptionsIdx": arrisRouterLanClientDHCPOptionsIdx,
       "arrisRouterLanClientDHCPOptionsTag": arrisRouterLanClientDHCPOptionsTag,
       "arrisRouterLanClientDHCPOptionsValue": arrisRouterLanClientDHCPOptionsValue,
       "arrisRouterLanClientDHCPOptionsRowStatus": arrisRouterLanClientDHCPOptionsRowStatus,
       "arrisRouterRIPObjects": arrisRouterRIPObjects,
       "arrisRouterRIPEnable": arrisRouterRIPEnable,
       "arrisRouterRIPAuthEnable": arrisRouterRIPAuthEnable,
       "arrisRouterRIPReportTime": arrisRouterRIPReportTime,
       "arrisRouterRIPAuthKeyString": arrisRouterRIPAuthKeyString,
       "arrisRouterRIPAuthKeyID": arrisRouterRIPAuthKeyID,
       "arrisRouterRIPIPAddrType": arrisRouterRIPIPAddrType,
       "arrisRouterRIPIPAddr": arrisRouterRIPIPAddr,
       "arrisRouterRIPPrefixLen": arrisRouterRIPPrefixLen,
       "arrisRouterRIPAuthKeyChain": arrisRouterRIPAuthKeyChain,
       "arrisRouterRIPRoutedSubnetIPType": arrisRouterRIPRoutedSubnetIPType,
       "arrisRouterRIPRoutedSubnetIP": arrisRouterRIPRoutedSubnetIP,
       "arrisRouterRIPRoutedSubnetGWNetIPType": arrisRouterRIPRoutedSubnetGWNetIPType,
       "arrisRouterRIPRoutedSubnetGWNetIP": arrisRouterRIPRoutedSubnetGWNetIP,
       "arrisRouterRIPRoutedSubnetMask": arrisRouterRIPRoutedSubnetMask,
       "arrisRouterRIPRoutedSubnetEnabled": arrisRouterRIPRoutedSubnetEnabled,
       "arrisRouterRIPSendCMInterface": arrisRouterRIPSendCMInterface,
       "arrisRouterRIPRoutedSubnetDHCP": arrisRouterRIPRoutedSubnetDHCP,
       "arrisRouterRIPRoutedSubnetNAT": arrisRouterRIPRoutedSubnetNAT,
       "arrisRouterLanSettings": arrisRouterLanSettings,
       "arrisRouterLanEtherPortTable": arrisRouterLanEtherPortTable,
       "arrisRouterLanEtherPortEntry": arrisRouterLanEtherPortEntry,
       "arrisRouterLanEtherPortIdx": arrisRouterLanEtherPortIdx,
       "arrisRouterLanEtherPortIFIndex": arrisRouterLanEtherPortIFIndex,
       "arrisRouterLanEtherPortEnabled": arrisRouterLanEtherPortEnabled,
       "arrisRouterLanEtherPortDuplex": arrisRouterLanEtherPortDuplex,
       "arrisRouterLanEtherPortSpeed": arrisRouterLanEtherPortSpeed,
       "arrisRouterLanEtherPortAuto": arrisRouterLanEtherPortAuto,
       "arrisRouterLanEtherPortHasLink": arrisRouterLanEtherPortHasLink,
       "arrisRouterRIPngObjects": arrisRouterRIPngObjects,
       "arrisRouterRIPngEnable": arrisRouterRIPngEnable,
       "arrisRouterRIPngAddr": arrisRouterRIPngAddr,
       "arrisRouterRIPngSubnetEnable": arrisRouterRIPngSubnetEnable,
       "arrisRouterRIPngRoutedSubnetAddr": arrisRouterRIPngRoutedSubnetAddr,
       "arrisRouterRIPngRoutedSubnetPrefixLength": arrisRouterRIPngRoutedSubnetPrefixLength,
       "arrisRouterRIPngSendCMInterface": arrisRouterRIPngSendCMInterface,
       "arrisRouterLanSrvDHCPOptionsTable": arrisRouterLanSrvDHCPOptionsTable,
       "arrisRouterLanSrvDHCPOptionsEntry": arrisRouterLanSrvDHCPOptionsEntry,
       "arrisRouterLanSrvDHCPOptionsIdx": arrisRouterLanSrvDHCPOptionsIdx,
       "arrisRouterLanSrvDHCPOptionsEnable": arrisRouterLanSrvDHCPOptionsEnable,
       "arrisRouterLanSrvDHCPOptionsIPAddrType": arrisRouterLanSrvDHCPOptionsIPAddrType,
       "arrisRouterLanSrvDHCPOptionsTag": arrisRouterLanSrvDHCPOptionsTag,
       "arrisRouterLanSrvDHCPOptionsValue": arrisRouterLanSrvDHCPOptionsValue,
       "arrisRouterLanSrvDHCPOptionsRowStatus": arrisRouterLanSrvDHCPOptionsRowStatus,
       "arrisRouterLanMaxIPv6RAInterval": arrisRouterLanMaxIPv6RAInterval,
       "arrisRouterLanMinIPv6RAInterval": arrisRouterLanMinIPv6RAInterval,
       "arrisRouterLanBridgeType": arrisRouterLanBridgeType,
       "arrisRouterLanUSBPortTable": arrisRouterLanUSBPortTable,
       "arrisRouterLanUSBPortEntry": arrisRouterLanUSBPortEntry,
       "arrisRouterLanUSBPortIdx": arrisRouterLanUSBPortIdx,
       "arrisRouterLanUSBPortHasLink": arrisRouterLanUSBPortHasLink,
       "arrisRouterLanUSBPortDescr": arrisRouterLanUSBPortDescr,
       "arrisRouterLanUSBPortSerialNum": arrisRouterLanUSBPortSerialNum,
       "arrisRouterLanUSBPortSpeed": arrisRouterLanUSBPortSpeed,
       "arrisRouterLanUSBPortManuf": arrisRouterLanUSBPortManuf,
       "arrisRouterLanUSBPortStorageNam": arrisRouterLanUSBPortStorageNam,
       "arrisRouterLanUSBPortFileSys": arrisRouterLanUSBPortFileSys,
       "arrisRouterLanUSBPortSpaceAvail": arrisRouterLanUSBPortSpaceAvail,
       "arrisRouterLanUSBPortTotalSpace": arrisRouterLanUSBPortTotalSpace,
       "arrisRouterLanUsbPortFoldersFile": arrisRouterLanUsbPortFoldersFile,
       "arrisRouterLanUSBPortDelStorage": arrisRouterLanUSBPortDelStorage,
       "arrisRouterLanFileSharingObjs": arrisRouterLanFileSharingObjs,
       "arrisRouterLanFilesharingEnable": arrisRouterLanFilesharingEnable,
       "arrisRouterLanFilesharingDevName": arrisRouterLanFilesharingDevName,
       "arrisRouterLanFileSharingTable": arrisRouterLanFileSharingTable,
       "arrisRouterLanFileSharingEntry": arrisRouterLanFileSharingEntry,
       "arrisRouterLanFilesharingIdx": arrisRouterLanFilesharingIdx,
       "arrisRouterLanFilesharingRowStatus": arrisRouterLanFilesharingRowStatus,
       "arrisRouterLanFilesharingUsbPort": arrisRouterLanFilesharingUsbPort,
       "arrisRouterLanFilesharingDirectory": arrisRouterLanFilesharingDirectory,
       "arrisRouterLanFilesharingName": arrisRouterLanFilesharingName,
       "arrisRouterLanFilesharingEnableHttp": arrisRouterLanFilesharingEnableHttp,
       "arrisRouterLanFilesharingEnableFtp": arrisRouterLanFilesharingEnableFtp,
       "arrisRouterLanFilesharingVisibility": arrisRouterLanFilesharingVisibility,
       "arrisRouterLanFilesharingEveryOnePerm": arrisRouterLanFilesharingEveryOnePerm,
       "arrisRouterLanFilesharingDesc": arrisRouterLanFilesharingDesc,
       "arrisRouterLanLocalUserTable": arrisRouterLanLocalUserTable,
       "arrisRouterLanLocalUserEntry": arrisRouterLanLocalUserEntry,
       "arrisRouterLanLocalUserIdx": arrisRouterLanLocalUserIdx,
       "arrisRouterLanLocalUserRowStatus": arrisRouterLanLocalUserRowStatus,
       "arrisRouterLanLocalUserName": arrisRouterLanLocalUserName,
       "arrisRouterLanLocalUserPasswd": arrisRouterLanLocalUserPasswd,
       "arrisRouterLanFilesharingPermitTable": arrisRouterLanFilesharingPermitTable,
       "arrisRouterLanFilesharingPermitEntry": arrisRouterLanFilesharingPermitEntry,
       "arrisRouterLanFilesharingPermitvalue": arrisRouterLanFilesharingPermitvalue,
       "arrisRouterLanIPv6RALifetime": arrisRouterLanIPv6RALifetime,
       "arrisRouterWirelessCfg": arrisRouterWirelessCfg,
       "arrisRouterWiFiCountry": arrisRouterWiFiCountry,
       "arrisRouterWiFiChannel": arrisRouterWiFiChannel,
       "arrisRouterWiFiMode": arrisRouterWiFiMode,
       "arrisRouterWiFiBGProtect": arrisRouterWiFiBGProtect,
       "arrisRouterWiFiBeaconInterval": arrisRouterWiFiBeaconInterval,
       "arrisRouterWiFiDTIMInterval": arrisRouterWiFiDTIMInterval,
       "arrisRouterWiFiTxPreamble": arrisRouterWiFiTxPreamble,
       "arrisRouterWiFiRTSThreshold": arrisRouterWiFiRTSThreshold,
       "arrisRouterWiFiFragmentThresh": arrisRouterWiFiFragmentThresh,
       "arrisRouterWiFiShortSlot": arrisRouterWiFiShortSlot,
       "arrisRouterWiFiFrameBurst": arrisRouterWiFiFrameBurst,
       "arrisRouterWiFiEnableRadio": arrisRouterWiFiEnableRadio,
       "arrisRouterWiFiShortRetryLimit": arrisRouterWiFiShortRetryLimit,
       "arrisRouterWiFiLongRetryLimit": arrisRouterWiFiLongRetryLimit,
       "arrisRouterWiFiOutputPower": arrisRouterWiFiOutputPower,
       "arrisRouterWiFi80211NSettings": arrisRouterWiFi80211NSettings,
       "arrisRouterWiFi80211NBand": arrisRouterWiFi80211NBand,
       "arrisRouterWiFiHTMCS": arrisRouterWiFiHTMCS,
       "arrisRouterWiFiChannelBW": arrisRouterWiFiChannelBW,
       "arrisRouterWiFi80211NSideBand": arrisRouterWiFi80211NSideBand,
       "arrisRouterWiFiHTMode": arrisRouterWiFiHTMode,
       "arrisRouterWiFiGuardInterval": arrisRouterWiFiGuardInterval,
       "arrisRouterWiFiDeclinePeerBA": arrisRouterWiFiDeclinePeerBA,
       "arrisRouterWiFiBlockAck": arrisRouterWiFiBlockAck,
       "arrisRouterWiFiNProtection": arrisRouterWiFiNProtection,
       "arrisRouterWiFiAllow40MHzOnlyOperation": arrisRouterWiFiAllow40MHzOnlyOperation,
       "arrisRouterBSSTable": arrisRouterBSSTable,
       "arrisRouterBSSEntry": arrisRouterBSSEntry,
       "arrisRouterBssID": arrisRouterBssID,
       "arrisRouterBssSSID": arrisRouterBssSSID,
       "arrisRouterBssActive": arrisRouterBssActive,
       "arrisRouterBssSSIDBroadcast": arrisRouterBssSSIDBroadcast,
       "arrisRouterBssSecurityMode": arrisRouterBssSecurityMode,
       "arrisRouterBssAccessMode": arrisRouterBssAccessMode,
       "arrisRouterBssNetworkIsolate": arrisRouterBssNetworkIsolate,
       "arrisRouterBssMACAccessCount": arrisRouterBssMACAccessCount,
       "arrisRouterBssMACAccessClear": arrisRouterBssMACAccessClear,
       "arrisRouterBSSArpAuditInterval": arrisRouterBSSArpAuditInterval,
       "arrisRouterBssMaxWifiClients": arrisRouterBssMaxWifiClients,
       "arrisRouterBssWmmEnable": arrisRouterBssWmmEnable,
       "arrisRouterBssWmmAPSD": arrisRouterBssWmmAPSD,
       "arrisRouterBssActiveTimeout": arrisRouterBssActiveTimeout,
       "arrisRouterDefaultBssSSID": arrisRouterDefaultBssSSID,
       "arrisRouterBssStaSteeringEnable": arrisRouterBssStaSteeringEnable,
       "arrisRouterWEPTable": arrisRouterWEPTable,
       "arrisRouterWEPEntry": arrisRouterWEPEntry,
       "arrisRouterWEPCurrentKey": arrisRouterWEPCurrentKey,
       "arrisRouterWEPEncryptionMode": arrisRouterWEPEncryptionMode,
       "arrisRouterWEP64BitKeyTable": arrisRouterWEP64BitKeyTable,
       "arrisRouterWEP64BitKeyEntry": arrisRouterWEP64BitKeyEntry,
       "arrisRouterWEP64BitKeyIndex": arrisRouterWEP64BitKeyIndex,
       "arrisRouterWEP64BitKeyValue": arrisRouterWEP64BitKeyValue,
       "arrisRouterWEP64BitKeyStatus": arrisRouterWEP64BitKeyStatus,
       "arrisRouterWEP128BitKeyTable": arrisRouterWEP128BitKeyTable,
       "arrisRouterWEP128BitKeyEntry": arrisRouterWEP128BitKeyEntry,
       "arrisRouterWEP128BitKeyIndex": arrisRouterWEP128BitKeyIndex,
       "arrisRouterWEP128BitKeyValue": arrisRouterWEP128BitKeyValue,
       "arrisRouterWEP128BitKeyStatus": arrisRouterWEP128BitKeyStatus,
       "arrisRouterWPATable": arrisRouterWPATable,
       "arrisRouterWPAEntry": arrisRouterWPAEntry,
       "arrisRouterWPAAlgorithm": arrisRouterWPAAlgorithm,
       "arrisRouterWPAPreSharedKey": arrisRouterWPAPreSharedKey,
       "arrisRouterWPAReAuthInterval": arrisRouterWPAReAuthInterval,
       "arrisRouterWPAPreAuthEnable": arrisRouterWPAPreAuthEnable,
       "arrisRouterDefaultWPAPreSharedKey": arrisRouterDefaultWPAPreSharedKey,
       "arrisRouterRadiusTable": arrisRouterRadiusTable,
       "arrisRouterRadiusEntry": arrisRouterRadiusEntry,
       "arrisRouterRadiusAddressType": arrisRouterRadiusAddressType,
       "arrisRouterRadiusAddress": arrisRouterRadiusAddress,
       "arrisRouterRadiusPort": arrisRouterRadiusPort,
       "arrisRouterRadiusKey": arrisRouterRadiusKey,
       "arrisRouterRadiusReAuthInterval": arrisRouterRadiusReAuthInterval,
       "arrisRouterMACAccessTable": arrisRouterMACAccessTable,
       "arrisRouterMACAccessEntry": arrisRouterMACAccessEntry,
       "arrisRouterMACAccessIndex": arrisRouterMACAccessIndex,
       "arrisRouterMACAccessAddr": arrisRouterMACAccessAddr,
       "arrisRouterMACAccessStatus": arrisRouterMACAccessStatus,
       "arrisRouterMACAccessDeviceName": arrisRouterMACAccessDeviceName,
       "arrisRouterWMMCfg": arrisRouterWMMCfg,
       "arrisRouterWMMEnable": arrisRouterWMMEnable,
       "arrisRouterWMMNoAck": arrisRouterWMMNoAck,
       "arrisRouterWMMAPSD": arrisRouterWMMAPSD,
       "arrisRouterWMMEDCAAPTable": arrisRouterWMMEDCAAPTable,
       "arrisRouterWMMEDCAAPEntry": arrisRouterWMMEDCAAPEntry,
       "arrisRouterWMMEDCAAPIndex": arrisRouterWMMEDCAAPIndex,
       "arrisRouterWMMEDCAAPCWmin": arrisRouterWMMEDCAAPCWmin,
       "arrisRouterWMMEDCAAPCWmax": arrisRouterWMMEDCAAPCWmax,
       "arrisRouterWMMEDCAAPAIFSN": arrisRouterWMMEDCAAPAIFSN,
       "arrisRouterWMMEDCAAPTxOpBLimit": arrisRouterWMMEDCAAPTxOpBLimit,
       "arrisRouterWMMEDCAAPTxOpAGLimit": arrisRouterWMMEDCAAPTxOpAGLimit,
       "arrisRouterWMMEDCAAPAdmitCont": arrisRouterWMMEDCAAPAdmitCont,
       "arrisRouterWMMEDCAAPDiscardOld": arrisRouterWMMEDCAAPDiscardOld,
       "arrisRouterWPSCfg": arrisRouterWPSCfg,
       "arrisRouterWpsMode": arrisRouterWpsMode,
       "arrisRouterWpsConfigState": arrisRouterWpsConfigState,
       "arrisRouterWpsDevicePIN": arrisRouterWpsDevicePIN,
       "arrisRouterWpsDeviceName": arrisRouterWpsDeviceName,
       "arrisRouterWpsModelName": arrisRouterWpsModelName,
       "arrisRouterWpsMfg": arrisRouterWpsMfg,
       "arrisRouterWpsResultStatus": arrisRouterWpsResultStatus,
       "arrisRouterWpsStatus": arrisRouterWpsStatus,
       "arrisRouterWpsConfigTimeout": arrisRouterWpsConfigTimeout,
       "arrisRouterWpsSTAPin": arrisRouterWpsSTAPin,
       "arrisRouterWpsPushButton": arrisRouterWpsPushButton,
       "arrisRouterWpsUUID": arrisRouterWpsUUID,
       "arrisRouterWPSMethodCfg": arrisRouterWPSMethodCfg,
       "arrisRouterWPSMethodLabel": arrisRouterWPSMethodLabel,
       "arrisRouterWPSMethodPIN": arrisRouterWPSMethodPIN,
       "arrisRouterWPSMethodPushButton": arrisRouterWPSMethodPushButton,
       "arrisRouterWPSMethodKeypad": arrisRouterWPSMethodKeypad,
       "arrisRouterWiFiResetDefaults": arrisRouterWiFiResetDefaults,
       "arrisRouterWiFiCustomSSIDStr": arrisRouterWiFiCustomSSIDStr,
       "arrisRouterWiFiRadioControlMode": arrisRouterWiFiRadioControlMode,
       "arrisRouterWiFiScan": arrisRouterWiFiScan,
       "arrisRouterWiFiStartScan": arrisRouterWiFiStartScan,
       "arrisRouterWiFiScanResult": arrisRouterWiFiScanResult,
       "arrisRouterWiFiScanResultTable": arrisRouterWiFiScanResultTable,
       "arrisRouterWiFiScanResultEntry": arrisRouterWiFiScanResultEntry,
       "arrisRouterWiFiScanIndex": arrisRouterWiFiScanIndex,
       "arrisRouterWiFiScanSSID": arrisRouterWiFiScanSSID,
       "arrisRouterWiFiScanChannel": arrisRouterWiFiScanChannel,
       "arrisRouterWiFiScanChannel2": arrisRouterWiFiScanChannel2,
       "arrisRouterWiFiScanRSSI": arrisRouterWiFiScanRSSI,
       "arrisRouterWiFiScanNoise": arrisRouterWiFiScanNoise,
       "arrisRouterWiFiScanMAC": arrisRouterWiFiScanMAC,
       "arrisRouterWiFiScanMfg": arrisRouterWiFiScanMfg,
       "arrisRouterWiFiScanSupportedRates": arrisRouterWiFiScanSupportedRates,
       "arrisRouterWiFiScanOperatingStandards": arrisRouterWiFiScanOperatingStandards,
       "arrisRouterWiFiScanSecurityModeEnabled": arrisRouterWiFiScanSecurityModeEnabled,
       "arrisRouterWiFiScanOperatingChannelBandwidth": arrisRouterWiFiScanOperatingChannelBandwidth,
       "arrisRouterWiFiClientInfoTable": arrisRouterWiFiClientInfoTable,
       "arrisRouterWiFiClientInfoEntry": arrisRouterWiFiClientInfoEntry,
       "arrisRouterWiFiClientInfoIndex": arrisRouterWiFiClientInfoIndex,
       "arrisRouterWiFiClientInfoIPAddrType": arrisRouterWiFiClientInfoIPAddrType,
       "arrisRouterWiFiClientInfoIPAddr": arrisRouterWiFiClientInfoIPAddr,
       "arrisRouterWiFiClientInfoIPAddrTextual": arrisRouterWiFiClientInfoIPAddrTextual,
       "arrisRouterWiFiClientInfoHostName": arrisRouterWiFiClientInfoHostName,
       "arrisRouterWiFiClientInfoMAC": arrisRouterWiFiClientInfoMAC,
       "arrisRouterWiFiClientInfoMACMfg": arrisRouterWiFiClientInfoMACMfg,
       "arrisRouterWiFiClientInfoStatus": arrisRouterWiFiClientInfoStatus,
       "arrisRouterWiFiClientInfoFirstSeen": arrisRouterWiFiClientInfoFirstSeen,
       "arrisRouterWiFiClientInfoLastSeen": arrisRouterWiFiClientInfoLastSeen,
       "arrisRouterWiFiClientInfoIdleTime": arrisRouterWiFiClientInfoIdleTime,
       "arrisRouterWiFiClientInfoInNetworkTime": arrisRouterWiFiClientInfoInNetworkTime,
       "arrisRouterWiFiClientInfoState": arrisRouterWiFiClientInfoState,
       "arrisRouterWiFiClientInfoFlags": arrisRouterWiFiClientInfoFlags,
       "arrisRouterWiFiClientInfoTxPkts": arrisRouterWiFiClientInfoTxPkts,
       "arrisRouterWiFiClientInfoTxFailures": arrisRouterWiFiClientInfoTxFailures,
       "arrisRouterWiFiClientInfoRxUnicastPkts": arrisRouterWiFiClientInfoRxUnicastPkts,
       "arrisRouterWiFiClientInfoRxMulticastPkts": arrisRouterWiFiClientInfoRxMulticastPkts,
       "arrisRouterWiFiClientInfoLastTxPktRate": arrisRouterWiFiClientInfoLastTxPktRate,
       "arrisRouterWiFiClientInfoLastRxPktRate": arrisRouterWiFiClientInfoLastRxPktRate,
       "arrisRouterWiFiClientInfoRateSet": arrisRouterWiFiClientInfoRateSet,
       "arrisRouterWiFiClientInfoRSSI": arrisRouterWiFiClientInfoRSSI,
       "arrisRouterWiFiPhysicalChannel": arrisRouterWiFiPhysicalChannel,
       "arrisRouterWiFi50RadioSettings": arrisRouterWiFi50RadioSettings,
       "arrisRouterWiFi50Channel": arrisRouterWiFi50Channel,
       "arrisRouterWiFi50Mode": arrisRouterWiFi50Mode,
       "arrisRouterWiFi50BeaconInterval": arrisRouterWiFi50BeaconInterval,
       "arrisRouterWiFi50DTIMInterval": arrisRouterWiFi50DTIMInterval,
       "arrisRouterWiFi50TxPreamble": arrisRouterWiFi50TxPreamble,
       "arrisRouterWiFi50RTSThreshold": arrisRouterWiFi50RTSThreshold,
       "arrisRouterWiFi50FragmentThresh": arrisRouterWiFi50FragmentThresh,
       "arrisRouterWiFi50ShortSlot": arrisRouterWiFi50ShortSlot,
       "arrisRouterWiFi50FrameBurst": arrisRouterWiFi50FrameBurst,
       "arrisRouterWiFi50EnableRadio": arrisRouterWiFi50EnableRadio,
       "arrisRouterWiFi50ShortRetryLimit": arrisRouterWiFi50ShortRetryLimit,
       "arrisRouterWiFi50LongRetryLimit": arrisRouterWiFi50LongRetryLimit,
       "arrisRouterWiFi50OutputPower": arrisRouterWiFi50OutputPower,
       "arrisRouterWiFi50MulticastA": arrisRouterWiFi50MulticastA,
       "arrisRouterWiFi50PhysicalChannel": arrisRouterWiFi50PhysicalChannel,
       "arrisRouterWiFi50NSettings": arrisRouterWiFi50NSettings,
       "arrisRouterWiFi50HTMCS": arrisRouterWiFi50HTMCS,
       "arrisRouterWiFi50ChannelBW": arrisRouterWiFi50ChannelBW,
       "arrisRouterWiFi50NSideBand": arrisRouterWiFi50NSideBand,
       "arrisRouterWiFi50HTMode": arrisRouterWiFi50HTMode,
       "arrisRouterWiFi50GuardInterval": arrisRouterWiFi50GuardInterval,
       "arrisRouterWiFi50AMSDUEnable": arrisRouterWiFi50AMSDUEnable,
       "arrisRouterWiFi50DeclinePeerBA": arrisRouterWiFi50DeclinePeerBA,
       "arrisRouterWiFi50BlockAck": arrisRouterWiFi50BlockAck,
       "arrisRouterWiFi50NProtection": arrisRouterWiFi50NProtection,
       "arrisRouterWiFi50HTTxStream": arrisRouterWiFi50HTTxStream,
       "arrisRouterWiFi50HTRxStream": arrisRouterWiFi50HTRxStream,
       "arrisRouterWiFi50EnableSTBC": arrisRouterWiFi50EnableSTBC,
       "arrisRouterWiFi50EnableRDG": arrisRouterWiFi50EnableRDG,
       "arrisRouterWiFi50IGMPSnooping": arrisRouterWiFi50IGMPSnooping,
       "arrisRouterWiFi50BlockDFSChan": arrisRouterWiFi50BlockDFSChan,
       "arrisRouterWiFi50RTSRetry": arrisRouterWiFi50RTSRetry,
       "arrisRouterWiFi50TxRetry": arrisRouterWiFi50TxRetry,
       "arrisRouterWiFiNumSSIDSupported": arrisRouterWiFiNumSSIDSupported,
       "arrisRouterWiFiHTTxStream": arrisRouterWiFiHTTxStream,
       "arrisRouterWiFiHTRxStream": arrisRouterWiFiHTRxStream,
       "arrisRouterWiFiEnableSTBC": arrisRouterWiFiEnableSTBC,
       "arrisRouterWiFiEnableRDG": arrisRouterWiFiEnableRDG,
       "arrisRouterWiFiIGMPSnooping": arrisRouterWiFiIGMPSnooping,
       "arrisRouterWiFiRTSRetry": arrisRouterWiFiRTSRetry,
       "arrisRouterWiFiTxRetry": arrisRouterWiFiTxRetry,
       "arrisRouterWiFiPhysicalChannelStats": arrisRouterWiFiPhysicalChannelStats,
       "arrisRouterWiFiPhysicalChannelStatsEnable": arrisRouterWiFiPhysicalChannelStatsEnable,
       "arrisRouterWiFiPhysicalChannelStatsMeasurementRate": arrisRouterWiFiPhysicalChannelStatsMeasurementRate,
       "arrisRouterWiFiPhysicalChannelStatsMeasurementInterval": arrisRouterWiFiPhysicalChannelStatsMeasurementInterval,
       "arrisRouterChannelStatsMeasurementTable": arrisRouterChannelStatsMeasurementTable,
       "arrisRouterChannelStatsMeasurementEntry": arrisRouterChannelStatsMeasurementEntry,
       "arrisRouterChannelStatsMinNoiseFloor": arrisRouterChannelStatsMinNoiseFloor,
       "arrisRouterChannelStatsMaxNoiseFloor": arrisRouterChannelStatsMaxNoiseFloor,
       "arrisRouterChannelStatsMedianNoiseFloor": arrisRouterChannelStatsMedianNoiseFloor,
       "arrisRouterChannelStatsPacketsSent": arrisRouterChannelStatsPacketsSent,
       "arrisRouterChannelStatsPacketsReceived": arrisRouterChannelStatsPacketsReceived,
       "arrisRouterChannelStatsCSTExceedPercent": arrisRouterChannelStatsCSTExceedPercent,
       "arrisRouterChannelStatsActivityFactor": arrisRouterChannelStatsActivityFactor,
       "arrisRouterChannelStatsChannelUtilization": arrisRouterChannelStatsChannelUtilization,
       "arrisRouterChannelStatsRetransmissionsMetric": arrisRouterChannelStatsRetransmissionsMetric,
       "arrisRouterChannelStatsRSSITable": arrisRouterChannelStatsRSSITable,
       "arrisRouterChannelStatsRSSITableEntry": arrisRouterChannelStatsRSSITableEntry,
       "arrisRouterChannelStatsRSSITableIndex": arrisRouterChannelStatsRSSITableIndex,
       "arrisRouterChannelStatsRSSICount": arrisRouterChannelStatsRSSICount,
       "arrisRouterWMM50Cfg": arrisRouterWMM50Cfg,
       "arrisRouterWMM50Enable": arrisRouterWMM50Enable,
       "arrisRouterWMM50NoAck": arrisRouterWMM50NoAck,
       "arrisRouterWMM50APSD": arrisRouterWMM50APSD,
       "arrisRouterWMM50EDCAAPTable": arrisRouterWMM50EDCAAPTable,
       "arrisRouterWMM50EDCAAPEntry": arrisRouterWMM50EDCAAPEntry,
       "arrisRouterWMM50EDCAAPIndex": arrisRouterWMM50EDCAAPIndex,
       "arrisRouterWMM50EDCAAPCWmin": arrisRouterWMM50EDCAAPCWmin,
       "arrisRouterWMM50EDCAAPCWmax": arrisRouterWMM50EDCAAPCWmax,
       "arrisRouterWMM50EDCAAPAIFSN": arrisRouterWMM50EDCAAPAIFSN,
       "arrisRouterWMM50EDCAAPTxOpBLimit": arrisRouterWMM50EDCAAPTxOpBLimit,
       "arrisRouterWMM50EDCAAPTxOpAGLimit": arrisRouterWMM50EDCAAPTxOpAGLimit,
       "arrisRouterWMM50EDCAAPAdmitCont": arrisRouterWMM50EDCAAPAdmitCont,
       "arrisRouterWMM50EDCAAPDiscardOld": arrisRouterWMM50EDCAAPDiscardOld,
       "arrisRouterWiFiExtensionChannel": arrisRouterWiFiExtensionChannel,
       "arrisRouterWPS50Cfg": arrisRouterWPS50Cfg,
       "arrisRouterWps50Mode": arrisRouterWps50Mode,
       "arrisRouterWps50ConfigState": arrisRouterWps50ConfigState,
       "arrisRouterWps50DevicePIN": arrisRouterWps50DevicePIN,
       "arrisRouterWps50DeviceName": arrisRouterWps50DeviceName,
       "arrisRouterWps50ModelName": arrisRouterWps50ModelName,
       "arrisRouterWps50Mfg": arrisRouterWps50Mfg,
       "arrisRouterWps50ResultStatus": arrisRouterWps50ResultStatus,
       "arrisRouterWps50Status": arrisRouterWps50Status,
       "arrisRouterWps50ConfigTimeout": arrisRouterWps50ConfigTimeout,
       "arrisRouterWps50STAPin": arrisRouterWps50STAPin,
       "arrisRouterWps50PushButton": arrisRouterWps50PushButton,
       "arrisRouterWps50UUID": arrisRouterWps50UUID,
       "arrisRouterWifiLowInitRate": arrisRouterWifiLowInitRate,
       "arrisRouterWiFiBssStaSteering": arrisRouterWiFiBssStaSteering,
       "arrisRouterWiFiBssStaSteeringReset": arrisRouterWiFiBssStaSteeringReset,
       "arrisRouterWiFiBssStaSteeringDenyCount": arrisRouterWiFiBssStaSteeringDenyCount,
       "arrisRouterWiFiBssStaSteeringDenyWindow": arrisRouterWiFiBssStaSteeringDenyWindow,
       "arrisRouterBssStaSteeringTable": arrisRouterBssStaSteeringTable,
       "arrisRouterBssStaSteeringEntry": arrisRouterBssStaSteeringEntry,
       "arrisRouterBssStaSteeringIndex": arrisRouterBssStaSteeringIndex,
       "arrisRouterBssStaSteeringTableClear": arrisRouterBssStaSteeringTableClear,
       "arrisRouterBssStaSteeringTableDenyCount": arrisRouterBssStaSteeringTableDenyCount,
       "arrisRouterBssStaSteeringTableDenyWindow": arrisRouterBssStaSteeringTableDenyWindow,
       "arrisRouterBssStaSteeringTableStatus": arrisRouterBssStaSteeringTableStatus,
       "arrisRouterBssStaSteeringClientTable": arrisRouterBssStaSteeringClientTable,
       "arrisRouterBssStaSteeringClientEntry": arrisRouterBssStaSteeringClientEntry,
       "arrisRouterBssStaSteeringClientIndex": arrisRouterBssStaSteeringClientIndex,
       "arrisRouterBssStaSteeringClientMacAddress": arrisRouterBssStaSteeringClientMacAddress,
       "arrisRouterBssStaSteeringClientLastAssocTime": arrisRouterBssStaSteeringClientLastAssocTime,
       "arrisRouterBssStaSteeringClientOtherBssJoinedCount": arrisRouterBssStaSteeringClientOtherBssJoinedCount,
       "arrisRouterWiFiInterworkingIE": arrisRouterWiFiInterworkingIE,
       "arrisRouterAirtimeCtrlCfg": arrisRouterAirtimeCtrlCfg,
       "arrisRouterAirtimeCtrlBSSIDEnable": arrisRouterAirtimeCtrlBSSIDEnable,
       "arrisRouterAirtimeCtrlBSSIDWeightTable": arrisRouterAirtimeCtrlBSSIDWeightTable,
       "arrisRouterAirtimeCtrlBSSIDWeightEntry": arrisRouterAirtimeCtrlBSSIDWeightEntry,
       "arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage": arrisRouterAirtimeCtrlBSSIDWeightGuaranteedPercentage,
       "arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage": arrisRouterAirtimeCtrlBSSIDWeightMaximumPercentage,
       "arrisRouterFWCfg": arrisRouterFWCfg,
       "arrisRouterFWEnabled": arrisRouterFWEnabled,
       "arrisRouterFWEnableDMZ": arrisRouterFWEnableDMZ,
       "arrisRouterFWIPAddrTypeDMZ": arrisRouterFWIPAddrTypeDMZ,
       "arrisRouterFWIPAddrDMZ": arrisRouterFWIPAddrDMZ,
       "arrisRouterFWSecurityLevel": arrisRouterFWSecurityLevel,
       "arrisRouterFWVirtSrvTable": arrisRouterFWVirtSrvTable,
       "arrisRouterFWVirtSrvEntry": arrisRouterFWVirtSrvEntry,
       "arrisRouterFWVirtSrvIndex": arrisRouterFWVirtSrvIndex,
       "arrisRouterFWVirtSrvDesc": arrisRouterFWVirtSrvDesc,
       "arrisRouterFWVirtSrvPortStart": arrisRouterFWVirtSrvPortStart,
       "arrisRouterFWVirtSrvPortEnd": arrisRouterFWVirtSrvPortEnd,
       "arrisRouterFWVirtSrvProtoType": arrisRouterFWVirtSrvProtoType,
       "arrisRouterFWVirtSrvIPAddrType": arrisRouterFWVirtSrvIPAddrType,
       "arrisRouterFWVirtSrvIPAddr": arrisRouterFWVirtSrvIPAddr,
       "arrisRouterFWVirtSrvLocalPortStart": arrisRouterFWVirtSrvLocalPortStart,
       "arrisRouterFWVirtSrvLocalPortEnd": arrisRouterFWVirtSrvLocalPortEnd,
       "arrisRouterFWVirtSrvRowStatus": arrisRouterFWVirtSrvRowStatus,
       "arrisRouterFWSrvTr69InstanceID": arrisRouterFWSrvTr69InstanceID,
       "arrisRouterFWIPFilterTable": arrisRouterFWIPFilterTable,
       "arrisRouterFWIPFilterEntry": arrisRouterFWIPFilterEntry,
       "arrisRouterFWIPFilterIndex": arrisRouterFWIPFilterIndex,
       "arrisRouterFWIPFilterDesc": arrisRouterFWIPFilterDesc,
       "arrisRouterFWIPFilterStartType": arrisRouterFWIPFilterStartType,
       "arrisRouterFWIPFilterStartAddr": arrisRouterFWIPFilterStartAddr,
       "arrisRouterFWIPFilterEndType": arrisRouterFWIPFilterEndType,
       "arrisRouterFWIPFilterEndAddr": arrisRouterFWIPFilterEndAddr,
       "arrisRouterFWIPFilterPortStart": arrisRouterFWIPFilterPortStart,
       "arrisRouterFWIPFilterPortEnd": arrisRouterFWIPFilterPortEnd,
       "arrisRouterFWIPFilterProtoType": arrisRouterFWIPFilterProtoType,
       "arrisRouterFWIPFilterTOD": arrisRouterFWIPFilterTOD,
       "arrisRouterFWIPFilterRowStatus": arrisRouterFWIPFilterRowStatus,
       "arrisRouterFWIPFilterAction": arrisRouterFWIPFilterAction,
       "arrisRouterFWIPFilterDirection": arrisRouterFWIPFilterDirection,
       "arrisRouterFWAllowAll": arrisRouterFWAllowAll,
       "arrisRouterFWMACFilterTable": arrisRouterFWMACFilterTable,
       "arrisRouterFWMACFilterEntry": arrisRouterFWMACFilterEntry,
       "arrisRouterFWMACFilterIndex": arrisRouterFWMACFilterIndex,
       "arrisRouterFWMACFilterAddr": arrisRouterFWMACFilterAddr,
       "arrisRouterFWMACFilterTOD": arrisRouterFWMACFilterTOD,
       "arrisRouterFWMACFilterRowStatus": arrisRouterFWMACFilterRowStatus,
       "arrisRouterFWPortTrigTable": arrisRouterFWPortTrigTable,
       "arrisRouterFWPortTrigEntry": arrisRouterFWPortTrigEntry,
       "arrisRouterFWPortTrigIndex": arrisRouterFWPortTrigIndex,
       "arrisRouterFWPortTrigDesc": arrisRouterFWPortTrigDesc,
       "arrisRouterFWPortTrigPortStart": arrisRouterFWPortTrigPortStart,
       "arrisRouterFWPortTrigPortEnd": arrisRouterFWPortTrigPortEnd,
       "arrisRouterFWPortTargPortStart": arrisRouterFWPortTargPortStart,
       "arrisRouterFWPortTargPortEnd": arrisRouterFWPortTargPortEnd,
       "arrisRouterFWPortTrigProtoType": arrisRouterFWPortTrigProtoType,
       "arrisRouterFWPortTrigRowStatus": arrisRouterFWPortTrigRowStatus,
       "arrisRouterFWFilterRules": arrisRouterFWFilterRules,
       "arrisRouterFWBlockFragIPPkts": arrisRouterFWBlockFragIPPkts,
       "arrisRouterFWPortScanProtect": arrisRouterFWPortScanProtect,
       "arrisRouterFWIPFloodDetect": arrisRouterFWIPFloodDetect,
       "arrisRouterFWBlockFragIPPktsV4": arrisRouterFWBlockFragIPPktsV4,
       "arrisRouterFWPortScanProtectV4": arrisRouterFWPortScanProtectV4,
       "arrisRouterFWIPFloodDetectV4": arrisRouterFWIPFloodDetectV4,
       "arrisRouterFWBlockFragIPPktsV6": arrisRouterFWBlockFragIPPktsV6,
       "arrisRouterFWPortScanProtectV6": arrisRouterFWPortScanProtectV6,
       "arrisRouterFWIPFloodDetectV6": arrisRouterFWIPFloodDetectV6,
       "arrisRouterFWDDNSObjs": arrisRouterFWDDNSObjs,
       "arrisRouterFWDDNSEnable": arrisRouterFWDDNSEnable,
       "arrisRouterFWDDNSType": arrisRouterFWDDNSType,
       "arrisRouterFWDDNSUserName": arrisRouterFWDDNSUserName,
       "arrisRouterFWDDNSPassword": arrisRouterFWDDNSPassword,
       "arrisRouterFWDDNSDomainName": arrisRouterFWDDNSDomainName,
       "arrisRouterFWDDNSIPAddrType": arrisRouterFWDDNSIPAddrType,
       "arrisRouterFWDDNSIPAddr": arrisRouterFWDDNSIPAddr,
       "arrisRouterFWDDNSStatus": arrisRouterFWDDNSStatus,
       "arrisRouterFWFeatures": arrisRouterFWFeatures,
       "arrisRouterFWIPSecPassThru": arrisRouterFWIPSecPassThru,
       "arrisRouterFWPPTPPassThru": arrisRouterFWPPTPPassThru,
       "arrisRouterFWEnableMulticast": arrisRouterFWEnableMulticast,
       "arrisRouterFWEnableRemoteMgmt": arrisRouterFWEnableRemoteMgmt,
       "arrisRouterFWL2TPPassThru": arrisRouterFWL2TPPassThru,
       "arrisRouterFWRemoteMgmt": arrisRouterFWRemoteMgmt,
       "arrisRouterFWRemoteMgmtHttp": arrisRouterFWRemoteMgmtHttp,
       "arrisRouterFWRemoteMgmtHttps": arrisRouterFWRemoteMgmtHttps,
       "arrisRouterFWRemoteMgmtHttpPort": arrisRouterFWRemoteMgmtHttpPort,
       "arrisRouterFWRemoteMgmtHttpsPort": arrisRouterFWRemoteMgmtHttpsPort,
       "arrisRouterFWRemoteMgmtAllowedType": arrisRouterFWRemoteMgmtAllowedType,
       "arrisRouterFWRemoteMgmtAllowedIPv4": arrisRouterFWRemoteMgmtAllowedIPv4,
       "arrisRouterFWRemoteMgmtAllowedIPv6": arrisRouterFWRemoteMgmtAllowedIPv6,
       "arrisRouterFWRemoteMgmtAllowedStartIPv4": arrisRouterFWRemoteMgmtAllowedStartIPv4,
       "arrisRouterFWRemoteMgmtAllowedEndIPv4": arrisRouterFWRemoteMgmtAllowedEndIPv4,
       "arrisRouterFWRemoteMgmtAllowedStartIPv6": arrisRouterFWRemoteMgmtAllowedStartIPv6,
       "arrisRouterFWRemoteMgmtAllowedEndIPv6": arrisRouterFWRemoteMgmtAllowedEndIPv6,
       "arrisRouterFWRemoteMgmtTelnet": arrisRouterFWRemoteMgmtTelnet,
       "arrisRouterFWSelectRemoteMgmt": arrisRouterFWSelectRemoteMgmt,
       "arrisRouterFWParentalControls": arrisRouterFWParentalControls,
       "arrisRouterKeywordCount": arrisRouterKeywordCount,
       "arrisRouterBlackListCount": arrisRouterBlackListCount,
       "arrisRouterWhiteListCount": arrisRouterWhiteListCount,
       "arrisRouterKeywordBlkTable": arrisRouterKeywordBlkTable,
       "arrisRouterKeywordBlkEntry": arrisRouterKeywordBlkEntry,
       "arrisRouterKeywordBlkIndex": arrisRouterKeywordBlkIndex,
       "arrisRouterKeywordBlkWord": arrisRouterKeywordBlkWord,
       "arrisRouterKeywordBlkTOD": arrisRouterKeywordBlkTOD,
       "arrisRouterKeywordBlkStatus": arrisRouterKeywordBlkStatus,
       "arrisRouterBlackListTable": arrisRouterBlackListTable,
       "arrisRouterBlackListEntry": arrisRouterBlackListEntry,
       "arrisRouterBlackListIndex": arrisRouterBlackListIndex,
       "arrisRouterBlackListDomain": arrisRouterBlackListDomain,
       "arrisRouterBlackListTOD": arrisRouterBlackListTOD,
       "arrisRouterBlackListStatus": arrisRouterBlackListStatus,
       "arrisRouterWhiteListTable": arrisRouterWhiteListTable,
       "arrisRouterWhiteListEntry": arrisRouterWhiteListEntry,
       "arrisRouterWhiteListIndex": arrisRouterWhiteListIndex,
       "arrisRouterWhiteListDomain": arrisRouterWhiteListDomain,
       "arrisRouterWhiteListTOD": arrisRouterWhiteListTOD,
       "arrisRouterWhiteListStatus": arrisRouterWhiteListStatus,
       "arrisRouterTrustedDeviceTable": arrisRouterTrustedDeviceTable,
       "arrisRouterTrustedDeviceEntry": arrisRouterTrustedDeviceEntry,
       "arrisRouterTrustedDeviceIndex": arrisRouterTrustedDeviceIndex,
       "arrisRouterTrustedDeviceMAC": arrisRouterTrustedDeviceMAC,
       "arrisRouterTrustedDeviceStatus": arrisRouterTrustedDeviceStatus,
       "arrisRouterTrustedDeviceName": arrisRouterTrustedDeviceName,
       "arrisRouterTrustedDeviceAddrType": arrisRouterTrustedDeviceAddrType,
       "arrisRouterTrustedDeviceAddr": arrisRouterTrustedDeviceAddr,
       "arrisRouterEnableParentalCont": arrisRouterEnableParentalCont,
       "arrisRouterListActiveType": arrisRouterListActiveType,
       "arrisRouterExceptionListCount": arrisRouterExceptionListCount,
       "arrisRouterExceptionListTable": arrisRouterExceptionListTable,
       "arrisRouterExceptionListEntry": arrisRouterExceptionListEntry,
       "arrisRouterExceptionListIndex": arrisRouterExceptionListIndex,
       "arrisRouterExceptionListDomain": arrisRouterExceptionListDomain,
       "arrisRouterExceptionListStatus": arrisRouterExceptionListStatus,
       "arrisRouterFWAllowICMP": arrisRouterFWAllowICMP,
       "arrisRouterFWVirtSrvTableEnabled": arrisRouterFWVirtSrvTableEnabled,
       "arrisRouterFWPortTrigTableEnabled": arrisRouterFWPortTrigTableEnabled,
       "arrisRouterFWIPv6Security": arrisRouterFWIPv6Security,
       "arrisRouterFWIPv6Enable": arrisRouterFWIPv6Enable,
       "arrisRouterFWMacBridgingWebPageEnabled": arrisRouterFWMacBridgingWebPageEnabled,
       "arrisRouterFWMacBridgingFunctionEnabled": arrisRouterFWMacBridgingFunctionEnabled,
       "arrisRouterFWMacBridgingTable": arrisRouterFWMacBridgingTable,
       "arrisRouterFWMacBridgingEntry": arrisRouterFWMacBridgingEntry,
       "arrisRouterFWMacBridgingIndex": arrisRouterFWMacBridgingIndex,
       "arrisRouterFWMacBridgingName": arrisRouterFWMacBridgingName,
       "arrisRouterFWMacBridgingMACAddr": arrisRouterFWMacBridgingMACAddr,
       "arrisRouterFWMacBridgingRowStatus": arrisRouterFWMacBridgingRowStatus,
       "arrisRouterFWPortAllowTable": arrisRouterFWPortAllowTable,
       "arrisRouterFWPortAllowEntry": arrisRouterFWPortAllowEntry,
       "arrisRouterFWPortAllowIndex": arrisRouterFWPortAllowIndex,
       "arrisRouterFWPortAllowInboundPort": arrisRouterFWPortAllowInboundPort,
       "arrisRouterFWPortAllowRowStatus": arrisRouterFWPortAllowRowStatus,
       "arrisRouterFWSrvTr69LastInstance": arrisRouterFWSrvTr69LastInstance,
       "arrisRouterSysCfg": arrisRouterSysCfg,
       "arrisRouterAdminPassword": arrisRouterAdminPassword,
       "arrisRouterAdminTimeout": arrisRouterAdminTimeout,
       "arrisRouterTimeZoneUTCOffset": arrisRouterTimeZoneUTCOffset,
       "arrisRouterReboot": arrisRouterReboot,
       "arrisRouterDefaults": arrisRouterDefaults,
       "arrisRouterLanguage": arrisRouterLanguage,
       "arrisRouterName": arrisRouterName,
       "arrisRouterSerialNumber": arrisRouterSerialNumber,
       "arrisRouterBootCodeVersion": arrisRouterBootCodeVersion,
       "arrisRouterHardwareVersion": arrisRouterHardwareVersion,
       "arrisRouterFirmwareVersion": arrisRouterFirmwareVersion,
       "arrisRouterLogLevel": arrisRouterLogLevel,
       "arrisRouterCustomSettings": arrisRouterCustomSettings,
       "arrisRouterCustomID": arrisRouterCustomID,
       "arrisRouterCurrentTime": arrisRouterCurrentTime,
       "arrisRouterAuthTable": arrisRouterAuthTable,
       "arrisRouterAuthEntry": arrisRouterAuthEntry,
       "arrisRouterAuthIndex": arrisRouterAuthIndex,
       "arrisRouterAuthUserName": arrisRouterAuthUserName,
       "arrisRouterAuthPassword": arrisRouterAuthPassword,
       "arrisRouterAuthType": arrisRouterAuthType,
       "arrisRouterAuthAccountEnabled": arrisRouterAuthAccountEnabled,
       "arrisRouterSNTPSettings": arrisRouterSNTPSettings,
       "arrisRouterEnableSNTP": arrisRouterEnableSNTP,
       "arrisRouterSNTPServerTable": arrisRouterSNTPServerTable,
       "arrisRouterSNTPServerEntry": arrisRouterSNTPServerEntry,
       "arrisRouterSNTPServerIndex": arrisRouterSNTPServerIndex,
       "arrisRouterSNTPServerAddrType": arrisRouterSNTPServerAddrType,
       "arrisRouterSNTPServerAddr": arrisRouterSNTPServerAddr,
       "arrisRouterSNTPServerName": arrisRouterSNTPServerName,
       "arrisRouterSNTPServerStatus": arrisRouterSNTPServerStatus,
       "arrisRouterEmailSettings": arrisRouterEmailSettings,
       "arrisRouterEmailServerName": arrisRouterEmailServerName,
       "arrisRouterEmailServerUser": arrisRouterEmailServerUser,
       "arrisRouterEmailServerPW": arrisRouterEmailServerPW,
       "arrisRouterEmailAddress": arrisRouterEmailAddress,
       "arrisRouterEnableLogEmail": arrisRouterEnableLogEmail,
       "arrisRouterEmailApplySettings": arrisRouterEmailApplySettings,
       "arrisRouterEmailSenderAddress": arrisRouterEmailSenderAddress,
       "arrisRouterEmailSend": arrisRouterEmailSend,
       "arrisRouterLogSettings": arrisRouterLogSettings,
       "arrisRouterUserLogs": arrisRouterUserLogs,
       "arrisRouterFirewallLogTable": arrisRouterFirewallLogTable,
       "arrisRouterFirewallLogEntry": arrisRouterFirewallLogEntry,
       "arrisRouterFWLogIndex": arrisRouterFWLogIndex,
       "arrisRouterFWLogTime": arrisRouterFWLogTime,
       "arrisRouterFWLogInfo": arrisRouterFWLogInfo,
       "arrisRouterParentalContLogTable": arrisRouterParentalContLogTable,
       "arrisRouterParentalContLogEntry": arrisRouterParentalContLogEntry,
       "arrisRouterPCLogIndex": arrisRouterPCLogIndex,
       "arrisRouterPCLogTime": arrisRouterPCLogTime,
       "arrisRouterPCLogInfo": arrisRouterPCLogInfo,
       "arrisRouterPCLogType": arrisRouterPCLogType,
       "arrisRouterChangeLogTable": arrisRouterChangeLogTable,
       "arrisRouterChangeLogEntry": arrisRouterChangeLogEntry,
       "arrisRouterChangeLogIndex": arrisRouterChangeLogIndex,
       "arrisRouterChangeLogTime": arrisRouterChangeLogTime,
       "arrisRouterChangeLogInfo": arrisRouterChangeLogInfo,
       "arrisRouterDebugLogTable": arrisRouterDebugLogTable,
       "arrisRouterDebugLogEntry": arrisRouterDebugLogEntry,
       "arrisRouterDebugLogIndex": arrisRouterDebugLogIndex,
       "arrisRouterDebugLogTime": arrisRouterDebugLogTime,
       "arrisRouterDebugLogInfo": arrisRouterDebugLogInfo,
       "arrisRouterFirewallLogExtTable": arrisRouterFirewallLogExtTable,
       "arrisRouterFirewallLogExtEntry": arrisRouterFirewallLogExtEntry,
       "arrisRouterFWLogExtIndex": arrisRouterFWLogExtIndex,
       "arrisRouterFWLogLatestEventTime": arrisRouterFWLogLatestEventTime,
       "arrisRouterFWLogLatestEventInfo": arrisRouterFWLogLatestEventInfo,
       "arrisRouterFWLogEventCount": arrisRouterFWLogEventCount,
       "arrisRouterMSOLogs": arrisRouterMSOLogs,
       "arrisRouterMSOChgLogTable": arrisRouterMSOChgLogTable,
       "arrisRouterMSOChgLogEntry": arrisRouterMSOChgLogEntry,
       "arrisRouterMSOChgLogIndex": arrisRouterMSOChgLogIndex,
       "arrisRouterMSOChgLogTime": arrisRouterMSOChgLogTime,
       "arrisRouterMSOChgLogInfo": arrisRouterMSOChgLogInfo,
       "arrisRouterClearMSOLogs": arrisRouterClearMSOLogs,
       "arrisRouterClearLogs": arrisRouterClearLogs,
       "arrisRouterTACACSAddr": arrisRouterTACACSAddr,
       "arrisRouterTACACSPort": arrisRouterTACACSPort,
       "arrisRouterTACACSSecretKey": arrisRouterTACACSSecretKey,
       "arrisRouterXmlProvisioningFile": arrisRouterXmlProvisioningFile,
       "arrisRouterXmlProvisioningStatus": arrisRouterXmlProvisioningStatus,
       "arrisRouterInboundTrafficLogEnable": arrisRouterInboundTrafficLogEnable,
       "arrisRouterInboundTrafficLogTable": arrisRouterInboundTrafficLogTable,
       "arrisRouterInboundTrafficLogEntry": arrisRouterInboundTrafficLogEntry,
       "arrisRouterInboundTrafficLogIndex": arrisRouterInboundTrafficLogIndex,
       "arrisRouterInboundTrafficLogData": arrisRouterInboundTrafficLogData,
       "arrisRouterWirelessBand": arrisRouterWirelessBand,
       "arrisRouterSaveCurrentConfigFile": arrisRouterSaveCurrentConfigFile,
       "arrisRouterRestoreCurrentConfigFile": arrisRouterRestoreCurrentConfigFile,
       "arrisRouterLocalPosixTimeZone": arrisRouterLocalPosixTimeZone,
       "arrisRouterFirstInstallWizardCompletionStatus": arrisRouterFirstInstallWizardCompletionStatus,
       "arrisRouterTroubleshooterEnable": arrisRouterTroubleshooterEnable,
       "arrisRouterCSRActiveTimeout": arrisRouterCSRActiveTimeout,
       "arrisRouterHostAccess": arrisRouterHostAccess,
       "arrisRouterWebAccessTable": arrisRouterWebAccessTable,
       "arrisRouterWebAccessEntry": arrisRouterWebAccessEntry,
       "arrisRouterWebAccessIndex": arrisRouterWebAccessIndex,
       "arrisRouterWebAccessPage": arrisRouterWebAccessPage,
       "arrisRouterWebAccessLevel": arrisRouterWebAccessLevel,
       "arrisRouterWebAccessRowStatus": arrisRouterWebAccessRowStatus,
       "arrisRouterWebAccessWANACL": arrisRouterWebAccessWANACL,
       "arrisRouterPingMgmt": arrisRouterPingMgmt,
       "arrisRouterPingTargetAddrType": arrisRouterPingTargetAddrType,
       "arrisRouterPingTargetAddress": arrisRouterPingTargetAddress,
       "arrisRouterPingNumPkts": arrisRouterPingNumPkts,
       "arrisRouterPingPktSize": arrisRouterPingPktSize,
       "arrisRouterPingInterval": arrisRouterPingInterval,
       "arrisRouterPingTimeout": arrisRouterPingTimeout,
       "arrisRouterPingVerifyReply": arrisRouterPingVerifyReply,
       "arrisRouterPingIpStackNumber": arrisRouterPingIpStackNumber,
       "arrisRouterPingStartStop": arrisRouterPingStartStop,
       "arrisRouterPingPktsSent": arrisRouterPingPktsSent,
       "arrisRouterPingRepliesReceived": arrisRouterPingRepliesReceived,
       "arrisRouterPingRepliesVerified": arrisRouterPingRepliesVerified,
       "arrisRouterPingOctetsSent": arrisRouterPingOctetsSent,
       "arrisRouterPingOctetsReceived": arrisRouterPingOctetsReceived,
       "arrisRouterPingIcmpErrors": arrisRouterPingIcmpErrors,
       "arrisRouterPingLastIcmpError": arrisRouterPingLastIcmpError,
       "arrisRouterPingAverageRtt": arrisRouterPingAverageRtt,
       "arrisRouterPingMinRtt": arrisRouterPingMinRtt,
       "arrisRouterPingMaxRtt": arrisRouterPingMaxRtt,
       "arrisRouterPingTargetDNSQueryIPAddrType": arrisRouterPingTargetDNSQueryIPAddrType,
       "arrisRouterPingLog": arrisRouterPingLog,
       "arrisRouterTraceRtMgmt": arrisRouterTraceRtMgmt,
       "arrisRouterTraceRtTargAddrType": arrisRouterTraceRtTargAddrType,
       "arrisRouterTraceRtTargetAddr": arrisRouterTraceRtTargetAddr,
       "arrisRouterTraceRtMaxHops": arrisRouterTraceRtMaxHops,
       "arrisRouterTraceRtDataSize": arrisRouterTraceRtDataSize,
       "arrisRouterTraceRtResolveHosts": arrisRouterTraceRtResolveHosts,
       "arrisRouterTraceRtBasePort": arrisRouterTraceRtBasePort,
       "arrisRouterTraceRtStart": arrisRouterTraceRtStart,
       "arrisRouterTraceRtLog": arrisRouterTraceRtLog,
       "arrisRouterTraceRtTimeout": arrisRouterTraceRtTimeout,
       "arrisRouterTraceRtDiffServ": arrisRouterTraceRtDiffServ,
       "arrisRouterApplyAllSettings": arrisRouterApplyAllSettings,
       "arrisRouterICtrl": arrisRouterICtrl,
       "arrisRouterICtrlPortMapCount": arrisRouterICtrlPortMapCount,
       "arrisRouterICtrlPortMapTable": arrisRouterICtrlPortMapTable,
       "arrisRouterICtrlPortMapEntry": arrisRouterICtrlPortMapEntry,
       "arrisRouterICtrlPortMapIndex": arrisRouterICtrlPortMapIndex,
       "arrisRouterPortMapDescription": arrisRouterPortMapDescription,
       "arrisRouterPortMapInternalClientAddrType": arrisRouterPortMapInternalClientAddrType,
       "arrisRouterPortMapInternalClientAddr": arrisRouterPortMapInternalClientAddr,
       "arrisRouterPortMapProtocol": arrisRouterPortMapProtocol,
       "arrisRouterPortMapExternalPort": arrisRouterPortMapExternalPort,
       "arrisRouterPortMapInternalPort": arrisRouterPortMapInternalPort,
       "arrisRouterPortMapRowStatus": arrisRouterPortMapRowStatus,
       "arrisRouterPortMapInternalStartPort": arrisRouterPortMapInternalStartPort,
       "arrisRouterPortMapInternalEndPort": arrisRouterPortMapInternalEndPort,
       "arrisRouterPortMapExternalStartPort": arrisRouterPortMapExternalStartPort,
       "arrisRouterPortMapExternalEndPort": arrisRouterPortMapExternalEndPort,
       "arrisRouterICtrlGetDeviceSettings": arrisRouterICtrlGetDeviceSettings,
       "arrisRouterICtrlDeviceSettingsFWversion": arrisRouterICtrlDeviceSettingsFWversion,
       "arrisRouterICtrlIsDeviceReady": arrisRouterICtrlIsDeviceReady,
       "arrisRouterICtrlDeviceStatus": arrisRouterICtrlDeviceStatus,
       "arrisRouterICtrlReboot": arrisRouterICtrlReboot,
       "arrisRouterICtrlInitiateReboot": arrisRouterICtrlInitiateReboot,
       "arrisRouterICtrlSetDeviceSettings": arrisRouterICtrlSetDeviceSettings,
       "arrisRouterICtrlSetDeviceName": arrisRouterICtrlSetDeviceName,
       "arrisRouterICtrlSetAdminPassword": arrisRouterICtrlSetAdminPassword,
       "arrisRouterICtrlRouterSettings": arrisRouterICtrlRouterSettings,
       "arrisRouterICtrlRouterManageRemote": arrisRouterICtrlRouterManageRemote,
       "arrisRouterICtrlRouterRemotePort": arrisRouterICtrlRouterRemotePort,
       "arrisRouterICtrlRouterRemoteSSL": arrisRouterICtrlRouterRemoteSSL,
       "arrisRouterICtrlWLanRadioSettings": arrisRouterICtrlWLanRadioSettings,
       "arrisRouterICtrlWLanRadioMacAddress": arrisRouterICtrlWLanRadioMacAddress,
       "arrisRouterICtrlWLanRadioChannelWidth": arrisRouterICtrlWLanRadioChannelWidth,
       "arrisRouterICtrlSetBridgeConnect": arrisRouterICtrlSetBridgeConnect,
       "arrisRouterICtrlSetBridgeEthernetPort": arrisRouterICtrlSetBridgeEthernetPort,
       "arrisRouterICtrlSetBridgeMinutes": arrisRouterICtrlSetBridgeMinutes,
       "arrisRouterICtrlSetBridgePermanentPort4Enable": arrisRouterICtrlSetBridgePermanentPort4Enable,
       "arrisRouterICtrlGetWanSettings": arrisRouterICtrlGetWanSettings,
       "arrisRouterICtrlGetWanType": arrisRouterICtrlGetWanType,
       "arrisRouterICtrlGetWanMTU": arrisRouterICtrlGetWanMTU,
       "arrisRouterICtrlGetWanPrefixLen": arrisRouterICtrlGetWanPrefixLen,
       "arrisRouterICtrlGetWanGatewayAddrType": arrisRouterICtrlGetWanGatewayAddrType,
       "arrisRouterICtrlGetWanGatewayAddr": arrisRouterICtrlGetWanGatewayAddr,
       "arrisRouterICtrlGetWanDNSPrimaryAddrType": arrisRouterICtrlGetWanDNSPrimaryAddrType,
       "arrisRouterICtrlGetWanDNSPrimaryAddr": arrisRouterICtrlGetWanDNSPrimaryAddr,
       "arrisRouterICtrlGetWanDNSSecondaryAddrType": arrisRouterICtrlGetWanDNSSecondaryAddrType,
       "arrisRouterICtrlGetWanDNSSecondaryAddr": arrisRouterICtrlGetWanDNSSecondaryAddr,
       "arrisRouterICtrlGetWanMacAddress": arrisRouterICtrlGetWanMacAddress,
       "arrisRouterICtrlHNAPServerPort": arrisRouterICtrlHNAPServerPort,
       "arrisRouterICtrlEnable": arrisRouterICtrlEnable,
       "arrisRouterICtrlHashingKey": arrisRouterICtrlHashingKey,
       "arrisRouterICtrlPortMapTableEnabled": arrisRouterICtrlPortMapTableEnabled,
       "arrisRouterFlapListCfg": arrisRouterFlapListCfg,
       "arrisRouterFlapListEnable": arrisRouterFlapListEnable,
       "arrisRouterFlapListWLANInterval": arrisRouterFlapListWLANInterval,
       "arrisRouterFlapListDHCPInterval": arrisRouterFlapListDHCPInterval,
       "arrisRouterFlapListReportPeroid": arrisRouterFlapListReportPeroid,
       "arrisRouterFlapListWLANCount": arrisRouterFlapListWLANCount,
       "arrisRouterFlapListLANCount": arrisRouterFlapListLANCount,
       "arrisRouterFlapListReqFreqThreshold": arrisRouterFlapListReqFreqThreshold,
       "arrisRouterFlapListWLANTable": arrisRouterFlapListWLANTable,
       "arrisRouterFlapListWLANEntry": arrisRouterFlapListWLANEntry,
       "arrisRouterFlapListWLANIndex": arrisRouterFlapListWLANIndex,
       "arrisRouterFlapListWLANMacAddress": arrisRouterFlapListWLANMacAddress,
       "arrisRouterFlapListWLANRemoveTime": arrisRouterFlapListWLANRemoveTime,
       "arrisRouterFlapListWLANFlapTime": arrisRouterFlapListWLANFlapTime,
       "arrisRouterFlapListLANTable": arrisRouterFlapListLANTable,
       "arrisRouterFlapListLANEntry": arrisRouterFlapListLANEntry,
       "arrisRouterFlapListLANIndex": arrisRouterFlapListLANIndex,
       "arrisRouterFlapListLANMacAddress": arrisRouterFlapListLANMacAddress,
       "arrisRouterFlapListLANRemoveTime": arrisRouterFlapListLANRemoveTime,
       "arrisRouterFlapListLANFlapTime": arrisRouterFlapListLANFlapTime}
)
