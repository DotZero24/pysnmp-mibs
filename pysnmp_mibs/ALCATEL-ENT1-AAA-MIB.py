# SNMP MIB module (ALCATEL-ENT1-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:50 2025
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

(softentIND1AAA,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1AAA")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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


# MODULE-IDENTITY

alcatelIND1AAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AAAMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBObjects = _AlcatelIND1AAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBObjects.setStatus("current")
_AaaServerMIB_ObjectIdentity = ObjectIdentity
aaaServerMIB = _AaaServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1)
)
_AaaServerTable_Object = MibTable
aaaServerTable = _AaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aaaServerTable.setStatus("current")
_AaaServerEntry_Object = MibTableRow
aaaServerEntry = _AaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1)
)
aaaServerEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaasName"),
)
if mibBuilder.loadTexts:
    aaaServerEntry.setStatus("current")


class _AaasName_Type(SnmpAdminString):
    """Custom type aaasName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasName_Type.__name__ = "SnmpAdminString"
_AaasName_Object = MibTableColumn
aaasName = _AaasName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 1),
    _AaasName_Type()
)
aaasName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaasName.setStatus("current")


class _AaasProtocol_Type(Integer32):
    """Custom type aaasProtocol based on Integer32"""
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
        *(("radius", 1),
          ("ldap", 2),
          ("ace", 3),
          ("tacacs", 4))
    )


_AaasProtocol_Type.__name__ = "Integer32"
_AaasProtocol_Object = MibTableColumn
aaasProtocol = _AaasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 2),
    _AaasProtocol_Type()
)
aaasProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasProtocol.setStatus("current")


class _AaasHostName_Type(SnmpAdminString):
    """Custom type aaasHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName_Type.__name__ = "SnmpAdminString"
_AaasHostName_Object = MibTableColumn
aaasHostName = _AaasHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 3),
    _AaasHostName_Type()
)
aaasHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName.setStatus("current")
_AaasIpAddress_Type = IpAddress
_AaasIpAddress_Object = MibTableColumn
aaasIpAddress = _AaasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 4),
    _AaasIpAddress_Type()
)
aaasIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress.setStatus("current")


class _AaasHostName2_Type(SnmpAdminString):
    """Custom type aaasHostName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName2_Type.__name__ = "SnmpAdminString"
_AaasHostName2_Object = MibTableColumn
aaasHostName2 = _AaasHostName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 5),
    _AaasHostName2_Type()
)
aaasHostName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName2.setStatus("current")
_AaasIpAddress2_Type = IpAddress
_AaasIpAddress2_Object = MibTableColumn
aaasIpAddress2 = _AaasIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 6),
    _AaasIpAddress2_Type()
)
aaasIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress2.setStatus("current")


class _AaasRetries_Type(Integer32):
    """Custom type aaasRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AaasRetries_Type.__name__ = "Integer32"
_AaasRetries_Object = MibTableColumn
aaasRetries = _AaasRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 7),
    _AaasRetries_Type()
)
aaasRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRetries.setStatus("current")


class _AaasTimout_Type(Integer32):
    """Custom type aaasTimout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AaasTimout_Type.__name__ = "Integer32"
_AaasTimout_Object = MibTableColumn
aaasTimout = _AaasTimout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 8),
    _AaasTimout_Type()
)
aaasTimout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTimout.setStatus("current")


class _AaasRadKey_Type(SnmpAdminString):
    """Custom type aaasRadKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasRadKey_Type.__name__ = "SnmpAdminString"
_AaasRadKey_Object = MibTableColumn
aaasRadKey = _AaasRadKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 9),
    _AaasRadKey_Type()
)
aaasRadKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKey.setStatus("current")


class _AaasRadAuthPort_Type(Integer32):
    """Custom type aaasRadAuthPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAuthPort_Type.__name__ = "Integer32"
_AaasRadAuthPort_Object = MibTableColumn
aaasRadAuthPort = _AaasRadAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 10),
    _AaasRadAuthPort_Type()
)
aaasRadAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAuthPort.setStatus("current")


class _AaasRadAcctPort_Type(Integer32):
    """Custom type aaasRadAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAcctPort_Type.__name__ = "Integer32"
_AaasRadAcctPort_Object = MibTableColumn
aaasRadAcctPort = _AaasRadAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 11),
    _AaasRadAcctPort_Type()
)
aaasRadAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAcctPort.setStatus("current")


class _AaasLdapPort_Type(Integer32):
    """Custom type aaasLdapPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasLdapPort_Type.__name__ = "Integer32"
_AaasLdapPort_Object = MibTableColumn
aaasLdapPort = _AaasLdapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 12),
    _AaasLdapPort_Type()
)
aaasLdapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPort.setStatus("current")


class _AaasLdapDn_Type(SnmpAdminString):
    """Custom type aaasLdapDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaasLdapDn_Type.__name__ = "SnmpAdminString"
_AaasLdapDn_Object = MibTableColumn
aaasLdapDn = _AaasLdapDn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 13),
    _AaasLdapDn_Type()
)
aaasLdapDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapDn.setStatus("current")


class _AaasLdapPasswd_Type(SnmpAdminString):
    """Custom type aaasLdapPasswd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasLdapPasswd_Type.__name__ = "SnmpAdminString"
_AaasLdapPasswd_Object = MibTableColumn
aaasLdapPasswd = _AaasLdapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 14),
    _AaasLdapPasswd_Type()
)
aaasLdapPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswd.setStatus("current")


class _AaasLdapSearchBase_Type(SnmpAdminString):
    """Custom type aaasLdapSearchBase based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasLdapSearchBase_Type.__name__ = "SnmpAdminString"
_AaasLdapSearchBase_Object = MibTableColumn
aaasLdapSearchBase = _AaasLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 15),
    _AaasLdapSearchBase_Type()
)
aaasLdapSearchBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapSearchBase.setStatus("current")


class _AaasLdapServType_Type(Integer32):
    """Custom type aaasLdapServType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("generic", 1),
          ("netscape", 2),
          ("novell", 3),
          ("sun", 4),
          ("microsoft", 5))
    )


_AaasLdapServType_Type.__name__ = "Integer32"
_AaasLdapServType_Object = MibTableColumn
aaasLdapServType = _AaasLdapServType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 16),
    _AaasLdapServType_Type()
)
aaasLdapServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapServType.setStatus("current")


class _AaasLdapEnableSsl_Type(Integer32):
    """Custom type aaasLdapEnableSsl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaasLdapEnableSsl_Type.__name__ = "Integer32"
_AaasLdapEnableSsl_Object = MibTableColumn
aaasLdapEnableSsl = _AaasLdapEnableSsl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 17),
    _AaasLdapEnableSsl_Type()
)
aaasLdapEnableSsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapEnableSsl.setStatus("current")


class _AaasRowStatus_Type(RowStatus):
    """Custom type aaasRowStatus based on RowStatus"""
    defaultValue = 2


_AaasRowStatus_Type.__name__ = "RowStatus"
_AaasRowStatus_Object = MibTableColumn
aaasRowStatus = _AaasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 18),
    _AaasRowStatus_Type()
)
aaasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRowStatus.setStatus("current")


class _AaasTacacsKey_Type(SnmpAdminString):
    """Custom type aaasTacacsKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasTacacsKey_Type.__name__ = "SnmpAdminString"
_AaasTacacsKey_Object = MibTableColumn
aaasTacacsKey = _AaasTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 19),
    _AaasTacacsKey_Type()
)
aaasTacacsKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKey.setStatus("current")


class _AaasTacacsPort_Type(Integer32):
    """Custom type aaasTacacsPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasTacacsPort_Type.__name__ = "Integer32"
_AaasTacacsPort_Object = MibTableColumn
aaasTacacsPort = _AaasTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 20),
    _AaasTacacsPort_Type()
)
aaasTacacsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsPort.setStatus("current")


class _AaasVrfName_Type(SnmpAdminString):
    """Custom type aaasVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasVrfName_Type.__name__ = "SnmpAdminString"
_AaasVrfName_Object = MibTableColumn
aaasVrfName = _AaasVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 21),
    _AaasVrfName_Type()
)
aaasVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasVrfName.setStatus("current")


class _AaasRadKeyHash_Type(SnmpAdminString):
    """Custom type aaasRadKeyHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasRadKeyHash_Type.__name__ = "SnmpAdminString"
_AaasRadKeyHash_Object = MibTableColumn
aaasRadKeyHash = _AaasRadKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 22),
    _AaasRadKeyHash_Type()
)
aaasRadKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKeyHash.setStatus("current")


class _AaasLdapPasswdHash_Type(SnmpAdminString):
    """Custom type aaasLdapPasswdHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasLdapPasswdHash_Type.__name__ = "SnmpAdminString"
_AaasLdapPasswdHash_Object = MibTableColumn
aaasLdapPasswdHash = _AaasLdapPasswdHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 23),
    _AaasLdapPasswdHash_Type()
)
aaasLdapPasswdHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswdHash.setStatus("current")


class _AaasTacacsKeyHash_Type(SnmpAdminString):
    """Custom type aaasTacacsKeyHash based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AaasTacacsKeyHash_Type.__name__ = "SnmpAdminString"
_AaasTacacsKeyHash_Object = MibTableColumn
aaasTacacsKeyHash = _AaasTacacsKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 1, 1, 1, 24),
    _AaasTacacsKeyHash_Type()
)
aaasTacacsKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKeyHash.setStatus("current")
_AaaAuthAcctMIB_ObjectIdentity = ObjectIdentity
aaaAuthAcctMIB = _AaaAuthAcctMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2)
)
_AaaAuthSATable_Object = MibTable
aaaAuthSATable = _AaaAuthSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aaaAuthSATable.setStatus("current")
_AaaAuthSAEntry_Object = MibTableRow
aaaAuthSAEntry = _AaaAuthSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1)
)
aaaAuthSAEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaatsInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthSAEntry.setStatus("current")


class _AaatsInterface_Type(Integer32):
    """Custom type aaatsInterface based on Integer32"""
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
        *(("default", 1),
          ("console", 2),
          ("telnet", 3),
          ("ftp", 4),
          ("http", 5),
          ("snmp", 6),
          ("ssh", 7))
    )


_AaatsInterface_Type.__name__ = "Integer32"
_AaatsInterface_Object = MibTableColumn
aaatsInterface = _AaatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 1),
    _AaatsInterface_Type()
)
aaatsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaatsInterface.setStatus("current")


class _AaatsName1_Type(SnmpAdminString):
    """Custom type aaatsName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName1_Type.__name__ = "SnmpAdminString"
_AaatsName1_Object = MibTableColumn
aaatsName1 = _AaatsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 2),
    _AaatsName1_Type()
)
aaatsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName1.setStatus("current")


class _AaatsName2_Type(SnmpAdminString):
    """Custom type aaatsName2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName2_Type.__name__ = "SnmpAdminString"
_AaatsName2_Object = MibTableColumn
aaatsName2 = _AaatsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 3),
    _AaatsName2_Type()
)
aaatsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName2.setStatus("current")


class _AaatsName3_Type(SnmpAdminString):
    """Custom type aaatsName3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName3_Type.__name__ = "SnmpAdminString"
_AaatsName3_Object = MibTableColumn
aaatsName3 = _AaatsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 4),
    _AaatsName3_Type()
)
aaatsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName3.setStatus("current")


class _AaatsName4_Type(SnmpAdminString):
    """Custom type aaatsName4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName4_Type.__name__ = "SnmpAdminString"
_AaatsName4_Object = MibTableColumn
aaatsName4 = _AaatsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 5),
    _AaatsName4_Type()
)
aaatsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName4.setStatus("current")


class _AaatsRowStatus_Type(RowStatus):
    """Custom type aaatsRowStatus based on RowStatus"""
    defaultValue = 2


_AaatsRowStatus_Type.__name__ = "RowStatus"
_AaatsRowStatus_Object = MibTableColumn
aaatsRowStatus = _AaatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 7),
    _AaatsRowStatus_Type()
)
aaatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsRowStatus.setStatus("current")


class _AaatsCertificate_Type(Integer32):
    """Custom type aaatsCertificate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noCertificate", 0),
          ("certificateOnly", 1),
          ("certificateWithPassword", 2))
    )


_AaatsCertificate_Type.__name__ = "Integer32"
_AaatsCertificate_Object = MibTableColumn
aaatsCertificate = _AaatsCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 1, 1, 8),
    _AaatsCertificate_Type()
)
aaatsCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsCertificate.setStatus("current")
_AaaAcctSATable_Object = MibTable
aaaAcctSATable = _AaaAcctSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aaaAcctSATable.setStatus("current")
_AaaAcctSAEntry_Object = MibTableRow
aaaAcctSAEntry = _AaaAcctSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1)
)
aaaAcctSAEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaacsInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctSAEntry.setStatus("current")


class _AaacsInterface_Type(Integer32):
    """Custom type aaacsInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacsInterface_Type.__name__ = "Integer32"
_AaacsInterface_Object = MibTableColumn
aaacsInterface = _AaacsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 1),
    _AaacsInterface_Type()
)
aaacsInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacsInterface.setStatus("current")


class _AaacsName1_Type(SnmpAdminString):
    """Custom type aaacsName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName1_Type.__name__ = "SnmpAdminString"
_AaacsName1_Object = MibTableColumn
aaacsName1 = _AaacsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 2),
    _AaacsName1_Type()
)
aaacsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName1.setStatus("current")


class _AaacsName2_Type(SnmpAdminString):
    """Custom type aaacsName2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName2_Type.__name__ = "SnmpAdminString"
_AaacsName2_Object = MibTableColumn
aaacsName2 = _AaacsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 3),
    _AaacsName2_Type()
)
aaacsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName2.setStatus("current")


class _AaacsName3_Type(SnmpAdminString):
    """Custom type aaacsName3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName3_Type.__name__ = "SnmpAdminString"
_AaacsName3_Object = MibTableColumn
aaacsName3 = _AaacsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 4),
    _AaacsName3_Type()
)
aaacsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName3.setStatus("current")


class _AaacsName4_Type(SnmpAdminString):
    """Custom type aaacsName4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName4_Type.__name__ = "SnmpAdminString"
_AaacsName4_Object = MibTableColumn
aaacsName4 = _AaacsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 5),
    _AaacsName4_Type()
)
aaacsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName4.setStatus("current")


class _AaacsRowStatus_Type(RowStatus):
    """Custom type aaacsRowStatus based on RowStatus"""
    defaultValue = 2


_AaacsRowStatus_Type.__name__ = "RowStatus"
_AaacsRowStatus_Object = MibTableColumn
aaacsRowStatus = _AaacsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 2, 1, 6),
    _AaacsRowStatus_Type()
)
aaacsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsRowStatus.setStatus("current")
_AaaAcctCmdTable_Object = MibTable
aaaAcctCmdTable = _AaaAcctCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aaaAcctCmdTable.setStatus("current")
_AaaAcctCmdEntry_Object = MibTableRow
aaaAcctCmdEntry = _AaaAcctCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1)
)
aaaAcctCmdEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaacmdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctCmdEntry.setStatus("current")


class _AaacmdInterface_Type(Integer32):
    """Custom type aaacmdInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacmdInterface_Type.__name__ = "Integer32"
_AaacmdInterface_Object = MibTableColumn
aaacmdInterface = _AaacmdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 1),
    _AaacmdInterface_Type()
)
aaacmdInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacmdInterface.setStatus("current")


class _AaacmdSrvName1_Type(SnmpAdminString):
    """Custom type aaacmdSrvName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName1_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName1_Object = MibTableColumn
aaacmdSrvName1 = _AaacmdSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 2),
    _AaacmdSrvName1_Type()
)
aaacmdSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName1.setStatus("current")


