# SNMP MIB module (G6-PACC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-PACC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:13 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pacc_ObjectIdentity = ObjectIdentity
pacc = _Pacc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46)
)


class _PaccEnablePortAccessControl_Type(Integer32):
    """Custom type paccEnablePortAccessControl based on Integer32"""
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


_PaccEnablePortAccessControl_Type.__name__ = "Integer32"
_PaccEnablePortAccessControl_Object = MibScalar
paccEnablePortAccessControl = _PaccEnablePortAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 1),
    _PaccEnablePortAccessControl_Type()
)
paccEnablePortAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccEnablePortAccessControl.setStatus("current")
_PaccReauthenticationPeriod_Type = Unsigned32
_PaccReauthenticationPeriod_Object = MibScalar
paccReauthenticationPeriod = _PaccReauthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 2),
    _PaccReauthenticationPeriod_Type()
)
paccReauthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccReauthenticationPeriod.setStatus("current")
_PaccNasIdentifier_Type = DisplayString
_PaccNasIdentifier_Object = MibScalar
paccNasIdentifier = _PaccNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 3),
    _PaccNasIdentifier_Type()
)
paccNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccNasIdentifier.setStatus("current")
_PaccMacSeparatorChar_Type = DisplayString
_PaccMacSeparatorChar_Object = MibScalar
paccMacSeparatorChar = _PaccMacSeparatorChar_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 4),
    _PaccMacSeparatorChar_Type()
)
paccMacSeparatorChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccMacSeparatorChar.setStatus("current")


class _PaccMacSpelling_Type(Integer32):
    """Custom type paccMacSpelling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lowerCase", 0),
          ("upperCase", 1))
    )


_PaccMacSpelling_Type.__name__ = "Integer32"
_PaccMacSpelling_Object = MibScalar
paccMacSpelling = _PaccMacSpelling_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 5),
    _PaccMacSpelling_Type()
)
paccMacSpelling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccMacSpelling.setStatus("current")


class _PaccMacPasswordSource_Type(Integer32):
    """Custom type paccMacPasswordSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useMac", 0),
          ("usePassword", 1))
    )


_PaccMacPasswordSource_Type.__name__ = "Integer32"
_PaccMacPasswordSource_Object = MibScalar
paccMacPasswordSource = _PaccMacPasswordSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 6),
    _PaccMacPasswordSource_Type()
)
paccMacPasswordSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccMacPasswordSource.setStatus("current")
_PaccMacPasswordString_Type = DisplayString
_PaccMacPasswordString_Object = MibScalar
paccMacPasswordString = _PaccMacPasswordString_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 7),
    _PaccMacPasswordString_Type()
)
paccMacPasswordString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccMacPasswordString.setStatus("current")
_PaccPrimaryAuthServerName_Type = DisplayString
_PaccPrimaryAuthServerName_Object = MibScalar
paccPrimaryAuthServerName = _PaccPrimaryAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 8),
    _PaccPrimaryAuthServerName_Type()
)
paccPrimaryAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccPrimaryAuthServerName.setStatus("current")
_PaccPrimaryAcctServerName_Type = DisplayString
_PaccPrimaryAcctServerName_Object = MibScalar
paccPrimaryAcctServerName = _PaccPrimaryAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 9),
    _PaccPrimaryAcctServerName_Type()
)
paccPrimaryAcctServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccPrimaryAcctServerName.setStatus("current")
_PaccFallbackAuthServerName_Type = DisplayString
_PaccFallbackAuthServerName_Object = MibScalar
paccFallbackAuthServerName = _PaccFallbackAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 10),
    _PaccFallbackAuthServerName_Type()
)
paccFallbackAuthServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccFallbackAuthServerName.setStatus("current")
_PaccFallbackAcctServerName_Type = DisplayString
_PaccFallbackAcctServerName_Object = MibScalar
paccFallbackAcctServerName = _PaccFallbackAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 11),
    _PaccFallbackAcctServerName_Type()
)
paccFallbackAcctServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccFallbackAcctServerName.setStatus("current")


class _PaccServerDownTimeout_Type(Integer32):
    """Custom type paccServerDownTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PaccServerDownTimeout_Type.__name__ = "Integer32"
_PaccServerDownTimeout_Object = MibScalar
paccServerDownTimeout = _PaccServerDownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 12),
    _PaccServerDownTimeout_Type()
)
paccServerDownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccServerDownTimeout.setStatus("current")
_PaccFilterAuthorizedMac_Type = DisplayString
_PaccFilterAuthorizedMac_Object = MibScalar
paccFilterAuthorizedMac = _PaccFilterAuthorizedMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 13),
    _PaccFilterAuthorizedMac_Type()
)
paccFilterAuthorizedMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccFilterAuthorizedMac.setStatus("current")
_PaccFilterAuthorizedPort_Type = DisplayString
_PaccFilterAuthorizedPort_Object = MibScalar
paccFilterAuthorizedPort = _PaccFilterAuthorizedPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 14),
    _PaccFilterAuthorizedPort_Type()
)
paccFilterAuthorizedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccFilterAuthorizedPort.setStatus("current")
_PaccFilterAuthorizedUser_Type = DisplayString
_PaccFilterAuthorizedUser_Object = MibScalar
paccFilterAuthorizedUser = _PaccFilterAuthorizedUser_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 15),
    _PaccFilterAuthorizedUser_Type()
)
paccFilterAuthorizedUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paccFilterAuthorizedUser.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1)
)
portConfigEntry.setIndexNames(
    (0, "G6-PACC-MIB", "portConfigPortIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigPortIndex_Type(Integer32):
    """Custom type portConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortConfigPortIndex_Type.__name__ = "Integer32"
