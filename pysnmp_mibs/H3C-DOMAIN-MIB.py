# SNMP MIB module (H3C-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-DOMAIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:56 2025
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

h3cDomain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46)
)
if mibBuilder.loadTexts:
    h3cDomain.setRevisions(
        ("2017-10-13 00:00",
         "2017-06-03 00:00",
         "2013-11-25 00:00",
         "2013-04-25 00:00",
         "2013-02-28 00:00",
         "2012-10-15 00:00",
         "2012-05-20 00:00",
         "2009-08-05 00:00",
         "2008-12-30 00:00",
         "2008-11-25 00:00",
         "2007-03-07 00:00",
         "2006-03-27 00:00",
         "2005-06-30 00:00",
         "2005-03-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cModeOfDomainScheme(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2),
          ("radius", 3),
          ("tacacs", 4),
          ("ldap", 5))
    )



class H3cAAATypeDomainScheme(TextualConvention, Integer32):
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
        *(("accounting", 1),
          ("authentication", 2),
          ("authorization", 3),
          ("none", 4))
    )



class H3cAccessModeofDomainScheme(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("login", 2),
          ("lanAccess", 3),
          ("portal", 4),
          ("ppp", 5),
          ("gcm", 6),
          ("dvpn", 7),
          ("dhcp", 8),
          ("voice", 9),
          ("superauthen", 10),
          ("command", 11),
          ("reserved", 12))
    )



# MIB Managed Objects in the order of their OIDs

_H3cDomainControl_ObjectIdentity = ObjectIdentity
h3cDomainControl = _H3cDomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 1)
)


class _H3cDomainDefault_Type(OctetString):
    """Custom type h3cDomainDefault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cDomainDefault_Type.__name__ = "OctetString"
_H3cDomainDefault_Object = MibScalar
h3cDomainDefault = _H3cDomainDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 1, 1),
    _H3cDomainDefault_Type()
)
h3cDomainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDomainDefault.setStatus("current")
_H3cDomainTables_ObjectIdentity = ObjectIdentity
h3cDomainTables = _H3cDomainTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2)
)
_H3cDomainInfoTable_Object = MibTable
h3cDomainInfoTable = _H3cDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDomainInfoTable.setStatus("current")
_H3cDomainInfoEntry_Object = MibTableRow
h3cDomainInfoEntry = _H3cDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1)
)
h3cDomainInfoEntry.setIndexNames(
    (0, "H3C-DOMAIN-MIB", "h3cDomainName"),
)
if mibBuilder.loadTexts:
    h3cDomainInfoEntry.setStatus("current")


class _H3cDomainName_Type(OctetString):
    """Custom type h3cDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cDomainName_Type.__name__ = "OctetString"
_H3cDomainName_Object = MibTableColumn
h3cDomainName = _H3cDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 1),
    _H3cDomainName_Type()
)
h3cDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainName.setStatus("current")


class _H3cDomainState_Type(Integer32):
    """Custom type h3cDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_H3cDomainState_Type.__name__ = "Integer32"
_H3cDomainState_Object = MibTableColumn
h3cDomainState = _H3cDomainState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 2),
    _H3cDomainState_Type()
)
h3cDomainState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainState.setStatus("current")
_H3cDomainMaxAccessNum_Type = Integer32
_H3cDomainMaxAccessNum_Object = MibTableColumn
h3cDomainMaxAccessNum = _H3cDomainMaxAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 3),
    _H3cDomainMaxAccessNum_Type()
)
h3cDomainMaxAccessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMaxAccessNum.setStatus("current")


class _H3cDomainVlanAssignMode_Type(Integer32):
    """Custom type h3cDomainVlanAssignMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("string", 2),
          ("vlanlist", 3))
    )


_H3cDomainVlanAssignMode_Type.__name__ = "Integer32"
_H3cDomainVlanAssignMode_Object = MibTableColumn
h3cDomainVlanAssignMode = _H3cDomainVlanAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 4),
    _H3cDomainVlanAssignMode_Type()
)
h3cDomainVlanAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainVlanAssignMode.setStatus("current")
_H3cDomainIdleCutEnable_Type = TruthValue
_H3cDomainIdleCutEnable_Object = MibTableColumn
h3cDomainIdleCutEnable = _H3cDomainIdleCutEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 5),
    _H3cDomainIdleCutEnable_Type()
)
h3cDomainIdleCutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutEnable.setStatus("current")
_H3cDomainIdleCutMaxTime_Type = Integer32
_H3cDomainIdleCutMaxTime_Object = MibTableColumn
h3cDomainIdleCutMaxTime = _H3cDomainIdleCutMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 6),
    _H3cDomainIdleCutMaxTime_Type()
)
h3cDomainIdleCutMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutMaxTime.setStatus("current")


