# SNMP MIB module (ARICENT-PNAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-PNAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:02 2025
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

(PaeControlledPortStatus,
 dot1xAuthOperControlledDirections) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus",
    "dot1xAuthOperControlledDirections")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fspnac = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64)
)
if mibBuilder.loadTexts:
    fspnac.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AuthenticMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteServer", 1),
          ("localServer", 2))
    )



class RemoteAuthServerType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radiusServer", 1),
          ("tacacsplusServer", 2))
    )



class PermissionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsPnacPaeSystem_ObjectIdentity = ObjectIdentity
fsPnacPaeSystem = _FsPnacPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1)
)


class _FsPnacSystemControl_Type(Integer32):
    """Custom type fsPnacSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsPnacSystemControl_Type.__name__ = "Integer32"
_FsPnacSystemControl_Object = MibScalar
fsPnacSystemControl = _FsPnacSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 1),
    _FsPnacSystemControl_Type()
)
fsPnacSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacSystemControl.setStatus("current")


class _FsPnacTraceOption_Type(Integer32):
    """Custom type fsPnacTraceOption based on Integer32"""
    defaultValue = 0


_FsPnacTraceOption_Type.__name__ = "Integer32"
_FsPnacTraceOption_Object = MibScalar
fsPnacTraceOption = _FsPnacTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 2),
    _FsPnacTraceOption_Type()
)
fsPnacTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacTraceOption.setStatus("current")
_FsPnacAuthenticServer_Type = AuthenticMethod
_FsPnacAuthenticServer_Object = MibScalar
fsPnacAuthenticServer = _FsPnacAuthenticServer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 3),
    _FsPnacAuthenticServer_Type()
)
fsPnacAuthenticServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacAuthenticServer.setStatus("current")


class _FsPnacNasId_Type(DisplayString):
    """Custom type fsPnacNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsPnacNasId_Type.__name__ = "DisplayString"
_FsPnacNasId_Object = MibScalar
fsPnacNasId = _FsPnacNasId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 4),
    _FsPnacNasId_Type()
)
fsPnacNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacNasId.setStatus("deprecated")
_FsPnacPaePortTable_Object = MibTable
fsPnacPaePortTable = _FsPnacPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5)
)
if mibBuilder.loadTexts:
    fsPnacPaePortTable.setStatus("current")
_FsPnacPaePortEntry_Object = MibTableRow
fsPnacPaePortEntry = _FsPnacPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1)
)
fsPnacPaePortEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsPnacPaePortNumber"),
)
if mibBuilder.loadTexts:
    fsPnacPaePortEntry.setStatus("current")
_FsPnacPaePortNumber_Type = InterfaceIndex
_FsPnacPaePortNumber_Object = MibTableColumn
fsPnacPaePortNumber = _FsPnacPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 1),
    _FsPnacPaePortNumber_Type()
)
fsPnacPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPnacPaePortNumber.setStatus("current")


class _FsPnacPaePortAuthMode_Type(Integer32):
    """Custom type fsPnacPaePortAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("macBased", 2))
    )


_FsPnacPaePortAuthMode_Type.__name__ = "Integer32"
_FsPnacPaePortAuthMode_Object = MibTableColumn
fsPnacPaePortAuthMode = _FsPnacPaePortAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 2),
    _FsPnacPaePortAuthMode_Type()
)
fsPnacPaePortAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaePortAuthMode.setStatus("current")
_FsPnacPaePortSupplicantCount_Type = Counter32
_FsPnacPaePortSupplicantCount_Object = MibTableColumn
fsPnacPaePortSupplicantCount = _FsPnacPaePortSupplicantCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 3),
    _FsPnacPaePortSupplicantCount_Type()
)
fsPnacPaePortSupplicantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacPaePortSupplicantCount.setStatus("current")


class _FsPnacPaePortUserName_Type(DisplayString):
    """Custom type fsPnacPaePortUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 63),
    )


_FsPnacPaePortUserName_Type.__name__ = "DisplayString"
_FsPnacPaePortUserName_Object = MibTableColumn
fsPnacPaePortUserName = _FsPnacPaePortUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 4),
    _FsPnacPaePortUserName_Type()
)
fsPnacPaePortUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaePortUserName.setStatus("current")