_PortConfigPortIndex_Object = MibTableColumn
portConfigPortIndex = _PortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 1),
    _PortConfigPortIndex_Type()
)
portConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portConfigPortIndex.setStatus("current")


class _PortConfigAuthorizeMode_Type(Integer32):
    """Custom type portConfigAuthorizeMode based on Integer32"""
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
        *(("alwaysAuthorized", 0),
          ("viaMacTable", 1),
          ("macViaRadius", 2),
          ("ms8021xViaRadius", 3),
          ("macOr8021xViaRadius", 4),
          ("forceUnauthorized", 5),
          ("macEventOnly", 6),
          ("edge8021xViaRadius", 7))
    )


_PortConfigAuthorizeMode_Type.__name__ = "Integer32"
_PortConfigAuthorizeMode_Object = MibTableColumn
portConfigAuthorizeMode = _PortConfigAuthorizeMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 2),
    _PortConfigAuthorizeMode_Type()
)
portConfigAuthorizeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAuthorizeMode.setStatus("current")


class _PortConfigAuthorizePriority_Type(Integer32):
    """Custom type portConfigAuthorizePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prefer8021x", 0),
          ("preferMac", 1))
    )


_PortConfigAuthorizePriority_Type.__name__ = "Integer32"
_PortConfigAuthorizePriority_Object = MibTableColumn
portConfigAuthorizePriority = _PortConfigAuthorizePriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 3),
    _PortConfigAuthorizePriority_Type()
)
portConfigAuthorizePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAuthorizePriority.setStatus("current")


class _PortConfigUnauthorizedMode_Type(Integer32):
    """Custom type portConfigUnauthorizedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 0),
          ("useUnauthorizedVlan", 1),
          ("incomingBlocked", 2))
    )


_PortConfigUnauthorizedMode_Type.__name__ = "Integer32"
_PortConfigUnauthorizedMode_Object = MibTableColumn
portConfigUnauthorizedMode = _PortConfigUnauthorizedMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 4),
    _PortConfigUnauthorizedMode_Type()
)
portConfigUnauthorizedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigUnauthorizedMode.setStatus("current")
_PortConfigAuthFailRetryTimer_Type = Unsigned32
_PortConfigAuthFailRetryTimer_Object = MibTableColumn
portConfigAuthFailRetryTimer = _PortConfigAuthFailRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 5),
    _PortConfigAuthFailRetryTimer_Type()
)
portConfigAuthFailRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigAuthFailRetryTimer.setStatus("current")


class _PortConfigMacTimeout_Type(Integer32):
    """Custom type portConfigMacTimeout based on Integer32"""
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
          ("slow", 1),
          ("fast", 2))
    )


_PortConfigMacTimeout_Type.__name__ = "Integer32"
_PortConfigMacTimeout_Object = MibTableColumn
portConfigMacTimeout = _PortConfigMacTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 6),
    _PortConfigMacTimeout_Type()
)
portConfigMacTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMacTimeout.setStatus("current")


class _PortConfigLimitedNumberOfMacs_Type(Integer32):
    """Custom type portConfigLimitedNumberOfMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortConfigLimitedNumberOfMacs_Type.__name__ = "Integer32"
_PortConfigLimitedNumberOfMacs_Object = MibTableColumn
portConfigLimitedNumberOfMacs = _PortConfigLimitedNumberOfMacs_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 7),
    _PortConfigLimitedNumberOfMacs_Type()
)
portConfigLimitedNumberOfMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigLimitedNumberOfMacs.setStatus("current")


class _PortConfigDropUnknownUnicasts_Type(Integer32):
    """Custom type portConfigDropUnknownUnicasts based on Integer32"""
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


_PortConfigDropUnknownUnicasts_Type.__name__ = "Integer32"
_PortConfigDropUnknownUnicasts_Object = MibTableColumn
portConfigDropUnknownUnicasts = _PortConfigDropUnknownUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 8),
    _PortConfigDropUnknownUnicasts_Type()
)
portConfigDropUnknownUnicasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDropUnknownUnicasts.setStatus("current")


class _PortConfigDropEgressBroadcasts_Type(Integer32):
    """Custom type portConfigDropEgressBroadcasts based on Integer32"""
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


_PortConfigDropEgressBroadcasts_Type.__name__ = "Integer32"
_PortConfigDropEgressBroadcasts_Object = MibTableColumn
portConfigDropEgressBroadcasts = _PortConfigDropEgressBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 9),
    _PortConfigDropEgressBroadcasts_Type()
)
portConfigDropEgressBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDropEgressBroadcasts.setStatus("current")
_PortConfigLearnMacNow_Type = DisplayString
_PortConfigLearnMacNow_Object = MibTableColumn
portConfigLearnMacNow = _PortConfigLearnMacNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 10),
    _PortConfigLearnMacNow_Type()
)
portConfigLearnMacNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigLearnMacNow.setStatus("current")
_PortConfigReauthenticate_Type = DisplayString
_PortConfigReauthenticate_Object = MibTableColumn
portConfigReauthenticate = _PortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 11),
    _PortConfigReauthenticate_Type()
)
portConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigReauthenticate.setStatus("current")
_PortConfigUnauthorizeMac_Type = DisplayString
_PortConfigUnauthorizeMac_Object = MibTableColumn
portConfigUnauthorizeMac = _PortConfigUnauthorizeMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 16, 1, 12),
    _PortConfigUnauthorizeMac_Type()
)
portConfigUnauthorizeMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigUnauthorizeMac.setStatus("current")
_AuthorizedMacsTable_Object = MibTable
authorizedMacsTable = _AuthorizedMacsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17)
)
if mibBuilder.loadTexts:
    authorizedMacsTable.setStatus("current")
_AuthorizedMacsEntry_Object = MibTableRow
authorizedMacsEntry = _AuthorizedMacsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1)
)
authorizedMacsEntry.setIndexNames(
    (0, "G6-PACC-MIB", "authorizedMacsIndex"),
)
if mibBuilder.loadTexts:
    authorizedMacsEntry.setStatus("current")


class _AuthorizedMacsIndex_Type(Integer32):
    """Custom type authorizedMacsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AuthorizedMacsIndex_Type.__name__ = "Integer32"
