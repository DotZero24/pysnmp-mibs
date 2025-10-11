# SNMP MIB module (FS-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-AAA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:22 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(radiusAccClientServerPortNumber,
 radiusAccServerAddress) = mibBuilder.importSymbols(
    "RADIUS-ACC-CLIENT-MIB",
    "radiusAccClientServerPortNumber",
    "radiusAccServerAddress")

(radiusAuthClientServerPortNumber,
 radiusAuthServerAddress) = mibBuilder.importSymbols(
    "RADIUS-AUTH-CLIENT-MIB",
    "radiusAuthClientServerPortNumber",
    "radiusAuthServerAddress")

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

fsAAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19)
)
if mibBuilder.loadTexts:
    fsAAAMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRadiusServerTrap_ObjectIdentity = ObjectIdentity
fsRadiusServerTrap = _FsRadiusServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 0)
)
_FsAAAMIBObjects_ObjectIdentity = ObjectIdentity
fsAAAMIBObjects = _FsAAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1)
)
_FsDot1xAuthObjects_ObjectIdentity = ObjectIdentity
fsDot1xAuthObjects = _FsDot1xAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1)
)


class _FsDot1xAuthStatus_Type(EnabledStatus):
    """Custom type fsDot1xAuthStatus based on EnabledStatus"""
    defaultValue = 2


_FsDot1xAuthStatus_Type.__name__ = "EnabledStatus"
_FsDot1xAuthStatus_Object = MibScalar
fsDot1xAuthStatus = _FsDot1xAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 1),
    _FsDot1xAuthStatus_Type()
)
fsDot1xAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthStatus.setStatus("current")


class _FsDot1xAuthObjectsQuietPeriod_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsQuietPeriod based on Unsigned32"""
    defaultValue = 60


_FsDot1xAuthObjectsQuietPeriod_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsQuietPeriod_Object = MibScalar
fsDot1xAuthObjectsQuietPeriod = _FsDot1xAuthObjectsQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 2),
    _FsDot1xAuthObjectsQuietPeriod_Type()
)
fsDot1xAuthObjectsQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsQuietPeriod.setStatus("current")


class _FsDot1xAuthObjectsTxPeriod_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsTxPeriod based on Unsigned32"""
    defaultValue = 30


_FsDot1xAuthObjectsTxPeriod_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsTxPeriod_Object = MibScalar
fsDot1xAuthObjectsTxPeriod = _FsDot1xAuthObjectsTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 3),
    _FsDot1xAuthObjectsTxPeriod_Type()
)
fsDot1xAuthObjectsTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsTxPeriod.setStatus("current")


class _FsDot1xAuthObjectsSuppTimeout_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsSuppTimeout based on Unsigned32"""
    defaultValue = 30


_FsDot1xAuthObjectsSuppTimeout_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsSuppTimeout_Object = MibScalar
fsDot1xAuthObjectsSuppTimeout = _FsDot1xAuthObjectsSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 4),
    _FsDot1xAuthObjectsSuppTimeout_Type()
)
fsDot1xAuthObjectsSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsSuppTimeout.setStatus("current")


class _FsDot1xAuthObjectsServerTimeout_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsServerTimeout based on Unsigned32"""
    defaultValue = 30


_FsDot1xAuthObjectsServerTimeout_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsServerTimeout_Object = MibScalar
fsDot1xAuthObjectsServerTimeout = _FsDot1xAuthObjectsServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 5),
    _FsDot1xAuthObjectsServerTimeout_Type()
)
fsDot1xAuthObjectsServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsServerTimeout.setStatus("current")


class _FsDot1xAuthObjectsMaxReq_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsMaxReq based on Unsigned32"""
    defaultValue = 2


_FsDot1xAuthObjectsMaxReq_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsMaxReq_Object = MibScalar
fsDot1xAuthObjectsMaxReq = _FsDot1xAuthObjectsMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 6),
    _FsDot1xAuthObjectsMaxReq_Type()
)
fsDot1xAuthObjectsMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsMaxReq.setStatus("current")


class _FsDot1xAuthObjectsReAuthPeriod_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsReAuthPeriod based on Unsigned32"""
    defaultValue = 3600


_FsDot1xAuthObjectsReAuthPeriod_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsReAuthPeriod_Object = MibScalar
fsDot1xAuthObjectsReAuthPeriod = _FsDot1xAuthObjectsReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 7),
    _FsDot1xAuthObjectsReAuthPeriod_Type()
)
fsDot1xAuthObjectsReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsReAuthPeriod.setStatus("current")


class _FsDot1xAuthObjectsMaxReauth_Type(Unsigned32):
    """Custom type fsDot1xAuthObjectsMaxReauth based on Unsigned32"""
    defaultValue = 2


_FsDot1xAuthObjectsMaxReauth_Type.__name__ = "Unsigned32"
_FsDot1xAuthObjectsMaxReauth_Object = MibScalar
fsDot1xAuthObjectsMaxReauth = _FsDot1xAuthObjectsMaxReauth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 8),
    _FsDot1xAuthObjectsMaxReauth_Type()
)
fsDot1xAuthObjectsMaxReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsMaxReauth.setStatus("current")


class _FsDot1xAuthObjectsReAuthEnable_Type(EnabledStatus):
    """Custom type fsDot1xAuthObjectsReAuthEnable based on EnabledStatus"""
    defaultValue = 2


_FsDot1xAuthObjectsReAuthEnable_Type.__name__ = "EnabledStatus"
_FsDot1xAuthObjectsReAuthEnable_Object = MibScalar
fsDot1xAuthObjectsReAuthEnable = _FsDot1xAuthObjectsReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 9),
    _FsDot1xAuthObjectsReAuthEnable_Type()
)
fsDot1xAuthObjectsReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsReAuthEnable.setStatus("current")
_FsDot1xAuthObjectsConfigTable_Object = MibTable
fsDot1xAuthObjectsConfigTable = _FsDot1xAuthObjectsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10)
)
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsConfigTable.setStatus("current")
_FsDot1xAuthObjectsConfigEntry_Object = MibTableRow
fsDot1xAuthObjectsConfigEntry = _FsDot1xAuthObjectsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1)
)
fsDot1xAuthObjectsConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsDot1xAuthObjectsConfigFdbId"),
    (0, "FS-AAA-MIB", "fsDot1xAuthObjectsConfigAddr"),
)
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsConfigEntry.setStatus("current")
_FsDot1xAuthObjectsConfigFdbId_Type = Unsigned32
_FsDot1xAuthObjectsConfigFdbId_Object = MibTableColumn
fsDot1xAuthObjectsConfigFdbId = _FsDot1xAuthObjectsConfigFdbId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 1),
    _FsDot1xAuthObjectsConfigFdbId_Type()
)
fsDot1xAuthObjectsConfigFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsConfigFdbId.setStatus("current")
_FsDot1xAuthObjectsConfigAddr_Type = MacAddress
_FsDot1xAuthObjectsConfigAddr_Object = MibTableColumn
fsDot1xAuthObjectsConfigAddr = _FsDot1xAuthObjectsConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 2),
    _FsDot1xAuthObjectsConfigAddr_Type()
)
fsDot1xAuthObjectsConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsConfigAddr.setStatus("current")


class _FsDot1xAuthObjectsPaeState_Type(Integer32):
    """Custom type fsDot1xAuthObjectsPaeState based on Integer32"""
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


_FsDot1xAuthObjectsPaeState_Type.__name__ = "Integer32"
_FsDot1xAuthObjectsPaeState_Object = MibTableColumn
fsDot1xAuthObjectsPaeState = _FsDot1xAuthObjectsPaeState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 3),
    _FsDot1xAuthObjectsPaeState_Type()
)
fsDot1xAuthObjectsPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsPaeState.setStatus("current")


class _FsDot1xAuthObjectsBackendAuthState_Type(Integer32):
    """Custom type fsDot1xAuthObjectsBackendAuthState based on Integer32"""
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


_FsDot1xAuthObjectsBackendAuthState_Type.__name__ = "Integer32"
_FsDot1xAuthObjectsBackendAuthState_Object = MibTableColumn
fsDot1xAuthObjectsBackendAuthState = _FsDot1xAuthObjectsBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 4),
    _FsDot1xAuthObjectsBackendAuthState_Type()
)
fsDot1xAuthObjectsBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsBackendAuthState.setStatus("current")


class _FsDot1xAuthObjectsAuthControlledPortStatus_Type(Integer32):
    """Custom type fsDot1xAuthObjectsAuthControlledPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_FsDot1xAuthObjectsAuthControlledPortStatus_Type.__name__ = "Integer32"
_FsDot1xAuthObjectsAuthControlledPortStatus_Object = MibTableColumn
fsDot1xAuthObjectsAuthControlledPortStatus = _FsDot1xAuthObjectsAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 5),
    _FsDot1xAuthObjectsAuthControlledPortStatus_Type()
)
fsDot1xAuthObjectsAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsAuthControlledPortStatus.setStatus("current")
_FsDot1xAuthObjectsKeyTxEnabled_Type = TruthValue
_FsDot1xAuthObjectsKeyTxEnabled_Object = MibTableColumn
fsDot1xAuthObjectsKeyTxEnabled = _FsDot1xAuthObjectsKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 6),
    _FsDot1xAuthObjectsKeyTxEnabled_Type()
)
fsDot1xAuthObjectsKeyTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsKeyTxEnabled.setStatus("current")
_FsDot1xAuthObjectsIfIndex_Type = IfIndex
_FsDot1xAuthObjectsIfIndex_Object = MibTableColumn
fsDot1xAuthObjectsIfIndex = _FsDot1xAuthObjectsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 10, 1, 7),
    _FsDot1xAuthObjectsIfIndex_Type()
)
fsDot1xAuthObjectsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsIfIndex.setStatus("current")
_FsDot1xAuthObjectsStatsTable_Object = MibTable
fsDot1xAuthObjectsStatsTable = _FsDot1xAuthObjectsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsStatsTable.setStatus("current")
_FsDot1xAuthStatsEntry_Object = MibTableRow
fsDot1xAuthStatsEntry = _FsDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1)
)
fsDot1xAuthStatsEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsDot1xAuthObjectsStatsFdbId"),
    (0, "FS-AAA-MIB", "fsDot1xAuthObjectsStatsAddr"),
)
if mibBuilder.loadTexts:
    fsDot1xAuthStatsEntry.setStatus("current")
_FsDot1xAuthObjectsStatsFdbId_Type = Unsigned32
_FsDot1xAuthObjectsStatsFdbId_Object = MibTableColumn
fsDot1xAuthObjectsStatsFdbId = _FsDot1xAuthObjectsStatsFdbId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 1),
    _FsDot1xAuthObjectsStatsFdbId_Type()
)
fsDot1xAuthObjectsStatsFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsStatsFdbId.setStatus("current")
_FsDot1xAuthObjectsStatsAddr_Type = MacAddress
_FsDot1xAuthObjectsStatsAddr_Object = MibTableColumn
fsDot1xAuthObjectsStatsAddr = _FsDot1xAuthObjectsStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 2),
    _FsDot1xAuthObjectsStatsAddr_Type()
)
fsDot1xAuthObjectsStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsStatsAddr.setStatus("current")
_FsDot1xAuthObjectsEapolFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapolFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapolFramesRx = _FsDot1xAuthObjectsEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 3),
    _FsDot1xAuthObjectsEapolFramesRx_Type()
)
fsDot1xAuthObjectsEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapolFramesTx_Type = Counter32
_FsDot1xAuthObjectsEapolFramesTx_Object = MibTableColumn
fsDot1xAuthObjectsEapolFramesTx = _FsDot1xAuthObjectsEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 4),
    _FsDot1xAuthObjectsEapolFramesTx_Type()
)
fsDot1xAuthObjectsEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolFramesTx.setStatus("current")
_FsDot1xAuthObjectsEapolFSFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapolFSFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapolFSFramesRx = _FsDot1xAuthObjectsEapolFSFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 5),
    _FsDot1xAuthObjectsEapolFSFramesRx_Type()
)
fsDot1xAuthObjectsEapolFSFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolFSFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapolLogoffFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapolLogoffFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapolLogoffFramesRx = _FsDot1xAuthObjectsEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 6),
    _FsDot1xAuthObjectsEapolLogoffFramesRx_Type()
)
fsDot1xAuthObjectsEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolLogoffFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapolRespIdFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapolRespIdFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapolRespIdFramesRx = _FsDot1xAuthObjectsEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 7),
    _FsDot1xAuthObjectsEapolRespIdFramesRx_Type()
)
fsDot1xAuthObjectsEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolRespIdFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapolRespFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapolRespFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapolRespFramesRx = _FsDot1xAuthObjectsEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 8),
    _FsDot1xAuthObjectsEapolRespFramesRx_Type()
)
fsDot1xAuthObjectsEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolRespFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapolReqIdFramesTx_Type = Counter32
_FsDot1xAuthObjectsEapolReqIdFramesTx_Object = MibTableColumn
fsDot1xAuthObjectsEapolReqIdFramesTx = _FsDot1xAuthObjectsEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 9),
    _FsDot1xAuthObjectsEapolReqIdFramesTx_Type()
)
fsDot1xAuthObjectsEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolReqIdFramesTx.setStatus("current")
_FsDot1xAuthObjectsEapolReqFramesTx_Type = Counter32
_FsDot1xAuthObjectsEapolReqFramesTx_Object = MibTableColumn
fsDot1xAuthObjectsEapolReqFramesTx = _FsDot1xAuthObjectsEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 10),
    _FsDot1xAuthObjectsEapolReqFramesTx_Type()
)
fsDot1xAuthObjectsEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapolReqFramesTx.setStatus("current")
_FsDot1xAuthObjectsInvalidEapolFramesRx_Type = Counter32
_FsDot1xAuthObjectsInvalidEapolFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsInvalidEapolFramesRx = _FsDot1xAuthObjectsInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 11),
    _FsDot1xAuthObjectsInvalidEapolFramesRx_Type()
)
fsDot1xAuthObjectsInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsInvalidEapolFramesRx.setStatus("current")
_FsDot1xAuthObjectsEapLengthErrorFramesRx_Type = Counter32
_FsDot1xAuthObjectsEapLengthErrorFramesRx_Object = MibTableColumn
fsDot1xAuthObjectsEapLengthErrorFramesRx = _FsDot1xAuthObjectsEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 12),
    _FsDot1xAuthObjectsEapLengthErrorFramesRx_Type()
)
fsDot1xAuthObjectsEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsEapLengthErrorFramesRx.setStatus("current")
_FsDot1xAuthObjectsLastEapolFrameVersion_Type = Unsigned32
_FsDot1xAuthObjectsLastEapolFrameVersion_Object = MibTableColumn
fsDot1xAuthObjectsLastEapolFrameVersion = _FsDot1xAuthObjectsLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 13),
    _FsDot1xAuthObjectsLastEapolFrameVersion_Type()
)
fsDot1xAuthObjectsLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsLastEapolFrameVersion.setStatus("current")
_FsDot1xAuthObjectsLastEapolFrameSource_Type = MacAddress
_FsDot1xAuthObjectsLastEapolFrameSource_Object = MibTableColumn
fsDot1xAuthObjectsLastEapolFrameSource = _FsDot1xAuthObjectsLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 11, 1, 14),
    _FsDot1xAuthObjectsLastEapolFrameSource_Type()
)
fsDot1xAuthObjectsLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthObjectsLastEapolFrameSource.setStatus("current")
_FsDot1xCurrentUserNumber_Type = Counter32
_FsDot1xCurrentUserNumber_Object = MibScalar
fsDot1xCurrentUserNumber = _FsDot1xCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 12),
    _FsDot1xCurrentUserNumber_Type()
)
fsDot1xCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xCurrentUserNumber.setStatus("current")
_FsDot1xCurrentAuthenticatedUserNumber_Type = Counter32
_FsDot1xCurrentAuthenticatedUserNumber_Object = MibScalar
fsDot1xCurrentAuthenticatedUserNumber = _FsDot1xCurrentAuthenticatedUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 13),
    _FsDot1xCurrentAuthenticatedUserNumber_Type()
)
fsDot1xCurrentAuthenticatedUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xCurrentAuthenticatedUserNumber.setStatus("current")


class _FsDot1xAccountStatus_Type(EnabledStatus):
    """Custom type fsDot1xAccountStatus based on EnabledStatus"""
    defaultValue = 2


_FsDot1xAccountStatus_Type.__name__ = "EnabledStatus"
_FsDot1xAccountStatus_Object = MibScalar
fsDot1xAccountStatus = _FsDot1xAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 14),
    _FsDot1xAccountStatus_Type()
)
fsDot1xAccountStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAccountStatus.setStatus("current")
_FsAuthIfTable_Object = MibTable
fsAuthIfTable = _FsAuthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 15)
)
if mibBuilder.loadTexts:
    fsAuthIfTable.setStatus("current")
_FsAuthIfEntry_Object = MibTableRow
fsAuthIfEntry = _FsAuthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 15, 1)
)
fsAuthIfEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAuthIf"),
)
if mibBuilder.loadTexts:
    fsAuthIfEntry.setStatus("current")
_FsAuthIf_Type = IfIndex
_FsAuthIf_Object = MibTableColumn
fsAuthIf = _FsAuthIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 15, 1, 1),
    _FsAuthIf_Type()
)
fsAuthIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthIf.setStatus("current")


class _FsAuthIfStatus_Type(EnabledStatus):
    """Custom type fsAuthIfStatus based on EnabledStatus"""
    defaultValue = 2


_FsAuthIfStatus_Type.__name__ = "EnabledStatus"
_FsAuthIfStatus_Object = MibTableColumn
fsAuthIfStatus = _FsAuthIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 15, 1, 2),
    _FsAuthIfStatus_Type()
)
fsAuthIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAuthIfStatus.setStatus("current")


class _FsAuthenticationMode_Type(Integer32):
    """Custom type fsAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eap", 1),
          ("chap", 2),
          ("pap", 3))
    )


