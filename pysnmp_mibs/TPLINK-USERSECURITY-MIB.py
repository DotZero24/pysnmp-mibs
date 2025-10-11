# SNMP MIB module (TPLINK-USERSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-USERSECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:55 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkUserSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41)
)
if mibBuilder.loadTexts:
    tplinkUserSecurity.setRevisions(
        ("1920-09-07 09:00",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkUserSecurityMIBObjects_ObjectIdentity = ObjectIdentity
tplinkUserSecurityMIBObjects = _TplinkUserSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1)
)
_UserSecurityUserAuth_ObjectIdentity = ObjectIdentity
userSecurityUserAuth = _UserSecurityUserAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1)
)


class _UserSecurityUserAuthType_Type(Integer32):
    """Custom type userSecurityUserAuthType based on Integer32"""
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
        *(("disable", 0),
          ("ip", 1),
          ("mac", 2),
          ("port", 3))
    )


_UserSecurityUserAuthType_Type.__name__ = "Integer32"
_UserSecurityUserAuthType_Object = MibScalar
userSecurityUserAuthType = _UserSecurityUserAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 1),
    _UserSecurityUserAuthType_Type()
)
userSecurityUserAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserAuthType.setStatus("current")
_UserSecurityUserAuthPort_ObjectIdentity = ObjectIdentity
userSecurityUserAuthPort = _UserSecurityUserAuthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2)
)


class _UserSecurityUserAuthPortEnable_Type(Integer32):
    """Custom type userSecurityUserAuthPortEnable based on Integer32"""
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


_UserSecurityUserAuthPortEnable_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortEnable_Object = MibScalar
userSecurityUserAuthPortEnable = _UserSecurityUserAuthPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 1),
    _UserSecurityUserAuthPortEnable_Type()
)
userSecurityUserAuthPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortEnable.setStatus("current")
_UserSecurityUserAuthPortTable_Object = MibTable
userSecurityUserAuthPortTable = _UserSecurityUserAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    userSecurityUserAuthPortTable.setStatus("current")
_UserSecurityUserAuthPortEntry_Object = MibTableRow
userSecurityUserAuthPortEntry = _UserSecurityUserAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1)
)
userSecurityUserAuthPortEntry.setIndexNames(
    (0, "TPLINK-USERSECURITY-MIB", "userSecurityUserAuthIndex"),
)
if mibBuilder.loadTexts:
    userSecurityUserAuthPortEntry.setStatus("current")
_UserSecurityUserAuthPortIndex_Type = Integer32
_UserSecurityUserAuthPortIndex_Object = MibTableColumn
userSecurityUserAuthPortIndex = _UserSecurityUserAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 1),
    _UserSecurityUserAuthPortIndex_Type()
)
userSecurityUserAuthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortIndex.setStatus("current")


class _UserSecurityUserAuthPortAccessSnmp_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessSnmp based on Integer32"""
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


_UserSecurityUserAuthPortAccessSnmp_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessSnmp_Object = MibTableColumn
userSecurityUserAuthPortAccessSnmp = _UserSecurityUserAuthPortAccessSnmp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 2),
    _UserSecurityUserAuthPortAccessSnmp_Type()
)
userSecurityUserAuthPortAccessSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessSnmp.setStatus("current")


class _UserSecurityUserAuthPortAccessTelnet_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessTelnet based on Integer32"""
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


_UserSecurityUserAuthPortAccessTelnet_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessTelnet_Object = MibTableColumn
userSecurityUserAuthPortAccessTelnet = _UserSecurityUserAuthPortAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 3),
    _UserSecurityUserAuthPortAccessTelnet_Type()
)
userSecurityUserAuthPortAccessTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessTelnet.setStatus("current")


class _UserSecurityUserAuthPortAccessSsh_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessSsh based on Integer32"""
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


_UserSecurityUserAuthPortAccessSsh_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessSsh_Object = MibTableColumn
userSecurityUserAuthPortAccessSsh = _UserSecurityUserAuthPortAccessSsh_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 4),
    _UserSecurityUserAuthPortAccessSsh_Type()
)
userSecurityUserAuthPortAccessSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessSsh.setStatus("current")


class _UserSecurityUserAuthPortAccessHttp_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessHttp based on Integer32"""
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