class _H3cDomainIdleCutMinFlow_Type(Integer32):
    """Custom type h3cDomainIdleCutMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240000),
    )


_H3cDomainIdleCutMinFlow_Type.__name__ = "Integer32"
_H3cDomainIdleCutMinFlow_Object = MibTableColumn
h3cDomainIdleCutMinFlow = _H3cDomainIdleCutMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 7),
    _H3cDomainIdleCutMinFlow_Type()
)
h3cDomainIdleCutMinFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIdleCutMinFlow.setStatus("current")
_H3cDomainMessengerEnable_Type = TruthValue
_H3cDomainMessengerEnable_Object = MibTableColumn
h3cDomainMessengerEnable = _H3cDomainMessengerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 8),
    _H3cDomainMessengerEnable_Type()
)
h3cDomainMessengerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerEnable.setStatus("current")


class _H3cDomainMessengerLimitTime_Type(Integer32):
    """Custom type h3cDomainMessengerLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_H3cDomainMessengerLimitTime_Type.__name__ = "Integer32"
_H3cDomainMessengerLimitTime_Object = MibTableColumn
h3cDomainMessengerLimitTime = _H3cDomainMessengerLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 9),
    _H3cDomainMessengerLimitTime_Type()
)
h3cDomainMessengerLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerLimitTime.setStatus("current")


class _H3cDomainMessengerSpanTime_Type(Integer32):
    """Custom type h3cDomainMessengerSpanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_H3cDomainMessengerSpanTime_Type.__name__ = "Integer32"
_H3cDomainMessengerSpanTime_Object = MibTableColumn
h3cDomainMessengerSpanTime = _H3cDomainMessengerSpanTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 10),
    _H3cDomainMessengerSpanTime_Type()
)
h3cDomainMessengerSpanTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainMessengerSpanTime.setStatus("current")
_H3cDomainSelfServiceEnable_Type = TruthValue
_H3cDomainSelfServiceEnable_Object = MibTableColumn
h3cDomainSelfServiceEnable = _H3cDomainSelfServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 11),
    _H3cDomainSelfServiceEnable_Type()
)
h3cDomainSelfServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSelfServiceEnable.setStatus("current")


class _H3cDomainSelfServiceURL_Type(OctetString):
    """Custom type h3cDomainSelfServiceURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDomainSelfServiceURL_Type.__name__ = "OctetString"
_H3cDomainSelfServiceURL_Object = MibTableColumn
h3cDomainSelfServiceURL = _H3cDomainSelfServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 12),
    _H3cDomainSelfServiceURL_Type()
)
h3cDomainSelfServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSelfServiceURL.setStatus("current")


class _H3cDomainAccFailureAction_Type(Integer32):
    """Custom type h3cDomainAccFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("reject", 2))
    )


_H3cDomainAccFailureAction_Type.__name__ = "Integer32"
_H3cDomainAccFailureAction_Object = MibTableColumn
h3cDomainAccFailureAction = _H3cDomainAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 13),
    _H3cDomainAccFailureAction_Type()
)
h3cDomainAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAccFailureAction.setStatus("current")
_H3cDomainRowStatus_Type = RowStatus
_H3cDomainRowStatus_Object = MibTableColumn
h3cDomainRowStatus = _H3cDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 14),
    _H3cDomainRowStatus_Type()
)
h3cDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainRowStatus.setStatus("current")
_H3cDomainCurrentAccessNum_Type = Integer32
_H3cDomainCurrentAccessNum_Object = MibTableColumn
h3cDomainCurrentAccessNum = _H3cDomainCurrentAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 15),
    _H3cDomainCurrentAccessNum_Type()
)
h3cDomainCurrentAccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainCurrentAccessNum.setStatus("current")
_H3cDomainIdleCutTime_Type = TimeTicks
_H3cDomainIdleCutTime_Object = MibTableColumn
h3cDomainIdleCutTime = _H3cDomainIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 16),
    _H3cDomainIdleCutTime_Type()
)
h3cDomainIdleCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIdleCutTime.setStatus("current")


class _H3cDomainServiceType_Type(Integer32):
    """Custom type h3cDomainServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hsi", 1),
          ("stb", 2),
          ("voip", 3))
    )