_FsAuthenticationMode_Type.__name__ = "Integer32"
_FsAuthenticationMode_Object = MibScalar
fsAuthenticationMode = _FsAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 16),
    _FsAuthenticationMode_Type()
)
fsAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAuthenticationMode.setStatus("current")
_FsDot1xAccountUpdateStatus_Type = EnabledStatus
_FsDot1xAccountUpdateStatus_Object = MibScalar
fsDot1xAccountUpdateStatus = _FsDot1xAccountUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 17),
    _FsDot1xAccountUpdateStatus_Type()
)
fsDot1xAccountUpdateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAccountUpdateStatus.setStatus("current")


class _FsDot1xAcctInterimInterval_Type(Unsigned32):
    """Custom type fsDot1xAcctInterimInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_FsDot1xAcctInterimInterval_Type.__name__ = "Unsigned32"
_FsDot1xAcctInterimInterval_Object = MibScalar
fsDot1xAcctInterimInterval = _FsDot1xAcctInterimInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 18),
    _FsDot1xAcctInterimInterval_Type()
)
fsDot1xAcctInterimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAcctInterimInterval.setStatus("current")
_FsDot1xEapolTagEnabled_Type = EnabledStatus
_FsDot1xEapolTagEnabled_Object = MibScalar
fsDot1xEapolTagEnabled = _FsDot1xEapolTagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 19),
    _FsDot1xEapolTagEnabled_Type()
)
fsDot1xEapolTagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xEapolTagEnabled.setStatus("current")
_FsDot1xIfUserMaxTable_Object = MibTable
fsDot1xIfUserMaxTable = _FsDot1xIfUserMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 20)
)
if mibBuilder.loadTexts:
    fsDot1xIfUserMaxTable.setStatus("current")
_FsDot1xIfUserMaxEntry_Object = MibTableRow
fsDot1xIfUserMaxEntry = _FsDot1xIfUserMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 20, 1)
)
fsDot1xIfUserMaxEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsDot1xIfUserMaxIndex"),
)
if mibBuilder.loadTexts:
    fsDot1xIfUserMaxEntry.setStatus("current")
_FsDot1xIfUserMaxIndex_Type = IfIndex
_FsDot1xIfUserMaxIndex_Object = MibTableColumn
fsDot1xIfUserMaxIndex = _FsDot1xIfUserMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 20, 1, 1),
    _FsDot1xIfUserMaxIndex_Type()
)
fsDot1xIfUserMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xIfUserMaxIndex.setStatus("current")


class _FsDot1xIfUserMaxNum_Type(Unsigned32):
    """Custom type fsDot1xIfUserMaxNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_FsDot1xIfUserMaxNum_Type.__name__ = "Unsigned32"
_FsDot1xIfUserMaxNum_Object = MibTableColumn
fsDot1xIfUserMaxNum = _FsDot1xIfUserMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 20, 1, 2),
    _FsDot1xIfUserMaxNum_Type()
)
fsDot1xIfUserMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xIfUserMaxNum.setStatus("current")


class _FsDot1xPseudoSrcmac_Type(EnabledStatus):
    """Custom type fsDot1xPseudoSrcmac based on EnabledStatus"""
    defaultValue = 1


_FsDot1xPseudoSrcmac_Type.__name__ = "EnabledStatus"
_FsDot1xPseudoSrcmac_Object = MibScalar
fsDot1xPseudoSrcmac = _FsDot1xPseudoSrcmac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 21),
    _FsDot1xPseudoSrcmac_Type()
)
fsDot1xPseudoSrcmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xPseudoSrcmac.setStatus("current")
_FsDot1xUserMIB_ObjectIdentity = ObjectIdentity
fsDot1xUserMIB = _FsDot1xUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22)
)
_FsDot1xUserTrapsObjects_ObjectIdentity = ObjectIdentity
fsDot1xUserTrapsObjects = _FsDot1xUserTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1)
)
_FsDot1xUserMac_Type = MacAddress
_FsDot1xUserMac_Object = MibScalar
fsDot1xUserMac = _FsDot1xUserMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 1),
    _FsDot1xUserMac_Type()
)
fsDot1xUserMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserMac.setStatus("current")
_FsDot1xUserName_Type = DisplayString
_FsDot1xUserName_Object = MibScalar
fsDot1xUserName = _FsDot1xUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 2),
    _FsDot1xUserName_Type()
)
fsDot1xUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserName.setStatus("current")
_FsDot1xUserIp_Type = IpAddress
_FsDot1xUserIp_Object = MibScalar
fsDot1xUserIp = _FsDot1xUserIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 3),
    _FsDot1xUserIp_Type()
)
fsDot1xUserIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserIp.setStatus("current")
_FsDot1xUserIpv6_Type = InetAddress
_FsDot1xUserIpv6_Object = MibScalar
fsDot1xUserIpv6 = _FsDot1xUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 4),
    _FsDot1xUserIpv6_Type()
)
fsDot1xUserIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserIpv6.setStatus("current")


class _FsDot1xUserWlanId_Type(Integer32):
    """Custom type fsDot1xUserWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsDot1xUserWlanId_Type.__name__ = "Integer32"
_FsDot1xUserWlanId_Object = MibScalar
fsDot1xUserWlanId = _FsDot1xUserWlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 5),
    _FsDot1xUserWlanId_Type()
)
fsDot1xUserWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserWlanId.setStatus("current")


class _FsDot1xUserVlanId_Type(Integer32):
    """Custom type fsDot1xUserVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsDot1xUserVlanId_Type.__name__ = "Integer32"
_FsDot1xUserVlanId_Object = MibScalar
fsDot1xUserVlanId = _FsDot1xUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 6),
    _FsDot1xUserVlanId_Type()
)
fsDot1xUserVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserVlanId.setStatus("current")
_FsDot1xUserSsid_Type = DisplayString
_FsDot1xUserSsid_Object = MibScalar
fsDot1xUserSsid = _FsDot1xUserSsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 7),
    _FsDot1xUserSsid_Type()
)
fsDot1xUserSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserSsid.setStatus("current")
_FsDot1xUserApMac_Type = MacAddress
_FsDot1xUserApMac_Object = MibScalar
fsDot1xUserApMac = _FsDot1xUserApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 8),
    _FsDot1xUserApMac_Type()
)
fsDot1xUserApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserApMac.setStatus("current")
_FsDot1xUserTerminalType_Type = DisplayString
_FsDot1xUserTerminalType_Object = MibScalar
fsDot1xUserTerminalType = _FsDot1xUserTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 9),
    _FsDot1xUserTerminalType_Type()
)
fsDot1xUserTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserTerminalType.setStatus("current")


class _FsDot1xUserOperType_Type(Integer32):
    """Custom type fsDot1xUserOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("authenfail", 3))
    )


_FsDot1xUserOperType_Type.__name__ = "Integer32"
_FsDot1xUserOperType_Object = MibScalar
fsDot1xUserOperType = _FsDot1xUserOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 10),
    _FsDot1xUserOperType_Type()
)
fsDot1xUserOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserOperType.setStatus("current")
_FsDot1xUserTerminateCause_Type = Integer32
_FsDot1xUserTerminateCause_Object = MibScalar
fsDot1xUserTerminateCause = _FsDot1xUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 11),
    _FsDot1xUserTerminateCause_Type()
)
fsDot1xUserTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserTerminateCause.setStatus("current")
_FsDot1xUserReplyMessage_Type = DisplayString
_FsDot1xUserReplyMessage_Object = MibScalar
fsDot1xUserReplyMessage = _FsDot1xUserReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 12),
    _FsDot1xUserReplyMessage_Type()
)
fsDot1xUserReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserReplyMessage.setStatus("current")


class _FsDot1xUserIfIndex_Type(Integer32):
    """Custom type fsDot1xUserIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsDot1xUserIfIndex_Type.__name__ = "Integer32"
_FsDot1xUserIfIndex_Object = MibScalar
fsDot1xUserIfIndex = _FsDot1xUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 1, 13),
    _FsDot1xUserIfIndex_Type()
)
fsDot1xUserIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDot1xUserIfIndex.setStatus("current")
_FsDot1xUserTraps_ObjectIdentity = ObjectIdentity
fsDot1xUserTraps = _FsDot1xUserTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 2)
)
_FsDot1xOnlineUserTable_Object = MibTable
fsDot1xOnlineUserTable = _FsDot1xOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    fsDot1xOnlineUserTable.setStatus("current")
_FsDot1xOnlineUserEntry_Object = MibTableRow
fsDot1xOnlineUserEntry = _FsDot1xOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1)
)
fsDot1xOnlineUserEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsDot1xOnlineUserID"),
)
if mibBuilder.loadTexts:
    fsDot1xOnlineUserEntry.setStatus("current")
_FsDot1xOnlineUserID_Type = Integer32
_FsDot1xOnlineUserID_Object = MibTableColumn
fsDot1xOnlineUserID = _FsDot1xOnlineUserID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 1),
    _FsDot1xOnlineUserID_Type()
)
fsDot1xOnlineUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserID.setStatus("current")
_FsDot1xOnlineUserName_Type = DisplayString
_FsDot1xOnlineUserName_Object = MibTableColumn
fsDot1xOnlineUserName = _FsDot1xOnlineUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 2),
    _FsDot1xOnlineUserName_Type()
)
fsDot1xOnlineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserName.setStatus("current")
_FsDot1xOnlineUserMacAddr_Type = MacAddress
_FsDot1xOnlineUserMacAddr_Object = MibTableColumn
fsDot1xOnlineUserMacAddr = _FsDot1xOnlineUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 3),
    _FsDot1xOnlineUserMacAddr_Type()
)
fsDot1xOnlineUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserMacAddr.setStatus("current")
_FsDot1xOnlineUserIfIndex_Type = Integer32
_FsDot1xOnlineUserIfIndex_Object = MibTableColumn
fsDot1xOnlineUserIfIndex = _FsDot1xOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 4),
    _FsDot1xOnlineUserIfIndex_Type()
)
fsDot1xOnlineUserIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserIfIndex.setStatus("current")
_FsDot1xOnlineUserVlanId_Type = Integer32
_FsDot1xOnlineUserVlanId_Object = MibTableColumn
fsDot1xOnlineUserVlanId = _FsDot1xOnlineUserVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 5),
    _FsDot1xOnlineUserVlanId_Type()
)
fsDot1xOnlineUserVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserVlanId.setStatus("current")
_FsDot1xOnlineUserIp_Type = IpAddress
_FsDot1xOnlineUserIp_Object = MibTableColumn
fsDot1xOnlineUserIp = _FsDot1xOnlineUserIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 6),
    _FsDot1xOnlineUserIp_Type()
)
fsDot1xOnlineUserIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserIp.setStatus("current")
_FsDot1xOnlineUserIpv6_Type = InetAddress
_FsDot1xOnlineUserIpv6_Object = MibTableColumn
fsDot1xOnlineUserIpv6 = _FsDot1xOnlineUserIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 3, 1, 7),
    _FsDot1xOnlineUserIpv6_Type()
)
fsDot1xOnlineUserIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xOnlineUserIpv6.setStatus("current")
_FsDot1xAbnormalOfflineUserCount_Type = Counter64
_FsDot1xAbnormalOfflineUserCount_Object = MibScalar
fsDot1xAbnormalOfflineUserCount = _FsDot1xAbnormalOfflineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 23),
    _FsDot1xAbnormalOfflineUserCount_Type()
)
fsDot1xAbnormalOfflineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAbnormalOfflineUserCount.setStatus("current")
_FsDot1xTotalAuthUserCount_Type = Counter64
_FsDot1xTotalAuthUserCount_Object = MibScalar
fsDot1xTotalAuthUserCount = _FsDot1xTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 24),
    _FsDot1xTotalAuthUserCount_Type()
)
fsDot1xTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xTotalAuthUserCount.setStatus("current")
_FsDot1xAuthSuccUserCount_Type = Counter64
_FsDot1xAuthSuccUserCount_Object = MibScalar
fsDot1xAuthSuccUserCount = _FsDot1xAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 25),
    _FsDot1xAuthSuccUserCount_Type()
)
fsDot1xAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthSuccUserCount.setStatus("current")
_FsDot1xAuthFailUserCount_Type = Counter64
_FsDot1xAuthFailUserCount_Object = MibScalar
fsDot1xAuthFailUserCount = _FsDot1xAuthFailUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 26),
    _FsDot1xAuthFailUserCount_Type()
)
fsDot1xAuthFailUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1xAuthFailUserCount.setStatus("current")
_FsAAAServerObjects_ObjectIdentity = ObjectIdentity
fsAAAServerObjects = _FsAAAServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2)
)