class _AaacmdSrvName2_Type(SnmpAdminString):
    """Custom type aaacmdSrvName2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName2_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName2_Object = MibTableColumn
aaacmdSrvName2 = _AaacmdSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 3),
    _AaacmdSrvName2_Type()
)
aaacmdSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName2.setStatus("current")


class _AaacmdSrvName3_Type(SnmpAdminString):
    """Custom type aaacmdSrvName3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName3_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName3_Object = MibTableColumn
aaacmdSrvName3 = _AaacmdSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 4),
    _AaacmdSrvName3_Type()
)
aaacmdSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName3.setStatus("current")


class _AaacmdSrvName4_Type(SnmpAdminString):
    """Custom type aaacmdSrvName4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName4_Type.__name__ = "SnmpAdminString"
_AaacmdSrvName4_Object = MibTableColumn
aaacmdSrvName4 = _AaacmdSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 5),
    _AaacmdSrvName4_Type()
)
aaacmdSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName4.setStatus("current")


class _AaacmdRowStatus_Type(RowStatus):
    """Custom type aaacmdRowStatus based on RowStatus"""
    defaultValue = 2


_AaacmdRowStatus_Type.__name__ = "RowStatus"
_AaacmdRowStatus_Object = MibTableColumn
aaacmdRowStatus = _AaacmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 3, 1, 6),
    _AaacmdRowStatus_Type()
)
aaacmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdRowStatus.setStatus("current")
_AaaAuthDATable_Object = MibTable
aaaAuthDATable = _AaaAuthDATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aaaAuthDATable.setStatus("current")
_AaaAuthDAEntry_Object = MibTableRow
aaaAuthDAEntry = _AaaAuthDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1)
)
aaaAuthDAEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaadaInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthDAEntry.setStatus("current")


class _AaadaInterface_Type(Integer32):
    """Custom type aaadaInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AaadaInterface_Type.__name__ = "Integer32"
_AaadaInterface_Object = MibTableColumn
aaadaInterface = _AaadaInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 1),
    _AaadaInterface_Type()
)
aaadaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaadaInterface.setStatus("current")


class _AaadaName1_Type(SnmpAdminString):
    """Custom type aaadaName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName1_Type.__name__ = "SnmpAdminString"
_AaadaName1_Object = MibTableColumn
aaadaName1 = _AaadaName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 2),
    _AaadaName1_Type()
)
aaadaName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName1.setStatus("current")


class _AaadaName2_Type(SnmpAdminString):
    """Custom type aaadaName2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName2_Type.__name__ = "SnmpAdminString"
_AaadaName2_Object = MibTableColumn
aaadaName2 = _AaadaName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 3),
    _AaadaName2_Type()
)
aaadaName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName2.setStatus("current")


class _AaadaName3_Type(SnmpAdminString):
    """Custom type aaadaName3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName3_Type.__name__ = "SnmpAdminString"
_AaadaName3_Object = MibTableColumn
aaadaName3 = _AaadaName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 4),
    _AaadaName3_Type()
)
aaadaName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName3.setStatus("current")


class _AaadaName4_Type(SnmpAdminString):
    """Custom type aaadaName4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaadaName4_Type.__name__ = "SnmpAdminString"
_AaadaName4_Object = MibTableColumn
aaadaName4 = _AaadaName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 5),
    _AaadaName4_Type()
)
aaadaName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaName4.setStatus("current")


class _AaadaRowStatus_Type(RowStatus):
    """Custom type aaadaRowStatus based on RowStatus"""
    defaultValue = 2


_AaadaRowStatus_Type.__name__ = "RowStatus"
_AaadaRowStatus_Object = MibTableColumn
aaadaRowStatus = _AaadaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 4, 1, 6),
    _AaadaRowStatus_Type()
)
aaadaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaadaRowStatus.setStatus("current")
_AaaAcctDATable_Object = MibTable
aaaAcctDATable = _AaaAcctDATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aaaAcctDATable.setStatus("current")
_AaaAcctDAEntry_Object = MibTableRow
aaaAcctDAEntry = _AaaAcctDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1)
)
aaaAcctDAEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaacdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctDAEntry.setStatus("current")


class _AaacdInterface_Type(Integer32):
    """Custom type aaacdInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AaacdInterface_Type.__name__ = "Integer32"
_AaacdInterface_Object = MibTableColumn
aaacdInterface = _AaacdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 1),
    _AaacdInterface_Type()
)
aaacdInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaacdInterface.setStatus("current")


class _AaacdName1_Type(SnmpAdminString):
    """Custom type aaacdName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName1_Type.__name__ = "SnmpAdminString"
_AaacdName1_Object = MibTableColumn
aaacdName1 = _AaacdName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 2),
    _AaacdName1_Type()
)
aaacdName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName1.setStatus("current")


class _AaacdName2_Type(SnmpAdminString):
    """Custom type aaacdName2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName2_Type.__name__ = "SnmpAdminString"
_AaacdName2_Object = MibTableColumn
aaacdName2 = _AaacdName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 3),
    _AaacdName2_Type()
)
aaacdName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName2.setStatus("current")


class _AaacdName3_Type(SnmpAdminString):
    """Custom type aaacdName3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName3_Type.__name__ = "SnmpAdminString"
_AaacdName3_Object = MibTableColumn
aaacdName3 = _AaacdName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 4),
    _AaacdName3_Type()
)
aaacdName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName3.setStatus("current")


class _AaacdName4_Type(SnmpAdminString):
    """Custom type aaacdName4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacdName4_Type.__name__ = "SnmpAdminString"
_AaacdName4_Object = MibTableColumn
aaacdName4 = _AaacdName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 5),
    _AaacdName4_Type()
)
aaacdName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdName4.setStatus("current")


class _AaacdRowStatus_Type(RowStatus):
    """Custom type aaacdRowStatus based on RowStatus"""
    defaultValue = 2


_AaacdRowStatus_Type.__name__ = "RowStatus"
_AaacdRowStatus_Object = MibTableColumn
aaacdRowStatus = _AaacdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 6),
    _AaacdRowStatus_Type()
)
aaacdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdRowStatus.setStatus("current")
_AaacdSyslogIPAddrType_Type = InetAddressType
_AaacdSyslogIPAddrType_Object = MibTableColumn
aaacdSyslogIPAddrType = _AaacdSyslogIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 7),
    _AaacdSyslogIPAddrType_Type()
)
aaacdSyslogIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdSyslogIPAddrType.setStatus("current")
_AaacdSyslogIPAddr_Type = InetAddress
_AaacdSyslogIPAddr_Object = MibTableColumn
aaacdSyslogIPAddr = _AaacdSyslogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 8),
    _AaacdSyslogIPAddr_Type()
)
aaacdSyslogIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdSyslogIPAddr.setStatus("current")


class _AaacdSyslogUdpPort_Type(Unsigned32):
    """Custom type aaacdSyslogUdpPort based on Unsigned32"""
    defaultValue = 514


_AaacdSyslogUdpPort_Type.__name__ = "Unsigned32"
_AaacdSyslogUdpPort_Object = MibTableColumn
aaacdSyslogUdpPort = _AaacdSyslogUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 9),
    _AaacdSyslogUdpPort_Type()
)
aaacdSyslogUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdSyslogUdpPort.setStatus("current")


class _AaacdCallngStationId_Type(Integer32):
    """Custom type aaacdCallngStationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2))
    )


_AaacdCallngStationId_Type.__name__ = "Integer32"
_AaacdCallngStationId_Object = MibTableColumn
aaacdCallngStationId = _AaacdCallngStationId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 5, 1, 10),
    _AaacdCallngStationId_Type()
)
aaacdCallngStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacdCallngStationId.setStatus("current")
_AlaAaaAuthConfig_ObjectIdentity = ObjectIdentity
alaAaaAuthConfig = _AlaAaaAuthConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6)
)


class _AlaAaaOnexReAuthStatus_Type(Integer32):
    """Custom type alaAaaOnexReAuthStatus based on Integer32"""
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


_AlaAaaOnexReAuthStatus_Type.__name__ = "Integer32"
_AlaAaaOnexReAuthStatus_Object = MibScalar
alaAaaOnexReAuthStatus = _AlaAaaOnexReAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 1),
    _AlaAaaOnexReAuthStatus_Type()
)
alaAaaOnexReAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaOnexReAuthStatus.setStatus("current")


class _AlaAaaOnexReAuthIntrvl_Type(Integer32):
    """Custom type alaAaaOnexReAuthIntrvl based on Integer32"""
    defaultValue = 3600


_AlaAaaOnexReAuthIntrvl_Type.__name__ = "Integer32"
_AlaAaaOnexReAuthIntrvl_Object = MibScalar
alaAaaOnexReAuthIntrvl = _AlaAaaOnexReAuthIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 2),
    _AlaAaaOnexReAuthIntrvl_Type()
)
alaAaaOnexReAuthIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaOnexReAuthIntrvl.setStatus("current")


class _AlaAaaOnexReAuthTrustRadStatus_Type(Integer32):
    """Custom type alaAaaOnexReAuthTrustRadStatus based on Integer32"""
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


_AlaAaaOnexReAuthTrustRadStatus_Type.__name__ = "Integer32"
_AlaAaaOnexReAuthTrustRadStatus_Object = MibScalar
alaAaaOnexReAuthTrustRadStatus = _AlaAaaOnexReAuthTrustRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 3),
    _AlaAaaOnexReAuthTrustRadStatus_Type()
)
alaAaaOnexReAuthTrustRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaOnexReAuthTrustRadStatus.setStatus("current")


class _AlaAaaOnexIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaOnexIntrmIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaOnexIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaOnexIntrmIntrvl_Object = MibScalar
alaAaaOnexIntrmIntrvl = _AlaAaaOnexIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 4),
    _AlaAaaOnexIntrmIntrvl_Type()
)
alaAaaOnexIntrmIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaOnexIntrmIntrvl.setStatus("current")


class _AlaAaaOnexIntmIntvlTrstRadSts_Type(Integer32):
    """Custom type alaAaaOnexIntmIntvlTrstRadSts based on Integer32"""
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


_AlaAaaOnexIntmIntvlTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaOnexIntmIntvlTrstRadSts_Object = MibScalar
alaAaaOnexIntmIntvlTrstRadSts = _AlaAaaOnexIntmIntvlTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 5),
    _AlaAaaOnexIntmIntvlTrstRadSts_Type()
)
alaAaaOnexIntmIntvlTrstRadSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaOnexIntmIntvlTrstRadSts.setStatus("current")


class _AlaAaaMacIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaMacIntrmIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaMacIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaMacIntrmIntrvl_Object = MibScalar
alaAaaMacIntrmIntrvl = _AlaAaaMacIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 6),
    _AlaAaaMacIntrmIntrvl_Type()
)
alaAaaMacIntrmIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacIntrmIntrvl.setStatus("current")


class _AlaAaaMacIntmIntvlTrstRadStatus_Type(Integer32):
    """Custom type alaAaaMacIntmIntvlTrstRadStatus based on Integer32"""
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


_AlaAaaMacIntmIntvlTrstRadStatus_Type.__name__ = "Integer32"
_AlaAaaMacIntmIntvlTrstRadStatus_Object = MibScalar
alaAaaMacIntmIntvlTrstRadStatus = _AlaAaaMacIntmIntvlTrstRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 7),
    _AlaAaaMacIntmIntvlTrstRadStatus_Type()
)
alaAaaMacIntmIntvlTrstRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacIntmIntvlTrstRadStatus.setStatus("current")


class _AlaAaaMacSessTimeoutStatus_Type(Integer32):
    """Custom type alaAaaMacSessTimeoutStatus based on Integer32"""
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


_AlaAaaMacSessTimeoutStatus_Type.__name__ = "Integer32"
_AlaAaaMacSessTimeoutStatus_Object = MibScalar
alaAaaMacSessTimeoutStatus = _AlaAaaMacSessTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 8),
    _AlaAaaMacSessTimeoutStatus_Type()
)
alaAaaMacSessTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacSessTimeoutStatus.setStatus("current")


class _AlaAaaMacSessTimeoutIntrvl_Type(Integer32):
    """Custom type alaAaaMacSessTimeoutIntrvl based on Integer32"""
    defaultValue = 43200


_AlaAaaMacSessTimeoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaMacSessTimeoutIntrvl_Object = MibScalar
alaAaaMacSessTimeoutIntrvl = _AlaAaaMacSessTimeoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 9),
    _AlaAaaMacSessTimeoutIntrvl_Type()
)
alaAaaMacSessTimeoutIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacSessTimeoutIntrvl.setStatus("current")


class _AlaAaaMacSesTimeoutTrstRadStatus_Type(Integer32):
    """Custom type alaAaaMacSesTimeoutTrstRadStatus based on Integer32"""
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


_AlaAaaMacSesTimeoutTrstRadStatus_Type.__name__ = "Integer32"
_AlaAaaMacSesTimeoutTrstRadStatus_Object = MibScalar
alaAaaMacSesTimeoutTrstRadStatus = _AlaAaaMacSesTimeoutTrstRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 10),
    _AlaAaaMacSesTimeoutTrstRadStatus_Type()
)
alaAaaMacSesTimeoutTrstRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacSesTimeoutTrstRadStatus.setStatus("current")


class _AlaAaaMacInActLogoutStatus_Type(Integer32):
    """Custom type alaAaaMacInActLogoutStatus based on Integer32"""
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


_AlaAaaMacInActLogoutStatus_Type.__name__ = "Integer32"
_AlaAaaMacInActLogoutStatus_Object = MibScalar
alaAaaMacInActLogoutStatus = _AlaAaaMacInActLogoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 11),
    _AlaAaaMacInActLogoutStatus_Type()
)
alaAaaMacInActLogoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacInActLogoutStatus.setStatus("current")


class _AlaAaaMacInActLogoutIntrvl_Type(Integer32):
    """Custom type alaAaaMacInActLogoutIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaMacInActLogoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaMacInActLogoutIntrvl_Object = MibScalar
alaAaaMacInActLogoutIntrvl = _AlaAaaMacInActLogoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 12),
    _AlaAaaMacInActLogoutIntrvl_Type()
)
alaAaaMacInActLogoutIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaMacInActLogoutIntrvl.setStatus("current")


class _AlaAaaCpIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaCpIntrmIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaCpIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaCpIntrmIntrvl_Object = MibScalar
alaAaaCpIntrmIntrvl = _AlaAaaCpIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 13),
    _AlaAaaCpIntrmIntrvl_Type()
)
alaAaaCpIntrmIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpIntrmIntrvl.setStatus("current")


class _AlaAaaCpIntmIntvlTrstRadStatus_Type(Integer32):
    """Custom type alaAaaCpIntmIntvlTrstRadStatus based on Integer32"""
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


_AlaAaaCpIntmIntvlTrstRadStatus_Type.__name__ = "Integer32"
_AlaAaaCpIntmIntvlTrstRadStatus_Object = MibScalar
alaAaaCpIntmIntvlTrstRadStatus = _AlaAaaCpIntmIntvlTrstRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 14),
    _AlaAaaCpIntmIntvlTrstRadStatus_Type()
)
alaAaaCpIntmIntvlTrstRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpIntmIntvlTrstRadStatus.setStatus("current")


class _AlaAaaCpSessTimeoutStatus_Type(Integer32):
    """Custom type alaAaaCpSessTimeoutStatus based on Integer32"""
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


_AlaAaaCpSessTimeoutStatus_Type.__name__ = "Integer32"
_AlaAaaCpSessTimeoutStatus_Object = MibScalar
alaAaaCpSessTimeoutStatus = _AlaAaaCpSessTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 15),
    _AlaAaaCpSessTimeoutStatus_Type()
)
alaAaaCpSessTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpSessTimeoutStatus.setStatus("current")


class _AlaAaaCpSessTimeoutIntrvl_Type(Integer32):
    """Custom type alaAaaCpSessTimeoutIntrvl based on Integer32"""
    defaultValue = 43200


_AlaAaaCpSessTimeoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaCpSessTimeoutIntrvl_Object = MibScalar
alaAaaCpSessTimeoutIntrvl = _AlaAaaCpSessTimeoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 16),
    _AlaAaaCpSessTimeoutIntrvl_Type()
)
alaAaaCpSessTimeoutIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpSessTimeoutIntrvl.setStatus("current")


class _AlaAaaCpSessTmotTrstRadStatus_Type(Integer32):
    """Custom type alaAaaCpSessTmotTrstRadStatus based on Integer32"""
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


_AlaAaaCpSessTmotTrstRadStatus_Type.__name__ = "Integer32"
_AlaAaaCpSessTmotTrstRadStatus_Object = MibScalar
alaAaaCpSessTmotTrstRadStatus = _AlaAaaCpSessTmotTrstRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 17),
    _AlaAaaCpSessTmotTrstRadStatus_Type()
)
alaAaaCpSessTmotTrstRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpSessTmotTrstRadStatus.setStatus("current")


class _AlaAaaCpInActLogoutStatus_Type(Integer32):
    """Custom type alaAaaCpInActLogoutStatus based on Integer32"""
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


_AlaAaaCpInActLogoutStatus_Type.__name__ = "Integer32"
_AlaAaaCpInActLogoutStatus_Object = MibScalar
alaAaaCpInActLogoutStatus = _AlaAaaCpInActLogoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 18),
    _AlaAaaCpInActLogoutStatus_Type()
)
alaAaaCpInActLogoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpInActLogoutStatus.setStatus("current")


class _AlaAaaCpInActLogoutIntrvl_Type(Integer32):
    """Custom type alaAaaCpInActLogoutIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaCpInActLogoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaCpInActLogoutIntrvl_Object = MibScalar