_H3cDomainServiceType_Type.__name__ = "Integer32"
_H3cDomainServiceType_Object = MibTableColumn
h3cDomainServiceType = _H3cDomainServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 17),
    _H3cDomainServiceType_Type()
)
h3cDomainServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainServiceType.setStatus("current")


class _H3cDomainIpPoolName_Type(OctetString):
    """Custom type h3cDomainIpPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cDomainIpPoolName_Type.__name__ = "OctetString"
_H3cDomainIpPoolName_Object = MibTableColumn
h3cDomainIpPoolName = _H3cDomainIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 18),
    _H3cDomainIpPoolName_Type()
)
h3cDomainIpPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolName.setStatus("current")


class _H3cDomainIpv6PoolName_Type(OctetString):
    """Custom type h3cDomainIpv6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cDomainIpv6PoolName_Type.__name__ = "OctetString"
_H3cDomainIpv6PoolName_Object = MibTableColumn
h3cDomainIpv6PoolName = _H3cDomainIpv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 1, 1, 19),
    _H3cDomainIpv6PoolName_Type()
)
h3cDomainIpv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpv6PoolName.setStatus("current")
_H3cDomainSchemeTable_Object = MibTable
h3cDomainSchemeTable = _H3cDomainSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDomainSchemeTable.setStatus("current")
_H3cDomainSchemeEntry_Object = MibTableRow
h3cDomainSchemeEntry = _H3cDomainSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1)
)
h3cDomainSchemeEntry.setIndexNames(
    (0, "H3C-DOMAIN-MIB", "h3cDomainName"),
    (0, "H3C-DOMAIN-MIB", "h3cDomainSchemeIndex"),
)
if mibBuilder.loadTexts:
    h3cDomainSchemeEntry.setStatus("current")
_H3cDomainSchemeIndex_Type = Integer32
_H3cDomainSchemeIndex_Object = MibTableColumn
h3cDomainSchemeIndex = _H3cDomainSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 1),
    _H3cDomainSchemeIndex_Type()
)
h3cDomainSchemeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainSchemeIndex.setStatus("current")
_H3cDomainSchemeMode_Type = H3cModeOfDomainScheme
_H3cDomainSchemeMode_Object = MibTableColumn
h3cDomainSchemeMode = _H3cDomainSchemeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 2),
    _H3cDomainSchemeMode_Type()
)
h3cDomainSchemeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeMode.setStatus("current")


class _H3cDomainAuthSchemeName_Type(OctetString):
    """Custom type h3cDomainAuthSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainAuthSchemeName_Type.__name__ = "OctetString"
_H3cDomainAuthSchemeName_Object = MibTableColumn
h3cDomainAuthSchemeName = _H3cDomainAuthSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 3),
    _H3cDomainAuthSchemeName_Type()
)
h3cDomainAuthSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAuthSchemeName.setStatus("current")


class _H3cDomainAcctSchemeName_Type(OctetString):
    """Custom type h3cDomainAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainAcctSchemeName_Type.__name__ = "OctetString"
_H3cDomainAcctSchemeName_Object = MibTableColumn
h3cDomainAcctSchemeName = _H3cDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 4),
    _H3cDomainAcctSchemeName_Type()
)
h3cDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainAcctSchemeName.setStatus("current")
_H3cDomainSchemeRowStatus_Type = RowStatus
_H3cDomainSchemeRowStatus_Object = MibTableColumn
h3cDomainSchemeRowStatus = _H3cDomainSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 5),
    _H3cDomainSchemeRowStatus_Type()
)
h3cDomainSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeRowStatus.setStatus("current")
_H3cDomainSchemeAAAType_Type = H3cAAATypeDomainScheme
_H3cDomainSchemeAAAType_Object = MibTableColumn
h3cDomainSchemeAAAType = _H3cDomainSchemeAAAType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 6),
    _H3cDomainSchemeAAAType_Type()
)
h3cDomainSchemeAAAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAAAType.setStatus("current")