class _FsAAAServerAuthPort_Type(Integer32):
    """Custom type fsAAAServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAServerAuthPort_Type.__name__ = "Integer32"
_FsAAAServerAuthPort_Object = MibScalar
fsAAAServerAuthPort = _FsAAAServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 2),
    _FsAAAServerAuthPort_Type()
)
fsAAAServerAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAAAServerAuthPort.setStatus("current")


class _FsAAAServerAcctPort_Type(Integer32):
    """Custom type fsAAAServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAServerAcctPort_Type.__name__ = "Integer32"
_FsAAAServerAcctPort_Object = MibScalar
fsAAAServerAcctPort = _FsAAAServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 3),
    _FsAAAServerAcctPort_Type()
)
fsAAAServerAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAAAServerAcctPort.setStatus("current")


class _FsAAAServerRadiusKeyStr_Type(DisplayString):
    """Custom type fsAAAServerRadiusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAAServerRadiusKeyStr_Type.__name__ = "DisplayString"
_FsAAAServerRadiusKeyStr_Object = MibScalar
fsAAAServerRadiusKeyStr = _FsAAAServerRadiusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 4),
    _FsAAAServerRadiusKeyStr_Type()
)
fsAAAServerRadiusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAAAServerRadiusKeyStr.setStatus("current")


class _FsAAAServerTacplusKeyStr_Type(DisplayString):
    """Custom type fsAAAServerTacplusKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAAServerTacplusKeyStr_Type.__name__ = "DisplayString"
_FsAAAServerTacplusKeyStr_Object = MibScalar
fsAAAServerTacplusKeyStr = _FsAAAServerTacplusKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 8),
    _FsAAAServerTacplusKeyStr_Type()
)
fsAAAServerTacplusKeyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAAAServerTacplusKeyStr.setStatus("current")
_FsAAAServerConfigTable_Object = MibTable
fsAAAServerConfigTable = _FsAAAServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsAAAServerConfigTable.setStatus("current")
_FsAAAServerConfigEntry_Object = MibTableRow
fsAAAServerConfigEntry = _FsAAAServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1)
)
fsAAAServerConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAAServerConfigProtocol"),
    (0, "FS-AAA-MIB", "fsAAAServerConfigIndex"),
)
if mibBuilder.loadTexts:
    fsAAAServerConfigEntry.setStatus("current")


class _FsAAAServerConfigProtocol_Type(Integer32):
    """Custom type fsAAAServerConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 1),
          ("tacplus", 2))
    )


_FsAAAServerConfigProtocol_Type.__name__ = "Integer32"
_FsAAAServerConfigProtocol_Object = MibTableColumn
fsAAAServerConfigProtocol = _FsAAAServerConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 1),
    _FsAAAServerConfigProtocol_Type()
)
fsAAAServerConfigProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAServerConfigProtocol.setStatus("current")


class _FsAAAServerConfigIndex_Type(Unsigned32):
    """Custom type fsAAAServerConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerConfigIndex_Type.__name__ = "Unsigned32"
_FsAAAServerConfigIndex_Object = MibTableColumn
fsAAAServerConfigIndex = _FsAAAServerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 2),
    _FsAAAServerConfigIndex_Type()
)
fsAAAServerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAServerConfigIndex.setStatus("current")
_FsAAAServerConfigAddressType_Type = InetAddressType
_FsAAAServerConfigAddressType_Object = MibTableColumn
fsAAAServerConfigAddressType = _FsAAAServerConfigAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 3),
    _FsAAAServerConfigAddressType_Type()
)
fsAAAServerConfigAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigAddressType.setStatus("current")
_FsAAAServerConfigAddress_Type = InetAddress
_FsAAAServerConfigAddress_Object = MibTableColumn
fsAAAServerConfigAddress = _FsAAAServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 4),
    _FsAAAServerConfigAddress_Type()
)
fsAAAServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigAddress.setStatus("current")


class _FsAAAServerConfigAuthPort_Type(Integer32):
    """Custom type fsAAAServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAServerConfigAuthPort_Type.__name__ = "Integer32"
_FsAAAServerConfigAuthPort_Object = MibTableColumn
fsAAAServerConfigAuthPort = _FsAAAServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 5),
    _FsAAAServerConfigAuthPort_Type()
)
fsAAAServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigAuthPort.setStatus("current")


class _FsAAAServerConfigAcctPort_Type(Integer32):
    """Custom type fsAAAServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAServerConfigAcctPort_Type.__name__ = "Integer32"
_FsAAAServerConfigAcctPort_Object = MibTableColumn
fsAAAServerConfigAcctPort = _FsAAAServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 6),
    _FsAAAServerConfigAcctPort_Type()
)
fsAAAServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigAcctPort.setStatus("current")


class _FsAAAServerConfigKeyStr_Type(DisplayString):
    """Custom type fsAAAServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAAServerConfigKeyStr_Type.__name__ = "DisplayString"
_FsAAAServerConfigKeyStr_Object = MibTableColumn
fsAAAServerConfigKeyStr = _FsAAAServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 7),
    _FsAAAServerConfigKeyStr_Type()
)
fsAAAServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigKeyStr.setStatus("current")
_FsAAAServerConfigRowStatus_Type = RowStatus
_FsAAAServerConfigRowStatus_Object = MibTableColumn
fsAAAServerConfigRowStatus = _FsAAAServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 9, 1, 8),
    _FsAAAServerConfigRowStatus_Type()
)
fsAAAServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAServerConfigRowStatus.setStatus("current")
_FsAAARadiusGroupTable_Object = MibTable
fsAAARadiusGroupTable = _FsAAARadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 10)
)
if mibBuilder.loadTexts:
    fsAAARadiusGroupTable.setStatus("current")
_FsAAARadiusGroupEntry_Object = MibTableRow
fsAAARadiusGroupEntry = _FsAAARadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 10, 1)
)
fsAAARadiusGroupEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAARadiusGroupName"),
)
if mibBuilder.loadTexts:
    fsAAARadiusGroupEntry.setStatus("current")


class _FsAAARadiusGroupName_Type(DisplayString):
    """Custom type fsAAARadiusGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAAARadiusGroupName_Type.__name__ = "DisplayString"
_FsAAARadiusGroupName_Object = MibTableColumn
fsAAARadiusGroupName = _FsAAARadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 10, 1, 1),
    _FsAAARadiusGroupName_Type()
)
fsAAARadiusGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAARadiusGroupName.setStatus("current")


class _FsAAARadiusGroupVrf_Type(DisplayString):
    """Custom type fsAAARadiusGroupVrf based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FsAAARadiusGroupVrf_Type.__name__ = "DisplayString"
_FsAAARadiusGroupVrf_Object = MibTableColumn
fsAAARadiusGroupVrf = _FsAAARadiusGroupVrf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 10, 1, 2),
    _FsAAARadiusGroupVrf_Type()
)
fsAAARadiusGroupVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupVrf.setStatus("current")
_FsAAARadiusGroupRowStatus_Type = RowStatus
_FsAAARadiusGroupRowStatus_Object = MibTableColumn
fsAAARadiusGroupRowStatus = _FsAAARadiusGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 10, 1, 3),
    _FsAAARadiusGroupRowStatus_Type()
)
fsAAARadiusGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupRowStatus.setStatus("current")
_FsAAARadiusGroupServerTable_Object = MibTable
fsAAARadiusGroupServerTable = _FsAAARadiusGroupServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11)
)
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerTable.setStatus("current")
_FsAAARadiusGroupServerEntry_Object = MibTableRow
fsAAARadiusGroupServerEntry = _FsAAARadiusGroupServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1)
)
fsAAARadiusGroupServerEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAARadiusGroupName"),
    (0, "FS-AAA-MIB", "fsAAARadiusGroupServerIndex"),
)
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerEntry.setStatus("current")


class _FsAAARadiusGroupServerIndex_Type(Unsigned32):
    """Custom type fsAAARadiusGroupServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAARadiusGroupServerIndex_Type.__name__ = "Unsigned32"
_FsAAARadiusGroupServerIndex_Object = MibTableColumn
fsAAARadiusGroupServerIndex = _FsAAARadiusGroupServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 1),
    _FsAAARadiusGroupServerIndex_Type()
)
fsAAARadiusGroupServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerIndex.setStatus("current")
_FsAAARadiusGroupServerAddressType_Type = InetAddressType
_FsAAARadiusGroupServerAddressType_Object = MibTableColumn
fsAAARadiusGroupServerAddressType = _FsAAARadiusGroupServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 2),
    _FsAAARadiusGroupServerAddressType_Type()
)
fsAAARadiusGroupServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerAddressType.setStatus("current")
_FsAAARadiusGroupServerAddress_Type = InetAddress
_FsAAARadiusGroupServerAddress_Object = MibTableColumn
fsAAARadiusGroupServerAddress = _FsAAARadiusGroupServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 3),
    _FsAAARadiusGroupServerAddress_Type()
)
fsAAARadiusGroupServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerAddress.setStatus("current")


class _FsAAARadiusGroupServerAuthPort_Type(Integer32):
    """Custom type fsAAARadiusGroupServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAARadiusGroupServerAuthPort_Type.__name__ = "Integer32"
_FsAAARadiusGroupServerAuthPort_Object = MibTableColumn
fsAAARadiusGroupServerAuthPort = _FsAAARadiusGroupServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 4),
    _FsAAARadiusGroupServerAuthPort_Type()
)
fsAAARadiusGroupServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerAuthPort.setStatus("current")


class _FsAAARadiusGroupServerAcctPort_Type(Integer32):
    """Custom type fsAAARadiusGroupServerAcctPort based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAARadiusGroupServerAcctPort_Type.__name__ = "Integer32"
_FsAAARadiusGroupServerAcctPort_Object = MibTableColumn
fsAAARadiusGroupServerAcctPort = _FsAAARadiusGroupServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 5),
    _FsAAARadiusGroupServerAcctPort_Type()
)
fsAAARadiusGroupServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerAcctPort.setStatus("current")
_FsAAARadiusGroupServerRowStatus_Type = RowStatus
_FsAAARadiusGroupServerRowStatus_Object = MibTableColumn
fsAAARadiusGroupServerRowStatus = _FsAAARadiusGroupServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 11, 1, 6),
    _FsAAARadiusGroupServerRowStatus_Type()
)
fsAAARadiusGroupServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAARadiusGroupServerRowStatus.setStatus("current")


class _FsAAAServerTotalOnlineCount_Type(Integer32):
    """Custom type fsAAAServerTotalOnlineCount based on Integer32"""
    defaultValue = 0


_FsAAAServerTotalOnlineCount_Type.__name__ = "Integer32"
_FsAAAServerTotalOnlineCount_Object = MibScalar
fsAAAServerTotalOnlineCount = _FsAAAServerTotalOnlineCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 12),
    _FsAAAServerTotalOnlineCount_Type()
)
fsAAAServerTotalOnlineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerTotalOnlineCount.setStatus("current")


class _FsAAAServerAbnormalOffline_Type(Counter32):
    """Custom type fsAAAServerAbnormalOffline based on Counter32"""
    defaultValue = 0


_FsAAAServerAbnormalOffline_Type.__name__ = "Counter32"
_FsAAAServerAbnormalOffline_Object = MibScalar
fsAAAServerAbnormalOffline = _FsAAAServerAbnormalOffline_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 13),
    _FsAAAServerAbnormalOffline_Type()
)
fsAAAServerAbnormalOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerAbnormalOffline.setStatus("current")


class _FsAAAServerRadiusAuthReqCount_Type(Counter32):
    """Custom type fsAAAServerRadiusAuthReqCount based on Counter32"""
    defaultValue = 0


_FsAAAServerRadiusAuthReqCount_Type.__name__ = "Counter32"
_FsAAAServerRadiusAuthReqCount_Object = MibScalar
fsAAAServerRadiusAuthReqCount = _FsAAAServerRadiusAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 14),
    _FsAAAServerRadiusAuthReqCount_Type()
)
fsAAAServerRadiusAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerRadiusAuthReqCount.setStatus("current")


class _FsAAAServerRadiusAuthRespCount_Type(Counter32):
    """Custom type fsAAAServerRadiusAuthRespCount based on Counter32"""
    defaultValue = 0


_FsAAAServerRadiusAuthRespCount_Type.__name__ = "Counter32"
_FsAAAServerRadiusAuthRespCount_Object = MibScalar
fsAAAServerRadiusAuthRespCount = _FsAAAServerRadiusAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 15),
    _FsAAAServerRadiusAuthRespCount_Type()
)
fsAAAServerRadiusAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerRadiusAuthRespCount.setStatus("current")


class _FsAAAServerRadiusAuthSuccessCount_Type(Counter32):
    """Custom type fsAAAServerRadiusAuthSuccessCount based on Counter32"""
    defaultValue = 0


_FsAAAServerRadiusAuthSuccessCount_Type.__name__ = "Counter32"
_FsAAAServerRadiusAuthSuccessCount_Object = MibScalar
fsAAAServerRadiusAuthSuccessCount = _FsAAAServerRadiusAuthSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 16),
    _FsAAAServerRadiusAuthSuccessCount_Type()
)
fsAAAServerRadiusAuthSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerRadiusAuthSuccessCount.setStatus("current")


class _FsAAAServerCurrOnlineUserCount_Type(Integer32):
    """Custom type fsAAAServerCurrOnlineUserCount based on Integer32"""
    defaultValue = 0