class _FsPnacPaePortPassword_Type(DisplayString):
    """Custom type fsPnacPaePortPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FsPnacPaePortPassword_Type.__name__ = "DisplayString"
_FsPnacPaePortPassword_Object = MibTableColumn
fsPnacPaePortPassword = _FsPnacPaePortPassword_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 5),
    _FsPnacPaePortPassword_Type()
)
fsPnacPaePortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaePortPassword.setStatus("current")
_FsPnacPaePortStatus_Type = PaeControlledPortStatus
_FsPnacPaePortStatus_Object = MibTableColumn
fsPnacPaePortStatus = _FsPnacPaePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 6),
    _FsPnacPaePortStatus_Type()
)
fsPnacPaePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacPaePortStatus.setStatus("current")


class _FsPnacPaePortStatisticsClear_Type(TruthValue):
    """Custom type fsPnacPaePortStatisticsClear based on TruthValue"""
    defaultValue = 2


_FsPnacPaePortStatisticsClear_Type.__name__ = "TruthValue"
_FsPnacPaePortStatisticsClear_Object = MibTableColumn
fsPnacPaePortStatisticsClear = _FsPnacPaePortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 7),
    _FsPnacPaePortStatisticsClear_Type()
)
fsPnacPaePortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaePortStatisticsClear.setStatus("current")


class _FsPnacPaePortAuthStatus_Type(Integer32):
    """Custom type fsPnacPaePortAuthStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsPnacPaePortAuthStatus_Type.__name__ = "Integer32"
_FsPnacPaePortAuthStatus_Object = MibTableColumn
fsPnacPaePortAuthStatus = _FsPnacPaePortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 8),
    _FsPnacPaePortAuthStatus_Type()
)
fsPnacPaePortAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaePortAuthStatus.setStatus("deprecated")


class _FsPnacPaeAuthReAuthMax_Type(Unsigned32):
    """Custom type fsPnacPaeAuthReAuthMax based on Unsigned32"""
    defaultValue = 2


_FsPnacPaeAuthReAuthMax_Type.__name__ = "Unsigned32"
_FsPnacPaeAuthReAuthMax_Object = MibTableColumn
fsPnacPaeAuthReAuthMax = _FsPnacPaeAuthReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 5, 1, 9),
    _FsPnacPaeAuthReAuthMax_Type()
)
fsPnacPaeAuthReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacPaeAuthReAuthMax.setStatus("current")


