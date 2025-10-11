# SNMP MIB module (TPLINK-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-SSL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:29 2025
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


# MODULE-IDENTITY

tplinkSslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42)
)
if mibBuilder.loadTexts:
    tplinkSslMIB.setRevisions(
        ("2012-12-13 09:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSslMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSslMIBObjects = _TplinkSslMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1)
)


class _TpHttpsEnable_Type(Integer32):
    """Custom type tpHttpsEnable based on Integer32"""
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


_TpHttpsEnable_Type.__name__ = "Integer32"
_TpHttpsEnable_Object = MibScalar
tpHttpsEnable = _TpHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 1),
    _TpHttpsEnable_Type()
)
tpHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsEnable.setStatus("current")


class _TpSslProtocolVersion_Type(Integer32):
    """Custom type tpSslProtocolVersion based on Integer32"""
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
        *(("sslv3", 1),
          ("tlsv1", 2),
          ("tlsv11", 3),
          ("tlsv12", 4),
          ("all", 5))
    )


_TpSslProtocolVersion_Type.__name__ = "Integer32"
_TpSslProtocolVersion_Object = MibScalar
tpSslProtocolVersion = _TpSslProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 2),
    _TpSslProtocolVersion_Type()
)
tpSslProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSslProtocolVersion.setStatus("current")


class _TpRc4Md5_Type(Integer32):
    """Custom type tpRc4Md5 based on Integer32"""
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


_TpRc4Md5_Type.__name__ = "Integer32"
_TpRc4Md5_Object = MibScalar
tpRc4Md5 = _TpRc4Md5_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 3),
    _TpRc4Md5_Type()
)
tpRc4Md5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRc4Md5.setStatus("current")


class _TpRc4Sha_Type(Integer32):
    """Custom type tpRc4Sha based on Integer32"""
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


_TpRc4Sha_Type.__name__ = "Integer32"
_TpRc4Sha_Object = MibScalar
tpRc4Sha = _TpRc4Sha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 4),
    _TpRc4Sha_Type()
)
tpRc4Sha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRc4Sha.setStatus("current")


class _TpDesCbcSha_Type(Integer32):
    """Custom type tpDesCbcSha based on Integer32"""
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


_TpDesCbcSha_Type.__name__ = "Integer32"
_TpDesCbcSha_Object = MibScalar
tpDesCbcSha = _TpDesCbcSha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 5),
    _TpDesCbcSha_Type()
)
tpDesCbcSha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpDesCbcSha.setStatus("current")


class _Tp3DesEdeCbcSha_Type(Integer32):
    """Custom type tp3DesEdeCbcSha based on Integer32"""
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


_Tp3DesEdeCbcSha_Type.__name__ = "Integer32"
_Tp3DesEdeCbcSha_Object = MibScalar
tp3DesEdeCbcSha = _Tp3DesEdeCbcSha_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 6),
    _Tp3DesEdeCbcSha_Type()
)
tp3DesEdeCbcSha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp3DesEdeCbcSha.setStatus("current")


class _TpEcdheAes128GcmSha256_Type(Integer32):
    """Custom type tpEcdheAes128GcmSha256 based on Integer32"""
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


_TpEcdheAes128GcmSha256_Type.__name__ = "Integer32"
_TpEcdheAes128GcmSha256_Object = MibScalar
tpEcdheAes128GcmSha256 = _TpEcdheAes128GcmSha256_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 7),
    _TpEcdheAes128GcmSha256_Type()
)
tpEcdheAes128GcmSha256.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpEcdheAes128GcmSha256.setStatus("current")


class _TpEcdheAes256GcmSha384_Type(Integer32):
    """Custom type tpEcdheAes256GcmSha384 based on Integer32"""
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


_TpEcdheAes256GcmSha384_Type.__name__ = "Integer32"
_TpEcdheAes256GcmSha384_Object = MibScalar
tpEcdheAes256GcmSha384 = _TpEcdheAes256GcmSha384_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 8),
    _TpEcdheAes256GcmSha384_Type()
)
tpEcdheAes256GcmSha384.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpEcdheAes256GcmSha384.setStatus("current")