_AuthorizedMacsIndex_Object = MibTableColumn
authorizedMacsIndex = _AuthorizedMacsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1, 1),
    _AuthorizedMacsIndex_Type()
)
authorizedMacsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authorizedMacsIndex.setStatus("current")
_AuthorizedMacsName_Type = DisplayString
_AuthorizedMacsName_Object = MibTableColumn
authorizedMacsName = _AuthorizedMacsName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1, 2),
    _AuthorizedMacsName_Type()
)
authorizedMacsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedMacsName.setStatus("current")
_AuthorizedMacsMacAddress_Type = MacAddress
_AuthorizedMacsMacAddress_Object = MibTableColumn
authorizedMacsMacAddress = _AuthorizedMacsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1, 3),
    _AuthorizedMacsMacAddress_Type()
)
authorizedMacsMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedMacsMacAddress.setStatus("current")
_AuthorizedMacsPermittedPorts_Type = Integer32
_AuthorizedMacsPermittedPorts_Object = MibTableColumn
authorizedMacsPermittedPorts = _AuthorizedMacsPermittedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1, 4),
    _AuthorizedMacsPermittedPorts_Type()
)
authorizedMacsPermittedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedMacsPermittedPorts.setStatus("current")


class _AuthorizedMacsTreatAsVendorMac_Type(Integer32):
    """Custom type authorizedMacsTreatAsVendorMac based on Integer32"""
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


_AuthorizedMacsTreatAsVendorMac_Type.__name__ = "Integer32"
_AuthorizedMacsTreatAsVendorMac_Object = MibTableColumn
authorizedMacsTreatAsVendorMac = _AuthorizedMacsTreatAsVendorMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 17, 1, 5),
    _AuthorizedMacsTreatAsVendorMac_Type()
)
authorizedMacsTreatAsVendorMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authorizedMacsTreatAsVendorMac.setStatus("current")
_SupplicantTable_Object = MibTable
supplicantTable = _SupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18)
)
if mibBuilder.loadTexts:
    supplicantTable.setStatus("current")
_SupplicantEntry_Object = MibTableRow
supplicantEntry = _SupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1)
)
supplicantEntry.setIndexNames(
    (0, "G6-PACC-MIB", "supplicantIndex"),
)
if mibBuilder.loadTexts:
    supplicantEntry.setStatus("current")


class _SupplicantIndex_Type(Integer32):
    """Custom type supplicantIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_SupplicantIndex_Type.__name__ = "Integer32"
_SupplicantIndex_Object = MibTableColumn
supplicantIndex = _SupplicantIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 1),
    _SupplicantIndex_Type()
)
supplicantIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    supplicantIndex.setStatus("current")


class _SupplicantEnableSupplicant_Type(Integer32):
    """Custom type supplicantEnableSupplicant based on Integer32"""
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


_SupplicantEnableSupplicant_Type.__name__ = "Integer32"
_SupplicantEnableSupplicant_Object = MibTableColumn
supplicantEnableSupplicant = _SupplicantEnableSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 2),
    _SupplicantEnableSupplicant_Type()
)
supplicantEnableSupplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantEnableSupplicant.setStatus("current")


class _SupplicantPort_Type(Integer32):
    """Custom type supplicantPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SupplicantPort_Type.__name__ = "Integer32"
_SupplicantPort_Object = MibTableColumn
supplicantPort = _SupplicantPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 3),
    _SupplicantPort_Type()
)
supplicantPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantPort.setStatus("current")