_UserSecurityUserAuthPortAccessHttp_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessHttp_Object = MibTableColumn
userSecurityUserAuthPortAccessHttp = _UserSecurityUserAuthPortAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 5),
    _UserSecurityUserAuthPortAccessHttp_Type()
)
userSecurityUserAuthPortAccessHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessHttp.setStatus("current")


class _UserSecurityUserAuthPortAccessHttps_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessHttps based on Integer32"""
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


_UserSecurityUserAuthPortAccessHttps_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessHttps_Object = MibTableColumn
userSecurityUserAuthPortAccessHttps = _UserSecurityUserAuthPortAccessHttps_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 6),
    _UserSecurityUserAuthPortAccessHttps_Type()
)
userSecurityUserAuthPortAccessHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessHttps.setStatus("current")


class _UserSecurityUserAuthPortAccessPing_Type(Integer32):
    """Custom type userSecurityUserAuthPortAccessPing based on Integer32"""
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


_UserSecurityUserAuthPortAccessPing_Type.__name__ = "Integer32"
_UserSecurityUserAuthPortAccessPing_Object = MibTableColumn
userSecurityUserAuthPortAccessPing = _UserSecurityUserAuthPortAccessPing_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 7),
    _UserSecurityUserAuthPortAccessPing_Type()
)
userSecurityUserAuthPortAccessPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortAccessPing.setStatus("current")


class _UserSecurityUserAuthPortConf_Type(OctetString):
    """Custom type userSecurityUserAuthPortConf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserSecurityUserAuthPortConf_Type.__name__ = "OctetString"
_UserSecurityUserAuthPortConf_Object = MibTableColumn
userSecurityUserAuthPortConf = _UserSecurityUserAuthPortConf_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 2, 2, 1, 8),
    _UserSecurityUserAuthPortConf_Type()
)
userSecurityUserAuthPortConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthPortConf.setStatus("current")
_UserSecurityUserAuthIp_ObjectIdentity = ObjectIdentity
userSecurityUserAuthIp = _UserSecurityUserAuthIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3)
)


class _UserSecurityUserAuthIpEnable_Type(Integer32):
    """Custom type userSecurityUserAuthIpEnable based on Integer32"""
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


_UserSecurityUserAuthIpEnable_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpEnable_Object = MibScalar
userSecurityUserAuthIpEnable = _UserSecurityUserAuthIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 1),
    _UserSecurityUserAuthIpEnable_Type()
)
userSecurityUserAuthIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpEnable.setStatus("current")
_UserSecurityUserAuthIpTable_Object = MibTable
userSecurityUserAuthIpTable = _UserSecurityUserAuthIpTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    userSecurityUserAuthIpTable.setStatus("current")
_UserSecurityUserAuthIpEntry_Object = MibTableRow
userSecurityUserAuthIpEntry = _UserSecurityUserAuthIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1)
)
userSecurityUserAuthIpEntry.setIndexNames(
    (0, "TPLINK-USERSECURITY-MIB", "userSecurityUserAuthIndex"),
)
if mibBuilder.loadTexts:
    userSecurityUserAuthIpEntry.setStatus("current")
_UserSecurityUserAuthIpIndex_Type = Integer32
_UserSecurityUserAuthIpIndex_Object = MibTableColumn
userSecurityUserAuthIpIndex = _UserSecurityUserAuthIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 1),
    _UserSecurityUserAuthIpIndex_Type()
)
userSecurityUserAuthIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpIndex.setStatus("current")


class _UserSecurityUserAuthIpAccessSnmp_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessSnmp based on Integer32"""
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


_UserSecurityUserAuthIpAccessSnmp_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessSnmp_Object = MibTableColumn
userSecurityUserAuthIpAccessSnmp = _UserSecurityUserAuthIpAccessSnmp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 2),
    _UserSecurityUserAuthIpAccessSnmp_Type()
)
userSecurityUserAuthIpAccessSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessSnmp.setStatus("current")


class _UserSecurityUserAuthIpAccessTelnet_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessTelnet based on Integer32"""
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


