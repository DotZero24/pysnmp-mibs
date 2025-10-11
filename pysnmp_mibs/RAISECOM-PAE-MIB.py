# SNMP MIB module (RAISECOM-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-PAE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:31 2025
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

(PaeControlledDirections,
 PaeControlledPortControl,
 PaeControlledPortStatus,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledDirections",
    "PaeControlledPortControl",
    "PaeControlledPortStatus",
    "dot1xPaePortNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raisecomDot1x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomDot1xObjects_ObjectIdentity = ObjectIdentity
raisecomDot1xObjects = _RaisecomDot1xObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1)
)
_RaisecomDot1xSystem_ObjectIdentity = ObjectIdentity
raisecomDot1xSystem = _RaisecomDot1xSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1)
)


class _RaisecomDot1xPaeSystemAuthControl_Type(Integer32):
    """Custom type raisecomDot1xPaeSystemAuthControl based on Integer32"""
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


_RaisecomDot1xPaeSystemAuthControl_Type.__name__ = "Integer32"
_RaisecomDot1xPaeSystemAuthControl_Object = MibScalar
raisecomDot1xPaeSystemAuthControl = _RaisecomDot1xPaeSystemAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 1),
    _RaisecomDot1xPaeSystemAuthControl_Type()
)
raisecomDot1xPaeSystemAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xPaeSystemAuthControl.setStatus("current")
_RaisecomDot1xPaePortTable_Object = MibTable
raisecomDot1xPaePortTable = _RaisecomDot1xPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomDot1xPaePortTable.setStatus("current")
_RaisecomDot1xPaePortEntry_Object = MibTableRow
raisecomDot1xPaePortEntry = _RaisecomDot1xPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2, 1)
)
raisecomDot1xPaePortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    raisecomDot1xPaePortEntry.setStatus("current")
_RaisecomDot1xPaePortProtocolVersion_Type = Unsigned32
_RaisecomDot1xPaePortProtocolVersion_Object = MibTableColumn
raisecomDot1xPaePortProtocolVersion = _RaisecomDot1xPaePortProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2, 1, 1),
    _RaisecomDot1xPaePortProtocolVersion_Type()
)
raisecomDot1xPaePortProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xPaePortProtocolVersion.setStatus("current")