class _SupplicantActionOnLinkDown_Type(Integer32):
    """Custom type supplicantActionOnLinkDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("deauthenticate", 1))
    )


_SupplicantActionOnLinkDown_Type.__name__ = "Integer32"
_SupplicantActionOnLinkDown_Object = MibTableColumn
supplicantActionOnLinkDown = _SupplicantActionOnLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 4),
    _SupplicantActionOnLinkDown_Type()
)
supplicantActionOnLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantActionOnLinkDown.setStatus("current")
_SupplicantIdentity_Type = DisplayString
_SupplicantIdentity_Object = MibTableColumn
supplicantIdentity = _SupplicantIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 5),
    _SupplicantIdentity_Type()
)
supplicantIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantIdentity.setStatus("current")
_SupplicantAnonymousIdentity_Type = DisplayString
_SupplicantAnonymousIdentity_Object = MibTableColumn
supplicantAnonymousIdentity = _SupplicantAnonymousIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 6),
    _SupplicantAnonymousIdentity_Type()
)
supplicantAnonymousIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantAnonymousIdentity.setStatus("current")
_SupplicantAuthenticationProtocol_Type = DisplayString
_SupplicantAuthenticationProtocol_Object = MibTableColumn
supplicantAuthenticationProtocol = _SupplicantAuthenticationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 7),
    _SupplicantAuthenticationProtocol_Type()
)
supplicantAuthenticationProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantAuthenticationProtocol.setStatus("current")
_SupplicantEnterPassword_Type = DisplayString
_SupplicantEnterPassword_Object = MibTableColumn
supplicantEnterPassword = _SupplicantEnterPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 8),
    _SupplicantEnterPassword_Type()
)
supplicantEnterPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantEnterPassword.setStatus("current")
_SupplicantEncryptedAuthPassword_Type = DisplayString
_SupplicantEncryptedAuthPassword_Object = MibTableColumn
supplicantEncryptedAuthPassword = _SupplicantEncryptedAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 9),
    _SupplicantEncryptedAuthPassword_Type()
)
supplicantEncryptedAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantEncryptedAuthPassword.setStatus("current")
_SupplicantReauthenticate_Type = DisplayString
_SupplicantReauthenticate_Object = MibTableColumn
supplicantReauthenticate = _SupplicantReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 18, 1, 10),
    _SupplicantReauthenticate_Type()
)
supplicantReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supplicantReauthenticate.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusEntry_Object = MibTableRow
portStatusEntry = _PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1)
)
portStatusEntry.setIndexNames(
    (0, "G6-PACC-MIB", "portStatusPortIndex"),
)
if mibBuilder.loadTexts:
    portStatusEntry.setStatus("current")


class _PortStatusPortIndex_Type(Integer32):
    """Custom type portStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortStatusPortIndex_Type.__name__ = "Integer32"
_PortStatusPortIndex_Object = MibTableColumn
portStatusPortIndex = _PortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 1),
    _PortStatusPortIndex_Type()
)
portStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatusPortIndex.setStatus("current")


class _PortStatusAuthorizationState_Type(Integer32):
    """Custom type portStatusAuthorizationState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("unauthorized", 2),
          ("processing", 3),
          ("authorized", 4),
          ("rejected", 5))
    )


_PortStatusAuthorizationState_Type.__name__ = "Integer32"
_PortStatusAuthorizationState_Object = MibTableColumn
portStatusAuthorizationState = _PortStatusAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 2),
    _PortStatusAuthorizationState_Type()
)
portStatusAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusAuthorizationState.setStatus("current")


class _PortStatusAuthorizationMode_Type(Integer32):
    """Custom type portStatusAuthorizationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("viaMacTable", 1),
          ("macViaRadius", 2),
          ("ms8021xViaRadius", 3),
          ("viaMacEventOnly", 6),
          ("edge8021xViaRadius", 7))
    )


_PortStatusAuthorizationMode_Type.__name__ = "Integer32"
_PortStatusAuthorizationMode_Object = MibTableColumn
portStatusAuthorizationMode = _PortStatusAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 3),
    _PortStatusAuthorizationMode_Type()
)
portStatusAuthorizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusAuthorizationMode.setStatus("current")
_PortStatusLastStateChange_Type = DisplayString
_PortStatusLastStateChange_Object = MibTableColumn
portStatusLastStateChange = _PortStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 4),
    _PortStatusLastStateChange_Type()
)
portStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLastStateChange.setStatus("current")


class _PortStatusNumberOfMacsToLearn_Type(Integer32):
    """Custom type portStatusNumberOfMacsToLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortStatusNumberOfMacsToLearn_Type.__name__ = "Integer32"
_PortStatusNumberOfMacsToLearn_Object = MibTableColumn
portStatusNumberOfMacsToLearn = _PortStatusNumberOfMacsToLearn_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 5),
    _PortStatusNumberOfMacsToLearn_Type()
)
portStatusNumberOfMacsToLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusNumberOfMacsToLearn.setStatus("current")


class _PortStatusNumberOfLearnedMacs_Type(Integer32):
    """Custom type portStatusNumberOfLearnedMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortStatusNumberOfLearnedMacs_Type.__name__ = "Integer32"