_FsAAAServerCurrOnlineUserCount_Type.__name__ = "Integer32"
_FsAAAServerCurrOnlineUserCount_Object = MibScalar
fsAAAServerCurrOnlineUserCount = _FsAAAServerCurrOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 17),
    _FsAAAServerCurrOnlineUserCount_Type()
)
fsAAAServerCurrOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerCurrOnlineUserCount.setStatus("current")
_FsAAAMasterAuthenServerConfigTable_Object = MibTable
fsAAAMasterAuthenServerConfigTable = _FsAAAMasterAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18)
)
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigTable.setStatus("current")
_FsAAAMasterAuthenServerConfigEntry_Object = MibTableRow
fsAAAMasterAuthenServerConfigEntry = _FsAAAMasterAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1)
)
fsAAAMasterAuthenServerConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAAMasterAuthenServerConfigGrpName"),
    (0, "FS-AAA-MIB", "fsAAAMasterAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigEntry.setStatus("current")


class _FsAAAMasterAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type fsAAAMasterAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAAAMasterAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_FsAAAMasterAuthenServerConfigGrpName_Object = MibTableColumn
fsAAAMasterAuthenServerConfigGrpName = _FsAAAMasterAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 1),
    _FsAAAMasterAuthenServerConfigGrpName_Type()
)
fsAAAMasterAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigGrpName.setStatus("current")


class _FsAAAMasterAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type fsAAAMasterAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAMasterAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_FsAAAMasterAuthenServerConfigSrvIndex_Object = MibTableColumn
fsAAAMasterAuthenServerConfigSrvIndex = _FsAAAMasterAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 2),
    _FsAAAMasterAuthenServerConfigSrvIndex_Type()
)
fsAAAMasterAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigSrvIndex.setStatus("current")
_FsAAAMasterAuthenServerConfigAddress_Type = IpAddress
_FsAAAMasterAuthenServerConfigAddress_Object = MibTableColumn
fsAAAMasterAuthenServerConfigAddress = _FsAAAMasterAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 3),
    _FsAAAMasterAuthenServerConfigAddress_Type()
)
fsAAAMasterAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigAddress.setStatus("current")


class _FsAAAMasterAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type fsAAAMasterAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAMasterAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_FsAAAMasterAuthenServerConfigAuthPort_Object = MibTableColumn
fsAAAMasterAuthenServerConfigAuthPort = _FsAAAMasterAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 4),
    _FsAAAMasterAuthenServerConfigAuthPort_Type()
)
fsAAAMasterAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigAuthPort.setStatus("current")


class _FsAAAMasterAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type fsAAAMasterAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAMasterAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_FsAAAMasterAuthenServerConfigAcctPort_Object = MibTableColumn
fsAAAMasterAuthenServerConfigAcctPort = _FsAAAMasterAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 5),
    _FsAAAMasterAuthenServerConfigAcctPort_Type()
)
fsAAAMasterAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigAcctPort.setStatus("current")


class _FsAAAMasterAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type fsAAAMasterAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAAMasterAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_FsAAAMasterAuthenServerConfigKeyStr_Object = MibTableColumn
fsAAAMasterAuthenServerConfigKeyStr = _FsAAAMasterAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 6),
    _FsAAAMasterAuthenServerConfigKeyStr_Type()
)
fsAAAMasterAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigKeyStr.setStatus("current")
_FsAAAMasterAuthenServerConfigRowStatus_Type = RowStatus
_FsAAAMasterAuthenServerConfigRowStatus_Object = MibTableColumn
fsAAAMasterAuthenServerConfigRowStatus = _FsAAAMasterAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 18, 1, 7),
    _FsAAAMasterAuthenServerConfigRowStatus_Type()
)
fsAAAMasterAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAuthenServerConfigRowStatus.setStatus("current")
_FsAAABackAuthenServerConfigTable_Object = MibTable
fsAAABackAuthenServerConfigTable = _FsAAABackAuthenServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19)
)
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigTable.setStatus("current")
_FsAAABackAuthenServerConfigEntry_Object = MibTableRow
fsAAABackAuthenServerConfigEntry = _FsAAABackAuthenServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1)
)
fsAAABackAuthenServerConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAABackAuthenServerConfigGrpName"),
    (0, "FS-AAA-MIB", "fsAAABackAuthenServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigEntry.setStatus("current")


class _FsAAABackAuthenServerConfigGrpName_Type(DisplayString):
    """Custom type fsAAABackAuthenServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAAABackAuthenServerConfigGrpName_Type.__name__ = "DisplayString"
_FsAAABackAuthenServerConfigGrpName_Object = MibTableColumn
fsAAABackAuthenServerConfigGrpName = _FsAAABackAuthenServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 1),
    _FsAAABackAuthenServerConfigGrpName_Type()
)
fsAAABackAuthenServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigGrpName.setStatus("current")


class _FsAAABackAuthenServerConfigSrvIndex_Type(Unsigned32):
    """Custom type fsAAABackAuthenServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAABackAuthenServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_FsAAABackAuthenServerConfigSrvIndex_Object = MibTableColumn
fsAAABackAuthenServerConfigSrvIndex = _FsAAABackAuthenServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 2),
    _FsAAABackAuthenServerConfigSrvIndex_Type()
)
fsAAABackAuthenServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigSrvIndex.setStatus("current")
_FsAAABackAuthenServerConfigAddress_Type = IpAddress
_FsAAABackAuthenServerConfigAddress_Object = MibTableColumn
fsAAABackAuthenServerConfigAddress = _FsAAABackAuthenServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 3),
    _FsAAABackAuthenServerConfigAddress_Type()
)
fsAAABackAuthenServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigAddress.setStatus("current")


class _FsAAABackAuthenServerConfigAuthPort_Type(Integer32):
    """Custom type fsAAABackAuthenServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAABackAuthenServerConfigAuthPort_Type.__name__ = "Integer32"
_FsAAABackAuthenServerConfigAuthPort_Object = MibTableColumn
fsAAABackAuthenServerConfigAuthPort = _FsAAABackAuthenServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 4),
    _FsAAABackAuthenServerConfigAuthPort_Type()
)
fsAAABackAuthenServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigAuthPort.setStatus("current")


class _FsAAABackAuthenServerConfigAcctPort_Type(Integer32):
    """Custom type fsAAABackAuthenServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAABackAuthenServerConfigAcctPort_Type.__name__ = "Integer32"
_FsAAABackAuthenServerConfigAcctPort_Object = MibTableColumn
fsAAABackAuthenServerConfigAcctPort = _FsAAABackAuthenServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 5),
    _FsAAABackAuthenServerConfigAcctPort_Type()
)
fsAAABackAuthenServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigAcctPort.setStatus("current")


class _FsAAABackAuthenServerConfigKeyStr_Type(DisplayString):
    """Custom type fsAAABackAuthenServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAABackAuthenServerConfigKeyStr_Type.__name__ = "DisplayString"
_FsAAABackAuthenServerConfigKeyStr_Object = MibTableColumn
fsAAABackAuthenServerConfigKeyStr = _FsAAABackAuthenServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 6),
    _FsAAABackAuthenServerConfigKeyStr_Type()
)
fsAAABackAuthenServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigKeyStr.setStatus("current")
_FsAAABackAuthenServerConfigRowStatus_Type = RowStatus
_FsAAABackAuthenServerConfigRowStatus_Object = MibTableColumn
fsAAABackAuthenServerConfigRowStatus = _FsAAABackAuthenServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 19, 1, 7),
    _FsAAABackAuthenServerConfigRowStatus_Type()
)
fsAAABackAuthenServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAuthenServerConfigRowStatus.setStatus("current")
_FsAAAMasterAcctServerConfigTable_Object = MibTable
fsAAAMasterAcctServerConfigTable = _FsAAAMasterAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20)
)
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigTable.setStatus("current")
_FsAAAMasterAcctServerConfigEntry_Object = MibTableRow
fsAAAMasterAcctServerConfigEntry = _FsAAAMasterAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1)
)
fsAAAMasterAcctServerConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAAMasterAcctServerConfigGrpName"),
    (0, "FS-AAA-MIB", "fsAAAMasterAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigEntry.setStatus("current")


class _FsAAAMasterAcctServerConfigGrpName_Type(DisplayString):
    """Custom type fsAAAMasterAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAAAMasterAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_FsAAAMasterAcctServerConfigGrpName_Object = MibTableColumn
fsAAAMasterAcctServerConfigGrpName = _FsAAAMasterAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 1),
    _FsAAAMasterAcctServerConfigGrpName_Type()
)
fsAAAMasterAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigGrpName.setStatus("current")


class _FsAAAMasterAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type fsAAAMasterAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAMasterAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_FsAAAMasterAcctServerConfigSrvIndex_Object = MibTableColumn
fsAAAMasterAcctServerConfigSrvIndex = _FsAAAMasterAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 2),
    _FsAAAMasterAcctServerConfigSrvIndex_Type()
)
fsAAAMasterAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigSrvIndex.setStatus("current")
_FsAAAMasterAcctServerConfigAddress_Type = IpAddress
_FsAAAMasterAcctServerConfigAddress_Object = MibTableColumn
fsAAAMasterAcctServerConfigAddress = _FsAAAMasterAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 3),
    _FsAAAMasterAcctServerConfigAddress_Type()
)
fsAAAMasterAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigAddress.setStatus("current")


class _FsAAAMasterAcctServerConfigAuthPort_Type(Integer32):
    """Custom type fsAAAMasterAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAMasterAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_FsAAAMasterAcctServerConfigAuthPort_Object = MibTableColumn
fsAAAMasterAcctServerConfigAuthPort = _FsAAAMasterAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 4),
    _FsAAAMasterAcctServerConfigAuthPort_Type()
)
fsAAAMasterAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigAuthPort.setStatus("current")


class _FsAAAMasterAcctServerConfigAcctPort_Type(Integer32):
    """Custom type fsAAAMasterAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAAMasterAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_FsAAAMasterAcctServerConfigAcctPort_Object = MibTableColumn
fsAAAMasterAcctServerConfigAcctPort = _FsAAAMasterAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 5),
    _FsAAAMasterAcctServerConfigAcctPort_Type()
)
fsAAAMasterAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigAcctPort.setStatus("current")


class _FsAAAMasterAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type fsAAAMasterAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAAMasterAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_FsAAAMasterAcctServerConfigKeyStr_Object = MibTableColumn
fsAAAMasterAcctServerConfigKeyStr = _FsAAAMasterAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 6),
    _FsAAAMasterAcctServerConfigKeyStr_Type()
)
fsAAAMasterAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigKeyStr.setStatus("current")
_FsAAAMasterAcctServerConfigRowStatus_Type = RowStatus
_FsAAAMasterAcctServerConfigRowStatus_Object = MibTableColumn
fsAAAMasterAcctServerConfigRowStatus = _FsAAAMasterAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 20, 1, 7),
    _FsAAAMasterAcctServerConfigRowStatus_Type()
)
fsAAAMasterAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAAMasterAcctServerConfigRowStatus.setStatus("current")
_FsAAABackAcctServerConfigTable_Object = MibTable
fsAAABackAcctServerConfigTable = _FsAAABackAcctServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21)
)
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigTable.setStatus("current")
_FsAAABackAcctServerConfigEntry_Object = MibTableRow
fsAAABackAcctServerConfigEntry = _FsAAABackAcctServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1)
)
fsAAABackAcctServerConfigEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAABackAcctServerConfigGrpName"),
    (0, "FS-AAA-MIB", "fsAAABackAcctServerConfigSrvIndex"),
)
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigEntry.setStatus("current")


class _FsAAABackAcctServerConfigGrpName_Type(DisplayString):
    """Custom type fsAAABackAcctServerConfigGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAAABackAcctServerConfigGrpName_Type.__name__ = "DisplayString"
_FsAAABackAcctServerConfigGrpName_Object = MibTableColumn
fsAAABackAcctServerConfigGrpName = _FsAAABackAcctServerConfigGrpName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 1),
    _FsAAABackAcctServerConfigGrpName_Type()
)
fsAAABackAcctServerConfigGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigGrpName.setStatus("current")


class _FsAAABackAcctServerConfigSrvIndex_Type(Unsigned32):
    """Custom type fsAAABackAcctServerConfigSrvIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAABackAcctServerConfigSrvIndex_Type.__name__ = "Unsigned32"
_FsAAABackAcctServerConfigSrvIndex_Object = MibTableColumn
fsAAABackAcctServerConfigSrvIndex = _FsAAABackAcctServerConfigSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 2),
    _FsAAABackAcctServerConfigSrvIndex_Type()
)
fsAAABackAcctServerConfigSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigSrvIndex.setStatus("current")
_FsAAABackAcctServerConfigAddress_Type = IpAddress
_FsAAABackAcctServerConfigAddress_Object = MibTableColumn
fsAAABackAcctServerConfigAddress = _FsAAABackAcctServerConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 3),
    _FsAAABackAcctServerConfigAddress_Type()
)
fsAAABackAcctServerConfigAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigAddress.setStatus("current")


class _FsAAABackAcctServerConfigAuthPort_Type(Integer32):
    """Custom type fsAAABackAcctServerConfigAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAABackAcctServerConfigAuthPort_Type.__name__ = "Integer32"
_FsAAABackAcctServerConfigAuthPort_Object = MibTableColumn
fsAAABackAcctServerConfigAuthPort = _FsAAABackAcctServerConfigAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 4),
    _FsAAABackAcctServerConfigAuthPort_Type()
)
fsAAABackAcctServerConfigAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigAuthPort.setStatus("current")


class _FsAAABackAcctServerConfigAcctPort_Type(Integer32):
    """Custom type fsAAABackAcctServerConfigAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsAAABackAcctServerConfigAcctPort_Type.__name__ = "Integer32"
_FsAAABackAcctServerConfigAcctPort_Object = MibTableColumn
fsAAABackAcctServerConfigAcctPort = _FsAAABackAcctServerConfigAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 5),
    _FsAAABackAcctServerConfigAcctPort_Type()
)
fsAAABackAcctServerConfigAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigAcctPort.setStatus("current")


class _FsAAABackAcctServerConfigKeyStr_Type(DisplayString):
    """Custom type fsAAABackAcctServerConfigKeyStr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsAAABackAcctServerConfigKeyStr_Type.__name__ = "DisplayString"
_FsAAABackAcctServerConfigKeyStr_Object = MibTableColumn
fsAAABackAcctServerConfigKeyStr = _FsAAABackAcctServerConfigKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 6),
    _FsAAABackAcctServerConfigKeyStr_Type()
)
fsAAABackAcctServerConfigKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigKeyStr.setStatus("current")
_FsAAABackAcctServerConfigRowStatus_Type = RowStatus
_FsAAABackAcctServerConfigRowStatus_Object = MibTableColumn
fsAAABackAcctServerConfigRowStatus = _FsAAABackAcctServerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 21, 1, 7),
    _FsAAABackAcctServerConfigRowStatus_Type()
)
fsAAABackAcctServerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAAABackAcctServerConfigRowStatus.setStatus("current")


class _FsAAAServerTotalAuthUserCount_Type(Unsigned32):
    """Custom type fsAAAServerTotalAuthUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsAAAServerTotalAuthUserCount_Type.__name__ = "Unsigned32"