class _H3cDomainSchemeAAAName_Type(OctetString):
    """Custom type h3cDomainSchemeAAAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainSchemeAAAName_Type.__name__ = "OctetString"
_H3cDomainSchemeAAAName_Object = MibTableColumn
h3cDomainSchemeAAAName = _H3cDomainSchemeAAAName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 7),
    _H3cDomainSchemeAAAName_Type()
)
h3cDomainSchemeAAAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAAAName.setStatus("current")
_H3cDomainSchemeAccessMode_Type = H3cAccessModeofDomainScheme
_H3cDomainSchemeAccessMode_Object = MibTableColumn
h3cDomainSchemeAccessMode = _H3cDomainSchemeAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 2, 1, 8),
    _H3cDomainSchemeAccessMode_Type()
)
h3cDomainSchemeAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainSchemeAccessMode.setStatus("current")
_H3cDomainIpPoolTable_Object = MibTable
h3cDomainIpPoolTable = _H3cDomainIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDomainIpPoolTable.setStatus("current")
_H3cDomainIpPoolEntry_Object = MibTableRow
h3cDomainIpPoolEntry = _H3cDomainIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1)
)
h3cDomainIpPoolEntry.setIndexNames(
    (0, "H3C-DOMAIN-MIB", "h3cDomainName"),
    (0, "H3C-DOMAIN-MIB", "h3cDomainIpPoolNum"),
)
if mibBuilder.loadTexts:
    h3cDomainIpPoolEntry.setStatus("current")


class _H3cDomainIpPoolNum_Type(Integer32):
    """Custom type h3cDomainIpPoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_H3cDomainIpPoolNum_Type.__name__ = "Integer32"
_H3cDomainIpPoolNum_Object = MibTableColumn
h3cDomainIpPoolNum = _H3cDomainIpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1, 1),
    _H3cDomainIpPoolNum_Type()
)
h3cDomainIpPoolNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDomainIpPoolNum.setStatus("current")
_H3cDomainIpPoolLowIpAddrType_Type = InetAddressType
_H3cDomainIpPoolLowIpAddrType_Object = MibTableColumn
h3cDomainIpPoolLowIpAddrType = _H3cDomainIpPoolLowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1, 2),
    _H3cDomainIpPoolLowIpAddrType_Type()
)
h3cDomainIpPoolLowIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLowIpAddrType.setStatus("current")
_H3cDomainIpPoolLowIpAddr_Type = InetAddress
_H3cDomainIpPoolLowIpAddr_Object = MibTableColumn
h3cDomainIpPoolLowIpAddr = _H3cDomainIpPoolLowIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1, 3),
    _H3cDomainIpPoolLowIpAddr_Type()
)
h3cDomainIpPoolLowIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLowIpAddr.setStatus("current")
_H3cDomainIpPoolLen_Type = Integer32
_H3cDomainIpPoolLen_Object = MibTableColumn
h3cDomainIpPoolLen = _H3cDomainIpPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1, 4),
    _H3cDomainIpPoolLen_Type()
)
h3cDomainIpPoolLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolLen.setStatus("current")
_H3cDomainIpPoolRowStatus_Type = RowStatus
_H3cDomainIpPoolRowStatus_Object = MibTableColumn
h3cDomainIpPoolRowStatus = _H3cDomainIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 3, 1, 5),
    _H3cDomainIpPoolRowStatus_Type()
)
h3cDomainIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDomainIpPoolRowStatus.setStatus("current")
_H3cDomainStatTable_Object = MibTable
h3cDomainStatTable = _H3cDomainStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4)
)
if mibBuilder.loadTexts:
    h3cDomainStatTable.setStatus("current")
_H3cDomainStatEntry_Object = MibTableRow
h3cDomainStatEntry = _H3cDomainStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1)
)
h3cDomainStatEntry.setIndexNames(
    (0, "H3C-DOMAIN-MIB", "h3cDomainName"),
)
if mibBuilder.loadTexts:
    h3cDomainStatEntry.setStatus("current")