_PortStatusNumberOfLearnedMacs_Object = MibTableColumn
portStatusNumberOfLearnedMacs = _PortStatusNumberOfLearnedMacs_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 100, 1, 6),
    _PortStatusNumberOfLearnedMacs_Type()
)
portStatusNumberOfLearnedMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusNumberOfLearnedMacs.setStatus("current")
_PortMacStatusTable_Object = MibTable
portMacStatusTable = _PortMacStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101)
)
if mibBuilder.loadTexts:
    portMacStatusTable.setStatus("current")
_PortMacStatusEntry_Object = MibTableRow
portMacStatusEntry = _PortMacStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1)
)
portMacStatusEntry.setIndexNames(
    (0, "G6-PACC-MIB", "portMacStatusPortIndex"),
)
if mibBuilder.loadTexts:
    portMacStatusEntry.setStatus("current")


class _PortMacStatusPortIndex_Type(Integer32):
    """Custom type portMacStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortMacStatusPortIndex_Type.__name__ = "Integer32"
_PortMacStatusPortIndex_Object = MibTableColumn
portMacStatusPortIndex = _PortMacStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 1),
    _PortMacStatusPortIndex_Type()
)
portMacStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portMacStatusPortIndex.setStatus("current")


class _PortMacStatusAuthorizationState_Type(Integer32):
    """Custom type portMacStatusAuthorizationState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("unauthorized", 2),
          ("processing", 3),
          ("authorized", 4),
          ("rejected", 5))
    )


_PortMacStatusAuthorizationState_Type.__name__ = "Integer32"
_PortMacStatusAuthorizationState_Object = MibTableColumn
portMacStatusAuthorizationState = _PortMacStatusAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 2),
    _PortMacStatusAuthorizationState_Type()
)
portMacStatusAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusAuthorizationState.setStatus("current")
_PortMacStatusUserMac_Type = MacAddress
_PortMacStatusUserMac_Object = MibTableColumn
portMacStatusUserMac = _PortMacStatusUserMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 3),
    _PortMacStatusUserMac_Type()
)
portMacStatusUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusUserMac.setStatus("current")
_PortMacStatusUserName_Type = DisplayString
_PortMacStatusUserName_Object = MibTableColumn
portMacStatusUserName = _PortMacStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 4),
    _PortMacStatusUserName_Type()
)
portMacStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusUserName.setStatus("current")
_PortMacStatusVlanAlias_Type = DisplayString
_PortMacStatusVlanAlias_Object = MibTableColumn
portMacStatusVlanAlias = _PortMacStatusVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 5),
    _PortMacStatusVlanAlias_Type()
)
portMacStatusVlanAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusVlanAlias.setStatus("current")


class _PortMacStatusVlanId_Type(Integer32):
    """Custom type portMacStatusVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortMacStatusVlanId_Type.__name__ = "Integer32"
_PortMacStatusVlanId_Object = MibTableColumn
portMacStatusVlanId = _PortMacStatusVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 6),
    _PortMacStatusVlanId_Type()
)
portMacStatusVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusVlanId.setStatus("current")


class _PortMacStatusIdleTimeout_Type(Integer32):
    """Custom type portMacStatusIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortMacStatusIdleTimeout_Type.__name__ = "Integer32"
_PortMacStatusIdleTimeout_Object = MibTableColumn
portMacStatusIdleTimeout = _PortMacStatusIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 7),
    _PortMacStatusIdleTimeout_Type()
)
portMacStatusIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusIdleTimeout.setStatus("current")


class _PortMacStatusSessionTimeout_Type(Integer32):
    """Custom type portMacStatusSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortMacStatusSessionTimeout_Type.__name__ = "Integer32"
_PortMacStatusSessionTimeout_Object = MibTableColumn
portMacStatusSessionTimeout = _PortMacStatusSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 8),
    _PortMacStatusSessionTimeout_Type()
)
portMacStatusSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusSessionTimeout.setStatus("current")
_PortMacStatusFilterId_Type = DisplayString
_PortMacStatusFilterId_Object = MibTableColumn
portMacStatusFilterId = _PortMacStatusFilterId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 9),
    _PortMacStatusFilterId_Type()
)
portMacStatusFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusFilterId.setStatus("current")
_PortMacStatusLastStateChange_Type = DisplayString
_PortMacStatusLastStateChange_Object = MibTableColumn
portMacStatusLastStateChange = _PortMacStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 101, 1, 10),
    _PortMacStatusLastStateChange_Type()
)
portMacStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacStatusLastStateChange.setStatus("current")
_Port8021xStatusTable_Object = MibTable
port8021xStatusTable = _Port8021xStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102)
)
if mibBuilder.loadTexts:
    port8021xStatusTable.setStatus("current")
_Port8021xStatusEntry_Object = MibTableRow
port8021xStatusEntry = _Port8021xStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1)
)
port8021xStatusEntry.setIndexNames(
    (0, "G6-PACC-MIB", "port8021xStatusPortIndex"),
)
if mibBuilder.loadTexts:
    port8021xStatusEntry.setStatus("current")


class _Port8021xStatusPortIndex_Type(Integer32):
    """Custom type port8021xStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Port8021xStatusPortIndex_Type.__name__ = "Integer32"
