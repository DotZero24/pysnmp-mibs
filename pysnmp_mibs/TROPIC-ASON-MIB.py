# SNMP MIB module (TROPIC-ASON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-ASON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:56:42 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(tnAsonMIB,
 tnSystemModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAsonMIB",
    "tnSystemModules")

(AluWdmFecMode,
 AluWdmNewTransferProtocol,
 AluWdmTransferProtocol,
 TnCommand) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmFecMode",
    "AluWdmNewTransferProtocol",
    "AluWdmTransferProtocol",
    "TnCommand")


# MODULE-IDENTITY

tnAsonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    tnAsonMibModule.setRevisions(
        ("2021-07-09 12:00",
         "2021-07-02 12:00",
         "2021-05-21 12:00",
         "2020-12-24 12:00",
         "2020-12-04 12:00",
         "2020-10-09 12:00",
         "2020-05-01 12:00",
         "2020-04-10 12:00",
         "2019-11-22 12:00",
         "2019-11-15 12:00",
         "2019-05-17 12:00",
         "2019-04-26 12:00",
         "2019-04-12 12:00",
         "2019-04-05 12:00",
         "2019-03-29 12:00",
         "2019-03-15 12:00",
         "2018-10-19 12:00",
         "2018-08-24 12:00",
         "2018-07-20 12:00",
         "2018-05-25 12:00",
         "2018-02-23 12:00",
         "2018-01-19 12:00",
         "2018-01-12 12:00",
         "2017-10-20 12:00",
         "2017-10-13 12:00",
         "2017-09-08 12:00",
         "2017-08-18 12:00",
         "2017-07-07 12:00",
         "2017-05-12 12:00",
         "2017-04-28 12:00",
         "2017-04-13 12:00",
         "2017-04-07 12:00",
         "2017-03-17 12:00",
         "2017-02-17 12:00",
         "2016-12-07 12:00",
         "2016-11-16 12:00",
         "2016-10-28 12:00",
         "2016-06-10 12:00",
         "2016-05-18 12:00",
         "2016-04-18 12:00",
         "2016-03-18 12:00",
         "2016-02-24 12:00",
         "2016-02-19 12:00",
         "2016-01-20 12:00",
         "2015-06-29 12:00",
         "2015-06-02 12:00",
         "2015-03-26 12:00",
         "2014-02-26 12:00",
         "2013-11-22 12:00",
         "2013-11-18 12:00",
         "2013-09-20 12:00",
         "2012-11-05 12:00",
         "2012-10-22 12:00",
         "2012-08-10 12:00",
         "2012-06-25 12:00",
         "2012-01-24 12:00",
         "2012-01-17 12:00",
         "2011-08-12 12:00",
         "2011-08-08 12:00",
         "2011-08-03 12:00",
         "2011-07-25 12:00",
         "2011-06-30 12:00",
         "2011-05-31 12:00",
         "2011-05-05 12:00",
         "2011-03-04 12:00",
         "2010-10-12 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluWdmAccessControlDevice(TextualConvention, Integer32):
    status = "current"
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
        *(("null", 1),
          ("cp", 2),
          ("mp", 3),
          ("cpMp", 4))
    )



class TnGmreOptLineImpEncoding(TextualConvention, Integer32):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("pdpsk", 2),
          ("dpsk", 3),
          ("cohpmbpsk", 4),
          ("cohpmqpsk", 5),
          ("icohpmqpsk", 6),
          ("cohpm16qam", 7),
          ("cohpm8qam", 8),
          ("cohspqpsk", 9),
          ("cohpm64qam", 10),
          ("cohpmqpskabs", 11),
          ("cohpm16qamDiffFree", 12),
          ("cohpm16qamAbsDcm", 13),
          ("optimum62g", 14),
          ("optimum67g", 15),
          ("optimum33g", 16),
          ("optimum45g", 17),
          ("optimum56g", 18),
          ("optimum86g", 19),
          ("optimum90g", 20),
          ("optimum90gtc", 21),
          ("optimum86gtc", 22))
    )



class TnGmreOptLineImpCompModule(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("pmdc", 2),
          ("mlse", 3),
          ("tdcm", 4),
          ("txfp", 5),
          ("hperf1", 6),
          ("tcfp", 17),
          ("cr", 18),
          ("ctxfpwt", 19),
          ("sperf2", 20),
          ("hperf2", 21),
          ("add3", 22),
          ("add2l", 23),
          ("cm2ac100h", 24),
          ("ovclk", 25),
          ("cm2ac100", 26),
          ("add3iw", 27),
          ("s13x100", 28),
          ("add3l", 29),
          ("tsfpplus", 30),
          ("cm130sl", 31),
          ("addxs", 32),
          ("add4", 33),
          ("c2aco", 34),
          ("c4aco", 35),
          ("ctxfpiwton", 36),
          ("s13x100l", 37),
          ("add3iwe", 38),
          ("add4l", 39),
          ("add4m", 40),
          ("add5", 41),
          ("alien", 42),
          ("add5u", 43),
          ("add5ul", 44),
          ("add4b", 45))
    )



class TnGmreOptLineImpPhaseEncode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAppl", 0),
          ("absolute", 1),
          ("differential", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnAsonConf_ObjectIdentity = ObjectIdentity
tnAsonConf = _TnAsonConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1)
)
_TnAsonGroups_ObjectIdentity = ObjectIdentity
tnAsonGroups = _TnAsonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1)
)
_TnAsonCompliances_ObjectIdentity = ObjectIdentity
tnAsonCompliances = _TnAsonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 2)
)
_TnAsonObjs_ObjectIdentity = ObjectIdentity
tnAsonObjs = _TnAsonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2)
)
_TnAsonGlobal_ObjectIdentity = ObjectIdentity
tnAsonGlobal = _TnAsonGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1)
)


class _TnGmreNodeIpAddr_Type(IpAddress):
    """Custom type tnGmreNodeIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreNodeIpAddr_Type.__name__ = "IpAddress"
_TnGmreNodeIpAddr_Object = MibScalar
tnGmreNodeIpAddr = _TnGmreNodeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 1),
    _TnGmreNodeIpAddr_Type()
)
tnGmreNodeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreNodeIpAddr.setStatus("current")


class _TnGmreNodeSubMask_Type(IpAddress):
    """Custom type tnGmreNodeSubMask based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreNodeSubMask_Type.__name__ = "IpAddress"
_TnGmreNodeSubMask_Object = MibScalar
tnGmreNodeSubMask = _TnGmreNodeSubMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 2),
    _TnGmreNodeSubMask_Type()
)
tnGmreNodeSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreNodeSubMask.setStatus("current")


class _TnGmreNotifyIpAddr_Type(IpAddress):
    """Custom type tnGmreNotifyIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreNotifyIpAddr_Type.__name__ = "IpAddress"
_TnGmreNotifyIpAddr_Object = MibScalar
tnGmreNotifyIpAddr = _TnGmreNotifyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 3),
    _TnGmreNotifyIpAddr_Type()
)
tnGmreNotifyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreNotifyIpAddr.setStatus("current")


class _TnGmreNotifySubMask_Type(IpAddress):
    """Custom type tnGmreNotifySubMask based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreNotifySubMask_Type.__name__ = "IpAddress"
_TnGmreNotifySubMask_Object = MibScalar
tnGmreNotifySubMask = _TnGmreNotifySubMask_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 4),
    _TnGmreNotifySubMask_Type()
)
tnGmreNotifySubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreNotifySubMask.setStatus("current")


class _TnGmreDiscoveryMode_Type(Integer32):
    """Custom type tnGmreDiscoveryMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnGmreDiscoveryMode_Type.__name__ = "Integer32"
_TnGmreDiscoveryMode_Object = MibScalar
tnGmreDiscoveryMode = _TnGmreDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 5),
    _TnGmreDiscoveryMode_Type()
)
tnGmreDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreDiscoveryMode.setStatus("current")


class _TnGmreAsonItuBandMode_Type(Integer32):
    """Custom type tnGmreAsonItuBandMode based on Integer32"""
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
        *(("unknown", 1),
          ("lBandOnly", 2),
          ("cBandOnly", 3),
          ("cPlusLBand", 4))
    )


_TnGmreAsonItuBandMode_Type.__name__ = "Integer32"
_TnGmreAsonItuBandMode_Object = MibScalar
tnGmreAsonItuBandMode = _TnGmreAsonItuBandMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 6),
    _TnGmreAsonItuBandMode_Type()
)
tnGmreAsonItuBandMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreAsonItuBandMode.setStatus("current")


class _TnGmreClusterMode_Type(Integer32):
    """Custom type tnGmreClusterMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnGmreClusterMode_Type.__name__ = "Integer32"
_TnGmreClusterMode_Object = MibScalar
tnGmreClusterMode = _TnGmreClusterMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 1, 7),
    _TnGmreClusterMode_Type()
)
tnGmreClusterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnGmreClusterMode.setStatus("current")
_TnAsonIorGlobal_ObjectIdentity = ObjectIdentity
tnAsonIorGlobal = _TnAsonIorGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2)
)


class _TnGmreCorbaName_Type(SnmpAdminString):
    """Custom type tnGmreCorbaName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnGmreCorbaName_Type.__name__ = "SnmpAdminString"
_TnGmreCorbaName_Object = MibScalar
tnGmreCorbaName = _TnGmreCorbaName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 1),
    _TnGmreCorbaName_Type()
)
tnGmreCorbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaName.setStatus("current")


class _TnGmreCorbaHostIpAddress_Type(IpAddress):
    """Custom type tnGmreCorbaHostIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreCorbaHostIpAddress_Type.__name__ = "IpAddress"
_TnGmreCorbaHostIpAddress_Object = MibScalar
tnGmreCorbaHostIpAddress = _TnGmreCorbaHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 2),
    _TnGmreCorbaHostIpAddress_Type()
)
tnGmreCorbaHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaHostIpAddress.setStatus("current")


class _TnGmreCorbaIor_Type(SnmpAdminString):
    """Custom type tnGmreCorbaIor based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 265),
    )


_TnGmreCorbaIor_Type.__name__ = "SnmpAdminString"
_TnGmreCorbaIor_Object = MibScalar
tnGmreCorbaIor = _TnGmreCorbaIor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 3),
    _TnGmreCorbaIor_Type()
)
tnGmreCorbaIor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaIor.setStatus("current")


class _TnGmreCorbaIorIPv6_Type(SnmpAdminString):
    """Custom type tnGmreCorbaIorIPv6 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 265),
    )


_TnGmreCorbaIorIPv6_Type.__name__ = "SnmpAdminString"
_TnGmreCorbaIorIPv6_Object = MibScalar
tnGmreCorbaIorIPv6 = _TnGmreCorbaIorIPv6_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 2, 4),
    _TnGmreCorbaIorIPv6_Type()
)
tnGmreCorbaIorIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreCorbaIorIPv6.setStatus("current")
_TnAsonOmsLineImp_ObjectIdentity = ObjectIdentity
tnAsonOmsLineImp = _TnAsonOmsLineImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3)
)
_TnGmreOmsLineImpAttributeTotal_Type = Integer32
_TnGmreOmsLineImpAttributeTotal_Object = MibScalar
tnGmreOmsLineImpAttributeTotal = _TnGmreOmsLineImpAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 1),
    _TnGmreOmsLineImpAttributeTotal_Type()
)
tnGmreOmsLineImpAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpAttributeTotal.setStatus("current")
_TnGmreOmsLineImpTable_Object = MibTable
tnGmreOmsLineImpTable = _TnGmreOmsLineImpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpTable.setStatus("current")
_TnGmreOmsLineImpEntry_Object = MibTableRow
tnGmreOmsLineImpEntry = _TnGmreOmsLineImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1)
)
tnGmreOmsLineImpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpEntry.setStatus("current")