_FsAAAServerTotalAuthUserCount_Object = MibScalar
fsAAAServerTotalAuthUserCount = _FsAAAServerTotalAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 22),
    _FsAAAServerTotalAuthUserCount_Type()
)
fsAAAServerTotalAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerTotalAuthUserCount.setStatus("current")


class _FsAAAServerAuthSuccUserCount_Type(Unsigned32):
    """Custom type fsAAAServerAuthSuccUserCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsAAAServerAuthSuccUserCount_Type.__name__ = "Unsigned32"
_FsAAAServerAuthSuccUserCount_Object = MibScalar
fsAAAServerAuthSuccUserCount = _FsAAAServerAuthSuccUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 23),
    _FsAAAServerAuthSuccUserCount_Type()
)
fsAAAServerAuthSuccUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerAuthSuccUserCount.setStatus("current")


class _FsAAAServerDot1xOnlineUserCount_Type(Integer32):
    """Custom type fsAAAServerDot1xOnlineUserCount based on Integer32"""
    defaultValue = 0


_FsAAAServerDot1xOnlineUserCount_Type.__name__ = "Integer32"
_FsAAAServerDot1xOnlineUserCount_Object = MibScalar
fsAAAServerDot1xOnlineUserCount = _FsAAAServerDot1xOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 24),
    _FsAAAServerDot1xOnlineUserCount_Type()
)
fsAAAServerDot1xOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerDot1xOnlineUserCount.setStatus("current")


class _FsAAAServerMacOnlineUserCount_Type(Integer32):
    """Custom type fsAAAServerMacOnlineUserCount based on Integer32"""
    defaultValue = 0


_FsAAAServerMacOnlineUserCount_Type.__name__ = "Integer32"
_FsAAAServerMacOnlineUserCount_Object = MibScalar
fsAAAServerMacOnlineUserCount = _FsAAAServerMacOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 25),
    _FsAAAServerMacOnlineUserCount_Type()
)
fsAAAServerMacOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerMacOnlineUserCount.setStatus("current")


class _FsAAAServerWebOnlineUserCount_Type(Integer32):
    """Custom type fsAAAServerWebOnlineUserCount based on Integer32"""
    defaultValue = 0


_FsAAAServerWebOnlineUserCount_Type.__name__ = "Integer32"
_FsAAAServerWebOnlineUserCount_Object = MibScalar
fsAAAServerWebOnlineUserCount = _FsAAAServerWebOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 26),
    _FsAAAServerWebOnlineUserCount_Type()
)
fsAAAServerWebOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerWebOnlineUserCount.setStatus("current")


class _FsAAAServerTatalOnlineUserCount_Type(Integer32):
    """Custom type fsAAAServerTatalOnlineUserCount based on Integer32"""
    defaultValue = 0


_FsAAAServerTatalOnlineUserCount_Type.__name__ = "Integer32"
_FsAAAServerTatalOnlineUserCount_Object = MibScalar
fsAAAServerTatalOnlineUserCount = _FsAAAServerTatalOnlineUserCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 27),
    _FsAAAServerTatalOnlineUserCount_Type()
)
fsAAAServerTatalOnlineUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerTatalOnlineUserCount.setStatus("current")
_FsAAAServerIfOnlineUserTable_Object = MibTable
fsAAAServerIfOnlineUserTable = _FsAAAServerIfOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28)
)
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserTable.setStatus("current")
_FsAAAServerIfOnlineUserEntry_Object = MibTableRow
fsAAAServerIfOnlineUserEntry = _FsAAAServerIfOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1)
)
fsAAAServerIfOnlineUserEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAAAServerIfOnlineUserIfIndex"),
)
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserEntry.setStatus("current")


class _FsAAAServerIfOnlineUserIfIndex_Type(Unsigned32):
    """Custom type fsAAAServerIfOnlineUserIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerIfOnlineUserIfIndex_Type.__name__ = "Unsigned32"
_FsAAAServerIfOnlineUserIfIndex_Object = MibTableColumn
fsAAAServerIfOnlineUserIfIndex = _FsAAAServerIfOnlineUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1, 1),
    _FsAAAServerIfOnlineUserIfIndex_Type()
)
fsAAAServerIfOnlineUserIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserIfIndex.setStatus("current")


class _FsAAAServerIfOnlineUserDot1xCount_Type(Unsigned32):
    """Custom type fsAAAServerIfOnlineUserDot1xCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerIfOnlineUserDot1xCount_Type.__name__ = "Unsigned32"
_FsAAAServerIfOnlineUserDot1xCount_Object = MibTableColumn
fsAAAServerIfOnlineUserDot1xCount = _FsAAAServerIfOnlineUserDot1xCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1, 2),
    _FsAAAServerIfOnlineUserDot1xCount_Type()
)
fsAAAServerIfOnlineUserDot1xCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserDot1xCount.setStatus("current")


class _FsAAAServerIfOnlineUserWebCount_Type(Unsigned32):
    """Custom type fsAAAServerIfOnlineUserWebCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerIfOnlineUserWebCount_Type.__name__ = "Unsigned32"
_FsAAAServerIfOnlineUserWebCount_Object = MibTableColumn
fsAAAServerIfOnlineUserWebCount = _FsAAAServerIfOnlineUserWebCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1, 3),
    _FsAAAServerIfOnlineUserWebCount_Type()
)
fsAAAServerIfOnlineUserWebCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserWebCount.setStatus("current")


class _FsAAAServerIfOnlineUserMacCount_Type(Unsigned32):
    """Custom type fsAAAServerIfOnlineUserMacCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerIfOnlineUserMacCount_Type.__name__ = "Unsigned32"
_FsAAAServerIfOnlineUserMacCount_Object = MibTableColumn
fsAAAServerIfOnlineUserMacCount = _FsAAAServerIfOnlineUserMacCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1, 4),
    _FsAAAServerIfOnlineUserMacCount_Type()
)
fsAAAServerIfOnlineUserMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserMacCount.setStatus("current")


class _FsAAAServerIfOnlineUserTotalCount_Type(Unsigned32):
    """Custom type fsAAAServerIfOnlineUserTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsAAAServerIfOnlineUserTotalCount_Type.__name__ = "Unsigned32"
_FsAAAServerIfOnlineUserTotalCount_Object = MibTableColumn
fsAAAServerIfOnlineUserTotalCount = _FsAAAServerIfOnlineUserTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 2, 28, 1, 5),
    _FsAAAServerIfOnlineUserTotalCount_Type()
)
fsAAAServerIfOnlineUserTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAAAServerIfOnlineUserTotalCount.setStatus("current")
_FsAuthUserObjects_ObjectIdentity = ObjectIdentity
fsAuthUserObjects = _FsAuthUserObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3)
)
_FsAuthAddrTable_Object = MibTable
fsAuthAddrTable = _FsAuthAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsAuthAddrTable.setStatus("current")
_FsAuthAddrEntry_Object = MibTableRow
fsAuthAddrEntry = _FsAuthAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 1, 1)
)
fsAuthAddrEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAuthPort"),
    (0, "FS-AAA-MIB", "fsAuthMacAddress"),
)
if mibBuilder.loadTexts:
    fsAuthAddrEntry.setStatus("current")
_FsAuthPort_Type = IfIndex
_FsAuthPort_Object = MibTableColumn
fsAuthPort = _FsAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 1, 1, 1),
    _FsAuthPort_Type()
)
fsAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthPort.setStatus("current")
_FsAuthMacAddress_Type = MacAddress
_FsAuthMacAddress_Object = MibTableColumn
fsAuthMacAddress = _FsAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 1, 1, 2),
    _FsAuthMacAddress_Type()
)
fsAuthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthMacAddress.setStatus("current")


class _FsAuthAddrStatus_Type(Integer32):
    """Custom type fsAuthAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_FsAuthAddrStatus_Type.__name__ = "Integer32"
_FsAuthAddrStatus_Object = MibTableColumn
fsAuthAddrStatus = _FsAuthAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 1, 1, 3),
    _FsAuthAddrStatus_Type()
)
fsAuthAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAuthAddrStatus.setStatus("current")
_FsAuthUserTable_Object = MibTable
fsAuthUserTable = _FsAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsAuthUserTable.setStatus("current")
_FsAuthUserEntry_Object = MibTableRow
fsAuthUserEntry = _FsAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1)
)
fsAuthUserEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAuthUserFdbId"),
    (0, "FS-AAA-MIB", "fsAuthUserMacAddress"),
)
if mibBuilder.loadTexts:
    fsAuthUserEntry.setStatus("current")
_FsAuthUserFdbId_Type = Unsigned32
_FsAuthUserFdbId_Object = MibTableColumn
fsAuthUserFdbId = _FsAuthUserFdbId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 1),
    _FsAuthUserFdbId_Type()
)
fsAuthUserFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserFdbId.setStatus("current")
_FsAuthUserMacAddress_Type = MacAddress
_FsAuthUserMacAddress_Object = MibTableColumn
fsAuthUserMacAddress = _FsAuthUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 2),
    _FsAuthUserMacAddress_Type()
)
fsAuthUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserMacAddress.setStatus("current")
_FsAuthUserName_Type = DisplayString
_FsAuthUserName_Object = MibTableColumn
fsAuthUserName = _FsAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 3),
    _FsAuthUserName_Type()
)
fsAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserName.setStatus("current")
_FsAuthUserSessionId_Type = DisplayString
_FsAuthUserSessionId_Object = MibTableColumn
fsAuthUserSessionId = _FsAuthUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 4),
    _FsAuthUserSessionId_Type()
)
fsAuthUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserSessionId.setStatus("current")
_FsAuthUserIpAddr_Type = IpAddress
_FsAuthUserIpAddr_Object = MibTableColumn
fsAuthUserIpAddr = _FsAuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 5),
    _FsAuthUserIpAddr_Type()
)
fsAuthUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserIpAddr.setStatus("current")
_FsAuthUserPort_Type = Integer32
_FsAuthUserPort_Object = MibTableColumn
fsAuthUserPort = _FsAuthUserPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 6),
    _FsAuthUserPort_Type()
)
fsAuthUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthUserPort.setStatus("current")
_FsAuthUserStatus_Type = ConfigStatus
_FsAuthUserStatus_Object = MibTableColumn
fsAuthUserStatus = _FsAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 2, 1, 7),
    _FsAuthUserStatus_Type()
)
fsAuthUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAuthUserStatus.setStatus("current")


class _FsAuthUserForVPNDel_Type(DisplayString):
    """Custom type fsAuthUserForVPNDel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsAuthUserForVPNDel_Type.__name__ = "DisplayString"
_FsAuthUserForVPNDel_Object = MibScalar
fsAuthUserForVPNDel = _FsAuthUserForVPNDel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 3),
    _FsAuthUserForVPNDel_Type()
)
fsAuthUserForVPNDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAuthUserForVPNDel.setStatus("current")
_FsOnlineUserTable_Object = MibTable
fsOnlineUserTable = _FsOnlineUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4)
)
if mibBuilder.loadTexts:
    fsOnlineUserTable.setStatus("current")
_FsOnlineUserEntry_Object = MibTableRow
fsOnlineUserEntry = _FsOnlineUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1)
)
fsOnlineUserEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsOnlineUserSessionId"),
)
if mibBuilder.loadTexts:
    fsOnlineUserEntry.setStatus("current")
_FsOnlineUserSessionId_Type = DisplayString
_FsOnlineUserSessionId_Object = MibTableColumn
fsOnlineUserSessionId = _FsOnlineUserSessionId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 1),
    _FsOnlineUserSessionId_Type()
)
fsOnlineUserSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserSessionId.setStatus("current")
_FsOnlineUserVid_Type = Unsigned32
_FsOnlineUserVid_Object = MibTableColumn
fsOnlineUserVid = _FsOnlineUserVid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 2),
    _FsOnlineUserVid_Type()
)
fsOnlineUserVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserVid.setStatus("current")
_FsOnlineUserMacAddress_Type = MacAddress
_FsOnlineUserMacAddress_Object = MibTableColumn
fsOnlineUserMacAddress = _FsOnlineUserMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 3),
    _FsOnlineUserMacAddress_Type()
)
fsOnlineUserMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserMacAddress.setStatus("current")
_FsOnlineUserPort_Type = Integer32
_FsOnlineUserPort_Object = MibTableColumn
fsOnlineUserPort = _FsOnlineUserPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 4),
    _FsOnlineUserPort_Type()
)
fsOnlineUserPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserPort.setStatus("current")
_FsOnlineUserName_Type = DisplayString
_FsOnlineUserName_Object = MibTableColumn
fsOnlineUserName = _FsOnlineUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 5),
    _FsOnlineUserName_Type()
)
fsOnlineUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserName.setStatus("current")
_FsOnlineUserIpAddr_Type = IpAddress
_FsOnlineUserIpAddr_Object = MibTableColumn
fsOnlineUserIpAddr = _FsOnlineUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 6),
    _FsOnlineUserIpAddr_Type()
)
fsOnlineUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOnlineUserIpAddr.setStatus("current")
_FsOnlineUserStatus_Type = ConfigStatus
_FsOnlineUserStatus_Object = MibTableColumn
fsOnlineUserStatus = _FsOnlineUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 4, 1, 7),
    _FsOnlineUserStatus_Type()
)
fsOnlineUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOnlineUserStatus.setStatus("current")
_FsAaaVersion_Type = Integer32
_FsAaaVersion_Object = MibScalar
fsAaaVersion = _FsAaaVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 3, 5),
    _FsAaaVersion_Type()
)
fsAaaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAaaVersion.setStatus("current")
_FsAuthModeObjects_ObjectIdentity = ObjectIdentity
fsAuthModeObjects = _FsAuthModeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 4)
)


class _FsIpAuthorizationMode_Type(Integer32):
    """Custom type fsIpAuthorizationMode based on Integer32"""
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
        *(("disable", 1),
          ("dhcpServer", 2),
          ("radiusServer", 3),
          ("supplicant", 4),
          ("mixed", 5))
    )