_Port8021xStatusPortIndex_Object = MibTableColumn
port8021xStatusPortIndex = _Port8021xStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 1),
    _Port8021xStatusPortIndex_Type()
)
port8021xStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    port8021xStatusPortIndex.setStatus("current")


class _Port8021xStatusAuthorizationState_Type(Integer32):
    """Custom type port8021xStatusAuthorizationState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("unauthorized", 2),
          ("processing", 3),
          ("authorized", 4),
          ("rejected", 5))
    )


_Port8021xStatusAuthorizationState_Type.__name__ = "Integer32"
_Port8021xStatusAuthorizationState_Object = MibTableColumn
port8021xStatusAuthorizationState = _Port8021xStatusAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 2),
    _Port8021xStatusAuthorizationState_Type()
)
port8021xStatusAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusAuthorizationState.setStatus("current")
_Port8021xStatusUserMac_Type = MacAddress
_Port8021xStatusUserMac_Object = MibTableColumn
port8021xStatusUserMac = _Port8021xStatusUserMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 3),
    _Port8021xStatusUserMac_Type()
)
port8021xStatusUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusUserMac.setStatus("current")
_Port8021xStatusUserName_Type = DisplayString
_Port8021xStatusUserName_Object = MibTableColumn
port8021xStatusUserName = _Port8021xStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 4),
    _Port8021xStatusUserName_Type()
)
port8021xStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusUserName.setStatus("current")
_Port8021xStatusVlanAlias_Type = DisplayString
_Port8021xStatusVlanAlias_Object = MibTableColumn
port8021xStatusVlanAlias = _Port8021xStatusVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 5),
    _Port8021xStatusVlanAlias_Type()
)
port8021xStatusVlanAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusVlanAlias.setStatus("current")


class _Port8021xStatusVlanId_Type(Integer32):
    """Custom type port8021xStatusVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Port8021xStatusVlanId_Type.__name__ = "Integer32"
_Port8021xStatusVlanId_Object = MibTableColumn
port8021xStatusVlanId = _Port8021xStatusVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 6),
    _Port8021xStatusVlanId_Type()
)
port8021xStatusVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusVlanId.setStatus("current")


class _Port8021xStatusIdleTimeout_Type(Integer32):
    """Custom type port8021xStatusIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Port8021xStatusIdleTimeout_Type.__name__ = "Integer32"
_Port8021xStatusIdleTimeout_Object = MibTableColumn
port8021xStatusIdleTimeout = _Port8021xStatusIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 7),
    _Port8021xStatusIdleTimeout_Type()
)
port8021xStatusIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusIdleTimeout.setStatus("current")


class _Port8021xStatusSessionTimeout_Type(Integer32):
    """Custom type port8021xStatusSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Port8021xStatusSessionTimeout_Type.__name__ = "Integer32"
_Port8021xStatusSessionTimeout_Object = MibTableColumn
port8021xStatusSessionTimeout = _Port8021xStatusSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 8),
    _Port8021xStatusSessionTimeout_Type()
)
port8021xStatusSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusSessionTimeout.setStatus("current")
_Port8021xStatusFilterId_Type = DisplayString
_Port8021xStatusFilterId_Object = MibTableColumn
port8021xStatusFilterId = _Port8021xStatusFilterId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 9),
    _Port8021xStatusFilterId_Type()
)
port8021xStatusFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusFilterId.setStatus("current")
_Port8021xStatusLastStateChange_Type = DisplayString
_Port8021xStatusLastStateChange_Object = MibTableColumn
port8021xStatusLastStateChange = _Port8021xStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 102, 1, 10),
    _Port8021xStatusLastStateChange_Type()
)
port8021xStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port8021xStatusLastStateChange.setStatus("current")
_UserStatusTable_Object = MibTable
userStatusTable = _UserStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103)
)
if mibBuilder.loadTexts:
    userStatusTable.setStatus("current")
_UserStatusEntry_Object = MibTableRow
userStatusEntry = _UserStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1)
)
userStatusEntry.setIndexNames(
    (0, "G6-PACC-MIB", "userStatusIndex"),
)
if mibBuilder.loadTexts:
    userStatusEntry.setStatus("current")


class _UserStatusIndex_Type(Integer32):
    """Custom type userStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 249),
    )


_UserStatusIndex_Type.__name__ = "Integer32"
_UserStatusIndex_Object = MibTableColumn
userStatusIndex = _UserStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 1),
    _UserStatusIndex_Type()
)
userStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userStatusIndex.setStatus("current")


class _UserStatusEntryState_Type(Integer32):
    """Custom type userStatusEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("inactive", 1),
          ("active", 2))
    )


_UserStatusEntryState_Type.__name__ = "Integer32"
_UserStatusEntryState_Object = MibTableColumn
userStatusEntryState = _UserStatusEntryState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 2),
    _UserStatusEntryState_Type()
)
userStatusEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusEntryState.setStatus("current")


