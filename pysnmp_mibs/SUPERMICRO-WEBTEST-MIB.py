# SNMP MIB module (SUPERMICRO-WEBTEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-WEBTEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:08 2025
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsWebTstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66)
)
if mibBuilder.loadTexts:
    fsWebTstMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FutureHttpTstTable_ObjectIdentity = ObjectIdentity
futureHttpTstTable = _FutureHttpTstTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1)
)
_FsHttpAuthTestTable_Object = MibTable
fsHttpAuthTestTable = _FsHttpAuthTestTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1)
)
if mibBuilder.loadTexts:
    fsHttpAuthTestTable.setStatus("current")
_FsHttpAuthTestEntry_Object = MibTableRow
fsHttpAuthTestEntry = _FsHttpAuthTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1)
)
fsHttpAuthTestEntry.setIndexNames(
    (0, "SUPERMICRO-WEBTEST-MIB", "fsHttpSessionId"),
)
if mibBuilder.loadTexts:
    fsHttpAuthTestEntry.setStatus("current")
_FsHttpSessionId_Type = Integer32
_FsHttpSessionId_Object = MibTableColumn
fsHttpSessionId = _FsHttpSessionId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 1),
    _FsHttpSessionId_Type()
)
fsHttpSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsHttpSessionId.setStatus("current")


class _FsHttpWWWAuthHeader_Type(DisplayString):
    """Custom type fsHttpWWWAuthHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthHeader_Type.__name__ = "DisplayString"
_FsHttpWWWAuthHeader_Object = MibTableColumn
fsHttpWWWAuthHeader = _FsHttpWWWAuthHeader_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 2),
    _FsHttpWWWAuthHeader_Type()
)
fsHttpWWWAuthHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthHeader.setStatus("current")


class _FsHttpAuthorizeHeader_Type(DisplayString):
    """Custom type fsHttpAuthorizeHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthorizeHeader_Type.__name__ = "DisplayString"
_FsHttpAuthorizeHeader_Object = MibTableColumn
fsHttpAuthorizeHeader = _FsHttpAuthorizeHeader_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 3),
    _FsHttpAuthorizeHeader_Type()
)
fsHttpAuthorizeHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthorizeHeader.setStatus("current")


class _FsHttpAuthInfoHeader_Type(DisplayString):
    """Custom type fsHttpAuthInfoHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthInfoHeader_Type.__name__ = "DisplayString"
_FsHttpAuthInfoHeader_Object = MibTableColumn
fsHttpAuthInfoHeader = _FsHttpAuthInfoHeader_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 4),
    _FsHttpAuthInfoHeader_Type()
)
fsHttpAuthInfoHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthInfoHeader.setStatus("current")


class _FsHttpWWWAuthScheme_Type(DisplayString):
    """Custom type fsHttpWWWAuthScheme based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthScheme_Type.__name__ = "DisplayString"
_FsHttpWWWAuthScheme_Object = MibTableColumn
fsHttpWWWAuthScheme = _FsHttpWWWAuthScheme_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 5),
    _FsHttpWWWAuthScheme_Type()
)
fsHttpWWWAuthScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthScheme.setStatus("current")


class _FsHttpWWWAuthRealm_Type(DisplayString):
    """Custom type fsHttpWWWAuthRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthRealm_Type.__name__ = "DisplayString"
_FsHttpWWWAuthRealm_Object = MibTableColumn
fsHttpWWWAuthRealm = _FsHttpWWWAuthRealm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 6),
    _FsHttpWWWAuthRealm_Type()
)
fsHttpWWWAuthRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthRealm.setStatus("current")


class _FsHttpWWWAuthUsername_Type(DisplayString):
    """Custom type fsHttpWWWAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthUsername_Type.__name__ = "DisplayString"
_FsHttpWWWAuthUsername_Object = MibTableColumn
fsHttpWWWAuthUsername = _FsHttpWWWAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 7),
    _FsHttpWWWAuthUsername_Type()
)
fsHttpWWWAuthUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthUsername.setStatus("current")


class _FsHttpWWWAuthNonce_Type(DisplayString):
    """Custom type fsHttpWWWAuthNonce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthNonce_Type.__name__ = "DisplayString"
_FsHttpWWWAuthNonce_Object = MibTableColumn
fsHttpWWWAuthNonce = _FsHttpWWWAuthNonce_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 8),
    _FsHttpWWWAuthNonce_Type()
)
fsHttpWWWAuthNonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthNonce.setStatus("current")


class _FsHttpWWWAuthQop_Type(DisplayString):
    """Custom type fsHttpWWWAuthQop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthQop_Type.__name__ = "DisplayString"