_UserSecurityUserAuthIpAccessTelnet_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessTelnet_Object = MibTableColumn
userSecurityUserAuthIpAccessTelnet = _UserSecurityUserAuthIpAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 3),
    _UserSecurityUserAuthIpAccessTelnet_Type()
)
userSecurityUserAuthIpAccessTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessTelnet.setStatus("current")


class _UserSecurityUserAuthIpAccessSsh_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessSsh based on Integer32"""
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


_UserSecurityUserAuthIpAccessSsh_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessSsh_Object = MibTableColumn
userSecurityUserAuthIpAccessSsh = _UserSecurityUserAuthIpAccessSsh_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 4),
    _UserSecurityUserAuthIpAccessSsh_Type()
)
userSecurityUserAuthIpAccessSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessSsh.setStatus("current")


class _UserSecurityUserAuthIpAccessHttp_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessHttp based on Integer32"""
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


_UserSecurityUserAuthIpAccessHttp_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessHttp_Object = MibTableColumn
userSecurityUserAuthIpAccessHttp = _UserSecurityUserAuthIpAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 5),
    _UserSecurityUserAuthIpAccessHttp_Type()
)
userSecurityUserAuthIpAccessHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessHttp.setStatus("current")


class _UserSecurityUserAuthIpAccessHttps_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessHttps based on Integer32"""
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


_UserSecurityUserAuthIpAccessHttps_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessHttps_Object = MibTableColumn
userSecurityUserAuthIpAccessHttps = _UserSecurityUserAuthIpAccessHttps_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 6),
    _UserSecurityUserAuthIpAccessHttps_Type()
)
userSecurityUserAuthIpAccessHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessHttps.setStatus("current")


class _UserSecurityUserAuthIpAccessPing_Type(Integer32):
    """Custom type userSecurityUserAuthIpAccessPing based on Integer32"""
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


_UserSecurityUserAuthIpAccessPing_Type.__name__ = "Integer32"
_UserSecurityUserAuthIpAccessPing_Object = MibTableColumn
userSecurityUserAuthIpAccessPing = _UserSecurityUserAuthIpAccessPing_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 7),
    _UserSecurityUserAuthIpAccessPing_Type()
)
userSecurityUserAuthIpAccessPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAccessPing.setStatus("current")
_UserSecurityUserAuthIpAddress_Type = IpAddress
_UserSecurityUserAuthIpAddress_Object = MibTableColumn
userSecurityUserAuthIpAddress = _UserSecurityUserAuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 8),
    _UserSecurityUserAuthIpAddress_Type()
)
userSecurityUserAuthIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpAddress.setStatus("current")
_UserSecurityUserAuthIpMask_Type = IpAddress
_UserSecurityUserAuthIpMask_Object = MibTableColumn
userSecurityUserAuthIpMask = _UserSecurityUserAuthIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 3, 2, 1, 9),
    _UserSecurityUserAuthIpMask_Type()
)
userSecurityUserAuthIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthIpMask.setStatus("current")
_UserSecurityUserAuthMac_ObjectIdentity = ObjectIdentity
userSecurityUserAuthMac = _UserSecurityUserAuthMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4)
)


class _UserSecurityUserAuthMacEnable_Type(Integer32):
    """Custom type userSecurityUserAuthMacEnable based on Integer32"""
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


_UserSecurityUserAuthMacEnable_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacEnable_Object = MibScalar
userSecurityUserAuthMacEnable = _UserSecurityUserAuthMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 1),
    _UserSecurityUserAuthMacEnable_Type()
)
userSecurityUserAuthMacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacEnable.setStatus("current")
_UserSecurityUserAuthMacTable_Object = MibTable
userSecurityUserAuthMacTable = _UserSecurityUserAuthMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    userSecurityUserAuthMacTable.setStatus("current")
_UserSecurityUserAuthMacEntry_Object = MibTableRow
userSecurityUserAuthMacEntry = _UserSecurityUserAuthMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1)
)
userSecurityUserAuthMacEntry.setIndexNames(
    (0, "TPLINK-USERSECURITY-MIB", "userSecurityUserAuthIndex"),
)
if mibBuilder.loadTexts:
    userSecurityUserAuthMacEntry.setStatus("current")
_UserSecurityUserAuthMacIndex_Type = Integer32
_UserSecurityUserAuthMacIndex_Object = MibTableColumn
userSecurityUserAuthMacIndex = _UserSecurityUserAuthMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 1),
    _UserSecurityUserAuthMacIndex_Type()
)
userSecurityUserAuthMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacIndex.setStatus("current")


class _UserSecurityUserAuthMacAccessSnmp_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessSnmp based on Integer32"""
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