alaAaaCpInActLogoutIntrvl = _AlaAaaCpInActLogoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 19),
    _AlaAaaCpInActLogoutIntrvl_Type()
)
alaAaaCpInActLogoutIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCpInActLogoutIntrvl.setStatus("current")


class _AlaAaaTacacsServerCmdAuthorization_Type(Integer32):
    """Custom type alaAaaTacacsServerCmdAuthorization based on Integer32"""
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


_AlaAaaTacacsServerCmdAuthorization_Type.__name__ = "Integer32"
_AlaAaaTacacsServerCmdAuthorization_Object = MibScalar
alaAaaTacacsServerCmdAuthorization = _AlaAaaTacacsServerCmdAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 2, 6, 20),
    _AlaAaaTacacsServerCmdAuthorization_Type()
)
alaAaaTacacsServerCmdAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTacacsServerCmdAuthorization.setStatus("current")
_AaaUserMIB_ObjectIdentity = ObjectIdentity
aaaUserMIB = _AaaUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3)
)
_AaaUserTable_Object = MibTable
aaaUserTable = _AaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aaaUserTable.setStatus("current")
_AaaUserEntry_Object = MibTableRow
aaaUserEntry = _AaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1)
)
aaaUserEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaauUserName"),
)
if mibBuilder.loadTexts:
    aaaUserEntry.setStatus("current")


class _AaauUserName_Type(SnmpAdminString):
    """Custom type aaauUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AaauUserName_Type.__name__ = "SnmpAdminString"
_AaauUserName_Object = MibTableColumn
aaauUserName = _AaauUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 1),
    _AaauUserName_Type()
)
aaauUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaauUserName.setStatus("current")


class _AaauPassword_Type(SnmpAdminString):
    """Custom type aaauPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauPassword_Type.__name__ = "SnmpAdminString"
_AaauPassword_Object = MibTableColumn
aaauPassword = _AaauPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 2),
    _AaauPassword_Type()
)
aaauPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPassword.setStatus("current")


class _AaauReadRight1_Type(Unsigned32):
    """Custom type aaauReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight1_Type.__name__ = "Unsigned32"
_AaauReadRight1_Object = MibTableColumn
aaauReadRight1 = _AaauReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 3),
    _AaauReadRight1_Type()
)
aaauReadRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight1.setStatus("current")


class _AaauReadRight2_Type(Unsigned32):
    """Custom type aaauReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight2_Type.__name__ = "Unsigned32"
_AaauReadRight2_Object = MibTableColumn
aaauReadRight2 = _AaauReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 4),
    _AaauReadRight2_Type()
)
aaauReadRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight2.setStatus("current")


class _AaauWriteRight1_Type(Unsigned32):
    """Custom type aaauWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight1_Type.__name__ = "Unsigned32"
_AaauWriteRight1_Object = MibTableColumn
aaauWriteRight1 = _AaauWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 5),
    _AaauWriteRight1_Type()
)
aaauWriteRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight1.setStatus("current")


class _AaauWriteRight2_Type(Unsigned32):
    """Custom type aaauWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight2_Type.__name__ = "Unsigned32"
_AaauWriteRight2_Object = MibTableColumn
aaauWriteRight2 = _AaauWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 6),
    _AaauWriteRight2_Type()
)
aaauWriteRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight2.setStatus("current")


class _AaauSnmpLevel_Type(Integer32):
    """Custom type aaauSnmpLevel based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("noauth", 2),
          ("sha", 3),
          ("md5", 4),
          ("shaDes", 5),
          ("md5Des", 6),
          ("shaAes", 7),
          ("sha224", 8),
          ("sha256", 9))
    )


_AaauSnmpLevel_Type.__name__ = "Integer32"
_AaauSnmpLevel_Object = MibTableColumn
aaauSnmpLevel = _AaauSnmpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 7),
    _AaauSnmpLevel_Type()
)
aaauSnmpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauSnmpLevel.setStatus("current")


class _AaauSnmpAuthKey_Type(OctetString):
    """Custom type aaauSnmpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaauSnmpAuthKey_Type.__name__ = "OctetString"
_AaauSnmpAuthKey_Object = MibTableColumn
aaauSnmpAuthKey = _AaauSnmpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 8),
    _AaauSnmpAuthKey_Type()
)
aaauSnmpAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauSnmpAuthKey.setStatus("current")


class _AaauRowStatus_Type(RowStatus):
    """Custom type aaauRowStatus based on RowStatus"""
    defaultValue = 2


_AaauRowStatus_Type.__name__ = "RowStatus"
_AaauRowStatus_Object = MibTableColumn
aaauRowStatus = _AaauRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 9),
    _AaauRowStatus_Type()
)
aaauRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauRowStatus.setStatus("current")


class _AaauOldPassword_Type(SnmpAdminString):
    """Custom type aaauOldPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauOldPassword_Type.__name__ = "SnmpAdminString"
_AaauOldPassword_Object = MibTableColumn
aaauOldPassword = _AaauOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 10),
    _AaauOldPassword_Type()
)
aaauOldPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauOldPassword.setStatus("current")


class _AaauPasswordExpirationDate_Type(SnmpAdminString):
    """Custom type aaauPasswordExpirationDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordExpirationDate_Type.__name__ = "SnmpAdminString"
_AaauPasswordExpirationDate_Object = MibTableColumn
aaauPasswordExpirationDate = _AaauPasswordExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 11),
    _AaauPasswordExpirationDate_Type()
)
aaauPasswordExpirationDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationDate.setStatus("current")


class _AaauPasswordExpirationInMinute_Type(Integer32):
    """Custom type aaauPasswordExpirationInMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 216000),
    )


_AaauPasswordExpirationInMinute_Type.__name__ = "Integer32"
_AaauPasswordExpirationInMinute_Object = MibTableColumn
aaauPasswordExpirationInMinute = _AaauPasswordExpirationInMinute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 12),
    _AaauPasswordExpirationInMinute_Type()
)
aaauPasswordExpirationInMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationInMinute.setStatus("current")


class _AaauPasswordAllowModifyDate_Type(SnmpAdminString):
    """Custom type aaauPasswordAllowModifyDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordAllowModifyDate_Type.__name__ = "SnmpAdminString"
_AaauPasswordAllowModifyDate_Object = MibTableColumn
aaauPasswordAllowModifyDate = _AaauPasswordAllowModifyDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 13),
    _AaauPasswordAllowModifyDate_Type()
)
aaauPasswordAllowModifyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauPasswordAllowModifyDate.setStatus("current")


class _AaauPasswordLockoutEnable_Type(Integer32):
    """Custom type aaauPasswordLockoutEnable based on Integer32"""
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
        *(("lockout", 1),
          ("unlock", 2),
          ("expired", 3))
    )


_AaauPasswordLockoutEnable_Type.__name__ = "Integer32"
_AaauPasswordLockoutEnable_Object = MibTableColumn
aaauPasswordLockoutEnable = _AaauPasswordLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 14),
    _AaauPasswordLockoutEnable_Type()
)
aaauPasswordLockoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordLockoutEnable.setStatus("current")


class _AaauBadAtempts_Type(Integer32):
    """Custom type aaauBadAtempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaauBadAtempts_Type.__name__ = "Integer32"
_AaauBadAtempts_Object = MibTableColumn
aaauBadAtempts = _AaauBadAtempts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 15),
    _AaauBadAtempts_Type()
)
aaauBadAtempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauBadAtempts.setStatus("current")


class _AaauReadRight3_Type(Unsigned32):
    """Custom type aaauReadRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight3_Type.__name__ = "Unsigned32"
_AaauReadRight3_Object = MibTableColumn
aaauReadRight3 = _AaauReadRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 16),
    _AaauReadRight3_Type()
)
aaauReadRight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight3.setStatus("current")


class _AaauReadRight4_Type(Unsigned32):
    """Custom type aaauReadRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight4_Type.__name__ = "Unsigned32"
_AaauReadRight4_Object = MibTableColumn
aaauReadRight4 = _AaauReadRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 17),
    _AaauReadRight4_Type()
)
aaauReadRight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight4.setStatus("current")


class _AaauWriteRight3_Type(Unsigned32):
    """Custom type aaauWriteRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight3_Type.__name__ = "Unsigned32"
_AaauWriteRight3_Object = MibTableColumn
aaauWriteRight3 = _AaauWriteRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 18),
    _AaauWriteRight3_Type()
)
aaauWriteRight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight3.setStatus("current")


class _AaauWriteRight4_Type(Unsigned32):
    """Custom type aaauWriteRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight4_Type.__name__ = "Unsigned32"
_AaauWriteRight4_Object = MibTableColumn
aaauWriteRight4 = _AaauWriteRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 19),
    _AaauWriteRight4_Type()
)
aaauWriteRight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight4.setStatus("current")


class _AaauSnmpPrivPassword_Type(OctetString):
    """Custom type aaauSnmpPrivPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 30),
    )


_AaauSnmpPrivPassword_Type.__name__ = "OctetString"
_AaauSnmpPrivPassword_Object = MibTableColumn
aaauSnmpPrivPassword = _AaauSnmpPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 3, 1, 1, 20),
    _AaauSnmpPrivPassword_Type()
)
aaauSnmpPrivPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauSnmpPrivPassword.setStatus("current")
_AaaAsaConfig_ObjectIdentity = ObjectIdentity
aaaAsaConfig = _AaaAsaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4)
)


class _AaaAsaPasswordSizeMin_Type(Integer32):
    """Custom type aaaAsaPasswordSizeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AaaAsaPasswordSizeMin_Type.__name__ = "Integer32"
_AaaAsaPasswordSizeMin_Object = MibScalar
aaaAsaPasswordSizeMin = _AaaAsaPasswordSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 1),
    _AaaAsaPasswordSizeMin_Type()
)
aaaAsaPasswordSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordSizeMin.setStatus("current")


class _AaaAsaDefaultPasswordExpirationInDays_Type(Integer32):
    """Custom type aaaAsaDefaultPasswordExpirationInDays based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaDefaultPasswordExpirationInDays_Type.__name__ = "Integer32"
_AaaAsaDefaultPasswordExpirationInDays_Object = MibScalar
aaaAsaDefaultPasswordExpirationInDays = _AaaAsaDefaultPasswordExpirationInDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 2),
    _AaaAsaDefaultPasswordExpirationInDays_Type()
)
aaaAsaDefaultPasswordExpirationInDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaDefaultPasswordExpirationInDays.setStatus("current")


class _AaaAsaPasswordContainUserName_Type(Integer32):
    """Custom type aaaAsaPasswordContainUserName based on Integer32"""
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


_AaaAsaPasswordContainUserName_Type.__name__ = "Integer32"
_AaaAsaPasswordContainUserName_Object = MibScalar
aaaAsaPasswordContainUserName = _AaaAsaPasswordContainUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 3),
    _AaaAsaPasswordContainUserName_Type()
)
aaaAsaPasswordContainUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordContainUserName.setStatus("current")


class _AaaAsaPasswordMinUpperCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinUpperCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinUpperCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinUpperCase_Object = MibScalar
aaaAsaPasswordMinUpperCase = _AaaAsaPasswordMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 4),
    _AaaAsaPasswordMinUpperCase_Type()
)
aaaAsaPasswordMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinUpperCase.setStatus("current")


class _AaaAsaPasswordMinLowerCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinLowerCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinLowerCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinLowerCase_Object = MibScalar
aaaAsaPasswordMinLowerCase = _AaaAsaPasswordMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 5),
    _AaaAsaPasswordMinLowerCase_Type()
)
aaaAsaPasswordMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinLowerCase.setStatus("current")


class _AaaAsaPasswordMinDigit_Type(Integer32):
    """Custom type aaaAsaPasswordMinDigit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinDigit_Type.__name__ = "Integer32"
_AaaAsaPasswordMinDigit_Object = MibScalar
aaaAsaPasswordMinDigit = _AaaAsaPasswordMinDigit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 6),
    _AaaAsaPasswordMinDigit_Type()
)
aaaAsaPasswordMinDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinDigit.setStatus("current")


class _AaaAsaPasswordMinNonAlphan_Type(Integer32):
    """Custom type aaaAsaPasswordMinNonAlphan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinNonAlphan_Type.__name__ = "Integer32"
_AaaAsaPasswordMinNonAlphan_Object = MibScalar
aaaAsaPasswordMinNonAlphan = _AaaAsaPasswordMinNonAlphan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 7),
    _AaaAsaPasswordMinNonAlphan_Type()
)
aaaAsaPasswordMinNonAlphan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinNonAlphan.setStatus("current")


class _AaaAsaPasswordHistory_Type(Integer32):
    """Custom type aaaAsaPasswordHistory based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AaaAsaPasswordHistory_Type.__name__ = "Integer32"
_AaaAsaPasswordHistory_Object = MibScalar
aaaAsaPasswordHistory = _AaaAsaPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 8),
    _AaaAsaPasswordHistory_Type()
)
aaaAsaPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordHistory.setStatus("current")


class _AaaAsaPasswordMinAge_Type(Integer32):
    """Custom type aaaAsaPasswordMinAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaPasswordMinAge_Type.__name__ = "Integer32"
_AaaAsaPasswordMinAge_Object = MibScalar
aaaAsaPasswordMinAge = _AaaAsaPasswordMinAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 9),
    _AaaAsaPasswordMinAge_Type()
)
aaaAsaPasswordMinAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinAge.setStatus("current")


class _AaaAsaLockoutWindow_Type(Integer32):
    """Custom type aaaAsaLockoutWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutWindow_Type.__name__ = "Integer32"
_AaaAsaLockoutWindow_Object = MibScalar
aaaAsaLockoutWindow = _AaaAsaLockoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 10),
    _AaaAsaLockoutWindow_Type()
)
aaaAsaLockoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutWindow.setStatus("current")


class _AaaAsaLockoutDuration_Type(Integer32):
    """Custom type aaaAsaLockoutDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutDuration_Type.__name__ = "Integer32"
_AaaAsaLockoutDuration_Object = MibScalar
aaaAsaLockoutDuration = _AaaAsaLockoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 11),
    _AaaAsaLockoutDuration_Type()
)
aaaAsaLockoutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutDuration.setStatus("current")


class _AaaAsaLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaLockoutThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaLockoutThreshold_Object = MibScalar
aaaAsaLockoutThreshold = _AaaAsaLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 12),
    _AaaAsaLockoutThreshold_Type()
)
aaaAsaLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutThreshold.setStatus("current")