class _TnGmreOmsLineImpMaxAlwCh_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpMaxAlwCh based on Unsigned32"""
    defaultValue = 88

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TnGmreOmsLineImpMaxAlwCh_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpMaxAlwCh_Object = MibTableColumn
tnGmreOmsLineImpMaxAlwCh = _TnGmreOmsLineImpMaxAlwCh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 1),
    _TnGmreOmsLineImpMaxAlwCh_Type()
)
tnGmreOmsLineImpMaxAlwCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpMaxAlwCh.setStatus("current")


class _TnGmreOmsLineImpPMD_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpPMD based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnGmreOmsLineImpPMD_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpPMD_Object = MibTableColumn
tnGmreOmsLineImpPMD = _TnGmreOmsLineImpPMD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 2),
    _TnGmreOmsLineImpPMD_Type()
)
tnGmreOmsLineImpPMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPMD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPMD.setUnits("1/10 picoSecond")


class _TnGmreOmsLineImpAlcMode_Type(Integer32):
    """Custom type tnGmreOmsLineImpAlcMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnGmreOmsLineImpAlcMode_Type.__name__ = "Integer32"
_TnGmreOmsLineImpAlcMode_Object = MibTableColumn
tnGmreOmsLineImpAlcMode = _TnGmreOmsLineImpAlcMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 3),
    _TnGmreOmsLineImpAlcMode_Type()
)
tnGmreOmsLineImpAlcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpAlcMode.setStatus("current")


class _TnGmreOmsLineImpDcuFree_Type(Integer32):
    """Custom type tnGmreOmsLineImpDcuFree based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnGmreOmsLineImpDcuFree_Type.__name__ = "Integer32"
_TnGmreOmsLineImpDcuFree_Object = MibTableColumn
tnGmreOmsLineImpDcuFree = _TnGmreOmsLineImpDcuFree_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 4),
    _TnGmreOmsLineImpDcuFree_Type()
)
tnGmreOmsLineImpDcuFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpDcuFree.setStatus("current")


class _TnGmreOmsLineImpCD_Type(Integer32):
    """Custom type tnGmreOmsLineImpCD based on Integer32"""
    defaultValue = 17000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40000, 78000),
    )


_TnGmreOmsLineImpCD_Type.__name__ = "Integer32"
_TnGmreOmsLineImpCD_Object = MibTableColumn
tnGmreOmsLineImpCD = _TnGmreOmsLineImpCD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 5),
    _TnGmreOmsLineImpCD_Type()
)
tnGmreOmsLineImpCD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD.setUnits("1/10 ps/nm")


class _TnGmreOmsLineImpFiberType_Type(Integer32):
    """Custom type tnGmreOmsLineImpFiberType based on Integer32"""
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ssmf", 1),
          ("eleaf", 2),
          ("twrs", 3),
          ("twc", 4),
          ("twp", 5),
          ("mixed", 6),
          ("ls", 7),
          ("dsf", 8),
          ("lx1830ssmf", 9),
          ("lx1830g654", 10))
    )


_TnGmreOmsLineImpFiberType_Type.__name__ = "Integer32"
_TnGmreOmsLineImpFiberType_Object = MibTableColumn
tnGmreOmsLineImpFiberType = _TnGmreOmsLineImpFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 6),
    _TnGmreOmsLineImpFiberType_Type()
)
tnGmreOmsLineImpFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpFiberType.setStatus("current")


class _TnGmreOmsLineImpPDL_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpPDL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TnGmreOmsLineImpPDL_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpPDL_Object = MibTableColumn
tnGmreOmsLineImpPDL = _TnGmreOmsLineImpPDL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 7),
    _TnGmreOmsLineImpPDL_Type()
)
tnGmreOmsLineImpPDL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPDL.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpPDL.setUnits("1 dB")


class _TnGmreOmsLineImpCD1546_Type(Integer32):
    """Custom type tnGmreOmsLineImpCD1546 based on Integer32"""
    defaultValue = 17000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40000, 78000),
    )


_TnGmreOmsLineImpCD1546_Type.__name__ = "Integer32"
_TnGmreOmsLineImpCD1546_Object = MibTableColumn
tnGmreOmsLineImpCD1546 = _TnGmreOmsLineImpCD1546_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 8),
    _TnGmreOmsLineImpCD1546_Type()
)
tnGmreOmsLineImpCD1546.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD1546.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpCD1546.setUnits("1/10 ps/nm")


class _TnGmreOmsLineImp1830lxdcm_Type(Integer32):
    """Custom type tnGmreOmsLineImp1830lxdcm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 0),
    )


_TnGmreOmsLineImp1830lxdcm_Type.__name__ = "Integer32"
_TnGmreOmsLineImp1830lxdcm_Object = MibTableColumn
tnGmreOmsLineImp1830lxdcm = _TnGmreOmsLineImp1830lxdcm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 3, 2, 1, 9),
    _TnGmreOmsLineImp1830lxdcm_Type()
)
tnGmreOmsLineImp1830lxdcm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImp1830lxdcm.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImp1830lxdcm.setUnits("1/10 ps/nm")
_TnAsonOptLineImp_ObjectIdentity = ObjectIdentity
tnAsonOptLineImp = _TnAsonOptLineImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4)
)
_TnGmreOptLineImpAttributeTotal_Type = Integer32
_TnGmreOptLineImpAttributeTotal_Object = MibScalar
tnGmreOptLineImpAttributeTotal = _TnGmreOptLineImpAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 1),
    _TnGmreOptLineImpAttributeTotal_Type()
)
tnGmreOptLineImpAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOptLineImpAttributeTotal.setStatus("current")
_TnGmreOptLineImpTable_Object = MibTable
tnGmreOptLineImpTable = _TnGmreOptLineImpTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2)
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpTable.setStatus("current")
_TnGmreOptLineImpEntry_Object = MibTableRow
tnGmreOptLineImpEntry = _TnGmreOptLineImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1)
)
tnGmreOptLineImpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOptLineImpIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpEntry.setStatus("current")
_TnGmreOptLineImpIndex_Type = Unsigned32
_TnGmreOptLineImpIndex_Object = MibTableColumn
tnGmreOptLineImpIndex = _TnGmreOptLineImpIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 1),
    _TnGmreOptLineImpIndex_Type()
)
tnGmreOptLineImpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOptLineImpIndex.setStatus("current")


class _TnGmreOptLineImpBitRate_Type(Integer32):
    """Custom type tnGmreOptLineImpBitRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate2G5", 1),
          ("rate10G", 2),
          ("rate40G", 3),
          ("rate100G", 4),
          ("rate260G", 5),
          ("rate50G", 6),
          ("rate200G", 7),
          ("rate250G", 8),
          ("rate400G", 9),
          ("rate300G", 10),
          ("rate600G", 11),
          ("rate500G", 12))
    )


_TnGmreOptLineImpBitRate_Type.__name__ = "Integer32"
_TnGmreOptLineImpBitRate_Object = MibTableColumn
tnGmreOptLineImpBitRate = _TnGmreOptLineImpBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 2),
    _TnGmreOptLineImpBitRate_Type()
)
tnGmreOptLineImpBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpBitRate.setStatus("current")
_TnGmreOptLineImpEncoding_Type = TnGmreOptLineImpEncoding
_TnGmreOptLineImpEncoding_Object = MibTableColumn
tnGmreOptLineImpEncoding = _TnGmreOptLineImpEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 3),
    _TnGmreOptLineImpEncoding_Type()
)
tnGmreOptLineImpEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpEncoding.setStatus("current")
_TnGmreOptLineImpCompModule_Type = TnGmreOptLineImpCompModule
_TnGmreOptLineImpCompModule_Object = MibTableColumn
tnGmreOptLineImpCompModule = _TnGmreOptLineImpCompModule_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 4),
    _TnGmreOptLineImpCompModule_Type()
)
tnGmreOptLineImpCompModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpCompModule.setStatus("current")
_TnGmreOptLineImpFecMode_Type = AluWdmFecMode
_TnGmreOptLineImpFecMode_Object = MibTableColumn
tnGmreOptLineImpFecMode = _TnGmreOptLineImpFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 5),
    _TnGmreOptLineImpFecMode_Type()
)
tnGmreOptLineImpFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpFecMode.setStatus("current")


class _TnGmreOptLineImpNLP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpNLP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99900000),
    )


_TnGmreOptLineImpNLP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpNLP_Object = MibTableColumn
tnGmreOptLineImpNLP = _TnGmreOptLineImpNLP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 6),
    _TnGmreOptLineImpNLP_Type()
)
tnGmreOptLineImpNLP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLP.setUnits("percentage")


class _TnGmreOptLineImpOSNR_Type(Unsigned32):
    """Custom type tnGmreOptLineImpOSNR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3162277660),
    )


_TnGmreOptLineImpOSNR_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpOSNR_Object = MibTableColumn
tnGmreOptLineImpOSNR = _TnGmreOptLineImpOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 7),
    _TnGmreOptLineImpOSNR_Type()
)
tnGmreOptLineImpOSNR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpOSNR.setStatus("current")


class _TnGmreOptLineImpNLPNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpNLPNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99900000),
    )


_TnGmreOptLineImpNLPNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpNLPNP_Object = MibTableColumn
tnGmreOptLineImpNLPNP = _TnGmreOptLineImpNLPNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 8),
    _TnGmreOptLineImpNLPNP_Type()
)
tnGmreOptLineImpNLPNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLPNP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpNLPNP.setUnits("percentage")


class _TnGmreOptLineImpOSNRNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpOSNRNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3162277660),
    )


_TnGmreOptLineImpOSNRNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpOSNRNP_Object = MibTableColumn
tnGmreOptLineImpOSNRNP = _TnGmreOptLineImpOSNRNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 9),
    _TnGmreOptLineImpOSNRNP_Type()
)
tnGmreOptLineImpOSNRNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpOSNRNP.setStatus("current")
_TnGmreOptLineImpRowStatus_Type = RowStatus
_TnGmreOptLineImpRowStatus_Object = MibTableColumn
tnGmreOptLineImpRowStatus = _TnGmreOptLineImpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 10),
    _TnGmreOptLineImpRowStatus_Type()
)
tnGmreOptLineImpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpRowStatus.setStatus("current")


class _TnGmreOptLineImpPower_Type(Unsigned32):
    """Custom type tnGmreOptLineImpPower based on Unsigned32"""
    defaultValue = 790

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40500),
    )


_TnGmreOptLineImpPower_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpPower_Object = MibTableColumn
tnGmreOptLineImpPower = _TnGmreOptLineImpPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 11),
    _TnGmreOptLineImpPower_Type()
)
tnGmreOptLineImpPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpPower.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpPower.setUnits("micro-Watts")
_TnGmreOptLineImpPhaseEncode_Type = TnGmreOptLineImpPhaseEncode
_TnGmreOptLineImpPhaseEncode_Object = MibTableColumn
tnGmreOptLineImpPhaseEncode = _TnGmreOptLineImpPhaseEncode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 4, 2, 1, 12),
    _TnGmreOptLineImpPhaseEncode_Type()
)
tnGmreOptLineImpPhaseEncode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpPhaseEncode.setStatus("current")
_TnAsonTopoAlarm_ObjectIdentity = ObjectIdentity
tnAsonTopoAlarm = _TnAsonTopoAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5)
)
_TnAsonTopoAlarmAttributeTotal_Type = Integer32
_TnAsonTopoAlarmAttributeTotal_Object = MibScalar
tnAsonTopoAlarmAttributeTotal = _TnAsonTopoAlarmAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 1),
    _TnAsonTopoAlarmAttributeTotal_Type()
)
tnAsonTopoAlarmAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonTopoAlarmAttributeTotal.setStatus("current")
_TnAsonTopoAlarmTable_Object = MibTable
tnAsonTopoAlarmTable = _TnAsonTopoAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2)
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmTable.setStatus("current")
_TnAsonTopoAlarmEntry_Object = MibTableRow
tnAsonTopoAlarmEntry = _TnAsonTopoAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2, 1)
)
tnAsonTopoAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmEntry.setStatus("current")


class _TnAsonTopoClearAlarm_Type(TnCommand):
    """Custom type tnAsonTopoClearAlarm based on TnCommand"""
    defaultValue = 1