class _FsPnacModuleOperStatus_Type(Integer32):
    """Custom type fsPnacModuleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsPnacModuleOperStatus_Type.__name__ = "Integer32"
_FsPnacModuleOperStatus_Object = MibScalar
fsPnacModuleOperStatus = _FsPnacModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 6),
    _FsPnacModuleOperStatus_Type()
)
fsPnacModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacModuleOperStatus.setStatus("current")


class _FsPnacRemoteAuthServerType_Type(RemoteAuthServerType):
    """Custom type fsPnacRemoteAuthServerType based on RemoteAuthServerType"""
    defaultValue = 1


_FsPnacRemoteAuthServerType_Type.__name__ = "RemoteAuthServerType"
_FsPnacRemoteAuthServerType_Object = MibScalar
fsPnacRemoteAuthServerType = _FsPnacRemoteAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 1, 7),
    _FsPnacRemoteAuthServerType_Type()
)
fsPnacRemoteAuthServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacRemoteAuthServerType.setStatus("current")
_FsPnacPaeAuthenticator_ObjectIdentity = ObjectIdentity
fsPnacPaeAuthenticator = _FsPnacPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2)
)
_FsPnacAuthSessionTable_Object = MibTable
fsPnacAuthSessionTable = _FsPnacAuthSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1)
)
if mibBuilder.loadTexts:
    fsPnacAuthSessionTable.setStatus("current")
_FsPnacAuthSessionEntry_Object = MibTableRow
fsPnacAuthSessionEntry = _FsPnacAuthSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1)
)
fsPnacAuthSessionEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsPnacAuthSessionSuppAddress"),
)
if mibBuilder.loadTexts:
    fsPnacAuthSessionEntry.setStatus("current")
_FsPnacAuthSessionSuppAddress_Type = MacAddress
_FsPnacAuthSessionSuppAddress_Object = MibTableColumn
fsPnacAuthSessionSuppAddress = _FsPnacAuthSessionSuppAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 1),
    _FsPnacAuthSessionSuppAddress_Type()
)
fsPnacAuthSessionSuppAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPnacAuthSessionSuppAddress.setStatus("current")
_FsPnacAuthSessionIdentifier_Type = Integer32
_FsPnacAuthSessionIdentifier_Object = MibTableColumn
fsPnacAuthSessionIdentifier = _FsPnacAuthSessionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 2),
    _FsPnacAuthSessionIdentifier_Type()
)
fsPnacAuthSessionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionIdentifier.setStatus("current")


class _FsPnacAuthSessionAuthPaeState_Type(Integer32):
    """Custom type fsPnacAuthSessionAuthPaeState based on Integer32"""
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
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_FsPnacAuthSessionAuthPaeState_Type.__name__ = "Integer32"
_FsPnacAuthSessionAuthPaeState_Object = MibTableColumn
fsPnacAuthSessionAuthPaeState = _FsPnacAuthSessionAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 3),
    _FsPnacAuthSessionAuthPaeState_Type()
)
fsPnacAuthSessionAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionAuthPaeState.setStatus("current")


class _FsPnacAuthSessionBackendAuthState_Type(Integer32):
    """Custom type fsPnacAuthSessionBackendAuthState based on Integer32"""
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
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_FsPnacAuthSessionBackendAuthState_Type.__name__ = "Integer32"
_FsPnacAuthSessionBackendAuthState_Object = MibTableColumn
fsPnacAuthSessionBackendAuthState = _FsPnacAuthSessionBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 4),
    _FsPnacAuthSessionBackendAuthState_Type()
)
fsPnacAuthSessionBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionBackendAuthState.setStatus("current")
_FsPnacAuthSessionPortStatus_Type = PaeControlledPortStatus
_FsPnacAuthSessionPortStatus_Object = MibTableColumn
fsPnacAuthSessionPortStatus = _FsPnacAuthSessionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 5),
    _FsPnacAuthSessionPortStatus_Type()
)
fsPnacAuthSessionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionPortStatus.setStatus("current")
_FsPnacAuthSessionPortNumber_Type = InterfaceIndex
_FsPnacAuthSessionPortNumber_Object = MibTableColumn
fsPnacAuthSessionPortNumber = _FsPnacAuthSessionPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 6),
    _FsPnacAuthSessionPortNumber_Type()
)
fsPnacAuthSessionPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionPortNumber.setStatus("current")
_FsPnacAuthSessionInitialize_Type = TruthValue
_FsPnacAuthSessionInitialize_Object = MibTableColumn
fsPnacAuthSessionInitialize = _FsPnacAuthSessionInitialize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 7),
    _FsPnacAuthSessionInitialize_Type()
)
fsPnacAuthSessionInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacAuthSessionInitialize.setStatus("deprecated")
_FsPnacAuthSessionReauthenticate_Type = TruthValue
_FsPnacAuthSessionReauthenticate_Object = MibTableColumn
fsPnacAuthSessionReauthenticate = _FsPnacAuthSessionReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 1, 1, 8),
    _FsPnacAuthSessionReauthenticate_Type()
)
fsPnacAuthSessionReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacAuthSessionReauthenticate.setStatus("deprecated")
_FsPnacAuthSessionStatsTable_Object = MibTable
fsPnacAuthSessionStatsTable = _FsPnacAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2)
)
if mibBuilder.loadTexts:
    fsPnacAuthSessionStatsTable.setStatus("current")
_FsPnacAuthSessionStatsEntry_Object = MibTableRow
fsPnacAuthSessionStatsEntry = _FsPnacAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1)
)
fsPnacAuthSessionStatsEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsPnacAuthSessionSuppAddress"),
)
if mibBuilder.loadTexts:
    fsPnacAuthSessionStatsEntry.setStatus("current")
_FsPnacAuthSessionOctetsRx_Type = Counter64
_FsPnacAuthSessionOctetsRx_Object = MibTableColumn
fsPnacAuthSessionOctetsRx = _FsPnacAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 1),
    _FsPnacAuthSessionOctetsRx_Type()
)
fsPnacAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionOctetsRx.setStatus("current")
_FsPnacAuthSessionOctetsTx_Type = Counter64
_FsPnacAuthSessionOctetsTx_Object = MibTableColumn
fsPnacAuthSessionOctetsTx = _FsPnacAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 2),
    _FsPnacAuthSessionOctetsTx_Type()
)
fsPnacAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionOctetsTx.setStatus("current")
_FsPnacAuthSessionFramesRx_Type = Counter32
_FsPnacAuthSessionFramesRx_Object = MibTableColumn
fsPnacAuthSessionFramesRx = _FsPnacAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 3),
    _FsPnacAuthSessionFramesRx_Type()
)
fsPnacAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionFramesRx.setStatus("current")
_FsPnacAuthSessionFramesTx_Type = Counter32
_FsPnacAuthSessionFramesTx_Object = MibTableColumn
fsPnacAuthSessionFramesTx = _FsPnacAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 4),
    _FsPnacAuthSessionFramesTx_Type()
)
fsPnacAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionFramesTx.setStatus("current")
_FsPnacAuthSessionId_Type = SnmpAdminString
_FsPnacAuthSessionId_Object = MibTableColumn
fsPnacAuthSessionId = _FsPnacAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 5),
    _FsPnacAuthSessionId_Type()
)
fsPnacAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionId.setStatus("current")


class _FsPnacAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type fsPnacAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteAuthServer", 1),
          ("localAuthServer", 2))
    )


_FsPnacAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_FsPnacAuthSessionAuthenticMethod_Object = MibTableColumn
fsPnacAuthSessionAuthenticMethod = _FsPnacAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 6),
    _FsPnacAuthSessionAuthenticMethod_Type()
)
fsPnacAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionAuthenticMethod.setStatus("current")
_FsPnacAuthSessionTime_Type = TimeTicks
_FsPnacAuthSessionTime_Object = MibTableColumn
fsPnacAuthSessionTime = _FsPnacAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 7),
    _FsPnacAuthSessionTime_Type()
)
fsPnacAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionTime.setStatus("current")


class _FsPnacAuthSessionTerminateCause_Type(Integer32):
    """Custom type fsPnacAuthSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("supplicantLogoff", 1),
          ("portFailure", 2),
          ("supplicantRestart", 3),
          ("reauthFailed", 4),
          ("authControlForceUnauth", 5),
          ("portReInit", 6),
          ("portAdminDisabled", 7),
          ("notTerminatedYet", 999))
    )