class _RaisecomDot1xPaePortCapabilities_Type(Bits):
    """Custom type raisecomDot1xPaePortCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dot1xPaePortAuthCapable", 0),
          ("dot1xPaePortSuppCapable", 1))
    )

_RaisecomDot1xPaePortCapabilities_Type.__name__ = "Bits"
_RaisecomDot1xPaePortCapabilities_Object = MibTableColumn
raisecomDot1xPaePortCapabilities = _RaisecomDot1xPaePortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2, 1, 2),
    _RaisecomDot1xPaePortCapabilities_Type()
)
raisecomDot1xPaePortCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xPaePortCapabilities.setStatus("current")
_RaisecomDot1xPaePortInitialize_Type = TruthValue
_RaisecomDot1xPaePortInitialize_Object = MibTableColumn
raisecomDot1xPaePortInitialize = _RaisecomDot1xPaePortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2, 1, 3),
    _RaisecomDot1xPaePortInitialize_Type()
)
raisecomDot1xPaePortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xPaePortInitialize.setStatus("current")
_RaisecomDot1xPaePortReauthenticate_Type = TruthValue
_RaisecomDot1xPaePortReauthenticate_Object = MibTableColumn
raisecomDot1xPaePortReauthenticate = _RaisecomDot1xPaePortReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 1, 2, 1, 4),
    _RaisecomDot1xPaePortReauthenticate_Type()
)
raisecomDot1xPaePortReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xPaePortReauthenticate.setStatus("current")
_RaisecomDot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
raisecomDot1xPaeAuthenticator = _RaisecomDot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2)
)
_RaisecomDot1xAuthConfigTable_Object = MibTable
raisecomDot1xAuthConfigTable = _RaisecomDot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomDot1xAuthConfigTable.setStatus("current")
_RaisecomDot1xAuthConfigEntry_Object = MibTableRow
raisecomDot1xAuthConfigEntry = _RaisecomDot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1)
)
raisecomDot1xAuthConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    raisecomDot1xAuthConfigEntry.setStatus("current")


class _RaisecomDot1xAuthPaeState_Type(Integer32):
    """Custom type raisecomDot1xAuthPaeState based on Integer32"""
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
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("restart", 10))
    )


_RaisecomDot1xAuthPaeState_Type.__name__ = "Integer32"
_RaisecomDot1xAuthPaeState_Object = MibTableColumn
raisecomDot1xAuthPaeState = _RaisecomDot1xAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 1),
    _RaisecomDot1xAuthPaeState_Type()
)
raisecomDot1xAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthPaeState.setStatus("current")


class _RaisecomDot1xAuthBackendAuthState_Type(Integer32):
    """Custom type raisecomDot1xAuthBackendAuthState based on Integer32"""
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
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7),
          ("ignore", 8))
    )


_RaisecomDot1xAuthBackendAuthState_Type.__name__ = "Integer32"
_RaisecomDot1xAuthBackendAuthState_Object = MibTableColumn
raisecomDot1xAuthBackendAuthState = _RaisecomDot1xAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 2),
    _RaisecomDot1xAuthBackendAuthState_Type()
)
raisecomDot1xAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthBackendAuthState.setStatus("current")
_RaisecomDot1xAuthAdminControlledDirections_Type = PaeControlledDirections
_RaisecomDot1xAuthAdminControlledDirections_Object = MibTableColumn
raisecomDot1xAuthAdminControlledDirections = _RaisecomDot1xAuthAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 3),
    _RaisecomDot1xAuthAdminControlledDirections_Type()
)
raisecomDot1xAuthAdminControlledDirections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthAdminControlledDirections.setStatus("current")
_RaisecomDot1xAuthOperControlledDirections_Type = PaeControlledDirections
_RaisecomDot1xAuthOperControlledDirections_Object = MibTableColumn
raisecomDot1xAuthOperControlledDirections = _RaisecomDot1xAuthOperControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 4),
    _RaisecomDot1xAuthOperControlledDirections_Type()
)
raisecomDot1xAuthOperControlledDirections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthOperControlledDirections.setStatus("current")
_RaisecomDot1xAuthAuthControlledPortStatus_Type = PaeControlledPortStatus
_RaisecomDot1xAuthAuthControlledPortStatus_Object = MibTableColumn
raisecomDot1xAuthAuthControlledPortStatus = _RaisecomDot1xAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 5),
    _RaisecomDot1xAuthAuthControlledPortStatus_Type()
)
raisecomDot1xAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthAuthControlledPortStatus.setStatus("current")
_RaisecomDot1xAuthAuthControlledPortControl_Type = PaeControlledPortControl
_RaisecomDot1xAuthAuthControlledPortControl_Object = MibTableColumn
raisecomDot1xAuthAuthControlledPortControl = _RaisecomDot1xAuthAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 6),
    _RaisecomDot1xAuthAuthControlledPortControl_Type()
)
raisecomDot1xAuthAuthControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthAuthControlledPortControl.setStatus("current")


class _RaisecomDot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type raisecomDot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60


_RaisecomDot1xAuthQuietPeriod_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthQuietPeriod_Object = MibTableColumn
raisecomDot1xAuthQuietPeriod = _RaisecomDot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 7),
    _RaisecomDot1xAuthQuietPeriod_Type()
)
raisecomDot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthQuietPeriod.setStatus("current")


class _RaisecomDot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type raisecomDot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30


_RaisecomDot1xAuthTxPeriod_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthTxPeriod_Object = MibTableColumn
raisecomDot1xAuthTxPeriod = _RaisecomDot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 8),
    _RaisecomDot1xAuthTxPeriod_Type()
)
raisecomDot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthTxPeriod.setStatus("deprecated")


class _RaisecomDot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type raisecomDot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 30


_RaisecomDot1xAuthSuppTimeout_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthSuppTimeout_Object = MibTableColumn
raisecomDot1xAuthSuppTimeout = _RaisecomDot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 9),
    _RaisecomDot1xAuthSuppTimeout_Type()
)
raisecomDot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthSuppTimeout.setStatus("deprecated")


class _RaisecomDot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type raisecomDot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 30


_RaisecomDot1xAuthServerTimeout_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthServerTimeout_Object = MibTableColumn
raisecomDot1xAuthServerTimeout = _RaisecomDot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 10),
    _RaisecomDot1xAuthServerTimeout_Type()
)
raisecomDot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthServerTimeout.setStatus("current")


class _RaisecomDot1xAuthMaxReq_Type(Unsigned32):
    """Custom type raisecomDot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2


