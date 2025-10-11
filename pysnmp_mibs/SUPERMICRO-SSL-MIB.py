# SNMP MIB module (SUPERMICRO-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-SSL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:57 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ssl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96)
)
if mibBuilder.loadTexts:
    ssl.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SslGeneralGroup_ObjectIdentity = ObjectIdentity
sslGeneralGroup = _SslGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1)
)


class _SslSecureHttpStatus_Type(Integer32):
    """Custom type sslSecureHttpStatus based on Integer32"""
    defaultValue = 1

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


_SslSecureHttpStatus_Type.__name__ = "Integer32"
_SslSecureHttpStatus_Object = MibScalar
sslSecureHttpStatus = _SslSecureHttpStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 2),
    _SslSecureHttpStatus_Type()
)
sslSecureHttpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslSecureHttpStatus.setStatus("current")


class _SslPort_Type(Integer32):
    """Custom type sslPort based on Integer32"""
    defaultValue = 443

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SslPort_Type.__name__ = "Integer32"
_SslPort_Object = MibScalar
sslPort = _SslPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 3),
    _SslPort_Type()
)
sslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPort.setStatus("current")
_SslTrace_Type = Integer32
_SslTrace_Object = MibScalar
sslTrace = _SslTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 4),
    _SslTrace_Type()
)
sslTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslTrace.setStatus("current")


class _SslVersion_Type(Integer32):
    """Custom type sslVersion based on Integer32"""
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
        *(("all", 1),
          ("ssl3", 2),
          ("tls1", 3))
    )


_SslVersion_Type.__name__ = "Integer32"
_SslVersion_Object = MibScalar
sslVersion = _SslVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 5),
    _SslVersion_Type()
)
sslVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslVersion.setStatus("current")


class _SslRestconfStatus_Type(Integer32):
    """Custom type sslRestconfStatus based on Integer32"""
    defaultValue = 1

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


_SslRestconfStatus_Type.__name__ = "Integer32"
_SslRestconfStatus_Object = MibScalar
sslRestconfStatus = _SslRestconfStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 1, 6),
    _SslRestconfStatus_Type()
)
sslRestconfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslRestconfStatus.setStatus("current")
_SslCiphers_ObjectIdentity = ObjectIdentity
sslCiphers = _SslCiphers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2)
)


class _SslCipherList_Type(Integer32):
    """Custom type sslCipherList based on Integer32"""
    defaultValue = 76


_SslCipherList_Type.__name__ = "Integer32"
_SslCipherList_Object = MibScalar
sslCipherList = _SslCipherList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2, 1),
    _SslCipherList_Type()
)
sslCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslCipherList.setStatus("current")


class _SslDefaultCipherList_Type(TruthValue):
    """Custom type sslDefaultCipherList based on TruthValue"""
    defaultValue = 2


_SslDefaultCipherList_Type.__name__ = "TruthValue"
_SslDefaultCipherList_Object = MibScalar
sslDefaultCipherList = _SslDefaultCipherList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 96, 2, 2),
    _SslDefaultCipherList_Type()
)
sslDefaultCipherList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslDefaultCipherList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-SSL-MIB",
    **{"ssl": ssl,
       "sslGeneralGroup": sslGeneralGroup,
       "sslSecureHttpStatus": sslSecureHttpStatus,
       "sslPort": sslPort,
       "sslTrace": sslTrace,
       "sslVersion": sslVersion,
       "sslRestconfStatus": sslRestconfStatus,
       "sslCiphers": sslCiphers,
       "sslCipherList": sslCipherList,
       "sslDefaultCipherList": sslDefaultCipherList}
)