_TnAsonTopoClearAlarm_Type.__name__ = "TnCommand"
_TnAsonTopoClearAlarm_Object = MibTableColumn
tnAsonTopoClearAlarm = _TnAsonTopoClearAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 5, 2, 1, 1),
    _TnAsonTopoClearAlarm_Type()
)
tnAsonTopoClearAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonTopoClearAlarm.setStatus("current")
_TnAsonFeasibility_ObjectIdentity = ObjectIdentity
tnAsonFeasibility = _TnAsonFeasibility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6)
)


class _TnAsonFeasibilityCommand_Type(Integer32):
    """Custom type tnAsonFeasibilityCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCmd", 1),
          ("transferFromRemote", 2))
    )


_TnAsonFeasibilityCommand_Type.__name__ = "Integer32"
_TnAsonFeasibilityCommand_Object = MibScalar
tnAsonFeasibilityCommand = _TnAsonFeasibilityCommand_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 1),
    _TnAsonFeasibilityCommand_Type()
)
tnAsonFeasibilityCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityCommand.setStatus("current")


class _TnAsonFeasibilityRemoteHostIp_Type(IpAddress):
    """Custom type tnAsonFeasibilityRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnAsonFeasibilityRemoteHostIp_Type.__name__ = "IpAddress"
_TnAsonFeasibilityRemoteHostIp_Object = MibScalar
tnAsonFeasibilityRemoteHostIp = _TnAsonFeasibilityRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 2),
    _TnAsonFeasibilityRemoteHostIp_Type()
)
tnAsonFeasibilityRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemoteHostIp.setStatus("current")


class _TnAsonFeasibilityRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityRemotePath_Object = MibScalar
tnAsonFeasibilityRemotePath = _TnAsonFeasibilityRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 3),
    _TnAsonFeasibilityRemotePath_Type()
)
tnAsonFeasibilityRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemotePath.setStatus("current")


class _TnAsonFeasibilityStatus_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityStatus based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityStatus_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityStatus_Object = MibScalar
tnAsonFeasibilityStatus = _TnAsonFeasibilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 4),
    _TnAsonFeasibilityStatus_Type()
)
tnAsonFeasibilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonFeasibilityStatus.setStatus("current")


class _TnAsonFeasibilityLastTransferredVersion_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityLastTransferredVersion based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonFeasibilityLastTransferredVersion_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityLastTransferredVersion_Object = MibScalar
tnAsonFeasibilityLastTransferredVersion = _TnAsonFeasibilityLastTransferredVersion_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 5),
    _TnAsonFeasibilityLastTransferredVersion_Type()
)
tnAsonFeasibilityLastTransferredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonFeasibilityLastTransferredVersion.setStatus("current")


class _TnAsonFeasibilityProtocol_Type(AluWdmNewTransferProtocol):
    """Custom type tnAsonFeasibilityProtocol based on AluWdmNewTransferProtocol"""
    defaultValue = 1


_TnAsonFeasibilityProtocol_Type.__name__ = "AluWdmNewTransferProtocol"
_TnAsonFeasibilityProtocol_Object = MibScalar
tnAsonFeasibilityProtocol = _TnAsonFeasibilityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 6),
    _TnAsonFeasibilityProtocol_Type()
)
tnAsonFeasibilityProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityProtocol.setStatus("current")


class _TnAsonFeasibilityUserId_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityUserId based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnAsonFeasibilityUserId_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityUserId_Object = MibScalar
tnAsonFeasibilityUserId = _TnAsonFeasibilityUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 7),
    _TnAsonFeasibilityUserId_Type()
)
tnAsonFeasibilityUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityUserId.setStatus("current")


class _TnAsonFeasibilityPassword_Type(SnmpAdminString):
    """Custom type tnAsonFeasibilityPassword based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_TnAsonFeasibilityPassword_Type.__name__ = "SnmpAdminString"
_TnAsonFeasibilityPassword_Object = MibScalar
tnAsonFeasibilityPassword = _TnAsonFeasibilityPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 8),
    _TnAsonFeasibilityPassword_Type()
)
tnAsonFeasibilityPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityPassword.setStatus("current")


class _TnAsonFeasibilityRemoteInetAddressType_Type(InetAddressType):
    """Custom type tnAsonFeasibilityRemoteInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnAsonFeasibilityRemoteInetAddressType_Type.__name__ = "InetAddressType"
_TnAsonFeasibilityRemoteInetAddressType_Object = MibScalar
tnAsonFeasibilityRemoteInetAddressType = _TnAsonFeasibilityRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 9),
    _TnAsonFeasibilityRemoteInetAddressType_Type()
)
tnAsonFeasibilityRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemoteInetAddressType.setStatus("current")


class _TnAsonFeasibilityRemoteInetAddress_Type(InetAddress):
    """Custom type tnAsonFeasibilityRemoteInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnAsonFeasibilityRemoteInetAddress_Type.__name__ = "InetAddress"
_TnAsonFeasibilityRemoteInetAddress_Object = MibScalar
tnAsonFeasibilityRemoteInetAddress = _TnAsonFeasibilityRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 10),
    _TnAsonFeasibilityRemoteInetAddress_Type()
)
tnAsonFeasibilityRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityRemoteInetAddress.setStatus("current")


class _TnAsonFeasibilityPort_Type(Unsigned32):
    """Custom type tnAsonFeasibilityPort based on Unsigned32"""
    defaultValue = 21

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TnAsonFeasibilityPort_Type.__name__ = "Unsigned32"
_TnAsonFeasibilityPort_Object = MibScalar
tnAsonFeasibilityPort = _TnAsonFeasibilityPort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 6, 11),
    _TnAsonFeasibilityPort_Type()
)
tnAsonFeasibilityPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonFeasibilityPort.setStatus("current")
_TnAsonMgracdInfo_ObjectIdentity = ObjectIdentity
tnAsonMgracdInfo = _TnAsonMgracdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7)
)
_TnAsonMgracdAttributeTotal_Type = Integer32
_TnAsonMgracdAttributeTotal_Object = MibScalar
tnAsonMgracdAttributeTotal = _TnAsonMgracdAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 1),
    _TnAsonMgracdAttributeTotal_Type()
)
tnAsonMgracdAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonMgracdAttributeTotal.setStatus("current")
_TnAsonMgracdTable_Object = MibTable
tnAsonMgracdTable = _TnAsonMgracdTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2)
)
if mibBuilder.loadTexts:
    tnAsonMgracdTable.setStatus("current")
_TnAsonMgracdEntry_Object = MibTableRow
tnAsonMgracdEntry = _TnAsonMgracdEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1)
)
tnAsonMgracdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAsonMgracdEntry.setStatus("current")


class _TnAsonOchMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOchMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOchMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOchMgracd_Object = MibTableColumn
tnAsonOchMgracd = _TnAsonOchMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 1),
    _TnAsonOchMgracd_Type()
)
tnAsonOchMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOchMgracd.setStatus("current")


class _TnAsonOmsochifMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOmsochifMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOmsochifMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOmsochifMgracd_Object = MibTableColumn
tnAsonOmsochifMgracd = _TnAsonOmsochifMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 2),
    _TnAsonOmsochifMgracd_Type()
)
tnAsonOmsochifMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOmsochifMgracd.setStatus("current")


class _TnAsonOtsMgracd_Type(AluWdmAccessControlDevice):
    """Custom type tnAsonOtsMgracd based on AluWdmAccessControlDevice"""
    defaultValue = 1


_TnAsonOtsMgracd_Type.__name__ = "AluWdmAccessControlDevice"
_TnAsonOtsMgracd_Object = MibTableColumn
tnAsonOtsMgracd = _TnAsonOtsMgracd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 7, 2, 1, 3),
    _TnAsonOtsMgracd_Type()
)
tnAsonOtsMgracd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonOtsMgracd.setStatus("current")
_TnAsonOmsWavelengthSet_ObjectIdentity = ObjectIdentity
tnAsonOmsWavelengthSet = _TnAsonOmsWavelengthSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8)
)
_TnGmreOmsWavelengthSetAttributeTotal_Type = Integer32
_TnGmreOmsWavelengthSetAttributeTotal_Object = MibScalar
tnGmreOmsWavelengthSetAttributeTotal = _TnGmreOmsWavelengthSetAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 1),
    _TnGmreOmsWavelengthSetAttributeTotal_Type()
)
tnGmreOmsWavelengthSetAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetAttributeTotal.setStatus("current")
_TnGmreOmsWavelengthSetTable_Object = MibTable
tnGmreOmsWavelengthSetTable = _TnGmreOmsWavelengthSetTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetTable.setStatus("current")
_TnGmreOmsWavelengthSetEntry_Object = MibTableRow
tnGmreOmsWavelengthSetEntry = _TnGmreOmsWavelengthSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1)
)
tnGmreOmsWavelengthSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOmsWavelengthEncodingType"),
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetEntry.setStatus("current")


class _TnGmreOmsWavelengthEncodingType_Type(Integer32):
    """Custom type tnGmreOmsWavelengthEncodingType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("pdpsk", 2),
          ("coherent", 3),
          ("slotWidth50", 4),
          ("slotWidth62p5", 5),
          ("coherent16qam", 6),
          ("slotWidth75g", 7),
          ("slotWidth87p5g", 8),
          ("slotWidth100g", 9),
          ("slotWidth112p5g", 10),
          ("slotWidth125g", 11))
    )


_TnGmreOmsWavelengthEncodingType_Type.__name__ = "Integer32"
_TnGmreOmsWavelengthEncodingType_Object = MibTableColumn
tnGmreOmsWavelengthEncodingType = _TnGmreOmsWavelengthEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1, 1),
    _TnGmreOmsWavelengthEncodingType_Type()
)
tnGmreOmsWavelengthEncodingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthEncodingType.setStatus("current")


class _TnGmreOmsWavelengthEncodingBitMap_Type(OctetString):
    """Custom type tnGmreOmsWavelengthEncodingBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TnGmreOmsWavelengthEncodingBitMap_Type.__name__ = "OctetString"
_TnGmreOmsWavelengthEncodingBitMap_Object = MibTableColumn
tnGmreOmsWavelengthEncodingBitMap = _TnGmreOmsWavelengthEncodingBitMap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 8, 2, 1, 2),
    _TnGmreOmsWavelengthEncodingBitMap_Type()
)
tnGmreOmsWavelengthEncodingBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthEncodingBitMap.setStatus("current")
_TnAsonSnapshot_ObjectIdentity = ObjectIdentity
tnAsonSnapshot = _TnAsonSnapshot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9)
)


class _TnAsonSnapshotRemoteHostIp_Type(IpAddress):
    """Custom type tnAsonSnapshotRemoteHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_TnAsonSnapshotRemoteHostIp_Type.__name__ = "IpAddress"
_TnAsonSnapshotRemoteHostIp_Object = MibScalar
tnAsonSnapshotRemoteHostIp = _TnAsonSnapshotRemoteHostIp_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 1),
    _TnAsonSnapshotRemoteHostIp_Type()
)
tnAsonSnapshotRemoteHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemoteHostIp.setStatus("current")
_TnAsonSnapshotProtocol_Type = AluWdmTransferProtocol
_TnAsonSnapshotProtocol_Object = MibScalar
tnAsonSnapshotProtocol = _TnAsonSnapshotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 2),
    _TnAsonSnapshotProtocol_Type()
)
tnAsonSnapshotProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotProtocol.setStatus("current")
_TnAsonSnapshotUserId_Type = SnmpAdminString
_TnAsonSnapshotUserId_Object = MibScalar
tnAsonSnapshotUserId = _TnAsonSnapshotUserId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 3),
    _TnAsonSnapshotUserId_Type()
)
tnAsonSnapshotUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotUserId.setStatus("current")
_TnAsonSnapshotPassword_Type = SnmpAdminString
_TnAsonSnapshotPassword_Object = MibScalar
tnAsonSnapshotPassword = _TnAsonSnapshotPassword_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 4),
    _TnAsonSnapshotPassword_Type()
)
tnAsonSnapshotPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotPassword.setStatus("current")


class _TnAsonSnapshotRootRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotRootRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotRootRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotRootRemotePath_Object = MibScalar
tnAsonSnapshotRootRemotePath = _TnAsonSnapshotRootRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 5),
    _TnAsonSnapshotRootRemotePath_Type()
)
tnAsonSnapshotRootRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRootRemotePath.setStatus("current")
_TnAsonSnapshotAttributeTotal_Type = Integer32
_TnAsonSnapshotAttributeTotal_Object = MibScalar
tnAsonSnapshotAttributeTotal = _TnAsonSnapshotAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 6),
    _TnAsonSnapshotAttributeTotal_Type()
)
tnAsonSnapshotAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotAttributeTotal.setStatus("current")
_TnAsonSnapshotTable_Object = MibTable
tnAsonSnapshotTable = _TnAsonSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7)
)
if mibBuilder.loadTexts:
    tnAsonSnapshotTable.setStatus("current")
_TnAsonSnapshotEntry_Object = MibTableRow
tnAsonSnapshotEntry = _TnAsonSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1)
)
tnAsonSnapshotEntry.setIndexNames(
    (0, "TROPIC-ASON-MIB", "tnAsonSnapshotTime"),
)
if mibBuilder.loadTexts:
    tnAsonSnapshotEntry.setStatus("current")
_TnAsonSnapshotTime_Type = Unsigned32
_TnAsonSnapshotTime_Object = MibTableColumn
tnAsonSnapshotTime = _TnAsonSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 1),
    _TnAsonSnapshotTime_Type()
)
tnAsonSnapshotTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAsonSnapshotTime.setStatus("current")


class _TnAsonSnapshotStatus_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotStatus_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotStatus_Object = MibTableColumn
tnAsonSnapshotStatus = _TnAsonSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 2),
    _TnAsonSnapshotStatus_Type()
)
tnAsonSnapshotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotStatus.setStatus("current")


class _TnAsonSnapshotRemotePath_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotRemotePath based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotRemotePath_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotRemotePath_Object = MibTableColumn
tnAsonSnapshotRemotePath = _TnAsonSnapshotRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 3),
    _TnAsonSnapshotRemotePath_Type()
)
tnAsonSnapshotRemotePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemotePath.setStatus("current")
_TnAsonSnapshotRowStatus_Type = RowStatus
_TnAsonSnapshotRowStatus_Object = MibTableColumn
tnAsonSnapshotRowStatus = _TnAsonSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 4),
    _TnAsonSnapshotRowStatus_Type()
)
tnAsonSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAsonSnapshotRowStatus.setStatus("current")


class _TnAsonSnapshotFilename_Type(SnmpAdminString):
    """Custom type tnAsonSnapshotFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAsonSnapshotFilename_Type.__name__ = "SnmpAdminString"
_TnAsonSnapshotFilename_Object = MibTableColumn
tnAsonSnapshotFilename = _TnAsonSnapshotFilename_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 7, 1, 5),
    _TnAsonSnapshotFilename_Type()
)
tnAsonSnapshotFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAsonSnapshotFilename.setStatus("current")


class _TnAsonSnapshotRemoteInetAddressType_Type(InetAddressType):
    """Custom type tnAsonSnapshotRemoteInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnAsonSnapshotRemoteInetAddressType_Type.__name__ = "InetAddressType"
_TnAsonSnapshotRemoteInetAddressType_Object = MibScalar
tnAsonSnapshotRemoteInetAddressType = _TnAsonSnapshotRemoteInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 8),
    _TnAsonSnapshotRemoteInetAddressType_Type()
)
tnAsonSnapshotRemoteInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemoteInetAddressType.setStatus("current")


class _TnAsonSnapshotRemoteInetAddress_Type(InetAddress):
    """Custom type tnAsonSnapshotRemoteInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnAsonSnapshotRemoteInetAddress_Type.__name__ = "InetAddress"
_TnAsonSnapshotRemoteInetAddress_Object = MibScalar
tnAsonSnapshotRemoteInetAddress = _TnAsonSnapshotRemoteInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 9, 9),
    _TnAsonSnapshotRemoteInetAddress_Type()
)
tnAsonSnapshotRemoteInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnAsonSnapshotRemoteInetAddress.setStatus("current")
_TnAsonOmsLineImpL_ObjectIdentity = ObjectIdentity
tnAsonOmsLineImpL = _TnAsonOmsLineImpL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10)
)
_TnGmreOmsLineImpLAttributeTotal_Type = Integer32
_TnGmreOmsLineImpLAttributeTotal_Object = MibScalar
tnGmreOmsLineImpLAttributeTotal = _TnGmreOmsLineImpLAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 1),
    _TnGmreOmsLineImpLAttributeTotal_Type()
)
tnGmreOmsLineImpLAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLAttributeTotal.setStatus("current")
_TnGmreOmsLineImpLTable_Object = MibTable
tnGmreOmsLineImpLTable = _TnGmreOmsLineImpLTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLTable.setStatus("current")
_TnGmreOmsLineImpLEntry_Object = MibTableRow
tnGmreOmsLineImpLEntry = _TnGmreOmsLineImpLEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1)
)
tnGmreOmsLineImpLEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLEntry.setStatus("current")


class _TnGmreOmsLineImpLMaxAlwCh_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpLMaxAlwCh based on Unsigned32"""
    defaultValue = 88

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TnGmreOmsLineImpLMaxAlwCh_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpLMaxAlwCh_Object = MibTableColumn
tnGmreOmsLineImpLMaxAlwCh = _TnGmreOmsLineImpLMaxAlwCh_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 1),
    _TnGmreOmsLineImpLMaxAlwCh_Type()
)
tnGmreOmsLineImpLMaxAlwCh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLMaxAlwCh.setStatus("current")


class _TnGmreOmsLineImpLPMD_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpLPMD based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TnGmreOmsLineImpLPMD_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpLPMD_Object = MibTableColumn
tnGmreOmsLineImpLPMD = _TnGmreOmsLineImpLPMD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 2),
    _TnGmreOmsLineImpLPMD_Type()
)
tnGmreOmsLineImpLPMD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLPMD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLPMD.setUnits("1/10 picoSecond")


class _TnGmreOmsLineImpLAlcMode_Type(Integer32):
    """Custom type tnGmreOmsLineImpLAlcMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TnGmreOmsLineImpLAlcMode_Type.__name__ = "Integer32"
_TnGmreOmsLineImpLAlcMode_Object = MibTableColumn
tnGmreOmsLineImpLAlcMode = _TnGmreOmsLineImpLAlcMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 3),
    _TnGmreOmsLineImpLAlcMode_Type()
)
tnGmreOmsLineImpLAlcMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLAlcMode.setStatus("current")


class _TnGmreOmsLineImpLDcuFree_Type(Integer32):
    """Custom type tnGmreOmsLineImpLDcuFree based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TnGmreOmsLineImpLDcuFree_Type.__name__ = "Integer32"
_TnGmreOmsLineImpLDcuFree_Object = MibTableColumn
tnGmreOmsLineImpLDcuFree = _TnGmreOmsLineImpLDcuFree_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 4),
    _TnGmreOmsLineImpLDcuFree_Type()
)
tnGmreOmsLineImpLDcuFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLDcuFree.setStatus("current")


class _TnGmreOmsLineImpLCD_Type(Integer32):
    """Custom type tnGmreOmsLineImpLCD based on Integer32"""
    defaultValue = 17000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40000, 78000),
    )


_TnGmreOmsLineImpLCD_Type.__name__ = "Integer32"
_TnGmreOmsLineImpLCD_Object = MibTableColumn
tnGmreOmsLineImpLCD = _TnGmreOmsLineImpLCD_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 5),
    _TnGmreOmsLineImpLCD_Type()
)
tnGmreOmsLineImpLCD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLCD.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLCD.setUnits("1/10 ps/nm")


class _TnGmreOmsLineImpLFiberType_Type(Integer32):
    """Custom type tnGmreOmsLineImpLFiberType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ssmf", 1),
          ("eleaf", 2),
          ("twrs", 3),
          ("twc", 4),
          ("twp", 5),
          ("mixed", 6),
          ("ls", 7),
          ("dsf", 8))
    )


_TnGmreOmsLineImpLFiberType_Type.__name__ = "Integer32"
_TnGmreOmsLineImpLFiberType_Object = MibTableColumn
tnGmreOmsLineImpLFiberType = _TnGmreOmsLineImpLFiberType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 6),
    _TnGmreOmsLineImpLFiberType_Type()
)
tnGmreOmsLineImpLFiberType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLFiberType.setStatus("current")


class _TnGmreOmsLineImpLPDL_Type(Unsigned32):
    """Custom type tnGmreOmsLineImpLPDL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_TnGmreOmsLineImpLPDL_Type.__name__ = "Unsigned32"
_TnGmreOmsLineImpLPDL_Object = MibTableColumn
tnGmreOmsLineImpLPDL = _TnGmreOmsLineImpLPDL_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 10, 2, 1, 7),
    _TnGmreOmsLineImpLPDL_Type()
)
tnGmreOmsLineImpLPDL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLPDL.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOmsLineImpLPDL.setUnits("1 dB")
_TnAsonOptLineImpL_ObjectIdentity = ObjectIdentity
tnAsonOptLineImpL = _TnAsonOptLineImpL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11)
)
_TnGmreOptLineImpLAttributeTotal_Type = Integer32
_TnGmreOptLineImpLAttributeTotal_Object = MibScalar
tnGmreOptLineImpLAttributeTotal = _TnGmreOptLineImpLAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 1),
    _TnGmreOptLineImpLAttributeTotal_Type()
)
tnGmreOptLineImpLAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLAttributeTotal.setStatus("current")
_TnGmreOptLineImpLTable_Object = MibTable
tnGmreOptLineImpLTable = _TnGmreOptLineImpLTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2)
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpLTable.setStatus("current")
_TnGmreOptLineImpLEntry_Object = MibTableRow
tnGmreOptLineImpLEntry = _TnGmreOptLineImpLEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1)
)
tnGmreOptLineImpLEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOptLineImpLIndex"),
)
if mibBuilder.loadTexts:
    tnGmreOptLineImpLEntry.setStatus("current")
_TnGmreOptLineImpLIndex_Type = Unsigned32
_TnGmreOptLineImpLIndex_Object = MibTableColumn
tnGmreOptLineImpLIndex = _TnGmreOptLineImpLIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 1),
    _TnGmreOptLineImpLIndex_Type()
)
tnGmreOptLineImpLIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLIndex.setStatus("current")


class _TnGmreOptLineImpLBitRate_Type(Integer32):
    """Custom type tnGmreOptLineImpLBitRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("rate2G5", 1),
          ("rate10G", 2),
          ("rate40G", 3),
          ("rate100G", 4),
          ("rate260G", 5),
          ("rate50G", 6),
          ("rate200G", 7),
          ("rate250G", 8),
          ("rate400G", 9),
          ("rate300G", 10),
          ("rate600G", 11),
          ("rate500G", 12))
    )


_TnGmreOptLineImpLBitRate_Type.__name__ = "Integer32"
_TnGmreOptLineImpLBitRate_Object = MibTableColumn
tnGmreOptLineImpLBitRate = _TnGmreOptLineImpLBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 2),
    _TnGmreOptLineImpLBitRate_Type()
)
tnGmreOptLineImpLBitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLBitRate.setStatus("current")
_TnGmreOptLineImpLEncoding_Type = TnGmreOptLineImpEncoding
_TnGmreOptLineImpLEncoding_Object = MibTableColumn
tnGmreOptLineImpLEncoding = _TnGmreOptLineImpLEncoding_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 3),
    _TnGmreOptLineImpLEncoding_Type()
)
tnGmreOptLineImpLEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLEncoding.setStatus("current")
_TnGmreOptLineImpLCompModule_Type = TnGmreOptLineImpCompModule
_TnGmreOptLineImpLCompModule_Object = MibTableColumn
tnGmreOptLineImpLCompModule = _TnGmreOptLineImpLCompModule_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 4),
    _TnGmreOptLineImpLCompModule_Type()
)
tnGmreOptLineImpLCompModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLCompModule.setStatus("current")
_TnGmreOptLineImpLFecMode_Type = AluWdmFecMode
_TnGmreOptLineImpLFecMode_Object = MibTableColumn
tnGmreOptLineImpLFecMode = _TnGmreOptLineImpLFecMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 5),
    _TnGmreOptLineImpLFecMode_Type()
)
tnGmreOptLineImpLFecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLFecMode.setStatus("current")


class _TnGmreOptLineImpLNLP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpLNLP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99900000),
    )


_TnGmreOptLineImpLNLP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpLNLP_Object = MibTableColumn
tnGmreOptLineImpLNLP = _TnGmreOptLineImpLNLP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 6),
    _TnGmreOptLineImpLNLP_Type()
)
tnGmreOptLineImpLNLP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLNLP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLNLP.setUnits("percentage")


class _TnGmreOptLineImpLOSNR_Type(Unsigned32):
    """Custom type tnGmreOptLineImpLOSNR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3162277660),
    )