_FsPnacAuthSessionTerminateCause_Type.__name__ = "Integer32"
_FsPnacAuthSessionTerminateCause_Object = MibTableColumn
fsPnacAuthSessionTerminateCause = _FsPnacAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 8),
    _FsPnacAuthSessionTerminateCause_Type()
)
fsPnacAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionTerminateCause.setStatus("current")
_FsPnacAuthSessionUserName_Type = SnmpAdminString
_FsPnacAuthSessionUserName_Object = MibTableColumn
fsPnacAuthSessionUserName = _FsPnacAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 9),
    _FsPnacAuthSessionUserName_Type()
)
fsPnacAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacAuthSessionUserName.setStatus("current")


class _FsPnacAuthSessionStatisticsClear_Type(TruthValue):
    """Custom type fsPnacAuthSessionStatisticsClear based on TruthValue"""
    defaultValue = 2


_FsPnacAuthSessionStatisticsClear_Type.__name__ = "TruthValue"
_FsPnacAuthSessionStatisticsClear_Object = MibTableColumn
fsPnacAuthSessionStatisticsClear = _FsPnacAuthSessionStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 2, 2, 1, 10),
    _FsPnacAuthSessionStatisticsClear_Type()
)
fsPnacAuthSessionStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacAuthSessionStatisticsClear.setStatus("current")
_FsPnacAuthServer_ObjectIdentity = ObjectIdentity
fsPnacAuthServer = _FsPnacAuthServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3)
)
_FsPnacASUserConfigTable_Object = MibTable
fsPnacASUserConfigTable = _FsPnacASUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1)
)
if mibBuilder.loadTexts:
    fsPnacASUserConfigTable.setStatus("current")
_FsPnacASUserConfigEntry_Object = MibTableRow
fsPnacASUserConfigEntry = _FsPnacASUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1)
)
fsPnacASUserConfigEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsPnacASUserConfigUserName"),
)
if mibBuilder.loadTexts:
    fsPnacASUserConfigEntry.setStatus("current")


class _FsPnacASUserConfigUserName_Type(OctetString):
    """Custom type fsPnacASUserConfigUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_FsPnacASUserConfigUserName_Type.__name__ = "OctetString"
_FsPnacASUserConfigUserName_Object = MibTableColumn
fsPnacASUserConfigUserName = _FsPnacASUserConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 1),
    _FsPnacASUserConfigUserName_Type()
)
fsPnacASUserConfigUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPnacASUserConfigUserName.setStatus("current")


class _FsPnacASUserConfigPassword_Type(DisplayString):
    """Custom type fsPnacASUserConfigPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsPnacASUserConfigPassword_Type.__name__ = "DisplayString"