class _AaaAsaAccessPolicyAdminConsoleOnly_Type(Integer32):
    """Custom type aaaAsaAccessPolicyAdminConsoleOnly based on Integer32"""
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


_AaaAsaAccessPolicyAdminConsoleOnly_Type.__name__ = "Integer32"
_AaaAsaAccessPolicyAdminConsoleOnly_Object = MibScalar
aaaAsaAccessPolicyAdminConsoleOnly = _AaaAsaAccessPolicyAdminConsoleOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 13),
    _AaaAsaAccessPolicyAdminConsoleOnly_Type()
)
aaaAsaAccessPolicyAdminConsoleOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessPolicyAdminConsoleOnly.setStatus("current")


class _AaaAsaAccessMode_Type(Integer32):
    """Custom type aaaAsaAccessMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("enhanced", 2))
    )


_AaaAsaAccessMode_Type.__name__ = "Integer32"
_AaaAsaAccessMode_Object = MibScalar
aaaAsaAccessMode = _AaaAsaAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 14),
    _AaaAsaAccessMode_Type()
)
aaaAsaAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessMode.setStatus("current")


class _AaaAsaAccessIpLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaAccessIpLockoutThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaAccessIpLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaAccessIpLockoutThreshold_Object = MibScalar
aaaAsaAccessIpLockoutThreshold = _AaaAsaAccessIpLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 15),
    _AaaAsaAccessIpLockoutThreshold_Type()
)
aaaAsaAccessIpLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessIpLockoutThreshold.setStatus("current")


class _AaaAsaAccessManagementIpStatus_Type(Integer32):
    """Custom type aaaAsaAccessManagementIpStatus based on Integer32"""
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


_AaaAsaAccessManagementIpStatus_Type.__name__ = "Integer32"
_AaaAsaAccessManagementIpStatus_Object = MibScalar
aaaAsaAccessManagementIpStatus = _AaaAsaAccessManagementIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 4, 16),
    _AaaAsaAccessManagementIpStatus_Type()
)
aaaAsaAccessManagementIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessManagementIpStatus.setStatus("current")
_AlaAaaClientAttr_ObjectIdentity = ObjectIdentity
alaAaaClientAttr = _AlaAaaClientAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5)
)
_AlaAaaRadClientGlobalAttr_ObjectIdentity = ObjectIdentity
alaAaaRadClientGlobalAttr = _AlaAaaRadClientGlobalAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1)
)


class _AlaAaaRadNasPortId_Type(SnmpAdminString):
    """Custom type alaAaaRadNasPortId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadNasPortId_Type.__name__ = "SnmpAdminString"
_AlaAaaRadNasPortId_Object = MibScalar
alaAaaRadNasPortId = _AlaAaaRadNasPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 1),
    _AlaAaaRadNasPortId_Type()
)
alaAaaRadNasPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadNasPortId.setStatus("current")


class _AlaAaaRadNasIdentifier_Type(SnmpAdminString):
    """Custom type alaAaaRadNasIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadNasIdentifier_Type.__name__ = "SnmpAdminString"
_AlaAaaRadNasIdentifier_Object = MibScalar
alaAaaRadNasIdentifier = _AlaAaaRadNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 2),
    _AlaAaaRadNasIdentifier_Type()
)
alaAaaRadNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadNasIdentifier.setStatus("current")


class _AlaAaaRadUserNameDelim_Type(SnmpAdminString):
    """Custom type alaAaaRadUserNameDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadUserNameDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaRadUserNameDelim_Object = MibScalar
alaAaaRadUserNameDelim = _AlaAaaRadUserNameDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 3),
    _AlaAaaRadUserNameDelim_Type()
)
alaAaaRadUserNameDelim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadUserNameDelim.setStatus("current")


class _AlaAaaRadPasswordDelim_Type(SnmpAdminString):
    """Custom type alaAaaRadPasswordDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadPasswordDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaRadPasswordDelim_Object = MibScalar
alaAaaRadPasswordDelim = _AlaAaaRadPasswordDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 4),
    _AlaAaaRadPasswordDelim_Type()
)
alaAaaRadPasswordDelim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadPasswordDelim.setStatus("current")


class _AlaAaaRadCallnStnIdDelim_Type(SnmpAdminString):
    """Custom type alaAaaRadCallnStnIdDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadCallnStnIdDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaRadCallnStnIdDelim_Object = MibScalar
alaAaaRadCallnStnIdDelim = _AlaAaaRadCallnStnIdDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 5),
    _AlaAaaRadCallnStnIdDelim_Type()
)
alaAaaRadCallnStnIdDelim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadCallnStnIdDelim.setStatus("current")


class _AlaAaaRadCalldStnIdDelim_Type(SnmpAdminString):
    """Custom type alaAaaRadCalldStnIdDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadCalldStnIdDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaRadCalldStnIdDelim_Object = MibScalar
alaAaaRadCalldStnIdDelim = _AlaAaaRadCalldStnIdDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 6),
    _AlaAaaRadCalldStnIdDelim_Type()
)
alaAaaRadCalldStnIdDelim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadCalldStnIdDelim.setStatus("current")


class _AlaAaaRadUserNameCase_Type(Integer32):
    """Custom type alaAaaRadUserNameCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaRadUserNameCase_Type.__name__ = "Integer32"
_AlaAaaRadUserNameCase_Object = MibScalar
alaAaaRadUserNameCase = _AlaAaaRadUserNameCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 7),
    _AlaAaaRadUserNameCase_Type()
)
alaAaaRadUserNameCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadUserNameCase.setStatus("current")


class _AlaAaaRadPasswordCase_Type(Integer32):
    """Custom type alaAaaRadPasswordCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaRadPasswordCase_Type.__name__ = "Integer32"
_AlaAaaRadPasswordCase_Object = MibScalar
alaAaaRadPasswordCase = _AlaAaaRadPasswordCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 8),
    _AlaAaaRadPasswordCase_Type()
)
alaAaaRadPasswordCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadPasswordCase.setStatus("current")


class _AlaAaaRadCallingStationIdCase_Type(Integer32):
    """Custom type alaAaaRadCallingStationIdCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaRadCallingStationIdCase_Type.__name__ = "Integer32"
_AlaAaaRadCallingStationIdCase_Object = MibScalar
alaAaaRadCallingStationIdCase = _AlaAaaRadCallingStationIdCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 9),
    _AlaAaaRadCallingStationIdCase_Type()
)
alaAaaRadCallingStationIdCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadCallingStationIdCase.setStatus("current")


class _AlaAaaRadCalledStationIdCase_Type(Integer32):
    """Custom type alaAaaRadCalledStationIdCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaRadCalledStationIdCase_Type.__name__ = "Integer32"
_AlaAaaRadCalledStationIdCase_Object = MibScalar
alaAaaRadCalledStationIdCase = _AlaAaaRadCalledStationIdCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 5, 1, 10),
    _AlaAaaRadCalledStationIdCase_Type()
)
alaAaaRadCalledStationIdCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadCalledStationIdCase.setStatus("current")
_AlaAaaProfileObjects_ObjectIdentity = ObjectIdentity
alaAaaProfileObjects = _AlaAaaProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6)
)
_AlaAaaProfileConfig_ObjectIdentity = ObjectIdentity
alaAaaProfileConfig = _AlaAaaProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1)
)
_AlaAaaProfTable_Object = MibTable
alaAaaProfTable = _AlaAaaProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    alaAaaProfTable.setStatus("current")
_AlaAaaProfEntry_Object = MibTableRow
alaAaaProfEntry = _AlaAaaProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1)
)
alaAaaProfEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "alaAaaProfName"),
)
if mibBuilder.loadTexts:
    alaAaaProfEntry.setStatus("current")


class _AlaAaaProfName_Type(SnmpAdminString):
    """Custom type alaAaaProfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaAaaProfName_Type.__name__ = "SnmpAdminString"
_AlaAaaProfName_Object = MibTableColumn
alaAaaProfName = _AlaAaaProfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 1),
    _AlaAaaProfName_Type()
)
alaAaaProfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAaaProfName.setStatus("current")


class _AlaAaaProfOnexReAuthSts_Type(Integer32):
    """Custom type alaAaaProfOnexReAuthSts based on Integer32"""
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


_AlaAaaProfOnexReAuthSts_Type.__name__ = "Integer32"
_AlaAaaProfOnexReAuthSts_Object = MibTableColumn
alaAaaProfOnexReAuthSts = _AlaAaaProfOnexReAuthSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 2),
    _AlaAaaProfOnexReAuthSts_Type()
)
alaAaaProfOnexReAuthSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfOnexReAuthSts.setStatus("current")


class _AlaAaaProfOnexReAuthIntrvl_Type(Integer32):
    """Custom type alaAaaProfOnexReAuthIntrvl based on Integer32"""
    defaultValue = 3600


_AlaAaaProfOnexReAuthIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfOnexReAuthIntrvl_Object = MibTableColumn
alaAaaProfOnexReAuthIntrvl = _AlaAaaProfOnexReAuthIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 3),
    _AlaAaaProfOnexReAuthIntrvl_Type()
)
alaAaaProfOnexReAuthIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfOnexReAuthIntrvl.setStatus("current")


class _AlaAaaProfOnexReAuthTrstRadSts_Type(Integer32):
    """Custom type alaAaaProfOnexReAuthTrstRadSts based on Integer32"""
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


_AlaAaaProfOnexReAuthTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfOnexReAuthTrstRadSts_Object = MibTableColumn
alaAaaProfOnexReAuthTrstRadSts = _AlaAaaProfOnexReAuthTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 4),
    _AlaAaaProfOnexReAuthTrstRadSts_Type()
)
alaAaaProfOnexReAuthTrstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfOnexReAuthTrstRadSts.setStatus("current")


class _AlaAaaProfOnexIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaProfOnexIntrmIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaProfOnexIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfOnexIntrmIntrvl_Object = MibTableColumn
alaAaaProfOnexIntrmIntrvl = _AlaAaaProfOnexIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 5),
    _AlaAaaProfOnexIntrmIntrvl_Type()
)
alaAaaProfOnexIntrmIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfOnexIntrmIntrvl.setStatus("current")


class _AlaAaaProfOnexIntmItvlTstRadSts_Type(Integer32):
    """Custom type alaAaaProfOnexIntmItvlTstRadSts based on Integer32"""
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


_AlaAaaProfOnexIntmItvlTstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfOnexIntmItvlTstRadSts_Object = MibTableColumn
alaAaaProfOnexIntmItvlTstRadSts = _AlaAaaProfOnexIntmItvlTstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 6),
    _AlaAaaProfOnexIntmItvlTstRadSts_Type()
)
alaAaaProfOnexIntmItvlTstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfOnexIntmItvlTstRadSts.setStatus("current")


class _AlaAaaProfMacIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaProfMacIntrmIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaProfMacIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfMacIntrmIntrvl_Object = MibTableColumn
alaAaaProfMacIntrmIntrvl = _AlaAaaProfMacIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 7),
    _AlaAaaProfMacIntrmIntrvl_Type()
)
alaAaaProfMacIntrmIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacIntrmIntrvl.setStatus("current")


class _AlaAaaProfMacIntmItvlTrstRadSts_Type(Integer32):
    """Custom type alaAaaProfMacIntmItvlTrstRadSts based on Integer32"""
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


_AlaAaaProfMacIntmItvlTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfMacIntmItvlTrstRadSts_Object = MibTableColumn
alaAaaProfMacIntmItvlTrstRadSts = _AlaAaaProfMacIntmItvlTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 8),
    _AlaAaaProfMacIntmItvlTrstRadSts_Type()
)
alaAaaProfMacIntmItvlTrstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacIntmItvlTrstRadSts.setStatus("current")


class _AlaAaaProfMacSessTimeoutSts_Type(Integer32):
    """Custom type alaAaaProfMacSessTimeoutSts based on Integer32"""
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


_AlaAaaProfMacSessTimeoutSts_Type.__name__ = "Integer32"
_AlaAaaProfMacSessTimeoutSts_Object = MibTableColumn
alaAaaProfMacSessTimeoutSts = _AlaAaaProfMacSessTimeoutSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 9),
    _AlaAaaProfMacSessTimeoutSts_Type()
)
alaAaaProfMacSessTimeoutSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacSessTimeoutSts.setStatus("current")


class _AlaAaaProfMacSessTimeoutIntrvl_Type(Integer32):
    """Custom type alaAaaProfMacSessTimeoutIntrvl based on Integer32"""
    defaultValue = 43200


_AlaAaaProfMacSessTimeoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfMacSessTimeoutIntrvl_Object = MibTableColumn
alaAaaProfMacSessTimeoutIntrvl = _AlaAaaProfMacSessTimeoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 10),
    _AlaAaaProfMacSessTimeoutIntrvl_Type()
)
alaAaaProfMacSessTimeoutIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacSessTimeoutIntrvl.setStatus("current")


class _AlaAaaProfMacSessTmoutTrstRadSts_Type(Integer32):
    """Custom type alaAaaProfMacSessTmoutTrstRadSts based on Integer32"""
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


_AlaAaaProfMacSessTmoutTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfMacSessTmoutTrstRadSts_Object = MibTableColumn
alaAaaProfMacSessTmoutTrstRadSts = _AlaAaaProfMacSessTmoutTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 11),
    _AlaAaaProfMacSessTmoutTrstRadSts_Type()
)
alaAaaProfMacSessTmoutTrstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacSessTmoutTrstRadSts.setStatus("current")


class _AlaAaaProfMacInActLogoutSts_Type(Integer32):
    """Custom type alaAaaProfMacInActLogoutSts based on Integer32"""
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


_AlaAaaProfMacInActLogoutSts_Type.__name__ = "Integer32"
_AlaAaaProfMacInActLogoutSts_Object = MibTableColumn
alaAaaProfMacInActLogoutSts = _AlaAaaProfMacInActLogoutSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 12),
    _AlaAaaProfMacInActLogoutSts_Type()
)
alaAaaProfMacInActLogoutSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacInActLogoutSts.setStatus("current")