_UserSecurityUserAuthMacAccessSnmp_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessSnmp_Object = MibTableColumn
userSecurityUserAuthMacAccessSnmp = _UserSecurityUserAuthMacAccessSnmp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 2),
    _UserSecurityUserAuthMacAccessSnmp_Type()
)
userSecurityUserAuthMacAccessSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessSnmp.setStatus("current")


class _UserSecurityUserAuthMacAccessTelnet_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessTelnet based on Integer32"""
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


_UserSecurityUserAuthMacAccessTelnet_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessTelnet_Object = MibTableColumn
userSecurityUserAuthMacAccessTelnet = _UserSecurityUserAuthMacAccessTelnet_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 3),
    _UserSecurityUserAuthMacAccessTelnet_Type()
)
userSecurityUserAuthMacAccessTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessTelnet.setStatus("current")


class _UserSecurityUserAuthMacAccessSsh_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessSsh based on Integer32"""
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


_UserSecurityUserAuthMacAccessSsh_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessSsh_Object = MibTableColumn
userSecurityUserAuthMacAccessSsh = _UserSecurityUserAuthMacAccessSsh_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 4),
    _UserSecurityUserAuthMacAccessSsh_Type()
)
userSecurityUserAuthMacAccessSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessSsh.setStatus("current")


class _UserSecurityUserAuthMacAccessHttp_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessHttp based on Integer32"""
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


_UserSecurityUserAuthMacAccessHttp_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessHttp_Object = MibTableColumn
userSecurityUserAuthMacAccessHttp = _UserSecurityUserAuthMacAccessHttp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 5),
    _UserSecurityUserAuthMacAccessHttp_Type()
)
userSecurityUserAuthMacAccessHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessHttp.setStatus("current")


class _UserSecurityUserAuthMacAccessHttps_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessHttps based on Integer32"""
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


_UserSecurityUserAuthMacAccessHttps_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessHttps_Object = MibTableColumn
userSecurityUserAuthMacAccessHttps = _UserSecurityUserAuthMacAccessHttps_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 6),
    _UserSecurityUserAuthMacAccessHttps_Type()
)
userSecurityUserAuthMacAccessHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessHttps.setStatus("current")


class _UserSecurityUserAuthMacAccessPing_Type(Integer32):
    """Custom type userSecurityUserAuthMacAccessPing based on Integer32"""
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


_UserSecurityUserAuthMacAccessPing_Type.__name__ = "Integer32"
_UserSecurityUserAuthMacAccessPing_Object = MibTableColumn
userSecurityUserAuthMacAccessPing = _UserSecurityUserAuthMacAccessPing_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 7),
    _UserSecurityUserAuthMacAccessPing_Type()
)
userSecurityUserAuthMacAccessPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAccessPing.setStatus("current")