_FsIpAuthorizationMode_Type.__name__ = "Integer32"
_FsIpAuthorizationMode_Object = MibScalar
fsIpAuthorizationMode = _FsIpAuthorizationMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 4, 1),
    _FsIpAuthorizationMode_Type()
)
fsIpAuthorizationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpAuthorizationMode.setStatus("current")
_FsClientProbeObjects_ObjectIdentity = ObjectIdentity
fsClientProbeObjects = _FsClientProbeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 5)
)
_FsClientProbeEnabledStatus_Type = EnabledStatus
_FsClientProbeEnabledStatus_Object = MibScalar
fsClientProbeEnabledStatus = _FsClientProbeEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 5, 1),
    _FsClientProbeEnabledStatus_Type()
)
fsClientProbeEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClientProbeEnabledStatus.setStatus("current")
_FsClientProbeHelloInterval_Type = Unsigned32
_FsClientProbeHelloInterval_Object = MibScalar
fsClientProbeHelloInterval = _FsClientProbeHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 5, 2),
    _FsClientProbeHelloInterval_Type()
)
fsClientProbeHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClientProbeHelloInterval.setStatus("current")
_FsClientProbeAliveInteval_Type = Unsigned32
_FsClientProbeAliveInteval_Object = MibScalar
fsClientProbeAliveInteval = _FsClientProbeAliveInteval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 5, 3),
    _FsClientProbeAliveInteval_Type()
)
fsClientProbeAliveInteval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsClientProbeAliveInteval.setStatus("current")
_FsAAAConfigObjects_ObjectIdentity = ObjectIdentity
fsAAAConfigObjects = _FsAAAConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6)
)
_FsAuthenConfigObjects_ObjectIdentity = ObjectIdentity
fsAuthenConfigObjects = _FsAuthenConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1)
)
_FsAuthenMethodListTable_Object = MibTable
fsAuthenMethodListTable = _FsAuthenMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    fsAuthenMethodListTable.setStatus("current")
_FsAuthenMethodListEntry_Object = MibTableRow
fsAuthenMethodListEntry = _FsAuthenMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1)
)
fsAuthenMethodListEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAuthenMethodListType"),
    (0, "FS-AAA-MIB", "fsAuthenMethodListName"),
)
if mibBuilder.loadTexts:
    fsAuthenMethodListEntry.setStatus("current")


class _FsAuthenMethodListType_Type(Integer32):
    """Custom type fsAuthenMethodListType based on Integer32"""
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
        *(("login", 1),
          ("ppp", 2),
          ("dot1x", 3),
          ("enable", 4),
          ("web", 5),
          ("cmweb", 6),
          ("mt", 7),
          ("general", 8))
    )


_FsAuthenMethodListType_Type.__name__ = "Integer32"
_FsAuthenMethodListType_Object = MibTableColumn
fsAuthenMethodListType = _FsAuthenMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 1),
    _FsAuthenMethodListType_Type()
)
fsAuthenMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenMethodListType.setStatus("current")


class _FsAuthenMethodListName_Type(DisplayString):
    """Custom type fsAuthenMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAuthenMethodListName_Type.__name__ = "DisplayString"
_FsAuthenMethodListName_Object = MibTableColumn
fsAuthenMethodListName = _FsAuthenMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 2),
    _FsAuthenMethodListName_Type()
)
fsAuthenMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenMethodListName.setStatus("current")


class _FsAuthenMethodListString_Type(DisplayString):
    """Custom type fsAuthenMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsAuthenMethodListString_Type.__name__ = "DisplayString"
_FsAuthenMethodListString_Object = MibTableColumn
fsAuthenMethodListString = _FsAuthenMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 3),
    _FsAuthenMethodListString_Type()
)
fsAuthenMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenMethodListString.setStatus("current")
_FsAuthenMethodListRowStatus_Type = RowStatus
_FsAuthenMethodListRowStatus_Object = MibTableColumn
fsAuthenMethodListRowStatus = _FsAuthenMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 1, 1, 1, 4),
    _FsAuthenMethodListRowStatus_Type()
)
fsAuthenMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenMethodListRowStatus.setStatus("current")
_FsAuthorConfigObjects_ObjectIdentity = ObjectIdentity
fsAuthorConfigObjects = _FsAuthorConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2)
)
_FsAuthorMethodListTable_Object = MibTable
fsAuthorMethodListTable = _FsAuthorMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    fsAuthorMethodListTable.setStatus("current")
_FsAuthorMethodListEntry_Object = MibTableRow
fsAuthorMethodListEntry = _FsAuthorMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1)
)
fsAuthorMethodListEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAuthorMethodListType"),
    (0, "FS-AAA-MIB", "fsAuthorMethodListName"),
    (0, "FS-AAA-MIB", "fsAuthorMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    fsAuthorMethodListEntry.setStatus("current")


class _FsAuthorMethodListType_Type(Integer32):
    """Custom type fsAuthorMethodListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("command", 2),
          ("network", 3))
    )


_FsAuthorMethodListType_Type.__name__ = "Integer32"
_FsAuthorMethodListType_Object = MibTableColumn
fsAuthorMethodListType = _FsAuthorMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 1),
    _FsAuthorMethodListType_Type()
)
fsAuthorMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthorMethodListType.setStatus("current")


class _FsAuthorMethodListName_Type(DisplayString):
    """Custom type fsAuthorMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAuthorMethodListName_Type.__name__ = "DisplayString"
_FsAuthorMethodListName_Object = MibTableColumn
fsAuthorMethodListName = _FsAuthorMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 2),
    _FsAuthorMethodListName_Type()
)
fsAuthorMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthorMethodListName.setStatus("current")


class _FsAuthorMethodListCmdLevel_Type(Integer32):
    """Custom type fsAuthorMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsAuthorMethodListCmdLevel_Type.__name__ = "Integer32"
_FsAuthorMethodListCmdLevel_Object = MibTableColumn
fsAuthorMethodListCmdLevel = _FsAuthorMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 3),
    _FsAuthorMethodListCmdLevel_Type()
)
fsAuthorMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthorMethodListCmdLevel.setStatus("current")


class _FsAuthorMethodListString_Type(DisplayString):
    """Custom type fsAuthorMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsAuthorMethodListString_Type.__name__ = "DisplayString"
_FsAuthorMethodListString_Object = MibTableColumn
fsAuthorMethodListString = _FsAuthorMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 4),
    _FsAuthorMethodListString_Type()
)
fsAuthorMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthorMethodListString.setStatus("current")
_FsAuthorMethodListRowStatus_Type = RowStatus
_FsAuthorMethodListRowStatus_Object = MibTableColumn
fsAuthorMethodListRowStatus = _FsAuthorMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 2, 1, 1, 5),
    _FsAuthorMethodListRowStatus_Type()
)
fsAuthorMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthorMethodListRowStatus.setStatus("current")
_FsAcctConfigObjects_ObjectIdentity = ObjectIdentity
fsAcctConfigObjects = _FsAcctConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3)
)
_FsAcctMethodListTable_Object = MibTable
fsAcctMethodListTable = _FsAcctMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    fsAcctMethodListTable.setStatus("current")
_FsAcctMethodListEntry_Object = MibTableRow
fsAcctMethodListEntry = _FsAcctMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1)
)
fsAcctMethodListEntry.setIndexNames(
    (0, "FS-AAA-MIB", "fsAcctMethodListType"),
    (0, "FS-AAA-MIB", "fsAcctMethodListName"),
    (0, "FS-AAA-MIB", "fsAcctMethodListCmdLevel"),
)
if mibBuilder.loadTexts:
    fsAcctMethodListEntry.setStatus("current")


class _FsAcctMethodListType_Type(Integer32):
    """Custom type fsAcctMethodListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exec", 1),
          ("command", 2),
          ("network", 3))
    )


_FsAcctMethodListType_Type.__name__ = "Integer32"
_FsAcctMethodListType_Object = MibTableColumn
fsAcctMethodListType = _FsAcctMethodListType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 1),
    _FsAcctMethodListType_Type()
)
fsAcctMethodListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcctMethodListType.setStatus("current")


class _FsAcctMethodListName_Type(DisplayString):
    """Custom type fsAcctMethodListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsAcctMethodListName_Type.__name__ = "DisplayString"
_FsAcctMethodListName_Object = MibTableColumn
fsAcctMethodListName = _FsAcctMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 2),
    _FsAcctMethodListName_Type()
)
fsAcctMethodListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcctMethodListName.setStatus("current")


class _FsAcctMethodListMode_Type(Integer32):
    """Custom type fsAcctMethodListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start-stop", 1),
          ("stop-only", 2))
    )


_FsAcctMethodListMode_Type.__name__ = "Integer32"
_FsAcctMethodListMode_Object = MibTableColumn
fsAcctMethodListMode = _FsAcctMethodListMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 3),
    _FsAcctMethodListMode_Type()
)
fsAcctMethodListMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAcctMethodListMode.setStatus("current")


class _FsAcctMethodListCmdLevel_Type(Integer32):
    """Custom type fsAcctMethodListCmdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsAcctMethodListCmdLevel_Type.__name__ = "Integer32"
_FsAcctMethodListCmdLevel_Object = MibTableColumn
fsAcctMethodListCmdLevel = _FsAcctMethodListCmdLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 4),
    _FsAcctMethodListCmdLevel_Type()
)
fsAcctMethodListCmdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAcctMethodListCmdLevel.setStatus("current")


class _FsAcctMethodListString_Type(DisplayString):
    """Custom type fsAcctMethodListString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsAcctMethodListString_Type.__name__ = "DisplayString"
_FsAcctMethodListString_Object = MibTableColumn
fsAcctMethodListString = _FsAcctMethodListString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 5),
    _FsAcctMethodListString_Type()
)
fsAcctMethodListString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAcctMethodListString.setStatus("current")
_FsAcctMethodListRowStatus_Type = RowStatus
_FsAcctMethodListRowStatus_Object = MibTableColumn
fsAcctMethodListRowStatus = _FsAcctMethodListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 6, 3, 1, 1, 6),
    _FsAcctMethodListRowStatus_Type()
)
fsAcctMethodListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAcctMethodListRowStatus.setStatus("current")
_FsAAAUserApplyObjects_ObjectIdentity = ObjectIdentity
fsAAAUserApplyObjects = _FsAAAUserApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 7)
)
_FsAAADo1xApplyObjects_ObjectIdentity = ObjectIdentity
fsAAADo1xApplyObjects = _FsAAADo1xApplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 7, 1)
)


class _FsDot1xAuthenMethodList_Type(DisplayString):
    """Custom type fsDot1xAuthenMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsDot1xAuthenMethodList_Type.__name__ = "DisplayString"
_FsDot1xAuthenMethodList_Object = MibScalar
fsDot1xAuthenMethodList = _FsDot1xAuthenMethodList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 7, 1, 1),
    _FsDot1xAuthenMethodList_Type()
)
fsDot1xAuthenMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthenMethodList.setStatus("current")


class _FsDot1xAuthorMethodList_Type(DisplayString):
    """Custom type fsDot1xAuthorMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsDot1xAuthorMethodList_Type.__name__ = "DisplayString"
_FsDot1xAuthorMethodList_Object = MibScalar
fsDot1xAuthorMethodList = _FsDot1xAuthorMethodList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 7, 1, 2),
    _FsDot1xAuthorMethodList_Type()
)
fsDot1xAuthorMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAuthorMethodList.setStatus("current")


class _FsDot1xAcctMethodList_Type(DisplayString):
    """Custom type fsDot1xAcctMethodList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_FsDot1xAcctMethodList_Type.__name__ = "DisplayString"
_FsDot1xAcctMethodList_Object = MibScalar
fsDot1xAcctMethodList = _FsDot1xAcctMethodList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 7, 1, 3),
    _FsDot1xAcctMethodList_Type()
)
fsDot1xAcctMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1xAcctMethodList.setStatus("current")
_FsRdASObjects_ObjectIdentity = ObjectIdentity
fsRdASObjects = _FsRdASObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 8)
)
_FsRdASipInetAddreType_Type = InetAddressType
_FsRdASipInetAddreType_Object = MibScalar
fsRdASipInetAddreType = _FsRdASipInetAddreType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 8, 1),
    _FsRdASipInetAddreType_Type()
)
fsRdASipInetAddreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRdASipInetAddreType.setStatus("current")
_FsRdASipInsetAddres_Type = InetAddress
_FsRdASipInsetAddres_Object = MibScalar
fsRdASipInsetAddres = _FsRdASipInsetAddres_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 8, 2),
    _FsRdASipInsetAddres_Type()
)
fsRdASipInsetAddres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRdASipInsetAddres.setStatus("current")
_FsAAAMIBConformance_ObjectIdentity = ObjectIdentity
fsAAAMIBConformance = _FsAAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2)
)
_FsAAAMIBCompliances_ObjectIdentity = ObjectIdentity
fsAAAMIBCompliances = _FsAAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 1)
)
_FsAAAMIBGroups_ObjectIdentity = ObjectIdentity
fsAAAMIBGroups = _FsAAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2)
)

# Managed Objects groups

fsDot1xAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 1)
)
fsDot1xAuthMIBGroup.setObjects(
      *(("FS-AAA-MIB", "fsDot1xAuthStatus"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsQuietPeriod"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsTxPeriod"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsSuppTimeout"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsServerTimeout"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsMaxReq"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsReAuthPeriod"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsReAuthEnable"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsConfigFdbId"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsConfigAddr"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsPaeState"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsBackendAuthState"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsAuthControlledPortStatus"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsKeyTxEnabled"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsIfIndex"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsStatsFdbId"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsStatsAddr"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolFramesTx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolFSFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolLogoffFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolRespIdFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolRespFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolReqIdFramesTx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapolReqFramesTx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsInvalidEapolFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsEapLengthErrorFramesRx"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsLastEapolFrameVersion"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsLastEapolFrameSource"),
        ("FS-AAA-MIB", "fsDot1xCurrentUserNumber"),
        ("FS-AAA-MIB", "fsDot1xCurrentAuthenticatedUserNumber"),
        ("FS-AAA-MIB", "fsDot1xAuthObjectsMaxReauth"),
        ("FS-AAA-MIB", "fsAuthIf"),
        ("FS-AAA-MIB", "fsAuthIfStatus"),
        ("FS-AAA-MIB", "fsAuthenticationMode"),
        ("FS-AAA-MIB", "fsDot1xPseudoSrcmac"),
        ("FS-AAA-MIB", "fsDot1xAbnormalOfflineUserCount"),
        ("FS-AAA-MIB", "fsDot1xTotalAuthUserCount"),
        ("FS-AAA-MIB", "fsDot1xAuthSuccUserCount"),
        ("FS-AAA-MIB", "fsDot1xAuthFailUserCount"))
)
if mibBuilder.loadTexts:
    fsDot1xAuthMIBGroup.setStatus("current")

fsAAAServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 2)
)
fsAAAServerMIBGroup.setObjects(
      *(("FS-AAA-MIB", "fsAAAServerAuthPort"),
        ("FS-AAA-MIB", "fsAAAServerAcctPort"),
        ("FS-AAA-MIB", "fsAAAServerRadiusKeyStr"),
        ("FS-AAA-MIB", "fsAAAServerTacplusKeyStr"),
        ("FS-AAA-MIB", "fsAAAServerConfigAddressType"),
        ("FS-AAA-MIB", "fsAAAServerConfigAddress"),
        ("FS-AAA-MIB", "fsAAAServerConfigAuthPort"),
        ("FS-AAA-MIB", "fsAAAServerConfigAcctPort"),
        ("FS-AAA-MIB", "fsAAAServerConfigKeyStr"),
        ("FS-AAA-MIB", "fsAAAServerConfigRowStatus"))
)
if mibBuilder.loadTexts:
    fsAAAServerMIBGroup.setStatus("current")

fsAuthAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 3)
)
fsAuthAddrMIBGroup.setObjects(
      *(("FS-AAA-MIB", "fsAuthMacAddress"),
        ("FS-AAA-MIB", "fsAuthPort"),
        ("FS-AAA-MIB", "fsAuthAddrStatus"),
        ("FS-AAA-MIB", "fsAuthUserFdbId"),
        ("FS-AAA-MIB", "fsAuthUserMacAddress"),
        ("FS-AAA-MIB", "fsAuthUserName"),
        ("FS-AAA-MIB", "fsAuthUserSessionId"),
        ("FS-AAA-MIB", "fsAuthUserIpAddr"),
        ("FS-AAA-MIB", "fsAuthUserPort"),
        ("FS-AAA-MIB", "fsAuthUserStatus"))
)
if mibBuilder.loadTexts:
    fsAuthAddrMIBGroup.setStatus("current")

fsAuthModeMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 4)
)
fsAuthModeMIBGroup.setObjects(
    ("FS-AAA-MIB", "fsIpAuthorizationMode")
)
if mibBuilder.loadTexts:
    fsAuthModeMIBGroup.setStatus("current")

fsClientProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 5)
)
fsClientProbeGroup.setObjects(
      *(("FS-AAA-MIB", "fsClientProbeEnabledStatus"),
        ("FS-AAA-MIB", "fsClientProbeHelloInterval"),
        ("FS-AAA-MIB", "fsClientProbeAliveInteval"))
)
if mibBuilder.loadTexts:
    fsClientProbeGroup.setStatus("current")

fsAAAConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 6)
)
fsAAAConfigMIBGroup.setObjects(
      *(("FS-AAA-MIB", "fsAuthenMethodListType"),
        ("FS-AAA-MIB", "fsAuthenMethodListName"),
        ("FS-AAA-MIB", "fsAuthenMethodListString"),
        ("FS-AAA-MIB", "fsAuthenMethodListRowStatus"),
        ("FS-AAA-MIB", "fsAuthorMethodListType"),
        ("FS-AAA-MIB", "fsAuthorMethodListName"),
        ("FS-AAA-MIB", "fsAuthorMethodListCmdLevel"),
        ("FS-AAA-MIB", "fsAuthorMethodListString"),
        ("FS-AAA-MIB", "fsAuthorMethodListRowStatus"),
        ("FS-AAA-MIB", "fsAcctMethodListType"),
        ("FS-AAA-MIB", "fsAcctMethodListName"),
        ("FS-AAA-MIB", "fsAcctMethodListMode"),
        ("FS-AAA-MIB", "fsAcctMethodListCmdLevel"),
        ("FS-AAA-MIB", "fsAcctMethodListString"),
        ("FS-AAA-MIB", "fsAcctMethodListRowStatus"),
        ("FS-AAA-MIB", "fsAAARadiusGroupName"),
        ("FS-AAA-MIB", "fsAAARadiusGroupVrf"),
        ("FS-AAA-MIB", "fsAAARadiusGroupRowStatus"),
        ("FS-AAA-MIB", "fsAAARadiusGroupServerAddressType"),
        ("FS-AAA-MIB", "fsAAARadiusGroupServerAddress"),
        ("FS-AAA-MIB", "fsAAARadiusGroupServerAuthPort"),
        ("FS-AAA-MIB", "fsAAARadiusGroupServerAcctPort"),
        ("FS-AAA-MIB", "fsAAARadiusGroupServerRowStatus"))
)
if mibBuilder.loadTexts:
    fsAAAConfigMIBGroup.setStatus("current")

fsAAAUserApplyMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 7)
)
fsAAAUserApplyMIBGroup.setObjects(
      *(("FS-AAA-MIB", "fsDot1xAuthenMethodList"),
        ("FS-AAA-MIB", "fsDot1xAuthorMethodList"),
        ("FS-AAA-MIB", "fsDot1xAcctMethodList"))
)
if mibBuilder.loadTexts:
    fsAAAUserApplyMIBGroup.setStatus("current")

fsRdASGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 2, 8)
)
fsRdASGroup.setObjects(
      *(("FS-AAA-MIB", "fsRdASipInetAddreType"),
        ("FS-AAA-MIB", "fsRdASipInsetAddres"))
)
if mibBuilder.loadTexts:
    fsRdASGroup.setStatus("current")


# Notification objects

fsRadiusAuthServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 0, 1)
)
fsRadiusAuthServerDownTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    fsRadiusAuthServerDownTrap.setStatus(
        "current"
    )

fsRadiusAccServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 0, 2)
)
fsRadiusAccServerDownTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    fsRadiusAccServerDownTrap.setStatus(
        "current"
    )

fsRadiusAuthServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 0, 3)
)
fsRadiusAuthServerRecoverTrap.setObjects(
      *(("RADIUS-AUTH-CLIENT-MIB", "radiusAuthServerAddress"),
        ("RADIUS-AUTH-CLIENT-MIB", "radiusAuthClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    fsRadiusAuthServerRecoverTrap.setStatus(
        "current"
    )

fsRadiusAccServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 0, 4)
)
fsRadiusAccServerRecoverTrap.setObjects(
      *(("RADIUS-ACC-CLIENT-MIB", "radiusAccServerAddress"),
        ("RADIUS-ACC-CLIENT-MIB", "radiusAccClientServerPortNumber"))
)
if mibBuilder.loadTexts:
    fsRadiusAccServerRecoverTrap.setStatus(
        "current"
    )

fsDot1xUserMgmtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 2, 1)
)
fsDot1xUserMgmtTrap.setObjects(
      *(("FS-AAA-MIB", "fsDot1xUserMac"),
        ("FS-AAA-MIB", "fsDot1xUserName"),
        ("FS-AAA-MIB", "fsDot1xUserIp"),
        ("FS-AAA-MIB", "fsDot1xUserIpv6"),
        ("FS-AAA-MIB", "fsDot1xUserWlanId"),
        ("FS-AAA-MIB", "fsDot1xUserVlanId"),
        ("FS-AAA-MIB", "fsDot1xUserSsid"),
        ("FS-AAA-MIB", "fsDot1xUserApMac"),
        ("FS-AAA-MIB", "fsDot1xUserTerminalType"),
        ("FS-AAA-MIB", "fsDot1xUserOperType"),
        ("FS-AAA-MIB", "fsDot1xUserTerminateCause"),
        ("FS-AAA-MIB", "fsDot1xUserReplyMessage"),
        ("FS-AAA-MIB", "fsDot1xUserIfIndex"))
)
if mibBuilder.loadTexts:
    fsDot1xUserMgmtTrap.setStatus(
        "current"
    )