_H3cDomainAccessedNum_Type = Unsigned32
_H3cDomainAccessedNum_Object = MibTableColumn
h3cDomainAccessedNum = _H3cDomainAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 1),
    _H3cDomainAccessedNum_Type()
)
h3cDomainAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainAccessedNum.setStatus("current")
_H3cDomainOnlineNum_Type = Unsigned32
_H3cDomainOnlineNum_Object = MibTableColumn
h3cDomainOnlineNum = _H3cDomainOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 2),
    _H3cDomainOnlineNum_Type()
)
h3cDomainOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineNum.setStatus("current")
_H3cDomainOnlinePPPUser_Type = Unsigned32
_H3cDomainOnlinePPPUser_Object = MibTableColumn
h3cDomainOnlinePPPUser = _H3cDomainOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 3),
    _H3cDomainOnlinePPPUser_Type()
)
h3cDomainOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlinePPPUser.setStatus("current")
_H3cDomainOnlineIPoEUser_Type = Unsigned32
_H3cDomainOnlineIPoEUser_Object = MibTableColumn
h3cDomainOnlineIPoEUser = _H3cDomainOnlineIPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 4),
    _H3cDomainOnlineIPoEUser_Type()
)
h3cDomainOnlineIPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineIPoEUser.setStatus("current")
_H3cDomainOnlinePPPoEUser_Type = Unsigned32
_H3cDomainOnlinePPPoEUser_Object = MibTableColumn
h3cDomainOnlinePPPoEUser = _H3cDomainOnlinePPPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 5),
    _H3cDomainOnlinePPPoEUser_Type()
)
h3cDomainOnlinePPPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlinePPPoEUser.setStatus("current")
_H3cDomainOnlinePPPoAUser_Type = Unsigned32
_H3cDomainOnlinePPPoAUser_Object = MibTableColumn
h3cDomainOnlinePPPoAUser = _H3cDomainOnlinePPPoAUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 6),
    _H3cDomainOnlinePPPoAUser_Type()
)
h3cDomainOnlinePPPoAUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlinePPPoAUser.setStatus("current")
_H3cDomainOnlinePPPoFRUser_Type = Unsigned32
_H3cDomainOnlinePPPoFRUser_Object = MibTableColumn
h3cDomainOnlinePPPoFRUser = _H3cDomainOnlinePPPoFRUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 7),
    _H3cDomainOnlinePPPoFRUser_Type()
)
h3cDomainOnlinePPPoFRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlinePPPoFRUser.setStatus("current")
_H3cDomainOnlineLacUser_Type = Unsigned32
_H3cDomainOnlineLacUser_Object = MibTableColumn
h3cDomainOnlineLacUser = _H3cDomainOnlineLacUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 8),
    _H3cDomainOnlineLacUser_Type()
)
h3cDomainOnlineLacUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineLacUser.setStatus("current")
_H3cDomainOnlineLnsUser_Type = Unsigned32
_H3cDomainOnlineLnsUser_Object = MibTableColumn
h3cDomainOnlineLnsUser = _H3cDomainOnlineLnsUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 9),
    _H3cDomainOnlineLnsUser_Type()
)
h3cDomainOnlineLnsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineLnsUser.setStatus("current")
_H3cDomainOnlineIPoEBindAuthUser_Type = Unsigned32
_H3cDomainOnlineIPoEBindAuthUser_Object = MibTableColumn
h3cDomainOnlineIPoEBindAuthUser = _H3cDomainOnlineIPoEBindAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 10),
    _H3cDomainOnlineIPoEBindAuthUser_Type()
)
h3cDomainOnlineIPoEBindAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineIPoEBindAuthUser.setStatus("current")
_H3cDomainOnlineIPoEWebAuthUser_Type = Unsigned32
_H3cDomainOnlineIPoEWebAuthUser_Object = MibTableColumn
h3cDomainOnlineIPoEWebAuthUser = _H3cDomainOnlineIPoEWebAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 11),
    _H3cDomainOnlineIPoEWebAuthUser_Type()
)
h3cDomainOnlineIPoEWebAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineIPoEWebAuthUser.setStatus("current")
_H3cDomainOnlineLeasedUser_Type = Unsigned32
_H3cDomainOnlineLeasedUser_Object = MibTableColumn
h3cDomainOnlineLeasedUser = _H3cDomainOnlineLeasedUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 4, 1, 12),
    _H3cDomainOnlineLeasedUser_Type()
)
h3cDomainOnlineLeasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainOnlineLeasedUser.setStatus("current")
_H3cDomainIPPoolStatTable_Object = MibTable
h3cDomainIPPoolStatTable = _H3cDomainIPPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5)
)
if mibBuilder.loadTexts:
    h3cDomainIPPoolStatTable.setStatus("current")
_H3cDomainIPPoolStatEntry_Object = MibTableRow
h3cDomainIPPoolStatEntry = _H3cDomainIPPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1)
)
h3cDomainIPPoolStatEntry.setIndexNames(
    (0, "H3C-DOMAIN-MIB", "h3cDomainName"),
)
if mibBuilder.loadTexts:
    h3cDomainIPPoolStatEntry.setStatus("current")