_FsPnacASUserConfigPassword_Object = MibTableColumn
fsPnacASUserConfigPassword = _FsPnacASUserConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 2),
    _FsPnacASUserConfigPassword_Type()
)
fsPnacASUserConfigPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacASUserConfigPassword.setStatus("current")
_FsPnacASUserConfigAuthProtocol_Type = Unsigned32
_FsPnacASUserConfigAuthProtocol_Object = MibTableColumn
fsPnacASUserConfigAuthProtocol = _FsPnacASUserConfigAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 3),
    _FsPnacASUserConfigAuthProtocol_Type()
)
fsPnacASUserConfigAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacASUserConfigAuthProtocol.setStatus("current")
_FsPnacASUserConfigAuthTimeout_Type = Unsigned32
_FsPnacASUserConfigAuthTimeout_Object = MibTableColumn
fsPnacASUserConfigAuthTimeout = _FsPnacASUserConfigAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 4),
    _FsPnacASUserConfigAuthTimeout_Type()
)
fsPnacASUserConfigAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacASUserConfigAuthTimeout.setStatus("current")
_FsPnacASUserConfigPortList_Type = PortList
_FsPnacASUserConfigPortList_Object = MibTableColumn
fsPnacASUserConfigPortList = _FsPnacASUserConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 5),
    _FsPnacASUserConfigPortList_Type()
)
fsPnacASUserConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacASUserConfigPortList.setStatus("current")
_FsPnacASUserConfigPermission_Type = PermissionType
_FsPnacASUserConfigPermission_Object = MibTableColumn
fsPnacASUserConfigPermission = _FsPnacASUserConfigPermission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 6),
    _FsPnacASUserConfigPermission_Type()
)
fsPnacASUserConfigPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPnacASUserConfigPermission.setStatus("current")
_FsPnacASUserConfigRowStatus_Type = RowStatus
_FsPnacASUserConfigRowStatus_Object = MibTableColumn
fsPnacASUserConfigRowStatus = _FsPnacASUserConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 3, 1, 1, 7),
    _FsPnacASUserConfigRowStatus_Type()
)
fsPnacASUserConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPnacASUserConfigRowStatus.setStatus("current")
_FsPnacTrapObjects_ObjectIdentity = ObjectIdentity
fsPnacTrapObjects = _FsPnacTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 4)
)
_FsPnacTrapAuthSessionTable_Object = MibTable
fsPnacTrapAuthSessionTable = _FsPnacTrapAuthSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 4, 1)
)
if mibBuilder.loadTexts:
    fsPnacTrapAuthSessionTable.setStatus("current")
_FsPnacTrapAuthSessionEntry_Object = MibTableRow
fsPnacTrapAuthSessionEntry = _FsPnacTrapAuthSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 4, 1, 1)
)
if mibBuilder.loadTexts:
    fsPnacTrapAuthSessionEntry.setStatus("current")


class _FsPnacTrapAuthSessionStatus_Type(Integer32):
    """Custom type fsPnacTrapAuthSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createFailed", 1),
          ("deleteFailed", 2),
          ("entryPresent", 3))
    )


_FsPnacTrapAuthSessionStatus_Type.__name__ = "Integer32"
_FsPnacTrapAuthSessionStatus_Object = MibTableColumn
fsPnacTrapAuthSessionStatus = _FsPnacTrapAuthSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 4, 1, 1, 1),
    _FsPnacTrapAuthSessionStatus_Type()
)
fsPnacTrapAuthSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPnacTrapAuthSessionStatus.setStatus("current")
_FsPnacNotifications_ObjectIdentity = ObjectIdentity
fsPnacNotifications = _FsPnacNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 5)
)
_FsPnacHwFailureTrap_ObjectIdentity = ObjectIdentity
fsPnacHwFailureTrap = _FsPnacHwFailureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 5, 0)
)
_FsDPnac_ObjectIdentity = ObjectIdentity
fsDPnac = _FsDPnac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6)
)


class _FsDPnacSystemStatus_Type(Integer32):
    """Custom type fsDPnacSystemStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 1),
          ("distributed", 2))
    )


_FsDPnacSystemStatus_Type.__name__ = "Integer32"
_FsDPnacSystemStatus_Object = MibScalar
fsDPnacSystemStatus = _FsDPnacSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 1),
    _FsDPnacSystemStatus_Type()
)
fsDPnacSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDPnacSystemStatus.setStatus("current")