class _AlaAaaProfMacInActLogoutIntrvl_Type(Integer32):
    """Custom type alaAaaProfMacInActLogoutIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaProfMacInActLogoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfMacInActLogoutIntrvl_Object = MibTableColumn
alaAaaProfMacInActLogoutIntrvl = _AlaAaaProfMacInActLogoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 13),
    _AlaAaaProfMacInActLogoutIntrvl_Type()
)
alaAaaProfMacInActLogoutIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfMacInActLogoutIntrvl.setStatus("current")


class _AlaAaaProfCpSessTimeoutSts_Type(Integer32):
    """Custom type alaAaaProfCpSessTimeoutSts based on Integer32"""
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


_AlaAaaProfCpSessTimeoutSts_Type.__name__ = "Integer32"
_AlaAaaProfCpSessTimeoutSts_Object = MibTableColumn
alaAaaProfCpSessTimeoutSts = _AlaAaaProfCpSessTimeoutSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 14),
    _AlaAaaProfCpSessTimeoutSts_Type()
)
alaAaaProfCpSessTimeoutSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpSessTimeoutSts.setStatus("current")


class _AlaAaaProfCpSessTimeoutIntrvl_Type(Integer32):
    """Custom type alaAaaProfCpSessTimeoutIntrvl based on Integer32"""
    defaultValue = 432000


_AlaAaaProfCpSessTimeoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfCpSessTimeoutIntrvl_Object = MibTableColumn
alaAaaProfCpSessTimeoutIntrvl = _AlaAaaProfCpSessTimeoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 15),
    _AlaAaaProfCpSessTimeoutIntrvl_Type()
)
alaAaaProfCpSessTimeoutIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpSessTimeoutIntrvl.setStatus("current")


class _AlaAaaProfCpSessTmotTrstRadSts_Type(Integer32):
    """Custom type alaAaaProfCpSessTmotTrstRadSts based on Integer32"""
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


_AlaAaaProfCpSessTmotTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfCpSessTmotTrstRadSts_Object = MibTableColumn
alaAaaProfCpSessTmotTrstRadSts = _AlaAaaProfCpSessTmotTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 16),
    _AlaAaaProfCpSessTmotTrstRadSts_Type()
)
alaAaaProfCpSessTmotTrstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpSessTmotTrstRadSts.setStatus("current")


class _AlaAaaProfCpInActLogoutSts_Type(Integer32):
    """Custom type alaAaaProfCpInActLogoutSts based on Integer32"""
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


_AlaAaaProfCpInActLogoutSts_Type.__name__ = "Integer32"
_AlaAaaProfCpInActLogoutSts_Object = MibTableColumn
alaAaaProfCpInActLogoutSts = _AlaAaaProfCpInActLogoutSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 17),
    _AlaAaaProfCpInActLogoutSts_Type()
)
alaAaaProfCpInActLogoutSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpInActLogoutSts.setStatus("current")


class _AlaAaaProfCpInActLogoutIntrvl_Type(Integer32):
    """Custom type alaAaaProfCpInActLogoutIntrvl based on Integer32"""
    defaultValue = 600


_AlaAaaProfCpInActLogoutIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfCpInActLogoutIntrvl_Object = MibTableColumn
alaAaaProfCpInActLogoutIntrvl = _AlaAaaProfCpInActLogoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 18),
    _AlaAaaProfCpInActLogoutIntrvl_Type()
)
alaAaaProfCpInActLogoutIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpInActLogoutIntrvl.setStatus("current")


class _AlaAaaProfCpIntrmIntrvl_Type(Integer32):
    """Custom type alaAaaProfCpIntrmIntrvl based on Integer32"""
    defaultValue = 43200


_AlaAaaProfCpIntrmIntrvl_Type.__name__ = "Integer32"
_AlaAaaProfCpIntrmIntrvl_Object = MibTableColumn
alaAaaProfCpIntrmIntrvl = _AlaAaaProfCpIntrmIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 19),
    _AlaAaaProfCpIntrmIntrvl_Type()
)
alaAaaProfCpIntrmIntrvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpIntrmIntrvl.setStatus("current")


class _AlaAaaProfCpItrmIntlTrstRadSts_Type(Integer32):
    """Custom type alaAaaProfCpItrmIntlTrstRadSts based on Integer32"""
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


_AlaAaaProfCpItrmIntlTrstRadSts_Type.__name__ = "Integer32"
_AlaAaaProfCpItrmIntlTrstRadSts_Object = MibTableColumn
alaAaaProfCpItrmIntlTrstRadSts = _AlaAaaProfCpItrmIntlTrstRadSts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 20),
    _AlaAaaProfCpItrmIntlTrstRadSts_Type()
)
alaAaaProfCpItrmIntlTrstRadSts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfCpItrmIntlTrstRadSts.setStatus("current")


class _AlaAaaProfRadNasPortId_Type(SnmpAdminString):
    """Custom type alaAaaProfRadNasPortId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadNasPortId_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadNasPortId_Object = MibTableColumn
alaAaaProfRadNasPortId = _AlaAaaProfRadNasPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 21),
    _AlaAaaProfRadNasPortId_Type()
)
alaAaaProfRadNasPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadNasPortId.setStatus("current")


class _AlaAaaProfRadNasIdentifier_Type(SnmpAdminString):
    """Custom type alaAaaProfRadNasIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadNasIdentifier_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadNasIdentifier_Object = MibTableColumn
alaAaaProfRadNasIdentifier = _AlaAaaProfRadNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 22),
    _AlaAaaProfRadNasIdentifier_Type()
)
alaAaaProfRadNasIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadNasIdentifier.setStatus("current")


class _AlaAaaProfRadUserNameDelim_Type(SnmpAdminString):
    """Custom type alaAaaProfRadUserNameDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadUserNameDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadUserNameDelim_Object = MibTableColumn
alaAaaProfRadUserNameDelim = _AlaAaaProfRadUserNameDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 23),
    _AlaAaaProfRadUserNameDelim_Type()
)
alaAaaProfRadUserNameDelim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadUserNameDelim.setStatus("current")


class _AlaAaaProfRadPasswrdDelim_Type(SnmpAdminString):
    """Custom type alaAaaProfRadPasswrdDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadPasswrdDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadPasswrdDelim_Object = MibTableColumn
alaAaaProfRadPasswrdDelim = _AlaAaaProfRadPasswrdDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 24),
    _AlaAaaProfRadPasswrdDelim_Type()
)
alaAaaProfRadPasswrdDelim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadPasswrdDelim.setStatus("current")


class _AlaAaaProfRadCallnStnIdDelim_Type(SnmpAdminString):
    """Custom type alaAaaProfRadCallnStnIdDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadCallnStnIdDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadCallnStnIdDelim_Object = MibTableColumn
alaAaaProfRadCallnStnIdDelim = _AlaAaaProfRadCallnStnIdDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 25),
    _AlaAaaProfRadCallnStnIdDelim_Type()
)
alaAaaProfRadCallnStnIdDelim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadCallnStnIdDelim.setStatus("current")


class _AlaAaaProfRadCalldStnIdDelim_Type(SnmpAdminString):
    """Custom type alaAaaProfRadCalldStnIdDelim based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfRadCalldStnIdDelim_Type.__name__ = "SnmpAdminString"
_AlaAaaProfRadCalldStnIdDelim_Object = MibTableColumn
alaAaaProfRadCalldStnIdDelim = _AlaAaaProfRadCalldStnIdDelim_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 26),
    _AlaAaaProfRadCalldStnIdDelim_Type()
)
alaAaaProfRadCalldStnIdDelim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadCalldStnIdDelim.setStatus("current")


class _AlaAaaProfRadUserNameCase_Type(Integer32):
    """Custom type alaAaaProfRadUserNameCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaProfRadUserNameCase_Type.__name__ = "Integer32"
_AlaAaaProfRadUserNameCase_Object = MibTableColumn
alaAaaProfRadUserNameCase = _AlaAaaProfRadUserNameCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 27),
    _AlaAaaProfRadUserNameCase_Type()
)
alaAaaProfRadUserNameCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadUserNameCase.setStatus("current")


class _AlaAaaProfRadPasswordCase_Type(Integer32):
    """Custom type alaAaaProfRadPasswordCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaProfRadPasswordCase_Type.__name__ = "Integer32"
_AlaAaaProfRadPasswordCase_Object = MibTableColumn
alaAaaProfRadPasswordCase = _AlaAaaProfRadPasswordCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 28),
    _AlaAaaProfRadPasswordCase_Type()
)
alaAaaProfRadPasswordCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadPasswordCase.setStatus("current")


class _AlaAaaProfRadCallnStnIdCase_Type(Integer32):
    """Custom type alaAaaProfRadCallnStnIdCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaProfRadCallnStnIdCase_Type.__name__ = "Integer32"
_AlaAaaProfRadCallnStnIdCase_Object = MibTableColumn
alaAaaProfRadCallnStnIdCase = _AlaAaaProfRadCallnStnIdCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 29),
    _AlaAaaProfRadCallnStnIdCase_Type()
)
alaAaaProfRadCallnStnIdCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadCallnStnIdCase.setStatus("current")


class _AlaAaaProfRadCalldStnIdCase_Type(Integer32):
    """Custom type alaAaaProfRadCalldStnIdCase based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 1),
          ("upperCase", 2))
    )


_AlaAaaProfRadCalldStnIdCase_Type.__name__ = "Integer32"
_AlaAaaProfRadCalldStnIdCase_Object = MibTableColumn
alaAaaProfRadCalldStnIdCase = _AlaAaaProfRadCalldStnIdCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 30),
    _AlaAaaProfRadCalldStnIdCase_Type()
)
alaAaaProfRadCalldStnIdCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRadCalldStnIdCase.setStatus("current")


class _AlaAaaProfRowStatus_Type(RowStatus):
    """Custom type alaAaaProfRowStatus based on RowStatus"""
    defaultValue = 2


_AlaAaaProfRowStatus_Type.__name__ = "RowStatus"
_AlaAaaProfRowStatus_Object = MibTableColumn
alaAaaProfRowStatus = _AlaAaaProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 1, 1, 31),
    _AlaAaaProfRowStatus_Type()
)
alaAaaProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfRowStatus.setStatus("current")
_AlaAaaProfAuthTable_Object = MibTable
alaAaaProfAuthTable = _AlaAaaProfAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    alaAaaProfAuthTable.setStatus("current")
_AlaAaaProfAuthEntry_Object = MibTableRow
alaAaaProfAuthEntry = _AlaAaaProfAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1)
)
alaAaaProfAuthEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "alaAaaProfName"),
    (0, "ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthInterface"),
)
if mibBuilder.loadTexts:
    alaAaaProfAuthEntry.setStatus("current")


class _AlaAaaProfAuthInterface_Type(Integer32):
    """Custom type alaAaaProfAuthInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("dot1x", 2),
          ("captivePortal", 3))
    )


_AlaAaaProfAuthInterface_Type.__name__ = "Integer32"
_AlaAaaProfAuthInterface_Object = MibTableColumn
alaAaaProfAuthInterface = _AlaAaaProfAuthInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 1),
    _AlaAaaProfAuthInterface_Type()
)
alaAaaProfAuthInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAaaProfAuthInterface.setStatus("current")


class _AlaAaaProfAuthSrvName1_Type(SnmpAdminString):
    """Custom type alaAaaProfAuthSrvName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAuthSrvName1_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAuthSrvName1_Object = MibTableColumn
alaAaaProfAuthSrvName1 = _AlaAaaProfAuthSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 2),
    _AlaAaaProfAuthSrvName1_Type()
)
alaAaaProfAuthSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAuthSrvName1.setStatus("current")


class _AlaAaaProfAuthSrvName2_Type(SnmpAdminString):
    """Custom type alaAaaProfAuthSrvName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAuthSrvName2_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAuthSrvName2_Object = MibTableColumn
alaAaaProfAuthSrvName2 = _AlaAaaProfAuthSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 3),
    _AlaAaaProfAuthSrvName2_Type()
)
alaAaaProfAuthSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAuthSrvName2.setStatus("current")


class _AlaAaaProfAuthSrvName3_Type(SnmpAdminString):
    """Custom type alaAaaProfAuthSrvName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAuthSrvName3_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAuthSrvName3_Object = MibTableColumn
alaAaaProfAuthSrvName3 = _AlaAaaProfAuthSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 4),
    _AlaAaaProfAuthSrvName3_Type()
)
alaAaaProfAuthSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAuthSrvName3.setStatus("current")


class _AlaAaaProfAuthSrvName4_Type(SnmpAdminString):
    """Custom type alaAaaProfAuthSrvName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAuthSrvName4_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAuthSrvName4_Object = MibTableColumn
alaAaaProfAuthSrvName4 = _AlaAaaProfAuthSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 5),
    _AlaAaaProfAuthSrvName4_Type()
)
alaAaaProfAuthSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAuthSrvName4.setStatus("current")


class _AlaAaaProfAuthRowStatus_Type(RowStatus):
    """Custom type alaAaaProfAuthRowStatus based on RowStatus"""
    defaultValue = 2


_AlaAaaProfAuthRowStatus_Type.__name__ = "RowStatus"
_AlaAaaProfAuthRowStatus_Object = MibTableColumn
alaAaaProfAuthRowStatus = _AlaAaaProfAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 2, 1, 6),
    _AlaAaaProfAuthRowStatus_Type()
)
alaAaaProfAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAuthRowStatus.setStatus("current")
_AlaAaaProfAcctTable_Object = MibTable
alaAaaProfAcctTable = _AlaAaaProfAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    alaAaaProfAcctTable.setStatus("current")
_AlaAaaProfAcctEntry_Object = MibTableRow
alaAaaProfAcctEntry = _AlaAaaProfAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1)
)
alaAaaProfAcctEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "alaAaaProfName"),
    (0, "ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctInterface"),
)
if mibBuilder.loadTexts:
    alaAaaProfAcctEntry.setStatus("current")


class _AlaAaaProfAcctInterface_Type(Integer32):
    """Custom type alaAaaProfAcctInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("dot1x", 2),
          ("captivePortal", 3))
    )


_AlaAaaProfAcctInterface_Type.__name__ = "Integer32"
_AlaAaaProfAcctInterface_Object = MibTableColumn
alaAaaProfAcctInterface = _AlaAaaProfAcctInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 1),
    _AlaAaaProfAcctInterface_Type()
)
alaAaaProfAcctInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAaaProfAcctInterface.setStatus("current")


class _AlaAaaProfAcctSrvName1_Type(SnmpAdminString):
    """Custom type alaAaaProfAcctSrvName1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAcctSrvName1_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAcctSrvName1_Object = MibTableColumn
alaAaaProfAcctSrvName1 = _AlaAaaProfAcctSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 2),
    _AlaAaaProfAcctSrvName1_Type()
)
alaAaaProfAcctSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSrvName1.setStatus("current")


class _AlaAaaProfAcctSrvName2_Type(SnmpAdminString):
    """Custom type alaAaaProfAcctSrvName2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAcctSrvName2_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAcctSrvName2_Object = MibTableColumn
alaAaaProfAcctSrvName2 = _AlaAaaProfAcctSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 3),
    _AlaAaaProfAcctSrvName2_Type()
)
alaAaaProfAcctSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSrvName2.setStatus("current")


class _AlaAaaProfAcctSrvName3_Type(SnmpAdminString):
    """Custom type alaAaaProfAcctSrvName3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAcctSrvName3_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAcctSrvName3_Object = MibTableColumn
alaAaaProfAcctSrvName3 = _AlaAaaProfAcctSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 4),
    _AlaAaaProfAcctSrvName3_Type()
)
alaAaaProfAcctSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSrvName3.setStatus("current")


class _AlaAaaProfAcctSrvName4_Type(SnmpAdminString):
    """Custom type alaAaaProfAcctSrvName4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaProfAcctSrvName4_Type.__name__ = "SnmpAdminString"
_AlaAaaProfAcctSrvName4_Object = MibTableColumn
alaAaaProfAcctSrvName4 = _AlaAaaProfAcctSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 5),
    _AlaAaaProfAcctSrvName4_Type()
)
alaAaaProfAcctSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSrvName4.setStatus("current")
_AlaAaaProfAcctSyslogIPAddrType_Type = InetAddressType
_AlaAaaProfAcctSyslogIPAddrType_Object = MibTableColumn
alaAaaProfAcctSyslogIPAddrType = _AlaAaaProfAcctSyslogIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 6),
    _AlaAaaProfAcctSyslogIPAddrType_Type()
)
alaAaaProfAcctSyslogIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSyslogIPAddrType.setStatus("current")
_AlaAaaProfAcctSyslogIPAddr_Type = InetAddress
_AlaAaaProfAcctSyslogIPAddr_Object = MibTableColumn
alaAaaProfAcctSyslogIPAddr = _AlaAaaProfAcctSyslogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 7),
    _AlaAaaProfAcctSyslogIPAddr_Type()
)
alaAaaProfAcctSyslogIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSyslogIPAddr.setStatus("current")


class _AlaAaaProfAcctSyslogUdpPort_Type(Unsigned32):
    """Custom type alaAaaProfAcctSyslogUdpPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaAaaProfAcctSyslogUdpPort_Type.__name__ = "Unsigned32"
_AlaAaaProfAcctSyslogUdpPort_Object = MibTableColumn
alaAaaProfAcctSyslogUdpPort = _AlaAaaProfAcctSyslogUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 8),
    _AlaAaaProfAcctSyslogUdpPort_Type()
)
alaAaaProfAcctSyslogUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctSyslogUdpPort.setStatus("current")