_FsHttpWWWAuthQop_Object = MibTableColumn
fsHttpWWWAuthQop = _FsHttpWWWAuthQop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 9),
    _FsHttpWWWAuthQop_Type()
)
fsHttpWWWAuthQop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthQop.setStatus("current")


class _FsHttpWWWAuthAlgorithm_Type(DisplayString):
    """Custom type fsHttpWWWAuthAlgorithm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthAlgorithm_Type.__name__ = "DisplayString"
_FsHttpWWWAuthAlgorithm_Object = MibTableColumn
fsHttpWWWAuthAlgorithm = _FsHttpWWWAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 10),
    _FsHttpWWWAuthAlgorithm_Type()
)
fsHttpWWWAuthAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthAlgorithm.setStatus("current")


class _FsHttpWWWAuthStale_Type(DisplayString):
    """Custom type fsHttpWWWAuthStale based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpWWWAuthStale_Type.__name__ = "DisplayString"
_FsHttpWWWAuthStale_Object = MibTableColumn
fsHttpWWWAuthStale = _FsHttpWWWAuthStale_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 11),
    _FsHttpWWWAuthStale_Type()
)
fsHttpWWWAuthStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpWWWAuthStale.setStatus("current")


class _FsHttpAuthInfoQop_Type(DisplayString):
    """Custom type fsHttpAuthInfoQop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthInfoQop_Type.__name__ = "DisplayString"
_FsHttpAuthInfoQop_Object = MibTableColumn
fsHttpAuthInfoQop = _FsHttpAuthInfoQop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 12),
    _FsHttpAuthInfoQop_Type()
)
fsHttpAuthInfoQop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthInfoQop.setStatus("current")


class _FsHttpAuthInfoRespAuth_Type(DisplayString):
    """Custom type fsHttpAuthInfoRespAuth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthInfoRespAuth_Type.__name__ = "DisplayString"
_FsHttpAuthInfoRespAuth_Object = MibTableColumn
fsHttpAuthInfoRespAuth = _FsHttpAuthInfoRespAuth_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 13),
    _FsHttpAuthInfoRespAuth_Type()
)
fsHttpAuthInfoRespAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthInfoRespAuth.setStatus("current")


class _FsHttpAuthInfoCnonce_Type(DisplayString):
    """Custom type fsHttpAuthInfoCnonce based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthInfoCnonce_Type.__name__ = "DisplayString"
_FsHttpAuthInfoCnonce_Object = MibTableColumn
fsHttpAuthInfoCnonce = _FsHttpAuthInfoCnonce_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 14),
    _FsHttpAuthInfoCnonce_Type()
)
fsHttpAuthInfoCnonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthInfoCnonce.setStatus("current")


class _FsHttpAuthInfoNonceCount_Type(DisplayString):
    """Custom type fsHttpAuthInfoNonceCount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_FsHttpAuthInfoNonceCount_Type.__name__ = "DisplayString"
_FsHttpAuthInfoNonceCount_Object = MibTableColumn
fsHttpAuthInfoNonceCount = _FsHttpAuthInfoNonceCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 66, 1, 1, 1, 15),
    _FsHttpAuthInfoNonceCount_Type()
)
fsHttpAuthInfoNonceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsHttpAuthInfoNonceCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-WEBTEST-MIB",
    **{"fsWebTstMIB": fsWebTstMIB,
       "futureHttpTstTable": futureHttpTstTable,
       "fsHttpAuthTestTable": fsHttpAuthTestTable,
       "fsHttpAuthTestEntry": fsHttpAuthTestEntry,
       "fsHttpSessionId": fsHttpSessionId,
       "fsHttpWWWAuthHeader": fsHttpWWWAuthHeader,
       "fsHttpAuthorizeHeader": fsHttpAuthorizeHeader,
       "fsHttpAuthInfoHeader": fsHttpAuthInfoHeader,
       "fsHttpWWWAuthScheme": fsHttpWWWAuthScheme,
       "fsHttpWWWAuthRealm": fsHttpWWWAuthRealm,
       "fsHttpWWWAuthUsername": fsHttpWWWAuthUsername,
       "fsHttpWWWAuthNonce": fsHttpWWWAuthNonce,
       "fsHttpWWWAuthQop": fsHttpWWWAuthQop,
       "fsHttpWWWAuthAlgorithm": fsHttpWWWAuthAlgorithm,
       "fsHttpWWWAuthStale": fsHttpWWWAuthStale,
       "fsHttpAuthInfoQop": fsHttpAuthInfoQop,
       "fsHttpAuthInfoRespAuth": fsHttpAuthInfoRespAuth,
       "fsHttpAuthInfoCnonce": fsHttpAuthInfoCnonce,
       "fsHttpAuthInfoNonceCount": fsHttpAuthInfoNonceCount}
)