fsDot1xWiredUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 1, 1, 22, 2, 2)
)
fsDot1xWiredUserTrap.setObjects(
      *(("FS-AAA-MIB", "fsDot1xUserMac"),
        ("FS-AAA-MIB", "fsDot1xUserName"),
        ("FS-AAA-MIB", "fsDot1xUserIfIndex"),
        ("FS-AAA-MIB", "fsDot1xUserVlanId"),
        ("FS-AAA-MIB", "fsDot1xUserIp"),
        ("FS-AAA-MIB", "fsDot1xUserIpv6"),
        ("FS-AAA-MIB", "fsDot1xUserOperType"),
        ("FS-AAA-MIB", "fsDot1xUserTerminateCause"))
)
if mibBuilder.loadTexts:
    fsDot1xWiredUserTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsAAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 19, 2, 1, 1)
)
fsAAAMIBCompliance.setObjects(
      *(("FS-AAA-MIB", "fsDot1xAuthMIBGroup"),
        ("FS-AAA-MIB", "fsAAAServerMIBGroup"),
        ("FS-AAA-MIB", "fsAuthAddrMIBGroup"),
        ("FS-AAA-MIB", "fsAuthModeMIBGroup"),
        ("FS-AAA-MIB", "fsAAAConfigMIBGroup"),
        ("FS-AAA-MIB", "fsAAAUserApplyMIBGroup"),
        ("FS-AAA-MIB", "fsRdASGroup"),
        ("FS-AAA-MIB", "fsClientProbeGroup"))
)
if mibBuilder.loadTexts:
    fsAAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-AAA-MIB",
    **{"fsAAAMIB": fsAAAMIB,
       "fsRadiusServerTrap": fsRadiusServerTrap,
       "fsRadiusAuthServerDownTrap": fsRadiusAuthServerDownTrap,
       "fsRadiusAccServerDownTrap": fsRadiusAccServerDownTrap,
       "fsRadiusAuthServerRecoverTrap": fsRadiusAuthServerRecoverTrap,
       "fsRadiusAccServerRecoverTrap": fsRadiusAccServerRecoverTrap,
       "fsAAAMIBObjects": fsAAAMIBObjects,
       "fsDot1xAuthObjects": fsDot1xAuthObjects,
       "fsDot1xAuthStatus": fsDot1xAuthStatus,
       "fsDot1xAuthObjectsQuietPeriod": fsDot1xAuthObjectsQuietPeriod,
       "fsDot1xAuthObjectsTxPeriod": fsDot1xAuthObjectsTxPeriod,
       "fsDot1xAuthObjectsSuppTimeout": fsDot1xAuthObjectsSuppTimeout,
       "fsDot1xAuthObjectsServerTimeout": fsDot1xAuthObjectsServerTimeout,
       "fsDot1xAuthObjectsMaxReq": fsDot1xAuthObjectsMaxReq,
       "fsDot1xAuthObjectsReAuthPeriod": fsDot1xAuthObjectsReAuthPeriod,
       "fsDot1xAuthObjectsMaxReauth": fsDot1xAuthObjectsMaxReauth,
       "fsDot1xAuthObjectsReAuthEnable": fsDot1xAuthObjectsReAuthEnable,
       "fsDot1xAuthObjectsConfigTable": fsDot1xAuthObjectsConfigTable,
       "fsDot1xAuthObjectsConfigEntry": fsDot1xAuthObjectsConfigEntry,
       "fsDot1xAuthObjectsConfigFdbId": fsDot1xAuthObjectsConfigFdbId,
       "fsDot1xAuthObjectsConfigAddr": fsDot1xAuthObjectsConfigAddr,
       "fsDot1xAuthObjectsPaeState": fsDot1xAuthObjectsPaeState,
       "fsDot1xAuthObjectsBackendAuthState": fsDot1xAuthObjectsBackendAuthState,
       "fsDot1xAuthObjectsAuthControlledPortStatus": fsDot1xAuthObjectsAuthControlledPortStatus,
       "fsDot1xAuthObjectsKeyTxEnabled": fsDot1xAuthObjectsKeyTxEnabled,
       "fsDot1xAuthObjectsIfIndex": fsDot1xAuthObjectsIfIndex,
       "fsDot1xAuthObjectsStatsTable": fsDot1xAuthObjectsStatsTable,
       "fsDot1xAuthStatsEntry": fsDot1xAuthStatsEntry,
       "fsDot1xAuthObjectsStatsFdbId": fsDot1xAuthObjectsStatsFdbId,
       "fsDot1xAuthObjectsStatsAddr": fsDot1xAuthObjectsStatsAddr,
       "fsDot1xAuthObjectsEapolFramesRx": fsDot1xAuthObjectsEapolFramesRx,
       "fsDot1xAuthObjectsEapolFramesTx": fsDot1xAuthObjectsEapolFramesTx,
       "fsDot1xAuthObjectsEapolFSFramesRx": fsDot1xAuthObjectsEapolFSFramesRx,
       "fsDot1xAuthObjectsEapolLogoffFramesRx": fsDot1xAuthObjectsEapolLogoffFramesRx,
       "fsDot1xAuthObjectsEapolRespIdFramesRx": fsDot1xAuthObjectsEapolRespIdFramesRx,
       "fsDot1xAuthObjectsEapolRespFramesRx": fsDot1xAuthObjectsEapolRespFramesRx,
       "fsDot1xAuthObjectsEapolReqIdFramesTx": fsDot1xAuthObjectsEapolReqIdFramesTx,
       "fsDot1xAuthObjectsEapolReqFramesTx": fsDot1xAuthObjectsEapolReqFramesTx,
       "fsDot1xAuthObjectsInvalidEapolFramesRx": fsDot1xAuthObjectsInvalidEapolFramesRx,
       "fsDot1xAuthObjectsEapLengthErrorFramesRx": fsDot1xAuthObjectsEapLengthErrorFramesRx,
       "fsDot1xAuthObjectsLastEapolFrameVersion": fsDot1xAuthObjectsLastEapolFrameVersion,
       "fsDot1xAuthObjectsLastEapolFrameSource": fsDot1xAuthObjectsLastEapolFrameSource,
       "fsDot1xCurrentUserNumber": fsDot1xCurrentUserNumber,
       "fsDot1xCurrentAuthenticatedUserNumber": fsDot1xCurrentAuthenticatedUserNumber,
       "fsDot1xAccountStatus": fsDot1xAccountStatus,
       "fsAuthIfTable": fsAuthIfTable,
       "fsAuthIfEntry": fsAuthIfEntry,
       "fsAuthIf": fsAuthIf,
       "fsAuthIfStatus": fsAuthIfStatus,
       "fsAuthenticationMode": fsAuthenticationMode,
       "fsDot1xAccountUpdateStatus": fsDot1xAccountUpdateStatus,
       "fsDot1xAcctInterimInterval": fsDot1xAcctInterimInterval,
       "fsDot1xEapolTagEnabled": fsDot1xEapolTagEnabled,
       "fsDot1xIfUserMaxTable": fsDot1xIfUserMaxTable,
       "fsDot1xIfUserMaxEntry": fsDot1xIfUserMaxEntry,
       "fsDot1xIfUserMaxIndex": fsDot1xIfUserMaxIndex,
       "fsDot1xIfUserMaxNum": fsDot1xIfUserMaxNum,
       "fsDot1xPseudoSrcmac": fsDot1xPseudoSrcmac,
       "fsDot1xUserMIB": fsDot1xUserMIB,
       "fsDot1xUserTrapsObjects": fsDot1xUserTrapsObjects,
       "fsDot1xUserMac": fsDot1xUserMac,
       "fsDot1xUserName": fsDot1xUserName,
       "fsDot1xUserIp": fsDot1xUserIp,
       "fsDot1xUserIpv6": fsDot1xUserIpv6,
       "fsDot1xUserWlanId": fsDot1xUserWlanId,
       "fsDot1xUserVlanId": fsDot1xUserVlanId,
       "fsDot1xUserSsid": fsDot1xUserSsid,
       "fsDot1xUserApMac": fsDot1xUserApMac,
       "fsDot1xUserTerminalType": fsDot1xUserTerminalType,
       "fsDot1xUserOperType": fsDot1xUserOperType,
       "fsDot1xUserTerminateCause": fsDot1xUserTerminateCause,
       "fsDot1xUserReplyMessage": fsDot1xUserReplyMessage,
       "fsDot1xUserIfIndex": fsDot1xUserIfIndex,
       "fsDot1xUserTraps": fsDot1xUserTraps,
       "fsDot1xUserMgmtTrap": fsDot1xUserMgmtTrap,
       "fsDot1xWiredUserTrap": fsDot1xWiredUserTrap,
       "fsDot1xOnlineUserTable": fsDot1xOnlineUserTable,
       "fsDot1xOnlineUserEntry": fsDot1xOnlineUserEntry,
       "fsDot1xOnlineUserID": fsDot1xOnlineUserID,
       "fsDot1xOnlineUserName": fsDot1xOnlineUserName,
       "fsDot1xOnlineUserMacAddr": fsDot1xOnlineUserMacAddr,
       "fsDot1xOnlineUserIfIndex": fsDot1xOnlineUserIfIndex,
       "fsDot1xOnlineUserVlanId": fsDot1xOnlineUserVlanId,
       "fsDot1xOnlineUserIp": fsDot1xOnlineUserIp,
       "fsDot1xOnlineUserIpv6": fsDot1xOnlineUserIpv6,
       "fsDot1xAbnormalOfflineUserCount": fsDot1xAbnormalOfflineUserCount,
       "fsDot1xTotalAuthUserCount": fsDot1xTotalAuthUserCount,
       "fsDot1xAuthSuccUserCount": fsDot1xAuthSuccUserCount,
       "fsDot1xAuthFailUserCount": fsDot1xAuthFailUserCount,
       "fsAAAServerObjects": fsAAAServerObjects,
       "fsAAAServerAuthPort": fsAAAServerAuthPort,
       "fsAAAServerAcctPort": fsAAAServerAcctPort,
       "fsAAAServerRadiusKeyStr": fsAAAServerRadiusKeyStr,
       "fsAAAServerTacplusKeyStr": fsAAAServerTacplusKeyStr,
       "fsAAAServerConfigTable": fsAAAServerConfigTable,
       "fsAAAServerConfigEntry": fsAAAServerConfigEntry,
       "fsAAAServerConfigProtocol": fsAAAServerConfigProtocol,
       "fsAAAServerConfigIndex": fsAAAServerConfigIndex,
       "fsAAAServerConfigAddressType": fsAAAServerConfigAddressType,
       "fsAAAServerConfigAddress": fsAAAServerConfigAddress,
       "fsAAAServerConfigAuthPort": fsAAAServerConfigAuthPort,
       "fsAAAServerConfigAcctPort": fsAAAServerConfigAcctPort,
       "fsAAAServerConfigKeyStr": fsAAAServerConfigKeyStr,
       "fsAAAServerConfigRowStatus": fsAAAServerConfigRowStatus,
       "fsAAARadiusGroupTable": fsAAARadiusGroupTable,
       "fsAAARadiusGroupEntry": fsAAARadiusGroupEntry,
       "fsAAARadiusGroupName": fsAAARadiusGroupName,
       "fsAAARadiusGroupVrf": fsAAARadiusGroupVrf,
       "fsAAARadiusGroupRowStatus": fsAAARadiusGroupRowStatus,
       "fsAAARadiusGroupServerTable": fsAAARadiusGroupServerTable,
       "fsAAARadiusGroupServerEntry": fsAAARadiusGroupServerEntry,
       "fsAAARadiusGroupServerIndex": fsAAARadiusGroupServerIndex,
       "fsAAARadiusGroupServerAddressType": fsAAARadiusGroupServerAddressType,
       "fsAAARadiusGroupServerAddress": fsAAARadiusGroupServerAddress,
       "fsAAARadiusGroupServerAuthPort": fsAAARadiusGroupServerAuthPort,
       "fsAAARadiusGroupServerAcctPort": fsAAARadiusGroupServerAcctPort,
       "fsAAARadiusGroupServerRowStatus": fsAAARadiusGroupServerRowStatus,
       "fsAAAServerTotalOnlineCount": fsAAAServerTotalOnlineCount,
       "fsAAAServerAbnormalOffline": fsAAAServerAbnormalOffline,
       "fsAAAServerRadiusAuthReqCount": fsAAAServerRadiusAuthReqCount,
       "fsAAAServerRadiusAuthRespCount": fsAAAServerRadiusAuthRespCount,
       "fsAAAServerRadiusAuthSuccessCount": fsAAAServerRadiusAuthSuccessCount,
       "fsAAAServerCurrOnlineUserCount": fsAAAServerCurrOnlineUserCount,
       "fsAAAMasterAuthenServerConfigTable": fsAAAMasterAuthenServerConfigTable,
       "fsAAAMasterAuthenServerConfigEntry": fsAAAMasterAuthenServerConfigEntry,
       "fsAAAMasterAuthenServerConfigGrpName": fsAAAMasterAuthenServerConfigGrpName,
       "fsAAAMasterAuthenServerConfigSrvIndex": fsAAAMasterAuthenServerConfigSrvIndex,
       "fsAAAMasterAuthenServerConfigAddress": fsAAAMasterAuthenServerConfigAddress,
       "fsAAAMasterAuthenServerConfigAuthPort": fsAAAMasterAuthenServerConfigAuthPort,
       "fsAAAMasterAuthenServerConfigAcctPort": fsAAAMasterAuthenServerConfigAcctPort,
       "fsAAAMasterAuthenServerConfigKeyStr": fsAAAMasterAuthenServerConfigKeyStr,
       "fsAAAMasterAuthenServerConfigRowStatus": fsAAAMasterAuthenServerConfigRowStatus,
       "fsAAABackAuthenServerConfigTable": fsAAABackAuthenServerConfigTable,
       "fsAAABackAuthenServerConfigEntry": fsAAABackAuthenServerConfigEntry,
       "fsAAABackAuthenServerConfigGrpName": fsAAABackAuthenServerConfigGrpName,
       "fsAAABackAuthenServerConfigSrvIndex": fsAAABackAuthenServerConfigSrvIndex,
       "fsAAABackAuthenServerConfigAddress": fsAAABackAuthenServerConfigAddress,
       "fsAAABackAuthenServerConfigAuthPort": fsAAABackAuthenServerConfigAuthPort,
       "fsAAABackAuthenServerConfigAcctPort": fsAAABackAuthenServerConfigAcctPort,
       "fsAAABackAuthenServerConfigKeyStr": fsAAABackAuthenServerConfigKeyStr,
       "fsAAABackAuthenServerConfigRowStatus": fsAAABackAuthenServerConfigRowStatus,
       "fsAAAMasterAcctServerConfigTable": fsAAAMasterAcctServerConfigTable,
       "fsAAAMasterAcctServerConfigEntry": fsAAAMasterAcctServerConfigEntry,
       "fsAAAMasterAcctServerConfigGrpName": fsAAAMasterAcctServerConfigGrpName,
       "fsAAAMasterAcctServerConfigSrvIndex": fsAAAMasterAcctServerConfigSrvIndex,
       "fsAAAMasterAcctServerConfigAddress": fsAAAMasterAcctServerConfigAddress,
       "fsAAAMasterAcctServerConfigAuthPort": fsAAAMasterAcctServerConfigAuthPort,
       "fsAAAMasterAcctServerConfigAcctPort": fsAAAMasterAcctServerConfigAcctPort,
       "fsAAAMasterAcctServerConfigKeyStr": fsAAAMasterAcctServerConfigKeyStr,
       "fsAAAMasterAcctServerConfigRowStatus": fsAAAMasterAcctServerConfigRowStatus,
       "fsAAABackAcctServerConfigTable": fsAAABackAcctServerConfigTable,
       "fsAAABackAcctServerConfigEntry": fsAAABackAcctServerConfigEntry,
       "fsAAABackAcctServerConfigGrpName": fsAAABackAcctServerConfigGrpName,
       "fsAAABackAcctServerConfigSrvIndex": fsAAABackAcctServerConfigSrvIndex,
       "fsAAABackAcctServerConfigAddress": fsAAABackAcctServerConfigAddress,
       "fsAAABackAcctServerConfigAuthPort": fsAAABackAcctServerConfigAuthPort,
       "fsAAABackAcctServerConfigAcctPort": fsAAABackAcctServerConfigAcctPort,
       "fsAAABackAcctServerConfigKeyStr": fsAAABackAcctServerConfigKeyStr,
       "fsAAABackAcctServerConfigRowStatus": fsAAABackAcctServerConfigRowStatus,
       "fsAAAServerTotalAuthUserCount": fsAAAServerTotalAuthUserCount,
       "fsAAAServerAuthSuccUserCount": fsAAAServerAuthSuccUserCount,
       "fsAAAServerDot1xOnlineUserCount": fsAAAServerDot1xOnlineUserCount,
       "fsAAAServerMacOnlineUserCount": fsAAAServerMacOnlineUserCount,
       "fsAAAServerWebOnlineUserCount": fsAAAServerWebOnlineUserCount,
       "fsAAAServerTatalOnlineUserCount": fsAAAServerTatalOnlineUserCount,
       "fsAAAServerIfOnlineUserTable": fsAAAServerIfOnlineUserTable,
       "fsAAAServerIfOnlineUserEntry": fsAAAServerIfOnlineUserEntry,
       "fsAAAServerIfOnlineUserIfIndex": fsAAAServerIfOnlineUserIfIndex,
       "fsAAAServerIfOnlineUserDot1xCount": fsAAAServerIfOnlineUserDot1xCount,
       "fsAAAServerIfOnlineUserWebCount": fsAAAServerIfOnlineUserWebCount,
       "fsAAAServerIfOnlineUserMacCount": fsAAAServerIfOnlineUserMacCount,
       "fsAAAServerIfOnlineUserTotalCount": fsAAAServerIfOnlineUserTotalCount,
       "fsAuthUserObjects": fsAuthUserObjects,
       "fsAuthAddrTable": fsAuthAddrTable,
       "fsAuthAddrEntry": fsAuthAddrEntry,
       "fsAuthPort": fsAuthPort,
       "fsAuthMacAddress": fsAuthMacAddress,
       "fsAuthAddrStatus": fsAuthAddrStatus,
       "fsAuthUserTable": fsAuthUserTable,
       "fsAuthUserEntry": fsAuthUserEntry,
       "fsAuthUserFdbId": fsAuthUserFdbId,
       "fsAuthUserMacAddress": fsAuthUserMacAddress,
       "fsAuthUserName": fsAuthUserName,
       "fsAuthUserSessionId": fsAuthUserSessionId,
       "fsAuthUserIpAddr": fsAuthUserIpAddr,
       "fsAuthUserPort": fsAuthUserPort,
       "fsAuthUserStatus": fsAuthUserStatus,
       "fsAuthUserForVPNDel": fsAuthUserForVPNDel,
       "fsOnlineUserTable": fsOnlineUserTable,
       "fsOnlineUserEntry": fsOnlineUserEntry,
       "fsOnlineUserSessionId": fsOnlineUserSessionId,
       "fsOnlineUserVid": fsOnlineUserVid,
       "fsOnlineUserMacAddress": fsOnlineUserMacAddress,
       "fsOnlineUserPort": fsOnlineUserPort,
       "fsOnlineUserName": fsOnlineUserName,
       "fsOnlineUserIpAddr": fsOnlineUserIpAddr,
       "fsOnlineUserStatus": fsOnlineUserStatus,
       "fsAaaVersion": fsAaaVersion,
       "fsAuthModeObjects": fsAuthModeObjects,
       "fsIpAuthorizationMode": fsIpAuthorizationMode,
       "fsClientProbeObjects": fsClientProbeObjects,
       "fsClientProbeEnabledStatus": fsClientProbeEnabledStatus,
       "fsClientProbeHelloInterval": fsClientProbeHelloInterval,
       "fsClientProbeAliveInteval": fsClientProbeAliveInteval,
       "fsAAAConfigObjects": fsAAAConfigObjects,
       "fsAuthenConfigObjects": fsAuthenConfigObjects,
       "fsAuthenMethodListTable": fsAuthenMethodListTable,
       "fsAuthenMethodListEntry": fsAuthenMethodListEntry,
       "fsAuthenMethodListType": fsAuthenMethodListType,
       "fsAuthenMethodListName": fsAuthenMethodListName,
       "fsAuthenMethodListString": fsAuthenMethodListString,
       "fsAuthenMethodListRowStatus": fsAuthenMethodListRowStatus,
       "fsAuthorConfigObjects": fsAuthorConfigObjects,
       "fsAuthorMethodListTable": fsAuthorMethodListTable,
       "fsAuthorMethodListEntry": fsAuthorMethodListEntry,
       "fsAuthorMethodListType": fsAuthorMethodListType,
       "fsAuthorMethodListName": fsAuthorMethodListName,
       "fsAuthorMethodListCmdLevel": fsAuthorMethodListCmdLevel,
       "fsAuthorMethodListString": fsAuthorMethodListString,
       "fsAuthorMethodListRowStatus": fsAuthorMethodListRowStatus,
       "fsAcctConfigObjects": fsAcctConfigObjects,
       "fsAcctMethodListTable": fsAcctMethodListTable,
       "fsAcctMethodListEntry": fsAcctMethodListEntry,
       "fsAcctMethodListType": fsAcctMethodListType,
       "fsAcctMethodListName": fsAcctMethodListName,
       "fsAcctMethodListMode": fsAcctMethodListMode,
       "fsAcctMethodListCmdLevel": fsAcctMethodListCmdLevel,
       "fsAcctMethodListString": fsAcctMethodListString,
       "fsAcctMethodListRowStatus": fsAcctMethodListRowStatus,
       "fsAAAUserApplyObjects": fsAAAUserApplyObjects,
       "fsAAADo1xApplyObjects": fsAAADo1xApplyObjects,
       "fsDot1xAuthenMethodList": fsDot1xAuthenMethodList,
       "fsDot1xAuthorMethodList": fsDot1xAuthorMethodList,
       "fsDot1xAcctMethodList": fsDot1xAcctMethodList,
       "fsRdASObjects": fsRdASObjects,
       "fsRdASipInetAddreType": fsRdASipInetAddreType,
       "fsRdASipInsetAddres": fsRdASipInsetAddres,
       "fsAAAMIBConformance": fsAAAMIBConformance,
       "fsAAAMIBCompliances": fsAAAMIBCompliances,
       "fsAAAMIBCompliance": fsAAAMIBCompliance,
       "fsAAAMIBGroups": fsAAAMIBGroups,
       "fsDot1xAuthMIBGroup": fsDot1xAuthMIBGroup,
       "fsAAAServerMIBGroup": fsAAAServerMIBGroup,
       "fsAuthAddrMIBGroup": fsAuthAddrMIBGroup,
       "fsAuthModeMIBGroup": fsAuthModeMIBGroup,
       "fsClientProbeGroup": fsClientProbeGroup,
       "fsAAAConfigMIBGroup": fsAAAConfigMIBGroup,
       "fsAAAUserApplyMIBGroup": fsAAAUserApplyMIBGroup,
       "fsRdASGroup": fsRdASGroup}
)