class _AlaAaaProfAcctCalingStationId_Type(Integer32):
    """Custom type alaAaaProfAcctCalingStationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2))
    )


_AlaAaaProfAcctCalingStationId_Type.__name__ = "Integer32"
_AlaAaaProfAcctCalingStationId_Object = MibTableColumn
alaAaaProfAcctCalingStationId = _AlaAaaProfAcctCalingStationId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 9),
    _AlaAaaProfAcctCalingStationId_Type()
)
alaAaaProfAcctCalingStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctCalingStationId.setStatus("current")


class _AlaAaaProfAcctRowStatus_Type(RowStatus):
    """Custom type alaAaaProfAcctRowStatus based on RowStatus"""
    defaultValue = 2


_AlaAaaProfAcctRowStatus_Type.__name__ = "RowStatus"
_AlaAaaProfAcctRowStatus_Object = MibTableColumn
alaAaaProfAcctRowStatus = _AlaAaaProfAcctRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 3, 1, 10),
    _AlaAaaProfAcctRowStatus_Type()
)
alaAaaProfAcctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaAaaProfAcctRowStatus.setStatus("current")


class _AlaAaaUserProfileSave_Type(Integer32):
    """Custom type alaAaaUserProfileSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("userProfile", 1),
          ("globalProfile", 2))
    )


_AlaAaaUserProfileSave_Type.__name__ = "Integer32"
_AlaAaaUserProfileSave_Object = MibScalar
alaAaaUserProfileSave = _AlaAaaUserProfileSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 6, 1, 4),
    _AlaAaaUserProfileSave_Type()
)
alaAaaUserProfileSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaUserProfileSave.setStatus("current")
_AaaSwitchAccessConfig_ObjectIdentity = ObjectIdentity
aaaSwitchAccessConfig = _AaaSwitchAccessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7)
)
_AaaSwitchAccessMgmtStationTable_Object = MibTable
aaaSwitchAccessMgmtStationTable = _AaaSwitchAccessMgmtStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationTable.setStatus("current")
_AaaSwitchAccessMgmtStationEntry_Object = MibTableRow
aaaSwitchAccessMgmtStationEntry = _AaaSwitchAccessMgmtStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1, 1)
)
aaaSwitchAccessMgmtStationEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessMgmtStationIpType"),
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessMgmtStationIpAddress"),
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessMgmtStationIpPrefixLength"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationEntry.setStatus("current")


class _AaaSwitchAccessMgmtStationIpType_Type(InetAddressType):
    """Custom type aaaSwitchAccessMgmtStationIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1))
    )


_AaaSwitchAccessMgmtStationIpType_Type.__name__ = "InetAddressType"
_AaaSwitchAccessMgmtStationIpType_Object = MibTableColumn
aaaSwitchAccessMgmtStationIpType = _AaaSwitchAccessMgmtStationIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1, 1, 1),
    _AaaSwitchAccessMgmtStationIpType_Type()
)
aaaSwitchAccessMgmtStationIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationIpType.setStatus("current")


class _AaaSwitchAccessMgmtStationIpAddress_Type(InetAddress):
    """Custom type aaaSwitchAccessMgmtStationIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AaaSwitchAccessMgmtStationIpAddress_Type.__name__ = "InetAddress"
_AaaSwitchAccessMgmtStationIpAddress_Object = MibTableColumn
aaaSwitchAccessMgmtStationIpAddress = _AaaSwitchAccessMgmtStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1, 1, 2),
    _AaaSwitchAccessMgmtStationIpAddress_Type()
)
aaaSwitchAccessMgmtStationIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationIpAddress.setStatus("current")
_AaaSwitchAccessMgmtStationIpPrefixLength_Type = InetAddressPrefixLength
_AaaSwitchAccessMgmtStationIpPrefixLength_Object = MibTableColumn
aaaSwitchAccessMgmtStationIpPrefixLength = _AaaSwitchAccessMgmtStationIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1, 1, 3),
    _AaaSwitchAccessMgmtStationIpPrefixLength_Type()
)
aaaSwitchAccessMgmtStationIpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationIpPrefixLength.setStatus("current")
_AaaSwitchAccessMgmtStationRowStatus_Type = RowStatus
_AaaSwitchAccessMgmtStationRowStatus_Object = MibTableColumn
aaaSwitchAccessMgmtStationRowStatus = _AaaSwitchAccessMgmtStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 1, 1, 4),
    _AaaSwitchAccessMgmtStationRowStatus_Type()
)
aaaSwitchAccessMgmtStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationRowStatus.setStatus("current")
_AaaSwitchAccessBannedIpTable_Object = MibTable
aaaSwitchAccessBannedIpTable = _AaaSwitchAccessBannedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpTable.setStatus("current")
_AaaSwitchAccessBannedIpEntry_Object = MibTableRow
aaaSwitchAccessBannedIpEntry = _AaaSwitchAccessBannedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 2, 1)
)
aaaSwitchAccessBannedIpEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessBannedIpType"),
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessBannedIpAddress"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpEntry.setStatus("current")
_AaaSwitchAccessBannedIpType_Type = InetAddressType
_AaaSwitchAccessBannedIpType_Object = MibTableColumn
aaaSwitchAccessBannedIpType = _AaaSwitchAccessBannedIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 2, 1, 1),
    _AaaSwitchAccessBannedIpType_Type()
)
aaaSwitchAccessBannedIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpType.setStatus("current")


class _AaaSwitchAccessBannedIpAddress_Type(InetAddress):
    """Custom type aaaSwitchAccessBannedIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AaaSwitchAccessBannedIpAddress_Type.__name__ = "InetAddress"
_AaaSwitchAccessBannedIpAddress_Object = MibTableColumn
aaaSwitchAccessBannedIpAddress = _AaaSwitchAccessBannedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 2, 1, 2),
    _AaaSwitchAccessBannedIpAddress_Type()
)
aaaSwitchAccessBannedIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpAddress.setStatus("current")
_AaaSwitchAccessBannedIpRowStatus_Type = RowStatus
_AaaSwitchAccessBannedIpRowStatus_Object = MibTableColumn
aaaSwitchAccessBannedIpRowStatus = _AaaSwitchAccessBannedIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 2, 1, 3),
    _AaaSwitchAccessBannedIpRowStatus_Type()
)
aaaSwitchAccessBannedIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpRowStatus.setStatus("current")
_AaaSwitchAccessPrivMaskTable_Object = MibTable
aaaSwitchAccessPrivMaskTable = _AaaSwitchAccessPrivMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessPrivMaskTable.setStatus("current")
_AaaSwitchAccessPrivMaskEntry_Object = MibTableRow
aaaSwitchAccessPrivMaskEntry = _AaaSwitchAccessPrivMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1)
)
aaaSwitchAccessPrivMaskEntry.setIndexNames(
    (0, "ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessType"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessPrivMaskEntry.setStatus("current")


class _AaaSwitchAccessType_Type(Integer32):
    """Custom type aaaSwitchAccessType based on Integer32"""
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
        *(("console", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("http", 4),
          ("https", 5))
    )


_AaaSwitchAccessType_Type.__name__ = "Integer32"
_AaaSwitchAccessType_Object = MibTableColumn
aaaSwitchAccessType = _AaaSwitchAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 1),
    _AaaSwitchAccessType_Type()
)
aaaSwitchAccessType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaSwitchAccessType.setStatus("current")


class _AaaSwitchAccessReadRight1_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight1_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight1_Object = MibTableColumn
aaaSwitchAccessReadRight1 = _AaaSwitchAccessReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 2),
    _AaaSwitchAccessReadRight1_Type()
)
aaaSwitchAccessReadRight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight1.setStatus("current")


class _AaaSwitchAccessReadRight2_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight2_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight2_Object = MibTableColumn
aaaSwitchAccessReadRight2 = _AaaSwitchAccessReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 3),
    _AaaSwitchAccessReadRight2_Type()
)
aaaSwitchAccessReadRight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight2.setStatus("current")


class _AaaSwitchAccessReadRight3_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight3_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight3_Object = MibTableColumn
aaaSwitchAccessReadRight3 = _AaaSwitchAccessReadRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 4),
    _AaaSwitchAccessReadRight3_Type()
)
aaaSwitchAccessReadRight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight3.setStatus("current")


class _AaaSwitchAccessReadRight4_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight4_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight4_Object = MibTableColumn
aaaSwitchAccessReadRight4 = _AaaSwitchAccessReadRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 5),
    _AaaSwitchAccessReadRight4_Type()
)
aaaSwitchAccessReadRight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight4.setStatus("current")


class _AaaSwitchAccessWriteRight1_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight1_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight1_Object = MibTableColumn
aaaSwitchAccessWriteRight1 = _AaaSwitchAccessWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 6),
    _AaaSwitchAccessWriteRight1_Type()
)
aaaSwitchAccessWriteRight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight1.setStatus("current")


class _AaaSwitchAccessWriteRight2_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight2_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight2_Object = MibTableColumn
aaaSwitchAccessWriteRight2 = _AaaSwitchAccessWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 7),
    _AaaSwitchAccessWriteRight2_Type()
)
aaaSwitchAccessWriteRight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight2.setStatus("current")


class _AaaSwitchAccessWriteRight3_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight3_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight3_Object = MibTableColumn
aaaSwitchAccessWriteRight3 = _AaaSwitchAccessWriteRight3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 8),
    _AaaSwitchAccessWriteRight3_Type()
)
aaaSwitchAccessWriteRight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight3.setStatus("current")


class _AaaSwitchAccessWriteRight4_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight4_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight4_Object = MibTableColumn
aaaSwitchAccessWriteRight4 = _AaaSwitchAccessWriteRight4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 7, 3, 1, 9),
    _AaaSwitchAccessWriteRight4_Type()
)
aaaSwitchAccessWriteRight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight4.setStatus("current")
_AlaAaaCommonCriteriaConfig_ObjectIdentity = ObjectIdentity
alaAaaCommonCriteriaConfig = _AlaAaaCommonCriteriaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 8)
)


class _AlaAaaCommonCriteriaMode_Type(Integer32):
    """Custom type alaAaaCommonCriteriaMode based on Integer32"""
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


_AlaAaaCommonCriteriaMode_Type.__name__ = "Integer32"
_AlaAaaCommonCriteriaMode_Object = MibScalar
alaAaaCommonCriteriaMode = _AlaAaaCommonCriteriaMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 8, 1),
    _AlaAaaCommonCriteriaMode_Type()
)
alaAaaCommonCriteriaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaCommonCriteriaMode.setStatus("current")
_AlaAaaTlsConfig_ObjectIdentity = ObjectIdentity
alaAaaTlsConfig = _AlaAaaTlsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9)
)
_AlaAaaTlsBaseConfig_ObjectIdentity = ObjectIdentity
alaAaaTlsBaseConfig = _AlaAaaTlsBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 1)
)


class _AlaAaaTlsCaFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCaFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCaFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCaFileName_Object = MibScalar
alaAaaTlsCaFileName = _AlaAaaTlsCaFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 1, 1),
    _AlaAaaTlsCaFileName_Type()
)
alaAaaTlsCaFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCaFileName.setStatus("current")


class _AlaAaaTlsCrlFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCrlFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCrlFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCrlFileName_Object = MibScalar
alaAaaTlsCrlFileName = _AlaAaaTlsCrlFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 1, 2),
    _AlaAaaTlsCrlFileName_Type()
)
alaAaaTlsCrlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCrlFileName.setStatus("current")


class _AlaAaaTlsKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsKeyFileName_Object = MibScalar
alaAaaTlsKeyFileName = _AlaAaaTlsKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 1, 3),
    _AlaAaaTlsKeyFileName_Type()
)
alaAaaTlsKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsKeyFileName.setStatus("current")
_AlaAaaTlsSelfSignedCert_ObjectIdentity = ObjectIdentity
alaAaaTlsSelfSignedCert = _AlaAaaTlsSelfSignedCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2)
)


class _AlaAaaTlsSelfSignedCertFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsSelfSignedCertFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertFileName_Object = MibScalar
alaAaaTlsSelfSignedCertFileName = _AlaAaaTlsSelfSignedCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 1),
    _AlaAaaTlsSelfSignedCertFileName_Type()
)
alaAaaTlsSelfSignedCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertFileName.setStatus("current")


class _AlaAaaTlsSelfSignedCertKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsSelfSignedCertKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertKeyFileName_Object = MibScalar
alaAaaTlsSelfSignedCertKeyFileName = _AlaAaaTlsSelfSignedCertKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 2),
    _AlaAaaTlsSelfSignedCertKeyFileName_Type()
)
alaAaaTlsSelfSignedCertKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertKeyFileName.setStatus("current")


class _AlaAaaTlsSelfSignedCertValidPeriod_Type(Integer32):
    """Custom type alaAaaTlsSelfSignedCertValidPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3650),
    )


_AlaAaaTlsSelfSignedCertValidPeriod_Type.__name__ = "Integer32"
_AlaAaaTlsSelfSignedCertValidPeriod_Object = MibScalar
alaAaaTlsSelfSignedCertValidPeriod = _AlaAaaTlsSelfSignedCertValidPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 3),
    _AlaAaaTlsSelfSignedCertValidPeriod_Type()
)
alaAaaTlsSelfSignedCertValidPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertValidPeriod.setStatus("current")


class _AlaAaaTlsSelfSignedCertCommonName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertCommonName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertCommonName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertCommonName_Object = MibScalar
alaAaaTlsSelfSignedCertCommonName = _AlaAaaTlsSelfSignedCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 4),
    _AlaAaaTlsSelfSignedCertCommonName_Type()
)
alaAaaTlsSelfSignedCertCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertCommonName.setStatus("current")


class _AlaAaaTlsSelfSignedCertOrgName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertOrgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertOrgName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertOrgName_Object = MibScalar
alaAaaTlsSelfSignedCertOrgName = _AlaAaaTlsSelfSignedCertOrgName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 5),
    _AlaAaaTlsSelfSignedCertOrgName_Type()
)
alaAaaTlsSelfSignedCertOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertOrgName.setStatus("current")


class _AlaAaaTlsSelfSignedCertOrgUnit_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertOrgUnit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertOrgUnit_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertOrgUnit_Object = MibScalar
alaAaaTlsSelfSignedCertOrgUnit = _AlaAaaTlsSelfSignedCertOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 6),
    _AlaAaaTlsSelfSignedCertOrgUnit_Type()
)
alaAaaTlsSelfSignedCertOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertOrgUnit.setStatus("current")


class _AlaAaaTlsSelfSignedCertLocality_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertLocality based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertLocality_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertLocality_Object = MibScalar
alaAaaTlsSelfSignedCertLocality = _AlaAaaTlsSelfSignedCertLocality_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 7),
    _AlaAaaTlsSelfSignedCertLocality_Type()
)
alaAaaTlsSelfSignedCertLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertLocality.setStatus("current")


class _AlaAaaTlsSelfSignedCertState_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertState_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertState_Object = MibScalar
alaAaaTlsSelfSignedCertState = _AlaAaaTlsSelfSignedCertState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 8),
    _AlaAaaTlsSelfSignedCertState_Type()
)
alaAaaTlsSelfSignedCertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertState.setStatus("current")


class _AlaAaaTlsSelfSignedCertCountry_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertCountry based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaAaaTlsSelfSignedCertCountry_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertCountry_Object = MibScalar
alaAaaTlsSelfSignedCertCountry = _AlaAaaTlsSelfSignedCertCountry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 9),
    _AlaAaaTlsSelfSignedCertCountry_Type()
)
alaAaaTlsSelfSignedCertCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertCountry.setStatus("current")