class _UserStatusAuthorizationState_Type(Integer32):
    """Custom type userStatusAuthorizationState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("unauthorized", 2),
          ("processing", 3),
          ("authorized", 4),
          ("rejected", 5))
    )


_UserStatusAuthorizationState_Type.__name__ = "Integer32"
_UserStatusAuthorizationState_Object = MibTableColumn
userStatusAuthorizationState = _UserStatusAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 3),
    _UserStatusAuthorizationState_Type()
)
userStatusAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusAuthorizationState.setStatus("current")


class _UserStatusAuthorizationMode_Type(Integer32):
    """Custom type userStatusAuthorizationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("viaMacTable", 1),
          ("macViaRadius", 2),
          ("ms8021xViaRadius", 3),
          ("viaMacEventOnly", 6),
          ("edge8021xViaRadius", 7))
    )


_UserStatusAuthorizationMode_Type.__name__ = "Integer32"
_UserStatusAuthorizationMode_Object = MibTableColumn
userStatusAuthorizationMode = _UserStatusAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 4),
    _UserStatusAuthorizationMode_Type()
)
userStatusAuthorizationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusAuthorizationMode.setStatus("current")


class _UserStatusPort_Type(Integer32):
    """Custom type userStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserStatusPort_Type.__name__ = "Integer32"
_UserStatusPort_Object = MibTableColumn
userStatusPort = _UserStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 5),
    _UserStatusPort_Type()
)
userStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusPort.setStatus("current")
_UserStatusUserMac_Type = MacAddress
_UserStatusUserMac_Object = MibTableColumn
userStatusUserMac = _UserStatusUserMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 6),
    _UserStatusUserMac_Type()
)
userStatusUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusUserMac.setStatus("current")
_UserStatusUserName_Type = DisplayString
_UserStatusUserName_Object = MibTableColumn
userStatusUserName = _UserStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 7),
    _UserStatusUserName_Type()
)
userStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusUserName.setStatus("current")
_UserStatusVlanAlias_Type = DisplayString
_UserStatusVlanAlias_Object = MibTableColumn
userStatusVlanAlias = _UserStatusVlanAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 8),
    _UserStatusVlanAlias_Type()
)
userStatusVlanAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusVlanAlias.setStatus("current")


class _UserStatusVlanId_Type(Integer32):
    """Custom type userStatusVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserStatusVlanId_Type.__name__ = "Integer32"
_UserStatusVlanId_Object = MibTableColumn
userStatusVlanId = _UserStatusVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 9),
    _UserStatusVlanId_Type()
)
userStatusVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusVlanId.setStatus("current")


class _UserStatusIdleTimeout_Type(Integer32):
    """Custom type userStatusIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserStatusIdleTimeout_Type.__name__ = "Integer32"
_UserStatusIdleTimeout_Object = MibTableColumn
userStatusIdleTimeout = _UserStatusIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 10),
    _UserStatusIdleTimeout_Type()
)
userStatusIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusIdleTimeout.setStatus("current")


class _UserStatusSessionTimeout_Type(Integer32):
    """Custom type userStatusSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UserStatusSessionTimeout_Type.__name__ = "Integer32"