_TnGmreOptLineImpLOSNR_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpLOSNR_Object = MibTableColumn
tnGmreOptLineImpLOSNR = _TnGmreOptLineImpLOSNR_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 7),
    _TnGmreOptLineImpLOSNR_Type()
)
tnGmreOptLineImpLOSNR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLOSNR.setStatus("current")


class _TnGmreOptLineImpLNLPNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpLNLPNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99900000),
    )


_TnGmreOptLineImpLNLPNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpLNLPNP_Object = MibTableColumn
tnGmreOptLineImpLNLPNP = _TnGmreOptLineImpLNLPNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 8),
    _TnGmreOptLineImpLNLPNP_Type()
)
tnGmreOptLineImpLNLPNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLNLPNP.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLNLPNP.setUnits("percentage")


class _TnGmreOptLineImpLOSNRNP_Type(Unsigned32):
    """Custom type tnGmreOptLineImpLOSNRNP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3162277660),
    )


_TnGmreOptLineImpLOSNRNP_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpLOSNRNP_Object = MibTableColumn
tnGmreOptLineImpLOSNRNP = _TnGmreOptLineImpLOSNRNP_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 9),
    _TnGmreOptLineImpLOSNRNP_Type()
)
tnGmreOptLineImpLOSNRNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLOSNRNP.setStatus("current")
_TnGmreOptLineImpLRowStatus_Type = RowStatus
_TnGmreOptLineImpLRowStatus_Object = MibTableColumn
tnGmreOptLineImpLRowStatus = _TnGmreOptLineImpLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 10),
    _TnGmreOptLineImpLRowStatus_Type()
)
tnGmreOptLineImpLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLRowStatus.setStatus("current")


class _TnGmreOptLineImpLPower_Type(Unsigned32):
    """Custom type tnGmreOptLineImpLPower based on Unsigned32"""
    defaultValue = 790

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40500),
    )


_TnGmreOptLineImpLPower_Type.__name__ = "Unsigned32"
_TnGmreOptLineImpLPower_Object = MibTableColumn
tnGmreOptLineImpLPower = _TnGmreOptLineImpLPower_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 11),
    _TnGmreOptLineImpLPower_Type()
)
tnGmreOptLineImpLPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLPower.setStatus("current")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLPower.setUnits("micro-Watts")
_TnGmreOptLineImpLPhaseEncode_Type = TnGmreOptLineImpPhaseEncode
_TnGmreOptLineImpLPhaseEncode_Object = MibTableColumn
tnGmreOptLineImpLPhaseEncode = _TnGmreOptLineImpLPhaseEncode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 11, 2, 1, 12),
    _TnGmreOptLineImpLPhaseEncode_Type()
)
tnGmreOptLineImpLPhaseEncode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOptLineImpLPhaseEncode.setStatus("current")
_TnAsonOmsWavelengthSetL_ObjectIdentity = ObjectIdentity
tnAsonOmsWavelengthSetL = _TnAsonOmsWavelengthSetL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12)
)
_TnGmreOmsWavelengthSetLAttributeTotal_Type = Integer32
_TnGmreOmsWavelengthSetLAttributeTotal_Object = MibScalar
tnGmreOmsWavelengthSetLAttributeTotal = _TnGmreOmsWavelengthSetLAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12, 1),
    _TnGmreOmsWavelengthSetLAttributeTotal_Type()
)
tnGmreOmsWavelengthSetLAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetLAttributeTotal.setStatus("current")
_TnGmreOmsWavelengthSetLTable_Object = MibTable
tnGmreOmsWavelengthSetLTable = _TnGmreOmsWavelengthSetLTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12, 2)
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetLTable.setStatus("current")
_TnGmreOmsWavelengthSetLEntry_Object = MibTableRow
tnGmreOmsWavelengthSetLEntry = _TnGmreOmsWavelengthSetLEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12, 2, 1)
)
tnGmreOmsWavelengthSetLEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnGmreOmsWavelengthLEncodingType"),
)
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthSetLEntry.setStatus("current")


class _TnGmreOmsWavelengthLEncodingType_Type(Integer32):
    """Custom type tnGmreOmsWavelengthLEncodingType based on Integer32"""
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
        *(("nrz", 1),
          ("pdpsk", 2),
          ("coherent", 3),
          ("slotWidth50", 4),
          ("slotWidth62p5", 5),
          ("coherent16qam", 6))
    )


_TnGmreOmsWavelengthLEncodingType_Type.__name__ = "Integer32"
_TnGmreOmsWavelengthLEncodingType_Object = MibTableColumn
tnGmreOmsWavelengthLEncodingType = _TnGmreOmsWavelengthLEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12, 2, 1, 1),
    _TnGmreOmsWavelengthLEncodingType_Type()
)
tnGmreOmsWavelengthLEncodingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthLEncodingType.setStatus("current")


class _TnGmreOmsWavelengthLEncodingBitMap_Type(OctetString):
    """Custom type tnGmreOmsWavelengthLEncodingBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TnGmreOmsWavelengthLEncodingBitMap_Type.__name__ = "OctetString"
_TnGmreOmsWavelengthLEncodingBitMap_Object = MibTableColumn
tnGmreOmsWavelengthLEncodingBitMap = _TnGmreOmsWavelengthLEncodingBitMap_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 12, 2, 1, 2),
    _TnGmreOmsWavelengthLEncodingBitMap_Type()
)
tnGmreOmsWavelengthLEncodingBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreOmsWavelengthLEncodingBitMap.setStatus("current")
_TnAsonClusterObjs_ObjectIdentity = ObjectIdentity
tnAsonClusterObjs = _TnAsonClusterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13)
)
_TnGmreClusterAttributeTotal_Type = Integer32
_TnGmreClusterAttributeTotal_Object = MibScalar
tnGmreClusterAttributeTotal = _TnGmreClusterAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 1),
    _TnGmreClusterAttributeTotal_Type()
)
tnGmreClusterAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreClusterAttributeTotal.setStatus("current")
_TnGmreClusterTable_Object = MibTable
tnGmreClusterTable = _TnGmreClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2)
)
if mibBuilder.loadTexts:
    tnGmreClusterTable.setStatus("current")
_TnGmreClusterEntry_Object = MibTableRow
tnGmreClusterEntry = _TnGmreClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1)
)
tnGmreClusterEntry.setIndexNames(
    (0, "TROPIC-ASON-MIB", "tnGmreClusterFarEndNode"),
)
if mibBuilder.loadTexts:
    tnGmreClusterEntry.setStatus("current")
_TnGmreClusterFarEndNode_Type = OctetString
_TnGmreClusterFarEndNode_Object = MibTableColumn
tnGmreClusterFarEndNode = _TnGmreClusterFarEndNode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 1),
    _TnGmreClusterFarEndNode_Type()
)
tnGmreClusterFarEndNode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreClusterFarEndNode.setStatus("current")
_TnGmreClusterRowStatus_Type = RowStatus
_TnGmreClusterRowStatus_Object = MibTableColumn
tnGmreClusterRowStatus = _TnGmreClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 2),
    _TnGmreClusterRowStatus_Type()
)
tnGmreClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreClusterRowStatus.setStatus("current")


class _TnGmreClusterIpAddress_Type(IpAddress):
    """Custom type tnGmreClusterIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_TnGmreClusterIpAddress_Type.__name__ = "IpAddress"
_TnGmreClusterIpAddress_Object = MibTableColumn
tnGmreClusterIpAddress = _TnGmreClusterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 3),
    _TnGmreClusterIpAddress_Type()
)
tnGmreClusterIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreClusterIpAddress.setStatus("current")


class _TnGmreClusterlinkStatus_Type(Integer32):
    """Custom type tnGmreClusterlinkStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_TnGmreClusterlinkStatus_Type.__name__ = "Integer32"
_TnGmreClusterlinkStatus_Object = MibTableColumn
tnGmreClusterlinkStatus = _TnGmreClusterlinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 4),
    _TnGmreClusterlinkStatus_Type()
)
tnGmreClusterlinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreClusterlinkStatus.setStatus("current")


class _TnGmreClusterInetAddressType_Type(InetAddressType):
    """Custom type tnGmreClusterInetAddressType based on InetAddressType"""
    defaultValue = 0


_TnGmreClusterInetAddressType_Type.__name__ = "InetAddressType"
_TnGmreClusterInetAddressType_Object = MibTableColumn
tnGmreClusterInetAddressType = _TnGmreClusterInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 5),
    _TnGmreClusterInetAddressType_Type()
)
tnGmreClusterInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreClusterInetAddressType.setStatus("current")


class _TnGmreClusterInetAddress_Type(InetAddress):
    """Custom type tnGmreClusterInetAddress based on InetAddress"""
    defaultHexValue = ""


_TnGmreClusterInetAddress_Type.__name__ = "InetAddress"
_TnGmreClusterInetAddress_Object = MibTableColumn
tnGmreClusterInetAddress = _TnGmreClusterInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 13, 2, 1, 6),
    _TnGmreClusterInetAddress_Type()
)
tnGmreClusterInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreClusterInetAddress.setStatus("current")
_TnAsonSubmarineGridMode_ObjectIdentity = ObjectIdentity
tnAsonSubmarineGridMode = _TnAsonSubmarineGridMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 14)
)
_TnGmreSubmarineGridModeTotal_Type = Integer32
_TnGmreSubmarineGridModeTotal_Object = MibScalar
tnGmreSubmarineGridModeTotal = _TnGmreSubmarineGridModeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 14, 1),
    _TnGmreSubmarineGridModeTotal_Type()
)
tnGmreSubmarineGridModeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeTotal.setStatus("current")
_TnGmreSubmarineGridModeTable_Object = MibTable
tnGmreSubmarineGridModeTable = _TnGmreSubmarineGridModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 14, 2)
)
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeTable.setStatus("current")
_TnGmreSubmarineGridModeEntry_Object = MibTableRow
tnGmreSubmarineGridModeEntry = _TnGmreSubmarineGridModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 14, 2, 1)
)
tnGmreSubmarineGridModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeEntry.setStatus("current")


class _TnGmreSubmarineGridModeType_Type(Integer32):
    """Custom type tnGmreSubmarineGridModeType based on Integer32"""
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
        *(("chSpacingNC", 1),
          ("chSpacing6p25", 2),
          ("chSpacing50", 3),
          ("chSpacing100", 4),
          ("chSpacing150", 5),
          ("chSpacing200", 6))
    )