class _FsDPnacPeriodicSyncTime_Type(Unsigned32):
    """Custom type fsDPnacPeriodicSyncTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_FsDPnacPeriodicSyncTime_Type.__name__ = "Unsigned32"
_FsDPnacPeriodicSyncTime_Object = MibScalar
fsDPnacPeriodicSyncTime = _FsDPnacPeriodicSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 2),
    _FsDPnacPeriodicSyncTime_Type()
)
fsDPnacPeriodicSyncTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDPnacPeriodicSyncTime.setStatus("current")


class _FsDPnacMaxKeepAliveCount_Type(Integer32):
    """Custom type fsDPnacMaxKeepAliveCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FsDPnacMaxKeepAliveCount_Type.__name__ = "Integer32"
_FsDPnacMaxKeepAliveCount_Object = MibScalar
fsDPnacMaxKeepAliveCount = _FsDPnacMaxKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 3),
    _FsDPnacMaxKeepAliveCount_Type()
)
fsDPnacMaxKeepAliveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDPnacMaxKeepAliveCount.setStatus("current")
_FsDPnacStatsTable_Object = MibTable
fsDPnacStatsTable = _FsDPnacStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4)
)
if mibBuilder.loadTexts:
    fsDPnacStatsTable.setStatus("current")
_FsDPnacStatsEntry_Object = MibTableRow
fsDPnacStatsEntry = _FsDPnacStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1)
)
fsDPnacStatsEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsDPnacSlotNumber"),
)
if mibBuilder.loadTexts:
    fsDPnacStatsEntry.setStatus("current")


class _FsDPnacSlotNumber_Type(Integer32):
    """Custom type fsDPnacSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsDPnacSlotNumber_Type.__name__ = "Integer32"
_FsDPnacSlotNumber_Object = MibTableColumn
fsDPnacSlotNumber = _FsDPnacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1, 1),
    _FsDPnacSlotNumber_Type()
)
fsDPnacSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDPnacSlotNumber.setStatus("current")
_FsDPnacEventUpdateFramesRx_Type = Counter32
_FsDPnacEventUpdateFramesRx_Object = MibTableColumn
fsDPnacEventUpdateFramesRx = _FsDPnacEventUpdateFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1, 2),
    _FsDPnacEventUpdateFramesRx_Type()
)
fsDPnacEventUpdateFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacEventUpdateFramesRx.setStatus("current")
_FsDPnacEventUpdateFramesTx_Type = Counter32
_FsDPnacEventUpdateFramesTx_Object = MibTableColumn
fsDPnacEventUpdateFramesTx = _FsDPnacEventUpdateFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1, 3),
    _FsDPnacEventUpdateFramesTx_Type()
)
fsDPnacEventUpdateFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacEventUpdateFramesTx.setStatus("current")
_FsDPnacPeriodicFramesTx_Type = Counter32
_FsDPnacPeriodicFramesTx_Object = MibTableColumn
fsDPnacPeriodicFramesTx = _FsDPnacPeriodicFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1, 4),
    _FsDPnacPeriodicFramesTx_Type()
)
fsDPnacPeriodicFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacPeriodicFramesTx.setStatus("current")
_FsDPnacPeriodicFramesRx_Type = Counter32
_FsDPnacPeriodicFramesRx_Object = MibTableColumn
fsDPnacPeriodicFramesRx = _FsDPnacPeriodicFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 4, 1, 5),
    _FsDPnacPeriodicFramesRx_Type()
)
fsDPnacPeriodicFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacPeriodicFramesRx.setStatus("current")
_FsDPnacSlotPortTable_Object = MibTable
fsDPnacSlotPortTable = _FsDPnacSlotPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 5)
)
if mibBuilder.loadTexts:
    fsDPnacSlotPortTable.setStatus("current")
_FsDPnacSlotPortEntry_Object = MibTableRow
fsDPnacSlotPortEntry = _FsDPnacSlotPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 5, 1)
)
fsDPnacSlotPortEntry.setIndexNames(
    (0, "ARICENT-PNAC-MIB", "fsDPnacSlotNumber"),
    (0, "ARICENT-PNAC-MIB", "fsDPnacPortIndex"),
)
if mibBuilder.loadTexts:
    fsDPnacSlotPortEntry.setStatus("current")
_FsDPnacPortIndex_Type = InterfaceIndex
_FsDPnacPortIndex_Object = MibTableColumn
fsDPnacPortIndex = _FsDPnacPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 5, 1, 1),
    _FsDPnacPortIndex_Type()
)
fsDPnacPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDPnacPortIndex.setStatus("current")
_FsDPnacPortAuthStatus_Type = PaeControlledPortStatus
_FsDPnacPortAuthStatus_Object = MibTableColumn
fsDPnacPortAuthStatus = _FsDPnacPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 5, 1, 2),
    _FsDPnacPortAuthStatus_Type()
)
fsDPnacPortAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacPortAuthStatus.setStatus("current")


class _FsDPnacPortControlledDirection_Type(Integer32):
    """Custom type fsDPnacPortControlledDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )


_FsDPnacPortControlledDirection_Type.__name__ = "Integer32"
_FsDPnacPortControlledDirection_Object = MibTableColumn
fsDPnacPortControlledDirection = _FsDPnacPortControlledDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 64, 6, 5, 1, 3),
    _FsDPnacPortControlledDirection_Type()
)
fsDPnacPortControlledDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDPnacPortControlledDirection.setStatus("current")
fsPnacAuthSessionEntry.registerAugmentions(
    ("ARICENT-PNAC-MIB",
     "fsPnacTrapAuthSessionEntry")
)
fsPnacTrapAuthSessionEntry.setIndexNames(*fsPnacAuthSessionEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsPnacPortBasedHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 64, 5, 0, 1)
)
fsPnacPortBasedHwFailureTrap.setObjects(
      *(("ARICENT-PNAC-MIB", "fsPnacPaePortStatus"),
        ("IEEE8021-PAE-MIB", "dot1xAuthOperControlledDirections"))
)
if mibBuilder.loadTexts:
    fsPnacPortBasedHwFailureTrap.setStatus(
        "current"
    )

fsPnacMacBasedHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 64, 5, 0, 2)
)
fsPnacMacBasedHwFailureTrap.setObjects(
      *(("ARICENT-PNAC-MIB", "fsPnacAuthSessionPortNumber"),
        ("ARICENT-PNAC-MIB", "fsPnacAuthSessionPortStatus"),
        ("ARICENT-PNAC-MIB", "fsPnacTrapAuthSessionStatus"))
)
if mibBuilder.loadTexts:
    fsPnacMacBasedHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-PNAC-MIB",
    **{"AuthenticMethod": AuthenticMethod,
       "RemoteAuthServerType": RemoteAuthServerType,
       "PermissionType": PermissionType,
       "fspnac": fspnac,
       "fsPnacPaeSystem": fsPnacPaeSystem,
       "fsPnacSystemControl": fsPnacSystemControl,
       "fsPnacTraceOption": fsPnacTraceOption,
       "fsPnacAuthenticServer": fsPnacAuthenticServer,
       "fsPnacNasId": fsPnacNasId,
       "fsPnacPaePortTable": fsPnacPaePortTable,
       "fsPnacPaePortEntry": fsPnacPaePortEntry,
       "fsPnacPaePortNumber": fsPnacPaePortNumber,
       "fsPnacPaePortAuthMode": fsPnacPaePortAuthMode,
       "fsPnacPaePortSupplicantCount": fsPnacPaePortSupplicantCount,
       "fsPnacPaePortUserName": fsPnacPaePortUserName,
       "fsPnacPaePortPassword": fsPnacPaePortPassword,
       "fsPnacPaePortStatus": fsPnacPaePortStatus,
       "fsPnacPaePortStatisticsClear": fsPnacPaePortStatisticsClear,
       "fsPnacPaePortAuthStatus": fsPnacPaePortAuthStatus,
       "fsPnacPaeAuthReAuthMax": fsPnacPaeAuthReAuthMax,
       "fsPnacModuleOperStatus": fsPnacModuleOperStatus,
       "fsPnacRemoteAuthServerType": fsPnacRemoteAuthServerType,
       "fsPnacPaeAuthenticator": fsPnacPaeAuthenticator,
       "fsPnacAuthSessionTable": fsPnacAuthSessionTable,
       "fsPnacAuthSessionEntry": fsPnacAuthSessionEntry,
       "fsPnacAuthSessionSuppAddress": fsPnacAuthSessionSuppAddress,
       "fsPnacAuthSessionIdentifier": fsPnacAuthSessionIdentifier,
       "fsPnacAuthSessionAuthPaeState": fsPnacAuthSessionAuthPaeState,
       "fsPnacAuthSessionBackendAuthState": fsPnacAuthSessionBackendAuthState,
       "fsPnacAuthSessionPortStatus": fsPnacAuthSessionPortStatus,
       "fsPnacAuthSessionPortNumber": fsPnacAuthSessionPortNumber,
       "fsPnacAuthSessionInitialize": fsPnacAuthSessionInitialize,
       "fsPnacAuthSessionReauthenticate": fsPnacAuthSessionReauthenticate,
       "fsPnacAuthSessionStatsTable": fsPnacAuthSessionStatsTable,
       "fsPnacAuthSessionStatsEntry": fsPnacAuthSessionStatsEntry,
       "fsPnacAuthSessionOctetsRx": fsPnacAuthSessionOctetsRx,
       "fsPnacAuthSessionOctetsTx": fsPnacAuthSessionOctetsTx,
       "fsPnacAuthSessionFramesRx": fsPnacAuthSessionFramesRx,
       "fsPnacAuthSessionFramesTx": fsPnacAuthSessionFramesTx,
       "fsPnacAuthSessionId": fsPnacAuthSessionId,
       "fsPnacAuthSessionAuthenticMethod": fsPnacAuthSessionAuthenticMethod,
       "fsPnacAuthSessionTime": fsPnacAuthSessionTime,
       "fsPnacAuthSessionTerminateCause": fsPnacAuthSessionTerminateCause,
       "fsPnacAuthSessionUserName": fsPnacAuthSessionUserName,
       "fsPnacAuthSessionStatisticsClear": fsPnacAuthSessionStatisticsClear,
       "fsPnacAuthServer": fsPnacAuthServer,
       "fsPnacASUserConfigTable": fsPnacASUserConfigTable,
       "fsPnacASUserConfigEntry": fsPnacASUserConfigEntry,
       "fsPnacASUserConfigUserName": fsPnacASUserConfigUserName,
       "fsPnacASUserConfigPassword": fsPnacASUserConfigPassword,
       "fsPnacASUserConfigAuthProtocol": fsPnacASUserConfigAuthProtocol,
       "fsPnacASUserConfigAuthTimeout": fsPnacASUserConfigAuthTimeout,
       "fsPnacASUserConfigPortList": fsPnacASUserConfigPortList,
       "fsPnacASUserConfigPermission": fsPnacASUserConfigPermission,
       "fsPnacASUserConfigRowStatus": fsPnacASUserConfigRowStatus,
       "fsPnacTrapObjects": fsPnacTrapObjects,
       "fsPnacTrapAuthSessionTable": fsPnacTrapAuthSessionTable,
       "fsPnacTrapAuthSessionEntry": fsPnacTrapAuthSessionEntry,
       "fsPnacTrapAuthSessionStatus": fsPnacTrapAuthSessionStatus,
       "fsPnacNotifications": fsPnacNotifications,
       "fsPnacHwFailureTrap": fsPnacHwFailureTrap,
       "fsPnacPortBasedHwFailureTrap": fsPnacPortBasedHwFailureTrap,
       "fsPnacMacBasedHwFailureTrap": fsPnacMacBasedHwFailureTrap,
       "fsDPnac": fsDPnac,
       "fsDPnacSystemStatus": fsDPnacSystemStatus,
       "fsDPnacPeriodicSyncTime": fsDPnacPeriodicSyncTime,
       "fsDPnacMaxKeepAliveCount": fsDPnacMaxKeepAliveCount,
       "fsDPnacStatsTable": fsDPnacStatsTable,
       "fsDPnacStatsEntry": fsDPnacStatsEntry,
       "fsDPnacSlotNumber": fsDPnacSlotNumber,
       "fsDPnacEventUpdateFramesRx": fsDPnacEventUpdateFramesRx,
       "fsDPnacEventUpdateFramesTx": fsDPnacEventUpdateFramesTx,
       "fsDPnacPeriodicFramesTx": fsDPnacPeriodicFramesTx,
       "fsDPnacPeriodicFramesRx": fsDPnacPeriodicFramesRx,
       "fsDPnacSlotPortTable": fsDPnacSlotPortTable,
       "fsDPnacSlotPortEntry": fsDPnacSlotPortEntry,
       "fsDPnacPortIndex": fsDPnacPortIndex,
       "fsDPnacPortAuthStatus": fsDPnacPortAuthStatus,
       "fsDPnacPortControlledDirection": fsDPnacPortControlledDirection}
)