class _UserSecurityUserAuthMacAddress_Type(OctetString):
    """Custom type userSecurityUserAuthMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserSecurityUserAuthMacAddress_Type.__name__ = "OctetString"
_UserSecurityUserAuthMacAddress_Object = MibTableColumn
userSecurityUserAuthMacAddress = _UserSecurityUserAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 1, 1, 4, 2, 1, 8),
    _UserSecurityUserAuthMacAddress_Type()
)
userSecurityUserAuthMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSecurityUserAuthMacAddress.setStatus("current")
_TplinkUserSecurityMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkUserSecurityMIBNotifications = _TplinkUserSecurityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 41, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-USERSECURITY-MIB",
    **{"MacAddress": MacAddress,
       "tplinkUserSecurity": tplinkUserSecurity,
       "tplinkUserSecurityMIBObjects": tplinkUserSecurityMIBObjects,
       "userSecurityUserAuth": userSecurityUserAuth,
       "userSecurityUserAuthType": userSecurityUserAuthType,
       "userSecurityUserAuthPort": userSecurityUserAuthPort,
       "userSecurityUserAuthPortEnable": userSecurityUserAuthPortEnable,
       "userSecurityUserAuthPortTable": userSecurityUserAuthPortTable,
       "userSecurityUserAuthPortEntry": userSecurityUserAuthPortEntry,
       "userSecurityUserAuthPortIndex": userSecurityUserAuthPortIndex,
       "userSecurityUserAuthPortAccessSnmp": userSecurityUserAuthPortAccessSnmp,
       "userSecurityUserAuthPortAccessTelnet": userSecurityUserAuthPortAccessTelnet,
       "userSecurityUserAuthPortAccessSsh": userSecurityUserAuthPortAccessSsh,
       "userSecurityUserAuthPortAccessHttp": userSecurityUserAuthPortAccessHttp,
       "userSecurityUserAuthPortAccessHttps": userSecurityUserAuthPortAccessHttps,
       "userSecurityUserAuthPortAccessPing": userSecurityUserAuthPortAccessPing,
       "userSecurityUserAuthPortConf": userSecurityUserAuthPortConf,
       "userSecurityUserAuthIp": userSecurityUserAuthIp,
       "userSecurityUserAuthIpEnable": userSecurityUserAuthIpEnable,
       "userSecurityUserAuthIpTable": userSecurityUserAuthIpTable,
       "userSecurityUserAuthIpEntry": userSecurityUserAuthIpEntry,
       "userSecurityUserAuthIpIndex": userSecurityUserAuthIpIndex,
       "userSecurityUserAuthIpAccessSnmp": userSecurityUserAuthIpAccessSnmp,
       "userSecurityUserAuthIpAccessTelnet": userSecurityUserAuthIpAccessTelnet,
       "userSecurityUserAuthIpAccessSsh": userSecurityUserAuthIpAccessSsh,
       "userSecurityUserAuthIpAccessHttp": userSecurityUserAuthIpAccessHttp,
       "userSecurityUserAuthIpAccessHttps": userSecurityUserAuthIpAccessHttps,
       "userSecurityUserAuthIpAccessPing": userSecurityUserAuthIpAccessPing,
       "userSecurityUserAuthIpAddress": userSecurityUserAuthIpAddress,
       "userSecurityUserAuthIpMask": userSecurityUserAuthIpMask,
       "userSecurityUserAuthMac": userSecurityUserAuthMac,
       "userSecurityUserAuthMacEnable": userSecurityUserAuthMacEnable,
       "userSecurityUserAuthMacTable": userSecurityUserAuthMacTable,
       "userSecurityUserAuthMacEntry": userSecurityUserAuthMacEntry,
       "userSecurityUserAuthMacIndex": userSecurityUserAuthMacIndex,
       "userSecurityUserAuthMacAccessSnmp": userSecurityUserAuthMacAccessSnmp,
       "userSecurityUserAuthMacAccessTelnet": userSecurityUserAuthMacAccessTelnet,
       "userSecurityUserAuthMacAccessSsh": userSecurityUserAuthMacAccessSsh,
       "userSecurityUserAuthMacAccessHttp": userSecurityUserAuthMacAccessHttp,
       "userSecurityUserAuthMacAccessHttps": userSecurityUserAuthMacAccessHttps,
       "userSecurityUserAuthMacAccessPing": userSecurityUserAuthMacAccessPing,
       "userSecurityUserAuthMacAddress": userSecurityUserAuthMacAddress,
       "tplinkUserSecurityMIBNotifications": tplinkUserSecurityMIBNotifications}
)