_H3cDomainIPTotalNum_Type = Unsigned32
_H3cDomainIPTotalNum_Object = MibTableColumn
h3cDomainIPTotalNum = _H3cDomainIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 1),
    _H3cDomainIPTotalNum_Type()
)
h3cDomainIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPTotalNum.setStatus("current")
_H3cDomainIPUsedNum_Type = Unsigned32
_H3cDomainIPUsedNum_Object = MibTableColumn
h3cDomainIPUsedNum = _H3cDomainIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 2),
    _H3cDomainIPUsedNum_Type()
)
h3cDomainIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPUsedNum.setStatus("current")
_H3cDomainIPConflictNum_Type = Unsigned32
_H3cDomainIPConflictNum_Object = MibTableColumn
h3cDomainIPConflictNum = _H3cDomainIPConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 3),
    _H3cDomainIPConflictNum_Type()
)
h3cDomainIPConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPConflictNum.setStatus("current")
_H3cDomainIPExcludeNum_Type = Unsigned32
_H3cDomainIPExcludeNum_Object = MibTableColumn
h3cDomainIPExcludeNum = _H3cDomainIPExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 4),
    _H3cDomainIPExcludeNum_Type()
)
h3cDomainIPExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPExcludeNum.setStatus("current")
_H3cDomainIPIdleNum_Type = Unsigned32
_H3cDomainIPIdleNum_Object = MibTableColumn
h3cDomainIPIdleNum = _H3cDomainIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 5),
    _H3cDomainIPIdleNum_Type()
)
h3cDomainIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPIdleNum.setStatus("current")