class _AlaAaaTlsSelfSignedCertAction_Type(Integer32):
    """Custom type alaAaaTlsSelfSignedCertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_AlaAaaTlsSelfSignedCertAction_Type.__name__ = "Integer32"
_AlaAaaTlsSelfSignedCertAction_Object = MibScalar
alaAaaTlsSelfSignedCertAction = _AlaAaaTlsSelfSignedCertAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 2, 10),
    _AlaAaaTlsSelfSignedCertAction_Type()
)
alaAaaTlsSelfSignedCertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertAction.setStatus("current")
_AlaAaaTlsCsr_ObjectIdentity = ObjectIdentity
alaAaaTlsCsr = _AlaAaaTlsCsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3)
)


class _AlaAaaTlsCsrFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCsrFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrFileName_Object = MibScalar
alaAaaTlsCsrFileName = _AlaAaaTlsCsrFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 1),
    _AlaAaaTlsCsrFileName_Type()
)
alaAaaTlsCsrFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrFileName.setStatus("current")


class _AlaAaaTlsCsrKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCsrKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrKeyFileName_Object = MibScalar
alaAaaTlsCsrKeyFileName = _AlaAaaTlsCsrKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 2),
    _AlaAaaTlsCsrKeyFileName_Type()
)
alaAaaTlsCsrKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrKeyFileName.setStatus("current")


class _AlaAaaTlsCsrCommonName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrCommonName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrCommonName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrCommonName_Object = MibScalar
alaAaaTlsCsrCommonName = _AlaAaaTlsCsrCommonName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 3),
    _AlaAaaTlsCsrCommonName_Type()
)
alaAaaTlsCsrCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrCommonName.setStatus("current")


class _AlaAaaTlsCsrOrgName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrOrgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrOrgName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrOrgName_Object = MibScalar
alaAaaTlsCsrOrgName = _AlaAaaTlsCsrOrgName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 4),
    _AlaAaaTlsCsrOrgName_Type()
)
alaAaaTlsCsrOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrOrgName.setStatus("current")


class _AlaAaaTlsCsrOrgUnit_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrOrgUnit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrOrgUnit_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrOrgUnit_Object = MibScalar
alaAaaTlsCsrOrgUnit = _AlaAaaTlsCsrOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 5),
    _AlaAaaTlsCsrOrgUnit_Type()
)
alaAaaTlsCsrOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrOrgUnit.setStatus("current")


class _AlaAaaTlsCsrLocality_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrLocality based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrLocality_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrLocality_Object = MibScalar
alaAaaTlsCsrLocality = _AlaAaaTlsCsrLocality_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 6),
    _AlaAaaTlsCsrLocality_Type()
)
alaAaaTlsCsrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrLocality.setStatus("current")


class _AlaAaaTlsCsrState_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrState_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrState_Object = MibScalar
alaAaaTlsCsrState = _AlaAaaTlsCsrState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 7),
    _AlaAaaTlsCsrState_Type()
)
alaAaaTlsCsrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrState.setStatus("current")


class _AlaAaaTlsCsrCountry_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrCountry based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaAaaTlsCsrCountry_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrCountry_Object = MibScalar
alaAaaTlsCsrCountry = _AlaAaaTlsCsrCountry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 3, 8),
    _AlaAaaTlsCsrCountry_Type()
)
alaAaaTlsCsrCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrCountry.setStatus("current")
_AlaAaaTlsValidate_ObjectIdentity = ObjectIdentity
alaAaaTlsValidate = _AlaAaaTlsValidate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 4)
)


class _AlaAaaTlsValidateCa_Type(SnmpAdminString):
    """Custom type alaAaaTlsValidateCa based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaAaaTlsValidateCa_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsValidateCa_Object = MibScalar
alaAaaTlsValidateCa = _AlaAaaTlsValidateCa_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 4, 1),
    _AlaAaaTlsValidateCa_Type()
)
alaAaaTlsValidateCa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsValidateCa.setStatus("current")