class _TpHttpsSessionTimeOut_Type(Integer32):
    """Custom type tpHttpsSessionTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_TpHttpsSessionTimeOut_Type.__name__ = "Integer32"
_TpHttpsSessionTimeOut_Object = MibScalar
tpHttpsSessionTimeOut = _TpHttpsSessionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 9),
    _TpHttpsSessionTimeOut_Type()
)
tpHttpsSessionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsSessionTimeOut.setStatus("current")


class _TpHttpsUserLimitEnable_Type(Integer32):
    """Custom type tpHttpsUserLimitEnable based on Integer32"""
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


_TpHttpsUserLimitEnable_Type.__name__ = "Integer32"
_TpHttpsUserLimitEnable_Object = MibScalar
tpHttpsUserLimitEnable = _TpHttpsUserLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 10),
    _TpHttpsUserLimitEnable_Type()
)
tpHttpsUserLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitEnable.setStatus("current")
_TpHttpsUserLimitMaxAdminNum_Type = Integer32
_TpHttpsUserLimitMaxAdminNum_Object = MibScalar
tpHttpsUserLimitMaxAdminNum = _TpHttpsUserLimitMaxAdminNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 11),
    _TpHttpsUserLimitMaxAdminNum_Type()
)
tpHttpsUserLimitMaxAdminNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxAdminNum.setStatus("current")
_TpHttpsUserLimitMaxOperatorNum_Type = Integer32
_TpHttpsUserLimitMaxOperatorNum_Object = MibScalar
tpHttpsUserLimitMaxOperatorNum = _TpHttpsUserLimitMaxOperatorNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 12),
    _TpHttpsUserLimitMaxOperatorNum_Type()
)
tpHttpsUserLimitMaxOperatorNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxOperatorNum.setStatus("current")
_TpHttpsUserLimitMaxPowerUserNum_Type = Integer32
_TpHttpsUserLimitMaxPowerUserNum_Object = MibScalar
tpHttpsUserLimitMaxPowerUserNum = _TpHttpsUserLimitMaxPowerUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 13),
    _TpHttpsUserLimitMaxPowerUserNum_Type()
)
tpHttpsUserLimitMaxPowerUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxPowerUserNum.setStatus("current")
_TpHttpsUserLimitMaxUserNum_Type = Integer32
_TpHttpsUserLimitMaxUserNum_Object = MibScalar
tpHttpsUserLimitMaxUserNum = _TpHttpsUserLimitMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 14),
    _TpHttpsUserLimitMaxUserNum_Type()
)
tpHttpsUserLimitMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsUserLimitMaxUserNum.setStatus("current")


class _TpHttpsPort_Type(Integer32):
    """Custom type tpHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TpHttpsPort_Type.__name__ = "Integer32"
_TpHttpsPort_Object = MibScalar
tpHttpsPort = _TpHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 1, 15),
    _TpHttpsPort_Type()
)
tpHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpHttpsPort.setStatus("current")
_TplinkSslNotifications_ObjectIdentity = ObjectIdentity
tplinkSslNotifications = _TplinkSslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 42, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SSL-MIB",
    **{"tplinkSslMIB": tplinkSslMIB,
       "tplinkSslMIBObjects": tplinkSslMIBObjects,
       "tpHttpsEnable": tpHttpsEnable,
       "tpSslProtocolVersion": tpSslProtocolVersion,
       "tpRc4Md5": tpRc4Md5,
       "tpRc4Sha": tpRc4Sha,
       "tpDesCbcSha": tpDesCbcSha,
       "tp3DesEdeCbcSha": tp3DesEdeCbcSha,
       "tpEcdheAes128GcmSha256": tpEcdheAes128GcmSha256,
       "tpEcdheAes256GcmSha384": tpEcdheAes256GcmSha384,
       "tpHttpsSessionTimeOut": tpHttpsSessionTimeOut,
       "tpHttpsUserLimitEnable": tpHttpsUserLimitEnable,
       "tpHttpsUserLimitMaxAdminNum": tpHttpsUserLimitMaxAdminNum,
       "tpHttpsUserLimitMaxOperatorNum": tpHttpsUserLimitMaxOperatorNum,
       "tpHttpsUserLimitMaxPowerUserNum": tpHttpsUserLimitMaxPowerUserNum,
       "tpHttpsUserLimitMaxUserNum": tpHttpsUserLimitMaxUserNum,
       "tpHttpsPort": tpHttpsPort,
       "tplinkSslNotifications": tplinkSslNotifications}
)