_TnGmreSubmarineGridModeType_Type.__name__ = "Integer32"
_TnGmreSubmarineGridModeType_Object = MibTableColumn
tnGmreSubmarineGridModeType = _TnGmreSubmarineGridModeType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 14, 2, 1, 1),
    _TnGmreSubmarineGridModeType_Type()
)
tnGmreSubmarineGridModeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeType.setStatus("current")
_TnAsonUpLink_ObjectIdentity = ObjectIdentity
tnAsonUpLink = _TnAsonUpLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15)
)
_TnGmreUplinkAttributeTotal_Type = Integer32
_TnGmreUplinkAttributeTotal_Object = MibScalar
tnGmreUplinkAttributeTotal = _TnGmreUplinkAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 1),
    _TnGmreUplinkAttributeTotal_Type()
)
tnGmreUplinkAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreUplinkAttributeTotal.setStatus("current")
_TnGmreUplinkTable_Object = MibTable
tnGmreUplinkTable = _TnGmreUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2)
)
if mibBuilder.loadTexts:
    tnGmreUplinkTable.setStatus("current")
_TnGmreUplinkEntry_Object = MibTableRow
tnGmreUplinkEntry = _TnGmreUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1)
)
tnGmreUplinkEntry.setIndexNames(
    (0, "TROPIC-ASON-MIB", "tnGmreUplinkIndex"),
)
if mibBuilder.loadTexts:
    tnGmreUplinkEntry.setStatus("current")
_TnGmreUplinkIndex_Type = Unsigned32
_TnGmreUplinkIndex_Object = MibTableColumn
tnGmreUplinkIndex = _TnGmreUplinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1, 1),
    _TnGmreUplinkIndex_Type()
)
tnGmreUplinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnGmreUplinkIndex.setStatus("current")
_TnGmreUplink1_Type = InterfaceIndexOrZero
_TnGmreUplink1_Object = MibTableColumn
tnGmreUplink1 = _TnGmreUplink1_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1, 2),
    _TnGmreUplink1_Type()
)
tnGmreUplink1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreUplink1.setStatus("current")
_TnGmreUplink2_Type = InterfaceIndexOrZero
_TnGmreUplink2_Object = MibTableColumn
tnGmreUplink2 = _TnGmreUplink2_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1, 3),
    _TnGmreUplink2_Type()
)
tnGmreUplink2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreUplink2.setStatus("current")
_TnGmreUplinkRowStatus_Type = RowStatus
_TnGmreUplinkRowStatus_Object = MibTableColumn
tnGmreUplinkRowStatus = _TnGmreUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1, 4),
    _TnGmreUplinkRowStatus_Type()
)
tnGmreUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnGmreUplinkRowStatus.setStatus("current")


class _TnGmreUplinkMode_Type(Integer32):
    """Custom type tnGmreUplinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 2))
    )


_TnGmreUplinkMode_Type.__name__ = "Integer32"
_TnGmreUplinkMode_Object = MibTableColumn
tnGmreUplinkMode = _TnGmreUplinkMode_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 15, 2, 1, 5),
    _TnGmreUplinkMode_Type()
)
tnGmreUplinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnGmreUplinkMode.setStatus("current")
_TnAlienOtEntity_ObjectIdentity = ObjectIdentity
tnAlienOtEntity = _TnAlienOtEntity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16)
)
_TnAlienOtEntityAttributeTotal_Type = Integer32
_TnAlienOtEntityAttributeTotal_Object = MibScalar
tnAlienOtEntityAttributeTotal = _TnAlienOtEntityAttributeTotal_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 1),
    _TnAlienOtEntityAttributeTotal_Type()
)
tnAlienOtEntityAttributeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlienOtEntityAttributeTotal.setStatus("current")
_TnAlienOtEntityTable_Object = MibTable
tnAlienOtEntityTable = _TnAlienOtEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2)
)
if mibBuilder.loadTexts:
    tnAlienOtEntityTable.setStatus("current")
_TnAlienOtEntityEntry_Object = MibTableRow
tnAlienOtEntityEntry = _TnAlienOtEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1)
)
tnAlienOtEntityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TROPIC-ASON-MIB", "tnAlienOtEntityIndex"),
)
if mibBuilder.loadTexts:
    tnAlienOtEntityEntry.setStatus("current")
_TnAlienOtEntityIndex_Type = Unsigned32
_TnAlienOtEntityIndex_Object = MibTableColumn
tnAlienOtEntityIndex = _TnAlienOtEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 1),
    _TnAlienOtEntityIndex_Type()
)
tnAlienOtEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnAlienOtEntityIndex.setStatus("current")
_TnAlienOtEntityRowStatus_Type = RowStatus
_TnAlienOtEntityRowStatus_Object = MibTableColumn
tnAlienOtEntityRowStatus = _TnAlienOtEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 2),
    _TnAlienOtEntityRowStatus_Type()
)
tnAlienOtEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntityRowStatus.setStatus("current")


class _TnAlienOtEntityDescription_Type(DisplayString):
    """Custom type tnAlienOtEntityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAlienOtEntityDescription_Type.__name__ = "DisplayString"
_TnAlienOtEntityDescription_Object = MibTableColumn
tnAlienOtEntityDescription = _TnAlienOtEntityDescription_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 3),
    _TnAlienOtEntityDescription_Type()
)
tnAlienOtEntityDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntityDescription.setStatus("current")


class _TnAlienOtEntityFrequencyMHz_Type(Unsigned32):
    """Custom type tnAlienOtEntityFrequencyMHz based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8610000, 9085000),
        ValueRangeConstraint(9130000, 9605000),
    )


_TnAlienOtEntityFrequencyMHz_Type.__name__ = "Unsigned32"
_TnAlienOtEntityFrequencyMHz_Object = MibTableColumn
tnAlienOtEntityFrequencyMHz = _TnAlienOtEntityFrequencyMHz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 4),
    _TnAlienOtEntityFrequencyMHz_Type()
)
tnAlienOtEntityFrequencyMHz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntityFrequencyMHz.setStatus("current")
if mibBuilder.loadTexts:
    tnAlienOtEntityFrequencyMHz.setUnits("MHz")


class _TnAlienOtEntitySlotWidthMHz_Type(Unsigned32):
    """Custom type tnAlienOtEntitySlotWidthMHz based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(37500, 125000),
    )


_TnAlienOtEntitySlotWidthMHz_Type.__name__ = "Unsigned32"
_TnAlienOtEntitySlotWidthMHz_Object = MibTableColumn
tnAlienOtEntitySlotWidthMHz = _TnAlienOtEntitySlotWidthMHz_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 5),
    _TnAlienOtEntitySlotWidthMHz_Type()
)
tnAlienOtEntitySlotWidthMHz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntitySlotWidthMHz.setStatus("current")
if mibBuilder.loadTexts:
    tnAlienOtEntitySlotWidthMHz.setUnits("MHz")


class _TnAlienOtEntityCompModule_Type(TnGmreOptLineImpCompModule):
    """Custom type tnAlienOtEntityCompModule based on TnGmreOptLineImpCompModule"""
    defaultValue = 42


_TnAlienOtEntityCompModule_Type.__name__ = "TnGmreOptLineImpCompModule"
_TnAlienOtEntityCompModule_Object = MibTableColumn
tnAlienOtEntityCompModule = _TnAlienOtEntityCompModule_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 6),
    _TnAlienOtEntityCompModule_Type()
)
tnAlienOtEntityCompModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntityCompModule.setStatus("current")


class _TnAlienOtEntityProfileId_Type(Unsigned32):
    """Custom type tnAlienOtEntityProfileId based on Unsigned32"""
    defaultValue = 99999


_TnAlienOtEntityProfileId_Type.__name__ = "Unsigned32"
_TnAlienOtEntityProfileId_Object = MibTableColumn
tnAlienOtEntityProfileId = _TnAlienOtEntityProfileId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 7),
    _TnAlienOtEntityProfileId_Type()
)
tnAlienOtEntityProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAlienOtEntityProfileId.setStatus("current")


class _TnAlienOtEntityXcId_Type(Unsigned32):
    """Custom type tnAlienOtEntityXcId based on Unsigned32"""
    defaultValue = 0


_TnAlienOtEntityXcId_Type.__name__ = "Unsigned32"
_TnAlienOtEntityXcId_Object = MibTableColumn
tnAlienOtEntityXcId = _TnAlienOtEntityXcId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 8),
    _TnAlienOtEntityXcId_Type()
)
tnAlienOtEntityXcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlienOtEntityXcId.setStatus("current")


class _TnAlienOtEntityXcIdAdd_Type(Unsigned32):
    """Custom type tnAlienOtEntityXcIdAdd based on Unsigned32"""
    defaultValue = 0


_TnAlienOtEntityXcIdAdd_Type.__name__ = "Unsigned32"
_TnAlienOtEntityXcIdAdd_Object = MibTableColumn
tnAlienOtEntityXcIdAdd = _TnAlienOtEntityXcIdAdd_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 9),
    _TnAlienOtEntityXcIdAdd_Type()
)
tnAlienOtEntityXcIdAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlienOtEntityXcIdAdd.setStatus("current")


class _TnAlienOtEntityXcIdDrop_Type(Unsigned32):
    """Custom type tnAlienOtEntityXcIdDrop based on Unsigned32"""
    defaultValue = 0


_TnAlienOtEntityXcIdDrop_Type.__name__ = "Unsigned32"
_TnAlienOtEntityXcIdDrop_Object = MibTableColumn
tnAlienOtEntityXcIdDrop = _TnAlienOtEntityXcIdDrop_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 2, 16, 2, 1, 10),
    _TnAlienOtEntityXcIdDrop_Type()
)
tnAlienOtEntityXcIdDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAlienOtEntityXcIdDrop.setStatus("current")

# Managed Objects groups

tnAsonGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 1)
)
tnAsonGlobalGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreNodeIpAddr"),
        ("TROPIC-ASON-MIB", "tnGmreNodeSubMask"),
        ("TROPIC-ASON-MIB", "tnGmreNotifyIpAddr"),
        ("TROPIC-ASON-MIB", "tnGmreNotifySubMask"),
        ("TROPIC-ASON-MIB", "tnGmreDiscoveryMode"),
        ("TROPIC-ASON-MIB", "tnGmreAsonItuBandMode"),
        ("TROPIC-ASON-MIB", "tnGmreClusterMode"))
)
if mibBuilder.loadTexts:
    tnAsonGlobalGroup.setStatus("current")

tnAsonIorGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 2)
)
tnAsonIorGlobalGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreCorbaName"),
        ("TROPIC-ASON-MIB", "tnGmreCorbaHostIpAddress"),
        ("TROPIC-ASON-MIB", "tnGmreCorbaIor"),
        ("TROPIC-ASON-MIB", "tnGmreCorbaIorIPv6"))
)
if mibBuilder.loadTexts:
    tnAsonIorGlobalGroup.setStatus("current")

tnAsonOmsLineImpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 3)
)
tnAsonOmsLineImpScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsLineImpAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpScalarsGroup.setStatus("current")

tnAsonOmsLineImpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 4)
)
tnAsonOmsLineImpGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOmsLineImpMaxAlwCh"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpPMD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpAlcMode"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpDcuFree"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpCD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpFiberType"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpPDL"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpCD1546"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImp1830lxdcm"))
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpGroup.setStatus("current")

tnAsonOptLineImpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 5)
)
tnAsonOptLineImpScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOptLineImpAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpScalarsGroup.setStatus("current")

tnAsonOptLineImpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 6)
)
tnAsonOptLineImpGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOptLineImpBitRate"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpEncoding"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpCompModule"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpFecMode"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpNLP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpOSNR"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpNLPNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpOSNRNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpRowStatus"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpPower"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpPhaseEncode"))
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpGroup.setStatus("current")

tnAsonTopoAlarmScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 7)
)
tnAsonTopoAlarmScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonTopoAlarmAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmScalarsGroup.setStatus("current")

tnAsonTopoAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 8)
)
tnAsonTopoAlarmGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonTopoClearAlarm")
)
if mibBuilder.loadTexts:
    tnAsonTopoAlarmGroup.setStatus("current")

tnAsonFeasibilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 9)
)
tnAsonFeasibilityGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonFeasibilityCommand"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemoteHostIp"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityStatus"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityLastTransferredVersion"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityProtocol"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityUserId"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityPassword"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemoteInetAddressType"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityRemoteInetAddress"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityPort"))
)
if mibBuilder.loadTexts:
    tnAsonFeasibilityGroup.setStatus("current")

tnAsonMgracdScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 10)
)
tnAsonMgracdScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAsonMgracdAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonMgracdScalarsGroup.setStatus("current")

tnAsonMgracdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 11)
)
tnAsonMgracdGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonOchMgracd"),
        ("TROPIC-ASON-MIB", "tnAsonOmsochifMgracd"),
        ("TROPIC-ASON-MIB", "tnAsonOtsMgracd"))
)
if mibBuilder.loadTexts:
    tnAsonMgracdGroup.setStatus("current")

tnAsonOmsWavelengthSetScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 12)
)
tnAsonOmsWavelengthSetScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthSetAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetScalarsGroup.setStatus("current")

tnAsonOmsWavelengthSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 13)
)
tnAsonOmsWavelengthSetGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthEncodingBitMap")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetGroup.setStatus("current")

tnAsonSnapshotScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 14)
)
tnAsonSnapshotScalarsGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonSnapshotRemoteHostIp"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotProtocol"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotUserId"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotPassword"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRootRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotAttributeTotal"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRemoteInetAddressType"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRemoteInetAddress"))
)
if mibBuilder.loadTexts:
    tnAsonSnapshotScalarsGroup.setStatus("current")

tnAsonSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 15)
)
tnAsonSnapshotGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonSnapshotStatus"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRemotePath"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotRowStatus"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotFilename"))
)
if mibBuilder.loadTexts:
    tnAsonSnapshotGroup.setStatus("current")

tnAsonOmsLineImpLScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 16)
)
tnAsonOmsLineImpLScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpLScalarsGroup.setStatus("current")

tnAsonOmsLineImpLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 17)
)
tnAsonOmsLineImpLGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOmsLineImpLMaxAlwCh"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLPMD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLAlcMode"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLDcuFree"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLCD"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLFiberType"),
        ("TROPIC-ASON-MIB", "tnGmreOmsLineImpLPDL"))
)
if mibBuilder.loadTexts:
    tnAsonOmsLineImpLGroup.setStatus("current")

tnAsonOptLineImpLScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 18)
)
tnAsonOptLineImpLScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOptLineImpLAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpLScalarsGroup.setStatus("current")

tnAsonOptLineImpLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 19)
)
tnAsonOptLineImpLGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreOptLineImpLBitRate"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLEncoding"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLCompModule"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLFecMode"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLNLP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLOSNR"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLNLPNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLOSNRNP"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLRowStatus"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLPower"),
        ("TROPIC-ASON-MIB", "tnGmreOptLineImpLPhaseEncode"))
)
if mibBuilder.loadTexts:
    tnAsonOptLineImpLGroup.setStatus("current")

tnAsonOmsWavelengthSetLScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 20)
)
tnAsonOmsWavelengthSetLScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthSetLAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetLScalarsGroup.setStatus("current")

tnAsonOmsWavelengthSetLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 21)
)
tnAsonOmsWavelengthSetLGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreOmsWavelengthLEncodingBitMap")
)
if mibBuilder.loadTexts:
    tnAsonOmsWavelengthSetLGroup.setStatus("current")

tnAsonClusterScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 22)
)
tnAsonClusterScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreClusterAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAsonClusterScalarsGroup.setStatus("current")

tnAsonClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 23)
)
tnAsonClusterGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreClusterRowStatus"),
        ("TROPIC-ASON-MIB", "tnGmreClusterIpAddress"),
        ("TROPIC-ASON-MIB", "tnGmreClusterlinkStatus"),
        ("TROPIC-ASON-MIB", "tnGmreClusterInetAddressType"),
        ("TROPIC-ASON-MIB", "tnGmreClusterInetAddress"))
)
if mibBuilder.loadTexts:
    tnAsonClusterGroup.setStatus("current")

tnGmreSubmarineGridModeScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 24)
)
tnGmreSubmarineGridModeScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreSubmarineGridModeTotal")
)
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeScalarsGroup.setStatus("current")

tnGmreSubmarineGridModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 25)
)
tnGmreSubmarineGridModeGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreSubmarineGridModeType")
)
if mibBuilder.loadTexts:
    tnGmreSubmarineGridModeGroup.setStatus("current")

tnGmreUplinkAttributeScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 26)
)
tnGmreUplinkAttributeScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnGmreUplinkAttributeTotal")
)
if mibBuilder.loadTexts:
    tnGmreUplinkAttributeScalarsGroup.setStatus("current")

tnGmreUplinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 27)
)
tnGmreUplinkGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnGmreUplink1"),
        ("TROPIC-ASON-MIB", "tnGmreUplink2"),
        ("TROPIC-ASON-MIB", "tnGmreUplinkRowStatus"),
        ("TROPIC-ASON-MIB", "tnGmreUplinkMode"))
)
if mibBuilder.loadTexts:
    tnGmreUplinkGroup.setStatus("current")

tnAlienOtEntityScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 28)
)
tnAlienOtEntityScalarsGroup.setObjects(
    ("TROPIC-ASON-MIB", "tnAlienOtEntityAttributeTotal")
)
if mibBuilder.loadTexts:
    tnAlienOtEntityScalarsGroup.setStatus("current")

tnAlienOtEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 1, 29)
)
tnAlienOtEntityGroup.setObjects(
      *(("TROPIC-ASON-MIB", "tnAlienOtEntityRowStatus"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityDescription"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityFrequencyMHz"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntitySlotWidthMHz"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityCompModule"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityProfileId"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityXcId"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityXcIdAdd"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityXcIdDrop"))
)
if mibBuilder.loadTexts:
    tnAlienOtEntityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAsonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 1, 9, 1, 2, 1)
)
tnAsonCompliance.setObjects(
      *(("TROPIC-ASON-MIB", "tnAsonGlobalGroup"),
        ("TROPIC-ASON-MIB", "tnAsonIorGlobalGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpGroup"),
        ("TROPIC-ASON-MIB", "tnAsonTopoAlarmScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonTopoAlarmGroup"),
        ("TROPIC-ASON-MIB", "tnAsonFeasibilityGroup"),
        ("TROPIC-ASON-MIB", "tnAsonMgracdScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonMgracdGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetGroup"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonSnapshotGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpLScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsLineImpLGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpLScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOptLineImpLGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetLScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonOmsWavelengthSetLGroup"),
        ("TROPIC-ASON-MIB", "tnAsonClusterScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAsonClusterGroup"),
        ("TROPIC-ASON-MIB", "tnGmreSubmarineGridModeScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnGmreSubmarineGridModeGroup"),
        ("TROPIC-ASON-MIB", "tnGmreUplinkAttributeScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnGmreUplinkGroup"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityScalarsGroup"),
        ("TROPIC-ASON-MIB", "tnAlienOtEntityGroup"))
)
if mibBuilder.loadTexts:
    tnAsonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ASON-MIB",
    **{"AluWdmAccessControlDevice": AluWdmAccessControlDevice,
       "TnGmreOptLineImpEncoding": TnGmreOptLineImpEncoding,
       "TnGmreOptLineImpCompModule": TnGmreOptLineImpCompModule,
       "TnGmreOptLineImpPhaseEncode": TnGmreOptLineImpPhaseEncode,
       "tnAsonMibModule": tnAsonMibModule,
       "tnAsonConf": tnAsonConf,
       "tnAsonGroups": tnAsonGroups,
       "tnAsonGlobalGroup": tnAsonGlobalGroup,
       "tnAsonIorGlobalGroup": tnAsonIorGlobalGroup,
       "tnAsonOmsLineImpScalarsGroup": tnAsonOmsLineImpScalarsGroup,
       "tnAsonOmsLineImpGroup": tnAsonOmsLineImpGroup,
       "tnAsonOptLineImpScalarsGroup": tnAsonOptLineImpScalarsGroup,
       "tnAsonOptLineImpGroup": tnAsonOptLineImpGroup,
       "tnAsonTopoAlarmScalarsGroup": tnAsonTopoAlarmScalarsGroup,
       "tnAsonTopoAlarmGroup": tnAsonTopoAlarmGroup,
       "tnAsonFeasibilityGroup": tnAsonFeasibilityGroup,
       "tnAsonMgracdScalarsGroup": tnAsonMgracdScalarsGroup,
       "tnAsonMgracdGroup": tnAsonMgracdGroup,
       "tnAsonOmsWavelengthSetScalarsGroup": tnAsonOmsWavelengthSetScalarsGroup,
       "tnAsonOmsWavelengthSetGroup": tnAsonOmsWavelengthSetGroup,
       "tnAsonSnapshotScalarsGroup": tnAsonSnapshotScalarsGroup,
       "tnAsonSnapshotGroup": tnAsonSnapshotGroup,
       "tnAsonOmsLineImpLScalarsGroup": tnAsonOmsLineImpLScalarsGroup,
       "tnAsonOmsLineImpLGroup": tnAsonOmsLineImpLGroup,
       "tnAsonOptLineImpLScalarsGroup": tnAsonOptLineImpLScalarsGroup,
       "tnAsonOptLineImpLGroup": tnAsonOptLineImpLGroup,
       "tnAsonOmsWavelengthSetLScalarsGroup": tnAsonOmsWavelengthSetLScalarsGroup,
       "tnAsonOmsWavelengthSetLGroup": tnAsonOmsWavelengthSetLGroup,
       "tnAsonClusterScalarsGroup": tnAsonClusterScalarsGroup,
       "tnAsonClusterGroup": tnAsonClusterGroup,
       "tnGmreSubmarineGridModeScalarsGroup": tnGmreSubmarineGridModeScalarsGroup,
       "tnGmreSubmarineGridModeGroup": tnGmreSubmarineGridModeGroup,
       "tnGmreUplinkAttributeScalarsGroup": tnGmreUplinkAttributeScalarsGroup,
       "tnGmreUplinkGroup": tnGmreUplinkGroup,
       "tnAlienOtEntityScalarsGroup": tnAlienOtEntityScalarsGroup,
       "tnAlienOtEntityGroup": tnAlienOtEntityGroup,
       "tnAsonCompliances": tnAsonCompliances,
       "tnAsonCompliance": tnAsonCompliance,
       "tnAsonObjs": tnAsonObjs,
       "tnAsonGlobal": tnAsonGlobal,
       "tnGmreNodeIpAddr": tnGmreNodeIpAddr,
       "tnGmreNodeSubMask": tnGmreNodeSubMask,
       "tnGmreNotifyIpAddr": tnGmreNotifyIpAddr,
       "tnGmreNotifySubMask": tnGmreNotifySubMask,
       "tnGmreDiscoveryMode": tnGmreDiscoveryMode,
       "tnGmreAsonItuBandMode": tnGmreAsonItuBandMode,
       "tnGmreClusterMode": tnGmreClusterMode,
       "tnAsonIorGlobal": tnAsonIorGlobal,
       "tnGmreCorbaName": tnGmreCorbaName,
       "tnGmreCorbaHostIpAddress": tnGmreCorbaHostIpAddress,
       "tnGmreCorbaIor": tnGmreCorbaIor,
       "tnGmreCorbaIorIPv6": tnGmreCorbaIorIPv6,
       "tnAsonOmsLineImp": tnAsonOmsLineImp,
       "tnGmreOmsLineImpAttributeTotal": tnGmreOmsLineImpAttributeTotal,
       "tnGmreOmsLineImpTable": tnGmreOmsLineImpTable,
       "tnGmreOmsLineImpEntry": tnGmreOmsLineImpEntry,
       "tnGmreOmsLineImpMaxAlwCh": tnGmreOmsLineImpMaxAlwCh,
       "tnGmreOmsLineImpPMD": tnGmreOmsLineImpPMD,
       "tnGmreOmsLineImpAlcMode": tnGmreOmsLineImpAlcMode,
       "tnGmreOmsLineImpDcuFree": tnGmreOmsLineImpDcuFree,
       "tnGmreOmsLineImpCD": tnGmreOmsLineImpCD,
       "tnGmreOmsLineImpFiberType": tnGmreOmsLineImpFiberType,
       "tnGmreOmsLineImpPDL": tnGmreOmsLineImpPDL,
       "tnGmreOmsLineImpCD1546": tnGmreOmsLineImpCD1546,
       "tnGmreOmsLineImp1830lxdcm": tnGmreOmsLineImp1830lxdcm,
       "tnAsonOptLineImp": tnAsonOptLineImp,
       "tnGmreOptLineImpAttributeTotal": tnGmreOptLineImpAttributeTotal,
       "tnGmreOptLineImpTable": tnGmreOptLineImpTable,
       "tnGmreOptLineImpEntry": tnGmreOptLineImpEntry,
       "tnGmreOptLineImpIndex": tnGmreOptLineImpIndex,
       "tnGmreOptLineImpBitRate": tnGmreOptLineImpBitRate,
       "tnGmreOptLineImpEncoding": tnGmreOptLineImpEncoding,
       "tnGmreOptLineImpCompModule": tnGmreOptLineImpCompModule,
       "tnGmreOptLineImpFecMode": tnGmreOptLineImpFecMode,
       "tnGmreOptLineImpNLP": tnGmreOptLineImpNLP,
       "tnGmreOptLineImpOSNR": tnGmreOptLineImpOSNR,
       "tnGmreOptLineImpNLPNP": tnGmreOptLineImpNLPNP,
       "tnGmreOptLineImpOSNRNP": tnGmreOptLineImpOSNRNP,
       "tnGmreOptLineImpRowStatus": tnGmreOptLineImpRowStatus,
       "tnGmreOptLineImpPower": tnGmreOptLineImpPower,
       "tnGmreOptLineImpPhaseEncode": tnGmreOptLineImpPhaseEncode,
       "tnAsonTopoAlarm": tnAsonTopoAlarm,
       "tnAsonTopoAlarmAttributeTotal": tnAsonTopoAlarmAttributeTotal,
       "tnAsonTopoAlarmTable": tnAsonTopoAlarmTable,
       "tnAsonTopoAlarmEntry": tnAsonTopoAlarmEntry,
       "tnAsonTopoClearAlarm": tnAsonTopoClearAlarm,
       "tnAsonFeasibility": tnAsonFeasibility,
       "tnAsonFeasibilityCommand": tnAsonFeasibilityCommand,
       "tnAsonFeasibilityRemoteHostIp": tnAsonFeasibilityRemoteHostIp,
       "tnAsonFeasibilityRemotePath": tnAsonFeasibilityRemotePath,
       "tnAsonFeasibilityStatus": tnAsonFeasibilityStatus,
       "tnAsonFeasibilityLastTransferredVersion": tnAsonFeasibilityLastTransferredVersion,
       "tnAsonFeasibilityProtocol": tnAsonFeasibilityProtocol,
       "tnAsonFeasibilityUserId": tnAsonFeasibilityUserId,
       "tnAsonFeasibilityPassword": tnAsonFeasibilityPassword,
       "tnAsonFeasibilityRemoteInetAddressType": tnAsonFeasibilityRemoteInetAddressType,
       "tnAsonFeasibilityRemoteInetAddress": tnAsonFeasibilityRemoteInetAddress,
       "tnAsonFeasibilityPort": tnAsonFeasibilityPort,
       "tnAsonMgracdInfo": tnAsonMgracdInfo,
       "tnAsonMgracdAttributeTotal": tnAsonMgracdAttributeTotal,
       "tnAsonMgracdTable": tnAsonMgracdTable,
       "tnAsonMgracdEntry": tnAsonMgracdEntry,
       "tnAsonOchMgracd": tnAsonOchMgracd,
       "tnAsonOmsochifMgracd": tnAsonOmsochifMgracd,
       "tnAsonOtsMgracd": tnAsonOtsMgracd,
       "tnAsonOmsWavelengthSet": tnAsonOmsWavelengthSet,
       "tnGmreOmsWavelengthSetAttributeTotal": tnGmreOmsWavelengthSetAttributeTotal,
       "tnGmreOmsWavelengthSetTable": tnGmreOmsWavelengthSetTable,
       "tnGmreOmsWavelengthSetEntry": tnGmreOmsWavelengthSetEntry,
       "tnGmreOmsWavelengthEncodingType": tnGmreOmsWavelengthEncodingType,
       "tnGmreOmsWavelengthEncodingBitMap": tnGmreOmsWavelengthEncodingBitMap,
       "tnAsonSnapshot": tnAsonSnapshot,
       "tnAsonSnapshotRemoteHostIp": tnAsonSnapshotRemoteHostIp,
       "tnAsonSnapshotProtocol": tnAsonSnapshotProtocol,
       "tnAsonSnapshotUserId": tnAsonSnapshotUserId,
       "tnAsonSnapshotPassword": tnAsonSnapshotPassword,
       "tnAsonSnapshotRootRemotePath": tnAsonSnapshotRootRemotePath,
       "tnAsonSnapshotAttributeTotal": tnAsonSnapshotAttributeTotal,
       "tnAsonSnapshotTable": tnAsonSnapshotTable,
       "tnAsonSnapshotEntry": tnAsonSnapshotEntry,
       "tnAsonSnapshotTime": tnAsonSnapshotTime,
       "tnAsonSnapshotStatus": tnAsonSnapshotStatus,
       "tnAsonSnapshotRemotePath": tnAsonSnapshotRemotePath,
       "tnAsonSnapshotRowStatus": tnAsonSnapshotRowStatus,
       "tnAsonSnapshotFilename": tnAsonSnapshotFilename,
       "tnAsonSnapshotRemoteInetAddressType": tnAsonSnapshotRemoteInetAddressType,
       "tnAsonSnapshotRemoteInetAddress": tnAsonSnapshotRemoteInetAddress,
       "tnAsonOmsLineImpL": tnAsonOmsLineImpL,
       "tnGmreOmsLineImpLAttributeTotal": tnGmreOmsLineImpLAttributeTotal,
       "tnGmreOmsLineImpLTable": tnGmreOmsLineImpLTable,
       "tnGmreOmsLineImpLEntry": tnGmreOmsLineImpLEntry,
       "tnGmreOmsLineImpLMaxAlwCh": tnGmreOmsLineImpLMaxAlwCh,
       "tnGmreOmsLineImpLPMD": tnGmreOmsLineImpLPMD,
       "tnGmreOmsLineImpLAlcMode": tnGmreOmsLineImpLAlcMode,
       "tnGmreOmsLineImpLDcuFree": tnGmreOmsLineImpLDcuFree,
       "tnGmreOmsLineImpLCD": tnGmreOmsLineImpLCD,
       "tnGmreOmsLineImpLFiberType": tnGmreOmsLineImpLFiberType,
       "tnGmreOmsLineImpLPDL": tnGmreOmsLineImpLPDL,
       "tnAsonOptLineImpL": tnAsonOptLineImpL,
       "tnGmreOptLineImpLAttributeTotal": tnGmreOptLineImpLAttributeTotal,
       "tnGmreOptLineImpLTable": tnGmreOptLineImpLTable,
       "tnGmreOptLineImpLEntry": tnGmreOptLineImpLEntry,
       "tnGmreOptLineImpLIndex": tnGmreOptLineImpLIndex,
       "tnGmreOptLineImpLBitRate": tnGmreOptLineImpLBitRate,
       "tnGmreOptLineImpLEncoding": tnGmreOptLineImpLEncoding,
       "tnGmreOptLineImpLCompModule": tnGmreOptLineImpLCompModule,
       "tnGmreOptLineImpLFecMode": tnGmreOptLineImpLFecMode,
       "tnGmreOptLineImpLNLP": tnGmreOptLineImpLNLP,
       "tnGmreOptLineImpLOSNR": tnGmreOptLineImpLOSNR,
       "tnGmreOptLineImpLNLPNP": tnGmreOptLineImpLNLPNP,
       "tnGmreOptLineImpLOSNRNP": tnGmreOptLineImpLOSNRNP,
       "tnGmreOptLineImpLRowStatus": tnGmreOptLineImpLRowStatus,
       "tnGmreOptLineImpLPower": tnGmreOptLineImpLPower,
       "tnGmreOptLineImpLPhaseEncode": tnGmreOptLineImpLPhaseEncode,
       "tnAsonOmsWavelengthSetL": tnAsonOmsWavelengthSetL,
       "tnGmreOmsWavelengthSetLAttributeTotal": tnGmreOmsWavelengthSetLAttributeTotal,
       "tnGmreOmsWavelengthSetLTable": tnGmreOmsWavelengthSetLTable,
       "tnGmreOmsWavelengthSetLEntry": tnGmreOmsWavelengthSetLEntry,
       "tnGmreOmsWavelengthLEncodingType": tnGmreOmsWavelengthLEncodingType,
       "tnGmreOmsWavelengthLEncodingBitMap": tnGmreOmsWavelengthLEncodingBitMap,
       "tnAsonClusterObjs": tnAsonClusterObjs,
       "tnGmreClusterAttributeTotal": tnGmreClusterAttributeTotal,
       "tnGmreClusterTable": tnGmreClusterTable,
       "tnGmreClusterEntry": tnGmreClusterEntry,
       "tnGmreClusterFarEndNode": tnGmreClusterFarEndNode,
       "tnGmreClusterRowStatus": tnGmreClusterRowStatus,
       "tnGmreClusterIpAddress": tnGmreClusterIpAddress,
       "tnGmreClusterlinkStatus": tnGmreClusterlinkStatus,
       "tnGmreClusterInetAddressType": tnGmreClusterInetAddressType,
       "tnGmreClusterInetAddress": tnGmreClusterInetAddress,
       "tnAsonSubmarineGridMode": tnAsonSubmarineGridMode,
       "tnGmreSubmarineGridModeTotal": tnGmreSubmarineGridModeTotal,
       "tnGmreSubmarineGridModeTable": tnGmreSubmarineGridModeTable,
       "tnGmreSubmarineGridModeEntry": tnGmreSubmarineGridModeEntry,
       "tnGmreSubmarineGridModeType": tnGmreSubmarineGridModeType,
       "tnAsonUpLink": tnAsonUpLink,
       "tnGmreUplinkAttributeTotal": tnGmreUplinkAttributeTotal,
       "tnGmreUplinkTable": tnGmreUplinkTable,
       "tnGmreUplinkEntry": tnGmreUplinkEntry,
       "tnGmreUplinkIndex": tnGmreUplinkIndex,
       "tnGmreUplink1": tnGmreUplink1,
       "tnGmreUplink2": tnGmreUplink2,
       "tnGmreUplinkRowStatus": tnGmreUplinkRowStatus,
       "tnGmreUplinkMode": tnGmreUplinkMode,
       "tnAlienOtEntity": tnAlienOtEntity,
       "tnAlienOtEntityAttributeTotal": tnAlienOtEntityAttributeTotal,
       "tnAlienOtEntityTable": tnAlienOtEntityTable,
       "tnAlienOtEntityEntry": tnAlienOtEntityEntry,
       "tnAlienOtEntityIndex": tnAlienOtEntityIndex,
       "tnAlienOtEntityRowStatus": tnAlienOtEntityRowStatus,
       "tnAlienOtEntityDescription": tnAlienOtEntityDescription,
       "tnAlienOtEntityFrequencyMHz": tnAlienOtEntityFrequencyMHz,
       "tnAlienOtEntitySlotWidthMHz": tnAlienOtEntitySlotWidthMHz,
       "tnAlienOtEntityCompModule": tnAlienOtEntityCompModule,
       "tnAlienOtEntityProfileId": tnAlienOtEntityProfileId,
       "tnAlienOtEntityXcId": tnAlienOtEntityXcId,
       "tnAlienOtEntityXcIdAdd": tnAlienOtEntityXcIdAdd,
       "tnAlienOtEntityXcIdDrop": tnAlienOtEntityXcIdDrop}
)