class _AlaAaaTlsValidateCert_Type(SnmpAdminString):
    """Custom type alaAaaTlsValidateCert based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaAaaTlsValidateCert_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsValidateCert_Object = MibScalar
alaAaaTlsValidateCert = _AlaAaaTlsValidateCert_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 1, 9, 4, 2),
    _AlaAaaTlsValidateCert_Type()
)
alaAaaTlsValidateCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsValidateCert.setStatus("current")
_AlcatelIND1AAAMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBConformance = _AlcatelIND1AAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBConformance.setStatus("current")
_AlcatelIND1AAAMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBGroups = _AlcatelIND1AAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBGroups.setStatus("current")
_AlcatelIND1AAAMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBCompliances = _AlcatelIND1AAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliances.setStatus("current")

# Managed Objects groups

aaaServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 1)
)
aaaServerMIBGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "aaasProtocol"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasHostName"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasHostName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasIpAddress2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRetries"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasTimout"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRadKey"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRadAuthPort"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRadAcctPort"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapPort"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapDn"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapPasswd"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapSearchBase"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapServType"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapEnableSsl"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasTacacsKey"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasTacacsPort"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasVrfName"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasRadKeyHash"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasLdapPasswdHash"),
        ("ALCATEL-ENT1-AAA-MIB", "aaasTacacsKeyHash"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaAccessMode"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaAccessIpLockoutThreshold"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaAccessManagementIpStatus"))
)
if mibBuilder.loadTexts:
    aaaServerMIBGroup.setStatus("current")

aaaAuthAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 2)
)
aaaAuthAcctGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "aaatsName1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaatsName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaatsName3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaatsName4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaatsRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaatsCertificate"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacsName1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacsName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacsName3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacsName4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacsRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacmdSrvName1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacmdSrvName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacmdSrvName3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacmdSrvName4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacmdRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaInterface"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaName1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaName3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaName4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaadaRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdName1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdName2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdName3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdName4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdSyslogIPAddrType"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdSyslogIPAddr"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdSyslogUdpPort"),
        ("ALCATEL-ENT1-AAA-MIB", "aaacdCallngStationId"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaOnexReAuthStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaOnexReAuthIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaOnexReAuthTrustRadStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaOnexIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaOnexIntmIntvlTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacIntmIntvlTrstRadStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacSessTimeoutStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacSessTimeoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacSesTimeoutTrstRadStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacInActLogoutStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaMacInActLogoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpSessTimeoutStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpSessTimeoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpSessTmotTrstRadStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpIntmIntvlTrstRadStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpInActLogoutStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCpInActLogoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTacacsServerCmdAuthorization"))
)
if mibBuilder.loadTexts:
    aaaAuthAcctGroup.setStatus("current")

aaaUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 3)
)
aaaUserMIBGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "aaauPassword"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauReadRight1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauReadRight2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauWriteRight1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauWriteRight2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauSnmpLevel"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauSnmpAuthKey"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauOldPassword"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauPasswordExpirationDate"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauPasswordExpirationInMinute"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauPasswordAllowModifyDate"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauPasswordLockoutEnable"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauBadAtempts"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauReadRight3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauReadRight4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauWriteRight3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauWriteRight4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordSizeMin"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaDefaultPasswordExpirationInDays"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordContainUserName"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordMinUpperCase"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordMinLowerCase"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordMinDigit"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordMinNonAlphan"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordHistory"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaPasswordMinAge"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaLockoutWindow"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaLockoutDuration"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaLockoutThreshold"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAsaAccessPolicyAdminConsoleOnly"),
        ("ALCATEL-ENT1-AAA-MIB", "aaauSnmpPrivPassword"))
)
if mibBuilder.loadTexts:
    aaaUserMIBGroup.setStatus("current")

alaAaaClientAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 4)
)
alaAaaClientAttrGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaRadNasPortId"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadNasIdentifier"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadUserNameDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadPasswordDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadCallnStnIdDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadCalldStnIdDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadUserNameCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadPasswordCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadCallingStationIdCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaRadCalledStationIdCase"))
)
if mibBuilder.loadTexts:
    alaAaaClientAttrGroup.setStatus("current")

alaAaaProfileObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 5)
)
alaAaaProfileObjectsGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaProfOnexReAuthSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfOnexReAuthIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfOnexReAuthTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfOnexIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfOnexIntmItvlTstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacIntmItvlTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacSessTimeoutSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacSessTimeoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacSessTmoutTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacInActLogoutSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfMacInActLogoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpSessTimeoutSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpSessTimeoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpSessTmotTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpInActLogoutSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpInActLogoutIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpIntrmIntrvl"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfCpItrmIntlTrstRadSts"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadNasPortId"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadNasIdentifier"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadUserNameDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadPasswrdDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadCallnStnIdDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadCalldStnIdDelim"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadUserNameCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadPasswordCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadCallnStnIdCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRadCalldStnIdCase"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthSrvName1"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthSrvName2"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthSrvName3"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthSrvName4"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAuthRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSrvName1"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSrvName2"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSrvName3"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSrvName4"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSyslogIPAddrType"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSyslogIPAddr"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctSyslogUdpPort"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctCalingStationId"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfAcctRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaUserProfileSave"))
)
if mibBuilder.loadTexts:
    alaAaaProfileObjectsGroup.setStatus("current")

aaaSwitchAccessMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 6)
)
aaaSwitchAccessMIBGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessMgmtStationRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessBannedIpRowStatus"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessReadRight1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessReadRight2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessReadRight3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessReadRight4"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessWriteRight1"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessWriteRight2"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessWriteRight3"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessWriteRight4"))
)
if mibBuilder.loadTexts:
    aaaSwitchAccessMIBGroup.setStatus("current")

alaAaaCommonCriteriaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 7)
)
alaAaaCommonCriteriaGroup.setObjects(
    ("ALCATEL-ENT1-AAA-MIB", "alaAaaCommonCriteriaMode")
)
if mibBuilder.loadTexts:
    alaAaaCommonCriteriaGroup.setStatus("current")

alaAaaTlsBaseConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 8)
)
alaAaaTlsBaseConfigGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCaFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCrlFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsKeyFileName"))
)
if mibBuilder.loadTexts:
    alaAaaTlsBaseConfigGroup.setStatus("current")

alaAaaTlsSelfSignedCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 9)
)
alaAaaTlsSelfSignedCertGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertKeyFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertValidPeriod"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertCommonName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertOrgName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertOrgUnit"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertLocality"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertState"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertCountry"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertAction"))
)
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertGroup.setStatus("current")

alaAaaTlsCsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 10)
)
alaAaaTlsCsrGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrKeyFileName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrCommonName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrOrgName"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrOrgUnit"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrLocality"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrState"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrCountry"))
)
if mibBuilder.loadTexts:
    alaAaaTlsCsrGroup.setStatus("current")

alaAaaTlsValidateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 1, 11)
)
alaAaaTlsValidateGroup.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsValidateCa"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsValidateCert"))
)
if mibBuilder.loadTexts:
    alaAaaTlsValidateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1AAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 15, 1, 2, 2, 1)
)
alcatelIND1AAAMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-AAA-MIB", "aaaServerMIBGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaAuthAcctGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaUserMIBGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaClientAttrGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaProfileObjectsGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "aaaSwitchAccessMIBGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaCommonCriteriaGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsBaseConfigGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsSelfSignedCertGroup"),
        ("ALCATEL-ENT1-AAA-MIB", "alaAaaTlsCsrGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-AAA-MIB",
    **{"alcatelIND1AAAMIB": alcatelIND1AAAMIB,
       "alcatelIND1AAAMIBObjects": alcatelIND1AAAMIBObjects,
       "aaaServerMIB": aaaServerMIB,
       "aaaServerTable": aaaServerTable,
       "aaaServerEntry": aaaServerEntry,
       "aaasName": aaasName,
       "aaasProtocol": aaasProtocol,
       "aaasHostName": aaasHostName,
       "aaasIpAddress": aaasIpAddress,
       "aaasHostName2": aaasHostName2,
       "aaasIpAddress2": aaasIpAddress2,
       "aaasRetries": aaasRetries,
       "aaasTimout": aaasTimout,
       "aaasRadKey": aaasRadKey,
       "aaasRadAuthPort": aaasRadAuthPort,
       "aaasRadAcctPort": aaasRadAcctPort,
       "aaasLdapPort": aaasLdapPort,
       "aaasLdapDn": aaasLdapDn,
       "aaasLdapPasswd": aaasLdapPasswd,
       "aaasLdapSearchBase": aaasLdapSearchBase,
       "aaasLdapServType": aaasLdapServType,
       "aaasLdapEnableSsl": aaasLdapEnableSsl,
       "aaasRowStatus": aaasRowStatus,
       "aaasTacacsKey": aaasTacacsKey,
       "aaasTacacsPort": aaasTacacsPort,
       "aaasVrfName": aaasVrfName,
       "aaasRadKeyHash": aaasRadKeyHash,
       "aaasLdapPasswdHash": aaasLdapPasswdHash,
       "aaasTacacsKeyHash": aaasTacacsKeyHash,
       "aaaAuthAcctMIB": aaaAuthAcctMIB,
       "aaaAuthSATable": aaaAuthSATable,
       "aaaAuthSAEntry": aaaAuthSAEntry,
       "aaatsInterface": aaatsInterface,
       "aaatsName1": aaatsName1,
       "aaatsName2": aaatsName2,
       "aaatsName3": aaatsName3,
       "aaatsName4": aaatsName4,
       "aaatsRowStatus": aaatsRowStatus,
       "aaatsCertificate": aaatsCertificate,
       "aaaAcctSATable": aaaAcctSATable,
       "aaaAcctSAEntry": aaaAcctSAEntry,
       "aaacsInterface": aaacsInterface,
       "aaacsName1": aaacsName1,
       "aaacsName2": aaacsName2,
       "aaacsName3": aaacsName3,
       "aaacsName4": aaacsName4,
       "aaacsRowStatus": aaacsRowStatus,
       "aaaAcctCmdTable": aaaAcctCmdTable,
       "aaaAcctCmdEntry": aaaAcctCmdEntry,
       "aaacmdInterface": aaacmdInterface,
       "aaacmdSrvName1": aaacmdSrvName1,
       "aaacmdSrvName2": aaacmdSrvName2,
       "aaacmdSrvName3": aaacmdSrvName3,
       "aaacmdSrvName4": aaacmdSrvName4,
       "aaacmdRowStatus": aaacmdRowStatus,
       "aaaAuthDATable": aaaAuthDATable,
       "aaaAuthDAEntry": aaaAuthDAEntry,
       "aaadaInterface": aaadaInterface,
       "aaadaName1": aaadaName1,
       "aaadaName2": aaadaName2,
       "aaadaName3": aaadaName3,
       "aaadaName4": aaadaName4,
       "aaadaRowStatus": aaadaRowStatus,
       "aaaAcctDATable": aaaAcctDATable,
       "aaaAcctDAEntry": aaaAcctDAEntry,
       "aaacdInterface": aaacdInterface,
       "aaacdName1": aaacdName1,
       "aaacdName2": aaacdName2,
       "aaacdName3": aaacdName3,
       "aaacdName4": aaacdName4,
       "aaacdRowStatus": aaacdRowStatus,
       "aaacdSyslogIPAddrType": aaacdSyslogIPAddrType,
       "aaacdSyslogIPAddr": aaacdSyslogIPAddr,
       "aaacdSyslogUdpPort": aaacdSyslogUdpPort,
       "aaacdCallngStationId": aaacdCallngStationId,
       "alaAaaAuthConfig": alaAaaAuthConfig,
       "alaAaaOnexReAuthStatus": alaAaaOnexReAuthStatus,
       "alaAaaOnexReAuthIntrvl": alaAaaOnexReAuthIntrvl,
       "alaAaaOnexReAuthTrustRadStatus": alaAaaOnexReAuthTrustRadStatus,
       "alaAaaOnexIntrmIntrvl": alaAaaOnexIntrmIntrvl,
       "alaAaaOnexIntmIntvlTrstRadSts": alaAaaOnexIntmIntvlTrstRadSts,
       "alaAaaMacIntrmIntrvl": alaAaaMacIntrmIntrvl,
       "alaAaaMacIntmIntvlTrstRadStatus": alaAaaMacIntmIntvlTrstRadStatus,
       "alaAaaMacSessTimeoutStatus": alaAaaMacSessTimeoutStatus,
       "alaAaaMacSessTimeoutIntrvl": alaAaaMacSessTimeoutIntrvl,
       "alaAaaMacSesTimeoutTrstRadStatus": alaAaaMacSesTimeoutTrstRadStatus,
       "alaAaaMacInActLogoutStatus": alaAaaMacInActLogoutStatus,
       "alaAaaMacInActLogoutIntrvl": alaAaaMacInActLogoutIntrvl,
       "alaAaaCpIntrmIntrvl": alaAaaCpIntrmIntrvl,
       "alaAaaCpIntmIntvlTrstRadStatus": alaAaaCpIntmIntvlTrstRadStatus,
       "alaAaaCpSessTimeoutStatus": alaAaaCpSessTimeoutStatus,
       "alaAaaCpSessTimeoutIntrvl": alaAaaCpSessTimeoutIntrvl,
       "alaAaaCpSessTmotTrstRadStatus": alaAaaCpSessTmotTrstRadStatus,
       "alaAaaCpInActLogoutStatus": alaAaaCpInActLogoutStatus,
       "alaAaaCpInActLogoutIntrvl": alaAaaCpInActLogoutIntrvl,
       "alaAaaTacacsServerCmdAuthorization": alaAaaTacacsServerCmdAuthorization,
       "aaaUserMIB": aaaUserMIB,
       "aaaUserTable": aaaUserTable,
       "aaaUserEntry": aaaUserEntry,
       "aaauUserName": aaauUserName,
       "aaauPassword": aaauPassword,
       "aaauReadRight1": aaauReadRight1,
       "aaauReadRight2": aaauReadRight2,
       "aaauWriteRight1": aaauWriteRight1,
       "aaauWriteRight2": aaauWriteRight2,
       "aaauSnmpLevel": aaauSnmpLevel,
       "aaauSnmpAuthKey": aaauSnmpAuthKey,
       "aaauRowStatus": aaauRowStatus,
       "aaauOldPassword": aaauOldPassword,
       "aaauPasswordExpirationDate": aaauPasswordExpirationDate,
       "aaauPasswordExpirationInMinute": aaauPasswordExpirationInMinute,
       "aaauPasswordAllowModifyDate": aaauPasswordAllowModifyDate,
       "aaauPasswordLockoutEnable": aaauPasswordLockoutEnable,
       "aaauBadAtempts": aaauBadAtempts,
       "aaauReadRight3": aaauReadRight3,
       "aaauReadRight4": aaauReadRight4,
       "aaauWriteRight3": aaauWriteRight3,
       "aaauWriteRight4": aaauWriteRight4,
       "aaauSnmpPrivPassword": aaauSnmpPrivPassword,
       "aaaAsaConfig": aaaAsaConfig,
       "aaaAsaPasswordSizeMin": aaaAsaPasswordSizeMin,
       "aaaAsaDefaultPasswordExpirationInDays": aaaAsaDefaultPasswordExpirationInDays,
       "aaaAsaPasswordContainUserName": aaaAsaPasswordContainUserName,
       "aaaAsaPasswordMinUpperCase": aaaAsaPasswordMinUpperCase,
       "aaaAsaPasswordMinLowerCase": aaaAsaPasswordMinLowerCase,
       "aaaAsaPasswordMinDigit": aaaAsaPasswordMinDigit,
       "aaaAsaPasswordMinNonAlphan": aaaAsaPasswordMinNonAlphan,
       "aaaAsaPasswordHistory": aaaAsaPasswordHistory,
       "aaaAsaPasswordMinAge": aaaAsaPasswordMinAge,
       "aaaAsaLockoutWindow": aaaAsaLockoutWindow,
       "aaaAsaLockoutDuration": aaaAsaLockoutDuration,
       "aaaAsaLockoutThreshold": aaaAsaLockoutThreshold,
       "aaaAsaAccessPolicyAdminConsoleOnly": aaaAsaAccessPolicyAdminConsoleOnly,
       "aaaAsaAccessMode": aaaAsaAccessMode,
       "aaaAsaAccessIpLockoutThreshold": aaaAsaAccessIpLockoutThreshold,
       "aaaAsaAccessManagementIpStatus": aaaAsaAccessManagementIpStatus,
       "alaAaaClientAttr": alaAaaClientAttr,
       "alaAaaRadClientGlobalAttr": alaAaaRadClientGlobalAttr,
       "alaAaaRadNasPortId": alaAaaRadNasPortId,
       "alaAaaRadNasIdentifier": alaAaaRadNasIdentifier,
       "alaAaaRadUserNameDelim": alaAaaRadUserNameDelim,
       "alaAaaRadPasswordDelim": alaAaaRadPasswordDelim,
       "alaAaaRadCallnStnIdDelim": alaAaaRadCallnStnIdDelim,
       "alaAaaRadCalldStnIdDelim": alaAaaRadCalldStnIdDelim,
       "alaAaaRadUserNameCase": alaAaaRadUserNameCase,
       "alaAaaRadPasswordCase": alaAaaRadPasswordCase,
       "alaAaaRadCallingStationIdCase": alaAaaRadCallingStationIdCase,
       "alaAaaRadCalledStationIdCase": alaAaaRadCalledStationIdCase,
       "alaAaaProfileObjects": alaAaaProfileObjects,
       "alaAaaProfileConfig": alaAaaProfileConfig,
       "alaAaaProfTable": alaAaaProfTable,
       "alaAaaProfEntry": alaAaaProfEntry,
       "alaAaaProfName": alaAaaProfName,
       "alaAaaProfOnexReAuthSts": alaAaaProfOnexReAuthSts,
       "alaAaaProfOnexReAuthIntrvl": alaAaaProfOnexReAuthIntrvl,
       "alaAaaProfOnexReAuthTrstRadSts": alaAaaProfOnexReAuthTrstRadSts,
       "alaAaaProfOnexIntrmIntrvl": alaAaaProfOnexIntrmIntrvl,
       "alaAaaProfOnexIntmItvlTstRadSts": alaAaaProfOnexIntmItvlTstRadSts,
       "alaAaaProfMacIntrmIntrvl": alaAaaProfMacIntrmIntrvl,
       "alaAaaProfMacIntmItvlTrstRadSts": alaAaaProfMacIntmItvlTrstRadSts,
       "alaAaaProfMacSessTimeoutSts": alaAaaProfMacSessTimeoutSts,
       "alaAaaProfMacSessTimeoutIntrvl": alaAaaProfMacSessTimeoutIntrvl,
       "alaAaaProfMacSessTmoutTrstRadSts": alaAaaProfMacSessTmoutTrstRadSts,
       "alaAaaProfMacInActLogoutSts": alaAaaProfMacInActLogoutSts,
       "alaAaaProfMacInActLogoutIntrvl": alaAaaProfMacInActLogoutIntrvl,
       "alaAaaProfCpSessTimeoutSts": alaAaaProfCpSessTimeoutSts,
       "alaAaaProfCpSessTimeoutIntrvl": alaAaaProfCpSessTimeoutIntrvl,
       "alaAaaProfCpSessTmotTrstRadSts": alaAaaProfCpSessTmotTrstRadSts,
       "alaAaaProfCpInActLogoutSts": alaAaaProfCpInActLogoutSts,
       "alaAaaProfCpInActLogoutIntrvl": alaAaaProfCpInActLogoutIntrvl,
       "alaAaaProfCpIntrmIntrvl": alaAaaProfCpIntrmIntrvl,
       "alaAaaProfCpItrmIntlTrstRadSts": alaAaaProfCpItrmIntlTrstRadSts,
       "alaAaaProfRadNasPortId": alaAaaProfRadNasPortId,
       "alaAaaProfRadNasIdentifier": alaAaaProfRadNasIdentifier,
       "alaAaaProfRadUserNameDelim": alaAaaProfRadUserNameDelim,
       "alaAaaProfRadPasswrdDelim": alaAaaProfRadPasswrdDelim,
       "alaAaaProfRadCallnStnIdDelim": alaAaaProfRadCallnStnIdDelim,
       "alaAaaProfRadCalldStnIdDelim": alaAaaProfRadCalldStnIdDelim,
       "alaAaaProfRadUserNameCase": alaAaaProfRadUserNameCase,
       "alaAaaProfRadPasswordCase": alaAaaProfRadPasswordCase,
       "alaAaaProfRadCallnStnIdCase": alaAaaProfRadCallnStnIdCase,
       "alaAaaProfRadCalldStnIdCase": alaAaaProfRadCalldStnIdCase,
       "alaAaaProfRowStatus": alaAaaProfRowStatus,
       "alaAaaProfAuthTable": alaAaaProfAuthTable,
       "alaAaaProfAuthEntry": alaAaaProfAuthEntry,
       "alaAaaProfAuthInterface": alaAaaProfAuthInterface,
       "alaAaaProfAuthSrvName1": alaAaaProfAuthSrvName1,
       "alaAaaProfAuthSrvName2": alaAaaProfAuthSrvName2,
       "alaAaaProfAuthSrvName3": alaAaaProfAuthSrvName3,
       "alaAaaProfAuthSrvName4": alaAaaProfAuthSrvName4,
       "alaAaaProfAuthRowStatus": alaAaaProfAuthRowStatus,
       "alaAaaProfAcctTable": alaAaaProfAcctTable,
       "alaAaaProfAcctEntry": alaAaaProfAcctEntry,
       "alaAaaProfAcctInterface": alaAaaProfAcctInterface,
       "alaAaaProfAcctSrvName1": alaAaaProfAcctSrvName1,
       "alaAaaProfAcctSrvName2": alaAaaProfAcctSrvName2,
       "alaAaaProfAcctSrvName3": alaAaaProfAcctSrvName3,
       "alaAaaProfAcctSrvName4": alaAaaProfAcctSrvName4,
       "alaAaaProfAcctSyslogIPAddrType": alaAaaProfAcctSyslogIPAddrType,
       "alaAaaProfAcctSyslogIPAddr": alaAaaProfAcctSyslogIPAddr,
       "alaAaaProfAcctSyslogUdpPort": alaAaaProfAcctSyslogUdpPort,
       "alaAaaProfAcctCalingStationId": alaAaaProfAcctCalingStationId,
       "alaAaaProfAcctRowStatus": alaAaaProfAcctRowStatus,
       "alaAaaUserProfileSave": alaAaaUserProfileSave,
       "aaaSwitchAccessConfig": aaaSwitchAccessConfig,
       "aaaSwitchAccessMgmtStationTable": aaaSwitchAccessMgmtStationTable,
       "aaaSwitchAccessMgmtStationEntry": aaaSwitchAccessMgmtStationEntry,
       "aaaSwitchAccessMgmtStationIpType": aaaSwitchAccessMgmtStationIpType,
       "aaaSwitchAccessMgmtStationIpAddress": aaaSwitchAccessMgmtStationIpAddress,
       "aaaSwitchAccessMgmtStationIpPrefixLength": aaaSwitchAccessMgmtStationIpPrefixLength,
       "aaaSwitchAccessMgmtStationRowStatus": aaaSwitchAccessMgmtStationRowStatus,
       "aaaSwitchAccessBannedIpTable": aaaSwitchAccessBannedIpTable,
       "aaaSwitchAccessBannedIpEntry": aaaSwitchAccessBannedIpEntry,
       "aaaSwitchAccessBannedIpType": aaaSwitchAccessBannedIpType,
       "aaaSwitchAccessBannedIpAddress": aaaSwitchAccessBannedIpAddress,
       "aaaSwitchAccessBannedIpRowStatus": aaaSwitchAccessBannedIpRowStatus,
       "aaaSwitchAccessPrivMaskTable": aaaSwitchAccessPrivMaskTable,
       "aaaSwitchAccessPrivMaskEntry": aaaSwitchAccessPrivMaskEntry,
       "aaaSwitchAccessType": aaaSwitchAccessType,
       "aaaSwitchAccessReadRight1": aaaSwitchAccessReadRight1,
       "aaaSwitchAccessReadRight2": aaaSwitchAccessReadRight2,
       "aaaSwitchAccessReadRight3": aaaSwitchAccessReadRight3,
       "aaaSwitchAccessReadRight4": aaaSwitchAccessReadRight4,
       "aaaSwitchAccessWriteRight1": aaaSwitchAccessWriteRight1,
       "aaaSwitchAccessWriteRight2": aaaSwitchAccessWriteRight2,
       "aaaSwitchAccessWriteRight3": aaaSwitchAccessWriteRight3,
       "aaaSwitchAccessWriteRight4": aaaSwitchAccessWriteRight4,
       "alaAaaCommonCriteriaConfig": alaAaaCommonCriteriaConfig,
       "alaAaaCommonCriteriaMode": alaAaaCommonCriteriaMode,
       "alaAaaTlsConfig": alaAaaTlsConfig,
       "alaAaaTlsBaseConfig": alaAaaTlsBaseConfig,
       "alaAaaTlsCaFileName": alaAaaTlsCaFileName,
       "alaAaaTlsCrlFileName": alaAaaTlsCrlFileName,
       "alaAaaTlsKeyFileName": alaAaaTlsKeyFileName,
       "alaAaaTlsSelfSignedCert": alaAaaTlsSelfSignedCert,
       "alaAaaTlsSelfSignedCertFileName": alaAaaTlsSelfSignedCertFileName,
       "alaAaaTlsSelfSignedCertKeyFileName": alaAaaTlsSelfSignedCertKeyFileName,
       "alaAaaTlsSelfSignedCertValidPeriod": alaAaaTlsSelfSignedCertValidPeriod,
       "alaAaaTlsSelfSignedCertCommonName": alaAaaTlsSelfSignedCertCommonName,
       "alaAaaTlsSelfSignedCertOrgName": alaAaaTlsSelfSignedCertOrgName,
       "alaAaaTlsSelfSignedCertOrgUnit": alaAaaTlsSelfSignedCertOrgUnit,
       "alaAaaTlsSelfSignedCertLocality": alaAaaTlsSelfSignedCertLocality,
       "alaAaaTlsSelfSignedCertState": alaAaaTlsSelfSignedCertState,
       "alaAaaTlsSelfSignedCertCountry": alaAaaTlsSelfSignedCertCountry,
       "alaAaaTlsSelfSignedCertAction": alaAaaTlsSelfSignedCertAction,
       "alaAaaTlsCsr": alaAaaTlsCsr,
       "alaAaaTlsCsrFileName": alaAaaTlsCsrFileName,
       "alaAaaTlsCsrKeyFileName": alaAaaTlsCsrKeyFileName,
       "alaAaaTlsCsrCommonName": alaAaaTlsCsrCommonName,
       "alaAaaTlsCsrOrgName": alaAaaTlsCsrOrgName,
       "alaAaaTlsCsrOrgUnit": alaAaaTlsCsrOrgUnit,
       "alaAaaTlsCsrLocality": alaAaaTlsCsrLocality,
       "alaAaaTlsCsrState": alaAaaTlsCsrState,
       "alaAaaTlsCsrCountry": alaAaaTlsCsrCountry,
       "alaAaaTlsValidate": alaAaaTlsValidate,
       "alaAaaTlsValidateCa": alaAaaTlsValidateCa,
       "alaAaaTlsValidateCert": alaAaaTlsValidateCert,
       "alcatelIND1AAAMIBConformance": alcatelIND1AAAMIBConformance,
       "alcatelIND1AAAMIBGroups": alcatelIND1AAAMIBGroups,
       "aaaServerMIBGroup": aaaServerMIBGroup,
       "aaaAuthAcctGroup": aaaAuthAcctGroup,
       "aaaUserMIBGroup": aaaUserMIBGroup,
       "alaAaaClientAttrGroup": alaAaaClientAttrGroup,
       "alaAaaProfileObjectsGroup": alaAaaProfileObjectsGroup,
       "aaaSwitchAccessMIBGroup": aaaSwitchAccessMIBGroup,
       "alaAaaCommonCriteriaGroup": alaAaaCommonCriteriaGroup,
       "alaAaaTlsBaseConfigGroup": alaAaaTlsBaseConfigGroup,
       "alaAaaTlsSelfSignedCertGroup": alaAaaTlsSelfSignedCertGroup,
       "alaAaaTlsCsrGroup": alaAaaTlsCsrGroup,
       "alaAaaTlsValidateGroup": alaAaaTlsValidateGroup,
       "alcatelIND1AAAMIBCompliances": alcatelIND1AAAMIBCompliances,
       "alcatelIND1AAAMIBCompliance": alcatelIND1AAAMIBCompliance}
)