class _H3cDomainIPUsedPercent_Type(OctetString):
    """Custom type h3cDomainIPUsedPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cDomainIPUsedPercent_Type.__name__ = "OctetString"
_H3cDomainIPUsedPercent_Object = MibTableColumn
h3cDomainIPUsedPercent = _H3cDomainIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 2, 5, 1, 6),
    _H3cDomainIPUsedPercent_Type()
)
h3cDomainIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainIPUsedPercent.setStatus("current")
_H3cDomainGlobalStat_ObjectIdentity = ObjectIdentity
h3cDomainGlobalStat = _H3cDomainGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3)
)
_H3cDomainGlobalAccessedNum_Type = Unsigned32
_H3cDomainGlobalAccessedNum_Object = MibScalar
h3cDomainGlobalAccessedNum = _H3cDomainGlobalAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 1),
    _H3cDomainGlobalAccessedNum_Type()
)
h3cDomainGlobalAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalAccessedNum.setStatus("current")
_H3cDomainGlobalOnlineNum_Type = Unsigned32
_H3cDomainGlobalOnlineNum_Object = MibScalar
h3cDomainGlobalOnlineNum = _H3cDomainGlobalOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 2),
    _H3cDomainGlobalOnlineNum_Type()
)
h3cDomainGlobalOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineNum.setStatus("current")
_H3cDomainGlobalOnlinePPPUser_Type = Unsigned32
_H3cDomainGlobalOnlinePPPUser_Object = MibScalar
h3cDomainGlobalOnlinePPPUser = _H3cDomainGlobalOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 3),
    _H3cDomainGlobalOnlinePPPUser_Type()
)
h3cDomainGlobalOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlinePPPUser.setStatus("current")
_H3cDomainGlobalOnlineIPoEUser_Type = Unsigned32
_H3cDomainGlobalOnlineIPoEUser_Object = MibScalar
h3cDomainGlobalOnlineIPoEUser = _H3cDomainGlobalOnlineIPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 4),
    _H3cDomainGlobalOnlineIPoEUser_Type()
)
h3cDomainGlobalOnlineIPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineIPoEUser.setStatus("current")
_H3cDomainGlobalOnlinePPPoEUser_Type = Unsigned32
_H3cDomainGlobalOnlinePPPoEUser_Object = MibScalar
h3cDomainGlobalOnlinePPPoEUser = _H3cDomainGlobalOnlinePPPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 5),
    _H3cDomainGlobalOnlinePPPoEUser_Type()
)
h3cDomainGlobalOnlinePPPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlinePPPoEUser.setStatus("current")
_H3cDomainGlobalOnlinePPPoAUser_Type = Unsigned32
_H3cDomainGlobalOnlinePPPoAUser_Object = MibScalar
h3cDomainGlobalOnlinePPPoAUser = _H3cDomainGlobalOnlinePPPoAUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 6),
    _H3cDomainGlobalOnlinePPPoAUser_Type()
)
h3cDomainGlobalOnlinePPPoAUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlinePPPoAUser.setStatus("current")
_H3cDomainGlobalOnlinePPPoFRUser_Type = Unsigned32
_H3cDomainGlobalOnlinePPPoFRUser_Object = MibScalar
h3cDomainGlobalOnlinePPPoFRUser = _H3cDomainGlobalOnlinePPPoFRUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 7),
    _H3cDomainGlobalOnlinePPPoFRUser_Type()
)
h3cDomainGlobalOnlinePPPoFRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlinePPPoFRUser.setStatus("current")
_H3cDomainGlobalOnlineLacUser_Type = Unsigned32
_H3cDomainGlobalOnlineLacUser_Object = MibScalar
h3cDomainGlobalOnlineLacUser = _H3cDomainGlobalOnlineLacUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 8),
    _H3cDomainGlobalOnlineLacUser_Type()
)
h3cDomainGlobalOnlineLacUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineLacUser.setStatus("current")
_H3cDomainGlobalOnlineLnsUser_Type = Unsigned32
_H3cDomainGlobalOnlineLnsUser_Object = MibScalar
h3cDomainGlobalOnlineLnsUser = _H3cDomainGlobalOnlineLnsUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 9),
    _H3cDomainGlobalOnlineLnsUser_Type()
)
h3cDomainGlobalOnlineLnsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineLnsUser.setStatus("current")
_H3cDomainGlobalOnlineIPoEBindAuthUser_Type = Unsigned32
_H3cDomainGlobalOnlineIPoEBindAuthUser_Object = MibScalar
h3cDomainGlobalOnlineIPoEBindAuthUser = _H3cDomainGlobalOnlineIPoEBindAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 10),
    _H3cDomainGlobalOnlineIPoEBindAuthUser_Type()
)
h3cDomainGlobalOnlineIPoEBindAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineIPoEBindAuthUser.setStatus("current")
_H3cDomainGlobalOnlineIPoEWebAuthUser_Type = Unsigned32
_H3cDomainGlobalOnlineIPoEWebAuthUser_Object = MibScalar
h3cDomainGlobalOnlineIPoEWebAuthUser = _H3cDomainGlobalOnlineIPoEWebAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 11),
    _H3cDomainGlobalOnlineIPoEWebAuthUser_Type()
)
h3cDomainGlobalOnlineIPoEWebAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineIPoEWebAuthUser.setStatus("current")
_H3cDomainGlobalOnlineLeasedUser_Type = Unsigned32
_H3cDomainGlobalOnlineLeasedUser_Object = MibScalar
h3cDomainGlobalOnlineLeasedUser = _H3cDomainGlobalOnlineLeasedUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 46, 3, 12),
    _H3cDomainGlobalOnlineLeasedUser_Type()
)
h3cDomainGlobalOnlineLeasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDomainGlobalOnlineLeasedUser.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-DOMAIN-MIB",
    **{"H3cModeOfDomainScheme": H3cModeOfDomainScheme,
       "H3cAAATypeDomainScheme": H3cAAATypeDomainScheme,
       "H3cAccessModeofDomainScheme": H3cAccessModeofDomainScheme,
       "h3cDomain": h3cDomain,
       "h3cDomainControl": h3cDomainControl,
       "h3cDomainDefault": h3cDomainDefault,
       "h3cDomainTables": h3cDomainTables,
       "h3cDomainInfoTable": h3cDomainInfoTable,
       "h3cDomainInfoEntry": h3cDomainInfoEntry,
       "h3cDomainName": h3cDomainName,
       "h3cDomainState": h3cDomainState,
       "h3cDomainMaxAccessNum": h3cDomainMaxAccessNum,
       "h3cDomainVlanAssignMode": h3cDomainVlanAssignMode,
       "h3cDomainIdleCutEnable": h3cDomainIdleCutEnable,
       "h3cDomainIdleCutMaxTime": h3cDomainIdleCutMaxTime,
       "h3cDomainIdleCutMinFlow": h3cDomainIdleCutMinFlow,
       "h3cDomainMessengerEnable": h3cDomainMessengerEnable,
       "h3cDomainMessengerLimitTime": h3cDomainMessengerLimitTime,
       "h3cDomainMessengerSpanTime": h3cDomainMessengerSpanTime,
       "h3cDomainSelfServiceEnable": h3cDomainSelfServiceEnable,
       "h3cDomainSelfServiceURL": h3cDomainSelfServiceURL,
       "h3cDomainAccFailureAction": h3cDomainAccFailureAction,
       "h3cDomainRowStatus": h3cDomainRowStatus,
       "h3cDomainCurrentAccessNum": h3cDomainCurrentAccessNum,
       "h3cDomainIdleCutTime": h3cDomainIdleCutTime,
       "h3cDomainServiceType": h3cDomainServiceType,
       "h3cDomainIpPoolName": h3cDomainIpPoolName,
       "h3cDomainIpv6PoolName": h3cDomainIpv6PoolName,
       "h3cDomainSchemeTable": h3cDomainSchemeTable,
       "h3cDomainSchemeEntry": h3cDomainSchemeEntry,
       "h3cDomainSchemeIndex": h3cDomainSchemeIndex,
       "h3cDomainSchemeMode": h3cDomainSchemeMode,
       "h3cDomainAuthSchemeName": h3cDomainAuthSchemeName,
       "h3cDomainAcctSchemeName": h3cDomainAcctSchemeName,
       "h3cDomainSchemeRowStatus": h3cDomainSchemeRowStatus,
       "h3cDomainSchemeAAAType": h3cDomainSchemeAAAType,
       "h3cDomainSchemeAAAName": h3cDomainSchemeAAAName,
       "h3cDomainSchemeAccessMode": h3cDomainSchemeAccessMode,
       "h3cDomainIpPoolTable": h3cDomainIpPoolTable,
       "h3cDomainIpPoolEntry": h3cDomainIpPoolEntry,
       "h3cDomainIpPoolNum": h3cDomainIpPoolNum,
       "h3cDomainIpPoolLowIpAddrType": h3cDomainIpPoolLowIpAddrType,
       "h3cDomainIpPoolLowIpAddr": h3cDomainIpPoolLowIpAddr,
       "h3cDomainIpPoolLen": h3cDomainIpPoolLen,
       "h3cDomainIpPoolRowStatus": h3cDomainIpPoolRowStatus,
       "h3cDomainStatTable": h3cDomainStatTable,
       "h3cDomainStatEntry": h3cDomainStatEntry,
       "h3cDomainAccessedNum": h3cDomainAccessedNum,
       "h3cDomainOnlineNum": h3cDomainOnlineNum,
       "h3cDomainOnlinePPPUser": h3cDomainOnlinePPPUser,
       "h3cDomainOnlineIPoEUser": h3cDomainOnlineIPoEUser,
       "h3cDomainOnlinePPPoEUser": h3cDomainOnlinePPPoEUser,
       "h3cDomainOnlinePPPoAUser": h3cDomainOnlinePPPoAUser,
       "h3cDomainOnlinePPPoFRUser": h3cDomainOnlinePPPoFRUser,
       "h3cDomainOnlineLacUser": h3cDomainOnlineLacUser,
       "h3cDomainOnlineLnsUser": h3cDomainOnlineLnsUser,
       "h3cDomainOnlineIPoEBindAuthUser": h3cDomainOnlineIPoEBindAuthUser,
       "h3cDomainOnlineIPoEWebAuthUser": h3cDomainOnlineIPoEWebAuthUser,
       "h3cDomainOnlineLeasedUser": h3cDomainOnlineLeasedUser,
       "h3cDomainIPPoolStatTable": h3cDomainIPPoolStatTable,
       "h3cDomainIPPoolStatEntry": h3cDomainIPPoolStatEntry,
       "h3cDomainIPTotalNum": h3cDomainIPTotalNum,
       "h3cDomainIPUsedNum": h3cDomainIPUsedNum,
       "h3cDomainIPConflictNum": h3cDomainIPConflictNum,
       "h3cDomainIPExcludeNum": h3cDomainIPExcludeNum,
       "h3cDomainIPIdleNum": h3cDomainIPIdleNum,
       "h3cDomainIPUsedPercent": h3cDomainIPUsedPercent,
       "h3cDomainGlobalStat": h3cDomainGlobalStat,
       "h3cDomainGlobalAccessedNum": h3cDomainGlobalAccessedNum,
       "h3cDomainGlobalOnlineNum": h3cDomainGlobalOnlineNum,
       "h3cDomainGlobalOnlinePPPUser": h3cDomainGlobalOnlinePPPUser,
       "h3cDomainGlobalOnlineIPoEUser": h3cDomainGlobalOnlineIPoEUser,
       "h3cDomainGlobalOnlinePPPoEUser": h3cDomainGlobalOnlinePPPoEUser,
       "h3cDomainGlobalOnlinePPPoAUser": h3cDomainGlobalOnlinePPPoAUser,
       "h3cDomainGlobalOnlinePPPoFRUser": h3cDomainGlobalOnlinePPPoFRUser,
       "h3cDomainGlobalOnlineLacUser": h3cDomainGlobalOnlineLacUser,
       "h3cDomainGlobalOnlineLnsUser": h3cDomainGlobalOnlineLnsUser,
       "h3cDomainGlobalOnlineIPoEBindAuthUser": h3cDomainGlobalOnlineIPoEBindAuthUser,
       "h3cDomainGlobalOnlineIPoEWebAuthUser": h3cDomainGlobalOnlineIPoEWebAuthUser,
       "h3cDomainGlobalOnlineLeasedUser": h3cDomainGlobalOnlineLeasedUser}
)