_UserStatusSessionTimeout_Object = MibTableColumn
userStatusSessionTimeout = _UserStatusSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 11),
    _UserStatusSessionTimeout_Type()
)
userStatusSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusSessionTimeout.setStatus("current")
_UserStatusFilterId_Type = DisplayString
_UserStatusFilterId_Object = MibTableColumn
userStatusFilterId = _UserStatusFilterId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 12),
    _UserStatusFilterId_Type()
)
userStatusFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusFilterId.setStatus("current")
_UserStatusLoginTimeStamp_Type = DisplayString
_UserStatusLoginTimeStamp_Object = MibTableColumn
userStatusLoginTimeStamp = _UserStatusLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 13),
    _UserStatusLoginTimeStamp_Type()
)
userStatusLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusLoginTimeStamp.setStatus("current")
_UserStatusLoginEpoch_Type = Unsigned32
_UserStatusLoginEpoch_Object = MibTableColumn
userStatusLoginEpoch = _UserStatusLoginEpoch_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 46, 103, 1, 14),
    _UserStatusLoginEpoch_Type()
)
userStatusLoginEpoch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userStatusLoginEpoch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-PACC-MIB",
    **{"protocol": protocol,
       "pacc": pacc,
       "paccEnablePortAccessControl": paccEnablePortAccessControl,
       "paccReauthenticationPeriod": paccReauthenticationPeriod,
       "paccNasIdentifier": paccNasIdentifier,
       "paccMacSeparatorChar": paccMacSeparatorChar,
       "paccMacSpelling": paccMacSpelling,
       "paccMacPasswordSource": paccMacPasswordSource,
       "paccMacPasswordString": paccMacPasswordString,
       "paccPrimaryAuthServerName": paccPrimaryAuthServerName,
       "paccPrimaryAcctServerName": paccPrimaryAcctServerName,
       "paccFallbackAuthServerName": paccFallbackAuthServerName,
       "paccFallbackAcctServerName": paccFallbackAcctServerName,
       "paccServerDownTimeout": paccServerDownTimeout,
       "paccFilterAuthorizedMac": paccFilterAuthorizedMac,
       "paccFilterAuthorizedPort": paccFilterAuthorizedPort,
       "paccFilterAuthorizedUser": paccFilterAuthorizedUser,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigPortIndex": portConfigPortIndex,
       "portConfigAuthorizeMode": portConfigAuthorizeMode,
       "portConfigAuthorizePriority": portConfigAuthorizePriority,
       "portConfigUnauthorizedMode": portConfigUnauthorizedMode,
       "portConfigAuthFailRetryTimer": portConfigAuthFailRetryTimer,
       "portConfigMacTimeout": portConfigMacTimeout,
       "portConfigLimitedNumberOfMacs": portConfigLimitedNumberOfMacs,
       "portConfigDropUnknownUnicasts": portConfigDropUnknownUnicasts,
       "portConfigDropEgressBroadcasts": portConfigDropEgressBroadcasts,
       "portConfigLearnMacNow": portConfigLearnMacNow,
       "portConfigReauthenticate": portConfigReauthenticate,
       "portConfigUnauthorizeMac": portConfigUnauthorizeMac,
       "authorizedMacsTable": authorizedMacsTable,
       "authorizedMacsEntry": authorizedMacsEntry,
       "authorizedMacsIndex": authorizedMacsIndex,
       "authorizedMacsName": authorizedMacsName,
       "authorizedMacsMacAddress": authorizedMacsMacAddress,
       "authorizedMacsPermittedPorts": authorizedMacsPermittedPorts,
       "authorizedMacsTreatAsVendorMac": authorizedMacsTreatAsVendorMac,
       "supplicantTable": supplicantTable,
       "supplicantEntry": supplicantEntry,
       "supplicantIndex": supplicantIndex,
       "supplicantEnableSupplicant": supplicantEnableSupplicant,
       "supplicantPort": supplicantPort,
       "supplicantActionOnLinkDown": supplicantActionOnLinkDown,
       "supplicantIdentity": supplicantIdentity,
       "supplicantAnonymousIdentity": supplicantAnonymousIdentity,
       "supplicantAuthenticationProtocol": supplicantAuthenticationProtocol,
       "supplicantEnterPassword": supplicantEnterPassword,
       "supplicantEncryptedAuthPassword": supplicantEncryptedAuthPassword,
       "supplicantReauthenticate": supplicantReauthenticate,
       "portStatusTable": portStatusTable,
       "portStatusEntry": portStatusEntry,
       "portStatusPortIndex": portStatusPortIndex,
       "portStatusAuthorizationState": portStatusAuthorizationState,
       "portStatusAuthorizationMode": portStatusAuthorizationMode,
       "portStatusLastStateChange": portStatusLastStateChange,
       "portStatusNumberOfMacsToLearn": portStatusNumberOfMacsToLearn,
       "portStatusNumberOfLearnedMacs": portStatusNumberOfLearnedMacs,
       "portMacStatusTable": portMacStatusTable,
       "portMacStatusEntry": portMacStatusEntry,
       "portMacStatusPortIndex": portMacStatusPortIndex,
       "portMacStatusAuthorizationState": portMacStatusAuthorizationState,
       "portMacStatusUserMac": portMacStatusUserMac,
       "portMacStatusUserName": portMacStatusUserName,
       "portMacStatusVlanAlias": portMacStatusVlanAlias,
       "portMacStatusVlanId": portMacStatusVlanId,
       "portMacStatusIdleTimeout": portMacStatusIdleTimeout,
       "portMacStatusSessionTimeout": portMacStatusSessionTimeout,
       "portMacStatusFilterId": portMacStatusFilterId,
       "portMacStatusLastStateChange": portMacStatusLastStateChange,
       "port8021xStatusTable": port8021xStatusTable,
       "port8021xStatusEntry": port8021xStatusEntry,
       "port8021xStatusPortIndex": port8021xStatusPortIndex,
       "port8021xStatusAuthorizationState": port8021xStatusAuthorizationState,
       "port8021xStatusUserMac": port8021xStatusUserMac,
       "port8021xStatusUserName": port8021xStatusUserName,
       "port8021xStatusVlanAlias": port8021xStatusVlanAlias,
       "port8021xStatusVlanId": port8021xStatusVlanId,
       "port8021xStatusIdleTimeout": port8021xStatusIdleTimeout,
       "port8021xStatusSessionTimeout": port8021xStatusSessionTimeout,
       "port8021xStatusFilterId": port8021xStatusFilterId,
       "port8021xStatusLastStateChange": port8021xStatusLastStateChange,
       "userStatusTable": userStatusTable,
       "userStatusEntry": userStatusEntry,
       "userStatusIndex": userStatusIndex,
       "userStatusEntryState": userStatusEntryState,
       "userStatusAuthorizationState": userStatusAuthorizationState,
       "userStatusAuthorizationMode": userStatusAuthorizationMode,
       "userStatusPort": userStatusPort,
       "userStatusUserMac": userStatusUserMac,
       "userStatusUserName": userStatusUserName,
       "userStatusVlanAlias": userStatusVlanAlias,
       "userStatusVlanId": userStatusVlanId,
       "userStatusIdleTimeout": userStatusIdleTimeout,
       "userStatusSessionTimeout": userStatusSessionTimeout,
       "userStatusFilterId": userStatusFilterId,
       "userStatusLoginTimeStamp": userStatusLoginTimeStamp,
       "userStatusLoginEpoch": userStatusLoginEpoch}
)