_RaisecomDot1xAuthMaxReq_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthMaxReq_Object = MibTableColumn
raisecomDot1xAuthMaxReq = _RaisecomDot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 11),
    _RaisecomDot1xAuthMaxReq_Type()
)
raisecomDot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthMaxReq.setStatus("deprecated")


class _RaisecomDot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type raisecomDot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_RaisecomDot1xAuthReAuthPeriod_Type.__name__ = "Unsigned32"
_RaisecomDot1xAuthReAuthPeriod_Object = MibTableColumn
raisecomDot1xAuthReAuthPeriod = _RaisecomDot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 12),
    _RaisecomDot1xAuthReAuthPeriod_Type()
)
raisecomDot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthReAuthPeriod.setStatus("current")


class _RaisecomDot1xAuthReAuthEnabled_Type(TruthValue):
    """Custom type raisecomDot1xAuthReAuthEnabled based on TruthValue"""
    defaultValue = 2


_RaisecomDot1xAuthReAuthEnabled_Type.__name__ = "TruthValue"
_RaisecomDot1xAuthReAuthEnabled_Object = MibTableColumn
raisecomDot1xAuthReAuthEnabled = _RaisecomDot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 13),
    _RaisecomDot1xAuthReAuthEnabled_Type()
)
raisecomDot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthReAuthEnabled.setStatus("current")
_RaisecomDot1xAuthKeyTxEnabled_Type = TruthValue
_RaisecomDot1xAuthKeyTxEnabled_Object = MibTableColumn
raisecomDot1xAuthKeyTxEnabled = _RaisecomDot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 1, 1, 14),
    _RaisecomDot1xAuthKeyTxEnabled_Type()
)
raisecomDot1xAuthKeyTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomDot1xAuthKeyTxEnabled.setStatus("current")
_RaisecomDot1xAuthStatsTable_Object = MibTable
raisecomDot1xAuthStatsTable = _RaisecomDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomDot1xAuthStatsTable.setStatus("current")
_RaisecomDot1xAuthStatsEntry_Object = MibTableRow
raisecomDot1xAuthStatsEntry = _RaisecomDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1)
)
raisecomDot1xAuthStatsEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    raisecomDot1xAuthStatsEntry.setStatus("current")
_RaisecomDot1xAuthEapolFramesRx_Type = Counter32
_RaisecomDot1xAuthEapolFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapolFramesRx = _RaisecomDot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 1),
    _RaisecomDot1xAuthEapolFramesRx_Type()
)
raisecomDot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolFramesRx.setStatus("current")
_RaisecomDot1xAuthEapolFramesTx_Type = Counter32
_RaisecomDot1xAuthEapolFramesTx_Object = MibTableColumn
raisecomDot1xAuthEapolFramesTx = _RaisecomDot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 2),
    _RaisecomDot1xAuthEapolFramesTx_Type()
)
raisecomDot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolFramesTx.setStatus("current")
_RaisecomDot1xAuthEapolStartFramesRx_Type = Counter32
_RaisecomDot1xAuthEapolStartFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapolStartFramesRx = _RaisecomDot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 3),
    _RaisecomDot1xAuthEapolStartFramesRx_Type()
)
raisecomDot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolStartFramesRx.setStatus("current")
_RaisecomDot1xAuthEapolLogoffFramesRx_Type = Counter32
_RaisecomDot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapolLogoffFramesRx = _RaisecomDot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 4),
    _RaisecomDot1xAuthEapolLogoffFramesRx_Type()
)
raisecomDot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolLogoffFramesRx.setStatus("current")
_RaisecomDot1xAuthEapolRespIdFramesRx_Type = Counter32
_RaisecomDot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapolRespIdFramesRx = _RaisecomDot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 5),
    _RaisecomDot1xAuthEapolRespIdFramesRx_Type()
)
raisecomDot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolRespIdFramesRx.setStatus("current")
_RaisecomDot1xAuthEapolRespFramesRx_Type = Counter32
_RaisecomDot1xAuthEapolRespFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapolRespFramesRx = _RaisecomDot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 6),
    _RaisecomDot1xAuthEapolRespFramesRx_Type()
)
raisecomDot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolRespFramesRx.setStatus("current")
_RaisecomDot1xAuthEapolReqIdFramesTx_Type = Counter32
_RaisecomDot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
raisecomDot1xAuthEapolReqIdFramesTx = _RaisecomDot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 7),
    _RaisecomDot1xAuthEapolReqIdFramesTx_Type()
)
raisecomDot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolReqIdFramesTx.setStatus("current")
_RaisecomDot1xAuthEapolReqFramesTx_Type = Counter32
_RaisecomDot1xAuthEapolReqFramesTx_Object = MibTableColumn
raisecomDot1xAuthEapolReqFramesTx = _RaisecomDot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 8),
    _RaisecomDot1xAuthEapolReqFramesTx_Type()
)
raisecomDot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapolReqFramesTx.setStatus("current")
_RaisecomDot1xAuthInvalidEapolFramesRx_Type = Counter32
_RaisecomDot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
raisecomDot1xAuthInvalidEapolFramesRx = _RaisecomDot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 9),
    _RaisecomDot1xAuthInvalidEapolFramesRx_Type()
)
raisecomDot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthInvalidEapolFramesRx.setStatus("current")
_RaisecomDot1xAuthEapLengthErrorFramesRx_Type = Counter32
_RaisecomDot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
raisecomDot1xAuthEapLengthErrorFramesRx = _RaisecomDot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 10),
    _RaisecomDot1xAuthEapLengthErrorFramesRx_Type()
)
raisecomDot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthEapLengthErrorFramesRx.setStatus("current")
_RaisecomDot1xAuthLastEapolFrameVersion_Type = Unsigned32
_RaisecomDot1xAuthLastEapolFrameVersion_Object = MibTableColumn
raisecomDot1xAuthLastEapolFrameVersion = _RaisecomDot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 11),
    _RaisecomDot1xAuthLastEapolFrameVersion_Type()
)
raisecomDot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthLastEapolFrameVersion.setStatus("current")
_RaisecomDot1xAuthLastEapolFrameSource_Type = MacAddress
_RaisecomDot1xAuthLastEapolFrameSource_Object = MibTableColumn
raisecomDot1xAuthLastEapolFrameSource = _RaisecomDot1xAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 16, 1, 2, 2, 1, 12),
    _RaisecomDot1xAuthLastEapolFrameSource_Type()
)
raisecomDot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDot1xAuthLastEapolFrameSource.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-PAE-MIB",
    **{"raisecomDot1x": raisecomDot1x,
       "raisecomDot1xObjects": raisecomDot1xObjects,
       "raisecomDot1xSystem": raisecomDot1xSystem,
       "raisecomDot1xPaeSystemAuthControl": raisecomDot1xPaeSystemAuthControl,
       "raisecomDot1xPaePortTable": raisecomDot1xPaePortTable,
       "raisecomDot1xPaePortEntry": raisecomDot1xPaePortEntry,
       "raisecomDot1xPaePortProtocolVersion": raisecomDot1xPaePortProtocolVersion,
       "raisecomDot1xPaePortCapabilities": raisecomDot1xPaePortCapabilities,
       "raisecomDot1xPaePortInitialize": raisecomDot1xPaePortInitialize,
       "raisecomDot1xPaePortReauthenticate": raisecomDot1xPaePortReauthenticate,
       "raisecomDot1xPaeAuthenticator": raisecomDot1xPaeAuthenticator,
       "raisecomDot1xAuthConfigTable": raisecomDot1xAuthConfigTable,
       "raisecomDot1xAuthConfigEntry": raisecomDot1xAuthConfigEntry,
       "raisecomDot1xAuthPaeState": raisecomDot1xAuthPaeState,
       "raisecomDot1xAuthBackendAuthState": raisecomDot1xAuthBackendAuthState,
       "raisecomDot1xAuthAdminControlledDirections": raisecomDot1xAuthAdminControlledDirections,
       "raisecomDot1xAuthOperControlledDirections": raisecomDot1xAuthOperControlledDirections,
       "raisecomDot1xAuthAuthControlledPortStatus": raisecomDot1xAuthAuthControlledPortStatus,
       "raisecomDot1xAuthAuthControlledPortControl": raisecomDot1xAuthAuthControlledPortControl,
       "raisecomDot1xAuthQuietPeriod": raisecomDot1xAuthQuietPeriod,
       "raisecomDot1xAuthTxPeriod": raisecomDot1xAuthTxPeriod,
       "raisecomDot1xAuthSuppTimeout": raisecomDot1xAuthSuppTimeout,
       "raisecomDot1xAuthServerTimeout": raisecomDot1xAuthServerTimeout,
       "raisecomDot1xAuthMaxReq": raisecomDot1xAuthMaxReq,
       "raisecomDot1xAuthReAuthPeriod": raisecomDot1xAuthReAuthPeriod,
       "raisecomDot1xAuthReAuthEnabled": raisecomDot1xAuthReAuthEnabled,
       "raisecomDot1xAuthKeyTxEnabled": raisecomDot1xAuthKeyTxEnabled,
       "raisecomDot1xAuthStatsTable": raisecomDot1xAuthStatsTable,
       "raisecomDot1xAuthStatsEntry": raisecomDot1xAuthStatsEntry,
       "raisecomDot1xAuthEapolFramesRx": raisecomDot1xAuthEapolFramesRx,
       "raisecomDot1xAuthEapolFramesTx": raisecomDot1xAuthEapolFramesTx,
       "raisecomDot1xAuthEapolStartFramesRx": raisecomDot1xAuthEapolStartFramesRx,
       "raisecomDot1xAuthEapolLogoffFramesRx": raisecomDot1xAuthEapolLogoffFramesRx,
       "raisecomDot1xAuthEapolRespIdFramesRx": raisecomDot1xAuthEapolRespIdFramesRx,
       "raisecomDot1xAuthEapolRespFramesRx": raisecomDot1xAuthEapolRespFramesRx,
       "raisecomDot1xAuthEapolReqIdFramesTx": raisecomDot1xAuthEapolReqIdFramesTx,
       "raisecomDot1xAuthEapolReqFramesTx": raisecomDot1xAuthEapolReqFramesTx,
       "raisecomDot1xAuthInvalidEapolFramesRx": raisecomDot1xAuthInvalidEapolFramesRx,
       "raisecomDot1xAuthEapLengthErrorFramesRx": raisecomDot1xAuthEapLengthErrorFramesRx,
       "raisecomDot1xAuthLastEapolFrameVersion": raisecomDot1xAuthLastEapolFrameVersion,
       "raisecomDot1xAuthLastEapolFrameSource": raisecomDot1xAuthLastEapolFrameSource}
)
